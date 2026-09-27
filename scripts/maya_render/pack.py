"""Build the copy-paste caption pack + posting guide for a MAYA day from its DAY-xx-CONTENT.md.

Usage:  python3 scripts/maya_render/pack.py            (defaults to week-01/day-01)
Writes: maya-content/week-01/day-01/final/captions/post{1,2,3}/<platform>.txt and final/POSTING-GUIDE.md
"""
from __future__ import annotations
import os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DAY = os.path.join(ROOT, "maya-content", "week-01", "day-01")
MD = os.path.join(DAY, "DAY-01-CONTENT.md")
FINAL = os.path.join(DAY, "final")
CAP = os.path.join(FINAL, "captions")

PLATFORM = {"📸": "instagram", "📘": "facebook", "🐦": "x", "💼": "linkedin", "🤖": "reddit", "📌": "pinterest", "📱": "threads", "🎵": "youtube"}
HDR = re.compile(r"^(📸|📘|🐦|💼|🤖|📌|📱|🎵) (.+?)(?: \((.*)\))?:\s*$")


def clean(text: str) -> str:
    text = text.replace("**First comment (Set A, 25):**",
                        "──────── FIRST COMMENT (paste as your own first comment right after publishing) ────────")
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)  # bold markers
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def parse():
    src = open(MD, encoding="utf-8").read()
    blocks = re.split(r"^╔═+╗\s*$", src, flags=re.M)[1:]  # 3 post blocks
    posts = []
    for n, blk in enumerate(blocks, 1):
        lines = blk.splitlines()
        title = lines[0].strip("║ ").strip()
        sections, alt, refs = {}, "", ""
        i = 0
        while i < len(lines):
            m = HDR.match(lines[i])
            if m and m.group(1) in PLATFORM:
                key, note = PLATFORM[m.group(1)], (m.group(3) or "")
                j, body = i + 1, []
                while j < len(lines) and lines[j].strip() != "---" and not lines[j].startswith("━━━"):
                    body.append(lines[j]); j += 1
                sections[key] = (note, clean("\n".join(body)))
                i = j
                continue
            if lines[i].startswith("♿ ALT TEXT"):
                j = i + 1; body = []
                while j < len(lines) and lines[j].strip() and not lines[j].startswith("━━━"):
                    body.append(lines[j]); j += 1
                alt = clean("\n".join(body)); i = j; continue
            if lines[i].startswith("📚 REFERENCES"):
                j = i + 1; body = []
                while j < len(lines) and lines[j].strip() != "---" and not lines[j].startswith("╔"):
                    body.append(lines[j]); j += 1
                refs = clean("\n".join(body)); i = j; continue
            i += 1
        posts.append(dict(n=n, title=title, sections=sections, alt=alt, refs=refs))
    return posts


def tweet_len(t: str) -> int:
    """Approximate X weighted length: URLs = 23, most emoji/symbols = 2."""
    t = re.sub(r"https?://\S+|\b[\w.-]+\.(?:app|com|org|in)(?:/\S*)?", "x" * 23, t)
    def w(ch):
        o = ord(ch)
        return 1 if (o <= 0x10FF or 0x2000 <= o <= 0x200D or 0x2010 <= o <= 0x201F or 0x2032 <= o <= 0x2037) else 2
    return sum(w(c) for c in t)


def split_tweets(body: str):
    body = "\n".join(l for l in body.splitlines() if not l.startswith("#")).strip()
    parts = re.split(r"\n(?=(?:Tweet \d+|Reply)[^\n]*:\n|\d/ )", "\n" + body)
    return [re.sub(r"^(?:Tweet \d+|Reply)[^\n]*:\n", "", x.strip()) for x in parts if x.strip()]


def qa(posts):
    problems = []
    forbidden = ["#AITherapy", "manasynsapp", "24/7 iCall", "@manasyn ", "@manasyn\n", "download the app"]
    for p in posts:
        for key, (note, body) in p["sections"].items():
            for f in forbidden:
                if f in body + "\n":
                    problems.append(f"post{p['n']}/{key}: contains '{f.strip()}'")
            if key == "x":
                for tw in split_tweets(body):
                    tl = tweet_len(tw)
                    if tl > 280:
                        problems.append(f"post{p['n']}/x: tweet over 280 weighted chars ({tl}): {tw[:50]!r}")
        m = re.search(r"Instagram \(≤125 chars\): \"(.+?)\"", p["alt"])
        if m and len(m.group(1)) > 125:
            problems.append(f"post{p['n']}: IG alt text {len(m.group(1))} chars")
    return problems


ATTACH = {
    1: {
        "instagram": ["post1/post1-portrait-1080x1350.jpg (feed)", "post1/post1-story-1080x1920.jpg (Story — add link sticker → manasyn.app)"],
        "facebook": ["post1/post1-portrait-1080x1350.jpg"],
        "x": ["post1/post1-square-1080x1080.jpg"],
        "linkedin": ["post1/post1-portrait-1080x1350.jpg"],
        "reddit": ["(text post — no image unless the sub allows it)"],
        "pinterest": ["post1/post1-pinterest-1000x1500.jpg · destination link: https://manasyn.app"],
        "threads": ["post1/post1-square-1080x1080.jpg"],
        "youtube": ["youtube/post1-ai-companion-short-1080x1920.mp4 (10 s, silent — add a track from the YouTube audio library)"],
    },
    2: {
        "instagram": ["post2/post2-portrait-1080x1350.jpg (feed; square version also provided)", "post2/post2-story-1080x1920.jpg (Story)"],
        "facebook": ["post2/post2-square-1080x1080.jpg"],
        "x": ["post2/post2-square-1080x1080.jpg on tweet 1"],
        "linkedin": ["post2/post2-portrait-1080x1350.jpg"],
        "reddit": ["post2/post2-square-1080x1080.jpg (optional — text is the post)"],
        "pinterest": ["post2/post2-pinterest-1000x1500.jpg · destination link: https://manasyn.app"],
        "threads": ["post2/post2-square-1080x1080.jpg"],
        "youtube": ["youtube/post2-sleep-anchors-short-1080x1920.mp4 (14 s, silent — add music)"],
    },
    3: {
        "instagram": ["post3/post3-slide-01.jpg … post3-slide-08.jpg — upload all 8 in order as a carousel"],
        "facebook": ["post3/post3-slide-01.jpg … 08.jpg (multi-photo post, in order)"],
        "x": ["Tweet 1: post3-slide-01.jpg · then slides 02–07 on tweets 2–7 as written in the thread"],
        "linkedin": ["post3/post3-carousel-linkedin.pdf (upload as a Document post)"],
        "reddit": ["post3/post3-slide-02.jpg … 07.jpg as a gallery (skip the cover + CTA slide) — check sub rules first"],
        "pinterest": ["post3/post3-pinterest-1000x1500.jpg · destination link: https://manasyn.app/courses"],
        "threads": ["post3/post3-slide-01.jpg (or all 8 as a carousel)"],
        "youtube": ["youtube/post3-freud-in-60s-short-1080x1920.mp4 (53 s, silent — add a calm lo-fi track)"],
    },
}

SCHEDULE = [
    ("8:00 AM", "Instagram", 1), ("8:00 AM", "X", 1), ("8:00 AM", "YouTube Shorts", 1), ("8:15 AM", "Threads", 1),
    ("8:30 AM", "Facebook", 1), ("9:00 AM", "LinkedIn", 1), ("9:00 AM", "Pinterest", 1),
    ("1:00 PM", "Instagram", 2), ("1:00 PM", "X", 2), ("1:00 PM", "Pinterest", 2), ("1:00 PM", "YouTube Shorts", 2),
    ("1:00 PM", "LinkedIn (optional)", 2), ("1:15 PM", "Threads", 2), ("1:30 PM", "Facebook", 2), ("2:00 PM", "Reddit", 2),
    ("7:00 PM", "Instagram", 3), ("7:00 PM", "X", 3), ("7:00 PM", "LinkedIn", 3), ("7:00 PM", "YouTube Shorts", 3),
    ("7:15 PM", "Threads", 3), ("7:30 PM", "Facebook", 3), ("7:30 PM", "Pinterest", 3), ("8:00 PM", "Reddit", 3),
]
KEY = {"Instagram": "instagram", "X": "x", "YouTube Shorts": "youtube", "Threads": "threads", "Facebook": "facebook",
       "LinkedIn": "linkedin", "LinkedIn (optional)": "linkedin", "Pinterest": "pinterest", "Reddit": "reddit"}


def write_pack(posts):
    os.makedirs(CAP, exist_ok=True)
    for p in posts:
        d = os.path.join(CAP, f"post{p['n']}"); os.makedirs(d, exist_ok=True)
        for key, (note, body) in p["sections"].items():
            head = f"# Post {p['n']} · {key.upper()}" + (f" — {note}" if note else "") + "\n# Attach: " + " | ".join(ATTACH[p['n']][key]) + "\n# (lines starting with # are notes — do not paste them)\n\n"
            open(os.path.join(d, f"{key}.txt"), "w", encoding="utf-8").write(head + body)
        open(os.path.join(d, "alt-text.txt"), "w", encoding="utf-8").write(f"# Post {p['n']} · ALT TEXT (paste into the platform's alt-text / accessibility field)\n\n" + p["alt"])
        open(os.path.join(d, "references.txt"), "w", encoding="utf-8").write(f"# Post {p['n']} · REFERENCES (APA 7) — for the bio link page / comments if asked\n\n" + p["refs"])

    rows = ["| Time (IST) | Platform | Post | Attach (from `final/`) | Caption file |", "|---|---|---|---|---|"]
    for t, plat, n in SCHEDULE:
        k = KEY[plat]
        rows.append(f"| {t} | {plat} | {n} | {'<br>'.join(ATTACH[n][k])} | `captions/post{n}/{k}.txt` |")
    guide = f"""# Day 1 — Ready-to-post pack (Mon 28 Sep 2026)

Everything in this folder is final: text, logo, badge and `manasyn.app` watermark are already baked into the images. No Canva step.
Open the caption file, copy everything below the `#` note lines, paste, attach the listed file(s), publish.

## Handles used in the captions
Instagram / Threads **@manasynapp** · X **@Manasynapp** · YouTube **@Manasyn** · LinkedIn **linkedin.com/company/manasyn** · Facebook **facebook.com/people/Manasyn/61594022532492/**

## Posting order
{chr(10).join(rows)}

## Platform notes
- **Instagram:** paste the caption, publish, then paste the hashtag block (below the `FIRST COMMENT` line in the file) as your own first comment. Add the alt text from `alt-text.txt` under *Advanced settings → Accessibility*. Story: use the 1080×1920 file and add a link sticker → `manasyn.app` (Post 3 story: `manasyn.app/courses`).
- **X:** `x.txt` is split into tweets (`Tweet 1:` / `Reply:` blocks, or `1/`, `2/` … for threads) — post each block as one tweet in the same thread, keeping the `1/` numbering. All tweets are ≤ 280 weighted characters. Attach the images noted in the file header.
- **LinkedIn:** Post 3 goes up as a *Document* post using the PDF (that is what makes it swipeable). Posts 1–2 are normal image posts.
- **Facebook:** Post 2 and Post 3 captions end with a poll — create the poll in the post composer with the options given.
- **Pinterest:** use the description as the pin description, the first line as the title, and set the destination link listed in the file header.
- **Reddit:** value-first text, disclosure at the end, no link unless the subreddit's rules allow it. Read each sub's self-promotion rule before posting.
- **YouTube Shorts:** upload the MP4, paste the *Title* and *Description* from `youtube.txt`, and add a track from the YouTube Audio Library (the files are silent by design so a copyright-safe track can be chosen inside YouTube). Tick "Altered or synthetic content" if prompted (images are AI-generated).
- **Threads:** casual Hinglish caption + the square image.

## Files
```
final/
├── post1/  square 1080×1080 · portrait 1080×1350 · story 1080×1920 · pinterest 1000×1500
├── post2/  square · portrait · story · pinterest
├── post3/  slide-01 … slide-08 (1080×1080) · pinterest 1000×1500 · post3-carousel-linkedin.pdf
├── youtube/ 3 Shorts (1080×1920 MP4, H.264, silent)
└── captions/post{{1,2,3}}/  instagram · facebook · x · linkedin · reddit · pinterest · threads · youtube · alt-text · references
```

## Before you hit publish (30-second check)
- Crisis footer is present on Posts 1 & 2 (112 · Tele-MANAS 14416 · iCall 9152987821 Mon–Sat 10 AM–8 PM) ✔ baked into the captions
- Nothing says therapy / diagnosis / cure / "download the app" ✔
- Instagram hashtags go in the first comment, not the caption ✔
- Re-generate anything after a text change: `python3 scripts/maya_render/day01.py all && python3 scripts/maya_render/shorts.py && python3 scripts/maya_render/pack.py`
"""
    open(os.path.join(FINAL, "POSTING-GUIDE.md"), "w", encoding="utf-8").write(guide)


if __name__ == "__main__":
    posts = parse()
    probs = qa(posts)
    write_pack(posts)
    for p in posts:
        print(f"post{p['n']}: {sorted(p['sections'])} alt={bool(p['alt'])} refs={bool(p['refs'])}")
    print("QA:", "OK" if not probs else "\n  " + "\n  ".join(probs))
    sys.exit(1 if probs else 0)
