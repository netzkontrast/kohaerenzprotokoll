# DSPy knowledge extract: `dspy-agents` + `Agentic-Dspy-Rag`

Reader slice 2026-09-24. Both repositories were read in full (every tracked file,
lock files excepted). Neither repository was modified. Every run happened in a
`git archive` copy under the scratchpad.

## 1. Header

### [agents] dspy-agents

- **Repo / commit:** github.com/netzkontrast/dspy-agents, `fde0dad` (2025-09-26, "Re-run compile/eval after dataset expansion"). 51 commits, 22–26 Sep 2025, author Ben Venker.
- **License:** none. There is no LICENSE file and the README names no license, so default copyright applies. Copy patterns, not code.
- **DSPy targeted:** `dspy-ai>=3.0.3,<4.0` (`requirements.txt:2`, with a leading space that pip and uv both tolerate). The compiled artifacts were saved with DSPy 3.0.3, Python 3.12 and cloudpickle 3.1 (the `metadata.json` in git history at `99966c8` and `99a03a7`). Resolving that range today gives `dspy-ai==3.3.1`, a meta-package that requires `dspy>=3.3.1`. With `--exclude-newer 2025-09-27` it gives 3.0.3.
- **Does it hold on 3.3.1?** Everything the repo constructs runs on 3.3.1 offline, with two exceptions. **`dspy.load(path)` raises on DSPy ≥3.1.0 unless `allow_pickle=True`**, and every caller swallows that error, so the compiled program is never used. **`OPENAI_MAX_OUTPUT_TOKENS` is silently ignored.**
- **What it is:** an Agno AgentOS (FastAPI) "Researcher" agent. Its tools call one DSPy program, `ChainOfThought("context, question -> answer")`, which is compiled once with MIPROv2 (`auto="light"`, exact match, `gpt-4o-mini`) on a 50-row hand-written QA JSONL. Around it sit:
  - an eval harness comparing zero-shot and compiled EM;
  - a SQLite/Postgres baseline store with drift thresholds and a CI monitor;
  - keyword retrieval plus LanceDB "hybrid" retrieval over a tiny docs folder;
  - request, run and tool logging;
  - ten per-directory `AGENTS.md` guides.

### [agentic-rag] Agentic-Dspy-Rag

- **Repo / commit:** github.com/netzkontrast/Agentic-Dspy-Rag, `474f107` (2025-06-18, "m"). 7 commits, 17–18 Jun 2025, author zaheer shaik. Five Python files, `workflow.txt`, one 26-page 1.4 MB PDF.
- **License:** none.
- **DSPy targeted:** unpinned. There is no `requirements.txt`; the README says „(You would create this file)" (`README.md:66`). The code uses `dspy.LM`, which only exists from DSPy 2.5. The README's own install line with `"pydantic<2"` (`README.md:68`) resolves to `dspy-ai==2.3.1`, which has no `dspy.LM`.
- **Does it hold on 3.3.1?** Yes, offline with fakes, but only if `numpy` is imported before `dspy`. Without that, `data_modules.py` fails at import on 3.3.1 (TRAP section).
- **What it is:** a FastAPI `/query` endpoint running this pipeline: optional chat-history condensation → `dspy.Predict("question -> intent")` classifier → substring routing to SimpleRAG, ComparativeRAG or MultiStepRAG (all `ChainOfThought`) → Qdrant retrieval with LLM query expansion → Gemini-embedding "rerank". Ingestion is Zerox vision OCR of one PDF. There are no tests.

### What I ran (all offline, `env -u OPENROUTER_API_KEY -u TYPESAFE_API_KEY -u OPENAI_API_KEY -u ANTHROPIC_API_KEY` on every command)

**Environments**, all under `scratchpad/venvs/`:

| venv | contents |
|---|---|
| `agents` | dspy 3.3.1, python-dotenv, pytest, optuna |
| `agents-full` | dspy 3.3.1, agno 3.0.11, lancedb 0.24.3 |
| `agents-2025` | `uv pip install --exclude-newer 2025-09-27 -r requirements.txt`: dspy 3.0.3, agno 2.0.11, lancedb 0.24.3, litellm 1.77.4 |
| `agents-mix` | dspy 3.3.1, agno 2.0.11 |
| `rag331` | dspy 3.3.1, qdrant-client 1.19.1, google-generativeai 0.8.6, fastapi 0.141.1 |
| `dspyvers/` | DSPy 3.0.4–3.3.0 and dspy-ai 2.3.1, extracted `--no-deps` to grep their source |

The shared `/home/user/kohaerenzprotokoll/.venv-dspy` (DSPy 3.3.1) was used read-only, for reading DSPy source and for one import check.

**Test suite.** pytest `-m "not integration"` in four environments (results under TEST).

**Offline fake LM.** `scratchpad/work/fakelm.py` defines `CountingFillLM(DummyLM)`: it fills every requested output field, counts calls thread-safely, and reports 10/5/15 tokens per call. It was used to run:
- MIPROv2 light on the repo's 50-row dataset;
- `dspy_optimize/compile_rag.py:main()` and `eval/harness.py:main()`, with `dspy.LM` monkeypatched to the fake;
- `dspy_config.get_rag_program()`;
- `dspy.Evaluate` at 1 and 8 threads inside `dspy.track_usage()`.

**Other checks.**
- Real `dspy.LM(...)` construction with the repo's kwargs, plus `_convert_chat_request_to_responses_request`.
- Reasoning-model detection compared across DSPy and the repo's two rules.
- A `Literal` intent parse on 3.3.1.
- LanceDB ingest, FTS and hybrid search with a fake embedder.
- `uv pip compile` of the RAG README install line, today and `--exclude-newer 2025-06-19`.
- `find_packages`; `git check-ignore`.
- The RAG orchestrator routing table (`scratchpad/work/rag_routing_check.py`).
- The RAG FastAPI app end to end through `TestClient` (`scratchpad/work/rag_api_check.py`).

Where code demanded a non-empty key, a fake value was set and `OPENAI_BASE_URL=http://127.0.0.1:9` was set as well. No network call to a model provider was made.

---

## 2. Knowledge items

## API

- **[agents] Chat vs Responses `dspy.LM` construction** — `configure_once()` chooses between two constructors:
  - reasoning models: `dspy.LM(f"openai/{model_id}", model_type="responses", use_developer_role=True, api_key=…, temperature=…, max_tokens=…, max_output_tokens=…, reasoning={"effort": effort})`;
  - otherwise: `dspy.LM(f"openai/{model_id}", model_type="chat", api_key=…, temperature=…, max_tokens=…)`.

  `OPENAI_USE_RESPONSES=auto` picks Responses for reasoning models. The value is `auto|true|false`, and any value outside `{1,true,yes,y,on}` means chat. `dspy_config.py:148-153,180-205` [api] (verified: the same kwargs construct a real `dspy.LM` on 3.3.1) → here: lmrun.py
- **[agents] 3.3.1 renames `max_tokens` for reasoning models** — For a model DSPy classes as reasoning, `max_tokens=20000` is stored as `max_completion_tokens`. For `gpt-5` the result is `lm.kwargs == {'temperature': 1.0, 'max_completion_tokens': 20000, 'max_output_tokens': 20000, 'reasoning': {'effort': 'medium'}}`. In Responses mode the converter maps it back: `max_completion_tokens → max_tokens → max_output_tokens`. DSPy 3.3.1 `dspy/clients/lm.py:123-135,634-638` [api] (verified: printed `lm.kwargs` and the converted request offline) → here: lmrun.py, check_dspy_surface.py
- **[agents] Reasoning-model validation message** — `dspy.LM("openai/gpt-5", temperature=0.0, max_tokens=4000)` raises `LMConfigurationError`: „[openai/gpt-5] OpenAI's reasoning models require passing temperature=1.0 or None and max_tokens >= 16000 or None to `dspy.LM(...)`". The repo satisfies it by forcing `temperature=1.0` and a 16000 floor (defaults: 20000 for reasoning models, 4000 otherwise). `dspy/clients/lm.py:125-131`; `dspy_config.py:160-164,177` [api] (verified: raised offline) → here: lmrun.py
- **[agents] DSPy's own reasoning-model rule** — `_is_openai_reasoning_model` matches `^(?:o[1345](?:-(?:mini|nano|pro))?(?:-\d{4}-\d{2}-\d{2})?|gpt-5(?!-chat)(?:-.*)?)$` against the id after the last `/`. `dspy/clients/lm.py:48-53` [api] (verified: comparison table under TRAP)
- **[agents] `use_developer_role`** — The default is `False`. With `True` and `model_type="responses"`, `system` messages are sent as role `developer`. `dspy/clients/lm.py:237-238`; set at `dspy_config.py:197` [api] (verified: 3.3.1 source; parameter present in `inspect.signature(dspy.LM.__init__)`)
- **[agents] `track_usage` switched on globally** — compile and eval pass it to `dspy.configure(lm=…, track_usage=True)` (`compile_rag.py:70-73`, `eval/harness.py:101-104`). Runtime config calls `dspy.settings.configure(track_usage=True)` after `dspy.configure(lm=lm)` (`dspy_config.py:207-208`), and `tests/test_caching.py:87` pins that second call. The `DEFAULT_CONFIG` default is `track_usage=False` (`dspy/dsp/utils/settings.py:25`). [api]
- **[agents] `dspy.track_usage()` output shape** — It is a context manager yielding a `UsageTracker`. `get_total_tokens()` returns `{lm.model: {prompt_tokens, completion_tokens, total_tokens, completion_tokens_details{...}, prompt_tokens_details{...}}}`, keyed by the LM's model string, e.g. `openai/gpt-4o-mini`. `dspy/utils/usage_tracker.py:69-74`; shape recorded in `dspy_optimize/baselines/compile_metrics.jsonl:1-2`; read back through `dspy.settings.lm.model` at `compile_rag.py:94,140` [api] (verified: offline tracker output)
- **[agents] `Prediction.get_lm_usage()` semantics** — The result depends on the context:
  - `None` when `track_usage=False`;
  - per-call usage when `dspy.configure(track_usage=True)`;
  - `None` inside an enclosing `with dspy.track_usage()`, because the outer tracker receives it.

  `dspy/primitives/module.py:102-103,121-122`. The repo uses it in `scripts/cache_benchmark.py:38` [api] (verified offline, all three cases) → here: lmrun.py
- **[agents] A cache hit reports zero usage** — On a hit, `Cache._prepare_cached_response` sets `response.usage = {}` and `cache_hit=True`, and `BaseLM` skips the tracker for `cache_hit`. „Clear the usage data when cache is hit, because no LM call is made" (`dspy/clients/cache.py:149-157`, `dspy/clients/base_lm.py:294-295`). The repo's own evidence is `eval_metrics.jsonl:2-3`: two eval runs with `"usage": {}`, the compiled pass taking 0.04 s. `cache_benchmark.py:39` infers `cached = not usage` [api] (verified: source + logged runs)
- **[agents] `dspy.configure_cache` on 3.3.1** — The signature is `(enable_disk_cache=True, enable_memory_cache=True, disk_cache_dir='~/.dspy_cache', disk_size_limit_bytes=30_000_000_000, memory_max_entries=1_000_000, restrict_pickle=False, safe_types=None)`. It replaces the global `dspy.cache` object. DSPy's default cache reads the env vars `DSPY_CACHEDIR` and `DSPY_CACHE_LIMIT`. `dspy/clients/__init__.py:19-61` [api] (verified: `inspect.signature` + source)
- **[agents] The repo's cache env names are its own** — They are `DSPY_ENABLE_DISK_CACHE`, `DSPY_ENABLE_MEMORY_CACHE`, `DSPY_CACHE_DISK_LIMIT_BYTES`, `DSPY_CACHE_MEMORY_MAX_ENTRIES`, `DSPY_CACHE_DIR` and `DSPY_CACHE_TAG`. Defaults: disk on, memory on, 30e9 bytes, 1e6 entries, `.cache/dspy`. **`DSPY_CACHE_DIR` (repo) ≠ `DSPY_CACHEDIR` (DSPy).** `dspy_config.py:100-123` [api] (verified: read; the cache landed in `$DSPY_CACHE_DIR/<sig>` offline)
- **[agents] DSPy cache key** — The key is `sha256(orjson.dumps(request, OPT_SORT_KEYS))` over the whole request minus `["api_key","api_base","base_url"]`. Any change to instructions, demos, model, temperature or `rollout_id` therefore produces a new key. `dspy/clients/cache.py:104-113,236` [api] (verified: source) → here: lmrun.py (uses `cache=False` anyway)
- **[agents] `reset_memory_cache()` is a no-op when the memory cache is disabled** — It returns early when `not self.enable_memory_cache`. The repo calls it straight after `configure_cache(enable_disk_cache=False, enable_memory_cache=False)`. `dspy/clients/cache.py:189-191`; `compile_rag.py:62-67`, `eval/harness.py:94-99` [api]
- **[agents] `dspy.load` needs `allow_pickle=True` since DSPy 3.1.0** — The 3.3.1 signature is `load(path: str, allow_pickle: bool = False)`. Without the flag it raises `ValueError`: „Loading with pickle is not allowed. Please set `allow_pickle=True` if you are sure you trust the source of the model." It raises before checking that the path exists. DSPy 3.0.3 and 3.0.4 have `load(path)`; 3.1.0, 3.1.3, 3.2.0, 3.2.1, 3.3.0 and 3.3.1 all have `allow_pickle`. `dspy/utils/saving.py:27-40` [api] (verified: grepped eight versions' source; ran it offline) → here: check_dspy_surface.py
- **[agents] `Module.save(path, save_program=True)`** — It writes a directory containing `program.pkl` (cloudpickle of the whole module) and `metadata.json`, which holds `{"dependency_versions": {python, dspy, cloudpickle}}`. The path must have no suffix. It logs „Loading untrusted .pkl files can run arbitrary code…" and accepts `modules_to_serialize` for `register_pickle_by_value`. `dspy/primitives/base_module.py:171-230`; used at `compile_rag.py:90` [api] (verified: saved offline)
- **[agents] Pickle-free alternative** — `program.save("x.json")` writes state only, with keys `predict` and `metadata`. Load it with `dspy.ChainOfThought("context, question -> answer").load("x.json")`; no pickle is involved. On a trivial MIPROv2 output this was 733 bytes against a 29,621-byte `program.pkl`. `Module.load(path, allow_pickle=False, allow_unsafe_lm_state=False)` is at `dspy/primitives/base_module.py:254-279` [recipe] (verified offline) → here: pairs.py artifacts
- **[agents] MIPROv2 decorates the program it returns** — It sets `score`, `trial_logs`, `candidate_programs` (11 on a light run), `mb_candidate_programs`, `total_calls` and `prompt_model_total_calls`. `save_program=True` pickles all of them, so every candidate prompt ends up inside the artifact. `dspy/teleprompt/mipro_optimizer_v2.py:675-688` [api] (verified: attributes present after `dspy.load(..., allow_pickle=True)`; `pickletools` on the historical artifacts at `99966c8`/`99a03a7` shows the candidate instructions, e.g. „In a high-stakes scenario where a user urgently needs insights into Agno AgentOS's functionalities…")
- **[agents] Default ChainOfThought prompt** — `dspy.ChainOfThought("context, question -> answer")` has the instruction „Given the fields `context`, `question`, produce the fields `answer`." and output fields `reasoning`, `answer`. [api] (verified: printed on 3.3.1)
- **[agentic-rag] Config kwargs on predictors** — `dspy.Predict("question -> intent", n=1)` and `dspy.ChainOfThought("question -> rephrased_queries", n=1)` pass `n` through as LM config. `agents.py:101`, `data_modules.py:40` [api]
- **[agentic-rag] `dspy.Retrieve` still exists in 3.3.1** — `Retrieve.__init__(k=3, callbacks=None)` and `forward(query, k=None, **kwargs)`. The subclass overrides `forward(self, query_or_queries, k=None)` and returns `dspy.Prediction(passages=list(dict.fromkeys(passages)))`. `data_modules.py:26-69` [api] (verified: `inspect` on 3.3.1; the module imports and runs with numpy imported first)
- **[agentic-rag] Extra fields on a `Prediction`** — `prediction.intent = user_intent` adds a field after the fact, read back with `getattr(prediction, 'intent', 'Unknown')`. `agents.py:126`, `main.py:146` [api] (verified: the `/query` response carried `intent` on 3.3.1)
- **[agentic-rag] LM history entries (3.3.1)** — Each entry holds `prompt, messages, kwargs, response, outputs, usage, cost, timestamp, uuid, model, response_model, model_type`. `cost` is LiteLLM's `response_cost`, which is `None` on a cache hit. Per-LM `lm.history` is capped at `settings.max_history_size = 10000`, and module-level `GLOBAL_HISTORY` at `MAX_HISTORY_SIZE = 10_000`. `dspy/clients/base_lm.py:22-23,299-313,776-799` [api] → here: lmrun.py (record per call instead)
- **[agentic-rag] `lm.kwargs` has no `"model"` key** — The model string is `lm.model`, so `lm.kwargs.get('model', 'unknown')` is always `'unknown'`. `agents.py:29,54` [api] (verified: printed on 3.3.1; the usage log line read „Model: unknown" in every offline run)
- **[agentic-rag] Settings are owned by one thread (applies to [agents] too)** — The first thread to call `dspy.configure` owns the settings. A later `configure` from another thread raises `RuntimeError`: „dspy.settings can only be changed by the thread that initially configured it." Inside an async task, a second `configure` is disallowed; use `dspy.context(...)`. `dspy/dsp/utils/settings.py:117-135` [api] (verified: FastAPI `TestClient` startup raised it at `main.py:75` once the main thread had configured first)
- **[agentic-rag] A `Literal` output type enforces the enum** — Declaring `intent: Literal["Factual","Comparative","Multi-step"] = dspy.OutputField()` makes the ChatAdapter print the choices in the system prompt (`` 1. `intent` (Literal['Factual', 'Comparative', 'Multi-step']): ``). Off-list outputs such as `"comparative"`, `"Multi-Step"` or `"Not Comparative"` raise `AdapterParseError` after the automatic JSONAdapter fallback. Matching is case-sensitive. [recipe] (verified offline with `DummyLM` on 3.3.1) → here: graphrag.py `--answer`, pairs.py decision field
- **[agents] `Evaluate` defaults inside MIPROv2** — MIPROv2 builds `Evaluate(devset=valset, metric, num_threads, max_errors=effective_max_errors, display_table=False, display_progress=True, provide_traceback=…)`. `effective_max_errors` defaults to `dspy.settings.max_errors = 10`. `dspy/teleprompt/mipro_optimizer_v2.py:217-227`; `settings.py:32` [api]

## OPT

- **[agents] The MIPROv2 call** — `dspy.MIPROv2(metric=dspy.evaluate.answer_exact_match, auto="light", num_threads=8)`, then `tp.compile(program, trainset=trainset)`. It passes no `valset`, no seed (default `seed=9`) and no demo limits (defaults `max_bootstrapped_demos=4`, `max_labeled_demos=4`). The call runs inside `with dspy.track_usage() as usage_tracker:`. `dspy_optimize/compile_rag.py:82-87` [recipe] (verified: identical call runs on 3.3.1 with the fake LM in 3.5 s)
- **[agents] What `light` means for one predictor** — 3.3.1 printed:

  „RUNNING WITH THE FOLLOWING LIGHT AUTO RUN SETTINGS: num_trials: 10 / minibatch: False / num_fewshot_candidates: 6 / num_instruct_candidates: 3 / valset size: 40"

  - `AUTO_RUN_SETTINGS`: `light {n:6, val_size:100}`, `medium {n:12, val_size:300}`, `heavy {n:18, val_size:1000}`.
  - `num_trials = int(max(2*num_vars*log2(n), 1.5*n))`, where `num_vars` = predictors × 2 when demos are allowed.
  - Instruction candidates = `n` when zero-shot, otherwise `int(n*0.5)`.
  - Minibatch is used only when `len(valset) > MIN_MINIBATCH_SIZE (50)`.

  `dspy/teleprompt/mipro_optimizer_v2.py:44-50,280-316` [number] (verified offline)
- **[agents] The automatic split takes the tail, unshuffled** — With `valset=None`: `valset_size = min(1000, max(1, int(len(trainset)*0.80)))` and `valset = trainset[cutoff:]`, with no shuffle. The repo's 50 rows become 10 train (rows 1–10: Agno and DSPy basics) and 40 val (the later-added observability, GitHub and OpenAI Responses rows). The earlier 29-row run was 6 train / 23 val. `mipro_optimizer_v2.py:319-333` [number] (verified offline) → here: trainset.py, pairs.py (pass stratified folds explicitly)
- **[agents] Size of one light run** — 482 LM calls for the 50-row set: 6 bootstrap sets over 10 train examples, 3 instruction proposals plus data and program summaries, and 11 full evaluations × 40. [number] (verified: counted in the fake LM)
- **[agents] Ties keep the untouched program** — `best_score` starts at the default program's score and is replaced only by a strictly higher one (`mipro_optimizer_v2.py:592,855`). When every candidate scores 0.0, the "optimized" program is the input: 0 demos and the instruction „Given the fields `context`, `question`, produce the fields `answer`." The repo's own logs show the same:
  - the cache-bypassed 29-row eval: zero-shot and compiled prompt tokens both 6466 (`eval_metrics.jsonl:1`);
  - the 50-row run on 2025-09-26: the compiled pass took 0.04 s with `usage: {}`, meaning every request was a cache hit on the zero-shot pass (`eval_metrics.jsonl:2`).

  [number] (verified offline: `same instruction as zero-shot: True`, `demos 0`)
- **[agents] What `score`, `total_calls` and `prompt_model_total_calls` mean** — `best_program.score` is the best full-valset score; both logged compile runs record 0.0 (`compile_metrics.jsonl:1-2`). `total_calls` and `prompt_model_total_calls` are set to 0 in `__init__` and never incremented, in 3.0.3 and in 3.3.1, so they are dead counters. `mipro_optimizer_v2.py:98-99,678-679` [trap] (verified: grep of both versions; offline run gives 0/0 after 482 calls) → here: baseline.py, pairs.py
- **[agents] Bootstrapping yields nothing when the metric never passes** — 3.3.1 printed „Bootstrapped 0 full traces after 9 examples for up to 1 rounds, amounting to 10 attempts." per set. With exact match on sentence answers, demo candidates can only be labeled demos. [number] (verified offline)
- **[agents] `requires_permission_to_run` is removed** — `False` logs a deprecation warning. `True` raises `ValueError`: „User confirmation is removed from MIPROv2. Please remove the 'requires_permission_to_run' argument." Same in 3.0.3. `mipro_optimizer_v2.py:128-136` [api]
- **[agents] Parameters that cannot be combined** — With `auto=None`, both `num_candidates` and `num_trials` are required. With `auto` set, passing either one raises „If auto is not None, num_candidates and num_trials cannot be set…". `minibatch=True` with `minibatch_size > len(valset)` raises „Minibatch size cannot exceed the size of the valset." `mipro_optimizer_v2.py:153-170,214-215` [api]
- **[agents] Data size against the repo's own docs** — The docs say „~28 doc-grounded Q/A pairs" (`dspy_optimize/AGENTS.md:7`, `README.md:74`), „29-question set" (`dspy_optimize/AGENTS.md:17`, `plan.md:57`) and „28 doc-grounded Q/A pairs" (`README.md:56`). The file has held 50 rows since `8cc8eaf`. Rows per commit: 15 (`706da7f`) → 25 → 28 → 29 → 46 → 50. The last compile record logs `"train_examples": 50` (`compile_metrics.jsonl:2`). Nothing re-derives the count. [number] (verified: `git show <c>:…jsonl | grep -c .` per commit)
- **[agents] Data size against MIPROv2 guidance** — With 50 rows, light mode trains on 10 examples against 4+4 demo slots and 6 demo-set candidates. The target's toolchain note puts MIPROv2 at „100+ / 50+ examples" (`kohaerenzprotokoll/Plan/concept/dspy-toolchain_2026-09-23.md:351`); dspy-agent-skills says „100–500 for MIPROv2-style bootstrapping" (`dspy-agent-skills/skills/dspy-evaluation-harness/SKILL.md:74`). [claim] (the dspy.ai figure was not re-fetched)
- **[agents] The program is compiled for one model and served by another** — Compile and eval hardcode `dspy.LM("openai/gpt-4o-mini", api_key=…, temperature=0)` in chat mode (`compile_rag.py:71`, `eval/harness.py:102`). The runtime serves the artifact through `configure_once()`: `OPENAI_MODEL` defaulting to `gpt-5`, Responses API, temperature 1.0 (`dspy_config.py:143-199`). The docs claim „LM: configured via `OPENAI_API_KEY` (and optional `OPENAI_MODEL`)" (`dspy_optimize/AGENTS.md:14`). [trap] (verified: read; `LM constructed with: (('openai/gpt-4o-mini',), {'temperature': 0})` offline) → here: pairs.py (compile and score on the model you will run)
- **[agents] Optimizers named in the docs but never used** — GEPA („Phase 8 — Advanced Optimization (Stretch)", `plan.md:75-77,100`) and BootstrapFinetune (`README.md:81`). Only MIPROv2 is ever called; GEPA and BootstrapFinetune appear only as corpus text in `skills/rag/search.py:58-75`, and `dspy.Evaluate` is never used. [number] (verified: grep of all `.py` files)

## MET

- **[agents] `answer_exact_match`** — The signature is `answer_exact_match(example, pred, trace=None, frac=1.0)`; it returns a bool. Gold may be a str or a list[str]. `frac < 1.0` switches to "max token-F1 ≥ frac". `dspy/evaluate/metrics.py:285-316` [api]
- **[agents] DSPy EM and the harness EM are the same normalisation** — `normalize_text` = Unicode NFD → lower → strip punctuation → remove articles `a|an|the` → collapse whitespace (`dspy/evaluate/metrics.py:87-124`). The harness's `_normalize` is identical minus the NFD step (`eval/harness.py:45-72`). So „Align compile metric with eval normalization (SQuAD‑style EM)" (`plan.md:97`) was already true. [api] (verified: read both)
- **[agents] Exact match cannot score these answers** — Gold answers run a median of 6 normalized tokens, maximum 17. 28 of 50 have ≥ 6 tokens; 16 of 50 have ≤ 3. Logged EM: zero-shot 3/29 and compiled 3/29 (`eval_metrics.jsonl:1`); 3/50 and 3/50 (`eval_metrics.jsonl:2-3`). The handoff says so: „Likely due to dataset vs. metric mismatch" (`handoff_issue20.md:16`). [number] (verified: normalized gold lengths computed) → here: pairs.py (decisions, not strings)
- **[agents] Unused remedies** — `answer_exact_match(..., frac=0.5)` would accept token-F1 ≥ 0.5. The docs suggest „For longer outputs, consider switching the compile metric to F1/ROUGE" (`dspy_optimize/AGENTS.md:28`). The repo's own Context7 snapshot recommends `dspy.MIPROv2(metric=dspy.SemanticF1(), auto="medium")` for RAG (`data/docs/context7/dspy_optimization.md:7`). None of these is used. [recipe]
- **[agents] Eval harness shape** — It loads the JSONL and runs two sequential loops, zero-shot `ChainOfThought` and the compiled artifact, each inside `dspy.track_usage()`. It computes `em_rate = hits/n`, and if the artifact is unavailable the compiled `em_rate` is `None`. The record also holds duration, usage, git and cache flags. There is no `dspy.Evaluate` and no threads, so its usage numbers are complete. `eval/harness.py:75-85,106-188` [pattern] (verified: 750 tracked = 50 calls × 15 offline)
- **[agents] Default drift thresholds, exactly** (`dspy_optimize/baselines/thresholds.py:49-86`):

  | script | metric | rule | env override | severity |
  |---|---|---|---|---|
  | `eval_harness` | `compiled_em_rate` | min 0.05 | `BASELINE_COMPILED_EM_MIN` | fail |
  | | | max_drop 0.03 | `…_MAX_DROP` | fail |
  | | | max_pct_drop 0.35 | `…_MAX_PCT_DROP` | fail |
  | | `delta_em_rate` | min 0.0 | `BASELINE_COMPILED_DELTA_MIN` | warn |
  | | `compiled_total_tokens` | max_pct_increase 0.5 | `BASELINE_EVAL_TOKEN_MAX_PCT_INCREASE` | warn |
  | `compile_rag` | `total_tokens` | max_pct_increase 0.75 | `BASELINE_COMPILE_TOKEN_MAX_PCT_INCREASE` | warn |

  [number]
- **[agents] Rule evaluation order** — absolute `min`, then `max`, then relative to the previous run: `max_drop`, `max_pct_drop`, `max_pct_increase`. The first hit returns, so a rule reports at most one finding. Status is the worst severity across rules. `thresholds.py:150-214` [api]
- **[agents] An unmeasured metric passes** — `if current_value is None: return None`: the rule is skipped and nothing is reported (`thresholds.py:186-187`). With DSPy 3.3.1 the compiled program never loads, `compiled_em_rate` is `None`, and the only fail rule is skipped. Offline run output: „Zero-shot EM: 0/50 … No compiled artifact found. … Baseline monitor status: ok". [trap] (verified offline) → here: baseline.py ("could not check" is a status, P23)
- **[agents] "Previous" means the last run, whatever it was** — `previous = store.latest(summary.script)` (`monitor.py:64`). The run is always stored, even when it failed (`monitor.py:85`), so a failed run becomes the next baseline. A decline of 0.03 or less per run never trips `max_drop` (the test is strictly `delta > max_drop`). The percentage checks are skipped when the baseline is 0 (`thresholds.py:202-203,208`). [trap] → here: baseline.py (compare to a floor and a pinned best, not to "last")
- **[agents] Token-increase rules can never fail** — A rule with `severity="fail"` is downgraded to `warn` on `max_pct_increase` (`thresholds.py:211`). [trap]
- **[agents] The compile score is never checked** — The primary metric is `program_score` (`store.py:20-23`), but `compile_rag` has only the `total_tokens` warn rule (`thresholds.py:79-86`). A compile scoring 0.0 is "ok". [trap] (verified offline: „Baseline monitor status: ok")
- **[agents] The thresholds file can switch the gate off** — `BASELINE_THRESHOLDS_PATH` JSON has the shape `{script: [{metric, min|min_value, max|max_value, max_drop, max_pct_drop, max_pct_increase, severity, note}]}`. Invalid JSON falls back to the defaults. A non-dict, or `{}`, yields no rules, so everything is "ok". Rules without `metric` are dropped silently. `thresholds.py:91-138`. The test `test_empty_thresholds_disable_checks` asserts that `em_rate` 0.0 with `{}` is `"ok"` (`tests/test_baselines_monitor.py:164-179`). [trap]
- **[agents] Monitor exit codes** — 2 on `fail`. 1 on `warn`, but only with `--treat-warn-as-error`. Unknown statuses (`missing`, `unknown`) rank as warn (`order.get(status.lower(), 1)`). `--report-only`, `--skip-compile`, `--skip-eval`; `--keep-cache` stops the monitor forcing `BASELINE_DISABLE_CACHE=1`. `scripts/baseline_monitor.py:31-33,79-116` [api]
- **[agents] Derived metrics** — `delta_em_rate = compiled − zero_shot` (`None` if either is missing). Token totals are summed across every LM key in `usage`, so prompt-model calls count too. `store.py:224-258,285-321` [api]

## DATA

- **[agents] Dataset format** — JSONL with keys `context`, `question`, `answer`; there are no `id`s, although the docs say „`id` (optional)" (`dspy_optimize/AGENTS.md:8`). It is loaded as `dspy.Example(**ex).with_inputs("context", "question")`. `compile_rag.py:39-45` [recipe] (verified: 50 rows, one key set)
- **[agents] Hand-written contexts** — Contexts are single sentences of 70–237 characters that already contain the answer; answers are often full sentences. It is a reading-comprehension set, not retrieval. `dspy_optimize/datasets/qa_agno_dspy.jsonl` [number] (verified)
- **[agents] Row order decides the split** — Appending new domains at the end of the file sends them all to MIPROv2's valset (OPT). [trap] → here: trainset.py
- **[agents] Offline docs budget** — „Only small `.md` or `.txt` files (3–10 short pages total)" (`data/docs/AGENTS.md:10`); „Size budget: keep total under ~50–100 KB for quick loads." (`data/docs/AGENTS.md:22`). No binaries, PDFs, scraped dumps or secrets. Subfolders separate provenance: `context7/` (vendor docs snapshotted through the Context7 MCP), `external/`, `internal/`. [pattern]
- **[agentic-rag] Ingestion recipe** — Zerox vision OCR (`model="gpt-4o-mini"`) over `documents/DBMS Notes.pdf` (26 pages). Then `RecursiveCharacterTextSplitter(separators=["\n\n","\n","##","#"," "], chunk_size=1024, chunk_overlap=150)`, `text-embedding-3-large` (3072 dims, COSINE), `recreate_collection` on every run, batches of 100, `uuid4` point ids, payload `{"text": chunk}`. `indexing.py:58-121` [recipe] (read; not run, needs Docker and keys)

## RAG

- **[agents] In-memory corpus search** — 15 hard-coded snippets (`skills/rag/search.py:6`). The score is the number of query words that occur as substrings (`sum(1 for w in q if w in text)`, so `"a"` matches everything). There is no relevance floor: top-k is returned even at score 0, and ties go to the higher index (`scores.sort(reverse=True)`). Output format is `"Title: text"`. `search.py:116-129` [pattern]
- **[agents] Offline docs loader** — Chunks split on `"\n\n"` and are truncated, not split, at 1200 characters (`chunk_utils.py:16,28-56`). The label is `domain/file_stem` (`offline_docs.py:85-93`). The in-process cache is keyed by `(signature, root)`. The signature is `sha1("rel:mtime_ns:size" …)[:12]` plus the sanitized `OFFLINE_DOCS_CACHE_TAG`; the values `missing` and `empty` are special. Every `offline_search` call re-stats every file to recompute the signature. `offline_docs.py:39-82,96-154` [pattern]
- **[agents] `mini_report_web` assembly** — LanceDB hits first, then keyword passages until `MINI_REPORT_WEB_TOPK` (default 6). Passages are deduplicated by exact string, joined with `"\n\n"` as `context`, and the answer gets a `Sources:` footer built from the passage labels. `tools/mini_report_web_tool.py:29-100` [pattern]
- **[agents] The two retrieval paths label the same chunk differently** — LanceDB builds `f"{domain}/{title}"` with `title = stem.replace("_"," ")`; the offline path uses `domain/stem`. The same chunk arrives as `context7/dspy optimization: …` and `context7/dspy_optimization: …`, the exact-string dedupe misses it, and it can appear twice in the context and footer. `lancedb_store.py:529-535`, `chunk_utils.py:104`, `offline_docs.py:88-93` [trap]
- **[agents] LanceDB schema and upsert** — Columns: `chunk_id, doc_path, domain, title, chunk_index, content, content_tokens (tiktoken cl100k_base or None), content_hash, source_signature, embedding fixed_size_list<float32, dim>`, with dim 1536 from `LANCEDB_EMBED_DIM`. `chunk_id = sha1(doc_path::chunk_index::content_hash)`. Upsert is `merge_insert("chunk_id").when_matched_update_all().when_not_matched_insert_all()`. Stale rows are deleted in batches of `LANCEDB_DELETE_BATCH=750` with SQL-escaped `IN`. Embeddings are checked for dimension and NaN. `skills/rag/lancedb_store.py:361-406,561-568,651-702` [recipe] (verified: ingest ran with the fake embedder)
- **[agents] "Hybrid" scoring does not normalise** — Vector search takes `limit*3` rows with score `1/(1+L2 distance)` ∈ (0,1]. FTS takes `limit*3` rows with the raw `_score`, which is BM25 and unbounded. The final score is `v_weight*vec + s_weight*fts`, both weights 1.0 by default. `LANCEDB_SEARCH_TYPE=VECTOR|FULLTEXT|HYBRID` forces 1/0 or 0/1. `LANCEDB_SCORE_THRESHOLD` defaults to 0. `lancedb_store.py:453-536` [pattern] (verified: vector scores 0.5/0.5/0.02; the native FTS index gave BM25 0.875/0.693 on a two-chunk corpus) → here: graphrag.py (normalise before fusing; relevance floor)
- **[agents] FTS is silently absent, so "hybrid" means vector-only** — `ensure_fts_index` calls `create_fts_index(["content","title"], use_tantivy=True)`, which needs `tantivy` and `pylance`; neither is in `requirements.txt`. The `ImportError` is logged at DEBUG („Skipping FTS index creation … Tantivy is unavailable" / „The lance library is required … `pip install pylance`"). `hybrid_search` then catches the FTS `RuntimeError`, also at DEBUG („Cannot perform full text search unless an INVERTED index has been created"). The design doc claims „installing `lancedb` already pulls it" (`docs/designs/lancedb_offline_corpus.md:61`). The native index (`create_fts_index("content")`, not tantivy) works out of the box. `lancedb_store.py:428-450,496-501` [trap] (verified with the period deps, with and without tantivy)
- **[agents] One changed mtime re-embeds the whole corpus** — `source_signature` is the corpus-wide mtime/size digest, stored on every row and compared in `_record_changed` (`lancedb_store.py:264,642`). Touching one file with unchanged content flagged 3 of 3 chunks `new_or_updated`, so every chunk is re-embedded (paid). This contradicts „The pair `(doc_path, content_hash)` helps skip re-embedding when content is unchanged even if mtimes shift." (`docs/designs/lancedb_offline_corpus.md:39`). The test monkeypatches the signature to a constant and so hides it (`tests/test_lancedb_ingest.py:33`). [trap] (verified)
- **[agents] The runtime signature guard, and where it stops checking** —
  - The guard runs only when `ENABLE_LANCEDB_RETRIEVAL ∈ {1,true,yes,on}`; note that `t` and `y` are not accepted, although the other flags accept them (`lancedb_runtime.py:39-40`).
  - An empty table, a missing dependency, a failed `ensure_table` or a failed search returns `[]`, and the caller falls back to keyword search.
  - A mismatch between the offline-docs signature and the table's `source_signature` set triggers one forced reload; if it still mismatches, the result is `ready=False, reason="signature mismatch"` (`lancedb_runtime.py:143-199`).
  - **The guard is skipped when the offline docs are missing or empty** (`offline_sig` is `None`, `:150-152`). `tests/test_lancedb_runtime.py:86-100` pins "ready when offline docs missing".
  - State is cached per process until `reset()` (`:80,216-221`), so later doc changes are not re-checked.

  [pattern] (verified: the three runtime tests pass with the period deps) → here: Wiki/index.json derivation guard
- **[agents] Research workflow retrieval** — Up to `MINI_REPORT_WEB_TOPK` offline passages, then keyword passages until about 8, deduplicated by string; sources are the labels before `:`. `workflows/research_report.py:128-158` [pattern]
- **[agentic-rag] Pipeline shape** — condense (if history) → classify intent → route → *inside each agent*: expand query → retrieve → rerank → generate. SimpleRAG reranks to k=3 and ComparativeRAG to k=7. The retriever uses k=20 per query over at most 4 queries (3 rephrasings plus the original), so up to about 80 pooled passages, deduplicated with `list(dict.fromkeys(passages))`. `agents.py:18-59`, `data_modules.py:33,42-69`, `main.py:113-153` [pattern]
- **[agentic-rag] Query expansion puts its instructions in the input field** — `rephrase_prompt = f"Generate 3 diverse but related questions … Separate them with a semi-colon. Original Query: {query}"` is passed as `question` to `ChainOfThought("question -> rephrased_queries")` and split on `;`. If the LM uses newlines instead, the result is one long "query". `data_modules.py:46-48` [trap]
- **[agentic-rag] The "reranker" is a second bi-encoder** — It embeds the passages and the query with Gemini `models/embedding-001` and ranks by dot product. On any exception it falls back to `passages[:k]`. The pool is built by `for query in set(queries)`, whose iteration order is hash-randomized per process, so the fallback context is not reproducible. `data_modules.py:54,83-98` [trap]
- **[agentic-rag] Multi-step discards the evidence** — The decomposer outputs `sub_questions` as one `;`-separated string; each sub-question goes to SimpleRAG; the synthesizer answers from `qa_pairs`. The returned `context` is `[qa_pairs]`, a single string of Q&A pairs, and the retrieved passages are gone. Offline API output: `'context': ['Sub-Question: What is A?\nAnswer: fake answer\n\nSub-Question: What is B?\nAnswer: fake answer\n\n']`. `agents.py:73-90` [trap] (verified: `TestClient`) → here: P13, graphrag.py returns quotations only
- **[agentic-rag] LM calls per route** — Factual 3 and Comparative 3 (classify, rephrase, answer). Multi-step with n sub-questions: 3 + 2n, so 7 for n = 2. Add 1 when `chat_history` is present. Each retrieval also makes up to 4 OpenAI embedding calls and 2 Gemini embedding calls. [number] (verified: fake retriever gave 2/2/5 LM calls, plus the rephraser call per retrieval read from `data_modules.py:47`)
- **[agentic-rag] Response contract** — `QueryResponse{answer: str, context: list[str], intent: str}` always returns the passages beside the answer, but with no document or line attribution. `main.py:107-110` [pattern]

## AGENT

- **[agents] A DSPy program as an Agno tool** — Plain `run_mini_report(input_data: str) -> str` functions are registered with `Toolkit.register(fn, name=...)`; the function docstring is the tool description the agent LLM sees. `f.stop_after_tool_call = True; f.show_result = True` returns the DSPy output directly with no second LLM turn. `tools/mini_report_toolkit.py:26-52` [pattern]
- **[agents] Configuring DSPy per worker** — Each tool calls `configure_once()` and `get_rag_program()` before predicting (`tools/mini_report_tool.py:27-28`). `build_agent()` calls `configure_once()` inside `try/except: pass` (`apps/agentos_api/app.py:222-226`), so the API starts with no key and fails at the first tool call. [pattern]
- **[agents] Two model stacks, configured apart** — The Agno agent's model is `OpenAIResponses(id=model_id)` for reasoning models and `OpenAIChat` otherwise (`app.py:300`). DSPy calls go through LiteLLM (`dspy_config.py`). Only DSPy calls reach `dspy.track_usage`. The tool logger reads `result.metrics`, which a str-returning DSPy tool never has (`observability.py:392-401`), so DSPy token usage at runtime is never logged although `track_usage=True`. [pattern]
- **[agents] Agent configuration** — `reasoning=True` with a custom `reasoning_agent` (tools `SafeReasoningToolkit` think/analyze; `reasoning=False`, `parse_response=False`, `structured_outputs=False`, `use_json_mode=False`). Also `enable_user_memories`, `enable_session_summaries`, `cache_session`, `add_history_to_context`, and `num_history_runs=3` from `AGNO_NUM_HISTORY_RUNS`. `tool_hooks=[tool_logging_hook]`. `app.py:296-351`. `SafeReasoningToolkit` tolerates a non-dict `session_state` (`tools/safe_reasoning_toolkit.py:37-43`). [api]
- **[agents] Tool hook contract** — `hook(function_name, function_call, arguments)` must call `function_call(**arguments)` and return its result. Retrieval metadata reaches the hook through a ContextVar deque (`record_tool_metadata`, then `_consume_tool_metadata`). `observability.py:356-425` [pattern]
- **[agents] Agno workflow with DSPy steps** — `Workflow(steps=[callables], input_schema=PydanticModel(extra='forbid'))`. Steps pass JSON strings through `step_input.get_last_step_content()`. `workflows/research_report.py:121-295`, `workflows/mini_report.py:29-50` [pattern]
- **[agents] The critique is never applied** — `critique_step` writes `state["critique"] = {notes, edits}` (`research_report.py:219-222`). `finalize_step` never reads them; it truncates the brief to 3 sentences and pads the outline with 4 default bullets („- Context", „- Key drivers", …) (`:238,265-277`). The outline is requested by stuffing an instruction into the QA program's `question` field (`:111-118`), a program optimised for QA. [trap] → here: any critique→repair pattern must consume the critique
- **[agents] MCP composition** — `MultiMCPTools(commands, urls, urls_transports, env, allow_partial_failure=True)` built from `MCP_COMMANDS` (split on newline, `;` or `,`), `MCP_URLS`, `MCP_SSE_URL` (appended), `MCP_URL_TRANSPORTS` and `MCP_DEFAULT_URL_TRANSPORT`. A subclass swallows `ValueError` on `connect()` and disables itself (`_disabled=True`). `app.py:79-161` [pattern]
- **[agentic-rag] Classify-then-route orchestrator** — `self.classifier = dspy.Predict("question -> intent", n=1)` is called with `question=f"Classify the user's question. Choices: Factual, Comparative, Multi-step. Question: {question}"`. The choices live only in the input text; the system prompt declares `` `intent` (str) ``. Routing is `if "Comparative" in user_intent … elif "Multi-step" in user_intent … else SimpleRAG`. `agents.py:101-127` [pattern] (verified: prompt printed offline)
- **[agentic-rag] Conversational memory** — `dspy.ChainOfThought("chat_history, new_question -> standalone_question")` runs before the orchestrator whenever history is present; history is rendered as `"role: content"` lines. `main.py:113,134-139` [pattern] (verified: `TestClient` with history returned 200)
- **[agentic-rag] An agent used as a tool** — `MultiStepRAG` holds a `SimpleRAG` instance and calls it once per sub-question. `agents.py:64-83` [pattern]

## PROD

- **[agents] Turning caches off for measurement** — If `BASELINE_DISABLE_CACHE` is truthy, call `configure_cache(enable_disk_cache=False, enable_memory_cache=False)` before `dspy.configure(...)`, so logged token counts are real calls (`compile_rag.py:62-73`, `eval/harness.py:94-104`). `scripts/baseline_monitor.py:93-95` sets it unless `--keep-cache`. „Set `BASELINE_DISABLE_CACHE=1` whenever regenerating baseline JSONL to avoid stale usage data." (`handoff_issue20.md:26`) [recipe] → here: lmrun.py (`cache=False` already)
- **[agents] `track_usage` loses every worker thread's usage** — `ParallelExecutor` gives each worker thread a `copy.deepcopy` of the usage tracker, and nothing merges them back. „Usage tracker needs to be deep copied across threads so that each thread tracks its own usage" (`dspy/utils/parallelizer.py:126-131` in 3.3.1; `:91-93` in 3.0.3). Measured offline:
  - `Evaluate(num_threads=8)` inside `track_usage()` recorded `{}` for 50 calls; `num_threads=1` and a plain loop both recorded 750 = 50 × 15;
  - the repo's `compile_rag.main()` printed „Compile usage (prompt=510, completion=255, total=765)" against 482 true calls (7230 tokens).

  So the repo's committed compile usage (24,053 and 35,699 tokens) counts main-thread calls only. [trap] (verified on 3.3.1; source identical in 3.0.3) → here: lmrun.py (count per call), baseline.py
- **[agents] What gets recorded, and what does not** — prompt, completion and total tokens with their `*_details`, per LM key, plus duration, git commit and branch, and cache env flags (`compile_rag.py:96-118`, `eval/harness.py:154-188`, `compile_metrics.jsonl`). No USD cost is recorded, although DSPy history carries `cost` per call (API). [number]
- **[agents] Baseline store** — SQLite by default at `dspy_optimize/baselines/baselines.db` (relative to the CWD), with `PRAGMA journal_mode=WAL`. `BASELINE_DB_URL` accepts `sqlite:///rel`, `sqlite:////abs`, `sqlite:///:memory:` or `postgresql://`; Postgres needs psycopg ≥ 3.1. Table `baseline_runs(script, run_kind, created_at TEXT, git_*, primary_metric, primary_value, metrics_json, payload_json, threshold_config_json, drift_status)`. `latest()` orders by `created_at DESC, id DESC`. `store.py:19-212` [recipe] (verified: store tests pass)
- **[agents] The JSONL is committed and the DB is not, so CI never has a baseline** — `.gitignore:15-16` ignores `dspy_optimize/artifacts/` and `dspy_optimize/baselines/*.db`, while the JSONL files are tracked. The monitor reads the DB, not the JSONL. The CI workflow has no cache or artifact step, so every CI run starts with no previous row, and **relative checks can never fire in CI**; only the 0.05 floor on `compiled_em_rate` can. `.github/workflows/baseline-monitor.yml:18-44` [trap]
- **[agents] CI gate on a secret** — `if: ${{ secrets.OPENAI_API_KEY != '' }}` sits at job level (`baseline-monitor.yml:20`). The `secrets` context is not available in `jobs.<id>.if`, so the workflow is invalid or the job never runs. Triggers: weekly cron, push to main, PRs touching `dspy_optimize/**` and similar. [claim] (per GitHub Actions context-availability rules; not run)
- **[agents] Git metadata capture writes to stderr** — `current_git_metadata()` runs `git rev-parse` and prints „fatal: not a git repository" to stderr outside a checkout; it records `None` (`dspy_optimize/baselines/utils.py:26-41`). [api] (verified)
- **[agents] Logging shape** — JSON to stdout by default. `RUN_LOG_LEVEL`, `RUN_LOG_FORMAT=json|text`, `RUN_LOG_SINK=stdout|stderr|<path>`, `RUN_LOG_INCLUDE_ARGUMENTS` (default off, so tool arguments are not logged), `RUN_LOG_PROPAGATE`. Loggers: `dspy_agents.{request,tool,run,weave,baseline}`. The request middleware honours `x-request-id` or mints a uuid4 and sets `X-Request-ID` and `X-Trace-ID`. A ContextVar `RunLogContext` carries request, run, session, user and trace ids. A ring buffer of the last 20 events (`RUN_LOG_BUFFER_SIZE`) feeds `runtime_diag`. The baseline status is attached to every log line and cached 60 s (`RUN_LOG_BASELINE_REFRESH_SECONDS`). `apps/agentos_api/observability.py:78-503` [pattern] (verified: 8 observability tests pass with period and current deps)
- **[agents] Instrumenting an agent without changing its shape** — `wrap_agent` replaces `agent.run/arun`, generates `run_id` and `trace.bound`, logs `run.started/completed/failed`, and attaches `metadata.trace` to results and to stream events that have a `metadata` attribute. It keeps coroutine versus async-generator shape by checking `inspect.iscoroutinefunction` (in Agno 2.0.11, `Agent.arun` is neither). `observability.py:633-770` [pattern] (verified: `test_wrap_agent_streaming_injects_trace` passes)
- **[agents] Weave re-wraps `arun` as a coroutine** — `maybe_enable_weave` replaces `arun` with `async def traced_arun(...): return await original_arun(...)` (`observability.py:820-827`). For streaming runs `original_arun` returns an async generator, and awaiting it raises `TypeError`. So `ENABLE_WEAVE_TRACE=1` breaks streaming, undoing the shape preservation. [claim] (reasoned from code and the Agno 2.0.11 `arun` shape; weave not installed)
- **[agents] Design doc and implementation disagree** — The design promises `run.cache_hit`, `retrieval.summary`, `tool.call.started`, a 100-character input preview and `token_usage` in `run.completed` (`docs/designs/run_logging_tracing.md:31-38`). The code emits `tool_call.completed/failed` and a 120-character preview, and none of the three promised event names exists anywhere in the Python sources. `run.completed` carries Agno's own `result.metrics` dict, i.e. the Agno model's tokens, not DSPy's; the tool logger's `token_usage` filter only fires when a tool returns an object with `.metrics`, which the str-returning DSPy tools never do (`observability.py:392-401,405-422,515-530,599-613`). [trap] (verified: grep of all `.py` files)
- **[agents] Secrets reach every MCP subprocess** — `tool_kwargs = {"env": dict(os.environ)}` passes the whole environment, `OPENAI_API_KEY` included, to every stdio MCP server started from `MCP_COMMANDS`. `app.py:119` [trap]
- **[agents] The demo MCP server does not start** — `mcp.run(transport="sse", host="0.0.0.0", port=8001)` raises `TypeError: FastMCP.run() got an unexpected keyword argument 'host'`; in the official SDK host and port are `FastMCP(...)` constructor arguments. The tool is also an unauthenticated URL fetcher bound to 0.0.0.0 (SSRF). `mcp/server.py:11-24` [trap] (verified: mcp 1.12.4 and the current version)
- **[agents] `runtime_diag` redacts by allow-list** — It prints only a named list of env vars, LM model, model_type, `max_*`, `reasoning`, memory stats, recent events and the baseline status. `tools/runtime_diag_tool.py:124-160,257-301` [pattern]
- **[agents] Two cache layers** — Agno toolkit results are cached for `AGNO_CACHE_TTL=3600` s in `~/.cache/agno_tools/<tag>__docs-<sig>__prog-<sig>`; components are sanitized to `[A-Za-z0-9_-]`, and an empty result becomes `hash-<sha1[:12]>`. The DSPy LM cache lives in `.cache/dspy/<DSPY_CACHE_TAG>__<artifact sig>`. `app.py:232-282`, `dspy_config.py:105-112` [pattern]
- **[agentic-rag] Error handling** — A global FastAPI handler maps `litellm.exceptions.RateLimitError` to HTTP 503 with a JSON message. The LM, retriever, reranker and agents are built once in `@app.on_event("startup")` (deprecated in FastAPI in favour of lifespan; it still works on 0.141.1) and stored in `app.state.orchestrator`. Startup raises `ValueError` if any of 4 env vars is missing. `main.py:38-94` [pattern] (verified: `TestClient`)
- **[agentic-rag] Usage logging through `lm.history[-1]`** — `usage = dspy.settings.lm.history[-1]['response'].usage` is logged with `print`, and every failure becomes „[USAGE LOG] Could not parse usage data…". `agents.py:26-31,51-56` [pattern]; defects under TRAP.

## TEST

- **[agents] RecorderLM** — A plain class, not a `dspy.BaseLM`, that records constructor `args`/`kwargs` and exposes `model` and `model_type`. It is monkeypatched in for `cfg.dspy.LM`, with `cfg.dspy.configure` stubbed. Assertions are made on the kwargs, so no LM is ever built: responses path for `gpt-5`, chat path for `gpt-4o-mini`, forced chat that still has temperature 1.0 and ≥ 16000 tokens. `tests/test_dspy_config.py:13-122` [pattern] (verified: 3 passed on DSPy 3.3.1 in 0.28 s) → here: lm_fixture.py, check_dspy_surface.py
- **[agents] RecorderLM cannot see what DSPy does with the kwargs** — Real 3.3.1 construction accepts them, but renames `max_tokens` and collapses the two token caps (API; TRAP `OPENAI_MAX_OUTPUT_TOKENS`). Pair a recorder with an offline real `dspy.LM(...)` construction plus a request-conversion assertion. [recipe] (verified)
- **[agents] "Unit" tests with real side effects** —
  - The tests write `os.environ[...]` directly rather than through `monkeypatch.setenv`, so `OPENAI_API_KEY="test-key"`, `OPENAI_MODEL` and others leak into later tests (`test_dspy_config.py:24-28,60-62,93-96`).
  - `configure_once()` calls the real `dspy.configure_cache`, which creates `.cache/dspy/missing/000…015/cache.db` in the CWD.
  - The cleanup in `test_caching.py:103` sets a nonexistent `_PROGRAM_CACHE_SIGNATURE`; the real memo is `_PROGRAM_CACHE_SIGNATURES`.
  - Importing `compile_rag` creates `dspy_optimize/artifacts/` (`compile_rag.py:27`).

  [trap] (verified: directories appeared in the scratch copy)
- **[agents] Call-order test** — It patches `module.configure_cache` and `module.dspy.cache.reset_memory_cache`, and makes `module.dspy.configure` raise `RuntimeError("stop after configure")`, then asserts the cache toggle happened before configure. `tests/test_baseline_cache_toggle.py:13-42`. **It needs a non-empty `OPENAI_API_KEY`**; without one it fails with „Actual message: 'OPENAI_API_KEY not set'" and relies on another test leaking the key. [pattern+trap] (verified: fails keyless, passes with `OPENAI_API_KEY=test-key`)
- **[agents] Stubs installed only when the import fails** — `conftest.py` puts a `dspy` stub (`configure`, `LM`, `ChainOfThought` only) and an `agno` stub tree into `sys.modules` if the real import fails (`tests/conftest.py:15-159`). The stub lacks `configure_cache`, `settings`, `cache`, `load`, `track_usage`, `agno.db.base`, `agno.memory`, `agno.utils`, and `Toolkit(cache_*)`, and `python-dotenv` is not stubbed. [trap]
- **[agents] Suite results, measured** (`-m "not integration"`, 44 collected, 1 deselected):

  | environment | key | result |
  |---|---|---|
  | dspy 3.3.1 + dotenv + pytest only | none | **0 run** („Interrupted: 4 errors during collection"); with `--continue-on-collection-errors` 20 passed / 6 failed / 4 errors |
  | commit-date deps (dspy 3.0.3, agno 2.0.11, lancedb 0.24.3) | none | 40 passed / 3 failed, all 3 from the missing key |
  | commit-date deps | fake | **43/43** |
  | dspy 3.3.1 + agno 2.0.11 | fake | 40 passed, 1 collection error: `ImportError: numpy._core.multiarray failed to import` in the lancedb test — the DSPy lazy-numpy trap (TRAP), because `conftest.py` imports dspy before lancedb/pyarrow |
  | dspy 3.3.1 + agno 3.0.11 | fake | 36 passed / 1 failed / 2 errors: `Agent.__init__() got an unexpected keyword argument 'reasoning'` (Agno API drift; `agno` unpinned, `requirements.txt:1`) |

  [number] (verified)
- **[agents] The suite stays green while compiled programs stop loading** — No test loads a real artifact through `get_rag_program()`, so the 3.1.0+ `dspy.load` break passes the whole suite. [trap] (verified: 40 passed on dspy 3.3.1) → here: check_dspy_surface.py
- **[agents] Integration gate** — `pytestmark = pytest.mark.integration`. The test skips unless `import dspy` works and, after `load_dotenv()`, the key matches `^sk-[A-Za-z0-9_-]{20,}$` and is not `"test-key"` (`tests/test_integration_e2e.py:11-37`). `pytest.ini` only registers the marker, with no `addopts`, so a plain `pytest` runs it when a key is present. OpenRouter-style keys (`sk-or-v1-…`) match the regex. [trap] (verified: regex on a synthetic `sk-or-v1-` string)
- **[agents] Offline CLI test** — The subprocess copies `os.environ` and removes `OPENAI_API_KEY` before running `ingest_lancedb_offline_docs.py --dry-run` (`tests/test_lancedb_ingest.py:99-108`). The fake embedder is `[float(len(text)+idx), 0, 0, 0]` (`:12-20`). Note that `--dry-run` still creates the table and writes `manifest.json`. [pattern]
- **[agentic-rag] No tests at all** — There is no test directory and no fixture. [claim]

## PAT

- **[agents] Configure once, with double-checked locking** — A module-level `_CONFIGURED` flag plus `threading.Lock`; `_configure_dspy_cache` is guarded the same way; the program is memoised in `_PROGRAM_CACHE`. `dspy_config.py:18-24,89-99,127-135,213-226` [pattern]
- **[agents] Signature-namespaced caches** — The artifact directory, the offline docs and the Agno toolkit cache are each keyed by `sha1(rel path + mtime_ns + size)[:12]`, plus a manual `*_CACHE_TAG`, so a changed input gets a fresh namespace. This is metadata, not content, and memoised per process. `dspy_config.py:45-86`, `offline_docs.py:39-82`, `app.py:250-272` [pattern]
- **[agents] Measure, persist, compare, verdict, after every run** — Each compile and eval appends a sorted-key JSONL record, logs to the DB, evaluates thresholds against the previous run, and prints `ok/warn/fail` with triggers. `compile_rag.py:96-138`, `eval/harness.py:154-208`, `baselines/monitor.py:20-86` [pattern] → here: baseline.py (floor + veto are better)
- **[agents] Record the anomaly in the handoff** — `handoff_issue20.md` lists Branch / Work Completed / Current Observations / Next Actions / Notes. Its observation: „MIPRO compile currently produces best score 0.0 and compiled EM 3/29, matching zero-shot performance." (`:16`) [pattern]
- **[agents] Degrading to deterministic output hides the degradation** — `_try_rag_answer` catches every exception, including a missing API key, and returns the first two sentences of the context as the "brief" (`workflows/research_report.py:67-91`). The output looks like a model answer. [pattern+trap]
- **[agentic-rag] Decompose, answer each, synthesize** — As implemented it merges the sub-answers into prose without attribution (RAG). [pattern]
- **[agentic-rag] A worked example kept as a versioned file** — `workflow.txt:1-99` is an ASCII diagram plus one sample query ("what about a unique key?") with its value at every step. It documents the intent; there is no measured trace. [pattern]

## SKILL

- **[agents] Per-directory `AGENTS.md` convention** — 10 files, 474 lines. Subdirectory guides open with `Scope` ("Applies to files under X/") and close with `References`; the middle sections vary (Overview / Modules|Tools|Workflows|Structure|Dataset / Usage / Configuration / Troubleshooting). The root guide opens with `## Quick Reminders` and has `Agent Map`, `Documentation Map` and `Contributor Checklist` (`AGENTS.md:3-84`). The stated rule is „Keep this root file concise; link to sub-guides for details." (`AGENTS.md:79`). [pattern] (verified: headings extracted from all 10) → here: job 4 (a description scaffold), check_skills.py
- **[agents] Measured drift in those guides** — At least eight of their statements are false for the code at `fde0dad`:
  1. dataset „~28" (`dspy_optimize/AGENTS.md:7`);
  2. compile LM „configured via … `OPENAI_MODEL`" (`:14`);
  3. „Latest EM benchmark … zero-shot 2/29 vs compiled 9/29" (`:17`); the only logged runs are 3/29 = 3/29 and 3/50 = 3/50;
  4. „pins `dspy-ai` to a version compatible with the compiled artifact" (`:32`); the range admits 3.1.0+;
  5. harness artifact path „override via `RAG_ARTIFACT_PATH`" (`eval/AGENTS.md:18`); `eval/harness.py:26` hardcodes it;
  6. `DSPY_CACHE_TAG` „sanitized to filesystem-safe characters" (`tools/AGENTS.md:54`); it is used raw;
  7. stubs „ensuring unit tests run in minimal environments" (`tests/AGENTS.md:12`); 0 tests run;
  8. MCP „defaults assume SSE when transport omitted" (`tools/AGENTS.md:55`) against „Streamable HTTP is the default transport" (`AGENTS.md:41`).

  [trap] (verified) → here: state.py --prose style checking
- **[agents] Docstrings are the tool descriptions** — Agno registers `run_mini_report` and its siblings, and each docstring is the description the agent model sees, e.g. „Answer a factual question with a 2-3 sentence brief using a tiny in-memory RAG + DSPy program." (`tools/mini_report_tool.py:18`). The agent's instructions list says when to pick each tool (`app.py:330-335`). This is the same role SKILL.md `description` plays for a ReAct agent. [pattern] → here: job 4

## TRAP

- **[agents] The compiled program is never used on DSPy ≥3.1.0, and nothing says so** —
  - `get_rag_program()` wraps `dspy.load(artifacts_path)` in a bare `except Exception` and falls back to zero-shot `dspy.ChainOfThought("context, question -> answer")` (`dspy_config.py:222-225`). On 3.3.1 it returned a fresh `ChainOfThought` with no `score` attribute and logged nothing, even at DEBUG.
  - `eval/harness.py:110-114` does the same and then prints „No compiled artifact found." (`:152`) although the artifact exists; it records `"available": false`.

  [trap] (verified offline on 3.3.1 with a real MIPROv2-saved artifact) → here: check_dspy_surface.py, any artifact loader (fail loudly; prefer JSON state)
- **[agents] `OPENAI_MAX_OUTPUT_TOKENS` does nothing on 3.3.1** — The repo passes both `max_tokens=20000` and `max_output_tokens=2048`. The converted Responses request carries `max_output_tokens: 20000`: the `max_tokens` value wins and the documented cap is dropped (`.env.sample:7`, `dspy_config.py:192`). [trap] (verified: `_convert_chat_request_to_responses_request` offline)
- **[agents] Three rules for "is this a reasoning model", disagreeing** —
  - `dspy_config.py:146` uses a prefix, `startswith(("gpt-5","o4","o3","o1"))`, commented „Detect reasoning models (prefix-based) to avoid substring false-positives".
  - `apps/agentos_api/app.py:230` uses substring `any(x in model_id …)`.
  - `dspy_config.py:190` uses substring `"gpt-5" not in model_id` for the `minimal` effort.
  - DSPy has its own regex (API).

  Disagreements: `gpt-5-chat-latest` and `o1-preview` count as reasoning for the repo but not for DSPy, so the repo forces Responses, temperature 1.0 and 16k where DSPy would not. `ft:gpt-5:org` counts only for the app's substring rule. [trap] (verified: table printed on 3.3.1) → here: lmrun.py (read DSPy's classification from a constructed `lm.kwargs`; do not re-encode it)
- **[agents] `runtime_diag` always shows temperature None** — It reads `getattr(lm, "temperature", None)` (`tools/runtime_diag_tool.py:155`), but `dspy.LM` has no `temperature` attribute; the value is in `lm.kwargs`. [trap] (verified: `hasattr(lm,"temperature") == False`)
- **[agents] `DSPY_CACHE_TAG` becomes a path component unsanitized** — `DSPY_CACHE_TAG='phase:7/../../escaped'` wrote the cache to `<base>/../escaped__missing`, outside the cache root (`dspy_config.py:108-112`). The Agno and offline-docs tags are sanitized. [trap] (verified)
- **[agents] `cache_benchmark.py --offline` makes live calls** — The flag means "also benchmark `mini_report_web`" (`scripts/cache_benchmark.py:80-83`), not "no network". `configure_once()` needs `OPENAI_API_KEY` and calls the real LM twice per variant. It is advertised as „Warm vs cold run benchmark: `python scripts/cache_benchmark.py --offline`" (`AGENTS.md:50`). [trap] (verified: read)
- **[agents] The monitor is fooled by unmeasured and failed runs** — The facts are under MET: None skipped, relative-only comparison, failed runs becoming the baseline, empty thresholds meaning ok, compile score unchecked. Together with the CI's missing DB (PROD), no configuration of this monitor can flag "compiled program not used" or "optimizer found nothing". [trap] (verified)
- **[agents] The eval scores the data the optimizer trained on** — There is no held-out split. `eval/harness.py:106-123` re-scores all 50 rows: the 10 MIPROv2 trained on and the 40 it selected on. There is also no non-model baseline in the loop. [trap] → here: pairs.py folds
- **[agents] `import dspy` then `import numpy.typing` fails** — DSPy 3.3.1 installs a `_LazyModule` for `numpy` in `sys.modules` at import (`dspy/utils/lazy_import.py:188-190`, via `require("numpy")`). Any later `import numpy.typing` fails: `ImportError: cannot import name 'NDArray' from partially initialized module 'numpy._typing' (most likely due to a circular import)`. qdrant-client does this, and `import pyarrow` / `import lancedb` after `import dspy` fails too, with „ImportError: numpy._core.multiarray failed to import". `import numpy` before `import dspy` avoids both; plain `import numpy` after dspy works. [trap] (verified: `import dspy, numpy.typing` fails in 3 venvs including `/home/user/kohaerenzprotokoll/.venv-dspy`; `import dspy; import pyarrow` fails in 2) → here: every `.venv-dspy` script; check_dspy_surface.py should import-test it
- **[agentic-rag] Substring routing on free text misroutes** — Offline with scripted intents:

  | classifier output | routed to | correct? |
  |---|---|---|
  | `Comparative` | ComparativeRAG | yes |
  | `Multi-step` | MultiStepRAG | yes |
  | `comparative` | SimpleRAG | **no** |
  | `Multi-Step` | SimpleRAG | **no** |
  | `Multistep` | SimpleRAG | **no** |
  | `multi-step question` | SimpleRAG | **no** |
  | `Not Comparative` | ComparativeRAG | **no** (negation) |
  | `Multi-step (Comparative)` | ComparativeRAG | **no** (check order) |

  Every miss is silent, because the `else` branch defaults to Factual. `agents.py:109-123` [trap] (verified: `scratchpad/work/rag_routing_check.py` on 3.3.1) → here: graphrag.py `--answer`, pairs.py (use `Literal` output; see API)
- **[agentic-rag] The README's install line produces an app that cannot start** — `pip install … "pydantic<2" …` (`README.md:68`) resolves, today and at the commit date, to `dspy-ai==2.3.1` and `pydantic==1.10.x`. DSPy 2.3.1 has no `dspy.LM` (its `__init__` exposes `OpenAI = dsp.GPT3` …) and does not depend on litellm. So `main.py:24 from litellm.exceptions import RateLimitError` and `main.py:74 dspy.LM(...)` both fail. In addition, `py-zerox` needs Python ≥ 3.11, while the README creates `python=3.10` (`README.md:61`); `uv pip compile --python-version 3.10` reports the set unsatisfiable. [trap] (verified: `uv pip compile` + dspy-ai 2.3.1 source)
- **[agentic-rag] The package definition packages nothing** — `find_packages(where="src")` returns `[]` because `src/agentic_rag/_init_.py` has single underscores; `find_namespace_packages` finds `['agentic_rag','agentic_rag.components']`. Imports still work as an implicit namespace package once `src` is on `sys.path`. `setup.py:7-8` [trap] (verified)
- **[agentic-rag] Qdrant API drift** — qdrant-client 1.19.1 has no `QdrantClient.search` (used at `data_modules.py:64`) and no `CollectionInfo.vectors_count` (used at `indexing.py:126`); 1.14.3, current at the commit date, had both. [trap] (verified)
- **[agentic-rag] `history[-1]` usage logging** — It records only the last call of each agent: classifier, rephraser, decomposer and synthesizer tokens are never logged (Multi-step logged 2 of 5 calls offline). It reads a history shared across concurrent requests, so another request's usage can be attributed. The model is always „unknown". On a cache hit `usage` is `{}`, and `.prompt_tokens` raises, which is caught as „Could not parse". `dspy.track_usage()` captured all 5 calls in the same run. `agents.py:26-31,51-56` [trap] (verified offline) → here: lmrun.py (record per call)
- **[agentic-rag] Instructions sent as input values** — Both the classifier prompt and the rephraser prompt are passed as the value of a `question` input field (`agents.py:109-110`, `data_modules.py:46-47`), so they cannot be optimised as instructions and the signature carries no constraint. [trap]
- **[agentic-rag] A `.gitignore` comment is part of the pattern** — `agentic_rag/ # In case a venv is created with the project name` (`.gitignore:71`) matches nothing. The pattern without the comment would have ignored `src/agentic_rag/`, the whole source package. [trap] (verified with `git check-ignore` in a scratch repo)
- **[agentic-rag] Configuring in startup can collide with the test thread** — `dspy.settings.configure(lm=llm)` in `@app.on_event("startup")` (`main.py:75`) raises the thread-ownership `RuntimeError` when anything configured DSPy first in another thread, e.g. a test module doing `dspy.configure` before `TestClient` starts the app in its portal thread. [trap] (verified)

---

## 3. Code worth keeping

**RecorderLM**, `tests/test_dspy_config.py:13-20`. Runs on 3.3.1: it is pure Python and the tests using it passed (3/3).

```python
class RecorderLM:
    def __init__(self, *args, **kwargs):
        # Capture constructor args for assertions
        self.args = args
        self.kwargs = kwargs
        # Expose selected fields similar to dspy.LM for sanity
        self.model = kwargs.get("model", args[0] if args else None)
        self.model_type = kwargs.get("model_type", "chat")
```

**Its use**, `tests/test_dspy_config.py:23-56`. Passed on DSPy 3.3.1. Note the leaking `os.environ` writes (TEST).

```python
def test_config_uses_responses_for_reasoning_models(monkeypatch):
    os.environ["OPENAI_API_KEY"] = "test-key"
    os.environ["OPENAI_MODEL"] = "gpt-5"
    os.environ["OPENAI_USE_RESPONSES"] = "auto"
    os.environ["OPENAI_REASONING_EFFORT"] = "low"
    os.environ["OPENAI_MAX_TOKENS"] = "20000"

    import dspy_config as cfg
    importlib.reload(cfg)
    reset_module(cfg)

    constructed = {}

    def fake_configure(**kwargs):
        return None

    def fake_lm(model, *args, **kwargs):
        lm = RecorderLM(model=model, **kwargs)
        constructed["lm"] = lm
        return lm

    monkeypatch.setattr(cfg.dspy, "configure", fake_configure)
    monkeypatch.setattr(cfg.dspy, "LM", fake_lm)

    cfg.configure_once()

    lm = constructed["lm"]
    assert lm.kwargs.get("model_type") == "responses"
    assert lm.kwargs.get("temperature") == 1.0
    # Must satisfy DSPy validation
    assert lm.kwargs.get("max_tokens", 0) >= 16000
    # Responses extras present
    assert lm.kwargs.get("max_output_tokens", 0) >= 16000
    assert lm.kwargs.get("reasoning", {}).get("effort") in {"minimal", "low", "medium", "high"}
```

**Cache off before configure, then a tracked compile**, `dspy_optimize/compile_rag.py:62-90`. Runs on 3.3.1: I ran `main()` offline with `dspy.LM` patched to a fake. The tracked usage is wrong under `num_threads=8`, and the saved artifact needs `dspy.load(..., allow_pickle=True)`.

```python
    if _env_flag("BASELINE_DISABLE_CACHE"):
        configure_cache(enable_disk_cache=False, enable_memory_cache=False)
        try:
            dspy.cache.reset_memory_cache()
        except Exception:
            pass

    # Configure LM once (temperature=0 for lower variance)
    dspy.configure(
        lm=dspy.LM("openai/gpt-4o-mini", api_key=api_key, temperature=0),
        track_usage=True,
    )

    # Simple program that consumes context + question and produces an answer
    program = dspy.ChainOfThought("context, question -> answer")

    # Load small trainset
    trainset = load_trainset()

    # Optimize with MIPROv2 (light) against exact-match metric (fits short answers)
    tp = dspy.MIPROv2(metric=dspy.evaluate.answer_exact_match, auto="light", num_threads=8)

    start = time.perf_counter()
    with dspy.track_usage() as usage_tracker:
        optimized = tp.compile(program, trainset=trainset)
    duration_seconds = time.perf_counter() - start

    # Persist for runtime
    optimized.save(str(ARTIFACT_PATH), save_program=True)
```

**A sequential evaluation whose usage is complete**, `eval/harness.py:75-85`. Runs on 3.3.1: 750 tokens tracked for 50 fake calls.

```python
def _evaluate_module(module: Any, dataset: list[dict[str, Any]]) -> tuple[int, dict[str, dict[str, Any]], float]:
    start = time.perf_counter()
    hits = 0
    with dspy.track_usage() as usage_tracker:
        for ex in dataset:
            prediction = module(context=ex["context"], question=ex["question"])
            answer = getattr(prediction, "answer", prediction)
            hits += em(answer, ex["answer"])
    duration = time.perf_counter() - start
    usage = summarize_usage(usage_tracker.get_total_tokens())
    return hits, usage, duration
```

**The silent fallback, as an anti-pattern**, `dspy_config.py:213-226`. It runs on 3.3.1 and always takes the `except` branch.

```python
def get_rag_program():
    """Return the compiled RAG program if present; otherwise a zero-shot program."""

    global _PROGRAM_CACHE
    if _PROGRAM_CACHE is not None:
        return _PROGRAM_CACHE

    configure_once()
    artifacts_path = os.getenv("RAG_ARTIFACT_PATH", "dspy_optimize/artifacts/rag_compiled")
    try:
        _PROGRAM_CACHE = dspy.load(artifacts_path)
    except Exception:
        _PROGRAM_CACHE = dspy.ChainOfThought("context, question -> answer")
    return _PROGRAM_CACHE
```

**Threshold rule evaluation**, `dspy_optimize/baselines/thresholds.py:181-214`. Standard library; its tests pass on the 3.3.1 venv. The anti-patterns are line 2 of the body (None skipped) and the fail→warn downgrade.

```python
def _evaluate_rule(
    rule: MetricThreshold,
    current_value: Optional[float],
    baseline_value: Optional[float],
) -> Optional[Dict[str, Any]]:
    if current_value is None:
        return None

    # Absolute bounds
    if rule.min_value is not None and current_value < rule.min_value:
        return _result(rule, current_value, baseline_value, "min", rule.min_value, rule.severity)
    if rule.max_value is not None and current_value > rule.max_value:
        return _result(rule, current_value, baseline_value, "max", rule.max_value, rule.severity)

    # Baseline-relative checks
    if baseline_value is not None:
        delta = baseline_value - current_value
        if rule.max_drop is not None and delta > rule.max_drop:
            return _result(rule, current_value, baseline_value, "max_drop", rule.max_drop, rule.severity)
        if (
            rule.max_pct_drop is not None
            and baseline_value not in (0, None)
            and (baseline_value - current_value) / abs(baseline_value) > rule.max_pct_drop
        ):
            return _result(rule, current_value, baseline_value, "max_pct_drop", rule.max_pct_drop, rule.severity)
        if (
            rule.max_pct_increase is not None
            and baseline_value not in (0, None)
            and (current_value - baseline_value) / abs(baseline_value) > rule.max_pct_increase
        ):
            severity = "warn" if rule.severity == "fail" else rule.severity
            return _result(rule, current_value, baseline_value, "max_pct_increase", rule.max_pct_increase, severity)

    return None
```

**Metadata signature for cache namespaces**, `dspy_config.py:61-86`. Standard library; it ran offline and produced `3547720bc75f`. It hashes path, mtime and size, not content.

```python
        digest = hashlib.sha1()

        files = (
            [root]
            if root.is_file()
            else sorted(p for p in root.rglob("*") if p.is_file())
        )

        if not files:
            signature = "empty"
            _PROGRAM_CACHE_SIGNATURES[key] = signature
            return signature

        for path in files:
            try:
                stat = path.stat()
            except OSError:
                continue
            rel = path.relative_to(root if root.is_dir() else path.parent).as_posix()
            digest.update(rel.encode("utf-8", "ignore"))
            digest.update(str(stat.st_mtime_ns).encode("ascii", "ignore"))
            digest.update(str(stat.st_size).encode("ascii", "ignore"))

        signature = digest.hexdigest()[:12]
        _PROGRAM_CACHE_SIGNATURES[key] = signature
        return signature
```

**Offline CLI test hygiene**, `tests/test_lancedb_ingest.py:99-108`. Passed with the period deps.

```python
    env = os.environ.copy()
    env.pop("OPENAI_API_KEY", None)
    result = subprocess.run(
        args,
        check=True,
        capture_output=True,
        text=True,
        env=env,
        cwd=str(repo_root),
    )
```

**Unnormalized hybrid fusion, as an anti-pattern**, `skills/rag/lancedb_store.py:485-517`. It ran with lancedb 0.24.3. In the repo's environment the FTS branch always drops out at DEBUG level.

```python
    if v_weight > 0:
        embedding = list(embed_fn([query]))
        if not embedding:
            return []
        _validate_embeddings(embedding, table)
        vector_rows = table.search(embedding[0]).limit(limit * 3).to_list()
        for row in vector_rows:
            distance = float(row.get("_distance", 0.0))
            score = 1.0 / (1.0 + distance)
            vector_results[row["chunk_id"]] = (row, score)

    if s_weight > 0:
        try:
            scalar_rows = table.search(query, query_type="fts").limit(limit * 3).to_list()
        except RuntimeError as exc:
            LOGGER.debug("FTS search failed (%s); continuing with vector results", exc)
            scalar_rows = []
        for row in scalar_rows:
            score = float(row.get("_score", 0.0))
            scalar_results[row["chunk_id"]] = (row, score)

    scores: dict[str, tuple[dict, float]] = {}
    for chunk_id, (row, score) in vector_results.items():
        scores[chunk_id] = (row, score * v_weight)
    for chunk_id, (row, score) in scalar_results.items():
        prev_row, prev_score = scores.get(chunk_id, (row, 0.0))
        scores[chunk_id] = (row if prev_row is None else prev_row, prev_score + score * s_weight)

    ranked = sorted(
        scores.values(),
        key=lambda item: item[1],
        reverse=True,
    )
```

**Classify-then-route, as an anti-pattern**, `Agentic-Dspy-Rag/src/agentic_rag/components/agents.py:107-127`. Runs on 3.3.1 when numpy is imported before dspy. The misrouting table is in TRAP. The fix is a class signature with `intent: Literal["Factual","Comparative","Multi-step"]`, which I verified rejects off-list values on 3.3.1.

```python
    def forward(self, question):
        # 1. Classify the intent of the user's question.
        prompt = f"Classify the user's question. Choices: Factual, Comparative, Multi-step. Question: {question}"
        intent_prediction = self.classifier(question=prompt)
        user_intent = intent_prediction.intent
        print(f"--- Detected Intent: '{user_intent}' ---")

        # 2. Route the question to the correct agent based on the classified intent.
        if "Comparative" in user_intent:
            print("--- Routing to: ComparativeRAG Agent ---")
            prediction = self.comparative_rag_agent(question=question)
        elif "Multi-step" in user_intent:
            print("--- Routing to: MultiStepRAG Agent ---")
            prediction = self.multi_step_rag_agent(question=question)
        else: # Default to the Factual agent.
            print("--- Routing to: SimpleRAG Agent ---")
            prediction = self.simple_rag_agent(question=question)
        
        # 3. Attach the detected intent to the final prediction object for API response.
        prediction.intent = user_intent
        return prediction
```

**Usage logging through history, as an anti-pattern**, `agents.py:26-31`. Runs on 3.3.1 but logs „Model: unknown" and only the last call.

```python
        # Log the token usage for this LLM call.
        try:
            usage = dspy.settings.lm.history[-1]['response'].usage
            log_api_usage("OpenAI", dspy.settings.lm.kwargs.get('model', 'unknown'), usage.prompt_tokens, usage.completion_tokens, usage.total_tokens)
        except Exception:
            print("[USAGE LOG] Could not parse usage data for SimpleRAG.")
```

---

## 4. The old report, corrected

### `dspy-repos_2026-09-23/dspy-agents.md`

1. **„MIPROv2 best score 0.0 in one logged run" (§1).** Both logged compile runs (29 and 50 examples) have `score` 0.0.
2. **§4 reads `"total_calls": 0` as the model never being called meaningfully.** `total_calls` and `prompt_model_total_calls` are dead counters: never incremented in 3.0.3 or 3.3.1, always 0 (0/0 after 482 calls offline). The real signal is that ties return the unmodified student. The compiled eval's prompt tokens equal zero-shot's (6466/6466), and its 2025-09-26 pass was entirely cache hits.
3. **„There is no absolute floor check here" (§4) is wrong for the eval.** `compiled_em_rate` has `min_value=0.05` (fail) and `delta_em_rate` `min 0.0` (warn) (`thresholds.py:49-78`). It is right for the compile: `program_score` has no rule at all. The flaws the report missed:
   - a `None` metric is skipped silently, so on DSPy 3.3.1 the eval reports "ok" with the compiled program unmeasured;
   - failed runs become the next baseline;
   - `{}` thresholds turn everything off, and a test pins it;
   - CI has no persisted DB, so relative checks can never fire there.
4. **Item 10, „Cache directory keyed by a content hash", is wrong.** It hashes path, mtime_ns and size (sha1[:12]), memoised per process. It is also unnecessary for correctness, because DSPy's cache key is already the sha256 of the full request.
5. **Item 11, „prefix detection, not substring", is half the story.** The same repo uses substring detection for the same property at `app.py:230` and `dspy_config.py:190`. DSPy 3.3.1's own regex disagrees with the prefix list (`gpt-5-chat-latest`, `o1-preview`).
6. **Item 9 and §3, which praise `dspy.track_usage()` as directly reusable, miss that it undercounts.** Worker-thread trackers are deep copies that are never merged. Under `num_threads=8` the repo's compile usage is main-thread only: 765 tracked against 7230 true tokens offline, and `Evaluate(num_threads=8)` tracked `{}`.
7. **§4's test numbers („15/26 … 16/26") describe the scanner's minimal venv, not the documented environment.** With the requirements as of the commit date the offline tier is 40/43 without a key and 43/43 with any fake key. With no deps, pytest runs 0 tests unless `--continue-on-collection-errors`. The real defects are key-dependence, order-dependence, leaking env writes, and side-effect directories.
8. **The report missed the load break.** `dspy.load` requires `allow_pickle=True` since DSPy 3.1.0; `get_rag_program()` and the harness swallow the error; the pin `>=3.0.3,<4.0` admits it. On today's install the compiled program is never used and the eval says „No compiled artifact found.".
9. **The report missed the model mismatch.** The program is compiled on `gpt-4o-mini` (chat, temperature 0) and served on `gpt-5` (Responses, temperature 1.0). The eval scores rows the optimizer trained and selected on. The automatic split puts the last 40 of 50 rows in the valset, with no shuffle.
10. **The report missed the silently ignored token cap.** `OPENAI_MAX_OUTPUT_TOKENS` does nothing on 3.3.1; `runtime_diag` shows temperature None; `DSPY_CACHE_TAG` is unsanitized, contrary to its doc.
11. **Item 22 misreads `cache_benchmark.py --offline`.** The flag makes live LM calls; it means "include `mini_report_web`".
12. **Item 17's signature guard is weaker than described.** It is skipped when the offline docs are missing or empty (a test pins that) and evaluated once per process. The per-row corpus signature forces re-embedding of every chunk after any mtime change. The "hybrid" search is vector-only in the repo's own environment (tantivy and pylance are missing; the errors are logged at DEBUG).
13. **The report missed three more defects.** The demo MCP server cannot start (`FastMCP.run()` has no `host`). `MultiMCPTools` receives the whole `os.environ`. `research_report`'s critique is never applied.
14. **The dataset drift bullet is correct and can be dated.** Rows went 15 → 25 → 28 → 29 → 46 → 50. The „9/29" claim has no committed log; the only logged compiled EM equals zero-shot (3/29 and 3/50).

### `dspy-repos_2026-09-23/agentic-dspy-rag.md`

1. **„pre-2.x style API" is wrong.** `dspy.LM(model=...)` is the 2.5+/3.x API, string signatures are current, and `dspy.Retrieve` still exists in 3.3.1.
2. **„The package … does not actually initialize as a Python package" is half-true.** `find_packages(where="src")` returns `[]`, so `setup.py` packages nothing. But `agentic_rag` imports fine as an implicit namespace package with `src` on `sys.path`, and I ran it.
3. **„Never run here" no longer holds.** I ran the orchestrator and the FastAPI `/query` endpoint offline on DSPy 3.3.1 with fakes; both return 200. It needs `import numpy` before `import dspy`: DSPy 3.3.1's lazy numpy proxy otherwise breaks `qdrant_client`'s `import numpy.typing` (and `pyarrow`). That applies to the target's `.venv-dspy` too.
4. **The `pydantic<2` point was underplayed** („a possible conflict if installed into a shared venv"). The README's own install line resolves to `dspy-ai==2.3.1`, which has no `dspy.LM`, and litellm is absent. The documented setup cannot start the app, and `py-zerox` needs Python ≥ 3.11 against the README's 3.10.
5. **Item 7 recommended copying the `history[-1]` usage snippet verbatim.** It logs „Model: unknown" always and only the last call per agent (2 of 5 calls on the multi-step path). It reads a history shared across concurrent requests and fails on cache hits. `dspy.track_usage()`, or the history entries' own `usage` and `cost` fields, are the 3.x answer.
6. **Routing fragility is now measured.** `comparative`, `Multi-Step`, `Multistep` and `multi-step question` go to SimpleRAG; `Not Comparative` and `Multi-step (Comparative)` go to ComparativeRAG; every miss is silent. A `Literal` output type makes these fail loudly (verified).
7. **The report missed:**
   - qdrant-client ≥ 1.19 removed `search` and `vectors_count`;
   - the fallback reranker order is hash-randomized through `set(queries)`;
   - `MultiStepRAG` returns one Q&A string as context, dropping the passages (verified);
   - `.gitignore:71`'s trailing comment neutralises a pattern that would have ignored the source package;
   - `dspy.settings.configure` in the FastAPI startup can hit DSPy's thread-ownership `RuntimeError`.

---

## 5. Ten things the skill must say

1. `dspy.load(path)` raises without `allow_pickle=True` from DSPy 3.1.0 on. Never wrap it in a bare `except` that falls back to zero-shot; prefer `save("x.json")` state files. (API `dspy.load`; TRAP "compiled program is never used")
2. `dspy.track_usage()` drops all usage from `Evaluate` or optimizer worker threads (`num_threads>1`). Count per call instead: 765 tracked against 7230 real. (PROD `track_usage`)
3. MIPROv2 returns the untouched student when no candidate beats it, and `total_calls` is always 0. Check `score > baseline` and the diff of demos and instructions, not the counters. (OPT "ties", "score/total_calls")
4. MIPROv2 with `valset=None` uses the *last* 80% of the list, unshuffled; `light` means 10 trials, 6 demo sets and 3 instructions for one predictor, with no minibatch below 51 val rows. (OPT "automatic split", "light")
5. A drift monitor that skips `None` metrics and compares only with the previous run passes a broken pipeline forever. Use a floor, a pinned best, and an explicit "could not check" status. (MET "unmeasured metric", "previous run")
6. Never route on a substring of free text. Declare `Literal[...]` outputs so the adapter rejects off-list values. (TRAP substring routing; API `Literal`)
7. On DSPy 3.3.1, `import numpy` before `import dspy`, or any later `import numpy.typing` (qdrant-client) or `import pyarrow`/`lancedb` fails. The shared `.venv-dspy` included. (TRAP numpy)
8. RecorderLM-style kwargs tests do not prove DSPy accepts or uses the kwargs. Add a real offline `dspy.LM(...)` construction and a request-conversion check (`max_output_tokens` is silently overridden). (TEST RecorderLM; TRAP `OPENAI_MAX_OUTPUT_TOKENS`)
9. Compile and evaluate on the model you serve, with a held-out split and a non-model baseline; this repo compiled on `gpt-4o-mini` and served `gpt-5` on the training rows. (OPT "compiled for one model"; TRAP "eval scores the data")
10. `dspy.settings` belongs to the first thread that configures it. Use `dspy.context(...)` in other threads and async tasks, and do not configure in a server startup hook that tests run in a portal thread. (API settings ownership; TRAP startup)
