# Next Claude Code session: self-evaluation and final project architecture

Mandate from the author, 2026-10-01. Start here when `NOW.md` names this task.
Produce one concrete recommended target architecture for the project, grounded
in what the repository has learned. Do not end with another catalogue of tools
or leave reversible engineering choices to the author.

The initializer prepares capabilities; it does not choose the session task.
Read `NOW.md`, `PRINCIPLES.md`, `GOAL.md` and the relevant parts of `CLAUDE.md`,
then `Plan/concept/strategic-learning_2026-10-01.md`. That review is a dated
starting point: reconcile it with the branch and current `main` before using it.

## Scope and authority

Use the standing instructions and decision files as the constraints. Design
and local offline checks are authorized. This mandate does not lift the reading
pause, restart the HyperExtract backfill, authorize a new corpus transmission,
or decide canon and novel-writing choices. Do not infer spend approval from a
desire for architecture. Existing consent is consulted for its exact scope.
Any authorized model experiment is serial and records every call and failure.

Work on a branch. Inspect open PRs for overlapping architecture work and reuse
merged work, especially the shared GraphQLite store and novelgraph. Preserve
uncommitted work. When the author merges the session's branch, merge updated
`origin/main` into it as instructed in `NOW.md`; do not reset or rebase it.

## A. Establish the actual baseline

Record commit SHA, branch, dirty state and available capabilities in
`Plan/runs/architecture-session-<date>/README.md`. Inspect the SessionStart log;
do not repeat a successful initialization just to obtain another green light.
If it did not run, use `scripts/knowledge.py init` as the coordinating session.
Missing optional capabilities are named, with their affected checks; they do
not prevent design work using the available tools.

Run the existing applicable checks, retain their outputs and exit codes, and
report each separately. In particular:

```bash
python3 scripts/account.py order --summary
python3 scripts/state.py --prose
python3 scripts/sources.py check
python3 scripts/quotes.py
python3 scripts/selftests.py --only std
python3 Plan/runs/graph-lab-2026-09-30/eval-audit.py
```

Use `.github/workflows/checks.yml` and the `tools` skill for the remaining
invariants. Graph parity/freshness and novelgraph fixtures run only with their
dependencies present; `not run` is not a pass. Keep corpus mutations, temporary
failure fixtures and benchmark builds in isolated copies when necessary.

Read the current decision index, the evaluation audit, DSPy learning proposal,
reader lab, gold relations and latest novelgraph validation. Inspect the actual
call sites and consumers before declaring a tool integrated. `GOAL.md` also
references `netzkontrast/agency/Plan/010-novel-domain/spec.md`: retrieve it if
accessible; otherwise name the access gap and proceed from the local evidence.
No new corpus reading is required for this architecture session.

## B. Evaluate the system's own work, not its self-description

Write the self-evaluation in the run README before choosing the architecture.
For each claimed improvement, identify the problem, implementation, measured
result, counterexample, coverage limit and consequence for the design. Classify
it as established behavior, supported inference, provisional construct or
unmeasured claim. An unknown or uncheckable result stays visible.

At minimum evaluate these competing claims:

- Green quotation and schema checks imply semantic fidelity: confront this
  with the reader lab's subject/voice/absence errors.
- More gold or graph edges improve retrieval: confront this with benchmark
  circularity, source overlap and decision 019's null marginal gain.
- Faster warm retrieval makes the CLI cheap: include model loading, cold
  startup, initialization, rebuild and packing, not only in-process search.
- A second blind reader provides truth: separate procedural independence,
  model-family dependence, reader agreement and author calibration.
- DSPy should optimize everything: identify an actual tunable surface, a
  fallible metric, a held-out set and a finite budget before recommending it.
- A novel-context tool can operate already: inspect missing writing decisions,
  spoilers/reader knowledge, and the difference between research and canon.

Challenge the session's own recommendation: give the strongest counterexample
and explain what observation would change it. This review can be done in the
coordinating session; do not create parallel model calls for a second opinion.

## C. Write `SPEC.md`: a complete recommended architecture

Do not copy the proposed directory tree from `GOAL.md` beside the existing
system. Choose boundaries around demonstrated responsibilities. Use a compact
diagram where topology matters, and tables for exact contracts and decisions.
Clearly distinguish implemented behavior, proposed migration and author-only
choices. A target design may be complete while its usefulness is still unmeasured.

The specification must contain:

1. **Purpose and workflows.** Evidence lookup, source-local reading and
   reconciliation, disagreements and prepared author decisions; future
   chapter-context and writing support with their unmet prerequisites.
2. **Authority and persistence.** Which files own source facts, readings,
   judgements and author approvals; which indexes are disposable; no circular
   derivation from answers into gold or model proposals into canonical facts.
3. **Modules and ownership.** A responsibility and actual current path per
   module; inputs, outputs, consumers, dependency direction and the smallest
   needed runtime. Resolve graph/store ownership and overlapping retrieval
   tools; explicitly choose what is retained, optional, consolidated or retired.
4. **Data and query contracts.** Concrete existing examples of source identity,
   source hash/revision, line ranges, evidence, typed relations and proposal
   provenance. Define a shared retrieval-hit and serialized context-pack
   contract, status/error states, de-duplication and ordering, disagreement
   metadata, budget unit and tokenizer policy. Mark new fields as proposals;
   do not invent a claim schema without instances.
5. **Update and restart behavior.** Full versus incremental rebuilds, the
   invalidation keys, deletions/title/code/model changes, stable identities,
   concurrency ownership, publication/interruption and stale-read refusal.
   Decide how `Index/`, vectors and the `Graph/` atlas are persisted or rebuilt.
6. **Learning and evaluation.** Turn L1–L7 from the strategic review into
   architectural gates. Separate regression, discovery, extraction, semantic
   fidelity, answer utility and cost. Specify frozen datasets, source-level
   leakage controls, paired comparisons, holdouts, baselines, veto errors,
   budgets, stop rules and what cannot be concluded without author labels.
   If source overlap prevents a clean holdout, report that rather than treating
   a random case split as independent. Generated `M-ask` answers must not become
   independent source evidence or gold for the system that generated them.
7. **Model and judgement boundaries.** What deterministic code decides, what
   models may propose, where the author decides; consent and call accounting.
   Question-generation stops on repeated questions, no new evidence, exhausted
   budget or an author-only decision; it never silently resolves disagreement.
8. **Architectural choices.** Recommend one coherent design. Compare it with
   the current system unchanged and at least one meaningful alternative.
   Each consequential choice names evidence, cost, rejected alternative and
   the observation that would reverse it. Reconcile relevant `GOAL.md` targets
   with newer decisions rather than treating older proposals as approval.
9. **Ordered migration and acceptance.** Small independently reviewable steps,
   exact touched paths, dependencies, offline fixtures, parity checks and
   rollback. Put evaluation repair before backend adoption or optimization.
   Do not migrate the entire runtime merely to make the diagram true.

## D. Completion means a reviewable decision, not an infinite study

Finish the engineering recommendation in this session. Where evidence is
insufficient, choose the smallest reversible default, name its limits and the
test that would change it. Distinguish those choices from author-only questions
about novel content, writing roles, paid runs or permissions; those go to
`Plan/questions-for-the-author.md`, with consequences, and do not block the spec.

Completion requires the self-evaluation and actual check outputs in the run
folder, the full `SPEC.md` with contracts/alternatives/migration, and a branch
with small commits and a PR. Re-run checks appropriate to actual changes and
fix regressions. The final report names the recommended architecture, what
was verified, what remains unmeasured and the first migration step.

Remove the active mandate from `NOW.md` only when these deliverables exist and
meet the criteria above; link the spec and any immediate unfinished migration
instead. A file's existence alone is not completion. Keep this briefing and its
dated review as task history. Do not create an adopted architecture decision
on behalf of the author: `SPEC.md` is the final session recommendation until
the author approves it.
