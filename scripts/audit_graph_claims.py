#!/usr/bin/env python3
"""Audit NovelClaim provenance in Graph/ against D-W2 (read-only).

    python3 scripts/audit_graph_claims.py              # table of counts + violating ids
    python3 scripts/audit_graph_claims.py --json       # machine-readable report
    python3 scripts/audit_graph_claims.py --root PATH  # another repository root (tests)

D-W2: the provenance graph carries claims only with a ``source_uri`` under
``Sources/`` or ``Canon/`` — never ``Wiki/`` and never a page body. Every
record in ``Graph/nodes/novel_claim.jsonl`` is classified by its
``source_uri``:

    canon    starts with Canon/
    sources  starts with Sources/
    wiki     starts with Wiki/           <- D-W2 violation
    other    any other non-empty value
    empty    no source_uri property, or an empty string

Exit 0 when no ``wiki`` claim exists, 1 when at least one does, 2 when the
audit cannot run (no Graph/ directory, or a malformed record). Nothing is
ever written. Only the standard library is used.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools import kpgraph  # noqa: E402  (needs ROOT on the path)

CLAIM_LABEL = "NovelClaim"
URI_PROPERTY = "source_uri"
# Classification order matters only for readability; prefixes are disjoint.
PREFIXES = (("canon", "Canon/"), ("sources", "Sources/"), ("wiki", "Wiki/"))
CLASSES = ("canon", "sources", "wiki", "other", "empty")
VIOLATION_CLASS = "wiki"
EXIT_OK, EXIT_VIOLATION, EXIT_CANNOT_RUN = 0, 1, 2


class AuditError(Exception):
    """The audit cannot run; the message says why."""


def classify(uri: str) -> str:
    if not uri:
        return "empty"
    for name, prefix in PREFIXES:
        if uri.startswith(prefix):
            return name
    return "other"


def claim_uris(root: Path) -> list[tuple[int, str]]:
    """``(node id, source_uri or '')`` for every NovelClaim record."""
    graph_dir = root / "Graph"
    if not graph_dir.is_dir():
        raise AuditError(f"no graph at {graph_dir}")
    try:
        graph = kpgraph.load(root)
    except ValueError as exc:
        raise AuditError(str(exc)) from exc
    claims = graph.nodes(CLAIM_LABEL)
    if not claims and not (graph_dir / "nodes" / "novel_claim.jsonl").is_file():
        raise AuditError(f"missing {graph_dir / 'nodes' / 'novel_claim.jsonl'}")
    return sorted((int(c["_nid"]), str(c.get(URI_PROPERTY, ""))) for c in claims)


def audit(root: Path) -> dict:
    """Counts per class plus the ids (and uris) of the violating and unclassified claims."""
    claims = claim_uris(root)
    counts = {name: 0 for name in CLASSES}
    flagged: dict[str, list[dict]] = {VIOLATION_CLASS: [], "other": [], "empty": []}
    for node_id, uri in claims:
        kind = classify(uri)
        counts[kind] += 1
        if kind in flagged:
            flagged[kind].append({"id": node_id, "source_uri": uri})
    return {"graph": (root / "Graph").as_posix(), "claims": len(claims), "counts": counts,
            "violations": flagged[VIOLATION_CLASS], "other": flagged["other"], "empty": flagged["empty"]}


def render(report: dict) -> str:
    lines = [f"NovelClaim records in {report['graph']}: {report['claims']}", "",
             "class     count", "-----     -----"]
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
    parser.add_argument("--root", type=Path, default=ROOT, help="repository root holding Graph/ (default: this repo)")
    parser.add_argument("--json", action="store_true", help="print the report as JSON")
    args = parser.parse_args(argv)
    try:
        report = audit(args.root)
    except AuditError as exc:
        print(f"audit cannot run: {exc}", file=sys.stderr)
        return EXIT_CANNOT_RUN
    print(json.dumps(report, ensure_ascii=False, indent=2) if args.json else render(report))
    return EXIT_VIOLATION if report["violations"] else EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
