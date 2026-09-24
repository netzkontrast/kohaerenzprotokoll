# dspy-auto-gepa: knowledge extract

## 1. Header

- **Repo**: `/home/user/dspy-auto-gepa` (origin `github.com/netzkontrast/dspy-auto-gepa`, a fork; `pyproject.toml:28-32` names `thememium/dspy-auto-gepa`). **Commit** `80a5402` (`80a54028d453d85beef1f27f4e31755da865b66e`, 2026-07-04, "chore(uv): update version"), 157 commits, package version `0.1.9` (`pyproject.toml:3`).
- **License**: MIT (`LICENSE:1-21`, `pyproject.toml:24`).
- **DSPy targeted**: `dspy>=3.2.1` (`pyproject.toml:18`). `uv.lock` pins `dspy 3.2.1` and `gepa 0.0.27`. `README.md:46` says "Requires **DSPy 3.1+**", which is false: on 3.1.0 the import fails. Python: `requires-python = ">=3.12"` (`pyproject.toml:6`, `.python-version`), but every file parses on 3.11 and the offline suite passes there.
- **Does its API usage hold on 3.3.1?** Yes, for every DSPy call it makes: `dspy.GEPA(metric, auto, reflection_lm, num_threads, track_stats, log_dir)`, `.compile(trainset=, valset=)`, `dspy.Evaluate`, `dspy.RLM(sig, verbose=)`, `dspy.Parallel`, `Module.set_lm`, `Signature.with_updated_fields`, `save`/`load`. I verified this on DSPy 3.3.1 + gepa 0.1.4: the whole offline suite, plus an end-to-end `AutoGEPA.run()` with fixture LMs.
- **What it is**: a thin wrapper (3,493 lines in `src/`) that turns `rows + dspy.Module` into `dspy.Example`s. It infers fields from the module's signature and splits train/val/test with a seeded shuffle. It has an LLM (default `dspy.RLM`) draft a metric `.py` file, unless `metric=Path` is given. It then runs `dspy.GEPA(auto="light")`, compares baseline and optimized on the test split, and saves the program by name. A second half, `AutoData` (`generator.py`, 1,686 lines), generates synthetic rows with an LLM.
- **What I ran** (all offline). Every command had `*_API_KEY` unset, `HTTPS_PROXY`/`HTTP_PROXY` black-holed to `127.0.0.1:9`, and `DSPY_CACHEDIR` in the scratchpad. It also loaded my guard `scratchpad/guard/offline_guard.py`, which makes `litellm.completion/acompletion/text_completion/responses` raise and records any attempt. Every run reported "attempted live LM calls: 0", except the one test run deliberately to show the leak. Environments: a venv `scratchpad/venvs/autogepa312` (Python 3.12.3, dspy 3.3.1, gepa 0.1.4, litellm 1.102.1, pandas 3.0.6, pyarrow 25.0.1, the `deno` 2.9.7 pip package) and `venvs/ag311` (Python 3.11 + dspy 3.3.1). I also used `uv run --isolated` with `dspy==3.2.1` and `dspy==3.1.0` for surface checks. All work ran on a copy of the repo (`scratchpad/repo-copy`); the original is untouched (`git status` clean). The runs:
  - the test suite (132 tests) minus the unmocked test: 131 passed;
  - the unmocked test alone, under the guard;
  - `scratchpad/verify/checks.py` (checks A–U);
  - `checks2.py` (V–Y);
  - `e2e.py` (full `run()` with fixture LMs) and `e2e_force.py` (`run(force=True)` on the same directory);
  - `broken_metric.py` (a metric that raises);
  - `inspect.signature` checks on DSPy 3.3.1, 3.2.1 and 3.1.0.

  "Verified: A" below means check A in `checks.py`, and so on.

## 2. Knowledge items

## API

- **`Evaluate.score` is a percentage** — `dspy.Evaluate.__call__` returns `EvaluationResult(score=round(100 * ncorrect / ntotal, 2), results=...)`, with `ncorrect = sum(score for *_, score in results)`. So `run_baseline()` returns `{"score": 0–100}` and `RunResult.improvement` is in percentage points. `dspy/evaluate/evaluate.py:180,223-226` (3.3.1); `src/dspy_auto_gepa/runner.py:303-311,362-366` [api] (verified: e2e.py printed `RunResult(baseline=100.0, optimized=100.0, improvement=0.0, ...)`) → here: baseline.py (store the scale next to every number).
- **`Evaluate` aggregates with plain `sum()`** — metric returns must support `0 + x`. `float` works, and so does `dspy.Prediction`, which has `__float__`, `__add__`, `__radd__`, `__truediv__` and `__lt__`: `sum([Prediction(score=.5), Prediction(score=.25)]) == 0.75`. Summing dicts raises `TypeError: unsupported operand type(s) for +: 'int' and 'dict'`. `dspy/evaluate/evaluate.py:180`; the repo's claim is in `src/dspy_auto_gepa/metric_builder.py:16-19` and the error text in `metric_builder.py:261-265` [api] (verified: python on 3.3.1) → here: pairs.py metric.
- **`Evaluate` on an empty devset crashes** — `ntotal == 0` gives `ZeroDivisionError: division by zero` in the score line. `dspy/evaluate/evaluate.py:182,224` [trap] (verified: R) → here: baseline.py (refuse empty splits before evaluating).
- **`Evaluate` swallows up to `max_errors` exceptions** — `Evaluate(*, devset, metric=None, num_threads=None, display_progress=False, display_table=False, max_errors=None, provide_traceback=None, failure_score=0.0, save_as_csv=None, save_as_json=None)`. `max_errors=None` inherits `dspy.settings.max_errors` = 10. A program or metric exception is logged as `ERROR dspy.utils.parallelizer: Error for Example(...)` and scored `failure_score` (0.0) until the cap is hit. `dspy/evaluate/evaluate.py:94-97,165,178`; `dspy/dsp/utils/settings.py:32` [api] (verified: broken_metric.py, where `run_baseline` returned `{'score': 0.0}` with no exception) → here: lmrun.py/pairs.py (P15: "could not score" must not become 0).
- **`answer_exact_match` takes objects, not strings** — the signature is `answer_exact_match(example, pred, trace=None, frac=1.0)`. It reads `.answer` from both arguments and returns a `bool`. Called with two strings it raises `AttributeError: 'str' object has no attribute 'answer'`. For strings, use `dspy.evaluate.EM(prediction, answers_list)`, which normalizes (`EM('The Paris', ['paris'])` is `True`), or `normalize_text(s)`. `dspy.evaluate` in 3.3.1 exports `CompleteAndGrounded, EM, Evaluate, EvaluationResult, SemanticF1, answer_exact_match, answer_passage_match, auto_evaluation, evaluate, metrics, normalize_text`; there is no `fuzzy_match`. Misuse: `metric_builder.py:31,123,184` [api] (verified: python on 3.3.1) → here: pairs.py.
- **`dspy.Parallel` with failed examples returns a 3-tuple** — the signature is `dspy.Parallel(num_threads=None, max_errors=None, access_examples=True, return_failed_examples=False, provide_traceback=None, disable_progress_bar=False, timeout=120, straggler_limit=3)`. Tasks are `(module, example)` pairs, and each example is passed as `**example.inputs()`. With `return_failed_examples=True` it returns `(results, failed_examples, exceptions)`. `generator.py:939-940,1124-1127` unwrap `[0]`. `generator.py:782-788` and `1353-1359` iterate the tuple as if it were the result list; they work only because the first element is a list and gets flattened by `result if isinstance(result, list) else [result]`. [api] (verified: real `Parallel` returned `tuple` of 3 lists).
- **ChainOfThought has no `.signature` in 3.3.1** — `dspy.ChainOfThought(sig)` has one predictor, `('predict', Predict)`, whose signature has `reasoning` prepended. `named_predictors()` always yields `Predict` objects, never `ChainOfThought`. `dspy.ReAct` and `dspy.RLM` expose `.signature`, which is the user's signature (`question -> answer`, `context, query -> answer`). `src/dspy_auto_gepa/data.py:218-274` depends on this [api] (verified: C) → here: check_dspy_surface.py.
- **Signatures always have a docstring** — a class signature with no docstring gets `'Given the fields `q`, produce the fields `a`.'` as `__doc__`. A whitespace docstring (`""" """`) stays `' '`. So `AutoData`'s "Module signature has no docstring and no description was provided" (`generator.py:615-620`) fires only for whitespace docstrings; its test has to force `NoDocSignature.__doc__ = ""` to reach it (`tests/test_generator.py:221-236`) [api] (verified: python on 3.3.1).
- **`dspy.LM` defaults** — `dspy.LM("openrouter/openai/gpt-oss-120b")` gives `cache=True, kwargs={'temperature': None, 'max_tokens': None}`. Constructing it makes no network call. `src/dspy_auto_gepa/config.py:32-35` [api] (verified: U) → here: lmrun.py (always pass `cache=False`).
- **OpenRouter provider pinning passes through `extra_body`** — `dspy.LM("openrouter/openai/gpt-oss-20b", extra_body={"provider": {"order": ["groq"], "allow_fallbacks": False}}, cache=False)`. The examples also use the model suffix `openrouter/openai/gpt-oss-120b:nitro`. `examples/basic.py:7-11`, `examples/data_split.py:11-14` [claim] (not run: it needs the provider).
- **Runtime-typed output fields** — a class-body annotation cannot use a runtime type, so the generator builds `pydantic.create_model(name, **{f: (type, ...)})` with `Literal.__getitem__(tuple(values))` for enum fields. It then sets `generated_outputs: list[Model]` with `Sig.with_updated_fields("generated_outputs", type_=list.__class_getitem__((model,)))`. ChatAdapter renders this as `` `generated_outputs` (list[GeneratedOutput]) `` plus a JSON-schema note. `generator.py:89-114,506-540` [recipe] (verified: formatted and parsed with `ChatAdapter` on 3.3.1) → here: job 2 (typed name lists).
- **A typed list parse is all-or-nothing** — one element outside the `Literal` (here `'LOW'` against `Literal['high','low']`) raises a pydantic `literal_error`, and the whole batch fails `ChatAdapter.parse`. `generator.py:111` [trap] (verified: python on 3.3.1).
- **Per-call LM override** — `with dspy.context(lm=...)` (`quality.py:198,247`) and `with dspy.settings.context(lm=...)` (`generator.py:724,750,879,1090,1319`) are the same mechanism. Both scope the LM to a block without touching the global LM. [api] (read, not run).
- **`dspy.configure` inside an imported metric changes the process-wide LM** — Example 3 of the metric-writing prompt does `_judge_lm = dspy.LM("openrouter/openai/gpt-oss-120b"); dspy.configure(lm=_judge_lm)` at module level. `load_metric()` executes the file, so after loading it the global LM changed from `openai/student-model` to `openrouter/openai/gpt-oss-120b`. The program under optimization would then run on the judge's model. `metric_builder.py:151-153`; `artifacts.py:8-19` [trap] (verified: V) → here: lmrun.py (never configure globally from a metric file).
- **LM errors are wrapped in 3.3.1** — a failing litellm call surfaces as `dspy.utils.exceptions.LMUnexpectedError: [openrouter/openai/gpt-oss-120b] <original message>`, raised from `dspy/clients/lm.py:261`. [api] (verified: the guarded run of the unmocked test) → here: lmrun.py status mapping.
- **Saving writes state only, and loading mutates in place** — `optimized_module.save("x.json")` writes keys `['predict', 'metadata']` for a ChainOfThought. GEPA's `detailed_results` attribute is not saved. `module.load(path)` mutates the module in place. `runner.py:385,423` [api] (verified: e2e.py).
- **Example construction** — `dspy.Example(**{k: row[k] for k in input_fields + output_fields}).with_inputs(*input_fields)`. Extra columns are dropped, and a missing column raises a bare `KeyError`. Nothing checks that the input and output lists are disjoint: `input_fields=["message","urgency"]` produced inputs `message, urgency` and labels `sentiment`, so a gold label became a model input. `data.py:345-354` [trap] (verified: final check) → here: trainset.py (assert inputs ∩ labels = ∅).

## OPT

- **`dspy.GEPA` constructor in 3.3.1, all parameters and defaults** — `metric` (required), `auto=None`, `max_full_evals=None`, `max_metric_calls=None`, `reflection_minibatch_size=3`, `candidate_selection_strategy='pareto'`, `reflection_lm=None`, `skip_perfect_score=True`, `add_format_failure_as_feedback=False`, `instruction_proposer=None`, `component_selector='round_robin'`, `use_merge=True`, `max_merge_invocations=5`, `num_threads=None`, `failure_score=0.0`, `perfect_score=1.0`, `log_dir=None`, `track_stats=False`, `use_wandb=False`, `wandb_api_key=None`, `wandb_init_kwargs=None`, `track_best_outputs=False`, `warn_on_score_mismatch=True`, `use_mlflow=False`, `seed=0`, `gepa_kwargs=None`. The compile signature is `compile(student, *, trainset, teacher=None, valset=None)`. [api] (verified: `inspect.signature` on 3.3.1) → here: check_dspy_surface.py.
- **What auto-gepa passes** — `dspy.GEPA(metric=self.load_metric(), auto=self.config.gepa_auto, reflection_lm=self.config.reflection_lm, num_threads=self.config.num_threads, track_stats=True, log_dir=<artifact_dir>/<name>/gepa_logs)`, then `optimizer.compile(task_module, trainset=datasets.train, valset=datasets.val)`. Everything else is DSPy's default (seed 0, merge on, minibatch 3, `skip_perfect_score`, `failure_score` 0.0, `perfect_score` 1.0). `runner.py:325-343` [api] (verified: e2e.py ran it on 3.3.1).
- **Wrapper defaults** — `gepa_auto="light"`, `num_threads=16`, `split=(0.7, 0.2, 0.1)`, `seed=42`, `artifact_dir=".auto_gepa"`, `metric_generator_verbose=True`. The config validates `gepa_auto in (light, medium, heavy)` and `sum(split) <= 1.0`. `runner.py:88-99`; `config.py:12-31` [api] (verified: A, U).
- **Exactly one budget knob** — setting none or more than one of `auto`, `max_full_evals`, `max_metric_calls` gives `AssertionError "Exactly one of max_metric_calls, max_full_evals, auto must be set."`. `max_full_evals` becomes `max_full_evals * (len(trainset) + len(valset))`. `dspy/teleprompt/gepa/gepa.py:427-432,558-559` [api] (read, not run).
- **What `auto` means** — `AUTO_RUN_SETTINGS = {"light": {"n": 6}, "medium": {"n": 12}, "heavy": {"n": 18}}` candidates (identical in 3.2.1). The budget is `auto_budget(num_preds, num_candidates, valset_size, minibatch_size=35, full_eval_steps=5)`:
  - N = `int(max(2*(num_preds*2)*log2(n), 1.5*n))`
  - total = `V + 5n + 35N + ((N+1)//5 + 1 + [N<5])*V`
  - `num_preds` = the number of named predictors plus Flex submodules; `V = len(valset)`, or `len(trainset)` without a valset.

  Trainset size does not enter the budget. `gepa.py:20-24,490-518,548-557` [api] (verified: `inspect` on 3.3.1 and 3.2.1) → here: pairs.py (n≈26: set `max_metric_calls` explicitly).
- **Measured budgets (metric calls)** — one predictor: light 384 / 388 / 400 / 420 / 460 / 520 for V = 1 / 2 / 5 / 10 / 20 / 35; medium 695–865; heavy 1042–1280. Two predictors: light 736–940, medium 1047–1285, heavy 1253–1525. [number] (verified: T, `GEPA.auto_budget` on 3.3.1).
- **What a light run costs on 10 rows** — setup: the 10 rows of `examples/basic.py` (7 train / 2 val / 1 test), one ChainOfThought predictor, `auto="light"`, fixture LMs. GEPA logged „Running GEPA for approx 388 metric calls of the program. This amounts to 43.11 full evals on the train+val set." The student LM was called 390 times (the 388 budget plus 2 test evaluations) and the reflection LM once. [number] (verified: e2e.py) → here: pairs.py GEPA rung (price it before asking for approval).
- **Perfect minibatches still spend budget** — after a candidate reached 1.0 at iteration 1, GEPA ran iterations 2–127. Each iteration evaluated a 3-example minibatch and logged „All subsample scores perfect for parent 1. Skipping." `skip_perfect_score` skips reflection, not evaluation, so the budget is spent anyway. [number] (verified: e2e.py log).
- **valset semantics** — „GEPA uses the trainset to perform reflective updates to the prompt, but uses the valset for tracking Pareto scores. If no valset is provided, GEPA will use the trainset for both." Without a valset, GEPA logs an overfitting warning. With `len(valset) > 35` it logs advice to shrink the valset. `gepa.py:531-532,567-580` [api] (read, not run).
- **A reflection LM is required** — `assert reflection_lm is not None or instruction_proposer is not None` runs at construction. The assert message recommends „`dspy.LM(model='gpt-5', temperature=1.0, max_tokens=32000)`". auto-gepa's default is `dspy.LM("openrouter/moonshotai/kimi-k2.5")` with cache on and no temperature or max_tokens. `gepa.py:441-445`; `config.py:34-35` [api] (verified: U).
- **Five-argument metric check at construction** — `inspect.signature(metric).bind(None, None, None, None, None)`; failure raises `TypeError("GEPA metric must accept five arguments: (gold, pred, trace, pred_name, pred_trace). See https://dspy.ai/api/optimizers/GEPA for details.")`. The check is present in 3.1.0, 3.2.1 and 3.3.1. `AutoGEPA.train()` with a three-argument metric file raised this before compile. `gepa.py:416-422` [api] (verified: I; source grep on 3.1.0 and 3.2.1) → here: check_dspy_surface.py, pairs.py.
- **GEPA is always seeded** — `seed=0` is the default (also in 3.2.1), used for `random.Random(self.seed)` and passed to `gepa.optimize(seed=...)`. The wrapper's `seed=42` only shuffles the split (`data.py:363`) and never reaches GEPA; run-to-run divergence comes from LM sampling. `gepa.py:320,582,660` [api] (verified: `inspect` on 3.3.1).
- **`log_dir` resumes, so `force=True` does not retrain** — DSPy says „Running GEPA with the same `log_dir` will resume the run from the last checkpoint." auto-gepa always uses `<artifact_dir>/<name>/gepa_logs`. A second `run(force=True)` on the same directory logged „Loading gepa state from run dir", made 4 student calls and 0 reflection calls, and re-promoted the old best. So `docs/basic.md:67` („`auto.run(force=True)   # Always retrain from scratch`") is false. With changed rows or metric, GEPA resumes stale state. `gepa.py:305-307`; `runner.py:325-329` [trap] (verified: e2e_force.py) → here: pairs.py (fresh `log_dir` per run, recorded in the ledger).
- **What `log_dir` holds (gepa 0.1.4)**:
  - `candidates.json`: a list of `{predictor_name: instruction}`;
  - `run_log.json`: a list with one entry per iteration (`i`, `selected_program_candidate`, `subsample_ids`, `subsample_scores`, `new_subsample_scores`, ...);
  - `gepa_state.bin`: the resume state;
  - `candidate_tree.html`;
  - `generated_best_outputs_valset/task_<i>/iter_<k>_prog_<j>.json`.

  auto-gepa parses none of it. [api] (verified: e2e.py file listing).
- **`track_stats=True` attaches results that `run()` then drops** — it puts `detailed_results` (a `DspyGEPAResult`) on the program returned by `compile`. `train()` returns that program. `run()` returns only a `RunResult`, and `save()` does not persist `detailed_results`. `gepa.py:664-668`; `runner.py:368-413` [trap] (verified: e2e saved keys) → here: pairs.py (keep the returned program and write its stats).
- **`compile` deep-copies the student, but a cached run loads in place** — `DspyAdapter.build_program` does `self.student.deepcopy()` and sets `pred.signature = pred.signature.with_instructions(candidate[name])`. After a fresh `run()` the caller's module is unchanged. A cached `run()` loads into the caller's module (`runner.py:385`). Same call, opposite side effects. `dspy/teleprompt/gepa/gepa_utils.py:184-199` [trap] (verified: e2e.py, "instructions unchanged after run(): True", then "program2 loaded in place: True").
- **A candidate is instructions only** — `seed_candidate = {name: pred.signature.instructions for name, pred in instruction_predictors}` (plus `dspy.Flex` code). GEPA in 3.3.1 evolves per-predictor instruction text; it does not touch demos or field descriptions. `gepa.py:628` [api] (read, not run) → here: job 4.
- **Metric exceptions in GEPA become silent zeros** — evaluation runs `Evaluate(..., failure_score=self.failure_score, max_errors=len(batch) * 100)` or `bootstrap_trace_data(raise_on_error=False, failure_score=...)` (`gepa_utils.py:240-266`). Exceptions while building the reflective dataset, which calls the metric with `pred_name`, are logged and swallowed (`gepa/proposer/reflective_mutation/reflective_mutation.py:446-450`, gepa 0.1.4). With a metric that raises on every example, `train()` returned normally after spending the whole budget: 390 student calls across `run_baseline` and `train`, 0 reflection calls, and „Reflective mutation did not propose a new candidate" every iteration. It returned the seed program. [trap] (verified: broken_metric.py) → here: pairs.py (run the metric on sample rows first, count exceptions, fail the run if any; P15, P23).
- **What the metric receives during reflection** — GEPA calls `metric(module_inputs, module_outputs, captured_trace, pred_name, trace_for_pred)` with `trace_for_pred = [(predictor, predictor_inputs, predictor_output)]`, a one-element list. If that score differs from the module-level score, GEPA warns once and uses the module-level score. DSPy: „GEPA (currently) expects the metric to return the same module-level score when called with and without the pred_name." `gepa.py:317-319,592-599`; `gepa_utils.py:424-430` [api] (read, not run).
- **A float-returning metric gets generic feedback** — a non-`Prediction` return is wrapped as `dict(score=o, feedback=f"This trajectory got a score of {o}.")`, so the reflection LM learns nothing from it. A `Prediction` with `feedback=None` gets the same text. `gepa.py:600-605` [api] (read, not run).
- **The default proposer sends a raw prompt and reads a fenced block** — the prompt begins „I provided an assistant with the following instructions to perform a task for me: ``` <current instruction> ``` The following are examples of different task inputs provided to the assistant along with the assistant's response for each of them, and so…". The new instruction is taken from between the first and last fence in the response. `gepa_utils.py:170-180`; `gepa/strategies/instruction_proposal.py:125-153` [api] (verified: e2e.py captured the prompt) → here: lm_fixture.py (a reflection fixture must answer inside ``` fences).
- **Nothing gates `promote()`** — `run()` is datasets → train → compare → promote, unconditionally. `promote()` is `optimized_module.save(dest)` after `mkdir`. A regression, or `improvement=0.0`, is saved the same way. `runner.py:388-424` [trap] (verified: e2e.py promoted with `improvement=0.0`) → here: baseline.py (compare against the floor, and a veto row).
- **Load-or-train keyed by name** — `run(force=False)` loads `<artifact_dir>/<name>/optimized_<name>.json` if it exists. The name falls back to `module.__class__.__name__`, then `"UnknownTask"`. The key ignores rows, metric and module structure, so a changed task under an old name loads stale state. Field resolution still runs first, so a cached load needs rows. `runner.py:140-143,377-386` [pattern] (verified: e2e.py RUN2 `loaded_from=...`).

## MET

- **The metric contract the repo uses** — `def metric(example, pred, trace=None, pred_name=None, pred_trace=None) -> dspy.Prediction(score=float, feedback=str)`. The defaults are needed because `dspy.Evaluate` calls `metric(example, pred)` while GEPA calls it with five arguments. `metric_builder.py:12-13,61`; `docs/medium.md:75` [api] (verified: e2e.py's metric file) → here: pairs.py (`score_one` adapter).
- **The metric-writing prompt's rules, verbatim** (from the `MetricSpecGenerator` docstring, which is its instruction):
  1. „ALWAYS return dspy.Prediction(score=..., feedback=...). … NEVER return a dict or bare float." (`metric_builder.py:16-19`)
  2. „Use MULTI-AXIS scoring. … Combine with EXPLICIT WEIGHTS declared as module-level constants." (`:20-22`)
  3. „Feedback must TEACH the optimizer: explain WHY the prediction failed and WHAT GOOD LOOKS LIKE. … Target 2-5 lines of actionable, specific critique per issue." (`:23-25`)
  4. „When pred_name is provided, write PER-PREDICTOR feedback … Include the predictor name in the feedback text." (`:26-28`)
  5. „Use exact string matching ONLY for enumerated/categorical fields." (`:29`)
  6. Prefer semantic similarity for free text (`:30-32`).
  7. Use an LLM judge only when deterministic checks are impossible, always with a fallback on judge failure (`:33-37`).
  8. „Include all imports at the top of the generated code" (`:38-39`).

  [claim] (the prompt asserts these as rules; see the next items).
- **A bare float does not break GEPA** — rule 1 says it does. A float works in both `Evaluate` and GEPA and only costs the feedback text (see the OPT item on float-returning metrics). A dict does break both. `metric_builder.py:15-19` [trap] (verified: sum check; GEPA source read).
- **Few-shot Example 1 is the only one that runs** — Example 1 (classification: weights 0.6/0.4, `_normalize`, `_safe_get`, per-predictor feedback) passes the validator and scores 1.00, „Correct on all axes.". Examples 2 and 3 pass the validator but raise `AttributeError: 'str' object has no attribute 'answer'` on any non-empty answer, because they call `answer_exact_match(str, str)` outside any try block. Example 3 also reconfigures the global LM on load. So the model is taught two broken metrics out of three. `metric_builder.py:41-226` [trap] (verified: V).
- **Example 1 pays for wrong answers** — `FORMAT_WEIGHT = 0.4` is granted whenever both predicted fields are non-empty, so a completely wrong prediction scores 0.4 and a right one 1.0. The usable range is compressed to [0.4, 1.0]. `metric_builder.py:46-47,89-94` [trap] (read, not run) → here: pairs.py (score the decision only; P27).
- **Example 3's reasoning check can never pass under GEPA** — it adds `REASONING_WEIGHT` only `if trace and pred_trace` and `len(pred_trace) >= 2`, else it appends „Reasoning issue: provide at least 2 explicit reasoning steps.". GEPA passes a one-element `pred_trace`, so the reflection-time score is always 0.4 lower than the evaluation-time score (with `trace=None` the weight is granted for free). That is a guaranteed `warn_on_score_mismatch` and misleading feedback. `metric_builder.py:211-221`; `gepa.py:592` [trap] (read, not run).
- **Rule 7 contradicts Example 3** — the rule says „use a cheaper model (e.g., gpt-4o-mini)" (`metric_builder.py:37`). The example uses `openrouter/openai/gpt-oss-120b` and configures it globally (`:151-153`). [trap] (read, not run).
- **Rule 6 names things that are not semantic, or do not exist** — „semantic similarity (e.g., dspy.evaluate.answer_exact_match, fuzzy_match, or embedding cosine similarity)". `answer_exact_match` is exact match, and `fuzzy_match` does not exist in `dspy.evaluate`. `metric_builder.py:30-32` [trap] (verified: dir(dspy.evaluate)).
- **The metric source guard cannot fail on the common defects** — `_validate_metric_source` rejects only `return {…}` dict literals (`ast.Dict`) and sources that lack the substring `"dspy.Prediction"`/`"Prediction("` anywhere. It never runs the metric. It passes:
  - a bare float with `dspy.Prediction` in a comment;
  - `return dict(score=...)`;
  - a three-argument metric, which GEPA rejects;
  - metrics that raise at runtime (Examples 2 and 3).

  `metric_builder.py:245-271` [trap] (verified: G, V) → here: pairs.py (a guard must execute the metric on sample rows; P23).
- **Fence stripping and parse failure** — `_strip_markdown_fences` drops only a first line and a last line that start with ``` . If prose precedes the fence, the fence survives, `ast.parse` fails, and the result is `ValueError("Generated metric is not valid Python code:\n<first 500 chars>...")`. There is no retry. `metric_builder.py:236-242,303-310` [trap] (verified: G).
- **What the metric writer sees** — `MetricSpecGenerator` has inputs `input_keys: list[str]`, `output_keys: list[str]`, `sample_rows_json: str`, `module_repr: str` and output `metric_source: str`. `sample_rows_json = json.dumps(sample_rows[:5], indent=2, default=str)` is the first five rows of the whole dataset before splitting, so it can include test rows; `module_repr=repr(module)`. `metric_builder.py:229-233,296-301` [api] (read, not run).
- **Loading a metric file** — `importlib.util.spec_from_file_location("auto_gepa_metric", path)` then `exec_module`. It raises `ValueError("Metric file must define a top-level metric(...) function")` if there is no `metric`. The module is not registered in `sys.modules`, and every `load_metric()` call re-executes the file (both `run_baseline` and `train` call it). `artifacts.py:8-19`; `runner.py:187-192,305,331` [api] (verified: Y).
- **The documented example metric crashes when GEPA calls it** — `docs/medium.md`'s "Example generated metric" returns a bare float when `pred_name is None` and `dspy.Prediction(...)` otherwise, but imports `re` instead of `dspy`. It passes the validator; `metric(ex, pred)` returns 1.0; `metric(..., pred_name='predict')` raises `NameError: name 'dspy' is not defined`. `docs/medium.md:72-95` [trap] (verified: H).
- **AutoData's row judge (not a GEPA metric)** — `_JudgeSignature(row_data, rubric, task_description="") -> scores_json: str, feedback: str`, default rubric `["correctness", "relevance", "coherence"]`. The row score is the mean of the per-dimension floats, capped with `min(avg, 1.0)`; nothing checks the lower bound or the range. A call failure gives `JudgeResult(0.0, "LLM judge call failed")`; a parse failure gives `0.0, "Failed to parse judge output"`. "Could not score" is thus indistinguishable from "scored 0". `quality.py:136-226` [trap] (repo tests `tests/test_quality.py:81-126` pass) → here: P15.
- **`batch_score`'s docstring claims a fallback the code lacks** — it makes one call for many rows, returning a `results_json` array aligned by position („in the SAME ORDER"). Missing or invalid entries become 0.0, „Failed to parse judge entry". The docstring says „Falls back to individual scoring for rows that fail to parse", but the code never calls `score()` for them. `quality.py:228-293` [trap] (read, not run).
- **A real gain was reported as zero** — `compare()` scores baseline and optimized on the same test split with the same metric and threads, and reports `improvement = optimized - baseline` in percentage points. With the default split on 10 rows the test split is one row. In e2e.py GEPA found a better instruction (valset 0.5 → 1.0), yet `compare()` reported `baseline=100.0, optimized=100.0, improvement=0.0`. The single test row („Can someone clean conference room B next week?", low/neutral) was already right before optimization. `runner.py:347-366` [number] (verified: e2e.py, e2e_force.py) → here: pairs.py (report per fold with n, never a single-row delta; P27).
- **`perfect_score=1.0` is assumed** — the prompt's examples cap with `min(score, 1.0)` (`metric_builder.py:99,143,226`), matching GEPA's `perfect_score=1.0`. A metric on another scale silently disables `skip_perfect_score`. [api] (read, not run).

## DATA

- **Accepted row sources** — `_to_dicts` accepts:
  - a `str`/`Path` by extension: `.jsonl` (a line per row), `.json` (an array or `{"rows": [...]}`), `.csv`, `.parquet`/`.pq` via pandas;
  - a `list`, returned as the same object;
  - objects with `.to_dicts()` (polars), `.collect()` (LazyFrame), `.to_dict(orient="records")` (pandas) or `.to_pandas()`.

  Anything else raises a `TypeError` listing the accepted types; a missing file raises `FileNotFoundError`; an unknown extension raises `ValueError`. `data.py:109-191` [api] (verified: repo tests pass).
- **Field inference** — with no field arguments, all signature fields must be a subset of the row keys; extra columns are allowed and later dropped. So `docs/basic.md:54` „exact match required" is wrong. The error text: „Row columns do not match module signature fields. Missing from rows: [...]. Extra in rows: [...]. Pass input_fields/output_fields to map row columns to signature fields, or ensure row columns match exactly." `data.py:290-305` [pattern] (verified: tests, C).
- **Mapping direction** — a dict is `{row_column: signature_field}`; a list gives exact names. An omitted side is inferred from the signature only, never from the rows (contrary to `README.md:375`). Explicit lists are never checked against the rows, so a mismatch surfaces later as a bare `KeyError('msg')` from `to_examples`. An empty side raises `ValueError("input_fields and output_fields must be non-empty")`. `data.py:307-327,352` [api] (verified: final check).
- **`reasoning` is not stripped in custom modules** — a custom `dspy.Module` holding one `ChainOfThought` yields outputs `['reasoning', 'urgency', 'sentiment']`, and `resolve_fields` raises „Missing from rows: ['reasoning']". Two CoTs keep `reasoning` too: `isinstance(predictor, dspy.ChainOfThought)` at `data.py:239` tests `Predict` objects and is never true. Only a bare `dspy.ChainOfThought` is stripped (`data.py:267-272`). The v0.1.8 multi-predictor feature (`CHANGELOG.md:169`) inherits the bug. [trap] (verified: C).
- **Split** — `random.Random(seed).shuffle(items)`, then `int()` truncation for train and val; the test split is the remainder. So the third proportion is ignored: `(0.5, 0.2, 0.1)` on 10 rows gives 5/2/3. A 2-tuple gives `(train, [], rest)`. Verified sizes with the default `(0.7, 0.2, 0.1)`: n=1 → 0/0/1; n=2 → 1/0/1; n=4 → 2/0/2; n=5 → 3/1/1; n=10 → 7/2/1. `data.py:357-378` [number] (verified: A) → here: pairs.py (stratified folds).
- **Split validation is incomplete** — the config checks only `sum(split) <= 1.0`. A 1-tuple or 4-tuple passes the config and fails later with `ValueError: not enough values to unpack` / `too many values to unpack`. n=1 gives `train=[]`, which trips GEPA's `AssertionError "Trainset must be provided and non-empty"` (`gepa.py:544`). `(0.7, 0.3, 0.0)` on 10 rows gives an empty test split, then `ZeroDivisionError` in `run_baseline`. `config.py:28-29` [trap] (verified: A, R).
- **The validation set can be the test set** — `Datasets(train=train, val=val or test, test=test)`. With any 2-tuple split, and with n ≤ 4 on the default split, GEPA's Pareto valset is the same list object as the test set `compare()` reports on (`ds.val is ds.test` → `True`). The README quick start uses 2 rows, giving train 1 and val = test = 1. `runner.py:242-246`; `README.md:89-92` [trap] (verified: B) → here: pairs.py (never select on the report set).
- **`run()` applies the mapping twice** — `run()` maps the rows, then calls `datasets(rows=mapped)`, which maps them again. For plain renames that is harmless; for a swap it undoes itself. `datasets()` called directly gave `question=QUESTION-7`; inside `run()` the training example had `question=ANSWER-7`. `runner.py:377-394`; `data.py:330-342` [trap] (verified: X).
- **`AutoDataConfig` fields and defaults** — `n=100, seed=42, max_retries=8, num_threads=16, chunk_size=10, max_inflight_requests=4, diversity_threshold=0.3, judge_enabled=True, validators_enabled=True, diversity_enabled=True, rejection_sampling_enabled=True, data_lm=None, judge_lm=None, balance_outputs=True, balance_tolerance=0.15, oversample_factor=2.0, generation_mode="split", diversity_categories="", seed_examples=None, output_path=None, force=False`. Validation: n > 0, max_retries > 0, chunk_size > 0, max_inflight_requests > 0 when set, diversity_threshold in [0, 1], and the generation mode. `config.py:59-93` [api] (verified: repo tests).
- **Six config flags do nothing** — `validators_enabled`, `diversity_enabled`, `rejection_sampling_enabled`, `balance_tolerance` and `oversample_factor` are read nowhere in `src/`; `diversity_threshold` is only range-checked. `judge_enabled`, `balance_outputs`, `max_inflight_requests` (output path only), `chunk_size` and `diversity_categories` are read. [trap] (verified: grep of `src/`).
- **Three generation paths** —
  - *Targeted*: taken when `balance_outputs` is on and some output field has allowed values. For each label combination it generates `ceil(n/len(combos))` inputs meant to produce that label. The label is the requested combination: no output generation, no judge, no dedup.
  - *Split*: generate inputs, then outputs (a typed batch of up to 20, then a single-row fallback), then judge scores.
  - *Signature*: full rows in one request, then judge scores.

  `generator.py:1513-1573` [pattern] (verified: N, O).
- **Allowed values come only from the seed rows** — they are inferred for output fields only, lowercased, and used when 2 ≤ distinct ≤ 10. A `Literal[...]` annotation is ignored: `python_type` falls back to `str` because a `Literal` is not a `type`, as does `list[str]`. No seeds means no enums and no balancing. A label absent from the seeds is never targeted. `_build_output_model` turns the lowercased values into `Literal['high','low']` and drops `reasoning`. `data.py:43-57,86,90`; `generator.py:89-114` [trap] (verified: D).
- **"Balanced" output is not balanced when n is not a multiple of the combinations** — n=10 with 9 combinations gives `per_combo=2`, 18 rows cut to 10: 5 combinations get 2 rows and 4 get none. The docstring says `n // len(output_combos)` and „perfectly balanced output distribution"; the code uses `ceil` and truncates in combination order. `generator.py:855-869,996-999` [trap] (verified: O).
- **Targeted mode keeps duplicates** — with a mocked model returning the same text, 10 rows came back with 1 distinct message. The fingerprint dedup exists only in the other two paths. `generator.py:847-999` [trap] (verified: O).
- **The judge never rejects a row** — split mode stores scores only (`generator.py:1193-1227`); signature mode does `all_scores.append(score or 0.0)` with no threshold (`generator.py:1399-1403`). `RejectionSampler(judge_threshold=0.5)` (`quality.py:392-454`) is never instantiated. Rows with judge score 0.0 were accepted. `quality_scores` is only reported. [trap] (verified: N).
- **Enums are enforced in one mode and not the other** — split-mode outputs are validated with `include_enum=False` (`generator.py:1016,1071`); the repo's own test asserts that the out-of-set label „critical" is accepted (`tests/test_generator.py:1004-1052`). Signature mode enforces enums (`generator.py:1276`). [trap] (verified: repo test passes).
- **Output-generation sizing** — batch size is `min(24, max(10, chunk_size*2))`, so 20 by default. Batches per round are `min(max_inflight_requests or num_threads, ceil(pending/batch))`, so 4 by default. Failed indices are retried one row at a time with the untyped `_OutputGenerationSignature`. Judge batches are 5 rows (the comment says „10 per LLM call") in a `ThreadPoolExecutor(max_workers=num_threads)`. `generator.py:1018-1021,1095-1121,1159-1216` [number] (read, not run).
- **Input generation ignores `max_inflight_requests` and sends identical requests** — up to 40 rows per request; per round, `min(num_threads, ceil(remaining/40))` requests, and every request in a round carries identical inputs (the same recent window, themes and `n_to_generate`). With n=200 that was 5 identical requests of 40 each. `max_inflight_requests=2` was not applied: the call size was 5. Variety within a round depends on sampling; exact duplicates are dropped by fingerprint. `generator.py:746-780` [trap] (verified: M).
- **When generation stops, and what happens on a shortfall** — it stops after `max(max_retries*5, n)` consecutive rounds with 0 accepted rows; in targeted mode, per combination, after `max(max_retries*5, per_combo)`. A shortfall is not an error: `GenerationFailed` is exported (`__init__.py:19,35`; `runner.py:65-75`) but never raised. A run producing 0 of 3 rows returned `GenerationResult(n_produced=0, n_failed=3)`. `generator.py:746,751-753,842-843,896,906` [trap] (verified: L).
- **Diversity prompting** — each request carries the last 20 rows as JSON (`recent_inputs_json`/`recent_rows_json`) and `covered_themes`: every distinct lowercased string value of every field seen so far, joined as `field: v1, v2; …`. For free-text fields that is the full text of every earlier input, and it grows without bound. Signature mode adds `diversity_categories`. The prompts demand „Every generated input MUST be completely unique. Do NOT repeat, closely paraphrase, or slightly modify any existing input." `generator.py:297-344,697-717,819-830` [pattern] (read, not run).
- **The output prompts trade accuracy for balance** — „When the input could reasonably fit multiple allowed values, prefer the less common one to maintain variety in the dataset." `generator.py:354-355,522-523` [trap] (read, not run).
- **Dedup fingerprint** — per field: `sanitize_string` then lowercase for strings, `json.dumps(sort_keys=True)` for dicts and lists, `str` for scalars; keys sorted and joined as `k=v|…`. Seed rows are in the fingerprint set, so a seed is never re-emitted. `generator.py:570-585,672-681,697-698` [pattern] (read, not run).
- **`sanitize_string` deletes whole scripts** — it strips the emoji regex, NFC-normalizes, and collapses whitespace including NBSP, ZWSP, NNBSP and U+2060. The regex range `\U000024c2-\U0001f251` („enclosed characters") deletes CJK, Hangul, fullwidth Latin, box drawing, ■, ✓, ⟶, ligatures and math alphanumerics: `'中文テスト한국어'` → `''`, `'ＡＢＣ'` → `''`, `'ﬁle'` → `'le'`, `'𝐀𝐁'` → `''`. German survives: `'Kohärenz „Guardian“ ß'` is unchanged, and so are `→ ≤ ₀`. It is applied to every generated string, and `no_emoji_validator` rejects such rows. `quality.py:45-78`; `generator.py:254-255,1067-1068` [trap] (verified: E).
- **ChainOfThought modules generate with an empty task description** — `generate()` computes `self.description or getattr(getattr(self.module, "signature", None), "__doc__", "")`. A ChainOfThought has no `.signature`, so on Python 3.12 the description is `''`; the signature's „Classify support tickets." never reaches the prompts. On Python 3.13, `None.__doc__` is `'The type of the None singleton.'`, which would become the description. `__init__` checks the inner predictor's docstring; `generate()` does not. This affects `examples/data_split.py` and `examples/auto_combined.py`. `generator.py:1505-1509` [trap] (verified: L; `None.__doc__` on 3.12 and 3.13).
- **Output writer** — `.jsonl` and `.json` are both written as JSONL, so a `.json` output cannot be read back by `_to_dicts` (`JSONDecodeError: Extra data: line 2 column 1`). JSONL appends with flush + `os.fsync` per write call; CSV appends without fsync; Parquet rewrites the whole file on every write; `flush()` and `close()` are no-ops. `generator.py:117-233` [trap] (verified: F).
- **Resume miscounts** — if the file has at least n rows and `force` is off, `generate()` returns the first n without any model call (`tests/test_generator.py:470-498`). With fewer rows, new rows are appended after the old ones and the counts come from the file: `n_requested=5, n_produced=8, n_failed=-3`, 5 rows returned, 8 in the file. The targeted path truncates the file instead (`generator.py:1547-1548`). `generator.py:1487-1503,1575-1589` [trap] (verified: P).
- **`AutoGEPA.generate()` picks the wrong LMs** — the data LM is `data_lm` or the constructor's `data_lm` or `metric_lm` (default `openrouter/openai/gpt-oss-120b`), never `dspy.settings.lm`. The constructor's `judge_lm` is never passed to `AutoData`, so the judge falls back to the data LM. The `schema=` argument is stored in `_schema_fields` and never read. `runner.py:426-473`; `generator.py:622-625` [trap] (verified: W, where the global LM was `openai/my-global` and generation used gpt-oss-120b with `config.judge_lm=None`).
- **Documented `generate(n=...)` raises** — the signature is `AutoData.generate(self, *, force=None, output_path=None)`, so `gen.generate(n=50)` raises `TypeError: AutoData.generate() got an unexpected keyword argument 'n'`. Used in `docs/generator.md:23,31,39` and `README.md:280`. [trap] (verified: K).
- **`_extract_json`** — four strategies, then passthrough:
  1. raw `json.loads`;
  2. the first ```json fenced block;
  3. the outermost `{…}`, then the outermost `[…]`;
  4. `ast.literal_eval` for Python literals, re-dumped as JSON.

  Otherwise the text comes back unchanged and the caller's `json.loads` fails. `generator.py:33-78` [recipe] (verified: Q).
- **`generate()` reseeds the global RNG** — `random.seed(self.config.seed)` mutates the process-global RNG, which nothing in the generator uses. `generator.py:1473` [trap] (read, not run).
- **CHANGELOG speed numbers are not reproducible** — an automated tuning loop (PR #4) logged, among others:
  - „Split mode 1.9s (54 rows/s)"
  - „New best — 3.45s, split 1.8s, 39x speedup"
  - „Final — 5s total, split 2.2s, 27x speedup with balanced accurate output"
  - „Split 3s, signature 11.3s (API variance)"

  The request row cap went 10→12→14→16→18→20→22→30→40, the output batch 10→16→20→24, and oversampling 4x→3x→2.5x→2.0x; there was also „Revert async judge (deadlock)". The baseline was „mocked DSPy workloads … simulated rate-limit pressure", and the harness (`.auto/`) was deleted, so none of this reproduces at 80a5402. `CHANGELOG.md:69,73,104-157` [claim].
- **CHANGELOG contradicts the code** — „Batch judge scoring (10 per call via ThreadPool)" (`CHANGELOG.md:139`), but the code has `judge_batch_size = 5` (`generator.py:1195`). „Increase max_inflight for output gen from 4 to num_threads (16)" (`CHANGELOG.md:140`), but the default is `max_inflight_requests=4` and output generation uses it (`config.py:64`; `generator.py:1018-1020`). Oversampling and „normalized deficit balancing" (`CHANGELOG.md:133-136`) survive only as the unused `_subsample_balanced` and a dead `oversample_factor`. [trap] (verified: grep).

## RLM

- **`dspy.RLM` is the default metric writer** — `AutoGEPAConfig` sets `metric_generator_module = dspy.RLM` and `metric_generator_signature = MetricSpecGenerator`. `generate_metric_file` builds `dspy.RLM(signature, verbose=metric_generator_verbose)` (default `True`); any other module class is built as `module(signature)`. It then calls `generator.set_lm(metric_lm)`. RLM replaced ChainOfThought in v0.1.2 (`CHANGELOG.md:319`). `config.py:36-39`; `metric_builder.py:286-294` [api] (verified: the guarded run of the unmocked test reached `rlm.py:728 forward`).
- **`set_lm` does not reach RLM's `sub_lm`** — `llm_query` inside the REPL uses `self.sub_lm`, then `dspy.settings.lm`, and raises `dspy.LMNotConfiguredError("No LM configured. Use dspy.configure(lm=...) or pass sub_lm to RLM.")` if neither is set. `set_lm(metric_lm)` sets only the RLM's predictors (action and extract), so sub-queries run on whatever global LM is configured. `dspy/predict/rlm.py:260-281` [api] (read, not run) → here: rlm_ingest.py (pass `sub_lm` explicitly).
- **RLM parameters were renamed between versions** — 3.3.1: `RLM(signature, max_iters=20, max_llm_calls=50, max_output_chars=10000, verbose=False, tools=None, sub_lm=None, interpreter_factory=PythonInterpreter)`. 3.2.1: `max_iterations=20, …, interpreter=None`. 3.1.0 has no `dspy.RLM`. The repo passes only `verbose`, so it survives the rename. [api] (verified: `inspect.signature` on 3.3.1, 3.2.1, 3.1.0) → here: check_dspy_surface.py, rlm_ingest.py.
- **RLM needs Deno** — the default interpreter runs Deno/Pyodide/WASM. `_find_deno_executable()` tries the `deno` pip package, then `PATH`. `deno` is not a dependency of dspy-auto-gepa. The target's `.venv-dspy` has `deno` 2.9.7, which is why the 2026-09-23 unmocked test ran RLM to completion there. `dspy/primitives/python_interpreter.py:84-94` [api] (verified: my venv had none until I installed it).
- **What happens at `max_iters`** — RLM logs „RLM reached max iterations, using extract to get final output" and fills the outputs from an extract predictor over the REPL history. The live test on 2026-09-23 hit this, per the old report's §4. `dspy/predict/rlm.py:543-561,735-736` [claim] (observed by the earlier reader, not re-run).

## AGENT

- **Signature mode does not generate ReAct or RLM traces for real modules** — `examples/data_signature.py` passes `dspy.ReAct(ReActSignature, tools=[])`. Its `.signature` is the user signature, so AutoData generates only `question`/`answer` rows. The claim that signature mode suits „ReAct reasoning traces or RLM explorations" (`config.py:53-56`; `README.md:210`) holds only for a hand-written signature with `thought/action/observation` fields, as in `tests/test_generator.py:1614-1641`. `infer_fields_from_module(dspy.ReAct(...))` gives `(['question'], ['answer'])`; `dspy.RLM(...)` gives `(['context', 'query'], ['answer'])`. [trap] (verified: C).

## PROD

- **Default models are on OpenRouter** — `metric_lm = dspy.LM("openrouter/openai/gpt-oss-120b")` and `reflection_lm = dspy.LM("openrouter/moonshotai/kimi-k2.5")` are built in `AutoGEPAConfig.__post_init__` (no network at construction); using either needs `OPENROUTER_API_KEY`. `metric=Path` avoids the metric LM, but `train()` still uses the reflection default unless `reflection_lm=` is passed, and `AutoGEPA.generate()` defaults to the metric LM. `config.py:32-35`; `runner.py:333,453` [trap] (verified: U, W) → here: lmrun.py (a real LM refused without `approval=`).
- **The library never turns the LM cache off** — it never sets `cache`, so its LMs use `cache=True`. Only the examples pass `cache=False` (`examples/basic.py:10,13`; `examples/data_split.py:13`; `examples/data_signature.py:13`; `examples/auto_combined.py:17,21`). The README and docs build LMs without it (`README.md:77-78,218`; `docs/basic.md:20-21`; `docs/medium.md:21-22`; `docs/generator.md:11`). "Cached" in the docs means the saved program, not the LM cache (`docs/basic.md:61-68`). [trap] (verified: U; grep) → here: lmrun.py (P18).
- **Corpus text goes to the LLMs** — SECURITY.md: „Training data (`rows`) is sent to LLMs during both metric generation and GEPA optimization reflection steps." Concretely: the first five rows go to the metric writer (`metric_builder.py:299`), and minibatch inputs, outputs and feedback go to the reflection LM (the reflection prompt captured in e2e.py). `SECURITY.md:19` [claim] → here: the target's approval rule for corpus text.
- **Generated code runs on load** — SECURITY.md: „…dynamically imports and executes them via `importlib`. Generated code is validated with `ast.parse()` for syntax, but semantic correctness and safety are not guaranteed." Module-level side effects run on every `load_metric()`; `dspy.configure` in Example 3 was verified. `SECURITY.md:18` [claim] (verified: V for the side effect).
- **The constructor creates a directory** — `AutoGEPA(...)` creates `artifact_dir` at construction (default `.auto_gepa`, relative to the working directory). Repo tests that construct it without `artifact_dir` create `.auto_gepa/` wherever pytest runs (`tests/test_auto_gepa.py:60-79,509-521`). `runner.py:121` [trap] (read, not run).
- **Artifact layout, and scores are never persisted** — `.auto_gepa/<name>/metric.py`, `.auto_gepa/<name>/gepa_logs/…`, `.auto_gepa/<name>/optimized_<name>.json`, `.auto_gepa/<name>/generated/rows.jsonl`. `save_results()`, which writes `results.json`, is exported but never called. `runner.py:125-129,223,325-329,380-382`; `generator.py:1477-1481`; `artifacts.py:22-44` [api] (verified: e2e listing; grep) → here: baseline.py (append the scores; don't rely on the wrapper).
- **Output noise** — `run_baseline` uses `display_progress=True, display_table=True`, which prints a pandas table per evaluation. RLM runs with `verbose=True` by default. AutoData prints tqdm bars and `tqdm.write` summaries. `runner.py:303-309` [api] (verified: e2e log shows the table).
- **Concurrency** — `num_threads=16` is shared by `Evaluate` and GEPA; AutoData uses 16 threads and 4 in-flight output batches. `runner.py:306,334`; `config.py:62-64` [number] (read, not run).
- **CI never runs the tests** — the only workflow is `publish.yml`. It installs Python 3.10 (`uv python install 3.10`) although `requires-python >= 3.12`, builds, runs `tests/test_smoke.py` against the wheel and the sdist with `uv run --isolated --no-project --with dist/*.whl tests/test_smoke.py`, and publishes. `.github/workflows/publish.yml:20-21,32-39` [trap] (read, not run).
- **The Python floor is declared, not needed** — all `.py` files parse under 3.11. The offline suite on Python 3.11 + DSPy 3.3.1 gave 130 passed and 1 failed; the failure is `test_smoke`, because an uninstalled source tree reports `__version__ = "unknown"` (`__init__.py:21-26`). [number] (verified: `venvs/ag311`) → here: `.venv-dspy` is 3.11; ideas port, the package cannot be pip-installed there.
- **The DSPy floor is real, and the README is wrong** — `pyproject`'s `>=3.2.1` holds: on DSPy 3.1.0, `import dspy_auto_gepa` raises `AttributeError: module 'dspy' has no attribute 'RLM'`, because the default argument `metric_generator_module: Any = dspy.RLM` is evaluated at import. `README.md:46`'s „Requires DSPy 3.1+" is false. `metric_builder.py:283` [trap] (verified: `uv run --with dspy==3.1.0`).

## TEST

- **The unmocked live-call test is still unmocked at 80a5402** — `test_partial_explicit_fields_infer_rest` calls `auto.datasets()` with no `metric=` and no patch of `generate_metric_file`. That reaches a real `dspy.RLM` with `openrouter/openai/gpt-oss-120b`. Under the offline guard it attempted `litellm.completion(model='openrouter/openai/gpt-oss-120b')` via `runner.py:228` → `metric_builder.py:296` → `dspy/predict/rlm.py:728`, raising `LMUnexpectedError`. Its siblings patch `dspy_auto_gepa.runner.generate_metric_file` (`tests/test_auto_gepa.py:479,501`). `tests/test_auto_gepa.py:538-560` [trap] (verified: pytest with the guard and keys unset; 1 attempt recorded, blocked) → here: lm_fixture.py `offline()` (exactly this guard).
- **Suite composition** — 132 tests: `test_auto_gepa.py` 35, `test_generator.py` 69, `test_quality.py` 27, `test_smoke.py` 1. Offline run on Python 3.12.3 / DSPy 3.3.1: 131 passed and 1 deselected in 4.87 s, with 0 LM attempts. [number] (verified: pytest).
- **`poe test-e2e` cannot run** — `test-e2e = "uv run pytest tests/ -v --run-e2e"`, but no `conftest.py` defines `--run-e2e`, so pytest exits with „error: unrecognized arguments: --run-e2e". The live test is not behind any flag. `pyproject.toml:71` [trap] (verified: pytest).
- **Mocking patterns the repo uses** —
  - `patch.object(module, "load")`, then `patch.object(auto, "datasets" | "train" | "compare" | "promote")` to test `run()` (`tests/test_auto_gepa.py:117-171`);
  - `patch("dspy_auto_gepa.runner.generate_metric_file")` (`:384-388`);
  - `patch("dspy_auto_gepa.generator.dspy.Predict")` returning a `MagicMock` whose return value is a real `dspy.Prediction(generated_inputs='[...]')` (`tests/test_generator.py:301-329`);
  - `patch("dspy_auto_gepa.quality.dspy.Predict")` for the judge (`tests/test_quality.py:81-126`).

  [pattern] (verified: suite passes) → here: lm_fixture.py.
- **The sync `Parallel` mock hides the real return shape** — `SyncParallel` returns a list; the real `Parallel(return_failed_examples=True)` returns a 3-tuple. The real tuple is exercised only by tests that patch `Predict` but not `Parallel` (`tests/test_generator.py:359-418,500-562,1004-1052`). Only `test_generate_force_overwrites` (`:500-536`) sends it through `_generate_inputs`'s accidental flattening. `tests/test_generator.py:62-86` [trap] (verified: real `Parallel` shape).
- **A test that cannot fail for its stated reason** — `test_generate_inputs_caps_inflight_requests` asserts a maximum call size of 2 with `max_inflight_requests=2`. But the helper config sets `num_threads=1` (`tests/test_generator.py:51`), and `_generate_inputs` never reads `max_inflight_requests`. With `num_threads=16` the call size was 5. `tests/test_generator.py:589-634` [trap] (verified: M).
- **Tests keep dead code looking alive** — `_subsample_balanced` (5 tests, `tests/test_generator.py:1188-1382`), `RejectionSampler` (5 tests, `tests/test_quality.py:134-175`) and `DiversityChecker` (4 tests, `tests/test_quality.py:18-42`) all pass, but the pipeline never calls them. [trap] (verified: grep of `src/`).
- **Three-argument metric files in the tests** — `def metric(example, pred, trace=None): return 1.0` appears at `tests/test_auto_gepa.py:102,134,215,233,393`. No test reaches `dspy.GEPA`; `train()` with such a file raises `TypeError` (see the five-argument check under OPT). [trap] (verified: I).
- **Smoke test** — it runs `python -c "import dspy_auto_gepa…"` in a subprocess with `timeout=10` and requires `__version__` to match `\d+\.\d+\.\d+`, so it fails for an uninstalled tree. It also checks the public API names. `tests/test_smoke.py:17-89` [pattern] (verified: failed on 3.11 without install, passed with install).
- **A warning filter** — `filterwarnings = ["ignore:.*prefix.*:DeprecationWarning:dspy.*"]` silences DSPy's field-prefix deprecation warnings. `pyproject.toml:55-56` [api] (read, not run).
- **My offline harness (not in the repo), which worked** — the guard makes `litellm.completion/acompletion/text_completion/atext_completion/responses/aresponses` raise and records attempts; it runs with `*_API_KEY` unset, the proxy black-holed, `LITELLM_LOCAL_MODEL_COST_MAP=True` and a scratch `DSPY_CACHEDIR`. A student fixture `dspy.BaseLM` returns ChatAdapter text (`[[ ## reasoning ## ]] … [[ ## completed ## ]]`), and a reflection fixture returns a fenced instruction. Together they ran a complete `dspy.GEPA` (388-call budget, 127 iterations) in about 2 s. `scratchpad/guard/offline_guard.py`; `scratchpad/verify/e2e.py` [recipe] (verified) → here: lm_fixture.py, pairs.py `--dry-run`.

## PAT

- **Generate, review, then run** — `build_metric()` writes `metric.py`, a person reads and edits it, then `run(metric=path)` uses it. `docs/medium.md:45-113`; `examples/basic.py:67-89` (interactive `input()` prompts). But the example's retrain path defeats the review: after `build_metric(force=True)` and a human edit, `run(force=True)` calls `generate_metric_file` again (2 calls in total), and the edit is lost. `runner.py:388-394` [trap] (verified: J) → here: pairs.py (a reviewed metric is a file passed by path, never regenerated).
- **Constructor-or-method arguments** — every pipeline method accepts `rows/module/name/metric` and falls back to constructor state (`_resolve_task`, `_resolve_and_prepare`). `runner.py:131-186` [pattern] (verified: repo tests).
- **Targeted (label-conditioned) generation** — „You are given the DESIRED output values. Generate input data that would naturally and correctly produce those exact output values when classified." The label is then asserted, never checked; the CHANGELOG calls it a „massive speedup" (`CHANGELOG.md:127`). `generator.py:374-428,978` [pattern] (verified: O).
- **Typed batch with a single-row fallback** — up to 20 inputs go into one typed `list[Model]` request; failed or missing indices are retried one row at a time with the untyped `_OutputGenerationSignature`. `generator.py:1101-1191` [pattern] (verified: repo tests).
- **A composable validator chain** — `ValidatorFn = Callable[[dict], tuple[bool, str]]`, with the factories `non_empty_validator(*fields)`, `no_emoji_validator(*fields)` and `enum_validator(field, allowed)` (case-insensitive; non-string values pass). `Validator.validate` collects every failure into `ValidationResult(is_valid, failures)`. `quality.py:85-128,301-320` [pattern] (verified: `tests/test_quality.py`) → here: catalogue (quotes.py-style guards).
- **Multi-axis metric** — weights as module constants, per-predictor feedback that names `pred_name or 'main'`, `min(score, 1.0)`. Example 1, with the format-weight caveat under MET. `metric_builder.py:44-99` [pattern] (verified: V).
- **The rejection-sampler design, never wired** — judge, then validator, then diversity; a row passes only if every enabled component passes, and the score is the judge score or 1.0. The diversity step checks only `existing_texts`, never the candidate row (`tests/test_quality.py:161-167` asserts exactly that). `quality.py:392-454` [trap] (verified: repo tests; grep).
- **Character-trigram Jaccard diversity** — the mean pairwise Jaccard of character 3-gram sets must be below the threshold (strict `<`, default 0.3). It is O(n²): 400 short texts made 79,800 pairs in 0.22 s. `quality.py:328-384` [number] (verified: S).

## SKILL

- **No text-artifact optimization here** — the package only runs `dspy.GEPA` on a `dspy.Module`, which evolves `pred.signature.instructions`. There is no `gepa.optimize_anything` path and no way to optimize a free text such as a SKILL.md `description` unless it is a predictor's instruction. `runner.py:330-343`; `gepa.py:628` [api] (read, not run) → here: job 4 uses `optimize_anything`, not this.
- **The prompt is the signature's docstring** — `MetricSpecGenerator`'s docstring (about 215 lines of rules and three examples) is the instruction the metric writer receives. Passing a different `metric_generator_signature` with the same five fields replaces the prompt; `metric_generator_module` swaps the strategy (RLM gets `verbose=`, others get only the signature). `metric_builder.py:9-233,286-291`; `docs/medium.md:128-150`; `tests/test_auto_gepa.py:430-455` [pattern] (verified: repo test) → here: job 4 (the instruction text is the artifact GEPA evolves).

## TRAP

- **The advanced-usage walkthrough raises at step 4** — `docs/advanced.md` constructs `AutoGEPA(input_fields=…, output_fields=…, metric_lm=…, reflection_lm=…, gepa_auto="medium")` without `module`, then calls `auto.run_baseline(datasets=ds)` and `auto.train(datasets=ds)`. That raises `ValueError: module must be provided either to the constructor or to run_baseline()`. It also uses the private `auto._run_dir`. `docs/advanced.md:31-37,68,75,94`; `runner.py:297-301,319-323` [trap] (verified: K).
- **The README API table describes different return types** — `run_baseline → float` is actually `dict {"score": …}`; `compare → dict` is a `RunResult`; `saved_to`/`loaded_from: Path` are `str`. `run` is described as „datasets → baseline → train → compare → promote", but no baseline runs before `train()`. `docs/basic.md:53-59` repeats that order. `README.md:348-363`; `runner.py:31-44,291-311,347-413` [trap] (read, not run).
- **The contributing guide describes a project that does not exist** — `poe dev` is not defined, `tests/test_runner.py` does not exist, `pytest-asyncio` is not a dependency, and the project structure omits `generator.py` and `quality.py`. `.github/contributing.md:105-125,139-142,94,228-241` [trap] (read, not run).
- **Dead or unused code in `src/`** —
  - never called: `_parallel_request_budget` (`generator.py:666-670`), `_generate_one_batch` (`generator.py:719-738`), `_subsample_balanced` (`generator.py:1591-1681`), `RejectionSampler`, `DiversityChecker`, `save_results`;
  - never raised: `GenerationFailed`;
  - never set: `GenerationResult.schema_hash`;
  - never used: `AutoGEPA._judge_lm`, `AutoData._schema_fields`;
  - never filled: `AutoGEPAConfig.input_fields/output_fields` (always `None`; `tests/test_auto_gepa.py:69` asserts it).

  [trap] (verified: grep).
- **`README.md:42` promises reproducible metrics** — „saving them as reproducible `.py` files". Generation runs on a cache-on LM, or on `cache=False` in the examples; with the cache off a regenerated metric differs, and with it on, a stale cached one is returned. [claim].
- **The example seeds contradict each other** — `examples/basic.py:32` labels „Thanks for fixing the VPN, works perfectly now!" as urgency `low`; `examples/data_split.py:41`, `examples/auto_combined.py:48` and `README.md:232` label the same message `medium`. Since allowed values are inferred from seeds (DATA), the seed labels decide which classes AutoData can produce at all. [trap] (read, not run).
- **The metric file is cached by task name** — if `.auto_gepa/<name>/metric.py` exists and `force` is off, `datasets()` reuses it, even when fields or rows changed under the same name. `runner.py:223-226,272-274` [trap] (read, not run).

## 3. Code worth keeping

**a. What auto-gepa passes to GEPA.** `src/dspy_auto_gepa/runner.py:325-345`. Runs on DSPy 3.3.1 (verified: e2e.py, 388-call light run). Add a fresh `log_dir` per run and an explicit budget before reusing it.

```python
        log_dir = (
            str(self._run_dir / "gepa_logs")
            if self._run_dir is not None
            else str(self.config.artifact_dir / "gepa_logs")
        )
        optimizer = dspy.GEPA(
            metric=self.load_metric(),
            auto=self.config.gepa_auto,
            reflection_lm=self.config.reflection_lm,
            num_threads=self.config.num_threads,
            track_stats=True,
            log_dir=log_dir,
        )

        optimized = optimizer.compile(
            task_module,
            trainset=datasets.train,
            valset=datasets.val,
        )

        return optimized
```

**b. DSPy 3.3.1 source: the metric contract as GEPA enforces it and wraps it** (not repo code). `dspy/teleprompt/gepa/gepa.py:416-422` and `600-605`. Verified: a three-argument metric raised this `TypeError`.

```python
        try:
            inspect.signature(metric).bind(None, None, None, None, None)
        except TypeError as e:
            raise TypeError(
                "GEPA metric must accept five arguments: (gold, pred, trace, pred_name, pred_trace). "
                "See https://dspy.ai/api/optimizers/GEPA for details."
            ) from e
# ...
                if hasattr(o, "feedback"):
                    if o["feedback"] is None:
                        o["feedback"] = f"This trajectory got a score of {o['score']}."
                    return o
                else:
                    return dict(score=o, feedback=f"This trajectory got a score of {o}.")
```

**c. The one few-shot metric that runs.** `src/dspy_auto_gepa/metric_builder.py:61-99`, dedented from the docstring. Constants `CORRECTNESS_WEIGHT = 0.6` and `FORMAT_WEIGHT = 0.4` are at `:46-47`; `_normalize` and `_safe_get` at `:49-59`. Runs on 3.3.1 (verified: V, score 1.00). Caveat: the format weight pays 0.4 for any non-empty wrong answer.

```python
def metric(example, pred, trace=None, pred_name=None, pred_trace=None):
    score = 0.0
    feedback_parts = []

    gold_urgency = _normalize(_safe_get(example, "urgency"))
    pred_urgency = _normalize(_safe_get(pred, "urgency"))

    if gold_urgency == pred_urgency:
        score += CORRECTNESS_WEIGHT * 0.5
    else:
        feedback_parts.append(
            f"Predictor '{pred_name or 'main'}': Urgency mismatch. "
            f"Expected '{gold_urgency}', got '{pred_urgency}'. "
            f"Think about how you could have reasoned to get the correct urgency label."
        )

    gold_sentiment = _normalize(_safe_get(example, "sentiment"))
    pred_sentiment = _normalize(_safe_get(pred, "sentiment"))

    if gold_sentiment == pred_sentiment:
        score += CORRECTNESS_WEIGHT * 0.5
    else:
        feedback_parts.append(
            f"Predictor '{pred_name or 'main'}': Sentiment mismatch. "
            f"Expected '{gold_sentiment}', got '{pred_sentiment}'. "
            f"Consider the tone and emotional cues in the input message."
        )

    if pred_urgency and pred_sentiment:
        score += FORMAT_WEIGHT
    else:
        feedback_parts.append(
            "Format issue: predicted fields should not be empty or None."
        )

    if not feedback_parts:
        feedback_parts.append("Correct on all axes.")

    return dspy.Prediction(score=min(score, 1.0), feedback=" ".join(feedback_parts))
```

**d. A guard to teach as a counter-example: it checks shape, never behaviour.** `src/dspy_auto_gepa/metric_builder.py:245-271`. Runs on 3.3.1. It passed a bare-float metric, `dict(...)`, a three-argument metric and two metrics that raise (verified: G, V).

```python
def _validate_metric_source(source: str) -> None:
    tree = ast.parse(source)

    class DictReturnVisitor(ast.NodeVisitor):
        def __init__(self):
            self.dict_returns = []

        def visit_Return(self, node: ast.Return) -> None:
            if isinstance(node.value, ast.Dict):
                self.dict_returns.append(node.lineno)
            self.generic_visit(node)

    visitor = DictReturnVisitor()
    visitor.visit(tree)
    if visitor.dict_returns:
        lines = ", ".join(str(line) for line in visitor.dict_returns)
        raise ValueError(
            f"Generated metric returns a dict on line(s) {lines}. "
            "GEPA metrics must return dspy.Prediction(score=..., feedback=...), "
            "not a dict. Dict returns crash dspy.Evaluate's parallel aggregator."
        )

    if "dspy.Prediction" not in source and "Prediction(" not in source:
        raise ValueError(
            "Generated metric does not appear to return dspy.Prediction. "
            "GEPA metrics must return dspy.Prediction(score=..., feedback=...)."
        )
```

**e. The split, with its truncation and remainder behaviour.** `src/dspy_auto_gepa/data.py:357-378`. Pure Python; verified sizes in DATA. The caller wraps it with `val=val or test` (`runner.py:244`).

```python
def split_examples(
    examples: list[dspy.Example],
    split: tuple[float, ...] = (0.7, 0.2, 0.1),
    seed: int = 42,
) -> tuple[list[dspy.Example], list[dspy.Example], list[dspy.Example]]:
    items = list(examples)
    random.Random(seed).shuffle(items)

    if len(split) == 2:
        train_pct, test_pct = split
        n_train = int(len(items) * train_pct)
        return items[:n_train], [], items[n_train:]

    train_pct, val_pct, test_pct = split
    n_train = int(len(items) * train_pct)
    n_val = int(len(items) * val_pct)

    return (
        items[:n_train],
        items[n_train : n_train + n_val],
        items[n_train + n_val :],
    )
```

**f. A mismatch error that names what is missing.** `src/dspy_auto_gepa/data.py:290-305`. Runs (verified: C, repo test `test_infer_fields_mismatch_raises_error`).

```python
    if input_fields is None and output_fields is None:
        if not all_sig <= row_keys:
            missing = all_sig - row_keys
            extra = row_keys - all_sig
            msg = (
                f"Row columns do not match module signature fields. "
                f"Missing from rows: {sorted(missing)}. "
            )
            if extra:
                msg += f"Extra in rows: {sorted(extra)}. "
            msg += (
                "Pass input_fields/output_fields to map row columns to "
                "signature fields, or ensure row columns match exactly."
            )
            raise ValueError(msg)
        return sig_in, sig_out, {}
```

**g. A runtime-typed list output field.** `src/dspy_auto_gepa/generator.py:506-540`. Runs on 3.3.1 (verified: rendered and parsed by `ChatAdapter`). Parsing is all-or-nothing per list.

```python
def _build_batch_output_signature(output_model: type) -> type[dspy.Signature]:
    """Build a DSPy Signature with strongly-typed batch output.

    The returned signature has ``generated_outputs: list[output_model]`` so DSPy
    emits a JSON Schema for the LLM rather than a free-form string.  The type
    is set via ``with_updated_fields`` after class creation because static type
    checkers reject using a runtime variable (``output_model``) as a type
    argument in a class-body annotation.
    """

    class _BatchOutputSignature(dspy.Signature):
        """Generate correct output values for multiple inputs at once.

        Return one output object per input, in the SAME ORDER as the inputs
        array.  Each object must match the schema exactly.

        When an input could reasonably fit multiple allowed values, prefer
        the less common one to maintain variety in the dataset.
        """

        task_description: str = dspy.InputField(desc="Description of the task")
        inputs_json: str = dspy.InputField(
            desc="JSON array of input objects to generate outputs for"
        )
        n_to_generate: int = dspy.InputField(
            desc="Number of output objects to generate (must match inputs_json length)"
        )
        generated_outputs: list[Any] = dspy.OutputField(
            desc="List of output objects, one per input, in the same order."
        )

    return _BatchOutputSignature.with_updated_fields(
        "generated_outputs",
        type_=cast("type | None", list.__class_getitem__((output_model,))),
    )
```

**h. Recovering JSON from model text.** `src/dspy_auto_gepa/generator.py:41-78`, the body of `_extract_json`. Pure Python (verified: Q).

```python
    text = text.strip()
    if not text:
        return text

    try:
        json.loads(text)
        return text
    except (json.JSONDecodeError, ValueError):
        pass

    match = re.search(r"```(?:json)?\s*\n?(.*?)\n?\s*```", text, re.DOTALL)
    if match:
        candidate = match.group(1).strip()
        try:
            json.loads(candidate)
            return candidate
        except (json.JSONDecodeError, ValueError):
            pass

    for open_ch, close_ch in [("{", "}"), ("[", "]")]:
        start = text.find(open_ch)
        end = text.rfind(close_ch)
        if start != -1 and end > start:
            candidate = text[start : end + 1]
            try:
                json.loads(candidate)
                return candidate
            except (json.JSONDecodeError, ValueError):
                pass

    try:
        parsed = ast.literal_eval(text)
        if isinstance(parsed, (dict, list)):
            return json.dumps(parsed, default=str)
    except (ValueError, SyntaxError):
        pass

    return text
```

**i. A mock that hides a shape (repo test code).** `tests/test_generator.py:62-86`. Runs (verified: the suite passes). Caveat: the real `dspy.Parallel(return_failed_examples=True)` returns `(results, failed_examples, exceptions)`; a faithful mock must too.

```python
def _make_sync_parallel_mock():
    """Create a mock for dspy.Parallel that executes tasks synchronously.

    Returns (mock_parallel_cls, executed_tasks) where executed_tasks is a list
    of (module, example) pairs that were executed.
    """
    executed_tasks = []

    class SyncParallel:
        def __init__(self, **kwargs):
            pass

        def __call__(self, tasks):
            results = []
            for module, example in tasks:
                executed_tasks.append((module, example))
                try:
                    result = module(**{k: example[k] for k in example.keys()})
                    results.append(result)
                except Exception as e:
                    results.append(e)
            return results

    mock_cls = MagicMock(side_effect=lambda **kwargs: SyncParallel(**kwargs))
    return mock_cls, executed_tasks
```

**j. The fixture that ran a full `dspy.GEPA` offline (mine, not the repo's).** `scratchpad/verify/e2e.py`, from `_resp` through `ReflectionFixture`. Runs on DSPy 3.3.1 + gepa 0.1.4 (verified: 388-call run in about 2 s).

```python
def _resp(text):
    return dotdict(choices=[dotdict(message=dotdict(content=text, tool_calls=None), finish_reason="stop")],
                   usage=dotdict(prompt_tokens=0, completion_tokens=0, total_tokens=0), model="fixture")


class StudentFixture(dspy.BaseLM):
    def __init__(self):
        super().__init__(model="fixture/student", cache=False)
        self.calls = 0

    def forward(self, prompt=None, messages=None, **kwargs):
        self.calls += 1
        system = messages[0]["content"] if messages else ""
        user = messages[-1]["content"] if messages else prompt
        m = re.search(r"\[\[ ## message ## \]\]\n(.*?)(?:\n\n|$)", user, re.S)
        msg = m.group(1).strip() if m else ""
        if "IMPROVED" in system and msg in GOLD:
            u, s = GOLD[msg]["urgency"], GOLD[msg]["sentiment"]
        else:
            u, s = "low", "neutral"
        return _resp(f"[[ ## reasoning ## ]]\nfixture\n\n[[ ## urgency ## ]]\n{u}\n\n[[ ## sentiment ## ]]\n{s}\n\n[[ ## completed ## ]]")


class ReflectionFixture(dspy.BaseLM):
    def __init__(self):
        super().__init__(model="fixture/reflection", cache=False)
        self.calls = 0
        self.prompts = []

    def forward(self, prompt=None, messages=None, **kwargs):
        self.calls += 1
        self.prompts.append(prompt or messages[-1]["content"])
        return _resp("```\nIMPROVED: classify each support ticket's urgency (low/medium/high) and sentiment.\n```")
```

## 4. The old report, corrected

Report: `/home/user/kohaerenzprotokoll/Plan/concept/dspy-repos_2026-09-23/dspy-auto-gepa.md`.

1. **§1, size and tests.** It says „~2900 lines" in `src/`; the count is 3,493. It speaks of „35 unit tests"; that is only `test_auto_gepa.py`. The suite has 132 tests, and 131 pass offline on DSPy 3.3.1.
2. **Idea 1, load-or-train.** It is correct but misses two traps. `force=True` does not retrain, because GEPA resumes from the fixed `gepa_logs` (verified: 4 calls, „Loading gepa state from run dir"). And a cached `run()` loads into the caller's module, while a fresh `run()` leaves it unoptimized.
3. **Idea 2, field inference.** The `reasoning` strip fails for any custom module that wraps a ChainOfThought, because the `isinstance` check sees `Predict` objects (verified). The inference path also drops extra columns silently, and explicit lists are never checked against the rows (`KeyError`).
4. **Idea 6, build_metric as an inspectable step.** `examples/basic.py`'s own retrain path regenerates the reviewed metric (verified: 2 generation calls, human edit lost).
5. **Idea 7, the `metric=Path` bypass.** Correct, with two gaps. The file must take five positional arguments or `dspy.GEPA` raises at construction; the repo's own tests use three-argument metric files. And the bypass does not remove OpenRouter: `train()` still uses the default `kimi-k2.5` reflection LM unless `reflection_lm=` is passed.
6. **Idea 8, AST validation.** The report called it „a genuinely good 'guard reports what it could not check' idea". It is a guard that cannot fail on the common defects: it passed a bare float, `dict(...)`, a three-argument metric, and metrics that raise at runtime (verified: G, V). It never executes the metric.
7. **Idea 9, the metric-writing rules.** Recommended as „a decent checklist". Two of the three few-shot examples crash on DSPy 3.3.1: `answer_exact_match(str, str)` raises `AttributeError`. `fuzzy_match` does not exist. Example 3 calls `dspy.configure` at import, which re-points the process-wide LM, and its `len(pred_trace) >= 2` can never hold under GEPA. The rules contradict the examples (the cheaper-model rule).
8. **Idea 10, the metric convention.** Missing: GEPA enforces it by `inspect.signature(metric).bind(None×5)` (from 3.1.0 on), and a float return yields only „This trajectory got a score of X.".
9. **Idea 11, the budget.** „GEPA's own auto parameter decides the actual rollout/reflection budget from `len(trainset)`" is wrong. The budget comes from the valset size (the trainset only when there is no valset) and the number of predictors: n = 6/12/18 candidates, about 380 + 4V metric calls for light with one predictor (table in OPT). A 10-row light run cost 390 student calls.
10. **Idea 12, `track_stats` and `log_dir`.** It missed that `log_dir` is resume state (see 2), and that `detailed_results` is dropped by `run()` and not saved.
11. **Idea 13, „no Pareto export".** GEPA itself writes `candidates.json`, `run_log.json`, `gepa_state.bin`, `candidate_tree.html` and `generated_best_outputs_valset/` (verified listing), so a parser needs no new instrumentation.
12. **Idea 14, compare() on the same split.** Right, but the split can be one row (10 rows → 7/2/1). A real 0.5 → 1.0 validation gain was reported as `improvement=0.0` (verified). Scores are percentages.
13. **Idea 16, split.** Missing: the third proportion is ignored (the test split gets the remainder: 5/2/3 for `(0.5, 0.2, 0.1)`), bad tuple lengths pass config validation, n=1 gives an empty trainset, and an empty test split crashes `Evaluate`.
14. **Idea 17, `val = val or test`.** Worse than an edge case: every 2-tuple split makes GEPA's selection set the very test set the improvement is reported on (`ds.val is ds.test`), and so does the README's own 2-row quick start.
15. **Idea 19, AutoData.** It says AutoData „includes an LLM-judge quality gate … diversity checker, balanced-output subsampling". False. The judge scores and never rejects (verified: rows scored 0.0 kept). `RejectionSampler`, `DiversityChecker` and `_subsample_balanced` are never called, and six config flags are dead. The balanced path is targeted generation, which skips the judge and dedup.
16. **Idea 21, `sanitize_string`.** „No emoji risk" for German is right (verified), but the regex deletes all CJK, fullwidth, box-drawing, ✓ and ligature characters. That matters for any non-Latin corpus.
17. **Idea 22, fsync writer.** fsync applies to JSONL only. A `.json` output is JSONL that `_to_dicts` cannot read back, and resume accounting is wrong (`n_failed=-3`).
18. **Idea 23, „five strategies".** There are four, then the text is passed through unchanged.
19. **Idea 24, `--run-e2e`.** Described as „reserved in pyproject". It is not defined anywhere, and `poe test-e2e` dies at argument parsing (verified).
20. **§4, seeding.** „No seed passed to `dspy.GEPA` … GEPA's own mutation/reflection sampling is not seeded" is wrong. `dspy.GEPA` defaults to `seed=0` (3.2.1 and 3.3.1); only the wrapper's 42 never reaches it.
21. **§5, the Python version.** „Cannot be installed into `.venv-dspy` as-is" is true only for `pip install`, because of `requires-python`. The code parses on 3.11, and the offline suite passes there (130/131; the failure is the metadata smoke check).
22. **Missed entirely:**
    - the README's „DSPy 3.1+" is false (the import fails on 3.1.0);
    - `generate(n=…)` in the README and docs raises `TypeError`;
    - `docs/advanced.md` raises at `run_baseline`;
    - `docs/medium.md`'s example metric has no `import dspy`;
    - `run()` maps rows twice, which breaks swap mappings;
    - a raising metric silently burns the whole GEPA budget;
    - ChainOfThought modules generate with an empty task description;
    - `AutoGEPA.generate()` ignores `judge_lm` and `dspy.settings.lm`;
    - a vacuous in-flight cap test, and a mock that hides `Parallel`'s tuple.
23. **The unmocked test.** Still unmocked at 80a5402 (verified with a guard; the attempt was blocked).

## 5. Ten things the skill must say

1. A GEPA metric takes five positional arguments and returns `dspy.Prediction(score, feedback)`. GEPA checks the arity at construction; a float return gives no feedback, and a dict breaks it. → MET "The metric contract the repo uses", OPT "Five-argument metric check at construction".
2. A metric that raises becomes silent zeros in both `Evaluate` and GEPA. GEPA then spends its whole budget and returns the seed program, so execute the metric on sample rows and count exceptions before any run. → OPT "Metric exceptions in GEPA become silent zeros".
3. A `log_dir` is resume state: reusing one continues the old run, so "force retrain" in auto-gepa does not retrain. Use a fresh `log_dir` per run. → OPT "`log_dir` resumes, so `force=True` does not retrain".
4. `auto` sets candidates (6/12/18) and the budget depends on the valset and predictor count, not on train size. `light` is about 380 + 4V metric calls with one predictor; 10 rows cost 390 calls. On small data, set `max_metric_calls` explicitly. → OPT "What `auto` means", "What a light run costs on 10 rows".
5. `Evaluate.score` is a percentage, and a one-row test split reported 0.0 improvement for a real gain. Report n with every delta. → API "`Evaluate.score` is a percentage", MET "A real gain was reported as zero".
6. Never select on the set you report on: `val = val or test` silently makes GEPA's Pareto set the test set. → DATA "The validation set can be the test set".
7. Do not let a model draft the metric. The prompt's own examples call `answer_exact_match` on strings, and the AST guard passes them. Use a hand-written metric passed by path. → MET "Few-shot Example 1 is the only one that runs", "The metric source guard cannot fail on the common defects".
8. A unit test with no `metric=` reached OpenRouter. The offline guard (unset keys, black-holed proxy, `litellm.completion` raising) caught it; ship that fixture. → TEST "The unmocked live-call test is still unmocked at 80a5402", "My offline harness".
9. `dspy.LM` caches by default and the library never turns it off; pass `cache=False` explicitly. → PROD "The library never turns the LM cache off".
10. AutoData's quality gates are mostly unwired: the judge never rejects, three components are never called, six flags are dead, and targeted mode asserts labels it never checks. Treat its rows as unvalidated. → DATA "The judge never rejects a row", "Six config flags do nothing", "Three generation paths".
