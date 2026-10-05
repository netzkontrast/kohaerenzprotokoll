"""The hit and the pack: one contract under every finder and every renderer (SPEC.md §4.2–4.3, migration step 4).

A finder returns **hits** — line ranges of a landed document, never prose:

    {"doc": slug, "line_start": 61, "line_end": 65, "anchors": [63], "finders": ["graph-evidence"], "rank": 0}

`hits(route, store)` turns `ask.route`'s anchors into hits: each anchor widened to its paragraph (or ±`window`
lines when the paragraph is long), touching spans of one document merged, documents in the route's rank order.
An anchor above a document's body (its frontmatter) is dropped: a frontmatter line is metadata, not source text.

`fit(items, budget, size)` is the one selection rule both packs use: items in order, each kept if it still fits
the budget and **skipped, not truncated,** if it does not — the next one is tried. What was skipped is returned,
never dropped silently: a pack with `omitted` is `incomplete` (`status`). `ask.build_pack` fits document blocks into
a byte budget over the whole serialized pack; `kg.bounded_context` fits quotations into its JSON's bytes.

The budget unit is **UTF-8 bytes** of the serialized text — what a transport carries and what `kg` always counted.
Characters are reported beside it. No model tokenizer is assumed.

Standard library.

    python3 scripts/pack.py selftest
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

WINDOW = 3            # lines on each side of an anchor when its paragraph is too long
PER_PARA = 6          # a paragraph up to 13 lines is shown whole
STATUSES = ("complete", "incomplete", "no_evidence", "refused")


class Refused(ValueError):
    """The parts of a pack that are never cut do not fit its budget."""


def size(text: str) -> int:
    """The budget unit: UTF-8 bytes."""
    return len(text.encode("utf-8"))


def body_start(doc: str, document=None) -> int:
    """The file line of a document's first body line (`subject.Document.offset`); 1 when the document is unknown."""
    if document is None:
        import subject
        document = subject.document
    try:
        return document(doc).offset
    except KeyError:
        return 1


def spans(store, doc: str, lines, window: int = WINDOW, per_para: int = PER_PARA) -> list[list[int]]:
    """Each anchor line widened to its paragraph (or ±window), merged where they touch; lines in file order."""
    out: list[list[int]] = []
    for line in sorted(lines):
        para = store.paragraph(doc, line)
        lo, hi = (para if para and para[1] - para[0] <= 2 * per_para else (line - window, line + window))
        lo, hi = max(1, min(lo, line - 1)), max(hi, line + 1)
        if out and lo <= out[-1][1] + 1:
            out[-1][1] = max(out[-1][1], hi)
        else:
            out.append([lo, hi])
    return out


def hits(route: dict, store, document=None, frontmatter: bool = False) -> list[dict]:
    """The route's anchors as hits, in its document order; frontmatter anchors dropped (`frontmatter_anchors`
    counts them) unless `frontmatter` keeps them, as the pack did before the contract."""
    out = []
    for rank, d in enumerate(route["docs"]):
        start = 1 if frontmatter else body_start(d["doc"], document)
        anchors = sorted(n for n in d["lines"] if n >= start)
        if not anchors:
            continue
        for lo, hi in spans(store, d["doc"], anchors):
            out.append({"doc": d["doc"], "line_start": lo, "line_end": hi,
                        "anchors": [n for n in anchors if lo <= n <= hi],
                        "finders": sorted(d["finders"]), "rank": rank})
    return out


def frontmatter_anchors(route: dict, document=None) -> int:
    return sum(1 for d in route["docs"] for n in d["lines"] if n < body_start(d["doc"], document))


def by_document(hit_list: list[dict]) -> list[tuple[str, list[dict]]]:
    """Hits grouped by document, in rank order."""
    groups: dict[str, list[dict]] = {}
    for h in hit_list:
        groups.setdefault(h["doc"], []).append(h)
    return sorted(groups.items(), key=lambda kv: kv[1][0]["rank"])


def fit(items, budget: int, measure, used: int = 0) -> tuple[list, list, int]:
    """Keep each item that still fits `budget` (given `used`), skip the rest; return kept, omitted, used."""
    kept, omitted = [], []
    for item in items:
        n = measure(item)
        if used + n > budget:
            omitted.append(item)
            continue
        kept.append(item)
        used += n
    return kept, omitted, used


def status(kept, omitted, refused: bool = False) -> str:
    if refused:
        return "refused"
    if not kept and not omitted:
        return "no_evidence"
    return "incomplete" if omitted else "complete"


def selftest() -> list[str]:
    """Each rule handed the case that breaks it; no store, no corpus file."""
    from types import SimpleNamespace
    fails = []

    class Store:
        def paragraph(self, doc, line):
            return {5: (4, 6), 30: (10, 40)}.get(line)

    docs = {"d": SimpleNamespace(offset=4), "e": SimpleNamespace(offset=1)}
    lookup = lambda slug: docs[slug] if slug in docs else (_ for _ in ()).throw(KeyError(slug))  # noqa: E731
    route = {"docs": [{"doc": "d", "lines": {2, 5, 7, 30}, "finders": {"bm25-lines", "graph-evidence"}},
                      {"doc": "e", "lines": {1}, "finders": {"parallel"}},
                      {"doc": "x", "lines": {9}, "finders": {"bm25-lines"}}]}
    got = hits(route, Store(), lookup)
    if [(h["doc"], h["line_start"], h["line_end"], h["anchors"]) for h in got] != [
            ("d", 4, 10, [5, 7]), ("d", 27, 33, [30]), ("e", 1, 4, [1]), ("x", 6, 12, [9])]:
        fails.append(f"hits: widening, merging, frontmatter or order wrong: {got}")
    if frontmatter_anchors(route, lookup) != 1:
        fails.append("the frontmatter anchor (d:L2) was not counted")
    if [d for d, _ in by_document(got)] != ["d", "e", "x"]:
        fails.append("by_document lost the route's rank order")
    kept, omitted, used = fit(["aaaa", "bbbbbbbb", "cc"], 7, len)
    if kept != ["aaaa", "cc"] or omitted != ["bbbbbbbb"] or used != 6:
        fails.append(f"fit: an item that does not fit must be skipped and the next tried: {kept} {omitted} {used}")
    if (status([], []), status(["a"], []), status(["a"], ["b"]), status([], [], refused=True)) != \
            ("no_evidence", "complete", "incomplete", "refused"):
        fails.append("status mislabels a pack")
    if size("ä") != 2:
        fails.append("the budget unit is not UTF-8 bytes")
    return fails


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        fails = selftest()
        for f in fails:
            print(f"  FAIL  {f}")
        print(f"pack: {6 - len(fails)} of 6 cases hold (hits, frontmatter count, rank order, fit skips, status, unit)")
        return 1 if fails else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
