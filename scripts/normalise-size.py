#!/usr/bin/env python3
"""Normalise generated assets to exact LinkedIn dimensions."""
import os, sys
from PIL import Image

def target_for(path):
    return (1080, 1350) if "postA" in os.path.basename(path) else (1080, 1080)

def run(paths):
    for p in paths:
        im = Image.open(p)
        if im.mode != "RGB": im = im.convert("RGB")
        w, h = im.size
        tgt = target_for(p)
        if (w, h) == tgt:
            print(f"  {os.path.basename(p):<34} already {w}x{h}"); continue
        im.resize(tgt, Image.LANCZOS).save(p, "PNG", optimize=True)
        print(f"  {os.path.basename(p):<34} {w}x{h} -> {tgt[0]}x{tgt[1]}")

if __name__ == "__main__":
    args = sys.argv[1:] or sorted(
        (os.path.join(r, f) for r, _, fs in os.walk("linkedin-week") for f in fs
         if f.endswith(".png") and "assets" not in r))
    run(args)
