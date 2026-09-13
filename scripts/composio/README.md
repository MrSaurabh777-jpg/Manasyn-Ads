# Composio bridge scripts

Zero-dependency tooling that lets this repo publish to LinkedIn (and later
Instagram) through [Composio](https://dashboard.composio.dev), even though the
Arena sandbox network blocks `*.composio.dev`. All Composio traffic runs inside
GitHub Actions instead.

## Files

- `mcp-cli.mjs` — Node 22 MCP "Streamable HTTP" client (no dependencies).
  Performs `initialize` → `notifications/initialized` → `tools/list` / `tools/call`,
  handles both JSON and SSE responses, MCP session ids, and protocol-version
  negotiation. Auth: reads `COMPOSIO_CONSUMER_KEY` from the environment and
  sends it as the `x-consumer-api-key` header. The key is never printed.
- `../.github/workflows/composio-bridge.yml` — the "Composio Bridge" workflow
  (`workflow_dispatch`) with modes `connectivity`, `tools`, and `call`.

## Usage (inside CI, or anywhere composio.dev is reachable)

```bash
export COMPOSIO_CONSUMER_KEY=...   # from dashboard.composio.dev — never commit this

node mcp-cli.mjs tools             # list tools exposed by the account
node mcp-cli.mjs tools --json      # full schemas as JSON
node mcp-cli.mjs call LINKEDIN_CREATE_POST --args '{"text":"Hello!"}'
```

Exit codes: `0` success · `1` remote/API/tool error · `2` local usage/config error.

## Triggering the workflow

```bash
gh workflow run composio-bridge.yml -f mode=connectivity
gh workflow run composio-bridge.yml -f mode=tools
gh workflow run composio-bridge.yml -f mode=call -f tool=LINKEDIN_CREATE_POST -f args='{"text":"Hello!"}'
```

Requires the repo secret `COMPOSIO_CONSUMER_KEY`
(Settings → Secrets and variables → Actions). If a run fails with an auth or
expired-connection error, re-approve the app connection in the Composio
dashboard.
