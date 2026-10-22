# AI Career Prompts — US Remote Job Playbook

*Next Software Academy · October 2026 edition*

These prompts work in ChatGPT, Claude, Gemini, Microsoft Copilot or any capable chat assistant, including the free tiers. Copy everything inside the gray box, replace the `[BRACKETS]`, and paste.

**Three rules for every prompt**

1. **Truth only.** Every prompt tells the AI not to invent experience, titles, dates, numbers, degrees, or tools. If it adds something you did not do, delete it. A fabricated resume line can cost you the offer at background check or in the interview, and on AI-training platforms it can get you removed.
2. **You are the editor.** AI writes the first draft. You check every fact, and you make the final voice sound like you.
3. **Never paste secrets.** Leave out your SSN, date of birth, home address, account numbers, and any confidential employer data. Use "[City, ST]" for location.

> **AI-training platforms forbid AI on the job itself.** Use these prompts to prepare your resume, profile and practice. Do **not** use an AI assistant to write answers on a DataAnnotation, Outlier, Mercor, Alignerr, TELUS or similar assessment or task. Platforms detect it, and contractors have been removed for it.

---

## Part 1 — Resume & job matching

### P01 — Job Description Decoder

Use this first, on every job you care about.

```
You are a senior US recruiter. Analyze the job description below.

Return:
1. The 5 must-have qualifications (quote the exact wording).
2. The 5 nice-to-have qualifications.
3. The 12 most important keywords/phrases an ATS or recruiter would search for, exactly as written in the posting.
4. The real problem this hire is meant to solve, in one sentence.
5. Red flags or unclear points (pay, location limits, contractor vs W-2, unpaid tests, upfront fees).
6. Three questions I should be ready to answer in a screening call.

Job description:
"""
[PASTE FULL JOB DESCRIPTION]
"""
```

### P02 — Honest Fit Check

```
Compare my resume to this job description. Be blunt and specific.

Rules: Use only facts in my resume. Do not assume skills I have not listed.

Return a table: Requirement | Evidence from my resume (quote it) | Match (Strong / Partial / Missing) | How to close the gap honestly (reword, add a real project, or skip this job).
Then give an overall fit score from 1 to 10 and say whether I should apply, apply with a referral, or skip.

Job description:
"""
[PASTE]
"""
My resume:
"""
[PASTE]
"""
```

### P03 — ATS-Ready Resume Tailor

```
Act as a US resume writer who builds ATS-readable resumes.

Rewrite my resume for the job below. Rules:
- Use ONLY information in my resume and the extra notes I provide. Never invent employers, dates, titles, degrees, certifications, tools, or numbers. If a metric would help but I did not give one, insert [ADD METRIC?] instead of guessing.
- Single column, no tables, no text boxes, no icons, no headers/footers for contact info.
- Standard section headings: Summary, Skills, Experience, Education, Certifications (only if I have them), Projects (only if I have them).
- Mirror the job's exact keywords where they truthfully describe my work.
- Each bullet: strong verb + what I did + tool/method + result. Max 2 lines.
- Most relevant role gets 4–6 bullets; older roles 2–3.
- Keep it to 1 page if under 10 years of experience, otherwise max 2 pages.
- After the resume, list every change you made and every [ADD METRIC?] placeholder so I can verify.

Job description:
"""
[PASTE]
"""
My current resume:
"""
[PASTE]
"""
Extra true facts I can add (optional):
"""
[e.g., "Trained 4 new hires", "Handled ~60 tickets/day in Zendesk"]
"""
```

### P04 — Bullet Point Upgrader (with metric interview)

```
Here are weak resume bullets. For each one, ask me up to 3 short questions to uncover real scope and results (volume, time saved, money, quality, people, tools). Wait for my answers. Then rewrite each bullet using only my answers. Do not guess numbers.

Bullets:
[PASTE 3–8 BULLETS]
```

### P05 — Career-Switcher Translator

```
I am switching from [OLD FIELD/ROLE] to [TARGET ROLE]. Translate my experience into the language of the target role.

Rules: Only reframe what I actually did. Do not claim the target title. Flag any requirement I truly lack and suggest a small real project (under 10 hours) that would demonstrate it.

Return:
1. A 3-line summary positioning me for [TARGET ROLE].
2. 8 transferable-skill bullets mapped to target-role keywords.
3. A list of gaps + a mini-project for each.

My background:
"""
[PASTE RESUME OR DESCRIPTION]
"""
```

### P06 — New-Grad / No-Experience Resume Builder

```
I am a [student / recent graduate] with little formal work experience. Build a one-page US resume for [TARGET ROLE TYPE, e.g., "AI data annotator", "remote customer support", "junior data analyst"].

Use only what I give you: coursework, class projects, part-time jobs, volunteering, clubs, research, personal projects. Turn them into results-focused bullets. Put Education first. Add a Projects section. Do not invent anything; use [ADD DETAIL?] where something is missing.

My information:
"""
School, degree, graduation date, GPA (if 3.3+):
Relevant courses:
Projects (what, tools, outcome):
Jobs/volunteering (where, what you did, how often):
Skills and tools:
Languages:
"""
```

### P07 — Laid-Off Professional Repositioning

```
I was laid off from [COMPANY/INDUSTRY] after [X] years as [TITLE]. I am targeting (a) remote roles like [ROLE A], and (b) short-term income through expert AI-training work (Mercor, Alignerr, Handshake, micro1) and/or freelance consulting.

From my resume below, produce:
1. A one-line LinkedIn headline for each target (a) and (b).
2. A 4-sentence "expert profile" paragraph for AI-training platforms that names my specific domain knowledge (sub-fields, tools, regulations, document types I can judge).
3. A list of 10 specific topics I could credibly evaluate AI answers on.
4. A one-sentence, non-defensive way to explain the layoff.

Use only real facts. No invented achievements.

Resume:
"""
[PASTE]
"""
```

## Part 2 — Profiles, portfolio, cover letters

### P08 — LinkedIn Profile Rebuild

```
Rewrite my LinkedIn profile for recruiters searching for [TARGET ROLE] in remote US roles.

Deliver:
1. Headline (max 220 characters): role + specialty + proof + target. Give 3 options.
2. About section (180–260 words): first 2 lines must hook a recruiter; include 8–10 searchable keywords naturally; end with what I'm looking for and how to contact me (no phone number).
3. Experience: rewrite my 2 most recent roles in 3–5 bullets each.
4. Top 10 skills to list, ordered by recruiter search value.
5. A "Featured" section plan: 3 items I could add.

Only use facts from my resume. Flag anything you'd like me to confirm.

Resume:
"""
[PASTE]
"""
```

### P09 — Upwork / Fiverr / Contra Profile Builder

```
Create a freelance profile for [PLATFORM] selling [SERVICE] to [TARGET CLIENT TYPE].

Return:
1. Title (max 70 characters) that names the outcome and the niche. 3 options.
2. Overview (Upwork: 200–300 words) that starts with the client's problem, shows 2–3 proof points from my real experience, lists what's included, and ends with a clear call to action.
3. For Fiverr: gig title, 3 packages (Basic/Standard/Premium) with scope, delivery time, revisions, and starting prices based on my target hourly rate of $[RATE].
4. 5 FAQ entries.
5. 3 portfolio-piece ideas I can create this week from real or self-initiated work, clearly labeled as samples.

Rules: No fake reviews, clients, or credentials. If I have no clients yet, do not imply that I do.

My background and skills:
"""
[PASTE]
"""
```

### P10 — Portfolio Case Study Writer

```
Turn this project into a one-page portfolio case study.

Structure: Title (outcome-focused) · Context (who, what problem) · My role · Process (3–5 steps, tools used) · Result (real numbers or qualitative outcome; if self-initiated, say "self-initiated sample project") · What I'd do next · Link/visual suggestions.

Max 300 words. Use plain language a non-technical client understands. Do not exaggerate results.

Project notes:
"""
[PASTE NOTES, LINKS, NUMBERS]
"""
```

### P11 — Cover Letter / Application Note (short)

```
Write a cover letter for the job below in under 200 words.

Structure:
1. One sentence that names the role and a specific thing about the company (from the job post or their website text I paste).
2. Two short proof paragraphs, each tying one must-have requirement to a real result from my resume.
3. One sentence on why remote work suits how I work (async communication, time zone, tools).
4. Simple close.

No clichés ("I am writing to express my interest", "passionate", "team player"). No invented facts.

Job description:
"""
[PASTE]
"""
Company info (optional):
"""
[PASTE]
"""
My resume:
"""
[PASTE]
"""
```

### P12 — Upwork Proposal Writer

```
Write an Upwork proposal for the job post below. Max 150 words.

Structure:
- Line 1: restate the client's specific goal in my words (this is what shows in the preview, so make it count).
- Lines 2–3: how I would approach it in 3 concrete steps.
- Line 4: one relevant proof point or portfolio link from my real experience.
- Line 5: one smart question about their project.
- Close with availability.

No "Dear Sir/Madam", no generic intro about myself, no invented experience.

Job post:
"""
[PASTE]
"""
My relevant experience and portfolio links:
"""
[PASTE]
"""
```

### P13 — Pricing & Scope Calculator

```
Help me price a freelance service.

My target take-home hourly rate: $[X]. My estimate of hours: [Y]. Platform fee: [Upwork 0–15% / Fiverr 20% / Contra 0%]. I'm a 1099 contractor, so set aside ~25–30% for taxes (I will confirm with a tax professional).

Return:
1. The fixed price to quote so that after platform fee I still hit my target rate.
2. A 3-tier package version (good/better/best) with scope boundaries.
3. A one-paragraph scope statement listing what is NOT included and the revision policy.
4. A polite script for responding when a client asks for a discount.
```

## Part 3 — Interviews & assessments

### P14 — AI Interview Simulator (master prompt)

```
You are my interview coach and interviewer. Run a realistic mock interview, one question at a time.

SETTINGS
- Interview type: [Behavioral | Customer service | AI-training platform screening (e.g., Mercor/Alignerr/micro1 AI interview) | Freelance client discovery call | Startup founder interview | Technical/role-specific: ___]
- Target role: [ROLE] at [COMPANY or "a remote US company"]
- My level: [Beginner / Experienced professional]
- Number of questions: [6]
- My resume (for resume-based questions):
"""
[PASTE]
"""
- Job description (optional):
"""
[PASTE]
"""

RULES
1. Ask ONE question, then stop and wait for my answer.
2. After each answer, score it 1–5 on each: Relevance, Specificity (numbers, examples), Structure (STAR or clear logic), Conciseness (60–120 seconds spoken), Credibility (no vague claims).
3. Give: one thing that worked, the single most important fix, and a rewritten model answer using ONLY facts I gave (mark any assumed detail as [YOUR DETAIL]).
4. Ask one realistic follow-up question an interviewer would ask, then move on.
5. For "AI-training platform screening" mode: ask about my domain expertise in depth (explain a concept, judge a flawed answer, describe a past project step by step), as an AI interviewer would.
6. For "Freelance client" mode: play a client with a vague brief and a tight budget; reward me for clarifying questions and scoping.
7. At the end: overall score, my 3 recurring weaknesses, and a 15-minute drill plan to fix them.

Start with a one-line intro, then question 1.
```

### P15 — STAR Story Bank Builder

```
Help me build 8 STAR stories (Situation, Task, Action, Result) from my experience for behavioral interviews.

Cover: a conflict, a mistake, a tight deadline, a difficult customer, leading without authority, learning something fast, improving a process, handling ambiguity.

Ask me 2 questions per story to get real details. Then write each story in 120–150 words (spoken ~60–90 seconds). Use my facts only. Finish with a table mapping each story to 3 common questions it can answer.
```

### P16 — Assessment Practice Generator (AI-training)

```
Create a practice set that mirrors the style of AI-training platform assessments (writing, rating, fact-checking). DO NOT reproduce any real proprietary test.

Generate:
1. Two "compare two AI responses" items: a user prompt plus Response A and Response B with realistic flaws (a factual error, a missed instruction, unsafe advice, verbosity). Ask me to pick the better one and justify in 3–5 sentences.
2. One "write an ideal response" item with explicit constraints (word limit, format, audience).
3. One "fact-check this paragraph" item with 3 subtle errors.
4. One rubric-writing item: write 5 pass/fail criteria for grading answers to a given prompt.

After I answer each item, grade me against a rubric: instruction-following, factual accuracy, reasoning quality, clarity, and safety. Show a model answer.
```

### P17 — Salary, Rate & Offer Negotiation

```
I received an offer: [ROLE], [W-2 or 1099], $[PAY] per [hour/year], [hours/week], [benefits]. Market data I found: [PASTE RANGES + SOURCES].

1. Tell me whether this is low, fair, or strong, and why (consider 1099 self-employment tax and lack of benefits if contractor).
2. Draft a short, warm email asking for [TARGET] with one evidence-based reason.
3. Give me 3 non-salary items to ask for if pay can't move (start date, equipment stipend, schedule, guaranteed hours, review in 90 days).
```

## Part 4 — Networking & follow-up

### P18 — Personalized Outreach Generator

```
Write a LinkedIn connection note (max 300 characters) and a follow-up message (max 120 words) to [NAME], [TITLE] at [COMPANY].

Context about them (from their profile/posts):
"""
[PASTE 2–3 REAL DETAILS]
"""
My goal: [learn about the team / ask for a 15-minute chat / ask about a specific open role JOB-ID / ask for a referral after a prior chat].
About me in one line: [LINE].

Rules: reference one specific detail; one clear ask; easy to say yes or no; no flattery, no attachments, no "pick your brain."
Give 2 versions: warm and direct.
```

### P19 — Coffee-Chat Prep Sheet

```
I have a 20-minute informational call with [NAME], [TITLE] at [COMPANY]. Using the notes below, prepare:
1. A 30-second intro about me.
2. 8 smart questions (team priorities, how they hire, what great looks like, tools, remote culture).
3. 2 questions that naturally open a referral conversation without asking directly.
4. A thank-you message template to send within 24 hours.

Notes:
"""
[PASTE THEIR PROFILE + JOB POST + MY RESUME SUMMARY]
"""
```

### P20 — Weekly Pipeline Review

```
Here is my job/client pipeline for the week (paste table: company/platform, role, date applied, stage, next step, contact).

1. Identify stalled items (no movement in 7+ days) and draft one follow-up for each.
2. Rank my pipeline by probability of income in the next 30 days.
3. Tell me the 3 highest-value actions for next week, with time estimates.
4. Point out any pattern (e.g., applying without referrals, low response from one channel).

Pipeline:
"""
[PASTE]
"""
```

### P21 — PDF Export & Final QA Check

```
Review my final resume text for an ATS and a human reader. Check: consistent date format (Mon YYYY), consistent tense (past for old roles, present for current), no first-person pronouns, no typos, no unexplained acronyms, no orphan lines, contact line format "Name · City, ST · email · LinkedIn URL". List issues as a checklist; do not rewrite unless I ask.

Resume:
"""
[PASTE]
"""
```
