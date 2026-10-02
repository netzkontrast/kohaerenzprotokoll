"""Three readings of the rlm-chunks run, offline, from its own files: no model call, no index.

Written after the run, on the inspection in PR #139 (`Plan/concept/pr140-architecture-input_2026-10-01.md`).
The pre-stated result stays the primary one; the other two are sensitivity views beside it.

1. **pre-stated** — accepted refs (shown by a search, within the budget), forced runs not scored;
2. **read** — only the accepted refs the agent also passed to `read_chunk` in code it ran. A ref accepted from a
   search's 200-character preview is evidence the agent *selected*, not evidence it *saw*. The read calls are
   recovered from the `[[ ## code ## ]]` sections of each recorded call (`lm/*.jsonl`): what the sandbox executed,
   not what the model said it did (it once wrote a whole tool output itself);
3. **incomplete as nothing** — every case scored; a forced or failed run delivered no evidence (0).

Paired differences against `heading@v1` with a 90 % bootstrap interval (10 000 resamples, seed 7).

    python3 Plan/runs/rlm-chunks-2026-10-01/analysis.py            # prints, writes analysis.json
"""

from __future__ import annotations

import json
import random
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import ask  # noqa: E402  the bench cases, unchanged

METHODS = ("heading200@v1", "heading@v1", "heading800@v1")
CODE = re.compile(r"\[\[ ## code ## \]\](.*?)(?=\[\[ ## |\Z)", re.S)
READ = re.compile(r"read_chunk\(\s*[\"']([^\"']+)[\"']")
REF = re.compile(r"^([a-z0-9-]+):L(\d+)-L(\d+)$")


def reads() -> dict[tuple[str, str], set[str]]:
    by_question = {c["question"]: c["id"] for c in ask.bench_cases()}
    out = {}
    for m in METHODS:
        for line in (HERE / "lm" / f"{m.replace('@', '-')}.jsonl").read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            case = by_question[r["inputs"]["question"].split("\n\nFinde")[0]]
            code = " ".join("".join(CODE.findall(x or "")) for x in r["raw"])
            out[(case, m)] = {x.strip().removesuffix(".md") for x in READ.findall(code)}
    return out


def recall(refs: list[str], gold: set) -> tuple[float, float]:
    covered = set()
    for ref in refs:
        slug, a, b = REF.match(ref).groups()
        covered |= {(slug, n) for n in range(int(a), int(b) + 1)}
    docs = {d for d, _ in gold}
    return len(gold & covered) / len(gold), len(docs & {s for s, _ in covered}) / len(docs)


def interval(diffs: list[float]) -> list[float]:
    rnd = random.Random(7)
    means = sorted(sum(rnd.choice(diffs) for _ in diffs) / len(diffs) for _ in range(10_000))
    return [round(means[500], 3), round(means[9500], 3)]


def main() -> dict:
    gold = {c["id"]: c["gold"] for c in ask.bench_cases() if c["gold"]}
    rows = {(r["case"], r["method"]): r for r in map(json.loads, (HERE / "results.jsonl").read_text().splitlines())}
    read = reads()
    views = {
        "pre-stated": lambda r: recall(r["accepted"], gold[r["case"]]) if r["scored"] else None,
        "read": lambda r: (recall([a for a in r["accepted"] if a in read[(r["case"], r["method"])]], gold[r["case"]])
                           if r["scored"] else None),
        "incomplete as nothing": lambda r: recall(r["accepted"], gold[r["case"]]) if r["scored"] else (0.0, 0.0),
    }
    out = {"accepted_refs": sum(len(r["accepted"]) for r in rows.values()),
           "accepted_and_read": sum(1 for r in rows.values() for a in r["accepted"] if a in read[(r["case"], r["method"])]),
           "views": {}}
    for name, fn in views.items():
        score = {k: fn(r) for k, r in rows.items()}
        v = {}
        for m in METHODS:
            got = [score[(c, m)] for c in gold if score[(c, m)] is not None]
            v[m] = {"cases": len(got), "line": round(sum(x[0] for x in got) / len(got), 3),
                    "doc": round(sum(x[1] for x in got) / len(got), 3)}
            if m != "heading@v1":
                pairs = [score[(c, m)][0] - score[(c, "heading@v1")][0] for c in gold
                         if score[(c, m)] is not None and score[(c, "heading@v1")] is not None]
                v[m]["paired_line_diff"] = round(sum(pairs) / len(pairs), 3)
                v[m]["interval_90"] = interval(pairs)
                v[m]["pairs"], v[m]["better"], v[m]["worse"] = len(pairs), sum(d > 0 for d in pairs), sum(d < 0 for d in pairs)
        out["views"][name] = v
    (HERE / "analysis.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return out


if __name__ == "__main__":
    result = main()
    print(f"accepted refs {result['accepted_refs']}, of them read via read_chunk {result['accepted_and_read']}")
    for name, v in result["views"].items():
        print(f"\n{name}")
        for m, s in v.items():
            extra = (f"  Δ {s['paired_line_diff']:+.3f} {s['interval_90']} pairs {s['pairs']} "
                     f"+{s['better']}/-{s['worse']}") if "pairs" in s else ""
            print(f"  {m:14} n {s['cases']:2} line {s['line']:.3f} doc {s['doc']:.3f}{extra}")
