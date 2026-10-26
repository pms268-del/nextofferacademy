# -*- coding: utf-8 -*-
"""Week 1 content for Next Offer Academy US (Oct 27 - Nov 2, 2026).

Every factual claim is tied to a source URL from us/OPPORTUNITY_DIRECTORY.csv or
us/WORKER_SUCCESS_RESEARCH.csv (research date 2026-10-22). Job-related posts start
as "needs_approval" and must be re-verified against the live listing before approval.
"""

CHECKED = "Oct 22, 2026"

# Brand-wide strings
HANDLE = "@nextofferacademyus"
LINK_CTA = "Link in bio"

POSTS = []


def post(**kw):
    POSTS.append(kw)


# ============================================================ DAY 1 · Tue Oct 27 · JOBS
post(id="2026-10-27-ig", date="2026-10-27", time_et="12:00", channel="instagram", format="carousel",
     pillar="jobs", topic="5 AI training gigs open to US residents",
     opportunity_ids=["OD002", "OD003", "OD007", "OD008", "OD005"],
     slides=[
         {"type": "cover", "kicker": "VERIFIED OPPORTUNITIES", "title": "5 AI training gigs open to US residents",
          "sub": f"The pay they actually list, and the catch nobody mentions. Checked {CHECKED}."},
         {"type": "item", "n": 1, "title": "DataAnnotation", "body": "Write, compare and rate chatbot answers. Strong English writing is the main requirement.",
          "pill": "Reported: ~$20+/hr to start", "catch": "One ~1-hour entry test. No retakes, and often no email if you don't pass.",
          "src": "dataannotation.tech · pay per 2026 reviews quoting the FAQ"},
         {"type": "item", "n": 2, "title": "Outlier", "body": "Generalist and expert AI-training tasks. Onboarding takes 30–90 minutes.",
          "pill": "Listed: up to ~$15/hr generalist", "catch": "Workers report empty queues: accepted, but no tasks for days.",
          "src": "outlier.ai · onboarding per Outlier blog"},
         {"type": "item", "n": 3, "title": "TELUS Digital", "body": "US Content Reviewer: part-time, self-scheduled rating work.",
          "pill": "Listing: est. $14/hr", "catch": "Unpaid qualification exam. One person per household.",
          "src": "Job-board copy of the TELUS listing, open to Nov 27, 2026"},
         {"type": "item", "n": 4, "title": "Prolific", "body": "Paid academic and AI research studies. The US is a supported country.",
          "pill": "Rule: min $8/hr, $12 recommended", "catch": "New sign-ups may be waitlisted. Small amounts per study.",
          "src": "Prolific help center"},
         {"type": "item", "n": 5, "title": "Handshake AI Fellowship", "body": "For US-based master's/PhD students and grads in any field.",
          "pill": "Handshake FAQ: $50–125/hr", "catch": "Applying doesn't guarantee a project. Projects can pause on short notice.",
          "src": "Handshake help center + Cornell Grad School posting"},
         {"type": "cta", "title": "Apply to 3, not 1.", "body": "Getting accepted isn't the same as getting work. Stack platforms, and never pay to join one.",
          "action": "Save this · Follow for verified openings"},
     ],
     caption=("5 AI training gigs open to US residents right now, with the pay each one actually lists 👇\n\n"
              "1. DataAnnotation: write and rate chatbot answers (reported ~$20+/hr to start)\n"
              "2. Outlier: generalist AI tasks (listed up to ~$15/hr)\n"
              "3. TELUS Digital: US Content Reviewer (listing est. $14/hr)\n"
              "4. Prolific: paid research studies ($8/hr minimum rule)\n"
              "5. Handshake AI Fellowship: US grad students ($50–125/hr per Handshake)\n\n"
              "The honest part: these are contract gigs. Work comes and goes, and some entry tests are one-shot. "
              "Apply to a few at once and treat them as income stacking, not a salary.\n\n"
              f"Pay and eligibility checked {CHECKED}. Always confirm on the official site before you apply.\n\n"
              "Which one are you trying first? 👇"),
     hashtags=["#remotejobs", "#aitraining", "#workfromhome", "#sidehustle", "#jobsearch"],
     sources=["https://www.secondtalent.com/resources/is-dataannotation-legit/",
              "https://outlier.ai/blog/your-first-steps-on-outlier-what-to-expect-from-onboarding",
              "https://theairankings.com/ai-jobs/outlier-review/",
              "https://cazvid.com/en/job/content-reviewer-united-states-5cb55c",
              "https://researcher-help.prolific.com/en/articles/445266-how-much-should-i-pay-participants",
              "https://support.joinhandshake.com/hc/en-us/articles/32264709473303-MOVE-Program-Overview-FAQs-for-EDU-Partners"])

post(id="2026-10-27-tt", date="2026-10-27", time_et="19:00", channel="tiktok", format="video",
     pillar="jobs", topic="AI training jobs that pay, and the catch",
     opportunity_ids=["OD002", "OD003", "OD008"],
     hook="These companies pay you to train AI. Here's the catch.",
     scenes=[
         {"text": "They pay you to train AI.\nHere's the catch.", "vo": "These companies pay you to train AI. Here's the catch nobody mentions.", "secs": 3.5},
         {"text": "DataAnnotation\n~$20+/hr reported", "vo": "DataAnnotation pays you to write and grade chatbot answers. Reviews quote about twenty dollars an hour to start.", "secs": 5},
         {"text": "One-shot test.\nNo retakes.", "vo": "But the entry test is one shot. No retakes, and you might not get an email if you fail.", "secs": 4.5},
         {"text": "Outlier\nup to ~$15/hr listed", "vo": "Outlier lists generalist work at up to about fifteen dollars an hour.", "secs": 4},
         {"text": "\"Empty queue\" = no tasks", "vo": "But workers say the queue can sit empty for days after you're accepted.", "secs": 4},
         {"text": "Prolific\n$8/hr minimum rule", "vo": "Prolific pays for research studies, and requires at least eight dollars an hour.", "secs": 4.5},
         {"text": "Apply to 3, not 1", "vo": "So apply to three, not one. Getting accepted is not the same as getting work.", "secs": 4.5},
         {"text": "Follow for verified\nremote jobs", "vo": "Follow for verified remote jobs every day.", "secs": 3},
     ],
     caption=f"AI training gigs are real, but read the fine print first. Pay checked {CHECKED}; confirm on the official sites. #remotejobs #aitraining #sidehustle #jobsearch",
     sources=["https://www.secondtalent.com/resources/is-dataannotation-legit/", "https://theairankings.com/ai-jobs/outlier-review/",
              "https://researcher-help.prolific.com/en/articles/445266-how-much-should-i-pay-participants"])

post(id="2026-10-27-th1", date="2026-10-27", time_et="09:00", channel="threads", format="text", pillar="jobs",
     topic="AI training reality check", opportunity_ids=["OD002", "OD003"],
     text=("Quick reality check on AI training gigs:\n\nThe legit ones (DataAnnotation, Outlier, Prolific, TELUS) do pay real people. "
           "But \"accepted\" and \"working\" are two different things. Outlier workers call it the empty queue.\n\n"
           "If you're trying this, apply to 3 at once and keep your regular job search running alongside."),
     sources=["https://theairankings.com/ai-jobs/outlier-review/", "https://www.indeed.com/cmp/DataAnnotation/reviews"])

# ============================================================ DAY 2 · Wed Oct 28 · PREP
post(id="2026-10-28-ig", date="2026-10-28", time_et="12:00", channel="instagram", format="carousel",
     pillar="prep", topic="How to pass a one-shot AI training test", opportunity_ids=["OD002"],
     slides=[
         {"type": "cover", "kicker": "APPLICATION PREP", "title": "How to pass a one-shot AI training test",
          "sub": "Some entry tests (like DataAnnotation's) give you exactly one attempt. Do it right the first time."},
         {"type": "tip", "n": 1, "title": "Read every instruction twice", "body": "Word limits, format, audience, \"explain why.\" Most fails are instruction misses, not knowledge gaps."},
         {"type": "tip", "n": 2, "title": "Accuracy beats style", "body": "A friendly answer with one wrong number loses to a dry answer that's correct. Check every fact and every bit of math."},
         {"type": "tip", "n": 3, "title": "Point to the exact sentence", "body": "Don't say \"B is clearer.\" Say which line is wrong, why, and what the ideal answer would do instead."},
         {"type": "tip", "n": 4, "title": "Don't use AI to answer", "body": "Contractors have been removed for using AI tools on tasks. Write it yourself. It's what they're paying for.",
          "src": "IBTimes report on contractor removals"},
         {"type": "tip", "n": 5, "title": "Block 90 quiet minutes", "body": "Laptop, not phone. Notifications off. Proofread once before you hit submit."},
         {"type": "cta", "title": "Practice before the real test", "body": "Our playbook includes 7 original practice assessments with model answers.", "action": f"{LINK_CTA} · Save for later"},
     ],
     caption=("Some AI training platforms give you ONE shot at the entry test. DataAnnotation's Starter Assessment can't be retaken, "
              "and if you don't pass you may never hear back.\n\nHere's how to give yourself the best chance:\n"
              "✅ Read every instruction twice\n✅ Accuracy beats style, so check the math\n✅ Justify with the exact sentence\n"
              "✅ Never use AI to write your answers\n✅ Block 90 quiet minutes\n\nSave this for test day 📌"),
     hashtags=["#aitraining", "#remotework", "#jobsearchtips", "#careertips"],
     sources=["https://www.secondtalent.com/resources/is-dataannotation-legit/", "https://ibtimes.co.uk/openai-contractors-removed-using-ai-1822365"])

post(id="2026-10-28-tt", date="2026-10-28", time_et="19:00", channel="tiktok", format="video",
     pillar="prep", topic="Spot the mistake: AI training test practice", opportunity_ids=[],
     hook="Can you spot the mistake? AI companies test for this.",
     scenes=[
         {"text": "Spot the mistake 👀", "vo": "Can you spot the mistake? AI training tests check for exactly this.", "secs": 3.5},
         {"text": "\"$100 at 10% interest,\ncompounded yearly...\"", "vo": "An AI explains compound interest to a kid: one hundred dollars at ten percent, compounded every year.", "secs": 5},
         {"text": "\"...after 2 years\nyou have $120.\"", "vo": "It says after two years, you'll have one hundred twenty dollars.", "secs": 4},
         {"text": "Wrong. It's $121.", "vo": "Wrong. Year one, you get to one-ten. Year two, you earn ten percent of one-ten. That's one twenty-one.", "secs": 6},
         {"text": "$120 = simple interest", "vo": "One twenty is simple interest. The exact thing it was supposed to explain the difference from.", "secs": 4.5},
         {"text": "Accuracy > style", "vo": "On these tests, a friendly answer with a wrong number loses. Accuracy beats style.", "secs": 4.5},
         {"text": "Follow for more\npractice questions", "vo": "Follow for more practice questions before your real test.", "secs": 3},
     ],
     caption="This is the kind of error AI training tests want you to catch. Did you get it? #aitraining #remotejobs #jobsearch #mathcheck",
     sources=[])

post(id="2026-10-28-th1", date="2026-10-28", time_et="17:00", channel="threads", format="text", pillar="prep",
     topic="Assessment tip", opportunity_ids=[],
     text=("The most common way people fail AI training entry tests isn't lack of knowledge.\n\nIt's missing an instruction. "
           "\"Under 100 words.\" \"Explain why.\" \"Use bullet points.\"\n\nRead the prompt twice before you write a single word."),
     sources=[])

# ============================================================ DAY 3 · Thu Oct 29 · JOBS (experts)
post(id="2026-10-29-ig", date="2026-10-29", time_et="12:00", channel="instagram", format="carousel",
     pillar="jobs", topic="Laid off? Expert AI training pays for your expertise",
     opportunity_ids=["OD001", "OD004", "OD006", "OD036"],
     slides=[
         {"type": "cover", "kicker": "FOR LAID-OFF PROFESSIONALS", "title": "Your expertise is worth more than generalist gigs",
          "sub": f"Expert AI-training listings and paid expert calls. Checked {CHECKED}."},
         {"type": "item", "n": 1, "title": "Mercor", "body": "Hourly contracts grading and improving AI output in law, finance, medicine, engineering, writing and more.",
          "pill": "Listing seen: $50–140/hr", "catch": "~20-min AI video interview based on your resume. Silence after it is common.",
          "src": "work.mercor.com listing + Mercor docs"},
         {"type": "item", "n": 2, "title": "Alignerr", "body": "Domain-expert AI training (STEM, coding, writing).",
          "pill": "US PhD listing: $30–150/hr", "catch": "AI interviewer \"Zara\" plus a domain test, often with one attempt.",
          "src": "Official Greenhouse listing"},
         {"type": "item", "n": 3, "title": "micro1", "body": "AI trainer and expert contracts through its jobs portal.",
          "pill": "Listings: $20–98/hr", "catch": "AI interview + ID check. Confirm the rate before you start.",
          "src": "jobs.micro1.ai listings"},
         {"type": "item", "n": 4, "title": "GLG (expert calls)", "body": "Get paid for 1-hour calls sharing industry knowledge with investors and consultants.",
          "pill": "Estimates: ~$100–300/hr", "catch": "Invitations are irregular. Never share confidential employer info.",
          "src": "Advice-site estimates, not GLG figures"},
         {"type": "stat", "big": "$16/hr", "title": "The reality check", "body": "Business Insider reported Mercor contractors being offered a follow-on project at $16/hr after earlier rates up to $60. Mercor disputed it. Rates change project to project.",
          "src": "Business Insider (via AOL)"},
         {"type": "cta", "title": "Lead with your niche", "body": "\"CPA, 8 yrs multistate sales tax\" beats \"finance professional.\" Specific expertise gets matched.", "action": "Follow · Share with someone job hunting"},
     ],
     caption=("Laid off? Your professional expertise has a market right now.\n\nAI companies pay domain experts to evaluate and improve their models. "
              "Listings we checked:\n• Mercor: $50–140/hr (expert trainer listing)\n• Alignerr: $30–150/hr (US PhD listing)\n"
              "• micro1: $20–98/hr\n• GLG: paid expert calls (often estimated at $100–300/hr)\n\n"
              "The honest part: it's 1099 contract work. Projects end, rates change, and interviews often go quiet. "
              "Use it to bridge income while you search, and set aside money for taxes.\n\n"
              f"Checked {CHECKED}. Verify each listing before applying."),
     hashtags=["#layoffs", "#remotejobs", "#aitraining", "#careerchange", "#opentowork"],
     sources=["https://work.mercor.com/jobs/list_AAABlRvLjyMZ_QjpNyhB6r5E/expert-model-trainer",
              "https://talent.docs.mercor.com/how-to/prepare-for-ai-interview",
              "https://job-boards.greenhouse.io/alignerr/jobs/4600287007",
              "https://jobs.micro1.ai/post/8f87173b-4f95-4fde-8df4-9cfd4a6c337f",
              "https://expertopportunities.com/expert-network-hourly-rates/",
              "https://www.aol.com/articles/ai-startup-powering-meta-openai-230627434.html"])

post(id="2026-10-29-tt", date="2026-10-29", time_et="19:00", channel="tiktok", format="video",
     pillar="jobs", topic="Laid off? AI companies pay for your expertise", opportunity_ids=["OD001", "OD004"],
     hook="Got laid off? AI companies are paying for what you already know.",
     scenes=[
         {"text": "Laid off?\nYour expertise pays.", "vo": "Got laid off? AI companies are paying for what you already know.", "secs": 3.5},
         {"text": "Experts grade AI answers", "vo": "They hire lawyers, nurses, accountants, engineers and writers to grade and fix AI answers.", "secs": 4.5},
         {"text": "Mercor listing:\n$50–140/hr", "vo": "One Mercor listing we checked pays fifty to one-forty an hour.", "secs": 4},
         {"text": "Alignerr US PhD listing:\n$30–150/hr", "vo": "Alignerr lists thirty to one-fifty for US-based PhD trainers.", "secs": 4},
         {"text": "20-min AI interview", "vo": "Mercor starts with a twenty-minute AI interview about your resume. Know every line on it.", "secs": 4.5},
         {"text": "It's contract work", "vo": "It's contract work. Projects end and rates change, so treat it as a bridge.", "secs": 4},
         {"text": "Be specific", "vo": "Lead with your exact niche, not just your job title.", "secs": 3.5},
         {"text": "Follow for verified\nremote work", "vo": "Follow for verified remote work every day.", "secs": 3},
     ],
     caption=f"Laid off? Expert AI training can bridge income. Listings checked {CHECKED}; verify before applying. #layoffs #remotejobs #aitraining #opentowork",
     sources=["https://work.mercor.com/jobs/list_AAABlRvLjyMZ_QjpNyhB6r5E/expert-model-trainer",
              "https://job-boards.greenhouse.io/alignerr/jobs/4600287007",
              "https://talent.docs.mercor.com/how-to/prepare-for-ai-interview"])

post(id="2026-10-29-th1", date="2026-10-29", time_et="09:00", channel="threads", format="text", pillar="jobs",
     topic="Expert AI training for laid-off pros", opportunity_ids=["OD001", "OD005"],
     text=("If you were laid off from a specialist role (accounting, nursing, law, engineering, teaching), look at expert AI-training listings.\n\n"
           "Mercor has listed $50–140/hr expert roles. Handshake's AI Fellowship lists $50–125/hr for US grad students and grads.\n\n"
           "Contract work, not a salary, but it pays for what you already know."),
     sources=["https://work.mercor.com/jobs/list_AAABlRvLjyMZ_QjpNyhB6r5E/expert-model-trainer",
              "https://support.joinhandshake.com/hc/en-us/articles/32264709473303-MOVE-Program-Overview-FAQs-for-EDU-Partners"])

post(id="2026-10-29-th2", date="2026-10-29", time_et="17:00", channel="threads", format="text", pillar="prep",
     topic="AI interview tip", opportunity_ids=["OD001", "OD004"],
     text=("AI interviewers (Mercor, Alignerr's \"Zara\", micro1) build their questions from your resume.\n\n"
           "So before you start: pick your 3 biggest projects and practice explaining each in 2 minutes. What you did, how, and the result with a number.\n\n"
           "Vague resume = vague interview."),
     sources=["https://talent.docs.mercor.com/how-to/prepare-for-ai-interview", "https://au.trustpilot.com/review/www.alignerr.com?page=8"])

# ============================================================ DAY 4 · Fri Oct 30 · EXPERIENCE
post(id="2026-10-30-ig", date="2026-10-30", time_et="12:00", channel="instagram", format="carousel",
     pillar="experience", topic="What AI training workers actually report", opportunity_ids=["OD001", "OD002", "OD003"],
     slides=[
         {"type": "cover", "kicker": "REAL WORKER EXPERIENCES", "title": "What AI training workers actually report",
          "sub": "The good and the bad, from reviews and reporting. Not hype."},
         {"type": "stat", "big": "4.1/5", "title": "The good: DataAnnotation", "body": "Rated 4.1 on Indeed (1,477 reviews, June 2026). Reviewers say payment is \"prompt and problem free.\"",
          "src": "Indeed company reviews"},
         {"type": "stat", "big": "Weekly", "title": "The good: Mercor pay", "body": "Indeed reviewers consistently praise weekly pay. Mercor's docs confirm weekly payouts for hourly contracts.",
          "src": "Indeed reviews + Mercor docs"},
         {"type": "stat", "big": "$50→$15", "title": "The bad: rate cuts", "body": "Business Insider reported an Outlier annotator whose hourly pay on generalist projects dropped from $50 to $15.",
          "src": "Business Insider (via Yahoo)"},
         {"type": "stat", "big": "2 wks–6 mo", "title": "The bad: long silences", "body": "Mercor applicants on Indeed report waiting \"2 weeks to 6 months\" to hear back, or never.",
          "src": "Indeed reviews"},
         {"type": "stat", "big": "500+", "title": "The trend: specialists win", "body": "xAI laid off at least 500 generalist AI tutors in Sept 2025 while planning to grow specialist tutors 10x.",
          "src": "Business Insider via Reuters"},
         {"type": "cta", "title": "The pattern", "body": "Real money, unstable volume. Specialize, stack platforms, and keep a steady job search going.", "action": "Follow for honest remote-work research"},
     ],
     caption=("We went through worker reviews and news reporting on AI training gigs. The honest picture:\n\n"
              "👍 DataAnnotation: 4.1/5 on Indeed, \"payment is prompt\"\n👍 Mercor: weekly pay praised\n"
              "👎 Outlier: one annotator's rate fell from $50 to $15/hr (Business Insider)\n👎 Long silences after interviews\n"
              "📉 xAI cut 500+ generalist tutors while expanding specialists\n\n"
              "Takeaway: specialize where you can, and treat these gigs as income stacking.\n\nHave you tried one? Tell us what happened 👇"),
     hashtags=["#aitraining", "#remotework", "#gigeconomy", "#jobsearch"],
     sources=["https://www.indeed.com/cmp/DataAnnotation/reviews", "https://www.indeed.com/cmp/Mercor/reviews",
              "https://talent.docs.mercor.com/how-to/payments",
              "https://tech.yahoo.com/ai/articles/inside-lucrative-surreal-disturbing-world-081101391.html",
              "https://www.aol.com/articles/musks-xai-lays-off-hundreds-025738720.html"])

post(id="2026-10-30-tt", date="2026-10-30", time_et="19:00", channel="tiktok", format="video",
     pillar="experience", topic="The truth about AI training side hustles", opportunity_ids=["OD002", "OD003"],
     hook="We read the reviews on AI training gigs so you don't have to.",
     scenes=[
         {"text": "AI training gigs:\nthe honest version", "vo": "We read the worker reviews and news reports on AI training gigs. Here's the honest version.", "secs": 4.5},
         {"text": "👍 They do pay", "vo": "The good: they do pay. DataAnnotation is rated four point one on Indeed, and reviewers call payment prompt.", "secs": 5},
         {"text": "👎 Rates can drop", "vo": "The bad: rates can drop. Business Insider reported one Outlier worker going from fifty to fifteen dollars an hour.", "secs": 5.5},
         {"text": "👎 Work comes and goes", "vo": "Work comes and goes. Accepted doesn't mean busy.", "secs": 3.5},
         {"text": "📈 Specialists last longer", "vo": "And the trend? xAI cut five hundred generalist tutors while hiring more specialists.", "secs": 5},
         {"text": "Stack. Specialize.\nKeep searching.", "vo": "So stack platforms, specialize where you can, and keep your job search going.", "secs": 4},
         {"text": "Follow for honest\nremote-work research", "vo": "Follow for honest remote-work research.", "secs": 3},
     ],
     caption="AI training gigs: real money, unstable volume. Sources: Indeed reviews, Business Insider. #aitraining #sidehustle #remotework #gigwork",
     sources=["https://www.indeed.com/cmp/DataAnnotation/reviews",
              "https://tech.yahoo.com/ai/articles/inside-lucrative-surreal-disturbing-world-081101391.html",
              "https://www.aol.com/articles/musks-xai-lays-off-hundreds-025738720.html"])

post(id="2026-10-30-th1", date="2026-10-30", time_et="09:00", channel="threads", format="text", pillar="experience",
     topic="Upwork first-client timelines", opportunity_ids=["OD024"],
     text=("What first-client timelines on Upwork actually look like, from freelancers on Upwork's own community forum:\n\n"
           "• \"About 2 months to land my first client, and 3 weeks after that to land my next\"\n"
           "• Others sent proposals for 6 months, and broke through only after narrowing their niche\n\n"
           "If you're 3 weeks in with nothing, change the profile, not just the number of proposals."),
     sources=["https://community.upwork.com/t5/Freelancers/How-many-proposals-til-your-first-job/m-p/1220716/highlight/true"])

# ============================================================ DAY 5 · Sat Oct 31 · JOBS (W-2)
post(id="2026-10-31-ig", date="2026-10-31", time_et="12:00", channel="instagram", format="carousel",
     pillar="jobs", topic="Remote W-2 jobs that hire beginners", opportunity_ids=[],
     slides=[
         {"type": "cover", "kicker": "REMOTE JOBS WITH A W-2", "title": "Remote jobs that hire beginners (with a real paycheck)",
          "sub": "Customer support and tech support. Apply only on the official careers sites."},
         {"type": "item", "n": 1, "title": "Amazon Virtual Customer Service", "body": "Chat and phone support from home. Openings come in waves, by state.",
          "pill": "Reported: ~$15–19/hr", "catch": "Apply only at amazon.jobs. Scammers copy this listing.", "src": "Third-party pay reports"},
         {"type": "item", "n": 2, "title": "Apple At Home Advisor", "body": "AppleCare support from home. There's a College Program version for students.",
          "pill": "College listing: $27.75–32.45/hr", "catch": "Seasonal and location-limited. Check jobs.apple.com monthly.", "src": "tech.co report"},
         {"type": "item", "n": 3, "title": "Concentrix", "body": "Customer service and tech support for big brands.",
          "pill": "Reported: ~$13–18/hr", "catch": "Internet speed test and background check. State limits apply.", "src": "2026 career-site reports"},
         {"type": "item", "n": 4, "title": "TTEC @Home", "body": "Customer care, tech support and sales roles.",
          "pill": "Reported: ~$15–18/hr", "catch": "Some roles pay a reduced training rate at first. Ask.", "src": "2026 career-site reports"},
         {"type": "tip", "n": "!", "title": "Why W-2 matters", "body": "Taxes are withheld, minimum wage applies, benefits are common, and you should never have to pay anything to start."},
         {"type": "cta", "title": "Never apply through a text or WhatsApp link", "body": "Type the company's careers URL yourself. If they ask you to pay for equipment or training, it's a scam.", "action": "Save · Send to a friend who needs work"},
     ],
     caption=("Need a remote job with a steady W-2 paycheck? These employers hire beginners for support roles:\n\n"
              "• Amazon Virtual Customer Service (~$15–19/hr reported)\n• Apple At Home Advisor (College Program listing $27.75–32.45/hr)\n"
              "• Concentrix (~$13–18/hr reported)\n• TTEC @Home (~$15–18/hr reported)\n\n"
              "Pay varies by state and role, so check the live posting. Most roles are limited to certain states.\n\n"
              "⚠️ Apply ONLY on official careers sites (amazon.jobs, jobs.apple.com, etc.). Fake recruiters copy these brands."),
     hashtags=["#workfromhome", "#remotejobs", "#customerservice", "#hiring", "#entryleveljobs"],
     sources=["https://www.lilachbullock.com/amazon-remote-jobs-real-work-from-home-roles/", "https://tech.co/news/fully-remote-jobs-at-apple",
              "https://joingerald.com/learn/work--income/customer-service-true-work-from-home-jobs"])

post(id="2026-10-31-tt", date="2026-10-31", time_et="19:00", channel="tiktok", format="video",
     pillar="jobs", topic="Remote jobs with a W-2 that hire beginners", opportunity_ids=[],
     hook="Want a remote job with an actual paycheck and benefits? Start here.",
     scenes=[
         {"text": "Remote job + real paycheck?", "vo": "Want a remote job with an actual paycheck, not gig work? Start here.", "secs": 3.5},
         {"text": "Apple At Home Advisor", "vo": "Apple hires At Home Advisors. A College Program listing was reported at about twenty-eight to thirty-two dollars an hour.", "secs": 5.5},
         {"text": "Amazon Virtual CS", "vo": "Amazon hires virtual customer service by state. Reported pay is around fifteen to nineteen an hour.", "secs": 5},
         {"text": "Concentrix · TTEC", "vo": "Concentrix and TTEC hire remote support reps too, often with no degree required.", "secs": 4.5},
         {"text": "W-2 = taxes withheld\n+ benefits", "vo": "These are W-2 jobs. Taxes withheld, minimum wage protections, often benefits.", "secs": 4.5},
         {"text": "⚠️ Official sites only", "vo": "Apply only on their official careers sites. Never through a text or WhatsApp link.", "secs": 4},
         {"text": "Follow for more\nverified jobs", "vo": "Follow for more verified remote jobs.", "secs": 3},
     ],
     caption="Remote W-2 support jobs that hire beginners. Pay varies by state; check the live posting. #workfromhome #remotejobs #customerservice #entryleveljobs",
     sources=["https://tech.co/news/fully-remote-jobs-at-apple", "https://www.lilachbullock.com/amazon-remote-jobs-real-work-from-home-roles/",
              "https://joingerald.com/learn/work--income/customer-service-true-work-from-home-jobs"])

post(id="2026-10-31-th1", date="2026-10-31", time_et="10:00", channel="threads", format="text", pillar="jobs",
     topic="W-2 vs 1099", opportunity_ids=["OD044"],
     text=("Before you take a \"work from home\" call-center gig, check one thing: W-2 or 1099?\n\n"
           "Some contractor models charge you up front. Liveops, for example, says agents pay a $25 background check, certification is unpaid, "
           "and some programs pay 25–34¢ per talk minute.\n\nDo the math on your real hourly rate first."),
     sources=["https://join.liveops.com/faqs"])

# ============================================================ DAY 6 · Sun Nov 1 · PREP
post(id="2026-11-01-ig", date="2026-11-01", time_et="12:00", channel="instagram", format="carousel",
     pillar="prep", topic="Rewrite your resume with AI in 45 minutes, honestly", opportunity_ids=[],
     slides=[
         {"type": "cover", "kicker": "RESUME WORKFLOW", "title": "Tailor your resume with AI in 45 min (without lying)",
          "sub": "Works with free ChatGPT, Claude or Gemini."},
         {"type": "tip", "n": 1, "title": "Decode the job (5 min)", "body": "Paste the full posting. Ask the AI for the 5 must-haves and the 12 exact keywords recruiters search for."},
         {"type": "tip", "n": 2, "title": "Fit check (5 min)", "body": "Ask it to compare your resume to each must-have and score fit 1–10. Below 6? Skip, or get a referral first."},
         {"type": "tip", "n": 3, "title": "Tailor with rules (15 min)", "body": "Tell it: use ONLY my facts, never invent numbers, and write [ADD METRIC?] where one is missing."},
         {"type": "before", "title": "Before → After", "before": "Responsible for helping customers", "after": "Resolved 40–60 customer issues per shift, including returns and escalations, in a high-volume store",
          "note": "Illustrative example. Use your own real numbers."},
         {"type": "tip", "n": 4, "title": "Test the PDF (5 min)", "body": "Open it, select all, paste into a plain-text editor. If the text comes out scrambled, remove columns and tables."},
         {"type": "cta", "title": "Get all 21 prompts", "body": "Copy-paste resume, LinkedIn, proposal and interview prompts are in the US Remote Job Playbook.", "action": f"{LINK_CTA} · Save this"},
     ],
     caption=("AI can tailor your resume in minutes, but only if you give it rules.\n\n"
              "The 45-minute workflow:\n1️⃣ Decode the job: must-haves + exact keywords\n2️⃣ Fit check: score 1–10, skip below 6\n"
              "3️⃣ Tailor with rules: \"Use only my facts. Never invent numbers.\"\n4️⃣ Test the PDF: copy-paste it into a text editor\n\n"
              "Golden rule: if you can't explain a line in an interview, delete it.\n\nSave this for your next application 📌"),
     hashtags=["#resumetips", "#jobsearch", "#chatgpt", "#careertips", "#newgrad"],
     sources=["https://atsverification.com/blog/ats-resume-myths-debunked/"])

post(id="2026-11-01-tt", date="2026-11-01", time_et="19:00", channel="tiktok", format="video",
     pillar="prep", topic="Fix a boring resume bullet", opportunity_ids=[],
     hook="Recruiters skip this resume line. Here's the fix.",
     scenes=[
         {"text": "Recruiters skip this line", "vo": "Recruiters skim right past this resume line. Here's the fix.", "secs": 3.5},
         {"text": "❌ \"Responsible for\nhelping customers\"", "vo": "Responsible for helping customers. It says nothing about what you did.", "secs": 4.5},
         {"text": "Ask: how many?\nwhat tools? what result?", "vo": "Ask yourself three things: how many, what tools, and what changed because of you.", "secs": 5},
         {"text": "✅ \"Resolved 40–60 customer\nissues per shift...\"", "vo": "Now it reads: resolved forty to sixty customer issues per shift, including returns and escalations.", "secs": 5.5},
         {"text": "AI rule: never invent", "vo": "If you use AI to rewrite it, tell it: use only my facts and never invent numbers.", "secs": 4.5},
         {"text": "Example only.\nUse YOUR numbers.", "vo": "That example is illustrative. Use your own real numbers.", "secs": 3.5},
         {"text": "Follow for more\nresume fixes", "vo": "Follow for more resume fixes.", "secs": 3},
     ],
     caption="One resume line, fixed. Numbers + tools + result. Never invent facts. #resumetips #jobsearch #careertips #newgrad",
     sources=[])

post(id="2026-11-01-th1", date="2026-11-01", time_et="11:00", channel="threads", format="text", pillar="prep",
     topic="ATS myth", opportunity_ids=[],
     text=("Unpopular opinion: the \"75% of resumes get auto-rejected by ATS\" stat gets repeated way more than it's backed up.\n\n"
           "Most ATS systems parse your resume and let recruiters search keywords. The real killers are tables, columns, and contact info stuck in the header.\n\n"
           "Simple single-column resume > fancy template."),
     sources=["https://atsverification.com/blog/ats-resume-myths-debunked/", "https://resumegenius.com/blog/applicant-tracking-systems-resume-keyword-help"])

# ============================================================ DAY 7 · Mon Nov 2 · PROMO + scams insight
post(id="2026-11-02-ig", date="2026-11-02", time_et="12:00", channel="instagram", format="carousel",
     pillar="promo", topic="Inside the US Remote Job Playbook", opportunity_ids=[],
     slides=[
         {"type": "cover", "kicker": "NEXT OFFER ACADEMY GUIDE", "title": "The US Remote Job Playbook",
          "sub": "Where to apply, how to get accepted, and how to start earning. No hype."},
         {"type": "stat", "big": "71", "title": "Opportunities with direct links", "body": "AI training, freelance marketplaces and remote employers, each labeled Apply Now, Explore, Caution or Unavailable."},
         {"type": "stat", "big": "51", "title": "Documented worker outcomes", "body": "What real workers reported: acceptances, payments, rate cuts, silences. Every one is sourced."},
         {"type": "stat", "big": "21", "title": "Copy-paste AI prompts", "body": "Resume tailoring, LinkedIn, proposals, pricing and an AI interview simulator."},
         {"type": "stat", "big": "7 + 30", "title": "Day action plans", "body": "An urgent-income track and a stable-job track, with printable trackers."},
         {"type": "tip", "n": "✓", "title": "What it won't do", "body": "Promise you a job or an income. It gives you verified places to apply and a plan to follow."},
         {"type": "cta", "title": "Get the playbook", "body": "Start applying in your first reading session.", "action": f"{LINK_CTA} · nextofferacademy"},
     ],
     caption=("We built the guide we wish existed for US job seekers chasing legit remote work. 📘\n\n"
              "Inside the US Remote Job Playbook:\n• 71 opportunities with direct links and status labels\n• 51 documented worker outcomes\n"
              "• 21 copy-paste AI career prompts\n• 7-day and 30-day action plans\n\nNo promises of jobs or income. Just verified places to apply and a plan.\n\n"
              "👉 Link in bio"),
     hashtags=["#remotejobs", "#jobsearch", "#careerguide", "#layoffs", "#newgrad"],
     sources=["us/OPPORTUNITY_DIRECTORY.csv", "us/WORKER_SUCCESS_RESEARCH.csv", "us/AI_CAREER_PROMPTS.md"])

post(id="2026-11-02-tt", date="2026-11-02", time_et="19:00", channel="tiktok", format="video",
     pillar="experience", topic="Remote job scam red flags (FTC data)", opportunity_ids=[],
     hook="Remote job scams quadrupled. Here's how to spot one in 10 seconds.",
     scenes=[
         {"text": "Spot a job scam\nin 10 seconds", "vo": "Remote job scams are exploding. Here's how to spot one in ten seconds.", "secs": 3.5},
         {"text": "~5,000 → ~20,000", "vo": "The FTC says task scam reports went from about five thousand in all of 2023 to about twenty thousand in just the first half of 2024.", "secs": 6},
         {"text": "$220M+ lost", "vo": "Job scam losses topped two hundred twenty million dollars in those six months.", "secs": 4},
         {"text": "🚩 You have to pay", "vo": "Red flag one: you have to pay. For training, equipment, or to unlock earnings.", "secs": 4.5},
         {"text": "🚩 WhatsApp / Telegram", "vo": "Red flag two: a recruiter texts you out of nowhere and moves you to WhatsApp or Telegram.", "secs": 4.5},
         {"text": "🚩 Chat-only interview", "vo": "Red flag three: a chat-only interview with an instant offer.", "secs": 3.5},
         {"text": "Legit jobs pay YOU", "vo": "Remember: legit jobs pay you. You never pay them.", "secs": 3.5},
         {"text": "Report: ReportFraud.ftc.gov", "vo": "Report scams at report fraud dot f-t-c dot gov. Follow for safe, verified jobs.", "secs": 4},
     ],
     caption="Task scams surged per FTC data (Dec 2024 report). Legit jobs never make you pay. Report at ReportFraud.ftc.gov #jobscams #remotejobs #workfromhome #scamalert",
     sources=["https://ftc.gov/news-events/news/press-releases/2024/12/new-ftc-data-show-skyrocketing-consumer-reports-about-game-online-job-scams"])

post(id="2026-11-02-th1", date="2026-11-02", time_et="09:00", channel="threads", format="text", pillar="promo",
     topic="Playbook announcement", opportunity_ids=[],
     text=("We put together a US Remote Job Playbook: 71 remote opportunities with direct links, each labeled Apply Now, Explore, Caution or Unavailable, "
           "plus 21 AI prompts and 7- and 30-day plans.\n\nNo income promises. Just verified places to apply.\n\nLink's in our bio if it helps."),
     sources=["us/OPPORTUNITY_DIRECTORY.csv"])

post(id="2026-11-02-th2", date="2026-11-02", time_et="17:00", channel="threads", format="text", pillar="experience",
     topic="Remote competition data", opportunity_ids=["OD059"],
     text=("Why remote jobs feel impossible to land: LinkedIn data showed remote roles were 8.4% of postings but drew 42% of applications.\n\n"
           "That's why applying in the first 24–48 hours and messaging someone on the team matters so much more for remote roles."),
     sources=["https://www.sherwood.news/business/22-of-job-posts-on-linked-on-linkedin-are-hybrid-or-remote-work"])
