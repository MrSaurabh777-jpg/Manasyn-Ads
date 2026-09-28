"""Reel assets for Day 1 / Post 1 (AI Companion, 30 s, 9:16):
- normalises the AI keyframes to exactly 1080x1920 JPG (what Kling / Hailuo should receive)
- renders the branded end card (shot 6) and the Reel cover with text baked in
Usage: python3 scripts/maya_render/reel.py
"""
from __future__ import annotations
import glob, os, sys
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(__file__))
from lib import *  # noqa

REEL = os.path.join(ROOT, "maya-content", "week-01", "day-01", "reel")
KF = os.path.join(REEL, "keyframes")
W, H = 1080, 1920


def cover_crop(im: Image.Image, w=W, h=H) -> Image.Image:
    s = max(w / im.width, h / im.height)
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    x, y = (im.width - w) // 2, (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))


def normalise_keyframes():
    out = []
    for p in sorted(glob.glob(os.path.join(KF, "shot-*.png"))):
        im = cover_crop(Image.open(p).convert("RGB"))
        q = p[:-4] + "-1080x1920.jpg"
        im.save(q, "JPEG", quality=95, optimize=True)
        os.remove(p)
        out.append(q)
    return out


def end_card():
    img = Image.new("RGBA", (W, H), (*NAVY, 255))
    # soft radial glow (small radial alpha mask scaled up = smooth falloff)
    n = 96
    mask = Image.new("L", (n, n), 0)
    px = mask.load()
    for yy in range(n):
        for xx in range(n):
            dist = ((xx - n / 2) ** 2 + (yy - n / 2) ** 2) ** 0.5 / (n / 2)
            px[xx, yy] = int(max(0.0, 1 - dist) ** 1.6 * 110)
    mask = mask.resize((1400, 1400), Image.BICUBIC)
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow.paste(Image.new("RGBA", mask.size, (*TEAL, 255)), (540 - 700, 860 - 700), mask)
    img.alpha_composite(glow)
    d = ImageDraw.Draw(img)
    img.alpha_composite(logo("card", 300), (390, 330))
    d.text((540, 700), "Raat ke 1 baje", font=poppins(64, "Bold"), fill=WHITE, anchor="mm")
    d.text((540, 780), "kisse baat karein?", font=poppins(64, "Bold"), fill=WHITE, anchor="mm")
    par(d, (90, 850), "Manasyn AI Companion \u2014 ek guided check-in, aapki bhasha mein.", inter(30, 400), LIGHT, 900, 1.3, align="center")
    d.text((540, 960), "English \u00b7 Hindi \u00b7 Maithili \u00b7 Bhojpuri \u00b7 Hinglish", font=inter(26, 500), fill=TEAL_L, anchor="mm")
    pill(d, (540, 1020), "Free during private beta", inter(24, 600), GREEN, anchor="mt")
    d.rounded_rectangle((140, 1120, 940, 1216), radius=48, fill=TEAL)
    d.text((540, 1168), "manasyn.app", font=poppins(40, "Bold"), fill=WHITE, anchor="mm")
    d.text((540, 1290), "Link in bio", font=inter(24, 500), fill=MUTED, anchor="mm")
    par(d, (90, 1400), "Self-help & educational companion \u2014 not therapy, not a diagnosis, not an emergency service.", inter(20, 400), MUTED, 900, 1.3, align="center")
    par(d, (90, 1470), "Emergency: 112  \u00b7  Tele-MANAS: 14416 (24\u00d77)  \u00b7  iCall: 9152987821 (Mon\u2013Sat, 10 AM\u20138 PM)", inter(20, 500), LIGHT, 900, 1.3, align="center")
    d.text((540, 1600), "@manasynapp", font=inter(24, 600), fill=TEAL_L, anchor="mm")
    watermark(img, dark=True, size=18)
    return img


def cover():
    src = sorted(glob.glob(os.path.join(KF, "shot-01-*.jpg")))[0]
    img = Image.open(src).convert("RGBA")
    gradient(img, 1000, 1560, NAVY, 0, 225)
    gradient(img, 1560, H, NAVY, 225, 250)
    d = ImageDraw.Draw(img)
    place_logo(img, "emblem", 80, (40, 232), card=True)
    pill(d, (1040, 262), "Manasyn Feature", inter(19, 600), TEAL, star=True)
    d.text((540, 1250), "Raat ke 1 baje", font=poppins(84, "Bold"), fill=WHITE, anchor="mm")
    d.text((540, 1350), "kisse baat karein?", font=poppins(84, "Bold"), fill=WHITE, anchor="mm")
    d.text((540, 1450), "30-second answer  \u2192", font=inter(30, 500), fill=TEAL_L, anchor="mm")
    d.text((540, 1570), "Manasyn AI Companion \u00b7 Free in beta", font=inter(26, 600), fill=GREEN, anchor="mm")
    watermark(img, dark=True, size=18)
    return img


if __name__ == "__main__":
    for q in normalise_keyframes():
        print("keyframe", os.path.relpath(q, ROOT))
    print("wrote", os.path.relpath(save(end_card(), os.path.join(REEL, "shot-06-end-card-1080x1920.jpg"), 95), ROOT))
    print("wrote", os.path.relpath(save(cover(), os.path.join(REEL, "reel-cover-1080x1920.jpg"), 95), ROOT))
