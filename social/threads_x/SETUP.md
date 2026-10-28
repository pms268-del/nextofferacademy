# Threads + X Setup Package (personal-style accounts)

These accounts don't exist yet. **You create them and log in; Claude never creates accounts.** They should be *you*: your real first name, your real face (or a plain avatar), connected openly to Next Offer Academy. No made-up persona, backstory or job history.

## 1. Username ideas (pick one available on both)

Replace `[name]` with your real first name or nickname.

| Option | Threads | X | Feel |
|---|---|---|---|
| A (recommended) | `[name].nextoffer` | `[name]_nextoffer` | Personal, ties to the brand |
| B | `[name]findsjobs` | `[name]findsjobs` | Curious, "I dig, you benefit" |
| C | `[name]onjobs` | `[name]onjobs` | Commentary/opinion angle |
| D | `itsnextoffer[name]` | `nextoffer[name]` | Brand-forward |

Threads uses your Instagram username by default. If you make Threads from **@nextofferacademyus**, it'll be a brand account, not a personal one. For a personal-style Threads, create a separate Instagram profile under your own name first, then join Threads with it.

## 2. Bio (pick one, ≤160 chars for X; Threads allows 150)

1. `Digging through remote jobs, AI training gigs & entry-level hiring so you don't have to. Sources included. Building @nextofferacademyus`
2. `Checking viral job posts before you apply to them. Remote, entry-level, AI gigs. US only. Part of @nextofferacademyus`
3. `Job search in 2026 is weird. I post what I find: real listings, scams, numbers. Next Offer Academy → nextofferacademy.us`

**Display name:** `[Your first name] | Next Offer Academy`
**Link:** `nextofferacademy.us`
**Location (optional):** `United States`

## 3. Positioning (one sentence)

> A real person who researches the US job market every day and shares what checks out (and what doesn't) about remote jobs, AI training gigs and entry-level hiring.

- **Is:** curious, specific, sourced, sometimes opinionated, asks good questions.
- **Isn't:** a guru, a "DM me for the link" account, a brand voice, or a fake success story.
- **Never:** invent experiences ("I got hired by…"), invent income, post unverified listings, or ask people to pay.

## 4. Setup checklist (about 30 minutes, owner)

- [ ] Pick a username (section 1) and check it's free on both platforms
- [ ] **X:** sign up at x.com with your email, set display name, bio, avatar, banner (can reuse a brand slide), link
- [ ] **X:** Settings → turn on two-factor authentication
- [ ] **Threads:** create or choose the Instagram profile you'll use (see note above), then open the Threads app → join with it
- [ ] **Threads:** set bio and link; profile **Public**
- [ ] Follow 20–30 accounts from section 5 so your feed teaches the algorithm your niche
- [ ] Post Day 1 by hand (it's an intro, best typed in your own words)
- [ ] **Buffer:** Channels → Connect channel → X, then Threads. Log in with the **new** accounts. ⚠️ Your Buffer plan allows **3 channels**, and Instagram + TikTok already use 2. Connecting both Threads and X needs a plan upgrade, or connect one now (we suggest X, since Threads can be posted from the app quickly) and post the other by hand.
- [ ] Tell Claude "Threads/X connected". Claude will run `list_channels`, confirm the handle matches the one you picked, write it into `social/config/channels.json` (`verified: true`), and load the approved Day 2–14 posts as **drafts**. Threads/X posts are scheduled directly (no Notify Me needed) only after you approve them.

## 5. Accounts and communities to follow

Only follow accounts you've checked are active and real. Starting points:

**Remote jobs & job boards (verify each before following):** Remote OK (`@remoteok` on X, per a 2026 job-account roundup), Wellfound, FlexJobs, Indeed, LinkedIn News, Y Combinator (`@ycombinator`) for startup hiring.
**People:** career coaches and recruiters who post specific, sourced advice. Find them with the searches below instead of trusting lists (many published lists are outdated).
**X Communities:** search Communities for `remote work`, `job search`, `new grads`, `tech jobs`, `freelance`. Join 2–3 that are active this week (look for posts in the last 24 hours).
**Threads:** follow topic tags `Job Search`, `Remote Work`, `Careers`, `Layoffs`; reply to posts there before posting your own.

## 6. Keywords and search queries (use daily, 10 minutes)

**X advanced search** (x.com/search, set to "Latest"):
- `"remote" ("hiring" OR "we're hiring") -crypto -dm lang:en min_faves:50`
- `("laid off" OR "job search") ("applications" OR "interviews") min_faves:200`
- `("AI training" OR "data annotation" OR "Outlier" OR "DataAnnotation") (pay OR rate) min_faves:20`
- `("new grad" OR "entry level") (job OR hiring) min_faves:100`
- `"ghosted" (recruiter OR interview) min_faves:100`

**Threads search:** `remote jobs`, `job search`, `ghosted after interview`, `entry level`, `AI training jobs`, `laid off`.

**Keywords to use naturally:** remote jobs, work from home, entry-level, new grad, AI training, data annotation, ghosted, job search, resume, LinkedIn, interview, layoffs, freelance, side gig, scam.

## 7. Conversation patterns that work on Threads/X (adapted, not copied)

| Pattern seen in popular posts | Our version |
|---|---|
| Frustration + strong opinion ("you don't own the company") | Mild, fair opinions about the market, tagged **owner voice** so you only post ones you believe |
| Specific result + timeframe + method (viral X ChatGPT thread) | Specific *researched* numbers + source, never fake personal results |
| "Who got hired?" honest-numbers threads | "How many applications are you at?" prompts |
| Short question that invites replies | 1 daily question post |

## 8. Daily routine (15 minutes)

1. Run 2 searches from section 6 and reply thoughtfully to 3–5 posts (replies grow new accounts faster than posts do).
2. Post (or approve in Buffer) that day's posts from `posts_14_days.md`.
3. Reply to every comment on your posts in the first hour.
4. Note one question people keep asking → it becomes a future post.

Posts: [`posts_14_days.md`](posts_14_days.md) (also `.csv` with status columns).
