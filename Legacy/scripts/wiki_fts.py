#!/usr/bin/env python3
"""Local BM25 candidate finder over Wiki/, Canon/ and Sources/drive/ (SQLite FTS5).

    python3 scripts/wiki_fts.py build                         # incremental, by file sha256
    python3 scripts/wiki_fts.py search "Kohärenz Schleier" [--limit 10] [--scope wiki|canon|sources|all] [--json]
    python3 scripts/wiki_fts.py stats                         # files and chunks per scope, index age
    python3 scripts/wiki_fts.py doctor                        # FTS5 present, index vs disk; exit 1 on problems
    python3 scripts/wiki_fts.py --root <dir> build            # index another tree (tests)

Every markdown file is split into one chunk per heading (the heading line up
to the line before the next heading; the preamble before the first heading is
its own chunk). A chunk carries its path, the heading trail ("A > B > C") and
its 1-based start/end lines, so a hit prints as ``path:Lstart-Lend`` and can be
turned into a ``^[file:L-L]`` citation after reading those lines. The index
lives in ``.cache/wiki-fts/index.sqlite`` (git-ignored) and is rebuilt only for
files whose sha256 changed.

This is a **candidate finder only**: BM25 ranks chunks, it does not verify
them. The agent opens the page and reads the cited lines before citing. Only
the standard library is used; no LLM, no network.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import sys
from contextlib import closing
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB_RELATIVE = Path(".cache/wiki-fts/index.sqlite")
# scope → (directory, glob); order is the display order of stats.
SCOPES = {
    "wiki": ("Wiki", "**/*.md"),
    "canon": ("Canon", "*.md"),
    "sources": ("Sources/drive", "*.md"),
}
DEFAULT_LIMIT = 10
SNIPPET_TOKENS = 24
HEADING = re.compile(r"^(?P<level>#{1,6})\s+(?P<title>.+?)\s*#*\s*$")
FENCE = re.compile(r"^\s*(```|~~~)")
TOKEN = re.compile(r"[^\W_][\w-]*", re.UNICODE)
SCHEMA = """
CREATE TABLE IF NOT EXISTS files (
    path TEXT PRIMARY KEY, scope TEXT NOT NULL, sha256 TEXT NOT NULL, indexed_at TEXT NOT NULL);
CREATE TABLE IF NOT EXISTS chunks (
    id INTEGER PRIMARY KEY, path TEXT NOT NULL, scope TEXT NOT NULL, heading TEXT NOT NULL,
    start_line INTEGER NOT NULL, end_line INTEGER NOT NULL);
CREATE INDEX IF NOT EXISTS chunks_path ON chunks(path);
CREATE VIRTUAL TABLE IF NOT EXISTS chunks_fts USING fts5(
    heading, text, path UNINDEXED, scope UNINDEXED);
CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
"""


def db_path(root: Path) -> Path:
    return root / DB_RELATIVE


def fts5_available() -> bool:
    try:
        with closing(sqlite3.connect(":memory:")) as con:
            con.execute("CREATE VIRTUAL TABLE probe USING fts5(x)")
        return True
    except sqlite3.Error:
        return False


def connect(root: Path) -> sqlite3.Connection:
    path = db_path(root)
    path.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(path)
    con.executescript(SCHEMA)
    return con


def sha256_of(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def list_files(root: Path) -> list[tuple[str, str]]:
    """(relative posix path, scope) for every indexable file, sorted by path."""
    found: list[tuple[str, str]] = []
    for scope, (directory, pattern) in SCOPES.items():
        base = root / directory
        if not base.is_dir():
            continue
        for path in sorted(base.glob(pattern)):
            if path.is_file():
                found.append((path.relative_to(root).as_posix(), scope))
    return found


def chunk_lines(lines: list[str]) -> list[dict]:
    """Split markdown lines into heading chunks with 1-based line spans.

    Headings inside fenced code blocks do not start a chunk. Empty chunks
    (whitespace only) are dropped.
    """
    chunks: list[dict] = []
    trail: list[str] = []
    start = 1
    body: list[str] = []
    in_fence = False

    def flush() -> None:
        text = "\n".join(body)
        if text.strip():
            chunks.append({"heading": " > ".join(trail), "start_line": start,
                           "end_line": last_content_line(body, start), "text": text})

    for number, line in enumerate(lines, start=1):
        if FENCE.match(line):
            in_fence = not in_fence
        heading = None if in_fence else HEADING.match(line)
        if heading is None:
            body.append(line)
            continue
        flush()
        level = len(heading.group("level"))
        trail[:] = trail[: level - 1] + [heading.group("title")]
        start, body = number, [line]
    flush()
    return chunks


def last_content_line(body: list[str], start: int) -> int:
    """1-based number of the last non-blank line of a chunk starting at ``start``."""
    end = start + len(body) - 1
    while end > start and not body[end - start].strip():
        end -= 1
    return end


def index_file(con: sqlite3.Connection, root: Path, rel: str, scope: str, digest: str) -> int:
    """Replace the chunks of one file; returns the chunk count."""
    remove_file(con, rel)
    chunks = chunk_lines((root / rel).read_text(encoding="utf-8", errors="replace").splitlines())
    for chunk in chunks:
        cur = con.execute("INSERT INTO chunks(path, scope, heading, start_line, end_line) VALUES (?,?,?,?,?)",
                          (rel, scope, chunk["heading"], chunk["start_line"], chunk["end_line"]))
        con.execute("INSERT INTO chunks_fts(rowid, heading, text, path, scope) VALUES (?,?,?,?,?)",
                    (cur.lastrowid, chunk["heading"], chunk["text"], rel, scope))
    con.execute("INSERT OR REPLACE INTO files(path, scope, sha256, indexed_at) VALUES (?,?,?,?)",
                (rel, scope, digest, utc_now()))
    return len(chunks)


def remove_file(con: sqlite3.Connection, rel: str) -> None:
    con.execute("DELETE FROM chunks_fts WHERE rowid IN (SELECT id FROM chunks WHERE path = ?)", (rel,))
    con.execute("DELETE FROM chunks WHERE path = ?", (rel,))
    con.execute("DELETE FROM files WHERE path = ?", (rel,))


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def disk_state(root: Path) -> dict[str, tuple[str, str]]:
    """path → (scope, sha256) for every file on disk."""
    return {rel: (scope, sha256_of(root / rel)) for rel, scope in list_files(root)}


def index_state(con: sqlite3.Connection) -> dict[str, str]:
    """path → sha256 as recorded in the index."""
    return dict(con.execute("SELECT path, sha256 FROM files").fetchall())


def command_build(root: Path, _: argparse.Namespace) -> int:
    if not fts5_available():
        print("SQLite FTS5 is not available in this python build")
        return 1
    on_disk = disk_state(root)
    with closing(connect(root)) as con:
        indexed = index_state(con)
        removed = [rel for rel in indexed if rel not in on_disk]
        for rel in removed:
            remove_file(con, rel)
        changed = [rel for rel, (_, digest) in on_disk.items() if indexed.get(rel) != digest]
        chunk_count = sum(index_file(con, root, rel, on_disk[rel][0], on_disk[rel][1]) for rel in changed)
        con.execute("INSERT OR REPLACE INTO meta(key, value) VALUES ('built_at', ?)", (utc_now(),))
        con.commit()
    unchanged = len(on_disk) - len(changed)
    print(f"indexed {len(changed)} files ({chunk_count} chunks), {unchanged} unchanged, {len(removed)} removed"
          f" → {db_path(root).relative_to(root)}")
    return 0


def match_expression(query: str, operator: str) -> str:
    """Quote every token so user input never reaches the FTS5 parser raw."""
    tokens = TOKEN.findall(query)
    if not tokens:
        raise SystemExit("search query has no searchable token")
    return f" {operator} ".join('"' + token.replace('"', '""') + '"' for token in tokens)


def run_search(con: sqlite3.Connection, expression: str, scope: str, limit: int) -> list[dict]:
    where = "chunks_fts MATCH ?" + ("" if scope == "all" else " AND chunks_fts.scope = ?")
    params: list[object] = [expression] + ([] if scope == "all" else [scope])
    rows = con.execute(
        f"""SELECT chunks.path, chunks.scope, chunks.heading, chunks.start_line, chunks.end_line,
                   bm25(chunks_fts) AS score,
                   snippet(chunks_fts, 1, '[', ']', '…', {SNIPPET_TOKENS}) AS snippet
            FROM chunks_fts JOIN chunks ON chunks.id = chunks_fts.rowid
            WHERE {where} ORDER BY score LIMIT ?""", params + [limit]).fetchall()
    keys = ("path", "scope", "heading", "start_line", "end_line", "score", "snippet")
    return [dict(zip(keys, row)) for row in rows]


def search(root: Path, query: str, scope: str = "all", limit: int = DEFAULT_LIMIT) -> list[dict]:
    """All terms first; when nothing matches, any term (BM25 still ranks by overlap)."""
    with closing(connect(root)) as con:
        hits = run_search(con, match_expression(query, "AND"), scope, limit)
        if not hits:
            hits = run_search(con, match_expression(query, "OR"), scope, limit)
    for rank, hit in enumerate(hits, start=1):
        hit["rank"] = rank
        hit["snippet"] = re.sub(r"\s+", " ", hit["snippet"]).strip()
    return hits


def command_search(root: Path, args: argparse.Namespace) -> int:
    if not db_path(root).is_file():
        print("no index yet — run: python3 scripts/wiki_fts.py build")
        return 1
    hits = search(root, args.query, args.scope, args.limit)
    if args.json:
        print(json.dumps(hits, ensure_ascii=False, indent=2))
        return 0
    if not hits:
        print("no matches")
        return 0
    for hit in hits:
        print(f"{hit['rank']:>2}. {hit['path']}:L{hit['start_line']}-L{hit['end_line']}  (bm25 {hit['score']:.3f})")
        print(f"    {hit['heading'] or '(preamble)'}")
        print(f"    {hit['snippet']}")
    return 0


def scope_counts(con: sqlite3.Connection, table: str) -> dict[str, int]:
    counts = {scope: 0 for scope in SCOPES}
    counts.update(dict(con.execute(f"SELECT scope, COUNT(*) FROM {table} GROUP BY scope").fetchall()))
    return counts


def command_stats(root: Path, _: argparse.Namespace) -> int:
    if not db_path(root).is_file():
        print("index: missing — run: python3 scripts/wiki_fts.py build")
        return 0
    with closing(connect(root)) as con:
        files, chunks = scope_counts(con, "files"), scope_counts(con, "chunks")
        built_at = con.execute("SELECT value FROM meta WHERE key = 'built_at'").fetchone()
    print(f"index: {db_path(root).relative_to(root)}")
    for scope in SCOPES:
        print(f"{scope}: {files[scope]} files, {chunks[scope]} chunks")
    print(f"total: {sum(files.values())} files, {sum(chunks.values())} chunks")
    print(f"built: {built_at[0] if built_at else 'unknown'} ({index_age(built_at[0]) if built_at else 'n/a'})")
    return 0


def index_age(built_at: str) -> str:
    built = datetime.strptime(built_at, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    minutes = int((datetime.now(timezone.utc) - built).total_seconds() // 60)
    return f"{minutes} min ago" if minutes < 120 else f"{minutes // 60} h ago"


def doctor_report(root: Path) -> list[str]:
    """Problems found; empty means healthy. A missing index is reported, not a problem."""
    problems: list[str] = []
    if not fts5_available():
        return ["SQLite FTS5 is not available in this python build"]
    print("fts5: available")
    if not db_path(root).is_file():
        print("index: not built yet (python3 scripts/wiki_fts.py build)")
        return problems
    on_disk = disk_state(root)
    with closing(connect(root)) as con:
        indexed = index_state(con)
    stale = sorted(rel for rel, (_, digest) in on_disk.items() if rel in indexed and indexed[rel] != digest)
    unindexed = sorted(rel for rel in on_disk if rel not in indexed)
    vanished = sorted(rel for rel in indexed if rel not in on_disk)
    for label, paths in (("stale", stale), ("unindexed", unindexed), ("vanished", vanished)):
        problems.extend(f"{label}: {rel}" for rel in paths)
    print(f"index: {len(indexed)} files; disk: {len(on_disk)} files; "
          f"stale {len(stale)}, unindexed {len(unindexed)}, vanished {len(vanished)}")
    return problems


def command_doctor(root: Path, _: argparse.Namespace) -> int:
    problems = doctor_report(root)
    for line in problems:
        print(line)
    print("doctor: OK" if not problems else "doctor: PROBLEMS — run: python3 scripts/wiki_fts.py build")
    return 1 if problems else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root to index (default: this repo)")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("build", help="index new and changed files").set_defaults(func=command_build)
    find = commands.add_parser("search", help="BM25-ranked chunks for a query")
    find.add_argument("query")
    find.add_argument("--limit", type=int, default=DEFAULT_LIMIT)
    find.add_argument("--scope", choices=["all", *SCOPES], default="all")
    find.add_argument("--json", action="store_true")
    find.set_defaults(func=command_search)
    commands.add_parser("stats", help="files and chunks per scope").set_defaults(func=command_stats)
    commands.add_parser("doctor", help="index health; exit 1 on problems").set_defaults(func=command_doctor)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args.root.resolve(), args)


if __name__ == "__main__":
    sys.exit(main())
