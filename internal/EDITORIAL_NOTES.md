# Editorial Notes — Revision 2 (22 Oktober 2026)

Internal only. Not distributed to readers.

## What changed
- Rebranded to Next Offer Academy; website constant `WEBSITE` in `scripts/build.py` (currently `nextoveracademy.id`, as supplied in the brief).
- Removed from reader-facing guide: methodology, evidence labels/grading, verification explanations, layoff positioning, pricing formula, directory-reading instructions, full directory tables, directory cards, evidence appendix, glossary.
- New reading flow: Pendahuluan → Peluang → Cara Diterima → Workflow CV AI → Wawancara → LinkedIn & Networking → Rencana Aksi → Keamanan → CTA website.
- Prompts consolidated into an end-to-end workflow (W1–W6) plus F1–F2, I1–I3, N1–N2 in `AI_CAREER_PROMPTS.md`.
- Added publicly reported interview questions (Mercor, Alignerr, micro1, Outlier, remote support), clearly separated from practice questions. Sources: `internal/RESEARCH_LOG.md` (section "REVISION RESEARCH") and `internal/RESEARCH_EVIDENCE.csv` (last 6 rows).
- Full database preserved in `REMOTE_WORK_DIRECTORY.csv` (102 rows) for the website.

## Accuracy guardrails kept in the reader text
- Eligibility caveats: "check location" box; platforms not accepting Indonesia (Prolific, Handshake AI, Uber AI Solutions, DataAnnotation per reports, Rev, User Interviews, OnlineJobs.ph).
- Compensation caveat: listing-based ranges only, no guaranteed hours/income.
- Safety: anti-scam checklist, OJK reporting contacts, confidentiality, AI-use prohibition during assessments.
- Website CTA phrased as "sedang menyiapkan / akan diperbarui"; does not claim the directory is live.

## Open items
- Confirm the domain spelling (`nextoveracademy.id` vs `nextofferacademy.id`) before publication.
- Previous fact-check gaps still apply: see `internal/FACT_CHECK_v1.md` §5.
- The example AI outputs in Bab 3 were generated for a fictional CV/job post and are labelled as such.
