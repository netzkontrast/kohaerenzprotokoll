---
source: Sources/drive/roman-lokalitaeten-konzept-und-ausarbeitung.md
drive_id: "1CsMXR0Fv8MsyeDQB6MS4WxIhXbolQ6y1UlgHynsFgqg"
title: "Roman-Lokalitäten: Konzept und Ausarbeitung"
category: worldbuilding
index_date: "2025-04-18"
extracted: "2026-09-17"
candidates: 109
---

# Term census — Roman-Lokalitäten: Konzept und Ausarbeitung

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py roman-lokalitaeten-konzept-und-ausarbeitung`

```
  lines                631  (frontmatter ends at 9)
  body words           12022
  headings             26   bold-only lines 7
  table rows           60   code fences 0
  question marks       52
  backslash escapes    77
  typographic marks    19   ascii quotes 106
  invisible characters none
  math symbol lines    0
  glued ref numbers    133
  repeated labels      Konzept/Zweck x18, Regeln/Logik x18, Sensorik x18, Symbolik x18, Ästhetik/Visualisierung x18, Atmosphäre/Mood x17, Charakter/Plot Link x17, Design Inspirations x17, Landmarken/Key Features x17, Risse/Entropie Manifestations x17
  longest line         984 chars
```

**26 headings and 60 table rows** — the first document read here whose structure
is a table rather than a sequence of blocks. **133 glued reference numbers** are
its 72 numbered citations, flattened by the export so that the marker sticks to
the word it annotates.

**The repeated labels come in two heights, 18 and 17, and the difference is a
finding rather than noise.** The document defines an eleven-field profile
template once, in German, and then instantiates it seventeen times. Five of the
eleven fields are renamed in every instance:

| defined at L105–L115 | used in all 17 profiles |
|---|---|
| `Atmosphäre/Stimmung` | `Atmosphäre/Mood` |
| `Landmarken/Schlüsselmerkmale` | `Landmarken/Key Features` |
| `Charakter/Plot-Verbindung` | `Charakter/Plot Link` |
| `Design-Inspirationen` | `Design Inspirations` |
| `Risse/Entropie-Manifestationen` | `Risse/Entropie Manifestations` |

The six that keep their name count 18; the five that change count 17 plus one.
**A label census that matched on the definition would have found each of these
five once and concluded the field was never used.**

## Stance — two documents in one file, and the boundary is a heading

Teil I and Teil II are a **literature review of worldbuilding craft**. They cite
72 external sources and assert nothing about this world: *Inception*,
*Silent Hill 2*, *Neuromancer*, *Westworld*, Bartle's player types, liminal
space, the method of loci, glitch aesthetics. The register is advisory throughout.

Teil III and Teil IV are a **catalogue of this world's places**. Teil III is one
table of 51 named locations; Teil IV profiles 17 of them.

Teil V says what the whole is for:

> „Der Wert dieses Dokuments liegt in seiner Funktion als zentrale \"Welt-Bibel\"
> für die Schauplätze von \"Kohärenz Protokoll\"." ^[L553]

**105 hedging words in 12,022 — one every 114.** `könnte` 31, `vielleicht` 29,
`möglicherweise` 18, `potenziell` 15, `könnten` 10, `wahrscheinlich` 1,
`vermutlich` 1. They are not spread evenly: the *names* in Teil III are asserted
flat, and the *interiors* in Teil IV are almost entirely conditional —
„Könnte wie eine endlose, labyrinthartige Bibliothek oder ein riesiges,
chaotisches Lagerhaus wirken" ^[L329].

**So the table is the assertion and the profiles are the proposal**, which
inverts the usual expectation that the longer passage carries more weight.

## The `Source` column, which is this document's most unusual property

Every row of the master list carries where its name came from:

| value | rows |
|---:|---|
| `Explorative V2` | 30 |
| `Plot Teil 1` | 12 |
| `Konzept Doc` | 8 |
| `Kontext` | 1 |

**30 of the 51 locations are invented here and the table says so, row by row.**
The document repeats it in prose — the list is „eine auf den Kontextinformationen
basierende Rekonstruktion und Erweiterung" ^[L244] — and Teil III's introduction
calls the additions „der explorativen Entwicklung von rund 20 zusätzlichen
Orten" ^[L166], which the count contradicts: it is 30, not 20.

**This is a per-row provenance marker, self-reported.** Nothing else read here
has one.

## Candidates

109, written while reading, in
`Plan/runs/roman-lokalitaeten-konzept-und-ausarbeitung/03-candidates.md`.
Counts are in `04-counts.txt`, each term reported twice — standing alone, and
including compounds.

### What the count corrected

| term | word | incl. compounds | what it means |
|---|--:|--:|---|
| `Guardian` | **0** | **0** | the word is not in this document at all |
| `Anomalie` | 0 | 7 | the document only ever writes `Anomalien` |
| `Lokalitäten-Profil` | 0 | 2 | only `Lokalitäten-Profils` and `Lokalitäten-Profile` |
| `Riss` | 6 | 49 | 40 of the 49 are `Risse`; the plural is the primary form |
| `Limina` | 9 | 19 | the other 10 are `Liminalität`, `Liminal`, `Liminale` — craft theory, not the Alter |
| `Muse` | 10 | 14 | the 4 are `Museum` and `Museen`, in a gallery profile |
| `Kern-Welt` | 14 | 32 | 18 of the 32 are `Kern-Welten` |

`Limina` and `Muse` are the substring trap the probes predicted, and both would
have been merged by a plain count: `Liminale Räume` is a design concept named in
Teil II, `Limina` is a person named in Teil III, and they share five letters.

**A count of exactly 2 identifies a profiled location, and a count of 1 a
listed one.** Every one of the 51 location names occurs either once — in the
master table only — or exactly twice, once in the table and once as a profile
heading. There are 17 of the latter, which is the whole of Teil IV.

## The six reality levels, stated twice and identically

The document enumerates them as a profile field —

> „Eindeutige Bezeichnung und Zuordnung zu einer der sechs Realitätsebenen
> (KW1-4, Überwelt, Externe Ebene)." ^[L105]

— and then recapitulates each with a bearer and a function ^[L172–L177]:

| level | bearer, as the document writes it | function |
|---|---|---|
| Kern-Welt 1 (KW1) | LogOS | „Ebene der Logik, Ordnung, Rationalität, Struktur" ^[L172] |
| Kern-Welt 2 (KW2) | Mnemosyne | „Ebene der Emotionen, Erinnerungen, des Traumas" ^[L173] |
| Kern-Welt 3 (KW3) | Cerberus | „Ebene der Abwehrmechanismen, Kontrolle, Grenzen, Paranoia, des inneren Konflikts" ^[L174] |
| Kern-Welt 4 (KW4) | Kairos/Sophia | „Ebene des Potenzials, der Kreativität, der Integration, der Sinnfindung, der Zukunftsperspektiven" ^[L175] |
| Überwelt | AEGIS | „Digitale, informationsbasierte Ebene. Zentrum der Systemkontrolle, abstrakt, funktional." ^[L176] |
| Externe Ebene | Juna | „Mysteriöse, externe Realitätsebene, die zur AEGIS-Welt kontrastiert." ^[L177] |

The counts hold across the whole file: `KW1` 21, `KW2` 28, `KW3` 23, `KW4` 18,
`Überwelt` 27, `Externe Ebene` 15. The spelled forms `Kern-Welt 1` … `Kern-Welt 4`
occur three times each — the recapitulation, the table's group header, and the
profile section header.

## Surfaces — one thing wearing several names

**`Wächter`, and never `Guardian`.** The English word does not occur once. The
German one occurs 12 times standing alone and names exactly four bearers, in a
list the document supplies itself:

> „die Domänen der jeweiligen Wächter (LogOS, Mnemosyne, Cerberus,
> Kairos/Sophia)" ^[L35]

It is used analytically throughout, not decoratively: „Sitz von AEGIS und den
Wächtern in ihrer Systemfunktion" ^[L176], „Reagiert auf Abfragen der
Wächter/AEGIS" ^[L468], and it generates two compounds — `Wächter-Registry` and
`Wächter-Parameter` ^[L233].

**`Kairos/Sophia` is one surface and never two.** All 10 occurrences of `Kairos`
and all 10 of `Sophia` are inside the slashed form; neither name occurs alone
anywhere in the file. The document never says what the slash means.

**`Orakel/Muse` behaves identically** — 10 occurrences, all slashed, and it is an
Alter rather than a Wächter: „Assoziiert mit Alters wie Orakel/Muse" ^[L175].

**`Kern-Welt` is always hyphenated** — 14 standing alone, 18 as `Kern-Welten`,
zero as an unhyphenated `Kernwelt`. The shorthand `KW1`–`KW4` carries most of the
traffic.

**`Risse` is the primary form and it is single-quoted.** 40 of 49, and 20 of the
document's 32 single-quoted tokens are `'Risse'` or `'Riss'`. In this document
single quotes mark **vocabulary the document is handling as established**, while
double quotes mark either an external citation — „konsensuale Halluzination"
^[L45] — or a word used in a distancing sense, „gültige" ^[L194], „tote Pixel"
^[L471]. Both glyphs are ASCII; there are 106 ASCII quotes and 19 typographic
marks.

## Gaps — used as known, defined nowhere here

- **`AEGIS`** — 47 occurrences, never defined. It is „Domäne" of the Überwelt
  ^[L176] and the owner of „Ordnung, Integrität, Effizienz" ^[L49], and the
  document treats what it *is* as settled elsewhere.
- **`Entropie`** — 39 standing alone. It is something to be managed
  („Entropie-Management" ^[L21]), to be measured („Entropielevel" ^[L464],
  „Entropie-Hotspots" ^[L465], „Entropie-Indikatoren" ^[L470]) and to manifest
  as `Risse`, but never explained.
- **`Reboot`** — three occurrences plus `Post-Reboot-Zustand` ^[L21] and
  `System-Reboots` ^[L91]. KW1 is „Startpunkt nach dem Reboot" ^[L172] and the
  document proposes that the environment should hint at „die zyklische Natur des
  Systems" ^[L91]. What a reboot is, and how many there have been, is assumed.
- **`DID`** — two occurrences, expanded once as „dissoziative Identitätsstruktur"
  ^[L35] and otherwise used as known.
- **`Alters`** — 22 occurrences, four named (Limina, Echo, Nox, Orakel/Muse),
  none introduced.
- **The NPCs** — `Archivar` 8, `Regel-Exekutor` 6, `Therapeut` 2. Each is given a
  location and a function and no origin.

## Self-consistency — the document contradicts itself twice and flags one of them

**The profile count.** The introduction to Teil IV promises „ca. 30 der wichtigsten oder konzeptuell
interessantesten Lokalitäten" ^[L250]. Teil IV holds 17.
The document says so at the end:

> „(Anmerkung: Die obigen 17 Profile sind Beispiele. Im finalen Dokument würden
> ca. 30 solcher detaillierten Profile stehen, ausgewählt aus der Master-Liste in
> Teil III, um eine breite Abdeckung der Ebenen und der Handlung von Teil 1 zu
> gewährleisten.)" ^[L543]

So Teil IV is explicitly a sample of a document that does not exist yet.

**The count of invented places.** Teil III says the list results from „rund 20
zusätzlichen Orten" ^[L166]. The `Source` column marks 30 rows `Explorative V2`.
This one is **not** flagged.

**The size of the list itself.** Teil III announces „ca. 50+ Orte" ^[L166] and
its closing note says „ca. 52 Orte" ^[L244]. The table holds 51. Both are
approximations and neither is wrong.

## What the extraction ran into

**A document that names 51 things and describes 17 of them, and the 34 it does
not describe still have names.** That is a shape none of the earlier documents
had. A term is established here by *appearing in a table with a level, a
function and a cast* — three columns of assertion — and nothing more is said. It
is neither an occurrence in the sense of a word used in passing nor a reading in
the sense of a source saying what a thing is.

**The `Design Inspirations` field is this document's imported-theory trap.**
Gattaca, Minority Report, Tron, Blade Runner, Borges' Bibliothek von Babel,
Escher, The Shining, Zen-Gärten, the Berliner Mauer, CERN. Seventeen profiles
each end with one, and every entry is a comparison to something outside this
world. A census that harvested the field would put a film festival in the wiki.

**Teil I and Teil II would produce the same defect at larger scale.** They are a
craft essay: `Environmental Storytelling`, `Liminale Räume`, `Gedächtnispaläste`,
`Trauma-Landschaften`, `Glitch-Ästhetik`, `Spielertypen`, `Cyberspace`. Each is
named as a method to apply and each is cited to an external reference. None of
them is a term of this world, and `Limina` — an Alter — shares a stem with one of
them.
