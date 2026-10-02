"""E4 arm C: a `dspy.RLM` agent over the chunk index answers a frozen case in `ask`'s JSON (`scripts/e4.py`).

Runs in `.venv-novelgraph`, where the index and the RLM tools are (`novelgraph.rlm.tools_for`, `heading@v1`, the
limits of PR #140: `ITERS` steps, `SUB_CALLS` sub-calls, `OUTPUT_CHARS` a step). The agent searches and reads; it
submits the answer JSON of `ask.SCHEMA` under `ask.RULES`, whose „Paket" here is what it read. **`shown` is only the
lines `read_chunk` returned to it** — a search preview is not reading, and a chunk cut at 4 000 characters showed only
the lines before the cut. Every call goes through `lmrun.call` into `<out>/lm/C.jsonl`, under `e4.capped`: a call
whose worst case could cross the case or the total allowance is not made.

Prints one JSON line: status, forced, the answer text, shown, cost, calls, estimates, refused_by, seconds.

    .venv-novelgraph/bin/python scripts/e4_rlm.py selftest      # offline: fixture index, fixture LM, deno sandbox
    (called by e4.py: e4_rlm.py case --case C1 --question … --out … --case-left 0.15 --total-left 19 --model … --approval …)
"""

from __future__ import annotations

import json
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

METHOD = "heading@v1"
LINE = re.compile(r"^(\d+)\| ", re.M)


def task(question: str) -> str:
    import ask
    return (f"# Frage\n\n{question}\n\nArt der Frage: `position`\n\n"
            "Das „Paket\" sind hier die Abschnitte, die du mit read_chunk gelesen hast; sonst nichts. "
            "search_chunks(query, mode) sucht (mode: 'hybrid', 'bm25' oder 'vec') und zeigt nur einen Anfang; "
            "read_chunk(ref) liest einen gefundenen Abschnitt, jede Zeile mit ihrer Nummer vor dem „|\" — das ist die "
            "`line_hint`. Suche mehrmals mit verschiedenen Begriffen, lies vor dem Zitieren. `doc` ist der Teil des "
            "ref vor dem Doppelpunkt.\n\n" + ask.RULES + "\n" + ask.SCHEMA +
            "\nGib die Antwort als JSON-Text in `answer` zurück. Rufe SUBMIT spätestens im vorletzten Schritt auf.")


def reading(read_chunk, shown_lines: dict):
    """`read_chunk`, recording the lines it actually returned."""
    def read(ref: str) -> str:
        """Read one chunk that search_chunks returned, each line prefixed with its file line number."""
        text = read_chunk(ref)
        if not text.startswith(("UNKNOWN", "STALE")):
            doc = str(ref).strip().removesuffix(".md").split(":", 1)[0]
            shown_lines.setdefault(doc, set()).update(int(n) for n in LINE.findall(text))
        return text
    read.__name__ = "read_chunk"
    return read


def one(question: str, out: Path, case_left: float, total_left: float, model: str, approval: str, *,
        ix=None, lm=None, interpreter_factory=None, case_id: str = "case") -> dict:
    import dspy
    import e4
    import lmrun
    from novelgraph import rlm, search
    ix = ix or search.Index(METHOD)
    shown: dict = {}
    shown_lines: dict[str, set[int]] = {}
    search_chunks, read_chunk = rlm.tools_for(ix, shown)
    tools = [search_chunks, reading(read_chunk, shown_lines)]
    kw = {"interpreter_factory": interpreter_factory} if interpreter_factory else {}
    program = dspy.RLM("question: str -> answer: str", tools=tools, max_iters=rlm.ITERS,
                       max_llm_calls=rlm.SUB_CALLS, max_output_chars=rlm.OUTPUT_CHARS, **kw)
    guard = e4.capped(lm or lmrun.make_lm(model), case_left, total_left)
    started = time.time()
    with dspy.context(lm=guard):
        pred, rec = lmrun.call(program, step="C", subject=case_id, out_dir=out / "lm", approval=approval,
                               question=task(question))
    status = rec["status"]
    if status == "unreachable" and e4.CAP_MARK in str(rec.get("error")):
        status = "capped"
    forced = pred is not None and getattr(pred, "final_reasoning", "") == rlm.FORCED
    return {"status": status, "forced": forced, "answer_text": getattr(pred, "answer", None) if pred is not None else None,
            "shown": {d: sorted(ns) for d, ns in shown_lines.items()}, "searched": len(shown),
            "cost": round(rec["cost"], 5), "calls": len(guard.estimates), "estimates": guard.estimates,
            "refused_by": guard.refused, "steps": len(getattr(pred, "trajectory", []) or []) if pred is not None else 0,
            "seconds": round(time.time() - started, 1), "error": rec.get("error")}


def stub() -> dict:
    """What e4.py's own selftest receives: the plumbing, no index and no model."""
    return {"status": "answered", "forced": False, "answer_text": json.dumps({
        "answerable": "no", "claims": [], "differ": [], "gaps": ["stub"], "need": [], "next": []}),
        "shown": {}, "searched": 0, "cost": 0.0, "calls": 0, "estimates": [], "refused_by": None, "steps": 0,
        "seconds": 0.0, "error": None}


def selftest() -> list[str]:
    """On novelgraph's fixture index and a scripted LM in the real sandbox: only read lines are shown, the answer
    JSON comes back, a call over the allowance is not made and the run is `capped`."""
    import tempfile
    from lm_fixture import FixtureLM, chat
    from novelgraph import build, search
    from novelgraph.selftest import QUIET, TEXTS, fixture
    fails = []

    class Costly(FixtureLM):
        def forward(self, *a, **k):
            r = super().forward(*a, **k)
            r._hidden_params = {"response_cost": 0.01}
            return r

    answer = json.dumps({"answerable": "partly", "claims": [], "differ": [], "gaps": [], "need": [], "next": []})
    code = ("import json\nhits = json.loads(search_chunks('Kael Sterne AEGIS Archiv'))\n"
            "print(read_chunk(hits[0]['ref']))")
    submit = f"SUBMIT(answer={answer!r})"
    with fixture(TEXTS), tempfile.TemporaryDirectory() as tmp:
        build.build(**QUIET)
        ix = search.Index(METHOD)
        lm = Costly([chat(reasoning="suchen und lesen", code=code), chat(reasoning="fertig", code=submit)])
        got = one("Was zählt Kael?", Path(tmp), 0.15, 19.0, "fixture", "fixture", ix=ix, lm=lm)
        if got["status"] != "answered" or json.loads(got["answer_text"] or "{}").get("answerable") != "partly":
            fails.append(f"the answer did not come back: {got['status']} {got.get('error')}")
        hits = json.loads(rlm_search(ix))
        first = hits[0]["ref"]
        doc, span = first.split(":L")
        lo, hi = (int(x) for x in span.split("-L"))
        if got["shown"] != {doc: list(range(lo, hi + 1))}:
            fails.append(f"shown is not exactly the read chunk's lines: {got['shown']} vs {doc}:{lo}-{hi}")
        if got["searched"] <= 1:
            fails.append("the search showed one chunk only; the test cannot tell reading from searching")
        if got["cost"] != 0.02 or got["calls"] != 2 or len((Path(tmp) / "lm" / "C.jsonl").read_text().splitlines()) != 1:
            fails.append(f"cost or record wrong: ${got['cost']} {got['calls']} calls")
        lm = Costly([chat(reasoning="x", code=code), "unused"])
        got = one("Was zählt Kael?", Path(tmp), 0.025, 19.0, "fixture", "fixture", ix=ix, lm=lm)
        if got["status"] != "capped" or got["refused_by"] != "case" or len(lm.requests) != 1 or got["cost"] != 0.01:
            fails.append(f"the case cap did not refuse the second call: {got['status']} {got['refused_by']} "
                         f"{len(lm.requests)} calls ${got['cost']}")
    return fails


def rlm_search(ix) -> str:
    from novelgraph import rlm
    return rlm.tools_for(ix, {})[0]("Kael Sterne AEGIS Archiv")


def main(argv: list[str]) -> int:
    import argparse
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("selftest")
    c = sub.add_parser("case")
    for name in ("--case", "--question", "--out", "--model", "--approval"):
        c.add_argument(name, required=True)
    c.add_argument("--case-left", type=float, required=True)
    c.add_argument("--total-left", type=float, required=True)
    c.add_argument("--fixture")
    a = ap.parse_args(argv)
    if a.cmd == "selftest":
        fails = selftest()
        for f in fails:
            print(f"  FAIL  {f}")
        print(f"e4_rlm: {'held' if not fails else f'{len(fails)} failed'} (answer back, shown = read lines, record, case cap)")
        return 1 if fails else 0
    if a.fixture == "stub":
        print(json.dumps(stub(), ensure_ascii=False))
        return 0
    if not a.model.startswith("claude-cli/"):
        raise SystemExit("decision 021 approves Claude only (claude-cli/…), not " + a.model)
    print(json.dumps(one(a.question, Path(a.out), a.case_left, a.total_left, a.model, a.approval, case_id=a.case),
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
