# -*- coding: utf-8 -*-
"""Record a published post's URL and performance numbers (copy them from Instagram/TikTok insights or Buffer analytics).

  python3 social/scripts/record_metrics.py 2026-10-27-ig --url https://www.instagram.com/p/XXXX/ --views 1200 --likes 80 --saves 40
Updates content_db.json and appends a row to data/performance_tracker.csv.
"""
import argparse
import csv
import datetime as dt
import json
import os

SOCIAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(SOCIAL, "data", "content_db.json")
TRACKER = os.path.join(SOCIAL, "data", "performance_tracker.csv")
FIELDS = ["views", "likes", "comments", "shares", "saves", "follows", "link_clicks"]

ap = argparse.ArgumentParser()
ap.add_argument("post_id")
ap.add_argument("--url")
for f in FIELDS:
    ap.add_argument(f"--{f.replace('_', '-')}", type=int)
a = ap.parse_args()
db = json.load(open(DB, encoding="utf-8"))
p = next(x for x in db["posts"] if x["id"] == a.post_id)
if a.url:
    p["published_url"] = a.url
    p["status"] = "published"
for f in FIELDS:
    v = getattr(a, f)
    if v is not None:
        p["metrics"][f] = v
p["metrics"]["updated_at"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
json.dump(db, open(DB, "w", encoding="utf-8"), indent=2, ensure_ascii=False)

rows = list(csv.DictReader(open(TRACKER, encoding="utf-8"))) if os.path.exists(TRACKER) else []
m = p["metrics"]
views = m.get("views") or 0
eng = sum((m.get(k) or 0) for k in ("likes", "comments", "shares", "saves"))
row = {"post_id": p["id"], "date": p["date"], "channel": p["channel"], "pillar": p["pillar"], "topic": p["topic"],
       "published_url": p.get("published_url") or "", **{f: m.get(f) if m.get(f) is not None else "" for f in FIELDS},
       "engagement_rate_pct": round(100 * eng / views, 2) if views else "", "updated_at": m["updated_at"]}
rows = [r for r in rows if r["post_id"] != p["id"]] + [row]
with open(TRACKER, "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(row.keys()))
    w.writeheader()
    w.writerows(sorted(rows, key=lambda r: (r["date"], r["channel"])))
print(f"Updated {p['id']}: {row}")
