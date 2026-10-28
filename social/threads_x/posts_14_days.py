# -*- coding: utf-8 -*-
"""14 days of personal-style Threads + X posts. Run to validate lengths/facts and write posts_14_days.md/.csv.

Rules: no invented personal experiences; first-person opinions are marked owner_voice=True so the owner
only posts the ones they actually agree with. Every number has a source in social/research/*.md.
X limit 280 chars, Threads 500.
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE), "scripts"))

# (day, platform, kind, text, source, owner_voice)
POSTS = [
    # Day 1: intro + ghosting
    (1, "threads", "intro",
     "Starting this account to share what I find while digging through remote jobs, AI training gigs and entry-level hiring in the US.\n\nNot a guru. No \"6 figures from your couch.\" Just links that check out, numbers with sources, and honest conversations about how weird job hunting is right now.\n\nWhat are you searching for right now?",
     "", True),
    (1, "x", "intro",
     "New account. I'll be posting remote jobs, AI training gigs and entry-level roles I can actually verify, plus the numbers behind the US job search. No hype.\n\nWhat's the hardest part of your search right now?",
     "", True),
    (1, "x", "finding",
     "53% of job seekers say a potential employer ghosted them in the past year. In 2024 it was 38%.\n\nIf you're being ignored, it's not just you. It's the market. (Instant Interview data via PRSA)",
     "https://www.prsa.org/article/when-the-job-search-goes-silent-SEPT26", False),
    # Day 2: fact-checked job posts
    (2, "threads", "finding",
     "We looked into 3 viral \"remote job\" posts from TikTok topic pages.\n\n• One said $22/hr. Closest real posting: a temp bilingual role at $20–21.\n• One said $24–30/hr. The listing exists but shows no pay. That range was from a different job.\n• One said up to $42.35/hr. Listings show $18.50–35.29.\n\nThe jobs were real-ish. The numbers weren't. Always check the employer's careers page.",
     "social/research/week2_fact_sources.md", False),
    (2, "threads", "question",
     "Genuine question: where do you actually find job leads now?\n\nLinkedIn, TikTok, Indeed, friends, school career site, Reddit, somewhere else?\n\nTrying to figure out where the real ones are.",
     "", False),
    (2, "x", "finding",
     "Checked 3 viral remote job posts.\n\n$22/hr → closest real posting $20–21\n$24–30/hr → listing shows no pay\n\"Up to $42.35\" → listings top out at $35.29\n\nCheck the careers page before you apply.",
     "social/research/week2_fact_sources.md", False),
    # Day 3: AI training
    (3, "threads", "finding",
     "AI training gigs, the honest version:\n\n• DataAnnotation: reported ~$20+/hr, but the entry test is one shot\n• Prolific: must pay at least $8/hr\n• Handshake AI Fellowship: up to $125/hr listed for US grad students, no guaranteed project\n• Outlier: one worker's rate went from $50 to $15/hr (Business Insider)\n\nReal money. Unreliable volume. Stack a few, keep job hunting.",
     "social/research/week2_fact_sources.md", False),
    (3, "x", "opinion",
     "Hot take: AI training gigs are a good bridge and a bad plan.\n\nThe pay can be real. The work comes and goes, rates change, and projects end without notice.\n\nUse it to buy time, not as a career.",
     "", True),
    (3, "x", "question",
     "If you've done AI training work (DataAnnotation, Outlier, Prolific, Handshake, Mercor), what surprised you most?\n\nThe pay, the tests, the dry spells, something else?",
     "", False),
    # Day 4: entry level
    (4, "threads", "finding",
     "Entry-level job postings hit a multi-year low this summer (Indeed data, July 2026 reporting).\n\nWhat recruiters said still works: keep your profiles updated because they search them directly, and lean on personal connections who can vouch for you.\n\nBoring advice. Still the advice.",
     "https://www.kctv5.com/2026/07/30/how-new-grads-can-stand-out-entry-level-job-postings-hit-multi-year-low/", False),
    (4, "threads", "question",
     "New grads: what did your career center tell you vs what actually happened?\n\nNo judgment, just curious how big the gap is.",
     "", False),
    (4, "x", "finding",
     "3 places new grads skip:\n\n1. Handshake AI Fellowship (grad students & recent grads)\n2. YC's Work at a Startup: one profile, founders can reach out\n3. Your school's Handshake. Alumni can often still log in",
     "social/research/week2_fact_sources.md", False),
    # Day 5: scams
    (5, "threads", "finding",
     "The FTC got about 5,000 task-scam reports in all of 2023.\n\nIn the first half of 2024 alone: about 20,000.\n\nThe pattern: a \"recruiter\" texts you, moves you to WhatsApp, has you do simple tasks, then asks you to pay to unlock your earnings.\n\nReal jobs never ask you to pay. Report it at ReportFraud.ftc.gov.",
     "social/research/week2_fact_sources.md", False),
    (5, "x", "finding",
     "Fake WFH job post checklist:\n\n🚩 Phone number + \"DM me\"\n🚩 Pay for training or equipment\n🚩 Moves you to WhatsApp/Telegram\n\nFTC: $220M+ lost to job scams in H1 2024 alone.",
     "social/research/week2_fact_sources.md", False),
    (5, "x", "question",
     "Have you ever gotten a \"job offer\" text you never applied for?\n\nWhat did it say? Trying to collect the current scripts so people can spot them.",
     "", False),
    # Day 6: application math
    (6, "threads", "finding",
     "One laid-off developer published his whole 2025 job search:\n\n152 applications → 6 interviews. 101 never got a reply.\n\nAcross ~461K tracked applications, the median time to a first offer was 68.5 days (Huntr, Q2 2025).\n\nIf you're at month two with nothing, you're roughly on schedule. That's bleak and also kind of reassuring.",
     "social/research/week2_fact_sources.md", False),
    (6, "threads", "question",
     "How many applications are you at right now?\n\nAnd how many actual human replies?\n\nCurious what the real ratio looks like for people here.",
     "", False),
    (6, "x", "finding",
     "Remote jobs: ~8% of LinkedIn postings, 42% of applications.\n\nThat's why remote listings feel impossible. Apply in the first 48 hours, then message someone on the team.",
     "social/research/week2_fact_sources.md", False),
    # Day 7: AI interviews
    (7, "threads", "finding",
     "More AI-training companies interview you with an AI now (Mercor, Alignerr, micro1).\n\nWhat Mercor says about theirs: ~20 minutes, questions come from your resume, there's a free practice round, and you can redo it before submitting.\n\nSo the prep is basically: know every line on your resume and have 3 project stories ready.",
     "social/research/week2_fact_sources.md", False),
    (7, "x", "question",
     "Would you rather do a 20-minute AI video interview or a 45-minute call with a human recruiter?\n\nHonestly torn on this one.",
     "", True),
    (7, "x", "finding",
     "AI interview prep in one line: pick 3 projects from your resume and practice saying what you did, how, and the result in under 2 minutes each.",
     "social/research/week2_fact_sources.md", False),
    # Day 8: ghost jobs
    (8, "threads", "opinion",
     "\"Ghost jobs\" are listings that stay up but aren't really being filled, and every estimate of how common they are is different.\n\nWhat you can check yourself: is it on the company's own careers page, does it have a recent date, has it been reposted unchanged for months?\n\nIf it fails all three, don't spend an hour on the cover letter.",
     "", True),
    (8, "threads", "question",
     "Recruiters and hiring managers on here: what makes you actually open an application?\n\nGenuinely asking. Job seekers are guessing.",
     "", False),
    (8, "x", "finding",
     "Ghosting came up in ~9.5% of ~21,000 job-market complaints analyzed in a 2026 report (HireTruffle).\n\nA polite follow-up after 7–10 days is still worth sending. Worst case: silence, which you already have.",
     "https://hiretruffle.com/reports/recruiting-complaints-2026", False),
    # Day 9: resume
    (9, "threads", "finding",
     "3 resume fixes that take less than a minute:\n\n1. File name: Firstname-Lastname-Resume.pdf\n2. Contact info in the body, not the page header (some systems misread headers)\n3. Swap one duty for a real number you can explain\n\nIf you can't explain a line in an interview, delete it.",
     "social/research/week2_fact_sources.md", False),
    (9, "x", "opinion",
     "Unpopular opinion: using AI on your resume is fine. Letting AI invent numbers on your resume is how you get caught in the interview.\n\nGive it your facts and a rule: \"never add anything I didn't write.\"",
     "", True),
    (9, "x", "question",
     "What's the worst resume advice you've ever gotten?",
     "", False),
    # Day 10: startup hiring
    (10, "threads", "finding",
     "If you want a startup job, YC's Work at a Startup is underrated: you make one profile, you can apply directly, and founders can message you.\n\nWorth 20 minutes if LinkedIn has been a black hole.\n\nworkatastartup.com",
     "social/research/week2_fact_sources.md", False),
    (10, "threads", "question",
     "Startup vs big company for your first job: which would you pick right now, and why?\n\nThe answer feels different in 2026 than it did a few years ago.",
     "", False),
    (10, "x", "question",
     "Founders and early startup employees: what got your first hire's attention? A cold email, a project, a referral?",
     "", False),
    # Day 11: freelance / income stacking
    (11, "threads", "opinion",
     "\"Income stacking\" is the most honest phrase in the remote work world right now.\n\nA part-time W-2 support role + one AI training platform + a freelance client isn't glamorous. But no single one of those can fire you all at once.\n\nIs anyone here actually doing this? What's your stack?",
     "", True),
    (11, "x", "finding",
     "Before you join any gig platform, check one thing: do they ever ask you to pay?\n\nTraining fees, equipment deposits, \"unlock\" fees. If yes, walk away. Legit platforms pay you.",
     "", False),
    (11, "x", "question",
     "W-2 remote job at $16/hr or 1099 gig work that sometimes pays $25/hr but isn't steady.\n\nWhich would you take?",
     "", False),
    # Day 12: LinkedIn
    (12, "threads", "finding",
     "Recruiters are actively searching profiles and reaching out to candidates directly (Indeed, July 2026 reporting).\n\nSo the boring stuff matters: a headline that says what job you want, a current location, and your skills spelled the way the job posts spell them.",
     "https://www.kctv5.com/2026/07/30/how-new-grads-can-stand-out-entry-level-job-postings-hit-multi-year-low/", False),
    (12, "x", "question",
     "Has a LinkedIn message ever turned into an actual interview for you? What did the message say?",
     "", False),
    # Day 13: struggles
    (13, "threads", "opinion",
     "The job search advice that annoys me most: \"just network.\"\n\nNetworking works, but nobody explains what it means when you don't know anyone. For most people it's: message one person on the team after you apply, keep it to three sentences, ask one specific question.\n\nWhat would you add?",
     "", True),
    (13, "threads", "question",
     "What's one thing that actually helped your job search that nobody talks about?",
     "", False),
    (13, "x", "opinion",
     "The job search is a numbers game, but the numbers are applications × response rate.\n\nMost people only work on the first one.",
     "", True),
    (13, "x", "finding",
     "Follow-up email that's easy to send:\n\n\"Hi [name], I applied for [role] on [date] and I'm still very interested. Happy to share anything else that would help. Thanks!\"\n\nSend it after 7–10 days.",
     "", False),
    # Day 14: recap + conversation
    (14, "threads", "question",
     "Two weeks of posting about remote jobs, AI training gigs and entry-level hiring.\n\nWhat do you want more of: verified job leads, scam breakdowns, interview prep, or real numbers on the market?",
     "", True),
    (14, "x", "question",
     "What should I look into next: AI training platforms, remote customer support jobs, startup hiring, or entry-level government jobs?",
     "", True),
]

LIMITS = {"x": 280, "threads": 500}


def main():
    import factcheck
    problems = []
    for day, plat, kind, text, src, ov in POSTS:
        if len(text) > LIMITS[plat]:
            problems.append(f"Day {day} {plat}: {len(text)} chars > {LIMITS[plat]}")
        post = {"channel": "threads", "pillar": "experience", "date": "2026-10-28", "text": text,
                "sources": [src] if src else []}
        fc = factcheck.check(post)
        problems += [f"Day {day} {plat}: {i}" for i in fc["issues"]]
    per_day = {}
    for day, plat, *_ in POSTS:
        per_day.setdefault(day, {"threads": 0, "x": 0})[plat] += 1
    for d, c in per_day.items():
        if not (1 <= c["threads"] <= 2 and 1 <= c["x"] <= 2):
            problems.append(f"Day {d}: {c}")
    if problems:
        print("\n".join(problems))
        sys.exit(1)

    md = ["# 14 Days of Threads + X Posts", "",
          "Personal-style posts for the owner's new accounts. **Owner voice** = a first-person opinion; post it only if you agree, or edit it into your own words.",
          "Every number has a source. Status for all: **DRAFT** (accounts not connected yet).", ""]
    with open(os.path.join(HERE, "posts_14_days.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["day", "platform", "kind", "text", "chars", "source", "owner_voice", "status", "buffer_post_id", "publish_url", "performance"])
        for day, plat, kind, text, src, ov in POSTS:
            w.writerow([day, plat, kind, text, len(text), src, ov, "DRAFT", "", "", ""])
    cur = None
    for day, plat, kind, text, src, ov in POSTS:
        if day != cur:
            md += [f"## Day {day}", ""]
            cur = day
        tag = f"**{'Threads' if plat == 'threads' else 'X'}** · {kind}" + (" · owner voice" if ov else "") + f" · {len(text)} chars"
        md += [tag, "", "> " + text.replace("\n", "\n> "), ""]
        if src:
            md += [f"Source: {src}", ""]
    open(os.path.join(HERE, "posts_14_days.md"), "w", encoding="utf-8").write("\n".join(md))
    print(f"OK: {sum(1 for p in POSTS if p[1] == 'threads')} Threads, {sum(1 for p in POSTS if p[1] == 'x')} X posts over {len(per_day)} days")


if __name__ == "__main__":
    main()
