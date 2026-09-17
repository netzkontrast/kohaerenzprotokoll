"""Hand the reader the document the way a citation will be checked.

Reading is the one step that produces a claim about a source, and the claim is
a quotation with a line: „…" ^[L272]. `scripts/quotes.py` verifies those
afterwards, and its first run found three that were right about the line and the
meaning and **wrong about the words** — „das Management" written for „dem
Management". Checking after the fact names the defect; it does not stop it being
written.

So this script serves the same text in both directions:

    view    the document with every line prefixed `NNN| `, the file line a
            citation names — so a quote is copied from its number, not typed
            next to one
    find    the reverse: give it the words you want to quote and it answers with
            the citation, or refuses. A quote that `--find` produced resolves in
            `quotes.py` by construction, because both ask the same question of
            the same normalised line.

A refusal is the useful half. `--find` prints the nearest lines when nothing
resolves, which is what turns „das Management" into „it is L61 and the word
there is dem".

Usage:
    python3 scripts/read.py <slug>                    # the whole document
    python3 scripts/read.py <slug> --from 120 --to 180
    python3 scripts/read.py <slug> --find "dem Management"
"""

from __future__ import annotations

import sys
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import quotes  # noqa: E402
from subject import Document, document  # noqa: E402

NEAREST = 3
PREVIEW = 110


def numbered(doc: Document, first: int, last: int) -> list[str]:
    """The document's lines, each prefixed with the file line a citation names."""
    width = len(str(doc.offset + len(doc.lines()) - 1))
    out = []
    for index, line in enumerate(doc.lines()):
        number = doc.offset + index
        if first <= number <= last:
            out.append(f"{number:>{width}}| {line}")
    return out


def locate(doc: Document, quote: str) -> list[int]:
    """Every file line the quote resolves against, by quotes.py's own comparison."""
    parts = quotes.parts_of(quote)
    if not parts:
        return []
    return [doc.offset + index
            for index, line in enumerate(doc.lines())
            if quotes.missing_part(quotes.normalise(line), parts) is None]


def spans(doc: Document, quote: str) -> list[tuple[int, int]]:
    """Pairs of consecutive lines the quote crosses.

    A quote that spans two lines is unresolvable — the line number is part of the
    claim, and `quotes.py` reports it rather than searching nearby. Saying so here
    turns that into an instruction: cite one line, or quote a fragment.
    """
    parts = quotes.parts_of(quote)
    lines = [quotes.normalise(line) for line in doc.lines()]
    found = []
    for index in range(len(lines) - 1):
        joined = f"{lines[index]} {lines[index + 1]}".strip()
        if parts and quotes.missing_part(joined, parts) is None:
            found.append((doc.offset + index, doc.offset + index + 1))
    return found


def nearest(doc: Document, quote: str) -> list[tuple[float, int, str]]:
    """The lines whose longest passage in common with the quote is longest.

    Shared *words* are the wrong measure here: the quote that fails is almost the
    line, off by one inflection, and a bag of words ranks it level with every
    other line that happens to mention the same nouns. The longest run of
    characters in common puts the line the reader meant on top, which is the
    whole point of answering a refusal.
    """
    wanted = quotes.normalise(quote)
    if not wanted:
        return []
    scored = []
    for index, line in enumerate(doc.lines()):
        clean = quotes.normalise(line)
        if not clean:
            continue
        run = SequenceMatcher(None, wanted, clean, autojunk=False)
        scored.append((run.find_longest_match().size / len(wanted), doc.offset + index, clean))
    scored.sort(key=lambda row: (-row[0], row[1]))
    return scored[:NEAREST]


def preview(line: str) -> str:
    """A cut line says so. A 110-character window that ends mid-sentence looks
    like a short line, and the word being searched for is often past it."""
    return line if len(line) <= PREVIEW else line[:PREVIEW] + "\u2026"


def report(doc: Document, quote: str) -> int:
    hits = locate(doc, quote)
    for line in hits:
        print(f"^[L{line}]  {preview(quotes.normalise(doc.lines()[line - doc.offset]))}")
    if hits:
        if len(hits) > 1:
            print(f"\n{len(hits)} lines carry these words. The citation is a claim about "
                  "which\none the reading came from — pick it, do not take the first.")
        return 0
    for first, last in spans(doc, quote):
        print(f"SPANS L{first}-{last}. A quote crossing two lines cannot be cited: the "
              "line\nnumber is part of the claim. Cite one line, or quote a fragment.")
        return 1
    print("NOT IN THIS DOCUMENT, on any single line. Nearest:")
    for share, line, clean in nearest(doc, quote):
        print(f"  L{line}  {share:.0%} in common  {preview(clean)}")
    return 1


def main(argv: list[str]) -> int:
    if not argv:
        print(__doc__.strip().split("Usage:")[-1].strip())
        return 2
    doc = document(argv[0])
    rest = argv[1:]

    def option(name: str, fallback: str | None = None) -> str | None:
        return rest[rest.index(name) + 1] if name in rest else fallback

    if "--find" in rest:
        return report(doc, option("--find") or "")
    last_line = doc.offset + len(doc.lines()) - 1
    first = int(option("--from", str(doc.offset)))
    last = min(int(option("--to", str(last_line))), last_line)
    print("\n".join(numbered(doc, first, last)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
