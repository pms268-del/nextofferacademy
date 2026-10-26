# -*- coding: utf-8 -*-
"""Minimal Buffer GraphQL API client (https://developers.buffer.com).

Facts from Buffer's docs (checked 2026-10-26): POST https://api.buffer.com with
"Authorization: Bearer <BUFFER_API_KEY>"; get organization id from `account`, list
`channels(input: {organizationId})`; create posts with the `createPost` mutation
(text, channelId, schedulingType, mode, dueAt in UTC ISO-8601); media is passed as
public URLs in `assets` (no upload endpoint); per-network options go in `metadata`.

NOT yet verified against a live account (Buffer was unreachable from the build
environment): the exact `assets` shape, enum spellings, and the draft flag. Run
`python3 social/scripts/buffer_client.py introspect` once with your key; it prints
the real CreatePostInput fields so you can confirm before the first live call.

Commands:
  python3 social/scripts/buffer_client.py channels      # list channels, match @nextofferacademyus, save IDs
  python3 social/scripts/buffer_client.py introspect    # print createPost input schema
"""
import json
import os
import sys
import urllib.error
import urllib.request

ENDPOINT = os.environ.get("BUFFER_API_URL", "https://api.buffer.com")
SOCIAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHANNELS_CFG = os.path.join(SOCIAL, "config", "channels.json")


class BufferError(RuntimeError):
    pass


def gql(query, variables=None):
    key = os.environ.get("BUFFER_API_KEY")
    if not key:
        raise BufferError("BUFFER_API_KEY is not set")
    body = json.dumps({"query": query, "variables": variables or {}}).encode()
    req = urllib.request.Request(ENDPOINT, data=body, method="POST", headers={
        "Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            data = json.loads(r.read())
    except urllib.error.HTTPError as e:
        raise BufferError(f"HTTP {e.code}: {e.read()[:500]!r}") from e
    if data.get("errors"):
        raise BufferError(json.dumps(data["errors"])[:800])
    return data["data"]


def organizations():
    return gql("query { account { organizations { id name } } }")["account"]["organizations"]


def channels(org_id):
    q = """query($org: OrganizationId!) { channels(input: {organizationId: $org}) {
             id name displayName service isQueuePaused } }"""
    return gql(q, {"org": org_id})["channels"]


def norm(handle):
    return (handle or "").lower().lstrip("@").strip()


def match_channels(expected):
    """Return {service: channel} for channels whose name/displayName equals the expected handle."""
    found, seen = {}, []
    for org in organizations():
        for ch in channels(org["id"]):
            seen.append(ch)
            want = expected.get(ch["service"])
            if want and norm(want) in (norm(ch.get("name")), norm(ch.get("displayName"))):
                found[ch["service"]] = {**ch, "organizationId": org["id"]}
    return found, seen


CREATE_POST = """mutation($input: CreatePostInput!) {
  createPost(input: $input) {
    ... on PostActionSuccess { post { id status dueAt } }
    ... on MutationError { message }
  }
}"""


def build_input(post, channel_id, media_urls, mode="draft"):
    """Translate a content_db record into CreatePostInput. mode: draft | schedule."""
    text = post.get("caption") or post.get("text") or ""
    if post["channel"] == "instagram" and post.get("hashtags"):
        text += "\n\n" + " ".join(post["hashtags"])
    inp = {"text": text, "channelId": channel_id, "schedulingType": "automatic"}
    if mode == "schedule":
        inp.update({"mode": "customScheduled", "dueAt": post["scheduled_at_utc"]})
    else:
        inp.update({"mode": "addToQueue", "saveToDraft": True})
    if post["channel"] == "instagram":
        inp["assets"] = {"images": [{"url": u} for u in media_urls]}
        inp["metadata"] = {"instagram": {"type": "post", "shouldShareToFeed": True}}
    elif post["channel"] == "tiktok":
        inp["assets"] = {"videos": [{"url": u} for u in media_urls]}
    return inp


def create_post(inp):
    res = gql(CREATE_POST, {"input": inp})["createPost"]
    if "message" in res:
        raise BufferError(res["message"])
    return res["post"]


def introspect():
    q = """query { __type(name: "CreatePostInput") { inputFields { name type { name kind ofType { name kind } } } } }"""
    return gql(q)


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "channels"
    if cmd == "introspect":
        print(json.dumps(introspect(), indent=2))
        return
    cfg = json.load(open(CHANNELS_CFG, encoding="utf-8"))
    expected = {svc: c["handle"] for svc, c in cfg["channels"].items()}
    found, seen = match_channels(expected)
    print("Channels in this Buffer account:")
    for ch in seen:
        mark = "MATCH" if any(f["id"] == ch["id"] for f in found.values()) else "skip "
        print(f"  [{mark}] {ch['service']:<10} {ch.get('displayName') or ch.get('name')}  ({ch['id']})")
    for svc, c in cfg["channels"].items():
        c["buffer_channel_id"] = found.get(svc, {}).get("id")
        c["buffer_organization_id"] = found.get(svc, {}).get("organizationId")
        c["verified"] = svc in found
    json.dump(cfg, open(CHANNELS_CFG, "w", encoding="utf-8"), indent=2)
    missing = [s for s in cfg["channels"] if s not in found]
    print("Saved matches to config/channels.json." + (f" NOT FOUND: {', '.join(missing)}" if missing else ""))


if __name__ == "__main__":
    main()
