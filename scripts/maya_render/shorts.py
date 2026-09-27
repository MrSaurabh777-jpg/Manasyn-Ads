"""Build YouTube Shorts (1080x1920 mp4) for Day 1 from the final images. Uses imageio-ffmpeg's bundled ffmpeg."""
from __future__ import annotations
import os, subprocess, sys, tempfile
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(__file__))
from lib import *  # noqa
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
DAY = os.path.join(ROOT, "maya-content", "week-01", "day-01")
FINAL = os.path.join(DAY, "final")
OUT = os.path.join(FINAL, "youtube")
os.makedirs(OUT, exist_ok=True)


def frame_for_slide(i: int) -> Image.Image:
    img = Image.new("RGBA", (1080, 1920), (*NAVY, 255))
    d = ImageDraw.Draw(img)
    d.text((540, 250), "PSYCH NOTES  \u00b7  FREUD IN 60 SECONDS", font=inter(24, 700), fill=TEAL_L, anchor="mm")
    d.text((540, 300), "Id \u00b7 Ego \u00b7 Superego + 8 Defense Mechanisms", font=poppins(28, "SemiBold"), fill=WHITE, anchor="mm")
    slide = Image.open(os.path.join(FINAL, f"post3/post3-slide-{i:02d}.jpg")).convert("RGBA").resize((1000, 1000), Image.LANCZOS)
    img.alpha_composite(slide, (40, 380))
    # progress
    d.rectangle((40, 1420, 1040, 1428), fill=SLATE)
    d.rectangle((40, 1420, 40 + int(1000 * i / 8), 1428), fill=TEAL)
    d.text((540, 1500), f"{i} / 8", font=inter(22, 600), fill=MUTED, anchor="mm")
    d.text((540, 1600), "Save it for your exam  \u00b7  Share with your study group", font=inter(26, 500), fill=LIGHT, anchor="mm")
    d.rounded_rectangle((140, 1660, 940, 1740), radius=40, fill=PURPLE)
    d.text((540, 1700), "Free courses + PDF notes  \u2192  manasyn.app/courses", font=inter(26, 700), fill=WHITE, anchor="mm")
    d.text((540, 1800), "@Manasyn on YouTube  \u00b7  @manasynapp on Instagram", font=inter(20, 500), fill=MUTED, anchor="mm")
    return img


def build_carousel_short(per=7.0, fade=0.5):
    tmp = tempfile.mkdtemp()
    frames = []
    for i in range(1, 9):
        p = os.path.join(tmp, f"f{i}.png"); frame_for_slide(i).convert("RGB").save(p); frames.append(p)
    args = [FF, "-y"]
    for p in frames:
        args += ["-loop", "1", "-t", str(per), "-i", p]
    fc, prev = [], "[0:v]"
    for k in range(1, 8):
        off = round(k * (per - fade), 3)
        fc.append(f"{prev}[{k}:v]xfade=transition=fade:duration={fade}:offset={off}[v{k}]")
        prev = f"[v{k}]"
    out = os.path.join(OUT, "post3-freud-in-60s-short-1080x1920.mp4")
    args += ["-filter_complex", ";".join(fc), "-map", prev, "-r", "30", "-pix_fmt", "yuv420p",
             "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-movflags", "+faststart", out]
    subprocess.run(args, check=True, capture_output=True)
    return out


def build_post1_short(secs=10):
    """Post 1: slow push-in on the text-free photo, static text/logo overlay on top (nothing gets cropped)."""
    import day01
    tmp = tempfile.mkdtemp()
    ov = os.path.join(tmp, "overlay.png"); day01.p1_story(photo=False).save(ov)
    photo = os.path.join(DAY, "images", "post1-spotlight-base.png")
    frames = secs * 30
    fc = (f"[1:v]scale=2160:2160,zoompan=z='min(zoom+0.0005,1.12)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
          f":d={frames}:s=1080x1080:fps=30,pad=1080:1920:0:300:color=0x0F172A[bg];[bg][0:v]overlay=0:0,format=yuv420p")
    out = os.path.join(OUT, "post1-ai-companion-short-1080x1920.mp4")
    args = [FF, "-y", "-loop", "1", "-i", ov, "-i", photo, "-filter_complex", fc, "-t", str(secs), "-r", "30",
            "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-movflags", "+faststart", out]
    subprocess.run(args, check=True, capture_output=True)
    return out


def build_post2_short(first=2.2, step=2.4, hold=4.0, fade=0.4):
    """Post 2: the five sleep anchors appear one by one (build animation)."""
    import day01
    tmp = tempfile.mkdtemp()
    frames, durs = [], []
    for k in range(0, 6):
        p = os.path.join(tmp, f"t{k}.png"); day01.p2_story(show=k).convert("RGB").save(p)
        frames.append(p); durs.append(first if k == 0 else (hold if k == 5 else step))
    args = [FF, "-y"]
    for p, t in zip(frames, durs):
        args += ["-loop", "1", "-t", str(t), "-i", p]
    fc, prev, off = [], "[0:v]", 0.0
    for k in range(1, len(frames)):
        off += durs[k - 1] - fade
        fc.append(f"{prev}[{k}:v]xfade=transition=fade:duration={fade}:offset={round(off, 3)}[v{k}]")
        prev = f"[v{k}]"
    out = os.path.join(OUT, "post2-sleep-anchors-short-1080x1920.mp4")
    args += ["-filter_complex", ";".join(fc), "-map", prev, "-r", "30", "-pix_fmt", "yuv420p",
             "-c:v", "libx264", "-crf", "20", "-preset", "medium", "-movflags", "+faststart", out]
    subprocess.run(args, check=True, capture_output=True)
    return out


if __name__ == "__main__":
    print("wrote", os.path.relpath(build_carousel_short(), ROOT))
    print("wrote", os.path.relpath(build_post1_short(), ROOT))
    print("wrote", os.path.relpath(build_post2_short(), ROOT))
