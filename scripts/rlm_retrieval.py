"""Small RLM retrieval experiment for graph questions without lexical seeds.

The case node is removed before building tools: its edges encode the gold pages.
The model proposes page IDs; code validates them and reports recall, never
turning an RLM answer into wiki prose or an inferred graph edge.

    .venv-dspy/bin/python scripts/rlm_retrieval.py --dry-run
    .venv-dspy/bin/python scripts/rlm_retrieval.py --model openrouter/... --approval "..."
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
        """Show a page's verified quotations with source and line, at most six."""
        if page_id not in pages:
            return "UNKNOWN PAGE"
        quotes = [e for e in graph["evidence"].get(page_id.split(":", 1)[1], [])
                  if e["status"] == "verified"]
        return json.dumps([{"quote": e["quote"], "source": e["doc"], "line": e["line"]}
                           for e in quotes[:6]], ensure_ascii=False)

    def list_pages(offset: int = 0) -> str:
        """Browse page IDs and titles in pages of 100, for questions without search terms."""
        offset = max(0, min(int(offset), len(pages)))
        return json.dumps([{"page": key, "title": pages[key]["term"]}
                           for key in sorted(pages)[offset:offset + 100]], ensure_ascii=False)

    return [search_pages, inspect_page, list_pages]


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
        search, inspect, listing = tools_for(isolated)
        assert "term:kael" in listing(0) + listing(100)
        assert "term:kael" in search("Kael")
        assert "UNKNOWN PAGE" == inspect("term:invented")
        assert all(row["source"] and row["line"] for row in json.loads(inspect("term:kael")))
        result = evaluate(["term:invented", *sorted(cases[case_id]["gold"]),
                           *sorted(cases[case_id]["gold"])], isolated, cases[case_id]["gold"])
        assert result["invalid"] and len(result["pages"]) == len(cases[case_id]["gold"])
        assert result["recall"] == 1.0
    print("rlm_retrieval: 2 of 2 cases hold (isolation, tools, citations, output validation)")
    return 0


def run(dry_run: bool, model: str | None, approval: str | None) -> list[dict]:
    import dspy
    from lm_fixture import FixtureLM, chat, offline

    if not dry_run and (not model or not approval):
        raise SystemExit("a real run needs --model and --approval for these two questions")
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
            # Proves parsing, validation and case isolation; fixture accuracy is meaningless.
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
                    if code != "SUBMIT(page_ids=['term:kael', 'term:invented'])":
                        raise AssertionError(f"unexpected fixture code {code!r}")
                    return FinalOutput({"page_ids": ["term:kael", "term:invented"]})

            lm = FixtureLM(lambda _: chat(reasoning="Offline fixture.",
                                          code="SUBMIT(page_ids=['term:kael', 'term:invented'])"))
            context = offline(lm)
            interpreter_factory = FixtureInterpreter
        else:
            from rlm_ingest import BASE, api_key
            lm = dspy.LM(model, api_key=api_key(), api_base=BASE, cache=False)
            context = dspy.context(lm=lm)
            interpreter_factory = dspy.PythonInterpreter
        rlm = dspy.RLM("question: str -> page_ids: list[str]", tools=tools,
                       max_iters=5, max_llm_calls=8, interpreter_factory=interpreter_factory)
        with context:
            pred = rlm(question=case["query"] + "\nFind existing page IDs using the tools. "
                       "Inspect evidence. Submit at most eight IDs; if none fit, submit [].")
        result = evaluate(pred.page_ids, isolated, case["gold"])
        result["steps"] = len(getattr(pred, "trajectory", []) or [])
        result["model_requests"] = len(lm.requests) if dry_run else len(lm.history)
        result["forced"] = getattr(pred, "final_reasoning", "") == "Extract forced final output"
        if dry_run:
            result["status"] = "fixture — no accuracy measured"
            result["recall"] = None
        elif result["forced"]:
            result["status"] = "unscored — forced extraction"
            result["recall"] = None
        result.update({"case": case_id, "baseline_recall": round(
            len({p["id"] for p in baseline["terms"]} & case["gold"]) / len(case["gold"]), 3)})
        results.append(result)
    return results


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--model")
    parser.add_argument("--approval")
    args = parser.parse_args()
    if args.selftest:
        return selftest()
    print(json.dumps(run(args.dry_run, args.model, args.approval), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
