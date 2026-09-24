# Running a model call for real

`testing.md` is this file's offline half — fixtures, dry runs, what a test can
get away with. This file starts where a call is trusted enough that its answer
might leave the container: the record it must leave, what it costs, how to
read it back, what happens when it fails, and what nine repositories' worth of
tracing, caching and serving code got wrong while doing the same thing.
`api.md` has the DSPy surface (`dspy.LM`, the error tree, `save`/`load`,
`configure_cache`) — this file does not repeat it, only what this repository
does with it.

## In this repository

### `lmrun.call`'s record, field by field

Every model call `pairs.py` and `graphrag.py` make goes through
`lmrun.call(program, *, step, subject="lm", approval=None, german=(), out_dir=None, **inputs)`,
and each call appends exactly one JSON object to
`Plan/runs/<subject>/lm/<step>.jsonl` (`scripts/lmrun.py`):

| field | where it comes from | why |
|---|---|---|
| `event`, `step`, `subject`, `at` | the call site and the clock | which run this belongs to |
| `model`, `fixture` | `lm.model`, `type(lm).__name__ == "FixtureLM"` | a real answer is never confused with a fixture's |
| `status` | classified below | `answered` / `refused` / `unparsed` / `unreachable` — **never a score** (P15) |
| `error` | `f"{type(exc).__name__}: {exc}"[:500]` | present only when an exception was caught, never invented |
| `inputs`, `outputs` | `str(v)` of what the program was given and returned | frozen at call time, never reconstructed later |
| `raw`, `finish_reason` | `lm.history[before:]`, one entry per choice, read **before** any parsing | a reasoning model that spends its whole budget and returns `content: None, finish_reason: length` is caught here, before the adapter gets a chance to call it anything else (P19) |
| `usage`, `cost` | `dspy.track_usage()`'s `get_total_tokens()`; `sum(e.get("cost") or 0 for e in entries)` | see *Cost and usage* |
| `problems` | empty output fields; a German field scored `wrong` or left `unmeasured` | P19, P23 — a problem is named, never silently absorbed into `answered` |
| `seconds` | `time.time() - started` | |
| `approval` | the caller's own string | which decision let this text leave the container |

### The approval rule

`call()` builds in three refusals no scanned repository enforces on its own
(`scripts/lmrun.py`):

1. **Cache on refuses.** `if getattr(lm, "cache", True): raise RuntimeError(...)` —
   a cached call replays its first completion, and repeats measure nothing
   (P18). `lmrun.make_lm()` is how `pairs.py` and `graphrag.py` build a real
   LM, and it forces `cache=False` explicitly (`kwargs.pop("cache", None)` then
   `dspy.LM(model, cache=False, **kwargs)`).
2. **No `approval=` refuses.** A non-fixture LM with nothing passed to
   `approval=` raises, naming that the author's decision has to be named
   (`NOW.md`). The fixture path (`_is_fixture(lm)`) needs neither check — that
   is what makes `testing.md`'s dry runs free.
3. **A `History`-carrying wrapper around `dspy.RLM` is not offered at all.**
   `dspy-session`'s own `docs/rlm.md` records that wrapper failing on every
   iteration with `"Unsupported value type: History"` on DSPy 3.1.3; re-read
   against 3.3.1 the same wrapper fails immediately instead, with `"Unexpected
   inputs not declared in the signature"` (re-checked 2026-09-24,
   `Plan/concept/dspy-extract_2026-09-24/`). This is not a bug in `lmrun.py` to
   fix; it is a combination this repository does not build.

**`rlm_ingest.py` does not go through `lmrun.call` at all**, and this is a real
architectural fact, not an oversight to describe away (P2). Its `run()`
function builds its own `dspy.LM(model, api_key=api_key(), api_base=BASE,
max_tokens=16000, temperature=0, cache=False)` and calls `dspy.RLM(...)`
directly (`scripts/rlm_ingest.py`). It carries its own, separate
approval gate — a bare `raise SystemExit(...)` when `--approval` is missing,
checked before anything is built (`scripts/rlm_ingest.py`) — and its
own key handling: `api_key()` reads `OPENROUTER_API_KEY` from the environment
first and only falls back to a line in a git-ignored `.env` file if that is
absent, never printing either (`scripts/rlm_ingest.py`). Because the
call bypasses `lmrun.call`, it produces **no** `Plan/runs/<subject>/lm/`
record, no four-way status, no German-language check on its own output — its
own artifact is `03-candidates-rlm.md`, with its own header line recording
`cost`, `approval`, `verified`, `reach` and `forced` in place of `lmrun`'s
JSONL row (`scripts/rlm_ingest.py`). `rlm.md` has what those fields
mean. With `scripts/route.py` — the door for third-party tools and direct
calls under decision 007, which records every call for offline replay — the
rule „no corpus text leaves without the author's decision" has **three**
encodings, with three record formats; which one the others should call is open
(`NOW.md`, *Three encodings of one rule*).

**What `unreachable` covers, since the 2026-09-24 fix.** `_unreachable(error)`
walks the exception's `__cause__`/`__context__` chain and matches it against
two things (`scripts/lmrun.py`): DSPy 3.3's own typed types,
`_NO_ANSWER = tuple(getattr(dspy, n) for n in ("LMProviderError",
"LMTransportError") if hasattr(dspy, n))`, plus a name-set fallback —
`NetworkRefused` (the fixture's own), `APIConnectionError`, `NotFoundError`,
`AuthenticationError`, `RateLimitError`, `ServiceUnavailableError`, `Timeout`,
`ConnectionError`, `PermissionDeniedError`. This is the sentence
`refused-connection-is-transport-error` names: `lmrun.call`'s classifier
folds every `LMProviderError` and `LMTransportError` into `status=
"unreachable"`, and a refused connection — nothing answering the port — is
exactly this shape when nothing came back at all.
[checked: refused-connection-is-transport-error] **Until 2026-09-24 the
`_NO_ANSWER` tuple did not include DSPy's own types**, because the first nine
offline selftest cases only ever raised the fixture's own `NetworkRefused`. A
probe against a closed local port — no model has ever been called here — raised
`dspy.LMTransportError`, and `call()` **re-raised it instead of recording
`unreachable`**. The tenth selftest case,
added the same day, constructs `dspy.LMTransportError` directly and asserts
the classification now holds (`scripts/lmrun.py`). `LMConfigurationError`
and `LMUnsupportedFeatureError` are deliberately **not** in either set — those
are this repository's own mistakes, and `call()` still lets them propagate.

`lmrun.py`'s own selftest is ten offline cases —
`.venv-dspy/bin/python scripts/lmrun.py` prints "`lmrun: 10 of 10 cases hold
(4 statuses, DSPy's own transport error, empty field, English caught, cache
refused, approval refused, short text unmeasured)`"
(`scripts/lmrun.py`). Three real runs are one command away and each
waits on the author's yes for that specific run: `pairs.py run --optimizer
labeled`, `graphrag.py ask "…" --answer`, and `rlm_ingest.py <slug>`. `NOW.md`
names what each would send.

## Cost and usage

**`lmrun.call` wraps each call individually** in its own
`with dspy.track_usage() as usage:` block (`scripts/lmrun.py`), so
`usage.get_total_tokens()` and the summed `cost` from `lm.history[before:]`
belong to exactly the one call the record describes — never to a program, a
session or a thread pool. This scoping is deliberate, and the nine
repositories are most of the reason why: every broader scope they tried
leaked usage somewhere.

**`dspy.track_usage()` drops every worker thread's usage.** `ParallelExecutor`
gives each thread its own `copy.deepcopy` of the tracker and nothing merges
them back — DSPy's own source calls this out ("Usage tracker needs to be
deep copied across threads so that each thread tracks its own usage",
`dspy:utils/parallelizer.py:126-131` in 3.3.1). Measured:
`dspy.Evaluate(num_threads=8)` inside `track_usage()` recorded `{}` for 50
calls; `num_threads=1` and a plain loop both recorded the true `750 = 50 × 15`
(`dspy-agents:dspy_config.py`, `[agents]` item, and its cross-repo
`Plan/concept/dspy-extract_2026-09-24/agents-rag.md` corrected-report note that "Item 9 … praise `dspy.track_usage()`
as directly reusable, miss that it undercounts"). `lmrun.call` never runs
under `num_threads>1` for exactly this reason — one call, one tracker block.

**A usage callback that reads the wrong shape reports zero, without error.**
`dspy-agent-skills`' own production example's `UsageCallback.on_lm_end` reads
`outputs.get("usage")` assuming `outputs` is a dict — but DSPy passes the LM's
list of completion strings there, e.g. `['[[ ## answer ## ]]\n4']`, even
though the hook is type-annotated `dict[str, Any] | None`. Against `DummyLM`
this measured `total_tokens: 0`; the shipped dry run only passes because it
feeds the callback invented `{"usage": {...}}` dicts a real call never
produces (`dspy-agent-skills:skills/dspy-production/SKILL.md:131-143`,
`dspy-agent-skills:skills/dspy-production/example_production.py:66,147-151`;
the annotation is `dspy:utils/callback.py:122`).
**A custom `BaseLM.forward` can double-count in the same way from the other
direction**: `BaseLM._process_lm_response` already calls
`settings.usage_tracker.add_usage(self.model, dict(response.usage))` on any
non-cache-hit response; the local-runtime example's own `forward` calls
`add_usage` again inside itself, and a canned 12-prompt/1-completion-token
response measured back as `{'prompt_tokens': 24, 'completion_tokens': 2,
'total_tokens': 26}` — exactly double
(`dspy-agent-skills:skills/dspy-local-runtime/example_local_runtime.py:113-114`;
`api.md` has `BaseLM`'s own usage-recording rule). `lm_fixture.FixtureLM`
never adds usage itself — its response object carries `usage={"prompt_tokens":
0, ...}` and lets `BaseLM` record that once (`scripts/lm_fixture.py`).

**Two other repositories' usage accounting is disconnected from DSPy
entirely.** `dspydantic`'s `api_calls`/`total_tokens` are `len(lm.history)`
and a sum over its `usage` fields — counted **before** `optimize()` runs and
including cache hits, and it **misses every call made through `lm.copy()`**:
measured, `MIPROv2`'s own `GroundedProposer` calls
`self.prompt_model.copy(rollout_id=...)`, and a real run logged 290 requests
against a reported `api_calls=200`
(`dspydantic:src/dspydantic/optimizer.py:1521-1529,2007-2018`; `dspy:propose/grounded_proposer.py:395`).
`braid-dspy` does not read `lm.history`, DSPy's tracker, or LiteLLM's usage at
all — every phase is priced from a hand-typed `TokenUsage(500, 200)` regardless
of what the call actually used, and a phase such as `"critic"` that the price
table has no bucket for is silently priced at zero
(`braid-dspy:braid/metrics.py:14-25,191-247`).

**Per-agent cost, done once, correctly, and once, incorrectly, in the same
repository.** `dspy-agents` turns `track_usage=True` on globally
(`dspy.configure(lm=…, track_usage=True)`), and a prediction's
`get_lm_usage()` then returns `None` when tracking is off, real per-call usage
when it is on and nothing else is tracking, and `None` again inside an
*enclosing* `with dspy.track_usage():` block, because the outer tracker
receives it instead (`dspy-agents:dspy_config.py:207-208`; `api.md`'s
`track_usage` line). The same repository's Agno-side tool logger reads
`result.metrics`, which a plain string-returning DSPy tool never has, so its
own runtime dashboard shows DSPy token usage as unlogged even with
`track_usage=True` set (`dspy-agents:apps/agentos_api/observability.py:392-401`,
`[agents]` item). This is the shape `lmrun.call`'s per-call scoping avoids by
never nesting: one call, one `with dspy.track_usage()`, one record, and no
outer block for the inner one to feed silently into.

## Inspecting a call

`dspy.inspect_history(n=1, file=None)` and the keys on each `lm.history`
entry — `prompt`, `messages`, `kwargs`, `response`, `outputs`, `usage`,
`cost`, `model`, `model_type`, `response_model`, `timestamp`, `uuid` — are
`api.md`'s to describe; this repository reads the same list `lmrun.call`
already reads: `raw` and `finish_reason` come straight off `entry["response"]`
before any parsing is trusted (`scripts/lmrun.py`). `GLOBAL_HISTORY`
(`from dspy.clients.base_lm import GLOBAL_HISTORY`) caps at 10,000 entries and
drops the oldest first — `dspy-agent-skills`' own production skill calls it
"a debugging window, not an audit log"
(`dspy-agent-skills:skills/dspy-production/reference.md:115-118`), which is
the reason `lmrun.call` writes its own append-only JSONL rather than trusting
DSPy's in-process history to still hold a call by the time anyone looks.

**Export the rendered prompt, adapter first.** `dspy.settings.lm.history[-1]
["messages"]` is what actually left the process — the first thing to read
when a model "ignored an instruction". `dspy-agent-skills`' book-production
chapter adds a trap worth carrying: swapping adapters between optimizing and
exporting renders the same demos in a different format from the one they were
*selected* under, so "if a human will read it, configure a readable adapter
**before** optimizing"
(`dspy-agent-skills:skills/dspy-book-production/SKILL.md:77-84`). Nothing here
switches adapters mid-pipeline; `dspy.settings.adapter` stays `None`
(`ChatAdapter`) end to end.

## Errors and retries

`api.md` has the full `LMError` tree and the two `[checked: …]` marks that
pin its shape (`unparseable-is-adapter-error`, and the fact that a `Literal`
outside its set is an adapter error, not a wrong answer). This file only adds
what changes once the answer is meant to be trusted for real.

**Never a bare `except` around an LM call.** `lmrun.call` classifies every
exception it catches — `_unreachable(exc)` first, then `"Adapter" in
type(exc).__name__ or "parse" in str(exc).lower()` for `unparsed` — and
**re-raises anything that matches neither** rather than folding an unknown
failure into a status (`scripts/lmrun.py`). `dspy-agent-skills`' own
book-production chapter states the same rule in prose — "A bare catch turns
your own bugs into silent fallbacks to a weaker model" — and then breaks it
one function away, wrapping its own handler in `except Exception as exc:
raise HTTPException(500, str(exc))`
(`dspy-agent-skills:skills/dspy-book-production/SKILL.md:66-75`,
`example_serving_checks.py:20-21,42-48`):

```python
# Exceptions a fallback may catch. Anything else is your bug, not the provider's.
FALLBACK_SAFE = {"APIError", "RateLimitError", "ServiceUnavailableError", "Timeout"}

def fallback_is_safe(caught: set[str]) -> tuple[bool, str]:
    if "Exception" in caught or "BaseException" in caught:
        return False, "bare Exception turns your own bugs into a silent downgrade"
    unknown = caught - FALLBACK_SAFE
    if unknown:
        return False, f"{sorted(unknown)} are not provider failures; catch typed errors only"
    return True, "typed provider failures only"
```

`dspy-agent-skills:skills/dspy-book-production/example_serving_checks.py:20-21,42-48`.
The same shape recurs at the other end of the nine repositories in a way that
is actively dangerous rather than merely inconsistent: the RLM-hooks skill's
own `_execute_code` catches **every** `Exception` and turns it into a
recoverable step observation, where DSPy's own sandbox catches only
`(CodeExecutionError, SyntaxError)` — so with hooks enabled a terminal
interpreter failure (Deno dying, a protocol break) looks like ordinary
step output, and the outer loop keeps spending LM calls against a dead
sandbox — verified by the `dspy-agent-skills` reader against the installed
`dspy-rlm-hooks` package itself (its `core/patcher.py:105-115`), documented at
`dspy-agent-skills:skills/dspy-rlm-hooks/reference.md:47-48`
(`dspy:predict/rlm.py:661-664`). Nothing in this repository wraps `dspy-rlm-
hooks` (see *Not taken*).

## Cache

`api.md` has `configure_cache`'s full signature; the two parameters that
matter for a live run are `restrict_pickle` (the disk cache deserialises with
pickle unless this is set) and the fact that the per-LM `cache=` flag, not the
process cache's on/off state, decides whether a given LM consults it.
`rollout_id` bypasses the cache for an otherwise-identical request, but
**only when `temperature > 0`** — at `temperature=0` DSPy itself warns
`"rollout_id has no effect when temperature=0; set temperature>0 to bypass the
cache"` (`dspy:clients/lm.py:98-102,165-170`), and `BestOfN`/`Refine` rely on
exactly this mechanism internally.

**Measure cost at least once with the cache off, because a warm cache does not
only hide cost — it hides correctness.** `braid-dspy`'s generator retries a
bad answer up to three times against the *same* input; with the default
`cache=True` that measured as **one** real completion behind three "attempts"
(`braid-dspy:braid/generator.py:103-108,141-156`). `dspydantic`'s single-pass
optimizer has the sharper version of the same trap: the descriptions it
*returns* come from one program call and the score it *reports* comes from a
different one; with the cache on the two happen to coincide because identical
inputs hit the cache, and with the cache off — this repository's default for
every real LM — they were measured to differ outright, returning one rewrite
while scoring another (`dspydantic:src/dspydantic/optimizer.py:1874-1882,1924-1963`, verified by the
`dspydantic` reader's own offline probe against the installed package).
`dspy-agent-skills`' own words for the general case: "Cached calls report no
new usage — which is why a benchmark run with a warm cache looks free and
tells you nothing about production cost"
(`dspy-agent-skills:skills/dspy-production/SKILL.md:73-75`). **This repository
does not have the choice to forget**: `lmrun.call` refuses an LM whose
`cache` attribute is `True` outright (see *In this repository*, above), so
neither question — is it free, is it the run it claims to be — can arise from
a warm cache here.

**A cache-adjacent trap this repository found in its own model sweep, and a
second one from `braid-dspy`'s sibling repository.** `openrouter/openrouter/
free`, OpenRouter's own Free Models Router, was one candidate in this
repository's own `lm-bench` comparison; it serves a *different underlying
model* on every call, yet "DSPy keys its cache on the prompt, not on the model
that answered, so a cached hit replays whichever model answered first"
(`Plan/quality/lm-bench_2026-09-16.md`) — a model chosen
this way would need the cache off to measure reliability for that reason
specifically, not only for P18's general one; it is not what `rlm_ingest.py`
defaults to (`nvidia/nemotron-3-super-120b-a12b:free`, chosen precisely
because it answers structured-output requests reliably). Separately,
`dspy-advanced-prompting`'s own `.env.example` sets `DSPY_CACHE_DIR=
.dspy_cache`; DSPy 3.3.1 reads `DSPY_CACHEDIR` (default `~/.dspy_cache`) and
`DSPY_CACHE_LIMIT`, so that line, and its `DSPY_LOG_LEVEL` neighbour, are
inert — a config file that looks like it is redirecting the cache and is not
(`dspy-advanced-prompting:.env.example:8-9`; `dspy:clients/__init__.py:15-16,60-61`).

## Saving and loading

`api.md` has the save/load API (state JSON vs. `save_program=True`'s
cloudpickle, `Module.load`'s `allow_pickle`/`allow_unsafe_lm_state` flags).
Two of its `[checked: …]` facts belong here because this file is where they
get used:

**A whole-program save pickles the program, and `dspy.load` refuses to read
it back unless told the source is trusted.** `save(dir, save_program=True)` writes
`program.pkl` with cloudpickle; loading it runs arbitrary code, and `dspy.load`
raises `ValueError` unless `allow_pickle=True` is passed explicitly.
[checked: load-refuses-pickle] Nothing in this repository's own scripts calls
`dspy.load` with `allow_pickle=True` — the only save form used here is the
state-only one, exactly because that form is "the one to keep" (`api.md`).

**The saved LM state never carries the key that would let a leaked file make a
live call.** `program.dump_state()` records the LM's model, cache, retry and
sampling settings, and not its `api_key` — built by setting a real `dspy.LM`'s
`api_key="PROBE-KEY"` and asserting the string is absent from
`repr(program.dump_state())`. [checked: saved-state-has-no-key] On load,
`allow_unsafe_lm_state=False` (the default) additionally drops `api_base`,
`base_url` and `model_list` from the state, so a saved file cannot silently
redirect a reloaded program's calls to a different endpoint (`api.md`).

**`baseline.digest()` hashes the program itself, never a tag someone bumps.**
`digest(*parts) -> hashlib.sha256(json.dumps(parts, sort_keys=True, ...))
[:12]` (`scripts/baseline.py`) is what `baseline.row()` calls on
whatever a candidate's `program`/`trainset` arguments actually are, so
`program_hash` changes exactly when the instructions, demos or rule source
change and not otherwise — ported in spirit, not in code, from `dspy-agents`'
`_program_artifact_signature` (`dspy-agents:dspy_config.py:45-86`;
`scripts/baseline.py`).

**Content-hash invalidation, and one repository's version of it that is not
actually a content hash.** `dspy-agents` keys its artifact directory, offline
docs and Agno toolkit caches by `sha1(rel_path + mtime_ns + size)[:12]` plus a
manual `*_CACHE_TAG`
(`dspy-agents:dspy_config.py:45-86`, `dspy-agents:skills/rag/offline_docs.py:39-82`,
`dspy-agents:apps/agentos_api/app.py:250-272`) —
this is **path-and-metadata** namespacing, not a hash of the artifact's
content, and the `dspy-agents` reader's corrected report
(`Plan/concept/dspy-extract_2026-09-24/agents-rag.md`) calls the distinction out directly: "it is also unnecessary for correctness, because
DSPy's cache key is already the sha256 of the full request." `dspydantic`
shows what happens when a version stamp is trusted instead of a content
check: `version("dspydantic")` falls back to a hardcoded `"0.1.2"` via
`importlib.metadata` when the package is not pip-installed (a source
checkout, for instance), while `__version__` in the code reads `"0.1.6"` —
persisted files silently under-report their own provenance
(`dspydantic:src/dspydantic/prompter.py:18-23`, `dspydantic:src/dspydantic/persistence.py:35-40,128-162`). Worse,
`dspydantic.load()` never compares the saved `model_schema` against the model
class passed in at all, so a field renamed since the file was saved is
ignored rather than flagged (`dspydantic:src/dspydantic/prompter.py:220-221`). **Content-hash
invalidation as its own mechanism is catalogued here, not built**: nothing in
this repository currently invalidates a cached derived artifact by hashing
its content rather than its path; `baseline.digest()` is the nearest instance,
and it hashes the program and trainset it is *given*, not a file on disk
(*Not taken*, below, has the waiting condition).

## Callbacks and tracing

**MLflow appears in four of the nine repositories, and none of the four is
installed here.** Every claim below is the repository's own, not run against
a real MLflow server in this project (`mlflow` is absent from `.venv-dspy`).

| repository | what it logs | what it loses |
|---|---|---|
| `dspy-agent-skills` (`dspy-production` skill) | `mlflow.dspy.autolog(log_traces=True, log_traces_from_compile=True, log_traces_from_eval=True, log_compiles=True, log_evals=True)` — "everything on in development and CI; inference traces only, sampled, in production" | untested here; `dspy-agent-skills:skills/dspy-production/SKILL.md:162-173`, `dspy-agent-skills:skills/dspy-production/reference.md:146-159` |
| `dspy-agent-skills` (`dspy-book-production` skill) | a span tree per call (module → adapter format → raw request/response → adapter parse → output); `compile()` creates one parent run plus a child run per evaluation holding candidate program state, score and traces; an MCP server exposes "26 tools, 11 of them trace tools" for search and for logging **feedback** (a judgment) or an **expectation** (curatable ground truth) | none named, but: "always pass an explicit field list when searching traces … or the default full span tree exhausts the context window after a few results" — the note calls this the single most useful operational detail in the chapter; `dspy-agent-skills:skills/dspy-book-production/SKILL.md:86-109`, `dspy-agent-skills:skills/dspy-book-production/reference.md:62-97` |
| `dspy-session` | `log_session()` logs params (`history_field`, `history_policy`, `max_turns`, a **class name**, never the LM), per-turn `history_length`, and `session_state.json`/`turns.json`/`examples.json` as artifacts | **no tokens and no cost, ever**; `mlflow_turn_logger`'s own `TurnLogger` guards `turn_score` on `turn.score is not None`, which inside `on_turn` is never true, so a score is never logged either — the committed `mlflow.db` in that repository holds only `history_length` and `total_turns` at every step; `dspy-session:dspy_session/integrations/mlflow.py:71-187,238-319` |
| `dspy-optimizer` | `MLflowCallback` logs `is_valid` metrics and the patch op/target/text on a successful merge | it reads keys — `initial_prompt`, `merger_strategy`, `score`, `new_prompt`, `optimizer` — that the real optimize loop **never writes**, so driven by a real run it logs an empty `params` dict and never the prompt text or the model name at all; `dspy-optimizer:dspy_optimizer/callback/mlflow_callback.py:35-125` |

Both `dspy-session` and `dspy-optimizer` also pass MLflow 3's deprecated
`artifact_path=` to `Model.log`/`log_model`, independently
(`dspy-session:dspy_session/integrations/mlflow.py:182-185,340-344`;
`dspy-optimizer:dspy_optimizer/callback/mlflow_callback.py:120-123`).

`api.md` has the full `BaseCallback` hook list
(`on_lm_start`/`on_lm_end`, …). **Callbacks run synchronously inside the call
path** — anything slow in `on_lm_end` is added latency on every request, so
sample at high volume, decide the sample in `on_lm_start` so start and end
stay paired, keep per-`call_id` state and `pop` it on end (a failed call must
not leak the entry), and redact before logging
(`dspy-agent-skills:skills/dspy-production/SKILL.md:128-160`).

**What this repository does instead of tracing.** No MLflow dependency is
installed; `lmrun.call`'s own append-only JSONL row plays the role a trace
would, ported in shape (not in code) from `dspy-optimizer`'s
`HistoryCallback._log_event`, which appends `{"event": …, **state}` per hook
with "zero dependencies"
(`dspy-optimizer:dspy_optimizer/callback/history_callback.py:8-59`). The
tradeoff is explicit: no span tree, no UI, no cross-run query surface — and no
external service, no deprecated kwarg to carry forward, and a file `git diff`
can show.

## Serving

**Load once, fail hard, never serve an uncompiled program silently.**
`dspy-agent-skills`' book-production chapter's own serving pattern: load and
`dspy.asyncify` the program once at process start (a FastAPI `lifespan`),
never per request
(`dspy-agent-skills:skills/dspy-book-production/SKILL.md:23-39`, `dspy-agent-skills:skills/dspy-book-production/reference.md:6-24`).
Its worker-count guidance is Little's law applied to the provider's own rate
limit, not the CPU count — `in_flight ≈ (requests_per_minute / 60) ×
mean_latency_seconds`, so 60 rpm at 2s latency wants about 2 workers, 3000 rpm
at 1.5s wants about 75
(`dspy-agent-skills:skills/dspy-book-production/example_serving_checks.py:34-39`).
Its own stated fix for a missing artifact is the one worth carrying: "a
service silently serving an uncompiled program is worse than one that refuses
to boot"
(`dspy-agent-skills:skills/dspy-book-production/SKILL.md:44-47`, `dspy-agent-skills:skills/dspy-book-production/reference.md:26-28`).

**A different repository's own code is the counter-example, in production.**
`dspy-agents`' `get_rag_program()` wraps `dspy.load(artifacts_path)` in a bare
`except Exception` and falls back to a fresh, uncompiled
`dspy.ChainOfThought("context, question -> answer")` — on 3.3.1 (where
`dspy.load` needs `allow_pickle=True` it is never given) this returns the
zero-shot fallback on **every** call, silently, with nothing logged even at
DEBUG:

```python
def get_rag_program():
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

`dspy-agents:dspy_config.py:213-226`, verified offline against the installed
3.3.1. Its own eval harness makes the same swallow and then prints "No
compiled artifact found" although the artifact exists on disk
(`dspy-agents:eval/harness.py:110-114,152`). **Nothing here serves a program
yet** — there is no equivalent of `get_rag_program()` in this repository — but
the moment one is written, this is the shape to refuse: `dspy.load`'s own
exception is specific (`ValueError` on a missing `allow_pickle=True`, a
version mismatch warning, a genuinely missing path), and a loader should
distinguish them, not catch `Exception` and hand back a program that looks
the same as the real one but answers with none of its optimization.

## Local runtimes

**A `dspy.BaseLM` over the Claude Code CLI**, one process per request:
`claude -p --output-format json --permission-mode plan --no-session-persistence
[--model alias] [--system-prompt …]`. The JSON reply carries `result`, `usage`
(`input_tokens`, `output_tokens`, `cache_read_input_tokens`), `is_error`,
`session_id` and `total_cost_usd`; `parse_result` maps `input_tokens` to
`prompt_tokens` and raises on `is_error`; system messages are joined into
`--system-prompt` and every other turn rendered `role: content`
(`dspy-agent-skills:skills/dspy-local-runtime/SKILL.md:27-57`, `dspy-agent-skills:skills/dspy-local-runtime/reference.md:11-42`).
**Its `copy()` strips what the CLI cannot honour rather than erroring on it**:
`temperature`, `max_tokens` and `rollout_id` are dropped silently in both
`__init__` and `copy()` — "Strip, never error, on `rollout_id` and
`temperature` in `copy()`", because "`BestOfN`, `Refine` and TetraFrame call
`lm.copy(rollout_id=…, temperature=…)` and must not crash"
(`dspy-agent-skills:skills/dspy-local-runtime/SKILL.md:34,106`) — `n>1` raises
`ValueError`, and `cache=True` raises `ValueError("ClaudeLM cannot cache: the
CLI has no deterministic sampling to cache against")`
(`dspy-agent-skills:skills/dspy-local-runtime/reference.md:44-51`):

```python
def copy(self, **kwargs):
    """lm.copy(rollout_id=…, temperature=…) is what BestOfN/Refine call: strip silently."""
    for key in STRIPPED_KWARGS:
        kwargs.pop(key, None)
    new = super().copy(**kwargs)
    new.kwargs = {k: v for k, v in new.kwargs.items() if k not in STRIPPED_KWARGS}
    return new
```

`dspy-agent-skills:skills/dspy-local-runtime/example_local_runtime.py:84-106`
— runs on 3.3.1, but its `forward` must drop the two lines that call
`usage_tracker.add_usage` a second time (see *Cost and usage*, above).
**Backend selection**: `DSPY_LOCAL_BACKEND` is `api`, `claude-cli` or `auto`
(the default); in `auto`, an `ANTHROPIC_API_KEY`/`OPENAI_API_KEY` selects the
API, else `claude` on `PATH` selects the CLI, else the API anyway — "no key,
no CLI → fail loudly at first call" — rather than silently picking neither
(`dspy-agent-skills:skills/dspy-local-runtime/SKILL.md:64-78`). **Budget
guidance, in calls rather than tokens**: one `Predict` costs roughly 5–10s;
`Evaluate` on 20 examples costs 2–4 minutes at `num_threads=1` ("the processes
contend for the same session"); `GEPA(auto="light")` on 20 train / 10 val
costs "a few hundred calls"
(`dspy-agent-skills:skills/dspy-local-runtime/SKILL.md:80-110`).

**This repository built and used the same pattern once, against a real
measurement.** The retired pipeline's own keyless `claude -p` bridge (the
`Hmbown/dspy-local` shape) supplied the outer LM for the one real `dspy.RLM`
run this repository has made against the corpus so far — a `max_iters=4`
census of a document with a known miscount trap — and a single trivial call
through that bridge was measured at **$0.078**, because the bridge re-creates
prompt cache per process
(`Plan/concept/rlm-measured-on-the-trap_2026-09-17.md`). "An RLM
loop is many such calls. Budget before looping" is this repository's own
conclusion from that one number, not a claim carried in from any of the nine.

## Baselines and drift

`scripts/baseline.py` and `Plan/runs/baselines.jsonl` are ported, reshaped,
from `dspy-agents`' `dspy_optimize/baselines/{store,monitor,thresholds}.py`
(`scripts/baseline.py`). A row is append-only:

```
task, candidate, program_hash, trainset_hash, n, scored, correct,
score, vetoed, outcomes {id: 1 | 0 | fraction | null}, cost, at, note
```

**`score` is `correct / scored`, and `scored` is always reported beside `n`.**
An example that could not be scored (unreachable, unparsed) is `null` in
`outcomes`, never `0` and never `1` (P15, P23) — `baseline.row()` builds
`scored = [v for v in outcomes.values() if v is not None]` explicitly, and
`score` is `None` outright when nothing could be scored
(`scripts/baseline.py`). **`vetoed` fails `compare()` whatever the
score**: `dspy.GEPA` optimizes a mean, so a candidate that merges the
`Negentropie`/`Entropie` canary otherwise loses only `1/n` — a veto refuses
the whole candidate instead of docking it a fraction
(`scripts/baseline.py`).

**The floor this repository added.** `dspy-agents`' own monitor compares each
run only with the one immediately before it — so a run logged at `score=0.0,
total_calls=0` becomes a normal new baseline, and a pipeline broken from its
very first row can never alert
(`dspy-agents:dspy_optimize/baselines/monitor.py:20-86`, cited via
`scripts/baseline.py`). `baseline.compare(task, floor=None)` checks
against **the floor**, not only the previous row: the floor defaults to the
task's first recorded row (here, always the deterministic rule) or an
explicitly named `--floor` candidate
(`scripts/baseline.py`). Its rule evaluation order for the drift piece,
ported from the same source: absolute floor first, then a comparison against
the best earlier score within a `TOLERANCE = 0.02` — a `warn`, not silent
passing, if the newest row is below the best row seen so far. The three
verdicts `dspy-agents`' own thresholds evaluator gets wrong, avoided here
directly:

| `dspy-agents`' defect | what it does | `baseline.compare()`'s answer |
|---|---|---|
| `if current_value is None: return None` | an unmeasured metric is skipped and **nothing is reported** (`thresholds.py:186-187`) | `scored < n` is itself a `warn` reason, never silently dropped |
| `severity="fail"` downgraded to `warn` on `max_pct_increase` | a token-increase rule **can never actually fail** (`thresholds.py:211`) | `vetoed` always returns `fail`, at any score |
| no rule at all on `program_score` | a compile scoring `0.0` reports `"ok"` because only `total_tokens` has a rule (`thresholds.py:79-86`) | every row's own `score` is the thing compared against the floor — there is no metric left unrated |

Its exit codes carry the same asymmetry into CI: `2` on `fail`, `1` on `warn`
only with `--treat-warn-as-error`, and an unrecognised status ranks as `warn`
rather than failing outright (`dspy-agents:scripts/baseline_monitor.py:31-33,79-116`).
**And the CI wiring makes the relative check moot on its own terms**: the
JSONL history is committed but the SQLite baseline DB the monitor actually
reads is `.gitignore`d, so every CI run starts from no previous row at all,
and only the absolute floor on `compiled_em_rate` can ever fire
(`dspy-agents:.github/workflows/baseline-monitor.yml:18-44`).

**The ledger in actual use, current rows** (`Plan/runs/baselines.jsonl`):

| task | growth | score |
|---|---|---|
| `one-term-or-two rule:fold` | n=36 → 44 → 49 → 57 | 58.3% → 61.4% → 59.2% → 57.9% |
| `one-term-or-two rule:plural` | n=57 | 71.9% (decision 010) |
| `graphrag-retrieval` seeds | n=9 → 10 → 14 → 17 | 39.5% → 38.4% → 45.3% → 41.9% |
| `graphrag-retrieval` ppr | n=9 → 10 → 14 → 17 | 57.8% → 56.3% → 62.0% → 64.3% |

Every growth step here moved the score, sometimes down — the fold task's
59.2% → 57.9% step is the floor doing exactly its job: a larger, harder set
scored slightly worse and the ledger says so rather than smoothing it (P24,
"done is a measurement, not a flag").

## Not taken

| thing | why not | source |
|---|---|---|
| `MIPROv2`, `BootstrapFewShotWithRandomSearch`, synthetic data generation | want 100+ / 50+ examples; `dspy-agents` itself ran `MIPROv2` on 50 rows while its own README still said "~28 examples" (`dspy-agents:README.md:74`) | `Plan/concept/dspy-toolchain_2026-09-23.md`, *Deliberately not taken* |
| `dspy-rlm-hooks`, wholesale | monkeypatches private DSPy internals and its own security note says to pin the pair; its speculative `llm_query`/`llm_query_batched` calls spend real, paid sub-LM calls **outside** `max_llm_calls` — speculative calls do not consume the logical budget, which counts only model-requested calls — bounded only by a separate `max_dispatches_per_turn=2048` — the exact kind of surprise a cost-control section exists to prevent | `dspy-agent-skills:skills/dspy-rlm-hooks/reference.md:47-48`, verified by that reader against the installed package's own `speculation/integration/registry.py:92-127,146-157` |
| async and streamed calls (`dspy.asyncify`, `dspy.streamify`) | nothing here uses them; `lmrun.call` is synchronous on purpose — one call, one record (`api.md`) | `api.md`, *Asynchronous and streamed calls* |
| wiring any of the four MLflow integrations above | no MLflow dependency is installed; `lmrun.py`'s own JSONL plays that role today (*Callbacks and tracing*, above) | this repository's own state |
| content-hash invalidation as its own mechanism | catalogued, not built; `baseline.digest()` hashes what it is handed, not a file on disk, so it is the nearest instance rather than the thing itself — waits for a second cached derived output that actually needs invalidating | `Plan/concept/dspy-toolchain_2026-09-23.md`, *Layer 3* |
| Jev (TypeSafe) as part of this file's model-calling story | Jev is not DSPy — it answers typed questions, never text — and `.agents/skills/typesafe` is where it is documented; two scripts call it (`bilingual.py`, `jev_entities.py`) and neither routes through `lmrun.py` | `.agents/skills/typesafe/SKILL.md` |

A `log_dir` for `dspy.GEPA` is not a fresh directory by default and this
matters here specifically: "Running GEPA with the same `log_dir` will resume
the run from the last checkpoint" — `dspy-auto-gepa` measured its own
`force=True` flag doing nothing as a result, loading old state and making 4
student calls and 0 reflection calls instead of retraining
(`dspy:teleprompt/gepa/gepa.py:305-307`, `dspy-auto-gepa:src/dspy_auto_gepa/runner.py:325-329`;
`dspy-agent-skills:skills/dspy-gepa-optimizer/SKILL.md`'s own examples give
the same warning independently). `pairs.py`'s `GEPA` rung has not yet run
against a real model; when it does, its `log_dir` has to be fresh per attempt
and recorded in the baseline row, not reused across runs the way `dspy-
auto-gepa`'s `<artifact_dir>/<name>/gepa_logs` is.
