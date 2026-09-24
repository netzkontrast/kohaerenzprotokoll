# Scan: `/home/user/dspy-agents`

## 1. What it is

An MVP combining Agno AgentOS (FastAPI runtime, sessions/memory, MultiMCP tools) with DSPy
(`Signatures` + `ChainOfThought` + `MIPROv2`) for one fixed skill: `context, question -> answer`.
Targets `dspy-ai>=3.0.3,<4.0` (older lineage than the target's pinned 3.3.1; `requirements.txt:2`).
Maturity: real code with CI-shaped tests and a git history of 51 commits organized in
numbered "Phases," but the core optimization result is weak/flat (MIPROv2 best score 0.0 in
one logged run, `dspy_optimize/baselines/compile_metrics.jsonl` last line) and roughly a third
of the test suite cannot even be collected without heavier deps than the repo claims are
optional (verified below). It is a working scaffold, not a validated pipeline — closer to
"toy with production plumbing" than "tested."

## 2. Every good idea

1. **Per-directory `AGENTS.md` convention** — every module directory (`tools/`, `workflows/`,
   `skills/`, `tests/`, `mcp/`, `eval/`, `dspy_optimize/`, `data/docs/`) carries a short
   `AGENTS.md` with a fixed shape: Scope / Overview / Config / Troubleshooting / References,
   and the root `AGENTS.md` is an index into all of them (`AGENTS.md:1-70`). `[adopt]` —
   kohaerenzprotokoll's `scripts/rules/` idea (decompositions library) could borrow this shape
   for documenting each script without inventing a new format.
2. **Root `AGENTS.md` "Quick Reminders" block up top** — the five or six things a session most
   needs (env activation, key env vars, CLI availability) stated before the overview
   (`AGENTS.md:5-13`). `[adopt]` — `NOW.md` could adopt a similar terse checklist at its top.
3. **Phase-based `plan.md` with per-phase Status/Acceptance/Results** — each phase states a
   goal, an acceptance criterion, and is updated in place with a `Results` paragraph once done
   (`plan.md:13-70`). `[catalogue]` — heavier machinery than kohaerenzprotokoll wants (no phases
   there), but the "acceptance criterion stated before doing the work" habit is worth keeping
   as an idea, distinct from the phase framing.
4. **Issue-scoped handoff files (`handoff_issue20.md`)** — a single file per issue: Branch, Work
   Completed, Current Observations, Next Actions, Notes (`handoff_issue20.md:1-24`). `[adopt]`
   — directly comparable to `NOW.md`; the "Current Observations" section (numbers that turned
   out surprising, e.g. "compiled EM matches zero-shot, needs investigation") is a good habit:
   record the anomaly, not just the task list.
5. **`.gitignore`'d compiled artifacts, but committed metric logs** — `dspy_optimize/artifacts/`
   is gitignored while `dspy_optimize/baselines/compile_metrics.jsonl` and `eval_metrics.jsonl`
   are tracked in git (verified: `git ls-files dspy_optimize/baselines/` lists the two `.jsonl`
   files but not `*.db`; `.gitignore` lines "DSPy artifacts / dspy_optimize/artifacts/ /
   dspy_optimize/baselines/*.db"). The binary/large artifact never enters history; the small,
   diffable measurement of what it did, does. `[adopt]` — matches P24 "done is a measurement";
   kohaerenzprotokoll already does something similar with `Plan/runs/`, but the git-vs-ignore
   split by file type (structured record tracked, heavy blob ignored) is a clean pattern to
   name explicitly.
6. **Compile → baseline record → drift check, every run** — `compile_rag.py` and
   `eval/harness.py` both, after producing a result, append a JSONL record (with git commit,
   env cache flags, token usage, duration) and then call `log_compile_record`/`log_eval_record`
   which diffs against the *previous* run for that script and prints `ok`/`warn`/`fail`
   (`dspy_optimize/compile_rag.py:96-138`, `eval/harness.py:154-208`,
   `dspy_optimize/baselines/monitor.py:20-43,59-86`). This is the closest analogue in this repo
   to "fold() = 65% measured before any model": every optimize/eval run is compared to its own
   history, not just eyeballed. `[adopt]` — the *shape* (measure, persist, diff against last,
   print a verdict) is worth taking for the `one-term-or-two` optimizer ladder: log each rung's
   score to a small append-only store and assert it does not regress the rung before it.
7. **Threshold rules as data, not code** — `MetricThreshold` dataclasses (`min/max/max_drop/
   max_pct_drop/max_pct_increase/severity/note`) are either the built-in defaults or loaded from
   a JSON file via `BASELINE_THRESHOLDS_PATH`, and every threshold is overridable by env var
   (`dspy_optimize/baselines/thresholds.py:31-101`). `[adapt]` — good general shape for
   "regression gate" tooling; kohaerenzprotokoll doesn't need Postgres/SQLite for this, but the
   dataclass-of-rules + "evaluate against previous run" function (`evaluate_thresholds`,
   `thresholds.py:150-178`) could be lifted almost as-is into a `scripts/rules/` module for
   watching e.g. `judgements.py`'s agree/DISAGREE rate over time.
8. **SQLite-first, Postgres-optional store behind one URL** — `BaselineStore` parses
   `BASELINE_DB_URL`, defaults to a local SQLite file, and swaps in `psycopg` only if a
   `postgresql://` URL is given and the import succeeds (`dspy_optimize/baselines/store.py:45-98`).
   `[catalogue]` — the target's stdlib-only philosophy (P1, standard-library scripts) would
   reject the Postgres branch, but "SQLite by default, degrade gracefully if a heavier client
   is absent" is a pattern worth keeping in mind if the project ever wants queryable run history
   instead of JSONL.
9. **`BASELINE_DISABLE_CACHE` flag to force fresh token counts** — before a baseline run, disk
   and memory caches are explicitly turned off and the memory cache reset, specifically so the
   logged token usage isn't zero from a cache hit (`compile_rag.py:62-67`, `eval/harness.py:94-99`,
   tested in `tests/test_baseline_cache_toggle.py`). `[adopt]` — directly useful lesson: P18
   ("repeats, cache off") already says this for the target, but the concrete mechanism (assert
   the toggle fires *before* `dspy.configure`, verified with a monkeypatched call-order test) is
   a good regression-test pattern to copy for any future DSPy-model script.
10. **Cache directory keyed by a content hash of the artifact, not a static path** —
    `_program_artifact_signature()` hashes every file's relative path + mtime + size under the
    compiled-program directory and folds that into the disk-cache subdirectory name, so a
    recompiled program automatically gets a fresh cache namespace (`dspy_config.py:45-124`).
    `[adopt]` — nice trick: cache invalidation by content signature rather than by remembering
    to bump a manual tag. Useful anywhere kohaerenzprotokoll caches something keyed to a
    document or a wiki snapshot.
11. **Explicit "reasoning model" detection by model-id prefix, not substring** — `mid.startswith(
    ("gpt-5","o4","o3","o1"))` specifically to avoid a substring false-positive
    (`dspy_config.py:144-146`), with a code comment naming the bug it avoids. `[catalogue]` —
    small idea, but "write down the bug the guard is preventing, right next to the guard" is
    exactly what the target's PRINCIPLES.md evidence-with-rule style already does; consistent
    practice worth reinforcing.
12. **Chat vs Responses API auto-switch with per-mode token/temperature defaults** — one
    function computes `model_type`, `temperature`, `max_tokens`/`max_output_tokens`, and a
    `reasoning.effort` value, all overridable by env, and asserts a floor (`>= 16000` tokens,
    `effort` remapped from `min`→`minimal` etc.) to satisfy DSPy's own validation
    (`dspy_config.py:127-210`). `[skip]` — OpenAI-Responses-specific, not applicable to
    kohaerenzprotokoll's OpenRouter/Jev/DSPy-3.3.1 stack, but the general idea "wrap provider
    quirks in one `configure_once()` and test it with a fake LM" is reusable and is item 13.
13. **`configure_once()` singleton with a fake-LM test double (`RecorderLM`)** — a small class
    that just records constructor kwargs, monkeypatched in for `dspy.LM`/`dspy.configure`, used
    to assert the computed kwargs without ever calling out (`tests/test_dspy_config.py:12-58`).
    `[adopt]` — cleanly reusable pattern for testing any DSPy configuration function without an
    API key; matches P5 ("every workflow ships an offline, no-key fixture").
14. **`conftest.py` stubs heavy deps only if they are absent** — `try: import dspy` / `except:
    stub`, same for `agno.workflow` (`tests/conftest.py:14-107`), so unit tests degrade to a
    minimal fake rather than failing outright when a dependency isn't installed. `[adapt]` —
    good intent, but **the stub coverage is incomplete** (see §4) — copy the intent, not the
    implementation as-is, and make sure every module actually imported by the "fast" test tier
    is stubbed, not just the two most obvious ones.
15. **Marker-gated test tiers (`-m "not integration"` vs `-m integration`)** — `pytest.ini`
    registers `integration`; the offline tier is meant to run without a key, the integration
    tier requires a real `sk-...` key and the real `dspy` package
    (`tests/AGENTS.md:1-32`, `pytest.ini`). `[adopt]` — same idea as the target's "offline,
    no-key fixture" principle, expressed as a pytest marker convention; easy, standard, and
    worth adopting verbatim if kohaerenzprotokoll ever wants pytest instead of `selftest.py`.
16. **`runtime_diag` tool: safe, non-secret introspection endpoint** — a tool that dumps env
    toggles, active LM config, recent memory/session metadata, and the latest baseline drift
    status, explicitly filtered to exclude secrets (`tools/AGENTS.md`, "Tools" section).
    `[catalogue]` — a "what does the system currently believe" tool is a useful category;
    kohaerenzprotokoll's `state.py --get` already covers the numeric half of this need.
17. **LanceDB hybrid retrieval with a manifest + signature guard** — `lancedb_runtime.py`
    validates the LanceDB store's signature against the current offline-docs snapshot before
    trusting it, and falls back to keyword search on any mismatch, missing store, or missing
    optional dependency (`skills/AGENTS.md`, "lancedb_runtime.py" section). `[skip]` — heavy
    dependency, out of scope (the target has no vector DB and P1/P2 argue against building one
    speculatively), but "verify a cached index's signature against the source before trusting
    it" is the same idea as the target's `Wiki/index.json` derivation guard and worth naming as
    a general principle if a search index is ever built here beyond qmd.
18. **Deterministic paragraph-chunking + content hash shared between two pipelines** —
    `skills/rag/chunk_utils.py` is explicitly a shared module so the naive keyword loader and
    the LanceDB ingestion pipeline "align," per its own docstring in `skills/AGENTS.md`.
    `[catalogue]` — matches the target's own "one recursive operation, not N pipelines" framing
    (`account.py`/`subject.py`); reinforces that lesson rather than adding anything new.
19. **Curated, size-budgeted offline docs directory with an explicit "what not to put here"
    list** — `data/docs/AGENTS.md` caps the offline doc cache at "3-10 short pages," "~50-100KB,"
    explicitly bans binaries/PDFs/secrets/scraped dumps, and separates it by provenance into
    `context7/`, `external/`, `internal/` subfolders (`data/docs/AGENTS.md:1-40`, directory
    listing). `[adopt]` — directly answers the brief's "pattern for keeping reference docs for
    agents" question; a small, curated, provenance-tagged reference cache with an explicit size
    budget and a "why not bigger" rationale is a reusable convention for
    `Plan/briefings/` or similar procedural-knowledge files.
20. **Provenance-tagged subfolders for reference docs**: `data/docs/context7/*` (vendor docs
    snapshotted via the Context7 MCP), `data/docs/external/*` (e.g. GitHub REST basics),
    `data/docs/internal/*` (this repo's own design notes), each a separate directory
    (`find data/docs`). `[adopt]` — cheap, clear convention: separate "what a third party says"
    from "what we ourselves decided," which is exactly the distinction
    `Plan/briefings/extract.md`'s procedural-vs-document-knowledge rule is trying to enforce for
    a different artifact type; naming the same split for reference docs is free value.
21. **A design doc per significant subsystem under `docs/designs/`** — e.g.
    `docs/designs/run_logging_tracing.md`, `docs/designs/lancedb_offline_corpus.md`
    (`find docs/designs`). `[catalogue]` — comparable to kohaerenzprotokoll's
    `Plan/concept/*.md` habit; no new idea, but confirms the convention is common practice
    worth keeping.
22. **`scripts/cache_benchmark.py --offline` warm-vs-cold benchmark** — a small script whose job
    is only to report latency/token deltas between a cold and a warm cache run
    (`AGENTS.md`, "Testing" section: "Warm vs cold run benchmark"). `[catalogue]` — a narrow,
    single-purpose measurement script in the spirit of the target's `duplicates.py`/`state.py`;
    no direct reuse (no caching layer to benchmark yet in kohaerenzprotokoll) but a good model
    for "one script, one measurement, one number."
23. **CI workflow gated on secret presence** — `.github/workflows/baseline-monitor.yml` runs the
    baseline monitor "when `OPENAI_API_KEY` is provided as a repository secret"
    (`dspy_optimize/AGENTS.md`, "Baseline Monitoring"). `[catalogue]` — not directly portable
    (no CI mentioned as in scope for kohaerenzprotokoll), but "a workflow silently no-ops rather
    than failing when a required secret is absent" is a reasonable convention if CI is ever
    added around `jev-decide`/`TYPESAFE_API_KEY`.
24. **SQuAD-style EM normalization function, isolated and testable** — `_normalize()` in
    `eval/harness.py:45-68` (lowercase, strip punctuation, remove articles, collapse whitespace)
    is a small pure function with an explicit doc-comment rationale. `[catalogue]` — nothing
    kohaerenzprotokoll doesn't already do better (P26 says "quote, never paraphrase," which is
    stricter than EM-normalizing an answer); mentioned because a scoring-normalization function
    living apart from the loop, independently testable, is worth remembering as a template for
    any future metric here.
25. **`Notes/Next Steps/Troubleshooting` triad in the root README** — the README ends with a
    "Notes / Next Steps" and a "Troubleshooting" section that names concrete failure symptoms
    and fixes (e.g. macOS `clang++`/Xcode license issue) (`README.md`, bottom). `[skip]` —
    content is OS/toolchain-specific and irrelevant here, but the "record the actual error
    message people hit, next to the fix" convention is good practice already present in
    `Plan/learnings/`.

## 3. Directly reusable for the target

- **Job 1 (`one-term-or-two`, optimizer ladder LabeledFewShot → BootstrapFewShot → InferRules →
  SIMBA → GEPA):** the *closest* transferable piece is not any DSPy code here (this repo never
  goes past `MIPROv2` and never builds an optimizer ladder), but the **baseline/drift-monitor
  shape** (`dspy_optimize/baselines/monitor.py` + `thresholds.py`): log each rung's accuracy to
  an append-only store, keyed by "script" (here: rung name), diff against the immediately
  preceding rung, and print `ok`/`warn`/`fail`. Would need: (a) swap SQLite/Postgres for a plain
  JSONL append (the target already has `Plan/runs/judgements.jsonl` in that shape — reuse the
  *rule*, not the code), (b) swap the metric from EM to score against
  `Plan/trainsets/surface-pairs.jsonl`, (c) drop the git/env metadata capture down to just a
  timestamp + code version, since P1/P2 argue against building unused infrastructure.
- **Job 1, test pattern:** `tests/test_dspy_config.py`'s `RecorderLM` fake-LM-double pattern
  (§2 item 13) is directly reusable to test whichever `configure_once()`-equivalent
  kohaerenzprotokoll writes for its DSPy 3.3.1 calls, once it makes any (currently P5's offline
  fixture requirement is unmet because nothing calls a model yet — this is the template for when
  it does).
- **Job 2 (entity lists):** nothing code-level transfers (this repo has no entity-extraction
  code), but `data/docs/AGENTS.md`'s size-budgeted, provenance-tagged reference doc convention
  (§2 items 19-20) is a good template for how `Plan/entities/*.md` reader instructions or
  `.agents/skills/*/SKILL.md` could organize any reference material a Haiku reader needs.
- **Job 3 (`dspy.RLM` census via `scripts/rlm_ingest.py`):** the `_program_artifact_signature()`
  content-hash-for-cache-invalidation trick (§2 item 10, `dspy_config.py:45-86`) is directly
  applicable: if `rlm_ingest.py` ever caches per-document RLM outputs, hash the document's own
  content+mtime rather than trusting a manually bumped tag — this is exactly the shape of bug
  the target's own "search coverage" and "stale reconciliation" open problems are about
  (something changed and nothing noticed).
- **Job 4 (skill-description optimization via GEPA):** the per-directory `AGENTS.md`
  documentation-map convention (§2 items 1-2) is a decent model for how `.agents/skills/*/SKILL.md`
  descriptions could be scaffolded before optimization — nothing to literally copy, but the
  "Scope / Overview / Config / Troubleshooting / References" shape is a good checklist for what
  a `SKILL.md` description needs to cover for a ReAct agent's `<available_skills>` block.
- **Open problem "stale reconciliations after merges":** the LanceDB runtime's
  signature-vs-snapshot mismatch guard (§2 item 17) is the same shape of problem — "a derived
  index silently goes stale relative to its source" — solved the same way the target wants to
  solve it (a task queue): detect the mismatch and refuse/fall back rather than serve stale
  data. No code to copy (no vector index here to steal), but the *pattern name* — "signature
  guard, not manual invalidation" — is worth stating explicitly when designing that task queue.
- **Open problem "cost/trace visibility of LM calls":** `dspy.track_usage()` +
  `usage_tracker.get_total_tokens()` used consistently around every LM call in this repo
  (`compile_rag.py:85-87`, `eval/harness.py:78-84`) is exactly the DSPy 3.x API for what the
  target's open problem is asking for. Directly reusable once any model call exists: wrap it in
  `with dspy.track_usage() as usage_tracker:` and log `usage_tracker.get_total_tokens()`
  alongside the judgement/decision — no new code needed, just the DSPy API call.

## 4. Conflicts with the principles

- **The "offline, no-key fixture" claim does not hold under test** (violates P5). Running
  `pytest -m "not integration"` in a clean throwaway venv (`python3.11`, only `pytest` +
  `python-dotenv` + `pydantic` installed — no `dspy`, `agno`, `lancedb`) produced **4 collection
  errors** (`tests/test_agent_mcp_tools.py`, `test_agent_memory.py`, `test_lancedb_ingest.py`,
  `test_observability.py` — all import real `agno.db`, `agno.memory`, `agno.utils`, or `lancedb`
  submodules the `conftest.py` stub never registers) and, among the tests that *did* collect,
  **10 more failures** because the `dspy` stub in `conftest.py` only provides `configure`, `LM`,
  `ChainOfThought` — not `configure_cache`, `dspy.settings`, `dspy.clients`, etc. — so
  `test_dspy_config.py`, `test_caching.py`, and `test_lancedb_runtime.py` all fail with
  `AttributeError`/`ModuleNotFoundError` even in the "unit" tier. Net: 15/26 collectible tests
  passed offline on the first attempt, 16/26 after adding `pydantic`. **The repo's own docs
  (`tests/AGENTS.md`) assert this tier "runs in minimal environments," which is not true as
  written** — a live instance of exactly the failure mode P23 warns against (a guard/test that
  doesn't say what it can't check, and here doesn't even fail loudly at the right layer — it
  fails at import/collection, which looks like a broken test suite rather than "no stub for
  this"). Name the trap: **a partial stub is worse than no stub**, because it creates
  false confidence that "unit tests pass offline" when a third of the suite never ran.
- **Documentation drift on the dataset size, uncaught.** `dspy_optimize/AGENTS.md` and `eval/
  AGENTS.md` both say "~28 doc-grounded Q/A pairs" / a "29-question set," and the README repeats
  "9/28"; the actual file `dspy_optimize/datasets/qa_agno_dspy.jsonl` has **50 lines** (verified
  with `wc -l`), and the last logged baseline record (`compile_metrics.jsonl`, 2025-09-26) shows
  `"train_examples": 50`. Nothing in this repo re-derives that count from the file the way
  `state.py --prose` does for kohaerenzprotokoll — it is exactly the "N of 409" bug the target's
  own CLAUDE.md describes, happening again in a sibling project, uncaught. This is strong direct
  evidence *for* the target's `state.py --prose` design, not a copyable idea from this repo.
- **The metric can silently report a false "compiled" success without ever calling the model
  meaningfully** — `compile_rag.py` logs `"score": 0.0, "total_calls": 0` as a normal baseline
  record (`compile_metrics.jsonl` tail) and the pipeline still writes an artifact and prints
  "Saved compiled program to ...". Nothing gates on `total_calls == 0`/`score == 0` being a
  suspicious result rather than a normal one — the same shape of bug P27/the target's own
  "coverage() returning 1.0 with nothing passed" story warns about. Name the trap: **a
  drift-monitor that only compares "current vs previous" can validate a broken run forever, if
  the very first run was already broken** — there is no absolute floor check here (only
  relative `max_drop`/`max_pct_drop` thresholds keyed to a *previous* run), so a pipeline that
  starts at 0.0 and stays at 0.0 triggers no alert.
- **No inherent "baseline before any model" discipline for the *dataset itself*.** Unlike the
  target's `fold()` (a deterministic function, scored before any model touches the problem),
  this repo's only "baseline" is `dspy.ChainOfThought` zero-shot vs the MIPROv2-compiled program
  — both are LM calls; there is no non-model baseline in the loop, so the "is the model even
  needed" question P1 asks is never posed here. Worth naming as a trap for whichever job
  kohaerenzprotokoll builds next: always keep a pure-code baseline alongside the model
  comparison, not just zero-shot-vs-optimized.
- **Cache defaults are silently on and could hide the very metric being measured** (mitigated,
  but only via an opt-in flag): `AGNO_CACHE_RESULTS`, `AGNO_CACHE_SESSION`,
  `DSPY_ENABLE_{DISK,MEMORY}_CACHE` all default to enabled (`AGENTS.md`, "Quick Reminders";
  `dspy_config.py:100-101`); the repo does the right thing by disabling them explicitly before a
  baseline run (`BASELINE_DISABLE_CACHE`, item 9 above), but *only* in the two scripts that
  remember to set that flag — any ad hoc script calling `configure_once()` directly gets a
  silently cached LM call by default, which P18 explicitly forbids for repeated measurements.

## 5. Dependencies & cost

- **Python:** 3.10+ per README; the repo itself runs fine at 3.11 (used above).
- **DSPy pin:** `dspy-ai>=3.0.3,<4.0` (`requirements.txt:2`) — an *older*, looser pin than the
  target's exact `3.3.1`. Installing this repo's `requirements.txt` into `.venv-dspy` would risk
  moving the target's pinned version; it should never be installed into that venv. If anything
  here is adapted, it should be copied as source (the monitor/threshold modules are pure
  stdlib + optional `psycopg`), not installed as a package dependency.
- **Heavy/optional deps actually needed to run the *full* test suite:** `agno` (a real package,
  not just its `agno.workflow` submodule — also `agno.db`, `agno.memory`, `agno.utils`),
  `lancedb`, `pydantic`, `python-dotenv`, `fastapi`/`uvicorn`, `mcp`. None of these are installed
  in kohaerenzprotokoll's environment and none are needed for anything reusable identified in
  §3 (all §3 items are patterns/small pure-Python snippets, not the packages themselves).
- **API keys:** `OPENAI_API_KEY` required for any real LM call (`compile_rag.py`, `eval/
  harness.py`, `dspy_config.configure_once()`); none of the reusable ideas in §3 require calling
  it — they were all read as source, not executed live. No API key was used in this scan.
- **What was actually run:** a throwaway venv (`/tmp/venv-scan`, python3.11) with only
  `pytest`, `python-dotenv`, `pydantic` installed (no `dspy`, `agno`, `lancedb`, no API key);
  `pytest -m "not integration"` took well under a minute both times. No `dspy`/`agno` install
  was attempted (would exceed the "cheap" budget and risks resolving a DSPy version other than
  3.3.1 in a shared cache).
- **Cost to adopt the useful pieces:** near zero. Items 5, 6, 7, 9, 10, 13, 19, 20 are all either
  small stdlib functions/classes (`thresholds.py`, `store.py`'s SQLite path, `dspy_config.py`'s
  signature hash, `RecorderLM`) or pure documentation conventions — copyable by hand into
  kohaerenzprotokoll's stdlib scripts without pulling in `agno`, `lancedb`, or a newer DSPy.

## 6. Verdict

The single most valuable thing to take is the **baseline-log-then-diff-against-previous-run
shape** in `dspy_optimize/baselines/{store,monitor,thresholds}.py` (§2 items 6-7): measure,
persist to an append-only store keyed by script/rung name, diff the new number against the
immediately preceding one, and print ok/warn/fail — reusable almost verbatim (minus SQLite) for
scoring the optimizer ladder's rungs against each other and against `fold()`'s 65%. The
per-directory `AGENTS.md` documentation convention (§2 items 1, 19-20) is worth adopting for any
new script family. Leave everything Agno/LanceDB/FastAPI-shaped — it is out of scope and none of
it is exercised correctly here anyway (§4): the offline test suite this repo claims to have does
not actually run offline, and its own dataset-size documentation has already gone stale exactly
the way the target's CLAUDE.md warns against, unnoticed by anything in this repo.

---
Scanned read-only; nothing in `/home/user/dspy-agents` was modified. Pytest was run in a
separate throwaway venv (`/tmp/venv-scan`), not inside the scanned repo.
