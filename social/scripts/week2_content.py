# -*- coding: utf-8 -*-
"""Week 2 (Oct 28 - Nov 3, 2026): trend-informed rework of Instagram + TikTok content.

Each topic has:
  - Variation A: a ready-to-post vertical video rendered by render2.py (TikTok + Instagram Reel)
  - Variation B: a film-yourself script (talking head / green screen) with a different hook
Instagram alternates Reels (Variation A video) and lo-fi "notes" carousels.
All facts come from sources researched Oct 22-27, 2026 (see sources per topic).
Audio: business accounts are limited to TikTok's Commercial Music Library / Meta Sound
Collection, so we suggest mood + where to find it, never a specific "trending" song.
"""

CHECKED = "Oct 27"
HANDLE = "@nextofferacademyus"

AUDIO = {
    "upbeat": "Upbeat, light lo-fi/pop instrumental, ~100-120 BPM, low volume under text. TikTok: Add sound > Commercial sounds > Trending. Instagram: Audio > browse tracks available to your account (Meta Sound Collection). Or use your own voiceover (always allowed).",
    "suspense": "Tense/mystery build that 'drops' on the reveal scene, ~90-110 BPM. TikTok: Commercial sounds > search 'suspense' or 'investigation'. Instagram: Audio > search 'suspense'. Or voiceover reading the on-screen lines.",
    "calm": "Calm, minimal piano or soft lo-fi, low volume so text is the focus. Pick from Commercial sounds (TikTok) / Meta Sound Collection (Instagram), or voiceover.",
    "punchy": "Punchy beat with clear hits for each cut (~120-130 BPM). TikTok Commercial sounds > Trending; Instagram audio picker. Cut on the beat in the app editor.",
}

TOPICS = [
    # ---------------------------------------------------------------- 1
    dict(
        key="myth-check", date="2026-10-28", pillar="jobs", ig_format="reel",
        topic="We fact-checked 3 viral remote job posts",
        reference_ids=["R3", "R4", "R1"],
        keywords=["remote jobs", "work from home jobs", "no degree jobs", "legit remote jobs", "job scams"],
        audio=AUDIO["suspense"],
        hook_a="This viral remote job post said $24–30 an hour. We checked.",
        scenes=[
            {"kind": "hook", "text": "Viral remote job posts 👀\nWe checked the pay.", "vo": "We fact-checked three viral remote job posts. Here's what was actually true.", "secs": 3},
            {"kind": "claim", "claim": "Part-time remote customer ops: $22/hr", "found": "Closest posting: temporary bilingual role, $20–21/hr", "vo": "Post one said twenty-two an hour. The closest real posting: a temporary bilingual role at twenty to twenty-one.", "secs": 4},
            {"kind": "claim", "claim": "Remote claims processor: $24–30/hr", "found": "Real listing, but no pay shown. The $24–30 was a different job.", "vo": "Post two: a real claims processor listing, but no pay shown. That range belonged to a different job.", "secs": 4},
            {"kind": "claim", "claim": "Care management associate: up to $42.35/hr", "found": "Listings show $18.50–35.29/hr", "vo": "Post three said up to forty-two. The listings we found top out at thirty-five twenty-nine.", "secs": 4},
            {"kind": "list", "text": "Before you apply:\n✅ Find it on the company's careers page\n✅ Check the pay there", "vo": "Before you apply, find the job on the company's own careers page and check the pay there.", "secs": 3.5},
            {"kind": "cta", "text": "Follow for remote jobs\nwe actually check", "vo": "Follow for remote jobs we actually check.", "secs": 2.5},
        ],
        tiktok_caption="Job-lead posts are great, but check the pay at the source 👀 We looked these up on Oct 27. Which one surprised you? #remotejobs #workfromhome #jobsearch #legitjobs",
        ig_caption=("We fact-checked 3 viral remote job posts 👀\n\n"
                    "1. \"$22/hr part-time remote customer ops\" → closest posting we found: temporary bilingual role, $20–21/hr\n"
                    "2. \"$24–30/hr remote claims processor\" → real listing, no pay shown (that range was a different job)\n"
                    "3. \"Up to $42.35/hr care management associate\" → listings show $18.50–35.29/hr\n\n"
                    "Job-lead posts are useful. Just verify on the employer's careers page before you apply.\n\n"
                    "Want us to check a job post you saw? Drop it in the comments 👇"),
        ig_hashtags=["#remotejobs", "#workfromhomejobs", "#jobsearch", "#legitjobs"],
        cta="Comment a job post you want us to check",
        app_links=["https://www.talentify.io/job/temp-customer-operations-specialist-spanishmandarin-us-remote-jobs-r15312",
                   "https://www.wayup.com/i-j-Claims-Processor-Marpai-Administrators-LLC-983939163668275/",
                   "https://remotive.com/remote/jobs/customer-service/care-management-associate-4401171"],
        sources=["https://www.talentify.io/job/temp-customer-operations-specialist-spanishmandarin-us-remote-jobs-r15312",
                 "https://www.wayup.com/i-j-Claims-Processor-Marpai-Administrators-LLC-983939163668275/",
                 "https://remotive.com/remote/jobs/customer-service/care-management-associate-4401171",
                 "https://ratracerebellion.com/cvs-is-hiring-remote-care-management-associate-18-50-35-29-hr"],
        variation_b=dict(
            hook="Stop applying to remote jobs from TikTok posts until you do this one thing.",
            format="Green screen (owner on camera, job-check card behind)",
            script=["[Green screen: card 'VIRAL POST SAID $24–30/hr'] Stop applying to remote jobs from TikTok posts until you do this.",
                    "I looked up three viral job posts today. Two had the pay wrong.",
                    "[Point at card 2] This one: real listing, but no pay posted. The pay in the video belonged to a different job.",
                    "So: open the company's careers page, search the job title, read the pay there.",
                    "Want me to check one for you? Comment the company name."],
            shots="3 cuts max. Phone at eye level, window light. Use tiktok_frames/scene_02–04.png as green-screen backgrounds.",
        ),
    ),
    # ---------------------------------------------------------------- 2
    dict(
        key="ai-pay", date="2026-10-29", pillar="jobs", ig_format="carousel",
        topic="What AI training actually pays (with the catch)",
        reference_ids=["R4", "R9"],
        keywords=["AI training jobs", "data annotation", "side hustle", "work from home", "Outlier", "Handshake AI"],
        audio=AUDIO["upbeat"],
        hook_a="AI training pays real money. Here's the part nobody posts.",
        scenes=[
            {"kind": "hook", "text": "AI training jobs pay.\nHere's what nobody posts 👇", "vo": "AI training pays real money. Here's the part nobody posts.", "secs": 3},
            {"kind": "card", "company": "DataAnnotation", "role": "Write & rate chatbot answers", "pay": "~$20+/hr reported", "note": "1 unpaid test. No retakes.", "vo": "DataAnnotation: around twenty an hour reported. But one unpaid test, no retakes.", "secs": 3.5},
            {"kind": "card", "company": "Prolific", "role": "Paid research studies", "pay": "$8/hr minimum rule", "note": "Waitlist possible", "vo": "Prolific: studies must pay at least eight an hour. You might get waitlisted.", "secs": 3.5},
            {"kind": "card", "company": "Handshake AI Fellowship", "role": "US grad students & grads", "pay": "Up to $125/hr listed", "note": "No guaranteed project", "vo": "Handshake's AI Fellowship lists up to one twenty-five for grad students. No project is guaranteed.", "secs": 3.5},
            {"kind": "claim", "claim": "\"$50/hr every week\"", "found": "One Outlier worker's rate dropped to $15/hr (Business Insider)", "vo": "And rates change. Business Insider reported one worker going from fifty to fifteen an hour.", "secs": 4},
            {"kind": "cta", "text": "Apply to 3, not 1.\nFollow for verified gigs", "vo": "Apply to three, not one. Follow for verified gigs.", "secs": 2.5},
        ],
        tiktok_caption="AI training is real money and real inconsistency. Pay as listed/reported, checked Oct 22–27. #aitraining #sidehustle #workfromhome #remotejobs",
        slides=[
            {"type": "cover", "title": "What AI training actually pays", "sub": "The number, and the catch nobody posts. Checked Oct 27."},
            {"type": "row", "title": "DataAnnotation", "pay": "~$20+/hr reported", "good": "Write & rate chatbot answers", "catch": "One ~1-hr unpaid test, no retakes, may never hear back"},
            {"type": "row", "title": "Prolific", "pay": "$8/hr minimum rule ($12 recommended)", "good": "Paid research studies, US supported", "catch": "Waitlist; small amounts"},
            {"type": "row", "title": "Handshake AI Fellowship", "pay": "Up to $125/hr listed", "good": "US grad students & recent grads, any field", "catch": "Rolling review, no guaranteed project"},
            {"type": "row", "title": "Outlier", "pay": "Generalist up to ~$15/hr listed", "good": "Lots of task types", "catch": "Empty queues; one worker's rate fell $50 → $15/hr (Business Insider)"},
            {"type": "end", "title": "The honest takeaway", "sub": "Treat it as income stacking, not a salary. Never pay to join. Apply to 3."},
        ],
        ig_caption=("What AI training actually pays, and the part people leave out 👇\n\n"
                    "• DataAnnotation: ~$20+/hr reported (one unpaid test, no retakes)\n"
                    "• Prolific: $8/hr minimum rule\n"
                    "• Handshake AI Fellowship: up to $125/hr listed for US grad students\n"
                    "• Outlier: generalist up to ~$15/hr listed; rates can change fast\n\n"
                    "Real money, uneven work. Stack a few, keep job searching.\n\nSave this before you sign up 📌"),
        ig_hashtags=["#aitraining", "#sidehustle", "#remotejobs", "#workfromhome"],
        cta="Save before you sign up",
        app_links=["https://www.dataannotation.tech", "https://www.prolific.com/participants", "https://joinhandshake.com/fellowship-program", "https://outlier.ai/experts/all"],
        sources=["https://www.secondtalent.com/resources/is-dataannotation-legit/",
                 "https://researcher-help.prolific.com/en/articles/445266-how-much-should-i-pay-participants",
                 "https://support.joinhandshake.com/hc/en-us/articles/32264709473303-MOVE-Program-Overview-FAQs-for-EDU-Partners",
                 "https://aitrainer.work/guides/handshake-ai-fellowship-guide",
                 "https://tech.yahoo.com/ai/articles/inside-lucrative-surreal-disturbing-world-081101391.html",
                 "https://theairankings.com/ai-jobs/outlier-review/"],
        variation_b=dict(
            hook="Everyone's posting AI training income. Nobody's posting the dry spells.",
            format="Talking head + text labels",
            script=["Everyone's posting AI training income. Nobody's posting the dry spells.",
                    "Yes, it pays. DataAnnotation is reported around twenty an hour to start. Handshake's fellowship lists up to one twenty-five for grad students.",
                    "But: the DataAnnotation test is one shot. Outlier workers talk about empty queues. And Business Insider reported a worker whose rate dropped from fifty to fifteen.",
                    "So apply to three platforms, not one, and keep your job search running.",
                    "Never pay to join any of them."],
            shots="Seated, one take or 2 jump cuts. Add on-screen labels with the numbers in the app.",
        ),
    ),
    # ---------------------------------------------------------------- 3
    dict(
        key="resume-fixes", date="2026-10-30", pillar="prep", ig_format="reel",
        topic="3 resume fixes in 20 seconds",
        reference_ids=["R5"],
        keywords=["resume tips", "resume mistakes", "ATS resume", "job search tips", "new grad resume"],
        audio=AUDIO["punchy"],
        hook_a="3 resume mistakes you can fix before your next application.",
        scenes=[
            {"kind": "hook", "text": "3 resume fixes\nin 20 seconds ⏱️", "vo": "Three resume fixes you can make before your next application.", "secs": 2.5},
            {"kind": "fix", "bad": "resume_final_v3.pdf", "good": "Jordan-Lee-Resume.pdf", "vo": "One. Name the file with your name, not resume final version three.", "secs": 3},
            {"kind": "fix", "bad": "Contact info in the page header", "good": "Contact info in the body, first line", "vo": "Two. Put your contact info in the body. Some systems misread headers.", "secs": 3.5},
            {"kind": "fix", "bad": "Responsible for helping customers", "good": "Resolved 40–60 customer issues per shift", "vo": "Three. Swap duties for numbers. This one's an example, use your real ones.", "secs": 4},
            {"kind": "list", "text": "Never invent numbers.\nIf you can't explain it,\ndelete it.", "vo": "And never invent numbers. If you can't explain it in an interview, delete it.", "secs": 3},
            {"kind": "cta", "text": "Follow for job search\nhelp that's actually useful", "vo": "Follow for more.", "secs": 2},
        ],
        tiktok_caption="Small fixes, big difference. The bullet example is illustrative; use your real numbers. #resumetips #jobsearch #careertips #newgrad",
        ig_caption=("3 resume fixes you can make in 20 seconds:\n\n"
                    "1️⃣ File name: Firstname-Lastname-Resume.pdf\n"
                    "2️⃣ Contact info in the body, not the page header (some systems misread headers)\n"
                    "3️⃣ Duties → numbers (\"Resolved 40–60 issues per shift\". Example only; use your real numbers)\n\n"
                    "Rule: if you can't explain a line in an interview, delete it.\n\nWhich one are you fixing first?"),
        ig_hashtags=["#resumetips", "#jobsearch", "#careertips", "#newgrad"],
        cta="Comment which fix you're making",
        app_links=[],
        sources=["https://atsverification.com/blog/ats-resume-myths-debunked/", "https://resumegenius.com/blog/applicant-tracking-systems-resume-keyword-help"],
        variation_b=dict(
            hook="Your resume file name might be the first thing a recruiter judges.",
            format="Screen recording of your own (anonymized) resume + voiceover",
            script=["Your resume file name might be the first thing a recruiter sees.",
                    "[Screen: rename file] Rename it: your name, dash, resume.",
                    "[Screen: move contact line from header to body] Contact info goes in the body. Some systems misread headers.",
                    "[Screen: rewrite one bullet] Swap a duty for a number you can actually back up.",
                    "That's it. Three minutes."],
            shots="Screen-record on your laptop (blur personal details), voiceover in the app.",
        ),
    ),
    # ---------------------------------------------------------------- 4
    dict(
        key="real-vs-fake", date="2026-10-31", pillar="experience", ig_format="carousel",
        topic="Real vs fake work-from-home job post",
        reference_ids=["R3"],
        keywords=["job scams", "fake job posts", "work from home scam", "remote jobs", "legit remote jobs"],
        audio=AUDIO["suspense"],
        hook_a="If a 'recruiter' asks you to do this, it's a scam.",
        scenes=[
            {"kind": "hook", "text": "Real or fake\nWFH job post? 🚩", "vo": "Real or fake work-from-home job post? Here's how to tell in ten seconds.", "secs": 3},
            {"kind": "fix", "bad": "Phone number + 'DM me' in the caption", "good": "Listed on the company's careers page", "vo": "Fake: a phone number and DM me. Real: it's on the company's careers page.", "secs": 4},
            {"kind": "fix", "bad": "Pay to start / buy equipment", "good": "They pay you. You never pay them.", "vo": "Fake: you pay for training or equipment. Real jobs pay you.", "secs": 3.5},
            {"kind": "fix", "bad": "Moves you to WhatsApp or Telegram", "good": "Email from the company domain", "vo": "Fake: they move you to WhatsApp or Telegram.", "secs": 3},
            {"kind": "stat", "big": "~20,000", "text": "task-scam reports to the FTC in the first half of 2024 alone", "vo": "The FTC got about twenty thousand task-scam reports in just the first half of 2024.", "secs": 4},
            {"kind": "cta", "text": "Send this to someone\njob hunting right now", "vo": "Send this to someone job hunting right now.", "secs": 2.5},
        ],
        tiktok_caption="Same keywords, very different posts. Report scams at ReportFraud.ftc.gov. #jobscams #remotejobs #workfromhome #scamalert",
        slides=[
            {"type": "cover", "title": "Real vs fake WFH job post 🚩", "sub": "Scam posts use the same keywords as real ones. Here's the difference."},
            {"type": "vs", "title": "Where it lives", "bad": "Caption with a phone number + \"DM me\"", "good": "Listed on the company's own careers page"},
            {"type": "vs", "title": "Money", "bad": "Pay for training, equipment, or to \"unlock\" earnings", "good": "They pay you. You never pay them."},
            {"type": "vs", "title": "Contact", "bad": "Moves you to WhatsApp/Telegram, chat-only interview", "good": "Company email domain, real interview"},
            {"type": "stat", "big": "$220M+", "title": "lost to job scams in H1 2024", "sub": "FTC: task-scam reports went from ~5,000 (all of 2023) to ~20,000 (first half of 2024)."},
            {"type": "end", "title": "Report it", "sub": "ReportFraud.ftc.gov · Send this to someone job hunting."},
        ],
        ig_caption=("Real vs fake work-from-home job posts 🚩\n\n"
                    "🚩 Phone number + \"DM me\" in the caption\n🚩 You pay for training/equipment\n🚩 Moved to WhatsApp/Telegram, chat-only interview\n\n"
                    "✅ Listed on the company's careers page\n✅ They pay you, never the other way around\n✅ Company email + real interview\n\n"
                    "FTC: ~20,000 task-scam reports in the first half of 2024, $220M+ lost to job scams in those six months.\n\n"
                    "Send this to someone who's job hunting 💛"),
        ig_hashtags=["#jobscams", "#remotejobs", "#workfromhome", "#jobsearch"],
        cta="Share with someone job hunting",
        app_links=["https://reportfraud.ftc.gov"],
        sources=["https://ftc.gov/news-events/news/press-releases/2024/12/new-ftc-data-show-skyrocketing-consumer-reports-about-game-online-job-scams"],
        variation_b=dict(
            hook="I'm not saying every 'no experience' remote job post is a scam. But this one is.",
            format="Green screen over the 'real vs fake' card (no real scammer screenshots or usernames)",
            script=["Not every 'no experience' remote job post is a scam. But here's how to spot the ones that are.",
                    "Red flag one: the caption has a phone number and says DM me. Real jobs live on the company's careers page.",
                    "Red flag two: you have to pay for anything. Training, equipment, a deposit. No.",
                    "Red flag three: they move you to WhatsApp or Telegram.",
                    "The FTC got about twenty thousand task-scam reports in the first half of 2024. Report them at ReportFraud dot FTC dot gov."],
            shots="Use the carousel slides as green-screen backgrounds. Never show a real person's username or number.",
        ),
    ),
    # ---------------------------------------------------------------- 5
    dict(
        key="application-math", date="2026-11-01", pillar="experience", ig_format="reel",
        topic="152 applications, 6 interviews: what the numbers say",
        reference_ids=["R10", "R8"],
        keywords=["job search", "laid off", "job applications", "ghosted", "remote jobs", "referrals"],
        audio=AUDIO["calm"],
        hook_a="152 applications. 6 interviews. Here's what that data says.",
        scenes=[
            {"kind": "hook", "text": "152 applications.\n6 interviews.", "vo": "A laid-off developer tracked every application. One hundred fifty-two applications. Six interviews.", "secs": 3.5},
            {"kind": "stat", "big": "101", "text": "of those applications were ghosted", "vo": "One hundred and one were ghosted.", "secs": 3},
            {"kind": "stat", "big": "68.5 days", "text": "median time to a first offer (461K tracked applications, Q2 2025)", "vo": "Across almost half a million tracked applications, the median time to a first offer was sixty-eight days.", "secs": 4},
            {"kind": "stat", "big": "8% → 42%", "text": "remote jobs: ~8% of LinkedIn postings, 42% of applications", "vo": "Remote jobs are about eight percent of LinkedIn postings, but get forty-two percent of applications.", "secs": 4},
            {"kind": "list", "text": "So: apply in the first 48h\n+ message someone on the team", "vo": "So apply in the first forty-eight hours, and message someone on the team.", "secs": 3.5},
            {"kind": "cta", "text": "It's not just you.\nFollow for what works", "vo": "It's not just you. Follow for what actually works.", "secs": 2.5},
        ],
        tiktok_caption="If your job search feels slow, the data agrees. Sources: a developer's public 2025 job-search log, Huntr Q2 2025, LinkedIn data via Sherwood. #jobsearch #laidoff #remotejobs #jobhunting",
        ig_caption=("If your job search feels impossible, it's not just you.\n\n"
                    "📊 A laid-off developer's public log: 152 applications → 6 interviews, 101 ghosted\n"
                    "📊 Median time to a first offer: 68.5 days (461K tracked applications, Q2 2025)\n"
                    "📊 Remote roles: ~8% of LinkedIn postings, 42% of applications\n\n"
                    "What tends to work better: apply in the first 48 hours, then message someone on the team.\n\n"
                    "How many applications are you at? No judgment 👇"),
        ig_hashtags=["#jobsearch", "#laidoff", "#remotejobs", "#jobhunting"],
        cta="Comment your application count",
        app_links=[],
        sources=["https://www.twistermc.com/50442/2025-job-search-reality-check/", "https://huntr.co/blog/job-search-tips",
                 "https://www.sherwood.news/business/22-of-job-posts-on-linked-on-linkedin-are-hybrid-or-remote-work"],
        variation_b=dict(
            hook="If you've sent 100+ applications and heard nothing, watch this.",
            format="Talking head, calm tone, numbers as on-screen text",
            script=["If you've sent a hundred applications and heard nothing, this isn't a you problem.",
                    "One laid-off developer published his numbers: one fifty-two applications, six interviews, a hundred and one ghosted.",
                    "Across almost half a million tracked applications, the median time to a first offer was about sixty-eight days.",
                    "And remote jobs get way more applicants than their share of postings.",
                    "What actually moves the needle: apply early, and message one person on the team every time."],
            shots="Single take, natural light. Add the three numbers as text in the app.",
        ),
    ),
    # ---------------------------------------------------------------- 6
    dict(
        key="ai-interview", date="2026-11-02", pillar="prep", ig_format="carousel",
        topic="How to pass an AI video interview",
        reference_ids=["R5", "R9"],
        keywords=["AI interview", "Mercor", "video interview tips", "AI training jobs", "interview tips"],
        audio=AUDIO["upbeat"],
        hook_a="Your next interviewer might be an AI. Here's how it works.",
        scenes=[
            {"kind": "hook", "text": "Your next interviewer\nmight be an AI 🤖", "vo": "Your next interviewer might be an AI. Here's how it works.", "secs": 3},
            {"kind": "list", "text": "Mercor: ~20-minute\nAI video interview\nbased on YOUR resume", "vo": "Mercor's is about twenty minutes, and the questions come from your resume.", "secs": 3.5},
            {"kind": "list", "text": "✅ Free practice interview\n✅ Redo before you submit", "vo": "There's a free practice round, and you can redo it before you submit.", "secs": 3},
            {"kind": "list", "text": "Prep 3 projects:\nwhat you did · how · result", "vo": "Prep three projects: what you did, how, and the result.", "secs": 3.5},
            {"kind": "list", "text": "Look at the lens.\nQuiet room. Good light.", "vo": "Look at the lens, quiet room, light in front of you.", "secs": 3},
            {"kind": "cta", "text": "Follow for AI job prep\nthat isn't hype", "vo": "Follow for more.", "secs": 2},
        ],
        tiktok_caption="AI interviews ask about your own resume. Know every line. Process per Mercor's candidate docs. #aiinterview #interviewtips #remotejobs #aitraining",
        slides=[
            {"type": "cover", "title": "How to pass an AI video interview", "sub": "Mercor, Alignerr and micro1 use AI interviewers. Here's the playbook."},
            {"type": "note", "title": "What to expect", "items": ["~20 minutes (Mercor)", "Questions built from your resume", "Free practice round", "You can redo it before submitting"]},
            {"type": "note", "title": "Prep (30 minutes)", "items": ["Pick 3 projects from your resume", "For each: what you did, how, the result", "Say one number per answer", "Know every line on your resume"]},
            {"type": "note", "title": "Setup", "items": ["Camera at eye level, look at the lens", "Light in front of you", "Quiet room, wired or strong Wi-Fi", "Pause 2 seconds before answering"]},
            {"type": "note", "title": "Don't", "items": ["Read a script", "Use AI tools during the interview", "Ramble past 2 minutes"]},
            {"type": "end", "title": "Practice free", "sub": "Google Interview Warmup + Mercor's practice round. Save this for interview day."},
        ],
        ig_caption=("Your next interviewer might be an AI 🤖\n\n"
                    "Mercor, Alignerr and micro1 all use AI interviewers. What we know:\n"
                    "• Mercor's runs ~20 minutes and asks about your own resume\n"
                    "• There's a free practice round, and you can redo it before submitting\n\n"
                    "Prep 3 projects (what you did, how, the result), look at the lens, and keep answers under 2 minutes.\n\nSave this for interview day 📌"),
        ig_hashtags=["#interviewtips", "#aiinterview", "#remotejobs", "#jobsearch"],
        cta="Save for interview day",
        app_links=["https://work.mercor.com"],
        sources=["https://talent.docs.mercor.com/how-to/prepare-for-ai-interview", "https://au.trustpilot.com/review/www.alignerr.com?page=8",
                 "https://jobs.micro1.ai/post/8f87173b-4f95-4fde-8df4-9cfd4a6c337f"],
        variation_b=dict(
            hook="I watched how AI interviewers work so you don't walk in blind.",
            format="Talking head with 'question cards' (owner reads 3 sample questions and answers one)",
            script=["Companies like Mercor now interview you with an AI. Here's what to know.",
                    "It's about twenty minutes and it asks about your own resume, so know every line.",
                    "There's a free practice round, and you can redo the interview before you submit.",
                    "Sample question: walk me through your biggest project. Answer: what you did, how, the result, in under two minutes.",
                    "Look at the lens, not your face."],
            shots="Note: 'I watched' is only OK if you did; otherwise use 'Here's how AI interviewers work.'",
        ),
    ),
    # ---------------------------------------------------------------- 7
    dict(
        key="new-grad", date="2026-11-03", pillar="jobs", ig_format="reel",
        topic="New grad? 3 places to look this week",
        reference_ids=["R1", "R6"],
        keywords=["new grad jobs", "entry level jobs", "college students", "Handshake", "startup jobs", "AI jobs"],
        audio=AUDIO["upbeat"],
        hook_a="New grad and getting nowhere on LinkedIn? Try these 3 instead.",
        scenes=[
            {"kind": "hook", "text": "New grad?\n3 places to look\nthat aren't LinkedIn", "vo": "New grad and getting nowhere on LinkedIn? Try these three.", "secs": 3},
            {"kind": "card", "company": "Handshake AI Fellowship", "role": "AI training for US grad students & recent grads", "pay": "Up to $125/hr listed", "note": "Rolling review", "vo": "One: Handshake's AI Fellowship. Up to one twenty-five an hour listed for grad students.", "secs": 4},
            {"kind": "card", "company": "YC Work at a Startup", "role": "One profile, startup founders reach out", "pay": "Salary shown per job", "note": "Can also apply directly", "vo": "Two: Y Combinator's Work at a Startup. One profile, and founders can reach out to you.", "secs": 4},
            {"kind": "card", "company": "Your school's Handshake", "role": "Internships, entry-level remote roles", "pay": "Varies", "note": "Alumni can often still log in", "vo": "Three: your school's Handshake. Alumni can often still use it.", "secs": 3.5},
            {"kind": "cta", "text": "Save this. Follow for\nentry-level leads", "vo": "Save this, and follow for entry-level leads.", "secs": 2.5},
        ],
        tiktok_caption="Three places new grads skip. Check eligibility on each site. #newgrad #entryleveljobs #collegestudent #jobsearch",
        ig_caption=("New grad and getting nowhere on LinkedIn? Try these 3:\n\n"
                    "1. Handshake AI Fellowship: AI training for US grad students & recent grads (up to $125/hr listed; no guaranteed project)\n"
                    "2. YC Work at a Startup: one profile, founders of YC-funded startups can reach out\n"
                    "3. Your school's Handshake: internships and entry-level roles (alumni can often still log in)\n\n"
                    "Links: joinhandshake.com · workatastartup.com\n\nTag a friend who just graduated 🎓"),
        ig_hashtags=["#newgrad", "#entryleveljobs", "#jobsearch", "#collegestudent"],
        cta="Tag a friend who just graduated",
        app_links=["https://joinhandshake.com/fellowship-program", "https://www.workatastartup.com", "https://joinhandshake.com"],
        sources=["https://support.joinhandshake.com/hc/en-us/articles/32264709473303-MOVE-Program-Overview-FAQs-for-EDU-Partners",
                 "https://aitrainer.work/guides/handshake-ai-fellowship-guide", "https://www.workatastartup.com/faq"],
        variation_b=dict(
            hook="If you graduated this year and you're only applying on LinkedIn, you're missing these.",
            format="Walk-and-talk or desk talking head",
            script=["If you graduated this year and only apply on LinkedIn, you're missing these.",
                    "Handshake's AI Fellowship pays grad students up to one twenty-five an hour listed for AI training work. Not guaranteed, but real.",
                    "Y Combinator's Work at a Startup: one profile, and startup founders can message you directly.",
                    "And your school's Handshake. A lot of alumni don't know they can still log in.",
                    "Save this and send it to your group chat."],
            shots="Natural, 3–4 cuts. Show each website on your phone screen (screen-record) between cuts.",
        ),
    ),
]
