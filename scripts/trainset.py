"""The judgement ledger as a trainset, and the baseline any model must beat.

`Plan/runs/judgements.jsonl` was written to keep mechanised rules checkable. It
turns out to be a labelled dataset as well, and an unusually well-shaped one:
every record carries the two surfaces, the decision, **and a `rule` field stating
in words why**. GEPA's entry in the optimizer table does not ask for a number of
examples — it asks that "failures can be described in words, not just scored".
This ledger was already written that way, for a different reason.

## The baseline, measured before anything is optimized

The deterministic rule in the repository — `fold()` equality — scores
**14/17 = 82%** on the labelled records. The three it misses are not bugs:

| id | pair | why fold() will not decide it |
|---|---|---|
| J4 | `Kern-Welten` / `Kern-Welt` | folding is deliberately not stemming; a stemmer aggressive enough to merge a plural also merges `Negentropie` with `Entropie` |
| J6, J14 | `Der Möglichkeits-Garten / Nexus-Vorstufe` / `Möglichkeits-Garten` | no rule exists for a slash inside a heading |

**So the 18% gap is the boundary of what a safe deterministic rule can claim**,
not a defect in it. That is the interesting place to put a model, and the reason
to measure the baseline first: anything that does not beat 82% is not worth a
call, and anything that beats it by breaking `Negentropie`/`Entropie` is worse
than the baseline however it scores.

## The metric is GEPA-shaped already

`score_one` returns `dspy.Prediction(score, feedback)` where the feedback is the
recorded rule — the human's words for why, which is what a reflective optimizer
reads. No LM is needed to produce it and none can fake it.

Usage:
    python3 scripts/trainset.py               # sizes, baseline, what is blocked
    python3 scripts/trainset.py --export      # write Plan/trainsets/*.jsonl
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "Plan" / "runs" / "judgements.jsonl"
OUT = ROOT / "Plan" / "trainsets"
sys.path.insert(0, str(ROOT / "scripts"))

DECIDED = ("one-term", "two-terms")


def surface_pairs() -> list[dict]:
    """The one-term-or-two task: the only task here with usable gold labels."""
    from judgements import records
    rows = []
    for record in records():
        if record["decision"] not in DECIDED or len(record.get("surfaces", [])) != 2:
            continue
        rows.append({
            "id": record["id"],
            "first": record["surfaces"][0],
            "second": record["surfaces"][1],
            "document": record.get("document", ""),
            "decision": record["decision"],          # the gold label
            "rule": record.get("rule", ""),          # the gold explanation — GEPA feedback
            "features": record.get("env_features", []),
        })
    return rows


def fold_baseline(rows: list[dict]) -> dict:
    """What the repository's own deterministic rule scores. Measure before optimizing."""
    from wiki_index import fold
    misses = []
    correct = 0
    for row in rows:
        predicted = "one-term" if fold(row["first"]) == fold(row["second"]) else "two-terms"
        if predicted == row["decision"]:
            correct += 1
        else:
            misses.append({**row, "predicted": predicted})
    return {"correct": correct, "total": len(rows),
            "accuracy": correct / len(rows) if rows else 0.0, "misses": misses}


def score_one(gold: dict, predicted: str):
    """GEPA-shaped: a score and the human's words for why, not a bare float."""
    hit = predicted.strip().lower() == gold["decision"]
    return {
        "score": 1.0 if hit else 0.0,
        "feedback": ("correct" if hit else
                     f"wrong: {gold['first']!r} / {gold['second']!r} is "
                     f"{gold['decision']}, because {gold['rule']}"),
    }


def blocked() -> list[dict]:
    """Tasks that cannot be trained yet, with the reason stated rather than implied."""
    runs = ROOT / "Plan" / "runs"
    lists = list(runs.glob("*/03-candidates.md"))
    reconstructions = [p for p in lists
                       if "reconstruct" in p.read_text(encoding="utf-8")[:300].lower()]
    return [
        {"task": "extract candidate terms from a document",
         "examples": len(lists), "usable": len(lists) - len(reconstructions),
         "why": "every candidate list so far is a reconstruction written after the "
                "counts, not while reading. capture.py refuses to count before a list "
                "exists, so document 5 onward can produce real ones — these cannot."},
        {"task": "is this a conflict",
         "examples": len(list((ROOT / "Wiki" / "conflicts").glob("*.md"))) + 1,
         "usable": 0,
         "why": "four conflicts and one recorded false positive (Zero-Trust). Too few, "
                "and conflict detection is deliberately never mechanised."},
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--export", action="store_true")
    args = parser.parse_args()

    rows = surface_pairs()
    base = fold_baseline(rows)

    print(f"one-term-or-two: {len(rows)} labelled examples")
    print(f"  {sum(1 for r in rows if r['decision'] == 'one-term')} one-term, "
          f"{sum(1 for r in rows if r['decision'] == 'two-terms')} two-terms")
    print(f"  all {sum(1 for r in rows if r['rule'])} carry a stated rule — GEPA feedback")
    print(f"\nbaseline (fold() equality, the rule already in the repository):")
    print(f"  {base['correct']}/{base['total']} = {base['accuracy']:.0%}")
    for miss in base["misses"]:
        print(f"    MISS {miss['id']:5} {miss['first']!r} / {miss['second']!r}")
        print(f"          gold {miss['decision']}, fold() said {miss['predicted']}")
    print("\n  Anything that does not beat this is not worth an LM call.")

    print("\nblocked, and why:")
    for row in blocked():
        print(f"  {row['task']}")
        print(f"    {row['usable']} usable of {row['examples']} — {row['why']}")

    if args.export:
        OUT.mkdir(parents=True, exist_ok=True)
        path = OUT / "surface-pairs.jsonl"
        path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows),
                        encoding="utf-8")
        print(f"\nwrote {len(rows)} examples to {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
