# optimizers-classic — DSPy 3.3.1's `dspy/teleprompt/` (minus `gepa/`) and `dspy/propose/`

## 1. Header

**Slice**: every file in `dspy/teleprompt/` except the `gepa/` subfolder, plus all of
`dspy/propose/`; the matching tests and the matching docs (see brief for exact list).

**Files read, in full**: 20 of `dspy/teleprompt/*.py` (5,268 lines: `mipro_optimizer_v2.py` 866,
`grpo.py` 635, `bettertogether.py` 631, `utils.py` 463, `simba.py` 377, `simba_utils.py` 253,
`copro_optimizer.py` 356, `bootstrap_finetune.py` 324, `avatar_optimizer.py` 217,
`random_search.py` 168, `bootstrap_trace.py` 153, `infer_rules.py` 152,
`teleprompt_optuna.py` 89, `teleprompt.py` 86, `knn_fewshot.py` 69, `signature_opt.py` 52,
`ensemble.py` 40, `vanilla.py` 30, `bootstrap.py` 272, `__init__.py` 35); all 5 of
`dspy/propose/*.py` (723 lines). Tests: full reads of `test_bootstrap.py`,
`test_bootstrap_finetune.py`, `test_bootstrap_trace.py`, `test_teleprompt.py`,
`test_random_search.py`, `test_copro_optimizer.py` (header), `test_grounded_proposer.py`,
`test_finetune.py` (1 line, a `# TODO` stub); every other test file's `def test_*`/
`pytest.raises`/`class Test*` lines read via `grep -n` (`test_bettertogether.py` 744,
`test_bootstrap_finetune.py`, `test_ensemble.py`, `test_grpo.py`, `test_knn_fewshot.py`,
`test_utils.py`) — structure and assertions read, not narrated line-by-line, per the
economy directive received mid-task. Docs: all 14 non-GEPA files in
`docs/docs/api/optimizers/`, both `docs/docs/learn/optimization/*.md`, both
`docs/docs/diving-deeper/{bootstrap-fewshot-family,choosing-an-optimizer}.md`, and the seven
tutorial entries (`optimize_ai_program`, `classification`, `rl_ai_program`, `papillon` as
short landing pages read in full; `classification_finetuning`, `rl_multihop`, `rl_papillon`
notebooks grepped for the optimizer-relevant cells, per the brief's "may be skimmed past
their output cells").

**What I ran**: `.venv-dspy/bin/python` with all four `*_API_KEY` vars unset, offline, against
the **installed** package (`.venv-dspy/lib/python3.11/site-packages/dspy`) — construction
probes for `GRPO`, `SignatureOptimizer`, `InferRules(num_candidates=0)`,
`COPRO(depth=0)` (via this repo's own `scripts/lm_fixture.FixtureLM`), a live
`reset_copy()`/`.lm` probe using `dspy.utils.dummies.DummyLM`, and one `inspect.signature`
dump over every class in the slice plus `create_dataset_summary`/`bootstrap_trace_data`.
Also one interpreter check that `list() / list()` raises `TypeError`, confirming the
arithmetic in a bug found by reading. `diff -rq` between the tag and the installed package
was not re-run (the brief's own header already states the two are identical outside
`__metadata__.py`, and this slice touches no files under `.venv-dspy` that would differ).

**What this part of DSPy is**: the "classic" (pre-GEPA) optimizer ladder — demo bootstrapping
(`LabeledFewShot`, `BootstrapFewShot`, its random-search and Optuna variants, `KNNFewShot`),
instruction search (`COPRO`, its dead `SignatureOptimizer` alias, `MIPROv2`, `SIMBA`,
`InferRules`), weight tuning (`BootstrapFinetune`, `GRPO`), and composition
(`BetterTogether`, `Ensemble`, the unconstructable `AvatarOptimizer`) — plus
`dspy.propose.GroundedProposer`, the instruction-proposal engine `MIPROv2` uses internally.
Every optimizer here mutates prompts, demos or (for `BootstrapFinetune`/`GRPO`) an LM's
weights; none of it touches retrieval, RL environments beyond `GRPO`, or the reflective
GEPA machinery, which is another reader's slice.

## 2. Knowledge items

### `## OPT`

**Cross-cutting, before the per-optimizer detail:**

- **`reset_copy()` wipes every predictor's `.lm` to `None`** — `LabeledFewShot.compile()`
  (`dspy/teleprompt/vanilla.py:11`) and `BootstrapFewShot._prepare_student_and_teacher`
  (`dspy/teleprompt/bootstrap.py:97`) both open with `self.student = student.reset_copy()`.
  `reset_copy()` is `deepcopy()` + `.reset()` on every parameter
  (`dspy/primitives/base_module.py:147-154`), and `Predict.reset()` sets
  `self.lm = None, self.demos = [], self.traces = [], self.train = []`
  (`dspy/predict/predict.py:65-69`). So even if you called `student.set_lm(my_lm)` first,
  the program `BootstrapFewShot`/`LabeledFewShot`/`InferRules` (a `BootstrapFewShot`
  subclass) hand back has `predictor.lm is None` on every predictor, relying entirely on
  whatever `dspy.settings.lm`/`dspy.context(lm=...)` is active at call time. [trap]
  (verified: ran offline — `student.set_lm(lm)` then `LabeledFewShot(k=1).compile(...)` and
  `BootstrapFewShot(...).compile(...)`, both left `compiled.predictors()[0].lm is None ==
  True`) · skill: **new**
- **`BootstrapFewShotWithRandomSearch`'s `seed=-3` (zero-shot) candidate is built via
  `student.reset_copy()`** (`dspy/teleprompt/random_search.py:82-83`) — one concrete instance
  of the reset above, and the one `dspy/teleprompt/bettertogether.py:552-563` names in its
  own comment as a defect it has to work around (below). [trap] (verified: read + the
  `reset_copy`/`Predict.reset` chain above, run) · skill: **new**
- **The official docs assert a blanket rule that is false for at least two optimizers in this
  slice.** `docs/docs/diving-deeper/choosing-an-optimizer.md:15-17`: "The first thing every
  optimizer does is `student.reset_copy()`... The compiled program is returned; the original
  you passed in stays untouched." `COPRO.compile` uses a plain `student.deepcopy()`
  (`dspy/teleprompt/copro_optimizer.py:137`), not `reset_copy()`.
  `BootstrapFinetune.compile` never copies the student at all — it does
  `pred.lm = finetuned_lm` on the passed-in object's own predictors
  (`dspy/teleprompt/bootstrap_finetune.py:126`) and `student._compiled = True; return student`
  (`:133-134`). `GRPO.compile` does the same — `student._compiled = True; return student`
  (`dspy/teleprompt/grpo.py:611-612`), with predictor `.lm` objects mutated in place by
  `job.step()` per its own comment ("We update the `.model` field of this LM... which also
  updates the LM in the student program since these point to the same reference",
  `grpo.py:524-528`). Both halves of the doc's sentence are wrong for these two. [trap]
  (verified: read, all three code paths) · skill: **wrong**: no file in the skill states or
  contradicts this, so it is new information, but flagged `wrong` against the doc it quotes
- **A recurring cache-bypass idiom: fresh `rollout_id` + `temperature=1.0`.** Appears
  independently in `bootstrap.py:191` (`BootstrapFewShot`'s extra rounds),
  `simba_utils.py:30` (`prepare_models_for_resampling`), `infer_rules.py:146-148`
  (`RulesInductionProgram.forward`), and `grounded_proposer.py:395-398`
  (`propose_instruction_for_predictor`'s `rollout_lm`). Every one of these calls runs at
  `temperature=1.0` **regardless of what temperature the configured LM was given** — the
  optimizer-exposed `temperature_for_*`/`init_temperature` knobs (SIMBA, COPRO, MIPROv2,
  GroundedProposer) control something else (see SIMBA, below), never this rollout
  temperature. [pattern] (verified: read, four sites) · skill: **new**
- **`Teleprompter.__init_subclass__` auto-wraps every subclass's own `compile` with callback
  instrumentation, with a reentrancy guard.** Any class that defines `compile` in its own
  body gets it wrapped by `with_callbacks`, tracked via a context-var `_ACTIVE_COMPILES`
  keyed by `(id(instance), thread_id, task_id)` so a **same-instance** nested call (e.g.
  `InferRules.compile` calling `super().compile()`) skips re-wrapping, but a **different**
  instance constructed internally (e.g. `BootstrapFewShotWithRandomSearch` building its own
  `BootstrapFewShot(...)` each seed) fires its own callbacks independently
  (`dspy/teleprompt/teleprompt.py:12-50`). [api] (verified: read) · skill: **new**
- **`get_params()` is `self.__dict__`, verbatim** (`dspy/teleprompt/teleprompt.py:79-86`,
  confirmed by DSPy's own `tests/teleprompt/test_teleprompt.py:14-17`, which only checks the
  trivial two-constructor-kwarg case). On a `BootstrapFewShot` instance **after** a compile
  this also dumps `self.student`, `self.teacher`, `self.trainset`, `self.validation`,
  `self.name2traces` — every intermediate object the compile touched, not just the
  hyperparameters (`bootstrap.py`'s heavy use of `self.X = ...` through `compile`/
  `_bootstrap`/`_train`). [trap] (verified: read + DSPy's own test) · skill: **new**
- **`all_predictors_have_lms(student)` is called three times for its return value and the
  return value is thrown away every time.** `bootstrap_finetune.py:67` (inside
  `BootstrapFinetune.compile`), `grpo.py:293` (inside `GRPO.compile`), and
  `bettertogether.py:311` (inside `BetterTogether._prepare_student_and_teacher`) each call it
  as a bare statement. The **actual** enforcement in `BootstrapFinetune` is a separate,
  later, per-predictor `if pred.lm is None: raise ValueError(...)` (`bootstrap_finetune.py:
  82-87`); `GRPO` has **no substitute check at all** — its own guard,
  `assert len(student_lms) == 1` on `{id(pred.lm) for pred in student.predictors()}`
  (`grpo.py:281-286`), would pass an all-`None`-LM program too, since `{id(None)}` also has
  length 1. `BetterTogether` is the one place the same helper is also used **correctly**,
  in an `if not all_predictors_have_lms(student): ...` guard, later in the same file
  (`bettertogether.py:557-563`) — so one file both misuses and correctly uses the identical
  function. [trap] (verified: read, three call sites plus the one correct one) · skill: **new**
- **`dspy/teleprompt/utils.py` monkey-patches `inspect.getfile` at import time, globally.**
  `inspect.getfile = new_getfile` runs as the last line of the module
  (`dspy/teleprompt/utils.py:463`) — importing this module (which every optimizer does,
  transitively, via `from dspy.teleprompt.utils import ...`) silently changes stdlib
  `inspect.getfile` behaviour process-wide, to work around Jupyter-cell source lookup. [trap]
  (verified: read) · skill: **new**

**`LabeledFewShot`** (`dspy/teleprompt/vanilla.py`, 30 lines):

- `dspy.LabeledFewShot(k=16)`; `compile(student, *, trainset, sample=True)`. `k` is applied
  as `min(k, len(trainset))`. [api] (verified: `inspect.signature` on the installed
  package) · skill: same
- **An empty trainset does not return the literal input `student`** — it returns
  `student.reset_copy()` (line 11 runs unconditionally, before the `len(trainset)==0` early
  return at line 14-15) — a fresh object with `.lm=None` and `.demos=[]`, not the caller's
  original. `optimizers.md`'s "An empty trainset returns the student unchanged" reads as
  identity-preserving; it is not. [trap] (verified: read) · skill: **wrong**:
  `optimizers.md` says "An empty trainset returns the student unchanged"
- One `rng = random.Random(0)` is created **once per `compile()` call**, outside the
  per-predictor loop, and `rng.sample(...)` is called once per predictor — so a
  **multi**-predictor program gets a **different** (though still seed-0-deterministic) demo
  sample per predictor, not the same k-subset repeated. [pattern] (verified: read) ·
  skill: **new**

**`BootstrapFewShot`** (`dspy/teleprompt/bootstrap.py`, 272 lines):

- `dspy.BootstrapFewShot(metric=None, metric_threshold=None, teacher_settings=None,
  max_bootstrapped_demos=4, max_labeled_demos=16, max_rounds=1, max_errors=None)`;
  `compile(student, *, teacher=None, trainset)`. [api] (verified: `inspect.signature`) ·
  skill: same
- **Order it consumes the trainset**: literal list order, never shuffled
  (`_bootstrap`, `bootstrap.py:155`), and it **stops early**: `if len(bootstrapped) >=
  max_bootstraps: break` is checked **before** each new example (`:156-157`), so once enough
  successful demos exist the rest of the trainset is never even attempted by the teacher.
  Worst case (nothing ever passes) is `len(trainset) * max_rounds` teacher calls; best case
  is as few as `max_bootstrapped_demos`. [number] (verified: read — derived from the loop,
  not measured) · skill: **new**
- **Teacher default is `teacher.deepcopy()` if given, else `student.deepcopy()`** — a plain
  deepcopy, **not** `reset_copy()` — so the teacher (unlike the student half of the same
  method) keeps its original `.lm`. The source comment marks this as a change: "NOTE:
  behavior change on Oct 28, 2024. Deep copy instead of reset copy for the student-as-teacher"
  (`bootstrap.py:99-100`). If the teacher isn't already compiled and `max_labeled_demos > 0`,
  it is **then** replaced by `LabeledFewShot(k=max_labeled_demos).compile(teacher.reset_copy(),
  trainset=trainset)` (`:104-106`) — which wipes the teacher's `.lm` too, through a second,
  separate path. [trap] (verified: read) · skill: **new**
- **Which trace becomes a demo, when a predictor fires more than once in one example, is
  chosen by a content-hash-seeded RNG, not any compile-level seed** (there is none):
  `rng = random.Random(Hasher.hash(tuple(demos)))`, then `rng.choice(demos[:-1])` half the
  time, else the last one (`bootstrap.py:250-254`). Deterministic given the same demo
  content, unrelated to `max_rounds`'s own `rollout_id`. [pattern] (verified: read) ·
  skill: **new**
- **`_train()`'s raw-demo sampling has an undocumented cross-predictor interaction.**
  `raw_demos = self.validation` is set once, but inside the per-predictor loop it is
  **reassigned**: `raw_demos = rng.sample(raw_demos, sample_size)` (`bootstrap.py:269`) —
  so for a program with more than one predictor, the second (and later) predictor's raw/
  labeled demos are drawn from whatever the **previous** predictor's sample left behind, not
  independently from the full validation pool. `sample_size` is re-clamped to the
  already-shrunk `len(raw_demos)` each iteration, so it never errors — it just silently
  narrows. Never mentioned in any docstring or comment. Does not bite `pairs.py`'s
  single-`dspy.Predict` program. [trap] (verified: read) · skill: **new**
- **`self.student = self._train()`'s own error handling for a mismatched predictor**:
  `except KeyError: continue  # FIXME: !` (`bootstrap.py:229-231`) when a trace's predictor
  isn't found in `predictor2name` — silently drops that demo rather than raising. [trap]
  (verified: read) · skill: same as `optimizers.md`'s existing "sessions" coverage of this
  exact line for a different caller (`dspy-session`); confirmed present in the base class
  itself too
- `metric_threshold` vs bare truthiness (`success = metric_val >= self.metric_threshold` /
  `else: success = metric_val`, `bootstrap.py:206-212`) — already the skill's central trap
  for this optimizer, confirmed at the same lines · skill: same

**`BootstrapFewShotWithRandomSearch` (`BootstrapRS`)** (`dspy/teleprompt/random_search.py`,
168 lines):

- `dspy.BootstrapFewShotWithRandomSearch(metric, teacher_settings=None,
  max_bootstrapped_demos=4, max_labeled_demos=16, max_rounds=1, num_candidate_programs=16,
  num_threads=None, max_errors=None, stop_at_score=None, metric_threshold=None)`;
  `compile(student, *, teacher=None, trainset, valset=None, restrict=None,
  labeled_sample=True)`. [api] (verified: `inspect.signature`) · skill: same
- **Builds `num_candidate_programs + 3` candidates, not `num_candidate_programs`.**
  `for seed in range(-3, self.num_candidate_sets):` (`random_search.py:75`) with
  `num_candidate_sets = num_candidate_programs` — three pinned seeds (`-3` zero-shot, `-2`
  labels-only, `-1` unshuffled bootstrap) **plus** `num_candidate_programs` shuffled ones,
  never subtracted. Contrast directly with `MIPROv2`'s own helper,
  `create_n_fewshot_demo_sets`, which explicitly does `num_candidate_sets -= 3` so **its**
  total equals exactly the requested count (`dspy/teleprompt/utils.py:350`) — the two "3
  pinned + N shuffled" implementations in this slice disagree about what "N" means. [trap]
  (verified: read, both sites) · skill: **wrong**: `optimizers.md` says BootstrapRS repeats
  `BootstrapFewShot` "under different random demo subsets to build
  `num_candidate_programs` full candidate programs" — the true count is +3
- **Two official docs describe this the same imprecise way.**
  `docs/docs/diving-deeper/bootstrap-fewshot-family.md:94`: "Three of those seeds are pinned
  baselines" — phrased as if the three are drawn **from** `num_candidate_programs`, not
  additional to it. `docs/docs/learn/optimization/optimizers.md:103` is looser but closer:
  "The optimizer will repeat this 10 times (**plus some initial attempts**)" — acknowledging
  extras without naming the count. [trap] (verified: read, both docs) · skill: **new**
  (a docs-internal inconsistency, not something the skill claims)
- **`restrict` parameter** (not in the skill at all): a set/iterable of seed numbers to run —
  raises `ValueError` naming `restrict` if its intersection with `range(-3,
  num_candidate_sets)` is empty (`random_search.py:61-67`). Confirmed safe against a
  single-use iterator: DSPy's own regression test constructs `restrict=iter([-3])` and
  asserts it still works (`tests/teleprompt/test_random_search.py:61-76`) — the code converts
  it to a `set` once (`:62`) before either check consumes it. [api] (verified: read + DSPy's
  own passing test) · skill: **new**
- `self.valset = valset or trainset  # TODO: FIXME: Note this choice.` (`random_search.py:59`)
  — the maintainers' own inline doubt about the exact default `optimizers.md` already
  documents. [claim] (verified: read) · skill: same (adds the maintainers' own comment as
  evidence)
- **Two separately-seeded `random.Random(seed)` objects per candidate**, not one advancing
  generator: `random.Random(seed).shuffle(trainset_copy)` then a second
  `random.Random(seed).randint(...)` (`random_search.py:106-107`) — the `randint` draw is
  unaffected by how much state the shuffle consumed. [pattern] (verified: read) · skill: **new**
- **Selection**: `best_program` updates only on strict `score > max(scores)`, checked
  **before** `scores.append(score)` (`:136-140`) — the zero-shot seed `-3` (always first,
  `len(scores)==0`) is the guaranteed fallback winner if nothing later beats it. `stop_at_score`
  short-circuits the seed loop entirely once met (`:146-148`), reducing real cost below the
  nominal `num_candidate_programs+3` figure. [pattern] (verified: read) · skill: **new**
- **Logs via bare `print()`, not `logging`** — every status line in this file
  (`random_search.py:54-55, 137, 141-142, 147, 156`) is a `print`, unlike every sibling
  optimizer in this slice, which uses `logger.info`/`logger.debug`. [pattern] (verified: read)
  · skill: **new**
- **The official deep-dive doc's own field-shape claim is wrong.** "`best_program
  .candidate_programs` carrying the full ranked list of `(seed, program, score, subscores)`
  tuples" (`docs/docs/diving-deeper/bootstrap-fewshot-family.md:100`) — the code appends a
  **dict**, `{"score": score, "subscores": subscores, "seed": seed, "program": program}`
  (`random_search.py:144`), with a different key order than the doc's tuple order. Iterating
  it as a 4-tuple (`for seed, program, score, subscores in ...`) would not work. [trap]
  (verified: read) · skill: **new**

**`BootstrapFewShotWithOptuna`** (`dspy/teleprompt/teleprompt_optuna.py`, 89 lines) — absent
from `optimizers.md` entirely:

- `dspy.BootstrapFewShotWithOptuna(metric, teacher_settings=None, max_bootstrapped_demos=4,
  max_labeled_demos=16, max_rounds=1, num_candidate_programs=16, num_threads=None)`;
  `compile(student, *, teacher=None, max_demos, trainset, valset=None)` — `max_demos` is
  **required** (no default), despite sitting after `teacher=None` and being keyword-only.
  [api] (verified: `inspect.signature` on the installed package) · skill: **new**
- **Is exported as `dspy.BootstrapFewShotWithOptuna`** (confirmed: `hasattr(dspy,
  "BootstrapFewShotWithOptuna") == True`), and is in `dspy/teleprompt/__init__.py`'s
  `__all__` (`:14, 30`) — yet it appears in **neither** `optimizers.md` nor the official
  docs' own "What DSPy Optimizers are currently available?" numbered list
  (`docs/docs/learn/optimization/optimizers.md:36-78`), which claims "Optimizers can be
  accessed as `dspy.<OptimizerName>`" (line 38) as if that list were exhaustive. [trap]
  (verified: ran `hasattr` against the installed package) · skill: **new**
- **Mechanism is different in kind from `BootstrapFewShotWithRandomSearch`**: runs one
  ordinary `BootstrapFewShot(max_bootstrapped_demos=max_demos, ...).compile(...)` **once**
  to build a pool of bootstrapped traces per predictor (`teleprompt_optuna.py:74-83`), then
  each of `num_candidate_sets` Optuna trials picks **exactly one** already-bootstrapped demo
  per predictor via `trial.suggest_int(f"demo_index_for_{name}", 0, len(all_demos)-1)`
  (`:54`) — never a **set** of several, and no further teacher/LM calls happen inside the
  Optuna loop beyond ordinary `Evaluate()` scoring. Needs `optuna` (same
  `_import_optuna()` shape and error message as `MIPROv2`, duplicated verbatim in this file,
  `:7-17`). [number] (verified: read) · skill: **new**

**`KNNFewShot`** (`dspy/teleprompt/knn_fewshot.py`, 69 lines):

- `dspy.KNNFewShot(k, trainset, vectorizer, **few_shot_bootstrap_args)`;
  `compile(student, *, teacher=None)`. Confirmed matches `optimizers.md`'s claim exactly
  (line-for-line: `:52-69`) · skill: same
- **Every forward call bootstraps against the *original* `student` object, not the returned
  `student_copy`.** `forward_pass` closes over `student` (the argument to `compile`, not
  `student_copy`) and runs `BootstrapFewShot(**few_shot_bootstrap_args).compile(student,
  teacher=teacher, trainset=knn_trainset)` fresh, per call (`knn_fewshot.py:58-66`) —
  `student_copy.forward` is only where the closure is installed. Consequence: every single
  inference call also re-triggers the `reset_copy()`/`.lm=None` chain above internally. [trap]
  (verified: read; corroborated by DSPy's own `tests/propose/test_grounded_proposer.py`
  pattern of constructing with a bare `Predict`) · skill: **new** (refines an existing entry
  without contradicting it)
- `num_threads` in `few_shot_bootstrap_args`, `save()` writing `demos: []` — already in the
  skill at the cited lines, confirmed · skill: same

**`InferRules`** (`dspy/teleprompt/infer_rules.py`, 152 lines):

- `dspy.InferRules(num_candidates=10, num_rules=10, num_threads=None, teacher_settings=None,
  **kwargs)`; `compile(student, *, teacher=None, trainset, valset=None)` — a
  `BootstrapFewShot` subclass. [api] (verified: `inspect.signature`) · skill: same
- **`num_candidates <= 0` silently returns `None` from `compile()`.**
  `for candidate_idx in range(self.num_candidates):` never executes; `best_program` stays
  `None`; it is returned as-is (`infer_rules.py:34-59`) — and the code even **logs** `"Final
  best score: -inf"` first, since `best_score = -math.inf` is also never updated. [trap]
  (verified: ran `dspy.InferRules(num_candidates=0, ...).compile(...)` offline against the
  installed package — printed `Final best score: -inf` then returned `None`) · skill: **new**
- **Every candidate shares identical demos.** All `num_candidates` deep-copies come from
  `original_program = self.student.deepcopy()` — the single, already-bootstrapped result of
  `super().compile(...)` (`infer_rules.py:28-31`) — so `num_candidates` varies only which
  rules get appended to instructions, never the demo set. [pattern] (verified: read) ·
  skill: **new**
- **Rule induction sends the *whole* half-trainset as one blob, with a shrink-and-retry loop
  on context-window failure.** `induce_natural_language_rules` builds `examples_text` from
  every row of `demos` (`get_predictor_demos` returns the **entire** trainset, not a sample)
  and calls `self.rules_induction_program(examples_text)` once; on `ValueError`,
  `e.__class__.__name__ == "BadRequestError"`, or `"ContextWindowExceededError" in str(e)`, it
  drops the **last** example and retries in a `while True:` loop, down to 1 example, else
  raises `RuntimeError` (`infer_rules.py:61-80`). Any **other** exception type fails the
  internal `assert` itself rather than propagating the original error cleanly. [trap]
  (verified: read) · skill: **new**
- **The rule-writer is a separate module from whatever "teacher" ran bootstrapping**, despite
  the official doc calling it "the teacher LM": `RulesInductionProgram` is its own
  `dspy.Module` (`dspy.ChainOfThought(CustomRulesInduction)`) constructed once in
  `InferRules.__init__` and reused across every predictor/candidate/retry
  (`infer_rules.py:126-141`); it runs inside its **own** `dspy.context(**self.teacher_settings)`
  and a fresh `dspy.settings.lm.copy(rollout_id=self.rng.randint(0, 10**9), temperature=1.0)`
  (`:143-150`), where `self.rng = random.Random(0)` is created once and **advances** across
  the whole compile — not the same object as the bootstrapping-phase teacher.
  `docs/docs/diving-deeper/bootstrap-fewshot-family.md:128`: "asks **the teacher LM**..."
  [trap] (verified: read) · skill: **new**
- Halved valset without an explicit one — `train_size = int(0.5*len(trainset))`, unshuffled
  (`infer_rules.py:24-26`) — matches the skill's existing citation to the same lines exactly
  · skill: same

**`COPRO`** (`dspy/teleprompt/copro_optimizer.py`, 356 lines):

- `dspy.COPRO(prompt_model=None, metric=None, breadth=10, depth=3, init_temperature=1.4,
  track_stats=False, **_kwargs)`; `compile(student, *, trainset, eval_kwargs=None)`. [api]
  (verified: `inspect.signature`) · skill: same
- **LM/evaluate-call cost is `breadth × depth` for a single-predictor program, but grows
  *quadratically* in `depth` for a multi-predictor one.** For a program with exactly one
  predictor, each depth round scores only that round's newest `breadth` candidates
  (`candidates_ = latest_candidates[id(p_old)]`, `copro_optimizer.py:194`). For **more than
  one** predictor, the code instead re-scores the **entire accumulated** candidate pool every
  round (`if len(module.predictors()) > 1: candidates_ = all_candidates[id(p_old)]`,
  `:195-200`), and that pool grows by `breadth` every round
  (`all_candidates[id(p_base)].proposed_instruction.extend(...)`, `:323-326`) — giving
  `breadth·(1+2+...+depth) = breadth·depth·(depth+1)/2` `evaluate()` calls **per predictor**,
  not the linear `breadth·depth`. [number] (verified: read — derived from the loop structure)
  · skill: **new**
- **The official selection-guide doc's own cost formula matches only the single-predictor
  case.** `docs/docs/diving-deeper/choosing-an-optimizer.md:90`: "Total LM cost is roughly
  `breadth × depth × num_predictors`" — linear in every factor; the quadratic-in-depth
  multi-predictor cost above contradicts it. [trap] (verified: read) · skill: **new**
- **`depth=0` crashes with a bare `IndexError` at the very end of `compile()`.**
  `for d in range(self.depth):` never runs, so `evaluated_candidates[id(predictor)]` stays
  `{}` for every predictor (seeded that way at line 174, never filled); `candidates = []`
  after the final loop; `best_program = candidates[0]["program"]` (`:349`) then raises
  `IndexError: list index out of range`. [trap] (verified: ran `COPRO(depth=0, breadth=2)
  .compile(...)` offline through this repo's own `scripts/lm_fixture.FixtureLM` — raised
  exactly `IndexError: list index out of range`) · skill: **new**
- **No `seed` parameter anywhere** — reproducibility depends entirely on the LM/provider's
  own sampling at `temperature=init_temperature` (default 1.4); every other search-based
  optimizer in this slice at least seeds its own internal randomness. [trap] (verified: read)
  · skill: **new**
- `total_calls` on the returned program is a **live** counter (incremented once per
  `evaluate()` call, `:230`), unlike `MIPROv2`'s dead `total_calls`/`prompt_model_total_calls`
  — but it counts *evaluation rounds*, not raw LM calls (each `evaluate()` call itself costs
  `len(trainset)` predictor invocations). [number] (verified: read) · skill: **new**
- Tie handling: `evaluated_candidates[id(p_old)][(instruction, prefix)]` is only overwritten
  when the new score is strictly higher (`if ... ["score"] >= score: replace_entry = False`,
  `:234-236`) — first-seen entry wins ties. `_drop_duplicates` only merges duplicates within
  **contiguous** equal-score runs of the globally sorted list (`:90-108`), so two identical
  (instruction, prefix) pairs separated by a differently-scored one in between are not
  deduplicated. [pattern] (verified: read) · skill: **new**
- **Sequential coordinate-ascent within one depth**: after scoring predictor `p_i`'s
  candidates, `module_clone`'s `p_i` signature is immediately set to `p_i`'s best-of-round
  result **before** predictor `p_i+1` is evaluated in the same depth iteration (`:258-267`,
  runs inside the `for p_i, (p_old, p_new) in enumerate(...)` loop) — so later predictors are
  scored against earlier predictors' already-improved instructions, not the original ones.
  [pattern] (verified: read) · skill: **new**
- `breadth<=1` raising `ValueError` at construction, `**_kwargs` silently swallowing a typo'd
  keyword — confirmed at the same lines the skill already cites · skill: same

**`SignatureOptimizer`** (`dspy/teleprompt/signature_opt.py`, 52 lines) — a deprecated
`COPRO` alias, not mentioned anywhere in `optimizers.md`:

- **Cannot be constructed at all on 3.3.1.** `SignatureOptimizer.__init__` calls
  `super().__init__(prompt_model, metric, breadth, depth, init_temperature, verbose,
  track_stats)` **positionally** — 7 values — but `COPRO.__init__`'s positional-or-keyword
  slots are only `(prompt_model, metric, breadth, depth, init_temperature, track_stats)`, 6,
  plus `**_kwargs` (which does not accept extra **positional** arguments). Every
  construction raises `TypeError: COPRO.__init__() takes from 1 to 7 positional arguments
  but 8 were given`, **after** printing its own deprecation warning ("SignatureOptimizer has
  been deprecated and replaced with COPRO... will be removed in a future release") — so the
  warning misleadingly implies a working, if discouraged, path. [trap] (verified: ran
  `from dspy.teleprompt.signature_opt import SignatureOptimizer; SignatureOptimizer(metric=...)`
  offline against the installed package — raised exactly that `TypeError`) · skill: **new**
- **Is not exported as `dspy.SignatureOptimizer`** — `hasattr(dspy, "SignatureOptimizer")
  == False`, and `dspy/teleprompt/__init__.py` never imports it; only reachable via
  `from dspy.teleprompt.signature_opt import SignatureOptimizer`. [api] (verified: ran
  `hasattr`) · skill: **new**
- **DSPy's own shipped test suite provides zero coverage that would catch this.**
  `tests/teleprompt/test_copro_optimizer.py`'s tests are named `test_signature_optimizer_*`
  but import `COPRO` — via `from dspy.teleprompt.signature_opt import COPRO`, a re-export
  inside that same module (`signature_opt.py:1`, `from .copro_optimizer import COPRO`) — and
  never touch the actual `SignatureOptimizer` class. [trap] (verified: read
  `tests/teleprompt/test_copro_optimizer.py:1-27`) · skill: **new**

**`MIPROv2`** (`dspy/teleprompt/mipro_optimizer_v2.py`, 866 lines):

- Full surface confirmed against the installed package (see §5); every parameter and default
  `optimizers.md` already states is confirmed unchanged (`auto="light"`, `seed=9`,
  `max_bootstrapped_demos=4`, `max_labeled_demos=4`, `minibatch_size=35`,
  `minibatch_full_eval_steps=5`, the `AUTO_RUN_SETTINGS` table, the `valset_size`/`num_trials`
  formulas) · skill: same
- **`num_candidates` sets both fewshot and instruct candidate counts identically** at
  construction (`self.num_fewshot_candidates = self.num_instruct_candidates =
  self.num_candidates = num_candidates`, `mipro_optimizer_v2.py:85-87`) — **overridden** under
  `auto=...`, where `num_instruct_candidates = auto_settings["n"] if zeroshot else
  int(auto_settings["n"] * 0.5)` while `num_fewshot_candidates = auto_settings["n"]` in full
  (`:309-313`) — i.e. when few-shot demos are allowed, the instruction-candidate budget is
  **halved** relative to the demo-candidate budget. The code's own comment: "generally
  better to spend optimization budget on few-shot examples when they are allowed." [number]
  (verified: read) · skill: **new**
- **Under `auto=...`, `minibatch` is force-overridden to `len(valset) > MIN_MINIBATCH_SIZE`
  (50)** (`:307`), **replacing whatever `minibatch=` the caller passed to `compile()`** — this
  only happens when `self.auto` is set; with `auto=None` the caller's own `minibatch`
  argument passes through untouched (`_set_hyperparams_from_run_mode`, `:299-317`). [number]
  (verified: read) · skill: **new** (refines `optimizers.md`'s existing "minibatching turns
  on only when `len(valset) > 50`" by naming the exact override condition)
- **Full-eval cadence is off by one from what the parameter name and the official doc both
  suggest.** The periodic full evaluation fires when `trial_num % (minibatch_full_eval_steps
  + 1) == 0` (`mipro_optimizer_v2.py:637`) — with the **default** `minibatch_full_eval_steps
  =5`, that is every **6th** trial, not every 5th. `docs/docs/api/optimizers/MIPROv2.md:65`:
  "The best averaging set of prompts is then evaluated on the full validation set every
  `minibatch_full_eval_steps`." [trap] (verified: read; exact modulo confirmed via
  `grep -n "trial_num % " dspy/teleprompt/mipro_optimizer_v2.py` → line 637) · skill: **new**
- **`_estimate_lm_calls` is dead code** — defined (`:353-399`) with a full breakdown of
  expected prompt-model and task-model calls, formatted for pretty console output, but
  **never called anywhere** in the package (confirmed via `grep -rn "_estimate_lm_calls"` over
  all of `dspy/` and `tests/` — only its own definition matches). Nothing in a real run ever
  prints or warns about the estimate this method exists to produce. Its own formula for
  prompt-model cost ("10 data summarizer calls + `num_instruct_candidates·num_predictors`
  + program-aware extra") also **disagrees in shape** with the real cost once you read
  `GroundedProposer`/`create_dataset_summary` (below: up to 12 summarizer calls, not 10; up to
  3 LM calls per instruction candidate under `program_aware`, not 1). [trap] (verified: read
  + grep confirming zero call sites) · skill: **new**
- `default_score` (logged as "Trial 1") evaluates the **unmodified input program** in full
  (`len(valset)` calls) before any search trial runs, and is registered into Optuna's own
  trial history via `optuna.trial.create_trial(...)` as a baseline point at the default
  parameter indices (instruction 0, demo-set 0 for every predictor) — `mipro_optimizer_v2.py:
  538-551, 661-671`. [pattern] (verified: read) · skill: **new**
- `instruction_candidates[i][0]` is **unconditionally overwritten** to the predictor's
  **original**, pre-optimization instruction text right after generation
  (`instruction_candidates[i][0] = get_signature(pred).instructions`, `:500`) — guaranteeing
  "keep the instruction as-is" is always one of the choices Optuna can select. [pattern]
  (verified: read) · skill: **new**
- **`eval_candidate_program` (shared with `BetterTogether`) swallows any evaluation
  exception**: `except Exception: logger.error(..., exc_info=True); return dspy.Prediction
  (score=0.0, results=[])` (`dspy/teleprompt/utils.py:59-62`), with the maintainers' own
  `# TODO: Handle this better, as -ve scores are possible` left in place. [trap] (verified:
  read) · skill: **new**
- `save_candidate_program` writes one `.json` file per trial to `<log_dir>/
  evaluated_programs/program_<trial_num>[_<note>].json` whenever `log_dir` is set
  (`dspy/teleprompt/utils.py:210-229`) — a real, unbounded-by-default disk cost over a long
  run (nothing caps how many trials write a file). [pat] (verified: read) · skill: **new**
- `get_program_with_highest_avg_score` raises `ValueError: No valid program found in
  param_score_dict` if every scored parameter combination has already been fully evaluated
  (`dspy/teleprompt/utils.py:116-140`). [trap] (verified: read) · skill: **new**
- `create_minibatch(trainset, batch_size=50, rng=None)` falls back to the **global, unseeded**
  `random` module when `rng` is `None` (`dspy/teleprompt/utils.py:27-42`) — `MIPROv2` itself
  always passes `self.rng`, so this does not bite `MIPROv2` specifically, but the helper is
  shared and any other caller passing no `rng` gets non-reproducible sampling. [trap]
  (verified: read) · skill: **new**
- `requires_permission_to_run` fully removed, ties keep the untouched program, dead
  `total_calls`/`prompt_model_total_calls` counters — all confirmed at the exact lines the
  skill already cites · skill: same
- **The official docs' own threshold guidance for choosing `MIPROv2` is absent from the
  skill's comparison table**, which cites only third-party repos: "If you have **very few
  examples** (around 10), start with `BootstrapFewShot`... If you're willing to use more
  inference calls to perform **longer optimization runs** (e.g. 40 trials or more), and have
  enough data (e.g. **200 examples or more** to prevent overfitting) then try `MIPROv2`"
  (`docs/docs/learn/optimization/optimizers.md:87-91`); a separate page adds "aim for at
  least **300 examples**" and states the 20/80 train/val split as general prompt-optimizer
  guidance, with GEPA named as the one exception
  (`docs/docs/learn/optimization/overview.md:8`). [claim] (verified: read, both pages) ·
  skill: **new**

**`SIMBA`** (`dspy/teleprompt/simba.py` 377 lines + `dspy/teleprompt/simba_utils.py` 253
lines):

- Full constructor/compile surface confirmed unchanged, including the keyword-only `metric`
  (`SIMBA(self, *, metric: ..., bsize: int = 32, ...)`, confirmed via `inspect.signature` on
  the installed package) and `assert len(trainset) >= self.bsize` at `simba.py:105` — both
  already correctly stated by the skill · skill: same
- **LM-call cost, derived exactly from the loop** (`simba.py:172-349`): per step, trajectory
  sampling costs `num_candidates * bsize` calls (`models × batch`, `:195-211`); candidate
  re-evaluation costs up to `(num_candidates+1) * bsize` more (`len(system_candidates) <=
  num_candidates+1`, capped by the `break` at `:300-301`, `:306-308`); **on top of both**, one
  extra reflective call per bucket where the randomly-chosen strategy is `append_a_rule`
  (never `append_a_demo`, which makes zero extra calls — pure bookkeeping over an
  already-computed trace, `simba_utils.py:73-105`). After all `max_steps` steps, a **final
  validation phase** evaluates up to `num_candidates+1` (deduplicated) programs on the
  **full** `trainset` — `(num_candidates+1) * len(trainset)` more calls (`simba.py:337-349`).
  For `pairs.py`'s own config (`bsize=min(train_size,16), num_candidates=4, max_steps=4`):
  up to `4·(16+16)+4·5 ≈ 148` per step (plus up to 4 reflective calls/step) over 4 steps, then
  up to `5 * len(trainset)` more at the end. [number] (verified: read — this is a derivation,
  not a measurement, and I say so) · skill: **new**
- **The rollout-sampling LMs are always constructed at `temperature=1.0`, hardcoded —
  `temperature_for_sampling`/`temperature_for_candidates` never touch the LM's temperature
  at all.** `prepare_models_for_resampling` builds `n` model copies via `lm.copy(
  rollout_id=r, temperature=1.0)` (`simba_utils.py:30`) — the optional `teacher_settings`
  LM is the one exception, kept at its own settings. `SIMBA`'s own `temperature_for_sampling`
  (default 0.2) and `temperature_for_candidates` (default 0.2) instead control only the
  **softmax program-selection** formula (`softmax_sample`, `simba.py:131-145, 197, 253-255`)
  — a naming collision between "temperature" as an LM sampling parameter and "temperature" as
  a softmax-selection parameter. [trap] (verified: read) · skill: **new**
- **`append_a_rule` sends the program's own source code and the training example's *gold
  label* to the reflection model.** Its `kwargs` include `"program_code":
  inspect.getsource(system.__class__)`, `"program_inputs": {**example.inputs()}`, and
  `"oracle_metadata": {**example.labels()}` (`simba_utils.py:143-157`), all JSON-serialized
  and sent to `prompt_model` (defaults to `dspy.settings.lm`, since `pairs.py`'s `SIMBA(...)`
  call never sets `prompt_model=`). For a **bare `dspy.Predict(Signature)` program**
  (`pairs.py`'s own shape), `system.__class__` is `dspy.Predict` itself, so `program_code`
  captures DSPy's own `Predict` class source, not any project code — but the trainset row's
  German judgement (`example.inputs()`/`example.labels()`) still goes out. [trap] (verified:
  read) · skill: **new**
- **Appended advice is never pruned; demos are, but only probabilistically.** A successful
  `append_a_rule` does `instructions = predictor.signature.instructions + "\n\n" +
  advice[name]` (`simba_utils.py:169-170`) — pure accretion, no cap, across every generation
  of `max_steps`. Demos, by contrast, get a **soft**, Poisson-distributed drop before each new
  candidate is built: `num_demos_to_drop = max(rng_np.poisson(num_demos / max_demos_tmp),
  int(num_demos >= max_demos_tmp))` (`simba.py:269`) — this is a statistical target around
  `max_demos`, **not a hard per-step cap**; a predictor can end up holding more than
  `max_demos` demos after a few generations. Neither is documented as such anywhere. [trap]
  (verified: read) · skill: **new**
- **A module name missing from — or not recognised in — the model's `advice` dict fails
  completely silently**, in both directions: `if name in advice:` only logs "Advice for
  {name}: ..." for the modules that got one (`simba_utils.py:166-168`); a module left out, or
  an extra key the model invented that matches no real predictor name, produces no log line
  at all. [trap] (verified: read) · skill: **new**
- **`wrap_program` can never raise** — a crashing program call is caught (`logger.warning`,
  `simba_utils.py:38-41`) leaving `prediction=None`; the metric is still called on that
  `None`; if the metric **also** raises (likely, given `prediction=None`), that is caught too
  (`:60-61`), yielding `score=0.0, output_metadata={}` with no error surfaced beyond two
  warning logs. [trap] (verified: read) · skill: **new** (extends the skill's existing
  "SIMBA's own metric wrapper" trap with the double-failure case)
- **Even SIMBA's own explicit metric-contract error is swallowed.** `wrap_program` raises
  `ValueError("When metric returns a dspy.Prediction, it must contain a score field.")`
  (`simba_utils.py:54`) if the returned `Prediction` has no `.score` — but that `raise`
  happens **inside** the same `try` block that catches it two lines later (`:60-61`), so this
  explicit, deliberately-worded validation error is caught and turned into a silent `score=
  0.0` exactly like any other exception. [trap] (verified: read) · skill: **new**
- Two independently-seeded RNGs per compile from the same `seed` value:
  `rng = random.Random(seed)` for shuffling/choice, `rng_np = np.random.default_rng(seed)`
  for the Poisson draws (`simba.py:108-109`) — both deterministic given the seed, but
  advancing independently. [pattern] (verified: read) · skill: **new**
- **Final candidate downsampling**: evenly-spaced indices over `winning_programs`
  (`round(i*M/(N-1))` for `i in range(N)`, `M = len(winning_programs)-1`, `N =
  num_candidates+1`), then deduplicated via `dict.fromkeys` (`simba.py:337-346`) — see
  §3 for the snippet. [pattern] (verified: read) · skill: **new**
- The official doc's "identifies challenging examples with high output variability... uses
  the LLM to introspectively analyze failures and generate self-reflective improvement rules
  or add successful demonstrations" (`docs/docs/diving-deeper/choosing-an-optimizer.md:101`)
  glosses over the actual mechanism: `append_a_demo` uses the single **best** trajectory in a
  bucket (`good = bucket[0]`, `simba_utils.py:78`), not something that "addresses" the worst
  one; the bucket-selection itself (`simba.py:213-236`) sorts by `(max_to_min_gap, max_score,
  max_to_avg_gap)`, not by "worst-scoring examples" per se. [claim] (verified: read) ·
  skill: **new**, minor

**`BetterTogether`** (`dspy/teleprompt/bettertogether.py`, 631 lines):

- Full `compile()` signature is missing one parameter from the skill's own "full signature"
  line: `optimizers.md` lists `compile(student, *, trainset, teacher=None, valset=None,
  num_threads=None, max_errors=None, seed=None, valset_ratio=0.1,
  shuffle_trainset_between_steps=True, strategy="p -> w -> p", optimizer_compile_args=None)`
  — the installed package's real signature also has `provide_traceback: bool | None = None`
  between `max_errors` and `seed` (`bettertogether.py:193-209`, confirmed via
  `inspect.signature`). [api] (verified: `inspect.signature` on the installed package) ·
  skill: **wrong**: `optimizers.md`'s compile signature line omits `provide_traceback`
- **`optimizer_compile_args` is an entire mechanism, absent from the skill.** Per-step
  `compile()` kwargs, validated against `inspect.signature(optimizer.compile).parameters`
  (`_validate_compile_args`, `bettertogether.py:392-407`); a `"student"` key raises
  `ValueError`; a `GEPA` sub-optimizer additionally may not be given a `teacher=` (since
  `GEPA.compile` itself rejects one) — checked eagerly by class name
  (`optimizer.__class__.__name__ == "GEPA"`, `:383-388`), not `isinstance`. [api] (verified:
  read) · skill: **new**
- **LM lifecycle management, precisely**: `launch_lms(student)` runs once, before the
  baseline evaluation, at the very start (`_run_strategies`, `:432-433`); `kill_lms(student)`
  runs once, at the very end (`:482-483`), including on an early `break` from a failed step
  (control falls through to the cleanup code regardless). Mid-sequence, after any step,
  `_models_changed` (compares `pred.lm.model` **names** before/after, `:586-591`) triggers a
  fresh `launch_lms(student)` **only for the new LM objects** a step like `BootstrapFinetune`
  installed — the **old**, now-orphaned LM(s) from that step are never explicitly
  `kill_lms`'d mid-run, only whatever LMs the **final** student ends up holding get killed at
  the end. [pattern] (verified: read) · skill: **new**
- **The maintainers' own comment names the concrete, cross-optimizer defect this file exists
  to paper over**: "Some optimizers like `BootstrapFewShotWithRandomSearch` reset predictor
  LMs during compilation, which breaks weight optimizers as they require each predictor to
  have an LM. We should ensure that all optimizers respect the assigned LMs of programs and
  do not override them. Until then, we restore the original LMs here." (`bettertogether.py:
  552-556`) — the mechanism is exactly the `reset_copy()` chain documented above (specifically
  `random_search.py`'s `seed=-3` branch, and by extension anything that routes through
  `BootstrapFewShot`). `BetterTogether` detects it via `if not all_predictors_have_lms
  (student): ...; for pred, lm in zip(student.predictors(), pred_lms_before, strict=False):
  pred.lm = lm` (`:557-563`) — snapshotting every predictor's `.lm` **before** each step and
  restoring it if the step's own output failed to keep one. [trap] (verified: read) ·
  skill: **new**
- **`compile(seed=None)` — not reproducible by default.** `rng = random.Random(seed)`
  (`:423`); with `seed=None` (the default), `random.Random(None)` seeds from OS entropy, so
  the trainset shuffling and evaluation sampling differ run to run — unlike every sibling
  optimizer in this slice that defaults its own seed (`MIPROv2(seed=9)`, `SIMBA.compile(
  seed=0)`, `GRPO(seed=0)`). [trap] (verified: read) · skill: **new**
- `is_new_best = score is not None and score >= best_score_so_far` (`:582`) uses `>=`, not
  strict `>` — a tie is logged as "New best score!" — contrast `MIPROv2`'s strict `>` for the
  same kind of comparison. [pattern] (verified: read) · skill: **new**
- Every `_evaluate_on_valset` call is a **full** pass (`batch_size = len(valset)` via
  `eval_candidate_program(len(valset), valset, program, evaluate, rng)`, `:630`) — no
  minibatching anywhere in `BetterTogether`, unlike `MIPROv2`. [pattern] (verified: read) ·
  skill: **new**
- `all_predictors_have_lms(student)` called for its side effect and discarded in
  `_prepare_student_and_teacher` (`:311`) — see the cross-cutting item above; the **same**
  helper is used correctly, in a real `if not ...:` guard, later in this same file (`:557`).
  · skill: **new** (cross-referenced, not duplicated as a separate item)
- Ties in the final sort keep the **earlier** program: `sort(key=lambda x: (x[1]["score"] if
  ... else float("-inf"), -x[0]), reverse=True)` (`:486-490`) — worked through: among equal
  scores, the smaller original index sorts first. Confirmed exactly matches
  `optimizers.md`'s existing claim · skill: same
- `"Fine-Tuning and Prompt Optimization: Two Great Steps that Work Better Together"`
  (arXiv:2407.10930, Soylu/Potts/Khattab) and the Databricks case study numbers — SFT alone
  +1.9, GEPA alone +2.1, GEPA+SFT (`BetterTogether`) +4.8, on "IE Bench" (100+ page documents,
  70+ extraction fields) with GPT-4.1 (`docs/docs/api/optimizers/BetterTogether.md:126-132`).
  [claim][number] (verified: read) · skill: **new**
- "Currently supported [fine-tunable providers]: `LocalProvider`, `DatabricksProvider`, and
  `OpenAIProvider`. You can extend the `Provider` class for custom use cases."
  (`docs/docs/api/optimizers/BetterTogether.md:124`) [claim] (verified: read; partially
  corroborated — `dspy/clients/lm_local.py:25` sets `self.finetunable = True`, confirmed by
  grep, though `dspy/clients/*.py` is outside this slice) · skill: **new**

**`BootstrapFinetune`** (`dspy/teleprompt/bootstrap_finetune.py`, 324 lines):

- `dspy.BootstrapFinetune(metric=None, multitask=True, train_kwargs=None, adapter=None,
  exclude_demos=False, num_threads=None)`; `compile(student, trainset, teacher=None)` —
  `trainset` is **positional**, not keyword-only, unlike almost every other optimizer's
  `compile` in this slice. [api] (verified: `inspect.signature`) · skill: same for the
  parameters; the positional-`trainset` fact is new
- **Requires every predictor's `.lm` to already be set explicitly, or raises with a named
  remedy.** `if pred.lm is None: raise ValueError(f"Predictor {pred_ind} does not have an LM
  assigned. Please ensure the module's predictors have their LM set before fine-tuning. You
  can set it using: your_module.set_lm(your_lm)")` (`bootstrap_finetune.py:82-87`). Confirmed
  by DSPy's own passing test, `tests/teleprompt/test_bootstrap_finetune.py:80-97`, which
  checks the message contains both `"does not have an LM assigned"` and `"set_lm"`. [trap]
  (verified: read + DSPy's own test) · skill: same as `optimizers.md`'s "needs a fine-tunable
  model" note, now with the exact message and the enforcement mechanism
- **The `_prepare_finetune_data` truthiness trap is a *new*, undocumented instance of the
  family `optimizers.md` already names — and this optimizer is absent from that list.**
  `trace_data = [d for d in trace_data if d["score"]]` (`bootstrap_finetune.py:172`) filters
  on raw truthiness; `d["score"]` is the metric's **raw return value**, set by
  `bootstrap_trace_data`'s `wrapped_metric`: `return metric(example, prediction, trace) if
  metric else True` (`bootstrap_trace.py:57-59`) — never coerced. A metric returning
  `dspy.Prediction(score=0.0, feedback=...)` is truthy and is **never filtered out**.
  `optimizers.md`'s "Affected the same way" list for this exact bug names
  `BootstrapFewShotWithRandomSearch`, `KNNFewShot`'s bootstrap step, `InferRules`, `MIPROv2`'s
  demo-bootstrapping, and `BetterTogether`'s default `p=` stage — **not**
  `BootstrapFinetune`. [trap] (verified: read, both files) · skill: **wrong**: the "Affected
  the same way" list in `optimizers.md` is incomplete
- **With the default `metric=None`, no filtering happens at all** — every bootstrapped trace,
  right or wrong, becomes fine-tuning data (the `if self.metric:` guard at
  `bootstrap_finetune.py:170` skips the filter entirely). DSPy's own official fine-tuning
  tutorial runs it exactly this way: `optimizer = dspy.BootstrapFinetune(num_threads=16)  #
  if you *do* have labels, pass metric=your_metric here!`
  (`docs/docs/tutorials/classification_finetuning/index.ipynb`, cell containing that exact
  comment). [trap] (verified: read source + grepped the tutorial notebook) · skill: **new**
- `exclude_demos` **defaults to `False`** here (contrast `GRPO`, where the same-named
  parameter must be `True` or construction fails, below) — so by default, whatever demos the
  student already had are **kept** on top of the newly fine-tuned weights:
  `pred.demos = [] if self.exclude_demos else pred.demos` (`:130`), and
  `build_call_data_from_trace` includes demos in the fine-tune data the same way unless
  excluded (`:208`). [pattern] (verified: read) · skill: **new**
- **Mutates the passed-in `student` object directly and returns the same object** — no
  `deepcopy()`/`reset_copy()` anywhere in `compile()`: `pred.lm = finetuned_lm` is set
  directly on `student.predictors()` (`:126`), then `student._compiled = True; return
  student` (`:133-134`). See the cross-cutting item above for how this falsifies the official
  docs' "original untouched" claim. [trap] (verified: read) · skill: **new**
- `key_to_data`/thread-count check: `if len(key_to_data) > num_threads: raise ValueError(...)`
  with a detailed explanation of how the job count depends on `multitask` (`:106-115`) —
  `num_threads` defaults to `dspy.settings.num_threads` = 8 when `self.num_threads` is `None`
  (`:74`, confirmed default via `dspy/dsp/utils/settings.py:31`). [number] (verified: read) ·
  skill: **new**
- `finetune_lms` calls `lm.kill()` on the LM about to be superseded **before** calling
  `lm.finetune(**kwargs)`, "to free up resources... This won't have any effect if the LM is
  not running" (`:150-155`), then joins each job's thread (`:163`). [pattern] (verified:
  read) · skill: **new**
- `random.Random(0).shuffle(data)` (`:191`) — deterministic, hardcoded, not exposed as a
  parameter, for the finetune-data ordering. [pattern] (verified: read) · skill: **new**
- Required `train_kwargs` keys for `LocalProvider`, per the official tutorial: `device,
  use_peft, num_train_epochs, per_device_train_batch_size, gradient_accumulation_steps,
  learning_rate, max_seq_length, packing, bf16, output_dir`
  (`docs/docs/tutorials/classification_finetuning/index.ipynb`, cell with that exact list).
  [claim] (verified: read — grepped the notebook) · skill: **new**
- The `prepare_teacher`/`assert_structural_equivalency`/`assert_no_shared_predictor` helper
  chain (`:270-307`) — reused by `BetterTogether` via `prepare_student`/`prepare_teacher`
  imports, and structurally re-implemented (not reused) by `GRPO`'s own inline checks. [api]
  (verified: read) · skill: **new**

**`GRPO`** (`dspy/teleprompt/grpo.py`, 635 lines) — **not present anywhere in the skill**:

- **Not exported as `dspy.GRPO`** — `hasattr(dspy, "GRPO") == False`, confirmed against the
  installed package; only reachable via `from dspy.teleprompt.grpo import GRPO`. Absent from
  `dspy/teleprompt/__init__.py`'s imports and `__all__` entirely — the only class in
  `dspy/teleprompt/` this slice covers that is neither exported nor deprecated-and-aliased.
  Also absent from the official docs' own "What DSPy Optimizers are currently available?"
  numbered list. [trap] (verified: ran `hasattr(dspy, "GRPO")` against the installed
  package) · skill: **new**
- **Default construction crashes.** `GRPO.__init__(self, metric=None, multitask=True,
  train_kwargs=None, adapter=None, exclude_demos: bool = False, ...)` — `exclude_demos`
  **defaults to `False`**, but the very next lines assert `assert exclude_demos,
  "exclude_demos==False is not supported yet. Please set it to True."` (`grpo.py:33, 68`).
  `GRPO(metric=lambda *a, **k: 1.0)` — the natural, minimal call — always raises
  `AssertionError`. `multitask` is asserted `True` too (`:69`), but that one's default (`True`)
  already satisfies it. [trap] (verified: ran `GRPO(metric=lambda *a, **k: 1.0)` offline —
  raised exactly `AssertionError: exclude_demos==False is not supported yet. Please set it to
  True.`) · skill: **new**
- **The default adapter fallback fails GRPO's own very next assertion.** At training-data
  build time: `adapter = self.adapter[pred_lm] or settings.adapter or XMLAdapter()`
  (`grpo.py:467`) — immediately followed by `assert isinstance(adapter, ChatAdapter), f"...
  GRPO training is not supported for this adapter."` (`:468`). Unless a `ChatAdapter` was
  explicitly configured (via `GRPO(adapter=...)` or `dspy.settings.configure(adapter=
  ChatAdapter())`), the fallback (`XMLAdapter()`) is *always* incompatible with the assertion
  immediately after it — the default path cannot succeed. [trap] (verified: read) ·
  skill: **new**
- **Requires an external RL-capable provider; none ships in `dspy/clients/`.**
  `compile()` calls `pred.lm.reinforce(train_kwargs)` per unique `(LM, data_key)`
  (`grpo.py:339`); `LM.reinforce` checks `if not self.provider.reinforceable: raise
  LMUnsupportedFeatureError(...)` (outside this slice, `dspy/clients/lm.py:366-379`, read for
  context). The base `Provider.reinforceable` defaults to `False`
  (`dspy/clients/provider.py:215`, grepped for context); none of the shipped providers
  (`openai.py`, `databricks.py`, `lm_local.py`) sets it `True` — `lm_local.py` sets only
  `finetunable = True`. `"arbor"` appears nowhere in `dspy/`'s own code. [trap] (verified:
  grepped `dspy/clients/` for `reinforceable`/`finetunable`/`arbor`; zero matches for
  `reinforceable=True` or `arbor` anywhere in the package) · skill: **new**
- **Confirmed, decisively, by DSPy's own RL tutorials — and they don't call `dspy.GRPO`
  either.** `docs/docs/tutorials/rl_multihop/index.ipynb` and `rl_papillon/index.ipynb` both
  install a **separate PyPI package**, `pip install -U arbor-ai`, then
  `import arbor; from arbor import ArborGRPO, ArborProvider; arbor.init()`, and construct the
  student's LM with `provider=ArborProvider()`. The optimizer actually invoked is
  `compiler = ArborGRPO(metric=..., multitask=True, num_dspy_examples_per_grpo_step=4, ...)`
  — parameter names mirror `dspy.teleprompt.grpo.GRPO`'s own — **not**
  `dspy.teleprompt.grpo.GRPO` directly, even though the surrounding markdown heading says
  "Optimize... with `dspy.GRPO`". [claim] (verified: grepped both notebooks for
  `GRPO|Arbor|arbor`, read the surrounding cells) · skill: **new**
- **Real GPU training infrastructure, per the tutorial's own numbers**: "We ran this on
  4xH100 GPUs for a couple of hours." `train_kwargs` in the worked example includes a LoRA
  config (`r=8, lora_alpha=16, target_modules=[q_proj,k_proj,v_proj,o_proj,up_proj,down_proj,
  gate_proj]`), `num_training_gpus: 3, num_inference_gpus: 1`,
  `per_device_train_batch_size: 8`, `gradient_accumulation_steps: 4`, `bf16: True`,
  `report_to: "wandb"` (`docs/docs/tutorials/rl_papillon/index.ipynb`, the cell building
  `train_kwargs` before `ArborGRPO(...)`). [claim][number] (verified: read the notebook cell)
  · skill: **new**
- **`all_predictors_have_lms(student)` is called and its result discarded here too**
  (`grpo.py:293`), and unlike `BootstrapFinetune`, **there is no later per-predictor
  substitute check** — `assert len(student_lms) == 1` on `{id(pred.lm) for pred in
  student.predictors()}` (`:281-286`) would pass an all-`None` program (`{id(None)}` also
  has length 1), only to crash less clearly later. [trap] (verified: read) · skill: **new**
- **LM cache is disabled structurally, for the whole training run, and restored after** —
  `disable_lm_cache`/`recover_lm_cache` (`:615-635`) run over every predictor of the student
  **and every teacher** before/after the training loop, not merely a project convention. [api]
  (verified: read) · skill: **new**
- **Mutates the student's LM objects in place; never constructs a new LM or copies the
  student.** Per the code's own comment: "The job here has a reference to a particular LM
  that's attached to the student program. We update the `.model` field of this LM inside the
  job, which also updates the LM in the student program since these point to the same
  reference... TODO(GRPO Team): This is inconsistent with how `BootstrapFinetune` works,
  which creates new LM instances post training." (`:523-536`). `return student` at the end is
  the same object passed in. [trap] (verified: read) · skill: **new**
- `FailedPrediction`s (malformed/off-format completions) are **included** in training data
  with a penalty reward (`score = trace_instance[2].format_reward or
  self.format_failure_score`, `:478-488`), not dropped. `variably_invoked_predictor_grouping_
  mode` ("truncate"/"fill"/"ragged") governs how a predictor invoked a variable number of
  times per rollout (e.g. inside a loop) gets equalised into training groups (`:439-452`).
  [api] (verified: read) · skill: **new**
- Teacher handling: `teacher=None` defaults to `[student]`; `assert student in teachers`;
  `assert num_rollouts_per_grpo_step % len(teachers) == 0` (`:298-312`). Polls
  `while not _any_available_for_step(): time.sleep(1)` with **no timeout** (`:369-370`). [api]
  (verified: read) · skill: **new**

**`Ensemble`** (`dspy/teleprompt/ensemble.py`, 40 lines):

- `dspy.Ensemble(*, reduce_fn=None, size=None, deterministic=False)`; `compile(programs)` —
  not `(student, trainset)`. Confirmed exactly matches `optimizers.md`'s existing coverage,
  including `assert deterministic is False` and the unseeded global `random.sample` for
  `size` · skill: same
- **The official selection-guide doc directly contradicts the shipped source.**
  `docs/docs/diving-deeper/choosing-an-optimizer.md:117`: "`.compile(programs)` returns a
  module that runs each input through every program **in parallel**..." The actual `forward`
  is a plain, sequential list comprehension: `outputs = [prog(*args, **kwargs) for prog in
  programs]` (`dspy/teleprompt/ensemble.py:33`) — matching the skill's own already-measured
  2.68× (not ≈1×) latency figure for `Ensemble`, which is exactly what sequential-not-
  parallel execution would produce. [trap] (verified: read the source; the skill's own cited
  measurement is consistent with sequential execution) · skill: **new**

**`AvatarOptimizer`** (`dspy/teleprompt/avatar_optimizer.py`, 217 lines):

- Cannot be constructed (`dspy.TypedPredictor` doesn't exist in 3.3.1) — confirmed at the
  exact line `optimizers.md` already cites (`avatar_optimizer.py:90`) · skill: same
- **The official selection guide describes it as fully working and recommends it, with zero
  caveat.** `docs/docs/diving-deeper/choosing-an-optimizer.md:121-122`: "Built for
  agent-style programs. Partitions the trainset by metric into positive... and negative
  examples. On each iteration, asks an LM to read positive and negative examples and propose
  instruction edits..." — and the page's own cheat-sheet table lists `AvatarOptimizer` as the
  answer for "Agent / tool-use task" (`:137`), with no mention anywhere on the page that
  constructing it currently raises `AttributeError` unconditionally. [trap] (verified: read
  the doc; cross-checked against the construction failure already confirmed by the skill) ·
  skill: **new**
- **Even if it could be constructed**, `_get_pos_neg_results` requires at least one example
  scoring `>= upper_bound` (default 1) **and** at least one scoring `<= lower_bound` (default
  0) on the **very first** iteration, else it raises `ValueError` immediately (`"No positive
  examples found..."` / `"No negative examples found..."`, `avatar_optimizer.py:169-172`);
  `process_example` swallows any exception from either the actor or the metric and returns
  `(example, None, 0)` (`:105-111`); evaluation uses a bespoke `ThreadPoolExecutor`
  (`thread_safe_evaluator`, `:114-137`), not `dspy.Evaluate`. Rough cost, if it worked:
  `max_iters * (len(trainset) + 2)` calls (one comparator + one feedback-instruction call per
  iteration, plus a full trainset pass). `best_score` sentinels are hardcoded finite `±999`,
  not `±inf` (`:179`). [trap][number] (verified: read) · skill: **new** (framed conditionally,
  since the class cannot be built)

### `## MET`

- **SIMBA's metric contract is looser than `dspy.Evaluate`'s, and every one of its failure
  modes resolves to a silent `score=0.0`** — see the `SIMBA`/`wrap_program` items above
  (crash-then-crash, and even its own explicit `ValueError` for a `Prediction` with no
  `.score`, are all caught by the same `try/except`). [trap] (verified: read) · skill: **new**
  (extends the existing trap with the double-failure and self-validation-swallowed cases)
- **`BootstrapFinetune`'s trace filter has the identical truthiness bug as `BootstrapFewShot`,
  and is missing from the skill's own list of affected optimizers** — see above. [trap]
  (verified: read) · skill: **wrong**
- **`bootstrap_trace_data`'s `wrapped_metric` is the shared point where a metric's raw return
  value enters both `BootstrapFinetune` and `GRPO`'s training data**: `return metric(example,
  prediction, trace) if metric else True` (`bootstrap_trace.py:57-59`) — with `metric=None`,
  every row scores `True` and (for `BootstrapFinetune`) nothing is ever filtered since
  `data_dict["score"]` isn't even set unless a metric is given (`:149-150`). [api] (verified:
  read) · skill: **new**
- `eval_candidate_program`'s blanket `except Exception: ... return Prediction(score=0.0,
  results=[])` (`teleprompt/utils.py:59-62`), shared by `MIPROv2` and `BetterTogether` — an
  evaluation crash and a genuine 0 score are indistinguishable downstream. [trap] (verified:
  read) · skill: **new**

### `## DATA`

- **`create_n_fewshot_demo_sets` (`MIPROv2`) and `BootstrapFewShotWithRandomSearch`
  implement the identical "3 pinned seeds + N shuffled" shape with opposite bookkeeping** —
  one subtracts 3 from the requested count so the output equals exactly N
  (`teleprompt/utils.py:350`), the other does not, so its output is N+3
  (`random_search.py:75`). Anyone porting a candidate count between the two would be off by
  3 in one direction. [trap] (verified: read, both sites) · skill: **new**
- **`InferRules`'s 0.5/0.5 split is unshuffled and applies to whatever `trainset` `InferRules`
  itself receives** (`infer_rules.py:24-26`) — confirmed exactly matches the citation the
  skill's `data.md` already has (`"InferRules splits int(0.5 * len(trainset)), unshuffled..."`)
  · skill: same
- **`KNNFewShot`'s per-call "trainset" is the `k` nearest neighbours of that single input**,
  re-derived from the KNN index fresh on every forward call, and handed to a brand-new
  `BootstrapFewShot(**few_shot_bootstrap_args)` against the **original** `student` (not
  `student_copy`) — see the `KNNFewShot` item above. [pattern] (verified: read) · skill: **new**
- `BootstrapFewShot`'s own consumption order — literal trainset order, stop-early once
  `max_bootstrapped_demos` successes are found — directly answers "the order in which it
  consumes the trainset" for the rung one below `pairs.py`'s `bootstrap` optimizer. [number]
  (verified: read) · skill: **new**
- `BetterTogether`'s auto-split, confirmed exact: `valset = trainset[:num_val_examples];
  trainset = trainset[num_val_examples:]` — the **front** `valset_ratio` fraction, unshuffled
  (`bettertogether.py:340-343`) · skill: same as `data.md`'s existing citation

## 3. Code worth keeping

**`Predict.reset()` + `reset_copy()` — why every `BootstrapFewShot`/`LabeledFewShot` compile
strips `.lm`** (`dspy/predict/predict.py:65-69`, `dspy/primitives/base_module.py:147-154`,
outside this slice but the direct cause of a slice-internal trap; ran on the installed
package):

```python
# dspy/predict/predict.py:65-69
def reset(self):
    self.lm = None
    self.traces = []
    self.train = []
    self.demos = []

# dspy/primitives/base_module.py:147-154
def reset_copy(self):
    """Deep copy the module and reset all parameters."""
    new_instance = self.deepcopy()
    for param in new_instance.parameters():
        param.reset()
    return new_instance
```

**GRPO's default-construction crash and its very next, also-failing, adapter fallback**
(`dspy/teleprompt/grpo.py:33,44,63-77,467-468`; ran on the installed package):

```python
def __init__(self, metric=None, ..., exclude_demos: bool = False, ...):
    ...
    assert failure_score > format_failure_score, "..."
    if self.use_train_as_val:
        assert report_train_scores, "..."
    assert exclude_demos, "exclude_demos==False is not supported yet. Please set it to True."
    assert multitask, "independent GRPO training jobs ... not supported yet. ..."
# --- later, inside compile(), building one training example ---
adapter = self.adapter[pred_lm] or settings.adapter or XMLAdapter()
assert isinstance(adapter, ChatAdapter), f"Adapter {adapter} is not a ChatAdapter. " \
    "GRPO training is not supported for this adapter."
```

**`SIMBA`'s rollout-sampling temperature is hardcoded, separate from its own "temperature"
knobs** (`dspy/teleprompt/simba_utils.py:14-32`; read):

```python
def prepare_models_for_resampling(program, n, teacher_settings=None):
    lm = program.get_lm() or dspy.settings.lm
    start_rollout_id = lm.kwargs.get("rollout_id", 0)
    rollout_ids = [start_rollout_id + i for i in range(n)]
    start_rollout_idx, models = 0, []
    if teacher_settings:
        teacher_lm = teacher_settings.get("lm") or lm
        teacher_lm.kwargs["rollout_id"] = rollout_ids[start_rollout_idx]
        models.append(teacher_lm)
        start_rollout_idx += 1
    models.extend([lm.copy(rollout_id=r, temperature=1.0) for r in rollout_ids[start_rollout_idx:]])
    return models
```

**`create_dataset_summary` — the exact shape of what `MIPROv2`'s data-aware proposer sends to
the model** (`dspy/propose/dataset_summary_generator.py:48-78`, trimmed; read):

```python
def create_dataset_summary(trainset, view_data_batch_size, prompt_model, log_file=None, verbose=False):
    upper_lim = min(len(trainset), view_data_batch_size)
    prompt_model = prompt_model if prompt_model else dspy.settings.lm
    with dspy.context(lm=prompt_model):
        observation = dspy.Predict(DatasetDescriptor, n=1, temperature=1.0)(
            examples=order_input_keys_in_string(trainset[0:upper_lim].__repr__())
        )
    observations = observation["observations"]
    skips = 0
    try:
        max_calls = 10
        calls = 0
        for b in range(view_data_batch_size, len(trainset), view_data_batch_size):
            calls += 1
            if calls >= max_calls:
                break
            upper_lim = min(len(trainset), b + view_data_batch_size)
            with dspy.context(lm=prompt_model):
                output = dspy.Predict(DatasetDescriptorWithPriorObservations, n=1, temperature=1.0)(
                    prior_observations=observations,
                    examples=order_input_keys_in_string(trainset[b:upper_lim].__repr__()),
                )
            if len(output["observations"]) >= 8 and output["observations"][:8].upper() == "COMPLETE":
                skips += 1
                if skips >= 5:
                    break
                continue
            observations += output["observations"]
    except Exception:
        pass  # uses observations from past round for a summary
```

**`COPRO`'s single- vs multi-predictor candidate-pool asymmetry — the source of the quadratic
cost** (`dspy/teleprompt/copro_optimizer.py:192-201,321-326`; read):

```python
candidates_ = latest_candidates[id(p_old)]  # this round's new candidates only
if len(module.predictors()) > 1:
    # multi-predictor: re-score EVERY candidate generated so far, at every depth
    candidates_ = all_candidates[id(p_old)]
...
new_candidates[id(p_base)] = instr.completions
all_candidates[id(p_base)].proposed_instruction.extend(instr.completions.proposed_instruction)
all_candidates[id(p_base)].proposed_prefix_for_output_field.extend(
    instr.completions.proposed_prefix_for_output_field,
)
```

**The `present / expected` bug in `bootstrap_trace.py`'s partial-parse handler** (`dspy/
teleprompt/bootstrap_trace.py:74-94`; read — see the `TRAP` entry below):

```python
present = list(parsed_result.keys()) if parsed_result else None
expected = list(failed_signature.output_fields.keys())
...
if present:
    failed_pred = FailedPrediction(
        completion_text=completion_str,
        format_reward=format_failure_score
        + (failure_score - format_failure_score) * (present / expected),   # both are lists
    )
else:
    failed_pred = FailedPrediction(completion_text=completion_str, format_reward=format_failure_score)
```

**`BootstrapFewShotWithRandomSearch`'s pinned-seed loop, unadjusted** (`dspy/teleprompt/
random_search.py:75-119`, trimmed; read):

```python
for seed in range(-3, self.num_candidate_sets):     # num_candidate_sets = num_candidate_programs
    if seed == -3:
        program = student.reset_copy()                          # zero-shot
    elif seed == -2:
        program = LabeledFewShot(k=self.max_labeled_demos).compile(student, trainset=trainset_copy,
                                                                     sample=labeled_sample)
    elif seed == -1:
        program = BootstrapFewShot(metric=self.metric, ...).compile(student, teacher=teacher,
                                                                      trainset=trainset_copy)
    else:
        random.Random(seed).shuffle(trainset_copy)
        size = random.Random(seed).randint(self.min_num_samples, self.max_num_samples)
        program = BootstrapFewShot(metric=self.metric, max_bootstrapped_demos=size, ...).compile(
            student, teacher=teacher, trainset=trainset_copy)
```

## 4. Probes worth adding

All five ran on `.venv-dspy/bin/python`, offline, with all four `*_API_KEY` vars unset.

```python
# [checked: reset-copy-clears-predictor-lm]
# "LabeledFewShot.compile() and BootstrapFewShot.compile() both return a program whose
#  predictor .lm is None, even when the input student had an explicit .lm set."
def probe_reset_copy_clears_lm():
    import dspy
    from dspy.utils.dummies import DummyLM

    lm = DummyLM([{"output": "blue"}])

    class M(dspy.Module):
        def __init__(self):
            super().__init__()
            self.p = dspy.Predict("input -> output")

        def forward(self, **kw):
            return self.p(**kw)

    student = M()
    student.set_lm(lm)
    ex = dspy.Example(input="x", output="blue").with_inputs("input")

    labeled = dspy.LabeledFewShot(k=1).compile(student, trainset=[ex])
    if labeled.predictors()[0].lm is not None:
        return "LabeledFewShot.compile() kept .lm set (expected None)"

    dspy.configure(lm=lm)
    student2 = M()
    student2.set_lm(lm)
    bf = dspy.BootstrapFewShot(metric=lambda e, p, t=None: True,
                                max_bootstrapped_demos=1, max_labeled_demos=1)
    compiled = bf.compile(student2, trainset=[ex])
    if compiled.predictors()[0].lm is not None:
        return "BootstrapFewShot.compile() kept .lm set (expected None)"
    return None
```

```python
# [checked: infer-rules-zero-candidates-returns-none]
# "InferRules(num_candidates=0).compile(...) returns None, silently, after logging
#  'Final best score: -inf'."
def probe_infer_rules_zero_candidates():
    import dspy
    from dspy.utils.dummies import DummyLM

    dspy.configure(lm=DummyLM([{"decision": "one-term", "rule": "x"}] * 20))
    student = dspy.Predict("a, b -> decision")
    trainset = [dspy.Example(a="x", b="y", decision="one-term").with_inputs("a", "b")
                for _ in range(4)]
    ir = dspy.InferRules(num_candidates=0, num_rules=1, metric=lambda e, p, t=None: True)
    result = ir.compile(student, trainset=trainset)
    if result is not None:
        return f"expected compile() to return None, got {result!r}"
    return None
```

```python
# [checked: copro-depth-zero-indexerror]
# "COPRO(depth=0).compile(...) raises IndexError, not a clear message, because
#  evaluated_candidates is never populated when the depth loop body never runs."
def probe_copro_depth_zero():
    import sys
    import dspy
    sys.path.insert(0, "/home/user/kohaerenzprotokoll/scripts")
    from lm_fixture import FixtureLM, fill, offline

    with offline(FixtureLM(fill())):
        student = dspy.Predict("a, b -> decision")
        trainset = [dspy.Example(a="x", b="y", decision="one-term").with_inputs("a", "b")
                    for _ in range(4)]
        copro = dspy.COPRO(metric=lambda e, p, t=None: 1.0, breadth=2, depth=0)
        try:
            copro.compile(student, trainset=trainset)
        except IndexError:
            return None
        return "expected IndexError, compile() did not raise it"
```

```python
# [checked: grpo-default-construction-fails]
# "dspy.teleprompt.grpo.GRPO(metric=...) with no other arguments always raises
#  AssertionError, because exclude_demos defaults to False but must be True."
def probe_grpo_default_construction():
    from dspy.teleprompt.grpo import GRPO
    try:
        GRPO(metric=lambda *a, **k: 1.0)
    except AssertionError as e:
        if "exclude_demos" in str(e):
            return None
        return f"AssertionError for the wrong reason: {e}"
    return "GRPO(metric=...) constructed without raising (expected AssertionError)"
```

```python
# [checked: signature-optimizer-cannot-construct]
# "dspy.teleprompt.signature_opt.SignatureOptimizer cannot be constructed at all on 3.3.1:
#  it prints its deprecation warning, then raises TypeError from a stale positional call
#  into COPRO.__init__."
def probe_signature_optimizer_broken():
    from dspy.teleprompt.signature_opt import SignatureOptimizer
    try:
        SignatureOptimizer(metric=lambda *a, **k: 1.0)
    except TypeError as e:
        if "positional argument" in str(e):
            return None
        return f"TypeError for the wrong reason: {e}"
    return "SignatureOptimizer(metric=...) constructed without raising (expected TypeError)"
```

## 5. Surface worth asserting

Every line below is `inspect.signature(...)` run against the **installed** package
(`.venv-dspy/bin/python`, offline):

```
dspy.LabeledFewShot(k=16)
dspy.LabeledFewShot.compile(self, student, *, trainset, sample=True)

dspy.BootstrapFewShot(metric=None, metric_threshold=None, teacher_settings=None,
    max_bootstrapped_demos=4, max_labeled_demos=16, max_rounds=1, max_errors=None)
dspy.BootstrapFewShot.compile(self, student, *, teacher=None, trainset)

dspy.BootstrapFewShotWithRandomSearch(metric, teacher_settings=None,
    max_bootstrapped_demos=4, max_labeled_demos=16, max_rounds=1,
    num_candidate_programs=16, num_threads=None, max_errors=None, stop_at_score=None,
    metric_threshold=None)
dspy.BootstrapFewShotWithRandomSearch.compile(self, student, *, teacher=None, trainset,
    valset=None, restrict=None, labeled_sample=True)

dspy.BootstrapFewShotWithOptuna(metric, teacher_settings=None, max_bootstrapped_demos=4,
    max_labeled_demos=16, max_rounds=1, num_candidate_programs=16, num_threads=None)
dspy.BootstrapFewShotWithOptuna.compile(self, student, *, teacher=None, max_demos, trainset,
    valset=None)

dspy.KNNFewShot(k: int, trainset: list[Example], vectorizer: Embedder,
    **few_shot_bootstrap_args: dict[str, Any])
dspy.KNNFewShot.compile(self, student, *, teacher=None)

dspy.InferRules(num_candidates=10, num_rules=10, num_threads=None, teacher_settings=None,
    **kwargs)
dspy.InferRules.compile(self, student, *, teacher=None, trainset, valset=None)

dspy.COPRO(prompt_model=None, metric=None, breadth=10, depth=3, init_temperature=1.4,
    track_stats=False, **_kwargs)
dspy.COPRO.compile(self, student, *, trainset, eval_kwargs=None)

# from dspy.teleprompt.signature_opt import SignatureOptimizer  (not on dspy.*)
SignatureOptimizer(prompt_model=None, metric=None, breadth=10, depth=3,
    init_temperature=1.4, verbose=False, track_stats=False)   # always raises TypeError
SignatureOptimizer.compile(self, student, *, devset, eval_kwargs)

dspy.MIPROv2(metric: Callable, prompt_model=None, task_model=None, teacher_settings=None,
    max_bootstrapped_demos: int = 4, max_labeled_demos: int = 4,
    auto: Literal['light','medium','heavy'] | None = 'light', num_candidates=None,
    num_threads=None, max_errors=None, seed: int = 9, init_temperature: float = 1.0,
    verbose: bool = False, track_stats: bool = True, log_dir=None, metric_threshold=None)
dspy.MIPROv2.compile(self, student, *, trainset, teacher=None, valset=None,
    num_trials=None, max_bootstrapped_demos=None, max_labeled_demos=None, seed=None,
    minibatch: bool = True, minibatch_size: int = 35, minibatch_full_eval_steps: int = 5,
    program_aware_proposer: bool = True, data_aware_proposer: bool = True,
    view_data_batch_size: int = 10, tip_aware_proposer: bool = True,
    fewshot_aware_proposer: bool = True, requires_permission_to_run=None,
    provide_traceback=None)

dspy.SIMBA(*, metric, bsize: int = 32, num_candidates: int = 6, max_steps: int = 8,
    max_demos: int = 4, prompt_model=None, teacher_settings=None,
    demo_input_field_maxlen: int = 100000, num_threads=None,
    temperature_for_sampling: float = 0.2, temperature_for_candidates: float = 0.2)
dspy.SIMBA.compile(self, student, *, trainset, seed: int = 0)

dspy.BetterTogether(metric: Callable, **optimizers: Teleprompter)
dspy.BetterTogether.compile(self, student, *, trainset, teacher=None, valset=None,
    num_threads=None, max_errors=None, provide_traceback=None, seed=None,
    valset_ratio: float = 0.1, shuffle_trainset_between_steps: bool = True,
    strategy: str = 'p -> w -> p', optimizer_compile_args=None)

dspy.BootstrapFinetune(metric=None, multitask: bool = True, train_kwargs=None,
    adapter=None, exclude_demos: bool = False, num_threads=None)
dspy.BootstrapFinetune.compile(self, student, trainset, teacher=None)   # trainset positional

dspy.Ensemble(*, reduce_fn=None, size=None, deterministic=False)
dspy.Ensemble.compile(self, programs)

dspy.AvatarOptimizer(metric: Callable, max_iters: int = 10, lower_bound: int = 0,
    upper_bound: int = 1, max_positive_inputs=None, max_negative_inputs=None,
    optimize_for: str = 'max')          # __init__ always raises AttributeError
dspy.AvatarOptimizer.compile(self, student, *, trainset)

# from dspy.teleprompt.grpo import GRPO  (not on dspy.*)
GRPO(metric=None, multitask: bool = True, train_kwargs=None, adapter=None,
    exclude_demos: bool = False, num_threads: int = 6, num_train_steps: int = 100,
    seed: int = 0, num_dspy_examples_per_grpo_step: int = 1,
    num_rollouts_per_grpo_step: int = 1, use_train_as_val: bool = False,
    num_steps_for_val: int = 5, report_train_scores: bool = False,
    failure_score: float = 0, format_failure_score: float = -1,
    variably_invoked_predictor_grouping_mode: Literal['truncate','fill','ragged'] = 'truncate',
    variably_invoked_predictor_fill_strategy: Literal['randint','max'] | None = None)
    # __init__ raises AssertionError at defaults (exclude_demos must be True)
GRPO.compile(self, student, trainset, teacher=None, valset=None, **kwargs)

dspy.propose.GroundedProposer(prompt_model, program, trainset, view_data_batch_size=10,
    use_dataset_summary=True, program_aware=True, use_task_demos=True,
    num_demos_in_context=3, use_instruct_history=True, use_tip=True,
    set_tip_randomly=True, set_history_randomly=True, verbose=False, rng=None,
    init_temperature: float = 1.0)
GroundedProposer.propose_instructions_for_program(self, trainset, program, demo_candidates,
    trial_logs, N)
GroundedProposer.propose_instruction_for_predictor(self, program, predictor, pred_i,
    demo_candidates, demo_set_i, trial_logs, tip=None)

dspy.propose.dataset_summary_generator.create_dataset_summary(trainset,
    view_data_batch_size, prompt_model, log_file=None, verbose=False)

dspy.teleprompt.bootstrap_trace.bootstrap_trace_data(program, dataset, metric=None,
    num_threads=None, raise_on_error=True, capture_failed_parses=False,
    failure_score: float = 0, format_failure_score: float = -1,
    log_format_failures: bool = False, callback_metadata=None, capture_crashes=False)
```

`dspy.__version__` on the installed package: `3.3.1`.

## 6. Ten things the skill must say

1. `BootstrapFewShot.compile()` and `LabeledFewShot.compile()` both hand back a program with
   every predictor's `.lm` set to `None` — via `student.reset_copy()` →
   `Predict.reset()` — **even if `student.set_lm(...)` was called first.** The official docs'
   own claim that "every optimizer" does this and "the original stays untouched" is false for
   `BootstrapFinetune` and `GRPO`, which mutate the passed-in student directly instead.
2. `GRPO` is not `dspy.GRPO` — it is unreachable except via `from dspy.teleprompt.grpo import
   GRPO` — and its own default constructor (`exclude_demos=False`) immediately raises
   `AssertionError`; its default adapter fallback (`XMLAdapter()`) then fails its own very
   next assertion (must be `ChatAdapter`) unless one is configured explicitly.
3. `GRPO` needs an external, RL-capable LM provider that no file in `dspy/clients/` ships
   (`Provider.reinforceable` defaults `False` everywhere); DSPy's own RL tutorials install
   `arbor-ai` separately and call `ArborGRPO`, never `dspy.GRPO`/`dspy.teleprompt.grpo.GRPO`
   directly, on real GPU hardware ("4xH100... a couple of hours").
4. `SignatureOptimizer` (`from dspy.teleprompt.signature_opt import SignatureOptimizer`)
   cannot be constructed at all on 3.3.1 — it prints "deprecated, use COPRO" and then raises
   `TypeError` from a stale positional call into `COPRO.__init__`. DSPy's own test file named
   for it tests `COPRO` instead and never catches this.
5. `BootstrapFewShotWithRandomSearch` builds `num_candidate_programs + 3` candidates, not
   `num_candidate_programs` — both official doc pages that describe this undercount or omit
   the +3, and the sibling helper `MIPROv2` uses for the same "3 pinned + N" shape handles the
   count the opposite way (subtracts 3 so its own total is exact).
6. `MIPROv2`'s periodic full-eval fires every `minibatch_full_eval_steps + 1` trials (every 6
   by default), not every `minibatch_full_eval_steps` (5) as its own parameter name and its
   own doc page state; its cost-estimator method, `_estimate_lm_calls`, is defined but never
   called anywhere in the package.
7. `dspy.propose.GroundedProposer` — what `MIPROv2`'s default `program_aware`/
   `data_aware` proposers actually send to `prompt_model`: the program's own signature source
   (skipped only for bare `Predict`/`ChainOfThought`), and, via `create_dataset_summary`, the
   literal `repr()` of raw trainset `Example` objects in batches, up to a hardcoded
   `max_calls=10` — directly relevant to this project's corpus-text rule.
8. `COPRO`'s cost is `breadth × depth` for a one-predictor program (matches `pairs.py`'s own
   `SameTerm`), but grows **quadratically** in `depth` for a multi-predictor one, because the
   multi-predictor branch rescoring the whole accumulated candidate pool every round — the
   official doc's own linear formula only holds for one predictor. `COPRO(depth=0)` crashes
   with a bare `IndexError`.
9. `SIMBA` hardcodes `temperature=1.0` on every rollout-sampling LM copy, regardless of the
   configured LM's own temperature — `temperature_for_sampling`/`temperature_for_candidates`
   control only program **selection**, never LM sampling. Its `append_a_rule` strategy sends
   the program's own source and the training example's **gold label** to the reflection
   model; appended advice is never pruned (only demos are, and only probabilistically via a
   Poisson-distributed drop that does not hard-cap `max_demos`).
10. `InferRules(num_candidates=0)` silently returns `None` from `compile()` (after logging
    "Final best score: -inf"). `BootstrapFinetune`'s default `metric=None` trains on every
    bootstrapped trace unfiltered — DSPy's own fine-tuning tutorial runs it exactly that way
    — and when a metric *is* given, its truthiness trap on a `Prediction`-returning metric is
    the same bug family `optimizers.md` already names for five other optimizers, but leaves
    `BootstrapFinetune` off that list.
