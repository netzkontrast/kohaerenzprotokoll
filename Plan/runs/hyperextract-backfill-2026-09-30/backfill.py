#!/usr/bin/env python3
"""The HyperExtract backfill: the contracts of the scaled pass over every document that has been read.

The author, 2026-09-30: „Use Haiku agents to Backpoet hyperextract for all allready Read sources“. A document is *read*
when it has a census in `Sources/terms/` (58 of the 586 landed). The three contracts that the graph laboratory measured
— `TermDefinitions`, `TermContrasts`, `CausalLinks`, whose lines the `he-lines` finder answers from — ran on twelve of them
(`Plan/runs/hyperextract-templates-2026-09-30/scaled.sh`); this runs them on the rest, Haiku through `claude -p`
(`he_claude.py`, decision 011), **one run at a time** — the author's „achte auf mein Nutzungslimit - starte diese nicht
parallel“ is a standing rule for model runs — each staged into `Plan/runs/<slug>/hyperextract/<contract>-haiku-2026-09-30/`
with its calls and its cost, so that the catalogue and `hegraph.py report` read it like the twelve.

    python3 Plan/runs/hyperextract-backfill-2026-09-30/backfill.py plan        # what would run, and the estimate
    python3 Plan/runs/hyperextract-backfill-2026-09-30/backfill.py run [--budget USD] [--limit N]
    python3 Plan/runs/hyperextract-backfill-2026-09-30/backfill.py status      # what is done, what it cost
    touch Plan/runs/hyperextract-backfill-2026-09-30/STOP                      # stop after the run in progress

**Resumable**: a (document, contract) whose `usage.json` exists is done and is skipped, so a stopped or killed pass
continues where it was. **Ordered by the gold**: the documents that hold the most lines of the conflict and question
records come first, because `he-lines` is worth what the contracts have read of them. **It stops by itself** after three
runs in a row that failed wholly (a usage limit or an outage answers every call with an error, and each failed call is
paid for), or when the budget is spent. A run that failed wholly is renamed `<name>-failed<n>` so that its name is free for
a retry; it stays on disk, because what failed is a finding.

Standard library only; every model call is `he_claude.py`'s, with its own record.
"""
from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "scripts"))

CONTRACTS = ("TermDefinitions", "TermContrasts", "CausalLinks")
APPROVAL = ("decision 011 (Claude, first party); the author's instruction of 2026-09-30 „Use Haiku agents to Backpoet "
            "hyperextract for all allready Read sources“")
RATE = 7.3            # dollars a megabyte a contract, from the 71 runs of the pilot and the scaled pass (§4.5 of the note)
LOG = HERE / "log.txt"
STOP = HERE / "STOP"
RUNTIME = 3600        # seconds one run may take; the largest document is 372 KB


def read_documents() -> list[str]:
    return sorted(p.stem for p in (ROOT / "Sources" / "terms").glob("*.md") if p.stem != "README")


def gold_lines() -> dict[str, int]:
    import ask
    lines = {(d, l) for c in ask.bench_cases() for d, l in c["gold"]}
    out: dict[str, int] = {}
    for d, _ in lines:
        out[d] = out.get(d, 0) + 1
    return out


def run_name(contract: str) -> str:
    return f"{contract.lower()}-haiku-2026-09-30"


def done(slug: str, contract: str) -> bool:
    return (ROOT / "Plan" / "runs" / slug / "hyperextract" / run_name(contract) / "usage.json").exists()


def size(slug: str) -> int:
    return (ROOT / "Sources" / "drive" / f"{slug}.md").stat().st_size


def plan() -> list[tuple[str, str]]:
    gold = gold_lines()
    docs = sorted(read_documents(), key=lambda s: (-gold.get(s, 0), size(s), s))
    return [(s, c) for s in docs for c in CONTRACTS if not done(s, c)]


def log(line: str) -> None:
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


def cmd_plan() -> int:
    todo = plan()
    docs = list(dict.fromkeys(s for s, _ in todo))
    mb = sum(size(s) for s in docs) / 1e6
    per = {c: sum(1 for _, x in todo if x == c) for c in CONTRACTS}
    print(f"{len(docs)} documents ({mb:.2f} MB) and {len(todo)} runs left: {per}")
    print(f"about ${mb * RATE * len(CONTRACTS):.0f} and {mb * 51 * len(CONTRACTS) / 60:.1f} hours "
          f"(${RATE} a megabyte a contract, 51 minutes a megabyte, from the scaled pass)")
    gold = gold_lines()
    print("first ten documents:", ", ".join(f"{s[:38]} ({gold.get(s, 0)} gold)" for s in docs[:10]))
    return 0


def totals() -> dict:
    t = {"runs": 0, "calls": 0, "failed_calls": 0, "seconds": 0.0, "cost": 0.0, "names": 0, "quote": 0, "refused": 0, "failed_runs": 0}
    for f in sorted((ROOT / "Plan" / "runs").glob("*/hyperextract/*-haiku-2026-09-30*/usage.json")):
        if f.parts[-2].split("-haiku")[0] not in {c.lower() for c in CONTRACTS}:
            continue
        u = json.loads(f.read_text(encoding="utf-8"))
        if "backfill" not in u.get("approval", "") and "Backpoet" not in u.get("approval", ""):
            continue
        t["runs"] += 1
        t["calls"] += u["calls"]
        t["failed_calls"] += u["failed_calls"]
        t["seconds"] += u["seconds"]
        t["cost"] += u["cost_usd"]
        t["failed_runs"] += bool(u.get("failed"))
        rep = f.with_name("report.json")
        if rep.exists():
            for r in json.loads(rep.read_text(encoding="utf-8"))["rows"]:
                if r["status"] == "candidate":
                    t["names"] += 1
                elif r.get("reason") == "surface absent from document" and r.get("quote_status") == "placed" and len(r.get("lines") or []) == 1:
                    t["quote"] += 1
                else:
                    t["refused"] += 1
    return t


def cmd_status() -> int:
    t = totals()
    todo = plan()
    print(f"done under the backfill's approval: {t['runs']} runs, {t['calls']} calls ({t['failed_calls']} failed), "
          f"{t['seconds'] / 60:.0f} min, ${t['cost']:.2f}; rows {t['names']} on names, {t['quote']} on the quotation, {t['refused']} refused; "
          f"{t['failed_runs']} runs failed wholly")
    print(f"left: {len(todo)} runs over {len(set(s for s, _ in todo))} documents")
    return 0


def cmd_run(budget: float, limit: int | None) -> int:
    todo = plan()
    if limit:
        todo = todo[:limit]
    log(f"== start {time.strftime('%Y-%m-%d %H:%M:%S')}  {len(todo)} runs planned, budget ${budget:.0f}")
    spent, streak = 0.0, 0
    for n, (slug, contract) in enumerate(todo, 1):
        if STOP.exists():
            log(f"== stopped by {STOP.name} after {n - 1} runs")
            break
        if spent >= budget:
            log(f"== budget ${budget:.0f} spent after {n - 1} runs")
            break
        name = run_name(contract)
        log(f"== [{n}/{len(todo)}] {slug} {contract} {time.strftime('%H:%M:%S')}")
        try:
            out = subprocess.run([sys.executable, str(ROOT / "scripts" / "he_claude.py"), "run", slug,
                                  str(ROOT / "Plan" / "hyperextract" / f"{contract}.yaml"), "--run", name, "--model", "haiku",
                                  "--approval", APPROVAL], cwd=ROOT, capture_output=True, text=True, timeout=RUNTIME)
            lines = [l for l in out.stdout.splitlines() if l.startswith('{"source_sha256') or l.startswith('{"document"')]
            for l in lines:
                log(l[:420])
            if out.returncode not in (0, 1) or not lines:
                log(f"   exit {out.returncode}: {(out.stderr or out.stdout)[-300:].strip()}")
        except subprocess.TimeoutExpired:
            log(f"   timed out after {RUNTIME} s")
        target = ROOT / "Plan" / "runs" / slug / "hyperextract" / name
        usage = json.loads((target / "usage.json").read_text(encoding="utf-8")) if (target / "usage.json").exists() else None
        if usage:
            spent += usage["cost_usd"]
        if usage is None or usage.get("failed"):
            streak += 1
            if target.exists():
                k = 1
                while target.with_name(f"{name}-failed{k}").exists():
                    k += 1
                target.rename(target.with_name(f"{name}-failed{k}"))
            log(f"   FAILED ({streak} in a row)")
            if streak >= 3:
                log("== stopped: three runs in a row failed wholly — a usage limit or an outage? nothing more is run")
                return 1
        else:
            streak = 0
    log(f"== end {time.strftime('%Y-%m-%d %H:%M:%S')}  spent ${spent:.2f}")
    return 0


def main(argv: list[str]) -> int:
    if not argv or argv[0] == "plan":
        return cmd_plan()
    if argv[0] == "status":
        return cmd_status()
    if argv[0] == "run":
        budget = float(argv[argv.index("--budget") + 1]) if "--budget" in argv else 90.0
        limit = int(argv[argv.index("--limit") + 1]) if "--limit" in argv else None
        return cmd_run(budget, limit)
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
