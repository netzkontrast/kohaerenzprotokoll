"""What the wiki says relates to what, and what it says it does not know.

Two things are already written on every page and neither is machine-readable:

**Relations.** A page links another as `[[slug]]`, or `[[slug|as the prose reads
it]]`. Backticks mean something else and now only that: `` `Nexus` `` names a
term, it does not point at a page. Both were the same mark until the two meanings
were separated, which is why the graph could not distinguish a cross-reference
from a word in code font. The three hardest open problems are all *relation*
questions rather than term questions:

    C4   what is the relation between the Guardians and AEGIS?
    J18  are `Nexus` and `Überraum` one space?
    J13  is `Kael-Julia-Bindung` what the corpus calls this thing?

**And the markup undercounts the wiki badly.** `--unmarked` finds every place a
page writes another page's *term* in prose without marking it, and there are
three times as many of those as there are marked links. `aegis` is the clearest
case: nothing links to it, and its term is written in the prose of a dozen other
pages. A page that reads as connected and measures as an orphan is a markup
problem, not a content problem, and only the second kind is worth writing.

`account(subject, question)` has subjects for a document, a term, a pair of
surfaces, the corpus and the pipeline's order. It has none for a relation, which
is why those three had to be argued in prose instead of looked up.

**Open questions.** 36 of 46 pages carry an `## Open` section — about 70
statements of what a source did not settle. They were written as honesty and they
are also two other things nobody used: **the work queue** (what a next document
would have to answer to be worth reading) and **the evaluation set** (can the
wiki answer this yet?). The `dspy-deep-refine` loop consumes exactly this shape.

## Derived, not extracted

Everything here comes from what pages already say — a mention is a mention. No
model is asked to invent a relation, for the same reason conflict detection is
never mechanised: a guessed edge is indistinguishable from a stated one once it
is in the graph, and it would be believed.

Whether an LM should propose relations the prose does not state is a separate
question, to be asked against this baseline rather than instead of it.

Usage:
    python3 scripts/relations.py              # the graph and the queue
    python3 scripts/relations.py --orphans    # pages nothing links to
    python3 scripts/relations.py --unmarked   # links the prose makes and the markup does not
    python3 scripts/relations.py --open       # every open question, by page
    python3 scripts/relations.py --json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "Wiki" / "candidates"
OPEN_HEAD = re.compile(r"^##+ .*\bOpen\b.*$", re.M | re.I)
NEXT_HEAD = re.compile(r"^##+ ", re.M)
SENTENCE = re.compile(r"(?<=[.?])\s+")
TICKED = re.compile(r"`[^`]*`")
LINK = re.compile(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]")
SHORTEST_TERM = 4


@lru_cache(maxsize=1)
def graph() -> dict:
    """Pages, the mentions between them, and what nothing mentions."""
    slugs = sorted(p.stem for p in PAGES.glob("*.md"))
    known = set(slugs)
    edges: list[tuple[str, str]] = []
    broken: list[tuple[str, str]] = []
    for path in sorted(PAGES.glob("*.md")):
        body = path.read_text(encoding="utf-8")
        for target in dict.fromkeys(LINK.findall(body)):
            if target == path.stem:
                continue
            (edges if target in known else broken).append((path.stem, target))
    linked_to = {target for _, target in edges}
    return {
        "pages": slugs,
        "edges": edges,
        "broken": broken,
        "orphans": [s for s in slugs if s not in linked_to],
        "isolated": [s for s in slugs
                     if s not in linked_to and not any(a == s for a, _ in edges)],
    }


def term_of(slug: str) -> str:
    """The term a page is about, from its frontmatter, falling back to the slug."""
    head = (PAGES / f"{slug}.md").read_text(encoding="utf-8")[:600]
    match = re.search(r"^term:\s*(.+)$", head, re.M)
    return match.group(1).strip().strip('"') if match else slug


@lru_cache(maxsize=1)
def unmarked() -> list[tuple[str, str, int]]:
    """(source, target, times) where a page writes another's term and does not mark it.

    Only prose outside backticks counts, so an already-marked link is never
    reported twice, and a term shorter than SHORTEST_TERM is skipped for the
    same reason every comparison here has a length guard: a short string is a
    substring of far too much.
    """
    slugs = sorted(p.stem for p in PAGES.glob("*.md"))
    terms = {s: term_of(s) for s in slugs}
    linked = {edge for edge in graph()["edges"]}
    found = []
    for path in sorted(PAGES.glob("*.md")):
        prose = TICKED.sub("", LINK.sub("", path.read_text(encoding="utf-8")))
        for other in slugs:
            if other == path.stem or len(terms[other]) < SHORTEST_TERM:
                continue
            if (path.stem, other) in linked:
                continue
            hits = len(re.findall(
                rf"(?<![\w-]){re.escape(terms[other])}(?![\w-])", prose))
            if hits:
                found.append((path.stem, other, hits))
    return found


@lru_cache(maxsize=1)
def open_questions() -> list[dict]:
    """Every statement under an `## Open` heading, with the page it sits on."""
    found = []
    for path in sorted(PAGES.glob("*.md")):
        body = path.read_text(encoding="utf-8")
        for head in OPEN_HEAD.finditer(body):
            rest = body[head.end():]
            nxt = NEXT_HEAD.search(rest)
            section = rest[:nxt.start()] if nxt else rest
            for piece in SENTENCE.split(section):
                text = " ".join(piece.split())
                if len(text) >= 25:
                    found.append({"page": path.stem, "question": text})
    return found


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--orphans", action="store_true")
    parser.add_argument("--unmarked", action="store_true")
    parser.add_argument("--open", dest="show_open", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    g, q = graph(), open_questions()
    if args.json:
        print(json.dumps({"graph": g, "open_questions": q,
                          "unmarked": unmarked()}, indent=2, ensure_ascii=False))
        return 0

    if args.unmarked:
        rows = unmarked()
        inbound: dict[str, int] = {}
        for _, target, hits in rows:
            inbound[target] = inbound.get(target, 0) + hits
        print(f"{len(rows)} unmarked mentions against {len(g['edges'])} marked links.\n")
        for slug in sorted(g["orphans"], key=lambda s: -inbound.get(s, 0)):
            if inbound.get(slug):
                print(f"  {slug:28} 0 marked in, {inbound[slug]} unmarked")
        never = [s for s in g["orphans"] if not inbound.get(s)]
        print(f"\n  {len(never)} orphans no page mentions at all, marked or not:")
        print("    " + ", ".join(never))
        print("\n  For some of these the isolation is the finding. The protocol terms"
              "\n  are asked about in Q2 precisely because one document introduced them"
              "\n  and did nothing but evaluate them.")
        return 0

    if args.orphans:
        print(f"{len(g['orphans'])} of {len(g['pages'])} pages nothing links to:\n")
        for slug in g["orphans"]:
            out = sum(1 for a, _ in g["edges"] if a == slug)
            print(f"  {slug:34} links out {out}")
        return 0

    if args.show_open:
        page = None
        for row in q:
            if row["page"] != page:
                page = row["page"]
                print(f"\n{page}")
            print(f"  - {row['question'][:110]}")
        print(f"\n{len(q)} open questions across "
              f"{len({r['page'] for r in q})} pages")
        return 0

    print(f"pages           {len(g['pages'])}")
    print(f"relations       {len(g['edges'])}  (a page linking another as [[slug]])")
    if g["broken"]:
        print(f"BROKEN LINKS    {len(g['broken'])}  pointing at no page: "
              + ", ".join(sorted({t for _, t in g['broken']})))
    print(f"orphans         {len(g['orphans'])}  nothing links to them")
    print(f"isolated        {len(g['isolated'])}  no link in and none out")
    print(f"open questions  {len(q)}  across {len({r['page'] for r in q})} pages")
    print(f"unmarked        {len(unmarked())}  a page's term written in another's "
          f"prose, not marked")
    print("\n  --orphans, --unmarked, --open, --json")
    print("  Derived from what pages already say. No relation is invented here.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
