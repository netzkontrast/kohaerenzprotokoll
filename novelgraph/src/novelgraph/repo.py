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
def write_jsonl(path, rows):
    from .store import atomic_text
    import json
    atomic_text(path, "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))


def documents():
    """Every landed document of the manifest (`Sources/ask/` answers excluded, decision 017)."""
    return subject.documents()


def refresh_documents():
    subject.documents.cache_clear()


def catalogue_stat():
    st = subject.MANIFEST.stat()
    return st.st_mtime_ns, st.st_size, st.st_ino


def manifest_rows() -> list[dict]:
    return subject.rows()


def bench_cases(live: bool = False) -> list[dict]:
    """The 24 cases of `ask.py bench`, frozen (`Plan/eval/retrieval-cases-v1.json`, `benchset.cases`): the record's
    question, gold = the (slug, file line) it cites. `live` reads the records, whose gold moves with every edit."""
    import benchset
    return benchset.cases(live=live)


def bench_identity(live: bool = False) -> dict:
    """`case_set` and `cases_sha256` of the cases a bench scored, for its saved result (`benchset.identity`)."""
    import benchset
    return benchset.identity(live)


__all__ = ["ROOT", "INDEX", "documents", "manifest_rows", "bench_cases", "bench_identity", "fold", "read_jsonl", "write_jsonl"]
