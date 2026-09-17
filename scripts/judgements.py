"""Replay every recorded judgement against the code that now claims to handle it.

A judgement is a decision a person made about a near match: one term or two. Some
of them get mechanised -- the rule goes into `fold()` and the case stops costing
anything. That is the whole point of recording them, and it is also the risk:
**a mechanised rule is a silent assumption unless it keeps being checked.**

So every judgement is replayable. `fold()` is applied to the recorded surfaces and
compared against the recorded decision:

    agrees        the code still decides what the person decided
    DISAGREES     the code changed, or the rule was wrong -- go and look
    judgement     no code claims this case; it is still a person's call

A DISAGREES is not automatically a bug in the code. It may be the record that is
wrong, or a rule that held for four documents and breaks on the fifth. **Either
way it is the signal that something needs looking at again**, which is what could
not happen while the rules lived only in a commit message.

Usage:
    python3 scripts/judgements.py            # replay all
    python3 scripts/judgements.py --open     # only the ones still needing judgement
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "Plan" / "runs" / "judgements.jsonl"

sys.path.insert(0, str(ROOT / "scripts"))
from wiki_index import fold  # noqa: E402


def records() -> list[dict]:
    """The ledger, parsed. The only place that reads the file."""
    if not LEDGER.exists():
        sys.exit(f"no ledger at {LEDGER.relative_to(ROOT)}")
    return [json.loads(line) for line in LEDGER.read_text(encoding="utf-8").splitlines()
            if line.strip()]


def replay(record: dict) -> tuple[str, str]:
    """Return (verdict, detail) for one recorded judgement."""
    surfaces = record.get("surfaces") or []
    if len(surfaces) != 2:
        return "skipped", "record does not name exactly two surfaces"
    if not record.get("mechanised_by"):
        return "judgement", "no code claims this case"

    folded = [fold(s) for s in surfaces]
    code_says = "one-term" if folded[0] == folded[1] else "two-terms"
    decided = record["decision"]
    detail = f"{folded[0]!r} vs {folded[1]!r} -> code says {code_says}"
    return ("agrees" if code_says == decided else "DISAGREES"), detail


def main(argv: list[str]) -> int:
    ledger = records()
    only_open = "--open" in argv

    counts = {"agrees": 0, "DISAGREES": 0, "judgement": 0, "skipped": 0}
    rows = []
    for record in ledger:
        verdict, detail = replay(record)
        counts[verdict] += 1
        if only_open and verdict != "judgement":
            continue
        rows.append((verdict, record, detail))

    for verdict, record, detail in rows:
        pair = " / ".join(record.get("surfaces", []))
        print(f"  {verdict:10} {record['id']:4} {pair}")
        print(f"             {record['decision']:10} "
              f"{record['rule'] or '— no rule stated; this one is still open'}")
        if verdict == "DISAGREES":
            print(f"             !! {detail}")
        print()

    print(f"{len(ledger)} judgements: "
          f"{counts['agrees']} agree, {counts['DISAGREES']} DISAGREE, "
          f"{counts['judgement']} still judgement, {counts['skipped']} skipped")
    if counts["DISAGREES"]:
        print("\nA DISAGREES means the code and a recorded decision no longer match.")
        print("It may be the code, or the record, or a rule that has met its first exception.")
        return 1
    return 0


if __name__ == "__main__":
    try:
        import signal

        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass
    raise SystemExit(main(sys.argv[1:]))
