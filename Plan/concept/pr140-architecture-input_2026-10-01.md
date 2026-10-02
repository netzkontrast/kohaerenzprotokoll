# PR #140 as an architecture input, not a second RLM project

2026-10-01. The author explicitly pointed the architecture starter to
[PR #140](https://github.com/netzkontrast/kohaerenzprotokoll/pull/140).
This inspection refers to commit `68bbc8e7fb7f7360dd1a209d4ba91964aa193af7`
on `claude/rlm-chunk-optimize`, against main
`219a3ee9d3cf77649880c265c171eee949a834e2`. The PR and its run are still open;
refresh their state before drawing conclusions. No new model call, source
reading or change to that branch was made for this inspection.

## What already exists on that branch

| Work | Concrete owner | Architectural consequence |
|---|---|---|
| Offline action/forced-output loop test | `scripts/rlm_ingest.py --loop-selftest` | Reuse the pinned DSPy fixture; do not claim it tests the real Deno sandbox |
| RLM over the wiki graph | `scripts/rlm_retrieval.py` | Corpus navigation is implemented as an experiment; it is no longer merely a proposal |
| RLM over indexed chunks | `novelgraph/src/novelgraph/rlm.py` | Reuse its search/read tools and trace format when comparing controllers |
| Two provisional size variants | `Index/methods.toml`, `heading200@v1` and `heading800@v1` projections | Their existence is not selection of a new default |
| Serial Claude run with consent label and ledger | `lmrun.make_lm("claude-cli/haiku")`, `lmrun.call`, `Plan/runs/rlm-chunks-2026-10-01/` | Better transmission/accounting boundary than the ingestion runner's direct OpenRouter call |
| Fixed experiment design | Run README: 24 cases × 3 chunkers, paired comparison, 3,200 text-token budget | Preserve the pre-stated design and record limitations separately; do not rewrite it after seeing a winner |

The code wraps a whole RLM invocation in `lmrun.call`; its ledger aggregates the
LM history. This is not the same as intercepting each root, child, adapter retry
and forced-extraction call to enforce a pre-call global allowance. Inspect the
actual model adapter and child-call behavior before asserting a hard limit.

## Snapshot of the checked-in run

There are **13 of 72 planned case/chunker rows**, excluding the separate pilot.
This is a repository snapshot, not a statement about a process currently running
elsewhere. The main results and three ledgers agree on case counts and cost
after rounding. No winner follows from these partial rows.

| Method | Rows | Scored | Forced | Calls recorded in results | Cost, USD |
|---|---:|---:|---:|---:|---:|
| `heading200@v1` | 5 | 5 | 0 | 28 | 0.4589 |
| `heading@v1` | 4 | 3 | 1 | 25 | 0.4695 |
| `heading800@v1` | 4 | 3 | 1 | 24 | 0.4627 |

These costs are recorded estimates for the main results, not a billing statement
or total including the pilot. The run README's Result section is still empty.
The PR describes 74/74 repository selftests; those are the author's branch's
reported checks, not checks independently rerun by this architecture inspection.
The automated graph review also explicitly says its coverage is partial.

## Questions Claude must resolve before generalizing the result

1. **Selected, seen and read are different.** `search_chunks` adds a full chunk
   to `shown` but returns only a 200-character preview. `evaluate` accepts any
   shown ref and credits its entire line range; it does not require a successful
   `read_chunk`. `read_chunk` itself truncates at 4,000 characters, and step output
   is capped at 3,000. Therefore reported line recall is coverage of selected
   chunks, not proof of evidence the agent actually saw or understood. For
   chunk selection this can be a valid metric; for a reading/answer claim it is
   insufficient. Define and retain those distinct metrics in the common pack.
2. **The compared budgets cover different things.** The 3,200 count uses the
   chunker's regex token unit, not the provider tokenizer; it excludes search
   previews, repeated reads, prompts and history. Equal selected-text budgets
   do not establish equal total context, calls, latency or dollars. Document the
   unit and show both budgets; do not relabel regex counts as model usage.
3. **Missing outcomes can change the ranking.** Forced/failed runs are counted
   and excluded from the paired score. Preserve that rule, report pair counts
   and method-specific completion, and add a sensitivity view that counts an
   incomplete attempt as no successfully delivered evidence. Do not silently
   replace the pre-stated primary result. Case-by-case order helps pairing but
   a cost stop can still interrupt the middle of a three-method case.
4. **The threshold is not a transferred power calculation.** The +0.027 in
   `evaluation-audit_2026-09-30.md` comes from the standard error of a particular
   `he-lines` comparison. A new RLM/chunker comparison has different variance,
   dependence and missingness. Keep +0.027 as the run's pre-stated decision
   threshold, but do not call it this run's detectable effect without a new
   uncertainty analysis. Source overlap also limits an independent holdout.
5. **A soft spend stop and resume key are not a reproducibility contract.**
   `run` checks `spent > cost_cap` before the next case, after the previous RLM
   invocation finished. It can overshoot the cap within that invocation. Resume
   skips `(case, method)` without matching source/index hashes, prompt, model,
   limits or code version. Either bind a run to those inputs or start a distinct
   run when they change. Do not edit an active run in place.
6. **A size comparison is not evidence for adopting RLM.** All three treatments
   use RLM. They can inform size selection under that controller, but cannot
   show that RLM beats static retrieval, bounded expansion or a direct pack.
   That requires an additional matched baseline and an author-utility target.
7. **The gates have useful but narrow meanings.** Ref rejection caught invented
   addresses in this snapshot; an accepted ref only establishes a real location
   returned by search. It does not establish semantic support. Claude-only model
   validation is implemented for this runner; a nonempty `approval` argument is
   still a label whose exact decision scope must be checked. The ingestion
   runner remains a separate consent/accounting path.

## How the architecture session should use this

First inspect the latest #140 head, run README and report. If it merged, integrate
its actual owners into the baseline; if it remains open, compare it from an
isolated checkout and preserve its branch. Do not restart its paid run, create
parallel calls, declare a chunk-size winner or duplicate its RLM implementation.

Use E0–E2 from `architecture-options_2026-10-01.md` to map these tools onto one
verified evidence-pack contract. Record the findings above as evaluation limits,
then choose the smallest offline migration. Design E4 as a later comparison of
controllers, distinct from #140's chunk-size study. A final `SPEC.md` can retain
RLM as optional while selecting the existing deterministic path as the supported
default; no additional paid experiment is required to finish the recommendation.

PR #139 is the architecture starter; #140 is implementation/experimental input.
Neither replaces author decisions or the briefing's completion criteria.
