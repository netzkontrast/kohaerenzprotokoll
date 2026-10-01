"""The one place novelgraph touches the repository's own scripts.

Every helper is imported, never copied (P6): the manifest and the frontmatter
boundary from `scripts/subject.py`, `fold()` from `scripts/wiki_index.py`, the
bench cases from `scripts/ask.py`. The scripts are being consolidated; when one of
these moves, this file is the only one that follows it.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SCRIPTS = ROOT / "scripts"
INDEX = ROOT / "Index"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import subject  # noqa: E402
from wiki_index import fold  # noqa: E402

read_jsonl = subject.read_jsonl
write_jsonl = subject.write_jsonl


def documents():
    """Every landed document of the manifest (`Sources/ask/` answers excluded, decision 017)."""
    return subject.documents()


def manifest_rows() -> list[dict]:
    return subject.rows()


def bench_cases() -> list[dict]:
    """The 24 cases of `ask.py bench`: the record's question, gold = the (slug, file line) it cites."""
    import ask
    return ask.bench_cases()


__all__ = ["ROOT", "INDEX", "documents", "manifest_rows", "bench_cases", "fold", "read_jsonl", "write_jsonl"]
