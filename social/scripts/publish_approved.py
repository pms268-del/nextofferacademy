# -*- coding: utf-8 -*-
"""Send APPROVED posts to Buffer and log the result.

  python3 social/scripts/publish_approved.py --mode draft      # default: create Buffer drafts only
  python3 social/scripts/publish_approved.py --mode schedule   # schedule at the post's time (requires explicit opt-in)
  python3 social/scripts/publish_approved.py --dry-run         # print what would be sent

Guards: status must be "approved", automated checks passed, media valid, scheduled time in
the future, channel enabled and matched to @nextofferacademyus (config/channels.json verified=true).
Media must be reachable at MEDIA_BASE_URL + <repo-relative path> (public, non-expiring URLs).
"""
import argparse
import csv
import datetime as dt
import json
import os
import sys

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
SOCIAL = os.path.dirname(SCRIPTS)
sys.path.insert(0, SCRIPTS)
import buffer_client as B  # noqa: E402

DB = os.path.join(SOCIAL, "data", "content_db.json")
LOG = os.path.join(SOCIAL, "data", "publication_log.csv")
LOG_COLS = ["timestamp_utc", "post_id", "channel", "action", "mode", "buffer_post_id", "result", "detail"]


def log(row):
    new = not os.path.exists(LOG)
    with open(LOG, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=LOG_COLS)
        if new:
            w.writeheader()
        w.writerow({"timestamp_utc": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"), **row})


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["draft", "schedule"], default="draft")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", nargs="*", help="limit to these post ids")
    a = ap.parse_args()
    if a.mode == "schedule" and os.environ.get("ALLOW_SCHEDULING") != "yes":
        raise SystemExit("Scheduling is locked. Set ALLOW_SCHEDULING=yes once you've approved automatic scheduling.")
    base = os.environ.get("MEDIA_BASE_URL", "").rstrip("/")
    cfg = json.load(open(os.path.join(SOCIAL, "config", "channels.json"), encoding="utf-8"))["channels"]
    db = json.load(open(DB, encoding="utf-8"))
    now = dt.datetime.now(dt.timezone.utc)
    sent = 0
    for p in db["posts"]:
        if a.only and p["id"] not in a.only:
            continue
        if p["status"] != "approved":
            continue
        ch = cfg.get(p["channel"], {})
        reasons = []
        if not p["factcheck"]["passed"]:
            reasons.append("checks failed")
        if p["media_check"]["issues"]:
            reasons.append("media invalid")
        if p["channel"] in ("instagram", "tiktok") and not p["media"]:
            reasons.append("no media")
        if dt.datetime.fromisoformat(p["scheduled_at_utc"].replace("Z", "+00:00")) <= now:
            reasons.append("scheduled time has passed")
        if not ch.get("enabled") or not ch.get("verified") or not ch.get("buffer_channel_id"):
            reasons.append(f"{p['channel']} channel not enabled/verified")
        if p["media"] and not base:
            reasons.append("MEDIA_BASE_URL not set")
        if reasons:
            log({"post_id": p["id"], "channel": p["channel"], "action": "skip", "mode": a.mode, "buffer_post_id": "",
                 "result": "skipped", "detail": "; ".join(reasons)})
            print(f"SKIP {p['id']}: {'; '.join(reasons)}")
            continue
        urls = [f"{base}/{m}" for m in p["media"]]
        inp = B.build_input(p, ch["buffer_channel_id"], urls, a.mode)
        if a.dry_run:
            print(f"DRY {p['id']}: {json.dumps(inp)[:400]}")
            continue
        try:
            res = B.create_post(inp)
            p["buffer"] = {"channel_id": ch["buffer_channel_id"], "post_id": res.get("id"), "state": res.get("status"), "error": None}
            p["status"] = "scheduled" if a.mode == "schedule" else "buffer_draft"
            log({"post_id": p["id"], "channel": p["channel"], "action": "createPost", "mode": a.mode,
                 "buffer_post_id": res.get("id"), "result": "ok", "detail": res.get("dueAt") or ""})
            sent += 1
            print(f"OK   {p['id']} -> Buffer {res.get('id')} ({p['status']})")
        except B.BufferError as e:
            p["buffer"]["error"] = str(e)[:500]
            p["status"] = "failed"
            log({"post_id": p["id"], "channel": p["channel"], "action": "createPost", "mode": a.mode,
                 "buffer_post_id": "", "result": "error", "detail": str(e)[:300]})
            print(f"FAIL {p['id']}: {e}")
    if not a.dry_run:
        json.dump(db, open(DB, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"{sent} post(s) sent to Buffer.")


if __name__ == "__main__":
    main()
