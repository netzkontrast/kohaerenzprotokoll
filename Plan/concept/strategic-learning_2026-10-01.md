# Strategic learning: which uncertainty should the project reduce next?

Review of `main` at `219a3ee9`, including the merged PRs #137 and #138.
The author's request of 2026-10-01 is to review strategic learning goals and
refactor the next Claude Code session to self-evaluate and produce the final
project architecture. This is an engineering mandate, not a new canon decision.

## What the repository already establishes

The product goal is evidence-backed help with the novel: locating sources,
preserving incompatible readings, preparing decisions, and eventually building
bounded chapter context (`GOAL.md`). The current product is a source-derived
wiki (`README.md`, `CLAUDE.md`). These are different stages of one project.
An extraction count, a larger graph or an installed package is not product value.

| Finding | Evidence | What it permits us to conclude |
|---|---|---|
| Source identity, quotations and pipeline order are checked against files | `scripts/sources.py`, `quotes.py`, `account.py`; current checks in `Plan/runs/architecture-audit-2026-10-01/README.md` | Mechanical integrity holds for the reported coverage; semantic fidelity needs its own audit |
| Citation validity and interpretation can diverge | `Plan/runs/reader-lab-2026-09-30/README.md`, R2 and R3 | A cheaper reader must pass a claims audit as well as quotation checks |
| Fixed context and repeated tool calls dominate reader cost | Same lab, transcript measurements and clean-reader experiments | Compare minimal readers on the same tasks; do not infer a model ranking from different documents |
| Retrieval gold is predominantly already quoted on wiki pages; none of its gold documents is unread | Replayed `Plan/runs/graph-lab-2026-09-30/eval-audit.py`; output in the current audit run | Current benches support regression comparisons, not a claim of discovery quality |
| Blind relation gold is a different target from a term list or quotation validity | `Plan/runs/gold-2026-09-30/README.md`; `evaluation-audit_2026-09-30.md`, section 5 | Relation correctness, reader agreement and retrieval contribution must be scored separately |
| Graph, proposals and full text share a disposable store | `scripts/askdb.py`, `kg.py`; `Plan/concept/ask-sources_2026-09-30.md` | Consolidate the existing implementation; a second authoritative graph would duplicate facts |
| The chunk index is operational but no pipeline consumer uses it | `novelgraph/src/novelgraph/`, `docs/novelgraph-index.md`; `Plan/runs/novelgraph-pr137-final/` | Speed and incremental correctness justify a candidate backend, not automatic adoption |
| The desired question loop and chapter context are not a completed writing workflow | `GOAL.md`, sections 4.5, 4.7 and 7; `Plan/concept/novel-writing-plan_2026-09-29.md`; `NOW.md` | Their usefulness needs task-level evaluation and the author's unresolved writing decisions |

The replay still finds 1,130 of 1,226 gold lines also quoted by pages, and all
55 gold documents have been read. These are dated measurements, not live state
claims. PR #137's recorded heading hybrid document recall@8 is 0.068; its warm
P95 is 34.2 ms, whereas `docs/novelgraph-index.md` reports a roughly 15-second
cold CLI invocation. None of those measures the quality of a final answer.
Do not compare graph recall, chunk recall and pack recall as though their
units, budgets and eligible evidence were identical.

## Strategic learning goals, in dependency order

Each row asks a question that could change a design choice. Targets below are
proposed gates, not attained results. Choose effect thresholds before the run.

| Priority / learning question | Baseline and experiment | Evidence to report | Architecture decision and stop condition |
|---|---|---|---|
| L1: Can the evaluation detect useful new evidence rather than repeat its inputs? | Keep current benches as regression fixtures; freeze and hash cases; split by shared source clusters; design held-out and document-masked retrieval comparisons | Per-case outcomes, eligible/unjudged evidence, leakage paths, paired differences and uncertainty | No retrieval winner before the evaluation can distinguish regression from discovery; stop tuning on the held-out set |
| L2: What improves evidence found per context budget? | Compare current `ask` routing, FTS/BM25 and optional novelgraph, then graph expansion; identical questions, source snapshot and serialized pack budgets; separate routing from packing | Relevant evidence coverage, first relevant rank, duplicate evidence, conflicts/questions retained, actual bytes/chars and tokens when a tokenizer exists | Add a backend only for a reproducible marginal gain or lower cost at equivalent usefulness; warm and cold latency reported separately |
| L3: What is the least expensive trustworthy reading procedure? | Use existing lab traces first; design a paired comparison of the minimal clean reader and the current reader on already permitted material | Claims audit by defect class, candidate agreement/containment, missing claims, retries, all calls and tokens, wall time; proxy cost labelled as proxy | Select the procedure by quality and total cost, not quote-check success alone; no new document reading while the pause stands |
| L4: Which extracted relations earn their cost? | Separate endpoint detection, pair/type correctness, and added retrieval utility; use existing gold and contract runs; design a second blind relation reading before treating one gold list as truth | Reader agreement, per-contract precision/recall with uncertainty, unverifiable rows, marginal useful evidence per paid call | Keep `P_HE_*` experimental until a held-out downstream gain justifies it; preserve decision 019's STOP and default-off finders |
| L5: Where can DSPy improve an actual decision surface? | Adopt `dspy-learning_2026-09-30.md` as candidates: query routing/rule cards before broad extraction; compare deterministic and unoptimized baselines | Frozen train/dev/test membership, exact prompt/model versions, total call budget, semantic errors and safety vetoes separately from mean score | Compile only a better held-out artifact; no false merge or fabricated evidence traded for average recall; stop at the declared budget |
| L6: Do questions and context packs reduce the author's work? | Design tasks from existing open questions and decision sheets; later compare bounded evidence packs or answers blindly, with author calibration | Answerable/contested/author-only distinctions, novelty, redundant questions, evidence sufficiency, omitted disagreements, decision usefulness | A loop earns continuation by reducing a stated uncertainty; stop on repeated questions, no new supported information or exhausted budget |
| L7: Can the architecture survive a fresh session and input changes? | Existing initializer, graph freshness and novelgraph corruption/interruption fixtures; perturb only temporary copies | Capability-specific readiness, rebuild scope, stable IDs/line resolution, parity, failure/refusal behavior, restart and cold cost | One owner per derivation; missing optional tools must not be reported as product failure or silently treated as present |

Independent relevance labels and author usefulness judgements do not yet exist
in the form the evaluation audit proposes. Masking an already read document
simulates discovery; it does not prove performance on genuinely unread sources.
Question novelty alone is not value. Generated questions and answers remain
proposals, and the author's interpretation stays outside an optimizer's reward.

## Architecture direction to challenge in the next session

The strongest starting hypothesis is a local, file-based system with these
responsibilities. This is a recommendation to test, not an adopted architecture.

| Responsibility | Existing anchor | Recommended boundary |
|---|---|---|
| Authoritative input and decisions | `Sources/`, attributed `Wiki/` readings, decision files | Source bytes immutable; approved interpretations and decisions remain file-backed; derived indexes never author truth |
| Reading and reconciliation | `capture.py`, `census.py`, `readings.py`, `reconcile.py`, `record.py` | Source-local extraction frozen before wiki access; code handles placement/rendering, judgement remains explicit |
| Query projection | `graph.py` → `askdb.py`; `kg.py` | One rebuildable shared graph/FTS store, provenance on every returned edge/evidence item; `Graph/` stays an output atlas |
| Retrieval and context | `graphrag.py`, `ask.py`; optional `novelgraph/` and qmd | Backends find candidates; a common packer verifies source locations, de-duplicates and budgets evidence; no unmeasured default switch |
| Learned proposals | `P_*`, `hx.py`, contract runs, DSPy artifacts | Separate from stated graph facts; versioned models/prompts and recorded consent; no automatic promotion or canon resolution |
| Evaluation and improvement | Existing scorers, run ledgers, invariant suites | Separate integrity, semantic fidelity, discovery, answer usefulness and cost; compare before compiling or adopting |
| Author interaction and future writing | `Plan/weichen/`, questions, chapter readings, snapshot UI | Prepared decisions with evidence; future chapter-context service, contingent on writing choices; research prose never becomes novel prose |

The next session must decide the integration boundary between the lightweight
index and `ask`, ownership of derived chunks and whether `Index/` belongs in
Git, a common result/pack contract, and a minimal dependency/startup surface.
It must also reconcile the target in `GOAL.md` with decisions 006, 015, 018–020:
legacy canon precedence, automatic conflict adjudication and concurrent reader
plans cannot silently override the newer instructions. Explain the resolution
and retain questions only where the choice belongs to the author.

## What happens next

`Plan/briefings/architecture-session.md` is the operative session task. It calls
for an evidence-backed `SPEC.md`, a self-evaluation with reproducible checks,
and an ordered migration. It does not commission another extraction sweep,
an optimizer run or a rewrite of the novel.

The author clarified the starter on 2026-10-01: expand and explain the ideas,
planning and caveats for Claude to continue. The companion
`Plan/concept/architecture-options_2026-10-01.md` develops concrete RLM/DSPy
options, simpler comparators, version/consent limits, experiment gates and the
first contribution on PR #139. These are hypotheses for the next session,
not a claim that a final architecture has already been implemented or adopted.

The author's later pointer to PR #140 is covered in
`Plan/concept/pr140-architecture-input_2026-10-01.md`. Its graph/chunk RLM code
is work to reuse and assess, not a reason to repeat the same experiment.
