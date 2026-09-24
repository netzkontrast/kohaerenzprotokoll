# `Plan/` — how the work is done, and what it has left behind

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
| `Plan/entities/` | one model's entity list per document, and the German–English map | the `entity-lists` workflow, `scripts/entities.py`, `scripts/bilingual.py` |
| `Plan/briefings/` | what a reader reads before a document: procedural knowledge, never another document's content | a person |
| `Plan/rules/` | `exceptions.jsonl`: documents a rule deliberately skips, each with its reason and when to revisit | a person; `scripts/derive.py` reads it |
| `Plan/hyperextract/` | four Hyper-Extract templates, provisional; the tool review's attempt to run one could not load it (`Plan/concept/tool-review_2026-09-24/hyperextract.md`) | a session; `scripts/templates.py` checks them |
| `Plan/quality/` | the OpenRouter model benchmark of 2026-09-16; the script it names is no longer in `scripts/` | a session, then |
| `Plan/trainsets/` | `surface-pairs.jsonl`, the export `scripts/trainset.py --export` writes; nothing reads it, and it lags the ledger | `scripts/trainset.py` |
| `Plan/derived/` | git-ignored; absent in a fresh clone until `python3 scripts/derive.py` rebuilds it, in about 3s | `scripts/derive.py` |

`Plan/state.json` is the last run of `python3 scripts/state.py`: an artifact,
not the source of truth. `python3 scripts/state.py --check` says whether it has
drifted from the repository.

## Two conventions that hold across the folders

- **A dated file says what was true on its date.** Where a claim in it turned
  out wrong, the correction stands beside it, with how it went wrong
  (`CLAUDE.md`, *Changing your mind*).
- **A number in prose carries a `<!--state:key-->` marker** where a measurement
  exists (`GOAL.md`, rule 14), so `state.py --prose` catches it going stale.
