#!/usr/bin/env python3
"""Which model reads a contract on a source: mostly the best measured one, sometimes another, at random — to learn.

The author, 2026-10-01: „Lets then implement it in a way that it Rotates Models - Maybe at 20% of the time Random - so
that we can learn which Models to use where". The policy is `Plan/hyperextract/models.json` — the pool, the default,
the share of runs that explore (`explore`), and how many labelled rows a model needs before it counts (`min_labels`).

**Explore.** A run explores when `u < explore`, `u` a number in [0, 1) drawn from the sha256 of `contract|slug|run` —
random across runs, the same every time for one run, so a choice can be re-derived and checked. An exploring run takes a
model from the pool by a second draw from the same hash.

**Exploit.** Otherwise the model with the highest labelled precision for this contract — the share of its labelled rows
marked `ok` (`Plan/runs/hyperextract-templates-2026-09-30/labels.jsonl`) — among the models with at least `min_labels`
labelled rows; first on documents of the source's category, then on any document; a tie goes to the cheaper model per
admitted row. With no model qualifying, the policy's `default`. **Never by admitted rows or yield**: a row staging admits
can still lose its line's stance (testbed finding 6), so only a label ranks a model.

What the rotation can learn is bounded by the labels: it produces runs of different models on comparable documents; which
model is better is known only where someone labelled their rows. `Plan/runs/models.md` (`contracts.py`) is the table.

    python3 scripts/modelpick.py <Contract> <slug> <run>   # the choice and why, as JSON
    python3 scripts/modelpick.py selftest

`he_claude.py run --model auto` (its default) asks here and records the choice in the run's `usage.json`.
Standard library only.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
POLICY = ROOT / "Plan" / "hyperextract" / "models.json"


def policy(path: Path = POLICY) -> dict:
    p = json.loads(path.read_text(encoding="utf-8"))
    if p["default"] not in p["pool"] or not 0 <= p["explore"] <= 1:
        raise ValueError(f"{path}: the default must be in the pool and explore in [0, 1]")
    return p


def draws(contract: str, slug: str, run: str) -> tuple[float, float]:
    h = hashlib.sha256(f"{contract}|{slug}|{run}".encode()).digest()
    return int.from_bytes(h[:8], "big") / 2 ** 64, int.from_bytes(h[8:16], "big") / 2 ** 64


def standings(contract: str, category: str | None, stats: list[dict], min_labels: int) -> list[dict]:
    """The models that qualify for this contract, best first: in the category if any qualifies there, else anywhere."""
    for scope in ([category] if category else []) + [None]:
        agg: dict[str, dict] = {}
        for s in stats:
            if s["contract"] != contract or (scope is not None and s["category"] != scope):
                continue
            a = agg.setdefault(s["model"], {"model": s["model"], "labelled": 0, "ok": 0, "cost": 0.0, "admitted": 0})
            a["labelled"] += s["labelled"]
            a["ok"] += s["ok"]
            a["cost"] += s["cost_usd"]
            a["admitted"] += s["admitted"]
        ok = [dict(a, precision=a["ok"] / a["labelled"], scope=scope or "any",
                   per_row=a["cost"] / a["admitted"] if a["admitted"] else float("inf"))
              for a in agg.values() if a["labelled"] >= min_labels]
        if ok:
            return sorted(ok, key=lambda a: (-a["precision"], a["per_row"]))
    return []


def choose(contract: str, slug: str, run: str, category: str | None = None, stats: list[dict] | None = None,
           pol: dict | None = None) -> dict:
    pol = pol or policy()
    if stats is None:
        import contracts
        stats = contracts.model_stats()
    u, v = draws(contract, slug, run)
    if u < pol["explore"]:
        model = pol["pool"][int(v * len(pol["pool"]))]
        return {"model": model, "explored": True, "u": round(u, 4),
                "reason": f"explore: u {u:.3f} < {pol['explore']}, a model drawn from the pool"}
    ranked = [s for s in standings(contract, category, stats, pol["min_labels"]) if s["model"] in pol["pool"]]
    if ranked:
        best = ranked[0]
        return {"model": best["model"], "explored": False, "u": round(u, 4),
                "reason": f"exploit: {best['ok']} of {best['labelled']} labelled rows ok "
                          f"({best['precision']:.0%}) on {best['scope']} documents, the best of {len(ranked)} qualifying"}
    return {"model": pol["default"], "explored": False, "u": round(u, 4),
            "reason": f"exploit: no model has {pol['min_labels']} labelled rows for {contract}; the default"}


def selftest() -> int:
    cases = []
    pol = {"pool": ["haiku", "sonnet"], "default": "haiku", "explore": 0.2, "min_labels": 3}
    runs = [f"r{i}" for i in range(2000)]
    explored = [choose("C", "doc", r, None, [], pol)["explored"] for r in runs]
    share = sum(explored) / len(runs)
    cases.append((f"about a fifth of runs explore ({share:.3f})", 0.17 < share < 0.23))
    picks = {choose("C", "doc", r, None, [], pol)["model"] for r, e in zip(runs, explored) if e}
    cases.append(("exploring reaches every model in the pool", picks == {"haiku", "sonnet"}))
    cases.append(("one run's choice is the same every time",
                  choose("C", "doc", "r7", None, [], pol) == choose("C", "doc", "r7", None, [], pol)))
    exploit = next(r for r, e in zip(runs, explored) if not e)
    cases.append(("no labels: the default", choose("C", "doc", exploit, None, [], pol)["model"] == "haiku"))
    stats = [{"contract": "C", "category": "plot", "model": "haiku", "labelled": 10, "ok": 4, "cost_usd": 1, "admitted": 10},
             {"contract": "C", "category": "plot", "model": "sonnet", "labelled": 10, "ok": 8, "cost_usd": 2, "admitted": 10},
             {"contract": "C", "category": "theory", "model": "haiku", "labelled": 10, "ok": 9, "cost_usd": 1, "admitted": 10},
             {"contract": "C", "category": "theory", "model": "sonnet", "labelled": 2, "ok": 2, "cost_usd": 1, "admitted": 2}]
    cases.append(("the better-labelled model wins in its category",
                  choose("C", "doc", exploit, "plot", stats, pol)["model"] == "sonnet"))
    cases.append(("in another category, that category's labels decide",
                  choose("C", "doc", exploit, "theory", stats, pol)["model"] == "haiku"))
    got = choose("C", "doc", exploit, "physics", stats, pol)
    cases.append(("a category with no labels falls back to all documents", got["model"] == "sonnet"
                  and "any documents" in got["reason"]))
    rich = [dict(s, ok=s["labelled"], admitted=1000) for s in stats]
    cases.append(("yield never ranks: a model with many admitted rows and no labels does not qualify",
                  choose("C", "doc", exploit, None, [{"contract": "C", "category": "x", "model": "sonnet", "labelled": 0,
                                                       "ok": 0, "cost_usd": 0, "admitted": 9999}], pol)["model"] == "haiku"))
    cases.append(("a tie goes to the cheaper model per admitted row",
                  standings("C", "plot", [dict(s, ok=s["labelled"]) for s in rich[:2]], 3)[0]["model"] == "haiku"))
    try:
        policy_path = ROOT / "Plan" / "hyperextract" / "models.json"
        cases.append(("the committed policy loads", policy(policy_path)["explore"] == 0.2))
    except (OSError, ValueError, KeyError):
        cases.append(("the committed policy loads", False))
    failed = [n for n, ok in cases if not ok]
    for n, ok in cases:
        print(("held " if ok else "FAIL ") + n)
    print(f"modelpick: {len(cases) - len(failed)} of {len(cases)} cases hold")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    if len(argv) != 3:
        print(__doc__)
        return 2
    from subject import read_jsonl
    category = next((r.get("category") for r in read_jsonl(ROOT / "Sources" / "manifest.jsonl")
                     if r["slug"] == argv[1]), None)
    print(json.dumps(choose(argv[0], argv[1], argv[2], category), ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
