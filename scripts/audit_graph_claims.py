#!/usr/bin/env python3
"""Audit NovelClaim provenance in the agency graph against D-W2 (read-only).

    python3 scripts/audit_graph_claims.py              # table of counts + violating ids
    python3 scripts/audit_graph_claims.py --json       # machine-readable report
    python3 scripts/audit_graph_claims.py --db PATH    # another sqlite file (tests)

D-W2: the provenance graph ``.agency/session.db`` carries claims only with a
``source_uri`` under ``Sources/`` or ``Canon/`` — never ``Wiki/`` and never a
page body. Every node labelled ``NovelClaim`` is classified by its
``source_uri`` property:

    canon    starts with Canon/
    sources  starts with Sources/
    wiki     starts with Wiki/           <- D-W2 violation
    other    any other non-empty value
    empty    no source_uri property, or an empty string

Exit 0 when no ``wiki`` claim exists, 1 when at least one does, 2 when the
audit cannot run (database or tables missing, no ``source_uri`` property key).
The database is opened with ``mode=ro``; nothing is ever written. Only the
standard library is used.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from contextlib import closing
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_DB = ROOT / ".agency" / "session.db"
CLAIM_LABEL = "NovelClaim"
URI_PROPERTY = "source_uri"
REQUIRED_TABLES = ("nodes", "node_labels", "node_props_text", "property_keys")
# Classification order matters only for readability; prefixes are disjoint.
PREFIXES = (("canon", "Canon/"), ("sources", "Sources/"), ("wiki", "Wiki/"))
CLASSES = ("canon", "sources", "wiki", "other", "empty")
VIOLATION_CLASS = "wiki"
EXIT_OK, EXIT_VIOLATION, EXIT_CANNOT_RUN = 0, 1, 2


class AuditError(Exception):
    """The audit cannot run; the message says why."""


def connect_readonly(db: Path) -> sqlite3.Connection:
    if not db.is_file():
        raise AuditError(f"no database at {db}")
    return sqlite3.connect(f"file:{db.as_posix()}?mode=ro", uri=True)


def check_tables(con: sqlite3.Connection) -> None:
    present = {row[0] for row in con.execute("SELECT name FROM sqlite_master WHERE type = 'table'")}
    missing = [name for name in REQUIRED_TABLES if name not in present]
    if missing:
        raise AuditError(f"missing tables: {', '.join(missing)}")


def key_column(con: sqlite3.Connection) -> str:
    """The text column of ``property_keys`` that holds the key name (``name`` or ``key``)."""
    columns = [row[1] for row in con.execute("PRAGMA table_info(property_keys)")]
    for candidate in ("name", "key"):
        if candidate in columns:
            return candidate
    raise AuditError(f"property_keys has no name column; columns: {columns}")


def uri_key_id(con: sqlite3.Connection) -> int:
    column = key_column(con)
    row = con.execute(f"SELECT id FROM property_keys WHERE {column} = ?", (URI_PROPERTY,)).fetchone()
    if row is not None:
        return int(row[0])
    similar = [r[0] for r in con.execute(
        f"SELECT {column} FROM property_keys WHERE {column} LIKE '%source%' OR {column} LIKE '%uri%'")]
    raise AuditError(f"no property key {URI_PROPERTY!r} in property_keys; similar keys: {similar or 'none'}")


def classify(uri: str) -> str:
    if not uri:
        return "empty"
    for name, prefix in PREFIXES:
        if uri.startswith(prefix):
            return name
    return "other"


def claim_uris(con: sqlite3.Connection, key_id: int) -> list[tuple[int, str]]:
    """(node id, source_uri or '') for every NovelClaim node."""
    rows = con.execute(
        """SELECT labels.node_id, COALESCE(props.value, '')
           FROM node_labels AS labels
           LEFT JOIN node_props_text AS props
             ON props.node_id = labels.node_id AND props.key_id = ?
           WHERE labels.label = ?
           ORDER BY labels.node_id""", (key_id, CLAIM_LABEL)).fetchall()
    return [(int(node_id), uri) for node_id, uri in rows]


def audit(db: Path) -> dict:
    """Counts per class plus the ids (and uris) of the violating and unclassified claims."""
    with closing(connect_readonly(db)) as con:
        check_tables(con)
        claims = claim_uris(con, uri_key_id(con))
    counts = {name: 0 for name in CLASSES}
    flagged: dict[str, list[dict]] = {VIOLATION_CLASS: [], "other": [], "empty": []}
    for node_id, uri in claims:
        kind = classify(uri)
        counts[kind] += 1
        if kind in flagged:
            flagged[kind].append({"id": node_id, "source_uri": uri})
    return {"db": db.as_posix(), "claims": len(claims), "counts": counts,
            "violations": flagged[VIOLATION_CLASS], "other": flagged["other"], "empty": flagged["empty"]}


def render(report: dict) -> str:
    lines = [f"NovelClaim nodes in {report['db']}: {report['claims']}", "", "class     count", "-----     -----"]
    lines += [f"{name:<9} {report['counts'][name]:>5}" for name in CLASSES]
    lines.append("")
    if report["violations"]:
        lines.append(f"D-W2 violations ({len(report['violations'])} claim(s) with source_uri under Wiki/):")
        lines += [f"  node {item['id']}: {item['source_uri']}" for item in report["violations"]]
    else:
        lines.append("D-W2: no claim points into Wiki/")
    for name in ("other", "empty"):
        if report[name]:
            lines.append(f"{name} ({len(report[name])}): " + ", ".join(str(item["id"]) for item in report[name]))
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--db", type=Path, default=DEFAULT_DB, help="sqlite file (default: .agency/session.db)")
    parser.add_argument("--json", action="store_true", help="print the report as JSON")
    args = parser.parse_args(argv)
    try:
        report = audit(args.db)
    except (AuditError, sqlite3.Error) as exc:
        print(f"audit cannot run: {exc}", file=sys.stderr)
        return EXIT_CANNOT_RUN
    print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else render(report))
    return EXIT_VIOLATION if report["violations"] else EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
