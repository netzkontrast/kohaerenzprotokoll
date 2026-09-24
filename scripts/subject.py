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
from functools import cached_property, lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "Sources" / "manifest.jsonl"
DUPLICATES = ROOT / "Sources" / "duplicates.jsonl"
DERIVED = ROOT / "Plan" / "derived"
PAGES = ROOT / "Wiki" / "candidates"
CONFLICTS = ROOT / "Wiki" / "conflicts"
QUESTIONS = ROOT / "Wiki" / "questions"
JUDGEMENTS = ROOT / "Plan" / "runs" / "judgements.jsonl"


@dataclass(frozen=True)
class Document:
    """One landed source document, with its body and the line its body starts on.

    `offset` is the **file** line of the first body line, so a citation written
    from it resolves against the file as it sits on disk -- frontmatter included,
    which is the convention `Sources/README.md` fixes. some landed
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

    def lines(self) -> tuple[str, ...]:
        """The body's lines, split once per document; index `n - offset` is file line n."""
        return self._lines

    @cached_property
    def _lines(self) -> tuple[str, ...]:
        # A tuple, because every caller shares it. Splitting per call cost
        # quotes.py one split per cited line and bilingual.py one per example.
        return tuple(self.body.split("\n"))


def _split(text: str) -> tuple[str, int]:
    """Return (body, offset). The only implementation of this in the repository."""
    lines = text.split("\n")
    marks = [i for i, line in enumerate(lines) if line.strip() == "---"]
    start = marks[1] + 1 if len(marks) >= 2 and marks[0] == 0 else 0
    return "\n".join(lines[start:]), start + 1


def read_jsonl(path: Path) -> list[dict]:
    """Every object in a JSONL file, in file order, blank lines skipped.

    A missing file raises: whether absence means „none yet" or „something is
    wrong" is the caller's to say, and the manifest's absence is the second.
    """
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines()
            if line.strip()]


def write_jsonl(path: Path, rows) -> None:
    """One compact object per line, non-ASCII kept as written — every JSONL file here."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows),
                    encoding="utf-8")


def rows() -> list[dict]:
    """Every manifest row, in file order."""
    return read_jsonl(MANIFEST)


def duplicates() -> list[dict]:
    """Every row folded out of the manifest by scripts/dedupe.py; [] before the first."""
    return read_jsonl(DUPLICATES) if DUPLICATES.exists() else []


@lru_cache(maxsize=1)
def documents() -> tuple[Document, ...]:
    """Every landed document. Cached: the corpus does not change within a run."""
    out = []
    for row in rows():
        if not row.get("export_path"):
            continue
        path = ROOT / row["export_path"]
        if not path.exists():
            raise FileNotFoundError(
                f"{row['slug']} is landed and not a duplicate, but {path} is gone. "
                "A missing file used to be skipped here, which made the corpus "
                "quietly smaller and every count quietly wrong.")
        body, offset = _split(path.read_text(encoding="utf-8"))
        out.append(Document(
            slug=row["slug"], category=row.get("category", "?"),
            date=row.get("index_date") or "?", format=row.get("format", "?"),
            sha256=row.get("sha256", ""), path=path, body=body, offset=offset,
        ))
    return tuple(out)


@lru_cache(maxsize=1)
def _by_slug() -> dict[str, Document]:
    by: dict[str, Document] = {}
    for doc in documents():
        by.setdefault(doc.slug, doc)
    return by


def document(slug: str) -> Document:
    try:
        return _by_slug()[slug]
    except KeyError:
        raise KeyError(f"no landed document with slug {slug!r}") from None


def derived(slug: str) -> dict:
    """The rule cache for one document, or {} if scripts/derive.py has not run."""
    path = DERIVED / f"{slug}.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}


def facts(slug: str, rule: str) -> dict:
    """One rule's derived facts for one document, or {}."""
    return derived(slug).get(rule, {}).get("facts", {})


def judgements() -> list[dict]:
    """The judgement ledger, in file order; [] before the first judgement."""
    return read_jsonl(JUDGEMENTS) if JUDGEMENTS.exists() else []


def cli(main) -> None:
    """Run a script's `main(argv)` and exit with the status it returns.

    `sources.py status | head` closes the pipe early, which otherwise ends in a
    BrokenPipeError traceback over perfectly good output. Restoring the default
    SIGPIPE makes the process exit the way every other command-line tool does.
    """
    import sys
    try:
        import signal
        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass                                    # not POSIX, or not the main thread
    raise SystemExit(main(sys.argv[1:]))
