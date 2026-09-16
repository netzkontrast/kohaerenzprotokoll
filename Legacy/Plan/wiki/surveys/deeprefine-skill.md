# DeepRefine-Skill Repository Report

## 1. What It Is

DeepRefine-Skill is a Python 3.10+ CLI and multi-agent adapter that refines structured knowledge graphs through iterative LLM-guided refinement loops. It plugs into Cursor, GitHub Copilot CLI, Gemini CLI, Codex, OpenCode, and Claude Code with a single `/deeprefine` command. The core algorithm (autorefiner.DeepRefine) detects unanswerable queries against a knowledge graph, applies k-hop retrieval expansion, conducts error abduction (incompleteness/incorrectness/redundancy analysis), generates graph refinement actions, and validates them before applying. Stack: Python, OpenAI-compatible LLM APIs, Graphify (json graph format), NetworkX. Maturity: Beta v0.2.0 (PyPI, actively maintained).

---

## 2. Architecture: The "Deep Refine" Loop

The refinement loop operates in five phases per query:

### Phase 1: Judgment (Answerability Check)
- Runs LLM judgment: "Is this query answerable with the current KG context?"
- Input: query + retrieved subgraph triples (k-hop, initial top_k=5–10)
- Output: `<judge>Yes/No</judge>` tag (parsed in `agent_loop.py::parse_judge()`)
- If answerable → **early exit** (no refinement needed)
- If not answerable → proceed to Phase 2

### Phase 2: Iterative Expansion (Multi-hop Retrieval)
- Expands search with incremented k-hops (1→4 by default) via retrieval methods:
  - Step 1: `graphify_query`, `graphify_query+graph_read`, `wiki_search`, `wiki_search+k_hop_expansion`
  - Step 2+: above plus `k_hop_expansion`, `link_traversal` (wiki variants)
- Validates per step: triple count bounds, required fields (subject/relation/object)
- Each step re-judges; stops on `answerable=True` or max_hops reached
- Captured in `interaction_history` (list of `RetrievalStepResult`)
- **Stopping criteria** (refine_runner.py, agent_loop.py):
  - Early exit: `len(interaction_history) ≤ 1` (single hop answered)
  - Refinement path: `len(interaction_history) > 1` (multiple hops failed → error abduction required)

### Phase 3: Error Abduction
- LLM analyzes why the query remained unanswerable across all hops
- Prompt: `REAFINER_ERROR_ABDUCTION_SYSTEM` + interaction history
- Output: `<abduction>...</abduction>` reason block (INCOMPLETENESS, INCORRECTNESS, REDUNDANCY perspectives)
- Captured in trace as `error_abduction_raw` and `error_abduction_reason`
- Mandatory when refinement path is taken

### Phase 4: Refinement Action Generation
- LLM generates 1–10 graph mutations to address the abduction findings
- Three action types: `insert_edge(subj, rel, obj)`, `delete_edge(subj, rel, obj)`, `replace_node(old, new)`
- Prompt: `REAFINER_KG_REFINEMENT_ACTION_SYSTEM` (agent_prompts.py)
- Output: `<refinement>action1|action2|...</refinement>` pipe-delimited list
- Parsed by `agent_graph.py::parse_refinement_block()`

### Phase 5: Evidence-Aware Review & Safe Apply
- **Evidence scoring** (action_review.py::review_action()):
  - **HIGH**: Exact edge exists, direct code evidence (regex match in files), direct wiki evidence ([[link]])
  - **MEDIUM**: Both endpoint nodes exist but relation inferred by refinement loop
  - **LOW**: Ambiguous node names (bare `main()`, `run()`, etc.), cross-community, unqualified
  - Ambiguous labels flagged in `AMBIGUOUS_LABELS` set (action_review.py:12–35)
- Review stops dry-run; user must approve before apply
- Apply guarded: LOW-confidence actions refused by default; requires `--allow-low-confidence` + explicit user risk acceptance
- On apply: graph mutations applied (agent_graph.py), checkpoint created, wiki regenerated if `--refresh-wiki`

### Persistence & Checkpointing
- Per-run backup: `graph.json.bak.<seq>` (pre-state before first refinement in batch)
- Post-state checkpoint: `checkpoints/graph.checkpoint.<seq>.json` (after each query's refinements)
- Checkpoint timeline: `checkpoints.json` (registry)
- Per-query trace: `loop_trace_<query_id>.json` (JSON schema v1, full interaction history + abduction + refinement)
- Refined history marked: `history.jsonl` (per-query `refined=true` flag)

---

## 3. Concepts Worth Stealing

### 3.1. **Multi-Hop Judgment Loop**
**What**: Iterative retrieval expansion with per-step answerability judgment (phases 1–2 above).  
**Why for Kohärenz**: Canon contradictions often emerge only when multiple concepts are integrated. A multi-hop loop that repeatedly asks "is this answerable yet?" will flush out missing causal chains (e.g., character motivation → plot consequence → thematic payoff). Each hop can surface canon gaps.  
**Files**: `refine_runner.py::run_refine()` (lines 98–230), `agent_loop.py::default_trace()` (lines 43–62), `agent_prompts.py::REAFINER_JUDGEMENT_*` (lines 3–15).

### 3.2. **Three-Dimensional Error Abduction**
**What**: LLM analysis of failure along three axes: incompleteness (missing info), incorrectness (contradictory info), redundancy (bloat confusing retrieval). Frames refinement as causal reasoning, not just "add missing edges."  
**Why for Kohärenz**: Canon errors fall into these buckets: missing character motivations (incompleteness), contradictory timeline facts (incorrectness), overstated thematic motifs (redundancy). Abduction makes refinement intentional.  
**Files**: `agent_prompts.py::REAFINER_ERROR_ABDUCTION_SYSTEM` (lines 17–23), `refine_runner.py` refinement call (lines 169–170).

### 3.3. **Evidence-Grounded Action Confidence Scoring**
**What**: Actions labeled HIGH/MEDIUM/LOW based on verifiable code/graph/wiki evidence (file regex, edge existence, wikilink presence). Ambiguous bare names (`main()`, `run()`) are flagged automatically.  
**Why for Kohärenz**: Prevents phantom canon facts (e.g., "Juna learns X at timestamp Y" without actual scene evidence). Confidence scores make review human-readable and slow down application of speculative canon.  
**Files**: `action_review.py::review_action()` (lines 263–366), `AMBIGUOUS_LABELS` set (lines 12–35), evidence functions `_has_code_evidence()`, `_has_wiki_evidence()` (lines 168–227).

### 3.4. **Dry-Run-First with Explicit Approval Gates**
**What**: Default workflow stops after review, showing HIGH/MEDIUM/LOW actions; apply happens only on explicit user approval in the **same message**. LOW-confidence actions blocked unless user acknowledges risk.  
**Why for Kohärenz**: Prevents silent canon drift. A session can explore "what if we added X?" without committing. Approval is atomic per query (one message = one apply decision).  
**Files**: `claude_skill/SKILL.md` (lines 52–82), `refine_runner.py::_persist()` guard (lines 142–143), `deeprefine apply --allow-low-confidence` CLI (README.md:185–186).

### 3.5. **Trace Schema as Provenance Record**
**What**: `loop_trace_<query_id>.json` is a complete audit log: query, all retrieval steps (num_hops, subgraph, judgement), abduction reason, refinement actions raw, checkpoint refs. Schema version 1 enforced by validation in `agent_loop.py::validate_trace()`.  
**Why for Kohärenz**: Every canon refinement is tied to a query trace. If a refinement seems wrong later, the trace explains the reasoning chain (which query → which hops revealed the gap → what was abduced → why that action was chosen).  
**Files**: `agent_loop.py::default_trace()`, `agent_loop.py::validate_trace()` (lines 121–229), `refine_runner.py` trace save (lines 170–171).

### 3.6. **Qualified Label Matching with Ambiguity Detection**
**What**: Node references can be bare (`"Juna"`) or qualified (`"characters.md::Juna"`) to disambiguate across wikis. Matching is case-insensitive, alias-aware, and source-aware. Cross-references check file path suffixes.  
**Why for Kohärenz**: Allows canon to reference "Juna" from multiple source documents without collision. Refinement suggestions automatically qualify ambiguous names: if `main()` matches 3 functions, suggest `pretraining/training.py::main()`.  
**Files**: `action_review.py::_split_qualified_label()` (lines 71–75), `action_review.py::_matching_nodes()` (lines 89–97), `agent_graph.py::_find_node_id_by_label()` (lines 35–47).

### 3.7. **Staged Wiki Refresh with Rollback**
**What**: When `--refresh-wiki` is used, graph is staged to a temp dir, wiki export runs on staging, validation checks wiki/index.md consistency, then production graph and wiki are **atomically replaced**. If export fails, production is untouched.  
**Why for Kohärenz**: Prevents partial wiki updates (graph refined but wiki stale). Rollback safety means a bad refinement doesn't corrupt the published wiki.  
**Files**: `wiki_refresh.py::apply_refinement_with_wiki_refresh()` (imported in refine_runner.py:13), `tests/test_wiki_refresh.py` (full rollback test coverage).

### 3.8. **Skill Adapter Pattern (Multi-Platform)**
**What**: Deeprefine-Skill ships separate SKILL.md + reference files for Claude Code, Copilot CLI, Codex, Gemini, OpenCode. Each adapter enforces platform-specific safety (e.g., Claude Code must stop before apply; Copilot detects keywords like "approve" to trigger apply). Installers (`deeprefine claude install`, etc.) copy platform-specific files to project or user skill dirs.  
**Why for Kohärenz**: You can invoke `/deeprefine` the same way in Claude Code, Cursor, and Copilot—same rules, different UX. Skill discovery is automatic; no manual command routing needed.  
**Files**: `deeprefine_skill/claude_skill/SKILL.md`, `deeprefine_skill/SKILL_COPILOT.md`, `deeprefine_skill/codex_skill/SKILL.md`, `deeprefine_skill/commands/opencode/deeprefine.md`, installer logic in `installers.py`.

### 3.9. **History Queue Management with Deduplication**
**What**: `history.jsonl` stores one entry per unique query (deduplicated by `query_id(query)` hash). `pending_queries()` filters for `refined != true`. Syncing from graphify memory is idempotent: `sync-memory` imports `graphify-out/memory/query_*.md` and appends only new queries.  
**Why for Kohärenz**: Running `/deeprefine` multiple times doesn't refine the same query twice. You can run queries via wiki search, mark them for refinement, then batch-refine all pending in one session.  
**Files**: `history.py::query_id()`, `history.py::pending_queries()`, `history.py::mark_refined()`, README.md "queue behavior" (lines 97–112).

### 3.10. **Convergence Stopping Criterion**
**What**: Loop stops when `len(interaction_history) <= 1` OR `max_hops` reached OR any step judges `answerable=True`. No infinite loops; trace validation enforces that last step is terminal.  
**Why for Kohärenz**: Prevents runaway refinement. If a query remains unanswerable after 4 hops, the abduction captures why (e.g., "character motivation not encoded in any source"). You can then decide: add it as new canon, or accept the gap.  
**Files**: `agent_loop.py::reafiner_early_exit()` (lines 91–93), `agent_loop.py::validate_trace()` check at lines 183–186.

---

## 4. Reusable Code/Assets

| File/Module | Purpose | Dependencies | Portability |
|---|---|---|---|
| `action_review.py` | Evidence scoring (HIGH/MEDIUM/LOW) + ambiguity detection | `networkx` (via graphify graph format) | High — can be ported to any graph tool; parameterize `project_root` |
| `agent_loop.py::validate_trace()` | Trace schema enforcement + control-flow validation | None | Very high — pure JSON schema validation |
| `agent_prompts.py` | Judgment, abduction, refinement prompts (verbatim from autorefiner) | None | High — prompt strings are framework-agnostic; just fill template vars |
| `agent_graph.py::_find_node_id_by_label()` + `_parse_action_string()` | Node lookup + action parsing | None | Very high — pure string/dict logic |
| `history.py::query_id()` | Query deduplication by hash | None | Very high — one-liner |
| `paths.py::create_checkpoint()` | Checkpoint management (backup naming, metadata registry) | None | High — logic is file-system generic |
| `CLI installer logic` (`installers.py`) | Copy bundled skill files to platform-specific directories | `pathlib` | Medium — platform paths hardcoded; can be abstracted |

**Most portable for novel use**:
- `action_review.py::review_action()` — copy directly, adapt `_node_source()` to your canon node format
- `agent_prompts.py` — copy as-is, reuse in any LLM refinement pipeline
- `agent_loop.py::validate_trace()` — use to validate your own traces if you adopt the schema

---

## 5. Not Useful / Caveats

1. **Graphify Dependency**: DeepRefine-Skill assumes knowledge graphs are in Graphify format (json with `nodes`, `links`, directed/multigraph flags). Porting to RDF, Neo4j, or other KG formats requires rewriting graph I/O (`adapter_graphify.py`).

2. **OpenAI-Compatible LLM Requirement**: The system calls judge/abduction/refinement via OpenAI-compatible APIs. If you use a different LLM service (Anthropic, Replicate), you'd need to adapt `refine_runner.py::make_clients()` (lines 77–95). **Note**: The project doesn't vendor the DeepRefine algorithm itself (`autorefiner.DeepRefine`); it's an external dependency. You must install it separately or run the algorithm elsewhere.

3. **Wiki Export Assumption**: `--refresh-wiki` mode assumes you have `graphify export wiki` command available (from Graphify CLI). Without it, you can still refine the graph, but wiki regeneration won't work.

4. **No DSPy Integration Yet**: Although the system is designed to be composable with DSPy (per the task context), there's no native DSPy module here. You'd need to wrap the refinement loop as a DSPy Signature/ChainOfThought.

5. **Evaluation Incomplete**: `eval/benchmarks/refinement_recall.py` is a skeleton—the LLM refinement loop itself is not implemented in the eval harness. Smoke tests exist, but no end-to-end benchmark yet.

---

## 6. Verdict

**DeepRefine-Skill is a strong template for the Kohärenz canon refinement process.** Specifically:

- **Import the evidence-scoring and trace-validation logic** (`action_review.py`, `agent_loop.py`) to prevent hallucinated canon facts and enforce audit trails. The HIGH/MEDIUM/LOW confidence model is perfect for "did we actually see this in a source, or is it inferred?"
- **Adopt the multi-hop judgment + abduction loop** as your canon-gap detection process. Every time a query fails to answer (e.g., "how does character X's flaw drive the climax?"), your system will surface the causal chain and propose fixes.
- **Use the trace schema** for provenance: every canon refinement is tied to a query that exposed the gap, the retrieval steps, and the LLM reasoning. This is essential for a novel where canon is contested.
- **Port the skill adapter pattern** to your DSPy workflow: same refinement logic, different entry points (Claude Code, CLI, research agent).
- **Do not try to reuse Graphify integration directly**—Kohärenz canon lives in markdown + agency graph, not Graphify. But the refinement algorithm is graph-agnostic; you can adapt it to your graph format.

**Primary reusable components**: evidence scorer, trace validator, prompt templates, multi-hop loop skeleton, approval-gate pattern. **Skip**: Graphify-specific I/O, full DeepRefine algorithm (run externally or wrap differently in DSPy).
