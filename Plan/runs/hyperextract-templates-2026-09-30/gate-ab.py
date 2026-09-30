#!/usr/bin/env python3
"""Does the cue gate lose what an ungated run finds? Reads what `gate-ab.sh` staged and writes `gate-ab.md`.

For each document, the lines on which a run admitted a row (the quotation placed on one line, on names or on the
quotation alone — `hegraph.staged`'s two footings) are compared across three runs of `CausalLinks`: the first ungated
run of the scaled pass (U1), a second ungated run (U2) and a gated run (G). A model's repeat differs from itself, so the
question is not whether G equals U1 but whether G differs from U1 more than U2 does. Standard library only.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
HERE = Path(__file__).resolve().parent
AB = HERE / "gate-ab"


def lines_of(report: Path) -> tuple[set[int], int]:
    """The lines a run admitted a row on, and how many rows that was."""
    rows = json.loads(report.read_text(encoding="utf-8"))["rows"]
    kept = [r for r in rows if r.get("quote_status") == "placed" and len(r.get("lines") or []) == 1
            and (r["status"] == "candidate" or (r["status"] == "refused" and r.get("reason") == "surface absent from document"))]
    return {r["lines"][0] for r in kept}, len(kept)


def usage(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    import ask
    gold: dict[str, set[int]] = {}
    for c in ask.bench_cases():
        for d, line in c["gold"]:
            gold.setdefault(d, set()).add(line)
    docs = sorted(p.name for p in AB.iterdir() if p.is_dir())
    out = ["# The cue gate against the ungated run — `CausalLinks`, three German documents", "",
           "U1 is the first ungated run of the scaled pass, U2 a second ungated run, G a gated run (`he_claude.py run --gate`). "
           "A cell is a count of lines on which a run admitted a row. *Recall* is the share of U1's lines a run also finds; "
           "*of its own*, the share of a run's lines that U1 also has. U2 is what a repeat does to itself; G is the gate.", "",
           "| document | run | rows | lines | recall of U1's lines | of its own lines in U1 | gold lines (of those in U1) | calls | cost | share of the text sent |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    pooled = {"U1": [0, 0, 0, 0.0], "U2": [0, 0, 0, 0.0], "G": [0, 0, 0, 0.0]}     # rows, lines, calls, cost
    hits = {"U2": [0, 0, 0], "G": [0, 0, 0]}                                          # lines also in U1, own lines, U1's lines
    gold_in = {"U1": 0, "U2": 0, "G": 0, "U1∪U2": 0, "U1∪G": 0}
    sent = [0, 0]
    for doc in docs:
        u1, n1 = lines_of(ROOT / "Plan/runs" / doc / "hyperextract/causallinks-haiku-2026-09-30/report.json")
        runs = {"U1": (u1, n1, usage(ROOT / "Plan/runs" / doc / "hyperextract/causallinks-haiku-2026-09-30/usage.json")),
                "U2": (*lines_of(AB / doc / "repeat/report.json"), usage(AB / doc / "repeat/usage.json")),
                "G": (*lines_of(AB / doc / "gated/report.json"), usage(AB / doc / "gated/usage.json"))}
        g = gold.get(doc, set())
        for name, (lines, n, u) in runs.items():
            found = len(lines & u1)
            share = ""
            if "gate" in u:
                share = f"{u['gate']['characters_sent'] / u['gate']['characters_in_document']:.0%}"
                sent[0] += u["gate"]["characters_sent"]
                sent[1] += u["gate"]["characters_in_document"]
            out.append(f"| `{doc[:48]}` | {name} | {n} | {len(lines)} | "
                       f"{'—' if name == 'U1' else f'{found / len(u1):.0%} ({found})'} | "
                       f"{'—' if name == 'U1' else f'{found / len(lines):.0%}' if lines else '—'} | "
                       f"{len(lines & g)} ({len(lines & g & u1)}) | {u['calls']} | ${u['cost_usd']:.2f} | {share} |")
            p = pooled[name]
            p[0] += n; p[1] += len(lines); p[2] += u["calls"]; p[3] += u["cost_usd"]
            gold_in[name] += len(lines & g)
            if name != "U1":
                hits[name][0] += found; hits[name][1] += len(lines); hits[name][2] += len(u1)
        gold_in["U1∪U2"] += len((runs["U1"][0] | runs["U2"][0]) & g)
        gold_in["U1∪G"] += len((runs["U1"][0] | runs["G"][0]) & g)
    out += ["", "## Pooled over the three documents", "",
            "| run | rows | lines | recall of U1's lines | of its own lines in U1 | gold lines | calls | cost |", "|---|---|---|---|---|---|---|---|"]
    for name, (rows, lines, calls, cost) in pooled.items():
        if name == "U1":
            out.append(f"| U1 | {rows} | {lines} | — | — | {gold_in['U1']} | {calls} | ${cost:.2f} |")
        else:
            h = hits[name]
            out.append(f"| {name} | {rows} | {lines} | {h[0] / h[2]:.0%} | {h[0] / lines:.0%} | {gold_in[name]} | {calls} | ${cost:.2f} |")
    out += ["", f"The gate sent {sent[0]:,} of {sent[1]:,} characters ({sent[0] / max(sent[1], 1):.0%}). Gold lines found by U1 and U2 together: "
            f"{gold_in['U1∪U2']}; by U1 and G together: {gold_in['U1∪G']}; U1 alone: {gold_in['U1']}."]
    (HERE / "gate-ab.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
