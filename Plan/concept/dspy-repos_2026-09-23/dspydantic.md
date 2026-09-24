# Scan: `/home/user/dspydantic`

## 1. What it is

A standalone library (`dspydantic`, PyPI-style package, Alpha) that optimizes Pydantic
`Field(description=...)` strings and optional system/instruction prompts for structured
extraction, using DSPy teleprompters as the optimization engine and a Pydantic model's
JSON schema as the thing being tuned. It ships a `PydanticOptimizer` (low-level) and a
`Prompter` (higher-level, save/load, `predict()`/`run()`) API. Maturity: real unit-test
suite (134 tests, offline, no API key — verified below, all pass), an integration suite
gated on `OPENAI_API_KEY` (not run here), docs site (mkdocs), but the flagship
`ABLATION_RESULTS.md` numbers are **not measured** — they come from a synthetic/estimated
script, not a real benchmark run (see §4). Targets DSPy `>=3.0.4`; verified below to
actually run against DSPy **3.3.1**.

## 2. Every good idea

1. **JSON-schema-walk field-path extraction** — `extract_field_descriptions()` recursively
   walks `model.model_json_schema()`, resolving `$ref`/`$defs` and array `items`, to build a
   flat `{"address.street": "description"}` map, falling back to the field name when no
   description exists. `src/dspydantic/extractor.py:19-101`. `[adapt]` — the dot-path-over-
   nested-schema idea is directly reusable for walking a census/note frontmatter schema, but
   the kohaerenzprotokoll wiki has no nested Pydantic models today.
2. **Schema-preserving field rewrite, not description replacement** —
   `apply_optimized_descriptions()` deep-copies the JSON schema and only overwrites
   `description` in place, and `create_optimized_model()` rebuilds an equivalent Pydantic
   model class (preserving constraints like `min_length`/`pattern`/`examples`) with the new
   descriptions baked into `Field(...)`. `src/dspydantic/extractor.py:226-571`. `[catalogue]`
   — useful pattern if the target ever wants a "typed judgement" schema whose field
   descriptions get tuned without losing validators.
3. **Auto-optimizer selection by n** — `_auto_select_optimizer()`: n≤2 → MIPROv2 zero-shot
   (avoids a known BootstrapFewShot bug on tiny sets), 3–19 → BootstrapFewShot, ≥20 →
   BootstrapFewShotWithRandomSearch. `src/dspydantic/optimizer.py:512-533`. `[adopt]` — this
   is exactly the n=26 "surface-pairs" regime the target's optimizer ladder targets
   (LabeledFewShot→BootstrapFewShot→...); the thresholds and the *reason* (avoid a bootstrap
   bug at n≤2) are worth stealing verbatim as a starting heuristic.
4. **Fast-mode kwargs table, keyed by optimizer name** — `_FAST_MODE_KWARGS` shrinks demo
   counts/`auto="light"` for four optimizers by default in single-pass mode.
   `src/dspydantic/optimizer.py:25-30`. `[adapt]` — small, concrete, cheap: a dict of
   "sane defaults per optimizer name" that any wrapper around DSPy teleprompters should keep.
5. **Runtime `Teleprompter` subclass discovery** — `_get_teleprompter_subclasses()` walks
   `Teleprompter.__subclasses__()` recursively and maps `lower(name) -> class`, so any
   optimizer DSPy ships (including GEPA, SIMBA, COPRO, KNNFewShot...) is selectable by string
   without a hardcoded registry, and it validates the string against that live set.
   `src/dspydantic/optimizer.py:438-469`. `[adopt]` — cheap way to keep an optimizer ladder
   (the target's LabeledFewShot→...→GEPA plan) future-proof against DSPy adding new
   teleprompters, and to fail fast with a clear "valid options: [...]" error.
6. **Deepest-field-first, then prompts, sequential optimization with a rolling baseline** —
   `_optimize_sequential()` sorts fields by `.` depth (`_sort_fields_by_depth`), optimizes
   nested fields before parents, holds all other fields fixed per field, and only accepts an
   improvement (`new_score > baseline_score`, ties broken toward the shorter text).
   `src/dspydantic/optimizer.py:499-511, 1016-1269`. `[adapt]` — the "only keep it if it
   measurably beat the baseline, else keep the human original" discipline matches the
   target's P24 (done is a measurement) and P13 (never silently overwrite); the tie-breaks
   toward *shorter* text is a nice small idea (simpler wording all else equal).
7. **Parallel field optimization via `ThreadPoolExecutor` with per-field snapshots** — each
   field's optimizer sees an immutable snapshot of `current_descriptions` at task start, so
   threads never race on shared state; results are merged only after `as_completed`.
   `src/dspydantic/optimizer.py:959-1015`. `[adapt]` — directly useful if the target ever
   parallelizes per-document or per-field census/judgement calls.
8. **`on_progress` callback + `FieldOptimizationProgress` dataclass** — a structured event
   emitted per field/phase (`phase`, `score_before`, `score_after`, `improved`,
   `optimized_value`, `elapsed_seconds`), wrapped in try/except so a callback bug never
   aborts optimization. `src/dspydantic/optimizer.py:1282-1294`, `src/dspydantic/types.py:
   40-67`. `[adopt]` — good shape for any pipeline step's progress/telemetry event, and the
   "never let telemetry break the run" try/except is a small robustness idea worth copying.
9. **Evaluator plugin registry + factory** — `EVALUATOR_REGISTRY` (string → class) plus
   `EvaluatorFactory.create()` accepting a string, `{"type": ..., "config": {...}}`, or a
   custom class directly, with `default_lm` auto-injected into LM-needing evaluators.
   `src/dspydantic/evaluators/config.py`. `[adopt]` — a clean, minimal plugin pattern; the
   target's `scripts/rules/` decomposition library could use exactly this shape for
   `account()`'s per-subject question handlers.
10. **Per-field evaluator overrides** — `evaluator_config = {"default": ..., "field_overrides":
    {"id": "exact", "name": "levenshtein"}}`, applied only to leaf field paths.
    `src/dspydantic/evaluators/functions.py:413-568`. `[adapt]` — maps well onto
    one-term-or-two: exact match on canonical ids, fuzzy on surface variants, judge on
    free-text notes, all as one config object per field.
11. **Leaf-field-only scoring to avoid double counting** — before averaging field scores, it
    computes `leaf_field_paths` by dropping any path that is a strict prefix of another
    (i.e. only scores fields with no children). `src/dspydantic/evaluators/functions.py:
    501-568`. `[adopt]` — small but real bug class avoided (parent+child both scored,
    double-weighting a mismatch); worth a note in the target's own future metric code.
12. **`DeepDiff.deep_distance` for nested-structure scoring, binary for `exact`** — nested
    dict/list fields are compared with `DeepDiff(... get_deep_distance=True)`; the `exact`
    evaluator turns that into a strict 0/1, other evaluators use `1 - deep_distance`.
    `src/dspydantic/evaluators/functions.py:449-499`. `[adapt]` — a ready-made "structural
    diff distance" if the target ever needs to compare two structured outputs (e.g. two
    models' entity lists as sets) rather than hand-rolling set overlap.
13. **`None vs. None counts as a match, one-sided `None` is 0** — in per-field scoring, if
    both extracted and expected are `None` the field scores 1.0 (field correctly absent);
    if only one is `None` it's an automatic 0.0. `src/dspydantic/evaluators/functions.py:
    551-556`. `[adopt]` — a specific, easy-to-get-wrong scoring corner case worth reusing
    directly; getting this backwards silently inflates or deflates scores on optional fields.
14. **`PredefinedScoreEvaluator` — thread-local scripted score injection** — an evaluator
    that pops precomputed scores from a list in FIFO order, thread-safe via
    `threading.local()`, used to feed already-computed ground-truth or synthetic scores
    into the optimizer metric plumbing without recomputation.
    `src/dspydantic/evaluators/predefined_score.py`. `[adapt]` — good pattern for wiring the
    target's `Plan/runs/judgements.jsonl` recorded human decisions in as a "metric" for
    replay/regression testing (cf. `judgements.py`'s replay-and-compare idea), without
    needing a live judge call.
15. **Levenshtein similarity fallback for fuzzy matching, with a threshold gate** —
    a from-scratch (no extra dependency) Levenshtein distance normalized by max length, and
    a `threshold` below which the evaluator hard-returns 0 instead of a low fractional score.
    `src/dspydantic/evaluators/levenshtein.py`. `[adapt]` — directly usable as a baseline or
    tie-break signal alongside the target's `fold()` for one-term-or-two surface variants
    (`Guardian`/`Guardians`), though `fold()` already handles German inflection specifically,
    which generic Levenshtein does not (it would treat `Negentropie`/`Entropie` as "close"
    when the rule is NEVER merge — a real trap, see §4 item 2).
16. **LLM judge always returns a numeric fallback, never crashes on bad JSON** —
    `default_judge_fn`/`ScoreJudge` try `json.loads`, then two successively looser regexes
    for a `"score": <float>` pattern, and land on **0.5** (not error, not 1.0, not 0.0) if
    all parsing fails, logging a warning each time. `src/dspydantic/evaluators/functions.py:
    36-161`, `src/dspydantic/evaluators/score_judge.py:100-131`. `[skip]` for the fallback
    value itself (0.5 is arguably worse than refusing — see §4 item 1), but `[adopt]` the
    warning-and-continue mechanics and the JSON→regex→regex parsing cascade.
17. **`LabelModelGrader` — categorical/semantic label matching with an LLM only when needed**
    — checks exact string match first (cheap), and only calls the LLM to find "closest
    allowed label" if the expected label isn't literally in the allowed set; distinguishes
    exact/partial/no match with separate configurable scores.
    `src/dspydantic/evaluators/label_model_grader.py`. `[adapt]` — the "cheap check first,
    LLM only on ambiguous cases" gating is exactly the shape reconciliation-by-lookup already
    uses (`O(census)+O(judgement)`, not `O(wiki)`); this evaluator is a concrete instance of
    that same principle in a different codebase.
18. **`TextSimilarityEvaluator` — embeddings with an exact-match short-circuit and an
    exception fallback to exact match** — never crashes if the embedding provider fails or
    isn't installed; falls back to string equality. `src/dspydantic/evaluators/
    text_similarity.py:99-129`. `[adapt]` — the "if the fancy check fails, don't error, do
    the dumb-but-safe thing" fallback discipline is generically good, though note it
    silently masks embedding failures as a 0.0/1.0 result rather than reporting the failure
    (see §4 item 5).
19. **`PythonCodeEvaluator` — arbitrary user function evaluator, exceptions surfaced not
    swallowed** — unlike most evaluators here, a raised exception inside the user function is
    wrapped and re-raised as `RuntimeError`, not silently scored 0. `src/dspydantic/
    evaluators/python_code.py:51-75`. `[adopt]` — a good contrast case: this is the one
    evaluator in the package that fails loud, which is what P23 ("a guard reports what it
    could NOT check") wants; worth using as the template rather than the LLM-judge ones.
20. **Score clamping at every metric boundary** — every evaluator's return value, and the
    top-level `metric_function`, clamp to `[0.0, 1.0]` and log/print a warning if a metric
    returns something invalid (non-numeric or out of range), defaulting to `0.0` in that case.
    `src/dspydantic/optimizer.py:683-689`. `[adopt]` — cheap safety net against a custom
    metric silently propagating `None`/`NaN`/negative numbers into an optimizer's search.
21. **Auto-created single-field "OutputModel" for string-only examples** — if `model=None`
    and examples carry plain string `expected_output`, `create_output_model()` builds a
    throwaway one-field Pydantic model on the fly so the same optimization machinery works
    for free-text tasks. `src/dspydantic/optimizer.py:310-326`, referenced in `types.py`.
    `[catalogue]` — relevant if the target wants Pydantic-schema optimization for something
    as simple as "is this German and non-empty" (P19) without hand-rolling a model.
22. **Contextual dynamically-named DSPy Signatures** — `_make_contextual_field_signature()`
    builds a `type()`-constructed `dspy.Signature` subclass whose *class name* embeds the
    Pydantic model name (e.g. `OptimizeMedicalRecordFieldDescription`) at zero token cost,
    plus a short docstring and a `field_name` input, specifically because MiPROv2's proposer
    conditions on the signature's docstring/name and otherwise produces generic
    "Given field_description, produce optimized_field_description" filler.
    `src/dspydantic/module.py:50-155`, explained in `docs/explanation/how-optimization-works.md:44`.
    `[adopt]` — a concrete, cheap, well-motivated trick for getting more useful output from
    MiPROv2-style optimizers when optimizing skill descriptions
    (`.agents/skills/*/SKILL.md`, target's job #4) — literally the same "the class/field name
    is free context" idea applies to optimizing a `SKILL.md` `description` field.
23. **Template-placeholder-preserving prompt optimization** — when an `instruction_prompt`
    contains `{placeholders}`, the optimizer wraps it with explicit
    `ORIGINAL_PROMPT_TEMPLATE:` / `PROMPT_TEMPLATE_REWRITE_INSTRUCTIONS:` markers, asks the
    LLM to preserve placeholders, strips the markers back out afterward, de-duplicates a
    placeholder if the LLM echoed it twice, and **falls back to the original unmodified
    prompt if any placeholder went missing** after the rewrite.
    `src/dspydantic/module.py:214-368`. `[adopt]` — the "verify structural invariant after
    the LLM edit, revert to the safe original if it's violated" pattern is exactly the
    target's P12/P26 spirit (a model never gets to silently break something checkable);
    directly reusable if the target ever lets a model propose edits to a template line that
    must keep its `^[Lnn]`-style placeholders intact.
24. **Tie-break toward shorter text on equal score** — for both field descriptions
    (`_optimize_single_field`) and prompts (`_optimize_prompt`), when
    `new_score == baseline_score`, the shorter candidate wins.
    `src/dspydantic/optimizer.py:1126-1133, 1261-1269`. `[adopt]` — trivial, generically
    good default for any optimizer choosing among equally-scoring textual candidates.
25. **`skip_score_threshold` to avoid re-optimizing already-good fields** — in sequential
    mode, a field whose current baseline already clears a threshold is skipped entirely
    (with its own `FieldOptimizationProgress(phase="skipped")` event).
    `src/dspydantic/optimizer.py:1397-1424`. `[adapt]` — useful cost-control idea: don't
    spend judge/LLM calls re-checking a term/field that's already stable.
26. **`early_stopping_patience`** — sequential field optimization stops after N consecutive
    fields show no improvement. `src/dspydantic/optimizer.py:1375-1442`. `[adopt]` — same
    cost-control family as above; simple, no dependency, directly portable.
27. **Explicit optimizer-cost tiers documented per teleprompter** — a table of API-call
    counts (`~N`, `~N×10`, `~50`, `~200`, `~500+`, `~20-100`...) per optimizer, matched to
    "best for" use case. `docs/explanation/how-optimization-works.md:93-105`, also
    `docs/reference/optimizers.md:21` (`MIPROv2 | Fast | Fair | Low | Few examples`).
    `[catalogue]` — a ready-made "which optimizer for how much budget" cheat sheet the
    target's optimizer-ladder plan (LabeledFewShot→BootstrapFewShot→InferRules→SIMBA→GEPA)
    could reuse or cross-check against, though the actual call counts are asserted, not
    measured in this repo either (same caveat as the ablation results).
28. **Docs state an explicit "when NOT to optimize" section** — recommends manual
    descriptions when you have "very few or no examples," speed matters more than accuracy,
    or you already have domain expertise. `docs/explanation/how-optimization-works.md:
    179-186`. `[catalogue]` — matches the target's "small data: n=26, anything needing 100+
    examples is currently irrelevant" stance; worth citing as independent corroboration that
    a deterministic baseline (`fold()`) should stay the default until optimization clearly
    wins.
29. **Explicit example-count guidance table repeated in 3 docs** — "5–10: quick prototyping,
    10–20: most use cases, 20+: complex schemas" appears near-verbatim in
    `docs/core-concepts.md:64-68`, `docs/tutorials/extract-structured-data.md:120-124`, and
    `docs/guides/optimization/first-optimization.md:127`. `[catalogue]` — directly answers
    the brief's ask for "how many examples they recommend": their floor (5–10) is *below*
    the target's n=26 surface-pairs set, so by their own stated guidance the target already
    has enough data for BootstrapFewShot-class optimizers; no contradiction found.
30. **`save()`/`load()` round-trips only optimized artifacts, not model config** — persisted
    state (`PrompterState`) explicitly does *not* store `model_id`/API keys; the docstring
    says the user must reconfigure DSPy separately after loading.
    `src/dspydantic/prompter.py:779-813`, `src/dspydantic/types.py:76-100`. `[adopt]` — good
    separation of "learned artifact" vs. "runtime credentials," relevant if the target
    starts persisting any optimized rule (e.g. an optimized `fold()` variant or optimized
    skill description) — never bake a key or model choice into a checked-in artifact.
31. **Caching is opt-in and explicit, not a silent default** — `Prompter(cache=False)` by
    default; `cache=True` or a path string turns on a `dspy.LM(..., cache=...)` disk cache
    and creates the directory. `src/dspydantic/prompter.py:57-80, 124-177`. `[adopt]` —
    matches the target's own P18 ("repeats, cache off"); good evidence that off-by-default
    caching for LM calls is the right default when repeat calls need repeat measurement,
    though see §4 item 6 for the gap (the *judge* call inside evaluation isn't covered by
    the same cache flag at all, it just goes to whatever `dspy.settings.lm` currently is).
32. **`ScoreJudge`/`score_judge` explicitly named as the "Slow / $$$ / Excellent" evaluator
    tier in the decision tree**, positioned last after exact/levenshtein/text_similarity are
    ruled out. `docs/guides/evaluators/selection.md:1-45` (also mirrored as
    `docs/explanation/choosing-an-evaluator.md`). `[catalogue]` — a clean "cheapest-check-
    first" decision tree the target could adapt for choosing between `fold()`, Jev, and a
    full model call for one-term-or-two, mirroring what reconciliation-by-lookup already
    does architecturally.
33. **Ablation-of-optimization-strategy framing (not of optimizers)** — the ablation compares
    four *scheduling/parallelism* strategies (single-pass, sequential, sequential+parallel,
    sequential+max-val-cap) rather than comparing algorithms, i.e. it treats "how much of the
    search space to explore, and how" as its own axis independent of which teleprompter is
    used. `ABLATION_RESULTS.md:1-13`. `[catalogue]` — the framing (schedule/parallelism as an
    orthogonal axis to optimizer choice) is a useful mental model even though the specific
    numbers are fabricated (§4 item 3); a target ablation of, say, per-document vs. batched
    census reconciliation could use the same two-axis structure.

## 3. Directly reusable for the target

- **Job 1 (one-term-or-two, n=26 labelled pairs).**
  - `PydanticOptimizer._auto_select_optimizer()` (item 3) and `_get_teleprompter_subclasses()`
    (item 5) are directly portable as a small standalone helper — "given n examples, pick a
    DSPy teleprompter by name" — independent of the rest of dspydantic's Pydantic-schema
    machinery. Would need: strip out all the Pydantic-field-description plumbing; keep only
    the n-based dispatch table and the runtime subclass discovery.
  - `EvaluatorFactory` + evaluator registry (item 9) is a clean shape for the metric ladder:
    register a `fold_exact` evaluator (wraps the existing deterministic `fold()`), a
    `jev_choice` evaluator (wraps a Jev typed-choice call), and a `human_judgement_replay`
    evaluator built on `PredefinedScoreEvaluator` (item 14) fed from
    `Plan/runs/judgements.jsonl`, so `judgements.py`'s "replay recorded decisions" idea gets
    a reusable evaluator interface instead of a bespoke script.
  - What must change: the target's rule (`Negentropie`/`Entropie` = NEVER merge) is a
    *hard exception*, not a fuzzy-distance signal — `LevenshteinEvaluator` (item 15) would
    score that pair as similar and is actively wrong here; it must never be used as the sole
    or default evaluator for one-term-or-two, only `fold()`'s deterministic exception list or
    an evaluator that special-cases it explicitly.
- **Job 2 (entity lists, code writes the line).**
  - Item 11 (leaf-field-only scoring, drop parents that are prefixes of children) and item 12
    (`DeepDiff.deep_distance` for nested/list comparison) are reusable if entity lists are
    ever compared as structured sets (`{"entities": [...]}`) rather than free text — e.g.
    scoring two readers' entity lists against each other via set/list diff distance instead
    of hand-rolled precision/recall. This does **not** replace `entities.py`'s
    token-boundary `\bterm\b` matcher (item is about *scoring the resulting objects*, not
    about verifying a citation).
  - Item 22 (contextual, class-name-carrying Signatures) is directly relevant if a `dspy`
    module is ever built to *propose* entity names (still requiring code to find/verify the
    line, per the target's own rule that a model never types a line number) — the model name
    and field name folded into the Signature class is a real, cheap accuracy lever for
    MiPROv2-class optimizers.
- **Job 3 (census/`dspy.RLM` ingestion) and note/frontmatter.**
  - Item 1/2 (schema-walk + schema-preserving field rewrite) are the most directly reusable
    pieces if a census or note ever gets a Pydantic schema (e.g.
    `class CensusEntry(BaseModel): candidate: str; line: int; category: str`): dspydantic's
    extractor functions would let the target optimize *field descriptions* of such a schema
    (what counts as a "candidate," what "category" means) the same way it optimizes
    extraction-schema descriptions today — without dspydantic's optimizer itself needing to
    touch the census pipeline.
  - Item 23 (placeholder-preservation-with-fallback) is the concrete precedent for "if an
    LLM edits a template line, verify the invariant held or revert" — applicable to any
    future model-assisted rewrite of `Plan/briefings/extract.md` boilerplate that must keep
    its procedural markers intact.
- **Job 4 (SKILL.md description optimization via GEPA).**
  - This is dspydantic's closest match to an existing, tested feature: `optimizer="gepa"`
    is already selectable through item 5's discovery mechanism, and item 22's
    contextual-signature trick is precisely the technique needed to keep GEPA's `description`
    proposals grounded in "this is a skill description," not generic filler. The target could
    plausibly wrap `.agents/skills/*/SKILL.md`'s `description` field as a one-field Pydantic
    model (via item 21's `create_output_model()` pattern) and run dspydantic's
    `PydanticOptimizer(optimizer="gepa")` on it directly, rather than reimplementing the
    GEPA-plus-DSPy-Signatures wiring from scratch.
- **Open problem: cost/trace visibility of LM calls.**
  - `OptimizationResult` already carries `api_calls`, `total_tokens`, `estimated_cost_usd`
    fields (`src/dspydantic/types.py:29-36`), though in the code paths read here only
    `api_calls` is ever actually populated (via `len(lm.history)` in the example benchmark
    script, not inside the library itself — `examples/ablation_benchmark.py:126-128`); the
    dataclass shape is a reasonable target for the target's own "cost/trace visibility of LM
    calls" open problem, but the actual instrumentation is not implemented in the library —
    it would need to be added, not borrowed.

## 4. Conflicts with the principles — traps to name

1. **LLM judge silently defaults to 0.5, not a refusal, on any parse failure.**
   `default_judge_fn` (`src/dspydantic/evaluators/functions.py:127-161`) and `ScoreJudge`
   (`src/dspydantic/evaluators/score_judge.py:108-129`) both fall through three
   increasingly loose parse attempts and land on a **hardcoded 0.5** if none succeed. This
   directly violates P23 ("a guard reports what it could NOT check"): a broken judge call
   looks exactly like a genuinely middling extraction, and nothing distinguishes "the model
   judged this mediocre" from "the model's output was unparseable garbage." This is
   structurally similar to the target's own worst past defect (a coverage metric that
   returns 1.0 on empty input) — same shape, different constant. **Trap: never adopt a
   fallback numeric score for a parse failure; make it None/raise/flag instead.**
2. **Levenshtein/text-similarity evaluators can and would silently "merge" things the target
   forbids merging.** For a surface pair like `Negentropie`/`Entropie`, Levenshtein
   similarity is high (few edits, long string) even though the target's rule is
   NEVER merge these two terms. Nothing in `LevenshteinEvaluator` or `TextSimilarityEvaluator`
   knows about domain-specific hard exceptions; they would return a comfortably high score.
   This is the exact trap P13 warns about ("never merge two sources' readings into one
   definition… conflict detection is never mechanised") — a generic fuzzy-distance evaluator
   is precisely the kind of mechanised judge that would produce the target's cited
   `Zero-Trust` false-conflict failure mode, just inverted (false merge instead of false
   conflict).
3. **`ABLATION_RESULTS.md`'s numbers are not measurements — they are estimates from a
   script that says so out loud.** `examples/ablation_benchmark_mock.py:219` prints
   `"⚠️ SYNTHETIC BENCHMARK: Using estimated metrics for demonstration"` and the real,
   API-backed `examples/ablation_benchmark.py` has three of its four configs commented out
   (`# ("Single-pass (default)", ...)`, `# ("Sequential", ...)`,
   `# ("Sequential + Max Val=5", ...)` — `examples/ablation_benchmark.py:161-164`), so even
   if it were run, it would only ever produce one row, not the 4-row comparison the
   markdown file presents as fact. The markdown file itself carries no `n=`, no seed, no
   run date, no link to a log — it reads as measured (`"~30-60 seconds"`, `"+5-15% typical"`)
   but is asserted. This is a direct violation of the target's own "A claim is measured, or
   marked unmeasured" rule (from `kohaerenzprotokoll/CLAUDE.md`) — the exact failure mode
   the target explicitly built `state.py --prose` to catch. **Do not cite these numbers as
   evidence of anything; harvest only the ablation method's shape (§2 item 33), not its
   results.**
4. **A model can type a line number.** Nowhere in `dspydantic` does an LLM output get
   constrained to avoid inventing a line/id/offset — every evaluator either compares whole
   field values or lets the model free-write into a `str` field. This isn't a bug in
   dspydantic's own domain (it doesn't do line-cited extraction), but it means none of its
   machinery enforces the target's P12/P26 ("a model never types an identifier or line
   number — code does"); if any of dspydantic's Pydantic models were reused for a
   census/note schema with a `line: int` field, dspydantic would happily let the optimizer
   tune the *description* of that field to encourage the model to guess a number, with no
   verification step anywhere in the library. **Any reuse of a dspydantic-optimized schema
   for something with a citation/line field needs an external verifier
   (`scripts/quotes.py`-equivalent) bolted on; dspydantic provides none.**
5. **Fallback-to-exact-match on embedding/API failure looks identical to a genuine match.**
   `TextSimilarityEvaluator.evaluate()` catches *any* exception from the embedding call and
   falls back to `1.0 if extracted_str == expected_str else 0.0` (`src/dspydantic/
   evaluators/text_similarity.py:123-129`) — a network failure, a missing dependency, and a
   real semantic mismatch are all indistinguishable in the returned score. Same P23
   violation family as item 1.
6. **The "cache off by default" discipline the library states doesn't cover judge calls.**
   `Prompter.__init__`'s `cache` flag only threads through to the one `dspy.LM(...)` it
   itself configures (`src/dspydantic/prompter.py:57-80`); `ScoreJudge`, `LabelModelGrader`,
   and `default_judge_fn` all call `dspy.settings.lm` (or a separately-passed `judge_lm`)
   directly with no cache parameter of their own — whatever cache setting that LM object
   already has (set elsewhere, possibly by the user's own `dspy.configure`) silently applies.
   Not a crash risk, but a place where "cache off" is not actually guaranteed end-to-end,
   contrary to how it reads in the docs/README.
7. **DSPy pin is looser than what's actually exercised.** `pyproject.toml` says
   `dspy>=3.0.4` and `uv.lock` is frozen at `dspy==3.0.4` (`uv.lock:707-708`), i.e. the
   *committed* lockfile in this repo does not reflect DSPy 3.3.1 at all — a description gap
   (the repo describes itself as compatible with recent DSPy, but its own lockfile is stale
   by three minor versions). Confirmed working with 3.3.1 only by resolving fresh (§5).

## 5. Dependencies & cost

- **Runtime deps** (`pyproject.toml`): `pydantic>=2.0.0`, `dspy>=3.0.4`, `deepdiff>=8.0.0`,
  `pillow>=10.0.0`, `pdf2image>=1.16.0`, `rich>=13.0.0`. No pin ceiling on `dspy`.
- **Verified**: fresh `uv venv --python 3.11` + `uv pip install -e /home/user/dspydantic
  pytest` resolves **DSPy 3.3.1** (not the lockfile's frozen 3.0.4) with no conflict, so it
  can live in a venv alongside the target's pinned `.venv-dspy` (DSPy 3.3.1) without moving
  that pin, provided it's installed into its *own* venv (not `.venv-dspy` itself, to avoid
  disturbing that pin's resolution) — command used:
  `uv pip install --python .venv-dspydantic/bin/python -e /path/to/dspydantic`.
- **Offline unit tests pass with no API key**: `python -m pytest tests/unit -q` → **134
  passed, 0 failed, 1.44s**, no network calls, no `OPENAI_API_KEY` needed (verified in this
  scan). This satisfies the target's P5 (every workflow ships an offline, no-key fixture) —
  dspydantic's own test suite already is one, for its own code.
- **Integration tests require `OPENAI_API_KEY`** and are explicitly `@pytest.mark.skipif`-
  gated on it (`tests/integration/test_optimizer_integration.py:29-32` and similarly across
  `test_full_pipeline.py`, `test_miprov2_descriptions.py`); not run in this scan (rule:
  never with an API key).
- `TextSimilarityEvaluator` has a soft, undeclared dependency on `sentence-transformers`
  (or `openai` for its embedding path) that is **not** listed in `pyproject.toml`'s
  `dependencies` or `[project.optional-dependencies]` at all — it's imported lazily inside
  `_get_embedder()` and raises `ImportError` with an install hint only when that evaluator
  is actually used (`src/dspydantic/evaluators/text_similarity.py:50-70`). Cheap to ignore
  unless that specific evaluator is adopted.
- No API keys are needed for anything in §2/§3 except: the LLM-judge evaluators
  (`ScoreJudge`, `LabelModelGrader`, `default_judge_fn`) and any actual optimizer `.compile()`
  run, all of which need `dspy.configure(lm=...)` with a real provider key — same shape as
  the target's own Jev/OpenRouter key requirement, no new key type introduced.

## 6. Verdict

The single most valuable thing to take is the **evaluator-registry/factory pattern**
(§2 items 9–20) paired with the **n-based optimizer auto-selection + runtime teleprompter
discovery** (§2 items 3, 5): together they're a small, dependency-light, already-tested
recipe for "pick a cheap check first, escalate to a judge only when needed, and pick an
optimizer by how much data you actually have" — which is exactly the shape the target's
optimizer ladder and reconciliation-by-lookup already want, just not yet packaged as
reusable code. The contextual-Signature trick (item 22) is the second most valuable single
idea, directly aimed at job 4 (GEPA-optimizing `SKILL.md` descriptions). Leave behind:
`ABLATION_RESULTS.md`'s numbers entirely (fabricated, not measured — harvest only the
ablation's two-axis *framing*), and never adopt Levenshtein/text-similarity/LLM-judge as a
default or sole evaluator for one-term-or-two, since each would happily produce exactly the
false-merge/false-confidence failure the target's principles were written to prevent.
