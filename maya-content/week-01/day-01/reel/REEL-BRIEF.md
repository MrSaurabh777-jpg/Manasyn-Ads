# Reel — "Raat ke 1 baje kisse baat karein?" (Post 1 · AI Companion · 30 s · 9:16)

Six shots. Shots 1–5 are AI keyframes (this folder → `keyframes/`) that you animate with a free image-to-video tool; shot 6 is a finished end card (no animation needed). Stitch + text + music in CapCut. Total ≈ 30 s.

```
reel/
├── keyframes/shot-01-hook-1080x1920.jpg      0–5 s   restless, staring at the ceiling
├── keyframes/shot-02-scroll-1080x1920.jpg    5–10 s  doom-scrolling, face lit by the phone
├── keyframes/shot-03-open-1080x1920.jpg      10–15 s sits up, opens Manasyn, face softens
├── keyframes/shot-04-talk-1080x1920.jpg      15–20 s speaks quietly to the phone (voice check-in)
├── keyframes/shot-05-rest-1080x1920.jpg      20–25 s phone face-down, asleep, lamp dimmed
├── shot-06-end-card-1080x1920.jpg            25–30 s logo · CTA · disclaimer · helplines (still image)
└── reel-cover-1080x1920.jpg                  Reel cover / thumbnail
```
All keyframes are exactly 1080×1920, same woman, same room, no text — text is added in CapCut so it stays crisp and editable.

---

## 1. Which AI to use (free)

| Tool | Why | Free allowance (changes often — check the app) | Watermark |
|---|---|---|---|
| **Kling AI** (klingai.com / app) — **first choice** | Best face/character consistency from a still, 1080p, 5 s clips, "start + end frame" option | daily free credits (≈ 3–6 standard 5 s clips/day) | small logo bottom corner |
| **Hailuo AI** (hailuoai.video, by MiniMax) — backup | Fast, natural motion for people, no watermark on free | ≈ 10 clips/day, 6 s, 720p | none |
| Google Gemini app / Flow (Veo) — optional | Most cinematic + native ambient sound, 8 s | a few free generations/day on some accounts | Veo mark |
| **CapCut** (free, phone or desktop) | Stitch clips, on-screen text, music, export 1080×1920 | free | none on standard export |

**Plan:** do all 5 shots in Kling in **Standard** mode (cheapest credits, 5 s). If you run out of daily credits, finish the remaining shots in Hailuo the same day (720p is fine for Reels once mixed in CapCut). Generate each shot twice if credits allow and keep the better one.

**Kling settings:** Image to Video → upload the keyframe → paste the motion prompt below → Negative prompt (below) → Mode *Standard* → Duration *5 s* → Creativity/“relevance” slider towards *relevance* (keeps the face) → Generate.
**Hailuo settings:** Image to Video → upload → same prompt (shorten if needed) → 6 s.

**Negative prompt (paste in every shot):**
```text
text, subtitles, captions, letters, logo, watermark, extra fingers, deformed hands, distorted face, face changing, morphing, second person, fast motion, camera shake, flicker, blur, cartoon
```

---

## 2. Shot list with motion prompts

Keep motion small — the realism comes from subtle movement. Each prompt describes a 5 s clip.

### Shot 1 · 0–5 s · HOOK — `keyframes/shot-01-hook-1080x1920.jpg`
```text
Slow, gentle camera push-in. The woman lies still staring at the ceiling, blinks slowly, exhales, and turns her head slightly toward the phone on the pillow. The phone screen glows faintly and flickers once. Fairy lights twinkle softly. Realistic, subtle, cinematic night mood, no camera shake.
```
### Shot 2 · 5–10 s · PROBLEM — `keyframes/shot-02-scroll-1080x1920.jpg`
```text
Static close-up. Her thumb scrolls the phone slowly and repeatedly; the cool light from the screen shifts across her face with each scroll. Her eyes look tired and distant, she blinks slowly. Bokeh fairy lights in the background shimmer gently. Realistic, subtle motion.
```
### Shot 3 · 10–15 s · TURN — `keyframes/shot-03-open-1080x1920.jpg`
```text
Slow camera push-in. Sitting cross-legged, she looks at the phone; a soft teal glow brightens on her face, her expression relaxes into a small hopeful smile and she breathes out. Fairy lights glow steadily. Realistic, gentle, warm and calm, no sudden movement.
```
### Shot 4 · 15–20 s · SPEAKING IN HER LANGUAGE — `keyframes/shot-04-talk-1080x1920.jpg`
```text
Static profile close-up. She speaks quietly toward the phone, lips moving naturally as in a calm conversation, small nods, eyes relaxed. Tiny teal particles of light drift slowly between her face and the phone screen. Soft lamp rim light, realistic skin, subtle motion.
```
### Shot 5 · 20–25 s · OUTCOME — `keyframes/shot-05-rest-1080x1920.jpg`
```text
Very slow camera pull-back. She sleeps peacefully on her side, slow breathing visible in the blanket, the bedside lamp dims a little further, fairy lights glow softly, the phone stays face-down on the nightstand. Calm, resolved, quiet night, realistic.
```
### Shot 6 · 25–30 s · END CARD — `shot-06-end-card-1080x1920.jpg`
Still image, 5 s. Optional: CapCut → *Animation → In → Fade* (0.5 s). Nothing else needed — logo, CTA, disclaimer and helplines are already on it.

---

## 3. On-screen text (add in CapCut)

Style: font **Poppins Bold** (or Montserrat ExtraBold), white, size ≈ 60–70 pt on a 1080 canvas, subtle drop shadow or a 50 % navy (`#0F172A`) box; highlight words in teal `#0D9488` or mint `#5EEAD4`. Keep text in the middle 60 % of the screen (Instagram's UI covers the top and bottom ~15 %).

| Time | Line 1 | Line 2 (smaller) |
|---|---|---|
| 0.0–2.5 s | **Raat ke 1:12 baje.** | |
| 2.5–5.0 s | **Sab so gaye. Aur aap?** | |
| 5.0–7.5 s | **Kisi ko call karein?** | *"Itni raat ko? Aur bolenge kya?"* |
| 7.5–10 s | **Toh phir… scroll.** 📱 | |
| 10–15 s | **Yahin se shuru hota hai —** | **Manasyn AI Companion** (teal) · *guided check-in, chatbot nahi* |
| 15–17.5 s | **English · हिंदी · मैथिली · भोजपुरी** | *ya pure Hinglish mein* |
| 17.5–20 s | **Jaise sochte ho, waise bolo.** | |
| 20–22.5 s | **Mood · neend · stress notice karta hai** | |
| 22.5–25 s | **Ek chhoti report —** | **apne psychologist se share karo** |
| 25–30 s | (end card — no extra text) | |

Add **auto-captions** only if you record the voiceover (below); otherwise the text above is enough.

---

## 4. Voiceover script (optional, ≈ 28 s, calm female voice, Hinglish)

Record on your phone in a quiet room, or use CapCut *Text-to-speech* (pick an Indian-English / Hindi voice), or ask me to generate it.

```text
Raat ke ek baje. Sab so gaye… aur aap chhat ko ghoor rahe ho.
Kisi ko call karein? Itni raat ko? Toh phir… scroll.
Yahin se shuru hota hai Manasyn ka AI Companion — ek guided check-in, chatbot nahi.
English, Hindi, Maithili ya Bhojpuri — jaise sochte ho, waise bolo.
Yeh aapke mood, neend aur stress ko notice karta hai, aur ek chhoti report banata hai, jo aap apne psychologist se share kar sakte ho.
Abhi private beta mein free. manasyn.app
```

---

## 5. Music

CapCut → Audio → Sounds → search **"calm lo-fi"**, **"soft piano night"** or **"ambient hopeful"** (≈ 70–85 BPM, no vocals). Volume −18 dB if there is a voiceover, −8 dB if not. Fade out over the end card. (If you post from a Business account, Instagram's own music library is limited — CapCut's commercial-safe tracks avoid the problem.)

---

## 6. CapCut steps (10 minutes)

1. New project → ratio **9:16** → import the 5 generated clips + `shot-06-end-card-1080x1920.jpg`.
2. Put them on the timeline in order; trim each clip to **5.0 s** (end card 5.0 s). Total 30 s.
3. Transitions: none between 1→2→3 (hard cuts feel real); *Dissolve 0.4 s* between 4→5 and 5→6.
4. Speed: if any clip has slightly odd motion, set it to 0.9× and trim — slow reads as calm.
5. Text: add the lines from §3 at the times shown. Same style for all.
6. Audio: music (§5) + voiceover (§4) if you have it.
7. Colour (optional): Adjust → Warmth −5, Contrast +5 on all clips for a matched look.
8. Export: **1080×1920, 30 fps, high bitrate, MP4**. Smart HDR off.
9. Cover: when posting, choose *Add from camera roll* → `reel-cover-1080x1920.jpg`.

**Check before export:** no AI-tool watermark cut through the text · nothing on screen says therapy / diagnosis / cure / "download the app" · end card visible for a full 5 s (helplines must be readable).

---

## 7. Posting

**Where/when:** Instagram Reel (also share to Feed) + Facebook Reel. Best slot: **Day 2 (Tue 29 Sep) 8:00 AM IST** as the Manasyn Spotlight, so Day 1's three posts stay clean — or the same day at 6:00 PM if you want it out today. Repost the same file as a **Threads** video and on **X** (native video, ≤ 2:20) with the caption below.

**Reel caption (Instagram / Facebook / Threads):**
```text
Raat ke 1 baje kisse baat karein? 🌙

Sab so gaye, aur dimaag mein 50 tabs khule hain. Kisi ko call karna ajeeb lagta hai, toh scroll… aur scroll.

Manasyn ka AI Companion ek guided check-in hai — chatbot nahi. Sahi agla sawaal poochta hai, aapki bhasha mein (English, हिंदी, मैथिली, भोजपुरी ya Hinglish), aapke mood, neend aur stress ko notice karta hai, aur ek chhoti report banata hai jo aap apne psychologist ke saath share kar sakte ho. 💚

Saaf baat: yeh therapy nahi hai, diagnosis nahi hai. Lekin pehli baatcheet yahan se shuru ho sakti hai.

Abhi private beta mein free 👉 manasyn.app (link in bio)

Aap raat ko dimaag band na hone par kya karte ho? Comment mein batao 👇

🆘 Emergency: 112 · Tele-MANAS: 14416 (24×7) · iCall: 9152987821 (Mon–Sat, 10 AM–8 PM) · Manasyn is not an emergency service.
```
**First comment (hashtag Set B — Post 1 used Set A on the feed):**
```text
#manasyn #manasynapp #mindcareai #MentalHealthApp #AICompanion #MindcareIndia #MentalHealthSupport #MentalHealthTools #DigitalMentalHealth #MentalHealthTech #SelfHelpApp #MindfulTech #AnxietySupport #SleeplessNights #LateNightThoughts #RacingThoughts #CheckInWithYourself #HinglishMentalHealth #MentalHealthHindi #BharatMentalHealth #IndianYouth #StudentMentalHealth #WorkStressIndia #YouAreNotAlone #Reels
```
**X (video ≤ 280 chars):**
```text
1 AM. Everyone's asleep. You aren't.

Manasyn's AI Companion is a guided check-in, not a chatbot — in English, Hindi, Maithili or Bhojpuri, with a report you can share with your psychologist. Free in beta 💚 manasyn.app

Not therapy or an emergency service. India: 112 · Tele-MANAS 14416
```
**Alt text / accessibility caption:** "30-second Reel: a young Indian woman awake at 1 AM opens the Manasyn AI Companion on her phone, talks in her own language and falls asleep calmly. Ends with manasyn.app and helplines."

**Instagram settings:** tick *AI label* if Instagram asks (the visuals are AI-generated) · turn on *Share to Facebook* · reply to every comment in the first hour.
