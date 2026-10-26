# Instagram Carousel Template

**Spec:** 1080×1350 PNG (4:5), 5–7 slides, brand CSS `templates/brand.css`, rendered by `scripts/render.py`.
Buffer posts carousels as `assets.images` (public URLs, order = slide order).

## Slide types (fields → what goes there)

| Type | Use for | Fields |
|---|---|---|
| `cover` (dark) | Slide 1, the hook | `kicker` (2–4 words, caps) · `title` (≤ 9 words) · `sub` (one sentence + "Checked <date>" for job posts) |
| `item` | One opportunity | `n` · `title` (platform) · `body` (what you do) · `pill` (pay/fact with attribution: "Listed:", "Reported:", "Per X FAQ:") · `catch` (the honest downside) · `src` |
| `tip` | One action step | `n` · `title` (imperative, ≤ 6 words) · `body` (≤ 30 words) |
| `stat` | One number that matters | `big` (≤ 8 chars) · `title` · `body` · `src` |
| `before` | Resume/proposal rewrites | `title` · `before` · `after` · `note` ("Illustrative example. Use your own real numbers.") |
| `cta` (dark) | Last slide | `title` · `body` · `action` ("Save this · Follow for verified openings") |

## Formulas that fit our pillars

**Verified opportunities (40%)**: cover → 3–5 `item` slides → `cta`
> Cover: "[N] [type of] jobs open to US residents" · sub: "The pay they actually list, and the catch. Checked [date]."

**Applications, CV & interviews (30%)**: cover → 4–5 `tip` (or 1 `before`) → `cta`
> Cover: "How to [pass/fix/write] [thing] in [time]"

**Worker experiences (20%)**: cover → `stat` slides alternating good/bad → `cta` with "the pattern"
> Cover: "What [workers] actually report" · sub: "The good and the bad, from reviews and reporting."

**Guide promotion (10%)**: cover → `stat` slides (what's inside) → "what it won't do" `tip` → `cta` "Link in bio"

## Caption template

```
[Hook line restating the cover promise] 👇

[3–5 line list: one line per slide, with attributed pay]

The honest part: [contract/no guaranteed work/state limits/unpaid tests].

[Checked <date>. Confirm on the official site before you apply.]

[Question or save prompt] 👇

#remotejobs #[pillar tag] #[audience tag]   ← 3–5 hashtags max
```

## Checklist before approval

- [ ] Every $ figure appears in the opportunity DB or evidence CSV (the automated check enforces this)
- [ ] Pay is attributed ("listed", "reported", "per Handshake's FAQ")
- [ ] Each opportunity has its catch
- [ ] Job listings re-opened today: link works, still open to US residents, pay unchanged
- [ ] No "guaranteed", "easy money", or income promises
- [ ] Alt text file present (`alt_text.txt`)
