# -*- coding: utf-8 -*-
"""Automated pre-approval checks for a post. Human approval is still required.

Checks:
  - every dollar figure shown on screen / in captions exists in the research corpus
  - every source is a known research URL (or a repo file)
  - referenced opportunities exist, are not Unavailable, and were verified recently
  - banned hype phrases, platform length limits, required media specs
"""
import csv
import datetime as dt
import os
import re

SOCIAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(SOCIAL)
CORPUS_FILES = ["us/OPPORTUNITY_DIRECTORY.csv", "us/WORKER_SUCCESS_RESEARCH.csv",
                "us/research/00_RESEARCH_LOG_US.md", "us/PLAYBOOK.md", "social/data/opportunities.json"]
MAX_AGE_DAYS = 14  # job facts older than this must be re-verified before approval
BANNED = [r"guaranteed (income|job|pay|earnings|approval|work)", r"easy money", r"get rich", r"passive income",
          r"100% legit", r"make \$\d[\d,]* (a|per) (day|week)", r"instant approval", r"no (interview|experience) (and|\+) \$"]
LIMITS = {"instagram": 2200, "tiktok": 2200, "threads": 500}
MONEY = re.compile(r"\$\d[\d,]*(?:\.\d+)?")


def _corpus():
    text = []
    for f in CORPUS_FILES:
        p = os.path.join(REPO, f)
        if os.path.exists(p):
            text.append(open(p, encoding="utf-8-sig").read())
    return "\n".join(text)


def _directory():
    p = os.path.join(REPO, "us/OPPORTUNITY_DIRECTORY.csv")
    return {r["id"]: r for r in csv.DictReader(open(p, encoding="utf-8-sig"))}


CORPUS = _corpus()
DIRECTORY = _directory()


def visible_text(post):
    parts = [post.get("caption", ""), post.get("text", "")]
    for s in post.get("slides", []):
        parts += [str(v) for k, v in s.items() if k != "type"]
    for sc in post.get("scenes", []):
        parts.append(sc["text"])
    return "\n".join(parts)


def money_in_corpus(fig):
    num = fig.replace("$", "")
    variants = {fig, num, num.replace(",", "")}
    if num.endswith(".00"):
        variants.add(num[:-3])
    return any(v and v in CORPUS for v in variants)


def check(post, media_report=None):
    issues, warnings = [], []
    text = visible_text(post)

    for fig in sorted(set(MONEY.findall(text))):
        if not money_in_corpus(fig):
            issues.append(f"Dollar figure {fig} not found in research corpus")

    low = text.lower()
    for b in BANNED:
        m = re.search(b, low)
        if m:
            issues.append(f"Banned/hype phrase: '{m.group(0)}'")

    body = post.get("caption") or post.get("text") or ""
    if post["channel"] == "instagram" and post.get("hashtags"):
        body = body + "\n\n" + " ".join(post["hashtags"])
    if len(body) > LIMITS[post["channel"]]:
        issues.append(f"{post['channel']} text is {len(body)} chars (limit {LIMITS[post['channel']]})")

    for s in post.get("sources", []):
        if s.startswith("http"):
            if s not in CORPUS:
                warnings.append(f"Source not in research corpus (verify manually): {s}")
        elif not os.path.exists(os.path.join(REPO, s)):
            issues.append(f"Source file missing: {s}")
    if post["pillar"] == "jobs" and not post.get("sources"):
        issues.append("Job post has no sources")

    post_date = dt.date.fromisoformat(post["date"])
    for oid in post.get("opportunity_ids", []):
        row = DIRECTORY.get(oid)
        if not row:
            issues.append(f"Unknown opportunity id {oid}")
            continue
        if row["status"] == "Unavailable":
            issues.append(f"{row['platform']} is marked Unavailable")
        age = (post_date - dt.date.fromisoformat(row["verified_date"])).days
        if age > MAX_AGE_DAYS:
            issues.append(f"{row['platform']} last verified {row['verified_date']} ({age} days before post): re-verify")
        elif post["pillar"] == "jobs":
            warnings.append(f"Re-check live listing before approval: {row['platform']} ({row['apply_link']})")

    if media_report:
        issues += media_report.get("issues", [])
    return {"passed": not issues, "issues": issues, "warnings": warnings,
            "checked_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")}
