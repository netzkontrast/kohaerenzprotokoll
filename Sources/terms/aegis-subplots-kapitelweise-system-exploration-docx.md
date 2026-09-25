---
source: Sources/drive/aegis-subplots-kapitelweise-system-exploration-docx.md
drive_id: "1StyFADCnWfMnriBDi_S0CzJFg66Cw8YU"
title: "AEGIS-Subplots Kapitelweise System-Exploration .docx"
category: aegis
index_date: "2025-08-05"
extracted: "2026-09-17"
candidates: 51
---

# Term census — AEGIS-Subplots Kapitelweise System-Exploration .docx

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py aegis-subplots-kapitelweise-system-exploration-docx`

```
  lines                620  (frontmatter ends at 9)
  body words           13947
  headings             2   bold-only lines 40
  table rows           0   code fences 0
  question marks       91
  backslash escapes    15
  typographic marks    53   ascii quotes 20
  invisible characters none
  math symbol lines    0
  glued ref numbers    180
  repeated labels      AEGIS-Fokus x39, Analyse des AEGIS-Fokus x39, Konzept/Trope x39, Recherchethemen x39
  longest line         785 chars
```

**91 question marks in 13,947 words**, and 180 glued reference numbers — the most
of any document processed. Both are structural rather than damage: the question
marks are the document's method, and the glued numbers are its citations to an
external bibliography that the export flattened.

## Stance — this document is a brief, and it says so in its first sentence

„Ziel ist es, die Natur, Methoden, Paradoxien und Interaktionen von AEGIS
systematisch zu explorieren und narrative Bausteine für die Konfrontation des
Protagonisten Kael mit dem System bereitzustellen." ^[L13]

So almost nothing here is an assertion about what is true in the novel. It is a
catalogue of what the novel **could** do, organised as 39 chapter blocks with
five fields each:

| field | what it is | how to read it |
|---|---|---|
| `AEGIS-Fokus` | one line naming the chapter's system question | often literally a question |
| `Analyse des AEGIS-Fokus` | the closest thing here to assertion | still hedged — „vermutlich" ^[L35], „könnte", `wahrscheinlich` |
| `Konzept/Trope` | **external theory imported as a lens** | never canon |
| `Recherchethemen` | two research prompts | questions by construction |
| `Subplot-Idee` (+ `Entwicklung`, `Diskussion`) | explicit invention | never canon |

The profile counted four of those labels 39 times each. `Subplot-Idee` is bolded
inline rather than list-prefixed, which is why it is not in the repeated-label
count and why the 40 bold-only lines are what they are.

**The `Konzept/Trope` field is the trap.** It carries Foucault's Panoptismus,
Sozialkreditsysteme, UEBA, Anomalieerkennung, Selbstorganisierte Kritikalität,
Searle's Chinesisches Zimmer, Gödels Unvollständigkeitssätze, Kybernetik,
Regelungstechnik, Ansteckungsmodelle, Datenbereinigung (Clear/Purge/Destroy),
Change Point Detection, Prinzipal-Agent-Problem, Edge-Case-Testing, Bostroms
Simulationshypothese, Ryles Geist in der Maschine, Qualia and the philosophical
zombie. Every one is named **as a model to apply**, with a `Begründung` saying
why it fits. None of them is a term of this world, and a census that harvested
them would inject a philosophy syllabus into the wiki.

## Candidates

51, written while reading, in `Plan/runs/aegis-subplots-kapitelweise-system-exploration-docx/03-candidates.md`.
**This is the first candidate list on this project that was written during the
read rather than reconstructed afterwards**, so it is the first one that can
serve as a baseline.

Counts are in `04-counts.txt`, each term reported twice — standing alone, and
including compounds.

### What the count corrected

| term | word | incl. compounds | what it means |
|---|--:|--:|---|
| `V` | 7 | 198 | the 198 are `Verhalten`, `Verbindung`, `Verteidigung`. `V` appears only as `Juna/V` |
| `AEGIS` | 257 | 342 | the 85 are `AEGIS-Fokus`, `AEGIS-Architektur`, `AEGIS-Direktive`, `Rest-AEGIS` |
| `Alter` | 1 | 12 | almost always `'Alters'`, in quotes, plural |
| `Guardian` | 22 | 63 | `Guardians`, `Guardian-Typen`, `Guardian-Subroutinen` |
| `Kern-Welt` | **0** | **0** | this document never writes it that way |

`Guardian-Subroutine`, `Kerndirektive` and `Kernsystem` each scored 0 as a word
and 1–2 as a substring: the document only ever uses them inflected —
`Guardian-Subroutinen`, `Kerndirektiven`, `Kernsystems`. Proposed in the singular
while reading, which is the German inflection problem doing exactly what the
briefing predicts. **A zero here meant `written differently`, not „absent", and
nothing in the count said so** — so `capture.py` now lists the surfaces it did
find under each candidate, and the same pass surfaced one candidate the reading
had missed entirely: `Kernsystemprotokoll` ^[L293].

`Innere Reise`, `Meta-Ebene` and `Äußere Konfrontation` scored 0 both ways
because the document writes them in full capitals as part section headers —
`TEIL 1: INNERE REISE` (L15), `TEIL 2: DIE META-EBENE & ZYKLEN` (L188),
`TEIL 3: DIE ÄUSSERE KONFRONTATION & RÜCKKEHR` (L361). They are structure, not
terms, and are withdrawn.

## Surfaces — one thing wearing several names

**`Wächter` is German for `Guardian`, and the document uses both.** The split is
not random: `Guardian` appears 22 times standing alone across every analytic
field, while `Wächter` appears **only in the titles of invented subplots** —
„Das Dilemma des Wächters" ^[L279] and „Der Wächter am Tor" ^[L530]. The English
term is the analytic register; the German one is the fictional register. Whether
that is one term is a judgement, but the distribution is a fact.

**`KW1` · `KW3` · `Kernwelt 1` · `Kernwelten`.** The document uses a shorthand
throughout — `KW1` 8 times, `KW3` once — and expands it exactly once:
„Untersucht Kernwelt 1 (Logik/LogOS) als direkte Manifestation von AEGIS'
Kernverarbeitungsstil" ^[L152]. That single line does three things at once: it expands
the abbreviation, it names KW1's domain as Logik, and it identifies KW1 with a
Guardian.

**`Juna/V`.** All 9 occurrences of `Juna` are in the compound form „Juna/V"
(L126, L133, L419, L420, L427, L433, L440), never alone. `V` never appears
outside it. The document treats the pair as a single referent — „Vorläufern von Juna/V" ^[L126], „(wahrscheinlich Juna/V, die Anomalie)" ^[L420] — and never says
what the slash means.

**`EP` / `Externe Ebene`.** „Kaels EP-Intrusion" ^[L60], and the expansion arrives
once in the same slashed shape: „bezogen auf die Externe Ebene/EP" ^[L61].

**`Riss` / `Risse`.** 11 and 5 standing alone, almost always in single quotes —
„Ein 'Riss' (Spalt/Bruch)" ^[L100]. The quotes are the document marking a term it
treats as established vocabulary rather than one it is coining.

## Gaps — used as known, defined nowhere here

- **`TSDP`** — „vermutlich TSDP-bedingt" ^[L35], „Psychologische Modelle der
  Dissoziation (TSDP)" ^[L40]. The parenthesis attaches it to dissociation and stops.
- **`Alters`** — used throughout in quotes as a known plural of psychological
  parts, never introduced.
- **`Kernwelten`** — the set is assumed; only KW1 and KW3 are ever numbered, and
  only KW1 is described.
- **`AEGIS` itself** — the root term is never defined. it is called „das
  antagonistische KI-System AEGIS" ^[L13] and every one of the 39 blocks then asks what
  it is, what it wants, whether it is conscious. **The document's method is to
  interrogate its own root term.**

## Self-consistency

No stated count contradicts the content. The document promises „jedes der 39
Kapitel" ^[L13] and delivers 39 numbered blocks across three parts (13 + 13 + 13).
Both part boundaries are stated and hold: Kapitel 1–13, 14–26, 27–39.

## What the extraction ran into

**A chapter that stages a question the wiki recorded as an answer.**

`Wiki/conflicts/c4` and `Wiki/questions/q1` both cite this document as holding a
passage that appears to settle whether the Guardians sit inside AEGIS. Chapter 20
is entirely about that question — and its title is
**„Die Natur eines Guardians - Autonomer Agent oder bloßes Werkzeug?
(Konfrontation)" ^[L272]** (L272).

The structural language does place them inside, consistently: „AEGIS und seinen
Guardians" ^[L274], „Führt er lediglich AEGIS' Code aus" ^[L273], „eine reine
AEGIS-Erweiterung" ^[L280], „Modelliert den Guardian als funktionale Komponente
innerhalb der AEGIS-Architektur" ^[L50]. But the chapter exists in order to put
that reading under pressure, via the Prinzipal-Agent-Problem: could a Guardian's
goals „selbst geringfügig, von AEGIS' Gesamtziel abweichen" ^[L274]?

**So the passage is about the right subject, at the right line, and does not say
what a search snippet suggested.** That is the failure mode a ranked result
invites, and it is the first time it has been caught here.

**Two counting defects, both found on the first count and both fixed** —
`scripts/capture.py` counted `V` 198 times with a substring match, and read the
nine prose bullets of the candidates file as candidates. See the commit.
