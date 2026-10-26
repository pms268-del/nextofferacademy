# -*- coding: utf-8 -*-
"""Render Instagram carousel slides (PNG) and TikTok videos (MP4 + SRT) from post dicts."""
import html
import json
import os
import shutil
import subprocess
import tempfile

SOCIAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = os.path.join(SOCIAL, "templates", "brand.css")
SHOOT = os.path.join(SOCIAL, "scripts", "shoot.js")
NODE_ENV = dict(os.environ, NODE_PATH=os.environ.get("NODE_PATH", "/opt/node22/lib/node_modules"))
BRAND = "NEXT OFFER ACADEMY US"
HANDLE = "@nextofferacademyus"


def esc(s):
    return html.escape(str(s))


def _page(slides_html):
    css = open(CSS, encoding="utf-8").read()
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{slides_html}</body></html>"


def _shoot(page_html, out_dir, prefix):
    with tempfile.TemporaryDirectory() as tmp:
        p = os.path.join(tmp, "slides.html")
        open(p, "w", encoding="utf-8").write(page_html)
        subprocess.run(["node", SHOOT, p, out_dir, prefix], check=True, env=NODE_ENV, capture_output=True)


# ------------------------------------------------------------------ Instagram
def ig_slide(s, i, n):
    dark = s["type"] in ("cover", "cta")
    cls = "slide ig" + (" dark" if dark else "")
    top = f"<div class='brand'><span>{BRAND}</span><span class='page'>{i}/{n}</span></div>"
    src = f"<span class='src'>Source: {esc(s['src'])}</span>" if s.get("src") else "<span></span>"
    foot = f"<div class='foot'>{src}<span>{HANDLE}</span></div>"
    t = s["type"]
    if t == "cover":
        inner = (f"<div class='kicker'>{esc(s['kicker'])}</div><h1>{esc(s['title'])}</h1><div class='rule'></div>"
                 f"<div class='sub muted'>{esc(s['sub'])}</div><div class='swipe'>SWIPE →</div>")
        inner = f"<div style='margin-top:auto;margin-bottom:auto'>{inner}</div>"
    elif t == "item":
        inner = (f"<div class='num'>{esc(s['n'])}</div><h2>{esc(s['title'])}</h2><div class='body'>{esc(s['body'])}</div>"
                 f"<div class='pill'>{esc(s['pill'])}</div><div class='catch'><b>The catch:</b> {esc(s['catch'])}</div>")
    elif t == "tip":
        inner = f"<div class='num'>{esc(s['n'])}</div><h2>{esc(s['title'])}</h2><div class='body'>{esc(s['body'])}</div>"
    elif t == "stat":
        inner = f"<div class='big'>{esc(s['big'])}</div><h2 style='margin-top:30px'>{esc(s['title'])}</h2><div class='body'>{esc(s['body'])}</div>"
    elif t == "before":
        inner = (f"<h2>{esc(s['title'])}</h2><div class='ba'><div class='box bad'><div class='label'>BEFORE</div>{esc(s['before'])}</div>"
                 f"<div class='box good'><div class='label'>AFTER</div>{esc(s['after'])}</div></div><div class='note'>{esc(s['note'])}</div>")
    elif t == "cta":
        inner = (f"<h1 style='font-size:92px'>{esc(s['title'])}</h1><div class='rule'></div><div class='sub muted'>{esc(s['body'])}</div>"
                 f"<div class='action'>{esc(s['action'])}</div><div class='handle'>{HANDLE}</div>")
        inner = f"<div style='margin-top:auto;margin-bottom:auto;display:flex;flex-direction:column'>{inner}</div>"
    else:
        raise ValueError(f"unknown slide type {t}")
    if t in ("item", "tip", "stat", "before"):
        inner = f"<div style='margin-top:auto;margin-bottom:auto;display:flex;flex-direction:column'>{inner}</div>"
    return f"<div class='{cls}'>{top}{inner}{foot}</div>"


def render_carousel(post, out_dir):
    n = len(post["slides"])
    page = _page("".join(ig_slide(s, i + 1, n) for i, s in enumerate(post["slides"])))
    _shoot(page, out_dir, "ig_slide")
    return [os.path.join(out_dir, f"ig_slide_{i + 1:02d}.png") for i in range(n)]


# ------------------------------------------------------------------ TikTok
def tt_scene(sc, i, n, total, elapsed):
    pct = int(100 * (elapsed + sc["secs"]) / total)
    text = esc(sc["text"])
    return (f"<div class='slide tt dark'><div class='prog'><i style='width:{pct}%'></i></div>"
            f"<div class='brand'><span>{BRAND}</span><span class='page'>{i}/{n}</span></div>"
            f"<div class='scene-text'>{text}</div><div class='cap'>{esc(sc['vo'])}</div>"
            f"<div class='foot'><span>{HANDLE}</span></div></div>")


def srt_time(t):
    ms = int(round(t * 1000))
    h, ms = divmod(ms, 3600000)
    m, ms = divmod(ms, 60000)
    s, ms = divmod(ms, 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def render_video(post, out_dir):
    scenes = post["scenes"]
    total = sum(s["secs"] for s in scenes)
    frames_dir = os.path.join(out_dir, "tiktok_frames")
    os.makedirs(frames_dir, exist_ok=True)
    parts, elapsed = [], 0.0
    for i, sc in enumerate(scenes):
        parts.append(tt_scene(sc, i + 1, len(scenes), total, elapsed))
        elapsed += sc["secs"]
    _shoot(_page("".join(parts)), frames_dir, "scene")

    # SRT captions matching the voiceover lines
    lines, t = [], 0.0
    for i, sc in enumerate(scenes, 1):
        lines += [str(i), f"{srt_time(t)} --> {srt_time(t + sc['secs'])}", sc["vo"], ""]
        t += sc["secs"]
    open(os.path.join(out_dir, "tiktok_captions.srt"), "w", encoding="utf-8").write("\n".join(lines))

    # One clip per scene with a slow push-in, then concatenate. Silent AAC track keeps uploaders happy;
    # add the voiceover/sound in TikTok or replace the track (see templates/tiktok_template.md).
    with tempfile.TemporaryDirectory() as tmp:
        clips = []
        for i, sc in enumerate(scenes, 1):
            img = os.path.join(frames_dir, f"scene_{i:02d}.png")
            frames = int(round(sc["secs"] * 30))
            clip = os.path.join(tmp, f"c{i:02d}.mp4")
            vf = (f"scale=1188:2112,zoompan=z='min(1+0.0012*on,1.06)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
                  f":d={frames}:s=1080x1920:fps=30,fade=t=in:st=0:d=0.25,format=yuv420p")
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", img, "-vf", vf, "-frames:v", str(frames),
                            "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-r", "30", clip], check=True)
            clips.append(clip)
        lst = os.path.join(tmp, "list.txt")
        open(lst, "w").write("".join(f"file '{c}'\n" for c in clips))
        out = os.path.join(out_dir, "tiktok_video.mp4")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
                        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
                        "-shortest", "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", out], check=True)
    shutil.copy(os.path.join(frames_dir, "scene_01.png"), os.path.join(out_dir, "tiktok_cover.png"))
    return out, total


def probe(path):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration:stream=width,height,codec_type",
                        "-of", "json", path], check=True, capture_output=True, text=True)
    return json.loads(r.stdout)
