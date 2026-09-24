"""Merge the four parallel chunk readings: code places every line, refuses the rest.

Each chunk_N.tsv is `subject<TAB>RELATION<TAB>object` from one Haiku reader that
saw only its line range. A subject or object the range does not contain as a
whole word (entities.holds, the rule `place` uses) refuses the row — a model's
line is never typed, and a name it did not read is never kept (P26). Rows that
survive are deduplicated by exact string; names are the union of subjects and
objects, and are scored like any other names file.

    python3 Plan/runs/<slug>/second-readers/fast/merge.py [--repair]
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
SLUG = HERE.parents[1].name
sys.path.insert(0, str(ROOT / "scripts"))
from entities import holds  # noqa: E402

RANGES = {1: (1, 342), 2: (343, 730), 3: (731, 1070), 4: (1071, 1393)}
lines = (ROOT / "Sources" / "drive" / f"{SLUG}.md").read_text(encoding="utf-8").split("\n")

REPAIR = "--repair" in sys.argv


def place(term, lo, hi):
    """First line in the range holding the term as a whole word. With --repair, an
    underscore the reader wrote for a space is read as a space first; the raw
    term is still tried after it (the document writes an underscore only in three
    file names, L1393), and the placed name must stand on its line word for word."""
    for candidate in ([term.replace("_", " ")] if REPAIR and "_" in term else []) + [term]:
        for n in range(lo, hi + 1):
            if holds(lines[n - 1], candidate):
                return n
    return None

kept, refused, seen = [], [], set()
for k, (lo, hi) in RANGES.items():
    path = HERE / f"chunk_{k}.tsv"
    if not path.exists():
        print(f"chunk_{k}.tsv missing"); continue
    for raw in path.read_text(encoding="utf-8").splitlines():
        parts = [p.strip() for p in raw.split("\t")]
        if len(parts) != 3 or not all(parts):
            refused.append((k, raw, "not three fields")); continue
        s, r, o = parts
        if REPAIR:
            s, o = s.replace("_", " "), o.replace("_", " ")
        ls, lo_ = place(s, lo, hi), place(o, lo, hi)
        if ls is None or lo_ is None:
            refused.append((k, raw, "subject" if ls is None else "object")); continue
        if (s, r, o) in seen:
            continue
        seen.add((s, r, o)); kept.append((s, r, o, k, ls, lo_))
(HERE / ("merged-repaired.tsv" if REPAIR else "merged.tsv")).write_text("".join(f"{s}\t{r}\t{o}\tchunk{k}\tL{a}\tL{b}\n" for s, r, o, k, a, b in kept), encoding="utf-8")
(HERE / ("refused-repaired.tsv" if REPAIR else "refused.tsv")).write_text("".join(f"chunk{k}\t{why}\t{raw}\n" for k, raw, why in refused), encoding="utf-8")
names = sorted({s for s, *_ in kept} | {o for _, _, o, *_ in kept})
(HERE / ("names-repaired.json" if REPAIR else "names.json")).write_text(json.dumps({"source": SLUG, "written_by": "four Haiku readers in parallel, one per chapter block; lines by code",
    "entities": [{"term": n} for n in names]}, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{len(kept)} rows kept, {len(refused)} refused, {len(names)} names, {len({r for _, r, *_ in kept})} relations")
