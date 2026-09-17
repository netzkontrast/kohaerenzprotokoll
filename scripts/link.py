"""Mark the links the prose already makes, without touching a single quotation.

The wiki was three times more connected than its own graph said: 48 marked links
against 158 places where one page wrote another page's term in prose and left it
unmarked. `aegis` was an orphan with its term standing unmarked in other pages 68
times. A page that reads as connected and measures as an orphan is a markup
problem, and this closes it.

Two syntaxes now mean two different things, which is the point of the change:

    `Nexus`              the term, named
    [[nexus]]            the link, set
    [[nexus|Nexus-Raum]] the link, set, with the prose left exactly as written

## What it will not touch, and why that is the whole design

Rewriting prose in a repository whose quotations are checked against source
lines is how a citation silently stops resolving. So the replacement runs only
in **linkable prose**, and everything else is masked out first:

- the frontmatter, fenced code, and inline `` `code` ``
- anything inside „…" or "…" — a quotation reproduces a source and may not gain
  markup the source did not have
- an existing `[[link]]` or a markdown `[text](url)`
- heading lines and blockquote lines
- **any line carrying a `^[` citation, entirely.** A line that cites is evidence.
  It is not edited to make a graph look better.

That mask governs the prose stage. The backtick-slug stage below deliberately
runs outside it — it rewrites a cross-reference and never the words of a
quotation — with one guard kept: it will not fire inside „…" either.

One link per page per target, at the first unmasked occurrence — a wiki links a
term once, not every time it appears.

## The one exception to the inline-code mask

A backticked token that is **exactly a page slug** — `` `aegis-metriken` `` — was
never code and never a term as the prose would write it (that is
„AEGIS-Metriken"). It is how this wiki wrote a cross-reference before there was a
link syntax, and it is converted. A backticked term that is not a slug is left
alone: `` `Nexus` `` names the term and points at nothing. Skipping this cost 4
pages their only inbound edge on the first run. This stage reaches a table row
that also carries a citation, and that is intended: it relabels the row's first
cell and leaves the quotation in the next cell untouched.

`python3 scripts/quotes.py` is the proof the pass was safe, and it is run before
and after.

Usage:
    python3 scripts/link.py             # dry run: what would be marked, where
    python3 scripts/link.py --apply     # mark them
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from relations import PAGES, SHORTEST_TERM, term_of  # noqa: E402

SOURCES = ["candidates", "conflicts", "questions"]
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)
FENCE = re.compile(r"```.*?```", re.S)
INLINE = re.compile(r"`[^`\n]*`")
# A German quotation wraps across lines, so this may not be line-bounded. It was,
# in the first version, and the pass put `[[logos]]` inside „…" on two pages
# before `quotes.py` reported them — the whole reason that check exists. Bounded
# at 600 characters and requiring a closer, so an unpaired „ cannot swallow a file.
QUOTED = re.compile(r"„[^„“]{0,600}[“\"]|\"[^\"\n]{0,400}\"")
WIKILINK = re.compile(r"\[\[[^\]]*\]\]")
MDLINK = re.compile(r"\[[^\]]*\]\([^)]*\)")
LINE_OUT = re.compile(r"^(?:\s*(?:#{1,6}|>).*|.*\^\[.*)$", re.M)
MASKS = (FRONTMATTER, FENCE, INLINE, QUOTED, WIKILINK, MDLINK, LINE_OUT)


def masked(text: str) -> list[bool]:
    """True where a character may not be rewritten."""
    block = [False] * len(text)
    for pattern in MASKS:
        for match in pattern.finditer(text):
            for i in range(match.start(), match.end()):
                block[i] = True
    return block


def first_free(text: str, block: list[bool], needle: str) -> int:
    """Where `needle` stands as a whole word outside every mask, or -1."""
    for match in re.finditer(rf"(?<![\w-]){re.escape(needle)}(?![\w-])", text):
        if not any(block[match.start():match.end()]):
            return match.start()
    return -1


def link_for(slug: str, surface: str) -> str:
    """`[[slug]]` when the prose already reads as the slug, else keep the prose."""
    if surface.strip("`").lower() == slug.lower():
        return f"[[{slug}]]"
    return f"[[{slug}|{surface}]]"


def ticked_slugs(text: str, known: set[str], own: str) -> list[tuple[int, str, str]]:
    """The first `` `slug` `` per target — the cross-reference written before links."""
    quotes = [(m.start(), m.end()) for m in QUOTED.finditer(text)]
    found, seen = [], set()
    for match in INLINE.finditer(text):
        slug = match.group(0).strip("`")
        if slug not in known or slug == own or slug in seen:
            continue
        if any(start <= match.start() < end for start, end in quotes):
            continue
        seen.add(slug)
        found.append((match.start(), slug, match.group(0)))
    return found


def proposals(path: Path, targets: dict[str, str]) -> list[tuple[int, str, str]]:
    """(position, slug, surface) for each link this page should gain, first-first."""
    text = path.read_text(encoding="utf-8")
    block = masked(text)
    found = ticked_slugs(text, set(targets), path.stem)
    already = {slug for _, slug, _ in found}
    for slug, term in targets.items():
        if slug in already:
            continue
        if slug == path.stem:
            continue
        # The term as the page writes it, else the slug itself — a page that
        # already cross-referenced `slug` in backticks keeps that link.
        for surface in (term, slug):
            if len(surface) < SHORTEST_TERM:
                continue
            at = first_free(text, block, surface)
            if at >= 0:
                found.append((at, slug, surface))
                break
    return sorted(found)


def rewrite(text: str, found: list[tuple[int, str, str]]) -> str:
    """Apply from the back, so every earlier position stays valid."""
    for at, slug, surface in sorted(found, reverse=True):
        text = text[:at] + link_for(slug, surface) + text[at + len(surface):]
    return text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    targets = {p.stem: term_of(p.stem) for p in sorted(PAGES.glob("*.md"))}
    files = [p for name in SOURCES
             for p in sorted((PAGES.parent / name).glob("*.md")) if p.stem != "README"]

    total = 0
    for path in files:
        found = proposals(path, targets)
        if not found:
            continue
        total += len(found)
        where = path.relative_to(ROOT)
        print(f"{where}  +{len(found)}")
        if not args.apply:
            for _, slug, surface in found[:6]:
                print(f"    {link_for(slug, surface)}")
            if len(found) > 6:
                print(f"    … and {len(found) - 6} more")
            continue
        path.write_text(rewrite(path.read_text(encoding="utf-8"), found), encoding="utf-8")

    print(f"\n{total} links {'marked' if args.apply else 'would be marked'} "
          f"across {len(files)} files.")
    if not args.apply:
        print("Nothing was written. Re-run with --apply, then scripts/quotes.py.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
