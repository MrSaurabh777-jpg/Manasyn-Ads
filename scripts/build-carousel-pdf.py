#!/usr/bin/env python3
"""Assemble a day's carousel slides into one LinkedIn document-post PDF.

LinkedIn document posts (PDF) outperform multi-image carousels. Slides are
embedded at native 1080x1350 resolution, one page each, no added margins.

Usage:  python3 scripts/build-carousel-pdf.py day-01 [day-02 ...]
"""
import os, sys
from PIL import Image

DPI = 150  # -> 7.2 x 9.0 in portrait pages at 1080x1350

def build(day):
    folder = os.path.join("linkedin-week", day)
    slides = sorted(
        os.path.join(folder, f) for f in os.listdir(folder)
        if f.startswith(f"{day}-postA-slide") and f.endswith(".png"))
    if not slides:
        print(f"  {day}: no slides found"); return None
    imgs = []
    for s in slides:
        im = Image.open(s)
        if im.mode != "RGB": im = im.convert("RGB")
        imgs.append(im)
    out = os.path.join(folder, f"{day}-postA-carousel.pdf")
    first, rest = imgs[0], imgs[1:]
    first.save(out, "PDF", resolution=DPI, save_all=True, append_images=rest)
    print(f"  {day}: {len(imgs)} slides -> {out}  ({os.path.getsize(out)/1024:.0f} KB)")
    return out

if __name__ == "__main__":
    days = sys.argv[1:] or sorted(
        d for d in os.listdir("linkedin-week") if d.startswith("day-"))
    for d in days: build(d)
