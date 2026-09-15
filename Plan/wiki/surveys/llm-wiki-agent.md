# LLM Wiki Agent — Repository Survey Report

## 1. What It Is

**LLM Wiki Agent** is a multi-agent coding skill that ingests raw research documents (PDF, DOCX, Markdown, audio, etc.) and synthesizes them into a persistent, interlinked knowledge wiki. The agent reads documents, extracts claims, creates cross-referenced entity and concept pages, flags contradictions, and maintains an append-only audit log. It works with Claude Code (via `CLAUDE.md`), Codex/OpenCode (via `AGENTS.md`), and Gemini CLI (via `GEMINI.md`). **Stack:** Python tools + Markdown pages + Claude API (litellm) + vis.js graph visualization + NetworkX community detection. **Maturity:** Production-ready; MIT licensed; no external database needed.

## 2. Architecture

### Directory Layout
- **`raw/`** — immutable source documents (user uploads; tools read-only)
- **`wiki/`** — the managed layer (agent-owned)
  - `index.md` — catalog of all pages, updated on every ingest
  - `log.md` — append-only chronological record: `## [YYYY-MM-DD] ingest | Title`
  - `overview.md` — living synthesis across all sources (regenerated on ingest if warranted)
  - `sources/` — one summary page per source document
  - `entities/` — auto-created pages for people, companies, projects
  - `concepts/` — auto-created pages for ideas, frameworks, theories
  - `syntheses/` — saved query answers filed back into the wiki
- **`graph/`** — derived output
  - `graph.json` — nodes (one per page) + edges (EXTRACTED from `[[wikilinks]]`, INFERRED via LLM)
  - `graph.html` — interactive vis.js visualization (standalone, no server)
- **`tools/`** — Python CLI scripts (independent of agent, run standalone with `ANTHROPIC_API_KEY`)
  - `ingest.py` — main pipeline (auto-convert non-MD, extract knowledge, validate)
  - `build_graph.py` — two-pass graph builder (deterministic EXTRACTED + semantic INFERRED)
  - `lint.py` — content quality checks (orphan pages, broken links, missing entities, contradictions, link density)
  - `heal.py` — auto-generate missing entity pages from references
  - `_utils.py` — shared utilities (wikilink extraction, LLM calls, file I/O)

### Data Model: Page Frontmatter Schema
Every wiki page uses YAML frontmatter followed by markdown body:

```yaml
---
title: "Page Title"
type: source | entity | concept | synthesis
tags: [optional, tags]
sources: [source-slug-1, source-slug-2]       # for entity/concept pages only
last_updated: YYYY-MM-DD
---
## Body section
```

**Page types:**
- `source`: One per ingested document (slug from filename, kebab-case)
- `entity`: Auto-created for people/companies/projects mentioned in 3+ pages
- `concept`: Auto-created for ideas/frameworks mentioned in 3+ pages
- `synthesis`: Query answers filed back into the wiki

### Ingest Flow (10 steps, defined in `CLAUDE.md` §Ingest Workflow)
1. Read source document (auto-convert if non-markdown via markitdown)
2. Read `wiki/index.md` and `wiki/overview.md` for context
3. Invoke Claude with schema constraints (return JSON only; no markdown fences)
4. Claude returns structured JSON with: title, slug, `source_page` (markdown), `index_entry`, `overview_update` (or null), `entity_pages` list, `concept_pages` list, `contradictions` list, `log_entry`
5. Write `wiki/sources/<slug>.md`
6. Write/update `wiki/entities/*.md` (from `entity_pages` array)
7. Write/update `wiki/concepts/*.md` (from `concept_pages` array)
8. Append to `wiki/log.md`
9. Update `wiki/index.md` with new entry
10. Update `wiki/overview.md` if provided
11. **Post-ingest validation:** check for broken `[[wikilinks]]`, verify all new pages in index (report warnings)

### LLM vs. Deterministic Code
- **LLM-driven:** ingest (schema extraction), query (synthesis), contradiction detection, graph inference
- **Deterministic:** health checks (empty files, index sync, log coverage), broken-link detection, orphan detection, link-density analysis, graph building Pass 1 (wikilink extraction)

## 3. Concepts Worth Stealing

### 1. **Frontmatter Type Enum + Page Template Inheritance**
**What:** Pages are typed (`source|entity|concept|synthesis`). Each type has a schema-defined template structure.
**Why for novel-canon:** Canon pages could be typed (`canon-event`, `canon-character`, `canon-location`, `canon-rule`). Research pages typed (`research-paper`, `research-note`, `hypothesis`). The type determines validation rules (e.g., canon-event must cite a storyform date; research-note must cite its source). **File:** `CLAUDE.md` §Page Format; templates in `tools/ingest.py` lines 205–238.

### 2. **Append-Only Log with Grep-Parseable Format**
**What:** `wiki/log.md` uses format `## [YYYY-MM-DD] <operation> | <title>` so `grep "^## \[" wiki/log.md` gives chronological view of all ingests/queries/lints/graphs.
**Why for novel-canon:** A provenance trail showing when each canon claim was verified, which agent verified it, whether it was contradicted later. Query: `grep "\[canon\]" wiki/log.md` to see all canon-touch history. **File:** `CLAUDE.md` §Log Format; used in `tools/ingest.py` line 270.

### 3. **Source Immutability Layer (raw/ is read-only)**
**What:** `raw/` contains untouched originals. Ingest converts them to markdown, then to wiki pages. Never edit raw directly; conversion is one-way.
**Why for novel-canon:** Separates user-uploaded research (Google Drive exports, PDFs) from the curated canon wiki. Prevents accidental mutation of source truth. Audit trail shows what was in raw/ at ingest time (via SHA256 hash in log). **File:** `tools/ingest.py` lines 199–202 (hash + log); `CLAUDE.md` directives.

### 4. **Health vs. Lint Distinction (free vs. expensive checks)**
**What:** 
  - `health` (fast, zero LLM calls): empty files, index sync, log coverage
  - `lint` (expensive, LLM-based): orphans, contradictions, semantic gaps, stale summaries
**Why for novel-canon:** Canon verification is expensive (deep narrative checks). Research contradiction detection is cheaper (factual claims). Run health daily (pre-flight), lint periodically (e.g., before publishing). **Files:** `CLAUDE.md` §Health Workflow table; `tools/heal.py` (stub generator); boundary docs at `CLAUDE.md` lines 199–211.

### 5. **Domain-Specific Page Templates**
**What:** Beyond default source template, the schema defines:
  - **Diary template:** Event Summary, Key Decisions, Energy & Mood, Connections, Shifts & Contradictions
  - **Meeting notes template:** Goal, Key Discussions, Decisions Made, Action Items
**Why for novel-canon:** Different source types need different structure. Canon storyform → Storyform template (Dramatica quads, throughlines, acts). Character codex → Character template (aliases, roles, arc). Physics rules → Physics axiom template (law, exceptions, in-world justification). **File:** `CLAUDE.md` §Domain-Specific Templates.

### 6. **Wikilink Trigger Matching for Deduplication**
**What:** When ingest writes entity/concept pages, it aggressively converts known terms inline to `[[WikiLinks]]`. The prompt says: "CRITICAL: Aggressively convert key people, products, concepts and projects into [[Wikilinks]] inline in the text. Omitting [[ ]] for known terms is a failure."
**Why for novel-canon:** Canon terms (character names, locations, concepts) should link to their canon definitions. Prevents hallucinated synonyms. Query: `grep -r "JunaXX"` finds all references; `[[JunaXX]]` ensures they route to the canon page, not a new orphan. **File:** `tools/ingest.py` lines 226–227 (prompt instruction).

### 7. **Two-Pass Graph Building (Deterministic + Semantic)**
**What:**
  - **Pass 1 (EXTRACTED):** Parse all `[[wikilinks]]` deterministically → edges with `confidence: 1.0`
  - **Pass 2 (INFERRED):** Claude infers implicit relationships not captured by wikilinks → edges tagged `INFERRED` (high confidence) or `AMBIGUOUS` (low confidence)
**Why for novel-canon:** Canon links are explicit (entered by author). Research links may be implicit ("this paper discusses concepts from that paper"). Separate treatment prevents false connections in canon while enriching research graph. **File:** `tools/build_graph.py` lines 116–139 (Pass 1), lines 142+ (Pass 2 checkpoint); edge color codes in lines 60–64.

### 8. **Multi-Format Ingest via markitdown Auto-Conversion**
**What:** Supported formats include PDF, DOCX, PPTX, XLSX, HTML, TXT, CSV, JSON, XML, RST, RTFM EPUB, IPYNB, YAML, WAV, MP3. Non-markdown is auto-converted via markitdown; markdown ingested directly. Optional `--no-convert` flag skips conversion.
**Why for novel-canon:** Researchers upload PDFs, meeting transcripts, Notion exports. Single ingest command handles all. Optional `tools/pdf2md.py` for arXiv papers (higher fidelity). **File:** `tools/ingest.py` lines 45–51 (CONVERTIBLE_EXTENSIONS), lines 144–175 (convert_to_md), lines 186–196 (auto-convert logic).

### 9. **Post-Ingest Validation Pipeline**
**What:** After writing pages, validate:
  - **Broken wikilinks:** `[[WikiLink]]` → no matching page (reported as warnings)
  - **Unindexed pages:** created pages not registered in `index.md` (reported as warnings)
  - **Summary printed:** created N pages, updated M pages, W contradictions, B broken links
**Why for novel-canon:** Catch LLM hallucinations (invented character names, phantom locations). Ensures every new page is findable. **File:** `tools/ingest.py` lines 101–142 (validate_ingest function), lines 289–316 (summary printing).

### 10. **Contradiction Detection at Ingest Time**
**What:** Prompt asks Claude to flag contradictions with existing wiki content. Results printed and optionally appended to page metadata.
**Why for novel-canon:** Early warning when research contradicts established canon. Example: "This paper claims mutation X is impossible, but Canon-Rule-7 states it is mandatory." Can be recorded as `contradictions:` field in frontmatter for later review. **File:** `tools/ingest.py` lines 235–237 (contradictions field in JSON schema), lines 273–277 (print contradictions).

### 11. **Orphan & Missing Entity Detection**
**What:** 
  - Orphans: pages with zero inbound `[[wikilinks]]` (except overview.md)
  - Missing entities: entity names mentioned in 3+ pages but no dedicated page yet
**Why for novel-canon:** Canon locations/characters mentioned in 3 plot outlines but never defined → create canon definition page. Research papers citing same author across multiple sources → auto-create author entity. **File:** `tools/lint.py` lines 47–55 (find_orphans), lines 68–78 (find_missing_entities).

### 12. **Link Density Budgeting**
**What:** Pages with fewer than N outbound `[[wikilinks]]` (default N=2) are flagged as sparse/fragmented.
**Why for novel-canon:** A canon-character page with zero links to scenes/locations/relationships is incomplete. A plot-outline with one link is isolated. Helps identify missing story connections. **File:** `tools/lint.py` lines 81–102 (check_link_density).

### 13. **Schema File as Single Source of Truth**
**What:** `CLAUDE.md` (or `AGENTS.md` for Codex) defines page format, ingest workflow, query workflow, lint checks, graph building, naming conventions. Agent reads this file on every session start.
**Why for novel-canon:** Allows drift-free agent behavior. Change the schema once, all future agent runs follow it. Prevents inconsistent page structures. **File:** `CLAUDE.md` (all sections); system-reminder integration via `.claude/settings.json` hooks (not visible in this repo, but referenced).

## 4. Reusable Code / Assets

### Python Tools (no API key needed for structure/validation, but ingest/lint use Claude API)

| File | Purpose | Reusability | Dependencies |
|---|---|---|---|
| `tools/_utils.py` | Shared: `extract_wikilinks()`, `all_wiki_pages()`, `read_file()`, `write_file()`, `sha256()`, `append_log()`, `call_llm()` | **High** — vendor this as-is | pathlib, litellm (optional for call_llm) |
| `tools/ingest.py` | Main ingest pipeline: markdown conversion, JSON schema extraction, page writing, validation | **High** — port the validation loop and JSON prompt structure | markitdown (optional), litellm |
| `tools/build_graph.py` | Two-pass graph builder, Louvain communities, vis.js template generation | **Medium** — useful for research graph, less so for canon (which may not need inference) | networkx, litellm |
| `tools/lint.py` | Orphan/broken-link/missing-entity detection, link-density checks, hub-stub detection | **High** — deterministic checks directly applicable | litellm (for semantic lint only) |
| `tools/heal.py` | Auto-generate missing entity pages from references | **Medium** — port for research codex generation | litellm |

### Schema Files

| File | Purpose | Reusability |
|---|---|---|
| `CLAUDE.md` | Full schema: page format, frontmatter, ingest/query/lint/graph workflows, naming conventions | **Very High** — adapt for novel by changing section 2 (Page Format) and section 5 (Domain-Specific Templates) |
| `AGENTS.md` | Codex-specific variant of CLAUDE.md | **Medium** — reference for multi-agent portability |
| `.claude/commands/*.md` | Slash command definitions (wiki-ingest, wiki-query, wiki-lint, wiki-graph) | **High** — copy structure, adapt paths for novel-wiki |

### CLI Slash Commands (Claude Code-specific)

`.claude/commands/wiki-ingest.md`, `wiki-query.md`, `wiki-lint.md`, `wiki-graph.md` — Simple markdown definitions that tell Claude Code to follow the CLAUDE.md workflows. **Reuse pattern:** Rename to `/canon-ingest`, `/canon-lint`, `/research-query`, etc.

## 5. Not Useful / Caveats

### 1. **No Deterministic Contradiction Checking**
LLM-driven contradiction detection is probabilistic. For canon, we need hard rules: "Canon-Event-X must cite a valid storyform marker" or "Character aliases must match regex /Juna[A-Z]/" — the code provides no rule engine.

### 2. **No Provenance Tracking (Agent/Session Identity)**
The log records `[YYYY-MM-DD] ingest | Title` but not which agent (Claude Code vs. Codex), which human user, or which session ran it. For novel canon, we need "Verified by @claude-haiku on 2026-06-15 session_xyz during /gate pre_draft".

### 3. **No Canon/Research Separation Layer**
The ingest pipeline treats all sources uniformly. For a novel, we need: canon pages locked (read-only after verification), research pages open for update, cross-contamination guards. This repo has no such guards — an agent could accidentally rewrite a canon page.

### 4. **Graph Inference Cost**
Pass 2 (semantic inference) invokes Claude for every page pair to detect implicit relationships. For 600 research documents, this is expensive and latency-heavy. May not be worth the cost for a novel-knowledge system where explicit `[[links]]` suffice.

### 5. **No Version Control Integration**
Relies entirely on git commits external to the agent. No built-in diff/rollback/branching in the tool layer. For a novel with multiple editors, concurrent canon changes, and versioning needs, git alone may not suffice.

### 6. **Multi-Format Ingest Complexity**
Full support for PDF/DOCX/PPTX/XLSX/YAML/WAV adds dependencies (markitdown, arxiv2md, marker, etc.). For a novel wiki, Markdown + optional PDF conversion may suffice.

### 7. **Contradiction Detection Limits**
The prompt asks Claude to flag contradictions, but provides only recent wiki pages as context (lines 72–74 of `ingest.py`). In a large wiki with 600+ documents, missing context could yield false negatives.

## 6. Verdict

**Role in Novel-Canon System:** This repo is an **excellent reference architecture** for the page-templating, ingest-pipeline, validation-chain, and graph-analysis layers. Directly applicable concepts:

1. **Port** `tools/_utils.py` and the validation loop from `tools/ingest.py` (handle JSON parsing, page writing, broken-link detection, index coverage).
2. **Adapt** the `CLAUDE.md` schema: define `type: canon-event|canon-character|canon-location|research-paper|research-note` instead of `source|entity|concept|synthesis`.
3. **Implement** domain-specific templates for canon (Storyform, Character, Location, Physics-Axiom, Plot-Beat) using the diary/meeting-notes pattern as reference.
4. **Adopt** the append-only log format with enhanced provenance: `## [YYYY-MM-DD] ingest | <title> | agent=claude-haiku | session=session_xyz | verified=true/false`.
5. **Build custom** contradiction checking (deterministic rule engine, not LLM) and canon-lock semantics (pages signed after verification, read-only thereafter).

**Do not use** the graph inference pass (too expensive for a novel), full multi-format support (Markdown + selective PDF suffice), or the generic query→synthesis pattern (novel needs canon-aware synthesis with citation grounding).

This repo saves 4–6 weeks of ingest-pipeline engineering. Use it as a scaffold; build the canon-verification and provenance layers on top.

