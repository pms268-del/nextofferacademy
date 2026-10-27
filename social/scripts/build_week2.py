# -*- coding: utf-8 -*-
"""Build week 2 (Oct 28 - Nov 3): render media, fact-check, write production briefs and the tracking DB.

Run: python3 social/scripts/build_week2.py
Output:
  social/content/week2/<date>/video/      video.mp4 (TikTok + IG Reel), cover.png, captions.srt, frames/ (green-screen backgrounds)
  social/content/week2/<date>/instagram/  carousel slides (carousel days only)
  social/content/week2/<date>/BRIEF.md    everything the owner needs: hook, script, audio, caption, links, variation B
  social/data/production_db.json / .csv   one row per platform post with the workflow fields and status
Statuses: IDEA -> DRAFT -> REVIEW -> APPROVED -> READY TO PUBLISH -> PUBLISHED (existing statuses are preserved).
"""
import csv
import datetime as dt
import json
import os
import sys
from zoneinfo import ZoneInfo

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
SOCIAL = os.path.dirname(SCRIPTS)
REPO = os.path.dirname(SOCIAL)
sys.path.insert(0, SCRIPTS)
import factcheck  # noqa: E402
import render  # noqa: E402
import render2  # noqa: E402
from week2_content import TOPICS  # noqa: E402

ET = ZoneInfo("America/New_York")
DB = os.path.join(SOCIAL, "data", "production_db.json")
OUT = os.path.join(SOCIAL, "content", "week2")
LIB = "social/research/trend_reference_library.md"
STATUSES = ["IDEA", "DRAFT", "REVIEW", "APPROVED", "READY TO PUBLISH", "PUBLISHED"]
TIMES = {"instagram": "12:00", "tiktok": "19:00"}
FIELDS = ["platform", "topic", "reference_url", "hook", "script", "media", "audio_suggestion", "caption", "keywords",
          "cta", "status", "publish_url", "performance"]


def rel(p):
    return os.path.relpath(p, REPO)


def ref_urls(topic):
    """Reference URLs for the topic's trend references (from the library table)."""
    rows = {}
    for line in open(os.path.join(REPO, LIB), encoding="utf-8"):
        if line.startswith("| R"):
            cells = [c.strip() for c in line.split("|")]
            url = cells[2].split("](")[-1].rstrip(")") if "](" in cells[2] else ""
            rows[cells[1]] = url
    return [rows[r] for r in topic["reference_ids"] if r in rows]


def check_video(path):
    info = render.probe(path)
    v = [s for s in info["streams"] if s["codec_type"] == "video"][0]
    d = float(info["format"]["duration"])
    issues = []
    if (v["width"], v["height"]) != (1080, 1920):
        issues.append("Video is not 1080x1920")
    if not 15 <= d <= 45:
        issues.append(f"Video is {d:.1f}s (target 15-45s)")
    return {"issues": issues, "duration_s": round(d, 1)}


def check_slides(files):
    from PIL import Image
    issues = [f"{os.path.basename(f)} is not 1080x1350" for f in files if Image.open(f).size != (1080, 1350)]
    if not 2 <= len(files) <= 10:
        issues.append(f"Carousel needs 2-10 images, has {len(files)}")
    return {"issues": issues}


def script_text(t):
    return " ".join(sc["vo"] for sc in t["scenes"])


def brief(t, d, video, slides, refs, fcs):
    ig_is_reel = t["ig_format"] == "reel"
    b = t["variation_b"]
    md = [f"# {d} · {t['topic']}", "",
          f"**Status:** REVIEW (Buffer drafts saved, Notify Me mode, nothing published) · **Pillar:** {t['pillar']}", "",
          "## Variation A: ready-made video", "",
          f"**Hook (first 3 s):** {t['hook_a']}", "",
          f"**Video:** `{rel(video)}` ({sum(s['secs'] for s in t['scenes'])} s, silent: add audio in the app)", "",
          "| # | Secs | On screen | Voiceover / caption line |", "|---|---|---|---|"]
    for i, sc in enumerate(t["scenes"], 1):
        on = " / ".join(str(v).replace("\n", " / ") for k, v in sc.items() if k not in ("kind", "secs", "vo"))
        md.append(f"| {i} | {sc['secs']} | {on} | {sc['vo']} |")
    md += ["", f"**Full voiceover script (optional, read it yourself or use the app's text-to-speech):** {script_text(t)}", "",
           f"**Audio suggestion:** {t['audio']}", "",
           "## Variation B: film it yourself", "",
           f"**Hook:** {b['hook']}", "", f"**Format:** {b['format']}", "",
           "**Script:**", ""] + [f"{i}. {line}" for i, line in enumerate(b["script"], 1)] + [
           "", f"**Shooting notes:** {b['shots']}", "",
           "## Captions", "", "**TikTok:**", "", "```", t["tiktok_caption"], "```", "",
           f"**Instagram ({'Reel, same video' if ig_is_reel else 'carousel'}):**", "", "```",
           t["ig_caption"] + "\n\n" + " ".join(t["ig_hashtags"]), "```", ""]
    if slides:
        md += [f"**Carousel slides:** `{rel(os.path.dirname(slides[0]))}/` ({len(slides)} slides)", ""]
    md += [f"**CTA:** {t['cta']}", "", f"**Keywords (say/show them; TikTok search reads on-screen text and captions):** {', '.join(t['keywords'])}", "",
           "**Application / official links:**"] + ([f"- {u}" for u in t["app_links"]] or ["- (none: tips post)"]) + [
           "", "**Trend references (pattern only, nothing copied):**"] + [f"- {r}: {u}" for r, u in zip(t["reference_ids"], refs)] + [
           "", "**Sources:**"] + [f"- {s}" for s in t["sources"]] + [
           "", "**Automated check:** " + "; ".join(f"{k}: {'PASS' if v['passed'] else 'FAIL'}" for k, v in fcs.items()), ""]
    for k, v in fcs.items():
        md += [f"- {k} issue: {i}" for i in v["issues"]]
    md += ["## Before you publish (owner)", "",
           "1. Open each application link above; confirm the job is open and the pay matches.",
           "2. When Buffer notifies you, open the post in TikTok/Instagram, add a sound from the commercial library (or voiceover), add captions with the in-app auto-captions, then post.",
           "3. Paste the live link back to Claude so it can be tracked.", ""]
    open(os.path.join(d_dir(d), "BRIEF.md"), "w", encoding="utf-8").write("\n".join(md))


def d_dir(d):
    return os.path.join(OUT, d)


def main():
    db = {"posts": []}
    if os.path.exists(DB):
        db = json.load(open(DB, encoding="utf-8"))
    prev = {p["id"]: p for p in db["posts"]}
    records = []
    for t in TOPICS:
        d = t["date"]
        vdir = os.path.join(d_dir(d), "video")
        os.makedirs(vdir, exist_ok=True)
        video, _ = render2.render_video(t, vdir)
        vcheck = check_video(video)
        slides = []
        if t["ig_format"] == "carousel":
            idir = os.path.join(d_dir(d), "instagram")
            os.makedirs(idir, exist_ok=True)
            slides = render2.render_carousel(t, idir)
        refs = ref_urls(t)
        tt_post = {"channel": "tiktok", "pillar": t["pillar"], "date": d, "caption": t["tiktok_caption"],
                   "scenes": t["scenes"], "sources": t["sources"]}
        ig_post = {"channel": "instagram", "pillar": t["pillar"], "date": d, "caption": t["ig_caption"], "hashtags": t["ig_hashtags"],
                   "scenes": t["scenes"] if not slides else [], "slides": t.get("slides", []) if slides else [], "sources": t["sources"]}
        fcs = {"tiktok": factcheck.check(tt_post, vcheck),
               "instagram": factcheck.check(ig_post, check_slides(slides) if slides else vcheck)}
        brief(t, d, video, slides, refs, fcs)

        for ch, fc in fcs.items():
            pid = f"w2-{d}-{'tt' if ch == 'tiktok' else 'ig'}"
            local = dt.datetime.fromisoformat(f"{d}T{TIMES[ch]}").replace(tzinfo=ET)
            old = prev.get(pid, {})
            media = [video] if ch == "tiktok" or not slides else slides
            rec = {
                "id": pid, "date": d, "time_et": TIMES[ch], "due_at": local.isoformat(),
                "platform": ch, "format": "video" if ch == "tiktok" else t["ig_format"], "topic": t["topic"], "pillar": t["pillar"],
                "reference_url": refs, "hook": t["hook_a"], "script": script_text(t),
                "media": [rel(m) for m in media], "audio_suggestion": t["audio"],
                "caption": t["tiktok_caption"] if ch == "tiktok" else t["ig_caption"] + "\n\n" + " ".join(t["ig_hashtags"]),
                "keywords": t["keywords"], "cta": t["cta"], "app_links": t["app_links"], "sources": t["sources"],
                "variation_b": t["variation_b"], "brief": rel(os.path.join(d_dir(d), "BRIEF.md")),
                "factcheck": fc, "media_check": vcheck if media == [video] else check_slides(slides),
                "status": old.get("status", "DRAFT"), "needs_native_edit": True, "scheduling_type": "notification",
                "buffer": old.get("buffer", {"channel_id": None, "post_id": None, "idea_id": None, "state": None}),
                "approval": old.get("approval", {"approved_by": None, "approved_at": None}),
                "publish_url": old.get("publish_url"),
                "performance": old.get("performance", {"views": None, "likes": None, "comments": None, "shares": None,
                                                       "saves": None, "follows": None, "link_clicks": None, "updated_at": None}),
            }
            assert rec["status"] in STATUSES, rec["status"]
            records.append(rec)
            print(f"{pid:<18} {rec['format']:<9} {'PASS' if fc['passed'] else 'FAIL'} {vcheck['duration_s']}s"
                  + "".join(f"\n    ! {i}" for i in fc["issues"]))

    db = {"updated_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), "statuses": STATUSES, "posts": records}
    json.dump(db, open(DB, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    with open(DB.replace(".json", ".csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["id", "date", "time_et"] + FIELDS + ["buffer_post_id"])
        for r in records:
            perf = "; ".join(f"{k}={v}" for k, v in r["performance"].items() if v is not None)
            w.writerow([r["id"], r["date"], r["time_et"], r["platform"], r["topic"], " | ".join(r["reference_url"]), r["hook"],
                        r["script"], " | ".join(r["media"]), r["audio_suggestion"], r["caption"], ", ".join(r["keywords"]),
                        r["cta"], r["status"], r["publish_url"] or "", perf, r["buffer"].get("post_id") or ""])


if __name__ == "__main__":
    main()
