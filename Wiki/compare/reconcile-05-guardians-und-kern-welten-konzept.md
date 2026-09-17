---
step: reconcile
census: Sources/terms/guardians-und-kern-welten-konzept.md
note: Sources/notes/guardians-und-kern-welten-konzept.md
machine_record: Plan/runs/guardians-und-kern-welten-konzept/reconcile.json
state_before: 32 pages, 3 conflicts
state_after: 46 pages, 4 conflicts
reconciled: "2026-09-17"
supersedes: Wiki/compare/reconcile-04-guardians-und-kern-welten-konzept.md
new_terms: 14
new_readings: 4
new_surfaces: 3
new_conflicts: 1
judgements: J14–J19
---

# Reconcile — `guardians-und-kern-welten-konzept` against 32 pages

**This replaces `reconcile-04`, which compared against 14.** That run used the
state document 1 left, while document 3 had already taken the wiki to 32. Nothing
enforced the order, so nothing noticed. `scripts/account.py order` does now.

## What the pre-classification decided, and what it could not

```
22 candidates
 → 3 surface groups folded to one term first  (the definite-article rule)
19 candidates — 15 decided by lookup, 4 to judgement
```

**Three pages were saved by a bug fix made during this run.** `reconcile.py`
reported `Die Konstrukt-Stadt` and `Konstrukt-Stadt` as two separate new terms,
and the same for `Grenzfeste` and `Resonanz-Landschaft` — six new_term rows for
three worlds. Its intra-list check read `a != b and (a in b or b in a)`, so
exact fold-equality, which is the article rule's entire purpose, fell through
both branches. The docstring named that exact pair as its example.

`fold()` was correct the whole time. The caller excluded it.

## New terms — fourteen pages

| pages | why |
|---|---|
| `logos` `mnemosyne` `cerberus` `kairos` `sophia` | five Guardians, nine fields each, single source |
| `konstrukt-stadt` `resonanz-landschaft` `grenzfeste` `moeglichkeits-garten` | four worlds, eight fields each, one Guardian each |
| `partnerin` | 30 occurrences, no name; the presence every Guardian is blind to |
| `nexus` · `ueberraum` | **two pages on purpose** — see J18 below |
| `kohaerenz-programm` | the system, as this document names it |
| `personas` | the consciousness instances, glossed once in a parenthesis |

## New readings — four

| page | what changed |
|---|---|
| `guardians` | a role in a subordinate clause → five named bearers, and the blind spot made structural ^[L137] |
| `kern-welten` | zero readings across two documents → four named worlds with their own physics |
| `risse` | one mechanism → four manifestations, each a world's own principle turned against itself |
| `blinder-fleck` | a second bearer, typed three ways by the document itself ^[L117] |

## Judgements — six

| id | pair | decision |
|---|---|---|
| J14 | `Der Möglichkeits-Garten / Nexus-Vorstufe` / `Möglichkeits-Garten` | one term — a slash in a heading is an alias |
| J15 | `Nexus-Vorstufe` / `Nexus` | two terms — a precursor is not the thing |
| J16 | `Kohärenz-Programm` / `Kohärenz` | two terms — a compound is its own token |
| J17 | `Das Seelen-Kohärenz-Protokoll` / `Kohärenz` | two terms — and the first is the novel's title, not a term of the fiction |
| J18 | `Nexus` / `Überraum` | **open** — kept apart |
| J19 | `Die Konstrukt-Stadt` / `Konstrukt-Stadt` | one term — the article rule, firing for the first time |

### J18 is the one worth reading

Five Guardian fields are named `Repräsentation im Nexus`. **All five filled
instances open `Im Überraum…`.** Eleven occurrences against five, in the same
sentences, and the document never says they are one space.

That is regular enough to be evidence and it is not a statement. Merging on
positional regularity is how a wiki acquires a claim no source made, so the two
stay separate and cross-referenced.

## New conflict — C4, and it names its own successor

`blinder-fleck` now has two bearers: AEGIS (document 3) and each Guardian (this
one). **`AEGIS` occurs zero times here**, in 5,839 words about the system it is
elsewhere said to run.

A corpus-wide search finds a passage that appears to settle it — „Modelliert den
Guardian als funktionale Komponente innerhalb der AEGIS-Architektur" — in
`aegis-subplots-kapitelweise-system-exploration-docx`, which has **no census, no note
and no reconciliation.**

It is quoted in `Wiki/conflicts/c4-guardians-and-aegis.md` as evidence about
what to do next and added to no page. Ingesting a fifth document out of order is
exactly what the per-document pipeline exists to prevent.

**So C4 is the first conflict that chooses the next document instead of waiting
for category order to reach one.**

## What the census could not have seen

The document carries one `(laut User Query: …)` marker ^[L117] — the same
convention that was document 3's headline finding, 26 times. **Nothing in this
document's extraction saw it**: not the profile, not the probes, not the
candidate list, not the census.

That is the census rule working, not failing. A census may not carry knowledge
from another document. `scripts/rules/attribution.py` now derives the markers for
all 346 documents, which is where procedural knowledge belongs — and measured
while writing it, a plain string probe finds the marker in 3 documents while the
same probe after undoing export escaping finds 18.

## The numbers

| | |
|---|--:|
| state before | 32 pages, 3 conflicts |
| new terms | **14** |
| new readings | **4** |
| new conflicts | **1** |
| state after | **46 pages, 4 conflicts** |

New terms nearly doubled the wiki for the second document running. For a first
`worldbuilding` document that is expected; if it does not fall sharply for the
next one, the corpus has more vocabulary than a term wiki can hold.
