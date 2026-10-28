# -*- coding: utf-8 -*-
"""Record a published post's URL and real performance numbers (from Instagram/TikTok insights or Buffer analytics).

  python3 social/scripts/record_metrics.py w2-2026-10-29-tt --url https://www.tiktok.com/@nextofferacademyus/video/... \
      --views 1200 --likes 80 --saves 40 --avg-watch-time-s 6.1 --completion-rate-pct 22 --source "TikTok analytics"
Works for week-1 ids (content_db.json) and week-2+ ids (production_db.json). Never enter estimated numbers.
"""
import argparse
import csv
import datetime as dt
import json
import os

SOCIAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DBS = [os.path.join(SOCIAL, "data", "production_db.json"), os.path.join(SOCIAL, "data", "content_db.json")]
TRACKER = os.path.join(SOCIAL, "data", "performance_tracker.csv")
INTS = ["views", "likes", "comments", "shares", "saves", "follows", "link_clicks"]
FLOATS = ["avg_watch_time_s", "completion_rate_pct"]
COLS = ["post_id", "date", "platform", "format", "topic", "hook", "publish_url", *INTS, *FLOATS,
        "engagement_rate_pct", "source_of_numbers", "updated_at"]

ap = argparse.ArgumentParser()
ap.add_argument("post_id")
ap.add_argument("--url")
ap.add_argument("--source", default="platform insights")
for f in INTS:
    ap.add_argument(f"--{f.replace('_', '-')}", type=int)
for f in FLOATS:
    ap.add_argument(f"--{f.replace('_', '-')}", type=float)
a = ap.parse_args()

for path in DBS:
    db = json.load(open(path, encoding="utf-8"))
    p = next((x for x in db["posts"] if x["id"] == a.post_id), None)
    if p:
        break
else:
    raise SystemExit(f"{a.post_id} not found")
week2 = "platform" in p
m = p.setdefault("performance" if week2 else "metrics", {})
if a.url:
    p["publish_url" if week2 else "published_url"] = a.url
    p["status"] = "PUBLISHED"
for f in INTS + FLOATS:
    v = getattr(a, f)
    if v is not None:
        m[f] = v
m["source"] = a.source
m["updated_at"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
json.dump(db, open(path, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

rows = list(csv.DictReader(open(TRACKER, encoding="utf-8"))) if os.path.exists(TRACKER) else []
views = m.get("views") or 0
eng = sum((m.get(k) or 0) for k in ("likes", "comments", "shares", "saves"))
row = {"post_id": p["id"], "date": p["date"], "platform": p.get("platform", p.get("channel")), "format": p["format"],
       "topic": p["topic"], "hook": p.get("hook") or "", "publish_url": p.get("publish_url") or p.get("published_url") or "",
       **{f: m.get(f, "") if m.get(f) is not None else "" for f in INTS + FLOATS},
       "engagement_rate_pct": round(100 * eng / views, 2) if views else "", "source_of_numbers": a.source,
       "updated_at": m["updated_at"]}
rows = [r for r in rows if r["post_id"] != p["id"]] + [row]
with open(TRACKER, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=COLS, extrasaction="ignore")
    w.writeheader()
    w.writerows(sorted(rows, key=lambda r: (r["date"], r["platform"])))
print(f"Updated {p['id']}: {row}")
