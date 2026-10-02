"""Small RLM retrieval experiment for graph questions without lexical seeds.

The case node is removed before building tools: its edges encode the gold pages.
The model proposes page IDs; code validates them and reports recall, never
turning an RLM answer into wiki prose or an inferred graph edge.

    .venv-dspy/bin/python scripts/rlm_retrieval.py --dry-run
    .venv-dspy/bin/python scripts/rlm_retrieval.py --approval "decision 011"     # Claude Haiku through claude -p

**Claude only** (2026-10-01). The tools hand the model wiki titles and verified quotations, and decision 011 lets
a quotation reach Claude and no other model; the first trial (2026-09-25) sent them to an OpenRouter model under
a consent given for that run alone. The LM is built by `lmrun.make_lm`, cache off; anything but `claude-cli/…`
is refused. Every case goes through `lmrun.call` (subject `rlm-retrieval`, step the case): its approval and cache
checks, one record per call under `Plan/runs/rlm-retrieval/lm/` with raw outputs, trajectory, status and cost — a
dry run records into a temporary directory. A call that is `unreachable` or `unparsed` is recorded and not scored. The same agent over the chunk index is `novelgraph rlm` (`novelgraph/src/novelgraph/rlm.py`).
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import graph as kg  # noqa: E402
import graphrag  # noqa: E402

CASES = ("conflict:C10", "question:Q2")


def tools_for(graph: dict):
    """Read-only, bounded tools; neither returns a question's gold edges."""
    pages = {key: value for key, value in graph["nodes"].items() if value["type"] == "term"}

    def search_pages(words: str) -> str:
        """Search page names and verified quotations; return up to eight page IDs."""
        if not words.strip():
            return "[]"
        query = graphrag.vector(words)
        ranked = []
        for key, node in pages.items():
            quotes = [e for e in graph["evidence"].get(key.split(":", 1)[1], [])
                      if e["status"] == "verified"]
            title = " ".join([node["term"], *node.get("surfaces", [])])
            score = max([graphrag.cosine(query, graphrag.vector(title))] +
                        [graphrag.cosine(query, graphrag.vector(e["quote"])) for e in quotes])
            if score > 0:
                ranked.append((score, key, node["term"]))
        ranked.sort(key=lambda item: (-item[0], item[1]))
        return json.dumps([{"page": key, "title": title, "score": round(score, 3)}
                           for score, key, title in ranked[:8]], ensure_ascii=False)

    def inspect_page(page_id: str) -> str:
        """Show the first six verified quotations, with source and line."""
        if page_id not in pages:
            return "UNKNOWN PAGE"
        quotes = [e for e in graph["evidence"].get(page_id.split(":", 1)[1], [])
                  if e["status"] == "verified"]
        return json.dumps([{"quote": e["quote"], "source": e["doc"], "line": e["line"]}
                           for e in quotes[:6]], ensure_ascii=False)

    def search_quotes(page_id: str, words: str) -> str:
        """Find verified quotations anywhere on a page; return at most eight cited hits."""
        if page_id not in pages:
            return "UNKNOWN PAGE"
        if not words.strip():
            return "[]"
        query = graphrag.vector(words)
        ranked = []
        for e in graph["evidence"].get(page_id.split(":", 1)[1], []):
            if e["status"] != "verified":
                continue
            score = graphrag.cosine(query, graphrag.vector(e["quote"]))
            if score > 0:
                ranked.append((score, e))
        ranked.sort(key=lambda row: (-row[0], row[1]["doc"], row[1]["line"]))
        return json.dumps([{"quote": e["quote"], "source": e["doc"], "line": e["line"]}
                           for _, e in ranked[:8]], ensure_ascii=False)

    def list_pages(offset: int = 0) -> str:
        """Browse page IDs and titles in pages of 100, for questions without search terms."""
        offset = max(0, min(int(offset), len(pages)))
        return json.dumps([{"page": key, "title": pages[key]["term"]}
                           for key in sorted(pages)[offset:offset + 100]], ensure_ascii=False)

    return [search_pages, inspect_page, search_quotes, list_pages]


def evaluate(proposed, graph: dict, gold: set[str]) -> dict:
    """Unknown IDs are visible failures; duplicates cannot inflate recall."""
    if not isinstance(proposed, list):
        proposed = []
    valid = list(dict.fromkeys(p for p in proposed if isinstance(p, str) and
                               graph["nodes"].get(p, {}).get("type") == "term"))[:8]
    invalid = [p for p in proposed if p not in valid]
    return {"pages": valid, "invalid": invalid, "hits": sorted(set(valid) & gold),
            "recall": round(len(set(valid) & gold) / len(gold), 3) if gold else None}


def selftest() -> int:
    graph = kg.build()
    cases = {case["id"]: case for case in graphrag.cases(graph)}
    for case_id in CASES:
        isolated = graphrag.without(graph, case_id)
        assert case_id not in isolated["nodes"]
        search, inspect, search_quotes, listing = tools_for(isolated)
        assert "term:kael" in listing(0) + listing(100)
        assert "term:kael" in search("Kael")
        assert "UNKNOWN PAGE" == inspect("term:invented")
        assert all(row["source"] and row["line"] for row in json.loads(inspect("term:kael")))
        if case_id == "conflict:C10":
            assert not any("Knöchel" in row["quote"] for row in json.loads(inspect("term:kael")))
            later = json.loads(search_quotes("term:kael", "Knöchel"))
            assert later and any("Knöchel" in row["quote"] for row in later)
            assert all(row["source"] and row["line"] for row in later)
        else:
            assert all(page in listing(0) + listing(100) for page in cases[case_id]["gold"])
        result = evaluate(["term:invented", *sorted(cases[case_id]["gold"]),
                           *sorted(cases[case_id]["gold"])], isolated, cases[case_id]["gold"])
        assert result["invalid"] and len(result["pages"]) == len(cases[case_id]["gold"])
        assert result["recall"] == 1.0
    print("rlm_retrieval: 2 of 2 cases hold (isolation, tools, citations, output validation)")
    return 0


def run(dry_run: bool, model: str | None, approval: str | None, out_dir: Path | None = None,
        fixture_code: str = "SUBMIT(page_ids=['term:kael', 'term:invented'])") -> list[dict]:
    import tempfile

    import dspy
    import lmrun
    from lm_fixture import FixtureLM, chat, offline

    if not dry_run and not approval:
        raise SystemExit("a real run sends quotations to the model: name the decision (--approval \"decision 011\")")
    if not dry_run and not model.startswith("claude-cli/"):
        raise SystemExit("decision 011 lets quotations reach Claude only (claude-cli/…), not " + model)
    if dry_run and out_dir is None:
        out_dir = Path(tempfile.mkdtemp(prefix="rlm-retrieval-"))   # a fixture's record is not a run's
    graph = kg.build()
    cases = {case["id"]: case for case in graphrag.cases(graph)}
    results = []
    for case_id in CASES:
        case = cases[case_id]
        isolated = graphrag.without(graph, case_id)
        assert case_id not in isolated["nodes"]
        tools = tools_for(isolated)
        baseline = graphrag.retrieve(case["query"], isolated)
        if dry_run:
            # Proves parsing, validation, case isolation and the record; fixture accuracy is meaningless.
            from dspy.primitives.code_interpreter import FinalOutput

            class FixtureInterpreter:
                def __init__(self):
                    self.tools = {}
                    self.output_fields = {}

                def start(self):
                    pass

                def shutdown(self):
                    pass

                def execute(self, code, variables=None):
                    if code != fixture_code:
                        raise AssertionError(f"unexpected fixture code {code!r}")
                    return FinalOutput({"page_ids": ["term:kael", "term:invented"]})

            lm = FixtureLM(lambda _: chat(reasoning="Offline fixture.", code=fixture_code) if fixture_code
                           else "keine Felder")
            context = offline(lm)
            interpreter_factory = FixtureInterpreter
        else:
            lm = lmrun.make_lm(model)
            context = dspy.context(lm=lm)
            interpreter_factory = dspy.PythonInterpreter
        rlm = dspy.RLM("question: str -> page_ids: list[str]", tools=tools,
                       max_iters=5, max_llm_calls=8, interpreter_factory=interpreter_factory)
        with context:
            pred, rec = lmrun.call(rlm, step=case_id.replace(":", "-"), subject="rlm-retrieval",
                                   approval=approval or "fixture", out_dir=out_dir,
                                   question=case["query"] + "\nFind existing page IDs using the tools. "
                                   "If the first quotations on a page do not address the question, use "
                                   "search_quotes on that page. Submit at most eight IDs; if none fit, submit [].")
        result = evaluate(getattr(pred, "page_ids", []) if pred is not None else [], isolated, case["gold"])
        result["steps"] = len(getattr(pred, "trajectory", []) or [])
        result["model_requests"] = len(lm.requests) if dry_run else len(lm.history)
        result["forced"] = getattr(pred, "final_reasoning", "") == "Extract forced final output"
        result["call_status"], result["cost"] = rec["status"], rec["cost"]
        if rec["status"] != "answered":
            result["status"] = f"unscored — {rec['status']}"
            result["recall"] = None
        elif dry_run:
            result["status"] = "fixture — no accuracy measured"
            result["recall"] = None
        elif result["forced"]:
            result["status"] = "unscored — forced extraction"
            result["recall"] = None
        result.update({"case": case_id, "baseline_recall": round(
            len({p["id"] for p in baseline["terms"]} & case["gold"]) / len(case["gold"]), 3)})
        results.append(result)
    return results


def record_selftest() -> int:
    """An answered and a failed fixture run each leave one record per case, and the failed one is not scored."""
    import tempfile
    fails = []
    for code, status in (("SUBMIT(page_ids=['term:kael', 'term:invented'])", "answered"), ("", "unparsed")):
        with tempfile.TemporaryDirectory() as tmp:
            got = run(True, None, None, out_dir=Path(tmp), fixture_code=code)
            for r in got:
                ledger = Path(tmp) / f"{r['case'].replace(':', '-')}.jsonl"
                rows = [json.loads(x) for x in ledger.read_text().splitlines()] if ledger.exists() else []
                if len(rows) != 1 or rows[0]["status"] != status or r["call_status"] != status:
                    fails.append(f"{status} {r['case']}: {len(rows)} records, {[x['status'] for x in rows]}")
                if status != "answered" and (r["recall"] is not None or r["pages"]):
                    fails.append(f"a {status} run was scored: {r}")
    for f in fails:
        print(f"  FAIL  {f}")
    print(f"rlm_retrieval records: {'held' if not fails else f'{len(fails)} failed'} (answered and failed runs recorded)")
    return 1 if fails else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--record-selftest", action="store_true")
    parser.add_argument("--model", default="claude-cli/haiku")
    parser.add_argument("--approval")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    if args.record_selftest:
        return record_selftest()
    print(json.dumps(run(args.dry_run, args.model, args.approval), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
