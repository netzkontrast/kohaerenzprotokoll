#!/usr/bin/env python3
"""What the three contracts cost and found, per pass and per contract: the earlier runs and the backfill.

Reads `Plan/runs/<document>/hyperextract/<contract>-haiku-2026-09-30/{usage,report}.json`. A run belongs to the backfill when
its `usage.json` names the author's instruction of 2026-09-30 („Use Haiku agents to Backpoet hyperextract…“) as its approval;
every other run of these three contracts is an earlier one — the scaled pass's 36 on twelve documents and the pilot's 3 on two
others. A run that failed wholly (`…-failed<n>`) is counted apart, because
its calls were paid for and found nothing.

    python3 Plan/runs/hyperextract-backfill-2026-09-30/stats.py            # one table per pass, and the two together
    python3 Plan/runs/hyperextract-backfill-2026-09-30/stats.py --documents   # one line per document

Standard library only. Every number is a count over the files; nothing here is an estimate except the line that says so.
"""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CONTRACTS = ["TermDefinitions", "TermContrasts", "CausalLinks"]
FIELDS = ("runs", "calls", "failed_calls", "seconds", "cost_usd", "input_tokens", "output_tokens", "input_rows", "candidates",
          "quote", "refused")


def pass_of(usage: dict) -> str:
    return "backfill" if "Backpoet" in usage.get("approval", "") else "earlier"


def footing(row: dict) -> str:
    """`names`: admitted on the names; `quote`: refused on the names but placed on one line by its quotation; else `refused`."""
    if row["status"] == "candidate":
        return "names"
    if (row.get("reason") == "surface absent from document" and row.get("quote_status") == "placed"
            and len(row.get("lines") or []) == 1):
        return "quote"
    return "refused"


def collect() -> tuple[dict, dict, dict]:
    by_pass: dict = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
    by_doc: dict = defaultdict(lambda: defaultdict(float))
    failed: dict = defaultdict(lambda: defaultdict(float))
    for f in sorted((ROOT / "Plan" / "runs").glob("*/hyperextract/*-haiku-2026-09-30*/usage.json")):
        run = f.parent.name
        contract = next((c for c in CONTRACTS if run.startswith(c.lower() + "-haiku-2026-09-30")), None)
        if contract is None:
            continue
        doc = f.parts[-4]
        u = json.loads(f.read_text(encoding="utf-8"))
        if "-failed" in run or u.get("failed"):
            for k in ("calls", "failed_calls", "seconds", "cost_usd"):
                failed[pass_of(u)][k] += u[k]
            failed[pass_of(u)]["runs"] += 1
            continue
        t = by_pass[pass_of(u)][contract]
        t["runs"] += 1
        for k in ("calls", "failed_calls", "seconds", "cost_usd", "input_tokens", "output_tokens"):
            t[k] += u[k]
        rep = f.with_name("report.json")
        if rep.exists():
            r = json.loads(rep.read_text(encoding="utf-8"))
            t["input_rows"] += r["input_rows"]
            for row in r["rows"]:
                k = footing(row)
                t["candidates" if k == "names" else k] += 1
        d = by_doc[(pass_of(u), doc)]
        d["runs"] += 1
        d["calls"] += u["calls"]
        d["seconds"] += u["seconds"]
        d["cost_usd"] += u["cost_usd"]
        d["size"] = (ROOT / "Sources" / "drive" / f"{doc}.md").stat().st_size
    return by_pass, by_doc, failed


def line(label: str, t: dict) -> str:
    return (f"{label:18} {int(t['runs']):>4} {int(t['calls']):>6} {int(t['failed_calls']):>6} {t['seconds'] / 60:>7.0f} "
            f"{t['cost_usd']:>8.2f} {int(t['input_rows']):>8} {int(t['candidates']):>6} {int(t['quote']):>6} {int(t['refused']):>8}")


def main(argv: list[str]) -> int:
    by_pass, by_doc, failed = collect()
    head = (f"{'':18} {'runs':>4} {'calls':>6} {'failed':>6} {'min':>7} {'cost $':>8} {'rows in':>8} {'names':>6} "
            f"{'quote':>6} {'refused':>8}")
    total = defaultdict(lambda: defaultdict(float))
    for name in ("earlier", "backfill"):
        if name not in by_pass:
            continue
        print(f"\n== {name}\n{head}")
        acc: dict = defaultdict(float)
        for c in CONTRACTS:
            t = by_pass[name].get(c)
            if not t:
                continue
            print(line(c, t))
            for k, v in t.items():
                acc[k] += v
                total[c][k] += v
        print(line("all three", acc))
        if name in failed:
            f = failed[name]
            print(f"   and {int(f['runs'])} runs that failed wholly: {int(f['calls'])} calls, ${f['cost_usd']:.2f}, {f['seconds'] / 60:.0f} min")
    if len(by_pass) > 1:
        print(f"\n== both passes\n{head}")
        acc = defaultdict(float)
        for c in CONTRACTS:
            print(line(c, total[c]))
            for k, v in total[c].items():
                acc[k] += v
        print(line("all three", acc))
        mb_contracts = sum(d["runs"] * d["size"] for d in by_doc.values()) / 1e6             # a run is one document under one contract
        print(f"\n{len(set(doc for _, doc in by_doc))} documents; ${acc['cost_usd'] / max(mb_contracts, 1e-9):.2f} a megabyte a contract "
              f"over the runs done (the note's estimate was $7.3)")
    if "--documents" in argv:
        print("\n== per document (backfill)")
        for (p, doc), d in sorted(by_doc.items(), key=lambda kv: -kv[1]["cost_usd"]):
            if p == "backfill":
                print(f"{doc[:62]:62} {int(d['runs'])} runs  {d['size'] / 1e3:>6.0f} KB  ${d['cost_usd']:.2f}  {d['seconds'] / 60:.0f} min")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
