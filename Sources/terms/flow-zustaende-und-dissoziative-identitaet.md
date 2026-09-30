---
source: Sources/drive/flow-zustaende-und-dissoziative-identitaet.md
drive_id: "1CnmblO7cR5fS8dwq_VBcXNuC7XNhGdDkN9JxKW2KD2E"
title: "Flow-Zustände und dissoziative Identität"
category: theorie-psychologie
index_date: "2026-04-23"
extracted: "2026-09-29"
candidates: 318
---

# Term census — Flow-Zustände und dissoziative Identität

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

Read by a `document-reader` subagent (Sonnet), 2026-09-29: the whole document once,
with line numbers, then the list written while reading (five passes, `Plan/runs/flow-zustaende-und-dissoziative-identitaet/03-candidates.md`),
then the count. Every number below is re-counted in `Plan/runs/flow-zustaende-und-dissoziative-identitaet/05-verify.txt`.
Terms are written in code spans here; a quotation with a line is in the note.

## Structural profile

`python3 scripts/profile.py flow-zustaende-und-dissoziative-identitaet`

```
  lines                278  (frontmatter ends at 9)
  body words           6477
  headings             27   bold-only lines 0
  table rows           16   code fences 0
  question marks       10
  backslash escapes    64
  typographic marks    26   ascii quotes 90
  invisible characters none
  math symbol lines    0
  glued ref numbers    57
  repeated labels      none
  longest line         1247 chars
```

What the numbers are, once looked at. **Headings:** 27, every one set in bold, one H1
(L11, the report's own title), ten H2, fifteen H3 and one H4 (`Referenzen`, L219); no two
have the same text. The manifest's title `Flow-Zustände und dissoziative Identität` ^[flow-zustaende-und-dissoziative-identitaet.md:#0]
is not written anywhere in the body. Three H3 headings carry an ordinal in their own text (L153, L161,
L171); the list writes them without it. **Tables:** the 16 table rows are two tables, L71–80 and
L132–137, each with an empty header row, an alignment row and its real column heads in the
third row; every head and every row-head cell is wrapped in escaped asterisks, and the 64
backslash escapes are those and nothing else (ten such cells in the first table, six in the
second, four escapes to a cell). **Marks:** the 26 typographic marks are 15 en dashes in the
body and 11 characters in reference titles (curly quotation marks and dashes); the 90 ASCII quotation marks
are all in the body, so the body's quotation marks are the straight kind throughout.
**Question marks:** ten, and two of them are the only ones in the prose: both inside a
therapist's address to a patient at L145; the other eight are in reference titles and URLs, so
no candidate stands only inside a question. **Glued reference numbers:** the profile counts 57 and all 57 are the
date `April 23` in the 57 access notes of the reference list. It does not see the citation numbers
of the body, which are glued to the closing full stop of a sentence (`.1`, `.2` …) in 177 places
and stand after a word and a space before a comma in three more (L15, L147 twice); see
*What the extraction ran into*. No invisible characters, no formulas, no subscripts, no repeated labels.

## Stance, read per passage

The document is one voice throughout, a synthesising report: it writes in the present tense as
one who states findings, and it carries no tag of its own (no bracketed labels).
Reading the passages one by one:

| file lines | passage | how it speaks |
|---|---|---|
| 13–17 | lead | states a historical view of Flow and pathological dissociation as opposites and replaces it in the next sentence by a continuum; states the report's purpose and says it analyses the literature exhaustively |
| 19–33 | Flow and psychische Entropie | definition: names an originator, defines Flow and `psychische Entropie` in sentences of their own, and lists five numbered characteristics, each opening with a bold phrase |
| 35–43 | pathological dissociation and DIS | definition and description in the report's voice; the clinical names `Alters`, `Innenpersonen`, ANP and EP are put in quotation marks |
| 45–80 | comparative neurobiology | cited claims about regions, waves and chemistry; ends in a comparison table of seven dimensions, every content cell carrying a reference number |
| 82–96 | overlap and danger | boundary passage: what Flow and dissociation share, what separates them from `maladaptives Tagträumen`, and the warning signs of Flow that only masks dissociation |
| 98–118 | therapeutic mechanisms | assertion: Flow is called effective across all phases of treatment; three subsections give mechanisms; the last sentence of L118 (the `Sandkasten`) carries no reference number |
| 120–147 | prerequisites | instruction: grounding techniques in a three-row table, dual attention, and a `Safe Flow` metaphor that the text itself calls an adaptation from traffic engineering and medicine |
| 149–173 | methods | recommendation: three modalities, each described and linked to Flow by a sentence |
| 175–199 | co-consciousness and communication | practice: one method is described, in the text's words, as found in clinical practice and in `Betroffenenberichte`; quoted voices in German and English; `Co-Conning` and `Co-Fronting` are labels in parentheses |
| 201–207 | the system as an organisation | analogy marked as such by the text itself; the vocabulary of organisational communication is carried over to the DIS system |
| 209–217 | conclusion | restates the argument in three paragraphs and ends on an agenda: sharpen and operationalise the boundaries between Flow, maladaptive daydreaming and functional dissociation |
| 219–277 | Referenzen | 57 numbered entries, each a title, an access note and a URL |

## How the list was made

Decision 012 asks first for what a document names in the novel's world. This document names none:
it is a German-language clinical and neuroscientific report with no fictional world in it, so that
part of the rule found nothing. What the list holds is the second and third parts of the rule
applied to this text: words the document uses as its own terms (defined in a sentence,
glossed in parentheses, set in quotation marks after `sogenannte`, set in bold, or heading a section or a table
column), and the people and institutions it names as originators of a concept (Csikszentmihalyi, Dietrich,
Deisseroth, Reddemann, Stanford University, the ISSTD). English glosses are listed as the document writes them. Each
inflected surface that a count would split is listed on its own (`Flow-Zustand`, `Flow-Zustände`,
`Flow-Zustandes`, `Flow-Zuständen`; `Anteil`, `Anteile`, `Anteilen`, `Anteils`). Where the document joins two names
with a slash or a parenthesis the joined form and each name are listed (`Emotional Funnels/Dampeners`).

Left off by rule: the titles of cited works (L221–277); nouns in their ordinary sense (`Handlungen`,
`Überforderung`, `Langeweile`, `Flashbacks`, `Hypervigilanz`, `Amnesie`); method names of imaging
(`fMRT`, `EEG`, `PET`); the researchers' names that stand only inside reference titles. **The heading rule was applied
unevenly.** These heading words head a section and are not on the list: `Theoretische Fundierung` and `Konstrukt` (L19),
`Vergleichende Neurobiologie` (L45), `neurobiologische Signatur` (L49 and L59), `Schnittmenge` (L82),
`Therapeutische Implikationen` (L98), `Modifikation der neuronalen Netzwerke` (L102), `Methodische Ansätze` (L149) and the title's
`Neurobiologische und psychotherapeutische Dimensionen` and `systematische Analyse` (L11); yet the pure
section labels `Fazit und zukunftsorientierte Forschungsperspektiven` (L209) and `Prädiktorvariablen und Grundvoraussetzungen` (L120) are on it.
The list was not changed after the count, so the inconsistency stands. One sentence in the paragraph of
pass 5 of `03-candidates.md` (about suspended compounds) was corrected after the count; no `- ` line was changed, and
`scripts/gold.py` rules the list gold, with nothing added or dropped after the count.

The list has a `## lens` section of five terms, all from two places where the text itself says it borrows: the
`Safe Flow` metaphor from traffic engineering and medicine (L147) and the model of an organisation applied to the DIS
system (L201–207). No framework name from outside the document is listed as lens, because the document writes none
beyond the researchers above.

## Candidates and counts

318 candidates: 162 in pass 1, 43 in pass 2, 47 in pass 3, 50 in pass 4, 11 in pass 5 and 5 under lens. Copied
from `Plan/runs/flow-zustaende-und-dissoziative-identitaet/04-counts.txt` and `counts.json`, written by code. **word** is the term standing
alone (no letter, digit or hyphen on either side, case as written), **in** is the string anywhere including compounds and
inflections, and the lines are the file lines holding the string (the first eight). **The counts run over the whole
file, the reference list included** (L221–277), because the count cannot tell a term in the document's own sentence from
the same string in a cited title; the lines show where it happens. "also written as" lists what the document writes after the string.

### Pass 1 — file lines 11 to 110 (162 candidates)

| candidate | word | in | file lines holding the string | also written as |
|---|---:|---:|---|---|
| Flow | 56 | 108 | 11, 13, 15, 17, 19, 21, 25, 27 … | Flow-Zustände ×10; Flow-Zuständen ×9; Flow-Zustand ×7; Flows ×7 |
| Flow-Zustand | 7 | 9 | 13, 25, 27, 49, 51, 90, 96, 122 … | Flow-Zustandes ×2 |
| Flow-Zustandes | 2 | 2 | 27, 49 |  |
| Flow-Zustände | 10 | 19 | 11, 13, 17, 21, 86, 94, 100, 126 … | Flow-Zuständen ×9 |
| Flow-Zuständen | 9 | 9 | 11, 17, 21, 100, 159, 197, 211, 213 |  |
| Flow-Erleben | 1 | 3 | 19, 73, 106 | Flow-Erlebens ×2 |
| Flow-Erlebens | 2 | 2 | 19, 106 |  |
| optimalen Erfahrungszuständen | 1 | 1 | 13 |  |
| optimalen Erfahrung | 2 | 3 | 13, 21, 23 |  |
| dissoziative Identitätsstörung | 1 | 1 | 41 |  |
| dissoziativen Identitätsstörung | 9 | 9 | 11, 13, 23, 35, 39, 100, 177, 203 … |  |
| DIS | 16 | 23 | 13, 15, 39, 43, 61, 65, 73, 104 … |  |
| Dissoziation | 27 | 28 | 13, 15, 17, 35, 37, 39, 41, 47 … | Dissoziationen ×1 |
| pathologische Dissoziation | 8 | 8 | 13, 15, 37, 61, 84, 122, 211 |  |
| pathologischer Dissoziation | 2 | 2 | 13, 47 |  |
| Pathologische Dissoziation | 2 | 2 | 39, 73 |  |
| Kontinuum | 4 | 4 | 13, 17, 82, 84 |  |
| veränderter Bewusstseinszustände | 1 | 1 | 13 |  |
| Absorption | 10 | 10 | 13, 17, 21, 75, 82, 84, 90, 122 … |  |
| Absorption auf einem Kontinuum | 1 | 1 | 82 |  |
| Amnesiebarrieren | 2 | 2 | 15, 43 |  |
| Fragmentierung der Identität | 1 | 1 | 15 |  |
| psychologische Entropie | 2 | 2 | 15, 19 |  |
| psychische Entropie | 1 | 1 | 205 |  |
| psychischen Entropie | 2 | 2 | 23 |  |
| Psychische Entropie | 1 | 1 | 23 |  |
| Entropie | 8 | 8 | 15, 19, 23, 25, 205, 215 |  |
| Mihaly Csikszentmihalyi | 1 | 1 | 21 |  |
| Csikszentmihalyi | 2 | 2 | 21, 23 |  |
| Challenge | 3 | 3 | 25, 74, 173 | challenges ×1 |
| Skill | 3 | 3 | 25, 74, 173 |  |
| schmalen Korridor der optimalen Passung | 1 | 1 | 25 |  |
| Vollständige Konzentration auf die Gegenwart | 1 | 1 | 29 |  |
| Das Verschmelzen von Handlung und Bewusstsein | 1 | 1 | 30 |  |
| Verlust des reflektierenden Selbstbewusstseins | 1 | 1 | 31 |  |
| Verzerrung der Zeitwahrnehmung (Zeitdilatation) | 1 | 1 | 32 |  |
| Zeitdilatation | 1 | 1 | 32 |  |
| tiefes Jetzt | 1 | 1 | 32 |  |
| Deep Now | 2 | 2 | 32, 75 |  |
| Autotelische Erfahrung | 1 | 1 | 33 |  |
| kritische innere Instanz | 1 | 1 | 31 |  |
| Kampf-oder-Flucht-Reaktion | 1 | 1 | 37 |  |
| Hyperarousal | 2 | 2 | 37, 78 |  |
| Hypoarousal | 2 | 2 | 37, 78 |  |
| Freeze-Response | 1 | 1 | 37 |  |
| Freeze-Zustand | 1 | 1 | 65 |  |
| posttraumatischen Belastungsstörung | 1 | 1 | 39 |  |
| PTBS | 1 | 2 | 39, 173 | PTBS-Forschung ×1 |
| DSM-V | 1 | 1 | 39 |  |
| D-PTSD | 1 | 1 | 39 |  |
| Borderline-Persönlichkeitsstörung | 1 | 1 | 39 |  |
| BPS | 1 | 1 | 39 |  |
| Dissociative Experiences Scale | 2 | 2 | 39 |  |
| DES | 1 | 3 | 39 |  |
| DES-II | 1 | 1 | 39 |  |
| Multidimensional Inventory of Dissociation | 1 | 1 | 39 |  |
| MID | 1 | 1 | 39 |  |
| Adolescent Dissociative Experiences Scale | 1 | 1 | 39 |  |
| A-DES | 1 | 1 | 39 |  |
| Entwicklungstrauma | 1 | 1 | 41 |  |
| strukturellen Dissoziation | 1 | 1 | 41 |  |
| Persönlichkeitszuständen | 2 | 2 | 43, 177 |  |
| Persönlichkeitsanteile | 4 | 6 | 17, 23, 43, 189, 207 | Persönlichkeitsanteilen ×2 |
| Persönlichkeitsanteilen | 2 | 2 | 23, 43 |  |
| Alters | 8 | 8 | 43, 76, 143, 159, 177, 195, 207 |  |
| Innenpersonen | 2 | 2 | 43, 112 |  |
| Anscheinend Normalen Persönlichkeitsanteilen | 1 | 1 | 43 |  |
| ANP | 1 | 1 | 43 |  |
| Emotionale Persönlichkeitsanteile | 1 | 1 | 43 |  |
| EP | 1 | 2 | 43, 265 |  |
| Identitätsanteilen | 1 | 1 | 76 |  |
| Transiente Hypofrontalität | 2 | 2 | 45, 77 |  |
| transiente Hypofrontalität | 2 | 2 | 106, 183 |  |
| transienten Hypofrontalität | 2 | 2 | 51, 213 |  |
| Hypofrontalität | 7 | 7 | 45, 51, 65, 77, 106, 183, 213 |  |
| Transient Hypofrontality Hypothesis | 1 | 1 | 51 |  |
| THH | 2 | 2 | 51, 77 |  |
| limbisches Chaos | 1 | 1 | 45 |  |
| Arne Dietrich | 1 | 1 | 51 |  |
| präfrontalen Kortex | 3 | 3 | 51, 53, 137 |  |
| präfrontale Kortex | 3 | 3 | 53, 104, 183 |  |
| präfrontale Komplex | 1 | 1 | 106 |  |
| inneren Kritikers | 2 | 3 | 53, 102, 104 |  |
| Kritikerstimmen | 1 | 1 | 104 |  |
| Theta-Wellen-Aktivität | 1 | 1 | 55 |  |
| Alpha-Aktivität | 1 | 1 | 55 |  |
| Theta/Alpha-Synchronisation | 1 | 1 | 77 |  |
| Locus Coeruleus-Noradrenalin-System | 1 | 1 | 57 |  |
| LC-NE | 2 | 3 | 57, 77 | LC-NE-Aktivität ×1 |
| umgekehrten U-Kurve | 1 | 1 | 57 |  |
| Cocktails | 1 | 1 | 57 |  |
| Cocktail | 1 | 2 | 57, 78 | Cocktails ×1 |
| Dopamin | 3 | 3 | 57, 78, 112 |  |
| Noradrenalin | 2 | 3 | 57, 78 |  |
| Anandamid | 3 | 3 | 57, 78, 112 |  |
| Endorphinen | 2 | 2 | 57, 78 |  |
| Serotonin | 2 | 2 | 57, 78 |  |
| Default Mode Network | 2 | 2 | 57, 88 |  |
| DMN | 2 | 2 | 57, 88 |  |
| Shutdown | 3 | 3 | 61, 77, 96 |  |
| regionalen zerebralen Durchblutung | 1 | 1 | 63 |  |
| rCBF | 1 | 1 | 63 |  |
| Glukosestoffwechsel | 1 | 1 | 63 |  |
| CMRglu | 1 | 1 | 63 |  |
| orbitofrontalen Kortex | 2 | 2 | 63, 77 |  |
| Hippocampus | 2 | 3 | 63, 77, 145 | Hippocampus-Funktion ×1 |
| Amygdala | 3 | 4 | 65, 77, 145, 163 | Amygdala-Hyperaktivität ×1 |
| Angstzentrum | 1 | 1 | 65 |  |
| Karl Deisseroth | 1 | 1 | 63 |  |
| Stanford University | 1 | 1 | 63 |  |
| Cockpit des eigenen Körpers | 1 | 1 | 63 |  |
| Depersonalisation | 4 | 4 | 63, 75, 136, 195 |  |
| Derealisation | 3 | 3 | 75, 128, 195 |  |
| Numbing | 3 | 3 | 65, 136, 195 |  |
| Analgesie | 1 | 1 | 65 |  |
| Interozeption | 2 | 2 | 65, 126 |  |
| Analytische Dimension | 1 | 1 | 73 |  |
| Optimales Flow-Erleben | 1 | 1 | 73 |  |
| Pathologische Dissoziation (DIS) | 1 | 1 | 73 |  |
| Ätiologie und Auslöser | 1 | 1 | 74 |  |
| Qualität der Aufmerksamkeit | 1 | 1 | 75 |  |
| Struktur des Selbstgefühls | 1 | 1 | 76 |  |
| Neurobiologische Marker | 1 | 1 | 77 |  |
| Neurochemisches Milieu | 1 | 1 | 78 |  |
| Körperliche Repräsentation | 1 | 1 | 79 |  |
| Konsequenzen (Post-Effekt) | 1 | 1 | 80 |  |
| Embodiment | 3 | 3 | 79, 106, 251 |  |
| Agency | 3 | 3 | 79, 108, 112 |  |
| Selbstwirksamkeit | 2 | 2 | 80, 90 |  |
| LISREL-Modellen | 1 | 1 | 84 |  |
| dissoziativen Fluchtmechanismus | 1 | 1 | 84 |  |
| maladaptiven Tagträumens | 2 | 2 | 88, 90 |  |
| Maladaptives Tagträumen | 2 | 2 | 86, 90 |  |
| Maladaptive Daydreaming | 2 | 2 | 88, 245 |  |
| MD | 2 | 3 | 88, 231 |  |
| funktionale Dissoziation | 1 | 1 | 94 |  |
| funktionalen Dissoziation | 1 | 1 | 92 |  |
| Binges | 1 | 1 | 94 |  |
| Workaholismus | 1 | 1 | 94 |  |
| Out-of-Body | 1 | 1 | 96 |  |
| Maskierung der Dissoziation | 1 | 1 | 96 |  |
| achtsamen Flow | 1 | 1 | 96 |  |
| Mindful Flow | 1 | 1 | 96 |  |
| interozeptiven Bewusstheit | 1 | 1 | 96 |  |
| International Society for the Study of Trauma & Dissociation | 1 | 1 | 100 |  |
| ISSTD | 1 | 1 | 100 |  |
| Phase-Oriented Treatment | 1 | 1 | 100 |  |
| PoT | 1 | 2 | 100, 177 |  |
| phasenorientierte Psychotherapie | 1 | 1 | 100 |  |
| Herstellung von Sicherheit | 1 | 1 | 100 |  |
| Modifizierte Konfrontation | 1 | 1 | 100 |  |
| Identitätsintegration | 3 | 3 | 13, 100, 207 |  |
| Flow als neurobiologischer Katalysator der Trauma-Integration | 1 | 1 | 98 |  |
| Katalysator | 2 | 2 | 17, 98 |  |
| Overtime | 1 | 1 | 104 |  |
| Verstummen des inneren Kritikers | 1 | 1 | 102 |  |
| Täterimitierende Anteile | 1 | 1 | 104 |  |
| Introjekte der Täter | 1 | 1 | 104 |  |
| Reset | 1 | 1 | 106 |  |
| Rekalibrierung des neurochemischen Milieus und Wiedererlangung von Agency | 1 | 1 | 108 |  |
| Hypothalamus-Hypophysen-Nebennierenrinden-Achse | 1 | 1 | 110 |  |
| HPA-Achse | 1 | 1 | 110 |  |

### Pass 2 — file lines 110 to 150 (43 candidates)

| candidate | word | in | file lines holding the string | also written as |
|---|---:|---:|---|---|
| DIS-System | 2 | 2 | 112, 207 |  |
| DIS-Patienten | 5 | 5 | 110, 118, 159, 165, 217 |  |
| Kampf-oder-Flucht-Bereitschaft | 1 | 1 | 110 |  |
| Handlungsfähigkeit | 4 | 4 | 15, 112, 213 |  |
| Handlungsfähigkeit (Agency) | 1 | 1 | 112 |  |
| neuroplastisches Fenster | 1 | 1 | 112 |  |
| Identitätstransformation | 1 | 1 | 114 |  |
| Identitätstransformation und das Verschmelzen von Handlung und Bewusstsein | 1 | 1 | 114 |  |
| Verschmelzen von Handlung und Bewusstsein | 3 | 3 | 30, 76, 114 |  |
| Alter | 2 | 11 | 43, 76, 118, 143, 159, 177, 195, 207 … | Alters ×8; Alterations ×1 |
| Sandkasten | 1 | 1 | 118 |  |
| Identitätsentwürfe | 1 | 1 | 118 |  |
| Identitätszustände | 1 | 1 | 118 |  |
| Prädiktorvariablen und Grundvoraussetzungen | 1 | 1 | 120 |  |
| Erdung und Duale Aufmerksamkeit | 1 | 1 | 120 |  |
| Wechsel der exekutiven Kontrolle | 1 | 1 | 122 |  |
| Flow-Induktion | 2 | 2 | 149, 171 |  |
| Somatischer Erdung (Grounding) | 1 | 1 | 124 |  |
| Erdungstechniken | 3 | 3 | 126, 128, 199 |  |
| Grounding | 7 | 7 | 124, 126, 232, 252, 253, 254, 255 | grounding-techniques ×2; grounding-techniques-menu ×1 |
| neurologische Unterbrecher | 1 | 1 | 128 |  |
| Kategorie der Erdung | 1 | 1 | 134 |  |
| Methodische Beispiele | 1 | 1 | 134 |  |
| Neurophysiologische Wirkung | 1 | 1 | 134 |  |
| Sensorische Erdung | 1 | 1 | 135 |  |
| Physische Erdung | 1 | 1 | 136 |  |
| Kognitive Erdung & Atmung | 1 | 1 | 137 |  |
| 5-4-3-2-1-Methode | 1 | 1 | 135 |  |
| Box Breathing | 1 | 1 | 137 |  |
| Metakognition und Duale Aufmerksamkeit als Brücke zum Flow | 1 | 1 | 141 |  |
| Metakognition | 2 | 2 | 141, 143 |  |
| dualen Aufmerksamkeit | 2 | 2 | 143 |  |
| Dual Awareness | 1 | 2 | 143, 257 |  |
| Sensomotorische Psychotherapie | 1 | 1 | 143 |  |
| Somatic Experiencing | 3 | 3 | 143, 173, 257 |  |
| Pendulation | 1 | 1 | 145 |  |
| Titration | 1 | 1 | 145 |  |
| Ressource | 1 | 2 | 145, 205 | ressourcenorientierten ×1; Ressourcen ×1; ressourcen ×1 |
| Stresstoleranzfenster | 2 | 2 | 147, 151 |  |
| Window of Tolerance | 1 | 1 | 147 |  |
| Retraumatisierung | 1 | 1 | 147 |  |
| kardiopulmonalen Bypass | 1 | 1 | 147 |  |
| Informationsfluss | 1 | 1 | 147 |  |

### Pass 3 — file lines 150 to 182 (47 candidates)

| candidate | word | in | file lines holding the string | also written as |
|---|---:|---:|---|---|
| Fragmentierung der DIS | 1 | 1 | 151 |  |
| Psychodynamisch Imaginative Traumatherapie (PITT) | 3 | 3 | 153, 155, 213 |  |
| Psychodynamisch Imaginative Traumatherapie | 3 | 3 | 153, 155, 213 |  |
| PITT | 7 | 7 | 153, 155, 157, 159, 213, 263 | pitt-english ×1 |
| Luise Reddemann | 1 | 1 | 155 |  |
| Imagination | 3 | 6 | 155, 157, 159 | Imaginationen ×2; Imaginationstechniken ×1 |
| Imaginationstechniken | 1 | 1 | 155 |  |
| inneren sicheren Ortes | 1 | 1 | 157 |  |
| Guided Imagery and Music | 2 | 2 | 159, 266 |  |
| GIM | 2 | 2 | 159, 266 |  |
| Ego-State-Therapie | 1 | 1 | 159 |  |
| Arbeit auf der inneren Bühne | 1 | 1 | 159 |  |
| Trance- oder Flow-Zuständen | 1 | 1 | 159 |  |
| Kunsttherapie | 6 | 6 | 161, 163, 213, 267, 269 | kunsttherapie-bei-demenz ×1 |
| Kunsttherapie und der kreative Flow | 1 | 1 | 161 |  |
| kreative Flow | 1 | 1 | 161 |  |
| kreativen Flow | 2 | 3 | 165, 189, 215 |  |
| Theta/Alpha-Wellen-Muster | 1 | 1 | 165 |  |
| bilaterale Zeichnen | 1 | 1 | 167 |  |
| Corpus Callosum | 1 | 1 | 167 |  |
| interhemisphärische Integration | 1 | 1 | 167 |  |
| gravitationalen Sicherheit | 1 | 1 | 169 |  |
| Gravitational Security | 1 | 1 | 169 |  |
| Körperbasierte und sensomotorische Flow-Induktion | 1 | 1 | 171 |  |
| Ocean Therapy | 1 | 1 | 173 |  |
| Somatic Self-Inquiry & Integration | 1 | 1 | 173 |  |
| non-dualer Bewusstheit | 1 | 1 | 173 |  |
| Balance von Skill und Challenge | 2 | 2 | 74, 173 |  |
| Förderung der internen Systemkommunikation und Co-Bewusstheit durch Flow-Zustände | 1 | 1 | 175 |  |
| internen Systemkommunikation | 3 | 3 | 17, 175, 203 |  |
| interne Systemkommunikation | 1 | 1 | 215 |  |
| Co-Bewusstheit | 1 | 1 | 175 |  |
| amnestischen Barrieren | 2 | 2 | 177, 191 |  |
| Zeitverlust | 1 | 1 | 177 |  |
| Überwindung der Kommunikationsbarrieren durch entspannte Konzentration | 1 | 1 | 179 |  |
| Kommunikationsbarrieren | 2 | 2 | 179, 203 |  |
| entspannte Konzentration | 1 | 1 | 179 |  |
| Co-Bewusstsein (Co-Consciousness) | 1 | 1 | 177 |  |
| Co-Bewusstsein | 1 | 3 | 177, 187, 215 | Co-Bewusstseins ×2 |
| Co-Consciousness | 1 | 1 | 177 |  |
| Exekutivkontrolle | 1 | 1 | 177 |  |
| beschützende Anteile (Protectors) | 1 | 1 | 181 |  |
| Protectors | 1 | 1 | 181 |  |
| Gastgeber-Identitäten (Hosts) | 1 | 1 | 181 |  |
| Hosts | 2 | 2 | 181, 189 |  |
| Host | 2 | 4 | 181, 189, 205 | Hosts ×2 |
| Brute-Forcing | 1 | 1 | 181 |  |

### Pass 4 — file lines 182 to 217 (50 candidates)

| candidate | word | in | file lines holding the string | also written as |
|---|---:|---:|---|---|
| Co-Conning | 1 | 1 | 183 |  |
| Co-Fronting | 1 | 1 | 189 |  |
| die Führung übernehmen | 1 | 1 | 189 |  |
| entspannten Konzentration | 1 | 1 | 183 |  |
| Automatisches Schreiben und Flow-basiertes Journaling | 1 | 1 | 185 |  |
| Automatisches Schreiben | 1 | 1 | 185 |  |
| Flow-basiertes Journaling | 2 | 2 | 185, 213 |  |
| System-Journaling | 1 | 1 | 187 |  |
| automatischem Schreiben (Auto-Writing) | 1 | 1 | 187 |  |
| Auto-Writing | 1 | 1 | 187 |  |
| Flow-Schreiben | 1 | 1 | 199 |  |
| Flow-Praxis | 1 | 1 | 187 |  |
| Flow-Methode | 1 | 1 | 191 |  |
| Co-Bewusstseins | 2 | 2 | 187, 215 |  |
| emotionalen Dämpfern und Schutzanteilen | 1 | 1 | 193 |  |
| Emotionale Dämpfer | 1 | 1 | 195 |  |
| Trichter | 1 | 1 | 195 |  |
| Emotional Funnels/Dampeners | 1 | 1 | 195 |  |
| Emotional Funnels | 1 | 1 | 195 |  |
| Dampeners | 1 | 1 | 195 |  |
| Gefühlsstarre | 1 | 1 | 195 |  |
| Schutzanteilen | 2 | 2 | 193, 215 |  |
| Dämpfer-Anteil | 1 | 1 | 199 |  |
| Dämpfungs-Episoden | 1 | 1 | 199 |  |
| Crisis State | 1 | 1 | 199 |  |
| Metaphorische Parallelen zur internen Unternehmenskommunikation | 1 | 1 | 201 |  |
| Unternehmenskommunikation | 1 | 1 | 201 |  |
| Vertrauensverlust (Loss of Trust) | 1 | 1 | 205 |  |
| Loss of Trust | 1 | 1 | 205 |  |
| Lack of Alignment | 1 | 1 | 205 |  |
| toxischer Desorganisation | 1 | 1 | 205 |  |
| Top-Management | 1 | 1 | 205 |  |
| Protektoren | 1 | 1 | 205 |  |
| organismischen Flow | 1 | 1 | 207 |  |
| organismischem Flow | 1 | 1 | 215 |  |
| Team-Flow | 1 | 1 | 207 |  |
| Communication Flows Smoothly | 1 | 1 | 207 |  |
| Fazit und zukunftsorientierte Forschungsperspektiven | 1 | 1 | 209 |  |
| täterimitierenden Kritiker | 1 | 1 | 213 |  |
| psychischer Entropie | 1 | 1 | 215 |  |
| kreativen Flows | 1 | 1 | 215 |  |
| maladaptivem Tagträumen | 1 | 1 | 217 |  |
| vermeidender Dissoziation | 1 | 1 | 217 |  |
| heilsamem Flow | 2 | 2 | 94, 217 |  |
| heilsamer Flow-Zustände | 1 | 1 | 163 |  |
| echter Flow | 1 | 1 | 84 |  |
| vermeintliche Flow | 1 | 1 | 96 |  |
| tiefen Flow | 1 | 1 | 147 |  |
| bilaterales Zeichnen | 1 | 1 | 213 |  |
| somatische Erdung | 1 | 2 | 199, 213 |  |

### Pass 5 — the whole read, file lines 11 to 277 (11 candidates)

| candidate | word | in | file lines holding the string | also written as |
|---|---:|---:|---|---|
| Anteil | 2 | 9 | 104, 177, 181, 183, 187, 189, 191, 195 … | Anteile ×4; Anteils ×1; Anteilen ×1 |
| Anteile | 4 | 5 | 104, 181, 183, 191, 195 | Anteilen ×1 |
| Anteilen | 1 | 1 | 191 |  |
| Anteils | 1 | 1 | 189 |  |
| Teile (Alters) | 1 | 1 | 207 |  |
| Erdung | 8 | 11 | 120, 124, 126, 128, 134, 135, 136, 137 … | Erdungstechniken ×3 |
| Duale Aufmerksamkeit | 2 | 2 | 120, 141 |  |
| Traumatherapie | 6 | 6 | 147, 149, 153, 155, 207, 213 |  |
| Trauma-Integration | 1 | 1 | 98 |  |
| Verkörperung | 1 | 1 | 106 |  |
| Ich-Synthese | 1 | 1 | 13 |  |

### lens — borrowed by the document itself (5 candidates)

| candidate | word | in | file lines holding the string | also written as |
|---|---:|---:|---|---|
| Safe Flow | 2 | 2 | 147 |  |
| Minimum Safe Flow | 1 | 1 | 147 |  |
| minimaler sicherer Fluss | 1 | 1 | 147 |  |
| Das System als Organisation | 1 | 1 | 201 |  |
| heuristisches Modell | 1 | 1 | 203 |  |

## Zeros and flags

**Zeros: none.** No candidate is at `0 word` and none at `0 in`: a search of `04-counts.txt` for either finds
nothing (05-verify.txt). That is by construction more than luck. Every phrase of two or more words was put to
`read.py --find` before it went on the list, and each one resolved; the eleven acronyms shorter than four characters
(`DIS`, `BPS`, `DES`, `MID`, `ANP`, `EP`, `THH`, `DMN`, `MD`, `PoT`, `GIM`) are refused by `--find` for their length
although its nearest lines hold them at 100 %, and the count found every one.

**Substring flags: five, none a defect.** `Flow-Erleben` (1 word, 3 in) — the other two are `Flow-Erlebens`, listed on its
own. `DES` (1 word, 3 in) — the other two are inside `DES-II` and `A-DES`, both listed. `Alter` (2 word, 11 in) — eight are `Alters`,
which is listed, and one is `Alterations`, an English word in the title of reference 13 (L233), not the term. `Co-Bewusstsein`
(1 word, 3 in) — two are `Co-Bewusstseins`, listed. `Anteil` (2 word, 9 in) — `Anteile`, `Anteils` and `Anteilen` are listed, and so is `Dämpfer-Anteil` (L199).

## What the extraction ran into

**1. A reference list inside the counts.** L219 opens `Referenzen` and L221–277 hold 57 numbered entries, each
ending in an access note, `Zugriff am April 23, 2026` ^[flow-zustaende-und-dissoziative-identitaet.md:#57], and a URL. Their titles are
titles of cited works and stay off the list by rule, but the count reads them. Fourteen candidates have hits on
reference-list lines: ten as whole words (`Flow`, `Absorption`, `Embodiment`, `Maladaptive Daydreaming`, `Grounding`,
`Somatic Experiencing`, `PITT`, `Guided Imagery and Music`, `GIM`, `Kunsttherapie`) and four only inside a longer
word (`EP` in `REPAT`, L265; `MD` in `MDPI`, L231; `Alter` in `Alterations`, L233; `Dual Awareness` in `Non-Dual Awareness`, L257).
So the `word` count of those ten is not the document's own usage alone: of the seven whole-word hits of `Grounding` ^[flow-zustaende-und-dissoziative-identitaet.md:#7],
five are reference titles (L232, L252–255) and two are the body's (L124, L126). The substring trap appears in English
too (`Alter` in `Alterations`).

**2. Citation numbers the profile does not see, and a false count it reports.** The body cites its 57 references by a
number glued to the closing full stop of the sentence (`.1`, `.2` …), in 177 places, and by a number after a word and a space
before a comma in three more (L15, L147 twice). The profile's `glued ref numbers 57` is not these: every one of its 57
matches is `April 23`. The numbers cited in the body are 45 different ones; twelve of the 57 references are cited nowhere in
the body: 11, 14, 25, 26, 36, 40, 41, 42, 43, 48, 49 and 56. A quotation is written without the glued number; `quotes.py` drops it from
the source line.

**3. Two tables with an empty header row.** Each table has an empty header row (`|  |  |  |`), then the alignment row, then heads
in the third row, all in `\*\*`. A row is one line with pipes, so the flattened one-cell-per-line shape the briefing warns of does
not occur; the content cells end in the glued number of their source.

**4. Two headings the count reads as prose.** `Transiente Hypofrontalität vs. limbisches Chaos` (L45) and
`Maladaptives Tagträumen vs. Flow-Zustände` (L86) contain `vs. `, which `capture.py` takes for a sentence: listed whole they
would not have been counted, so the parts are listed. The same holds for any phrase with a comma, so the three phases of
the treatment at L100 are listed by their first words (`Herstellung von Sicherheit`, `Modifizierte Konfrontation`,
`Identitätsintegration`), not whole.

**5. Case and inflection.** `--find` is case-sensitive: the heading at L185 writes `Flow-basiertes Journaling`, and
`Flow-Basiertes` was refused. Headings and running text inflect the same term: `dissoziative Identitätsstörung` (L41)
and `dissoziativen Identitätsstörung` (nine hits) are listed apart, as are `Flow-Zustand`, `Flow-Zustände`, `Flow-Zustandes`
and `Flow-Zuständen`. Two suspended compounds: `Trance- oder Flow-Zuständen` (L159), whose expanded member `Trance-Zuständen` ^[flow-zustaende-und-dissoziative-identitaet.md:#0]
is written nowhere, and `fMRT- und EEG-Studien` (L217), whose first member `fMRT-Studien` stands once at L157.

**6. One word, three Flows.** `Flow` ^[flow-zustaende-und-dissoziative-identitaet.md:#56] is Csikszentmihalyi's state of optimal experience (L21); at L147 it is
also a borrowed fluid metaphor, `Safe Flow` ^[flow-zustaende-und-dissoziative-identitaet.md:#2] (blood flow in bypass surgery, traffic in lanes), turned onto how much traumatic
memory the patient meets at once (`Informationsfluss`); and at L207 and L215 it is `organismischen Flow` (L207), `organismischem Flow` (L215) and `Team-Flow` (L207), smooth
communication among the parts of the system. The count does not separate them. The document also qualifies Flow in many
words that each mark a different Flow: `echter Flow` (L84), `heilsamem Flow` (L94, L217), `vermeintliche Flow` (L96),
`achtsamen Flow` (L96), `kreative Flow` (L161), `tiefen Flow` (L147), `organismischen Flow` (L207).

**7. One thing, many names: the parts of the system.** `Alters` is used as a plural without an ending (seven
times) and once as the genitive singular (L143, `eines anderen Alters`), and the singular `Alter` stands twice (L118, L207); all ten
whole-word hits mean a part of the system. Beside it the document writes `Innenpersonen`, `Persönlichkeitsanteile`,
`Persönlichkeitszuständen`, `Identitätsanteilen`, `Anteil`/`Anteile`, `Protectors`/`Protektoren`, `Hosts`/`Host`,
`Schutzanteilen`, `Dämpfer-Anteil` and `Teile`. Which of these name one thing is said only by glosses: `Alters` or
`Innenpersonen` (L43), `beschützende Anteile (Protectors)` and `hypervigilante Gastgeber-Identitäten (Hosts)` (L181), `alle Teile (Alters)`
(L207), and `Emotionale Dämpfer` or `Trichter` (L195). ANP and EP are two typed names of parts (L43). The census keeps every
surface apart.

**8. The inner critic has no fixed name.** It is `kritische innere Instanz` (L31), `innerer Kritik` (L23), `inneren Kritikers`
(L53, L102), `inneren Kritikerstimmen` (L104) and `täterimitierenden Kritiker` (L213). The nominative `innerer Kritiker` ^[flow-zustaende-und-dissoziative-identitaet.md:#0]
is written nowhere, so a count of it cannot find the idea.

**9. `Entropie` and its two adjectives.** The construct is `psychologische Entropie` ^[flow-zustaende-und-dissoziative-identitaet.md:#2] (L15, L19) and
`psychische Entropie` ^[flow-zustaende-und-dissoziative-identitaet.md:#1] (L205), in `psychischen Entropie` (L23 twice) and `psychischer Entropie` (L215); it is defined once, in its own sentence at
L23. At L205 the same words name wasted time and energy in an organisation. The document never says where the word comes from:
`Thermodynamik` ^[flow-zustaende-und-dissoziative-identitaet.md:#0], `Physik` ^[flow-zustaende-und-dissoziative-identitaet.md:#0], `Shannon` ^[flow-zustaende-und-dissoziative-identitaet.md:#0] and `Boltzmann` ^[flow-zustaende-und-dissoziative-identitaet.md:#0] are not written.

**10. What quotation marks do here.** They are straight ASCII and are used for at least four things nothing announces:
a term taken from clinical usage, sometimes introduced by `sogenannte` (`sogenannte` ^[flow-zustaende-und-dissoziative-identitaet.md:#2] whole-word, 3 with `sogenannten`: L43, L94, L195); a figure
of speech (`Sandkasten`, `Reset`, `Overtime`, `Shutdown`, `Binges`, `Brute-Forcing`, `Cocktails`); a sentence of another speaker
named only by role or not at all (the therapist's questions at L145, a first-person German sentence at L187 with no speaker named,
English sentences at L181 and L197 that stand verbatim in German text); and an example text (the box-breathing counts, the affirmation at L137). Each was read in place.
English originals stand in parentheses beside German terms in many places (for example L25, L96, L100, L124, L143, L147, L169,
L177, L181, L205).

**11. Restated, then rejected; and the report's own voice.** The historical view of Flow and dissociation as `unvereinbare Gegensätze` (L13)
is restated in order to be replaced; `Brute-Forcing` (L181) and the `Herkömmliches, gezwungenes Tagebuchschreiben` of L187 are
restated as the method that fails. Sentences that state the report's own synthesis or figure of speech often carry no reference number
(the last sentence of L118, the second sentence of L122, L151, the last two sentences of L217), so a reading can tell a cited
finding from the report's own claim by that number.

**12. One numeral, four series.** `1.` opens the five Flow characteristics (L29–33), the three phases of treatment (inline, L100),
the three modalities (headings at L153, L161, L171) and the 57 references (L221–277). Nothing in the text says which series a
bare number belongs to.

**13. Gaps.** Used as known, and glossed at most once in a parenthesis: `Co-Conning` (L183) and `Co-Fronting` (L189), the
labels of states in which another part reaches the page; `Introjekte`, `Interozeption`, `Ego-State-Therapie`, `Somatic Experiencing`,
`Titration`, and `Embodiment` and `Agency` (each glossed once, `Verkörperung` at L106 and `Handlungsfähigkeit (Agency)` at L112). The
instruments of L39 (`DES`, `DES-II`, `MID`, `A-DES`) and the neurochemicals of L57 are named in single lists and none is explained.
The document's own root terms are defined: `Flow` in a sentence at L21 and DIS by its structure at L41–43. What the document itself names
as still open is the boundary between Flow, `maladaptivem Tagträumen` and `funktionaler, vermeidender Dissoziation`, which
L217 says must be sharpened and operationalised; that phrase inflects and splits the adjective, so `funktionale Dissoziation` (L94)
and `funktionalen Dissoziation` (L92) do not find it.

**14. Self-consistency.** Stated counts match: `drei Hauptkategorien` (L128) and three table rows (L135–137); `alle fünf
Sinne` (L157) and five named; the three phases at L100. No heading text repeats. The report treats one behaviour on both sides: temporary loss of
bodily signals is a feature of Flow (L33, and `Ausblenden von Grundbedürfnissen` in the table, L79) and neglect of bodily needs is a warning
sign of Flow that masks dissociation (L96); the text separates them by `temporär` against `chronische, selbstschädigende`. The first table names
`Cortisol` ^[flow-zustaende-und-dissoziative-identitaet.md:#1] (L78) and `Theta/Alpha-Synchronisation` ^[flow-zustaende-und-dissoziative-identitaet.md:#1] (L77), which the prose never writes: L55 gives Theta and Alpha as two
activities at two sites and L165 calls it a `Theta/Alpha-Wellen-Muster`. Lens terms were checked against the text before the
count: each of the five is written whole.

**15. What the document says about its own standing and date.** It calls itself a `Forschungsbericht` that analyses the literature
`exhaustiv` (L17) and its title calls it an analysis (L11); it makes no claim to be canon or a decision, and no tag, no bracketed
label and none of `Canon` ^[flow-zustaende-und-dissoziative-identitaet.md:#0], `Kanon` ^[flow-zustaende-und-dissoziative-identitaet.md:#0], `DEPRECATED` ^[flow-zustaende-und-dissoziative-identitaet.md:#0] is written. The only date the document gives for itself is the access
date of the 57 references, `April 23, 2026`, which is also the manifest's `index_date`; `Ich bin sicher im Jahr 2026` (L137) is an example
affirmation and dates nothing. It cites its sources by number, 57 entries listed and 45 of them cited in the body; that is its claim about them, not their text.

**16. Not anticipated by the briefing.** (a) A reference list at the tail of the file that the count reads as body, with English titles
that hit candidates whole and inside longer words (finding 1). (b) A profile field that reports 57 and means 57 dates, while the real
citation numbers go unseen (finding 2). (c) `--find` is case-sensitive and refuses acronyms under four characters, so short terms are
settled by the count alone. (d) No novel-world content at all, so the first line of decision 012 is empty and the list is the document's
own vocabulary. (e) One numeral numbering four series (finding 12). (f) The document's own metaphors carry borrowed source domains
(traffic, medicine, organisation) that it names itself; they are under `## lens`.
