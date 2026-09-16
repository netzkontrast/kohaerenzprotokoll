#!/usr/bin/env python3
"""Export the provenance graph from SQLite into plain, diffable files.

The graph used to live in `.agency/session.db`, a property-graph schema owned
by an engine plugin. The novel facts in it — codex entries, world axioms,
chapters, claims — are the author's, and they outlive any tool that wrote
them. This script lifts them out into `Graph/`, one JSONL file per node
label plus one edge file, so every fact is greppable, diffable and readable
without a database.

    python3 scripts/export_graph.py                  # write Graph/
    python3 scripts/export_graph.py --check          # exit 1 if Graph/ is stale
    python3 scripts/export_graph.py --db path.db     # read a different snapshot

Two kinds of node live in the source database and only one is exported.
CONTENT labels are the novel: they carry facts a reader of the book could in
principle check. ENGINE labels (Invocation, Event, Intent, Phase, Gate,
Reflection, Artefact, Skill, Agent) are the plugin's own audit trail of which
tool call produced which write — meaningless once the plugin is gone, and
2,800 of the 3,953 nodes. They are dropped, and so are the SERVES and
PERFORMED_BY edges that only connect them.

Node identity is preserved: `_nid` is the integer the edge records point at,
so an exported edge resolves exactly as it did in SQL. `vto` is dropped
because every live node carries the same open value; `vfrom` is kept because
it records when the fact entered the graph.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DB = ROOT / ".agency" / "session.db"
OUT = ROOT / "Graph"
OPEN_VTO = 1_000_000_000_000

# The novel's own labels, in the order a reader would meet them.
CONTENT_LABELS = [
    "Novel", "Storyform", "Chapter", "Scene", "NarrativeBeat",
    "World", "WorldAxiom", "CodexEntry", "StoryTimeEvent",
    "NovelClaim", "DecisionRecord",
]

# Edges between content nodes. SERVES and PERFORMED_BY are engine bookkeeping.
CONTENT_EDGES = [
    "CODEX_OF", "PART_OF_WORLD", "CHAPTER_OF",
    "SCENE_OF", "PRECEDES", "HAPPENS_AT", "REVEALED_IN",
]

PROP_TABLES = (("node_props_text", str), ("node_props_int", int), ("node_props_bool", bool))


def file_name(label: str) -> str:
    """``CodexEntry`` -> ``codex_entry.jsonl``."""
    snake = "".join(f"_{ch.lower()}" if ch.isupper() else ch for ch in label).lstrip("_")
    return f"{snake}.jsonl"


def read_nodes(conn: sqlite3.Connection, label: str) -> list[dict]:
    """Every live node of ``label``, its properties merged into one record."""
    keys = {r[0]: r[1] for r in conn.execute("SELECT id, key FROM property_keys")}
    ids = [r[0] for r in conn.execute("SELECT node_id FROM node_labels WHERE label=?", (label,))]
    props: dict[int, dict] = {nid: {"_nid": nid} for nid in ids}
    for table, cast in PROP_TABLES:
        for nid, kid, value in conn.execute(f"SELECT node_id, key_id, value FROM {table}"):
            if nid in props:
                props[nid][keys[kid]] = cast(value)
    live = [p for p in props.values() if p.pop("vto", OPEN_VTO) == OPEN_VTO]
    return sorted(live, key=lambda p: p["_nid"])


def read_edges(conn: sqlite3.Connection, kept: set[int]) -> list[dict]:
    """Content edges whose both ends survived the export."""
    rows = conn.execute("SELECT source_id, target_id, type FROM edges WHERE type IN "
                        f"({','.join('?' * len(CONTENT_EDGES))})", CONTENT_EDGES)
    edges = [{"type": t, "source": s, "target": d} for s, d, t in rows if s in kept and d in kept]
    return sorted(edges, key=lambda e: (e["type"], e["source"], e["target"]))


def as_jsonl(records: list[dict]) -> str:
    return "".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n" for r in records)


def render(db: Path) -> dict[str, str]:
    """Every file the export produces, as ``relative path -> text``."""
    conn = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    by_label = {label: read_nodes(conn, label) for label in CONTENT_LABELS}
    kept = {n["_nid"] for nodes in by_label.values() for n in nodes}
    files = {f"nodes/{file_name(label)}": as_jsonl(nodes) for label, nodes in by_label.items()}
    files["edges.jsonl"] = as_jsonl(read_edges(conn, kept))
    conn.close()
    return files


def write(files: dict[str, str]) -> list[str]:
    written = []
    for rel, text in sorted(files.items()):
        target = OUT / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")
        written.append(f"Graph/{rel}")
    return written


def stale(files: dict[str, str]) -> list[str]:
    out = []
    for rel, text in sorted(files.items()):
        target = OUT / rel
        if not target.is_file():
            out.append(f"Graph/{rel}: missing")
        elif target.read_text(encoding="utf-8") != text:
            out.append(f"Graph/{rel}: stale")
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--db", type=Path, default=DEFAULT_DB)
    ap.add_argument("--check", action="store_true", help="exit 1 if the files differ from the database")
    ns = ap.parse_args(argv)
    if not ns.db.is_file():
        print(f"no database at {ns.db}; Graph/ is the source of truth now", file=sys.stderr)
        return 2
    files = render(ns.db)
    if ns.check:
        problems = stale(files)
        for p in problems:
            print(p)
        print("Graph/ up to date" if not problems else f"{len(problems)} file(s) differ")
        return 1 if problems else 0
    for rel in write(files):
        print(f"wrote {rel}")
    counts = {rel: text.count("\n") for rel, text in sorted(files.items())}
    print("\n" + "  ".join(f"{rel.split('/')[-1]}={n}" for rel, n in counts.items()))
    return 0


if __name__ == "__main__":
    sys.exit(main())
