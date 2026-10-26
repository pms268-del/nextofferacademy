# TikTok Video Template

**Spec:** 1080×1920 MP4 (H.264, 30 fps), 20–45 s, 6–9 scenes of 3–6 s each. Rendered by `scripts/render.py`:
on-screen headline + burned-in caption + progress bar, plus `tiktok_captions.srt` and `tiktok_cover.png`.
Safe zones: key text sits in the middle third; burned captions sit above the bottom ~470 px and clear of the right-side icons.

## Structure

| Scene | Seconds | Purpose | On-screen text (≤ 6 words) | Voiceover |
|---|---|---|---|---|
| 1 | ≤ 3.5 | **Hook**: tension or curiosity | "They pay you to train AI. Here's the catch." | Say the hook in full |
| 2–3 | 4–6 each | Fact #1 + its catch | Platform + attributed pay | One sentence each; spell numbers as spoken |
| 4–5 | 4–6 each | Fact #2 + its catch | | |
| 6 | 4–5 | The takeaway / what to do | "Apply to 3, not 1" | |
| 7 | 3 | CTA | "Follow for verified remote jobs" | "Follow for verified remote jobs every day." |

## Hook formulas (rotate; don't reuse within 14 days)

- "They pay you to [X]. Here's the catch."
- "Got laid off? [Group] is paying for what you already know."
- "Can you spot the mistake? [Companies] test for this."
- "Recruiters skip this [resume line]. Here's the fix."
- "[Stat] — here's what that means for your job search."
- "Read this before you pay for any 'job'."

## Audio: important

The rendered MP4 has a **silent audio track**. Choose one before publishing:
1. **Record the voiceover** from `script.md` (phone mic is fine) and replace the track:
   `ffmpeg -i tiktok_video.mp4 -i voice.m4a -map 0:v -map 1:a -c:v copy -shortest final.mp4`
2. **Use TikTok's in-app text-to-speech or a sound**: in Buffer, use TikTok's "notification" publishing so you finish the post in the app,
   or open the draft in TikTok directly. (Direct auto-publishing via Buffer would post the silent version.)
3. Generate a voiceover with a TTS tool you've approved, then use option 1's command.

## Caption

`[One-line takeaway]. [Source or "checked <date>"]. #remotejobs #[topic] #[audience] #jobsearch` (≤ 300 chars, 3–4 hashtags)

## Checklist before approval

- [ ] 20–45 s, 1080×1920 (automated check)
- [ ] Hook lands in the first 2–3 seconds
- [ ] Every number on screen is attributed in VO or caption
- [ ] Audio plan chosen (voiceover recorded, or in-app finish)
- [ ] Captions file uploaded or burned-in captions readable
