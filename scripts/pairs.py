"""One term or two — the harness every rule and every model is scored through.

The task, the rows and the metric already exist and are not restated here:
`trainset.surface_pairs()` derives the labelled pairs from
`Plan/runs/judgements.jsonl`, `trainset.fold_baseline()` scores the rule in the
repository, `trainset.score_one()` returns a score *and the human's rule as
feedback* (P6: one encoding each). This adds what a model run needs and no
scanned repository supplied:

- **A canary veto.** The never-merge pairs in `selftest.MUST_NOT_MERGE`
  (`Negentropie`/`Entropie` first) are asked of every candidate. One merge and
  the candidate is `vetoed` in `Plan/runs/baselines.jsonl`, whatever its
  accuracy — `dspy.GEPA` optimizes a mean, and `dspy-auto-gepa`'s `promote()`
  saves whatever training produced, so otherwise a merged canary costs 1/n.
- **Rule first, model on the residual.** Neither rule in `RULES` has produced a
  false merge on this set; every miss is a pair it calls two terms. So a hybrid
  answers `one-term` wherever the rule named by `--rule` does and asks a model
  only about the rest. A model is never given the chance to undo a rule's merge.
  The model still *trains* on every labelled row outside the held-out fold,
  including the pairs the rule answers.
- **Pinned, stratified folds.** Canaries are never training data. The labelled
  rows are split by decision into k folds deterministically by id, and each
  row is scored by a program compiled without it.
- **Repeats with the cache off** (P18): `--repeats N` scores each held-out row
  N times through `lmrun.call`; its outcome is the fraction correct.
- **The metric is five-argument from day one**
  (`metric(example, pred, trace=None, pred_name=None, pred_trace=None) ->
  dspy.Prediction(score, feedback)`), the shape `dspy-auto-gepa`,
  `dspy-agent-skills` and `dspy-book-eight-steps` converge on, so GEPA needs no
  rewrite. A metric returning a dict crashes `dspy.Evaluate`'s executor — the
  dspy-agent-skills tests guard against exactly that.

The optimizer ladder is `optimizers-and-data_2026-09-17.md`'s:
`labeled` → `bootstrap` → `inferrules` → `simba` → `gepa`. SIMBA's `bsize` is
set to the training size, at most 16, because its default of 32 exceeded the
whole set when this was written and `dspy-book-optimizers` measured it scoring
*below* its baseline while costing the most of twelve.

    python3 scripts/pairs.py score [--rule fold|plural] [--record]   # standard library, offline
    python3 scripts/pairs.py selftest                               # the veto, shown failing
    python3 scripts/pairs.py report [--rule plural]                 # each row split: merges found, false merges
    .venv-dspy/bin/python scripts/pairs.py final --optimizer inferrules --rule plural --model … --approval …
                                                                    # one compile on all pairs, saved; no row
    .venv-dspy/bin/python scripts/pairs.py run --optimizer labeled [--rule plural] --dry-run
    .venv-dspy/bin/python scripts/pairs.py run --optimizer inferrules --rule plural \\
        --model claude-cli/haiku --approval "decision 011" [--folds 5] [--repeats 3] [--threads 4] [--record]
    .venv-dspy/bin/python scripts/pairs.py run --optimizer labeled --rule plural \\
        --model route/<a free model from Plan/runs/route/models.json> --approval "decision 011" …
    .venv-dspy/bin/python scripts/pairs.py run --optimizer gepa --rule plural --model claude-cli/haiku \\
        --reflection-model claude-cli/sonnet --approval "decision 011" …

`--model` takes the three kinds of name `lmrun.make_lm` builds (decision 011): `claude-cli/…`
is Claude, first party; `route/…` is a free OpenRouter model through `route.py`, pinned;
anything else is a LiteLLM string and needs its own decision. The row's `cost` is every
call the run made, compile included.

A new deterministic rule is one entry in `RULES`, scored by `score --rule <name>`
and asked first by `run --rule <name>`, so a model sees only what the rule leaves.
**A rule's reach is a decision, not this file's**, so `RULES` holds only what the
repository has decided: `fold()`, and the plural rule whose reach decision 010
set on the author's delegation.
"""


import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import baseline  # noqa: E402
import trainset  # noqa: E402
from selftest import MUST_NOT_MERGE  # noqa: E402
from wiki_index import fold  # noqa: E402

TASK = "one-term-or-two"


def plural(a: str, b: str, endings: tuple[str, ...] = ("s", "es", "e", "en", "n"),
           written: bool = True) -> str:
    """`fold()`, and a plural ending is not a term boundary (J4, J23), within the
    reach decision 010 gives it: an ending from a closed set appended to the whole
    shorter surface, `-n` only after `-e`, a stem of at least four letters, and the
    ending written in lower case in the longer surface.

    Not a stemmer: nothing is ever removed from the shorter surface, so
    `Negentropie`/`Entropie`, which differ at the front, stay apart. `-er` is not
    an ending here because it also makes a noun of a verb: `Spiel`/`Spieler`.
    The lower-case test is what keeps `Logo` out of the Guardian `LogOS`, which
    `fold()` spells `logos`. `endings` and `written` exist so that the selftest
    can hand the canary veto a rule that reaches too far."""
    fa, fb = fold(a), fold(b)
    if fa == fb:
        return "one-term"
    (short, _), (longer, raw) = sorted(((fa, a), (fb, b)), key=lambda p: len(p[0]))
    ending = longer[len(short):]
    if len(short) < 4 or not longer.startswith(short) or ending not in endings:
        return "two-terms"
    if ending == "n" and not short.endswith("e"):
        return "two-terms"          # Alter/Altern stays a person's call (decision 010)
    if written and not re.sub(r"\W+$", "", raw).endswith(ending):
        return "two-terms"
    return "one-term"


RULES = {
    "fold": lambda a, b: "one-term" if fold(a) == fold(b) else "two-terms",
    "plural": plural,
}


def rows() -> list[dict]:
    return trainset.surface_pairs()


def canaries() -> list[tuple[str, str]]:
    return list(MUST_NOT_MERGE)


def canary_pair(row: dict) -> bool:
    """Whether a ledger row is one of the never-merge pairs, in either order."""
    return frozenset((row["first"], row["second"])) in {frozenset(c) for c in canaries()}


WINDOW = 160   # characters kept on either side of a surface; a landed line can be a whole paragraph
GIVE_UP = 6    # unreachable calls in a row that end a run as not reached


def evidence(row: dict) -> str:
    """The lines a program may see beside the two surfaces, found by code alone.

    `NOW.md`: eleven of the nineteen pairs the plural rule leaves were decided from
    the passage, and the program saw only the surfaces. This is the passage, placed
    the way `entities.py place` places a name (P26): the first line of the pair's
    document holding both surfaces as whole words, else the first line holding each.
    **Never the lines the person cited**: a deployed program meets a new pair before
    anyone has read it, and a score built on the person's choice of line would
    measure that choice. A surface the document does not hold is said, not guessed."""
    import entities
    import subject
    a, b = row.get("first", ""), row.get("second", "")
    try:
        doc = subject.document(row.get("document") or "")
    except Exception:
        return "(kein Quelldokument)"
    lines = doc.lines()
    both = next((i for i, line in enumerate(lines) if entities.holds(line, a) and entities.holds(line, b)), None)
    picks = [both] if both is not None else [
        i for i in dict.fromkeys(
            (entities.first_line(doc, t) or 0) - doc.offset if entities.first_line(doc, t) else None
            for t in (a, b)) if i is not None]
    out = [f"L{doc.offset + i}: {_window(lines[i], (a, b))}" for i in picks]
    for term in (a, b):
        if entities.first_line(doc, term) is None:
            out.append(f"(»{term}« steht in diesem Dokument auf keiner Zeile als ganzes Wort)")
    return "\n".join(out)


def _window(line: str, terms: tuple[str, ...]) -> str:
    """The parts of a long line around each surface, joined by an ellipsis."""
    low = line.lower()
    spans = []
    for term in terms:
        at = low.find(term.lower())
        if at >= 0:
            spans.append([max(0, at - WINDOW), min(len(line), at + len(term) + WINDOW)])
    if not spans:
        return line[: 2 * WINDOW]
    spans.sort()
    merged = [spans[0]]
    for start, end in spans[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    text = " … ".join(line[s:e].strip() for s, e in merged)
    return ("… " if merged[0][0] > 0 else "") + text + (" …" if merged[-1][1] < len(line) else "")


def folds(labelled: list[dict], k: int) -> list[list[dict]]:
    """Stratified by decision, deterministic by id: the same rows, the same folds."""
    out: list[list[dict]] = [[] for _ in range(k)]
    for decision in trainset.DECIDED:
        group = sorted((r for r in labelled if r["decision"] == decision),
                       key=lambda r: baseline.digest(r["id"]))
        for i, r in enumerate(group):
            out[i % k].append(r)
    return [f for f in out if f]


def merged_canaries(rule) -> list[tuple[str, str]]:
    """The never-merge pairs a rule merges. Any one of them vetoes it."""
    return [(a, b) for a, b in canaries() if rule(a, b) == "one-term"]


def score_rule(name: str) -> dict:
    import inspect
    rule = RULES[name]
    labelled = rows()
    outcomes = {r["id"]: int(trainset.score_one(r, rule(r["first"], r["second"]))["score"])
                for r in labelled}
    merged = merged_canaries(rule)
    # fold()'s own source is part of every rule's identity. Until 2026-09-24 only
    # the rule's source was hashed, so a change inside fold() left the hash as it was.
    return baseline.row(TASK, f"rule:{name}", outcomes,
                        program=[inspect.getsource(rule), inspect.getsource(fold)],
                        trainset=labelled, vetoed=bool(merged),
                        note=f"canaries merged: {merged}" if merged else "no canary merged")


def selftest() -> tuple[list[str], int]:
    """The plural rule merges the plurals the ledger's judgements merged and no
    canary; a rule reaching one step further is vetoed, each for its own reason.
    Without the last two cases nothing would show the veto can fire on this rule:
    the four canaries before decision 010 were out of any plural rule's reach."""
    failures = []
    merges = [("Kern-Welt", "Kern-Welten"), ("Guardian", "Guardians"), ("Riss", "Risse"),
              ("Alter", "Alters"), ("Anomalie", "Anomalien"), ("Coheron", "Coheronen"),
              ("Glitch", "Glitches")]
    for a, b in merges:
        if plural(a, b) != "one-term":
            failures.append(f"plural kept {a!r} and {b!r} apart")
    if merged_canaries(plural):
        failures.append(f"plural merged {merged_canaries(plural)}")
    too_far = {
        "an -er ending": (lambda a, b: plural(a, b, endings=("s", "es", "e", "en", "n", "er")),
                          ("Spiel", "Spieler")),
        "an ending not written in lower case": (lambda a, b: plural(a, b, written=False),
                                                ("Logo", "LogOS")),
    }
    for why, (rule, pair) in too_far.items():
        if pair not in merged_canaries(rule):
            failures.append(f"{why}: the veto did not fire on {pair}")
    # a ledger row that is a canary pair vetoes a run when a held-out repeat merges it
    if not canary_pair({"first": "Entropie", "second": "Negentropie"}):
        failures.append("the canary Negentropie/Entropie is not recognised in the other order")
    if canary_pair({"first": "Riss", "second": "Risse"}):
        failures.append("a pair the ledger merges was taken for a canary")
    return failures, len(merges) + 1 + len(too_far) + 2


# --- the model half: imported only when a model is asked for ---------------------

def program_and_metric(with_evidence: bool = False):
    import dspy
    from typing import Literal

    class SameTerm(dspy.Signature):
        """Sind die beiden Oberflächenformen derselbe Begriff im Korpus (one-term)
        oder zwei verschiedene Begriffe (two-terms)? Ein bestimmter Artikel ist nie
        eine Begriffsgrenze. Ein Kompositum wird nach dem eingeordnet, was es
        benennt, nie nach seinem Kopf. Gegensätze wie Negentropie/Entropie sind nie
        ein Begriff. Nenne die Regel, nach der du entscheidest."""
        first: str = dspy.InputField()
        second: str = dspy.InputField()
        decision: Literal["one-term", "two-terms"] = dspy.OutputField()
        rule: str = dspy.OutputField(desc="die Regel, in einem Satz")

    def metric(example, pred, trace=None, pred_name=None, pred_trace=None):
        judged = trainset.score_one(example.toDict(), str(getattr(pred, "decision", "")))
        return dspy.Prediction(score=judged["score"], feedback=judged["feedback"])

    signature = SameTerm
    if with_evidence:
        signature = SameTerm.append("evidence", dspy.InputField(
            desc="die Zeilen des Quelldokuments, in denen die Formen stehen, mit Zeilennummer — "
                 "von Code gefunden, nicht ausgewählt"), type_=str)
    return dspy.Predict(signature), metric


def optimizer(name: str, metric, train_size: int, reflection_lm=None, gepa_calls: int | None = None):
    import dspy
    if name == "labeled":
        return dspy.LabeledFewShot(k=min(8, train_size))
    if name == "bootstrap":
        return dspy.BootstrapFewShot(metric=lambda e, p, t=None: metric(e, p).score,
                                     max_bootstrapped_demos=4, max_labeled_demos=8)
    if name == "inferrules":
        return dspy.InferRules(num_candidates=4, num_rules=6,
                               metric=lambda e, p, t=None: metric(e, p).score)
    if name == "simba":
        return dspy.SIMBA(metric=lambda e, p: metric(e, p).score, bsize=min(train_size, 16),
                          num_candidates=4, max_steps=4)
    if name == "gepa":
        # auto="light" is ~380 + 4 x trainset metric calls per compile, six compiles a run;
        # --gepa-calls sets max_metric_calls instead, so a run's size is chosen, not implied
        budget = {"max_metric_calls": gepa_calls} if gepa_calls else {"auto": "light"}
        return dspy.GEPA(metric=metric, reflection_lm=reflection_lm, seed=0, track_stats=True, **budget)
    raise SystemExit(f"unknown optimizer {name!r}: labeled, bootstrap, inferrules, simba, gepa")


def run(name: str, model: str | None, approval: str | None, k: int, repeats: int,
        dry_run: bool, record: bool, reflection: str | None, rule: str = "fold", threads: int = 1,
        with_evidence: bool = False, gepa_calls: int | None = None, score: bool = True) -> dict:
    """Compile per fold, score each held-out row `repeats` times, ask the canaries of the
    final compile. `threads` scores held-out rows in parallel, each thread on its own
    copy of the LM, so `lmrun.call` reads only its own call's history."""
    import inspect
    import tempfile
    import threading
    from concurrent.futures import ThreadPoolExecutor
    from datetime import datetime
    import dspy
    from dspy.clients.base_lm import GLOBAL_HISTORY
    from lmrun import call, make_lm

    if with_evidence and model and model.startswith("route/"):
        raise SystemExit("decision 011: no line of a document goes to a free model — "
                         "run --evidence on claude-cli/…")
    first = RULES[rule]           # asked before the model, so the model sees only its residual
    labelled = rows()             # the trainset hash stays the labelled pairs', evidence or not

    def inputs(r: dict) -> dict:
        shown = {"first": r["first"], "second": r["second"]}
        if with_evidence:
            shown["evidence"] = evidence(r)
        return shown
    examples = {r["id"]: dspy.Example(**{**r, **inputs(r)}).with_inputs(*inputs(r)) for r in labelled}
    program, metric = program_and_metric(with_evidence)
    started = datetime.now().isoformat()

    if dry_run:
        from lm_fixture import FixtureLM, fill, offline
        lm = FixtureLM(fill(decision="two-terms", rule="Probelauf: immer zwei Begriffe."))
        context = offline(lm)
        out_dir = Path(tempfile.mkdtemp())
        per_repeat = [lm] * repeats
    else:
        if not (model and approval):
            raise SystemExit("a real run needs --model and --approval naming the author's decision")
        options = {"purpose": f"dspy-pairs-{name}"} if model.startswith("route/") else {}
        lm = make_lm(model, **options)
        context = dspy.context(lm=lm)
        out_dir = None
        # through route.py an identical request is answered from its recording, so each
        # repeat is its own attempt number; every other LM here has no cache to defeat (P18)
        per_repeat = ([make_lm(model, attempt=i, **options) for i in range(repeats)]
                      if model.startswith("route/") else [lm] * repeats)
    reflection_lm = lm if dry_run else (
        make_lm(reflection, **({"thinking": None} if reflection.startswith("claude-cli/") else {}))
        if reflection else None)

    label = (f"{name}{gepa_calls}" if name == "gepa" and gepa_calls else name) + ("+evidence" if with_evidence else "")
    step = f"pairs-{label.replace('+', '-')}-" + re.sub(r"[^a-z0-9]+", "-", (model or "fixture").lower()).strip("-")

    unreached = {"in a row": 0}
    guard = threading.Lock()

    def ask(compiled, r) -> tuple[str, float | None]:
        hits = []
        for i in range(repeats):
            with guard:
                if unreached["in a row"] >= GIVE_UP:
                    return r["id"], None
            own = per_repeat[i] if dry_run or threads == 1 else per_repeat[i].copy()
            with dspy.context(lm=own):
                # the ledger's rules are English (the work language), and they are the demos'
                # `rule` field: a model that follows its demos answers in English (P19)
                pred, rec = call(compiled, step=step, subject="surface-pairs",
                                 approval=approval, english=["rule"], out_dir=out_dir, **inputs(r))
            with guard:
                unreached["in a row"] = unreached["in a row"] + 1 if rec["status"] == "unreachable" else 0
            if rec["status"] == "answered":
                hits.append(trainset.score_one(r, str(pred.decision))["score"])
        return r["id"], (round(sum(hits) / len(hits), 3) if hits else None)

    outcomes: dict[str, float | None] = {}
    compiled_states = []
    with context:
        for held in (folds(labelled, k) if score else []):
            held_ids = {r["id"] for r in held}
            train = [examples[i] for i in examples if i not in held_ids]
            compiled = optimizer(name, metric, len(train), reflection_lm, gepa_calls).compile(
                program.deepcopy(), trainset=train)
            compiled_states.append(compiled.dump_state())
            asked = []
            for r in held:
                if first(r["first"], r["second"]) == "one-term":
                    outcomes[r["id"]] = float(r["decision"] == "one-term")   # the rule answers
                else:
                    asked.append(r)
            with ThreadPoolExecutor(max(1, threads)) as pool:
                outcomes.update(pool.map(lambda r: ask(compiled, r), asked))
            if unreached["in a row"] >= GIVE_UP:
                # never reached is not answered badly (P15): no row, and the reason said
                raise SystemExit(f"{model}: {GIVE_UP} calls in a row unreachable — not reached, "
                                 "nothing recorded; the calls made are in Plan/runs/surface-pairs/lm/")
        merged = []
        final = optimizer(name, metric, len(examples), reflection_lm, gepa_calls).compile(
            program.deepcopy(), trainset=list(examples.values()))
        for a, b in canaries():
            if first(a, b) == "one-term":
                merged.append((a, b))
                continue
            # asked as often as a held-out pair (P18): until 2026-09-25 each canary was asked
            # once, and a free model that merged Negentropie/Entropie one time in three on its
            # held-out row passed the veto
            for i in range(repeats):
                with dspy.context(lm=per_repeat[i]):
                    pred, rec = call(final, step=f"{step}-canary", subject="surface-pairs",
                                     approval=approval, out_dir=out_dir, **inputs({"first": a, "second": b}))
                if rec["status"] == "answered" and str(pred.decision) == "one-term":
                    merged.append((a, b))
                    break
        # a ledger row that is a canary pair is asked of each fold's program as well
        for r in labelled:
            if canary_pair(r) and outcomes.get(r["id"]) is not None and outcomes[r["id"]] < 1:
                merged.append((r["first"], r["second"], f"held-out {r['id']}"))
        if not dry_run:
            save_program(final, step, rule, merged, compiled_states)

    # every call this run made, compile included: DSPy's global history holds each LM's
    # entries with the cost its response reported (claude_lm: the CLI's total_cost_usd)
    cost = round(sum(e.get("cost") or 0.0 for e in list(GLOBAL_HISTORY)
                     if str(e.get("timestamp", "")) >= started), 4)
    unscored = sum(v is None for v in outcomes.values())
    entry = baseline.row(TASK, f"{'dry-run:' if dry_run else ''}rule:{rule}+{label}:{model or 'fixture'}",
                         outcomes, program=[inspect.getsource(first), inspect.getsource(fold),
                                            compiled_states],
                         trainset=labelled, vetoed=bool(merged), cost=cost,
                         note=f"k={k} repeats={repeats}; canaries merged: {merged}; "
                              f"{unscored} rows not scored; reflection {reflection or '-'}")
    if record and not dry_run:
        baseline.append(entry)
    return entry


PROGRAMS = ROOT / "Plan" / "runs" / "surface-pairs" / "programs"


def save_program(program, step: str, rule: str, merged: list, folds: list | None = None) -> Path:
    """The final compile of a real run, as DSPy dumps it — the demos an optimizer chose, the
    instructions it wrote, InferRules' rules, GEPA's text — and each fold's program, which
    is what scored the held-out pairs. Until 2026-09-25 nothing kept either, so the first
    InferRules run's rules left with its process."""
    from datetime import datetime, timezone
    PROGRAMS.mkdir(parents=True, exist_ok=True)
    target = PROGRAMS / f"{step}.json"
    signature = getattr(program, "signature", None)
    target.write_text(json.dumps({
        "step": step, "rule_first": rule, "canaries_merged": merged,
        "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "instructions": getattr(signature, "instructions", None),
        "demos": len(getattr(program, "demos", []) or []),
        "state": program.dump_state(),
        "folds": folds or [],
    }, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
    return target


def report(floor: str = "plural") -> list[str]:
    """Every row of this task on the current trainset, split by direction.

    A score mixes the two errors this task has, and they are not worth the same: a
    merge the rule missed and the model found is recall, a pair the ledger keeps
    apart and the model merged is a **false merge** — the kind the canaries exist
    for. So each row is read against the rule named by `floor`: the pairs it
    leaves, how many of their gold merges the candidate found, how many of their
    gold splits it kept, and every pair it merged against the ledger, by id."""
    labelled = {r["id"]: r for r in rows()}
    left = {i: r for i, r in labelled.items() if RULES[floor](r["first"], r["second"]) != "one-term"}
    merges = [i for i, r in left.items() if r["decision"] == "one-term"]
    splits = [i for i, r in left.items() if r["decision"] == "two-terms"]
    current = baseline.digest(list(labelled.values()))
    lines = [f"{len(left)} pairs the rule {floor!r} leaves: {len(merges)} gold one-term, {len(splits)} gold two-terms"]
    for row in baseline.rows(TASK):
        if row["trainset_hash"] != current or not all(i in row["outcomes"] for i in left):
            continue
        got = row["outcomes"]
        found = sum(got[i] or 0 for i in merges)
        kept = sum(got[i] or 0 for i in splits)
        false = sorted((i for i in splits if got[i] is not None and got[i] < 1), key=lambda i: got[i])
        unscored = sum(got[i] is None for i in left)
        flag = "  VETOED" if row["vetoed"] else ""
        missed = [i for i in splits if canary_pair(labelled[i]) and got[i] is not None and got[i] < 1]
        if missed and not row["vetoed"]:
            flag += f"  CANARY MERGED IN A HELD-OUT REPEAT ({', '.join(missed)}) — not vetoed when recorded"
        lines.append(f"{row['candidate']:<52} {row['score'] if row['score'] is not None else '—':>6}  "
                     f"merges found {found:5.2f}/{len(merges)}  kept apart {kept:5.2f}/{len(splits)}  "
                     f"${row.get('cost') or 0:.2f}{flag}"
                     + (f"  unscored {unscored}" if unscored else "")
                     + ("".join(f"\n      false merge {i} {got[i]:.2f}: {labelled[i]['first']} / {labelled[i]['second']}"
                                for i in false)))
    return lines


def main(argv: list[str]) -> int:
    def opt(flag, default=None):
        return argv[argv.index(flag) + 1] if flag in argv else default

    rule = opt("--rule", "fold")
    if rule not in RULES:
        raise SystemExit(f"unknown rule {rule!r}: {', '.join(RULES)}")
    if argv[:1] == ["selftest"]:
        problems, total = selftest()
        for p in problems:
            print(f"  FAIL  {p}")
        print(f"pairs: {total - len(problems)} of {total} cases hold "
              f"(plural merges, no canary merged, the veto fires on -er and on case, "
              f"a canary pair is known in either order)")
        return 1 if problems else 0
    if argv[:1] == ["final"]:
        # one compile on every labelled pair, the canaries asked, the program saved —
        # no folds and no ledger row: an artifact to read, not a measurement
        entry = run(opt("--optimizer", "labeled"), opt("--model"), opt("--approval"), 0, 1, "--dry-run" in argv,
                    False, opt("--reflection-model"), rule, 1, "--evidence" in argv,
                    int(opt("--gepa-calls")) if opt("--gepa-calls") else None, score=False)
        if "--dry-run" not in argv:
            print(f"saved under {PROGRAMS.relative_to(ROOT)}/; cost ${entry['cost']:.4f}; {entry['note']}")
        return 0
    if argv[:1] == ["report"]:
        print("\n".join(report(rule if "--rule" in argv else "plural")))
        return 0
    if argv[:1] == ["score"]:
        name = rule
        entry = score_rule(name)
        print(f"{entry['candidate']}: {entry['correct']}/{entry['scored']} = {entry['score']:.1%} "
              f"on {entry['n']} labelled pairs; {entry['note']}")
        if "--record" in argv:
            baseline.append(entry)
            verdict, why = baseline.compare(TASK, floor="rule:fold")
            print(f"recorded; compare against rule:fold → {verdict} {why}")
        return 0
    if argv[:1] == ["run"]:
        entry = run(opt("--optimizer", "labeled"), opt("--model"), opt("--approval"),
                    int(opt("--folds", "5")), int(opt("--repeats", "1")),
                    "--dry-run" in argv, "--record" in argv, opt("--reflection-model"), rule,
                    int(opt("--threads", "1")), "--evidence" in argv,
                    int(opt("--gepa-calls")) if opt("--gepa-calls") else None)
        print(json.dumps({k: entry[k] for k in ("candidate", "n", "scored", "correct", "score",
                                                "vetoed", "cost", "note")}, ensure_ascii=False, indent=1))
        if "--record" in argv and "--dry-run" not in argv:
            verdict, why = baseline.compare(TASK, floor=f"rule:{rule}")
            print(f"compare against rule:{rule} → {verdict} {why}")
        return 1 if entry["vetoed"] else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
