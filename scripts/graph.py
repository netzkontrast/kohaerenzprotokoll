"""The wiki as a typed knowledge graph, every edge carrying the line that states it.

`relations.py` answers *which page links which*. A knowledge graph for
retrieval needs more, and all of it is already written down — in frontmatter,
in `[[links]]`, in `^[slug.md:Lnn]` citations. Nothing here is extracted by a
model and nothing is inferred: **a guessed edge is indistinguishable from a
stated one once it is in the graph** (decision 005), so an edge exists only
where a file states it, and `via` names that file and line.

Nodes:

| id | from | carries |
|---|---|---|
| `term:<slug>` | `Wiki/candidates/<slug>.md` | term, surfaces (every form the index folds to it), status, conflict |
| `doc:<slug>` | `Sources/manifest.jsonl`, for every document a page reads or cites | title, category, date |
| `conflict:<Cn>` | `Wiki/conflicts/*.md` | subject, kind, status |
| `question:<Qn>` | `Wiki/questions/*.md` | question, status |

Edges (`source -type-> target`, each with `via: file:line`):

| type | stated by |
|---|---|
| `links` | `[[slug]]` in a page's prose — the only term→term edge |
| `reads` | a page's `ingested:` list — the page carries a reading of that document |
| `cites` | `^[slug.md:Lnn]` on a page — with every cited line, so a retriever can go to the passage |
| `contests` | a conflict's `pages:` |
| `raised_by` | a question's `raised_by:` — question → the page that asks it |
| `asks` | a question's `documents:` |
| `concerns` | a question's `conflict:` |

And **evidence**: every quotation on a page with its citation, its section
heading, and whether `quotes.py`'s own comparison resolves it against the
cited line (`verified` / `unresolved` / `unchecked`). That is the unit a
GraphRAG retriever serves, and it is checked here, not trusted.

`--check` compares the graph against the filesystem (P7, P8): an edge to a page
that does not exist, a document no manifest row lands, a conflict or question
naming a page that is gone.

    python3 scripts/graph.py                    # counts, then the check; exit 1 on a disagreement
    python3 scripts/graph.py --json             # the whole graph
    python3 scripts/graph.py --graphml > kg.graphml   # for Gephi, networkx, a GraphRAG store
    python3 scripts/graph.py --triples          # subject<TAB>predicate<TAB>object<TAB>via
    python3 scripts/graph.py --around nexus [--hops 2] [--mermaid]
    python3 scripts/graph.py --proposals [--missing]   # entity lists and stated glosses, kept apart
    python3 scripts/graph.py --selftest
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, deque
from functools import lru_cache
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import quotes  # noqa: E402
import wiki_index  # noqa: E402
from subject import rows as manifest_rows  # noqa: E402

PAGES = ROOT / "Wiki" / "candidates"
CONFLICTS = ROOT / "Wiki" / "conflicts"
QUESTIONS = ROOT / "Wiki" / "questions"
LINK = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]*))?\]\]")
CITED_DOC = re.compile(r"([A-Za-z0-9][A-Za-z0-9\-]*)\.md:L(\d+)")
HEADING = re.compile(r"^(#{1,4}) (.*)$")


def _line_of(text: str, needle: str) -> int:
    for number, line in enumerate(text.split("\n"), 1):
        if needle in line:
            return number
    return 1


def _rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def evidence_of(path: Path, text: str) -> list[dict]:
    """Every quotation on a page, with its citation, section and verdict.

    Pairing and verdict are `quotes.pairs` and `quotes.verdict` — the same code
    `quotes.py` checks with, so a quotation served as evidence here is verified
    exactly when the checker says it is. A quotation with no resolvable citation
    is `unchecked` and kept: P23 says count what could not be checked.
    """
    lines = text.split("\n")
    starts = [0]
    for line in lines:
        starts.append(starts[-1] + len(line) + 1)

    def line_at(pos: int) -> int:
        lo, hi = 0, len(starts) - 1
        while lo < hi - 1:
            mid = (lo + hi) // 2
            lo, hi = (mid, hi) if starts[mid] <= pos else (lo, mid)
        return lo

    section, sections = "", []
    for line in lines:
        match = HEADING.match(line)
        if match:
            section = match.group(2).strip()
        sections.append(section)

    default = quotes.slug_of(path)
    out = []
    for match, refs in quotes.pairs(text):
        status, _ = quotes.verdict(refs, default, match.group("quote"))
        ref = quotes.REF.match(refs[0]) if refs else None
        out.append({"quote": " ".join(quotes.WRAP.sub(" ", match.group("quote")).split()),
                    "page_line": line_at(match.start()) + 1,
                    "section": sections[line_at(match.start())],
                    "ref": refs[0] if refs else None,
                    "doc": (ref.group("slug") or default) if ref else None,
                    "line": int(ref.group("line")) if ref else None,
                    "status": status})
    return out


@lru_cache(maxsize=1)
def build() -> dict:
    index = wiki_index.build()
    manifest = {r["slug"]: r for r in manifest_rows()}
    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    evidence: dict[str, list[dict]] = {}

    def doc_node(slug: str) -> str:
        key = f"doc:{slug}"
        if key not in nodes:
            row = manifest.get(slug, {})
            nodes[key] = {"id": key, "type": "doc", "slug": slug, "title": row.get("title"),
                          "category": row.get("category"), "date": row.get("index_date"),
                          "landed": bool(row.get("export_path"))}
        return key

    def edge(src: str, kind: str, dst: str, via: str, **extra) -> None:
        edges.append({"source": src, "type": kind, "target": dst, "via": via, **extra})

    for path in sorted(PAGES.glob("*.md")):
        slug, text = path.stem, path.read_text(encoding="utf-8")
        meta = wiki_index.frontmatter(text)
        row = index["terms"].get(slug, {})
        nodes[f"term:{slug}"] = {
            "id": f"term:{slug}", "type": "term", "slug": slug,
            "term": meta.get("term", slug), "status": meta.get("status"),
            "surfaces": row.get("surfaces", [meta.get("term", slug)]),
            "conflict": meta.get("conflict"), "path": _rel(path)}
        for doc in meta.get("ingested", []) or []:
            edge(f"term:{slug}", "reads", doc_node(doc), f"{_rel(path)}:{_line_of(text, 'ingested:')}")
        seen: set[str] = set()
        for number, line in enumerate(text.split("\n"), 1):
            for m in LINK.finditer(line):
                target = m.group(1).strip()
                if target == slug or target in seen:
                    continue
                seen.add(target)
                edge(f"term:{slug}", "links", f"term:{target}", f"{_rel(path)}:{number}",
                     anchor=m.group(2) or target)
        cited: dict[str, list[int]] = {}
        for m in CITED_DOC.finditer(text):
            cited.setdefault(m.group(1), []).append(int(m.group(2)))
        for doc, lines_ in cited.items():
            edge(f"term:{slug}", "cites", doc_node(doc),
                 f"{_rel(path)}:{_line_of(text, doc + '.md:L')}", lines=sorted(set(lines_)))
        evidence[slug] = evidence_of(path, text)

    for path in sorted(CONFLICTS.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        meta = wiki_index.frontmatter(text)
        key = f"conflict:{meta.get('id', path.stem)}"
        nodes[key] = {"id": key, "type": "conflict", "subject": meta.get("subject"),
                      "kind": meta.get("kind"), "status": meta.get("status"), "path": _rel(path)}
        for page in meta.get("pages", []) or []:
            edge(key, "contests", f"term:{page}", f"{_rel(path)}:{_line_of(text, 'pages:')}")

    for path in sorted(QUESTIONS.glob("q*.md")):
        text = path.read_text(encoding="utf-8")
        meta = wiki_index.frontmatter(text)
        key = f"question:{meta.get('id', path.stem)}"
        # The flat frontmatter parser cannot read a value holding a `"`, and Q4's
        # does. Read that one line raw rather than widen the shared parser.
        raw = re.search(r"^question:\s*(.+)$", text, re.M)
        question = meta.get("question") or (raw.group(1).strip().strip('"') if raw else None)
        nodes[key] = {"id": key, "type": "question", "question": question,
                      "status": meta.get("status"), "path": _rel(path)}
        for page in meta.get("raised_by", []) or []:
            edge(key, "raised_by", f"term:{page}", f"{_rel(path)}:{_line_of(text, 'raised_by:')}")
        for doc in meta.get("documents", []) or []:
            edge(key, "asks", doc_node(doc), f"{_rel(path)}:{_line_of(text, 'documents:')}")
        # A question may name several conflicts (Q5: `C6, C9`); it concerns each.
        # Matching the whole value as one id kept one edge of three.
        for conflict in re.findall(r"\bC\d+\b", str(meta.get("conflict", ""))):
            edge(key, "concerns", f"conflict:{conflict}", f"{_rel(path)}:{_line_of(text, 'conflict:')}")

    return {"nodes": nodes, "edges": edges, "evidence": evidence}


GLOSS_MIN_DOCS = 2
STATED = ROOT / "Plan" / "runs" / "bilingual" / "stated.jsonl"


@lru_cache(maxsize=1)
def proposals() -> dict:
    """What a model chose or the corpus merely co-states — kept apart from the graph.

    Nothing here is an edge between term pages, and nothing enters `build()`.
    Each item says who chose it and who verified it:

    - **entities** — the names in `Plan/entities/<slug>.md`, from lists that pass
      `entities.py verify` as a reading (a reconstruction is left out, as `matrix`
      leaves it out). A model chose the name; code placed the line, so every
      `names` edge (document → entity, `via` the document line) is a verified
      fact that the document names it there. An entity whose fold equals a page
      surface gets `folds_to` that page — the lookup every reconcile uses.
    - **glosses** — from `Plan/runs/bilingual/stated.jsonl`, pairs the corpus
      writes itself. Only the `A (B)` shape, written in at least
      `GLOSS_MIN_DOCS` documents, where exactly one side is a page surface and
      the other is no page's surface. **The relation is unjudged:** `Kael (Host)`
      is a role, `Grenzfeste (Cerberus)` a place and its guardian, and the slash
      shape pairs opposites (`Kohärenz/Inkohärenz`). So a gloss may route a
      question to a page and is shown as a gloss; it never merges a surface into
      a page (P13, and `Plan/runs/judgements.jsonl` decides that).
    """
    import entities as E
    index = wiki_index.build()
    page_of: dict[str, str] = {}
    for slug, row in index["terms"].items():
        for surface in row.get("surfaces", []):
            if len(wiki_index.fold(surface)) >= 3:
                page_of.setdefault(wiki_index.fold(surface), f"term:{slug}")

    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    skipped = []
    for entry in E.lists():
        E.verify(entry)
        if not entry["reading"]:
            skipped.append(entry["slug"])
            continue
        path = f"Sources/drive/{entry['slug']}.md"
        for row in entry["rows"]:
            if not row["verified"]:
                continue
            key = f"entity:{wiki_index.fold(row['term'])}"
            node = nodes.setdefault(key, {"id": key, "type": "entity", "surfaces": [], "kinds": [],
                                          "named_by": [], "chosen_by": "model", "placed_by": "code"})
            if row["term"] not in node["surfaces"]:
                node["surfaces"].append(row["term"])
            if row["kind"] and row["kind"] not in node["kinds"]:
                node["kinds"].append(row["kind"])
            node["named_by"].append(entry["slug"])
            edges.append({"source": f"doc:{entry['slug']}", "type": "names", "target": key,
                          "via": f"{path}:{row['line']}", "rank": row["rank"]})
    for key, node in nodes.items():
        page = page_of.get(key.split(":", 1)[1])
        if page:
            edges.append({"source": key, "type": "folds_to", "target": page,
                          "via": "Wiki/index.json surfaces"})

    glosses = []
    if STATED.exists():
        for line in STATED.read_text(encoding="utf-8").splitlines():
            row = json.loads(line)
            if row.get("shape") != "paren" or row.get("docs", 0) < GLOSS_MIN_DOCS:
                continue
            fa, fb = wiki_index.fold(row["a"]), wiki_index.fold(row["b"])
            pa, pb = page_of.get(fa), page_of.get(fb)
            if bool(pa) == bool(pb):
                continue
            page, surface = (pa, row["b"]) if pa else (pb, row["a"])
            if len(wiki_index.fold(surface)) < 4:
                continue
            glosses.append({"surface": surface, "page": page, "pair": f"{row['a']} ({row['b']})",
                            "docs": row["docs"], "cites": row.get("cites", [])[:3]})
    # A surface glossing two different pages (`Ordnung` → Kohärenz and AEGIS,
    # `Anteile` → Alters and Personas) says nothing about which: drop it.
    pages_of: dict[str, set] = {}
    for g in glosses:
        pages_of.setdefault(wiki_index.fold(g["surface"]), set()).add(g["page"])
    glosses = [g for g in glosses if len(pages_of[wiki_index.fold(g["surface"])]) == 1]
    return {"nodes": nodes, "edges": edges, "glosses": glosses, "lists_skipped": skipped}


def check(graph: dict) -> list[str]:
    """Every way the graph can disagree with the files it was derived from."""
    problems = []
    nodes = graph["nodes"]
    for e in graph["edges"]:
        if e["target"] not in nodes and not e["target"].startswith("doc:"):
            problems.append(f"{e['via']}: {e['type']} → {e['target']}, which does not exist")
    for key, node in nodes.items():
        if node["type"] == "doc" and not node["landed"]:
            problems.append(f"{key} is read or cited, and no manifest row lands it")
    return problems


def selftest() -> list[str]:
    """The check names each defect it exists for — asserted on a damaged copy."""
    import copy
    failures = []
    g = copy.deepcopy(build())
    if check(g):
        failures.append(f"the real graph already disagrees: {check(g)[:2]}")
    g["edges"].append({"source": "term:aegis", "type": "links", "target": "term:no-such-page",
                       "via": "fixture:1"})
    g["nodes"]["doc:fixture-unlanded"] = {"id": "doc:fixture-unlanded", "type": "doc", "landed": False}
    found = check(g)
    if not any("no-such-page" in p for p in found):
        failures.append("an edge to a missing page was not reported")
    if not any("fixture-unlanded" in p for p in found):
        failures.append("a document no manifest row lands was not reported")
    core = {e["type"] for e in build()["edges"]}
    if core & {"names", "folds_to"}:
        failures.append("proposal edges leaked into the core graph")
    named = sum(len(re.findall(r"\bC\d+\b", str(wiki_index.frontmatter(p.read_text(encoding="utf-8")).get("conflict", ""))))
                for p in QUESTIONS.glob("q*.md"))
    concerns = sum(1 for e in build()["edges"] if e["type"] == "concerns")
    if concerns != named:
        failures.append(f"questions name {named} conflicts, graph.py holds {concerns} concerns edges")
    links = sum(1 for e in build()["edges"] if e["type"] == "links")
    import relations
    if links != len(relations.graph()["edges"]):
        failures.append(f"graph.py has {links} links, relations.py {len(relations.graph()['edges'])}")
    return failures


def neighbours(graph: dict, start: str, hops: int = 1, types: set[str] | None = None) -> dict[str, int]:
    """Node → distance, walking edges in both directions."""
    adjacent: dict[str, set[str]] = {}
    for e in graph["edges"]:
        if types and e["type"] not in types:
            continue
        adjacent.setdefault(e["source"], set()).add(e["target"])
        adjacent.setdefault(e["target"], set()).add(e["source"])
    seen, queue = {start: 0}, deque([start])
    while queue:
        node = queue.popleft()
        if seen[node] >= hops:
            continue
        for nxt in adjacent.get(node, ()):
            if nxt not in seen:
                seen[nxt] = seen[node] + 1
                queue.append(nxt)
    return seen


def mermaid(graph: dict, keep: set[str]) -> str:
    """A neighbourhood as Mermaid text — a picture a person reads, never an input."""
    safe = lambda k: re.sub(r"[^A-Za-z0-9_]", "_", k)  # noqa: E731
    label = lambda n: (n.get("term") or n.get("subject") or n.get("slug") or n["id"]).replace('"', "'")  # noqa: E731
    out = ["graph LR"]
    for key in sorted(keep):
        out.append(f'  {safe(key)}["{label(graph["nodes"].get(key, {"id": key}))}"]')
    for e in graph["edges"]:
        if e["source"] in keep and e["target"] in keep and e["type"] != "cites":
            out.append(f"  {safe(e['source'])} -->|{e['type']}| {safe(e['target'])}")
    return "\n".join(out)


def graphml(graph: dict) -> str:
    keys = ["type", "label", "status", "category"]
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<graphml xmlns="http://graphml.graphdrawing.org/xmlns">']
    for k in keys:
        out.append(f'  <key id="{k}" for="node" attr.name="{k}" attr.type="string"/>')
    out += ['  <key id="etype" for="edge" attr.name="type" attr.type="string"/>',
            '  <key id="via" for="edge" attr.name="via" attr.type="string"/>',
            '  <graph edgedefault="directed">']
    for key, n in graph["nodes"].items():
        label = n.get("term") or n.get("subject") or n.get("question") or n.get("title") or key
        data = {"type": n["type"], "label": label, "status": n.get("status"), "category": n.get("category")}
        cells = "".join(f'<data key="{k}">{escape(str(v))}</data>' for k, v in data.items() if v)
        out.append(f'    <node id="{escape(key)}">{cells}</node>')
    for i, e in enumerate(graph["edges"]):
        out.append(f'    <edge id="e{i}" source="{escape(e["source"])}" target="{escape(e["target"])}">'
                   f'<data key="etype">{e["type"]}</data><data key="via">{escape(e["via"])}</data></edge>')
    out += ["  </graph>", "</graphml>"]
    return "\n".join(out)


def stats(graph: dict) -> dict:
    ev = [e for items in graph["evidence"].values() for e in items]
    return {"nodes": dict(Counter(n["type"] for n in graph["nodes"].values())),
            "edges": dict(Counter(e["type"] for e in graph["edges"])),
            "evidence": dict(Counter(e["status"] for e in ev))}


def main(argv: list[str]) -> int:
    if "--selftest" in argv:
        problems = selftest()
        for p in problems:
            print(f"  FAIL  {p}")
        print(f"graph: {6 - len(problems)} of 6 cases hold (clean, broken edge, unlanded doc, "
              "no proposal in the core, every conflict a question names, agrees with relations.py)")
        return 1 if problems else 0
    graph = build()
    if "--json" in argv:
        print(json.dumps(graph, ensure_ascii=False, indent=1))
        return 0
    if "--graphml" in argv:
        print(graphml(graph))
        return 0
    if "--triples" in argv:
        for e in graph["edges"]:
            print(f"{e['source']}\t{e['type']}\t{e['target']}\t{e['via']}")
        return 0
    if "--proposals" in argv:
        prop = proposals()
        linked = {e["source"] for e in prop["edges"] if e["type"] == "folds_to"}
        missing = [n for k, n in prop["nodes"].items() if k not in linked]
        print(f"entities {len(prop['nodes'])} from reading lists "
              f"(skipped as reconstructions: {', '.join(prop['lists_skipped']) or 'none'}); "
              f"{len(linked)} fold to a page, {len(missing)} have none")
        print(f"glosses {len(prop['glosses'])} — `A (B)` in {GLOSS_MIN_DOCS}+ documents, one side a page")
        if "--missing" in argv:
            for n in sorted(missing, key=lambda n: (-len(set(n["named_by"])), n["surfaces"][0])):
                print(f"  {len(set(n['named_by']))}  {n['surfaces'][0]}  ({', '.join(n['kinds'])})")
        return 0
    if "--around" in argv:
        start = argv[argv.index("--around") + 1]
        start = start if ":" in start else f"term:{start}"
        if start not in graph["nodes"]:
            print(f"no node {start}")
            return 1
        hops = int(argv[argv.index("--hops") + 1]) if "--hops" in argv else 1
        near = neighbours(graph, start, hops)
        if "--mermaid" in argv:
            print(mermaid(graph, set(near)))
        else:
            for key, distance in sorted(near.items(), key=lambda kv: (kv[1], kv[0])):
                print(f"{distance}  {key}")
        return 0
    s = stats(graph)
    print("nodes    " + "  ".join(f"{k} {v}" for k, v in sorted(s["nodes"].items())))
    print("edges    " + "  ".join(f"{k} {v}" for k, v in sorted(s["edges"].items())))
    print("evidence " + "  ".join(f"{k} {v}" for k, v in sorted(s["evidence"].items())))
    problems = check(graph)
    for p in problems:
        print(f"  {p}")
    print(f"{len(problems)} places where the graph and the files disagree")
    return 1 if problems else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
