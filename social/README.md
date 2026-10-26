# Next Offer Academy US: Social Content System

A low-cost daily pipeline for **@nextofferacademyus** (Instagram, TikTok, Threads):
calendar → sourced opportunity database → Claude generation → media rendering → automated fact-check → **human approval** → Buffer → publication log → performance tracker.

## Current status (Oct 26, 2026 · updated after Buffer connection)

| Piece | Status |
|---|---|
| 7 days of finished content (Oct 27 – Nov 2) | ✅ 7 Instagram carousels (49 slides), 7 TikTok MP4s (29–34 s, 1080×1920), 9 Threads posts; all pass automated checks; **all `needs_approval`** |
| 30-day calendar | ✅ `calendar/30_day_calendar.md` / `.csv` (43% jobs · 30% prep · 17% experience · 10% promo) |
| Templates | ✅ `templates/instagram_carousel_template.md`, `templates/tiktok_template.md`, `templates/brand.css` |
| Threads library | ✅ 33 posts in `threads/threads_library.md` |
| Content database | ✅ `data/content_db.json` (+ `.csv` view), `data/opportunities.json`, `data/publication_log.csv`, `data/performance_tracker.csv` |
| Daily generator | ✅ `scripts/pipeline.py` (Claude API), not yet run against the live API |
| **Buffer connection** | ✅ Connected through the Buffer MCP connector. Organization "My organization" (America/New_York). **TikTok @nextofferacademyus matched** (channel `6adea3562f1f5ed648d1a6bc`). **Instagram and Threads are not connected in Buffer yet.** Plan limits: 3 channels, 10 scheduled posts. |
| Buffer drafts | ✅ All 7 TikTok videos saved as **Buffer drafts** with their planned times (7:00 PM ET, Oct 27 – Nov 2). Status `draft`, nothing published. Media served from commit-pinned public URLs. IDs in `data/content_db.json` and `data/publication_log.csv`. |
| Automation (GitHub Actions / n8n) | 🟡 Configs written in `automation/`, **inactive** until you copy them into `.github/workflows/` |
| TikTok audio | 🟡 Videos have a silent track. Record the voiceover in `script.md` or finish in the TikTok app (see template) |
| Threads | 🟡 Disabled in `config/channels.json` until the account is connected to Buffer |

## Daily workflow

```
cron (GitHub Actions 8:47 AM ET, or n8n)
  └─ pipeline.py --verify       Claude writes IG + TikTok + Threads from the calendar row,
     │                          using ONLY facts in opportunities.json + WORKER_SUCCESS_RESEARCH.csv;
     │                          Claude web search re-checks each listing (adds warnings)
     └─ build_week.py           renders PNG/MP4/SRT, runs factcheck.py, saves status needs_approval
         └─ PR opened for review
you: approve.py approve <id> --by "<name>" [--live-checked]   ← job posts require a live re-check
  └─ merge → publish_approved.py --mode draft     → Buffer drafts (default)
             publish_approved.py --mode schedule  → Buffer schedule (locked until ALLOW_SCHEDULING=yes)
  └─ publication_log.csv · record_metrics.py → performance_tracker.csv
```

**Publishing an approved TikTok draft (via Claude + Buffer MCP):** approve it (`approve.py approve <id> --by <name> --live-checked`), then ask Claude to convert the Buffer draft to scheduled (`edit_post` with `saveToDraft: false`, keeping its time). Because the videos are silent, either replace the video with a voiced version first, or switch the draft to `schedulingType: notification` so Buffer reminds you to finish it in the TikTok app with a voiceover or sound.

**Safety rails built in**
- Automated checks: every dollar figure must exist in the research corpus; sources must be known research URLs; hype phrases blocked; length limits; media specs (IG 1080×1350, 2–10 slides; TikTok 1080×1920, 20–45 s); opportunity data older than 14 days must be re-verified.
- Nothing reaches Buffer without `status: approved`. Job posts can't be approved without `--live-checked`.
- Buffer posts are **drafts by default**. Scheduling needs both `--mode schedule` and `ALLOW_SCHEDULING=yes`.
- Posting only to channels whose Buffer name matches `@nextofferacademyus` (`config/channels.json`, `verified: true`).
- Edited content falls back to `needs_approval`.

## Setup to go live (about 30 minutes)

1. **Connect Buffer.** ✅ Done via MCP (TikTok). Still to do: connect Instagram (and Threads later) in Buffer. For unattended runs you also need:
   - **Buffer MCP in Claude:** add Buffer at <https://claude.ai/customize/connectors>, then start a new session. Claude can then list channels, create drafts and schedule through MCP. Or:
   - **Buffer API key** (needed for unattended runs): create one in Buffer's API settings (see <https://developers.buffer.com>). Then:
     ```bash
     export BUFFER_API_KEY=...            # never commit it
     python3 social/scripts/buffer_client.py introspect   # confirms createPost field names on your account
     python3 social/scripts/buffer_client.py channels     # lists channels, matches @nextofferacademyus, saves IDs
     ```
     If `introspect` shows different field names than `build_input()` uses (assets/metadata/draft flag), adjust `buffer_client.py` before the first send. Those field names come from Buffer's docs but haven't been tested live.
2. **Host media publicly.** ✅ The repo is public; media is served as `https://raw.githubusercontent.com/pms268-del/nextofferacademy/<commit-sha>/<path>` (pinned to a commit so it never changes). For automation set `MEDIA_BASE_URL` to that prefix, or copy `social/content/` to a public bucket (Cloudflare R2/S3) and point `MEDIA_BASE_URL` there.
3. **Approve week 1.** `python3 social/scripts/approve.py list`, open each listing, then `approve ... --live-checked`.
4. **Test with drafts.** `python3 social/scripts/publish_approved.py --dry-run`, then `--mode draft --only 2026-10-27-ig`. Check the draft in Buffer.
5. **Turn on daily generation.** Add repo secrets `ANTHROPIC_API_KEY` and `BUFFER_API_KEY`, and variable `MEDIA_BASE_URL`; copy `automation/github-actions/*.yml` to `.github/workflows/` on `main`.
6. **Only when you're ready for auto-scheduling:** set repo variables `PUBLISH_MODE=schedule` and `ALLOW_SCHEDULING=yes`.

## Cost estimate

- **Claude API** (`claude-opus-5-5`, effort medium; $4/M input, $20/M output): roughly 6–8K input and 4–6K output tokens per day ≈ **$0.10–0.15/day**, plus web-search verification (about $0.10–0.25/day). Roughly **$5–12/month**. Set `CONTENT_MODEL` to another model to change cost/quality.
- **GitHub Actions**: about 5–8 min/day, within the free tier for most accounts.
- **Buffer**: check your plan's channel and scheduled-post limits for 3 channels.

## Rebuild commands

```bash
python3 social/scripts/seed_opportunities.py   # refresh opportunity DB from us/OPPORTUNITY_DIRECTORY.csv
python3 social/scripts/make_calendar.py        # regenerate the 30-day calendar
python3 social/scripts/build_week.py           # re-render all media + checks (keeps approvals unless content changed)
python3 social/scripts/pipeline.py --date 2026-11-03 --dry-run   # inspect what Claude will receive
```

Requirements: Python 3.10+ with Pillow; Node + Playwright (Chromium); ffmpeg; `pip install anthropic` for `pipeline.py`.
