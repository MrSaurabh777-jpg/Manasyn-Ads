# HANDOFF PROMPT — Next Session

> **How to use this:** copy everything inside the code fence in §15 and paste it as your
> first message in a new Arena session on this repo. It is self-contained. Everything
> below §1 is reference material backing that prompt.

---

## 1. Session state (as of last commit `2e82990`)

| Item | Status |
|---|---|
| Branch | `arena/01a0a103-manasyn-ads` (never use any other branch) |
| Repo root | `/home/user/Manasyn-Ads` |
| 21-post text plan | ✅ `linkedin-week/LINKEDIN-WEEK-CONTENT.md` (1623 lines) |
| Alt text, 70 entries | ✅ `linkedin-week/ALT-TEXT.md` |
| Logo reference | ✅ `linkedin-week/assets/logo.png` (verified) |
| Day 1 images | ✅ 9/9 + `day-01-postA-carousel.pdf` (7 pages) |
| Days 2–7 images | ❌ **54 images remaining** + 6 PDFs |
| Tooling | ✅ `scripts/qa-images.py`, `normalise-size.py`, `build-carousel-pdf.py` |

**Remaining: 6 batches of 9** (Day 2, 3, 4, 5, 6, 7), then a final QA sweep.

---

## 2. The logo situation — RESOLVED, do not re-litigate

The original brief said the logo was at `launch-week/assets/logo.png`. **That path never
existed** — neither did the `launch-week/` folder, `PAGE-SETUP-KIT.md`,
`AUDIO-MUSIC-GUIDE.md`, or `launch-week-package.zip`. The repo had one commit
(`5e2aab1 logo of manasyn`) with the logo at the **root** as `1001042846.png`.

Verified by pure-Python pixel analysis (no vision available):

| Band | Y-range | Evidence |
|---|---|---|
| Arc ring + sparkles | 180–270 | teal `#A0C0C0`, lavender `#80A0C0` |
| Emblem (hands/leaves/face) | 280–740 | blue-teal→lavender `#60A0C0` `#80C0C0` `#6080C0` |
| Wordmark "Manasyn" | 825–945 | **navy `#204060`** + purple `#8080C0` `#6060C0` |
| Heart divider | y=1002 | 42.8% ink, single row |
| Tagline | 1056–1074 | uniform text band |
| Gradient underline | y=1110 | 51.7% ink, single row |

1254×1254, 89% white background. **Confirmed as the official logo.** Copied to
`linkedin-week/assets/logo.png`, MD5 `355dc42c864041e03a2051415643091a` — verify this
hash on load. The root `1001042846.png` is still tracked; leave it alone.

---

## 3. Environment gotchas — cost real time, read these first

1. **Pillow does not persist between turns.** It installs to `~/.local`, which snapshots
   exclude. Run this at the start of every turn that touches images:
   ```
   pip install --quiet --break-system-packages pillow
   ```
   (~2s, silent, harmless if cached.)

2. **Sandbox resets roll back git history, but NOT the working tree.** This happened
   **twice** — most recently after committing the handoff doc, when local HEAD snapped back
   to `5e2aab1` and every commit made that session vanished from history. Critical detail:
   **all files on disk survived** (images, PDF, scripts, docs). Only `.git` was rolled back.

   So when a push is rejected with `non-fast-forward` or `fetch first`:
   - Don't panic and don't re-generate anything — check `ls linkedin-week/day-0N/` first.
   - `git fetch origin arena/01a0a103-manasyn-ads`
   - Confirm the files are still on disk, then `git merge FETCH_HEAD` (non-destructive).
   - **Never force-push.** Your missing work is almost certainly still in the working tree
     and will be re-committed by the merge.
   - The recovery commit for reference: `2e82990`.

3. **Generated images do not come out at the requested size.** They arrive at
   **928×1152** (postA slides) and **1024×1024** (postB/postC). `scripts/normalise-size.py`
   fixes this with LANCZOS. Always run it after generating.

4. **The agent has no vision on image files.** `read_file` on a PNG returns
   "an image was provided but you do not have vision capabilities." Automated QA is
   colour-signature based only — it proves the logo's *colours* are in the corner, **not**
   that the logo is pixel-identical. State this limitation honestly; do not claim to have
   visually verified anything. Ask the user to eyeball at least one asset per batch.

5. **Context discipline:** don't re-read the 1623-line master doc in full. Grep the day
   you need: `sed -n '/^# DAY 2/,/^# DAY 3/p' linkedin-week/LINKEDIN-WEEK-CONTENT.md`.

---

## 4. Brand rules (non-negotiable)

**Palette** — use strictly, nothing else:

| Role | Hex |
|---|---|
| Primary Dark (forest green) | `#3E4A3E` |
| Accent (violet) | `#655396` |
| Warm (coral) | `#D68C78` |
| Background (cream) | `#F5F2ED` |
| Text (sage) | `#52615A` |

**Aesthetic:** minimal, premium, editorial. Soft gradients, ≥35% negative space, thin
line-art (lotus, breathing circles, journal, soundwave). **No faces, no stock people, no
clinical/hospital imagery, no fear-based visuals.**

**Logo rules:**
1. Pass `linkedin-week/assets/logo.png` as a reference image in **every** `generate_image`
   call with: *"Reproduce the provided logo EXACTLY — do not redraw, recolour, restyle,
   crop, stretch or reinterpret it."*
2. Small, subtle, consistent — bottom-right or top-left, **6–10% of canvas width**.
3. Light designs → white bg blends into cream. Dark designs → intact logo inside a small
   white rounded card (~12% canvas width).
4. QA every image; regenerate on any drift.

**Hard rules:**
- Manasyn is **never** therapy, diagnosis, or a replacement for a psychologist/psychiatrist.
- No cure claims, no outcome guarantees.
- No fake testimonials, invented clinician names, fabricated credentials, invented stats.
- **NMHS is NIMHANS/MoHFW — NOT a WHO survey.** The brief said "WHO's 2016 National Mental
  Health Survey"; that is wrong and was corrected.
- iCall is **Mon–Sat, 10 AM–8 PM** — never call it 24/7.
- No implied affiliation with Tele-MANAS or any government service.
- No optimisation for "manas" alone — always "Manasyn".
- Student tools = educational simulation, **not accreditation or a licence to practise**.
- Screening tools = **educational, not diagnostic**.
- No engagement-bait, no dark patterns, no fear/shame, no fake vulnerability.
- College+ framing only.

**Crisis footer** (caption only, never baked into an image):
```
🆘 Emergency: 112 · Tele-MANAS: 14416 (24×7, MoHFW) · iCall: 9152987821 (Mon–Sat, 10 AM–8 PM) · Manasyn is not an emergency service.
```
Required on posts **7, 8, 9, 13, 14, 15, 18** (all of Day 5; Day 3's three; Day 6 Post C).

**Manasyn mentions — exactly 7 of 21, already allocated:**

| Post | Day | Slot | Angle |
|---|---|---|---|
| 3 | D1 | C | student simulator, educational only, free in beta |
| 5 | D2 | B | clinic documentation for independent practitioners |
| 8 | D3 | B | guided 4-7-8 + grounding, 4 languages |
| 12 | D4 | C | pricing transparency before beta ends |
| 14 | D5 | B | simulated clients you can get wrong |
| 18 | D6 | C | AI states its limits inside the app |
| 20 | D7 | B | free in beta, access first |

The other 14 posts: **zero brand mention in the caption**, small logo on the visual only.
Never move a mention to a different post without saying why.

**LinkedIn is a professional platform — market indirectly.** The 14 no-mention posts carry
no brand reference at all. The 7 mention posts carry exactly one sentence, written as a
peer sharing what they built, never a pitch.

---

## 5. Verified facts (cite only these)

| Fact | Wording |
|---|---|
| Treatment gap | NMHS 2015–16: **84.5%** overall; **70–92%** by disorder |
| Prevalence | lifetime **13.67%**, current **10.56%**; **~150 million** need care |
| Psychiatrist density | **0.75** per 100,000 vs WHO norm of **3+** |
| Attribution | **NIMHANS**, funded by Ministry of Health & Family Welfare. ~10 years old — treat as a floor. |
| RCI | registers Clinical Psychologists via RCI-approved M.Phil / MA-MSc / PsyD |
| NCAHP Act 2021 | covers "Psychologist (except Clinical Psychologist under RCI)" |
| ⚠️ Uncertainty | M.Phil being phased out under NEP 2020. **Always write "requirements vary — check RCI, NCAHP and your university's current norms."** |
| iCall | 9152987821, **Mon–Sat 10 AM–8 PM**, TISS School of Human Ecology |
| Tele-MANAS | 14416 (also 1800-891-4416), 24×7, MoHFW, NIMHANS nodal |
| Emergency | 112 |

If a number isn't in this table, the post uses no number.

---

## 6. Reusable image prompt — [DESIGN SYSTEM]

Append to all prompts. Use the dark variant for carousel covers and quote cards only.

```
LinkedIn editorial graphic. Cream #F5F2ED background with a soft vertical gradient
toward near-white, at least 35% empty negative space. Thin single-weight line-art motif
in #3E4A3E at 14% opacity in the upper-right corner only. Accent rules and markers in
#655396 violet and #D68C78 coral, used sparingly. Headline text in #3E4A3E forest green,
body text in #52615A sage. Clean geometric sans-serif, left-aligned, wide letter-tracking
on small uppercase labels, strong typographic hierarchy. Absolutely no faces, no people,
no hands, no stock photography, no clinical or hospital imagery, no dark or fear-based
visuals. Premium, calm, minimal, editorial.

LOGO: Reproduce the provided logo EXACTLY — do not redraw, recolour, restyle, crop,
stretch or reinterpret it. Place the intact logo small in the bottom-right corner at
approximately 8% of canvas width; its white background blends seamlessly into the cream
canvas with no seam, box or border. Keep all text areas clear of the logo zone.
```

**Dark variant** (swap in):
```
Deep forest-green #3E4A3E background with a soft violet #655396 radial glow in the
upper-right corner. All text in #F5F2ED cream, accents in #D68C78 coral. Place the intact
logo inside a small white rounded-corner card in the bottom-right corner, card width
approximately 12% of canvas width. Do not alter the logo itself.
```

Always end with:
```
Render this text exactly, letter-perfect, correct spelling and punctuation:
LABEL: "..."
HEADLINE: "..."
BODY: "..."
```

---

## 7. Batch procedure (repeat 6×)

```
1. pip install --quiet --break-system-packages pillow
2. Read the day's spec:
   sed -n '/^# DAY N (/,/^# DAY N+1 (/p' linkedin-week/LINKEDIN-WEEK-CONTENT.md
3. Generate 9 images in ONE parallel block (7 slides + postB + postC),
   each with images: ["linkedin-week/assets/logo.png"]
4. python3 scripts/normalise-size.py          # 928x1152 / 1024x1024 -> 1080x1350 / 1080x1080
5. python3 scripts/qa-images.py               # dims, palette, logo signature
   - PASS = all rows "OK", palette >=72%, logo-sig >=12
   - Regenerate any FAIL before moving on
6. python3 scripts/build-carousel-pdf.py day-0N
7. git add -A && commit && git fetch && (merge if needed) && push
   A push rejection here is NORMAL — see gotcha #2. Fetch, merge, re-push.
   Never force-push; your files are almost certainly still on disk.
8. Present one asset to the user, and say plainly that you cannot see it
```

**QA thresholds:** dimensions exact · palette ≥72% on-brand · logo-signature ≥12 px hits in
the bottom-right zone. Day 1 scored 95–98% palette and 931–1609 signature hits — use those
as the baseline. A large deviation means drift.

---

## 8. Day 2 spec — ready to generate immediately

**Theme: What college doesn't teach.** Files → `linkedin-week/day-02/`.

### Post 2A — Carousel, 7 slides, 1080×1350 (slot A, 09:30 IST)
Label: `FIRST SESSIONS`. Slide 1 dark cover; slides 2–7 light; slide 7 coral underline.

| # | Headline | Body | Motif |
|---|---|---|---|
| 1 | Your first session, honestly | It will not follow the format in your textbook. Seven things textbooks leave out. | two chairs angled toward each other |
| 2 | Rapport starts in five minutes | How you greet, where you sit, and what you say about confidentiality set the tone before the work begins. | two chair outlines facing |
| 3 | Explain confidentiality before you ask | Including its limits. Clients relax when they know exactly what stays private and what cannot. | lock / bracket |
| 4 | Ask, then stop talking | Open with "what brings you here?" and let the silence work. Silence is data, not dead air. | soundwave flattening to a flat line |
| 5 | Take notes, keep your eyes up | Agree on note-taking out loud. Write sparingly in session; write fully immediately after. | journal + pen |
| 6 | Close the session on purpose | Summarise, check how the client is leaving, and agree the next step. Never let it just end. | bracket closing a line |
| 7 | Steal this checklist | Six habits that make first sessions safer for clients and calmer for you. | coral underline rule |

Caption hook: *"Your first client session will not follow the format in your textbook."*
Manasyn: **NO**. Footer: **NO**.
Engagement hook: "Which of these took you the longest to get right in your own first sessions?"
Hashtags: `#PsychologyStudents #ClinicalPsychology #Psychologists #TherapistLife`

### Post 2B — Image, 1080×1080 (slot B, 13:00 IST) — **Manasyn: YES**
Label: `CASE DOCUMENTATION`. Motif: sheet of paper with three ruled lines, lower-left.
Title: **SOAP, IN SIXTY SECONDS**
- **S — Subjective** · What the client reported, in their words
- **O — Objective** · What you observed: affect, behaviour, engagement
- **A — Assessment** · Your clinical read, and how it's changed
- **P — Plan** · Next step, agreed out loud with the client
Footer line: **Write it the same day.**

Caption hook: *"The case note is the least taught and most consequential thing you will write."*
**Exact Manasyn line:** "Manasyn's practitioner side exists partly because of this problem —
patient records and session documentation built for independent psychologists and
counsellors, not repurposed from a hospital system. It's free during private beta."
Engagement hook: "What does your note-taking structure look like — SOAP, DAP, BIRP, or
something you invented yourself?"
Hashtags: `#Psychologists #ClinicalPsychology #TherapistLife #MentalHealthProfessionals #Manasyn`

### Post 2C — Quote card, 1080×1080 (slot C, 19:30 IST), **light cream**
Label: `PRACTICE IN INDIA`. Motif: abstract contour map of a small town, upper-right.
Quote: **"In a small city, your client will know your family. Ethics has to be practical
before it's theoretical."**
Sub-line (coral): **Decide the boundary before you need it.**

Caption hook: quote first line. Manasyn: **NO**. Footer: **NO**.
Engagement hook: "Practitioners in tier-2 and tier-3 cities — what's the dual-relationship
situation you've had to navigate that nobody prepared you for?"
Hashtags: `#IndianPsychologists #Psychologists #MentalHealthIndia #TherapistLife`

---

## 9. Days 3–7 at a glance

| Day | Theme | Post A (carousel) | Post B (image) | Post C (quote) | Manasyn slot | Footer |
|---|---|---|---|---|---|---|
| 3 Wed | CBT craft | The thought record, taught properly (7 steps) | 4-7-8 breathing, step by step | "A breathing exercise is a seatbelt, not a steering wheel" | **B** | A, B, C |
| 4 Thu | Private practice | Starting a practice: the unglamorous list | 8 agreements before a video session | On charging a fair fee | **C** | — |
| 5 Fri | The helper's mind | Burnout is not a character flaw | Imposter feelings: what's happening | A work in progress and still useful | **B** | A, B, C |
| 6 Sat | MH × technology | 5 questions for any mental-health tool | Where AI helps / where it must never | "I can't help with this" | **C** | C |
| 7 Sun | Reflection & community | Seven days, seven useful ideas | The treatment gap, in one card | The field needs people who last | **B** | — |

Full captions, slide text and per-slide motifs are in `LINKEDIN-WEEK-CONTENT.md` under each
`# DAY N` heading. Alt text for all 21 is in `ALT-TEXT.md`.

---

## 10. Posting times (already decided — don't re-derive)

| Day | A | B | C |
|---|---|---|---|
| Mon | 09:00 | 13:00 | 19:30 |
| Tue | 09:30 | 13:00 | 19:30 |
| Wed | 10:00 | 13:00 | 19:30 |
| Thu | 09:30 | 13:00 | 19:30 |
| Fri | 09:30 | 12:30 | 19:30 |
| Sat | 10:30 | 12:00 | 20:00 ⚠️ |
| Sun | 10:00 | 12:30 | 19:00 |

LinkedIn India peaks Tue–Fri 9:30–11:30. Carousels get the peak window. ⚠️ Saturday evening
is the weakest slot of the week (~40–50% of a weekday evening). **The user was asked about
this and skipped the question — it is still unresolved.** Offer the three options again, or
default to "post Saturday 8 PM and accept lower reach" and flag it.

---

## 11. Unresolved items — surface these, don't silently decide

1. **Visual QA of Day 1.** The user never confirmed the logo renders pixel-identically.
   Ask before generating Day 3.
2. **Saturday Post C slot** (see §10).
3. **63 images is the full ask.** If the user wants to cut scope, the obvious lever is
   dropping carousels from 7 to 5 slides (49 → 35 slides, 63 → 49 images). Don't
   unilaterally cut.
4. **`launch-week/` folder is still missing.** If the user expected launch-week posts,
   covers, WhatsApp card and the setup kit to exist, they don't — that's a separate work
   item, not part of this 21-post series.

---

## 12. Commit convention

```
git add -A
git -c user.name="Arena Agent" -c user.email="agent@arena.ai" commit -q -m "..."
git fetch origin arena/01a0a103-manasyn-ads      # ALWAYS fetch first
git push origin arena/01a0a103-manasyn-ads       # if rejected: MERGE, never force-push
```
One commit per batch. Push after each so nothing is lost to a sandbox reset.

---

## 13. Files

```
linkedin-week/
  LINKEDIN-WEEK-CONTENT.md    21 captions, 49 slides, 63 prompts, playbook
  ALT-TEXT.md                 70 entries, all <=250 chars
  HANDOFF-NEXT-SESSION.md     this file
  assets/logo.png             verified official logo (MD5 355dc42c...)
  day-01/                     7 slides + postB + postC + carousel.pdf   [DONE]
  day-02 … day-07/            empty, awaiting generation
scripts/
  qa-images.py                dims + palette + logo-signature
  normalise-size.py           928x1152/1024x1024 -> 1080x1350/1080x1080
  build-carousel-pdf.py       slides -> LinkedIn document PDF
1001042846.png                original root logo — leave in place
```

---

## 14. Validation already done (don't redo)

- 49 slide rows: 0 violations (headline ≤8 words, body ≤25 words)
- 70 alt-text rows: all ≤250 chars (range 117–217)
- Day 1: 9/9 images pass, 95–98% on-palette, logo signature in all

---

## 15. ⬇️ COPY FROM HERE — paste as your first message next session

```
Continue the Manasyn 7-day LinkedIn series from where the last session stopped.

CONTEXT
Repo /home/user/Manasyn-Ads, branch arena/01a0a103-manasyn-ads (never any other branch).
Read linkedin-week/HANDOFF-NEXT-SESSION.md first — it has the full brief, brand rules,
verified facts, environment gotchas and the reusable image prompt. Then read only the
section of linkedin-week/LINKEDIN-WEEK-CONTENT.md for the day you are generating; don't
load the whole 1623-line file.

DONE ALREADY
- linkedin-week/LINKEDIN-WEEK-CONTENT.md: all 21 captions, 7 carousels x 7 slides
  (49 slides), 63 image prompts, posting times, engagement hooks, playbook
- linkedin-week/ALT-TEXT.md: 70 alt-text entries, all under 250 chars
- linkedin-week/assets/logo.png: official logo, verified by pixel analysis
  (MD5 355dc42c864041e03a2051415643091a — check it)
- Day 1: 9 images generated, normalised, QA-passed, plus the 7-page carousel PDF

REMAINING: 54 images across 6 batches (Day 2, 3, 4, 5, 6, 7), then a final QA sweep.

START WITH BATCH 2 = DAY 2. Spec is in handoff §8, no need to re-read the master doc
for Day 2.

PROCEDURE PER BATCH
1. pip install --quiet --break-system-packages pillow   (Pillow does NOT persist between
   turns — it installs to ~/.local which snapshots exclude. Run this every turn.)
2. Generate all 9 images in ONE parallel block (7 carousel slides + postB + postC).
   Every single call must pass images: ["linkedin-week/assets/logo.png"] and include:
   "Reproduce the provided logo EXACTLY — do not redraw, recolour, restyle, crop,
   stretch or reinterpret it."
   Use the [DESIGN SYSTEM] block from handoff §6, swapping in the dark variant for
   carousel covers and quote cards.
3. python3 scripts/normalise-size.py     (images arrive at 928x1152 / 1024x1024 and must
   become 1080x1350 / 1080x1080)
4. python3 scripts/qa-images.py          (PASS = exact dims, palette >=72%, logo-signature
   >=12. Day 1 scored 95-98% palette, 931-1609 signature hits — use as baseline.
   Regenerate any failure before continuing.)
5. python3 scripts/build-carousel-pdf.py day-0N
6. git add -A, commit, then git fetch BEFORE git push. If the push is rejected, MERGE —
   never force-push. A sandbox reset already dropped a local commit once.
7. Present one asset from the batch and state plainly that you cannot see the images —
   your QA is colour-signature analysis only, so ask the user to eyeball the logo.

NON-NEGOTIABLES
- Palette only: #3E4A3E forest, #655396 violet, #D68C78 coral, #F5F2ED cream, #52615A sage
- Logo small at 6-10% canvas width, bottom-right; white rounded card on dark designs
- Manasyn is never therapy, diagnosis, or a replacement for a psychologist/psychiatrist
- No cure claims, no outcome guarantees, no invented stats, no fake testimonials
- NMHS is NIMHANS/MoHFW, NOT a WHO survey
- iCall 9152987821 is Mon-Sat 10 AM-8 PM — never 24/7
- Crisis footer in the CAPTION only (never baked into an image):
  "Emergency: 112 | Tele-MANAS: 14416 (24x7, MoHFW) | iCall: 9152987821 (Mon-Sat,
  10 AM-8 PM) | Manasyn is not an emergency service."
  Required on posts 7, 8, 9, 13, 14, 15, 18
- Exactly 7 of 21 posts mention Manasyn — posts 3, 5, 8, 12, 14, 18, 20. Use the exact
  pre-written line for each. The other 14 get zero mention in the caption.
- Student tools = educational simulation, NOT accreditation or a licence to practise
- LinkedIn is professional: market indirectly, one honest sentence, never a pitch

Then continue to Day 3 in the next turn, and so on through Day 7. Report progress after
each batch with the QA numbers.
```
