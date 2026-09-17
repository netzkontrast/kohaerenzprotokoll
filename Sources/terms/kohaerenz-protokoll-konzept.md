---
source: Sources/drive/kohaerenz-protokoll-konzept.md
drive_id: "1C8NGPq4Ut-uj-lcuuCRsQY5OiXBaV85t4BpNd_NpAzI"
title: "Kohärenz Protokoll - Konzept"
category: kernkonzept
index_date: "2025-04-17"
extracted: "2026-09-17"
candidates: 151
---

# Term census — Kohärenz Protokoll - Konzept

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py kohaerenz-protokoll-konzept`

```
  lines                417  (frontmatter ends at 9)
  body words           10653
  headings             12   bold-only lines 29
  table rows           29   code fences 0
  question marks       38
  backslash escapes    117
  typographic marks    32   ascii quotes 212
  invisible characters none
  math symbol lines    0
  glued ref numbers    117
  repeated labels      Inhaltlicher Fokus x3, Narrativer Rahmen x3, Pacing x3, Psychologischer Rahmen x3
  longest line         9219 chars
```

**12 headings are one H1 document title, ten roman-numeral `##` sections
(I–X), and one `####` "Quellenangaben" that jumps two levels** rather than
continuing the pattern. Inside section VII, a three-part label structure
repeats once per `Teil` (`Narrativer Rahmen` / `Psychologischer Rahmen` /
`Inhaltlicher Fokus` / `Pacing`), which is where the four `x3` repeated labels
above come from. The 9,219-character longest line is the
`Quellenangaben` section — 53 numbered references, glued by the export into a
single unbroken line with no line breaks between entries, checked by counting
`\d{1,2}\.` markers directly in that line. **The 117 "glued ref numbers" this
document reports are almost entirely something else** — checked against the
matcher directly: 42 are `Welt N`, 36 `Phase N`, 29 `Teil N`, 3 `Ebene N`, and
only a handful (`Qualia`, `Stories`, `Change`, `Dissociation`, `Adults`) sit
near an actual footnote number inside the reference titles themselves. The
metric that flags citation glue in other documents is here mostly flagging this
document's own structural numbering of worlds, phases and parts.

## What this document is

The first `kernkonzept` document read here, out of 75 landed in that category.
The title calls it a revised Fassung of an earlier draft:

> „Roman-Konzeptdokument: Seelen-Kohärenz-Protokoll (Überarbeitete Fassung)" ^[L11]

and it names that earlier draft in parentheses two lines later as Blueprint V5
^[L17]. It says explicitly what it replaces: the abstract Personas, named as
Architekt and Echo, become a specific diagnosis — Dissociative Identity
Disorder, in a protagonist named Michael — and the passive Partnerin ^[L31]
becomes a specific character, Julia. It reads as a full concept document —
logline, themes, conflict, character architecture, worldbuilding, narrative
structure, a chapter-by-chapter plot outline, a literature summary and an
open-questions section — rather than a note or a brief on one aspect of the
project.

## Candidates

151, written while reading, in
`Plan/runs/kohaerenz-protokoll-konzept/03-candidates.md`. Counts are in
`04-counts.txt`, each term reported twice — standing alone, and including
compounds. Every number below is re-run in `05-verify.txt`.

### What the count corrected

| term | word | incl. compounds | what it means |
|---|--:|--:|---|
| `nicht-lokale Phänomene` | 0 | 0 | document only writes `nicht-lokalen Phänomenen` |
| `strukturelle Dissoziation` | 0 | 0 | document only writes `strukturellen Dissoziation` |
| `nicht-lokale Verschränkung` | 0 | 0 | document only writes `nicht-lokaler Verschränkung` |
| `nicht-lokales Bewusstsein` | 0 | 0 | document only writes it genitive/dative, `Bewusstseins`/`Bewusstsein` |
| `ontologischer Konflikt` | 0 | 0 | document capitalises it as a heading, `Ontologischer Konflikt`, or inflects it, `des ontologischen Konflikts` — never the lowercase nominative the candidate proposed |
| `Kern` | 7 | 28 | the 28 fold three unrelated things: `Kernthemen` (3), `Kernpersönlichkeit` (3), `Kern-Trauma` (3), plus `Kernkonzept` (2) and more |
| `Alter` | 12 | 86 | 55 of the 86 are `Alters`, the plural the document actually uses |

Every zero above is inflection or capitalisation, not absence — checked by hand
against the source lines in `05-verify.txt`.

### Surfaces — one thing wearing several names

**The four Guardian "Werkzeuge" are named twice, with two different phrasings,
and neither reference names the other.** At L151–154, as noun phrases:
`Protokolle zur Datensynchronisation`, `Algorithmen zur Emotionsdämpfung`,
`Module zur Verhaltenskorrektur`, `Logische Kohärenz-Analysatoren`. At L344, as
compact compounds introducing the same four tools by example: `Daten-
Synchronisator`, `Emotions-Dämpfer`, `Verhaltens-Korrektor`, `Kohärenz-
Analysator`. `Kohärenz-Analysator` is the only one of the eight surfaces the
count catches twice (`Kohärenz-Analysatoren` at L154, `Kohärenz-Analysator` at
L344) — the other three pairs share no substring the counter can find.

**`Seele=Info` / `Seele = Information` occurs 13 times and is quoted every
time, but the quote mark is not consistent.** Only the first occurrence, at
L17, uses the German typographic „…" mark the document's own quotations use
elsewhere; the other 12 use a straight ASCII `"..."`. `02-probes.txt` already
counts 32 typographic marks against 212 ASCII quotes for the whole file, so
this is the export's general behaviour rather than something specific to this
phrase.

**`Michael` (87 standalone, 148 with compounds) and `Julia` (52 standalone, 72
with compounds) both compound onto each other**: `Michael-Julia-Verbindung`,
`Michael-Julia-Dynamik`, `Michael-Julia` on one side; `Julia-Verbindung`,
`Julia-Krise` on the other. The relationship between the two names is itself
named often enough to be a term of its own, not only a description.

**`Alters` (55) outnumbers the nominative `Alter` used for this sense** — the
86-count for bare `Alter` is inflated by the substring match against `Alters`
itself, `alters` (lowercase, 3), `Alter-Funktionen` and `Alter-Archetypen`.
This document always writes the concept in the plural.

### Gaps — used as known, defined nowhere here

- **`Guardians`** — 85 occurrences, the document's most frequent named entity,
  and never defined beyond their number (four) and their paradigm
  (`Seele=Info`). What a Guardian *is* — a program, an entity, a
  consciousness — is not stated.
- **`externe Ebene`** — 8 occurrences, and section X names its nature as the
  first open question: „Was genau *ist* die externe Ebene (physikalische
  Realität, höhere Dimension, Bewusstseinsfeld)?" ^[L396]. The document is
  explicit that this gap is not an oversight but an open decision.
- **`LogOS`, `Mnemosyne`, `Cerberus`, `Kairos/Sophia`** — each given one
  domain word (`Logik/Systemintegrität` etc., L138–141) and never a personality,
  a voice or an origin, unlike the human-side Alter table two sections earlier
  which gives each entry six columns.
- **`Kernpersönlichkeit`** — named to say the document avoids committing to
  one, „um der Theorie der strukturellen Dissoziation gerecht zu werden" ^[L109].
  A rejected concept rather than an undefined one, and the census records both
  kinds the same way: present, not explained.

### Self-consistency — one unflagged overshoot

Section VIII's introduction promises „ca. 13 Punkte pro Teil" ^[L321] across
the plot outline's three parts. Teil 1 holds exactly 13 numbered points, Teil 2
holds exactly 13, and **Teil 3 holds 15** — checked by counting the numbered
top-level bullets in each part's line range (`05-verify.txt`). The document
does not flag the overshoot; there is no parenthetical the way a later
document flags its own sample-size promise. 13+13+15 = 41 plot points total.

### What the extraction ran into

**A concept document that names its own predecessor and says exactly what it
is replacing**, which is not a shape earlier documents in this corpus had —
`Personas (Architekt, Echo etc.)` and `Partnerin` are candidates that occur
only inside that supersession and are recorded as such rather than as terms
this document defines on its own account.

**One table assigns the same world two different labels across two rows.** The
`Alter-Archetypen` table (L104–121) gives each alter a `Welt`, and two rows —
Persecutor and Memory Holder — both point at Welt 1 under two different
parenthetical labels, `(Zerbrochene Stadt)` and `(Trauma-Loop)`. `Trauma-Loop`
occurs nowhere else in the document; it exists only in that one table cell.
