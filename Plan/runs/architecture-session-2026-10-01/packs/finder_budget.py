"""The co-mention finder's share of the pack: the frozen cases packed with it at 10 paragraphs (default), 3, and off.

`finder_yield.py` found co-mention the costliest finder per gold line. This builds the real pack (`ask.build_pack`,
60 000 characters, its own record removed from the graph) under the three settings and reports gold lines sent,
gold documents sent and the characters of the whole pack, paired per case. Offline, no model.

    .venv-graphqlite/bin/python Plan/runs/architecture-session-2026-10-01/packs/finder_budget.py
"""
import json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
import ask, askdb, graph as kg, graphrag  # noqa: E401,E402

SETTINGS = {"co-mention 10 (default)": (ask.DEFAULT_FINDERS, 10), "co-mention 3": (ask.DEFAULT_FINDERS, 3),
            "co-mention off": (tuple(f for f in ask.DEFAULT_FINDERS if f != "co-mention"), 10)}
frozen = json.loads((ROOT / "Plan" / "eval" / "retrieval-cases-v1.json").read_text(encoding="utf-8"))
s, g = askdb.Store(), kg.build()
out = {k: [] for k in SETTINGS}
for c in frozen["cases"]:
    gold = {tuple(x) for x in c["gold"]}
    iso = graphrag.without(g, c["key"])
    for name, (finders, cm) in SETTINGS.items():
        text, meta = ask.build_pack(c["question"], "position", ask.BUDGET, s, iso, finders=finders, comention=cm)
        sent = {(d, n) for d, ns in meta["shown"].items() for n in ns}
        out[name].append({"id": c["id"], "line": len(gold & sent) / len(gold),
                          "doc": len({d for d, _ in gold} & set(meta["shown"])) / len({d for d, _ in gold}),
                          "gold_lines": len(gold & sent), "chars": meta["chars"], "docs": len(meta["shown"])})
    print(c["id"], *(f"{k.split()[1]}:{out[k][-1]['gold_lines']}/{out[k][-1]['chars']}" for k in SETTINGS), flush=True)
base = out["co-mention 10 (default)"]
summary = {}
for k, rows in out.items():
    summary[k] = {"line": round(sum(r["line"] for r in rows) / len(rows), 4), "doc": round(sum(r["doc"] for r in rows) / len(rows), 3),
                  "gold_lines": sum(r["gold_lines"] for r in rows), "chars": round(sum(r["chars"] for r in rows) / len(rows)),
                  "docs": round(sum(r["docs"] for r in rows) / len(rows), 1),
                  "worse_cases": sum(r["gold_lines"] < b["gold_lines"] for r, b in zip(rows, base)),
                  "better_cases": sum(r["gold_lines"] > b["gold_lines"] for r, b in zip(rows, base))}
(HERE / "finder_budget.json").write_text(json.dumps({"summary": summary, "rows": out, "frozen_sha256": frozen["sha256"]},
                                                    ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for k, v in summary.items():
    print(f"{k:24} line {v['line']:.4f} doc {v['doc']:.3f} gold lines {v['gold_lines']:4} chars {v['chars']:6} docs {v['docs']:5} "
          f"better {v['better_cases']} worse {v['worse_cases']}")
