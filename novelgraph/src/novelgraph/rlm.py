"""`novelgraph rlm`: a `dspy.RLM` agent searches this index for the evidence a bench question asks for.

PR #76 asked whether an RLM — a model that works in a sandboxed REPL with tools instead of reading a
context — retrieves what a fixed search misses. Its trial ran over the wiki graph and never finished
(`scripts/rlm_retrieval.py`). This runs the same agent over the chunk index, and uses it for the
question the index leaves open: **which chunk size helps a reader find the evidence.** The static
bench ranks chunks; an agent has to read them, and a chunk that ranks well but holds half a thought
costs it a read. So the agent's success under each chunker is the measurement that chooses one.

- **Tools** (`tools_for`): `search_chunks(query, mode)` returns up to eight chunks of one method as
  `ref` (`slug:Lstart-Lend`), heading path and the first 200 characters; `read_chunk(ref)` returns a
  chunk the agent has already been shown, its lines numbered, at most 4 000 characters. A ref it was
  not shown is refused, so the agent cannot guess an address.
- **Output**: `evidence: list[str]`, refs, most important first. Code validates them (`evaluate`): a ref
  the agent was never shown is invalid; the rest are taken in order **until 3 200 tokens of chunk text**
  — the same text budget for every chunker, or a large chunk would win by its size alone.
- **Score**: per case, the share of the record's gold lines (`ask.bench_cases()`, unchanged) that lie in
  the accepted chunks, and the share of its gold documents. A forced answer (`max_iters` ran out and DSPy
  extracted one from the trajectory) is recorded and **not scored** (`scripts/rlm_ingest.py`'s rule).
- **Resume and spend**: every row carries `run_fp` (`run_fingerprint`); a results file holding rows of another
  fingerprint is refused, not resumed. The cost cap is checked between runs, so one invocation can pass it.
- **Model**: Claude through `claude -p`, `lmrun.make_lm("claude-cli/haiku")`, every call through
  `lmrun.call` with `approval=` — decision 011: chunk text may reach Claude and no other model. One run at
  a time (the author, 2026-09-30). Each call is recorded under `Plan/runs/<run>/lm/`, each case under
  `Plan/runs/<run>/results.jsonl`; a case already in it is skipped, so a run resumes.

    .venv-novelgraph/bin/novelgraph rlm --selftest                    # tools, refusal, budget, scoring; offline
    .venv-novelgraph/bin/novelgraph rlm --dry-run --cases C10         # the DSPy loop on a fixture LM
    .venv-novelgraph/bin/novelgraph rlm --approval "decision 011" --methods heading@v1 --cases C1,C2
    .venv-novelgraph/bin/novelgraph rlm --report                      # the table, from results.jsonl

Needs the `rlm` extra: `UV_PROJECT_ENVIRONMENT=$PWD/.venv-novelgraph uv sync --project novelgraph --extra rlm`.
"""

from __future__ import annotations

import json
import re
import statistics
import time
from pathlib import Path

import numpy  # noqa: F401  before dspy: DSPy's lazy importer breaks NumPy if it loads first
from . import build, search, store  # noqa: E402
from .repo import ROOT, bench_cases, read_jsonl  # noqa: E402

RUN = ROOT / "Plan" / "runs" / "rlm-chunks-2026-10-01"
METHODS = ("heading200@v1", "heading@v1", "heading800@v1")
BUDGET = 3200          # tokens of chunk text accepted as evidence, the same for every chunker
MAX_REFS = 16
ITERS, SUB_CALLS = 6, 2
OUTPUT_CHARS = 3000      # what one step shows the model; the pilot spent ~85 % of its tokens re-reading steps
REF = re.compile(r"^\s*([a-z0-9-]+)(?:\.md)?:L(\d+)-L?(\d+)\s*$")
FORCED = "Extract forced final output"
TASK = ("\n\nFinde mit den Werkzeugen die Stellen in den Quellen, die diese Frage belegen. "
        "search_chunks(query, mode) sucht (mode: 'hybrid', 'bm25' oder 'vec'); read_chunk(ref) liest einen "
        "gefundenen Abschnitt. Suche mehrmals mit verschiedenen Begriffen, lies vor dem Belegen. "
        "Gib als evidence die refs (Form slug:Lstart-Lend) der belegenden Abschnitte zurück, die wichtigsten "
        f"zuerst — gewertet werden die ersten etwa {BUDGET} Tokens Text. Nur refs, die eine Suche geliefert hat. "
        f"Rufe SUBMIT spätestens im Schritt {ITERS - 1} von {ITERS} auf.")


def ref_of(hit: dict) -> str:
    return f"{hit['slug']}:L{hit['line_start']}-L{hit['line_end']}"


def tools_for(ix: search.Index, shown: dict):
    """The agent's two tools over one method's index. `shown` collects every chunk a search returned."""

    def search_chunks(query: str, mode: str = "hybrid") -> str:
        """Search the source corpus. Returns up to 8 chunks as JSON: ref, heading path, first 200 characters."""
        if mode not in search.MODES:
            return f"UNKNOWN MODE — use one of {', '.join(search.MODES)}"
        if not str(query).strip():
            return "[]"
        out = []
        for h in ix.search(str(query), 8, mode):
            c = search._chunk(h["slug"], ix.method, h["id"])
            lines = store.read_text_lines(build._path(h["slug"]))
            ref = ref_of(h)
            shown[ref] = {**c, "slug": h["slug"]}
            out.append({"ref": ref, "heading": " › ".join(c["heading_path"]),
                        "preview": " ".join(build.chunk_text(lines, c).split())[:200]})
        return json.dumps(out, ensure_ascii=False)

    def read_chunk(ref: str) -> str:
        """Read one chunk that search_chunks returned, each line prefixed with its file line number."""
        c = shown.get(str(ref).strip().removesuffix(".md"))
        if c is None:
            return "UNKNOWN REF — read only refs that search_chunks returned"
        lines = store.read_text_lines(build._path(c["slug"]))
        text = "\n".join(f"{n}| {lines[n - 1]}" for n in range(c["line_start"], c["line_end"] + 1))
        return text if len(text) <= 4000 else text[:4000] + "\n… (gekürzt)"

    return [search_chunks, read_chunk]


def evaluate(evidence, shown: dict, gold: set[tuple[str, int]], budget: int = BUDGET) -> dict:
    """Shown refs only, deduplicated, in the agent's order, until `budget` tokens; the rest is visible."""
    if not isinstance(evidence, list):
        evidence = [evidence] if evidence else []
    accepted, invalid, over, tokens = [], [], [], 0
    for raw in evidence[:MAX_REFS * 2]:
        ref = str(raw).strip().removesuffix(".md")
        m = REF.match(ref)
        key = f"{m.group(1)}:L{m.group(2)}-L{m.group(3)}" if m else ref
        if key not in shown:
            invalid.append(str(raw))
            continue
        if key in accepted:
            continue
        if tokens + shown[key]["tokens"] > budget or len(accepted) >= MAX_REFS:
            over.append(key)
            continue
        accepted.append(key)
        tokens += shown[key]["tokens"]
    covered = {(shown[k]["slug"], n) for k in accepted
               for n in range(shown[k]["line_start"], shown[k]["line_end"] + 1)}
    docs = {d for d, _ in gold}
    return {"accepted": accepted, "invalid": invalid, "over_budget": over, "tokens": tokens,
            "line_recall": round(len(gold & covered) / len(gold), 3) if gold else None,
            "doc_recall": round(len(docs & {shown[k]["slug"] for k in accepted}) / len(docs), 3) if docs else None,
            "lines": len(covered)}


def cases(only: list[str] | None = None) -> list[dict]:
    out = [c for c in bench_cases() if c["gold"]]
    return [c for c in out if c["id"] in only] if only else out


def program(tools, interpreter_factory=None):
    import dspy
    kw = {"interpreter_factory": interpreter_factory} if interpreter_factory else {}
    return dspy.RLM("question: str -> evidence: list[str]", tools=tools, max_iters=ITERS,
                    max_llm_calls=SUB_CALLS, max_output_chars=OUTPUT_CHARS, **kw)


def run_fingerprint(methods, model: str, dry_run: bool) -> str:
    """What a row of a run depends on besides its case: this module's code, the model, every limit, and the
    `_build/` stamp of each method's index. A resume continues only rows made under the same fingerprint."""
    import hashlib
    parts = {"code": hashlib.sha1(Path(__file__).read_bytes()).hexdigest(), "model": "fixture" if dry_run else model,
             "limits": [ITERS, SUB_CALLS, OUTPUT_CHARS, BUDGET, MAX_REFS], "task": TASK,
             "index": {m: build.build_stamp(m, store.default_embedder())[0] for m in methods}}
    return hashlib.sha1(json.dumps(parts, sort_keys=True).encode()).hexdigest()[:12]


def run(methods, only, model: str, approval: str | None, dry_run: bool, log=print,
        cost_cap: float = 15.0) -> list[dict]:
    import dspy
    import lmrun
    if not dry_run and not approval:
        raise SystemExit("a real run sends chunk text to the model: name the decision that allows it "
                         "(--approval \"decision 011\"; Claude only)")
    if not dry_run and not model.startswith("claude-cli/"):
        raise SystemExit("decision 011 lets chunk text reach Claude only (claude-cli/…), not " + model)
    RUN.mkdir(parents=True, exist_ok=True)
    out_path = RUN / ("results-dry.jsonl" if dry_run else "results.jsonl")
    fp = run_fingerprint(methods, model, dry_run)
    previous = read_jsonl(out_path) if out_path.exists() else []
    foreign = {r.get("run_fp") for r in previous} - {fp}
    if foreign:
        # a resume skips what is done; done under other code, limits, model or index it is not this run's (PR #139)
        raise SystemExit(f"{out_path} holds rows of another run ({sorted(map(str, foreign))[:2]}); "
                         "start a new run directory instead of resuming it")
    done = {(r["case"], r["method"]) for r in previous}
    rows = []
    spent = sum(r["cost"] for r in read_jsonl(out_path)) if out_path.exists() else 0.0
    indexes = {m: search.Index(m) for m in methods}
    # case by case, every method in turn: a run that stops early still leaves complete pairs
    for case in cases(only):
        for method in methods:
            ix = indexes[method]
            if (case["id"], method) in done:
                continue
            if spent > cost_cap:
                log(f"stopped: ${spent:.2f} recorded, over the cap of ${cost_cap:.2f}")
                return rows
            shown: dict = {}
            tools = tools_for(ix, shown)
            if dry_run:
                from lm_fixture import FixtureLM, chat, offline
                first = ix.search(case["question"], 1, "hybrid")
                ref = ref_of(first[0]) if first else "none:L1-L1"
                code = f"r = search_chunks({case['question']!r})\nSUBMIT(evidence=[{ref!r}, 'erfunden:L1-L2'])"
                lm = FixtureLM(lambda _: chat(reasoning="Offline fixture.", code=code))
                ctx = offline(lm)
            else:
                lm = lmrun.make_lm(model)
                ctx = dspy.context(lm=lm)
            started = time.time()
            with ctx:
                pred, rec = lmrun.call(program(tools), step=method.replace("@", "-"), subject=RUN.name,
                                       approval=approval or "fixture", question=case["question"] + TASK)
            forced = getattr(pred, "final_reasoning", "") == FORCED if pred is not None else False
            score = evaluate(getattr(pred, "evidence", []) if pred is not None else [], shown, case["gold"])
            row = {"case": case["id"], "method": method, "run_fp": fp, "model": "fixture" if dry_run else model,
                   "status": rec["status"], "forced": forced,
                   "scored": rec["status"] == "answered" and not forced and not dry_run,
                   **score, "shown": len(shown), "steps": len(getattr(pred, "trajectory", []) or []),
                   "calls": len(lm.history) if not dry_run else len(getattr(lm, "requests", [])),
                   "cost": rec["cost"], "seconds": round(time.time() - started, 1)}
            if not row["scored"]:
                row["line_recall_unscored"], row["line_recall"] = row["line_recall"], None
                row["doc_recall_unscored"], row["doc_recall"] = row["doc_recall"], None
            with out_path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(row, ensure_ascii=False) + "\n")
            rows.append(row)
            spent += row["cost"]
            log(f"{case['id']:4} {method:14} {row['status']:9} forced={forced!s:5} line {row['line_recall']} "
                f"doc {row['doc_recall']} shown {row['shown']} refs {len(row['accepted'])} "
                f"${row['cost']:.4f} {row['seconds']}s")
    return rows


def report(path: Path | None = None) -> dict:
    """Per method: scored cases, mean line and document recall, forced and failed runs, cost; and the
    paired comparison against heading@v1 on the cases both scored."""
    rows = read_jsonl(path or RUN / "results.jsonl")
    from .repo import documents
    landed = {d.slug for d in documents()}
    by = {}
    for r in rows:
        by.setdefault(r["method"], []).append(r)
    out = {}
    base = {r["case"]: r for r in by.get("heading@v1", []) if r["scored"]}
    for m, rs in by.items():
        sc = [r for r in rs if r["scored"]]
        paired = [(r["line_recall"] - base[r["case"]]["line_recall"]) for r in sc if r["case"] in base]
        out[m] = {"cases": len(rs), "scored": len(sc), "forced": sum(r["forced"] for r in rs),
                  "failed": sum(r["status"] != "answered" for r in rs),
                  "line_recall": round(statistics.mean(r["line_recall"] for r in sc), 3) if sc else None,
                  "doc_recall": round(statistics.mean(r["doc_recall"] for r in sc), 3) if sc else None,
                  "refs": round(statistics.mean(len(r["accepted"]) for r in sc), 1) if sc else None,
                  "tokens": round(statistics.mean(r["tokens"] for r in sc)) if sc else None,
                  "invalid_refs": sum(len(r["invalid"]) for r in rs),
                  # an invalid ref naming no landed document was invented, not merely unshown
                  "invented_refs": sum(1 for r in rs for x in r["invalid"]
                                       if (REF.match(str(x).strip().removesuffix(".md")) or [None, None])[1] not in landed),
                  "cost": round(sum(r["cost"] for r in rs), 4),
                  "seconds": round(sum(r["seconds"] for r in rs)),
                  "vs_heading": {"pairs": len(paired),
                                 "mean_diff": round(statistics.mean(paired), 3) if paired else None,
                                 "better": sum(d > 0 for d in paired), "worse": sum(d < 0 for d in paired)}}
    return out


def selftest() -> list[str]:
    """The tools, the refusal of an unshown ref, the budget, the scoring — on a temporary two-source index
    with the deterministic stand-in embedder of `selftest.fixture`, so it needs no corpus build and no model."""
    from .selftest import QUIET, TEXTS, fixture
    with fixture(TEXTS):
        build.build(**QUIET)
        return _selftest(search.Index("heading@v1"))


def _selftest(ix) -> list[str]:
    fails = []
    shown: dict = {}
    search_chunks, read_chunk = tools_for(ix, shown)
    hits = json.loads(search_chunks("Kael Sterne AEGIS Archiv"))
    if not hits or not all(REF.match(h["ref"]) for h in hits):
        fails.append(f"search_chunks returned no well-formed refs: {hits[:2]}")
        return fails
    if not read_chunk(hits[0]["ref"]).split("\n", 1)[0].startswith(f"{hits[0]['ref'].split(':L')[1].split('-')[0]}|"):
        fails.append("read_chunk does not number lines from the chunk's first file line")
    if not read_chunk("erfunden:L1-L9").startswith("UNKNOWN REF"):
        fails.append("read_chunk read a ref no search had shown")
    if not search_chunks("x", mode="semantic").startswith("UNKNOWN MODE"):
        fails.append("search_chunks accepted an unknown mode")
    h = shown[hits[0]["ref"]]
    gold = {(h["slug"], h["line_start"]), (h["slug"], h["line_end"]), ("anderes-dokument", 3)}
    got = evaluate([hits[0]["ref"], hits[0]["ref"] + ".md", "erfunden:L1-L2"], shown, gold)
    if got["accepted"] != [hits[0]["ref"]] or got["invalid"] != ["erfunden:L1-L2"]:
        fails.append(f"evaluate: duplicates or unshown refs leaked: {got}")
    if got["line_recall"] != round(2 / 3, 3) or got["doc_recall"] != 0.5:
        fails.append(f"evaluate scored {got['line_recall']}/{got['doc_recall']}, expected 0.667/0.5")
    tight = evaluate([r["ref"] for r in hits], shown, gold, budget=shown[hits[0]["ref"]]["tokens"])
    if tight["accepted"] != [hits[0]["ref"]] or not tight["over_budget"]:
        fails.append(f"the token budget did not stop the evidence: {tight}")
    if evaluate("keine Liste", shown, gold)["accepted"]:
        fails.append("a non-list answer was accepted as evidence")
    return fails
