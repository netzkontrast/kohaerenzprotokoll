# Metrics, judges, and the checks that cannot fail

This file is about scoring: the one metric this repository has written, what a
judge is worth and how it is gamed, and the finding that repeats across the nine
repositories — a check that returns a perfect score on nothing to check. Signature
and `dspy.Evaluate` facts already stated in `api.md` are not repeated here; this
file points to it.

## In this repository

**The only metric that exists is `pairs.py`'s, and it is a thin wrapper around
`trainset.score_one`.**

```python
def metric(example, pred, trace=None, pred_name=None, pred_trace=None):
    judged = trainset.score_one(example.toDict(), str(getattr(pred, "decision", "")))
    return dspy.Prediction(score=judged["score"], feedback=judged["feedback"])
```

`scripts/pairs.py`. `score_one` itself is standard library, returns a
plain `dict`, not a `Prediction` — the wrapping happens once, at the metric
boundary, in `pairs.py`:

```python
def score_one(gold: dict, predicted: str):
    """GEPA-shaped: a score and the human's words for why, not a bare float."""
    hit = predicted.strip().lower() == gold["decision"]
    return {
        "score": 1.0 if hit else 0.0,
        "feedback": ("correct" if hit else
                     f"wrong: {gold['first']!r} / {gold['second']!r} is "
                     f"{gold['decision']}, because {gold['rule']}"),
    }
```

`scripts/trainset.py`. **The feedback on a miss is not generated — it is
the recorded human's own sentence for why**, read out of `gold["rule"]`, which
came from a person deciding that exact pair in `Plan/runs/judgements.jsonl`. No
model writes this text and none can fake it (`scripts/trainset.py`).

**Could-not-score is `null`, never `0`.** `baseline.row()` takes an `outcomes`
map of `{id: 1 | 0 | fraction | None}` and computes `scored = [v for v in
outcomes.values() if v is not None]` (`scripts/baseline.py`) — an example
nothing could answer is invisible to the mean, not a zero inside it. `pairs.py
run()` writes exactly this: a held-out row `fold()` does not settle goes to the
model, and scores `None` when no repeat through `lmrun.call` came back
`answered` (`scripts/pairs.py`).
`baseline.compare()` reports `"unscored"` when the latest row's score is `None`
at all, and `"warn"` — never a passing score — when `scored < n`
(`scripts/baseline.py`).

**The canary veto is separate from the score, and it wins regardless of it.**
`selftest.MUST_NOT_MERGE` — four pairs, `Negentropie`/`Entropie` first — is asked
of every rule and every compiled program, never trained on
(`scripts/selftest.py`). `score_rule()` checks a deterministic rule
candidate against the canaries and records `vetoed=bool(merged)`
(`scripts/pairs.py`); `run()` does the same against the final compiled
program (`scripts/pairs.py`). `baseline.compare()` returns `"fail"` for
a vetoed row whatever its score (`scripts/baseline.py`) — a candidate that
merges the canary is disqualified, not docked `1/n`, because `dspy.GEPA`
optimizes a mean and would otherwise treat the merge as noise.

**The floor is a named row, not "whatever ran last."** `compare(task, floor=)`
defaults to the task's first recorded candidate and takes that candidate's
newest row on the same trainset; when there is none it answers `warn` —
"re-score the floor before comparing" — instead of a verdict
(`scripts/baseline.py`). Until 2026-09-24 it took the candidate's oldest row,
so re-scoring could never clear that warning (`optimizers.md`, *What
`baseline.py compare` says*). `--floor` names a
different candidate. The first floor is `fold()` itself, scored through
`score_rule("fold")`: **67 <!--state:pairs.labelled--> labelled pairs; `fold()`
decides 40 <!--state:pairs.fold_correct--> of them (57%).** `trainset.py`'s own
output: "Anything that does not beat this is not worth an LM call."
(`scripts/trainset.py`). A model run after the plural rule answers to a higher
one, `rule:plural`, which decides 48 <!--state:pairs.plural_correct-->
(decision 010). No optimizer rung has run against a real model yet
(`CLAUDE.md`, *Calling a model*), so `Plan/runs/baselines.jsonl` holds no
model row: its rows are `rule:fold`, `rule:plural` and `graphrag.py bench`'s
retrieval methods.

**The two-reader ceiling is F1 ≈ 0.66, and both scripts that score a model list
say so.** Both readers were Claude sessions (P27, corrected 2026-09-24), and F1
between two lists moves with how much each lists: `scripts/agree.py` prints
containment beside it. `entities.py cmd_score()` computes
precision/recall/F1 for a model's entity list against a reader's, then prints
`"— two readers scored 0.66 (P27)"` on the same line
(`scripts/entities.py`) and lists both difference sets by name, never a bare
delta (`scripts/entities.py`, P27). `rlm_ingest.py score()` scores through
`drg-kg`'s `_score_sets`, prints both difference lists, and gives P27's second
measurement instead of the 0.66: "A miss is not automatically an
error and an invention is not automatically wrong: the reader's list is one
reader. Two independent readings of one document differed by 109 against 143
candidates." (`scripts/rlm_ingest.py`). Neither script treats the "gold"
list as truth — a model at 0.66 is *at* the ceiling, and one clearly above it is
most likely fitted to a single reader (P27).

## The contract

**Five arguments, `dspy.Prediction(score, feedback)` out.** Signature-level facts
— what `dspy.Evaluate` does with the return value, why a `dict` crashes it, why
a percentage is not a fraction — are in `api.md`; this section is about what the
*function* must do, not the call site.

**An optional sixth argument, `program_trace`, exists for `dspy.Flex`.** DSPy
3.3.1's `GEPAFeedbackMetric` protocol adds `program_trace: Optional[DSPyTrace] =
None` after `pred_trace`, "supplied at scoring time when a `dspy.Flex` submodule
is being optimized. Declare this parameter to score against how an answer was
produced … rather than only whether it was correct. Unlike `trace`, it is
populated during candidate *scoring*." (`dspy:teleprompt/gepa/gepa.py:28-49`).
The return type widens to `ScoreWithFeedback`, a `Prediction` subclass adding
`objective_scores: dict[str, float] | None`
(`dspy:teleprompt/gepa/gepa_utils.py:57-60`). Nothing here declares a sixth
parameter or uses `dspy.Flex`.

**A dict crashes `dspy.Evaluate`.** [checked: metric-dict-crashes] A metric
returning `{"score": 1.0, "feedback": "x"}` raises `TypeError: unsupported
operand type(s) for +: 'int' and 'dict'` the moment `Evaluate` tries to sum
scores. Every metric-writing rule in the nine repositories says not to do this,
and one repository's own guard cannot catch it: `dspy-auto-gepa`'s
`_validate_metric_source` rejects only a literal `return {…}`
(`ast.Dict`), so `return dict(score=...)` — the exact same crash, spelled
differently — passes the guard silently
(`dspy-auto-gepa:src/dspy_auto_gepa/metric_builder.py:245-271`).

**A `Prediction(score, feedback)` metric aggregates correctly under `Evaluate`.**
[checked: metric-prediction-aggregates] `.score` still comes out a percentage,
same as a bare float would. But it is **not** safe to hand a `Prediction`
metric to `BootstrapFewShot` or its relatives: `bool(dspy.Prediction(score=0.0))`
is `True`, so a bootstrap-family optimizer that filters demos by truthiness keeps
every wrong one. Measured: an all-wrong run kept 4 of 4 wrong demos with a
`Prediction` metric, 0 of 4 with a float metric, and 0 with `metric_threshold=0.5`
added back (`dspy:teleprompt/bootstrap.py:204-212`, verified offline).
`dspy-agent-skills:skills/dspy-optimizer-selection/SKILL.md:121`'s "everything
else (the score is read)" is wrong about this exact case. `pairs.py`'s own
`optimizer()` already gets this right without stating the rule: `bootstrap`,
`inferrules` and `simba` each wrap the metric as `lambda e, p, t=None: metric(e,
p).score` (a bare float), and only `gepa` receives the `Prediction`-returning
`metric` directly (`scripts/pairs.py`). See `optimizers.md` for
the ladder-wide consequence.

**Feedback is text an optimizer can act on, not a number.** A binary metric
gives an optimizer no gradient to climb — "a metric an optimizer can climb takes
more than two distinct values"
(`dspy-agent-skills:skills/dspy-book-metrics/SKILL.md:48-62`). `dspy-auto-gepa`'s
own metric-writing prompt asks for "2-5 lines of actionable, specific critique
per issue" (`dspy-auto-gepa:src/dspy_auto_gepa/metric_builder.py:23-25`); this
repository's feedback is one sentence, but it is never generated — it is the
actual reason a person gave (above). `score_one` never scores the `rule` output
field `SameTerm` produces alongside `decision` — only the decision is compared.
A model's stated rule is read by a person, never checked against the gold rule
by code (P4: no scored axis without an instance asking for one).

**`pred_name` carries the blame in a multi-predictor program.** The recipe —
branch on `pred_name`, never on `trace`, because `trace is not None` also fires
inside `BootstrapFewShot` where `pred_trace` is unset and subscripting it raises
— is `dspy-agent-skills:skills/dspy-book-metrics/reference.md:143-163`, and the
reverse mistake is measured: a metric that tests `if trace is None and pred_name
is None` breaks `BootstrapFewShot` outright: it aborts after 10 metric errors
(`dspy-agent-skills:skills/dspy-book-metrics/reference.md:145-155`; the limit is
`max_errors=10`, `dspy:dsp/utils/settings.py:32`, `dspy:teleprompt/bootstrap.py:216-220`; verified:
`boot1.py`, `gepa1.py`). `pairs.py`'s `SameTerm` is a single `dspy.Predict`, so
`pred_name` is always `None` in every call this repository makes; the recipe
waits for a multi-predictor program.

## Could-not-score and failing cases

**Every metric here ships a case in which it must fail**, and the reason is not
local doctrine — it is the one finding that repeats across all nine
repositories, and it is this project's own founding defect restated nine times:
a coverage term returning 1.0 when passed no gold, never once passed any
(`scripts/selftest.py`). `scripts/baseline.py selftest()` proves `compare()`
itself can fail for each of its own reasons — `unscored`, `fail` (does not beat
the floor), `fail` (vetoed), `ok`, `warn` (not fully scored), `warn` (trainset
changed) — asserting the *reason string*, not just the verdict
(`scripts/baseline.py`). `scripts/selftest.py`'s `MUST_NOT_MERGE` /
`MUST_MERGE` do the same for `fold()`, and `quotes.py` / `read.py --find` carry
six quotation and three citation cases built the same way. `testing.md` has the
full inventory; this section says why the doctrine exists rather than restating
each case (P6).

**"Could not score" is a third state everywhere in this repository, and it is
not what most metric code defaults to.** `lmrun.py` records one of four
statuses per call — `answered`, `refused`, `unparsed`, `unreachable` — never a
score (P15). `baseline.py` writes `null`, never `0`, into `outcomes` for an
unscorable example. `dspy.Evaluate`'s own default, `failure_score=0.0`, is the
opposite choice, and nothing here reads its aggregate as a measurement:
`pairs.py` scores each held-out example through `lmrun.call` and writes `null`
itself (`api.md`).

**Six of the nine repositories fold "could not score" into a real-looking
number, each differently:**

- `dspy-auto-gepa`'s row judge returns `JudgeResult(0.0, "LLM judge call
  failed")` on a call failure and `0.0, "Failed to parse judge output"` on a
  parse failure — the same score both times, distinguished only by a message
  string nothing downstream reads (`dspy-auto-gepa:src/dspy_auto_gepa/quality.py:136-226`,
  verified: repo tests pass).
- `dspydantic`'s `ScoreJudge` and `default_judge_fn` both cascade to **0.5** on
  unparseable judge text — the same value a genuinely mediocre judgement would
  give (`dspydantic:src/dspydantic/evaluators/score_judge.py:105-131`,
  `dspydantic:src/dspydantic/evaluators/functions.py:127-161`, verified:
  `'{"score": "high"}'` → 0.5, `'The extraction is 100% correct'` → 0.5).
- `dspy-session`'s `on_metric_error="zero"` and a metric returning a bare
  `None` both become `0.0`, indistinguishable from a genuinely wrong answer
  (`dspy-session:dspy_session/session.py:1111-1135`, verified).

## Recipes by output shape

`dspy-agent-skills:skills/dspy-book-metrics/SKILL.md:31-46` and
`example_metric_recipes.py:24-35` give a routing table from output shape to
recipe; it is reproduced here because nothing else in this skill states it, and
the recipe used depends on what job 1 or job 2 eventually needs.

| output shape | recipe | the trap in it |
|---|---|---|
| one canonical short answer | `dspy.evaluate.answer_exact_match` | "The capital is Paris." fails against gold `"Paris"` |
| required structure, free wording | regex, binary or partial credit | none stated; the honest baseline |
| a set of required points | keyword overlap, `\b`-bounded | without the boundary, `car` matches `carbon` |
| OCR / spelling | Levenshtein ≤ threshold | only fits OCR/spelling; `good`/`goof` is 1 edit |
| paraphrase of a known answer | embedding cosine, unbinarized | blind to negation — see below |
| extractive span | token F1 | rewards overlap, not correctness — the same negation trap |
| translation / summary | BLEU / ROUGE | weaker than embeddings; still worth a fast sanity check |
| subjective quality | judge calibrated on human labels | untrusted below 80% agreement — see *Judges* |
| several independent axes | weighted rubric, weights sum to 1.0 | see *Composite and rubric scores* |
| multi-step pipeline | trace-aware per-predictor feedback | branch on `pred_name`, never on `trace` (above) |

**Overlap metrics reward a reversed fact.** The book's own measured example:
token F1 between `"the treaty was signed"` and `"…not signed"` scores 0.89
(`dspy-agent-skills:skills/dspy-book-metrics/reference.md:70-92`). No overlap
metric — token F1, BLEU, ROUGE, cosine similarity — sees a negation; only an
exact match or a judge does. This repository's own canary,
`Negentropie`/`Entropie`, is the same shape in one word: two terms whose
surfaces are close and whose meanings are opposite (`Not taken`, below).

## Judges

**Calibration protocol** — the one sequence in the nine repositories with a
stated trust bar, `dspy-agent-skills:skills/dspy-book-metrics/SKILL.md:64-84`
and `reference.md:94-119`: label by hand with a metric that always asks *why*
and blocks on input ("'Why' is more valuable than 'Yes/No' for LLMs"),
`num_threads=1`, append every label to JSONL as you go; 20–50 labels, more if
subtle; a judge `Signature` with `is_good: bool` and `reasoning: str`; optimize
on 80%; **measure agreement on the held-out 20% before trusting it** — "Do not
skip step 5. An uncalibrated judge is an unfalsifiable metric." Nothing here has
a judge yet. If job 1 or job 2 ever adds one, this is the protocol — and P27's
ceiling matters for setting the trust bar realistically for *this* corpus: a
German near-match task between two independent readers already disagrees by
about a third (P27), so the book's 80–90% agreement bar may be optimistic for a
task this hard, not a floor to clear easily.

**Agreement is not chance-corrected.** "80% on a balanced binary task is closer
to 60% corrected" — Cohen's κ = (0.8 − 0.5) / (1 − 0.5) = 0.6
(`dspy-agent-skills:skills/dspy-book-metrics/reference.md:121-123`, verified:
the arithmetic). Treat the book's 80–90% bar as a floor, not a ceiling.

**Gaming a judge, measured four ways in one pattern collection**
(`dspy-agent-skills`, the seven knowledge-work patterns):
- a negation backstop fails a criterion phrased negatively — "No regressions in
  existing functionality." restated as "There are no regressions…" is marked
  failed, while a sloppy "all tests pass" claim passes on 2 of 4 keywords
  (`dspy-agent-skills:skills/dspy-autodialectics/example_autodialectics.py:67,138-153`,
  verified: probes AD1, AD1b);
- declared uncertainties buy the "unsupported claims" score down to zero —
  three declared uncertainties turn a 1.0 into 0.0 regardless of whether the
  claims were actually supported
  (`dspy-agent-skills:skills/dspy-autodialectics/example_autodialectics.py:190,194,201`,
  verified: probes AD2, AD7);
- feedback names a number, never a cause — the code emits `"fake_completion
  1.00; unsupported_claims 1.00; …"` where the docs promise "fake completion:
  'done' claimed with no test results or files"
  (`dspy-agent-skills:skills/dspy-autodialectics/example_autodialectics.py:214-215`,
  verified: dry-run output);
- an empty output is low-slop: `Output(text="")` scores composite 0.175, i.e.
  **0.825** ("low slop"), because `requirement_drift` and `fake_completion` are
  the only dimensions an empty string can trip
  (`dspy-agent-skills:skills/dspy-autodialectics/example_autodialectics.py:176-177`,
  verified: probe AD8b).

**Position and length bias.** `dspy-agent-skills:skills/dspy-book-metrics/SKILL.md:122-129`
names both as additions the book itself does not cover. The one built defence
against position bias in the nine repositories is a randomized-position
pairwise judge: `swap = random.random() < 0.5; candidate_won = (verdict == ("A"
if not swap else "B"))`
(`dspy-agent-skills:skills/dspy-book-coding-agents/reference.md:46-64`) — the
pattern to reuse if a pairwise judge is ever built here.

**When a pattern table beats a judge.** "The quickstart notebook replaces the
LLM judge with a table of roughly eighteen compiled regex patterns for known
tells, scoring zero on any hit and naming the matched patterns in its feedback
string. It costs nothing, never drifts, and the feedback is more specific than a
judge's. Reach for a judge when the quality you want cannot be written as a
pattern — not before."
(`dspy-agent-skills:skills/dspy-book-eight-steps/SKILL.md:76-84`,
`reference.md:80-90`). This repository already has its own instance of exactly
this rule, built before the recipe was read: `fold()` decides
40 <!--state:pairs.fold_correct--> of 67
<!--state:pairs.labelled--> pairs for free, the plural rule of decision 010
decides 48 <!--state:pairs.plural_correct-->, and `pairs.py` sends a model only
the residual the rule named by `--rule` calls two-terms (P1).

**Deterministic gate before the judge.** The financial-analyst recipe — parse
the number, a close-enough check that never calls the judge on a wrong or
unparseable answer, only *then* grade the trajectory
(`dspy-agent-skills:skills/dspy-book-use-cases/SKILL.md:65-77`,
`example_use_case_router.py:61-90`, verified dry-run: wrong and unparseable
answers make zero judge calls) — is the same shape as two things already built
here: `pairs.py`'s rule-first routing (above), and `rlm_ingest.py`'s two-tier
verification, where a candidate must first cite a line that actually contains
it (Tier 1) before its *reach* across the document is even measured (Tier 2)
(`scripts/rlm_ingest.py`). Cheap check first, expensive check
second, in both cases.

## Composite and rubric scores

**Normalisation.** The weighted-rubric recipe: one `Signature` per axis (each an
`int` 1–5 with its own description), explicit weights as module constants
summing to 1.0, `normalized = (score - 1) / 4.0`, and "score your
known-best and known-worst examples and confirm they land where you expect"
(`dspy-agent-skills:skills/dspy-book-metrics/SKILL.md:86-100`,
`reference.md:125-141`, verified: best 1.00, worst 0.00, mixed 0.55, weights not
summing to 1 raise).

**Report each axis — P11.** "Never collapse several checks into one pass/fail
bit. Report each check's own status. A single green light hides which of nine
things was actually verified." The wiki-compile metric in `dspy-agent-skills`
is a composite of exactly this shape — five weighted axes, 0.30 citations /
0.25 decisions / 0.20 merge / 0.15 diffs / 0.10 links
(`dspy-agent-skills:skills/dspy-wiki-compile/example_wiki_compile.py:161-170,224-237`)
— and it is P11's violation made concrete: `_mean([])` returns 1.0, so four of
the five axes score perfect when there is nothing to check on them, and an
empty compile scores **0.70** with feedback "clean" (verified: dry-run). The
tetraframe pattern's verification suite hides the same way from the other
direction: it is a mean over seven checks with named thresholds, and a run
whose contradiction-honesty check falls below its own threshold (0.25 < 0.75)
still scores 0.893 overall
(`dspy-agent-skills:skills/dspy-tetraframe/example_tetraframe.py:233-236`,
verified: probes T5, T5b, T6) — one number hides which check failed, exactly
what P11 forbids. `baseline.py`'s own reporting — `score`, `scored` and `n`
always printed together, never folded into one figure
(`scripts/baseline.py`) — is this repository's answer to P11 at the
metric-ledger level, not inside a single metric function.

**Two encodings of "mean of nothing" disagree, inside one repository.** The
wiki-compile pattern's `_mean([])` is 1.0; the tetraframe pattern's is 0.0 for
the same shape of gap (`dspy-agent-skills:skills/dspy-wiki-compile/example_wiki_compile.py:161-163`
against `skills/dspy-tetraframe/example_tetraframe.py:142-144`, verified: read).
A composite's empty-case behaviour is a decision, and an untested one — P6: one
encoding per rule, and a self-test that proves which one is intended.

## Evaluator registries in the nine repositories

| repository | registry | members | what an unscoreable case returns |
|---|---|---|---|
| `dspydantic` | `EvaluatorFactory.create` / `EVALUATOR_REGISTRY` | `exact`/`string_check`, `levenshtein`, `text_similarity`, `score_judge`/`score_model_grader`, `label_model_grader`, `python_code`, `predefined_score` | 0.5 on a judge parse failure; rebuilt fresh **per call**, so no evaluator's state survives between examples (`dspydantic:src/dspydantic/evaluators/config.py:110-157`) |
| `dspy-agent-skills` (`drg-kg`) | `_score_sets` / `_prf(tp, fp, fn)` | precision, recall, F1 over `Counter`-matched keys, `strip().lower()`'d | **0.0**, never 1.0, on an empty comparison — the one evaluator among all nine repositories verified to get this right, and the one this repository actually calls (`entities.py score`, `rlm_ingest.py score`) |
| `dspy-optimizer` | `Registry` / `get(name)` | `exact_match`, `numeric` (decimal-comma bug — `data.md`) | `scorer(example, prediction) -> bool`, 2-argument, first non-input label only; fails **closed** on a missing key (`dspy-optimizer:dspy_optimizer/strategies/scoring/common.py:25-33`) |
| `dspy-agents` | threshold rules in `thresholds.py` | `min`, `max`, `max_drop`, `max_pct_drop`, `max_pct_increase`, per metric | a metric with no current value **skips its rule** rather than failing it (`dspy-agents:dspy_optimize/baselines/thresholds.py:186-187`) |
| this repository | `pairs.RULES` | `fold` (one entry today) | not a registry of evaluators but of deterministic *rules*, scored the same way through `score_rule()`; "Its reach is the author's decision, not this file's" (`scripts/pairs.py`) |
| this repository | `baseline.compare()`'s verdicts | `ok`, `warn`, `fail`, `unscored` | the state this repository reports a check in, contrasted with `dspy-agents`' two-state (fail / not-fail) drift rules above |

## The table of checks that cannot fail

One row per defect found, sorted by repository. Each is a check that returns a
number indistinguishable from a real pass on an input that should not have
passed. `SKILL.md`'s *The finding that repeats across the nine repositories*
names the shape and points here for the line: "`references/metrics.md` has the
table, one row per repository with the line."

| repository | the check | what it returns, and on what |
|---|---|---|
| `dspy-advanced-prompting` | `edge_case_performance`, `robustness_score` | **1.0** when that test-case type is simply absent from the suite (`dspy-advanced-prompting:src/evaluations/evaluation_framework.py:226-268`) |
| `dspy-advanced-prompting` | `consistency_score` | **1.0** for identical *failing* scores (`1 − std`), and 1.0 when no type has ≥2 scores; `test_coverage` is 1.0 by construction — three failing FUNCTIONAL tests give overall **0.70** (`dspy-advanced-prompting:src/evaluations/evaluation_framework.py:77-89,270-278`, verified: probe T3) |
| `dspy-advanced-prompting` | escape-hatch "confidence" | **0.95** for "I don't know." — the trigger phrases are capitalised, the text is lowercased first, so they never match (`dspy-advanced-prompting:src/techniques/escape_hatches.py:60-96,161-203`, verified: probes S4, T1) |
| `dspy-advanced-prompting` | A/B significance test | **"significant: True"**, t = 1.007e16, from five cache-identical deterministic repeats (`dspy-advanced-prompting:src/evaluations/evaluation_framework.py:403-445`, verified: probe T4) |
| `braid-dspy` | `_default_metric` | **1.000** for a right answer, a wrong one, an exception string, and a bare "6" (`braid-dspy:braid/optimizer.py:475-519`, verified: probe I2) |
| `braid-dspy` | `GRDMetrics` atomicity / masking axes | **1.0** for zero nodes and for zero leak-regex hits; an empty plan still scores 0.68 overall (`braid-dspy:braid/optimizer.py:23-252`, verified: probe I1) |
| `braid-dspy` | Critic self-verification "confidence" | **0.50** (pass) on the empty string `""`; "There are no errors, the answer is right." *fails*, on a `\bno\b` hit (`braid-dspy:braid/critic.py:216-275`, verified: probe E1) |
| `braid-dspy` | `gsm8k_example.py`'s printed accuracy | **100.0%**, from 0 valid results and a substring match of `""` in `""` (`braid-dspy:examples/gsm8k_example.py:56-59`, verified: ran offline) |
| `dspydantic` | every LLM-judge evaluator, on a parse failure | **0.5**, the same value a genuinely mediocre judgement would give (`dspydantic:src/dspydantic/evaluators/score_judge.py:105-131`, `functions.py:127-161`, verified: V/v_eval.py F, G) |
| `dspydantic` | `LabelModelGrader` | never calls its LM at all when the expected label is already in the allowed set — returns 0.0/0.5 by substring only, although its docstring promises "Semantic match via LLM" (`dspydantic:src/dspydantic/evaluators/label_model_grader.py:83-151`, verified: V/v_eval.py D, D') |
| `dspydantic` | list-of-model leaf fields | **1.0** for a completely wrong list and for two empty lists — both sides resolve to `None` (`dspydantic:src/dspydantic/evaluators/functions.py:437-446,551-553`, verified: V/v_eval.py E, E') |
| `dspydantic` | `PredefinedScoreEvaluator` | rebuilt per example, position drifts per thread — `[0.1, 0.9, 0.5]` scored `[0.5, 0.5, 0.5]` for 3 examples (`dspydantic:src/dspydantic/evaluators/predefined_score.py:47-75`, verified: V/v_eval.py H, H') |
| `dspy-optimizer` | `full` / `batched` / `sample` validation strategies | **pass** on an empty dataset — `"# Vacuously true."` is a comment in the code itself (`dspy-optimizer:dspy_optimizer/strategies/validation/{full,batched,sample}.py`, verified) |
| `dspy-agents` | the baseline drift monitor | a rule whose current value is `None` (an unreachable model, `compiled_em_rate=None`) is **skipped**, and prints "Baseline monitor status: ok" (`dspy-agents:dspy_optimize/baselines/thresholds.py:150-214,186-187`, verified offline) |
| `dspy-agents` | the same monitor, on the compile score | the primary metric `program_score` has **no fail rule at all** — only a `total_tokens` warn — so a compile scoring 0.0 is "ok" (`dspy-agents:dspy_optimize/baselines/thresholds.py:79-86`, verified: "Baseline monitor status: ok") |
| `dspy-agents` | the same monitor, on an empty thresholds file | an empty or malformed config yields **no rules**, so every score is "ok"; the repo's own test asserts `em_rate=0.0` with `{}` is `"ok"` (`dspy-agents:dspy_optimize/baselines/thresholds.py:91-138`, `tests/test_baselines_monitor.py:164-179`) |
| `Agentic-Dspy-Rag` | intent classification's `else` branch | a misrouted, negated, or mis-cased intent string **silently defaults** to Factual — 6 of 8 tested miscasings misroute with no report (`Agentic-Dspy-Rag:src/agentic_rag/components/agents.py:109-123`, verified offline) |
| `Agentic-Dspy-Rag` | usage logging | a cache hit or a parse failure becomes the printed string "Could not parse usage data", never raised, and only the *last* of several calls in a run is ever logged (`Agentic-Dspy-Rag:src/agentic_rag/components/agents.py:26-31,51-56`, verified offline) |
| `dspy-auto-gepa` | `AutoData`'s row judge | a call failure and a parse failure both score **0.0** — only a message string distinguishes "could not score" from "scored 0" (`dspy-auto-gepa:src/dspy_auto_gepa/quality.py:136-226`, verified: repo tests pass) |
| `dspy-auto-gepa` | `_validate_metric_source` | never **executes** the metric it is guarding — a bare float with a comment saying `dspy.Prediction`, `return dict(score=...)`, a three-argument metric, and a metric that raises all pass (`dspy-auto-gepa:src/dspy_auto_gepa/metric_builder.py:245-271`, verified: probes G, V) |
| `dspy-auto-gepa` | `compare()`'s reported improvement | a 1-row test split (n=10, default 0.7/0.2/0.1 fractions) reported **`improvement=0.0`** for a run that genuinely improved (valset 0.5 → 1.0) (`dspy-auto-gepa:src/dspy_auto_gepa/runner.py:347-366`, verified: e2e.py, e2e_force.py) |
| `dspy-session` | `to_examples(gold=None)` | a label-comparing metric compares a prediction **with itself**, trivially 1.0 (`dspy-session:dspy_session/session.py:1085-1109`, verified) |
| `dspy-session` | `on_metric_error="zero"` | a raised exception and a genuinely wrong answer both score **0.0**, indistinguishably (`dspy-session:dspy_session/session.py:1111-1135`, verified) |
| `dspy-agent-skills` (wiki-compile) | the weighted compile metric | `_mean([])` = **1.0** — an empty extraction scores 0.70 and reports "clean" (`dspy-agent-skills:skills/dspy-wiki-compile/example_wiki_compile.py:161-170,224-237`, verified: dry-run) |
| `dspy-agent-skills` (adversarial-review) | `judge_metric` | an empty flag, a one-word flag, or the whole artifact used as one flag all score **1.0**, "every overstated and unsupported claim found, none invented" (`dspy-agent-skills:skills/dspy-adversarial-review/example_adversarial_review.py:85-121`, verified: probes A1, A2, A2b) |
| `dspy-agent-skills` (autodialectics) | objection coverage | **1.0** when nothing was objected to, and out-of-range `objection_index` values still count — the anti-pattern `SKILL.md:183` names by name (`dspy-agent-skills:skills/dspy-autodialectics/example_autodialectics.py:223`, verified: probe AD5) |
| `dspy-agent-skills` (`drg-kg`, via its skill) | extraction with no LM configured | documented to return an **empty graph** confidently unless `DRG_REQUIRE_LM=1`; the note found this path unreachable in practice once auto-config runs — a claim that did not reproduce, recorded either way (`dspy-agent-skills:skills/dspy-drg-kg/SKILL.md:90-103`; `drg/extract/__init__.py:190-203`, verified: two installs) |
| `dspy-agent-skills` (TARA, via its skill) | the context-quality gate at the final retry | **always outputs**, even below threshold — the example's own printed "only total<20 escalates" is false at its own numbers (`dspy-agent-skills:skills/dspy-tara-rag/example_tara.py:81-86,137-139`; upstream `loop.py:318-333`) |
| `dspy-agent-skills` (core) | the CI regression gate | `assert result.score >= 0.75` passes for **any score of 0.75% or more**, because `.score` is a 0–100 percentage (`dspy-agent-skills:skills/dspy-evaluation-harness/SKILL.md:104`, verified: behav2.py) |
| `dspy-agent-skills` (core) | `BootstrapFewShot` reading a `Prediction` metric | `bool(dspy.Prediction(score=0.0))` is `True`, so every wrong demo is kept as if it passed (`dspy:teleprompt/bootstrap.py:204-212`, verified: bfs.py) — see *The contract*, above |

## Not taken

- **Levenshtein or embedding similarity as a merge signal** — refused. Either
  would score `Negentropie`/`Entropie` as close; the canary exists to catch
  exactly this (`Plan/concept/dspy-toolchain_2026-09-23.md`, *Deliberately not
  taken*).
- **LLM-drafted metrics** (`dspy-auto-gepa`'s default flow) — refused. The rule
  a program is scored by is written by a person; the `metric=Path(...)` bypass
  is the only path this repository would use.
- **TARA's progressive leniency** — refused. Lowering the acceptance bar until
  something passes trades a real gap for a plausible-looking one; the right
  terminal state for a gate here is an unanswered question, not a lowered bar
  (P15; `Wiki/questions/` is where that state already lives).
- **Conflict detection as a mechanised metric** — refused. "Conflict detection
  is never mechanised … a program that guessed would reproduce the `Zero-Trust`
  false conflict" (`CLAUDE.md`). `dspy-wiki-compile`'s `decision_legal()` and
  its judge-based demotion are catalogued for the first promotion
  (`Plan/concept/dspy-toolchain_2026-09-23.md`, Layer 3), but its verdict is
  never trusted as given: T4 and T15 in that pattern (self-reported legality,
  unsupported claims ignored by the demotion check) are exactly why a model's
  claim about its own legality is not the same as a check of it.
- **A reviewer LM asserted to differ from the writer, when it does not really**
  — a trap to avoid rather than a recipe to take: one plan's own design defaults
  both the judge role and the reflection role to the same model, differing only
  in temperature (`dspy-agent-skills`, plugin plan D3) — "a weak independence"
  by the plan's own standard. Nothing here has a reviewer role yet.
- **A judge for job 1 or job 2** — waits on 20–50 hand-labelled cases per the
  calibration protocol's own floor. Job 1's 67 <!--state:pairs.labelled-->
  judgement records already carry a stated rule each and are close to that
  floor; job 2's 395 <!--state:entities.rows_verified--> entity rows are
  proposals a model wrote, never judgement labels a person made, and do not
  count toward it (`entities.py`'s own docstring: "the ingest skill forbids a
  model list from becoming gold").
