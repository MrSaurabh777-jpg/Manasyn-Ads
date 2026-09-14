# Manasyn — 7-Day LinkedIn Content Series (21 Posts)

**Audience:** (1) Psychology students in India (college+) · (2) Practising psychologists & counsellors
**Platform:** LinkedIn only · **Format:** 3 posts/day × 7 days
**Operator:** Saurabh Kumar, Gaya, Bihar · aura777ai@gmail.com · manasyn.app · IG @manasynapp

> ⚠️ **STATUS: PENDING APPROVAL.** This document is the complete text plan for all 21 posts.
> Image generation begins only after you approve this doc **and** confirm the logo file (see §0).

---

## 0. BLOCKER — LOGO FILE NOT FOUND AT THE STATED PATH

You specified `launch-week/assets/logo.png`. **That path does not exist in this repository.**

What I found instead:

| Check | Result |
|---|---|
| `launch-week/` folder | ❌ Does not exist (no `images/`, `pages/`, `PAGE-SETUP-KIT.md`, `AUDIO-MUSIC-GUIDE.md`, `ALT-TEXT.md`, or `launch-week-package.zip`) |
| Tracked files in repo | Only `.github/workflows/composio-bridge.yml`, `1001042846.png`, `README.md`, `scripts/composio/*` |
| Git history | 1 commit total: `5e2aab1 logo of manasyn` |
| Root PNG | ✅ `1001042846.png` — **1254 × 1254 px**, 8-bit RGB — matches your stated dimensions exactly |

**The root `1001042846.png` is almost certainly the logo** (correct dimensions, committed with the message "logo of manasyn"), but I cannot visually verify it matches your description because I have no vision on this file.

**I need you to confirm one of these before I generate a single image:**
- **(a)** Yes — `1001042846.png` is the logo. I'll copy it to `linkedin-week/assets/logo.png` and use that as the reference.
- **(b)** No — attach / re-upload the correct `logo.png` and I'll use that.
- **(c)** Use it but at the root path directly (`1001042846.png`) without copying.

Per your instruction I am stopping short of image generation until this is resolved.

---

## 1. BRAND GUARDRAILS (applies to every asset)

**Philosophy:** Support. Heal. Grow. At your own pace.
**Logo lockup tagline:** SUPPORT. REFLECT. GROW.

### Palette (strict)
| Role | Hex |
|---|---|
| Primary Dark (forest green) | `#3E4A3E` |
| Accent (violet) | `#655396` |
| Warm (coral) | `#D68C78` |
| Background (cream) | `#F5F2ED` |
| Text (sage) | `#52615A` |

**Aesthetic:** minimal, premium, editorial. Soft gradients, generous negative space (≥35% empty), thin line-art (lotus, breathing circles, journal, soundwave). **No faces, no stock people, no clinical/hospital imagery, no fear-based visuals.**

### Logo rules (non-negotiable)
1. `linkedin-week/assets/logo.png` is passed as a reference image in **every** `generate_image` call, with the instruction: *"Reproduce the provided logo EXACTLY — do not redraw, recolour, restyle, crop, stretch or reinterpret it."*
2. Logo appears **small, subtle, consistent** — bottom-right or top-left, **6–10% of canvas width**. Value-first professional posts, **not ads**.
3. Light designs → logo's white background blends into the cream canvas. Dark designs → intact logo inside a small white rounded card.
4. Every image is QA'd: logo unchanged, text letter-perfect, palette correct. Regenerate on any drift.

### Hard rules enforced throughout
- Manasyn is **never** therapy, diagnosis, or a replacement for a psychologist/psychiatrist.
- **No** cure claims, outcome guarantees, or specific results.
- **No** fake testimonials, invented clinician names, fabricated credentials, or invented statistics.
- iCall is **never** described as 24/7 (it is not).
- No optimisation for "manas" alone; **no implied affiliation** with Tele-MANAS or any government service.
- Student tools = **educational simulation, not accreditation or a licence to practise**. Screening tools = **educational, not diagnostic**.
- No engagement-bait, no dark patterns, no fear-mongering, no shame, no fake vulnerability.
- College+ framing only; no targeting minors.

### Crisis footer (used on posts marked **[FOOTER]**)
```
🆘 Emergency: 112 · Tele-MANAS: 14416 (24×7, MoHFW) · iCall: 9152987821 (Mon–Sat, 10 AM–8 PM) · Manasyn is not an emergency service.
```
*The footer lives **in the caption only**, never baked into the image — so the visual stays clean and the footer can be updated the moment a helpline changes hours.*

---

## 2. FACT-CHECK APPENDIX (verified — cite conservatively)

| Fact | Verified wording | Source |
|---|---|---|
| Treatment gap | National Mental Health Survey (NMHS) 2015–16: overall treatment gap **84.5%**; ranged **70%–92%** by disorder (common mental disorders 85.0%, alcohol use 86.3%, tobacco use 91.8%) | NMHS 2015-16, NIMHANS [1](https://pmc.ncbi.nlm.nih.gov/articles/PMC5419008/) |
| Prevalence | Lifetime **13.67%**, current **10.56%** among adults; ~**150 million** people need care | NMHS 2015-16 [4](https://journals.sagepub.com/doi/abs/10.1177/0020764020907941) |
| Psychiatrist density | ~**0.75 psychiatrists per 100,000** population vs WHO-recommended norm of at least **3** | NMHS / secondary analyses [1](https://anantamias.com/mental-health-treatment-gap/) |
| ⚠️ Attribution | NMHS was **conducted by NIMHANS** and funded by the Ministry of Health & Family Welfare. **It is NOT a WHO survey.** Never write "WHO's National Mental Health Survey" | NIMHANS/NMHS |
| Clinical Psychologist registration | **RCI (Rehabilitation Council of India)** issues registration to Clinical Psychologists, typically via RCI-approved M.Phil / MA-MSc / PsyD routes | RCI [2](https://www.ipn.net.in/faq/) |
| Other psychologists | **NCAHP Act, 2021** lists "Behavioural Health Sciences Professional — Psychologist (except Clinical Psychologist covered under RCI)". Guidelines and licensing processes are still evolving | NCAHP [3](https://www.epsychology.in/blog/what-is-ncahp-registration/) |
| ⚠️ Uncertainty | M.Phil is being phased out under NEP 2020 in favour of RCI-regulated MA Clinical Psychology; **requirements are in flux**. Always write: *"requirements vary — check RCI, NCAHP and your university's current norms"* | RCI/UGC/NCAHP updates |
| iCall | **9152987821**, **Monday to Saturday, 10:00 AM – 8:00 PM**. Run by TISS School of Human Ecology. **NOT 24/7** | TISS [5](https://tiss.ac.in/view/18/projects/icall-telephonic-counselling-service-for-individua/) |
| Tele-MANAS | **14416** (also 1800-891-4416), **24×7**, free, MoHFW / National Tele Mental Health Programme, NIMHANS nodal | MoHFW [6](https://www.iitk.ac.in/counsel/TeleManas.php) |
| Emergency | **112** | — |

**Rule applied:** where a number is not in this table, the post uses no number.

---

## 3. IMAGE GENERATION — MASTER DESIGN PROMPT

Every single image prompt in this document is composed of **[DESIGN SYSTEM] + [MOTIF] + [LAYOUT] + [TEXT]**. The block below is reused verbatim.

### [DESIGN SYSTEM] — append to all 63 prompts
```
LinkedIn editorial graphic, 1080x1350 portrait (or 1080x1080 square where specified).
Background: warm cream #F5F2ED with a very soft vertical gradient toward near-white,
generous negative space with at least 35% of the canvas empty and breathing.
Thin single-weight line-art motif in #3E4A3E at 12-15% opacity, placed as a quiet
background element in one corner only. Accent underline rules, small icons and
numbered markers in #655396 (violet) and #D68C78 (coral), used sparingly.
All headline text in #3E4A3E forest green. All body text in #52615A sage.
Typography: clean geometric sans-serif, high legibility, left-aligned, wide
letter-tracking on small uppercase labels, strong typographic hierarchy.
Absolutely no faces, no people, no hands, no stock photography, no clinical or
hospital imagery, no medical equipment, no dark or fear-based imagery.
Premium, calm, minimal, editorial. Crisp vector-clean rendering, no texture noise.

LOGO: Reproduce the provided logo EXACTLY — do not redraw, recolour, restyle,
crop, stretch or reinterpret it. Place the intact logo small in the bottom-right
corner at approximately 8% of the total canvas width. Its white background blends
seamlessly into the light cream canvas with no visible seam, box or border.
Keep all text areas clear of the logo zone.
```

### [DARK VARIANT] — used on cover slides and quote cards only
```
...same as DESIGN SYSTEM, but background is a deep forest-green #3E4A3E field with
a soft violet #655396 glow in one corner. All text in #F5F2ED cream. Accents in
#D68C78 coral. When the background is dark, place the intact logo inside a small
white rounded-corner card (radius ~14% of card height) in the bottom-right corner,
card width approximately 12% of canvas width. Do not alter the logo itself.
```

### Per-slide text rendering instruction
```
Render the following text exactly as written, letter-perfect, with correct
spelling and punctuation:

HEADLINE: "<headline>"
BODY: "<body>"

[<optional third short label>]
```

---

## 4. SUMMARY CALENDAR — 21 POSTS

| # | Day | Slot | Time (IST) | Type | Theme | Manasyn | Footer |
|---|---|---|---|---|---|---|---|
| 1 | Mon D1 | A | 09:00 | Carousel ×7 | Psychology in India: the map nobody hands you | NO | — |
| 2 | Mon D1 | B | 13:00 | Image 1:1 | 6 questions before you enrol | NO | — |
| 3 | Mon D1 | C | 19:30 | Quote 1:1 | The roadmap is still being written | **YES** | — |
| 4 | Tue D2 | A | 09:30 | Carousel ×7 | Your first session, honestly | NO | — |
| 5 | Tue D2 | B | 13:00 | Image 1:1 | SOAP notes in 60 seconds | **YES** | — |
| 6 | Tue D2 | C | 19:30 | Quote 1:1 | Ethics in a small city | NO | — |
| 7 | Wed D3 | A | 10:00 | Carousel ×7 | The thought record, taught properly | NO | **YES** |
| 8 | Wed D3 | B | 13:00 | Image 1:1 | 4-7-8 breathing, step by step | **YES** | **YES** |
| 9 | Wed D3 | C | 19:30 | Quote 1:1 | A seatbelt, not a steering wheel | NO | **YES** |
| 10 | Thu D4 | A | 09:30 | Carousel ×7 | Starting a practice: the unglamorous list | NO | — |
| 11 | Thu D4 | B | 13:00 | Image 1:1 | 8 agreements before a video session | NO | — |
| 12 | Thu D4 | C | 19:30 | Quote 1:1 | On charging a fair fee | **YES** | — |
| 13 | Fri D5 | A | 09:30 | Carousel ×7 | Burnout is not a character flaw | NO | **YES** |
| 14 | Fri D5 | B | 13:00 | Image 1:1 | Imposter feelings: what's happening | **YES** | **YES** |
| 15 | Fri D5 | C | 19:30 | Quote 1:1 | A work in progress and still useful | NO | **YES** |
| 16 | Sat D6 | A | 10:30 | Carousel ×7 | 5 questions for any mental-health tool | NO | — |
| 17 | Sat D6 | B | 12:00 | Image 1:1 | Where AI helps / where it must never | NO | — |
| 18 | Sat D6 | C | 20:00 | Quote 1:1 | "I can't help with this" | **YES** | **YES** |
| 19 | Sun D7 | A | 10:00 | Carousel ×7 | Seven days, seven useful ideas | NO | — |
| 20 | Sun D7 | B | 12:30 | Image 1:1 | The treatment gap, in one card | **YES** | — |
| 21 | Sun D7 | C | 19:00 | Quote 1:1 | The field needs people who last | NO | — |

**Manasyn mentions: 7 / 21** ✅ (posts 3, 5, 8, 12, 14, 18, 20 — one per day)
**No-mention posts: 14 / 21** ✅

### Posting-time rationale
- LinkedIn India peaks **Tue–Fri 9:30–11:30 AM**. Carousels (Post A) are the highest-reach asset, so they get the peak window on those days and are pulled slightly later on Mon/Sat/Sun when the feed wakes up slower.
- **Post B** at lunch (12:00–13:00) catches the mid-day scroll; Friday moves to 12:30 because Friday afternoons die early.
- **Post C** at 19:00–20:00 catches the evening scroll; Sunday 19:00 is the single strongest evening of the week (people plan the coming week).
- **Saturday evening is the weakest slot of the week.** Day 6 Post C is set to 20:00 and should be treated as a *low-reach* post — expect roughly 40–50% of a weekday evening's impressions. Option: hold it and repost Sunday 10:00 AM.

---
---

# DAY 1 (MONDAY) — CAREERS IN PSYCHOLOGY IN INDIA
*Folder: `linkedin-week/day-01/`*

---

## POST 1A — Carousel (7 slides, 1080×1350)
**Slot A · 09:00 IST · Manasyn: NO · Footer: NO**
**File:** `day-01-postA-slide1.png` … `slide7.png` → assemble to `day-01-postA-carousel.pdf`

### Caption
> Most psychology students in India are told "scope hai" — and handed no map.
>
> So here is the map. Or at least the honest version of it.
>
> Inside: what a degree does and doesn't get you, who regulates what right now, why "RCI-approved" is a question you should ask before you pay a fee, and the fact that the clinic is only one of ten places this degree can take you.
>
> One note I want to be careful about: the rules are genuinely in flux. The M.Phil pathway is being reworked under NEP 2020, and the NCAHP Act, 2021 has created a separate category for psychology professionals outside the RCI's remit. Anyone who tells you the licensure picture is settled and simple is selling you something.
>
> **Requirements vary. Check the RCI website, the NCAHP notifications, and your university's current norms before you commit two years and a fee.**
>
> If you are a student: save this. If you are a practitioner: add what I got wrong in the comments — that comment section will be more useful than the carousel.
>
> What I'd genuinely like to know: **which career path do you wish someone had explained to you before you chose your course?**
>
> #PsychologyStudents #PsychologyCareers #MentalHealthIndia #IndianPsychologists

### Slides

| # | Headline (≤8 words) | Body (≤25 words) | Visual note |
|---|---|---|---|
| 1 | The map nobody hands you | Ten career paths, one honest look at the licence reality, and what to verify first. | **Dark cover** — branching-path line-art motif |
| 2 | Your degree is only step one | BA or BSc builds theory. Registration depends on your course and regulator — check both before enrolling. | Numbered "01" marker, violet |
| 3 | Who regulates what, right now | RCI registers Clinical Psychologists. The NCAHP Act, 2021 covers other psychology professionals. Rules are still evolving. | Two-column diagram, thin rules |
| 4 | Check approval before you pay | Not every MA, MPhil or diploma leads to registration. Verify the institute on the RCI list first. | Checklist line-art |
| 5 | Supervised hours are non-negotiable | Practica, case reports and supervision build competence. No format — online or offline — replaces them. | Hourglass / concentric arcs |
| 6 | The field is wider than the clinic | Schools, hospitals, NGOs, corporate wellbeing, research, forensic, rehabilitation, sport, product, policy. | Ten-dot constellation |
| 7 | Your next step this week | Pick one path. Find one person doing it. Ask one good question. Then save this for later. | **Coral underline** + takeaway lockup |

### Image prompt
```
[DESIGN SYSTEM] + [DARK VARIANT for slide 1 only]
MOTIF: thin continuous line drawing of a path that branches into several
diverging routes, drawn as a single elegant line, in #3E4A3E at 14% opacity,
anchored in the upper-left quadrant, leaving the text area clear.
LAYOUT: 1080x1350. Generous margins of 120px. Small uppercase label top-left
reading "CAREERS IN PSYCHOLOGY · INDIA" in #655396. Headline occupies the
upper-middle third in large bold #3E4A3E. Body text sits below in #52615A at
approximately 40% of headline size. Large slide number in the bottom-left in
light coral #D68C78.
TEXT: <per table above>
```

### Posting time
**09:00 IST, Monday.** Monday morning is inbox/planning mode — slightly after the 8:30 baseline catches people once they settle. Carousels earn longer dwell time so they survive a slower feed.

### Engagement hook
"Which career path do you wish someone had explained to you before you chose your course?"

### Alt text
`Editorial graphic on cream: thin branching-path line-art, headline "The map nobody hands you", body text on psychology career routes and licensure in India, Manasyn logo bottom-right.`

### Manasyn: **NO**

---

## POST 1B — Image post (1080×1080)
**Slot B · 13:00 IST · Manasyn: NO · Footer: NO**
**File:** `day-01-postB.png`

### Caption
> Before you pay a psychology programme fee, ask these six questions.
>
> I keep meeting students in their final semester who discover — too late — that their course doesn't lead where they assumed it did. Not because anyone lied. Because nobody thought to ask out loud.
>
> So ask out loud. In the admissions office, in the WhatsApp group, in the email. The quality of the answers you get tells you almost as much as the answers themselves.
>
> My favourite of the six is #4 — "how many supervised hours, and where?" A programme that can't answer that crisply hasn't thought about your clinical training, only your tuition.
>
> Add your own question in the comments if I missed one. The more of these circulating in student groups, the better decisions people make.
>
> #PsychologyStudents #PsychologyCareers #ClinicalPsychology

### On-image text (6-item checklist)
**Title:** 6 QUESTIONS TO ASK ANY PSYCHOLOGY PROGRAMME
1. Is this programme on the current RCI approved list?
2. How many supervised clinical hours, and where?
3. Who supervises — and are they RCI-registered?
4. What do graduates actually go on to do?
5. Is the mode of study recognised for registration?
6. What happens if the rules change mid-course?

### Image prompt
```
[DESIGN SYSTEM]
MOTIF: thin line-art of an open notebook with a single folded corner, drawn in
#3E4A3E at 13% opacity, positioned in the lower-left as a background whisper.
LAYOUT: 1080x1080 square. Small uppercase label top-left: "BEFORE YOU ENROL"
in #655396. Title beneath in large bold #3E4A3E. Six numbered checklist rows
below, each number as a violet #655396 circle-outline, each item in #52615A,
with thin 1px #3E4A3E rules at 15% opacity separating rows. Generous 96px margins.
TEXT: <per on-image text above>
```

### Posting time
**13:00 IST, Monday.** Lunch scroll; checklists are high-save content and Monday is when students are actively planning.

### Engagement hook
"If you could add a seventh question to this list, what would it be?"

### Alt text
`Checklist graphic on cream with six questions for psychology students to ask before enrolling in a programme, covering approval, supervised hours, supervision and outcomes. Manasyn logo bottom-right.`

### Manasyn: **NO**

---

## POST 1C — Conversation post (1080×1080) → **Manasyn: YES**
**Slot C · 19:30 IST · Footer: NO**
**File:** `day-01-postC.png`

### Caption
> "The scope is real. The roadmap is still being written. Both can be true at once."
>
> Every week I speak to psychology students in India who feel like they've missed a memo everyone else got.
>
> You haven't. The memo doesn't exist yet.
>
> The M.Phil pathway is being reworked. NCAHP has opened a category for psychology professionals who fall outside the RCI's remit. Universities are interpreting all of it at different speeds. That's not you falling behind — that's a profession mid-revision.
>
> What you *can* control in the meantime: build supervised hours, keep real case notes, find one supervisor who will actually read your work, and get comfortable saying "I'll check the current RCI notification and come back to you" instead of guessing.
>
> One thing I've been building, in that spirit: **Manasyn has an educational side for psychology students — AI-simulated clients you can practise on, case studies, and an AI mentor for the questions you're too tired to ask at midnight. It's educational only. It is not accreditation, not training hours, and not a licence to practise. It's free during private beta.**
>
> Genuinely curious: **what's the single most confusing thing about psychology licensure in India right now?** I'll gather the answers and publish a sourced round-up next month.
>
> #PsychologyStudents #PsychologyCareers #MentalHealthIndia #Manasyn

### On-image text (quote card)
**Label:** PSYCHOLOGY IN INDIA
**Quote:** "The scope is real. The roadmap is still being written. Both can be true at once."
**Footer line:** Support. Reflect. Grow.

### Image prompt
```
[DESIGN SYSTEM] + [DARK VARIANT]
MOTIF: thin concentric arc rings, like a partial orbit, drawn in #F5F2ED cream
at 12% opacity in the upper-right, suggesting a route still being drawn.
LAYOUT: 1080x1080 square. Deep forest-green #3E4A3E field with a very soft
violet #655396 radial glow in the upper-right corner. Small uppercase label
top-left "PSYCHOLOGY IN INDIA" in #D68C78. Large serif-feel quote text in
#F5F2ED cream, centre-left, generous line spacing, occupying the middle 55%.
Thin coral #D68C78 rule beneath the quote. Tagline "Support. Reflect. Grow."
in small cream letter-spaced caps at the bottom-left. Logo in a small white
rounded card, bottom-right.
TEXT: <per on-image text above>
```

### Posting time
**19:30 IST, Monday.** Evening scroll; reflection posts perform best when people are winding down rather than working.

### Engagement hook
"What's the single most confusing thing about psychology licensure in India right now?"

### Alt text
`Deep forest-green quote card: "The scope is real. The roadmap is still being written. Both can be true at once." with faint concentric arc line-art and the Manasyn logo in a white rounded card bottom-right.`

### Manasyn: **YES**
**Exact line used (in caption):** "Manasyn has an educational side for psychology students — AI-simulated clients you can practise on, case studies, and an AI mentor for the questions you're too tired to ask at midnight. It's educational only. It is not accreditation, not training hours, and not a licence to practise. It's free during private beta."

---
---

# DAY 2 (TUESDAY) — WHAT COLLEGE DOESN'T TEACH
*Folder: `linkedin-week/day-02/`*

---

## POST 2A — Carousel (7 slides, 1080×1350)
**Slot A · 09:30 IST · Manasyn: NO · Footer: NO**
**File:** `day-02-postA-slide1.png` … `slide7.png` → `day-02-postA-carousel.pdf`

### Caption
> Your first client session will not follow the format in your textbook.
>
> Here's what actually happens, in the order it actually happens.
>
> The gap isn't your fault. Textbooks teach you the *model* of a session. They don't teach you the texture: the forty seconds of silence after "so, what brings you here?", the moment a client asks "will you tell anyone?", the fact that you will be nervous and that the nervousness is not a competence problem.
>
> Seven things that only get learned by doing them badly once and then better:
>
> Slide 4 is the one I'd print and stick above a desk.
>
> **If you're a practitioner reading this: which of these took you the longest to get right?** I suspect the answer is distributed very differently across the profession, and I'd like to see the spread.
>
> #PsychologyStudents #ClinicalPsychology #Psychologists #TherapistLife

### Slides

| # | Headline (≤8 words) | Body (≤25 words) | Visual note |
|---|---|---|---|
| 1 | Your first session, honestly | It will not follow the format in your textbook. Seven things textbooks leave out. | **Dark cover** — two-chair / dialogue line-art |
| 2 | Rapport starts in five minutes | How you greet, where you sit, and what you say about confidentiality set the tone before the work begins. | Two simple chair outlines facing |
| 3 | Explain confidentiality before you ask | Including its limits. Clients relax when they know exactly what stays private and what cannot. | Lock / bracket line-art |
| 4 | Ask, then stop talking | Open with "what brings you here?" and let the silence work. Silence is data, not dead air. | Soundwave flattening to a flat line |
| 5 | Take notes, keep your eyes up | Agree on note-taking out loud. Write sparingly in session; write fully immediately after. | Journal + pen line-art |
| 6 | Close the session on purpose | Summarise, check how the client is leaving, and agree the next step. Never let it just end. | Bracket closing a line |
| 7 | Steal this checklist | Six habits that make first sessions safer for clients and calmer for you. | **Coral underline** + takeaway lockup |

### Image prompt
```
[DESIGN SYSTEM] + [DARK VARIANT for slide 1 only]
MOTIF: minimal line-art of two chairs angled toward each other, drawn in a
single thin #3E4A3E line at 14% opacity, upper-right quadrant, no people.
Where noted per-slide, substitute: a bracket, a journal, or a soundwave.
LAYOUT: 1080x1350. 120px margins. Uppercase label top-left "FIRST SESSIONS"
in #655396. Large bold #3E4A3E headline in the upper-middle. Body in #52615A
below. Slide number bottom-left in coral #D68C78.
TEXT: <per table above>
```

### Posting time
**09:30 IST, Tuesday.** Opens the LinkedIn India peak window (9:30–11:30) — the strongest slot of the week for a carousel.

### Engagement hook
"Which of these took you the longest to get right in your own first sessions?"

### Alt text
`Cream editorial carousel slide with thin two-chair line-art, headline "Your first session, honestly", body text on what textbooks omit about first client sessions. Manasyn logo bottom-right.`

### Manasyn: **NO**

---

## POST 2B — Image post (1080×1080) → **Manasyn: YES**
**Slot B · 13:00 IST · Footer: NO**
**File:** `day-02-postB.png`

### Caption
> The case note is the least taught and most consequential thing you will write.
>
> Not your thesis. Not your formulation essay. The three paragraphs you write after a session, on a Tuesday, when you're tired and the next client is already in the waiting room.
>
> SOAP isn't glamorous and it isn't the only structure, but it's the one that survives contact with a real caseload: **what the client reported, what you observed, what you think it means, what happens next.** In that order. Separate boxes, because collapsing them is how a note quietly becomes an assumption.
>
> Two habits worth building early:
> 1. Write it the same day. Memory degrades faster than you think.
> 2. Quote the client for Subjective, describe for Objective. Never mix them.
>
> **Manasyn's practitioner side exists partly because of this problem — patient records and session documentation built for independent psychologists and counsellors, not repurposed from a hospital system. It's free during private beta.** If documentation is eating your evenings, that's the gap we're trying to close.
>
> What does your note-taking structure look like — SOAP, DAP, BIRP, or something you invented yourself?
>
> #Psychologists #ClinicalPsychology #TherapistLife #MentalHealthProfessionals #Manasyn

### On-image text (mini-framework)
**Title:** SOAP, IN SIXTY SECONDS
- **S — Subjective** · What the client reported, in their words
- **O — Objective** · What you observed: affect, behaviour, engagement
- **A — Assessment** · Your clinical read, and how it's changed
- **P — Plan** · Next step, agreed out loud with the client
**Footer line:** Write it the same day.

### Image prompt
```
[DESIGN SYSTEM]
MOTIF: thin line-art of a single sheet of paper with three ruled lines, in
#3E4A3E at 12% opacity, lower-left background.
LAYOUT: 1080x1080 square. Uppercase label top-left "CASE DOCUMENTATION" in
#655396. Title "SOAP, IN SIXTY SECONDS" in large bold #3E4A3E. Below, four
rows: each with a large violet #655396 letter (S / O / A / P) in a thin circle,
the row title in bold #3E4A3E, and the description in #52615A. Thin 1px rules
at 15% opacity between rows. Bottom line "Write it the same day." in coral
#D68C78. 96px margins.
TEXT: <per on-image text above>
```

### Posting time
**13:00 IST, Tuesday.** Peak weekday; frameworks get saved and reshared by practitioners building their own systems.

### Engagement hook
"What does your note-taking structure look like — SOAP, DAP, BIRP, or something you invented yourself?"

### Alt text
`Cream framework card explaining the SOAP case-note structure with four rows — Subjective, Objective, Assessment, Plan — and the line "Write it the same day." Manasyn logo bottom-right.`

### Manasyn: **YES**
**Exact line used (in caption):** "Manasyn's practitioner side exists partly because of this problem — patient records and session documentation built for independent psychologists and counsellors, not repurposed from a hospital system. It's free during private beta."

---

## POST 2C — Conversation post (1080×1080)
**Slot C · 19:30 IST · Manasyn: NO · Footer: NO**
**File:** `day-02-postC.png`

### Caption
> "In a small city, your client will know your family. Ethics has to be practical before it's theoretical."
>
> Most ethics teaching in India is built for an anonymous metropolis that most of us don't practise in.
>
> The real questions arrive looking nothing like an exam paper:
>
> · Your client sends you a friend request.
> · You meet a client at a wedding. Both of you pretend otherwise.
> · A client's mother asks you how her daughter is doing.
> · You're the only psychologist in a district, and the referral options are four hours away.
> · Your client is also your landlord's nephew.
>
> None of these are in the textbook. All of them are Tuesday.
>
> The principle I find most useful: **decide the boundary before you need it.** A policy you wrote calmly in advance is a completely different thing from a boundary you're negotiating in the moment, with a relationship on the line.
>
> **Practitioners in tier-2 and tier-3 cities — what's the dual-relationship situation you've had to navigate that nobody prepared you for?** I think this is the most under-documented part of Indian practice.
>
> #IndianPsychologists #Psychologists #MentalHealthIndia #TherapistLife

### On-image text (quote card)
**Label:** PRACTICE IN INDIA
**Quote:** "In a small city, your client will know your family. Ethics has to be practical before it's theoretical."
**Footer line:** Decide the boundary before you need it.

### Image prompt
```
[DESIGN SYSTEM]
MOTIF: a thin-line contour map of a small town — a few concentric rings with a
handful of simple building outlines and connecting roads — in #3E4A3E at 12%
opacity, upper-right, abstract and geometric, no people.
LAYOUT: 1080x1080 square. Cream #F5F2ED background with a very soft vertical
gradient. Uppercase label top-left "PRACTICE IN INDIA" in #655396. Large quote
text in #3E4A3E, centre-left, generous line spacing. Thin violet #655396 rule
beneath. Coral #D68C78 sub-line bottom-left: "Decide the boundary before you
need it." Logo bottom-right at 8% width, white background blended into cream.
TEXT: <per on-image text above>
```

### Posting time
**19:30 IST, Tuesday.** Practitioners are free of sessions by evening; identity/ethics posts draw the longest, most substantive comment threads.

### Engagement hook
"Practitioners in tier-2 and tier-3 cities — what's the dual-relationship situation you've had to navigate that nobody prepared you for?"

### Alt text
`Cream quote card with a faint abstract town-map line-art: "In a small city, your client will know your family. Ethics has to be practical before it's theoretical." Manasyn logo bottom-right.`

### Manasyn: **NO**

---
---

# DAY 3 (WEDNESDAY) — CBT CRAFT
*Folder: `linkedin-week/day-03/`*

---

## POST 3A — Carousel (7 slides, 1080×1350)
**Slot A · 10:00 IST · Manasyn: NO · Footer: YES**
**File:** `day-03-postA-slide1.png` … `slide7.png` → `day-03-postA-carousel.pdf`

### Caption
> Most people are handed a thought record worksheet and never taught the sequence.
>
> That's like being handed a musical score and told to "play it with feeling." The worksheet is a container. The skill is the order — and the order is where almost everyone goes wrong.
>
> The two mistakes I see most:
>
> 1. **Jumping from situation straight to "balanced thought."** The reframe arrives fully formed, generated by the part of the mind that was already anxious. It feels tidy and changes nothing.
> 2. **Rating the emotion only once.** Without a before and after, you have no evidence the exercise did anything — and no way to notice when it isn't working.
>
> The sequence inside: situation → emotion + rating → the exact automatic thought → evidence both ways → balanced statement → re-rate.
>
> A note I care about: **a worksheet is not therapy.** If distress stays high or climbs while someone works through this, that's information — it's time for a qualified professional, not a longer worksheet.
>
> 🆘 Emergency: 112 · Tele-MANAS: 14416 (24×7, MoHFW) · iCall: 9152987821 (Mon–Sat, 10 AM–8 PM) · Manasyn is not an emergency service.
>
> **Clinicians: how do you introduce the thought record so clients don't experience it as homework?**
>
> #CBT #ClinicalPsychology #Psychologists #PsychologyStudents

### Slides

| # | Headline (≤8 words) | Body (≤25 words) | Visual note |
|---|---|---|---|
| 1 | The thought record, taught properly | Seven steps, in order. Most people get the worksheet and never the sequence. | **Dark cover** — 7-step staircase line-art |
| 2 | Step 1 — Describe the situation | Facts only, like a camera. Who, what, when, where. No interpretation, no "and then I felt". | Step badge "01", violet |
| 3 | Step 2 — Name and rate emotion | Name the feeling precisely and rate intensity 0–10. Sad, disappointed and ashamed are not the same. | Thermometer-scale line-art |
| 4 | Step 3 — Catch the automatic thought | The exact words in your head, first person, present tense. Not a summary — the sentence itself. | Speech-bubble outline, thin |
| 5 | Steps 4–5 — Weigh the evidence | Evidence for. Evidence against. Real facts, not reassurance. If it isn't observable, it isn't evidence. | Balance / two-pan line-art |
| 6 | Step 6 — Write a balanced thought | Not positive. Accurate. A statement you can believe at 70% and a good friend would accept. | Converging lines |
| 7 | Step 7 — Re-rate, then take away | Re-rate the emotion 0–10. Small movement counts. A worksheet is not therapy — know when to refer. | **Coral underline** + takeaway lockup |

### Image prompt
```
[DESIGN SYSTEM] + [DARK VARIANT for slide 1 only]
MOTIF: per-slide thin line-art — a seven-step ascending staircase; a 0-to-10
scale; an empty speech-bubble outline; a two-pan balance; two lines converging.
All in #3E4A3E at 13% opacity, upper-right, no people, no hands.
LAYOUT: 1080x1350. 120px margins. Uppercase label top-left "CBT CRAFT" in
#655396. Large bold #3E4A3E headline upper-middle. Body in #52615A below.
Step number as a large coral #D68C78 numeral bottom-left.
TEXT: <per table above>
```

### Posting time
**10:00 IST, Wednesday.** Mid-week peak; a step-by-step teaching carousel is a save-and-return asset, and mid-week is when practitioners look for material to use in Thursday sessions.

### Engagement hook
"Clinicians: how do you introduce the thought record so clients don't experience it as homework?"

### Alt text
`Cream carousel slide with thin staircase line-art, headline "The thought record, taught properly", body text on teaching CBT thought records in sequence. Manasyn logo bottom-right.`

### Manasyn: **NO**

---

## POST 3B — Image post (1080×1080) → **Manasyn: YES**
**Slot B · 13:00 IST · Footer: YES**
**File:** `day-03-postB.png`

### Caption
> 4-7-8 breathing is one of the most taught and least explained techniques in the field.
>
> Here it is properly: **inhale through the nose for 4, hold for 7, exhale through the mouth for 8.** The ratio matters more than the absolute count. If 4-7-8 is too long, scale it to 2-3.5-4 — same proportion, smaller numbers. The exhale being roughly twice the inhale is the part doing the work.
>
> Three things worth saying out loud:
>
> · It is a **regulation** technique, not a cure. It changes a state, not a condition.
> · A little light-headedness on the first couple of rounds is common. If it's more than mild, stop.
> · It works better practised when calm than deployed when panicking. **Skill before crisis.**
>
> **We've built guided 4-7-8 and 5-senses grounding into Manasyn, with voice sessions in English, हिंदी, मैथिली and भोजपुरी — free during private beta. They're self-guided wellness tools: not therapy, not treatment, and not a substitute for working with a professional.**
>
> 🆘 Emergency: 112 · Tele-MANAS: 14416 (24×7, MoHFW) · iCall: 9152987821 (Mon–Sat, 10 AM–8 PM) · Manasyn is not an emergency service.
>
> Which breathing or grounding technique do you actually find yourself recommending most — and has it changed over your career?
>
> #CBT #Psychologists #MentalHealthIndia #Manasyn

### On-image text (step card)
**Title:** 4-7-8 BREATHING, DONE PROPERLY
1. **Inhale** through the nose — 4 counts
2. **Hold** — 7 counts
3. **Exhale** through the mouth — 8 counts
4. **Repeat** 4 rounds. Scale to 2-3.5-4 if needed.
**Footer line:** Practise it calm. Use it later.

### Image prompt
```
[DESIGN SYSTEM]
MOTIF: three concentric breathing-circle outlines, thin, in #3E4A3E at 12%
opacity, positioned in the upper-right, with a small coral #D68C78 arc marking
one segment of the outer ring.
LAYOUT: 1080x1080 square. Uppercase label top-left "CBT CRAFT · GROUNDING"
in #655396. Title in large bold #3E4A3E. Four numbered rows beneath, each with
a violet #655396 circle-outline numeral, a bold #3E4A3E verb (Inhale / Hold /
Exhale / Repeat) and a #52615A description. Thin 1px rules at 15% opacity
between rows. Coral sub-line at the bottom: "Practise it calm. Use it later."
96px margins.
TEXT: <per on-image text above>
```

### Posting time
**13:00 IST, Wednesday.** Lunch break is exactly when people try a breathing exercise; high save + high send-to-a-friend rate.

### Engagement hook
"Which breathing or grounding technique do you actually find yourself recommending most — and has that changed over your career?"

### Alt text
`Cream step card with concentric breathing-circle line-art explaining the 4-7-8 breathing technique in four numbered steps and the line "Practise it calm. Use it later." Manasyn logo bottom-right.`

### Manasyn: **YES**
**Exact line used (in caption):** "We've built guided 4-7-8 and 5-senses grounding into Manasyn, with voice sessions in English, हिंदी, मैथिली and भोजपुरी — free during private beta. They're self-guided wellness tools: not therapy, not treatment, and not a substitute for working with a professional."

---

## POST 3C — Conversation post (1080×1080)
**Slot C · 19:30 IST · Manasyn: NO · Footer: YES**
**File:** `day-03-postC.png`

### Caption
> "A breathing exercise is a seatbelt, not a steering wheel."
>
> I think the mental-health internet has a calibration problem.
>
> On one side, self-help tools get marketed as though a worksheet can do the work of a therapeutic relationship. On the other, any tool that isn't a full course of therapy gets dismissed as useless.
>
> Both are wrong, and the people who pay for it are the ones in the middle — someone who can't access a psychologist this month and needs *something* that isn't nothing.
>
> A more honest framing: **regulation techniques change a state. Therapy changes a pattern.** A breathing exercise can help you get through the next twenty minutes. It will not resolve why the twenty minutes keep happening. Both of those things matter, and confusing them helps nobody.
>
> The standard I'd like to hold every tool to — including the one we're building — is simply this: **say clearly what you are, and say clearly what you are not.**
>
> 🆘 Emergency: 112 · Tele-MANAS: 14416 (24×7, MoHFW) · iCall: 9152987821 (Mon–Sat, 10 AM–8 PM) · Manasyn is not an emergency service.
>
> **Where do you draw the line between self-help and therapy when a client asks you about an app?**
>
> #CBT #Psychologists #ClinicalPsychology #MentalHealthIndia

### On-image text (quote card)
**Label:** ON SELF-HELP
**Quote:** "A breathing exercise is a seatbelt, not a steering wheel."
**Footer line:** Regulation changes a state. Therapy changes a pattern.

### Image prompt
```
[DESIGN SYSTEM]
MOTIF: a single thin continuous line that curves and loops into a loose knot
before continuing forward — abstract, geometric, in #3E4A3E at 13% opacity,
upper-right, no people.
LAYOUT: 1080x1080 square. Cream #F5F2ED with soft vertical gradient. Uppercase
label top-left "ON SELF-HELP" in #655396. Large quote text in #3E4A3E,
centre-left, generous line spacing, middle 55%. Thin violet #655396 rule
beneath. Coral #D68C78 sub-line bottom-left: "Regulation changes a state.
Therapy changes a pattern." Logo bottom-right at 8% width, white background
blended into the cream.
TEXT: <per on-image text above>
```

### Posting time
**19:30 IST, Wednesday.** Evening; a calibration/ethics post invites the reflective, longer-form comments that LinkedIn rewards.

### Engagement hook
"Where do you draw the line between self-help and therapy when a client asks you about an app?"

### Alt text
`Cream quote card with a thin looping-line motif: "A breathing exercise is a seatbelt, not a steering wheel." Sub-line: "Regulation changes a state. Therapy changes a pattern." Manasyn logo bottom-right.`

### Manasyn: **NO**

---
---

# DAY 4 (THURSDAY) — BUILDING A PRIVATE PRACTICE
*Folder: `linkedin-week/day-04/`*

---

## POST 4A — Carousel (7 slides, 1080×1350)
**Slot A · 09:30 IST · Manasyn: NO · Footer: NO**
**File:** `day-04-postA-slide1.png` … `slide7.png` → `day-04-postA-carousel.pdf`

### Caption
> Nobody tells psychology graduates that private practice is roughly 40% clinical work and 60% paperwork, boundaries and admin.
>
> The clinical part you've been trained for. The other 60% is where practices quietly fail.
>
> Six decisions that matter more than your logo, your website or your visiting card — none of which are taught in any syllabus I've seen:
>
> · **Scope** — write down what you do and don't treat, before a client asks.
> · **Fees** — in writing, stated before the first session, including cancellation.
> · **Consent** — a signed document, not a verbal nod.
> · **Records** — written for the clinician who reads them next.
> · **Online agreements** — platform, location, identity, emergency plan, dropouts.
> · **Referral network** — built before you need it, not during.
>
> The unglamorous truth: most of what protects a practice is decided in the first month and never revisited. Revisit it annually.
>
> **If you run a practice: what's the admin system you'd build again from scratch, and what would you throw out?**
>
> #Psychologists #IndianPsychologists #TherapistLife #MentalHealthProfessionals

### Slides

| # | Headline (≤8 words) | Body (≤25 words) | Visual note |
|---|---|---|---|
| 1 | Starting a practice: the unglamorous list | Six decisions that matter more than your logo, your website or your visiting card. | **Dark cover** — open-door / threshold line-art |
| 2 | Decide your scope before your brand | Write down what you do and do not treat. Referral is a clinical skill, not a failure. | Bracketed list line-art |
| 3 | Write your fees down, say them clearly | State fees before the first session, in writing. Clarity protects the client and protects you. | Document + line line-art |
| 4 | Consent is a document, not a vibe | Informed consent covers method, risks, limits of confidentiality, fees and cancellation. Signed, dated, filed. | Signature-rule line-art |
| 5 | Your records are your professional memory | Date, session number, what changed, risk noted, plan agreed. Write for the next clinician. | Stacked-file line-art |
| 6 | Online work needs extra agreements | Platform, location, identity, emergency plan, and what happens if the connection drops. | Screen-frame line-art |
| 7 | Build slow, document everything | Private practice is mostly admin and boundaries. Plan for it and the clinical work gets room. | **Coral underline** + takeaway lockup |

### Image prompt
```
[DESIGN SYSTEM] + [DARK VARIANT for slide 1 only]
MOTIF: per-slide thin line-art — a doorway threshold; a bracketed list; a ruled
document; a signature line; stacked files; a simple screen frame. All in
#3E4A3E at 13% opacity, upper-right, no people, no hands, no furniture brands.
LAYOUT: 1080x1350. 120px margins. Uppercase label top-left "PRIVATE PRACTICE"
in #655396. Large bold #3E4A3E headline upper-middle. Body in #52615A below.
Slide number bottom-left in coral #D68C78.
TEXT: <per table above>
```

### Posting time
**09:30 IST, Thursday.** Second-strongest weekday peak; practice-building content gets reshared into professional WhatsApp groups, which compounds reach.

### Engagement hook
"If you run a practice: what's the admin system you'd build again from scratch, and what would you throw out?"

### Alt text
`Cream carousel slide with thin doorway-threshold line-art, headline "Starting a practice: the unglamorous list", body text on the six non-clinical decisions that matter most. Manasyn logo bottom-right.`

### Manasyn: **NO**

---

## POST 4B — Image post (1080×1080)
**Slot B · 13:00 IST · Manasyn: NO · Footer: NO**
**File:** `day-04-postB.png`

### Caption
> Eight things to agree before the first video session — not during it.
>
> Online work is now ordinary practice in India, and most of the problems I hear about aren't clinical. They're the unglamorous logistics nobody agreed in advance: the client is driving, the connection drops mid-disclosure, the "confidential space" is a shared bedroom.
>
> Agree all eight in the first session or in a written onboarding note. It takes ten minutes and removes an entire category of awkwardness.
>
> My two that get skipped most often:
>
> **#4 — the emergency plan.** Agreeing *beforehand* what happens if a client is at risk, including who their local emergency contact is and what you'd do if they go silent, is the single most important agreement on this list.
>
> **#6 — the dropout protocol.** "If we lose connection, I'll call you back in two minutes; if I can't reach you in ten, I'll contact your emergency contact." Say it once, in session one.
>
> Which of these did you only learn to add *after* something went wrong?
>
> #Psychologists #IndianPsychologists #TherapistLife #MentalHealthProfessionals

### On-image text (checklist)
**Title:** BEFORE THE FIRST VIDEO SESSION — AGREE 8 THINGS
1. Which platform, and who pays for it
2. The client's physical location during sessions
3. Confirming identity at the start
4. The emergency plan, and a local contact
5. Confidentiality limits at the client's end
6. What happens if the connection drops
7. Session length, fee and cancellation terms
8. Whether sessions may be recorded (usually: no)

### Image prompt
```
[DESIGN SYSTEM]
MOTIF: a thin-line rectangular screen frame with a small signal arc in one
corner, #3E4A3E at 12% opacity, upper-right, no people, no interface text.
LAYOUT: 1080x1080 square. Uppercase label top-left "ONLINE CONSULTATION" in
#655396. Title in large bold #3E4A3E across two lines. Eight numbered rows
below, each with a small violet #655396 circle-outline numeral and #52615A
text at a compact but legible size. Thin 1px rules at 15% opacity between
rows. 88px margins.
TEXT: <per on-image text above>
```

### Posting time
**13:00 IST, Thursday.** Practical checklists get saved heavily on weekdays; Thursday lunch still sits inside the active part of the week.

### Engagement hook
"Which of these did you only learn to add after something went wrong?"

### Alt text
`Cream checklist card listing eight agreements to make before a first online therapy session, including emergency plan, platform, location and connection-drop protocol. Manasyn logo bottom-right.`

### Manasyn: **NO**

---

## POST 4C — Conversation post (1080×1080) → **Manasyn: YES**
**Slot C · 19:30 IST · Footer: NO**
**File:** `day-04-postC.png`

### Caption
> "Charging a fair fee is not greed. Unclear fees are what actually damage trust."
>
> I've watched early-career psychologists in India do something quietly self-destructive: undercharge, feel resentful, raise the fee mid-therapy without warning, and then carry the guilt of it for a year.
>
> The dynamics worth naming:
>
> · **Undercharging isn't kindness.** It's a subsidy you pay for out of your own sustainability, and practices that burn out serve nobody.
> · **Sliding scales are legitimate** — but they need a stated policy, not case-by-case improvisation that leaves clients guessing.
> · **The damage is done by surprise, not by amount.** A client who knows the fee and agrees to it is fine. A client who discovers it on the invoice isn't.
> · **Say the number out loud, in the first conversation, in writing.** Every time.
>
> Transparency isn't only an ethical posture — it's the thing that lets you keep doing this work for twenty years.
>
> **On transparency: Manasyn is free during private beta, and we intend to publish pricing openly before that changes. If you're an independent practitioner, you deserve to know what a tool will cost before you build your workflow around it — we're not going to surprise anyone.**
>
> **How did you arrive at your first fee — and would you do it the same way now?**
>
> #Psychologists #IndianPsychologists #TherapistLife #Manasyn

### On-image text (quote card)
**Label:** ON FEES
**Quote:** "Charging a fair fee is not greed. Unclear fees are what actually damage trust."
**Footer line:** Say the number out loud, in writing, every time.

### Image prompt
```
[DESIGN SYSTEM]
MOTIF: a thin-line balance scale with a single beam and two open circles,
abstract and geometric, #3E4A3E at 12% opacity, upper-right.
LAYOUT: 1080x1080 square. Cream #F5F2ED with a very soft vertical gradient.
Uppercase label top-left "ON FEES" in #655396. Large quote text in #3E4A3E,
centre-left, generous line spacing, middle 55%. Thin violet #655396 rule
beneath. Coral #D68C78 sub-line bottom-left: "Say the number out loud, in
writing, every time." Logo bottom-right at 8% width, white background blended
into the cream.
TEXT: <per on-image text above>
```

### Posting time
**19:30 IST, Thursday.** Money conversations land best in the evening when practitioners are out of session and reflective about the business side.

### Engagement hook
"How did you arrive at your first fee — and would you do it the same way now?"

### Alt text
`Cream quote card with a thin balance-scale line-art: "Charging a fair fee is not greed. Unclear fees are what actually damage trust." Manasyn logo bottom-right.`

### Manasyn: **YES**
**Exact line used (in caption):** "On transparency: Manasyn is free during private beta, and we intend to publish pricing openly before that changes. If you're an independent practitioner, you deserve to know what a tool will cost before you build your workflow around it — we're not going to surprise anyone."

---
---

# DAY 5 (FRIDAY) — THE HELPER'S MIND
*Folder: `linkedin-week/day-05/`*
**All three posts carry the crisis footer.**

---

## POST 5A — Carousel (7 slides, 1080×1350)
**Slot A · 09:30 IST · Manasyn: NO · Footer: YES**
**File:** `day-05-postA-slide1.png` … `slide7.png` → `day-05-postA-carousel.pdf`

### Caption
> Burnout in the helping professions is not a personal failure. It's an occupational hazard — and hazards are things you plan for.
>
> I want to be careful here, so let me be precise about what I'm claiming and what I'm not.
>
> **What I'm saying:** exhaustion that rest doesn't fix, distance from clients, and a quiet drop in confidence are patterns that show up again and again in caring work. They're signals about load and fit, not verdicts on your character.
>
> **What I'm not saying:** that any of this is a diagnosis, that there's a protocol here, or that a carousel substitutes for supervision. It doesn't. If these patterns are persistent and affecting your work or your life, that's a conversation for a professional you trust — not a LinkedIn post.
>
> The three things worth building before you need them: **supervision booked like a client, a caseload ceiling you actually respect, and a life outside the room.**
>
> 🆘 Emergency: 112 · Tele-MANAS: 14416 (24×7, MoHFW) · iCall: 9152987821 (Mon–Sat, 10 AM–8 PM) · Manasyn is not an emergency service.
>
> **What's the one thing that genuinely restores you — not the thing you think should?**
>
> #Psychologists #TherapistLife #MentalHealthProfessionals #MentalHealthIndia

### Slides

| # | Headline (≤8 words) | Body (≤25 words) | Visual note |
|---|---|---|---|
| 1 | Burnout is not a character flaw | It is an occupational signal. Naming it early is a professional skill, not a confession. | **Dark cover** — guttering-candle / arc line-art |
| 2 | Exhaustion that rest doesn't fix | When a weekend doesn't restore you, the problem isn't your stamina. It's the load, or the fit. | Descending-bar line-art |
| 3 | Distance from clients is a sign | Feeling detached, going through the motions, dreading the diary. Notice it early; it's information. | Two figures of dots drifting apart |
| 4 | Holding stories has a cost | Repeated exposure to other people's trauma changes helpers. Naming it makes it manageable. | Nested-arc line-art |
| 5 | Supervision is the job, not extra | Peer consultation is where competence is maintained. Book it like a client, not like a favour. | Two-circle overlap line-art |
| 6 | Self-compassion is a clinical skill | You cannot offer a steadiness you never practise. The work starts with how you speak to yourself. | Hand-cupped-circle line-art (abstract) |
| 7 | Plan to last, not to impress | Sustainable careers beat heroic ones. Rest, supervision and limits are part of good practice. | **Coral underline** + takeaway lockup |

### Image prompt
```
[DESIGN SYSTEM] + [DARK VARIANT for slide 1 only]
MOTIF: per-slide thin line-art — a softly guttering candle flame; descending
bars; two constellations of dots drifting apart; nested arcs; two overlapping
circles; an abstract cupped circle. All in #3E4A3E at 12% opacity, upper-right.
No people, no flames rendered realistically, nothing alarming or dark-feeling —
the tone stays calm and held, never frightening.
LAYOUT: 1080x1350. 120px margins. Uppercase label top-left "THE HELPER'S MIND"
in #655396. Large bold #3E4A3E headline upper-middle. Body in #52615A below.
Slide number bottom-left in coral #D68C78.
TEXT: <per table above>
```

### Posting time
**09:30 IST, Friday.** Post early in the peak window — Friday attention collapses after ~2 PM, and a heavy topic needs the larger morning audience to find the right readers.

### Engagement hook
"What's the one thing that genuinely restores you — not the thing you think should?"

### Alt text
`Cream carousel slide with a soft abstract guttering-flame line-art, headline "Burnout is not a character flaw", body text reframing burnout as an occupational signal. Manasyn logo bottom-right.`

### Manasyn: **NO**

---

## POST 5B — Image post (1080×1080) → **Manasyn: YES**
**Slot B · 12:30 IST · Footer: YES**
**File:** `day-05-postB.png`

### Caption
> Almost every competent psychologist I know has felt, at some point, like a fraud waiting to be found out.
>
> Here's the reframe that helped me most, and I want to be honest that it's a reframe and not a study finding: **the feeling and the competence are running on different clocks.** Competence accumulates slowly and invisibly. The feeling of fraudulence is loudest exactly when your standards have just risen faster than your skills — which is a sign of growth, not of fraud.
>
> Four things that reliably make it worse in Indian training contexts:
>
> · Comparing your **internal** uncertainty to someone's **external** confidence.
> · Supervision cultures where questions read as weakness.
> · Being the only psychologist in the room, with no peers to calibrate against.
> · Never seeing senior clinicians admit what they don't know.
>
> And one that helps: **name it out loud to one peer.** The feeling loses most of its power the moment it's spoken in a room where someone nods.
>
> **Part of why Manasyn's student side is built the way it is: AI-simulated clients you can get wrong, with no supervisor watching and no consequence. Educational only — it isn't training hours, isn't accreditation, and isn't a licence to practise. Free during private beta.**
>
> 🆘 Emergency: 112 · Tele-MANAS: 14416 (24×7, MoHFW) · iCall: 9152987821 (Mon–Sat, 10 AM–8 PM) · Manasyn is not an emergency service.
>
> **When did the imposter feeling actually start to loosen for you — or has it?**
>
> #PsychologyStudents #Psychologists #TherapistLife #MentalHealthIndia #Manasyn

### On-image text (insight card)
**Title:** IMPOSTER FEELINGS: WHAT'S ACTUALLY HAPPENING
- Your standards are rising faster than your skills → it feels like falling behind. It isn't.
- You compare your **inside** to everyone else's **outside**.
- Confidence and competence run on different clocks.
- Naming it to one peer removes most of its weight.
**Footer line:** It's a signal of growth, not of fraud.

### Image prompt
```
[DESIGN SYSTEM]
MOTIF: two thin arc lines of very different lengths running parallel and
slowly converging, #3E4A3E at 12% opacity, upper-right — abstract, geometric,
no people.
LAYOUT: 1080x1080 square. Uppercase label top-left "THE HELPER'S MIND" in
#655396. Title in large bold #3E4A3E. Four bullet rows below, each with a small
violet #655396 diamond marker and #52615A text; the words "inside" and
"outside" set in bold #3E4A3E. Thin 1px rules at 15% opacity between rows.
Coral #D68C78 sub-line at the bottom: "It's a signal of growth, not of fraud."
92px margins.
TEXT: <per on-image text above>
```

### Posting time
**12:30 IST, Friday.** Pulled 30 minutes earlier than the baseline — Friday afternoon engagement drops sharply, and this is the post most likely to be read by students finishing the week.

### Engagement hook
"When did the imposter feeling actually start to loosen for you — or has it?"

### Alt text
`Cream insight card with converging-arc line-art on imposter feelings: rising standards, inside-versus-outside comparison, and the line "It's a signal of growth, not of fraud." Manasyn logo bottom-right.`

### Manasyn: **YES**
**Exact line used (in caption):** "Part of why Manasyn's student side is built the way it is: AI-simulated clients you can get wrong, with no supervisor watching and no consequence. Educational only — it isn't training hours, isn't accreditation, and isn't a licence to practise. Free during private beta."

---

## POST 5C — Conversation post (1080×1080)
**Slot C · 19:30 IST · Manasyn: NO · Footer: YES**
**File:** `day-05-postC.png`

### Caption
> "You are allowed to be a work in progress and still be useful to someone today."
>
> The thing I'd say to every psychology student in India reading this at the end of a hard week:
>
> You are being trained in a field where the raw material is human distress, in a country where the need vastly exceeds the workforce, by a system that is still deciding what your qualification is called. That is a genuinely heavy thing to carry, and if it feels heavy, that is an accurate reading of the situation — not a personal inadequacy.
>
> Some things that are true and worth holding:
>
> · You don't need to be finished to be helpful.
> · Rest is not a reward for completing the work. It's part of the work.
> · Asking for help is a professional competency, not a confession.
> · Nobody in this field has it figured out. Some have just been at it longer.
>
> Be kind to yourself this weekend. Not as a treat — as maintenance.
>
> 🆘 Emergency: 112 · Tele-MANAS: 14416 (24×7, MoHFW) · iCall: 9152987821 (Mon–Sat, 10 AM–8 PM) · Manasyn is not an emergency service.
>
> **What's one thing you're going to stop doing this weekend to make room for rest?**
>
> #PsychologyStudents #Psychologists #TherapistLife #MentalHealthIndia

### On-image text (quote card)
**Label:** FOR THE WEEKEND
**Quote:** "You are allowed to be a work in progress and still be useful to someone today."
**Footer line:** Rest is maintenance, not a reward.

### Image prompt
```
[DESIGN SYSTEM] + [DARK VARIANT]
MOTIF: a single thin continuous line that rises in a soft, irregular wave —
never a straight ascent — in #F5F2ED cream at 13% opacity, upper-right.
LAYOUT: 1080x1080 square. Deep forest-green #3E4A3E field with a very soft
violet #655396 radial glow upper-right. Uppercase label top-left "FOR THE
WEEKEND" in #D68C78. Large quote text in #F5F2ED cream, centre-left, generous
line spacing, middle 55%. Thin coral #D68C78 rule beneath. Small cream
letter-spaced sub-line bottom-left: "Rest is maintenance, not a reward."
Logo in a small white rounded card, bottom-right.
TEXT: <per on-image text above>
```

### Posting time
**19:30 IST, Friday.** End-of-week reflection post; Friday evening is strong for warm, generous content as people close the working week.

### Engagement hook
"What's one thing you're going to stop doing this weekend to make room for rest?"

### Alt text
`Deep green quote card with a faint rising-wave line: "You are allowed to be a work in progress and still be useful to someone today." Manasyn logo in a white rounded card bottom-right.`

### Manasyn: **NO**

---
---

# DAY 6 (SATURDAY) — MENTAL HEALTH × TECHNOLOGY
*Folder: `linkedin-week/day-06/`*

---

## POST 6A — Carousel (7 slides, 1080×1350)
**Slot A · 10:30 IST · Manasyn: NO · Footer: NO**
**File:** `day-06-postA-slide1.png` … `slide7.png` → `day-06-postA-carousel.pdf`

### Caption
> Before you recommend any mental-health app to a client, ask it these five questions.
>
> I build in this space, so I want to be clear about my interest: **I think these questions should be asked of every tool in the category, including ours.** A field where only the bad tools get scrutinised is a field where nobody trusts anything.
>
> The five:
>
> 1. **What data does it collect, and where does it live?**
> 2. **What happens when someone is at risk?**
> 3. **Does it say what it is not?**
> 4. **Who is accountable when it's wrong?**
> 5. **What does the evidence actually support?**
>
> My strong opinion: **question 3 is the tell.** A tool that volunteers its own limits — that says "I'm not therapy, I'm not diagnosis, I'm not for emergencies" without being asked — is usually built by people who've thought hard about the rest. A tool that only talks about what it can do has often not considered what it shouldn't.
>
> "Vague answers are answers" is the line I'd most want students to take from this.
>
> **Clinicians: have you ever had a client bring an app into session? How did you handle it?**
>
> #MentalHealthIndia #Psychologists #ClinicalPsychology #MentalHealthProfessionals

### Slides

| # | Headline (≤8 words) | Body (≤25 words) | Visual note |
|---|---|---|---|
| 1 | Five questions for any mental-health tool | Ask these before you recommend an app to a client, a student or a colleague. | **Dark cover** — question-mark-as-arc line-art |
| 2 | What data does it collect? | What is stored, where it lives, who can read it, and how long it's kept. Vague answers are answers. | Nested-database line-art |
| 3 | What happens at risk? | If someone discloses risk, does the tool escalate — and to whom? A tool that goes silent has chosen. | Branching-alert line-art |
| 4 | Does it say what it is not? | Therapy? Diagnosis? Emergency care? Honest tools name their limits without being asked. | Circle with a defined edge |
| 5 | Who is accountable when it's wrong? | Is there a named human, a complaints route and a clinical review process? Or only a terms page? | Chain-of-nodes line-art |
| 6 | What does the evidence actually support? | Ask whether claims were tested, on whom, and published. Marketing language is not evidence. | Bar-and-baseline line-art |
| 7 | Ask before you recommend | AI literacy is now part of clinical literacy. Save these five for your next tool conversation. | **Coral underline** + takeaway lockup |

### Image prompt
```
[DESIGN SYSTEM] + [DARK VARIANT for slide 1 only]
MOTIF: per-slide thin line-art — a question mark rendered as an open arc;
nested rounded squares; a branching alert path; a circle with one defined
segment; a chain of nodes; three bars against a baseline. All in #3E4A3E at
13% opacity, upper-right. Abstract, geometric, no screens showing faces, no
robots, no humanoid imagery.
LAYOUT: 1080x1350. 120px margins. Uppercase label top-left "AI LITERACY FOR
CLINICIANS" in #655396. Large bold #3E4A3E headline upper-middle. Body in
#52615A below. Slide number bottom-left in coral #D68C78.
TEXT: <per table above>
```

### Posting time
**10:30 IST, Saturday.** The weekend feed starts later. Saturday morning is quieter but the audience that is present is in browsing mode, which suits a save-able framework carousel.

### Engagement hook
"Clinicians: have you ever had a client bring an app into session? How did you handle it?"

### Alt text
`Cream carousel slide with abstract question-mark arc line-art, headline "Five questions for any mental-health tool", body text on data, risk escalation and stated limits. Manasyn logo bottom-right.`

### Manasyn: **NO**

---

## POST 6B — Image post (1080×1080)
**Slot B · 12:00 IST · Manasyn: NO · Footer: NO**
**File:** `day-06-postB.png`

### Caption
> Where AI helps in mental health — and where it must never.
>
> A two-column card, because I think this is the most useful thing a clinician can hand a curious client.
>
> **Where it genuinely helps:** structure and repetition. Practising a thought record at 11 PM. Journaling prompts that ask the same good question every day. Drafting the boring parts of documentation so you spend your attention on the clinical parts. Simulated clients for students who need repetition without consequences. Reducing the friction between "I should" and "I did."
>
> **Where it must never:** risk assessment and crisis response. Diagnosis. Deciding medication. Reading a specific person's mind at a specific moment. Being the only thing between someone and their distress. Substituting for a relationship with a trained human.
>
> The dividing line isn't "complex vs simple." It's: **does getting this wrong cost someone their safety?** If yes, a human is in the loop. Not adjacent to the loop — in it.
>
> This is a position I hold about our own product too, and I'd rather say that plainly than imply otherwise.
>
> **Where would you draw the line differently?**
>
> #MentalHealthIndia #Psychologists #ClinicalPsychology #MentalHealthProfessionals

### On-image text (two-column comparison)
**Title:** WHERE AI HELPS · WHERE IT MUST NEVER

**HELPS** (violet #655396 column)
- Repetition and practice
- Journaling prompts
- Drafting documentation
- Simulated clients for students
- Lowering the friction to start

**NEVER** (coral #D68C78 column)
- Risk assessment
- Crisis response
- Diagnosis
- Medication decisions
- Replacing human care

**Footer line:** Does getting it wrong cost someone their safety? Then a human stays in the loop.

### Image prompt
```
[DESIGN SYSTEM]
MOTIF: a single thin vertical hairline dividing the card, with a small circle
at its midpoint, #3E4A3E at 12% opacity — abstract, no people, no robots.
LAYOUT: 1080x1080 square. Uppercase label top-left "MENTAL HEALTH ×
TECHNOLOGY" in #655396. Title across two lines in large bold #3E4A3E, with
"WHERE AI HELPS" set in #655396 and "WHERE IT MUST NEVER" set in #D68C78.
Below, two clearly separated columns with generous gutter: left column header
"HELPS" in #655396 with five #52615A bullet rows; right column header "NEVER"
in #D68C78 with five #52615A bullet rows. Thin 1px vertical rule at 15% opacity
between columns. Coral #D68C78 sub-line across the bottom: "Does getting it
wrong cost someone their safety? Then a human stays in the loop." 88px margins.
TEXT: <per on-image text above>
```

### Posting time
**12:00 IST, Saturday.** Weekend lunchtime; comparison cards are the most reshared format in this category, and resharing compounds over the weekend.

### Engagement hook
"Where would you draw the line differently?"

### Alt text
`Two-column card on cream: violet "HELPS" column listing repetition, prompts, documentation and simulated clients; coral "NEVER" column listing risk assessment, crisis response and diagnosis. Manasyn logo bottom-right.`

### Manasyn: **NO**

---

## POST 6C — Conversation post (1080×1080) → **Manasyn: YES**
**Slot C · 20:00 IST · Footer: YES**
**File:** `day-06-postC.png`

### Caption
> "An AI tool that never says 'I can't help with this' is not confident. It's careless."
>
> The most under-rated feature in any mental-health technology isn't the model, the interface or the language support. It's the refusal.
>
> A tool that will talk to anyone about anything, at any hour, with total confidence and no escalation path, is not a supportive product. It's a product that has decided — by omission — that it can safely handle whatever arrives. Nothing can safely handle whatever arrives.
>
> What honest design looks like in practice:
>
> · Stating plainly that it is **not therapy, not diagnosis, not an emergency service**.
> · Showing crisis contacts without being asked, at the moment they're relevant.
> · Declining to engage with certain disclosures and handing off to a human.
> · Being clear that screening questionnaires are **educational, not diagnostic** — a score is a starting point for a conversation, not an answer.
>
> **Manasyn's AI states its limits inside the app, and Manasyn is not a therapy, diagnostic or emergency service. I don't think that's a competitive disadvantage — I think it's the minimum standard every tool in this space should be held to, ours included.**
>
> 🆘 Emergency: 112 · Tele-MANAS: 14416 (24×7, MoHFW) · iCall: 9152987821 (Mon–Sat, 10 AM–8 PM) · Manasyn is not an emergency service.
>
> **If you could mandate one disclosure from every mental-health app, what would it be?**
>
> #MentalHealthIndia #Psychologists #ClinicalPsychology #Manasyn

### On-image text (quote card)
**Label:** HONEST AI
**Quote:** "An AI tool that never says 'I can't help with this' is not confident. It's careless."
**Footer line:** The most under-rated feature is the refusal.

### Image prompt
```
[DESIGN SYSTEM]
MOTIF: a thin circle with one clean, deliberate gap in its outline, #3E4A3E at
13% opacity, upper-right — abstract and geometric, suggesting a stated limit
rather than something broken.
LAYOUT: 1080x1080 square. Cream #F5F2ED with a very soft vertical gradient.
Uppercase label top-left "HONEST AI" in #655396. Large quote text in #3E4A3E,
centre-left, generous line spacing, middle 55%. Thin violet #655396 rule
beneath. Coral #D68C78 sub-line bottom-left: "The most under-rated feature is
the refusal." Logo bottom-right at 8% width, white background blended into
the cream.
TEXT: <per on-image text above>
```

### Posting time
**20:00 IST, Saturday.** ⚠️ **Lowest-reach slot of the week** — Saturday evening LinkedIn India is quiet. Expect roughly 40–50% of a weekday evening's impressions. Two options: post as scheduled and accept lower reach, or hold it and run Sunday 10:00 AM with Post 7A shifted to 11:00 AM.

### Engagement hook
"If you could mandate one disclosure from every mental-health app, what would it be?"

### Alt text
`Cream quote card with a thin circle broken by one deliberate gap: "An AI tool that never says 'I can't help with this' is not confident. It's careless." Manasyn logo bottom-right.`

### Manasyn: **YES**
**Exact line used (in caption):** "Manasyn's AI states its limits inside the app, and Manasyn is not a therapy, diagnostic or emergency service. I don't think that's a competitive disadvantage — I think it's the minimum standard every tool in this space should be held to, ours included."

---
---

# DAY 7 (SUNDAY) — REFLECTION & COMMUNITY
*Folder: `linkedin-week/day-07/`*

---

## POST 7A — Carousel (7 slides, 1080×1350)
**Slot A · 10:00 IST · Manasyn: NO · Footer: NO**
**File:** `day-07-postA-slide1.png` … `slide7.png` → `day-07-postA-carousel.pdf`

### Caption
> Seven days, twenty-one posts, one question: was any of it actually useful to you?
>
> Here's the week compressed — one idea per day, for psychology students and practitioners in India.
>
> **Mon** — careers and the licensure reality
> **Tue** — first sessions and case documentation
> **Wed** — CBT craft, taught in sequence
> **Thu** — building a private practice
> **Fri** — the helper's mind
> **Sat** — mental health × technology
> **Sun** — this
>
> The through-line, if there is one: **most of what makes this work sustainable is learned outside the syllabus.** Rapport, records, fees, boundaries, rest. The syllabus teaches the model. The profession runs on the rest.
>
> So: **what should we cover next week?**
>
> I mean it as a real question, not a rhetorical one. Reply with the topic you wish Indian psychology content covered better and I'll build the week around the strongest themes.
>
> #PsychologyStudents #Psychologists #MentalHealthIndia #IndianPsychologists

### Slides

| # | Headline (≤8 words) | Body (≤25 words) | Visual note |
|---|---|---|---|
| 1 | Seven days, seven useful ideas | A compressed recap for psychology students and practitioners in India. Skim, save, steal. | **Dark cover** — seven-dot arc |
| 2 | Monday — careers and licensure | Verify institute approval, ask about supervised hours, and treat regulator sites as the source. | Compass-arc line-art |
| 3 | Tuesday — first sessions and notes | Rapport before technique. Notes written the same day. Ethics made practical for small cities. | Two-chair line-art |
| 4 | Wednesday — CBT craft | Thought records taught in order. Breathing and grounding as skills, not cures. | Seven-step line-art |
| 5 | Thursday — building a practice | Scope first, fees in writing, consent documented, records as professional memory. | Document-stack line-art |
| 6 | Friday — the helper's mind | Burnout is occupational. Supervision is the job. Self-compassion is a clinical skill. | Nested-arc line-art |
| 7 | What should we cover next? | Tell us the one topic you wish Indian psychology content covered better. We'll build around it. | **Coral underline** + takeaway lockup |

### Image prompt
```
[DESIGN SYSTEM] + [DARK VARIANT for slide 1 only]
MOTIF: per-slide thin line-art — seven dots along a shallow arc; a compass
arc; two chairs; seven ascending steps; a document stack; nested arcs. All in
#3E4A3E at 13% opacity, upper-right. Abstract, geometric, no people.
LAYOUT: 1080x1350. 120px margins. Uppercase label top-left "WEEK IN REVIEW"
in #655396. A small day marker (MON / TUE / WED / THU / FRI / SAT) in coral
#D68C78 above the headline. Large bold #3E4A3E headline upper-middle. Body in
#52615A below. Slide number bottom-left in violet #655396.
TEXT: <per table above>
```

### Posting time
**10:00 IST, Sunday.** Sunday late morning catches the planning-the-week audience; recap carousels get saved for Monday.

### Engagement hook
"What should we cover next week? Reply with the topic you wish Indian psychology content covered better."

### Alt text
`Cream carousel slide with a seven-dot arc line-art, headline "Seven days, seven useful ideas", body text recapping a week of content for psychology students and practitioners in India. Manasyn logo bottom-right.`

### Manasyn: **NO**

---

## POST 7B — Image post (1080×1080) → **Manasyn: YES**
**Slot B · 12:30 IST · Footer: NO**
**File:** `day-07-postB.png`

### Caption
> The treatment gap in India, in four numbers.
>
> Sourced carefully, because numbers in this space get stretched:
>
> · **~150 million** people in India need mental health care.
> · **84.5%** overall treatment gap — roughly five in six people with a mental disorder receive no care.
> · **70%–92%** — the gap ranges by disorder (common mental disorders 85.0%, alcohol use disorders 86.3%).
> · **0.75** psychiatrists per 100,000 people, against a WHO-recommended norm of at least 3.
>
> All four figures come from the **National Mental Health Survey of India 2015–16**, conducted by NIMHANS and funded by the Ministry of Health and Family Welfare. Worth knowing: it's now about a decade old, and the survey's own authors treat prevalence figures as conservative because of under-reporting. **Treat these as a floor, not as today's exact number.**
>
> Two reasons I'm sharing this on a Sunday rather than as a hook: because the number deserves more than outrage, and because the response it calls for isn't panic — it's workforce, access and honest triage.
>
> **On access: Manasyn is free during private beta. That's a deliberate choice while we work out pricing that doesn't put tools behind a wall — self-guided wellness tools for individuals, and clinic management for independent practitioners. It is not therapy and not diagnosis, and it doesn't close a gap this large. Nothing single-handed does.**
>
> **If you work in this field: what's the most under-used lever we have for closing this gap?**
>
> #MentalHealthIndia #Psychologists #MentalHealthProfessionals #Manasyn

### On-image text (stat card)
**Label:** INDIA · NATIONAL MENTAL HEALTH SURVEY 2015–16
- **~150 million** — people needing mental health care
- **84.5%** — overall treatment gap
- **70–92%** — gap range, by disorder
- **0.75** — psychiatrists per 100,000 (WHO norm: 3+)
**Footer line:** Figures are a floor, not today's exact number.

### Image prompt
```
[DESIGN SYSTEM]
MOTIF: a thin-line horizontal bar with one long filled segment and one very
short filled segment — abstract, geometric, #3E4A3E at 12% opacity with the
short segment in coral #D68C78, upper-right.
LAYOUT: 1080x1080 square. Uppercase label top-left "INDIA · NATIONAL MENTAL
HEALTH SURVEY 2015-16" in #655396 at small size. Four stat rows: each with a
very large bold numeral in #3E4A3E on the left and a short #52615A descriptor
on the right, separated by thin 1px rules at 15% opacity. Small source line in
#52615A at 60% size near the bottom: "NIMHANS, Ministry of Health and Family
Welfare." Coral #D68C78 sub-line at the very bottom: "Figures are a floor, not
today's exact number." 96px margins.
TEXT: <per on-image text above>
```

### Posting time
**12:30 IST, Sunday.** Stat cards get saved and cited; Sunday midday gives it time to accumulate before the Monday morning wave.

### Engagement hook
"If you work in this field: what's the most under-used lever we have for closing this gap?"

### Alt text
`Cream stat card citing India's National Mental Health Survey 2015-16: about 150 million people needing care, 84.5% treatment gap, 70-92% range by disorder, 0.75 psychiatrists per 100,000. Manasyn logo bottom-right.`

### Manasyn: **YES**
**Exact line used (in caption):** "On access: Manasyn is free during private beta. That's a deliberate choice while we work out pricing that doesn't put tools behind a wall — self-guided wellness tools for individuals, and clinic management for independent practitioners. It is not therapy and not diagnosis, and it doesn't close a gap this large. Nothing single-handed does."

---

## POST 7C — Conversation post (1080×1080)
**Slot C · 19:00 IST · Manasyn: NO · Footer: NO**
**File:** `day-07-postC.png`

### Caption
> "The field doesn't need more heroes. It needs more people who last."
>
> Closing the week with the thing I believe most about this profession in India.
>
> We are very good at celebrating the psychologist who runs a free clinic at midnight, sees forty clients a week and never says no. We are less good at protecting them.
>
> But the person who closes a gap of 84.5% isn't a hero working themselves to nothing. It's a thousand practitioners with sustainable caseloads, real supervision, documented work, fair fees, and careers that last thirty years instead of six.
>
> So if you take one thing from this week: **build the version of this career you can still be doing in 2045.** Boring systems, honest limits, actual rest. That's not the unambitious path. It's the only one that gets us there.
>
> Thank you to everyone who commented, corrected and added this week. Several of you fixed things I got wrong, publicly, and the thread is better for it. That's the whole point of doing this on LinkedIn instead of in a broadcast.
>
> Next week's themes are open. Tell me what to build.
>
> **What's the one piece of advice you'd give to someone starting out, that you'd want them to hear in year one rather than year ten?**
>
> #PsychologyStudents #Psychologists #MentalHealthIndia #IndianPsychologists

### On-image text (quote card)
**Label:** CLOSING THE WEEK
**Quote:** "The field doesn't need more heroes. It needs more people who last."
**Footer line:** Build the career you can still be doing in 2045.

### Image prompt
```
[DESIGN SYSTEM] + [DARK VARIANT]
MOTIF: a long thin horizontal line with seven small evenly spaced dots along
it, extending past the right edge, #F5F2ED cream at 13% opacity, upper-right —
suggesting duration rather than intensity.
LAYOUT: 1080x1080 square. Deep forest-green #3E4A3E field with a very soft
violet #655396 radial glow upper-right. Uppercase label top-left "CLOSING THE
WEEK" in #D68C78. Large quote text in #F5F2ED cream, centre-left, generous
line spacing, middle 55%. Thin coral #D68C78 rule beneath. Small cream
letter-spaced sub-line bottom-left: "Build the career you can still be doing
in 2045." Logo in a small white rounded card, bottom-right.
TEXT: <per on-image text above>
```

### Posting time
**19:00 IST, Sunday.** The strongest evening slot of the week — people plan the coming week on Sunday night, and a closing reflection post converts that attention into follows.

### Engagement hook
"What's the one piece of advice you'd give to someone starting out, that you'd want them to hear in year one rather than year ten?"

### Alt text
`Deep green quote card with a faint horizontal line of seven dots: "The field doesn't need more heroes. It needs more people who last." Manasyn logo in a white rounded card bottom-right.`

### Manasyn: **NO**

---
---

# 5. CAROUSEL → PDF WORKFLOW (LinkedIn document posts)

LinkedIn document posts (PDF) consistently outperform multi-image posts for carousels. **Do not upload 7 separate PNGs as an image carousel.**

### Exact slide order
Assemble each day's carousel strictly as:

```
day-0N-postA-slide1.png   ← cover (dark variant)
day-0N-postA-slide2.png
day-0N-postA-slide3.png
day-0N-postA-slide4.png
day-0N-postA-slide5.png
day-0N-postA-slide6.png
day-0N-postA-slide7.png   ← takeaway + soft CTA
→ day-0N-postA-carousel.pdf   (7 pages, 1080×1350 each, portrait)
```

### Build command
```bash
# One PDF per day, from that day's 7 slides, in filename order
python3 scripts/build-carousel-pdf.py day-01
```
*(Script to be added — assembles slides to a 1080×1350-per-page PDF with zero added margins.)*

### LinkedIn upload notes
- Post type: **Document** (📄 icon), not "Photo".
- Add a short title in the document title field (it appears above the doc): `Psychology in India: the map nobody hands you`
- Caption goes in the post body — the same caption text above.
- **First ~140 characters of the caption must carry the hook** — LinkedIn truncates the body behind "…see more" on mobile at roughly 140–210 characters. Every hook line above is written to survive that fold.
- Vertical 1080×1350 renders full-height in the LinkedIn document viewer. Keep text within the central 80% so nothing is clipped by the viewer's rounded corners.

---

# 6. ENGAGEMENT PLAYBOOK

## 6.1 The 60-minute daily reply routine

Split into **two 30-minute windows**, not one hour. Reply velocity in the first 90 minutes after posting is what LinkedIn's ranking rewards most.

**Window 1 — +30 to +60 min after each post (30 min)**
1. **Reply to every substantive comment** (a paragraph or more) with a real answer — not "Thanks for sharing!" Minimum 2 sentences, ideally referencing something specific they said.
2. **Ask one follow-up question** in each reply. A reply that ends in a question doubles the chance of a second round, and second rounds are what push a post into other feeds.
3. **Never reply to the easy comment first.** Sort by most thoughtful, not most recent.

**Window 2 — +4 to +6 hours after posting (30 min)**
4. **Reply to the late comments** — these are often from a different time zone / different professional cohort, and they extend the post's life.
5. **Tag no one** unless they asked to be tagged.
6. **Pin the best comment** to the top of the thread on carousels — a practitioner adding a correction or an extra tip makes the whole post more credible.

**Daily totals across 3 posts:** ~60–75 min. If time is short, prioritise **Post A (carousel)** replies first — it carries the most reach — then Post C (conversation), which is engineered for comments.

## 6.2 When Saurabh should comment as founder

**Comment as founder (personal profile, Saurabh Kumar) when:**
- Someone **corrects or challenges** a claim → acknowledge, thank, and commit to checking. This is the single highest-trust action available.
- Someone shares **lived professional experience** (a tier-2 dual-relationship story, a first-fee story) → respond with a genuine reflection, not a pitch.
- Someone asks **"is this an ad?"** or questions Manasyn → answer directly and plainly: what it is, what it isn't, that it's free in beta. Never defend; clarify.
- Someone asks a **technical or product** question → answer it yourself, briefly, and offer to continue over DM or email (aura777ai@gmail.com).

**Do NOT comment as founder when:**
- The thread is flowing well between peers. Your presence can flatten peer-to-peer conversation — let practitioners talk to each other.
- The comment is a drive-by "Great post!" — a founder reply adds nothing and costs credibility.
- **Never** pivot a comment thread to a product pitch. On the 7 Manasyn-mention posts the product appears once, in the caption, and stays there.

**Founder signature move:** once or twice a week, leave a comment that **adds new value** rather than responding — an extra tip, a caveat, a resource. That is what makes people follow the profile.

## 6.3 Resharing carousels from personal → company page

**Recommended flow (personal first, always):**

1. **Post from Saurabh's personal profile at the scheduled time.** Personal profiles out-reach company pages on LinkedIn by a wide margin, and this is where the comments happen.
2. **Wait 24 hours.** Let the personal post accumulate its comment thread.
3. **Reshare to the Manasyn company page** with the 🔁 repost button, choosing **"Repost with your thoughts"** rather than a bare repost.
4. **Write a fresh angle in the reshare, not a copy of the caption.** Best-performing framings:
   - *"Our founder's post on [topic] got a comment thread worth your time — particularly [specific insight]. Sharing here so it doesn't get lost in the feed."*
   - *"We published this for psychology students in India. The comments from practising psychologists are the better version of it — see below."*
   - *"One correction from the thread we want to surface: [correction]. Updating our own understanding in public."*
5. **Never reshare all 21.** Reshare **Post A (carousel) only** — 7 reshares max across the week, one per day, 24 hours behind. Resharing all three daily slots makes the company page read as a broadcast feed and suppresses reach on everything.
6. **Link the comment thread.** When you reshare with thoughts, explicitly point people to the comments. It drives traffic back to the personal post and keeps one conversation in one place instead of splitting it.

## 6.4 Weekly rhythm

| Day | Priority |
|---|---|
| Mon | Post A replies (careers posts draw students — highest volume, lowest depth) |
| Tue–Thu | Peak activity. Full 60-min routine, all three posts |
| Fri | Post A + Post C (burnout posts need careful, slow replies — do not batch-rush these) |
| Sat | Light: check once, ~15 min. Low reach is expected |
| Sun | Post A reshare to company page + plan next week from the Post 7A comments |

## 6.5 What to do with the corrections

Several posts deliberately invite practitioners to correct the content (Posts 1A, 1C, 5A). When they do:
1. **Reply and thank them publicly.**
2. **Edit the post** if the correction is factual — LinkedIn allows editing, and editing with a visible correction is a credibility signal.
3. **Collect every correction** into the sourced round-up promised in Post 1C. That post then becomes next month's highest-value asset.

---

# 7. IMAGE PRODUCTION PLAN (post-approval)

**Total: 63 images** — 49 carousel slides (7 days × 7 slides) + 14 single images (7 × Post B, 7 × Post C).

Generation is capped at ~10 images per turn, so this runs as **7 batches of 9**. Each batch = one full day.

| Batch | Turn | Assets | Count |
|---|---|---|---|
| 1 | T1 | `day-01-postA-slide1…7` + `day-01-postB` + `day-01-postC` | 9 |
| 2 | T2 | `day-02-postA-slide1…7` + `day-02-postB` + `day-02-postC` | 9 |
| 3 | T3 | `day-03-postA-slide1…7` + `day-03-postB` + `day-03-postC` | 9 |
| 4 | T4 | `day-04-postA-slide1…7` + `day-04-postB` + `day-04-postC` | 9 |
| 5 | T5 | `day-05-postA-slide1…7` + `day-05-postB` + `day-05-postC` | 9 |
| 6 | T6 | `day-06-postA-slide1…7` + `day-06-postB` + `day-06-postC` | 9 |
| 7 | T7 | `day-07-postA-slide1…7` + `day-07-postB` + `day-07-postC` | 9 |
| 8 | T8 | QA sweep + PDF assembly + any regenerations | — |

### QA checklist — applied to all 63, per batch
- [ ] Logo present, **pixel-identical** to `linkedin-week/assets/logo.png` — correct colours, correct lockup, tagline legible
- [ ] Logo at **6–10% of canvas width**, bottom-right (or in a white rounded card on dark designs)
- [ ] Logo not cropped, stretched, recoloured or reinterpreted
- [ ] Every headline and body string **letter-perfect** against the source table — no dropped words, no invented words, no punctuation drift
- [ ] Palette correct: `#3E4A3E` / `#655396` / `#D68C78` / `#F5F2ED` / `#52615A` only
- [ ] No faces, no people, no hands, no stock or clinical imagery
- [ ] Devanagari (हिंदी / मैथिली / भोजपुरी on `day-03-postB`) renders correctly with proper conjuncts
- [ ] Dimensions correct: 1080×1350 carousels, 1080×1080 singles
- [ ] Any drift → regenerate that image immediately before moving to the next batch

### Sequence
1. **Confirm logo** (§0 blocker) → copy to `linkedin-week/assets/logo.png`
2. Add `scripts/build-carousel-pdf.py`
3. Batches 1–7, one per turn, QA'ing each before the next
4. Batch 8: full QA sweep, PDF assembly, `ALT-TEXT.md` final pass
5. Commit + push to `arena/01a0a103-manasyn-ads`

---

## 8. COMPLIANCE SIGN-OFF

| Rule | Status |
|---|---|
| Manasyn never = therapy / diagnosis / replacement | ✅ stated in posts 3, 8, 9, 18, 20 and implied in 12, 14 |
| No cure / outcome guarantees | ✅ no post promises results |
| No fake testimonials, clinician names, credentials | ✅ none used |
| No invented statistics | ✅ all figures trace to §2 |
| NMHS correctly attributed to NIMHANS/MoHFW, **not** WHO | ✅ corrected from brief |
| iCall never described as 24/7 | ✅ hours stated every time it appears |
| No implied Tele-MANAS / government affiliation | ✅ referenced only as a public helpline in the footer |
| No optimisation for "manas" alone | ✅ always "Manasyn" |
| Crisis footer on distress / burnout / suicide-adjacent posts | ✅ posts 7, 8, 9, 13, 14, 15, 18 |
| No engagement-bait / fear / shame | ✅ all hooks are content previews or genuine questions |
| College+ framing, no minors | ✅ |
| Student tools = educational, not a licence | ✅ stated in posts 3, 14 |
| Screening tools = educational, not diagnostic | ✅ stated in post 18 |
| 7 / 21 Manasyn mentions | ✅ posts 3, 5, 8, 12, 14, 18, 20 |
| Hashtags 3–5, from the approved list | ✅ |
