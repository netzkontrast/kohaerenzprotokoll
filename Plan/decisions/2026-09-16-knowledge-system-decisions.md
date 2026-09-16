# Decisions D-W1 … D-W12 — knowledge system (2026-09-16)

Recorded from the author's answers in session
`session_018FqFPzyW6Wj3qK2xnqrquv` on 2026-09-16. The questions are in
[`Plan/wiki/knowledge-system-concept_2026-09-15.md`](../wiki/knowledge-system-concept_2026-09-15.md) §7
and [`Plan/wiki/integration-plan_2026-09-15.md`](../wiki/integration-plan_2026-09-15.md) §5.
D-W2 was assessed with `/tetraframe` first; the run is
[`tetraframe/d-w2-wiki-markdown-vs-graph.json`](tetraframe/d-w2-wiki-markdown-vs-graph.json).

| id | decision | consequence |
|---|---|---|
| D-W1 | Commit all markdown exports under `Sources/drive/` | Phase 2 exports the full corpus into git; citations resolve on any clone; the lint verifies quotes offline |
| D-W2 | Two-axis rule: wiki **pages** are file-only; atomic cited **claims** keep `capture_claim`, sourced from `Sources/` or `Canon/`, never from a `Wiki/` path; `edges.jsonl` is not "the graph" | concept §2 2a, §3.3, §4 E; lint rule `no-page-body-in-graph` on every graph-write payload (Phase 1); audit of the ~220 existing `NovelClaim.source_uri` values (Phase 1); Phase 7's T2-claim writes stay valid |
| D-W6 | Ingest everything: tiers T1–T3, claims extracted, superseded drafts marked `superseded_by`; `T4` dropped (D-W9) | Phase 2/3 batch order unchanged; a superseded draft never raises a question alone |
| D-W9 | Keep Drive ids; drop the 13 appendix (`T4`) rows from the manifest; review titles of personal documents before Phase 2 | `scripts/source_inventory.py` excludes `T4` rows (Phase 1); title review is a checklist item of Phase 2 |
| D-W10 | Three new pack skills | merged as v0.7.0 via dspy-agent-skills#4 |
| D-W11 | Independent reviewer: `claude/haiku` for wiki pages, `claude/sonnet` for the promotion gate | `AdversarialReview` config in `tools/kpwiki/lm.py` roles (Phase 4); reviewer ≠ writer asserted by the skill |
| D-W12 | Canon is **not normative inside the wiki loop** until verified against the populated wiki: every Canon claim starts `unverified`; Canon/research conflicts are open questions with no default winner. Manuscript work keeps Canon normative | `canon_status` gains `unverified` as initial value (concept §3.2); CLAUDE.md working agreement amended; the verification pass is a Phase-4/5 deliverable |

## The D-W2 run, in short

Eight of nine checks passed (branch independence 1.00, divergence 0.93,
rigor of both 0.91 / neither 0.95, contradiction honesty 0.75,
transformation quality 1.00, robustness 0.86, slop 0.82). **Fake-novelty
risk failed at 0.44**: P* coined "page-shaped", "claim-shaped" and "relation
ledger", terms no corner used. The decision therefore cites the corners and
the cartography, and restates P* in their vocabulary (the wording in concept
§2 2a); the P* text in the artefact is not quoted as the rule.

What the run established that the seed had not: the provenance graph was
never canon-only (about 220 `NovelClaim` nodes exist and Phase 7 plans more);
"the graph" named two structures; "research in the graph" named two acts.
The two-axis rule keeps P at full strength for pages and not-P at full
strength for claims, which is why it is not a compromise.

Run facts: `claude/sonnet` via the CLI backend, 20 min, no corner retries,
per-stage checkpoints; the first attempt on `claude/opus` had exceeded the
300 s per-call timeout at the cartography stage (fixed: `KP_LM_CLI_TIMEOUT`,
default now 1800 s, and checkpoints).
