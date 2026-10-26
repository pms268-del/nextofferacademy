# -*- coding: utf-8 -*-
"""Daily content pipeline: calendar row -> sourced context -> Claude -> media -> checks -> needs_approval.

  python3 social/scripts/pipeline.py                 # next un-generated calendar day
  python3 social/scripts/pipeline.py --date 2026-11-03
  python3 social/scripts/pipeline.py --date 2026-11-03 --verify   # also web-check listings with Claude web search
  python3 social/scripts/pipeline.py --date 2026-11-03 --dry-run  # print the prompt, no API call

Requires ANTHROPIC_API_KEY (and `pip install anthropic`). Never publishes: output lands in
social/generated/<date>.json and content_db.json with status needs_approval.
"""
import argparse
import csv
import datetime as dt
import json
import os
import subprocess
import sys

SCRIPTS = os.path.dirname(os.path.abspath(__file__))
SOCIAL = os.path.dirname(SCRIPTS)
REPO = os.path.dirname(SOCIAL)
GEN = os.path.join(SOCIAL, "generated")
MODEL = os.environ.get("CONTENT_MODEL", "claude-opus-5-5")
CHANNEL_TIMES = {"threads": ["09:00", "17:00"], "instagram": "12:00", "tiktok": "19:00"}

S = {"type": "string"}
SLIDE = {"type": "object", "additionalProperties": False,
         "properties": {k: S for k in ["type", "kicker", "title", "sub", "n", "body", "pill", "catch", "src", "big",
                                       "before", "after", "note", "action"]},
         "required": ["type", "kicker", "title", "sub", "n", "body", "pill", "catch", "src", "big", "before", "after", "note", "action"]}
SCENE = {"type": "object", "additionalProperties": False,
         "properties": {"text": S, "vo": S, "secs": {"type": "number"}}, "required": ["text", "vo", "secs"]}
SCHEMA = {"type": "object", "additionalProperties": False, "required": ["instagram", "tiktok", "threads"], "properties": {
    "instagram": {"type": "object", "additionalProperties": False, "required": ["topic", "slides", "caption", "hashtags", "sources"],
                  "properties": {"topic": S, "slides": {"type": "array", "items": SLIDE}, "caption": S,
                                 "hashtags": {"type": "array", "items": S}, "sources": {"type": "array", "items": S}}},
    "tiktok": {"type": "object", "additionalProperties": False, "required": ["topic", "hook", "scenes", "caption", "sources"],
               "properties": {"topic": S, "hook": S, "scenes": {"type": "array", "items": SCENE}, "caption": S,
                              "sources": {"type": "array", "items": S}}},
    "threads": {"type": "array", "items": {"type": "object", "additionalProperties": False, "required": ["topic", "text", "sources"],
                                           "properties": {"topic": S, "text": S, "sources": {"type": "array", "items": S}}}}}}

SYSTEM = """You write social content for Next Offer Academy US (@nextofferacademyus): a brand that helps US job seekers, new grads and laid-off professionals find LEGITIMATE remote work.

Voice: natural American English, warm, direct, practical. Sound like a knowledgeable friend, not a brand bot. No hype, no emojis walls, no "game-changer", no "unlock", no "in today's fast-paced world". Short sentences. Concrete details.

Hard rules (a human fact-checker rejects anything that breaks them):
1. Use ONLY facts, numbers, pay figures and URLs present in the CONTEXT block. Never invent opportunities, pay, statistics, testimonials or personal experiences. Never write "I tried" or imply the brand did something it didn't.
2. Attribute pay precisely: "listed", "reported", "per Handshake's FAQ", etc., matching the context's pay_source. Every post's `sources` must be URLs copied from the context.
3. Always include the honest catch (contract work, no guaranteed tasks, unpaid tests, state limits) when discussing an opportunity.
4. Never promise jobs or income. Never tell people to pay to get a job.
5. Adapt to each channel; never copy the same text across channels.

Formats:
- Instagram carousel: 5-7 slides. First slide type "cover" (kicker, title <= 9 words, sub). Middle slides use "item" (n, title, body, pill = pay/fact chip, catch, src), "tip" (n, title, body), "stat" (big = short number, title, body, src) or "before" (title, before, after, note). Last slide type "cta" (title, body, action). Use "" for unused fields. Caption <= 1,800 chars, ends with a question or save prompt; 3-5 hashtags.
- TikTok: 20-45 seconds total across 6-9 scenes. Scene 1 is the hook (<= 3.5 s). `text` is the big on-screen line (<= 6 words, may use one line break), `vo` is the spoken voiceover sentence (spell out numbers the way they're spoken), `secs` 3-6. End with a follow CTA. Caption <= 300 chars with 3-4 hashtags.
- Threads: 1-2 conversational posts, each <= 450 characters, plain text, no hashtags needed, useful on its own.
"""


def load_calendar():
    return list(csv.DictReader(open(os.path.join(SOCIAL, "calendar", "30_day_calendar.csv"), encoding="utf-8")))


def context_for(row):
    ops = {o["id"]: o for o in json.load(open(os.path.join(SOCIAL, "data", "opportunities.json"), encoding="utf-8"))["opportunities"]}
    ev = {e["id"]: e for e in csv.DictReader(open(os.path.join(REPO, "us", "WORKER_SUCCESS_RESEARCH.csv"), encoding="utf-8-sig"))}
    want_ops = [i for i in row["opportunity_ids"].split() if i]
    want_ev = [i for i in row["evidence_ids"].split() if i]
    db = json.load(open(os.path.join(SOCIAL, "data", "content_db.json"), encoding="utf-8"))
    day = dt.date.fromisoformat(row["date"])
    recent = [f"{p['date']} {p['channel']}: {p['topic']} | hook: {p.get('hook') or (p.get('caption') or p.get('text') or '')[:80]}"
              for p in db["posts"] if 0 < (day - dt.date.fromisoformat(p["date"])).days <= 14]
    return {"calendar": row,
            "opportunities": [{k: ops[i][k] for k in ("id", "platform", "status", "apply_link", "roles_and_tasks", "beginner_friendly",
                                                      "us_eligibility", "published_pay", "pay_source", "application_steps", "sources",
                                                      "verified_date")} for i in want_ops if i in ops],
            "evidence": [ev[i] for i in want_ev if i in ev],
            "recent_posts_do_not_repeat": recent}


def call_claude(ctx):
    import anthropic
    client = anthropic.Anthropic()
    user = ("Create today's content.\n\nCONTEXT (the only facts you may use):\n" + json.dumps(ctx, indent=1, ensure_ascii=False)
            + "\n\nWrite the Instagram carousel, the TikTok video, and the Threads posts for this calendar row. "
              "Avoid hooks and angles similar to recent_posts_do_not_repeat.")
    try:
        resp = client.beta.messages.create(
            model=MODEL, max_tokens=16000, system=SYSTEM,
            messages=[{"role": "user", "content": user}],
            output_config={"effort": "medium", "format": {"type": "json_schema", "schema": SCHEMA}},
            betas=["server-side-fallback-2026-07-01"], fallbacks="default",
        )
    except anthropic.RateLimitError as e:
        raise SystemExit(f"Rate limited, retry later: {e}")
    except anthropic.APIStatusError as e:
        raise SystemExit(f"Claude API error {e.status_code}: {e.message}")
    except anthropic.APIConnectionError as e:
        raise SystemExit(f"Network error reaching Claude API: {e}")
    if resp.stop_reason == "refusal":
        raise SystemExit("Model declined the request; review the calendar row.")
    if resp.stop_reason == "max_tokens":
        raise SystemExit("Output truncated (max_tokens); rerun.")
    text = "".join(b.text for b in resp.content if b.type == "text")
    return json.loads(text), resp.usage


def verify_listings(ctx):
    """Best-effort live check of each opportunity with Claude's web search. Adds warnings; never approves anything."""
    import anthropic
    if not ctx["opportunities"]:
        return []
    client = anthropic.Anthropic()
    ask = ("For each opportunity below, search the web for its CURRENT official listing/sign-up page. Report whether it still "
           "appears open to US residents and whether the pay shown in the official listing matches `published_pay`. "
           "Reply with ONLY a JSON array of {id, still_open: true|false|\"unknown\", pay_matches: true|false|\"unknown\", "
           "evidence_url, note}.\n\n" + json.dumps([{k: o[k] for k in ("id", "platform", "apply_link", "published_pay")}
                                                   for o in ctx["opportunities"]], indent=1))
    messages = [{"role": "user", "content": ask}]
    for _ in range(4):
        resp = client.messages.create(model=MODEL, max_tokens=8000, messages=messages, output_config={"effort": "medium"},
                                      tools=[{"type": "web_search_20260209", "name": "web_search", "max_uses": 8}])
        if resp.stop_reason != "pause_turn":
            break
        messages.append({"role": "assistant", "content": resp.content})
    text = "".join(b.text for b in resp.content if b.type == "text").strip()
    start, end = text.find("["), text.rfind("]")
    try:
        return json.loads(text[start:end + 1])
    except ValueError:
        return [{"id": "all", "still_open": "unknown", "pay_matches": "unknown", "note": "could not parse verifier output"}]


def to_posts(row, out, verification):
    d = row["date"]
    allowed = set()
    ctx_ops = json.load(open(os.path.join(SOCIAL, "data", "opportunities.json"), encoding="utf-8"))["opportunities"]
    for o in ctx_ops:
        allowed.update(o["sources"])
    for e in csv.DictReader(open(os.path.join(REPO, "us", "WORKER_SUCCESS_RESEARCH.csv"), encoding="utf-8-sig")):
        allowed.add(e["source_url"])
    oids = [i for i in row["opportunity_ids"].split() if i]

    def clean_sources(src):
        return [s for s in src if s in allowed]

    def strip(slide):
        return {k: v for k, v in slide.items() if v not in ("", None)}

    ig, tt = out["instagram"], out["tiktok"]
    posts = [
        {"id": f"{d}-ig", "date": d, "time_et": CHANNEL_TIMES["instagram"], "channel": "instagram", "format": "carousel",
         "pillar": row["pillar"], "topic": ig["topic"], "opportunity_ids": oids, "slides": [strip(s) for s in ig["slides"]],
         "caption": ig["caption"], "hashtags": ig["hashtags"][:5], "sources": clean_sources(ig["sources"]), "generated_by": MODEL},
        {"id": f"{d}-tt", "date": d, "time_et": CHANNEL_TIMES["tiktok"], "channel": "tiktok", "format": "video",
         "pillar": row["pillar"], "topic": tt["topic"], "opportunity_ids": oids, "hook": tt["hook"], "scenes": tt["scenes"],
         "caption": tt["caption"], "sources": clean_sources(tt["sources"]), "generated_by": MODEL},
    ]
    for i, th in enumerate(out["threads"][:2]):
        posts.append({"id": f"{d}-th{i + 1}", "date": d, "time_et": CHANNEL_TIMES["threads"][i], "channel": "threads",
                      "format": "text", "pillar": row["pillar"], "topic": th["topic"], "opportunity_ids": oids,
                      "text": th["text"], "sources": clean_sources(th["sources"]), "generated_by": MODEL})
    for p in posts:
        p["live_verification"] = verification
    return posts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date")
    ap.add_argument("--verify", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    cal = load_calendar()
    os.makedirs(GEN, exist_ok=True)
    if a.date:
        row = next(r for r in cal if r["date"] == a.date)
    else:
        today = dt.date.today().isoformat()
        row = next((r for r in cal if r["date"] >= today and r["status"] == "planned"
                    and not os.path.exists(os.path.join(GEN, f"{r['date']}.json"))), None)
        if row is None:
            print("No planned calendar day left to generate.")
            return
    ctx = context_for(row)
    if a.dry_run:
        print(SYSTEM + "\n\n" + json.dumps(ctx, indent=1, ensure_ascii=False))
        return
    verification = verify_listings(ctx) if a.verify else []
    out, usage = call_claude(ctx)
    posts = to_posts(row, out, verification)
    json.dump({"date": row["date"], "calendar": row, "usage": {"input_tokens": usage.input_tokens, "output_tokens": usage.output_tokens},
               "posts": posts}, open(os.path.join(GEN, f"{row['date']}.json"), "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print(f"Generated {len(posts)} posts for {row['date']} ({usage.input_tokens} in / {usage.output_tokens} out tokens)")
    subprocess.run([sys.executable, os.path.join(SCRIPTS, "build_week.py"), "--date", row["date"]], check=True)


if __name__ == "__main__":
    main()
