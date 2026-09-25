# Optimizers

Every optimizer here is `account(subject, question) -> account` at one more
scale: `compile(student, trainset, ...)` turns a program and a labelled set
into a program with different demos, instructions, code or weights. `api.md`
has the installed signature of each (`surface` block); this file has what each
one changes, what it needs, what the nine repositories measured running it,
and where it breaks quietly. Metrics — what a metric may return, and what
breaks `dspy.Evaluate` — are `metrics.md`; trainsets, splits and `fold()` are
`data.md`.

## In this repository

`scripts/pairs.py` is the one ladder built here, for the one task with usable
gold labels: **one term or two**, **69 <!--state:pairs.labelled--> labelled
pairs** in `Plan/runs/judgements.jsonl`, each with `first`, `second`, a gold
`decision` and a `rule` — the person's own words for why, which is the GEPA
feedback string with no extra work. `scripts/trainset.py`'s `surface_pairs()`
turns the ledger into rows; `score_one()` returns `{score, feedback}` for one
prediction; `fold_baseline()` scores the repository's own deterministic rule
first. The code is `scripts/pairs.py`, `scripts/baseline.py`,
`scripts/trainset.py` and `scripts/check_dspy_surface.py`.

### The floor is `fold()`, and nothing is worth a call below it

`wiki_index.fold()` is a deterministic surface-normalisation rule, not a
model. `trainset.fold_baseline()` and `pairs.score_rule("fold")` both score it
the same way: **41 <!--state:pairs.fold_correct--> of 69 <!--state:pairs.labelled-->
labelled pairs**, run live 2026-09-24 (`python3 scripts/pairs.py score` prints
`rule:fold: 36/63 = 57.1% on 63 labelled pairs`). All 27 misses have the same
shape — gold `one-term`, `fold()` says `two-terms` — so on this ledger `fold()`
has never produced a **false merge**; every miss is the safe direction. That is
the reason the ladder is rule-first: a model is only ever asked about the
residual `fold()` calls `two-terms` — on 2026-09-24, 59 of the 63 pairs, 27 of
them gold `one-term` — so it can only be asked to *find* a merge `fold()`
missed, never given the chance to *undo* one `fold()` made correctly
(`scripts/pairs.py`).

**The plural rule raises the floor, without a model.** Decision 010 set, on the
author's delegation, the reach of `pairs.RULES["plural"]`: `fold()`, plus a
plural ending — `-s` `-es` `-e` `-en`, `-n` only after `-e` — on a stem of four
letters or more, written in lower case. It decides
**49 <!--state:pairs.plural_correct--> of 69 <!--state:pairs.labelled-->**,
with no false merge and no canary merged. It is a row on the ledger and not part
of `fold()`: reconciliation still merges by `fold()` alone.
`pairs.py run --rule plural` asks it before the model, which then sees 51 pairs,
19 of them gold `one-term` (2026-09-24), and a run on that residual has to beat
`rule:plural`, not `rule:fold` (`python3 scripts/baseline.py compare
one-term-or-two --floor rule:plural`). Eleven of those nineteen were decided
from the passage, which `SameTerm`'s two input fields do not carry (`NOW.md`).

`scripts/trainset.py`'s docstring keeps the first measurement — 14/17 = 82%,
misses J4/J6/J14, from `Plan/concept/trainset-and-the-baseline_2026-09-17.md`,
when the ledger held 17 rows — dated, beside the rule that held since: every
miss is in the safe direction. Until 2026-09-24 it stated the 82% as current.
The number to use is the one the script prints.

### The five rungs, exactly as `pairs.py` builds them

`pairs.py optimizer(name, metric, train_size, reflection_lm)` constructs one
of five, by name, at `scripts/pairs.py`:

| rung | construction in `pairs.py` | changes | LM calls (order of magnitude) |
|---|---|---|---|
| `labeled` | `dspy.LabeledFewShot(k=min(8, train_size))` | demos | ~0 to compile |
| `bootstrap` | `dspy.BootstrapFewShot(metric=lambda e,p,t=None: metric(e,p).score, max_bootstrapped_demos=4, max_labeled_demos=8)` | demos | tens |
| `inferrules` | `dspy.InferRules(num_candidates=4, num_rules=6, metric=lambda e,p,t=None: metric(e,p).score)` | instructions + demos | tens × `num_candidates` |
| `simba` | `dspy.SIMBA(metric=lambda e,p: metric(e,p).score, bsize=min(train_size, 16), num_candidates=4, max_steps=4)` | demos + instructions | medium |
| `gepa` | `dspy.GEPA(metric=metric, auto="light", reflection_lm=reflection_lm, seed=0, track_stats=True)` | instructions (+ `Flex` code) | high, plus reflection |

**`.score` goes to every optimizer except GEPA.** `program_and_metric()`'s
`metric` returns the full `dspy.Prediction(score=judged["score"],
feedback=judged["feedback"])` (`scripts/pairs.py`); every rung but
GEPA is handed a lambda that reads `.score` back out into a bare float first.
That is not stylistic — see BootstrapFewShot below for the trap this avoids,
which `InferRules` inherits and `SIMBA` mostly does not.

**Pinned, stratified folds; canaries never trained on.** `folds(labelled, k)`
groups repeated unordered, spelling-folded pairs and balances decision counts
across `k` folds (`scripts/pairs.py`), so ledger order does not change the
partition and no pair occurs in training and holdout. `model_rows()` excludes
the folded canary pairs first, including J5, which is present in the judgement
ledger. `canaries()`
returns `selftest.MUST_NOT_MERGE`; they are asked once per
compiled program, after every fold and again after the final full compile
(`scripts/pairs.py`, `canaries()` and the loop after the final compile).

**The labeled rung uses explicit demos.** DSPy 3.3.1 samples `k` rows with a
fixed seed by default; `pairs.py` instead reserves two of eight slots for
ledger-labelled lookalikes that are distinct terms, then adds a positive and
stable-ID examples from that fold's training rows. It compiles with
`sample=False`, asserts that the predictor received those IDs, and records
them in the baseline note. This selection applies only to `labeled`; the
other optimizers retain their own training behavior.

**A canary merge vetoes the run, whatever its score.** If the rule named by
`--rule` already says `one-term` for a canary pair the veto fires without a call
at all (`first = RULES[rule]`, `first(a, b) == "one-term"`); otherwise the
compiled program is asked. Two canaries sit one step past the plural rule's
reach — `Spiel`/`Spieler` (`-er`) and `Logo`/`LogOS` (an ending in upper case) —
and `python3 scripts/pairs.py selftest` hands the veto a rule that takes each
step and shows it fire; before decision 010 no canary was within any plural
rule's reach.
`baseline.row(..., vetoed=bool(merged))` records it, and `baseline.compare`
fails a vetoed row unconditionally (below). This exists because `dspy.GEPA`
optimizes a mean score: a candidate that merges the one pair that must never
merge otherwise costs only 1/57 of the metric, invisible in an aggregate.

**Repeats, cache off (P18).** `--repeats N` calls `lmrun.call` up to `N` times
per held-out row and records the fraction of hits
(`round(sum(hits)/len(hits), 3)`), never a bare 0/1 from one attempt.

### The dry run proves the plumbing, not the accuracy

`--dry-run` builds a single `lm_fixture.FixtureLM` that answers every call
with `fill(decision="two-terms", rule="Probelauf: immer zwei Begriffe.")`
(`scripts/pairs.py`) and uses that **same fixture object as the
reflection LM too** (`reflection_lm = lm if dry_run else ...`,
`scripts/pairs.py`) — so GEPA's own reflection calls are answered by it as
well, reached because `fill()` reads whatever output fields a prompt asks for
from `ChatAdapter`'s rendered system message and answers each one
(`scripts/lm_fixture.py`).

Run live here, offline, 2026-09-24 (`.venv-dspy/bin/python scripts/pairs.py
run --optimizer <name> --dry-run`), all five rungs score **exactly
`0.5789` (33/57), 0 canaries merged, exit 0** — identical to `fold()` itself.
Later the same day, at 63 pairs, the `labeled` rung gave `0.5714` (36/63), and
with `--rule plural` `0.6984` (44/63) — each rule's own score, by the same
construction.
That is not a coincidence to be proud of: the fixture always answers
`two-terms`, and every one of `fold()`'s 24 misses is a case where the gold
answer is `one-term` and `fold()` (hence the fixture) says `two-terms`, so a
fixed wrong-in-the-safe-direction answer reproduces `fold()`'s own score by
construction. The dry run demonstrates that each optimizer compiles, that
`call()`'s bookkeeping and the veto check run, and that the harness exits
cleanly — it demonstrates nothing about what a real model would do. GEPA's own
reflection log makes the same point directly: watched live, its "Proposed new
text for self" during a dry run is the fixture's raw `ChatAdapter` output
pasted in verbatim —

```
[[ ## decision ## ]]
two-terms

[[ ## rule ## ]]
Probelauf: immer zwei Begriffe.

[[ ## completed ## ]]
```

— because GEPA's reflection call bypasses `ChatAdapter` and asks the LM
directly for a fenced block (`dspy:teleprompt/gepa/gepa_utils.py:170-180`, see GEPA below), and
`fill()`'s system-message lookup finds no `system` role in that raw call and
falls back to formatting its given defaults. GEPA correctly rejects this
non-instruction every time ("not better than old score, skipping"), and the
final compiled candidate is unaffected because the fixture ignores whatever
instructions it is given anyway.

The same live run is where `dspy.GEPA`'s budget formula closes the loop with
this project's own numbers: `pairs.py`'s final compile (no `valset`, so
`trainset` doubles as valset at 57 rows) logged **`GEPA Optimization: 606/608
rollouts`** — exactly `auto_budget(1, 6, 57) = 608` (see GEPA below).

### What a real run needs

`run(dry_run=False, ...)` requires **both** `--model` and `--approval "<the
author's decision>"` or refuses (`scripts/pairs.py`); `lmrun.make_lm`
builds the LM with `cache=False`, and `lmrun.call` separately refuses a cached
LM and refuses a real LM with no `approval=`. **Decision 011 is that decision
for this ladder**: `--model claude-cli/haiku` (Claude through `claude -p`) or
`--model route/<free model>` (one free OpenRouter model through `route.py`,
pinned), `--approval "decision 011"`.

### The ladder on real models, 2026-09-25

LabeledFewShot, BootstrapFewShot, InferRules and GEPA (`--gepa-calls 200`,
Sonnet reflecting) ran on Haiku; LabeledFewShot also with `--evidence` and on
the free models that answered. `python3 scripts/pairs.py report` prints every
row split by direction — merges found among the pairs the rule leaves, pairs
kept apart, and each **false merge** by judgement id — and
`Plan/concept/dspy-optimization_2026-09-25.md` reads them. What held, in words:

- **Every Claude rung beat the plural rule, by recall, at almost no loss of
  precision**; Bootstrap was the best row, and its one false merge,
  `AEGIS-Echo`/`Echo-AEGIS`, is two compounds of the same parts.
- **InferRules cost the most and did not beat Bootstrap** — the same null result
  the one published measurement near this scale reports
  (`Plan/concept/dspy-source_2026-09-24/research.md`). Its induced rules, kept by
  `pairs.py final` in `Plan/runs/surface-pairs/programs/`, restate the ledger's.
- **Document lines as evidence raised recall and cost precision**: a line where
  two surfaces stand together reads as identity to a model.
- **A free model's score can hide a false merge on every other pair**, the
  founding canary among them. The veto asked each canary once, so it did not
  fire; it now asks as often as a held-out pair, and a held-out canary row vetoes.
- **Measured per call** (`Plan/runs/surface-pairs/lm/`): Haiku with thinking off
  answers in 2.4–3.9 s for about $0.0024; InferRules' candidate evaluation and
  rule-induction prompts make it the most expensive rung per run.
- **SIMBA was not run** — about $8 of Claude usage, and no published evidence.

### What `baseline.py compare` says

`Plan/runs/baselines.jsonl` holds one append-only row per scored candidate:
`task, candidate, program_hash, trainset_hash, n, scored, correct, score,
vetoed, outcomes, cost, at, note`. `compare(task, floor)` reads `("ok" |
"warn" | "fail" | "unscored", reasons)` for the **newest** row of a task
against the newest row of the candidate named by `floor` (default: the task's
first candidate) scored on the same trainset — `scripts/baseline.py`:

- `unscored` — the newest row's `score` is `None` (0 of `n` examples could be
  scored).
- `fail` — the row is `vetoed` (a canary merged), **or** its score does not
  beat the floor's, whatever the score.
- `warn` — the floor candidate has no row on this trainset (compare the
  hashes, re-score the floor first), or some examples were not scored, or the
  score fell more than `TOLERANCE = 0.02` below the best earlier row on the same
  trainset.
- `ok` — beats the floor, nothing else flagged.

Run live here, 2026-09-24, before one fix:

```
$ python3 scripts/baseline.py compare one-term-or-two --floor rule:fold
warn
  trainset changed since the floor (ea786421cb69 → 8164aef4b827): re-score the floor before comparing
```

`ea786421cb69` is the `n=36` row of 2026-09-23: `compare` took the floor
candidate's **oldest** row, so re-scoring the floor — what the message asks
for — appended a row `compare` never read, and the warning could not be
cleared. And behind that sat a second defect the first one hid: it measured a
fall against the best row on *any* trainset, so with only the floor fixed, the
floor re-scored at 57 pairs (57.9%) would still have been flagged as below its
own 61.4% at 44. Both are fixed, and `baseline.py selftest` carries one case
for each, each failing against the old code. After `pairs.py score --rule fold --record`
and `--rule plural --record`:

```
$ python3 scripts/baseline.py compare one-term-or-two --floor rule:fold
ok
```

`baseline.digest` hashes what a program or trainset **is**, never a version
someone bumps by hand. For a rule row that now includes `fold()`'s own source:
until 2026-09-24 only the lambda that calls `fold()` was hashed —
`43807fbbefd8` on every `rule:fold` row — so a change inside `fold()` would
have left the hash as it was. The row recorded that day carries
`9e29d450e8b8`, although `fold()` did not change.

## Choosing an optimizer

Every source that gives a number ties the choice to **how many labelled
examples exist**, in the same order, with different exact cutoffs:

| source | thresholds |
|---|---|
| `dspy-agent-skills`'s selection matrix | LabeledFewShot (any) → BootstrapFewShot (~10+) → BootstrapRS (50+) → KNNFewShot (varied inputs) → COPRO (instructions) → MIPROv2 (100+, scalar, optuna) → GEPA (feedback) → SIMBA (cheaper reflective pass) → BootstrapFinetune → Ensemble → BetterTogether (`dspy-agent-skills:skills/dspy-optimizer-selection/SKILL.md:40-57`) |
| `dspy-agent-skills`'s trainset-size table | <10 LabeledFewShot; 10–50 BootstrapFewShot/SIMBA; 50–100 BootstrapRS/SIMBA/GEPA; 100–500 MIPROv2/GEPA/BootstrapRS; 500+ MIPROv2/BootstrapFinetune/BetterTogether (`dspy-agent-skills:skills/dspy-optimizer-selection/reference.md:65-78`) — SIMBA in the 10–50 row contradicts its own default `bsize=32` assertion below |
| `dspydantic`'s `_auto_select_optimizer` | n≤2 → `miprov2zeroshot`; 3≤n<20 → `bootstrapfewshot`; n≥20 → `bootstrapfewshotwithrandomsearch` (`dspydantic:src/dspydantic/optimizer.py:512-533`) |
| this repository, `Plan/concept/optimizers-and-data_2026-09-17.md` | `LabeledFewShot` (floor) → `BootstrapFewShot` (~10+) → `InferRules` (project-specific, below) → `SIMBA` (cap `bsize`) → `GEPA` (feedback already written); MIPROv2 (100+) and BootstrapRS (50+) ruled out at n=26, unchanged at n=57 |

**"Escalate only on a measured plateau. Two optimizers in a row that fail to
beat the baseline usually mean the metric is wrong, not that the optimizer is
weak."** (`dspy-agent-skills:skills/dspy-optimizer-selection/SKILL.md:59-73`,
`[claim]`). The same pack's book slice gives the order this repository already
follows by hand: signatures → modules → explore a few by hand → dataset →
metrics → **a baseline, "a number to beat, before any compile"** → optimize →
test and iterate, naming steps 3 and 6 as the ones people skip
(`dspy-agent-skills:skills/dspy-book-eight-steps/SKILL.md:21-33`, `[pattern]`)
— `fold()`'s 57% is exactly that step-6 number here. Where the metric is
itself a judge model, the same pack's chapter 3 optimizes the judge before the
task and reloads it frozen, "because optimizing a task against an unvalidated
judge moves the program toward the judge's errors, and you cannot tell from
the score that it happened" (`dspy-agent-skills:skills/dspy-book-eight-steps/SKILL.md:35-43`,
`[pattern]`) — not this project's situation today (the metric is `fold()` plus
a person's recorded rule, never a model), but the shape to repeat if a judge
metric is ever built (`metrics.md`).

**No automatic selector is built here.** `dspydantic`'s `_auto_select_optimizer`
is catalogued in `Plan/concept/dspy-toolchain_2026-09-23.md` as a pattern
worth taking **once more than one task sits on the ladder** — today there is
exactly one (`one-term-or-two`), so an auto-selector would have nothing to
select between. Its own numbers are a reason for caution before building one
anyway: it is an n-only rule with no floor check baked in, and dspydantic's
own single-pass flow reverts to the un-optimized field description whenever
the optimized one does not score strictly higher — which is also why its
regression test — "Assert that optimized descriptions are actual descriptions,
not meta-instructions" (`dspydantic:tests/integration/test_miprov2_descriptions.py:291`,
`META_INSTRUCTION_PATTERNS`) — passes whether or not the fix works: a reverted,
untouched original trivially contains no meta-instruction either
(`dspydantic:tests/integration/test_miprov2_descriptions.py:19-26,288-300`,
`[trap]`). An auto-selected optimizer still needs the same floor check
`baseline.compare` already does by hand.

## LabeledFewShot

`dspy.LabeledFewShot(k=16)`; `compile(student, *, trainset, sample=True)` —
`api.md` has the full surface entry. The floor rung: **no metric, no LM call
to compile.** For every predictor in the module, `sample=True` draws
`rng.sample(trainset, min(k, len(trainset)))` from one `random.Random(0)`
created once per compile (`dspy:teleprompt/vanilla.py:10-21`); `sample=False`
instead takes the literal first `k` rows in trainset order. An empty trainset
returns the student unchanged.

**Two compiles of the same `LabeledFewShot(k)` on the same trainset choose
identical demos, and that set is a genuine sample, not the first `k` rows in
order.** [checked: labeledfewshot-fixed-seed] The fixed `random.Random(0)`
seed is not configurable — every compile of `LabeledFewShot(k=5)` on the same
20-row set in this project's probe picks the same q6, q7, q3, q0
(`dspy-agent-skills:skills/dspy-book-optimizers/SKILL.md:41,77`, `[number]`),
run to run, container to container.

**Measured** (`dspy-agent-skills`'s AI-text-detection chapter, `k=4`, 160-row
train / 80-row locked test, one `exact_match` metric): val 63.33, **test 67.50
(54/80), +13.75** over the unoptimized baseline, $0, 0.0 s
(`dspy-agent-skills:skills/dspy-book-optimizers/reference.md:36`, `[number]`).
Free, and the same test score as the much more expensive `BootstrapFewShot`
run below on the same data — "If putting 16 labelled pairs in a prompt does
not beat 65%, the problem is the task's framing and no amount of reflection
will fix it" (`Plan/concept/optimizers-and-data_2026-09-17.md`, written at
16 pairs and a 65% floor).

**In this repository**, `pairs.py`'s `labeled` rung is `k=min(8, train_size)`
— the one rung `pairs.py score` names as the cheapest model call waiting on
approval.

## BootstrapFewShot

`dspy.BootstrapFewShot(metric=None, metric_threshold=None,
teacher_settings=None, max_bootstrapped_demos=4, max_labeled_demos=16,
max_rounds=1, max_errors=None)`; `compile(student, *, teacher=None,
trainset)` — `api.md` surface entry. Runs the teacher (the student itself,
uncompiled, if none given) on `trainset`, keeps traces the metric calls
successful as bootstrapped demos, and fills any remaining slots up to
`max_labeled_demos` with an inner `LabeledFewShot`. **Changes demos only.**

**The central trap: without `metric_threshold`, success is the metric's
return value read for its truthiness, and `bool(dspy.Prediction(score=0.0))`
is `True`.** [checked: bootstrap-keeps-wrong-demos-on-prediction] The source
is exactly that branch: `success = metric_val >= self.metric_threshold` when a
threshold is set, else **`success = metric_val` itself**
(`dspy:teleprompt/bootstrap.py:206-212`). Measured, offline, with every
generated answer wrong: a metric returning `dspy.Prediction(score=0.0,
feedback=...)` kept **4 of 4 wrong answers as demos**; the identical wrongness
scored by a bare-`float`-returning metric kept **0**; the same
`Prediction`-returning metric with an explicit `metric_threshold=0.5` also
kept 0. This is why every non-GEPA rung of `pairs.py`'s ladder is handed
`lambda e, p, t=None: metric(e, p).score` instead of the raw five-argument
metric (`scripts/pairs.py`) — GEPA is the one place the full
`Prediction` object is read by name (`.score`, `.feedback`), never by
truthiness. **Affected the same way:** `BootstrapFewShotWithRandomSearch`,
`KNNFewShot`'s bootstrap step, `InferRules` (a subclass, below), MIPROv2's
demo-bootstrapping stage, and `BetterTogether`'s default `p=` stage — none of
them are safe to hand a bare `Prediction`-returning metric either.

Two more shapes of the same class of bug, independently confirmed:
`dspydantic` hands `BootstrapFewShot` a metric with no `metric_threshold` at
all, so **any positive float becomes a kept demo** — a rewrite scoring 0.25
still gets bootstrapped (`dspydantic:src/dspydantic/optimizer.py:...`, its
own live run: "Bootstrapped 1 full traces" at metric 0.5,
`[trap]`). `braid-dspy`'s `BraidOptimizer` builds its examples **without**
`.with_inputs()`, so `input_keys=None`, and BootstrapFewShot logs "Inputs have
not been set for this example" for every row, reports "Bootstrapped 0 full
traces", and **still installs raw labelled demos anyway**
(`braid-dspy:braid/optimizer.py:413-415,451-457`, `[trap]`).

**With `metric=None`, every attempt succeeds unconditionally** — nothing is
filtered (`dspy-agents:dspy_optimize/compile_rag.py`, cross-confirmed at
`dspy:teleprompt/bootstrap.py:212`).

**Recompiling.** A fresh `.deepcopy()` per compile (what `pairs.py` does per
fold, `scripts/pairs.py`) never stacks demos across runs — three
successive compiles from a clean copy each leave exactly the new demos, the
original untouched. Compiling an **already-compiled** student object directly
raises `AssertionError: Student must be uncompiled.`
(`dspy-agent-skills:skills/dspy-book-optimizers/reference.md:91-92`,
`dspy:teleprompt/bootstrap.py:96-102`, `[trap]`) — a documented claim in one of
the nine repositories' own skills ("compiling the same object three times
stacks demos") is false on 3.3.1.

**Measured**: same chapter-6 detector, `max_bootstrapped_demos=2,
max_labeled_demos=2, max_rounds=1, max_errors=1`: val 66.67, **test 67.50
(54/80), +13.75**, $0.0030, 4.5 s — "a third of a cent and 4.5 seconds for the
same +13.75 as `LabeledFewShot`"
(`dspy-agent-skills:skills/dspy-book-optimizers/reference.md:37`, `[number]`).

## BootstrapFewShotWithRandomSearch

`dspy.BootstrapFewShotWithRandomSearch(metric, teacher_settings=None,
max_bootstrapped_demos=4, max_labeled_demos=16, max_rounds=1,
num_candidate_programs=16, num_threads=None, max_errors=None,
stop_at_score=None, metric_threshold=None)`, aliased `dspy.BootstrapRS`
(`dspy:__init__.py:63`); `compile(student, *, teacher=None, trainset,
valset=None, restrict=None, labeled_sample=True)`. Repeats
`BootstrapFewShot` under different random demo subsets to build
`num_candidate_programs` full candidate programs, scores each on the valset
(or a `trainset`-derived split), and keeps the best. **Changes demos**, by
search rather than by one pass.

**`dspydantic`'s "fast mode" default kwargs crash it outright.**
`_FAST_MODE_KWARGS["bootstrapfewshotwithrandomsearch"]` passes
`num_candidates=4` — there is no such parameter; the real one is
`num_candidate_programs` — so the **default** auto-selected path at n≥20
raises `TypeError` at construction, before any LM call
(`dspydantic:src/dspydantic/optimizer.py:27,398-403,948`, `[trap]`).

**Measured**, `num_candidate_programs=8, max_bootstrapped_demos=2,
max_labeled_demos=2, num_threads=1`: val 61.67, **test 65.00 (52/80), +11.25**,
**$0.8766, 1119.1 s** (`dspy-agent-skills:skills/dspy-book-optimizers/reference.md:38,60-62`,
`[number]`) — at 8 candidates already more expensive than `GEPA`'s 616.7 s /
$0.62 run below, for less than half GEPA's gain.

**Not taken here**: "50+ examples" is the threshold in every source that gives
one; this project compiles on 49 to 51 labelled pairs per fold, 63 in all
(2026-09-24) — at the threshold rather than past it, and the cost measured above
buys less than half GEPA's gain. Absent from
`pairs.py`'s ladder and from `Plan/concept/optimizers-and-data_2026-09-17.md`'s
ruled-in table by name (grouped with MIPROv2 and synthetic data generation
under the same "100+/50+ examples" reason, `Plan/concept/dspy-toolchain_2026-09-23.md`).

## KNNFewShot

`dspy.KNNFewShot(k, trainset, vectorizer: Embedder, **few_shot_bootstrap_args)`;
`compile(student, *, teacher=None)`. **Construction is not free** — `KNN.__init__`
embeds the whole `trainset` immediately (`dspy:predict/knn.py:40-47`), so
building one with a hosted `dspy.Embedder` already spends API calls before
`compile` is even called; this is why the optimizer-selection dry-run in
`dspy-agent-skills` constructs every optimizer **except** `KNNFewShot`
(`dspy-agent-skills:skills/dspy-optimizer-selection/example_optimizer_selection.py:156-158`,
`[trap]`).

**`compile()` changes nothing at compile time.** It only replaces `forward`
so that **every inference call** retrieves the `k` nearest neighbours by
embedding similarity and runs a fresh `BootstrapFewShot(**few_shot_bootstrap_args)`
against just those neighbours before predicting
(`dspy:teleprompt/knn_fewshot.py:52-69`). The book chapter's "$0/0 s to
compile" is real but moves the cost to every subsequent call — with
`max_bootstrapped_demos>0` each prediction pays its own bootstrap LM calls;
the chapter's own `max_bootstrapped_demos=0` config avoids that by using the
retrieved neighbours as raw labelled demos only
(`dspy-agent-skills:skills/dspy-book-optimizers/SKILL.md:93-96`, `[trap]`).

**Two traps that only appear later.** `num_threads` in
`few_shot_bootstrap_args` is accepted silently at construction and compile,
and only raises `TypeError: BootstrapFewShot.__init__() got an unexpected
keyword argument 'num_threads'` on the **first forward call**. `save()` writes
`demos: []` — retrieval is not persisted, so a saved-and-reloaded `KNNFewShot`
program is zero-shot (`dspy-agent-skills:skills/dspy-book-optimizers/SKILL.md:93-96`,
`[trap]`).

**Measured**: `k=4, max_bootstrapped_demos=0, max_labeled_demos=4`, a local
hashed n-gram embedder (no API key, no cost): val 71.67, **test 72.50 (58/80),
+18.75 — the best free result of all twelve runs**, beating every paid
optimizer's test score except GEPA's
(`dspy-agent-skills:skills/dspy-book-optimizers/reference.md:39`, `[number]`).

**Not taken here, waiting**: `Plan/concept/optimizers-and-data_2026-09-17.md`
rules it out for needing a `dspy.Embedder` — "though qmd now has a local
embedding model, so this becomes cheap if step 0–2 disappoint." It is a
waiting item, not a refusal: the condition it is waiting for is the cheaper
rungs of this same ladder failing to beat the floor.

## InferRules

`dspy.InferRules(num_candidates=10, num_rules=10, num_threads=None,
teacher_settings=None, **kwargs)` — a `BootstrapFewShot` **subclass**,
forwarding `metric`, `metric_threshold`, `max_errors` and the demo-count
kwargs to the parent; `compile(student, *, teacher=None, trainset,
valset=None)`.

**Mechanism, read from the source.** `compile()` first calls
`super().compile(student, teacher=teacher, trainset=trainset)` — an ordinary
`BootstrapFewShot` pass, inheriting the exact truthiness trap above, which is
why `pairs.py` hands InferRules `.score` too, not only because of the
`Evaluate` call below. It then deep-copies the bootstrapped program
`num_candidates` times; for each candidate it asks a `ChainOfThought`
"extract a list of `{num_rules}` concise and non-redundant natural language
rules…" over every training row, formatted as `Input Fields: …
========= Output Fields: …`, and appends the result to that predictor's
instructions as "Please adhere to the following rules when making your
prediction:\n{rules}"; each candidate is then scored with `dspy.Evaluate`
(a percentage, failures folded to 0) and the best-scoring candidate wins
(`dspy:teleprompt/infer_rules.py:23-59,61-96,110-134`). **So it changes both
instructions and demos**, never instructions alone.

**Without an explicit `valset`, `compile()` splits the trainset exactly in
half by list order, unshuffled — the first half for rule induction, the
second half to choose among the candidates.** [checked: inferrules-halves-trainset]
`train_size = int(0.5*len(trainset)); trainset, valset =
trainset[:train_size], trainset[train_size:]`
(`dspy:teleprompt/infer_rules.py:24-26`). `pairs.py`'s InferRules rung never
passes a `valset` (`scripts/pairs.py`), so every real run on this
ledger is silently halved this way. What it halves is the compile trainset —
every labelled row outside the held-out fold, the pairs the rule answers
included — not the residual a model is asked about: on 2026-09-24, 49 to 51 of
the 63 rows per fold, so 24 or 25 to write rules from and the rest to pick a
winner among, and 31 of 63 in the final compile. (Until 2026-09-24 this
paragraph said „the 24-row residual … 12 rows … and 12"; `pairs.py` asks a
model about the 59 pairs `fold()` calls two terms, 27 of them gold `one-term`,
and trains it on all.) **No canary is held back at all**, because `pairs.py`'s
canary check runs separately, after compile, on the final program.

**This is the rung this project's own concept doc singles out, and it is
absent from `dspy-agent-skills`'s own selection table.** The reason is
specific to this ledger: `Plan/runs/judgements.jsonl` already carries a
person's stated `rule` in words for every labelled pair, so an induced rule
is directly comparable to a human one — does the model find the same rule ("a
leading German definite article is never a term boundary"), and if an induced
rule survives, it becomes a `fold()` candidate that `judgements.py` can
replay against every recorded decision
(`Plan/concept/optimizers-and-data_2026-09-17.md`).

**Not in any of the twelve book runs**, and not in any of the nine
repositories' optimizer-selection tables — `dspy-agent-skills`'s core slice
notes this explicitly: "InferRules exists in 3.3.1, and the pack teaches
nothing about it" (`dspy-agent-skills`, `das-core` OPT). **Not run against a
real model here yet** — `--dry-run` only, as of 2026-09-24.

## COPRO

`dspy.COPRO(prompt_model=None, metric=None, breadth=10, depth=3,
init_temperature=1.4, track_stats=False, **_kwargs)` — raises `ValueError:
Breadth must be greater than 1` at construction if `breadth<=1` (confirmed
here, directly, against the installed package: `dspy:teleprompt/copro_optimizer.py:70-71`),
and **silently swallows any misspelled or unsupported keyword** through
`**_kwargs` — a typo in a COPRO argument produces no error at all.
`compile(student, *, trainset, eval_kwargs=None)`. **Changes instructions
only, never demos**: a `breadth × depth` search over instruction rewrites
written by `prompt_model` and scored by `metric`.

**COPRO has no held-out split of its own — it scores every candidate on
whatever is handed to it as `trainset`.** The book chapter passes its
validation split as COPRO's `trainset` argument specifically so its own
"validation" number is not the training set ("note: valset passed as
trainset"), which means the 53.33 figure reported as COPRO's validation score
in that run is COPRO's own search set, not a held-out score — the fair
comparison is the separately computed 80-row test score
(`dspy-agent-skills:skills/dspy-book-optimizers/SKILL.md:47`,
`dspy:teleprompt/copro_optimizer.py:138`, `[trap]`).

**Measured**: `breadth=4, depth=2, init_temperature=1.0, track_stats=True`:
val 53.33, **test 50.00 (40/80), −3.75 — made the detector worse than doing
nothing**, cost **≥$0.0732** (a lower bound; chapter 6's COPRO/MIPROv2 cost
figures undercount a shared-history accounting bug the chapter later fixed),
861.1 s (`dspy-agent-skills:skills/dspy-book-optimizers/reference.md:40,64-67`,
`[number]`).

**Neither ruled in nor ruled out here.** COPRO does not appear in
`pairs.py`'s ladder or in either table of
`Plan/concept/optimizers-and-data_2026-09-17.md` — an omission, not a
decision. The nine repositories' own selection matrix places it between
`BootstrapRS` and `MIPROv2`, needing only "instructions" rather than a
specific example count (Choosing an optimizer, above).

## MIPROv2

`dspy.MIPROv2(metric, prompt_model=None, task_model=None,
teacher_settings=None, max_bootstrapped_demos=4, max_labeled_demos=4,
auto="light", num_candidates=None, num_threads=None, max_errors=None, seed=9,
init_temperature=1.0, verbose=False, track_stats=True, log_dir=None,
metric_threshold=None)`; `compile(student, *, trainset, teacher=None,
valset=None, num_trials=None, minibatch=True, minibatch_size=35,
minibatch_full_eval_steps=5, requires_permission_to_run=None)` — `api.md`
surface entry. With no `dspy.configure(lm=...)` and no `prompt_model`/`task_model`
pair, raises `ValueError` at construction. **Changes demos and instructions**,
in three internal steps: bootstrap demo candidates, propose instruction
candidates, then a Bayesian search (optuna) over combinations, scored by
`minibatch` evaluation with periodic full evals.

**Needs `optuna`, and fails only after paying for the first two steps.**
`_import_optuna()` raises `ImportError: MIPROv2 requires optional dependency
'optuna'. Install it with pip install dspy[optuna].` at **step 3**, "finding
optimal prompt parameters" — after demo bootstrapping (step 1) and
instruction proposal (step 2) have already spent LM calls
(`dspy:teleprompt/mipro_optimizer_v2.py:28-39,520`). `optuna` is **not
installed in `.venv-dspy` here** (confirmed against the installed package,
2026-09-24). Three independent readings confirm the same failure point
(`dspy-agent-skills`, `dspydantic:src/dspydantic/optimizer.py`, `dspy-agents`).

**`auto` and `num_candidates`/`num_trials` are mutually exclusive**, and with
`auto=None` both are required — three independent sources measure the same
`AUTO_RUN_SETTINGS`: light `{n:6, val_size:100}`, medium `{n:12, val_size:300}`,
heavy `{n:18, val_size:1000}`; `num_trials = int(max(2*num_vars*log2(n),
1.5*num_candidates))` where `num_vars = predictors × 2` unless zero-shot;
minibatching turns on only when `len(valset) > 50`
(`dspy:teleprompt/mipro_optimizer_v2.py:44-50,280-316`).

**Without a `valset`, the automatic split takes the trailing 80% of the
trainset, unshuffled**, needing ≥2 rows
(`valset_size = min(1000, max(1, int(len(trainset)*0.80)))`,
`dspy:teleprompt/mipro_optimizer_v2.py:320-330`). `dspy-agents`' real
50-row run shows exactly what this does to an ordered dataset: rows 1–10
(Agno and DSPy basics) become the 10-row train set and rows 11–50 (later-added
observability, GitHub and OpenAI-Responses rows) become the 40-row val set —
whichever ten rows sort first are what MIPROv2 ever bootstraps demos from
(`dspy-agents:dspy_optimize/compile_rag.py:82-87`, `dspy:teleprompt/mipro_optimizer_v2.py:319-333`,
`[number]`).

**`requires_permission_to_run` is fully removed**: `False` only logs a
deprecation warning; `True` raises `ValueError: User confirmation is removed
from MIPROv2. Please remove the 'requires_permission_to_run' argument.`

**Ties keep the untouched program.** `best_score` is replaced only by a
strictly higher score; when every candidate scores 0.0 the "optimized"
program is the unmodified input — 0 demos, the generic instruction `"Given
the fields \`context\`, \`question\`, produce the fields \`answer\`."` —
which looks like a completed, harmless compile rather than a run that found
nothing (`dspy:teleprompt/mipro_optimizer_v2.py:592,855`). `total_calls` and
`prompt_model_total_calls` are dead counters, set to 0 and never incremented,
in 3.0.3 and in 3.3.1 alike — never trust them for cost accounting
(`dspy-agents:dspy_optimize/compile_rag.py`, `dspy:teleprompt/mipro_optimizer_v2.py:98-99,678-679`,
`[trap]`).

**Measured** (dspy-agents, `auto="light"`, one predictor, real run on 50
rows): the light run alone logged `num_trials: 10 / minibatch: False /
num_fewshot_candidates: 6 / num_instruct_candidates: 3 / valset size: 40` and
cost **482 LM calls** — 6 bootstrap sets over the 10 train rows, 3 instruction
proposals plus data/program summaries, and 11 full evaluations × 40. Bootstrap
on exact-match answers yielded **0 full traces** ("Bootstrapped 0 full traces
after 9 examples … amounting to 10 attempts") — with a strict metric, demo
candidates can only ever be labelled demos, never bootstrapped ones.
(`dspy-agents:dspy_optimize/compile_rag.py:82-87`, `[number]`.) The same
project's own documentation undercounted its own dataset throughout — "28
doc-grounded Q/A pairs" while the file held 50 rows since an earlier commit,
and nothing re-derived the count — the exact shape of stale claim `CLAUDE.md`'s
*Changing your mind* names.

**Measured** (book chapter, `auto='light'`, `max_bootstrapped_demos=2,
max_labeled_demos=2, seed=42`): val 76.67, **test 66.25 (53/80), +12.50**,
cost **≥$0.3052**, 270.8 s — a **10.42-point validation-to-test gap**, the
chapter's own worked example of "Report the held-out number."
(`dspy-agent-skills:skills/dspy-book-optimizers/SKILL.md:65-67`,
`dspy-agent-skills:skills/dspy-book-optimizers/reference.md:41,69-72`,
`[number]`).

**Not taken here**: "100+ examples" is the threshold `dspy-agent-skills` and
this project's own concept doc both give; this project compiles on 63 labelled
pairs, 49 to 51 per fold. `dspydantic`'s
auto-selector places MIPROv2 (zero-shot) only at the **opposite** end, n≤2 —
a different regime entirely from "100+", not a disagreement about this
project's size.

## SIMBA

`dspy.SIMBA(*, metric, bsize=32, num_candidates=6, max_steps=8, max_demos=4,
prompt_model=None, teacher_settings=None, demo_input_field_maxlen=100000,
num_threads=None, temperature_for_sampling=0.2, temperature_for_candidates=0.2)`
— every argument including `metric` is keyword-only, so `SIMBA(my_metric)`
raises `TypeError: SIMBA.__init__() takes 1 positional argument but 2 were
given`; `compile(student, *, trainset, seed=0)` — **no `valset` parameter at
all**. Needs `numpy` (`np = require("numpy")`,
`dspy:teleprompt/simba.py:12`), matching this repository's `dspy[numpy]`
install. **Changes demos and instructions**, mixed: each step samples a
mini-batch of `bsize` rows and, per candidate, applies either
`append_a_demo` (keep a good trajectory as a demo) or `append_a_rule` (write a
textual rule from a reflective call); both strategies run when `max_demos>0`
(the default); with `max_demos=0` only `append_a_rule` runs.

**`SIMBA` refuses a trainset smaller than `bsize`.** [checked: simba-trainset-below-bsize]
`assert len(trainset) >= self.bsize, f"Trainset too small: {len(trainset)} <
{self.bsize}"` (`dspy:teleprompt/simba.py:105`). With the **default**
`bsize=32`, any trainset under 32 rows refuses before doing anything at all —
confirmed here, offline, against the installed package: `SIMBA(bsize=32).compile(...,
trainset=<20 examples>)` raises `AssertionError: Trainset too small: 20 <
32`. This is exactly why `pairs.py`'s SIMBA rung overrides the default —
`bsize=min(train_size, 16)` (`scripts/pairs.py`) — since every fold's
training portion of this 57-row ledger is well under 32.

**SIMBA's own metric wrapper is looser than `dspy.Evaluate`'s, and fails
quietly.** `output = metric(example, prediction)`: an int/float is read
directly as the score; a `dspy.Prediction` must carry `.score` (its other
fields become `output_metadata`); a `Prediction` with no `.score`, or **any**
metric exception, is caught, **logged as a warning, and scored 0.0** — no
crash at all, unlike `dspy.Evaluate`'s failure-then-`failure_score` behaviour
(`dspy:teleprompt/simba_utils.py:40-67`).

**Measured**: `bsize=8` (already below the default, still costly), `num_candidates=4,
max_steps=6, max_demos=2`: val 51.67, **test 47.50 (38/80), −6.25 — made it
worse**, **$1.1413 — the single most expensive run of all twelve, and the
worst-scoring paid run**, 321.3 s
(`dspy-agent-skills:skills/dspy-book-optimizers/reference.md:43,74-75`,
`[number]`). This is the exact measurement `CLAUDE.md` cites as the reason
`pairs.py` caps `bsize` below the default rather than letting it exceed the
trainset. The qualitative "medium" cost this project's own ladder doc gives
SIMBA does not match the one real cost measurement available, which puts it
above every other rung including GEPA.

## GEPA

`dspy.GEPA(metric, auto=None, max_full_evals=None, max_metric_calls=None,
reflection_minibatch_size=3, candidate_selection_strategy="pareto",
reflection_lm=None, skip_perfect_score=True, add_format_failure_as_feedback=False,
instruction_proposer=None, component_selector="round_robin", use_merge=True,
max_merge_invocations=5, num_threads=None, failure_score=0.0, perfect_score=1.0,
log_dir=None, track_stats=False, use_wandb=False, track_best_outputs=False,
warn_on_score_mismatch=True, use_mlflow=False, seed=0, gepa_kwargs=None)`;
`compile(student, *, trainset, teacher=None, valset=None)` — 26 parameters,
every one after `metric` keyword-only; `api.md` has the full surface entry.
**Changes predictor instructions** (`signature.instructions`) and, for a
`dspy.Flex` submodule, its **source code** (`module_src`) — never demos.

### The metric contract

Five positional arguments, checked at **construction**:
`inspect.signature(metric).bind(None, None, None, None, None)`; a metric that
cannot bind five positional arguments raises `TypeError: GEPA metric must
accept five arguments: (gold, pred, trace, pred_name, pred_trace).`
(`dspy:teleprompt/gepa/gepa.py:416-422`). A **sixth**, optional argument,
`program_trace`, is part of the protocol but not checked at construction: it
is supplied only at scoring time, when a `dspy.Flex` submodule is being
optimized, so a metric can score against *how* an answer was produced — for
example `len(program_trace)` as an LM-call penalty — rather than only whether
it was correct (`dspy:teleprompt/gepa/gepa.py:28-60`).

During reflection GEPA calls the metric per predictor as
`metric(module_inputs, module_outputs, captured_trace, pred_name,
trace_for_pred)`, where `trace_for_pred` is a one-element list
`[(predictor, predictor_inputs, predictor_output)]`
(`dspy:teleprompt/gepa/gepa.py:584-599`). The return is read like this:

- a plain float or other non-`Prediction` value is wrapped as `dict(score=o,
  feedback=f"This trajectory got a score of {o}.")` — **the reflection LM
  learns nothing but the number**;
- a `dspy.Prediction` with `feedback=None` gets the same generic text;
- **per-predictor scores are ignored.** If the score a metric returns with
  `pred_name` set differs from the module-level score (no `pred_name`), GEPA
  warns once ("GEPA does not support predictor level scoring … will ignore
  the differing score returned, and instead use module level score",
  `dspy:teleprompt/gepa/gepa_utils.py:420-430`) and uses the module-level
  score — only the **feedback text** is taken per predictor, never the score.

`warn_on_score_mismatch=True` is the default that produces that warning.

### Budgets

`auto="light"|"medium"|"heavy"` is mutually exclusive with `max_full_evals`
and `max_metric_calls` — exactly one of the three, checked by assertion
(`Exactly one of max_metric_calls, max_full_evals, auto must be set.`,
`dspy:teleprompt/gepa/gepa.py:427-432`). [checked: gepa-budget-exclusive] The formula, read directly from
`auto_budget` (`dspy:teleprompt/gepa/gepa.py:490-520`):

```
N = int(max(2 * (num_preds*2) * log2(num_candidates), 1.5 * num_candidates))
total = V + 5*num_candidates + N*M + (periodic_fulls + extra_final) * V
    where M = minibatch_size (35), V = valset_size (or len(trainset) with none),
    periodic_fulls = (N+1)//full_eval_steps + 1 (full_eval_steps default 5),
    extra_final = 1 if N < full_eval_steps else 0
```

`num_candidates` comes from `AUTO_RUN_SETTINGS = {"light": 6, "medium": 12,
"heavy": 18}`; `num_preds` is the predictor count plus any `dspy.Flex`
submodule count. In closed form, for **one predictor**: `light = 380 + 4V`,
`medium = 690 + 5V`, `heavy = 1035 + 7V`.

**For `auto="light"`, one predictor, `auto_budget` gives exactly `{484, 560,
608}` metric calls at valset sizes `{26, 45, 57}`.** [checked: gepa-light-budget]
57 is this project's own `pairs.labelled` count today, and `pairs.py`'s own
final compile — no `valset`, so its 57-row trainset serves as valset too —
logged **`GEPA Optimization: 606/608 rollouts`** live here, 2026-09-24,
matching the formula exactly (see *In this repository*, above).

### valset, reflection LM, merge, candidate selection

**Without a `valset`, GEPA uses the trainset for both**, and warns: "this is
useful as an inference-time scaling strategy where you want GEPA to find the
best solutions for the provided tasks in the trainset … it makes GEPA
overfit prompts" (`dspy:teleprompt/gepa/gepa.py:567-580`). With a valset over
35 rows it separately suggests shrinking it. GEPA's own advice inverts
MIPROv2's: **"maximize the training set and reserve only enough validation
examples to represent downstream behaviour"**
(`dspy-agent-skills:skills/dspy-gepa-optimizer/SKILL.md:132-134`, `[claim]`)
against MIPROv2's default 20/80 train/val split (above).

**`reflection_lm` (or a custom `instruction_proposer`) is required, and the
check runs at construction, not at `.compile()`.** [checked: gepa-asserts-reflection-lm]
`assert reflection_lm is not None or instruction_proposer is not None`
(`dspy:teleprompt/gepa/gepa.py:441-445`); the message recommends
`dspy.LM(model='gpt-5', temperature=1.0, max_tokens=32000)`. `teacher=` is
rejected outright rather than ignored: `assert teacher is None, "Teacher is
not supported in DspyGEPA yet."` (`dspy:teleprompt/gepa/gepa.py:544-545`).

**`use_merge=True, max_merge_invocations=5` by default** (note: the `gepa`
package's own default is `use_merge=False`; `dspy.GEPA` overrides it to
`True`). **`candidate_selection_strategy`**: DSPy types `"pareto"` (the
default — stochastic selection from the Pareto frontier of validation
scores) and `"current_best"`; the installed `gepa` 0.1.4 also accepts
`"epsilon_greedy"` (ε=0.1) and `"top_k_pareto"` as raw strings DSPy forwards
without typing. **`component_selector`**: `"round_robin"` (default, cycles
through predictors one at a time) or `"all"` (optimizes every predictor at
once); an unrecognised string constructs without error and fails only at
`.compile()` (`Unknown module_selector strategy: ...`).

**`skip_perfect_score=True` (default) skips reflection, not evaluation, when
every score in a minibatch is already perfect** — the budget is still spent
walking past those minibatches. Two book examples ran to completion with
**zero** reflection calls this way: an invoice-extraction benchmark made 393
task requests and 0 reflection requests and returned the seed instruction
unchanged, and a math example with two strong models (baseline 83.33% and
93.33%) accepted zero mutations
(`dspy-agent-skills:skills/dspy-book-use-cases/reference.md:51-55`,
`dspy-agent-skills:articles/03-inside-the-examples.md:48,75`, `[number]`). A
saturated baseline is not a broken run: "Baseline >0.95 means GEPA correctly
no-ops" (`dspy-agent-skills:skills/dspy-advanced-workflow/reference.md:120-128`,
`[claim]`).

### Cost, reflection and keyword traps — read from GEPA itself

Read from DSPy 3.3.1 and GEPA 0.1.4 themselves on 2026-09-25
(`Plan/concept/dspy-source_2026-09-24/gepa-core.md`):

- **GEPA cannot see what its reflection costs.** `dspy.GEPA` hands
  `gepa.optimize()` a plain callable, which GEPA wraps in `TrackingLM`; that
  wrapper counts estimated tokens and reports a cost of 0.0 forever.
  [checked: gepa-tracking-lm-cost-inert] `dspy.GEPA` refuses
  `max_reflection_cost` for that reason. A run's cost is what DSPy's own LM
  history records — `pairs.py` sums `GLOBAL_HISTORY` over the run, compile and
  reflection included.
- **`gepa_kwargs` is checked at `.compile()`, not at construction.** A key
  `gepa.optimize()` does not take — `enable_tool_optimization` belongs only to
  GEPA's own vendored adapter — constructs `dspy.GEPA` without complaint and
  raises `TypeError` when the run starts. [checked: gepa-kwargs-fail-at-compile]
- **`stop_callbacks` in `gepa_kwargs` do not replace the metric-call budget**,
  whatever `dspy.GEPA`'s docstring says: both stoppers run, and the first to
  fire ends the run (`gepa:src/gepa/api.py:252-295`).
- **The reflection model is stronger than the task model** in every production
  use the research reader found (task GPT-4.1-mini with GPT-5.1 reflecting;
  task gpt-5-mini with gpt-5.2-pro), and a task model that never fails gives
  reflection nothing to work on (`Plan/concept/dspy-source_2026-09-24/research.md`).
  `pairs.py run --optimizer gepa --reflection-model claude-cli/sonnet` with
  `--model claude-cli/haiku` is that shape; `--gepa-calls N` sets
  `max_metric_calls` instead of `auto="light"`.

### seed, log_dir, track_stats, Flex

**`seed=0` by default**, used to build `random.Random(self.seed)` and passed
through to `gepa.optimize(seed=...)` for reproducibility
(`dspy:teleprompt/gepa/gepa.py:582,660`). `pairs.py` pins it explicitly
(`seed=0`).

**`log_dir` resumes a run from its last checkpoint under the same directory**
— DSPy's own docstring: "Running GEPA with the same `log_dir` will resume the
run from the last checkpoint." One of the nine repositories built exactly on
this and got burned: `dspy-auto-gepa` always reuses
`<artifact_dir>/<name>/gepa_logs`, so a second `run(force=True)` on the same
task **loaded the prior state, made 4 student calls and 0 reflection calls,
and re-promoted the old best** — its own docs' comment on `run(force=True)`,
"Always retrain from scratch", is false (`dspy-auto-gepa:docs/basic.md:67`,
`dspy-auto-gepa:src/dspy_auto_gepa/runner.py:325-329`,
`dspy:teleprompt/gepa/gepa.py:305-307`, `[trap]`). `pairs.py` does not pass
`log_dir` at all, so this trap does not currently apply here, but any future
use of `log_dir` needs a fresh directory per run, recorded, the same way a
`--repeats` run needs the cache off (P18). What `log_dir` actually holds
(gepa 0.1.4): `candidates.json`, `run_log.json` (one entry per iteration),
`gepa_state.bin` (the resume checkpoint, pickle or cloudpickle),
`candidate_tree.html`, `generated_best_outputs_valset/task_<id>/`.

**`track_stats=True`** (`pairs.py` sets it) attaches `detailed_results` — a
frozen `DspyGEPAResult` dataclass with `candidates`, `parents`,
`val_aggregate_scores` (per-candidate, on the valset), `val_subscores`,
`per_val_instance_best_candidates`, `discovery_eval_counts`,
`best_outputs_valset`, `total_metric_calls`, `num_full_val_evals`, `log_dir`,
`seed`, and properties `best_idx`/`best_candidate` — to the **returned**
program (`dspy:teleprompt/gepa/gepa.py:64-127,666-668`). `track_best_outputs=True`
additionally requires `track_stats=True` (asserted at construction) and
populates `detailed_results.best_outputs_valset` — the recipe for using GEPA
as a batch inference-time search: `compile(student, trainset=batch,
valset=batch, track_stats=True, track_best_outputs=True)` and read the best
output per task back out (`dspy:teleprompt/gepa/gepa.py:235-243`).

**`dspy.Flex` submodules are components too.** `seed_candidate` is instruction
text per named predictor **plus** `module_src` per `Flex` submodule
(`dspy:teleprompt/gepa/gepa.py:628`); GEPA rewrites Flex's actual source code
inside the Deno sandbox the same way it rewrites another predictor's
instructions. Nothing in this repository builds a `dspy.Flex` module today
(`text-artifacts.md`).

### What fails silently

**A predictor never called in `forward()` is still a GEPA component, and gets
no feedback.** GEPA enumerates every entry of `student.named_predictors()`
regardless of whether `forward()` ever calls it, and matches trace entries to
a component by signature equality. A predictor that never runs logs "No valid
reflective examples found for {pred_name}" for that component alone, or, if
**no** selected component ever produced a trace, GEPA raises "No valid
predictions found for any module."
(`dspy-agent-skills` `das-patterns`: `named_predictors()` printed
`answer.predict` for a batch-compile program whose `forward()` never calls
`answer`; `dspy:teleprompt/gepa/gepa_utils.py:348,434-441`, `[trap]`). Restricting GEPA to a
subset of predictors is never demonstrated in any of the nine repositories'
own examples — the mechanism is to set `_compiled=True` on the sub-module to
freeze, since `named_parameters` skips anything already marked compiled
(`base_module.py:52-56`). `pairs.py`'s program is a single `dspy.Predict`, so
this trap does not bite there, but it is the first thing to check before
adding a second predictor to that program.

**A metric that raises during reflective-dataset construction is logged and
swallowed — GEPA finishes the whole budget and returns the seed program
unchanged, which looks exactly like "nothing to improve."** With a metric
that raises on every example, one measured run made 390 student calls across
baseline-and-train, 0 reflection calls, logged "Reflective mutation did not
propose a new candidate" every iteration, and returned the untouched seed
program (`dspy:teleprompt/gepa/gepa_utils.py:231-264`, its evaluation path
built on `failure_score`/`max_errors`/`raise_on_error=False`; the reflective
step itself logs and continues past the exception one level deeper, in the
`gepa` package `dspy-auto-gepa` runs through: `except Exception as e:
self.logger.log(f"Iteration {i}: Exception building reflective dataset:
{e}"); ...; continue`, `[trap]`) — the recommended defence is to run the metric on a few sample rows
first, count exceptions, and refuse the optimizer run if any occur (P15,
P23). **Metric exceptions during ordinary scoring** score `failure_score`
(0.0) through an inner `Evaluate(..., max_errors=len(batch)*100)`, but an
**LM provider or rate-limit error is re-raised, not scored** — `raise_on_exception=True`
is passed to `gepa.optimize` specifically so an unreachable model is never
folded into "answered badly" (P15).

### Traps in the documentation, not the code

Both budget tables published in the nine repositories' own skills disagree
with the real formula and with each other: one gives "light ~20–40 full
evals / medium ~80–150 / heavy ~300–600" with "each full eval ≈ `len(valset)`
metric calls", the other "light ~50 metric calls / medium ~200 / heavy
~500+"; for one predictor at `V=10` the real figures are 420, 740 and 1,105
metric calls (16.8, 29.6, 44.2 full evals) — neither table is close
(`dspy-agent-skills:skills/dspy-gepa-optimizer/SKILL.md:87-95`,
`dspy-agent-skills:skills/dspy-advanced-workflow/reference.md:98-100`, `[trap]`).
`detailed_results.candidate_programs` and `.reflection_traces` do not exist
(`AttributeError`) — the real attribute is `val_aggregate_scores`, per
*candidate*, not "Pareto frontier scores" as one skill's own docstring
mislabels it too. The documented `log_dir` layout (`candidates/<id>.json`,
`scores.jsonl`, `reflections/`) does not match what gepa 0.1.4 actually
writes (above). A documented `instruction_proposer` signature, `(program,
reflections, trace) -> str`, is wrong; the real one is `(candidate,
reflective_dataset, components_to_update) -> dict[str, str]`.

## BetterTogether

`dspy.BetterTogether(metric)`; `compile(student, *, trainset, teacher=None,
valset=None, num_threads=None, max_errors=None, seed=None, valset_ratio=0.1,
shuffle_trainset_between_steps=True, strategy="p -> w -> p",
optimizer_compile_args=None)`. Constructed the way the full signature reads
in the nine repositories, it also takes named sub-optimizers as keywords —
`BetterTogether(metric, **optimizers: Teleprompter)` — defaulting, when none
are named, to `p=BootstrapFewShotWithRandomSearch(metric)` and
`w=BootstrapFinetune(metric)`. **Changes both prompts and weights**, by
running the named sub-optimizers in the order `strategy` spells out.

**A non-`Teleprompter` value for a named optimizer raises `TypeError`.** The
strategy string's tokens must be exactly the constructor's keyword names —
the default `"p -> w -> p"` only means anything if the optimizers were named
`p=` and `w=`; naming them anything else and keeping the default strategy
raises `ValueError: Strategy contains invalid optimizer keys`.
[checked: bettertogether-strategy-keys] Two sibling
skills inside the same repository disagree about this on 3.3.1: one correctly
states the rule, the other teaches a call shape that raises
(`dspy-agent-skills:skills/dspy-gepa-optimizer/SKILL.md:88-92,113-114`,
`dspy:teleprompt/bettertogether.py`, `[trap]`).

**A failing step is swallowed, not raised.** An exception in any step logs an
ERROR and "Stopping optimization early. Returning best program found so far";
`compile` returns normally with `flag_compilation_error_occurred=True` set on
the returned program — check that flag, since nothing else marks the failure
(`dspy:teleprompt/bettertogether.py:470-503`, `[trap]`).

**Without a `valset`, the first 10% of the trainset, unshuffled, becomes
validation** (`valset_ratio=0.1`); at 10 rows that is a single-example
valset, logged as "Created validation set: 1 examples. Training set: 9
examples." At `valset_ratio=0` there is no validation at all and the latest
program simply wins (`dspy:teleprompt/bettertogether.py:320-345`, `[trap]`).
Returns `candidate_programs`: `{program, score, strategy}` sorted best first,
baseline counted as strategy `""`, ties keep the earlier program.

**Measured**: `p=prompt_optimizer, w=finetuner, strategy="p -> w"`: val 60.00,
**test 65.00 (52/80), +13.75** — from a **different** 51.25% baseline (the
finetuned student's own zero-shot score, not the 53.75% baseline every
prompt-only row is measured against), **$0.8445, 1740.0 s — the slowest of
all twelve runs**
(`dspy-agent-skills:skills/dspy-book-optimizers/reference.md:46,95-105`,
`[number]`).

**Not taken here**: "not this shape of problem" — no weight-optimizable
model in play, and BetterTogether's default weight stage needs one
(`Plan/concept/optimizers-and-data_2026-09-17.md`).

## BootstrapFinetune

`dspy.BootstrapFinetune(metric=None, multitask=True, train_kwargs=None,
adapter=None, exclude_demos=False, num_threads=None)`; `compile(student,
trainset, teacher=None)`. **Changes model weights** — the only optimizer on
any list here that does, not prompts or demos. Builds a fine-tuning dataset
from bootstrapped traces (`bootstrap_trace_data`) and hands it to the
provider's fine-tune path (local or hosted).

**Needs a fine-tunable model and local training infrastructure.** The book's
run trained `Qwen/Qwen2.5-0.5B-Instruct` via a `LocalProvider`, PyTorch +
Transformers + TRL + PEFT (LoRA, `use_peft=True`), 10 epochs, batch size 1,
gradient accumulation 4, learning rate 2e-4, max sequence length 768, on
Apple MPS or CUDA. Measured: val 70.00, **test 70.00 (56/80), +18.75 — but
from its own 51.25% baseline** (the small model's own zero-shot score, not
the 53.75% baseline the prompt-only rows share), **$0.8651, 1026.3 s**
(`dspy-agent-skills:skills/dspy-book-optimizers/reference.md:45,52-53,107-117`,
`[number]`). Its **test-equals-validation** (70.00/70.00) is not, on its own,
unique in the twelve-row table — see *The measured comparison*, below.

**Not taken here**: needs a fine-tunable model; this project's models are
free, hosted OpenRouter models, not fine-tunable through this path
(`Plan/concept/optimizers-and-data_2026-09-17.md`).

## Ensemble

`dspy.Ensemble(*, reduce_fn=None, size=None, deterministic=False)`;
`compile(programs)` — **not** `(student, trainset)` like every other
optimizer here; no trainset, no metric, and `programs` must already be
compiled. `deterministic=True` raises `AssertionError` immediately ("TODO:
Implement example hashing for deterministic ensemble.") — the parameter
exists in the signature but only `False` is implemented
(`dspy:teleprompt/ensemble.py:14`). **Changes nothing about any of the
wrapped programs**; it wraps N already-built programs into one that, per
call, runs every one of them **sequentially** in a plain list comprehension
(latency is additive, never parallel), `size` draws a random subset per call
using the unseeded global `random` module, and `reduce_fn` (commonly
`dspy.majority`) combines the outputs; with no `reduce_fn` it returns the raw
list of every program's output (`dspy:teleprompt/ensemble.py:23-39`).

**Measured**: three already-compiled programs (`LabeledFewShot`,
`BootstrapFewShot`, `BootstrapRS`), `Ensemble(reduce_fn=boolean_majority).compile([...])`:
val 65.00, **test 70.00 (56/80), +16.25**, **$0.8881, 1151.2 s**; mean per-call
latency **4.803 s vs 1.789 s baseline (2.68×)**, "because every component runs
on every example, forever"
(`dspy-agent-skills:skills/dspy-book-optimizers/reference.md:44,78-93`,
`[number]`) — unlike every optimizer above, Ensemble's cost is paid **per
call, forever**, not once at compile time.

**Not taken here**: "nothing to ensemble yet" — Ensemble needs several
already-compiled candidate programs to combine, and this project has not
compiled even one
(`Plan/concept/optimizers-and-data_2026-09-17.md`).

## AvatarOptimizer

`dspy.AvatarOptimizer(metric, max_iters=10, lower_bound=0, upper_bound=1,
max_positive_inputs=None, max_negative_inputs=None, optimize_for="max")`.
**Cannot be constructed at all on the installed package.** `__init__` builds
`self.comparator = dspy.TypedPredictor(Comparator)`
(`dspy:teleprompt/avatar_optimizer.py:90`), and `dspy.TypedPredictor` does
not exist in DSPy 3.3.1. Confirmed directly here, offline, 2026-09-24:

```python
>>> dspy.AvatarOptimizer(metric=lambda ex, pred: 1.0)
AttributeError: module 'dspy' has no attribute 'TypedPredictor'
```

every other argument is irrelevant — the failure happens on the second line
of `__init__`, before `metric` or anything else is even used. This is a
DSPy 3.3.1 defect in the optimizer itself, independently confirmed by two of
the nine repositories against the installed package
(`dspydantic:src/dspydantic/optimizer.py`, cross-referenced against
`dspy-agent-skills`'s own construction sweep).

Even if it constructed, it optimizes a `dspy.Avatar`-shaped tool-using agent
specifically — its `Comparator`/`FeedbackBasedInstruction` signatures compare
positive- and negative-scoring runs and rewrite the agent's instruction — a
module shape nothing in this repository builds (`api.md`'s module table has
no `Avatar`; the nearest tool-using modules are `ReAct` and `RLM`, neither of
which this optimizer targets).

**Not taken here**: "not this shape of problem"
(`Plan/concept/optimizers-and-data_2026-09-17.md`), written before this
defect was found — now doubly true, since the package currently makes the
decision on its own.

## The measured comparison

One dataset, one task (AI-generated-text detection), one model pair, DSPy
3.3.0 pinned by the chapter (re-verified against 3.3.1 here where noted): 300
rows, pair-grouped 160 train / 60 validation / **80 locked test**
(`dspy-agent-skills:skills/dspy-book-optimizers/SKILL.md:24-33`). Eleven
optimizer runs plus the unoptimized baseline — the chapter's own "twelve
optimizers" headline counts the baseline as the twelfth
(`dspy-agent-skills:skills/dspy-book-optimizers/SKILL.md:5`, `[trap]`):

| rung | config | val | test (n/80) | Δ test | cost | time |
|---|---|--:|--:|--:|--:|--:|
| (baseline) | unoptimized | 55.00 | 53.75 (43) | — | $0 | 0 s |
| LabeledFewShot | k=4 | 63.33 | 67.50 (54) | +13.75 | $0.0000 | 0.0 s |
| BootstrapFewShot | 2 demos | 66.67 | 67.50 (54) | +13.75 | $0.0030 | 4.5 s |
| BootstrapRS | 8 candidates | 61.67 | 65.00 (52) | +11.25 | $0.8766 | 1119.1 s |
| KNNFewShot | k=4, local embedder | 71.67 | 72.50 (58) | +18.75 | $0.00 | 0 s |
| COPRO | breadth=4, depth=2 | 53.33 | 50.00 (40) | **−3.75** | ≥$0.0732 | 861.1 s |
| MIPROv2 | auto=light, seed=42 | 76.67 | 66.25 (53) | +12.50 | ≥$0.3052 | 270.8 s |
| **GEPA** | auto=light, seed=42 | **80.00** | **80.00 (64)** | **+26.25** | $0.6220¹ | 616.7 s |
| SIMBA | bsize=8 | 51.67 | 47.50 (38) | **−6.25** | **$1.1413** | 321.3 s |
| Ensemble | 3 programs, majority | 65.00 | 70.00 (56) | +16.25 | $0.8881 | 1151.2 s |
| BootstrapFinetune | Qwen2.5-0.5B, LoRA | 70.00 | 70.00 (56) | +18.75² | $0.8651 | 1026.3 s |
| BetterTogether | p=prompt, w=finetune | 60.00 | 65.00 (52) | +13.75² | $0.8445 | **1740.0 s** |

¹ $0.5824 optimization + $0.0396 evaluation, 684 metric calls, 10 candidates.
² measured against a **different**, 51.25%, baseline — the fine-tuned
student's own zero-shot score, not the shared 53.75% row above; not directly
comparable to the other Δ figures.

(`dspy-agent-skills:skills/dspy-book-optimizers/SKILL.md`,
`dspy-agent-skills:skills/dspy-book-optimizers/reference.md:29-117`, `[number]`)

**The four lessons the chapter draws, in its own words**: (1) "optimizing can
make it worse" — COPRO and SIMBA both scored below the unoptimized baseline,
"if you do not measure a baseline and a held-out test set, you cannot detect
this"; (2) free optimizers are not the weak ones — by test accuracy, both
free runs beat five of the ten paid ones, and `KNNFewShot` alone beats eight;
(3) "validation gain is not test gain" — report the held-out number, not the
number the optimizer selected on; (4) "cost does not predict quality" — extra
compile spend "buys candidate selection, not a new instruction." Uplift per
dollar among the **paid, positive** runs: BootstrapFewShot 4583 points/$,
GEPA 45.1, MIPROv2 41.0, BootstrapFinetune 21.7, Ensemble 18.3, BetterTogether
16.3, BootstrapRS 12.8 — COPRO and SIMBA are excluded, having gone negative
(`dspy-agent-skills:skills/dspy-book-optimizers/SKILL.md:53-72`, `[number]`).

**The statistics attached to the one winning row, and their limit.** GEPA's
+26.25 carries a McNemar test (p = 0.000104 across 29 discordant pairs) and a
bootstrap 95% CI of [16.25, 36.25] points over 40 pairs, 10,000 samples — the
one row in the whole table with any significance test attached at all
(`dspy-agent-skills:skills/dspy-book-optimizers/reference.md:121-132`,
`[number]`). Every other row in the table is a **single run, one seed, no
repeats** (P18) — and single-seed spread on a comparable task, measured
across DSPy versions in the same repository, is as large as several of the
reported gains: the same invoice-extraction task scored a committed baseline
of 0.833, a 3.1.3 probe of 0.739 (interrupted early, best observed 0.944), and
a 3.2.0 baseline of 0.944 — a **0.205 spread** against a reported GEPA gain of
0.098 on that task; a RAG-QA task swung 86.10→91.75 on 3.1.3 versus
80.47→100.00 on 3.2.0 with the same model pair
(`dspy-agent-skills:articles/03-inside-the-examples.md:22,126`, `[number]`).
Two more caveats specific to this table: the article that reports these
numbers elsewhere calls the **selection-set** score (the same valset GEPA
picked its winning candidate on) the "final" number, which is exactly what
the optimizers chapter's own rule says not to report
(`dspy-agent-skills:articles/03-inside-the-examples.md:112`, `[trap]`); and
the chapter's own claim that "GEPA was the only optimizer where validation
and test agreed exactly" is false by its own table — BootstrapFinetune's gap
is 0.0 too (`dspy-agent-skills:skills/dspy-book-optimizers/example_optimizer_results.py:108-109`,
`[trap]`). **Read this table as one dataset's one run each, not as a ranking
that would replay.**

## Sessions inside optimizers

`dspy-session` wraps a module to give it conversation memory; none of the
five optimizers above are built to see through that wrapper, and the
findings are specific enough to name even though nothing in this repository
wraps a module today.

**Every DSPy optimizer silently no-ops on a `dspy_session`-wrapped module by
default, without an error.** `_wrap_predictor` reads the predictor's own
`forward` once, `orig_forward = self._get_attr_quiet(predictor, "forward")`,
and installs a closure over it as the new method:
`predictor.forward = types.MethodType(wrapped_forward, predictor)` where
`wrapped_forward` injects history from a contextvar and then always calls
`return orig_forward(**kwargs)`
(`dspy-session:dspy_session/session.py:557-572`). `orig_forward` is bound to
whichever predictor object existed at wrap time. `copy.deepcopy` (what
`fork()` does to build its cloned module,
`dspy-session:dspy_session/session.py:1052-1066`) rebinds the wrapper method
itself to the copy, but the closure inside it still calls the *original*'s
forward — so after `deepcopy()`, `fork()`, `reset_copy()`, or any optimizer's
own internal copying: calls run on the original's signature, demos and LM;
demos an optimizer sets on the copy are never read; demos set on the original
leak into every copy and fork instead (`[trap]`, the reading's own probe:
"closure bound to ORIGINAL; copy demo in prompt False; original demo in
copy's prompt True, in fork's True"). A compile that reports success and a
copy that never changes are indistinguishable without checking which object
actually answers.

**The README's own `BootstrapFewShot` recipe fails on 3.3.1 for a related,
independent reason.** `dspy.BootstrapFewShot().compile(session,
trainset=examples)` logs "Bootstrapped 2 full traces after 2 examples" and
leaves **0 demos** on the compiled predictor. The trace records the
*original* predictor object; `self.predictor2name[id(predictor)]` then raises
`KeyError` for it, and `BootstrapFewShot` drops the step silently — `except
KeyError: continue  # FIXME: !`, the maintainers' own comment
(`dspy:teleprompt/bootstrap.py:228-230`) — rather than raising or warning.
Nothing in `dspy.Evaluate`'s or `BootstrapFewShot`'s own logging says a demo
was dropped; the run just ends with fewer demos than traces bootstrapped.

**The path that does work**: optimize an *unwrapped* module whose signature
already declares a `history: dspy.History` field, trained on
`session.to_examples()`, then call `session.update_module(optimized)` — it
deep-copies the optimized module, re-patches the signature, and wraps it with
a closure bound to the *new* copy, so the wrapping and the optimizing never
happen on the same object at the same time
(`dspy-session:dspy_session/session.py:1006-1010`, `[recipe]`).

**A student signature with no `history` field drops history from every
example, and the optimizer never sees it was there.** The README's own GEPA
example compiles `dspy.Predict(Support)` — a signature with no `history`
field — on `session.to_examples()`; every example's `history` is silently
dropped at the adapter (a warning fires; nothing stops the run), so GEPA
reflects on each turn as if it were a single, contextless exchange. Calling
`session.update_module(optimized)` afterwards adds history back in, but to a
module GEPA never optimized *with* it (`README.md`, `[trap]`). And a
compiled or forked session's deep copy includes the accumulated
`_default_state.turns`, so a freshly "optimized" program still continues the
*old* conversation it was copied from — the README's own worked answer
literally references an earlier turn ("just like we did for x²")
(`README.md`, `[pattern]`).

## Non-DSPy optimizers in the nine repositories

Two of the nine repositories implement their own optimization loop, calling
no DSPy `Teleprompter` at all. `dspydantic`'s field-description optimizer is
**not** a third one: `_create_teleprompter` (Choosing an optimizer, above)
constructs real `dspy.BootstrapFewShot`/`COPRO`/`MIPROv2`/etc. instances and
compiles each field through one of them — its own contribution is the
accept-or-revert wrapper and the n-based selection rule around them, both
already covered above.

**`dspy-optimizer`'s critique→repair loop.** `PromptOptimizer(signature,
initial_prompt, merger_strategy="block_based", validation_strategy="full",
config=Config())` subclasses `dspy.Module` but has no `forward`;
`optimize(dataset, scorer, callbacks=None)` returns a final prompt **string**,
never a program (`dspy-optimizer:dspy_optimizer/optimizer.py:13-58,195`,
`[api]`). Its real loop, read from the source, is **Evaluator → scorer →
Refiner → Merger → Validator**, not the "Evaluator → Refiner → Validator →
Merger" order its own README states — merging precedes validation
(`dspy-optimizer:dspy_optimizer/optimizer.py:86-190`, `[trap]`): for each
wrong example, up to `Config.max_refine_iters=5` times, a `ChainOfThought`
Refiner proposes a patch, the Merger applies it to build a **candidate**
prompt, the Validator scores the candidate, and on success the candidate
replaces the live prompt immediately — so it applies to every later example
in the same pass, mid-optimization. **Validation runs on the training set
itself** — the same `dataset` being optimized, never a held-out one, despite
the design doc promising a separate validation set
(`dspy-optimizer:dspy_optimizer/optimizer.py:152-158`, `[trap]`). Strategy
parameters are fixed at construction with no arguments
(`batch_size=10, sample_size=3, threshold=1.0`, unconfigurable short of
overwriting the instance directly); the evaluation counter under-counts
(`total_evaluations += 1` once per validation call regardless of how many
evaluator calls the validator itself made — the code's own comment: "TODO:
This is a simplification"); `Config.temperature` and `parallel_workers` are
declared and never read, so evaluation is sequential despite the README's
"parallel evaluation" claim
(`dspy-optimizer:dspy_optimizer/optimizer.py:159-161`,
`dspy-optimizer:dspy_optimizer/models.py:7-19`, `[trap]`).

**`braid-dspy`'s `BraidOptimizer`.** A `dspy.Module` with no `forward` —
purely a wrapper (`braid-dspy:braid/optimizer.py:315-344`, `[api]`). It calls
a real DSPy `Teleprompter` underneath (`self.base_optimizer.compile(...)`),
but with two defects that make the compile pointless by default: (1)
**`_optimize_planning` compiles a predictor the default program never
calls** — `BraidReasoning(use_generator=True)`, the default, plans through
`self.generator.predictor`, not the `module.plan` predictor `BraidOptimizer`
compiles, so those demos are dead on arrival; verified with
`LabeledFewShot(k=2)`: `plan.demos == 2`, `generator.predictor.demos == 0`
(`braid-dspy:braid/optimizer.py:381-418,420-464`,
`braid-dspy:braid/module.py:94-117`, `[trap]`); (2) **its own metric contract
never reaches the base optimizer** — `BraidOptimizer.optimize(module,
trainset, metric)` expects `metric(result: BraidResult, expected_answer)`,
but the base optimizer is constructed with, and calls, **its own** metric in
ordinary DSPy shape (`example, prediction, trace=None`) on the sub-predictor's
output — the two metrics never talk to each other
(`braid-dspy:braid/optimizer.py:346-379,416,438,460-462`, `[pattern]`). Its
training examples are built without `.with_inputs()` (`input_keys=None`),
which triggers the same `BootstrapFewShot` truthiness family of failures
described above — logged, not raised, and labelled demos are installed
anyway (`braid-dspy:braid/optimizer.py:413-415,451-457`, `[trap]`). With no
base optimizer at all, `optimize()` is a **documented no-op**:
`_simple_optimize` returns the module unchanged while its own example script
still prints "Optimization completed" and "Score improvement: +0.000"
(`braid-dspy:braid/optimizer.py:466-473`, `[trap]`).

**`dspy-advanced-prompting`'s "distillation" module** is prompt editing under
an optimizer's name, not an optimizer: `_create_distilled_prompt` per
strategy either returns the original prompt unchanged (`DIRECT`), appends
three hardcoded examples out of a `num_examples` default of 100 — 97 wasted
teacher calls — (`SYNTHETIC`), or appends fixed generic text (`CHAIN`,
`SELECTIVE`, `ENSEMBLE`); neither the "teacher" nor the "student" predictor is
ever given its own LM via `Module.set_lm` (available since before 3.3.1), so
both run on whatever `dspy.settings.lm` happens to be configured — the
teacher/student distinction is cosmetic
(`dspy-advanced-prompting:src/techniques/model_distillation.py:54-57,93-98,162,178-255,284,317-336,338-354`,
`[trap]`). Its loop also stops after exactly one iteration by construction:
`quality_retention = 0.88 / 0.95` is two hardcoded constants, always
`0.9263`, permanently above the default `quality_threshold=0.9`.

## Not taken

| thing | why, and what already covers it |
|---|---|
| `MIPROv2` | "100+" examples in every source that gives a threshold; the compile trainset here is 63 labelled pairs, 49 to 51 per fold — see MIPROv2, above |
| `BootstrapFewShotWithRandomSearch` ("random search") | "50+" examples; its own measured cost (8 candidates, $0.88, 1119 s) exceeds GEPA's for less than half the gain — see the section above |
| synthetic data generation | grouped with the two above in `Plan/concept/dspy-toolchain_2026-09-23.md` under the same "100+/50+" reason. `dspy-auto-gepa`'s `AutoData` is the nine repositories' own instance of this: it generates rows with an LLM from seed examples, but its allowed output values come **only from the seed rows** (a `Literal` type annotation is ignored; no seed of a class means no rows of that class ever get generated — `dspy-auto-gepa:src/dspy_auto_gepa/data.py:43-57,86,90`, `[trap]`), and its judge **never rejects a row** — scores are recorded, never thresholded, so a synthetically generated row scored 0.0 for quality is accepted anyway (`dspy-auto-gepa:src/dspy_auto_gepa/generator.py:1193-1227,1399-1403`, `[trap]`). Synthetic rows would not, by themselves, fix this project's undersized residual with a check this project would trust |
| LLM-drafted metrics | `Plan/concept/dspy-toolchain_2026-09-23.md`, *Deliberately not taken*: "the rule a program is scored by is written by a person; the `metric=Path(...)` bypass is the only path used." `dspy-auto-gepa` is the instance this refuses: by default it has `dspy.RLM` **draft a `metric.py` file** from a natural-language spec — a 215-line prompt of rules and three worked examples is the model's only instruction (`dspy-auto-gepa:src/dspy_auto_gepa/metric_builder.py:9-233,229-233,286-294`, `[pattern]`) — unless a human-written `metric=Path(...)` is passed instead, which is the only path this project would ever take. Its own documented "generate, review, then run" workflow does not survive a retrain: `run(force=True)` regenerates the metric file again, silently discarding a human's edit (`dspy-auto-gepa:src/dspy_auto_gepa/runner.py:388-394`, `[trap]`) — a sharp illustration of why a metric stays a person's file, never a step that reruns |
| `BootstrapFinetune`, `BetterTogether`, `Ensemble`, `AvatarOptimizer` | each has its own reason in its own section above — a need for a fine-tunable model, nothing yet to ensemble, or (`AvatarOptimizer`) a defect in the installed package itself |
| `COPRO` | neither ruled in nor ruled out — an omission in this project's own concept doc, not a decision; see COPRO, above |
| `KNNFewShot` | not refused, waiting — see its own section: cheap once a local embedding model is already paid for elsewhere in this project (`qmd`) |
