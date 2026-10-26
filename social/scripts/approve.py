# -*- coding: utf-8 -*-
"""Approval gate. Nothing reaches Buffer until a human approves it here.

  python3 social/scripts/approve.py list                       # what's waiting
  python3 social/scripts/approve.py show 2026-10-27-ig         # full post + checks
  python3 social/scripts/approve.py approve 2026-10-27-ig --by "Your Name" [--live-checked]
  python3 social/scripts/approve.py reject 2026-10-27-ig --by "Your Name" --notes "why"

Job posts (pillar=jobs) require --live-checked: confirm you opened each listing today
and the link, eligibility and pay still match.
"""
import argparse
import datetime as dt
import json
import os

SOCIAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(SOCIAL, "data", "content_db.json")
OPS = os.path.join(SOCIAL, "data", "opportunities.json")


def load():
    return json.load(open(DB, encoding="utf-8"))


def save(db):
    db["updated_at"] = dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")
    json.dump(db, open(DB, "w", encoding="utf-8"), indent=2, ensure_ascii=False)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["list", "show", "approve", "reject"])
    ap.add_argument("ids", nargs="*")
    ap.add_argument("--by")
    ap.add_argument("--notes")
    ap.add_argument("--live-checked", action="store_true")
    a = ap.parse_args()
    db = load()
    posts = {p["id"]: p for p in db["posts"]}
    if a.cmd == "list":
        for p in db["posts"]:
            fc = "ok " if p["factcheck"]["passed"] else "FAIL"
            print(f"{p['id']:<18} {p['channel']:<9} {p['pillar']:<10} {p['status']:<15} checks:{fc} {p['topic']}")
        return
    for pid in a.ids:
        p = posts[pid]
        if a.cmd == "show":
            print(json.dumps(p, indent=2, ensure_ascii=False))
            continue
        if not a.by:
            raise SystemExit("--by is required")
        if a.cmd == "approve":
            if not p["factcheck"]["passed"]:
                raise SystemExit(f"{pid}: automated checks failed: {p['factcheck']['issues']}")
            if p["media_check"]["issues"]:
                raise SystemExit(f"{pid}: media invalid: {p['media_check']['issues']}")
            if p["pillar"] == "jobs" and not a.live_checked:
                raise SystemExit(f"{pid}: job post - re-check live listings, then pass --live-checked")
            p["status"] = "approved"
            if p["opportunity_ids"] and a.live_checked:
                ops = json.load(open(OPS, encoding="utf-8"))
                for o in ops["opportunities"]:
                    if o["id"] in p["opportunity_ids"]:
                        o["approved_for_social"] = True
                        o["last_live_check"] = dt.date.today().isoformat()
                json.dump(ops, open(OPS, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
        else:
            p["status"] = "rejected"
        p["approval"] = {"approved_by": a.by, "approved_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds"),
                         "notes": a.notes, "live_checked": a.live_checked}
        print(f"{pid}: {p['status']}")
    save(db)


if __name__ == "__main__":
    main()
