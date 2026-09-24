"""The score of every program on every task, append-only, compared against a floor.

`optimizers-and-data_2026-09-17.md` measured the deterministic baseline first
— `fold()` at 17/26 — and said: anything that does not beat it is not worth a
call. That sentence needs somewhere to live that is not a person's memory.

`Plan/runs/baselines.jsonl` holds one row per scored run:

    task, candidate, program_hash, trainset_hash, n, scored, correct,
    score, vetoed, outcomes {id: 1 | 0 | fraction | null}, cost, at, note

- **`score` is correct / scored, and `scored` is reported beside `n`.** An
  example that could not be scored (unreachable, unparsed) is `null` in
  `outcomes`, never 0 and never 1 (P15, P23).
- **`vetoed`** is set when a candidate broke a hard constraint — a never-merge
  canary. A vetoed row fails `compare` whatever its score: `dspy.GEPA` optimizes
  a mean, so a candidate that merges `Negentropie`/`Entropie` otherwise loses
  only 1/26.
- **`compare` checks against the floor, not only the previous row.** Ported
  from `netzkontrast/dspy-agents` `dspy_optimize/baselines/monitor.py`, whose
  monitor compared each run only with the one before — so a run logged at
  `score=0.0, total_calls=0` became a normal baseline and a pipeline broken from
  its first run could never alert. Here the floor is the task's first row by
  default (the deterministic rule), or the candidate named by `--floor`.
- **`program_hash`** is a hash of what the program *is* (instructions, demos,
  rule source), never a tag someone bumps — `dspy-agents`
  `_program_artifact_signature`.

Done is a measurement (P24): which program is best is derived from this file,
never stored as a flag.

    python3 scripts/baseline.py show [task]
    python3 scripts/baseline.py compare <task> [--floor fold]
    python3 scripts/baseline.py selftest
"""

from __future__ import annotations

import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from subject import read_jsonl  # noqa: E402

LEDGER = ROOT / "Plan" / "runs" / "baselines.jsonl"
TOLERANCE = 0.02


def digest(*parts) -> str:
    """A short, stable hash of whatever a program or trainset consists of."""
    blob = json.dumps(parts, sort_keys=True, ensure_ascii=False, default=str)
    return hashlib.sha256(blob.encode("utf-8")).hexdigest()[:12]


def row(task: str, candidate: str, outcomes: dict[str, int | None], *, program: object,
        trainset: object, vetoed: bool = False, cost: float = 0.0, note: str = "") -> dict:
    """Build a ledger row. `outcomes` maps example id to 1 or 0 — or a fraction,
    for a graded case such as recall — or None when it could not be scored."""
    scored = [v for v in outcomes.values() if v is not None]
    return {
        "task": task, "candidate": candidate,
        "program_hash": digest(program), "trainset_hash": digest(trainset),
        "n": len(outcomes), "scored": len(scored), "correct": round(sum(scored), 4),
        "score": round(sum(scored) / len(scored), 4) if scored else None,
        "vetoed": vetoed, "outcomes": outcomes, "cost": cost,
        "at": datetime.now(timezone.utc).isoformat(timespec="seconds"), "note": note,
    }


def append(entry: dict, ledger: Path = LEDGER) -> dict:
    ledger.parent.mkdir(parents=True, exist_ok=True)
    with ledger.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")
    return entry


def rows(task: str | None = None, ledger: Path = LEDGER) -> list[dict]:
    if not ledger.exists():
        return []
    return [r for r in read_jsonl(ledger) if task is None or r["task"] == task]


def compare(task: str, floor: str | None = None, ledger: Path = LEDGER) -> tuple[str, list[str]]:
    """(`ok` | `warn` | `fail` | `unscored`, reasons) for the newest row of a task."""
    history = rows(task, ledger)
    if not history:
        return "unscored", [f"no rows for {task!r}"]
    latest = history[-1]
    reasons = []
    if latest["score"] is None:
        return "unscored", [f"{latest['candidate']}: 0 of {latest['n']} examples could be scored"]
    if latest["scored"] < latest["n"]:
        reasons.append(f"{latest['n'] - latest['scored']} of {latest['n']} examples not scored — "
                       "the score is over the rest")
    if latest["vetoed"]:
        return "fail", reasons + [f"{latest['candidate']} broke a never-merge canary"]
    floors = [r for r in history if r["candidate"] == floor] if floor else history[:1]
    if not floors:
        return "fail", reasons + [f"no row for floor {floor!r}"]
    base = floors[0]
    if latest is not base and base["trainset_hash"] != latest["trainset_hash"]:
        reasons.append(f"trainset changed since the floor ({base['trainset_hash']} → "
                       f"{latest['trainset_hash']}): re-score the floor before comparing")
        return "warn", reasons
    if latest is not base and latest["score"] <= base["score"]:
        return "fail", reasons + [f"{latest['candidate']} {latest['score']:.3f} does not beat the floor "
                                  f"{base['candidate']} {base['score']:.3f}"]
    earlier = [r for r in history[:-1] if r["score"] is not None and not r["vetoed"]]
    best = max(earlier, key=lambda r: r["score"], default=None)
    if best and latest["score"] < best["score"] - TOLERANCE:
        return "warn", reasons + [f"below the best earlier row, {best['candidate']} {best['score']:.3f}"]
    return ("warn" if reasons else "ok"), reasons


def selftest() -> list[str]:
    """Each verdict produced, each for its own reason."""
    import tempfile
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        ledger = Path(tmp) / "b.jsonl"
        t = ["a", "b", "c", "d"]
        append(row("x", "fold", {"a": 1, "b": 1, "c": 0, "d": 0}, program="fold", trainset=t), ledger)
        cases = [
            ("unscored", row("x", "m0", {i: None for i in t}, program="m0", trainset=t), "could be scored"),
            ("fail", row("x", "m1", {"a": 1, "b": 0, "c": 0, "d": 1}, program="m1", trainset=t), "does not beat"),
            ("fail", row("x", "m2", {i: 1 for i in t}, program="m2", trainset=t, vetoed=True), "canary"),
            ("ok", row("x", "m3", {"a": 1, "b": 1, "c": 1, "d": 0}, program="m3", trainset=t), ""),
            ("warn", row("x", "m4", {"a": 1, "b": 1, "c": 1, "d": None}, program="m4", trainset=t), "not scored"),
            ("warn", row("x", "m5", {"a": 1, "b": 1, "c": 1}, program="m5", trainset=t[:3]), "trainset changed"),
        ]
        for expected, entry, needle in cases:
            append(entry, ledger)
            verdict, why = compare("x", ledger=ledger)
            if verdict != expected or (needle and not any(needle in w for w in why)):
                failures.append(f"{entry['candidate']}: expected {expected} naming {needle!r}, got {verdict} {why}")
    if digest({"a": 1, "b": 2}) != digest({"b": 2, "a": 1}):
        failures.append("digest depends on key order")
    return failures


def main(argv: list[str]) -> int:
    if not argv or argv[0] == "show":
        task = argv[1] if len(argv) > 1 else None
        for r in rows(task):
            score = "—" if r["score"] is None else f"{r['score']:.3f}"
            flag = "  VETOED" if r["vetoed"] else ""
            print(f"{r['at'][:10]}  {r['task']:<16} {r['candidate']:<24} {score:>6}  "
                  f"{r['correct']}/{r['scored']} of {r['n']}  {r['program_hash']}{flag}")
        return 0
    if argv[0] == "compare" and len(argv) > 1:
        floor = argv[argv.index("--floor") + 1] if "--floor" in argv else None
        verdict, why = compare(argv[1], floor)
        print(verdict)
        for w in why:
            print(f"  {w}")
        return {"ok": 0, "warn": 0}.get(verdict, 1)
    if argv[0] == "selftest":
        problems = selftest()
        for p in problems:
            print(f"  FAIL  {p}")
        print(f"baseline: {7 - len(problems)} of 7 cases hold")
        return 1 if problems else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
