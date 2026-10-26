# -*- coding: utf-8 -*-
"""Write the 30-day content calendar (CSV + Markdown). Edit ROWS, then re-run.

Columns used by pipeline.py: date, pillar, opportunity_ids, evidence_ids, status ("built" = finished in week 1,
"planned" = generate with pipeline.py). Mix target: ~40% jobs, 30% prep, 20% experience, 10% promo.
"""
import csv
import datetime as dt
import os
from collections import Counter

SOCIAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
START = dt.date(2026, 10, 27)
# pillar, IG format, IG topic, TikTok topic, Threads topics, opportunity ids, evidence ids, needs live research
ROWS = [
    ("jobs", "carousel", "5 AI training gigs open to US residents", "AI training jobs that pay, and the catch", "AI training reality check", "OD002 OD003 OD007 OD008 OD005", "WS009 WS019", "N"),
    ("prep", "carousel", "How to pass a one-shot AI training test", "Spot the mistake: AI training test practice", "Assessment tip", "OD002", "WS008 WS009", "N"),
    ("jobs", "carousel", "Laid off? Expert AI training pays for your expertise", "Laid off? AI companies pay for your expertise", "Expert AI training; AI interview tip", "OD001 OD004 OD006 OD036", "WS001 WS006", "N"),
    ("experience", "carousel", "What AI training workers actually report", "The truth about AI training side hustles", "Upwork first-client timelines", "OD001 OD002 OD003", "WS003 WS004 WS011 WS016 WS026", "N"),
    ("jobs", "carousel", "Remote W-2 jobs that hire beginners", "Remote jobs with a W-2 that hire beginners", "W-2 vs 1099", "OD039 OD040 OD041 OD042", "WS048", "N"),
    ("prep", "carousel", "Tailor your resume with AI in 45 minutes, honestly", "Fix a boring resume bullet", "ATS myth", "", "", "N"),
    ("promo", "carousel", "Inside the US Remote Job Playbook", "Remote job scam red flags (FTC data)", "Playbook announcement; remote competition data", "OD059", "WS043 WS045", "N"),
    ("jobs", "carousel", "Get paid for your opinion: 4 legit research-study sites", "Paid studies that actually pay (and what they pay)", "Prolific minimum-pay rule", "OD054 OD055 OD056 OD008", "WS028 WS029 WS050", "N"),
    ("prep", "carousel", "How AI video interviews work (Mercor, Alignerr, micro1)", "Prep for an AI interviewer in 60 seconds", "Resume deep-dive prep", "OD001 OD004 OD006", "WS001 WS020 WS025", "N"),
    ("jobs", "carousel", "What freelance platforms take from your pay", "Upwork vs Fiverr vs Contra fees", "Fee math before you price", "OD024 OD025 OD026", "", "N"),
    ("experience", "carousel", "How long the first freelance client really takes", "First client: 6 days to 6 months", "Profile beats proposal volume", "OD024 OD025", "WS031 WS032 WS033 WS036 WS037 WS038", "N"),
    ("jobs", "carousel", "Grad students: the Handshake AI Fellowship explained", "$50-125/hr for grad students? The details", "Ask your career office", "OD005", "WS022 WS023", "N"),
    ("prep", "carousel", "The Upwork proposal formula (before/after)", "Rewrite a weak proposal in 30 seconds", "First line = client's goal", "OD024", "WS031", "N"),
    ("promo", "carousel", "The 7-day urgent income plan (from the playbook)", "If you need income in 7 days, do this", "Two tracks at once", "OD002 OD003 OD008 OD054", "WS042", "N"),
    ("jobs", "carousel", "Free remote job boards worth your time", "Where remote jobs are posted first", "Apply in the first 48 hours", "OD061 OD062 OD063 OD022 OD021", "WS043", "N"),
    ("prep", "carousel", "Fix your LinkedIn headline + Open to Work settings", "LinkedIn headline formula", "Recruiters-only vs green banner", "OD059", "", "N"),
    ("experience", "carousel", "Why remote jobs feel impossible (the data)", "8% of jobs, 42% of applicants", "Referrals vs cold applying", "OD059", "WS039 WS040 WS041 WS043", "N"),
    ("jobs", "carousel", "Developer side income: AI coding evaluation and vetted networks", "Coders get paid to grade AI code", "Coding track reality", "OD009 OD002 OD028 OD033", "", "N"),
    ("prep", "carousel", "The 3-part message hiring managers answer", "DM a hiring manager without being weird", "One detail, one ask", "OD059", "WS041", "N"),
    ("jobs", "carousel", "Online tutoring: pay and commissions compared", "Tutoring online: who takes what cut", "Start on a marketplace, then go direct", "OD048 OD049 OD050", "", "N"),
    ("experience", "carousel", "Contract pay got cut? Protect yourself", "Rate cuts happen: do these 3 things", "Keep records from day one", "OD003 OD004", "WS006 WS016 WS021", "N"),
    ("prep", "carousel", "Build 8 STAR stories before your next interview", "The STAR answer, fixed", "Interview story bank", "", "", "N"),
    ("jobs", "carousel", "Laid off? Free help most people don't use", "Free job help from the government", "File for unemployment first", "OD071", "WS042", "N"),
    ("prep", "carousel", "Price freelance work after fees and taxes", "The freelance pricing formula", "Set aside 25-30% for taxes", "OD024 OD025 OD026", "", "N"),
    ("jobs", "carousel", "Expert networks: get paid for 1-hour calls", "Paid expert calls for laid-off pros", "Never share confidential info", "OD036 OD037", "WS027", "N"),
    ("experience", "carousel", "Read this before you pay for any \"job\"", "Pay-to-work red flags", "Worker-paid costs", "OD069", "WS045 WS046 WS047 WS048", "N"),
    ("prep", "carousel", "Customer service interview answers that work", "Angry customer? Say this", "Empathy + action + options", "OD039 OD040", "", "N"),
    ("jobs", "carousel", "Startup jobs: YC Work at a Startup and Wellfound", "How to get noticed by startup founders", "One profile, many founders", "OD021 OD022", "", "N"),
    ("promo", "carousel", "21 AI prompts that won't lie on your resume", "The prompt that stops AI inventing your resume", "Never-invent rule", "", "", "N"),
    ("jobs", "carousel", "Seasonal remote roles to check now (re-verify live)", "Holiday-season remote openings", "Check official careers sites", "OD039 OD040 OD041 OD042", "", "Y"),
]

rows = []
for i, r in enumerate(ROWS):
    d = START + dt.timedelta(days=i)
    rows.append({"day": i + 1, "date": d.isoformat(), "weekday": d.strftime("%a"), "pillar": r[0], "ig_format": r[1],
                 "ig_topic": r[2], "tiktok_topic": r[3], "threads_topics": r[4], "opportunity_ids": r[5], "evidence_ids": r[6],
                 "needs_live_research": r[7], "status": "built" if i < 7 else "planned"})
with open(os.path.join(SOCIAL, "calendar", "30_day_calendar.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)
mix = Counter(r["pillar"] for r in rows)
md = ["# 30-Day Content Calendar: Next Offer Academy US", "",
      f"Oct 27 – Nov 25, 2026 · Mix: " + ", ".join(f"{k} {v} ({round(100 * v / len(rows))}%)" for k, v in mix.most_common()),
      "", "Days 1–7 are finished (media in `social/content/`). Days 8–30 are generated by `scripts/pipeline.py` from this calendar, "
      "then fact-checked and approved before scheduling. Default times (ET): Threads 9:00 & 17:00 · Instagram 12:00 · TikTok 19:00.", "",
      "| Day | Date | Pillar | Instagram (carousel) | TikTok | Threads | Status |", "|---|---|---|---|---|---|---|"]
for r in rows:
    md.append(f"| {r['day']} | {r['weekday']} {r['date'][5:]} | {r['pillar']} | {r['ig_topic']} | {r['tiktok_topic']} | {r['threads_topics']} | "
              f"{r['status']}{' · live research' if r['needs_live_research'] == 'Y' else ''} |")
open(os.path.join(SOCIAL, "calendar", "30_day_calendar.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
print(mix)
