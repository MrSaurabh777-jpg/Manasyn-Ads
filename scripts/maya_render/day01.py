"""Render all final, ready-to-post images for Week 1 · Day 1.
Usage:  python3 scripts/maya_render/day01.py [post1|post2|post3|all]
"""
from __future__ import annotations
import os, sys
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(__file__))
from lib import *  # noqa

DAY = os.path.join(ROOT, "maya-content", "week-01", "day-01")
SRC = os.path.join(DAY, "images")
OUT = os.path.join(DAY, "final")


def base(name) -> Image.Image:
    return Image.open(os.path.join(SRC, name)).convert("RGBA")


# =====================================================================================
# POST 1 — Manasyn Spotlight (photo + overlay)
# =====================================================================================
P1_HEAD = "Raat ke 1 baje\nkisse baat karein?"
P1_SUB = "Manasyn ka AI Companion — ek guided check-in, aapki bhasha mein."
P1_LANG = "English · Hindi · Maithili · Bhojpuri · Hinglish"
P1_MICRO = "Free during private beta  ·  manasyn.app"


def p1_header(img, badge_size=17):
    d = ImageDraw.Draw(img)
    place_logo(img, "emblem", 76, (32, 32), card=True)
    pill(d, (img.size[0] - 32, 46), "Manasyn Feature", inter(badge_size, 600), TEAL, star=True)


def p1_square():
    img = base("post1-spotlight-base.png")  # 1080x1080
    gradient(img, 520, 1080, NAVY, 0, 235)
    p1_header(img)
    y = glow_text(img, (56, 730), P1_HEAD, poppins(60, "Bold"), WHITE, 900, 1.08)
    d = ImageDraw.Draw(img)
    y = par(d, (56, y + 14), P1_SUB, inter(22, 400), LIGHT, 760, 1.3)
    y = par(d, (56, y + 6), P1_LANG, inter(19, 500), TEAL_L, 760, 1.3)
    par(d, (56, y + 12), P1_MICRO, inter(16, 600), GREEN, 760)
    watermark(img, dark=True)
    return img


def p1_portrait():  # 1080x1350: photo on top, caption plate below
    img = Image.new("RGBA", (1080, 1350), (*NAVY, 255))
    photo = base("post1-spotlight-base.png")
    img.alpha_composite(photo, (0, 0))
    gradient(img, 820, 1080, NAVY, 0, 255)
    p1_header(img)
    d = ImageDraw.Draw(img)
    y = par(d, (56, 940), P1_HEAD, poppins(62, "Bold"), WHITE, 960, 1.08)
    y = par(d, (56, y + 18), P1_SUB, inter(23, 400), LIGHT, 900, 1.3)
    y = par(d, (56, y + 6), P1_LANG, inter(20, 500), TEAL_L, 900, 1.3)
    par(d, (56, y + 14), P1_MICRO, inter(17, 600), GREEN, 900)
    watermark(img, dark=True)
    return img


def p1_story(photo=True):  # 1080x1920; photo=False -> transparent overlay layer (for the video build)
    if photo:
        img = Image.new("RGBA", (1080, 1920), (*NAVY, 255))
        img.alpha_composite(base("post1-spotlight-base.png"), (0, 300))
    else:
        img = Image.new("RGBA", (1080, 1920), (0, 0, 0, 0))
        dd = ImageDraw.Draw(img)
        dd.rectangle((0, 0, 1080, 300), fill=(*NAVY, 255)); dd.rectangle((0, 1380, 1080, 1920), fill=(*NAVY, 255))
    gradient(img, 300, 420, NAVY, 255, 0)      # blend top edge
    gradient(img, 1100, 1380, NAVY, 0, 255)    # blend bottom edge
    d = ImageDraw.Draw(img)
    place_logo(img, "card", 150, (40, 60))
    pill(d, (1040, 92), "Manasyn Feature", inter(19, 600), TEAL, star=True)
    d.text((540, 250), "MANASYN SPOTLIGHT", font=inter(20, 600), fill=TEAL_L, anchor="mm")
    y = par(d, (60, 1300), P1_HEAD, poppins(74, "Bold"), WHITE, 960, 1.08)
    y = par(d, (60, y + 22), P1_SUB, inter(28, 400), LIGHT, 940, 1.3)
    y = par(d, (60, y + 8), P1_LANG, inter(24, 500), TEAL_L, 940, 1.3)
    y = par(d, (60, y + 24), P1_MICRO, inter(21, 600), GREEN, 940)
    d.rounded_rectangle((60, 1720, 1020, 1800), radius=40, fill=TEAL)
    d.text((540, 1760), "Tap the link  \u2192  manasyn.app", font=inter(26, 700), fill=WHITE, anchor="mm")
    watermark(img, dark=True, size=18)
    return img


def p1_pin():  # 1000x1500 Pinterest
    img = Image.new("RGBA", (1000, 1500), (*NAVY, 255))
    photo = fit_square(base("post1-spotlight-base.png"), 1000)
    img.alpha_composite(photo, (0, 230))
    gradient(img, 230, 330, NAVY, 255, 0)
    gradient(img, 1000, 1230, NAVY, 0, 255)
    d = ImageDraw.Draw(img)
    place_logo(img, "card", 130, (40, 40))
    d.text((190, 80), "Manasyn · AI Companion", font=poppins(28, "SemiBold"), fill=WHITE, anchor="lm")
    d.text((190, 122), "Mental health check-in in your language", font=inter(20, 400), fill=TEAL_L, anchor="lm")
    y = par(d, (56, 1150), P1_HEAD, poppins(60, "Bold"), WHITE, 900, 1.08)
    y = par(d, (56, y + 16), P1_SUB, inter(23, 400), LIGHT, 880, 1.3)
    y = par(d, (56, y + 6), P1_LANG, inter(20, 500), TEAL_L, 880, 1.3)
    par(d, (56, y + 14), P1_MICRO, inter(17, 600), GREEN, 880)
    watermark(img, dark=True)
    return img


# =====================================================================================
# POST 2 — Wellbeing Wisdom (infographic, parametric layout)
# =====================================================================================
TIPS = [
    ("10 min subah ki roshni", "Balcony, chhat ya walk — body clock set ho jaati hai."),
    ("Uthne ka time fix", "Sunday bhi. Sone ka nahi — uthne ka."),
    ("Chai / coffee cutoff 3–4 PM", "Caffeine 6 ghante baad bhi neend todti hai. (Drake et al., 2013)"),
    ("20-minute rule", "Neend nahi aayi? Utho, dim light, wapas jab aankhein bhaari hon."),
    ("Brain-dump list", "Kal ka to-do likh do — dimaag ko chhutti. (Scullin et al., 2018)"),
]


def p2_layout(W, H, head_size, tip_title, tip_body, sub_size, badge="Wellbeing Tip", kicker=None, footer=True, show=5):
    src = base("post2-wellbeing-base.png")
    bg = src.getpixel((20, 20))[:3]
    img = Image.new("RGBA", (W, H), (*bg, 255))
    d = ImageDraw.Draw(img)
    m = int(W * 0.052)  # margin
    # header
    place_logo(img, "emblem", int(W * 0.074), (m - 8, m - 8))
    pill(d, (W - m, m + 6), badge, inter(int(W * 0.0157), 600), GREEN)
    y = m + int(W * 0.09)
    if kicker:
        d.text((m, y), kicker, font=inter(int(W * 0.018), 600), fill=TEAL, anchor="la"); y += int(W * 0.032)
    hp = poppins(head_size, "Bold")
    y = rich(d, (m, y), [("Ek raat kam soye =\ndimaag ", hp, TEXT), ("60%", hp, PURPLE), (" zyada reactive.", hp, TEXT)], W - 2 * m, 1.12)
    y = par(d, (m, y + 8), "Neend rest nahi hai — yeh overnight emotional processing hai. (Yoo et al., 2007)",
            inter(sub_size, 400), TEXT2, W - 2 * m, 1.3)
    # tips block height
    ft, fb = poppins(tip_title, "SemiBold"), inter(tip_body, 400)
    row_h = line_height(ft, 1.15) + line_height(fb, 1.25) + int(W * 0.018)
    footer_h = int(W * 0.075) if footer else int(W * 0.03)
    tips_h = row_h * 5 + int(W * 0.03)
    # illustration fills what's left
    avail = H - footer_h - tips_h - (y + int(W * 0.02)) - int(W * 0.045)
    size = max(240, min(avail, int(W * 0.72)))
    ill = src.resize((size, size), Image.LANCZOS)
    img.alpha_composite(ill, ((W - size) // 2, y + int(W * 0.02)))
    # tips
    ty = y + int(W * 0.02) + size + int(W * 0.015)
    r = int(W * 0.019)
    fn = poppins(int(r * 1.25), "SemiBold")
    for i, (t, b) in enumerate(TIPS, 1):
        if i > show:
            break
        circle_num(d, m + r, ty + r + 4, r, i, fn)
        tx = m + r * 2 + int(W * 0.018)
        yy = par(d, (tx, ty), t, ft, TEAL, W - tx - m, 1.15)
        par(d, (tx, yy), b, fb, TEXT, W - tx - m, 1.25)
        ty += row_h
    # footer strip
    if not footer:
        return img
    fy = H - footer_h
    panel(img, (0, fy, W, H), (13, 148, 136, 30), 0)
    d = ImageDraw.Draw(img)
    # bookmark glyph
    bx, by, bw, bh = m, fy + footer_h // 2 - int(W * 0.013), int(W * 0.016), int(W * 0.024)
    d.polygon([(bx, by), (bx + bw, by), (bx + bw, by + bh), (bx + bw // 2, by + bh - bw // 2), (bx, by + bh)], fill=TEAL)
    d.text((bx + bw + 12, fy + footer_h // 2), "Save this for tonight", font=inter(int(W * 0.0165), 600), fill=TEXT, anchor="lm")
    d.text((bx + bw + 12 + inter(int(W * 0.0165), 600).getlength("Save this for tonight") + 18, fy + footer_h // 2),
           "·  Sleep anchors & wind-down reminders: Manasyn Daily Routine — free in beta",
           font=inter(int(W * 0.0148), 400), fill=TEXT2, anchor="lm")
    watermark(img, dark=False, size=int(W * 0.0148))
    return img


def p2_square():
    return p2_layout(1080, 1080, 42, 20, 16, 18)


def p2_portrait():
    return p2_layout(1080, 1350, 46, 23, 18, 20)


def p2_pin():
    return p2_layout(1000, 1500, 46, 23, 18, 20, kicker="5 SCIENCE-BACKED SLEEP HABITS FOR BETTER MENTAL HEALTH")


def p2_story(show=5):
    img = Image.new("RGBA", (1080, 1920), (*MINT, 255))
    inner = p2_layout(1080, 1500, 50, 25, 19, 21, footer=False, show=show)
    img.alpha_composite(inner, (0, 210))
    d = ImageDraw.Draw(img)
    bg = base("post2-wellbeing-base.png").getpixel((20, 20))[:3]
    d.rectangle((0, 0, 1080, 210), fill=bg); d.rectangle((0, 1710, 1080, 1920), fill=bg)
    d.text((540, 120), "WELLBEING WISDOM \u00b7 SLEEP", font=inter(22, 600), fill=TEAL, anchor="mm")
    d.text((540, 1735), "Sleep anchors & wind-down reminders are built into Manasyn Daily Routine \u2014 free in beta", font=inter(18, 400), fill=TEXT2, anchor="mm")
    d.rounded_rectangle((60, 1770, 1020, 1850), radius=40, fill=TEAL)
    d.text((540, 1810), "Save \u00b7 Share with a friend  \u2192  manasyn.app", font=inter(26, 700), fill=WHITE, anchor="mm")
    return img


# =====================================================================================
# POST 3 — Psych Notes carousel (8 slides)
# =====================================================================================
N = 8


def slide_frame(i, name, badge=True):
    img = base(name)
    progress(img, i, N)
    if badge:
        d = ImageDraw.Draw(img)
        pill(d, (1048, 40), "Psych Notes", inter(17, 600), PURPLE)
    return img


def heading(d, xy, text, size=44, width=960, color=WHITE):
    return par(d, xy, text, poppins(size, "Bold"), color, width, 1.1)


def body(d, xy, text, width, size=22, color=LIGHT, mult=1.38):
    return par(d, xy, text, inter(size, 400), color, width, mult)


def keyterm(d, xy, label, terms):
    x, y = xy
    b = chip(d, (x, y), label, inter(13, 700), NAVY, bg=YELLOW, pad=(10, 5))
    d.text((b[2] + 12, (b[1] + b[3]) / 2), terms, font=inter(17, 600), fill=YELLOW, anchor="lm")
    return b[3]


def finish(img, i, dark=True):
    page_dots(img, i, N)
    watermark(img, dark=dark)
    return img


def s1():
    img = slide_frame(1, "post3-psychnotes-slide-01.png", badge=True)
    panel(img, (30, 200, 690, 560), (15, 23, 42, 150), 24)
    place_logo(img, "card", 150, (32, 32))
    d = ImageDraw.Draw(img)
    d.text((60, 232), "PSYCH NOTES  ·  WEEK 1", font=inter(18, 700), fill=TEAL_L, anchor="la")
    y = heading(d, (60, 262), "FREUD'S\nPSYCHOANALYSIS", 62, 620)
    y = par(d, (60, y + 8), "Id · Ego · Superego + 8 Defense Mechanisms", poppins(24, "SemiBold"), YELLOW, 620, 1.2)
    y = par(d, (60, y + 6), "Everything you need to know in 60 seconds", inter(20, 400), LIGHT, 620, 1.3)
    par(d, (60, y + 8), "\u201cThis confused me too\u2026 until I made this.\u201d", inter(18, 400, italic=True), MUTED, 620, 1.3)
    d.text((1040, 1000), "Swipe  \u2192", font=inter(24, 700), fill=TEAL_L, anchor="rm")
    return finish(img, 1)


def s2():
    img = slide_frame(2, "post3-psychnotes-slide-02.png")
    place_logo(img, "emblem", 80, (32, 32))
    d = ImageDraw.Draw(img)
    y = heading(d, (60, 130), "The Mind Is\nan Iceberg", 44, 440)
    y = body(d, (60, y + 16), "Conscious = what you notice right now (the tip). Preconscious = memories you can pull up when needed (just below the waterline). Unconscious = wishes, fears and memories pushed out of awareness \u2014 the biggest part, still steering your behaviour.", 420, 21)
    keyterm(d, (60, y + 14), "KEY TERM", "Unconscious")
    # zone labels on the right of the iceberg, aligned to zones
    for (label, col, yy, x0) in [("CONSCIOUS", TEAL_L, 185, 870), ("PRECONSCIOUS", GREEN, 272, 870), ("UNCONSCIOUS", PURPLE_L, 600, 870)]:
        d.line([(x0 - 40, yy), (x0 - 8, yy)], fill=col, width=2)
        d.ellipse((x0 - 46, yy - 4, x0 - 38, yy + 4), fill=col)
        d.text((x0, yy), label, font=poppins(19, "SemiBold"), fill=col, anchor="lm")
    d.text((870, 205), "what you notice now", font=inter(14, 400), fill=MUTED, anchor="la")
    d.text((870, 292), "can be recalled", font=inter(14, 400), fill=MUTED, anchor="la")
    d.text((870, 620), "pushed out of\nawareness", font=inter(14, 400), fill=MUTED, anchor="la")
    par(d, (60, 968), "Fun fact: Freud never used the iceberg image himself \u2014 it came later via G. Stanley Hall (Green, 2019). The three levels are Freud's: the topographic model.", inter(14, 400), MUTED, 960, 1.3)
    return finish(img, 2)


def s3():
    img = slide_frame(3, "post3-psychnotes-slide-03.png")
    place_logo(img, "emblem", 80, (32, 32))
    d = ImageDraw.Draw(img)
    y = heading(d, (60, 128), "Id, Ego, Superego: The Trio", 42, 960)
    y = body(d, (60, y + 12), "Id: \u201cI want it NOW\u201d \u2014 pleasure principle, present from birth. Superego: \u201cYou SHOULD\u201d \u2014 morality principle, learned from parents and society. Ego: the referee \u2014 reality principle, finds a realistic way to satisfy the Id without angering the Superego.", 960, 21)
    orbs = [(205, "ID", PURPLE_L, "Pleasure principle", "\u201cI want it NOW.\u201d"),
            (545, "EGO", TEAL_L, "Reality principle", "\u201cLet's find a way.\u201d"),
            (900, "SUPEREGO", YELLOW, "Morality principle", "\u201cYou SHOULD.\u201d")]
    for cx, name, col, principle, quote in orbs:
        d.text((cx, 660), name, font=poppins(30, "Bold"), fill=col, anchor="mm")
        d.text((cx, 700), principle, font=inter(17, 600), fill=col, anchor="mm")
        d.text((cx, 730), quote, font=inter(16, 400, italic=True), fill=LIGHT, anchor="mm")
    d.text((375, 470), "wants", font=inter(14, 500), fill=MUTED, anchor="mm")
    d.text((720, 470), "demands", font=inter(14, 500), fill=MUTED, anchor="mm")
    keyterm(d, (60, 830), "KEY TERMS", "pleasure principle · reality principle · morality principle")
    par(d, (60, 900), "Born with the Id; the Ego develops as a child meets reality; the Superego forms as rules are internalised (roughly ages 3\u20136).", inter(15, 400), MUTED, 960, 1.3)
    return finish(img, 3)


def s4():
    img = slide_frame(4, "post3-psychnotes-slide-04.png")
    place_logo(img, "emblem", 80, (32, 32))
    d = ImageDraw.Draw(img)
    heading(d, (60, 124), "Exam Night: The Trio Fights", 40, 700)
    # speech-bubble text (bubbles measured on the base image)
    def bubble(box, tag, col, quote, size):
        x0, y0, x1, y1 = box
        f_tag, f_q = poppins(size + 1, "Bold"), inter(size, 500)
        lines = wrap(quote, f_q, x1 - x0)
        total = line_height(f_tag, 1.1) + len(lines) * line_height(f_q, 1.15)
        yy = (y0 + y1) // 2 - total // 2
        d.text(((x0 + x1) // 2, yy), tag, font=f_tag, fill=col, anchor="ma"); yy += line_height(f_tag, 1.1)
        for ln in lines:
            d.text(((x0 + x1) // 2, yy), ln, font=f_q, fill=WHITE, anchor="ma"); yy += line_height(f_q, 1.15)
    bubble((236, 212, 474, 358), "ID", PURPLE_L, "\u201cEk episode aur\u2026 phone uthao.\u201d", 21)
    bubble((458, 360, 630, 472), "EGO", TEAL_L, "\u201cDeal: 20 min break, 2 ghante revision, 11:30 so.\u201d", 15)
    bubble((636, 266, 776, 354), "SUPEREGO", YELLOW, "\u201cPadhoge nahi toh Papa ka bharosa tootega.\u201d", 13)
    # caption plate
    panel(img, (40, 850, 1040, 985), (15, 23, 42, 215), 18)
    y = par(d, (64, 866), "Exam kal hai. Teeno bolte hain \u2014 aur a strong Ego negotiates. When it can't, the clash creates anxiety.", inter(21, 400), LIGHT, 950, 1.3)
    keyterm(d, (64, y + 8), "KEY TERM", "anxiety  \u2192  triggers the Ego's defenses (next slide)")
    return finish(img, 4)


def legend(d, x, y, groups, width=360):
    """groups = [(bucket, color, [(name, example), ...]), ...]"""
    for bucket, col, items in groups:
        chip(d, (x, y), bucket, inter(13, 700), NAVY, bg=col, pad=(10, 4)); y += 40
        for name, ex in items:
            d.text((x, y), name, font=poppins(20, "SemiBold"), fill=WHITE, anchor="la"); y += 28
            y = par(d, (x, y), ex, inter(15, 400, italic=True), MUTED, width, 1.25) + 10
        y += 8
    return y


def quad_labels(d, labels):
    """labels = [(cx, cy, text, color)] drawn on a dark plate over the shield quadrants."""
    for cx, cy, text, col in labels:
        f = poppins(15, "Bold")
        w = f.getlength(text) + 20
        d.rounded_rectangle((cx - w / 2, cy - 14, cx + w / 2, cy + 14), radius=8, fill=(15, 23, 42, 200))
        d.text((cx, cy), text, font=f, fill=col, anchor="mm")


def s5():
    img = slide_frame(5, "post3-psychnotes-slide-05.png")
    place_logo(img, "emblem", 80, (32, 32))
    d = ImageDraw.Draw(img)
    y = heading(d, (60, 128), "Defense Mechanisms:\nThe Ego's Shields", 38, 400)
    y = body(d, (60, y + 12), "When Id\u2013Superego conflict creates anxiety, the Ego protects itself automatically and unconsciously \u2014 with defense mechanisms (mapped in detail by Anna Freud, 1936). Everyone uses them. Trouble starts only when one becomes your default.", 370, 18, mult=1.35)
    y = legend(d, 60, y + 18, [
        ("PUSH IT DOWN", BLUE, [("Repression", "Painful memory pushed out of awareness. \u201cBachpan ki woh baat\u2026 yaad hi nahi.\u201d"),
                                ("Denial", "Refusing to see what's real. \u201cMujhe koi stress nahi hai\u201d (result kal, nails chewed).")]),
        ("PUSH IT OUT", PURPLE_L, [("Projection", "Your feeling, pinned on someone else. \u201cMain nahi \u2014 WOH jealous hai.\u201d"),
                                   ("Displacement", "Feeling redirected to a safer target. Boss ne daanta \u2192 chhote bhai pe gussa.")]),
    ], width=350)
    quad_labels(d, [(622, 478, "REPRESSION", BLUE), (836, 478, "DENIAL", BLUE),
                    (622, 745, "PROJECTION", PURPLE_L), (836, 745, "DISPLACEMENT", PURPLE_L)])
    return finish(img, 5)


def s6():
    img = slide_frame(6, "post3-psychnotes-slide-06.png")
    place_logo(img, "emblem", 80, (32, 32))
    d = ImageDraw.Draw(img)
    y = heading(d, (60, 128), "Four More Shields", 40, 400)
    y = legend(d, 60, y + 18, [
        ("DRESS IT UP", YELLOW, [("Rationalisation", "A logical-sounding excuse for the real reason. \u201cWoh company waise bhi achhi nahi thi.\u201d"),
                                 ("Reaction formation", "Acting the opposite of what you feel. Secretly like someone \u2192 extra rude to them.")]),
        ("GO BACK / GO UP", GREEN, [("Regression", "Sliding back to a younger self under stress. Breakup \u2192 Mummy ke haath ka khaana aur sulking."),
                                    ("Sublimation", "Channelling the urge into something useful. Gussa \u2192 gym, cricket, poetry. The healthiest one.")]),
    ], width=350)
    par(d, (60, y + 14), "Freud today: many of his specifics can't be tested (Popper, 1963), but defense mechanisms are still researched and ranked from immature to mature (Vaillant, 2000; Cramer, 2015).", inter(14, 400), MUTED, 350, 1.3)
    quad_labels(d, [(622, 470, "RATIONALISATION", YELLOW), (836, 470, "REACTION FORMATION", YELLOW),
                    (622, 735, "REGRESSION", GREEN), (836, 735, "SUBLIMATION", GREEN)])
    return finish(img, 6)


def s7():
    img = slide_frame(7, "post3-psychnotes-slide-07.png")
    place_logo(img, "emblem", 80, (32, 32))
    d = ImageDraw.Draw(img)
    heading(d, (60, 126), "Remember it this way:", 40, 960)
    # block 1: IES
    panel(img, (60, 190, 1020, 345), (13, 148, 136, 40), 18)
    d.rounded_rectangle((60, 190, 1020, 345), radius=18, outline=TEAL, width=2)
    d.text((84, 214), "I \u00b7 E \u00b7 S  \u2014  like the IES exam", font=poppins(24, "Bold"), fill=TEAL_L, anchor="la")
    f = inter(20, 500)
    d.text((84, 262), "Id = Instinct (wants)", font=f, fill=PURPLE_L, anchor="la")
    d.text((400, 262), "Ego = Executive (decides)", font=f, fill=TEAL_L, anchor="la")
    d.text((730, 262), "Superego = Standards (judges)", font=f, fill=YELLOW, anchor="la")
    d.text((84, 296), "Instinct wants \u2192 Executive decides \u2192 Standards judge.   Ego ke 4 moves: dabao \u00b7 phenko \u00b7 sajao \u00b7 peeche/upar jao.", font=inter(16, 400, italic=True), fill=LIGHT, anchor="la")
    # boxes: (x0,y0,x1,y1) measured
    boxes = [((90, 380, 500, 610), "DOWN", BLUE, "Repression \u00b7 Denial", "push it down"),
             ((570, 380, 985, 610), "OUT", PURPLE_L, "Projection \u00b7 Displacement", "push it out"),
             ((90, 690, 500, 920), "DRESS", YELLOW, "Rationalisation \u00b7 Reaction formation", "dress it up"),
             ((570, 690, 985, 920), "BACK / UP", GREEN, "Regression \u00b7 Sublimation", "go back, or go up")]
    for (x0, y0, x1, y1), title, col, mech, hint in boxes:
        d.rounded_rectangle((x0 + 14, y0 + 12, x0 + 14 + poppins(24, "Bold").getlength(title) + 24, y0 + 50), radius=8, fill=(15, 23, 42, 210))
        d.text((x0 + 26, y0 + 31), title, font=poppins(24, "Bold"), fill=col, anchor="lm")
        fm = inter(17, 600)
        w = fm.getlength(mech) + 24
        fh = inter(14, 400, italic=True)
        d.rounded_rectangle((x0 + 14, y1 - 66, x0 + 14 + w, y1 - 40), radius=8, fill=(15, 23, 42, 210))
        d.text((x0 + 26, y1 - 53), mech, font=fm, fill=WHITE, anchor="lm")
        hw = fh.getlength(hint) + 20
        d.rounded_rectangle((x0 + 14, y1 - 34, x0 + 14 + hw, y1 - 10), radius=8, fill=(15, 23, 42, 210))
        d.text((x0 + 24, y1 - 22), hint, font=fh, fill=col, anchor="lm")
    return finish(img, 7)


def s8():
    img = slide_frame(8, "post3-psychnotes-slide-08.png")
    img.alpha_composite(logo("card", 250), (415, 120))
    d = ImageDraw.Draw(img)
    d.text((540, 425), "Save this for your exam!", font=poppins(42, "Bold"), fill=WHITE, anchor="mm")
    d.text((540, 480), "Share this with your study group  \u00b7  Follow @manasynapp for more Psych Notes", font=inter(19, 500), fill=LIGHT, anchor="mm")
    par(d, (90, 522), "Full crash courses \u2014 Psychology 1st Sem, Biopsychology, Forensic \u2014 with free PDF notes \u2192 manasyn.app/courses", inter(18, 600), TEAL_L, 900, 1.3, align="center")
    panel(img, (70, 596, 1010, 722), (15, 23, 42, 170), 16)
    d = ImageDraw.Draw(img)
    par(d, (90, 610), "Sources: Freud, S. (1923/1961). The ego and the id. SE 19  \u00b7  Freud, A. (1936/1937). The ego and the mechanisms of defence  \u00b7  NCERT (2007). Psychology, Class XII, Ch. 2  \u00b7  Vaillant, G. E. (2000). Am Psychol, 55(1)  \u00b7  Cramer, P. (2015). Psychodyn Psychiatry, 43(4)  \u00b7  Green, C. D. (2019). Hist Psychol, 22(4)", inter(14, 400), MUTED, 900, 1.35, align="center")
    d.text((60, 1046), "Educational content for psychology students \u2014 not clinical advice.", font=inter(13, 400), fill=MUTED, anchor="ld")
    return finish(img, 8)


def p3_pin():
    img = Image.new("RGBA", (1000, 1500), (*NAVY, 255))
    cover = s1().resize((1000, 1000), Image.LANCZOS)
    img.alpha_composite(cover, (0, 0))
    gradient(img, 900, 1000, NAVY, 0, 255)
    d = ImageDraw.Draw(img)
    d.text((60, 1040), "Inside this carousel:", font=poppins(28, "Bold"), fill=WHITE, anchor="la")
    items = ["The iceberg model \u2014 conscious, preconscious, unconscious",
             "Id \u00b7 Ego \u00b7 Superego with an exam-night example",
             "All 8 defense mechanisms with everyday examples",
             "The I\u00b7E\u00b7S + DOWN\u00b7OUT\u00b7DRESS\u00b7BACK/UP mnemonic"]
    y = 1095
    for it in items:
        d.ellipse((60, y + 9, 72, y + 21), fill=TEAL)
        d.text((88, y), it, font=inter(21, 400), fill=LIGHT, anchor="la"); y += 40
    d.rounded_rectangle((60, 1300, 940, 1370), radius=35, fill=PURPLE)
    d.text((500, 1335), "Free crash courses + PDF notes  \u2192  manasyn.app/courses", font=inter(22, 700), fill=WHITE, anchor="mm")
    d.text((500, 1430), "Manasyn Psych Notes  \u00b7  @manasynapp", font=inter(18, 500), fill=MUTED, anchor="mm")
    watermark(img, dark=True)
    return img


# =====================================================================================
def run(which="all"):
    jobs = {
        "post1": [("post1/post1-square-1080x1080.jpg", p1_square), ("post1/post1-portrait-1080x1350.jpg", p1_portrait),
                  ("post1/post1-story-1080x1920.jpg", p1_story), ("post1/post1-pinterest-1000x1500.jpg", p1_pin)],
        "post2": [("post2/post2-square-1080x1080.jpg", p2_square), ("post2/post2-portrait-1080x1350.jpg", p2_portrait),
                  ("post2/post2-story-1080x1920.jpg", p2_story), ("post2/post2-pinterest-1000x1500.jpg", p2_pin)],
        "post3": [(f"post3/post3-slide-{i:02d}.jpg", fn) for i, fn in enumerate([s1, s2, s3, s4, s5, s6, s7, s8], 1)]
                 + [("post3/post3-pinterest-1000x1500.jpg", p3_pin)],
    }
    keys = jobs.keys() if which == "all" else [which]
    for k in keys:
        for rel, fn in jobs[k]:
            p = save(fn(), os.path.join(OUT, rel))
            print("wrote", os.path.relpath(p, ROOT))
    if which in ("all", "post3"):
        pages = [Image.open(os.path.join(OUT, f"post3/post3-slide-{i:02d}.jpg")).convert("RGB") for i in range(1, 9)]
        pdf = os.path.join(OUT, "post3/post3-carousel-linkedin.pdf")
        pages[0].save(pdf, save_all=True, append_images=pages[1:], resolution=150)
        print("wrote", os.path.relpath(pdf, ROOT))


if __name__ == "__main__":
    run(sys.argv[1] if len(sys.argv) > 1 else "all")
