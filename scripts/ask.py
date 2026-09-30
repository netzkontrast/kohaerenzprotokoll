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
4. **verify** (code): every quotation must name a document in the pack and is
   placed on its line by `quotes.py`'s own comparison, or it is rejected; a claim
   with no placed quotation is `unsupported`.
5. **land**: the rendered answer goes to `Sources/ask/<id>.md` with a checksum
   and a manifest row, once; a second landing of the same id is refused.

    .venv-dspy/bin/python scripts/ask.py pack "Wann erscheint Juna zuerst direkt?" [--kind locate]
    .venv-dspy/bin/python scripts/ask.py run <id> --backend claude-cli [--model sonnet]
    .venv-dspy/bin/python scripts/ask.py run <id> --backend route
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
WINDOW = 3            # lines on each side of an anchor
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


def ask_id(question: str) -> str:
    return time.strftime("%Y-%m-%d") + "-" + hashlib.sha256(question.encode()).hexdigest()[:8]


def run_dir(qid: str) -> Path:
    return RUNS / qid


# ── route ─────────────────────────────────────────────────────────────────────

def route(question: str, kind: str, store=None) -> dict:
    import graphrag
    import askdb
    s = store or askdb.Store()
    evidence = graphrag.retrieve(question)
    anchors: list[dict] = []
    for ev in evidence["evidence"]:
        anchors.append({"doc": ev["doc"], "line": ev["line"], "finder": "graph-evidence"})
    for r in s.bm25(question, limit=BM25_HITS):
        anchors.append({"doc": r["slug"], "line": r["line"], "finder": "bm25-lines"})
    for r in evidence.get("unread_routes", []):
        line = int(str(r["via"]).rsplit(":L", 1)[-1]) if ":L" in str(r["via"]) else None
        if line:
            anchors.append({"doc": r["doc"], "line": line, "finder": "entity-unread"})
    path = []
    seeds = [x["term"] for x in evidence["seeds"]]
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


def build_pack(question: str, kind: str = "explain", budget: int = BUDGET, store=None) -> tuple[str, dict]:
    import graphrag
    import askdb
    s = store or askdb.Store()
    r = route(question, kind, s)
    parts, sent, cut, used = [], [], [], 0
    parts.append(f"# Frage\n\n{question}\n\nArt der Frage: `{kind}`\n")
    parts.append(RULES)
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
            lo, hi = max(1, line - WINDOW), line + WINDOW
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
                n += 1
            rows.append("…")
        read = "gelesen" if d["doc"] in r["evidence_docs"] else "ungelesen"
        block = (f"\n### `{d['doc']}` — {when.get(d['doc']) or 'undatiert'}, {tiers.get(d['doc'], '')}, {read}; "
                 f"gefunden von: {', '.join(sorted(d['finders']))}\n\n" + "\n".join(rows) + "\n")
        if used + len(block) > budget:
            cut.append(d["doc"])
            continue
        used += len(block)
        windows.append(block)
        sent.append(d["doc"])
    parts.append("".join(windows))
    skills = skills_for(question)
    if skills:
        parts.append("## Passende Skills (Auszug)\n\n" + "\n".join(
            f"- **{x['skill']}**: {x['description']}" for x in skills) + "\n")
    parts.append(SCHEMA)
    text = "\n".join(parts)
    meta = {"id": ask_id(question), "question": question, "kind": kind, "built": now(),
            "sends_text_of": sent, "cut_by_budget": cut, "budget": budget, "chars": len(text),
            "window_chars": used, "finders": {d["doc"]: sorted(d["finders"]) for d in r["docs"]},
            "seeds": [x["term"] for x in r["evidence"]["seeds"]], "skills": [x["skill"] for x in skills],
            "hash": hashlib.sha256(text.encode()).hexdigest()}
    return text, meta


def cmd_pack(question: str, kind: str) -> str:
    text, meta = build_pack(question, kind)
    d = run_dir(meta["id"])
    d.mkdir(parents=True, exist_ok=True)
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


def cmd_run(qid: str, backend: str, model: str | None) -> dict:
    d = run_dir(qid)
    pack = (d / "pack.md").read_text(encoding="utf-8")
    if backend == "claude-cli":
        res = backend_claude_cli(pack, model or "sonnet")
    elif backend == "route":
        res = backend_route(pack, model)
    elif backend in ("session", "jules"):
        raw = d / f"raw.{backend}.json"
        if not raw.exists():
            sys.exit(f"{raw.relative_to(ROOT)} is absent: the {backend} backend writes it; "
                     f"then run `ask.py verify {qid} --backend {backend}`")
        res = json.loads(raw.read_text(encoding="utf-8"))
    else:
        sys.exit(f"unknown backend {backend!r}")
    res.update(backend=backend, at=now(), pack_hash=json.loads((d / "pack.json").read_text())["hash"])
    (d / f"raw.{backend}.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    with (RUNS / "ledger.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps({k: res.get(k) for k in ("at", "backend", "model", "status", "seconds", "cost")}
                           | {"id": qid}, ensure_ascii=False) + "\n")
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


def place(doc_slug: str, quote: str, hint) -> tuple[str, int | None, str | None]:
    """(`placed` | `unresolved`, line, why) — by quotes.py's own comparison."""
    import read
    from subject import document
    if isinstance(hint, int) and quotes.verdict([f"{doc_slug}.md:L{hint}"], None, quote)[0] == "verified":
        return "placed", hint, None
    try:
        doc = document(doc_slug)
    except Exception:  # noqa: BLE001
        return "unresolved", None, "no such document"
    lines = read.locate(doc, quote)
    if not lines:
        return "unresolved", None, "the words stand on no single line"
    best = min(lines, key=lambda n: abs(n - hint)) if isinstance(hint, int) else lines[0]
    return "placed", best, None


def verify(answer: dict | None, in_pack: list[str]) -> dict:
    if answer is None:
        return {"status": "unparsed", "claims": [], "unsupported": [], "differ": [], "gaps": [],
                "next": [], "need": [], "counts": {}}
    claims, unsupported, counts = [], [], {"placed": 0, "unresolved": 0, "outside-pack": 0}
    supported_docs = set()
    for c in answer.get("claims", []) or []:
        doc = str(c.get("doc", "")).removesuffix(".md")
        checked = []
        for q in c.get("quotes", []) or []:
            text = str(q.get("text", "")).strip().strip("„“\"")
            if doc not in in_pack:
                status, line, why = "outside-pack", None, "the pack held no text of this document"
            else:
                status, line, why = place(doc, text, q.get("line_hint"))
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


def dates() -> dict[str, str]:
    import askdb
    return {r["slug"]: r.get("index_date", "") for r in askdb.manifest()}


def render(qid: str, meta: dict, raw: dict, v: dict) -> str:
    when = dates()
    out = ["---", f"id: ask-{qid}", "tier: M-ask", "kind: answer", f"question: {json.dumps(meta['question'], ensure_ascii=False)}",
           f"backend: {raw.get('backend')}", f"model: {raw.get('model', '')}", f"answered: {raw.get('at')}",
           f"pack: Plan/runs/ask/{qid}/pack.md", f"pack_hash: {meta['hash']}",
           f"placed: {v['counts'].get('placed', 0)}", f"unresolved: {v['counts'].get('unresolved', 0)}",
           f"outside_pack: {v['counts'].get('outside-pack', 0)}", "---", "",
           f"# Antwort: {meta['question']}", "",
           f"**Eine Modell-Lesart der Quellen (Entscheidung 017, Tier `M-ask`), keine Entscheidung.** "
           f"Backend `{raw.get('backend')}`, Modell `{raw.get('model', '')}`; "
           f"beantwortbar laut Modell: `{v.get('answerable')}`. Jedes Zitat unten hat Code auf seine Zeile gesetzt.", ""]
    if v["status"] != "answered":
        out += [f"Status: **{v['status']}** — {raw.get('why', 'die Antwort war kein lesbares JSON')}", ""]
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


def cmd_verify(qid: str, backend: str) -> tuple[str, dict]:
    d = run_dir(qid)
    meta = json.loads((d / "pack.json").read_text(encoding="utf-8"))
    raw = json.loads((d / f"raw.{backend}.json").read_text(encoding="utf-8"))
    v = verify(parse(raw.get("text", "")) if raw.get("status") == "answered" else None, meta["sends_text_of"])
    if raw.get("status") != "answered":
        v["status"] = raw.get("status", "unparsed")
    text = render(qid, meta, raw, v)
    (d / f"answer.{backend}.json").write_text(json.dumps(v, ensure_ascii=False, indent=1), encoding="utf-8")
    (d / f"answer.{backend}.md").write_text(text, encoding="utf-8")
    print(f"{qid} {backend}: {v['status']}, {len(v['claims'])} supported claims, "
          f"{len(v['unsupported'])} unsupported, quotes {v['counts']}")
    return text, v


# ── land ──────────────────────────────────────────────────────────────────────

def cmd_land(qid: str, backend: str) -> Path:
    d = run_dir(qid)
    text = (d / f"answer.{backend}.md").read_text(encoding="utf-8")
    LANDED.mkdir(parents=True, exist_ok=True)
    slug = f"ask-{qid}-{backend}"
    target = LANDED / f"{slug}.md"
    if target.exists():
        sys.exit(f"{target.relative_to(ROOT)} is landed already; an answer is never edited (decision 017)")
    target.write_text(text, encoding="utf-8")
    meta = json.loads((d / "pack.json").read_text(encoding="utf-8"))
    raw = json.loads((d / f"raw.{backend}.json").read_text(encoding="utf-8"))
    row = {"slug": slug, "tier": "M-ask", "question": meta["question"], "backend": backend,
           "model": raw.get("model"), "answered": raw.get("at"), "landed": now(),
           "export_path": str(target.relative_to(ROOT)), "pack_hash": meta["hash"],
           "sha256": hashlib.sha256(text.encode()).hexdigest()}
    with MANIFEST.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(f"landed {target.relative_to(ROOT)}")
    return target


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
    v = verify(answer, [slug])
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
    if cmd == "selftest":
        fails = selftest()
        for f in fails:
            print("FAIL", f)
        print(f"ask selftest: {'held' if not fails else 'FAILED'}")
        return 1 if fails else 0
    if cmd == "pack":
        cmd_pack(positional[0], opt("--kind", "explain"))
    elif cmd == "run":
        cmd_run(positional[0], backend, opt("--model"))
    elif cmd == "verify":
        cmd_verify(positional[0], backend)
    elif cmd == "land":
        cmd_land(positional[0], backend)
    elif cmd == "ask":
        qid = cmd_pack(positional[0], opt("--kind", "explain"))
        res = cmd_run(qid, backend, opt("--model"))
        cmd_verify(qid, backend)
        if res["status"] == "answered":
            cmd_land(qid, backend)
    else:
        print(f"unknown command {cmd!r}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
