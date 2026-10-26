# -*- coding: utf-8 -*-
"""Seed social/data/opportunities.json (the approved-opportunity database) from the playbook directory.

Only rows the playbook labels Apply Now or Explore are seeded. Nothing is approved for posting by
default: set "approved_for_social": true after you re-check the live listing (scripts/approve.py does this).
Existing approval/verification fields are preserved on re-run.
"""
import csv
import datetime as dt
import json
import os

SOCIAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(SOCIAL)
OUT = os.path.join(SOCIAL, "data", "opportunities.json")
KEEP = ["platform", "category", "status", "apply_link", "roles_and_tasks", "beginner_friendly", "us_eligibility",
        "published_pay", "pay_source", "application_steps", "evidence_strength", "sources", "verified_date"]

rows = list(csv.DictReader(open(os.path.join(REPO, "us/OPPORTUNITY_DIRECTORY.csv"), encoding="utf-8-sig")))
old = {}
if os.path.exists(OUT):
    old = {o["id"]: o for o in json.load(open(OUT, encoding="utf-8"))["opportunities"]}
ops = []
for r in rows:
    if r["status"] not in ("Apply Now", "Explore"):
        continue
    o = {"id": r["id"], **{k: r[k] for k in KEEP}}
    o["sources"] = [s.strip() for s in r["sources"].split("|")]
    o["reverify_by"] = (dt.date.fromisoformat(r["verified_date"]) + dt.timedelta(days=14)).isoformat()
    prev = old.get(r["id"], {})
    o["approved_for_social"] = prev.get("approved_for_social", False)
    o["last_live_check"] = prev.get("last_live_check")
    o["times_featured"] = prev.get("times_featured", 0)
    o["last_featured"] = prev.get("last_featured")
    ops.append(o)
json.dump({"source": "us/OPPORTUNITY_DIRECTORY.csv", "seeded_at": dt.date.today().isoformat(), "opportunities": ops},
          open(OUT, "w", encoding="utf-8"), indent=2, ensure_ascii=False)
print(f"{len(ops)} opportunities -> {OUT}")
