# Architecture-session preparation: current baseline

2026-10-01. Read-only engineering review of `main` at
`219a3ee9d3cf77649880c265c171eee949a834e2`, then branch
`codex/strategic-learning-architecture-session`. The initial checkout was clean.
No source ingestion, backfill, model calls or corpus transmission was performed.
The only open PR returned by the repository's open-PR listing was #76,
`Codex/dspy canary validation`; PRs #137 and #138 were already merged.

## Measurements and checks

| Command | Actual result |
|---|---|
| `python3 scripts/knowledge.py init --profile reader` | exit 1: optional qmd installation failed; sources, derivation, graph build/freshness, qmd update/status/coverage and template checks each reported ok. The initializer's overall failure is retained, not relabelled ready |
| `python3 scripts/account.py order --summary` | order holds: 58 documents with a census, 0 violations |
| `python3 scripts/state.py --prose` | 0 prose claims contradict the repository |
| `python3 scripts/sources.py check` | 587 manifest rows; 586 landed/verified, 1 not fetched; no missing files, checksum mismatch or file outside the manifest |
| `python3 scripts/quotes.py` | 21,969 cited quotes checked, 0 unresolved, 0 unchecked; 1,507 count marks checked, 0 wrong; 1,143 absence phrases carry no mark |
| `python3 scripts/selftests.py --only std` | 55 held, 0 failed, 0 not run among selected suites; 16 dependency suites skipped by request; raw output in `standard-library.txt` |
| `python3 scripts/wiki_index.py --check` | exit 0; 0 frontmatter/body drift; reports 80 alias gaps and 10 pages without reading headings as coverage limits |
| `python3 scripts/judgements.py --open` | exit 0; 120 judgements: 8 agree, 0 disagree, 106 still judgement, 6 skipped |
| `python3 scripts/chapters.py` | exit 0; 41 pages, 585 readings, 0 defects |
| `python3 Plan/runs/graph-lab-2026-09-30/eval-audit.py` | exit 0; current counts reproduce the circular-gold and missing discovery-label findings; raw output in `evaluation-audit.txt` |
| `bash -n .claude/hooks/session-start.sh` | pass |
| Real SessionStart hook with temporary fixture initializer | both successful and failed initialization keep the session alive, print the NOW task-routing instruction before initialization, and report the failure when present; environment PATH export retained |

The hook fixture substitutes only `python3` in a temporary PATH, with a temporary
project root and environment file. No production initializer ran in the fixture.
The standard-library suites were run on the base before the documentation and
hook message changed; no runtime pipeline logic changed. The broader dependency
suite and a fresh novelgraph build/benchmark were not run here. Novelgraph
performance claims in the strategic review refer explicitly to the already
committed PR #137 validation, not to a new measurement.

Quote resolution does not verify interpretation. Unmarked absence phrases stay
visible as a coverage limit. The strategic review's proposed gates are not
completed experiments, and the future `SPEC.md` is not claimed to exist yet.
