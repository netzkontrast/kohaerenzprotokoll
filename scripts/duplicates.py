"""Whether any landed document is a near-copy of another. Today: none.

Drive held up to five exports of the same document -- a gdoc export, a docx
export, a `kopie` of each, and a second run of both -- and `sources.py` landed
every one, because each is its own `drive_id`. **409 files were 346 documents**,
and every count phrased as "N of 409 documents" was counting copies.

Found when `qmd` returned four hits for one query, at the same line, in four
slugs differing only by suffix.

`scripts/dedupe.py` has since folded the 63 extra files away, so this script now
reports 0 groups and its job has changed: it is the check that says so. **A count
over files and a count over documents are the same number again, and this is what
keeps them that way.** Run it after landing anything new.

## What it cost while it was true

| term | files | documents | today |
|---|--:|--:|--:|
| AEGIS | 315 | 276 | 269 |
| Kael | 287 | 256 | 249 |
| Entropie | 206 | 160 | 151 |
| Guardians | 104 | 90 | 87 |

Proportions mostly survived, because duplication was roughly uniform -- but not
always: `Entropie` was 50% of files and 45% of documents, and is 44% now. **An
absolute count was wrong by about 15%; a proportion was usually right and
sometimes not.**

## Why byte-identity was not enough

Only **2** were byte-identical to another, and `sources.py` had
already caught those two at landing time. The rest differed by export run, a
heading, a footnote number -- so `sha256` found almost none of it. The comparison
is a Jaccard overlap of 8-word shingles at 0.8. The threshold is a choice, not a
fact: `--threshold` moves it and `--groups` shows what changed.

**`STRIDE` must stay 1.** At 4 the measure is phase-sensitive: one inserted word
breaks shingle alignment for everything after it, so the same document scored
0.258 against its own copy instead of 0.841, and the run reported 52 near-copies
where there were 63. A sweep at stride 1 gives 0.897 / 0.841 / 0.788 for shingle
5 / 8 / 12 -- the shingle length is a tuning choice, the stride is not.

Usage:
    python3 scripts/duplicates.py                  # the groups and the totals
    python3 scripts/duplicates.py --term AEGIS     # one term, counted both ways
    python3 scripts/duplicates.py --threshold 0.6
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from subject import documents, facts  # noqa: E402

WORD = re.compile(r"\w+")
SHINGLE, STRIDE = 8, 1


def signature(body: str) -> set[bytes]:
    words = WORD.findall(body.lower())
    return {
        hashlib.blake2b(" ".join(words[i:i + SHINGLE]).encode(), digest_size=8).digest()
        for i in range(0, max(1, len(words) - SHINGLE), STRIDE)  # STRIDE must stay 1
    }


CACHE = ROOT / "Plan" / "derived" / "duplicates.json"


def _fingerprint(docs) -> str:
    """The corpus this answer is about: every slug and checksum, hashed."""
    joined = "".join(f"{d.slug}:{d.sha256}" for d in docs)
    return hashlib.blake2b(joined.encode(), digest_size=16).hexdigest()


@lru_cache(maxsize=4)
def representatives(threshold: float) -> dict[str, str]:
    """Each slug mapped to the first slug of its near-duplicate group.

    Cached on disk keyed by (corpus fingerprint, threshold). The comparison is
    O(n^2) over every shingle set: 16 seconds over 371 documents, 63 before
    pairs of too different a size were skipped. `state.py` asks for it on every
    run, so re-deriving it each time would make the state check unusable. The cache is invalidated by any document changing or any document
    being added, which is the same rule `derive.py` uses.
    """
    docs = list(documents())
    fingerprint = _fingerprint(docs)
    if CACHE.exists():
        stored = json.loads(CACHE.read_text(encoding="utf-8"))
        if stored.get("fingerprint") == fingerprint and stored.get("threshold") == threshold:
            return stored["representatives"]
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
            if not (a and b):
                continue
            # |a & b| / |a | b| can never exceed the smaller set over the larger,
            # so a pair whose sizes alone fall short needs no intersection. It
            # decides the same: 371 of 371 representatives, measured at 0.8.
            small, large = sorted((len(a), len(b)))
            if small / large >= threshold and len(a & b) / len(a | b) >= threshold:
                rep[other] = first
    CACHE.parent.mkdir(parents=True, exist_ok=True)
    # Written aside and renamed into place: `selftests.py` runs suites at once,
    # and two of them derive the state, so a reader must see a whole file or none.
    written = CACHE.with_name(f"{CACHE.name}.{os.getpid()}")
    written.write_text(json.dumps({"fingerprint": fingerprint, "threshold": threshold,
                                   "representatives": rep}, indent=2) + "\n", encoding="utf-8")
    os.replace(written, CACHE)
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
    if not found:
        print("No near-copies. A count over files is a count over documents.")
        return 0
    for group in found if args.groups else found[:12]:
        print(f"  {len(group)}x  {group[0]}")
        if args.groups:
            for slug in group[1:]:
                print(f"       {slug}")
    if not args.groups and len(found) > 12:
        print(f"  … {len(found) - 12} more groups — --groups for all")
    print("\nA count over files is not a count over documents. Say which one it is.")
    print("scripts/dedupe.py folds these away.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
