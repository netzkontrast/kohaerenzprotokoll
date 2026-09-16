# AutoSci Repository Survey

## 1. What It Is

AutoSci (ΩmegaWiki) is a memory-centric agentic system designed for managing the full scientific research lifecycle. Built on Claude Code and Codex, it ingests research papers and external sources into a structured wiki, orchestrates ideation and experiments via typed skills, and maintains persistent provenance across projects. The system is production-ready (status: internal beta) for research teams building end-to-end automated pipelines from literature ingestion through manuscript publication, with bilingual (English/Chinese) skill support and bidirectional entity linking.

## 2. Architecture

### Directory Layout

```
wiki/                      # Product surface (30+ entity types)
  ├── index.md            # Catalog of all pages (YAML frontmatter)
  ├── log.md              # Append-only chronological record
  ├── papers/             # Paper summaries with venue, year, importance (1-5)
  ├── concepts/           # Cross-paper technical concepts (maturity: stable/active/emerging/deprecated)
  ├── topics/             # Research direction maps
  ├── people/             # Researcher profiles (type: researcher|team|organization)
  ├── ideas/              # Research ideas with lifecycle status + novelty_score
  ├── experiments/        # Experiment records with outcome enum
  ├── methods/            # Reusable method entities (parent/child hierarchy)
  ├── Summary/            # Domain-wide surveys
  ├── foundations/        # Terminal: background knowledge (no outward links)
  ├── outputs/            # Generated artifacts (Related Work, paper drafts)
  └── graph/              # Auto-generated (edges.jsonl, citations.jsonl, context_brief.md, open_questions.md)

raw/                       # User-owned / skill-writable
  ├── papers/             # User-owned .tex/.pdf (read-only to skills)
  ├── notes/              # User-owned .md notes (read-only)
  ├── web/                # User-owned HTML/Markdown (read-only)
  ├── discovered/         # Skill-writable: fetched by /init and /daily-arxiv
  └── tmp/                # Skill-writable: intermediate state for /init

runtime/                   # Single source of truth for contract
  ├── loader.py           # Schema access API (shared by tools/lint.py and tools/research_wiki.py)
  ├── schema/
  │   ├── entities.yaml   # Entity kinds, fields, types, enums, lifecycle
  │   ├── edges.yaml      # Edge types, direction, confidence, workflow
  │   ├── xref.yaml       # Forward/reverse link rules (bidirectional sync)
  │   └── conventions.yaml # Slug rule, path pattern, ownership zones
  └── policy/
      └── writers.yaml    # Field/edge write permissions per skill (declarative only)

templates/                 # Body section skeletons per entity kind
  ├── papers.md.tmpl      # Problem & Context, Key idea, Method, Experiment & Results, Limitations, etc.
  ├── concepts.md.tmpl    # Definition, Intuition, Variants, Comparison, Known limitations, etc.
  ├── ideas.md.tmpl       # Hypothesis, Approach, Related ideas, Status, etc.
  └── [9 entity types total]

tools/                     # Deterministic Python (2861 lines research_wiki.py, 1170 lines lint.py)
  ├── research_wiki.py    # Wiki engine: init, add-edge, batch-edges, find, query, neighbors, compile-context, transition, checkpoint
  ├── lint.py             # Validator: wikilinks, orphans, required fields, enum validation, xref symmetry
  ├── discover.py         # Paper recommendation (anchor-driven, topic-driven, venue-filtered, wiki-state)
  ├── init_discovery.py   # Bootstrap discovery for /init
  ├── daily_arxiv.py      # arXiv recommendations with multi-source ranking
  └── [10+ other tools: fetch_s2.py, fetch_deepxiv.py, poster.py, serve.py, etc.]

.claude/skills/            # Claude Code skills (30+ skill directories, bilingual in i18n/)
  ├── ask/                 # Retrieve, synthesize, optionally crystallize back
  ├── check/               # Tiered lint report with --fix and --suggest
  ├── prefill/             # Seed wiki/foundations/ to avoid duplicate textbook pages
  ├── ingest/              # Paper → wiki pages + edges + citations
  ├── discover/            # Ranked shortlist without ingest side-effects
  ├── novelty/             # Multi-source novelty verification (WebSearch + S2 + DeepXiv + wiki + Review LLM)
  ├── review/              # Cross-model review (Review LLM independent reviewer)
  ├── refine/              # Multi-round iterative improvement loop (review → fix → re-review)
  ├── ideate/              # 5-phase research idea generation + pilot
  ├── edit/                # Add/remove sources or update wiki content
  └── [20+ more: exp-design, exp-run, exp-status, exp-eval, exp-pilot-run, exp-pilot-eval, etc.]

i18n/                      # Bilingual source of truth
  ├── en/skills/           # English skill definitions (shared source)
  ├── en/shared-references/# Reference docs (cross-model-review.md, etc.)
  ├── zh/skills/           # Chinese skill definitions
  └── setup.sh regenerates .claude/skills/ and .agents/skills/ from these
```

### Runtime Contract (Schema + Policy + Templates)

**Entities** (declared in `runtime/schema/entities.yaml`):
- **papers** — title, slug, arxiv, venue, year, tags, importance (1-5), s2_id, tldr, contribution_type, datasets, code_url, cited_by
- **concepts** — title, aliases, tags, maturity (stable|active|emerging|deprecated), definition, key_papers, first_introduced, related_concepts, linked_ideas, parent_topic
- **topics** — title, tags, key_venues, related_topics, key_people, key_papers, linked_ideas
- **ideas** — title, slug, status (proposed|in_progress|tested|validated|failed), origin, origin_gaps, tags, target_venue, novelty_score (1-5), priority (1-5), pilot_result, failure_reason (required when status=failed), linked_experiments, date_proposed, date_resolved
- **experiments** — title, slug, status (planned|running|completed|abandoned), linked_idea, evaluates_methods, hypothesis, tags, setup (model, dataset, hardware, framework), metrics, baseline, outcome (succeeded|failed|inconclusive), key_result, date_planned, date_completed, run_log, remote (server, gpu, session, etc.)
- **methods** — name, slug, type (architecture|training|inference|evaluation|data|benchmark|system|optimization|prompting|protocol|other), tags, source_papers, parent_methods, child_methods, realizes_concepts, code_repo, date_updated
- **people** — name, affiliation, research_areas, homepage, scholar, type.kind (researcher|team|organization)
- **foundations** — terminal (no outward links). title, slug, domain, status (mainstream|historical), aliases, first_introduced, source_url

**Edge Types** (from `runtime/schema/edges.yaml`):
- **Paper-to-paper**: `builds_on`, `challenges`, `same_problem_as` (symmetric), `similar_method_to` (symmetric) — all require confidence (high|medium|low) + evidence
- **Paper-to-concept**: `introduces_concept`, `uses_concept`, `extends_concept`, `critiques_concept` — all require confidence + evidence
- **Cross-workflow** (endpoints broad, stored in graph/): `supports`, `contradicts`, `tested_by`, `invalidates`, `addresses_gap`, `derived_from`, `inspired_by` — with optional evidence
- **Citation**: `cites` (paper → paper) with source (semantic_scholar|parsed_bib|manual), stored separately in graph/citations.jsonl

**Xref Rules** (bidirectional link contract in `runtime/schema/xref.yaml`):
- papers.Related (body_section) ↔ concepts.key_papers (frontmatter_field) — append_slug on reverse
- ideas.origin_gaps (frontmatter) ↔ concepts.linked_ideas (frontmatter) — append_slug on reverse
- experiments.linked_idea (frontmatter) ↔ ideas.linked_experiments (frontmatter) — append_slug on reverse
- [12 forward/reverse rules total]; foundations are terminal (any link to foundations writes no reverse)

**Ownership Zones** (from `runtime/schema/conventions.yaml`):
- User-owned (skills must not overwrite): raw/papers, raw/notes, raw/web
- Tools-only (only via research_wiki.py): wiki/graph
- Append-only (never rewritten in place): wiki/log.md

**Slug Rule**: `^[a-z0-9]+(-[a-z0-9]+)*$` (lowercase, hyphen-separated, no spaces)

### Write Permissions Per Skill (Declarative in `runtime/policy/writers.yaml`)

**Paper identity/ranking** (frozen after first write): ingest
**Method provenance**: ingest, init, edit
**Topic curation**: ingest, init, edit
**Concept taxonomy**: ingest, init, edit
**Idea lifecycle**: ideate, exp-eval, exp-pilot-eval, refine
**Experiment lifecycle**: exp-design, exp-run, exp-status, exp-eval
**Paper-paper semantic edges**: ingest only
**Paper-concept semantic edges**: ingest only
**Cross-workflow edges**: supports (ingest, exp-eval); contradicts (ingest); tested_by (exp-design); invalidates (exp-eval); addresses_gap (ideate); inspired_by (ideate)

### Wiki Engine (tools/research_wiki.py)

**Core commands**:
- `init <wiki_root>` — scaffold wiki structure
- `slug "<title>"` — slugify string per rule
- `set-meta <path> <field> <value> [--append]` — update frontmatter
- `add-edge --from <id> --to <id> --type <type> [--evidence "..."] [--confidence high|medium|low]` — graph edge write
- `batch-edges` — bulk edge writes (stdin JSON array)
- `find <wiki_root> <entity_type> [--field value ...]` — search by entity type and field
- `query <wiki_root> <subquery> [options]` — semantic queries
- `neighbors <wiki_root> <node_id> [--depth N] [--edge-type T]` — BFS traversal
- `compile-context <wiki_root> --for <purpose> [--max-chars 8000]` — context generation for skills
- `rebuild-context-brief`, `rebuild-open-questions`, `rebuild-index` — derived data
- `transition <path> --to <status>` — lifecycle validation
- `checkpoint-save`, `checkpoint-load` — session-resumable state for batch operations

**Data source**: YAML frontmatter + body sections. Single Python package `runtime.loader` exposes schema as dicts (ENTITIES, EDGES, XREF, CONVENTIONS, WRITERS) — zero codegen.

### Lint Validator (tools/lint.py)

**Checks** (1170 lines; outputs JSON via `--json` flag):
1. Broken wikilinks — [[slug]] target missing
2. Orphan pages — zero incoming links
3. Missing required fields (per entity type: papers needs title/slug/tags/importance, concepts needs title/tags/maturity/key_papers, ideas needs title/slug/status/origin/tags/priority, etc.)
4. Enum/range validation (papers.importance ∈ {1-5}, concepts.maturity ∈ {stable, active, emerging, deprecated}, ideas.status ∈ {proposed, in_progress, tested, validated, failed}, etc.)
5. Conditional required (ideas.failure_reason required when status=failed)
6. Xref asymmetry — forward link without matching reverse
7. Graph edge consistency — from/to nodes exist as wiki pages
8. Citation consistency — papers in cites edges exist

**Modes**:
- Default (report-only): `python3 tools/lint.py --wiki-dir wiki/ --json`
- Auto-fix: `python3 tools/lint.py --wiki-dir wiki/ --fix --json` (fills missing required fields with defaults, completes xref reverses)
- Preview: `python3 tools/lint.py --wiki-dir wiki/ --fix --dry-run --json`
- Suggest: `python3 tools/lint.py --wiki-dir wiki/ --suggest` (recommendations for non-fixable issues)

### Skills Structure and Chaining

Each skill is a directory under `.claude/skills/` with:
- `SKILL.md` — frontmatter (description, argument-hint) + workflow sections (Inputs, Outputs, Wiki Interaction, Steps)
- Supporting `.md` references — dedup-policy.md, cross-references.md, error-handling.md, etc.
- No Python code in the skill itself; skills orchestrate calls to `tools/` via Bash

**Skill chains** (example flow):
1. `/prefill [domain]` — seed foundations to avoid duplication
2. `/init [topic]` — bootstrap wiki from raw/papers/, raw/notes/, raw/web/, with optional discovery
3. `/ingest [paper]` — single paper → wiki pages + edges
4. `/discover --venue iclr --year 2024` — ranked shortlist, no side-effects
5. `/ask "what is the core difference between LoRA and Adapter?"` — retrieve, synthesize, optionally crystallize
6. `/ideate [research-direction]` — 5-phase pipeline: landscape → brainstorm → filter → write → pilot
7. `/novelty [idea-slug]` — multi-source novelty verification, optionally write score
8. `/review [artifact-slug]` — Review LLM independent review (standard|hard|adversarial)
9. `/refine [artifact-slug]` — multi-round loop: review → fix → re-review until target score
10. `/check --fix` — tiered lint report with auto-fix
11. `/exp-design [idea]` → `/exp-run` → `/exp-eval` — experiment pipeline
12. `/daily-arxiv` — scheduled arXiv recommendations

**Resumable state**: Skills use `.checkpoints/` to save and recover batch operation progress (e.g., `.checkpoints/init-sources.json` passed from /init to /ingest).

### Internationalization (i18n)

Bilingual source: `i18n/{en,zh}/skills/` (skill SKILL.md files) + `i18n/{en,zh}/shared-references/` (reference docs)
- Setup script: `./setup.sh --lang en` regenerates `.claude/skills/` and `.agents/skills/` from the selected language's source
- Enables skill authoring once, deployment to Claude Code and Codex in both languages
- Each runtime (Claude Code `.claude/`, Codex `.agents/`) gets symlinked or copied skills via setup

### Configuration and Hooks

- `config/settings.local.json.example` — Claude Code permissions (Bash, Read, Edit, WebSearch, WebFetch, MCP)
- `config/.env.example` — API keys (ANTHROPIC_API_KEY, OPENAI_API_KEY, SEMANTIC_SCHOLAR_API_KEY, DEEPXIV_TOKEN, LLM_API_KEY)
- Bilingual AGENTS.md generated from i18n/ at setup time
- No explicit hook system visible; skills are invoked manually or via daily-arxiv CI

## 3. Concepts Worth Stealing

1. **Schema-as-contract approach** (runtime/loader.py + runtime/schema/ + runtime/policy/)
   - What: YAML files declare entity kinds, field types, enums, required fields, lifecycle states, edge types, forward/reverse xref rules, and write permissions. Python loader exposes as dicts at import time; zero codegen; all tools (lint.py, research_wiki.py, skills) import and use the same schema.
   - Why for novel wiki: Enforce entity consistency across 680 research sources without replicating schema in multiple places. New field types or enum values require only YAML edit, no code changes to validation/linting/prompts.
   - Files: `runtime/schema/{entities,edges,xref,conventions}.yaml`, `runtime/loader.py`, `runtime/policy/writers.yaml`

2. **Bidirectional xref reciprocity rule** (runtime/schema/xref.yaml)
   - What: Declares forward→reverse link pairs. When skills write a paper.Related wikilink to a concept, the reverse (concept.key_papers) is auto-updated. Foundations (terminal pages) are exempted — they receive inward links but write no reverse.
   - Why for novel wiki: Canon pages must stay in sync with research pages without manual reverse-link edits. Prevents orphaned references and "ghost" citations that break the provenance graph.
   - Files: `runtime/schema/xref.yaml` (12 rules covering papers/concepts/ideas/topics/methods/experiments); xref validation in `tools/lint.py` + auto-fix

3. **Terminal entity type (foundations)** (runtime/schema/entities.yaml, foundations.md.tmpl)
   - What: Foundations (background knowledge, textbook material) are marked `terminal: true` — they receive incoming links but never write reverses. They seed `wiki/foundations/` and are never auto-created by /ingest.
   - Why for novel wiki: Separate canon axioms (hard rules, worldbuilding axioms) from research claims. Prevents research ingestion from mutating foundational knowledge; canon axioms can be citable without bidirectional entanglement.
   - Files: `runtime/schema/entities.yaml` (foundations block with `terminal: true`), `/prefill` skill to seed them, `/ingest` dedup logic to avoid duplicate foundation creation

4. **Lifecycle states with transitions** (runtime/schema/entities.yaml)
   - What: Ideas, experiments, and concepts have lifecycle.transitions maps (e.g., ideas: proposed→in_progress→tested→[validated|failed]; experiments: planned→running→[completed|abandoned]). The schema allows transition, not arbitrary state changes.
   - Why for novel wiki: Enforce narrative flow (ideas can't jump from proposed to validated without testing; experiments can't go backward). Provides auditability and prevents impossible states.
   - Files: `runtime/schema/entities.yaml` (lifecycle.transitions); validation via `tools/research_wiki.py transition --to <status>`

5. **Confidence + evidence on semantic edges** (runtime/schema/edges.yaml, edges validation)
   - What: Paper-to-paper and paper-to-concept semantic edges require `confidence` (high|medium|low) and `evidence` fields. Linter enforces both are present.
   - Why for novel wiki: Distinguish high-confidence plot connections from speculative links. Allows queries like "what papers are high-confidence related?" without drowning in weak associations.
   - Files: `runtime/schema/edges.yaml` (attributes: confidence required, evidence required), `tools/lint.py` edge validation, `tools/research_wiki.py add-edge` rejects missing values

6. **Prefill skill to seed foundations** (`.claude/skills/prefill/`, `.claude/skills/prefill/foundations-catalog.yaml`)
   - What: `/prefill [domain]` reads a catalog of foundational concepts (general, NLP, CV, ML Systems, Robotics), fetches Wikipedia summaries, and writes terminal `wiki/foundations/{slug}.md` pages. Idempotent — skips already-seeded concepts.
   - Why for novel wiki: Prevent /ingest from creating duplicate concept pages for physics axioms, logic foundations, psychology basics. Canon rules should pre-populate as foundations so research papers dedup against them.
   - Files: `.claude/skills/prefill/SKILL.md` (workflow), `.claude/skills/prefill/foundations-catalog.yaml` (seed list)

7. **Ask skill with crystallization** (`.claude/skills/ask/`)
   - What: `/ask "question"` retrieves relevant pages, synthesizes an answer with `[[slug]]` citations, and with `--crystallize` writes the answer back as a new output page or new concept, updating graph edges and index.
   - Why for novel wiki: Exploration compounds — user questions about research become new wiki entities (cross-paper insights). Prevents ad-hoc "I learned X" moments from disappearing. Answer writes trigger xref reverse-updates and context rebuilds.
   - Files: `.claude/skills/ask/SKILL.md` (workflow, crystallize modes), `tools/research_wiki.py compile-context` used for retrieval

8. **Check skill with tiered fix reports** (`.claude/skills/check/`, `tools/lint.py`)
   - What: `/check --fix` runs lint, auto-fixes deterministic issues (missing default fields, incomplete xref reverses), and outputs a tiered report (auto-fixable / non-fixable). `--suggest` gives recommendations.
   - Why for novel wiki: Users can safely run health checks and auto-fix without manual intervention. Three-tier output (red/yellow/blue) prioritizes what matters most. Helps teams discover orphan canon pages or contradictions.
   - Files: `.claude/skills/check/SKILL.md`, `tools/lint.py` (auto-fix logic), `runtime/schema/entities.yaml` (required fields + defaults)

9. **Review LLM as independent reviewer** (`.claude/skills/review/`)
   - What: `/review [artifact] --difficulty [standard|hard|adversarial]` uses an independent Review LLM (Codex, DeepSeek, etc., via LLM_API_KEY + LLM_BASE_URL) to critique research ideas, proposals, experiments, or paper drafts. Outputs structured score (1-10), strengths, weaknesses, wiki entity mapping.
   - Why for novel wiki: Cross-model review catches blind spots. Research ideas can be vetted against published wiki knowledge without author bias. Multi-round hard/adversarial modes simulate harsh reviewers.
   - Files: `.claude/skills/review/SKILL.md`, `shared-references/cross-model-review.md`, `mcp-servers/llm-review/` (MCP integration)

10. **Refine skill as multi-round improvement loop** (`.claude/skills/refine/`)
    - What: `/refine [artifact] --max-rounds N --target-score M` repeatedly calls /review, parses feedback, fixes the artifact, and re-reviews until score reaches M or max-rounds exhausted. Tracks score trajectory and cumulative fixes.
    - Why for novel wiki: Research artifacts (ideas, experiment plans, paper drafts) improve incrementally. Refine loops enforce quality gates (target-score) without manual rewriting cycles. Updates wiki entities as fixes are applied.
    - Files: `.claude/skills/refine/SKILL.md` (workflow: init → loop: review→parse→fix→rebuild-context → check termination)

11. **Novelty skill with multi-source verification** (`.claude/skills/novelty/`)
    - What: `/novelty [idea-description-or-slug]` searches WebSearch, Semantic Scholar, DeepXiv (semantic search), existing wiki pages, and arXiv recent preprints. Review LLM cross-verifies. Outputs novelty score (1-5), closest prior work, differentiation. Can write score back with `--write`.
    - Why for novel wiki: Ideas must be checked against published literature + wiki ideas to avoid reinventing failed approaches. Novelty verification prevents wasted effort and identifies where to position novel contributions.
    - Files: `.claude/skills/novelty/SKILL.md`, `tools/fetch_s2.py`, `tools/fetch_deepxiv.py`, `tools/discover.py` (underlying search tools)

12. **Ideate skill with 5-phase pipeline** (`.claude/skills/ideate/`)
    - What: `/ideate [research-direction]` executes: landscape scan → dual-model brainstorm (Claude + Review LLM) → filter & validation → write to wiki (creates idea page) → pilot experiment. Outputs idea pages with status (proposed|in_progress), novelty scores, pilot results.
    - Why for novel wiki: Full research idea lifecycle in one orchestrated pipeline. Combines landscape knowledge (what exists), creativity (brainstorm), rigor (review), and early validation (pilot). Results are wiki pages (provenance recorded).
    - Files: `.claude/skills/ideate/SKILL.md` (5 phases), integration with `/novelty` (Phase 4), `/review` (phase 3), `/exp-pilot-run` + `/exp-pilot-eval` (phase 5)

13. **User-owned flags (argument-hint)** (CLAUDE.md, every skill's SKILL.md argument-hint section)
    - What: Skills declare which user-facing flags are "user-owned" (e.g., `--crystallize` for /ask, `--write` for /novelty, `--visualize` for /ingest). Rule: do not invent, flip, or drop these flags based on repo state; use defaults only when skill docs specify omission behavior; otherwise ask the user.
    - Why for novel wiki: Prevents agents from auto-enabling side-effects. User explicitly chooses whether to crystallize a query into the wiki, write a novelty score back, or visualize the canvas. Preserves intentionality.
    - Files: `CLAUDE.md` (Hard Rule 5), every skill's argument-hint field in SKILL.md frontmatter

14. **Append-only log with parseable grammar** (runtime/schema/conventions.yaml, tools/research_wiki.py log)
    - What: `wiki/log.md` is append-only and never rewritten. Entries follow grammar: `## [{date}] {skill} | {details}` (e.g., `## [2026-09-15] ingest | paper-title` or `## [2026-09-15] ideate | created idea with novelty_score=4`). Grep-parseable.
    - Why for novel wiki: Audit trail of who (which skill) did what when. Enables recovery of lost work, versioning, and traceability. Append-only guarantees immutability.
    - Files: `runtime/schema/conventions.yaml` (log_grammar), `tools/research_wiki.py log` (writer), every skill appends via `tools/research_wiki.py log "message"`

15. **Discovered/tmp raw dirs for skill-writable external sources** (runtime/schema/conventions.yaml ownership zones)
    - What: `raw/papers/, raw/notes/, raw/web/` are user-owned (read-only to skills). `raw/discovered/` is skill-writable (filled by /init discovery, /daily-arxiv). `raw/tmp/` is skill-writable (intermediate state for /init paper preparation). Enforced by ownership rules.
    - Why for novel wiki: Separates user's primary research sources (never auto-overwritten) from skill-fetched candidates (auto-refreshable). Allows re-running /init discovery without losing user drops.
    - Files: `runtime/schema/conventions.yaml` (ownership.user_owned, ownership.append_only), `/init` workflow uses `raw/discovered/` and `raw/tmp/`, `/daily-arxiv` fetches to `raw/discovered/`

## 4. Reusable Code/Assets

1. **runtime/loader.py** (25 KB, Python 3.9+)
   - Single schema access API for tools and skills. Zero dependencies beyond PyYAML. Exports ENTITIES, EDGES, XREF, CONVENTIONS, WRITERS dicts + helper functions for edge type queries.
   - Dependency: PyYAML (already in requirements.txt)
   - Can be vendored directly; add `sys.path.insert(0, ...)` to import from sibling directory

2. **tools/lint.py** (1170 lines, Python 3.9+)
   - Comprehensive wiki validator: broken links, orphans, required fields, enum validation, xref symmetry, edge consistency. Outputs JSON. Auto-fix mode.
   - Dependencies: PyYAML, pathlib (stdlib), json (stdlib)
   - Could be extracted as standalone tool for any wiki using the schema contract

3. **tools/research_wiki.py** (2861 lines, Python 3.9+)
   - Core wiki engine: frontmatter read/write, graph add-edge, batch operations, find/query/neighbors, context compilation, lifecycle transitions, checkpoint save/load
   - Dependencies: pathlib, json, yaml, re, subprocess (all stdlib or PyYAML)
   - Could be ported as a library with a CLI interface for other wikis

4. **runtime/templates/{entity-kind}.md.tmpl** (9 files, Markdown with {{frontmatter}} placeholder)
   - Skeleton body sections for each entity type (papers, concepts, ideas, experiments, methods, topics, people, Summary, foundations)
   - Zero dependencies; pure templates
   - Could be customized per domain

5. **runtime/schema/*.yaml** (4 files: entities, edges, xref, conventions)
   - Declarative schema definitions
   - Zero dependencies
   - Could be adapted for other knowledge domains by changing enum values, adding entity types, defining new xref rules

6. **tools/discover.py** (1255 lines, Python 3.9+)
   - Paper discovery with ranking: anchor-driven, topic-driven, venue-filtered, wiki-state-based. Calls Semantic Scholar, DeepXiv, Paper Copilot API.
   - Dependencies: PyYAML, requests, json (stdlib)
   - Could be extracted for other research ranking pipelines

7. **tools/daily_arxiv.py** (1534 lines, Python 3.9+)
   - arXiv recommendation feed: multi-source ranking (arXiv + Semantic Scholar + DeepXiv), digest generation, optional email
   - Dependencies: requests, yaml, json, datetime (stdlib)
   - Could be standalone daily-digest tool

8. **Skill structure (.claude/skills/{skill-name}/)** (30+ directories with standardized SKILL.md + references)
   - Template: SKILL.md frontmatter + description/argument-hint sections + Inputs/Outputs/Wiki Interaction/Workflow steps
   - Supporting .md files for references (dedup-policy.md, cross-references.md, error-handling.md)
   - Could be copied as template for new skills

## 5. Not Useful / Caveats

- **Experiment execution pipeline** (exp-run with remote GPU support, remote.py) assumes local Linux/macOS environment with ssh/rsync/screen. Windows + WSL2 partial support only. Not portable to cloud-native setups without refactoring.
- **Daily arXiv CI** (daily_arxiv.py + GitHub Actions) relies on Codex CLI or legacy Claude Code action; no Vercel/other cloud platforms tested.
- **Review LLM integration** (LLM_API_KEY + LLM_BASE_URL) assumes OpenAI-compatible API. Claude Code integration is single-model only; cross-model review only works with external LLM setup.
- **Experiment metadata** (setup.model, setup.dataset, setup.hardware, setup.framework) are free-text strings, not enums. No enforcement of hardware naming conventions or dataset URLs.
- **Graph visualization** (tools/serve.py on localhost:8765) requires running a separate Python server; no built-in web deploy documented. Obsidian Canvas export exists but offline-only.
- **i18n** is bilingual (EN/Chinese) only. Adding more languages requires duplicating entire skill trees under `i18n/{lang}/`.
- **Poster skill** (tools/poster.py, 1313 lines) is specific to academic paper posters; not useful for non-academic domains.
- **License** is MIT; check compatibility if integrating into proprietary systems.

## 6. One-Paragraph Verdict

AutoSci's architecture is directly applicable to a novel research wiki with canon/research separation: the schema-as-contract approach (YAML + loader.py) allows separating canon axioms (foundations, terminal) from research sources (papers, ideas, experiments) with zero code duplication. The bidirectional xref system ensures canon edits propagate without manual reverse-link updates. The `/prefill` skill and foundations concept map perfectly onto novel worldbuilding (seed physics rules, logic axioms, character archetypes as terminal foundation pages). Skills like `/ask` with crystallization, `/review` with independent LLM, and `/refine` with iterative improvement loops provide templates for knowledge exploration without hallucination. The tiered lint system (`/check`) and multi-source novelty verification (`/novelty`) protect against contradictions and silent canon drift. The append-only log and checkpoint system support session-resumable state for batch ingestion of 680 sources. Core assets (loader.py, lint.py, research_wiki.py, schema YAML) are portable and worth vendoring; the skill orchestration model (tools calling tools via Bash, no cross-skill coupling) is well-suited for Claude Code subagent dispatch. Limitations: experiment execution is Linux-biased, i18n is bilingual-only, and cloud deploy story is thin — but the core wiki + linting + skill chaining infrastructure is production-ready and battle-tested on multi-project research teams.
