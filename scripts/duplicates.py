"""Which landed documents are copies of each other, and what that costs a count.

Drive holds several copies of many documents -- `…-docx.md`, `…-docx-2.md`,
`…-kopie-docx.md` -- and `sources.py` landed each as its own row because each is
its own `drive_id` with its own checksum. That is correct: the manifest records
what Drive holds. But **409 files are 357 documents**, and every count phrased as
"N of 409 documents" has been counting copies.

Found when `qmd` returned four hits for one query, at the same line, in four
slugs differing only by suffix.

## What it changes, measured

| term | documents | distinct | of 409 | of 357 |
|---|--:|--:|--:|--:|
| AEGIS | 315 | 276 | 77% | 77% |
| Kael | 287 | 256 | 70% | 72% |
| Entropie | 206 | 160 | 50% | **45%** |
| Guardians | 104 | 90 | 25% | 25% |

Proportions mostly survive, because duplication is roughly uniform -- but not
always: `Entropie` drops five points, so the copies are concentrated in
entropy-heavy documents. **An absolute count is wrong by about 13%; a proportion
is usually right and sometimes not.** Which is exactly why this is a script and
not a footnote.

## Why byte-identity is not enough

Only **2** of the 409 are byte-identical to another. The rest differ by export
run, a heading, a footnote number -- so `sha256` finds almost nothing. The
comparison is a Jaccard overlap of 8-word shingles at 0.8, which finds 29 groups
covering 52 files. The threshold is a choice, not a fact: `--threshold` moves it
and `--groups` shows what changed.

Usage:
    python3 scripts/duplicates.py                  # the groups and the totals
    python3 scripts/duplicates.py --term AEGIS     # one term, counted both ways
    python3 scripts/duplicates.py --threshold 0.6
"""

from __future__ import annotations

import argparse
import hashlib
import re
import sys
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from subject import documents, facts  # noqa: E402

WORD = re.compile(r"\w+")
SHINGLE, STRIDE = 8, 4


def signature(body: str) -> set[bytes]:
    words = WORD.findall(body.lower())
    return {
        hashlib.blake2b(" ".join(words[i:i + SHINGLE]).encode(), digest_size=8).digest()
        for i in range(0, max(1, len(words) - SHINGLE), STRIDE)
    }


@lru_cache(maxsize=4)
def representatives(threshold: float) -> dict[str, str]:
    """Each slug mapped to the first slug of its near-duplicate group."""
    docs = list(documents())
    signatures = {doc.slug: signature(doc.body) for doc in docs}
    rep: dict[str, str] = {}
    slugs = [doc.slug for doc in docs]
    for index, first in enumerate(slugs):
        if first in rep:
            continue
        rep[first] = first
        for other in slugs[index + 1:]:
            if other in rep:
                continue
            a, b = signatures[first], signatures[other]
            if a and b and len(a & b) / len(a | b) >= threshold:
                rep[other] = first
    return rep


def groups(threshold: float) -> list[list[str]]:
    rep = representatives(threshold)
    collected: dict[str, list[str]] = {}
    for slug, head in rep.items():
        collected.setdefault(head, []).append(slug)
    return sorted((g for g in collected.values() if len(g) > 1), key=len, reverse=True)


def distinct(slugs, threshold: float) -> int:
    rep = representatives(threshold)
    return len({rep.get(slug, slug) for slug in slugs})


def carrying(term: str) -> list[str]:
    return [d.slug for d in documents()
            if term in (facts(d.slug, "surfaces") or {}).get("tokens", {})]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--threshold", type=float, default=0.8)
    parser.add_argument("--term", help="count one term both ways")
    parser.add_argument("--groups", action="store_true", help="list every group in full")
    args = parser.parse_args()

    total = len(documents())
    found = groups(args.threshold)
    copies = sum(len(g) - 1 for g in found)

    if args.term:
        slugs = carrying(args.term)
        kept = distinct(slugs, args.threshold)
        print(f"{args.term}: {len(slugs)} documents, {kept} distinct "
              f"— {len(slugs) / total:.0%} of {total} files, "
              f"{kept / (total - copies):.0%} of {total - copies} documents")
        return 0

    print(f"{total} files, {total - copies} distinct documents "
          f"({copies} near-copies in {len(found)} groups, Jaccard >= {args.threshold})\n")
    for group in found if args.groups else found[:12]:
        print(f"  {len(group)}x  {group[0]}")
        if args.groups:
            for slug in group[1:]:
                print(f"       {slug}")
    if not args.groups and len(found) > 12:
        print(f"  … {len(found) - 12} more groups — --groups for all")
    print("\nA count over files is not a count over documents. Say which one it is.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
