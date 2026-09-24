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
    .venv-dspy/bin/python scripts/pairs.py run --optimizer labeled [--rule plural] --dry-run
    .venv-dspy/bin/python scripts/pairs.py run --optimizer inferrules --rule plural \\
        --model openrouter/… --approval "<the author's decision>" [--folds 5] [--repeats 3] [--record]

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
    return failures, len(merges) + 1 + len(too_far)


# --- the model half: imported only when a model is asked for ---------------------

def program_and_metric():
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

    return dspy.Predict(SameTerm), metric


def optimizer(name: str, metric, train_size: int, reflection_lm=None):
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
        return dspy.GEPA(metric=metric, auto="light", reflection_lm=reflection_lm, seed=0,
                         track_stats=True)
    raise SystemExit(f"unknown optimizer {name!r}: labeled, bootstrap, inferrules, simba, gepa")


def run(name: str, model: str | None, approval: str | None, k: int, repeats: int,
        dry_run: bool, record: bool, reflection: str | None, rule: str = "fold") -> dict:
    import inspect
    import tempfile
    import dspy
    from lmrun import call, make_lm

    first = RULES[rule]           # asked before the model, so the model sees only its residual
    labelled = rows()
    examples = {r["id"]: dspy.Example(**r).with_inputs("first", "second") for r in labelled}
    program, metric = program_and_metric()

    if dry_run:
        from lm_fixture import FixtureLM, fill, offline
        lm = FixtureLM(fill(decision="two-terms", rule="Probelauf: immer zwei Begriffe."))
        context = offline(lm)
        out_dir = Path(tempfile.mkdtemp())
    else:
        if not (model and approval):
            raise SystemExit("a real run needs --model and --approval naming the author's decision")
        context = dspy.context(lm=make_lm(model))
        out_dir = None
    reflection_lm = lm if dry_run else (make_lm(reflection) if reflection else None)

    outcomes: dict[str, float | None] = {}
    compiled_states = []
    with context:
        for held in folds(labelled, k):
            held_ids = {r["id"] for r in held}
            train = [examples[i] for i in examples if i not in held_ids]
            compiled = optimizer(name, metric, len(train), reflection_lm).compile(
                program.deepcopy(), trainset=train)
            compiled_states.append(compiled.dump_state())
            for r in held:
                if first(r["first"], r["second"]) == "one-term":
                    outcomes[r["id"]] = float(r["decision"] == "one-term")   # the rule answers
                    continue
                hits = []
                for _ in range(repeats):
                    pred, rec = call(compiled, step=f"pairs-{name}", subject="surface-pairs",
                                     approval=approval, german=["rule"], out_dir=out_dir,
                                     first=r["first"], second=r["second"])
                    if rec["status"] == "answered":
                        hits.append(trainset.score_one(r, str(pred.decision))["score"])
                outcomes[r["id"]] = round(sum(hits) / len(hits), 3) if hits else None
        merged = []
        final = optimizer(name, metric, len(examples), reflection_lm).compile(
            program.deepcopy(), trainset=list(examples.values()))
        for a, b in canaries():
            if first(a, b) == "one-term":
                merged.append((a, b))
                continue
            pred, rec = call(final, step=f"pairs-{name}-canary", subject="surface-pairs",
                             approval=approval, out_dir=out_dir, first=a, second=b)
            if rec["status"] == "answered" and str(pred.decision) == "one-term":
                merged.append((a, b))

    entry = baseline.row(TASK, f"{'dry-run:' if dry_run else ''}rule:{rule}+{name}:{model or 'fixture'}",
                         outcomes, program=[inspect.getsource(first), inspect.getsource(fold),
                                            compiled_states],
                         trainset=labelled, vetoed=bool(merged),
                         note=f"k={k} repeats={repeats}; canaries merged: {merged}")
    if record and not dry_run:
        baseline.append(entry)
    return entry


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
              f"(plural merges, no canary merged, the veto fires on -er and on case)")
        return 1 if problems else 0
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
                    "--dry-run" in argv, "--record" in argv, opt("--reflection-model"), rule)
        print(json.dumps({k: entry[k] for k in ("candidate", "n", "scored", "correct", "score",
                                                "vetoed", "note")}, ensure_ascii=False, indent=1))
        return 1 if entry["vetoed"] else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
