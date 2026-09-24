# dspy-agent-skills: the core API and operations slice

## 1. Header

- **Repo:** `/home/user/dspy-agent-skills`, a clone of github.com/netzkontrast/dspy-agent-skills. The docs install from the upstream `intertwine/dspy-agent-skills` (`README.md:57,64,73`).
- **Commit:** `9d13f98` ("Merge pull request #6 from netzkontrast/claude/gallant-newton-k6u1jr"). Pack version v0.11.0 (`.claude-plugin/plugin.json:3`, `README.md:186`).
- **License:** MIT, "Copyright (c) 2026 Bryan Young" (`LICENSE`). The skills ported from third parties carry their own licences (`README.md:201-214`). `dspytools` is "see repo", and the TARA repo's README claims MIT but has no LICENSE file.
- **DSPy targeted:** `dspy>=3.3.0,<3.4` (`requirements.txt:13`), validated on 3.3.1. The committed example artifacts were produced on DSPy 3.2.0 (examples 01, 02) and 3.1.3 (example 03) (`examples/README.md:7-11`).
- **Does its API use hold on 3.3.1?** Mostly. Every dry-run passes, and so do the surface check and the test suite. But several call shapes taught as live code fail on 3.3.1:
  - `dspy.load(dir)` without `allow_pickle=True`;
  - `save_as_json` combined with a metric that returns a `dspy.Prediction`, which breaks the README's headline live command;
  - `BetterTogether.compile` without `strategy=` when the optimizers have names;
  - `dspy.GEPA(auto=..., max_metric_calls=...)` with both set;
  - the attribute names on `detailed_results`.
  - It also teaches two budget tables that disagree with DSPy's own `auto_budget` formula, and a claim that "the score is read" for Prediction-returning metrics, which is false for the `BootstrapFewShot` family. See `## TRAP`.
- **What the slice is:** a Markdown skill pack that teaches coding agents DSPy 3.3.x. This slice covers ten core skills: fundamentals, evaluation, GEPA, optimizer selection, production, retrieval, local CLI runtime, dspytools CLI, book router, and the end-to-end workflow. Each has a `SKILL.md`, a `reference.md` and an `example_*.py --dry-run`. Around them sit:
  - `scripts/check_dspy_surface.py`, a live signature check;
  - a pytest suite of regression rules, each written after a documented mistake;
  - a CHANGELOG of corrections;
  - three end-to-end GEPA examples with committed numbers.
- **What I ran.** All runs were offline, with `env -u OPENROUTER_API_KEY -u TYPESAFE_API_KEY -u OPENAI_API_KEY -u ANTHROPIC_API_KEY`:
  - `uv run --with pytest python -m pytest tests/ -q`: **633 passed in 0.87s**.
  - `scripts/check_dspy_surface.py` with the shared DSPy 3.3.1 interpreter (`/home/user/kohaerenzprotokoll/.venv-dspy/bin/python`): **"OK: DSPy 3.3.1 surface matches"**.
  - All 11 `example_*.py --dry-run` in the slice: **exit 0**, run from a scratch cwd, and no files written.
  - The 3 `examples/*/run.py --dry-run` under `uv run --no-project --with dspy==3.3.1 --with rank-bm25 --with python-dotenv`: **exit 0**. The repo documents them for 3.2.0.
  - Nine probe scripts, kept in `scratchpad/das-core-verify/`: `sigs.py`, `behav1.py`, `behav2.py`, `gepa1.py`, `bt.py`, `usage_cb.py`, `fut_ann.py`, `bfs.py`, `artifacts.py`. They use `inspect.signature`, `dspy.utils.DummyLM`, and a `subprocess.run` patched onto the loaded example module.
  - Reads of the installed DSPy 3.3.1 and gepa 0.1.4 source, wherever a claim needed checking.
- **Source paths.** `SP/` is `/home/user/kohaerenzprotokoll/.venv-dspy/lib/python3.11/site-packages/`.
- **Clean-up.** I deleted only the cache directories my own runs created (`.pytest_cache`, `tests/__pycache__`, and two `skills/*/__pycache__` directories). Other readers' `__pycache__` directories were left alone. Nothing else in the repo was changed.

## 2. Knowledge items

## API

- **dspy.configure defaults** — `dspy.configure(**kwargs)` has no explicit signature in 3.3.1. The settings defaults are `track_usage=False`, `async_max_workers=8`, `warn_on_type_mismatch=True`, `max_errors=10`, `num_threads=8`, `adapter=None`, `callbacks=[]`. The reference's pseudo-signature matches these except `num_threads`/`max_errors`, which it omits. `skills/dspy-fundamentals/reference.md:5-16` [api] (verified: behav1.py printed `dspy.settings`) → here: lmrun.py
- **configure belongs to one thread** — calling `dspy.configure(...)` from a second thread raises `RuntimeError: dspy.settings can only be changed by the thread that initially configured it.` The reference says "Sets thread-local defaults" (`skills/dspy-fundamentals/reference.md:18`). That is `dspy.context(...)`, not `configure`. `SP/dspy/dsp/utils/settings.py:127` [trap] (verified: fut_ann.py) → here: pairs.py/graphrag.py whenever threads are used
- **dspy.LM signature (3.3.1)** — `LM(model, model_type='chat', temperature=None, max_tokens=None, cache=True, callbacks=None, num_retries=3, provider=None, finetuning_model=None, launch_kwargs=None, train_kwargs=None, use_developer_role=False, **kwargs)`. `api_key`/`api_base` are **not** named parameters. The reference lists them as such (`skills/dspy-fundamentals/reference.md:26-27`); they pass through `**kwargs` to LiteLLM. [api] (verified: sigs.py) → here: lmrun.py
- **Constructing an LM makes no network call** — "`dspy.LM(...)` is a cheap stub until you actually call it" (`skills/dspy-gepa-optimizer/SKILL.md:199`, `CLAUDE.md:73`). Every dry-run builds `dspy.LM(...)` stubs with no key (`example_gepa.py:77`, `example_optimizer_selection.py:153`). [api] (verified: dry-runs with keys unset) → here: lm_fixture.py
- **OpenAI reasoning models are checked when the LM is constructed** — the check matches `^(?:o[1345](?:-(?:mini|nano|pro))?(?:-\d{4}-\d{2}-\d{2})?|gpt-5(?!-chat)(?:-.*)?)$`. `dspy.LM("openai/gpt-5", temperature=1.0, max_tokens=8000)` raises `LMConfigurationError: ... OpenAI's reasoning models require passing temperature=1.0 or None and max_tokens >= 16000 or None`. `temperature=0.0` gets through, because the check tests `if temperature and ...`. So the examples' `--reflection-model openai/gpt-5` path, with `max_tokens=8000` (`example_gepa.py:93-95`, `example_bettertogether.py:74-78`, `example_pipeline.py:128`), fails at construction. The canonical `dspy.LM("openai/gpt-5", temperature=1.0, max_tokens=32000)` (`skills/dspy-gepa-optimizer/SKILL.md:26`) passes. `SP/dspy/clients/lm.py:48-53,125-133` [trap] (verified: bt.py)
- **rollout_id** — the pack says "`.copy(rollout_id=n)` creates a deterministic variant that bypasses cache collisions" (`skills/dspy-fundamentals/reference.md:42`). The 3.3.1 docstring adds two conditions. First, "Different values bypass DSPy's caches while still caching future calls with the same inputs and rollout ID. Note that `rollout_id` only affects generation when `temperature` is non-zero. This argument is stripped before sending requests to the provider." Second, DSPy warns "rollout_id has no effect when temperature=0; set temperature>0 to bypass the cache." `SP/dspy/clients/lm.py:98-102,165-170` [api] (verified: source) → here: pairs.py repeats (P18)
- **BaseLM constructor and capability properties** — `BaseLM(model, model_type='chat', temperature=None, max_tokens=None, cache=True, callbacks=None, num_retries=3, **kwargs)`. The properties `supports_function_calling`, `supports_reasoning` and `supports_response_schema` default to `False`, and `supported_params` defaults to `set()`. "In 3.3.x, DSPy's adapters read those capability properties directly from `BaseLM`" (`skills/dspy-fundamentals/reference.md:111`). `skills/dspy-fundamentals/reference.md:85-109`, `SP/dspy/clients/base_lm.py:265-283` [api] (verified: sigs.py) → here: lm_fixture.py
- **Two contracts for a custom LM in 3.3.1 (not in the pack)** — `forward_contract = "legacy"`, the default, means `forward(prompt=None, messages=None, **kwargs)` returns an OpenAI-like response. `forward_contract = "typed_lm"` means `forward(request: dspy.LMRequest) -> dspy.LMResponse`, for example `return dspy.LMResponse.from_text("hello", model=request.model)`, called as `lm(dspy.User("..."))` inside `dspy.context(experimental=True)`. The docstring adds: "LMs must be serializable as part of saved DSPy programs ... If a subclass stores additional persistent state, override both methods [dump_state/load_state]". `SP/dspy/clients/base_lm.py:96-170` [api] (verified: source) → here: lm_fixture.py `FixtureLM`
- **BaseLM records usage itself** — `_process_lm_response` does `if not getattr(response, "cache_hit", False) and settings.usage_tracker: settings.usage_tracker.add_usage(self.model, dict(response.usage))`. A custom `forward()` must not add usage again. `SP/dspy/clients/base_lm.py:286-295` [api] (verified: usage_cb.py, see TRAP) → here: lm_fixture.py
- **ContextWindowExceededError** — `dspy.ContextWindowExceededError(*, model=None, message='Context window exceeded', **kwargs)` takes keyword arguments only. The pack's advice: "If your provider throws a context-window exception, translate it to `dspy.ContextWindowExceededError(model=self.model, message=...)` so DSPy's retry/truncation logic can respond correctly." `skills/dspy-fundamentals/reference.md:111` [api] (verified: sigs.py)
- **Two forms of signature** — string shorthand (`dspy.Predict("question -> answer")`, `"context, question -> answer: str"`), or a class whose docstring becomes the instruction. Fields accept Pydantic models, `list[T]`, `dict[K,V]` and `Literal[...]`. `skills/dspy-fundamentals/reference.md:44-59`, `SKILL.md:50-68` [api] (verified: Pydantic output parsed into the model with DummyLM in fut_ann.py)
- **prefix/format/parser are deprecated no-ops** — passing `prefix=`, `format=` or `parser=` to `InputField`/`OutputField` emits `DeprecationWarning: The 'prefix' argument in InputField/OutputField is deprecated and has no effect in DSPy.` Use `desc=` and real types instead. `skills/dspy-fundamentals/reference.md:61`, `SP/dspy/signatures/field.py:10-24,73-85` [api] (verified: source)
- **TypedPredictor and dspy.OpenAI no longer exist** — on 3.3.1 both `hasattr(dspy, "TypedPredictor")` and `hasattr(dspy, "OpenAI")` are False. "Superseded" (`skills/dspy-fundamentals/SKILL.md:52`) undersells it: old code raises `AttributeError`. Anti-patterns 2 and 3 are at `SKILL.md:89-90`. [api] (verified: sigs.py)
- **Predictor constructors (verified)** —
  - `Predict(signature, callbacks=None, **config)`
  - `ChainOfThought(signature, rationale_field=None, rationale_field_type=str, **config)`
  - `ReAct(signature, tools, max_iters=20)`
  - `ProgramOfThought(signature, max_iters=3, interpreter_factory=PythonInterpreter)`
  - `CodeAct(signature, tools, max_iters=5, interpreter_factory=PythonInterpreter)`, which the table omits
  - `RLM(signature, max_iters=20, max_llm_calls=50, max_output_chars=10000, verbose=False, tools=None, sub_lm=None, interpreter_factory=PythonInterpreter)`

  `skills/dspy-fundamentals/reference.md:63-71`, `SKILL.md:40-48` [api] (verified: sigs.py)
- **Refine / BestOfN** — both are `(module, N, reward_fn: Callable[[dict, Prediction], float], threshold, fail_count=None)`. "Refine/BestOfN are dspy.Module subclasses: inspect `__init__` (the class signature is rewritten by the Module metaclass)." `scripts/check_dspy_surface.py:118-125` [api] (verified: sigs.py)
- **ChainOfThought adds `reasoning`** — `pred.reasoning` exists (`skills/dspy-fundamentals/SKILL.md:37,45`). In 3.2.0 and later the saved field prefix is `Reasoning:`; the 3.1.3 artifact has `Reasoning: Let's think step by step in order to`. `examples/*/optimized_program.json` [api] (verified: artifacts inspected)
- **Module methods** — `named_predictors()`, `dump_state()/load_state()`, `save/load`, `inspect_history(n=1, file=None)`, `get_lm()`, `set_lm()`, `acall()`, and `batch(examples, num_threads=None, max_errors=None, return_failed_examples=False, provide_traceback=None, disable_progress_bar=False, timeout=120, straggler_limit=3)`. The reference's `batch(examples, num_threads=8)` is wrong about the default: it is `None`, which falls back to `settings.num_threads=8`. `skills/dspy-fundamentals/reference.md:73-83` [api] (verified: sigs.py)
- **`_compiled` freezes a submodule** — `sub._compiled = True` removes that submodule's predictors from `named_predictors()` (measured: `['inner.p','q']` becomes `['q']`), so optimizers skip it. `BetterTogether` sets `student._compiled = True` on the program it returns. `skills/dspy-fundamentals/reference.md:145`, `skills/dspy-advanced-workflow/SKILL.md:163`, `SP/dspy/teleprompt/bettertogether.py:304` [api] (verified: fut_ann.py)
- **Type-mismatch and extra-field warnings are logging calls** — the messages are "Type mismatch for field 'a': expected str based on given Signature, but the provided value is incompatible: 5." and "Input contains fields not in signature. These fields will be ignored: ['extra']. Expected fields: ['a']." They go through `logging`, not `warnings.warn`, so `warnings.catch_warnings()` or `-W error` cannot turn them into failures. Turn them off with `dspy.configure(warn_on_type_mismatch=False)`. `skills/dspy-fundamentals/SKILL.md:109`, `docs/usage.md:164` [trap] (verified: fut_ann.py captured 0 `warnings`) → here: lmrun.py (P19 assertions must read the log)
- **The `from __future__ import annotations` claim holds only in part** — on 3.3.1, a Pydantic model defined at module level resolves under PEP 563: the annotation is the class. A model defined inside a function stays `ForwardRef('Local')`. The pack's general claim, "`from __future__ import annotations` breaks Pydantic-typed DSPy signatures" (`docs/CHANGELOG.md:391`; `examples/03-invoice-extraction/README.md:102`; `examples/03-invoice-extraction/pipeline.py:7-11`), therefore holds on 3.3.1 only for types that cannot be resolved from module globals. `examples/01-rag-qa/pipeline.py:7` itself uses the future import with a `list[str]` output. [claim→partly verified] (verified: fut_ann.py)
- **Adapters** — `ChatAdapter` (the default), `JSONAdapter`, `XMLAdapter` and `TwoStepAdapter` are all top-level. `ChatAdapter` renders `[[ ## field ## ]]` sections and ends with `[[ ## completed ## ]]`. The reference calls it "JSON-in-markdown with section headers" (`skills/dspy-fundamentals/reference.md:135`), which is wrong.
  - `ChatAdapter(callbacks=None, use_native_function_calling=False, native_response_types=None, use_json_adapter_fallback=True, parallel_tool_calls=None)` falls back to `JSONAdapter` on a parse failure. It does not fall back on an `LMError` or when `use_json_adapter_fallback=False`.
  - `JSONAdapter(callbacks=None, use_native_function_calling=True, parallel_tool_calls=None)`.
  - "XMLAdapter — good for Claude models" is a [claim] (`reference.md:137`).
  - `SP/dspy/adapters/chat_adapter.py:47-92` [api] (verified: sigs.py, inspect_history output)
- **The state-JSON format** — `save(path, save_program=False, modules_to_serialize=None)` writes `{"<predictor path>": {"traces", "train", "demos", "signature", "lm"}, "metadata": {"dependency_versions": {"python","dspy","cloudpickle"}}}`. A `.pkl` suffix saves the same state as a pickle. `skills/dspy-production/reference.md:14,32-48` [api] (verified: behav1.py)
- **A whole-program save needs a directory path** — `save(path, save_program=True)` with a suffix raises `ValueError: \`path\` must point to a directory without a suffix when \`save_program=True\``. It writes `metadata.json` and `program.pkl`. `SP/dspy/primitives/base_module.py:205` [api] (verified: behav1.py)
- **dspy.load needs allow_pickle=True on 3.3.1** — the signature is `dspy.load(path, allow_pickle=False)`. Without the flag it raises `ValueError: Loading with pickle is not allowed. Please set \`allow_pickle=True\` if you are sure you trust the source of the model.` The pack's `dspy.load(dir)` calls all fail. `SP/dspy/utils/saving.py:39-40` [trap] (verified: behav1.py; see TRAP) → here: any saved pairs.py program
- **Module.load(path, allow_pickle=False, allow_unsafe_lm_state=False)** —
  - A `.pkl` state file needs `allow_pickle=True`; without it DSPy raises `ValueError: Loading .pkl files can run arbitrary code ...`.
  - LM state keys in `UNSAFE_LM_STATE_KEYS = {"api_base", "base_url", "model_list"}` are dropped with the warning "Ignoring unsafe LM config key(s) during state load: ['api_base']. Pass allow_unsafe_lm_state=True to preserve these keys for trusted files". The same flag gates importing a custom LM class.
  - `api_key` is never written into the saved state.

  `SP/dspy/primitives/base_module.py:254-292`, `SP/dspy/predict/predict.py:22-40` [api] (verified: behav1.py)
- **State files load across versions** — the committed 3.1.3 and 3.2.0 `optimized_program.json` files load into 3.3.1 programs. Each load logs "There is a mismatch of dspy version between saved model and current environment. You saved with `dspy==3.2.0`, but now you have `dspy==3.3.1`..." and the same for python 3.10 against 3.11. The pack's "a compiled artifact is not portable across majors" (`skills/dspy-production/SKILL.md:177`) is about majors; across 3.x minors it loads, with a warning. [number] (verified: artifacts.py)
- **Prediction's numeric protocol** — `dspy.Prediction` defines `__float__`, `__add__`, `__radd__`, `__truediv__` and comparison operators. `float(Prediction(score=0.25))` is `0.25` and `sum([P, P])` is `0.5`. `float(Prediction(answer="x"))` raises `ValueError: Prediction object does not have a 'score' field to convert to float.` `skills/dspy-evaluation-harness/SKILL.md:16`, `reference.md:51` [api] (verified: behav2.py) → here: pairs.py metric
- **EvaluationResult** — it subclasses `dspy.Prediction`, with fields `score` and `results`, and its docstring reads "score: An float value (e.g., 67.30)". The reference shows it as a `@dataclass` (`skills/dspy-evaluation-harness/reference.md:24-29`), which is wrong in form and silent about scale. `SP/dspy/evaluate/evaluate.py:48-58` [api] (verified: behav2.py)
- **Evaluate signature (3.3.1)** — `Evaluate(*, devset, metric=None, num_threads=None, display_progress=False, display_table=False, max_errors=None, provide_traceback=None, failure_score=0.0, save_as_csv=None, save_as_json=None, **kwargs)` takes keyword arguments only (`skills/dspy-retrieval/reference.md:108` says so correctly). `__call__(program, metric=None, devset=None, num_threads=None, display_progress=None, display_table=None, callback_metadata=None, save_as_csv=None, save_as_json=None)`. The list at `skills/dspy-evaluation-harness/reference.md:7-20` is right about parameters but omits `*` and `**kwargs`. [api] (verified: sigs.py)
- **Evaluate calls the metric with two arguments** — `metric(example, prediction)`, so inside `dspy.Evaluate` the `trace`, `pred_name` and `pred_trace` parameters stay `None`. [api] (verified: behav2.py spy metric saw `(None, None, None)`)
- **Evaluate error handling** — a metric or program exception is logged as `ERROR ... Error for Example({...}) ... Set \`provide_traceback=True\` for traceback.`, and the example scores `failure_score`. The run continues until `max_errors`, whose default is `dspy.settings.max_errors=10`. With `max_errors=0`: `Exception: Execution cancelled due to errors or interruption.` [api] (verified: behav2.py; see TRAP on swallowed failures)
- **display_table needs pandas** — without pandas the table is skipped with the warning "Skipping table display since `pandas` is not installed." `SP/dspy/evaluate/evaluate.py:185-193` [api] (verified: source; pandas absent in the venv)
- **What save_as_json writes** — a list of dicts. Example fields are prefixed `example_`, prediction fields `pred_`, and one extra key holds the metric's `__name__` (a lambda gives `"<lambda>"`). Measured: `[{"question": "a", "example_answer": "a", "pred_answer": "a", "<lambda>": 1.0}]`. It does not create the parent directory. `SP/dspy/evaluate/evaluate.py:195-221` [api] (verified: behav/ad-hoc run)
- **dspy.Parallel** — `Parallel(num_threads=None, max_errors=None, access_examples=True, return_failed_examples=False, provide_traceback=None, disable_progress_bar=False, timeout=120, straggler_limit=3)`. The reference omits `timeout` and `straggler_limit` (`skills/dspy-production/reference.md:27-29`). `forward(exec_pairs, num_threads=None)` accepts `(module, Example)` (unpacked via `.inputs()`), `(module, dict)` (passed as kwargs) or `(module, tuple)` (positional). `SP/dspy/predict/parallel.py:77-110` [api] (verified: sigs.py, source)
- **asyncify / streamify** — `dspy.asyncify(program)` runs the program in a worker thread and carries the caller's thread-local overrides over. It is "a boundary adapter, not a speedup" (`skills/dspy-production/SKILL.md:83`). The signature is `streamify(program, status_message_provider=None, stream_listeners=None, include_final_prediction_in_output_stream=True, is_async_program=False, async_streaming=True)`, and `is_async_program=False` means the program is wrapped with `asyncify`. [api] (verified: sigs.py, `SP/dspy/utils/asyncify.py`)
- **StreamListener** — `StreamListener(signature_field_name, predict=None, predict_name=None, allow_reuse=False)`. The docstring for `allow_reuse=True` says "the stream listener can be reused for multiple streams ... could hurt the performance". The DSPy docstring says: "When the program hit cache, or no listeners captured anything, the final prediction will still be included in the output stream even if this is `False`." `SP/dspy/streaming/streamify.py:50-58`, `streaming_listener.py:40-55,160-175` [api] (verified: source)
- **GLOBAL_HISTORY** — `from dspy.clients.base_lm import GLOBAL_HISTORY` is a list. It is capped at `MAX_HISTORY_SIZE = 10_000` and the oldest entry is popped first. A legacy-path entry is a dict with keys `cost, kwargs, messages, model, model_type, outputs, prompt, response, response_model, timestamp, usage, uuid`; `cost` is `None` on a cache hit. "Treat it as a debugging window, not an audit log" (`skills/dspy-production/reference.md:115-118`). `SP/dspy/clients/base_lm.py:22-23,776-784` [api] (verified: DummyLM run)
- **inspect_history** — `dspy.inspect_history(n=1, file=None)` exists both top-level and as a Module method, and `file=` captures the output. "Most 'the model ignored my instruction' bugs are visible in one line of it" (`skills/dspy-production/SKILL.md:123-126`). [api] (verified: printed a rendered prompt to StringIO)
- **get_lm_usage** — with `track_usage=True`, `pred.get_lm_usage()` returns `{model: {prompt_tokens, completion_tokens, total_tokens}}`. `skills/dspy-production/SKILL.md:65-71` [api] (verified: DummyLM run)
- **BaseCallback hooks (complete list, verified)** — start/end pairs `on_lm_*`, `on_module_*`, `on_tool_*`, `on_adapter_format_*`, `on_adapter_parse_*`, `on_evaluate_*`, `on_compile_*`, plus `on_interpreter_startup_*`, `on_interpreter_execute_*`, `on_interpreter_tool_call_*` and `on_interpreter_shutdown_*`. The signatures are `on_lm_start(call_id, instance, inputs)` and `on_lm_end(call_id, outputs, exception: BaseException|None=None)`. Register with `dspy.configure(callbacks=[cb])`, or per module with `dspy.Predict(sig, callbacks=[cb])`. `skills/dspy-production/reference.md:73-101` [api] (verified: sigs.py)
- **configure_cache defaults (verified)** — `configure_cache(enable_disk_cache=True, enable_memory_cache=True, disk_cache_dir=$DSPY_CACHEDIR or ~/.dspy_cache, disk_size_limit_bytes=3e10 (env DSPY_CACHE_LIMIT), memory_max_entries=1_000_000, restrict_pickle=False, safe_types=None)`. It replaces `dspy.cache`.
  - `DSPY_CACHEDIR` is read at import time, so set it before `import dspy` or pass `disk_cache_dir`.
  - A `safe_types` entry that is not a type raises `TypeError`.
  - With `restrict_pickle=True`, an allowlist of `(module, qualname)` is enforced and a `DeserializationError` counts as a cache miss.

  `skills/dspy-production/reference.md:10-12,50-65`, `SP/dspy/clients/__init__.py:15-16,19-55`, `SP/dspy/clients/cache.py:84-137` [api] (verified: sigs.py, source)
- **Embedder** — `Embedder(model: str|Callable, batch_size=200, caching=True, **kwargs)`; `__call__(inputs: str|list[str], batch_size=None, caching=None, **kwargs) -> np.ndarray`. `skills/dspy-retrieval/reference.md:12,47-54` [api] (verified: sigs.py)
- **Top-level primitives** — `dspy.Reasoning`, `File`, `Code`, `PythonInterpreter`, `History`, `Tool`, `Image` and `Audio` all exist. `dspy.utils.PythonInterpreter` does not, and never did (`docs/CHANGELOG.md:37-43`). `scripts/check_dspy_surface.py:127-128,169-171` [api] (verified: sigs.py)
- **dspy.Flex (3.3.1, not taught)** — `dspy.Flex` exists. GEPA treats a Flex submodule's `module_src` as a candidate component, so its *code* is optimized, not only its instructions. A metric may declare a sixth parameter, `program_trace`, "populated during candidate *scoring*" (for example `len(program_trace)` as an LM-call count). `SP/dspy/teleprompt/gepa/gepa.py:36-48,548,628-630` [api] (verified: source)
- **Common provider prefixes** — `openai/`, `anthropic/`, `azure/`, `vertex_ai/`, `bedrock/`, `ollama/`. For Ollama: `dspy.LM("ollama_chat/llama3.1:8b", api_base="http://localhost:11434")`. For Vertex, use `vertex_ai/` rather than `gemini/`, with `vertex_project` and `vertex_location`. `skills/dspy-fundamentals/SKILL.md:111`, `reference.md:146` [claim]
- **Provider-side prompt caching** — "via `cache_control_injection_points` on `dspy.LM(...)`", for long repeated system prompts such as `dspy.ReAct`. It is a LiteLLM kwarg passed through `**kwargs`. `skills/dspy-fundamentals/reference.md:129` [claim]

## OPT

- **GEPA is Genetic-Pareto** — "The expansion 'Genetic-Evolutionary Prompt Adaptation' that appears in some AI-generated summaries is an LLM-hallucinated backronym ... the 'Pareto' is load-bearing (GEPA keeps a frontier of candidates rather than collapsing to one)." arXiv 2507.19457. `skills/dspy-gepa-optimizer/SKILL.md:11`, `docs/CHANGELOG.md:395-397` [claim]
- **GEPA constructor (3.3.1, verified)** — `GEPA(metric, *, auto=None, max_full_evals=None, max_metric_calls=None, reflection_minibatch_size=3, candidate_selection_strategy='pareto', reflection_lm=None, skip_perfect_score=True, add_format_failure_as_feedback=False, instruction_proposer=None, component_selector='round_robin', use_merge=True, max_merge_invocations=5, num_threads=None, failure_score=0.0, perfect_score=1.0, log_dir=None, track_stats=False, use_wandb=False, wandb_api_key=None, wandb_init_kwargs=None, track_best_outputs=False, warn_on_score_mismatch=True, use_mlflow=False, seed=0, gepa_kwargs=None)`. That is 26 parameters, and every one after `metric` is keyword-only; the reference omits the `*`. `skills/dspy-gepa-optimizer/reference.md:11-42`, `SKILL.md:97-128` [api] (verified: sigs.py) → here: pairs.py GEPA rung
- **GEPA checks the metric's arity at construction** — `inspect.signature(metric).bind(None, None, None, None, None)`, and a failure raises `TypeError: GEPA metric must accept five arguments: (gold, pred, trace, pred_name, pred_trace).` Measured: a metric shaped `(g, p, trace=None)` or `(g, p, trace=None, **kw)` is rejected; `*args` and the full 5-argument form are accepted. `SP/dspy/teleprompt/gepa/gepa.py:416-422` [api] (verified: ad-hoc GEPA constructions) → here: pairs.py
- **reflection_lm is required at construction** — `AssertionError: GEPA requires a reflection language model, or custom instruction proposer to be provided. Typically, you can use \`dspy.LM(model='gpt-5', temperature=1.0, max_tokens=32000)\` to get a good reflection model. ...` It cannot be deferred to `.compile()`. `skills/dspy-gepa-optimizer/SKILL.md:191-199`, `CLAUDE.md:73`, `docs/CHANGELOG.md:366`, `SP/dspy/teleprompt/gepa/gepa.py:441-445` [api] (verified: gepa1.py) → here: pairs.py `--dry-run` must build a stub LM
- **Exactly one budget** — `AssertionError: Exactly one of max_metric_calls, max_full_evals, auto must be set. You set max_metric_calls=300, max_full_evals=None, auto=light.` The same assertion fires when none is set. `skills/dspy-gepa-optimizer/SKILL.md:85`, `SP/dspy/teleprompt/gepa/gepa.py:427-432` [api] (verified: gepa1.py)
- **The auto budget is a formula, not a table** — `auto_budget(num_preds, num_candidates, valset_size, minibatch_size=35, full_eval_steps=5)`:
  - `N = int(max(2*(num_preds*2)*log2(num_candidates), 1.5*num_candidates))`
  - `total = V + 5*num_candidates + N*35 + ((N+1)//5 + 1 + [N<5]) * V`
  - `num_candidates` comes from `AUTO_RUN_SETTINGS = {light: 6, medium: 12, heavy: 18}`, and `num_preds` is the number of predictors plus Flex submodules.

  In closed form this is: for 1 predictor, **light = 380 + 4V**, **medium = 690 + 5V**, **heavy = 1035 + 7V** metric calls; for 3 predictors, light = 1115 + 8V. `SP/dspy/teleprompt/gepa/gepa.py:20,490-520,552-558` [number] (verified: gepa1.py computed a V×preds grid) → here: pairs.py budgeting, baseline.py
- **auto budget, measured values** — for 1 predictor, V=10: light 420, medium 740, heavy 1105 metric calls. For 1 predictor, V=9: light **416**. That is exactly the `"planned_rollouts": 416` recorded for example 03 (1 predictor, valset 9) at `examples/03-invoice-extraction/version_comparison.json` and README:25, so the formula is confirmed by the repo's own run. For 1 predictor, V=100: light 780. For 3 predictors, V=10: light 1195. [number] (verified: gepa1.py)
- **max_full_evals counts train+val** — `max_metric_calls = max_full_evals * (len(trainset) + len(valset))`. DSPy logs "Running GEPA for approx {N} metric calls of the program. This amounts to {N/(train+val)} full evals on the train+val set." `SP/dspy/teleprompt/gepa/gepa.py:559-566` [api] (verified: source)
- **Without a valset, GEPA uses the trainset for both** — it warns "No valset provided; Using trainset as valset ... it makes GEPA overfit prompts to the provided trainset ... Provide the smallest valset that is just large enough to match the downstream task distribution, while keeping trainset as large as possible." With a valset larger than 35 it logs advice to use a smaller sample. `SP/dspy/teleprompt/gepa/gepa.py:568-581` [api] (verified: source)
- **Checks inside GEPA.compile** — `assert trainset is not None and len(trainset) > 0, "Trainset must be provided and non-empty"` and `assert teacher is None, "Teacher is not supported in DspyGEPA yet."`. So passing a teacher raises; the pack says "`teacher` is not currently used" (`skills/dspy-gepa-optimizer/SKILL.md:130`, `reference.md:51`). `SP/dspy/teleprompt/gepa/gepa.py:544-545` [api] (verified: source)
- **How GEPA calls the metric for feedback** — `self.metric_fn(module_inputs, module_outputs, captured_trace, pred_name, trace_for_pred)`, with five positional arguments.
  - A float return is wrapped as `dict(score=o, feedback=f"This trajectory got a score of {o}.")`.
  - A Prediction whose `feedback` is `None` gets the same text.
  - So a float metric does run under GEPA, but reflection reads only the number. The skill's "GEPA needs the score+feedback pair" (`skills/dspy-evaluation-harness/SKILL.md:16`) overstates it, while "Float-only metric ... GEPA collapses to random search" (`skills/dspy-gepa-optimizer/SKILL.md:185`) is a [claim].

  `SP/dspy/teleprompt/gepa/gepa.py:585-609` [api] (verified: source)
- **Per-predictor scores are ignored** — "GEPA does not support predictor level scoring (support coming soon), and only requires a feedback text ... GEPA will ignore the differing score returned, and instead use module level score." This warning fires once, unless `warn_on_score_mismatch=False`. With `pred_name` set, return the module-level score and per-predictor *feedback*. `SP/dspy/teleprompt/gepa/gepa_utils.py:420-430` [api] (verified: source) → here: pairs.py metric
- **Parse failures and reflection** — with `add_format_failure_as_feedback=False` (the default), `FailedPrediction` traces are dropped from the reflective dataset. With `True`, the raw completion is included along with "Your output failed to parse. Follow this structure:" and the ChatAdapter-rendered format. `SP/dspy/teleprompt/gepa/gepa_utils.py:349-352,405-413` [api] (verified: source)
- **The reflective dataset record** — `{"Inputs": {...}, "Generated Outputs": {...} | str, "Feedback": str}`. `dspy.History` inputs are rendered as a JSON list under `"Context"`. If no valid traces exist the log reads "No valid reflective examples found for {pred_name}". `SP/dspy/teleprompt/gepa/gepa_utils.py:340-440` [api] (verified: source)
- **Failures during GEPA evaluation** — metric exceptions score `failure_score`, because the inner `Evaluate` runs with `provide_traceback=True, max_errors=len(batch)*100`. A Flex candidate that fails to build scores the batch as failures. "an LM provider or rate-limit error ... is not the candidate's fault and must propagate". `raise_on_exception=True` is passed to `gepa.optimize`. `SP/dspy/teleprompt/gepa/gepa_utils.py:201-270`, `gepa.py:658` [api] (verified: source)
- **skip_perfect_score** — a reflection step is skipped when `all(s >= perfect_score for s in minibatch_scores)`, and the log reads "Iteration {i}: All subsample scores perfect for parent {idx}. Skipping." `perfect_score=1.0` is "The maximum score achievable by the metric". `SP/gepa/proposer/reflective_mutation/reflective_mutation.py:395-400`, `SP/dspy/teleprompt/gepa/gepa.py:303` [api] (verified: source)
- **The minibatch sampler is epoch-shuffled** — `EpochShuffledBatchSampler` shuffles every train id each epoch and pads to a multiple of the minibatch size with the least-used ids, seeded. So every training example appears once per epoch. The minibatch size changes how often a failing example is drawn, not whether it is drawn. `SP/gepa/strategies/batch_sampler.py:26-66` [api] (verified: source)
- **reflection_minibatch_size guidance** —
  - Example 02 comments that "With ~83% baseline accuracy on this task, minibatch=3 kept sampling all-correct subsets for 139 iterations (reflection LM never called). 8 lifts P(at-least-one-failure) above ~0.75 per iteration on a trainset with ~4/25 failures" (`examples/02-math-reasoning/run.py:144-148`). The arithmetic 1−(21/25)^8 = 0.75 holds, but the trainset there has 34 rows, not 25. Under gepa 0.1.4's epoch sampler, 139 consecutive all-perfect minibatches means the trainset had no failures at all.
  - The pack's advice in two places is to raise the minibatch to 6–8 when the baseline is above 0.7 for a plateau, and lower it to 2 for oscillation (`skills/dspy-advanced-workflow/reference.md:125`, `docs/CHANGELOG.md:392`, `skills/dspy-gepa-optimizer/reference.md:121`).

  [claim] (not reproducible offline)
- **candidate_selection_strategy** — gepa 0.1.4 accepts `'pareto'`, `'current_best'`, `'epsilon_greedy'` (ε=0.1) and `'top_k_pareto'`, or a `CandidateSelector` instance. DSPy types only the first two but forwards the string; an unknown string fails at compile ("Unknown candidate_selector strategy"). `SP/gepa/api.py:56-57,307-326` [api] (verified: gepa1.py constructed with `epsilon_greedy`)
- **component_selector** — `'round_robin'` (the default), `'all'`, or a `ReflectionComponentSelector` with `__call__(state, trajectories, subsample_scores, candidate_idx, candidate) -> list[str]`. `'random'` constructs, then fails at compile with `AssertionError: Unknown module_selector strategy: random. Supported strategies: 'round_robin', 'all'`. The pack's test forbids teaching it (`tests/test_skill_correctness.py:351-353`). `skills/dspy-gepa-optimizer/reference.md:77-81`, `SP/gepa/api.py:336-348`, `SP/gepa/proposer/reflective_mutation/base.py:16-24` [api] (verified: gepa1.py, source)
- **instruction_proposer protocol** — `ProposalFn.__call__(candidate: dict[str,str], reflective_dataset: Mapping[str, Sequence[Mapping[str, Any]]], components_to_update: list[str]) -> dict[str,str]`. The pack's `(program, reflections, trace) -> str` (`skills/dspy-gepa-optimizer/reference.md:85`) is wrong. A custom proposer is also the only way to change the reflection prompt, because `reflection_prompt_template` passed through `gepa_kwargs` raises `ValueError`. `SP/gepa/core/adapter.py:47-65`, `SP/dspy/teleprompt/gepa/gepa.py:483-488` [api] (verified: source)
- **track_best_outputs requires track_stats** — construction asserts `"track_stats must be True if track_best_outputs is True."` `SP/dspy/teleprompt/gepa/gepa.py:469-471` [api] (verified: source)
- **detailed_results (DspyGEPAResult) fields** — `candidates`, `parents`, `val_aggregate_scores` (a per-candidate aggregate valset score), `val_subscores`, `per_val_instance_best_candidates`, `discovery_eval_counts`, `best_outputs_valset`, `total_metric_calls`, `num_full_val_evals`, `log_dir`, `seed`, `val_aggregate_subscores`, `per_objective_best_candidates`, `objective_pareto_front`. Its properties are `best_idx`, `best_candidate` and `highest_score_achieved_per_val_task`. It is `@experimental(version="3.0.0")` and `@dataclass(frozen=True)`, and exists only when `track_stats=True`. The pack's `candidate_programs` and `reflection_traces` (`skills/dspy-gepa-optimizer/reference.md:58-61`) do not exist. `SP/dspy/teleprompt/gepa/gepa.py:64-127` [api] (verified: source) → here: pairs.py ledger fields
- **GEPA as batch inference-time search** — "passing `valset=trainset, track_stats=True, track_best_outputs=True`, and using ... `optimized_program.detailed_results.best_outputs_valset` [which] will contain the best outputs for each task in the batch." `SP/dspy/teleprompt/gepa/gepa.py:235-243`, `skills/dspy-gepa-optimizer/SKILL.md:179-181` [api] (verified: source)
- **What log_dir actually holds** — `gepa_state.bin` (written atomically as pickle, or cloudpickle), `run_log.json`, `candidates.json`, `generated_best_outputs_valset/task_<id>/`, and `candidate_tree.html`. When `gepa_state.bin` exists the run resumes, logging "Loading gepa state from run dir". A `frontier_type` mismatch raises `ValueError`. The pack's `candidates/<id>.json`, `scores.jsonl`, `reflections/` and `<log_dir>/candidates/` (`skills/dspy-gepa-optimizer/reference.md:93`, `SKILL.md:177`) do not match gepa 0.1.4. Constructing GEPA with `log_dir` creates nothing. `SP/gepa/core/state.py:306-346,660-690`, `SP/gepa/core/engine.py:983-988` [api] (verified: source; dry-run left cwd empty)
- **Stale state resumes silently** — "Clear `gepa_logs/` before cross-version reruns; otherwise GEPA will resume from the previous saved state" (`examples/README.md:96`). Examples 01 and 02 note that GEPA checkpoints to `gepa_logs/gepa_state.bin` (`examples/01-rag-qa/README.md:82`). [pattern] → here: pairs.py must use a fresh log_dir per run
- **use_cloudpickle** — `gepa_kwargs={"use_cloudpickle": True}` is needed when the state holds dynamically generated classes, such as signatures or modules defined inside functions (`examples/02-math-reasoning/run.py:156-159`), ChainOfThought's synthesized signature subclass (`examples/01-rag-qa/run.py:157-161`), or Pydantic outputs (`examples/03-invoice-extraction/run.py:156-159`). gepa's own error hint is "Hint: standard pickle failed to serialize the GEPA state. Try setting use_cloudpickle=True". If cloudpickle is missing, gepa warns and falls back to pickle. Registering the pipeline module in `sys.modules` before `exec_module` also helps plain pickle (`examples/03-invoice-extraction/run.py:30-32`). `SP/gepa/core/state.py:306-338` [recipe] (verified: source)
- **gepa_kwargs pass-through** — the documented keys are `batch_sampler`, `merge_val_overlap_floor`, `stop_callbacks` (FileStopper, TimeoutStopCondition, SignalStopper, NoImprovementStopper; "This overrides the default max_metric_calls stopping condition"), `use_cloudpickle`, `val_evaluation_policy`, `use_mlflow`, `mlflow_tracking_uri`, `mlflow_experiment_name`, `sampling_strategy`, `selection_strategy`, `acceptance_criterion` (default `'strict_improvement'`), `wandb_attach_existing`, `mlflow_attach_existing` and `tracking_key_prefix`.
  - `max_reflection_cost` raises `ValueError("max_reflection_cost is not supported by dspy.GEPA yet.")`.
  - The docstring says keys that duplicate explicit parameters "will be overridden". But `optimize(..., seed=self.seed, **self.gepa_kwargs)` would raise `TypeError` on a duplicate key; that follows from Python call semantics.

  `SP/dspy/teleprompt/gepa/gepa.py:321-356,478-488,632-662` [api] (verified: source)
- **Multi-objective GEPA (3.3.1, not taught)** — a metric's `dspy.Prediction` may carry `objective_scores: dict[str, float]`, which fills `val_aggregate_subscores` and `objective_pareto_front`. gepa takes `frontier_type` from `'instance'|'objective'|'hybrid'|'cartesian'` (default `'instance'`). `SP/dspy/teleprompt/gepa/gepa_utils.py:55-66`, `SP/gepa/api.py:46-60` [api] (verified: source)
- **The gepa pin** — DSPy 3.3.1 requires `gepa[dspy]==0.1.4`. `optuna` and `numpy` are extras (`dspy[optuna]`, `dspy[numpy]`). `use_merge` defaults to `False` in gepa but `True` in dspy.GEPA. [api] (verified: importlib.metadata)
- **Import paths** — `dspy.GEPA` is preferred; `from dspy.teleprompt import GEPA` and `dspy.teleprompt.gepa.gepa.GEPA` resolve to the same class. `from dspy.optimizers import GEPA` was a draft error (`docs/CHANGELOG.md:354`). `skills/dspy-gepa-optimizer/SKILL.md:56-65`, `reference.md:5-9` [api]
- **GEPA data split** — "maximize the training set and reserve only enough validation examples to represent downstream behavior". That contrasts with the "20% train / 80% validation" that DSPy recommends for other prompt optimizers. MIPROv2's default split really is 20/80: see the MIPROv2 compile item. `skills/dspy-gepa-optimizer/SKILL.md:132-134`, `reference.md:126-128`, `skills/dspy-advanced-workflow/reference.md:130-132` [claim]
- **When to prefer GEPA, MIPROv2 or SIMBA** — prefer GEPA when the metric can produce "specific, teachable critiques", when there are several predictors, or when the rollout budget is small. Prefer MIPROv2 for a scalar-only metric, for pure few-shot bootstrapping, or for 500+ examples. SIMBA is "a lighter reflective optimizer". `skills/dspy-gepa-optimizer/SKILL.md:159-173` [claim]
- **GEPA anti-patterns** — a float-only metric; the same set used for train and val; a small reflection LM ("it can't critique"); running `auto="heavy"` on an untested metric instead of `light` first; ignoring `log_dir`. `skills/dspy-gepa-optimizer/SKILL.md:183-189` [claim]
- **GEPA tuning table** — no improvement: check feedback specificity and reflection LM strength. Oscillation: `reflection_minibatch_size` 3→2 and `pareto`. OOM: lower the reflection LM's `max_tokens`. Cost: an explicit `max_metric_calls`. Held-out regression: a bigger or more representative valset. `skills/dspy-gepa-optimizer/reference.md:116-124` [claim]
- **Plateau checks** — run the metric by hand on 5 failing examples; if the feedback is vague, "GEPA has nothing to learn from". Also check train/val overlap, the reflection LM's strength ("a 7B model reflecting on a 70B model's output rarely helps"), and saturation ("Baseline >0.95 means GEPA correctly no-ops"). `skills/dspy-advanced-workflow/reference.md:120-128` [claim]
- **BetterTogether (3.3.1)** —
  - Signatures: `BetterTogether(metric, **optimizers: Teleprompter)`; `compile(student, *, trainset, teacher=None, valset=None, num_threads=None, max_errors=None, provide_traceback=None, seed=None, valset_ratio=0.1, shuffle_trainset_between_steps=True, strategy='p -> w -> p', optimizer_compile_args=None)`.
  - A non-Teleprompter raises `TypeError: Optimizer 'gepa' must be a Teleprompter, got function`.
  - Without named optimizers the defaults are `p=BootstrapFewShotWithRandomSearch(metric)` and `w=BootstrapFinetune(metric)`.
  - The strategy keys must be constructor keyword names, joined with `" -> "`.

  `skills/dspy-gepa-optimizer/SKILL.md:136-157`, `SP/dspy/teleprompt/bettertogether.py:142-192,347-360` [api] (verified: sigs.py, bt.py) → here: none planned
- **BetterTogether with named optimizers needs an explicit strategy** — measured: `bt.compile(p, trainset=train)` raises `ValueError: Strategy contains invalid optimizer keys: ['p', 'w', 'p']. Valid keys are: ['bootstrap', 'gepa']`. This happens with or without `set_lm`. The gepa skill says so (`skills/dspy-gepa-optimizer/SKILL.md:155`, `reference.md:114`, `skills/dspy-advanced-workflow/reference.md:69`). The optimizer-selection skill contradicts it: see TRAP. [api] (verified: bt.py)
- **What BetterTogether returns** — `candidate_programs`, a list of `{'program','score','strategy'}` sorted best first, with the earlier program winning ties, plus `flag_compilation_error_occurred`. The baseline evaluation counts as strategy `""`. Without a valset, the *latest* program is returned. `example_bettertogether.py:150` reads `optimized.candidate_programs[0]["strategy"] or "baseline"`. `SP/dspy/teleprompt/bettertogether.py:424-505` [api] (verified: source)
- **BetterTogether's valset_ratio** — without a valset it takes `valset = trainset[:int(0.1*len)]`, the first 10%, unshuffled. For 10 examples that leaves a 1-example valset, as logged: "Created validation set: 1 examples. Training set: 9 examples." `valset_ratio` must be in [0, 1); at 0 there is no validation and the latest program wins. `SP/dspy/teleprompt/bettertogether.py:320-345` [trap] (verified: bt.py log)
- **BetterTogether's LM requirements** — the docstring says "program.set_lm(lm) can be used to assign a language model to all modules". `example_bettertogether.py:120,128` calls `program.set_lm(task_lm)`. The metric docstring: "Should accept `(example, prediction, trace=None)` and return a numeric score". `SP/dspy/teleprompt/bettertogether.py:59,150-152,307-318` [api] (verified: source)
- **MIPROv2 constructor (3.3.1)** — `MIPROv2(metric, prompt_model=None, task_model=None, teacher_settings=None, max_bootstrapped_demos=4, max_labeled_demos=4, auto='light', num_candidates=None, num_threads=None, max_errors=None, seed=9, init_temperature=1.0, verbose=False, track_stats=True, log_dir=None, metric_threshold=None)`. With no `dspy.configure(lm=...)` and no `prompt_model`/`task_model` pair it raises `ValueError: Either provide both prompt_model and task_model or set a default LM through dspy.configure(lm=...)` at construction. `skills/dspy-optimizer-selection/reference.md:12-16`, `SKILL.md:104-109` [api] (verified: sigs.py, bt.py)
- **MIPROv2 compile rules (3.3.1, not taught)** —
  - Signature: `compile(student, *, trainset, teacher=None, valset=None, num_trials=None, max_bootstrapped_demos=None, max_labeled_demos=None, seed=None, minibatch=True, minibatch_size=35, minibatch_full_eval_steps=5, program_aware_proposer=True, data_aware_proposer=True, view_data_batch_size=10, tip_aware_proposer=True, fewshot_aware_proposer=True, requires_permission_to_run=None, provide_traceback=None)`.
  - Passing `requires_permission_to_run` raises "User confirmation is removed from MIPROv2."
  - `auto` combined with `num_candidates`/`num_trials` raises `ValueError`; with `auto=None`, both are required.
  - The auto settings are light n=6 val_size=100, medium 12/300, heavy 18/1000; the valset is subsampled to `val_size`, and `minibatch = len(valset) > 50`.
  - Without auto, `minibatch_size > len(valset)` raises "Minibatch size cannot exceed the size of the valset."
  - With `valset=None`, the last 80% of the trainset (capped at 1000) becomes the valset, and fewer than 2 examples raises.

  `SP/dspy/teleprompt/mipro_optimizer_v2.py:42-50,180-215,286-334` [api] (verified: ad-hoc run, source)
- **MIPROv2 requires optuna** — `_import_optuna()` raises `ImportError: MIPROv2 requires optional dependency 'optuna'. Install it with \`pip install dspy[optuna]\`.` It is called in step 3, "finding optimal prompt parameters", after demo bootstrapping (step 1) and instruction proposal (step 2) have already spent LM calls. `requirements-extras.txt:12-13` says "Without it, MIPROv2 falls back to a non-Bayesian search path", which is false on 3.3.1. `SP/dspy/teleprompt/mipro_optimizer_v2.py:28-39,520` [trap] (verified: source; optuna absent in the venv)
- **SIMBA (3.3.1)** —
  - `SIMBA(*, metric, bsize=32, num_candidates=6, max_steps=8, max_demos=4, prompt_model=None, teacher_settings=None, demo_input_field_maxlen=100000, num_threads=None, temperature_for_sampling=0.2, temperature_for_candidates=0.2)`; `compile(student, *, trainset, seed=0)`.
  - A positional metric raises `TypeError: SIMBA.__init__() takes 1 positional argument but 2 were given`.
  - `np = require("numpy")`, so SIMBA needs numpy.
  - `assert len(trainset) >= self.bsize, f"Trainset too small: {len(trainset)} < {self.bsize}"`, so with the default bsize a trainset under 32 fails.

  `skills/dspy-optimizer-selection/reference.md:18-21`, `SP/dspy/teleprompt/simba.py:12,105` [api] (verified: sigs.py, bt.py, source) → here: pairs.py SIMBA rung (set `bsize` ≤ folds)
- **SIMBA's metric wrapper** — `output = metric(example, prediction)`. An `int`/`float` is the score. A `dspy.Prediction` must have `.score`, and its other fields go into `output_metadata`. A Prediction without `score` raises a `ValueError` that is **logged as a warning and scored 0.0**; so is any metric exception. `SP/dspy/teleprompt/simba_utils.py:40-67` [api] (verified: source)
- **BootstrapFewShot** — `BootstrapFewShot(metric=None, metric_threshold=None, teacher_settings=None, max_bootstrapped_demos=4, max_labeled_demos=16, max_rounds=1, max_errors=None)`; `compile(student, *, teacher=None, trainset)`. Success is `metric_val >= metric_threshold` when a threshold is set; otherwise it is **`metric_val` itself**, used for its truthiness. `SP/dspy/teleprompt/bootstrap.py:204-212` [api] (verified: sigs.py, source; see TRAP)
- **BootstrapFewShotWithRandomSearch** — `BootstrapFewShotWithRandomSearch(metric, teacher_settings=None, max_bootstrapped_demos=4, max_labeled_demos=16, max_rounds=1, num_candidate_programs=16, num_threads=None, max_errors=None, stop_at_score=None, metric_threshold=None)`. `metric` is required. The alias is `dspy.BootstrapRS`. Construction prints "Going to sample between 1 and 4 traces per predictor. Will attempt to bootstrap 16 candidate sets." `compile(student, *, teacher=None, trainset, valset=None, restrict=None, labeled_sample=True)`. It bootstraps through inner `BootstrapFewShot(... metric_threshold=self.metric_threshold)`. `SP/dspy/teleprompt/random_search.py:39-47,92-111` [api] (verified: dry-run output, sigs.py)
- **LabeledFewShot** — `LabeledFewShot(k=16)` has no metric; `compile(student, *, trainset, sample=True)`. It uses `rng = random.Random(0)` and `rng.sample(trainset, min(k, len(trainset)))` per predictor, so the sample is deterministic. An empty trainset returns the student unchanged. `SP/dspy/teleprompt/vanilla.py:10-22` [api] (verified: source) → here: pairs.py first rung
- **KNNFewShot embeds the trainset at construction** — `KNNFewShot(k, trainset, vectorizer: Embedder, **few_shot_bootstrap_args)`; `compile(student, *, teacher=None)`. `KNN.__init__` runs `self.trainset_vectors = self.embedding(...)` straight away, so building one with a hosted `dspy.Embedder` makes API calls. That is why the optimizer-selection dry-run constructs every optimizer *except* KNNFewShot (`example_optimizer_selection.py:156-158`). The KNN-with-bootstrap `num_threads` trap belongs to the book slice. `SP/dspy/predict/knn.py:40-47`, `SP/dspy/teleprompt/knn_fewshot.py:52` [trap] (verified: source)
- **COPRO / BootstrapFinetune / Ensemble** —
  - `COPRO(prompt_model=None, metric=None, breadth=10, depth=3, init_temperature=1.4, track_stats=False, **_kwargs)`; `compile(student, *, trainset, eval_kwargs=None)`.
  - `BootstrapFinetune(metric=None, multitask=True, train_kwargs=None, adapter=None, exclude_demos=False, num_threads=None)`, where `train_kwargs` and `adapter` may be per-LM dicts; `compile(student, trainset, teacher=None)`.
  - `Ensemble(*, reduce_fn=None, size=None, deterministic=False)`; `compile(programs)`, with `dspy.majority` as a reducer.

  `skills/dspy-optimizer-selection/reference.md:23-63` [api] (verified: sigs.py)
- **InferRules exists in 3.3.1, and the pack teaches nothing about it** —
  - `class InferRules(BootstrapFewShot)`; `InferRules(num_candidates=10, num_rules=10, num_threads=None, teacher_settings=None, **kwargs)`, where `metric`, `metric_threshold`, `max_errors` and the demo counts go to BootstrapFewShot; `compile(student, *, teacher=None, trainset, valset=None)`.
  - With `valset=None` the trainset is split at 50%, first half train and second half val, unshuffled.
  - It first bootstraps demos, which inherits the truthiness trap. Then, for each of `num_candidates` candidates, it asks a `ChainOfThought` rule inducer "extract a list of {num_rules} concise and non-redundant natural language rules ..." over *all* train examples formatted as "Input Fields: ... Output Fields: ...". Examples are dropped from the end until they fit the context; a single example that does not fit raises `RuntimeError`.
  - Each candidate appends "Please adhere to the following rules when making your prediction:\n{rules}", is scored by `Evaluate` on the valset (a percent score), and the best is returned.
  - Rule induction runs on `dspy.settings.lm.copy(rollout_id=rng.randint(0, 10**9), temperature=1.0)` with `rng = random.Random(0)`, so reruns reuse the same rollout ids and replay from cache when the cache is on.

  `SP/dspy/teleprompt/infer_rules.py:12-60,61-150` [api] (verified: sigs.py, source) → here: pairs.py InferRules rung
- **The selection matrix** — read top to bottom and stop at the first row you can satisfy: LabeledFewShot (any trainset, no metric) → BootstrapFewShot (~10+) → BootstrapRS (50+) → KNNFewShot (varied inputs) → COPRO (instructions) → MIPROv2 (100+, scalar, optuna) → GEPA (feedback) → SIMBA (cheaper reflective pass) → BootstrapFinetune → Ensemble → BetterTogether → "GEPA over a custom adapter" for a text artifact. `skills/dspy-optimizer-selection/SKILL.md:40-57` [claim] → here: pairs.py ladder
- **Escalation order** — baseline → LabeledFewShot → BootstrapFewShot → BootstrapRS; on a plateau, MIPROv2/SIMBA for a scalar metric or GEPA for rich feedback; then BootstrapFinetune/BetterTogether. "Escalate only on a measured plateau. Two optimizers in a row that fail to beat the baseline usually mean the metric is wrong, not that the optimizer is weak." `skills/dspy-optimizer-selection/SKILL.md:59-73` [claim] → here: pairs.py, baseline.py
- **Trainset-size table** — under 10: LabeledFewShot; 10–50: BootstrapFewShot, SIMBA; 50–100: BootstrapRS, SIMBA, GEPA; 100–500: MIPROv2, GEPA, BootstrapRS; 500+: MIPROv2, BootstrapFinetune, BetterTogether. "GEPA ... learns from the *feedback text* of a few dozen informative failures, so a train-heavy split of 20–50 well-chosen examples often beats 500 bland ones." SIMBA in the 10–50 row contradicts its default `bsize=32` assertion. `skills/dspy-optimizer-selection/reference.md:65-78` [claim]
- **The deterministic `recommend()`** — it encodes the matrix as a function. No baseline gives `"none"`. More than one candidate program gives Ensemble. Fewer than 10 examples, or no metric, gives LabeledFewShot. A plateau with a finetunable LM gives BetterTogether; a plateau without one gives MIPROv2, whatever the metric's shape. Per-input demos give KNNFewShot, feedback gives GEPA, 100+ gives MIPROv2, 50+ gives BootstrapRS, otherwise BootstrapFewShot. It never returns SIMBA, COPRO or BootstrapFinetune. `skills/dspy-optimizer-selection/example_optimizer_selection.py:49-69` [pattern] (verified: dry-run printed 10 routes)
- **Teacher and prompt models** — `BootstrapFewShot(metric=..., teacher_settings=dict(lm=dspy.LM("openai/gpt-5")))`. MIPROv2 separates `prompt_model`, which writes instructions and is called rarely so should be the stronger one, from `task_model`. `skills/dspy-optimizer-selection/reference.md:96-111` [recipe]
- **The fine-tuning path** — run a prompt optimizer until it plateaus; `program.set_lm(finetunable)`; `compile(program, trainset=...)`; compare against the *prompt-optimized* baseline. "The win is usually latency and cost per call, not accuracy." `skills/dspy-optimizer-selection/reference.md:113-123` [claim]
- **Budget discipline** — separate optimization cost from inference cost: "`Ensemble` is cheap to build and expensive forever after; `MIPROv2` is the reverse". Set `num_threads` to what the rate limit tolerates. Record the seed. Save every candidate. Run compile with `track_usage=True`: "an optimizer that silently costs ten times the alternative is a finding". `skills/dspy-optimizer-selection/SKILL.md:127-135` [pattern] → here: baseline.py
- **Reporting a compile run** — record the optimizer and every non-default argument, the DSPy version, train/dev sizes and split rule, baseline and compiled scores on the same devset, the seed, and LM usage during compile and per call afterwards. `skills/dspy-optimizer-selection/reference.md:141-152` [pattern] → here: baseline.py ledger fields

## MET

- **Evaluate's `.score` is a percentage** — `EvaluationResult(score=round(100 * ncorrect / ntotal, 2), ...)`. Measured: 3 of 4 correct gives `75.0`; a metric returning 0.5 each time gives `50.0`. The only file in the slice that encodes this is `scripts/check_dspy_surface.py:188` (`result.score == 100.0`), which the test at `tests/test_skill_correctness.py:382` requires. No skill states the scale. `SP/dspy/evaluate/evaluate.py:224` [api] (verified: behav2.py) → here: baseline.py (floors must be on 0–100)
- **Metric return types under Evaluate** — `float` and `bool` work (a bool is kept as `True` in `results`), and so does a `dspy.Prediction` with `score`. A `dict` raises `TypeError: unsupported operand type(s) for +: 'int' and 'dict'`, a `str` raises `... 'int' and 'str'`, and `None` raises `... 'int' and 'NoneType'`. `skills/dspy-evaluation-harness/SKILL.md:16`, `reference.md:45-51`, `docs/CHANGELOG.md:388,401-402` [api] (verified: behav2.py)
- **The canonical five-argument metric** — `def metric(gold, pred, trace=None, pred_name=None, pred_trace=None) -> dspy.Prediction(score=float, feedback=str)`. It is "the recommended shape for any metric that will be used with an optimizer". `pred_name` and `pred_trace` are GEPA-only and are `None` under Evaluate. "Writing the 5-argument form from the start costs nothing and keeps GEPA open as an option." `skills/dspy-evaluation-harness/reference.md:31-53`, `skills/dspy-optimizer-selection/SKILL.md:116-125` [api] (verified: GEPA enforcement, Evaluate spy) → here: pairs.py metric
- **A Prediction metric is not safe everywhere** — "`dspy.Prediction(score=..., feedback=...)` (5-arg signature) | GEPA, and everything else (the score is read)" (`skills/dspy-optimizer-selection/SKILL.md:121`) is false in two places. BootstrapFewShot-based optimizers read its truthiness. `Evaluate(save_as_json=...)` cannot serialize it. Both are in TRAP. The examples' `_score_wrapper` returns `float(out["score"])` for Evaluate and passes the raw Prediction metric only to GEPA (`examples/01-rag-qa/run.py:85-94`, `examples/02-math-reasoning/run.py:57-68`). [trap] (verified: bfs.py, ad-hoc save_as_json run) → here: pairs.py
- **A rich-feedback recipe** — compute sub-scores ("multi-axis beats scalar"), then write feedback naming the axis, predicted against expected, the likely cause, and the fix. For example: "Answer mismatch. Predicted: {pred!r}. Expected: {gold!r}. Likely cause: reasoning skipped the units/quantity in the question." Weights are explicit constants. `skills/dspy-evaluation-harness/SKILL.md:19-48,86-88` [recipe]
- **"The metric is usually more important than the program"** — "the quality of **textual feedback** in your metric determines whether optimization converges". `skills/dspy-evaluation-harness/SKILL.md:12` [claim]
- **LM-as-judge pattern** — a `Judge` signature with `question`, `gold_answer` and `pred_answer` in and `score: float` and `critique: str` out, run through `ChainOfThought`. `judge_metric` returns `dspy.Prediction(score=float(j.score), feedback=j.critique)`. Use a stronger judge LM via `dspy.context(lm=strong_lm)`. The slice has no calibration step; the book-metrics skill has one. `skills/dspy-evaluation-harness/reference.md:55-73` [pattern]
- **A metric that raises becomes a zero** — Evaluate scores an erroring example `failure_score` (0.0) and keeps going. GEPA and SIMBA do the same. The harness table maps "All scores 0.0" to "Metric raised; set `provide_traceback=True`" (`skills/dspy-evaluation-harness/reference.md:85`). `provide_traceback` only adds the traceback to the log; it does not stop the run. [trap] (verified: behav2.py) → here: lmrun.py statuses (P15: "never reached" is not "answered badly")
- **Harness anti-patterns** — scalar-only metrics under GEPA; dict returns; exact match on open-ended generation; evaluating on the trainset ("optimistic by 10–30 points", [claim]); `provide_traceback=False` ("you'll blame the LM for a KeyError"); changing the metric mid-experiment without re-baselining. `skills/dspy-evaluation-harness/SKILL.md:116-123` [claim]
- **Failure-mode table** — optimization plateaus after 1–2 rounds: the feedback is generic. Eval is slow: `num_threads=1`. Non-deterministic scores: a cache miss. Baseline beats optimized: overfitting, so use a separate valset. `skills/dspy-evaluation-harness/reference.md:81-89` [claim]
- **01-rag-qa metric** — `0.55*correctness + 0.30*citation + 0.15*conciseness`.
  - Correctness is 1.0 on a full substring match, otherwise the fraction of significant gold tokens (length ≥ 2) found *as substrings*, so "1" inside "10" counts.
  - Citation scores 1.0 if any cited id is gold, minus 0.15 per extra id, floored at 0; no citations scores 0.
  - Conciseness is 1.0 for 3–25 words, 0.3 below 3, and `max(0, 1-(n-25)/50)` above 25.
  - The feedback reveals the gold ids: "the correct one is {sorted(gold_cites)}".

  `examples/01-rag-qa/pipeline.py:83-160` [pattern] (verified: read)
- **02-math metric** — it takes the last number in the answer, with commas stripped. A match within `1e-3 + 1e-6*max(|a|,|b|)` scores 1.0; a relative error under 0.1 scores 0.2 partial credit ("so the gradient isn't all-or-nothing"); anything else scores 0. The feedback adds whether the reasoning mentioned the problem's salient numbers, "off by a small arithmetic slip" or "likely misread the problem structure" (relative error over 2.0), and the per-row `trap` hint. `examples/02-math-reasoning/pipeline.py:52-132` [pattern] (verified: dry-run metric probe: "WRONG: predicted 42, expected 26 (relative error 0.62)")
- **03-invoice metric** — `0.20 schema + 0.15 vendor + 0.15 date (exact YYYY-MM-DD) + 0.35 line-item set-F1 + 0.15 total (|Δ| ≤ 0.50)`. A description matches when ≥ 60% of the gold tokens (length ≥ 2) appear as substrings. A price matches within 0.01. An unparseable record scores 0.0. `examples/03-invoice-extraction/pipeline.py:141-243` [pattern] (verified: artifacts.py)
- **The 03 metric is lenient** — an empty but parseable record scores **0.2**. Vendor `"A"` scores **1.00** against gold "Acme Supplies Co.", because `gold_vendor.startswith(pred_vendor)`. "Acme Supplies Corporation Holdings" also passes. A record with 1 of 3 line items scores **0.83** (the dry-run probe). The baselines of 0.833 or higher reported for this task sit on that floor. `examples/03-invoice-extraction/pipeline.py:155-172` [trap] (verified: artifacts.py, dry-run)
- **Weights as constants, and a changed metric resets comparisons** — "Weight them explicitly; don't hide weights inside magic numbers — make them constants so optimizers can be told to trade off." Also: "Changing the metric mid-experiment without re-baselining — prior numbers become incomparable." `skills/dspy-evaluation-harness/SKILL.md:88,123` [pattern] → here: baseline.py (metric version in the ledger)

## DATA

- **with_inputs** — `dspy.Example(question="…", answer="…").with_inputs("question")` marks the inputs; the rest are gold labels, including extra per-row fields such as `trap`, `cite` and `gold_passages` that only the metric reads. `skills/dspy-evaluation-harness/SKILL.md:77-84`; `examples/02-math-reasoning/pipeline.py:41-49`; `examples/01-rag-qa/pipeline.py:71-80` [api]
- **Dataset sizes** — "20–50 examples is enough for GEPA's reflective loop; 100–500 for MIPROv2-style bootstrapping". "Representativeness beats size. Include edge cases, ambiguity, adversarial inputs." `skills/dspy-evaluation-harness/SKILL.md:74-77` [claim] → here: pairs.py (57 pairs)
- **Separate sets** — a trainset for optimization, a valset for the optimized program, and "A test set you *never* look at during development is gold". The workflow's rule: "If held-out test score drops, preserve that result and diagnose ... After test-informed changes, use a new untouched final holdout or label subsequent results exploratory; do not repeatedly tune against the original test set." `skills/dspy-evaluation-harness/SKILL.md:75`, `skills/dspy-advanced-workflow/SKILL.md:42,162` [pattern] → here: pairs.py folds
- **Optimizers' implicit splits (verified)** — GEPA with `valset=None` reuses the trainset. MIPROv2 with `valset=None` uses the last 80% as valset. BetterTogether takes the first 10% as valset. InferRules makes a 50/50 split, first half train. None of these shuffles the data. Sources: `SP/dspy/teleprompt/gepa/gepa.py:568-572`; `mipro_optimizer_v2.py:319-334`; `bettertogether.py:320-345`; `infer_rules.py:23-26`. [trap] (verified: source) → here: pairs.py must always pass explicit, stratified splits
- **Deduplicate train and val** — "Deduplicate `trainset` and `valset`; shared examples cause memorization." `skills/dspy-advanced-workflow/reference.md:126` [pattern]
- **The datasets behind the examples** — 01: 12 solar-system docs, 15 train, 10 val, one source doc per question. 02: 34 train, 12 val; each row has a one-line `trap` "description of the typical mistake", which the metric weaves into feedback "so the reflection LM learns *structural* fixes rather than memorizing answers". 03: 20 train, 9 val, "genuinely tricky layouts" (discount rows, seller/bill-to ambiguity, varied date formats, freight lines that are not items, tax-inclusive totals). `examples/01-rag-qa/README.md:23-27`, `examples/02-math-reasoning/README.md:27-36`, `examples/03-invoice-extraction/README.md:61` [number] (verified: `wc -l data/*`)
- **Seeds** — GEPA `seed=0`, MIPROv2 `seed=9`, SIMBA `compile(seed=0)`, `LabeledFewShot` uses `Random(0)`, InferRules' rule rollouts use `Random(0)`, and BetterTogether's `compile(seed=None)`. Record the seed with the result (`skills/dspy-optimizer-selection/SKILL.md:132`). [api] (verified: sigs.py, source)

## RLM

- **The RLM constructor (3.3.1)** — `RLM(signature, max_iters=20, max_llm_calls=50, max_output_chars=10000, verbose=False, tools=None, sub_lm=None, interpreter_factory=PythonInterpreter)`. `forward(self, interpreter=None, /, **input_args)`: a caller-owned interpreter goes to `forward` as a positional-only argument. `scripts/check_dspy_surface.py:130-157` [api] (verified: sigs.py, surface check) → here: rlm_ingest.py
- **The 3.3.0 renames** — `max_iterations` became `max_iters`, and `interpreter=<instance>` became `interpreter_factory=<callable>`, with the instance moving to `forward`. Both "hand an agent a `TypeError` on construction". The same move applied to `ProgramOfThought` and `CodeAct`. `requirements.txt:10-12`, `docs/CHANGELOG.md:11-20`, `tests/test_skill_correctness.py:31-35,492-547` [api] → here: rlm_ingest.py surface assertion
- **max_output_chars history** — "was documented as `10_000`, real default is `100_000`" on the 3.1.x line (`docs/CHANGELOG.md:404`). Then "DSPy 3.2.0's `max_output_chars=10_000` default" (`docs/CHANGELOG.md:319`). 3.3.1 is `10000` (asserted at `scripts/check_dspy_surface.py:150-153`). [api] (verified: sigs.py)
- **The interpreter contract** — a `CodeInterpreter` subclass owes `start()`, `execute(code, variables=None)`, `shutdown()` and a mutable `tools` mapping, "not just `execute(code) -> str`". The working import paths are `dspy.primitives.*`, plus `dspy.PythonInterpreter` on 3.3.x only. `docs/CHANGELOG.md:37-43` [api]
- **Deno** — "`dspy.RLM` needs Deno for its default Pyodide/WASM interpreter" (`CLAUDE.md:74`), and ProgramOfThought "generates & runs Python (needs Deno)" (`skills/dspy-fundamentals/SKILL.md:47`). [claim]
- **The routing threshold** — "Context >100k tokens → `dspy-rlm-module`" (`skills/dspy-fundamentals/SKILL.md:117`, `docs/usage.md:10`). [claim]

## RAG

- **The retriever is an injected argument** — "`dspy.Retrieve` and `dspy.ColBERTv2` still exist and read a globally configured `rm=` ... a global retriever cannot be swapped per test, per tenant, or per evaluation split." The contract: "Anything callable that takes a query string and returns an object with `.passages` works." `skills/dspy-retrieval/SKILL.md:30-64`, `reference.md:25-45` [pattern] → here: graphrag.py (a stub retriever for tests)
- **dspy.Embeddings (verified)** — `Embeddings(corpus, embedder, k=5, callbacks=None, cache=False, brute_force_threshold=20000, normalize=True)`. At or above the threshold it builds a FAISS `IndexIVFPQ` over an `IndexFlatL2` quantizer, searches `k*10` candidates, then re-ranks exactly. If FAISS is missing: `ImportError: Please \`pip install faiss-cpu\` or increase \`brute_force_threshold\` to avoid FAISS.` It returns `Prediction(passages, indices)`; `EmbeddingsWithScores` adds `scores`. `skills/dspy-retrieval/SKILL.md:66-87`, `reference.md:12-23,61-72`, `SP/dspy/retrievers/embeddings.py:28-107,242-261` [api] (verified: sigs.py, source)
- **Persisting an index** — `search.save(path)` writes `config.json` (k, normalize, the corpus, `has_faiss_index`), `corpus_embeddings.npy` and, if built, `faiss_index.bin`. `dspy.Embeddings.from_saved(path, embedder)` is a **classmethod**; the reference's "# staticmethod" (`reference.md:18`) is wrong. "Persist whenever embedding the corpus costs more than loading it — which is almost always after the first thousand passages" is a [claim]. `SP/dspy/retrievers/embeddings.py:143-210` [api] (verified: getattr_static, source)
- **An index manifest** — persist `MANIFEST.json` (embedding model id, chunk-rule version, corpus hash, build time) beside the index, and compare it on load: "Mismatch means rebuild — never 'probably fine'". "The vectors from two models are not comparable, and nothing raises an error if you mix them." `skills/dspy-retrieval/reference.md:56-59,87-99` [pattern]
- **Chunking rules** — one idea per passage; 100–500 words; 10–20% overlap; prefix each chunk with its title or section; chunk deterministically and version the rule. `skills/dspy-retrieval/reference.md:74-85` [claim]
- **Multi-hop** — generate the next query from the context so far, deduplicate between hops with `list(dict.fromkeys(...))` (order-preserving), and cap at 2–3 hops. Log the query per hop: "A degenerate second query that merely restates the first is the most common multi-hop failure". "Optimize the query generator with the retrieval metric, not the answer metric." `skills/dspy-retrieval/SKILL.md:96-123`, `reference.md:122-127` [pattern]
- **Score retrieval separately** — `recall_at_k` is |got ∩ want| / |want|, with feedback naming up to 2 missed passages. Run `dspy.Evaluate` with this metric and with the answer metric. The diagnosis: low/low points to corpus, chunking or embedding; high recall with low answers points to the generator or the context field type; low recall with high answers means "answering from parameters ... check for leakage". `skills/dspy-retrieval/SKILL.md:125-149`, `example_retrieval.py:103-125` [pattern] (verified: dry-run) → here: graphrag.py bench (recall@8)
- **Other retrieval metrics** — recall@k when all gold passages are needed; MRR when one passage suffices and its rank matters; precision@k when the context budget is tight; hit rate as a coarse smoke test. `skills/dspy-retrieval/reference.md:113-120` [claim]
- **Return the context** — "Returning `context` alongside `answer` is not decoration — it is what lets a metric check grounding". Raising `k` to fix low recall "raises cost and dilutes context. Fix the chunking first." `skills/dspy-retrieval/SKILL.md:58-60,155` [pattern]
- **Local embedder** — `dspy.Embedder(SentenceTransformer("all-MiniLM-L6-v2").encode)`; it must accept `list[str]` and return a 2D array. `skills/dspy-retrieval/SKILL.md:89-94` [recipe]
- **Legacy retrievers** — `dspy.Retrieve(k=3, callbacks=None)` and `dspy.ColBERTv2(url='http://0.0.0.0', port=None, post_requests=False)`. There is no deprecation warning in their source. `skills/dspy-retrieval/reference.md:129-135` [api] (verified: sigs.py, grep)
- **01-rag-qa retriever** — `rank_bm25.BM25Okapi` over tokens matching `[a-zA-Z0-9°]+` from title plus text, k=3. Context lines are formatted `[{id}] {title}: {text}`. The output is `citations: list[str]`. The dry-run probe retrieved `['mars', 'saturn', 'earth']` for the Mars question. `examples/01-rag-qa/pipeline.py:15-64` [number] (verified: dry-run)

## AGENT

- **ReAct / CodeAct** — `dspy.ReAct(signature, tools: list[Callable], max_iters=20)` and `dspy.CodeAct(signature, tools, max_iters=5, interpreter_factory=PythonInterpreter)`. `skills/dspy-fundamentals/reference.md:69` [api] (verified: sigs.py)
- **The CLI's plan mode is not a tool sandbox** — `claude -p --permission-mode plan` means "the model may not run tools; text in, text out". The anti-pattern: "Treating the CLI's permission mode as a tool sandbox for agents; use `plan` and keep the model text-only." `skills/dspy-local-runtime/reference.md:21`, `SKILL.md:117` [claim]
- **History inputs in GEPA reflection** — when a predictor input is a `dspy.History`, GEPA's reflective dataset renders its messages as an indexed JSON block under `"Context"` instead of the raw field. `SP/dspy/teleprompt/gepa/gepa_utils.py:374-384` [api] (verified: source)

## PROD

- **Save formats** — state-only JSON is the default: "You supply the class, so nothing executes on load." A whole-program save uses cloudpickle: "Loading one executes code from the artifact. Use it only for artifacts your own pipeline produced". For a file from elsewhere: state JSON "with review", pickle "never". `skills/dspy-production/SKILL.md:25-44`, `reference.md:32-48` [pattern] → here: pairs.py artifacts
- **Cache hardening** — `dspy.configure_cache(restrict_pickle=True)`, with `safe_types=[...]` for your own types, or `enable_disk_cache=False` for ephemeral deployments. "A shared disk cache across tenants is a data-leak path, not an optimization." Use a project-local `disk_cache_dir` (`.cache/dspy`) in CI. `skills/dspy-production/SKILL.md:46-63` [recipe] (verified: API)
- **Cached calls cost nothing and say so** — "Cached calls report no new usage — which is why a benchmark run with a warm cache looks free and tells you nothing about production cost. Measure cost with the cache disabled at least once." Verified in source (`SP/dspy/clients/base_lm.py:294`). Also: "Optimizer runs warm the cache heavily. The second compile of the same program is not evidence that it got faster." `skills/dspy-production/SKILL.md:73-75`, `reference.md:67-71` [api] (verified: source) → here: lmrun.py `cache=False` (P18)
- **Cache replays in the examples** — `optimized-eval 0.0s` in 01 (`examples/01-rag-qa/results.md:11`) and in 02 (`examples/02-math-reasoning/results.md:11`); a historical 02 baseline of `0.2s` and eval of `0.1s` (`examples/02-math-reasoning/version_comparison.json`). With `cache=True` (`examples/common/config.py:70,87`), the post-compile evaluation replays GEPA's own valset calls. [number] (verified: read)
- **Async** — built-in modules implement `acall()`; custom modules implement `aforward()` next to `forward()`; `dspy.asyncify(program)` "moves work to a thread; it does not make the program concurrent"; `async_max_workers` bounds the pool. "Do not call blocking I/O inside `aforward()`." Concurrency above the rate limit "converts directly into 429s and retries". `skills/dspy-production/SKILL.md:77-92`, `reference.md:123-131` [claim]
- **Batch** — `dspy.Parallel(num_threads=8, return_failed_examples=True)([(program, {"question": q}) for q in questions])`. For evaluation runs prefer `dspy.Evaluate`. `skills/dspy-production/reference.md:133-144` [api] (verified: signature)
- **Streaming** — `dspy.streamify(dspy.Predict("question -> answer"), stream_listeners=[dspy.streaming.StreamListener(signature_field_name="answer")])` with `async for chunk in stream(...)`. Set `allow_reuse=True` for looped modules such as ReAct, "or you get only the first occurrence" ([claim]). A cache hit yields only the final Prediction, so "test the streaming path with the cache off". `skills/dspy-production/SKILL.md:94-111` [api] (verified: source for the cache behaviour)
- **Callbacks run on the call path** — "Callbacks run **synchronously inside the call path**. Anything slow in `on_lm_end` is added latency on every request. Buffer and flush elsewhere; never log to a remote sink inline." Sample at high volume; decide sampling in `on_lm_start` so start and end stay paired; keep state per `call_id` and `pop` it on end "so a failed call cannot leak the entry"; redact before logging. `skills/dspy-production/SKILL.md:128-160`, `reference.md:97-107`, `example_production.py:44-82` [pattern] → here: lmrun.py record writer
- **Callbacks and optimizers** — "Exceptions in a callback surface in the call path; guard your own handlers." Callbacks "do not see inside optimizer internals — use MLflow's compile traces for that". `skills/dspy-production/reference.md:103-107` [claim]
- **MLflow** — `mlflow.dspy.autolog(log_traces=True, log_traces_from_compile=True, log_traces_from_eval=True, log_compiles=True, log_evals=True)`: "everything on in development and CI; inference traces only, sampled, in production". `skills/dspy-production/SKILL.md:162-173`, `reference.md:146-159` [claim] (mlflow not installed)
- **W&B via GEPA** — `dspy.GEPA(..., use_wandb=True, wandb_api_key=..., wandb_init_kwargs=...)`; the key otherwise comes from `WANDB_API_KEY`. `skills/dspy-evaluation-harness/reference.md:78`, `skills/dspy-gepa-optimizer/SKILL.md:119-121` [api] (verified: signature)
- **The pre-ship checklist** — pin the DSPy version; state JSON; `restrict_pickle=True` and no cache shared across tenants; measure once with the cache off; load-test async, streaming and batch separately; callbacks that sample, buffer and redact; keep the evaluation harness runnable against the deployed artifact. `skills/dspy-production/SKILL.md:175-183` [pattern]
- **What to record with an artifact** — the DSPy version; optimizer, arguments and seed; the devset score and devset identity; the metric version; the LM and provider "including model version"; the save format. "Without this, 'the model got worse' is unanswerable." `skills/dspy-production/reference.md:161-172` [pattern] → here: baseline.py
- **Local runtime: a BaseLM over `claude -p`** — one process per request: `claude -p --output-format json --permission-mode plan --no-session-persistence [--model alias] [--system-prompt …]`.
  - The JSON carries `result`, `usage` (`input_tokens`, `output_tokens`, `cache_read_input_tokens`), `is_error`, `session_id` and `total_cost_usd`.
  - `parse_result` maps `input_tokens` to `prompt_tokens` and raises on `is_error`.
  - System messages are joined into `--system-prompt`, and other turns are rendered `role: content`.

  `skills/dspy-local-runtime/SKILL.md:27-57`, `reference.md:11-42`, `example_local_runtime.py:37-64` [pattern] (verified: dry-run)
- **Local runtime: kwargs the CLI cannot honour** — `temperature`, `max_tokens` and `rollout_id` are stripped silently in `__init__` and `copy()`, "Strip, never error, on `rollout_id` and `temperature` in `copy()`", because BestOfN, Refine and TetraFrame call `lm.copy(rollout_id=…, temperature=…)`. `n>1` raises `ValueError`. `cache=True` raises `ValueError("ClaudeLM cannot cache: the CLI has no deterministic sampling to cache against")`. In the upstream file, `tools`, `tool_choice`, `response_format` and `logprobs` raise. `skills/dspy-local-runtime/reference.md:44-51`, `example_local_runtime.py:84-106` [pattern] (verified: dry-run)
- **Local runtime: choosing a backend** — `DSPY_LOCAL_BACKEND` is `api`, `claude-cli` or `auto` (the default). In `auto`, `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` selects the API; otherwise `claude` on PATH selects the CLI; otherwise the API, so that it "fail[s] loudly at first call". Model ids differ between the two (`anthropic/claude-haiku-4-5` against `claude/haiku`); warn when the inactive set is overridden. `skills/dspy-local-runtime/SKILL.md:64-78`, `example_local_runtime.py:67-76` [pattern] (verified: dry-run)
- **Local runtime budget** — one `Predict` takes about 5–10 s; `Evaluate` on 20 examples takes 2–4 min with `num_threads=1` ("the processes contend for the same session"); `GEPA(auto="light")` on 20 train / 10 val takes "a few hundred calls". "Budget in calls, not tokens." Upstream isolates `HOME`, copying only the credentials in, and `probe_claude_runtime()` reports `ready | missing_cli | missing_credentials`. `skills/dspy-local-runtime/SKILL.md:80-110`, `reference.md:65-92` [claim]
- **The examples' LM configuration** — task LM `temperature=0.0, max_tokens=2000, cache=True`; reflection LM `temperature=1.0, max_tokens=8000, cache=True`, wired to OpenRouter (`api_base https://openrouter.ai/api/v1`). `num_retries` defaults to 12, overridable with `DSPY_EXAMPLE_NUM_RETRIES` (the reproduction commands use 8). `num_threads` comes from `DSPY_EXAMPLE_NUM_THREADS`. `configure_dspy` sets `track_usage=True`. The defaults are the free `openrouter/z-ai/glm-4.5-air:free` and `openrouter/nvidia/nemotron-3-super-120b-a12b:free`. `examples/common/config.py:19-109` [recipe]
- **Free-tier limits** — "OpenRouter's free-tier daily quota (2000 req/day) was exhausted at iteration 24 of ~25" in the 03 run; `qwen3-1.7b` returned "404: No endpoints found". Cheap paid fallbacks cost about $0.10–$0.15 per M tokens. `examples/03-invoice-extraction/README.md:15,21,36`, `examples/README.md:59-62` [number]
- **uv resolving an old DSPy** — `UV_EXCLUDE_NEWER=7 days` set globally made `uv run --with dspy` resolve DSPy 3.1.3 while 3.2 was on PyPI. The fix is `env -u UV_EXCLUDE_NEWER uv run --with dspy==3.3.1 ...`. `docs/installation.md:108-118`, `CLAUDE.md:34-38` [trap]
- **Secrets and cache directory** — "Do not commit `.env`, API keys, DSPy caches ... prefer `DSPY_CACHEDIR=.cache/dspy` for reproducible local runs" (`AGENTS.md:31`). `.gitignore` ignores `gepa_logs/`, `.cache/` and `.env*` except `.env.example`. [pattern]

## TEST

- **check_dspy_surface.py** —
  - It asserts `dspy.__version__ == --expected-version` (default `3.3.1`).
  - It checks parameter sets for GEPA (plus `candidate_selection_strategy` default `"pareto"`), `BetterTogether` (`**kwargs` present; `compile` has `student`, `trainset`, `valset`, `strategy`, `optimizer_compile_args`), `Evaluate`, `LM`, `SIMBA`, `Embedder.__call__`, `configure_cache`, `Refine`/`BestOfN`, the RLM constructor (`max_iterations` absent, `max_output_chars == 10_000`, `forward` has `interpreter`), and `ProgramOfThought`/`CodeAct`.
  - It checks that `Reasoning`, `File`, `Code` and `PythonInterpreter` exist.
  - It constructs a real GEPA with a 5-argument metric, and runs one `dspy.Evaluate` with a callable `_EchoModule`, requiring `result.score == 100.0` and a `Prediction` preserved in `results[0][2]`.
  - It prints `FAIL: ...` and exits 1 on any assertion.

  `scripts/check_dspy_surface.py:1-203` [pattern] (verified: passes on 3.3.1) → here: check_dspy_surface.py
- **What the surface check does not cover** — it has no probe for `dspy.load`/`allow_pickle`, `Evaluate(save_as_json=...)` with a Prediction metric, `BootstrapFewShot` with a Prediction metric, GEPA budget exclusivity, `DspyGEPAResult` field names, MIPROv2's optuna/compile rules, KNNFewShot's construction cost, callback `outputs` shape, or `Parallel`/`streamify`. Some of these are asserted by example dry-runs, which only check signatures. Every live-path defect in TRAP is outside what it checks. [trap] (verified: read)
- **Examples that assert their own surface** — `assert_api_surface()` in three examples fails loudly on drift:
  - optimizer-selection: BootstrapRS alias; LabeledFewShot has `k` and no metric; SIMBA keyword-only with seed on `compile`; `Ensemble.compile(programs)`; KNN trainset in the constructor; BetterTogether `**optimizers` (`example_optimizer_selection.py:102-124`);
  - production: `configure_cache` defaults, `save_program=False` default, `StreamListener.allow_reuse=False`, `inspect_history` `n=1`, 7 callback hooks, `GLOBAL_HISTORY` a list (`example_production.py:108-135`);
  - retrieval: Embeddings defaults, `save`/`from_saved`, `EmbeddingsWithScores` (`example_retrieval.py:128-139`).

  [pattern] (verified: dry-runs pass) → here: check_dspy_surface.py
- **The dry-run convention** — every `example_*.py` takes `--dry-run`, which "exercises Signature/Module construction without calling an LM". A stub `dspy.LM(...)` is allowed because construction makes no network call. The 11 slice dry-runs take 0.04–2.0 s each and write no files. `CLAUDE.md:17-18,57`, `docs/usage.md:166-266` [pattern] (verified: ran all) → here: P5
- **The pytest suite passes on 633 tests** — `test_skill_metadata.py` (frontmatter spec), `test_manifests.py` (plugin/marketplace JSON, versions agree in plugin.json, marketplace.json and README `## Version`, strict JSON), `test_examples_parse.py` (every example, script and scaffold parses; every scaffold is named in `docs/`), and `test_skill_correctness.py` (ten regression rules plus doc-alignment tests). `tests/*` [number] (verified: 633 passed in 0.87s)
- **The regression rules and their provenance** — each rule exists because a mistake shipped:
  - 1: `.overall_score` should be `.score`.
  - 2: dict metrics, caught in code, prose and multi-line dict literals.
  - 3: a stale RLM `max_output_chars` of 100_000.
  - 4: BetterTogether's `prompt_optimizer=`/`weight_optimizer=`.
  - 5: every skill ships an example with `--dry-run`.
  - 6: `docs/usage.md` lists every example.
  - 7: the install doc mentions 3.3.1, `OPENROUTER_API_KEY`, `UV_EXCLUDE_NEWER` and the surface script.
  - 8: no "all artifacts are 3.1.3" regressions.
  - 9: the RAG example's numbers agree across 5 docs.
  - 10: stale RLM constructor names.

  "These rules exist because we shipped subtly wrong teaching material once and caught it in external review." `tests/test_skill_correctness.py:1-40` [pattern] → here: PRINCIPLES catalogue
- **Marker-word allowlist** — a line may *mention* a banned pattern if it also contains one of `crashes, anti-pattern, wrong, bad, do not, don't, breaks, not a dict, dict), typeerror, instead of, enforces`. Rule 10 also allows migration lines (`3.2`, `renamed`, `re-introduced`, `before dspy 3.3`, or a line carrying the new name). The CHANGELOG is excluded because "linting it for anti-patterns would be a tautology". `tests/test_skill_correctness.py:56-58,82-100,495-515` [pattern] → here: state.py/quotes.py-style checkers
- **Past mistakes pinned as negative asserts** — `'"random"' not in reference` (unsupported `component_selector`); `"dspy.Prediction | str" not in reference`; `"float | dict" not in text`; `"dspy==3.2.1" not in combined`. `tests/test_skill_correctness.py:338-373` [pattern]
- **A guard proven by breaking the code** — "The Rule 10 guard was verified by reintroducing the `max_iterations` rename: it fails, and passes again once reverted." `docs/CHANGELOG.md:99-100` [pattern] → here: selftest.py (a check proven able to fail)
- **Tests that pin committed numbers** — `test_rag_qa_results_match_clean_3_2_comparison` requires `results.json` to match the `clean_dspy_3_2_0` run and the formatted baseline, optimized and delta values to appear in 5 docs. `test_version_comparisons_do_not_commit_machine_temp_paths` rejects `/tmp/dspy-refresh`. `tests/test_skill_correctness.py:424-489` [pattern] → here: state.py `--prose`
- **The dry-run test only checks for a string** — `test_example_has_dry_run` and `test_every_skill_has_example` check that the string `"--dry-run"` appears in the source; nothing in pytest runs a dry-run. "633 passed" says nothing about whether the examples run. `tests/test_examples_parse.py:38-44`, `tests/test_skill_correctness.py:268-280` [trap] (verified: read) → here: selftests.py runs, not greps
- **The frontmatter parser** — it is hand-rolled, not YAML: a `key: value` line at column 0 starts a field. A separate guard, `test_frontmatter_plain_scalars_are_yaml_safe`, catches inline plain scalars containing `": "` that strict YAML parsers such as `npx skills` reject. `tests/test_skill_metadata.py:47-67,128-154` [pattern] → here: check_skills.py
- **dspy.utils.DummyLM runs modules offline (not used by the pack)** — `DummyLM([{"answer": "4"}])` answers `Predict`, `ChainOfThought`, `Evaluate` and `BootstrapFewShot` offline. It reproduced every live-path defect found here: the save_as_json TypeError, BootstrapFewShot's truthiness, and callback outputs. The pack's dry-runs only *construct* objects, so they could not. [pattern] (verified: bfs.py, usage_cb.py, ad-hoc runs) → here: lm_fixture.py
- **install.sh** — flags `--claude-only`, `--codex-only`, `--copy`, `--link`, `--uninstall`, `--verify`, `--dry-run`. Skills are discovered as `skills/*/SKILL.md`; each target is `rm -rf`'d before relinking; `--verify` checks symlink targets or copies for `SKILL.md` and exits with the count of failures. `scripts/install.sh:1-154` [api]
- **Test counts per release** — 34 tests (v0.1.0), 87 → 105 (v0.2.2), 108, 114 (v0.2.3), 249 (v0.7.0), 525 → 633 (v0.11.0). `docs/CHANGELOG.md:95,180,264,275,296,367` [number]

## PAT

- **Baseline before any optimizer** — "Step 0, not optional: the baseline ... Without that number, no optimizer result means anything." "Always baseline before optimizing — no baseline, no claim." `skills/dspy-optimizer-selection/SKILL.md:31-38`, `skills/dspy-advanced-workflow/SKILL.md:160` [pattern] → here: baseline.py
- **The seven-step build loop** — spec, program, data, rich metric, baseline, optimize, export & deploy. "Stop at a validated baseline for a prototype; optimizer runs require an appropriate authorized budget and evidence of need. Exporting a local artifact does not authorize deployment." `skills/dspy-advanced-workflow/SKILL.md:9-99` [pattern] → here: the approval gate in lmrun.py
- **The self-optimizing loop order** — reflect, then GEPA (with the slop score folded in), then an autodialectics gate ("promote the challenger only if score is up, slop is not, canaries pass"), then deep-refine, then rlm-workflow. Clarify runs at authority boundaries, TetraFrame before contested decisions, adversarial review "with a reviewer LM that is asserted to differ from the writer". "Every loop is dry-run-first and keeps a human approval on writes." `skills/dspy-advanced-workflow/SKILL.md:165-181` [claim]
- **One source of truth per API** — skills from the source pack that overlap are not ported: "Porting them would have created two sources of truth for the same API". `skills/dspy-optimizer-selection/reference.md:154-159`; also `CLAUDE.md:69`: "If one SKILL.md has a wrong import path, others likely do too; check the sibling skills". [pattern]
- **Honest artifacts** — example 03 keeps its completed 3.1.3 artifact rather than promoting an interrupted run, and says why. Committed comparisons are "measurements, not claims about the current API, and rewriting their labels would have made them lie" (`docs/CHANGELOG.md:68-72`). The README must not imply the historical artifacts were rerun (`tests/test_skill_correctness.py:326-335`). [pattern] → here: baseline.py (vetoed rows)
- **Routers as functions** — the book router is a table plus `find()` (alias first, then substring) with asserted counts: 57 notebooks, 11 chapters, every alias resolves (`skills/dspy-context-engineering-book/example_book_map.py:75-123`). The dspytools skill encodes "which service does this command need" as a dict (`skills/dspy-tools-cli/example_tools_cli.py:22-61`). [pattern]
- **Where a notebook and the pack disagree** — "Where a notebook and a skill disagree on an API, prefer the skill ... A notebook was accurate when it was authored." Notebooks hard-code retired models, and the `dspy.LM(...)` line is the usual edit. `skills/dspy-context-engineering-book/reference.md:44-53` [claim; see TRAP on the "asserted" overclaim]
- **What GEPA learns is visible, and it memorizes** — the optimized instructions are 3,153 characters (01), 2,351 (02) and 5,921 (03). Measured: 4 of 15 training gold answers in 01 (`3474 km`, `2100 km/h`, `2006`, `464°C`) appear verbatim in the learned instruction, and 0 of 10 valset answers do. In 02, trainset values `210`, `3.5` and `14.29` appear, and 0 of 12 valset answers. The 03 instruction dictates a Python-repr output format. `examples/*/optimized_program.json` [number] (verified: my script) → here: read the instruction diff before accepting a GEPA result

## SKILL

- **Honoured frontmatter fields** — `name` (required, kebab-case, ≤64, equal to the directory name), `description` (required; combined with `when_to_use` it must stay ≤1536 characters; tests also require ≥30), `when_to_use`, `argument-hint`, `disable-model-invocation`, `user-invocable`, `allowed-tools`, `model`, `effort`, `context`, `agent`, `hooks`, `paths`, `shell`. `CLAUDE.md:44-49`, `tests/test_skill_metadata.py:25-44,181-193` [api] → here: check_skills.py
- **Forbidden fields** — `triggers`, `version`, `dspy-compatibility` and `dspy-version` "are silently ignored by the harness and are rejected by `tests/test_skill_metadata.py`. Version lives in `.claude-plugin/plugin.json`." `CLAUDE.md:51`, `tests/test_skill_metadata.py:41` [api] → here: check_skills.py
- **The file must be named `SKILL.md`** — "`skill.md` or `Skill.md` won't be loaded by Claude Code". `CLAUDE.md:53,75`, `tests/test_skill_metadata.py:93-103` [api]
- **Strict-YAML breakage happened** — "Fixed `dspy-evaluation-harness` frontmatter so strict YAML parsers used by `npx skills` discover all five skills": an inline scalar containing `": "` made the skill vanish. `docs/CHANGELOG.md:307-308` [trap] → here: check_skills.py
- **Progressive disclosure** — keep `SKILL.md` under about 500 lines, put deep API detail in `reference.md`, and ship a runnable `example_*.py --dry-run`. `CLAUDE.md:55-57`, `AGENTS.md:19` [pattern]
- **Selection happens on the description** — "Claude Code / Codex auto-select skills by matching the `description` field." Explicit invocation is `/dspy-gepa-optimizer` in Claude Code ("if `user-invocable` is true, which it is by default") and `$dspy-gepa-optimizer` in Codex. `docs/usage.md:42,118-123` [claim] → here: job 4 (the description is the optimizable text)
- **Install locations** — `~/.claude/skills/` for Claude Code and `~/.agents/skills/` for Codex. "Codex also scans `.agents/skills/` walking up from cwd to repo root". A symlink install means "a broken edit immediately breaks the agent's skill invocation". `docs/installation.md:33-68`, `CLAUDE.md:77` [claim]
- **A text artifact that is not a DSPy program** — the matrix's last row: "The artifact is text but not a DSPy program | GEPA over a custom adapter | a metric on that artifact". There is no recipe for it in this slice; the book-coding-agents skill carries `optimize_anything`. `skills/dspy-optimizer-selection/SKILL.md:57` [claim] → here: job 4
- **Grounding rule** — "Every DSPy API claim must be verifiable against https://dspy.ai/ for DSPy 3.3.x. If you update a signature or parameter, re-check the docs and update `reference.md` in lockstep." `CLAUDE.md:59-61` [pattern]

## TRAP

- **The CI gate cannot fail** — `assert result.score >= 0.75, f"Regression: {result.score:.3f}"` (`skills/dspy-evaluation-harness/SKILL.md:104`), but `.score` is 0–100. It passes for any score of 0.75% or more. The same scale confusion is in the README table, which puts 80.47 (a percent) beside 0.833 (a GEPA 0–1 aggregate), explained only at `examples/03-invoice-extraction/README.md:31` ("0.773 (reported as 77.31%)"). [trap] (verified: behav2.py) → here: baseline.py floor units
- **Every taught `dspy.load(dir)` raises on 3.3.1** — `ValueError: Loading with pickle is not allowed ...` at `skills/dspy-fundamentals/SKILL.md:81`, `skills/dspy-production/SKILL.md:38` and `reference.md:15`, `skills/dspy-advanced-workflow/SKILL.md:94` and `reference.md:84`. Fix: `dspy.load(dir, allow_pickle=True)`, only for trusted artifacts. `check_dspy_surface.py` never tests it, and the production example asserts only `hasattr(dspy, "load")` (`example_production.py:134-135`). [trap] (verified: behav1.py)
- **save_as_json with a Prediction metric crashes after the run** — `TypeError: Object of type Prediction is not JSON serializable`, raised after every LM call of the evaluation has been spent. The pack teaches exactly this combination at `skills/dspy-evaluation-harness/SKILL.md:53-63`, `skills/dspy-advanced-workflow/SKILL.md:51-54,134-136`, and `skills/dspy-advanced-workflow/example_pipeline.py:113-120` (live path). Reproducing the live path with DummyLM crashed at the baseline step. So **the README's headline live command** (`README.md:124-126`, `CLAUDE.md:29-31`: `example_pipeline.py --auto light`) dies on 3.3.1 before GEPA starts. The examples under `examples/` avoid it only because `_score_wrapper` returns floats. [trap] (verified: ad-hoc Evaluate run and DummyLM reproduction)
- **save_as_json does not create directories** — `open(save_as_json, "w")`, so `"eval_runs/baseline.json"` or `"runs/baseline.json"` raises `FileNotFoundError` after the run unless the directory exists. `example_pipeline.py:121` creates `runs/`; the SKILL snippets do not. `SP/dspy/evaluate/evaluate.py:210-221` [trap] (verified)
- **BootstrapFewShot reads a Prediction metric by truthiness** — `bool(dspy.Prediction(score=0.0, feedback="x"))` is `True`. With `metric_threshold=None`, BootstrapFewShot keeps every trace as a successful demo. Measured: all answers wrong, a Prediction metric keeps **4 of 4 wrong demos**; a float metric keeps 0; the same Prediction metric with `metric_threshold=0.5` keeps 0.
  - Affected: `BootstrapFewShot`, `BootstrapRS`, `KNNFewShot`, MIPROv2's demo bootstrapping, `InferRules` (a subclass), and BetterTogether's `bootstrap` stage.
  - Contradicts `skills/dspy-optimizer-selection/SKILL.md:121` ("everything else (the score is read)").
  - Fix: pass `metric_threshold`, or a float-returning wrapper, to every non-GEPA rung.
  - `SP/dspy/teleprompt/bootstrap.py:204-212` [trap] (verified: bfs.py) → here: **pairs.py ladder (LabeledFewShot → BootstrapFewShot → InferRules)**
- **BetterTogether without a strategy raises** — `skills/dspy-optimizer-selection/SKILL.md:88-92` and `reference.md:127-139` teach `optimizer.compile(program, trainset=trainset)` with named `bootstrap=`/`gepa=` and say "The keyword *names* are yours; the order is the run order", and "runs them in the order given" (`SKILL.md:113-114`). On 3.3.1 this raises `ValueError: Strategy contains invalid optimizer keys: ['p', 'w', 'p']`. The sibling skill states the correct rule. [trap] (verified: bt.py)
- **BetterTogether swallows step failures** — an exception in any step is logged as ERROR, "Stopping optimization early. Returning best program found so far". `compile` returns normally, with `flag_compilation_error_occurred=True` on the program. Check the flag. `SP/dspy/teleprompt/bettertogether.py:470-503` [trap] (verified: source)
- **GEPA with both `auto` and `max_metric_calls`** — `skills/dspy-local-runtime/SKILL.md:95`: `dspy.GEPA(metric=my_metric, reflection_lm=reflection_lm, auto="light", max_metric_calls=300)` raises `AssertionError: Exactly one of max_metric_calls, max_full_evals, auto must be set.` The table row "run in the background, set `max_metric_calls`" (`SKILL.md:88`) invites the same mistake. [trap] (verified: gepa1.py)
- **Both GEPA budget tables are wrong** — the GEPA skill's "light ~20–40 full evals / medium ~80–150 / heavy ~300–600" and "Each 'full eval' ≈ `len(valset)` metric calls" (`skills/dspy-gepa-optimizer/SKILL.md:87-95`), and the workflow's "light ~50 metric calls / medium ~200 / heavy ~500+" (`skills/dspy-advanced-workflow/reference.md:98-100`), match neither the formula nor each other. For 1 predictor and V=10 the real figures are 420, 740 and 1,105 metric calls, which is 16.8, 29.6 and 44.2 full evaluations in DSPy's own train+val sense for 15 train examples. Budget from `auto_budget`. [trap] (verified: gepa1.py)
- **detailed_results attribute names are wrong** — `candidate_programs` and `reflection_traces` (`skills/dspy-gepa-optimizer/reference.md:59-61`) raise `AttributeError`. `val_aggregate_scores` is per *candidate*, not "Pareto frontier scores" (`reference.md:58`, `SKILL.md:50-51` prints `sorted(pareto)[:5]` as "Pareto frontier"). DSPy's own class docstring repeats the mislabel ("pareto_frontier is a list of scores, one for each task in the batch", `SP/dspy/teleprompt/gepa/gepa.py:242-244`), and its `DspyGEPAResult` docstring contradicts it. [trap] (verified: source)
- **The documented log_dir layout is wrong** — `candidates/<id>.json`, `scores.jsonl` and `reflections/` (`skills/dspy-gepa-optimizer/reference.md:93`) are not what gepa 0.1.4 writes; see the OPT item on log_dir. [trap] (verified: source)
- **The instruction_proposer signature is wrong** — `(program, reflections, trace) -> str` (`skills/dspy-gepa-optimizer/reference.md:85`); the real one is `(candidate, reflective_dataset, components_to_update) -> dict[str, str]`. [trap] (verified: source)
- **SIMBA with its default bsize on a small trainset** — the trainset-size table recommends SIMBA for 10–50 examples (`skills/dspy-optimizer-selection/reference.md:70`), and the selection matrix gives it "scalar metric, mini-batches" (`SKILL.md:53`). SIMBA asserts `len(trainset) >= bsize` with default 32. It also needs numpy. [trap] (verified: source) → here: pairs.py (57 pairs: a 2-fold training split has 28 examples, below 32, so pass `bsize` ≤ the training-fold size)
- **Errors become scores** — a metric exception becomes `failure_score` in `Evaluate` and in GEPA's evaluation, and SIMBA logs a warning and scores 0.0. BetterTogether continues after a failed step. `Evaluate` silently accepts misspelled keyword arguments (measured: `num_thread=64`, `dispaly_table=5` and `return_all_scores=True` are accepted and ignored; only `return_outputs` raises). None of these yields "could not score". [trap] (verified: behav2.py, ad-hoc run) → here: lmrun.py statuses (P15, P23)
- **MIPROv2 without optuna** — `requirements-extras.txt:12-13` claims a non-Bayesian fallback. 3.3.1 raises `ImportError` at step 3, after paying for steps 1 and 2. [trap] (verified: source)
- **KNNFewShot construction calls the embedder** — it embeds the whole trainset in `__init__`. "Constructing is free" holds for `dspy.LM`, not for `KNNFewShot`, and a dry-run must not build one with a hosted embedder. [trap] (verified: source)
- **ClaudeLM double-counts usage** — `example_local_runtime.py:113-114` calls `dspy.settings.usage_tracker.add_usage(...)` inside `forward`, and `BaseLM` adds the same `usage` again. Measured with a patched `subprocess.run` and a canned 12/1-token response: `get_lm_usage()` reported `{'prompt_tokens': 24, 'completion_tokens': 2, 'total_tokens': 26}`. The docs call the upstream "records usage on DSPy's tracker" a feature (`SKILL.md:62`). [trap] (verified: usage_cb.py) → here: lm_fixture.py
- **The production UsageCallback counts 0 tokens against a real LM** — `on_lm_end` reads `outputs.get("usage")` when `outputs` is a dict (`skills/dspy-production/example_production.py:66`). DSPy passes the LM's **list of completion strings**, for example `['[[ ## answer ## ]]\n4']`, though the hook is annotated `dict[str, Any] | None`. Measured against DummyLM: `total_tokens: 0`. The dry-run passes only because it feeds invented `{"usage": {...}}` dicts (`example_production.py:147-151`), a fixture that real calls never produce. The SKILL snippet (`skills/dspy-production/SKILL.md:131-143`) also lacks `__init__`, where `started`, `errors` and `latencies` would be set, and `import time`. [trap] (verified: usage_cb.py) → here: lm_fixture.py realism
- **Stale and overclaimed statements** —
  - `docs/installation.md:3` says "All of them install the same 14 skills"; there are 32.
  - `README.md:94` says the examples "exercise every skill"; they exercise 3 (`examples/README.md:21-27`).
  - `docs/usage.md:38-40` has a blank line that splits the skills table.
  - The dspytools "first eight commands" are nine, and the plan evaluates `qa-dev`, which it never loads (`skills/dspy-tools-cli/SKILL.md:49-60`, `example_tools_cli.py:82-84`).
  - The book reference claims "every API claim in this pack is asserted against the installed wheel by its example's dry run" (`skills/dspy-context-engineering-book/reference.md:44-46`). The defects above are counterexamples.
  - The CHANGELOG has two `## v0.7.0` entries (`docs/CHANGELOG.md:165,182`).
  - The evaluation reference's OpenTelemetry line `dspy.settings.configure(callbacks=[OTelCallback()])` (`skills/dspy-evaluation-harness/reference.md:79`) names a class DSPy does not have and uses the form the fundamentals skill bans (`SKILL.md:90`).

  [trap] (verified: grep, counts)
- **The examples' "Optimized" number is a selection-set number** — every `optimized_score` comes from the same valset GEPA used for Pareto selection. 01 and 02 replay it from cache (0.0s). 03's is "GEPA's own full-valset evaluations cached in `gepa_state.bin`, which are the same values GEPA uses for candidate selection — they're reliable" (`examples/03-invoice-extraction/README.md:21`). No example has a held-out test set. [trap] (verified: results files) → here: pairs.py must score on a held-out fold
- **Baseline variance exceeds the gains** — same program, same task/reflection model pair and same seed, across runs and DSPy versions. The comparison files record empty caches for the "clean" runs; the other runs record no cache state.
  - 03: baselines of **0.739** (3.1.3 probe), **0.833** (3.1.3 historical) and **0.944** (3.2.0), a spread of 0.205, against a reported gain of +0.098.
  - 01: baselines of **75.77** (3.2.0, `docs/CHANGELOG.md:332`), **80.47** (3.2.0 clean) and **86.10** (3.1.3 clean).
  - 02: +8.33 on a 12-example valset is exactly one example (1/12).
  - 03's valset has 9 examples and 01's has 10.
  - The repo calls the 0.944 baseline "saturation"; it is equally consistent with run-to-run noise.

  [trap] (verified: arithmetic on the committed JSON) → here: pairs.py repeats (P18), baseline.py
- **The reasoning-model LM rule meets the examples' flags** — `--reflection-model openai/gpt-5` with the examples' `max_tokens=8000` raises `LMConfigurationError` at construction. [trap] (verified: bt.py)
- **Smaller doc errors** —
  - `Embeddings.from_saved` is a classmethod, not a staticmethod (`skills/dspy-retrieval/reference.md:18`).
  - ChatAdapter is not "JSON-in-markdown" (`skills/dspy-fundamentals/reference.md:135`).
  - `EvaluationResult` is not a dataclass (`skills/dspy-evaluation-harness/reference.md:24-29`).
  - `api_key`/`api_base` are not named `LM` parameters (`skills/dspy-fundamentals/reference.md:26-27`).
  - `teacher=` raises in GEPA, rather than being ignored.
  - `configure` is not thread-local.

  [trap] (verified: sigs.py, source)
- **The gepa_kwargs docstring is wrong about duplicates** — "Parameters already handled by DSPy's GEPA class will be overridden by the direct parameters", but duplicates reach `optimize(seed=..., **gepa_kwargs)` and would raise `TypeError: got multiple values for keyword argument`. `SP/dspy/teleprompt/gepa/gepa.py:353-354,632-662` [trap] (verified: Python call semantics, not executed)

## 3. Code worth keeping

**a. A semantic probe beyond signatures.** `scripts/check_dspy_surface.py:174-192`. It runs on 3.3.1: I ran the script, and it printed OK. It pins the metric contract and the percent scale.
```python
    def gepa_metric(gold, pred, trace=None, pred_name=None, pred_trace=None):
        return dspy.Prediction(score=1.0, feedback=f"ok for {pred_name or 'program'}")

    dspy.GEPA(
        metric=gepa_metric,
        auto="light",
        reflection_lm=dspy.LM("openai/gpt-5", temperature=1.0, max_tokens=32000),
    )

    def evaluate_metric(gold, pred, trace=None):
        return dspy.Prediction(score=float(pred.answer == gold.answer), feedback="ok")

    example = dspy.Example(question="ping", answer="ping").with_inputs("question")
    result = dspy.Evaluate(devset=[example], metric=evaluate_metric)(_EchoModule())
    _require(result.score == 100.0, "Evaluate did not aggregate Prediction metric score")
    _require(
        isinstance(result.results[0][2], dspy.Prediction),
        "Evaluate did not preserve Prediction metric result",
    )
```

**b. Asserting the optimizer surface the skill teaches.** `skills/dspy-optimizer-selection/example_optimizer_selection.py:102-124`. It runs on 3.3.1 (the dry-run exits 0).
```python
def assert_api_surface() -> None:
    """Fail loudly if the signatures this skill teaches have drifted."""
    import dspy

    assert dspy.BootstrapRS is dspy.BootstrapFewShotWithRandomSearch, "BootstrapRS alias is gone"
    assert "k" in inspect.signature(dspy.LabeledFewShot.__init__).parameters
    assert "metric" not in inspect.signature(dspy.LabeledFewShot.__init__).parameters, (
        "LabeledFewShot gained a metric parameter; the skill says it has none"
    )
    # SIMBA is keyword-only and carries its seed on compile(), not __init__.
    simba_init = inspect.signature(dspy.SIMBA.__init__).parameters
    assert all(p.kind is p.KEYWORD_ONLY for n, p in simba_init.items() if n != "self")
    assert "seed" in inspect.signature(dspy.SIMBA.compile).parameters
    assert "seed" not in simba_init
    # Ensemble.compile takes a list of programs, not (student, trainset).
    ensemble_compile = list(inspect.signature(dspy.Ensemble.compile).parameters)
    assert "programs" in ensemble_compile and "trainset" not in ensemble_compile
    # KNNFewShot takes the trainset up front and compiles without one.
    assert "trainset" in inspect.signature(dspy.KNNFewShot.__init__).parameters
    assert "trainset" not in inspect.signature(dspy.KNNFewShot.compile).parameters
    # BetterTogether takes arbitrary named optimizers, not a fixed pair.
    bt = inspect.signature(dspy.BetterTogether.__init__).parameters
    assert any(p.kind is p.VAR_KEYWORD for p in bt.values()), "BetterTogether lost **optimizers"
```

**c. A five-argument metric with a format axis and specific feedback.** `skills/dspy-advanced-workflow/example_pipeline.py:52-71`. It runs on 3.3.1: I ran it under Evaluate with DummyLM. Do not pair it with `save_as_json` (see TRAP), and set `metric_threshold` if a BootstrapFewShot-family optimizer uses it.
```python
    def rich_metric(gold, pred, trace=None, pred_name=None, pred_trace=None):
        pred_s = str(getattr(pred, "sentiment", "")).strip().lower()
        gold_s = gold.sentiment.strip().lower()
        correct = pred_s == gold_s
        format_ok = pred_s in {"positive", "negative", "neutral"}
        score = 1.0 if correct else (0.2 if format_ok else 0.0)
        if correct:
            feedback = "Correct label and valid format."
        elif format_ok:
            feedback = (
                f"Wrong label (predicted {pred_s!r}, expected {gold_s!r}). "
                f"Re-read the review for the dominant emotional valence; "
                f"don't over-index on neutral when there's a clear strong word."
            )
        else:
            feedback = (
                f"Invalid format: {pred_s!r}. "
                f"Output exactly one of: positive, negative, neutral — no extra words."
            )
        return dspy.Prediction(score=score, feedback=feedback)
```

**d. Partial credit plus diagnosis plus a per-row hint the dataset ships.** `examples/02-math-reasoning/pipeline.py:96-128`. It runs on 3.3.1: the dry-run's metric probe printed "WRONG: predicted 42, expected 26 (relative error 0.62)".
```python
    correct = _approx_equal(pred_ans, gold_ans)
    if correct:
        return dspy.Prediction(
            score=1.0,
            feedback=f"PASS: correct answer ({pred_ans:g}).",
        )

    # Scale the miss: a near-miss (within 10% relative) gets partial credit
    # so the gradient isn't all-or-nothing and GEPA can notice small fixes.
    denom = max(abs(gold_ans), 1.0)
    rel_err = abs(pred_ans - gold_ans) / denom
    partial = 0.2 if rel_err < 0.1 else 0.0

    # Diagnose: did the reasoning at least mention the right numbers?
    steps_look_sane = all(
        str(int(v)) in reasoning or f"{v:.1f}" in reasoning
        for v in _extract_salient_numbers(gold.problem)
    )
    diag = []
    if not steps_look_sane:
        diag.append("reasoning trace missed a salient number from the problem")
    if rel_err < 0.1:
        diag.append("off by a small arithmetic slip")
    elif rel_err > 2.0:
        diag.append("likely misread the problem structure")

    feedback = (
        f"WRONG: predicted {pred_ans:g}, expected {gold_ans:g}"
        f" (relative error {rel_err:.2f}). "
        + ("Observations: " + "; ".join(diag) + ". " if diag else "")
        + f"HINT for this problem: {gold.trap}"
    )
    return dspy.Prediction(score=partial, feedback=feedback)
```

**e. A deterministic test-double retriever and recall@k.** `skills/dspy-retrieval/example_retrieval.py:38-49,103-113`. It runs on 3.3.1 (the dry-run exits 0).
```python
class StubRetriever:
    """Deterministic lexical retriever: a test double with the same contract."""

    def __init__(self, corpus: list[str], k: int = DEFAULT_K) -> None:
        self.corpus, self.k = corpus, k

    def __call__(self, query: str):
        import dspy

        wanted = terms(query)
        ranked = sorted(self.corpus, key=lambda p: -len(wanted & terms(p)))
        return dspy.Prediction(passages=ranked[: self.k])

def recall_at_k(gold, pred, trace=None, pred_name=None, pred_trace=None):
    """Fraction of gold passages retrieval surfaced; GEPA-compatible return."""
    import dspy

    got = {p.strip() for p in pred.context}
    want = {p.strip() for p in gold.gold_passages}
    score = len(got & want) / max(len(want), 1)
    missing = want - got
    feedback = (f"Missed {len(missing)} gold passage(s): {sorted(missing)[:2]}"
                if missing else "All gold passages retrieved.")
    return dspy.Prediction(score=score, feedback=feedback)
```

**f. A BaseLM subclass that strips kwargs it cannot honour.** `skills/dspy-local-runtime/example_local_runtime.py:84-102`. It runs on 3.3.1 (the dry-run exits 0). Its `forward` must drop lines 113-114, which double-count usage on 3.3.1.
```python
    def __init__(self, model: str = "claude/default", *, permission_mode: str = "plan",
                 timeout_seconds: int = DEFAULT_TIMEOUT_SECONDS, cache: bool = False, **kwargs: Any):
        if cache:
            raise ValueError("ClaudeLM cannot cache: the CLI has no deterministic sampling to cache against")
        if not model.startswith("claude/"):
            raise ValueError(f"model must be 'claude/<alias>', got {model!r}")
        super().__init__(model=model, model_type="chat", temperature=None, max_tokens=None, cache=False, **kwargs)
        self.kwargs = {k: v for k, v in self.kwargs.items() if k not in STRIPPED_KWARGS}
        self.alias = model.split("/", 1)[1]
        self.permission_mode = permission_mode
        self.timeout_seconds = timeout_seconds

    def copy(self, **kwargs: Any) -> "ClaudeLM":
        """`lm.copy(rollout_id=…, temperature=…)` is what BestOfN/Refine and TetraFrame call: strip silently."""
        for key in STRIPPED_KWARGS:
            kwargs.pop(key, None)
        new = super().copy(**kwargs)
        new.kwargs = {k: v for k, v in new.kwargs.items() if k not in STRIPPED_KWARGS}
        return new
```

**g. Making a dynamically loaded pipeline picklable for GEPA checkpoints.** `examples/03-invoice-extraction/run.py:23-34`. It runs on 3.3.1 (the dry-run exits 0).
```python
def _import_pipeline():
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "invoice_pipeline", Path(__file__).parent / "pipeline.py"
    )
    mod = importlib.util.module_from_spec(spec)
    # Register in sys.modules BEFORE exec so pickle can resolve
    # `invoice_pipeline.InvoiceRecord` during GEPA state.save().
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod
```

**h. One metric, two consumers: a float for Evaluate, the Prediction for GEPA.** `examples/01-rag-qa/run.py:85-94`. It runs on 3.3.1 (dry-run exit 0; its `float(out)` relies on `Prediction.__float__`, which I verified). This is what keeps `save_as_json` from crashing in the examples.
```python
def _score_wrapper(metric):
    """dspy.Evaluate needs a metric returning a float; unwrap dict→float."""

    def m(g, p, trace=None, **kw):
        out = metric(g, p, trace, **kw)
        if isinstance(out, dict):
            return out.get("score", 0.0)
        return float(out)

    return m
```

**i. Frontmatter that strict YAML parsers accept.** `tests/test_skill_metadata.py:128-154`. It runs (pytest passes).
```python
@pytest.mark.parametrize("skill_dir", _skill_dirs(), ids=lambda p: p.name)
def test_frontmatter_plain_scalars_are_yaml_safe(skill_dir: Path):
    """Guard compatibility with strict YAML frontmatter parsers.

    The `npx skills` CLI uses a real YAML parser and skips skills whose
    frontmatter cannot parse. In inline plain scalars, `: ` starts a mapping,
    so values with human prose containing colon-space need quotes or a block
    scalar.
    """

    block = _frontmatter_block((skill_dir / "SKILL.md").read_text(encoding="utf-8"))
    offenders: list[str] = []
    for line_no, line in enumerate(block.splitlines(), 2):
        if line.startswith(" "):
            continue
        m = re.match(r"^([A-Za-z][A-Za-z0-9_-]*)\s*:\s*(.*)$", line)
        if not m:
            continue
        value = m.group(2)
        if _is_inline_plain_scalar(value) and ": " in value:
            offenders.append(f"{skill_dir / 'SKILL.md'}:{line_no}: {line.strip()}")

    assert not offenders, (
        "Inline YAML frontmatter values containing `: ` must be quoted or written "
        "as block scalars for npx skills compatibility:\n  "
        + "\n  ".join(offenders)
    )
```

**j. GEPA's auto budget, from the installed DSPy 3.3.1 wheel, not from the slice.** `SP/dspy/teleprompt/gepa/gepa.py:490-520`. It runs: I called it through `g.auto_budget(...)` in gepa1.py. A skill should show this instead of either of the pack's tables.
```python
    def auto_budget(
        self, num_preds, num_candidates, valset_size: int, minibatch_size: int = 35, full_eval_steps: int = 5
    ) -> int:
        num_trials = int(max(2 * (num_preds * 2) * math.log2(num_candidates), 1.5 * num_candidates))
        if num_trials < 0 or valset_size < 0 or minibatch_size < 0:
            raise ValueError("num_trials, valset_size, and minibatch_size must be >= 0.")
        if full_eval_steps < 1:
            raise ValueError("full_eval_steps must be >= 1.")

        V = valset_size
        N = num_trials
        M = minibatch_size
        m = full_eval_steps

        # Initial full evaluation on the default program
        total = V

        # Assume upto 5 trials for bootstrapping each candidate
        total += num_candidates * 5

        # N minibatch evaluations
        total += N * M
        if N == 0:
            return total  # no periodic/full evals inside the loop
        # Periodic full evals occur when trial_num % (m+1) == 0, where trial_num runs 2..N+1
        periodic_fulls = (N + 1) // (m) + 1
        # If 1 <= N < m, the code triggers one final full eval at the end
        extra_final = 1 if N < m else 0

        total += (periodic_fulls + extra_final) * V
        return total
```

## 4. The old report, corrected

Part A is `dspy-agent-skills-A.md` and Part B is `-B.md`, both from 2026-09-23.

- **A §1: "~40 ... skills".** There are 32 skill directories and 33 example files.
- **A §1 and §2.9: "Every skill ships a runnable example_*.py --dry-run (no LM call, asserted by tests ...)".** The tests assert only that the *string* `--dry-run` appears (`tests/test_examples_parse.py:38-44`, `tests/test_skill_correctness.py:268-280`). No test runs a dry-run. I ran all 11 in the slice (exit 0), plus the 3 `examples/*/run.py --dry-run` on 3.3.1 (exit 0; the repo documents them only for 3.2.0).
- **A §2.1: "walks inspect.signature on every API surface the pack teaches".** It covers a subset. It has no probe for `dspy.load`, `save_as_json`, BootstrapFewShot, MIPROv2, KNNFewShot, Ensemble, `DspyGEPAResult` fields or GEPA budget exclusivity. Each of those hides a real 3.3.1 defect listed in TRAP. The one semantic probe A mentions, `result.score == 100.0`, proves that `.score` is a percentage. A did not draw the consequence: the harness skill's `assert result.score >= 0.75` cannot fail.
- **A §2.12: the five-argument metric as "the single most load-bearing, most repeated fact".** It is correct but incomplete.
  - (a) In 3.3.1, GEPA itself enforces it at construction: `TypeError: GEPA metric must accept five arguments`. I did not check which release added this.
  - (b) Returning `dspy.Prediction` everywhere is not safe. BootstrapFewShot-family optimizers read it by truthiness, so every wrong demo is kept unless `metric_threshold` is set, and `Evaluate(save_as_json=...)` raises `TypeError` after the run.
  - Both matter for the target, whose `pairs.py` ladder puts one Prediction metric through LabeledFewShot → BootstrapFewShot → InferRules → SIMBA → GEPA.
- **A §2.14: GEPA asserts at construction.** This is right. Add the exact assertion message and the second construction assertion, "Exactly one of max_metric_calls, max_full_evals, auto must be set". A missed that `dspy-local-runtime/SKILL.md:95` violates it.
- **A §2.15 ("20–50 well-chosen beats 500 bland") and A §3 ("direct license to try GEPA").** This is an unmeasured [claim] in the pack. A presented it as guidance. The pack's own examples measure gains of +0.098, +8.33 and +19.53 on valsets of 9–12 examples, with run-to-run baseline spreads (0.205 in 03; 10.3 points in 01) as large as or larger than the gains. They are also scored on the selection set. They do not support any claim about GEPA's effect size.
- **A §2.16 and §3: "InferRules ... isn't covered anywhere here beyond the name; would need upstream DSPy docs".** True of the pack. But `dspy.InferRules` exists in 3.3.1, and its constructor, compile, split, rule-induction prompt, cache behaviour and inherited bootstrap trap are now in `## OPT` from the installed source.
- **A §2.17: the constructor and `compile` tables are "verified against dspy 3.3.1".** The signatures verify. The same skill's BetterTogether usage does not: `compile(program, trainset=...)` without `strategy=` raises `ValueError` on 3.3.1, and "the order is the run order" is false. Its "Prediction ... everything else (the score is read)" is false for BootstrapFewShot. Its trainset table offers SIMBA for 10–50 examples, although SIMBA asserts `len(trainset) >= bsize=32`.
- **A §2.18 on BetterTogether.** Add: step failures are swallowed (`flag_compilation_error_occurred`); `valset_ratio=0.1` takes the *first* 10% unshuffled; every predictor needs an LM (`set_lm`).
- **A §2.34: "use save_program=False always".** Right, but incomplete for 3.3.1. `dspy.load` now requires `allow_pickle=True`. `Module.load` has `allow_pickle` and `allow_unsafe_lm_state`, and LM endpoint keys are stripped on load. Every `dspy.load(dir)` the pack teaches raises.
- **A §2.35: measure cost with the cache disabled.** Verified in source: `BaseLM` skips usage when `cache_hit`. A missed the pack's own evidence: every "optimized-eval 0.0s" in the examples is a cache replay of GEPA's selection-set calls.
- **A §2.36 and §3: "Add one dspy.configure(track_usage=True) ... print(prediction.get_lm_usage())".** This works. But a custom `BaseLM` that records usage itself, like the pack's `ClaudeLM`, double-counts on 3.3.1 (measured 24/2 tokens for a 12/1 response). And the production skill's usage callback records 0 tokens against a real LM, because `on_lm_end` receives a list. That is directly relevant to `lm_fixture.py`/`lmrun.py`.
- **A §4 contradicts itself on dict metrics.** It says "No dict-metric anywhere is *tested for*", then that the pack "tests against it in three places". The rule-2 test catches dict *guidance* in docs, and the surface check probes only Prediction aggregation. No test runs a dict metric; I did (`TypeError: unsupported operand type(s) for +: 'int' and 'dict'`).
- **A §2.1 says check_dspy_surface.py spans lines 1-204.** It is 203 lines. This is trivial, but the brief requires real line numbers.
- **B §2.53 and §4 (P18): "nothing in the material I scanned tells you how to turn DSPy's cache off".** The core slice does: `dspy.LM(..., cache=False)`, `configure_cache(enable_disk_cache=False, enable_memory_cache=False)`, "Measure cost with the cache disabled at least once", and local-runtime's "`cache=False`, always". The DSPy source adds `DSPY_CACHEDIR`/`DSPY_CACHE_LIMIT`, read at import.
- **B §5: "no `dspy.LM(...)` construction even".** This holds for the book examples B read. In the core slice, the GEPA, BetterTogether, optimizer-selection and pipeline dry-runs *do* construct `dspy.LM` stubs, without a network call. No dry-run executes a module; `dspy.utils.DummyLM`, which the pack never uses, would.
- **B §3: the examples' READMEs were "skimmed via wc -l only".** They are read here, with the conditions of every number.
  - `optimized_score` is measured on GEPA's own selection valset (9–12 examples), and for 03 it is GEPA's internal aggregate on a 0–1 scale, while 01 and 02 use Evaluate percentages.
  - Baselines for identical configurations differ by more than the reported gains.
  - The learned instructions quote training answers verbatim (4 of 15 in 01).
  - `auto="light"` planned 416 rollouts for 1 predictor and 9 val, which confirms the formula.
- **B §2.66: "the check asserted 7 of 8 relevant symbols and missed RLM".** The CHANGELOG lists 8 asserted surfaces (GEPA, BetterTogether, Evaluate, LM, SIMBA, Embedder, Refine, BestOfN) and says RLM was never asserted (`docs/CHANGELOG.md:22-25`).
- **Both reports miss the new 3.3.1 surfaces.** These are the typed custom-LM contract (`forward_contract="typed_lm"`, `dspy.LMRequest`/`LMResponse`), `dspy.Flex` code optimization with a sixth `program_trace` metric parameter, multi-objective GEPA through `objective_scores`, and gepa 0.1.4's `gepa_kwargs` (stop callbacks, `acceptance_criterion`, `val_evaluation_policy`). All are relevant to `lm_fixture.py` and `pairs.py`.

## 5. Ten things the skill must say

1. `dspy.Evaluate(...)(program).score` is a percentage: `round(100*ncorrect/ntotal, 2)`. Every floor and CI gate must use 0–100. See MET "Evaluate's `.score` is a percentage" and TRAP "The CI gate cannot fail".
2. GEPA's metric must accept five positional arguments, `(gold, pred, trace, pred_name, pred_trace)`, which 3.3.1 enforces at construction. Return the module-level score together with per-predictor feedback. A float only yields "This trajectory got a score of X." See OPT "GEPA checks the metric's arity" and "How GEPA calls the metric for feedback".
3. A metric returning `dspy.Prediction(score, feedback)` is truthy even at score 0. Give every BootstrapFewShot-family rung (BootstrapRS, KNN, MIPROv2 demos, InferRules) a `metric_threshold` or a float wrapper, and never combine it with `save_as_json`. See TRAP "BootstrapFewShot reads a Prediction metric by truthiness" and "save_as_json with a Prediction metric crashes".
4. Set exactly one GEPA budget. Budget from `auto_budget`: light ≈ 380 + 4V metric calls for one predictor, and the repo's example 03 run planned exactly 416 for V=9. The pack's two tables are wrong. See OPT "The auto budget is a formula" and TRAP "Both GEPA budget tables are wrong".
5. Failures turn into scores silently. Evaluate, GEPA and SIMBA score metric exceptions as `failure_score`/0. BetterTogether swallows step errors. Evaluate ignores misspelled kwargs. Record "could not score" separately. See TRAP "Errors become scores".
6. On 3.3.1, `dspy.load` needs `allow_pickle=True`, and `Module.load` strips `api_base`/`base_url`/`model_list` unless `allow_unsafe_lm_state=True`. State JSON is the only format to accept from elsewhere. See API "dspy.load needs allow_pickle=True" and "Module.load".
7. Optimizers split data implicitly and unshuffled: GEPA reuses the trainset, MIPROv2 uses the last 80%, BetterTogether the first 10%, InferRules 50/50. BetterTogether with named optimizers needs `strategy=`, and SIMBA needs `len(trainset) >= bsize` (32). Pass explicit stratified splits. See DATA "Optimizers' implicit splits" and OPT "BetterTogether" and "SIMBA".
8. Cached calls record no usage and emit no stream chunks. The examples' "optimized" scores are cache replays of GEPA's selection-set evaluation. Measure with the cache off and on a held-out set. See PROD "Cached calls cost nothing" and TRAP "The examples' Optimized number is a selection-set number".
9. The examples' gains (+19.53, +8.33, +0.098) fall within run-to-run baseline variance on valsets of 9–12 examples. Cite them only as mechanics, never as evidence of GEPA's effect. See TRAP "Baseline variance exceeds the gains".
10. A custom `BaseLM` must not record usage itself (BaseLM already does), and `on_lm_end` receives a list, not a dict. Test with `dspy.utils.DummyLM`, which runs modules offline: a dry-run that only constructs objects missed every live-path defect listed here. See API "BaseLM records usage itself", TRAP "ClaudeLM double-counts usage", and TEST "dspy.utils.DummyLM runs modules offline".
