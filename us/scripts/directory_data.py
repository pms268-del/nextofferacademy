# -*- coding: utf-8 -*-
"""Single source of truth for OPPORTUNITY_DIRECTORY.csv (US edition).

Every row is backed by source URLs found during research on 2026-10-22
(see us/research/00_RESEARCH_LOG_US.md). Pay is quoted as published by the
platform or as reported by the cited source; "Not published" means no
reliable figure was found. Do not add rows without a source.

Status labels
  Apply Now   - genuine, currently open application route for US residents AND
                credible evidence that past workers were accepted and paid.
  Explore     - real platform, but openings are listing-specific, invite-only,
                narrow, or worker-outcome evidence is thin. Check before investing time.
  Caution     - real company, but material risks: upfront costs, pay disputes,
                very low or unreliable volume, legal complaints, or limited remote access.
  Unavailable - not accepting US applicants / sign-ups closed as of verification.
"""

VERIFIED = "2026-10-22"

APPLY, EXPLORE, CAUTION, UNAVAILABLE = "Apply Now", "Explore", "Caution", "Unavailable"

CAT_A = "A. AI Training & AI Startups"
CAT_B = "B. Freelance & Project Marketplaces"
CAT_C = "C. Other Remote Jobs"

FIELDS = [
    "id", "platform", "category", "subcategory", "status", "website", "apply_link",
    "roles_and_tasks", "beginner_friendly", "requirements", "us_eligibility",
    "published_pay", "pay_source", "application_steps", "payment_and_fees",
    "worker_outcome_evidence", "evidence_strength", "common_challenges",
    "success_strategies", "verified_date", "verification_method", "sources",
]

ROWS = []


def add(**kw):
    kw.setdefault("verified_date", VERIFIED)
    kw.setdefault("verification_method", "Web search of official pages/listings + third-party reports, 2026-10-22")
    missing = [f for f in FIELDS if f not in kw and f != "id"]
    if missing:
        raise ValueError(f"{kw.get('platform')}: missing {missing}")
    ROWS.append(kw)


# =====================================================================  A
add(platform="Mercor", category=CAT_A, subcategory="Expert AI training marketplace", status=APPLY,
    website="https://mercor.com", apply_link="https://work.mercor.com",
    roles_and_tasks="Hourly contracts writing, grading and red-teaming AI outputs in a domain (law, finance, medicine, STEM, software, writing, audio, operations); some concierge/ops roles",
    beginner_friendly="Some (generalist and writing roles exist; best fit is proven domain experience)",
    requirements="Resume that clearly shows domain expertise; quiet room, webcam and mic for AI interview; some roles need degrees/licenses",
    us_eligibility="Yes (many listings US/UK/CA; check each listing)",
    published_pay="Listings seen: Expert Model Trainer $50–140/hr; Concierge AI Trainer (US) $65–75/hr; Training & Development Specialist $60–110/hr (US/UK/CA, min 15 h/wk). BI reported a follow-on project at $16/hr",
    pay_source="Official listings + aggregator copies + Business Insider",
    application_steps="Create profile and upload resume → ~20-min AI video interview based on your resume (practice interview available; retakes allowed before submitting) → role-specific assessment or form → sometimes human call → contract and onboarding",
    payment_and_fees="No application fee. Hourly contractors paid weekly via Stripe to a bank account in your own name (official docs). 1099 contractor: no tax withholding",
    worker_outcome_evidence="Indeed reviewers praise weekly pay; WSJ/BI report 30,000+ contractors hired in 2025; BI documented pay cut on follow-on project; Blind/Indeed report long silences after interview",
    evidence_strength="Strong",
    common_challenges="Ghosting after AI interview; projects end early; pay varies by project; time tracking; LLM use on tasks is prohibited and grounds for removal",
    success_strategies="Apply to the narrowest listing that matches your verifiable expertise; rehearse a 60-second walk-through of each resume project; take the practice interview; reuse a strong completed interview across listings",
    sources="https://work.mercor.com/jobs/list_AAABlRvLjyMZ_QjpNyhB6r5E/expert-model-trainer | https://remotive.com/remote/jobs/artificial-intelligence/concierge-ai-trainer-4499317 | https://talent.docs.mercor.com/how-to/payments | https://talent.docs.mercor.com/how-to/prepare-for-ai-interview | https://www.indeed.com/cmp/Mercor/reviews | https://www.aol.com/articles/ai-startup-powering-meta-openai-230627434.html")

add(platform="DataAnnotation", category=CAT_A, subcategory="AI training & RLHF (Surge AI crowd brand, reported)", status=APPLY,
    website="https://www.dataannotation.tech", apply_link="https://www.dataannotation.tech",
    roles_and_tasks="Write prompts, compare and rate chatbot answers, fact-check, coding evaluation, specialist (math, science, law) tracks",
    beginner_friendly="Yes (generalist track requires strong English writing and reasoning, no degree)",
    requirements="US/UK/CA/AU/NZ residency (reported); excellent written English; careful reasoning; coding track needs real coding skill",
    us_eligibility="Yes",
    published_pay="Generalist from ~$20+/hr; coding/specialist ~$40/hr and up (FAQ as quoted by multiple 2026 reviews; job board shows higher ranges for technical roles)",
    pay_source="Third-party reviews quoting official FAQ/job board",
    application_steps="Apply on site → one-time Starter Assessment (~1 hr, unpaid, no retake) → silent wait (days to ~4 weeks) → acceptance email → paid qualifications → projects appear on dashboard",
    payment_and_fees="No fee. PayPal; hourly work reportedly payable ~7 days after submission, per-task ~3 days (community FAQ)",
    worker_outcome_evidence="Indeed 4.1/5 (1,477 reviews, Jun 2026), Glassdoor 4.1/5; reviewers report prompt pay; others report no reply to assessment or sudden account closures; class action alleges misclassification (unproven)",
    evidence_strength="Strong",
    common_challenges="Single-shot assessment; no rejection notice; project dry spells; account closures without explanation",
    success_strategies="Take the assessment when rested; write complete, sourced, well-structured answers; never use AI to write answers; complete every qualification offered after acceptance",
    sources="https://www.secondtalent.com/resources/is-dataannotation-legit/ | https://annotation.academy/blog/is-dataannotation-tech-legit | https://www.indeed.com/cmp/DataAnnotation/reviews | https://ie.trustpilot.com/review/dataannotation.tech | https://getcoai.com/news/ai-data-labeling-startup-surge-ai-faces-unpaid-wages-lawsuit")

add(platform="Outlier (Scale AI)", category=CAT_A, subcategory="AI training & RLHF", status=APPLY,
    website="https://outlier.ai", apply_link="https://outlier.ai/experts/all",
    roles_and_tasks="Generalist writing/rating, domain expert tasks (STEM, medicine, law, coding), multilingual and audio projects",
    beginner_friendly="Yes for generalist projects (availability uneven)",
    requirements="Pass skill screening and ID verification; project-specific onboarding",
    us_eligibility="Yes",
    published_pay="Generalist listings advertise up to ~$15/hr; contributor-reported $12–30/hr standard work; expert pages advertise higher (e.g., up to $50/hr for some domains). Pay varies by verified country",
    pay_source="Official expert pages + third-party reviews",
    application_steps="Create account → choose expertise → skill screening (30–90 min general onboarding, unpaid) → identity verification → project onboarding and qualifiers (unpaid) → tasks",
    payment_and_fees="No fee. Weekly payments (processed Tuesdays) via PayPal, AirTM or ACH",
    worker_outcome_evidence="Glassdoor 3.2/5; 2026 reviews cite interesting tasks but sudden deactivation; BI documented generalist rate cut from $50 to $15/hr; 2024 payment thread reports weekly arrivals plus some delays",
    evidence_strength="Strong",
    common_challenges="Empty queue (no tasks) for days/weeks; unpaid onboarding; opaque quality flags; rate changes",
    success_strategies="Treat as supplemental; finish onboarding fast and accurately; read guidelines twice; match PayPal name/details to profile; join several platforms in parallel",
    sources="https://outlier.ai/blog/your-first-steps-on-outlier-what-to-expect-from-onboarding | https://outlier.ai/blog/your-guide-to-working-on-outlier | https://theairankings.com/ai-jobs/outlier-review/ | https://www.glassdoor.co.in/Reviews/Outlier-AI-Reviews-E2858115.htm | https://tech.yahoo.com/ai/articles/inside-lucrative-surreal-disturbing-world-081101391.html")

add(platform="Alignerr (Labelbox)", category=CAT_A, subcategory="Expert AI training", status=APPLY,
    website="https://www.alignerr.com", apply_link="https://job-boards.greenhouse.io/alignerr",
    roles_and_tasks="Domain-expert AI training (STEM, coding in many languages, writing), human preference ranking, code evaluation",
    beginner_friendly="Some (most listings want degrees or professional skill)",
    requirements="Resume + ID verification; AI interview with 'Zara' for many roles; domain assessment (often one attempt)",
    us_eligibility="Yes",
    published_pay="AI Trainer (PhD) $30–150/hr for US-based (official listing); homepage reportedly cites ~$80/hr average; listings vary widely",
    pay_source="Official Greenhouse listing + third-party review",
    application_steps="Apply to a listing → ID verification → Zara AI interview (resume-specific) → domain assessment → contract/onboarding → project invitations",
    payment_and_fees="No fee. Weekly or bi-weekly cycles reported; method depends on country",
    worker_outcome_evidence="Trustpilot 2026: positives on tailored AI interview and responsive leads; negatives on unpaid removal after ~6 hrs, disputed ~$1.3k, rate cuts",
    evidence_strength="Medium",
    common_challenges="Approval ≠ work; payment disputes reported; one-attempt assessments",
    success_strategies="Apply only where your degree/skill matches exactly; prepare concrete resume stories for Zara; log your hours and task IDs for any dispute",
    sources="https://job-boards.greenhouse.io/alignerr/jobs/4600287007 | https://nodemaven.com/blog/alignerr-review/ | https://labelbox.com/services/alignerr-connect/ | https://uk.trustpilot.com/review/www.alignerr.com?page=10 | https://au.trustpilot.com/review/www.alignerr.com?page=8")

add(platform="Handshake AI Fellowship (MOVE)", category=CAT_A, subcategory="AI training for students & graduates", status=APPLY,
    website="https://joinhandshake.com", apply_link="https://joinhandshake.com/fellowship-program",
    roles_and_tasks="Expert prompts, evaluation and reasoning tasks for frontier AI labs by academic field",
    beginner_friendly="Yes for current/recent graduate students (master's/PhD) in any field",
    requirements="US-based; master's/doctoral students, candidates or graduates; government ID verification; work authorization (visa rules: check current page)",
    us_eligibility="Yes",
    published_pay="$50–125/hr by education and expertise (official EDU-partner FAQ); individual listings e.g. $75–100/hr math",
    pay_source="Official FAQ + university career-office posting",
    application_steps="Sign up at fellowship page → upload resume, verify profile → government ID check → rolling review and matching → paid training exercise → project onboarding → tasking",
    payment_and_fees="No fee. Weekly payouts via Stripe (third-party tracker)",
    worker_outcome_evidence="Official pages describe paid onboarding and progression to reviewer roles; Rutgers AI Ethics Lab page documents a researcher working as a fellow; independent pay reports limited",
    evidence_strength="Medium",
    common_challenges="No guaranteed project; projects pause or end on short notice; removal if quality expectations not met",
    success_strategies="Ask your career office (many promote it); list thesis/research methods precisely; complete paid training exercise carefully",
    sources="https://support.joinhandshake.com/hc/en-us/articles/32244754462615-Apply-to-the-Handshake-AI-Fellowship | https://support.joinhandshake.com/hc/en-us/articles/32264709473303-MOVE-Program-Overview-FAQs-for-EDU-Partners | https://support.joinhandshake.com/hc/en-us/articles/38150760132119-Handshake-AI-Fellowship-expectations | https://gradcareers.cornell.edu/opportunities/put-ai-to-the-test-and-get-paid | https://aitrainer.work/guides/handshake-ai-fellowship-guide")

add(platform="micro1", category=CAT_A, subcategory="AI trainer marketplace + AI recruiter", status=APPLY,
    website="https://www.micro1.ai", apply_link="https://jobs.micro1.ai",
    roles_and_tasks="AI trainer & data annotator, software engineer AI trainer, domain experts, some full-time placements",
    beginner_friendly="Some (generalist annotator listings; college-student listings seen)",
    requirements="AI interview with 'Zara' (camera, mic, screen); government ID",
    us_eligibility="Yes (listing-specific)",
    published_pay="Official portal: AI Trainer & Data Annotator $20–98/hr; Software Engineer AI Trainer $30–80/hr; Indeed average ~$67/hr across 13 postings",
    pay_source="Official job portal + Indeed",
    application_steps="Browse opportunities portal → apply → Zara skill interview (30–60 min, reported no retakes) → ID verification → certified expert → contract offers",
    payment_and_fees="No fee. Contractor; some reviewers say only active time is paid",
    worker_outcome_evidence="Indeed 4.8/5 (130 reviews) praising flexibility; Glassdoor Mar 2026 reviewer got a low-rate generic contract despite high score",
    evidence_strength="Medium",
    common_challenges="Offered rate may be below listing max; project pauses",
    success_strategies="Apply to a specific listing (not just the general pool); answer interview questions with metrics; negotiate within the posted range",
    sources="https://jobs.micro1.ai/post/8f87173b-4f95-4fde-8df4-9cfd4a6c337f | https://jobs.micro1.ai/post/ce4dbaaf-d119-4f92-b12e-8354a98e4fbc | https://www.micro1.ai/experts-guide/complete-guide-to-ai-training-jobs | https://www.indeed.com/cmp/micro1/reviews | https://de.glassdoor.ch/Bewertungen/Bewertungen-Micro1-E7558526-RVW99002455.htm")

add(platform="TELUS Digital AI Community", category=CAT_A, subcategory="Search/ads/content rating, data collection", status=APPLY,
    website="https://www.telusdigital.com", apply_link="https://www.telusdigital.com/careers",
    roles_and_tasks="Content reviewer, search/map rater, data collection and annotation, AI response assessment",
    beginner_friendly="Yes",
    requirements="Reside in US; pass qualification exam/training; one person per household; own computer",
    us_eligibility="Yes",
    published_pay="Content Reviewer – United States: est. $14/hr ($0.2333 per task), open to Nov 27, 2026; earlier US Rater listing $12–14/hr",
    pay_source="Job-board copies of TELUS listings",
    application_steps="Apply to country/language listing → profile verification → unpaid qualification exam (study guidelines) → onboarding → part-time self-scheduled work",
    payment_and_fees="No fee — TELUS warns it never asks for deposits or 'Premium ID' fees. Independent contractor",
    worker_outcome_evidence="Long-running program with many public listings; worker accounts on review sites mixed on hours cap and exam difficulty",
    evidence_strength="Medium",
    common_challenges="Rigorous unpaid exam; weekly hour caps; task-based pay means $/hr depends on speed",
    success_strategies="Study the rater guidelines like a test; practice on sample items; keep a quiet distraction-free block; ignore any 'recruiter' who asks for money",
    sources="https://cazvid.com/en/job/content-reviewer-united-states-5cb55c | https://remotive.com/remote-jobs/all-others/content-reviewer-english-us-2091105 | https://www.workingnomads.com/jobs/rater-united-states-telus | https://www.theworkathomewoman.com/telus-digital-review/ | https://www.lilachbullock.com/?p=142450")

add(platform="Prolific", category=CAT_A, subcategory="Paid academic & AI research studies", status=APPLY,
    website="https://www.prolific.com", apply_link="https://www.prolific.com/participants",
    roles_and_tasks="Surveys, experiments, AI evaluation studies, some specialist AI tasker pools",
    beginner_friendly="Yes",
    requirements="Reside in supported country (US supported); 18+; identity checks; may be waitlisted",
    us_eligibility="Yes (waitlist possible)",
    published_pay="Researchers must pay at least $8/hr; Prolific recommends $12/hr (official). Self-reported totals ~$150–500/month for active users",
    pay_source="Official help center + community self-reports",
    application_steps="Register → join waitlist if prompted → verify identity → complete 'About You' screeners thoroughly → claim studies as they appear",
    payment_and_fees="No fee for participants; cash out via PayPal (new accounts have waiting periods between cash-outs, third-party)",
    worker_outcome_evidence="r/beermoney Nov 2025 earnings threads list Prolific among top earners ($147–$360/month for some users)",
    evidence_strength="Strong",
    common_challenges="Waitlist; studies fill in minutes; small totals",
    success_strategies="Answer screeners honestly and completely; keep the tab open with notifications; never rush attention checks",
    sources="https://researcher-help.prolific.com/en/articles/445266-how-much-should-i-pay-participants | https://participant-help.prolific.com/en/article/628d72 | https://www.reddit.com/r/beermoney/comments/1pb287m | https://visu.network/blog/prolific-review/")

add(platform="Turing", category=CAT_A, subcategory="LLM coding & expert training contracts", status=APPLY,
    website="https://www.turing.com", apply_link="https://www.turing.com/jobs",
    roles_and_tasks="LLM coding evaluation (Python, JS, C++ and more), agent/function-call training, domain expert tasks",
    beginner_friendly="No (developers and domain experts)",
    requirements="Coding skill verified by tests; AI interview; some roles US-based with Pacific-time overlap",
    us_eligibility="Yes",
    published_pay="Turing recruiting page: $50–250/hr; listings $25–55/hr (LLM trainer) to $200–300/hr (senior dev)",
    pay_source="Official recruiting page + listings",
    application_steps="Profile → automated coding tests → AI-powered interview → practical assessment → matched to projects (no bidding)",
    payment_and_fees="No fee. Monthly USD via Deel/Payoneer/bank; independent contractor",
    worker_outcome_evidence="Many active listings; independent pay reports limited",
    evidence_strength="Medium",
    common_challenges="Assessments are demanding; matches not guaranteed",
    success_strategies="Prepare for timed coding tests; keep GitHub current; state hours/time-zone overlap clearly",
    sources="https://turing.hackerearth.com/ | https://aitrainer.work/guides/turing-ai-training-review/ | https://turing.betterteam.com/javascript-developer")

add(platform="Invisible Technologies (Expert Marketplace / Meridial)", category=CAT_A, subcategory="Expert AI training", status=EXPLORE,
    website="https://www.invisible.co", apply_link="https://www.invisible.co",
    roles_and_tasks="Freelance AI trainers by domain (writing, Python, finance, law, instructional design)",
    beginner_friendly="Some",
    requirements="Project-specific; own computer and fast internet; no visa sponsorship",
    us_eligibility="Yes (listing-specific)",
    published_pay="Listings: $8–65/hr by experience/location; specialist roles up to $150–200/hr (pay guide of ~800 listings)",
    pay_source="Third-party listing analysis",
    application_steps="Apply to listing → assessment → onboarding (details vary)",
    payment_and_fees="Contractor, no benefits",
    worker_outcome_evidence="Many listings; limited independent worker outcome data",
    evidence_strength="Weak",
    common_challenges="Wide pay range; listings close quickly",
    success_strategies="Apply only to listings with posted pay; confirm rate in writing",
    sources="https://www.aigigjobs.com/blog/invisible-technologies-pay-guide-2026 | https://portfoliocareers.levelequity.com/companies/invisible-technologies-2/jobs/37955455-advanced-ai-trainer-software-development-python-expert | https://remowork.life/companies/meridial-ai/pay-and-benefits")

add(platform="Snorkel AI Expert Community", category=CAT_A, subcategory="Expert AI data", status=EXPLORE,
    website="https://snorkel.ai/expert-community/", apply_link="https://snorkel.ai/expert-community/",
    roles_and_tasks="Expert contributors in law, medicine, STEM, computer science write and grade tasks",
    beginner_friendly="No (advanced degrees common)",
    requirements="US location for many listings; MD/DO for medical; JD for legal",
    us_eligibility="Yes",
    published_pay="$10–100 per high-quality task (law listing); $10–80 per submission (2025 listing)",
    pay_source="Official listings via job boards",
    application_steps="Apply via expert community → screening → project onboarding",
    payment_and_fees="Independent contractor; payments via agent of record (third-party report)",
    worker_outcome_evidence="Listings exist; independent outcome reports thin",
    evidence_strength="Weak",
    common_challenges="Per-task pay makes hourly rate uncertain",
    success_strategies="Time yourself on first tasks to compute real $/hr",
    sources="https://snorkel.ai/expert-community/ | https://builtin.com/job/expert-contributor-law-and-legal-contract/4531758 | https://remotive.com/remote/jobs/all-others/expert-contributor-1263624")

add(platform="xAI — AI Tutor", category=CAT_A, subcategory="AI lab direct hire (temporary)", status=EXPLORE,
    website="https://x.ai/careers", apply_link="https://job-boards.greenhouse.io/xai",
    roles_and_tasks="Full-time temporary AI tutor roles (STEM, bilingual, specialist)",
    beginner_friendly="Some (specialists now preferred)",
    requirements="Device and smartphone requirements; ~6-month temporary roles; training 9:00–5:30 PST first 2 weeks",
    us_eligibility="Yes",
    published_pay="$35–65/hr in listings",
    pay_source="Listings (official Greenhouse + copies)",
    application_steps="Apply on Greenhouse → assessments → interview → training period",
    payment_and_fees="Full-time temp; medical insurance depending on residence",
    worker_outcome_evidence="BI/Reuters: ≥500 generalist tutors laid off Sep 2025 as xAI pivoted to specialists",
    evidence_strength="Medium",
    common_challenges="Abrupt team changes; specialist bias",
    success_strategies="Apply for specialist roles matching your degree; have a backup income stream",
    sources="https://boards.greenhouse.io/xai/jobs/4595198007 | https://startup.jobs/ai-tutor-xai-4859847 | https://www.aol.com/articles/musks-xai-lays-off-hundreds-025738720.html")

add(platform="Mindrift (Toloka)", category=CAT_A, subcategory="AI tutor freelance", status=EXPLORE,
    website="https://mindrift.ai", apply_link="https://mindrift.ai",
    roles_and_tasks="AI trainer writers, STEM/code specialists, journalists, designers",
    beginner_friendly="Some (≥1 year professional experience, C1 English for writer roles)",
    requirements="Reside in listed country; CV review; short assessment; Persona ID check",
    us_eligibility="Yes (listing-specific)",
    published_pay="Advertised $15–100+/hr; typical generalist $15–30/hr; listing example $55/hr STEM",
    pay_source="Third-party reviews + listings",
    application_steps="Apply with CV → team review → short assessment → ID verification → matched when projects open",
    payment_and_fees="No fee (official). Per-task pay; PayPal/Payoneer about twice monthly",
    worker_outcome_evidence="Reviews describe regular payments with task droughts",
    evidence_strength="Medium",
    common_challenges="Waiting for project matching; per-task pay variance",
    success_strategies="Keep CV specific to domain; respond fast to project invites",
    sources="https://mindrift.ai/blog/legit-mindrift | https://www.aitrainingjobsfinder.com/blog/mindrift-review-2026 | https://joingerald.com/learn/work--income/mindrift-jobs-guide")

add(platform="Welo Data (Welocalize)", category=CAT_A, subcategory="Search quality rating (W-2 part-time)", status=EXPLORE,
    website="https://welodata.ai", apply_link="https://jobs.lever.co/weloglobal",
    roles_and_tasks="Search quality rater, ads rater, translation validation",
    beginner_friendly="Yes",
    requirements="Reside in named states for some US listings; qualification exam",
    us_eligibility="Yes (state-limited listings)",
    published_pay="Scout Search Quality Rater – English (US): $14.50/hr, W-2 part-time, paid every 2 weeks, 12-month project (Apr 2026 listing)",
    pay_source="Listing copy (Remotive)",
    application_steps="Apply on Lever → screening → exam → onboarding",
    payment_and_fees="W-2 (taxes withheld) for the US Scout listing",
    worker_outcome_evidence="Long history of rater programs; limited 2026 worker reports",
    evidence_strength="Medium",
    common_challenges="State restrictions; hours vary",
    success_strategies="Filter Lever board for 'United States'; study rater guidelines",
    sources="https://remotive.com/remote-jobs/data/scout-search-quality-rater-english-2088618 | https://jobs.lever.co/weloglobal | https://www.workingnomads.com/jobs/search-quality-rater-english-united-states-welocalize")

add(platform="RWS TrainAI", category=CAT_A, subcategory="Search evaluation & AI data", status=EXPLORE,
    website="https://www.rws.com/artificial-intelligence/train-ai-data-services/", apply_link="https://jobs.lever.co/rws",
    roles_and_tasks="Search engine evaluator, AI data annotator, speech evaluation",
    beginner_friendly="Yes",
    requirements="Qualification exam (unpaid, rigorous); 10–20 h/wk typical",
    us_eligibility="Yes (listing-specific)",
    published_pay="US Search Engine Evaluator listing 'up to $15.8/hr' (Oct 2, 2026); blogs report $15–22/hr",
    pay_source="Listing copy + third-party",
    application_steps="Apply → exam → onboarding → hourly work",
    payment_and_fees="Contractor; Tipalti payment complaints reported",
    worker_outcome_evidence="Reviews report payment/support friction",
    evidence_strength="Weak",
    common_challenges="Exam failure rates; payment portal issues",
    success_strategies="Use as backup; keep records of invoices",
    sources="https://remowork.life/jobs/6ace73548529ebd46a48c7ca/search-engine-evaluator-spanish-united-states | https://breakingeven.online/platforms/rws | https://selfmadesuccess.com/?p=14665")

add(platform="Appen (CrowdGen)", category=CAT_A, subcategory="Crowd AI data", status=CAUTION,
    website="https://www.appen.com", apply_link="https://crowdgen.com",
    roles_and_tasks="Search/social evaluation, annotation, data collection",
    beginner_friendly="Yes",
    requirements="Profile verification; project qualifications",
    us_eligibility="Yes",
    published_pay="Not published centrally; reviews cite $10–20/hr industry averages",
    pay_source="Third-party",
    application_steps="Register on CrowdGen → verification → apply to projects → qualify",
    payment_and_fees="No fee; bank/PayPal/Payoneer/Airtm",
    worker_outcome_evidence="Indeed reviews (Apr–May 2026): little work available, pay timing issues; lost Google contract in 2024",
    evidence_strength="Medium",
    common_challenges="Low project volume",
    success_strategies="Register as a backup only",
    sources="https://www.aitrainingjobs.it/appen-crowdgen-review-2026-ai-training-jobs-pay-tasks-reality/ | https://remoteonlineevaluator.com/appen-review-from-a-real-worker/ | https://hk.indeed.com/cmp/Appen/reviews")

add(platform="OneForma (Centific)", category=CAT_A, subcategory="Crowd AI data", status=CAUTION,
    website="https://www.oneforma.com", apply_link="https://www.oneforma.com",
    roles_and_tasks="Annotation, transcription, data collection",
    beginner_friendly="Yes",
    requirements="Multi-stage approval",
    us_eligibility="Yes (project-specific)",
    published_pay="Reported $7–13/hr equivalent; transcription $0.50–1.25 per audio minute",
    pay_source="Third-party",
    application_steps="Register → profile → apply to jobs → qualifications (can take months)",
    payment_and_fees="PayPal (reported $300/yr cap), Payoneer",
    worker_outcome_evidence="Jun 2026 report: unresponsive support, postings down >60% late 2025",
    evidence_strength="Medium",
    common_challenges="Slow approval; low volume",
    success_strategies="Low priority",
    sources="https://remoteonlineevaluator.com/is-oneforma-legit/ | https://breakingeven.online/insights/oneforma | https://remowork.life/blog/oneforma-review-is-it-legit-pay-rates-and-how-it-works")

add(platform="Clickworker / UHRS", category=CAT_A, subcategory="Microtasks", status=EXPLORE,
    website="https://www.clickworker.com", apply_link="https://www.clickworker.com",
    roles_and_tasks="Microtasks: categorization, short writing, UHRS search judging",
    beginner_friendly="Yes",
    requirements="SSN + W-9 for US residents",
    us_eligibility="Yes",
    published_pay="Effective $2–9/hr typical (third-party)",
    pay_source="Third-party",
    application_steps="Register → assessments → tasks",
    payment_and_fees="PayPal min €10 per official help; scheduled bill runs",
    worker_outcome_evidence="Long-running; low earnings consistently reported",
    evidence_strength="Medium",
    common_challenges="Very low hourly",
    success_strategies="Only for gap-filling",
    sources="https://support-workplace.clickworker.com/support/solutions/articles/80000672346-how-do-i-get-paid-for-my-work- | https://remoteonlineevaluator.com/is-clickworker-legit/")

add(platform="Remotasks", category=CAT_A, subcategory="Crowd AI data (Scale AI legacy)", status=UNAVAILABLE,
    website="https://www.remotasks.com", apply_link="https://outlier.ai",
    roles_and_tasks="Legacy annotation platform; new sign-ups redirected to Outlier in tests",
    beginner_friendly="n/a", requirements="n/a", us_eligibility="Not verified (closure notice seen elsewhere)",
    published_pay="n/a", pay_source="n/a",
    application_steps="Use Outlier instead",
    payment_and_fees="n/a",
    worker_outcome_evidence="Closures in several countries (2024); Aug 2026 sign-up test showed closure notice pointing to Outlier",
    evidence_strength="Medium",
    common_challenges="Not open", success_strategies="Apply to Outlier",
    sources="https://visu.network/blog/remotasks-review/ | https://restofworld.org/2024/scale-ai-remotasks-banned-workers/")

add(platform="Uber AI Solutions", category=CAT_A, subcategory="Gig AI data", status=EXPLORE,
    website="https://www.uber.com/us/en/ai-solutions/", apply_link="https://www.uber.com/us/en/ai-solutions/",
    roles_and_tasks="Coding validation, audio recording, image/video labeling; US driver pilot for in-app tasks",
    beginner_friendly="Yes (pilot-based)", requirements="Program-specific; driver pilot via Uber app",
    us_eligibility="Partial (pilot)",
    published_pay="Not verified ($20–200/hr claim from a weak source)",
    pay_source="Third-party",
    application_steps="Watch Uber app / AI Solutions page for invitations",
    payment_and_fees="Not verified",
    worker_outcome_evidence="Pilot reported Oct 2025; division leadership exits Jan & Jul 2026",
    evidence_strength="Weak",
    common_challenges="Limited access", success_strategies="Opportunistic only",
    sources="https://www.staffingindustry.com/news/global-daily-news/uber-gig-worker-data-labeling-business-undergoes-shakeup | https://getcoai.com/news/ubers-new-assignment-for-gig-workers-ai-data-labeling/")

add(platform="Y Combinator — Work at a Startup", category=CAT_A, subcategory="AI startup jobs (full-time, contract, intern)", status=APPLY,
    website="https://www.workatastartup.com", apply_link="https://www.workatastartup.com",
    roles_and_tasks="Engineering, design, product, operations, sales, recruiting at YC-funded startups; remote filter available",
    beginner_friendly="Some (new grads and interns welcome at many startups)",
    requirements="One profile; founders reach out; you can also apply directly",
    us_eligibility="Yes",
    published_pay="Salary and equity shown per listing (e.g., Halluminate roles $150–275K)",
    pay_source="Official listings",
    application_steps="Create one profile → set role/remote preferences → founders message you or you apply to listings → founder chats → work trial/interviews",
    payment_and_fees="Free",
    worker_outcome_evidence="Official FAQ; widely used by YC companies; individual outcome reports limited in search index",
    evidence_strength="Medium",
    common_challenges="High competition for remote roles; many SF in-person roles",
    success_strategies="Write a specific 'what I've built' section; message founders with a 3-line note tied to their product",
    sources="https://www.workatastartup.com/faq | https://www.ycombinator.com/jobs/role/all/remote | https://www.workatastartup.com/jobs/84521")

add(platform="Wellfound (formerly AngelList Talent)", category=CAT_A, subcategory="Startup job board", status=APPLY,
    website="https://wellfound.com", apply_link="https://wellfound.com/candidates/remote",
    roles_and_tasks="Startup roles across functions; remote filters; salary/equity shown before applying",
    beginner_friendly="Some",
    requirements="Profile + resume; check 'Hires remotely from' for each job",
    us_eligibility="Yes",
    published_pay="Salary and equity ranges on listings",
    pay_source="Official listings",
    application_steps="Build profile → filter remote/US → apply with short note → recruiter chat",
    payment_and_fees="Free",
    worker_outcome_evidence="Reviews: salary transparency praised; some users get few replies or spam",
    evidence_strength="Medium",
    common_challenges="Low response rate on popular remote roles",
    success_strategies="Apply within 48 hours of posting; personalize the note",
    sources="https://help.wellfound.com/article/762-remote-job-search-filters | https://jobright.ai/blog/wellfound-review-2026-features-walkthrough-and-alternatives/")

add(platform="Halluminate (YC S25)", category=CAT_A, subcategory="AI startup (finance RL environments)", status=EXPLORE,
    website="https://halluminate.ai", apply_link="https://www.workatastartup.com/jobs/84521",
    roles_and_tasks="Full-time SF roles; company recruits and trains 'contractor finance staff' (no public contractor application found)",
    beginner_friendly="No",
    requirements="Finance analyst/associate background for project lead roles",
    us_eligibility="Yes (in-person SF for full-time)",
    published_pay="$150–275K full-time (YC listings)",
    pay_source="Official YC listing",
    application_steps="3 × 30-min video chats → 2-day in-person or 5-day remote work trial",
    payment_and_fees="n/a",
    worker_outcome_evidence="None public for contractors",
    evidence_strength="Weak",
    common_challenges="No open contractor route",
    success_strategies="Finance professionals: follow founders on LinkedIn/X and ask about contractor roles",
    sources="https://www.workatastartup.com/jobs/84521 | https://zerogtalent.com/ai-jobs/halluminate/founding-member-of-technical-staff-87881")

# =====================================================================  B
add(platform="Upwork", category=CAT_B, subcategory="General freelance marketplace", status=APPLY,
    website="https://www.upwork.com", apply_link="https://www.upwork.com/nx/signup/?dest=home",
    roles_and_tasks="Bid on client jobs or sell Project Catalog packages: writing, design, admin/VA, marketing, data, development, AI services",
    beginner_friendly="Yes (slow start typical)",
    requirements="Profile approval; ID verification (often after first contract)",
    us_eligibility="Yes",
    published_pay="Freelancer sets rate. Fees: variable freelancer service fee 0–15% shown at proposal (third-party); Freelancer Plus $19.99/mo incl. 100 Connects and 0% service fee (Upwork pricing page)",
    pay_source="Official pricing page + third-party fee guides",
    application_steps="Sign up → complete profile (title, overview, portfolio, rate) → approval → buy/spend Connects on proposals → interview via chat/call → contract → milestones/hours",
    payment_and_fees="Basic: 10 free Connects/mo, extra $0.15 each; withdraw to US bank",
    worker_outcome_evidence="Upwork community: '2 months to first client', '6 months of proposals'; Upwork-quoted Reddit: profile July → first client October",
    evidence_strength="Strong",
    common_challenges="Connects cost; saturated categories; first review is hardest",
    success_strategies="Niche title; 2–3 portfolio pieces; apply within hours of posting; small fixed-price first jobs; specific 120–180 word proposals",
    sources="https://www.upwork.com/resources/is-upwork-free | https://golance.com/blogs/upwork-fees-explained-2026 | https://community.upwork.com/t5/Freelancers/How-many-proposals-til-your-first-job/m-p/1220716/highlight/true | https://www.upwork.com/resources/upwork-success-stories-reddit")

add(platform="Fiverr", category=CAT_B, subcategory="Gig (productized service) marketplace", status=APPLY,
    website="https://www.fiverr.com", apply_link="https://www.fiverr.com/start_selling",
    roles_and_tasks="Sell fixed-scope gigs: design, writing, video, voice, data, AI services, VA",
    beginner_friendly="Yes",
    requirements="Seller profile, gigs with packages and samples",
    us_eligibility="Yes",
    published_pay="Seller sets price; Fiverr keeps 20% of every order incl. tips",
    pay_source="Third-party fee guides citing ToS",
    application_steps="Create seller account → publish 1–3 gigs (packages, FAQ, gallery) → respond fast to inquiries → deliver → reviews unlock levels",
    payment_and_fees="Earnings clear after ~14 days (7 for Top Rated); withdrawal fees vary",
    worker_outcome_evidence="Fiverr community: first order after ~3 weeks; first order in a week then 3 months none; returning sellers struggle",
    evidence_strength="Medium",
    common_challenges="Visibility; 20% fee; price competition",
    success_strategies="Narrow gig ('Notion CRM setup for real-estate agents'); outcome-based title; fast response time; reuse buyers",
    sources="https://vaultleap.com/blog/fiverr-fees-explained-2026 | https://community.fiverr.com/public/forum/boards/ask-the-community-xsm/posts/307297-after-so-much-failures-i-got-my-first-order | https://community.fiverr.com/public/forum/boards/freelancer-lounge-sry/posts/319341-got-my-first-order-and-immediately-had-two-repeat-orders-after-that")

add(platform="Contra", category=CAT_B, subcategory="Portfolio-first, commission-free", status=APPLY,
    website="https://contra.com", apply_link="https://contra.com",
    roles_and_tasks="Portfolio + service listings for design, development, marketing, content; invoices and contracts for clients you bring",
    beginner_friendly="Yes (best for invoicing clients you find yourself)",
    requirements="Portfolio",
    us_eligibility="Yes",
    published_pay="0% commission for freelancers (official); Pro $29/mo or $199/yr (third-party)",
    pay_source="Official + third-party",
    application_steps="Create profile → add projects and services → share link with leads → send proposals/invoices",
    payment_and_fees="Bank, card, PayPal, USDC payouts; clients may pay fees",
    worker_outcome_evidence="Reviews: job board thin without Pro",
    evidence_strength="Weak",
    common_challenges="Few inbound clients", success_strategies="Use as your portfolio + payment rail; bring clients from LinkedIn",
    sources="https://contra.com/commission-free | https://ruul.io/blog/what-is-contra | https://www.fastlancer.org/en/fastlancer-blog/contra-review/")

add(platform="Freelancer.com", category=CAT_B, subcategory="Bidding marketplace + contests", status=EXPLORE,
    website="https://www.freelancer.com", apply_link="https://www.freelancer.com/signup",
    roles_and_tasks="Bid on projects; contests for design",
    beginner_friendly="Yes (very price-competitive)",
    requirements="Profile; limited free bids",
    us_eligibility="Yes",
    published_pay="Freelancer fee 10% or $5 minimum per project payment (Fees page as cited Jul 2026)",
    pay_source="Third-party citing official page",
    application_steps="Sign up → skills/exams → bid → award → milestone payments",
    payment_and_fees="Membership tiers add bids",
    worker_outcome_evidence="Limited recent US outcome data",
    evidence_strength="Weak",
    common_challenges="Low budgets; spam projects",
    success_strategies="Bid only on verified-payment clients; never move payment off-platform",
    sources="https://www.jobbers.io/the-freelance-platform-fee-encyclopedia-every-fee-on-every-platform-documented/ | https://www.freelancer.com/feesandcharges")

add(platform="Toptal", category=CAT_B, subcategory="Vetted senior network", status=APPLY,
    website="https://www.toptal.com", apply_link="https://www.toptal.com/talent/apply",
    roles_and_tasks="Developers, designers, finance experts, project/product managers on client engagements",
    beginner_friendly="No (senior talent)",
    requirements="Strong English and communication; technical test; live screening; test project",
    us_eligibility="Yes",
    published_pay="Talent sets hourly rate; Toptal does not publish markup",
    pay_source="Official",
    application_steps="Language & personality interview → timed skill test → live technical screening → test project (1–3 wks) → onboarding; total 3–8 weeks; <3% accepted (Toptal claim)",
    payment_and_fees="No fee to talent",
    worker_outcome_evidence="Long-running network; acceptance-rate claims self-reported",
    evidence_strength="Medium",
    common_challenges="Very selective", success_strategies="Apply only with 3+ years of strong, demonstrable work",
    sources="https://www.toptal.com/top-3-percent | https://themeisle.com/blog/toptal-review/ | https://wise.com/us/blog/upwork-vs-toptal-comparison")

add(platform="Braintrust", category=CAT_B, subcategory="Talent network with AI recruiter", status=APPLY,
    website="https://www.usebraintrust.com", apply_link="https://www.usebraintrust.com/for-talent",
    roles_and_tasks="Contract roles in engineering, design, product, marketing at enterprise clients",
    beginner_friendly="No",
    requirements="AI interview (AIR); experience",
    us_eligibility="Yes",
    published_pay="Talent keeps 100% (official: no talent fees)",
    pay_source="Official",
    application_steps="Create profile → AI screening interview → apply to jobs → client interviews",
    payment_and_fees="Free to talent",
    worker_outcome_evidence="Limited recent independent reports",
    evidence_strength="Weak",
    common_challenges="Competitive", success_strategies="Use for mid/senior contract roles",
    sources="https://www.usebraintrust.com/for-talent | https://usebraintrust.com/blog/braintrust-network-update-aug-sept-2024 | https://www.hireinsouth.com/post/braintrust-review")

add(platform="Guru", category=CAT_B, subcategory="General marketplace", status=EXPLORE,
    website="https://www.guru.com", apply_link="https://www.guru.com",
    roles_and_tasks="Programming, writing, design, admin, engineering",
    beginner_friendly="Yes", requirements="Profile", us_eligibility="Yes",
    published_pay="Job fee ~4.95–8.95% by membership plan",
    pay_source="Third-party citing pricing page",
    application_steps="Profile → quotes on jobs → SafePay agreements",
    payment_and_fees="SafePay escrow",
    worker_outcome_evidence="Limited recent data", evidence_strength="Weak",
    common_challenges="Lower traffic", success_strategies="Secondary profile",
    sources="https://www.guru.com/pricing-freelancer | https://aiproposer.com/learn/guru-fees")

add(platform="PeoplePerHour", category=CAT_B, subcategory="UK-based marketplace (US accepted)", status=EXPLORE,
    website="https://www.peopleperhour.com", apply_link="https://www.peopleperhour.com",
    roles_and_tasks="Hourlies (fixed offers) and proposals",
    beginner_friendly="Yes", requirements="Profile approval", us_eligibility="Yes",
    published_pay="Fees: 20% on first £500 per client, then 7.5%, then 3.5% (third-party; tiers disputed)",
    pay_source="Third-party",
    application_steps="Apply → approval → proposals/hourlies",
    payment_and_fees="GBP-centric", worker_outcome_evidence="Limited US data", evidence_strength="Weak",
    common_challenges="UK client base", success_strategies="Good for UK/EU-facing services",
    sources="https://aiproposer.com/learn/peopleperhour-fees")

add(platform="99designs (Vista)", category=CAT_B, subcategory="Design contests & 1-to-1", status=EXPLORE,
    website="https://99designs.com", apply_link="https://99designs.com/designers",
    roles_and_tasks="Logo, branding, packaging, web design contests and direct projects",
    beginner_friendly="Yes (contests) ", requirements="Portfolio; levels Entry/Mid/Top",
    us_eligibility="Yes",
    published_pay="Contest prizes ~$249–1,300+; designer platform fee reported 15/10/5% by level",
    pay_source="Official help + third-party",
    application_steps="Sign up → enter contests → win/finalist → level reviews in application windows",
    payment_and_fees="Level-based fees", worker_outcome_evidence="Long-running; contests are speculative work",
    evidence_strength="Medium", common_challenges="Unpaid contest entries", success_strategies="Limit contest time; move winners to 1-to-1",
    sources="https://support.99designs.com/hc/articles/360022097311 | https://99designs.ca/designer-resource-center/designer-levels3 | https://www.jobbers.io/?p=86121")

add(platform="Arc.dev", category=CAT_B, subcategory="Remote developer network", status=APPLY,
    website="https://arc.dev", apply_link="https://arc.dev",
    roles_and_tasks="Freelance and full-time remote developer roles",
    beginner_friendly="No", requirements="Profile screen, technical vetting, interviews",
    us_eligibility="Yes",
    published_pay="Reported $60–80/hr for freelancers (third-party)",
    pay_source="Third-party",
    application_steps="Profile → screen → technical interview → matching",
    payment_and_fees="Free to developers", worker_outcome_evidence="Limited", evidence_strength="Weak",
    common_challenges="Selective", success_strategies="Strong GitHub + clear stack",
    sources="https://arc.dev/employer-blog/?p=3388 | https://flexiple.com/reviews/arcdev")

add(platform="MarketerHire", category=CAT_B, subcategory="Vetted marketing freelancers", status=EXPLORE,
    website="https://marketerhire.com", apply_link="https://marketerhire.com",
    roles_and_tasks="Paid media, growth, content, lifecycle, SEO contracts",
    beginner_friendly="No", requirements="Work samples, skills assessment, video interview",
    us_eligibility="Yes", published_pay="Not published", pay_source="n/a",
    application_steps="Apply → review of experience and samples → skills assessment → video interview",
    payment_and_fees="Not published", worker_outcome_evidence="Company claims <5% accepted",
    evidence_strength="Weak", common_challenges="Selective", success_strategies="Bring quantified campaign results",
    sources="https://marketerhire.com/blog/marketerhire-vs-toptal | https://ddiy.co/?p=8508")

add(platform="Catalant", category=CAT_B, subcategory="Independent consulting marketplace", status=EXPLORE,
    website="https://gocatalant.com", apply_link="https://gocatalant.com",
    roles_and_tasks="Strategy, operations, finance consulting projects for enterprises",
    beginner_friendly="No", requirements="Consulting/industry experience",
    us_eligibility="Yes", published_pay="Not published", pay_source="n/a",
    application_steps="Expert profile → matched to project briefs",
    payment_and_fees="Not published", worker_outcome_evidence="Mixed freelancer sentiment on Trustpilot",
    evidence_strength="Weak", common_challenges="Few matches", success_strategies="For ex-consultants/managers",
    sources="https://www.gtm8020.com/blog/catalant-review.md")

add(platform="GLG (Gerson Lehrman Group)", category=CAT_B, subcategory="Expert network — paid calls", status=APPLY,
    website="https://glginsights.com", apply_link="https://glginsights.com",
    roles_and_tasks="Paid 1-hour phone/video consultations with investors and consultants about your industry knowledge",
    beginner_friendly="No (needs industry experience; laid-off professionals fit well)",
    requirements="Industry expertise; compliance training; confidentiality rules (no current-employer secrets)",
    us_eligibility="Yes",
    published_pay="You set/agree a per-call rate; advice sites estimate $100–300/hr typical",
    pay_source="Third-party estimates",
    application_steps="Create network member profile → wait for project invitations → screening questions → scheduled call",
    payment_and_fees="Paid per consultation", worker_outcome_evidence="Widely documented industry; volume unpredictable",
    evidence_strength="Medium", common_challenges="Irregular invitations",
    success_strategies="Detail niche expertise (products, vendors, regions) in profile; answer screening questions quickly",
    sources="https://expertopportunities.com/expert-network-hourly-rates/ | https://arbolus.com/resources/how-much-do-expert-networks-pay")

add(platform="AlphaSights / Guidepoint", category=CAT_B, subcategory="Expert networks", status=EXPLORE,
    website="https://www.alphasights.com", apply_link="https://www.guidepoint.com",
    roles_and_tasks="Paid expert calls and surveys",
    beginner_friendly="No", requirements="Industry experience", us_eligibility="Yes",
    published_pay="Per-call; estimates $100–300/hr", pay_source="Third-party",
    application_steps="Usually invited via LinkedIn/email; Guidepoint accepts expert sign-ups",
    payment_and_fees="Per consultation", worker_outcome_evidence="Industry-wide", evidence_strength="Medium",
    common_challenges="Irregular", success_strategies="Keep LinkedIn headline specific to your niche",
    sources="https://expertopportunities.com/what-is-an-expert-network/ | https://arbolus.com/resources/how-much-do-expert-networks-pay")

add(platform="Dribbble / Behance", category=CAT_B, subcategory="Design portfolios with job boards", status=EXPLORE,
    website="https://dribbble.com", apply_link="https://www.behance.net",
    roles_and_tasks="Portfolio hosting, freelance project inquiries, job boards",
    beginner_friendly="Yes", requirements="Portfolio", us_eligibility="Yes",
    published_pay="Not applicable (client-set)", pay_source="n/a",
    application_steps="Publish case studies → enable hire-me → respond to inquiries",
    payment_and_fees="Platform payment fees vary by plan", worker_outcome_evidence="Limited", evidence_strength="Weak",
    common_challenges="Passive inbound", success_strategies="Use as portfolio links in Upwork/LinkedIn outreach",
    sources="https://passionates.com/top-behance-alternatives-for-startups/")

# =====================================================================  C
add(platform="Amazon — Virtual Customer Service", category=CAT_C, subcategory="Customer service (W-2)", status=EXPLORE,
    website="https://www.amazon.jobs", apply_link="https://www.amazon.jobs/en/search?base_query=virtual+customer+service",
    roles_and_tasks="Chat/phone customer service from home; seasonal and regular",
    beginner_friendly="Yes", requirements="Reside in a hiring state; reliable internet; quiet workspace",
    us_eligibility="State-limited",
    published_pay="~$15–19/hr reported; ZipRecruiter aggregate avg $18.80/hr",
    pay_source="Third-party/aggregate",
    application_steps="Apply only on amazon.jobs → assessment → virtual onboarding",
    payment_and_fees="W-2 with benefits after waiting period (reported)",
    worker_outcome_evidence="Large-scale past hiring pushes (e.g., 3,000 remote CS roles in 18 states)",
    evidence_strength="Medium", common_challenges="Openings appear in waves; scams impersonate Amazon",
    success_strategies="Set job alerts on amazon.jobs; never apply via text/WhatsApp links",
    sources="https://www.lilachbullock.com/amazon-remote-jobs-real-work-from-home-roles/ | https://www.ziprecruiter.com/Jobs/Remote-Amazon-Customer-Service | https://www.fox13seattle.com/news/amazon-hiring-spree-looking-for-3000-remote-workers")

add(platform="Apple — At Home Advisor", category=CAT_C, subcategory="Tech support (W-2)", status=EXPLORE,
    website="https://jobs.apple.com", apply_link="https://jobs.apple.com/en-us/search?search=at%20home%20advisor",
    roles_and_tasks="AppleCare phone/chat support; College Program variant for students",
    beginner_friendly="Yes", requirements="US residency in hiring area; home office setup",
    us_eligibility="Yes (location-limited)",
    published_pay="College Program At Home Advisor $27.75–32.45/hr (tech.co); ZipRecruiter aggregate avg $26.41 (Aug 2026)",
    pay_source="Third-party",
    application_steps="Apply on jobs.apple.com → assessments → virtual interview → paid training",
    payment_and_fees="W-2 employee", worker_outcome_evidence="Glassdoor interview reports exist",
    evidence_strength="Medium", common_challenges="Seasonal openings", success_strategies="Search 'At Home Advisor' monthly",
    sources="https://tech.co/news/fully-remote-jobs-at-apple | https://www.ziprecruiter.com/Jobs/Apple-Home-Advisor | https://hireaniner.charlotte.edu/jobs/84dfc4b36c3fdf9bfb2adfd83c0d4772")

add(platform="Concentrix (work-at-home)", category=CAT_C, subcategory="Customer service BPO (W-2)", status=EXPLORE,
    website="https://www.concentrix.com", apply_link="https://jobs.concentrix.com",
    roles_and_tasks="Customer service, tech support, sales for client brands",
    beginner_friendly="Yes", requirements="Background check, internet speed test, state residency",
    us_eligibility="State-limited", published_pay="~$13–18/hr reported (2026)", pay_source="Third-party",
    application_steps="Apply → assessment → interview → paid training",
    payment_and_fees="W-2", worker_outcome_evidence="Large employer; reviews mixed", evidence_strength="Medium",
    common_challenges="Strict metrics", success_strategies="Filter careers site by 'remote' + your state",
    sources="https://joingerald.com/learn/work--income/customer-service-true-work-from-home-jobs | https://www.lilachbullock.com/remote-customer-service-jobs-beginners/")

add(platform="TTEC @Home", category=CAT_C, subcategory="Customer service BPO (W-2)", status=EXPLORE,
    website="https://www.ttec.com", apply_link="https://careers.ttec.com",
    roles_and_tasks="Customer care, tech support, sales",
    beginner_friendly="Yes", requirements="Background check; equipment/internet requirements",
    us_eligibility="State-limited", published_pay="~$15–18/hr reported; some reduced training rate",
    pay_source="Third-party", application_steps="Apply → assessments → virtual interview → training",
    payment_and_fees="W-2", worker_outcome_evidence="Large employer", evidence_strength="Medium",
    common_challenges="Training-rate period", success_strategies="Ask about training pay in interview",
    sources="https://joingerald.com/learn/work--income/customer-service-true-work-from-home-jobs")

add(platform="Foundever (formerly Sitel)", category=CAT_C, subcategory="Customer service BPO (W-2)", status=EXPLORE,
    website="https://foundever.com", apply_link="https://foundever.com/careers",
    roles_and_tasks="Customer service and support", beginner_friendly="Yes",
    requirements="Internet speed check before offer; equipment often provided",
    us_eligibility="State-limited", published_pay="~$14–17/hr reported", pay_source="Third-party",
    application_steps="Apply → speed check → assessment → interview → training",
    payment_and_fees="W-2", worker_outcome_evidence="Glassdoor reviews; one 2026 review ~$25/hr specific account",
    evidence_strength="Medium", common_challenges="Account-dependent schedules", success_strategies="Prioritize postings that ship equipment",
    sources="https://joingerald.com/learn/work--income/sitel-work-from-home-foundever-careers | https://static-pc.glassdoor.fr/Reviews/Employee-Review-Foundever-E11480-RVW15252318.htm")

add(platform="Liveops", category=CAT_C, subcategory="Customer service (independent contractor)", status=CAUTION,
    website="https://join.liveops.com", apply_link="https://join.liveops.com",
    roles_and_tasks="Inbound calls for client programs (insurance, healthcare, retail)",
    beginner_friendly="Some", requirements="$25 background check paid by you; unpaid certification; dual monitors, wired internet; Windows PC",
    us_eligibility="Yes",
    published_pay="Talk-time 25–34¢ per minute for some programs; some commission-only (official FAQ)",
    pay_source="Official",
    application_steps="Apply → pay background check → unpaid program certification → schedule calls",
    payment_and_fees="Paid twice monthly; you cover equipment; no guaranteed earnings",
    worker_outcome_evidence="Long-running; reviews note pay only while on calls",
    evidence_strength="Medium", common_challenges="Upfront costs; unpaid certification; only talk time paid",
    success_strategies="Calculate realistic $/hr before paying anything",
    sources="https://liveops.com/blog/pay-transparency-how-independent-contractors-earn-with-liveops/ | https://join.liveops.com/faqs")

add(platform="Arise", category=CAT_C, subcategory="Customer service (contractor via 'IBO')", status=CAUTION,
    website="https://www.arise.com", apply_link="https://www.arise.com",
    roles_and_tasks="Customer service for client brands as an independent business",
    beginner_friendly="Some", requirements="Historically: paid training/certification and equipment",
    us_eligibility="Yes", published_pay="Not published", pay_source="n/a",
    application_steps="Register business → paid certification courses (historically) → client programs",
    payment_and_fees="Worker-paid costs reported",
    worker_outcome_evidence="ProPublica investigation; D.C. Attorney General lawsuit alleging misclassification and pay practices",
    evidence_strength="Strong", common_challenges="Pay-to-work model", success_strategies="Prefer W-2 customer service employers",
    sources="https://www.propublica.org/article/d-c-attorney-general-sues-customer-service-firm-arise-for-stiffing-workers-on-pay")

add(platform="Working Solutions", category=CAT_C, subcategory="Customer service (contractor)", status=EXPLORE,
    website="https://workingsolutions.com", apply_link="https://workingsolutions.com",
    roles_and_tasks="Customer support, sales, tech support programs",
    beginner_friendly="Some", requirements="Program certification", us_eligibility="Yes",
    published_pay="Not verified (~$15/hr listicle)", pay_source="Weak third-party",
    application_steps="Apply → assessment → program certification",
    payment_and_fees="Contractor", worker_outcome_evidence="Thin", evidence_strength="Weak",
    common_challenges="Unverified pay", success_strategies="Ask for program pay in writing before certifying",
    sources="https://bloggerspassion.com/5-real-online-jobs-for-earning-quick-money-2/")

add(platform="BELAY", category=CAT_C, subcategory="Virtual assistant / bookkeeping (US contractors)", status=EXPLORE,
    website="https://belaysolutions.com", apply_link="https://belaysolutions.com/careers/",
    roles_and_tasks="Executive/virtual assistant, bookkeeping, web specialist for US small businesses",
    beginner_friendly="No (admin experience expected)", requirements="US-based; experience; vetting (claims top 2–3% accepted)",
    us_eligibility="Yes",
    published_pay="Clients pay ~$42–50/hr; VA pay ~$20/hr in one anonymous report; BELAY says it raised specialist pay ≥53% in four years",
    pay_source="Third-party + Glassdoor",
    application_steps="Apply → assessments → interviews → client match",
    payment_and_fees="1099 contractor", worker_outcome_evidence="Glassdoor reviews mixed (great flexibility; low end for EA)",
    evidence_strength="Medium", common_challenges="Wait for client match", success_strategies="Lead with admin tools you master (Google Workspace, QuickBooks, CRM)",
    sources="https://www.usecarly.com/blog/belay-virtual-assistant-review/ | https://www.glassdoor.de/Bewertungen/Bewertungen-BELAY-E893704-RVW103745843.htm")

add(platform="Wyzant", category=CAT_C, subcategory="Online tutoring marketplace", status=APPLY,
    website="https://www.wyzant.com", apply_link="https://www.wyzant.com",
    roles_and_tasks="1-on-1 tutoring in academic subjects, test prep, professional skills",
    beginner_friendly="Yes (subject mastery required)", requirements="Profile, subject quizzes, background check",
    us_eligibility="Yes",
    published_pay="Tutors set rates; commission 25% until $2,000 earned, then 20% (third-party)",
    pay_source="Third-party",
    application_steps="Profile → subject tests → approval → respond to student requests",
    payment_and_fees="Commission per lesson", worker_outcome_evidence="Widely used; outcomes depend on subject demand",
    evidence_strength="Medium", common_challenges="Starting without reviews", success_strategies="Price modestly at first; respond within an hour",
    sources="https://blog.theinterviewguys.com/?p=11567 | https://sidehusl.com/12-best-tutoring-platforms/")

add(platform="Varsity Tutors", category=CAT_C, subcategory="Assigned online tutoring", status=EXPLORE,
    website="https://www.varsitytutors.com", apply_link="https://www.varsitytutors.com",
    roles_and_tasks="Tutoring matched by algorithm", beginner_friendly="Yes",
    requirements="Subject tests; background check", us_eligibility="Yes",
    published_pay="$15–40/hr; ~$15 most common (third-party)", pay_source="Third-party",
    application_steps="Apply → subject assessments → mock session → matching",
    payment_and_fees="Contractor", worker_outcome_evidence="Reviews note low base pay", evidence_strength="Medium",
    common_challenges="Low base rate", success_strategies="Use for quick start, move to own clients",
    sources="https://sidehusl.com/varsity-tutors/")

add(platform="Tutor.com (Princeton Review)", category=CAT_C, subcategory="On-demand tutoring", status=EXPLORE,
    website="https://www.tutor.com", apply_link="https://www.tutor.com/apply",
    roles_and_tasks="On-demand chat tutoring", beginner_friendly="Yes", requirements="Subject exams; often college student or degree",
    us_eligibility="Yes", published_pay="$12–22/hr reported", pay_source="Third-party",
    application_steps="Apply → exams → mock session → certification", payment_and_fees="Contractor",
    worker_outcome_evidence="Long-running", evidence_strength="Weak", common_challenges="Low pay", success_strategies="Quick-start option",
    sources="https://sidehusl.com/12-best-tutoring-platforms/ | https://blog.theinterviewguys.com/?p=11567")

add(platform="Rev", category=CAT_C, subcategory="Transcription & captioning", status=APPLY,
    website="https://www.rev.com", apply_link="https://www.rev.com/freelancers",
    roles_and_tasks="Transcription, captions, subtitles", beginner_friendly="Yes",
    requirements="Grammar test + transcription sample", us_eligibility="Yes",
    published_pay="~$0.30–1.10 per audio minute (third-party); effective hourly often low",
    pay_source="Third-party",
    application_steps="Apply → English/grammar test → transcription sample → claim jobs from queue",
    payment_and_fees="PayPal weekly (reported)", worker_outcome_evidence="Glassdoor Feb 2026: test easy, no feedback after assessment",
    evidence_strength="Medium", common_challenges="Low effective hourly; AI competition", success_strategies="Use for short-term income; aim for captioning",
    sources="https://www.lilachbullock.com/how-does-rev-transcription-work-for-freelancers/ | https://www.glassdoor.com.br/Entrevista/Rev-Entrevista-E802400-RVW18146796.htm | https://joingerald.com/learn/work--income/best-transcription-jobs-from-home-2026")

add(platform="TranscribeMe", category=CAT_C, subcategory="Transcription", status=EXPLORE,
    website="https://www.transcribeme.com", apply_link="https://workhub.transcribeme.com",
    roles_and_tasks="Short-clip transcription", beginner_friendly="Yes", requirements="Training course + exam",
    us_eligibility="Yes", published_pay="$15–22 per audio hour (third-party)", pay_source="Third-party",
    application_steps="Free training → exam → tasks", payment_and_fees="PayPal",
    worker_outcome_evidence="Long-running", evidence_strength="Weak", common_challenges="Very low hourly", success_strategies="Gap-filler only",
    sources="https://joingerald.com/learn/work--income/best-transcription-jobs-from-home-2026")

add(platform="GoTranscript", category=CAT_C, subcategory="Transcription", status=EXPLORE,
    website="https://gotranscript.com", apply_link="https://gotranscript.com/transcription-jobs",
    roles_and_tasks="Transcription", beginner_friendly="Yes", requirements="Test", us_eligibility="Yes",
    published_pay="Up to $0.60 per audio minute (third-party)", pay_source="Third-party",
    application_steps="Test → tasks", payment_and_fees="PayPal/Payoneer",
    worker_outcome_evidence="Long-running", evidence_strength="Weak", common_challenges="Low hourly", success_strategies="Gap-filler only",
    sources="https://www.aol.com/lifestyle/15-best-transcription-jobs-online-125700079.html")

add(platform="UserTesting", category=CAT_C, subcategory="Website/app feedback tests", status=APPLY,
    website="https://www.usertesting.com", apply_link="https://www.usertesting.com/get-paid-to-test",
    roles_and_tasks="Think-aloud tests (~$10 for 15–20 min), live interviews ($30–60)",
    beginner_friendly="Yes", requirements="Practice test; mic; screen recorder",
    us_eligibility="Yes", published_pay="~$10 per test; live interviews $30–60 (third-party)", pay_source="Third-party",
    application_steps="Sign up → practice test → screeners → tests",
    payment_and_fees="PayPal", worker_outcome_evidence="Trustpilot: tests first-come-first-served; reward shown upfront",
    evidence_strength="Medium", common_challenges="Tests vanish fast", success_strategies="Enable notifications; speak continuously during tests",
    sources="https://www.softwaretestinghelp.com/usertesting-review/ | https://au.trustpilot.com/review/usertesting.com?page=7")

add(platform="Respondent", category=CAT_C, subcategory="Paid research interviews (professionals)", status=APPLY,
    website="https://www.respondent.io", apply_link="https://www.respondent.io",
    roles_and_tasks="Paid user-research interviews, focus groups",
    beginner_friendly="Yes (professional background helps)", requirements="Verified LinkedIn/profile",
    us_eligibility="Yes", published_pay="$50–400+ per study (third-party)", pay_source="Third-party",
    application_steps="Profile → apply to studies → screener → scheduled session",
    payment_and_fees="Paid after session", worker_outcome_evidence="Widely cited", evidence_strength="Medium",
    common_challenges="Low selection rate", success_strategies="Accurate job title and tools in profile",
    sources="https://www.finder.com/make-money-online/how-to-earn-money-user-testing")

add(platform="User Interviews", category=CAT_C, subcategory="Paid research studies", status=APPLY,
    website="https://www.userinterviews.com", apply_link="https://www.userinterviews.com/studies",
    roles_and_tasks="Interviews, surveys, usability studies", beginner_friendly="Yes",
    requirements="Supported country (US supported)", us_eligibility="Yes",
    published_pay="Per study (shown on listing)", pay_source="Official listings",
    application_steps="Sign up → apply to studies → screener", payment_and_fees="Gift cards/PayPal",
    worker_outcome_evidence="Official country list", evidence_strength="Medium",
    common_challenges="Selective screeners", success_strategies="Apply daily",
    sources="https://www.userinterviews.com/support/participant-countries")

add(platform="uTest (Applause)", category=CAT_C, subcategory="Crowdtesting", status=EXPLORE,
    website="https://www.utest.com", apply_link="https://www.utest.com",
    roles_and_tasks="Functional/usability testing; pay per approved bug", beginner_friendly="Yes",
    requirements="Academy courses; devices", us_eligibility="Yes",
    published_pay="Per bug/cycle; $5–50 per cycle commonly reported", pay_source="Third-party",
    application_steps="Sign up → academy → sandbox → invitations",
    payment_and_fees="PayPal/Payoneer", worker_outcome_evidence="Glassdoor: high competition; rejected bugs unpaid",
    evidence_strength="Medium", common_challenges="Pay-per-bug variance", success_strategies="Build QA skills to move to Testlio/QA jobs",
    sources="https://softwaretestpilot.com/blog/career-interview-prep/crowd-testing-platforms-utest-testlio | https://de.glassdoor.ch/Bewertungen/Bewertungen-uTest-E370465-RVW85326531.htm")

add(platform="Testlio", category=CAT_C, subcategory="Freelance QA (hourly)", status=EXPLORE,
    website="https://testlio.com", apply_link="https://testlio.com/job/freelance-us-guam",
    roles_and_tasks="Hourly software testing on client projects", beginner_friendly="Some",
    requirements="Technical screen + paid trial cycle", us_eligibility="Yes",
    published_pay="Hourly; e.g., $18/hr listing (2025)", pay_source="Official listings",
    application_steps="Apply → screen → paid trial cycle → projects",
    payment_and_fees="Weekly PayPal/Payoneer (reported)", worker_outcome_evidence="Official network pledge; listings",
    evidence_strength="Medium", common_challenges="Country/device-specific projects", success_strategies="List your devices and OS versions",
    sources="https://testlio.com/pledge | https://jobs.techstars.com/companies/testlio/jobs/59349570-freelance-software-tester-payments-testing-austria")

add(platform="LinkedIn Jobs", category=CAT_C, subcategory="Job board + network", status=APPLY,
    website="https://www.linkedin.com/jobs", apply_link="https://www.linkedin.com/jobs/search/?f_WT=2",
    roles_and_tasks="All functions; 'Remote' workplace filter (f_WT=2)", beginner_friendly="Yes",
    requirements="Profile", us_eligibility="Yes",
    published_pay="Pay ranges shown on many US listings", pay_source="Official",
    application_steps="Filter Remote + date posted (past 24h/week) → apply → message poster/recruiter",
    payment_and_fees="Free (Premium optional)",
    worker_outcome_evidence="LinkedIn data: remote = 8.4% of postings but 42% of applications",
    evidence_strength="Strong", common_challenges="Huge competition on remote roles",
    success_strategies="Apply early, then message the hiring team; prefer referrals",
    sources="https://www.sherwood.news/business/22-of-job-posts-on-linked-on-linkedin-are-hybrid-or-remote-work")

add(platform="Indeed", category=CAT_C, subcategory="Job board", status=APPLY,
    website="https://www.indeed.com", apply_link="https://www.indeed.com/q-remote-jobs.html",
    roles_and_tasks="All functions incl. remote customer service, admin, sales", beginner_friendly="Yes",
    requirements="Resume", us_eligibility="Yes", published_pay="Varies", pay_source="Listings",
    application_steps="Search 'remote' + title → apply → assessments",
    payment_and_fees="Free", worker_outcome_evidence="Largest US job board; scams present in listings",
    evidence_strength="Medium", common_challenges="Fake postings", success_strategies="Cross-check employer careers page before applying",
    sources="https://hiringlab.indeed.com/")

add(platform="We Work Remotely", category=CAT_C, subcategory="Remote job board", status=APPLY,
    website="https://weworkremotely.com", apply_link="https://weworkremotely.com",
    roles_and_tasks="Programming, design, customer support, sales, marketing, management",
    beginner_friendly="Some", requirements="Varies", us_eligibility="Yes (region filters incl. USA only)",
    published_pay="Varies", pay_source="Listings", application_steps="Filter region → apply on employer site",
    payment_and_fees="Free for job seekers", worker_outcome_evidence="Long-running remote board", evidence_strength="Medium",
    common_challenges="Senior-heavy tech roles", success_strategies="Use the Customer Support category for entry roles",
    sources="https://weworkremotely.com | https://www.jobbers.io/jobbers-io-vs-flexjobs-paid-subscription-vs-free-platform/")

add(platform="Remotive", category=CAT_C, subcategory="Remote job board", status=APPLY,
    website="https://remotive.com", apply_link="https://remotive.com/remote-jobs",
    roles_and_tasks="Tech, support, marketing, AI training listings", beginner_friendly="Some",
    requirements="Varies", us_eligibility="Yes (location tags per listing)",
    published_pay="Often listed", pay_source="Listings", application_steps="Filter → apply on employer site",
    payment_and_fees="Free (paid accelerator optional)", worker_outcome_evidence="Carries many AI training listings cited in this guide",
    evidence_strength="Medium", common_challenges="Location restrictions", success_strategies="Read 'location' tag before applying",
    sources="https://remotive.com | https://joinsecret.com/remotive")

add(platform="Himalayas", category=CAT_C, subcategory="Remote job board", status=APPLY,
    website="https://himalayas.app", apply_link="https://himalayas.app/jobs/countries/united-states",
    roles_and_tasks="Remote roles with company profiles", beginner_friendly="Some", requirements="Free profile",
    us_eligibility="Yes", published_pay="Often listed", pay_source="Listings", application_steps="Filter by US → apply",
    payment_and_fees="Free", worker_outcome_evidence="Limited", evidence_strength="Weak",
    common_challenges="Duplicates of other boards", success_strategies="Use country filter",
    sources="https://himalayas.app")

add(platform="Remote OK", category=CAT_C, subcategory="Remote job board", status=EXPLORE,
    website="https://remoteok.com", apply_link="https://remoteok.com",
    roles_and_tasks="Remote tech and non-tech roles", beginner_friendly="Some", requirements="Varies",
    us_eligibility="Yes", published_pay="Often listed", pay_source="Listings", application_steps="Filter → apply",
    payment_and_fees="Free for seekers", worker_outcome_evidence="Frequently updated (review)", evidence_strength="Weak",
    common_challenges="Tech-heavy", success_strategies="Sort by highest paid / newest",
    sources="https://sidehustles.com/remoteok-review/")

add(platform="Working Nomads", category=CAT_C, subcategory="Remote job aggregator", status=EXPLORE,
    website="https://www.workingnomads.com", apply_link="https://www.workingnomads.com/jobs",
    roles_and_tasks="Curated remote jobs", beginner_friendly="Some", requirements="Varies", us_eligibility="Yes",
    published_pay="Varies", pay_source="Listings", application_steps="Filter → apply",
    payment_and_fees="Free board; premium optional", worker_outcome_evidence="Limited", evidence_strength="Weak",
    common_challenges="Expired listings", success_strategies="Check listing date",
    sources="https://workingnomads.com/premium-subscription")

add(platform="Dynamite Jobs", category=CAT_C, subcategory="Remote job board", status=EXPLORE,
    website="https://dynamitejobs.com", apply_link="https://dynamitejobs.com",
    roles_and_tasks="Remote roles at bootstrapped companies (ops, VA, marketing)", beginner_friendly="Some",
    requirements="Varies", us_eligibility="Yes", published_pay="Salary shown on listings", pay_source="Listings",
    application_steps="Apply via listing", payment_and_fees="Free", worker_outcome_evidence="Limited", evidence_strength="Weak",
    common_challenges="Smaller volume", success_strategies="Good for ops/VA roles",
    sources="https://dynamitejobs.com/about-us")

add(platform="Built In", category=CAT_C, subcategory="Tech job board", status=EXPLORE,
    website="https://builtin.com", apply_link="https://builtin.com/jobs/remote",
    roles_and_tasks="Tech company roles incl. remote; carries AI training listings", beginner_friendly="Some",
    requirements="Varies", us_eligibility="Yes", published_pay="Often listed", pay_source="Listings",
    application_steps="Filter remote → apply", payment_and_fees="Free", worker_outcome_evidence="Limited",
    evidence_strength="Weak", common_challenges="Tech-centric", success_strategies="Combine with company research",
    sources="https://builtin.com/job/expert-contributor-law-and-legal-contract/4531758")

add(platform="Handshake (student & new-grad jobs)", category=CAT_C, subcategory="Early-career job platform", status=APPLY,
    website="https://joinhandshake.com", apply_link="https://joinhandshake.com",
    roles_and_tasks="Internships, entry-level remote roles, virtual career fairs", beginner_friendly="Yes",
    requirements="Student/alum account (many schools partner)", us_eligibility="Yes",
    published_pay="Varies", pay_source="Listings", application_steps="Log in via school → filter Remote → apply → attend virtual fairs",
    payment_and_fees="Free", worker_outcome_evidence="Primary early-career channel at partner schools", evidence_strength="Medium",
    common_challenges="Volume of applicants", success_strategies="Message employers after virtual fairs",
    sources="https://support.joinhandshake.com/hc/en-us/articles/31620022060055-Introduction-to-the-MOVE-Program")

add(platform="FlexJobs", category=CAT_C, subcategory="Paid, hand-screened remote board", status=CAUTION,
    website="https://www.flexjobs.com", apply_link="https://www.flexjobs.com",
    roles_and_tasks="Screened remote/flexible listings", beginner_friendly="Yes", requirements="Paid subscription",
    us_eligibility="Yes",
    published_pay="Subscription: $2.95 14-day trial auto-renewing ~$23.95/4 weeks; quarterly ~$29.85; annual ~$71.40 (third-party, varies)",
    pay_source="Third-party", application_steps="Subscribe → search → apply on employer site",
    payment_and_fees="Watch auto-renewal", worker_outcome_evidence="Users flag renewal visibility",
    evidence_strength="Medium", common_challenges="Cost; many listings also free elsewhere",
    success_strategies="Use free boards first; if you subscribe, set a cancel reminder",
    sources="https://resume.co/blog/flexjobs-review | https://blog.theinterviewguys.com/?p=11182")

add(platform="USAJOBS (federal)", category=CAT_C, subcategory="Federal government jobs", status=CAUTION,
    website="https://www.usajobs.gov", apply_link="https://www.usajobs.gov",
    roles_and_tasks="Federal roles; remote now rare", beginner_friendly="Some", requirements="Federal resume format",
    us_eligibility="Yes (citizenship often required)",
    published_pay="GS pay scales on listings", pay_source="Official",
    application_steps="Profile → federal resume → questionnaire → referral → interview",
    payment_and_fees="Free",
    worker_outcome_evidence="Jan 2025 executive order ended most federal remote work; hiring freeze → targeted 2026 thaw (10,475 open positions Feb 24, 2026)",
    evidence_strength="Strong", common_challenges="Few remote roles; long timelines",
    success_strategies="Look for 'Remote job: Yes' only from agencies hiring now; don't rely on it for urgent income",
    sources="https://www.hrdive.com/news/trump-eliminates-remote-work-for-feds-institutes-hiring-freeze/737841/ | https://data.opm.gov/explore-data/analytics/federal-recruitment")

add(platform="CareerOneStop / American Job Centers", category=CAT_C, subcategory="Free public reemployment services", status=APPLY,
    website="https://www.careeronestop.org", apply_link="https://www.careeronestop.org/WorkerReEmployment/",
    roles_and_tasks="Unemployment insurance finder, ~2,300 local American Job Centers, resume help, training funds, state job banks",
    beginner_friendly="Yes", requirements="None for self-service; some programs need eligibility",
    us_eligibility="Yes", published_pay="Free services", pay_source="Official (U.S. DOL)",
    application_steps="Use Worker ReEmployment site → file UI in your state → book an American Job Center appointment",
    payment_and_fees="Free", worker_outcome_evidence="Official federal program", evidence_strength="Strong",
    common_challenges="Mostly self-service", success_strategies="Ask about WIOA-funded training and free LinkedIn Learning access",
    sources="https://www.careeronestop.org/WorkerReEmployment/ | https://dol.gov/agencies/eta/american-job-centers")


for i, r in enumerate(ROWS, 1):
    r["id"] = f"OD{i:03d}"


def rows_as_dicts():
    return [{f: r[f] for f in FIELDS} for r in ROWS]
