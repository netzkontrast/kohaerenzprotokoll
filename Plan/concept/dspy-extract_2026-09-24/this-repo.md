# What this repository (kohaerenzprotokoll) has already measured, decided or learned about calling models

Scope: everything below is evidence *from this repository itself* — its scripts,
their selftests, its `Plan/` concept notes, learnings, decisions and run
artifacts. External-repository findings are included only where this repo
explicitly ported, verified or measured against them (tagged accordingly).
Numbers marked "current" were re-derived with `python3 scripts/state.py` on
2026-09-24 during this extraction; numbers marked with a date are historical
snapshots from a specific document and may have since moved — several sections
below show the same quantity at multiple points in time on purpose, because
this repository's own working agreement (`CLAUDE.md`, *Changing your mind*)
treats a moving number as a finding, not noise.

## CALL

- **`lmrun.py` is the only way a model is called** — every step that calls a real model goes through `lmrun.call(program, step=, subject=, approval=, german=, **inputs)`, which appends one JSON record per call to `Plan/runs/<subject>/lm/<step>.jsonl`. `scripts/lmrun.py:1-44` [decided]

- **Cache is refused, not just discouraged** — `call()` raises `RuntimeError` if the configured `dspy.settings.lm` has `cache=True` (fixtures are exempt): "a cached call replays its first answer (P18)". `scripts/lmrun.py:117-120` [decided]

- **Approval is refused, not just recommended** — a non-fixture LM with no `approval=` string raises `RuntimeError` naming that the author's decision must be named (`NOW.md`). `scripts/lmrun.py:121-123` [decided]

- **Four statuses only, never a score** — `answered` / `refused` / `unparsed` / `unreachable`; a 404 is explicitly "not a wrong answer" (P15). `scripts/lmrun.py:61,111-138` [decided]

- **`_unreachable()` classification** — matches DSPy 3.3's own `LMProviderError`/`LMTransportError` (only if present on the installed version) plus a name-set including `NetworkRefused`, `APIConnectionError`, `NotFoundError`, `AuthenticationError`, `RateLimitError`, `ServiceUnavailableError`, `Timeout`, `ConnectionError`, `PermissionDeniedError`, checked through the exception's `__cause__`/`__context__` chain. `scripts/lmrun.py:94-108` [decided]

- **P19 built into the record, not left to the caller** — `status` flips to `refused` if every choice's content is empty/None or any `finish_reason == "length"` (a reasoning model spending its whole budget on reasoning), *before* any output parsing is trusted; a German field is checked with an 8-word-minimum threshold (`MIN_WORDS_FOR_LANGUAGE`) below which the verdict is `"unmeasured"` rather than wrong. `scripts/lmrun.py:64,149-163,242-243` [decided]

- **Record schema** — `inputs`, `outputs` frozen at call time (never reconstructed later), `raw` (the model's own text from `lm.history`), `finish_reason`, `usage` (via `dspy.track_usage()`), `cost` (summed from each history entry's `cost`), `model`, `fixture` flag, `status`, `error`, `problems`, `approval`. `scripts/lmrun.py:165-181` [decided]

- **The German/English word-marker lists used for the P19 language check**: `MARKERS = {"de": (" der ", " die ", " das ", " und ", " nicht ", " ist ", " ein ", " eine "), "en": (" the ", " and ", " not ", " is ", " of ", " with ", " a ", " an ")}` — a crude but cheap heuristic, deliberately paired with the 8-word `MIN_WORDS_FOR_LANGUAGE` floor so a short answer is reported `unmeasured` rather than wrongly judged. `scripts/lmrun.py:62-64` [decided]

- **10 offline selftest cases** (no key, no network) assert every status plus every refusal: `answered`, `unparsed` (garbage text 3×), `refused` (empty string), `answered` w/ an empty output field, `answered` w/ English content where German was required, `unreachable` via a custom `NetworkRefused`, `unreachable` via DSPy's own `LMTransportError`, a cached LM refused, an unapproved real LM refused, and a one-word answer scored `unmeasured` rather than wrong. `scripts/lmrun.py:185-244` [measured]

- **The tenth case is new (2026-09-24) and found a real bug** — the first nine offline cases never exercised DSPy 3.3's own `LMTransportError`; a live run did, and `call()` **re-raised it instead of recording `unreachable`** — the classifier's `_NO_ANSWER` tuple (built from `hasattr(dspy, n)`) now explicitly includes it. `Plan/concept/dspy-toolchain_2026-09-23.md:16`; `scripts/lmrun.py:94-98,206-208` [lesson]

- **Providers actually used**: OpenRouter (`openrouter/<vendor>/<model>` LiteLLM strings, `api_base="https://openrouter.ai/api/v1"`) for DSPy-side real calls; TypeSafe's Jev (`jev-latest`, resolved `jev-1.13.0` on 2026-09-23) for typed judgements; a local `claude -p` bridge (`Legacy/tools/kpwiki/local_lm.py`, the `Hmbown/dspy-local` pattern) used once for a key-less RLM run. `scripts/rlm_ingest.py:99-107,227-233`; `.agents/skills/typesafe/SKILL.md:16,125-126`; `Plan/concept/rlm-measured-on-the-trap_2026-09-17.md:13-17` [measured]

- **Keys never touch a file or chat** — `OPENROUTER_API_KEY` and `TYPESAFE_API_KEY` come from the environment's settings only; `rlm_ingest.api_key()` falls back to a git-ignored `.env` only if the environment variable is absent. `CLAUDE.md:41,656-657`; `scripts/rlm_ingest.py:99-107` [decided]

- **Free models actually reached in this repo's experiments**: `nex-agi/nex-n2.5-pro:free`, `nex-agi/nex-n2.5-mini:free`, `dots-studio/dots-3-note-preview:free`, `nvidia/nemotron-3.5-lightning:free`, `nvidia/nemotron-3-super-120b-a12b:free` (the `rlm_ingest.py` default), `openrouter/openrouter/free` (the free-models router), plus `qwen/qwen3.8-27b:free`, `google/gemma-4-31b-it:free`, `poolside/laguna-s-2.1:free` in `bilingual.py`'s rotation. `Plan/concept/rlm-measured-on-the-trap_2026-09-17.md:36-39`; `Plan/quality/lm-bench_2026-09-16.md:10-20`; `scripts/bilingual.py:68-71` [measured]

- **`rlm_ingest.py`'s default model reasoning**: `nvidia/nemotron-3-super-120b-a12b:free` was chosen because it is free *and* answers structured-output requests — "18 of the 24 free models on OpenRouter do not". The first default, `nex-agi/nex-n2.5-pro:free`, returns its final answer inside `reasoning_content` with `text: None`, which DSPy's ChatAdapter rejects as an empty response — "worth re-testing; not worth losing a run to." `scripts/rlm_ingest.py:90-95` [lesson]

- **Jev call cost, measured once**: 0.6s, 414 input tokens, 73 output tokens for 3 questions over one sentence. `Plan/concept/jev-in-ingestion_2026-09-23.md:15-16,161-163`; `.agents/skills/typesafe/SKILL.md:14-16` [measured]

- **`pairs.py`'s exact CLI contract, the model-calling surface for job 1**: `python3 scripts/pairs.py score [--rule fold] [--record]` (stdlib, offline); `.venv-dspy/bin/python scripts/pairs.py run --optimizer labeled|bootstrap|inferrules|simba|gepa --dry-run`; a real run additionally needs `--model M --approval "<the author's decision>"`, with optional `--folds 5 --repeats 3 --record --reflection-model M`. `scripts/pairs.py:37-40,203-225`; `.agents/skills/tools/references/commands.md:141-151` [decided]

- **`rlm_ingest.py`'s exact CLI contract and defaults**: `.venv-dspy/bin/python scripts/rlm_ingest.py <slug> --approval "<decision>" [--model M] [--iters N] [--calls N] [--sub-model M]`, plus `--score` (compares against the human list) and `--selftest` (offline). Defaults: `--iters 12`, `--calls 40` (`max_llm_calls`), `--model` defaults to `DEFAULT_MODEL`. `scripts/rlm_ingest.py:68-72,326-341` [decided]

- **`check_dspy_surface.py`'s stated reason for existing**: `dspy.RLM` is upstream-experimental and "was renamed once already (`max_iterations` → `max_iters`, `interpreter` → `interpreter_factory`, in 3.3.0)... A renamed keyword does not fail at import — it fails in the middle of a paid run, or worse, is swallowed by `**kwargs`." `scripts/check_dspy_surface.py:3-6` [lesson]

- **Jev price, quoted from OpenRouter (2026-09-23)**: $0.042 per million input tokens, output free; Haiku by comparison is $1/$5 per million. Projected whole-corpus cost (110,796 lines) with Jev: "roughly $3". `NOW.md:311-313` [measured]

- **`bilingual.py` total measured cost**: 1,015 Jev calls, 10.9M input tokens, ≈$0.46; plus 99 free-OpenRouter calls that took 70 minutes because "only `nemotron-3-super` and `dots-3-note` answered a batch of 80 reliably". `NOW.md:363-365` [measured]

- **A model sweep for OpenRouter model selection exists in this repo** (`Plan/quality/lm-bench_2026-09-16.md`), but it scores the *retired* `tools/kpwiki` `SourceIngest` DSPy program on `ingest_metric`, not the current pipeline — kept here because it is real measurement done in-repo and the lessons (below, MET/FAILED) still apply to any model call made here today. `Plan/quality/lm-bench_2026-09-16.md:1-20` [measured]

- **lm-bench full result table (n=3 attempts, cache off, models concurrent)**: `openrouter/openrouter/free` (Free Models Router, 6 attempts) 100% structure, score 1.00, 28.7s median, free; `nex-agi/nex-n2.5-pro:free` 100%/1.00/35.2s/free; `dots-studio/dots-3-note-preview:free` 100%/1.00/48.2s/free; `inclusionai/ling-3.0-flash` 100%/1.00/24.3s/n·a cost; `qwen/qwen3.7-flash` 100%/1.00/41.9s/$0.0019; `openai/gpt-oss-120b` 100%/1.00/74.2s/$0.0016; `ibm-granite/granite-4.0-h-micro` 100%/**0.75**/13.9s/n·a; `mistralai/mistral-nemo` 100%/**0.73**/27.9s/$0.0001; `nvidia/nemotron-3.5-lightning:free` **67%**/1.00/245.2s/free. `Plan/quality/lm-bench_2026-09-16.md:10-20` [measured]

- **Free Models Router (`openrouter/openrouter/free`)**: LiteLLM string is `openrouter/openrouter/free` (provider prefix + the router's own id `openrouter/free`; the single-segment spelling resolves to the provider but sends model id `free`, which does not exist). Benchmarked at 6 attempts (not 3) because it serves a different underlying model per call. Held schema on all six, second-fastest median, no cost — but **DSPy's cache keys on the prompt, not on the model that answered**, so a cached hit silently replays whichever model happened to answer first; reliability must be measured with cache off. `Plan/quality/lm-bench_2026-09-16.md:29-49` [lesson]

- **Author's rule (2026-09-16, dated the same day as the two-layer reset), narrow in scope**: "use OpenRouter only where no DSPy program, and therefore no typed schema, is at stake." Grepping every LLM-touching file outside `tools/kpwiki/` found only 3 matches (two setup scripts + `lm_bench.py` itself); the one real candidate named was `scripts/lit_critic_gate.py`, a Legacy-era free-text prose gate. `Plan/quality/lm-bench_2026-09-16.md:102-119` [decided]

- **Fetching a document never calls a model at all** — `sources.py fetch` calls the Drive MCP connectors directly from a script; the learnings file states plainly "**No model is involved at any point** — not the orchestrator, not a subagent," saving an estimated ~6.5M tokens against a subagent-delegated plan. `Plan/learnings/fetch.md:84-86` [decided]


## OPT

- **The optimizer ladder, in cost order**: `LabeledFewShot(k)` (~0 LM calls, the floor) → `BootstrapFewShot` (tens of calls, `max_bootstrapped_demos=4` default) → `InferRules` (tens × `num_candidates`) → `SIMBA` (medium, "caution: `bsize` defaults to 32, larger than the whole trainset") → `GEPA` (high, needs a 5-arg metric `Prediction(score, feedback)` and a reflection LM). `Plan/concept/optimizers-and-data_2026-09-17.md:19-27` [decided]

- **Ruled out and why**: `MIPROv2` (wants 100+ examples), `BootstrapFewShotWithRandomSearch` (50+), `BootstrapFinetune` (needs a finetunable model; free API models are not), `KNNFewShot` (needs a `dspy.Embedder` — "though qmd now has a local embedding model, so this becomes cheap if step 0–2 disappoint"), `AvatarOptimizer` and `BetterTogether` (not this shape of problem), `Ensemble` (nothing to ensemble yet). `Plan/concept/optimizers-and-data_2026-09-17.md:29-34` [decided]

- **`InferRules` singled out as the rung that fits this project specifically** and is "absent from `dspy-optimizer-selection`'s table" — because `Plan/runs/judgements.jsonl` already stores a human-written rule per near-match decision, so an induced rule can be compared directly against a person's stated rule; a surviving induced rule becomes a `fold()` candidate, replayable by `judgements.py`. `Plan/concept/optimizers-and-data_2026-09-17.md:36-58` [claim]

- **A trap named before any run**: `InferRules.compile()` silently splits the trainset 50/50 when no `valset` is passed — at n=26 that was 13 train/13 validation "with no canary held back at all". `Plan/concept/optimizers-and-data_2026-09-17.md:60-62` [lesson]

- **`pairs.py` is the built harness for job 1** ("one term or two"): rule-first (only asks a model about the residual `fold()` leaves two-terms), a canary veto against every pair in `selftest.MUST_NOT_MERGE` (a merge vetoes the whole candidate regardless of accuracy, because `dspy.GEPA` optimizes a mean and would otherwise cost only 1/n), pinned+stratified k-fold split by decision (canaries never trained on), repeats with cache off, and a 5-argument GEPA-shaped metric from day one. `scripts/pairs.py:1-46` [decided]

- **`pairs.py optimizer()` construction per rung**: `labeled`→`dspy.LabeledFewShot(k=min(8, train_size))`; `bootstrap`→`dspy.BootstrapFewShot(max_bootstrapped_demos=4, max_labeled_demos=8)`; `inferrules`→`dspy.InferRules(num_candidates=4, num_rules=6)`; `simba`→`dspy.SIMBA(bsize=min(train_size, 16), num_candidates=4, max_steps=4)` (overriding the 32 default because it exceeds the trainset); `gepa`→`dspy.GEPA(auto="light", seed=0, track_stats=True)`. `scripts/pairs.py:121-137` [decided]

- **SIMBA's `bsize` override is evidence-based**: "`dspy-book-optimizers` measured SIMBA scoring *below* its baseline while being the most expensive run of twelve" (an external-repo finding, applied here as the reason to cap `bsize`). `Plan/concept/dspy-toolchain_2026-09-23.md:219-220` [claim]

- **`pairs.py`'s deterministic-rule registry currently holds exactly one entry**: `RULES = {"fold": lambda a, b: "one-term" if fold(a) == fold(b) else "two-terms"}` — explicitly built so that "a new deterministic rule — the morphology rule `NOW.md` names — is one entry in `RULES`" once the author decides its reach, scored the same way via `pairs.py score --rule <name> --record`. `scripts/pairs.py:42-45,61-63,85-94` [decided]

- **Status as of the last build (2026-09-23/24)**: all five optimizers run end-to-end under `--dry-run` against the offline fixture; **none has run against a real model** — "that sends corpus words to a third party, and the author has not said yes to it." `CLAUDE.md:736-740`; `Plan/concept/dspy-toolchain_2026-09-23.md:18` [measured]

- **`fold()` scores 33/57 = 58% on the current ledger** (`pairs.labelled`/`pairs.fold_correct`, current `state.py`) — the floor row job 1 must beat before any optimizer run is worth its cost. `CLAUDE.md:736-737`; `python3 scripts/state.py --get pairs.fold_correct` [measured]

- **Job 2 (entity-list extraction as a structural fix) is built as an idea but not implemented** — gated on "the author's definition of an entity" (research vocabulary vs. the fictional world), named explicitly as open in `NOW.md`. `Plan/concept/dspy-toolchain_2026-09-23.md:20,279-280` [decided]

- **Job 3 (`rlm_ingest.py`) is built — cache off, call budget, `find_line`/`count` tools, `--approval` required — but not run live**: it "needs Deno as well" and a yes. `Plan/concept/dspy-toolchain_2026-09-23.md:19` [decided]

- **Job 4 (skill descriptions via `gepa.optimize_anything`) has only a guard built** (`example_param_ok()` in `check_dspy_surface.py`) — "no routing failures recorded, so no dataset (P4)". `Plan/concept/dspy-toolchain_2026-09-23.md:21,321-323` [decided]

- **`gepa.optimize_anything`'s trap**: it introspects its evaluator by `inspect.signature` and the **second** parameter must be literally named `example`; named anything else, the data is silently dropped and the crash surfaces layers later. Guarded by `check_dspy_surface.example_param_ok()`, self-tested against a "good" (`candidate, example`) and a "bad" (`candidate, task`) signature. `scripts/check_dspy_surface.py:56-63,103-106`; `Plan/concept/dspy-toolchain_2026-09-23.md:316-319` [lesson]

- **`dspy.GEPA` asserts `reflection_lm is not None` at construction, not compile time** — checked behaviourally in `check_dspy_surface.run()` by constructing `dspy.GEPA(metric=…, auto="light")` with no `reflection_lm` and expecting an `AssertionError`. `scripts/check_dspy_surface.py:84-89` [measured]

- **Build order actually prescribed**: guards (0.1–0.4, no model/key) → the call record + baseline ledger (1.1–1.2), with `rlm_ingest.py` moved onto `lmrun.py` as the *first* user so the wrapper is "proved on a real instance rather than anticipated" (P3) → job 1a, a deterministic morphology rule scored through `baseline.py` against `fold()` — "still no model" → only then any optimizer rung. `Plan/concept/dspy-toolchain_2026-09-23.md:355-368` [decided]

- **`continuous-improvement`'s five-step order** (written 2026-09-17, predates the toolchain build): 1) carry the evidence a judgement rested on into the ledger row — "not yet done, and it is not a model"; 2) optimise skill descriptions with `optimize_anything` — "unblocked today", needs no gold candidate list, scored on trigger queries instead; 3) two or three more hand-read documents to make extraction trainable; 4) the n=26(→57) one-term-or-two ladder, `LabeledFewShot` first, "nothing that fails to beat 17/26 [the then-baseline] is worth an LM call"; 5) only then a recall metric over candidate lists using DRG's `_score_sets` with `fold()` as the key. `Plan/concept/continuous-improvement_2026-09-17.md:166-180` [decided]

- **"Nothing in the pipeline calls any of the three [`dspy-skills`, `dspytools`, `drg-kg`] yet. They are installed, reachable, and measured against this repository."** `CLAUDE.md:715-716`; `Plan/concept/continuous-improvement_2026-09-17.md:182-184` [decided]

- **`dspy-skills`/`dspytools` fit named as the cheapest real DSPy use available**: `SkillManager([Path(".agents/skills")])` builds the `<available_skills>` block **from the `description` field alone**, so the description is "the optimisable surface" and needs no gold list — only trigger queries. `Plan/concept/continuous-improvement_2026-09-17.md:83-98`; `CLAUDE.md` *Installing anything* [claim]


## MET

- **`fold()` baseline evolution, over time, on the same one-term-or-two task** (each point sourced to when it was measured): **14/17 = 82%** (2026-09-17, first 17 rows) → **17/26 = 65%** (2026-09-17, after 13 more judgements added — "every new miss is a plural or an inflection") → **21/36 = 58.3%** (`Plan/runs/baselines.jsonl`, 2026-09-23T18:45:35) → **27/44 = 61.4%** (2026-09-24T08:50:04) → **29/49 = 59.2%** (2026-09-24T10:15:10) → **33/57 = 57.9% ≈ 58%** (current, `CLAUDE.md:736-737`, `state.py`). `Plan/concept/trainset-and-the-baseline_2026-09-17.md:13,33-42`; `NOW.md:164-170`; `Plan/runs/baselines.jsonl` [measured]

- **`fold()` has "perfect precision and 65% recall" on the labelled set**: every miss is gold-says-one-term/`fold()`-says-two-terms, never a false merge; not one false merge has ever been produced. `Plan/concept/continuous-improvement_2026-09-17.md:49-53` [measured]

- **All misses are the same shape**: German plurals/inflections — `Guardian`/`Guardians`, `Riss`/`Risse`, `Alter`/`Alters`, `Kern-Welt`/`Kern-Welten`, `AEGIS`/`Rest-AEGIS` — "`fold()` strips the German definite article and does nothing else. The next improvement is a rule, not a model." `NOW.md:164-170`; `Plan/concept/continuous-improvement_2026-09-17.md:52-53` [claim]

- **The canary that decides whether a model beats the baseline for the right reason**: `Negentropie`/`Entropie` must never merge. On the original n=17 set, `nex-agi/nex-n2.5-mini:free` **tied** `fold()`'s score (14/17=82%) while **merging this canary** — "worse than the baseline however it scores"; a scalar metric alone would have called the two equal. `Plan/concept/trainset-and-the-baseline_2026-09-17.md:48-60`; `Plan/concept/skills_2026-09-17.md:135-137` [lesson]

- **Full canary set** (`selftest.MUST_NOT_MERGE`, asked of every optimizer candidate via `pairs.canaries()`): `(Negentropie, Entropie)`, `(Guardian, Guardians-Subroutine-Log)`, `(Kern-Welt, Kern-Programm)`, `(Riss, Rissbildung-Protokoll)`. `scripts/selftest.py:73-78` [decided]

- **`fold()`'s positive rule set** (`MUST_MERGE`, must always merge): `(Die Konstrukt-Stadt, Konstrukt-Stadt)` — the definite-article rule, `(Der Möglichkeits-Garten, Möglichkeits-Garten)`, `(das Nexus, Nexus)`. `scripts/selftest.py:81-85` [decided]

- **Zero-shot free-model comparison on the original n=17** (no optimizer, held-out canary): `nex-agi/nex-n2.5-pro:free` **16/17=94%** (canary held; the one miss was an unparsable answer, not a wrong decision) — beats `fold()`; `nex-agi/nex-n2.5-mini:free` 14/17=82% but merged the canary — worse than the baseline despite the tied score; `fold()` 14/17=82% (canary held by construction). `Plan/concept/trainset-and-the-baseline_2026-09-17.md:50-60` [measured]

- **Caution against reading too much into that delta**: "94% against 82% on **17 items is 16 right against 14** — two examples. There is no held-out split; the canary is one case. Nothing here justifies replacing `fold()` in the pipeline." `Plan/concept/trainset-and-the-baseline_2026-09-17.md:68-71` [lesson]

- **`baseline.py compare()` checks against a floor, not only the previous row** — ported from `dspy-agents`, whose monitor only compared consecutive rows, so "a run logged at `score=0.0, total_calls=0` became a normal baseline and a pipeline broken from its first run could never alert." Here the floor defaults to the task's first row (the deterministic rule) or a `--floor`-named candidate. `scripts/baseline.py:19-24,85-114` [decided]

- **`baseline.py` row schema**: `task, candidate, program_hash, trainset_hash, n, scored, correct, score, vetoed, outcomes{id: 1|0|fraction|null}, cost, at, note`; `score = correct/scored` and `scored` is reported beside `n` so an unscored example is visible rather than silently dropped; `program_hash`/`trainset_hash` are content hashes, never a manually bumped tag. `scripts/baseline.py:1-30,56-68` [decided]

- **A `vetoed` row fails `compare()` whatever its score**, because `dspy.GEPA` optimizes a mean and a canary merge would otherwise cost only 1/n. `scripts/baseline.py:15-18,97-98` [decided]

- **`baselines.jsonl` actual recorded rows (graphrag-retrieval)**: seeds-only (the floor) n=9 score=0.3947 → n=10 (added C6) 0.3838 → n=14 (added C7–C10) 0.4527; personalized PageRank (`ppr`) n=9 0.5782 → n=10 0.5633 → n=14 0.6203; `ppr+gloss` identical to `ppr` at every point ("no bench case is English-only, so no change is expected"). `Plan/runs/baselines.jsonl` (all 7 graphrag-retrieval rows, 2026-09-23T18:39–2026-09-24T10:15) [measured]

- **The current CLAUDE.md figure (17 cases, 42%/64%) is one step ahead of the last recorded baseline row** (n=14, seeds 45.3%/ppr 62.0%, 2026-09-24T10:15:10) — meaning documents 11–13 (which added C11, C12, Q5) grew the bench cases without a matching `graphrag.py bench --record` run since. `Plan/runs/baselines.jsonl` vs. `CLAUDE.md:439-440` and current `state.py` (`graphrag.cases=17`) [claim]

- **graphrag bench recall@8, current**: seeds-only floor **42%**, personalized PageRank **64%**, over **17** cases the wiki labels itself (each question's `raised_by`, each conflict's `pages`), the case's own graph node removed first so it cannot retrieve itself. Historically (before documents 7–9) it was 9 cases at 40%/58%. `CLAUDE.md:438-444`; `Plan/concept/graphrag_2026-09-23.md:94-101` [measured]

- **What the bench number is *not***: "Seventeen cases, written by the same hand that wrote the pages, so the labels and the graph share an author." `Q2` finds no seed at all (its question names "the seven protocol terms" and none of them by surface). Precision is low where a conflict has only one page (C1, C2) because 8 pages are always returned. `Plan/concept/graphrag_2026-09-23.md:103-108` [claim]

- **P27 — establish the human ceiling before scoring a model. Evidence**: two independent readings of one document (`orte-konzept-fuer-kohaerenz-protokoll`), same process, neither seeing the other — **131 and 113 candidates, 80 shared** → precision 0.71, recall 0.61, **F1 0.66**. A second pair on `roman-lokalitaeten-konzept-und-ausarbeitung` gave **109 against 143**, and one of the two raised a conflict the other never saw at all. `PRINCIPLES.md:184-191`; `Plan/learnings/extract-terms.md:397-414`; `.agents/skills/ingest/SKILL.md:44-51` [measured]

- **"A model at 0.66 is at the ceiling, not two thirds right, and one clearly above it is most likely fitted to a single reader. Report both difference lists by name: a miss is not automatically an error and an invention is not automatically wrong."** `PRINCIPLES.md:190-193` [claim]

- **P16 — measure per step, never globally**: "a model good at extraction can be bad at merging. Model choice comes from a benchmark against *that step's* fixture and *that step's* metric." `PRINCIPLES.md:180-182` [decided]

- **P17 — benchmark the real thing**: "score the actual program with the actual metric a real run is judged by." `PRINCIPLES.md:195-197` [decided]

- **P18 — one attempt measures nothing; the cache must be off. Evidence**: `nemotron-3.5-lightning:free` scored 1.00 in `lm-bench` when it worked but failed 1 of 3 attempts by emitting chain-of-thought (`"Here's a thinking process:"`) where JSON belonged — `AdapterParseError`; a single attempt would have shown a false 100%. `PRINCIPLES.md:199-204`; `Plan/quality/lm-bench_2026-09-16.md:73-79` [lesson]

- **P19 — assert non-empty output *and* assert the language. Evidence**: a reasoning model spent its whole token budget on reasoning and returned `content: None`, `finish_reason: length`, no error — nothing to catch without an explicit assertion; the free router returned correct German claims but an **English** `triage.summary`, invisible because `ingest_metric` checked only the claims' language. `PRINCIPLES.md:206-212`; `Plan/quality/lm-bench_2026-09-16.md:51-55,126-141` [lesson]

- **P15 — separate "never reached" from "answered badly". Evidence**: the first free-model sweep reported two models at 0% — neither had failed the task; one 404'd (listed in the catalogue but not actually served), one was restricted to "agentic harnesses only". `PRINCIPLES.md:170-175`; `Plan/quality/lm-bench_2026-09-16.md:22-27` [lesson]

- **`drg-kg`'s evaluation scorer, verified against this repo**: `drg.evaluation._prf(tp, fp, fn)` returns explicit zero guards — empty gold/empty pred → P0.0 R0.0 F1 0.0; empty gold/5 predicted → P0.0 R0.0 F1 0.0 (5 false positives); 10 gold/0 predicted → P0.0 R0.0 F1 0.0 (10 false negatives) — "it returns 0.0 where the retired pipeline's `coverage()` returned 1.0. That is the exact defect inverted." `Plan/concept/continuous-improvement_2026-09-17.md:106-123` [measured]

- **`drg-kg`'s scorer independently reproduces this project's own measured failure mode**: feeding `fold()` in as the key function to `drg.evaluation._score_sets` on a raw-vs-folded plural pair gives identical scores both ways (P0.50 R0.50 F1 0.50, missing `Grenzfeste`/`Kern-Welt` raw or `grenzfeste`/`kernwelt` folded) — "folding changed nothing on the plural pair. An outside scorer reproduces the project's own measured failure mode." `Plan/concept/continuous-improvement_2026-09-17.md:60-69` [measured]

- **`drg-kg`'s one hazard for this project, flagged rather than adopted uncritically**: document 5 added zero wiki pages *on purpose* (a brief supplying occurrences, not readings) — under `_score_sets` that run would score 0.0. "So the scorer belongs on the candidate list, where 'found nothing' really is a failure, and never on the pages, where 'promoted nothing' can be the correct outcome." `Plan/concept/continuous-improvement_2026-09-17.md:129-134` [claim]

- **`selftest.py` exists because nobody had ever seen the load-bearing checkers fail** — `quotes.py`, `read.py --find`, `fold()` are trusted by everything downstream, and "nobody had ever seen any of them fail," which is exactly the shape of the retired pipeline's `coverage()` (pinned at 1.0 with no gold passed; two live runs scored 0.987 and 0.967). `scripts/selftest.py:1-7`; `.agents/skills/ingest/SKILL.md:26-33` [lesson]

- **`selftest.py` totals 17 asserted cases**: 6 quotation cases + 4 citation cases (3 find-cases + 1 cross-line span) + 7 `fold()` pairs (4 must-not-merge + 3 must-merge). `scripts/selftest.py:39-85,139-152` [decided]

- **`judgements.jsonl` replay, current**: **68** total records, **7** mechanised (a rule now claims and still agrees with them), **0** disagreeing. `CLAUDE.md:207-209`; `python3 scripts/state.py --get judgements.total` [measured]

- **`judgements.py`'s first run found a live bug**: `fold()`'s own docstring claimed behaviour it did not have, and "the same false claim had been repeated in two other files." `Plan/concept/continuous-improvement_2026-09-17.md:16` [lesson]

- **What a green `judgements.py` replay does *not* prove**: `fold()` was correct the whole time `reconcile.py`'s own intra-list check excluded exact fold-equality, which made it report three worlds as six new terms — no recorded judgement covered the caller, so the ledger replayed green throughout. "A green replay says the recorded decisions still hold, not that the code around them is right." `CLAUDE.md:478-488` [lesson]

- **P23 — measure how much of itself a guard actually covers. Evidence, three cases in one session**: `state.py --prose` could not see 8 of its 49 markers (a regex forbade a newline between a number and its marker, so a wrapped number's marker matched nothing — `order.holds` among them — while the check printed "0 prose claims contradict the repository"); `capture.py` dropped every candidate over 40 characters (of 28 long lines, all 24 prose misses were already caught elsewhere, but 4 real terms were silently missed); the retired pipeline's `coverage()` returned 1.0 with no gold ever passed. `PRINCIPLES.md:109-120` [lesson]

- **`baseline.py`'s own selftest, 7 cases**: `unscored` (all-None outcomes), `fail` (below floor), `fail` (vetoed/canary broken regardless of score), `ok`, `warn` (partially scored), `warn` (trainset changed since the floor row), plus a `digest()` key-order-independence check. `scripts/baseline.py:117-140,163` [measured]


## DATA

- **The judgement ledger's growth is itself a dataset-quality story**: it grew from 17 labelled pairs (2026-09-17) → 26 (`NOW.md`, same day) → 36 (2026-09-23) → 44/49 (2026-09-24, documents 7–9) → **57 current** (`pairs.labelled`, documents 10–13 added more) — every growth step moved `fold()`'s measured accuracy (see MET). `Plan/runs/judgements.jsonl`; `python3 scripts/state.py --get pairs.labelled` [measured]

- **`Plan/trainsets/surface-pairs.jsonl` (the exported snapshot) is stale relative to the live ledger by design of the fix, not by accident**: directly observed to hold **36** rows (ids `J1`…`J45` with gaps) while `pairs.labelled` (from the ledger) is 57 — because `pairs.py` was changed to read `trainset.surface_pairs()` (the ledger) live and never the export file. `NOW.md:249-250`; `Plan/concept/dspy-toolchain_2026-09-23.md:24-33`; direct read of `Plan/trainsets/surface-pairs.jsonl` [measured]

- **Row shape observed directly** (`Plan/trainsets/surface-pairs.jsonl`), e.g. `{"id": "J1", "first": "Die Konstrukt-Stadt", "second": "Konstrukt-Stadt", "document": "guardians-und-kern-welten-konzept", "decision": "one-term", "rule": "strip leading der/die/das before folding", "features": ["near-match:intra-list", "german-article-prefix", "worldbuilding"]}`. Every row carries `id, first, second, document, decision, rule, features`. [measured]

- **`trainset.surface_pairs()`** is "the one-term-or-two task: the only task here with usable gold labels" — filters `judgements.records()` to `decision in {"one-term","two-terms"}` with exactly two `surfaces`. `scripts/trainset.py:52-68` [decided]

- **`trainset.blocked()` names exactly two tasks that cannot be trained yet, with reasons rather than a silent gap**: "extract candidate terms from a document" (usable count = total `03-candidates.md` files minus those whose first 300 chars mention "reconstruct" — because "every candidate list so far is a reconstruction written after the counts, not while reading" except from document 5 on); "is this a conflict" (0 usable of N conflicts+1 false positive — "conflict detection is deliberately never mechanised"). `scripts/trainset.py:97-114` [decided]

- **`trainset.gold_candidate_lists` moved from 0 (2026-09-17) to 2 (current)** — the precondition for ever training extraction, and it "goes up as a byproduct of doing documents rather than as a separate project." `Plan/concept/trainset-and-the-baseline_2026-09-17.md:88-90`; `python3 scripts/state.py --get trainset.gold_candidate_lists` [measured]

- **`Plan/runs/README.md`'s six-artifact shape per document**: `01-profile.txt` (structure, script), `02-probes.txt` (export damage/inflection/substrings, script), `03-candidates.md` (written while reading, before any counting — "the only artifact a program cannot produce" — a person), `04-counts.txt` (occurrences, script), `05-verify.txt` (every number that went into prose, re-checked), `run.md` (timings, what's missing). `Plan/runs/README.md:10-18` [decided]

- **The first four documents' `03-candidates.md` are reconstructions and "cannot serve as a gold set"** — written after the census rather than while reading, and marked as such; `01`/`02`/`04` are deterministic and were re-run so those are genuine. `Plan/runs/README.md:28-41` [lesson]

- **`Plan/runs/CONVENTIONS.md`'s JSON contract**: every step object requires `document`, `drive_id` (**never typed, always copied from the manifest**), `step`, `at`, `by`; no fixed schema beyond that (P4 — no structure without instances). `Plan/runs/CONVENTIONS.md:11-22` [decided]

- **The `reconcile` JSON object** (the one this whole incremental design rests on): `state_before`/`state_after` each `{pages, conflicts}`, `new_terms`, `new_readings`, `new_surfaces`, `new_conflicts`, `minutes`. `Plan/runs/CONVENTIONS.md:41-57` [decided]

- **Entity lists, current**: **4** lists exist (`Plan/entities/<slug>.md`), **3** pass verification as readings (≥90% cited lines hold), **317 of 317** rows verify (100%) — "by construction, since code wrote every line (revision 3)". `CLAUDE.md`; `python3 scripts/state.py --get entities.rows_verified` [measured]

- **Entity-list pilot, revision 1 (4 documents)**: 280 of 374 rows (74.9%) cited a line holding the entity; no list reached the 90% "reading" threshold. Of 94 failures: 39 wrote a form the document never contains, 29 cited the wrong line, 26 were 1–3 lines off. One reader stopped at line 1200 of 2498 and reported comprehensive coverage. `Plan/concept/entity-lists_2026-09-23.md:81-84` [measured]

- **Entity-list pilot F1 against the two reader-written gold lists that exist**: `roman-lokalitaeten` **0.67** — "at the human ceiling"; `aegis-subplots` **0.13** — "the model took the document's research vocabulary (Kybernetik, Spieltheorie) where the reader took its world." `Plan/concept/entity-lists_2026-09-23.md:86-88` [measured]

- **Revision 3 re-pilot, same 4 slugs, 2026-09-23**: `aegis-subplots-kapitelweise-system-exploration-docx` — 70 placed, 14 refused, F1 0.28→**0.25**; `kohaerenz-protokoll` — 82 placed, 13 refused, "not a reading — one line unread [of 2498]"; `ki-agenten-kohaerenz-und-prompt-generierung` — 68 placed, 22 refused; `roman-lokalitaeten-konzept-und-ausarbeitung` — 97 placed, 0 refused, F1 0.67→**0.69**. `NOW.md:268-273` [measured]

- **Revision 3's structural fix, and why it worked**: the reader returns **names only** into `Plan/entities/names/<slug>.json`; `entities.py place` finds each name's first whole-word line and refuses any name the document does not contain word-for-word — "every row verifies because no row was typed. The refusals are the forms revision 2 would have written anyway." `NOW.md:263-266,275-276` [lesson]

- **Cost of the 4-document pilot**: "423,531 subagent tokens and about 75 s wall-clock, run in parallel as four Haiku agents with the workflow's prompt verbatim, not through the Workflow tool." `NOW.md:295-297` [measured]

- **Full-corpus entity-list run, priced but not started**: at the piloted rate, 342 more documents ≈ **36M tokens**, scaled by length rather than count — "say what the full run costs before starting it, and ask." `NOW.md:335-337` [claim]

- **`entities.py verify()`'s reading threshold**: `READING = 0.9` — a list under 90% verified is a reconstruction and `matrix` leaves it out. `scripts/entities.py:69` [decided]

- **A checker bug, not a reader bug, was hiding behind "reconstruction" labels**: `quotes.normalise` dropped a 1–2 digit number glued to a word (footnote debris), so `(KW2),` became `(KW),` while the searched name stayed `KW2` — a name ending in a digit could never verify. Revision 2's gazetteer lost `KW2`–`KW4`, `Kern-Welt 1`–`4` and `Silent Hill 2` to it and blamed the reader. `entities.py` now asks one shared question (`holds()`) for placing and verifying. `NOW.md:285-289` [lesson]

- **`Plan/runs/jev/` shape, observed directly**: two document trials exist — `aegis-subplots-kapitelweise-system-exploration-docx/` and `roman-lokalitaeten-konzept-und-ausarbeitung/` — each with `calls/<hash>.json` (32 and 34 cached request/response files respectively), `list.md`, `stats.json`. [measured]

- **`Plan/runs/jev/*/stats.json` exact numbers**: `aegis-subplots…` — 619 lines, 2044 candidates, 32 requests, 0 unreached, 2044 judged, 423 "yes" (p≥0.5), 100 kept (capped), 401,306 input / 36,607 output tokens, 5.7s wall, model `jev-1.13.0`. `roman-lokalitaeten…` — 630 lines, 2191 candidates, 34 requests, 428 yes, 100 kept, 421,786 input / 39,234 output tokens, wall 0.0s (a `--replay` run served from cache). [measured]

- **`Plan/runs/jev/*/list.md` top rows show a known failure mode directly**: on `aegis-subplots`, cited authors from footnotes rank above world terms — `Sartre` p=0.98, `Camus` p=0.98, `Foucault` p=0.97, `Hegel` p=0.97, `Ryle` p=0.96 — beside `AEGIS` p=0.99, `Kael` p=0.98, `LogOS` p=0.97, `Mnemosyne` p=0.96. [measured]

- **`Plan/runs/bilingual/` shape, observed directly**: `stated.jsonl`, `entities.jsonl`, `propose.jsonl`, `pairs.jsonl` at the top level, plus a `calls/{jev,openrouter}/` cache holding **1,114** files total (counted directly). [measured]

- **`Plan/quality/lm-candidates.txt`**: the model list fed to `lm_bench.py`, fetched from `openrouter.ai/api/v1/models` on 2026-09-16 — "444 models, 24 of them free… Model ids drift — re-fetch before trusting this list." `Plan/quality/lm-candidates.txt:1-9` [measured]

- **`baselines.jsonl` currently holds 12 rows total**: 7 `graphrag-retrieval` rows (`seeds`/`ppr`/`ppr+gloss` recorded three separate times as the case count grew: n=9, n=10, n=14) and 3 `one-term-or-two rule:fold` rows (n=36, n=44, n=49) plus the two `ppr`/`ppr+gloss` rows at n=9. [measured]


## RLM

- **`rlm_ingest.py` combines three pieces**: `dspy_skills.SkillManager` (loads `.agents/skills/`, renders the `<available_skills>` block from the `description` field alone, `activate()` reads one skill's full `SKILL.md` — the model gets the same instructions a person here gets, from the same file); `dspy.RLM` (a sandboxed Python REPL — "a census is counting, and a model that can *compute* over the text does not have to be believed about how many times a word occurs"); `scripts/read.py`'s `NNN| `-prefixed document text. `scripts/rlm_ingest.py:1-16` [decided]

- **Why the line prefix is mandatory, not cosmetic**: "left to count for itself the model reported 690 lines where this project counts 691 — the two-line-bases trap, frontmatter against file." `scripts/rlm_ingest.py:14-16` [lesson]

- **The founding failure this whole script is built around**: the first `dspy.RLM` run ran out of REPL budget before finishing the document, and its own reasoning trace said, verbatim: "*We have full document variable inaccessible except history outputs. Need leverage all shown snippets … We can reconstruct from outputs.*" It was about to hand back a reconstruction as a reading, "and from a model it is **invisible**: the list looks the same." It only failed to land because the answer arrived in `reasoning_content` with `text: None`, which DSPy's adapter rejected — "that is luck, not a safeguard." `scripts/rlm_ingest.py:18-31`; `Plan/learnings/extract-terms.md:366-384` [lesson]

- **The rule that failure produced**: every candidate must come back as `- term ^[Lnn]`, and every cited line is checked against the document by the same comparison `quotes.py` uses (`verified()`); a candidate whose cited line does not contain it is reported as unverified rather than dropped; a mostly-unverified list names itself `PARTLY RECONSTRUCTED` in its header, a field `state.py` reads. `scripts/rlm_ingest.py:32-37,205-217,262-266` [decided]

- **Output goes to `03-candidates-rlm.md`, never `03-candidates.md`** — "the gold list is written by a reader while reading; a model's list is the thing gold is used to score, and the two must never be able to become each other." `scripts/rlm_ingest.py:40-43`; `.agents/skills/ingest/SKILL.md:263-268` [decided]

- **Four changes made 2026-09-23, from reading nine DSPy repositories against this one**: (1) cache off; (2) `max_llm_calls` set explicitly and `--sub-model` may name a cheaper `sub_lm`, because "the first run ran out of REPL budget and began reconstructing from scrollback"; (3) `find_line`/`count` passed to the REPL as tools, so the model *asks* for a line the way a person here does (P26, enforced inside the sandbox); (4) a second verification tier, "reach" — a list that never cites past 90% of the document "did not read to the end, whatever it says". `scripts/rlm_ingest.py:48-66` [decided]

- **`tools_for(slug)`**: `find_line(words)` returns `^[Lnn]` hits (up to 20) via `read.locate`, or `"NOT FOUND. nearest: ..."` via `read.nearest`; `count(term)` counts lines containing the term via `quotes.normalise` — both reuse the project's own comparison, so "a line the model gets from `find_line` passes the verification below by construction." `scripts/rlm_ingest.py:110-135` [decided]

- **`reach(slug, good_lines)`**: furthest verified-citation line, its share of the document's line span, and how many of 10 "tenths" of the document the citations touch. `scripts/rlm_ingest.py:138-147` [decided]

- **Model construction for a real run**: `dspy.LM(model, api_key=…, api_base="https://openrouter.ai/api/v1", max_tokens=16000, temperature=0, cache=False)`, optional `sub_lm` at `max_tokens=8000`; `dspy.RLM("document: str, task: str -> candidates: str", max_iters=iters, max_llm_calls=calls, tools=tools_for(slug), sub_lm=sub)`. `scripts/rlm_ingest.py:220-233` [decided]

- **`--approval` is a hard `SystemExit` gate**, naming that this "sends a whole corpus document to OpenRouter." `scripts/rlm_ingest.py:223-225` [decided]

- **"Reading" vs "PARTLY RECONSTRUCTED" threshold**: verified-share ≥0.9 **and** no `UNREAD` lines **and** no uncited candidates **and** `reach` share ≥0.9 — otherwise every list is downgraded regardless of how plausible it looks. `scripts/rlm_ingest.py:262-266` [decided]

- **`rlm_ingest.py score`** compares a model's `03-candidates-rlm.md` against a reader's `03-candidates.md` through `drg.evaluation._runner._score_sets` with `fold()` as the key function, printing precision/recall/F1 and the two difference-lists by name, with the P27 human-ceiling caveat printed inline ("Two independent readings of one document differed by 109 against 143 candidates"). `scripts/rlm_ingest.py:295-322` [decided]

- **`rlm_ingest.py --selftest`, 4 offline cases (no model, no key)**: `find_line` locates a real line by its own words; `find_line` refuses ("NOT FOUND") for words the document does not contain; `count` finds at least one `AEGIS` in a document about AEGIS; `reach` correctly separates an early-only citation set (share <0.9) from a full-coverage one (share ≥0.99, all 10 tenths touched). `scripts/rlm_ingest.py:344-367` [measured]

- **First live RLM measurement against the corpus (2026-09-17), "the trap"**: the census for `guardians-und-kern-welten-konzept` records that the document says "die vier zentralen Hüter" (^L15) and "die vier Guardian/Welt-Paare" (^L135) yet **names five Guardians**, reconciled only in one parenthetical (^L96: "Kairos und Sophia werden als zwei distinkte, aber komplementäre Guardians dargestellt"). Ground truth = 5. `Plan/concept/rlm-measured-on-the-trap_2026-09-17.md:19-30` [measured]

- **Results on that trap**: `dspy.RLM` (haiku via the `claude -p` bridge, `max_iters=4`) → **4/5, missed Sophia**; direct-prompt `nex-agi/nex-n2.5-pro:free` (whole document in context) → **5/5**; direct-prompt `nex-agi/nex-n2.5-mini:free` → **5/5**; direct-prompt `nvidia/nemotron-3.5-lightning:free` → **3/5**, missed Kairos and Sophia (cut off mid-reasoning by a 120-token test cap). "Four runs, two right. And both failures are partly mine." `Plan/concept/rlm-measured-on-the-trap_2026-09-17.md:34-43` [measured]

- **"Eleven of fifteen free models did not answer at all — 404, 429, 403, or a response with no `choices`. The free tier is not a benchmark surface."** `Plan/concept/rlm-measured-on-the-trap_2026-09-17.md:45-46` [lesson]

- **The interesting finding was structural, not about model capability**: "the RLM reproduced the document's own off-by-one" — a reader who trusts the prose gets four, same as the RLM did. The census reached five by cross-checking **three** independent signals a chunk-and-summarise pass has no reason to connect: the two "vier" statements, the reconciling parenthetical at L96, and a purely structural artifact — a duplicated `### A.` heading (^L98 "A. Guardian Kairos", ^L110 "A. Guardian Sophia") both under one section. `Plan/concept/rlm-measured-on-the-trap_2026-09-17.md:50-63` [claim]

- **What this measurement does *not* argue**: "nothing here says an LM should be kept out of this pipeline. Two models got it right in one shot… the *count* questions are the risky ones, and a verification pass for them should check structure rather than re-read prose." `Plan/concept/rlm-measured-on-the-trap_2026-09-17.md:72-76` [claim]

- **Cost note**: "the `claude -p` bridge re-creates prompt cache per process — a trivial call measured **$0.078**. An RLM loop is many such calls. Budget before looping." `Plan/concept/rlm-measured-on-the-trap_2026-09-17.md:78-81` [measured]

- **Setup dependencies measured for that first run**: Deno (the Pyodide sandbox `dspy.RLM` needs) via `Legacy/scripts/setup_dspy.sh --deno`, "does not survive a container"; DSPy 3.3.1 in `.venv-dspy/`; the key-less LM bridge `Legacy/tools/kpwiki/local_lm.py` (the `Hmbown/dspy-local` pattern, already built and "parked in `Legacy/`"). `Plan/concept/rlm-measured-on-the-trap_2026-09-17.md:9-17` [measured]

- **What the generic RLM gives a model** (read from `netzkontrast/rlm`'s own `prompts.py`, MIT, `pip install rlms`): `context` as a variable (str/list[str]), `llm_query(prompt)`, `llm_query_batched(prompts)`, `rlm_query(prompt)` (a **recursive** sub-RLM), `SHOW_VARS()`, and an `answer={"content":…, "ready": False}` termination protocol. "REPL outputs over ~20K characters are truncated" — the environment itself enforces never printing the whole corpus, not merely instructing against it. `Plan/concept/rlm-the-real-one_2026-09-17.md:8-25` [claim, about the external `rlm` package, ported as design guidance]

- **This project's self-comparison against that shape**: `context` as a variable ✓ (`Plan/derived/*.json`, `Wiki/index.json`); never-print-the-payload ✓, and **structurally**: `corpus.py` "has no code path that emits a body"; `answer`/`ready` ✓ by another name (census/note/page); `llm_query`/`llm_query_batched`/`rlm_query` — **not built**; the model writing its own code — **not built, deliberately, for now**. "So: the environment half is built and the language-model half is not. Every query here is a program someone wrote, replayable and checkable against `judgements.jsonl`." `Plan/concept/rlm-the-real-one_2026-09-17.md:32-45` [decided]

- **The one premise of generic RLM this project explicitly does NOT act on at document scale**: "RLM's whole premise is that the context is too large to read, so it must be sliced and delegated. At the document level here, that premise is false and acting on it would break the method" — a source document is ~6,700 words, and the census rule requires a full read before any counting, since "roughly half of the twenty-one special cases found so far are invisible to any pattern a slicing strategy would start from." `Plan/concept/rlm-the-real-one_2026-09-17.md:51-61` [decided]

- **Where a batched/RLM-style loop *would* fit, sized but unbuilt**: `corpus.py plan` computes "AEGIS — 315 documents, 14,676,980 chars / 41 sub-calls at 400,000 chars each" — a real cost estimate, produced without reading anything, purely from the surface index and manifest sizes. `Plan/concept/rlm-the-real-one_2026-09-17.md:67-79` [measured]

- **Honest cost caveat on wiring it**: "the relevant price is the retired pipeline's **$2.79 and 18 minutes per document** — 41 sub-calls over 14.7M chars is a different shape, but it is not free, and the project has no measured number for it." `Plan/concept/rlm-the-real-one_2026-09-17.md:89-96` [claim]

- **Explicit gate on any corpus-scale RLM wiring**: "None of it is worth doing before the hand pass finishes. The four documents are producing the rules the sub-calls would need to be given, and a sub-call sent without them would reproduce the pipeline that already failed — 19 quoting defects in 141 claims, because nobody had written down what a quote had to be." `Plan/concept/rlm-the-real-one_2026-09-17.md:98-101` [decided]

- **The one RLM idea explicitly stolen already**: `SHOW_VARS()` — "the environment tells the model what it has. Here, nothing tells a reader what the derived cache already knows… A reader wanting to know whether a question is already answered has to read the code." (Not yet built, named as worth stealing.) `Plan/concept/rlm-the-real-one_2026-09-17.md:103-108` [claim]

- **Banlist of rejected RLM-adjacent ideas, kept so they are not re-proposed**: subagent fan-out to move document bytes ("moves the context leak, does not remove it"); full re-comparison of all censuses per document (O(n²), each superseded the last); merging readings on a term page ("destroys which source said what — the wiki's only job"); mechanising conflict detection ("reproduces the `Zero-Trust` false conflict"); a fixed enum of document kinds (decision 004). `Plan/concept/rlm-transfer_2026-09-17.md:32-42` [decided]

- **RLM idea D explicitly rejected**: making the unit of work a *query* (reconcile one term across all documents) rather than a document — "a term-first pass reads many documents through one lens, which is exactly the contamination the census exists to prevent. The unit stays the document." `Plan/concept/rlm-transfer_2026-09-17.md:63-68` [decided]

- **RLM idea E (corpus-scale term recursion) not built, not yet needed**: "What does the corpus say about AEGIS?" → 226 documents is "precisely the RLM case," but "nothing is asking corpus-scale questions of a term yet" — `corpus.py where AEGIS` already returns the document list without the documents, so the shape is enabled but unused. `Plan/concept/rlm-transfer_2026-09-17.md:70-76` [decided]

- **Building `corpus.py` (a non-model, RLM-inspired query layer) immediately found a real defect**: 26 of the then-409 landed documents had no frontmatter at all, and "every ad-hoc count in this session used `lines[9:]`, which silently swallowed nine lines of content in those 26 documents" — the exact cause of a `Julia`-count that disagreed by one document (26 vs 27) between two counting passes. `Plan/concept/rlm-transfer_2026-09-17.md:79-88` [lesson]

- **The generalized lesson from that**: "a heredoc encodes an assumption once and nobody audits it; a tool encodes it once and everyone inherits the audit." `Plan/concept/rlm-transfer_2026-09-17.md:94-96` [claim]

- **Two-views-of-a-count trap, generalized as judgement `J12`**: the surface index counts a compound as one token (`Kael-Julia-Bindung` does not add to `Kael`); a `\bKael\b` regex over raw text counts the head inside every compound too — **293 documents (regex) vs. 287 (index)**. "Neither is wrong… the danger is quoting them as the same fact." `Plan/concept/rules-as-the-project_2026-09-17.md:99-110` [measured]

- **`entities.py search` reproduces this exact split deliberately, for `Guardian`**: "`Guardian` is 448 in one and 334 in the other, and both are right about different questions" — `entities.py` counts hyphen compounds too (`\bGuardian\b`-style: 448), `corpus.py count` treats a compound as one token (334). `scripts/entities.py:19-37` [measured]


## RAG

- **`graphrag.py`'s 4-step retrieval pipeline**: (1) **seed** — pages whose folded surfaces occur in the folded question, via `fold()`, no embeddings; (2) **spread** — personalized PageRank over `graph.py`'s typed edges (`DAMPING=0.85`, `ITERATIONS=40`, edge weights `links 1.0, contests 0.8, raised_by 0.8, concerns 0.5, reads 0.3, cites 0.3, asks 0.3`); (3) **select** — MMR with a relevance floor over verified quotations only; (4) **return** — quotations verbatim with `doc:line`, the touching conflicts/questions, and the documents reached — "**No synthesis** (P13)". `scripts/graphrag.py:1-26,62-73` [decided]

- **MMR parameters**: `BUDGET=8`, `DIVERSITY_LAMBDA=0.65` ("kp_canon_retriever's measured default, above upstream's 0.5"), `MIN_RELEVANCE=0.15` (the floor; 0.0 reproduces unguarded MMR), `MIN_SURFACE=4` ("a shorter fold is a substring of far too much"). `scripts/graphrag.py:66-70` [decided]

- **Why the relevance floor exists, ported from `dspy-agent-skills`' `kp_canon_retriever.py` (itself from `dspy-refrag`, MIT)**: "measured there, plain MMR picks an unrelated passage over a relevant near-duplicate at every λ from 0.5 to 0.8." `scripts/graphrag.py:16-21`; `Plan/concept/graphrag_2026-09-23.md:77-80` [claim]

- **The exact fixture that reproduces that defect, and its guarded fix, both asserted in `selftest()`**: relevance `[0.9, 0.88, 0.6, 0.0]`, similarity `{(0,1):0.97, (0,2):0.5, (1,2):0.5}` — unguarded (`min_relevance=0.0`) may pick index 3, the unrelated item; guarded, budget 2, picks exactly `[0, 2]` (the near-duplicate plus the relevant-distinct one). `scripts/graphrag.py:369-383` [measured]

- **The one model step, `--answer`**: the model sees numbered quotations and returns only `chosen: list[int]` and `gaps: list[str]` — it never types a quotation; code prints the quotations those numbers point at ("a model that cannot type a quotation cannot misquote one" — P26 applied to answering). Invalid numbers are dropped and named. Runs through `lmrun.call`, so cache is off, the call is recorded, and a real run needs `--approval`. `scripts/graphrag.py:295-328` [decided]

- **`graphrag.py selftest`, 9 asserted cases**: the MMR defect reproduced unguarded / fixed guarded (2 cases); a bench case cannot retrieve itself once its own node is removed; a nonsense query (`"xyzzy quux"`) seeds and retrieves nothing; an English question seeds nothing **without** `--gloss`; the same English question reaches the German page **with** `ppr+gloss`; an ambiguous gloss (`Ordnung` → two pages) is excluded; a named entity in an **unread** document is still routed to, with its line; a list that fails `entities.py verify()` (a "reconstruction") is excluded from those routes. `scripts/graphrag.py:369-409,417-418` [measured]

- **`bench()` methodology**: for each labelled case (a question's `raised_by` pages, a conflict's `pages`) the case's own node is removed from the graph first via `without()` so it cannot retrieve itself; scored for 3 methods — `seeds`, `ppr`, `ppr+gloss`. `scripts/graphrag.py:333-366` [decided]

- **`graph.py` derives a typed KG purely from what pages already state** — nothing extracted or inferred by a model: node types `term:`, `doc:`, `conflict:`, `question:`; edge types `links` ([[…]] — the only term→term edge), `reads` (`ingested:`), `cites` (`^[slug.md:Lnn]`, every cited line), `contests`, `raised_by`, `asks`, `concerns` — **every edge carries `via: file:line`**. `scripts/graph.py:1-30` [decided]

- **Graph counts, current**: **122** nodes, **1161** edges; evidence layer **1219** quotations, **1104** verified against their line by `quotes.verdict`. `CLAUDE.md:409-416`; `python3 scripts/state.py --get graph.edges` [measured]

- **Building the graph exposed a real disagreement between two independent implementations of "does this quotation resolve"**: the graph's own first quotation-pairing found **14 unresolved** where `quotes.py` found **4** — unified into a shared `quotes.pairs`/`quotes.verdict` that both now call; "`quotes.py`'s own numbers did not change." `NOW.md:251-254` [lesson]

- **`graph.py --selftest`, 5 asserted checks**: the real graph already passes `check()` with zero problems (or the failure is surfaced); a fixture edge to a missing page IS reported; a fixture document with no manifest row IS reported; proposal-layer edge types (`names`, `folds_to`) never leak into `build()`'s core edge set; `graph.py`'s own `links`-edge count matches `relations.py`'s independently-computed count exactly. `scripts/graph.py:303-325` [measured]

- **`graph.proposals()` — a layer kept explicitly apart from the checked graph**, two kinds: **entities** (from `Plan/entities/<slug>.md` lists that pass `entities.py verify()` as a reading — "a model chose the name, code placed the line"); **glosses** (from `Plan/runs/bilingual/stated.jsonl`, only the `A (B)` shape, written in ≥`GLOSS_MIN_DOCS=2` documents, exactly one side a page surface — "the relation is **unjudged**": `Kael (Host)` is a role, `Grenzfeste (Cerberus)` a place-and-its-guardian). `scripts/graph.py:204-229` [decided]

- **Gloss ambiguity is dropped by rule**: a surface glossing two different pages (`Ordnung`→Kohärenz and AEGIS; `Anteile`→Alters and Personas) is excluded — "says nothing about which." `scripts/graph.py:281-286` [decided]

- **Proposal counts, current**: **226** entities from lists that verify as readings, **28** of those fold to a wiki-page surface; **182** stated glosses routing to exactly one page. `CLAUDE.md:448-452`; `python3 scripts/state.py --get proposals.entities` [measured]

- **qmd has 1,047 files in its index, every one markdown, zero JSON** — meaning `Plan/runs/judgements.jsonl` and every `reconcile.json` were **invisible to every search**, "which is precisely backwards: they are the densest record of what was decided." Fixed by having `judgements.py` render `Plan/runs/judgements.md` on every run so the search-visible copy cannot lag the source of truth. `Plan/concept/skills_2026-09-17.md:96-102`; `scripts/judgements.py:64-76` [lesson]

- **qmd local model stack (CPU-only in this container)**: `embed = embeddinggemma-300M-Q8_0` (~300MB — "qmd's own default and the small one," vs. `Qwen3-Embedding-0.6B` at ~640MB), `rerank = Qwen3-Reranker-0.6B-Q8_0` (~610MB), `generate = qmd-query-expansion-1.7B-q4_k_m` (~1.2GB); `qmd doctor` reports "four math cores and no GPU". `.agents/skills/qmd/references/setup.md:30-33,51-64`; `.agents/skills/qmd/SKILL.md:128-131` [measured]

- **Three qmd search commands, timed on this corpus after embeddings finished, on queries never asked before**: `search` (BM25, no model) **0.22–0.24s**; `vsearch` (vectors only) **12.7s**; `query` (1.7B expansion model + both retrieval legs + 0.6B reranker, CPU) **2m41s**. "`query` became eleven times slower once embeddings existed" (14.5s before the vector leg ran, 2m41s once it did) — "the 0.2s came from the index's `llm_cache`… the documented example phrase had been asked before." `.agents/skills/qmd/SKILL.md:117-133`; `Plan/concept/skills_2026-09-17.md:60-68` [measured]

- **Before that measurement, `qmd` had **0 of 464 (later 465) documents embedded** — the embedding model had simply never been downloaded, and `vsearch` silently returned `"No results found"` (exit 0) instead of an error. `Plan/concept/skills_2026-09-17.md:63-64`; `.agents/skills/qmd/SKILL.md:139-141` [lesson]

- **A "search result never becomes a number" — the load-bearing qmd rule, with its own measurement**: `Kernwelt` occurs in **144 of 346** (then-current) landed documents, but a 40-hit search list is not a census of that — "measured, the line that defines `KW1` is not in the top forty, because BM25 favours short, early chunks" (top hits sat at lines 3, 26, 25, 16, 11 of their documents, not the line-152 definition). `.agents/skills/qmd/SKILL.md:20-24`; `CLAUDE.md` *Searching the corpus* [measured]

- **Query language must match the collection's own language, measured**: `"Plural Flexion Term Grenze"` (German) against the `decisions` collection → **0 hits**; `"plural inflection term boundary"` (English) → **1 hit at 0.92**, the right one — `decisions`/`plan` are English (reconciliation records, judgements, concept notes), `sources`/`census`/`notes` are German. `.agents/skills/qmd/SKILL.md:35-44` [measured]

- **`vsearch` does earn its cost on paraphrase without shared words**: "wer bewacht welche Welt" against `wiki` returns the Personas page, the Guardians/Kern-Welten reconciliation, and the Möglichkeits-Garten — "none of which contains those words. BM25 cannot do that at any price." 12.7s. `.agents/skills/qmd/SKILL.md:128-132` [measured]

- **Even fully embedded, a hard case stayed hard**: "welcher Guardian gehört zu Kernwelt 1" via `vsearch` returns a *different, wrong* document; the fully structured `intent:`/`lex:`/`vec:` query took **3m14s** and scored worse than plain `search` — "the reason is the chunk… For a specific line in a long document the answer is `grep -n`." `.agents/skills/qmd/SKILL.md:222-233` [lesson]

- **`qmd cleanup` found 126 inactive document records still in the index after `dedupe.py` folded away the duplicate exports** — and cleanup also clears the `llm_cache`, "which is what makes a repeated `query` fast — so a cleanup makes the next one slow again." `.agents/skills/qmd/SKILL.md:243-246` [measured]

- **`qmd bench` (a 4-backend IR evaluation harness — `bm25`/`vector`/`hybrid`/`full`, reporting `precision@k, recall, recall@1/3/5, mrr, f1, latency_ms`) has never been run on this corpus**; the fixture is nearly free because "every `Wiki/questions/` page and conflict record already contain a sentence of the form 'a search across all N documents finds this, in `<slug>`'" — a relevance label the work produced incidentally. `NOW.md:156-162`; `Plan/concept/skills_2026-09-17.md:35-52,69-83` [decided]

- **Nothing in the wiki-building pipeline depends on qmd** — `reconcile.py` answers "by lookup against `Wiki/index.json`" so cost stays `O(census) + O(judgement)`; a qmd hit only "finds candidates to read; it decides nothing." `CLAUDE.md` *Searching the corpus* [decided]

- **`qmd mcp` (an MCP server exposing `query`/`get`/`multi_get`/`status`) is explicitly decided against**, on the author's call: "the CLI is enough, and a skill that documents every step is clearer written against commands a person can also type… a skill whose job is to describe every step should name commands, not tool calls. A reader can type a command, check its output and disagree with it; an MCP tool call is invisible in exactly the way this project's process artifacts exist to prevent." `Plan/concept/skills_2026-09-17.md:114-126` [decided]

- **`qmd context add` (human-written per-collection summaries) was measured to do less than its name suggests**: "the context never reaches the reranking model. It is stored per collection, attached to results as metadata and printed above `get` output. It is documentation for a reader, not an input to search." `Plan/concept/skills_2026-09-17.md:118-121` [measured]

- **`graphrag.py`'s exact CLI surface**: `python3 scripts/graphrag.py ask "<question>" [--gloss] [--budget N] [--unchecked] [--json]`; `python3 scripts/graphrag.py bench [--k 8] [--record]`; `python3 scripts/graphrag.py selftest`; the one model-calling form is `.venv-dspy/bin/python scripts/graphrag.py ask "…" --answer [--model M --approval "…" | --dry-run]` — `--answer` without either `--model`+`--approval` or `--dry-run` prints a usage error and exits 2. `scripts/graphrag.py:40-46,449-459` [decided]

- **Embedding-context sizing, from `qmd`'s own measurement (not this corpus)**: the small embedding model (≲350MB) is "measured by qmd at ~2048 tokens of embedding context"; the larger `Qwen3-Embedding-0.6B-Q8` (~640MB) needs "roughly 1190 MB per batch." `.agents/skills/qmd/references/commands.md:100-104` [claim, from qmd's own docs]


## JEV

- **What Jev is, as this repo's `typesafe` skill defines it**: `POST https://api.typesafe.ai/v1/systemone` takes a `state` (string or any JSON) and a map of named typed questions — `Noul` (`.noul` ∈[0,1], "0.5 means 'as likely yes as no', not 'medium'"), `Choice` (one of a closed set, ≤255 options, "reliably up to ~240"), `Score` (≤10 ordered levels, "eleven is a server error") — and returns probabilities, not text. "The model judges; code decides." `.agents/skills/typesafe/SKILL.md:16-32` [decided]

- **`jev-latest` resolved to `jev-1.13.0` here on 2026-09-23**; TypeSafe's own cookbooks were run on `jev-1.12` — "record `response.model` with every result." `.agents/skills/typesafe/SKILL.md:125-126` [measured]

- **Two scripts call Jev in this repository**: `scripts/jev_entities.py` (a test of entity candidates on 2 documents) and `scripts/bilingual.py` (the corpus-wide German–English mapping — a Noul per surface, then a Choice per pair). "Nothing in the [wiki] pipeline calls Jev." `.agents/skills/typesafe/SKILL.md:167-172` [decided]

- **`jev_entities.py`'s mechanical candidate extraction** (never a model, so a candidate's line "cannot be wrong" — P26): every capitalised/digit-bearing token, hyphen compound, and bold/`code`/first-table-cell span up to 5 words, each with its first file line and count. Windowed into `WINDOW=40`-line chunks (`L052| …` format), all candidates of a window asked in one request (`MAX_Q=80`, split if more), `WORKERS=6` ("the public endpoint rate-limits above about eight"), output capped at `CAP=100` rows ("the size the Haiku lists aim at"), ranked by Jev probability then by count. `scripts/jev_entities.py:1-19,34-41` [decided]

- **`jev_entities.py` measured runs (jev-1.13.0)**: `aegis-subplots-kapitelweise-system-exploration-docx` — 619 lines, **2,044** candidates, 32 requests, **423** answered "yes" (p≥0.5), 100 kept, 401,306 input / 36,607 output tokens, **5.7s** wall. `roman-lokalitaeten-konzept-und-ausarbeitung` — 630 lines, **2,191** candidates, 34 requests, **428** yes, 100 kept, 421,786 input / 39,234 output tokens. `Plan/runs/jev/*/stats.json` [measured]

- **Jev vs. the Haiku-reader pilot, the exact comparison table** (`NOW.md`): Haiku rev 1/2 — gazetteer F1 **0.67**, `aegis-subplots` F1 **0.28**, 85–95% lines right, ~2 min/doc, ~110k tokens/doc. Jev, top-100 by p — gazetteer F1 **0.47**, `aegis-subplots` F1 **0.10**, 99% lines right "by code" (lines are placed by code, so only the yes/no judgement is scored), **6s**, ~410k tokens. Every script candidate with no Jev filter at all — gazetteer F1 **0.09**, `aegis-subplots` F1 **0.04**. `NOW.md:305-309` [measured]

- **"Faster by about 20×, cheaper by about 4× in money, not in tokens"** — Jev $0.042/M input tokens with free output (OpenRouter, 2026-09-23) vs. Haiku's $1/$5; token count is high because "each of ~2,100 questions per document repeats its wording; the state is paid once per window." `NOW.md:311-315` [measured]

- **The candidate-script's recall ceiling is the real bottleneck, not Jev's judgement**: 0.80 (gazetteer) and 0.63 (`aegis-subplots`) — it "misses multi-word names with a space in them (`Externe Ebene`, `Kern-Welt 1`) and splits none of the slashed forms (`Juna/V`). That ceiling is code's, and fixable." `NOW.md:316-318` [lesson]

- **Jev said yes to ~20% of candidates and ranked cited authors highest** (`Sartre`, `Camus`, `Chinese_room` from footnote URLs) on `aegis-subplots` — "it did what the question asked… the definition decides the list, not the model." `NOW.md:319-323` [lesson]

- **Near-duplicates crowd Jev's top-100** (`Neuromancer`, `"Neuromancer (Roman, 1984)"`) — "folding parentheticals is code, not judgement." `NOW.md:324-325` [claim]

- **Overall verdict on Jev-for-entities**: "Jev is not a replacement for a reader here, but it is a cheap filter behind a better candidate script. The gold lists are noisy too — each carries a reader's notes as `- ` lines, which no list can match." `NOW.md:327-329` [claim]

- **The three-question gate every proposed Jev placement must pass** (`jev-in-ingestion_2026-09-23.md`): (1) does its answer become part of the record, or only direct attention? — a page/link/conflict is record, a reading order is attention, "Jev may only direct attention"; (2) is there a labelled set to measure it against before it is trusted? (P3/P16/P17/P27); (3) can it run offline? (P5 — every call cached on first run, replayed after). `Plan/concept/jev-in-ingestion_2026-09-23.md:22-34` [decided]

- **Where Jev may explicitly never go, listed to avoid re-arguing it**: `03-candidates.md` ("Gold is a person's reading… Jev cannot enumerate anyway"), conflict detection ("never mechanised… `Zero-Trust` is the standing counter-example"), creating a page ("a page from an occurrence says nothing"), `[[links]]` ("a link is never inferred"), any count in prose ("a probability summed over documents is a guess shaped like a number"), deciding a near match ("a model decision has no rule to replay"). `Plan/concept/jev-in-ingestion_2026-09-23.md:37-47` [decided]

- **Four candidate placements, in order of evidence available**: (1) a second opinion on the judgement ledger — "measurable today" against 36+ existing decisions, and TypeSafe's own entity-alignment recipe's 3-level `Score` (different / related-a-person-decides / same) is judged a better fit than a bare `Noul` because "a person already decides every case that no rule settles"; (2) choosing the next document — where qmd is known to fail (BM25 misses the `KW1`-defining line), a `Noul` like *"does this passage assert X rather than ask/propose it"* could route, and a cited legal-passage rerank cookbook "took top-10 from 38% to 62%"; (3) flagging per-passage stance — "useful, and the most dangerous," must live in its own file `02b-stance-jev.txt`, explicitly `provisional`, scored against a person's marks before trusted; (4) triage for the 17 unresolved quotations — "probably not," named a second tempting-but-wrong fix. `Plan/concept/jev-in-ingestion_2026-09-23.md:51-148` [decided]

- **The stance-flagging idea's explicit demotion header**, in `CLAUDE.md`'s own three-line format: `stance_jev: provisional` / `# may not: appear in the profile, gate a page, or be read before the document` / `# retire when: it disagrees with the reader's marks as often as two readers do`. `Plan/concept/jev-in-ingestion_2026-09-23.md:135-139` [decided]

- **Author permission history, exact wording**: 2026-09-23, yes #1 — "a small test on the two documents with a reader's list" (the `jev_entities.py` run). Same day, yes #2 — using Jev **and** OpenRouter's free models for the German–English entity mapping (`bilingual.py`), which "sent Jev up to two lines of context per surface for 18,026 surfaces and up to four lines per pair for 11,277 pairs, drawn from across the landed corpus. The free models got **names only**, because a free endpoint may keep what it is sent." `NOW.md:103-110` [decided]

- **"Anything beyond those two uses should be asked for again, with its cost."** `NOW.md:110` [decided]

- **A concrete refusal that validates the permission boundary**: "When this session tried to send the 36 ledger pairs [to Jev for a second-opinion trial], the environment's permission check stopped it as data leaving the repository, and that was the right call to escalate rather than work around." `Plan/concept/jev-in-ingestion_2026-09-23.md:154-157` [decided]

- **Both API keys confirmed present in the environment (2026-09-23, presence only, never the value)**: "removes the technical block and none of the permission one above." A key pasted in chat earlier in the setting-up session "should be treated as spent and rotated." `NOW.md:114-116` [decided]

- **`bilingual.py`'s 5-stage pipeline**: (1) **stated** — code finds `A (B)`/`A (engl. B)`/`A/B` glosses the corpus writes itself, free, no model; (2) **entities** — Jev, one Noul per surface (in ≥`MIN_DOCS=5` documents, or named by a gloss), "is this an entity or key term of the corpus, not ordinary vocabulary?"; (3) **propose** — 4 free OpenRouter models, **names only, no corpus text**, up to 3 counterparts per entity, code keeps a counterpart only if the corpus actually contains it; (4) **pairs** — Jev Choice over the relation for every stated/proposed pair; (5) **write** — `Plan/entities/bilingual.md`+`.jsonl`. `scripts/bilingual.py:2-27,59-71` [decided]

- **Stage-1 gloss detection is pure regex, no model**: `PAREN` matches `Name (Name)` with an optional `engl./dt./auch/bzw./=/aka` marker inside the parenthesis; `SLASH` matches `Name/Name`; `LEADING` strips a leading German/English article (`Der|Die|Das|Den|Dem|Des|Ein|Eine|The|A|An`) before comparing surfaces. `scripts/bilingual.py:78-87` [decided]

- **`bilingual.py` measured results (2026-09-23)**: **stated** — 12,526 glosses found, 8,129 with ≥1 side an entity; **entities** — Jev accepted **6,989 of 18,026** surfaces as entities/key terms, spot-check "sound" (`Wächter` 0.83, `Guardian` 0.93, `Ziel` 0.17, `Die` 0.11 — one article slipped through at `Das` 0.73, so the write stage now drops bare articles); **propose** — 4 free models given names only proposed counterparts, **2,312** entities got one the corpus contains, **34** names never answered; **pairs** — Jev classified **11,277** pairs into **3,785** translation (2,474 at p≥0.8), **989** abbreviation, **250** variant, **2,465** role-or-part, **3,783** distinct. `NOW.md:353-362` [measured]

- **`bilingual.py` total cost**: **1,015** Jev calls, **10.9M** input tokens, ≈**$0.46**; plus 99 free-OpenRouter calls taking **70 minutes** because "only `nemotron-3-super` and `dots-3-note` answered a batch of 80 reliably." `NOW.md:363-365` [measured]

- **`OR_ROTATION` per-model reliability, measured on an 80-term batch (2026-09-23)**: `nvidia/nemotron-3-super-120b-a12b:free` and `dots-studio/dots-3-note-preview:free` answered in 45–120s; `nemotron-3-ultra` **hung 218s and broke off**; `gemma` and `qwen` were **rate-limited**. `scripts/bilingual.py:68-73` [measured]

- **What still needs a person, named explicitly**: the high-confidence (p≥0.8) pairs read correctly on wiki-relevant terms — `Kernwelten`/`Core Worlds` (8 documents), `Überwelt`/`Overworld` (5), `Risse`/`Rifts` (3), `Handlungsfähigkeit`/`Agency`, `Erleben`/`Qualia` (15) — but even there Jev calls some pairs "translations" that are actually naming relations, e.g. `Logik`/`LogOS` at 0.85 ("a guardian named for its domain"); below 0.8 the list is noisy (`Signposts`/`Transits` 0.63). "No pair has entered `judgements.jsonl`. Reviewing the high tier into it is the next step, and it is a person's." `NOW.md:367-373` [claim]

- **Offline replay discipline shared by both Jev scripts (P5)**: every request/response is cached — `jev_entities.py` under `Plan/runs/jev/<slug>/calls/<key>.json`, `bilingual.py` under `Plan/runs/bilingual/calls/{jev,openrouter}/<hash>.json` — and `--replay` serves from the recording with no key and no network; "a call that never returned is not an answer" (P15), so unreached calls are never cached. `scripts/jev_entities.py:114-119,128-129`; `scripts/bilingual.py:170-182,192-193` [decided]

- **Cache size, observed directly**: `Plan/runs/bilingual/calls/jev/` holds **1,114** cached call files. [measured]

- **TypeSafe cookbook-sourced limits carried into this repo's skill (none of these numbers were measured on this corpus, each cites its own cookbook)**: `Choice` max 255 options, "reliably up to roughly 240" (classification); `Score` max 10 levels, 11 is a server error (autoresearch); repeatability std-dev ≈0.01 over 15 identical repeats, and a borderline question still crossed 0.5 (`0.43`–`0.53`) — "repeatability is not correctness" (consistency_noul/consistency_choice); re-ranking a BM25 legal-passage shortlist "took top-10 from 38% to 62%" (rerank); rate limit "above roughly eight" concurrent (entity_alignment); default client timeout 10s, cookbooks used 30–120s for long states. `.agents/skills/typesafe/SKILL.md:30-34,90-95,118-129,151-156`; full detail in `.agents/skills/typesafe/references/cookbooks.md` [claim, TypeSafe's own measurements]

- **SDK as installed**: `typesafe-sdk` **0.7.1** in `.venv-typesafe`; `TypeSafeClient`/`Noul`/`NoulCriteria`/`Choice`/`Score`/`RetryPolicy`; `r.model` records the resolved version, `r.usage.input_tokens` ("output tokens were priced at 0 in every cookbook"); offline replay via `TypeSafeClient(transport=...)` + `httpx2.MockTransport`. `.agents/skills/typesafe/SKILL.md:131-160` [measured]

- **"Every call sends text to a third-party API, so no corpus text goes through it until a person has decided it may."** `CLAUDE.md:656-657` [decided]

- **Vendored `jev*` skills**: 11 folders copied unchanged from `wuyoscar/jev-skill` tag `v0.2.0`, commit `82c01055c80fa96d3e8a1b82132361693b6bf3a1`, MIT — real folders (not symlinks), so `rlm_ingest.py`'s `SkillManager` does not render them into its prompt; their `jev-decide` CLI is not in the repository and "does not survive the container" (must be `git clone`d and `uv tool install`ed fresh each time). "The route chosen for them is **A, real Jev**." `CLAUDE.md:663-676` [decided]


## TEST

- **`selftests.py` runs 16 named suites** across two interpreters: 9 standard-library suites (`quotes, find, fold`; `entities matcher`; `skills` ×2 — self-test and live; `baseline ledger`; `graph`; `graphrag`; `rlm_ingest tools, reach`; `prose numbers`) and 7 `.venv-dspy` suites (`dspy surface`; `dspy skill` ×2; `lm fixture`; `lmrun`; `pairs dry-run` [labeled optimizer]; `graphrag answer dry-run`). `scripts/selftests.py:25-43` [decided]

- **Three verdicts only, never collapsed into one bit (P11/P15)**: `held` / `FAILED` / `not run` — a `.venv-dspy` suite reports `not run` with the exact venv-creation command when the venv is absent, and "not run" still fails the overall exit status. `scripts/selftests.py:1-13,46-64` [decided]

- **`lm_fixture.FixtureLM`**: a `dspy.BaseLM` subclass built with `cache=False`; answers from a callable (`respond(messages)->str`) or a consumed list; an exhausted script `raise`s `AssertionError` instead of repeating its last answer — "a repeated answer is how a fixture quietly stops testing what it claims to." `scripts/lm_fixture.py:83-102` [decided]

- **`lm_fixture.offline()`**: configures dspy with the fixture, strips every `*_API_KEY` from `os.environ`, and monkeypatches `litellm.completion`/`acompletion` to a hard-raising `_refuse` — built because "`dspy-auto-gepa`'s test `test_partial_explicit_fields_infer_rest` was unmocked, fell through to the default LM, and made a live OpenRouter call from this container" during a routine repository scan (fixture words only, no corpus text). `scripts/lm_fixture.py:1-21,116-133` [lesson]

- **`lm_fixture.fill(**values)`**: reads ChatAdapter's "Your output fields are:" block straight out of the system message and answers whichever fields an optimizer's own internal prompts ask for (e.g. `InferRules` proposing rules, `GEPA` reflecting) — "lets a dry-run reach every optimizer's internal calls instead of dying on the first unknown one." `scripts/lm_fixture.py:63-80` [decided]

- **`lm_fixture.selftest()`, 3 cases**: the fixture answers and records the exact request sent; a real `dspy.LM` constructed *inside* `offline()` is refused (and every hidden API key is restored afterward); an exhausted scripted list raises rather than repeating. `scripts/lm_fixture.py:136-167` [measured]

- **`check_dspy_surface.py` asserts only what THIS repo calls**, via `inspect.signature`, across 9 DSPy symbols (`dspy.LM`, `dspy.RLM.__init__`, `LabeledFewShot`, `BootstrapFewShot`, `InferRules`, `SIMBA`, `GEPA`, `Evaluate`, `BaseLM.__init__`) — "a surface check that asserts things nobody uses is a second, drifting description of DSPy" — plus behavioural checks: the `dspy.__version__ == "3.3.1"` pin, `dspy.LM`'s `cache` default is `True` (this repo overrides it — a changed default should be noticed), `dspy.SIMBA`'s `bsize` default is 32 ("the ladder note assumes 32 > n=26"), `dspy.track_usage` still exists, `dspy.GEPA()` without `reflection_lm` still raises, `gepa.optimize_anything` is importable and still accepts `evaluator=`, `numpy` is importable (SIMBA needs it), and `example_param_ok()`'s own good/bad-signature self-check. **17 total checks.** `scripts/check_dspy_surface.py:34-107,114` [decided]

- **`check_skills.py`**: validates `.agents/skills/*/SKILL.md` (and the `.claude/skills/` symlinks) against the agentskills.io spec — filename case (`skill.md`/`Skill.md` rejected), `name == directory`, a whitelisted `SUPPORTED` frontmatter field set, a `FORBIDDEN` set (`triggers`, `version`, `dspy-compatibility`, `dspy-version`), `description+when_to_use ≤1536` chars, and this project's own P6 rule that `.claude/skills/<name>` must be a **symlink** into `.agents/skills/` (a real folder is a drifting second copy). Vendored `jev*` folders are checked but explicitly never fail the run — reported under their own heading. `scripts/check_skills.py:1-26,40-48` [decided]

- **`check_skills.selftest()`, 6 fixture cases**: lowercase filename, misnamed (`name` ≠ folder), missing `description`, `description` over the 1536-char limit, a forbidden legacy field (`version:`), and one clean control case. `scripts/check_skills.py:127-149,157` [measured]

- **`scripts/selftest.py`** (the corpus-fixture checker, distinct from each script's own `selftest()`): 6 quotation cases (`verbatim`/`declension`/`wrong-line`/`fabricated`/`emphasis`/`wrapped`) + 4 citation cases (`locate`/`declension-refused`/`fabricated-refused`/a cross-line `SPAN_CASE`) + 7 `fold()` pairs (4 `MUST_NOT_MERGE` + 3 `MUST_MERGE`) = **17** asserted cases, all run against a **real landed document** (`aegis-subplots-kapitelweise-system-exploration-docx`) so the whole resolution path — frontmatter, slug lookup, export unescaping, emphasis stripping, blockquote wrapping, glued footnote numbers — is actually exercised rather than a synthetic stand-in. `scripts/selftest.py:1-19,36-85,139-152` [decided]

- **A refusal must name *which* line it points at, asserted explicitly**: "a refusal that shrugs is worth no more than a wrong number" — `check_find()` checks that a declined `find_line` still names the nearest correct line (272) rather than merely saying "not found." `scripts/selftest.py:56-64,107-125` [decided]

- **`entities.py`'s own selftest**: an 8-probe cross-check of its whole-word token matcher against a literal `\bterm\b` regex (`AEGIS`, `Kern-Welt`, `Juna`, `Entropie`, `Guardian`, `Nexus`, `Wächter`, `KW1`), plus 7 hand-written `holds()` cases, each "the exact defect it once had or must never have" — `"(KW2),"` must still hold `"KW2"` (the footnote-digit-glue rule) but must **not** let it match bare `"KW"` (which would have merged `KW1`–`4` into one name); `*Silent Hill 2*` holds through italics; `"Kern\-Welt 1"` holds through export-escaping; `"Kontaktaufnahme"` must **not** hold `"Kontakt"` (the substring trap revision 2 failed); `"KIRA-Instanz"` must **not** hold `"KI"`; `"McLaughlin-Graphen"` must **not** hold `"McLaughlin-Graph"`. `scripts/entities.py:385-414` [measured]

- **`lmrun.py`, `lm_fixture.py`, `baseline.py`, `pairs.py`, `graphrag.py`, `graph.py`, `rlm_ingest.py`, `entities.py`, `check_dspy_surface.py`, `check_skills.py` and `scripts/selftest.py` all carry a self-test**; **`bilingual.py` and `jev_entities.py` do not**, and neither is listed in `selftests.py`'s `SUITES` — the two scripts that actually call Jev (real money, real corpus-adjacent data) are the two model-calling scripts in this repository with no offline fixture-based self-test of their own logic (they do have `--replay` cached-response reruns, which is a different guarantee: replaying real past answers, not asserting a failure mode). `scripts/selftests.py:25-43`; direct grep of `scripts/bilingual.py` and `scripts/jev_entities.py` for `selftest`/`SELFTEST` (no match) [claim]

- **`baseline.py`'s own selftest, 7 cases**: `unscored` (all outcomes `None`), `fail` (below the floor), `fail` (`vetoed` — a canary broken, regardless of score), `ok`, `warn` (some examples unscored), `warn` (trainset changed since the floor row), plus `digest()`'s key-order independence. `scripts/baseline.py:117-140,163` [measured]

- **`pairs.py`'s fold determinism**: `folds(labelled, k)` stratifies by `decision` (one-term/two-terms) and sorts each stratum by `baseline.digest(row id)` before distributing round-robin — "the same rows, the same folds," so a repeated run reproduces the identical split. `scripts/pairs.py:74-82` [decided]

- **`drg-kg` is installed for exactly one module — its evaluation scorer** — precisely *because* it was independently cross-checked against this repo's own `fold()` failure mode and reproduced it (see MET); its extraction and graph layers stay unused "because a canon link is written by a person and never inferred by a model." `CLAUDE.md:705-712` [decided]

- **`Plan/concept/dspy-toolchain_2026-09-23.md`'s cross-repository finding that motivated all of the above**: "six of the nine [scanned DSPy] repositories contain a check that cannot fail, each in a different costume" — `dspy-advanced-prompting`'s `edge_case_performance`/`test_coverage` returns 1.0 on an absent case type; `dspydantic`'s LLM-judge evaluators return 0.5 silently on a parse failure; `dspy-optimizer`'s validation strategies pass on empty input; `dspy-agents`' baseline-drift monitor accepts a `score=0.0, total_calls=0` run as a normal baseline; `braid-dspy`'s self-verification is keyword-counting on the model's own text; `drg-kg`'s own extraction silently returns an empty graph with no LM configured unless `DRG_REQUIRE_LM=1`. "Every metric and every guard below ships with a `selftest.py` case in which it must fail." `Plan/concept/dspy-toolchain_2026-09-23.md:86-109` [claim, cross-repo, taken as this project's own design mandate]


## DECIDED

- **GOAL.md's rule 13 (the top-level constraint on every model call, Ist-Stand 2026-09-23)**: "**Ein Modell schlägt vor, es entscheidet nie, und nichts verlässt den Container ohne Ja.** Jeder Modellaufruf läuft über `scripts/lmrun.py`: Cache aus, Protokoll pro Aufruf, und ohne `approval=` wird ein echtes Modell verweigert. Korpustext an OpenRouter oder TypeSafe braucht jeweils eine eigene Zustimmung des Autors." `GOAL.md:63` [decided]

- **Three model runs are each one command away, and each waits on its own yes** because each sends corpus words to OpenRouter: `pairs.py run --optimizer labeled` (the cheapest rung, on `fold()`'s residual — "the surface pairs and their rules, a few thousand tokens"); `graphrag.py ask "…" --answer` (a model picks evidence numbers — "the question and eight quotations per call"); `rlm_ingest.py <slug>` (a whole document; also needs Deno). `NOW.md:85-87,176-185` [decided]

- **"TypeSafe/Jev beyond the two uses already approved" is an explicitly open, unresolved permission question** — listed by name under *The process — the author's call*. `NOW.md:88` [decided]

- **Both `OPENROUTER_API_KEY` and `TYPESAFE_API_KEY` are confirmed present in the environment** (checked 2026-09-23, presence only, never the value) — "that removes the technical block and none of the permission one above." `NOW.md:114-116` [decided]

- **The narrowing of GOAL.md's proposed conflict-detection pipeline is itself an author-facing open item (C2)**: the goal's §4.4 step 2 asks a model to adjudicate; `CLAUDE.md` forbids mechanised conflict detection outright. The Ist-Stand block's proposed reconciliation is: steps 1 and 3 (predicate-value comparison, lock-pair satisfiability) are programs (P1); step 2 is **"Vorschlag, nie Record"** — the model-adjudication step writes only to a separate candidate file, through `lmrun.py`, with code-looked-up quotations, and "ein Conflict-Record entsteht erst, wenn eine Person ihn gelesen hat." This narrowing is flagged in Anhang C as "zu bestätigen oder zu ersetzen" — not yet the author's confirmed answer. `GOAL.md:294-304,744` [decided/claim — explicitly still open per the file itself]

- **"Nothing in the pipeline calls any of the three [installed DSPy-adjacent packages] yet. They are installed, reachable, and measured against this repository."** `CLAUDE.md:715-718` [decided]

- **Every dependency goes into a virtualenv, never the system Python** — "`pip install --break-system-packages` was tried once and broke `cryptography` for the whole container, which took the system interpreter down with it." `CLAUDE.md:610-615` [decided]

- **Four venvs, none surviving a container, each rebuilt on demand**: `.venv-tools` (3.11, markitdown for `sources.py land`), `.venv-dspy` (3.11, DSPy 3.3.1 with numpy — "every `scripts/` step that calls a model or its fixture"), `.venv-dspytools` (**3.12**, `dspytools` refuses 3.11), `.venv-typesafe` (3.11, `typesafe-sdk` for `jev_entities.py` and `bilingual.py`). `CLAUDE.md:633-636` [decided]

- **`dspy.RLM` needs Deno for its default Pyodide/WASM sandbox** — installed via `Legacy/scripts/setup_dspy.sh --deno`, and it "does not survive a container." `Plan/concept/rlm-measured-on-the-trap_2026-09-17.md:9-11` [decided]

- **The vendored-skill route decided for `jev*`**: "The route chosen for them is **A, real Jev**" (as opposed to a simulated/no-key fallback). `CLAUDE.md:676` [decided]

- **Two DSPy-skills packages installed for a different purpose than any of the model jobs above — making a `SKILL.md` reachable by a ReAct agent rather than only a person**: the runtime half `dspy-skills-implementation-` (installed with `--no-deps`, because it declares `dspy-ai>=2.5.0`, the old distribution name, which would move `.venv-dspy` off the pinned DSPy 3.3.1) plus `strictyaml`; the management half `dspytools` (needs Python 3.12, hence its own venv). `CLAUDE.md` *Installing anything* [decided]

- **`drg-kg` installed with `[extract]` but used for exactly one module — its evaluation scorer** — its extraction and graph layers deliberately stay unused. `CLAUDE.md:705-712` [decided]

- **P6 enforced structurally, not just by convention**: `.claude/skills/<name>` must be a **symlink** into `.agents/skills/`; `check_skills.py` checks this and the vendored `jev*` folders are the one deliberate exception, being real (unlinked) folders precisely so `rlm_ingest.py`'s `SkillManager` does not render them into an agent's prompt. `CLAUDE.md:663-668`; `scripts/check_skills.py:15-21` [decided]

- **A per-run cost budget is a named requirement, not yet a hard limit**: "Budget before looping" (RLM) and "say what the full run costs before starting it, and ask" (the full entity-list run, ≈36M tokens) are both stated as author-facing gates rather than code-enforced ceilings. `Plan/concept/rlm-measured-on-the-trap_2026-09-17.md:81`; `NOW.md:335-337` [decided]

- **`ask` (graphrag) is explicitly capped at chosen-and-verified quotations for now** — "`graphrag.py` returns verified quotations and never prose, because prose over two sources is a merge (P13)." Whether it should ever produce more (a framing sentence, a marked-as-the-model's summary) is "the author's to decide, and nothing builds it until then." `NOW.md:186-189` [decided]

- **Whether a model may ever *propose* a graph edge the prose does not state is deferred, not merely unbuilt**: "to be asked against this baseline rather than instead of it — a guessed edge is indistinguishable from a stated one once it is in the graph." The bench (42%/64% recall@8) is explicitly named as the baseline any such proposal would have to beat. `CLAUDE.md:387-390`; `Plan/concept/graphrag_2026-09-23.md:149-153` [decided]

- **Jev's placement rule, generalized to a policy in the vendored skill**: "A Jev answer may direct attention, never enter the record. No candidate list, page, reading, link, conflict or count is written from a probability." "Sending corpus text to TypeSafe is an author decision (P0) and has not been made [beyond the two approved uses]." `.agents/skills/typesafe/SKILL.md:174-180` [decided]


## OPEN

- **Which of the three one-command model runs the author will approve, and when**: `pairs.py run --optimizer labeled`; `graphrag.py ask "…" --answer`; `rlm_ingest.py <slug>`. `NOW.md:85-87,176-185` [claim]

- **How far TypeSafe/Jev use may go beyond the two already-approved uses** (`jev_entities.py`'s pilot, `bilingual.py`'s mapping) — no third use has a yes yet, including reviewing the corpus-search reranking idea, the document-choice idea, or the stance-flagging idea. `NOW.md:88,103-112`; `Plan/concept/jev-in-ingestion_2026-09-23.md:51-148` [claim]

- **How far `ask` may go**: chosen quotations only forever, or eventually a framing sentence / a summary explicitly marked as the model's. `NOW.md:89-90,186-189`; `Plan/concept/graphrag_2026-09-23.md` *Next*, item 4–5 [claim]

- **How much morphology `fold()` (a deterministic rule) may claim**, before the residual is handed to a model at all — plurals and inflections are its systematic misses (see MET), and "the next improvement is a rule, not a model," but the rule's exact reach is not yet decided. `NOW.md:95-96,164-170` [claim]

- **Whether a model may ever propose a graph edge the prose does not state** — explicitly deferred to be measured against the 42%/64% bench baseline rather than argued abstractly. `CLAUDE.md:387-390`; `Plan/concept/graphrag_2026-09-23.md` *Next*, item 5 [claim]

- **GOAL.md's own open item C2**: whether its Ist-Stand narrowing of the conflict-detection model step (program for steps 1/3, model output only a never-committed candidate file for step 2) is the author's confirmed design or needs replacing. `GOAL.md:744` [claim]

- **A tension between GOAL.md's stated embeddings policy and current practice, not reconciled anywhere in the text**: GOAL.md §8 says "keine Vektor-Datenbank… Embeddings kommen höchstens optional in Phase 7, wenn die Gold-Q&A es verlangt" (no vector database; embeddings at most optionally in Phase 7, if the Gold-Q&A requires it) — but qmd, already in daily use for corpus search, has run local embeddings (`embeddinggemma-300M`) since `qmd embed` was first run, with no Gold-Q&A in place. `GOAL.md:608` vs. `.agents/skills/qmd/SKILL.md` [claim, inferred tension — not flagged as resolved by any document read]

- **Job 2's gate**: the author's definition of an entity — research vocabulary (what the Jev/candidate-script pilot leaned toward) vs. "the world" (what the human readers captured) — named as the open question by both the Haiku pilot and, more sharply, the Jev pilot: "the definition decides the list, not the model." `Plan/concept/dspy-toolchain_2026-09-23.md:279-280`; `NOW.md:319-323,341-345` [claim]

- **Job 4's gate**: 5–20 recorded routing failures (an agent loaded the wrong skill, or none) are needed before `optimize_anything` on skill descriptions can start under P4 — "none are recorded today." `Plan/concept/dspy-toolchain_2026-09-23.md:321-323`; `NOW.md:235-236` [claim]

- **Whether a one-line stated reading gap should demote an entity list from "reading" status** (`kohaerenz-protokoll`'s `read_to_line` 2497 of 2498) — left explicitly undecided as "a decision, not a fix," alternative being to have the reader simply finish the line. `NOW.md:279-282,333-334` [claim]

- **Reviewing `bilingual.py`'s high-confidence (≥0.8) pairs into `judgements.jsonl`** — named as "the next step, and it is a person's," not yet done as of the last read. `NOW.md:372-373` [claim]

- **Whether corpus text may leave the repository at all for the three not-yet-adopted Jev placements** (document-choice reranking, per-passage stance flagging, quotation-triage) — "an author decision, not an engineering one." `Plan/concept/jev-in-ingestion_2026-09-23.md:150-157` [claim]

- **Which qmd backend this corpus actually wants** — `qmd bench` (the 4-backend IR harness) has never been run; the fixture is nearly free (existing "a search finds this in `<slug>`" claims) but the run itself is gated on the author's go-ahead being named explicitly as still open. `NOW.md:156-162` [claim]


## FAILED

- **The retired predecessor's `coverage()` metric term returned 1.0 whenever it was passed zero gold fragments, and it was never passed any** — two live runs of that pipeline scored **0.987** and **0.967** across 53 LM calls on a recall axis "that could not fall for missing anything." This is the single most-cited failure in this repository's model-evaluation culture, invoked as the reason `selftest.py`, `check_dspy_surface.py`'s trap-check, and the DSPy-repo scan's "six of nine contain a check that cannot fail" finding all exist. `.agents/skills/ingest/SKILL.md:26-33`; `scripts/selftest.py:1-7` [lesson]

- **The first `dspy.RLM` run on this corpus ran out of REPL budget mid-document and was about to fabricate the rest** — its own reasoning trace read: "*We have full document variable inaccessible except history outputs… We can reconstruct from outputs.*" It only failed to land because the reply parsed as empty (`text: None` inside `reasoning_content`) — "that is luck, not a safeguard." This single event produced the per-candidate line-verification requirement now built into `rlm_ingest.py`. `Plan/learnings/extract-terms.md:366-384`; `scripts/rlm_ingest.py:18-31` [lesson]

- **`rlm_ingest.py`'s originally-preferred model, `nex-agi/nex-n2.5-pro:free`, is structurally unusable for RLM**: it returns its answer inside `reasoning_content` with `text: None`, which DSPy's `ChatAdapter` treats as an empty response — replaced by `nvidia/nemotron-3-super-120b-a12b:free` as the script's default. `scripts/rlm_ingest.py:90-95` [lesson]

- **`dspy-auto-gepa`'s own test suite made a live, uncontrolled OpenRouter call from this container** — `test_partial_explicit_fields_infer_rest` was unmocked and fell through to the default LM during a routine dependency scan (fixture words only — "hello", "bye" — no corpus text reached the network). It is the direct cause of `lm_fixture.offline()` hard-refusing the network rather than trusting mocking discipline alone. `scripts/lm_fixture.py:7-17` [lesson]

- **`lmrun.py`'s own offline test suite had a real gap until 2026-09-24**: its first nine cases never exercised DSPy 3.3's own `LMTransportError`; the first live run that hit it found `call()` **re-raising it instead of recording `status="unreachable"`** — the `_unreachable()` classifier's `_NO_ANSWER` tuple now explicitly includes it. `Plan/concept/dspy-toolchain_2026-09-23.md:16`; `scripts/lmrun.py:94-98` [lesson]

- **A free model tied the deterministic baseline's *score* while silently breaking the one distinction that matters**: `nex-agi/nex-n2.5-mini:free` matched `fold()`'s 14/17=82% on the one-term-or-two task while **merging the `Negentropie`/`Entropie` canary** — "the exact failure `fold()` is built to avoid. A scalar would have called them equal." Caught only because a held-out canary existed at all. `Plan/concept/trainset-and-the-baseline_2026-09-17.md:57-60`; `Plan/concept/skills_2026-09-17.md:135-137` [lesson]

- **A model can score a perfect 1.00 and still fail unpredictably**: `nvidia/nemotron-3.5-lightning:free` scored 1.00 when it worked in `lm-bench` but failed 1 of 3 attempts by emitting chain-of-thought ("Here's a thinking process:") where JSON belonged, `AdapterParseError`. "This is exactly the failure mode the benchmark was built to catch, and exactly why `--repeats 1` would have been worthless: a single lucky attempt would have shown 100%." `Plan/quality/lm-bench_2026-09-16.md:73-79` [lesson]

- **A metric that checks a claim's language but not the whole output's language misses a real defect**: the free-models router returned correct German claims (scored 1.00) but an **English** `triage.summary` for a German source — invisible to `ingest_metric`, which "checks the claims' language, not the summary's. A lint proves what is forbidden is absent; it cannot prove what is required is right." `Plan/quality/lm-bench_2026-09-16.md:51-55` [lesson]

- **A reasoning model silently spent its whole token budget on hidden reasoning and returned nothing, with no error**: at `max_tokens=400`, `poolside/laguna-s-2.1:free` (served via `openrouter/free`) returned `content: None`, `finish_reason: length`, after consuming all 400 tokens as `reasoning_tokens` — "a longer-reasoning model returns empty content with no error, which a prose gate would read as 'nothing to report'." The same model's reasoning overhead varied 16-fold across three otherwise-identical calls (25 to 400 reasoning tokens). `Plan/quality/lm-bench_2026-09-16.md:121-141` [lesson]

- **Two "0% score" models in an early sweep were not model failures at all**: one returned a 404 (`nvidia/nemotron-3-ultra-550b-a55b:free`, listed in OpenRouter's catalogue but not actually served), the other was hard-restricted to "agentic harnesses only" (`thinkingmachines/inkling:free`) — recorded explicitly as "never reached — not measured, and not a verdict on the model." `Plan/quality/lm-bench_2026-09-16.md:22-27` [lesson]

- **Eleven of fifteen free OpenRouter models did not answer a real prompt at all** during the Guardians-count trap experiment (404/429/403/no-`choices`) — "the free tier is not a benchmark surface." `Plan/concept/rlm-measured-on-the-trap_2026-09-17.md:45-46` [lesson]

- **An RLM run can reproduce a source document's own internal error rather than correcting it**: on the five-vs-"vier"-Guardians trap, `dspy.RLM` (haiku) landed on **4**, matching the document's own inconsistent framing text, missing Sophia — "the RLM reproduced the document's own off-by-one. That is the interesting failure, because it is the *document* that is misleading, not the task." `Plan/concept/rlm-measured-on-the-trap_2026-09-17.md:50-53` [lesson]

- **`graph.py`'s first independent implementation of quotation-verification disagreed with `quotes.py`'s**: 14 unresolved vs. 4, on the same pages — "two encodings of one rule disagreed on the first run," resolved by merging into one shared `quotes.pairs`/`quotes.verdict` implementation both scripts now call. `NOW.md:251-254` [lesson]

- **`judgements.py`'s very first replay run found a live, already-shipped defect**: `fold()`'s own docstring claimed behaviour it did not have, and "the same false claim had been repeated in two other files." `Plan/concept/continuous-improvement_2026-09-17.md:16` [lesson]

- **A 100%-green `judgements.py` replay did not catch a real counting bug**: `fold()` itself was correct throughout while `reconcile.py`'s own intra-list check excluded exact fold-equality, causing it to report three worlds as six "new" terms — no recorded judgement covered the calling code, so nothing in the ledger could have caught it. "A green replay says the recorded decisions still hold, not that the code around them is right." `CLAUDE.md:478-488` [lesson]

- **`state.py --prose`'s own guard could not see 8 of its 49 markers**, because its regex forbade a newline between a number and its `<!--state:key-->` marker — a number wrapped across a line break left the marker matching nothing, `order.holds` among them, "while the check printed '0 prose claims contradict the repository.'" `PRINCIPLES.md:109-114` [lesson]

- **`capture.py` silently dropped every extraction candidate longer than 40 characters** — of 28 long lines found in one audit, the 24 that were prose were already caught by another check, but the 4 that were real terms were missed and never reported as "could not check." `PRINCIPLES.md:114-117` [lesson]

- **qmd's index had 0 of 464 (then 465) documents embedded for an unknown period, and nothing said so** — the embedding model had simply never been downloaded, so `vsearch` returned `"No results found"` **with exit code 0** — "it looks like an answer." `Plan/concept/skills_2026-09-17.md:63-64`; `.agents/skills/qmd/SKILL.md:139-141` [lesson]

- **This repository's own prior advice about qmd was itself wrong and went uncorrected until measured**: `CLAUDE.md` had said qmd "answers a lowercase German phrase in about 0.2s" and recommended structured `lex:`/`vec:`/`hyde:` queries over a plain phrase — "both halves were wrong." The 0.2s figure came from a cache hit on an already-asked example phrase; structured queries for a real hard case (`"welcher Guardian gehört zu Kernwelt 1"`) took **3m14s** and scored *worse* than plain search. `Plan/concept/skills_2026-09-17.md:55-67`; `.agents/skills/qmd/SKILL.md:222-233` [lesson]

- **`qmd`'s own visible index carried 1,047 markdown files and zero JSON**, meaning the two densest decision records in the repository — `judgements.jsonl` and every `reconcile.json` — were invisible to every search until `judgements.py` began rendering a markdown mirror on every run. `Plan/concept/skills_2026-09-17.md:96-102` [lesson]

- **`qmd`'s free-text `--check` self-report drifted from reality**: `setup_qmd.sh --check` printed "7 of 6" for the `decisions` collection because the expected count was a hard-coded constant rather than derived — "the same defect as the three-file list in `--prose`, one directory over." `Plan/concept/skills_2026-09-17.md:110-112` [lesson]

- **`bilingual.py`'s free-model rotation is unreliable at scale, measured**: on an 80-term test batch, `nemotron-3-ultra` **hung for 218 seconds and broke off**, and `gemma`/`qwen` were **rate-limited** — only 2 of 5 rotation models (`nemotron-3-super`, `dots-3-note`) answered reliably, which is why the full `propose` stage's 99 free calls took 70 minutes. `scripts/bilingual.py:68-73`; `NOW.md:363-365` [lesson]

- **Jev, asked "is this an entity" with too permissive a definition, optimised for the wrong list**: it said yes to ~20% of candidates on `aegis-subplots` and ranked cited authors from footnote URLs (`Sartre`, `Camus`) above the document's own world-terms — "it did what the question asked… the definition decides the list, not the model." `NOW.md:319-323` [lesson]

- **Entity-list revision 2's gazetteer silently lost a whole class of names to a checker bug, and the reader was blamed first**: `quotes.normalise` stripped a 1–2 digit number glued to a word (footnote-number debris), turning `(KW2),` into `(KW),` while the target name stayed `KW2` — a name ending in a digit could never verify, costing `KW2`–`KW4`, `Kern-Welt 1`–`4` and `Silent Hill 2` from the gazetteer list. Found only while building `entities.py`'s unified `holds()` check. `NOW.md:285-289` [lesson]

- **Entity-list revision 1 reproduced the exact identifier-fabrication defect P26 exists to prevent**: of 374 rows, only 280 (74.9%) cited a line that actually held the entity; 39 of the 94 failures invented a form the document never contains at all — fixed only in revision 3 by taking line numbers away from the model entirely (names in, lines placed by code). `Plan/concept/entity-lists_2026-09-23.md:81-84,90-93`; `PRINCIPLES.md:154-157` [lesson]

- **An earlier session's corpus-wide counting tool exposed a systematic error hiding inside "careful" ad-hoc counts**: every heredoc count taken before `corpus.py` existed used `lines[9:]` to skip frontmatter, silently swallowing nine lines of real content in the 26 (of then-409) documents that had none — the direct cause of a `Julia`-occurrence count disagreeing by exactly one document (26 vs. 27) between two supposedly-careful passes. `Plan/concept/rlm-transfer_2026-09-17.md:79-88` [lesson]

