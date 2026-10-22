# Fact-Check Report: US Remote Job Playbook

*Next Software Academy · October 2026 edition · Research window: October 21–22, 2026*

This report documents how the playbook's claims were verified, what is strong, what is weak, and what remains unresolved. Read it before republishing or updating the guide.

## 1. Method

| Step | What was done |
|---|---|
| Platform discovery | Web searches for each platform's official site, help center, job board (Greenhouse, Lever, company portals), pay, eligibility, and process; follow-up searches for third-party reviews and news. |
| Worker evidence | Searches across news outlets (Business Insider, WSJ via secondary coverage, Bloomberg, ProPublica), review sites (Indeed, Glassdoor, Trustpilot), community forums (Upwork Community, Fiverr Community, Blind, Lemmy) and Reddit (via indexed mirrors). |
| Labeling | Every directory row has `status`, `evidence_strength`, `pay_source`, `verified_date`, `verification_method`, and `sources`. Every evidence row has `evidence_type`, `strength`, `source_date`, and `source_url`. |
| Single source of truth | `scripts/directory_data.py` and `scripts/evidence_data.py` generate both CSVs and all tables in the PDF, so the numbers in the book and the CSVs always match. |

### Environment limitations (important)

1. **No direct page fetching.** Outbound HTTP from the research environment was blocked (proxy 403, then DNS failures in the fetch tool). All verification relied on **search-engine results and their indexed snippets**. A page "verified" here means it was returned by the search index with content matching the claim on 2026-10-22, not that the page was opened and an application was clicked through.
2. **Reddit was not reachable** through the search tool (domain blocked). Reddit threads were read through indexed read-only mirrors (redlib/sentinel snapshots). The CSV cites the **original reddit.com path**. Re-verify those threads directly before quoting them publicly.
3. **No screenshots.** The brief asked for screenshots where possible. Because pages could not be loaded, none were captured. Recommended: add screenshots of each Apply Now application page before publication (see §5).

## 2. Status-label rules applied

- **Apply Now** requires (a) an open application route for US residents found in an official page or listing, **and** (b) credible evidence of past worker acceptance/payment/hiring (journalism, aggregated reviews, official program statements, or multiple consistent anecdotes).
- **Explore**: real organization; listing-specific, narrow, or thin worker-outcome evidence.
- **Caution**: material risk (upfront worker costs, pay disputes, legal complaints, very low volume, few remote roles).
- **Unavailable**: sign-ups closed or redirected.

Result: 71 entries, of which 30 are Apply Now, 34 Explore, 6 Caution and 1 Unavailable.

## 3. Strength of key claims

### Strong (official source or multiple independent sources)

| Claim | Source(s) |
|---|---|
| FTC task-scam growth (≈5,000 reports in 2023 → ≈20,000 in H1 2024; job-scam losses > $220M in H1 2024) | FTC press release, Dec 2024 |
| Prolific minimum $8/hr, recommended $12/hr | Prolific researcher help center |
| Mercor AI interview ~20 min, practice interview, redo before submit; weekly Stripe payouts | Mercor talent docs (URLs and content from the companion Indonesian edition's research log, 2026-10-21; not re-fetched in this session) |
| Outlier onboarding 30–90 min; weekly payments (Tuesdays) | Outlier official blog |
| Handshake AI Fellowship $50–125/hr, US-based grad students/grads; no guaranteed project; paid training exercise | Handshake help center + Cornell Graduate School posting |
| Alignerr AI Trainer (PhD) $30–150/hr US | Official Greenhouse listing |
| micro1 listings $20–98/hr and $30–80/hr | Official jobs.micro1.ai listings |
| Upwork Freelancer Plus $19.99/mo, 100 Connects; Basic 10 Connects/mo | Upwork pricing page |
| Liveops $25 background check, 25–34¢/talk-minute, no guaranteed earnings | Liveops FAQ and blog |
| Arise lawsuit / ProPublica investigation | ProPublica |
| xAI layoff of ≥500 generalist tutors (Sep 2025) | Business Insider via Reuters/AOL |
| Federal remote-work rollback (Jan 2025 EO) and 2026 targeted thaw; OPM 10,475 openings (Feb 24, 2026) | HR Dive, OPM data page |
| Remote = 8.4% of LinkedIn postings, 42% of applications | LinkedIn data via Sherwood News (publication date not confirmed; see §4) |

### Medium (single credible secondary source, or listing copies on aggregators)

- TELUS US Content Reviewer est. $14/hr ($0.2333/task), and Welo Data US Scout rater $14.50/hr W-2: job-board copies of official listings.
- DataAnnotation pay ($20+/hr generalist, $40+/hr coding/specialist), Starter Assessment rules: third-party reviews quoting the official FAQ.
- Fiverr 20% fee and 14-day clearance; Upwork 0–15% variable fee; Freelancer.com 10%/$5; Contra Pro pricing: third-party fee guides (some citing official pages).
- Customer-service employer pay ranges (Concentrix, TTEC, Foundever, Amazon, Apple): career blogs and aggregate salary sites, not official pay pages.
- Huntr Q2 2025 (68.5-day median to first offer); Greenhouse 2025 (≈70% call the market very competitive): vendor reports seen through summaries.

### Weak (anecdotal, promotional, or unverified)

- Individual Reddit/forum earnings and timelines (labeled ANECDOTE in the CSV).
- The Substack "barista hired in 6 days" case: the author sells a course; labeled as promotional.
- Belay VA pay (~$20/hr): a single anonymous report.
- Working Solutions and Uber AI Solutions pay: unverified; kept as Explore with "Not verified."
- Expert-network rates ($100–300/hr): advice-site estimates, not network disclosures.

## 4. Unresolved items and conflicts

| # | Item | Status / conflict | Recommended action |
|---|---|---|---|
| U1 | DataAnnotation eligible countries | Reported (US, UK, CA, AU, NZ, sometimes IE) by third parties; no official list found | Check the sign-up page country dropdown |
| U2 | Upwork freelancer service fee | Third parties report a variable 0–15%, and the Upwork pricing page says Plus members pay 0%; no single official statement of the full range was confirmed | Recheck upwork.com/legal and pricing before publishing |
| U3 | Fiverr seller-level thresholds | Conflicting third-party criteria | Not used in the book; confirm in Fiverr Help Center if added |
| U4 | Alignerr payment frequency | Weekly vs. bi-weekly conflict between sources | Left as "weekly or bi-weekly cycles reported" |
| U5 | Handshake AI visa eligibility | Cornell says F-1/OPT, J-1, H-1B accepted; a third-party tracker says some visas don't qualify | Book tells readers to check the current page |
| U6 | Handshake pay floor | Official FAQ says $50; a tracker cites $40 | Book uses the official $50–125/hr |
| U7 | LinkedIn remote share data date | Sherwood article date not visible in snippet (data described as stable since Nov 2023) | Confirm date; consider LinkedIn's latest Economic Graph release |
| U8 | Remotasks US status | Closure notice seen from Brazil (Aug 2026); US not tested | Labeled Unavailable/redirect to Outlier; verify from a US connection |
| U9 | Halluminate contractor route | No public contractor application found | Labeled Explore |
| U10 | Contra Pro price and client fees | Conflicting third-party figures | Book states "reported"; verify on contra.com |
| U11 | FlexJobs pricing | Several conflicting price points | Book cites the most common pattern and labels it Caution |
| U12 | Mercor "$1.5M per day" BI headline vs. Sacra's estimate of "$2M+ per day" | Conflicting estimates | Not used as a fact in the book |
| U13 | Surge AI / DataAnnotation relationship | Widely reported (lawsuit names "Surge Labs, Inc. dba DataAnnotation"); not confirmed on DataAnnotation's site | Book says "reported" |
| U14 | Apply links set to home/careers pages | Where a deep application URL could not be confirmed (e.g., Wyzant, Varsity Tutors, Respondent, GLG, Guidepoint, MarketerHire, Prolific participants, Arc.dev, Guru, PeoplePerHour, Invisible, Working Solutions, Clickworker, Dynamite Jobs, uTest), the link points to the official home/landing page | Replace with confirmed deep links after a manual click-through |
| U15 | Deep links not seen in search results but believed standard | upwork.com/nx/signup, fiverr.com/start_selling, toptal.com/talent/apply, tutor.com/apply, rev.com/freelancers, usertesting.com/get-paid-to-test, workhub.transcribeme.com, gotranscript.com/transcription-jobs, freelancer.com/signup, 99designs.com/designers, telusdigital.com/careers, careers.ttec.com, jobs.concentrix.com, foundever.com/careers, belaysolutions.com/careers/, x.ai/careers, crowdgen.com, uber.com/us/en/ai-solutions/ | Click-test each before publication; fix any 404 |
| U16 | Glassdoor/Indeed rating counts | Counts change daily; captured from snippets dated mid-2026 | Treat as approximate |

## 5. Pre-publication checklist

- [ ] Click every `apply_link` in `OPPORTUNITY_DIRECTORY.csv` from a US connection; record HTTP status and whether an Apply/Join button exists.
- [ ] Capture a screenshot of each Apply Now application page (date-stamped) for the PDF and the website.
- [ ] Re-check pay on every Apply Now listing (listings change weekly).
- [ ] Open each Reddit source directly and confirm the quoted content.
- [ ] Resolve U1–U16 above.
- [ ] Have a US tax professional review the tax paragraphs in Chapter 5 and the W-2 vs. 1099 table in Chapter 4.
- [ ] Re-run `python3 us/scripts/build.py` after edits, then spot-check the TOC page numbers.

## 6. What the book does **not** claim

- It does not promise employment, acceptance, project availability, or earnings.
- It does not present anecdotes as typical results; each anecdote is labeled.
- It does not contain fabricated listings, testimonials, interviews, or earnings. The resume "before/after" example and the mock-assessment answers are clearly marked as illustrative, original practice material, and the example interview answer notes that its numbers are illustrative.
- It does not reproduce any platform's proprietary assessment content.
