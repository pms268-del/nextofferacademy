# Daily Content Workflow (revised Oct 28, 2026)

```
1 Trend research ─► 2 Pick formats ─► 3 Verify job facts ─► 4 Write ─► 5 Make media ─► 6 Buffer drafts
                                                                                          │
10 Track ◄── 9 Publish (owner, in-app) ◄── 8 Schedule: Notify Me / direct ◄── 7 Owner approval
```

| Step | Who | What | Where it's saved |
|---|---|---|---|
| 1. Trend research | Claude (+ owner 5 min/week) | Web search on TikTok topic pages, Reels, Threads, X and news; owner pastes TikTok Creative Center US top hashtags/songs weekly (Claude can't open Creative Center from the cloud) | `research/trend_reference_library.md` |
| 2. Pick formats | Claude | Match a proven pattern (myth check, job card, 3 fixes, receipts, real-vs-fake, opinion + question) to each topic | `scripts/week2_content.py` (one dict per topic) |
| 3. Verify facts | Claude, then owner | Every $ figure must be in the research corpus (`factcheck.py`); owner re-opens job links on the day | `research/week2_fact_sources.md` |
| 4. Write | Claude | Hook (first 3 s), script, captions, keywords, CTA, **variation A + B** | same dict |
| 5. Media | Claude | `python3 social/scripts/build_week2.py` → video (TikTok + Reel), carousel PNGs, captions.srt, BRIEF.md | `content/week2/<date>/` |
| 6. Buffer drafts | Claude (Buffer MCP) | Draft per platform, **Notify Me** mode, tag **Native edit: add music**, brief stored as a Buffer **Idea** | Buffer + `data/production_db.json` |
| 7. Approve | Owner | Watch the draft, check links; then `status.py approve <id> --by <name> [--live-checked]` or tell Claude "approve Oct 29" | `production_db.json` |
| 8. Schedule | Claude or owner | IG/TikTok: draft → scheduled **Notify Me** (keeps the time). Threads/X: scheduled **automatically** once connected and approved | Buffer |
| 9. Publish | Owner | Buffer notification → open the native app → add music/effects/cover → post | Instagram / TikTok |
| 10. Track | Owner pastes link + real numbers; Claude records | `record_metrics.py <id> --url ... --views ...` | `data/performance_tracker.csv` |

**Statuses:** `IDEA → DRAFT → REVIEW → APPROVED → READY TO PUBLISH → PUBLISHED` (`scripts/status.py`).
Current week-2 posts are all **REVIEW** (Buffer drafts exist; nothing approved or published).

**Per-post fields** (in `data/production_db.json`, flat view in `.csv`):
Platform · Topic · Reference URL · Hook · Script · Media · Audio Suggestion · Caption · Keywords · CTA · Status · Publish URL · Performance, plus app links, sources, variation B, fact-check result and Buffer IDs.

## Music: what's true and what isn't

- Buffer can't add music. Videos are exported silent on purpose.
- With **Notify Me**, Buffer sends a phone notification at the scheduled time; you open the post in TikTok/Instagram, pick a sound and finish there.
- **Buffer drafts do not appear in TikTok or Instagram's own Drafts folder.** To make a native draft: download the video (link in BRIEF.md) → open TikTok → + → Upload → add sound → **Drafts**. Instagram: + → Reel → pick the video → add audio → **Save draft**.
- Business accounts can only use TikTok's **Commercial Music Library** and Instagram's licensed library (Meta Sound Collection). Pick from what the app shows you; never import a song file. Each brief gives a mood/tempo and where to search, not a specific "trending" song we can't verify.

## Weekly review (Sundays, 20 minutes)

1. Owner: paste each live link + numbers from the app's analytics (or ask Claude to pull them from Buffer with `get_post includeMetrics`).
2. Claude ranks posts by **saves + shares per 1,000 views** and by **3-second hold** (TikTok "watched full video" / average watch time) where available.
3. Keep doing what wins: the top 2 hooks become templates for next week; the bottom 2 topics get a new format or are dropped.
4. Write the result in `data/weekly_review.md` (date, what we learned, what changes). **Only real numbers; blank stays blank.**
5. Refresh the trend library (Creative Center US: top 5 hashtags, top 5 commercial songs) and re-check every job link used next week.

## Weekly prompt for Claude

```
Run the weekly cycle for Next Offer Academy US.
1. Pull metrics for last week's published posts from Buffer and update the performance tracker (real numbers only).
2. Write the weekly review: best/worst hooks, formats and topics.
3. Research current US trends (TikTok topic pages, Reels, Threads, X, news) and update the trend library.
4. Make next week's 7 IG + 7 TikTok posts in social/scripts/ (variation A video + variation B script), verify every fact,
   build media, commit/push, then save Buffer drafts in Notify Me mode with the "Native edit: add music" tag and an Idea brief.
5. Draft 7 days of Threads/X posts. If those channels are connected, save them as Buffer drafts.
Do not publish or schedule anything. Show me the list.
```
