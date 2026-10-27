# -*- coding: utf-8 -*-
"""Week-2 renderer: lo-fi native-looking vertical video (TikTok + Instagram Reel) and notes-style carousels.

Scene kinds: hook, claim, card, fix, stat, list, cta.  Slide types: cover, row, vs, stat, note, end.
Video is silent on purpose: music/voiceover is added in the TikTok/Instagram editor (Notify Me workflow).
"""
import os
import shutil
import subprocess
import tempfile

import render  # reuse _shoot, srt_time, probe

SOCIAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS = os.path.join(SOCIAL, "templates", "lofi.css")
HANDLE = render.HANDLE
esc = render.esc


def _page(body):
    css = open(CSS, encoding="utf-8").read()
    return f"<!doctype html><html><head><meta charset='utf-8'><style>{css}</style></head><body>{body}</body></html>"


def _bubbles(text, cls=""):
    return "".join(f"<div><span class='bubble {cls}'>{esc(line)}</span></div>" for line in text.split("\n"))


# ------------------------------------------------------------------ vertical video
def v_scene(sc, i, total, elapsed):
    pct = int(100 * (elapsed + sc["secs"]) / total)
    k = sc["kind"]
    bg = "dark" if k == "cta" else f"bg{i % 4}"
    if k == "hook":
        inner = f"<div class='stack center'>{_bubbles(sc['text'], 'y')}</div>"
    elif k == "claim":
        inner = (f"<div class='claim'><div class='box said'><div class='lab'>THE POST SAID</div>{esc(sc['claim'])}</div>"
                 f"<div class='box found'><div class='lab'>WHAT WE FOUND</div>{esc(sc['found'])}</div></div>")
    elif k == "card":
        inner = (f"<div class='job'><div class='tag'>CHECKED {esc(CHECKED)}</div><div class='co'>{esc(sc['company'])}</div>"
                 f"<div class='role'>{esc(sc['role'])}</div><div class='pay'>{esc(sc['pay'])}</div>"
                 f"<div class='catch'>⚠ {esc(sc['note'])}</div></div>")
    elif k == "fix":
        inner = (f"<div class='fix'><div class='row bad'>✗ {esc(sc['bad'])}</div><div class='arrow'>↓</div>"
                 f"<div class='row good'>✓ {esc(sc['good'])}</div></div>")
    elif k == "stat":
        inner = f"<div class='stack center'><div class='big'>{esc(sc['big'])}</div><div class='statline'>{esc(sc['text'])}</div></div>"
    elif k == "list":
        inner = f"<div class='note'><div class='bar'><span>‹ Notes</span><span>Done</span></div><div class='line'>{esc(sc['text'])}</div></div>"
    elif k == "cta":
        inner = f"<div class='stack center'>{_bubbles(sc['text'])}</div>"
    else:
        raise ValueError(f"unknown scene kind {k}")
    return (f"<div class='slide v {bg}'><div class='prog'><i style='width:{pct}%'></i></div>{inner}"
            f"<div class='handle'>{HANDLE}</div></div>")


CHECKED = "Oct 27"


def render_video(topic, out_dir):
    scenes = topic["scenes"]
    total = sum(s["secs"] for s in scenes)
    frames_dir = os.path.join(out_dir, "frames")
    os.makedirs(frames_dir, exist_ok=True)
    parts, elapsed = [], 0.0
    for i, sc in enumerate(scenes):
        parts.append(v_scene(sc, i, total, elapsed))
        elapsed += sc["secs"]
    render._shoot(_page("".join(parts)), frames_dir, "scene")

    lines, t = [], 0.0
    for i, sc in enumerate(scenes, 1):
        lines += [str(i), f"{render.srt_time(t)} --> {render.srt_time(t + sc['secs'])}", sc["vo"], ""]
        t += sc["secs"]
    open(os.path.join(out_dir, "captions.srt"), "w", encoding="utf-8").write("\n".join(lines))

    with tempfile.TemporaryDirectory() as tmp:
        clips = []
        for i, sc in enumerate(scenes, 1):
            img = os.path.join(frames_dir, f"scene_{i:02d}.png")
            frames = int(round(sc["secs"] * 30))
            clip = os.path.join(tmp, f"c{i:02d}.mp4")
            # quick "pop" in, then a gentle push: feels like a native edit, not a slideshow
            vf = (f"scale=1188:2112,zoompan=z='if(lt(on,6),1.04-0.006*on,1+0.0008*on)':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)'"
                  f":d={frames}:s=1080x1920:fps=30,format=yuv420p")
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-loop", "1", "-i", img, "-vf", vf, "-frames:v", str(frames),
                            "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-r", "30", clip], check=True)
            clips.append(clip)
        lst = os.path.join(tmp, "list.txt")
        open(lst, "w").write("".join(f"file '{c}'\n" for c in clips))
        out = os.path.join(out_dir, "video.mp4")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst,
                        "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=44100",
                        "-shortest", "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-movflags", "+faststart", out], check=True)
    shutil.copy(os.path.join(frames_dir, "scene_01.png"), os.path.join(out_dir, "cover.png"))
    return out, total


# ------------------------------------------------------------------ Instagram carousel
def ig_slide(s, i, n):
    t = s["type"]
    bg = f"bg{i % 4}"
    if t == "cover":
        inner = (f"<div class='center-wrap'><div class='kick'>CHECKED {CHECKED}</div><h1>{esc(s['title'])}</h1>"
                 f"<div class='sub'>{esc(s['sub'])}</div><div class='swipe'>Swipe →</div></div>")
    elif t == "row":
        inner = (f"<div class='center-wrap'><div class='job'><div class='co'>{esc(s['title'])}</div><div class='role'>{esc(s['good'])}</div>"
                 f"<div class='pay'>{esc(s['pay'])}</div><div class='catch'>⚠ {esc(s['catch'])}</div></div></div>")
    elif t == "vs":
        inner = (f"<div class='center-wrap'><div class='kick'>{esc(s['title'].upper())}</div><div class='vs'>"
                 f"<div class='row bad'>🚩 {esc(s['bad'])}</div><div class='row good'>✅ {esc(s['good'])}</div></div></div>")
    elif t == "stat":
        inner = (f"<div class='center-wrap'><div class='big'>{esc(s['big'])}</div><h1 style='font-size:62px'>{esc(s['title'])}</h1>"
                 f"<div class='sub'>{esc(s['sub'])}</div></div>")
    elif t == "note":
        items = "".join(f"<li>{esc(x)}</li>" for x in s["items"])
        inner = (f"<div class='center-wrap'><div class='note'><div class='bar'><span>‹ Notes</span><span>Done</span></div>"
                 f"<h3>{esc(s['title'])}</h3><ul>{items}</ul></div></div>")
    elif t == "end":
        bg = "dark"
        inner = (f"<div class='center-wrap'><h1 style='color:#fff'>{esc(s['title'])}</h1>"
                 f"<div class='sub' style='color:#cfd6de'>{esc(s['sub'])}</div></div>")
    else:
        raise ValueError(f"unknown slide type {t}")
    return f"<div class='slide ig {bg}'><div class='pg'>{i}/{n}</div>{inner}<div class='handle'>{HANDLE}</div></div>"


def render_carousel(topic, out_dir):
    n = len(topic["slides"])
    render._shoot(_page("".join(ig_slide(s, i + 1, n) for i, s in enumerate(topic["slides"]))), out_dir, "slide")
    return [os.path.join(out_dir, f"slide_{i + 1:02d}.png") for i in range(n)]
