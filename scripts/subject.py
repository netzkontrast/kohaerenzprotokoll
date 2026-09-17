"""The one place the corpus becomes addressable. Every other script asks here.

Four scripts had their own copy of "find where the frontmatter ends". That is not
a tidiness problem: the boundary is the difference between a citation resolving
and resolving to the wrong text, and of the four copies one had an off-by-nine
bug that reported body-relative line numbers as file lines, and another carried a
docstring claiming behaviour it did not have.

One implementation, found per document and never assumed, is the fix.

## What a subject is

Everything this project works on is a **subject** with an **account**: a document,
a term, a pair of surfaces, the corpus itself. The steps that grew one at a time
-- census, note, reconcile, gather, corpus query, judgement -- are the same
operation applied to different subjects at different scales, and each decomposes
into the same operation on smaller ones.

This module holds the substrate they share. `scripts/account.py` is the verb.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "Sources" / "manifest.jsonl"
DERIVED = ROOT / "Plan" / "derived"
PAGES = ROOT / "Wiki" / "candidates"
CONFLICTS = ROOT / "Wiki" / "conflicts"
JUDGEMENTS = ROOT / "Plan" / "runs" / "judgements.jsonl"


@dataclass(frozen=True)
class Document:
    """One landed source document, with its body and the line its body starts on.

    `offset` is the **file** line of the first body line, so a citation written
    from it resolves against the file as it sits on disk -- frontmatter included,
    which is the convention `Sources/README.md` fixes. 26 of the 409 landed
    documents have no frontmatter at all, so the value is found, never assumed.
    """

    slug: str
    category: str
    date: str
    format: str
    sha256: str
    path: Path
    body: str
    offset: int

    @property
    def has_frontmatter(self) -> bool:
        return self.offset > 1

    def lines(self) -> list[str]:
        return self.body.split("\n")


def _split(text: str) -> tuple[str, int]:
    """Return (body, offset). The only implementation of this in the repository."""
    lines = text.split("\n")
    marks = [i for i, line in enumerate(lines) if line.strip() == "---"]
    start = marks[1] + 1 if len(marks) >= 2 and marks[0] == 0 else 0
    return "\n".join(lines[start:]), start + 1


def rows() -> list[dict]:
    """Every manifest row, in file order."""
    return [json.loads(line) for line in MANIFEST.read_text(encoding="utf-8").splitlines()]


@lru_cache(maxsize=1)
def documents() -> tuple[Document, ...]:
    """Every landed document. Cached: the corpus does not change within a run."""
    out = []
    for row in rows():
        if not row.get("export_path"):
            continue
        path = ROOT / row["export_path"]
        if not path.exists():
            continue
        body, offset = _split(path.read_text(encoding="utf-8"))
        out.append(Document(
            slug=row["slug"], category=row.get("category", "?"),
            date=row.get("index_date") or "?", format=row.get("format", "?"),
            sha256=row.get("sha256", ""), path=path, body=body, offset=offset,
        ))
    return tuple(out)


def document(slug: str) -> Document:
    for doc in documents():
        if doc.slug == slug:
            return doc
    raise KeyError(f"no landed document with slug {slug!r}")


def derived(slug: str) -> dict:
    """The rule cache for one document, or {} if scripts/derive.py has not run."""
    path = DERIVED / f"{slug}.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def facts(slug: str, rule: str) -> dict:
    """One rule's derived facts for one document, or {}."""
    return derived(slug).get(rule, {}).get("facts", {})


def judgements() -> list[dict]:
    if not JUDGEMENTS.exists():
        return []
    return [json.loads(l) for l in JUDGEMENTS.read_text(encoding="utf-8").splitlines() if l.strip()]
