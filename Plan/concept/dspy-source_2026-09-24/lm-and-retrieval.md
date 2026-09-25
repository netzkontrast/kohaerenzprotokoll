# lm-and-retrieval — DSPy 3.3.1's LM clients and retrieval layer

## 1. Header

**Slice**: `dspy/clients/` (13 files), `dspy/retrievers/` (5 files), `dspy/dsp/colbertv2.py`,
`dspy/dsp/utils/{utils.py,dpr.py}`, `dspy/utils/{usage_tracker.py,inspect_history.py,caching.py}`
— 24 source files, ~6,856 lines, all read in full.

**Tests**: `tests/clients/test_lazy_litellm_import.py` (86 lines), `test_lm_local.py` (97) and
`tests/retrievers/test_colbertv2.py` (41) read in full. `test_lm.py` (2,174 lines total; ~710
read directly — cache/rollout_id/reasoning-model/retry/responses-cache-hit sections — plus the
full `def test_`/`class` index grepped for the remainder), `test_cache.py` (556; ~180 read —
init, save/load, `request_cache`), `test_disk_serialization.py` (404; ~90 read — the
`restrict_pickle` allowlist and attack-payload tests), `test_embedding.py` (199; ~175, nearly
all), `test_inspect_global_history.py` (139; ~55), `test_usage_tracker.py` (394; ~55, the
`ParallelExecutor` case). `test_databricks.py` and `tests/retrievers/test_embeddings.py` were
indexed by function name only, not read line by line — Databricks finetuning and the
`Embeddings` save/load round trip are both already fully confirmed independently from the
source files. `test_lm_direct_live.py` (482 lines) was read structurally (every `def test_`
and its `@pytest.mark.llm_call` marker) and **never run**, per the brief.

**Docs**: every file the task named, in full. `docs/docs/api/models/*.md` and
`docs/docs/api/tools/{ColBERTv2,Embeddings}.md` and `docs/docs/api/utils/{configure_cache,
inspect_history,disable_litellm_logging,enable_litellm_logging}.md` are mkdocstrings stubs — a
`:::` directive and nothing else; their content is the docstrings already read in source, except
one fact stated only in the stub wrapper (the `numpy` extra). `docs/docs/learn/programming/
language_models.md`, `docs/docs/community/normalized-lm-api-migration.md`,
`docs/docs/production/index.md`, `docs/docs/tutorials/cache/index.md` and
`.../deployment/index.md` are hand-written and were read in full; `.../llms_txt_generation/
index.md` was read/grepped in full and contributes almost nothing to this slice (one bare
`dspy.LM(model="gpt-4o-mini")` call, no provider prefix). `.../rag/index.ipynb` (52 cells) and
`.../multihop_search/index.ipynb` (32 cells) were read cell-by-cell for markdown and code,
skipping long output cells, per the brief's allowance for notebooks.

**Verification**: `.venv-dspy/bin/python` throughout, offline
(`env -u OPENROUTER_API_KEY -u TYPESAFE_API_KEY -u OPENAI_API_KEY -u ANTHROPIC_API_KEY`).
`inspect.signature` against the installed package for every constructor in the Surface section;
five self-contained probes (below) that monkeypatch `litellm.completion` the same way DSPy's own
`tests/clients/test_lm.py` does — this is the only way to exercise the real cache machinery,
because `lm_fixture.FixtureLM` hardcodes `cache=False` at construction
(`scripts/lm_fixture.py:92`) and so cannot be used to probe caching itself.

**What this slice is, in 5 lines**: `dspy.LM` wraps litellm behind DSPy's own two-level cache and
a typed error hierarchy, with a second, still-experimental typed call path (`LMRequest`/
`LMResponse`) migrating in underneath the same public surface. `dspy.Embedder` and
`dspy.retrievers.Embeddings` are a thin, fully local-capable embedding+search pair — a plain
Python callable is a first-class "provider." `dspy.Retrieve`/`ColBERTv2`/`WeaviateRM`/
`DatabricksRM` are the older `dspy.settings.rm`-based retrieval interface, unified only by every
result needing a `.long_text` attribute. `dspy.clients.lm_local.LocalProvider` is DSPy's own
local-inference launcher (SGLang, bound to `0.0.0.0`) and local-finetuning path (`trl`/`peft`),
independent of simply pointing `dspy.LM` at someone else's OpenAI-compatible server. Usage and
cost tracking, the disk cache, and pickle-restriction are three separate, deliberately-scoped
security/observability mechanisms, and none of them is as simple as their names suggest.

## 2. Knowledge items

## API

- **`dspy.LM.__init__` full signature** — `model, model_type="chat", temperature=None, max_tokens=None, cache=True, callbacks=None, num_retries=3, provider=None, finetuning_model=None, launch_kwargs=None, train_kwargs=None, use_developer_role=False, **kwargs`. `dspy/clients/lm.py:63-77`, confirmed by `inspect.signature(dspy.LM.__init__)`. [api] (verified: ran) · skill: **wrong: `api.md:28`** — the `surface` block lists `dspy.LM(model, model_type="chat", temperature=None, max_tokens=None, cache=True, callbacks=None, num_retries=3, provider=None, use_developer_role=False)` and omits `finetuning_model`, `launch_kwargs`, `train_kwargs` entirely, even though `api.md:296` shows a plain `dspy.LM(...)` call with none of them either — the three parameters the brief specifically names are missing from the skill's declared surface.
- **`rollout_id` is a documented `**kwargs` parameter, not a named one** — `dspy.LM`'s own docstring documents `rollout_id` in its `Args:` block (`dspy/clients/lm.py:98-102`: "stripped before sending requests to the provider") but it is never a named parameter anywhere in `LM.__init__`/`BaseLM.__init__`; it only exists because it flows through `**kwargs` into `self.kwargs`. `dspy/clients/lm.py:63-77`. [trap] (verified: `inspect.signature` shows no `rollout_id` parameter) · skill: new.
- **The cache key is the sha256 of the whole request dict, minus three keys, plus the calling function's identity** — `Cache.cache_key(request, ignored_args_for_cache_key)` builds `params = {k: _transform_value(v) for k,v in request.items() if k not in ignored}` then `sha256(orjson.dumps(params, option=OPT_SORT_KEYS)).hexdigest()`. `dspy/clients/cache.py:104-113`. For `dspy.LM`, `request_cache`'s `process_request` first injects `modified_request["_fn_identifier"] = f"{fn.__module__}.{fn.__qualname__}"` (`dspy/clients/cache.py:249,262`), so `litellm_completion`'s cache and `litellm_text_completion`'s cache are two disjoint spaces even given byte-identical requests. `ignored_args_for_cache_key` for LM calls is `["api_key", "api_base", "base_url"]` (`dspy/clients/lm.py:174`), so **the cache key is portable across endpoints and keys but not across `model_type`/calling paths**. [api] (verified: read + probed) · skill: unchecked — `operations.md` and `api.md:500-515` describe the two-level cache and `restrict_pickle` but never state the key formula or the `_fn_identifier` component.
- **`_transform_value` makes the cache key content-sensitive to callables by their source code** — a callable value in the request (e.g. a custom `dspy.Embedder` function) is hashed as `f"<callable_source:{inspect.getsource(value)}>"`, falling back to `f"<callable:{name}>"` only if `inspect.getsource` raises `TypeError`/`OSError` (e.g. a lambda with no retrievable source). `dspy/clients/cache.py:24-37`. So changing a local embedder's *code* (not just its identity) changes the cache key. [api] (verified: read) · skill: new.
- **rollout_id always changes the cache key, at any temperature — the "no effect at temperature=0" warning is about the provider's output, not about whether the cache is bypassed.** `dspy.LM(temperature=0)` called twice with `rollout_id=1` then `rollout_id=2` makes **two** real `litellm.completion` calls (2 distinct cache entries); a third call repeating `rollout_id=1` is a cache hit. `dspy/clients/lm.py:165-171` (the warning fires) and `:241-242,299-300` (rollout_id is only *popped* from kwargs when it is `None` — never because temperature is 0). The docs get this exactly right: "DSPy hashes both the inputs and the `rollout_id` when looking up a cache entry, so different values force a new LM request... **Changing only the `rollout_id` while keeping `temperature=0` will not affect the LM's output**" (`docs/docs/learn/programming/language_models.md:208-212`) — output, not request. [trap] (verified: probe `rollout-id-busts-cache-at-zero-temperature`, ran, holds — 2 real calls made at `temperature=0`) · skill: **wrong: `api.md:261-264`** and `operations.md:260-264` both say "`rollout_id` bypasses the cache for an otherwise-identical request, but **only when `temperature > 0`**" — read plainly this says the cache is *not* bypassed at `temperature=0`, which the probe disproves; DSPy's own runtime warning text ("...set `temperature>0` to **bypass the cache**") is the same imprecise phrasing and is arguably the source of the skill's error.
- **`rollout_id=None` passed explicitly is indistinguishable from not passing it at all** — both are stripped from kwargs before the request dict is built (`if kwargs.get("rollout_id") is None: kwargs.pop("rollout_id", None)`, `dspy/clients/lm.py:241-242`), so they hash identically and hit the same cache entry. Test-proven: a call with no `rollout_id` and a later identical call with `rollout_id=None` register 1 and 0 new usage entries respectively (`tests/clients/test_lm.py:168-174`). [api] (verified: test read) · skill: new.
- **The zero-temperature-rollout warning fires at most once per LM instance, and `copy()` resets that** — `self._warned_zero_temp_rollout` is set once in `BaseLM.__init__` (`dspy/clients/base_lm.py:203`) and `BaseLM.copy()` explicitly resets it to `False` on the copy (`dspy/clients/base_lm.py:768-769`), so an LM copied via `lm.copy(rollout_id=…)` — exactly what `BestOfN`/`Refine` do — will warn again even if the original already warned once. [trap] (verified: test `test_zero_temperature_rollout_warns_once`, `tests/clients/test_lm.py:181-197`, read) · skill: new.
- **Per-call `cache=` overrides the LM's own `cache` attribute** — `forward()`/`aforward()` do `cache = kwargs.pop("cache", self.cache)` (`dspy/clients/lm.py:234,292`), so `lm("q", cache=False)` bypasses caching for one call on an otherwise `cache=True` LM, and vice versa. [api] (verified: read) · skill: new — `api.md`'s cache section only discusses the constructor-level flag.
- **DSPy always disables litellm's own cache and always disables its own retry parameters' relation to litellm's** — `litellm_cache_args = {"no-cache": True, "no-store": True}` is passed on *every* completion call regardless of `cache=True/False` on the DSPy side (`dspy/clients/lm.py:181-183,496,514,544,562,590,606`); litellm's process-global cache is also forced off once at first import: `litellm.cache = None` (`dspy/clients/_litellm.py:15`). DSPy's own two-level `Cache` (memory+disk) is the *only* caching layer that ever applies to a `dspy.LM` call — litellm's native caching is structurally unreachable through DSPy. [api] (verified: read) · skill: new — this closes a gap the skill leaves open (it documents DSPy's cache and separately notes provider-side prompt caching, but never states that litellm's own cache is force-disabled).
- **`litellm.telemetry` is force-disabled the first time any DSPy code touches litellm** — `_configure_litellm_defaults` (cached with `functools.cache`, so it runs exactly once) sets `litellm.telemetry = False` and `litellm.suppress_debug_info = True` (unless logging was already explicitly configured) on first `get_litellm()` call. `dspy/clients/_litellm.py:11-18,29-35`. Directly answers the brief's local-server question: DSPy itself adds no outbound call beyond the configured `api_base`, and actively turns off litellm's own home-phoning; a `User-Agent: DSPy/{version}` header is the only thing DSPy adds to the request (`dspy/clients/lm.py:710-715`). Litellm's own model-cost-map fetch behaviour is outside this slice (litellm internals, not `dspy/clients`) and is **not verified here** — flagged as an open caveat, not a claim. [api] (verified: read) · skill: new.
- **litellm is imported lazily; the `openai` SDK is not.** `import dspy` alone never puts `"litellm"` in `sys.modules`, even after touching `dspy.LM`, `dspy.Embedder`, `dspy.streamify` (`tests/clients/test_lazy_litellm_import.py:25-34`, read and this is the test's own assertion). Litellm materializes only on first real use (`.supports_function_calling`, an embedding call, …), via `dspy/clients/_litellm.py:29-35`'s `functools.cache`d `get_litellm`, and a missing-litellm error names the feature and says to `pip install dspy[litellm]` (same test file, `:37-60`). By contrast `dspy/clients/openai.py:5` does a bare top-level `import openai`, unconditionally — `dspy.clients.lm` imports `OpenAIProvider` from that module at `dspy/clients/lm.py:15`, and `dspy/clients/__init__.py:10` imports `dspy.clients.lm` — so **the `openai` package is a hard, eager dependency of `import dspy`**, unlike litellm. [trap] (verified: test read + source read) · skill: new.
- **Concurrent first-use of litellm is safe** — 8 threads racing to trigger `get_litellm()` for the first time all succeed and return a usable module (`tests/clients/test_lazy_litellm_import.py:63-86`, read). [pattern] (verified: test read) · skill: new (minor).
- **Every real LM error in DSPy 3.3 is one of two shapes at the litellm boundary: a name-and-message match, or a raw HTTP status.** `_wrap_litellm_exception` (`dspy/clients/lm.py:185-207`) first checks `is_litellm_context_window_error` → `ContextWindowExceededError`; else tries `_lm_error_class_from_litellm_exception` (`:726-758`) which (a) matches `"api key"/"apikey"/"credentials"/"environment variable"` substrings in the message when there's no HTTP status → `LMNotConfiguredError`, (b) matches `"timeout"` in the class name or message → `LMTimeoutError`, (c) matches `"connection"`/`"network"` → `LMTransportError`, then (d) a fixed table of litellm exception **class names**: `AuthenticationError→LMAuthError`, `RateLimitError→LMRateLimitError`, `NotFoundError→LMUnsupportedModelError`, `UnsupportedParamsError→LMUnsupportedFeatureError`, `UnprocessableEntityError/ContentPolicyViolationError/BadRequestError/InvalidRequestError→LMInvalidRequestError`, `InternalServerError/ServiceUnavailableError→LMServerError`, `APIConnectionError→LMTransportError`, `APIResponseValidationError→LMProviderError`, `BudgetExceededError→LMBillingError`, `RouterRateLimitError→LMRateLimitError`. If none of that matches, falls back to `_lm_error_class_from_status` (`:761-776`) purely by HTTP status: `401/403→LMAuthError`, `402→LMBillingError`, `404→LMUnsupportedModelError`, `408→LMTimeoutError`, `429→LMRateLimitError`, other `4xx→LMInvalidRequestError`, `5xx→LMServerError`, **no status at all → `LMUnexpectedError`**, any other status (e.g. a bare `3xx`) → `LMProviderError`. [api] (verified: read; matches `tests/clients/test_lm.py:279-313` exactly) · skill: unchecked — `api.md:384-417` has the exception *tree* and the `unreachable` classification rule but not this mapping table; nobody could reconstruct which litellm exception produces which DSPy type from the skill today.
- **Exception metadata is best-effort and documented as such in the source itself** — `_exception_status`/`_message`/`_headers`/`_request_id`/`_retry_after`/`_provider_code` (`dspy/clients/lm.py:784-842`) all use defensive `getattr` chains with an explicit comment: "LiteLLM exception metadata is not exposed as a single stable typed shape across providers... Keep the defensive getattr-based extraction localized here." `request_id` tries four header name variants (`x-request-id`, `request-id`, `x-amzn-requestid`, `x-ms-request-id`). [api] (verified: read) · skill: new.
- **num_retries is litellm's own tenacity-based retry, and DSPy passes it through untouched** — `litellm_completion` calls `litellm.completion(..., num_retries=num_retries, retry_strategy="exponential_backoff_retry", ...)` (`dspy/clients/lm.py:495-508`); `num_retries` on `dspy.LM` is `self.num_retries` (default 3), and there is no separate DSPy-level retry loop anywhere in this slice. Empirically: `num_retries=3` on a `RateLimitError` produces **4** total attempts (1 original + 3 retries) (`tests/clients/test_lm.py:349-374`, read: `retry_tracking[0] == 4`). `dspy.is_retryable_lm_error(e)` (referenced, not in this slice's files) decides rate-limit/timeout/server/transport errors are retryable and auth/billing/invalid-request are not — consistent with which litellm exceptions the mapping table above routes to which DSPy type. [api] (verified: test read) · skill: unchecked — `api.md`'s LM section says "`num_retries=3` is litellm's retry" but never states the off-by-one (N retries = N+1 attempts) or names `retry_strategy="exponential_backoff_retry"` as the literal string DSPy passes.
- **A reasoning model is detected by two different, disagreeing functions in the shipped 3.3.1 code.** `dspy/clients/lm.py:48-53`'s `_is_openai_reasoning_model` (used by the legacy `LM.forward()`/`dump_state`/`load_state` path) is a regex `^(?:o[1345](?:-(?:mini|nano|pro))?(?:-\d{4}-\d{2}-\d{2})?|gpt-5(?!-chat)(?:-.*)?)$` matched against the last `/`-segment — it includes **o5**. `dspy/clients/openai_format.py:550-556`'s same-named `_is_openai_reasoning_model` (used only by the new typed `LMRequest`→Responses/Chat-kwargs path, i.e. `_validate_openai_reasoning_temperature` and `_uses_max_completion_tokens`) is `model_name.startswith(("o1","o3","o4","gpt-5"))` with a separate `"chat" in model_name` exclusion — it does **not** include o5, and it uses `startswith` (so `"o10"` or `"o1abc"` would also match, unlike the regex). The two paths therefore validate reasoning-model temperature/token requirements differently: the legacy path requires `max_tokens>=16000` for any recognized reasoning model (raising `LMConfigurationError` otherwise, `dspy/clients/lm.py:125-132`); the typed path (`_validate_openai_reasoning_temperature`, `dspy/clients/openai_format.py:523-543`) only checks temperature-vs-reasoning-effort and never enforces a token minimum at all, and it is explicitly called with `enforce_reasoning_temperature=False` from the legacy-compatibility shim (`_convert_chat_request_to_responses_request`, `dspy/clients/lm.py:664`) so even that weaker check is skipped on the path this repository would actually use for `model_type="responses"`. [trap] (verified: probe `reasoning-model-detectors-disagree`, ran, holds) · skill: unchecked — `api.md:314-317` documents only the legacy-path regex and its `temperature and …` truthiness gap (`temperature=0.0` slips through, confirmed still true — `dspy/clients/lm.py:126`); it has no mark for the second, disagreeing implementation.
- **The reasoning-model `temperature` truthiness gap is real and reproduced exactly.** `if (temperature and temperature != 1.0) or (max_tokens and max_tokens < 16000): raise LMConfigurationError(...)` (`dspy/clients/lm.py:126-132`) — `temperature=0.0` is falsy in Python, so it never trips the first branch; `dspy.LM("openai/o1", temperature=0.0, max_tokens=16000)` constructs without error even though `o1` "requires" `temperature=1.0 or None`. [trap] (verified: read; matches skill's existing `[checked: …]`) · skill: same — already correctly stated in `api.md:314-317`.
- **Reasoning models swap `max_tokens` for `max_completion_tokens` internally, and `dump_state`/`load_state` translate back.** `_get_initial_kwargs` builds `max_completion_tokens=max_tokens` instead of `max_tokens=max_tokens` for a recognized reasoning model (`dspy/clients/lm.py:133`); `LM.dump_state()` renames it back to `max_tokens` in the saved state (`:421-422`) and `LM.load_state()` renames it forward again on load (`:429-433`) — so a saved/loaded reasoning-model LM round-trips the *external* key name even though the *internal* `self.kwargs` key differs. [api] (verified: read; matches tests `test_reasoning_model_dump_state_uses_constructor_max_tokens`, `test_reasoning_model_load_state_round_trips_canonical_state`, `test_reasoning_model_load_state_accepts_max_completion_tokens_alias`, `tests/clients/test_lm.py:915-1004`, indexed) · skill: new.
- **`lm.history[i]["cost"]` is not cleared on a cache hit, contradicting DSPy's own inline comment.** `BaseLM._process_lm_response`'s comment reads "Logging, with removed api key & where `cost` is None on cache hit" (`dspy/clients/base_lm.py:300`), but the field is built unconditionally as `getattr(response, "_hidden_params", {}).get("response_cost")` (`:309`) — `Cache._prepare_cached_response` (`dspy/clients/cache.py:149-158`) clears only `response.usage = {}` and stamps `cache_hit=True`; it never touches `_hidden_params`. A cache hit therefore replays the exact same `_hidden_params["response_cost"]` the original call computed. `usage_from_response`/`cost_from_response` in the typed path make the identical read (`dspy/clients/openai_format.py:860-862`). [trap] (verified: probe `cache-hit-keeps-cost`, ran, holds — real litellm-shaped mock with `_hidden_params={"response_cost": 0.0042}`, both the fresh call and the cache-hit report `0.0042`; also verified with a minimal `Cache.put`/`.get` round trip with no `dspy.LM` involved at all) · skill: new — and directly relevant to `operations.md`'s "Cost and usage" section, which describes `lmrun.call`'s cost field as `sum(e.get("cost") or 0 for e in entries)` without noting that a cache hit's `cost` is *not* zero/None the way its `usage` is.
- **The cache-tutorial's own worked example contradicts its own prose about cache-hit usage.** `docs/docs/tutorials/cache/index.md:17` states "the usage metrics for a cached call will be `None`", but the very example two paragraphs later shows the cached call's own printed output as `Total usage: {}` (`:48`) — an empty dict, not `None`. Source confirms the dict reading is the correct one: `add_usage` never appends an empty usage dict at all (`len(usage_entry) > 0` guard, `dspy/utils/usage_tracker.py:52-55`), and no call is ever made to `add_usage` for a cache hit in the first place (`if not getattr(response, "cache_hit", False) and settings.usage_tracker: ...`, `dspy/clients/base_lm.py:294-295`) — so `get_total_tokens()` simply has no key for that model on a cache-hit-only tracker, and `Prediction.get_lm_usage()` reads back as `{}`. [trap] (verified: read, docs' own two claims disagree; matches `lm.history[-1]["usage"] == {}` asserted at `tests/clients/test_lm.py:1319,1802,1859`) · skill: new.
- **A third cache layer exists that DSPy does not control: provider-side prompt caching**, enabled via `cache_control_injection_points=[{"location": "message", "role": "system"}]` passed straight through `**kwargs` to `dspy.LM(...)`, forwarded by litellm to Anthropic/OpenAI's own prompt-cache mechanism. `docs/docs/tutorials/cache/index.md:7-13,51-76`. This is orthogonal to DSPy's in-memory/on-disk cache and to `rollout_id`. [claim] (verified: read only, not run — needs a real provider) · skill: new.
- **`restrict_pickle=True` is a real, tested defense against a concrete pickle-RCE gadget, not a vague safety knob.** `_RestrictedUnpickler.find_class` (`dspy/clients/disk_serialization.py:43-54`) allows: any class whose module starts with `litellm.types.` or `openai.types.` (`:23-26`), a fixed set of numpy reconstruction internals — `numpy.dtype`, `numpy.ndarray`, `numpy._core.numeric._frombuffer` (and the `core.numeric` pre-2.0 alias), `numpy.core.multiarray._reconstruct`/`numpy._core.multiarray._reconstruct`, `_codecs.encode` (`:28-36`) — and whatever `(module, qualname)` pairs `safe_types` names. Everything else raises `DeserializationError("Type {module}.{name} is not in the safe_types allowlist. Register it via dspy.configure_cache(safe_types=[...]).")` (`:51-54`). Proven against `numpy.ctypeslib.load_library` specifically — a crafted pickle payload invoking it is rejected (`tests/clients/test_disk_serialization.py:335-349`, read) — confirming the allowlist really is "specific reconstruction functions," not "any numpy.\*". A real litellm/openai response type (`ModelResponse`, `TextCompletionResponse`, `EmbeddingResponse`) round-trips fine even restricted (`:376-408`, read). A rejected/corrupted entry is treated as a cache **miss** and the bad disk entry is deleted, never a hard crash (`except DeserializationError: logger.debug(...); self.disk_cache.delete(key); return None`, `dspy/clients/cache.py:134-137`). [api] (verified: test read; matches skill's existing framing) · skill: same, with the numpy-gadget proof and exact allowlist as new detail — `api.md:500-515` states the flags exist but not the mechanism.
- **The cache tutorial's log-level claim for a rejected entry does not match the code.** `docs/docs/tutorials/cache/index.md:113-117` shows `WARNING dspy.clients.cache: Failed to deserialize disk cache entry <key>` as the expected log line; the actual call is `logger.debug("Failed to deserialize disk cache entry %s", key)` (`dspy/clients/cache.py:135`) — `logging.DEBUG`, not `WARNING`, so at any default logging configuration this line is silent. [trap] (verified: read both) · skill: new.
- **`configure_cache`'s `disk_cache_dir` default is a plain string literal frozen the first time `dspy.clients` is imported, not re-read from `DSPY_CACHEDIR` at call time.** `DISK_CACHE_DIR = os.environ.get("DSPY_CACHEDIR") or os.path.join(Path.home(), ".dspy_cache")` (`dspy/clients/__init__.py:15`) is a module-level constant used as `configure_cache`'s default parameter value (`:22`) — a classic eager-default-argument trap: setting `os.environ["DSPY_CACHEDIR"]` *after* `import dspy` has no effect on a bare `dspy.configure_cache()` call afterward; the caller must pass `disk_cache_dir=` explicitly. `dspy/utils/caching.py:5` computes the *same* value independently, at its own import time, for `get_finetune_directory()`/`create_subdir_in_cachedir` — two separately-frozen copies of one env lookup. `python3 -c` confirms the installed default is the literal `/root/.dspy_cache` (this container's `$HOME`). [trap] (verified: probe `configure-cache-dir-default-is-frozen-at-import`, ran, holds — `inspect.signature(dspy.configure_cache).parameters["disk_cache_dir"].default` matches `dspy.clients.DISK_CACHE_DIR` exactly, a plain string) · skill: unchecked — `api.md:500-515` and `operations.md:298-302` both state the env var and default, and correctly flag that a *different-looking* env var (`DSPY_CACHE_DIR` in one third-party repo's `.env.example`) is inert, but neither notes that even the *correct* env var, `DSPY_CACHEDIR`, must be set before `import dspy` for `configure_cache()`'s own default to see it.
- **`dspy.cache` is a fully replaceable global** — swap it entirely by assigning `dspy.cache = CustomCache(...)` after subclassing `dspy.clients.Cache` and overriding `cache_key`/`get`/`put` (the doc recommends keeping `**kwargs` in overrides for forward compatibility). The worked example customizes `cache_key` to hash only `request["messages"]`, so two different models sharing the same prompt text share a cache entry. `docs/docs/tutorials/cache/index.md:159-263`. [pattern] (verified: read, not independently run) · skill: new.
- **`Cache` ships `save_memory_cache`/`load_memory_cache`, cloudpickle-based, and `load_memory_cache` refuses without `allow_pickle=True`** the same way `dspy.load` does. `dspy/clients/cache.py:196-216`; test-confirmed (`tests/clients/test_cache.py:204-236`, read). Not mentioned anywhere in the skill. [api] (verified: test read) · skill: new.
- **`Predict`/module-level `rollout_id` plumbing exists outside this slice but is directly relevant to P18.** LM kwargs including `rollout_id`/`temperature` may be passed at `dspy.Predict(...)` construction to set per-call defaults, or overridden for one invocation via `predict(question=..., config={"rollout_id": 5, "temperature": 1.0})` (`docs/docs/learn/programming/language_models.md:218-235`). [claim] (verified: doc read only — `dspy/predict/predict.py` is outside this slice) · skill: new.
- **`allow_unsafe_lm_state` does two jobs through one flag, confirmed against the source it plumbs into.** `Module.load(path, allow_pickle=False, allow_unsafe_lm_state=False)` both (a) strips `api_base`/`base_url`/`model_list` from the saved LM state when `False` (`_sanitize_lm_state`, `dspy/predict/predict.py:25-37`, outside this slice but grepped) and (b) is passed straight through as `allow_custom_lm_class` to `BaseLM.load_state` (`dspy/clients/base_lm.py:687-731`), gating whether a *non-builtin* `BaseLM` subclass may even be imported and reconstructed from saved state — `BaseLM.load_state`'s own refusal message explicitly says "Pass `allow_unsafe_lm_state=True`..." (`:721-723`) even though the local parameter on `BaseLM.load_state` itself is spelled `allow_custom_lm_class` — this is not a documentation bug, the message is written from the public `Module.load` caller's perspective, confirmed by `docs/docs/learn/programming/language_models.md:333-339` giving the exact same call shape. [api] (verified: read + grep + doc cross-check) · skill: same, with the double-duty mechanism as new detail — `api.md:319-326` states the *effect* (`api_base`/`base_url`/`model_list` dropped) but not that the same flag also gates custom-class loading.
- **`BaseLM.copy()`'s exact contract, including a `None`-means-delete rule.** Shallow `copy.copy(self)`; `history=[]` and a fresh `callbacks` list and `kwargs` dict are isolated per copy (provider clients/sessions/local-model handles stay shared by reference). For each passed kwarg: if the copy already has that attribute, `setattr` it; if the key is (already) in `kwargs`, **or** it is not a real attribute on `self` at all, update `kwargs` too — and passing `value=None` there **deletes** the key from `kwargs` rather than storing `None`. `dspy/clients/base_lm.py:735-771`. [api] (verified: read; matches `docs/docs/learn/programming/language_models.md:341-346`) · skill: unchecked — `api.md` never documents `copy()`'s own signature or the delete-on-`None` behavior, only cites it in passing for `rollout_id`.
- **`GLOBAL_HISTORY` and per-LM `.history` have independent, only-coincidentally-equal caps, and one keeps growing when you think you turned it off.** `GLOBAL_HISTORY` is capped by the hardcoded module constant `MAX_HISTORY_SIZE = 10_000` (`dspy/clients/base_lm.py:22-23`) and is **never** consulted for `settings.max_history_size`. `update_history` appends to `GLOBAL_HISTORY` first — gated only by `settings.disable_history` — and *only then* checks `if settings.max_history_size == 0: return`, which skips appending to `self.history` and to every module in `settings.caller_modules`, but has already appended to `GLOBAL_HISTORY`. `dspy/clients/base_lm.py:776-800`. `settings.max_history_size` itself defaults to `10000` (`dspy/dsp/utils/settings.py:35`, grepped — same value as `MAX_HISTORY_SIZE`, coincidentally, not by reference). So **setting `dspy.configure(max_history_size=0)` to save memory on `lm.history` does not stop `dspy.inspect_history()`'s global log from growing** (up to 10,000 entries, each holding the full prompt/response). [trap] (verified: read) · skill: new.
- **`dspy.inspect_history()`/`lm.inspect_history()` never print usage or cost — you must read `lm.history[-1]["usage"]`/`["cost"]` directly.** `pretty_print_history` (`dspy/utils/inspect_history.py:27-107`) prints timestamp, every message (with images/audio/files rendered as length-only placeholders, never the base64 payload itself — `:63-89`), tool calls, and the response text; no usage/cost field is touched anywhere in the function. It also indexes `outputs[0]` unconditionally (`:93,101`), so a history entry with an empty `outputs` list would raise `IndexError`, uncaught. [trap] (verified: read) · skill: new.
- **Calling an LM directly returns a list of strings only when no output carries extra structure; otherwise a list of dicts.** `BaseLM._process_completion` (`dspy/clients/base_lm.py:802-836`) builds one dict per choice with `text` always, plus `reasoning_content` if non-empty, `logprobs` if the caller asked for them, `tool_calls` if present, `citations` if the provider returned any (via `provider_specific_fields["citations"]`, litellm's Anthropic citations passthrough, `:838-854`). Only `if all(len(output) == 1 for output in outputs)` — i.e. every output is *just* `{"text": ...}` — does the whole list collapse to plain strings (`:833-836`). [trap] (verified: read; the installed `check_dspy_skill.py` probe for this only exercises the plain-string case — see Probes below) · skill: unchecked — `api.md:311-313`'s `[checked: lm-call-returns-list]` mark and its probe (`scripts/check_dspy_skill.py:483-485`) verify only `FixtureLM(lambda messages: "hallo")("frage") == ["hallo"]`, the trivial case; nothing checks the dict-fallback path.
- **`lm.history[i]["usage"]` is the provider's raw dict, not a normalized DSPy type** — the legacy `.history` entry stores `dict(getattr(response, "usage", {}) or {})` verbatim (`dspy/clients/base_lm.py:295,308`), whatever shape the provider/litellm returned (typically OpenAI-style `prompt_tokens`/`completion_tokens`/`total_tokens` plus nested `*_details` dicts, per the cache tutorial's own sample output at `docs/docs/tutorials/cache/index.md:45`). Only the new typed path normalizes usage into `LMUsage` via `usage_from_response` (`dspy/clients/openai_format.py:865-884`). [api] (verified: read) · skill: new.
- **A parallel typed call path, `LMRequest`/`LMResponse`, exists behind `dspy.context(experimental=True)`, is a documented multi-release migration, and changes the *default* return type of `lm(...)` starting at 3.5.** `BaseLM.__call__` (`dspy/clients/base_lm.py:321-373`) routes to the typed path when `request=` is given, the first positional item is an `LMRequest`, `dspy.context(experimental=True)` is active, or the LM class declares `forward_contract = "typed_lm"`; otherwise it returns the legacy `list[str|dict]`. Top-level typed names confirmed real by the migration doc itself: `dspy.LMRequest`, `dspy.LMResponse`, `dspy.System`, `dspy.User`, `dspy.Assistant`, `dspy.ToolCall`, `dspy.ToolResult`; the full vocabulary lives under `dspy.core.types` (e.g. `LMTextPart`, `LMImagePart`). `docs/docs/community/normalized-lm-api-migration.md:107`. **Version sequence** (`:218-227`, a table): 3.3 (now) — typed only via `experimental=True`; 3.4 — a missing `forward_contract` on a custom LM warns; 3.5 — **the typed path becomes the default `lm(...)` return type**, with a legacy escape hatch; 3.6/4.0 — the legacy `forward(prompt, messages, **kwargs)` contract is removed outright. [claim for the version table specifically, api for the rest] (verified: read source + doc; the migration doc is explicit that "names and exact release timing may change") · skill: new — and a genuine forward-compatibility risk for this repository: `lmrun.py` reads `lm.history[before:]` as a list of dicts and treats a direct LM call's return as `list[str|dict]` (`operations.md:27-28`); if `.venv-dspy` is ever bumped past 3.3.1/3.4 without re-checking this file, `dspy.LM(...)()`'s return shape may change under it.
- **`BaseLM.forward_contract` is already correctly taught by the skill** — the two contracts (`"legacy"`: `forward(prompt=None, messages=None, **kwargs)`; `"typed_lm"`: `forward(request: LMRequest) -> LMResponse`), the default of `"legacy"`, and the double-counting-usage trap for a custom subclass. `dspy/clients/base_lm.py:57-274`. [api] (verified: read) · skill: same — `api.md:346-364` states this correctly; the *rest* of the typed-call mechanism (`__call__`'s routing, `experimental=True`, top-level typed names, the version table) is what is missing.
- **`dspy.Embedder(model_or_callable, batch_size=200, caching=True, **kwargs)` supports a fully local, no-provider embedder: any callable `list[str] -> 2D array-like`.** `dspy/clients/embedding.py:86-90`. The doc's own second example is `dspy.Embedder(SentenceTransformer(...).encode)` — genuinely local, no key, no network once weights are downloaded (`docs/docs/api/models/Embedder.md` cross-referenced against the docstring at `dspy/clients/embedding.py:54-68`). `dspy.Embedder` requires the `numpy` extra: `pip install dspy[numpy]` (`docs/docs/api/models/Embedder.md:3-4`, `docs/docs/api/tools/Embeddings.md:3-4`). [api] (verified: read + doc) · skill: unchecked — `retrieval.md:264-266` already names the pattern from a third-party skill's example; it does not cite the `pip install dspy[numpy]` requirement or that `dspy.Embedder` is *itself* the mechanism (not something bolted on).
- **`Embedder`'s own `caching=` kwarg never actually reaches litellm as `True`.** `_compute_embeddings` recomputes `caching = caching and _get_litellm().cache is not None` before calling `litellm.embedding(..., caching=caching, ...)` (`dspy/clients/embedding.py:157-161`); since litellm's own cache is always `None` under DSPy (`_configure_litellm_defaults`, above), this is always `False` regardless of what `Embedder(caching=True)` requested — test-confirmed: `mock_litellm.assert_called_once_with(model=model, input=inputs, caching=False)` even when the `Embedder` itself was constructed `caching=True` (`tests/clients/test_embedding.py:27-49`, read, its own comment: "Because we disable the litellm cache, it should be called with caching=False"). The *actual* caching for a hosted embedder happens one level up, through DSPy's own `request_cache`-wrapped `_cached_compute_embeddings` — `Embedder.caching=True` selects that wrapper (`dspy/clients/embedding.py:138`), it does not turn on anything inside litellm. [trap] (verified: test read) · skill: unchecked — `retrieval.md:225-230` already flags the *naming* mismatch between `Embedder.caching` (default `True`) and `Embeddings.cache` (default `False`); it does not know that `Embedder`'s own inner `caching=` kwarg to litellm is a dead flag.
- **Per-call `caching=` on `Embedder.__call__`/`.acall` overrides the instance default in both directions, test-proven for sync and async.** `tests/clients/test_embedding.py:156-198`, read: `Embedder(model, caching=True)` then `embedding(inputs, caching=False)` makes 2 real calls where the plain repeat would have made 1; `Embedder(model, caching=False)` then two calls each with `caching=True` makes only 1. Same for `acall`. [api] (verified: test read) · skill: new.
- **`Embedder(123)` (an invalid model type) does not raise at construction — only on first call.** The type check (`str` or `callable`) lives in `_compute_embeddings`, not `__init__` (`dspy/clients/embedding.py:86-90,157-165`); `Embedder(123)` alone succeeds, `Embedder(123)(["x"])` raises `ValueError`. `tests/clients/test_embedding.py:125-129`, read. [trap] (verified: test read) · skill: new (minor).
- **`Embedder`'s own cache key for a hosted model includes the literal batch of text being embedded, plus a mangled positional-argument name.** `_cached_compute_embeddings`/`_cached_acompute_embeddings` are `@request_cache(ignored_args_for_cache_key=[...])` with **no** `cache_arg_name`, so per `request_cache`'s own contract the *entire* call is hashed: `model` and `batch_inputs` arrive positionally and get renamed `positional_arg_0`/`positional_arg_1` in the hashed dict (`dspy/clients/cache.py:253-262`), so the cache key is built from the model identifier (or its source code, if callable) and the actual text batch, plus `_fn_identifier`. Different from `dspy.LM`'s cache, which is keyed off one named `request=` argument. `dspy/clients/embedding.py:168-186`. [api] (verified: read) · skill: new.
- **`dspy.Embedder.acall` exists and is not in the skill's surface block at all.** `dspy/clients/embedding.py:146-154`. [api] (verified: `inspect.signature`) · skill: new — `retrieval.md:225-226` states `dspy.Embedder(model, batch_size=200, caching=True)` as the whole surface.
- **`dspy.Embeddings(..., cache=True)` always raises `AssertionError` at construction; `cache` exists only to be asserted `False`.** `assert cache is False, "Caching is not supported for embeddings-based retrievers"` (`dspy/retrievers/embeddings.py:31`). The `Embedder` passed to it is still cached (or not) by its own `caching=`; `Embeddings.cache` is a dead knob whose only legal value is its default. [trap] (verified: probe `embeddings-cache-must-be-false`, ran, holds) · skill: unchecked — `retrieval.md:225-230` states the default (`cache=False`) but not that any other value is a hard construction-time error.
- **`Embeddings` similarity is cosine only because `normalize=True` is the default; the score is a raw dot product otherwise.** `_rerank_and_predict` computes `np.einsum("qd,qkd->qk", q_embeds, candidate_embeddings)` (`dspy/retrievers/embeddings.py:96-98`) — a batched dot product; `normalize=True` (default) L2-normalizes both query and corpus embeddings first (`_normalize`, `:110-112`), which is what makes that dot product a cosine similarity. `normalize=False` turns it into a raw, magnitude-sensitive inner product. [api] (verified: read) · skill: new — `retrieval.md` doesn't discuss `normalize` at all.
- **The FAISS index parameters are concrete and non-default-obvious: `IndexIVFPQ` with 32-byte codes, `nlist = 2·sqrt(N)`, `nprobe = min(16, nlist)`, and a 10× overfetch before exact rerank.** `_build_faiss` (`dspy/retrievers/embeddings.py:70-91`): `nbytes=32`, `partitions=int(2*sqrt(len(corpus)))`, quantizer `IndexFlatL2(dim)`. `_batch_forward` (`:61-68`) asks FAISS for `self.k*10` candidates before the exact cosine rerank narrows to `k`. Missing `faiss-cpu` above `brute_force_threshold=20000` raises exactly `"Please \`pip install faiss-cpu\` or increase \`brute_force_threshold\` to avoid FAISS."` (`:78`). [api] (verified: read; matches the skill's existing threshold claim) · skill: same for the threshold, new for the exact IVFPQ parameters and the 10× overfetch — `retrieval.md:244-248` states the threshold and the missing-package message but not `nbytes`/`nlist`/`nprobe`/the overfetch factor.
- **`Embeddings.save`/`.load` never persist or check the embedder's identity — confirmed directly in DSPy's own source, not only as a third-party recipe.** `save()` writes `config.json` with only `k`, `normalize`, `corpus`, `has_faiss_index` (`dspy/retrievers/embeddings.py:127-135`); `corpus_embeddings.npy` and, if present, `faiss_index.bin`. `load(path, embedder)` takes `embedder` as a caller-supplied argument and never compares it against anything saved — nothing prevents `Embeddings.from_saved(path, a_different_embedder)` from silently mixing vector spaces. `from_saved` bypasses `__init__` entirely via `cls.__new__(cls)` so no embedding computation happens on load (`:209-239`). `from_saved` **is** a `@classmethod` (`:209`), confirmed directly. [api] (verified: read) · skill: **wrong→now confirmed, was previously only a claim** — `retrieval.md:249-259` already states both facts (no manifest check; `from_saved` is a classmethod, correcting a third-party skill's "staticmethod" claim) but sources them to `dspy-agent-skills`' recipe/critique; this read verifies both directly against DSPy's own shipped code, upgrading them from cited-claim to source-verified.
- **`dspy.Retrieve`'s contract is exactly one thing: `dspy.settings.rm(query, k=k, **kwargs)` must return an iterable of objects each exposing `.long_text`.** `Retrieve.forward` (`dspy/retrievers/retrieve.py:43-65`): if `dspy.settings.rm` is falsy, raises a bare `AssertionError("No RM is loaded.")` — not a typed DSPy error, no `LMError` relation at all; otherwise wraps a non-iterable single result in a list, then does `[psg.long_text for psg in passages]` unconditionally. `dspy.Retrieve(k=3, callbacks=None)`. [api] (verified: read) · skill: new — `retrieval.md`'s DSPy-primitives section states the surface line but not the `.long_text` contract or the untyped `AssertionError`.
- **`WeaviateRM.forward`'s docstring says it returns `dspy.Prediction`; the code returns a bare `list[dotdict]`.** `dspy/retrievers/weaviate_rm.py:73-111`: the docstring at `:81-82` reads "Returns: dspy.Prediction: An object containing the retrieved passages," but `forward` builds `passages.extend(dotdict({"long_text": d}) for d in parsed_results)` per query and returns `passages` — a plain list, never wrapped in `Prediction(...)`. This still works when `WeaviateRM` is assigned to `dspy.settings.rm` (since `Retrieve.forward` only needs `.long_text` per item, not a `Prediction`), but calling `WeaviateRM(...)` directly and reading `.passages` off the result, as the class's own module docstring examples at `:39-41` show (`retrieve("...").passages`), only works because that call goes through the base `Retrieve.__call__`→`forward`, which *is* `Prediction`-wrapping — calling `WeaviateRM.forward` directly, or any code that assumes its return has `.passages`, does not get one. [trap] (verified: read) · skill: new.
- **`dspy.ColBERTv2(post_requests=True)` returns records without a `long_text` key; `dspy.Retrieve`/anything doing `.long_text` on them will raise `AttributeError`.** `colbertv2_get_request_v2` adds the key: `topk = [{**d, "long_text": d["text"]} for d in topk]` (`dspy/dsp/colbertv2.py:56`); `colbertv2_post_request_v2` does not — it returns `res_json["topk"][:k]` verbatim (`:82`). Test-confirmed: the GET-path unit test asserts `result[0]["long_text"]` (`tests/retrievers/test_colbertv2.py:26-32`), the POST-path test asserts `result[0]["text"]` — no `long_text` check, because there is no `long_text` key (`:35-41`). `ColBERTv2.__call__` wraps either path's result identically as `dotdict(psg)` when `simplify=False` (`dspy/dsp/colbertv2.py:37`), so a `dotdict(psg).long_text` access on a POST-sourced record raises `AttributeError`. [trap] (verified: test read) · skill: new — the skill's surface line for `ColBERTv2` doesn't mention `post_requests` changes the result shape at all.
- **`dspy.ColBERTv2`'s GET path hard-caps `k<=100`; the POST path does not.** `assert k <= 100, "Only k <= 100 is supported for the hosted ColBERTv2 server at the moment."` exists only in `colbertv2_get_request_v2` (`dspy/dsp/colbertv2.py:42`), not in `colbertv2_post_request_v2`. Both use a hardcoded 10-second `requests` timeout (`:45,72`), not configurable through `dspy.ColBERTv2(...)`. [trap] (verified: read) · skill: unchecked — the skill's `ColBERTv2(url=..., port=None, post_requests=False)` surface line names no `k` limit or timeout at all.
- **`dspy.ColBERTv2`'s GET and POST request functions are each wrapped by `@request_cache()` twice — once directly, once through a same-named wrapper that calls the first.** `colbertv2_get_request_v2` is `@request_cache()`-decorated (`dspy/dsp/colbertv2.py:40-41`); `colbertv2_get_request` (the name `ColBERTv2.__call__` actually uses, `:65`) is `colbertv2_get_request_v2_wrapped`, itself `@request_cache()`-decorated and whose body is just `return colbertv2_get_request_v2(*args, **kwargs)` (`:60-63`). Same shape for POST (`:85-90`). A cold call therefore does two separate `dspy.cache` lookups/writes under two different `_fn_identifier`s (`...colbertv2_get_request_v2` and `...colbertv2_get_request_v2_wrapped`) for what is functionally one request. Not incorrect, just doubled work and a doubled cache footprint. [trap] (verified: read) · skill: new.
- **Two fully-local, provider-free retrieval/rerank classes exist in `dsp/colbertv2.py` and are unrelated to the hosted `ColBERTv2` server class.** `ColBERTv2RetrieverLocal(passages, colbert_config, load_only=False)` (`dspy/dsp/colbertv2.py:93-186`) needs the real `colbert-ai` package and a `ColBERTConfig` with `checkpoint`/`index_name` set (hard `AssertionError`s otherwise with instructive messages, `:102-114`); its `forward(query, k=7, ...)` default `k` is **7**, different from `ColBERTv2`'s default `k=10`. `ColBERTv2RerankerLocal(colbert_config=None, checkpoint="bert-base-uncased")` (`:189-233`) scores query/passage pairs with the real ColBERT model and returns a raw `np.ndarray`, not a `Prediction` or `dotdict` list. Both need `colbert-ai[faiss-gpu,torch]`, realistically GPU-shaped (matching this container's CPU-only posture the way `grawiki`'s `--torch-backend cpu` already does for a different library). Both classes' own `import colbert` failure paths only **print** a message and continue (`:131-137,147-153,191-197`) — the real `ModuleNotFoundError` then surfaces moments later from a subsequent `from colbert... import ...` line, an inconsistent double-signal rather than one clean early failure. [api/trap] (verified: read) · skill: new — nothing in `retrieval.md` mentions either class.
- **`DatabricksRM` is never auto-inferred and needs no special package to import**, unlike Weaviate. `dspy/retrievers/databricks_rm.py` has no top-level provider import guard; `_databricks_sdk_installed = find_spec("databricks.sdk") is not None` (`:12`) chooses between an SDK path and a plain `requests`-based path (`:253-278`) at call time. `use_with_databricks_agent_framework=True` additionally needs `mlflow` (raised as `ValueError`, not `ImportError`, `:169-173`). Neither `DatabricksRM` nor `WeaviateRM` is re-exported at the `dspy` top level or from `dspy.retrievers.__all__` (`dspy/retrievers/__init__.py`, 4 lines: only `Embeddings`, `EmbeddingsWithScores`, `Retrieve`) — both need an explicit submodule import (`from dspy.retrievers.databricks_rm import DatabricksRM`). Confirmed by grepping `dspy/__init__.py`: it imports `ColBERTv2` directly (`from dspy.dsp.colbertv2 import ColBERTv2`) and `from dspy.retrievers import *`, nothing else names either RM class. [api] (verified: read + grep) · skill: new.
- **`WeaviateRM`/`DatabricksRM` need extras DSPy does not install by default** — `weaviate_rm.py:6-14` fails at import with `"The 'weaviate' extra is required to use WeaviateRM. Install it with pip install dspy-ai[weaviate]"` if `weaviate` isn't present; `databricks_rm.py` needs `databricks-sdk` only when `_databricks_sdk_installed` is checked, or falls back to plain `requests`. [api] (verified: read) · skill: new (minor, low priority given no provider is used here).
- **`dotdict`/`dotdict_lax` are the shared glue behind every retriever's `.long_text` contract, and they differ on a missing key.** `dotdict(dict)` (`dspy/dsp/utils/utils.py:101-124`) raises `AttributeError` for a missing key (via `__getattr__`'s `except KeyError: raise AttributeError(...)`); `dotdict_lax` (`:127-130`) instead aliases `__getattr__ = dict.get`, so a missing key silently returns `None`. Every retriever in this slice (`ColBERTv2`, `ColBERTv2RetrieverLocal`, `WeaviateRM`) builds `dotdict`, not `dotdict_lax` — so a genuinely missing `long_text` (the `post_requests=True` trap above) is a loud `AttributeError`, not a silent `None`. [api] (verified: read) · skill: new.

## RAG

- **`graphrag.py` calls none of DSPy's retrieval primitives — already correctly stated by the skill and reconfirmed here from the other direction.** Nothing in `dspy/retrievers/`, `dspy/dsp/colbertv2.py`, or `dspy.Retrieve` shows any coupling to `scripts/graphrag.py`'s own hand-rolled seeding/PageRank/MMR pipeline; `retrieval.md:220-223` already states this plainly ("`graphrag.py` calls none of these"). [pattern] (verified: read this slice, cross-checked against `retrieval.md`) · skill: same.
- **The official DSPy multi-hop RAG tutorial (not a third-party repository) uses exactly the fixed-depth `question, notes -> query` / `question, notes, context -> new_notes` shape the skill already documents from `dspy-agent-skills`, with a concrete `num_hops=4` default.** `docs/docs/tutorials/multihop_search/index.ipynb`, cell 16: `class Hop(dspy.Module)` with `num_docs=10, num_hops=4`, `self.generate_query = dspy.ChainOfThought('claim, notes -> query')`, `self.append_notes = dspy.ChainOfThought('claim, notes, context -> new_notes: list[str], titles: list[str]')`, looping `num_hops` times, deduping titles with `list(set(titles))` at the end. Retrieval itself is a hand-rolled BM25 function (`bm25s` library) called directly inside `forward`, not any DSPy retriever class. [api] (verified: notebook read) · skill: unchecked — `retrieval.md:412-437` attributes this exact pattern only to `dspy-agent-skills:skills/dspy-book-agents/...`; it is also DSPy's own official tutorial's pattern, one authoritative source rather than only a third-party one.
- **The official RAG tutorial's retriever is exactly `dspy.Embedder` + `dspy.retrievers.Embeddings`, using a real, concrete OpenAI call shape.** `docs/docs/tutorials/rag/index.ipynb`, cell 30: `embedder = dspy.Embedder('openai/text-embedding-3-small', dimensions=512)`; `search = dspy.retrievers.Embeddings(embedder=embedder, corpus=corpus, k=topk_docs_to_retrieve)`. `dimensions=512` is an extra kwarg flowing straight through `Embedder.__init__`'s `**kwargs` into the litellm embedding call (OpenAI's newer embedding models support truncating output dimensionality this way) — a concrete example of the pass-through kwargs mechanism. [api] (verified: notebook read) · skill: new (as a concrete worked example; the classes themselves are already documented).

## PROD

- **DSPy's own production story is entirely MLflow-shaped, and MLflow is not installed here.** `docs/docs/production/index.md` points every production concern (observability, reproducibility, deployment, scalability) at MLflow tracing/model-serving; the deployment tutorial's two paths are FastAPI (`dspy.asyncify`) or MLflow (`mlflow.dspy.log_model` + `mlflow models serve`). `operations.md:364-397` already establishes MLflow is absent from `.venv-dspy` and that `lmrun.py`'s own JSONL record plays the role a trace would. [pattern] (verified: docs read) · skill: same, corroborated from the docs side rather than only the four scanned repositories.
- **`dspy.asyncify`'s worker-pool default is 8, configurable via `dspy.configure(async_max_workers=N)`, and is literally a worker pool, not a rate limiter tied to the provider.** "If you have 8 in-flight programs and call it once more, the 9th call will wait until one of the 8 returns." `docs/docs/tutorials/deployment/index.md:59-64`. Matches `api.md`'s already-known `async_max_workers=8` default. [api] (verified: doc read) · skill: same.
- **MLflow deployment as of 2.22.0 requires wrapping a `dspy.Predict`/`ChainOfThought` in a custom `dspy.Module` subclass** because MLflow's serving contract needs positional arguments and DSPy's built-in modules disallow them. `docs/docs/tutorials/deployment/index.md:152-186`. [claim] (verified: doc read only, no MLflow installed to run it against) · skill: new (low priority — not used here).
- **DSPy's own local-serving launcher (`LocalProvider`) binds its SGLang server to all interfaces, `0.0.0.0`, while the client that talks to it uses `localhost`.** `command = ["python", "-m", "sglang.launch_server", "--model-path", model, "--port", str(port), "--host", "0.0.0.0"]` (`dspy/clients/lm_local.py:58-68`); the client is then pointed at `lm.kwargs["api_base"] = f"http://localhost:{port}/v1"` (`:124-125`). Readiness is polled against `{base_url}/v1/models` with the literal header `Authorization: Bearer None` (the string `"None"`, `:346-349`), timeout defaulting to 1800s (`launch_kwargs.get("timeout", 1800)`, `:57`). In a container with the launching port exposed externally, this server is reachable from outside the box even though the *client's* own connection stays local. `.launch()`/`.kill()` require `sglang` to be importable and require passing `provider=LocalProvider()` explicitly to `dspy.LM(...)` — `LocalProvider` never overrides `is_provider_model` (inherits `Provider`'s hardcoded `False`, `dspy/clients/provider.py:219-232`), so it is never auto-inferred from a model string the way `OpenAIProvider` is. `subprocess.Popen` is always given a `list`, never `shell=True` — model-name shell-injection is structurally ruled out (`tests/clients/test_lm_local.py:37-65`, read). [prod/trap] (verified: read + test read) · skill: unchecked — `operations.md:448-501` documents a *different* "local runtime" pattern entirely (a third-party Claude-CLI-backed `BaseLM`); it never mentions this repository has DSPy's own SGLang launcher available, nor its `0.0.0.0` bind.
- **`dspy.LM(...).finetune()` on an "openai/"-prefixed model reaches the real OpenAI cloud API regardless of any `api_base` override on the LM.** `OpenAIProvider.is_provider_model` matches any model string starting with `"openai/"` or `"ft:"` purely by prefix (`dspy/clients/openai.py:48-55`) — including a model pointed at a fully local OpenAI-compatible server via `api_base=`. But `OpenAIProvider.finetune`/`upload_data`/`_start_remote_training`/`wait_for_job` all call the bare `openai.*` SDK functions directly (`openai.files.create`, `openai.fine_tuning.jobs.create`, `.retrieve`, `.list_events`, `dspy/clients/openai.py:166-227`) — the raw `openai` package's own implicit global client, configured via its own `OPENAI_API_KEY`/`OPENAI_BASE_URL` env vars or SDK defaults, **not** the `api_base`/`api_key` the `dspy.LM` instance was constructed with. So a local-server LM that answers inference calls entirely on-box would still, if `.finetune()` were called on it, attempt to reach `https://api.openai.com` (or wherever the bare SDK is pointed) rather than the local endpoint. Not exercised by this repository's pipeline (nothing here calls `.finetune()`), but directly answers the brief's "whether any request can leave the machine" for the one DSPy-native LM method where the answer is "yes, by a different mechanism than the one used for inference." [trap] (verified: read) · skill: new.
- **`ParallelExecutor`/`dspy.Parallel` gives each worker thread its own deep-copied `UsageTracker`, and the parent tracker sees none of it — proven with real numbers, not just cited.** `tests/utils/test_usage_tracker.py:342-393` (the whole test read): two tasks run under `dspy.Parallel()` inside one `with dspy.context(track_usage=True, usage_tracker=parent_tracker):` block each record their own distinct token counts (task1: 50 prompt/10 completion; task2: 80/15) with zero cross-contamination, and the comment confirms the parent tracker is asserted unchanged afterward. Matches and strengthens `operations.md:119-129`'s citation of the same mechanism (there sourced to a scanned repository's measurement plus DSPy's own source comment; here directly run/read as DSPy's own test). [prod] (verified: test read) · skill: same, upgraded from cited-elsewhere to directly-confirmed.
- **`UsageTracker.add_usage` silently no-ops on an empty usage dict — a real call with no usage data simply never appears in `get_total_tokens()`, with no error and no zero-valued entry.** `if len(usage_entry) > 0: self.usage_data[lm].append(...)` (`dspy/utils/usage_tracker.py:52-55`) — this is the same mechanism that makes a cache hit invisible to `track_usage()` (cache hits are already filtered out one level up, `dspy/clients/base_lm.py:294`), but it would equally hide a real call from a provider that simply returns no usage block. [prod/trap] (verified: read) · skill: unchecked — `operations.md` already documents the cache-hit case; not this more general empty-dict guard.
- **A usage entry's values that are pydantic `BaseModel`s (e.g. litellm's `PromptTokensDetailsWrapper` for `prompt_tokens_details`) are flattened to plain dicts on the way in, but only one level deep; merging across multiple calls (`get_total_tokens`) recursively sums nested dict values.** `_flatten_usage_entry` (`dspy/utils/usage_tracker.py:25-33`) converts top-level `BaseModel` values via `.model_dump()`; `_merge_usage_entries` (`:35-50`) recursively merges/sums matching keys, including nested dicts, treating `None` as `0` when summing (`(current_v or 0) + (v or 0)`). [prod] (verified: read) · skill: new.

## TEST

- **`lm_fixture.FixtureLM` cannot be used to test DSPy's caching mechanism at all** — its constructor hardcodes `cache=False` (`scripts/lm_fixture.py:92`, `super().__init__(model=model, cache=False)`), so any cache-key/rollout_id/cache-hit behaviour must be probed against a real `dspy.LM` with `litellm.completion` monkeypatched — the exact technique DSPy's own `tests/clients/test_lm.py` uses throughout (`test_dspy_cache`, `test_rollout_id_bypasses_cache`, etc.), and the technique this reader's own probes use. [pattern] (verified: read `lm_fixture.py` + DSPy's own tests) · skill: new — worth stating explicitly in `testing.md` so a future reader doesn't try to reach for `FixtureLM` for a cache question and wonder why nothing ever hits.
- **DSPy's own `restrict_pickle` test suite includes a live attack payload, not just positive-path round-trips**, and a corrupt-pickle case that must surface as `DeserializationError`, not a raw `pickle.UnpicklingError`. `tests/clients/test_disk_serialization.py:335-349` (a hand-built pickle stream invoking `numpy.ctypeslib.load_library`) and `:360-366` (`test_corrupt_pickle_raises_deserialization_error`, flipping bytes in a valid pickle stream). [pattern] (verified: read) · skill: new.
- **Rollout-id/cache-key regression coverage in DSPy's own suite is exact and numeric**, not just directional: `test_rollout_id_bypasses_cache` (`tests/clients/test_lm.py:134-178`) walks five calls and asserts usage-tracker entry counts of `1,0,1,1,0` respectively, then a final `len(dspy.cache.memory_cache) == 3`. This is the kind of assertion shape (exact counts, not "changed"/"unchanged") this repository's own `P18`/baseline discipline already favors. [pattern] (verified: read) · skill: new (as a citable worked pattern for writing a similar assertion in this repository's own tests).

## PAT

- **The "point `dspy.LM` at a local OpenAI-compatible server" recipe is a one-line convention, not special code**: `dspy.LM("openai/<served-model-name>", api_base="http://127.0.0.1:PORT/v1", api_key="", model_type="chat")` — the `openai/` prefix selects litellm's OpenAI-compatible chat-completions path, and `api_base` redirects it; nothing provider-specific runs. Documented for three concrete cases: an SGLang server the user starts by hand (`docs/docs/learn/programming/language_models.md:91-108`), Ollama's OpenAI-compatible endpoint (`ollama_chat/llama3.2`, `api_base='http://localhost:11434'`, `:110-124`), and any "OpenAI-compatible" third-party provider generically (`:139-145`). A llama.cpp server exposing an `/v1` OpenAI-compatible surface (the brief's own example) needs nothing beyond this pattern — an empty or dummy `api_key` if the server doesn't check one, `model_type="chat"` unless the server serves a legacy completions endpoint. [pattern] (verified: doc read) · skill: new — the skill has no worked "point at a local server" recipe at all today; this is the one to add.
- **DSPy explicitly warns against two Vertex AI config-naming pitfalls that silently misroute a request**: using `gemini/` instead of `vertex_ai/` routes to the wrong API entirely (needs a key instead of GCP credentials); passing `project`/`location` instead of `vertex_project`/`vertex_location` is silently ignored by litellm, which then "falls back to defaults, which may cause requests to land in an unintended region." `docs/docs/learn/programming/language_models.md:78-80`. [claim] (verified: doc read, not run — no GCP credentials here) · skill: new (low priority, no Vertex use here).
- **Errors are meant to be caught by specific subclass, and DSPy's own guide shows the intended shape**: catch `ContextWindowExceededError` first (shrink the prompt, don't blindly retry), `LMRateLimitError` for `.provider`/`.retry_after`, generic `LMError` last for `.code`/`.model`/`.request_id`. `docs/docs/learn/programming/language_models.md:253-269`. [pattern] (verified: doc read) · skill: same in substance — `operations.md:215-253` already teaches "never a bare `except`" and a typed-catch discipline; this is the same discipline from DSPy's own docs, worth citing as corroboration rather than only third-party evidence.

## TRAP

(Every item tagged `[trap]` above belongs here too by the brief's own definition; the following are trap-shaped findings that don't fit cleanly under a single API/PROD bullet above.)

- **The skill's own rollout_id/temperature claim and DSPy's own runtime warning text share the same imprecision, and both are contradicted by DSPy's own docs and by direct testing.** See the API-section item above; restated here because it is this slice's single most important correction relative to the brief's explicit "repeats that measure something — P18" concern: **rollout_id always changes the cache key; only the resulting *output* is unaffected at `temperature=0`.** A pipeline here relying on rollout_id to force fresh calls at `temperature=0` (e.g. to sample the same prompt against a model whose greedy decoding is not perfectly deterministic in practice, or simply to record a fresh timestamped call) will in fact get fresh calls — the risk is the opposite of what the skill currently implies: someone reading `api.md:261-264` today might wrongly conclude rollout_id is *useless* at `temperature=0` and reach for `temperature>0` unnecessarily, when the real, narrower caveat is only about whether the text comes back different.
- **`dspy.LM(...).finetune()` on an `openai/`-prefixed local-server model silently targets the real OpenAI API** (full detail under PROD, above) — the one place in this slice where "point at a local server" and "nothing leaves the machine" diverge for a *specific, named* method.
- **Two independently-defined, disagreeing `_is_openai_reasoning_model` functions ship in 3.3.1** (full detail under API, above) — a real inconsistency between the legacy and typed request-building paths, not a misreading; the disagreement is specifically about `o5` and about token-minimum enforcement.
- **DSPy's own inline comment about cache-hit cost is wrong, verified two ways** (full detail under API, above): a raw `Cache.get`/`.put` round trip and a full `dspy.LM(...)()` call both show `cost` unchanged on a cache hit, contradicting the comment right above the code that builds it.
- **The cache tutorial's own prose ("usage will be `None`") is contradicted by its own example's shown output (`{}`)** (full detail under API, above).
- **The cache tutorial shows a `WARNING`-level log line for a rejected pickle entry; the code logs at `DEBUG`** (full detail under API, above) — a default-configured process will never see this line at all.
- **`configure_cache`'s `disk_cache_dir=` default is frozen at `dspy.clients` import time, so setting `DSPY_CACHEDIR` after `import dspy` and then calling `dspy.configure_cache()` with no arguments silently uses the old value** (full detail under API, above).
- **`WeaviateRM.forward`'s own docstring names a return type (`dspy.Prediction`) the method does not return** (full detail under API, above).
- **`dspy.ColBERTv2(post_requests=True)` drops the `long_text` field every downstream consumer needs** (full detail under API, above).

## 3. Code worth keeping

**The full litellm-exception → DSPy-exception mapping** (`dspy/clients/lm.py:726-776`, ran indirectly via `tests/clients/test_lm.py:279-313`):

```python
def _lm_error_class_from_litellm_exception(exc: Exception) -> type[LMError] | None:
    message = _exception_message(exc).lower()
    class_name = type(exc).__name__.lower()
    if _exception_status(exc) is None and any(
        phrase in message for phrase in ("api key", "apikey", "credentials", "environment variable")
    ):
        return LMNotConfiguredError
    if "timeout" in class_name or "timed out" in message or "timeout" in message:
        return LMTimeoutError
    if "connection" in class_name or "network" in message or "connection" in message:
        return LMTransportError

    mappings = [
        ("AuthenticationError", LMAuthError), ("RateLimitError", LMRateLimitError),
        ("NotFoundError", LMUnsupportedModelError), ("UnsupportedParamsError", LMUnsupportedFeatureError),
        ("UnprocessableEntityError", LMInvalidRequestError), ("ContentPolicyViolationError", LMInvalidRequestError),
        ("BadRequestError", LMInvalidRequestError), ("InvalidRequestError", LMInvalidRequestError),
        ("InternalServerError", LMServerError), ("ServiceUnavailableError", LMServerError),
        ("APIConnectionError", LMTransportError), ("APIResponseValidationError", LMProviderError),
        ("BudgetExceededError", LMBillingError), ("RouterRateLimitError", LMRateLimitError),
    ]
    for litellm_name, dspy_cls in mappings:
        litellm_cls = _safe_litellm_exception_class(litellm_name)
        if litellm_cls is not None and isinstance(exc, litellm_cls):
            return dspy_cls
    return None


def _lm_error_class_from_status(status: int | None) -> type[LMError]:
    if status in (401, 403): return LMAuthError
    if status == 402: return LMBillingError
    if status == 404: return LMUnsupportedModelError
    if status == 408: return LMTimeoutError
    if status == 429: return LMRateLimitError
    if status is not None and 400 <= status < 500: return LMInvalidRequestError
    if status is not None and status >= 500: return LMServerError
    return LMUnexpectedError if status is None else LMProviderError
```

**The cache key formula** (`dspy/clients/cache.py:104-113`, ran directly):

```python
def cache_key(self, request: dict[str, Any], ignored_args_for_cache_key: list[str] | None = None) -> str:
    ignored_args_for_cache_key = ignored_args_for_cache_key or []
    params = {k: _transform_value(v) for k, v in request.items() if k not in ignored_args_for_cache_key}
    return sha256(orjson.dumps(params, option=orjson.OPT_SORT_KEYS)).hexdigest()
```

**Cache-hit response scrubbing — clears usage, keeps `_hidden_params`/cost** (`dspy/clients/cache.py:149-158`, ran directly, see the two probes above):

```python
def _prepare_cached_response(self, response):
    response = copy.deepcopy(response)
    if hasattr(response, "usage"):
        response.usage = {}
        object.__setattr__(response, "cache_hit", True)
    return response
```

**The restricted unpickler's allowlist** (`dspy/clients/disk_serialization.py:23-54`, ran indirectly via `tests/clients/test_disk_serialization.py:335-408`):

```python
_TRUSTED_MODULE_PREFIXES = ("litellm.types.", "openai.types.")
_NUMPY_ALLOWED: frozenset[tuple[str, str]] = frozenset({
    ("numpy", "dtype"), ("numpy", "ndarray"),
    ("numpy._core.numeric", "_frombuffer"), ("numpy.core.numeric", "_frombuffer"),
    ("numpy.core.multiarray", "_reconstruct"), ("numpy._core.multiarray", "_reconstruct"),
    ("_codecs", "encode"),
})

class _RestrictedUnpickler(pickle.Unpickler):
    _allowed: frozenset[tuple[str, str]] = frozenset()
    def find_class(self, module: str, name: str) -> type:
        if any(module.startswith(p) for p in _TRUSTED_MODULE_PREFIXES):
            return super().find_class(module, name)
        if (module, name) in _NUMPY_ALLOWED or (module, name) in self._allowed:
            return super().find_class(module, name)
        raise DeserializationError(
            f"Type {module}.{name} is not in the safe_types allowlist. "
            f"Register it via dspy.configure_cache(safe_types=[...])."
        )
```

**`Embeddings`'s FAISS build**, showing every non-default-obvious parameter (`dspy/retrievers/embeddings.py:70-91`, read, not independently run — needs `faiss-cpu`):

```python
def _build_faiss(self):
    nbytes = 32
    partitions = int(2 * np.sqrt(len(self.corpus)))
    dim = self.corpus_embeddings.shape[1]
    try:
        import faiss
    except ImportError:
        raise ImportError("Please `pip install faiss-cpu` or increase `brute_force_threshold` to avoid FAISS.")
    quantizer = faiss.IndexFlatL2(dim)
    index = faiss.IndexIVFPQ(quantizer, dim, partitions, nbytes, 8)
    index.train(self.corpus_embeddings)
    index.add(self.corpus_embeddings)
    index.nprobe = min(16, partitions)
    return index
```

## 4. Probes worth adding

All five ran and held on `.venv-dspy/bin/python`, offline (`env -u OPENROUTER_API_KEY -u TYPESAFE_API_KEY -u OPENAI_API_KEY -u ANTHROPIC_API_KEY`), by monkeypatching `litellm.completion` with a local Python function — never a network call — the same technique DSPy's own `tests/clients/test_lm.py` uses. Saved at
`/tmp/claude-0/-home-user-kohaerenzprotokoll/a2e3b1c0-0873-50c6-be3a-bb4d50bd8e11/scratchpad/readers/lm-and-retrieval/probes.py`. Output: `5 of 5 probes hold`.

- id: `cache-hit-keeps-cost` — "A cache hit clears `lm.history[i]['usage']` but not `['cost']`: the cost replays the original call's `_hidden_params['response_cost']`, contradicting `base_lm.py`'s own inline comment."
```python
def p_cache_hit_keeps_cost():
    import litellm, tempfile, dspy
    from litellm.utils import Choices, Message, ModelResponse

    def fake_completion(*, cache, num_retries, retry_strategy, **request):
        resp = ModelResponse(
            choices=[Choices(message=Message(role="assistant", content="Hi!"))],
            usage={"prompt_tokens": 3, "completion_tokens": 1, "total_tokens": 4}, model="dummy")
        resp._hidden_params = {"response_cost": 0.0042}
        return resp

    saved = litellm.completion
    litellm.completion = fake_completion
    try:
        with tempfile.TemporaryDirectory() as tmp:
            dspy.configure_cache(enable_disk_cache=True, enable_memory_cache=True, disk_cache_dir=tmp)
            lm = dspy.LM("openai/probe-model", model_type="chat")  # cache=True default
            lm("hello"); lm("hello")  # second call is a cache hit
            first, second = lm.history[0], lm.history[1]
            if second["usage"] != {}:
                return f"cache hit usage was not cleared: {second['usage']!r}"
            if second["cost"] != first["cost"] or second["cost"] != 0.0042:
                return f"cache hit cost changed or was cleared: first={first['cost']!r} second={second['cost']!r}"
            return None
    finally:
        litellm.completion = saved
        dspy.configure_cache()
```

- id: `rollout-id-busts-cache-at-zero-temperature` — "`rollout_id` changes DSPy's cache key even at `temperature=0` (two real calls for two rollout_ids); the runtime warning's 'no effect' is about the provider's output determinism, not about whether DSPy's own cache is bypassed."
```python
def p_rollout_id_busts_cache_at_zero_temperature():
    import litellm, tempfile, dspy
    from litellm.utils import Choices, Message, ModelResponse
    calls = []
    def fake_completion(*, cache, num_retries, retry_strategy, **request):
        calls.append(1)
        return ModelResponse(choices=[Choices(message=Message(role="assistant", content="Hi!"))],
                              usage={"prompt_tokens": 1, "completion_tokens": 1, "total_tokens": 2}, model="dummy")
    saved = litellm.completion
    litellm.completion = fake_completion
    try:
        with tempfile.TemporaryDirectory() as tmp:
            dspy.configure_cache(enable_disk_cache=True, enable_memory_cache=True, disk_cache_dir=tmp)
            lm = dspy.LM("openai/probe-model", model_type="chat", temperature=0)
            lm("Query", rollout_id=1); lm("Query", rollout_id=2); lm("Query", rollout_id=1)  # 3rd repeats the 1st
            if len(calls) != 2:
                return f"expected 2 real calls (rollout 1, rollout 2), got {len(calls)}"
            return None
    finally:
        litellm.completion = saved
        dspy.configure_cache()
```

- id: `reasoning-model-detectors-disagree` — "`dspy/clients/lm.py` and `dspy/clients/openai_format.py` each define their own `_is_openai_reasoning_model`, and they disagree about `o5` models."
```python
def p_reasoning_model_detectors_disagree():
    from dspy.clients.lm import _is_openai_reasoning_model as legacy_check
    from dspy.clients.openai_format import _is_openai_reasoning_model as typed_check
    legacy, typed = legacy_check("openai/o5"), typed_check("openai/o5")
    if legacy == typed:
        return f"the two checks now agree on o5 ({legacy!r}); the TRAP may be fixed upstream"
    if not (legacy is True and typed is False):
        return f"unexpected values: legacy={legacy!r} typed={typed!r}"
    return None
```

- id: `embeddings-cache-must-be-false` — "`dspy.Embeddings(..., cache=True)` always raises `AssertionError`; the parameter exists only to be asserted `False`."
```python
def p_embeddings_cache_must_be_false():
    from dspy.retrievers.embeddings import Embeddings
    def embedder(texts): return [[0.0] for _ in texts]
    try:
        Embeddings(["a"], embedder, cache=True)
    except AssertionError:
        return None
    return "Embeddings(cache=True) did not raise"
```

- id: `configure-cache-dir-default-frozen-at-import` — "`configure_cache`'s `disk_cache_dir` default is a plain literal baked in when `dspy.clients` was first imported, not re-read from `DSPY_CACHEDIR` at call time."
```python
def p_configure_cache_dir_default_is_frozen_at_import():
    import inspect, dspy, dspy.clients as clients_mod
    default = inspect.signature(dspy.configure_cache).parameters["disk_cache_dir"].default
    if default != clients_mod.DISK_CACHE_DIR:
        return f"default {default!r} does not match module constant {clients_mod.DISK_CACHE_DIR!r}"
    if not isinstance(default, str):
        return f"default is not a plain string, so this claim needs re-checking: {default!r}"
    return None
```

## 5. Surface worth asserting

Every line below is taken from `inspect.signature` against the installed `.venv-dspy` package, run directly:

```surface
dspy.LM(model, model_type="chat", temperature=None, max_tokens=None, cache=True, callbacks=None, num_retries=3, provider=None, finetuning_model=None, launch_kwargs=None, train_kwargs=None, use_developer_role=False, **kwargs)
dspy.BaseLM(model, model_type="chat", temperature=None, max_tokens=None, cache=True, callbacks=None, num_retries=3, **kwargs)
dspy.BaseLM.copy(**kwargs)
dspy.BaseLM.dump_state()
dspy.BaseLM.load_state(state, *, allow_custom_lm_class=False)
dspy.BaseLM.__call__(*items, prompt=None, messages=None, request=None, **kwargs)
dspy.BaseLM.inspect_history(n=1, file=None)
dspy.LM.finetune(train_data, train_data_format, train_kwargs=None)
dspy.LM.reinforce(train_kwargs)
dspy.LM.launch(launch_kwargs=None)
dspy.configure_cache(enable_disk_cache=True, enable_memory_cache=True, disk_cache_dir='<DSPY_CACHEDIR or ~/.dspy_cache, frozen at import>', disk_size_limit_bytes=30000000000, memory_max_entries=1000000, restrict_pickle=False, safe_types=None)
dspy.clients.Cache(enable_disk_cache, enable_memory_cache, disk_cache_dir, disk_size_limit_bytes=10485760, memory_max_entries=1000000, restrict_pickle=False, safe_types=None)
dspy.clients.Cache.cache_key(request, ignored_args_for_cache_key=None)
dspy.clients.Cache.get(request, ignored_args_for_cache_key=None)
dspy.clients.Cache.put(request, value, ignored_args_for_cache_key=None, enable_memory_cache=True)
dspy.clients.Cache.save_memory_cache(filepath)
dspy.clients.Cache.load_memory_cache(filepath, allow_pickle=False)
dspy.clients.cache.request_cache(cache_arg_name=None, ignored_args_for_cache_key=None, enable_memory_cache=True, *, maxsize=None)
dspy.inspect_history(n=1, file=None)
dspy.enable_litellm_logging()
dspy.disable_litellm_logging()
dspy.Embedder(model, batch_size=200, caching=True, **kwargs)
dspy.Embedder.__call__(inputs, batch_size=None, caching=None, **kwargs)
dspy.Embedder.acall(inputs, batch_size=None, caching=None, **kwargs)
dspy.Embeddings(corpus, embedder, k=5, callbacks=None, cache=False, brute_force_threshold=20000, normalize=True)
dspy.Embeddings.save(path)
dspy.Embeddings.load(path, embedder)
dspy.Embeddings.from_saved(path, embedder)          # classmethod, confirmed
dspy.EmbeddingsWithScores.forward(query)
dspy.Retrieve(k=3, callbacks=None)
dspy.ColBERTv2(url='http://0.0.0.0', port=None, post_requests=False)
dspy.ColBERTv2.__call__(query, k=10, simplify=False)
dspy.clients.provider.Provider()                     # no constructor args
dspy.clients.lm_local.LocalProvider.launch(lm, launch_kwargs=None)
dspy.clients.openai.OpenAIProvider.is_provider_model(model)
dspy.utils.usage_tracker.UsageTracker.add_usage(lm, usage_entry)
dspy.utils.usage_tracker.UsageTracker.get_total_tokens()
dspy.track_usage()                                    # -> contextmanager yielding UsageTracker
```

Module-level constants confirmed on the installed package: `dspy.clients.DISK_CACHE_DIR == dspy.utils.caching.DSPY_CACHEDIR == '/root/.dspy_cache'` (this container's `$HOME`); `dspy.clients.DISK_CACHE_LIMIT == 30000000000`; `dspy.__version__ == '3.3.1'`.

Not in the top-level `dspy.*` namespace despite extending `dspy.Retrieve` — needs an explicit submodule import: `dspy.retrievers.databricks_rm.DatabricksRM`, `dspy.retrievers.weaviate_rm.WeaviateRM`.

## 6. Ten things the skill must say

1. **The rollout_id/temperature=0 claim is backwards from what matters.** `rollout_id` always changes DSPy's cache key at any temperature; only the *output* is unaffected at `temperature=0`. Fix `api.md:261-264` and `operations.md:260-264` — both currently read as "rollout_id doesn't bypass the cache unless temperature>0," which the probe `rollout-id-busts-cache-at-zero-temperature` disproves.
2. **A cache hit does not clear cost, only usage.** `lm.history[i]["cost"]` replays the original call's cost on every subsequent cache hit, contradicting DSPy's own source comment (`dspy/clients/base_lm.py:300`). Anything in this repository that sums `cost` across `lm.history` entries (`lmrun.call`'s cost field, per `operations.md`) needs to know a cache hit is not free in the `cost` column the way it is in `usage`.
3. **The litellm-exception → DSPy-exception mapping table** (`dspy/clients/lm.py:726-776`) should be in `api.md` verbatim or as a table — currently only the error *tree* is documented, not which litellm exception class or HTTP status produces which DSPy type.
4. **`num_retries=N` means `N+1` total attempts**, via litellm's own tenacity-based `retry_strategy="exponential_backoff_retry"`, test-proven at exactly 4 attempts for `num_retries=3`. There is no DSPy-level retry loop anywhere in this slice.
5. **Two disagreeing `_is_openai_reasoning_model` implementations ship in 3.3.1** (`lm.py` includes o5 and enforces `max_tokens>=16000`; `openai_format.py` excludes o5 and enforces no token minimum at all on the typed/Responses path). Anything here that might touch `model_type="responses"` with an `o5`-family model should know the guard rails differ.
6. **`import dspy` never imports litellm; it always imports `openai`.** Litellm is lazy (`functools.cache`d, materializes on first real use); `dspy/clients/openai.py` does a bare top-level `import openai`, unconditionally reachable from `import dspy` alone. Relevant to any concern about what's actually installed/reachable in a fresh container.
7. **`dspy.Embedder(callable)` is the fully-local, no-provider embedding path**, already gestured at from a third-party recipe in `retrieval.md`; this read confirms it directly in DSPy's own docstring and doc pages, plus the `pip install dspy[numpy]` requirement, plus that `Embedder`'s own `caching=` kwarg to litellm is always forced `False` regardless of what was asked (the *actual* caching happens one level up, in DSPy's own `request_cache` wrapper).
8. **DSPy ships its own local-inference launcher, `dspy.clients.lm_local.LocalProvider`, separate from "point `dspy.LM` at someone else's local server."** It starts an SGLang subprocess bound to `0.0.0.0` (not `localhost`) and needs `provider=LocalProvider()` passed explicitly — never auto-inferred. Worth a `operations.md`/`retrieval.md` entry distinguishing it from the third-party Claude-CLI local-runtime pattern already documented there.
9. **`.finetune()` on an `openai/`-prefixed model always talks to the real OpenAI API**, via the bare `openai` SDK's own global client — even if the same `dspy.LM` instance's inference calls are redirected to a local server via `api_base`. The one concrete "leaves the machine" trap in this slice.
10. **A restricted-pickle probe or `[checked: …]` mark for `restrict_pickle=True`** is worth adding: the allowlist is real and specific (litellm/openai response types by module prefix, six named numpy reconstruction functions, user `safe_types`), proven here against an actual `numpy.ctypeslib.load_library` pickle-RCE payload, and a rejected/corrupt entry degrades to a cache miss rather than a crash — none of this is in the skill today even though `api.md:500-515` already names the flags.
