#!/usr/bin/env python3
"""QA generated LinkedIn assets: dimensions, brand palette, logo presence."""
import sys, os
from PIL import Image

BRAND = {"forest #3E4A3E":(0x3E,0x4A,0x3E), "violet #655396":(0x65,0x53,0x96),
         "coral #D68C78":(0xD6,0x8C,0x78), "cream #F5F2ED":(0xF5,0xF2,0xED),
         "sage #52615A":(0x52,0x61,0x5A)}
# logo-only signature colours from the verified reference file
LOGO_SIG = {"navy #204060":(0x20,0x40,0x60), "purple #8080C0":(0x80,0x80,0xC0),
            "teal #60A0C0":(0x60,0xA0,0xC0), "lavender #A0C0E0":(0xA0,0xC0,0xE0)}

def dist(a,b): return sum((x-y)**2 for x,y in zip(a,b))**0.5
def near(px, ref, tol): return dist(px, ref) <= tol

def load_rgb(p):
    im = Image.open(p)
    if im.mode != "RGB": im = im.convert("RGB")
    return im

def zone_stats(im, box, tol=42, step=2):
    crop = im.crop(box); w,h = crop.size; px = crop.load()
    hits = {k:0 for k in LOGO_SIG}; tot = 0; white = 0
    for y in range(0,h,step):
        for x in range(0,w,step):
            c = px[x,y]; tot += 1
            if min(c) > 240: white += 1
            for k,ref in LOGO_SIG.items():
                if near(c,ref,tol): hits[k]+=1
    return hits, tot, white

def palette_check(im, step=4):
    w,h = im.size; px = im.load()
    counts = {k:0 for k in BRAND}; tot=0; off=0
    for y in range(0,h,step):
        for x in range(0,w,step):
            c = px[x,y]; tot += 1
            best = min(BRAND.values(), key=lambda r: dist(c,r))
            if dist(c,best) <= 46:
                for k,v in BRAND.items():
                    if v == best: counts[k]+=1
            else: off += 1
    return counts, tot, off

def main(paths):
    print(f"{'file':<34}{'dimensions':>14}{'onpalette':>11}{'logo-sig px':>13}  verdict")
    print("-"*88)
    for p in paths:
        im = load_rgb(p); w,h = im.size
        exp = (1080,1350) if "postA" in p else (1080,1080)
        dimok = (w,h) == exp
        # logo zone = bottom-right corner, generous search window
        zw = int(w*0.20); zh = int(h*0.16)
        box = (w-zw, h-zh, w, h)
        hits, tot, white = zone_stats(im, box)
        sig = sum(hits.values())
        counts, ptot, off = palette_check(im)
        onpal = 100*(ptot-off)/ptot
        verdict = []
        if not dimok: verdict.append(f"DIM {w}x{h}!= {exp[0]}x{exp[1]}")
        if onpal < 72: verdict.append(f"PALETTE {onpal:.0f}%")
        if sig < 12: verdict.append("LOGO-MISSING/WEAK")
        print(f"{os.path.basename(p):<34}{f'{w}x{h}':>14}{onpal:>10.0f}%{sig:>13}  {'OK' if not verdict else ' | '.join(verdict)}")
        if sig >= 12:
            det = ", ".join(f"{k.split()[0]}={v}" for k,v in hits.items() if v)
            print(f"{'':<34}   logo signature found: {det}   (white bg in zone {100*white/tot:.0f}%)")
    print()

if __name__ == "__main__":
    args = sys.argv[1:] or sorted(
        (os.path.join(r,f) for r,_,fs in os.walk("linkedin-week") for f in fs if f.endswith(".png") and "assets" not in r))
    main(args)
