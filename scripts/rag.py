"""The project's retrieval tools, served from one file: the core of the MCP server (decision 029).

`graphrag.py`, `read.py` and `quotes.py` answer from the repository's files and from a
graph `graph.py` takes about thirty seconds to build. A serverless function has neither
the repository nor thirty seconds. So this script derives **one SQLite file** at build
time that holds everything the tools read, and answers every tool from it:

- `docs` — every landed document's body and the file line it starts on, so a line number
  here is the file line a citation names (`subject.Document`'s convention);
- `lines` — FTS5 over every non-empty line of every landed document;
- `quotes` — FTS5 over every **verified** quotation on a term page, with its page,
  document and line (the set `quotes.py` passes);
- `items` and `items_fts` — the wiki's pages, conflicts, questions and chapter pages, the
  reconciliation records, the notes and censuses, `NOW.md`, as markdown with their path;
- `blobs` — the graph and its proposal layer as `graph.py` builds them, the measurements of
  `Plan/state.json`, the next sessions of `sessions.py`, and the build's own facts.

Nothing is inferred and nothing is summarised: a tool returns rows with their document and
line, or a record's markdown with its path. **No tool writes prose about a source** (P13);
a client's model may answer from what it returns. `verify_quote` asks the question
`quotes.py` asks, through `read.py`'s own functions, of the same lines.

    python3 scripts/rag.py build [--out Plan/derived/serve/serve.db]
    python3 scripts/rag.py search "Juna Resonanz" [--scope sources|quotes|items] [--limit 10]
    python3 scripts/rag.py ask "Wie hängen die Guardians mit AEGIS zusammen?"
    python3 scripts/rag.py lines <slug> <from> <to>
    python3 scripts/rag.py verify <slug> "<the words>" [--line N]
    python3 scripts/rag.py item <kind> <id>          # page, conflict, question, chapter, record, note, census
    python3 scripts/rag.py selftest

The database is derived and never committed (`Plan/derived/`). `RAG_DB` names another
file; the MCP server (`api/mcp.py`) reads the one `web.py` builds for the deployment.
"""

from __future__ import annotations

import json
import os
import re
import sqlite3
import sys
import tempfile
import time
import zlib
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

DEFAULT_DB = ROOT / "Plan" / "derived" / "serve" / "serve.db"
TOKENIZER = "unicode61 remove_diacritics 2"
SCOPES = ("sources", "quotes", "items")
MAX_LIMIT = 50
MAX_WINDOW = 200
LINE_SPAN = 1_000_000     # a source line's rowid is document number × LINE_SPAN + file line
# What the server never serves (decision 029 §3, the author's rules of decision 028): a figure's earlier name and the
# trauma symbol, line by line, wherever they stand; and the whole text of a document nobody has read (the held ones)
# or whose note marks personal material. Their wiki pages and records are served; their lines are not.
WITHHELD_LINE = re.compile("|".join(("Mich" "ael", "Jul" "ia", "Sha" "dow", "Lost " "One", "Isab" "ella", "Kis" "sen",
                                     r"\bGe" r"lb")), re.I)
PERSONAL_NOTE = re.compile(r"personal material|real diagnosis|autobiograph|real person|real people|writing process", re.I)
WITHHELD_TEXT = "[withheld]"
STOP = set("aber alle auch dass dem den der des die das ein eine einem einen einer eines für ist mit nicht noch "
           "oder sich sind und von was wie wird zum zur über the and are does how what which with".split())
ITEM_KINDS = ("page", "conflict", "question", "chapter", "record", "note", "census", "decision", "now")


class Refused(ValueError):
    """A request this tool will not answer, with the reason in words."""


# ── build ──────────────────────────────────────────────────────────────────────

SCHEMA = f"""
CREATE TABLE docs (id INTEGER PRIMARY KEY, slug TEXT UNIQUE, title TEXT, category TEXT, date TEXT, tier TEXT,
                   read INTEGER, offset INTEGER, body BLOB);
CREATE VIRTUAL TABLE lines USING fts5(text, content='', tokenize='{TOKENIZER}');
CREATE VIRTUAL TABLE quotes USING fts5(page UNINDEXED, doc UNINDEXED, line UNINDEXED, section UNINDEXED, text,
                                       tokenize='{TOKENIZER}');
CREATE TABLE items (n INTEGER PRIMARY KEY, kind TEXT, id TEXT, path TEXT, title TEXT, markdown BLOB, UNIQUE (kind, id));
CREATE VIRTUAL TABLE items_fts USING fts5(title, text, content='', tokenize='{TOKENIZER}');
CREATE TABLE blobs (name TEXT PRIMARY KEY, json BLOB);
"""


def write(path: Path, docs: list[dict], quotes: list[dict], items: list[dict], blobs: dict) -> dict:
    """Write the serving file from rows already collected. Atomic: a half-built file is never served."""
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    if tmp.exists():
        tmp.unlink()
    con = sqlite3.connect(tmp)
    con.executescript(SCHEMA)
    n_lines, n_withheld = 0, 0
    docs = [{**d, "body": "\n".join(WITHHELD_TEXT if WITHHELD_LINE.search(ln) else ln for ln in d["body"].split("\n"))}
            for d in docs]
    n_withheld = sum(d["body"].split("\n").count(WITHHELD_TEXT) for d in docs)
    items = [{**it, "markdown": "\n".join(WITHHELD_TEXT if WITHHELD_LINE.search(ln) else ln
                                          for ln in it["markdown"].split("\n"))} for it in items]
    quotes = [q for q in quotes if not WITHHELD_LINE.search(q["quote"]) and not WITHHELD_LINE.search(q.get("section", ""))]
    for n, d in enumerate(docs, 1):
        con.execute("INSERT INTO docs VALUES (?,?,?,?,?,?,?,?,?)",
                    (n, d["slug"], d.get("title", ""), d.get("category", ""), d.get("date", ""), d.get("tier", ""),
                     1 if d.get("read") else 0, d["offset"], pack(d["body"])))
        # contentless: the index holds no text; a hit's rowid is the document and the file line
        rows = [(n * LINE_SPAN + d["offset"] + i, line) for i, line in enumerate(d["body"].split("\n"))
                if line.strip() and line != WITHHELD_TEXT]
        con.executemany("INSERT INTO lines (rowid, text) VALUES (?,?)", rows)
        n_lines += len(rows)
    con.executemany("INSERT INTO quotes VALUES (?,?,?,?,?)",
                    [(q["page"], q["doc"], q["line"], q.get("section", ""), q["quote"]) for q in quotes])
    for n, it in enumerate(items, 1):
        con.execute("INSERT INTO items VALUES (?,?,?,?,?,?)", (n, it["kind"], it["id"], it["path"], it["title"], pack(it["markdown"])))
        con.execute("INSERT INTO items_fts (rowid, title, text) VALUES (?,?,?)", (n, it["title"], it["markdown"]))
    facts = {"docs": len(docs), "lines": n_lines, "lines_withheld": n_withheld, "quotes": len(quotes), "items": len(items)}
    blobs = {**blobs, "build": {**blobs.get("build", {}), **facts}}
    con.executemany("INSERT INTO blobs VALUES (?,?)", [(k, pack(json.dumps(v, ensure_ascii=False))) for k, v in blobs.items()])
    con.commit()
    con.execute("VACUUM")
    con.close()
    os.replace(tmp, path)
    return facts


def pack(text: str) -> bytes:
    return zlib.compress(text.encode("utf-8"), 9)


def unpack(data: bytes) -> str:
    return zlib.decompress(data).decode("utf-8")


def withheld(text: str) -> bool:
    return bool(WITHHELD_LINE.search(text or ""))


def clean_graph(g: dict) -> dict:
    """The graph without a node, surface, edge or quotation that names what is withheld."""
    nodes = {}
    for key, n in g["nodes"].items():
        if withheld(key) or withheld(n.get("term", "")):
            continue
        nodes[key] = {**n, **({"surfaces": [x for x in n["surfaces"] if not withheld(x)]} if "surfaces" in n else {})}
    edges = [e for e in g["edges"] if e["source"] in nodes and e["target"] in nodes]
    evidence = {page: [ev for ev in evs if not withheld(ev.get("quote", "")) and not withheld(ev.get("section", ""))]
                for page, evs in g["evidence"].items() if not withheld(page)}
    return {**g, "nodes": nodes, "edges": edges, "evidence": evidence}


def collect() -> tuple[list[dict], list[dict], list[dict], dict]:
    """Every row the serving file holds, read from the repository by the scripts that own each kind."""
    import subprocess
    import graph
    import sessions
    import subject
    import wiki_index

    manifest = {r["slug"]: r for r in subject.rows()}
    read = {p.parent.name for p in (ROOT / "Plan" / "runs").glob("*/reconcile.json")}
    personal = {p.stem for p in (ROOT / "Sources" / "notes").glob("*.md")
                if PERSONAL_NOTE.search(p.read_text(encoding="utf-8"))}
    docs, held = [], {"unread": [], "personal": []}
    for d in subject.documents():
        if d.slug not in read or d.slug in personal:
            held["unread" if d.slug not in read else "personal"].append(d.slug)
            continue
        docs.append({"slug": d.slug, "title": manifest.get(d.slug, {}).get("title", d.slug), "category": d.category,
                     "date": d.date, "tier": manifest.get(d.slug, {}).get("tier", ""), "read": True,
                     "offset": d.offset, "body": d.body})

    g = clean_graph(graph.build())
    quotes = [{"page": page, "doc": ev["doc"], "line": ev["line"], "section": ev.get("section", ""), "quote": ev["quote"]}
              for page, evs in g["evidence"].items() for ev in evs if ev.get("status") == "verified"]

    items = []

    def add(kind: str, ident: str, path: Path) -> None:
        if withheld(ident):
            return
        text = path.read_text(encoding="utf-8")
        meta = wiki_index.frontmatter(text) if text.startswith("---") else {}
        body, _ = subject._split(text)
        title = meta.get("term") or next((ln[2:].strip() for ln in body.splitlines() if ln.startswith("# ")), ident)
        title = WITHHELD_TEXT if withheld(title) else title
        items.append({"kind": kind, "id": ident, "path": path.relative_to(ROOT).as_posix(), "title": title,
                      "markdown": text})

    for p in sorted((ROOT / "Wiki" / "candidates").glob("*.md")):
        add("page", p.stem, p)
    for p in sorted((ROOT / "Wiki" / "conflicts").glob("c*.md")):
        add("conflict", p.stem.split("-", 1)[0].upper(), p)
    for p in sorted((ROOT / "Wiki" / "questions").glob("q*.md")):
        add("question", p.stem.split("-", 1)[0].upper(), p)
    for p in sorted((ROOT / "Wiki" / "chapters").glob("kap-*.md")):
        add("chapter", str(int(p.stem.split("-")[1])), p)
    for p in sorted((ROOT / "Wiki" / "compare").glob("reconcile-*.md"), key=lambda p: int(p.stem.split("-")[1])):
        m = re.match(r"reconcile-\d+-(.+)$", p.stem)
        if m:
            add("record", m.group(1), p)
    for kind, folder in (("note", "notes"), ("census", "terms")):
        for p in sorted((ROOT / "Sources" / folder).glob("*.md")):
            add(kind, p.stem, p)
    for p in sorted((ROOT / "Plan" / "decisions").glob("[0-9]*.md")):
        add("decision", p.stem[:3], p)
    add("now", "NOW", ROOT / "NOW.md")

    # a document read twice has two records: the later file (higher number) is the one kept
    items = list({(it["kind"], it["id"]): it for it in items}.values())
    state = json.loads((ROOT / "Plan" / "state.json").read_text(encoding="utf-8"))
    plan = sessions.derive()
    head = subprocess.run(["git", "log", "-1", "--format=%h %cs"], cwd=ROOT, capture_output=True, text=True).stdout.split()
    if not head and os.environ.get("VERCEL_GIT_COMMIT_SHA"):
        head = [os.environ["VERCEL_GIT_COMMIT_SHA"][:7], time.strftime("%Y-%m-%d")]
    prop = graph.proposals()
    prop = {**prop, "nodes": {k: v for k, v in prop["nodes"].items() if not withheld(k)},
            "edges": [e for e in prop["edges"] if not withheld(e.get("source", "")) and not withheld(e.get("target", ""))],
            "glosses": [x for x in prop.get("glosses", []) if not withheld(str(x))]}
    blobs = {"withheld": {k: sorted(v) for k, v in held.items()}, "graph": g, "proposals": prop,
             "state": {k: {"value": v.get("value"), "how": v.get("how")} for k, v in state.get("measurements", {}).items()},
             "sessions": [{k: s.get(k) for k in ("id", "title", "status", "next_md", "files")} for s in plan.get("sessions", [])],
             "build": {"commit": head[0] if head else "", "date": head[1] if len(head) > 1 else "",
                       "built": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}}
    return docs, quotes, items, blobs


def build(path: Path = DEFAULT_DB) -> dict:
    started = time.time()
    facts = write(path, *collect())
    facts["seconds"] = round(time.time() - started, 1)
    facts["bytes"] = path.stat().st_size
    return facts


# ── serve ──────────────────────────────────────────────────────────────────────

class Store:
    """The serving file, opened read-only. The graph is parsed once, on first use."""

    def __init__(self, path: Path | str | None = None):
        self.path = Path(path or os.environ.get("RAG_DB") or DEFAULT_DB)
        if not self.path.exists():
            raise Refused(f"no serving index at {self.path}: python3 scripts/rag.py build")
        self.con = sqlite3.connect(f"file:{self.path}?mode=ro", uri=True, check_same_thread=False)
        self._blobs: dict = {}

    def blob(self, name: str):
        if name not in self._blobs:
            row = self.con.execute("SELECT json FROM blobs WHERE name = ?", (name,)).fetchone()
            self._blobs[name] = json.loads(unpack(row[0])) if row else None
        return self._blobs[name]

    # -- the tools --------------------------------------------------------------

    def search(self, query: str, scope: str = "sources", limit: int = 10) -> dict:
        if scope not in SCOPES:
            raise Refused(f"scope must be one of {', '.join(SCOPES)}, not {scope!r}")
        match = fts_query(query)
        if not match:
            raise Refused("the query has no word of four letters or more that is not a stop word")
        limit = max(1, min(int(limit), MAX_LIMIT))
        if scope == "sources":
            hits = []
            for (rowid,) in self.con.execute("SELECT rowid FROM lines WHERE lines MATCH ? ORDER BY bm25(lines) LIMIT ?",
                                             (match, limit)).fetchall():
                d, n = self._doc_by_id(rowid // LINE_SPAN), rowid % LINE_SPAN
                hits.append({"doc": d["slug"], "line": n, "text": d["lines"][n - d["offset"]], "title": d["title"],
                             "date": d["date"], "read": d["read"], "cite": f"{d['slug']}.md:L{n}"})
        elif scope == "quotes":
            rows = self.con.execute("SELECT page, doc, line, section, text FROM quotes WHERE quotes MATCH ? "
                                    "ORDER BY bm25(quotes) LIMIT ?", (match, limit)).fetchall()
            hits = [{"page": p, "doc": d, "line": n, "section": s, "quote": t, "cite": f"{d}.md:L{n}"}
                    for p, d, n, s, t in rows]
        else:
            words = [w.strip('"').lower() for w in match.split(" OR ")]
            hits = []
            for (rowid,) in self.con.execute("SELECT rowid FROM items_fts WHERE items_fts MATCH ? ORDER BY bm25(items_fts) "
                                             "LIMIT ?", (match, limit)).fetchall():
                k, i, p, t, md = self.con.execute("SELECT kind, id, path, title, markdown FROM items WHERE n = ?",
                                                  (rowid,)).fetchone()
                text = unpack(md)
                line = next((ln.strip() for ln in text.splitlines() if any(w in ln.lower() for w in words)), "")
                hits.append({"kind": k, "id": i, "path": p, "title": t, "snippet": line[:300]})
        return {"query": query, "scope": scope, "match": match, "hits": hits, **self.provenance()}

    def ask(self, question: str, k: int = 8, lines: int = 8) -> dict:
        """graphrag.retrieve over the stored graph, plus BM25 lines from the sources as a second finder."""
        import graphrag
        graph, proposals = self.blob("graph"), self.blob("proposals")
        if not graph:
            raise Refused("the serving index holds no graph")
        original = graphrag.kg.proposals
        graphrag.kg.proposals = lambda: proposals
        try:
            pack = graphrag.retrieve(question, graph=graph, budget=max(1, min(int(k), 20)))
        finally:
            graphrag.kg.proposals = original
        try:
            found = self.search(question, "sources", lines)["hits"]
        except Refused:
            found = []
        return {"question": question, "graph": pack, "source_lines": found,
                "note": "evidence, not an answer: every quotation carries its document and line", **self.provenance()}

    @lru_cache(maxsize=64)
    def _doc_by_id(self, n: int) -> dict:
        row = self.con.execute("SELECT slug, title, category, date, tier, read, offset, body FROM docs WHERE id = ?",
                               (n,)).fetchone()
        d = dict(zip(("slug", "title", "category", "date", "tier", "read", "offset", "body"), row))
        d["body"], d["read"] = unpack(d["body"]), bool(d["read"])
        d["lines"] = d["body"].split("\n")
        return d

    def document(self, slug: str) -> dict:
        row = self.con.execute("SELECT id FROM docs WHERE slug = ?", (slug,)).fetchone()
        if not row:
            raise Refused(f"no landed document with slug {slug!r}")
        return self._doc_by_id(row[0])

    def read_lines(self, slug: str, first: int, last: int) -> dict:
        d = self.document(slug)
        body = d["body"].split("\n")
        end = d["offset"] + len(body) - 1
        first, last = max(int(first), d["offset"]), min(int(last), end)
        if last < first:
            raise Refused(f"{slug} has lines {d['offset']}–{end}")
        if last - first + 1 > MAX_WINDOW:
            raise Refused(f"at most {MAX_WINDOW} lines per call")
        return {"doc": slug, "title": d["title"], "first": first, "last": last, "last_line": end,
                "lines": [{"line": n, "text": body[n - d["offset"]]} for n in range(first, last + 1)], **self.provenance()}

    def verify_quote(self, slug: str, quote: str, line: int | None = None) -> dict:
        """quotes.py's question, asked through read.py's functions of the same lines."""
        import read
        import subject
        d = self.document(slug)
        doc = subject.Document(slug=slug, category=d["category"], date=d["date"], format="md", sha256="",
                               path=Path(f"{slug}.md"), body=d["body"], offset=d["offset"])
        hits = read.locate(doc, quote)
        out = {"doc": slug, "quote": quote, "lines": hits, **self.provenance()}
        if line is not None:
            out["claimed"] = int(line)
            out["holds"] = int(line) in hits
        if not hits:
            out["spans"] = [list(s) for s in read.spans(doc, quote)]
            out["nearest"] = [{"line": n, "share": round(s, 2), "text": read.preview(t)} for s, n, t in read.nearest(doc, quote)]
        return out

    def item(self, kind: str, ident: str) -> dict:
        if kind not in ITEM_KINDS:
            raise Refused(f"kind must be one of {', '.join(ITEM_KINDS)}")
        ident = str(ident).strip()
        if kind in ("conflict", "question"):
            ident = ident.upper()
        if kind == "chapter":
            ident = str(int(re.sub(r"\D", "", ident) or -1))
        row = self.con.execute("SELECT kind, id, path, title, markdown FROM items WHERE kind = ? AND id = ?",
                               (kind, ident)).fetchone()
        if not row:
            raise Refused(f"no {kind} {ident!r}")
        return {**dict(zip(("kind", "id", "path", "title"), row[:4])), "markdown": unpack(row[4]), **self.provenance()}

    def listing(self, kind: str) -> dict:
        if kind not in ITEM_KINDS:
            raise Refused(f"kind must be one of {', '.join(ITEM_KINDS)}")
        rows = self.con.execute("SELECT id, title, path FROM items WHERE kind = ? ORDER BY id", (kind,)).fetchall()
        return {"kind": kind, "items": [{"id": i, "title": t, "path": p} for i, t, p in rows], **self.provenance()}

    def state(self) -> dict:
        return {"measurements": self.blob("state") or {}, **self.provenance()}

    def sessions(self) -> dict:
        return {"sessions": self.blob("sessions") or [], **self.provenance()}

    def provenance(self) -> dict:
        b = self.blob("build") or {}
        return {"snapshot": {"commit": b.get("commit", ""), "date": b.get("date", ""), "built": b.get("built", "")}}


def fts_query(text: str) -> str:
    """An FTS5 MATCH expression from free text: every content word quoted, OR-ed. Never raw syntax."""
    words = []
    for w in re.findall(r"\w+", text):
        if len(w) >= 3 and w.lower() not in STOP and w.lower() not in (x.lower() for x in words):
            words.append(w)
    return " OR ".join('"' + w.replace('"', "") + '"' for w in words[:16])


# ── selftest ───────────────────────────────────────────────────────────────────

def fixture(path: Path) -> dict:
    """A serving file of one document, three items and a one-page graph — what the self-tests read."""
    early = "Mich" "ael"
    body = f"# Titel\nJuna erscheint im Riss.\n\nAEGIS misst die Kohärenz.\nDie Kohärenz hält.\n{early} sagt etwas."
    docs = [{"slug": "doc-a", "title": "Doc A", "category": "x", "date": "2026-05-01", "offset": 5, "body": body, "read": True}]
    quotes = [{"page": "juna", "doc": "doc-a", "line": 6, "section": "Reading", "quote": "Juna erscheint im Riss"}]
    items = [{"kind": "page", "id": "juna", "path": "Wiki/candidates/juna.md", "title": "Juna", "markdown": "# Juna\nResonanz"},
             {"kind": "conflict", "id": "C2", "path": "Wiki/conflicts/c2-x.md", "title": "C2", "markdown": "# C2"},
             {"kind": "chapter", "id": "13", "path": "Wiki/chapters/kap-13.md", "title": "Kap 13", "markdown": "# Kap 13"}]
    graph = {"nodes": {"term:juna": {"id": "term:juna", "type": "term", "slug": "juna", "term": "Juna",
                                     "surfaces": ["Juna"], "conflict": "none"}},
             "edges": [], "evidence": {"juna": [{**quotes[0], "status": "verified", "ref": "doc-a.md:L6"}]}}
    return write(path, docs, quotes, items, {"graph": graph, "proposals": {"nodes": {}, "edges": [], "glosses": []},
                                             "build": {"commit": "abc1234"}})


def selftest() -> list[str]:
    """Each case carries the exact outcome it must produce; the fixture is built in a temp dir."""
    failures: list[str] = []

    def expect(name: str, ok: bool) -> None:
        if not ok:
            failures.append(name)

    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "serve.db"
        facts = fixture(path)
        expect("write: counts non-empty, served lines only (4 of 6)", facts["lines"] == 4)
        expect("write: an earlier name's line is withheld, not indexed", facts["lines_withheld"] == 1)
        s = Store(path)
        hit = s.search("Kohärenz", "sources")["hits"]
        expect("search: two lines, each with its file line (offset 5 → L8, L9)", sorted(h["line"] for h in hit) == [8, 9])
        expect("search: diacritics folded — Koharenz finds Kohärenz", len(s.search("Koharenz")["hits"]) == 2)
        expect("search: quotes scope returns the page", s.search("erscheint", "quotes")["hits"][0]["page"] == "juna")
        expect("search: items scope returns the page", s.search("Resonanz", "items")["hits"][0]["id"] == "juna")
        for bad, why in (("", "empty"), ("die der und", "stop words only"), ('"))) OR NEAR(', "FTS syntax")):
            try:
                r = s.search(bad)
                expect(f"search: {why} is refused or harmless", why == "FTS syntax" and isinstance(r["hits"], list))
            except Refused:
                pass
        try:
            s.search("Juna", "everything")
            expect("search: an unknown scope is refused", False)
        except Refused:
            pass
        w = s.read_lines("doc-a", 1, 100)
        expect("read_lines: clipped to the body (L5–L10)", (w["first"], w["last"]) == (5, 10))
        expect("read_lines: the withheld line reads [withheld]", w["lines"][-1]["text"] == WITHHELD_TEXT)
        expect("search: a withheld line is not found", not s.search("sagt etwas")["hits"])
        expect("read_lines: the text of L6", w["lines"][1]["text"] == "Juna erscheint im Riss.")
        v = s.verify_quote("doc-a", "Juna erscheint im Riss", 6)
        expect("verify: a true quotation holds on L6", v["holds"] is True and v["lines"] == [6])
        v = s.verify_quote("doc-a", "Juna erscheinen im Riss", 6)
        expect("verify: a wrong inflection fails and names the nearest line L6",
               v["holds"] is False and v["nearest"] and v["nearest"][0]["line"] == 6)
        expect("item: conflict id is case-insensitive", s.item("conflict", "c2")["id"] == "C2")
        expect("item: chapter accepts kap-13", s.item("chapter", "kap-13")["id"] == "13")
        try:
            s.item("page", "nobody")
            expect("item: a missing page is refused", False)
        except Refused:
            pass
        a = s.ask("Wo erscheint Juna?")
        expect("ask: the stored graph seeds juna and returns its verified quotation",
               a["graph"]["evidence"] and a["graph"]["evidence"][0]["doc"] == "doc-a")
        expect("ask: provenance names the snapshot's commit", a["snapshot"]["commit"] == "abc1234")
    try:
        Store(Path(tempfile.gettempdir()) / "no-such-serve.db")
        expect("store: a missing index is refused", False)
    except Refused:
        pass
    return failures


# ── command line ───────────────────────────────────────────────────────────────

def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__.split("    python3")[0].strip())
        return 2
    cmd, rest = argv[0], argv[1:]

    def option(name: str, default=None):
        return rest[rest.index(name) + 1] if name in rest else default

    if cmd == "selftest":
        failures = selftest()
        print(f"rag: {'held' if not failures else 'FAILED'} — "
              + ("every case holds" if not failures else "; ".join(failures)))
        return 1 if failures else 0
    if cmd == "build":
        facts = build(Path(option("--out", DEFAULT_DB)))
        print(json.dumps(facts))
        return 0
    s = Store()
    try:
        if cmd == "search":
            out = s.search(rest[0], option("--scope", "sources"), int(option("--limit", 10)))
        elif cmd == "ask":
            out = s.ask(rest[0])
        elif cmd == "lines":
            out = s.read_lines(rest[0], int(rest[1]), int(rest[2]))
        elif cmd == "verify":
            out = s.verify_quote(rest[0], rest[1], int(option("--line")) if option("--line") else None)
        elif cmd == "item":
            out = s.item(rest[0], rest[1])
        else:
            print(f"unknown command {cmd!r}")
            return 2
    except Refused as e:
        print(f"refused: {e}")
        return 1
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
