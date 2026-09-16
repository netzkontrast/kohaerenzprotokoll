# llm-wiki-compiler Repository Survey

## 1. What It Is

llm-wiki-compiler is a mature TypeScript knowledge-compilation system that transforms raw source documents (PDFs, web pages, markdown, etc.) into a durable, interlinked wiki with structured metadata, citations, and review gates. It implements Andrej Karpathy's LLM Wiki pattern as a production-ready CLI, SDK, and MCP server. Sources compile through a two-phase LLM pipeline (concept extraction, then page generation) into typed, markdown-native wiki pages with YAML frontmatter. Currently at v1.3.0 with multiple provider support (Anthropic, OpenAI, Ollama, GitHub Copilot, etc.).

## 2. Architecture

### Directory Layout
- **`sources/`** — Raw immutable source documents (text, PDFs, images, web content); never edited
- **`wiki/`** — Compiled output: `concepts/` (concept pages), `queries/` (saved answers), `index.md` (auto-generated TOC); plain markdown with wikilinks
- **`.llmwiki/`** — Compiler state and config: `state.json` (source hashes, concept ownership), `profile.json` (domain model contract), `config.json` (review policy), `embeddings.json` or `.bin` (vector index), `candidates/` (review queue)
- **`log.md`** — Append-only activity journal with parseable timestamps
- **`artifacts/`** — Content-addressed profile-declared artifacts with hash pinning

### Data Model & Frontmatter
Every compiled page is plain markdown with YAML frontmatter. Standard fields include:
- **`title`**, **`summary`**, **`kind`** (concept/entity/comparison/overview)
- **`sources`** — Array of source filenames that produced this page
- **`createdAt`**, **`updatedAt`** — ISO timestamps
- **`orphaned`**, **`contradictedBy`**, **`archived`** — Metadata flags
- **`confidence`** — LLM confidence score (optional, triggers review gates)
- Custom fields declared in profile (e.g., `doi`, `status`, `year` for research profiles)

Pages use `[[wikilink]]` syntax (Obsidian-compatible) and inline citations: `^[source-file.md:123-456]` for paragraph-level source attribution.

### Compile Pipeline (Two Phases)
1. **Phase 1 — Concept Extraction**: All changed sources → LLM → extract concepts + metadata; all extractions complete before any page write; knowledge of cross-source concepts captured here
2. **Phase 2 — Page Generation**: Per extracted concept → LLM generates structured page; multi-source concepts merge into one page instead of duplicating
3. **Post-compile**: Chunk embeddings computed, index rebuilt, wikilinks resolved, review candidates staged per policy

Incremental compilation via SHA-256 source hashing (`.llmwiki/state.json`): unchanged sources skip the LLM entirely.

### Source Contract
Sources are tracked by filename and SHA-256 hash in `.llmwiki/state.json` under `state.sources[filename].concepts` (array of page slugs derived from that source). No schema file required; all sources ingest as-is. Supported formats (auto-converted to markdown): `.md`, `.pdf`, `.docx`, `.pptx`, `.xlsx`, `.html`, `.txt`, `.csv`, `.json`, `.xml`, `.rst`, `.rtf`, `.epub`, `.ipynb`, `.yaml`, `.wav`, `.mp3` (via `markitdown` library).

### LLM vs Deterministic Boundaries
- **LLM-backed**: concept extraction, page generation, query answering, citation support evaluation
- **Deterministic**: hash comparison, wikilink resolution, citation validation, lint rules, orphan/stale detection, index generation, freshness computation, profile validation, review policy application
- **Hybrid caching**: Content-hash-aware embedding updates, citation judgement caching (`.llmwiki/eval/citation-cache.jsonl`)

### Configurable Lifecycle Profiles (CLP)
**Profile** (`profile.json`) is the domain model contract. Declares:
- **Entity types** — directories (e.g., `papers/`, `ideas/`), fields, field types, defaults, required state
- **Relations** — typed edges between entity types with directionality, counts, and standing invariants
- **Lifecycles** — finite-state machines over one frontmatter field (e.g., `status: concept→drafted→submitted`); gated transitions
- **Workflows** — multi-stage processes with read/write/gate declarations, action shortcuts, artifact outputs
- **Artifacts** — hash-pinned files with manifest metadata; artifact-existence preconditions on lifecycle states
- **Connectors** — first-party data imports (e.g., Crossref for papers) that stage review candidates

All enforcement is data-driven, not hardcoded. Default profile (no `profile.json`) preserves original behavior (concepts + queries).

### Config Files
- **`.llmwiki/config.json`** — Review policy: which hold modes active (`low-confidence`, `contradicted`, `schema-violating`, `provenance-violating`) and thresholds
- **`.llmwiki/schema.json`** — Optional page-kind policy: min wikilinks per kind, seed pages to materialize
- **`.llmwiki/state.json`** — Source ownership: per-file hashes + concept slugs it owns
- **`log.md`** — Fixed-format headers `## [ISO-TIMESTAMP] operation | description` (grep-parseable); useful for agents to audit operation history

## 3. Concepts Worth Stealing

1. **Two-Phase Compile with Cross-Source Merging** (`src/compiler/index.ts`, `extraction-phase.ts`, `extraction-merge.ts`)
   - Phase 1 extracts all concepts before writing any pages, enabling deterministic merging of duplicate concepts across sources
   - **Why useful**: For novel research, you need to know when two research docs claim the same worldbuilding fact (a contradiction) or refine the same rule. Merging at compile time means the graph sees unified entities, not competing chunks.
   - Exact paths: `src/compiler/extraction-phase.ts` (LLM extraction), `extraction-merge.ts` (cross-source dedup), `rule-candidates.ts` (candidate ranking)

2. **Source Hashing & Freshness Tracking** (`src/freshness/index.ts`, `src/compiler/hasher.ts`)
   - SHA-256 hashing per source; `state.json` records ownership (which page slugs derived from which files); freshness computed on-demand without re-reading state
   - Four-state enum: `fresh` (all owners exist, hash matches), `stale` (owner exists but hash changed), `orphaned` (all owners deleted), `unverified` (query pages, hand-authored)
   - **Why useful**: Canon is immutable until explicitly changed; research docs can be refreshed independently. Stale detection means you catch when a research assumption invalidates existing canon.
   - Exact paths: `src/freshness/index.ts` (freshness classification), `src/compiler/hasher.ts` (SHA256 per file)

3. **Profile-Enforced Lifecycle Gates** (`src/profile/lifecycle.ts`, `validate-relation-requirements.ts`, `validate-artifact-requirements.ts`)
   - Profiles declare state machines with typed preconditions: relation counts (e.g., a character must know ≥2 facts before marked `established`), artifact existence, field contracts
   - Gates enforced at write time (compile, workflow, review approval) — not left as prompt conventions
   - **Why useful**: Canon rules (e.g., "a motif can't be first used after Act II") become machine-checkable preconditions. Research-to-canon promotion can require proof (artifacts, citations) before allowing state transition.
   - Exact paths: `src/profile/lifecycle.ts` (state machine), `validate-relation-requirements.ts` (relation precondition load validation), `enforce-precondition.ts` in relations/ (write-time enforcement)

4. **Citation Paragraph-Level Tracing** (`src/linter/rules-citations.ts`, `compiler/citation-normalize.ts`)
   - Pages cite sources line-range: `^[file.md:123-456]`. Lint checks for malformed, broken, or missing citations
   - Citable-segment extraction; pages with generated or inferred content (not directly cited) flagged
   - **Why useful**: Novel prose needs to cite which research doc inspired a scene's sensory detail or character decision. Citation tracking prevents hallucinated provenance.
   - Exact paths: `src/linter/rules-citations.ts` (citation validation rules), `citation-normalize.ts` (citation parsing)

5. **Lint Rules as Pure Static Analysis** (`src/linter/index.ts`, `rules.ts`, `rules-citations.ts`, `rules-crosslinks.ts`)
   - 13 rule families: wikilinks, orphans, citations, confidence, contradictions, schema violations, freshness, duplicates, empty pages, inferred-without-source, journal health, pending embeddings, workflow runs
   - Rules run concurrently; no LLM calls; deterministic output
   - **Why useful**: Daily health checks for canon/research separation, broken links, missing provenance, stale assumptions. Use in CI to prevent bad commits.
   - Exact paths: `src/linter/rules.ts` (main rules), `rules-citations.ts` (citation checks), `rules-crosslinks.ts` (schema-aware link rules)

6. **Review Candidates with Approval Pinning** (`src/review/`, `src/compiler/candidates.ts`)
   - Pages can be held for review based on confidence, contradiction, schema, or provenance rules
   - Candidates stored in `.llmwiki/candidates/` as JSON; rejected move to `archive/` for audit
   - External data (OKF imports, connector fetches) pinned to exact reviewed body (`--draft-content-hash`) so approval locks the exact content the operator reviewed
   - **Why useful**: Research ingestion can be auto-held until a human reviews it for alignment with canon. Pinning prevents drift between review and approval.
   - Exact paths: `src/review/` (approval workflow), `src/compiler/candidates.ts` (candidate lifecycle), `rule-candidates.ts` (triggering conditions)

7. **Open Knowledge Format (OKF) Import/Export** (`src/export/okf/`, `src/import/`)
   - Portable markdown with structured frontmatter for knowledge exchange
   - OKF imports stage as review candidates by default (untrusted); trusted imports validate against profile
   - Re-export preserves foreign producer keys + original paths; local edits reflected; no data loss
   - **Why useful**: Research wiki can accept OKF bundles from external systems (other teams, research archives) without contaminating canon. Staged review gates external data.
   - Exact paths: `src/export/okf/` (OKF generation), `src/import/okf.ts` (OKF parsing + staging), `src/import/index.ts` (review-gated approval)

8. **Eval Harness with Citation Support** (`src/eval/index.ts`, `citation-support.ts`, `health.ts`)
   - Health score: per-page freshness, citation coverage, wikilink density, orphaned count
   - Optional LLM judge for citation quality (do cited spans actually support claims?)
   - Cached citation judgements avoid re-running expensive judges
   - **Why useful**: Measure research wiki quality over time; detect when ingest broke citation coverage. LLM judge catches hallucinated citations.
   - Exact paths: `src/eval/index.ts` (orchestrator), `citation-support.ts` (LLM-based judgment), `health.ts` (freshness/orphan/stats aggregation)

9. **Profile-Aware Linting** (`src/profile/lint.ts`, `relation-lint.ts`, `event-lint.ts`, `artifact-lint.ts`)
   - When profile loaded, lint enforces typed constraints: entity-type consistency, relation direction/endpoint validity, lifecycle standing invariants, artifact hash integrity
   - Linting is profile-aware; default profile produces byte-identical output to non-profile linting (no lint noise)
   - **Why useful**: Canon entities must satisfy their profile contract. Research entities can trigger lint if they violate canon invariants.
   - Exact paths: `src/profile/lint.ts` (profile entity lint), `relation-lint.ts`, `event-lint.ts`, `artifact-lint.ts` (constraint checks)

10. **Hybrid Retrieval** (`src/search/`, `context/builder.ts`)
    - Cosine similarity (dense embeddings) → BM25 reranking (lexical relevance) → wikilink-graph expansion (contextual neighbors)
    - Chunk-level embeddings with qualified page IDs; binary storage for large indexes
    - Lexical-only fallback when provider has no embedding endpoint
    - **Why useful**: Query for research that informs a scene returns not just semantically similar papers but their conceptual neighbors in the wiki graph. Citation-aware context packs for agents.
    - Exact paths: `src/search/` (retrieval orchestration), `context/builder.ts` (evidence-pack construction)

11. **Append-Only Activity Journal** (`log.md`)
    - Fixed header format: `## [YYYY-MM-DDThh:mm:ssZ] operation | description`
    - Parseable with grep; agents can read to audit what was compiled when
    - **Why useful**: Track research ingest history; detect when a critical assumption was introduced; audit trail for contradictions.
    - Exact format: `## [ISO-TIMESTAMP] ingest|compile|query|lint|eval | title` + bullet body with wikilinks + counts

12. **Artifact Hash Pinning** (`src/artifacts/`, `src/profile/validate-artifact-requirements.ts`)
    - Artifacts (files referenced in pages) are content-addressed: stored at hash, manifest records hash
    - Artifact-ref frontmatter fields point to these; profile can require artifact presence to allow lifecycle transition
    - **Why useful**: Canon can require that a character-design scene include an image or a fact check includes a PDF proof. Hash pinning prevents silently replacing artifacts.
    - Exact paths: `src/artifacts/` (artifact lifecycle), `profile/validate-artifact-requirements.ts` (gate logic)

13. **MCP Server Integration** (`src/mcp/`, `serve` command in CLI)
    - All ingest, compile, query, lint, eval, context, review, OKF functions exposed as MCP tools
    - Agents can drive wiki operations without shelling out
    - **Why useful**: Subagents can autonomously research, ingest findings, and run lint gates. No human in the loop for deterministic checks.
    - Exact paths: `src/mcp/` (tool definitions), `src/commands/serve.ts` (MCP server launch)

## 4. Reusable Code/Assets

1. **`src/compiler/hasher.ts`** — SHA-256 file hashing logic; used for source ownership tracking
2. **`src/freshness/index.ts`** — Freshness classification (fresh/stale/orphaned/unverified); pure compute, no I/O
3. **`src/linter/rules.ts` and siblings** — 13 independent lint rule implementations; can be ported to Python as deterministic checks
4. **`src/profile/types.ts`** — Profile data structures (entity types, field contracts, lifecycle definitions, relation types); TypeScript branded types model; port to Python Pydantic
5. **`docs/concepts/wiki-model.mdx`** — Authoritative specification of page structure, frontmatter schema, directory layout; use as reference for Python wiki model
6. **`.llmwiki/profile.json` schema in `src/profile/schema/`** — Full profile validation schema; can extract JSON Schema and use with DSPy validation
7. **`src/compiler/prompts.ts` and `rule-prompts.ts`** — Concept extraction + page generation prompt templates; easily portableto Python LLM calls
8. **`src/export/okf/`** — OKF generation logic; can study to port OKF export to DSPy
9. **`docs/concepts/configurable-lifecycle-profiles.mdx`** — CLP design rationale; guides profile-aware wiki design
10. **`docs/guides/open-knowledge-format.mdx`** — OKF workflow; informs knowledge exchange design

## 5. Not Useful / Caveats

- **TypeScript stack vs. Python/DSPy base**: llmwiki is production TypeScript; cannot directly vendor code. Patterns and design must be ported to Python (Pydantic, DSPy LLM chains, async)
- **Provider abstraction layer heavy**: llmwiki supports 8+ LLM providers; DSPy already abstracts that, so the provider isolation logic doesn't transfer
- **Viewer is browser-based SvelteKit**: Read-only UI for browsing compiled wiki; novel research wiki may need different UX (e.g., direct editing, inline suggestions)
- **Node.js-only CLI**: Binary assets (embedding indexes) use Node.js Buffer; Python would use numpy
- **Profile complexity assumption**: Assumes teams want richer domain models (workflows, artifacts, connectors); simple research wiki might not need that level
- **Embedding provider dependency**: All retrieval assumes embeddings provider (Anthropic, OpenAI, etc.); Python/DSPy could fall back to lexical-only but evaluation would differ
- **OKF as primary export target**: Useful for knowledge exchange but assumes adoption by external systems; internal research wiki might use different formats (JSON, SQLite, graph database)

## 6. Verdict

**llm-wiki-compiler is an authoritative reference for a production research wiki design.** For the novel-research wiki project, the most valuable transfers are:

1. **Two-phase compile with deterministic concept merging** — Core pattern to steal for handling research docs that describe the same worldbuilding concept
2. **Source hashing + freshness tracking** — Critical for detecting when research invalidates existing canon
3. **Profile-enforced gates** — Enables typed validation (e.g., "character must have ≥2 scenes before marked `established`")
4. **Lint-rule architecture** — Pure static analysis (no LLM) for daily health checks
5. **Citation paragraph-level tracing** — Ensures research assumptions are attributed to sources
6. **Review candidate workflow** — Staging external/ingest data for human approval before canon promotion

Do **not** attempt to use TypeScript code directly. Instead, read the design docs (`configurable-lifecycle-profiles.mdx`, `wiki-model.mdx`, `how-it-works.mdx`) and port the patterns to Python + DSPy. The profile schema and lint rule taxonomy are the highest-ROI reference points. Expect to write a fresh Python implementation; the conceptual depth (especially CLP and freshness semantics) is the durable asset.
