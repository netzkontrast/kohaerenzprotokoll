#!/usr/bin/env python3
"""Ask the source documents a question: route, pack, answer, verify, land.

The design is `Plan/concept/ask-sources_2026-09-30.md`; decision 017 says what
an answer is: logged and treated like a source, landed once under `Sources/ask/`,
tier `M-ask` — a model's reading of other sources, never the author's word.

1. **route** (code): graph evidence from `graphrag.retrieve`, BM25 over every
   line of every landed document from the GraphQLite store (`askdb.py`), unread
   documents from the entity lists, and for a `compare` question the shortest
   path between two seeds with the line that states each hop.
2. **pack** (code): the question, a rules card, the graph excerpt, numbered
   source windows, a skill excerpt, the answer schema — one file, the same for
   every backend.
3. **run**: `claude-cli` (default, `claude -p`, no tools: only the pack),
   `route` (a free OpenRouter model through `route.py`), `session` (a subagent
   reads the pack and writes `raw.session.json`), `jules` (see `jules`).
   A pack is immutable: its text must still hash to `pack.json`, a changed pack
   gets the next id (`<id>.2`), and a run is never overwritten — a repeat is
   `--attempt N` and gets its own files (P18).
4. **verify** (code): the reply must hold the schema (else `schema-invalid`,
   with the reasons); every quotation must stand on a line the pack *sent*
   (`meta.shown`) by `quotes.py`'s own comparison — the same words elsewhere in
   the document are `outside-window` — or it is rejected; a claim with no placed
   quotation is `unsupported`.
5. **land**: the rendered answer goes to `Sources/ask/<id>-<backend>.md` with a
   checksum and a manifest row, once; a second landing is refused. `subject.document`
   resolves a landed answer by its slug, so `quotes.py` and `read.py` cite it like
   any source, while it stays out of `documents()` and every corpus count.

    .venv-dspy/bin/python scripts/ask.py pack "Wann erscheint Juna zuerst direkt?" [--kind locate]
    .venv-dspy/bin/python scripts/ask.py run <id> --backend claude-cli [--model sonnet]
    .venv-dspy/bin/python scripts/ask.py run <id> --backend route
    .venv-dspy/bin/python scripts/ask.py run <id> --backend route --attempt 1   # a repeat, beside the first
    .venv-dspy/bin/python scripts/ask.py verify <id> [--backend B]      # re-verify a stored reply
    .venv-dspy/bin/python scripts/ask.py land <id> [--backend B]
    .venv-dspy/bin/python scripts/ask.py ask "…" [--backend B]          # pack, run, verify, land
    .venv-dspy/bin/python scripts/ask.py selftest
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import quotes  # noqa: E402

RUNS = ROOT / "Plan" / "runs" / "ask"
LANDED = ROOT / "Sources" / "ask"
MANIFEST = LANDED / "manifest.jsonl"
SKILL_DIRS = [ROOT / ".agents" / "skills"]
WINDOW = 3            # lines on each side of an anchor when its paragraph is too long
PER_PARA = 6          # a paragraph up to 13 lines is shown whole
PER_DOC = 60          # at most this many lines of one document
BUDGET = 60_000       # characters of source windows in one pack
BM25_HITS = 30
KINDS = ("locate", "position", "compare", "explain")

RULES = """## Regeln für diese Antwort

1. Antworte nur aus diesem Paket. Was nicht darin steht, gehört in `gaps`, nicht in eine Behauptung.
2. Eine Behauptung gilt einem Dokument. Sie nennt es mit seinem Slug (`doc`).
3. Jede Behauptung trägt mindestens ein Zitat: die Wörter der Quelle, buchstäblich, ohne Auslassung,
   aus einer einzigen Zeile. `line_hint` ist die Zeilennummer, die vor der Zeile im Paket steht.
4. Zitate bleiben in der Sprache der Quelle. Nichts wird übersetzt. `says`, `differ` und `gaps` schreibst du auf Deutsch.
5. Vergleiche zwei Dokumente nur in `differ`, und nur, wenn für beide eine belegte Behauptung steht.
6. Keine Quelle entscheidet über eine andere. Ein Datum oder der Anspruch, Kanon zu sein, entscheidet nichts.
7. Wenn das Paket die Frage nicht beantwortet, setze `answerable` auf `no` und sage in `gaps`, was fehlt.
8. `need` darf höchstens drei Einträge haben: ein Begriff oder ein Zeilenbereich eines Dokuments.
9. Gib nur JSON zurück, im Schema unten, ohne Text davor oder danach.
10. Dass das Paket etwas nicht zeigt, beweist nicht, dass die Quellen es nicht sagen: Das Paket ist eine Auswahl.
    Schreibe dann „nicht im Paket", nie „keine Quelle sagt".
"""

SCHEMA = """## Antwortschema (JSON)

{"answerable": "yes | partly | no",
 "claims": [{"doc": "<slug>", "says": "<ein Satz>",
             "quotes": [{"text": "<wörtlich>", "line_hint": 123}]}],
 "differ": ["<slug-a> vs <slug-b>: <was sich unterscheidet>"],
 "gaps": ["<was das Paket nicht hält>"],
 "need": [{"term": "<Begriff>"}, {"doc": "<slug>", "lines": [100, 140]}],
 "next": [{"doc": "<slug>", "why": "<eine Zeile>"}]}
"""


def now() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S")


def ask_id(question: str, kind: str = "explain") -> str:
    key = question if kind == "explain" else f"{kind}\0{question}"  # explain keeps the ids already landed
    return time.strftime("%Y-%m-%d") + "-" + hashlib.sha256(key.encode()).hexdigest()[:8]


def sha(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


def load_pack(qid: str) -> tuple[str, dict]:
    """The pack as sent, refused if its text no longer has the hash its meta recorded."""
    d = run_dir(qid)
    text = (d / "pack.md").read_text(encoding="utf-8")
    meta = json.loads((d / "pack.json").read_text(encoding="utf-8"))
    if sha(text) != meta["hash"]:
        sys.exit(f"{qid}: pack.md does not hash to pack.json's {meta['hash'][:12]}; a pack is never edited")
    return text, meta


def tag(backend: str, attempt: int) -> str:
    """A run's file name part: the backend, and the attempt from the second on (P18)."""
    return backend if attempt == 0 else f"{backend}-a{attempt}"


def run_dir(qid: str) -> Path:
    return RUNS / qid


# ── route ─────────────────────────────────────────────────────────────────────

def route(question: str, kind: str, store=None, graph: dict | None = None) -> dict:
    import graphrag
    import askdb
    s = store or askdb.Store()
    evidence = graphrag.retrieve(question, graph=graph)
    anchors: list[dict] = []
    for ev in evidence["evidence"]:
        anchors.append({"doc": ev["doc"], "line": ev["line"], "finder": "graph-evidence"})
    for r in s.bm25(question, limit=BM25_HITS):
        anchors.append({"doc": r["slug"], "line": r["line"], "finder": "bm25-lines"})
    for r in evidence.get("unread_routes", []):
        line = int(str(r["via"]).rsplit(":L", 1)[-1]) if ":L" in str(r["via"]) else None
        if line:
            anchors.append({"doc": r["doc"], "line": line, "finder": "entity-unread"})
    seeds = [x["term"] for x in evidence["seeds"]]
    # paragraphs anywhere in the corpus where the seed terms stand together (askextract: MENTIONS)
    for r in s.comention(seeds[:4]):
        anchors.append({"doc": r["slug"], "line": r["first"], "finder": "co-mention", "span": (r["first"], r["last"])})
    # the same passage carried into other documents (learned `parallel` hyperedges)
    for a in [a for a in anchors if a["finder"] in ("graph-evidence", "co-mention")][:15]:
        span = a.get("span") or s.paragraph(a["doc"], a["line"])
        if span:
            for q in s.parallels(f"para:{a['doc']}:{span[0]}"):
                anchors.append({"doc": q["slug"], "line": q["first"], "finder": "parallel", "span": (q["first"], q["last"])})
    path = []
    if kind == "compare" and len(seeds) >= 2:
        p = s.path(seeds[0], seeds[1])
        for a, b in zip(p.get("path", []), p.get("path", [])[1:]):
            path.append({"from": a, "to": b, "via": s.via(a, b)})
    # rank: documents several finders reach come first, graph evidence before bm25
    by_doc: dict[str, dict] = {}
    for a in anchors:
        d = by_doc.setdefault(a["doc"], {"doc": a["doc"], "lines": set(), "finders": set()})
        d["lines"].add(a["line"])
        d["finders"].add(a["finder"])
    order = sorted(by_doc.values(), key=lambda d: (-len(d["finders"]),
                                                   "graph-evidence" not in d["finders"],
                                                   -len(d["lines"]), d["doc"]))
    read_docs = {r["k"].split(":", 1)[1] for r in s.cypher("MATCH (d:Doc) WHERE d.read = true RETURN d.id AS k")}
    return {"evidence": evidence, "anchors": anchors, "docs": order, "path": path, "evidence_docs": read_docs}


# ── pack ──────────────────────────────────────────────────────────────────────

def skills_for(question: str, k: int = 2) -> list[dict]:
    """The skills whose description shares the most content words with the question."""
    import askdb
    words = {w.lower() for w in re.findall(r"\w[\w-]{3,}", question)} - askdb.STOP
    scored = []
    for base in SKILL_DIRS:
        for p in sorted(base.glob("*/SKILL.md")):
            text = p.read_text(encoding="utf-8")
            m = re.search(r"^description:\s*(>-?\s*\n)?(.*?)(?=^\w[\w-]*:|^---)", text, re.S | re.M)
            desc = " ".join((m.group(2) if m else "").split())
            overlap = len(words & {w.lower() for w in re.findall(r"\w[\w-]{3,}", desc)})
            if overlap >= 2:
                scored.append({"skill": p.parent.name, "description": desc, "overlap": overlap})
    return sorted(scored, key=lambda x: -x["overlap"])[:k]


def build_pack(question: str, kind: str = "explain", budget: int = BUDGET, store=None,
               graph: dict | None = None, rules: str = RULES, schema: str = SCHEMA) -> tuple[str, dict]:
    """The pack every backend reads. `rules` and `schema` are parameters so another step (an
    extraction lab) reuses the same pack, `verify` and `render` rather than a second verifier."""
    import graphrag
    import askdb
    s = store or askdb.Store()
    r = route(question, kind, s, graph)
    parts, sent, cut, used, shown = [], [], [], 0, {}
    parts.append(f"# Frage\n\n{question}\n\nArt der Frage: `{kind}`\n")
    parts.append(rules)
    parts.append("## Was das Wiki schon weiß (Graph)\n\n" + graphrag.render(r["evidence"]) + "\n")
    if r["path"]:
        lines = [f"- `{h['from']}` → `{h['to']}`: "
                 + "; ".join(f"{v['t']} ({v['via']})" for v in h["via"]) for h in r["path"]]
        parts.append("## Wie die Begriffe verbunden sind\n\n" + "\n".join(lines) + "\n")
    when = dates()
    tiers = {r["slug"]: r.get("tier", "") for r in askdb.manifest()}
    windows = ["## Quellen — Zeilen mit ihrer Nummer\n"]
    for d in r["docs"]:
        spans = []
        for line in sorted(d["lines"]):
            para = s.paragraph(d["doc"], line)
            lo, hi = (para if para and para[1] - para[0] <= 2 * PER_PARA else (line - WINDOW, line + WINDOW))
            lo, hi = max(1, min(lo, line - 1)), max(hi, line + 1)
            if spans and lo <= spans[-1][1] + 1:
                spans[-1][1] = max(spans[-1][1], hi)
            else:
                spans.append([lo, hi])
        rows, n = [], 0
        for lo, hi in spans:
            for number, text in s.window(d["doc"], lo, hi):
                if n >= PER_DOC:
                    break
                rows.append(f"L{number}: {text}")
                shown.setdefault(d["doc"], []).append(number)
                n += 1
            rows.append("…")
        read = "gelesen" if d["doc"] in r["evidence_docs"] else "ungelesen"
        block = (f"\n### `{d['doc']}` — {when.get(d['doc']) or 'undatiert'}, {tiers.get(d['doc'], '')}, {read}; "
                 f"gefunden von: {', '.join(sorted(d['finders']))}\n\n" + "\n".join(rows) + "\n")
        if used + len(block) > budget:
            cut.append(d["doc"])
            shown.pop(d["doc"], None)
            continue
        used += len(block)
        windows.append(block)
        sent.append(d["doc"])
    parts.append("".join(windows))
    skills = skills_for(question)
    if skills:
        parts.append("## Passende Skills (Auszug)\n\n" + "\n".join(
            f"- **{x['skill']}**: {x['description']}" for x in skills) + "\n")
    parts.append(schema)
    text = "\n".join(parts)
    meta = {"id": ask_id(question, kind), "question": question, "kind": kind, "built": now(),
            "sends_text_of": sent, "cut_by_budget": cut, "budget": budget, "chars": len(text),
            "window_chars": used, "finders": {d["doc"]: sorted(d["finders"]) for d in r["docs"]},
            "seeds": [x["term"] for x in r["evidence"]["seeds"]], "skills": [x["skill"] for x in skills],
            "hash": hashlib.sha256(text.encode()).hexdigest(), "shown": shown}
    return text, meta


def cmd_pack(question: str, kind: str) -> str:
    text, meta = build_pack(question, kind)
    base, n = meta["id"], 1
    # a pack is immutable: the same text is reused, a different one gets the next free id
    while (run_dir(meta["id"]) / "pack.json").exists():
        if json.loads((run_dir(meta["id"]) / "pack.json").read_text(encoding="utf-8"))["hash"] == meta["hash"]:
            print(f"{meta['id']}: the same pack exists already")
            return meta["id"]
        n += 1
        meta["id"] = f"{base}.{n}"
    d = run_dir(meta["id"])
    d.mkdir(parents=True)
    (d / "question.txt").write_text(question + "\n", encoding="utf-8")
    (d / "pack.md").write_text(text, encoding="utf-8")
    (d / "pack.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{meta['id']}: {meta['chars']} chars, {len(meta['sends_text_of'])} documents, "
          f"{len(meta['cut_by_budget'])} cut by budget → {d.relative_to(ROOT)}/pack.md")
    return meta["id"]


# ── backends ──────────────────────────────────────────────────────────────────

def backend_claude_cli(pack: str, model: str) -> dict:
    from claude_lm import ClaudeCLI
    lm = ClaudeCLI(model, timeout=600)
    started = time.time()
    try:
        reply = lm._one("", pack)
    except Exception as exc:  # noqa: BLE001 — every failure is `unreachable`, never raised (P15)
        return {"status": "unreachable", "why": str(exc)[:400]}
    return {"status": "answered", "text": reply.get("result", ""), "model": f"claude-cli/{model}",
            "seconds": round(time.time() - started, 1), "cost": reply.get("total_cost_usd"),
            "usage": reply.get("usage")}


def backend_route(pack: str, prefer: str | None) -> dict:
    import route as rt
    started = time.time()
    try:
        rec = rt.chat({"messages": [{"role": "user", "content": pack}], "max_tokens": 6000, "temperature": 0},
                    purpose="ask", prefer=prefer)
    except rt.Refused as exc:
        return {"status": "refused", "why": str(exc)}
    if "unreached" in rec:
        return {"status": "unreachable", "why": rec["unreached"][:400]}
    return {"status": "answered", "text": rec["content"], "model": f"route/{rec['model']}",
            "seconds": round(time.time() - started, 1), "cost": 0}


def cmd_run(qid: str, backend: str, model: str | None, attempt: int = 0) -> dict:
    d = run_dir(qid)
    pack, meta = load_pack(qid)
    out = d / f"raw.{tag(backend, attempt)}.json"
    if backend not in ("session", "jules") and out.exists():
        sys.exit(f"{out.relative_to(ROOT)} exists: a run is never overwritten; pass --attempt {attempt + 1}")
    if backend == "claude-cli":
        res = backend_claude_cli(pack, model or "sonnet")
    elif backend == "route":
        res = backend_route(pack, model)
    elif backend in ("session", "jules"):
        raw = out
        if not raw.exists():
            sys.exit(f"{raw.relative_to(ROOT)} is absent: the {backend} backend writes it; "
                     f"then run `ask.py verify {qid} --backend {backend}`")
        res = json.loads(raw.read_text(encoding="utf-8"))
    else:
        sys.exit(f"unknown backend {backend!r}")
    if backend in ("session", "jules") and res.get("pack_hash") not in (None, meta["hash"]):
        sys.exit(f"{out.relative_to(ROOT)} answers another pack ({res['pack_hash'][:12]})")
    res.update(backend=backend, attempt=attempt, at=res.get("at") or now(), pack_hash=meta["hash"])
    out.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    with (RUNS / "ledger.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps({k: res.get(k) for k in ("at", "backend", "model", "status", "seconds", "cost")}
                           | {"id": qid, "attempt": attempt}, ensure_ascii=False) + "\n")
    print(f"{qid} {backend}: {res['status']} {res.get('model', '')} {res.get('seconds', '')}s "
          f"cost {res.get('cost')}")
    return res


# ── verify ────────────────────────────────────────────────────────────────────

def parse(text: str) -> dict | None:
    text = (text or "").strip()
    m = re.search(r"\{.*\}", text, re.S)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


ANSWERABLE = ("yes", "partly", "no")


def schema_errors(answer) -> list[str]:
    """What makes a parsed answer break the contract SCHEMA states; [] when it holds."""
    if not isinstance(answer, dict):
        return ["the answer is not an object"]
    errs = []
    if answer.get("answerable") not in ANSWERABLE:
        errs.append(f"answerable is {answer.get('answerable')!r}, not one of {ANSWERABLE}")
    claims = answer.get("claims")
    if not isinstance(claims, list):
        errs.append("claims is not a list")
        claims = []
    for i, c in enumerate(claims):
        if not isinstance(c, dict):
            errs.append(f"claims[{i}] is not an object")
            continue
        if not isinstance(c.get("doc"), str) or not isinstance(c.get("says"), str):
            errs.append(f"claims[{i}]: doc and says must be strings")
        qs = c.get("quotes", [])
        if not isinstance(qs, list):
            errs.append(f"claims[{i}].quotes is not a list")
            continue
        for j, q in enumerate(qs):
            if not isinstance(q, dict) or not isinstance(q.get("text"), str):
                errs.append(f"claims[{i}].quotes[{j}] has no text string")
            elif q.get("line_hint") is not None and not isinstance(q.get("line_hint"), int):
                errs.append(f"claims[{i}].quotes[{j}].line_hint is not an integer")
    for key in ("differ", "gaps"):
        v = answer.get(key, [])
        if not isinstance(v, list) or not all(isinstance(x, str) for x in v):
            errs.append(f"{key} is not a list of strings")
    for key in ("need", "next"):
        v = answer.get(key, [])
        if not isinstance(v, list) or not all(isinstance(x, dict) for x in v):
            errs.append(f"{key} is not a list of objects")
    return errs


def place(doc_slug: str, quote: str, hint, shown: list[int]) -> tuple[str, int | None, str | None]:
    """(`placed` | `outside-window` | `unresolved`, line, why) — by quotes.py's own comparison.

    A quotation is placed only on a line the pack sent. The same words elsewhere in the
    document are `outside-window`: true of the source, but not read from the pack.
    """
    import read
    from subject import document
    sent = sorted(set(shown), key=lambda n: (abs(n - hint) if isinstance(hint, int) else 0, n))
    for n in sent:
        if quotes.verdict([f"{doc_slug}.md:L{n}"], None, quote)[0] == "verified":
            return "placed", n, None
    try:
        lines = read.locate(document(doc_slug), quote)
    except KeyError:
        return "unresolved", None, "no such document"
    if lines:
        return "outside-window", None, f"the words stand on L{lines[0]}, which the pack did not send"
    return "unresolved", None, "the words stand on no single line"


def verify(answer: dict | None, shown: dict[str, list[int]]) -> dict:
    """`shown` is the pack's meta["shown"]: every document and the line numbers it sent."""
    empty = {"claims": [], "unsupported": [], "differ": [], "differ_dropped": [], "gaps": [],
             "next": [], "need": [], "counts": {}}
    if answer is None:
        return {"status": "unparsed"} | empty
    errs = schema_errors(answer)
    if errs:
        return {"status": "schema-invalid", "why": "; ".join(errs[:8])} | empty
    claims, unsupported, counts = [], [], {"placed": 0, "unresolved": 0, "outside-pack": 0, "outside-window": 0}
    supported_docs = set()
    for c in answer.get("claims", []) or []:
        doc = str(c.get("doc", "")).removesuffix(".md")
        checked = []
        for q in c.get("quotes", []) or []:
            text = str(q.get("text", "")).strip().strip("„“\"")
            if doc not in shown:
                status, line, why = "outside-pack", None, "the pack held no text of this document"
            else:
                status, line, why = place(doc, text, q.get("line_hint"), shown[doc])
            counts[status] = counts.get(status, 0) + 1
            checked.append({"text": text, "status": status, "line": line, "why": why})
        good = [q for q in checked if q["status"] == "placed"]
        row = {"doc": doc, "says": c.get("says", ""), "quotes": checked}
        if good:
            claims.append(row)
            supported_docs.add(doc)
        else:
            unsupported.append(row)
    differ = [x for x in answer.get("differ", []) or []
              if sum(1 for d in supported_docs if d in str(x)) >= 2]
    return {"status": "answered", "answerable": answer.get("answerable"), "claims": claims,
            "unsupported": unsupported, "differ": differ,
            "differ_dropped": [x for x in answer.get("differ", []) or [] if x not in differ],
            "gaps": answer.get("gaps", []) or [], "next": answer.get("next", []) or [],
            "need": answer.get("need", []) or [], "counts": counts}


def score(v: dict, gold: set[tuple[str, int]], shown: dict[str, list[int]]) -> dict:
    """The answer metric for optimizing a rules card (Plan/concept/dspy-learning_2026-09-30.md).

    `score` is None — could not score, never 0 or 1 — for an unparsed or schema-invalid
    answer or one with no quotation. `fabricated` counts words standing on no line of their
    document; it is a veto, reported beside the score and never averaged into it.
    """
    c = v.get("counts", {})
    total = sum(c.values())
    if v.get("status") != "answered" or not total:
        return {"score": None, "why": v.get("status") if v.get("status") != "answered" else "no quotation",
                "precision": None, "gold_hit": None, "fabricated": 0}
    precision = c.get("placed", 0) / total
    fabricated = sum(1 for row in v["claims"] + v["unsupported"] for q in row["quotes"]
                     if q["status"] == "unresolved" and "no single line" in str(q["why"]))
    sent_gold = {(d, n) for d, n in gold if n in set(shown.get(d, ()))}
    hit = {(row["doc"], q["line"]) for row in v["claims"] for q in row["quotes"] if q["status"] == "placed"}
    gold_hit = len(sent_gold & hit) / len(sent_gold) if sent_gold else None
    s = precision if gold_hit is None else 0.7 * precision + 0.3 * gold_hit
    return {"score": round(s, 3), "precision": round(precision, 3),
            "gold_hit": None if gold_hit is None else round(gold_hit, 3), "fabricated": fabricated,
            "vetoed": fabricated > 0, "why": None}


def dates() -> dict[str, str]:
    import askdb
    return {r["slug"]: r.get("index_date", "") for r in askdb.manifest()}


def render(qid: str, meta: dict, raw: dict, v: dict) -> str:
    when = dates()
    out = ["---", f"id: ask-{qid}", "tier: M-ask", "kind: answer", f"question: {json.dumps(meta['question'], ensure_ascii=False)}",
           f"backend: {raw.get('backend')}", f"model: {raw.get('model', '')}", f"answered: {raw.get('at')}",
           f"pack: Plan/runs/ask/{qid}/pack.md", f"pack_hash: {meta['hash']}",
           f"placed: {v['counts'].get('placed', 0)}", f"unresolved: {v['counts'].get('unresolved', 0)}",
           f"outside_pack: {v['counts'].get('outside-pack', 0)}",
           f"outside_window: {v['counts'].get('outside-window', 0)}", "---", "",
           f"# Antwort: {meta['question']}", "",
           f"**Eine Modell-Lesart der Quellen (Entscheidung 017, Tier `M-ask`), keine Entscheidung.** "
           f"Backend `{raw.get('backend')}`, Modell `{raw.get('model', '')}`; "
           f"beantwortbar laut Modell: `{v.get('answerable')}`. Jedes Zitat unten hat Code auf seine Zeile gesetzt.", ""]
    if v["status"] != "answered":
        out += [f"Status: **{v['status']}** — {v.get('why') or raw.get('why') or 'die Antwort war kein lesbares JSON'}", ""]
        return "\n".join(out)
    for c in sorted(v["claims"], key=lambda c: (when.get(c["doc"], ""), c["doc"])):
        out.append(f"## `{c['doc']}`, {when.get(c['doc'], 'undatiert')}")
        out.append("")
        out.append(c["says"])
        out.append("")
        for q in c["quotes"]:
            if q["status"] == "placed":
                out.append(f"> „{q['text']}\" ^[{c['doc']}.md:L{q['line']}]")
                out.append("")
    if v["differ"]:
        out += ["## Wo die Quellen auseinandergehen", ""] + [f"- {x}" for x in v["differ"]] + [""]
    if v["gaps"]:
        out += ["## Was das Paket nicht hält", ""] + [f"- {x}" for x in v["gaps"]] + [""]
    if v["next"]:
        out += ["## Wo weiterlesen", ""] + [f"- `{x.get('doc')}`: {x.get('why', '')}" for x in v["next"]] + [""]
    if v["unsupported"] or v["differ_dropped"]:
        out += ["## Verworfen — ohne platziertes Zitat", ""]
        for c in v["unsupported"]:
            reasons = "; ".join(f"{q['status']}: {q['why']}" for q in c["quotes"]) or "kein Zitat"
            out.append(f"- `{c['doc']}`: {c['says']} — {reasons}")
        out += [f"- Vergleich ohne zwei belegte Seiten: {x}" for x in v["differ_dropped"]]
        out.append("")
    return "\n".join(out)


def load_raw(qid: str, backend: str, attempt: int, meta: dict) -> dict:
    raw = json.loads((run_dir(qid) / f"raw.{tag(backend, attempt)}.json").read_text(encoding="utf-8"))
    if raw.get("pack_hash") != meta["hash"]:
        sys.exit(f"{qid} {tag(backend, attempt)}: the answer names pack {str(raw.get('pack_hash'))[:12]}, "
                 f"the pack is {meta['hash'][:12]}")
    return raw


def cmd_verify(qid: str, backend: str, attempt: int = 0) -> tuple[str, dict]:
    d = run_dir(qid)
    _, meta = load_pack(qid)
    raw = load_raw(qid, backend, attempt, meta)
    v = verify(parse(raw.get("text", "")) if raw.get("status") == "answered" else None, meta["shown"])
    if raw.get("status") != "answered":
        v["status"] = raw.get("status", "unparsed")
    backend = tag(backend, attempt)
    text = render(qid, meta, raw, v)
    (d / f"answer.{backend}.json").write_text(json.dumps(v, ensure_ascii=False, indent=1), encoding="utf-8")
    (d / f"answer.{backend}.md").write_text(text, encoding="utf-8")
    print(f"{qid} {backend}: {v['status']}, {len(v['claims'])} supported claims, "
          f"{len(v['unsupported'])} unsupported, quotes {v['counts']}")
    return text, v


# ── land ──────────────────────────────────────────────────────────────────────

def cmd_land(qid: str, backend: str, attempt: int = 0) -> Path:
    d = run_dir(qid)
    _, meta = load_pack(qid)
    raw = load_raw(qid, backend, attempt, meta)
    backend = tag(backend, attempt)
    text = (d / f"answer.{backend}.md").read_text(encoding="utf-8")
    if f"pack_hash: {meta['hash']}" not in text:
        sys.exit(f"answer.{backend}.md was rendered from another pack; run verify again")
    LANDED.mkdir(parents=True, exist_ok=True)
    slug = f"ask-{qid}-{backend}"
    target = LANDED / f"{slug}.md"
    if target.exists():
        sys.exit(f"{target.relative_to(ROOT)} is landed already; an answer is never edited (decision 017)")
    target.write_text(text, encoding="utf-8")
    row = {"slug": slug, "tier": "M-ask", "question": meta["question"], "backend": backend,
           "model": raw.get("model"), "answered": raw.get("at"), "landed": now(),
           "export_path": str(target.relative_to(ROOT)), "pack_hash": meta["hash"],
           "sha256": sha(text), "attempt": attempt}
    with MANIFEST.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"landed {target.relative_to(ROOT)}")
    return target


# ── bench: pack recall against the records, no model ─────────────────────────

REF = re.compile(r"\^\[([a-z0-9-]+)\.md:L(\d+)")


def bench_cases() -> list[dict]:
    out = []
    for folder, kind in (("conflicts", "conflict"), ("questions", "question")):
        for p in sorted((ROOT / "Wiki" / folder).glob("[cq]*.md")):
            text = p.read_text(encoding="utf-8")
            head = text.split("\n---\n", 1)[0]
            rid = re.search(r"^id: (\w+)", head, re.M).group(1)
            if kind == "question":
                q = re.search(r"^question: (.*)$", head, re.M).group(1)
            else:
                q = re.search(r"^# \w+ — (.*)$", text, re.M).group(1)
            gold = {(m.group(1), int(m.group(2))) for m in REF.finditer(text)}
            out.append({"id": rid, "key": f"{kind}:{rid}", "question": q, "gold": gold})
    return out


def bench(budget: int = BUDGET) -> dict:
    import askdb
    import graph as kg
    import graphrag
    s, g = askdb.Store(), kg.build()
    rows = []
    for c in bench_cases():
        if not c["gold"]:
            continue
        _, meta = build_pack(c["question"], "position", budget, s, graphrag.without(g, c["key"]))
        docs = {d for d, _ in c["gold"]}
        shown = {d: set(v) for d, v in meta["shown"].items()}
        line_hits = sum(1 for d, l in c["gold"] if l in shown.get(d, ()))
        doc_hits = len(docs & set(shown))
        rows.append({"id": c["id"], "gold_docs": len(docs), "doc_recall": round(doc_hits / len(docs), 3),
                     "gold_lines": len(c["gold"]), "line_recall": round(line_hits / len(c["gold"]), 3),
                     "pack_docs": len(shown), "chars": meta["chars"]})
        print(f"{c['id']:4} docs {doc_hits:3}/{len(docs):3}  lines {line_hits:4}/{len(c['gold']):4}  "
              f"pack {len(shown):3} docs {meta['chars']:6} chars", flush=True)
    mean = lambda k: round(sum(r[k] for r in rows) / len(rows), 3)
    result = {"cases": len(rows), "doc_recall": mean("doc_recall"), "line_recall": mean("line_recall"),
              "budget": budget, "rows": rows}
    print(f"\n{len(rows)} cases: document recall {result['doc_recall']}, line recall {result['line_recall']}")
    return result


# ── self-test ─────────────────────────────────────────────────────────────────

def selftest() -> list[str]:
    fails = []
    if parse('```json\n{"answerable": "no"}\n```') != {"answerable": "no"}:
        fails.append("parse does not strip a fence")
    if parse("kein json") is not None:
        fails.append("parse accepted text")
    # a real line of a real document, and three defects around it
    import askdb
    s = askdb.Store()
    hit = s.bm25("Juna erste direkte Erscheinung", limit=1)
    if not hit:
        return fails + ["the store finds no line to test with"]
    slug, line, text = hit[0]["slug"], hit[0]["line"], hit[0]["text"]
    words = " ".join(re.sub(r"[*_\\]", "", text).split()[:6])
    answer = {"answerable": "yes", "claims": [
        {"doc": slug, "says": "richtig", "quotes": [{"text": words, "line_hint": line}]},
        {"doc": slug, "says": "falsche Wörter", "quotes": [{"text": "Juna tanzt auf dem Mond im Kapitel", "line_hint": line}]},
        {"doc": "nicht-im-paket", "says": "außerhalb", "quotes": [{"text": words, "line_hint": line}]},
        {"doc": slug, "says": "ohne Zitat", "quotes": []}],
        "differ": [f"{slug} vs nicht-im-paket: erfunden"]}
    v = verify(answer, {slug: [line]})
    if [c["says"] for c in v["claims"]] != ["richtig"]:
        fails.append(f"only the true quotation should stand: {[c['says'] for c in v['claims']]} ({words!r})")
    if v["counts"].get("unresolved") != 1:
        fails.append(f"wrong words not named unresolved: {v['counts']}")
    if v["counts"].get("outside-pack") != 1:
        fails.append(f"a document outside the pack not named: {v['counts']}")
    if v["differ"]:
        fails.append("a comparison with one supported side survived")
    if len(v["unsupported"]) != 3:
        fails.append(f"three claims should be unsupported: {len(v['unsupported'])}")
    # review finding 3: right words, right document, a line the pack did not send
    w = verify({"answerable": "yes", "claims": [{"doc": slug, "says": "x", "quotes": [{"text": words, "line_hint": line}]}]},
               {slug: [line + 40, line + 41]})
    if w["claims"] or w["counts"].get("outside-window") != 1:
        fails.append(f"a quotation outside the sent window was accepted: {w['counts']}")
    # review finding 5: valid JSON, wrong schema — a status, never an exception
    for bad in ({"claims": "oops"}, {"answerable": "yes", "claims": [{"quotes": "oops"}]}, {}, [],
                {"answerable": "yes", "claims": [{"doc": slug, "says": "x", "quotes": [{"text": 3}]}]}):
        try:
            b = verify(bad, {slug: [line]})
        except Exception as exc:  # noqa: BLE001
            fails.append(f"schema {bad!r} raised {type(exc).__name__}")
            continue
        if b["status"] != "schema-invalid" or not b.get("why"):
            fails.append(f"schema {bad!r} not named schema-invalid: {b['status']}")
    # the metric: an answer that is all outside the window scores low, a crash is never 0 or 1
    sc = score(w, {(slug, line)}, {slug: [line + 40, line + 41]})
    if sc["score"] != 0.0 or sc["gold_hit"] is not None:
        fails.append(f"score of an out-of-window answer: {sc}")
    sc = score(v, {(slug, line)}, {slug: [line]})
    # one placed, one invented, one outside the pack: the invented one vetoes
    if not (sc["gold_hit"] == 1.0 and sc["precision"] == 0.333 and sc["fabricated"] == 1 and sc["vetoed"]):
        fails.append(f"score of one placed, one invented, one outside: {sc}")
    if score({"status": "schema-invalid", "counts": {}}, set(), {})["score"] is not None:
        fails.append("a schema-invalid answer got a score")
    fab = verify({"answerable": "yes", "claims": [{"doc": slug, "says": "x",
                  "quotes": [{"text": "Kein Satz dieser Art steht irgendwo in diesem Dokument", "line_hint": line}]}]},
                 {slug: [line]})
    if not score(fab, set(), {slug: [line]})["vetoed"]:
        fails.append("a fabricated quotation did not veto")
    # review finding 2: a pack is immutable, a run is never overwritten
    import tempfile
    global RUNS
    keep = RUNS
    with tempfile.TemporaryDirectory(dir=ROOT / "Plan" / "derived") as tmp:
        RUNS = Path(tmp)
        try:
            d = run_dir("t")
            d.mkdir()
            (d / "pack.md").write_text("paket", encoding="utf-8")
            (d / "pack.json").write_text(json.dumps({"hash": sha("paket"), "shown": {}}), encoding="utf-8")
            (d / "raw.jules.json").write_text(json.dumps({"status": "answered", "text": "{}"}), encoding="utf-8")
            cmd_run("t", "jules", None)
            if json.loads((d / "raw.jules.json").read_text())["pack_hash"] != sha("paket"):
                fails.append("a run does not record the pack it answered")
            (d / "pack.md").write_text("paket, verändert", encoding="utf-8")
            for step in (lambda: cmd_verify("t", "jules"), lambda: cmd_run("t", "jules", None)):
                try:
                    step()
                    fails.append("an edited pack was accepted")
                except SystemExit:
                    pass
            (d / "pack.md").write_text("paket", encoding="utf-8")
            (d / "raw.route.json").write_text("{}", encoding="utf-8")
            try:
                cmd_run("t", "route", None)
                fails.append("a second run overwrote the first")
            except SystemExit:
                pass
        finally:
            RUNS = keep
    # review finding 1: a landed answer resolves by slug and its quotation verifies
    import subject
    with tempfile.TemporaryDirectory(dir=ROOT / "Plan" / "derived") as tmp:
        body = "---\nid: ask-test\n---\n\nDiese Modellantwort soll zitierbar sein.\n"
        f = Path(tmp) / "ask-test.md"
        f.write_text(body, encoding="utf-8")
        m = Path(tmp) / "manifest.jsonl"
        m.write_text(json.dumps({"slug": "ask-test", "export_path": str(f.relative_to(ROOT)),
                                 "sha256": sha(body), "answered": "2026-09-30"}) + "\n", encoding="utf-8")
        keep_m = subject.ASK_MANIFEST
        subject.ASK_MANIFEST = m
        subject.answers.cache_clear()
        try:
            if quotes.verdict(["ask-test.md:L5"], None, "Diese Modellantwort soll zitierbar sein.")[0] != "verified":
                fails.append("a landed answer's quotation does not verify")
            if any(d.slug == "ask-test" for d in subject.documents()):
                fails.append("a landed answer entered the corpus")
        finally:
            subject.ASK_MANIFEST = keep_m
            subject.answers.cache_clear()
    return fails


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd, rest = argv[0], argv[1:]

    def opt(name, default=None):
        return rest[rest.index(name) + 1] if name in rest else default
    positional = [a for i, a in enumerate(rest) if not a.startswith("--") and (i == 0 or not rest[i - 1].startswith("--"))]
    backend = opt("--backend", "claude-cli")
    attempt = int(opt("--attempt", 0))
    if cmd == "selftest":
        fails = selftest()
        for f in fails:
            print("FAIL", f)
        print(f"ask selftest: {'held' if not fails else 'FAILED'}")
        return 1 if fails else 0
    if cmd == "bench":
        res = bench(int(opt("--budget", BUDGET)))
        out = RUNS / f"bench-{time.strftime('%Y-%m-%d')}-{res['budget']}.json"
        out.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
        return 0
    if cmd == "pack":
        cmd_pack(positional[0], opt("--kind", "explain"))
    elif cmd == "run":
        cmd_run(positional[0], backend, opt("--model"), attempt)
    elif cmd == "verify":
        cmd_verify(positional[0], backend, attempt)
    elif cmd == "land":
        cmd_land(positional[0], backend, attempt)
    elif cmd == "ask":
        qid = cmd_pack(positional[0], opt("--kind", "explain"))
        res = cmd_run(qid, backend, opt("--model"), attempt)
        _, v = cmd_verify(qid, backend, attempt)
        if v["status"] == "answered":
            cmd_land(qid, backend, attempt)
    else:
        print(f"unknown command {cmd!r}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
