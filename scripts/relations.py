"""What the wiki says relates to what, and what it says it does not know.

Two things are already written on every page and neither is machine-readable:

**Relations.** A page mentions another page as `` `slug` ``. 45 such mentions
exist across 46 pages — and **22 pages nothing mentions at all.** The wiki is a
list of terms with a very sparse graph over it, and that is not cosmetic: the
three hardest open problems are all *relation* questions, not term questions.

    C4   what is the relation between the Guardians and AEGIS?
    J18  are `Nexus` and `Überraum` one space?
    J13  is `Kael-Julia-Bindung` what the corpus calls this thing?

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


@lru_cache(maxsize=1)
def graph() -> dict:
    """Pages, the mentions between them, and what nothing mentions."""
    slugs = sorted(p.stem for p in PAGES.glob("*.md"))
    edges: list[tuple[str, str]] = []
    for path in sorted(PAGES.glob("*.md")):
        body = path.read_text(encoding="utf-8")
        for other in slugs:
            if other != path.stem and f"`{other}`" in body:
                edges.append((path.stem, other))
    linked_to = {target for _, target in edges}
    return {
        "pages": slugs,
        "edges": edges,
        "orphans": [s for s in slugs if s not in linked_to],
        "isolated": [s for s in slugs
                     if s not in linked_to and not any(a == s for a, _ in edges)],
    }


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
    parser.add_argument("--open", dest="show_open", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    g, q = graph(), open_questions()
    if args.json:
        print(json.dumps({"graph": g, "open_questions": q}, indent=2, ensure_ascii=False))
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
    print(f"relations       {len(g['edges'])}  (a page naming another as `slug`)")
    print(f"orphans         {len(g['orphans'])}  nothing links to them")
    print(f"isolated        {len(g['isolated'])}  no link in and none out")
    print(f"open questions  {len(q)}  across {len({r['page'] for r in q})} pages")
    print("\n  --orphans, --open, --json")
    print("  Derived from what pages already say. No relation is invented here.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
