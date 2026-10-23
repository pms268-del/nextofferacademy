# Editorial Notes — Revision 2 (22 Oktober 2026)

Internal only. Not distributed to readers.

## What changed
- Rebranded to Next Offer Academy; website constant `WEBSITE` in `scripts/build.py` (`nextofferacademy.id`).
- Removed from reader-facing guide: methodology, evidence labels/grading, verification explanations, layoff positioning, pricing formula, directory cards, evidence appendix, glossary.
- Revision 2b: full 102-platform directory list kept in the guide ("Direktori Lengkap Platform", generated from directory_data.py with research wording stripped). Per-platform detail (selection, payment, sources) goes to the website database via REMOTE_WORK_DIRECTORY.csv.
- Revision 2c (2026-10-23): domain set to nextofferacademy.id. Directory in the guide restored to full per-platform entries like the original (category, website, work type, skills, Indonesia status + scope, advertised pay, selection process, fees/payment, notes, data date + info links). Only technical fields (verification method, evidence strength, IDs) stay database-only.
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
- Confirm the domain spelling (`nextofferacademy.id`) — confirmed by client 2026-10-23.
- Previous fact-check gaps still apply: see `internal/FACT_CHECK_v1.md` §5.
- The example AI outputs in Bab 3 were generated for a fictional CV/job post and are labelled as such.
