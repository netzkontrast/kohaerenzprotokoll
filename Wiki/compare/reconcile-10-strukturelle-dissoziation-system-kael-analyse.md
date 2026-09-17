---
document: strukturelle-dissoziation-system-kael-analyse
against: "Wiki/index.json, built 2026-09-17, 59 pages / 6 conflicts"
ran: "2026-09-17"
candidates: 115
decisions: 106
by_lookup: 86
judgements: 14
new_pages: 1
new_readings: 7
---

# Reconciliation 10 — `strukturelle-dissoziation-system-kael-analyse`

The tenth reconciliation and the first `theorie-psychologie` document, the
first `T2-theory` tier. `scripts/reconcile.py` pre-classified 115 candidates
into 86 decided by lookup and 20 sent to judgement; this record covers the 14
of those 20 that produced a genuine one-term/two-terms decision (the other 6
were the nine epithet pairs folded under one rule, J84) plus four decisions
the lookup could not have reached at all, because they turn on whether an
imported clinical term has become a project term rather than on any surface
match.

## Why this document needed more judgement than any before it

The census splits its 115 candidates into 69 imported discipline vocabulary
(TSDP, ANP, EP, Aktionssysteme, the named Phobien, Ko-Bewusstheit, Switching,
and related terms, all cited to Van der Hart, Nijenhuis and Steele) against 46
project-specific rows. No `T3-work` document has carried anything close to
that ratio. **Reconciliation-by-lookup settles surface identity; it cannot
settle whether an imported term has become a project term** — that is a
person's call, stated as a rule each time, per `Plan/runs/judgements.jsonl`
J86 (`Aktionssysteme`, stays import) and J87 (the Gaslighting neuroscience
vocabulary, stays import). The contrast case is `Spannungspunkte` (J97): the
one candidate that is neither cited to an external source nor stated in the
document's own modal-hedge register, and the only one of the 115 that becomes
a new page.

## The hedging boundary, applied to page-worthiness

220 modal-hedge words in 12,762 (one every 58) sit almost entirely in Teil 1
and Teil 3 — the *application* of TSDP to System Kael's eleven specific
Anteile — while Teil 2 states TSDP itself flatly. That boundary decided
whether the eleven Anteile earned individual pages: their names and former
names are stated as fact, but everything else proposed about any one of
them is conditional. **No individual Anteil page was created.** The roster,
former names (`ehem.`) and English epithets are recorded as a new reading on
[[alters]] instead — the same outcome document 6's ten hedged profiles
reached (`oder ähnlich` on every name), reached here by the modal-hedge
register rather than an explicit qualifier.

## Decisions by lookup (86)

Not itemised here — `reconcile.py`'s `already_there` bucket was empty (0) and
its `new_reading`/`new_term` buckets are what the readings and the one new
page below are built from. Full pre-classification:
`Plan/runs/strukturelle-dissoziation-system-kael-analyse/reconcile-pre.json`.

## Decisions by judgement (14 rows, J84–J97)

| id | surfaces | decision | rule |
|---|---|---|---|
| J84 | 9 epithet pairs (`Kael`/`Kael (ANP Host)`, etc.) | one-term | a parenthetical English role-epithet at a recurring section header labels a name, not a term boundary |
| J85 | `System Kael` / `Kael` | two-uses-one-page | a whole/part distinction a page already states is a second surface, not a new term, under a new name |
| J86 | `Aktionssysteme` | stays-import | applying an imported term to project instances does not re-coin it, absent a project-specific redefinition |
| J87 | `Amygdala` / `präfrontaler Kortex` / `kognitive Dissonanz` | stays-import | a real-world citation supporting one claim, used once, is recorded as supporting vocabulary, not promoted |
| J88 | `Anteile` / `Alters` | one-term | the discipline's own native-language word and the corpus's borrowed-English word for the same concept are a language variant |
| J89 | `der Manager` / `Alltagsmanager` / `Managers` | one-term | a role's shortened, self-quoted form is the same term as its full compound |
| J90 | `Fragmentierung` / `psychische Fragmentierung` | one-term | a bare noun used as shorthand for an already-aliased compound folds with it |
| J91 | `Potentialität/Emergenz` / `Emergenz` | not-related | a world's psychological theme and an entity's cosmological origin are different referents despite sharing a word |
| J92 | `Depersonalisation` / `Personas` | not-related | a substring shared with an unrelated project term is coincidental |
| J93 | `Kohärenz Protokoll` / `Kohärenz` | not-related | a document naming its own novel's title is self-reference, not a reading of the concept the title contains a word from |
| J94 | `PTSD` / `komplexe PTSD` | one-term | a named subtype of an imported diagnosis is the same imported term as its base |
| J95 | `Konfliktdyaden` / `Analyse spezifischer Konfliktdyaden` | one-term | a heading and the noun inside it name one structural device, not two terms |
| J96 | `Juna/V` / `Juna` | one-term | a slash-suffixed surface used consistently, never contrasted with the bare form, is a reading |
| J97 | `Spannungspunkte` | new-page | neither cited to an external source nor stated in the hedge register — the contrast case |

All 14 replay `agrees`/`skipped` under `scripts/judgements.py` (0 disagree);
`Plan/runs/judgements.jsonl` has the evidence for each.

## New page (1)

- **`spannungspunkte`** — the document's own analytical frame (Spannungspunkte
  / Pressure Points), defined flatly at L19 and organising all of Teil 1.
  Aliases: `Pressure Points`.

## New readings (7)

- **`kael`** — fifth confirmation of the Michael→Kael rename; `System Kael`
  and `Kael` read as the existing Host/Gesamtsystem distinction under new
  surfaces; Alltagsmanager role; TSDP classification (Primärer ANP – Host);
  core phobia.
- **`kern-welten`** — a fifth independent Kern-Welten naming (`Co₁`, `McL`,
  `B`, `Ly`), sharing no vocabulary with the four namings already on the page;
  functions loosely aligned with document 5's `KW1`–`KW4`, recorded as an
  observation rather than a join.
- **`aegis`** — AEGIS's method against System Kael named as a clinical
  mechanism (weaponised dissociation via Gaslighting) rather than a
  systems-engineering one; settles neither `C1` nor `C3`.
- **`did`** — the corpus's first document to state TSDP itself, cited to its
  real authors, before applying it to anything project-specific: ANP/EP
  definitions, the three-tier spectrum; `Fragmentierung` added as an alias.
- **`multiplizitaet`** — a third independent use of exactly `funktionale
  Multiplizität`, restating Integration-is-not-Fusion in TSDP's own words;
  AEGIS present (75 occurrences) but bare `Entropie` absent (0), so the
  entropy/multiplicity question stays untouched, for a different reason than
  `kohaerenz-protokoll-konzept`'s.
- **`juna`** — Juna/V read entirely through disorganized-attachment theory as
  a counterweight to AEGIS; never explained beyond that.
- **`alters`** — a fifth, eleven-name Anteile roster (former names +
  epithets + TSDP classifications), sharing only `Kael` with
  `charakterkonzepte-fuer-kohaerenz-protokoll`'s ten; `Anteile` recorded as
  this document's own word for `Alters`; inter-Anteil `Amnesie` cross-
  referenced to [[risse]] without changing that page's own reading count.

## Conflict C6 — this document's side, now recorded

`Wiki/conflicts/c6-alter-roster-two-documents.md` already raised this
document's roster against `charakterkonzepte-fuer-kohaerenz-protokoll`'s.
This reconciliation moves that row from "not reconciled" to "reconciled" and
adds nothing that settles it — **the conflict is not resolved here.** Both
sides are now on record; which roster the novel keeps, if either, remains the
author's call.

## Not promoted (50)

Recorded with lines in `Plan/runs/strukturelle-dissoziation-system-kael-analyse/reconcile.json`.
Four are false-positive near-matches kept apart (`Kohärenz Protokoll`,
`Depersonalisation`, `Konfliktdyaden`, `PTSD`, per J92–J95 and J93); the
remaining 46 are the document's own textbook trauma-theory vocabulary and
structural labels — real-world clinical and neuroscience terms, cited or
generic, that stay the discipline's own words rather than becoming this
project's.

## What this reconciliation did not do

It did not resolve `C6`. It did not create a page for any individual Anteil,
even though all eleven names are stated as fact rather than hedged — the
document's *content* about them is hedged, and a page from that content would
be a page from an occurrence. It did not promote any of the 69
imported-vocabulary candidates to their own page, following the same rule the
census itself names for `Aktionssysteme` and `Homöostase`. It did not touch
`Wiki/questions/q3-how-many-kern-welten-and-alters.md`'s own count, though
the new Kern-Welten naming is cross-referenced from `kern-welten.md`.

## State

Before: 59 pages, 6 conflicts. After: 60 pages, 6 conflicts.
`Plan/runs/strukturelle-dissoziation-system-kael-analyse/reconcile.json` has
the full record.
