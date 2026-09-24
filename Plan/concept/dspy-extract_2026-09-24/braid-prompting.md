# Extract: braid-dspy + dspy-advanced-prompting (DSPy knowledge, deep read)

## 1. Header

**braid-dspy**: `/home/user/braid-dspy`, commit `c50c5b1` (github.com/netzkontrast/braid-dspy; its own metadata points to github.com/ziyacivan/braid-dspy). MIT ("Copyright (c) 2025 Braid-DSPy Contributors"). Version 0.2.3 in `pyproject.toml:7` and `braid/__init__.py`, but still `0.1.6` in `setup.py:8`. Targets `dspy-ai>=2.0.0` (`pyproject.toml:28-30`). Its `uv.lock` resolves `dspy 2.6.27` for Python <3.10 and `dspy 3.0.4` for ≥3.10 (`uv.lock:906-911, 942-949`).
- **On DSPy 3.3.1 the library code works.** All 185 tests pass offline, and a DummyLM runs planning plus execution end to end.
- **The documented usage does not.** `dspy.OpenAI` no longer exists, `MIPROv2()` needs a metric, and 11 of 11 documented snippets fail.

What it is: BRAID ("Bounded Reasoning for Autonomous Inference and Decisions", taken from a vendor blog post, README.md:337). One `dspy.Predict` writes a plan as a Mermaid flowchart. Code parses it and orders the nodes with Kahn's algorithm, and a second `Predict` executes each node label. Around that sit regex "protocol" modules (masking, validators, critic, stateful engine, cost metrics, synthetic data) that the main module never calls.

**dspy-advanced-prompting**: `/home/user/dspy-advanced-prompting`, commit `facc1ad` (github.com/netzkontrast/dspy-advanced-prompting; README clones evalops/…). MIT ("Copyright (c) 2025 Jonathan Haas"). Pins `dspy-ai>=2.4.0` (`requirements.txt:1`, `setup.py:8`).
- **On DSPy 3.3.1 everything imports** (pydantic 2.13.5, two `PydanticDeprecatedSince20` warnings). Every DSPy call pattern it uses works under DummyLM: untyped string signatures under `ChainOfThought`/`Predict`, and `dspy.LM(model=…, api_key=…, max_tokens=…)`.

What it is: eleven "techniques used by top AI startups". Nine are files in `src/techniques/`, plus `src/prompts/manager_style.py` and `src/evaluations/evaluation_framework.py`. Each wraps one or more `ChainOfThought` calls around a long instruction text that is passed as an **input field**. Pydantic schemas, keyword heuristics and several hardcoded "results" sit around the calls. The brief's slice lists a `tests/` directory; it does not exist at `facc1ad` (README.md:228 claims it). The only test-like files are `test_notebooks.py`, `validate_with_dspy.py` and `validate_with_real_api.py`.

**What I ran.** Everything was offline: API keys unset, and DSPy's disk cache disabled in every probe. All runs used `git archive` copies under the scratchpad, so neither repository was touched (both `git status` clean). The interpreter was a scratch venv with `dspy==3.3.1` plus pytest, pytest-cov, rich, loguru, jinja2, python-dotenv, jsonschema and numpy. Scripts are in `scratchpad/work/`:
- braid tests: `pytest tests/ --cov=braid [--cov-fail-under=70]`.
- `sig_compare.py` and `rf_compare.py`: old vs new signatures on dspy 3.3.1, 3.0.4 and 2.6.27 (via `uv run --with dspy==X --with cffi`).
- `probe_braid_dspy.py` (A1–A5, B1–B6): DummyLM, and a `litellm_completion` counting patch for cache hits.
- `probe_braid_pure.py` (C–E) and `probe_braid_pure2.py` (F–K): parser, engine, critic, masking, validators, metrics, training, utils. C6 was repeated under PYTHONHASHSEED 1–6.
- `docs_snippets.py`: the documented API, run as written.
- All three braid example scripts, run with no LM.
- `probe_adv_dspy.py` (S1–S9): DummyLM for every technique.
- `probe_adv_eval.py` (T1–T7): evaluation framework and uncertainty detector.
- An inline structured-output probe (U1–U9).
- `validate_with_dspy.py`, plus `test_notebooks.py` both as a script and under pytest.
- Notebooks: JSON parsed, markdown and code cells read, no outputs executed.

`validate_with_real_api.py`, `main.py` and `examples/quick_start.py` were read, not run (they need a real key).

## API

- **[braid] The "type hints fix" changes nothing observable** — Commit `cd1cc2e` ("Fix: Add type hints to signatures for structured output compatibility") only turned `x = dspy.InputField(...)` into `x: str = dspy.InputField(...)` in the four signatures. `c50c5b1` ("Bump version to 0.2.3 and fix structured output signatures") only bumps versions. On DSPy 2.6.27, 3.0.4 and 3.3.1, the pre- and post-commit signatures produce:
  - byte-identical messages in ChatAdapter, JSONAdapter and XMLAdapter (XMLAdapter is absent in 2.6.27);
  - identical JSONAdapter structured-output schemas (`{"properties": {"grd": {"type": "string"}}, "additionalProperties": false, …}`);
  - identical parses.

  Nothing in the repo (no test, issue or changelog entry) shows what broke. The only version-sensitive path in 3.3.1 is PEP 649 annotation handling on Python ≥3.14 (signature.py:142-161), and braid targets 3.9–3.11. braid/signatures.py:6-89; `git show cd1cc2e c50c5b1` [api] (verified: sig_compare.py ×3 versions, rf_compare.py) → here: check_dspy_surface.py
- **[braid] What DSPy 3.3.1 does with an unannotated field** — `SignatureMeta.__new__` sets `raw_annotations[name] = str` for every `FieldInfo` without an annotation and marks `json_schema_extra["IS_TYPE_UNDEFINED"] = True` (dspy/signatures/signature.py:162-169). The only reader of that flag is `Predict`'s input check, which skips the "Type mismatch for field '%s'…" warning for untyped inputs when `settings.warn_on_type_mismatch` is on (dspy/predict/predict.py:202-216). So `: str` re-enables one warning and nothing else. 3.0.4 and 2.6.27 have no such flag (`IS_TYPE_UNDEFINED` is None for both variants there). [api] (verified: sig_compare.py prints the flags per version; read)
- **[braid] A class docstring is the LM's objective** — ChatAdapter sends the signature docstring after "In adhering to this structure, your objective is:". braid's docstrings are developer notes, and they go to the model verbatim: "Signature for GRD planning phase. This signature defines the input/output structure for generating a Guided Reasoning Diagram…", and for steps "Used internally by the BRAID module for step-by-step execution." braid/signatures.py:7-17, 79-83 [trap] (verified: sig_compare.py printed the system message)
- **[braid] Rules carried in an output field `desc`** — `BraidPlanSignature.grd` has a six-point "CRITICAL RULES" desc: no answer; procedural scaffold; action not value; node label under 15 tokens; `flowchart TD`; no numerical results. In the default path this desc, plus the docstring, is the only BRAID rule text the LM sees. signatures.py:21-30 [pattern] (verified: probe A1 — "CRITICAL RULES" present in messages, generator rules absent)
- **[braid] InputField with `default=`** — `previous_results: str = dspy.InputField(desc=…, default="")`. DSPy 3.3.1 `Predict` fills missing inputs from field defaults (dspy/predict/predict.py:186-189). `BraidExecuteSignature` (the only one with a default) and `BraidReasoningSignature` are exported and used nowhere. signatures.py:33-75 [api] (verified: grep; read)
- **[braid] Overriding `__call__` and returning a dataclass bypasses DSPy's module machinery** — `BraidReasoning.forward` returns `BraidResult` (a dataclass, not `dspy.Prediction`), and `__call__` is overridden as `return self.forward(problem, **kwargs)`. That skips DSPy 3.3.1 `Module.__call__`: the `@with_callbacks` decorator, the `caller_modules` context, and `track_usage` → `_set_lm_usage` (dspy/primitives/module.py:93-110). A registered callback's `on_module_start` fired four times, all for inner `Predict` calls, never for `BraidReasoning`, and `isinstance(result, dspy.Prediction)` is False. braid/module.py:12-24, 273-275 [trap] (verified: probe B3) → here: lmrun.py
- **[braid] DSPy only tunes predictors reachable through Module attributes** — `BraidReasoning().named_predictors()` is `['plan', 'execute_step']`. The predictor the default `forward` actually calls, `self.generator.predictor`, lives on `GRDGenerator`, a plain class, so no DSPy optimizer can see it. Modules held in dicts are discovered: see `[prompting] AdaptiveFolder`, 11 predictors. braid/module.py:66-74; generator.py:10, 77-78 [trap] (verified: probe B2) → here: pairs.py
- **[braid] `dspy.LM` has no `.temperature` attribute** — Temperature lives in `lm.kwargs["temperature"]`, so `hasattr(dspy.LM("openai/x", temperature=0.9), "temperature")` is False. `GRDGenerator(temperature=0.3)` sets `lm.temperature` only `if hasattr(lm, "temperature")` and never takes effect. In the default Predict path it is not even attempted. generator.py:55-75, 121-136 [trap] (verified: probe A3) → here: lmrun.py
- **[braid] Calling an LM directly returns `list[str]`** — `lm(prompt)` returns a list of completions. The `use_dspy_predict=False` fallback does `getattr(response, "text", str(response))`, producing the repr `"['[[ ## grd ## ]]\\n```mermaid\\nflowchart TD…']"` with escaped newlines. The extractor then finds nothing, so a valid diagram yields "Could not extract Mermaid code from response". generator.py:109-136 [trap] (verified: probe A4)
- **[braid] `dspy.LM()` needs a model** — `dspy.LM.__init__(self, model: str, …)` (dspy/clients/lm.py:62-64). The fallback's `dspy.LM()` raises TypeError, which a bare `except:` converts to `ValueError("DSPy language model not configured. Call dspy.configure(lm=...) first.")`. generator.py:111-119 [api] (verified: read)
- **[braid] The no-LM error text** — Without `dspy.configure(lm=…)`, `Predict` raises "No LM is loaded. Please configure the LM using `dspy.configure(lm=dspy.LM(...))`. e.g, `dspy.configure(lm=dspy.LM('openai/gpt-4o-mini'))`" (dspy/predict/predict.py:154). braid catches it per step; see TRAP. [api] (verified: probe B1)
- **[braid] `dspy.OpenAI` is gone in 3.3.1** — `AttributeError: module 'dspy' has no attribute 'OpenAI'`. Used at README.md:56, braid/module.py:39, docs/index.md:14, docs/integration.md:23, docs/examples.md:10,64, docs/examples/basic_usage.md:10, docs/examples/gsm8k.md:10 and docs/examples/optimization.md:12, and in comments/prints of all three examples. The 3.x form is `dspy.LM("openai/<model>")`. [api] (verified: docs_snippets.py) → here: check_dspy_surface.py
- **[braid] `MIPROv2()` requires `metric`** — `TypeError: MIPROv2.__init__() missing 1 required positional argument: 'metric'`. The docs construct it bare at docs/examples.md:77, docs/integration.md:49 and docs/examples/optimization.md:43 (commented at examples/optimization_example.py:60 and gsm8k_example.py:122). [api] (verified: docs_snippets.py)
- **[braid] `Example.inputs()` without `with_inputs`** — Raises `ValueError("Inputs have not been set for this example. Use `example.with_inputs()` to set them.")` (dspy/primitives/example.py:264). This is what BootstrapFewShot hits on braid's trainsets; see OPT. [api] (verified: probe B6 log)
- **[braid] Calling `.forward()` directly logs a warning in 3.3.1** — `Module.__getattribute__` inspects the stack and logs "Calling module.forward(...) on <Class> directly is discouraged. Please use module(...) instead." unless the calling frame is named `__call__` (dspy/primitives/module.py:336-350). braid's `__call__` override avoids it by name; its tests call `.forward` directly (tests/test_module.py:45, tests/test_integration.py:146). [api] (verified: read)
- **[prompting] Every technique is a `ChainOfThought` over an untyped string signature** — 15 classes construct 20 predictors: 19 `ChainOfThought` and 1 `Predict`. `ChainOfThought` prepends a `reasoning` output, e.g. `ManagerStylePrompt`: `manager_instructions, task, context -> reasoning, output`, and `EscapeHatchSignature`: `question, uncertainty_guidelines, context -> reasoning, response, uncertainty_analysis`. The one plain `Predict` is `PromptDistiller.student` (`task, examples -> output`). All fields are unannotated (so `str`), including those that carry JSON. [api] (verified: probe S1 lists every predictor and its fields)
- **[prompting] Static instructions passed as input fields** — The technique's instruction text is an input value sent on every call:
  - `manager_instructions`: a rendered onboarding doc of 7,329 chars / 1,043 words / 200 lines;
  - `role_description`, `planning_guidelines`, `optimization_guidelines`, `uncertainty_guidelines`, `trace_instructions`, `output_schema`, `folding_strategy`.

  This text lands in the user message. The system message's objective is the one-line docstring ("Execute task with manager-style detailed instructions"). Instruction-proposing optimizers (MIPROv2/COPRO/GEPA) rewrite `signature.instructions`, not input values, so the text that *is* the technique cannot be optimized, and it is resent in full on every call. manager_style.py:184-210; role_prompting.py:37-92; task_planning.py:53-116; escape_hatches.py:45-52, 205-218; thinking_traces.py:93-99 [pattern] (verified: probe S2 — doc in user message True, in system False)
- **[prompting] `forward` returns plain Python values, not a `Prediction`** — By class:
  - `str`: ManagerStyleAgent, PersonaAgent, FewShotLearner, StructuredOutputGenerator, TaskExecutor;
  - `dict`: EscapeHatchResponder, GracefulDegradation, ThinkingTracer, DebugLogger, TaskOrchestrator, `PromptFolder.fold`;
  - a pydantic `TaskPlan`: TaskPlanner;
  - a tuple: `ChainOfThoughtFewShot`.

  `dspy.Evaluate` and optimizers hand whatever `forward` returns to the metric as `pred`. manager_style.py:202-210; escape_hatches.py:205-226; task_planning.py:78-122 [api] (verified: probe S2 `forward returns: str`; read)
- **[prompting] JSON inside a `str` output field, with no schema given** — `task_plan_json`, `analysis_json`, `sub_prompts_json`, `uncertainty_analysis` and `debug_info` are free-text fields parsed with `json.loads`. The desc never states the schema; `TaskPlan` needs `goal, context, sub_tasks[id,title,description,estimated_complexity,acceptance_criteria], success_metrics`. A fenced reply fails: `ValueError: Failed to parse task plan: Expecting value: line 1 column 1 (char 0)`. The DSPy 3.x alternative is an output field typed with the Pydantic model (`task_plan: TaskPlan = dspy.OutputField()`), where the adapter states the schema and validates. task_planning.py:59, 118-122; meta_prompting.py:49, 97-101; prompt_folding.py:50, 87-90; escape_hatches.py:52; thinking_traces.py:108, 343-346 [pattern] (verified: probe S8)
- **[prompting] A free-text boolean compared as a string** — `ConditionalFolder` uses `dspy.ChainOfThought("prompt, result -> condition_met")` and then `result.condition_met.lower() == "true"`, so "True." and "Yes" count as false. A field typed `condition_met: bool` would be parsed by the adapter. prompt_folding.py:182, 196-203 [pattern] (verified: read)
- **[prompting] Inline string signatures** — `dspy.ChainOfThought("prompt -> critique")`, `("prompt, critique -> refined_prompt")` and `("task -> best_strategy")`, all untyped. The last (`AdaptiveFolder.task_analyzer`) is never called, because routing uses keywords. meta_prompting.py:273-274; prompt_folding.py:346 [api] (verified: probes S1, S7)
- **[prompting] Modules held in dicts are discovered by DSPy** — `AdaptiveFolder.folders = {strategy: PromptFolder(strategy) for strategy in FoldingStrategy}` exposes 11 predictors, e.g. `folders['FoldingStrategy.RECURSIVE'].prompt_generator.predict`, plus the unused `task_analyzer`. `WorkflowFolder` exposes 6 that are never called. `MultiPersonaOrchestrator` exposes `personas['e'].role_executor.predict`. prompt_folding.py:224-228, 347-350; role_prompting.py:289-291 [api] (verified: probe S1)
- **[prompting] LM configuration used everywhere** — `dspy.LM(model="gpt-4o-mini", api_key=api_key, max_tokens=2000)` followed by `dspy.settings.configure(lm=lm)` (validate_with_real_api.py:33-38; examples/quick_start.py:77-78 with 1000; the notebooks with 1500/2000). There is no provider prefix and no `cache=`, so DSPy's request cache is on. [api] (verified: read; not run, needs a real key)
- **[prompting] Pydantic v1 idioms on Pydantic 2.13.5** — `class Config: arbitrary_types_allowed = True` (thinking_traces.py:76-77; evaluation_framework.py:101-102) and `metrics.__fields__` (evaluation_framework.py:293, 477, 523) emit `PydanticDeprecatedSince20`. `.dict()`/`.json()` are the same deprecated family (task_planning.py:136, 215; meta_prompting.py:125; prompt_folding.py:83, 97). `from pydantic import validator` is imported and unused (structured_output.py:10; evaluation_framework.py:10). [api] (verified: import probe with warnings on; T2/T5 printed the `__fields__` warning)

## OPT

- **[braid] BraidOptimizer compiles a predictor that the default program never calls** — `_optimize_planning` sets `module.plan = self.base_optimizer.compile(student=module.plan, trainset=plan_trainset)`, and `_optimize_execution` compiles `module.execute_step`. The default `BraidReasoning()` (`use_generator=True`) plans through `self.generator.predictor`, so the compiled planning demos are dead. With `LabeledFewShot(k=2)`: `plan.demos = 2`, `generator.predictor.demos = 0`, and the next planning call carried 2 messages (system + user, zero demos). optimizer.py:381-418, 420-464; module.py:94-117 [trap] (verified: probe B5) → here: pairs.py
- **[braid] The trainset is the model's own unfiltered output** — The plan trainset pairs every generated `grd` with its problem, including `None` or invalid ones. A `quality` score is computed per GRD and never used. Execution demos are the model's own step outputs. The user metric's `execution_score` is computed and discarded. optimizer.py:386-416, 425-462 [trap] (verified: read; probe B5 shows the model's GRDs as demos)
- **[braid] Examples built without `.with_inputs()`** — `dspy.Example(problem=…, grd=…)` and `dspy.Example(step_description=…, context=…, step_output=…)` have `input_keys=None`. BootstrapFewShot then:
  - logs "Failed to run or to evaluate example Example({...}) (input_keys=None) with <metric> due to Inputs have not been set for this example. Use `example.with_inputs()` to set them.";
  - reports "Bootstrapped 0 full traces after 0 examples for up to 1 rounds, amounting to 1 attempts.";
  - still installs raw labeled demos (plan demos = 1 with `max_labeled_demos=1`).

  Errors are logged, not raised, until `max_errors` (default `None` → `dspy.settings.max_errors`, which is 10). optimizer.py:413-415, 451-457; dspy/teleprompt/bootstrap.py:42-45, 104-105, 218-221; dspy/dsp/utils/settings.py:32 [trap] (verified: probe B6)
- **[braid] Two incompatible metric contracts** — `BraidOptimizer.optimize(module, trainset, metric)` expects `metric(result: BraidResult, expected_answer)`. It is never forwarded to `base_optimizer.compile(…)`. The base optimizer calls its own metric (given at its construction) DSPy-style, as `metric(example, prediction, trace=None)`, on the compiled sub-predictor's output. optimizer.py:346-379, 416, 438, 460-462 [pattern] (verified: read)
- **[braid] `num_threads` is accepted and ignored** — `optimize(..., num_threads: int = 1)` never uses it, while docs/integration.md:149 advises "Use `num_threads` in optimizer for parallel optimization". optimizer.py:351 [trap] (verified: grep)
- **[braid] With no base optimizer, `optimize` is a no-op** — `_simple_optimize` returns the module unchanged ("In a real implementation, this could use few-shot learning…"). examples/optimization_example.py still prints "Optimization completed (simple mode)" and "Score improvement: +0.000". optimizer.py:466-473 [trap] (verified: ran optimization_example.py offline)
- **[braid] Train/serve context mismatch** — Execution demos use `context=f"Problem: {ex['problem']}"`. At runtime the context is `f"Problem: {problem}\n\nPrevious Steps:\n{previous_results}"`. optimizer.py:452-456; module.py:185 [pattern] (verified: read)
- **[braid] The optimizer class is a `dspy.Module` with no `forward`** — `BraidOptimizer(dspy.Module)` is a wrapper, not a program. optimizer.py:315-344 [api] (verified: read)
- **[braid] LabeledFewShot in 3.3.1** — `compile(student, *, trainset, sample=True)` sets each predictor's `demos = rng.sample(trainset, min(k, len(trainset)))`, with no metric and no LM call. dspy/teleprompt/vanilla.py:10-21 [api] (verified: read; probe B5)
- **[braid] BootstrapFewShot defaults in 3.3.1** — `max_bootstrapped_demos=4, max_labeled_demos=16, max_errors=None`, and `compile(student, *, teacher=None, trainset)`. Labeled demos come from an inner `LabeledFewShot(k=max_labeled_demos)` when the teacher is uncompiled. dspy/teleprompt/bootstrap.py:37-45, 84, 104-105 [api] (verified: read)
- **[prompting] The adaptive distillation loop stops after one iteration by construction** — `quality_retention = 0.88 / 0.95 = 0.9263` always, because both accuracies are hardcoded. With the default `quality_threshold=0.9`, the loop breaks in iteration 1. `_adjust_config` (strategy rotation if < 0.8, `num_examples += 20` if < 0.9) can never trigger. model_distillation.py:54-57, 162, 284, 317-336, 338-354 [trap] (verified: probe S9)
- **[prompting] "Distillation" is a prompt edit, and teacher and student are one LM** — `_create_distilled_prompt` by strategy:
  - DIRECT returns the original;
  - SYNTHETIC appends only `examples[:3]`, although `num_examples` defaults to 100 (97 teacher calls wasted);
  - CHAIN appends 4 hardcoded generic steps; SELECTIVE, 3 hardcoded features; ENSEMBLE, a fixed paragraph.

  Neither predictor has its own LM, so both run on `dspy.settings.lm`. The model names are used only for a cost lookup. 3.3.1 has `Module.set_lm(lm)` for per-module LMs (dspy/primitives/module.py:179). model_distillation.py:93-98, 178-255 [trap] (verified: probe S9 — `teacher.predict.lm is student.lm` → both None)

## MET

- **[braid] `_default_metric` cannot tell a right answer from a wrong one** — The score is the sum of:
  - `0.5 · overall_quality` (if parsed);
  - `0.5 · (step_score + answer_present)/2`;
  - `+0.2` if `expected in answer or answer in expected`;

  capped at 1.0. For a 4-node GRD with 4 steps and expected "60 km/h": the answers "60 km/h", "7000 km/h", "Error: No LM is loaded." and "6" all score **1.000**. optimizer.py:475-519 [trap] (verified: probe I2) → here: pairs.py (the metric must fall on the canaries)
- **[braid] GRDMetrics weights, with vacuous components** — `overall = 0.15·validity + 0.10·completeness + 0.10·traceability + 0.25·atomicity + 0.20·masking + 0.20·scaffolding`. Atomicity is 1.0 for zero nodes, and masking is 1.0 when no leak regex hits. Measured overall scores:
  - `"flowchart TD"` (empty chart): **0.68**;
  - non-Mermaid text `"graphs are nice\nhello"`: 0.68;
  - `A[banana] --> B[banana]`: 0.86;
  - a cyclic plan whose Kahn order keeps 1 of 4 nodes: 0.938.

  optimizer.py:23-252 [trap] (verified: probe I1)
- **[braid] The scaffolding score counts verbs anywhere, including node IDs** — `procedural_scaffolding_score` counts action verbs over the whole Mermaid text and divides by the number of `\w+\s*\[[^\]]+\]` nodes (minimum 1). `Calculate[Calculate]` counts twice, and diamond or round nodes are not counted as nodes. Buckets are ≥0.8 → 1.0, ≥0.5 → 0.8, ≥0.3 → 0.6, else 0.4. The GRD in examples/optimization_example.py:121-127 scores 1.000 on every metric. optimizer.py:161-203 [trap] (verified: ran optimization_example.py)
- **[braid] Masking-compliance buckets** — 0 regex hits → 1.0, ≤2 → 0.7, ≤5 → 0.4, else 0.1. The five patterns are `=\s*\d+`, `result\s*[:=]?\s*\d+`, `answer\s*[:=]?\s*\d+`, `\d+\s*(?:km/h|mph|m/s)` and `\d+\s*(?:dollars?|\$)`. optimizer.py:125-159 [number] (verified: read)
- **[braid] Completeness and traceability formulas** — `completeness` = 0.3 (has a start) + 0.3 (has an end) + 0.2 (3–20 nodes; 0.1 if >20) + 0.2 (has edges). `execution_traceability` = (|Kahn order|/|nodes| + (1.0 if every node is ordered else 0.5)) / 2. optimizer.py:35-95 [number] (verified: read)
- **[braid] GRDValidator's combined score and validity** — Weights are atomicity 0.4, scaffolding 0.4, structural 0.2. The structural score is `1 − 0.25·errors − 0.1·warnings`. `valid` requires every sub-validator to be valid, but atomicity and scaffolding are always valid in non-strict mode, so default validity equals structural validity. Measured:
  - an empty GRD scores 0.93 (TOO_FEW_NODES, INVALID_START_NODES);
  - `A[banana] --> B[banana banana]` is valid with 1.0;
  - a 40-token label is valid with 0.833.

  validators.py:161, 312-316, 466-475, 519-541 [trap] (verified: probe G1)
- **[braid] "Tokens" are regex words, and the 15-token rule is unmeasured** — `count_tokens = len(re.findall(r"\b\w+\b|[^\w\s]", text))`, so "don't use 3.5km/h" counts 9. The node score is `max(0, 1 − (tokens/max − 1)·0.5)`. The ≤15 limit is attributed to "BRAID research" ("nano-scale models achieve highest accuracy when node labels contain fewer than 15 tokens"), and no measurement exists in the repo. validators.py:73-75, 101-121, 152-158 [claim] (verified: probe G1)
- **[braid] WEAK_SCAFFOLDING costs nothing** — The INFO issue is added per node, but `validate_grd` filters INFO out and scores only errors and warnings, so a label without any action verb scores 1.0. validators.py:293-310, 333-334 [trap] (verified: probe G1)
- **[braid] Critic "confidence" is a keyword ratio** — `passed=False` iff `failure_count > 0 and failure_count >= success_count`. `confidence = max(s,f)/(s+f)`, and 0.5 when no keyword matches. Measured:
  - `""` passes (0.50);
  - "The answer is not correct." passes (1.00);
  - "There are no errors, the answer is right." fails (a tie, via `\bno\b`);
  - "I verified it: true, but one error remains" passes (0.67).

  critic.py:216-275 [trap] (verified: probe E1)
- **[braid] The PPD score is off by 100× from its own docstring** — `ppd = (accuracy / cost) · 0.01`. The docstring says "A score of 100 means 100% accuracy at $0.01 cost", but `calculate_ppd_score(1.0, 0.01) = 1.0`. A cost of 0 gives `inf` (0.0 if accuracy is 0). metrics.py:275-302 [trap] (verified: probe H1)
- **[braid] `efficiency_multiplier` is hardwired to 1.0** — `compare_with_baseline` returns 1.0 unless `baseline_accuracy` is passed. README.md:130-131, docs/examples.md:286-287 and `generate_report(…, baseline_model=…)` never pass it, so every report prints "1.00x". Passing `baseline_accuracy=0.95` with the README numbers gives 0.474. The "baseline cost" there is ONE average call (`avg_tokens·0.7` in, `·0.3` out; $0.01293), compared against BRAID's total of 3 calls ($0.02725). metrics.py:304-356, 408-418 [trap] (verified: probe H2)
- **[braid] `BraidOptimizer.evaluate` field semantics** — `average_execution_score` is `min(len(reasoning_steps)/10, 1.0)`, so more steps score better. `valid_results` counts evaluated examples, not results with `valid=True`: the offline run printed `valid_results: 2` while both results were invalid. optimizer.py:521-578 [trap] (verified: ran optimization_example.py)
- **[braid] Substring answer matching makes "" correct** — examples/gsm8k_example.py:56-59 tests `expected in got or got in expected`. With no LM configured, every `result.answer` is "", and the script prints "Valid Results: 0 / Correct Answers: 3 / Accuracy: 100.0%". [trap] (verified: ran gsm8k_example.py offline)
- **[prompting] A suite where every test fails scores 0.70** — Several metrics default to perfect when they have nothing to measure:
  - `edge_case_performance` and `robustness_score` are 1.0 when no test of that type exists;
  - `consistency_score` = mean over types of `1 − std(scores)`, so identical failing scores are perfectly "consistent", and it is 1.0 when no type has ≥2 scores;
  - precision and recall are 1.0 when their denominators are 0, so `f1 = 1.0`;
  - `test_coverage = len(results)/len(test_cases)` is 1.0 by construction.

  `overall_score = 0.3·accuracy + 0.2·consistency + 0.2·robustness + 0.2·edge + 0.1·f1`. Three FUNCTIONAL `exact_match` tests that all fail give accuracy 0.0, precision/recall/f1 1.0, consistency, robustness, edge and coverage 1.0, and **overall 0.70**. `passed` is True when `minimum_scores` is empty. evaluation_framework.py:77-89, 226-268, 270-278 [trap] (verified: probe T3) → here: baseline.py
- **[prompting] The `custom_evaluator` contract mismatch fails tests regardless of output** — `_evaluate_output` returns `evaluator(actual, expected)` and the caller unpacks `passed, score`. The suite's own evaluators return a bare bool (`lambda actual, _: "DROP TABLE" not in actual`). The ADVERSARIAL and CONSISTENCY tests therefore always fail with "cannot unpack non-iterable bool object" (caught and recorded as a failure). The module's own `__main__` demo ends "Overall Score: 0.460 / Passed: False". evaluation_framework.py:149-153, 198-200, 354, 367 [trap] (verified: probe T2)
- **[prompting] Criteria precedence and thresholds** — The first matching criterion decides:
  1. `exact_match`;
  2. `contains_all`: score = 1 − missing/required, and passed only if score **> 0.8**, so 4 of 5 present → (False, 0.8);
  3. `semantic_similarity`: word-set Jaccard with threshold 0.8 ("the cat sat" vs "a cat is sitting" = 0.167);
  4. `custom_evaluator`;
  5. plain `==`.

  evaluation_framework.py:178-220 [pattern] (verified: probe T7)
- **[prompting] `importance` and `timeout_ms` are never read** — `TestCase.importance` (the suite sets 0.8–2.0) and `timeout_ms=5000` are declared and not used by any scoring or execution. evaluation_framework.py:56-58, 332-380 [trap] (verified: grep)
- **[prompting] A/B "significance" from deterministic repeats** — `compare_prompts` reruns both prompts `num_runs=5` times. It uses `np.std` (ddof 0), `pooled = sqrt((sa²+sb²)/2)`, `t = (ma−mb)/(pooled·sqrt(2/n))` and a fixed `|t| > 2.0` with no degrees of freedom. Deterministic outputs, which is what the DSPy cache returns on reruns, give stds of 0 and 1e-16, so t = 1.007e16 → "significant: True, winner: A". A vs A gives t = 0.0, "Tie". evaluation_framework.py:403-445 [trap] (verified: probe T4) → here: baseline.py (repeats with the cache off, P18)
- **[prompting] The regression runner crashes on its second run** — The first run stores the baseline with `json.dump(..., default=str)`, which turns the `EvaluationMetrics` object into the string "accuracy=1.0 precision=1.0 recall=1.0 f1_score=1.0 …". The second run calls `baseline_metrics.get(metric, 0)` on that string → `AttributeError: 'str' object has no attribute 'get'`. The drift threshold is ±0.05 absolute per metric. evaluation_framework.py:455-503 [trap] (verified: probe T5) → here: baseline.py
- **[prompting] Failure lists are truncated silently** — `failed_tests[:5]` and `failed[:5]` print no count of the rest. evaluation_framework.py:313, 534 [trap] (verified: read)
- **[prompting] Escape-hatch "confidence" is a hedge-word lookup that cannot see "I don't know"** — Levels are checked UNABLE → HIGH → MEDIUM → LOW, first substring hit wins, and the values are {0.0, 0.2, 0.5, 0.7, 0.95}. The text is lowercased, but the HIGH/UNABLE phrases are written with a capital "I" ("I'm not sure", "I don't know", "I cannot", "I'm unable", "I don't have access", "I lack the information"), so they never match. Measured:
  - "I don't know." → NONE 0.95;
  - the guidelines' own recommended admissions, "I don't have enough information to answer that definitively" and "As of my last update…" → 0.95;
  - "could" → 0.5, and "may" (so "The Mayo Clinic…") → 0.5.

  README.md:178's "Confidence: 0.15" is not a value the detector can produce. escape_hatches.py:60-96, 161-203 [trap] (verified: probes S4, T1)
- **[prompting] The model's own uncertainty report is discarded** — `EscapeHatchSignature` asks for `uncertainty_analysis` "in JSON format". `forward` returns it only as `raw_analysis`, and everything downstream uses the keyword number. escape_hatches.py:52, 220-226 [trap] (verified: probe S4 keys)
- **[prompting] Degradation replaces confident answers** — `GracefulDegradation(confidence_threshold=0.6)` swaps in a template when the keyword confidence is below 0.6, i.e. whenever "could", "may" or "might" appears. The confident "You could use a hash map; it is O(1)." became "I have limited confidence in my response to this question.…". The template's clarifying-question and resource sections never appear, because the detector never fills them. escape_hatches.py:229-293 [trap] (verified: probe S4)
- **[prompting] The real-API "validation" counts keywords and output characters** — Success means "no exception". `has_empathy`, `has_solution`, `has_root_cause` and `has_thinking_markers` (which checks an `[ANALYSIS]` marker the instructions never define) are printed and never affect success. Usage is estimated as response chars // 4 × $0.0015/1K, ignoring input prompts and the CoT `reasoning`. README.md:128-135's "6 calls · 1,282 tokens · $0.0019" comes from this. validate_with_real_api.py:72-79, 223, 242-268, 322-348 [claim] (verified: read; not run)
- **[prompting] Notebook "scores" are typed in** — when_to_use_what.ipynb prints "Manager-Style: 95/100 … 🏆 Winner" from hardcoded dicts. technique_comparison.ipynb states "Security Detection: All techniques successfully identified SQL injection vulnerability" and "~2-4 seconds" (lines 434-435 of the JSON) with 0 saved outputs across all 79 cells of the 4 notebooks. Its "detection" is `count_security_mentions` over a prompt that itself says "security vulnerabilities". [claim] (verified: parsed the notebook JSON)
- **[prompting] Distillation metrics are constants** — `_evaluate_model_performance` returns accuracy 0.95/0.88 ("# Simulated"), consistency 0.92/0.85 and token_efficiency 0.8. The collected outputs are never scored. The `prompt` argument is unused and the student is called with `examples=""`, so the distilled prompt never reaches it. `speed_improvement` is a ratio of `time.time()` latencies of the same LM. model_distillation.py:257-288 [trap] (verified: probe S9 — 11 LM calls, student saw no distilled prompt)

## DATA

- **[braid] Synthetic data contains five GRDs, whatever its size** — There are 3 math, 1 logic and 1 reasoning template, each with one fixed GRD; the variables only change the problem text. `generate_training_dataset(size=100)` returned 100 valid samples with **5 distinct GRDs** and 89 distinct problems. Mix ratios are 0.4/0.3/0.3 via `int()`, the remainder goes to reasoning, and `random` is unseeded (no seed parameter). training.py:64-153, 172-182, 262-291 [trap] (verified: probe J1) → here: trainset.py
- **[braid] Template artefacts** — The generated data contains:
  - "Tweety is a mammals" (`{item} is a {category_a}` filled with plural categories);
  - answers built with `rstrip('s')` ("living thing");
  - float noise ("x = 0.3333333333333333");
  - giver == receiver in 27 of 300 reasoning samples ("Bob has 5 books. Bob gives Bob 2 more.").

  training.py:79, 96, 113, 119, 131, 137-151 [trap] (verified: probe J1)
- **[braid] `create_dspy_examples` drops the label** — It builds `dspy.Example(problem, grd).with_inputs("problem")` and calls `.with_inputs("problem")` again when `expected_answer` exists; the answer itself is never stored (keys `['problem','grd']`). training.py:417-446 [trap] (verified: probe J1)
- **[braid] Synthetic "validation" is structural only** — `validate_samples` uses the default `GRDValidator` (non-strict, so structural checks only) and 100 of 100 pass. `DatasetStats.validation_passed` counts successful extraction and parsing, not validator verdicts. training.py:293-333, 485-540 [trap] (verified: probe J1)
- **[braid] OpenAI fine-tune export shape** — `{"messages": [system (4 BRAID rules), user "Create a GRD for this problem: …", assistant = grd including the ```mermaid fences]}`. JSONL/JSON exporters use `ensure_ascii=False` and round-trip. training.py:336-400, 448-483 [recipe] (verified: tests pass; read)
- **[prompting] Few-shot quality tiers** — `ExampleQuality` is GOLD/SILVER/BRONZE/CHALLENGING. `select_examples` takes up to 2 CHALLENGING first, then GOLD up to `max_examples=5`, then any others except BRONZE. **`input_text` is not used**, despite the `strategy="similarity"` default: two different inputs select the same list, `['challenging','challenging','gold','gold','gold']`. CHALLENGING examples get "(Note: This is a challenging case)" appended. few_shot.py:16-20, 42-47, 78-107 [pattern] (verified: probe S3) → here: pairs.py (force hard negatives such as Negentropie/Entropie into every prompt)
- **[prompting] Examples are prompt text, not DSPy demos** — `FewShotLearner` formats examples into the `examples` **input field** ("Example 1:\nInput: …\nReasoning: …\nOutput: …", separator `"\n---\n"`). The predictor's `demos` stays empty, so LabeledFewShot and BootstrapFewShot cannot see, select or replace them. `task_with_examples` is built and unused. few_shot.py:97-124 [pattern] (verified: probe S3 — demos 0, "Example 1:" in the user message)
- **[prompting] A GOLD example contains broken code** — `await processS inglePayment(payment, idempotencyKey);`, and a linear `delay(1000 * (4 - retries))` is labelled "Exponential backoff". few_shot.py:249, 255 [trap] (verified: read)
- **[prompting] The test-case taxonomy** — `TestCaseType` is FUNCTIONAL, EDGE_CASE, ADVERSARIAL, PERFORMANCE, REGRESSION, CONSISTENCY, ROBUSTNESS. `TestCase(id, name, test_type, input, expected_output, evaluation_criteria, importance=1.0, tags=None, timeout_ms=5000)`, and `EvaluationSuite(name, description, test_cases, evaluation_criteria={}, minimum_scores={})`. README.md:293-303's snippet omits `name` and `test_type` (TypeError) and `description` (ValidationError). evaluation_framework.py:24-63, 92-99 [pattern] (verified: probe T6)
- **[prompting] Teacher example generation** — Cycles five variation labels ("simple case", "complex case", "edge case", "typical use case", "challenging scenario") appended as `"{base_prompt} (Variation: …)"`, with context "Generate a high-quality example for: …", and stores `input, reasoning, output`. model_distillation.py:100-129 [pattern] (verified: read; probe S9)

## AGENT

- **[prompting] A model-planned DAG, scheduled by code** — `TaskPlanner` asks the model for a JSON plan, and `TaskOrchestrator` runs it with a code-side scheduler:
  - a task is executable when all its `dependencies` are COMPLETED;
  - if nothing is executable while tasks remain, it raises `RuntimeError(f"Tasks blocked: {ids}")`, so cycles and dangling ids surface;
  - a failed task re-raises;
  - `max_parallel` only caps the batch size, and execution stays sequential.

  task_planning.py:125-218 [pattern] (verified: read)
- **[prompting] RecursiveTaskPlanner leaves dangling dependencies** — Children get ids `"{parent}.{child}"`, but their `dependencies` are not rewritten (`('1.b', ['a'])`). Siblings that depended on the replaced parent keep pointing at it (`('2', ['1'])`), so `TaskOrchestrator` would stop with "Tasks blocked". Decomposition triggers on `estimated_complexity >= 7`, >50 words, or the substrings "multiple steps" or "complex"; `max_depth=3`. task_planning.py:271-320 [trap] (verified: probe S8)
- **[prompting] Multi-persona "orchestration"** — `MultiPersonaOrchestrator.panel_discussion` calls each persona in turn and returns a dict of raw answers, with no aggregation or judge. `forward(task, required_personas)` does the same for a subset. role_prompting.py:286-311 [pattern] (verified: read)
- **[braid] An engine driven by an executor callable** — `StatefulExecutionEngine.execute(problem, executor)` and `CriticExecutor.execute_with_feedback(problem, executor)` take any `executor(node, context) -> str`. The context carries `problem`, `current_node`, `current_label`, `previous_results`, `execution_path` and `previous_steps_formatted` (label: result lines). Neither is wired to DSPy or to `BraidReasoning`. engine.py:236-366; critic.py:391-433 [pattern] (verified: probes D1-D4, E2; grep)

## PROD

- **[braid] Retries under the request cache replay the same answer** — `GRDGenerator.generate` retries `self.predictor(problem=problem)` with identical inputs up to `max_retries=3`. With `dspy.LM(cache=True)` (the default), a bad first answer comes back from the cache: 3 attempts made **1 real completion** (3 with `cache=False`). In 3.3.1 a retry can bypass the cache with a different `rollout_id` plus temperature > 0; with temperature 0 DSPy warns "rollout_id has no effect when temperature=0; set temperature>0 to bypass the cache." generator.py:103-108, 141-156; dspy/clients/lm.py:98-102, 165-168, 173-183 [trap] (verified: probe A5) → here: lmrun.py (cache=False already)
- **[braid] A price "update" deleted its provenance marks** — `baec4f3` ("update models and pricing for Dec 2025") changed values and removed the `# Estimated` comments on claude-4.5-sonnet/-opus, gemini-2.5-flash and gemini-3.0-pro/-flash, plus the "Currently free in experimental" note on gemini-2.0-pro-exp. The header now says "Updated December 2025". The prices themselves could not be checked offline. metrics.py:92-133; `git show baec4f3` [trap] (verified: git diff)
- **[braid] Unknown or LiteLLM-style model ids are priced silently** — `get_model_config` falls back to `ModelConfig(model_id, 1.0, 2.0, "unknown")` with no warning. `"openai/gpt-4o-mini"` (the DSPy/LiteLLM form) and `"claude-sonnet-4-5"` hit the fallback; `"gpt-4o-mini"` does not. metrics.py:161-167 [trap] (verified: probe H3)
- **[braid] Token counts are typed by hand** — Usage is recorded as `track_usage(TokenUsage(500, 200), phase)`, and nothing in braid reads `lm.history`, DSPy usage tracking or LiteLLM usage. Every non-"planning" phase is priced at the solver model. A phase such as "critic" appears in the total but in neither bucket (total 0.002, planning 0, execution 0). metrics.py:14-25, 191-247 [trap] (verified: grep + probe H4) → here: lmrun.py
- **[braid] LatencyTracker** — A context manager around `time.perf_counter()` with an `elapsed_ms` property. metrics.py:463-480 [recipe] (verified: tests)
- **[prompting] Wrong cache env-var name** — `.env.example` sets `DSPY_CACHE_DIR=.dspy_cache` and `DSPY_LOG_LEVEL=INFO`. DSPy 3.3.1 reads `DSPY_CACHEDIR` (default `~/.dspy_cache`) and `DSPY_CACHE_LIMIT` (default 3e10 bytes), and no log-level variable, so both lines are inert. .env.example:8-9; dspy/clients/__init__.py:15-16, 60-61 [trap] (verified: grep of installed 3.3.1)
- **[prompting] Logging side effects** — `DebugLogger(log_file=…)` calls `logger.add(log_file, rotation="10 MB")` on the global loguru logger at every construction, so sinks duplicate. `duration_ms` is `time.time()` around a possibly cached call. `DebugInfo.memory_usage` and `token_counts` are never filled. thinking_traces.py:291-352 [trap] (verified: read)
- **[prompting] ProductionOptimizer's units are wrong** — It compares per-token cost (`cost_per_1k/1000`) against a per-request budget, and `1000/tokens_per_second` against `max_latency_ms`; `min_accuracy` is unused. For the repo's own distillation requirements it returns **gpt-4**, the teacher, as the production model, with `fallback_model` hardcoded to "gpt-3.5-turbo" and a per-token cost reported as `cost_per_request`. model_distillation.py:377-462, 500 [trap] (verified: probe S9)
- **[prompting] `async def` without `await`** — `DistillationPipeline.distill_and_deploy` is async and runs everything synchronously, blocking the event loop. README.md:314 awaits it. model_distillation.py:472-509 [trap] (verified: read)
- **[prompting] Demo output that is invented** — main.py:208-212 prints "Quality Retention: 92% / Cost Reduction: 85% / Speed Improvement: 4.2x" under `# Simulated result for demo` without calling the pipeline. main.py never configures an LM, so every other demo ends in "Demo error". [trap] (verified: read)
- **[prompting] A hardcoded cost table** — `_get_model_cost` holds gpt-4 0.03, gpt-3.5-turbo 0.002, claude-3 0.025 and claude-2 0.008 per 1K tokens, with unknown models at 0.01. model_distillation.py:290-300 [claim] (verified: read)

## TEST

- **[braid] The suite passes offline on 3.3.1, but the coverage gate fails** — `pytest tests/` gives **185 passed in 5.65 s** with no LM and no key. Coverage is **69.66 %** (1,648 statements, 500 missed), so the CI command's `--cov-fail-under=70` fails with pytest-cov 7.1.0 / coverage 7.16.1 ("FAIL Required test coverage of 70% not reached. Total coverage: 69.66%"). Per-file counts match the CHANGELOG (masking 18, validators 17, metrics 18, training 17; 185 total). .github/workflows/ci.yml:32; CHANGELOG.md:89-97 [number] (verified: pytest --cov on a git-archive copy)
- **[braid] Engine and critic are untested** — No test imports `braid.engine` or `braid.critic`. Their 25 % and 26 % coverage is class-definition lines. [trap] (verified: coverage report + grep)
- **[braid] Assertions that cannot fail** —
  - `len(labeled_edges) >= 0` (tests/test_parser.py:102);
  - `len(leaks) >= 0` (tests/test_masking.py:92);
  - `structure["edge_count"] >= 0` (tests/test_utils.py:186, 251);
  - `"error" in result or …`, where every return dict contains "error" (tests/test_integration.py:160);
  - no assertion at all (tests/test_masking.py:116-124, 126-134);
  - `score >= 0.0` (tests/test_optimizer.py:273, 289, 319, 334).

  [trap] (verified: read)
- **[braid] `try: … assert … except Exception: pass` swallows the test's own AssertionError** — tests/test_module.py:138-145 asserts `len(result.reasoning_steps) > 0` on a run with no LM. That run returns `valid=True` with 0 steps, so the assertion fails and is swallowed. The same pattern appears at tests/test_module.py:44-51, tests/test_generator.py:152-158 and 163-170, tests/test_integration.py:63-69, and tests/test_optimizer.py:374-383, 401-406, 416-421, 443-448, 459-464, 474-479 and 489-494. [trap] (verified: replayed the body of test_module.py:138-145 without the try → AssertionError)
- **[braid] No LM fixture anywhere** — No test configures an LM or uses DummyLM. The LM path is exercised only as the "No LM is loaded" error path. [trap] (verified: grep of tests/)
- **[braid] CI covers two DSPy major lines** — The matrix is 3.9/3.10/3.11 with `pip install -e ".[dev]"` (no lock) against `dspy-ai>=2.0.0`. DSPy 3.3.1 requires Python `>=3.10,<3.15`, so the 3.9 job gets DSPy 2.x; braid's own `uv.lock` pins 2.6.27 for <3.10 and 3.0.4 for ≥3.10. ci.yml:14, 25-28; uv.lock:906-911, 942-949 [number] (verified: read the lock + dspy-3.3.1 METADATA)
- **[braid] The documented API does not run** — 11 of 11 documented snippets fail on 3.3.1:
  - `NumericalMasker(placeholder_prefix=…)` → TypeError (docs/api.md:67-71);
  - `AtomicityValidator.suggest_split` → AttributeError (api.md:119; examples.md:354);
  - `GRDValidator(strict_mode=…)` → TypeError (api.md:130-133);
  - `StatefulExecutionEngine(max_iterations_per_node=3, enable_branching=True)` → TypeError (api.md:153-156);
  - `engine.has_cycles(grd)` → TypeError (api.md:165);
  - `CriticDetector.detect_critic_nodes` and `detect_feedback_loops` → AttributeError (api.md:185-189; examples.md:382, 388);
  - `CriticExecutor(max_retries=3)` → TypeError, missing `grd` (api.md:200);
  - `ValidationResult.suggestions` → AttributeError (api.md:432);
  - `dspy.OpenAI` → AttributeError;
  - `MIPROv2()` → TypeError.

  [trap] (verified: docs_snippets.py)
- **[braid] The examples, run offline** —
  - basic_usage.py's Example 2 prints "Answer: Error: No LM is loaded…" from a `valid=True` result;
  - gsm8k_example.py reports 100 % accuracy with 0 valid results;
  - optimization_example.py prints 0.000 metrics before and after, plus "Optimization completed (simple mode)".

  [trap] (verified: ran all three with no LM)
- **[prompting] No test suite, and the one pytest-collectable file cannot fail** — README.md:228 lists `tests/`, which does not exist. `test_notebooks.py` defines `test_notebook_structure`, `test_imports` and `test_basic_functionality`; they print ✅/❌ and `return` booleans. As a script it reports "2/3" (matplotlib is missing). Under pytest it reports "3 passed, 3 warnings" (PytestReturnNotNoneWarning: "Did you mean to use `assert` instead of `return`?"). `test_notebook_structure` returns True unconditionally (test_notebooks.py:56) and did not catch the escape-hatches notebook's broken import. [trap] (verified: ran as a script and under pytest)
- **[prompting] `validate_with_dspy.py` proves instantiation only** — It exits 0 with "✓ Basic functionality works" and zero LM calls. The "mock LM" named in its docstring is never created (validate_with_dspy.py:121-130). Its functionality checks print without asserting. `check_api_keys` reads `os.getenv` before calling `load_dotenv()`, so keys that exist only in `.env` are reported missing (validate_with_dspy.py:184-199). README.md:89 nonetheless says "FULLY VALIDATED". [trap] (verified: ran offline)
- **[prompting] Broken notebooks** — escape_hatches_deep_dive.ipynb's setup cell imports `UncertaintyAnalysis` (ImportError; the class is `UncertaintyResponse`), and its cell 11 reads `result['confidence']`, a key GracefulDegradation never returns (JSON lines 53, 359). technique_comparison.ipynb promises "all 11 advanced prompting techniques" (JSON line 9) and runs 6; it imports `TaskOrchestrator` and `MetaPromptOptimizer` without using them. [trap] (verified: import probe; parsed the JSON)
- **[prompting] An in-module offline fixture** — The evaluation module's `__main__` defines `MockCodeGenerator(dspy.Module)`, whose `forward` returns canned strings keyed on input substrings. It is a no-key fixture that runs the evaluator end to end, and it exposes the `custom_evaluator` bug. evaluation_framework.py:541-562 [recipe] (verified: probe T2)
- **[both] The offline harness used for this extract** — DSPy 3.3.1 `DummyLM` (`class DummyLM(BaseLM)`, `forward_contract = "legacy"`) returns list-of-dict answers formatted with the adapter's `[[ ## field ## ]]` headers and zero usage. It is a `BaseLM`, so it never passes through `dspy.LM`'s request-cache wrapper. To observe cache behavior:
  - patch the module-level `dspy.clients.lm.litellm_completion` with a counting fake that returns a `litellm.ModelResponse`;
  - call `dspy.configure_cache(enable_disk_cache=False)` so `~/.dspy_cache` is never written.

  `ChainOfThought` modules need a `reasoning` key in every DummyLM answer. dspy/utils/dummies.py:16-160; dspy/clients/lm.py:173-183, 209-262 [recipe] (verified: probes A1-A5, B1-B6, S2-S9) → here: lm_fixture.py

## PAT

- **[braid] Plan-then-execute: two Predicts and code in between** — Three stages:
  1. Plan: `Predict(BraidPlanSignature)(problem) -> grd`, a Mermaid string.
  2. Code: `MermaidParser.validate` → `parse` → `get_execution_order()`.
  3. Execute: for each node in order, up to `max_execution_steps=20`, `Predict(BraidStepSignature)(step_description=node.label, context="Problem: …\n\nPrevious Steps:\nStep i (id): result…")`.

  The executor never sees the diagram, the edges or the node's successors, and the context grows with every step. module.py:48-237 [pattern] (verified: probes B1, B4) → here: rlm_ingest.py (a model proposes structure, code walks it)
- **[braid] Answer selection** — `_extract_answer` returns the output of the first end node (end-node order comes from a set) if it is under 500 chars, else the last reasoning step, else all "id: result" lines. module.py:239-271 [pattern] (verified: read)
- **[braid] Node regexes are order-dependent and lossy** — NODE_PATTERNS try `[[..]]`, `[(..)]` (labelled STADIUM, actually Mermaid's cylinder), `((..))`, `{..}` **before** `{{..}}`, `(..)`, and `[..]` **before** `[/../]`; the first match per id wins. Results:
  - `H{{Prepare}}` → DIAMOND with label "{Prepare";
  - `S([Go])` → ROUNDED with label "[Go]";
  - `P[/Input/]` → RECTANGLE with label "/Input/";
  - `C[(Store)]` → STADIUM;
  - HEXAGON, CYLINDRICAL, TRAPEZOID and PARALLELOGRAM are never produced.

  parser.py:9-22, 104-113, 190-221 [trap] (verified: probe C2)
- **[braid] Parentheses inside a label create phantom nodes** — `Calc[Compute f(x) for x]` also yields a node `f` (label "x", ROUNDED) with no edges. It is both a start and an end node, and it is executed first (`['f', 'Calc', 'Done']`). The StructuralValidator would flag it as ORPHAN_NODES, but BraidReasoning never runs that validator. parser.py:110, 196-221 [trap] (verified: probe C1)
- **[braid] Edges the regexes miss** — Supported are `-->`, `==>`, `-->|label|` and `---|label|`. Failures:
  - chained `A --> B --> C` keeps only A→B;
  - `A & B --> C` keeps only B→C;
  - `A -- yes --> B` creates a node "yes" and an edge yes→B;
  - dotted `A -.-> B` and labelled thick `A ==>|go| B` produce no edge.

  parser.py:116, 223-270 [trap] (verified: probe C3)
- **[braid] Kahn's order silently drops cycles** — `get_execution_order` returns only nodes whose in-degree reaches 0. Every node on a cycle, and everything downstream of one, is omitted without an error. The README's own verification-loop shape (`Check -->|No| Calc`) therefore executes only `Start`: 1 of 4 nodes, 1 LM call, `valid=True`, with Start's output as the answer. parser.py:71-97; module.py:153-171 [trap] (verified: probes C4, B4) → here: graphrag.py (detect cycles explicitly before ordering)
- **[braid] Start and end order depend on PYTHONHASHSEED** — `_identify_start_end_nodes` iterates a `set`. For `S --> A; S --> B`, `end_nodes` is `['B','A']` under seeds 1, 2 and 4 and `['A','B']` under 3, 5 and 6, so which end node's output becomes the answer changes between processes. parser.py:272-286; module.py:254-260 [trap] (verified: probe C6 across 6 seeds) → here: graphrag.py (sort before emitting)
- **[braid] `validate()` is `parse()` minus the exception** — It accepts anything with a line starting "graph" or "flowchart" (case-insensitive). `"graph TD"` (0 nodes, empty order) and `"graphs are nice\nhello"` both return `(True, None)`. Only ValueError is caught. parser.py:186-188, 288-302 [trap] (verified: probe C5)
- **[braid] The stateful engine walks a single path** — It starts at `start_nodes[0]` only. At a node with several unlabelled edges it follows the first unlabelled one, so fan-out branches never run: `Start→A, Start→B, A→C, B→C` ran Start, A, C. Labelled edges are tried in order through `ConditionEvaluator`. On an exception it follows an edge labelled exactly "error", "failure" or "fail", else the first edge. engine.py:262-343, 368-420 [trap] (verified: probe D1)
- **[braid] Loop caps, and success after truncation** — `max_iterations_per_node=3`: the fourth visit is SKIPPED and ends execution with `success=False`. `max_total_steps=50` ends the loop silently and still reports `success=True` if the last node completed (A→…→E with max 2 steps ran A, B; success True; answer "out-B"). `ExecutionState.reset_for_retry` is never called. engine.py:63-72, 209-229, 281-343 [trap] (verified: probes D3, D4)
- **[braid] ConditionEvaluator semantics** — By condition type:
  - Keyword labels ("success/yes/true/valid/correct/pass/ok" vs "failure/no/false/invalid/incorrect/fail/error") are decided by `_is_success_result`: the last output contains none of "error", "failed", "invalid", "incorrect", "exception". So "yes" is True for "The answer is not correct".
  - Comparisons `(value|result)? op number` use the **last** number in the output ("about 150 or maybe 20" vs `> 100` → False).
  - "not contains X" is always True, because it searches for the literal "not  x".
  - Anything else is a substring test ("Maybe" in "maybe later" → True).

  engine.py:100-196 [trap] (verified: probe D2)
- **[braid] Cycle helpers** — `has_cycles()` is a DFS with a recursion stack. `detect_cycles()` enumerates from every node and returns rotations and duplicates: one 2-node cycle produced 3 entries. engine.py:456-505 [pattern] (verified: probe D5)
- **[braid] Critic nodes are found by label prefix, in English** — The patterns are `^Check[:\s]`, `^Verify[:\s]`, `^Double[- ]?check`, `^Validate[:\s]`, `^Ensure[:\s]`, `^Assert[:\s]`, `^Review[:\s]`, `^Examine[:\s]`, `^Inspect[:\s]`, `^Confirm[:\s]`, `^Make sure[:\s]` and `^Is this correct`, case-insensitive. "Please verify the sum", "Verification step" and "Prüfe das Ergebnis" are not critics. critic.py:56-112 [trap] (verified: probe E3)
- **[braid] The critic invents a retry edge** — If a critic node has no outgoing edge whose label matches `fail|error|retry|incorrect|wrong|no\s*$`, `_find_fallback_node` returns the first incoming node. A linear plan `Calc → Check[Verify: sum] → Answer` thus gets a Check→Calc retry loop that the diagram does not contain. After `max_retries=2` (3 evaluations; `retry_count` is shared across all critics), execution stops with `next_node=None`. The `critic_exceeded_retries` flag stays in the context, and `final_output` is the critic's own text ("This is wrong"). `max_total_steps=100` is hardcoded. critic.py:146-163, 294-389, 391-487 [trap] (verified: probe E2)
- **[braid] Numerical masking mechanics** — Patterns in priority order: currency ($ € £ ₺), percentage, speed, distance, weight, time, volume, scientific, fraction, decimal, integer. Placeholders `{{VALUE_n}}` are numbered in **reverse** position order, so the last match is VALUE_1. The README example gives `Calculate[Speed = {{VALUE_2}}] --> Answer[Result = {{VALUE_1}}]`, matching README.md:80. The class docstring's example is wrong: the actual output is `Calculate[{{VALUE_3}} ÷ {{VALUE_2}} = {{VALUE_1}}]`, with "60 km/h" masked as one unit. masking.py:38-80, 158-208 [pattern] (verified: probes F1, F2)
- **[braid] Exclusion by span overlap** — Before masking a match, the masker re-scans a ±10-char window with EXCLUDE_PATTERNS (`Step\s*\d+`, `Node\s*\d+`, `\bA\d+\b`, `\bB\d+\b`, `\bC\d+\b`, `flowchart\s+\w+`, `graph\s+\w+`). It excludes the match only when an excluded span overlaps the candidate span, not merely when it is nearby. masking.py:83-91, 130-145 [pattern] (verified: probe F7 — "Step 1" preserved) → here: quotes.py-style "don't flag inside a larger allowed pattern"
- **[braid] Unit regexes lack word boundaries** — Measured:
  - "Wait 5 minutes" → "Wait {{VALUE_1}}inutes";
  - "2 gallons" → "{{VALUE_1}}allons", "3 miles" → "…iles", "12 inches" → "…ches", "2 months" → "…onths";
  - "Put 3 in the box" → "Put {{VALUE_1}} the box".

  masking.py:67-71 [trap] (verified: probe F3)
- **[braid] `mask_grd_nodes` corrupts the value mapping** — It calls `mask()` per node, and `mask()` resets `_counter = 0`. Every node's placeholders therefore restart at `{{VALUE_1}}`, and `value_mapping.update` overwrites the earlier nodes. "Multiply 5 by 3 / Add 7 kg / Subtract 4" gives mapping `{VALUE_1: '4', VALUE_2: '5'}` and `mask_count=2`, and `unmask` returns "Multiply 5 by 4 / Add 4 / Subtract 4". Its problem-value guard skips any node containing the substrings "problem", "given", "input", "question", "if" or "when", and "Simplify", "Verify" and "Identify" all contain "if". masking.py:168, 295-349 [trap] (verified: probes F4, F5)
- **[braid] The leak detector double-counts; two parameters do nothing** — `detect_leakage` reports "Result = 60" both as `labeled_answer` and `equals_result`, so the README example yields 3 leaks for 2 values. `preserve_step_numbers` is stored and never read, so exclusions always apply. `min_value_to_mask` fails open when the numeric parse fails: "3 seconds" cleans to "3e" and is masked despite a threshold of 10. masking.py:93-108, 147-156, 258-293 [trap] (verified: probes F6, F7)
- **[braid] Structured validation issues** — `ValidationIssue(severity=ERROR|WARNING|INFO, code, message, node_id, suggestion)` sits inside `ValidationResult(valid, issues, score)` with `has_errors`, `get_errors` and `summary`. Codes: ATOMICITY_VIOLATION, EQUALS_VALUE, LABELED_ANSWER, UNIT_VALUE, COMPUTED_AGGREGATE, WEAK_SCAFFOLDING, TOO_FEW_NODES, TOO_MANY_NODES, INVALID_START_NODES, INVALID_END_NODES, ORPHAN_NODES, INVALID_EDGES. `validate_and_report` renders Markdown. validators.py:17-66, 215-232, 346-475, 543-585 [pattern] (verified: tests + probe G1) → here: quotes.py / state.py guards (machine code + message + location)
- **[braid] Mermaid extraction helpers** —
  - `extract_mermaid_code` takes the first ```` ```(?:mermaid)?\s*\n(.*?)``` ```` match, else the stripped text if it starts with "graph", "flowchart" or "sequenceDiagram", else None. It returns `""` (not None) when a non-mermaid fenced block precedes the mermaid one, and it accepts sequence diagrams that the parser rejects.
  - `parse_grd_structure` misses every edge whose source node carries a label (`A[Node A] --> B[Node B]` → no edges).
  - `format_grd_prompt` calls `str.format` after appending example GRDs, so a diamond `{…}` inside an example raises `KeyError`.

  utils.py:7-27, 54-85, 88-128 [trap] (verified: probe K1)
- **[braid] The protocol rule text is never sent by default** — `_build_prompt` holds:
  - the contrastive rules ("WRONG: 'Calculate[Speed = 60 km/h]' (contains the answer!) / RIGHT: 'Calculate[Divide distance by time]' (describes the action)", "Keep each node label UNDER 15 tokens", "Use verbs: Calculate, Identify, Extract, Compare, Verify, Apply");
  - three procedural few-shot GRDs;
  - `problem_type` and `custom_instructions`.

  In the default `use_dspy_predict=True` path none of it reaches the LM: 2 messages, no rules, no examples, no markers. generator.py:16-53, 194-251 [trap] (verified: probe A1) → here: pairs.py (rules belong in `signature.instructions`, examples in `predictor.demos`)
- **[prompting] Technique 1: the manager-style prompt** — `ManagerStylePromptConfig` has 12 required fields: role_title, department, company_context, reporting_structure, key_responsibilities, performance_metrics, tools_and_resources, communication_style, decision_authority, escalation_procedures, constraints, examples_of_excellence (title/situation/action/result/takeaway). A Jinja2 template renders it into a 7,329-char / 1,043-word document, passed as `manager_instructions` to `ChainOfThought(ManagerStylePrompt)`. The only mechanism is template rendering. Most of the text is fixed boilerplate, identical for every role: every responsibility gets the same three sub-bullets, every metric reads "This is a critical success factor for your role", every tool "Utilize this for maximum efficiency", plus "Start of Day / End of Day" procedures. manager_style.py:14-210 [pattern] (verified: probe S2)
- **[prompting] Technique 2: role prompting** — `RolePersona` (name, background, personality_traits, communication_style as a `PersonaTone` enum, domain_expertise, values, typical_phrases, knowledge_boundaries) becomes an f-string `role_description` for `ChainOfThought(RolePromptSignature)`. `knowledge_boundaries` turns into "You acknowledge when topics fall outside your expertise, specifically: …", which is prompt text only; nothing checks it. Only the first characteristic phrase gets its "- " bullet. role_prompting.py:14-92 [pattern] (verified: probe U8)
- **[prompting] Technique 3: task planning** — Inputs are `task_description, context, planning_guidelines`, and the output is `task_plan_json`. The guidelines cover decomposition, prioritisation, 1–10 complexity, acceptance criteria, risks and success metrics, followed by `TaskPlan(**json.loads(…))`. Execution: see AGENT. The model invents both the dependency graph and the acceptance criteria, and nothing checks the criteria after execution. task_planning.py:15-122 [pattern] (verified: probe S8)
- **[prompting] Technique 4: structured output** — `OutputSchema(format: XML|MARKDOWN|JSON|HYBRID, sections[tag, content, attributes, required], validation_rules, example)` is rendered into the `output_schema` input of `ChainOfThought(StructuredOutputSignature)`. Generation never validates or retries; `OutputValidator` is separate. Validators:
  - XML wraps the output in `<root>` and calls `ET.fromstring`. It names each missing required tag, fails on "AT&T", and loses nested child text (`[None]`).
  - Markdown: `##\s*{tag}\s*\n(.*?)(?=\n##|\Z)`.
  - JSON: `json.loads`, then key presence. Fenced JSON fails, and a scalar such as `5` raises TypeError.
  - Hybrid: `##\s*{tag}.*?<{tag}>(.*?)</{tag}>`. The code-review schema's own example fails 6 of 6 (Title-Case headers vs tag names), and 3 required sections are missing even after renaming.

  `_build_schema_description` prints `- <tag> (required): tag`, so the section descriptions never reach the model. structured_output.py:17-221, 224-297 [pattern] (verified: probe U1-U7) → here: job 2 (parse, then name the missing part)
- **[prompting] Parahelp-style tags** — `ParahelpStyleFormatter` formats and parses the fixed tags `analysis`, `approach`, `implementation`, `verification` and `manager_verify`, with `<!-- description -->` comments stripped on parse. It is pure Python: a `dspy.Module` with no `forward`. `StructuredDialogueFormatter` builds `<turn number=… speaker=…>` XML via `str.format` with no escaping. structured_output.py:300-374 [pattern] (verified: probe U9)
- **[prompting] Technique 5: meta-prompting** — Three `ChainOfThought` predictors:
  - analyzer: `prompt, example_outputs, task_context -> analysis_json`, parsed into `PromptAnalysis` with 0–10 clarity/specificity plus lists;
  - optimizer: `original_prompt, analysis, examples, optimization_guidelines -> optimized_prompt, changes_explanation`;
  - debugger: `prompt, expected_output, actual_output -> debug_analysis, suggested_fixes`.

  `optimize_prompt` hardcodes `confidence_score=0.8`, passes only examples with quality ≥ 8, and splits `changes_explanation` on newlines. The loop is under SKILL. meta_prompting.py:15-147 [pattern] (verified: probes S1, S6)
- **[prompting] Technique 6, few-shot: two stubs** — `AdaptiveFewShotLearner` picks a category by first-match keyword (error, security, performance, api, code, else "general"), updates an EMA of `0.8·old + 0.2·score` with prior 0.5, has no `forward`, and raises `KeyError: 'general'` when that pool is absent. `ChainOfThoughtFewShot.forward` builds a prompt and returns the literals ("Breaking down the problem systematically...", "Based on the analysis...") with **no LM call**. few_shot.py:323-405 [trap] (verified: probe S3)
- **[prompting] Technique 7: prompt folding** — `PromptFolder` has a generator (`parent_prompt, context (JSON of FoldingContext), folding_strategy -> sub_prompts_json`) and an executor (`prompt, context -> result`). It recurses until `remaining_depth <= 0` or `_is_atomic_prompt` (<10 words; or the substrings "specific", "calculate", "return"; or "?" and <50 chars). Strategies:
  - PARALLEL and RECURSIVE both run sequentially and merge into `{"merged_results": […], "summary": "Combined output from N sub-tasks"}`, with no LM synthesis;
  - PIPELINE stores the *previous* result as `step_n`, so the first stored value is None and the last result is never stored;
  - BRANCHING and ADAPTIVE have no branch in `_fold_recursive`.

  Failure modes:
  - a JSON-string reply is iterated **character by character**: `'"Do it"'` → 1 generation + 5 executions on "D", "o", " ", "i", "t";
  - a list of objects raises `TypeError: unhashable type: 'slice'`;
  - non-JSON text becomes one sub-prompt.

  `WorkflowFolder` builds `PromptNode` trees that nothing executes. prompt_folding.py:16-174, 219-338 [trap] (verified: probe S7)
- **[prompting] AdaptiveFolder routes on substrings** — `analyze_task` maps "step"/"first" → PIPELINE, "if"/"when" → BRANCHING, "simultaneously"/"parallel" → PARALLEL, >50 words → RECURSIVE, else ADAPTIVE. "Identify the key drivers of churn" → BRANCHING, from the "if" in "Identify", and BRANCHING then falls back to recursive. prompt_folding.py:341-383 [trap] (verified: probe S7)
- **[prompting] Technique 8, escape hatches: the prompt text** — An 8-point "UNCERTAINTY HANDLING GUIDELINES" block (admission, confidence phrasing, partial knowledge, clarifying questions, caveats, alternative interpretations, resource suggestions, patterns to avoid), with an optional "9. SOURCES", sent as `uncertainty_guidelines`. The rest of the technique (detector, degradation, hallucination and domain regexes) is keyword code; see MET and below. escape_hatches.py:158-218 [pattern] (verified: read) → here: job 2 entity-list prompt ("omit what you cannot point to")
- **[prompting] Hallucination and domain regexes** — `HallucinationPreventer` flags:
  - `\d{4}` (any 4-digit number: "port 8080"), `\d+%`, `\$[\d,]+`, dates, "according to", "study shows", "research indicates", "everyone knows";
  - more than 2 matches of `always|never|all|none` with no word boundaries: "Install it and call the small function usually." → "Multiple absolute statements".

  It only appends a disclaimer. `ContextualEscapeHatch.detect_domain` uses substrings in dict order: "issue" → legal ("sue"), "Is Spain nice in May?" → medical ("pain"), "economy" → personal ("my"), "lawn" → legal ("law"). escape_hatches.py:296-407 [trap] (verified: probe S4)
- **[prompting] Technique 9: thinking traces** — `ChainOfThought(ThinkingTraceSignature)` is `task, trace_instructions -> reasoning, thinking_trace, final_answer`, so the model reasons twice (CoT's `reasoning` plus the requested trace). Marker parsing:
  - [THOUGHT] [QUESTION] [HYPOTHESIS] [VERIFICATION] [DECISION] [ERROR] [INSIGHT] are recognised only at line start and case-sensitively; "- [THOUGHT] b", "1. [HYPOTHESIS] c", "**[INSIGHT]** d" and "[thought] e" all parse as OBSERVATION;
  - per-type confidences are constants (HYPOTHESIS 0.7, INSIGHT 0.9, others 1.0);
  - the result is a flat list; children, decision points and errors are never filled.

  `InteractiveDebugger.debug_prompt` returns `"output": "Execution result"` without executing anything. `create_code_debugging_trace` hardcodes the "solution" checkpoint `{"error": "even/odd logic reversed"}`. thinking_traces.py:93-215, 355-515 [trap] (verified: probes S1, S5)

## SKILL

- **[prompting] "Self-optimization" that never runs the candidate prompt** — `MetaPromptOptimizer.iterative_optimization` builds `PromptExample(output=expected_output, quality_score=8.0)` for every test case, so the prompt is never executed. `avg_score` is therefore always 8.0: `best_prompt` is set once, to the initial prompt, and never replaced, and `avg_score >= 9.0` never fires. Each iteration still spends 2 LM calls (analyze + optimize). With `max_iterations=3`: 6 LM calls, `optimized_prompt == "Summarize the text"` (the input), confidence 0.8. meta_prompting.py:149-193 [trap] (verified: probe S6) → here: job 4 (`gepa.optimize_anything` must score every candidate on data)
- **[prompting] Genetic "evolution" of prompt strings** — `mutate_prompt` applies one of five string edits with probability `mutation_rate` (0.3 default; 0.5 for the initial population):
  - append "For example: [specific example]";
  - `replace("should","MUST")`;
  - append "Follow these steps:\n1. First...\n2. Then...";
  - `replace("some","specifically")`: "Handle something awesome" → "Handle specificallything awespecifically";
  - append a bullet format.

  `crossover_prompts` interleaves lines by index parity. Selection always breeds the top two, with elitism of one. Fitness is a user callable, evaluated `population_size·generations + population_size` times (30 with the defaults). `self.optimizer = MetaPromptOptimizer()` is never used, and `random` is unseeded. meta_prompting.py:196-265 [trap] (verified: probe S6 + read)
- **[prompting] The self-critique loop stops only on exact equality** — `SelfCriticalPromptRefinement.iterative_refinement` stops when `refined == current_prompt`, which an LM practically never produces, so it always runs all `iterations=3` at 2 calls each. The critique instructions are packed into the `prompt` input, and the refiner receives the critique twice (inside `prompt` and as `critique`). meta_prompting.py:268-324 [trap] (verified: read)
- **[prompting] Schema-less JSON analysis** — `analyze_prompt` needs JSON that validates as `PromptAnalysis` (clarity and specificity as floats in 0–10, plus lists), guided only by the desc "JSON analysis of the prompt's effectiveness". Any mismatch raises `ValueError("Failed to parse analysis: …")`. meta_prompting.py:15-23, 43-49, 97-101 [pattern] (verified: probe S6 with valid JSON; read)
- **[braid] A "swappable example pool" that is never sent** — `GRDGenerator.examples`, `add_example()` and `get_template()` look like a tunable few-shot pool, but the default path never sends them. The text DSPy can tune is `signature.instructions` and `predictor.demos`. generator.py:71, 253-299 [trap] (verified: probe A1)

## TRAP

- **[braid] Step errors become answers while `valid` stays True** — Per-step exceptions are caught and stored as `step_results[node_id] = f"Error: {e}"`, the step is not added to `reasoning_steps`, and the result stays `valid=True`. Without an LM: `valid: True | answer: 'Error: No LM is loaded. Please configure…' | reasoning_steps: 0`. examples/basic_usage.py's Example 2 prints exactly this. module.py:214-237 [trap] (verified: probe B1)
- **[braid] Plans are truncated silently** — `execution_order[: self.max_execution_steps]` (20) drops the rest with no flag in the result. module.py:171 [trap] (verified: read)
- **[braid] The protocol modules are not wired in** — `BraidReasoning` uses only `GRDGenerator`, `MermaidParser` and two `Predict`s. `NumericalMasker` is instantiated in `SyntheticDataGenerator` and never called; `GRDValidator` is used only in training; `StatefulExecutionEngine`, `CriticExecutor` and `PPDAnalyzer` are exported and unused. README.md:156-188 nonetheless draws masking → validation → stateful engine → critic → PPD as phases of one flow. [trap] (verified: grep of braid/)
- **[braid] Dead code** — `BraidExecuteSignature`, `BraidReasoningSignature`, `utils.validate_mermaid_syntax`, `parse_grd_structure`, `format_grd_prompt`, `GRDGenerator.get_template` and `ExecutionState.reset_for_retry` are not used by the library. [trap] (verified: grep)
- **[braid] Metadata drift** —
  - `setup.py:8` says "0.1.6" while `pyproject.toml:7` and `__init__.py` say "0.2.3";
  - the CHANGELOG stops at 0.2.1, with no entries for 0.2.2 (prices) or 0.2.3 (annotations);
  - CHANGELOG.md:21 says "adding 7 new modules" and lists 6;
  - CONTRIBUTING.md:187 requires "type checking", which commit 87fbb1e removed from CI.

  [trap] (verified: read + git log)
- **[braid] Claims never measured** —
  - README.md:13 "significantly improves reliability and reduces hallucinations" (docs/index.md adds "compared to traditional Chain-of-Thought");
  - CHANGELOG.md:21 "implements the full BRAID protocol from the research paper", while the only reference is a vendor blog (README.md:337);
  - "≤15 tokens" as optimal (validators.py:73-75);
  - docs/examples/index.md:22 "See how BRAID-DSPy performs on GSM8K", followed by 2 problems and no numbers.

  No benchmark result exists anywhere in the repo. [claim] (verified: read)
- **[prompting] Claims never measured** —
  - README.md:3 "state-of-the-art prompting techniques used by top AI startups";
  - :14 "6+ page detailed prompts" (measured: 1,043 words);
  - :36 "Prompt evolution using genetic algorithms" (string templates);
  - :89-98 "FULLY VALIDATED … Core techniques functional with real LLMs" (no committed evidence; the offline validation makes no LM call);
  - :178 "Confidence: 0.15" (an impossible value).

  [claim] (verified: read + probes S2, T1)
- **[prompting] Stubs that return result-shaped constants** — `ChainOfThoughtFewShot.forward`, `InteractiveDebugger.debug_prompt`, `_extract_reasoning_steps`, `_identify_key_features`, `_evaluate_model_performance` ("# Simulated"), `optimize_prompt`'s `confidence_score=0.8`, and main.py's distillation demo. [trap] (verified: probes S3, S9 + read)
- **[prompting] Keyword checks presented as measurements** — This pattern recurs across the repo: escape-hatch confidence, degradation, hallucination flags, domain detection, the notebook's "Prediction Accuracy", the real-API quality flags and the notebook's security detection. In each, substring presence, without word boundaries, case handling or negation, decides a label that downstream code treats as a measured value. [trap] (verified: probes S4, T1)
- **[prompting] Declared dependencies versus actual imports** — requirements.txt and setup.py declare `openai`, `anthropic` and `jsonschema`, which no repo file imports. `pytest` is imported at runtime by the evaluation module (evaluation_framework.py:18), and `numpy` is used only for mean/std (model_distillation.py:15; evaluation_framework.py:16). [trap] (verified: grep)
- **[braid] `import braid` imports DSPy** — Even for parser-only use, since `braid/__init__.py:16-43` imports every submodule eagerly. [api] (verified: read)

## Code worth keeping

**1. [braid] Kahn's order, the shape to copy and the defect to know** — `braid/parser.py:71-97`. Pure Python; runs on 3.3.1. It silently omits every node on or downstream of a cycle (probe C4: nodes `Check, Start, Calc, Answer` → order `['Start']`). Pair it with an explicit cycle check and an error when `len(result) < len(nodes)`.
```python
    def get_execution_order(self) -> List[str]:
        """
        Get the execution order of nodes using topological sort.
        Returns a list of node IDs in execution order.
        """
        # Build adjacency list
        in_degree = {node.id: 0 for node in self.nodes}
        graph = {node.id: [] for node in self.nodes}

        for edge in self.edges:
            graph[edge.from_node].append(edge.to_node)
            in_degree[edge.to_node] = in_degree.get(edge.to_node, 0) + 1

        # Find start nodes (nodes with no incoming edges)
        queue = [node_id for node_id, degree in in_degree.items() if degree == 0]
        result = []

        while queue:
            node_id = queue.pop(0)
            result.append(node_id)

            for neighbor in graph[node_id]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        return result
```

**2. [braid] Exclusion by overlap, not proximity** — `braid/masking.py:130-145`. Pure Python; runs on 3.3.1 (probe F7: "Step 1" preserved, "5" masked).
```python
    def _should_exclude(self, text: str, match_start: int, match_end: int) -> bool:
        """Check if a match should be excluded from masking."""
        # Get surrounding context
        context_start = max(0, match_start - 10)
        context_end = min(len(text), match_end + 10)
        context = text[context_start:context_end]

        for pattern in self._exclude_compiled:
            if pattern.search(context):
                # Check if the excluded pattern overlaps with our match
                for exc_match in pattern.finditer(context):
                    exc_start = context_start + exc_match.start()
                    exc_end = context_start + exc_match.end()
                    if not (exc_end <= match_start or exc_start >= match_end):
                        return True
        return False
```

**3. [braid] Anti-pattern: a metric where correctness is worth +0.2 on top of an already-full score** — `braid/optimizer.py:486-519` (the body of `_default_metric`). Runs on 3.3.1. Probe I2: right, wrong, "Error: …" and "6" answers all score 1.000.
```python
        score = 0.0

        # GRD quality
        if result.parsed_grd:
            grd_quality = self.metrics.overall_quality(result.grd, result.parsed_grd)
            score += grd_quality * self.grd_quality_weight

        # Execution quality
        if result.reasoning_steps:
            # Check if we have reasonable number of steps
            step_count = len(result.reasoning_steps)
            if 2 <= step_count <= 15:
                step_score = 1.0
            elif step_count > 15:
                step_score = 0.5
            else:
                step_score = 0.0

            # Check if answer is present
            answer_score = 1.0 if result.answer else 0.0

            execution_score = (step_score + answer_score) / 2.0
            score += execution_score * self.execution_quality_weight

        # Answer correctness (if expected answer provided)
        if expected_answer and result.answer:
            # Simple string similarity (could be improved with semantic similarity)
            expected_lower = expected_answer.lower().strip()
            answer_lower = result.answer.lower().strip()

            if expected_lower in answer_lower or answer_lower in expected_lower:
                score += 0.2

        return min(score, 1.0)
```

**4. [braid] Anti-pattern: compiling the model's own outputs, without `with_inputs`, into a predictor the program never calls** — `braid/optimizer.py:381-418`. Runs on 3.3.1, and that is the problem. Probe B5: demos land on `plan` while `generator.predictor` keeps 0. Probe B6: BootstrapFewShot logs "Inputs have not been set…" and bootstraps 0 traces.
```python
    def _optimize_planning(
        self, module: BraidReasoning, trainset: List[Dict[str, Any]], metric: Callable
    ) -> BraidReasoning:
        """Optimize the planning (GRD generation) phase."""
        # Collect GRD quality metrics
        grd_scores = []

        for example in trainset:
            problem = example.get("problem", "")
            if not problem:
                continue

            # Generate GRD
            if module.use_generator and module.generator:
                gen_result = module.generator.generate(problem=problem)
                grd = gen_result.get("grd", "")
                grd_structure = gen_result.get("parsed_structure")
            else:
                plan_result = module.plan(problem=problem)
                grd = plan_result.grd
                try:
                    grd_structure = module.parser.parse(grd)
                except Exception:
                    grd_structure = None

            # Evaluate quality
            quality = self.metrics.overall_quality(grd, grd_structure)
            grd_scores.append({"problem": problem, "grd": grd, "quality": quality})

        # Use base optimizer if available
        if self.base_optimizer:
            # Optimize the plan signature
            plan_trainset = [
                dspy.Example(problem=ex["problem"], grd=ex["grd"]) for ex in grd_scores
            ]
            module.plan = self.base_optimizer.compile(student=module.plan, trainset=plan_trainset)

        return module
```

**5. [braid] Anti-pattern: a retry loop with identical inputs** — `braid/generator.py:103-108`. Runs on 3.3.1. Under `dspy.LM(cache=True)`, 3 attempts made 1 real completion (probe A5). Retries must change the request (e.g. `rollout_id` with temperature > 0) or run with the cache off.
```python
        for attempt in range(self.max_retries):
            try:
                if self.use_dspy_predict:
                    # Use DSPy's Predict API (recommended)
                    result = self.predictor(problem=problem)
                    raw_response = result.grd
```

**6. [prompting] A validator that names the missing part** — `src/techniques/structured_output.py:110-135`. Pure Python (stdlib `xml.etree`); runs on 3.3.1. Probe U1 passes the bug-report example; U3 shows it fails on "AT&T" (no escaping); U4 shows nested text lost (`[None]`).
```python
    @staticmethod
    def validate_xml(output: str, schema: OutputSchema) -> ValidationResult:
        """Validate XML-formatted output"""
        errors = []
        warnings = []
        parsed = {}

        try:
            root = ET.fromstring(f"<root>{output}</root>")

            for section in schema.sections:
                elements = root.findall(section.tag)
                if not elements and section.required:
                    errors.append(f"Missing required section: <{section.tag}>")
                elif elements:
                    parsed[section.tag] = [elem.text for elem in elements]

        except ET.ParseError as e:
            errors.append(f"Invalid XML: {str(e)}")

        return ValidationResult(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings,
            parsed_content=parsed
        )
```

**7. [prompting] Tier-forcing example selection (the policy, not the module)** — `src/techniques/few_shot.py:78-95`. Pure Python; runs on 3.3.1 (probe S3). Note that `input_text` is unused. In DSPy the chosen examples should become `predictor.demos`, not text in an input field.
```python
    def select_examples(self, input_text: str, selector: ExampleSelector) -> List[FewShotExample]:
        """Select relevant examples for the given input"""

        selected = []

        if selector.prioritize_challenging:
            challenging = [ex for ex in self.examples if ex.quality == ExampleQuality.CHALLENGING]
            selected.extend(challenging[:2])

        gold_examples = [ex for ex in self.examples if ex.quality == ExampleQuality.GOLD]
        selected.extend(gold_examples[:selector.max_examples - len(selected)])

        if len(selected) < selector.max_examples:
            other_examples = [ex for ex in self.examples
                            if ex not in selected and ex.quality != ExampleQuality.BRONZE]
            selected.extend(other_examples[:selector.max_examples - len(selected)])

        return selected[:selector.max_examples]
```

**8. [prompting] Anti-pattern: vacuous 1.0 defaults** — `src/evaluations/evaluation_framework.py:226-256`. Runs on 3.3.1. Probe T3: a suite that fails every test gets `overall_score() = 0.70`.
```python
        # Basic accuracy
        passed_results = [r for r in results if r.passed]
        accuracy = len(passed_results) / len(results) if results else 0.0

        # Type-specific metrics
        type_scores = defaultdict(list)
        for result in results:
            type_scores[result.test_type].append(result.score)

        edge_case_performance = np.mean(type_scores[TestCaseType.EDGE_CASE]) if type_scores[TestCaseType.EDGE_CASE] else 1.0
        robustness_score = np.mean(type_scores[TestCaseType.ROBUSTNESS]) if type_scores[TestCaseType.ROBUSTNESS] else 1.0

        # Consistency (variance of scores for similar test types)
        consistency_scores = []
        for test_type, scores in type_scores.items():
            if len(scores) > 1:
                consistency_scores.append(1.0 - np.std(scores))
        consistency_score = np.mean(consistency_scores) if consistency_scores else 1.0

        # Execution time
        execution_times = [r.execution_time_ms for r in results]
        avg_execution_time = np.mean(execution_times) if execution_times else 0.0

        # Calculate precision/recall (simplified)
        true_positives = len([r for r in passed_results if r.score > 0.8])
        false_positives = len([r for r in results if not r.passed and r.score > 0.5])
        false_negatives = len([r for r in results if r.passed and r.score < 0.5])

        precision = true_positives / (true_positives + false_positives) if (true_positives + false_positives) > 0 else 1.0
        recall = true_positives / (true_positives + false_negatives) if (true_positives + false_negatives) > 0 else 1.0
        f1_score = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0.0
```

**9. [prompting] Anti-pattern: an "optimizer" that never scores the candidate** — `src/techniques/meta_prompting.py:153-185`. Runs on 3.3.1. Probe S6: 6 LM calls, and it returns the initial prompt.
```python
        current_prompt = initial_prompt
        best_prompt = initial_prompt
        best_score = 0.0

        for iteration in range(max_iterations):
            examples = []
            total_score = 0.0

            for test_input, expected_output in test_cases:
                example = PromptExample(
                    input=test_input,
                    output=expected_output,
                    quality_score=8.0,
                )
                examples.append(example)
                total_score += example.quality_score

            avg_score = total_score / len(test_cases)

            if avg_score > best_score:
                best_score = avg_score
                best_prompt = current_prompt

            if avg_score >= 9.0:
                break

            analysis = self.analyze_prompt(current_prompt, examples)

            if not analysis.improvement_areas:
                break

            optimization_result = self.optimize_prompt(current_prompt, analysis, examples)
            current_prompt = optimization_result.optimized_prompt
```

**10. [prompting] Anti-pattern: case-mismatched keyword "confidence"** — `src/techniques/escape_hatches.py:60-96`. Runs on 3.3.1. Probe T1: "I don't know." → (NONE, 0.95), because the phrases are capitalised and the text is lowercased.
```python
        self.uncertainty_phrases = {
            UncertaintyLevel.LOW: [
                "likely", "probably", "seems to", "appears to", "suggests that",
                "generally", "typically", "usually", "often", "tends to"
            ],
            UncertaintyLevel.MEDIUM: [
                "might", "could", "possibly", "perhaps", "may", "potentially",
                "it's possible", "uncertain", "unclear", "debatable"
            ],
            UncertaintyLevel.HIGH: [
                "I'm not sure", "I don't know", "unknown", "cannot determine",
                "insufficient information", "no clear answer", "highly uncertain"
            ],
            UncertaintyLevel.UNABLE: [
                "I cannot", "I'm unable", "beyond my knowledge", "outside my expertise",
                "I don't have access", "I lack the information"
            ]
        }

    def detect_uncertainty(self, text: str) -> Tuple[UncertaintyLevel, float]:
        """Detect uncertainty level in text"""

        text_lower = text.lower()

        for level in [UncertaintyLevel.UNABLE, UncertaintyLevel.HIGH,
                     UncertaintyLevel.MEDIUM, UncertaintyLevel.LOW]:
            if any(phrase in text_lower for phrase in self.uncertainty_phrases[level]):
                confidence_map = {
                    UncertaintyLevel.UNABLE: 0.0,
                    UncertaintyLevel.HIGH: 0.2,
                    UncertaintyLevel.MEDIUM: 0.5,
                    UncertaintyLevel.LOW: 0.7,
                    UncertaintyLevel.NONE: 0.95
                }
                return level, confidence_map[level]

        return UncertaintyLevel.NONE, 0.95
```

**11. [prompting] Anti-pattern: a significance test fed cache-identical repeats** — `src/evaluations/evaluation_framework.py:418-434`. Runs on 3.3.1. Probe T4: t = 1.007e16, "significant", from 5 deterministic runs.
```python
        # Calculate statistics
        mean_a = np.mean(results_a)
        mean_b = np.mean(results_b)
        std_a = np.std(results_a)
        std_b = np.std(results_b)

        # Simple t-test approximation
        pooled_std = np.sqrt((std_a**2 + std_b**2) / 2)
        t_statistic = (mean_a - mean_b) / (pooled_std * np.sqrt(2/num_runs))

        # Determine winner
        if abs(t_statistic) > 2.0:  # Roughly 95% confidence
            winner = "A" if mean_a > mean_b else "B"
            significant = True
        else:
            winner = "Tie"
            significant = False
```

**12. [prompting] An offline fixture module inside the code it tests** — `src/evaluations/evaluation_framework.py:545-555`. Runs on 3.3.1 (probe T2: `python -m src.evaluations.evaluation_framework` completes offline).
```python
    # Mock prompt module for testing
    class MockCodeGenerator(dspy.Module):
        def forward(self, input_text: str) -> str:
            if "factorial" in input_text:
                return "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n-1)"
            elif "empty list" in input_text:
                return "def process_list(lst):\n    if not lst:\n        return []\n    return lst"
            elif "DROP TABLE" in input_text:
                return "# Sanitized input - no SQL injection"
            else:
                return "def generic_function():\n    pass"
```

**13. Not repo code: the cache-hit counter used for this extract** — `scratchpad/work/probe_braid_dspy.py` (section A5), condensed. Runs on 3.3.1 (probe A5: 1 completion with `cache=True`, 3 with `cache=False`). It makes no network call.
```python
import dspy, dspy.clients.lm as lm_mod
from litellm import ModelResponse
dspy.configure_cache(enable_disk_cache=False)       # never touch ~/.dspy_cache
calls = {"n": 0}
def fake_completion(request, num_retries, cache=None):
    calls["n"] += 1
    return ModelResponse(
        choices=[{"message": {"role": "assistant",
                  "content": "[[ ## grd ## ]]\nI refuse to draw a chart.\n\n[[ ## completed ## ]]"}}],
        usage={"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
        model="openai/probe-model")
orig = lm_mod.litellm_completion
lm_mod.litellm_completion = fake_completion          # dspy.LM.forward looks this name up per call
try:
    dspy.configure(lm=dspy.LM("openai/probe-model", api_key="not-a-key", cache=True))
    GRDGenerator(max_retries=3).generate(problem="retry-probe")
    print(calls["n"])                                  # -> 1 : retries 2 and 3 were cache hits
finally:
    lm_mod.litellm_completion = orig
```

## The old report, corrected

**braid-dspy.md (2026-09-23)**
- **"Targets … the pre-3.x DSPy API (`dspy.OpenAI`, `dspy.Predict`) — not verified against DSPy 3.3.1"** — Now verified. The library imports, and all 185 tests pass on 3.3.1 in 5.65 s. `dspy.Predict` is current API. Only the docs, README and the `module.py:39` docstring use the removed `dspy.OpenAI`. The report also said "the library code itself doesn't hardcode `dspy.OpenAI`", but the docstring does.
- **"185 … tests pass offline"** — True, but the report missed that the suite cannot fail in many places:
  - 11 tautological or assertion-free tests;
  - 12 try/except blocks that swallow assertions, one of which provably fails;
  - no tests for engine or critic (25 %/26 % coverage);
  - the CI gate `--cov-fail-under=70` fails at 69.66 %.

  It said "CI runs … with 70% coverage gate" as if that were green.
- **Idea #3 (Kahn's order, "[adopt]")** — It omitted the defect that matters: every node on or after a cycle is silently dropped. The README's own critic loop therefore executes 1 of 4 nodes and returns `valid=True`. Start/end order also depends on PYTHONHASHSEED.
- **Idea #4 ("StatefulExecutionEngine/BraidReasoning.forward refuse to execute an invalid plan")** — `BraidReasoning` never uses `StatefulExecutionEngine`. `validate()` accepts `"graph TD"` and even `"graphs are nice\nhello"`.
- **Ideas #10–12 (engine)** — Missed:
  - the engine is a single-path walker, so fan-out branches never run;
  - "not contains X" is always True;
  - `max_total_steps` truncation reports `success=True`;
  - `detect_cycles` returns duplicates;
  - `reset_for_retry` is dead.
- **Ideas #13–14 (critic)** — Right direction, but missed:
  - empty critic output passes (0.5);
  - ties count as failure ("no errors, … right" fails);
  - "not correct" passes;
  - a retry edge back to the previous node is invented when the plan has none;
  - after the retries run out, the critic's text becomes `final_output`.
- **Ideas #15–18 (PPD)** — Missed:
  - `efficiency_multiplier` is hardwired to 1.0 unless `baseline_accuracy` is passed, and README.md:130-131 and `generate_report` never pass it;
  - the PPD docstring scale is off by 100×;
  - LiteLLM-style ids (`openai/gpt-4o-mini`) are silently priced at $1/$2;
  - commit `baec4f3` deleted the "# Estimated" markers, which is stronger evidence than "gemini-3.0 looks speculative".
- **Idea #9 (masking)** — Missed the defects:
  - `mask_grd_nodes` resets the counter per node and corrupts round-trips ("Multiply 5 by 3" → "Multiply 5 by 4");
  - unit regexes without word boundaries ("5 minutes" → "{{VALUE_1}}inutes");
  - the "if" substring guard skips "Verify", "Simplify" and "Identify";
  - `preserve_step_numbers` is dead;
  - the class docstring example is wrong.
- **Idea #20–22 (training)** — Missed that any dataset holds only 5 distinct GRDs, that `create_dspy_examples` drops `expected_answer`, and the grammatical and float artefacts in the samples.
- **Idea #23 (GRDMetrics)** — Missed that an empty flowchart scores 0.68 and non-Mermaid text also 0.68, and that verbs are double-counted through node IDs.
- **Idea #24 ("[adopt]" — `BraidOptimizer` as a clean wrapper of DSPy optimizers)** — Wrong as a pattern to adopt:
  - it compiles `module.plan`, which the default `forward` never calls (verified: demos land on `plan`, planning calls carry 0 demos);
  - the trainset is the model's own unfiltered output;
  - the Examples lack `with_inputs`, so BootstrapFewShot bootstraps 0 traces;
  - the user metric is never passed on;
  - `num_threads` is ignored;
  - `_default_metric` gives a wrong answer 1.000.
- **Idea #25 (a two-tier prompt of "rules + swappable examples", "[adapt]")** — In the default path neither the rules nor the examples, `problem_type` or `custom_instructions` reach the LM (verified via DummyLM history).
- **Idea #26 (`extract_mermaid_code` "returns None … when nothing is found")** — It returns `""` when a non-mermaid fence comes first, and it accepts `sequenceDiagram`, which the parser rejects.
- **Idea #30 (a step error doesn't abort the run)** — The report missed the consequence: the error string becomes the answer, and `valid` stays True with 0 reasoning steps.
- **Missed entirely** —
  - retries under the DSPy cache (3 attempts → 1 completion);
  - `temperature` is never applied (`dspy.LM` has no `.temperature`);
  - the fallback path's `str(list)` bug;
  - the `__call__` override bypasses callbacks and usage tracking;
  - `named_predictors` cannot see `generator.predictor`;
  - 11 of 11 documented snippets fail;
  - `gsm8k_example.py` reports 100 % accuracy with 0 valid results;
  - the signature-annotation commit changed no prompt on 2.6.27, 3.0.4 or 3.3.1.

**dspy-advanced-prompting.md (2026-09-23)**
- **"every module in `src/` imports cleanly and runs its non-LM code paths under DSPy 3.3.1"** — The imports are correct (with `PydanticDeprecatedSince20` warnings). "Runs its non-LM code paths" is too generous:
  - the regression runner crashes on its 2nd run;
  - the suite's own `custom_evaluator` tests can never pass;
  - the hybrid validator rejects its own schema's example (6/6);
  - `AdaptiveFewShotLearner` raises `KeyError: 'general'`.
- **Idea #4 ("the one real mechanism", structured validators)** — Needs caveats:
  - `_build_schema_description` never sends the section descriptions;
  - `validate_xml` fails on `&` and loses nested text;
  - `validate_json` fails on fences and crashes on scalars;
  - `validate_hybrid` fails the schema's own example;
  - generation never validates or retries.
- **Idea #5 (meta-prompting "returns analysis_json as an opaque string with no parsing/validation shown")** — Wrong: `analyze_prompt` parses with `json.loads` and validates into `PromptAnalysis` (meta_prompting.py:97-101). The report missed the real defect: `iterative_optimization` always returns the initial prompt (hardcoded quality 8.0; verified 6 calls, input returned).
- **Idea #6 (few-shot tiers, "real, simple selection logic")** — Missed:
  - `input_text` is ignored (no similarity);
  - examples travel as input-field text, not DSPy demos, so optimizers cannot see them;
  - `ChainOfThoughtFewShot` is a stub returning literals without any LM call.
- **Idea #8 (escape hatches)** — Missed the case bug: the capitalised HIGH/UNABLE phrases never match lowercased text, so "I don't know" scores 0.95, and the guidelines' own recommended admission phrases also score 0.95. "could" and "may" trigger degradation of correct answers, and README's "0.15" cannot occur.
- **Idea #12 (distillation, "mostly scaffolding")** — Understated:
  - accuracies are hardcoded (0.95/0.88, "# Simulated");
  - the distilled prompt never reaches the student;
  - teacher and student are the same LM;
  - the adaptive loop always stops after 1 iteration;
  - ProductionOptimizer picks gpt-4;
  - main.py prints invented "92% / 85% / 4.2x".
- **Idea #13 (thinking traces, "[adapt]" the parser)** — Missed:
  - `ChainOfThought` already adds `reasoning`, so the model reasons twice;
  - markers after "- ", "1. " or "**" are not recognised;
  - `InteractiveDebugger` never executes anything.
- **Section 4 (vacuous metrics)** — Correct for edge, robustness, consistency and `test_coverage`. It missed that precision and recall also default to 1.0, which makes a 0 %-accuracy suite score **0.70** overall (verified). It also missed the A/B t-test exploding to 1e16 on deterministic repeats, and the regression runner crash.
- **"`.env.example` sets `DSPY_CACHE_DIR=.dspy_cache`"** — That variable is not read. DSPy reads `DSPY_CACHEDIR`, so the line does nothing. The cache is on anyway through `dspy.LM(cache=True)`.
- **"No committed test suite (…nothing under `tests/`)"** — Correct, and the README still lists `tests/`. It missed that `test_notebooks.py` is pytest-collectable and "passes" under pytest (3 passed) even when it reports a failure as a script.
- **Idea #7 (prompt folding, "[skip]")** — Fine as a verdict. It missed the character-by-character recursion on a JSON-string reply, the TypeError on a list of objects, the unimplemented BRANCHING and ADAPTIVE strategies, and the substring router sending "Identify…" to BRANCHING.
- **Missed entirely** —
  - the instructions are passed as input fields, so no DSPy instruction optimizer can tune them;
  - several `forward` methods return plain Python types;
  - JSON travels in untyped `str` outputs instead of typed Pydantic fields;
  - `RecursiveTaskPlanner` leaves dependencies dangling;
  - two notebook runtime errors (`UncertaintyAnalysis` import, `result['confidence']`);
  - `validate_with_dspy.py` checks the API key before calling `load_dotenv()`.

## Ten things the skill must say

1. A retry with identical inputs is a cache hit: 3 retries made 1 real completion. Retry with cache off, or with a new `rollout_id` and temperature > 0 → PROD "[braid] Retries under the request cache replay the same answer".
2. Optimize the predictor your program actually calls. Check `named_predictors()`: a predictor on a non-Module helper is invisible, and compiling the wrong one does nothing → OPT "[braid] BraidOptimizer compiles a predictor…", API "[braid] DSPy only tunes predictors reachable through Module attributes".
3. Build every trainset `Example` with `.with_inputs(...)`. Without it, BootstrapFewShot logs "Inputs have not been set…", bootstraps 0 traces and still installs raw demos → OPT "[braid] Examples built without `.with_inputs()`".
4. A metric must be able to fall. `_default_metric` scores a wrong answer 1.000, and vacuous 1.0 defaults give an all-failing suite 0.70 → MET "[braid] `_default_metric`…", MET "[prompting] A suite where every test fails scores 0.70".
5. Instructions belong in `signature.instructions` and examples in `predictor.demos`. Text passed as an input field, or built and never sent, can neither be optimized nor even reaches the LM → API "[prompting] Static instructions passed as input fields", PAT "[braid] The protocol rule text is never sent by default", DATA "[prompting] Examples are prompt text, not DSPy demos".
6. Type structured outputs. JSON inside a `str` field breaks on fences and has no schema, and a free-text "true" breaks on "True." → API "[prompting] JSON inside a `str` output field…", "[prompting] A free-text boolean compared as a string".
7. Keep DSPy's module contract: don't override `__call__`, and return a `dspy.Prediction`. Otherwise callbacks and usage tracking never see the module → API "[braid] Overriding `__call__`…".
8. Plans a model writes need explicit cycle and fan-out handling, plus deterministic ordering. Kahn silently drops cycles, the engine walks one path, and set iteration makes the answer node vary with the hash seed → PAT "[braid] Kahn's order silently drops cycles", "[braid] Start and end order depend on PYTHONHASHSEED", "[braid] The stateful engine walks a single path".
9. Keyword checks are not verification: case, negation and substring bugs turned "I don't know" into 0.95 confidence, "not correct" into a passed critique, and "issue" into a legal question → MET "[prompting] Escape-hatch confidence…", MET "[braid] Critic confidence…", PAT "[prompting] Hallucination and domain regexes".
10. Repeated runs need the cache off, or significance is fiction. Five cached-identical runs gave t = 1e16 → MET "[prompting] A/B significance from deterministic repeats". Also: a test that wraps its asserts in `try/except Exception` has none → TEST "[braid] `try: … assert … except Exception: pass`…".
