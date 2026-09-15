# Quicky Wiki Repository Survey

## What It Is

Quicky Wiki is a Node.js/TypeScript CLI tool that builds a confidence-scored knowledge graph from ingested sources (markdown, PDFs, URLs). It extracts claims via LLM, tracks epistemic events (reinforced/challenged/weakened), measures confidence decay over time, and detects contradictions and cascade risks. The tool compiles to multiple formats (wiki, slides, flashcards, graph, timeline) and exposes an HTTP dashboard and MCP server for querying. Maturity: early production (v0.1.2, npm published, MIT licensed).

**Stack:** Node.js 20+, TypeScript, SQLite with FTS5, Commander.js CLI, better-sqlite3, Anthropic/OpenAI/Gemini/Ollama LLM adapters.

## Architecture

### Core Components

**Data Layer:** `src/graph/store.ts` — SQLite database (`.quicky/graph.sqlite`) with 8 core tables (sources, pages, claims, epistemic_events, claim_sources, claim_dependencies, claim_contradictions, page_links) plus FTS5 virtual tables for full-text search. Uses WAL mode, 64MB cache, memory-mapped I/O. Pre-prepared statements for performance.

**Claim Extraction:** `src/compiler/ingest.ts` — reads source files (auto-detects markdown/PDF/URL/HTML), parses frontmatter, passes to LLM (via `src/llm/adapter.ts`) with schema asking for claims, tags, page title, and contradictions. `src/compiler/diff.ts` computes knowledge delta (reinforced, challenged, new, gaps).

**Graph Query:** `src/graph/query.ts` — uses FTS5 search to find relevant pages/claims, builds context, queries LLM with chat interface, returns answer + claim IDs + confidence. `src/graph/cascade.ts` implements dependency propagation: when a foundational claim confidence changes, dampened deltas cascade to dependents (depth limit 10, damping 0.5).

**Temporal Tracking:** `src/graph/temporal.ts` — applies exponential confidence decay (`confidence * e^(-decayRate * daysSince)`); default decay rate 0.002/day. Tracks epistemic events as a timeline.

**Rendering:** `src/render/` suite — markdown (frontmatter + claims per page, `[[wikilinks]]`), Marp slides, Anki flashcards, D3 graph, timeline. All use YAML frontmatter with kind/metadata/confidence metadata.

**Discovery:** `src/discovery/discover.ts` — LLM-driven modes (gaps, horizon, bridges, contradictions) read claim context, return ranked suggestions with related claims.

**CLI Commands:** `src/cli.ts` orchestrates 15 subcommands: `init`, `ingest`, `query`, `claims`, `timeline`, `metabolism` (health/decay/resurface/redteam), `compile`, `discover`, `lint`, `watch`, `export`, `serve` (HTTP dashboard), `mcp` (Model Context Protocol server).

**Health Checks:** `src/metabolism/health.ts` generates report: confidence distribution, stale claims (no reinforcement >N days), contested claims (with contradictions), cascade risks (foundational claims with many dependents). `redteam.ts` adversarially challenges high-confidence claims.

### LLM Abstraction

`src/llm/adapter.ts` — provider-agnostic chat interface supporting Anthropic, OpenAI, Gemini, Ollama, and OpenAI-compatible (Groq, Together, vLLM, LM Studio). Auto-detects API keys from environment. Returns structured JSON responses parsed by `src/llm/parse-json.ts`.

### Config & CLI Context

`src/cli/context.ts` — loads `.quicky/config.yaml` (provider, model, apiKey, baseUrl), opens/closes store, creates LLM adapter. `src/cli/create.ts` scaffolds zero-config initialization.

## Concepts Worth Stealing

1. **Confidence Scoring with Decay** (`src/graph/temporal.ts`, `src/types.ts` lines 55-69)
   - *What:* Each claim has 0–1 confidence, decays exponentially when not reinforced, reinforced/challenged via LLM when new sources ingest.
   - *Why for novel-research wiki:* Canon facts must be traceable to source quality (peer-reviewed vs blog); decay signals which research is stale and needs re-verification. Prevents silent rot in research assumptions.
   - *Files:* `src/graph/temporal.ts`, `src/types.ts` (Claim interface), `src/graph/store.ts` (updateClaimConfidence).

2. **Cascade Propagation on Contradiction** (`src/graph/cascade.ts`)
   - *What:* When a foundational claim is challenged, confidence changes cascade to dependent claims with dampening (0.5x per level, depth limit 10). Prevents orphaned high-confidence claims built on shaky foundations.
   - *Why for novel-research wiki:* If core physics axiom (e.g., "Multiplizität is linear") is challenged, all downstream plot mechanics automatically weaken. Surfaces cascade risks (claims with 10+ dependents but <60% confidence).
   - *Files:* `src/graph/cascade.ts`, `src/graph/store.ts` (getDependents, updateClaimConfidence).

3. **Knowledge Diff on Ingest** (`src/compiler/diff.ts`, CLI output in `src/cli/ingest.ts` lines 11–72)
   - *What:* Each ingest prints delta: N claims reinforced (confidence ↑), N challenged (↓), new concepts, new claims, knowledge gaps identified. Maps which source changed what.
   - *Why for novel-research wiki:* Prevents silent canon mutations. User sees exactly what changed when they ingest a paper. Contradictions flag immediately. Gaps surface research leads.
   - *Files:* `src/compiler/diff.ts`, `src/types.ts` (KnowledgeDiff interface), `src/cli/ingest.ts` (printDiff).

4. **FTS5 Search + LLM Re-ranking** (`src/graph/query.ts`, `src/graph/store.ts` lines 92–105)
   - *What:* SQLite FTS5 finds top-50 matching claims/pages (phrase + boolean ops), LLM re-ranks and synthesizes with confidence scores, caveats. Avoids loading full graph into context window.
   - *Why for novel-research wiki:* Allows chat-style Q&A against 10k+ claims without token explosion. Justifies answers with specific claim IDs and confidence bands (WARN if <50%).
   - *Files:* `src/graph/query.ts`, `src/graph/store.ts` (search method, FTS triggers), `src/types.ts` (WikiPage, Claim, LLMAdapter).

5. **Entity Kind + Metadata per Page** (`src/types.ts` lines 72–84, `src/compiler/ingest.ts` lines 39–63)
   - *What:* Pages carry kind (topic/entity/concept/etc. via rules: path pattern or frontmatter type) + metadata YAML. Ingest rule engine: first match wins (pattern substring or type:value).
   - *Why for novel-research wiki:* Distinguish character entries from world axioms from thematic concepts. Metadata can hold character status (alive/dead/NPC), world-id backrefs, research status. MCP endpoint `list_entities` filters by kind.
   - *Files:* `src/types.ts`, `src/compiler/ingest.ts` (inferPageKind, syncPrimaryPageEntity), `src/render/markdown.ts` (frontmatter generation).

6. **Epistemic Event Timeline** (`src/types.ts` lines 44–53, `src/graph/store.ts` lines 65–74)
   - *What:* Every claim has timeline: created/reinforced/challenged/weakened/superseded/resolved with date, trigger source, confidence before/after. Append-only log in epistemic_events table.
   - *Why for novel-research wiki:* Audit trail: which source changed belief in a fact? When? By how much? Enables "show all challenges to fact X" or "what happened when we ingested author-notes.md?"
   - *Files:* `src/types.ts`, `src/graph/store.ts`, `src/cli/timeline.ts` (render per-concept timeline).

7. **Health Metabolism** (`src/metabolism/health.ts`, `src/metabolism/decay.ts`, `src/metabolism/resurface.ts`, `src/metabolism/redteam.ts`)
   - *What:* Commands run diagnostics: `--report` (stale/contested/cascade-risk claims), `--decay` (run confidence decay), `--resurface` (get claims to review), `--redteam` (LLM adversarially challenges high-confidence claims).
   - *Why for novel-research wiki:* Prevents canon drift. Stale assumptions get flagged. Contradictions surface. High-confidence but foundation-weak claims get stress-tested before being "locked" as canon.
   - *Files:* `src/metabolism/`, `src/cli/metabolism.ts`, `src/types.ts` (HealthReport).

8. **Multi-Format Compilation** (`src/render/`)
   - *What:* Compile same graph to markdown (Obsidian compatible), Marp slides, Anki flashcards, D3 graph, timeline. Uses `WikiPage`/`Claim` types directly.
   - *Why for novel-research wiki:* Research knowledge lives in wiki but author wants slides for worldbuilding review, cards for spaced repetition, graph for thematic networks. Single source, multiple targets.
   - *Files:* `src/render/markdown.ts`, `src/render/marp.ts`, `src/render/anki.ts`, `src/render/graph-viz.ts`, `src/render/timeline.ts`.

## Reusable Code/Assets

- **SQLite schema + FTS setup:** `src/graph/store.ts` lines 13–129. Copy the SCHEMA + FTS_SCHEMA + FTS_TRIGGERS for Python SQLite integration.
- **LLM adapter factory:** `src/llm/adapter.ts`. Pattern: provider factory with shared interface. Can be ported to DSPy as a thin layer selecting DSPy LM based on env vars.
- **Confidence decay formula:** `src/graph/temporal.ts` lines 13–14. Exponential with configurable rate; easy to replicate in Python.
- **Cascade algorithm:** `src/graph/cascade.ts` lines 24–43. Recursive walk with damping and cycle detection. Core logic is provider-agnostic.
- **Markdown rendering template:** `src/render/markdown.ts` lines 41–84. YAML frontmatter + Obsidian wikilinks pattern reusable for Python rendering.
- **Episode event types:** `src/types.ts` lines 36–42. Enum: created/reinforced/challenged/weakened/superseded/resolved. Port directly to Python TypedDict.

## Not Useful / Caveats

- **Language:** TypeScript/Node.js. Your project uses Python + DSPy. No direct code reuse; architecture/patterns are portable but implementation requires rewrite.
- **SQLite ORM:** Uses raw SQL + prepared statements. Python will likely want SQLAlchemy or similar; schema is portable but query patterns differ.
- **CLI framework:** Commander.js (Node). Python equivalent would be Click, Typer, or ArgumentParser.
- **Dashboard/MCP:** Embedded in dist bundle (tsup build). Python would need Streamlit/FastAPI + separate HTTP server.
- **FTS5 gotchas:** better-sqlite3 has quirks with FTS rebuild. Python's sqlite3 is simpler but less performant; may need search ranking fallback.

## Verdict

Quicky Wiki is a production-quality, well-architected system for evidence-based knowledge graphs with temporal semantics. Its cascade propagation, confidence decay, epistemic event logging, and multi-format compilation are directly applicable to a novel-research wiki. The LLM extraction pipeline (schema-driven claim extraction, contradiction detection, gap discovery) and health-check metabolism are patterns worth adopting. However, the TypeScript/Node stack is orthogonal to a Python/DSPy base. The real value is conceptual: steal the cascade model, decay formula, entity-kind typing, and event timeline architecture; rebuild the implementation in Python with DSPy as the LLM substrate and a relational DB schema ported from SQLite. The CLI structure and skill-integration patterns are less directly useful given your agency/Claude Code target, but the CLI commands (ingest, query, metabolism, discover, compile) map cleanly to Claude Code slash commands or agency verbs.
