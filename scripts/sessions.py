"""The next sessions, derived from NOW.md — a view, never a backlog.

NOW.md is the handover between sessions, and its section `Half-done — where the
next session starts` lists the open work „in the order to act on it". This
script reads that section and nothing else, and turns each item into a session
an agent can be handed: a title, the step NOW.md names as next, the files it
points at, whether it waits on the author, and a prompt that carries the
standing instructions with it. It stores nothing — CLAUDE.md's rule that there
is no board, no status field and no backlog holds, because the plan is NOW.md
read again on every build: an item that leaves NOW.md leaves the plan.

    python3 scripts/sessions.py                 # the plan, one line per item
    python3 scripts/sessions.py --json          # what the app and the website serve
    python3 scripts/sessions.py --prompt <id>   # the prompt for one session, ready to paste
    python3 scripts/sessions.py board           # the plan against GitHub: claimed, free, active elsewhere
    python3 scripts/sessions.py selftest        # every rule, handed the case it exists for

## The rules, all of them written down

- **An item** is one top-level `- ` bullet of the section; its title is the first
  bold run, its id the title folded to a slug (stable while the title is).
- **Next** is the text after the first `**Next:**`, `**Next: …**`, `Next:` or
  `**Open:**` marker, to the end of its sentence. An item with no marker but a
  gate (below) is a session whose step is the sentence holding the gate. Any
  other item is a **note** (`The branch`, `Every check runs on GitHub`): it
  binds every session and is not one.
- **Waits on the author** when the item says so in words a person wrote there:
  „waits on", „only with the author's word", „the author's yes", „until the author".
  The phrase is reported with the status, so the rule can be read against the text.
- **Files** are backtick spans and markdown links that name a path that exists.

A prompt is a list of blocks (`blocks()`: header, read first, the author's own
instruction, task, next step, gate, files, standing instructions, notes, rules);
the app's start-prompt editor switches them on and off, and `free` is the prompt
for a session the author names in their own words.

**The board** (`board`, and the Now page live in the browser) sets the plan against GitHub's public API: an
open pull request claims a session by a line `Session: <id>` in its body or title (`CLAIM`), a branch pushed
within `ACTIVE_HOURS` is active, and active work that claims no planned session is listed apart. Nothing else is
inferred — a branch named like a session has not claimed it. When GitHub cannot be reached the board says the
live state is unknown and calls no session free. The session-start hook prints it.

The prompt contains NOW.md's own words and paths, no corpus text, so handing it to
a session sends nothing that has not already left the container.
"""

from __future__ import annotations

import json
import re
import urllib.request
from datetime import datetime, timedelta, timezone
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NOW = ROOT / "NOW.md"
SECTION = "Half-done"
STANDING = "The author's standing instructions"
NEXT = re.compile(r"\*\*(?:Next|Open):\*\*\s*|\*\*Next:\s*|(?<![\w*])Next:\s*")
WAITS = ("waits on", "only with the author's word", "the author's yes", "until the author", "wait on the yes")
REPO = "netzkontrast/kohaerenzprotokoll"
API = f"https://api.github.com/repos/{REPO}"
PAGE = "https://kohaerenzprotokoll.vercel.app/#/now"
# A claim is a line in an open pull request's body or title; the board and the Now page read the same pattern.
CLAIM = r"(?:^|\n)\s*Session:\s*`?([A-Za-z0-9][A-Za-z0-9-]*)`?"
ACTIVE_HOURS = 24


def section(text: str, head: str) -> str:
    """The body under the `##` or `###` heading starting with `head`, to the next heading of its level or above."""
    m = re.search(r"^(#{2,3}) " + re.escape(head) + r".*?$\n", text, re.M)
    if not m:
        return ""
    end = re.compile(r"^#{1," + str(len(m.group(1))) + r"} ", re.M).search(text, m.end())
    return text[m.end():end.start() if end else len(text)]


def bullets(body: str) -> list[str]:
    """Top-level `- ` items, continuation lines folded in."""
    items: list[str] = []
    for line in body.splitlines():
        if line.startswith("- "):
            items.append(line[2:].strip())
        elif items and line.startswith((" ", "\t")) and line.strip():
            items[-1] += " " + line.strip()
    return items


def plain(md: str) -> str:
    """Markdown to the words a person reads: links to their text, emphasis and code marks dropped."""
    md = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", md)
    return re.sub(r"\*\*|`", "", md).strip()


def slug(text: str) -> str:
    s = unicodedata.normalize("NFKD", plain(text).lower()).encode("ascii", "ignore").decode()
    out = ""
    for word in re.findall(r"[a-z0-9]+", s):
        if out and len(out) + 1 + len(word) > 48:
            break
        out = f"{out}-{word}" if out else word
    return out


def sentence(text: str) -> str:
    """Up to the end of the first sentence: a full stop, colon or em dash list end followed by a space and a capital, or the end."""
    m = re.search(r"(?<=[.!?])\s+(?=[A-Z„*(])", text)
    return text[:m.start()] if m else text


def files(md: str, root: Path = ROOT) -> list[str]:
    found: list[str] = []
    for cand in re.findall(r"`([^`\s]+)`", md) + re.findall(r"\]\(([^)\s]+)\)", md):
        cand = cand.rstrip(".,;:").split("#")[0]
        if "/" not in cand and not cand.endswith(".md"):
            continue
        base = cand.rstrip("/").rstrip("…").rstrip("-")
        if base and (root / base).exists() and cand not in found:
            found.append(cand)
    return found


def derive(text: str | None = None, root: Path = ROOT) -> dict:
    """The plan: sessions in NOW.md's order, the notes that bind them, the standing instructions."""
    text = text if text is not None else (root / "NOW.md").read_text(encoding="utf-8")
    sessions, notes, seen = [], [], set()
    for item in bullets(section(text, SECTION)):
        m = re.match(r"\*\*(.+?)\*\*", item)
        title = plain(m.group(1)).rstrip(".:") if m else plain(sentence(item))[:80]
        marker = NEXT.search(item)
        low = item.lower().replace("’", "'")
        waits = next((w for w in WAITS if w in low), "")
        if marker:
            nxt = sentence(item[marker.end():]).strip()
            if marker.group(0).startswith("**") and not marker.group(0).rstrip().endswith(":**"):
                nxt = nxt.replace("**", "", 1)  # `**Next: step 8**` — the marker took the opening `**`
        elif waits:  # no next step of its own: the gate is the step
            start = item.rfind(". ", 0, low.index(waits)) + 1
            nxt = sentence(item[start:].strip())
        else:
            notes.append({"title": title, "md": item})
            continue
        sid = slug(title) or f"item-{len(sessions) + 1}"
        while sid in seen:
            sid += "-2"
        seen.add(sid)
        sessions.append({"id": sid, "n": len(sessions) + 1, "title": title, "next": plain(nxt), "next_md": nxt,
                         "status": "waits on the author" if waits else "ready", "because": waits,
                         "files": files(item, root), "md": item})
    standing = []
    for item in bullets(section(text, STANDING)):
        m = re.match(r"(\d{4}-\d{2}-\d{2})\s+\*\*(.+?)\*\*", item)
        standing.append({"date": m.group(1), "said": plain(m.group(2))} if m else {"date": "", "said": plain(sentence(item))})
    for s in sessions:
        s["prompt"] = prompt(s, notes, standing)
        s["blocks"] = blocks(s, notes, standing)
    free = dict(FREE, blocks=blocks(FREE, notes, standing))
    return {"source": "NOW.md § Half-done — where the next session starts", "board": {"claim": CLAIM, "hours": ACTIVE_HOURS, "api": API, "page": PAGE, "repo": REPO}, "sessions": sessions,
            "notes": notes, "standing": standing, "free": free}


def quoted(said: str) -> str:
    return said if said[:1] in "„“\"" else f"„{said}“"


FREE = {"id": "free", "title": "", "md": "", "next": "", "status": "ready", "because": "", "files": []}
LABELS = {"head": "Header", "read": "Read first", "ask": "Your instruction", "task": "Task from NOW.md",
          "next": "Next step", "gate": "Gate", "files": "Files", "standing": "Standing instructions",
          "notes": "Binding notes", "rules": "Claim and app-refresh"}


def blocks(s: dict, notes: list[dict], standing: list[dict], ask: str = "") -> list[list[str]]:
    """One session's prompt as `[key, label, text]` blocks, in order. The app's editor switches them on and off
    and puts the author's own instruction (`ask`) in its place; `prompt` joins them all."""
    title = s["title"] or "a task the author names below"
    out = [["head", f"Session for {REPO}: {title}"],
           ["read", "Read NOW.md, CLAUDE.md and PRINCIPLES.md first; NOW.md wins where this prompt is older than it."]]
    if ask.strip():
        out.append(["ask", "The author's instruction for this session:\n" + ask.strip()])
    if s["md"]:
        out.append(["task", "The task, as NOW.md states it (§ Half-done):\n" + plain(s["md"])])
        out.append(["next", f"Start with: {s['next'] or '(NOW.md names no next step: read the item and ask)'}"])
    if s["status"] != "ready":
        out.append(["gate", f"This item {s['because']} — put the question to the author and do not start what it gates."])
    if s["files"]:
        out.append(["files", "Open first: " + ", ".join(s["files"])])
    if standing:
        out.append(["standing", "\n".join(["The author's standing instructions, newest first (NOW.md):"] +
                                           [f"- {x['date']} {quoted(x['said'])}" if x["date"] else f"- {x['said']}"
                                            for x in standing])])
    if notes:
        out.append(["notes", "\n".join(["Binding on every session:"] + [f"- {plain(n['md'])}" for n in notes])])
    sid = s.get("id") or "free"
    out.append(["rules", "Claim the work before starting it: open a pull request at once, its body under a `## Claim` heading "
                         f"holding the line `Session: {sid}`" + (" (or an id of your own for a task NOW.md does not name)" if sid == "free" else "")
                         + f" — the session board reads that line (`python3 scripts/sessions.py board`, and the Now page {PAGE}).\n"
                         "Before any pull request: the app-refresh skill (`.agents/skills/app-refresh/SKILL.md`); "
                         "the pre-PR hook refuses a pull request whose app was not rebuilt and checked for this commit."])
    return [[k, LABELS[k], t] for k, t in out]


def prompt(s: dict, notes: list[dict], standing: list[dict], ask: str = "") -> str:
    """One session's prompt: self-contained, NOW.md's words and the author's, nothing from the corpus."""
    return "\n\n".join(b[2] for b in blocks(s, notes, standing, ask))


# ---------------------------------------------------------------- the board

def fetch_live(timeout: float = 10.0) -> dict:
    """Open pull requests and the last day's pushes, from GitHub's public API. Never raises: a failure is
    returned as `ok: False` with its reason, because a board that cannot see GitHub must not call a session free."""
    def get(path: str):
        req = urllib.request.Request(API + path, headers={"Accept": "application/vnd.github+json", "User-Agent": "kp-sessions"})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return json.load(r)
    at = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    try:
        pulls = get("/pulls?state=open&per_page=100")
        activity = get("/activity?per_page=100&time_period=day")
    except Exception as e:  # noqa: BLE001 — any failure means the live state is unknown, said so
        return {"ok": False, "error": f"{type(e).__name__}: {e}"[:200], "at": at, "pulls": [], "activity": []}
    return {"ok": True, "error": "", "at": at,
            "pulls": [{"number": p["number"], "title": p["title"], "body": p.get("body") or "", "branch": p["head"]["ref"],
                       "url": p["html_url"], "updated": p["updated_at"]} for p in pulls],
            "activity": [{"ref": a["ref"], "type": a["activity_type"], "at": a["timestamp"], "sha": a["after"]} for a in activity]}


def _ts(iso: str) -> datetime:
    return datetime.strptime(iso, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)


def board(plan: dict, live: dict, now: datetime | None = None) -> dict:
    """The plan against what GitHub shows: which session an open pull request claims (`Session: <id>`), which
    branches were pushed within ACTIVE_HOURS, and the work that claims no planned session. Infers nothing else:
    a branch whose name resembles a session is not a claim."""
    now = now or datetime.now(timezone.utc)
    pattern = re.compile(CLAIM)
    branches: dict[str, dict] = {}
    for a in live.get("activity", []):
        if a["type"] != "push" or not a["ref"].startswith("refs/heads/") or a["ref"] == "refs/heads/main":
            continue
        if now - _ts(a["at"]) > timedelta(hours=ACTIVE_HOURS):
            continue
        b = branches.setdefault(a["ref"][len("refs/heads/"):], {"pushes": 0, "last": a["at"], "sha": a["sha"]})
        b["pushes"] += 1
        if a["at"] > b["last"]:
            b["last"], b["sha"] = a["at"], a["sha"]
    claims = []
    for p in live.get("pulls", []):
        ids = [m.lower() for m in pattern.findall(p["title"] + "\n" + p["body"])]
        b = branches.get(p["branch"])
        claims.append({"pr": p["number"], "title": p["title"], "url": p["url"], "branch": p["branch"], "ids": ids,
                       "last": b["last"] if b else p["updated"], "active": bool(b)})
    planned = {x["id"] for x in plan["sessions"]}
    rows = []
    for x in plan["sessions"]:
        by = [c for c in claims if x["id"] in c["ids"]]
        state = "unknown" if not live.get("ok") else ("claimed" if by else "free")
        rows.append({"n": x["n"], "id": x["id"], "title": x["title"], "status": x["status"], "next": x["next"],
                     "state": state, "by": by})
    claimed_branches = {c["branch"] for c in claims if set(c["ids"]) & planned}
    other = []
    for name, b in sorted(branches.items(), key=lambda kv: kv[1]["last"], reverse=True):
        if name in claimed_branches:
            continue
        pr = next((c for c in claims if c["branch"] == name), None)
        other.append({"branch": name, "last": b["last"], "pushes": b["pushes"], "sha": b["sha"],
                      "pr": pr["pr"] if pr else None, "title": pr["title"] if pr else "", "ids": pr["ids"] if pr else []})
    return {"ok": live.get("ok", False), "error": live.get("error", ""), "at": live.get("at", ""), "rows": rows,
            "other": other, "claims": claims, "hours": ACTIVE_HOURS}


def ago(iso: str, now: datetime | None = None) -> str:
    m = int(((now or datetime.now(timezone.utc)) - _ts(iso)).total_seconds() // 60)
    return f"{m} min ago" if m < 90 else f"{m // 60} h ago"


def board_text(b: dict, now: datetime | None = None) -> str:
    head = (f"Session board — NOW.md § Half-done against GitHub at {b['at']} ({len(b['claims'])} open pull requests, "
            f"{len(b['other']) + len({c['branch'] for r in b['rows'] for c in r['by']})} branches pushed in {b['hours']} h)")
    if not b["ok"]:
        head = f"Session board — GitHub not reached ({b['error']}): LIVE STATE UNKNOWN — do not assume a session is free"
    lines = [head]
    for r in b["rows"]:
        if r["by"]:
            c = r["by"][0]
            who = f"claimed by #{c['pr']} ({c['branch']}, {'pushed ' + ago(c['last'], now) if c['active'] else 'no push in ' + str(b['hours']) + ' h'})"
        else:
            who = {"free": "free", "unknown": "unknown"}[r["state"]]
        lines.append(f"{r['n']:>2}  {r['status']:<20} {who:<58} {r['id']}")
    if b["other"]:
        lines.append(f"Active in the last {b['hours']} h, claiming no planned session:")
        for o in b["other"]:
            pr = f"#{o['pr']} „{o['title'][:60]}“" + (f" Session: {', '.join(o['ids'])}" if o["ids"] else "") if o["pr"] else "no pull request"
            lines.append(f"  {o['branch']} — pushed {ago(o['last'], now)}, {pr}")
    silent = [o for o in b["other"] if not o["pr"]]
    if b["ok"] and silent and any(r["state"] == "free" and r["status"] == "ready" for r in b["rows"]):
        lines.append(f"CAUTION: {len(silent)} branch(es) were pushed in {b['hours']} h with no pull request, so no claim: "
                     f"{', '.join(o['branch'] for o in silent)}. A session marked free may be running there — look at "
                     "`git log origin/<branch>` before taking it, and open your claim pull request first.")
    lines.append(f"Claim before you start: a pull request whose body holds `Session: <id>`. The author's view: {PAGE}")
    return "\n".join(lines)


# ---------------------------------------------------------------- selftest

# One clock and one live state, built for the third session of whatever plan it is given. Shared by this
# self-test and by `ui.py`'s check that the Now page's JavaScript board answers exactly as `board()` does —
# two implementations of one rule, held together by one case.
FIXTURE_NOW = datetime(2026, 10, 5, 20, 0, tzinfo=timezone.utc)


def fixture_live(claimed: str) -> dict:
    return {"ok": True, "at": "2026-10-05T20:00:00Z", "pulls": [
        {"number": 7, "title": "Ingest", "body": f"## Claim\nSession: `{claimed}`\n", "branch": "claude/ingest", "url": "u7", "updated": "2026-10-05T19:00:00Z"},
        {"number": 8, "title": "My own task", "body": "Session: board-ui", "branch": "claude/ui", "url": "u8", "updated": "2026-10-05T19:00:00Z"}],
        "activity": [
        {"ref": "refs/heads/claude/ingest", "type": "push", "at": "2026-10-05T19:50:00Z", "sha": "a"},
        {"ref": "refs/heads/claude/ui", "type": "push", "at": "2026-10-05T19:40:00Z", "sha": "b"},
        {"ref": "refs/heads/claude/storyform", "type": "push", "at": "2026-10-05T19:30:00Z", "sha": "c"},
        {"ref": "refs/heads/claude/old", "type": "push", "at": "2026-10-03T19:30:00Z", "sha": "d"},
        {"ref": "refs/heads/claude/merged", "type": "pr_merge", "at": "2026-10-05T19:56:00Z", "sha": "g"},
        {"ref": "refs/heads/main", "type": "pr_merge", "at": "2026-10-05T19:55:00Z", "sha": "e"}]}


FIXTURE = """# Now

## The author's standing instructions

- 2026-10-05 **„keep the ui updated"** — the app is rebuilt.
- No corpus text leaves the container.

## Half-done — where the next session starts

- **The storyforms, step by step** (decision 025). Steps 0–16 are answered. **Next:** the players (W10), logline and genre. More after.
- **Step 8, E4** — designed. **Next: step 8, E4** — fixed pack, approved.
- **The ingest continues** one at a time. Next: `NOW.md` and `nowhere/at-all.md`, both claimed.
- **Entity lists**: lists exist. **Open:** the full run — it waits on the yes above.
- **HyperExtract** is measured. To resume it, only with the author's word: delete the STOP file.
- **The branch** carries the work; merge, never rebase.
  continued on a second line.

## Where things are
- `CLAUDE.md`
"""


def selftest() -> list[str]:
    plan = derive(FIXTURE)
    s = {x["id"]: x for x in plan["sessions"]}
    fail = []
    want = ["the-storyforms-step-by-step", "step-8-e4", "the-ingest-continues", "entity-lists", "hyperextract"]
    if list(s) != want:
        fail.append(f"sessions in NOW.md's order: want {want}, got {list(s)}")
    if s.get("the-storyforms-step-by-step", {}).get("next") != "the players (W10), logline and genre.":
        fail.append(f"**Next:** read to its sentence's end: got {s.get('the-storyforms-step-by-step', {}).get('next')!r}")
    if s.get("step-8-e4", {}).get("next_md", "").count("**") % 2:
        fail.append(f"**Next: …** leaves an unpaired `**`: got {s.get('step-8-e4', {}).get('next_md')!r}")
    if not s.get("step-8-e4", {}).get("next", "").startswith("step 8, E4"):
        fail.append(f"**Next: …** inside the bold: got {s.get('step-8-e4', {}).get('next')!r}")
    if s.get("entity-lists", {}).get("status") != "waits on the author" or s.get("entity-lists", {}).get("because") != "waits on":
        fail.append(f"a gated item: got {s.get('entity-lists', {}).get('status')!r} because {s.get('entity-lists', {}).get('because')!r}")
    hx = s.get("hyperextract", {})
    if hx.get("status") != "waits on the author" or not hx.get("next", "").startswith("To resume it"):
        fail.append(f"a gate without a marker is a gated session, its step the gate's sentence: got {hx.get('status')!r}, {hx.get('next')!r}")
    if s.get("the-storyforms-step-by-step", {}).get("status") != "ready":
        fail.append("an ungated item reported as waiting")
    if s.get("the-ingest-continues", {}).get("files") != ["NOW.md"]:
        fail.append(f"files: only paths that exist, got {s.get('the-ingest-continues', {}).get('files')}")
    if [n["title"] for n in plan["notes"]] != ["The branch"] or "second line" not in plan["notes"][0]["md"]:
        fail.append(f"an item with no marker is a note, continuation folded in: got {plan['notes']}")
    if [x["date"] for x in plan["standing"]] != ["2026-10-05", ""]:
        fail.append(f"standing instructions: got {plan['standing']}")
    p = s.get("entity-lists", {}).get("prompt", "")
    for words in ("Start with: the full run", "do not start what it gates", "2026-10-05 „keep the ui updated\"",
                  "The branch carries the work", "Claim the work"):
        if words not in p:
            fail.append(f"the prompt lacks {words!r}")
    ent = s.get("entity-lists", {})
    keys = [b[0] for b in ent.get("blocks", [])]
    if keys != ["head", "read", "task", "next", "gate", "standing", "notes", "rules"]:
        fail.append(f"blocks of a gated session: got {keys}")
    if "\n\n".join(b[2] for b in ent.get("blocks", [])) != ent.get("prompt"):
        fail.append("the prompt is not its blocks joined")
    asked = prompt(ent, plan["notes"], plan["standing"], ask="Nur das erste Dokument.")
    if "The author's instruction for this session:\nNur das erste Dokument." not in asked or \
            asked.index("Nur das erste") > asked.index("The task, as NOW.md"):
        fail.append("the author's instruction: missing, or not before the task")
    if [b[0] for b in plan["free"]["blocks"]] != ["head", "read", "standing", "notes", "rules"]:
        fail.append(f"the free prompt's blocks: got {[b[0] for b in plan['free']['blocks']]}")
    if "Session: entity-lists" not in ent.get("prompt", "") or "Session: free" not in "\n".join(b[2] for b in plan["free"]["blocks"]):
        fail.append("the rules block does not name the claim line `Session: <id>`")
    now, live = FIXTURE_NOW, fixture_live(plan["sessions"][2]["id"])
    bd = board(plan, live, now)
    st = {r["id"]: r for r in bd["rows"]}
    if st["the-ingest-continues"]["state"] != "claimed" or st["the-ingest-continues"]["by"][0]["pr"] != 7:
        fail.append(f"a `Session:` line in a pull request body (backticks too) claims its session: got {st['the-ingest-continues']}")
    if st["the-storyforms-step-by-step"]["state"] != "free":
        fail.append("a branch whose name resembles a session claimed it — no inference")
    if [o["branch"] for o in bd["other"]] != ["claude/ui", "claude/storyform"]:
        fail.append(f"active work outside the plan: want ui, storyform (newest first; old and main left out), got {[o['branch'] for o in bd['other']]}")
    off = board(plan, {"ok": False, "error": "URLError: no network", "at": "x"}, now)
    if any(r["state"] != "unknown" for r in off["rows"]) or "LIVE STATE UNKNOWN" not in board_text(off, now):
        fail.append("GitHub unreachable: a session reported free, or the board did not say the live state is unknown")
    live_silent = dict(live, activity=live["activity"] + [{"ref": "refs/heads/claude/quiet", "type": "push", "at": "2026-10-05T19:59:00Z", "sha": "f"}])
    if "CAUTION: 2 branch(es)" not in board_text(board(plan, live_silent, now), now) or "claude/quiet" not in board_text(board(plan, live_silent, now), now):
        fail.append("an active branch with no pull request beside a free ready session: no caution")
    if "claimed by #7 (claude/ingest, pushed 10 min ago)" not in board_text(bd, now):
        fail.append(f"board text: got {board_text(bd, now)!r}")
    if derive("# Now\n")["sessions"]:
        fail.append("a NOW.md without the section yields sessions")
    return fail


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        fail = selftest()
        for f in fail:
            print(f"  FAILED  {f}")
        print(f"sessions: {'every rule held' if not fail else str(len(fail)) + ' case(s) failed'} (order, two Next forms, Open, gate, gate as step, files, notes, standing, prompt, blocks, instruction, free, claim line, board: claim, no inference, other work, offline, caution, text, empty)")
        return 1 if fail else 0
    plan = derive()
    if argv[:1] == ["board"]:
        b = board(plan, fetch_live())
        print(json.dumps(b, ensure_ascii=False, indent=1) if "--json" in argv else board_text(b))
        return 0
    if "--json" in argv:
        print(json.dumps(plan, ensure_ascii=False, indent=1))
        return 0
    if "--prompt" in argv:
        i = argv.index("--prompt")
        want = argv[i + 1] if len(argv) > i + 1 else ""
        hit = [s for s in plan["sessions"] if s["id"] == want or str(s["n"]) == want]
        if not hit:
            print(f"sessions: no session {want!r}; ids: {', '.join(s['id'] for s in plan['sessions'])}", file=sys.stderr)
            return 1
        print(hit[0]["prompt"])
        return 0
    if not plan["sessions"]:
        print(f"sessions: NOW.md has no item with a next step under „{SECTION}“", file=sys.stderr)
        return 1
    for s in plan["sessions"]:
        print(f"{s['n']:>2}  {s['status']:<20}  {s['id']:<40}  {s['next'][:90]}")
    print(f"{len(plan['sessions'])} sessions, {len(plan['notes'])} notes binding all of them — from {plan['source']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
