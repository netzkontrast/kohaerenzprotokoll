# LLM Wiki Bootstrap: Repository Survey & Analysis

## 1. What It Is

**Karpathy LLM Wiki Bootstrap** is an installable Claude Code skill that scaffolds and operates persistent, LLM-maintained Markdown wikis built from immutable raw sources. Instead of query-time RAG retrieval, it compiles source knowledge into a structured, interlinked wiki layer that remains maintained and queryable. The skill provides three core workflows (ingest, query, lint) plus optional local BM25 full-text search, seeded with a working reference wiki demonstrating the pattern in action.

## 2. The Karpathy LLM-Wiki Principles

From `karpathy-llm-wiki-original.md`:

- **Three-layer architecture**: "Raw sources" (immutable evidence), "The wiki" (LLM-generated derived knowledge), and "The schema" (operating contract defining how the LLM behaves).

- **The wiki is a persistent, compounding artifact**: "The cross-references are already there. The contradictions have already been flagged. The synthesis already reflects everything you've read." Knowledge is "compiled once and then kept current, not re-derived on every query."

- **The LLM writes and maintains all of it**: "You never (or rarely) write the wiki yourself." Humans curate sources and ask questions; the LLM performs all "summaries, cross-referencing, filing, and bookkeeping."

- **Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase**: Uses familiar tools (Obsidian, git, Markdown) but shifts the development metaphor from documents to versioned knowledge.

- **Raw sources are immutable**: "These are immutable — the LLM reads from them but never modifies them. This is your source of truth." Evidence and derived judgment are separated.

- **Index and log are primary navigation**: "`index.md` is content-oriented" (page catalog with one-line summaries by category); "`log.md` is chronological" (append-only record of operations, grepped as `^## [YYYY-MM-DD]`). Together they scale to ~100 sources and hundreds of pages without requiring embedding infrastructure.

- **The maintenance problem is the real blocker**: "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping." LLMs solve this by having "near-zero" maintenance cost.

- **Good answers should be filed back**: Query results can become "new pages" in the wiki, so "explorations compound in the knowledge base just like ingested sources do."

- **The schema is the operating contract**: "A document (e.g. CLAUDE.md for Claude Code or AGENTS.md for Codex) tells the LLM how the wiki is structured, what the conventions are, and what workflows to follow."

## 3. Architecture of This Implementation

### Directory Layout
```
raw/                           # Immutable source files (read-only after bootstrap)
raw/assets/                    # Image and attachment storage
wiki/                          # LLM-maintained derived layer
  ├── index.md                 # Content catalog and primary navigation
  ├── concept-table.md         # Compressed concept map (definitions, relationships, maintenance)
  ├── log.md                   # Append-only operation log
  ├── overview.md              # Top-level synthesis
  ├── sources/                 # One summary per ingested source
  ├── entities/                # People, organizations, tools, projects
  ├── concepts/                # Durable ideas and frameworks
  ├── comparisons/             # Side-by-side analyses
  └── synthesis/               # Cross-wiki interpretations
SCHEMA.md                      # Operating contract (single source of truth for agent behavior)
AGENTS.md                      # Thin pointer to SCHEMA.md (runtime-specific)
EXTEND.md                      # (Optional) preferences for BM25, language, ingest behavior
scripts/wiki_fts.py            # (Optional) local SQLite FTS5 BM25 search helper
indexes/fts.sqlite             # (Rebuildable) BM25 index
exports/                       # (Rebuildable) BM25 export artifacts
```

### Page Schema
Every wiki page (except `index.md` and `log.md`) has **YAML frontmatter** with:
```yaml
---
title: Page Title
type: source-summary | entity | concept | comparison | synthesis | overview
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [source-file.md]  # filenames only, immutable audit trail
tags: [tag1, tag2]
---
```

Bodies use `[[wikilink]]` syntax for internal cross-references and cite sources inline as `[Title](../sources/slug.md)`.

### Ingest Workflow
From `skill/references/workflows/ingest.md`:

1. **Pre-flight**: Check EXTEND.md preferences, verify source exists, detect language, check if already ingested
2. **Read & comprehend**: Extract key claims, entities, concepts; identify contradictions
3. **Discuss**: Present 2–3 bullet summary to user; gather emphasis guidance
4. **Create source summary**: Write `wiki/sources/{slug}.md` with summary, key claims, entities, concepts, quotes
5. **Ripple updates**: If BM25 enabled, search for related pages before creating new ones; merge or create entity/concept pages
6. **Contradiction format**: Flag discrepancies with source citations and resolution status
7. **Update concept table**: Add/revise rows for every concept touched (status: high confidence | single-source | tentative | contradicted)
8. **Update index, log, overview**: Add entries, append log line, revise synthesis if warranted
9. **Rebuild BM25**: `python3 scripts/wiki_fts.py build`

### Query Workflow
From `skill/references/workflows/query.md`:

1. **Navigate via index**: Read `wiki/index.md` (and `concept-table.md` for conceptual questions)
2. **Search (optional)**: If BM25 enabled, use `python3 scripts/wiki_fts.py search "{query}"` to find candidate pages; check freshness with `stats`
3. **Read pages**: Open returned wiki pages and read full context (never answer from snippets alone)
4. **Synthesize**: Compose answer with inline wiki citations, confidence levels, and gaps
5. **File decision**: If answer is worthy (comparison, new connection, 3+ source synthesis), create a new wiki page; update index, concept table, log

### Lint Workflow
From `skill/references/workflows/lint.md`:

1. **Full scan**: Read index, concept table, and every page; build internal model of links, sources, contradictions, tags
2. **Run checks**: Detect orphan pages, broken wikilinks, missing pages, index drift, concept-table drift, unresolved contradictions, stale claims, stale overview, missing backlinks, isolated clusters
3. **Report by severity**: High (broken links, index drift, stale claims), Medium (orphans, contradictions, search staleness), Low (single-source concepts, empty pages)
4. **Fix approved items**: Update or delete pages, rebuild BM25, append log

### BM25 Search Layer
`skill/references/templates/wiki_fts.py` is a ~400-line SQLite FTS5 wrapper that:
- Chunks wiki pages by heading
- Exports to CSV with fields: `chunk_id, page_path, title, type, heading_path, ordinal, sources, tags, updated, text`
- Commands: `doctor` (check health), `build` (rebuild index), `search "{query}"` (BM25 ranked results), `stats` (freshness check)
- **Critical rule**: BM25 is a candidate finder only; agent must open the returned `page_path` files before citing them

### Skill Design
`skill/SKILL.md` enforces:
- **Single SCHEMA.md**: Config lives in one place; pointer files (CLAUDE.md, AGENTS.md) are thin redirects
- **Intent router**: Triggers for bootstrap, ingest, query, lint, BM25 config
- **Reference loading rules**: Load only the workflow file needed for the current task (progressive disclosure)
- **Hard rules**: Never overwrite wikis without approval; never modify `raw/`; always update index.md and log.md on changes; preserve source language

## 4. Concepts Worth Stealing

1. **Source-of-truth separation** (`wiki/concepts/source-of-truth-separation.md`): Keep raw immutable, let derived pages be rewritten. Why: canon/research mixing is the death of narrative wikis. For Kohärenz Protokoll, this means raw Google Drive research stays untouched; wiki synthesizes and flags canon vs. research boundaries explicitly.

2. **Concept-table as compressed map** (`wiki/concept-table.md`): Replaces the index for understanding. Each row carries: definition, role in wiki, sources, related pages, status (high confidence | single-source | tentative | contradicted), maintenance note. Why: A novel wiki needs to track not just "what pages exist" but "what is known with what confidence, from which sources, and what next questions to investigate."

3. **Contradiction block format** (ingest.md, step 4): Explicit resolution field (pending | Source B supersedes | both valid in different contexts). Why: For a novel, contradictions between character arcs, physics rules, or event timelines must be surfaced, not hidden. The resolution field prevents silent canon drift.

4. **Operation log as git-greppable structure** (`log.md`, with `^## [YYYY-MM-DD] <op> | <title>`): Parseable in one line. Why: Audit trail for "when did we last ingest research about X" or "what was decided about storyform Y."

5. **Preference preflight (EXTEND.md)** (`references/config/extend-schema.md`): Loads user preferences before every operation (ingest, query, lint, BM25). Why: Makes wiki language, search mode, rebuild behavior configurable without touching skill code. For novel: can toggle "strict canon-only" mode vs. "research exploratory" mode.

6. **Ripple updates via BM25 search** (ingest.md, step 4): Before creating a new concept page, search existing pages to merge rather than duplicate. Why: Keeps the graph coherent as research grows from 680 documents to thousands.

7. **The ingest→discuss→create loop** (ingest.md, steps 2–3): Present findings to user before writing pages. Why: Prevents LLM hallucination; forces human judgment on emphasis. Critical for fiction where tone and implication matter as much as facts.

8. **Filed query artifacts** (`wiki/concepts/filed-query-artifacts.md`): Query answers become pages. Why: Allows explorations to compound; every synthesis can become canon if it's good enough. For novel research, "why did Juna choose this?" can become a character motivation page.

9. **Schema as single source of truth** (SCHEMA.md): All operating rules in one document; thin pointers elsewhere. Why: No silent drift between CLAUDE.md and AGENTS.md; one authoritative version that skill always reads.

10. **BM25 freshness gate** (query.md, step 1): Check `python3 scripts/wiki_fts.py stats` before searching; rebuild if stale. Why: Prevents answering from outdated indexes. For novel wiki, critical when research evolves rapidly.

## 5. Reusable Code/Assets

- **`skill/references/templates/wiki_fts.py`** (lines 1–400+): Vendorable SQLite FTS5 wrapper. Language: Python. No dependencies beyond stdlib + sqlite3. Can be ported as-is.
- **`skill/references/templates/schema.md`**: Schema template with all page types, frontmatter rules, operation protocols. Language: Markdown. Adapt by inserting domain-specific snippets from `references/templates/domain-page-types.md`.
- **`skill/references/templates/concept-table.md`**: Concept table structure with Maintenance Rules, Concept Clusters, Concepts matrix. Template for the wiki's compressed map.
- **`skill/references/workflows/ingest.md`** (through lint.md): Complete step-by-step workflow procedures. Language: Markdown. Adapt for novel by adding canon/research flag checks.
- **`llm-wiki/SCHEMA.md`**: Working example of generated SCHEMA.md with all page types, protocols, BM25 rules. Language: Markdown. Shows what output looks like after skill runs.
- **`llm-wiki/wiki/concept-table.md`**: Populated concept table with 11 concepts, showing the maintenance rules and Concept Clusters pattern in practice.
- **`skill/SKILL.md`**: Skill metadata and intent router. Installable as-is. Language: Markdown + YAML frontmatter.

## 6. Not Useful / Caveats

- **Language detection is manual**: Skill asks user to confirm primary language but doesn't auto-detect. For German novel wiki, must explicitly declare `language: de` in EXTEND.md first time.
- **No built-in versioning**: Git handles history, but the skill doesn't tag "stable canon" vs. "research hypothesis" internally. Requires manual frontmatter discipline (e.g., adding `canon_status: canon | research` to every page).
- **BM25 only works locally**: No cloud sync. For a distributed novel team, would need Git + CI rebuild or API wrapper.
- **No graph visualization**: Concept table is tabular; no visual knowledge graph UI (though Obsidian graph view works). For large wikis (800+ pages), text navigation may bottleneck.
- **Contradiction resolution is manual**: Finds contradictions but agent can't auto-resolve; requires human judgment. Appropriate for fiction (contradictions often indicate creative tension).
- **No numeric/structured data**: Pages are Markdown only. For a physics-heavy novel tracking constants or timeline data, would need CSV/JSON export or templated tables.

## 7. Verdict

The Karpathy LLM Wiki pattern as implemented here is directly applicable to a German hard-scifi novel research system. Its strength is in **separating evidence (raw/), derived knowledge (wiki/), and operating rules (SCHEMA.md)** while keeping maintenance cost low through LLM ownership of the wiki layer. The concept-table formalism solves the "confidence tracking" problem: every piece of knowledge is tagged with sources and a maintenance note, enabling linting to catch stale canon. The contradiction block format is a lightweight way to surface conflicts without losing evidence. For Kohärenz Protokoll, porting the skill means: copy the workflow reference docs, configure EXTEND.md to require canon/research separation frontmatter fields, add a linting rule to prevent unlabeled canon drift, and adapt the concept-table rows to track storyform coherence and physics rule stability. The BM25 search is optional but valuable once research passes 500 documents. The main work is not the tool—it is the discipline of writing one source-summary page per ingest, maintaining the concept table, and filing query results back into the wiki when they are worth keeping.
