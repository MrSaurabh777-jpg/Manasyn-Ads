"""Build the manual-posting pack for a MAYA day from its DAY-xx-CONTENT.md.

Usage:  python3 scripts/maya_render/pack.py            (defaults to week-01/day-01)
Writes: final/POSTING-GUIDE.md                      ← the run-sheet: every slot in order with image, caption, alt text
        final/captions/post{1,2,3}/<platform>.txt   ← the same captions as plain text files
Platforms: Instagram, Facebook, X, LinkedIn, Threads, Pinterest, Reddit (YouTube is out of scope).
"""
from __future__ import annotations
import os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DAY = os.path.join(ROOT, "maya-content", "week-01", "day-01")
MD = os.path.join(DAY, "DAY-01-CONTENT.md")
FINAL = os.path.join(DAY, "final")
CAP = os.path.join(FINAL, "captions")

PLATFORM = {"📸": "instagram", "📘": "facebook", "🐦": "x", "💼": "linkedin", "🤖": "reddit", "📌": "pinterest", "📱": "threads"}
HDR = re.compile(r"^(📸|📘|🐦|💼|🤖|📌|📱|🎵) (.+?)(?: \((.*)\))?:\s*$")
FIRST_COMMENT = "──────── FIRST COMMENT (paste as your own first comment right after publishing) ────────"
NAMES = {1: "Manasyn Spotlight — AI Companion", 2: "Wellbeing Wisdom — Sleep", 3: "Psych Notes — Freud's Psychoanalysis (8-slide carousel)"}


def clean(text: str) -> str:
    text = text.replace("**First comment (Set A, 25):**", FIRST_COMMENT)
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)  # bold markers
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def parse():
    src = open(MD, encoding="utf-8").read()
    blocks = re.split(r"^╔═+╗\s*$", src, flags=re.M)[1:]  # 3 post blocks
    posts = []
    for n, blk in enumerate(blocks, 1):
        lines = blk.splitlines()
        sections, alt, refs = {}, {"short": "", "long": "", "slides": []}, ""
        i = 0
        while i < len(lines):
            m = HDR.match(lines[i])
            if m:
                key, note = PLATFORM.get(m.group(1)), (m.group(3) or "")
                j, body = i + 1, []
                while j < len(lines) and lines[j].strip() != "---" and not lines[j].startswith("━━━"):
                    body.append(lines[j]); j += 1
                if key:  # 🎵 YouTube is parsed and dropped
                    sections[key] = (note, clean("\n".join(body)))
                i = j
                continue
            if lines[i].startswith("♿ ALT TEXT"):
                j = i + 1
                while j < len(lines) and lines[j].strip() and not lines[j].startswith("━━━"):
                    ln = lines[j].strip()
                    m1 = re.match(r'- Instagram \(≤125 chars\): "(.+)"$', ln)
                    m2 = re.match(r'- Long[^:]*: "(.+)"$', ln)
                    m3 = re.match(r'\d\. "(.+)"$', ln)
                    if m1: alt["short"] = m1.group(1)
                    elif m2: alt["long"] = m2.group(1)
                    elif m3: alt["slides"].append(m3.group(1))
                    j += 1
                i = j; continue
            if lines[i].startswith("📚 REFERENCES"):
                j = i + 1; body = []
                while j < len(lines) and lines[j].strip() != "---" and not lines[j].startswith("╔"):
                    body.append(lines[j]); j += 1
                refs = clean("\n".join(body)); i = j; continue
            i += 1
        posts.append(dict(n=n, sections=sections, alt=alt, refs=refs))
    return posts


# ---------------------------------------------------------------- QA
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
    out = []
    for x in parts:
        x = x.strip()
        if not x:
            continue
        label = "Tweet"
        m = re.match(r"^(Tweet \d+|Reply)[^\n]*:\n", x)
        if m:
            label = m.group(1); x = x[m.end():]
        elif re.match(r"^\d/ ", x):
            label = f"Tweet {x[0]}"
        out.append((label, x.strip()))
    return out


def qa(posts):
    problems = []
    forbidden = ["#AITherapy", "manasynsapp", "24/7 iCall", "@manasyn ", "@manasyn\n", "download the app"]
    for p in posts:
        for key, (note, body) in p["sections"].items():
            for f in forbidden:
                if f in body + "\n":
                    problems.append(f"post{p['n']}/{key}: contains '{f.strip()}'")
            if key == "x":
                for label, tw in split_tweets(body):
                    tl = tweet_len(tw)
                    if tl > 280:
                        problems.append(f"post{p['n']}/x {label}: over 280 weighted chars ({tl})")
        if len(p["alt"]["short"]) > 125:
            problems.append(f"post{p['n']}: IG alt text {len(p['alt']['short'])} chars")
        for k, a in enumerate(p["alt"]["slides"], 1):
            if len(a) > 125:
                problems.append(f"post{p['n']}: slide {k} alt text {len(a)} chars")
        missing = set(PLATFORM.values()) - set(p["sections"])
        if missing:
            problems.append(f"post{p['n']}: missing captions for {sorted(missing)}")
    return problems


# ---------------------------------------------------------------- what to attach where
SL = [f"post3/post3-slide-{i:02d}.jpg" for i in range(1, 9)]
ATTACH = {  # (post, platform) -> list of (file, note)
    (1, "instagram"): [("post1/post1-portrait-1080x1350.jpg", "feed post"), ("post1/post1-story-1080x1920.jpg", "Story — add a link sticker → manasyn.app")],
    (1, "facebook"): [("post1/post1-portrait-1080x1350.jpg", "")],
    (1, "x"): [("post1/post1-square-1080x1080.jpg", "on tweet 1")],
    (1, "linkedin"): [("post1/post1-portrait-1080x1350.jpg", "")],
    (1, "threads"): [("post1/post1-square-1080x1080.jpg", "")],
    (1, "pinterest"): [("post1/post1-pinterest-1000x1500.jpg", "destination link: https://manasyn.app")],
    (1, "reddit"): [],
    (2, "instagram"): [("post2/post2-portrait-1080x1350.jpg", "feed post (square version also in post2/)"), ("post2/post2-story-1080x1920.jpg", "Story — link sticker → manasyn.app")],
    (2, "facebook"): [("post2/post2-square-1080x1080.jpg", "")],
    (2, "x"): [("post2/post2-square-1080x1080.jpg", "on tweet 1")],
    (2, "linkedin"): [("post2/post2-portrait-1080x1350.jpg", "")],
    (2, "threads"): [("post2/post2-square-1080x1080.jpg", "")],
    (2, "pinterest"): [("post2/post2-pinterest-1000x1500.jpg", "destination link: https://manasyn.app")],
    (2, "reddit"): [("post2/post2-square-1080x1080.jpg", "optional — only if the sub allows images; the text is the post")],
    (3, "instagram"): [(f, f"slide {i}") for i, f in enumerate(SL, 1)] + [("post3/post3-story-1080x1920.jpg", "Story after publishing — link sticker → manasyn.app/courses")],
    (3, "facebook"): [(f, f"photo {i}") for i, f in enumerate(SL, 1)],
    (3, "x"): [(SL[0], "tweet 1")] + [(SL[i], f"tweet {i + 1}") for i in range(1, 7)],
    (3, "linkedin"): [("post3/post3-carousel-linkedin.pdf", "upload as a Document post (this is what makes it swipeable)")],
    (3, "threads"): [(SL[0], "cover (or add all 8 as a carousel)")],
    (3, "pinterest"): [("post3/post3-pinterest-1000x1500.jpg", "destination link: https://manasyn.app/courses")],
    (3, "reddit"): [(f, f"gallery image {i - 1}") for i, f in enumerate(SL, 1) if 2 <= i <= 7],
}
TWEET_IMG = {1: {1: "post1/post1-square-1080x1080.jpg"}, 2: {1: "post2/post2-square-1080x1080.jpg"},
             3: {i: SL[i - 1] for i in range(1, 8)}}

SCHEDULE = [  # (time, platform label, post)
    ("8:00 AM", "Instagram", 1), ("8:00 AM", "X", 1), ("8:15 AM", "Threads", 1), ("8:30 AM", "Facebook", 1),
    ("9:00 AM", "LinkedIn", 1), ("9:00 AM", "Pinterest", 1),
    ("1:00 PM", "Instagram", 2), ("1:00 PM", "X", 2), ("1:00 PM", "Pinterest", 2), ("1:00 PM", "LinkedIn (optional)", 2),
    ("1:15 PM", "Threads", 2), ("1:30 PM", "Facebook", 2), ("2:00 PM", "Reddit", 2),
    ("7:00 PM", "Instagram", 3), ("7:00 PM", "X", 3), ("7:00 PM", "LinkedIn", 3), ("7:15 PM", "Threads", 3),
    ("7:30 PM", "Facebook", 3), ("7:30 PM", "Pinterest", 3), ("8:00 PM", "Reddit", 3),
]
KEY = {"Instagram": "instagram", "X": "x", "Threads": "threads", "Facebook": "facebook", "LinkedIn": "linkedin",
       "LinkedIn (optional)": "linkedin", "Pinterest": "pinterest", "Reddit": "reddit"}
NOTES = {
    "instagram": "Paste the caption → publish → immediately paste the hashtag block as your own **first comment**. Alt text: *Advanced settings → Write alt text*. Then post the Story and add the link sticker.",
    "facebook": "Normal photo post. Where the caption ends with a poll / fill-in-the-blank, add it in the composer (Poll) or just leave it in the text — both work.",
    "x": "One tweet per box below, each as a reply to the previous one (a thread). Add alt text on the image (*+ALT*).",
    "linkedin": "Post from the **Manasyn company page** (linkedin.com/company/manasyn), not a personal profile. Alt text: click the image → *Add alt text*.",
    "threads": "Casual tone is intentional (lower-case Hinglish). Same image as X.",
    "pinterest": "Title = the *Title:* line, description = the rest, set the destination link, pick the board named in the header.",
    "reddit": "Text post first, image/gallery only if the sub allows. Read the sub's self-promotion rule first; keep the disclosure at the end; reply to comments, don't link-drop.",
}


def fence(text: str) -> str:
    return "```text\n" + text.strip() + "\n```\n"


def thumbs(files, w):
    return " ".join(f'<img src="{f}" width="{w}" alt="">' for f in files)


def write_txt(posts):
    os.makedirs(CAP, exist_ok=True)
    for p in posts:
        d = os.path.join(CAP, f"post{p['n']}"); os.makedirs(d, exist_ok=True)
        for key, (note, body) in p["sections"].items():
            att = ATTACH[(p["n"], key)]
            att_s = " | ".join(f + (f" ({n})" if n else "") for f, n in att) or "text only"
            head = (f"# Post {p['n']} · {key.upper()}" + (f" — {note}" if note else "") + f"\n# Attach: {att_s}\n"
                    "# (lines starting with # are notes — do not paste them)\n\n")
            open(os.path.join(d, f"{key}.txt"), "w", encoding="utf-8").write(head + body)
        a = p["alt"]
        alt_txt = f"# Post {p['n']} · ALT TEXT\n\nInstagram / Threads / X (≤125 chars):\n{a['short']}\n\nFacebook / LinkedIn / Pinterest (long):\n{a['long']}\n"
        if a["slides"]:
            alt_txt += "\nPer slide (Instagram carousel):\n" + "\n".join(f"{i}. {s}" for i, s in enumerate(a["slides"], 1)) + "\n"
        open(os.path.join(d, "alt-text.txt"), "w", encoding="utf-8").write(alt_txt)
        open(os.path.join(d, "references.txt"), "w", encoding="utf-8").write(f"# Post {p['n']} · REFERENCES (APA 7) — for the bio link page / comments if asked\n\n" + p["refs"])


def slot_section(p, plat_label, time):
    n, key = p["n"], KEY[plat_label]
    note, body = p["sections"][key]
    att = ATTACH[(n, key)]
    out = [f"## {time} · {plat_label} · Post {n}\n", f"**{NAMES[n]}**" + (f" — *{note}*" if note else "") + "\n"]
    # images
    if att:
        out.append("**Attach:**\n")
        for f, nt in att:
            out.append(f"- `{f}`" + (f" — {nt}" if nt else ""))
        out.append("")
        imgs = [f for f, _ in att if f.endswith(".jpg")]
        if imgs:
            out.append(thumbs(imgs, 110 if len(imgs) > 4 else 220) + "\n")
    else:
        out.append("**Attach:** nothing — text post.\n")
    # caption
    if key == "x":
        for label, tw in split_tweets(body):
            m = re.match(r"Tweet (\d+)", label)
            img = TWEET_IMG[n].get(int(m.group(1))) if m else None
            out.append(f"**{label}**" + (f" — attach `{img}`" if img else "") + f" ({tweet_len(tw)} chars)\n")
            out.append(fence(tw))
    elif key == "instagram" and FIRST_COMMENT in body:
        cap, first = body.split(FIRST_COMMENT, 1)
        out.append("**Caption:**\n"); out.append(fence(cap))
        out.append("**First comment (hashtags — Set A):**\n"); out.append(fence(first))
    else:
        out.append("**Caption:**\n"); out.append(fence(body))
    # alt text
    a = p["alt"]
    if key in ("facebook", "linkedin", "pinterest"):
        out.append(f"**Alt text:** {a['long']}\n")
    elif key == "reddit":
        pass
    else:
        out.append(f"**Alt text:** {a['short']}\n")
        if key == "instagram" and a["slides"]:
            out.append("Per-slide alt text (optional, one per image):\n")
            out.extend(f"{i}. {s}" for i, s in enumerate(a["slides"], 1))
            out.append("")
    out.append(f"**How:** {NOTES[key]}\n")
    out.append("---\n")
    return "\n".join(out)


def write_guide(posts):
    by_n = {p["n"]: p for p in posts}
    rows = ["| Time (IST) | Platform | Post | Attach | Caption file |", "|---|---|---|---|---|"]
    for t, plat, n in SCHEDULE:
        k = KEY[plat]
        files = ATTACH[(n, k)]
        if not files:
            att = "text only"
        elif len(files) > 3:
            att = f"{len(files)} images (see section)"
        else:
            att = "<br>".join(f"`{f}`" for f, _ in files)
        rows.append(f"| {t} | {plat} | {n} | {att} | `captions/post{n}/{k}.txt` |")
    head = f"""# Day 1 run-sheet — Monday 28 September 2026 (all times IST)

Everything here is final. Text, logo, badge and the `manasyn.app` watermark are already inside the images — nothing to edit.
For each slot: attach the file(s) listed, copy the caption box, paste the alt text, publish. Same captions also sit in `captions/` as plain `.txt`.

**Handles:** Instagram / Threads **@manasynapp** · X **@Manasynapp** · LinkedIn **linkedin.com/company/manasyn** · Facebook **facebook.com/people/Manasyn/61594022532492/**
**Hashtag rotation:** Day 1 uses Set A (Set B tomorrow, Set C the day after — all three sets are at the end of `../DAY-01-CONTENT.md`).

## Schedule at a glance

{chr(10).join(rows)}

## Files in this folder

| Folder | Files |
|---|---|
| `post1/` | `post1-square-1080x1080.jpg` (X, Threads) · `post1-portrait-1080x1350.jpg` (IG, FB, LinkedIn) · `post1-story-1080x1920.jpg` (IG Story) · `post1-pinterest-1000x1500.jpg` |
| `post2/` | `post2-square-1080x1080.jpg` (X, Threads, FB, Reddit) · `post2-portrait-1080x1350.jpg` (IG, LinkedIn) · `post2-story-1080x1920.jpg` · `post2-pinterest-1000x1500.jpg` |
| `post3/` | `post3-slide-01.jpg` … `post3-slide-08.jpg` (carousel, in order) · `post3-carousel-linkedin.pdf` · `post3-story-1080x1920.jpg` · `post3-pinterest-1000x1500.jpg` |
| `captions/postN/` | `instagram` · `facebook` · `x` · `linkedin` · `threads` · `pinterest` · `reddit` · `alt-text` · `references` (`.txt`) |

---

"""
    body = "".join(slot_section(by_n[n], plat, t) for t, plat, n in SCHEDULE)
    tail = """## 30-second check before each publish
- Right image for the platform (portrait on IG/FB/LinkedIn, square on X/Threads, PDF for the LinkedIn carousel)
- Instagram hashtags in the first comment, not the caption
- Alt text pasted
- Crisis line present on Posts 1 & 2 captions (it is) · nothing says therapy / diagnosis / cure / "download the app"
- Posting from the Manasyn page/account, not a personal profile (LinkedIn, Facebook)

## After posting
- Reply to every comment in the first hour (the question at the end of each caption is the hook)
- Pin the X reply under Post 1 · pin the Instagram carousel comment with the mnemonic if people ask for it
- Day 2 previews are at the bottom of `../DAY-01-CONTENT.md`
"""
    open(os.path.join(FINAL, "POSTING-GUIDE.md"), "w", encoding="utf-8").write(head + body + tail)


if __name__ == "__main__":
    posts = parse()
    probs = qa(posts)
    write_txt(posts)
    write_guide(posts)
    for p in posts:
        print(f"post{p['n']}: {sorted(p['sections'])} alt={bool(p['alt']['short'])}/{bool(p['alt']['long'])}/{len(p['alt']['slides'])} refs={bool(p['refs'])}")
    print("QA:", "OK" if not probs else "\n  " + "\n  ".join(probs))
    sys.exit(1 if probs else 0)
