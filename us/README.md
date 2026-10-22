# US Remote Job Playbook (Next Software Academy)

A research-based career guide and workbook that helps US job seekers (laid-off workers, unemployed professionals, undergraduates, new graduates, and career switchers) find legitimate remote work, get accepted, and start earning. October 2026 edition; data verified October 22, 2026.

## Deliverables

| File | Contents |
|---|---|
| `US_REMOTE_JOB_PLAYBOOK.pdf` | The complete ebook (US Letter, clickable contents, PDF bookmarks, live source links): 12 chapters plus 3 appendices |
| `PLAYBOOK.md` | Editable manuscript, assembled from `manuscript/` |
| `OPPORTUNITY_DIRECTORY.csv` | 71 platforms/employers: status label, website, application link, roles, requirements, US eligibility, published pay, steps, fees, worker-outcome evidence, challenges, strategies, verification date, and sources |
| `WORKER_SUCCESS_RESEARCH.csv` | 51 documented worker outcomes and data points, each labeled by type, pattern, and strength, with source links |
| `AI_CAREER_PROMPTS.md` | 21 copy-paste prompts: resume, profile, portfolio, proposals, pricing, the AI Interview Simulator, assessments, networking |
| `ACTION_WORKBOOK.pdf` / `.md` | Exercises, templates, and 7-day / 30-day trackers |
| `FACT_CHECK.md` | Method, claim strength, conflicts, unresolved items, and a pre-publication checklist |
| `research/00_RESEARCH_LOG_US.md` | Raw research notes with source URLs |

## Editing and rebuilding

Sources of truth:
- Chapter text: `manuscript/*.md` (placeholders such as `{{TABLE:A}}`, `{{PRIORITY}}`, `{{CARDS}}`, `{{EVIDENCE}}`, `{{PROMPT:P03}}` are filled in at build time)
- Directory data: `scripts/directory_data.py`
- Evidence data: `scripts/evidence_data.py`
- Prompts: `AI_CAREER_PROMPTS.md`
- Design: `scripts/style.css`

```bash
python3 us/scripts/build.py   # regenerates both CSVs, PLAYBOOK.md, ACTION_WORKBOOK.md and both PDFs
```

Requirements: Python 3 (`beautifulsoup4`, `pypdf`), `pandoc`, and Node.js with Playwright + Chromium.
