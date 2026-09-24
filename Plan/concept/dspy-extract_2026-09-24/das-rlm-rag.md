# dspy-agent-skills — RLM, graph and retrieval-package slice

## Header

- **Repo:** `github.com/netzkontrast/dspy-agent-skills`, commit `9d13f98` (checked out at `/home/user/dspy-agent-skills`, working tree clean before and after this read).
- **License:** MIT (`LICENSE:1-3`, „Copyright (c) 2026 Bryan Young"). Plugin version `0.11.0` (`.claude-plugin/plugin.json:3`).
- **DSPy targeted:** `dspy>=3.3.0,<3.4` (`requirements.txt:10-13`, floor raised because of the `dspy.RLM` rename). All DSPy API usage in this slice holds on 3.3.1: `scripts/check_dspy_surface.py --expected-version 3.3.1` prints „OK", all six dry-runs exit 0. Four of the six skills teach third-party packages (`dspy-rlm-hooks`, `drg-kg`, `dspy-refrag`, TARA), and several of their behavioural claims do **not** reproduce against those packages (sections TRAP and „The old report, corrected").
- **What the slice is:** six skills plus one scaffold. `dspy-rlm-module` covers `dspy.RLM`, the sandboxed-REPL long-context module. `dspy-rlm-workflow` is a DSPy port of a prose „rlm-workflow" (distill → decompose → solve → synthesize → verify → iterate). `dspy-rlm-hooks` covers a monkeypatching instrumentation package for RLM. `dspy-drg-kg` covers schema-first knowledge-graph extraction, `dspy-refrag` fragment selection with MMR, and `dspy-tara-rag` a self-corrective ReAct RAG with a 4D context score. `scaffolding/kp_canon_retriever.py` is an inert MMR-with-floor retriever sketched for a Kohärenz Protokoll layout that no longer exists.
- **What I ran to verify.** Everything ran offline, with every `*_API_KEY` unset. In every probe `litellm.completion` and `litellm.acompletion` were replaced by a raiser, and the drg/benchmark runs also had a dead `HTTPS_PROXY`. No LM call left the machine.
  - All six `example_*.py --dry-run` on DSPy 3.3.1 (`/home/user/kohaerenzprotokoll/.venv-dspy/bin/python`): exit 0, 0.04–1.8 s each.
  - `scripts/check_dspy_surface.py --expected-version 3.3.1`: OK. `pytest tests/` in a scratch venv: 633 passed in 0.97 s.
  - `inspect.signature` of `dspy.RLM`, `ProgramOfThought` and `CodeAct` on DSPy **3.2.1** (scratch venv) and on 3.3.1.
  - Read DSPy 3.3.1's `dspy/predict/rlm.py` (825 lines), `primitives/python_interpreter.py`, `code_interpreter.py`, `repl_types.py`, `runner.js`, `predict/refine.py`, `best_of_n.py` and `primitives/module.py`.
  - Probes (scratchpad `probe/*.py`):
    - `dspy.RLM` driven by `DummyLM` with a host-side mock interpreter: trajectory, extract fallback, call limit, SUBMIT errors, validation errors.
    - The same inside the **real Deno/Pyodide sandbox**. The shared venv carries the `deno` 2.9.7 PyPI package.
    - `dspy.Refine` failure counting.
  - `dspy-rlm-hooks==0.1.14` installed with DSPy 3.3.1 in a Python 3.12 scratch venv: the hooks example dry-run with the package present, the order trap probed on real RLM instances, source read, and the LM-free benchmark run.
  - `drg-kg` 0.1.2 from PyPI and from git (both commit `g4d6970bcc`): the drg example dry-run with the package present, then `extract_typed` probed without an LM, with `DRG_REQUIRE_LM=1` and with over-long text, plus the evaluation scorer with and without DSPy installed.
  - Cloned the upstream sources `dspy-refrag@a868813` and `self-corrective-rag@6c307f3`. Read the code the skills cite, then ran the pack's MMR against upstream `AdvancedSensor` on the pack's own fixture.
  - `__pycache__` directories my imports created in the repo were removed.

---

## API

- **`dspy.PythonInterpreter` exists in 3.2.1 too** — `hasattr(dspy, "PythonInterpreter")` is True on DSPy 3.2.1 and on 3.3.1, and `dspy.PythonInterpreter is dspy.primitives.PythonInterpreter`. The reference says the alias is 3.3.x-only: „the bare `dspy.PythonInterpreter` alias is 3.3.x-only" (`skills/dspy-rlm-module/reference.md:60`, repeated in `docs/CHANGELOG.md:40-41`). `dspy.utils.PythonInterpreter` is absent in both versions, as the reference says (`reference.md:57-59`). [trap] (verified: import on 3.2.1 and 3.3.1)
- **ProgramOfThought / CodeAct took the same move in 3.3.0** — 3.2.1: `ProgramOfThought(signature, max_iters=3, interpreter=None)`, `CodeAct(signature, tools, max_iters=5, interpreter=None)`. 3.3.1: `interpreter_factory=PythonInterpreter` in the constructor and `forward(self, interpreter=None, /, **kwargs)`. `skills/dspy-rlm-module/SKILL.md:66-68`, `reference.md:32-35`, pinned by `scripts/check_dspy_surface.py:159-167`. [api] (verified: inspect.signature on both versions) → here: `scripts/check_dspy_surface.py`
- **`dspy.Refine` signature and loop** — `Refine(module, N, reward_fn, threshold, fail_count=None)`. Each attempt runs a `deepcopy` of the module with `lm.copy(rollout_id=start+i, temperature=1.0)`, where `start = lm.kwargs.get("rollout_id", 0)`. It returns the first prediction with `reward >= threshold`, else the best one seen. `threshold=None` runs all N. `dspy/predict/refine.py:41-49,98-146`; the skill's description is at `skills/dspy-rlm-workflow/reference.md:111-121`. [api] (verified: read refine.py 3.3.1)
- **Refine's advice path** — after a below-threshold attempt that is not the last one, `dspy.Predict(OfferFeedback)` receives `program_code`, `modules_defn`, `program_inputs`, `program_trajectory`, `program_outputs`, `reward_code` (the **source** of `reward_fn`), `target_threshold`, `reward_value` and `module_names`, and returns `advice: dict[str, str]`. The next attempt wraps the adapter so every predictor receives `hint_ = advice.get(<its predictor name>, "N/A")` (`refine.py:15-38,121-130,148-167`). It never sees your metric's feedback string: the reward is a float. Advice keyed by any name the LM invents instead of the exact `named_predictors()` names degrades silently to „N/A". [api] (verified: read refine.py)
- **`fail_count=0` means N** — `self.fail_count = fail_count or N` (`refine.py:91`, `best_of_n.py:48`). You cannot ask for fail-fast with 0. [trap] (verified: probe, `Refine(..., N=2, fail_count=0).fail_count == 2`)
- **Refine returns `None` when every attempt raises and N ≤ 2** — failures are printed (`print(f"Refine: Attempt failed with rollout id {rid}: {e}")`). The check `if idx > self.fail_count: raise` runs before `self.fail_count -= 1` (`refine.py:170-174`). With an always-raising module: N=1 → `None`, N=2 → `None`, N=3 → raises on the third failure. The decrement also persists across calls on the same instance (fail_count 1 → 0 → −1 over three calls). The skill says only „`fail_count` (default `N`): how many attempts may raise before the error propagates" (`skills/dspy-rlm-workflow/reference.md:124`). [trap] (verified: probe on 3.3.1)
- **Refine needs source code** — `inspect.getsource(module.__class__)` and `inspect.getsource(reward_fn)` run in `__init__` (`refine.py:92-96`, with a `TypeError` fallback to `reward_fn.__class__` only). A module class defined in a stdin script raises `OSError: could not get source code` at construction. The skill: „define both in a file, not in a notebook cell or lambda" (`reference.md:125-126`). A lambda defined **in a file** works; the notebook case was not tested. [claim] (partly verified: stdin probe raised OSError; the example's nested class in a file constructs fine)
- **Refine/BestOfN fail on mixed per-predictor LMs** — `lm = self.module.get_lm() or dspy.settings.lm`. `Module.get_lm()` raises `ValueError("Multiple LMs are being used in the module. There's no unique LM to return.")` when the predictors hold different `lm`s (`dspy/primitives/module.py:198-216`). `mod.set_lm(lm_)` then overwrites every predictor's LM with the temperature-1.0 copy (`refine.py:107-109`). A judge predictor with its own cheap LM therefore cannot sit inside a Refine-wrapped module. [trap] (verified: read module.py/refine.py)
- **`BestOfN` = Refine without advice** — the same rollout/temperature loop and threshold break, no `OfferFeedback`, no `getsource` (`dspy/predict/best_of_n.py:36-83`). `threshold=None` makes `reward >= None` raise inside its try block. `skills/dspy-rlm-workflow/SKILL.md:148-149`. [api] (verified: read best_of_n.py)
- **Calling `forward` directly logs a warning** — `Module.__getattribute__` logs „Calling module.forward(...) on X directly is discouraged. Please use module(...) instead." whenever `forward` is not reached through `__call__` (`dspy/primitives/module.py:336-348`). The canonical workflow recurses with `self.forward(...)` (`skills/dspy-rlm-workflow/SKILL.md:91`, `example_rlm_workflow.py:102`), so every recursion warns and bypasses `__call__` (callbacks, usage context). Use `self(...)`. [trap] (verified: read module.py)
- **`dspy.Prediction` unpacks with `**`** — `dspy.Prediction(plan=1, **pred)` works (mapping protocol), as the canonical program uses in `return dspy.Prediction(plan=plan, sub_results=results, **merged)` (`SKILL.md:98`). With `ChainOfThought`, `merged` also carries `reasoning`. [api] (verified: probe)
- **DSPy 3.3.1 LM error hierarchy** — `LMError` has these subclasses:
  - `LMProviderError`, with `LMAuthError`, `LMBillingError`, `LMRateLimitError`, `LMServerError`, `LMTimeoutError` and `LMInvalidRequestError` (the last with `ContextWindowExceededError` and `LMUnsupportedModelError`);
  - `LMConfigurationError`, with `LMNotConfiguredError`;
  - `LMTransportError`, `LMUnexpectedError` and `LMUnsupportedFeatureError`.

  `AdapterParseError` is a separate `DSPyError`, and an exception raised inside a patched `litellm.completion` surfaces as `LMUnexpectedError`. [api] (verified: introspected `dspy.utils.exceptions`) → here: `scripts/lmrun.py` statuses (`AdapterParseError` → unparsed, provider/transport errors → unreachable)
- **DSPy logger** — the `dspy` logger is set to INFO and writes to **stderr** through `DSPyLoggingStream`. `dspy.disable_logging()` silences it (`dspy/utils/logging_utils.py:40-66`). [api] (verified: read; verbose RLM output appeared on stderr)

## OPT

- **RLM inside a module, GEPA on the whole** — wrap `dspy.RLM` in a `dspy.Module` beside other predictors and compile with `dspy.GEPA(metric=...).compile(student=..., trainset=..., valset=...)`. `skills/dspy-rlm-module/SKILL.md:80-97` (the `RepoAuditor` example). [recipe]
- **What GEPA can mutate in an RLM** — an RLM has exactly two predictors, `generate_action` and `extract` (`named_predictors()` → `['generate_action', 'extract']`). `generate_action`'s instruction is the entire REPL template: `ACTION_INSTRUCTIONS_TEMPLATE`, the task docstring and the tool docs, built once in `__init__` (`dspy/predict/rlm.py:336-389`). A GEPA run therefore rewrites DSPy's own REPL rules, not only „the RLM's outer signature instruction" (`SKILL.md:82`). [api] (verified: probe listing predictors and fields)
- **The cascade is the GEPA metric** — `dspy.GEPA(metric=verify_cascade, auto="light", reflection_lm=dspy.LM("openai/gpt-5", temperature=1.0, max_tokens=32000))`, then `.compile(student=RLMWorkflow(), trainset=..., valset=...)`. `skills/dspy-rlm-workflow/SKILL.md:151-157`. Per-module blame comes from feedback text that names the sub-problem or module, which GEPA reads with `pred_name` set (`reference.md:104-106`, `SKILL.md:159-160`). [recipe]
- **Budget knobs** — `max_depth` 1 for prototypes, 2 by default, 3 only with `track_usage=True`. `Refine` at `N=3` with `threshold` set to the score you would ship at (0.85–0.9). The distiller's `max_llm_calls` 20–50. GEPA `auto="light"` first, because the cascade is expensive per example. The judge model is cheaper than the task LM. `skills/dspy-rlm-workflow/reference.md:128-136`. [recipe]
- **Runtime vs compile-time iteration** — `dspy.Refine` at runtime (re-runs with advice), `dspy.BestOfN` for sampling without advice, GEPA at compile time on the same metric (`SKILL.md:136-160`). Anti-pattern: re-decomposing on every iteration. Only re-decompose when Tier 2 blames the decomposition (`SKILL.md:180`). [pattern]
- **drg-kg optimizer is opt-in** — `drg.optimizer.optimize_extractor(training_data, *, config=KGOptimizerConfig(...), extractor=None, schema=None)`. The default is `optimizer_type="bootstrap"` (also `labeled_few_shot`, `mipro`, `copro`), with a composite metric weighting entities 0.6 and relations 0.4. Normal extraction never compiles. `skills/dspy-drg-kg/reference.md:106-115`. [claim]
- **TARA compiles only the generator** — `experiments/run.py:_apply_optimization` finds the `generator` attribute (`ChainOfThought(QnAGenerateSignature)`), and only a variant with `optimization: bootstrap|mipro` compiles (only `configs/experiment/rq5.yaml`). The metric is `token_f1(prediction.answer, example.answer)`, the trainset is cached at `data/optimization/{dataset}_trainset.json` and needs ≥3 examples. `optimize_mipro(...)` is `auto="light"` only, and `num_candidates`/`max_demos` are accepted but not passed through. `skills/dspy-tara-rag/SKILL.md:118-121`, `reference.md:112-124`. [claim]

## MET

- **The verification cascade** — three tiers, fail-fast, returning `dspy.Prediction(score, feedback)` through the five-argument metric signature `(gold, pred, trace=None, pred_name=None, pred_trace=None)`:
  - Tier 1 failing returns `0.3*t1`.
  - Tier 2 below 0.8 returns `0.3 + 0.4*t2`, so the score stays under 0.62.
  - Otherwise the score is `0.3 + 0.4*t2 + 0.3*t3`.

  The weights are syntactic 0.3, semantic 0.4 and pragmatic 0.3. `skills/dspy-rlm-workflow/SKILL.md:118-134`, `reference.md:92-102`. [pattern] (verified: example dry-run, good=1.00, bad=0.00) → here: `scripts/rlm_ingest.py` verification tiers, `scripts/pairs.py` metric
- **What each tier checks, per the reference** —
  - Tier 1: Pydantic validation, required fields, lint/compile for code, a well-formed `contradictions` list.
  - Tier 2: tests or gold comparison, every `success_criteria` item addressed, every sub-result referenced, contradictions listed when sub-results disagree.
  - Tier 3: an LM judge on a cheaper model with a written rubric.

  „The prose skill's 'Overall Confidence 0–100 %' is `score * 100`." `reference.md:94-102`. [pattern]
- **The example's cascade is thinner than the prose** —
  - Tier 1 is binary: `(1.0 if not problems else 0.0)`, so `0.3*t1` is always 0 on failure (`skills/dspy-rlm-workflow/example_rlm_workflow.py:113-123`).
  - Tier 2 is a case-insensitive substring test of each success criterion against `pred.answer` (`:130-132`).
  - Tier 3 is a constant: „Tier 3 (pragmatic) would be an LM judge; the smoke test treats it as passed." (`:136-137`).
  - The coverage check („every `[id]` appears in `answer` or `gaps`", `reference.md:143`) and „Tier 2 checks it is non-empty when sub-results disagree" (`SKILL.md:178`) exist only in prose.

  [trap] (verified: read example, dry-run)
- **Feedback must name the culprit** — „Feedback strings must say *which sub-problem or module* failed and *what good looks like*". „A verifier that returns only a float — GEPA has nothing to learn from." `reference.md:104-106`, `SKILL.md:176`. [pattern]
- **Fast-fail ordering is a cost rule** — „a schema error at Tier 1 is free to catch, expensive at Tier 3" (`SKILL.md:177`), with Tier 3 on a cheaper model (`SKILL.md:133-134`). [pattern]
- **The drg-kg scorer cannot score vacuously** — `_prf(tp, fp, fn)` returns precision, recall and F1 = 0.0 whenever its denominator is 0, so empty gold with empty prediction scores 0.0, not 1.0. `_score_sets` does multiset (`Counter`) matching on keys normalised by `strip().lower()`, and records `false_positive_keys` and `false_negative_keys` in `details`. From the installed package, not from the skill: `drg/evaluation/_runner.py:33-34,149-181`. [api] (verified: `_prf(0,0,0)` → all 0.0; `_score_sets` of one gold against two predictions → P 0.5, R 1.0, F1 0.6667, FP key `('juna', 'person')`) → here: the drg scorer the target uses (`.venv-dspy`; CLAUDE.md: „whose `_prf` returns **0.0** where the retired pipeline's `coverage()` returned 1.0")
- **The drg scorer runs without DSPy** — `from drg.evaluation._runner import _score_sets, _prf` imports in a venv holding `drg-kg==0.1.2` and no DSPy. `import drg.extract` there raises `ModuleNotFoundError: No module named 'dspy'`. It does not import `drg.extract` and so never triggers LM auto-configuration. [api] (verified: scratch venv without DSPy)
- **drg evaluation surface** — `BenchmarkRunner(...).evaluate(datasets, runner=fn)`, `compare_reports`, `render_markdown_report`, `evaluate_ontology`, `evaluate_graph_quality`, and CLI `drg eval run dataset.json`, `drg eval compare baseline.json candidate.json`. „Declared stable for the alpha series." `skills/dspy-drg-kg/reference.md:147-149`, `SKILL.md:144`. [claim]
- **TARA's 4D context score** — relevance 0–30, coverage 0–25, specificity 0–25, sufficiency 0–20, summing to 100. Each dimension localises a different failure: wrong passages, missing pieces, too general, unanswerable. `skills/dspy-tara-rag/SKILL.md:52-66`. The example's `weakest()` picks the minimum of score/ceiling (`example_tara.py:57-65`) and maps it to a repair (`:68-73`). [pattern] (verified: dry-run; good 88, thin → sufficiency, wrong → relevance)
- **TARA: the LLM does the arithmetic** — `EvaluationSignature` has the LLM emit `total_score` itself. `pipeline/loop.py` substitutes the dimension sum only when `total == 0` and the sum is > 0 (`skills/dspy-tara-rag/reference.md:71-74`; upstream `agentic_rag/pipeline/loop.py:302-308`). Any other disagreement between `total_score` and the dimensions passes. [trap] (verified: read upstream loop.py@6c307f3)
- **Judge a self-corrective design against baselines** — five pipelines share one retriever and loader: `naive`, `crag`, `loop`, `ircot`, `agentic`. „A self-corrective design that is not measured against `naive` and `loop` is unfalsifiable." The repo's own results: gain on 2WikiMultiHopQA, not significant on HotpotQA and FinanceBench. `skills/dspy-tara-rag/SKILL.md:85-100,144-145`. [claim]
- **Speedups need equivalent steps** — the `dspy-rlm-hooks` benchmark asserts step equivalence across variants. „a speedup only counts when every variant ran the same steps with the same results", and a high `evicted` count relative to `claimed` means wrong predictions (`skills/dspy-rlm-hooks/SKILL.md:124-129`, `reference.md:101-102`). The CLI exits 1 when steps differ (`dspy_rlm_hooks/benchmark/report.py:183`). [pattern] (verified: benchmark run, „steps identical across variants: True")

## DATA

- **The distilled context is an input** — „Either way the distilled text is an *input* to `RLMWorkflow`, so the workflow is testable with a hand-written distillation." `skills/dspy-rlm-workflow/SKILL.md:115-116`. [pattern] → here: `scripts/lm_fixture.py`-style fixtures
- **Gold for the cascade** — `dspy.Example(problem="rate limiting", success_criteria=["sliding window", "redis"])`, called directly with no `with_inputs` (`example_rlm_workflow.py:169`). [recipe]
- **Record exclusions and compute compression** — report `compression = len(distilled) / len(original)`, target 10–20 %. Record what was excluded as a list output „so the verifier can check that nothing named in `success_criteria` was dropped". `reference.md:82-85`. SKILL.md says the ratio is „computed from token counts" (`SKILL.md:25`) while the reference uses `len()` of strings, i.e. characters (`reference.md:82`): pick one. [pattern]
- **Distill by size** — for ≤ ~100k tokens, run a `Distill` signature per chunk (`chunk, query -> relevance: Literal[0,1,2,3], excerpt`, chunks by heading or ~2k tokens): keep the 3s, summarise the 1–2s, drop the 0s. For > ~100k tokens, run `dspy.RLM("context, query -> distilled", sub_lm=cheap, max_llm_calls=30)`. `SKILL.md:105-116`, `reference.md:75-85`. [recipe]
- **Complexity classes** — *constant*: one step, decomposition buys nothing; *linear*: N independent sub-tasks; *quadratic*: N tasks with N interactions. „Decompose only linear and quadratic problems." `reference.md:40-42`. [pattern]
- **TARA datasets** — `scripts/prepare_datasets.py --dataset {hotpotqa|2wikimultihopqa|musique|financebench|all} --sample N`. Sources: `hot_pot_qa` distractor validation, `framolfese/2WikiMultihopQA`, `bdsaglam/musique`, and `PatronusAI/financebench` (train, CC-BY-NC-4.0). The runs use 150–200 questions per dataset. `experiments/run.py --dataset` defaults to `popqa`, which `prepare_datasets.py` no longer exposes, so always pass it. `skills/dspy-tara-rag/reference.md:97-110`, `SKILL.md:115-116,127`. [claim; the default is verified at upstream `experiments/run.py:678`]
- **drg text limit** — `extract_typed` raises `ValueError("Input text is too long (100,001 chars). Maximum allowed: 100,000 chars (set DRG_MAX_TEXT_CHARS to override).")` before any LM call. The limit is overridable by env, not „hard" as `skills/dspy-drg-kg/reference.md:128` says. Chunk and use `extract_from_chunks(chunks, schema)`. [api] (verified: probe with 100,001 chars)

## RLM

- **What `dspy.RLM` is** — a `dspy.Module` marked `@experimental` („This class may change or be removed in a future release without warning."). An outer LM writes Python in a REPL and sees the output, iterating until it calls `SUBMIT(...)`. It reaches semantics by calling a sub-LM with `llm_query(prompt)` / `llm_query_batched(prompts)`. Reference: „Recursive Language Models" (Zhang, Kraska, Khattab, 2025). `dspy/predict/rlm.py:1-9,115-137`; `skills/dspy-rlm-module/SKILL.md:9`, `reference.md:5`. [api] (verified: read source)
- **„Recursive" means depth one** — `llm_query` calls the sub-LM with a **raw prompt string** (`target_lm(prompt)`, `rlm.py:276-296`): no signature, no adapter, no REPL, no nested RLM. The sub-LM must return `dspy.LMResponse` or a non-empty list, otherwise `TypeError`. [api] (verified: probe; the DummyLM sub-LM received raw prompts)
- **Constructor, 3.3.1** — `RLM(signature, max_iters=20, max_llm_calls=50, max_output_chars=10_000, verbose=False, tools=None, sub_lm=None, interpreter_factory=PythonInterpreter)`. `rlm.py:139-149`; taught correctly at `skills/dspy-rlm-module/SKILL.md:43-57`, `reference.md:9-23,37-48`. [api] (verified: inspect.signature 3.3.1; `example_rlm.py:35-55` asserts the names)
- **Forward, 3.3.1** — `forward(self, interpreter=None, /, **input_args)` and `aforward` with the same shape. A caller-owned interpreter is the first **positional** argument. Passing `interpreter=` as a keyword raises `TypeError("To use a caller-owned interpreter, pass it as the first positional argument when calling the module.")` (`rlm.py:425-430,701`). [api] (verified: probe)
- **The 3.2.x → 3.3.0 renames** — 3.2.1: `RLM(signature, max_iterations=20, max_llm_calls=50, max_output_chars=10000, verbose=False, tools=None, sub_lm=None, interpreter=None)` and `forward(self, **input_args)`. 3.3.x: `max_iters` and `interpreter_factory`, with the instance moved to the call. Both are hard `TypeError`s on the wrong version. `SKILL.md:59-68`, `reference.md:25-35`. [api] (verified: inspect.signature on 3.2.1 and 3.3.1) → here: `scripts/check_dspy_surface.py`, `scripts/rlm_ingest.py`
- **`max_iters`** — the maximum number of REPL iterations; each costs one outer `generate_action` call. The prompt shows `iteration` as `"i/max_iters"` (`rlm.py:677-681`). [api]
- **At `max_iters` the RLM does not fail; it fabricates an ending** — when the loop exhausts `max_iters` without `SUBMIT`, `_extract_fallback` logs WARNING „RLM reached max iterations, using extract to get final output". It then calls a second predictor, `extract`, over `variables_info` and `repl_history`, and returns an ordinary `Prediction` with `final_reasoning="Extract forced final output"` (`rlm.py:543-562,735-736`). No exception, and every output field is filled. The reference's failure row „`RLM hit max_iters`" (`reference.md:98`) does not exist. [trap] (verified: probe B, 2 action calls + 1 extract call; final_reasoning as quoted) → here: `scripts/rlm_ingest.py` must map `final_reasoning == "Extract forced final output"` to „never reached" (P15), never to an answer
- **`max_llm_calls` caps only sub-LM calls** — the counter is per `forward()` (fresh closure), is incremented by `llm_query` (1) and `llm_query_batched` (`len(prompts)`, checked **before** any call), and raises `RuntimeError("LLM call limit exceeded: {n} + {k} > {max}. Use Python code for aggregation instead of making more LLM calls.")` (`rlm.py:261-325`). It does not count the outer action calls or the extract call. The worst case per forward is `max_iters` action calls + 1 extract + `max_llm_calls` sub-calls, plus an adapter retry for each unparsable action. The reference calls it „Hard cap across the whole RLM invocation" (`reference.md:43`). [trap] (verified: probe C)
- **Exceeding `max_llm_calls` does not stop the run** — the `RuntimeError` is raised inside the sandbox. If uncaught, it becomes the step's output `"[Error] RuntimeError: ['RuntimeError: LLM call limit exceeded: 2 + 1 > 2. ...']"` and the loop continues; the model can still `SUBMIT`. Calls made earlier in the same failing block are spent, and their prints are lost. The reference's „`Sub-LM call count exceeded`" message (`reference.md:101`) does not exist. [api] (verified: probe C mock + real sandbox, sub-LM calls actually made = 2 with max 2)
- **`llm_query_batched`** — at most 8 threads (`_make_llm_tools(max_workers=8)`, not configurable), with the contextvars copied into each thread. A per-prompt `dspy.LMError` becomes the string `"[ERROR] <message>"` in the result list, and other exceptions propagate (`rlm.py:305-323`). Prompt text tells the model the sub-LM has „~500K char capacity" (`rlm.py:62`) whatever the actual `sub_lm` window is. [api] (verified: read; probe 4)
- **`sub_lm`** — defaults to `dspy.settings.lm` at call time. If both are None, `llm_query` raises `dspy.LMNotConfiguredError("No LM configured. Use dspy.configure(lm=...) or pass sub_lm to RLM.")` (`rlm.py:276-281`). The skill's advice: a cheaper model for inner calls (`SKILL.md:14,103`). [api] → here: `scripts/rlm_ingest.py` (pass it explicitly so the choice is visible)
- **`max_output_chars` truncates only in the prompt** — `REPLHistory.format()` renders each output head+tail: `"Output ({raw_len:,} chars):"` header, `max_output_chars//2` characters from each end, and `"... ({omitted:,} characters omitted) ..."` between (`dspy/primitives/repl_types.py:111-125`). The stored entry and `result.trajectory` keep the full output. The reference's „`Output truncated at 10000 chars`" (`reference.md:102`) is not a real message. [api] (verified: probe, stored 30 chars with cap 10)
- **Each input's preview is in every prompt** — `REPLVariable.from_value(..., preview_chars=1000)` puts `"Variable: \`name\` (access it in your code)"`, `Type`, the field `desc` and `constraints` if set, `"Total length: N characters"`, and a preview into every action prompt. The preview is 500 head chars + "..." + 500 tail chars, JSON-dumped with indent 2 for dicts and lists (`repl_types.py:26-95`). „Pass data as kwargs, not in the instruction" (`SKILL.md:104`) is right, but ~1 kB of every input still reaches the outer LM on each iteration. [api] (verified: probe, preview length 1003 for a 1200-char input)
- **Input variables are re-injected every iteration** — `_execute_code` calls `repl.execute(code, variables=dict(input_args))` on every step (`rlm.py:654-664`), and `PythonInterpreter` prepends `name = <literal>` assignments to the code (`python_interpreter.py:692-715`). A reassignment such as `context = context.upper()` is undone on the next iteration. Other names do persist („State persists between iterations"). [trap] (verified: real sandbox, step 1 printed `ALPHA`, step 2 `alpha`)
- **An input field named `json` breaks the default sandbox** — `PythonInterpreter._inject_variables` rejects `key == "json"` with `CodeInterpreterError: Invalid variable name: 'json'` (`python_interpreter.py:695-696`), a terminal error. `dspy.RLM("json -> answer")` still constructs, with only a pydantic UserWarning. [trap] (verified: probe)
- **Reserved names** — tools may not be named `llm_query`, `llm_query_batched`, `SUBMIT` or `print`. Input fields may not use those names or collide with a tool, and output fields may not be `trajectory` or `final_reasoning`. The messages are `ValueError: Input fields conflict with built-in sandbox functions: ['print']`, `Output fields conflict with RLM result metadata: ['trajectory']`, `Tool name 'SUBMIT' conflicts with built-in sandbox function`, and `Input fields conflict with user tools: ['context']` (`rlm.py:188-238`). [api] (verified: probe)
- **The tools contract, construction** — `tools` must be a **list** of callables or `dspy.Tool`. A dict raises `TypeError("tools must be a list, not a dict. Change tools={'name': func} to tools=[func] (tool names are inferred from function names, or use dspy.Tool(func, name='custom_name'))")`. Duplicate names raise `ValueError("Duplicate tool name 'grep'")`, and names must be identifiers and not keywords (`rlm.py:192-225`). [api] (verified: probe)
- **The tools contract, the prompt** — tool docs are appended as „Additional tools available (use these instead of standard library equivalents):" with lines of the form ``- `grep(pattern: string)` - <docstring or "No description">``. Types come from the JSON schema and the description from the docstring (`rlm.py:240-259`). Write docstrings: the prompt says „No description" otherwise. [api] (verified: probe)
- **The tools contract, the call** — the sandbox defines a Python wrapper per tool whose signature is rebuilt from the host function. It keeps parameter names, annotations only for `str/int/float/bool/list/dict/None`, and defaults as JSON literals. It forwards to the host as **kwargs** (`runner.js:44-65`, `python_interpreter.py:461-475,505-538`). Positional calls inside the sandbox therefore work (`count('alpha')`), but positional-only, `*args` or non-JSON defaults break. [api] (verified: real sandbox, `count('alpha')` → `int 100`) → here: `scripts/rlm_ingest.py` tools `find_line`, `count`
- **Tool return values** — `None` or `str` arrives as a string. Anything else is JSON-encoded (`json.dumps(..., allow_nan=False)`), so an int stays an int and a tuple becomes a list, with a fallback to `str()`. Pydantic models, dataclasses and namedtuples are dumped to dicts (`python_interpreter.py:186-214,518-525`). A host-side tool exception reaches sandbox code as `RuntimeError("<ExcType>: <message>")` (`runner.js:184-191`, wrapper `:62-63`). Async tools are awaited. A tool may not call `execute` on its own interpreter: `CodeInterpreterError("PythonInterpreter cannot execute recursively from one of its tools.")` (`python_interpreter.py:773-774`). [api] (verified: read; int preserved in probe)
- **What the result looks like** — `Prediction(<output fields parsed with parse_value>, trajectory=[{"reasoning": str, "code": str, "output": str}, ...], final_reasoning=str)`. The last trajectory output is `"FINAL: {...}"` on SUBMIT. `final_reasoning` is the last action's reasoning, or „Extract forced final output" (`rlm.py:627-641,558-562`). [api] (verified: probes A–E; keys `['answer', 'final_reasoning', 'trajectory']`)
- **Step outputs you will see** —
  - `"(no output - did you forget to print?)"` for empty stdout (`rlm.py:420-423`).
  - `"[Error] <Type>: [args]"` for code errors.
  - `"[Error] Expected Python code but got \`\`\`javascript fence. Write Python code, not javascript."` for a non-Python fence (`rlm.py:81-112`).
  - `"[Error] Missing output fields: ['n']. Use SUBMIT(answer, n)"` when a SUBMIT dict lacks fields.
  - `"[Type Error] n: expected int, got str: ..."` for unparsable values (`rlm.py:564-598`).

  All of these are recoverable: the loop continues. [api] (verified: probes D, E; real sandbox)
- **SUBMIT is a typed function in the real sandbox** — `SUBMIT(answer: str, n: int)` is generated from the output fields (`runner.js:70-90`). Positional `SUBMIT('x', 3)` works, and a missing argument surfaces as `"[Error] TypeError: [\"SUBMIT() missing 1 required positional argument: 'n'\"]"`. SUBMIT raises `_DSPyFinalOutput(BaseException)` (`runner.js:23-25`), so `except Exception:` in model code does not swallow it. Prints in the same block as SUBMIT are discarded. [api] (verified: real sandbox)
- **An expression at the end replaces printed output** — the runner returns the value of the block's last expression if it is not None, and stdout otherwise (`runner.js:342-346`). `print('x')\nlen(context)` reports `1100`, and the print is lost. [trap] (verified: real sandbox)
- **Code fences** — `_strip_code_fences` accepts ```` ```python ````, `py`, `python3`, `py3` or bare fences and strips outer decorative fence pairs (`rlm.py:78-112`). The action signature asks for ```` ```python\n<code>\n``` ```` (`rlm.py:368`). [api]
- **An unparsable action aborts the run** — `generate_action` is a `dspy.Predict`. A response neither ChatAdapter nor its JSONAdapter fallback can parse raises `AdapterParseError` out of `rlm(...)`, after two LM calls for that step, and so does any `LMError` from the outer LM. Nothing catches either (`rlm.py:666-695`). [api] (verified: probe 2, 3 outer calls then AdapterParseError) → here: `scripts/lmrun.py` status `unparsed`
- **`verbose=True`** — logs „RLM iteration i/max\nReasoning: ...\nCode:\n..." and non-final outputs, truncated head+tail, via `logger.info` of `dspy.predict.rlm`, i.e. to **stderr** (`rlm.py:650-651,682-686`). It is not „stdout" as `reference.md:45` says. Error outputs are not logged. [api] (verified: probe 4 captured stderr)
- **`interpreter_factory`** — a zero-argument callable, invoked per `forward()` (possibly concurrently); DSPy shuts down every interpreter it creates (`rlm.py:162-165,519-537`). Passing an instance raises `TypeError("interpreter_factory received an object that already implements CodeInterpreter, so its ownership is ambiguous. ...")`, and a non-callable raises `TypeError("interpreter_factory must be a zero-argument callable that creates a CodeInterpreter, not int.")` (`code_interpreter.py:150-162`). A factory may expose an `execution_instructions` string that is added to the action prompt (`rlm.py:354-357`). [api] (verified: probe)
- **A caller-owned interpreter keeps state across calls** — `rlm(interp, ...)` injects fresh tools but never resets the namespace or shuts the interpreter down (`rlm.py:526-530`). A variable set while processing document one is visible while processing document two. Reuse only „sequentially", never across overlapping invocations (`SKILL.md:67-68`). [trap] (verified: real sandbox, call 2 read `secret == "document-ONE"`)
- **The `CodeInterpreter` protocol** — a `runtime_checkable` Protocol with a `tools` dict property, `start()` (idempotent), `execute(code, variables=None)` returning `FinalOutput`, str, list or None, and `shutdown()` (`code_interpreter.py:51-147`). Errors: `CodeExecutionError` is recoverable; a bare `CodeInterpreterError` is terminal (process or protocol failure) (`:18-29`). You do not have to subclass anything: a structural match passes `isinstance`. The reference says „subclass `dspy.primitives.CodeInterpreter` and implement its four members" (`reference.md:62-65`). [api] (verified: a non-subclassing mock passed and ran RLM end to end)
- **The default sandbox** — `PythonInterpreter` runs Pyodide **0.29.4** (`npm:pyodide@0.29.4/pyodide.js`) under Deno, and also imports `https://deno.land/std@0.186.0/io/mod.ts` (`runner.js:3-4`). A cold `DENO_DIR` therefore needs network on first start. Deno runs with `--no-config --no-lock --node-modules-dir=false`, reads only the runner and the Deno cache (the cache read is revoked after start), and gets no env, net or write access unless `enable_env_vars`, `enable_network_access` or `enable_write_paths` are given (`python_interpreter.py:243-336`, `runner.js:144-146`). „subprocesses and native extensions are unavailable" (`:346-350`). [api] (verified: read; sandbox ran)
- **The Deno requirement in 3.3.x** — DSPy 3.3.1 declares the extra `deno = ["deno<3.0.0,>=2.4.5"]` (dspy METADATA lines 56-57; there is no such extra in 3.2.1) and prefers that package's binary (`from deno import find_deno_bin`) over `PATH` (`python_interpreter.py:84-94`). It requires Deno `>=2.0.0,<3.0.0` (`:39-41,124-138`). Missing Deno raises `CodeInterpreterError: Unable to determine the Deno version from 'deno'. PythonInterpreter requires Deno >=2.0.0,<3.0.0. Install a compatible runtime with \`pip install "dspy[deno]"\`, or pass a custom \`deno_command\`.` The skill teaches `brew install deno` and `which deno` (`SKILL.md:13,107`, `reference.md:53,97`). `which deno` is empty when Deno comes from the pip package, so it gives a false negative. [trap] (verified: missing-Deno message on 3.3.1 in a venv without the package; the shared venv found `.venv-dspy/bin/deno` 2.9.7 with nothing on PATH)
- **Sandbox cost** — a fresh `PythonInterpreter` start plus first execution took 2.9 s. A whole 6-iteration RLM run with a scripted LM took 3.3 s. The default factory pays this per `forward()`. [number] (verified: real sandbox, this container, warm Deno cache)
- **`PythonInterpreter` is single-thread** — using one instance from a second thread raises `RuntimeError("PythonInterpreter is not thread-safe and cannot be shared across threads. Create a separate interpreter instance for each thread.")` (`python_interpreter.py:384-393`). Variables whose Python-literal form exceeds 100 MB go through the virtual filesystem (`/tmp/dspy_vars/{k}.json`), because „Pyodide's FFI crashes at exactly 128MB" (`:36-38,698-713`). [api] (verified: read)
- **Custom mounts** — `enable_read_paths` and `enable_write_paths` mount files at `/sandbox/<basename>` and require unique basenames. With `sync_files=True` (default), write paths are copied back to the host after each execution. Write paths may not overlap the runner or the Deno dir (`python_interpreter.py:274-310,426-459`). [api]
- **Usage accounting** — with `dspy.configure(track_usage=True)`, `result.get_lm_usage()` returns a dict keyed by model, and sub-LM calls go through the same tracker (`llm_query_batched` copies contextvars into its threads). `reference.md:91`. [claim] (partly verified: probe returned usage under `'dummy'`, but the outer and sub DummyLM share that name, so separation was not shown)
- **When to use RLM** — below 100k tokens, when the answer fits one call → `Predict`/`ChainOfThought`; external tools → `ReAct`; math or code that must run → `ProgramOfThought`; a huge context, recursive chunking or a data-exploration loop → `RLM`; whole-codebase reasoning → RLM with file tools. „Using RLM when a 32k-token prompt would fit — overhead is not worth it." `SKILL.md:70-78,115`. [recipe]
- **Budget rule** — „Keep `max_llm_calls` tight (20–50) in production; raise for research." „`max_llm_calls` left at default in a production path — runaway cost." `SKILL.md:101,117`. The example uses `max_iters=10, max_llm_calls=20` (`example_rlm.py:25-32`). [recipe]
- **DSPy's own REPL prompt** — the action prompt includes the rule „MINIMIZE RETYPING (INPUTS & OUTPUTS) - When values are long, precise, or error-prone (IDs, numbers, code, quotes), re-access them via variables and parse/compute in code instead of retyping" (`rlm.py:73`). It also says „SUBMIT ONLY AFTER SEEING OUTPUTS" (`:74`) and „You have max {max_llm_calls} sub-LLM calls" (`:76`). The first rule is P26 inside DSPy. [api] → here: `scripts/rlm_ingest.py` (still verify every cited line in code)
- **Secrets** — „Passing secrets in the `context` string — they get echoed into REPL state." (`SKILL.md:118`). The preview and outputs also reach the outer LM's prompt. [claim]
- **dspy-rlm-hooks 0.1.14, the package** — MIT, Development Status 3 (Alpha), `Requires-Python >=3.12`, `dspy>=3.1.0`, `pydantic>=2.0.0`, extras `predict-rlm` and `tracing` (`mlflow>=2.14.0`). `skills/dspy-rlm-hooks/SKILL.md:18-20`, `reference.md:6-7,119-123`. [api] (verified: METADATA of the installed wheel)
- **The hooks API** — `enable_rlm_hooks(rlm, *, pre_iteration_hook=None, pre_execution_hook=None, post_execution_hook=None, post_iteration_hook=None)`, all keyword-only, one callable per stage. Calling it again replaces the hooks rather than appending. The positional hook signatures are:
  - `pre_iteration(iteration, variables, history, input_args)` → `PreIterationOutput`;
  - `pre_execution(iteration, code, variables, history, input_args)` → `PreExecutionOutput(code)`;
  - `post_execution(iteration, code, result, variables, history, input_args)` → `PostExecutionOutput(result)`;
  - `post_iteration(iteration, pred, code, result, history)` → `PostIterationOutput(history, stop=False)`.

  `SKILL.md:54-63`, `reference.md:20-37`. [api] (verified: inspect.signature on 0.1.14; the example's `assert_api_surface` passed with the package installed)
- **`PreIterationOutput` fields** —
  - `extra_vars={}` is merged into the input variables for this iteration, so it goes through the same literal injection and the same `json` restriction.
  - `python_code=""` is prepended this iteration only.
  - `persistent_python_code=None` replaces `repl.repl_globals`: `""` clears it, `None` keeps it. It lives on the interpreter, so the default factory loses it at the next forward.
  - `prompt_context=""` is appended to `variables_info` as „Additional context for this iteration (instructions only; not a Python variable):".

  `dspy_rlm_hooks/core/patcher.py:136-157`, `core/utils.py:8-28`; `SKILL.md:65-68`. [api] (verified: read source)
- **Hook lifecycle** — `pre_iteration → generate_action → pre_execution → execute → post_execution → post_iteration` (`patcher.py:129-131`). `pre_execution` is skipped when fence stripping fails. `post_iteration` runs only when the step did not finish, i.e. never on the SUBMIT step (`patcher.py:208`). [api] (verified: read)
- **`stop=True` looks like hitting `max_iters`** — `PostIterationOutput(stop=True)` calls `self._extract_fallback(...)` (`patcher.py:217-218`), which yields the same WARNING and `final_reasoning="Extract forced final output"` as running out of iterations. A hook-stopped run is indistinguishable from a max-iters run in the result. [trap] (verified: read)
- **What `enable_rlm_hooks` validates and patches** — it raises `AttributeError: RLM instance missing required attributes: ... Ensure you are passing a dspy.RLM instance from dspy>=3.1.` when `_execute_iteration`, `_aexecute_iteration`, `_process_execution_result`, `generate_action`, `verbose`, or `max_iters`/`max_iterations` is absent (`patcher.py:73-102`). It binds `_execute_iteration`, `_aexecute_iteration` and `_execute_code` per instance with `MethodType` (`patcher.py:398-400`), and `disable_rlm_hooks` deletes those instance attributes (`:424-434`). When MLflow is importable, the top-level `enable_rlm_hooks` switches to `enable_rlm_hooks_with_tracing` (`dspy_rlm_hooks/__init__.py:72-95`). `enable_predict_rlm_hooks` is exported from `dspy_rlm_hooks.core` only (`reference.md:17-18`). [api] (verified: probe; error text as quoted)
- **The ordering trap, confirmed** — enabling hooks then speculation leaves `_execute_code` as `_speculation_execute_code` (both active). Enabling speculation then hooks leaves `_execute_code` as the hooks' `_execute_code`, so speculation is inactive while `generate_action` is still the `_StreamingGenerateAction` wrapper: a half-patched instance. Calling `disable_rlm_speculation` then `disable_rlm_hooks` restores `RLM._execute_code` and `Predict`. The package documents the order itself („The reverse order (Order 2) leaves speculation inactive because `enable_rlm_hooks` overwrites `_execute_code`", `speculation/integration/api.py:25-32`). `skills/dspy-rlm-hooks/SKILL.md:92-94`. [trap] (verified: probe on real `dspy.RLM` 3.3.1 instances)
- **Speculation defaults** — `enable_rlm_speculation(rlm, *, tools=None, max_inflight=8, max_dispatches_per_turn=2048, speculate_llm_query=True, speculate_llm_query_batched=True, speculate_user_tools=False, timeout_s=5.0, streaming=True, persistent_shadow=True, latency_aware=True)`. `SpeculationConfig` has `enabled=True` plus the same fields. `SpeculationPolicy(speculatable=False, pure=False, deterministic=False, latency_hint_ms=1000.0, gate=None)`. `speculative(fn, *, name=None, deterministic=False, latency_hint_ms=1000.0)`. `speculate(tool, *, policy=None, **policy_kwargs)`. `reference.md:50-74`. [api] (verified: inspect on 0.1.14)
- **Purity guard** — `speculate(f, speculatable=True, pure=False)` raises `ValueError: tool '<lambda>': speculatable=True requires pure=True — a tool with observable side effects must never execute early`. `speculative()`-wrapped tools are **always** speculated, regardless of `speculate_user_tools` (`api.py:161`). The tool name must equal its REPL registration name, or every speculation is evicted (`reference.md:76-77`). [api] (verified: probe)
- **LM-free benchmark** — `python -m dspy_rlm_hooks.benchmark --variants default spec [hooks|module:fn ...] --repeats N --tool-ms 60 --llm-ms 150 --pace-ms 1.0 --json-out f.json`. It scripts `generate_action`, fakes the tools and the sub-LM, reports wall, generate, execute, tool-critical and tool-serial time with speculation counters, and exits 1 when steps differ (`benchmark/report.py:140-183`). `Scenario(name, iterations, tools, llm_latency_ms=150.0, max_llm_calls=50)`, `ScriptedIteration(reasoning, code)`, `ToolPlan(name, latency_ms, result)` (`benchmark/scenario.py:18-45`). It executes the scripted code in the real `PythonInterpreter`, so „no API key and no LM are needed — dspy must be installed" (`skills/dspy-rlm-hooks/SKILL.md:120-122`) leaves out the Deno requirement: with Deno off PATH the run dies with `CodeInterpreterError: Unable to determine the Deno version from 'deno'. …`. [api] (verified: ran it with and without Deno on PATH)
- **Measured on this container** — default scenario, 3 repeats, Deno on PATH, no LM:

  | variant | wall median | stdev |
  |---|--:|--:|
  | default | 4.339 s | 0.197 |
  | spec | 3.399 s | 0.853 |
  | hooks (no-op) | 4.823 s | 0.954 |

  Speedup of spec: wall x1.277, tool-critical x2.3. Hooks: x0.9, within noise at 3 repeats. Spec dispatched 8 and claimed 8, with 0 evicted; steps identical across variants. [number] (verified: ran it)

## RAG

- **drg-kg is extraction, not retrieval** — „DRG is **not** a GraphRAG, RAG or retrieval stack. It produces a graph artifact." `skills/dspy-drg-kg/SKILL.md:20-24`. PyPI name `drg-kg`, import name `drg`. The unrelated PyPI package `drg` is a Medicare grouper (`reference.md:3-5`). Python `>=3.10,<3.14`. [claim]
- **drg install matrix** — `pip install drg-kg` gives the schema, graph, validation, versioning and evaluation layers; `[dspy]` adds extraction; `[extract]` adds `tiktoken` on top. Other extras: `neo4j`, `api`, `mcp`, `openai`, `gemini`, `openrouter`, `local`, `louvain`, `leiden`, `spectral`, `networkx`, `coreference`, `all`, `dev` (`reference.md:9-16`). Without DSPy, `import drg.extract` fails with `ModuleNotFoundError: No module named 'dspy'`, as the skill says (`SKILL.md:97`, an `ImportError` subclass). `requirements-extras.txt:37` pins `drg-kg[dspy]>=0.1` with no upper bound. [api] (verified: base venv) → here: `.venv-dspy` (installed for the scorer only)
- **The schema is the contract** — `EnhancedDRGSchema(entity_types=[EntityType(name, description, examples=[], properties={})], relation_groups=[RelationGroup(name, relations=[Relation(name, src, dst)])])`. An empty description raises `SchemaError: EntityType description cannot be empty`, and a `RelationGroup` needs at least one relation. Triples outside the schema are dropped. `SKILL.md:36-66`. [api] (verified: probe for SchemaError)
- **An inferred schema is a draft** — `generate_schema_from_text(corpus_sample)`. „Treat an inferred schema as a draft. It decides what can ever be extracted." `SKILL.md:59-66,151`. [pattern]
- **Extraction path** — `entities, triples = extract_typed(text, schema)`, then `kg = build_enhanced_kg(entities_typed=entities, triples=triples, schema=schema, source_text=text)` and `kg.save_json("graph.json")`. `build_enhanced_kg` lives in `drg.graph.builders`, is not top-level, and is keyword-only: positional use raises `TypeError: build_enhanced_kg() takes 0 positional arguments but 2 were given`. `SKILL.md:68-82`, `reference.md:48-54`. [api] (verified: probe)
- **`extract_typed` defaults** — `enable_entity_resolution=True`, `enable_coreference_resolution=False`, `enable_implicit_relationships=True`, `embedding_provider=None`, `return_enriched=False`, `min_confidence=None`, `filter_negated=True`, `enable_reverse_relation_fallback=False`, `lm=None`. „`enable_implicit_relationships` defaults to **True** (it adds LLM-inferred edges you did not state)." `SKILL.md:84-88`, `reference.md:34-38`. [api] (verified: inspect on 0.1.2) → here: never use drg extraction for wiki links (links are never inferred, decision 005); if ever used, pass `enable_implicit_relationships=False` and an explicit `lm=`
- **`extract_from_chunks` defaults** — `enable_cross_chunk_relationships=True`, `enable_entity_resolution=True`, `enable_coreference_resolution=False`, `enable_implicit_relationships=True`, `enable_cross_chunk_context_snippets=True`, `max_cross_chunk_context_chunks=3`, `cross_chunk_snippet_chars=350`, `max_cross_chunk_context_chars=1200`, `min_anchor_entity_len=3`, `max_anchor_entities=8`, `two_pass_extraction=True`, and more. The `_async` variants are `asyncio.to_thread` shims (`reference.md:40-46,59`). [api] (verified: read drg/extract/__init__.py:1070-1086)
- **`build_enhanced_kg` defaults** — `filter_against_schema=True`, `prune_isolated_nodes=True`, `filter_redundant_relations=True`, `confidence_strategy="default"` (`reference.md:48-54`). „Nodes disappear | Isolated nodes are pruned by default" (`SKILL.md:99`). [api] (verified: grep of drg/graph/builders.py:434-435)
- **Windowed extraction multiplies calls without a flag** — it is active when `len(chunks) >= DRG_WINDOWED_RELATION_CHUNK_THRESHOLD` (6) or `len(entities) >= DRG_WINDOWED_RELATION_ENTITY_THRESHOLD` (25). `DRG_WINDOWED_RELATION_EXTRACTION` takes `auto|always|never` or truthy/falsy values. Caps: `DRG_MAX_RELATION_CANDIDATE_PAIRS` 160, `DRG_MAX_RELATION_EVIDENCE_WINDOWS` 3, `DRG_MAX_IMPLICIT_CANDIDATE_PAIRS` 120. `SKILL.md:128-135`, `reference.md:130-135`; source `drg/extract/__init__.py:529-536,547-548,616-617`. „Measure on one document before a corpus." [api] (verified: read source 0.1.2; the example encodes the thresholds at `example_drg_kg.py:24-25,92-94`)
- **drg query layer is deterministic** — `kg.query()` returns a `GraphQuery` with `entity`, `find_entities`, `relations`, `neighbors`, `find_paths`, `shortest_path`, `related_entities`, `community_of`, `search`, `query(text)`. Provenance: `evidence_for`, `explain`, `events_for`. Metrics: `centrality`, `pagerank`, `influence_scores`. Temporal: `relations_active_at`, `role_holders_at`, `temporal_*`, `changes_between`, `entity_transitions`. `GraphQuery.from_json(filepath)`. „Query is **deterministic graph traversal**, not an LLM call." `SKILL.md:105-115`, `reference.md:83-92`. [claim]
- **Validation, versioning and diff are modules** — `drg.graph.validation.validate_graph_file(path)` → `ValidationReport`, and `validate_graph_data(data, path="<memory>")`. `drg.graph.versioning.create_snapshot(kg, graph_path, *, operation="snapshot", document_id=None, versions_dir=None)`, `list_versions`, `diff_versions`, `rollback_to_version`. `drg.graph.diff.diff_graph_data(old: dict, new: dict)` → `SnapshotDiff`. They operate on paths and dicts; `EnhancedKG` has no `validate`, `diff` or `version`. `SKILL.md:117-126`, `reference.md:61-81`. [api] (verified: the example's `assert_api_surface` passed with drg 0.1.2)
- **How drg uses DSPy** — `KGExtractor(dspy.Module)` builds five signatures dynamically from the schema, each in `dspy.Predict`: `EntityExtraction`, `RelationExtraction`, `DocumentRelationExtraction`, `ImplicitRelationExtraction`, `CoreferenceResolution`. Schema generation adds `SchemaGeneration`, `SchemaReview`, `SchemaCoverageAudit`. The extractor cache is rebuilt when the schema fingerprint or the injected `lm` changes (`reference.md:94-104`; `drg/extract/__init__.py:1036-1062`). Changing the schema changes the prompts. [api] (verified: read the cache code)
- **drg supporting layers** — `drg.reasoning` (rule inference: `PathBridgeRule`, `InverseRule`, `SymmetricRule`, `TransitiveRule`, `CompositionRule`), `drg.graph.neo4j_exporter`, `drg.graph.visualization_adapter`, `drg.graph.hub_mitigation.apply_hub_relation_proxy_split`, `drg.graph.incremental`. `reference.md:141-156`. [claim]
- **The REFRAG idea vs the package** — „retrieve many chunks, then select a small subset to expand into the prompt". The package implements retrieval and selection but „does **not** implement the compression the idea is named for". `skills/dspy-refrag/SKILL.md:19-22`. [claim] (verified by the next item)
- **The selection that never shrinks the prompt** — `REFRAGModule.forward` computes `selected_idxs`, writes `meta.setdefault("selected", i in selected_idxs)`, then joins **every** passage: `f"Passage {i}: {p['text']} (selected: {p.get('selected', False)})"`. Upstream `src/dspy_refrag/refrag.py:87-114`; the skill at `SKILL.md:41-58`, `reference.md:81`. The fix is prompt assembly from `selected_idxs` only (`example_refrag.py:96-100`). [trap] (verified: upstream@a868813)
- **refrag's other verified defects** — each checked at upstream a868813:
  - `__init__.py:15` imports `PSQLRetriever`, whose `psql_retriever.py:10` is `import psycopg2`, so importing the package needs psycopg2.
  - `FAISSRetriever` raises `NotImplementedError` (`faiss_retriever.py:53`, `:83`), and so does `PineconeRetriever`.
  - `pyproject.toml:23` pins `"weaviate-client>=3.25,<4.0"` while `weaviate_retriever.py:15-16` import the v4-only `weaviate.classes.*`.
  - `vector(768)` is hard-coded (`psql_retriever.py:45`).
  - LM errors are swallowed into `answer = f"Error calling LM: {str(e)}"` (`refrag.py:116-123`).
  - `lm_model` is overridden by `maybe_configure_openrouter_env()` (`refrag.py:17,64`).
  - `SimpleRetriever` without an embedder returns random normalised vectors (`retriever.py:110-111`), and its default corpus metadata is `{"id": "a"}` (`:93`), so `p['text']` raises `KeyError` once an LM is set.

  `SKILL.md:78-102`, `reference.md:77-88`. [trap] (verified: upstream source lines as cited)
- **refrag signatures** — `REFRAGModule(retriever=None, lm=None, sensor=None, k=5, budget=2, lm_model="gpt-3.5-turbo", api_key=None, **kwargs)`, `SimpleRetriever(embed_dim=768, corpus=None, embedder=None)`, `Sensor(mode="heuristic", threshold=None, learned_weights=None)` (it asserts `mode in ("heuristic","learned")`, and learned mode without weights falls back to heuristic, `sensor.py:29,62-63`), `AdvancedSensor.select(query_vec, chunk_vecs, budget=2, metadata=None) -> list[int]`, `build_corpus_from_data(embedder, data_dir, max_chars=1500, overlap=200)`, `make_ollama_embedder(api_endpoint="http://localhost:11434", model="nomic-embed-text:latest", normalize=True)`. `reference.md:24-49`. Not on PyPI; install with `pip install git+https://github.com/netzkontrast/dspy-refrag`. [api]
- **refrag `SelectionConfig`** — `strategy=SIMILARITY`, `diversity_lambda=0.5`, `temperature=1.0`, `ensemble_weights=None`, `adaptive_percentile=0.75`, `min_score=None`. `diversity_lambda` and `adaptive_percentile` are validated to lie in [0,1] and `temperature` must be > 0 (upstream `sensor_advanced.py:27-35,55-61`). [api] (verified: upstream source)
- **Upstream MMR weights *relevance* by λ** — `mmr = lambda_param * relevance - (1 - lambda_param) * redundancy` with `lambda_param = self.config.diversity_lambda` (upstream `sensor_advanced.py:148,166`): standard Carbonell–Goldstein MMR, where a higher λ gives *less* diversity. The skill says „`diversity_lambda` … higher favours diversity over relevance" (`reference.md:56`). The example, the scaffold and the target's port all use the inverted `(1 - λ)·relevance - λ·redundancy` (`example_refrag.py:78`, `kp_canon_retriever.py:138`, and `/home/user/kohaerenzprotokoll/scripts/graphrag.py:175`). So λ=0.65 in the pack means redundancy-weighted, and in upstream it means relevance-weighted. The two are the same function only under λ ↦ 1−λ. [trap] (verified: upstream source + mmr_probe) → here: `scripts/graphrag.py` (its comment „above upstream's 0.5" compares parameters of opposite meaning)
- **Upstream MMR ignores `min_score`** — `min_score` is applied only in `_select_similarity` (upstream `sensor_advanced.py:116-123`); `_select_mmr` never reads it (`:129-173`). On the fixture, upstream MMR with `min_score=0.15` returns the same selection as without it at every λ. The skill's „**Always set `min_score`** … the floor is what keeps irrelevant passages out" (`SKILL.md:129-137`) and „plus the floor that package exposes as `SelectionConfig.min_score`" (`kp_canon_retriever.py:98-99`) describe the pack's own re-implementation, not the package. Vendoring `sensor_advanced.py` as recommended (`SKILL.md:143`) does not give you a floor. [trap] (verified: mmr_probe)
- **The MMR fixture, measured exactly** — query `[1,0,0]`, with cosines to the query 0.9949, 0.9926, 0.3011 and 0.0 for dup0, dup1, distinct and UNRELATED. The pack's MMR, budget 2:
  - Floor off: λ ≤ 0.47 → dup0+dup1; λ ≥ 0.50 → dup0+UNRELATED.
  - Floor 0.15: λ ≤ 0.53 → dup0+dup1; λ ≥ 0.54 → dup0+distinct. The analytic crossover is ≈0.534, the analytic unguarded switch ≈0.498.

  Upstream MMR: λ ≤ 0.50 → dup0+UNRELATED; λ ≥ 0.53 → dup0+dup1. It **never** reaches „distinct", with or without `min_score`. [number] (verified: mmr_probe over λ ∈ {0, .3, .45, .47, .5, .53, .54, .6, .65, .7, .8, 1.0})
- **Other refrag strategies** — `UNCERTAINTY` samples with unseeded `np.random.choice` from a temperature softmax (`sensor_advanced.py:175-200`); 20 calls gave 10 distinct selections, so it is non-deterministic. `ENSEMBLE` builds sub-sensors with **default** configs (`SelectionConfig(strategy=strategy)`, `:227`), ignoring your λ, temperature and min_score, and adds `UNCERTAINTY` once weights are given. `ADAPTIVE` thresholds at `np.percentile(similarities, adaptive_percentile*100)` (`:257`) and falls back to top-1. All strategies score with a raw dot product (`:99-104`: „normalized recommended"). [trap] (verified: upstream source + probe)
- **What to lift, per the skill** — „vendor `sensor_advanced.py` (MIT); it is self-contained" (`SKILL.md:143`). It depends on **numpy** (`sensor_advanced.py:13`). Reuse `data_ingest.build_corpus_from_data` for PDF → chunks. For FAISS use `dspy.Embeddings` rather than refrag's stub. „not this package" for production retrieval: „no retries, pooling, batching or async anywhere" (`SKILL.md:139-147`). [recipe]
- **TARA shape** — a research codebase, not a library. Distribution `agentic-self-corrective-rag`, flat package `agentic_rag/`. The transferable idea: a ReAct agent holding retrieval tools decides how to repair bad retrieval instead of running a fixed refine loop. `skills/dspy-tara-rag/SKILL.md:20-27`. [claim]
- **TARA's seven tools** —
  - `search_passages(query, top_k=10)`: hybrid FAISS + BM25.
  - `decompose_query(question)`: makes its own LLM call.
  - `evaluate_passages(question, passage_ids_json, retry_count=0)`: makes its own LLM call.
  - `get_passage_detail(passage_id, include_adjacent=False)`.
  - `list_document_sections(keyword="")`.
  - `get_terminology(user_term)`.
  - `calculate(expression)`: a restricted `eval`.

  The README says six. The registry keys are short names: `search`, `structure`, `terminology`, `evaluate`, `inspect`, `decompose`, `calculate` (upstream `agentic_rag/tools/__init__.py:28-36`). `create_tools(retriever, indexer, evaluator, enabled_tools=None)` enables all seven when `enabled_tools=None`, and each tool returns a JSON string. `SKILL.md:29-50`, `reference.md:26-39`. [api] (verified: upstream registry)
- **TARA's evaluation outputs** — `relevance_score`, `coverage_score`, `specificity_score`, `sufficiency_score`, `total_score`, `action` (`output|refine|route_to_agent`), `keywords_to_add`, `keywords_to_remove`, `suggested_query`, `reasoning`. The inputs include `retry_count` and `max_retry`, and `Evaluation1DSignature` is the 1D control (`reference.md:60-74`). „a failing score carries its own repair instruction" (`SKILL.md:64-66`). [pattern]
- **TARA's agent** — `dspy.ReAct(sig_cls, tools=tools, max_iters=...)`, with `max_iters` from `settings.agent.max_iterations` (10). When a budget is set, it is narrowed by `effective_max_iters() = max(1, (llm_call_budget - 3) // 2)`, because each iteration is one reasoning call plus at most one tool-internal call. If the agent never evaluates, `_run_mandatory_evaluate` forces one. `AgenticRAGPipeline` is a plain class, not a `dspy.Module` (`reference.md:41-58`; upstream `pipeline/agentic.py:99-105`). [claim] (partly verified: the budget formula in the upstream docstring)
- **Index before run** — `uv run python scripts/build_index.py --dataset ...` builds FAISS `IndexFlatIP` (L2-normalised), BM25, `section_index` and `term_index`. „The index must exist before any run; nothing builds it lazily." `SKILL.md:102-113`, `reference.md:105-110`. [claim]
- **The KP canon seam** — `CanonIndex` is a dataclass (`passages`, `embedder=None`, `k=12`, `budget=5`, `diversity_lambda=0.65`, `min_relevance=0.15`) whose `__call__(claims) -> str` satisfies `CanonRetriever = Callable[[list[Claim]], str]`. It returns cited passages `"[source#section] text"` joined by `"\n\n---\n\n"`. „Canon passages must arrive citable, or a conflict cannot be adjudicated." `scaffolding/kp_canon_retriever.py:71-83,161-187`. [pattern]
- **A two-stage shortlist then select** — `_shortlist` sorts the passages by lexical term overlap and takes `k`. `_select` then runs MMR only when an embedder exists **and** every candidate has a vector; otherwise it returns `candidates[:budget]` (`kp_canon_retriever.py:189-204`). `load()`/`build()` raise `NotImplementedError` with build instructions: chunk per canon section and per codex entry, embed with `dspy.Embeddings`, persist a manifest with the corpus hash, chunking-rule version and embedding model id (`:222-240`). [pattern]
- **Query weighting that only works for embeddings** — `claims_to_query` repeats the entities twice before the claim bodies „to weight them" (`kp_canon_retriever.py:150-158`). In the lexical fallback, `terms()` produces a **set**, so the repetition changes nothing there. [trap] (verified: read)

## AGENT

- **RLM tools are agent tools with REPL semantics** — the model calls them from code, with results as Python values. Custom tools such as `read_file` or `grep` are „regular Python callables passed via `tools=[...]`" (`skills/dspy-rlm-module/SKILL.md:106`, `reference.md:72-87`). The sandbox is not the tools' security boundary: „If you pass custom `tools` that do I/O, your tools' security posture is yours. Never hand raw `subprocess.run` to the RLM." (`SKILL.md:109-111`). [recipe] → here: `scripts/rlm_ingest.py` `find_line`, `count`
- **Two TARA tools hide LLM calls** — „Two tools make their own LLM calls (`decompose_query`, `evaluate_passages`), so the agent's iteration count understates the real cost." `SKILL.md:49-50`. The example's cost formula `n + 2*max(0, n-2) + 1` (`example_tara.py:100-103`) is invented, not measured: it returns 1 call for 0 tool calls and 12 for 5. [claim]
- **In the agentic path the LLM applies the leniency rule** — `evaluate_passages` returns `eval_result.action` and `total_score` straight from the LLM (upstream `agentic_rag/tools/evaluate.py:106-107,115-116,130`). The signature docstring gives the rule without a floor: „effective_threshold = QUALITY_THRESHOLD - (retry_count * 5)" (`signatures/evaluate.py:41`). The code-level floor at 20 exists only in `pipeline/loop.py:311`. So the skill's „The code wins" (`SKILL.md:75-76`) holds for the `loop` pipeline, not for TARA's agent. [trap] (verified: upstream source)
- **Hooks are not a sandbox** — „RLM executes LM-generated Python. Hooks observe and rewrite; they are not a sandbox." Anyone holding the RLM instance can inject behaviour, so hook sources are trusted code (`skills/dspy-rlm-hooks/reference.md:113-117`, `SKILL.md:135`). [claim]

## PROD

- **Pin DSPy with anything that patches RLM internals** — „treat the pair `(dspy, dspy-rlm-hooks)` as one version unit and pin both." `skills/dspy-rlm-hooks/reference.md:47-48`, `SKILL.md:31-36,137`. The hooks package carries its **own copy** of `_strip_code_fences` (`core/utils.py:31-81`, with an extra adjacent-fence branch) and of the iteration loop (`core/patcher.py:118-220`). A DSPy release that changes the loop is silently shadowed by the copy on patched instances. [trap] (verified: read source)
- **Hooks turn terminal sandbox errors into prompts** — the hooks' `_execute_code` catches **every** `Exception` and returns `f"[Error] {exc}"` (`dspy_rlm_hooks/core/patcher.py:105-115`). DSPy's own catches only `(CodeExecutionError, SyntaxError)` (`rlm.py:661-664`). With hooks enabled, a terminal `CodeInterpreterError` (Deno died, protocol failure) becomes a recoverable step output, and the loop keeps spending outer-LM calls against a dead interpreter. [trap] (verified: read both sources)
- **Speculation spends sub-LM calls outside `max_llm_calls`** — `speculate_llm_query=True` is the default. Speculative `llm_query`/`llm_query_batched` executions „call the sub-LM directly instead: they do not consume the logical budget" (`speculation/integration/registry.py:92-101,103-127`), bounded only by `max_dispatches_per_turn=2048` per turn and per-prompt dedup. Only **claimed** calls count against `max_llm_calls` (`api.py:16-19`). Evicted speculations are paid and uncounted. `llm_query` is also registered `speculatable=True, pure=True` (`registry.py:146-147,156-157`) even though it is a paid call, which is exactly what the skill's own rule forbids for user tools: „Tool costs money per call; evicted speculations are paid for and thrown away." (`example_rlm_hooks.py:58-59`). [trap] (verified: read source) → here: never enable speculation where `max_llm_calls` is the cost guard (P18 repeats)
- **Dispose of speculation** — „Always call `disable_rlm_speculation(rlm)` when done: it spawns subprocesses, threads and an asyncio loop." `SKILL.md:105-107`. Isolation is a real subprocess with a per-statement watchdog, because „An in-process jail cannot stop the `().__class__.__mro__[1].__subclasses__()` escape" (`SKILL.md:109-111`). [claim]
- **drg configures DSPy's global LM for you** — with no `lm=` and nothing configured, `extract_typed` calls `_configure_llm_auto()`, whose `LMConfig._configure_unsafe()` does two things:
  - It runs `load_dotenv(".env", override=False)` from the **current working directory**.
  - It picks `DRG_MODEL` (default `openai/gpt-4o-mini`), only warns about a missing key („Cloud model (openai/gpt-4o-mini) selected but OPENAI_API_KEY not found. An API key may be required."), and **always** calls `dspy.configure(lm=...)`.

  Source: `drg/config.py:59-230`, `drg/extract/__init__.py:171-203,1026-1033`. After one `extract_typed` call, `dspy.settings.lm` changed from `None` to `openai/gpt-4o-mini`, and a live completion to that model was attempted, which my probe refused. [trap] (verified: probe on drg-kg 0.1.2 and git g4d6970bcc, DSPy 3.3.1) → here: never call drg extraction without an explicit `lm=`; a `.env` in cwd would be read
- **`DRG_REQUIRE_LM=1` does not stop that call** — the strict guard `_guard_lm_or_mock_empty` raises `LLMConfigError` only when no LM exists after auto-config (`drg/extract/__init__.py:183-203`). Auto-config always creates one, so with `DRG_REQUIRE_LM=1` the same keyless call was attempted and failed at request time. The skill's row „Empty graph, only a log warning | No DSPy LM configured — extraction returns `([], [])` | Set `DRG_REQUIRE_LM=1` …" (`SKILL.md:96`) did not reproduce. The strict variables are `DRG_STRICT` (via `drg/utils/strict.py:25-30`), `DRG_REQUIRE_LM` and `DRG_PRODUCTION`, with truthy values `1/true/yes/y/on` (`extract/__init__.py:162-168`). [trap] (verified: probe; see „The old report, corrected")
- **drg LM environment** — `DRG_MODEL` (default `openai/gpt-4o-mini`; Gemini names are normalised to `gemini/<name>`), `DRG_BASE_URL`, `DRG_TEMPERATURE` (0.0), `DRG_MAX_TOKENS` (1500 in `config.py:170`; the CLI raises it to 4096 when unset, `cli.py:443-444`). Keys come from `OPENAI_/GEMINI_/ANTHROPIC_/OPENROUTER_/PERPLEXITY_API_KEY`, and OpenRouter gets base `https://openrouter.ai/api/v1`. drg also **writes** keys back into `os.environ` (`config.py:196-216`). `skills/dspy-drg-kg/reference.md:117-125`. [api] (verified: read config.py)
- **Reproducible latency needs the cache off** — TARA: „For reproducible latency numbers set `DISABLE_LLM_CACHE=true`" (`SKILL.md:131`). Upstream the default is `disable_llm_cache: bool = Field(False, alias="DISABLE_LLM_CACHE")` (`agentic_rag/config/settings.py:225`), and `experiments/verify.py:216` fails a campaign with „DISABLE_LLM_CACHE was off: latency is not measurable". `LLM_EXPECTED_RESPONSE_MODELS` aborts if the provider serves a different snapshot (`reference.md:138-145`). [pattern] (verified: upstream grep) → here: `scripts/lmrun.py` `cache=False` (P18)
- **A „controlled" comparison was opt-in** — `RETRIEVAL_MAX_PASSAGES_ALL_PIPELINES` is off by default, so the published runs gave naive and CRAG more passages than loop and agentic (`SKILL.md:132-134`). The setting is `settings.retrieval.max_passages_all_pipelines`, recorded in the run manifest (`experiments/manifest.py:297`), default `max_passages_all_pipelines: bool = False` (upstream `agentic_rag/config/settings.py:119`). [pattern] (verified: upstream source)
- **TARA cost profile** — „CRAG issues roughly 40 LLM calls per question against naive's one"; a full campaign is five pipelines × four datasets × 150–200 questions × repeats; building the FinanceBench index costs LLM calls (`SKILL.md:123-130`). Raw JSONL results are not committed, only `data/results/RESULTS_SUMMARY.md` (`reference.md:147-148`). [claim]
- **TARA license** — the README carries an MIT badge and links `LICENSE`, but no `LICENSE`, `LICENCE` or `COPYING` exists (`SKILL.md:136-140`, `reference.md:9-10`). „Treat the design as readable and the code as unlicensed until fixed." [trap] (verified: `ls` in the clone at 6c307f3)

## TEST

- **Pin the RLM surface in the dry-run** — `assert_rlm_surface()` asserts the 8 constructor names, the absence of `max_iterations`, and `interpreter` in `forward` (`skills/dspy-rlm-module/example_rlm.py:35-55`). The dry-run constructs an RLM without Deno and prints the input and output fields. [pattern] (verified: dry-run on 3.3.1) → here: `scripts/check_dspy_surface.py`
- **Maintainer surface check** — `scripts/check_dspy_surface.py:130-171` asserts the RLM params, `max_iterations` absent, `max_output_chars` default 10_000, `interpreter` on `forward` for RLM, PoT and CodeAct, `dspy.PythonInterpreter` present, and Refine/BestOfN params (`:120-125`). Regression tests pin the same facts: rule 3, stale `max_output_chars=100_000` patterns (`tests/test_skill_correctness.py:193-217`), and rule 10, stale constructor names with a migration-context allow-list (`:492-574`). [pattern] (verified: ran both; 633 passed)
- **A mock `CodeInterpreter` makes RLM testable without Deno** — any object with `tools`, `start()`, `execute(code, variables)` and `shutdown()` that returns `FinalOutput(dict)` on SUBMIT and raises `CodeExecutionError` on code errors lets `DummyLM` drive a full RLM loop. It is not in the repo; „Code worth keeping" has a working one. [pattern] (verified: probes A–E) → here: `scripts/lm_fixture.py` (P5 for job 3)
- **Four of six dry-runs never touch their package** — the hooks, drg, refrag and TARA examples re-implement the skill's model of the package in plain Python (`composition_is_correct`, `may_speculate`, `diagnose_empty_graph`, `select_mmr`, `decide`, …). They assert the package only when it is installed, and otherwise print „package not installed: skipped live API assertions" (`example_rlm_hooks.py:151-159`, `example_drg_kg.py:157-166`, `example_refrag.py:179-184`). The reporting is honest (P23), but the model can be wrong about the package: drg's empty graph, refrag's MMR λ and floor, TARA's routing (section TRAP). [trap] (verified: all four dry-runs ran in 0.04–0.07 s without importing dspy)
- **With the package installed, the asserts are signature-level** — the drg example checks defaults and keyword-only-ness (`example_drg_kg.py:97-128`), the hooks example checks defaults, fields and the purity refusal (`example_rlm_hooks.py:92-125`). Both passed on the real packages (hooks 0.1.14, drg 0.1.2), yet the behaviour claims they sit beside were wrong or unverified: the CHANGELOG says „their asserted API surfaces verified live" (`docs/CHANGELOG.md:163`). A signature check does not verify behaviour. [trap] (verified: both examples with packages)
- **A check that passes vacuously** — `try: validate_dag(<cycle>) except ValueError as exc: assert "cycle" in str(exc)` has no `else: raise` (`example_rlm_workflow.py:164-168`), so a `validate_dag` that stops raising passes the test. The hooks example does it right with an `else: raise AssertionError(...)` (`example_rlm_hooks.py:115-121`). [trap] (verified: read)
- **More weak asserts** — `assert wrong.weakest() == "sufficiency" or wrong.weakest() == "relevance"` accepts either (`example_tara.py:115`). The refrag stub check `except TypeError: pass  # signature differs; the stub claim is checked by source above` passes on any signature mismatch, and no source check of the stubs exists above it (`example_refrag.py:129-137`). The compression-defect detector is a string heuristic: `"selected_idxs" in source.split("context_str")[-1][:400]` (`:119`). [trap] (verified: read)
- **Examples require `--dry-run`** — the whole pack is guarded by `tests/test_examples_parse.py` and rule 5, and every example in this slice honours it. The live paths default to real models (`openai/gpt-4o`, `example_rlm.py:71`; `example_rlm_workflow.py:153`). [pattern]

## PAT

- **`validate_dag`: never let the LM order the work** — plain Python that rejects duplicate ids (`ValueError("duplicate sub-problem ids")`) and unknown dependencies (`"dependencies on unknown ids: [..]"`), and detects cycles with a DFS naming the path (`"cycle: 1 -> 2 -> 1"`). It returns topological order. „Do not ask the LM to order the work — it will get it wrong on the day it matters." `skills/dspy-rlm-workflow/reference.md:44-69`, `SKILL.md:101-103`, `example_rlm_workflow.py:30-54`. [pattern] (verified: dry-run, order [1,2,3,4], cycle raised) → here: P1
- **Phase → construct map** — Initialize → `WorkflowPlan` (depth clamp); Distill → RLM or a per-chunk `Distill`; Decompose → `list[SubProblem]` + `validate_dag`; Solve in topological order with dependency results injected, recursing on `complexity == "high"` while depth remains; Synthesize → agreements, contradictions, gaps, answer, confidence; Verify → cascade; Iterate → Refine/GEPA. `SKILL.md:20-30`. [pattern]
- **Typed models** — `SubProblem(id, description, dependencies=[], complexity: Literal["low","medium","high"]="medium", success_criteria)`, `WorkflowPlan(complexity: Literal["constant","linear","quadratic"], depth: int = Field(ge=1, le=3), success_criteria: list[str])`, `SubResult(..., confidence: float = Field(ge=0, le=1))`, `Synthesis(agreements, contradictions, gaps, answer, confidence)`. `reference.md:10-38`. The canonical program's `Solve.confidence: float` has no bounds, and only Tier 1 checks them. [api]
- **Never resolve a contradiction silently** — the `Synthesize` docstring says „Never resolve a contradiction silently", and the `contradictions` field format is „topic — A says / B says — resolution — why". `SKILL.md:65-74`, `reference.md:34`. The pattern still resolves contradictions. For the target, only the *listing* half is admissible (P13: conflicts are recorded and never settled by a model). [pattern] → here: reconcile/conflict pages (list, never resolve)
- **Recombination follows the graph** — a chain → sequential; no edges → parallel (`dspy.Parallel` or threads); mixed → hierarchical (synthesize groups first). `reference.md:71-73`. [pattern]
- **Distillation strategies as RLM tools** — funnel filter (all → dirs → matches → sections), anchor expansion (known file → imports → callers → tests), cross-reference (intersect pattern hits). `reference.md:87-90`. [pattern]
- **Run report template** — Problem · Complexity · Depth · Success criteria / Distillation N → M tokens (x %), excluded / Decomposition table / Sub-results / Synthesis / Verification tiers → score / Iterations (attempt, reward, advice) / Lessons. `reference.md:148-162`. [pattern]
- **Progressive leniency is an anti-pattern for a gate** — TARA's `effective_threshold = max(quality_threshold - retry*5, 20)` (default 40, 3 retries) ends by lowering the bar. The skill: „decide deliberately whether 'eventually accept something mediocre' is the behaviour you want" (`SKILL.md:68-83`). The upstream code is looser still (TRAP). For a canon gate, the terminal state should be „not answered", not a lower bar. [pattern] → here: P15
- **An inert seam with a no-op default** — the scaffold fills a `Callable[[list[Claim]], str]` seam whose current default `no_canon_retrieval` returns `""`, „So `CheckCanonConflict` currently never fires: with nothing retrieved, nothing can conflict, and every ingest reports zero conflicts." `kp_canon_retriever.py:6-17`. A green zero from a check that is fed nothing is the „check that cannot fail" shape. [pattern] (the `tools/kpwiki/` it describes does not exist in `/home/user/kohaerenzprotokoll`)
- **Why a floor matters for conflict checks** — „a duplicate merely wastes context, an unrelated passage invites a fabricated conflict". `kp_canon_retriever.py:106-114`. [pattern] → here: `scripts/graphrag.py` (the floor exists; see RAG for λ semantics)

## SKILL

- **Pin the version you verified in the skill** — `dspy-rlm-hooks` names 0.1.14 (`SKILL.md:18`) and `dspy-refrag` names 0.1.0 (`SKILL.md:17`). `dspy-drg-kg` says only „alpha" (`SKILL.md:18`), and `requirements-extras.txt:37` allows `drg-kg[dspy]>=0.1`. TARA names no commit. The drg behaviour claims could not be tied to any version. [pattern]
- **Verify behaviour, not just signatures** — the pack's verification discipline (`inspect.signature`, `check_dspy_surface.py`) caught every rename in this slice and missed every behavioural error: extract fallback, drg auto-config, inverted λ, ignored `min_score`, TARA final-retry output. A skill that teaches a third-party package needs one behavioural probe per headline claim. [pattern]
- **Frontmatter in the slice is spec-only** — `name`, `description` and `when_to_use` only (e.g. `skills/dspy-rlm-hooks/SKILL.md:1-16`, folded `>-` scalars). They pass `tests/test_skill_metadata.py`. [api] (verified: pytest)

## TRAP

- **RLM extract fallback fabricates an ending** — see RLM. The single most consequential RLM fact for a verified census: a run that never reached `SUBMIT` returns a normal `Prediction`. Detect it through `final_reasoning`. (`dspy/predict/rlm.py:543-562`) [trap] (verified)
- **`max_llm_calls` is not a spend cap on the invocation** — see RLM (`rlm.py:261-325`; `reference.md:43` is wrong). [trap] (verified)
- **The failure table in `dspy-rlm-module/reference.md:93-103` is mostly invented** — `deno: command not found` is a shell message, and DSPy raises „Unable to determine the Deno version from 'deno' …". „`RLM hit max_iters`" does not exist: extract fallback with a WARNING. „`Sub-LM call count exceeded`" does not exist: the message is „LLM call limit exceeded: …" inside the sandbox. „`Output truncated at 10000 chars`" does not exist: the prompt shows „… (N characters omitted) …". „`KeyError` in final `.answer`" cannot occur on the SUBMIT or extract paths, where the failure would be `AdapterParseError`. [trap] (verified: probes and source)
- **The canonical workflow drops dependency results on recursion** — for a `high`-complexity sub-problem the code computes `deps` and then recurses with `self.forward(sp.description, distilled_context, depth + 1)` without them (`skills/dspy-rlm-workflow/SKILL.md:89-93`, `example_rlm_workflow.py:100-103`). In `SAMPLE_PLAN`, sub-problem 3 is `high` with `dependencies=[1, 2]` (`example_rlm_workflow.py:145`), so a live run would solve it blind. [trap] (verified: read)
- **`dspy.PythonInterpreter` „3.3.x-only" is false** — see API (`reference.md:60`, `docs/CHANGELOG.md:40-41`). [trap] (verified)
- **„Check `which deno`" gives a false negative in 3.3.x** — DSPy prefers the pip `deno` package binary, which is not on PATH (`python_interpreter.py:84-94`; `SKILL.md:107`). [trap] (verified)
- **drg's documented silent-empty mode did not reproduce; a live call happened instead** — see PROD. The empty path exists in code (`drg/extract/__init__.py:190-203`), but auto-config (`config.py:221-223`) makes it unreachable in a fresh process. The skill (`SKILL.md:90-103`), the CHANGELOG (`docs/CHANGELOG.md:141`) and the example's `diagnose_empty_graph` (`example_drg_kg.py:74-89`) all describe the unreachable branch. [trap] (verified: probe, two installs)
- **„`DRG_MAX_TEXT_CHARS` (100000 hard limit)"** — the limit is overridable, as the error message itself says (`reference.md:128`). [trap] (verified)
- **The pack's MMR is not the package's MMR** — λ is inverted and `min_score` is not applied in MMR upstream. „Ported from dspy-refrag `sensor_advanced.py` (MIT)" (`kp_canon_retriever.py:98`) and „reproduced faithfully" (`example_refrag.py:65`) are false about the formula. [trap] (verified)
- **„The floor changes the outcome at every lambda"** — false on the scaffold's own fixture: for λ ≤ 0.47 floor-off and floor-on both give dup0+dup1 (`kp_canon_retriever.py:124`). The CHANGELOG's „The floor fixes it at every setting" (`docs/CHANGELOG.md:157`) holds only over the tested 0.5–0.8. „needs roughly 0.6 or above to bite" (`skills/dspy-refrag/SKILL.md:135-136`) and „only lambda >= 0.6 reaches a relevant-but-distinct passage" (`kp_canon_retriever.py:51-53`): the measured crossover is 0.534. [trap] (verified: mmr_probe)
- **The scaffold contradicts itself on λ** — the constant is 0.65 because „0.5 still returns the duplicate" (`kp_canon_retriever.py:51-55`), while the docstring calls 0.5 „the upstream default and a sane start for a codex where several entries restate the same rule" (`:102-104`). [trap] (verified: read)
- **The scaffold's lexical fallback has no floor** — `_shortlist` sorts by overlap and takes `k` even at zero overlap, and without an embedder `_select` returns `candidates[:budget]` (`kp_canon_retriever.py:189-199`). An unrelated claim („Kael sieht Juna") received both unrelated passages. That is the exact failure the floor exists to prevent, in the path tests use. [trap] (verified: probe)
- **`terms()` drops four-letter names** — `len(w) > MIN_TERM_LENGTH` with `MIN_TERM_LENGTH = 4` keeps only words of ≥5 characters, and length is checked before punctuation is stripped (`kp_canon_retriever.py:60,146-147`). `terms("Kael und Juna treffen AEGIS im Kernwelt-Garten")` → `{'aegis', 'kernwelt-garten', 'treffen'}`: the protagonists' names vanish, and hyphen compounds stay whole. [trap] (verified: probe) → here: any lexical matching over German canon (compare `entities.py`/`corpus.py` tokenisation)
- **`cosine` silently truncates dimension mismatches** — `zip(a, b)` gives `cosine([1,0,0],[1,0]) == 1.0` (`kp_canon_retriever.py:86-89`, `example_refrag.py:44-47`). Semantic selection also switches to the lexical fallback without a report whenever any candidate lacks a vector (`kp_canon_retriever.py:197-199`). [trap] (verified: probe)
- **refrag example: „implements the five selection strategies"** — it implements three (similarity, MMR, adaptive; `example_refrag.py:3-6,50-93`), and its adaptive differs from upstream: pack `[0, 1]`, upstream `[0]` on the fixture, because upstream interpolates with `np.percentile`. [trap] (verified: mmr_probe)
- **TARA outputs any context at the final retry** — upstream `loop.py:318-320`: `elif retry >= max_retry: # Always generate on final retry — don't route away; action_override = "output"`. A „diminishing returns" early exit also outputs a below-threshold context whenever the score does not improve (`:321-333`). `route_to_agent` is never produced by the override, and routing needs `enable_agent_routing` **and** zero passages (`pipeline/_mixin.py:230-237`: „Generate from available passages (even if below threshold)"). The signature docstring agrees: „retry_count >= max_retry → action = "output" (always generate on final retry)" (`signatures/evaluate.py:45`). The skill's „Only a context below 20 is ever routed away" (`SKILL.md:81`) is wrong. [trap] (verified: upstream@6c307f3)
- **The TARA example's own model contradicts its printout** — with base 40 and `max_retry=3`, the threshold at the last retry is 25, not 20. `decide()` routes a total of 22 away at retry 3 (`example_tara.py:81-86`), yet the dry-run prints „only total<20 escalates" (`:137-139`). The floor of 20 is reached only at retry 4. [trap] (verified: probe, `decide(22, 3) == "route_to_agent"`)
- **`fail_count` and Refine's `None`** — see API (`refine.py:91,170-177`). A Refine-wrapped workflow can return `None`, which a downstream `.answer` turns into an `AttributeError` far from the cause. [trap] (verified)
- **Hooks: `--variant-fn` does not exist** — the CLI takes custom variants as `--variants mymod:my_variant` (`benchmark/report.py:144-173`). The package's own docstring (`benchmark/__init__.py:34`, `report.py:34`) and the skill (`reference.md:94`) name a `--variant-fn` flag that argparse rejects. [trap] (verified: `--help` and parser source)
- **Old CHANGELOG line contradicts the current floor** — `docs/CHANGELOG.md:181` says the rlm example „still fails … the pack targets the DSPy 3.2.x series", while `:54` raises the floor to 3.3.0 and the example passes on 3.3.1. A historical entry, but it reads as current. [trap] (verified: read)

---

## Code worth keeping

**validate_dag** — `skills/dspy-rlm-workflow/example_rlm_workflow.py:30-54`. Pure Python; runs on DSPy 3.3.1 (the dry-run asserts order `[1, 2, 3, 4]` and a raised cycle; add an `else: raise` to the cycle test).
```python
def validate_dag(sub_problems: list[SubProblem]) -> list[SubProblem]:
    """Return sub-problems in dependency order; raise ValueError on bad graphs."""
    by_id = {sp.id: sp for sp in sub_problems}
    if len(by_id) != len(sub_problems):
        raise ValueError("duplicate sub-problem ids")
    unknown = {d for sp in sub_problems for d in sp.dependencies if d not in by_id}
    if unknown:
        raise ValueError(f"dependencies on unknown ids: {sorted(unknown)}")
    order: list[SubProblem] = []
    state: dict[int, int] = {}

    def visit(sid: int, stack: tuple[int, ...]) -> None:
        if state.get(sid) == 2:
            return
        if state.get(sid) == 1:
            raise ValueError(f"cycle: {' -> '.join(map(str, stack + (sid,)))}")
        state[sid] = 1
        for dep in by_id[sid].dependencies:
            visit(dep, stack + (sid,))
        state[sid] = 2
        order.append(by_id[sid])

    for sp in sub_problems:
        visit(sp.id, ())
    return order
```

**Fast-fail cascade metric (five-argument, returns Prediction)** — `skills/dspy-rlm-workflow/example_rlm_workflow.py:125-137` (dedented by four spaces; it lives inside `build()`). Runs on 3.3.1 (dry-run: good 1.00, bad 0.00). Tier 3 is a stub; replace the constant with a judge before trusting scores.
```python
def verify_cascade(gold, pred, trace=None, pred_name=None, pred_trace=None):
    t1, report = tier1_syntactic(pred)
    if t1 < 1.0:
        return dspy.Prediction(score=0.3 * t1, feedback=f"Tier 1 failed: {report}")
    # Tier 2: every success criterion must be addressed in the answer.
    criteria = list(getattr(gold, "success_criteria", []) or [])
    hit = sum(c.lower() in pred.answer.lower() for c in criteria)
    t2 = hit / len(criteria) if criteria else 1.0
    if t2 < 0.8:
        missing = [c for c in criteria if c.lower() not in pred.answer.lower()]
        return dspy.Prediction(score=0.3 + 0.4 * t2, feedback=f"Tier 2 failed: criteria missing {missing}")
    # Tier 3 (pragmatic) would be an LM judge; the smoke test treats it as passed.
    return dspy.Prediction(score=0.3 + 0.4 * t2 + 0.3, feedback="Verified on all three tiers.")
```

**RLM surface pin** — `skills/dspy-rlm-module/example_rlm.py:35-55`. Runs on 3.3.1 (dry-run OK); fails on 3.2.1 by design.
```python
def assert_rlm_surface() -> None:
    """Pin the dspy.RLM constructor names this skill teaches.

    DSPy 3.3.0 renamed ``max_iterations`` to ``max_iters`` and replaced the
    ``interpreter`` constructor argument with an ``interpreter_factory``,
    moving a caller-owned ``interpreter`` to ``forward``. Asserting the names
    here means a future rename fails the smoke test rather than a user's run.
    """
    import inspect

    import dspy

    init = inspect.signature(dspy.RLM.__init__).parameters
    for name in ("signature", "max_iters", "max_llm_calls", "max_output_chars",
                 "verbose", "tools", "sub_lm", "interpreter_factory"):
        assert name in init, f"dspy.RLM.__init__ lost parameter {name!r}"
    assert "max_iterations" not in init, (
        "dspy.RLM re-introduced max_iterations; revisit this skill"
    )
    forward = inspect.signature(dspy.RLM.forward).parameters
    assert "interpreter" in forward, "dspy.RLM.forward lost its interpreter argument"
```

**What happens at `max_iters` (DSPy's own code)** — `dspy/predict/rlm.py:543-562` (DSPy 3.3.1 installed source). This is the branch a caller must detect.
```python
    def _extract_fallback(
        self,
        variables: list[REPLVariable],
        history: REPLHistory,
        output_field_names: list[str],
    ) -> Prediction:
        """Use extract module to get final output when max iterations reached."""
        logger.warning("RLM reached max iterations, using extract to get final output")

        variables_info = [variable.format() for variable in variables]
        extract_pred = self.extract(
            variables_info=variables_info,
            repl_history=history,
        )

        return Prediction(
            trajectory=[e.model_dump() for e in history],
            final_reasoning="Extract forced final output",
            **{name: getattr(extract_pred, name) for name in output_field_names},
        )
```

**The sub-call counter (DSPy's own code)** — `dspy/predict/rlm.py:263-274`. It counts only `llm_query`/`llm_query_batched`, fresh per forward.
```python
        state = {"call_count": 0}
        lock = threading.Lock()
        lm = self.sub_lm

        def _check_and_increment(n: int = 1) -> None:
            with lock:
                if state["call_count"] + n > self.max_llm_calls:
                    raise RuntimeError(
                        f"LLM call limit exceeded: {state['call_count']} + {n} > {self.max_llm_calls}. "
                        f"Use Python code for aggregation instead of making more LLM calls."
                    )
                state["call_count"] += n
```

**A host-side mock interpreter + DummyLM that drives `dspy.RLM` offline** — written for this extraction, not from the repo (condensed from `scratchpad/probe/rlm_probe.py`; this exact condensed text was re-run as `probe/condensed_check.py`: `isinstance(..., CodeInterpreter)` True, answer `x`, trajectory outputs `['3\n', "FINAL: {'answer': 'x'}"]`). The longer version produced RLM probes A–E on DSPy 3.3.1. Not a sandbox: `exec` on the host, for tests only. Inputs are re-injected per call the way `PythonInterpreter` does it.
```python
from dspy.primitives.code_interpreter import CodeExecutionError, FinalOutput
import io, contextlib

class _Submit(BaseException):
    pass

class HostInterp:  # passes isinstance(x, dspy.primitives.code_interpreter.CodeInterpreter)
    def __init__(self):
        self.tools, self.ns, self.output_fields = {}, {}, None
    def start(self):
        pass
    def execute(self, code, variables=None):
        self.ns.update(variables or {})
        self.ns.update(self.tools)           # llm_query, llm_query_batched, user tools
        def SUBMIT(**kw):
            raise _Submit(kw)
        self.ns["SUBMIT"] = SUBMIT
        buf = io.StringIO()
        try:
            with contextlib.redirect_stdout(buf):
                exec(code, self.ns)
        except _Submit as s:
            return FinalOutput(s.args[0])
        except SyntaxError:
            raise
        except Exception as e:
            raise CodeExecutionError(f"{type(e).__name__}: {e}")
        return buf.getvalue()
    def shutdown(self):
        pass

# usage: dspy.configure(lm=DummyLM([{"reasoning": "r", "code": "SUBMIT(answer='x')"}]))
#        dspy.RLM("context -> answer", interpreter_factory=HostInterp)(context="...")
```

**MMR with a relevance floor** — `scaffolding/kp_canon_retriever.py:126-143` (the body; the signature is at `:92-95`). Stdlib only; runs anywhere; numbers verified under RAG. Note its λ weights **redundancy**, the inverse of upstream refrag.
```python
    eligible = [i for i in range(len(passage_vecs))
                if cosine(query_vec, passage_vecs[i]) >= min_relevance]
    if not eligible:                                  # nothing clears the floor
        return []
    chosen: list[int] = []
    remaining = list(eligible)
    while remaining and len(chosen) < budget:
        best, best_score = remaining[0], -math.inf
        for i in remaining:
            relevance = cosine(query_vec, passage_vecs[i])
            redundancy = max((cosine(passage_vecs[i], passage_vecs[j]) for j in chosen),
                             default=0.0)
            score = (1 - diversity_lambda) * relevance - diversity_lambda * redundancy
            if score > best_score:
                best, best_score = i, score
        chosen.append(best)
        remaining.remove(best)
    return chosen
```

**Upstream refrag MMR, for contrast** — `dspy-refrag@a868813 src/dspy_refrag/sensor_advanced.py:148-168`. Requires numpy; λ weights **relevance**, and there is no floor.
```python
        lambda_param = self.config.diversity_lambda

        for _ in range(budget):
            if not remaining_indices:
                break

            if not selected_indices:
                # First selection: pure similarity
                best_idx = remaining_indices[np.argmax(similarities[remaining_indices])]
            else:
                # MMR: balance similarity and diversity
                mmr_scores = []
                for idx in remaining_indices:
                    relevance = similarities[idx]
                    # Max similarity to already selected chunks
                    redundancy = max(
                        pairwise[idx, sel_idx] for sel_idx in selected_indices
                    )
                    mmr = lambda_param * relevance - (1 - lambda_param) * redundancy
                    mmr_scores.append(mmr)
                best_idx = remaining_indices[np.argmax(mmr_scores)]
```

**Four-hook skeleton** — `skills/dspy-rlm-hooks/example_rlm_hooks.py:74-86`. Runs with `dspy-rlm-hooks==0.1.14` on DSPy 3.3.1 under Python 3.12 (the example's installed-package branch passed).
```python
    def pre_iteration(iteration, variables, history, input_args):
        return PreIterationOutput(extra_vars={"iteration_seen": iteration},
                                  prompt_context="Prefer already-loaded variables.")

    def pre_execution(iteration, code, variables, history, input_args):
        return PreExecutionOutput(code=code)          # rewrite point

    def post_execution(iteration, code, result, variables, history, input_args):
        return PostExecutionOutput(result=result)     # redact/cap point

    def post_iteration(iteration, pred, code, result, history):
        log.append(f"iteration {iteration}")
        return PostIterationOutput(history=history, stop=False)
```

**4D score with weakest-dimension routing** — `skills/dspy-tara-rag/example_tara.py:34-65`. Pure Python; the dry-run passed. The ceilings are validated in code, not trusted from the LLM.
```python
@dataclass(frozen=True)
class ContextScore:
    """The 4D assessment. Each dimension localizes a different failure."""

    relevance: int
    coverage: int
    specificity: int
    sufficiency: int

    def __post_init__(self) -> None:
        for name, value, ceiling in (
            ("relevance", self.relevance, MAX_RELEVANCE),
            ("coverage", self.coverage, MAX_COVERAGE),
            ("specificity", self.specificity, MAX_SPECIFICITY),
            ("sufficiency", self.sufficiency, MAX_SUFFICIENCY),
        ):
            if not 0 <= value <= ceiling:
                raise ValueError(f"{name}={value} outside 0..{ceiling}")

    @property
    def total(self) -> int:
        return self.relevance + self.coverage + self.specificity + self.sufficiency

    def weakest(self) -> str:
        """Which dimension to act on — the point of scoring four instead of one."""
        fractions = {
            "relevance": self.relevance / MAX_RELEVANCE,
            "coverage": self.coverage / MAX_COVERAGE,
            "specificity": self.specificity / MAX_SPECIFICITY,
            "sufficiency": self.sufficiency / MAX_SUFFICIENCY,
        }
        return min(fractions, key=fractions.get)
```

**drg's non-vacuous P/R/F1** — `drg/evaluation/_runner.py:149-160` (drg-kg 0.1.2 installed source). No DSPy needed.
```python
def _prf(tp: int, fp: int, fn: int) -> MetricResult:
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    return MetricResult(
        precision=precision,
        recall=recall,
        f1=f1,
        true_positives=tp,
        false_positives=fp,
        false_negatives=fn,
    )
```

---

## The old report, corrected

Against `/home/user/kohaerenzprotokoll/Plan/concept/dspy-repos_2026-09-23/dspy-agent-skills-A.md`, for this slice only.

- **§2 item 21: „`max_llm_calls` … budgets the whole RLM invocation, separate from `max_iters`"** — it caps only `llm_query`/`llm_query_batched` calls per forward. Exceeding it raises inside the sandbox and the run continues. The outer LM adds up to `max_iters` action calls plus one extract call (`rlm.py:261-325,543-562`). The old report inherited `reference.md:43`'s wording.
- **§2 items 19–25 missed the most important RLM behaviour** — at `max_iters` the RLM returns an extract-forced answer (`final_reasoning="Extract forced final output"`) instead of failing. A job that must tell „never reached" from „answered" (P15) needs this.
- **§2 item 25: „RLM tools are kwargs-only"** — the host dispatches by keyword. The sandbox wrapper rebuilds named parameters, so positional calls work there, and what breaks is positional-only, `*args` and non-JSON defaults. `verbose` goes to stderr through the `dspy` logger, not stdout.
- **§2 item 22: „Tier1 syntactic / Tier2 semantic / Tier3 pragmatic"** — the report took the tiers from prose. In code, Tier 1 is binary, Tier 2 is substring matching, and Tier 3 is the constant 0.3. The coverage and „contradictions non-empty" checks are not implemented. The proposal to use it „as the metric" also has to account for Refine never seeing feedback text, and Refine returning `None` when N ≤ 2 and every attempt raises.
- **§2 item 23: validate_dag** — correct, but its own test cannot fail when the function stops raising (`example_rlm_workflow.py:164-168`). The canonical program also drops dependency results on recursion.
- **§2 item 24 and §4: dspy-rlm-hooks** — the order trap is real (verified live), but three cost and safety facts were missed:
  - Speculated `llm_query` calls bypass `max_llm_calls` and are registered `pure=True`.
  - The hooks' `_execute_code` swallows terminal `CodeInterpreterError`s.
  - The documented `--variant-fn` flag does not exist.

  The „offline benchmark harness" was run: default 4.339 s, spec 3.399 s, hooks 4.823 s median of 3. It needs Deno: with Deno off PATH it fails with `CodeInterpreterError`.
- **§2 item 43: MMR** —
  - The line reference `kp_canon_retriever.py:41-46` is wrong. The constants are at `:49-59` and `select_mmr` at `:92-143`.
  - „`diversity_lambda` needs ≥0.6" is 0.534 on the fixture.
  - Missed entirely: the pack's λ is the inverse of upstream refrag's, upstream MMR ignores `min_score`, and the floor exists only in the pack's own code.
  - The target's `scripts/graphrag.py:68,175` inherited the pack's convention. It is internally consistent, but its comment „above upstream's 0.5" compares parameters of opposite meaning.
- **§5: „vendoring `sensor_advanced.py` (self-contained, MIT, no external deps beyond stdlib math per the scaffolding file read)"** — `sensor_advanced.py` imports numpy (`:13`). The stdlib-math file is the pack's scaffold, not the upstream file.
- **§4: „`drg-kg` silently returns an empty graph with only a log warning when no LM is configured … unless `DRG_REQUIRE_LM=1`"** — not reproduced on drg-kg 0.1.2 or git `g4d6970bcc` with DSPy 3.3.1. drg auto-configures `openai/gpt-4o-mini` into DSPy's global settings (it warns only about the key), reads `.env` from cwd, and attempts a live call; `DRG_REQUIRE_LM=1` does not prevent it. The real risk is an unexpected network call plus global DSPy mutation, not a green empty graph. The advice to pass `lm=` explicitly stands.
- **§4 / §5: „must be double-checked that [the `_score_sets` scorer] never touches the extraction/graph layers"** — checked. `drg.evaluation._runner` imports and runs without DSPy and without `drg.extract`. `_prf` returns 0.0 on empty sets, and `_score_sets` is multiset matching with FP/FN keys in `details`.
- **§4: „TARA's progressive-leniency retry accepts a mediocre context by lowering the bar, floor at 20/100"** — understated. The upstream loop outputs **any** context at the final retry and on diminishing returns, and routes to an agent only with zero passages. In the agentic tool the LLM applies the leniency rule (no floor) and emits `total_score` itself.
- **§1/§2: „Every skill ships a runnable `example_*.py --dry-run`"** — true, but four of the six in this slice test a plain-Python model of their package unless it is installed, and the model was wrong in three places (drg empty graph, refrag MMR, TARA routing).
- **§2 item 19** — `dspy.PythonInterpreter` is not 3.3.x-only (`reference.md:60`). It exists in 3.2.1.
- **Not in the old report at all:**
  - Deno comes via `pip install "dspy[deno]"` in 3.3.x, so `which deno` can be empty while DSPy works.
  - Pyodide 0.29.4 is fetched from npm on a cold cache, and there is about 3 s of sandbox start per forward.
  - Inputs are re-injected each iteration, and a 1000-char preview of each input goes into every prompt.
  - A block ending in an expression drops its prints, and SUBMIT is a `BaseException`.
  - A caller-owned interpreter leaks state across documents.
  - An input named `json` breaks the default sandbox.
  - Reserved names; `AdapterParseError` aborts an RLM run; `Module.get_lm()` breaks Refine for mixed-LM modules; calling `forward` directly warns.
  - `terms()` drops the four-letter names „Kael" and „Juna".

---

## Ten things the skill must say

1. At `max_iters`, `dspy.RLM` returns an extract-forced answer, never an error. Check `final_reasoning == "Extract forced final output"` and record it as „not reached" (RLM: *At `max_iters` the RLM does not fail*).
2. `max_llm_calls` caps only sub-LM calls, and exceeding it only errors inside the sandbox. Budget per forward = `max_iters` + 1 + `max_llm_calls`, plus parse retries (RLM: *`max_llm_calls` caps only sub-LM calls*).
3. 3.3.0 renamed `max_iterations` → `max_iters` and `interpreter=` → `interpreter_factory=`, with the instance passed positionally to the call; PoT and CodeAct moved too; pin it with `inspect.signature` (RLM: *The 3.2.x → 3.3.0 renames*; TEST: *Pin the RLM surface*).
4. The sandbox needs Deno 2.x, best via `pip install "dspy[deno]"` (`which deno` is not the test), fetches Pyodide on a cold cache, and costs about 3 s per forward (RLM: *The Deno requirement in 3.3.x*, *Sandbox cost*).
5. Inputs are re-injected every step and previewed (1 kB) in every prompt. A trailing expression replaces stdout, `except Exception` cannot catch SUBMIT, and a reused interpreter leaks state across documents (RLM items on re-injection, preview, expression, SUBMIT, caller-owned interpreter).
6. Tools: pass a list, write docstrings, name params, avoid reserved names and an input named `json`. Tool errors reach the model as `RuntimeError` text; an unparsable action or an outer `LMError` aborts the whole run (RLM: *The tools contract*, *Reserved names*, *An unparsable action aborts the run*).
7. The cascade metric shape (fast-fail 0.3/0.4/0.3, feedback naming the module, `validate_dag` in code) is sound. The shipped example's Tier 3 is a constant, Refine never reads feedback text, and Refine returns `None` when N ≤ 2 and every attempt fails (MET: *The verification cascade*, *The example's cascade is thinner*; API: *Refine returns `None`*).
8. dspy-rlm-hooks: enable hooks before speculation. Speculated `llm_query` calls are paid and bypass `max_llm_calls`, and hooks convert terminal interpreter errors into prompts; pin DSPy together with the package (RLM: *The ordering trap, confirmed*; PROD: *Speculation spends …*, *Hooks turn terminal …*).
9. MMR: say which term λ weights. The pack's λ is the inverse of upstream refrag's, upstream MMR ignores `min_score`, and the floor must be your own code. The measured crossover on the fixture is 0.534, and the floor is irrelevant below 0.498. refrag's selection never shrinks the prompt (RAG: *Upstream MMR weights relevance*, *Upstream MMR ignores `min_score`*, *The MMR fixture, measured exactly*, *The selection that never shrinks the prompt*).
10. Third-party behaviour must be probed, not read off signatures. drg auto-configures a global LM and calls it despite `DRG_REQUIRE_LM` (always pass `lm=`), and its implicit relationships are on by default. TARA outputs any context at the final retry and lets the LLM do its arithmetic. Four of the six dry-runs test a model of the package, not the package (PROD: *drg configures DSPy's global LM*; TRAP: *TARA outputs any context at the final retry*; TEST: *Four of six dry-runs never touch their package*).
