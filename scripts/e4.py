"""E4: fixed pack, bounded expansion, RLM — which controller reaches more *read* gold evidence at equal cost.

The design, written before any call, is `Plan/runs/e4-controllers/README.md` (SPEC.md §9 step 8, decision 021):
three arms answer the same frozen case in the same JSON (`ask.SCHEMA`), every answer is checked by the same
`ask.verify(answer, shown)`, and `shown` is exactly the lines that arm put in the model's context.

- **A — fixed pack**: `ask.build_pack` (default finders, 72 000 bytes, the case's own record out of the graph); one call.
- **B — bounded expansion**: the pack; when the answer's `need` names a term (`Store.bm25`) or a line range
  (`Store.window`) whose lines were not shown, code appends at most `EXPAND_BYTES` of them and asks again; at most
  `EXTRA_ROUNDS` extra rounds. The last parsed answer stands; a later round that fails or is capped leaves it.
- **C — RLM over chunks**: `scripts/e4_rlm.py` in `.venv-novelgraph` (the chunk index lives there): `novelgraph rlm`'s
  tools and limits, the same answer JSON; `shown` is only the lines `read_chunk` returned.

**Metric**: read gold = quotes `ask.verify` placed, on lines that arm showed, that are gold — in two views, `all`
gold and `unquoted` gold (lines no term or chapter page cites, `unquoted_lines`). Invented evidence (`unresolved`,
`outside-pack`) is counted and listed, never scored. A run that is not `answered`, or is forced, scores 0 in the
primary view; the complete-case view stands beside it.

**Cost** (`CapReached`, `Capped`): before every call the arm's spend on the case plus that call's estimated worst case
(`worst`) is checked against `CASE_CAP`, and everything E4 recorded plus that call against `TOTAL`. A call that could
cross is not made: the case ends with what it has (`capped`), and the whole experiment stops at the total.
The estimate is a stated assumption — `BYTES_PER_TOKEN` bytes a token, cache-write price for every input token,
`OUT_TOKENS` output tokens — and every row keeps estimate beside actual cost, so the pilot can show it is wrong.

**Resume**: a run lives in `Plan/runs/e4-controllers/<run>/`; every row carries `run_fp` (code, model, limits, frozen
cases, the store's input hash, the chunk index's stamp). Rows of another fingerprint refuse the run.

    .venv-dspy/bin/python scripts/e4.py selftest                   # offline: fixture LM, every path, caps, stop, rule
    .venv-dspy/bin/python scripts/e4.py run --run pilot --cases C1,Q2 --approval "decision 021"
    .venv-dspy/bin/python scripts/e4.py analyse --run main          # analysis.json, the decision rule line by line
"""

from __future__ import annotations

import hashlib
import json
import random
import re
import statistics
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

E4 = ROOT / "Plan" / "runs" / "e4-controllers"
ARMS = ("A", "B", "C")
MODEL = "claude-cli/haiku"
KIND = "position"
CASE_CAP = 0.15          # dollars per case and arm (README: equal cost)
TOTAL = 20.0             # dollars for the whole experiment, pilot included (decision 021)
EXPAND_BYTES = 8_000     # B: at most this many bytes appended per round
EXTRA_ROUNDS = 2         # B: at most this many rounds after the first
NEED_HITS = 12           # B: lines a `term` need fetches through the pack's own lexical finder
NEED_SPAN = 40           # B: at most this many lines of one requested range
# the worst-case estimate of one call — assumptions, replaced by what the pilot measures (Haiku 4.5 list prices)
BYTES_PER_TOKEN = 2.5    # German text runs nearer 3.5; 2.5 errs high
IN_PRICE = 1.25e-6       # dollars per input token at the cache-write price, the highest input rate
OUT_PRICE = 5e-6         # dollars per output token
OUT_TOKENS = 4_000       # an answer of the schema has run to ~1 500 tokens
CAP_MARK = "E4-CAP"
NOVELGRAPH_PY = ROOT / ".venv-novelgraph" / "bin" / "python"
SEED, RESAMPLES = 7, 10_000
APPEND = ("\n\n## Nachgereicht auf deine Anfrage (`need`)\n\nDiese Zeilen gehören jetzt zum Paket. Antworte erneut, "
          "vollständig, im Schema oben; eine Behauptung darf sich auf das ganze Paket stützen.\n")


# ── cost ──────────────────────────────────────────────────────────────────────

def worst(text_bytes: int) -> float:
    """The estimated worst-case dollars of one call whose prompt is `text_bytes` long."""
    return text_bytes / BYTES_PER_TOKEN * IN_PRICE + OUT_TOKENS * OUT_PRICE


def recorded_total(root: Path = E4) -> float:
    """Everything E4 has spent: every model call recorded under any of its runs, pilot included."""
    total = 0.0
    for p in root.glob("*/lm/*.jsonl"):
        for line in p.read_text(encoding="utf-8").splitlines():
            if line.strip():
                total += float(json.loads(line).get("cost") or 0)
    return total


def _dspy():
    import dspy
    return dspy


def capped(inner, case_left: float, total_left: float):
    """`inner` wrapped so that no call is made whose worst case could cross either allowance.

    A refused call raises `CapReached` — a `dspy.LMRateLimitError`, so `lmrun.call` records the run (`unreachable`,
    its error marked `E4-CAP`) with the cost of every call made before it, instead of losing it."""
    dspy = _dspy()

    class CapReached(dspy.LMRateLimitError):
        pass

    class Capped(dspy.BaseLM):
        forward_contract = "legacy"

        def __init__(self):
            super().__init__(model=inner.model, cache=False)
            self.spent, self.estimates, self.refused = 0.0, [], None

        def forward(self, prompt=None, messages=None, **kwargs):
            messages = messages or [{"role": "user", "content": prompt or ""}]
            est = worst(sum(len(str(m.get("content") or "").encode("utf-8")) for m in messages))
            for name, left in (("case", case_left), ("total", total_left)):
                if self.spent + est > left:
                    self.refused = name
                    raise CapReached(f"{CAP_MARK} {name}: ${self.spent:.4f} spent + ${est:.4f} worst case "
                                     f"> ${left:.4f} left", model=inner.model, provider="e4")
            response = inner.forward(prompt=prompt, messages=messages, **kwargs)
            cost = float((getattr(response, "_hidden_params", None) or {}).get("response_cost") or 0)
            self.spent += cost
            self.estimates.append([round(est, 5), round(cost, 5)])
            return response

    return Capped()


# ── the gold views ────────────────────────────────────────────────────────────

CITE = re.compile(r"\^\[([a-z0-9-]+)\.md:L(\d+)")


def unquoted_lines(cases: list[dict]) -> dict[str, set[tuple[str, int]]]:
    """Per case, its gold lines that no term or chapter page cites (`evaluation-audit_2026-09-30.md` counted
    the complement: 1 130 of 1 226 gold lines are such citations)."""
    quoted = set()
    for folder in ("candidates", "chapters"):
        for p in (ROOT / "Wiki" / folder).glob("*.md"):
            quoted |= {(m.group(1), int(m.group(2))) for m in CITE.finditer(p.read_text(encoding="utf-8"))}
    return {c["id"]: {g for g in c["gold"] if g not in quoted} for c in cases}


# ── one model call ────────────────────────────────────────────────────────────

def ask_once(lm, text: str, *, step: str, case: str, out_dir: Path, approval: str, packs: Path) -> dict:
    """One call with `text` as the whole prompt, through `lmrun.call`. The prompt is written to `packs/` and the
    record names its sha256, so a 72 KB pack is kept once, not inside every record."""
    import ask
    import lmrun
    dspy = _dspy()
    sha = hashlib.sha256(text.encode("utf-8")).hexdigest()
    packs.mkdir(parents=True, exist_ok=True)
    (packs / f"{sha[:16]}.md").write_text(text, encoding="utf-8")

    class Raw(dspy.Module):
        def forward(self, case, prompt_sha):
            out = dspy.settings.lm(messages=[{"role": "user", "content": text}])
            first = out[0] if out else ""
            return dspy.Prediction(text=first.get("text", "") if isinstance(first, dict) else str(first))

    with dspy.context(lm=lm):
        pred, rec = lmrun.call(Raw(), step=step, subject=case, out_dir=out_dir, approval=approval,
                               case=case, prompt_sha=sha)
    status = rec["status"]
    if status == "unreachable" and CAP_MARK in str(rec.get("error")):
        status = "capped"
    answer = ask.parse(pred.text) if pred is not None and status == "answered" else None
    if status == "answered" and answer is None:
        status = "unparsed"
    return {"status": status, "answer": answer, "cost": rec["cost"], "seconds": rec["seconds"],
            "prompt_sha": sha, "error": rec.get("error")}


# ── the arms ──────────────────────────────────────────────────────────────────

def _lines(shown: dict) -> set[tuple[str, int]]:
    return {(d, n) for d, ns in shown.items() for n in ns}


def fetch(need: list, shown: dict, store, budget: int = EXPAND_BYTES) -> tuple[str, dict]:
    """B's expansion: what `need` asks for that was not shown, as pack-formatted blocks within `budget` bytes."""
    import pack
    rows: list[tuple[str, int, str]] = []
    for item in (need or [])[:3]:
        if not isinstance(item, dict):
            continue
        if item.get("term"):
            rows += [(r["slug"], r["line"], r["text"]) for r in store.bm25(str(item["term"]), limit=NEED_HITS)]
        elif item.get("doc") and isinstance(item.get("lines"), list) and len(item["lines"]) == 2:
            try:
                a, b = sorted(int(x) for x in item["lines"])
            except (TypeError, ValueError):
                continue
            doc = str(item["doc"]).removesuffix(".md")
            rows += [(doc, n, t) for n, t in store.window(doc, a, min(b, a + NEED_SPAN - 1))]
    seen, new = _lines(shown), []
    for r in rows:
        if (r[0], r[1]) not in seen:
            seen.add((r[0], r[1]))
            new.append(r)
    kept, _, _ = pack.fit(new, budget, lambda r: pack.size(f"L{r[1]}: {r[2]}\n") + 8)
    added: dict[str, list[int]] = {}
    blocks: dict[str, list[str]] = {}
    for doc, n, t in sorted(kept):
        added.setdefault(doc, []).append(n)
        blocks.setdefault(doc, []).append(f"L{n}: {t}")
    text = "".join(f"\n### `{d}` — nachgereicht\n\n" + "\n".join(b) + "\n" for d, b in blocks.items())
    return text, added


def arm_pack(case: dict, ctx: dict, expand: bool) -> dict:
    """A (`expand` False) or B. `ctx` carries the pack builder, the store, the LM factory and the allowances."""
    pack_text, meta = ctx["pack"](case)
    shown = {d: list(v) for d, v in meta["shown"].items()}
    lm = capped(ctx["lm"](), ctx["case_left"], ctx["total_left"])
    arm = "B" if expand else "A"
    text, best, calls, rounds, statuses, extra = pack_text, None, [], 0, [], ""
    while True:
        got = ask_once(lm, text, step=arm, case=case["id"], out_dir=ctx["out"] / "lm", approval=ctx["approval"],
                       packs=ctx["out"] / "packs")
        calls.append(got)
        statuses.append(got["status"])
        if got["status"] == "answered":
            best = got
        if not expand or got["status"] != "answered" or rounds >= EXTRA_ROUNDS:
            break
        more, added = fetch(got["answer"].get("need") or [], shown, ctx["store"])
        if not added:
            break
        rounds += 1
        for d, ns in added.items():
            shown.setdefault(d, []).extend(ns)
        extra += more
        text = pack_text + APPEND + extra
    return {"status": best["status"] if best else statuses[-1], "answer": best["answer"] if best else None,
            "forced": False, "shown": shown, "rounds": rounds, "calls": len(lm.estimates), "statuses": statuses,
            "cost": round(sum(c["cost"] for c in calls), 5), "estimates": lm.estimates, "refused_by": lm.refused,
            "seconds": round(sum(c["seconds"] for c in calls), 1), "pack_status": meta["status"],
            "prompts": [c["prompt_sha"][:16] for c in calls]}


def arm_rlm(case: dict, ctx: dict) -> dict:
    """C, in `.venv-novelgraph` — its index and RLM tools live there. One subprocess per case."""
    args = [str(ctx.get("novelgraph_py", NOVELGRAPH_PY)), str(ROOT / "scripts" / "e4_rlm.py"), "case",
            "--case", case["id"], "--question", case["question"], "--out", str(ctx["out"]),
            "--case-left", str(ctx["case_left"]), "--total-left", str(ctx["total_left"]),
            "--model", ctx["model"], "--approval", ctx["approval"]] + (["--fixture", ctx["fixture"]] if ctx.get("fixture") else [])
    p = subprocess.run(args, capture_output=True, text=True, timeout=3600)
    try:
        got = json.loads(p.stdout.strip().splitlines()[-1])
    except (IndexError, json.JSONDecodeError):
        return {"status": "unreachable", "answer": None, "forced": False, "shown": {}, "rounds": 0, "calls": 0,
                "statuses": ["unreachable"], "cost": 0.0, "estimates": [], "refused_by": None, "seconds": 0.0,
                "error": (p.stderr or p.stdout)[-600:]}
    import ask
    answer = got.pop("answer_text", None)
    parsed = ask.parse(answer) if isinstance(answer, str) else (answer if isinstance(answer, dict) else None)
    if got["status"] == "answered" and parsed is None:
        got["status"] = "unparsed"
    return got | {"answer": parsed, "rounds": 0, "statuses": [got["status"]]}


# ── scoring ───────────────────────────────────────────────────────────────────

def score(res: dict, gold: set, unquoted: set) -> dict:
    """Read gold in both views, invented evidence, and whether the row scores (answered, not forced)."""
    import ask
    v = ask.verify(res["answer"], res["shown"]) if res["answer"] is not None else {"status": "unparsed"}
    if v["status"] == "schema-invalid":
        res["status"] = "schema-invalid"
    quotes = [(row["doc"], q) for row in v.get("claims", []) + v.get("unsupported", []) for q in row["quotes"]]
    placed = {(d, q["line"]) for d, q in quotes if q["status"] == "placed"}
    invented = [{"doc": d, "text": q["text"][:200], "status": q["status"]} for d, q in quotes
                if q["status"] in ("unresolved", "outside-pack")]
    scored = res["status"] == "answered" and not res["forced"]
    rg, ru = placed & gold, placed & unquoted
    recall = lambda hit, g: round(len(hit) / len(g), 4) if g else None  # noqa: E731
    return {"scored": scored, "placed": sorted(map(list, placed)), "invented": invented,
            "outside_window": sum(1 for _, q in quotes if q["status"] == "outside-window"),
            "read_gold": sorted(map(list, rg)), "gold": len(gold), "unquoted_gold": len(unquoted),
            "recall_all": recall(rg, gold) if scored else 0.0 if gold else None,
            "recall_unquoted": (recall(ru, unquoted) if scored else 0.0) if unquoted else None,
            "complete_all": recall(rg, gold) if scored else None,
            "shown_lines": len(_lines(res["shown"]))}


# ── a run ─────────────────────────────────────────────────────────────────────

def fingerprint(case_list: list[dict], model: str, fixture: str | None = None) -> str:
    import askdb
    import benchset
    code = b"".join((ROOT / "scripts" / f).read_bytes() for f in
                    ("e4.py", "e4_rlm.py", "ask.py", "pack.py", "askdb.py", "lmrun.py", "claude_lm.py", "claude_cli.py"))
    code += b"".join(p.read_bytes() for p in sorted((ROOT / "novelgraph" / "src" / "novelgraph").glob("*.py")))
    stamp = ROOT / "Index" / "_build"
    parts = {"code": hashlib.sha1(code).hexdigest(), "model": fixture and "fixture" or model,
             "limits": [CASE_CAP, TOTAL, EXPAND_BYTES, EXTRA_ROUNDS, NEED_HITS, NEED_SPAN, BYTES_PER_TOKEN, IN_PRICE,
                        OUT_PRICE, OUT_TOKENS],
             "cases": benchset.identity()["cases_sha256"], "asked": sorted(c["id"] for c in case_list),
             "store": askdb.stats().get("input_hash"),
             "index": sorted(p.name for p in stamp.glob("heading@v1*")) if stamp.exists() else None}
    return hashlib.sha1(json.dumps(parts, sort_keys=True, default=str).encode()).hexdigest()[:12]


def read_rows(path: Path) -> list[dict]:
    return [json.loads(x) for x in path.read_text(encoding="utf-8").splitlines() if x.strip()] if path.exists() else []


class Stop(Exception):
    """The whole experiment's budget is spent."""


def run(run_name: str, only: list[str] | None, approval: str | None, *, model: str = MODEL, log=print,
        ctx_over: dict | None = None, root: Path = E4, cases_in: list[dict] | None = None) -> list[dict]:
    """Case-major, the arm order rotating by case; every check before every call. Returns this invocation's rows."""
    import benchset
    if not approval:
        raise SystemExit("E4 sends corpus text to Claude: name the decision (--approval \"decision 021\")")
    if not model.startswith("claude-cli/") and not (ctx_over or {}).get("fixture"):
        raise SystemExit("decision 021 approves Claude only (claude-cli/…), not " + model)
    all_cases = cases_in if cases_in is not None else [c for c in benchset.cases() if c["gold"]]
    case_list = [c for c in all_cases if not only or c["id"] in only]
    if only and len(case_list) != len(only):
        raise SystemExit(f"unknown case ids: {sorted(set(only) - {c['id'] for c in case_list})}")
    out = root / run_name
    out.mkdir(parents=True, exist_ok=True)
    path = out / "results.jsonl"
    ctx = dict(ctx_over or {})
    fp = ctx.pop("fp", None) or fingerprint(case_list, model, ctx.get("fixture"))
    previous = read_rows(path)
    foreign = {r["run_fp"] for r in previous} - {fp}
    if foreign:
        raise SystemExit(f"{path.relative_to(ROOT) if path.is_relative_to(ROOT) else path} holds rows of another "
                         f"run ({sorted(foreign)}); a changed input is a new --run")
    done = {(r["case"], r["arm"]) for r in previous}
    unq = unquoted_lines(all_cases)
    if "pack" not in ctx or "store" not in ctx:
        import askdb
        import ask
        import graph as kg
        import graphrag
        store, g = askdb.Store(), kg.build()
        ctx.setdefault("store", store)
        ctx.setdefault("pack", lambda c: ask.build_pack(c["question"], KIND, store=store,
                                                        graph=graphrag.without(g, c["key"])))
    if "lm" not in ctx:
        import lmrun
        ctx["lm"] = lambda: lmrun.make_lm(model)
    ctx.update(out=out, approval=approval, model=model)
    rows = []
    for i, case in enumerate(case_list):
        order = ARMS[i % 3:] + ARMS[:i % 3]
        for arm in order:
            if (case["id"], arm) in done:
                continue
            total_left = TOTAL - recorded_total(root)
            if total_left < worst(1_000):   # not even a one-kilobyte call fits
                raise Stop(f"stopped: ${TOTAL - total_left:.2f} recorded, ${total_left:.2f} left of ${TOTAL:.2f}")
            ctx.update(case_left=CASE_CAP, total_left=total_left)
            started = time.time()
            res = arm_rlm(case, ctx) if arm == "C" else arm_pack(case, ctx, expand=arm == "B")
            row = {"case": case["id"], "arm": arm, "order": "".join(order), "run_fp": fp,
                   "model": "fixture" if ctx.get("fixture") else model, **{k: v for k, v in res.items()
                                                                           if k not in ("answer", "shown")},
                   "wall": round(time.time() - started, 1),
                   **score(res, case["gold"], unq[case["id"]])}
            row["status"] = res["status"]
            row["shown"] = {d: compress(ns) for d, ns in sorted(res["shown"].items())}
            with path.open("a", encoding="utf-8") as fh:
                fh.write(json.dumps(row, ensure_ascii=False) + "\n")
            rows.append(row)
            log(f"{case['id']:4} {arm} {row['status']:14} recall {row['recall_all']} unquoted {row['recall_unquoted']} "
                f"invented {len(row['invented'])} shown {row['shown_lines']} calls {row['calls']} "
                f"${row['cost']:.4f} {row['wall']}s")
            if row.get("refused_by") == "total":
                raise Stop(f"stopped inside {case['id']} {arm}: the next call could cross ${TOTAL:.2f}")
    return rows


def compress(lines) -> list[list[int]]:
    out: list[list[int]] = []
    for n in sorted(set(lines)):
        if out and n == out[-1][1] + 1:
            out[-1][1] = n
        else:
            out.append([n, n])
    return out


# ── analysis and the decision rule ───────────────────────────────────────────

def bootstrap(diffs: list[float], seed: int = SEED, n: int = RESAMPLES) -> list[float]:
    rnd = random.Random(seed)
    means = sorted(statistics.mean(rnd.choice(diffs) for _ in diffs) for _ in range(n))
    return [round(means[int(0.05 * n)], 4), round(means[int(0.95 * n) - 1], 4)]


def analyse(rows: list[dict]) -> dict:
    """The decision rule of the README applied as written, per adaptive arm, on the cases every arm finished."""
    by = {(r["case"], r["arm"]): r for r in rows}
    cases = sorted({c for c, _ in by if all((c, a) in by for a in ARMS)})
    arms = {}
    for a in ARMS:
        rs = [by[(c, a)] for c in cases]
        done = [r for r in rs if r["scored"]]
        arms[a] = {"cases": len(rs), "scored": len(done),
                   "failed": {s: sum(r["status"] == s for r in rs) for s in sorted({r["status"] for r in rs})},
                   "forced": sum(bool(r.get("forced")) for r in rs),
                   "recall_all": round(statistics.mean(r["recall_all"] for r in rs), 4) if rs else None,
                   "recall_unquoted": _mean([r["recall_unquoted"] for r in rs]),
                   "complete_case_all": _mean([r["complete_all"] for r in rs]),
                   "invented": sum(len(r["invented"]) for r in rs),
                   "cost_mean": round(statistics.mean(r["cost"] for r in rs), 4) if rs else None,
                   "cost_total": round(sum(r["cost"] for r in rs), 4),
                   "read_gold_per_dollar": round(sum(len(r["read_gold"]) for r in rs) / sum(r["cost"] for r in rs), 1)
                   if rs and sum(r["cost"] for r in rs) else None,
                   "estimate_ratio_max": max((act / est for r in rs for est, act in r.get("estimates", []) if est),
                                             default=None)}
    verdicts = {}
    for a in ("B", "C"):
        d = [by[(c, a)]["recall_all"] - by[(c, "A")]["recall_all"] for c in cases]
        du = [by[(c, a)]["recall_unquoted"] - by[(c, "A")]["recall_unquoted"] for c in cases
              if by[(c, a)]["recall_unquoted"] is not None and by[(c, "A")]["recall_unquoted"] is not None]
        if not d:
            verdicts[a] = {"replaces_A": False, "why": "no complete triples"}
            continue
        ci = bootstrap(d) if len(d) > 1 else [d[0], d[0]]
        better, worse = sum(x > 0 for x in d), sum(x < 0 for x in d)
        lines = {
            "1_recall": {"mean_diff": round(statistics.mean(d), 4), "ci90": ci, "better": better, "worse": worse,
                         "holds": statistics.mean(d) >= 0.03 and ci[0] > 0 and better > worse},
            "2_unquoted": {"mean_diff": _mean(du), "pairs": len(du),
                           "holds": bool(du) and statistics.mean(du) >= 0},
            "3_invented": {"arm": arms[a]["invented"], "A": arms["A"]["invented"],
                           "holds": arms[a]["invented"] <= arms["A"]["invented"],
                           "listed": [dict(i, case=c) for c in cases for i in by[(c, a)]["invented"]]},
            "4_cost": {"mean": arms[a]["cost_mean"], "cap": CASE_CAP, "holds": arms[a]["cost_mean"] <= CASE_CAP}}
        verdicts[a] = {**lines, "replaces_A": all(v["holds"] for v in lines.values())}
    return {"triples": len(cases), "cases": cases, "arms": arms, "verdicts": verdicts,
            "recommendation": next((f"{a} replaces A — a proposal to the author, on circular cases"
                                    for a in ("B", "C") if verdicts.get(a, {}).get("replaces_A")), "A stays")}


def _mean(xs):
    xs = [x for x in xs if x is not None]
    return round(statistics.mean(xs), 4) if xs else None


# ── self-test ─────────────────────────────────────────────────────────────────

def selftest() -> list[str]:
    """Every path on a fixture LM and a stub pack over a real landed document: A answered, B expanding and not
    expanding, every failure status, the case cap, the total stop, resume, the decision rule. No model, no network."""
    import tempfile
    from types import SimpleNamespace
    import subject
    from lm_fixture import FixtureLM
    fails = []
    doc = next(d for d in subject.documents() if len(d.lines()) > 60 and d.offset > 1)
    line = lambda n: doc.lines()[n - doc.offset]  # noqa: E731
    sent = list(range(doc.offset + 5, doc.offset + 15))
    later = doc.offset + 40
    quotable = lambda n: next(w for w in [line(n).strip()[:60]] if w)  # noqa: E731
    a_line = next(n for n in sent if len(line(n).strip()) > 20)
    b_line = next(n for n in range(later, later + 20) if len(line(n).strip()) > 20 and
                  all(line(n).strip()[:60] not in line(m) for m in sent))
    gold = {(doc.slug, a_line), (doc.slug, b_line), (doc.slug, 1)}

    def answer(*quotes, need=None, extra=None):
        claims = [{"doc": d, "says": "x", "quotes": [{"text": t, "line_hint": h}]} for d, t, h in quotes]
        return json.dumps({"answerable": "partly", "claims": claims, "differ": [], "gaps": [], "need": need or [],
                           "next": []} | (extra or {}))

    class Costly(FixtureLM):
        def __init__(self, script, cost=0.01):
            super().__init__(script)
            self.cost = cost

        def forward(self, *a, **k):
            r = super().forward(*a, **k)
            r._hidden_params = {"response_cost": self.cost}
            return r

    class Store:
        def bm25(self, q, limit=20):
            return [{"slug": doc.slug, "line": n, "text": line(n)} for n in range(later, later + 20)][:limit]

        def window(self, slug, a, b):
            return [(n, line(n)) for n in range(a, b + 1)] if slug == doc.slug else []

    pack_text = "# Frage\n\n" + "\n".join(f"L{n}: {line(n)}" for n in sent)
    stub_pack = lambda c: (pack_text, {"shown": {doc.slug: sent}, "status": "complete"})  # noqa: E731
    cases = [{"id": "T1", "key": "x", "question": "q1", "gold": gold}, {"id": "T2", "key": "y", "question": "q2", "gold": gold}]

    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        base = {"pack": stub_pack, "store": Store(), "fixture": "1", "fp": "fp1", "novelgraph_py": sys.executable}

        def go(name, script, cost=0.01, only=("T1",), over=None, arms=("A",)):
            lm = Costly(list(script), cost)
            global ARMS
            saved, ARMS = ARMS, arms
            try:
                return run(name, list(only), "fixture", log=lambda *_: None, root=root, cases_in=cases,
                           ctx_over={**base, "lm": lambda: lm, **(over or {})}), lm
            finally:
                ARMS = saved

        # A: one placed gold quote, one invented quote, one outside-pack quote
        rows, _ = go("a", [answer((doc.slug, quotable(a_line), a_line), (doc.slug, "Diese Worte stehen nirgends xyz", 3),
                                  ("anderes-dokument", "irgendwas", 1))])
        r = rows[0]
        if r["read_gold"] != [[doc.slug, a_line]] or r["recall_all"] != round(1 / 3, 4):
            fails.append(f"A: read gold wrong: {r['read_gold']} {r['recall_all']}")
        if sorted(i["status"] for i in r["invented"]) != ["outside-pack", "unresolved"]:
            fails.append(f"A: invented evidence not counted: {r['invented']}")
        # B: the need is fetched, the second answer quotes a line only the expansion showed
        rows, lm = go("b", [answer((doc.slug, quotable(a_line), a_line), need=[{"term": "x"}]),
                            answer((doc.slug, quotable(a_line), a_line), (doc.slug, quotable(b_line), b_line))],
                      arms=("B",))
        r = rows[0]
        if r["rounds"] != 1 or r["read_gold"] != sorted([[doc.slug, a_line], [doc.slug, b_line]]):
            fails.append(f"B: the expansion's line did not become read gold: rounds {r['rounds']} {r['read_gold']}")
        if quotable(b_line) not in lm.requests[1]["messages"][0]["content"] or len(lm.requests) != 2:
            fails.append("B: the second prompt did not carry the fetched lines")
        # B: a need already shown asks for no round; A never quotes the expansion's line
        rows, lm = go("b2", [answer((doc.slug, quotable(a_line), a_line), need=[{"doc": doc.slug, "lines": sent[:2]}])],
                      arms=("B",))
        if rows[0]["rounds"] != 0 or len(lm.requests) != 1:
            fails.append("B: a need for lines already shown started a round")
        # B: a quote of a line the pack never showed stays outside-window, never read gold
        rows, _ = go("a2", [answer((doc.slug, quotable(b_line), b_line))])
        if rows[0]["read_gold"] or rows[0]["outside_window"] != 1:
            fails.append(f"A: a line the arm never showed was scored: {rows[0]['read_gold']}")
        # every failure status scores 0 in the primary view and None in the complete-case view
        for name, script, want in (("u", ["kein json"], "unparsed"), ("s", ['{"answerable": "vielleicht"}'], "schema-invalid"),
                                   ("e", [""], "refused")):
            rows, _ = go(name, script)
            if rows[0]["status"] != want or rows[0]["recall_all"] != 0.0 or rows[0]["complete_all"] is not None:
                fails.append(f"{want}: status {rows[0]['status']}, recall {rows[0]['recall_all']}")

        class Down(Costly):
            def forward(self, *a, **k):
                from lm_fixture import NetworkRefused
                raise NetworkRefused("down")
        rows = run("n", ["T1"], "fixture", log=lambda *_: None, root=root, cases_in=cases,
                   ctx_over={**base, "lm": lambda: Down([])})
        if rows[0]["status"] != "unreachable" or rows[0]["recall_all"] != 0.0:
            fails.append(f"unreachable: {rows[0]['status']}")
        # the case cap: B's second round would cross $0.15 — not made, the first answer stands, status answered
        rows, lm = go("cap", [answer((doc.slug, quotable(a_line), a_line), need=[{"term": "x"}]), "unused"],
                      cost=0.14, arms=("B",))
        r = rows[0]
        if len(lm.requests) != 1 or r["refused_by"] != "case" or r["status"] != "answered" or r["statuses"][-1] != "capped":
            fails.append(f"case cap: {len(lm.requests)} calls, refused_by {r['refused_by']}, {r['statuses']}")
        # the total stop: with $19.99 recorded, no call is made and the run raises Stop
        (root / "spent" / "lm").mkdir(parents=True)
        (root / "spent" / "lm" / "A.jsonl").write_text(json.dumps({"cost": 19.99}) + "\n")
        try:
            go("stop", ["unused"])
            fails.append("the total did not stop the run")
        except Stop:
            if read_rows(root / "stop" / "results.jsonl"):
                fails.append("the total was checked only inside the arm, not before it began")
        # $0.07 left: the first call ($0.05) is made, the second could cross the total and is not
        (root / "spent" / "lm" / "A.jsonl").write_text("")
        (root / "spent" / "lm" / "A.jsonl").write_text(json.dumps({"cost": TOTAL - 0.07 - recorded_total(root)}) + "\n")
        try:
            go("stop2", [answer((doc.slug, quotable(a_line), a_line), need=[{"term": "x"}]), "unused"], cost=0.05,
               arms=("B",))
            fails.append("a call that could cross the total was made")
        except Stop:
            if read_rows(root / "stop2" / "results.jsonl")[0]["refused_by"] != "total":
                fails.append("the total stop did not name itself")
        (root / "spent" / "lm" / "A.jsonl").unlink()
        # resume: done rows are skipped; rows of another fingerprint refuse the run
        rows, lm = go("a", ["unused"], only=("T1",))
        if rows or lm.requests:
            fails.append("a resumed run repeated a done case")
        try:
            run("a", ["T1"], "fixture", log=lambda *_: None, root=root, cases_in=cases,
                ctx_over={**base, "fp": "fp2", "lm": lambda: Costly([])})
            fails.append("a run resumed over rows of another fingerprint")
        except SystemExit:
            pass
        # C through its subprocess in fixture mode: the stub answers
        rows, _ = go("c", [], arms=("C",), over={"novelgraph_py": sys.executable, "fixture": "stub"})
        if rows[0]["status"] != "answered" or rows[0]["arm"] != "C":
            fails.append(f"C: the subprocess path failed: {rows[0].get('status')} {rows[0].get('error', '')[:200]}")
    # the decision rule, on rows made up for it
    def row(c, a, rec, unq=0.0, inv=0, cost=0.05):
        return {"case": c, "arm": a, "scored": True, "status": "answered", "recall_all": rec, "recall_unquoted": unq,
                "complete_all": rec, "invented": [{"doc": "d", "text": "t", "status": "unresolved"}] * inv,
                "cost": cost, "read_gold": [], "forced": False}
    cs = [f"K{i}" for i in range(10)]
    good = [row(c, "A", 0.30) for c in cs] + [row(c, "B", 0.36 + 0.01 * (i % 3)) for i, c in enumerate(cs)] + \
           [row(c, "C", 0.30) for c in cs]
    an = analyse(good)
    if not an["verdicts"]["B"]["replaces_A"] or an["verdicts"]["C"]["replaces_A"] or not an["recommendation"].startswith("B"):
        fails.append(f"rule: B should pass and C fail: {an['recommendation']}")
    worse_inv = [dict(r, invented=r["invented"] + [{"doc": "d", "text": "t", "status": "unresolved"}]) if r["arm"] == "B" else r
                 for r in good]
    if analyse(worse_inv)["verdicts"]["B"]["replaces_A"]:
        fails.append("rule: more invented evidence than A did not veto")
    lower_unq = [dict(r, recall_unquoted=-0.1) if r["arm"] == "B" else r for r in good]
    if analyse(lower_unq)["verdicts"]["B"]["replaces_A"]:
        fails.append("rule: worse on the unquoted view did not veto")
    small = [dict(r, recall_all=0.32) if r["arm"] == "B" else r for r in good]
    if analyse(small)["verdicts"]["B"]["replaces_A"]:
        fails.append("rule: +0.02 passed the +0.03 threshold")
    costly = [dict(r, cost=0.2) if r["arm"] == "B" else r for r in good]
    if analyse(costly)["verdicts"]["B"]["replaces_A"]:
        fails.append("rule: a mean cost over the cap passed")
    if worst(72_000) > CASE_CAP:
        fails.append(f"a full pack's worst case ${worst(72_000):.3f} exceeds the case cap: A could never run")
    return fails


def main(argv: list[str]) -> int:
    import argparse
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("selftest")
    r = sub.add_parser("run")
    r.add_argument("--run", required=True)
    r.add_argument("--cases")
    r.add_argument("--approval")
    r.add_argument("--model", default=MODEL)
    a = sub.add_parser("analyse")
    a.add_argument("--run", required=True)
    args = ap.parse_args(argv)
    if args.cmd == "selftest":
        fails = selftest()
        for f in fails:
            print(f"  FAIL  {f}")
        print(f"e4: {'held' if not fails else f'{len(fails)} failed'} (A, B expanding and not, read gold only on shown "
              "lines, every failure status, case cap, total stop, resume, C subprocess, the decision rule)")
        return 1 if fails else 0
    if args.cmd == "run":
        try:
            run(args.run, args.cases.split(",") if args.cases else None, args.approval, model=args.model)
        except Stop as exc:
            print(exc)
        print(f"recorded E4 spend: ${recorded_total():.4f} of ${TOTAL:.2f}")
        return 0
    rows = read_rows(E4 / args.run / "results.jsonl")
    result = analyse(rows)
    (E4 / args.run / "analysis.json").write_text(json.dumps(result, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("triples", "recommendation")} |
                     {"arms": {a: {k: v[k] for k in ("recall_all", "recall_unquoted", "invented", "cost_mean")}
                               for a, v in result["arms"].items()}}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
