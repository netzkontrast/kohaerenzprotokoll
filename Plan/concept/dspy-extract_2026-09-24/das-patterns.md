# dspy-agent-skills — knowledge-work patterns (DAS-patterns slice)

Seven skills — `dspy-wiki-compile`, `dspy-adversarial-review`, `dspy-clarify`,
`dspy-tetraframe`, `dspy-autodialectics`, `dspy-deep-refine`, `dspy-reflect-loop` —
and the two plans `docs/kohaerenz-protokoll-plugin-plan.md` and
`docs/compounding-wiki-extension-plan.md`. Every file in each skill was read in
full (SKILL.md, reference.md, example_*.py). All example paths below are relative
to `/home/user/dspy-agent-skills/`; `ex:` abbreviates the skill's `example_*.py`.

## 1. Header

- **Repo:** `netzkontrast/dspy-agent-skills` (local `/home/user/dspy-agent-skills`), commit `9d13f98` ("Merge pull request #6 …"). `.claude-plugin/plugin.json` still names `intertwine/dspy-agent-skills` as homepage/repository; version `0.11.0`.
- **License:** MIT (`LICENSE`, © 2026 Bryan Young). Upstream licences for this slice (README.md:200-214 and each reference.md): tetraframe ← `Hmbown/tetraframe-dspy` MIT; clarify ← `Hmbown/clarify` Apache-2.0; autodialectics ← `Hmbown/autodialectics` MIT; deep-refine ← DeepRefine (arXiv:2605.10488) + `DeepRefine-Skill` v0.2.0, licence listed as "—"; reflect-loop ← `claude-reflect-system` v1.3.0, licence "—"; wiki-compile ← Karpathy LLM-wiki bootstrap, `llm-wiki-agent` (MIT), `llm-wiki-compiler` (none stated), `synthadoc` ("AGPL, patterns only"), `quicky-wiki` (MIT); adversarial-review ← synthadoc (AGPL, patterns only), AutoSci (MIT), quicky-wiki (MIT), llm-wiki-compiler.
- **DSPy targeted:** 3.3.x — `requirements.txt` pins `dspy>=3.3.0,<3.4`; CHANGELOG.md:3-5 "Retargeted to DSPy 3.3.1". The slice was first validated on 3.2.1 (CHANGELOG.md:250 deep-refine and reflect-loop, :235 clarify, :221 tetraframe, :194 wiki-compile and adversarial-review; the autodialectics entry at :207 names no version) and **its API usage holds on 3.3.1**: all seven dry-runs exit 0 on 3.3.1, and every DSPy construct it uses (class signatures with pydantic/`Literal`/`tuple` field types, `ChainOfThought`, `Predict`, `BestOfN`, `Refine`, `dspy.context`, `LM.copy(rollout_id=…, temperature=…)`, `named_predictors`, `Example.with_inputs`, `Prediction.toDict`, `configure(track_usage=True)`, the GEPA parameters named in the docs) exists with those parameters (checked against the installed source). None of the 3.3.0 RLM renames touch this slice.
- **What it is:** seven procedures of knowledge work — compile sources into a cited wiki, review an artifact with an independent model, make a claim precise by asking, analyse a contested decision from four isolated corners, keep a program run honest, repair a knowledge base from unanswerable questions, turn human corrections into gold — each as a DSPy program whose LM stages are typed Signatures and whose metric is a deterministic Python function returning `dspy.Prediction(score, feedback)`. The two plans are integration plans for the target's predecessor (the pre-reset Kohärenz Protokoll).
- **What I ran** (all offline; every Python run prefixed `env -u OPENROUTER_API_KEY -u TYPESAFE_API_KEY -u OPENAI_API_KEY -u ANTHROPIC_API_KEY`; interpreter `/home/user/kohaerenzprotokoll/.venv-dspy/bin/python` = DSPy 3.3.1, pydantic 2.13.5):
  1. all seven `ex --dry-run` → exit 0, 1.7–2.3 s wall each; printed numbers quoted below;
  2. seven probe scripts, one per skill, that import the example module and feed edge cases to its deterministic functions (cited as "probe W…/A…/C…/T…/AD…/DR…/R…");
  3. `review_refine` end to end with two `dspy.utils.dummies.DummyLM`s (writer, reviewer) to see which LM writes `dspy.Refine`'s feedback;
  4. `DeepRefine(max_hops=5)` against a `DummyLM` that always answers `answerable=False`;
  5. `ChatAdapter().parse` on a `Clarification` that violates `min_length=2`;
  6. `BestOfN`/`Refine` around a module that always raises, N = 1, 2, 3;
  7. read of the installed DSPy source: `predict/refine.py`, `predict/best_of_n.py`, `primitives/base_module.py:23-67`, `primitives/module.py:179-216`, `clients/lm.py`, `clients/base_lm.py:735-765`, `clients/cache.py:104-112`, `teleprompt/gepa/gepa.py:549`, `teleprompt/gepa/gepa_utils.py:340-441`; `inspect.signature` of `GEPA`, `Embeddings`;
  8. `uv run --no-project --with pytest --with pyyaml python -m pytest tests/ -q -p no:cacheprovider` → `633 passed in 0.87s`;
  9. `ls`/`find` in `/home/user/kohaerenzprotokoll` for every path the two plans name.
  The probe imports wrote `__pycache__/example_*.pyc` into the seven skill directories; I deleted exactly those; `git status` of the pack is clean.

## 2. Knowledge items

### API

- **Class signatures whose one output is a pydantic model** — every LM stage in the slice is a class-based `dspy.Signature` with typed pydantic outputs: `triage: Triage`, `claims: list[Claim]`, `concepts: list[ConceptDraft]`, `decision: IngestDecision`, `diff: Diff`, `answer: Answer` (wiki-compile ex:245-293); `review: Review`, `support: Support` (adversarial ex:129-145); `clarification: Clarification` (clarify ex:137-150); `distilled: Distilled`, `selection: Selection`, `corner: Corner`, `cartography: Cartography`, `frame: Frame` (tetraframe ex:245-293); `steps: list[str]`, `objections: list[Objection]`, `dispositions: list[Disposition]`, `revised_steps: list[str]`, `output: Output`, `checks: list[tuple[str, bool, str]]` (autodialectics ex:266-301); `answerable: bool`, `abduction: Abduction`, `actions: list[RefinementAction]` (deep-refine ex:168-190); `signal: LearningSignal` (reflect ex:74-82). [api] (verified: all seven dry-runs construct them on 3.3.1)
- **Pydantic models as inputs** — nested models are passed as InputFields and serialised by the adapter: `page: PageState`, `concept: ConceptDraft`, `extractions: list[Extraction]`, `pages: list[PageState]` (wiki-compile ex:267-292), `view: CornerView`, `corners: list[Corner]`, `cartography: Cartography` (tetraframe ex:261, 283, 290-292), `contract: Contract` on all five autodialectics predictors (ex:269-300), `abduction: Abduction` (deep-refine ex:189). [api] (verified: dry-runs construct)
- **Closed enums as `Literal`** — the slice's vocabulary is carried by `Literal` types, not strings: `Tier`, `Action`, `PageStatus`, `ConceptStatus`, `Resolution` (wiki-compile ex:28-32); `Difficulty`, `Verdict` (adversarial ex:31-32); verdict `Literal["clear","needs-author","not-promotable"]` (clarify ex:53); `Mode` (tetraframe ex:25); `Domain` (autodialectics ex:26); `RefinementAction.kind`, `ActionReview.confidence` (deep-refine ex:47, 53); `kind`/`confidence` as `Literal[...] | None = None`, `scope_hint` (reflect ex:34-39). Free-text `basis_label: str` is the one exception: the tetraframe vocabularies (`BOTH_BASES`, `NEITHER_FAILURES`) are checked by the metric, not typed (ex:79, 154, 161). [api]
- **Tuple element types in an output list** — `checks: list[tuple[str, bool, str]] = dspy.OutputField()` (autodialectics ex:301; SKILL.md:116 adds `desc="(criterion, passed, reason)"`) builds a valid signature on 3.3.1. [api] (verified: constructed a signature with that field)
- **Signature subclasses as instruction variants** — `class CornerP(GenerateCorner): """…"""` (tetraframe ex:258-277) inherits the fields and replaces the instructions with the subclass docstring; a subclass without a docstring keeps the base docstring; `ChainOfThought` prepends `reasoning` to the outputs. [api] (verified: `Child.instructions == 'Child instruction.'`, `Bare.instructions == 'Base instruction.'`, CoT outputs `['reasoning','corner']`)
- **Output-model constraints fail the whole prediction** — pydantic constraints inside an output model (`Citation.start/end ge=1` wiki-compile ex:41-42; `Review.score ge=1, le=10` adversarial ex:44; `Ambiguity.readings min_length=2` clarify ex:32; `RefinementAction.args min_length=2, max_length=3` deep-refine ex:48; `Corner.confidence_score`/`Distilled.frame_risk_score` 0..1 tetraframe ex:50, 84; `Objection.severity` 0..1 autodialectics ex:84) are enforced at parse time: one ambiguity with a single reading makes `ChatAdapter.parse` raise `AdapterParseError` citing pydantic `too_short`, and through `Predict` the call ends in `AdapterParseError` after the JSONAdapter fallback — the whole `Clarification` is lost, not one item. [api|trap] (verified: probe_parse, probe_parse2) → here: `lmrun.py` status `unparsed`; keep output constraints loose and check them in code afterwards
- **`InputField(desc=…)` carries the context contract** — `evidence` "the pages or spans the artifact may rely on" (adversarial ex:136), `source_excerpt` "the cited lines of the source", `glossary_terms` "comma-separated known slugs", `canon_context` "… or empty" (clarify ex:146-149), `triples` "one 'subject \| relation \| object' per line", `interaction_history` "last steps: hop, triples, judgement" (deep-refine SKILL.md:49, 61), `prior_assistant_turn` "what the program/assistant did right before" (reflect SKILL.md:62). [api]
- **A second LM for one call** — the writer stays under `dspy.configure(lm=writer)`, the judge runs inside `with dspy.context(lm=self.reviewer_lm):` (adversarial ex:161-162, 167-168; SKILL.md:71-74). [api]
- **`LM.copy(rollout_id=i, temperature=t)`** — returns a shallow copy with `history = []`, a copied `callbacks` list and a copied `kwargs` dict (base_lm.py:735-765). `rollout_id` is popped before the provider call (`request.pop("rollout_id", None)`, lm.py:498) but is part of the request dict the cache keys on (cache.py:104-112 ignores only `api_key`, `api_base`, `base_url`), so different ids bypass the cache and the same id hits it. With `temperature == 0` DSPy warns „rollout_id has no effect when temperature=0; set temperature>0 to bypass the cache." (lm.py:165-169). Used per corner in tetraframe (ex:317-318). [api] (verified: source read)
- **`dspy.LM(...).kwargs` in 3.3.1** — a bare `dspy.LM("openai/gpt-4o")` has `kwargs == {'temperature': None, 'max_tokens': None}`; `cache` is an attribute, not a kwarg. `LM.__init__(model, model_type="chat", temperature=None, max_tokens=None, cache=True, callbacks=None, num_retries=3, provider=None, finetuning_model=None, launch_kwargs=None, train_kwargs=None, use_developer_role=False, **kwargs)` (lm.py:62-76). [api] (verified: probe A3) → here: any guard comparing LMs by kwargs
- **`dspy.Refine(module, N, reward_fn, threshold, fail_count=None)`** — each attempt runs `lm.copy(rollout_id=start+i, temperature=1.0)` on a `module.deepcopy()` via `mod.set_lm(lm_)` (not via `dspy.context`), so `dspy.settings.lm` stays the original LM during the attempt and the reward; the first attempt with `reward >= threshold` wins, else the best; between attempts `dspy.Predict(OfferFeedback)` — run on `dspy.settings.lm` — writes per-predictor `advice` from the program code, the trajectory, `reward_code` (the reward function's source), `target_threshold` and `reward_value`, and the next attempt receives it through an appended `hint_` input field ("A hint to the module from an earlier run") (refine.py:15-38, 98-177). Constructor calls `inspect.getsource(module.__class__)` and of `reward_fn` (refine.py:92-96), so both must be defined in a file. [api] (verified: source read + DummyLM run)
- **Refine's type warnings in 3.3.1** — Refine orjson-dumps every non-string advice input (refine.py:163-166), so each feedback call logs „Type mismatch for field 'target_threshold': expected float …", same for `reward_value` and `module_names`. Harmless, but it appears in every Refine run with a threshold. [api] (verified: DummyLM run)
- **`dspy.BestOfN(module, N, reward_fn, threshold, fail_count=None)`** — same rollout scheme at `temperature=1.0` (best_of_n.py:57), no feedback between attempts, returns the first prediction whose reward ≥ threshold or the best one; the reward's own LM calls are excluded from the trace (best_of_n.py:66). [api]
- **`Module.get_lm()` / `set_lm()`** — `set_lm` sets `lm` on every predictor (module.py:179-196); `get_lm` returns the single LM all predictors share and raises „Multiple LMs are being used in the module. There's no unique LM to return." otherwise — including when the module has no predictors (module.py:198-216). Refine and BestOfN call it first (refine.py:99, best_of_n.py:51) and fall back to `dspy.settings.lm` only when it returns `None`. [api]
- **`named_parameters()` walks dict and list attributes one level deep, dedupes by `id`, and skips sub-modules with `_compiled=True`** (base_module.py:23-67). So `self.generators = {"P": ChainOfThought(...), …}` is found and named `generators['P'].predict`; the aliases `self.corner_p = self.generators["P"]` (tetraframe ex:302-303) are redundant in 3.3.1 — the dry-run lists the corners only under their dict paths, never as `corner_p`. [api] (verified: dry-run output)
- **`Prediction.toDict()`, `Example.inputs()/labels()`** — `corrections_metric` stringifies `pred.toDict()` (reflect ex:105); `learning_to_example(...).with_inputs(*failing_input)` makes the failing input's keys the inputs and `expected_behavior`, `forbidden_behavior`, `feedback` the labels (reflect ex:99-102). [api] (verified: probe R2c)
- **Lazy `import dspy`** — all seven examples import dspy inside `build()` and inside each metric; the deterministic core (models, guards, metrics' helpers) imports only pydantic, so it runs where DSPy is absent (autodialectics calls this "Tier 0", SKILL.md:34-43). [pattern]
- **Live-path configuration** — `dspy.configure(lm=dspy.LM(args.model), track_usage=True)` in clarify ex:213, tetraframe ex:391, deep-refine ex:280, reflect ex:176; plain `dspy.configure(lm=…)` in wiki-compile ex:382, adversarial ex:234, autodialectics ex:378. Defaults: `DSPY_MODEL` or `openai/gpt-4o` everywhere except autodialectics `openai/gpt-4o-mini` (ex:371); adversarial reviewer `DSPY_REVIEWER` or `openai/gpt-4o-mini` (ex:204) — i.e. the default judge is the weaker model. No live path sets `cache=False`. [api]
- **OpenAI-compatible endpoint** — `dspy.LM("openai/<model>", api_base="http://127.0.0.1:8642/v1", api_key="EMPTY")` (autodialectics reference.md:171-173); a cheaper LM for `Antithesis` and `Verify` via `dspy.context(lm=…)` inside `forward` (reference.md:176-177). [recipe]
- **`dspy.Embeddings` in 3.3.1** — `Embeddings(corpus, embedder, k=5, callbacks=None, cache=False, brute_force_threshold=20000, normalize=True)`; the plugin plan's canon index is built with it (plugin plan:141-144). [api] (verified: inspect.signature)

### OPT

- **GEPA per pattern, as the docs prescribe** — wiki-compile: `dspy.GEPA(auto="light")` over `extract`, `merge`, `decide` with `compile_metric`, `answer` on a separate gold set (SKILL.md:112-114); adversarial: GEPA light on `review.predict` with `judge_metric` (reference.md:82-83); clarify: GEPA light, 20–40 claims (SKILL.md:124-126); tetraframe: GEPA light over the corner generators and the transformer, 10–20 seeds (SKILL.md:168-171); autodialectics Tier 2: GEPA on the planner/`Dialectic` → challenger (SKILL.md:167-168); deep-refine: GEPA light rewriting `abduce` and `propose` (SKILL.md:147-150); reflect: GEPA on the program with corrections folded in, and on `ReflectLoop` with `reflector_metric` after ≥ 5 reviewed sessions (reference.md:126-127). [recipe|claim] — no example constructs `dspy.GEPA`; see T47.
- **GEPA constructor/compile in 3.3.1** — `metric` required; `auto=None`, `reflection_lm=None`, `track_stats=False`, `log_dir=None`, `max_metric_calls=None`, `reflection_minibatch_size=3`, `candidate_selection_strategy='pareto'`, `use_merge=True`, `seed=0`; `compile(student, *, trainset, teacher=None, valset=None)` — trainset keyword-only. The deep-refine snippet `dspy.GEPA(metric=refine_metric, auto="light", reflection_lm=dspy.LM("openai/gpt-5", temperature=1.0, max_tokens=32000), track_stats=True, log_dir="./gepa_logs")` + `compile(student=DeepRefine(retrieve), trainset=trainset, valset=valset)` (reference.md:163-167) matches it. [api] (verified: inspect.signature)
- **Restricting GEPA to some predictors is never shown** — the docs say "over `extract`, `merge` and `decide`" but not how. GEPA enumerates `student.named_predictors()` (gepa.py:549) and `named_parameters` skips sub-modules with `_compiled=True` (base_module.py:52-56), so freezing a stage means setting `_compiled = True` on it. [api] (verified: source read; not run through GEPA)
- **Unused predictors become GEPA components** — `BatchCompile.answer` is never called in `forward` (wiki-compile ex:303, 305-320) and `AdversarialReviewer.support` only in `check_citation` (adversarial ex:151, 166-168), yet both are in `named_predictors()`. GEPA matches trace entries to a component by `signature.equals` (gepa_utils.py:348), logs „No valid reflective examples found for {pred_name}" for a component with no trace, and raises „No valid predictions found for any module." if no selected component has any (gepa_utils.py:434-441). [api|trap] (verified: source read)
- **Champion/challenger promotion (autodialectics)** — `promote(champion, challenger, canaries_passed)` over `(score, slop)` pairs: canary failed → no; challenger slop > champion slop → no; challenger score ≤ champion score → no; else promote (ex:250-258). All three required (reference.md:146-150); keep the previous champion with `program.save(...)` so rollback is a file swap (reference.md:164-165). One measurement per side, no repeats, no floor. [recipe] (verified: dry-run asserts `promote((0.6,0.3),(0.7,0.2),True)` and rejects `(0.7,0.4)`) → here: `baseline.py compare` already fails below a floor and on a `vetoed` row; pairs.py's canary veto is the canary rule
- **Tier-2 plan metric (reference only)** — `plan_metric`: `terms = salient_terms(gold.failure_focus)` (words > 3 chars, deduped), `coverage = hits / max(len(terms),1)`, `verifies = any(k in plan for k in ("verify","verification","test","evidence","check"))`, `score = min(0.15 + 0.6·coverage + 0.25·verifies, 1.0)`; feedback „Explicitly address: …" when coverage < 0.6, „Add concrete verification, testing or evidence-checking steps." when not verifies; end-to-end metric `0.4·plan_metric + 0.6·slop_score`; `failure_focus` = the champion's previous slop feedback on the example (reference.md:126-144). Not in the example. [recipe|claim]
- **Folding a gate metric into a pipeline metric** — clarify: weight ≥ 0.3 „so that clarity cannot be traded for throughput" (SKILL.md:126-128); corrections: weight ≥ 0.3 „so learned corrections cannot be traded away for other axes" (reflect reference.md:112-114). [recipe]
- **LM judges sit above deterministic floors** — wiki-compile: „the judge may sit on top of these axes, never below them" (SKILL.md:123); tetraframe: a `JudgeRun` signature, take the minimum of judge and heuristic (reference.md:152-155); clarify: a paraphrase judge as a seventh axis with weight ≤ 0.2, lexical axes kept as floors, never lower the meaning-kept weight (reference.md:93-95, 109). [recipe]
- **MEDIUM approvals feed bootstrap stages** — approvals become positive demos for `BootstrapFewShot` / `BetterTogether(bootstrap=…)`; LOW observations are logged only (reflect SKILL.md:111-113, reference.md:105-110). [recipe]
- **Meta-learning replaced by GEPA** — the original's per-pattern acceptance statuses `insufficient_data (<5)`, `deprecated (<0.20)`, `needs_review (<0.5)`, `healthy`, `excellent (≥0.80)` and `--use-meta` deltas (+0.1 / −0.15…−0.3) become gold for the extractor (reflect reference.md:118-127). [number|claim]

### MET

- **Contract shared by all eight metrics** — `metric(gold, pred, trace=None, pred_name=None, pred_trace=None) -> dspy.Prediction(score=float, feedback=str)`: `compile_metric` (wiki-compile ex:224), `judge_metric` (adversarial ex:103), `clarify_metric` (clarify ex:70), `tetraframe_metric` (tetraframe ex:227), `harness_metric` (autodialectics ex:322), `refine_metric` (deep-refine ex:219), `corrections_metric`, `reflector_metric` (reflect ex:104, 114). None uses `pred_name`/`pred_trace`; blame is carried by the feedback wording only. [api] (verified: dry-runs call each)
- **Reward functions are a different contract** — `reward_fn(args: dict, pred) -> float` for `BestOfN`/`Refine`: `transform_reward` (tetraframe ex:220-224), `review_reward(...)(args, pred)` = review score / 10 (adversarial ex:170-176). [api]
- **compile_metric (wiki-compile)** — weights `{"citations": 0.30, "decisions": 0.25, "merge": 0.20, "diffs": 0.15, "links": 0.10}` (ex:34); citations = `1 − bad/all` over every claim citation and every concept citation, `0.0` if there are none (ex:166-170); decisions = mean of `decision_legal` (ex:173-181); merge = per concept mean of four checks — sources ⊆ batch and distinct, ≥ 1 citation, every disagreement has ≥ 2 distinct sources, `status == "contradicted"` iff some disagreement is `pending` (ex:184-198); diffs = per existing page 0/1 on `diff_consistent` (ex:201-208); links = per concept mean of "known entities linked" and `language_kept` (ex:211-221); score rounded to 3 places (ex:235-237). Fixture 1.0, broken fixture 0.657 (verified: dry-run). Weights are also in SKILL.md:85-91 and reference.md:57-58. [number]
- **compile_metric feedback templates** — `citation does not resolve: {file}:{start}-{end} {quote[:30]!r}`; `illegal decision: {action} on {slug} (status {status or 'absent'}, conflicts {conflicts})`; `{slug}: a disagreement needs two distinct sources`; `{slug}: status {status} does not match its pending disagreements`; `{slug}: sources outside the batch or no citation`; `{slug}: challenged item without a conflict: {x!r}`; `{slug}: 'new' item already on the page: {x!r}`; `{slug}: known entities not linked: [...]`; `{slug}: definition is not in the source language ({language})`; clean: `cited, legally decided, merged across sources, consistent diff` (ex:169, 179-180, 193-197, 144-146, 207, 218-220, 237; reference.md:60-72). [pattern]
- **judge_metric (adversarial)** — score = `round(0.5·F1(overstated quotes) + 0.5·F1(unsupported), 3)`; matching normalises whitespace and case and counts a hit when either string contains the other (ex:81-100); F1 is 1.0 when both lists are empty, 0.0 when only one is (probe A6). Feedback: `missed overstated claims: [...]`, `flagged supported claims as overstated: [...]`, `missed unsupported claims: [...]`, `flagged cited claims as unsupported: [...]`, clean `every overstated and unsupported claim found, none invented` (ex:111-121). Exact fixture 1.0, sloppy review 0.0 (verified: dry-run). See T10. [number]
- **clarify_metric (clarify)** — weights 0.30 meaning · 0.15 scope · 0.15 hedges · 0.15 bindings · 0.15 questions · 0.10 language (ex:130). Meaning = `1 − min(1, 0.5·new_terms + 0.5·dropped_entities + 0.5·new_quantifiers)` where new_terms = glossary slugs present (substring, case-folded) in the output but absent from claim+excerpt+context, dropped = gold entities neither in the output nor bound, new_quantifiers = space-delimited `QUANTIFIERS` in the output minus those in the context (ex:80-91). Scope = 0/1: every non-`unspecified` scope value is a substring of the context (ex:93-98). Hedges = 0/1: no undeclared hedge and hedge count not increased (ex:100-106). Bindings = 0/1: every slug in the glossary (ex:108-112). Questions = 0/1: every question ends with "?" and `(verdict != "clear") == bool(ambiguities)` (ex:114-121). Language = 0 if the claim has German function words `{der, die, das, und, nicht, wird, ist}` and the output English ones `{the, and, is, not}` (ex:123-128). Dry-run: good 1.00, asks 1.00, bad 0.25. [number] (verified: dry-run)
- **clarify feedback templates** — „Introduced terms absent from the source: […]." / „Dropped entities: […]." / „Added quantifiers the source does not state: […]." / „Scope values not found in the source: […]; use 'unspecified'." / „Hedges left unresolved and undeclared: […]; resolve from the source or list them as ambiguities." / „Bindings to unknown glossary slugs: […]." / „Ambiguities without a question: […]." / „Verdict inconsistent with the ambiguity list ('clear' needs an empty list)." / „The claim was translated; keep the source language." / clean „Clarified without adding or losing meaning." (ex:86-131; reference.md:73-80). [pattern]
- **clarify marker lists** — `HEDGES = ("irgendwie","meist","meistens","wohl","vielleicht","ungefähr","manchmal","eigentlich","somehow","probably","maybe","roughly","sometimes","kind of","sort of")`; `QUANTIFIERS = ("alle","jede","jeder","jedes","immer","nie","niemals","kein","keine","nur","all","every","always","never","only")` (ex:23-26; reference.md:66-71). [number]
- **tetraframe verification suite** — seven deterministic checks with thresholds `branch_independence 0.90, rigor_of_both 0.78, rigor_of_neither 0.78, contradiction_honesty 0.75, transformation_quality 0.82, fake_novelty_risk 0.70, slop_risk 0.70` (ex:40-41). Formulas: branch = `1 − min(1, 0.6·mean(max(0, sim(residual_a, residual_b) − 0.35)))` over (P,not-P), (P,neither), (not-P,neither) on `core_claim` with seed tokens removed (ex:168-172); both = mean(basis ∈ BOTH_BASES, co-hold word in explanation ["both","co-hold","simult","split"] else 0.5, scope conditions present else 0.5, falsifier quality) − 0.4 if a compromise phrase is in `strongest_case` (ex:153-157); neither = mean(basis ∈ NEITHER_FAILURES, replacement predicate present, explanation ≥ 8 words else 0.5, falsifier quality) − 0.3 if "it depends" (ex:160-165); falsifier quality = mean over falsifiers of 1.0 (≥ 5 words) or 0.5, 0.0 if none (ex:147-150); contradiction honesty = `min(1, 0.4 + 0.1·|contradictions| + 0.05·|discriminators|)`, else 0.35 with complementarities, 0.25 with nothing (ex:184-187); transformation = `min(1, mean(5 lists non-empty) + 0.3·(1 − sim(P*, P ∪ not-P patched claims)))` then − 0.4 for compromise language (ex:175-181); fake novelty = `1 − min(0.6, 0.08·n)` for P* tokens > 4 chars found in no corner, invariant or survivor list (ex:190-198); slop = `1 − 3·ratio` of MUSH tokens in P* frame and patched claims (ex:201-205). Fixture: `{branch 1.0, both 1.0, neither 1.0, contradiction 0.8, transformation 1.0, novelty 1.0, slop 1.0}`; a compromise P* → transformation 0.60 (verified: dry-run). [number]
- **tetraframe metric and feedback** — `score = mean(verify(run).values()) × 0.5 if any gold.banned_transformed_phrases occurs in P*`, rounded to 3; feedback `"{check} {score:.2f} < {threshold:.2f}"` per failing check joined with "; ", plus `P* uses banned phrases [...]`, clean `independent corners, rigorous both/neither, transformed P*` (ex:227-237; reference.md:142-148). The metric is a mean, the thresholds only name deficits — see T24. [number]
- **tetraframe's documented deviation** — `transformation_quality` caps at 1.0 *before* the compromise penalty, so a compromise P* with all lists filled scores 0.60 instead of upstream's 0.88 (reference.md:110-112; ex:180 comment "cap BEFORE the penalty"). [pattern] (verified: dry-run 0.60)
- **autodialectics slop score** — twelve dimensions clamped to [0,1], `composite = Σ w·v / Σ w`, `score = 1 − composite`, feedback = every dimension > 0.3 as `"{name} {value:.2f}"`, highest first, joined "; ", or „No slop dimension above threshold." (ex:207-216). Weights: verbosity_without_gain 0.12, repetition_without_progress 0.10, unsupported_claims 0.15, requirement_drift 0.10, fake_completion 0.15, self_verification_bias 0.08, and six at 0.05 — benchmark_gaming, shallow_novelty, context_contamination, refusal_to_surface_uncertainty, tool_abuse, synthesis_ignores_objections (ex:50-55; sum 1.00). Heuristics as coded: verbosity 0 below 200 words else `min(words/5000,1)·(1 − summary_words/words)`; repetition = mean(repeated-sentence ratio, repeated-trigram ratio); unsupported = claim-pattern hits (`(is|are) (the)? (best|only|proven)`, `studies show|it is known`, `clearly|obviously|certainly`, `it follows that|this means that`) not backed by an excerpt whose first 100 chars occur verbatim, `× (1 − uncertainties/claims)`; drift = `1 − (0.6·objective-keyword overlap + 0.4·constraint-keyword overlap)`; fake completion = mean of two flags (completion word without tests/patches; constraints but no declared uncertainties); self-verification = (self-verify phrases − tool-log test/verify entries)/phrases; benchmark gaming = 0.3 per `hard-?coded|overfit|optimized (specifically|just) to pass`; shallow novelty = novelty words not echoed in the summary; contamination = `(mean Jaccard(excerpt, output) − 0.3)/0.5`; refusal = `1 − hedges/(certain+hedges)`, × 0.3 if uncertainties declared, 0 when no certainty words and no declared uncertainties; tool abuse = "redundant"/"duplicate" log entries share; ignored objections = serious (severity > 0.5) objections whose keywords never appear (ex:169-204). Dry-run: sloppy slop 0.57, honest 0.05. [number] (verified: dry-run, probes AD2-AD8)
- **autodialectics run score and gate** — `run_score` = rubric-weighted mean of task_success (= criterion pass rate), groundedness (= 1 − unsupported), objection_coverage (= distinct disposition indices / objections, 1.0 with no objections), unsupported_assertion_rate (= 1 − unsupported), redundancy_rate (= 1 − repetition), novelty_usefulness (= 1 − (shallow + gaming)/2), requirement_fidelity (= 1 − drift), verification_quality (= pass rate) (ex:219-230). Base rubric 0.30/0.20/0.10/0.05/0.05/0.10/0.10/0.10; overrides code {task_success 0.35, verification_quality 0.15, groundedness 0.15, novelty_usefulness 0.05}, research {groundedness 0.30, task_success 0.20, objection_coverage 0.15}, experiment {verification_quality 0.20, groundedness 0.20, task_success 0.25} (ex:56-64; reference.md:54-65 — the table lists no writing/analysis overrides and the code has none). Gate in order: verdict fail and confidence < 0.3 → reject; slop > 0.7 → reject; verdict pass and score ≥ 0.6 and slop < 0.4 → accept; else revise (ex:65, 233-240). Dry-run: sloppy score 0.46 → **revise** (not reject), honest 0.95 → accept. [number] (verified: dry-run)
- **autodialectics end-to-end metric** — `harness_metric` = `run_score(contract, pred.checks, slop.dims, …)` halved when the gate says reject; feedback `gate={decision}; {slop feedback}` (ex:322-331). `pred.checks` come from the LM's `Verify` predictor, not from `criterion_checks` — see T32. [pattern]
- **autodialectics canary** — passes iff every `must_include` substring is present (text lower-cased, terms not), none of `must_not_include`, `slop ≤ max_slop` (0.6) and `groundedness ≥ min_groundedness` (0.2) (ex:243-247); example format `dspy.Example(contract=…, evidence_summary="...deliberately contradictory...", is_canary=True, must_include=["ambiguous","contradictory","uncertain"], must_not_include=["guaranteed","definitively","clearly established"], max_slop=0.6, min_groundedness=0.2).with_inputs("contract","evidence_summary")` (reference.md:152-160). [recipe]
- **refine_metric (deep-refine)** — early exit: 1.0 if `gold.answerable_at_hop0` else 0.0 with „Judged answerable at hop 0 but the base lacks the fact."; otherwise review the actions, apply the non-LOW ones to a copy of `gold.graph`, `answerable_now` = every `gold.expected_triples` triple present by label; `score = 0.6·answerable_now + 0.3·(1 − LOW/max(1,reviews)) + 0.1·(actions ≤ 5)`; feedback „{n} LOW-confidence action(s): {first warning}", „Expected triples still missing after applying non-LOW actions.", „More than 5 actions; prefer the minimal edit set.", clean „Minimal, grounded actions; question now answerable." (ex:219-238). Dry-run 0.90; no actions → 0.4 (probe DR4). The judge LM is not in the metric (reference.md:172-174). [number] (verified: dry-run, probe)
- **corrections_metric (reflect)** — over `str(pred.toDict()).lower()`: satisfied = expected empty or present; violated = forbidden present and not satisfied; score 0.0 violated / 1.0 satisfied / 0.5 neither; feedback = `gold.feedback` („User corrected this: {learning}") unless satisfied (ex:104-112). The comment explains the order: „the corrected form may contain the old one as a substring, e.g. "uv pip install"" (ex:107-108). [number] (verified: dry-run bad 0.0 good 1.0; probe R2)
- **reflector_metric (reflect)** — `score = (|got ∩ want| / max(1,|want|)) × (1 − noise/max(1,|signals|))` over exact lower-cased `(learning, confidence)` pairs, noise = signals whose learning was skipped before; feedback „Missed {fn} accepted learning(s)." / „{n} proposal(s) the user skipped before." (ex:114-125). See T43. [number]
- **Metrics that need no gold output** — clarify's metric reads only claim, excerpt, context, glossary and entities (reference.md:96-99 „the metric needs no gold clarification, which makes gold sets cheap"); compile_metric reads only sources, pages, known entities and language; tetraframe's reads only `banned_transformed_phrases` (reference.md:137-140). Reference-free metrics measure "violates nothing", never "did the job" — see T2, T19. [pattern]
- **Diagnosis tables worth keeping** — clarify failure modes: everything `clear` → gold with expected `needs-author`; near-miss slugs → pass exact slugs; scope always unspecified → cite a paragraph, not the line; rewrite in English → language axis (reference.md:101-109). deep-refine: every action LOW → demand `source::Name`; always early-exits → add `answerable_at_hop0 == False` golds; deletes unrelated triples → check deletions appear in `incorrectness`/`redundancy`; retrieval never widens → k-hop expansion, assert growth; apply corrupts views → stage → validate → swap (reference.md:176-184). reflect: same learning every session → consult ledger; corrections do not stick → weight ≥ 0.3 and store the failing input; extractor flags task instructions → add skipped examples; promotion pollutes → threshold ≥ 2 and human approval (reference.md:132-140). [recipe]

### DATA

- **Gold-set sizes stated per pattern** — wiki-compile: „Twenty to thirty sources with hand-checked claims, five of which must `flag` an existing reviewed page, and a handful of deliberately truncated bodies" (SKILL.md:110-111); adversarial: „forty claims, half overstated by construction" (reference.md:82); clarify: 20–40 claims, including `needs-author` cases (SKILL.md:124-126); tetraframe: 10–20 seeds with the expected predicate key phrase, admissible `both` bases, expected `neither` failure modes, banned P* phrases, including seeds whose answer is *neither* „so the optimizer does not learn that every debate has a winner" (SKILL.md:168-173); deep-refine: 20–40 real failed queries (SKILL.md:147-148); reflect: GEPA on the extractor after ≥ 5 reviewed sessions (reference.md:126-127). None measured in the repo. [claim]
- **Example shapes** — wiki-compile `dspy.Example(sources=…, pages=…, known_entities=…, language="de").with_inputs("sources","pages","known_entities")` (ex:363); adversarial `dspy.Example(artifact, evidence, overstated=[…], unsupported=[…]).with_inputs("artifact","evidence")` (ex:211); clarify `.with_inputs("claim_text","source_excerpt","entities","glossary_terms","canon_context")` (ex:169-173); deep-refine gold `question, graph, expected_triples, answerable_at_hop0` (reference.md:170-171) — its dry-run example has no `with_inputs` (ex:269-270); tetraframe metric example `dspy.Example(seed=…, banned_transformed_phrases=[…])` without `with_inputs` (ex:383); reflect `learning_to_example` (ex:99-102) and reflector gold `accepted=[{learning, confidence}], skipped=[learning]` (ex:166-167). [api]
- **Autodialectics trainset from past runs** — `dspy.Example(contract=…, evidence_summary=…, failure_focus="<what the slop feedback said>")` (SKILL.md:164-166). [recipe]
- **Corrections become training rows with their failing input** — a HIGH correction with the input that triggered it → `dspy.Example(inputs…, expected_behavior, forbidden_behavior, feedback)` appended to the program's trainset; an explicit "remember:" without input → shared instruction prefix or a synthetic example (reflect reference.md:103-110). [recipe] → here: `Plan/runs/judgements.jsonl` rows → `pairs.py`'s labelled pairs
- **Hard negatives by construction** — adversarial: half the claims overstated by construction; clarify: include expected `needs-author` claims; tetraframe: include *neither* seeds; deep-refine: include `answerable_at_hop0 == False` golds; wiki-compile: five sources that must `flag`, truncated bodies. [recipe]
- **Signal taxonomy for correction data** — HIGH correction („no, don't use X, use Y", „actually …", „instead of X … Y", „never/always …", DE „nein …", „verwende/benutze X statt Y", „immer/niemals …"); HIGH explicit („remember: …", „merk dir: …"); MEDIUM approval („yes, perfect/exactly/correct", „works perfectly", „good job on …"); LOW observation („have you considered …", „why not try …", „what about …"). False-positive rules: user turns only; approvals must follow an assistant turn; ignore messages under 10 characters; attribute only to programs used in the session (reflect reference.md:8-19). Target from the original: > 80 % precision, > 60 % recall at the signal level (reference.md:65-66). [number|claim]

### RLM

- **Long sources in wiki-compile** — „For sources above ~100k tokens, extract with `dspy.RLM` (`dspy-rlm-module`) and record `truncated: false`" (SKILL.md:114-115); keep `Citation` line ranges by giving the RLM the numbered text (reference.md:97-99). [recipe] → here: `rlm_ingest.py`, but with P26 — code, not the RLM, types the line (`find_line`)
- **Autodialectics context exploration** — `dspy.RLM` above ~8k chars, below that pass assets inline (SKILL.md:50); the original's RLM path was two `ChainOfThought` calls per segment, „which `dspy.RLM` subsumes" (reference.md:14). [claim]
- **Knowledge fence via RLM hooks (plan only)** — `PreIterationOutput.prompt_context` injected without execution and `post_iteration_hook` stopping on a violation, for „a character may only know what they have learned by that scene"; deferred because it patches private DSPy internals; pin DSPy and the hooks package together (plugin plan:197-207). [claim]

### RAG

- **Deep-refine retrieval contract** — `retrieve(question, hop, previous) -> list[Triple]`; hop 0 = lexical/semantic search; hop ≥ 1 = 1-hop neighbours of `previous`, optionally unioned with a fresh search; must widen, and `set(new) == set(previous)` may stop early with `retrieval_method = "exhausted"` (reference.md:95-103). Constants `MAX_HOPS = 4`, `INCREMENT_HOP = 1`, `BASE_TOP_K = 10`, `MAX_TRIPLE_NUM_BY_STEP = [5, 10, 15, 20]`, `HISTORY_HORIZON = 4`, `MAX_ACTIONS = 10` (reference.md:10-17); the example dedupes with `dict.fromkeys` and caps per step (ex:206). Dry-run widening 1 → 3 triples (verified). [number]
- **Retrieval before merge (wiki-compile extension)** — pass BM25 hits over existing concept pages into `MergeConcepts` as extra extractions with `source="wiki:<slug>"`, „so a new source merges into an existing concept instead of creating a twin" (reference.md:94-96). [recipe] → here: refused — reconciliation answers by lookup against `Wiki/index.json` and never reads page text, so the accumulated wiki cannot decide what a new document may say
- **Canon retriever seam (plugin plan)** — `CanonRetriever = Callable[[list[Claim]], str]` with default `no_canon_retrieval` returning "" „so nothing can conflict" (plugin plan:26-35); with it `CheckCanonConflict` „never fires and every ingest reports zero conflicts … it cannot contradict canon it never retrieved" (plugin plan:131-134). Fill it with `dspy.Embeddings` over canon + codex views, chunked per section, selected with MMR (scaffolding/kp_canon_retriever.py); order: build index → measure recall@k on a devset of claims whose canon location is known → enable; reversible by passing `no_canon_retrieval` (plugin plan:136-151). [recipe] → here: `graphrag.py` (PPR + MMR with a relevance floor) is the target's retrieval; the default-off seam is its injection pattern
- **Do not skip the recall measurement** — „An unmeasured retriever that returns plausible passages will make the conflict check look like it is working." (plugin plan:234). [pattern] → here: `graphrag.py bench` recall@8
- **D1 — index only author-locked text** — the canon index covers `Canon/` and the graph, not `Manuscript/`: „A chapter that is drafted but not revised is not yet true, and indexing it makes the retriever able to return a draft's own error as the canon a later draft is checked against. The error then reads as confirmed." (plugin plan:241-256). [pattern] → here: decision 006 makes every source equally in question, so the analogue is "retrieve only verified quotations", which graphrag already does
- **TARA's four dimensions without progressive leniency** — relevance (repair: reformulate from claim entities), coverage (retrieve per entity), specificity (pull the codex entry, not the chapter), sufficiency (raise an OpenQuestion instead of guessing); „Do not adopt the progressive leniency … a context scoring 27 out of 100 is accepted at retry 3. For a canon gate, the correct terminal state is an OpenQuestion, not a lowered bar." (plugin plan:175-195). [pattern] → here: P15 and `Wiki/questions/`
- **Learnings through a declared input field, default off** — `WithLearnings(inner, scopes, retrieve=no_learnings)`: „A declared input field, not a string prepend" (a `learnings: list[Learning]` field instead of mutating the longest string argument), off unless constructed, retrieval reuses the canon retriever („no reason for two retrieval stacks") (compounding plan:123-143). [pattern]

### AGENT

- **Deep-refine hop loop** — for step 1..max_hops: retrieve, dedupe, cap, judge; stop on the first `answerable=True`; `len(history) <= 1` → early exit with no abduction and no actions; else abduce over the last `HORIZON` steps and propose ≤ 10 actions (ex:203-217; reference.md:74-89). „refinement runs when `len(interaction_history) > 1`, not only when every judgement was `False`. A question answered at hop 2 still exposed a retrieval gap worth an edit." (reference.md:91-93). [pattern] (verified: DummyLM run reaches step 4)
- **Queue discipline** — refine the pending queue first: past queries with `refined != true`, deduplicated by `query_id = sha1(query)[:16]`, first-seen order; the current question only when the queue is empty; mark `refined = true` only after review (and approved apply) (reference.md:143-148). Doc only. [recipe] → here: `NOW.md` and `Wiki/questions/`
- **Dialectic plan loop** — `Thesis(contract, evidence_summary) → steps`; `Antithesis(contract, steps[, evidence_summary]) → objections: list[Objection(claim, objection, severity 0..1)]` („Severity 1.0 = the plan fails the contract, 0.3 = nit"); `Synthesis(contract, steps, objections) → dispositions: list[Disposition(objection_index, accepted, how)], revised_steps[, assumptions]` („Unaddressed objections with severity > 0.8 are failures"); executor; `Verify(contract, output) → checks` which never sees the plan (SKILL.md:86-135; ex:266-317). [pattern]
- **Reflect loop over a transcript** — iterate user turns that pass the pre-filter, find the prior assistant turn, extract a `LearningSignal`, keep `is_learning` ones (ex:65-68, 84-97); dry-run picks turns [2, 4] from the six-turn transcript and filters „ok" (verified). Auto-mode is an opt-in detached Stop hook with a lock file and `last-reflection.timestamp` (reference.md:99-101). [pattern]

### PROD

- **Judgement cache by content** — `digest(*parts) = sha256("\x1f".join(parts))[:16]` over `(artifact, evidence, difficulty, reviewer model)`; the cache lives on the module instance; persist as JSON keyed by digest when reviews are expensive (adversarial ex:77-78, 158-164; reference.md:45-53). See T12. [recipe]
- **Contract immutability** — `source_hash = sha256(json.dumps(task, sort_keys=True))`; „A run whose task hashes differently from its contract is a different run — never patch the contract in place" (autodialectics reference.md:50-52); lists normalised as user items first, domain defaults appended, duplicates removed (ex:122-135). Five common forbidden shortcuts always appended (ex:28-34). `max_repair_attempts` 3 for code, 1 otherwise (reference.md:52). Dry-run hash prefix `ad62eca5537d` for the demo task. [recipe] → here: the manifest's two checksums; a census frozen before the wiki is consulted
- **Apply with backup, validate, rollback, never commit** — reflect `apply`: back up the target (`<file>.<timestamp>.bak`), write, validate (JSON lines parse; pydantic for examples), roll back on error, log each decision to `meta/feedback-log.jsonl`, print the git command; „It never commits or pushes" (reference.md:95-101). deep-refine: stage → validate → swap on a copy, regenerate derived views on the copy, keep a backup of the pre-state and a checkpoint of the post-state (reference.md:138-141). [recipe] → here: the target commits one page per commit naming its source; a derived layer is re-derived, never repaired by hand (P25)
- **Ledger persistence** — JSONL (`.reflect/learnings.jsonl`) or SQLite, one row per fingerprint; context id `sha256(git remote origin url)[:12]`, fallback `sha256(cwd)`, or the program name (reflect reference.md:68-80). [recipe]
- **Three LM roles (D3)** — extractor = `worker` (`anthropic/claude-haiku-4-5`, temperature 0.0), judge = `task` (`anthropic/claude-opus-5`, 0.0), reflection = `reflection` (`anthropic/claude-opus-5`, 1.0), overridable per role through the environment (plugin plan:281-300; Legacy/tools/kpwiki/lm.py:6-8, 57-59, 131-133 confirm the defaults). „The separation is the point, not the model choice." (plugin plan:294). See T49. [pattern]
- **DSPy's default cache stays on in every live path** — none of the seven sets `cache=False`; repeats of the same input return the cached answer, and tetraframe's fixed `rollout_id=0..3` per corner make a rerun of the same seed a pure cache hit. Upstream's robustness check (same seed twice, agreement threshold 0.70; tetraframe reference.md:161-163) and clarify's "second-reader consistency" (run twice with different `rollout_id`s and diff the ambiguity sets; reference.md:88-90) only work with the cache off or offset ids. [trap] (verified: source read of the cache key) → here: `lmrun.py` already forces `cache=False` (P18)
- **Version contract between pack and consumer** — the plan made "the pack is validated against DSPy X" an explicit two-sided contract: whichever side moves first owes the other a notice; the pack moved to 3.3.1 first and recorded that KP's twelve DSPy symbols (`ChainOfThought`, `Evaluate`, `Example`, `InputField`, `LM`, `Module`, `OutputField`, `Predict`, `Prediction`, `Signature`, `configure`, `context`) did not change between 3.2.1 and 3.3.1 (plugin plan:70-88; CHANGELOG.md:58-66). `Legacy/requirements-dspy.txt` now pins `dspy==3.3.1` with that reasoning in its comment, so the bump was made before the reset. [claim] (verified: file read) → here: `check_dspy_surface.py`

### TEST

- **Dry-run shape used by all seven** — construct the program (LM construction does not touch the network, adversarial ex:210 „construction never hits the network"), score a hand-built good fixture (assert ≥ threshold), break it in named ways, assert the score falls and each defect's feedback substring appears (wiki-compile ex:365-380; adversarial ex:213-232; clarify ex:188-211; tetraframe ex:376-389; autodialectics ex:351-365; deep-refine ex:255-278; reflect ex:151-174), print `named_predictors()`. [recipe] (verified: all seven exit 0) → here: `selftest.py`'s "each case carries the exact defect the checker must name"
- **None of the dry-runs tests a degenerate prediction** — no dry-run feeds an empty or near-empty prediction, an empty quote, a one-word flag or an all-`clear` run; each defect in T1, T10, T19, T33 survives the shipped dry-runs. [trap] (verified: probes) → here: P5 plus the target's rule that a checker must be shown to fail
- **The pytest suite does not execute dry-runs** — `test_example_has_dry_run` only asserts the string `"--dry-run"` is in the source (tests/test_examples_parse.py:36-43); `test_every_skill_has_example` checks the same (tests/test_skill_correctness.py:265-280). The CHANGELOG's "all 33 dry-runs pass on 3.3.1" (CHANGELOG.md:93-97) was a manual run. [trap] (verified: 633 passed, read of tests)
- **Offline LM doubles for these patterns** — `dspy.utils.dummies.DummyLM(answers)` takes a list (consumed in order) or a dict keyed by a substring of the last message (lets one double answer several signatures); its `model` is `"dummy"` and kwargs `{temperature: 0.0, max_tokens: 1000}`, so two DummyLMs fail `same_lm`-style independence guards unless one's `model` is changed; `LM.copy()` shares the answer source (shallow copy) but resets `history` (verified: probe_refine). [recipe] → here: `lm_fixture.py` `FixtureLM`

### PAT

#### wiki-compile

- **Premise** — „raw sources are immutable, the LLM maintains the wiki, a schema is the contract" (SKILL.md:24-25); „The program returns drafts; writing them anywhere is the caller's separate, reviewed step." (SKILL.md:30-31). Sources: Karpathy bootstrap (layers, concept-table statuses, contradiction block with a `resolution` field, „open the page before citing it"), llm-wiki-agent (typed page kinds, post-ingest validation, health vs lint), llm-wiki-compiler (two-phase compile, `^[file:L-L]` citations, freshness by source hash), synthadoc (decision RULE 1/1b/2/2b/3, active-page protection, truncated flag, staged candidates), quicky-wiki (knowledge diff) (reference.md:3-11). [pattern]
- **Stages** — triage `TriageSource(source_name, text) → triage: Triage{tier, category, language, truncated}`; extract `ExtractClaims(source_name, numbered_text, known_entities) → claims: list[Claim]` („Never paraphrase into the quote; never add what the source does not say"); merge `MergeConcepts(extractions, known_entities) → concepts: list[ConceptDraft]` over the whole batch; decide `DecideIngest(page, concept) → decision: IngestDecision` („RULE 1 … RULE 1b … RULE 2 … List every conflict verbatim"); diff `KnowledgeDiff(page, concept) → diff: Diff`; answer `AnswerQuery(question, pages) → answer: Answer` („Answer from the given pages only, cite pages as [[slug]], name gaps"); health is a lint, not a predictor (SKILL.md:33-43; ex:245-293). All six are `ChainOfThought` (ex:298-303). `number_lines` renders `"{i}: {line}"`, 1-based (ex:118-119). [pattern]
- **Models** — `Citation{file, start ≥1, end ≥1, quote}` (1-based, inclusive); `Claim{text, citation, kind ∈ fact|definition|rule|event|opinion = "fact", entities}`; `Triage{tier, category, language, truncated=False}`; `Extraction{source, triage, claims}`; `PageState{slug, status, body}`; `Disagreement{topic, sources, positions, resolution="pending"}`; `ConceptDraft{slug, definition, sources, citations, disagreements, status}`; `IngestDecision{slug, action, rationale, conflicts}`; `Diff{reinforced, challenged, new, gaps}`; `Answer{text, cited_pages, confidence ∈ high|medium|low, gaps}`; `Compiled{extractions, concepts, decisions, diffs: dict[str, Diff]}` (ex:39-113; reference.md:13-28). [api]
- **Enums** — `Tier = primary · secondary · superseded · duplicate · out-of-scope` („replace with the domain's tiers; keep it closed"); `Action = flag · update · create` („`create` is decided in code"); `PageStatus = draft · reviewed · locked · contested · archived` („`reviewed` and `locked` are protected", `PROTECTED_STATUSES = ("reviewed","locked")`); `ConceptStatus = high-confidence · single-source · tentative · contradicted`; `Resolution = pending · supersedes · both-valid` („`pending` forces `ConceptStatus.contradicted`") (reference.md:30-38; ex:28-33). [api]
- **Legal decisions** — `decision_legal(d, page)`: no page → only `create` is legal; `create` on an existing page is illegal; `update` on a `reviewed`/`locked` page with non-empty `conflicts` is illegal; everything else is legal (ex:129-135). Rules encoded twice, in the signature docstring and in the metric: RULE 1 dispute → flag (challenged ⊆ conflicts); RULE 1b protected → flag, never update (scores 0); RULE 2 undisputed additions → update (`new` absent from the page); RULE 2b one entity's comprehensive profile → own page (prompt only); RULE 3 no page → create (code, not LM) (reference.md:40-48). See T4. [pattern] (verified: dry-run needle „illegal decision: update on juna")
- **Diff consistency** — challenged items must share a token (> 2 chars) with some conflict; `new` items must not already be substrings of the page body (ex:138-147). See T5. [pattern]
- **Rules** — 1 sources never modified; 2 extract everything before merging anything („A concept that appears in three sources is one draft with three sources, not three drafts"); 3 a reviewed page is authoritative, protected update scores 0; 4 the diff is the receipt, printed before anything is written, challenged maps to a conflict; 5 drafts go to a candidates area, promotion is a human step that pins the reviewed content hash, the program never writes pages; 6 health before lint (SKILL.md:93-106). [pattern]
- **Anti-patterns** — merging inside the extraction loop („the second source then overwrites the first"); letting the LM decide `create` („that is a lookup, not a judgement"); citations as page names („the lint can then prove nothing"); treating `flag` as failure („it is the moment the human learns something"); an LLM judge as the metric's floor (SKILL.md:117-123). [pattern]
- **Lint boundary** — outside the program, free: broken `[[links]]`, unindexed pages, orphans, sparse pages; required frontmatter and enum values, illegal lifecycle transitions; citation ranges against files on disk; stale sources by sha256, `truncated: true` warnings; candidates older than N days, promotion hash mismatch — „The program's metric proves the *draft* is right; the lint proves the *written page* still is." (reference.md:78-90). [pattern] → here: `state.py --prose`, `quotes.py`, `relations.py`, `graph.py`, `wiki_index.py`
- **Epistemic events** — turn each `Diff` into log lines `claim | <slug> | reinforced|challenged|new | by=<source>`: „no confidence decay, supersession is explicit"; batch merge and lint per ~25 sources (reference.md:100-104). [recipe] → here: `Wiki/compare/<doc>.md` is already the per-document record
- **Doc-vs-code gaps** — T1, T2, T3, T8, T9.
- **→ target: citation** — the pack's `Citation{file,start,end,quote}` lets the model type line numbers; the target's rule is P26 (the model quotes, `read.py --find` answers `^[Lnn]`), and its `quotes.py` normalises export escaping, emphasis, blockquote wrapping and cross-line quotes that the pack's literal substring check false-fails (T3). Keep the target's; adopt nothing here except the feedback template. [pattern]
- **→ target: merge** — `ConceptDraft.definition` (one merged definition sentence per concept) is exactly what P13 forbids: „Where two sources say different things about one term, the page holds both, attributed." The target equivalent of `MergeConcepts` is *gather*: attach each document's reading to the page with its `^[slug.md:Lnn]`, never a synthesised definition; `Disagreement` maps to a conflict record in `Wiki/conflicts/`, and `resolution` may only ever be `pending` for a program — `supersedes`/`both-valid` are the author's (decision 006: no date or self-declared canon retires another source). [pattern]
- **→ target: decide** — `create` by lookup is what `reconcile.py` already does against `Wiki/index.json` (68 of 109 candidates decided by lookup in document 6); `flag`/`update` correspond to "new conflict" / "new reading"; `decision_legal`'s protected statuses correspond to promoted pages in `Wiki/terms/`, which does not exist yet, so the rule has no instance today (P4) — record it as a demoted construct (`provisional`, `may not`, `retire when`) rather than build it. [pattern]
- **→ target: diff** — `reinforced / challenged / new / gaps` corresponds to the per-document table "new terms / new readings / new conflicts" in `Wiki/compare/`; `gaps` is the column the target lacks and maps to `Wiki/questions/` and P10's `MISSING`. [pattern]
- **→ target: metric** — every axis is P1-compatible, but the weighted sum violates P11 („Never collapse several checks into one pass/fail bit"); the target should report each axis's own status and keep "no citations" as "not scored" (P15), not 0.70 (T1). [pattern]

#### adversarial-review

- **Premise** — „a second model reads what the first wrote and is only allowed to object" (SKILL.md:24-25); it reviews an *artifact* against *evidence* with a *different model*, as opposed to autodialectics which keeps a *program run* honest (SKILL.md:33-36). [pattern]
- **Signatures and models** — `ReviewArtifact(artifact, evidence, difficulty) → review: Review` with docstring „Review the artifact against the evidence only. Quote every overstated claim verbatim and say what evidence would be needed; list claims with no support in the evidence; score 1–10. 'hard' demands a citation for every factual sentence; 'adversarial' also attacks the framing and the omissions. Never propose replacement text." (ex:129-138); `CitationSupport(claim, span) → support: Support{verdict ∈ supported|partial|unsupported, reason}` (ex:140-145, 51-53); `Review{score int 1..10, overstated: list[Overstated{quote, why, evidence_needed}], unsupported: list[str], strengths, weaknesses}` (ex:37-48). `review` is `ChainOfThought`, `support` is `Predict` (ex:150-151). [api]
- **Difficulty is an instruction, never a threshold** — `standard`: flag unsupported claims and superlatives without comparison; `hard`: also demand a citation for every factual sentence; `adversarial`: also attack the framing (what the artifact implies) and the omissions (what the evidence says that the artifact leaves out) (reference.md:25-31). Anti-pattern: „Raising the threshold instead of the difficulty when a page "feels" weak." (SKILL.md:110). [pattern]
- **Independence guard** — `same_lm(a, b)`: identical object, or equal `.model` and equal `.kwargs`; `assert_independent(reviewer, writer)` raises „no writer LM configured; call dspy.configure(lm=...) for the writer first" when the writer is `None` and „reviewer must differ from the writer LM (…)" when `same_lm` (ex:58-69); called at the top of `forward` against `dspy.settings.lm` (ex:157). The doc concedes: „Two `dspy.LM` objects with the same model string but different `temperature` pass the guard; that is a weak independence and the skill says so." (reference.md:41-43). See T11. [pattern] (verified: dry-run + probe A3)
- **Demotion** — `demotion(review, demote_at=3)` → `"contested"` when `len(overstated) ≥ 3`, else `"keep"`; „a status change, never an edit" (ex:72-74; SKILL.md:45). Synthadoc's original demoted to `contradicted` (reference.md:7). See T15. [pattern]
- **Refine to a target** — `review_refine(writer, reviewer, evidence, rounds=3) = dspy.Refine(module=writer, N=rounds, reward_fn=review_reward(reviewer, evidence), threshold=0.8)`, reward = review score / 10, the writer's prediction must expose `.text` (ex:170-180; reference.md:55-65). See T13 for what Refine actually feeds back. [recipe]
- **Rules** — 1 reviewer ≠ writer, asserted at call time; same vendor with a different model is acceptable, a different vendor stronger; 2 the reviewer never proposes text; 3 demotion changes status, not content; 4 cache by content; 5 „Evidence is the only ground. What the reviewer knows from elsewhere is not a finding." (SKILL.md:95-104). [pattern]
- **Anti-patterns** — passing the writer's LM as reviewer „to save a config line; the guard exists because it happens"; letting the reviewer rewrite („that makes it a second writer with no reviewer"); raising the threshold instead of the difficulty; „Skipping the judge metric and calling the reviewer optimised because it finds more." (SKILL.md:106-111). [pattern]
- **Judge needs its own metric** — „a reviewer that flags everything scores low on precision, one that flags nothing scores low on recall. Without this metric an "adversarial" reviewer optimises toward harshness." (SKILL.md:88-93). [pattern]
- **Extensions** — citation pass over every `(claim, span)` pair with demotion on `unsupported` count too; a second vendor; record `(round, score)` pairs and stop on a plateau; a milestone red-team of `confidence: high` pages at `adversarial`, „demotions go to the human, never to auto-fix" (reference.md:85-94). [recipe]
- **→ target: what the reviewer may touch** — the target's conflict detection is never mechanised and P0 says promotion (and user-facing flags) are never a session's to make; so a reviewer here may only *direct attention*: its `overstated{quote, why, evidence_needed}` is a list of page sentences to re-read against their line, and `evidence_needed` names the next document. `demotion` must not change any page status (demotion to `contested` would also remove wiki-compile's protection, T4). [pattern]
- **→ target: judge metric** — `judge_metric` is P27 in shape (score the judge against human labels), and the labels already exist: `Plan/runs/judgements.jsonl` (68 human decisions) and the 12 conflict records. Replace its bidirectional-substring matching (T10) with line identity — a flagged item is a `^[slug.md:Lnn]` produced by `read.py --find`, compared by line. [pattern] → here: `pairs.py` (canaries), `judgements.py`
- **→ target: independence** — useful where a second model gives a second opinion on a near match (the typesafe/Jev skill), with `lmrun.py` approval; compare LMs on model string alone (T11), and remember the D3 contradiction (T49). [pattern]

#### clarify

- **Premise** — transposes `Hmbown/clarify` (reveal intent, make the implicit explicit, add nothing, remove noise, never change behaviour) from code to statements: „It does not decide anything the source does not decide — that is the whole point: precision by *asking*, not by guessing." (SKILL.md:14-22). Rule mapping code → statement: rename → bindings; magic values → explicit `scope` only where the source states it; cryptic condition → `Ambiguity(phrase, readings, question)`; explicit assumptions → `assumptions[]`; comments explain why → `clarified_text` says what the source says; project standards → glossary, scope axes and language are inputs; avoid over-clarification → penalise added terms/quantifiers/scope; never change behaviour → "meaning kept" (0.30) (reference.md:9-20). [pattern]
- **Signature** — `ClarifyClaim(claim_text, source_excerpt, entities: list[str], glossary_terms: str, canon_context: str) → clarification: Clarification`, docstring „Rewrite the claim so that a reader with the glossary understands exactly what it asserts, and nothing more: make the scope explicit (world, act, character part) only where the source states it, bind names to glossary slugs, state implicit assumptions as assumptions, and turn every remaining ambiguity into a question for the author instead of choosing a reading. Never add, drop or generalise content; keep the source language." (ex:137-150); `ClarifyGate` wraps one `ChainOfThought` (ex:152-161). Inputs: claim and excerpt non-empty; entities, glossary and canon context may be empty, but an empty glossary makes the binding axis trivial (reference.md:52-60). [api]
- **Models** — `Ambiguity{phrase (verbatim), readings: list[str] min_length=2, question (ends with "?")}`, `Binding{mention, slug}`, `Scope{world, act, part = "unspecified"}` (domain axes: for a novel world/act/character part, for a codebase module/version/platform), `Clarification{clarified_text, scope, assumptions, ambiguities, bindings, verdict}` (ex:30-53; SKILL.md:85-87). [api]
- **Verdicts** — `clear` is the only verdict that may propose promotion; `needs-author` goes to the question list („its questions are the deliverable"); `not-promotable` is for inputs that are not claims (instructions, questions, fragments) or that contradict their own citation, and never proposes promotion (SKILL.md:26-31, 110-112; reference.md:48-50). See T18. [pattern]
- **Rules** — questions are not answered by the model („A second call with the same input must not resolve an ambiguity the first call raised; only the human (or a source passage) does"); bindings only to the passed glossary; assumptions go to `assumptions`, never into `clarified_text`; dry-run first — writing is the caller's step (SKILL.md:108-120). [pattern]
- **Anti-patterns** — letting the gate "fix" the claim from canon context („context is for binding names and detecting conflicts, not for rewriting what the source says"); domain-free scope; treating hedges as noise to delete („a hedge the source uses is meaning"); running the gate after promotion („it is a gate, not a linter"); skipping the glossary (SKILL.md:130-137). [pattern]
- **Where it plugs in** — research → canon promotion; the Initialize step of context-heavy work; before refining a knowledge base for a failing query; when a correction enters reflect-loop (SKILL.md:24-31). [pattern]
- **Doc-vs-code gaps** — T16, T17, T18, T19.
- **→ target: where the gate sits** — the target has no rewrite step: pages quote (P12), and a model never types an identifier (P26). So `clarified_text` has no place on a page. What maps is the *verdict and the questions*: `needs-author` → an entry under the author-questions heading of `NOW.md` or a `Wiki/questions/` page, `not-promotable` → stays in the note, `clear` → may be *proposed* (P0: promotion is the author's). The deterministic "no new quantifier / no smuggled slug / scope only where the source states it" checks are worth porting as checks over a model's *proposal text*, with word-boundary matching (T16). [pattern]
- **→ target: scope and glossary** — scope axes map to the novel's Kernwelten (KW1–KW4), chapters (Kap 1–39) and the Alters; bindings map to the slugs and surfaces in `Wiki/index.json` (exact match, as the metric requires). Hedge counting already exists in the target's reading of document 5 (163 hedging words in 13,947). [pattern]

#### tetraframe

- **Premise** — the method „refuses the two lazy outcomes of a debate: picking a side and splitting the difference"; „The output is never a decision. It is the strongest possible material for one: four hardened positions, their contradictions, the evidence that would discriminate between them, and a candidate reframing with operational tests." (SKILL.md:15-24). Upstream has ten stages, a `CornerInputView` with a blocked-field list, pairwise plus global cartography, BestOfN transformer, eight-check `VerificationSuite`; the skill folds them into six predictors (reference.md:3-19). [pattern]
- **Signatures** — `DistillSeed(seed) → distilled: Distilled{normalized_seed, stakes, constraints, hidden_assumptions, candidate_predicates, frame_risk_score 0..1 ("high when the seed bundles objectives"), evaluation_criteria}`; `SelectPredicate(distilled) → selection: Selection{primary_predicate, rejected, rationale}` („Choose one operational, falsifiable primary predicate"); `GenerateCorner(view: CornerView) → corner: Corner` with subclasses `CornerP` („basis_label must be 'affirmation'"), `CornerNotP` („'rejection'"), `CornerBoth`, `CornerNeither`; `MapCorners(corners) → cartography: Cartography{contradiction_map, complementarity_map, discriminators, invariants, arbiter_notes}` („without adding premises"); `Transform(primary_predicate, corners, cartography) → frame: Frame{transformed_predicate, transformed_frame, survivors_from_p, survivors_from_not_p, hidden_structure_from_both, dissolved_false_frame_from_neither, operational_tests}` (ex:44-111, 245-293). `Corner{mode, core_claim, strongest_case, scope_conditions, evidence_needs, unique_signal, basis_label, basis_explanation, replacement_predicate, patched_claim, minimal_falsifiers, confidence_score 0..1 = 0.5}` (ex:72-84). [api]
- **Closed vocabularies** — both: `temporal_split, scale_split, role_split, ontology_split, context_split, layered_causality, admissible_paradox`; neither: `category_error, false_binary, overloaded_predicate, missing_latent_variable, bad_ontology, ill_posed_objective, frame_collapse_under_scrutiny`; P/not-P: `affirmation`/`rejection`; compromise phrases `middle ground, balanced approach, split the difference, on the one hand, on the other hand`; mush words `balanced, nuanced, important, helpful, complex, thoughtful, consider, various, multiple`; upstream's eight pairwise relation types `support, contradiction, complementarity, paradox, category_error, frame_dependency, evidence_discriminator, scale_dependency` (not ported) (ex:27-33; reference.md:62-77). [api]
- **Corner contracts** — P: „Strongest clean affirmation of the predicate. No compromise, no mention of other corners."; not-P: „Strongest clean rejection, inversion or dismantling of the predicate. No mere surface negation."; both: „Valid only when P and not-P co-hold under a typed split or an admissible paradox."; neither: „Valid only when the predicate is misframed and replaced by a better predicate or frame." (ex:34-39). [pattern]
- **Isolation and sampling** — each corner sees only a `CornerView` (seed, stakes, constraints, hidden assumptions, primary predicate, evaluation criteria, contract) and runs under `dspy.context(lm=lm.copy(rollout_id=i, temperature=0.9 if mode in ("both","neither") else 0.7))`; the transformer is `dspy.BestOfN(module=ChainOfThought(Transform), N=3, reward_fn=transform_reward, threshold=0.84)` (ex:305-324). Providers that strip both rollout id and temperature (a CLI-backed LM) „rely on the contract docstrings alone — verify `branch_independence` more strictly there" (reference.md:89-93). See T20, T22, T25. [pattern]
- **Rules** — 1 the run is not the decision (present corners, map and P*, record the human's choice separately and cite the run); 2 „A failed check blocks the run, not the decision. Re-run with a sharper seed or stronger anti-collapse hints; never edit a corner by hand to pass verification."; 3 one predicate per run (bundled seeds → high `frame_risk_score`, split and run twice); 4 P* must be testable (`operational_tests`, `minimal_falsifiers` are what the decision record inherits; „a P* without them is a slogan"); 5 dry-run first (SKILL.md:151-164). [pattern]
- **Anti-patterns** — passing other corners "for context" („the model will otherwise write four paragraphs of one essay"); *both* as "a bit of each" („the honest *both* corner has low confidence and says so"); lowering thresholds („the thresholds are the method"); seeds that are plans or requests; P* introducing a noun no corner produced (SKILL.md:175-184). [pattern]
- **Where it plugs in** — question → decision record; knowledge-base change "page A should replace page B"; promotion with conflict (clarify `needs-author`, relation *contradicts*) — „the conflict page lists the discriminating evidence to fetch next"; a plan bundling two goals. Run clarify on a vague seed first (SKILL.md:26-36). [pattern]
- **Doc-vs-code gaps** — T20–T26; Legacy's own port had regeneration and a German-aware tokenizer (T21, T22).
- **→ target: a conflict record, not a metric** — C6 (two Guardians vs five) or C11 (Landauer warmth) are exactly "contested decisions with two camps". The *shape* maps well onto a conflict record: P/not-P = the two sources' readings, attributed; *both* = a typed split the sources themselves state (document 11 puts the character bible's Kap-33 garden down as Juna's *effect* and her appearance in Kap 38 — a `temporal_split` of C7); *neither* = "the conflict is misframed" (P14); `discriminators` = which unread document would settle it. The output stays a discussion item (decision 006). [pattern]
- **→ target: do not optimise on it** — `contradiction_honesty` scores more contradictions higher (T23), which is the direction P14 and the retired `Zero-Trust` false conflict warn against; the suite is English-tokenised (T21). Any port must be German-aware and must not reward the count of conflicts. [pattern]

#### autodialectics

- **Premise** — ports the control loop of `autodialectics` (immutable contracts, evidence, dialectical planning, domain execution, independent verification, slop scoring, gate, champion/challenger), not the product (CLI, REST API, MCP server, CLI gateways, SQLite store, sandbox); „every stage that was a prompt string plus a regex parser becomes a typed Signature, and every stage that was a heuristic stays a deterministic function that returns `dspy.Prediction(score, feedback)` — so the slop scorer is both the runtime gate and the GEPA metric." (SKILL.md:24-32; reference.md:9-23). [pattern]
- **Tiers** — 0: `compile_contract → slop_score → gate` on an output you already have, no LM calls; 1: `Dialectic` + `Verify` around your executor, 4 LM calls; 2: champion/challenger GEPA with canaries, „Do not load Tier 2 for a single run." (SKILL.md:34-43). [pattern]
- **Contract** — `Contract{source_hash, title, domain, objectives, constraints, acceptance_criteria, forbidden_shortcuts, rubric}`; domain inferred from keyword overlap (`code`: code, bug, function, test, implement, refactor, repo; `research`: research, literature, sources, cite, synthesize, papers; `writing`: draft, essay, argument, revise, prose, tone; `experiment`: experiment, hypothesis, protocol, ablation, measure; `analysis`: analyze, analysis, dataset, trend, interpret); per-domain default criteria (code: „All tests pass on the reference interpreter/platform.", „No regressions in existing functionality."; research: „Every factual claim cites a verifiable source.", „Contradictory evidence is acknowledged and discussed."; …) (ex:35-49, 70-78, 113-135; reference.md:39-48). Five common forbidden shortcuts: „Do not claim completion without verification evidence.", „Do not invent citations, logs, tests, files, or benchmark results.", „Do not silently rewrite objectives or constraints during the run.", „Do not suppress uncertainty when evidence is weak or conflicting.", „Do not treat scratchpad notes as canonical requirements." (ex:28-34). See T34. [pattern]
- **Deterministic verification backstop** — per acceptance criterion: keywords (> 3 chars, stripped of `.,;:()`) present ≥ `max(1, len(terms)//2)` and not negated, where negated = every sentence mentioning ≥ 50 % of the criterion's keywords contains a marker from `("did not","didn't","does not","cannot","unable","without","missing","fail","not ","no ")` (ex:67, 138-153). Verdict pass iff every check passes; confidence = passed/total (reference.md:82). Independent findings the original adds: constraints without declared uncertainties; completion claimed without tests, patches or files; empty output with status "completed" (reference.md:83-85; not in the example). See T29. [pattern]
- **Anti-patterns** — parsing "Claim / Objection / Severity" from free text („the original needed four regex styles"); letting `Verify` see the thesis or synthesis („that is self-verification"); reading `slop_score` as a number („its feedback is the GEPA signal; log it"); re-compiling the contract mid-run („compare `source_hash`; a changed task is a new run"); Tier 2 for one-off work; „Treating "no objections" as coverage 1.0 without checking that the antithesis actually ran (the original's parser-gap bug)." (SKILL.md:176-183). The reference keeps the parser-gap rule: „an antithesis that returns an empty list on a non-trivial contract is a finding, not a pass" (reference.md:67-71). See T31. [pattern]
- **Canary rule** — „A challenger that "wins" by sounding confident fails the canary and is not promoted." (SKILL.md:172-174). [pattern]
- **Doc-vs-code gaps** — T27–T35.
- **→ target: which parts carry** — the contract hash is the target's census-frozen-first rule in another form; `Verify` seeing only contract + output is what `quotes.py`/`read.py` do deterministically (P1: a model is not the verifier where code can be); `fake_completion` and `self_verification_bias` are P24 ("done is a measurement") and `selftest.py` (a check must be shown to fail); `promote` + canaries is `baseline.py compare` + pairs.py's never-merge canaries, which are stricter (a floor, a `vetoed` row). Nothing in the twelve English regex heuristics applies to German corpus text. [pattern]

#### deep-refine

- **Premise** — „DeepRefine treats a question the knowledge base cannot answer as a *defect in the base*, not in the prompt: it retrieves wider, judges again, abduces the error, proposes minimal edits, and applies them only after evidence review and explicit approval." (SKILL.md:13-21). [pattern]
- **Signatures** — `JudgeAnswerable(question, triples: str) → answerable: bool` („Decide whether the question is answerable from the given triples alone"; CoT); `AbduceErrors(question, interaction_history) → abduction: Abduction{incompleteness ("facts or links the base lacks"), incorrectness ("wrong or conflicting triples"), redundancy ("duplicates that confuse retrieval")}` („Cite the triples or gaps you mean; do not propose edits"; CoT); `ProposeRefinements(question, triples, abduction) → actions: list[RefinementAction{kind ∈ insert_edge|delete_edge|replace_node, args 2..3}]` („at most 10 minimal actions … never delete unrelated triples; use source-qualified node names ('file.md::Name') whenever a bare name is ambiguous"; Predict) (SKILL.md:46-75; ex:168-190, 198-200). The three original tagged prompts (`<judge>`, `<abduction>`, `<refinement>`) became typed fields „so no tag parsing exists anywhere" (reference.md:62-72). [api]
- **Evidence review** — per entity argument (indices 0 and 2, or 0 and 1 for `replace_node`): match nodes by id/label/alias case-folded, `src::Name` qualifies by source suffix; warnings (each forces LOW): bare name in the ambiguous set, name matching > 1 node, no evidence at all; evidence: „Node exists: …", „Exact edge already exists.", „Both endpoint nodes exist; relation inferred by the loop.", „Replacement source node exists."; confidence: any warning → LOW; else "Exact edge"/"Replacement source" evidence → HIGH; else any evidence → MEDIUM; else LOW with „No node or edge evidence found." (ex:62-112; reference.md:105-126). Dry-run labels `[MEDIUM, HIGH, LOW]` (verified). See T36, T38. [pattern]
- **Apply gate** — `apply_actions(graph, reviews, *, allow_low=False)` returns a deep copy, refuses LOW unless `allow_low`, inserts nodes as `deeprefine_<name>` with `source="deeprefine"`, deletes only exact edges, relabels for `replace_node` (ex:119-152); „`apply_actions` … **never called by the module**" (SKILL.md:32); „A generated action list, a valid trace, or a successful review is **not** approval." (SKILL.md:121-122); `allow_low=True` only when the user's approval explicitly accepts that risk (SKILL.md:120-121). See T37. [pattern] (verified: dry-run asserts the input graph keeps 2 edges, the copy gets 3)
- **Trace schema** — `LoopTrace{schema_version=1, query, query_id = sha1(query)[:16], constants, interaction_history: list[Step{step, num_hops, base_top_k=10, query, retrieval_method ∈ search|k_hop_expansion|search+k_hop_expansion, retrieved_subgraph, answerable}], abduction, actions, early_exit}`; `validate_trace` checks judgement per hop, stop condition, `num_hops == (step−1)·INCREMENT_HOP`, caps, `early_exit == (len(history) ≤ 1)` with no abduction/actions, abduction non-empty on at least one axis, actions only with abduction, ≤ 10 actions (reference.md:25-60, 150-159). Not implemented — T40. [pattern]
- **Anti-patterns** — applying inside `forward()`; skipping abduction („abduction is what the metric and GEPA reason about"); free-text actions („the closed `kind` enum plus argument count is what keeps `apply_actions` safe"); refining only the latest question; judging with the same triples every hop („assert the retrieved set changes or stop early"); treating the review as approval (SKILL.md:162-169). [pattern]
- **Doc-vs-code gaps** — T36–T41.
- **→ target: the loop's three axes** — the target already has the premise: a question the wiki cannot answer names its own next document. Map abduction's axes onto the target's three records, never onto graph edits: *incompleteness* → a `Wiki/questions/` page naming the unread document (entity lists route a question to unread documents that name it, with the line); *incorrectness* → a conflict record (never resolved by the loop, P13/P14); *redundancy* → a one-term-or-two judgement for `pairs.py`/`judgements.jsonl`. [pattern]
- **→ target: the actions are forbidden** — `insert_edge` is an inferred link (decision 005: „A link is never inferred"; the graph is derived from `[[…]]` and citations only); `replace_node` merges two surfaces or two entities (P13, and T36 shows it is graded HIGH); `delete_edge` edits a derived layer by hand (P25). The only transferable part is the refusal machinery: closed action enum, deterministic review, apply never called by the proposer, review ≠ approval. [pattern]
- **→ target: the metric** — `refine_metric`'s `expected_triples` check has a direct analogue in `graphrag.py bench` (17 cases labelled by the wiki itself, recall@8 42 % seeds / 64 % PPR): "does the question become answerable" is measured there by retrieval over verified quotations, not by applying edits. [pattern]

#### reflect-loop

- **Premise** — „a correction is not a markdown section to append — it is a **gold example plus feedback**" (SKILL.md:16-18); the skill is described as the human-feedback source of `reflect-loop → GEPA → deep-refine → rlm-workflow` (SKILL.md:20-21). [pattern]
- **Signature and model** — `ExtractLearningSignal(message, prior_assistant_turn, program_name) → signal: LearningSignal{is_learning, kind ∈ correction|approval|observation|explicit|None, confidence ∈ HIGH|MEDIUM|LOW|None, old_behavior, new_behavior, learning ("one actionable sentence, source language kept"), scope_hint ∈ program|project|global = "program", reasoning}` („Decide whether a user message contains a reusable learning for the program (not a one-off task instruction)… Works in any language; keep the learning in the user's language.") (SKILL.md:45-64; ex:32-39, 74-82 — the example drops `reasoning`). Ledger row `Learning{fingerprint, learning, kind, confidence, program, contexts, count=1, status ∈ pending|accepted|skipped|promoted, first_seen, last_seen}`; `ReviewDecision{fingerprint, decision ∈ accept|modify|skip|quit, modification}` (reference.md:37-53). [api]
- **Pre-filter** — a recall-tuned regex over user turns ≥ 10 chars: `(?i)\b(instead of|statt|don't|do not|never|niemals|always|immer|actually|nein,|no,|use \w+ instead|verwende|benutze|remember:|merk dir|perfect|exactly|genau so|works? (perfectly|great)|have you considered|why not)\b` (ex:23-28, 65-68); the original's semantic detector cost ~2–3 s per message, which is why it was opt-in (reference.md:59-66). See T42. [pattern]
- **Ledger and promotion** — `fingerprint = sha256(" ".join(learning.lower().split()))[:16]` (whitespace- and case-insensitive, verified probe R5); `record` upserts by fingerprint, appends a new context, increments count; `eligible_for_promotion(threshold=2)` = ≥ 2 contexts and not promoted (ex:42-62); promotion moves a learning from one program's trainset to the shared gold set or family instruction prefix, gated `preview → user approval → apply with a backup`, „never automatic" (SKILL.md:115-129). Dry-run: not eligible after one context, eligible after two, fingerprint `50f0f26ef96476c2` (verified). See T45. [pattern]
- **Safety** — dry-run by default; `review()` shows, `apply()` only after the user's explicit choice per signal; backups before every write, validation after, rollback on error; never auto-commit or push, print the command; lock/timestamp against double reflection; auto-mode opt-in; „Learnings stay in the user's language; nothing leaves the machine." (SKILL.md:153-162). [pattern]
- **Anti-patterns** — appending correction text to the docstring by hand („GEPA will overwrite or contradict it; give it the example + feedback instead"); treating every "yes" as an approval; „Promoting on first sight — threshold ≥ 2 contexts, then a human."; skipping the ledger („the same learning is re-proposed every session"); running the extractor over the whole transcript with the task LM (SKILL.md:164-170). [pattern]
- **Doc-vs-code gaps** — T42–T45.
- **→ target: the judgements ledger is this, already** — `Plan/runs/judgements.jsonl` records a person's decision about a near match with the two surfaces, the rule and whether code claims it, and `judgements.py` replays every row against current code (`agrees` / `DISAGREES` / `judgement`). That is `corrections_metric` done by identity instead of substring, over all history. What reflect-loop adds: (a) the rule text of a judgement is the GEPA feedback string for `pairs.py`'s model on the residual; (b) the fingerprint + contexts + threshold ≥ 2 is a promotion rule for a judgement to become mechanised (code claims it) — still a human step. [pattern] → here: `pairs.py`, `judgements.py`
- **→ target: corrections from the author** — the author's corrections arrive in German (decision 006 is quoted in German); the pre-filter's German alternatives `nein,` and `remember:`-style anchors never fire (T42). Nothing from a transcript may become a judgement without the author's yes (P0). [pattern]

#### The two Kohärenz-Protokoll plans

- **What they are** — `docs/kohaerenz-protokoll-plugin-plan.md` (v0.8.0, CHANGELOG.md:150-153) makes the pack the plugin repo of KP and ports six upstreams; `docs/compounding-wiki-extension-plan.md` (v0.9.0, CHANGELOG.md:122-126) adds a learnings layer. Both are "a plan, not a change" (plugin plan:3-6; compounding plan:3-4) and both end in author decisions D1–D6 recorded at v0.11.0 (CHANGELOG.md:74-91). They describe the target *before* its reset to two layers (decision 001). [claim]
- **Port verdicts (plugin plan:90-125)** — dspy-refrag: one file (`sensor_advanced.py`, MMR), vendored under MIT, „Nothing else" — fragment selection never shrinks the prompt, FAISS/Pinecone raise `NotImplementedError`, psycopg2 import, contradictory Weaviate pin; drg-kg: adopt as a dependency, proposal-only; TARA: port the pattern, not the code (licence file missing); dspy-rlm-hooks: adopt later, only with an RLM step; dspytools: do not port („Two systems of record for the same concern"); context-engineering book: do not port, cite. [pattern]
- **drg-kg rules (plugin plan:167-173)** — „Set `DRG_REQUIRE_LM=1`. Without it, a missing key returns an empty graph and a green run. A canon pipeline that silently ingests nothing is worse than one that fails." and keep `enable_implicit_relationships` off („inferred edges must not enter canon without passing the same gate as any other claim"); „It proposes; the author decides." [pattern] → here: decision 005, P15
- **Sequence (plugin plan:209-223)** — 1 declare dependency, equal pins; 2 vendor MMR („MMR beats plain top-k on a near-duplicate fixture"); 3 canon index + recall@k („Step 3 is where the real gain is"); 4 4D score („sufficiency routes to OpenQuestion"); 5 optimise `SourceIngest` („compiled beats baseline on a held-out set"); 6 DRG proposal-only; 7 RLM hooks if an RLM step exists. Each step independently valuable and revertible. [recipe]
- **What not to do (plugin plan:225-234)** — no writes to `Canon/` or the provenance graph without a D-xx decision; do not widen the codex `kind` enum from inside KP; do not adopt refrag as a package; do not copy TARA source; no FalkorDB, Redis or second skill graph; do not move either DSPy pin unilaterally; do not translate canon prose („claims quote the source language, which `metrics.py` already enforces with `language_kept`"); do not skip the recall measurement. [pattern]
- **D2 — enum growth belongs to its owner** — the codex `kind` enum `{concept, location, faction, artefact, minor-character}` grows by `rule, motif, theme, voice, character`, but in the agency engine, not KP; migration of ~600 entries from a `**Kategorie:**` body line must be idempotent against graph ground truth, and every parser must read both shapes while migration is in flight (plugin plan:257-279). [pattern]
- **Compounding finding** — „**The wiki already produces learnings. It has no path that reads them back.**" (compounding plan:15) — decision log, agent memory, lit-critic triage are written and read only by a human who remembers them (compounding plan:17-30). [pattern] → here: `Plan/decisions/001…006`, `Plan/learnings/`, `NOW.md` are the target's three
- **Upstream defects not to copy (compounding plan:54-67)** — a literal backslash-n in the injected context; similarity hard-coded to 0.9 with the `threshold` argument ignored; a field-name mismatch that stores auto-codified rows with empty title/content so dedup no-ops on them; README claims teleprompter optimisation that does not exist; README claims JSON storage (SQLite + vector index; verification checks the disabled format); `compounding work` edits the current branch in place, the worktree path calls a missing cleanup method (`AttributeError`); no LICENSE. „Take the architecture. Do not take the code." [trap|claim] (not verified: upstream not in this slice)
- **E1 — a typed Learning** — `LearningSource = Literal["decision-log","lit-critic","agent-memory","ingest","manual"]`, `LearningScope = Literal["canon","prose","process","tooling"]`, `Learning{id, source, scope, statement (English; quoted canon keeps its language), rationale, applies_to, citation: Citation ("a learning without a source does not exist"), supersedes="", status ∈ active|superseded|parked}`; stored as `Wiki/learnings/*.md` frontmatter, „Not a new database" (compounding plan:73-104, 212-213). [pattern]
- **E2 — importers, read-only, deterministic where possible** — decision-log table → learnings („the highest-value and lowest-risk piece … a parser, it needs no model"); one learning per *rejected* lit-critic finding; one per agent-memory bullet; nothing writes back (compounding plan:106-121). [pattern] → here: a parser over `Plan/decisions/*.md` needs no model
- **E4 + D5 — suppression is visible** — a gate checks whether an active learning already rejected a finding; if so it reports it in a *suppressed* section citing the learning id and it does not drive the exit code; „A suppressed finding never changes exit 0/1 silently; it changes it visibly." (compounding plan:145-153, 215-229). [pattern] → here: P23; `judgements.py` replay could annotate "already decided" instead of filtering
- **Measure whether it compounds** — „State it as a measurement before building, or the system will be believed rather than checked": repeat findings per review (should fall), suppression precision („a suppressed finding the author would have accepted is a regression, and the expensive error"), decisions re-litigated, learnings cited per ingest (zero means retrieval is not reaching the corpus) (compounding plan:179-193). [pattern]
- **D4, D6** — learnings are English (engineering artefact), quoted canon keeps its language (compounding plan:200-213); `MEMORY.md` stays hand-written, the layer imports from it and never writes back, one writer per file (compounding plan:231-245). [pattern] → here: CLAUDE.md's "canon prose is German and is never translated; engineering language is English"
- **Paths the plans name, checked in `/home/user/kohaerenzprotokoll` today** — absent at the named path and **parked under `Legacy/`** (read by nothing): `tools/kpwiki/` → `Legacy/tools/kpwiki/` (now 22 files, 6,655 lines, including `programs.py` with the `CanonRetriever` seam at :37, :59, :67, :203, `lm.py`, `schema.py`, `metrics.py` with `language_kept` at :81, and the pack's patterns as real modules: `compile_metric.py`, `clarify.py`, `clarify_metric.py`, `tetraframe.py`, `tetraframe_metric.py`); `requirements-dspy.txt` → `Legacy/requirements-dspy.txt` (pins `dspy==3.3.1`); `scripts/setup_dspy.sh`, `scripts/render_codex_views.py`, `lit_critic_gate.py`, `wiki_lint` → `Legacy/scripts/`; `Canon/`, `Codex/`, `Manuscript/` (incl. `ncp.json`, `ncp-b.json`) → `Legacy/…`; `Plan/drafting/decision-log*.md` → `Legacy/Plan/drafting/` (two files); `.claude/agent-memory/<agent>/MEMORY.md` → `Legacy/claude-config/agent-memory/` (three agents); `Plan/quality/lit-critic/` → only `Legacy/Plan-quality-lit-critic/README.md`. **Absent everywhere:** `.agency/session.db` (no `.agency` anywhere), `Plan/wiki/index/canon` (`Legacy/Plan/wiki/` exists without `index/`), `tools/kpwiki/selection.py` (step 2 never happened), `Wiki/learnings/` (E1 never built). `Plan/quality/` exists at top level but without `lit-critic/`. [number] (verified: ls/find)
- **The Legacy modules are richer than the pack's examples** — `Legacy/tools/kpwiki/compile_metric.py` has the axis `links_language` (:45), collapses whitespace so a quote across a line break matches (:54-56), zeroes merge when „no concepts merged although {n} claims were extracted" and folds in `gold_concepts` coverage (:243-253); `tetraframe.py:334, 370-383` regenerates near-duplicate corners (`max_corner_attempts=2`); `tetraframe_metric.py:28-34` detects content leakage between corners with `CROSS_REFERENCE_MARKERS` (`"other corner"`, `"p says"`, `"as above"`, `"die andere position"` …), adds `divergence_quality 0.45` and `robustness 0.70` to the thresholds, and tokenises `[a-zA-ZäöüÄÖÜß_]+`; `clarify_metric.py:18-23` has `gewissermaßen` in HEDGES and a named `WEIGHTS` dict. The pack's examples are compact reductions of code the target's predecessor ran. [claim] (verified: grep/sed of the Legacy files; not executed)

### SKILL

- **Corrections to a skill or program go in as data, not prose** — reflect-loop's rule for SKILL.md and program instructions alike: never hand-append "Critical Corrections"; turn the correction into a gold example plus a feedback sentence the metric emits whenever the old behaviour recurs, and let GEPA rewrite the instruction (SKILL.md:88-113, 166). [pattern] → here: job 4 (SKILL.md descriptions via `optimize_anything`) should take author corrections as cases with feedback, not as edits
- **Promotion of a learning across programs** — a learning seen in ≥ 2 contexts moves to the shared gold set or the family-level instruction prefix so every program in the family is optimised against it, after preview and approval (reflect SKILL.md:123-129). [recipe]
- **Frontmatter of the seven skills** — each frontmatter holds only `name`, `description`, `when_to_use`, consistent with the pack's forbidden-field test. [api] (verified: read)

### TRAP

- **T1 wiki-compile: an empty compile scores 0.70 and says "clean"** — `_mean([])` returns 1.0 (ex:161-163), so decisions, merge, diffs and links score 1.0 when there is nothing to judge; only citations return 0.0 for none (ex:170). An empty `Compiled` scores 0.70 with feedback „cited, legally decided, merged across sources, consistent diff"; one extraction with one claim quoting „Juna" and nothing merged or decided scores **1.0**. [trap] (verified: probe W P1, P2) → here: P15/P23 — report "not scored", never a number
- **T2 wiki-compile has no recall axis** — the metric never compares with expected claims or concepts although the gold set is to have „hand-checked claims" (SKILL.md:110); extracting one claim from a 100-line source is indistinguishable from extracting all. Legacy's version zeroed the merge axis when claims existed but no concept was merged and folded in `gold_concepts` coverage (Legacy/tools/kpwiki/compile_metric.py:243-253). [trap] (verified: read) → here: P10 `MISSING`
- **T3 `citation_resolves` accepts empty and one-character quotes** — `c.quote.strip() in "\n".join(lines[start-1:end])` (ex:122-126) is True for `""` and `"K"`; it is literal (a quote spanning a line break must contain `\n`; with a space it fails) and the model types `start`/`end`. [trap] (verified: probe W P3, P4) → here: `quotes.py` normalises and `read.py --find` supplies the line (P26)
- **T4 legality is self-reported** — `decision_legal` only fires when the model's own `conflicts` list is non-empty: `update` with `conflicts=[]` on a `reviewed` page is legal; `update` with conflicts on a `contested` page is legal; and adversarial-review's `demotion` produces exactly `contested`, so a model's demotion removes the protection. [trap] (verified: probe W P6, P6b) → here: the protected state must be decided by a person and checked against the page, not the model's claim
- **T5 "challenged ⊆ conflicts" is any shared word** — `_overlap` accepts any common token longer than 2 chars; „Kapitel 13 ist falsch" matches conflict „… ist strittig" through „ist" (ex:138-147). [trap] (verified: probe W P8)
- **T6 link check incompatible with alias links** — `unlinked_entities` requires the literal `[[Entity]]`: `[[aegis|AEGIS]]` and `[[aegis]]` + bare „AEGIS" are both reported unlinked, while one `[[AEGIS]]` hides any number of unlinked occurrences (ex:150-151). [trap] (verified: probe W P5) → here: `relations.py --unmarked`
- **T7 `language_kept` passes text with no markers** — `own >= other` so 0 ≥ 0 passes (a definition of names and numbers), ties pass, an unlisted language code always fails (ex:154-158). [trap] (verified: probe W P7) → here: P19 must also assert non-empty
- **T8 "deterministic" truncation guard is the model's boolean** — SKILL.md:37 lists „`truncated` recorded whenever a body was capped" as the deterministic guard, but nothing caps a body; `truncated` is whatever `TriageSource` outputs (ex:53-57, 306). [trap] (verified: read)
- **T9 `answer` is a dead predictor inside the optimised program** — see OPT; `named_predictors()` prints `answer.predict` (dry-run). [trap]
- **T10 judge_metric scores degenerate reviews 1.0** — bidirectional substring matching after normalisation (ex:85-90) makes an empty-string flag, a one-word flag („Kernwelten", „Kael"), or the whole artifact as one flag each score **1.0** with „every overstated and unsupported claim found, none invented". The precision/recall promise of SKILL.md:88-93 does not hold under optimisation. [trap] (verified: probe A1, A2, A2b)
- **T11 the independence guard compares the wrong things** — `same_lm` passes the same model string with a different temperature and `writer.copy(rollout_id=1)` (refuses only identical kwargs), and `assert_independent` checks `dspy.settings.lm`, not the LMs the writer's predictors actually carry — a writer set with `set_lm` is invisible to it (ex:58-69, 157). [trap] (verified: probe A3; read) → here: compare model strings, and compare against the writer module's `get_lm()`
- **T12 review cache ignores the reviewer's configuration** — the key is `(artifact, evidence, difficulty, reviewer model string)`; two reviewer configs with different kwargs share a key, and after GEPA rewrites `review.predict` the instance still returns pre-optimisation verdicts (ex:158-160). [trap] (verified: probe A4; DummyLM run: 1 reviewer call for 3 Refine rounds)
- **T13 `dspy.Refine` feeds the writer its own LM's advice, not the judge's findings** — adversarial reference.md:62-64 says „the writer learns from the judge, not from itself"; in 3.3.1 Refine's `OfferFeedback` runs on `dspy.settings.lm` — the writer — and receives the reward *number* and the reward function's source, never the review (refine.py:148-167). With DummyLMs: two feedback calls landed on the writer LM, the reviewer's reason string never appeared in them, `0.3` did. [trap] (verified: probe_refine)
- **T14 BestOfN/Refine hide total failure for N ≤ 2** — when every attempt raises, both print „… Attempt failed …" and return `None` for N = 1 or 2, and raise only on the third attempt for N = 3; `fail_count` is instance state decremented across calls (best_of_n.py:75-79, refine.py:170-174). Tetraframe's `self.transform(...).frame` would then fail with `AttributeError` on `None`. [trap] (verified: probe_failcount) → here: P15 — "never reached" must not look like an answer
- **T15 demotion ignores unsupported claims** — five unsupported and zero overstated → `keep` (ex:72-74); the extension point says to add it (reference.md:87-88). [trap] (verified: probe A5)
- **T16 clarify's quantifier and hedge detection is space-delimited** — `_present` looks for `" {m} "` in `" {text} "` (ex:61-63), so „nie." and „immer," are invisible: „AEGIS wird in Akt I beim Namen genannt, nie." scores **1.0** although it drops „nicht" and adds „nie". [trap] (verified: probe C1)
- **T17 clarify penalises a hedge increase silently** — the hedge axis is 0 when the count rose even if every hedge is declared, but feedback is only emitted for undeclared hedges (ex:100-106): an added, declared „vielleicht" scores 0.85 with „Clarified without adding or losing meaning." [trap] (verified: probe C2)
- **T18 `not-promotable` is scored as inconsistent** — the consistency check `(verdict != "clear") == bool(ambiguities)` fails a `not-promotable` verdict with no ambiguities (0.85) and the message talks about 'clear' (ex:116-121), contradicting „the metric does not score it differently" (reference.md:48-50). [trap] (verified: probe C3)
- **T19 clarify cannot tell "clarified" from "copied"** — an identity rewrite of a hedge-free claim with verdict `clear` scores 1.0; scope values „I" and „a" count as grounded (substring of the context); English → German rewriting is not caught (only German → English); the metric reads no gold clarification or expected verdict (reference.md:96-99), yet SKILL.md:124 asks for „a hand-written clarification each" and :125-126 says gold `needs-author` cases teach the optimizer — the metric cannot see them. [trap] (verified: probe C4, C5, C6)
- **T20 tetraframe's isolation guard cannot fire** — `assert_isolation` compares `view.model_dump()` keys with `CornerView.model_fields` (ex:131-134), but pydantic's default `extra="ignore"` drops unknown kwargs at construction, so the difference is always empty; leakage through a field's *content* (another corner's text in `hidden_assumptions`) passes too. Isolation holds only because each generator is a separate call with only the view. Legacy's port checked content instead, with cross-reference markers (Legacy/tools/kpwiki/tetraframe_metric.py:28-29). [trap] (verified: probe T1, T1b)
- **T21 tetraframe tokenises ASCII only** — `[a-zA-Z_]+` (ex:117) turns „Die Schöpfung hält Kernwelten zusammen" into `{die, kernwelten, pfung, sch, zusammen}`; `slop` uses `[a-zA-Z]+` and English MUSH words, so German filler scores slop 1.0. Every similarity-based check (branch independence, near duplicates, fake novelty, transformation overlap) is degraded on German. Legacy used `[a-zA-ZäöüÄÖÜß_]+`. [trap] (verified: probe T2, T7)
- **T22 near-duplicate regeneration is documented, not implemented** — SKILL.md:131 and CHANGELOG.md:213 promise regeneration at Jaccard ≥ 0.78; `forward` never calls `near_duplicates`, which appears only in the dry-run assertion (ex:137-139, 308-326, 380). [trap] (verified: read) → P2
- **T23 contradiction_honesty rewards the number of contradictions** — 0.25 for none, 0.75 for three plus one discriminator, 1.0 for six (ex:184-187); as a GEPA metric it pushes the mapper toward listing more contradictions. [trap] (verified: probe T3) → P14
- **T24 tetraframe's metric is a mean that hides a failed gate** — a run whose cartography names no contradiction at all (0.25 < 0.75) still scores **0.893**; banned phrases are checked only in `transformed_frame`, not `transformed_predicate`, and gold phrases are not lower-cased, so „Balanced approach" never matches (ex:233-236). [trap] (verified: probe T5, T5b, T6) → P11
- **T25 BestOfN threshold 0.84 is a 1.0 in disguise** — `transform_reward` takes only 0, 0.25, 0.5, 0.75, 1.0 (minus 0.4), so 0.84 accepts only a perfect reward (ex:220-224, 305-306). [trap] (verified: probe T4)
- **T26 branch independence has a floor and an empty-set quirk** — three identical incompatible corners still score 0.61; two corners whose residuals are empty (all tokens in the seed) count as similarity 1.0 (ex:124-128, 168-172). [trap] (verified: probe T8, T9)
- **T27 autodialectics' feedback has no causes** — the docs say the reflection LM reads „fake completion: 'done' claimed with no test results or files" and „needs the cause, not the number" (SKILL.md:146-147; reference.md:106-109); the code emits `"fake_completion 1.00; unsupported_claims 1.00; …"` (ex:214-215). [trap] (verified: dry-run output)
- **T28 "five more at 0.05" is six** — SKILL.md:141-144 lists six weights and „five more at 0.05"; the code has six dimensions at 0.05 (ex:50-55; sum 1.00). [trap] (verified: probe AD3)
- **T29 the negation backstop fails criteria phrased negatively** — criterion „No regressions in existing functionality." against the output „There are no regressions in existing functionality." → fail („3/3 keywords, negated"), because `"no "` is a negation marker; meanwhile the sloppy „all tests pass" claim passes „All tests pass on the reference interpreter/platform." on 2 of 4 keywords (ex:67, 138-153). The demo's honest output says „shows zero regressions", which dodges it. [trap] (verified: probe AD1, AD1b)
- **T30 declared uncertainties buy down unsupported claims** — `(claims − supported)/claims × (1 − uncertainties/claims)`, clamped: three declared uncertainties turn unsupported_claims 1.0 into 0.0; declaring one uncertainty with no hedge word in the text costs 0.3 on refusal (ex:194, 190, 201). [trap] (verified: probe AD2, AD7)
- **T31 objection coverage is 1.0 when nothing was objected** — `coverage = … if objections else 1.0` and out-of-range `objection_index` values count (ex:223); this is the anti-pattern SKILL.md:183 names. The pass rate enters twice (task_success + verification_quality = 0.40 base, 0.50 code) and unsupported claims twice (groundedness + unsupported_assertion_rate) (ex:224-229). [trap] (verified: probe AD5)
- **T32 the end-to-end metric trusts the program's own verifier** — `harness_metric` scores `pred.checks` from the `Verify` predictor inside the `Dialectic` it optimises (ex:326-329), not `criterion_checks`; the sloppy demo output with LM-claimed passes scores 0.71 (gate revise) against 0.46 with the deterministic checks. GEPA can raise the metric by rewriting `Verify`'s instruction. [trap] (verified: probe AD6) → P1
- **T33 an empty output is low-slop** — `slop_score` of `Output(text="")` has composite 0.175 („requirement_drift 1.00; fake_completion 0.50"), i.e. score 0.825; the "status completed with < 50 chars of output" indicator of reference.md:97 is not in the code (ex:176-177). Only the verification rule of the gate catches it. [trap] (verified: probe AD8b) → P19
- **T34 domain inference differs from its doc** — ties go to the first dict key (`code`), not `generic`; there is no "strong keywords count double"; matching is exact-word („tests" ≠ „test" → `generic`) (ex:113-119 vs reference.md:27-28). [trap] (verified: probe AD4)
- **T35 autodialectics constructs that exist only in docs** — `plan_metric`/`salient_terms`, `independent_findings`, `Synthesis.assumptions`, `Antithesis.evidence_summary`, `Dialectic(executor)`, the "trained on the benchmark" pattern, the three-indicator fake completion (SKILL.md:93-135; reference.md:83-85, 97, 99, 128-138); the example has none of them. [trap] (verified: read)
- **T36 deep-refine grades destructive and no-op actions HIGH** — `replace_node(Juna → Kael)` (merging two characters) is HIGH because the source node exists; `delete_edge` of an existing edge is HIGH; `insert_edge` of an edge that already exists (a no-op) is HIGH; a genuinely new edge between existing nodes is MEDIUM; an edge to a nonexistent node with one known endpoint is MEDIUM (ex:96-111). The label measures "well-formed against the graph", not "right". [trap] (verified: probe DR1)
- **T37 `replace_node` relabels instead of merging** — reference.md:137 promises „merge into an existing `new` node if present, rewiring edges"; the code only sets `label` (ex:138-141), so two nodes are labelled „Kael" afterwards and every later action naming Kael is LOW. [trap] (verified: probe DR2)
- **T38 ambiguous-name list is half the documented one** — code: 10 labels (`main, main(), run, run(), index, home, overview, notes, todo, draft`, ex:24); reference.md:114: 19 (adds `train, train(), test, test(), setup, setup(), untitled, new_page, introduction`) — „setup" passes as MEDIUM. [trap] (verified: probe DR1, DR6)
- **T39 `max_hops > 4` crashes** — `CAPS[step - 1]` has four entries (ex:23, 206); `DeepRefine(max_hops=5)` raises `IndexError: list index out of range` at step 5. [trap] (verified: DummyLM run)
- **T40 trace, validation, queue and "exhausted" are docs only** — `LoopTrace`, `validate_trace`, the pending-queue discipline and the early stop on a non-widening retriever (SKILL.md:152-160, 167-168; reference.md:95-103, 143-159) do not exist in the example; SKILL.md:154 says „Every run writes a `LoopTrace`". [trap] (verified: read) → P2
- **T41 the program cannot see the example's graph** — `forward(question)` retrieves through the retriever bound in `build(retrieve)` (ex:165, 206) while `refine_metric` applies the actions to `gold.graph` (ex:224-229); a trainset of per-example graph snapshots (reference.md:170-171) optimises proposals against one graph and scores them against another. [trap] (verified: read)
- **T42 reflect's German and punctuation anchors never match** — the trailing `\b` after `nein,`, `no,` and `remember:` needs a word character next, so „Nein, das ist falsch so.", „No, that's the wrong file." and „Remember: tabs for Makefiles." are all filtered out; „benutzen" does not match `benutze`; „Nimm lieber uv als pip." does not match (ex:23-27). [trap] (verified: probe R1)
- **T43 reflector_metric ignores unseen noise and punishes paraphrase** — eight extra never-skipped signals keep the score at 1.0; a paraphrase of the accepted learning or the right text with confidence MEDIUM scores 0.0 (ex:114-119). [trap] (verified: probe R3, R3b, R3c)
- **T44 corrections_metric is satisfied by coexistence** — both „uv pip install" and „pip install" in the output → 1.0; neither → 0.5 (ex:105-110). [trap] (verified: probe R2)
- **T45 the ledger keeps the first confidence** — reference.md:74 says „keep max confidence"; after LOW then HIGH the row stays LOW (ex:54-58); the deterministic kind → confidence mapping („the Signature may lower but never raise it", reference.md:55-57) is not implemented. [trap] (verified: probe R4)
- **T46 nothing runs the dry-runs automatically** — see TEST. [trap]
- **T47 "GEPA-optimizable" is unexercised** — no example constructs `dspy.GEPA`, runs `compile`, or checks that a metric's feedback reaches reflection; each skill's GEPA claim is a claim. [claim] (verified: grep of the seven examples)
- **T48 two encodings of "mean of nothing"** — wiki-compile's `_mean([])` is 1.0 (ex:161-163), tetraframe's is 0.0 (ex:142-144). [trap] (verified: read) → P6
- **T49 D3 contradicts its own table** — „GEPA's reflection model must not be the judge it is optimising against" (plugin plan:295-296), yet the judge role `task` and the `reflection` role both default to `anthropic/claude-opus-5`, differing only in temperature (plugin plan:288-292; Legacy/tools/kpwiki/lm.py:57-59) — by adversarial-review's own standard a "weak independence". [trap] (verified: read)
- **T50 the compounding plan's count is stale** — „D-01…D-21" and „twenty-one already-made author decisions" (compounding plan:22, 118-119); `Legacy/Plan/drafting/decision-log_2026-09-11.md` holds D-01…D-24. [claim] (verified: grep)
- **T51 the old plugin plan's size figure is stale** — „`tools/kpwiki/`, 523 lines" (plugin plan:16); the parked copy is 6,655 lines in 22 files. [claim] (verified: wc)

## Code worth keeping

**1. Legal-decision guard and citation check** — wiki-compile ex:118-135. Runs on 3.3.1 (dry-run exercises both; the broken fixture's `update` on the reviewed page is named). Keep the shape; replace the substring test with the target's `quotes.verdict` (T3) and the model's `conflicts` with the page's recorded state (T4).

```python
def number_lines(text: str) -> str:
    return "\n".join(f"{i}: {line}" for i, line in enumerate(text.splitlines(), 1))


def citation_resolves(c: Citation, sources: dict[str, str]) -> bool:
    lines = sources.get(c.file, "").splitlines()
    if not lines or not 1 <= c.start <= c.end <= len(lines):
        return False
    return c.quote.strip() in "\n".join(lines[c.start - 1:c.end])


def decision_legal(d: IngestDecision, page: PageState | None) -> bool:
    """Active-page protection: a reviewed or locked page with conflicts is flagged, never updated."""
    if page is None:
        return d.action == "create"
    if d.action == "create":
        return False
    return not (d.action == "update" and page.status in PROTECTED_STATUSES and d.conflicts)
```

**2. The weighted deterministic metric, and the helper that makes it pass on nothing** — wiki-compile ex:161-170 and ex:224-237. Runs on 3.3.1 (dry-run: 1.0 / 0.657). Show it with T1: `_mean([]) == 1.0`.

```python
def _mean(xs) -> float:
    xs = list(xs)
    return sum(xs) / len(xs) if xs else 1.0


def _citation_axis(run: Compiled, sources: dict[str, str], deficits: list[str]) -> float:
    cites = [c.citation for e in run.extractions for c in e.claims] + [c for k in run.concepts for c in k.citations]
    bad = [c for c in cites if not citation_resolves(c, sources)]
    deficits += [f"citation does not resolve: {c.file}:{c.start}-{c.end} {c.quote[:30]!r}" for c in bad]
    return 1.0 - len(bad) / len(cites) if cites else 0.0
```

```python
def compile_metric(gold, pred, trace=None, pred_name=None, pred_trace=None):
    """GEPA-compatible metric: every axis is deterministic and names its blame."""
    import dspy

    run: Compiled = pred.compiled
    deficits: list[str] = []
    axes = {"citations": _citation_axis(run, gold.sources, deficits),
            "decisions": _decision_axis(run, gold.pages, deficits),
            "merge": _merge_axis(run, deficits),
            "diffs": _diff_axis(run, gold.pages, deficits),
            "links": _link_axis(run, gold.known_entities, gold.language, deficits)}
    score = sum(WEIGHTS[a] * v for a, v in axes.items())
    return dspy.Prediction(score=round(score, 3),
                           feedback="; ".join(deficits) or "cited, legally decided, merged across sources, consistent diff")
```

**3. Independence guard, demotion, content digest** — adversarial ex:58-78. Runs on 3.3.1 (dry-run asserts `assert_independent(writer, writer)` raises „must differ"). Show with T11.

```python
def same_lm(a, b) -> bool:
    if a is b:
        return True
    return getattr(a, "model", None) == getattr(b, "model", None) and getattr(a, "kwargs", None) == getattr(b, "kwargs", None)


def assert_independent(reviewer, writer) -> None:
    """The judge may not be the author: same object or same model+kwargs is refused."""
    if writer is None:
        raise ValueError("no writer LM configured; call dspy.configure(lm=...) for the writer first")
    if same_lm(reviewer, writer):
        raise ValueError(f"reviewer must differ from the writer LM ({getattr(writer, 'model', writer)!r})")


def demotion(review: Review, demote_at: int = DEMOTE_AT) -> Literal["keep", "contested"]:
    """Too many overstated claims demote the artifact's status; its body is never touched."""
    return "contested" if len(review.overstated) >= demote_at else "keep"


def digest(*parts: str) -> str:
    return hashlib.sha256("\x1f".join(parts).encode("utf-8")).hexdigest()[:16]
```

**4. A metric on the judge (precision and recall with named misses and inventions)** — adversarial ex:85-121. Runs on 3.3.1 (dry-run 1.0 / 0.0). The matching rule is the weak point (T10).

```python
def _matches(flagged: list[str], gold: list[str]) -> tuple[list[str], list[str]]:
    """(missed gold items, spurious flagged items) with substring tolerance either way."""
    hit = lambda a, b: _norm(a) in _norm(b) or _norm(b) in _norm(a)  # noqa: E731
    missed = [g for g in gold if not any(hit(g, f) for f in flagged)]
    spurious = [f for f in flagged if not any(hit(g, f) for g in gold)]
    return missed, spurious


def _f1(flagged: list[str], gold: list[str]) -> float:
    if not flagged and not gold:
        return 1.0
    missed, spurious = _matches(flagged, gold)
    tp = len(flagged) - len(spurious)
    precision = tp / len(flagged) if flagged else 0.0
    recall = (len(gold) - len(missed)) / len(gold) if gold else 0.0
    return 2 * precision * recall / (precision + recall) if precision + recall else 0.0


def judge_metric(gold, pred, trace=None, pred_name=None, pred_trace=None):
    """Score the reviewer itself: F1 on overstated and unsupported claims against a labelled set."""
    import dspy

    review: Review = pred.review
    flagged = [o.quote for o in review.overstated]
    missed_o, spurious_o = _matches(flagged, gold.overstated)
    missed_u, spurious_u = _matches(review.unsupported, gold.unsupported)
    parts = []
    if missed_o:
        parts.append(f"missed overstated claims: {missed_o}")
    if spurious_o:
        parts.append(f"flagged supported claims as overstated: {spurious_o}")
    if missed_u:
        parts.append(f"missed unsupported claims: {missed_u}")
    if spurious_u:
        parts.append(f"flagged cited claims as unsupported: {spurious_u}")
    score = round(0.5 * _f1(flagged, gold.overstated) + 0.5 * _f1(review.unsupported, gold.unsupported), 3)
    return dspy.Prediction(score=score, feedback="; ".join(parts) or "every overstated and unsupported claim found, none invented")
```

**5. Reviewer module, reward, and Refine wiring** — adversarial ex:147-180. Runs on 3.3.1 (verified end to end with two DummyLMs); what Refine feeds back is T13.

```python
    class AdversarialReviewer(dspy.Module):
        def __init__(self, reviewer_lm, demote_at: int = DEMOTE_AT):
            super().__init__()
            self.review = dspy.ChainOfThought(ReviewArtifact)
            self.support = dspy.Predict(CitationSupport)
            self.reviewer_lm = reviewer_lm
            self.demote_at = demote_at
            self.cache: dict[str, dspy.Prediction] = {}

        def forward(self, artifact: str, evidence: str, difficulty: Difficulty = "standard"):
            assert_independent(self.reviewer_lm, dspy.settings.lm)
            key = digest(artifact, evidence, difficulty, str(self.reviewer_lm.model))
            if key in self.cache:
                return self.cache[key]
            with dspy.context(lm=self.reviewer_lm):
                review = self.review(artifact=artifact, evidence=evidence, difficulty=difficulty).review
            self.cache[key] = dspy.Prediction(review=review, verdict=demotion(review, self.demote_at), cache_key=key)
            return self.cache[key]

        def check_citation(self, claim: str, span: str) -> Support:
            with dspy.context(lm=self.reviewer_lm):
                return self.support(claim=claim, span=span).support

    def review_reward(reviewer: AdversarialReviewer, evidence: str, difficulty: Difficulty = "standard"):
        """Reward for dspy.Refine around the writer: the independent review score in [0, 1]."""

        def reward(args: dict, pred) -> float:
            return reviewer(artifact=pred.text, evidence=evidence, difficulty=difficulty).review.score / 10

        return reward

    def review_refine(writer: dspy.Module, reviewer: AdversarialReviewer, evidence: str, rounds: int = 3):
        """The writer is re-run until the reviewer's score reaches the target or the rounds are spent."""
        return dspy.Refine(module=writer, N=rounds, reward_fn=review_reward(reviewer, evidence), threshold=TARGET_SCORE)
```

**6. The "never change behaviour" metric, first half** — clarify ex:74-106. Runs on 3.3.1 (dry-run 1.00 / 1.00 / 0.25). Needs word-boundary matching (T16) before use on real text.

```python
    c: Clarification = pred.clarification
    original, excerpt = gold.claim_text, gold.source_excerpt
    context = " ".join([original, excerpt, getattr(gold, "canon_context", "")])
    glossary = [g.strip() for g in gold.glossary_terms.split(",") if g.strip()]
    problems: list[str] = []

    # 1. meaning kept: no glossary term smuggled in, no entity dropped, no new quantifier
    new_terms = [g for g in glossary if g.lower() in c.clarified_text.lower() and g.lower() not in context.lower()]
    dropped = [e for e in gold.entities if e.lower() not in c.clarified_text.lower()
               and not any(b.mention.lower() == e.lower() for b in c.bindings)]
    new_quant = _present(c.clarified_text, QUANTIFIERS) - _present(context, QUANTIFIERS)
    meaning = 1.0 - min(1.0, 0.5 * len(new_terms) + 0.5 * len(dropped) + 0.5 * len(new_quant))
    if new_terms:
        problems.append(f"Introduced terms absent from the source: {new_terms}.")
    if dropped:
        problems.append(f"Dropped entities: {dropped}.")
    if new_quant:
        problems.append(f"Added quantifiers the source does not state: {sorted(new_quant)}.")

    # 2. scope grounded: a value other than 'unspecified' must occur in the source/context
    ungrounded = [v for v in (c.scope.world, c.scope.act, c.scope.part)
                  if v != UNSPECIFIED and v.lower() not in context.lower()]
    grounded = 0.0 if ungrounded else 1.0
    if ungrounded:
        problems.append(f"Scope values not found in the source: {ungrounded}; use 'unspecified'.")

    # 3. hedges: fewer than the original, and any that remain are declared ambiguities
    left = _present(c.clarified_text, HEDGES)
    declared = {a.phrase.lower() for a in c.ambiguities}
    undeclared = [h for h in left if not any(h in d for d in declared)]
    hedges = 1.0 if not undeclared and _count(c.clarified_text, HEDGES) <= _count(original, HEDGES) else 0.0
    if undeclared:
        problems.append(f"Hedges left unresolved and undeclared: {undeclared}; resolve from the source or list them as ambiguities.")
```

**7. Clarify metric, second half (bindings, questions, language, weights)** — clarify ex:108-131. Runs on 3.3.1.

```python
    # 4. bindings: every slug must be a known glossary term
    bad_slugs = [b.slug for b in c.bindings if b.slug not in glossary]
    bindings = 1.0 if not bad_slugs else 0.0
    if bad_slugs:
        problems.append(f"Bindings to unknown glossary slugs: {bad_slugs}.")

    # 5. questions well-formed and verdict consistent
    malformed = [a.phrase for a in c.ambiguities if not a.question.strip().endswith("?")]
    consistent = (c.verdict != "clear") == bool(c.ambiguities)
    questions = 1.0 if not malformed and consistent else 0.0
    if malformed:
        problems.append(f"Ambiguities without a question: {malformed}.")
    if not consistent:
        problems.append("Verdict inconsistent with the ambiguity list ('clear' needs an empty list).")

    # 6. language kept: no English function words when the original is German
    german = bool(_words(original) & {"der", "die", "das", "und", "nicht", "wird", "ist"})
    english = bool(_words(c.clarified_text) & {"the", "and", "is", "not"})
    language = 0.0 if german and english else 1.0
    if german and english:
        problems.append("The claim was translated; keep the source language.")

    score = 0.3 * meaning + 0.15 * grounded + 0.15 * hedges + 0.15 * bindings + 0.15 * questions + 0.1 * language
    return dspy.Prediction(score=score, feedback=" ".join(problems) or "Clarified without adding or losing meaning.")
```

**8. Four isolated corners and a BestOfN transformer** — tetraframe ex:308-326. Constructs on 3.3.1 (dry-run lists the predictors); `forward` was not executed (it needs an LM; the mechanics — `lm.copy(rollout_id, temperature)`, `dspy.context`, `BestOfN` — are verified separately).

```python
        def forward(self, seed: str):
            d = self.distill(seed=seed).distilled
            s = self.select(distilled=d).selection
            corners = {}
            for i, mode in enumerate(MODES):
                view = CornerView(normalized_seed=d.normalized_seed, stakes=d.stakes, constraints=d.constraints,
                                  hidden_assumptions=d.hidden_assumptions, primary_predicate=s.primary_predicate,
                                  evaluation_criteria=d.evaluation_criteria, corner_contract=CONTRACTS[mode])
                assert_isolation(view)
                lm = dspy.settings.lm
                with dspy.context(lm=lm.copy(rollout_id=i, temperature=0.9 if mode in ("both", "neither") else 0.7)):
                    corner = self.generators[mode](view=view).corner
                corner.mode = mode
                corners[mode] = corner
            cartography = self.map(corners=list(corners.values())).cartography
            frame = self.transform(primary_predicate=s.primary_predicate, corners=list(corners.values()),
                                   cartography=cartography).frame
            return dspy.Prediction(run=Run(seed=seed, distilled=d, selection=s, corners=corners,
                                           cartography=cartography, frame=frame))
```

**9. Anti-collapse heuristics** — tetraframe ex:168-187. Runs on 3.3.1 (dry-run). English-only tokens (T21), count-rewarding contradiction score (T23).

```python
def branch_independence(run: Run) -> float:
    seed = run.distilled.normalized_seed
    pair = [max(0.0, similarity(residual(run.corners[a].core_claim, seed), residual(run.corners[b].core_claim, seed)) - 0.35)
            for a, b in INCOMPATIBLE]
    return max(0.0, 1.0 - min(1.0, 0.6 * _mean(pair)))


def transformation_quality(frame: Frame, corners: dict[str, Corner]) -> float:
    text = (frame.transformed_frame + " " + frame.transformed_predicate).lower()
    required = [frame.survivors_from_p, frame.survivors_from_not_p, frame.hidden_structure_from_both,
                frame.dissolved_false_frame_from_neither, frame.operational_tests]
    overlap = similarity(frame.transformed_predicate, corners["P"].patched_claim + " " + corners["not-P"].patched_claim)
    score = min(1.0, _mean(1.0 if r else 0.0 for r in required) + 0.3 * (1.0 - overlap))  # cap BEFORE the penalty
    return max(0.0, score - (0.4 if any(m in text for m in COMPROMISE) else 0.0))


def contradiction_honesty(c: Cartography) -> float:
    if not c.contradiction_map:
        return 0.35 if c.complementarity_map else 0.25
    return min(1.0, 0.4 + 0.1 * len(c.contradiction_map) + 0.05 * len(c.discriminators))
```

**10. BestOfN reward and the verification metric** — tetraframe ex:220-237. Runs on 3.3.1 (dry-run).

```python
def transform_reward(args: dict, pred) -> float:
    f: Frame = pred.frame
    penalty = 0.4 if any(m in (f.transformed_predicate + f.transformed_frame).lower() for m in COMPROMISE) else 0.0
    parts = [f.survivors_from_p, f.survivors_from_not_p, f.hidden_structure_from_both, f.dissolved_false_frame_from_neither]
    return max(0.0, _mean(1.0 if p else 0.0 for p in parts) - penalty)


def tetraframe_metric(gold, pred, trace=None, pred_name=None, pred_trace=None):
    import dspy

    run: Run = pred.run
    scores = verify(run)
    deficits = [f"{k} {v:.2f} < {THRESHOLDS[k]:.2f}" for k, v in scores.items() if v < THRESHOLDS[k]]
    banned = [b for b in getattr(gold, "banned_transformed_phrases", []) or [] if b in run.frame.transformed_frame.lower()]
    if banned:
        deficits.append(f"P* uses banned phrases {banned}")
    score = _mean(scores.values()) * (0.5 if banned else 1.0)
    return dspy.Prediction(score=round(score, 3), feedback="; ".join(deficits) or "independent corners, rigorous both/neither, transformed P*")
```

**11. Deterministic criterion backstop** — autodialectics ex:138-153. Runs on 3.3.1 (dry-run); the negation list fails negatively phrased criteria (T29).

```python
def _negated_support(text: str, terms: set[str]) -> bool:
    """True when every sentence that mentions the criterion also carries a negation marker."""
    windows = [w for w in re.split(r"(?<=[.!?])\s+|\n+", text) if len(terms & keywords(w)) / max(len(terms), 1) >= 0.5]
    return bool(windows) and all(any(n in f" {w.lower()} " for n in NEGATION) for w in windows)


def criterion_checks(contract: Contract, text: str) -> list[tuple[str, bool, str]]:
    """Deterministic backstop: keyword overlap per criterion; a criterion mentioned only in negated sentences fails."""
    checks = []
    for criterion in contract.acceptance_criteria:
        terms = keywords(criterion)
        present = terms & keywords(text)
        negated = _negated_support(text, terms)
        passed = len(present) >= max(1, len(terms) // 2) and not negated
        checks.append((criterion, passed, f"{len(present)}/{len(terms)} keywords" + (", negated" if negated else "")))
    return checks
```

**12. Gate, canary, promotion** — autodialectics ex:233-258. Pure Python, runs (dry-run asserts accept/reject and promote/refuse).

```python
def gate(verdict_pass: bool, confidence: float, score: float, slop: float) -> str:
    if not verdict_pass and confidence < REJECT_CONFIDENCE:
        return "reject"
    if slop > REJECT_SLOP:
        return "reject"
    if verdict_pass and score >= ACCEPT_MIN_SCORE and slop < ACCEPT_MAX_SLOP:
        return "accept"
    return "revise"


def canary_passes(text: str, must_include: list[str], must_not_include: list[str], slop: float,
                  groundedness: float, max_slop: float = 0.6, min_groundedness: float = 0.2) -> bool:
    lowered = text.lower()
    return (all(t in lowered for t in must_include) and not any(t in lowered for t in must_not_include)
            and slop <= max_slop and groundedness >= min_groundedness)


def promote(champion: tuple[float, float], challenger: tuple[float, float], canaries_passed: bool) -> tuple[bool, str]:
    """(score, slop) pairs; all three conditions are required."""
    if not canaries_passed:
        return False, "canary failed"
    if challenger[1] > champion[1]:
        return False, f"challenger slop {challenger[1]:.2f} > champion {champion[1]:.2f}"
    if challenger[0] <= champion[0]:
        return False, f"challenger score {challenger[0]:.2f} <= champion {champion[0]:.2f}"
    return True, "score up, slop not up, canaries pass"
```

**13. End-to-end harness metric (the one that trusts the program's verifier)** — autodialectics ex:322-331. Runs on 3.3.1 (probe AD6); keep as the counter-example for T32.

```python
def harness_metric(gold, pred, trace=None, pred_name=None, pred_trace=None):
    """End-to-end GEPA metric: verified criteria + slop feedback, one Prediction."""
    import dspy

    slop = slop_score(gold.contract, pred.output, pred.objections)
    score = run_score(gold.contract, pred.checks, slop.dims, pred.objections, pred.dispositions)
    decision = gate(all(ok for _, ok, _ in pred.checks), sum(ok for _, ok, _ in pred.checks) / max(len(pred.checks), 1),
                    score, slop.composite)
    return dspy.Prediction(score=score * (0.5 if decision == "reject" else 1.0),
                           feedback=f"gate={decision}; {slop.feedback}")
```

**14. Deterministic evidence review** — deep-refine ex:78-112. Runs on 3.3.1 (dry-run labels MEDIUM, HIGH, LOW). Keep the refusal machinery, not the grading (T36).

```python
def review_action(graph: dict, action: RefinementAction) -> ActionReview:
    """Deterministic HIGH/MEDIUM/LOW grading (port of DeepRefine action_review)."""
    evidence, warnings = [], []
    entity_idx = [0, 2] if action.kind != "replace_node" else [0, 1]
    matches = {}
    for i in entity_idx:
        if i >= len(action.args):
            warnings.append(f"missing argument {i}")
            continue
        name = action.args[i]
        found = _matches(graph, name)
        matches[i] = found
        if "::" not in name and name.casefold() in AMBIGUOUS:
            warnings.append(f"Ambiguous bare node name: {name!r}; include a source path.")
        if len(found) > 1:
            warnings.append(f"Ambiguous node name: {name!r} matches {len(found)} nodes.")
        if found:
            evidence.append(f"Node exists: {name}")
    if action.kind in {"insert_edge", "delete_edge"} and len(action.args) == 3:
        subs, objs = matches.get(0, []), matches.get(2, [])
        if _edge_exists(graph, subs, action.args[1], objs):
            evidence.append("Exact edge already exists.")
        elif subs and objs:
            evidence.append("Both endpoint nodes exist; relation inferred by the loop.")
    if action.kind == "replace_node" and matches.get(0):
        evidence.append("Replacement source node exists.")
    if warnings:
        confidence = "LOW"
    elif any(e.startswith(("Exact edge", "Replacement source")) for e in evidence):
        confidence = "HIGH"
    elif evidence:
        confidence = "MEDIUM"
    else:
        confidence, warnings = "LOW", ["No node or edge evidence found."]
    return ActionReview(action=action, confidence=confidence, evidence=evidence, warnings=warnings)
```

**15. Hop loop and the metric that applies proposals to a copy** — deep-refine ex:203-238. Runs on 3.3.1 (DummyLM reaches step 4; dry-run metric 0.90).

```python
        def forward(self, question: str):
            history, triples = [], []
            for step in range(1, self.max_hops + 1):
                triples = list(dict.fromkeys(retrieve(question, step - 1, triples)))[: CAPS[step - 1]]
                verdict = self.judge(question=question, triples=fmt(triples)).answerable
                history.append({"step": step, "num_hops": step - 1, "triples": triples, "answerable": verdict})
                if verdict:
                    break
            if len(history) <= 1:
                return dspy.Prediction(history=history, early_exit=True, abduction=None, actions=[])
            hist = "\n".join(f"step {h['step']} hops={h['num_hops']} answerable={h['answerable']}\n{fmt(h['triples'])}"
                             for h in history[-HORIZON:])
            abduction = self.abduce(question=question, interaction_history=hist).abduction
            actions = self.propose(question=question, triples=fmt(triples), abduction=abduction).actions[:MAX_ACTIONS]
            return dspy.Prediction(history=history, early_exit=False, abduction=abduction, actions=actions)

    def refine_metric(gold, pred, trace=None, pred_name=None, pred_trace=None):
        if pred.early_exit:
            ok = bool(gold.answerable_at_hop0)
            return dspy.Prediction(score=1.0 if ok else 0.0,
                                   feedback="Early exit was correct." if ok else "Judged answerable at hop 0 but the base lacks the fact.")
        reviews = review_actions(gold.graph, pred.actions)
        low = [r for r in reviews if r.confidence == "LOW"]
        staged = apply_actions(gold.graph, reviews)
        by_id = {n["id"]: n["label"] for n in staged["nodes"]}
        present = {(by_id[e["source"]], e["relation"], by_id[e["target"]]) for e in staged["edges"]}
        answerable_now = all(tuple(t) in present for t in gold.expected_triples)
        parts = []
        if low:
            parts.append(f"{len(low)} LOW-confidence action(s): {low[0].warnings[0]}")
        if not answerable_now:
            parts.append("Expected triples still missing after applying non-LOW actions.")
        if len(pred.actions) > 5:
            parts.append("More than 5 actions; prefer the minimal edit set.")
        score = 0.6 * answerable_now + 0.3 * (1 - len(low) / max(1, len(reviews))) + 0.1 * (len(pred.actions) <= 5)
        return dspy.Prediction(score=score, feedback=" ".join(parts) or "Minimal, grounded actions; question now answerable.")
```

**16. Fingerprint ledger and pre-filter** — reflect ex:42-68. Pure Python, runs (dry-run). The regex it applies is T42.

```python
def fingerprint(learning: str) -> str:
    return hashlib.sha256(" ".join(learning.lower().split()).encode()).hexdigest()[:16]


class Ledger:
    """In-memory ledger; persist as JSONL in real use."""

    def __init__(self) -> None:
        self.rows: dict[str, dict] = {}

    def record(self, sig: LearningSignal, context_id: str) -> str:
        fp = fingerprint(sig.learning)
        row = self.rows.setdefault(fp, {"learning": sig.learning, "confidence": sig.confidence,
                                        "contexts": [], "count": 0, "status": "pending"})
        if context_id not in row["contexts"]:
            row["contexts"].append(context_id)
        row["count"] += 1
        return fp

    def eligible_for_promotion(self, threshold: int = PROMOTION_THRESHOLD) -> list[str]:
        return [fp for fp, r in self.rows.items() if len(r["contexts"]) >= threshold and r["status"] != "promoted"]


def candidate_turns(transcript: list[dict]) -> list[int]:
    """Deterministic pre-filter: user turns long enough that match a signal pattern."""
    return [i for i, t in enumerate(transcript)
            if t["role"] == "user" and len(t["content"]) >= MIN_MESSAGE_CHARS and PREFILTER.search(t["content"])]
```

**17. Correction and reflector metrics** — reflect ex:99-125. Run on 3.3.1 (dry-run 0.0 / 1.0 / 1.0).

```python
    def learning_to_example(sig: LearningSignal, failing_input: dict) -> dspy.Example:
        return dspy.Example(**failing_input, expected_behavior=sig.new_behavior,
                            forbidden_behavior=sig.old_behavior,
                            feedback=f"User corrected this: {sig.learning}").with_inputs(*failing_input)

    def corrections_metric(gold, pred, trace=None, pred_name=None, pred_trace=None):
        text = str(pred.toDict()).lower()
        satisfied = not gold.expected_behavior or gold.expected_behavior.lower() in text
        # A violation is the old behaviour showing up *without* the corrected one
        # (the corrected form may contain the old one as a substring, e.g. "uv pip install").
        violated = bool(gold.forbidden_behavior) and gold.forbidden_behavior.lower() in text and not satisfied
        score = 0.0 if violated else (1.0 if satisfied else 0.5)
        fb = gold.feedback if (violated or not satisfied) else "Follows the learned correction."
        return dspy.Prediction(score=score, feedback=fb)

    def reflector_metric(gold, pred, trace=None, pred_name=None, pred_trace=None):
        got = {(s.learning.lower(), s.confidence) for s in pred.signals}
        want = {(s["learning"].lower(), s["confidence"]) for s in gold.accepted}
        noise = [s for s in pred.signals if s.learning.lower() in {x.lower() for x in gold.skipped}]
        tp, fn = len(got & want), len(want - got)
        score = (tp / max(1, len(want))) * (1 - len(noise) / max(1, len(pred.signals)))
        fb = []
        if fn:
            fb.append(f"Missed {fn} accepted learning(s).")
        if noise:
            fb.append(f"{len(noise)} proposal(s) the user skipped before.")
        return dspy.Prediction(score=score, feedback=" ".join(fb) or "All accepted learnings found, no skipped noise.")
```

**18. Where Refine's feedback comes from (DSPy 3.3.1 source)** — `dspy/predict/refine.py:148-167`: the advice is written by `dspy.Predict(OfferFeedback)` on the default LM from the reward value and the reward function's source; nothing the reward function computed besides the number is passed.

```python
                modules = {"program_code": self.module_code, "modules_defn": inspect_modules(mod)}
                trajectory = [{"module_name": predictor2name[p], "inputs": i, "outputs": dict(o)} for p, i, o in trace]
                trajectory = {
                    "program_inputs": kwargs,
                    "program_trajectory": trajectory,
                    "program_outputs": dict(outputs),
                }
                reward = {
                    "reward_code": self.reward_fn_code,
                    "target_threshold": self.threshold,
                    "reward_value": reward,
                }

                advise_kwargs = dict(**modules, **trajectory, **reward, module_names=module_names)
                # only dumps if it's a list or dict
                advise_kwargs = {
                    k: v if isinstance(v, str) else orjson.dumps(recursive_mask(v), option=orjson.OPT_INDENT_2).decode()
                    for k, v in advise_kwargs.items()
                }
                advice = dspy.Predict(OfferFeedback)(**advise_kwargs).advice
```

**19. Offline test of an independent-judge refine loop (written for this extraction, not in the repo)** — two `DummyLM`s, a reviewer with a distinct `model`, and assertions on which LM received the feedback call. Runs on 3.3.1 (output: 2 feedback calls on the writer, reviewer reason absent, reward present, 1 reviewer call because of the cache).

```python
import dspy, json
from dspy.utils.dummies import DummyLM
# AdversarialReviewer, review_refine = build()  (from example_adversarial_review.py)

class Drafter(dspy.Module):
    def __init__(self):
        super().__init__()
        self.write = dspy.Predict("question -> text")
    def forward(self, question):
        return self.write(question=question)

writer = DummyLM({"program_code": {"discussion": "d", "advice": {"write": "WRITER_ADVICE"}},
                  "question": {"text": "Der Schleier ist das wichtigste Ritual."}})
review = {"score": 3, "overstated": [{"quote": "das wichtigste Ritual", "why": "ZZ_REVIEWER_REASON_ZZ",
          "evidence_needed": "a ranking"}], "unsupported": [], "strengths": [], "weaknesses": []}
reviewer_lm = DummyLM({"artifact": {"reasoning": "r", "review": review}})
reviewer_lm.model = "dummy-reviewer"          # two DummyLMs are otherwise "the same LM"
dspy.configure(lm=writer)
reviewer = AdversarialReviewer(reviewer_lm)
out = review_refine(writer=Drafter(), reviewer=reviewer, evidence=EVIDENCE, rounds=3)(question="Was ist der Schleier?")
fb = [h for h in writer.history if "program_code" in json.dumps(h.get("messages", ""))]
assert len(fb) == 2                                              # Refine's feedback ran on the writer LM
assert "ZZ_REVIEWER_REASON_ZZ" not in json.dumps(fb[0]["messages"])   # the review never reaches it
assert len(reviewer_lm.history) == 1                             # same text -> cached review
```

## The old report, corrected

`Plan/concept/dspy-repos_2026-09-23/dspy-agent-skills-A.md` read SKILL.md and reference.md of these skills but only `example_wiki_compile.py` in full, so every code-versus-doc gap below the wiki-compile one was invisible to it.

- **§0 "file paths in them do not resolve here"** — incomplete. Most of them resolve under `Legacy/`: `Legacy/tools/kpwiki/` (22 files, 6,655 lines, not 523), `Legacy/requirements-dspy.txt` (already pinned `dspy==3.3.1`, so the plan's bump was carried out), the decision logs (D-01…D-24, not D-21), agent memory, the scripts. Only `.agency/session.db`, `Plan/wiki/index/canon`, `tools/kpwiki/selection.py` and `Wiki/learnings/` never existed. More importantly, the predecessor ran the pack's patterns as real modules (`compile_metric.py`, `clarify_metric.py`, `tetraframe.py`, `tetraframe_metric.py`), and those are *better* than the pack's examples (gold-concept coverage, a no-concepts guard, whitespace-collapsing citations, near-duplicate regeneration, a German-aware tokenizer).
- **§2.10 compile_metric as "a clean worked example" [adopt-as-reference]** — its numbers are right (1.0 / 0.657), but it missed T1 (empty compile 0.70 with the all-clean feedback; one claim, nothing merged → 1.0), T2 (no recall), T3 (empty quote resolves) and T7. Adopt the shape only with "not scored" for empty axes (P15) and per-axis reporting (P11).
- **§2.11 `decision_legal` "exactly as the brief described"** — it reads the model's own `conflicts`: an `update` with `conflicts=[]` on a reviewed page is legal, and a `contested` page (the status adversarial-review's demotion produces) is unprotected (T4).
- **§2.27 "the target's quotes.py … caught `das Management` vs `dem Management`, which this pack's substring check would not catch"** — wrong. A literal substring check does catch a changed article. The real differences run the other way: the pack's check is *too literal* (false-fails escaped or wrapped export text, cross-line quotes need `\n`), accepts empty and one-character quotes, and lets the model type the line numbers (P26).
- **§2.28 "challenged ⊆ conflicts"** — the check is one shared token of three or more characters, „ist" suffices (T5).
- **§2.30 clarify's metric as "a precise, mechanical version of P12/P26/P13"** — quantifiers next to punctuation are invisible (T16), the English → German direction is unchecked, an identity rewrite scores 1.0, a declared hedge increase is penalised silently (T17, T19).
- **§2.31 "asking scores as high as resolving built into the gold set discipline"** — the metric reads no expected verdict or clarification, so gold `needs-author` cases cannot teach anything through it; SKILL.md:124 and reference.md:96-99 disagree on whether a hand-written clarification is needed; `not-promotable` without ambiguities is penalised (T18, T19).
- **§2.32 deep-refine's HIGH/MEDIUM/LOW as "a good template for scoring a model's proposed page merge"** — the opposite: `replace_node` on any existing node — a merge — is graded HIGH, as are deleting an existing edge and inserting an edge that already exists (T36); `replace_node` does not even merge (T37). As a template for merges it would certify exactly what P13 forbids.
- **Missing: adversarial-review's Refine claim** — the report repeats "`dspy.Refine` … so the writer learns from the judge". In 3.3.1 the writer's own LM writes the advice from a number; the judge's findings never reach it (T13). Also missed: `judge_metric` scores empty/one-word/whole-artifact flags 1.0 (T10), the guard passes `writer.copy(rollout_id=1)` (T11), the cache ignores reviewer configuration (T12).
- **Missing: tetraframe** — the isolation guard cannot fire (T20), near-duplicate regeneration is not implemented despite SKILL.md and CHANGELOG (T22), the suite is ASCII-only (T21), the metric rewards counting contradictions (T23) and averages away a failed gate (T24), threshold 0.84 ≡ 1.0 (T25).
- **Missing: autodialectics** — feedback without causes against its own rule (T27), "five more" is six (T28), the negation backstop fails "No regressions" (T29), uncertainties buy down unsupported claims (T30), coverage 1.0 without objections — the anti-pattern the skill names (T31), `harness_metric` trusts the optimised program's own `Verify` (T32), an empty output is low-slop (T33), domain ties (T34).
- **Missing: deep-refine and reflect-loop code gaps** — T36–T45: AMBIGUOUS has 10 of 19 labels, `max_hops > 4` crashes, `LoopTrace`/`validate_trace` do not exist, the program cannot see the example's graph; the reflect pre-filter's `nein,`/`no,`/`remember:` never match, `reflector_metric` ignores unseen noise, the ledger keeps the first confidence.
- **Missing: DSPy mechanics this slice depends on** — `BestOfN`/`Refine` return `None` silently for N ≤ 2 when every attempt raises (T14); output-model constraints turn one bad item into a lost prediction (API); unused predictors (`answer`, `support`) are GEPA components (OPT); GEPA matches trace entries by signature equality; the default cache makes tetraframe's fixed rollout ids replay (PROD).
- **Missing: D3's internal contradiction** — judge and reflection share `anthropic/claude-opus-5` (T49).
- **§1 "every skill ships a runnable example … asserted by tests"** — the tests assert only that the string `--dry-run` occurs (T46); I ran all seven, and all pass on 3.3.1.

## Ten things the skill must say

1. A metric that returns 1.0 for nothing is the commonest defect in this slice: `_mean([]) == 1.0` makes an empty wiki compile score 0.70 "clean" and a one-claim compile 1.0 — report "not scored" instead (T1, P15).
2. Substring matching in a judge metric is gameable to 1.0 by an empty or one-word flag; compare flagged items by identity (a line produced by `read.py --find`), never by containment (T10, T3).
3. `dspy.Refine` does not pass a judge's findings to the writer — the writer's own LM writes the advice from a reward number; to feed a review back, put it in an input field yourself (T13).
4. `BestOfN`/`Refine` return `None` silently when every attempt raises and N ≤ 2 — "never reached" must be reported as such (T14).
5. A deterministic check that reads the model's own self-report (`conflicts`, `Verify.checks`, `truncated`) is not deterministic; legality and verification must be computed from the page and the source (T4, T8, T32).
6. Word matching for German needs word boundaries and umlauts: space-delimited markers miss „nie.", `[a-zA-Z]` splits „Schöpfung" (T16, T21).
7. Never let a model's merge or demotion through a gate: `ConceptDraft.definition`, `replace_node` graded HIGH and demotion to `contested` all violate never-merge and the reviewed-page rule; the target's equivalents are attributed readings, conflict records and a human promotion (PAT wiki-compile/deep-refine, T36).
8. A metric that rewards more contradictions trains a conflict detector to invent them; conflict detection stays unmechanised (T23, P14).
9. Report each check's own status: weighted sums and means hide a failed gate (tetraframe 0.893 with no contradictions) (T24, P11).
10. Keep the refusal machinery these skills share — closed action enums, `create` by lookup, apply never called by the proposer, review ≠ approval, suppression visible, promotion after ≥ 2 contexts and a human — and verify each doc claim against code: every one of the seven skills documents behaviour its example does not have (T8, T13, T18, T22, T35, T40, T45; P2).
