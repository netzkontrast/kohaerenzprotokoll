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
| `03-candidates-blind-<n>.md` | a blind re-reading, for measuring how far two readings agree — never gold, never the census's list; `scripts/agree.py <slug>` compares it | a Claude subagent that saw only the briefing, 01, 02 and `read.py` |
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
| `sweep.jsonl` | every page the sweep found in a read document's text that its census did not list: a reading or an occurrence, and why (decision 012) | a person; `scripts/reconcile.py --sweep-open` counts what no row settles |
| `baselines.jsonl` | every scored program on every task, append-only | `scripts/baseline.py`, through `pairs.py` and `graphrag.py bench --record` |
| `dedupe.json` | the decision per group of near-identical exports | `scripts/dedupe.py` |
| `bilingual/` | every stage of the German–English mapping, cached so `--replay` needs no key | `scripts/bilingual.py` |
| `jev/` | requests and responses of the Jev entity test, for `--replay` | `scripts/jev_entities.py` |
| `route/` | the consent file of decision 007, the call ledger and the recorded calls | `scripts/route.py` |
| `tooltest/` | outputs of the tool review under decision 007 | the tools under review, through `route.py` |
| `record-audit-2026-09-24/` | every attribution the conflict and question records make to documents 7–13, checked against the lines, the findings and two skeptics' verdicts, and which were written | `.claude/workflows/record-audit.js`; the README's rule decided the writing |
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

**Which lists are gold is decided by `scripts/gold.py`** (decision 009): a
list written while reading, counted, unchanged since its count, and of its
document. 12 <!--state:trainset.gold_candidate_lists--> are gold today,
documents 5 to 14. Documents 5 and 6 say a reader wrote them; from document 7
on, the session reading the document wrote the list before any count, and its
`written_by:` line says so. `python3 scripts/gold.py` prints every verdict and
the criterion a list fails.

**The reader of documents 5 and 6 was a Claude session too** — the commit of
document 5's census speaks of „my own quotations". Every list here, gold or
not, was written by a Claude session, and none by the author — which is why
`gold.py` asks what a list is rather than who wrote it. Four documents were read again blind on 2026-09-24
(`03-candidates-blind-<n>.md`): each blind reader held 97–100 % of the
committed list's content, and the lists differed in how much each chose to
list (`Plan/learnings/extract-terms.md`, *Blind re-readings*).

## Superseded finished artifacts

Pages and censuses that were rewritten live in git, not here. `git log -p
<path>` gives the evolution. Two rewrites worth knowing about:

- `Wiki/candidates/aegis.md` was written from three documents before the
  document-by-document order existed and was rebuilt to document 1's state
- `Sources/terms/entropie-aegis.md` carried forward-looking notes about later
  documents and was rewritten to describe only its own document
