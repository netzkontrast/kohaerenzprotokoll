# Repo survey — what the nine tool repositories offer a novel-research wiki

Surveyed 2026-09-15 for the Kohärenz Protokoll knowledge system. Eight repos
were read by haiku agents (full reports in [surveys/](surveys/)); the DSPy
skill pack was read and set up directly ([docs/dspy-base.md](../../docs/dspy-base.md)).
The synthesis that uses these findings is
[knowledge-system-concept_2026-09-15.md](knowledge-system-concept_2026-09-15.md).

## One line per repo

| repo | what it is | licence | role for us |
|---|---|---|---|
| `dspy-agent-skills` | 5 Claude-Code skills teaching DSPy 3.2.x (signatures, eval harness, GEPA, RLM, workflow); 114 tests, dry-run examples | MIT | **adopted** as the LLM tooling base |
| `Llm-Wiki-` (Karpathy LLM-wiki bootstrap) | the original three-layer idea (raw / wiki / schema) as a skill, plus a 400-line SQLite FTS5 BM25 helper | — | **architecture blueprint**; port `wiki_fts.py`, concept-table, contradiction block |
| `llm-wiki-agent` | Python tools + CLAUDE.md schema: ingest → source/entity/concept pages, index/log, health vs lint, two-pass graph | MIT | **reference for page templates, post-ingest validation, health/lint split** |
| `llm-wiki-compiler` | TypeScript knowledge compiler: two-phase compile, source hashing + freshness, lifecycle profiles, 13 pure lint rules, review candidates with hash-pinned approval, line-range citations | (npm) | **design reference** (port patterns, not code) |
| `synthadoc` | Python wiki engine: 5-state page lifecycle, active-page protection, ingest decision rules, AuditDB snapshots, `^[file:L-L]` citations, candidates dir, agentic workflows with approval | AGPL-3.0 core | **patterns only** (copyleft); lifecycle + decision rules + candidates |
| `AutoSci` (ΩmegaWiki) | schema-as-contract (YAML entities/edges/xref/policy), terminal "foundations", `/ask --crystallize`, `/check --fix`, `/review` + `/refine` loops with a second LLM, user-owned flags | MIT | **schema contract, xref reciprocity, foundations, refine loop, flag rule** |
| `DeepRefine-Skill` | KG refinement loop: answerability judgment → multi-hop → error abduction (incompleteness / incorrectness / redundancy) → actions → evidence-scored review → dry-run apply | (PyPI) | **the "question our understanding" loop**; trace schema; HIGH/MED/LOW evidence |
| `quicky-wiki` | TypeScript claim graph: confidence, epistemic events, cascade propagation, knowledge diff on ingest, metabolism/redteam | MIT | **knowledge diff, epistemic event log, cascade idea**; skip decay |
| `llm-tldr` | code-structure extractor (AST→PDG), daemon, FAISS; content-hash dedup, dirty-flag batching, durability partitioning | AGPL-3.0 | **operational patterns only**: dedup, batching thresholds, durable vs volatile |

> **Update 2026-09-16 — the `dspy-agent-skills` row has moved on.** The table
> above is the snapshot as surveyed and is left as written. Since then the pack
> has grown from 5 skills to **32** (v0.11.0) and from 114 tests to **633**, and
> it retargeted from DSPy 3.2.x to **3.3.1**. This repo's pin followed in
> `requirements-dspy.txt`; `tools/kpwiki/` needed no code change, because the
> two breaking renames in DSPy 3.3.0 (`dspy.RLM`'s `max_iterations` → `max_iters`,
> and `interpreter=` → `interpreter_factory=` on `RLM`/`ProgramOfThought`/`CodeAct`)
> land on APIs this repo does not call. Current state:
> [docs/dspy-base.md](../../docs/dspy-base.md). The adoption verdict is unchanged.

## The concept catalogue (what we take, from where)

### Layers and ownership
- **Raw sources are immutable; the LLM maintains the wiki; a single schema
  document is the operating contract** — Karpathy (`surveys/llm-wiki.md` §2),
  `llm-wiki-agent` (`raw/` read-only), AutoSci ownership zones
  (`runtime/schema/conventions.yaml`: user-owned / tools-only / append-only).
- **Terminal foundations**: pages that receive links but never write reverse
  links and are never auto-created by ingest — AutoSci `foundations`. Our
  Canon plays this role for the research wiki.
- **Durable vs volatile partition** — llm-tldr `durability.py`: load canon
  once, re-index research on demand.

### Page model
- Typed frontmatter with closed enums (`type`, `status`, `confidence`, `sources`)
  — `llm-wiki-agent` CLAUDE.md, synthadoc `WikiPage`, AutoSci `entities.yaml`.
- **Lifecycle states** `draft → active → contradicted | stale → archived` with
  an allowed-transition matrix and cascade cleanup on archive — synthadoc
  `storage/wiki.py`; lifecycle FSMs as data — llm-wiki-compiler CLP.
- **Active-page protection**: a reviewed page is never overwritten by a new
  source; conflicts flag it instead — synthadoc RULE 1b.
- **Concept table** as compressed map (definition, sources, status
  `high-confidence | single-source | tentative | contradicted`, maintenance
  note) — Karpathy skill `concept-table.md`.
- **Line-scoped citations** `^[file:L-L]` validated deterministically against
  the source — synthadoc, llm-wiki-compiler `rules-citations.ts`.
- **Confidence + evidence required on semantic edges** — AutoSci `edges.yaml`.
- **Forward link ⇒ reverse link written in the same step** — AutoSci `xref.yaml`.

### Ingest pipeline
- **Content-hash dedup and near-duplicate clustering before any LLM call** —
  llm-tldr `dedup.py`, llm-wiki-compiler `hasher.ts`; the Drive index already
  marks 246 byte-equal copies.
- **Two-phase compile**: extract from all sources of a batch first, then merge
  concepts across sources, then write pages — llm-wiki-compiler
  `extraction-phase.ts` / `extraction-merge.ts`.
- **Ingest decision rules** (flag / update / create; entity profiles get their
  own page) — synthadoc `_DECISION_PROMPT`.
- **Staged candidates + approval pinned to the reviewed content hash** —
  synthadoc `wiki/candidates/`, llm-wiki-compiler `--draft-content-hash`.
- **Knowledge diff printed per ingest** (new / reinforced / challenged / gaps) —
  quicky-wiki `compiler/diff.ts`.
- **Post-ingest validation** (broken wikilinks, unindexed pages, summary) —
  `llm-wiki-agent` `tools/ingest.py::validate_ingest`.
- **Batch expensive passes on a dirty-count threshold**, not per file —
  llm-tldr `dirty_flag.py`.
- **Truncation flag** per source when a body is capped — synthadoc `SourceRef.truncated`.

### Health, lint, audit
- **Health (free, deterministic, every session) vs lint (LLM, periodic)** —
  `llm-wiki-agent` CLAUDE.md boundary table.
- **Pure static lint rule families**: wikilinks, orphans, citations, schema
  enums, xref symmetry, freshness/stale hash, duplicates, empty pages,
  inferred-without-source, index/log sync — llm-wiki-compiler `linter/`,
  AutoSci `tools/lint.py` (with `--fix --dry-run` tiers).
- **Append-only, grep-parseable log** `## [date] op | title` —
  Karpathy, `llm-wiki-agent`, AutoSci `log_grammar`.
- **Immutable audit DB with content-deduped snapshots and rollback** —
  synthadoc `storage/log.py`.
- **Adversarial review gate** (second model flags overstated claims;
  threshold demotes) — synthadoc lint; AutoSci `/review --difficulty adversarial`;
  quicky-wiki `metabolism --redteam`.

### Questioning and refining understanding
- **Answerability judgment → multi-hop retrieval → error abduction on three
  axes (incompleteness, incorrectness, redundancy) → proposed actions →
  evidence-scored review (HIGH exact evidence / MEDIUM inferred / LOW
  ambiguous) → dry-run first, apply only on explicit approval, LOW refused by
  default** — DeepRefine (`refine_runner.py`, `action_review.py`).
- **Trace as provenance record** (`loop_trace_<id>.json`, schema-validated) —
  DeepRefine `agent_loop.py::validate_trace`.
- **Query → synthesis → file it back if it synthesised 3+ sources**
  (crystallization) — Karpathy, AutoSci `/ask --crystallize`; our `/query` already does this.
- **Multi-round refine loop against a target score with a separate reviewer
  model** — AutoSci `/refine`; maps onto DSPy metric + GEPA.
- **Knowledge-gap callout when retrieval is thin** — synthadoc query agent.
- **Epistemic event timeline per claim** (created / reinforced / challenged /
  superseded / resolved) — quicky-wiki `epistemic_events`.

### Agent-side safety
- **User-owned flags**: never invent, flip or drop a user-facing flag from repo
  state — AutoSci Hard Rule 5.
- **Write permissions per skill declared as data** — AutoSci `policy/writers.yaml`.
- **Skill = SKILL.md + reference docs; tools called via Bash; progressive
  disclosure** — AutoSci, dspy-agent-skills, Karpathy skill router.
- **Hooks on ingest/lint completion** (JSON on stdin, blocking or not) —
  synthadoc `hooks/`; our `.claude/hooks/` already does this for chapters.

## Deliberately not adopted

| idea | from | why not |
|---|---|---|
| confidence decay over time | quicky-wiki | research about a novel does not rot with calendar time; it is superseded by decisions. We record `superseded_by` instead |
| LLM-inferred graph edges (pass 2) | llm-wiki-agent | expensive at 680 docs, and canon links must be explicit |
| experiment / paper / poster pipelines | AutoSci | academic workflow, not ours |
| code-structure analysis, daemon, FAISS | llm-tldr | code tool; embeddings optional later (BM25 first) |
| full profile engine, OKF export, MCP server | llm-wiki-compiler | TypeScript; we port a minimal YAML schema + lint, not the platform |
| Obsidian plugin, web UI | synthadoc | optional later; storage stays plain markdown + git |
| copying AGPL code | synthadoc, llm-tldr | patterns only, own implementation in `tools/kpwiki` |
| a second Markdown copy of the **canon** graph | (learnings 2026-09-11 §2) | the graph + `Codex/` views stay the canon record; the wiki is for research |
