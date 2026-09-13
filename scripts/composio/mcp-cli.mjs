#!/usr/bin/env node
/**
 * mcp-cli.mjs — zero-dependency MCP "Streamable HTTP" client for Composio.
 *
 * Protocol flow: initialize -> notifications/initialized -> tools/list | tools/call
 * Handles both application/json and text/event-stream (SSE) responses,
 * MCP session ids, and protocol-version negotiation fallback.
 *
 * Usage:
 *   node mcp-cli.mjs tools [--json]
 *   node mcp-cli.mjs call <TOOL_SLUG> [--args '<json-object>'] [--json]
 *
 * Environment:
 *   COMPOSIO_CONSUMER_KEY   required. Sent only as an HTTP header; NEVER printed.
 *   COMPOSIO_MCP_URL        optional. Default: https://connect.composio.dev/mcp
 *   COMPOSIO_TIMEOUT_MS     optional. Per-request timeout. Default: 90000
 *   MCP_DEBUG=1             optional. Print stack traces on failure.
 *
 * Exit codes:
 *   0 success | 1 remote/API/tool error | 2 local usage/config error
 *
 * NOTE: composio.dev hosts are unreachable from the Arena sandbox by design.
 * This script is meant to run inside the "Composio Bridge" GitHub Action.
 */

const DEFAULT_URL = 'https://connect.composio.dev/mcp';
const TIMEOUT_MS = Number(process.env.COMPOSIO_TIMEOUT_MS || 90000);
const PROTOCOL_VERSIONS = ['2025-06-18', '2025-03-26', '2024-11-05'];

const KEY = (process.env.COMPOSIO_CONSUMER_KEY || '').trim();
const BASE_URL = (process.env.COMPOSIO_MCP_URL || DEFAULT_URL).trim();

/* ---------- output helpers (every string is redacted before printing) ---- */

function redact(value) {
  if (typeof value !== 'string') return value;
  return KEY ? value.split(KEY).join('***REDACTED***') : value;
}
const rawLog = console.log.bind(console);
const rawErr = console.error.bind(console);
console.log = (...a) => rawLog(...a.map(redact));
console.error = (...a) => rawErr(...a.map(redact));
// Diagnostics ([mcp-cli] ... lines) go to stderr so stdout stays pure data
// (tool listings / call results / --json output can be piped and parsed).
const diag = (...a) => console.error('[mcp-cli]', ...a);

function fail(code, message) {
  console.error(`[mcp-cli] ERROR: ${message}`);
  process.exit(code);
}

/* ---------- startup config checks ---------------------------------------- */

if (!KEY) {
  console.error('[mcp-cli] ERROR: COMPOSIO_CONSUMER_KEY is not set (or empty).');
  console.error('[mcp-cli] Add it in the repo: Settings -> Secrets and variables -> Actions.');
  console.error('[mcp-cli] Get the key from dashboard.composio.dev. Never paste it in chat or commit it.');
  process.exit(2);
}

let ENDPOINT;
try {
  ENDPOINT = new URL(BASE_URL);
  if (!/^https?:$/.test(ENDPOINT.protocol)) throw new Error(`unsupported protocol "${ENDPOINT.protocol}"`);
} catch (err) {
  fail(2, `COMPOSIO_MCP_URL is not a valid http(s) URL: ${err.message}`);
}

/* ---------- MCP streamable-HTTP transport -------------------------------- */

let sessionId = null;
let nextId = 1;

function buildHeaders() {
  const headers = {
    'content-type': 'application/json',
    accept: 'application/json, text/event-stream',
    // Official Composio Connect MCP auth header (dashboard.composio.dev keys).
    'x-consumer-api-key': KEY,
    // Accepted by some Composio gateways/versions as a fallback; harmless duplicate.
    'x-api-key': KEY,
  };
  if (sessionId) headers['mcp-session-id'] = sessionId;
  return headers;
}

async function drain(res) {
  try {
    if (res.body) await res.body.cancel();
  } catch {
    /* ignore */
  }
}

/** Pick the JSON-RPC response matching wantId out of an object or batch array. */
function pickResponse(data, wantId) {
  const candidates = Array.isArray(data) ? data : [data];
  if (wantId !== undefined) {
    const match = candidates.find((m) => m && m.id === wantId);
    if (match) return match;
  }
  return candidates.find((m) => m && (m.result !== undefined || m.error !== undefined)) || null;
}

/**
 * Read an SSE (text/event-stream) response body, resolving with the JSON-RPC
 * message matching wantId as soon as it arrives, then cancelling the stream.
 */
async function readSse(res, wantId) {
  const reader = res.body.getReader();
  const decoder = new TextDecoder();
  let buffer = '';
  let dataLines = [];

  const handleEvent = () => {
    if (!dataLines.length) return undefined;
    const payload = dataLines.join('\n');
    dataLines = [];
    let parsed;
    try {
      parsed = JSON.parse(payload);
    } catch {
      return undefined; // keep-alive / non-JSON event data — ignore
    }
    return pickResponse(parsed, wantId);
  };

  try {
    for (;;) {
      const { done, value } = await reader.read();
      if (done) break;
      buffer += decoder.decode(value, { stream: true });
      let newline;
      while ((newline = buffer.indexOf('\n')) !== -1) {
        let line = buffer.slice(0, newline);
        buffer = buffer.slice(newline + 1);
        if (line.endsWith('\r')) line = line.slice(0, -1);
        if (line === '') {
          const picked = handleEvent();
          if (picked !== undefined) return picked;
        } else if (line.startsWith('data:')) {
          dataLines.push(line.slice(5).replace(/^ /, ''));
        }
        // "event:", "id:", "retry:" and ":" comments are ignored.
      }
    }
    buffer += decoder.decode();
    const lastLine = buffer.replace(/\r$/, '');
    if (lastLine.startsWith('data:')) dataLines.push(lastLine.slice(5).replace(/^ /, ''));
    return handleEvent() ?? null;
  } finally {
    await reader.cancel().catch(() => {});
  }
}

/** POST one JSON-RPC message; returns the matching response object (or null for 202). */
async function rpcRaw(message) {
  const isNotification = message.id === undefined;
  let res;
  try {
    res = await fetch(ENDPOINT, {
      method: 'POST',
      headers: buildHeaders(),
      body: JSON.stringify(message),
      signal: AbortSignal.timeout(TIMEOUT_MS),
    });
  } catch (err) {
    const reason =
      err?.name === 'TimeoutError' || err?.name === 'AbortError'
        ? `timed out after ${TIMEOUT_MS}ms`
        : err?.cause?.code || err?.message || String(err);
    fail(
      1,
      `could not reach ${BASE_URL} (${reason}). ` +
        'Reminder: composio.dev is blocked from the Arena sandbox — run this through the "Composio Bridge" GitHub Action.'
    );
  }

  const sid = res.headers.get('mcp-session-id');
  if (sid) sessionId = sid;

  if (res.status === 202) {
    await drain(res);
    return null; // accepted notification, no content
  }
  if (!res.ok) {
    const body = (await res.text().catch(() => '')).slice(0, 1500);
    if (res.status === 401 || res.status === 403) {
      fail(
        1,
        `Composio rejected authentication (HTTP ${res.status}). The consumer key may be missing, wrong, or revoked. ` +
          'Fix: repo Settings -> Secrets and variables -> Actions -> COMPOSIO_CONSUMER_KEY (value from dashboard.composio.dev). ' +
          `Server body: ${body || '(empty)'}`
      );
    }
    if (res.status === 404) {
      fail(1, `endpoint not found (HTTP 404): ${BASE_URL}. Check COMPOSIO_MCP_URL. Server body: ${body || '(empty)'}`);
    }
    fail(1, `HTTP ${res.status} from ${BASE_URL}: ${body || '(empty body)'}`);
  }

  const contentType = (res.headers.get('content-type') || '').toLowerCase();
  if (contentType.includes('text/event-stream')) return readSse(res, message.id);
  if (isNotification) {
    await drain(res);
    return null;
  }
  let data;
  try {
    data = await res.json();
  } catch (err) {
    fail(1, `could not parse JSON response for "${message.method}": ${err.message}`);
  }
  return pickResponse(data, message.id);
}

function unwrap(resp, method) {
  if (resp === null || resp === undefined) {
    fail(1, `no JSON-RPC response received for "${method}" (connection/stream closed early)`);
  }
  if (resp.error) {
    const extra = resp.error.data ? ` | data: ${JSON.stringify(resp.error.data).slice(0, 600)}` : '';
    fail(1, `JSON-RPC error on "${method}": [${resp.error.code}] ${resp.error.message}${extra}`);
  }
  return resp.result;
}

/** Send a request (with id) and return its result, or fail with a clear error. */
async function rpc(method, params) {
  const message = { jsonrpc: '2.0', id: nextId++, method };
  if (params !== undefined) message.params = params;
  return unwrap(await rpcRaw(message), method);
}

/* ---------- handshake ----------------------------------------------------- */

async function initialize() {
  let lastError = null;
  for (const protocolVersion of PROTOCOL_VERSIONS) {
    const resp = await rpcRaw({
      jsonrpc: '2.0',
      id: nextId++,
      method: 'initialize',
      params: {
        protocolVersion,
        capabilities: {},
        clientInfo: { name: 'composio-bridge-cli', version: '1.0.0' },
      },
    });
    if (!resp) fail(1, `initialize (protocol ${protocolVersion}) got no response`);
    if (resp.error) {
      lastError = resp.error;
      if (/version/i.test(String(resp.error.message || ''))) continue; // negotiate down
      fail(1, `initialize failed: [${resp.error.code}] ${resp.error.message}`);
    }
    const negotiated = resp.result?.protocolVersion || protocolVersion;
    const server = resp.result?.serverInfo?.name || 'unknown';
    const serverVersion = resp.result?.serverInfo?.version ? ` ${resp.result.serverInfo.version}` : '';
    diag(`initialized: server=${server}${serverVersion} protocol=${negotiated}`);
    await rpcRaw({ jsonrpc: '2.0', method: 'notifications/initialized' });
    return resp.result;
  }
  fail(1, `initialize failed for all protocol versions; last error: ${JSON.stringify(lastError)}`);
}

/* ---------- commands ------------------------------------------------------ */

function oneLine(text, max) {
  return String(text || '').replace(/\s+/g, ' ').trim().slice(0, max);
}

function printToolCompact(tool, index) {
  const schema = tool.inputSchema || tool.input_schema || {};
  const required = Array.isArray(schema.required) && schema.required.length ? schema.required.join(', ') : '(none)';
  const props = Object.entries(schema.properties || {})
    .map(([name, def]) => `${name}:${def?.type || '?'}`)
    .join(', ');
  console.log(`${String(index + 1).padStart(3)}. ${tool.name}`);
  const description = oneLine(tool.description, 140);
  if (description) console.log(`     ${description}`);
  console.log(`     required: ${required}${props ? ` | params: ${oneLine(props, 220)}` : ''}`);
}

async function cmdTools(asJson) {
  await initialize();
  const tools = [];
  let cursor;
  do {
    const result = await rpc('tools/list', cursor ? { cursor } : {});
    tools.push(...(result?.tools || []));
    cursor = result?.nextCursor;
  } while (cursor);

  if (asJson) {
    console.log(JSON.stringify(tools, null, 2));
    return;
  }

  diag(`${tools.length} tool(s) exposed by this Composio account:`);
  tools.forEach(printToolCompact);

  const matches = (re) => tools.filter((t) => re.test(`${t.name} ${t.description || ''}`));
  if (!matches(/linkedin/i).length) {
    diag(
      'NOTE: no LinkedIn tools found. LinkedIn is likely not connected in Composio yet:\n' +
        '          dashboard.composio.dev -> Toolkits -> LinkedIn -> Connect -> approve the OAuth flow, then re-run mode=tools.'
    );
  }
  if (!matches(/instagram/i).length) {
    diag('NOTE: no Instagram tools found (connect Instagram in Composio the same way when needed).');
  }
}

async function cmdCall(toolName, argsJson, asJson) {
  let args;
  try {
    args = JSON.parse(argsJson);
  } catch (err) {
    fail(2, `--args is not valid JSON: ${err.message}`);
  }
  if (args === null || typeof args !== 'object' || Array.isArray(args)) {
    fail(2, `--args must be a JSON object, e.g. {"text":"..."} (got: ${argsJson.slice(0, 100)})`);
  }

  await initialize();
  diag(`calling "${toolName}" with arguments: ${JSON.stringify(args)}`);
  const result = await rpc('tools/call', { name: toolName, arguments: args });

  const text = (result?.content || [])
    .filter((c) => c && c.type === 'text')
    .map((c) => c.text)
    .join('\n');

  if (result?.isError) {
    diag(`tool "${toolName}" returned an error (isError=true):`);
    if (text) console.error(text);
    console.error(JSON.stringify(result, null, 2));
    diag('If this is an auth/expired-connection error, re-approve the app connection in dashboard.composio.dev.');
    process.exit(1);
  }

  diag(`tool "${toolName}" succeeded.`);
  if (text) console.log(`--- tool output ---\n${text}`);
  if (result?.structuredContent !== undefined) {
    console.log(`--- structuredContent ---\n${JSON.stringify(result.structuredContent, null, 2)}`);
  }
  if (asJson) console.log(`--- raw result ---\n${JSON.stringify(result, null, 2)}`);
}

function usage() {
  console.error(
    'Usage:\n' +
      '  node mcp-cli.mjs tools [--json]\n' +
      "  node mcp-cli.mjs call <TOOL_SLUG> [--args '{\"text\":\"...\"}'] [--json]\n\n" +
      'Env: COMPOSIO_CONSUMER_KEY (required), COMPOSIO_MCP_URL, COMPOSIO_TIMEOUT_MS'
  );
  process.exit(2);
}

async function main() {
  const [cmd, ...rest] = process.argv.slice(2);
  const asJson = rest.includes('--json');

  if (cmd === 'tools') {
    const unknown = rest.filter((f) => f !== '--json');
    if (unknown.length) fail(2, `unexpected argument(s) for tools: ${unknown.join(' ')}`);
    await cmdTools(asJson);
    return;
  }

  if (cmd === 'call') {
    let toolName = null;
    let argsJson = '{}';
    for (let i = 0; i < rest.length; i++) {
      const flag = rest[i];
      if (flag === '--json') continue;
      if (flag === '--args') {
        const value = rest[++i];
        if (value === undefined || value.startsWith('--')) fail(2, '--args requires a JSON value');
        argsJson = value;
      } else if (flag.startsWith('--args=')) {
        argsJson = flag.slice('--args='.length);
      } else if (flag.startsWith('--')) {
        fail(2, `unknown flag: ${flag}`);
      } else if (toolName === null) {
        toolName = flag;
      } else {
        fail(2, `unexpected argument: ${flag}`);
      }
    }
    if (!toolName) usage();
    await cmdCall(toolName, argsJson, asJson);
    return;
  }

  usage();
}

main().catch((err) => {
  if (err?.name === 'AbortError' || err?.name === 'TimeoutError') {
    fail(1, `request to ${BASE_URL} timed out after ${TIMEOUT_MS}ms`);
  }
  const detail = process.env.MCP_DEBUG && err?.stack ? err.stack : err?.message || String(err);
  fail(1, detail);
});
