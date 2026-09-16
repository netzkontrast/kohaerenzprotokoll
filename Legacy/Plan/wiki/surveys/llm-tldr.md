# Survey: llm-tldr Repository

**Location:** `/home/user/llm-tldr`  
**License:** AGPL-3.0 (with some MIT-licensed components from original tldr-code)  
**Language:** Python 3.10+  
**Maturity:** Production-ready (v1.5.2, PyPI published)

---

## 1. What It Is

**llm-tldr** is a mature, production-grade Python package that extracts code *structure* instead of code *text*, reducing token usage by **95%** while preserving semantic meaning. It builds a **5-layer analysis stack** (AST → Call Graph → CFG → DFG → PDG) to support everything from quick file browsing to deep program slicing. The tool runs a per-project daemon with in-memory indexes for 300x faster queries than CLI spawns, and includes a semantic search layer using `bge-large-en-v1.5` embeddings via FAISS. It supports 17 languages (Python, TypeScript, JavaScript, Go, Rust, Java, C/C++, Ruby, PHP, C#, Kotlin, Scala, Swift, Lua, Elixir) with hybrid extraction strategies (Python's `ast` module for speed, tree-sitter for other languages, Pygments fallback).

---

## 2. Architecture

### Core Pipeline

The system processes code through this deterministic stack:

```
Source Files → [Tree-sitter/AST] → Layer 1 (AST signatures)
            → [Hybrid Extractor]  → Layer 2 (Call Graph)
            → [CFG Extractor]     → Layer 3 (Control Flow)
            → [DFG Extractor]     → Layer 4 (Data Flow)  
            → [PDG Extractor]     → Layer 5 (Program Dependence)
            → [Semantic Indexer]  → 1024-dim embeddings (FAISS)
            → [Daemon]            → In-memory indexes + socket API
```

**Layer responsibilities:**
- **L1 (AST):** Extracts function signatures, class hierarchy, imports, docstrings, type hints—all via tree-sitter for most languages, Python's `ast` for Python files (faster, more precise).
- **L2 (Call Graph):** Builds bidirectional call edges (who calls what + who calls me). Uses language-specific heuristics: Python AST walking, tree-sitter for TS/JS/Go/Rust, regex fallback for others.
- **L3 (CFG):** Control flow graph with cyclomatic complexity, branch/loop counts, block counts. Enables debugging via program slicing (what code affects line N?).
- **L4 (DFG):** Data flow—tracks variable definitions, uses, transformations. Identifies control dependence and def-use chains.
- **L5 (PDG):** Combines CFG + DFG into program dependence graph; powers `tldr slice` (surgical line extraction).

**Daemon:** Long-running server (one per project, socket-based per project hash) holds indexes in RAM (~50–100MB base, 500MB–1GB with embeddings). Auto-reindexes on file-change thresholds (default: 20 dirty files) in background. Auto-shutdown after 30 min idle.

**Semantic Layer:** Every function gets indexed with L1–L5 metadata + first ~10 lines of code → encoded into 1024-dim vectors → FAISS index for natural-language search (e.g., "validate JWT" finds `verify_access_token()` even without that text).

**Caching Strategy:**
- **Content-hash dedup** (`dedup.py`): Files with identical content share index entry. Tracks {content_hash → edges} + {file_path → content_hash}. Saves 10–20% storage on projects with copy-pasted utilities or generated files.
- **Incremental parse** (`incremental_parse.py`): Tree-sitter can re-parse only edited regions (10–100x faster than full reparse). Caches parse trees for reuse across queries.
- **Dirty-flag tracking** (`dirty_flag.py`): Tracks which files changed. Semantic re-indexing waits for threshold (auto_reindex_threshold, configurable, default 20).
- **Durability partitioning** (`durability.py`): Classifies files as DURABLE (node_modules, .venv, vendor) vs VOLATILE (user code). Durable portions loaded once on startup, never re-indexed.
- **Query memoization** (`daemon/cached_queries.py`): Daemon caches query results (context, cfg, dfg, slice, etc.) keyed by (function_name, file_path, query_type).

**Extraction approach:** 
- **Python:** Native `ast` module (fastest, most accurate). Walks AST for defs/uses.
- **TypeScript/JavaScript:** tree-sitter + custom CommonJS/ESM require/import walker.
- **Other languages:** tree-sitter for Go/Rust/Java/etc., Pygments regex fallback for rare languages.

**Storage:**
- Indexes live in `.tldr/cache/` (call_graph.json, semantic.faiss, content_index.json, etc.).
- Daemon config: `.tldr/config.json` or `.claude/settings.json`.
- MCP integration: Registers `tldr-mcp` command for Claude Desktop/Claude Code.

---

## 3. Concepts Worth Stealing

For ingesting 680 heterogeneous research documents into a novel wiki, these patterns are high-value:

### 1. **Content-Hash Deduplication** (`tldr/dedup.py`, lines 1–185)
**What:** Store {content_hash → metadata} with lookup {file_path → hash}. Identical files share one index entry.  
**Why:** Research includes many duplicated/near-duplicated versions of concept papers. Dedup avoids re-processing the same content multiple times. Can save 10–20% storage/compute. `get_or_create_edges()` checks hash before extraction; cache hits increment a counter for observability.  
**For KP wiki:** When ingesting the same paper from multiple drive locations (v1, v1_final, v1_final_final), dedup detects it via SHA-1 and reuses the single extracted summary. Track dedup stats to flag to the user that duplicates were found.

### 2. **Hierarchical Layer-Based Analysis** (5-layer stack: AST → CallGraph → CFG → DFG → PDG)
**What:** Each layer answers a different question. Query only the layer you need.  
**Why:** Not every question needs full PDG analysis (expensive). Different users have different workflows—fast browsing vs. deep understanding. Layering makes it cheap to ask L1 (structure) vs. expensive (but precise) L5 (slice).  
**For KP wiki:** Model canon-vs-research separation as layers: Layer 1 (document metadata), Layer 2 (canon claims/world axioms vs. research claims), Layer 3 (contradictions detected), Layer 4 (character/world knowledge graph), Layer 5 (reconciliation/synthesis). Query only the layers needed for each task.

### 3. **Dirty-Flag Driven Incremental Indexing** (`tldr/dirty_flag.py`, `tldr/session_warm.py`)
**What:** Track which files changed, batch updates only when dirty count exceeds threshold (e.g., 20 files).  
**Why:** Avoids re-indexing on every single file edit. Batching is cheaper than per-file updates. Threshold is configurable.  
**For KP wiki:** When ingesting a batch of papers, mark them dirty. After N papers, trigger re-synthesis (coherence check, contradiction detection). Don't re-run expensive gates after every ingest; batch them. `_dirty_count` and `_dirty_files` in daemon/core.py lines 85–86 show the pattern.

### 4. **Durability Partitioning** (`tldr/durability.py`)
**What:** Classify files as DURABLE (rarely change: dependencies) or VOLATILE (frequently change: source). Load durable once, never re-index.  
**Why:** Don't waste cycles on static dependencies. Load node_modules once, forget it.  
**For KP wiki:** Partition canon into DURABLE (published storyform, world axioms—rarely edited) and VOLATILE (draft chapters, research notes—frequently edited). Load canon axioms once; ingest research on demand without touching canon.

### 5. **Semantic Embedding with Context Enrichment** (`tldr/semantic.py` via sentence-transformers + FAISS)
**What:** Every function/entity gets encoded with multi-layer metadata (signature, calls, CFG complexity, code snippet) → 1024-dim vectors. FAISS index for natural-language queries.  
**Why:** Natural-language search finds code by *what it does*, not text match. "Validate JWT" finds `verify_token()` because the embedding captures purpose.  
**For KP wiki:** Encode each research document summary with: type (plot, character, physics, etc.), domain tags, contradictions flagged, canon references. Then query by natural language: "What explains the Multiplizitäts-Schleier?" Returns papers ordered by relevance, not just keyword match.

### 6. **Incremental Parse Caching** (`tldr/incremental_parse.py`)
**What:** Tree-sitter can re-parse only edited regions of a file (not the whole file). Cache parse trees.  
**Why:** 10–100x speedup on edits to large files.  
**For KP wiki:** When a user re-uploads a revised research paper (e.g., physics_theory_v1.md → physics_theory_v2.md, only 5% changed), tree-sitter re-parses only the changed section. Faster extraction of summaries.

### 7. **Cross-File Call Graph with Bidirectional Edges** (`tldr/cross_file_calls.py`, `tldr/hybrid_extractor.py`)
**What:** Build forward call graph (A calls B) and backward (B is called by A). Both directions enable impact analysis.  
**Why:** Forward answers "what does this do?", backward answers "what breaks if I change this?".  
**For KP wiki:** Bidirectional "cites" graph: forward = "this paper cites X", backward = "papers that cite this". Also bidirectional "contradicts": A contradicts B ⟷ B contradicts A. Enables "impact of change" queries.

### 8. **FAISS Semantic Index with Fast Rebuilding** (PyPI: `faiss-cpu>=1.13.2`, indexed in daemon)
**What:** 1024-dim embeddings in FAISS, auto-rebuilt when dirty files exceed threshold.  
**Why:** FAISS is industry-standard for fast vector search. Auto-rebuild avoids stale indexes.  
**For KP wiki:** Store document summaries + world axiom descriptions as embeddings. On ingest of N new papers, mark dirty. At threshold, re-embed and rebuild FAISS. Then `semantic_search("theme of isolation")` returns relevant papers ranked by similarity.

### 9. **Configuration via Multiple Sources with Precedence** (`daemon/core.py` lines 112–147)
**What:** Load config from `.claude/settings.json` (highest priority) → `.tldr/config.json` → built-in defaults.  
**Why:** Claude users get IDE-integrated config. TLDR-specific users get `.tldr/config.json`. Non-configured users get sensible defaults. No breaking changes.  
**For KP wiki:** Load overrides from `Canon/.claude/wiki-config.json` (canon settings) and `Research/.claude/wiki-config.json` (research settings). E.g., canon has `contradiction_threshold: hard`, research has `soft`. Enables per-layer policy.

### 10. **Efficient Token Counting + Stats Tracking** (`tldr/stats.py`)
**What:** Tracks token usage per query (via tiktoken), per session, per hook (git/editor).  
**Why:** Observability. Know which workflows burn tokens.  
**For KP wiki:** Track tokens spent on: document ingest, contradition detection, synthesis, gate passes. Show user "You've spent X tokens on research ingestion, Y on canon reconciliation." Helps budget for downstream Claude API calls.

---

## 4. Reusable Code/Assets

**Important AGPL caveat:** Any code you copy from this repo must be used under AGPL-3.0. This means if you distribute or deploy derived code as a service (web app, Claude skill, etc.), you must open-source it under AGPL-3.0. For private/offline use, AGPL is less restrictive, but vendoring for a deployed service is legally complex. **Best approach: use these as inspiration for your own implementations, don't copy directly.**

**Files safe to rewrite/inspire from:**

| Path | What | Copy or Inspire? | Reason |
|------|------|------------------|--------|
| `tldr/dedup.py` (185 lines) | Content-hash dedup, index storage | **Inspire** | Core logic is straightforward (SHA1 + dict); rewrite in your style for clean AGPL boundary. |
| `tldr/dirty_flag.py` | Dirty-file tracking | **Inspire** | Simple dict + set pattern; rewrite for clarity. |
| `tldr/durability.py` | Durable vs volatile classification | **Copy OK** | Just pattern matching on paths + comments. Low risk. |
| `tldr/patch.py` (lines 1–70) | File hash + edge extraction | **Inspire** | The hash computation and edge dataclass are generic; rewrite without copy. |
| `tldr/stats.py` | Token counting via tiktoken | **Copy OK** | Thin wrapper around tiktoken. Safe if you already use tiktoken. |
| `tldr/incremental_parse.py` | Tree-sitter incremental caching | **Inspire** | Tree-sitter API details change; adapt to your needs rather than copy. |
| `tldr/daemon/core.py` (lines 112–147) | Config precedence logic | **Copy OK** | Generic `.json` loading with try/except. Pattern is clear. |

**Non-copyable (core algorithm):**
- `tldr/hybrid_extractor.py` — Tree-sitter wiring, language dispatch
- `tldr/cfg_extractor.py`, `dfg_extractor.py`, `pdg_extractor.py` — CFG/DFG/PDG analysis (complex AST walking)
- `tldr/cross_file_calls.py` — Call graph construction

**Vendorable under AGPL (but requires disclosure):**
- The semantic indexing pattern (L1–L5 embedding input construction) is documented in docs/TLDR.md and could be adapted.

---

## 5. Not Useful / Caveats

1. **AGPL-3.0 licensing blocks easy vendoring:** If the Kohärenz Protokoll novel system is deployed as a web service or Claude skill distributed to others, AGPL requires opening the source. For private/research-only use, this is less of an issue. For productization, evaluate whether you can/want to open-source under AGPL or if you need a different license.

2. **Designed for code, not prose:** TLDR assumes structured, parseable source code with clear function/class boundaries. Research documents are often narrative prose, mixed code snippets, and unstructured claims. The 5-layer analysis stack doesn't fit well to "Chapter 3: physics fundamentals" with paragraphs and equations. Would need to adapt extraction strategies.

3. **No built-in contradiction detection:** TLDR is a linter/analyzer for static code properties (complexity, calls, data flow). It doesn't detect *semantic* contradictions (e.g., "character X is alive" vs. "character X died in scene 5"). You'd need to add that on top.

4. **Semantic search is expensive on first run:** The `bge-large-en-v1.5` model is 1.3GB. First `tldr warm` downloads it and builds embeddings (~2 min on typical project). Subsequent queries are fast, but cold start is slow.

5. **Daemon is per-project, not multi-project:** Each project gets its own socket/daemon. If you have 680 research papers in one directory and chapters in another, you need separate daemons. The .tldr/cache grows with project size (100s of MB with semantic search enabled).

6. **No built-in versioning/history:** TLDR indexes the current state. It doesn't track how the graph changed over time (e.g., "when did function A start calling B?"). For tracking research-paper versions, you'd layer version control on top.

---

## 6. Verdict

**llm-tldr is a mature, well-engineered tool for extracting lightweight code summaries, not research documents.** Its 5-layer analysis stack, content-hash deduplication, incremental indexing, and semantic embedding patterns are excellent references for building a robust research-document wiki engine. The AGPL license and code-specific design mean you should adapt key concepts (dirty-flag batching, hierarchical layers, durability partitioning, embedding enrichment) into your own Python implementation rather than copy code directly. The daemon pattern with FAISS indexes and configurable thresholds is battle-tested for 300x query speedup; porting that architecture to your wiki (mark canon/research dirty, batch re-synthesis at threshold, embed with multi-layer context) would yield fast, scalable contradiction detection and synthesis. For the Kohärenz Protokoll wiki to ingest 680 research papers without hallucination, study dedup.py, dirty_flag.py, and the semantic indexing pattern; then build your own canon-safe equivalents in your stack.

---

**Report generated:** 2026-09-15  
**Surveyed files:** README.md, pyproject.toml, NOTICE, LICENSE, tldr/__init__.py, tldr/dedup.py, tldr/dirty_flag.py, tldr/durability.py, tldr/patch.py, tldr/session_warm.py, tldr/incremental_parse.py, tldr/daemon/core.py, tldr/cli.py, tldr_code.py, tests/test_typescript_semantic.py, docs/TLDR.md
