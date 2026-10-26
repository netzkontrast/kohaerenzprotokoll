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
DERIVED_ID = re.compile(r"^Q-[a-z0-9-]+-(weiche|regel)-[a-z0-9]+$")
# The states of an answer, in the order it moves through them. Only the last two bind; „übernommen" is the one a tool
# has acted on, with the answer file as its provenance (Plan/sessions/applied.jsonl).
STATES = ("Entwurf", "eingereicht", "gemergt", "übernommen")
BASE_REF = "origin/main"


def _barred(text: str) -> bool:
    import prose_rules
    return bool(prose_rules.BARRED.search(text) or prose_rules.TRAUMA.search(text))


def load(folder: Path | None = None, root: Path | None = None) -> dict:
    """{"records": [...], "answers": [...], "applied": [...], "problems": [(file, why)]} — read only. A record whose
    `derive` names a briefing gets its questions derived from the files that decide them (`derived_questions`)."""
    folder = folder or FOLDER
    root = root or (ROOT if folder == FOLDER else folder.parent.parent)
    out = {"records": [], "answers": [], "applied": [], "problems": [], "root": root}
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
    ap = folder / "applied.jsonl"
    for n, line in enumerate(ap.read_text(encoding="utf-8").splitlines() if ap.exists() else [], 1):
        if line.strip():
            try:
                out["applied"].append(dict(json.loads(line), _line=n))
            except ValueError as exc:
                out["problems"].append((ap, f"line {n} is not JSON: {exc}"))
    for rec in out["records"]:
        try:
            rec["_derived"] = derived_questions(rec, root)
        except (OSError, ValueError, KeyError) as exc:
            rec["_derived"] = []
            out["problems"].append((rec["_file"], f"derive failed: {exc}"))
    return out


# --- questions the files decide ----------------------------------------------------------

def _section(text: str, head: str) -> str:
    m = re.search(r"^## " + re.escape(head) + r".*?$\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return m.group(1).strip() if m else ""


def _first_paragraph(text: str, limit: int = 600) -> str:
    for block in re.split(r"\n\s*\n", text):
        b = " ".join(x.strip() for x in block.splitlines() if x.strip() and not x.strip().startswith("|"))
        if b:
            return b if len(b) <= limit else b[:limit].rsplit(" ", 1)[0] + " …"
    return ""


ART = {"schlüssel": 0, "schalter": 1, "standard": 2}


def derived_questions(rec: dict, root: Path = ROOT) -> list[dict]:
    """The questions a briefing leaves open, read from the files that decide them — never typed into a record:
    every Weiche the briefing lists under „Offen“ whose sheet is still `offen` (depth 2 when the sheet has options,
    else 3), then every open prose rule in the chapter's scope (depth 1). Blocking first, in a written order: a Weiche
    others among them depend on comes first, then Schlüssel before Schalter before Standard, then the id."""
    spec = rec.get("derive") or {}
    if not spec:
        return []
    import prose_rules
    import weiche
    brief = root / spec["briefing"]
    btext = brief.read_text(encoding="utf-8")
    kap = int(spec.get("kapitel", 1))
    m = re.search(r"^written: (\S+)", btext, re.M)
    asked = m.group(1) if m else ""
    listed = re.findall(r"^- \*\*([A-Z]+\d*)\*\* \(", _section(btext, "Offen"), re.M)
    sheets = weiche.sheets(root / "Plan" / "weichen")
    open_w = []
    for wid in listed:
        path = sheets.get(wid)
        if path is None:
            continue
        text = path.read_text(encoding="utf-8")
        meta = weiche.frontmatter(text)
        if meta.get("status") == "offen":
            open_w.append((wid, path, text, meta))
    ids = {w for w, *_ in open_w}
    def deps(meta):
        d = meta.get("hängt_ab_von") or []
        return [x for x in (d if isinstance(d, list) else [d]) if x in ids]
    dependents = {w: sorted(o for o, _, _, m in open_w if w in deps(m)) for w in ids}
    open_w.sort(key=lambda t: (-len(dependents[t[0]]), ART.get(t[3].get("frage_art", ""), 3), len(deps(t[3])), t[0]))
    rid = rec.get("id", "")
    out = []
    for n, (wid, path, text, meta) in enumerate(open_w, 1):
        title = re.sub(r"^#\s*\S+\s+[—–-]\s*", "", next((ln for ln in text.splitlines() if ln.startswith("# ")), wid)).strip()
        opts = weiche.options_of(text)
        emp = str(meta.get("empfehlung") or "").strip()
        key = emp[:1] if emp[:1] in {k for k, _ in opts} and (len(emp) == 1 or not emp[1].isalnum()) else ""
        why = re.sub(r"\*\*|`", "", _first_paragraph(_section(text, "Empfehlung")))
        first = (f"Zuerst, weil {len(dependents[wid])} weitere offene Weiche(n) von Kap 1 davon abhängen ({', '.join(dependents[wid])})."
                 if dependents[wid] else f"Reihenfolge: {meta.get('frage_art', '')}-Frage, Kap 1 nennt sie im Briefing.")
        rel = path.relative_to(root).as_posix()
        out.append({"@type": "Question", "id": f"Q-{rid}-weiche-{wid.lower()}", "depth": 2 if opts else 3,
                    "text": f"{wid} — {title}", "context": _first_paragraph(_section(text, "Die Frage")),
                    "options": [{"key": k, "text": t} for k, t in opts], "recommended": key,
                    "recommendation": (f"Empfehlung der Sitzung, ein Vorschlag: {emp}. " + why).strip() if emp else "",
                    "concerns": [f"weiche:{wid}", f"chapter:kap-{kap:02d}"], "lands_in": rel, "asked_on": asked,
                    "blocking": True, "order": n, "derived_from": spec["briefing"],
                    "dependents": dependents[wid], "art": meta.get("frage_art", ""), "why_first": first,
                    "tool": f"python3 scripts/weiche.py answer {wid} --from-answer <Antwortdatei> --question Q-{rid}-weiche-{wid.lower()}"})
    reg = root / "Manuscript" / "regeln.jsonl"
    rules = prose_rules.rows(reg) if reg.exists() else []
    weave = None
    wpath = root / "Plan" / "storyform" / "weave.json"
    if wpath.exists():
        weave = json.loads(wpath.read_text(encoding="utf-8"))
    for n, r in enumerate([r for r in rules if r.get("status") == "offen" and prose_rules.in_scope(r, kap, weave)], len(out) + 1):
        out.append({"@type": "Question", "id": f"Q-{rid}-regel-{r['id'].lower()}", "depth": 1,
                    "text": f"Soll Regel {r['id']} gelten? {r['text']}",
                    "context": f"Quelle: {r.get('source', '')}. Gilt für {prose_rules.scope_text(r.get('scope', 'alle'))}. "
                               "Bestätigt prüft prose_rules.py jeden Entwurf darauf; offen bleibt sie eine Rückfrage.",
                    "options": [], "recommended": "", "recommendation": "", "concerns": [f"rule:{r['id']}", f"chapter:kap-{kap:02d}"],
                    "lands_in": "Manuscript/regeln.jsonl", "asked_on": asked, "blocking": False, "order": n,
                    "why_first": "Blockiert die erste Szene nicht: eine offene Regel bleibt eine Rückfrage an jeden Entwurf.",
                    "derived_from": "Manuscript/regeln.jsonl",
                    "tool": f"python3 scripts/prose_rules.py confirm|reject {r['id']} --from-answer <Antwortdatei> --question Q-{rid}-regel-{r['id'].lower()}"})
    return out


def questions(data: dict) -> dict[str, dict]:
    """Every question by id: a record's own, then the ones derived for it (marked `derived`)."""
    out = {}
    for r in data["records"]:
        for q in r.get("questions", []):
            if isinstance(q, dict) and "id" in q:
                out[q["id"]] = dict(q, session=r["id"])
        for q in r.get("_derived", []):
            out[q["id"]] = dict(q, session=r["id"], derived=True)
    return out


def _replaced(data: dict) -> set[tuple[str, str]]:
    """(file, question) pairs a later file replaces: it names the file in `supersedes` and answers that question again.
    A superseded file's other answers stand — a revision replaces what it re-answers, nothing else."""
    out = set()
    for a in data["answers"]:
        again = {x.get("question", "") for x in a.get("answers", [])}
        for old in a.get("supersedes", []):
            out |= {(old, q) for q in again}
    return out


def merged_at(path: Path, root: Path = ROOT, ref: str | None = None) -> bool | None:
    """Is the file in the base branch? True, False, or None when the base ref is not there to ask (a shallow CI
    checkout, a container without `origin/main`)."""
    import subprocess
    ref = ref or BASE_REF
    try:
        rel = path.relative_to(root).as_posix()
    except ValueError:
        return None
    has_ref = subprocess.run(["git", "rev-parse", "--verify", "-q", ref], cwd=root, capture_output=True).returncode == 0
    if not has_ref:
        return None
    return subprocess.run(["git", "cat-file", "-e", f"{ref}:{rel}"], cwd=root, capture_output=True).returncode == 0


def applied_index(data: dict) -> dict[tuple[str, str], dict]:
    """(answer file name, question) → the row that says which tool took the answer over."""
    return {(Path(r.get("answer", "")).name, r.get("question", "")): r for r in data.get("applied", [])}


def status_of(data: dict, file: Path, qid: str, merged=None) -> str:
    """eingereicht / gemergt / übernommen — from the files, never from a flag a person or a session sets.
    „Entwurf" is the browser's own state and never reaches a file."""
    if (file.name, qid) in applied_index(data):
        return "übernommen"
    m = (merged or merged_at)(file, data.get("root", ROOT))
    return "gemergt" if m else "eingereicht" if m is False else "im Arbeitsbaum"


def state(data: dict, merged=None) -> dict[str, dict]:
    """Per question id: the newest answer not replaced by a revision, with its file and status — or none (open)."""
    gone = _replaced(data)
    out: dict[str, dict] = {}
    for a in sorted(data["answers"], key=lambda a: (a.get("given_on", ""), a["_file"].name)):
        for x in a.get("answers", []):
            q = x.get("question", "")
            if (a["_file"].name, q) not in gone:
                out[q] = dict(x, file=a["_file"], given_on=a.get("given_on", ""), session=a.get("session", ""),
                              status=status_of(data, a["_file"], q, merged))
    return out


def binding(entry: dict | None) -> bool:
    """An answer binds once it is merged; a submitted one is the author's word in a pull request, not yet a decision."""
    return bool(entry) and entry.get("status") in ("gemergt", "übernommen")


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
        f = _rel(r["_file"], root)
        spec = r.get("derive")
        if spec is not None and (not isinstance(spec, dict) or not (root / str(spec.get("briefing", ""))).exists()):
            out.append(f"{f}: derive names a briefing that does not exist")
        for run in r.get("runs", []):
            if not DAY.match(str(run.get("on") or "")) or not str(run.get("what") or "").strip():
                out.append(f"{f}: a run needs on (YYYY-MM-DD) and what")
        for q in r.get("_derived", []):
            if not DERIVED_ID.match(q["id"]) or q["id"] in seen_q:
                out.append(f"{f} {q['id']}: a derived question id collides or is malformed")
            seen_q[q["id"]] = f
            if not (root / q["lands_in"]).exists():
                out.append(f"{f} {q['id']}: lands_in {q['lands_in']} does not exist")
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
    for row in data.get("applied", []):
        where = f"Plan/sessions/applied.jsonl line {row.get('_line')}"
        af = root / str(row.get("answer", ""))
        if not af.exists():
            out.append(f"{where}: answer file {row.get('answer')} does not exist — an application needs its provenance")
            continue
        a = next((x for x in data["answers"] if x["_file"].resolve() == af.resolve()), None)
        if a is None or not any(x.get("question") == row.get("question") for x in a.get("answers", [])):
            out.append(f"{where}: {row.get('answer')} does not answer {row.get('question')}")
        if not str(row.get("tool") or "").strip() or not str(row.get("result") or "").strip():
            out.append(f"{where}: an application names the tool that acted and what it wrote")
        if not DAY.match(str(row.get("on") or "")):
            out.append(f"{where}: on is not YYYY-MM-DD")
    gone = _replaced(data)
    for qid, files in answered_in.items():
        live = [x for x in files if (x, qid) not in gone]
        if len(live) > 1:
            out.append(f"{qid}: answered in {', '.join(live)} and none supersedes the other — a changed answer names the old file")
    return out


# --- the workshop's next allowed step and taking an answer over ----------------------------

def next_step(rec: dict, data: dict, merged=None) -> dict:
    """The next step decision 030 allows for a record that derives from a briefing — from the files alone:
    a merged answer not yet taken over comes first; then the first blocking question without a binding answer;
    then the beats of the next scene; then that scene's own next step (manuscript.py)."""
    spec = rec.get("derive") or {}
    if not spec:
        return {}
    root = data.get("root", ROOT)
    kap = int(spec.get("kapitel", 1))
    st = state(data, merged)
    for q in rec.get("_derived", []):
        a = st.get(q["id"])
        if a and a["status"] == "gemergt":
            return {"kind": "übernehmen", "question": q["id"], "text": f"Deine gemergte Antwort auf {q['text'].split(' — ')[0]} übernehmen — mit der Antwortdatei als Provenienz.",
                    "command": q["tool"].replace("<Antwortdatei>", _rel(a["file"], root))}
    for q in rec.get("_derived", []):
        a = st.get(q["id"])
        if q.get("blocking") and not binding(a):
            pending = f" — eingereicht in {_rel(a['file'], root)}, wartet auf deinen Merge" if a else ""
            return {"kind": "frage", "question": q["id"], "text": f"Deine Antwort auf {q['text']}{pending}", "command": ""}
    import manuscript
    sc = manuscript.scenes(kap, root / "Manuscript") if (root / "Manuscript").is_dir() else []
    nxt = next((x for x in sc if x["head"].get("status") != "freigegeben"), None)
    if nxt is None:
        k = len(sc) + 1
        return {"kind": "beats", "question": "", "text": f"Die Beats von Kap {kap}, Szene {k} vorlegen — erst deine freigegebenen Beats, dann Prosa.",
                "command": f"python3 scripts/manuscript.py beats kap-{kap:02d} {k} --words \"…\" --beats \"…\""}
    k = nxt["head"].get("szene", "?")
    what = {"beats": ("Die Szene schreiben, auf den freigegebenen Beats", ""),
            "entwurf": ("Die Szene prüfen", f"python3 scripts/manuscript.py check kap-{kap:02d} {k}"),
            "redigiert": ("Deine Freigabe der Szene, mit deinen Worten", f"python3 scripts/manuscript.py approve kap-{kap:02d} {k} --words \"…\"")}
    t, c = what.get(nxt["head"].get("status", ""), ("Den Stand der Szene klären", ""))
    return {"kind": "szene", "question": "", "text": f"Kap {kap}, Szene {k}: {t}.", "command": c}


def answer_from(answer_file: Path, qid: str, data: dict | None = None, merged=None) -> dict:
    """The author's answer to one question, read from a merged answer file — what a tool takes over. Refuses an
    answer that is not merged (eingereicht binds nothing), a file that fails `check`, and a question it does not answer."""
    data = data if data is not None else load()
    root = data.get("root", ROOT)
    path = answer_file if answer_file.is_absolute() else root / answer_file
    probs = [p for p in problems(data, root) if path.name in p]
    if probs:
        raise SystemExit("the answer file fails its check: " + "; ".join(probs[:3]))
    a = next((x for x in data["answers"] if x["_file"].resolve() == path.resolve()), None)
    x = next((y for y in (a or {}).get("answers", []) if y.get("question") == qid), None)
    if x is None:
        raise SystemExit(f"{_rel(path, root)} does not answer {qid}")
    st = status_of(data, path, qid, merged)
    if st == "übernommen":
        raise SystemExit(f"{qid} from {_rel(path, root)} was already taken over (Plan/sessions/applied.jsonl)")
    if st != "gemergt":
        raise SystemExit(f"{_rel(path, root)} is {st}, not merged — an answer binds only after the author's merge")
    live = state(data, merged).get(qid)
    if live and live["file"].resolve() != path.resolve():
        raise SystemExit(f"{_rel(path, root)} is not the live answer to {qid}: {_rel(live['file'], root)} supersedes it")
    q = questions(data).get(qid, {})
    return dict(x, depth=q.get("depth"), file=_rel(path, root), given_on=a.get("given_on", ""))


def record_applied(answer: dict, qid: str, tool: str, result: str, today: str | None = None,
                   folder: Path | None = None) -> dict:
    """Append the row that makes an answer „übernommen“: which tool took it over and what it wrote."""
    folder = folder or FOLDER
    row = {"answer": answer["file"], "question": qid, "tool": tool, "result": result, "on": today or date.today().isoformat()}
    with (folder / "applied.jsonl").open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


# --- the prompt's blocks ---------------------------------------------------------------

def _newest(recs: list[dict]) -> list[dict]:
    """Records newest first: by `updated` (or the last run, or started), then id — a written, total order."""
    def key(r):
        runs = [x.get("on", "") for x in r.get("runs", [])]
        return (str(r.get("updated") or max(runs + [str(r.get("started") or "")])), r.get("id", ""))
    return sorted(recs, key=key, reverse=True)


def blocks(data: dict | None = None, merged=None) -> list[list[str]]:
    """`[key, text]` for sessions.py, the same contract the app and agents/sessions.json read: the newest record's
    report, the next allowed step of every record that derives from a briefing, the answers by status, the questions
    still open (blocking first, with depth), the apps. Deterministic for the same files and git state; only the
    records' and the repository's words, never corpus text. Empty when there is no record."""
    data = data if data is not None else load()
    recs = _newest([r for r in data["records"] if isinstance(r.get("report"), dict)])
    if not recs:
        return []
    root = data.get("root", ROOT)
    last = recs[0]
    rep = last["report"]
    lines = [f"What the last session reported (Plan/sessions/{last['id']}.json — {last.get('title', '')}):"]
    for part, head in (("done", "Done"), ("thought", "Thought"), ("priorities", "Priorities"), ("next", "Next")):
        lines.append(f"{head}:")
        for x in rep.get(part) or []:
            mark = f"{x['rank']}. " if part == "priorities" and x.get("rank") else "- "
            refs = f" [{', '.join(x['refs'])}]" if x.get("refs") else ""
            lines.append(f"  {mark}{x.get('text', '')}{refs}" + (f" (`{x['command']}`)" if x.get("command") else ""))
    if len(recs) > 1:
        lines.append("Other records: " + "; ".join(f"{r['id']} ({'ended ' + r['ended'] if r.get('ended') else 'open'})" for r in recs[1:]))
    out = [["report", "\n".join(lines)]]
    steps = [(r, next_step(r, data, merged)) for r in recs if r.get("derive")]
    steps = [(r, x) for r, x in steps if x]
    if steps:
        rows = ["The next allowed step (decision 030), derived from the files:"]
        rows += [f"- {r['id']}: {x['text']}" + (f"\n  `{x['command']}`" if x.get("command") else "") for r, x in steps]
        out.append(["step", "\n".join(rows)])
    qs, st = questions(data), state(data, merged)
    given = sorted(((qid, st[qid]) for qid in qs if qid in st), key=lambda t: (t[1]["given_on"], t[0]))
    if given:
        rows = ["The author's answers, by status (Plan/sessions/answers/; applied.jsonl records what a tool took over):"]
        for label, want in (("Merged, not yet taken over — fold these first, with the answer file as provenance:", "gemergt"),
                            ("Submitted in a pull request, not merged — NOT binding, decide nothing on them:", "eingereicht"),
                            ("In the working tree, merge state unknown — NOT binding:", "im Arbeitsbaum"),
                            ("Taken over by a tool:", "übernommen")):
            these = [(qid, x) for qid, x in given if x["status"] == want]
            if not these:
                continue
            rows.append(label)
            for qid, x in these:
                q = qs[qid]
                said = "ja" if x.get("yes") is True else "nein" if x.get("yes") is False else x.get("option", "")
                words = f" „{x['words']}“" if x.get("words") else ""
                tool = f"; `{q['tool'].replace('<Antwortdatei>', _rel(x['file'], root))}`" if want == "gemergt" and q.get("tool") else ""
                rows.append(f"- {qid} (depth {q['depth']}) {(said + ' ') if said else ''}{words.strip()} — {_rel(x['file'], root)}, given {x['given_on'][:10]}, lands in {q.get('lands_in')}{tool}")
        out.append(["decided", "\n".join(rows)])
    open_q = [q for qid, q in qs.items() if not binding(st.get(qid))]
    open_q.sort(key=lambda q: (not q.get("blocking"), q["session"], q.get("order", 0), q["id"]))
    if open_q:
        rows = ["Still open — do not ask again; the blocking ones first:"]
        rows += [f"- {q['id']} (depth {q['depth']}{', blocking' if q.get('blocking') else ''}, {q['session']}): {q['text'][:160]}" for q in open_q]
        out.append(["open", "\n".join(rows)])
    apps = [r for r in recs if r.get("app")]
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


def MERGED(path, root):  # noqa: N802 — the fixture's git: every answer file counts as merged
    return True


def _workshop(tmp: Path) -> dict:
    """A briefing with two open Weichen (one depends on the other) and an open rule — synthetic, never project data."""
    (tmp / "Manuscript" / "kap-01").mkdir(parents=True, exist_ok=True)
    (tmp / "Manuscript" / "kap-01" / "briefing.md").write_text(
        "---\nkapitel: 1\nwritten: 2026-10-26\n---\n\n# Briefing\n\n## Offen — vor der ersten Szene zu beantworten\n\n"
        "- **W1** (offen, schlüssel) — x\n- **W2** (offen, standard) — y\n- **W3** (offen, schlüssel) — z\n\n## Szenen\n", encoding="utf-8")
    sheet = "---\nid: {id}\nstatus: {st}\nhängt_ab_von: [{dep}]\nfrage_art: {art}\nempfehlung: \"{emp}\"\n---\n\n# {id} — Frage {id}?\n\n" \
            "## Die Frage und die Evidenz\n\nWarum {id}.\n\n## Optionen und Folgen\n\n| Option | a |\n|---|---|\n| A — Erstens | x |\n| B — Zweitens | y |\n\n" \
            "## Empfehlung und Prüfpunkt\n\n**A**, weil.\n"
    for wid, st, dep, art, emp in (("W1", "offen", "W2", "schlüssel", "A"), ("W2", "offen", "", "standard", "B"), ("W3", "beantwortet", "", "schlüssel", "A")):
        (tmp / "Plan" / "weichen" / f"{wid.lower()}.md").write_text(sheet.format(id=wid, st=st, dep=dep, art=art, emp=emp), encoding="utf-8")
    (tmp / "Manuscript" / "regeln.jsonl").write_text(json.dumps({"id": "L9", "text": "Keine Wärme in Kap 1.", "source": "fixture", "scope": "alle", "status": "offen"}) + "\n", encoding="utf-8")
    ws = {"@type": "Session", "id": "ws", "title": "Werkstatt", "started": "2026-10-26", "ended": None, "mandate": "030",
          "report": {"done": [{"text": "Werkzeuge"}], "thought": [{"text": "Worte entscheiden"}], "priorities": [{"rank": 1, "text": "Weichen"}],
                     "next": [{"text": "Beats"}]}, "app": None, "questions": [], "follows": [],
          "derive": {"briefing": "Manuscript/kap-01/briefing.md", "kapitel": 1}}
    (tmp / "Plan" / "sessions" / "ws.json").write_text(json.dumps(ws), encoding="utf-8")
    return ws


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
        b = dict((k, t) for k, t in blocks(data, merged=MERGED))
        cases.append(("a revision replaces only what it re-answers: Q-02 is the revision's A, Q-01 and Q-03 stand from the older file",
                      st.get("Q-pilot-02", {}).get("option") == "A" and st.get("Q-pilot-01", {}).get("yes") is True
                      and st.get("Q-pilot-03", {}).get("words") == "Frist"))
        cases.append(("the prompt's blocks: report, decided, apps — nothing open once all three are answered",
                      list(b) == ["report", "decided", "apps"] and "1. answers" in b["report"]
                      and "Q-pilot-02 (depth 2) A" in b["decided"] and "Q-pilot-01 (depth 1) ja" in b["decided"] and "(depth 3) „Frist“" in b["decided"]
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
        cases.append(("the prompt's blocks are the same for the same files", blocks(load(tmp / "Plan" / "sessions"), merged=MERGED) == blocks(load(tmp / "Plan" / "sessions"), merged=MERGED)))
        bare = load(tmp / "Plan" / "sessions")
        bare["answers"] = []
        cases.append(("with no answer every question is carried as open, depth named",
                      "Q-pilot-03 (depth 3, pilot)" in dict((k, t) for k, t in blocks(bare, merged=MERGED)).get("open", "")))
        _ = p
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d)
        _fixture(tmp)
        _workshop(tmp)
        data = load(tmp / "Plan" / "sessions")
        ws = next(r for r in data["records"] if r["id"] == "ws")
        ids = [q["id"] for q in ws["_derived"]]
        cases.append(("derived from the briefing: open Weichen only (W3 answered is left out), the one others depend on first, then the open rule",
                      ids == ["Q-ws-weiche-w2", "Q-ws-weiche-w1", "Q-ws-regel-l9"]))
        w2 = ws["_derived"][0]
        cases.append(("a derived Weiche: depth 2, stable keys from the sheet's table, the recommendation named and marked as one",
                      w2["depth"] == 2 and [o["key"] for o in w2["options"]] == ["A", "B"] and w2["recommended"] == "B"
                      and w2["recommendation"].startswith("Empfehlung der Sitzung, ein Vorschlag") and "abhängen (W1)" in w2["why_first"]))
        cases.append(("the next allowed step is the first blocking question", next_step(ws, data, MERGED)["question"] == "Q-ws-weiche-w2"))
        body = {"@type": "AnswerSet", "session": "ws", "by": "author", "given_on": "2026-10-26T19:00:00Z",
                "answers": [{"question": "Q-ws-weiche-w2", "option": "A", "words": "A, aber nur im Pilot"}]}
        _answer(tmp, "ws-20261026T190000Z.json", body)
        data = load(tmp / "Plan" / "sessions")
        ws = next(r for r in data["records"] if r["id"] == "ws")
        submitted = lambda p, r: False  # noqa: E731 — a pull request not yet merged
        cases.append(("a submitted answer is not binding: the step stays the question, the prompt says NOT binding",
                      next_step(ws, data, submitted)["kind"] == "frage" and "wartet auf deinen Merge" in next_step(ws, data, submitted)["text"]
                      and "NOT binding" in dict(blocks(data, merged=submitted))["decided"]))
        try:
            answer_from(Path("Plan/sessions/answers/ws-20261026T190000Z.json"), "Q-ws-weiche-w2", data, submitted)
            cases.append(("a tool refuses an answer that is not merged", False))
        except SystemExit:
            cases.append(("a tool refuses an answer that is not merged", True))
        st = next_step(ws, data, MERGED)
        cases.append(("a merged answer not taken over comes first, with the command and the file",
                      st["kind"] == "übernehmen" and "ws-20261026T190000Z.json" in st["command"]))
        a = answer_from(Path("Plan/sessions/answers/ws-20261026T190000Z.json"), "Q-ws-weiche-w2", data, MERGED)
        cases.append(("the author's words come back verbatim, restriction included", a["words"] == "A, aber nur im Pilot" and a["option"] == "A"))
        record_applied(a, "Q-ws-weiche-w2", "weiche.py answer W2", "Plan/weichen/w2.md", today="2026-10-27", folder=tmp / "Plan" / "sessions")
        data = load(tmp / "Plan" / "sessions")
        ws = next(r for r in data["records"] if r["id"] == "ws")
        cases.append(("taken over: status übernommen, a second take-over refused, the next blocking question is next",
                      state(data, MERGED)["Q-ws-weiche-w2"]["status"] == "übernommen" and next_step(ws, data, MERGED)["question"] == "Q-ws-weiche-w1"
                      and not problems(data, tmp)))
        try:
            answer_from(Path("Plan/sessions/answers/ws-20261026T190000Z.json"), "Q-ws-weiche-w2", data, MERGED)
            cases.append(("an answer is taken over once", False))
        except SystemExit:
            cases.append(("an answer is taken over once", True))
        _answer(tmp, "ws-20261027T080000Z.json", dict(body, given_on="2026-10-27T08:00:00Z", supersedes=["ws-20261026T190000Z.json"],
                                                        answers=[{"question": "Q-ws-weiche-w2", "option": "B", "words": "doch B"}]))
        data = load(tmp / "Plan" / "sessions")
        cases.append(("a correction keeps the earlier answer file and its take-over, and is the live answer",
                      (tmp / "Plan" / "sessions" / "answers" / "ws-20261026T190000Z.json").exists()
                      and state(data, MERGED)["Q-ws-weiche-w2"]["option"] == "B" and len(data["applied"]) == 1 and not problems(data, tmp)))
        _answer(tmp, "pilot-20261027T090000Z.json", {"@type": "AnswerSet", "session": "pilot", "by": "author", "given_on": "2026-10-27T09:00:00Z",
                                                    "answers": [{"question": "Q-pilot-03", "words": "Frist"}]})
        _answer(tmp, "ws-20261027T090000Z.json", {"@type": "AnswerSet", "session": "ws", "by": "author", "given_on": "2026-10-27T09:00:00Z",
                                                 "answers": [{"question": "Q-ws-regel-l9", "yes": True}]})
        data = load(tmp / "Plan" / "sessions")
        st2 = state(data, MERGED)
        cases.append(("two sessions saving at the same second write two files, overwrite nothing",
                      st2["Q-pilot-03"]["words"] == "Frist" and st2["Q-ws-regel-l9"]["yes"] is True and not problems(data, tmp)))
        _answer(tmp, "ws-20261027T100000Z.json", {"@type": "AnswerSet", "session": "ws", "by": "author", "given_on": "2026-10-27T10:00:00Z",
                                                 "answers": [{"question": "Q-ws-weiche-w1", "option": "Z"}]})
        cases.append(("a derived question answered with an option it does not have is refused",
                      any("one of the options" in x for x in problems(load(tmp / "Plan" / "sessions"), tmp))))
        text = "\n".join(t for _, t in blocks(load(tmp / "Plan" / "sessions"), merged=MERGED))
        cases.append(("the prompt carries no secret-shaped string and no citation of a source line",
                      not re.search(r"ghp_|github_pat_|Bearer |SITE_PASSWORD|RAG_MCP_TOKEN|\^\[", text)))
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
