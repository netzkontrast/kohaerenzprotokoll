# Scan: dspy-auto-gepa

Repo: `/home/user/dspy-auto-gepa` (read-only scan; not modified). 157 commits, MIT,
`thememium/dspy-auto-gepa`, pyproject version `0.1.9`.

## 1. What it is

A thin wrapper (`src/dspy_auto_gepa/`, ~2900 lines across `runner.py`, `data.py`,
`metric_builder.py`, `quality.py`, `generator.py`, `config.py`, `artifacts.py`)
that turns `rows + dspy.Module` into `dspy.Example`s, drafts a metric `.py` file
with an LLM (`dspy.RLM` by default), splits train/val/test, runs `dspy.GEPA`, and
saves/loads the optimized program by name. A second, larger half (`generator.py`,
1686 lines) is `AutoData`, a synthetic-row generator unrelated to GEPA itself.
Targets DSPy `>=3.2.1` (`pyproject.toml:18`), requires **Python >=3.12**
(`pyproject.toml:6`, `.python-version:1`). 35 unit tests in `tests/test_auto_gepa.py`
mostly pass offline with mocks, but **one test makes a real, unmocked LLM call**
(see §4) — I ran it once with `OPENROUTER_API_KEY` present in this environment and
it hit OpenRouter for real; I stopped further test runs after discovering this.
Maturity: real usage examples, a CHANGELOG with an actual GEPA benchmarking history
(AutoData iteration), but the GEPA orchestration itself (`runner.py`) is thin and has
almost no GEPA-specific tuning — budget/threading/caching are pass-throughs to
`dspy.GEPA`'s own defaults.

## 2. Every good idea

1. **`run(force=False)` load-or-train cache-by-path** — checks
   `.auto_gepa/<name>/optimized_<name>.json` before training and `module.load()`s it
   if present (`runner.py:380-386`). Cheap idempotency for repeat invocations.
   `[adapt]` — kohaerenzprotokoll has no optimizer runs yet; the pattern (name → fixed
   artifact path → skip if exists unless `--force`) is worth copying verbatim for a
   `scripts/*_optimize.py` wrapper, keyed off dataset+prompt hash rather than just name.
2. **Field inference from `dspy.Signature`, not from the caller** — `infer_fields_from_module`
   (`data.py:218-274`) reads `module.signature.fields` (with a fallback that walks
   `named_predictors()` for wrapped modules like `ChainOfThought`) so callers don't
   restate input/output field names. `[skip]` — the target's `score_one` is a plain
   Python function taking `(gold, predicted)`, not a `dspy.Signature`-carrying module;
   there is nothing here to infer fields from for job 1.
3. **Explicit, helpful mismatch error** — when row columns don't match the signature,
   the error names exactly what's missing/extra (`data.py:290-304`), rather than a bare
   `KeyError`. `[catalogue]` — a generically good error-message pattern (P23: "a guard
   reports what it could NOT check") worth imitating in any future field-mapping code.
4. **List *or* dict field mapping, one code path** — `resolve_fields` accepts
   `list[str]` (assert-exact) or `dict[str,str]` (rename), with a single fallthrough to
   inference (`data.py:277-327`). `[catalogue]` — a reusable idiom, not project-specific.
5. **File-format auto-detection by extension** (`.jsonl/.json/.csv/.parquet`) for both
   loading rows and writing generated data (`data.py:143-160`, `generator.py:117-233`).
   `[skip]` — kohaerenzprotokoll's data is already JSONL by convention; extra format
   support is unneeded surface.
6. **`build_metric()` as a separate, inspectable step before spending on GEPA** —
   `docs/medium.md:45-96` and `examples/basic.py:67-87` explicitly pause for a human to
   read/edit the generated metric file before any optimization run. `[adopt]` — this is
   exactly P3/P4's "by hand first" discipline, applied to metrics instead of pages: a
   metric is materialized as a reviewable file, never silently embedded. Directly
   compatible with the target's existing `metric=Path` override in job 1's `train()`
   step, and worth adopting as ceremony even where the metric (`score_one`) is already
   hand-written and never LLM-drafted.
7. **`metric=Path|str` bypasses LLM metric generation entirely** — `runner.py:220-227`,
   `runner.py:262-264`; `load_metric()` (`artifacts.py:8-19`) just `exec`s the file and
   grabs a top-level `metric` function. `[adopt]` — this is the load-bearing integration
   point for job 1: point it at a file that defines `metric = score_one` (renamed/adapted,
   see §3) and the whole "draft a metric with an LLM" path is skipped, satisfying
   P12/P26 (no model ever writes the scoring rule).
8. **AST-level validation of a generated metric before it is trusted**
   (`metric_builder.py:245-272`): parses the source, rejects `return {...}` (a dict —
   because `dspy.Evaluate`'s aggregator needs `__float__`/`__add__`, which `dspy.Prediction`
   supports and dict does not), and requires the string `dspy.Prediction` or `Prediction(`
   to appear. `[catalogue]` — a genuinely good "guard reports what it could not check"
   idea (belongs with P23), even though the target will never run the LLM-metric path:
   the *technique* (parse the AST, check for a banned return shape, not just "does it
   run") is reusable anywhere a script writes code that another script will `exec`.
9. **Explicit multi-axis scoring rules baked into the metric-writing prompt**
   (`metric_builder.py:9-227`, the `MetricSpecGenerator` docstring): weighted sub-scores
   as module-level constants, feedback that must "teach the optimizer... 2-5 lines,"
   per-predictor attribution via `pred_name`, exact-match only for enums, LLM-judge only
   as a last resort with a fallback on judge failure. `[catalogue]` — none of this fires
   for job 1 (metric is hand-written), but the *prose rules themselves* are a decent
   checklist for anyone hand-writing a GEPA metric here later, e.g. for job 3 (RLM
   census extraction) where a metric will eventually be needed.
10. **GEPA metric signature convention**: `metric(example, pred, trace=None,
    pred_name=None, pred_trace=None) -> dspy.Prediction(score, feedback)`
    (`metric_builder.py:61`, `docs/medium.md:75`). `[adopt]` — this is the exact shape
    `score_one` must be adapted to (see §3); the trace/pred_name/pred_trace kwargs let
    GEPA attribute feedback to a specific sub-predictor in a multi-module pipeline,
    which the target's single-decision task does not need but should accept and ignore.
11. **`gepa_auto: Literal["light","medium","heavy"]`, default `"light"`**
    (`config.py:21`, `runner.py:330-337`) — this *is* the entirety of "budget selection"
    in this package; it is a bare pass-through to `dspy.GEPA(auto=...)`. `[adapt]` — worth
    taking as the entry point, but there is no independent budget logic to learn from:
    GEPA's own `auto` parameter (not this repo) decides the actual rollout/reflection
    budget from `len(trainset)`. Given n=26 (train~18), "light" is almost certainly the
    only sane setting; "medium"/"heavy" would spend far more than the data supports.
12. **`train()` always passes `track_stats=True` and a `log_dir`**
    (`runner.py:325-337`) so GEPA's own trajectory/candidate logs land under
    `.auto_gepa/<name>/gepa_logs/`. `[adopt]` — cheap, and satisfies "every step keeps
    its artifact" (kohaerenzprotokoll's own `Plan/runs/<slug>/` convention) almost for
    free; just needs the `log_dir` redirected into `Plan/runs/<task>/gepa_logs/`.
13. **No Pareto frontier export or candidate-list artifact of its own** — confirmed by
    grep (`grep -rn "pareto\|candidate" src/` — nothing besides unrelated string-parsing
    variables named `candidate`). Whatever Pareto/candidate data exists is only what
    `dspy.GEPA(track_stats=True, log_dir=...)` itself writes; `dspy_auto_gepa` adds no
    parsing, summarization, or export of it. `[catalogue]` — worth knowing so nobody
    assumes this package gives Pareto-frontier tooling "for free"; the raw dspy.GEPA log
    files would need their own parser if the target wants a `Plan/runs/.../pareto.json`.
14. **`compare()` runs baseline and optimized through the *same* `run_baseline()`/
    `dspy.Evaluate` call** (`runner.py:347-366`), guaranteeing baseline and optimized are
    scored on the identical `datasets.test` split with the identical metric function.
    `[adopt]` — small but load-bearing correctness property (same split, same metric,
    same threading) that's easy to get subtly wrong by hand; the target's own baseline
    number (`fold()` = 14/17 = 82%, `scripts/trainset.py:82-95`) should be reproduced
    through the identical eval path GEPA training used, not recomputed separately.
15. **`num_threads` for both `dspy.Evaluate` and `dspy.GEPA`, default 16**
    (`config.py:22`, `runner.py:303-337`). `[adapt]` — 16 parallel threads against n≈18
    train examples means the whole trainset fires in one round; fine for a tiny n like
    26, but should be turned down for OpenRouter rate limits and is unrelated to the
    canary-safety question (parallelism doesn't affect correctness here).
16. **Split defaults to `(0.7, 0.2, 0.1)` train/val/test, seeded shuffle**
    (`config.py:16`/`17`, `data.py:357-378`) via `random.Random(seed).shuffle`.
    `[adapt]` — deterministic given a fixed seed (good for P24 "done is a
    measurement" / reproducibility), but **not stratified by label** and **not
    canary-aware**: nothing guarantees the Negentropie/Entropie pair (or any other
    single high-signal negative) lands in train vs. val vs. test. On n=26 with a 0.7
    split, `val` gets ~5 examples and `test` ~2-3 — small enough that an unlucky shuffle
    could put the one canary example anywhere, including entirely out of both eval
    splits. This needs manual override for the target (see §4).
17. **Empty-val fallback**: `Datasets.val=val or test` in `datasets()`
    (`runner.py:244`) — if the val split rounds to zero rows, it silently reuses `test`
    as val. `[skip → but note]` — silently swapping data on empty-split is exactly the
    kind of "a metric that cannot fail silently" trap P18/P24 warn about; for n=26 use
    train/val/test proportions that keep every split ≥1, or split 2-way and drop the
    third, deliberately and visibly, not via this fallback.
18. **`promote()` is a one-line file write** (`runner.py:415-424`,
    `optimized_module.save(str(dest))`) — no comparison-before-promote gate built in;
    `run()` always calls `promote()` on whatever `train()` returned, regardless of
    whether `compare()` showed an improvement (`runner.py:396-406`). `[adopt-with-fix]`
    — the pattern (save to a name-derived path) is fine; the **missing gate** ("only
    promote if optimized beats baseline, and never if it breaks the canary") is exactly
    what the target must add on top — see §4.
19. **Loud, explicit synthetic-data path fully separated from the optimization path**
    (`AutoData`/`AutoDataConfig`, `generator.py`, `config.py:42-94`) — includes an
    LLM-judge quality gate (`quality.py:171-293`), deterministic validators
    (`non_empty_validator`, `enum_validator`, `no_emoji_validator`,
    `quality.py:88-128`), an n-gram Jaccard diversity checker
    (`quality.py:328-384`), balanced-output subsampling, and crash-safe streaming
    writes with `fsync` (`generator.py:152-159`). `[skip]` — the brief is explicit:
    "Small data: n=26. Anything needing 100+ examples is currently irrelevant." AutoData
    exists precisely to manufacture 100+ examples and is the wrong tool for a
    hand-labelled 26-row judgement ledger whose whole value is that a person wrote the
    `rule` field. Using it to pad the trainset would violate P13 (never merge two
    sources into one) in spirit — synthetic pairs would dilute a corpus of real,
    attributed human judgements.
20. **`enum_validator`/`non_empty_validator` as tiny composable `(row) -> (bool, str)`
    functions chained by `Validator`** (`quality.py:88-128`, `301-320`). `[catalogue]`
    — a clean, dependency-free pattern for deterministic gates, reusable outside
    AutoData if the target ever wants a similarly composable validator chain for, say,
    `quotes.py`-style checks (though those already exist and are more specific).
21. **Emoji/whitespace sanitization as a pure function, tested against no-context
    input** (`sanitize_string`, `quality.py:66-78`) — normalizes to NFC, strips a wide
    emoji ranges regex, collapses exotic whitespace. `[skip]` — a German corpus of
    scholarly/hard-SF prose has essentially no emoji risk; not a problem this project has.
22. **`StreamingDatasetWriter` writes each row immediately with `fsync`**
    (`generator.py:117-233`) so a crashed generation run doesn't lose already-produced
    rows. `[catalogue]` — generic crash-safety idea worth remembering for any future
    long-running script here that appends JSONL (e.g. `Sources` landing or a census run),
    even though it's presently attached to AutoData, which the target shouldn't use.
23. **`_extract_json` tries five strategies to recover JSON from LLM text**
    (`generator.py:33-78`: raw parse → fenced-code-block strip → bracket-scanning →
    `ast.literal_eval` fallback). `[catalogue]` — a solid defensive-parsing recipe for
    "a model produced JSON-ish text," useful anywhere an LM output must be parsed
    (e.g. if the target ever lets a model propose candidate terms as structured output).
24. **`--run-e2e` pytest flag reserved in `pyproject.toml`** (`poe.tasks.test-e2e`,
    line 71) suggesting live-API tests are meant to be opt-in — but **the actual test
    file does not gate `test_partial_explicit_fields_infer_rest` behind any such flag**
    (see §4). `[catalogue]` — the *intent* (separate fast/offline tests from live/e2e
    tests via an explicit flag) is exactly right and matches P5; the target should copy
    the intent, not the (broken) implementation.
25. **`RunResult`/`Datasets`/`GenerationResult` as small `pydantic.BaseModel`/plain
    classes with a custom `__repr__` for readable one-line printing**
    (`runner.py:13-62`). `[catalogue]` — minor ergonomic pattern, not project-specific.
26. **CHANGELOG entries are literally optimization run diffs** (e.g. "Split mode
    rock-solid at 2.2s, signature mode 5-11s (API variance)," `CHANGELOG.md`) —
    the commit history *is* a lab notebook of iterative speed/accuracy tuning runs.
    `[catalogue]` — mirrors kohaerenzprotokoll's own "every revision names its source
    document" commit discipline (CLAUDE.md, "Committing a wiki page"): a commit message
    that names a measurement rather than "misc fixes" is the same virtue applied to a
    different repo. Worth citing as independent confirmation of that convention, not
    worth importing code for.
27. **Constructor-vs-method argument override pattern**: every pipeline method
    (`datasets`, `build_metric`, `train`, `run_baseline`, `compare`) accepts the same
    named args as the constructor and falls back to constructor state via
    `_resolve_task`/`_resolve_and_prepare` (`runner.py:131-186`). `[skip]` — convenient
    API ergonomics for a general-purpose package with many call sites; the target has
    exactly one task (job 1) and a bespoke script would just hardcode the values.

## 3. Directly reusable for the target

**Job 1 (`one-term-or-two`, `Plan/trainsets/surface-pairs.jsonl`, `scripts/trainset.py`):**

- The task does **not** fit `AutoGEPA`'s row/module/signature model as-is. `score_one`
  (`trainset.py:79-87`) is a free function `(gold: dict, predicted: str) -> dict`, not a
  metric over `(example, pred, ...)`; `surface_pairs()` rows have `first`/`second`/
  `document`/`decision`/`rule`, not clean input/output field names a `dspy.Signature`
  could infer. Concretely, to use `dspy_auto_gepa.AutoGEPA`:
  1. Write a `dspy.Signature` with inputs `first: str, second: str` (maybe `document: str`
     for context) and output `decision: Literal["one-term","two-terms"]`, and a
     `dspy.Predict`/`dspy.ChainOfThought` module over it — this is new code the target
     does not have yet (currently `fold()` is deterministic, no LM program exists).
  2. Convert `surface_pairs()` rows to that shape (rename `decision` as the gold output
     field DSPy expects, consistent with `to_examples`, `data.py:345-354`).
  3. Write an adapter metric file (satisfying `artifacts.load_metric`'s requirement of a
     top-level `metric` function, `artifacts.py:16-17`) that wraps `score_one`:
     `def metric(example, pred, trace=None, pred_name=None, pred_trace=None):`
     `    r = score_one({"first": example.first, ..., "decision": example.decision, ...}, pred.decision)`
     `    return dspy.Prediction(score=r["score"], feedback=r["feedback"])`
     This satisfies rule 7/10 above and keeps `score_one`'s human-written `rule` text as
     the feedback verbatim — no paraphrase, matching P12/P26.
  4. Pass this file via `metric=Path(...)` to `AutoGEPA(...)` to **skip LLM metric
     generation entirely** (`runner.py:220-227`) — critical, since an LLM-drafted metric
     for this task would be exactly the kind of ungrounded scoring the project forbids.
  5. Use `split=(0.7, 0.15, 0.15)` or similar only after manually checking the canary
     example (`J5`, `Negentropie`/`Entropie`) lands in a split that is actually
     evaluated — the built-in `split_examples` (`data.py:357-378`) has no way to pin a
     specific example to a split; the target would need to pre-partition and call
     `to_examples`/pass explicit lists rather than rely on `AutoGEPA.datasets()`'s
     shuffle-then-slice, or wrap it with a stratified/pinned splitter.
  6. `gepa_auto="light"` (`config.py:21`) is the only sane budget for n≈18 train rows;
     do not use "medium"/"heavy".
  7. **No part of this package enforces the canary as a hard constraint.** `dspy.GEPA`
     (via this wrapper) optimizes the mean of `score_one` over the trainset; a candidate
     program that merges Negentropie/Entropie only loses 1/N of its score, it is not
     disqualified. The target must add its own gate after `train()`/`compare()`
     (`runner.py:347-366`) — e.g. re-run the optimized program specifically on the J5
     example, and refuse `promote()` (`runner.py:415-424`) if it fails, regardless of
     the aggregate score. This is new code; nothing here provides it (see §4).
- **Ladder mismatch**: the target's stated ladder is `LabeledFewShot → BootstrapFewShot →
  InferRules → SIMBA → GEPA`. `dspy_auto_gepa` only wraps `dspy.GEPA` — it has no
  code path for the earlier, cheaper rungs. Those would be plain DSPy calls outside
  this package; `AutoGEPA` only becomes relevant at the last rung, and only for its
  save/load/compare bookkeeping (rules 1, 12, 14, 18), not for the optimizer choice itself.

**Job 4 (skill `description` optimization):** `AutoGEPA` has **no `optimize_anything`-style
path**. Every entry point (`datasets`, `train`, `run`) requires a `dspy.Module` with an
inferable `dspy.Signature` (`data.py:218-274`) — it optimizes DSPy program instructions
(the module's prompt), never an arbitrary text artifact like a `SKILL.md` `description`
field directly. To use `dspy.GEPA` for that job, the target needs a program whose single
"instruction" field *is* the description text (a trivial one-field `dspy.Signature`/
`dspy.Predict` used only as a text container) — nothing in `dspy_auto_gepa` builds or
suggests that shape; the target's own plan already correctly points at
`dspy-book-coding-agents`'s `optimize_anything` for this (per
`Plan/concept/continuous-improvement_2026-09-17.md`), not at `dspy-auto-gepa`. **Verdict:
not directly reusable for job 4.**

**Job 2/3 (entity lists, RLM census extraction):** No direct reuse identified. `AutoData`
(rule 19) is superficially relevant to "generate more labelled data" but is explicitly
out of scope per the brief's n=26 rule, and entity/census extraction needs verified line
citations (P12/P26), which `AutoData`/`quality.py` never produces (it validates
enum/non-empty/diversity, never a line reference into a source document).

## 4. Conflicts with the principles

- **A test suite makes a live, unmocked LLM call when an API key happens to be present.**
  `tests/test_auto_gepa.py::test_partial_explicit_fields_infer_rest` (`tests/test_auto_gepa.py:538-559`)
  calls `auto.datasets()` with no `metric=` override and without mocking
  `generate_metric_file`, so it falls through to `AutoGEPAConfig`'s default
  `metric_lm = dspy.LM("openrouter/openai/gpt-oss-120b")` and `dspy.RLM(MetricSpecGenerator)`
  (`config.py:32-39`, `metric_builder.py:286-301`) — a real network call to OpenRouter.
  **I ran `pytest tests/test_auto_gepa.py` once in this session** (with
  `OPENROUTER_API_KEY` present from this container's environment settings) and confirmed
  it: the run printed a real generated metric body and an `RLM reached max iterations`
  warning from an actual model response, taking 15s wall time versus ~1s for every other
  (mocked) test. I stopped running `test_generator.py`/`test_quality.py` after this to
  avoid further live calls. This is a direct violation of the brief's own rule ("never
  with an API key") and of P5 ("every workflow ships an offline, no-key fixture") — this
  package's test suite does not: it is not key-gated, not `--dry-run`-able, and the
  `--run-e2e` flag defined in `pyproject.toml` (idea 24) does not actually gate this test.
  Name the trap: **a "unit" test that silently degrades into a live API call is worse
  than an explicit e2e test**, because nobody reviewing `pytest -q` output would notice.
- **Metric-writing is delegated to a model by default.** The whole `metric_builder.py`
  path (idea 6-9) has an LLM draft the scoring function from a `module_repr` and five
  sample rows. This is directly the shape P12/P26 forbid for the target's canonical
  record — a scoring rule *is* a judgement, and "conflict detection is never mechanised"
  (CLAUDE.md) generalizes to "scoring is never invented by a model when a human already
  wrote the rule," which is exactly `score_one`'s situation. The target avoids this only
  by using the `metric=Path` bypass (idea 7); the *default* behavior of this package is
  the trap.
- **`promote()` has no correctness gate.** `run()` always saves whatever `train()`
  produced (`runner.py:396-406`, idea 18) even if `compare()` shows a regression, and
  there is no mechanism at all for a hard constraint like "never merge Negentropie/
  Entropie regardless of aggregate score" (P13-adjacent: this is a correctness floor, not
  a soft objective). Any use of this package for job 1 needs a bespoke post-training gate
  bolted on top, defeating the "thin orchestration" convenience it advertises.
- **`Datasets.val = val or test` silently substitutes test data as validation data on a
  small split** (`runner.py:244`, idea 17) — a silent behavior change based on split size
  rather than a stated failure, in the spirit of what P23 asks every guard to avoid.
- **No caching control anywhere in the library.** `cache=False` appears only in
  `examples/*.py` (`examples/basic.py:10,13`; `examples/auto_combined.py:17,21`), never
  enforced or even mentioned by `AutoGEPAConfig`/`AutoGEPA`. The target's own principle
  P18 ("repeats, cache off") is not supported by this package — the target would need to
  remember to instantiate every `dspy.LM` with `cache=False` itself; `dspy_auto_gepa`
  does nothing to help or warn about it.
- **No seed passed to `dspy.GEPA` itself** — `config.seed` (`config.py:17`, default 42)
  is only used for the row shuffle in `split_examples` (`data.py:363`); GEPA's own
  mutation/reflection sampling is not seeded through this wrapper at all, so two runs
  with identical `seed=42` can still diverge inside GEPA's search. Determinism claims
  should stop at "the split is reproducible," not "the optimization is reproducible."

## 5. Dependencies & cost

- **Runtime deps** (`pyproject.toml:17-23`): `dspy>=3.2.1`, `pandas>=3.0.3`,
  `pyarrow>=24.0.0`, `pydantic>=2.13.4`, `tqdm>=4.67.3`. The DSPy floor (`>=3.2.1`) does
  **not** pin above 3.3.1 — it can coexist with the target's DSPy 3.3.1 pin without
  moving it (confirmed: the shipped `uv.lock` resolved `dspy==3.2.1`, but re-resolving
  with `dspy==3.3.1` present would satisfy `>=3.2.1` fine).
- **Python version is the real obstacle, not DSPy.** `requires-python = ">=3.12"`
  (`pyproject.toml:6`) and `.python-version` pins `3.12`. kohaerenzprotokoll's
  `.venv-dspy` is **Python 3.11** (CLAUDE.md's venv table). This package cannot be
  installed into `.venv-dspy` as-is; it would need its own `.venv-autogepa` (3.12) or a
  vendored subset of the ideas (§2) reimplemented directly, since the target's other
  DSPy-adjacent venv (`.venv-dspytools`) is 3.12 but is for a different package
  (`dspytools`) and pinning `dspy-auto-gepa` there would mix concerns.
- **API keys**: no keys are needed to import/construct/unit-test the non-LLM parts
  (field inference, splitting, save/load), but the *default* metric-generation path and
  the *default* `metric_lm`/`reflection_lm` (`config.py:32-35`, both `openrouter/...`
  models) require `OPENROUTER_API_KEY` the moment `datasets()`/`train()` actually run
  without an explicit `metric=` override — this is what caused the live call in §4.
  Kohaerenzprotokoll already has `OPENROUTER_API_KEY` set at the environment level per
  its own CLAUDE.md, so this would fire silently rather than erroring, unless the
  `metric=` bypass is always used.
- **Extra deps not in kohaerenzprotokoll's stack**: `pandas`, `pyarrow` (for CSV/Parquet
  I/O the target does not need — everything here is JSONL) — dead weight for job 1.
- **Test run cost incurred by this scan**: one real OpenRouter call (see §4), small
  (single gpt-oss-120b generation via `dspy.RLM`), not repeated.

## 6. Verdict

The single most valuable thing to take is not code but the **contract**: a GEPA metric
must be `def metric(example, pred, trace=None, pred_name=None, pred_trace=None) ->
dspy.Prediction(score, feedback)`, and a hand-written metric can be dropped in via a
`metric=Path` bypass to skip LLM-drafted scoring entirely (`runner.py:220-227`,
`artifacts.py:8-19`) — that shape is exactly what wrapping `score_one` needs, and the
save/load-by-name pattern (`run(force=False)`, idea 1) is worth copying for any future
optimizer runs here. Leave the whole `AutoData` half (idea 19), the LLM metric-generation
default path (ideas 6-9, the actual trap in §4), and the package itself as a dependency —
its `>=3.12` requirement, unmocked live-API test, and missing canary/promotion gate mean
it's cheaper to hand-roll ~40 lines around `dspy.GEPA` directly than to install and then
defeat most of what this package automates.
