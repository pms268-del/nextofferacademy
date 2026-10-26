# -*- coding: utf-8 -*-
"""Render media, write caption/script files, fact-check, and upsert the content database.

Run: python3 social/scripts/build_week.py [--date YYYY-MM-DD]
Sources: week1_content.POSTS plus every social/generated/<date>.json written by pipeline.py.
Statuses are never downgraded: a post you've already approved/scheduled keeps its
status, but if its content changed, it returns to needs_approval.
"""
import argparse
import csv
import datetime as dt
import glob
import hashlib
import json
import os
import sys
from collections import Counter
from zoneinfo import ZoneInfo

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
SOCIAL = os.path.dirname(SCRIPTS)
sys.path.insert(0, SCRIPTS)
import factcheck  # noqa: E402
import render  # noqa: E402
from week1_content import POSTS  # noqa: E402

DB = os.path.join(SOCIAL, "data", "content_db.json")
CONTENT = os.path.join(SOCIAL, "content")
ET = ZoneInfo("America/New_York")
HANDLES = {"instagram": "@nextofferacademyus", "tiktok": "@nextofferacademyus", "threads": "@nextofferacademyus"}


def rel(p):
    return os.path.relpath(p, os.path.dirname(SOCIAL))


def content_hash(p):
    keys = ("caption", "text", "slides", "scenes", "hashtags", "time_et", "date")
    return hashlib.sha256(json.dumps({k: p.get(k) for k in keys}, sort_keys=True).encode()).hexdigest()[:16]


def media_check(post, files, duration=None):
    issues = []
    if post["channel"] == "instagram":
        from PIL import Image
        if not 2 <= len(files) <= 10:
            issues.append(f"Carousel needs 2-10 images, has {len(files)}")
        for f in files:
            if Image.open(f).size != (1080, 1350):
                issues.append(f"{os.path.basename(f)} is not 1080x1350")
    elif post["channel"] == "tiktok":
        info = render.probe(files[0])
        v = [s for s in info["streams"] if s["codec_type"] == "video"][0]
        d = float(info["format"]["duration"])
        if (v["width"], v["height"]) != (1080, 1920):
            issues.append("Video is not 1080x1920")
        if not 20 <= d <= 45:
            issues.append(f"Video is {d:.1f}s (target 20-45s)")
        duration = round(d, 1)
    return {"issues": issues, "duration_s": duration}


def write_texts(post, out):
    if post["channel"] == "instagram":
        open(os.path.join(out, "caption.txt"), "w", encoding="utf-8").write(post["caption"] + "\n\n" + " ".join(post["hashtags"]) + "\n")
        alt = "\n".join(f"Slide {i + 1}: " + " | ".join(str(v) for k, v in s.items() if k != "type") for i, s in enumerate(post["slides"]))
        open(os.path.join(out, "alt_text.txt"), "w", encoding="utf-8").write(alt + "\n")
    elif post["channel"] == "tiktok":
        md = [f"# {post['topic']}", "", f"**Hook (first 2s):** {post['hook']}", "", "| # | Secs | On-screen text | Voiceover |", "|---|---|---|---|"]
        for i, sc in enumerate(post["scenes"], 1):
            md.append(f"| {i} | {sc['secs']} | {sc['text'].replace(chr(10), ' / ')} | {sc['vo']} |")
        md += ["", "**Full voiceover script:**", "", " ".join(sc["vo"] for sc in post["scenes"]), "",
               f"**Caption:** {post['caption']}", "", "**Sources:**"] + [f"- {s}" for s in post["sources"]]
        open(os.path.join(out, "script.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
        open(os.path.join(out, "caption.txt"), "w", encoding="utf-8").write(post["caption"] + "\n")
    else:
        open(os.path.join(out, "post.txt"), "w", encoding="utf-8").write(post["text"] + "\n")


def all_posts():
    posts = list(POSTS)
    for f in sorted(glob.glob(os.path.join(SOCIAL, "generated", "*.json"))):
        posts += json.load(open(f, encoding="utf-8"))["posts"]
    return posts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="only build posts for this date")
    args = ap.parse_args()
    db = {"posts": []}
    if os.path.exists(DB):
        db = json.load(open(DB, encoding="utf-8"))
    existing = {p["id"]: p for p in db["posts"]}

    for post in all_posts():
        if args.date and post["date"] != args.date:
            continue
        out = os.path.join(CONTENT, post["date"], post["channel"])
        os.makedirs(out, exist_ok=True)
        files, duration = [], None
        if post["channel"] == "instagram":
            files = render.render_carousel(post, out)
        elif post["channel"] == "tiktok":
            path, duration = render.render_video(post, out)
            files = [path]
        if post["channel"] == "threads":
            out = os.path.join(CONTENT, post["date"], "threads")
            os.makedirs(out, exist_ok=True)
            write_texts(post, out)
            # one file per Threads post
            os.replace(os.path.join(out, "post.txt"), os.path.join(out, post["id"].split("-")[-1] + ".txt"))
        else:
            write_texts(post, out)
        mc = media_check(post, files, duration) if files else {"issues": [], "duration_s": None}
        fc = factcheck.check(post, mc)

        local = dt.datetime.fromisoformat(f"{post['date']}T{post['time_et']}").replace(tzinfo=ET)
        h = content_hash(post)
        prev = existing.get(post["id"], {})
        status = prev.get("status", "needs_approval")
        if prev and prev.get("content_hash") != h and status in ("approved", "scheduled"):
            status = "needs_approval"
        record = {
            "id": post["id"], "date": post["date"], "time_et": post["time_et"],
            "scheduled_at_utc": local.astimezone(dt.timezone.utc).isoformat().replace("+00:00", "Z"),
            "channel": post["channel"], "account_handle": HANDLES[post["channel"]],
            "pillar": post["pillar"], "format": post["format"], "topic": post["topic"],
            "hook": post.get("hook"), "caption": post.get("caption"), "hashtags": post.get("hashtags", []),
            "text": post.get("text"), "media": [rel(f) for f in files],
            "media_check": mc, "generated_by": post.get("generated_by", "manual (week 1)"),
            "live_verification": post.get("live_verification", []), "opportunity_ids": post.get("opportunity_ids", []), "sources": post.get("sources", []),
            "factcheck": fc, "content_hash": h, "status": status,
            "approval": prev.get("approval", {"approved_by": None, "approved_at": None, "notes": None}),
            "buffer": prev.get("buffer", {"channel_id": None, "post_id": None, "state": None, "error": None}),
            "published_url": prev.get("published_url"),
            "metrics": prev.get("metrics", {"views": None, "likes": None, "comments": None, "shares": None, "saves": None,
                                            "follows": None, "link_clicks": None, "updated_at": None}),
        }
        existing[post["id"]] = record
        flag = "PASS" if fc["passed"] else "FAIL"
        print(f"{post['id']:<18} {post['channel']:<9} {flag}  media={len(files)} {('%.1fs' % mc['duration_s']) if mc.get('duration_s') else ''}"
              + ("".join(f"\n    ! {i}" for i in fc["issues"])))

    db["posts"] = sorted(existing.values(), key=lambda p: (p["date"], p["time_et"], p["channel"]))
    db["updated_at"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    json.dump(db, open(DB, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

    # Flat CSV view of the database for spreadsheets
    cols = ["id", "date", "time_et", "channel", "pillar", "format", "topic", "status", "factcheck_passed", "media",
            "sources", "buffer_post_id", "published_url"]
    with open(os.path.join(SOCIAL, "data", "content_db.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(cols)
        for p in db["posts"]:
            w.writerow([p["id"], p["date"], p["time_et"], p["channel"], p["pillar"], p["format"], p["topic"], p["status"],
                        p["factcheck"]["passed"], " | ".join(p["media"]), " | ".join(p["sources"]),
                        p["buffer"]["post_id"] or "", p["published_url"] or ""])
    mix = Counter(p["pillar"] for p in db["posts"])
    total = sum(mix.values())
    print("Pillar mix:", ", ".join(f"{k} {v} ({100 * v // total}%)" for k, v in mix.most_common()))


if __name__ == "__main__":
    main()
