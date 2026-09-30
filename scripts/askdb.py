#!/usr/bin/env python3
"""The store `ask` answers from: one derived SQLite file, GraphQLite and FTS5 together.

`Plan/concept/ask-sources_2026-09-30.md` §3.1 has the design; decision 017 the
standing of what `ask` writes. This module builds and reads `Plan/derived/ask.db`:

- **the stated graph** — `graph.py`'s nodes and typed edges, every edge keeping
  `via`, the file line that states it; every landed document as a `Doc` node
  (read or not, from the manifest); the chapter pages as `Chapter` nodes that
  `READ` the documents their reading headings name; the decision sheets as
  `Sheet` nodes that `DEPEND_ON` what their head's `hängt_ab_von` names;
- **the proposal graph** — verified entity lists as `Entity` nodes with
  `P_NAMED_IN` edges (a model chose the name, code placed the line). Every
  proposal relation type starts with `P_`, and no query for stated facts names one;
- **full text** — `lines`: every non-empty line of every landed document;
  `quotes`: every verified quotation on a term page. FTS5, `bm25()` ranking,
  no vectors.

It is derived and never committed (P25): `build` rebuilds it from the files and
`check` compares it with them (P8). GraphQLite needs `.venv-dspy/bin/python`.

    .venv-dspy/bin/python scripts/askdb.py build
    .venv-dspy/bin/python scripts/askdb.py check
    .venv-dspy/bin/python scripts/askdb.py bm25 "Juna erscheint" [--limit 10]
    .venv-dspy/bin/python scripts/askdb.py ppr term:juna term:aegis [--k 15]
    .venv-dspy/bin/python scripts/askdb.py path term:juna term:aegis
    .venv-dspy/bin/python scripts/askdb.py cypher "MATCH (c:Conflict) RETURN c.id"
    .venv-dspy/bin/python scripts/askdb.py sheets
    .venv-dspy/bin/python scripts/askdb.py selftest
"""

from __future__ import annotations

import json
import re
import sqlite3
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

DB = ROOT / "Plan" / "derived" / "ask.db"
DRIVE = ROOT / "Sources" / "drive"
MANIFEST = ROOT / "Sources" / "manifest.jsonl"
CHAPTERS = ROOT / "Wiki" / "chapters"
SHEETS = ROOT / "Plan" / "weichen"
READING = re.compile(r"^## Reading — `([^`]+)`", re.M)
TOKENIZER = "unicode61 remove_diacritics 2"


def _graphqlite():
    try:
        from graphqlite import Graph
    except ImportError:
        sys.exit("graphqlite is not installed here: run with .venv-dspy/bin/python "
                 "(scripts/install.sh dspy installs it)")
    return Graph


def scalar(v):
    """GraphQLite stores scalars; a list or dict is kept as its JSON text."""
    if v is None or isinstance(v, (str, int, float, bool)):
        return v
    return json.dumps(v, ensure_ascii=False)


# ── what the files state ──────────────────────────────────────────────────────

def manifest() -> list[dict]:
    rows = [json.loads(l) for l in MANIFEST.read_text(encoding="utf-8").splitlines() if l.strip()]
    return [r for r in rows if r.get("export_path")]


def sheet_heads() -> dict[str, dict]:
    heads = {}
    for p in sorted(SHEETS.glob("*.md")):
        text = p.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            continue
        head = text.split("\n---\n", 1)[0]
        fields = {}
        for line in head.splitlines()[1:]:
            m = re.match(r"([\wäöü_]+):\s*(.*?)\s*(?:#.*)?$", line)
            if m:
                fields[m.group(1)] = m.group(2).strip().strip('"')
        if "id" in fields:
            deps = fields.get("hängt_ab_von", "").strip("[]")
            fields["deps"] = [d.strip() for d in deps.split(",") if d.strip()]
            fields["file"] = str(p.relative_to(ROOT))
            heads[fields["id"]] = fields
    return heads


def collect() -> dict:
    """Everything the store holds, as plain rows — built from the files only."""
    import graph as kg
    g = kg.build()
    nodes: dict[str, tuple[dict, str]] = {}
    edges: list[tuple[str, str, dict, str]] = []

    for key, n in g["nodes"].items():
        props = {k: scalar(v) for k, v in n.items() if k != "id"}
        nodes[key] = (props, n["type"].capitalize())
    for e in g["edges"]:
        edges.append((e["source"], e["target"], {"via": e["via"]}, e["type"].upper()))

    for r in manifest():
        key = f"doc:{r['slug']}"
        props = {"slug": r["slug"], "title": r.get("title", ""), "date": r.get("index_date", ""),
                 "category": r.get("category", ""), "tier": r.get("tier", ""),
                 "read": key in g["nodes"]}
        if key in nodes:
            nodes[key][0].update(props)
        else:
            nodes[key] = (props, "Doc")

    for p in sorted(CHAPTERS.glob("kap-*.md")):
        key = f"chapter:{p.stem}"
        text = p.read_text(encoding="utf-8")
        nodes[key] = ({"slug": p.stem, "path": str(p.relative_to(ROOT))}, "Chapter")
        for m in READING.finditer(text):
            line = text.count("\n", 0, m.start()) + 1
            target = f"doc:{m.group(1)}"
            if target in nodes:
                edges.append((key, target, {"via": f"{p.relative_to(ROOT)}:{line}"}, "READS"))

    heads = sheet_heads()
    for sid, h in heads.items():
        nodes[f"sheet:{sid}"] = ({"slug": sid, "status": h.get("status", ""),
                                  "frage_art": h.get("frage_art", ""),
                                  "empfehlung": h.get("empfehlung", ""),
                                  "auslöser": h.get("auslöser", ""), "file": h["file"]}, "Sheet")
    for sid, h in heads.items():
        for d in h["deps"]:
            target = f"conflict:{d}" if re.fullmatch(r"C\d+", d) else f"sheet:{d}"
            if target not in nodes:          # named, but no sheet or record exists
                nodes[target] = ({"slug": d, "status": "kein Blatt", "file": ""}, "Sheet")
            edges.append((f"sheet:{sid}", target, {"via": h["file"]}, "DEPENDS_ON"))

    # the proposal graph: a model chose the names, code placed the lines
    try:
        import entities
        matrix = entities.load_matrix()["entities"]
    except Exception:                         # no lists yet: the stated graph stands alone
        matrix = {}
    for name, meta in matrix.items():
        key = f"entity:{name}"
        nodes[key] = ({"name": name, "kinds": scalar(meta.get("kinds")),
                       "documents": meta.get("documents", 0)}, "Entity")
        for slug, (n, first) in meta.get("in", {}).items():
            if f"doc:{slug}" in nodes:
                edges.append((key, f"doc:{slug}", {"n": n, "line": first}, "P_NAMED_IN"))

    quotes = [(ev["doc"], ev["line"], ev["quote"], page)
              for page, evs in g.get("evidence", {}).items()
              for ev in evs if ev.get("status") == "verified" and ev.get("doc")]
    return {"nodes": nodes, "edges": edges, "quotes": quotes,
            "stated_types": sorted({e["type"].upper() for e in g["edges"]} | {"READS", "DEPENDS_ON"})}


# ── build and check ───────────────────────────────────────────────────────────

def build(db: Path = DB) -> dict:
    Graph = _graphqlite()
    t0 = time.time()
    data = collect()
    if db.exists():
        db.unlink()
    db.parent.mkdir(parents=True, exist_ok=True)
    g = Graph(str(db))
    ids = g.insert_nodes_bulk([(k, p, label) for k, (p, label) in data["nodes"].items()])
    n_edges = g.insert_edges_bulk(data["edges"], ids)
    conn = sqlite3.connect(str(db))
    conn.execute(f"CREATE VIRTUAL TABLE lines USING fts5(slug UNINDEXED, line UNINDEXED, text, tokenize='{TOKENIZER}')")
    conn.execute(f"CREATE VIRTUAL TABLE quotes USING fts5(slug UNINDEXED, line UNINDEXED, text, page UNINDEXED, tokenize='{TOKENIZER}')")
    n_lines = 0
    for r in manifest():
        path = ROOT / r["export_path"]
        if not path.exists():
            continue
        rows = [(r["slug"], i, l.rstrip("\n")) for i, l in enumerate(path.read_text(encoding="utf-8").split("\n"), 1) if l.strip()]
        conn.executemany("INSERT INTO lines VALUES (?,?,?)", rows)
        n_lines += len(rows)
    conn.executemany("INSERT INTO quotes VALUES (?,?,?,?)", data["quotes"])
    stats = {"built": time.strftime("%Y-%m-%dT%H:%M:%S"), "seconds": round(time.time() - t0, 1),
             "nodes": len(data["nodes"]), "edges": n_edges, "lines": n_lines, "quotes": len(data["quotes"]),
             "labels": dict(Counter(label for _, label in data["nodes"].values())),
             "types": dict(Counter(t for *_, t in data["edges"])),
             "stated_types": data["stated_types"]}
    conn.execute("CREATE TABLE meta (key TEXT PRIMARY KEY, value TEXT)")
    conn.execute("INSERT INTO meta VALUES ('stats', ?)", (json.dumps(stats, ensure_ascii=False),))
    conn.commit()
    conn.close()
    stats["mb"] = round(db.stat().st_size / 1e6, 1)
    return stats


def stats(db: Path = DB) -> dict:
    conn = sqlite3.connect(str(db))
    return json.loads(conn.execute("SELECT value FROM meta WHERE key='stats'").fetchone()[0])


def check(db: Path = DB) -> list[str]:
    """What the store says against what the files say now (P8)."""
    if not db.exists():
        return [f"{db.relative_to(ROOT)} does not exist: run build"]
    want = collect()
    have = stats(db)
    problems = []
    if have["nodes"] != len(want["nodes"]):
        problems.append(f"nodes: store {have['nodes']}, files {len(want['nodes'])}")
    if have["edges"] != len(want["edges"]):
        problems.append(f"edges: store {have['edges']}, files {len(want['edges'])}")
    if have["quotes"] != len(want["quotes"]):
        problems.append(f"quotes: store {have['quotes']}, files {len(want['quotes'])}")
    lines = sum(1 for r in manifest() if (ROOT / r["export_path"]).exists()
                for l in (ROOT / r["export_path"]).read_text(encoding="utf-8").split("\n") if l.strip())
    if have["lines"] != lines:
        problems.append(f"lines: store {have['lines']}, files {lines}")
    leaked = [t for t in have["stated_types"] if t.startswith("P_")]
    if leaked:
        problems.append(f"a stated relation type looks like a proposal: {leaked}")
    return problems


# ── reading the store ─────────────────────────────────────────────────────────

class Store:
    def __init__(self, db: Path = DB):
        if not db.exists():
            sys.exit(f"{db.relative_to(ROOT)} does not exist: run askdb.py build")
        Graph = _graphqlite()
        self.g = Graph(str(db))
        self.sql = sqlite3.connect(str(db))
        self._ext: dict[int, str] | None = None

    def cypher(self, q: str) -> list[dict]:
        return self.g.query(q)

    def ext(self) -> dict[int, str]:
        if self._ext is None:
            self._ext = {r["i"]: r["k"] for r in self.cypher("MATCH (n) RETURN id(n) AS i, n.id AS k")}
        return self._ext

    def internal(self, keys: list[str]) -> list[int]:
        rev = {v: k for k, v in self.ext().items()}
        return [rev[k] for k in keys if k in rev]

    def ppr(self, seeds: list[str], k: int = 20) -> list[tuple[str, float]]:
        ids = self.internal(seeds)
        if not ids:
            return []
        rows = self.cypher(f"RETURN personalizedPageRank('{json.dumps(ids)}')")
        ranked = next(iter(rows[0].values())) if rows else []
        ext = self.ext()
        return [(ext[r["node_id"]], r["score"]) for r in ranked if r["node_id"] in ext][:k]

    def degree(self) -> dict[str, int]:
        return {r["k"]: r["d"] for r in self.cypher(
            "MATCH (n)-[r]-() WHERE NOT type(r) STARTS WITH 'P_' RETURN n.id AS k, count(r) AS d")}

    def path(self, a: str, b: str) -> dict:
        return self.g.shortest_path(a, b)

    def communities(self) -> dict[str, int]:
        return {r["user_id"]: r["community"] for r in self.g.louvain()}

    def via(self, a: str, b: str) -> list[dict]:
        return self.cypher(f"MATCH (x {{id:'{a}'}})-[r]-(y {{id:'{b}'}}) "
                           "WHERE NOT type(r) STARTS WITH 'P_' RETURN type(r) AS t, r.via AS via")

    def bm25(self, query: str, table: str = "lines", limit: int = 20,
             slugs: list[str] | None = None) -> list[dict]:
        match = fts_query(query)
        if not match:
            return []
        cols = "slug, line, text" + (", page" if table == "quotes" else "")
        where = f"{table} MATCH ?"
        args: list = [match]
        if slugs:
            where += f" AND slug IN ({','.join('?' * len(slugs))})"
            args += slugs
        rows = self.sql.execute(f"SELECT {cols}, bm25({table}) FROM {table} WHERE {where} "
                                f"ORDER BY bm25({table}) LIMIT ?", args + [limit]).fetchall()
        keys = cols.split(", ") + ["score"]
        return [dict(zip(keys, r)) for r in rows]

    def window(self, slug: str, first: int, last: int) -> list[tuple[int, str]]:
        return self.sql.execute("SELECT line, text FROM lines WHERE slug=? AND line BETWEEN ? AND ? "
                                "ORDER BY line", (slug, first, last)).fetchall()


STOP = set("der die das und oder ein eine einer eines ist sind wird werden wie was wer wann wo "
           "warum welche welcher welches mit von zu im in am an auf aus für bei nicht nur auch "
           "the a an of and or is are to in on for what when who how why which".split())


def fts_query(text: str) -> str:
    """Content words as an OR query, each quoted, so no FTS5 syntax slips in."""
    words = [w for w in re.findall(r"\w[\w-]*", text) if len(w) > 2 and w.lower() not in STOP]
    return " OR ".join(f'"{w}"' for w in dict.fromkeys(words))


# ── the decision sheets as a graph (§3.8) ─────────────────────────────────────

def sheets(s: Store) -> dict:
    deps = defaultdict(list)
    for r in s.cypher("MATCH (a:Sheet)-[:DEPENDS_ON]->(b) RETURN a.slug AS a, b.id AS b"):
        deps[r["a"]].append(r["b"].split(":", 1)[1].upper() if r["b"].startswith("conflict:") else r["b"].split(":", 1)[1])
    info = {r["k"]: r for r in s.cypher(
        "MATCH (n:Sheet) RETURN n.slug AS k, n.status AS status, n.frage_art AS art, n.file AS file")}
    unlocks = defaultdict(list)
    for a, bs in deps.items():
        for b in bs:
            unlocks[b].append(a)
    missing = sorted(k for k, v in info.items() if not v["file"])
    # cycles: strongly connected components of size > 1, Tarjan over the small graph
    index, low, stack, on, comps, i = {}, {}, [], set(), [], [0]

    def visit(v):
        index[v] = low[v] = i[0]; i[0] += 1; stack.append(v); on.add(v)
        for w in deps.get(v, []):
            if w not in index:
                visit(w); low[v] = min(low[v], low[w])
            elif w in on:
                low[v] = min(low[v], index[w])
        if low[v] == index[v]:
            comp = []
            while True:
                w = stack.pop(); on.discard(w); comp.append(w)
                if w == v:
                    break
            if len(comp) > 1:
                comps.append(sorted(comp))
    for v in list(info) + [b for bs in deps.values() for b in bs]:
        if v not in index:
            visit(v)
    return {"unlocks": {k: sorted(v) for k, v in sorted(unlocks.items(), key=lambda kv: -len(kv[1]))},
            "missing": missing, "cycles": comps,
            "open_key": sorted(k for k, v in info.items() if v["status"] == "offen" and v["art"] == "schlüssel")}


# ── self-test ─────────────────────────────────────────────────────────────────

def selftest() -> list[str]:
    import tempfile
    Graph = _graphqlite()
    fails = []
    probe = fts_query('Juna AND "x" NEAR(')
    if probe != '"Juna" OR "NEAR"':
        fails.append(f"fts_query leaked syntax: {probe!r}")
    with tempfile.TemporaryDirectory() as d:
        db = Path(d) / "t.db"
        g = Graph(str(db))
        ids = g.insert_nodes_bulk([("term:a", {"slug": "a"}, "Term"), ("term:b", {"slug": "b"}, "Term"),
                                   ("sheet:W1", {"slug": "W1", "status": "offen", "frage_art": "schlüssel", "file": "x"}, "Sheet"),
                                   ("sheet:W2", {"slug": "W2", "status": "offen", "frage_art": "standard", "file": "y"}, "Sheet"),
                                   ("sheet:W9", {"slug": "W9", "status": "kein Blatt", "file": ""}, "Sheet")])
        g.insert_edges_bulk([("term:a", "term:b", {"via": "f.md:3"}, "LINKS"),
                             ("sheet:W1", "sheet:W2", {"via": "x"}, "DEPENDS_ON"),
                             ("sheet:W2", "sheet:W1", {"via": "y"}, "DEPENDS_ON"),
                             ("sheet:W2", "sheet:W9", {"via": "y"}, "DEPENDS_ON")], ids)
        conn = sqlite3.connect(str(db))
        conn.execute(f"CREATE VIRTUAL TABLE lines USING fts5(slug UNINDEXED, line UNINDEXED, text, tokenize='{TOKENIZER}')")
        conn.executemany("INSERT INTO lines VALUES (?,?,?)", [("d1", 1, "Juna erscheint in Kap 38"),
                                                              ("d1", 2, "Kael zählt Platten"),
                                                              ("d2", 7, "Die Kohärenz fällt")])
        conn.commit()
        s = Store(db)
        if [r["slug"] for r in s.bm25("Wann erscheint Juna?")] != ["d1"]:
            fails.append("bm25 did not find the one line naming Juna")
        if not s.bm25("Kohaerenz") and not s.bm25("Kohärenz"):
            fails.append("bm25 found no Kohärenz line")
        if s.ppr(["term:a"])[:1] and s.ppr(["term:a"])[0][0] != "term:a":
            fails.append("personalized PageRank does not rank its own seed first")
        if s.via("term:a", "term:b") != [{"t": "LINKS", "via": "f.md:3"}]:
            fails.append(f"via lost the stating line: {s.via('term:a', 'term:b')}")
        sh = sheets(s)
        if sh["cycles"] != [["W1", "W2"]]:
            fails.append(f"cycle not found: {sh['cycles']}")
        if sh["missing"] != ["W9"]:
            fails.append(f"missing sheet not found: {sh['missing']}")
        if sh["open_key"] != ["W1"]:
            fails.append(f"open key questions wrong: {sh['open_key']}")
    return fails


# ── command line ──────────────────────────────────────────────────────────────

def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd, rest = argv[0], argv[1:]
    if cmd == "build":
        print(json.dumps(build(), ensure_ascii=False, indent=1))
        return 0
    if cmd == "check":
        problems = check()
        for p in problems:
            print("DIFFERS ", p)
        print("store matches the files" if not problems else f"{len(problems)} difference(s)")
        return 1 if problems else 0
    if cmd == "selftest":
        fails = selftest()
        for f in fails:
            print("FAIL", f)
        print(f"askdb selftest: {'held' if not fails else 'FAILED'}")
        return 1 if fails else 0
    s = Store()
    limit = int(rest[rest.index("--limit") + 1]) if "--limit" in rest else 10
    args = [a for i, a in enumerate(rest) if a != "--limit" and (i == 0 or rest[i - 1] != "--limit")]
    if cmd == "bm25":
        for r in s.bm25(" ".join(args), limit=limit):
            print(f"{r['slug']}.md:L{r['line']}\t{r['score']:.2f}\t{r['text'][:140]}")
    elif cmd == "ppr":
        for k, sc in s.ppr(args, k=limit):
            print(f"{sc:.4f}\t{k}")
    elif cmd == "path":
        p = s.path(args[0], args[1])
        print(json.dumps(p, ensure_ascii=False))
        for a, b in zip(p.get("path", []), p.get("path", [])[1:]):
            print(a, "→", b, s.via(a, b))
    elif cmd == "cypher":
        for r in s.cypher(" ".join(args)):
            print(json.dumps(r, ensure_ascii=False))
    elif cmd == "sheets":
        print(json.dumps(sheets(s), ensure_ascii=False, indent=1))
    else:
        print(f"unknown command {cmd!r}")
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
