---
source: Sources/drive/angst-bei-komplexen-traumafolgen.md
drive_id: "15n2apvMTmWxmtmXR6GExS80DlB07I4ETQAyzCXqTXIk"
title: "Angst bei komplexen Traumafolgen"
category: theorie-psychologie
index_date: "2026-04-24"
extracted: "2026-09-29"
candidates: 268
---

# Term census — Angst bei komplexen Traumafolgen

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py angst-bei-komplexen-traumafolgen`

```
  lines                274  (frontmatter ends at 9)
  body words           6355
  headings             25   bold-only lines 0
  table rows           15   code fences 0
  question marks       8
  backslash escapes    64
  typographic marks    16   ascii quotes 82
  invisible characters none
  math symbol lines    0
  glued ref numbers    80
  repeated labels      none
  longest line         1369 chars
```


### What the profile counts, and what it does not

The 25 headings are one H1 (L11), seven H2 (L13, L23, L53, L95, L101, L136, L189), sixteen H3 and one H4 (L197, `Referenzen`). Of the sixteen H3, five carry the ordinals 1. to 5. and open the five kinds of anxiety (L57 to L89), six carry 1. to 6. and open the treatment (L140 to L179), two are `Tabelle 1` and `Tabelle 2` (L107, L120) and three have no ordinal (L27, L35, L41). The prose ends at L195. The reference list runs from L199 to L273 and holds 75 numbered entries, each closing with an access date: `Zugriff am April 24, 2026` ^[angst-bei-komplexen-traumafolgen.md:#75].

The profile line `glued ref numbers 80` is not a count of footnote numbers in this file. Its pattern is a capitalised word, a space and one or two digits. Here that matches `April 24` in each of the 75 access lines (`April` ^[angst-bei-komplexen-traumafolgen.md:#75]) and five more strings: `Etwa 70` (from `70,4 Prozent`), `Tabelle 1`, `Tabelle 2`, `Phase 2` and `Chapter 6` (inside a reference title). The document's own source numbers are glued after the sentence-final period instead, as in `Psychotraumatologie.1`, a shape the pattern does not see. 136 of them stand in the prose and table cells before the reference list and they point to 54 of the 75 entries. The 21 entries numbered 2, 16, 20, 32, 34, 40, 45, 46, 49, 50, 53, 56, 57, 59, 61, 65, 66, 69, 70, 74 and 75 are cited nowhere in the text. The census records that the numbers are there and does not resolve them.

The body writes every quoted term in ASCII quotation marks (82 by the profile). Typographic marks stand as en dashes in prose at L61, L67, L138 and L195, and as glyphs in reference titles at L206, L228, L233, L235, L252, L259, L261 and L266. Of the 64 backslash escapes, 60 are `\*` around the header cells and row labels of the two tables (L113 to L118, L128 to L132), one is `\]` (L259) and three are `\_` (L247); a `\>` at L185 is not among the 64. The count reads the raw line, so a term that crosses a bold boundary counts zero. None of the 268 does.

### Stance, read per passage

The document has no bracketed labels, no self-review notes and no voice change without a marker; it labels its passages only by headings and by the glued source numbers, which say where a claim comes from and not how to read it. Stance is therefore read from the verbs and from where the numbers are missing.

| lines | passage | how it stands |
|---|---|---|
| L11 to L21 | Introduction: kPTBS against PTBS and ICD-11, the DSO features, aetiology, prevalence, cost, and the document's own programme for the taxonomy | reported claims with source numbers; the programme sentence that closes L21 has none |
| L23 to L51 | Neurobiology and the polyvagal frame | reported and numbered; the frame is attributed to a named author and introduced as a model that `postuliert` ^[angst-bei-komplexen-traumafolgen.md:#1] three states |
| L53 to L93 | The taxonomy: five kinds of anxiety | the document's own analytic frame, set in headings; each kind is carried by a reported theory or a clinical description, and the Fear Paradigm is restated in order to be criticised |
| L95 to L99 | Flight and migration | reported and numbered |
| L101 to L134 | Differential diagnosis: two tables, each with a paragraph | comparative assertions in table cells, two source numbers per row; the introductions at L105 and L122 have none |
| L136 to L187 | Treatment: phases, techniques, shame-focused, existential and trauma-focused methods, Prazosin | prescriptive, with reported evidence; hedged at the end of L187, where further randomised studies and off-label results are named |
| L189 to L195 | Conclusion | three paragraphs with no source number at all; restates the taxonomy under partly new names |
| L197 to L273 | 75 references | web pages, guideline files and articles, each with the same access date |

The necessity marker `zwingend` ^[angst-bei-komplexen-traumafolgen.md:#7] stands at L15, L69, L99, L138, L172, L193 and L195, that is in the diagnostic, treatment and conclusion passages. Across the prose and list lines before the reference list, ten carry no source number: L45, L55, L105, L122, L142, L144, L145, L191, L193 and L195. Those are introductions, two list items whose number stands on the third item, and the conclusion, which is the only stretch of more than one paragraph in a row without a number.

### Candidates and counts

268 candidates were written while reading, in four passes and a lens section (114, 40, 66, 41 and 7). `capture.py --count` read none of the `- ` lines as prose, and every candidate counts at least once. What went on the list: the document's own terms (headings, bold labels, table row labels, words introduced with `sogenannten` ^[angst-bei-komplexen-traumafolgen.md:#3] or set in quotation marks), the clinical entities it names (brain structures, instruments, drugs, therapies, guidelines), the persons it names as authors of a framework, and two named things of the world (`Weltgesundheitsorganisation`, `Erdbeben von L'Aquila`). What stayed off: nouns of the clinical register in their ordinary sense, phrases of the argument, the titles of the 75 cited works, and the ordinals of the numbered headings, so a heading is listed without its `1.`. Nothing in the document belongs to a fictional world: `Kohärenz` ^[angst-bei-komplexen-traumafolgen.md:#0], `Roman` ^[angst-bei-komplexen-traumafolgen.md:#0] and `Kapitel` ^[angst-bei-komplexen-traumafolgen.md:#0] stand 0 times.

Counts are case-sensitive. `alone` is the string with no letter, digit or hyphen on either side, `in` is the string anywhere, compounds included, and the inflected surfaces it found are in `04-counts.txt`. Line numbers are file lines. Lines from 199 on are reference-list entries, titles of works the document cites; they are listed apart, and 26 candidates have a hit there. The counts do not separate the two, the columns do.

### Reading, lines 10 to 109 (114)

| candidate | alone | in | body lines | reference-list lines |
|---|---:|---:|---|---|
| `Angst-Arten` | 1 | 1 | 11 |  |
| `komplexen Traumafolgestörungen` | 2 | 2 | 11, 55 |  |
| `multidimensionale Taxonomie der Angst` | 1 | 1 | 53 |  |
| `komplexen posttraumatischen Belastungsstörung` | 2 | 2 | 13, 15 |  |
| `kPTBS` | 22 | 30 | 15, 17, 21, 29, 51, 53, 63, 67 +18 | 201 |
| `Posttraumatische Belastungsstörung` | 8 | 8 | 15 | 202, 222, 240, 241, 246, 248, 253 |
| `PTBS` | 22 | 55 | 15, 17, 21, 29, 33, 39, 43, 51 +26 | 201, 203, 222, 240, 241, 247, 253 |
| `ICD-11` | 2 | 2 | 15 | 199 |
| `Internationalen Klassifikation der Krankheiten` | 1 | 1 | 15 |  |
| `Psychotraumatologie` | 2 | 2 | 15, 162 |  |
| `Traumafolgestörungen` | 4 | 4 | 11, 15, 19, 55 |  |
| `Disorders of Self-Organization` | 1 | 1 | 15 |  |
| `DSO` | 4 | 7 | 15, 67, 103, 138, 160, 172, 175 |  |
| `Störungen der Selbstorganisation` | 1 | 1 | 15 |  |
| `emotionalen Dysregulation` | 2 | 2 | 15, 91 |  |
| `negativen Selbstkonzept` | 1 | 1 | 15 |  |
| `interpersonellen Beziehungsstörungen` | 1 | 1 | 15 |  |
| `Bindungsängsten` | 1 | 1 | 15 |  |
| `Hyperarousal` | 14 | 16 | 15, 39, 51, 57, 59, 63, 99, 118 +5 | 212 |
| `Intrusionen` | 3 | 3 | 15, 33, 129 |  |
| `Flashbacks` | 6 | 6 | 15, 33, 39, 154, 187, 193 |  |
| `Vermeidungsverhalten` | 3 | 3 | 15, 65, 73 |  |
| `Coping` | 1 | 2 | 17, 117 |  |
| `Angst` | 36 | 52 | 11, 21, 23, 25, 37, 39, 43, 45 +28 | 232, 243 |
| `Furcht` | 6 | 11 | 21, 25, 29, 31, 63, 67, 71, 77 +2 |  |
| `Bindungstraumata` | 2 | 2 | 21, 177 |  |
| `Amygdala-Komplex` | 1 | 1 | 29 |  |
| `basolateralen Komplex` | 2 | 2 | 29 |  |
| `BLA` | 1 | 1 | 29 |  |
| `präfrontale Kortex` | 1 | 1 | 31 |  |
| `PFC` | 4 | 4 | 31, 33, 156 |  |
| `anteriore cinguläre Kortex` | 1 | 1 | 31 |  |
| `ACC` | 2 | 2 | 31, 33 |  |
| `Furchtextinktion` | 1 | 1 | 31 |  |
| `Furchtkonditionierung` | 1 | 1 | 29 |  |
| `Salienz-Netzwerk` | 1 | 1 | 33 |  |
| `SN` | 1 | 2 | 33, 181 |  |
| `Default Mode Network` | 1 | 1 | 33 |  |
| `DMN` | 1 | 1 | 33 |  |
| `Hippocampus` | 2 | 2 | 33 |  |
| `HPA-Achse` | 2 | 2 | 37 |  |
| `Nucleus paraventricularis` | 1 | 1 | 37 |  |
| `PVN` | 1 | 1 | 37 |  |
| `Yohimbin` | 1 | 1 | 39 |  |
| `Allopregnanolon` | 1 | 1 | 39 |  |
| `Stress-Lernen` | 1 | 1 | 29 |  |
| `ANS` | 1 | 1 | 43 |  |
| `Neurozeption` | 5 | 5 | 41, 43, 51, 148 |  |
| `Toleranzfenster` | 1 | 1 | 51 |  |
| `ventrale Vagalkomplex` | 1 | 1 | 47 |  |
| `dorsale Vagalkomplex` | 1 | 1 | 49 |  |
| `Vagalkomplex` | 4 | 5 | 47, 49, 71, 99, 148 |  |
| `sympathische Nervensystem` | 1 | 1 | 48 |  |
| `Mobilisation/Kampf-oder-Flucht` | 1 | 1 | 48 |  |
| `Mobilisation` | 1 | 1 | 48 |  |
| `Kampf-oder-Flucht` | 1 | 1 | 48 |  |
| `Immobilisation/Freeze/Shutdown` | 1 | 1 | 49 |  |
| `Immobilisation` | 2 | 2 | 49 |  |
| `Freeze` | 2 | 5 | 49, 51, 71, 118, 152 |  |
| `Shutdown` | 2 | 3 | 49, 118, 156 |  |
| `Sicherheit und soziale Verbundenheit` | 1 | 1 | 47 |  |
| `Totstellreflex` | 1 | 1 | 49 |  |
| `Numbing` | 3 | 3 | 49, 93, 118 |  |
| `Dissoziation` | 2 | 2 | 49, 93 |  |
| `Fear Paradigm` | 2 | 2 | 57, 63 |  |
| `Furcht-Paradigma` | 1 | 1 | 63 |  |
| `somatische Hyperarousal` | 1 | 1 | 57 |  |
| `Trigger` | 2 | 4 | 61, 118, 130 | 218 |
| `emotionaler Flashback` | 1 | 1 | 63 |  |
| `Hypoarousal` | 1 | 1 | 71 |  |
| `Hypervigilanz` | 4 | 5 | 73, 132, 183, 185 | 245 |
| `Maskierung` | 1 | 1 | 73 |  |
| `Normal-Sein-Wollen` | 1 | 1 | 73 |  |
| `Acting-in` | 1 | 1 | 73 |  |
| `toxische Scham` | 3 | 3 | 69, 114, 160 |  |
| `toxischer Scham` | 4 | 4 | 67, 91, 131, 193 |  |
| `schambasierte soziale Angst` | 2 | 2 | 67, 122 |  |
| `inneren Kritiker` | 1 | 1 | 69 |  |
| `innere Kritiker` | 1 | 1 | 65 |  |
| `Bindungsangst` | 3 | 3 | 75, 79, 175 |  |
| `relationale Traumatisierung` | 1 | 1 | 75 |  |
| `Bindungssystem` | 1 | 1 | 77 |  |
| `desorganisierten Bindungsstil` | 1 | 1 | 77 |  |
| `Abandonment Anxiety` | 1 | 1 | 79 |  |
| `Fear of Intimacy` | 1 | 1 | 79 |  |
| `Verlassenheitsangst` | 1 | 1 | 79 |  |
| `Angst vor dem Verlassenwerden` | 1 | 1 | 79 |  |
| `Angst vor Nähe und Intimität` | 1 | 1 | 79 |  |
| `Trauma Bonds` | 1 | 1 | 81 |  |
| `traumatischen Bindungen` | 1 | 1 | 81 |  |
| `Self-Abandonment` | 1 | 1 | 81 |  |
| `Selbstverrat` | 1 | 1 | 81 |  |
| `existenzielle Angst` | 2 | 2 | 85, 87 |  |
| `Assumptive World` | 2 | 2 | 83, 87 |  |
| `Mortalitätssalienz` | 1 | 1 | 85 |  |
| `Angst vor dem Kontrollverlust` | 1 | 1 | 89 |  |
| `emotionale Taubheit` | 1 | 1 | 93 |  |
| `Depersonalisation` | 1 | 1 | 93 |  |
| `Derealisation` | 2 | 2 | 33, 118 |  |
| `Akkulturationsstress` | 1 | 1 | 97 |  |
| `Differenzialdiagnostik` | 1 | 1 | 101 |  |
| `generalisierte Angststörungen` | 1 | 1 | 103 |  |
| `GAD` | 4 | 4 | 103, 122, 128, 129 |  |
| `Borderline-Persönlichkeitsstörung` | 4 | 4 | 103, 107, 113 | 201 |
| `BPS` | 4 | 5 | 103, 107, 113, 176 | 201 |
| `somatoformen Störungen` | 1 | 1 | 103 |  |
| `Trauma-Trias` | 1 | 1 | 103 |  |
| `International Trauma Questionnaire` | 1 | 1 | 103 |  |
| `ITQ` | 1 | 1 | 103 |  |
| `International Trauma Interview` | 1 | 1 | 103 |  |
| `ITI` | 1 | 1 | 103 |  |
| `Stephen Porges` | 1 | 1 | 43 |  |
| `Jennifer Freyd` | 1 | 1 | 77 |  |
| `Ronnie Janoff-Bulman` | 1 | 1 | 85 |  |

### Reading, lines 110 to 150 (40)

| candidate | alone | in | body lines | reference-list lines |
|---|---:|---:|---|---|
| `Klinische Dimension` | 1 | 1 | 113 |  |
| `Komplexe PTBS (kPTBS)` | 2 | 2 | 113, 128 |  |
| `Komplexe PTBS` | 3 | 3 | 113, 128 | 203 |
| `komplexe PTBS` | 2 | 2 | 77 | 201 |
| `komplexen PTBS` | 3 | 3 | 97, 138, 172 |  |
| `Borderline-Persönlichkeitsstörung (BPS)` | 3 | 3 | 103, 107, 113 |  |
| `Beziehungsmuster` | 1 | 1 | 115 |  |
| `Disconnection` | 1 | 1 | 115 |  |
| `Verlassensangst` | 1 | 1 | 116 |  |
| `Impulsivität & Suizidalität` | 1 | 1 | 117 |  |
| `Emotionsregulation` | 3 | 3 | 118, 175, 176 |  |
| `Diagnostisches Kriterium` | 1 | 1 | 128 |  |
| `GAD / Panikstörung / Soziale Phobie (SAD)` | 1 | 1 | 128 |  |
| `Generalisierten Angststörung` | 1 | 1 | 122 |  |
| `Panikstörung` | 4 | 5 | 103, 122, 128, 129 | 232 |
| `Soziale Phobie` | 2 | 2 | 128 | 232 |
| `sozialen Phobie` | 1 | 1 | 67 |  |
| `SAD` | 2 | 2 | 128, 129 |  |
| `Kognitiver Fokus der Angst` | 1 | 1 | 129 |  |
| `Auslöser (Trigger)` | 1 | 1 | 130 |  |
| `Qualität der sozialen Angst` | 1 | 1 | 131 |  |
| `Natur des Hyperarousals` | 1 | 1 | 132 |  |
| `kPTBS-Angst` | 1 | 1 | 120 |  |
| `primären Angststörungen` | 3 | 3 | 21, 120, 193 |  |
| `Expositionstherapien` | 1 | 1 | 134 |  |
| `S3-Leitlinien` | 1 | 1 | 138 |  |
| `AWMF` | 2 | 2 | 138 | 246 |
| `phasenorientierte Therapiemodell` | 1 | 1 | 140 |  |
| `relationale Sicherheit` | 1 | 1 | 140 |  |
| `Sicherheit und Stabilisierung` | 2 | 2 | 144, 148 |  |
| `Safety and Stabilization` | 3 | 3 | 144 | 251, 257 |
| `Traumaexposition und -bearbeitung` | 1 | 1 | 145 |  |
| `Trauma Processing` | 1 | 1 | 145 |  |
| `Integration und Neuorientierung` | 1 | 1 | 146 |  |
| `Integration and Meaning-making` | 1 | 1 | 146 |  |
| `therapeutische Allianz` | 1 | 1 | 148 |  |
| `Reparenting` | 1 | 1 | 148 |  |
| `inneren Kindes` | 1 | 1 | 148 |  |
| `erarbeitete sichere Bindung` | 1 | 1 | 148 |  |
| `earned secure attachment` | 1 | 1 | 148 |  |

### Reading, lines 150 to 185 (66)

| candidate | alone | in | body lines | reference-list lines |
|---|---:|---:|---|---|
| `Neuro-somatische Stabilisierungstechniken` | 1 | 1 | 150 |  |
| `Affektregulation` | 1 | 2 | 150, 162 |  |
| `Erdungs- und Reorientierungstechniken` | 1 | 1 | 154 |  |
| `Erdungs- und Reorientierungstechniken im Hier und Jetzt` | 1 | 1 | 154 |  |
| `5-4-3-2-1-Methode` | 1 | 1 | 154 |  |
| `Tauchreflex` | 1 | 1 | 154 |  |
| `Imaginative Distanzierung und Affektkontrolle` | 1 | 1 | 155 |  |
| `Screen-Technik` | 1 | 1 | 155 |  |
| `Tresor-Übung` | 1 | 1 | 155 |  |
| `Psychoedukation und Entpathologisierung` | 1 | 1 | 156 |  |
| `Psychoedukation` | 1 | 1 | 156 |  |
| `Entpathologisierung` | 1 | 1 | 156 |  |
| `Schamspezifische Interventionen` | 1 | 1 | 158 |  |
| `Compassion-Focused Therapy (CFT)` | 3 | 3 | 158, 160 | 261 |
| `Compassion-Focused Therapy` | 5 | 5 | 158, 160, 195 | 260, 261 |
| `CFT` | 5 | 5 | 158, 160, 162 | 261 |
| `Paul Gilbert` | 1 | 1 | 160 |  |
| `Affektregulationssysteme` | 1 | 1 | 162 |  |
| `Bedrohungssystem (Threat/Amygdala)` | 1 | 1 | 162 |  |
| `Bedrohungssystem` | 3 | 3 | 162 |  |
| `Threat` | 1 | 1 | 162 |  |
| `Antriebssystem (Drive/Dopamin)` | 1 | 1 | 162 |  |
| `Antriebssystem` | 1 | 1 | 162 |  |
| `Drive` | 1 | 2 | 162 | 214 |
| `Beruhigungs- und Fürsorgesystem (Soothing System/Oxytocin und Opiate)` | 1 | 1 | 162 |  |
| `Beruhigungssystem` | 1 | 1 | 162 |  |
| `Soothing System` | 1 | 1 | 162 |  |
| `mitfühlenden Selbst` | 1 | 1 | 162 |  |
| `Compassionate Self` | 1 | 1 | 162 |  |
| `Selbst-Mitgefühls` | 1 | 1 | 162 |  |
| `Selbstmitgefühl` | 1 | 1 | 172 |  |
| `schmutzige kleine Geheimnis` | 1 | 1 | 162 |  |
| `Humanistisch-Existenzielle Perspektiven` | 1 | 1 | 164 |  |
| `existenzialistisch-humanistischen Psychotherapie` | 1 | 1 | 166 |  |
| `Kirk Schneider` | 1 | 1 | 168 |  |
| `Accelerated Experiential Dynamic Psychotherapy (AEDP)` | 1 | 1 | 168 |  |
| `AEDP` | 1 | 1 | 168 |  |
| `Traumafokussierte und integrative Expositionsverfahren` | 1 | 1 | 170 |  |
| `fokussierte Traumabearbeitung` | 1 | 1 | 172 |  |
| `Affekttoleranz` | 1 | 1 | 172 |  |
| `EMDR (Eye Movement Desensitization and Reprocessing)` | 1 | 1 | 174 |  |
| `EMDR` | 3 | 3 | 174, 195 | 247 |
| `Eye Movement Desensitization and Reprocessing` | 1 | 1 | 174 |  |
| `STAIR-NT (Skills Training in Affective and Interpersonal Regulation - Narrative Therapy)` | 1 | 1 | 175 |  |
| `STAIR-NT` | 1 | 1 | 175 |  |
| `Skills Training in Affective and Interpersonal Regulation` | 1 | 1 | 175 |  |
| `Narrative Expositionstherapie (NET)` | 1 | 1 | 175 |  |
| `Narrative Expositionstherapie` | 1 | 1 | 175 |  |
| `NET` | 2 | 2 | 175, 195 |  |
| `DBT-PTBS / DBT-TF` | 1 | 1 | 176 |  |
| `DBT-PTBS` | 1 | 1 | 176 |  |
| `DBT-TF` | 1 | 1 | 176 |  |
| `Dialektisch-Behavioralen Therapie` | 1 | 1 | 176 |  |
| `MBT-TF (Mentalisierungsbasierte Therapie für Trauma)` | 1 | 1 | 177 |  |
| `MBT-TF` | 1 | 1 | 177 |  |
| `Mentalisierungsbasierte Therapie für Trauma` | 1 | 1 | 177 |  |
| `Pharmakologische Interventionen` | 1 | 1 | 179 |  |
| `Prazosin` | 12 | 13 | 179, 183, 185, 187, 195 | 223, 270, 271, 273 |
| `selektive Serotonin-Wiederaufnahmehemmer` | 1 | 1 | 181 |  |
| `SSRI` | 1 | 1 | 181 |  |
| `Serotonin-Noradrenalin-Wiederaufnahmehemmer` | 1 | 1 | 181 |  |
| `SNRI` | 1 | 1 | 181 |  |
| `Sertralin` | 1 | 1 | 181 |  |
| `Paroxetin` | 1 | 1 | 181 |  |
| `Venlafaxin` | 1 | 1 | 181 |  |
| `Cluster-D-Symptome` | 1 | 1 | 185 |  |

### Reading, lines 186 to 200, and forms noticed while reading the whole (41)

| candidate | alone | in | body lines | reference-list lines |
|---|---:|---:|---|---|
| `Alpha-1-Blockade` | 1 | 1 | 187 |  |
| `polyvagale Komplex` | 1 | 1 | 191 |  |
| `Bindungsstörungen` | 1 | 1 | 193 |  |
| `Desorganisationsmuster` | 1 | 1 | 193 |  |
| `schambasierte soziale Vermeidungsangst` | 1 | 1 | 193 |  |
| `Vermeidungsangst` | 1 | 1 | 193 |  |
| `emotionalen Flashbacks` | 3 | 3 | 33, 154, 193 |  |
| `Retraumatisierungen` | 1 | 1 | 193 |  |
| `Traumanetzwerke` | 1 | 1 | 195 |  |
| `neuro-somatischer Stabilisierungsverfahren` | 1 | 1 | 195 |  |
| `schamfokussierte Ansätze` | 1 | 1 | 195 |  |
| `existenzialistisch-humanistische Ansätze` | 1 | 1 | 195 |  |
| `komplexen Posttraumatischen Belastungsstörung` | 1 | 1 | 191 |  |
| `Traumafolgen` | 1 | 1 | 25 |  |
| `Trauma-Bonds` | 1 | 1 | 156 |  |
| `Sympathikusdominanz` | 1 | 1 | 51 |  |
| `dorsale Vagusdominanz` | 1 | 1 | 51 |  |
| `sympathische Hyperarousal` | 2 | 2 | 99, 185 |  |
| `traumatische Hyperarousal` | 1 | 1 | 59 |  |
| `traumabedingte Hyperarousal` | 1 | 1 | 122 |  |
| `traumabedingte Angst` | 1 | 1 | 21 |  |
| `traumabedingten Angst` | 1 | 1 | 23 |  |
| `traumatischen Angst` | 1 | 1 | 37 |  |
| `soziale Angst` | 3 | 3 | 65, 67, 122 |  |
| `Soziale Angst` | 1 | 1 | 67 |  |
| `sekundäre Scham` | 1 | 1 | 156 |  |
| `Kernemotion` | 1 | 1 | 114 |  |
| `Defekthaftigkeit` | 2 | 2 | 67, 129 |  |
| `Selbstkritik` | 2 | 2 | 160, 162 |  |
| `Dysregulation` | 7 | 7 | 15, 27, 37, 39, 43, 91 | 212 |
| `Scham` | 16 | 20 | 15, 65, 67, 69, 71, 73, 91, 114 +7 | 228, 233 |
| `Verrat` | 5 | 6 | 75, 77, 79, 131, 148 |  |
| `Grundannahmen` | 3 | 3 | 85, 166, 191 |  |
| `Grundüberzeugungen` | 1 | 1 | 85 |  |
| `Abgrenzungsspektrum` | 1 | 1 | 101 |  |
| `Interkulturelle und soziopolitische Kontexte` | 1 | 1 | 95 |  |
| `Flucht und Migration` | 1 | 1 | 95 |  |
| `prä-migratorische Traumatisierungen` | 1 | 1 | 97 |  |
| `post-migratorischen Stressoren` | 1 | 1 | 97 |  |
| `Weltgesundheitsorganisation` | 2 | 2 | 15, 17 |  |
| `Erdbeben von L'Aquila` | 1 | 1 | 73 |  |

### Lens — borrowed frameworks the document applies (7)

| candidate | alone | in | body lines | reference-list lines |
|---|---:|---:|---|---|
| `Polyvagal-Theorie` | 3 | 3 | 41, 43, 45 |  |
| `Window of Tolerance` | 7 | 7 | 41, 51, 152, 195 | 216, 218, 219 |
| `Betrayal Trauma Theory` | 1 | 1 | 77 |  |
| `Theorie des Verratstraumas` | 1 | 1 | 77 |  |
| `Shattered Assumptions` | 4 | 4 | 85, 166 | 208, 224 |
| `zerbrochene Grundannahmen` | 1 | 1 | 85 |  |
| `Terror-Management-Theorie` | 1 | 1 | 85 |  |


Seven names stand under the lens heading: five borrowed concepts the document applies to the anxiety picture (`Polyvagal-Theorie`, `Window of Tolerance`, `Betrayal Trauma Theory`, `Shattered Assumptions`, `Terror-Management-Theorie`) and two German glosses of two of them (`Theorie des Verratstraumas`, `zerbrochene Grundannahmen`). Each was checked as a whole word against the raw file before the count, and each is written as the document writes it.

### What the extraction ran into

No candidate counts zero, alone or inside compounds. That follows from asking `read.py --find` for every phrase of two or more words before it went on the list (138 of the 268 hold a space or a slash, and a second pass over all of them refused none), and from writing each inflected form as the document has it. Three dictionary forms were refused and replaced by what the text writes: `innerer Kritiker` by `inneren Kritiker` and `innere Kritiker`, `emotionale Flashbacks` by `emotionaler Flashback` and `emotionalen Flashbacks`, `prä-migratorischen Traumatisierungen` by `prä-migratorische Traumatisierungen`. Fifteen candidates are shorter than the four characters `--find` compares (`DSO`, `BLA`, `PFC`, `ACC`, `SN`, `DMN`, `PVN`, `ANS`, `GAD`, `BPS`, `ITQ`, `ITI`, `SAD`, `CFT`, `NET`). For a token that short `--find` answers that it is not in the document even when it is, so those were asked of the count, and each stands at least once. A list with no zero says that no listed form is one the document lacks. It does not say that nothing is missing.

Omissions seen after the count. The list is frozen, so they are recorded here and not added. `Amygdala` stands alone 12 times (`Amygdala` ^[angst-bei-komplexen-traumafolgen.md:#12]) and is on the list only inside `Amygdala-Komplex`, although `Hippocampus`, a structure of the same kind, is listed. `Selbstkonzept` (`Selbstkonzept` ^[angst-bei-komplexen-traumafolgen.md:#3]) heads the first row of Table 1 and stands in the conclusion, and only `negativen Selbstkonzept` is listed. The transmitter names `Serotonin`, `Noradrenalin` and `Dopamin` (L37, and `Dopamin` ^[angst-bei-komplexen-traumafolgen.md:#1] alone) and `GABA` (L39) were left off although `Yohimbin` and `Allopregnanolon` were listed, which is an inconsistency of this reading's selection and not a rule. `Sicherheit` stands alone 17 times (`Sicherheit` ^[angst-bei-komplexen-traumafolgen.md:#17]) as the word for what the polyvagal evaluation looks for, what the first treatment phase builds and what the assumptive world loses; it was left off as an ordinary noun and is the one such noun this document leans on most.

The counts include the reference list. English candidates are the ones that pick up titles of cited works there: `Window of Tolerance` stands in three titles, `Safety and Stabilization` in two, `Compassion-Focused Therapy` in two, `Shattered Assumptions` in two, `Prazosin` in four. The rest of the 26 are German disorder names and clinical words in titles such as the first entries.

One disorder wears six surfaces: `kPTBS`, `Komplexe PTBS`, `komplexe PTBS`, `komplexen PTBS`, `komplexen posttraumatischen Belastungsstörung` (L13, L15) and `komplexen Posttraumatischen Belastungsstörung` (L191, capital P). The abbreviation `kPTBS` is introduced at L15 and used throughout, while the half-spelled `komplexe PTBS` and `komplexen PTBS` also stand in prose at L77, L97, L138 and L172 and in both table headers. `PTBS` is 22 alone and 55 in, the difference being `kPTBS` and other compounds. The same idea carries variant spellings, each listed as written: `Verlassensangst` ^[angst-bei-komplexen-traumafolgen.md:#1] as a table label and `Verlassenheitsangst` ^[angst-bei-komplexen-traumafolgen.md:#1] in prose, `Trauma Bonds` ^[angst-bei-komplexen-traumafolgen.md:#1] and `Trauma-Bonds` ^[angst-bei-komplexen-traumafolgen.md:#1], `Selbst-Mitgefühls` ^[angst-bei-komplexen-traumafolgen.md:#1] and `Selbstmitgefühl` ^[angst-bei-komplexen-traumafolgen.md:#1]. `Hyperarousal` takes four modifiers (`somatische`, `traumatische`, `traumabedingte`, `sympathische`), `toxische Scham` and `toxischer Scham` are two grammatical forms, and the dorsal vagal state has five names (`Immobilisation`, `Freeze`, `Shutdown`, `Hypoarousal`, `Totstellreflex`). `Freeze` stands alone twice (`Freeze` ^[angst-bei-komplexen-traumafolgen.md:#2]) and three more times inside `Freeze-Zustand`, so its `in` count is 5.

The group of five kinds has no fixed name. The H1 has `Angst-Arten` (`Angst-Arten` ^[angst-bei-komplexen-traumafolgen.md:#1]) and `Arten` stands 0 times as a word (`Arten` ^[angst-bei-komplexen-traumafolgen.md:#0]); the body says `Manifestationsformen` (`Manifestationsformen` ^[angst-bei-komplexen-traumafolgen.md:#1]) at L21, `Taxonomie` (`Taxonomie` ^[angst-bei-komplexen-traumafolgen.md:#1]) at L53 and `Ebenen` (`Ebenen` ^[angst-bei-komplexen-traumafolgen.md:#1]) at L55. The manifest title, `Angst bei komplexen Traumafolgen` ^[angst-bei-komplexen-traumafolgen.md:#1], is not the H1; it stands once in the body as the words of a sentence at L25.

`Komplex` is three things under one string: an anatomical structure (`Amygdala-Komplex`, `basolateralen Komplex`, `zentrokortikomedialen Komplex`), the vagal branches (`ventrale Vagalkomplex`, `dorsale Vagalkomplex`, and `polyvagale Komplex` in the conclusion), and the adjective in `komplexe PTBS`. As a word alone `Komplex` ^[angst-bei-komplexen-traumafolgen.md:#4] stands four times, and 12 times with compounds. `Bindung` names attachment (`desorganisierten Bindungsstil`, `Bindungssystem`) and the bond of a `Trauma Bond` (`traumatischen Bindungen`); `Bindungstraumata` (L21, L177) is used without an explanation and without a link to `Trauma Bonds`. One numeral labels several series: the taxonomy's five headings, the three polyvagal states, the three treatment phases (`Phase 2` at L172 is the trauma-processing phase), the six treatment sections and the 75 references all count from 1, so a `2` can be a kind of anxiety, a vagal state, a phase, a section or a reference.

Damage in the text itself and in the export. The sentence at L51 reads „Dieser ständige Wechselbedingte Erschöpfung ist ein Kardinalsymptom der Störung.“ ^[L51], which is ungrammatical as written and is not export damage; quotations of it are verbatim. At L183 a Greek letter is missing from the drug class: „Prazosin ist ein stark lipophiler -Adrenorezeptor-Antagonist“ ^[L183], and no invisible character stands there. L187 calls the same action a „reine Alpha-1-Blockade“ ^[L187]. Reference 51 has a hyphenated word split by a space, „Traumafolge- störungen“ ^[L249], and reference 61 is a title set in a shifted font encoding, „%HUDWXQJV XQG 7KHUDSLHPDQXDO“ ^[L259], which decodes by a fixed offset of 29 code points to a German title beginning with `Beratungs`. None of the four changes a candidate's count.

Three candidates stand once each inside quotation marks, as a gloss or a borrowed phrase: `Normal-Sein-Wollen` glosses `Maskierung` (L73), `Disconnection` stands in a table cell (L115), and `schmutzige kleine Geheimnis` is a quoted phrase attributed to no one, which the sentence then explains (L162). The quoted sentences of patients and therapists (L69, L114, L116, L160) are diction and are not on the list. No candidate stands only inside a question: all 8 question marks the profile counts are in the reference list (L201, L207, L215, L224, L229, L236, L270, L272). No `N. term` and no term with a comma was on the list, so nothing was read as prose.

The row labels of the two tables (`Klinische Dimension`, `Beziehungsmuster`, `Verlassensangst`, `Impulsivität & Suizidalität`, `Emotionsregulation`, `Diagnostisches Kriterium`, `Kognitiver Fokus der Angst`, `Auslöser (Trigger)`, `Qualität der sozialen Angst`, `Natur des Hyperarousals`) are the axes of a comparison and are listed because a label heads a row; `Emotionsregulation` also stands twice in the treatment section, the others once. Whether an axis label is a term of the document or only the template of its tables is for the reading to say.
