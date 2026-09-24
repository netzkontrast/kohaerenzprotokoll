---
document: kohaerenz-protokoll-storyform-und-outline-2026-06-10-md
against: 56 pages, 5 conflicts
ran: "2026-09-24"
candidates: 383
decisions: 385
by_lookup: 293
judgements: 92
new_pages: 4
new_readings: 17
---

# Reconciliation 8 — `kohaerenz-protokoll-storyform-und-outline-2026-06-10-md` against the wiki

`python3 scripts/reconcile.py kohaerenz-protokoll-storyform-und-outline-2026-06-10-md`

383 candidates, 385 decisions — **293 by lookup, 92 to judgement.** The largest
reconciliation so far, and the first document from the canon era (2026-05 on).

## What kind of document this is

A specification that labels every passage itself — `[K]` canon, `[V]` proposal,
`[S]` derived detail, `[L]` gap — and **never hedges**: zero hedging words in
6,157. It names itself „Source-of-Truth" ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L11] and states its own precedence rule, „bei
Konflikt gewinnt das Neuere" ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L13]. **Both are recorded as the document's claims and
not applied.** A source that grants itself authority is exactly what this wiki
does not honour; which source wins is the author's call.

## 275 new terms, 4 pages — the rule, and where it came from

The lookup found 275 candidates with no page and no near match. Most of them are
the novel's *craft*: Dramatica vocabulary used in its home sense, act and chapter
structure, prose rules, the names of source files, open-question labels.

**The document draws the line itself.** At L13 it says what it deliberately does
not contain — „DKT-Physik im Detail, Sprach-DNA/Figuren-Bibel" ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L13] — and that figures
appear here only as „outline-relevante Kurzanker" ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L13]. So:

| rule | effect |
|---|---|
| a page needs a reading from a `[K]` passage, and the term must name something in the world or its physics | `coheron`, `nichts-rauschen`, `trennungsprotokoll`, `landauer-signatur` |
| figure entries are short anchors by the document's own statement | the 12 Alter names beside Kael get no page; the roster is on `alters` |
| a name the document marks undecided gets no page | `Wir-AEGIS` (OQ-A), `Moonshine` (OQ-F) |

The 271 that did not become pages are in the census with counts and lines.

## Readings added — 17 pages

`aegis` · `kohaerenz` · `entropie` · `juna` · `kael` · `multiplizitaet` ·
`alters` · `did` · `risse` · `guardians` · `kern-welten` · `konstrukt-stadt` ·
`moeglichkeits-garten` · `ueberwelt` · `externe-ebene` · `mnemosyne` ·
`kaels-wohneinheit`

`konstrukt-stadt` had one source until now; its five bare citations were
qualified with their document first, or they would have left the checked count
silently.

## A new conflict — C6

**Two Guardians, not five, and „KEIN Guardian-1:1".** ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L214] Every earlier reading gave
five named Guardians paired with the Kern-Welten. This document keeps the names as
names of worlds and denies the pairing. `Wiki/conflicts/c6-guardians-count-and-pairing.md`
holds the three positions.

## Questions and conflicts moved

- **Q1** gets the direct statement it asked for — the Guardians as AEGIS'
  architecture — for a different set of Guardians than the earlier pages describe.
  Narrower, still open.
- **Q3** gets an Alter count, 13, and the same six levels; the correspondence is
  still open.
- **Q4** gets a sixth use of the word family: `Wächterin`, a chapter title.
- **C5** gets a third source: `Möglichkeits-Garten` as a second name of KW4.

## Judgements

J46–J53, eight rows, each with a rule in words. The rest of the 92 are compound
against head and were decided by rules already on the ledger (J16, J28, J24, J21).
`judgements.py`: 53 judgements, 7 agree, 0 disagree.
