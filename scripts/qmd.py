"""Talk to qmd from Python, and hand what it finds to the tools that answer.

qmd is a search engine: it returns ranked places to look. Everything in this
repository that produces a number — `corpus.py`, `duplicates.py`, `quotes.py` —
says what it counted and how. **Those are different kinds of answer and must not
be confused**, so this module is deliberately shaped to make the handoff explicit
rather than convenient to skip:

    for hit in search("kategoriale Unfähigkeit", collection="corpus"):
        doc = hit.document()          # the Document from subject.py, or None
        if doc:
            facts(doc.slug, "structure")   # now it is a measurement again

A `Hit` carries where to look. It carries no claim about the corpus.

## Why this exists as a module and not a shell call

A shell call returns text that each caller re-parses, which is how the
frontmatter boundary ended up with four implementations. `--json` is parsed here,
once, and `qmd://collection/relative/path` is resolved to a real `Path` here,
once — because that resolution is the only thing standing between a search result
and the rest of the toolchain.

## Collections

Named by **purpose**, not by folder, and `all` covers everything so a question
that could be answered by any layer has somewhere to go. `all` is excluded from
default queries because it overlaps the others; ask for it by name.

    search(q)                    # the default collections
    search(q, collection="all")  # everything, including the working agreement

Usage from the shell is still fine and unchanged; this is for code.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BIN = ROOT / ".tools-node" / "node_modules" / ".bin" / "qmd"
REF = re.compile(r"^qmd://(?P<collection>[^/]+)/(?P<path>.*)$")

sys.path.insert(0, str(ROOT / "scripts"))


class NotInstalled(RuntimeError):
    pass


def _run(args: list[str], parse_json: bool = False):
    if not BIN.exists():
        raise NotInstalled(
            "qmd is not installed. Run:\n"
            "  npm install --prefix .tools-node @tobilu/qmd\n"
            "  .tools-node/node_modules/.bin/qmd init")
    done = subprocess.run([str(BIN), *args], capture_output=True, text=True, cwd=ROOT)
    if done.returncode != 0 and not done.stdout:
        raise RuntimeError(f"qmd {' '.join(args)} failed: {done.stderr[:300]}")
    if not parse_json:
        return done.stdout
    try:
        return json.loads(done.stdout)
    except json.JSONDecodeError:
        return []


@lru_cache(maxsize=1)
def _paths() -> dict[str, Path]:
    """collection name -> the directory it indexes. `collection show` is the only source."""
    names = [line.split(" (qmd://")[0].strip()
             for line in _run(["collection", "list"]).splitlines() if " (qmd://" in line]
    found = {}
    for name in names:
        for line in _run(["collection", "show", name]).splitlines():
            if line.strip().startswith("Path:"):
                found[name] = Path(line.split("Path:", 1)[1].strip())
                break
    return found


@dataclass(frozen=True)
class Hit:
    """One place to look. Not an answer about the corpus."""

    collection: str
    path: Path          # resolved on disk, so the rest of the toolchain can take it
    line: int
    score: float
    title: str
    snippet: str
    docid: str

    @property
    def slug(self) -> str:
        return self.path.stem

    def document(self):
        """The `subject.Document` when this hit is a landed source, else None.

        This is the handoff. A hit says where; a Document is what every
        measurement in this repository is built on.
        """
        from subject import document, documents
        if any(d.slug == self.slug for d in documents()):
            return document(self.slug)
        return None

    def __str__(self) -> str:
        where = self.path.relative_to(ROOT) if self.path.is_relative_to(ROOT) else self.path
        return f"{self.score:.2f}  {where}:{self.line}"


def _resolve(ref: str) -> tuple[str, Path] | None:
    match = REF.match(ref)
    if not match:
        return None
    collection = match.group("collection")
    root = _paths().get(collection)
    return (collection, root / match.group("path")) if root else None


def _hits(rows: list[dict]) -> list[Hit]:
    out = []
    for row in rows:
        resolved = _resolve(row.get("file", ""))
        if not resolved:
            continue
        collection, path = resolved
        out.append(Hit(collection=collection, path=path, line=int(row.get("line") or 0),
                       score=float(row.get("score") or 0.0), title=row.get("title") or "",
                       snippet=row.get("snippet") or "", docid=row.get("docid") or ""))
    return out


def search(query: str, collection: str | None = None, n: int = 10) -> list[Hit]:
    """BM25 keyword search. No model, no network, about 0.2s."""
    args = ["search", query, "-n", str(n), "--json"]
    if collection:
        args += ["-c", collection]
    return _hits(_run(args, parse_json=True))


def vsearch(query: str, collection: str | None = None, n: int = 10) -> list[Hit]:
    """Vector similarity. Needs `qmd embed` to have run; empty until it has."""
    args = ["vsearch", query, "-n", str(n), "--json"]
    if collection:
        args += ["-c", collection]
    return _hits(_run(args, parse_json=True))


def get(ref: str | Path | Hit, start: int | None = None, count: int | None = None) -> str:
    """A document's text, line-numbered, by qmd ref, path or Hit."""
    if isinstance(ref, Hit):
        ref = ref.path
    if isinstance(ref, Path):
        rel = ref.relative_to(ROOT) if ref.is_relative_to(ROOT) else ref
        for name, root in _paths().items():
            if ref.is_relative_to(root):
                rel = ref.relative_to(root)
                ref = f"qmd://{name}/{rel}"
                break
        else:
            ref = str(rel)
    target = str(ref) + (f":{start}" + (f":{count}" if count else "") if start else "")
    return _run(["get", target])


def update() -> str:
    """Re-index every collection. Cheap; unchanged files are skipped."""
    return _run(["update"])


def collections() -> dict[str, Path]:
    return dict(_paths())


def main(argv: list[str]) -> int:
    if not argv:
        for name, path in sorted(collections().items()):
            where = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
            print(f"  {name:12} {where}")
        print("\n  python3 scripts/qmd.py <query> [collection]")
        return 0
    for hit in search(argv[0], collection=argv[1] if len(argv) > 1 else None, n=8):
        doc = hit.document()
        print(f"{hit}   {'source: ' + doc.category if doc else hit.collection}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
