# -*- coding: utf-8 -*-
"""Move week-2+ posts through the workflow statuses in data/production_db.json.

  IDEA -> DRAFT -> REVIEW -> APPROVED -> READY TO PUBLISH -> PUBLISHED

  python3 social/scripts/status.py list
  python3 social/scripts/status.py approve w2-2026-10-29-tt --by "Name" [--live-checked]
  python3 social/scripts/status.py ready w2-2026-10-29-tt       # after Buffer is switched from draft to Notify Me schedule
  python3 social/scripts/status.py published w2-2026-10-29-tt --url https://www.tiktok.com/@nextofferacademyus/video/...
  python3 social/scripts/status.py back w2-2026-10-29-tt --notes "why"   # returns to DRAFT

Job posts (pillar=jobs) need --live-checked to be approved. Statuses only move forward one step,
except `back`. Nothing here talks to Buffer: Claude (or you) changes Buffer, then records it here.
"""
import argparse
import datetime as dt
import json
import os

SOCIAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(SOCIAL, "data", "production_db.json")
ORDER = ["IDEA", "DRAFT", "REVIEW", "APPROVED", "READY TO PUBLISH", "PUBLISHED"]
TARGET = {"approve": "APPROVED", "ready": "READY TO PUBLISH", "published": "PUBLISHED", "review": "REVIEW"}


def now():
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["list", "review", "approve", "ready", "published", "back"])
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--by")
    ap.add_argument("--url")
    ap.add_argument("--notes")
    ap.add_argument("--live-checked", action="store_true")
    a = ap.parse_args()
    db = json.load(open(DB, encoding="utf-8"))
    posts = {p["id"]: p for p in db["posts"]}
    if a.cmd == "list":
        for p in db["posts"]:
            ok = "ok " if p["factcheck"]["passed"] else "FAIL"
            print(f"{p['id']:<18} {p['platform']:<9} {p['date']} {p['time_et']}  {p['status']:<17} checks:{ok} {p['topic']}")
        return
    for pid in a.ids:
        p = posts[pid]
        if a.cmd == "back":
            p["status"] = "DRAFT"
        else:
            want = TARGET[a.cmd]
            if ORDER.index(want) != ORDER.index(p["status"]) + 1:
                raise SystemExit(f"{pid}: is {p['status']}, can't jump to {want}")
            if want == "APPROVED":
                if not a.by:
                    raise SystemExit("--by is required")
                if not p["factcheck"]["passed"]:
                    raise SystemExit(f"{pid}: automated checks failed: {p['factcheck']['issues']}")
                if p["pillar"] == "jobs" and not a.live_checked:
                    raise SystemExit(f"{pid}: job post. Open every link in app_links, confirm pay/eligibility, then pass --live-checked")
                p["approval"] = {"approved_by": a.by, "approved_at": now(), "live_checked": a.live_checked, "notes": a.notes}
            if want == "PUBLISHED":
                if not a.url:
                    raise SystemExit("--url (the live post link) is required")
                p["publish_url"] = a.url
                p["performance"]["published_at"] = now()
            p["status"] = want
        p.setdefault("history", []).append({"at": now(), "status": p["status"], "by": a.by, "notes": a.notes})
        print(f"{pid}: {p['status']}")
    db["updated_at"] = now()
    json.dump(db, open(DB, "w", encoding="utf-8"), indent=2, ensure_ascii=False)


if __name__ == "__main__":
    main()
