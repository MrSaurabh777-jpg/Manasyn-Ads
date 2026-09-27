# maya-content/ — MAYA daily content packages

Output of the **MAYA** agent (`../MAYA-AGENT-PROMPT.md`) using the verified facts in `../MANASYN-DETAILS.md`.
One folder per week, one folder per day, three posts per day (Spotlight 8 AM · Wellbeing 1 PM · Psych Notes 7 PM IST).

```
maya-content/
  week-01/
    day-01/
      DAY-01-CONTENT.md        ← everything: prompts, overlay layers, alt text, 8 platform captions × 3 posts,
                                  carousel slide text, hashtag sets A/B/C, APA references, schedule
      images/
        post1-spotlight-base.png             1080×1080, text-free photo base
        post2-wellbeing-base.png             1080×1080, text-free infographic base
        post3-psychnotes-slide-01…08.png     1080×1080, text-free dark-academic slide bases
      final/                     ← READY TO POST (text, logo, badge, watermark baked in — no Canva)
        POSTING-GUIDE.md         the run-sheet: every slot in order with image, caption, alt text, how-to
        post1/  square 1080² · portrait 1080×1350 · story 1080×1920 · pinterest 1000×1500
        post2/  square · portrait · story · pinterest
        post3/  slide-01…08 (1080²) · story · pinterest · post3-carousel-linkedin.pdf
        captions/post{1,2,3}/  instagram · facebook · x · linkedin · threads · pinterest · reddit · alt-text · references (.txt)
```
Platforms covered: Instagram, Facebook, X, LinkedIn, Threads, Pinterest, Reddit. (YouTube is out of scope — the MAYA
brief's Shorts descriptions stay in the day file for reference only.)

## How to publish a day (manual, ≈ 20 min of copy-paste)

1. Open `final/POSTING-GUIDE.md` and work top to bottom — each slot shows the image(s) to attach, the caption box, the alt text and a one-line how-to.
2. Instagram hashtags go in the **first comment**; X threads are one box per tweet; LinkedIn carousel = the PDF as a Document post.
3. Prefer the `.txt` files? The same captions are in `final/captions/postN/` (skip the `#` note lines).

### Regenerating the pack (after editing text in `DAY-0N-CONTENT.md` or a layout)
```
pip install pillow                          # once
python3 scripts/maya_render/day01.py all    # images + LinkedIn PDF  → final/post1|2|3
python3 scripts/maya_render/pack.py         # captions + run-sheet + QA → final/captions, final/POSTING-GUIDE.md
```
Fonts are vendored in `../brand/fonts/` (Poppins + Inter, OFL). Layout code lives in `scripts/maya_render/` (`lib.py` = drawing
helpers, `day01.py` = Day 1 layouts). Days 2+ copy `day01.py` and change the text/positions.

## Manual fallback (Canva Free, ≈ 45 min)

1. **Open the day file** (`DAY-0N-CONTENT.md`) and the `images/` folder.
2. **Canva → Custom size 1080×1080** → upload the base image → follow the numbered **OVERLAY GUIDE** for that post
   (logo top-left from `../brand/manasyn-logo-emblem-transparent.png`, badge top-right, headline, watermark bottom-right).
   Fonts: Poppins Bold + Inter (both free in Canva).
3. **Carousel:** duplicate the page 8×, drop slide bases 01–08, paste the exact slide text from section **[C]**.
   Export → PNG (Instagram/Facebook) and → PDF (LinkedIn document post).
4. **Resize** (Canva "Resize" or manual): 4:5 for IG feed, 9:16 story, 2:3 Pinterest, 16:9 X.
5. **Paste captions** per platform from section **[D]**. Instagram hashtags go in the **first comment**. Rotate hashtag sets:
   Day 1 → A, Day 2 → B, Day 3 → C, Day 4 → A …
6. **Paste alt text** (IG ≤125 chars version; long version elsewhere).
7. Tick the **pre-publish checklist** at the top of the day file (logo, watermark, disclaimer, crisis footer, handles).

## Rules that never change
- Manasyn = self-help & educational companion. **Not therapy, not diagnosis, not an emergency service.** Say it on product posts.
- Crisis footer on anything touching distress: `🆘 Emergency: 112 · Tele-MANAS: 14416 (24×7) · iCall: 9152987821 (Mon–Sat, 10 AM–8 PM)`.
- Only cite numbers listed in `../MANASYN-DETAILS.md` §6 or fully referenced in the day file.
- Reddit: value first, disclosure last, never a pitch; read each subreddit's self-promo rule before posting.
- Never put text or the logo inside an AI image prompt — both are overlays added by the renderer (or Canva).

## Generating the next day
Start a new session on this repo and say:
> Read `MANASYN-DETAILS.md` and `MAYA-AGENT-PROMPT.md`, then: **MAYA, generate Day 2 content** (Week 1 themes; Day 2 angles are previewed at the end of `week-01/day-01/DAY-01-CONTENT.md`).

Image generation is capped at 10 per turn — exactly one day's worth (1 + 1 + 8). Then run the two render scripts above to produce that day's `final/` pack.
