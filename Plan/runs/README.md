# Runs — every artifact of every extraction

A census is the *output* of six steps. Five of them used to run in a terminal and
vanish, which made the process impossible to study: you could not tell how a
census was arrived at, could not compare a model against a person, and could not
see what a probe would have caught.

One directory per document, and beside them the ledgers every run appends to.

## Per document: `Plan/runs/<slug>/`

| file | what | who |
|---|---|---|
| `01-profile.txt` | structural facts | `scripts/capture.py` |
| `02-probes.txt` | export damage, inflection families, substring pairs | `scripts/capture.py` |
| **`03-candidates.md`** | **written while reading, before any counting** — its `written_by:` line says who | **a reader** |
| `04-counts.txt` | occurrences of everything in 03 | `scripts/capture.py --count` |
| `05-verify.txt` | every number that went into prose, re-checked | a person, with commands |
| `run.md` | timings, and what is missing | a person |
| `probes.json`, `counts.json` | the same steps, machine-readable (`CONVENTIONS.md`) | `scripts/capture.py` |
| `reconcile-pre.json` | the candidates classified against the wiki by lookup, before judgement | `scripts/reconcile.py` |
| `reconcile.json` | the reconciliation: the wiki's state before and after, and what was added | a person; `scripts/account.py order` reads it |

Two files appear only after a real model run, and none has happened yet:
`03-candidates-rlm.md` (`scripts/rlm_ingest.py` — never `03-candidates.md`, so a
model's list can never become gold) and `lm/<step>.jsonl` under a subject
folder (`scripts/lmrun.py`, one line per call).

## Beside them: the ledgers and the caches

| path | what | written by |
|---|---|---|
| `judgements.jsonl` | every judgement about a near match, with its rule; `judgements.md` is its rendering | a person; `scripts/judgements.py` replays and renders |
| `baselines.jsonl` | every scored program on every task, append-only | `scripts/baseline.py`, through `pairs.py` and `graphrag.py bench --record` |
| `dedupe.json` | the decision per group of near-identical exports | `scripts/dedupe.py` |
| `bilingual/` | every stage of the German–English mapping, cached so `--replay` needs no key | `scripts/bilingual.py` |
| `jev/` | requests and responses of the Jev entity test, for `--replay` | `scripts/jev_entities.py` |
| `route/` | the consent file of decision 007, the call ledger and the recorded calls | `scripts/route.py` |
| `tooltest/` | outputs of the tool review under decision 007 | the tools under review, through `route.py` |
| `CONVENTIONS.md` | what every run's JSON must carry | a person |

## Why `03` matters more than the rest

It is the only artifact a program cannot produce, and it is the **baseline**: what
a reader proposed before a count could bias them. Everything downstream is
derived from it, and a model scored on this step is scored against it.

Counting before proposing decides what gets seen — roughly half the special cases
found so far are invisible to a regex — so `--count` refuses to run without it.

## What is lost, and it is the first four documents

The four documents processed before this directory existed have **no original
`03`.** It was never written down. Their `03-candidates.md` is **reconstructed
from the finished census** and is marked as such in the file: a census is written
after counting and after judgement, so the reconstruction already reflects both
and **cannot be used as a baseline for scoring anything.**

`01`, `02` and `04` are deterministic and were re-run, so those are genuine.

That is the cost of not having kept them, stated plainly rather than papered
over: **the first four documents cannot serve as a model gold set for the
extraction step**, which is exactly what three hand-read documents were supposed
to be for.

Documents 5 and 6 are the first with a list a reader wrote while reading, and
they are what `scripts/state.py` counts as gold:
2 <!--state:trainset.gold_candidate_lists--> lists. From document 7 on, the list
was written by the session doing the reading, before any count, and its
`written_by:` line says so; it is not counted as gold.

## Superseded finished artifacts

Pages and censuses that were rewritten live in git, not here. `git log -p
<path>` gives the evolution. Two rewrites worth knowing about:

- `Wiki/candidates/aegis.md` was written from three documents before the
  document-by-document order existed and was rebuilt to document 1's state
- `Sources/terms/entropie-aegis.md` carried forward-looking notes about later
  documents and was rewritten to describe only its own document
