# How to Post: Simple Step-by-Step Guide

Your posts are made and waiting in **Buffer as drafts**. Nothing goes live until you finish it in the app yourself.

Every draft is set to **Notify Me** and tagged **"Native edit: add music"**. That means at posting time Buffer sends your phone a reminder, and you add the music and post from TikTok/Instagram.

## What's waiting (week of Oct 28)

| Day | TikTok (7:00 PM ET) | Instagram | Topic |
|---|---|---|---|
| Wed Oct 28 | video | Reel, **7:30 PM** | We fact-checked 3 viral remote job posts |
| Thu Oct 29 | video | Carousel, 12 PM | What AI training actually pays (with the catch) |
| Fri Oct 30 | video | Reel, 12 PM | 3 resume fixes in 20 seconds |
| Sat Oct 31 | video | Carousel, 12 PM | Real vs fake work-from-home job post |
| Sun Nov 1 | video | Reel, 12 PM | 152 applications, 6 interviews |
| Mon Nov 2 | video | Carousel, 12 PM | How to pass an AI video interview |
| Tue Nov 3 | video | Reel, 12 PM | New grad? 3 places to look this week |

Each day has a one-page **brief** in Buffer → **Ideas** (same title), and in `social/content/week2/<date>/BRIEF.md`. It has the music suggestion, the script, the links, and a **Variation B** you can film yourself if you prefer to be on camera.

---

## Every day (about 10 minutes)

### Step 1: Check the draft (2 min)
1. Open **Buffer** → **Drafts**. Open today's TikTok and Instagram draft.
2. Watch the video / swipe the slides and read the caption.
3. **Job posts (Oct 28, 29, Nov 3):** tap each link in the brief and make sure the job is still open and the pay matches. If not, tell Claude and it'll fix the post.

### Step 2: Approve and schedule (1 min)
1. In the draft, click **Schedule Post**. Keep the time. It stays in **Notify Me** mode.
2. Tell Claude *"approved Oct 29"* so the tracker is updated (or run `python3 social/scripts/status.py approve w2-2026-10-29-tt --by "your name" --live-checked`).

> **Free plan limit:** Buffer holds **10 scheduled posts** at once. Schedule 2–3 days ahead, not the whole week.

### Step 3: Finish in the app when Buffer notifies you (5 min)
1. Tap the Buffer notification on your phone (needs the Buffer mobile app with notifications on). Buffer opens the post so you can share the video into TikTok/Instagram and copy the caption.
2. **Add music:** tap **Add sound** (TikTok) or **Audio** (Instagram). Pick something from what the app offers. Business accounts only see licensed sounds, and that's the one you should use. The brief suggests a mood (e.g. "suspense build" or "upbeat lo-fi").
3. Optional: turn on **auto captions**, pick a cover (frame 1 works), add effects.
4. Paste the caption if it isn't there already, then **Post**.

**Want it in the app's own Drafts folder instead?** Buffer drafts don't go there automatically. Download the video from the brief → TikTok: **+ → Upload → add sound → Drafts**. Instagram: **+ → Reel → choose video → add audio → Save draft**.

### Step 4: Send Claude the link (30 sec)
Paste the live link to Claude: *"Oct 29 TikTok is live: (link)"*. A few days later: *"Oct 29 TikTok: 1,200 views, 40 saves"*. Or ask *"How did my posts do this week?"* and Claude pulls the numbers from Buffer.

---

## Threads and X (new personal accounts)

Not created yet. Start with `social/threads_x/SETUP.md` (usernames, bio, checklist, 30 min). The first 14 days of posts are in `social/threads_x/posts_14_days.md`. When you connect them in Buffer, tell Claude: it'll confirm the right account is connected and load the approved posts. Threads/X posts don't need music, so they're scheduled to post automatically after you approve them.

## Every week (one message to Claude)

The weekly prompt is in `social/WORKFLOW.md`. It reviews last week's real numbers, researches trends, makes the next 7 days, and saves Buffer drafts.

**Golden rules:** only real jobs from official sites, with the date checked. Never promise a job or income. Never ask anyone to pay. Never claim something happened to you that didn't.
