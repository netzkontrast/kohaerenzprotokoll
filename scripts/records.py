"""The sessions' records and the author's answers — what each session did, and what it asked.

The author's instruction of 2026-10-26 (`Plan/concept/session-apps_2026-10-26.md`): every session first says what it
did and thought, its priorities and what should follow; it asks the author through the app, each question with a
depth; the answers come back as files; a script turns every decision into the next start prompt. This module holds
the two kinds of file and the rules that refuse a bad one. It stores no plan: NOW.md stays the plan
(`scripts/sessions.py`), and a record is an account of what happened.

    Plan/sessions/<id>.json                       one per session, written by the session (`new` makes the skeleton)
    Plan/sessions/answers/<session>-<stamp>.json  one per save, written for the author (the app's export, later a PR)

A record:

    {"@type": "Session", "id": "<sessions.py slug>", "title": "…", "started": "YYYY-MM-DD", "ended": null | "YYYY-MM-DD",
     "branch": "…", "pr": 0 | null, "mandate": "…",
     "report": {"done": [{"text", "refs"?}], "thought": [{"text"}], "priorities": [{"rank", "text"}],
                "next": [{"text", "command"?}]},
     "app": null | {"name", "route": "#/…", "what"},
     "questions": [{"@type": "Question", "id": "Q-<session>-NN", "depth": 1 | 2 | 3, "text", "context",
                    "options": [{"key", "text", "refs"?}], "recommended"?, "concerns": [], "lands_in", "asked_on"}],
     "follows": ["<session id>"]}

**Depth** is how much a question asks of the author: 1 yes or no, 2 one of 2–4 options (the recommended one named),
3 the author's own words with the context needed to give them. An answer set:

    {"@type": "AnswerSet", "session": "<id>", "by": "author", "given_on": "YYYY-MM-DDTHH:MM:SSZ",
     "answers": [{"question": "Q-…", "yes"?: bool, "option"?: "<key>", "words"?: "…"}], "supersedes"?: ["<file>"]}

Answers are append-only: a changed answer is a new file that names the old one in `supersedes` (never an edit), so the
history stays and the prompt reads the newest. What an answer *settles* is not decided here: the question names where it
lands (`lands_in`), and the session that picks it up runs the tool that already exists for it (`weiche.py answer`,
`prose_rules.py confirm`, a decision file), citing the answer file. No record and no answer may carry an early name or
the trauma symbol (decision 028, `prose_rules.BARRED`/`TRAUMA`).

    python3 scripts/records.py                     # every record: report counts, questions open / answered
    python3 scripts/records.py show <id>           # one record as text
    python3 scripts/records.py new <id> --title "…" [--branch …] [--mandate …]   # the skeleton; refuses an existing id
    python3 scripts/records.py check               # the rules below, over every file (CI)
    python3 scripts/records.py selftest
"""

from __future__ import annotations

import json
import re
import sys
import tempfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))
FOLDER = ROOT / "Plan" / "sessions"
ID = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
QID = re.compile(r"^Q-[a-z0-9-]+-\d{2}$")
DAY = re.compile(r"^\d{4}-\d{2}-\d{2}$")
STAMP = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")
ANSWER_FILE = re.compile(r"^([a-z0-9-]+)-(\d{8}T\d{6}Z)\.json$")
REPORT = ("done", "thought", "priorities", "next")


def _barred(text: str) -> bool:
    import prose_rules
    return bool(prose_rules.BARRED.search(text) or prose_rules.TRAUMA.search(text))


def load(folder: Path | None = None) -> dict:
    """{"records": [...], "answers": [...], "problems": [(file, why)]} — read only, nothing judged but the JSON."""
    folder = folder or FOLDER
    out = {"records": [], "answers": [], "problems": []}
    for p in sorted(folder.glob("*.json")) if folder.is_dir() else []:
        try:
            rec = json.loads(p.read_text(encoding="utf-8"))
            rec["_file"] = p
            out["records"].append(rec)
        except ValueError as exc:
            out["problems"].append((p, f"not JSON: {exc}"))
    adir = folder / "answers"
    for p in sorted(adir.glob("*.json")) if adir.is_dir() else []:
        try:
            ans = json.loads(p.read_text(encoding="utf-8"))
            ans["_file"] = p
            out["answers"].append(ans)
        except ValueError as exc:
            out["problems"].append((p, f"not JSON: {exc}"))
    return out


def questions(data: dict) -> dict[str, dict]:
    return {q["id"]: dict(q, session=r["id"]) for r in data["records"] for q in r.get("questions", []) if isinstance(q, dict) and "id" in q}


def _replaced(data: dict) -> set[tuple[str, str]]:
    """(file, question) pairs a later file replaces: it names the file in `supersedes` and answers that question again.
    A superseded file's other answers stand — a revision replaces what it re-answers, nothing else."""
    out = set()
    for a in data["answers"]:
        again = {x.get("question", "") for x in a.get("answers", [])}
        for old in a.get("supersedes", []):
            out |= {(old, q) for q in again}
    return out


def state(data: dict) -> dict[str, dict]:
    """Per question id: the newest answer not replaced by a revision, with its file — or none (open)."""
    gone = _replaced(data)
    out: dict[str, dict] = {}
    for a in sorted(data["answers"], key=lambda a: a.get("given_on", "")):
        for x in a.get("answers", []):
            q = x.get("question", "")
            if (a["_file"].name, q) not in gone:
                out[q] = dict(x, file=a["_file"], given_on=a.get("given_on", ""), session=a.get("session", ""))
    return out


def _rel(p: Path, root: Path) -> str:
    try:
        return p.relative_to(root).as_posix()
    except ValueError:
        return p.as_posix()


def problems(data: dict | None = None, root: Path = ROOT) -> list[str]:
    """Every rule, over every record and answer file. An empty list is the only pass."""
    data = data if data is not None else load()
    out = [f"{_rel(p, root)}: {why}" for p, why in data["problems"]]
    ids = set()
    seen_q: dict[str, str] = {}
    for r in data["records"]:
        f = _rel(r["_file"], root)
        rid = r.get("id", "")
        if r.get("@type") != "Session":
            out.append(f"{f}: @type is not Session")
        if not ID.match(rid or "") or rid != r["_file"].stem:
            out.append(f"{f}: id {rid!r} is not a slug or not the file's name")
        ids.add(rid)
        for key in ("title", "started", "mandate"):
            if not str(r.get(key) or "").strip():
                out.append(f"{f}: {key} is empty")
        if r.get("started") and not DAY.match(str(r["started"])):
            out.append(f"{f}: started is not YYYY-MM-DD")
        if r.get("ended") and not DAY.match(str(r["ended"])):
            out.append(f"{f}: ended is not YYYY-MM-DD")
        rep = r.get("report") or {}
        for part in REPORT:
            items = rep.get(part)
            if not isinstance(items, list) or not items or any(not str((x or {}).get("text") or "").strip() for x in items):
                out.append(f"{f}: report.{part} is missing or has an item without text — a session says first what it did, thought, ranks and leaves next")
        ranks = [x.get("rank") for x in rep.get("priorities") or [] if isinstance(x, dict)]
        if ranks and ranks != list(range(1, len(ranks) + 1)):
            out.append(f"{f}: priorities are not ranked 1..{len(ranks)} in order")
        for x in rep.get("done") or []:
            for ref in (x or {}).get("refs", []):
                if not (root / ref.split(":")[0]).exists():
                    out.append(f"{f}: done names {ref}, which does not exist")
        app = r.get("app")
        if app is not None and (not isinstance(app, dict) or not str(app.get("name") or "").strip()
                                or not str(app.get("route") or "").startswith("#/")):
            out.append(f"{f}: app needs a name and a route starting with #/")
        for q in r.get("questions", []):
            qid = q.get("id", "")
            where = f"{f} {qid or '(no id)'}"
            if not QID.match(qid) or not qid.startswith(f"Q-{rid}-"):
                out.append(f"{where}: id must be Q-{rid}-NN")
            if qid in seen_q:
                out.append(f"{where}: also asked in {seen_q[qid]}")
            seen_q[qid] = f
            d = q.get("depth")
            if d not in (1, 2, 3):
                out.append(f"{where}: depth must be 1, 2 or 3")
            if not str(q.get("text") or "").strip():
                out.append(f"{where}: no question text")
            opts = q.get("options") or []
            keys = [o.get("key") for o in opts if isinstance(o, dict)]
            if d == 2:
                if not 2 <= len(opts) <= 4 or len(set(keys)) != len(keys) or any(not str(o.get("text") or "").strip() for o in opts):
                    out.append(f"{where}: depth 2 needs 2–4 options with distinct keys and text")
                if q.get("recommended") and q["recommended"] not in keys:
                    out.append(f"{where}: recommended {q['recommended']!r} is not an option")
            if d == 3 and not str(q.get("context") or "").strip():
                out.append(f"{where}: depth 3 gives the context the answer needs")
            for o in opts:
                for ref in o.get("refs", []):
                    if not (root / ref.split(":")[0]).exists():
                        out.append(f"{where}: option {o.get('key')} cites {ref}, which does not exist")
            lands = q.get("lands_in", "")
            if not lands or not (root / lands).exists():
                out.append(f"{where}: lands_in {lands!r} does not exist — an answer must land somewhere a tool or a person carries it")
            if not DAY.match(str(q.get("asked_on") or "")):
                out.append(f"{where}: asked_on is not YYYY-MM-DD")
        text = json.dumps({k: v for k, v in r.items() if k != "_file"}, ensure_ascii=False)
        if _barred(text):
            out.append(f"{f}: carries an early name or the trauma symbol (decision 028) — never written")
    for r in data["records"]:
        for other in r.get("follows", []):
            if other not in ids:
                out.append(f"{_rel(r['_file'], root)}: follows {other!r}, which has no record")
    qs = questions(data)
    names = {a["_file"].name for a in data["answers"]}
    answered_in: dict[str, list[str]] = {}
    for a in data["answers"]:
        f = _rel(a["_file"], root)
        m = ANSWER_FILE.match(a["_file"].name)
        if a.get("@type") != "AnswerSet":
            out.append(f"{f}: @type is not AnswerSet")
        if not m or m.group(1) != a.get("session"):
            out.append(f"{f}: name must be <session>-<YYYYMMDDTHHMMSSZ>.json for its session")
        if a.get("session") not in ids:
            out.append(f"{f}: session {a.get('session')!r} has no record")
        if a.get("by") != "author":
            out.append(f"{f}: by must be author — an answer is the author's words, never a session's")
        if not STAMP.match(str(a.get("given_on") or "")):
            out.append(f"{f}: given_on is not YYYY-MM-DDTHH:MM:SSZ")
        for s in a.get("supersedes", []):
            if s not in names:
                out.append(f"{f}: supersedes {s}, which is not an answer file")
        if not a.get("answers"):
            out.append(f"{f}: holds no answer")
        for x in a.get("answers", []):
            qid = x.get("question", "")
            q = qs.get(qid)
            if q is None:
                out.append(f"{f}: answers {qid!r}, which no record asks")
                continue
            if q["session"] != a.get("session"):
                out.append(f"{f}: answers {qid}, a question of {q['session']} — an answer set answers its own session")
            answered_in.setdefault(qid, []).append(a["_file"].name)
            d = q.get("depth")
            if d == 1 and not isinstance(x.get("yes"), bool):
                out.append(f"{f} {qid}: depth 1 is answered yes (true) or no (false)")
            if d == 2 and x.get("option") not in [o.get("key") for o in q.get("options", [])]:
                out.append(f"{f} {qid}: depth 2 is answered with one of the options")
            if d == 3 and not str(x.get("words") or "").strip():
                out.append(f"{f} {qid}: depth 3 is answered in the author's words")
        if _barred(json.dumps({k: v for k, v in a.items() if k != "_file"}, ensure_ascii=False)):
            out.append(f"{f}: carries an early name or the trauma symbol (decision 028) — never written")
    gone = _replaced(data)
    for qid, files in answered_in.items():
        live = [x for x in files if (x, qid) not in gone]
        if len(live) > 1:
            out.append(f"{qid}: answered in {', '.join(live)} and none supersedes the other — a changed answer names the old file")
    return out


# --- the prompt's blocks ---------------------------------------------------------------

def blocks(data: dict | None = None) -> list[list[str]]:
    """`[key, text]` for sessions.py: the newest record's report, the answers given, the questions still open,
    the sessions' apps. Empty when there is no record. Only the records' words, never corpus text."""
    data = data if data is not None else load()
    recs = [r for r in data["records"] if isinstance(r.get("report"), dict)]
    if not recs:
        return []
    recs.sort(key=lambda r: (r.get("ended") or "9999", r.get("started") or ""))
    last = recs[-1]
    rep = last["report"]
    lines = [f"What the last session reported (Plan/sessions/{last['id']}.json — {last.get('title', '')}):"]
    for part, head in (("done", "Done"), ("thought", "Thought"), ("priorities", "Priorities"), ("next", "Next")):
        items = rep.get(part) or []
        lines.append(f"{head}:")
        for x in items:
            mark = f"{x['rank']}. " if part == "priorities" and x.get("rank") else "- "
            lines.append(f"  {mark}{x.get('text', '')}" + (f" (`{x['command']}`)" if x.get("command") else ""))
    out = [["report", "\n".join(lines)]]
    qs, st = questions(data), state(data)
    given = [(qid, st[qid]) for qid in qs if qid in st]
    if given:
        rows = ["Decided by the author in the app — fold each into the tool its question names before anything else:"]
        for qid, x in sorted(given, key=lambda t: t[1]["given_on"]):
            q = qs[qid]
            said = "yes" if x.get("yes") is True else "no" if x.get("yes") is False else x.get("option", "")
            words = f" „{x['words']}“" if x.get("words") else ""
            rows.append(f"- {qid} (depth {q['depth']}) {said}{words} — lands in {q.get('lands_in')}; "
                        f"answer file {_rel(x['file'], ROOT)}, given {x['given_on'][:10]}")
        out.append(["decided", "\n".join(rows)])
    open_q = [q for qid, q in qs.items() if qid not in st]
    if open_q:
        rows = ["Still open — do not ask again, carry them:"]
        rows += [f"- {q['id']} (depth {q['depth']}, from {q['session']}): {q['text']}" for q in open_q]
        out.append(["open", "\n".join(rows)])
    apps = [r for r in data["records"] if r.get("app")]
    if apps:
        rows = ["Sessions with an app of their own (extend, do not duplicate):"]
        rows += [f"- {r['app']['name']} ({r['app']['route']}) — {r['app'].get('what', '')} · {r['id']}" for r in apps]
        out.append(["apps", "\n".join(rows)])
    return out


# --- the verbs ---------------------------------------------------------------------------

def new(rid: str, title: str, branch: str = "", mandate: str = "", today: str | None = None,
        folder: Path | None = None) -> Path:
    """The skeleton of a record. The report's four parts are left empty on purpose: `check` refuses the record until the
    session has written what it did, thought, ranked and leaves next."""
    folder = folder or FOLDER
    if not ID.match(rid):
        raise ValueError(f"{rid!r} is not a slug — use the id sessions.py gives the NOW.md item")
    path = folder / f"{rid}.json"
    if path.exists():
        raise ValueError(f"{_rel(path, ROOT)} exists — a record is written once and then edited, not made again")
    rec = {"@type": "Session", "id": rid, "title": title, "started": today or date.today().isoformat(), "ended": None,
           "branch": branch, "pr": None, "mandate": mandate,
           "report": {k: [] for k in REPORT}, "app": None, "questions": [], "follows": []}
    folder.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(rec, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return path


def show(rid: str, data: dict | None = None) -> str:
    data = data if data is not None else load()
    r = next((x for x in data["records"] if x.get("id") == rid), None)
    if r is None:
        return f"records: no record {rid!r}"
    st = state(data)
    lines = [f"{r['id']} — {r.get('title', '')}", f"  {r.get('started')} → {r.get('ended') or 'open'} · branch {r.get('branch') or '—'} · PR {r.get('pr') or '—'}"]
    for part in REPORT:
        lines.append(f"  {part}:")
        lines += [f"    - {x.get('text', '')}" for x in (r.get("report") or {}).get(part, [])]
    if r.get("app"):
        lines.append(f"  app: {r['app']['name']} {r['app']['route']}")
    for q in r.get("questions", []):
        a = st.get(q["id"])
        lines.append(f"  {q['id']} depth {q['depth']}: {q['text']}  [{'answered ' + a['given_on'][:10] if a else 'open'}]")
    return "\n".join(lines)


def listing(data: dict | None = None) -> str:
    data = data if data is not None else load()
    st = state(data)
    lines = []
    for r in data["records"]:
        qs = r.get("questions", [])
        n_ans = sum(1 for q in qs if q.get("id") in st)
        lines.append(f"{r.get('id', '?'):45} {r.get('started', '')} → {r.get('ended') or 'open':10} "
                     f"{'app ' + r['app']['name'] if r.get('app') else '':22} questions {n_ans}/{len(qs)} answered")
    lines.append(f"{len(data['records'])} record(s), {len(data['answers'])} answer file(s)")
    return "\n".join(lines)


# --- selftest ----------------------------------------------------------------------------

def _fixture(tmp: Path) -> dict:
    (tmp / "Plan" / "sessions" / "answers").mkdir(parents=True)
    (tmp / "Plan" / "weichen").mkdir(parents=True)
    (tmp / "Plan" / "weichen" / "w16.md").write_text("x", encoding="utf-8")
    rec = {"@type": "Session", "id": "pilot", "title": "Pilot", "started": "2026-10-26", "ended": None, "branch": "b",
           "pr": 1, "mandate": "the author's instruction",
           "report": {"done": [{"text": "built a thing", "refs": ["Plan/weichen/w16.md"]}], "thought": [{"text": "words decide"}],
                      "priorities": [{"rank": 1, "text": "answers"}], "next": [{"text": "beats", "command": "x"}]},
           "app": {"name": "Desk", "route": "#/manuscript/schreibtisch", "what": "marks"},
           "questions": [
               {"@type": "Question", "id": "Q-pilot-01", "depth": 1, "text": "Gilt L3?", "context": "", "concerns": [],
                "lands_in": "Plan/weichen/w16.md", "asked_on": "2026-10-26"},
               {"@type": "Question", "id": "Q-pilot-02", "depth": 2, "text": "Wie lang?", "context": "W16",
                "options": [{"key": "A", "text": "kurz"}, {"key": "B", "text": "lang"}], "recommended": "B", "concerns": [],
                "lands_in": "Plan/weichen/w16.md", "asked_on": "2026-10-26"},
               {"@type": "Question", "id": "Q-pilot-03", "depth": 3, "text": "Welche Haltung?", "context": "Zwei Lesarten.",
                "concerns": [], "lands_in": "Plan/weichen/w16.md", "asked_on": "2026-10-26"}],
           "follows": []}
    (tmp / "Plan" / "sessions" / "pilot.json").write_text(json.dumps(rec), encoding="utf-8")
    return rec


def _answer(tmp: Path, name: str, body: dict) -> None:
    (tmp / "Plan" / "sessions" / "answers" / name).write_text(json.dumps(body), encoding="utf-8")


def selftest() -> int:
    cases: list[tuple[str, bool]] = []

    def run(label, setup):
        with tempfile.TemporaryDirectory() as d:
            tmp = Path(d)
            rec = _fixture(tmp)
            setup(tmp, rec)
            probs = problems(load(tmp / "Plan" / "sessions"), root=tmp)
            return probs

    def rewrite(tmp, rec):
        (tmp / "Plan" / "sessions" / "pilot.json").write_text(json.dumps(rec), encoding="utf-8")

    def ok(label, setup):
        p = run(label, setup)
        cases.append((label, not p))
        if p:
            print(f"  ({label}: {p[:2]})")

    def fails(label, setup, words):
        p = run(label, setup)
        cases.append((label, any(words in x for x in p)))
        if not any(words in x for x in p):
            print(f"  ({label}: wanted {words!r}, got {p[:2]})")

    ok("a whole record with three depths is clean", lambda t, r: None)
    fails("a record without a report is refused", lambda t, r: (r.__setitem__("report", {k: [] for k in REPORT}), rewrite(t, r)),
          "report.done is missing")
    fails("priorities out of order", lambda t, r: (r["report"]["priorities"].append({"rank": 3, "text": "x"}), rewrite(t, r)),
          "not ranked")
    fails("depth 2 with one option", lambda t, r: (r["questions"][1].__setitem__("options", [{"key": "A", "text": "x"}]), rewrite(t, r)),
          "2–4 options")
    fails("a recommended option that is not one", lambda t, r: (r["questions"][1].__setitem__("recommended", "Z"), rewrite(t, r)),
          "is not an option")
    fails("depth 3 without context", lambda t, r: (r["questions"][2].__setitem__("context", ""), rewrite(t, r)), "context")
    fails("an answer that lands nowhere", lambda t, r: (r["questions"][0].__setitem__("lands_in", "Plan/nope.md"), rewrite(t, r)),
          "does not exist")
    fails("a question id of another session", lambda t, r: (r["questions"][0].__setitem__("id", "Q-other-01"), rewrite(t, r)),
          "must be Q-pilot-NN")
    fails("an early name in a record", lambda t, r: (r["report"]["thought"].append({"text": "Jul" "ia"}), rewrite(t, r)),
          "early name")
    good = {"@type": "AnswerSet", "session": "pilot", "by": "author", "given_on": "2026-10-26T18:00:00Z",
            "answers": [{"question": "Q-pilot-01", "yes": True}, {"question": "Q-pilot-02", "option": "B", "words": "im Pilot"},
                        {"question": "Q-pilot-03", "words": "Frist"}]}
    ok("a good answer set", lambda t, r: _answer(t, "pilot-20261026T180000Z.json", good))
    fails("an answer set by a session", lambda t, r: _answer(t, "pilot-20261026T180000Z.json", dict(good, by="session")),
          "by must be author")
    fails("depth 2 answered with no option", lambda t, r: _answer(t, "pilot-20261026T180000Z.json",
          dict(good, answers=[{"question": "Q-pilot-02", "option": "Z"}])), "one of the options")
    fails("depth 3 answered without words", lambda t, r: _answer(t, "pilot-20261026T180000Z.json",
          dict(good, answers=[{"question": "Q-pilot-03"}])), "author's words")
    fails("depth 1 answered with a string", lambda t, r: _answer(t, "pilot-20261026T180000Z.json",
          dict(good, answers=[{"question": "Q-pilot-01", "yes": "ja"}])), "yes (true) or no (false)")
    fails("a file named for another session", lambda t, r: _answer(t, "other-20261026T180000Z.json", good), "name must be")
    fails("an answer to a question no record asks", lambda t, r: _answer(t, "pilot-20261026T180000Z.json",
          dict(good, answers=[{"question": "Q-pilot-09", "yes": True}])), "which no record asks")

    def twice(t, r):
        _answer(t, "pilot-20261026T180000Z.json", good)
        _answer(t, "pilot-20261027T090000Z.json", dict(good, given_on="2026-10-27T09:00:00Z"))
    fails("the same question answered twice without supersedes", twice, "none supersedes the other")

    def revised(t, r):
        _answer(t, "pilot-20261026T180000Z.json", good)
        _answer(t, "pilot-20261027T090000Z.json", dict(good, given_on="2026-10-27T09:00:00Z",
                answers=[{"question": "Q-pilot-02", "option": "A"}], supersedes=["pilot-20261026T180000Z.json"]))
    ok("a revised answer that names the old file", revised)

    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        _fixture(tmp)
        revised(tmp, None)
        data = load(tmp / "Plan" / "sessions")
        st = state(data)
        b = dict((k, t) for k, t in blocks(data))
        cases.append(("a revision replaces only what it re-answers: Q-02 is the revision's A, Q-01 and Q-03 stand from the older file",
                      st.get("Q-pilot-02", {}).get("option") == "A" and st.get("Q-pilot-01", {}).get("yes") is True
                      and st.get("Q-pilot-03", {}).get("words") == "Frist"))
        cases.append(("the prompt's blocks: report, decided, apps — nothing open once all three are answered",
                      list(b) == ["report", "decided", "apps"] and "1. answers" in b["report"]
                      and "Q-pilot-02 (depth 2) A" in b["decided"] and "Q-pilot-01 (depth 1) yes" in b["decided"]
                      and "Desk (#/manuscript/schreibtisch)" in b["apps"]))
        p = new("second", "Zweite", folder=tmp / "Plan" / "sessions", today="2026-10-27")
        cases.append(("new writes a skeleton that check refuses until the report is written",
                      any("second.json: report.done" in x for x in problems(load(tmp / "Plan" / "sessions"), root=tmp))))
        try:
            new("second", "again", folder=tmp / "Plan" / "sessions")
            cases.append(("new refuses an existing id", False))
        except ValueError:
            cases.append(("new refuses an existing id", True))
        cases.append(("no record, no blocks", blocks({"records": [], "answers": [], "problems": []}) == []))
        bare = load(tmp / "Plan" / "sessions")
        bare["answers"] = []
        cases.append(("with no answer every question is carried as open, depth named",
                      "Q-pilot-03 (depth 3, from pilot)" in dict((k, t) for k, t in blocks(bare)).get("open", "")))
        _ = p
    for label, held in cases:
        print(f"  {'held  ' if held else 'FAILED'}  {label}")
    n = sum(1 for _, h in cases if h)
    print(f"{n} of {len(cases)} held")
    return 0 if n == len(cases) else 1


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    if argv[:1] == ["check"]:
        p = problems()
        for x in p:
            print(f"  FAIL  {x}")
        data = load()
        print(f"{len(data['records'])} record(s), {len(data['answers'])} answer file(s), {len(p)} problem(s)")
        return 1 if p else 0
    if argv[:1] == ["show"] and len(argv) > 1:
        print(show(argv[1]))
        return 0
    if argv[:1] == ["new"] and len(argv) > 1:
        def opt(name, default=""):
            return argv[argv.index(name) + 1] if name in argv and argv.index(name) + 1 < len(argv) else default
        try:
            path = new(argv[1], opt("--title", argv[1]), opt("--branch"), opt("--mandate"))
        except ValueError as exc:
            print(f"records: {exc}", file=sys.stderr)
            return 1
        print(f"wrote {_rel(path, ROOT)} — fill the report (done, thought, priorities, next) before `check` passes")
        return 0
    print(listing())
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
