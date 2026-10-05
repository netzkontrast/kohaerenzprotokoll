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

The prompt contains NOW.md's own words and paths, no corpus text, so handing it to
a session sends nothing that has not already left the container.
"""

from __future__ import annotations

import json
import re
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
    return {"source": "NOW.md § Half-done — where the next session starts", "sessions": sessions,
            "notes": notes, "standing": standing}


def quoted(said: str) -> str:
    return said if said[:1] in "„“\"" else f"„{said}“"


def prompt(s: dict, notes: list[dict], standing: list[dict]) -> str:
    """One session's prompt: self-contained, NOW.md's words, nothing from the corpus."""
    lines = [
        f"Session for {REPO}: {s['title']}",
        "",
        "Read NOW.md, CLAUDE.md and PRINCIPLES.md first; NOW.md wins where this prompt is older than it.",
        "",
        "The task, as NOW.md states it (§ Half-done):",
        plain(s["md"]),
        "",
        f"Start with: {s['next'] or '(NOW.md names no next step: read the item and ask)'}",
    ]
    if s["status"] != "ready":
        lines += ["", f"This item {s['because']} — put the question to the author and do not start what it gates."]
    if s["files"]:
        lines += ["", "Open first: " + ", ".join(s["files"])]
    if standing:
        lines += ["", "The author's standing instructions, newest first (NOW.md):"]
        lines += [f"- {x['date']} {quoted(x['said'])}" if x["date"] else f"- {x['said']}" for x in standing]
    if notes:
        lines += ["", "Binding on every session:"] + [f"- {plain(n['md'])}" for n in notes]
    lines += ["", "Claim the work before starting it: an open pull request naming it under a `Claim` heading.",
              "Before any pull request: the app-refresh skill (`.agents/skills/app-refresh/SKILL.md`); "
              "the pre-PR hook refuses a pull request whose app was not rebuilt and checked for this commit."]
    return "\n".join(lines)


# ---------------------------------------------------------------- selftest

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
    if derive("# Now\n")["sessions"]:
        fail.append("a NOW.md without the section yields sessions")
    return fail


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        fail = selftest()
        for f in fail:
            print(f"  FAILED  {f}")
        print(f"sessions: {'every rule held' if not fail else str(len(fail)) + ' case(s) failed'} (order, two Next forms, Open, gate, gate as step, files, notes, standing, prompt, empty)")
        return 1 if fail else 0
    plan = derive()
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
