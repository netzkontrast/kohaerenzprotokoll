"""One term or two — the harness every rule and every model is scored through.

The task, the rows and the metric already exist and are not restated here:
`trainset.surface_pairs()` derives the labelled pairs from
`Plan/runs/judgements.jsonl`, `trainset.fold_baseline()` scores the rule in the
repository, `trainset.score_one()` returns a score *and the human's rule as
feedback* (P6: one encoding each). This adds what a model run needs and no
scanned repository supplied:

- **A canary veto.** The never-merge pairs in `selftest.MUST_NOT_MERGE`
  (`Negentropie`/`Entropie` first) are asked of every compiled fold and the
  final candidate, as often as a held-out pair (P18: a free model that merged
  `Negentropie`/`Entropie` one time in three passed a veto that asked once). A
  merge or an unscorable answer vetoes the run in
  `Plan/runs/baselines.jsonl`, whatever its
  accuracy — `dspy.GEPA` optimizes a mean, and `dspy-auto-gepa`'s `promote()`
  saves whatever training produced, so otherwise a merged canary costs 1/n.
- **Rule first, model on the residual.** Neither rule in `RULES` has produced a
  false merge on this set; every miss is a pair it calls two terms. So a hybrid
  answers `one-term` wherever the rule named by `--rule` does and asks a model
  only about the rest. A model is never given the chance to undo a rule's merge.
  The model still *trains* on every labelled row outside the held-out fold,
  including the pairs the rule answers.
- **Pinned, stratified folds.** Canaries are never training data. All judgements
  of the same unordered, folded surface pair stay in one fold. Groups are
  assigned by decision with row counts balanced across folds; each row is
  scored by a program compiled without that pair.
- **Hard negatives in the labeled rung.** Among *training* rows, two labelled
  lookalikes that are different terms get reserved demo slots. `LabeledFewShot`
  uses `sample=False` to preserve that choice; the never-merge canaries remain
  outside training even when one also appears in the judgement ledger.
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
    .venv-dspy/bin/python scripts/pairs.py run --optimizer labeled [--rule plural] --dry-run
    .venv-dspy/bin/python scripts/pairs.py run --optimizer inferrules --rule plural \\
        --model claude-cli/haiku --approval "decision 011" [--folds 5] [--repeats 3] [--threads 4] [--record]
    .venv-dspy/bin/python scripts/pairs.py run --optimizer labeled --rule plural \\
        --model route/<a free model from Plan/runs/route/models.json> --approval "decision 011" …
    .venv-dspy/bin/python scripts/pairs.py run --optimizer gepa --rule plural --model claude-cli/haiku \\
        --reflection-model claude-cli/sonnet --approval "decision 011" [--gepa-calls 200] …
    .venv-dspy/bin/python scripts/pairs.py final --optimizer inferrules --rule plural --model … --approval …
                                                                    # one compile on all pairs, saved; no row

`--model` takes the three kinds of name `lmrun.make_lm` builds (decision 011): `claude-cli/…`
is Claude, first party; `route/…` is a free OpenRouter model through `route.py`, pinned;
anything else is a LiteLLM string and needs its own decision. The row's `cost` is every
call the run made, compile included. `--evidence` adds the document lines code places
beside the two surfaces, and is refused for a free model. A recorded run also records the
floor on the rows it used, when none is there, so the two can be compared.

A new deterministic rule is one entry in `RULES`, scored by `score --rule <name>`
and asked first by `run --rule <name>`, so a model sees only what the rule leaves.
**A rule's reach is a decision, not this file's**, so `RULES` holds only what the
repository has decided: `fold()`, and the plural rule whose reach decision 010
set on the author's delegation.
"""


import json
import re
import sys
from difflib import SequenceMatcher
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


def model_rows() -> list[dict]:
    """A canary may exist in the ledger; it still cannot train the model."""
    return without_canaries(rows())


def is_hard_negative(row: dict) -> bool:
    """A distinct-term judgement whose surfaces are visibly easy to conflate."""
    return row["decision"] == "two-terms" and bool(
        {"substring", "compound", "prefix", "shared-stem", "near-match:index",
         "proper-name-containment", "word-order"}.intersection(row["features"]))


def labeled_demos(training: list[dict], k: int = 8) -> list[dict]:
    """Reserve two slots for labelled lookalikes that are different terms.

    Only the caller's training fold is visible. A hard negative shares a stem,
    substring, prefix or compound with its counterpart in the person's ledger;
    similarity orders those examples, never guesses their label. Canaries have
    already been removed by model_rows().
    """
    training = without_canaries(training)
    hard = [r for r in training if is_hard_negative(r)]
    hard.sort(key=lambda r: (-SequenceMatcher(None, fold(r["first"]),
                                                  fold(r["second"])).ratio(), r["id"]))
    selected = hard[:min(2, k)]
    remaining = [r for r in training if r["id"] not in {s["id"] for s in selected}]
    # Both decisions remain represented even when the hard examples fill the
    # negative side. Stable IDs, not ledger insertion order, choose the rest.
    remaining.sort(key=lambda r: baseline.digest(r["id"]))
    if len(selected) < k and not any(r["decision"] == "one-term" for r in selected):
        positive = next((r for r in remaining if r["decision"] == "one-term"), None)
        if positive:
            selected.append(positive)
            remaining.remove(positive)
    return (selected + remaining)[:k]


def canaries() -> list[tuple[str, str]]:
    return list(MUST_NOT_MERGE)


def pair_key(row: dict) -> tuple[str, str]:
    """The two surfaces are unordered; fold() ignores their spelling variants."""
    return tuple(sorted((fold(row["first"]), fold(row["second"]))))


def without_canaries(labelled: list[dict]) -> list[dict]:
    """Exclude every spelling of a never-merge pair before model training."""
    held_out = {pair_key({"first": a, "second": b}) for a, b in canaries()}
    return [r for r in labelled if pair_key(r) not in held_out]


def canary_pair(row: dict) -> bool:
    """Whether a ledger row is one of the never-merge pairs, in either order and any spelling."""
    return pair_key(row) in {pair_key({"first": a, "second": b}) for a, b in canaries()}


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
    """Keep repeated surface pairs together, while balancing decision counts."""
    if k < 2:
        raise ValueError("fold count must be at least two")
    groups: dict[tuple[str, str], list[dict]] = {}
    for row in labelled:
        groups.setdefault(pair_key(row), []).append(row)
    for key, group in groups.items():
        if len({r["decision"] for r in group}) != 1:
            raise ValueError(f"conflicting judgements for surface pair {key!r}")
    out: list[list[dict]] = [[] for _ in range(k)]
    counts = [{decision: 0 for decision in trainset.DECIDED} for _ in range(k)]
    for decision in trainset.DECIDED:
        ordered = sorted((group for group in groups.values() if group[0]["decision"] == decision),
                         key=lambda group: baseline.digest(pair_key(group[0])))
        for group in ordered:
            i = min(range(k), key=lambda index: (counts[index][decision], len(out[index]), index))
            out[i].extend(sorted(group, key=lambda r: r["id"]))
            counts[i][decision] += len(group)
    return [f for f in out if f]


def merged_canaries(rule) -> list[tuple[str, str]]:
    """The never-merge pairs a rule merges. Any one of them vetoes it."""
    return [(a, b) for a, b in canaries() if rule(a, b) == "one-term"]


def check_program_canaries(compiled, first, *, name: str, approval: str | None,
                           out_dir: Path | None, lms: list | None = None, shown=None,
                           threads: int = 1) -> list[str]:
    """Veto a merge or an answer that cannot establish a canary stayed separate.

    Each canary is asked once per LM in `lms` — one per repeat, so as often as a
    held-out pair (P18) — each call on its own copy of that LM when calls run in
    parallel. `shown(a, b)` builds the program's inputs, evidence included. `name`
    is an optimizer's name or a run's step, `pairs-…`, which names the record."""
    import contextlib
    from concurrent.futures import ThreadPoolExecutor
    import dspy
    from lmrun import call
    lms = lms or [None]
    shown = shown or (lambda a, b: {"first": a, "second": b})
    step = f"{name}-canary" if name.startswith("pairs-") else f"pairs-{name}-canary"
    failures = [f"{a}/{b}: rule merged" for a, b in canaries() if first(a, b) == "one-term"]
    asked = [(a, b, lm) for a, b in canaries() if first(a, b) != "one-term" for lm in lms]

    def ask(item):
        a, b, lm = item
        own = lm.copy() if lm is not None and threads > 1 and type(lm).__name__ != "FixtureLM" else lm
        with dspy.context(lm=own) if own is not None else contextlib.nullcontext():
            pred, rec = call(compiled, step=step, subject="surface-pairs", approval=approval,
                             out_dir=out_dir, **shown(a, b))
        if rec["status"] != "answered":
            return f"{a}/{b}: {rec['status']}"
        return None if str(pred.decision) == "two-terms" else f"{a}/{b}: merged"

    with ThreadPoolExecutor(max(1, threads)) as pool:
        failures += [f for f in pool.map(ask, asked) if f]
    return failures


def score_rule(name: str, labelled: list[dict] | None = None) -> dict:
    """The rule's row on the whole ledger, or on the rows a model run used — a
    model's row is compared with the floor scored on the same rows."""
    import inspect
    rule = RULES[name]
    labelled = rows() if labelled is None else labelled
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
    labelled = model_rows()
    if any(pair_key(r) in {pair_key({"first": a, "second": b}) for a, b in canaries()}
           for r in labelled):
        failures.append("a canary reached the model trainset")
    variant = {"id": "canary-variant", "first": "die Negentropie",
               "second": "ENTROPIE", "decision": "two-terms", "features": []}
    if without_canaries([variant]) or labeled_demos([variant], k=1):
        failures.append("a spelling variant of a canary reached training or demos")
    for held in folds(labelled, 5):
        training = [r for r in labelled if r["id"] not in {h["id"] for h in held}]
        if {pair_key(r) for r in held} & {pair_key(r) for r in training}:
            failures.append("a held-out surface pair reached training")
        demos = labeled_demos(training)
        if {r["id"] for r in demos} & {r["id"] for r in held}:
            failures.append("a held-out row reached the labeled demos")
        if sum(is_hard_negative(r) for r in demos) < 2:
            failures.append("a fold's demos omitted hard negatives")
        if demos != labeled_demos(list(reversed(training))):
            failures.append("demo choice depends on ledger order")
    if {frozenset(r["id"] for r in held) for held in folds(labelled, 5)} != \
            {frozenset(r["id"] for r in held) for held in folds(list(reversed(labelled)), 5)}:
        failures.append("fold assignments depend on ledger order")
    # A future contradictory judgement must stop a run before any model calls.
    contradiction = dict(labelled[0], id="conflicting-test",
                         decision="two-terms" if labelled[0]["decision"] == "one-term"
                         else "one-term")
    try:
        folds(labelled + [contradiction], 5)
    except ValueError as exc:
        if "conflicting judgements" not in str(exc):
            failures.append(f"unexpected conflict error: {exc}")
    else:
        failures.append("contradictory judgements reached model folds")
    if not canary_pair({"first": "Entropie", "second": "Negentropie"}):
        failures.append("the canary Negentropie/Entropie is not recognised in the other order")
    if canary_pair({"first": "Riss", "second": "Risse"}):
        failures.append("a pair the ledger merges was taken for a canary")
    return failures, len(merges) + 1 + len(too_far) + 9


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
    """Compile per fold, ask each fold's program the canaries, score each held-out row
    `repeats` times, compile once more on every row and ask that program the canaries.
    `threads` runs the calls in parallel, each on its own copy of the LM, so
    `lmrun.call` reads only its own call's history. `score=False` skips the folds:
    one compile, the canaries, the program saved, and no row (`pairs.py final`)."""
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
    labelled = model_rows()  # includes no canary, even when a canary has a ledger row

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

    demo_ids = []

    def compile_on(training: list[dict]):
        if name == "labeled":
            chosen = labeled_demos(training)
            demo_ids.append([r["id"] for r in chosen])
            compiled = optimizer(name, metric, len(chosen), reflection_lm, gepa_calls).compile(
                program.deepcopy(), trainset=[examples[r["id"]] for r in chosen], sample=False)
            if [d.id for d in compiled.predictors()[0].demos] != demo_ids[-1]:
                raise RuntimeError("LabeledFewShot did not keep the selected demos")
            return compiled
        return optimizer(name, metric, len(training), reflection_lm, gepa_calls).compile(
            program.deepcopy(), trainset=[examples[r["id"]] for r in training])

    def canaries_of(compiled) -> list[str]:
        return check_program_canaries(compiled, first, name=step, approval=approval, out_dir=out_dir,
                                      lms=per_repeat, shown=lambda a, b: inputs({"first": a, "second": b}),
                                      threads=threads)

    outcomes: dict[str, float | None] = {}
    compiled_states = []
    canary_failures = []
    with context:
        for fold_number, held in enumerate(folds(labelled, k) if score else [], 1):
            held_ids = {r["id"] for r in held}
            compiled = compile_on([r for r in labelled if r["id"] not in held_ids])
            compiled_states.append(compiled.dump_state())
            canary_failures.extend(f"fold {fold_number}: {failure}" for failure in canaries_of(compiled))
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
        final = compile_on(labelled)
        canary_failures.extend(f"final: {failure}" for failure in canaries_of(final))
        if not dry_run:
            save_program(final, step, rule, canary_failures, compiled_states)

    # every call this run made, compile included: DSPy's global history holds each LM's
    # entries with the cost its response reported (claude_lm: the CLI's total_cost_usd)
    cost = round(sum(e.get("cost") or 0.0 for e in list(GLOBAL_HISTORY)
                     if str(e.get("timestamp", "")) >= started), 4)
    unscored = sum(v is None for v in outcomes.values())
    entry = baseline.row(TASK, f"{'dry-run:' if dry_run else ''}rule:{rule}+{label}:{model or 'fixture'}",
                         outcomes, program=[inspect.getsource(first), inspect.getsource(fold),
                                            inspect.getsource(pair_key), inspect.getsource(without_canaries),
                                            inspect.getsource(folds),
                                            *([inspect.getsource(is_hard_negative),
                                               inspect.getsource(labeled_demos)]
                                              if name == "labeled" else []),
                                            *([inspect.getsource(evidence)] if with_evidence else []),
                                            compiled_states],
                         trainset=labelled, vetoed=bool(canary_failures), cost=cost,
                         note=f"k={k} repeats={repeats}; labeled demos per fold and final: "
                              f"{demo_ids}; canary failures: {canary_failures}; {unscored} rows not scored; "
                              f"reflection {reflection or '-'}")
    if record and not dry_run and score:
        # the floor on the same rows, so `baseline.compare` can read the two against each other
        current = baseline.digest(labelled)
        if not any(r["candidate"] == f"rule:{rule}" and r["trainset_hash"] == current
                   for r in baseline.rows(TASK)):
            baseline.append(score_rule(rule, labelled))
        baseline.append(entry)
    return entry


PROGRAMS = ROOT / "Plan" / "runs" / "surface-pairs" / "programs"


def save_program(program, step: str, rule: str, failures: list, folds: list | None = None) -> Path:
    """The final compile of a real run, as DSPy dumps it — the demos an optimizer chose, the
    instructions it wrote, InferRules' rules, GEPA's text — and each fold's program, which
    is what scored the held-out pairs. Until 2026-09-25 nothing kept either, so the first
    InferRules run's rules left with its process."""
    from datetime import datetime, timezone
    PROGRAMS.mkdir(parents=True, exist_ok=True)
    target = PROGRAMS / f"{step}.json"
    signature = getattr(program, "signature", None)
    target.write_text(json.dumps({
        "step": step, "rule_first": rule, "canary_failures": failures,
        "at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "instructions": getattr(signature, "instructions", None),
        "demos": len(getattr(program, "demos", []) or []),
        "state": program.dump_state(),
        "folds": folds or [],
    }, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
    return target


def report(floor: str = "plural") -> list[str]:
    """Every row of this task, split by direction, each read against its own pairs.

    A score mixes the two errors this task has, and they are not worth the same: a
    merge the rule missed and the model found is recall, a pair the ledger keeps
    apart and the model merged is a **false merge** — the kind the canaries exist
    for. So each row is read against the rule named by `floor`, over the pairs the
    row itself scored: the ones the rule leaves, how many of their gold merges the
    candidate found, how many of their gold splits it kept, and every pair it merged
    against the ledger, by id. Rows are grouped by the pairs they were scored on,
    because the ledger grows and the harness changes, and a row stays what it
    measured."""
    ledger = {r["id"]: r for r in rows()}
    groups: dict[str, list[dict]] = {}
    for row in baseline.rows(TASK):
        groups.setdefault(row["trainset_hash"], []).append(row)
    lines = []
    for digest, group in groups.items():
        ids = [i for i in group[-1]["outcomes"] if i in ledger]
        left = [i for i in ids if RULES[floor](ledger[i]["first"], ledger[i]["second"]) != "one-term"]
        merges = [i for i in left if ledger[i]["decision"] == "one-term"]
        splits = [i for i in left if ledger[i]["decision"] == "two-terms"]
        lines.append(f"on {len(ids)} pairs ({digest}): the rule {floor!r} leaves {len(left)}, "
                     f"{len(merges)} gold one-term, {len(splits)} gold two-terms")
        for row in group:
            got = row["outcomes"]
            if not all(i in got for i in left):
                continue
            found = sum(got[i] or 0 for i in merges)
            kept = sum(got[i] or 0 for i in splits)
            false = sorted((i for i in splits if got[i] is not None and got[i] < 1), key=lambda i: got[i])
            unscored = sum(got[i] is None for i in left)
            flag = "  VETOED" if row["vetoed"] else ""
            missed = [i for i in splits if canary_pair(ledger[i]) and got[i] is not None and got[i] < 1]
            if missed and not row["vetoed"]:
                flag += f"  CANARY MERGED IN A HELD-OUT REPEAT ({', '.join(missed)}) — not vetoed when recorded"
            lines.append(f"  {row['candidate']:<54} {row['score'] if row['score'] is not None else '—':>6}  "
                         f"merges found {found:5.2f}/{len(merges)}  kept apart {kept:5.2f}/{len(splits)}  "
                         f"${row.get('cost') or 0:.2f}{flag}"
                         + (f"  unscored {unscored}" if unscored else "")
                         + "".join(f"\n        false merge {i} {got[i]:.2f}: {ledger[i]['first']} / "
                                   f"{ledger[i]['second']}" for i in false))
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
              f"(plural merges, no canary merged, the veto fires on -er and on case, canaries out of "
              f"training, folds and demos, a canary pair known in either order)")
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
