# Integration plan — every surveyed repo into the DSPy skill pack and into this repo

Finalised 2026-09-15 after reading the eight per-repo survey reports in
[surveys/](surveys/) in full. It completes
[repo-survey_2026-09-15.md](repo-survey_2026-09-15.md) (the catalogue) and
[knowledge-system-concept_2026-09-15.md](knowledge-system-concept_2026-09-15.md)
(the design) with the one thing both lacked: for every concept worth taking,
**which pack skill teaches the LLM part, which file in this repo carries the
deterministic part, and in which phase it lands.**

Two homes, one rule:

- **[netzkontrast/dspy-agent-skills](https://github.com/netzkontrast/dspy-agent-skills)**
  teaches *patterns* as DSPy programs: typed Signatures, closed enums,
  deterministic metrics that return `dspy.Prediction(score, feedback)`, a
  `--dry-run` example. A pattern goes into the pack when at least two surveyed
  repos share it or when it is an LLM step this repo needs more than once.
- **This repo** instantiates the patterns with the novel's enums
  (`tools/kpwiki/`), and carries everything deterministic as scripts and YAML
  (`scripts/`, `Wiki/schema/`). Nothing deterministic becomes a DSPy program;
  nothing LLM-driven lives outside `tools/kpwiki`.

## 0. Status per repo

| repo | licence | pack skill | this repo | remaining |
|---|---|---|---|---|
| `rlm-workflow` | MIT | `dspy-rlm-workflow` v0.3.0 ✔ | used by `/tetraframe` and the ingest plan | — |
| `DeepRefine-Skill` | PyPI | `dspy-deep-refine` v0.3.0 ✔ | `RaiseQuestions` signature ✔; loop, evidence grading, trace: Phase 5 | Phase 5 |
| `claude-reflect-system` | MIT | `dspy-reflect-loop` v0.3.0 ✔ | corrections during pilot review → gold: Phase 3 | Phase 3 |
| `clarify` | Apache 2.0 | `dspy-clarify` v0.4.0 ✔ | `ClarifyGate`, `clarify_metric`, `/clarify` ✔ | gold set: Phase 5 |
| `tetraframe-dspy` | MIT | `dspy-tetraframe` v0.5.0 ✔ | `TetraFrame`, metric, `/tetraframe` ✔ | first live run on D-W2 |
| `dspy-local` | MIT | **`dspy-local-runtime` (new, §2.3)** | `local_lm.py`, `KP_LM_BACKEND` ✔ | pack skill |
| `Llm-Wiki-` (Karpathy) | — | **`dspy-wiki-compile` (new, §2.1)** | `SourceIngest` ✔; concept table, fts, filed queries: Phase 1 | pack skill, Phase 1 |
| `llm-wiki-agent` | MIT | `dspy-wiki-compile` | health/lint split, post-ingest validation: Phase 1/3 | Phase 1 |
| `llm-wiki-compiler` | npm | `dspy-wiki-compile` | two-phase merge, freshness, hash-pinned candidates: Phase 1/4 | Phase 1 |
| `synthadoc` | AGPL core | `dspy-wiki-compile`, **`dspy-adversarial-review` (new, §2.2)** | lifecycle, decision rules, truncation, adversarial gate: Phase 1/3/4 | patterns only, own code |
| `AutoSci` | MIT | `dspy-adversarial-review` | schema contract, xref, foundations, writers policy, `/check` tiers: Phase 1 | Phase 1 |
| `quicky-wiki` | MIT | `dspy-wiki-compile` | knowledge diff, epistemic events: Phase 3/5 | Phase 3 |
| `llm-tldr` | AGPL | — (operational, no LLM step) | dedup, dirty-count batching, durable/volatile: Phase 1/3 | own code |

Five repos are fully ported. The remaining eight resolve into **three new
pack skills** and **one Phase-1 PR** in this repo.

## 1. Coverage matrix

One row per concept the surveys marked worth taking. "Pack" names the skill
that teaches the LLM pattern; "here" names the file that carries it in this
repo; a dash means the concept has no LLM part.

### Karpathy `Llm-Wiki-` (`surveys/llm-wiki.md` §3–4)

| concept | pack | here | phase |
|---|---|---|---|
| raw / wiki / schema separation; single `SCHEMA.md` contract, thin pointers | `dspy-wiki-compile` (rule 1) | `Wiki/SCHEMA.md`, pointer in `CLAUDE.md` | 1 |
| concept table as compressed map with status `high-confidence · single-source · tentative · contradicted` | `dspy-wiki-compile` (`ConceptDraft.status`) | `Wiki/concept-table.md`, rendered by `scripts/render_wiki_views.py` from concept frontmatter, never hand-edited | 1 |
| contradiction block with a resolution field | `dspy-wiki-compile` (`Disagreement.resolution`) | `question` pages, `contradicts` edges | 3 |
| ingest → discuss → create loop | — (process) | `/research-ingest` prints the knowledge diff and stops before writing outside `candidates/` | 3 |
| filed query artefacts (3+ sources ⇒ page) | — | `/query` already files to `Plan/queries/`; moves to `Wiki/syntheses/` (D-W4) | 1 |
| BM25 candidate finder, freshness gate, "open the page before citing" | — | `scripts/wiki_fts.py` (vendored, stdlib), `stats` check in `/query` | 1 |
| ripple update: search before creating a concept page | `dspy-wiki-compile` (merge phase input = fts hits) | `/wiki-understand` | 4 |
| preference preflight (`EXTEND.md`) | — | `Wiki/schema/conventions.yaml` (`language`, batch size) | 1 |

### `llm-wiki-agent` (`surveys/llm-wiki-agent.md` §3)

| concept | pack | here | phase |
|---|---|---|---|
| typed frontmatter + per-kind templates | — | `Wiki/schema/entities.yaml`, `Wiki/templates/<kind>.md.tmpl` | 1 |
| grep-parseable append-only log with provenance (agent, session, hash) | — | `Wiki/log.md` grammar `## [date] op \| title \| skill=… \| sha256=…` | 1 |
| health (free) vs lint (LLM) boundary | `dspy-wiki-compile` (rule 6) | `scripts/wiki_lint.py --health` (deterministic subset) vs `/lint-wiki` | 1 |
| post-ingest validation (broken links, unindexed pages, summary) | `dspy-wiki-compile` (metric axis *links resolve*) | `/research-ingest` runs `wiki_lint.py` on the batch before it reports | 3 |
| contradiction detection at ingest | `dspy-wiki-compile` (`DecideIngest.conflicts`) | `contradicts` edge + page `contested` | 3 |
| missing-entity detection (mentioned in ≥3 pages, no page) | — | `wiki_lint.py` rule `missing-entity` | 1 |
| link-density budget | — | `wiki_lint.py` rule `sparse-page` (warn) | 1 |
| aggressive `[[wikilink]]` binding of known terms | `dspy-wiki-compile` (metric axis *known entities linked*) | glossary = `Codex/GLOSSARY.md` slugs | 3 |
| two-pass graph (deterministic + inferred) | not adopted (cost; canon links are explicit) | deterministic pass only: `Wiki/graph/edges.jsonl` | 1 |

### `llm-wiki-compiler` (`surveys/llm-wiki-compiler.md` §3)

| concept | pack | here | phase |
|---|---|---|---|
| two-phase compile: extract all sources of a batch, then merge concepts, then write | `dspy-wiki-compile` (`BatchCompile.forward` order) | `tools/kpwiki/programs.py::BatchCompile` | 3 |
| source hashing + freshness `fresh · stale · orphaned · unverified` | — | `sha256` in source frontmatter; `wiki_lint.py` rule `stale-source` | 1 |
| line-range citations validated deterministically | `dspy-wiki-compile` (metric axis *citation resolves + quote is substring*) | `Citation` model ✔; `wiki_lint.py` rule `citation-resolves` | 1 |
| lifecycle gates as data (FSM over one frontmatter field) | — | `Wiki/schema/entities.yaml` `lifecycle.transitions`; `wiki_lint.py` rule `illegal-transition` | 1 |
| review candidates with approval pinned to the reviewed content hash | — | `Wiki/candidates/`; `/wiki-promote` records `sha256` of the reviewed body in `log.md`, refuses a changed hash | 1 |
| 13 pure lint rule families, run concurrently, no LLM | — | `wiki_lint.py` rule registry (one function per rule, `--json`) | 1 |
| citation-support judge with cached judgements | `dspy-adversarial-review` (`CitationSupport`) | judge cache keyed by `(claim hash, span hash)` under `.cache/` | 4 |
| health score per page (freshness, citation coverage, link density, orphans) | — | `Wiki/graph/coverage.json` | 1 |
| hybrid retrieval (dense → BM25 → graph) | not adopted (BM25 first) | `wiki_fts.py` + `neighbors` over `edges.jsonl` | 1 |
| OKF import/export, MCP server, profile engine | not adopted | — | — |

### `synthadoc` (`surveys/synthadoc.md` §3) — patterns only, AGPL

| concept | pack | here | phase |
|---|---|---|---|
| 5-state lifecycle with allowed-transition matrix and cascade cleanup on archive | — | concept §3.2 enums; `wiki_lint.py` rules `illegal-transition`, `archived-link` | 1 |
| active-page protection (RULE 1b): a reviewed page is flagged, never overwritten | `dspy-wiki-compile` (`DecideIngest` metric: `update` on a `reviewed` page with conflicts scores 0) | `Wiki/schema/writers.yaml`: `/research-ingest` may not write `status: reviewed` pages | 3 |
| ingest decision rules flag / update / create; entity profile ⇒ own page | `dspy-wiki-compile` (`IngestDecision.action` closed enum) | `BatchCompile` | 3 |
| claim-level `^[file:L-L]` citations, normalised | `dspy-wiki-compile` | `Citation` ✔ | — |
| adversarial review gate with threshold demotion | `dspy-adversarial-review` (`ReviewArtifact`, demotion rule) | `/wiki-promote --review` on `confidence: high` pages; demotes to `contested` | 4 |
| staged candidates before promotion | — | `Wiki/candidates/` | 1 |
| per-source truncation flag | `dspy-wiki-compile` (`Triage.truncated`) | source frontmatter `truncated: true` + lint warning | 2 |
| immutable audit log with content-deduplicated snapshots | — | git is the snapshot store; `log.md` carries the hash; no second database | 1 |
| query decomposition + knowledge-gap callout | `dspy-wiki-compile` (`AnswerQuery.gaps`) | `/query` reports gaps when fts returns < 3 hits | 4 |
| agentic workflows with diff + approval before write | — (process) | every command is dry-run first; `AskUserQuestion` before a write outside `candidates/` | all |
| hooks on ingest / lint completion | — | `.claude/settings.json` PostToolUse on `Wiki/**` (user applies) | 1 |
| 3-layer cache | — | `DSPY_CACHEDIR` covers LLM responses; embeddings not used | — |

### `AutoSci` / ΩmegaWiki (`surveys/autosci.md` §3)

| concept | pack | here | phase |
|---|---|---|---|
| schema as contract: `entities · edges · xref · conventions` YAML + loader, zero codegen | — | `Wiki/schema/*.yaml`, `tools/kpwiki/wiki_schema.py` loader shared by lint and programs | 1 |
| forward link ⇒ reverse link written in the same operation | — | `Wiki/schema/xref.yaml`; `wiki_lint.py --fix` completes reverses | 1 |
| terminal foundations (receive links, write no reverse, never auto-created) | `dspy-wiki-compile` (rule 3: canon is read-only context) | Canon and `Codex/` are terminal; lint rule `no-reverse-into-canon`, `no-auto-canon-page` | 1 |
| confidence + evidence required on semantic edges | — | `Wiki/graph/edges.jsonl` schema; lint rule `edge-evidence` | 1 |
| write permissions per skill as data | — | `Wiki/schema/writers.yaml`; `log.md` records the writing skill; lint rule `writer-policy` | 1 |
| `/ask --crystallize` | — | `/query` files syntheses (existing) | 1 |
| `/check --fix` with auto-fixable / non-fixable / suggest tiers | — | `wiki_lint.py --fix --dry-run`, `--suggest` | 1 |
| independent Review LLM (`standard · hard · adversarial`) | `dspy-adversarial-review` (`difficulty` enum, reviewer ≠ writer) | `lm_context("worker")` as reviewer; D-W11 | 4 |
| `/refine` multi-round loop against a target score | `dspy-adversarial-review` (`ReviewRefine` = `dspy.Refine` around the writer, review as reward) | `/wiki-understand --refine` | 4 |
| `/novelty` multi-source verification | not adopted (academic) | — | — |
| user-owned flags: never invent, flip or drop | — (rule in every skill) | `Wiki/schema/writers.yaml` `user_flags`; command docs | 1 |
| checkpoint save / load for batch runs | — | `/research-ingest` checkpoints in `.cache/kpwiki/ingest-<batch>.json` | 3 |
| `/prefill` foundations | not needed: Canon and `Codex/` already exist | — | — |

### `quicky-wiki` (`surveys/quicky-wiki.md`)

| concept | pack | here | phase |
|---|---|---|---|
| knowledge diff per ingest: reinforced · challenged · new · gaps | `dspy-wiki-compile` (`KnowledgeDiff` output, consistency axis) | `/research-ingest` prints it; stored in the batch log entry | 3 |
| epistemic event timeline per claim: created · reinforced · challenged · superseded · resolved | — | `log.md` lines `## [date] claim \| <slug> \| <event> \| by=<source>`; `scripts/render_wiki_views.py` renders a per-concept timeline | 3 |
| cascade risk: foundational claim with many dependents | — | `wiki_lint.py` rule `cascade-risk` over `supports` edges (report only) | 5 |
| redteam of high-confidence claims | `dspy-adversarial-review` | adversarial pass before a milestone (concept §4 F) | 4 |
| confidence decay | not adopted (research is superseded by decisions, not by time) | `superseded_by` | — |

### `llm-tldr` (`surveys/llm-tldr.md` §3) — inspiration only, AGPL

| concept | pack | here | phase |
|---|---|---|---|
| content-hash dedup before any LLM call; near-duplicate clustering | — | `scripts/source_dedup.py` (sha256 + shingle similarity; the manifest already marks 246 byte-equal copies) | 1 |
| dirty-count batching of expensive passes | — | `/research-ingest` runs merge + lint once per batch of 25, not per source | 3 |
| durable vs volatile partition | — | Canon glossary and axioms loaded once per lint run by hash; `Wiki/` re-indexed on demand | 1 |
| token / cost stats per workflow | — | `lm.py` `track_usage=True`; `/research-ingest` reports tokens per batch | 3 |
| config precedence | — | `Wiki/schema/conventions.yaml` < env | 1 |
| AST layers, daemon, FAISS | not adopted (code tool) | — | — |

## 2. What the pack gains: three skills (v0.7.0, [dspy-agent-skills#4](https://github.com/netzkontrast/dspy-agent-skills/pull/4))

### 2.1 `dspy-wiki-compile` — compile immutable sources into a maintained wiki

Sources: Karpathy §3–4, llm-wiki-agent §2–3, llm-wiki-compiler §2–3,
synthadoc §2 (decision rules, active protection, truncation), quicky-wiki
(knowledge diff). This is the generalisation of `tools/kpwiki/{signatures,
programs,metrics}.py` plus the three steps this repo does not have yet.

Signatures (typed, closed enums):

| signature | in → out | taken from |
|---|---|---|
| `TriageSource` | source text + manifest row → `Triage{tier, category, language, truncated}` | this repo ✔, synthadoc truncation |
| `ExtractClaims` | numbered source → `list[Claim{text, citation{file, start, end, quote}, kind, entities}]` | this repo ✔, compiler/synthadoc citations |
| `DecideIngest` | claims + existing page `{status, body}` → `IngestDecision{action: flag \| update \| create, rationale, conflicts[]}` | synthadoc RULE 1, 1b, 2, 2b, 3 |
| `MergeConcepts` | all extractions of a batch (+ fts hits) → `list[ConceptDraft{slug, definition, sources[], disagreements[{claim_a, claim_b, resolution: pending \| supersedes \| both_valid}], status}]` | compiler two-phase, Karpathy concept table + contradiction block |
| `KnowledgeDiff` | prior page + new claims → `Diff{reinforced[], challenged[], new[], gaps[]}` | quicky-wiki |
| `AnswerQuery` | question + retrieved pages → `Answer{text with [[citations]], confidence, gaps[]}` | Karpathy query, synthadoc gap callout |

Metric axes (deterministic; an LLM judge may sit on top but never below):
citation resolves and the quote is a substring of the cited lines; every
sentence of a merged definition carries ≥ 1 citation; a disagreement lists ≥ 2
distinct sources; `update` on a page with `status ∈ {reviewed, locked}` and
non-empty `conflicts` scores 0 (active-page protection as a number);
`challenged ⊆ conflicts` and `new ∩ prior = ∅` (diff consistency); known
entities appear as `[[links]]`; language kept.

Rules the skill states: raw sources are never modified; all extraction before
any merge; the program returns drafts and never writes (candidates are the
caller's step); truncation is recorded, never silent; the health check is
free and runs first, the lint that needs an LLM runs per batch.

Example: two fixture sources that disagree on one claim → `DecideIngest`
returns `flag`, `MergeConcepts` lists both with `resolution: pending`,
`KnowledgeDiff.challenged` is non-empty, and a compromise merge that drops one
source scores below threshold.

### 2.2 `dspy-adversarial-review` — an independent judge that cannot rewrite

Sources: synthadoc adversarial gate (§3.9), AutoSci `/review` + `/refine`
(§3.9–10), quicky-wiki redteam, llm-wiki-compiler citation-support judge.

| signature | in → out |
|---|---|
| `ReviewArtifact` | artifact + evidence pages + `difficulty: standard \| hard \| adversarial` → `Review{score 1–10, overstated[{quote, why, evidence_needed}], unsupported[], strengths[], weaknesses[]}` |
| `CitationSupport` | claim + cited span → `supported \| partial \| unsupported` with reason |

Mechanics: the reviewer runs under `dspy.context(lm=reviewer)` where
`reviewer is not writer` (asserted in code); demotion is a rule
(`len(overstated) ≥ k` ⇒ `status: contested`), never a deletion;
`ReviewRefine` wraps the writer in `dspy.Refine` with the review score as
reward, `max_rounds`, and a score trajectory the caller can read; judgements
are cached by content hash. Metric for the judge itself: precision and recall
of `overstated` and `unsupported` against a labelled set, so GEPA can
optimise the reviewer without making it merely harsher.

Rules: the reviewer never proposes prose; a demoted page keeps its body;
the same LM may not play both roles; `hard` and `adversarial` change the
instruction, not the threshold.

### 2.3 `dspy-local-runtime` — DSPy through the Claude CLI, no API key

Source: dspy-local. The skill documents the pattern this repo already runs:
a `BaseLM` subclass that executes `claude -p --output-format json` in an
isolated home, backend selection (`api · claude-cli · auto`), the kwargs the
CLI cannot honour (`temperature`, `max_tokens`, `rollout_id`, `n > 1`,
`cache=True`) and what each program loses without them (TetraFrame corner
diversity rests on the contract docstrings; `BestOfN` and `Refine` loop
sequentially), a budget table per call, and how to run GEPA `auto="light"`
in the background. Example: a minimal `ClaudeLM` whose `--dry-run` exercises
prompt building and result parsing without spawning, and a `--probe` that
makes one real call.

Pack changes: three skill directories, routing and loop rows in
`dspy-advanced-workflow`, README, `docs/usage.md`, `docs/installation.md`,
`docs/CHANGELOG.md`, manifests → 0.7.0; the validators and all fifteen dry
runs must pass.

## 3. What this repo gains: the Phase-1 PR, attributed

Everything deterministic the surveys recommended lands in one PR, before any
further LLM step, because every later phase depends on the lint.

| deliverable | from | done when |
|---|---|---|
| `Wiki/SCHEMA.md` + `Wiki/schema/{entities,edges,xref,conventions,writers}.yaml` + `tools/kpwiki/wiki_schema.py` loader | Karpathy, AutoSci, compiler, synthadoc | `tools/kpwiki/schema.py` enums are generated from the YAML, not duplicated |
| `Wiki/templates/{source,concept,question,synthesis}.md.tmpl` | llm-wiki-agent, AutoSci | each kind renders from its template |
| `Wiki/index.md`, `log.md`, `overview.md`, `concept-table.md` (rendered), `candidates/`, `graph/edges.jsonl`, `graph/coverage.json` | Karpathy, AutoSci | `render_wiki_views.py --check` clean on an empty wiki |
| `scripts/wiki_lint.py` with rule registry: `broken-link`, `orphan`, `missing-entity`, `sparse-page`, `required-field`, `enum`, `illegal-transition`, `archived-link`, `citation-resolves`, `stale-source`, `xref-symmetry`, `edge-evidence`, `writer-policy`, `no-k-marker-outside-canon`, `no-reverse-into-canon`, `no-auto-canon-page`, `index-sync`, `log-coverage`, `candidate-age`; modes `--health`, `--fix --dry-run`, `--suggest`, `--json`, `--hook` | compiler, AutoSci, llm-wiki-agent, synthadoc | `tests/test_wiki_lint.py` with one fixture per rule |
| `scripts/wiki_fts.py` (vendored Karpathy helper) | Karpathy | `build`, `search`, `stats`, `doctor` over `Wiki/`, `Canon/`, `Sources/drive/` |
| `scripts/source_dedup.py` | llm-tldr, compiler | byte-equal and near-duplicate clusters written into the manifest (`duplicate_of`) |
| `Sources/README.md` fetch procedure (Drive MCP → markdown, `sha256`, `truncated`) | llm-wiki-agent, synthadoc | one source exported by hand end to end |
| hook lines and deny rules for `.claude/settings.json` (documented, user applies) | synthadoc hooks, AutoSci ownership | listed in `docs/dspy-base.md` |

Phases 2–7 keep the concept §8 table; the attributions above say which
repo's pattern each command follows. Two additions to §8: Phase 3 batches
merge and lint per 25 sources (llm-tldr), and Phase 4 runs the adversarial
review before a page reaches `reviewed` with `confidence: high` (synthadoc,
AutoSci).

## 4. Not ported

Unchanged from the catalogue: confidence decay, LLM-inferred graph edges,
academic pipelines, code-structure analysis, the full profile engine and
OKF, Obsidian plugin and web UIs, AGPL code, a second Markdown copy of the
canon graph. Added after the full read: synthadoc's second database
(git and `log.md` are the audit trail), AutoSci `/prefill` (Canon and
`Codex/` are the foundations already), and llm-wiki-compiler's hybrid
retrieval (BM25 plus graph neighbours first; embeddings only if BM25 fails
on the theory slice).

## 5. Decisions for the author (Rule 0)

D-W1, D-W2 and D-W9 from the concept remain the gate for Phases 1 and 2.
This plan adds two:

| id | question | recommendation |
|---|---|---|
| D-W10 | Add `dspy-wiki-compile`, `dspy-adversarial-review`, `dspy-local-runtime` to the pack as v0.7.0 before the Phase-1 PR? | yes; the Phase-3 program `BatchCompile` is an instance of the first, and the pack stays the single place where a pattern is taught |
| D-W11 | Who is the independent reviewer? `claude/haiku` via the CLI (same vendor, different model, free on the subscription), `claude/sonnet`, or an external OpenAI-compatible model (AutoSci pattern, needs a key)? | `claude/haiku` as reviewer for wiki pages, `claude/sonnet` for the promotion gate; switch to a second vendor when a key exists. The skill asserts reviewer ≠ writer either way |

Epistemic events stay in `log.md` as lines plus a rendered per-concept
timeline; no per-claim table. The author can veto this without a decision
id.

## 6. Order of work

1. Pack v0.7.0 (D-W10): the three skills, one PR, validators and dry runs green — opened as dspy-agent-skills#4 (v0.6.0 had been taken by `dspy-autodialectics`, merged from another session; `dspy-adversarial-review` is positioned against it as artifact review by a second model).
2. `/tetraframe` on D-W2, first live run, result to the author.
3. Phase-1 PR here (§3), lint green on an empty wiki, one source by hand.
4. After D-W1 and D-W9: pilot export of the audit slice plus part of kernkonzept (about 25 documents), `BatchCompile` live on the CLI backend, review together; the corrections start the reflect loop and the 30-source gold set.
5. Baseline for `BatchCompile` recorded; GEPA only after the gold set exists (Phase 6).
