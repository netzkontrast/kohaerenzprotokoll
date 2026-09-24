# dspydantic — DSPy knowledge extracted (slice: whole repo except uv.lock)

## 1. Header

- **Repo:** `/home/user/dspydantic` (github.com/netzkontrast/dspydantic; docs and README point at upstream `davidberenstein1957/dspydantic`). **Commit:** `1afc528` (2026-03-20, "fix: validation leakage and unfair baseline causing inflated 100% metrics (#23)"). Package version `0.1.6` (`src/dspydantic/__init__.py:3`).
- **License:** contradictory. `LICENSE` is Apache-2.0 (`LICENSE:1-3`), README says Apache 2.0 (`README.md:8,197`), `pyproject.toml:7` says `license = {text = "MIT"}` and `pyproject.toml:15` has the MIT classifier.
- **DSPy targeted:** `dspy>=3.0.4` (`pyproject.toml:24`), Python `>=3.11` (`pyproject.toml:6`); the docs say "Python 3.10+" (`docs/index.md:229`). **Against DSPy 3.3.1:** the core calls work (a `dspy.Signature` subclass built with `type()`, `dspy.ChainOfThought`, `dspy.Prediction`, `dspy.Example.with_inputs`, `Teleprompter.compile`), and the offline unit suite passes. End to end, **several default paths break on 3.3.1**:
  - every image/PDF path (`dspy.Image.from_url` no longer takes data URIs);
  - the auto-selected optimizer for n≥20 (`num_candidates` passed to `BootstrapFewShotWithRandomSearch`);
  - the auto-selected optimizer for n≤2 (MIPROv2 needs the optional `optuna` extra);
  - `optimizer="gepa"` (the metric takes 3 arguments; GEPA needs 5);
  - `Prompter.predict` for any model with a PEP 604 `X | None` field (a bug in dspydantic itself, not a version issue).
- **What it is:** a library that tunes Pydantic `Field(description=...)` strings and optional system/instruction prompts for LLM structured extraction. The DSPy program being optimized is a per-field *description rewriter* (ChainOfThought: field_name, description, type → improved description). The metric runs a separate extraction call (`"prompt -> json_output"`) with the rewritten descriptions embedded in a JSON schema and compares the result field by field with `expected_output`. There are two APIs: `PydanticOptimizer` (low level) and `Prompter` (optimize, predict, save, load).
- **What I ran** (all offline, keys unset). V/ = `<scratchpad>/verify/dspydantic/`:
  - I made a `git archive 1afc528` copy under `scratchpad/copies/dspydantic` and a throwaway venv `scratchpad/venvs/dspydantic` (uv, Python 3.11) with `dspy==3.3.1`, pydantic 2.13.5, deepdiff 9.1.0, pillow, pdf2image, rich and pytest; `optuna 5.0.0` was added later for the MIPROv2 runs.
  - pytest with `V/offline_plugin.py`, which strips `*_API_KEY` and makes every `litellm.completion/acompletion/responses` raise and count.
  - Scripts, each driven by `V/fx.py`, an offline `FixtureLM(dspy.BaseLM)` that answers any ChatAdapter output fields it is asked for (plus a `dspy.LM` subclass variant):
    - `V/v_construct.py`: auto-selection and constructing every string optimizer.
    - `V/v_eval.py`: evaluators and metric behaviour.
    - `V/v_schema.py`: schema walk, model rebuild, Prompter behaviour.
    - `V/v_run.py`: end-to-end `optimize()` across modes and optimizers, with LM request counts.
    - `V/v_scored.py`: returned vs scored descriptions; compile_kwargs fallback.
    - `V/v_proposer.py`: what MIPROv2's proposer sees.
    - `V/v_docs.py`: doc snippets run as written.
  - Inline checks, cited below as **I1–I10**:
    - I1: `dspy.configure` from a worker thread.
    - I2: reserved field names and `optimized_` prefix stripping.
    - I3: which scoring calls carry few-shot demos.
    - I4: dump of the exact prompts the LM receives.
    - I5: the placeholder-preservation branch driven by a stub predictor.
    - I6: the integration tests' MIPROv2 kwargs recipe.
    - I7: reading `SentenceTransformer.encode` in the sentence-transformers 6.1.0 wheel (downloaded, not installed).
    - I8: nested `$ref` schema shape under pydantic 2.5.3 vs 2.9.2 (via `uv run --with`).
    - I9: coverage of the doc code blocks.
    - I10: effective optimizer kwargs read back from constructed teleprompters.
  - `inspect.signature` and source greps of DSPy 3.3.1 (`V/sigs.py`).

---

## API

- **Signature class built at runtime with `type()`** — `type(f"Optimize{model_name}FieldDescription", (dspy.Signature,), {"__doc__": docstring, "__annotations__": {"field_name": str, "field_description": str, "field_type": str, "optimized_field_description": str}, "field_name": dspy.InputField(desc=...), ..., "optimized_field_description": dspy.OutputField(desc=...)})`. Both `__annotations__` and the `InputField`/`OutputField` objects must be in the namespace dict. `src/dspydantic/module.py:50-95` (system prompt `98-124`, instruction prompt `127-154`) [api] (verified: compiled by BootstrapFewShot, COPRO and MIPROv2 in V/v_run.py on 3.3.1) → here: job 4, pairs.py (signatures built from data).
- **What the LM sees of a class-based signature** — the docstring becomes the objective line ("In adhering to this structure, your objective is: Improve a field description for Invoice structured data extraction. Output ONLY the improved description — a short descriptive phrase, not instructions."). Every InputField name and value is rendered. **The class name reaches no prompt**, neither the task call nor any MIPROv2 proposer call. `module.py:67-71` [api] (verified: I4 prompt dump; V/v_proposer.py plus a recount found `OptimizeMedicalRecordFieldDescription` in 0 of 38 proposer requests and 0 of all 92 requests, and the docstring in 12 of 12 `proposed_instruction` requests) → here: job 4 (context goes in instructions or input fields, never in class names).
- **String signatures get DSPy's generic instruction** — the extraction predictor `dspy.ChainOfThought("prompt -> json_output")` is shown to the LM as "Given the fields `prompt`, produce the fields `json_output`.", the same meta-instruction pattern the cd5c89d fix removed from the rewriter. It is never optimized. `src/dspydantic/evaluators/functions.py:329-333`, `src/dspydantic/utils.py:238-239` [api] (verified: I4) → here: lmrun.py callers (write instructions explicitly).
- **Image signatures** — `build_image_signature_and_kwargs`: no images → `"prompt -> json_output"`; one image → `"prompt, image -> json_output"` with kwargs `{"prompt": None, "image": img}`; more → `"prompt, images: list[dspy.Image] -> json_output"`. `utils.py:209-252` [api] (verified: unit tests `tests/unit/test_utils.py` pass).
- **Judge and grader signatures** — `"prompt -> evaluation"` (`functions.py:120-122`, `evaluators/score_judge.py:101-102`) and `"prompt -> label_selection"` (`evaluators/label_model_grader.py:111-112`). All are ChainOfThought with free-text outputs, parsed by hand; DSPy's typed/Pydantic output fields are never used [api].
- **Predictors held in a plain dict are discovered by optimizers** — `self.field_optimizers: dict[str, dspy.ChainOfThought]` (`module.py:192-194`). DSPy's `named_parameters` walks dict attributes, so MIPROv2 counted all 5 predictors of a 5-field model: 25 trials zero-shot = int(2·5·log2 6); 51 trials few-shot = int(2·10·log2 6) [api] (verified: V/v_run.py printed "num_trials: 25" and "num_trials: 51").
- **Dotted field paths as forward kwargs** — the program is called as `optimized_program(**{"address.street": desc, "field_type_address.street": "str", ...})`. `forward(self, system_prompt=None, instruction_prompt=None, **field_descriptions)` (`module.py:236-241`) skips keys starting with `field_type_` (`module.py:257-258`). Example keys contain dots and `with_inputs(*input_keys)` accepts them. `src/dspydantic/optimizer.py:832-845,902,1863-1875` [api] (verified: nested-model runs in V/v_run.py).
- **Prediction keys** — forward returns `dspy.Prediction(**optimized)` with keys `optimized_<path>`, `optimized_system_prompt` and `optimized_instruction_prompt` (`module.py:252-370`) [api].
- **Examples: inputs vs labels** — each `dspy.Example` holds `input_data`, `expected_output`, every description (key = field path), `field_type_<path>`, `system_prompt`, `instruction_prompt`. `with_inputs` marks only descriptions, types and prompts as inputs. The DSPy program therefore sees **identical inputs for every training example**; the data enters only through the metric (which reads `input_data`/`expected_output`) and MIPROv2's dataset summarizer. `optimizer.py:832-902` [pattern] (verified: I4 — the rewrite call's user message holds only `field_name`, `field_description`, `field_type`).
- **`dspy.Image` in 3.3.1** — `Image.from_url(url)` accepts only http(s) and downloads the resource (`dspy/adapters/types/image.py:116-127`: "Image.from_url requires an HTTP(S) URL, received: ..."). A data URI goes through `dspy.Image(data_uri)` / `dspy.Image(url=...)` (`image.py:37-106`). `Image.from_file` and `Image.from_PIL` are deprecated, "will be removed in 3.4" (`image.py:137-149`). dspydantic calls `dspy.Image.from_url(f"data:image/png;base64,{b64}")` (`utils.py:188-191`) [api] (verified: V/v_schema.py #7 ValueError) → here: check_dspy_surface.py.
- **Image encoding** — every base64 image is labelled `data:image/png` whatever the real format (`utils.py:188`). `image_to_base64` flattens RGBA/LA/P onto white RGB and re-encodes PNG (`utils.py:66-79`). PDFs are rasterized with `pdf2image.convert_from_path(dpi=pdf_dpi)` (default 300) to one PNG per page (`utils.py:15-47`), so a PDF's text layer is never used [api].
- **`dspy.configure` is owned by one thread (3.3.1)** — reconfiguring from another thread raises `RuntimeError: dspy.settings can only be changed by the thread that initially configured it.` (`dspy/dsp/utils/settings.py:127`). `Prompter(model_id=...)` calls `dspy.configure` (`prompter.py:75-76`) and therefore fails in worker threads once the main thread has configured. Use `dspy.context(lm=...)` there [api] (verified: I1) → here: lmrun.py (thread-local `dspy.context`, never `configure` in workers).
- **`dspy.settings.lm = None` works** — direct attribute assignment on settings is accepted in 3.3.1 (`tests/unit/test_prompter.py:514`) [api] (verified: I1 and the unit test passes).
- **LM history mechanics (3.3.1)** — each call appends `{prompt, messages, kwargs, response, outputs, usage, cost, timestamp, uuid, model, response_model, model_type}` (`dspy/clients/base_lm.py:299-314`). The per-instance cap is `settings.max_history_size = 10000` (`settings.py:35`). `lm.copy()` resets `new_instance.history = []` (`base_lm.py:735-756`). Cached responses carry `cache_hit=True` (`dspy/clients/cache.py:157`), are skipped by the usage tracker (`base_lm.py:294`), but are still written to history [api] (verified: source read) → here: lmrun.py.
- **A `dspy.BaseLM` that is not a `dspy.LM`** — calling it with several positional arguments raises `TypeError: Legacy BaseLM calls accept at most one positional prompt...` [api] (verified: V/v_eval.py B').
- **`Prompter` constructor** — `Prompter(model=None, model_id=None, api_key=None, cache=False, system_prompt=None, instruction_prompt=None, optimized_descriptions=None, optimized_system_prompt=None, optimized_instruction_prompt=None, optimized_demos=None)` (`prompter.py:124-177`). Other methods: `load(path, model=None, model_id=None, api_key=None, cache=False)` (179-223), `from_optimization_result(model, result)` (225-252), `optimize(examples, evaluate_fn=None, optimizer=None, train_split=0.8, num_threads=4, verbose=False, exclude_fields, include_fields, evaluator_config, sequential=False, parallel_fields=True, max_val_examples, skip_score_threshold, on_progress, **kwargs)` (254-339), `predict` (365-512), `run` (751-777, an alias), `predict_with_confidence` (546-584), `predict_batch(inputs, max_workers=4, on_error="raise")` (623-666), `apredict` (668-704, `run_in_executor(None, ...)`), `apredict_batch(inputs, max_concurrency=4, on_error="raise")` (706-749, a Semaphore plus `asyncio.gather`), `save(path)` (779-812) [api].
- **`PydanticOptimizer` constructor defaults** — `model, examples, evaluate_fn=None, system_prompt=None, instruction_prompt=None, num_threads=4, init_temperature=1.0, verbose=False, optimizer=None, train_split=0.8, optimizer_kwargs=None, compile_kwargs=None, exclude_fields=None, include_fields=None, evaluator_config=None, sequential=False, parallel_fields=True, max_val_examples=None, skip_score_threshold=None, skip_field_description_optimization=False, skip_system_prompt_optimization=False, skip_instruction_prompt_optimization=False, early_stopping_patience=None, auto_generate_prompts=False, on_progress=None`. There is no `model_id`/`api_key` parameter even though the class docstring shows them (`optimizer.py:67-105,148-182`). `optimizer.py:190-221` [api] (verified: V/v_docs.py; `model_id=` → TypeError).
- **How `Prompter.predict` extracts** — it builds a text prompt (System/Instruction/JSON schema/Examples/Input text), calls `dspy.ChainOfThought(signature)(prompt=...)`, then `_parse_json_output`: `json.loads`, then the first balanced `{...}`, then a greedy `\{.*\}`. It validates with `create_optimized_model(model, descriptions).model_validate(...)`. `prompter.py:398-512,514-544` [pattern].
- **`extract_field_descriptions` walk** — walks `model_json_schema()` into dot paths. It resolves only `"$ref"` values starting with `#/$defs/` (`extractor.py:11-16`) and falls back to the field name when a field has no description (`extractor.py:78-81`). Lists of models flatten to `items.name` with no index (`extractor.py:88-98`). `extractor.py:19-101` [api].
- **`extract_field_types` output** — formats annotations as strings: `"str"`, `"list[str]"`, `'Literal["a", "b"]'`, `'Enum["x", ...]'`, `"UnionType[Address, NoneType]"` for PEP 604, `"Union[int, NoneType]"` for `typing.Optional`. It reads `model_cls.__annotations__` (`extractor.py:192-199`), so inherited fields are missing. `extractor.py:104-223` [api] (verified: V/v_schema.py #1, #4).
- **`apply_optimized_descriptions`** — returns a deep copy of the JSON schema with descriptions replaced in `properties` and `$defs`, for use as a JSON-schema response format. `extractor.py:226-308` [api].
- **`Example` inputs** — `Example(expected_output=None, text=None, image_path=None, image_base64=None, pdf_path=None, pdf_dpi=300)`. `text` may be a dict: it is stored as `text_dict`, and the input text becomes the first truthy value of `"text"`, `"review"`, `"content"`, `"input"`, or else all values joined by spaces. `types.py:170-231` [api].
- **Result and progress types** — `OptimizationResult(optimized_descriptions, optimized_system_prompt, optimized_instruction_prompt, metrics, baseline_score, optimized_score, optimized_demos=None, api_calls=0, total_tokens=0, estimated_cost_usd=None)` (`types.py:12-38`). `FieldOptimizationProgress(phase, score_before, score_after, improved, total_fields, field_path, field_index, elapsed_seconds, optimized_value)` with phases `baseline|fields|skipped|system_prompt|instruction_prompt|complete` (`types.py:41-71`). `PrompterState` (`types.py:74-99`) [api].
- **The only LM dspydantic creates** — `dspy.LM(model_id, api_key=api_key, cache=cache_dir is not None)`, created only when `model_id` is given **and** `dspy.settings.lm is None`. `prompter.py:69-79` [api].

## OPT

- **Auto-selection by n** — n≤2 → `"miprov2zeroshot"`; 3≤n<20 → `"bootstrapfewshot"`; n≥20 → `"bootstrapfewshotwithrandomsearch"`. `optimizer.py:512-533` [recipe] (verified: V/v_construct.py for n=1,2,3,4,19,20,50) → here: pairs.py (57 labelled pairs; the thresholds are unmeasured, see TRAP).
- **"Fast mode" kwargs table** — `_FAST_MODE_KWARGS = {"bootstrapfewshot": {"max_bootstrapped_demos": 1}, "bootstrapfewshotwithrandomsearch": {"max_bootstrapped_demos": 1, "num_candidates": 4}, "miprov2": {"auto": "light", "max_bootstrapped_demos": 1}, "miprov2zeroshot": {"auto": "light"}}`. Applied whenever `sequential=False` (the default) and the optimizer is not custom; user `optimizer_kwargs` override it. `optimizer.py:24-30,398-403` [api] (verified: V/v_construct.py printed the merged kwargs).
- **Effective constructor kwargs** — merged as `{**default_kwargs, **self.optimizer_kwargs}`.
  - `miprov2zeroshot`: `metric, num_threads, init_temperature, auto="light", max_bootstrapped_demos=0, max_labeled_demos=0` (`optimizer.py:910-919`).
  - `miprov2`: `auto="light"`, and for n≤10 `max_bootstrapped_demos=2, max_labeled_demos=2` (`optimizer.py:920-930`), but fast mode overrides the bootstrapped count to 1.
  - Generic class: `metric` plus `num_threads` when `"num_threads" in inspect.signature(cls.__init__).parameters` (`optimizer.py:937-945`).
  - `bootstrapfewshot` with n<5: `max_bootstrapped_demos = max(1, min(2, n-1))` (`optimizer.py:946-947`), again overridden to 1 in single-pass.
  - Observed: n=5 single-pass miprov2 → `max_bootstrapped_demos=1, max_labeled_demos=2`; sequential → 2/2; n=12 single-pass → 1/4; n=2 → 0/0; n=3,4 sequential bootstrapfewshot → 2.
  
  [api] (verified: I10 table, printed from constructed teleprompters).
- **String → teleprompter registry** — the lowercased `__name__` of every `Teleprompter` subclass, found recursively, plus the alias `miprov2zeroshot` → MIPROv2. `optimizer.py:438-469`. On 3.3.1: `avataroptimizer, bettertogether, bootstrapfewshot, bootstrapfewshotwithoptuna, bootstrapfewshotwithrandomsearch, bootstrapfinetune, copro, ensemble, finetuneteleprompter, gepa, inferrules, knnfewshot, labeledfewshot, miprov2, simba` (+`miprov2zeroshot`) [api] (verified: V/v_construct.py).
- **Which strings actually construct (3.3.1, dspydantic's generic call)** — Constructed: `bettertogether`, `bootstrapfewshot`, `bootstrapfewshotwithoptuna`, `bootstrapfinetune`, `copro`, `inferrules`, `simba`, and `miprov2`/`miprov2zeroshot` once an LM is configured. Failed:
  - `bootstrapfewshotwithrandomsearch`: `unexpected keyword argument 'num_candidates'`, in single-pass mode only.
  - `gepa`: "GEPA metric must accept five arguments: (gold, pred, trace, pred_name, pred_trace)".
  - `labeledfewshot`, `ensemble`, `finetuneteleprompter`: `unexpected keyword argument 'metric'`.
  - `knnfewshot`: missing `k`, `trainset`, `vectorizer`.
  - `avataroptimizer`: `AttributeError: module 'dspy' has no attribute 'TypedPredictor'` (`dspy/teleprompt/avatar_optimizer.py:90`), a DSPy 3.3.1 defect.
  
  [trap] (verified: V/v_construct.py) → here: check_dspy_surface.py.
- **DSPy 3.3.1 compile signatures that matter** — `BootstrapFewShot.compile(student, *, teacher=None, trainset)` (no valset); `BootstrapFewShotWithRandomSearch.compile(..., valset=None, restrict=None, labeled_sample=True)`; `MIPROv2.compile(student, *, trainset, teacher=None, valset=None, num_trials=None, max_bootstrapped_demos=None, max_labeled_demos=None, seed=None, minibatch=True, minibatch_size=35, minibatch_full_eval_steps=5, program_aware_proposer=True, data_aware_proposer=True, view_data_batch_size=10, tip_aware_proposer=True, fewshot_aware_proposer=True, requires_permission_to_run=None, provide_traceback=None)`; `GEPA.compile(student, *, trainset, teacher=None, valset=None)`; `COPRO.compile(student, *, trainset, eval_kwargs=None)`; `SIMBA.compile(student, *, trainset, seed=0)`; `InferRules.compile(student, *, teacher=None, trainset, valset=None)`; `KNNFewShot.compile(student, *, teacher=None)`; `LabeledFewShot.compile(student, *, trainset, sample=True)` [api] (verified: V/sigs.py) → here: check_dspy_surface.py.
- **BFRS's candidate count is `num_candidate_programs`** — `BootstrapFewShotWithRandomSearch(metric, teacher_settings=None, max_bootstrapped_demos=4, max_labeled_demos=16, max_rounds=1, num_candidate_programs=16, num_threads=None, max_errors=None, stop_at_score=None, metric_threshold=None)`; there is no `num_candidates`. dspydantic's fast kwargs therefore crash the **default** path for n≥20. Introduced in 624d2ac (`fast` was opt-in); it became the default in 7901f6d (`if self.fast` → `if not self.sequential`) [trap] (verified: V/v_construct.py "n=20 default ... TypeError"; git show 624d2ac/7901f6d).
- **Valset feature detection by exception** — for names in `("miprov2zeroshot","miprov2","gepa","bootstrapfewshotwithrandomsearch","copro","simba","custom")` it calls `compile(program, trainset=..., valset=..., **compile_kwargs)` and on `TypeError` retries `compile(program, trainset=...)`, **dropping compile_kwargs**. Every other name calls `compile(program, trainset=..., **compile_kwargs)` with no fallback. `optimizer.py:1830-1861` (same at `1061-1088`, `1194-1221`) [trap] (verified: V/v_scored.py: a custom teleprompter saw `['num_trials','valset']`, then `[]`) → here: check_dspy_surface.py (probe with `inspect.signature`, not with exceptions).
- **MIPROv2 needs `optuna` in 3.3.1** — optuna is an optional extra (`Requires-Dist: optuna>=3.4.0; extra == "optuna"`). MIPROv2 raises `ImportError: MIPROv2 requires optional dependency 'optuna'. Install it with `pip install dspy[optuna]`.` at compile time, **after** bootstrapping and instruction proposal have spent LM calls (`dspy/teleprompt/mipro_optimizer_v2.py:28-38,520`). dspydantic's default for n≤2 hits this on a fresh `pip install dspydantic` [trap] (verified: V/v_run.py failed after "Proposing N=6 instructions") → here: .venv-dspy install notes.
- **MIPROv2 auto and num_trials are mutually exclusive** — auto set plus `num_trials` or `num_candidates` → `ValueError("If auto is not None, num_candidates and num_trials cannot be set...")`. With `auto=None` both are required ("If auto is None, num_trials must also be provided. Given num_candidates=N, we'd recommend setting num_trials to ~M" / "If auto is None, num_candidates must also be provided."). `mipro_optimizer_v2.py:153-167` [api] (verified: V/v_proposer.py first attempt raised it) → here: pairs.py ladder config.
- **Recipe: small MIPROv2 run** — `optimizer_kwargs={"auto": None, "num_candidates": 3}` + `compile_kwargs={"num_trials": 3, "minibatch": False}` (`tests/integration/test_miprov2_descriptions.py:308-309`). It is valid only with an explicit `optimizer="miprov2..."`; with the auto-selected BootstrapFewShot it raises `BootstrapFewShot.__init__() got an unexpected keyword argument 'auto'` [recipe] (verified: I6 ran it end to end with 53 fixture requests; V/v_docs.py #10).
- **MIPROv2 auto budgets** — `AUTO_RUN_SETTINGS = {"light": {"n": 6, "val_size": 100}, "medium": {"n": 12, "val_size": 300}, "heavy": {"n": 18, "val_size": 1000}}` (`mipro_optimizer_v2.py:46-49`). `num_trials = int(max(2*num_vars*log2(n), 1.5*n))` with `num_vars = len(program.predictors())`, doubled unless zero-shot (280-286). Instruction candidates = n when zero-shot, else `int(n*0.5)`; few-shot candidates = n (309-312). Minibatching turns on only when `len(valset) > MIN_MINIBATCH_SIZE = 50` (44, 307) [api] (verified: printed "num_trials: 25 / num_instruct_candidates: 6" zero-shot and "51 / 3" few-shot for 5 predictors).
- **MIPROv2 without a valset** — needs ≥2 train examples and takes the **last 80%** of the trainset as valset (`valset_size = min(1000, max(1, int(len(trainset)*0.80)))`). `mipro_optimizer_v2.py:320-330` [api].
- **MIPROv2 bootstraps even in zero-shot** — with `max_bootstrapped_demos=0, max_labeled_demos=0` it still logs "Bootstrapping set 1/6 … 6/6" [api] (verified: V/v_run.py output).
- **BootstrapFewShot treats any positive float as success** — `if self.metric_threshold: success = metric_val >= self.metric_threshold else: success = metric_val` (`dspy/teleprompt/bootstrap.py:206-214`); with `metric=None`, `success = True`. dspydantic never sets `metric_threshold`, so a rewrite scoring 0.25 becomes a demo [trap] (verified: V/v_run.py "Bootstrapped 1 full traces" at metric 0.5) → here: pairs.py (set `metric_threshold` or return a bool).
- **SIMBA minimum trainset** — `assert len(trainset) >= self.bsize, f"Trainset too small: {len(trainset)} < {self.bsize}"`, default `bsize=32` (`dspy/teleprompt/simba.py:33,105`) [api] (verified: V/v_run.py "Trainset too small: 4 < 32") → here: pairs.py (residual after `fold()` is 24 < 32: set `bsize`).
- **GEPA in 3.3.1** — the metric must bind five arguments (checked in `__init__`, `dspy/teleprompt/gepa/gepa.py:~418-421`); exactly one of `auto`/`max_full_evals`/`max_metric_calls` is required (~427-430); `reflection_lm` is required unless a custom `instruction_proposer` is given (docstring 256, 286-287, 361). No keyword `num_iterations` exists [api] (verified: V/v_construct.py, V/v_docs.py 6b) → here: pairs.py, job 4.
- **Constructors the docs show fail on 3.3.1** — `MIPROv2(auto="light", num_threads=8)` → missing `metric`; `GEPA(num_iterations=10, verbose=True)` → unexpected `num_iterations`; `SIMBA()` → missing keyword-only `metric`; `BetterTogether(optimizers=[...])` → missing `metric` (the real signature is `BetterTogether(metric, **optimizers)`); `Ensemble(programs=..., method=...)` against `Ensemble(*, reduce_fn=None, size=None, deterministic=False)` with `compile(programs)`. `docs/guides/advanced/configure-optimizations.md:205,260,284,308,338` [trap] (verified: V/v_docs.py #6; Ensemble from V/sigs.py).
- **A custom Teleprompter instance brings its own metric** — `_create_teleprompter` returns `self.custom_optimizer` unchanged (`optimizer.py:908-909`), so dspydantic's extraction metric is never attached. The class docstring's example `MIPROv2(metric=lambda x, y, trace=None: 0.9, ...)` (`optimizer.py:128-138`) would optimize against a constant. `BootstrapFewShot(max_bootstrapped_demos=4)` and `COPRO(verbose=True)` have `metric=None` [trap] (verified: V/v_docs.py 6f/6g).
- **One custom optimizer instance, many compiles** — in sequential mode the same instance compiles every field and both prompts, concurrently under `parallel_fields=True` (`optimizer.py:1059,1192,1006`) [trap].
- **Single-pass flow** — baseline on val → one `compile` → one call `optimized_program(**original_descriptions)` whose outputs are **returned** (`optimizer.py:1863-1895`) → a **separate** program call per val example, whose outputs are **scored** (1901-1967) → revert everything if the score fell (1976-1987); on an exact tie, revert each field and prompt that grew longer (1988-2005) [pattern] (verified: V/v_scored.py).
- **Sequential flow** — the baseline is computed on the **full** val set (`optimizer.py:1296-1316`). Fields are sorted deepest first (`499-510`) and each is compiled alone with `PydanticOptimizerModule(field_descriptions={path: desc}, ...)` (`1040-1047`), scored on the capped val set (`1329-1334`), then the system prompt and the instruction prompt (`1451-1503`), then a global revert if worse (`1505-1519`) [pattern].
- **Per-field acceptance rule** — `if new_score > baseline_score: accept; if new_score == baseline_score and len(new) <= len(original): accept; else keep current`. `optimizer.py:1124-1133` (prompts `1259-1269`) [recipe]. For n≤20 it is decided on 1–4 validation examples (see DATA).
- **Measured LM request counts** — offline fixture, cache off, a model with 5 description fields (`name`, `age`, `address`, `address.street`, `address.city`), n=5 unless noted:
  - single-pass BootstrapFewShot: 18 requests (15 rewrite + 3 extraction);
  - n=1: 18;
  - sequential + parallel: 52 (25 + 27);
  - sequential without parallel, `early_stopping_patience=1`: 11;
  - sequential without parallel, `skip_score_threshold=0.5`: 6 (extraction only);
  - COPRO `breadth=2, depth=1`: 257;
  - miprov2zeroshot, n=2: 290;
  - miprov2, n=5: 395;
  - BFRS `num_candidate_programs=2`, n=20, sequential without parallel: 329;
  - FAST_MIPRO recipe on a 2-field model: 53.

  These are counts of fixture calls, not latency or cost; a real LM with DSPy's cache on would repeat fewer. [number] (verified: V/v_run.py, I6) → here: baseline.py (record counts with conditions).
- **Documented call estimates are unmeasured and contradicted** — docs say "MIPROv2 (light) ~50", "MIPROv2 | Fast | Fair | Low", and "For 10 examples with a 5-field model: MIPROv2 ~17, BootstrapFewShot ~42, BFRS ~82, COPRO ~122" (`docs/explanation/how-optimization-works.md:94-106`, `docs/reference/optimizers.md:21,84-89`). The fixture runs above measured 290–395 requests for MIPROv2 light [claim] (verified: contradiction measured in V/v_run.py).
- **The "BootstrapFewShot bug" at n≤2 is never described** — the code comment "avoids BootstrapFewShot bug" (`optimizer.py:516,526`, added in ae822b3) gives no reproduction. BootstrapFewShot compiled at n=1 on 3.3.1 [claim] (verified: V/v_run.py "single-pass n=1" ran).
- **Optimizer names are case-insensitive** — `optimizer.lower()` (`optimizer.py:378`); an invalid name raises `ValueError("optimizer '<x>' is not a valid Teleprompter subclass. Valid options: [...]")` (381-386); a non-string non-Teleprompter raises TypeError (393-396) [api].
- **`init_temperature`** — passed only to MIPROv2 (default 1.0; `optimizer.py:914,924`) [api].
- **`auto_generate_prompts=True` text** — system prompt `"You are an expert at extracting structured {Model} data from text. Be precise and faithful to the source text."`, instruction `"Extract the following fields from the given text: {comma-joined field paths}. Return only values that are explicitly stated or clearly implied."`; only fills prompts that are `None`. `optimizer.py:412-424` [recipe].
- **Speed claim in commit b787d2e** — "sequential+parallel is fastest … (57s vs 64s in ablation study)". It was measured before the leakage fix, and the ablation script's only live config is mislabelled (see TRAP) [claim].

## MET

- **Metric contract** — `metric_function(example: dspy.Example, prediction: dspy.Prediction, trace=None) -> float`. It maps prediction keys to fields (`optimized_system_prompt` and `optimized_instruction_prompt` special-cased, other `optimized_*` keys become field paths), falls back to the current descriptions and prompts when the prediction has none (baseline), and converts the `dspy.Example` back into an `Example`. A non-numeric or out-of-range score **returns 0.0** (it is not clamped). `optimizer.py:617-691` (single field: `693-729`) [api].
- **Default evaluator** — extracts with the global LM, parses JSON (`json.loads` → one-level-nesting regex `\{(?:[^{}]|(?:\{[^{}]*\}))*\}` → greedy `\{.*\}`). Unparseable output → **0.0**, non-dict → **0.0**. `functions.py:341-368` [api] (verified: V/v_eval.py G) → here: lmrun.py (count these as `unparsed`, not as a score).
- **Field aggregation** — scores leaf paths only, i.e. paths that prefix no other path (`functions.py:501-515`), filtered by `include_fields`/`exclude_fields` with exact-or-prefix matching (517-542). Both values `None` → 1.0; exactly one `None` → 0.0 (551-556); the result is the mean (563). When no leaves remain it falls back to comparing the whole structure (564-566); the final score is clamped to [0, 1] (568) [api] → here: job 2 (entity-list scoring).
- **Nested values** — when either side is a dict or list, it uses `DeepDiff(expected, extracted, ignore_order=False, verbose_level=0, get_deep_distance=True)`: an empty diff → 1.0; if the **default** evaluator is `StringCheckEvaluator` → a binary result on `deep_distance == 0`; otherwise `1 - deep_distance`. Field overrides are consulted **only for primitive values**. `functions.py:449-499` [api].
- **Evaluator registry** — names `exact`, `string_check` → StringCheckEvaluator; `levenshtein`; `text_similarity`; `score_judge`, `score_model_grader` → ScoreJudge; `label_model_grader`; `python_code`; `predefined_score`. `evaluators/__init__.py:13-21` [api].
- **EvaluatorFactory.create forms** — a string name → `cls(config={})` (no LM injected); a class → `cls(config={})`; `{"class": C, "config": {...}}` or `{"type": name, "config": {...}}` → `default_lm` injected as `config["lm"]` **by mutating the caller's dict**; a dict with neither key → `ValueError`. `evaluators/config.py:110-157` [api] (verified: V/v_eval.py H, where the config gained key `lm`).
- **Evaluators are rebuilt per call** — `default_evaluate_fn` calls `EvaluatorFactory.create` inside every `evaluate()` call, i.e. per example (`functions.py:417-425`); state (a loaded embedding model, a score cursor) never survives between examples [trap].
- **StringCheckEvaluator (`exact`)** — `str(a) == str(b)` after `.strip()` (`strip_whitespace=True`), case-sensitive by default (`evaluators/string_check.py:39-40,60-71`). `30.0` vs `30` → 0.0; `True` vs `"true"` → 0.0; `"30"` vs `30` → 1.0 [api] (verified: V/v_eval.py J).
- **LevenshteinEvaluator** — `1 - distance/max_len` on stripped `str()`s; identical → 1.0; both empty → 1.0; below `threshold` (default 0.0) → 0.0. Pure-Python O(n·m) DP. `evaluators/levenshtein.py:42-95` [api]. For "John Smith"/"Jon Smith" it gives 0.9, matching `docs/explanation/understanding-evaluators.md:66`.
- **TextSimilarityEvaluator** — config `model` (default `"sentence-transformers/all-MiniLM-L6-v2"`), `provider` (`"sentence-transformers"`|`"openai"`), `api_key`, `threshold` (0.0) (`evaluators/text_similarity.py:44-47`). Equal strings → 1.0 (120-121); cosine similarity; **any exception → exact-match fallback** (127-129). The sentence-transformers branch calls `encode(texts, convert_to_numpy=False).tolist()` (77), but with `convert_to_numpy=False` (and `convert_to_tensor=False`) `encode` returns a Python list of tensors, which has no `.tolist()`. The evaluator therefore always falls back and returns 0.0 for any non-identical pair [trap] (verified: I7 read `sentence_transformers/sentence_transformer/model.py` 6.1.0 `encode()` tail, the list returned when neither conversion flag is set; not executed, torch not installed).
- **ScoreJudge** — config `criteria` (default `"Rate the quality on a scale of 0-1"`), `lm`, `temperature` (0.0), `system_prompt` (`evaluators/score_judge.py:47-50`). The prompt includes `Expected value: {expected}` even when it is None (84). Parsing: `json.loads(...)["score"]` (default 0.5 if the key is missing) → regex `"score"\s*:\s*([0-9.]+)` → regex `\b(0\.\d+|1\.0|1)\b` → **0.5**; the result is clamped (111-131). **`lm` and `temperature` are read but never used**; the judge runs on `dspy.settings.lm` (76-102) [trap] (verified: V/v_eval.py C: 0 calls to the configured judge LM).
- **default_judge_fn** — the same cascade, with `logger.warning("LLM judge returned text that could not be parsed; defaulting to 0.5. ...")` (`functions.py:127-161`). Its `lm` argument is unused, so `evaluate_fn=<dspy.LM judge>` is silently ignored. Observed outcomes: `'I cannot judge this'` → 0.5; `'{"score": "high"}'` → 0.5; `'{"score": 85}'` → 1.0 (clamped); `'Score: 8 out of 10, confidence 1'` → 1.0 (stray "1"); `'The extraction is 100% correct'` → 0.5 [trap] (verified: V/v_eval.py B, F) → here: lmrun.py `unparsed` status.
- **LabelModelGrader** — requires non-empty `allowed_labels` (ValueError otherwise). Options: `exact_match_score` 1.0, `partial_match_score` 0.5 (`evaluators/label_model_grader.py:45-50`). It raises if no global LM is configured, even when it will not call one (70-76). Case-insensitive exact match → 1.0 (83-84). **If the expected label is in the allowed set, it never calls the LM**: it only checks substring relations → 0.5 or 0.0 (137-151). Only an expected label outside the allowed set triggers an LLM "select the best matching label" call; its output is compared with substring rules, so an empty label gives `"" in expected` → 0.5 (88-136). Observed: `("good","positive")` → 0.0 with 0 LM calls (the docstring promises "Semantic match via LLM → 0.5"); `("pos","positive")` → 0.5; `("positive!","positive")` → 0.5 [trap] (verified: V/v_eval.py D, D').
- **PythonCodeEvaluator** — `config["function"]` is called as `fn(extracted, expected, input_data=..., field_path=...)` (keyword arguments), so a function without parameters named `input_data`/`field_path` fails. Results are clamped to [0, 1]; any exception becomes `RuntimeError("Error executing Python code evaluator function: ...")`; a missing function → `ValueError("'function' must be provided for PythonCodeEvaluator")`; a non-callable → `ValueError("'function' must be a callable")`. `evaluators/python_code.py:43-75` [api] (verified: V/v_docs.py 4, 4').
- **PredefinedScoreEvaluator** — returns the next item of `scores`, keeping a separate position per thread (`threading.local`); an exhausted list gives 0.0 (`evaluators/predefined_score.py:47-75`). Normalization: bool → 1/0; None → 0.0; values in [0, 1] as-is; others ÷ `max_value` (default 100), clamped (77-107). So `1` on a 0–100 scale reads as 1.0. Used through `evaluator_config` it is **rebuilt per example and consumed per leaf field**: scores `[0.1, 0.9, 0.5]` on a 2-field model gave `[0.5, 0.5, 0.5]` for 3 examples. Each thread restarts at index 0 [trap] (verified: V/v_eval.py H, H').
- **Custom callables are ignored for labelled examples** — `_resolve_evaluate_fn` wraps any callable in the default extraction evaluator (`optimizer.py:613-614`). The callable is used only as a *judge* for examples with `expected_output=None`. The documented 4-arg `evaluate(example, descriptions, system_prompt, instruction_prompt)` (`optimizer.py:87-105`) is therefore **never called** when labels exist. This regressed in 1f24e8d; before it, d49832e passed the callable through [trap] (verified: V/v_eval.py A: the function returns 0.9, the metric returned 1.0, 0 calls) → here: every metric wrapper (spy that the metric ran).
- **Custom judge arity dispatch** — with `expected_output is None`: a judge with ≥5 parameters gets `(example, extracted_data, descriptions, sys, instr)`, otherwise 4 args. `except (ValueError, TypeError): pass` also swallows errors raised **inside** the 5-arg call and silently retries with 4 args (`functions.py:374-393`) [trap].
- **`evaluate_fn` accepted forms** — `None`, `"exact"`, `"levenshtein"` (any other string → `ValueError('evaluate_fn must be a callable, dspy.LM, None, or one of ("exact", "levenshtein"), got "..."')`), a `dspy.LM` (whose judge role is ignored, see above), a callable, or `TypeError("Unexpected type for evaluate_fn: ...")`. An evaluator *object* such as `PredefinedScoreEvaluator(...)` hits the TypeError at `optimize()`, although a guide shows exactly that (`docs/guides/evaluators/configure.md:53-56`). `optimizer.py:577-615` [trap] (verified: V/v_eval.py I).
- **Demos passed by signature probing** — `optimized_demos=` is passed only if `inspect.signature(evaluate_fn).parameters` contains `optimized_demos` (`optimizer.py:950-957`) [pattern].
- **The search objective differs from the acceptance test** — after 1afc528, baseline and final scoring include few-shot demos, but the metric DSPy optimizes during `compile` (from `_create_metric_function`, `optimizer.py:676-681`) calls without demos, in single-pass mode and in the prompt phases (`_optimize_prompt`, 1188-1191). Single-pass extraction calls were `['demos','NO-demos','demos']`; in sequential mode the 4 system-prompt compile calls had no demos [trap] (verified: I3) → here: baseline.py (score exactly the configuration you ship).
- **The documented leakage and unfair-baseline bugs (1afc528)**, quoting the commit: „(1) `_optimize_single_field` always leaked validation data: val_single was always identical to train_single due to off-by-one in guard condition after slicing (split_idx < len(train_single) was always False); (2) Empty validation set silently fell back to training data …, now emits warnings.warn(); (3) `_optimize_prompt` metric evaluated candidates with original field descriptions instead of Phase 1 optimized ones; (4) Baseline evaluated WITHOUT few-shot demos while all subsequent evaluations included up to 8 demos — the 89% to 100% jump was from demos alone, not description optimization". Old line: `val_single = val_single[split_idx:] if split_idx < len(train_single) else train_single`, with `train_single` already sliced to `split_idx`. `git show 1afc528` [trap] (the 89→100% figure is [claim]: from the commit message, not reproducible here) → here: trainset.py, baseline.py.
- **Meta-instruction guard** — `META_INSTRUCTION_PATTERNS = [r"Given the fields", r"produce the fields", r"Using the fields.*optimize", r"your task is to produce", r"you are provided with", r"generate a clear and concise version"]` plus non-empty and `len < 500` (`tests/integration/test_miprov2_descriptions.py:19-26,288-300`). Because dspydantic reverts to the **original** descriptions on no improvement, the assertion passes whether or not the fix works [pattern] [trap].
- **`predict_with_confidence` is a heuristic** — `0.6*field_coverage + 0.4*word_overlap`, where coverage = share of non-empty fields and overlap = share of input words that appear in extracted string values; no text or no fields → 0.5 (`prompter.py:586-621`). There is **no second LM call**, contrary to the docstring (`prompter.py:556-557`); long inputs push the overlap term towards 0 [trap] (verified: V/v_schema.py #10: 1 LM call, confidence 0.6).

## DATA

- **Train/val split** — positional, no shuffle or stratification. `split_idx = max(1, int(len(trainset)*train_split))` with `train_split=0.8`. An empty val set emits `UserWarning("Not enough examples to create a separate validation set (... ) Using training set for validation — scores may be inflated.")` and sets `val = train`. `optimizer.py:1738-1751`. Sizes (train/val): n=1 → 1/1 (same example); 2 → 1/1; 3 → 2/1; 4 → 3/1; 5 → 4/1; 6 → 4/2; 10 → 8/2; 12 → 9/3; 20 → 16/4; 26 → 20/6; 57 → 45/12 [number] (verified: V/v_run.py `metrics` showed n=1 → 1/1, n=2 → 1/1, n=5 → 4/1, n=20 → 16/4; the rest by the formula) → here: pairs.py (stratified folds, repeats).
- **Extraction few-shot demos are not optimized** — they are simply the first `min(8, split_idx)` examples (`optimizer.py:1753-1763`), placed in every extraction prompt during optimization and at inference (`functions.py:281-289`, `prompter.py:456-464`). Image inputs appear in demos as the text "1 image" / "N image(s)" (`utils.py:83-93`). The name `optimized_demos` is misleading [trap].
- **String outputs** — a string `expected_output` becomes `{"output": s}`. With `model=None` a model `OutputModel(output: str = Field(description="The output value"))` is auto-created. `types.py:234-253`, `optimizer.py:310-326,865-871`, `functions.py:407-411`. `model=None` with dict outputs → `ValueError("model cannot be None unless examples have string expected_output values")` [api].
- **Model-instance outputs** — `expected_output` given as a Pydantic instance is `model_dump()`ed (`optimizer.py:867-868`, `functions.py:407-408`) [api].
- **`text=dict` round trip loses the dict** — the example's instruction-prompt *input* is the template formatted with that example's values (`optimizer.py:888-900`). Converting back to `Example` loses `text_dict` (`optimizer.py:806-810` → `Example(text=str)`), so the extraction prompt used for scoring contains the **literal placeholder** (`"{review}"`). The template's placeholder-preserving branch is therefore never the thing scored [trap] (verified: V/v_schema.py #6).
- **Lossy `_dspy_example_to_example`** — if `images_base64` is present it returns `Example(image_base64=images_base64[0])`: **the text is dropped and only the first image kept** (`optimizer.py:762-766`). Other fallbacks yield `Example(text="")` (776-816) [trap] (verified: V/v_schema.py #7 with a patched image converter; input keys after the round trip: `['images']`).
- **Reserved field names** — the example dict is `{"input_data": ..., "expected_output": ...}` then `.update(descriptions)` (`optimizer.py:873-878`). A model field named `input_data` (or `expected_output`, `system_prompt`, `instruction_prompt`, `field_type_*`) overwrites the data. A field `input_data` made every scoring call extract from `{'text': ''}` [trap] (verified: I2).
- **`None` labels** — examples with `expected_output=None` go down the judge path, per example; labelled and unlabelled examples can be mixed [api].
- **Example-count guidance is unmeasured** — "5-10 Good / 10-20 Better / 20+ Best" (`docs/core-concepts.md:64-70`, `docs/guides/optimization/first-optimization.md:127-131`, `docs/tutorials/extract-structured-data.md:121-125`); README: "5-20 examples typically enough" (`README.md:83`) [claim].

## PROD

- **The cache flag does not control the cache location** — `Prompter(cache=False)` is the default → `dspy.LM(..., cache=False)`. `cache=True` or a path string → `dspy.LM(..., cache=True)` plus `os.makedirs(".dspydantic_cache" or path)`, but the **path is never given to DSPy**, which keeps its own cache directory (`prompter.py:57-79,171-177`). The flag matters only when Prompter creates the LM. A user-configured `dspy.LM` defaults to `cache=True`, and judges/evaluators always use whatever the global LM has [trap] → here: lmrun.py (`cache=False` on the LM object).
- **`model_id` silently ignored** — if any LM is already configured, `Prompter(model_id=...)` returns without touching DSPy (`prompter.py:72-73`; `tests/unit/test_prompter.py:432-442`) [trap] (verified: V/v_schema.py #9: `settings.lm.model` stayed `fixture/p`).
- **One global LM** — extraction, judges and graders all use `dspy.settings.lm`; there is no per-component LM routing (`functions.py:330-333,120-122`; `evaluators/score_judge.py:100-103`) [api].
- **`api_calls` / `total_tokens`** — computed as `len(lm.history)` and the sum of `usage["total_tokens"]` over history entries (`optimizer.py:1521-1529,2007-2018`). This counts calls made **before** `optimize()` and **cache hits**, is capped at 10,000, and **misses calls made through `lm.copy()`**: MIPROv2's `GroundedProposer` uses `self.prompt_model.copy(rollout_id=...)` (`dspy/propose/grounded_proposer.py:395`). `estimated_cost_usd` is always None (1550, 2010) [trap] (verified: V/v_run.py miprov2zeroshot 290 requests vs `api_calls=200`; miprov2 395 vs 350; I6 53 vs 35) → here: lmrun.py (one record per call at the call site).
- **Persisted files** — `dspydantic_metadata.json` `{version, model_id, model_config, metadata}`, `optimized_state.json` `{optimized_descriptions, optimized_system_prompt, optimized_instruction_prompt, optimized_demos}`, `model_schema.json` (`persistence.py:69-93`). `save()` writes `model_id=""` and `model_config={}` (`prompter.py:804-805`) and requires non-empty `optimized_descriptions` ("Prompter must be optimized before saving. Call optimize() first.", 792-793). **It persists up to 8 training examples' `input_data` and `expected_output`**, base64 images included (`optimizer.py:1756-1763`, `persistence.py:85`) [trap] (verified: V/v_docs.py #11, 4 demos saved for n=5).
- **Version stamp** — `version("dspydantic")` via importlib.metadata, falling back to **"0.1.2"** when the package is not installed (`prompter.py:18-23`, `persistence.py:35-40`), while `__version__ = "0.1.6"`. On load: a major mismatch → `PersistenceError("Incompatible version: ...")`; a minor mismatch → `UserWarning`; unparsable → no check (`persistence.py:128-162`) [trap] (verified: V/v_docs.py #11 saved `"version": "0.1.2"` from a source checkout).
- **Load never checks the schema** — `load()` stores `state.model_schema` in `_saved_schema` and never compares it with the model passed in (`prompter.py:220-221`); stale descriptions for renamed fields are ignored silently [trap].
- **Train/serve prompt skew** — the scoring prompt has the header "JSON Schema (with optimized field descriptions):", a "Field descriptions summary:" block, the closing line "(which includes optimized field descriptions)", and truncated image URL lines (`functions.py:262-323`). The inference prompt has "JSON Schema:" with no summary or image lines (`prompter.py:448-482`). The descriptions are thus selected under one prompt and shipped under another [trap] → here: any optimizer (ship what you scored).
- **Dict input at inference** — `predict(text=dict)` builds `input_data = {}`, so the input reaches the LM only through a template instruction prompt. Without one, the text is dropped (`prompter.py:408-429,466-475`) [trap] (verified: V/v_schema.py #5: input absent from the prompt; ValidationError "Field required").
- **"System prompt" is prompt text** — it is inserted as the text `"System: ..."` inside the `prompt` input field, not as a chat system message (`functions.py:263-266`, `prompter.py:449-452`) [api] (verified: I4).
- **Returned instances fail type checks** — `predict` returns an instance of a class rebuilt by `create_model` with the same name; `isinstance(result, UserModel)` is False, and a FastAPI/Pydantic field typed `UserModel` rejects it: `Input should be a valid dictionary or instance of Invoice [type=model_type]` [trap] (verified: V/v_schema.py #5, V/v_docs.py #7).
- **Batch and async** — `predict_batch` uses `ThreadPoolExecutor(max_workers)`; `on_error="return"` puts exceptions in the result list; `apredict` runs sync `predict` in the default executor; `apredict_batch` uses `asyncio.Semaphore(max_concurrency)` + `gather` without `return_exceptions` (`prompter.py:623-749`) [api].
- **Progress output** — with `verbose=True` and no callback, a rich-console progress printer is installed (`optimizer.py:353-369`). Callbacks are wrapped `try: ... except Exception: pass` so telemetry can never abort a run (1282-1294). They fire **only in sequential mode** [pattern] (verified: V/v_run.py single-pass printed `progress phases: []`).
- **Dependencies** — runtime: `pydantic>=2.0.0, dspy>=3.0.4, deepdiff>=8.0.0, pillow>=10.0.0, pdf2image>=1.16.0, rich>=13.0.0` (`pyproject.toml:22-29`). sentence-transformers and openai are imported lazily and undeclared (`evaluators/text_similarity.py:57,79`); optuna is needed for MIPROv2 on 3.3.1 [api].

## TEST

- **Suite status** — `pytest tests/unit` → **134 passed** with **0 litellm call attempts** under a refusing plugin. `pytest tests` (what `make test` runs, `Makefile:34-35`) → **1 failed, 160 passed, 15 skipped**. The failure is `test_backward_compatibility_with_pydantic_optimizer` asserting `OptimizedModel.__name__ != Transaction.__name__` (`tests/integration/test_unified_workflow.py:173`), contradicting `tests/unit/test_extractor.py:151` (`==`). No CI workflow runs tests; only a docs deploy workflow exists (`.github/workflows/docs.yml`) [trap] (verified: pytest runs).
- **Script-style test files count 0 tests** — `tests/unit/test_init.py`, `test_field_names.py`, `test_field_types.py`, `test_type_integration.py`, `test_literal_enum.py` have module-level asserts and no `test_` functions: they run at import and contribute 0 tests. Their `class TestModel(BaseModel)` triggers `PytestCollectionWarning: cannot collect test class 'TestModel' because it has a __init__ constructor` [trap] (verified: pytest warnings).
- **Tests that re-implement the code under test** — `tests/unit/test_optimizer_validation_split.py:40-43,64` recompute the fixed slicing inside the test; `test_single_example_warns` (91-119) emits the warning itself (`warnings.warn(` at 109) and asserts it was emitted. None calls `_optimize_single_field` or `optimize()`, so a regression would pass [trap] → here: selftests (P: prove a check can fail).
- **Mocked-predictor test of the meta-instruction fix** — `test_forward_produces_descriptions_not_meta_instructions` replaces every predictor with a MagicMock returning clean text (`tests/unit/test_module.py:86-130`); it tests the mock, not the fix [trap].
- **Asserts on clamped ranges cannot fail** — `assert 0.0 <= score <= 1.0` (`tests/unit/test_evaluators.py:373`) and `assert result.optimized_score >= 0` (all MIPROv2 integration tests) [trap].
- **Comment/assert mismatch** — the thread test's comment says "all unique (no duplicates from race conditions)", but the assert only checks the count (`tests/unit/test_predefined_score_evaluator.py:90-91`). Per-thread indices hand the same scores to every thread [trap].
- **The regression-catching test never runs offline** — `test_optimizer_metric_function_integration` asserts `score == 0.9` from a custom `evaluate_fn` (`tests/integration/test_optimizer_integration.py:114-160`). It would catch the ignored-callable regression, but it is skipped without `OPENAI_API_KEY` although it uses a `MagicMock` LM [trap].
- **The `lm` fixture uses a real key when set** — `dspy.LM("openai/gpt-4.1-mini", api_key=os.getenv("OPENAI_API_KEY", "test-key"))` (`tests/conftest.py:16-17`): with a key in the environment, unit tests configure a live LM [trap] → here: lm_fixture.py `offline()` (hide keys, refuse litellm).
- **Test side effect** — `test_prompter_with_cache_enabled` creates `.dspydantic_cache/` in the working directory, via the real `os.makedirs` under a mocked `dspy` (`tests/unit/test_prompter.py:535` → `prompter.py:78-79`) [trap] (verified: the directory appeared in the scratch copy).
- **Registry pollution** — `register_evaluator("test", TestEvaluator)` mutates the global `EVALUATOR_REGISTRY` for the rest of the session (`tests/unit/test_evaluators.py:763`) [trap].
- **The docs test only parses** — `tests/test_docs.py` runs `ast.parse` only. It covers 23 of 49 Markdown files, **none of the mkdocs nav pages** (tutorials, how-to, explanation, most of reference), and skips any block whose first character is `#` (29 of 140 blocks in covered files, `tests/test_docs.py:61`). It parametrizes over a `docs/use-cases` directory that does not exist (120, "got empty parameter set"). All 257 Python blocks parse, yet many call APIs that do not exist (see TRAP) [trap] (verified: I9, V/v_docs.py).
- **Offline mock pattern used by the suite** — `with patch("dspydantic.evaluators.functions.dspy.ChainOfThought") as m: m.return_value.return_value = MagicMock(json_output='{"name": "John Doe", "age": 30}')` (`tests/unit/test_evaluators.py:71-76`) [pattern]. It patches the class the code instantiates; it does not survive a refactor to `dspy.Predict`.
- **Recipe: offline fixture that answers any signature** — read the output-field names from ChatAdapter's system message (`Your output fields are:\n1. `name` (type)`) and answer each in `[[ ## name ## ]]` blocks. This ran full `optimize()` with BootstrapFewShot, COPRO, MIPROv2 (with optuna) and BFRS on DSPy 3.3.1 with no key (`V/fx.py`) [recipe] (verified: V/v_run.py) → here: lm_fixture.py `fill()` (same design, confirmed working for MIPROv2's proposer fields `program_description`, `module_description`, `proposed_instruction`, `summary`, `observations`).

## PAT

- **Optimize a rewriter, score downstream** — the DSPy program under optimization produces text artifacts (descriptions or prompts). The metric plugs the artifact into a separate task call and scores that task. The optimizer's demos and instructions belong to the rewriter; the shipped artifact is one rewriter output (`module.py:157-370`, `optimizer.py:617-691`) [pattern] → here: job 4 (a SKILL.md description rewriter scored by routing accuracy).
- **Coordinate ascent with a rolling baseline** — deepest-first, one field per compile, others held fixed; the result becomes the next baseline; stop after N non-improving fields (`optimizer.py:499-510,1373-1449`) [pattern].
- **Prefer shorter text on ties** — descriptions `optimizer.py:1128-1132`, prompts `1263-1266`, single-pass `1988-2005` [pattern] → here: job 4.
- **Revert when optimization loses** — return the originals if the final score is below baseline (`optimizer.py:1505-1519,1976-1987`) [pattern] → here: baseline.py floor.
- **Check the invariant after a model edit, revert on violation** — the rewrite input embeds `ORIGINAL_PROMPT_TEMPLATE:` / `PROMPT_TEMPLATE_REWRITE_INSTRUCTIONS:` markers. Afterwards the code strips the markers, de-duplicates repeated placeholders (keeping the first) and **reverts to the original template if any placeholder is missing**. `module.py:286-365`. Observed outcomes: both placeholders kept → accepted; `{category}` dropped → original restored; `{review}` duplicated → second removed, leaving "…and again" dangling; markers echoed → stripped → reverted [pattern] (verified: I5) → here: P26 (code enforces what the model may not break).
- **Dot-path include/exclude** — include set = exact matches plus `startswith(path + ".")`, then minus the exclude set (`optimizer.py:471-497`). An include list that matches nothing leaves an empty effective set, and single-pass then **optimizes all fields** (`effective_descriptions or self.field_descriptions`, 1716-1719) while the metric falls back to a whole-structure comparison (`functions.py:517-525,564-566`, by reading) [pattern] [trap] (verified: V/v_docs.py #8: effective set `set()`).
- **Probe signatures instead of guessing kwargs** — `inspect.signature(cls.__init__).parameters` for `num_threads` (`optimizer.py:940-945`) and for `optimized_demos` (950-957) [pattern] → here: check_dspy_surface.py.
- **Typed progress event and a callback that cannot fail** — `FieldOptimizationProgress` plus the `_emit` try/except (`types.py:41-71`, `optimizer.py:1282-1294`) [pattern] → here: lmrun.py records.
- **Plugin registry and factory** — `register_evaluator(name, cls)` plus `EvaluatorFactory.create(str | dict | type)` (`evaluators/config.py:65-157`) [pattern]. It mutates the caller's config and rebuilds per call (see MET).
- **JSON recovery cascade** — `json.loads` → first balanced-brace object → greedy regex (`prompter.py:514-544`); the evaluator variant handles only one nesting level before the greedy fallback (`functions.py:342-360`) [pattern].
- **Contextual signature** — domain name in the class name, the instruction docstring, and an extra `field_name` input (`module.py:50-95`). Only the docstring and the input reach the LM in 3.3.1 [pattern] (verified: V/v_proposer.py, I4) → here: job 4.

## SKILL

- **What MIPROv2's proposer actually sees (3.3.1)** — the source code of the module class (the whole generic `PydanticOptimizerModule` source, including marker-stripping logic), per-predictor instructions (the docstring), field names, and a dataset summary built from trainset examples, labels included. The runtime signature class name is absent. For 5 predictors and n=2 it made 30 each of `program_description`, `module_description` and `proposed_instruction` calls, plus 1 `summary` and 1 `observations` [number] (verified: V/v_run.py by-kind counts, V/v_proposer.py program_code excerpt) → here: job 4 (put the skill's domain in the instruction text and in the evaluation cases the summarizer reads).
- **The rewriter never sees data** — its inputs are only `field_name`, `field_description`, `field_type` (identical for every example), so its only data signal is MIPROv2's dataset summary or bootstrapped demos, which are near-duplicates here [pattern] (verified: I4) → here: job 4 (GEPA's textual feedback carries the per-case signal; MIPROv2 would not).
- **Rewrite-instruction wording** — "Improve a field description for {Model} structured data extraction. Output ONLY the improved description — a short descriptive phrase, not instructions." with output desc "The improved field description — a short descriptive phrase" (`module.py:67-71,90-92`). The commit claims it stops meta-instruction outputs such as "Given the fields `field_description`, produce `optimized_field_description`"; that effect is not measured here or in the repo beyond the regex guard [claim] → here: job 4.
- **Descriptions are cost, too** — the tie-break toward shorter text is justified in the docs as "Shorter descriptions save tokens at inference time across every future extraction call" (`docs/guides/advanced/configure-optimizations.md:532`) [claim].
- **dspydantic cannot drive GEPA** — its metric is `(example, prediction, trace=None) -> float`, and GEPA 3.3.1 rejects anything that cannot bind `(gold, pred, trace, pred_name, pred_trace)`. A description optimizer on GEPA needs its own 5-arg metric returning `dspy.Prediction(score=..., feedback=...)` [api] (verified: V/v_construct.py, V/v_run.py) → here: job 4, pairs.py.

## TRAP

- **Default path n≥20 crashes** — BFRS receives `num_candidates=4` → `TypeError` at construction, before any LM call (`optimizer.py:27,398-403,948`) [trap] (verified: V/v_construct.py).
- **Default path n≤2 fails late** — MIPROv2 without optuna fails after bootstrap and proposal calls have been paid for [trap] (verified: V/v_run.py).
- **All image/PDF inputs fail on 3.3.1** — `dspy.Image.from_url(data URI)` → `ValueError` (`utils.py:191`); this covers `_prepare_dspy_examples` (optimizer.py:853-863), the evaluator (`functions.py:247-248`) and `Prompter.predict` (`prompter.py:485-488`) [trap] (verified: V/v_schema.py #7).
- **PEP 604 unions crash model rebuilding** — `create_optimized_model` compares `new_args != args` (list vs tuple, always True) and rebuilds `origin[tuple(new_args)]`; for `types.UnionType` this is `TypeError: type 'types.UnionType' is not subscriptable` (`extractor.py:438-455`). Every `Prompter.predict/run` on a model with an `X | None` field crashes, including the docs' flagship `JobPosting` (`docs/tutorials/extract-structured-data.md:28-29`, `docs/guides/optimization/first-optimization.md:34-35`) [trap] (verified: V/v_schema.py #3/#5a, V/v_docs.py #2).
- **The rebuilt model is not the original** — it is a new class with the same name: `isinstance` fails, `@field_validator`s are lost (the base becomes `BaseModel`), and only top-level `minLength/maxLength/minimum/maximum/pattern/examples` are copied (`extractor.py:361-380,418-422`). `gt`/`lt` and constraints inside `Optional` are lost: `score: float = Field(gt=0)` accepted 0.0, and `age: Optional[int] = Field(ge=0)` accepted -5 while the original rejected it. Inherited fields keep their original descriptions because the code reads `__annotations__` [trap] (verified: V/v_schema.py #3, #4).
- **Schema-walk gaps** — `Optional[Model]` (`anyOf`) is not descended: `extract_field_descriptions` gave `{'name','address'}` while `extract_field_types` had `address.street`. With pydantic < 2.9 a *described* nested field is `{"allOf": [{"$ref": ...}], "description": ...}` and is not descended either (pydantic 2.5.3 vs 2.9.2 shapes). Two fields sharing one `$defs` model collide in `apply_optimized_descriptions`: last writer wins, so `home.street`/`work.street` → "WORK street" (`extractor.py:65-98,272-281`) [trap] (verified: V/v_schema.py #1/#2, I8).
- **List-of-model fields always score 1.0** — leaf paths like `items.name` walk dicts only, so both sides resolve to `None`, which scores 1.0. A completely wrong list scored **1.0**, and an empty list scored **1.0** (`functions.py:437-446,551-553`). A check that cannot fail [trap] (verified: V/v_eval.py E, E') → here: job 2 (score list items explicitly), P23.
- **Custom evaluate_fn ignored; judge LM ignored** — see MET. Neither ScoreJudge nor LabelModelGrader uses its `lm`/`temperature` config [trap] (verified: V/v_eval.py A–C).
- **A parse failure becomes a mid score** — the judge returns 0.5 on unparseable text, and `'{"score": 85}'` → 1.0; the extractor returns 0.0 on unparseable output; text_similarity falls back to exact match (0.0) on any error. None of these is reported as "could not score" [trap] (verified: V/v_eval.py F/G, I7) → here: lmrun.py statuses, P15/P23.
- **The reported score belongs to a different sample** — in single-pass mode the returned descriptions come from one program call and the score from other calls. With the cache off they differ (returned `rewrite v3/v4`, scored `rewrite v5/v6`). With DSPy's default cache on they coincide only because identical inputs hit the cache [trap] (verified: V/v_scored.py) → here: lmrun.py (cache off) + score the returned artifact.
- **Parallel sequential mode races and ignores its limits** — `current_descriptions` is passed as the live dict ("Snapshot at start" comment, `optimizer.py:987`) and mutated by the main thread as futures complete (1012-1014), so results depend on completion order. Each field is compared with the same global baseline, and all accepted changes are merged without a joint check. `skip_score_threshold` and `early_stopping_patience` are ignored (applied only in the non-parallel branch, 1373-1449): parallel mode optimized all 5 fields with 52 requests, where non-parallel stopped (11) or skipped everything (6). Thread pools nest: `ThreadPoolExecutor(num_threads)` × each optimizer's `num_threads` [trap] (verified: V/v_run.py).
- **`max_val_examples` is unfair and often a no-op** — the baseline uses all val examples (`optimizer.py:1296-1316`) while fields are scored on the first `max_val_examples` (1329-1334). It never caps the valset handed to `compile` (`val_single = all_single[split_idx:]`, 1052-1054) and does nothing in single-pass mode, yet README and guides show it without `sequential=True` (`README.md:161-165`, `docs/guides/advanced/configure-optimizations.md:53`). In the ablation's "12 examples" scenario val = 3, so a cap of 5 changes nothing (`ABLATION_RESULTS.md:160-162,201`) [trap].
- **Accept-if-better on 1–4 examples** — for n≤20 each accept/reject is decided on a val set of 1–4 examples, with no repeats and no significance test (see DATA split table) [trap] → here: pairs.py folds/repeats (P18), baseline.py floor.
- **`except TypeError` swallows too much** — the valset fallback drops `compile_kwargs` and would equally swallow a TypeError raised inside compile (`optimizer.py:1848-1855`) [trap] (verified: V/v_scored.py).
- **Documented kwargs crash with the auto optimizer** — `compile_kwargs={"num_trials": 5, "minibatch": False}` with auto-selected BootstrapFewShot → `BootstrapFewShot.compile() got an unexpected keyword argument 'num_trials'` (no try around that branch). `optimizer_kwargs={"auto": None, "num_candidates": 3}` → `BootstrapFewShot.__init__() ... 'auto'`. Both are recommended without an explicit optimizer (`docs/guides/advanced/configure-optimizations.md:579`, `docs/how-to/configure-optimizations.md:196-197,236`, `docs/guides/optimization/first-optimization.md:272`) [trap] (verified: V/v_docs.py #9, #10).
- **Prefix stripping with `str.replace`** — `field_path = key.replace("optimized_", "")` removes every occurrence: prediction keys `optimized_optimized_value` → `value` and `optimized_is_optimized_flag` → `is_flag`, so those optimized descriptions never reach the schema (`optimizer.py:659-662`) [trap] (verified: I2).
- **Templates: several failures** — system-prompt placeholders are never filled, anywhere: `format_instruction_prompt_template` is applied only to the instruction prompt (`functions.py:226-229`, `prompter.py:439-443`). Literal JSON braces in a template raise `ValueError: Format specifier missing precision` via `str.format_map` (`utils.py:314-318`). Keys not matching a placeholder are appended as `"Additional context: k: v"` with a UserWarning (`utils.py:299-330`) [trap] (verified: V/v_schema.py #6, #8).
- **Docs call APIs that do not exist** (all verified in V/v_docs.py):
  - `Prompter.optimize(examples, system_prompt=..., instruction_prompt=...)` → `PydanticOptimizer() got multiple values for keyword argument 'system_prompt'` (`docs/guides/optimization/prompt-templates.md:106-110`, `docs/tutorials/use-prompt-templates.md:125-129`, `docs/reference/input-formats.md:123-127`).
  - `Example(..., predefined_score=0.95)` → TypeError (`docs/explanation/understanding-evaluators.md:138`).
  - `{"type": "python_code", "function": f}` without `"config"` → ValueError (`docs/how-to/configure-evaluators.md:107`, `docs/explanation/choosing-an-evaluator.md:102`).
  - `{"config": {"code": "def evaluate..."}}` → ValueError (`docs/guides/evaluators/selection.md:107`).
  - A lambda `(ext, exp, _, __)` → RuntimeError, because keyword arguments are passed (`choosing-an-evaluator.md:102`).
  - `"model_name"` for text_similarity, where the key is `model`: silently ignored (`docs/how-to/configure-evaluators.md:61`).
  - `PydanticOptimizer(model_id=...)` in every dataset example → TypeError (`examples/evaluator_config_example.py:40,83,160,215`, `examples/image_example.py:140`, `examples/imdb_example.py:119`, `examples/text_example.py:216`).
  - `Prompter(model=None).run(text) # Returns result.output (str)` → "model is required for extraction" (`docs/explanation/key-concepts.md:139`).
  - `# Returns MyModel instance` → it returns a same-named rebuilt class (key-concepts.md:133).
  
  [trap] → here: check_skills.py / doc checks (execute snippets against a fixture; `ast.parse` catches none of this).
- **Docs contradict the code** (claims, each verified false):
  - "Default behavior is smart: enums use exact match, strings use fuzzy match." (`docs/core-concepts.md:107`); the default is `exact` for everything (`functions.py:427-434`).
  - "Uses a second LLM call to assess extraction confidence" (`prompter.py:556-557`).
  - LabelModelGrader "LLM evaluates" (`understanding-evaluators.md:109`).
  - "The optimized score … This is what you'll get in production." (`docs/explanation/how-optimization-works.md:169`).
  - "What gets saved: … Model configuration"; "NOT saved: Examples" (`docs/guides/advanced/save-load.md:29,34`; `docs/how-to/save-and-load.md:21,25`).
  - "Callbacks are automatically invoked when `verbose=True`" (`docs/reference/api/types.md:91`); sequential mode only.
  - "PDFs work best with text-based content"; "Built-in OCR" (`docs/how-to/use-multimodal-inputs.md:95-96`, `docs/reference/input-formats.md:164`); PDFs are rasterized.
  - A data URI given as `image_base64` (`input-formats.md:11`) would be prefixed a second time (`utils.py:188`).
  - `FROM python:3.10-slim` (`docs/how-to/deploy-to-production.md:44`) against `requires-python >=3.11`.
  
  [trap].
- **Unmeasured headline numbers** — "Typical improvement: 10-30% higher accuracy" (`README.md:46`, `docs/explanation/how-optimization-works.md:134`); "# Accuracy: 68% → 94%" and "Here's a real optimization result" (`docs/index.md:45,52`); "Typical output: Before: 72% After: 91% API calls: 47 Tokens: 28,450" (`docs/guides/optimization/first-optimization.md:169-174`). No run, seed, n or log is attached [claim].
- **ABLATION_RESULTS.md shows no measurement** — times, call counts and "+5-15% / +15-30%" gains carry no n, seed, date or log. Its sources:
  - `examples/ablation_benchmark_mock.py` never runs `optimize()` ("We're not actually running optimize()", line 169). It hardcodes `baseline_score = 0.75` (177), a `quality_factor = 1.2` for sequential (181), compile counts `1/12/12/8` (224-227), and a max-val "0.7× compiles" (183, although capping val does not reduce compiles), with caps `min(optimized_score, 0.95)` and `min(improvement, 0.2)` (195-196). **On DSPy 3.3.1 every config errors with `'Settings' object has no attribute 'lm'`** from `patch('dspy.settings.lm', ...)` (135).
  - `examples/benchmark_instrumented.py` claims to measure "actual DSPy compile counts" (line 1) but hardcodes them (130-134), with `× 25 s` (145) and `× 50 calls` (153); its own output reads "Parallel fields give 1.0× speedup on sequential — 125s down to 125s", against the doc's "~4-6× faster" (`ABLATION_RESULTS.md:117`).
  - `examples/benchmark_analysis.py` hardcodes `single_pass_calls = 50` (39) and `seq_parallel_time = 75` (95).
  - The only live config of `examples/ablation_benchmark.py` is labelled "Sequential + Parallel" but passes `{"sequential": False, ...}`, i.e. single-pass (163); the others are commented out (161-164).
  - The doc's claims "Parallel fields snapshot `current_descriptions` at start; no shared state" and "Progress callbacks: Works with all modes; `phase="skipped"`…" (`ABLATION_RESULTS.md:290,293`) are false (see above).
  
  [trap] (verified: ran both mock scripts offline).
- **LICENSE vs pyproject** — Apache-2.0 vs MIT (see Header). `Makefile:95` `watch: watch-test` names a target that is not defined [trap].
- **AvatarOptimizer is broken in DSPy 3.3.1 itself** — `dspy.TypedPredictor(Comparator)` (`dspy/teleprompt/avatar_optimizer.py:90`) → AttributeError at construction [trap] (verified: V/v_construct.py) → here: check_dspy_surface.py.
- **The test that would have caught the regression is gated** — see TEST [trap].

---

## Code worth keeping

**1. Auto-selection by example count** — `src/dspydantic/optimizer.py:512-533`. It runs on 3.3.1 (V/v_construct.py). The ≥20 branch is usable only once `_FAST_MODE_KWARGS["bootstrapfewshotwithrandomsearch"]` uses `num_candidate_programs`, and the n≤2 branch needs `dspy[optuna]`.
```python
    def _auto_select_optimizer(self) -> str:
        """Auto-select the best optimizer based on the number of examples.

        Selection logic:
        - Very small datasets (1-2 examples): Use MIPROv2ZeroShot (avoids BootstrapFewShot bug)
        - Small datasets (3-19 examples): Use BootstrapFewShot
        - Larger datasets (>= 20 examples): Use BootstrapFewShotWithRandomSearch

        Returns:
            String name of the recommended optimizer type.
        """
        num_examples = len(self.examples)

        if num_examples <= 2:
            # Very small dataset - use MIPROv2ZeroShot to avoid BootstrapFewShot bug
            return "miprov2zeroshot"
        elif num_examples < 20:
            # Small dataset - use BootstrapFewShot
            return "bootstrapfewshot"
        else:
            # Larger dataset - use BootstrapFewShotWithRandomSearch
            return "bootstrapfewshotwithrandomsearch"
```

**2. Runtime teleprompter discovery** — `optimizer.py:438-469`. It runs on 3.3.1 and returns 15 names plus the alias (V/v_construct.py). It only validates the name; pair it with an `inspect.signature` check of the constructor and `compile` (6 of 16 names fail with dspydantic's generic kwargs).
```python
    @staticmethod
    def _get_teleprompter_subclasses() -> dict[str, type[Teleprompter]]:
        def get_all_subclasses(cls: type) -> set[type]:
            """Recursively get all subclasses of a class."""
            subclasses = set()
            for subclass in cls.__subclasses__():
                subclasses.add(subclass)
                subclasses.update(get_all_subclasses(subclass))
            return subclasses

        subclasses = get_all_subclasses(Teleprompter)
        mapping: dict[str, type[Teleprompter]] = {}
        for subclass in subclasses:
            if subclass.__name__ == "Teleprompter":
                continue
            mapping[subclass.__name__.lower()] = subclass
        if "miprov2" in mapping:
            mapping["miprov2zeroshot"] = mapping["miprov2"]
        return mapping
```
(Verbatim except the docstring and comment lines, which are removed.)

**3. Contextual signature built at runtime** — `src/dspydantic/module.py:67-95`. It runs on 3.3.1 and was compiled by BootstrapFewShot, COPRO and MIPROv2 (V/v_run.py). The docstring and the `field_name` input reach the LM; **the class name does not** (V/v_proposer.py).
```python
    docstring = (
        f"Improve a field description for {model_name} structured data extraction. "
        f"Output ONLY the improved description — a short descriptive phrase, "
        f"not instructions."
    )

    # Dynamic class name gives the proposer domain signal for free
    cls = type(
        f"Optimize{model_name}FieldDescription",
        (dspy.Signature,),
        {
            "__doc__": docstring,
            "__annotations__": {
                "field_name": str,
                "field_description": str,
                "field_type": str,
                "optimized_field_description": str,
            },
            "field_name": dspy.InputField(desc="Name of the field being optimized"),
            "field_description": dspy.InputField(
                desc="The current field description to improve"
            ),
            "field_type": dspy.InputField(desc="The data type of the field"),
            "optimized_field_description": dspy.OutputField(
                desc="The improved field description — a short descriptive phrase"
            ),
        },
    )
    return cls
```

**4. Invariant check after a model edit, reverting on violation** — `src/dspydantic/module.py:342-365`. Pure Python, independent of the DSPy version (exercised with a stub predictor in I5). Note that the `break` on the first missing placeholder skips de-duplication of later ones, and that de-duplication can leave dangling words.
```python
                # Verify all placeholders are present exactly once
                for placeholder_name in unique_placeholders:
                    placeholder_str = f"{{{placeholder_name}}}"
                    count = optimized_prompt.count(placeholder_str)

                    if count == 0:
                        break
                    elif count > 1:
                        # Duplicate - keep only the first occurrence
                        first_idx = optimized_prompt.find(placeholder_str)
                        if first_idx != -1:
                            before_first = optimized_prompt[: first_idx + len(placeholder_str)]
                            after_first = optimized_prompt[first_idx + len(placeholder_str) :]
                            after_first = after_first.replace(placeholder_str, "")
                            optimized_prompt = before_first + after_first

                # Final check: if any placeholders are still missing, use original prompt
                all_placeholders_present = all(
                    f"{{{p}}}" in optimized_prompt for p in unique_placeholders
                )
                if not all_placeholders_present:
                    optimized_prompt = instruction_prompt

                optimized["optimized_instruction_prompt"] = optimized_prompt.strip()
```

**5. Acceptance rule with a shorter-on-tie tie-break** — `optimizer.py:1124-1133`. Pure Python. Show it together with its weakness: `scores` comes from 1–4 validation examples for n≤20, with no repeats.
```python
        new_score = sum(scores) / len(scores) if scores else 0.0

        if new_score > baseline_score:
            return (new_description, new_score)
        if new_score == baseline_score:
            # Prefer the shorter (simpler) description on ties
            original = current_descriptions[field_path]
            if len(new_description) <= len(original):
                return (new_description, new_score)
        return (current_descriptions[field_path], baseline_score)
```

**6. Split that warns instead of silently reusing training data** — `optimizer.py:1738-1751`. It runs on 3.3.1; the warning appears for n=1 (V/v_run.py). It is positional with no shuffle.
```python
        split_idx = max(1, int(len(trainset) * self.train_split))
        train_examples = trainset[:split_idx]
        val_examples = trainset[split_idx:]
        if not val_examples:
            warnings.warn(
                f"Not enough examples to create a separate validation set "
                f"({len(trainset)} examples with train_split={self.train_split}). "
                f"Using training set for validation — scores may be inflated.",
                UserWarning,
                stacklevel=2,
            )
            val_examples = trainset
```

**7. Leaf-field scoring with explicit None handling** — `src/dspydantic/evaluators/functions.py:545-563`. Pure Python; show it together with the list-of-model defect (both sides `None` → 1.0 for `items.name`).
```python
        if leaf_field_paths:
            field_scores = []
            for field_path in leaf_field_paths:
                extracted_value = get_nested_value(extracted_data, field_path)
                expected_value = get_nested_value(expected, field_path)

                # If both values are None, consider it a match (field not present)
                if extracted_value is None and expected_value is None:
                    field_scores.append(1.0)
                # If one is None and the other isn't, it's a mismatch
                elif extracted_value is None or expected_value is None:
                    field_scores.append(0.0)
                else:
                    # Compare the values for this field
                    field_score = compare_values(extracted_value, expected_value, field_path)
                    field_scores.append(field_score)

            # Average all field scores
            score = sum(field_scores) / len(field_scores) if field_scores else 0.0
```

**8. A callback that can never abort the run, and signature probing** — `optimizer.py:1282-1294` and `950-957`. Pure Python.
```python
        def _emit(phase, score_before, score_after, field_path=None, field_index=None, optimized_value=None):
            if self.on_progress is None:
                return
            try:
                self.on_progress(FieldOptimizationProgress(
                    phase=phase, score_before=score_before, score_after=score_after,
                    improved=score_after > score_before, total_fields=total_fields,
                    field_path=field_path, field_index=field_index,
                    elapsed_seconds=time.perf_counter() - _t0,
                    optimized_value=optimized_value,
                ))
            except Exception:
                pass  # never abort optimization due to callback error

    @staticmethod
    def _evaluate_fn_accepts_optimized_demos(fn: Callable[..., float]) -> bool:
        """Check if evaluate_fn accepts optimized_demos keyword argument."""
        try:
            sig = inspect.signature(fn)
            return "optimized_demos" in sig.parameters
        except (ValueError, TypeError):
            return False
```
(These are two separate verbatim fragments.)

**9. A MIPROv2 budget that is legal on 3.3.1** — `tests/integration/test_miprov2_descriptions.py:305-309`. It ran end to end offline with optuna installed (I6: 53 requests). Use it only with an explicit `optimizer="miprov2..."`.
```python
# --- Shared kwargs to limit MiPROV2 trials for faster test runs ---
# auto=None disables auto-mode so we can set num_candidates explicitly.
# num_trials is a compile() arg, passed via compile_kwargs.
FAST_MIPRO_OPTIMIZER_KWARGS = {"auto": None, "num_candidates": 3}
FAST_MIPRO_COMPILE_KWARGS = {"num_trials": 3, "minibatch": False}
```

**10. Anti-pattern: a parse failure turned into a score** — `evaluators/score_judge.py:105-131`. It runs; show it as what **not** to do. 0.5 means "could not parse", and a stray "1" in prose means 1.0 (V/v_eval.py F).
```python
        # Extract evaluation from result
        evaluation_text = str(result.evaluation) if hasattr(result, "evaluation") else str(result)

        # Try to parse JSON from evaluation
        try:
            evaluation = json.loads(evaluation_text)
            score = float(evaluation.get("score", 0.5))
        except (json.JSONDecodeError, ValueError, AttributeError):
            # Try to extract score from text using regex
            score_match = re.search(r'"score"\s*:\s*([0-9.]+)', evaluation_text)
            if score_match:
                try:
                    score = float(score_match.group(1))
                except ValueError:
                    score = 0.5
            else:
                # Fallback: try to find a number between 0 and 1
                score_match = re.search(r"\b(0\.\d+|1\.0|1)\b", evaluation_text)
                if score_match:
                    try:
                        score = float(score_match.group(1))
                    except ValueError:
                        score = 0.5
                else:
                    score = 0.5

        return max(0.0, min(1.0, score))
```

**11. Anti-pattern: a list vs tuple comparison that is always True** — `src/dspydantic/extractor.py:438-455`. It crashes on 3.3.1 and on any Python ≥3.10 for `X | None` (V/v_schema.py #3). Show it as a trap. The fix: compare `tuple(new_args) != args`, or rebuild through `typing.Union[...]`.
```python
        elif origin is not None:
            # Handle generic types like List, Optional, etc.
            args = get_args(field_type)
            if args:
                # Check if any args are BaseModel subclasses
                new_args = []
                for arg in args:
                    if isinstance(arg, type) and issubclass(arg, BaseModel):
                        optimized_nested = create_optimized_nested_model(
                            arg, field_path, nested_model_cache
                        )
                        new_args.append(optimized_nested)
                    else:
                        new_args.append(arg)

                # Reconstruct the type with optimized nested models
                if new_args != args:
                    field_type = origin[tuple(new_args)]
```

---

## The old report, corrected

Corrections to `/home/user/kohaerenzprotokoll/Plan/concept/dspy-repos_2026-09-23/dspydantic.md`, cited by its section and item numbers:

1. **§1 and §5, "134 tests, offline, … all pass"** — true for `tests/unit` only.
   - `pytest tests` (the Makefile's `make test`) gives 1 failed, 160 passed, 15 skipped (`tests/integration/test_unified_workflow.py:173`).
   - Five unit "test" files are import-time scripts that count 0 tests.
   - The unit run writes `.dspydantic_cache/` into the working directory.
   - The report also missed that the `lm` fixture would configure a live LM whenever `OPENAI_API_KEY` is set.
2. **§1, "verified … to actually run against DSPy 3.3.1"** — only at the import and unit level. End to end on 3.3.1:
   - the default for n≥20 crashes;
   - the default for n≤2 needs optuna;
   - every image/PDF path raises (`Image.from_url`);
   - `optimizer="gepa"`, `labeledfewshot`, `knnfewshot` and `ensemble` cannot be constructed;
   - `X | None` fields crash `predict`.
3. **Item 3 ("[adopt] … the reason (avoid a bootstrap bug at n≤2) worth stealing verbatim")** — the "bug" is never described, and BootstrapFewShot compiled at n=1 on 3.3.1. The ≥20 branch is broken by default through `_FAST_MODE_KWARGS` (`num_candidates` is not a BFRS parameter). The thresholds are unmeasured. With the old report's n=26 (20 train / 6 val), or the target's current 57 labelled pairs (45/12), dspydantic would pick BFRS and crash unless `sequential=True`.
4. **Item 4 ("fast-mode kwargs table … a dict any wrapper should keep")** — one of its four entries is invalid for DSPy (`num_candidates` on BFRS). A kwargs table must be checked against `inspect.signature`.
5. **Item 5 ("any optimizer DSPy ships (including GEPA, SIMBA, COPRO, KNNFewShot...) is selectable by string")** — only the *name* validates.
   - GEPA (3-arg metric), KNNFewShot, LabeledFewShot, Ensemble and FinetuneTeleprompter fail at construction; AvatarOptimizer fails inside DSPy.
   - SIMBA fails at compile below 32 train examples.
   - COPRO works only through the `except TypeError` fallback, which drops `compile_kwargs`.
6. **Item 6 (rolling baseline, "only accepts an improvement")** — correct for non-parallel sequential mode, but:
   - under the default `parallel_fields=True`, every field is compared with the same global baseline and all changes are merged without a joint check;
   - with `max_val_examples`, the baseline is computed on the full val set and fields on the capped one;
   - the decisions rest on 1–4 validation examples for n≤20.
7. **Item 7 ("each field's optimizer sees an immutable snapshot … threads never race")** — false. The live dict is passed (`optimizer.py:987`) and mutated as futures complete (1012-1014).
8. **Item 8 (on_progress)** — events fire only in sequential mode; `phase="skipped"` is never emitted under `parallel_fields=True`.
9. **Items 9–10 (factory, default_lm auto-injected, per-field overrides)** — the LM is injected only for dict configs, **mutates the caller's config**, and is ignored by ScoreJudge and LabelModelGrader anyway. Evaluators are rebuilt per example. Overrides apply only to primitive values; dict and list values use DeepDiff typed by the *default* evaluator.
10. **Items 11 and 13 (leaf-only scoring, None/None = 1.0)** — the same rule makes **every list-of-model field score 1.0 regardless of content**; the report recommended adopting the rule without this caveat. `Optional[Model]` is not walked, and with pydantic < 2.9 described nested models (`allOf`) are not walked either.
11. **Item 14 (PredefinedScoreEvaluator "FIFO", "thread-safe", good for replaying judgements.jsonl)** —
    - through `evaluator_config` it is rebuilt per example and consumed per leaf field, so it cannot replay one decision per example;
    - per-thread cursors hand every thread the same scores;
    - `1` on a 0–100 scale reads as 1.0;
    - passed as `evaluate_fn` it raises TypeError at `optimize()`.
12. **Item 16 (judge 0.5 fallback)** — right, but incomplete: `'{"score": 85}'` → 1.0, any bare "1" in prose → 1.0, and the judge `lm` argument (`evaluate_fn=judge_lm`) is never used.
13. **Item 17 (LabelModelGrader, "LLM only when needed")** — in the common case (expected label in the allowed set) the LLM is **never** called, so the documented semantic match ("good" vs "positive" → 0.5) returns 0.0. An empty LLM label scores 0.5. The grader requires a configured LM even when it will not call one.
14. **Item 18 (TextSimilarity falls back to exact match on failure)** — worse than "on failure": with sentence-transformers the fallback is **always** taken (`.tolist()` on a list), so the evaluator is exact match in disguise.
15. **Item 20 ("score clamping at every metric boundary")** — the metric returns **0.0**, not a clamp, for out-of-range scores (`optimizer.py:683-687,725-726`). Class-based and `evaluator_config` evaluators are not clamped per field.
16. **Item 22 (contextual signatures; "the class/field name is free context")** — the **class name reaches no prompt** in DSPy 3.3.1 (V/v_proposer.py, I4). Only the docstring and the `field_name` input field reach the LM. The proposer's program-aware context is the generic module source code.
17. **Item 23 (placeholder preservation)** — the mechanism is correct (I5), but during optimization the scored candidates are pre-formatted prompts (placeholders filled per example), the evaluation path loses `text_dict` (literal `{review}` in scoring prompts), and system-prompt placeholders are never filled at all.
18. **Items 25–26 (skip_score_threshold, early_stopping_patience)** — both are **ignored in the default sequential configuration** (`parallel_fields=True`) and in single-pass mode.
19. **Item 27 (cost tiers)** — offline counts contradict them: MIPROv2 light made 290–395 LM requests on a 5-field model at n=2–5, against the documented "~50" and "~17".
20. **Item 30 (save/load stores only optimized artifacts)** — `save()` also persists up to 8 **training examples** (`optimized_demos`, including base64 images), and a from-source version stamp of "0.1.2".
21. **Item 31 ("cache=True or a path string turns on a dspy.LM(..., cache=...) disk cache and creates the directory")** — the directory is created but never passed to DSPy. The flag applies only when Prompter creates the LM, and a user-configured `dspy.LM` caches by default.
22. **§3 Job 4 ("`optimizer="gepa"` is already selectable … run `PydanticOptimizer(optimizer="gepa")` directly")** — false. It raises `TypeError: GEPA metric must accept five arguments` at construction, and GEPA also needs a budget and a `reflection_lm`. dspydantic cannot optimize SKILL.md descriptions with GEPA.
23. **§3, "only `api_calls` is ever actually populated (via `len(lm.history)` in the example benchmark script, not inside the library itself — examples/ablation_benchmark.py:126-128)"** — wrong. The library fills `api_calls` and `total_tokens` from `lm.history` (`optimizer.py:1521-1529,2007-2018`). These over-count (prior calls, cache hits) and under-count (MIPROv2's proposer runs on `lm.copy()`: 290 requests vs `api_calls=200`).
24. **§4 item 3 (ablation)** — correct as far as it goes; add:
    - the mock script errors on DSPy 3.3.1 (`'Settings' object has no attribute 'lm'`);
    - the "instrumented" benchmark hardcodes compile counts and prints a 1.0× parallel speedup, contradicting the doc's 4–6×;
    - the one live config is mislabelled (`sequential=False` under the name "Sequential + Parallel");
    - in the doc's own 12-example scenario val = 3, so "Max Val=5" is a no-op.
25. **Missed entirely** —
    - the documented custom 4-arg `evaluate_fn` is **silently ignored whenever examples have labels** (regression in 1f24e8d);
    - single-pass returns one sample of descriptions and scores another (identical only through the cache);
    - the optimizer's search metric omits the few-shot demos that the baseline and the final score include;
    - the train/serve prompt skew;
    - `predict(text=dict)` drops the input;
    - text+image examples lose their text inside the optimizer;
    - reserved field-name collisions (`input_data`) and the `str.replace` prefix bug;
    - an `include_fields` typo optimizes all fields;
    - BootstrapFewShot accepts any positive float as success;
    - `dspy.configure` is owned by one thread (Prompter in worker threads);
    - the license contradiction (Apache-2.0 LICENSE vs MIT pyproject);
    - the docs' Python 3.10 vs `requires-python >=3.11`;
    - `Prompter.optimize(system_prompt=...)` raises TypeError, and all three dataset examples pass `model_id=` to `PydanticOptimizer` (TypeError).

## Ten things the skill must say

1. **A metric you pass in must be proven to run.** dspydantic's documented custom `evaluate_fn` is silently replaced by its default when labels exist, and the only test that checks it is gated behind an API key → MET "Custom callables are ignored", TEST "The regression-catching test never runs offline".
2. **Score the exact artifact you return, with the cache off.** Single-pass returns one sample and scores another; they agree only through cache hits → TRAP "The reported score belongs to a different sample", OPT "Single-pass flow".
3. **Compare like with like.** The demos-only baseline made "89% → 100%" (commit 1afc528), and the search metric still omits the demos the acceptance test uses → MET "The documented leakage and unfair-baseline bugs (1afc528)", MET "The search objective differs from the acceptance test".
4. **Check every DSPy kwarg against `inspect.signature` before you run.** BFRS has `num_candidate_programs`; GEPA needs a 5-arg metric, a budget and a `reflection_lm`; MIPROv2's `auto` excludes `num_trials`; SIMBA needs ≥ `bsize` (32) train examples; MIPROv2 needs `dspy[optuna]` in 3.3.1 → OPT (the corresponding items) → check_dspy_surface.py.
5. **Hunt for checks that cannot fail.** List-of-model fields score 1.0 when wrong; tests re-implement the code they test; the docs test only parses; a regex meta-instruction guard passes on reverted originals → TRAP "List-of-model fields always score 1.0", TEST "Tests that re-implement the code under test", TEST "The docs test only parses", MET "Meta-instruction guard".
6. **A parse failure is not a score.** The judge maps it to 0.5 (and `{"score": 85}` to 1.0), the extractor to 0.0, text_similarity to exact match; record `unparsed` instead → MET "ScoreJudge", MET "default_judge_fn", MET "TextSimilarityEvaluator" → lmrun.py (P15/P23).
7. **In DSPy 3.3.1 a signature's class name never reaches the LM.** Domain context must go in the instruction docstring or an input field; MIPROv2's proposer sees module source, instructions, field names and a dataset summary → API "What the LM sees of a class-based signature", SKILL "What MIPROv2's proposer actually sees (3.3.1)" → job 4.
8. **Small, positional validation sets make accept-if-better noise.** n≤20 gives 1–4 validation examples, with no shuffle and no repeats → DATA "Train/val split", TRAP "Accept-if-better on 1–4 examples" → pairs.py folds and repeats (P18).
9. **Count calls at the call site, not from `lm.history`.** `lm.copy()` (MIPROv2's proposer) keeps a separate history, and cache hits and earlier calls are counted: 290 real requests showed as `api_calls=200` → PROD "`api_calls` / `total_tokens`" → lmrun.py.
10. **Optimize the prompt you ship and ship only what you optimized.** dspydantic scores under one prompt format and extracts under another, drops dict inputs at inference, persists training examples in the saved artifact, and breaks on 3.3.1 image inputs (`Image.from_url` wants http(s)) → PROD "Train/serve prompt skew", PROD "Dict input at inference", PROD "Persisted files", API "`dspy.Image` in 3.3.1".
