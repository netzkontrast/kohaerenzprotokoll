# `Plan/` — how the work is done, and what it has left behind

<!-- readme-context:start -->
Directory guide. Current work is in NOW.md; CLAUDE.md defines the session
contract. Counts with state markers are checked by `python3 scripts/state.py --prose`.

[Project](../README.md) · [Current work](../NOW.md)
<!-- readme-context:end -->

Nothing here is a source or a wiki page. It is the record of the work on them:
the designs argued before building, the decisions taken, the lessons of each
step, and every artifact a run leaves. `CLAUDE.md` is the working agreement and
`NOW.md` what is open; this page says which folder holds what.

**This page is checked, not remembered.** 0 <!--state:readme.plan_drift-->
folders in `Plan/` are missing from it or listed here without existing, and
`python3 scripts/state.py --prose` fails the day that number is not 0.

| folder | holds | written by |
|---|---|---|
| `Plan/concept/` | designs, one per topic, named `<topic>_<date>.md`, and the readers' reports behind the DSPy toolchain, the `dspy` skill and the tool review | a person, or a session, before or while building |
| `Plan/decisions/` | one file per decision, permanently — its README indexes them | a person |
| `Plan/learnings/` | one file per workflow step: what was learned, with its evidence | whoever ran the step |
| `Plan/runs/` | every artifact of every run: one folder per document, and the ledgers every run appends to | `scripts/capture.py`, the scripts named in its README, and a person |
| `Plan/weichen/` | one decision sheet per Weiche of the writing plan (`Plan/concept/novel-writing-plan_2026-09-29.md`, §5), in German: the question, the positions quoted and cited, costs and gains, a recommendation where the material supports one; nothing in them is decided | a session, for the author |
| `Plan/storyform/` | the novel's two Dramatica storyforms (decision 025): `a.json` and `b.json` are the source of truth, every value with its provenance; `overview.md` and `ncp/` are written from them by `scripts/storyform.py` and never edited | the author's answers, recorded by a session (skill `storyform`); `scripts/storyform.py` |
| `Plan/entities/` | one model's entity list per document, and the German–English map | the `entity-lists` workflow, `scripts/entities.py`, `scripts/bilingual.py` |
| `Plan/briefings/` | task instructions: the next-session architecture mandate, and procedural knowledge for a reader before a document, never another document's content | a person |
| `Plan/rules/` | `exceptions.jsonl`: documents a rule deliberately skips, each with its reason and when to revisit | a person; `scripts/derive.py` reads it |
| `Plan/hyperextract/` | HyperExtract contracts and model-selection configuration; the port in `scripts/hx.py` executes them, staged results remain proposals and decision 019 keeps the backfill stopped | a session; `scripts/templates.py` checks them |
| `Plan/quality/` | the OpenRouter model benchmark of 2026-09-16; the script it names is no longer in `scripts/` | a session, then |
| `Plan/trainsets/` | `surface-pairs.jsonl`, the export `scripts/trainset.py --export` writes; nothing reads it, and it lags the ledger | `scripts/trainset.py` |
| `Plan/fixtures/` | offline fixtures a script consumes and its self-test replays: `aegis/` holds the AEGIS pilot's two manual cases (`Plan/briefings/aegis-agent-pilot.md`), every in-world sentence invented test state, every assumption with an id; nothing in them is canon | a session, by hand; `scripts/aegis.py` reads them |
| `Plan/eval/` | frozen evaluation sets, one versioned file each with the commit it was taken at and a sha256 over its cases; never rewritten, a changed set is the next version (`scripts/benchset.py`) | `scripts/benchset.py freeze` |
| `Plan/derived/` | git-ignored; disposable outputs rebuilt by their owning tools; `python3 scripts/derive.py` rebuilds document-rule views, while graph, serving and app outputs have separate builders | `scripts/derive.py` |

`Plan/state.json` is the last run of `python3 scripts/state.py`: an artifact,
not the source of truth. `python3 scripts/state.py --check` says whether it has
drifted from the repository.

The adopted architecture is [SPEC.md](../SPEC.md) (decision 021); current next
steps are in [NOW.md](../NOW.md). The AEGIS pilot starts at
[its briefing](briefings/aegis-agent-pilot.md) and remains a proposed offline runtime.
The original architecture session starts at `Plan/briefings/architecture-session.md`.
Its dated inputs are `Plan/concept/strategic-learning_2026-10-01.md`,
`Plan/concept/architecture-options_2026-10-01.md` and
`Plan/concept/pr140-architecture-input_2026-10-01.md`; the last distinguishes
the ongoing RLM experiment from an adopted architecture.

## Two conventions that hold across the folders

- **A dated file says what was true on its date.** Where a claim in it turned
  out wrong, the correction stands beside it, with how it went wrong
  (`CLAUDE.md`, *Changing your mind*).
- **A number in prose carries a `<!--state:key-->` marker** where a measurement
  exists (`GOAL.md`, rule 14), so `state.py --prose` catches it going stale.
