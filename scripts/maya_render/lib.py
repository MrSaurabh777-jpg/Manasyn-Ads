"""Shared drawing helpers for MAYA post rendering (Pillow only, no Canva needed)."""
from __future__ import annotations
import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FONTS = os.path.join(ROOT, "brand", "fonts")
BRAND = os.path.join(ROOT, "brand")

# ---- brand tokens -------------------------------------------------------------
TEAL = (13, 148, 136)
TEAL_L = (94, 234, 212)
GREEN = (16, 185, 129)
PURPLE = (124, 58, 237)
PURPLE_L = (196, 181, 253)
NAVY = (15, 23, 42)
MINT = (240, 253, 244)
TEXT = (30, 41, 59)
TEXT2 = (51, 65, 85)
LIGHT = (226, 232, 240)
MUTED = (148, 163, 184)
YELLOW = (252, 211, 77)
BLUE = (96, 165, 250)
WHITE = (255, 255, 255)
SLATE = (51, 65, 85)


def hex2rgb(h: str):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


# ---- fonts --------------------------------------------------------------------
_cache = {}


def poppins(size: int, weight: str = "Bold") -> ImageFont.FreeTypeFont:
    key = ("p", size, weight)
    if key not in _cache:
        _cache[key] = ImageFont.truetype(os.path.join(FONTS, f"Poppins-{weight}.ttf"), size)
    return _cache[key]


def inter(size: int, weight: int = 400, italic: bool = False) -> ImageFont.FreeTypeFont:
    key = ("i", size, weight, italic)
    if key not in _cache:
        fn = "Inter-Italic-Variable.ttf" if italic else "Inter-Variable.ttf"
        f = ImageFont.truetype(os.path.join(FONTS, fn), size)
        f.set_variation_by_axes([min(32, max(14, size)), weight])
        _cache[key] = f
    return _cache[key]


# ---- text ---------------------------------------------------------------------
def wrap(text: str, font, max_width: int) -> list[str]:
    """Greedy word wrap; honours explicit newlines."""
    out = []
    for para in text.split("\n"):
        words = para.split(" ")
        line = ""
        for w in words:
            trial = (line + " " + w).strip()
            if font.getlength(trial) <= max_width or not line:
                line = trial
            else:
                out.append(line)
                line = w
        out.append(line)
    return out


def line_height(font, mult=1.3) -> int:
    asc, desc = font.getmetrics()
    return int((asc + desc) * mult)


def par(draw: ImageDraw.ImageDraw, xy, text, font, fill, max_width, mult=1.3, align="left", shadow=None):
    """Draw a wrapped paragraph. Returns bottom y."""
    x, y = xy
    lh = line_height(font, mult)
    for ln in wrap(text, font, max_width):
        if align == "left":
            ax, anchor = x, "la"
        elif align == "center":
            ax, anchor = x + max_width // 2, "ma"
        else:
            ax, anchor = x + max_width, "ra"
        if shadow:
            draw.text((ax + shadow[0], y + shadow[1]), ln, font=font, fill=shadow[2], anchor=anchor)
        draw.text((ax, y), ln, font=font, fill=fill, anchor=anchor)
        y += lh
    return y


def rich(draw, xy, runs, max_width, mult=1.3, align="left"):
    """runs = [(text, font, fill), ...] word-wrapped together; '\n' forces a break. Returns bottom y."""
    x0, y = xy
    tokens = []  # (text, font, fill) ; text "\n" = hard break
    for text, font, fill in runs:
        for pi, para in enumerate(text.split("\n")):
            if pi > 0:
                tokens.append(("\n", font, fill))
            parts = para.split(" ")
            for i, p in enumerate(parts):
                if p == "":
                    if i == 0 and tokens and tokens[-1][0] not in ("\n",) and not tokens[-1][0].endswith(" "):
                        t, f, c = tokens[-1]; tokens[-1] = (t + " ", f, c)
                    continue
                tokens.append((p + (" " if i < len(parts) - 1 else ""), font, fill))
    lines, cur, cur_w = [], [], 0.0
    for tok, font, fill in tokens:
        if tok == "\n":
            lines.append(cur); cur, cur_w = [], 0.0; continue
        w = font.getlength(tok)
        if cur and cur_w + font.getlength(tok.rstrip()) > max_width:
            lines.append(cur); cur, cur_w = [], 0.0
        cur.append((tok, font, fill)); cur_w += w
    if cur:
        lines.append(cur)
    lh = max(line_height(f, mult) for _, f, _ in runs)
    for ln in lines:
        if not ln:
            y += lh; continue
        total = sum(f.getlength(t) for t, f, _ in ln)
        if ln[-1][0].endswith(" "):
            total -= ln[-1][1].getlength(" ")
        if align == "center":
            x = x0 + (max_width - total) / 2
        elif align == "right":
            x = x0 + max_width - total
        else:
            x = x0
        for t, f, c in ln:
            draw.text((x, y), t, font=f, fill=c, anchor="la")
            x += f.getlength(t)
        y += lh
    return y


def text_size(text, font):
    b = font.getbbox(text)
    return b[2] - b[0], b[3] - b[1]


def glow_text(img: Image.Image, xy, text, font, fill, max_width, mult=1.15, align="left", blur=10, alpha=170):
    """Wrapped text with a soft dark glow behind it (for photo backgrounds). Returns bottom y."""
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    par(d, xy, text, font, (0, 0, 0, alpha), max_width, mult, align)
    layer = layer.filter(ImageFilter.GaussianBlur(blur))
    img.alpha_composite(layer)
    d2 = ImageDraw.Draw(img)
    return par(d2, xy, text, font, fill, max_width, mult, align)


# ---- shapes -------------------------------------------------------------------
def pill(draw, xy, text, font, bg, fg=WHITE, pad=(18, 10), anchor="rt", star=False):
    """Rounded pill. anchor 'rt' = xy is top-right; 'lt' = top-left; 'mt' = top-centre. Returns bbox."""
    tw, th = text_size(text, font)
    star_w = 22 if star else 0
    w, h = tw + pad[0] * 2 + star_w, th + pad[1] * 2 + 4
    x, y = xy
    if anchor == "rt":
        x0 = x - w
    elif anchor == "mt":
        x0 = x - w // 2
    else:
        x0 = x
    draw.rounded_rectangle((x0, y, x0 + w, y + h), radius=h // 2, fill=bg)
    tx = x0 + pad[0] + star_w
    if star:
        cx, cy, r = x0 + pad[0] + 7, y + h // 2, 7
        draw.polygon([(cx, cy - r), (cx + 2, cy - 2), (cx + r, cy), (cx + 2, cy + 2),
                      (cx, cy + r), (cx - 2, cy + 2), (cx - r, cy), (cx - 2, cy - 2)], fill=fg)
    draw.text((tx, y + h / 2), text, font=font, fill=fg, anchor="lm")
    return (x0, y, x0 + w, y + h)


def chip(draw, xy, text, font, fg, bg=None, pad=(12, 6), outline=None):
    tw, th = text_size(text, font)
    w, h = tw + pad[0] * 2, th + pad[1] * 2 + 2
    x, y = xy
    if bg or outline:
        draw.rounded_rectangle((x, y, x + w, y + h), radius=8, fill=bg, outline=outline, width=2)
    draw.text((x + pad[0], y + h / 2), text, font=font, fill=fg, anchor="lm")
    return (x, y, x + w, y + h)


def panel(img, box, fill=(15, 23, 42, 200), radius=20):
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).rounded_rectangle(box, radius=radius, fill=fill)
    img.alpha_composite(layer)


def gradient(img, y0, y1, color=NAVY, a0=0, a1=200):
    """Vertical gradient overlay from alpha a0 at y0 to a1 at y1 (full width)."""
    W, H = img.size
    strip = Image.new("RGBA", (1, max(1, y1 - y0)), (0, 0, 0, 0))
    px = strip.load()
    for i in range(y1 - y0):
        t = i / max(1, (y1 - y0 - 1))
        px[0, i] = (*color, int(a0 + (a1 - a0) * t))
    strip = strip.resize((W, y1 - y0))
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    layer.paste(strip, (0, y0))
    img.alpha_composite(layer)


def circle_num(draw, cx, cy, r, num, font, bg=PURPLE, fg=WHITE):
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=bg)
    draw.text((cx, cy + 1), str(num), font=font, fill=fg, anchor="mm")


# ---- brand furniture ----------------------------------------------------------
_logos = {}


def logo(kind="emblem", size=80) -> Image.Image:
    fn = {"emblem": "manasyn-logo-emblem-transparent.png",
          "card": "manasyn-logo-lockup-whitecard.png",
          "lockup": "manasyn-logo-lockup-transparent.png"}[kind]
    key = (kind, size)
    if key not in _logos:
        im = Image.open(os.path.join(BRAND, fn)).convert("RGBA")
        _logos[key] = im.resize((size, size), Image.LANCZOS)
    return _logos[key]


def place_logo(img, kind="emblem", size=80, xy=(32, 32), card=False):
    """card=True seats the emblem on a white rounded card (use on photos / very dark art)."""
    if card:
        pad = int(size * 0.1)
        layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
        ImageDraw.Draw(layer).rounded_rectangle((xy[0], xy[1], xy[0] + size + 2 * pad, xy[1] + size + 2 * pad),
                                                radius=int(size * 0.24), fill=(255, 255, 255, 235))
        img.alpha_composite(layer)
        img.alpha_composite(logo(kind, size), (xy[0] + pad, xy[1] + pad))
    else:
        img.alpha_composite(logo(kind, size), xy)


def watermark(img, dark=True, margin=24, size=16):
    d = ImageDraw.Draw(img)
    W, H = img.size
    col = (*TEAL_L, 178) if dark else (*TEAL, 153)
    layer = Image.new("RGBA", img.size, (0, 0, 0, 0))
    ImageDraw.Draw(layer).text((W - margin, H - margin), "manasyn.app", font=inter(size, 500), fill=col, anchor="rd")
    img.alpha_composite(layer)


def progress(img, i, n, color=TEAL, track=(30, 41, 59)):
    d = ImageDraw.Draw(img)
    W = img.size[0]
    d.rectangle((0, 0, W, 6), fill=track)
    d.rectangle((0, 0, int(W * i / n), 6), fill=color)


def page_dots(img, i, n, y=None):
    d = ImageDraw.Draw(img)
    W, H = img.size
    y = y or H - 40
    d.text((W // 2, y - 26), f"{i} / {n}", font=inter(15, 500), fill=MUTED, anchor="mm")
    gap, r = 18, 4
    x0 = W // 2 - (n - 1) * gap // 2
    for k in range(1, n + 1):
        cx = x0 + (k - 1) * gap
        d.ellipse((cx - r, y - r, cx + r, y + r), fill=TEAL if k == i else SLATE)


def fit_square(im: Image.Image, size: int) -> Image.Image:
    w, h = im.size
    s = min(w, h)
    im = im.crop(((w - s) // 2, (h - s) // 2, (w - s) // 2 + s, (h - s) // 2 + s))
    return im.resize((size, size), Image.LANCZOS)


def save(img: Image.Image, path: str, quality=92):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    rgb = img.convert("RGB")
    if path.lower().endswith(".png"):
        rgb.save(path, optimize=True)
    else:
        rgb.save(path, quality=quality, subsampling=0, optimize=True)
    return path
