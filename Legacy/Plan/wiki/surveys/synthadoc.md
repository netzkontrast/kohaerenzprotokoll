# Synthadoc Repository Survey

## 1. What It Is

**Synthadoc** (v1.3.3) is a production-grade, domain-agnostic LLM wiki engine that compiles knowledge at **ingest time** rather than query time. Written in Python 3.11+ with a TypeScript Obsidian plugin, it reads raw source documents (PDF, DOCX, PPTX, XLSX, MD, images, URLs, YouTube transcripts) and uses an LLM to synthesize them into a persistent, structured Markdown wiki. The system maintains a 5-state page lifecycle (draft → active → contradicted/stale → archived), auto-detects contradictions, builds weighted wikilink graphs with Louvain clustering, flags orphan pages, provides claim-level provenance with `^[file:L-L]` citations, and runs adversarial LLM review passes to catch overstated claims. It's engineered for solo users through enterprises, with local-first storage (no cloud), audit trails for every action, and cost guards. The core is AGPL-3.0; skills and providers use Apache-2.0 for third-party extensions.

## 2. Architecture

### Package Layout
- **`synthadoc/agents/`** — LLM orchestration: `ingest_agent.py`, `lint_agent.py`, `query_agent.py`, `search_decompose_agent.py`, plus agentic workflows (`workflows/*.py`) for contradiction resolution, orphan fixing, broken wikilink repair.
- **`synthadoc/storage/`** — Data persistence abstractions: `wiki.py` (WikiStorage + WikiPage + LifecycleState constants), `log.py` (AuditDB + LogWriter for immutable event log), `search.py` (BM25 + optional semantic search indexing).
- **`synthadoc/skills/`** — Format handlers (pdf, docx, pptx, xlsx, markdown, image, url, youtube, web_search, session). Each skill is a `BaseSkill` subclass at `skills/<format>/scripts/main.py`.
- **`synthadoc/providers/`** — LLM backend abstraction (Gemini, Groq, Anthropic, OpenAI, Ollama, Qwen, DeepSeek, MiniMax, Claude Code, Opencode).
- **`synthadoc/cli/`** — CLI commands grouped by domain (ingest, query, lint, lifecycle, jobs, candidates, context, retract).
- **`synthadoc/integration/`** — MCP server (FastMCP), HTTP API endpoints, job orchestration (Orchestrator singleton pattern).
- **`synthadoc/core/`** — Cache manager (3-layer caching: embedding, LLM response, provider prompt), config loader, sanitizer (strips zero-width chars, bidi overrides, instruction-override phrases).
- **`hooks/`** — Event-driven shell scripts fired on `on_ingest_complete` and `on_lint_complete`, receiving JSON context on stdin.
- **`obsidian-plugin/`** — TypeScript Obsidian plugin with ingest modal, streaming query UI, lint report, lifecycle controls, vault auto-snapshot (2 s debounce, dedup), knowledge graph Canvas panel.
- **`tests/`** — pytest suite with live/mock patterns, skill isolation tests, agent workflow tests, integration tests.

### Data Model (Page Schema & Lifecycle)

**WikiPage** (`synthadoc/storage/wiki.py` lines 99–116):
- `title`, `tags`, `content` (Markdown body)
- `status` (enum: draft | active | contradicted | stale | archived, from `LifecycleState` class, lines 28–36)
- `confidence` (string: low|medium|high)
- `sources` (list of `SourceRef`: file, hash, size, ingested timestamp, truncated flag)
- `created`, `updated` (ISO dates; updated only on re-ingest)
- `orphan` (bool; set by lint pass)
- `categories`, `aliases` (list; for Obsidian Properties)
- `contradiction_note`, `unresolved_note` (strings; capture auto-resolve reason)
- `lint_warnings` (list of dicts; adversarial review findings)
- `type` (OKF knowledge type: concept|person|technology|event|organization|location|product)
- `resource` (OKF primary source URL; for URL sources only)

**Frontmatter Format** (YAML, lines 16–18 & write_page() lines 173–196):
```yaml
---
title: "Page Title"
tags: [tag1, tag2]
status: active
confidence: high
created: 2026-05-20
updated: 2026-06-10
sources:
  - file: "raw_sources/report.pdf"
    hash: "abc123def456..."
    size: 45123
    ingested: "2026-05-20T14:30:00Z"
    truncated: false
orphan: false
categories: [Recently Added]
aliases: []
contradiction_note: null
lint_warnings: []
type: concept
resource: null
---
```

### Page Lifecycle State Machine & Transitions

**5 States** (LifecycleState, lines 29–36):
- `draft` — newly ingested, not yet reviewed
- `active` — human-reviewed, authoritative; protected from overwrite by sources
- `contradicted` — lint flagged source conflict or adversarial review demoted it
- `stale` — source file modified (hash mismatch detected) or no update within retention window
- `archived` — retired; cascade cleanup removes all `[[slug]]` references from live pages

**Allowed Transitions** (lines 41–54): User-driven transitions are validated; lint and ingest write status directly. Cascade cleanup fires on archive (line 864–866 in README). System pages (`index`, `log`, `dashboard`, `purpose`, `overview` in SYSTEM_PAGE_SLUGS line 23) are never promoted/demoted by lifecycle logic.

### Ingest Pipeline & Workflow

**`IngestAgent.run()`** (`synthadoc/agents/ingest_agent.py`):
1. **Skill dispatch** — file extension or intent → skill (`PdfSkill`, `DocxSkill`, `UrlSkill`, etc.)
2. **Extraction & analysis** — skill extracts text; LLM analyzes with `_ANALYSIS_PROMPT` (line 48–56): entities, tags, summary, OKF type
3. **Deduplication** — 3-layer cache check: embedding, LLM response, provider prompt. Skipped on `--force`
4. **Decision logic** (`_DECISION_PROMPT`, lines 65–102):
   - **RULE 1 (FLAG)** — source disputes existing page → action='flag' (contradicted state)
   - **RULE 1b (ACTIVE PROTECTION)** — active pages are authoritative; conflicting info → flag, not update
   - **RULE 2 (UPDATE)** — source adds new section to existing page, no dispute → action='update'
   - **RULE 2b (ENTITY PROFILE)** — comprehensive profile of one entity → action='create' (even if thematic page exists)
   - **RULE 3 (CREATE)** — novel subject → action='create' with new slug
5. **Citation normalization** (`_normalize_citation_markers()`, lines 135–151) — LLM emits `^[file:42]` or `^[file:12,16-21]`; normalize to canonical `^[file:N-N]`
6. **Wikilink injection** — cross-reference related pages via `[[slug]]` in generated content
7. **Write** — page written to disk with YAML frontmatter; status defaults to draft; sources list includes hash for stale detection
8. **Callback** — if configured, `on_ingest_complete` hook fires with JSON context (page slugs, tokens, cost)

**Result struct** (`IngestResult` lines 32–45): pages_created, pages_updated, pages_flagged, tokens_used, cost_usd, cache_hits, skipped flag and reason.

### Lint Agent & Contradiction Detection

**`LintAgent.run()`** (`synthadoc/agents/lint_agent.py`):
1. **Structural checks** (deterministic, no LLM):
   - Orphan detection: pages with no inbound `[[wikilinks]]` from content pages (excludes system pages, lines 61–66)
   - Dangling links: `[[slug]]` referencing non-existent pages; auto-remove with confirmation
   - Citation verification: `^[file:L-L]` markers validate against source files in `extracted/` directory (lines 110–167); reasons: malformed, broken_ref, out_of_range
   - Stale detection: source file hash mismatch (lines 52–67 test_lint_lifecycle.py shows hash-based stale transition)
   - Truncation flag: sources exceeding max_source_chars get `truncated: true`

2. **Adversarial review** (optional LLM pass; configurable gate):
   - Second-LLM pass flags overstated claims, unsupported superlatives, contestable facts
   - Demotes pages to contradicted if warning count exceeds threshold

3. **Lifecycle transitions** (auto):
   - Draft → Active (on clean pass, no contradictions)
   - Active → Stale (on hash mismatch)
   - Contradicted/Stale → Draft (if source re-ingested with new content)
   - Archived pages removed from searches; cascade cleanup of all `[[slug]]` references (line 865–867 README)

4. **Report** (`LintReport` dataclass, lines 35–50): contradictions_found/resolved/unresolved, orphan_slugs, dangling_links_removed, tokens_used, adversarial_warnings, citation_issues, lifecycle_promoted/stale/archived, warnings

**Graph Building** (lint_agent.py uses networkx + python-louvain for community detection, stored in audit DB, visualized in web UI with D3)

### Storage Abstraction

**WikiStorage** (`synthadoc/storage/wiki.py` lines 143–299):
- `write_page(slug, WikiPage|content, frontmatter)` — atomic write with YAML frontmatter + body
- `read_page(slug)` → WikiPage object (YAML parse + body extraction, lines 207–250)
- `page_exists(slug)`, `list_pages()`, `all_slugs()` (skip candidates subdir)
- Thread-safe: per-slug locks (`self._locks` dict, line 147) to prevent concurrent writes
- Append-to-index: auto-add new page to index.md under "Recently Added" section if it exists

**AuditDB** (`synthadoc/storage/log.py` lines 91+):
- SQLite database at `.synthadoc/audit.db`
- Immutable event log: ingest, lint, query, lifecycle transitions, snapshots
- Tracks page state snapshots at each lifecycle change (content deduped — unchanged saves cost nothing, line 268 README)
- `record_ingest(source_hash, tokens, file, page_slug, ...)` — logs ingest with source hash for stale detection
- `get_lifecycle_events(slug, limit, offset)` → returns ordered event history
- `snapshot_if_changed(slug, body)` — conditional snapshot (skips if body unchanged from last snapshot)

### LLM Integration Points

**Where LLM is called** (vs. deterministic code):
- **Ingest decision** — `_DECISION_PROMPT` (decide action: create/update/flag)
- **Analysis** — `_ANALYSIS_PROMPT` (extract entities, tags, type)
- **Citation pass** — post-generation normalization and claim extraction
- **Adversarial review** (lint) — flag overstated claims
- **Query** — search decomposition + BM25 ranking + semantic re-ranking (optional) + LLM synthesis
- **Contradiction resolution** (agentic workflow) — propose rewrite with diff
- **Orphan resolution** (agentic workflow) — suggest wikilinks for orphaned pages

**Where code is deterministic**:
- Orphan detection (regex wikilink extraction)
- Citation validation (line range checks)
- Stale detection (file hash comparison)
- Dangling link repair (regex substitution)
- Lifecycle transitions (state machine rules)
- Snapshot dedup (content hash comparison)

### Hooks System

**Event-driven** (`hooks/README.md`):
- `on_ingest_complete` — fires after source successfully ingested
- `on_lint_complete` — fires after lint pass finishes
- Hook is a shell command (e.g., `python git-auto-commit.py`)
- Receives JSON context on stdin
- Exit 0 on success, non-zero on failure
- Can be blocking or background (config.toml: `blocking = true|false`)
- Example hook: `git-auto-commit.py` (auto-commits wiki changes after every ingest)

### Claude Code Skills & Integration

**Skills system** (`synthadoc/skills/base.py` is Apache-2.0; implementations in `skills/<format>/SKILL.md` + `scripts/main.py`):
- Each skill is a `BaseSkill` subclass with `async def extract(source_path) → SkillResult`
- Metadata: entry script, triggers (file extensions, intents), dependencies
- Skill registry auto-discovers and chains skills by extension/intent
- Example: `pdf/SKILL.md` (lines 1–20) uses pypdf with pdfminer.six fallback for CJK fonts

**skills-lock.json** — locks specific skill versions by GitHub source + computed hash. Versioning ensures reproducibility across machines.

**CLAUDE.md / AGENTS.md / GEMINI.md** — auto-generated per wiki by `scaffold` command. Includes:
- Domain guidelines
- CLI quick reference (ingest, query, lint, lifecycle, export commands)
- Ingest syntax examples
- Query rules (use wiki only, no hallucination)
- Lint/staging/routing workflow
- MCP tool table

## 3. Concepts Worth Stealing

### 1. **5-State Page Lifecycle with Immutable Event Log**
**What it does**: Pages progress through `draft → active → contradicted|stale → archived` with full audit trail of who changed it, when, why, and with what content snapshot.

**Why useful for novel wiki**: Separates canon (active, human-approved) from research (draft, under review). Stale detection catches when source files change. Snapshots enable rollback. Archive with cascade cleanup prevents orphaned wikilinks when research is retracted.

**Files**: `synthadoc/storage/wiki.py` (LifecycleState enum, allowed transitions matrix), `synthadoc/storage/log.py` (AuditDB snapshot logic), `synthadoc/cli/lifecycle.py` (activate, archive, restore, history, rollback commands), `tests/test_lint_lifecycle.py` (transition tests, snapshot dedup).

### 2. **Active Page Protection Rule**
**What it does**: Pages marked `status: active` (human-reviewed) are protected from overwrites by incoming sources. Conflicting claims in new sources trigger `contradicted` flag instead of silent update.

**Why useful**: Prevents research sources from silently overwriting canon. Contradiction detection forces human review rather than data loss.

**Files**: `synthadoc/agents/ingest_agent.py` lines 79–82 (RULE 1b in _DECISION_PROMPT), lines 234–241 (ingest logic that respects active page status).

### 3. **Contradiction Detection via Ingest-Time Decision Logic**
**What it does**: LLM prompt with explicit decision rules (RULE 1–3 in _DECISION_PROMPT, lines 65–102) classifies whether a source should create, update, or flag an existing page. Contradictions are tagged with explanation.

**Why useful**: Surfaces conflicting sources at ingest time (not query time) so contradictions are visible and resolvable. Pairs with adversarial review gate for human sign-off before reaching canon.

**Files**: `synthadoc/agents/ingest_agent.py` (IngestAgent.run(), _DECISION_PROMPT), `synthadoc/agents/lint_agent.py` (adversarial review gate, contradiction auto-resolve logic).

### 4. **Weighted Wikilink Graph with Louvain Clustering**
**What it does**: `[[slug]]` wikilinks extracted from page bodies; co-source edges connect pages ingested from same document; edge weights reflect link frequency + co-source signals. Louvain clustering groups related pages into communities (visualized in web UI graph tab).

**Why useful**: Automatic knowledge graph without manual annotation. Community detection surfaces topic clusters. Co-source edges reveal which research documents connect disparate canon pages.

**Files**: `synthadoc/agents/lint_agent.py` (wikilink extraction, graph building with networkx), `tests/agents/test_lint_report_feature.py` (graph structure tests).

### 5. **Claim-Level Provenance via Line-Scoped Citations**
**What it does**: Every claim in generated pages receives `^[file:L-L]` citation marker. Lines are extracted to `.synthadoc/extracted/<source-slug>.txt` on ingest. Lint validates each citation against actual source line count.

**Why useful**: Enables "show me where that came from" button (Obsidian Source Viewer). Lint catches broken citations if source truncated or format changed. No hallucinated citations.

**Files**: `synthadoc/agents/ingest_agent.py` lines 135–151 (citation normalization), lines 110–167 (citation extraction post-LLM), `synthadoc/agents/lint_agent.py` (_check_page_citations function, citation validation), `synthadoc/storage/log.py` (citation excerpt storage).

### 6. **3-Layer Caching Strategy (Embedding, LLM, Provider Prompt)**
**What it does**: Cache keys derived from source hash + document hash. Repeat ingest of unchanged source returns cached result before calling LLM. Provider prompt cache reuses tokenization across identical queries.

**Why useful**: Repeat ingest is near-zero-cost (seconds instead of minutes + API calls). Prevents wasted tokens on unchanged research docs. Essential for 680+ documents.

**Files**: `synthadoc/core/cache.py` (CACHE_VERSION, make_cache_key logic), `synthadoc/agents/ingest_agent.py` (cache bypass on --force).

### 7. **Staged Candidates Before Wiki Promotion**
**What it does**: New pages land in `wiki/candidates/` as draft. Review via CLI or Obsidian plugin; promote (`candidates promote --all`) or discard (`candidates discard <slug>`) before entering live wiki.

**Why useful**: Prevents low-confidence ingest from polluting canon. Human review gate before integration. For novel wiki: filter research ingests so only approved docs → canon.

**Files**: `synthadoc/cli/candidates.py` (list, promote, discard commands), `synthadoc/templates/README.md` (candidates workflow walkthrough).

### 8. **Per-Source Truncation Flag & Max Char Limit**
**What it does**: Each ingest can set `--max-source-chars` (e.g., 64000). Sources exceeding limit are capped; `truncated: true` flag in frontmatter + lint warning.

**Why useful**: Prevents runaway token spend on huge PDFs. Signals truncated claims to users. Can override per-ingest to handle large files selectively.

**Files**: `synthadoc/storage/wiki.py` SourceRef.truncated (line 96), `synthadoc/agents/ingest_agent.py` (truncation logic), README line 64–65 (CLI example).

### 9. **Adversarial Review Gate with Threshold-Based Auto-Demotion**
**What it does**: Optional second-LLM pass flags overstated claims, unsupported superlatives. If warning count exceeds configurable threshold, page auto-demotes from active → contradicted for human review.

**Why useful**: Catches confident-but-wrong synthesis LLM produces. For canon: ensures only well-supported claims get published.

**Files**: `synthadoc/agents/lint_agent.py` (adversarial_review logic, threshold config), README line 177 (feature description).

### 10. **Agentic Workflows (Tool-Call Loops with Approval Gates)**
**What it does**: Seven conversational workflows (contradiction resolver, orphan resolver, broken wikilinks fixer, ingest-lint loop, etc.) run as agent tool-call chains. Each destructive action shows a diff and waits for human approval before write.

**Why useful**: Automates tedious manual fixes (e.g., resolving contradictions across 50 pages) but preserves human control. Streams progress inline. Rollback is always undoable.

**Files**: `synthadoc/agents/workflows/` (contradiction_resolver.py, orphan_resolver.py, broken_wikilinks.py, _base.py workflow scaffold), `synthadoc/cli/workflow.py` (CLI entry), README lines 777–821 (workflow command reference).

### 11. **Source Hash for Stale Detection**
**What it does**: On ingest, source file hash stored in SourceRef. On next lint pass, if source file hash differs, page auto-transitions to stale.

**Why useful**: Detects when research sources are updated. For novel wiki: flags research pages for review when underlying source changes.

**Files**: `synthadoc/storage/wiki.py` SourceRef (lines 91–96), `synthadoc/storage/log.py` record_ingest (stores hash), `synthadoc/agents/lint_agent.py` stale detection logic.

### 12. **Obsidian Plugin with Auto-Snapshot on Vault Save**
**What it does**: TypeScript plugin detects file saves (2 s debounce, dedup). Snapshots page body in AuditDB with reason "manual_edit". Provides ingest modal, streaming query UI, lint report, graph Canvas panel, vault background monitoring.

**Why useful**: Seamless integration with editing workflow. Snapshots enable rollback if manual edit gone wrong. Graph panel provides immediate visual overview of knowledge structure.

**Files**: `obsidian-plugin/src/` (TypeScript source), `obsidian-plugin/manifest.json` (plugin metadata), `synthadoc/data/obsidian-plugin/` (bundled plugin binary), plugin auto-installs on `synthadoc install`.

### 13. **MCP Server (12 Tools) for Claude Code / LangGraph Integration**
**What it does**: FastMCP server at localhost:7070/mcp/sse (stdio for Claude Desktop). Exposes synthadoc_ingest, synthadoc_query, synthadoc_lint, synthadoc_export, synthadoc_context, etc. No double-LLM cost for reads (queries go straight to BM25 + wiki, no re-synthesis).

**Why useful**: Claude Code can ingest research docs, query canon, run lint — all without leaving the agent. Enables tight integration with agency engine (e.g., novel.py calling synthadoc verbs).

**Files**: `synthadoc/integration/mcp_server.py` (FastMCP server, 12 tools), `docs/design.md` (MCP schema reference).

### 14. **Query Decomposition + Knowledge Gap Detection**
**What it does**: Query split into parallel sub-questions via BM25 + semantic re-ranking (optional). If few results, knowledge gap callout surfaces with suggested web searches.

**Why useful**: Compound questions don't disappear into silence. Users see when wiki lacks coverage. For novel wiki: identifies research gaps.

**Files**: `synthadoc/agents/search_decompose_agent.py` (decomposition logic), `synthadoc/agents/query_agent.py` (gap detection), README line 199 (knowledge gap detection).

### 15. **Scaffolding: Auto-Regenerate Index, Agent Files, Purpose**
**What it does**: `synthadoc scaffold` command regenerates index.md (with categories from page slugs), AGENTS.md (domain guidelines + CLI quick ref), purpose.md (synthesis of all page titles). Preserves user content above `<!-- synthadoc:scaffold -->` marker.

**Why useful**: Wiki structure stays in sync as pages grow. Agent guidelines stay current. No manual index maintenance.

**Files**: `synthadoc/cli/scaffold.py`, `synthadoc/templates/README.md` (scaffold zone rules), README line 637 (command).

## 4. Reusable Code & Assets

| Component | Path | One-Line Note | Dependencies |
|-----------|------|---------------|--------------|
| WikiPage dataclass + LifecycleState machine | `synthadoc/storage/wiki.py` lines 28–116 | Full page schema, state enums, transition rules | PyYAML, filelock |
| AuditDB SQLite schema + lifecycle event log | `synthadoc/storage/log.py` | Immutable event recording, snapshots, rollback support | aiosqlite |
| BaseSkill abstract class | `synthadoc/skills/base.py` | Pluggable format handlers (Apache-2.0 licensed for extensions) | async/await, dataclass |
| IngestAgent decision logic | `synthadoc/agents/ingest_agent.py` lines 48–102 | 3-rule decision prompt (create/update/flag), citation normalization | LLM provider |
| LintAgent orphan + citation checks | `synthadoc/agents/lint_agent.py` lines 61–167 | Structural lint (no LLM), graph building, contradiction flagging | networkx, python-louvain |
| WikiStorage read/write abstractions | `synthadoc/storage/wiki.py` lines 143–299 | Thread-safe file I/O, YAML frontmatter handling, atomic writes | PyYAML, filelock |
| 3-layer cache manager | `synthadoc/core/cache.py` | Embedding cache, LLM response cache, provider prompt cache | hashlib, provider SDKs |
| Context budget allocation | `synthadoc/agents/context_agent.py` | Proportional context splitting (60% wiki / 20% history / 15% system / 5% index) | token counting |
| Agentic workflow scaffolds | `synthadoc/agents/workflows/_base.py` | Reusable tool-call loop + approval gate pattern | LLM, tool invocation |
| Obsidian plugin UI components | `obsidian-plugin/src/` | Ingest modal, streaming query, graph Canvas, snapshot manager | Obsidian API, TypeScript |
| Domain templates (30 pre-built) | `synthadoc/templates/` | Seeded CLAUDE.md, routing, purpose, agent files per domain | YAML, Markdown |
| Contradiction resolver workflow | `synthadoc/agents/workflows/contradiction_resolver.py` | Interactive diff + approval loop for resolving contradicted pages | LLM, diff library |
| MCP server wrapper | `synthadoc/integration/mcp_server.py` lines 1–100 | 12-tool FastMCP server, no double-LLM cost reads | FastMCP |
| Skill registry + auto-discovery | `synthadoc/skills/registry.py` | Dynamic format → skill mapping, skill versioning via skills-lock.json | Python importlib, JSON |
| Hook system (on_ingest_complete / on_lint_complete) | `synthadoc/integration/hooks.py` + `hooks/README.md` | JSON context to stdin, blocking/background flag, example git-auto-commit | subprocess, JSON |
| Sensitive data retraction scanner | `synthadoc/cli/retract.py` | Pattern matching for API keys, emails, SSNs, credit cards; incremental scan | regex, cryptographic hashing |
| Semantic re-ranking (optional) | `synthadoc/agents/query_agent.py` | Vector re-ranking fallback (BAAI/bge-small-en-v1.5) when BM25 insufficient | sentence-transformers |

## 5. Not Useful / Caveats

- **License**: AGPL-3.0-or-later core (contributions require CLA). For novel wiki engine, vendor the Apache-2.0 base classes (BaseSkill, LLMProvider) but respect copyleft for core logic if derived.
- **Multi-LLM provider coupling**: Synthadoc abstracts multiple LLM providers (Gemini, Anthropic, OpenAI, etc.) into a single provider interface. For DSPy-based novel wiki, you'll need to decouple and route through DSPy's own LM() abstraction instead.
- **Obsidian plugin dependency**: The full user experience assumes Obsidian. For novel wiki, if you want a lightweight web UI without Obsidian, reimplement the query/ingest frontend without the plugin dependency.
- **No explicit canon/research separation fields**: Synthadoc uses status (active|draft|contradicted|stale|archived) to signal authority, but frontmatter has no explicit "is_canon" vs "is_research" field. You'd need to add a field or use a slug naming convention (e.g., `canon-*` vs `research-*`).
- **Wikilink syntax only**: Cross-references are hardcoded as `[[slug]]` Markdown links. No semantic edge types (e.g., "contradicts", "refines", "depends-on") are stored in frontmatter; edge types only exist in the graph DB. For explicit relationship tracking, extend the frontmatter schema.
- **Single-machine deployment**: Synthadoc is local-first (localhost-only). No built-in multi-user concurrency control beyond file locks. For team collaboration, you'd need to add git-based conflict resolution or a shared database backend.
- **No explicit research question / discovery workflow**: Synthadoc ingests and organizes sources, but doesn't have a built-in "research question → evidence pack → synthesis → publish" workflow. You'd need to layer that on top via custom skills or agentic workflows.

## 6. Verdict (One Paragraph)

Synthadoc is a **production-grade, reusable architecture** for a novel-research wiki that directly addresses canon/research separation, contradiction detection, and provenance. **Steal**: the WikiPage + LifecycleState machine (draft/active/stale/archived), the ingest-time decision logic (RULE 1–3), active page protection, AuditDB immutable event log with snapshots, wikilink graph + Louvain clustering, claim-level citations with line-scoped references, the 3-layer cache, and agentic workflows with approval gates. **Adapt**: license the Apache-2.0 base classes (BaseSkill, LLMProvider) but route LLM calls through DSPy instead of Synthadoc's provider abstraction. Add explicit "canon" vs "research" frontmatter fields or slug namespacing. Layer a research-question discovery workflow on top of ingest/query. Extend the MCP server to expose novel-specific verbs (e.g., `publish_canon`, `flag_research_conflict`). The contradiction detection, orphan fixing, and snapshot rollback patterns are immediately reusable; the Obsidian plugin can be optional (keep the storage layer portable). Cost: ~15K lines of Python, but the core abstractions (storage, lifecycle, lint) compress cleanly into ~3K; the remaining 12K is LLM orchestration + skills + web UI, which you can selectively adopt or replace with DSPy agents.
