# Brief: what the kohaerenzprotokoll repo needs (read before scanning)

You are scanning one DSPy repository to harvest ideas and code for a toolchain in
`/home/user/kohaerenzprotokoll`. Do NOT modify that repo or the repo you scan.

## The target project, in 15 lines
- A German research corpus (346 landed Drive documents, `Sources/drive/*.md`) turned into a
  wiki of term pages (`Wiki/candidates/*.md`, 56 pages) by a mostly-manual, heavily
  checked process: fetch -> census (every candidate term in ONE document) -> note (quotes
  with `^[Lnn]` line citations) -> reconcile (census vs wiki index, by lookup) -> human review.
- Standard-library Python scripts do everything decidable: `state.py` (derived counts, prose
  staleness check), `quotes.py` (every quotation resolves to its line), `read.py --find`
  (ask for a line number instead of typing it), `judgements.py` (replay recorded human
  decisions against code), `selftest.py` (prove checkers can fail), `reconcile.py`,
  `account.py` (one recursive operation: account(subject, question)).
- DSPy 3.3.1 is installed (`.venv-dspy`) but NOTHING in the pipeline calls a model yet.
  Candidate model jobs, in order of readiness:
  1. **one-term-or-two**: are two surface forms (e.g. `Guardian`/`Guardians`, `Riss`/`Risse`,
     `Negentropie`/`Entropie`=NEVER merge) the same wiki term? 26 labelled examples in
     `Plan/trainsets/surface-pairs.jsonl`, each with a human-written `rule` in words.
     Deterministic baseline `fold()` = 65%, perfect precision, misses only inflections.
     Planned optimizer ladder: LabeledFewShot -> BootstrapFewShot -> InferRules -> SIMBA -> GEPA.
  2. **entity lists**: a model names the 50-100 key entities of one document; CODE (not the
     model) finds and writes the line number. Measured: Haiku F1 0.67/0.28, Jev (typed
     yes/no classifier) cheaper but worse. Human-vs-human ceiling is F1 ~0.66.
  3. **candidate extraction / census** via `dspy.RLM` (`scripts/rlm_ingest.py`), every
     candidate must carry a verified line; unverified = "reconstruction".
  4. **skill descriptions** (`.agents/skills/*/SKILL.md`) could be optimized (GEPA) since
     `dspy_skills.SkillManager` renders prompts from the description field only.
- Open problems: stale reconciliations after merges (a derived task queue is planned),
  17 quotations that do not resolve, reviewed-page-vs-new-source conflicts, which qmd
  search backend is best (never benchmarked), cost/trace visibility of LM calls.

## Principles a proposal must survive (from PRINCIPLES.md)
- P1 anything decidable is a program; judgement is named as judgement.
- P3/P4 by hand first; no field/type/check without real instances. P2 describe no more than exists.
- P5 every workflow ships an offline, no-key fixture. P23 a guard reports what it could NOT check.
- P12/P26 quote, never paraphrase; a model never types an identifier or line number — code does.
- P13 never merge two sources' readings into one definition. Conflict detection is never mechanised.
- P15 "never reached" != "answered badly". P18 repeats, cache off. P19 assert non-empty + German.
- P24 done is a measurement. P27 score against the human ceiling, not a single gold reading.
- A model output may direct attention; it never enters the canonical record unverified.
- Small data: n=26. Anything needing 100+ examples is currently irrelevant — say so.

## What to produce
Write your report to the path given in your task, in English, as Markdown, with these sections:

1. **What it is** — 5 lines max. Maturity: tested? used? toy? DSPy version it targets.
2. **Every good idea** — a numbered list of EVERY idea worth knowing, generous, including
   small ones (a metric trick, a caching choice, a test pattern, a doc convention).
   Each item: one-line name, 1-3 sentence description, `path:line` evidence, and a tag
   `[adopt] [adapt] [catalogue] [skip]` for kohaerenzprotokoll, with one clause why.
3. **Directly reusable for the target** — map concrete pieces (module, file, function) to
   the target's jobs 1-4 or open problems above. State what would have to change.
4. **Conflicts with the principles** — where this repo does something the target forbids
   (e.g. model writes line numbers, metric that cannot fail, silent cache, no offline test).
   These are also useful: name the trap.
5. **Dependencies & cost** — install footprint, Python/DSPy version constraints, whether it
   can live in a venv beside DSPy 3.3.1 without moving the pin, API keys needed.
6. **Verdict** — 3 lines: the single most valuable thing to take, and what to leave.

Rules: cite files you actually opened. Mark anything you inferred without reading as
(unverified). Don't pad; don't praise. If something is broken or doesn't run, say so —
you may run offline tests/dry-runs with `uv run` in a throwaway venv if cheap (<2 min),
never with an API key, never `pip install` into the system Python.
