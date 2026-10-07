---
source: Sources/drive/roman-outline-kohaerenz-protokoll-uberarbeitung.md
drive_id: "12hA4-J_RYymH6KtEzTGbPx8Q_gH5b9QVZCWowHh9Eac"
title: "Roman-Outline: Kohärenz Protokoll Überarbeitung"
category: plot-outline
index_date: "2025-05-03"
extracted: "2026-10-07"
candidates: 96    # the terms capture.py counted
---

# Term census — Roman-Outline: Kohärenz Protokoll Überarbeitung

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py roman-outline-kohaerenz-protokoll-uberarbeitung`

```
  lines                400  (frontmatter ends at 9)
  body words           8770
  headings             27   bold-only lines 10
  table rows           29   code fences 0
  question marks       29
  backslash escapes    117
  typographic marks    108   ascii quotes 8
  invisible characters none
  math symbol lines    0
  glued ref numbers    39
  repeated labels      Ziel x13, Narrative Anwendung x6, Anwendung x4, Schlüsselkonzepte x4
  longest line         1315 chars
```

## Stance, read per passage

The document is a report about a novel outline, not the outline itself, and it speaks in four registers.

**Report on its own purpose and method.** The opening sections state what the report is for: „Dieser Bericht erläutert die multidisziplinäre Forschungsbasis“ ^[L17] and the method, which lists „bei Bedarf proaktive Recherchen (impliziert)“ ^[L21] among its steps, so one step is marked as implied and not as done. The headings `Zweckbestimmung`, `Methodik` and `Struktur des Berichts` carry this register (L15 to L25).

**Section announcements.** Each main section opens with a sentence saying what it does: „Dieser Abschnitt detailliert“ ^[L29], „Dieser Abschnitt verankert die Kernideen der Erzählung“ ^[L152], „Dieser Abschnitt verdeutlicht“ ^[L242].

**A repeated template per subsection (plan).** Every subsection of II to IV is built from labels: a `Ziel:` line (the profile counts 13 repeated `Ziel` labels), a `Kerntheorie` or `Schlüsselkonzepte` list, a `Narrative Anwendung` or `Anwendung` block. An example is „Kerntheorie: Prinzipien des Cosmic Horror“ ^[L69]. These labels name fields of the template, not terms of the novel's world; the narrative-application blocks describe what the outline does or is to do, in the present tense of a plan.

**Tables.** Three tables carry the headings „Tabelle: TSDP Phobien in Kaels Reise“ ^[L41], „Tabelle: Murdocks Heroine's Journey Stufen vs. Kaels Handlungsbogen“ ^[L108] and „Tabelle: AEGIS' Alignment-Fehler & Systemische Merkmale“ ^[L189] (the file writes them with their numbers, 1 to 3, and the quotation check drops a digit after a word; the tables are pipe rows whose header cells carry escaped doubled asterisks). Table 1 matches a theory's phobia to a manifestation in the novel, with chapters; one cell marks its own inference with „(implizit)“ ^[L51].

**Derivation paragraphs.** Below each block, long paragraphs argue a link between two frameworks, often with a closing „Daher“ and inline bracket tags such as `[Kontext]`, `[Glossar]` and `[Ch 8]` that point at other material, not at this text. Hedged wording marks them as proposals: „Kaels Reise ist möglicherweise nicht rein linear“ ^[L130].

**Closing claim of standing.** The conclusion calls the revised outline a base and its decisions founded: „Das überarbeitete Outline“ ^[L298] is said there to offer „eine starke und kohärente Grundlage“ ^[L298]. That is the document's own claim about its work and is recorded here, not applied.

**Reference list.** From L302 the document lists 98 numbered web references, each ending with the access date and a URL. Their titles name theories and are not terms of the novel.

## Candidates and counts

96 candidates, written while reading and frozen by the count (`Plan/runs/roman-outline-kohaerenz-protokoll-uberarbeitung/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `roman-outline-kohaerenz-protokoll-uberarbeitung.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kohärenz Protokoll` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#4] | 4 | 4 | 11, 17, 280, 298 |  |
| `AEGIS` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#116] | 116 | 116 | 37, 51, 52, 63, 67, 71, 75, 77, 78, 80, 82, 90 … |  |
| `Kael` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#46] | 46 | 125 | 31, 33, 37, 39, 41, 47, 48, 51, 52, 56, 57, 61 … | `Kaels` ×78, `Kael-Anteils` ×1 |
| `Juna/V` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#16] | 16 | 17 | 51, 67, 71, 75, 77, 80, 90, 93, 197, 198, 208, 214 … | `Juna/Vs` ×1 |
| `Fundament` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#16] | 16 | 18 | 67, 71, 75, 77, 78, 80, 90, 120, 166, 168, 208, 214 … | `fundamental` ×3, `Fundaments` ×2 |
| `Überwelt` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#2] | 2 | 2 | 166, 248 |  |
| `KW1` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#5] | 5 | 5 | 48, 76, 96, 115, 256 |  |
| `KW2` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#7] | 7 | 7 | 48, 63, 76, 96, 120, 266 |  |
| `KW3` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#6] | 6 | 6 | 76, 93, 96, 197, 256 |  |
| `KW4` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 199 |  |
| `Guardians` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#11] | 11 | 11 | 93, 94, 96, 117, 161, 166, 180, 187, 197 |  |
| `Selene` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#11] | 11 | 12 | 115, 121, 123, 124, 128, 148, 230, 231, 234, 236 | `Selenes` ×1 |
| `Lex` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#9] | 9 | 9 | 49, 50, 61, 116, 123, 128, 142, 220 |  |
| `Alex` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#7] | 7 | 7 | 50, 61, 116, 123, 128, 220 |  |
| `Nyx` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 123 |  |
| `Rhys` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#4] | 4 | 4 | 51, 142, 220 |  |
| `Kiko` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 122 |  |
| `Lia` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 122 |  |
| `Moros` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 122 |  |
| `Echo` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 199 |  |
| `Prolog` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#6] | 6 | 6 | 37, 76, 115, 187, 196, 199 |  |
| `Nichts Rauschen` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 76 |  |
| `Fehlausgerichtete Kohärenz` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#5] | 5 | 5 | 143, 187, 202, 222, 287 |  |
| `Kohärenz` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#23] | 23 | 24 | 11, 17, 82, 96, 143, 146, 148, 179, 181, 182, 187, 196 … | `Kohärenz-Protokoll` ×1 |
| `ANPs` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#14] | 14 | 14 | 37, 49, 50, 59, 61, 80, 123, 220, 236, 266 |  |
| `EPs` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#16] | 16 | 16 | 37, 50, 61, 80, 122, 214, 220, 236, 266 |  |
| `ANP` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 18 | 37, 48, 49, 50, 59, 61, 63, 80, 123, 220, 236, 266 |  |
| `EP` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 23 | 37, 48, 49, 50, 51, 59, 61, 63, 80, 122, 214, 220 … |  |
| `Swift Switching` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 57 |  |
| `funktionaler Multiplizität` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#3] | 3 | 3 | 52, 128, 148 |  |
| `Akt 1` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#6] | 6 | 6 | 63, 115, 117, 119, 204 |  |
| `Akt 2` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#12] | 12 | 12 | 63, 94, 118, 184, 187, 204, 238 |  |
| `Akt 3` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#4] | 4 | 4 | 63, 142, 232 |  |
| `Drei-Akt-Struktur` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 63 |  |
| `Phobie vor traumatischen Erinnerungen` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#2] | 2 | 2 | 48, 80 |  |
| `Phobie vor mentalen Inhalten` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 49 |  |
| `Phobie vor dissoziativen Anteilen` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#2] | 2 | 2 | 50, 61 |  |
| `Phobie vor Bindung/Bindungsverlust` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 51 |  |
| `Phobie vor normalem Leben/Risiko/Veränderung/Intimität` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 52 |  |
| `Anscheinend Normale Persönlichkeitsanteile` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 37 |  |
| `Emotionale Persönlichkeitsanteile` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 37 |  |
| `Begrenzte Perspektive` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 56 |  |
| `Andeutung statt Offenbarung` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 75 |  |
| `Zeigen statt Erklären` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 59 |  |
| `Informationskontrolle` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#2] | 2 | 2 | 92, 256 |  |
| `Psychologische Kriegsführung` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#2] | 2 | 2 | 93, 96 |  |
| `Kernparadoxon` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#3] | 3 | 3 | 96, 146, 199 |  |
| `Narrative Anwendung` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#6] | 6 | 6 | 73, 140, 166, 187, 218, 234 |  |
| `Schlüsselkonzepte` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#4] | 4 | 5 | 21, 158, 176, 210, 228 | `Schlüsselkonzepten` ×1 |
| `Schlüsselkapitel` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#3] | 3 | 3 | 47, 114, 195 |  |
| `Kerntheorie` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#4] | 4 | 4 | 35, 69, 104, 136 |  |
| `Kerntechniken` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 88 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Theorie der Strukturellen Dissoziation der Persönlichkeit` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#2] | 2 | 2 | 35, 286 |  |
| `TSDP` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#23] | 23 | 30 | 17, 35, 37, 39, 41, 47, 52, 61, 63, 80, 98, 130 … | `TSDP-Forschung` ×1, `TSDP-Phobie` ×1, `TSDP-Struktur` ×1, `TSDP-Vulnerabilitäten` ×1 |
| `Cosmic Horror` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#16] | 16 | 16 | 17, 65, 69, 71, 80, 260, 266, 280, 290, 294, 310, 311 … |  |
| `Heroine's Journey` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#13] | 13 | 13 | 17, 100, 104, 108, 130, 168, 236, 280, 288, 329, 330, 331 … |  |
| `Trügerischer Segen des Erfolgs` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#2] | 2 | 2 | 118, 130 |  |
| `Heilung des verwundeten Männlichen im Inneren` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#2] | 2 | 2 | 123, 128 |  |
| `Weibliche Wunde` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 122 |  |
| `Kognitive Dissonanz` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#3] | 3 | 3 | 136, 138, 146 |  |
| `Gaslighting` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#8] | 8 | 8 | 91, 93, 98, 146, 200, 256 |  |
| `Foreshadowing & Misdirection` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 90 |  |
| `Persönliche Identität` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 160 |  |
| `Hard Problem` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 161 |  |
| `Simulationshypothese` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#2] | 2 | 2 | 162, 272 |  |
| `Matrix als Metaphysik` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#3] | 3 | 3 | 163, 168, 289 |  |
| `It from Bit` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 164 |  |
| `KI-Alignment-Problem` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 178 |  |
| `Outer Alignment` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 178 |  |
| `Inner Alignment` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 178 |  |
| `Ziel-Fehlspezifikation` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#2] | 2 | 2 | 179, 196 |  |
| `Goodhart's Law` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#2] | 2 | 2 | 179, 196 |  |
| `Instrumentelle Konvergenz` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#2] | 2 | 2 | 180, 197 |  |
| `Reward Hacking` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 181 |  |
| `Deceptive Alignment` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#2] | 2 | 2 | 182, 200 |  |
| `Systemtheorie/Kybernetik` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#2] | 2 | 2 | 183, 248 |  |
| `Kybernetik zweiter Ordnung` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#3] | 3 | 3 | 184, 204 |  |
| `Kybernetik erster Ordnung` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 204 |  |
| `Luhmanns Soziale Systemtheorie` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 185 |  |
| `Autopoiesis` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 185 |  |
| `Operationale Geschlossenheit` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 198 |  |
| `KI-Ethik` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 2 | 212, 218 | `KI-Ethikprinzipien` ×1 |
| `Problem des Anderen` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 214 |  |
| `Paradoxon der Toleranz` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#4] | 4 | 4 | 215, 218, 222, 272 |  |
| `Philosophie der Ordnung` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 216 |  |
| `Potentialität (Dunamis)` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 230 |  |
| `Aktualität (Energeia)` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 230 |  |
| `Unbewegte Beweger` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 230 |  |
| `Entelechie` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 236 |  |
| `Komplexitätstheorie` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 231 |  |
| `Emergenz` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#11] | 11 | 11 | 124, 143, 174, 187, 199, 222, 226, 231, 234, 272 |  |
| `Selbstorganisation` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#4] | 4 | 4 | 226, 231, 234 |  |
| `Systemische Interventionskonzepte` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#1] | 1 | 1 | 232 |  |
| `Hard Science Fiction` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#2] | 2 | 2 | 244, 294 |  |
| `Psychological Thriller` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#4] | 4 | 4 | 84, 252, 290, 294 |  |
| `Philosophische Fiktion` ^[roman-outline-kohaerenz-protokoll-uberarbeitung.md:#2] | 2 | 2 | 268, 294 |  |

## What the extraction ran into

Zeros: none. Every one of the 96 listed surfaces stands at least once as written, so the reader's spellings, checked with `read.py --find` before the count, all hold.

Ten terms stand alone less often than inside compounds or inflections, and each gap is an inflection or a compound, not damage:

- `Kael` 46 alone against 125 anywhere: the genitive `Kaels` stands 78 times, and `Kael-Anteils` once.
- `Juna/V` 16 against 17: the genitive `Juna/Vs` once.
- `Fundament` 16 against 18: `Fundaments` twice; `fundamental` three times is another word that only contains the string.
- `Selene` 11 against 12: `Selenes` once.
- `Kohärenz` 23 against 24: `Kohärenz-Protokoll` once, in a question about AEGIS, as a compound that is not the novel's title: „heimlich sein fehlerhaftes Kohärenz-Protokoll verfolgt“ ^[L182].
- `ANP` 1 against 18: the plural `ANPs` carries the term (14 times alone); the singular stands once in the table cell on L48, and the rest are compounds such as `ANP-Konflikt`.
- `EP` 1 against 23: the plural `EPs` carries the term (16 times alone); the compounds are `EP-Inhalte`, `EP-Bindung`, `EP-Intrusionen`, `EP-Begegnungen` and `EP-Erinnerungen`. The count of `in` 23 also contains the letters EP inside other words.
- `Schlüsselkonzepte` 4 against 5: the dative `Schlüsselkonzepten` once.
- `TSDP` 23 against 30: the compounds `TSDP-Forschung`, `TSDP-Phobie`, `TSDP-Struktur` and `TSDP-Vulnerabilitäten`.
- `KI-Ethik` 1 against 2: the compound `KI-Ethikprinzipien` once.

**Export damage the reading met.** The profile reports 117 backslash escapes and 39 glued reference numbers: footnote numbers stand glued to words and sentences (for example „AEGIS' Einsatz von Techniken der psychologischen Kriegsführung“ ^[L96] is followed by the reference number 20 in the line), and the table header cells are wrapped in escaped doubled asterisks. Chapter references are written `Ch 8`, `Ch 5-6` or `Kapitel 21` and are not candidates here.

**Spellings kept as written.** The novel's worlds are written `KW1` to `KW4` with plain digits; the document never writes a subscripted form and never spells the abbreviation out, so what `KW` names is for reconciliation to ask. `ANP` and `EP` are spelled out once each, on L37: „Anscheinend Normale Persönlichkeitsanteile“ ^[L37] and „Emotionale Persönlichkeitsanteile“ ^[L37]. The theory is spelled out on L35 and again on L286, and is otherwise written `TSDP`. A compound candidate with a slash (`Phobie vor Bindung/Bindungsverlust`, `Systemtheorie/Kybernetik`, `Juna/V`) is listed as one form because the document writes it as one name.

**Quoted words belong to the theories.** Names inside the lens list (the five stages and phobias of the theories, `Goodhart's Law`, `Reward Hacking`) are the theories' own words as the document reports them, and only their application to Kael or AEGIS is the document's.

**The document's claim about its own standing.** It describes itself as a research report behind the outline and calls its decisions founded (L298, quoted above). The claim is recorded and decides nothing here.

**Absence checked.** The document does not write `Glossar` as a heading. It writes it once, in an inline bracket tag pointing at material outside this text (`[Glossar]`, L96), and `Kontext` stands 8 times as a bracket tag; the material they point at is not in front of this reading, so what it says about AEGIS in those places rests on a source the document does not quote.

**Zeros:** 0.

**Standing alone less often than with compounds:** 10 — `Kael` 46/125, `Juna/V` 16/17, `Fundament` 16/18, `Selene` 11/12, `Kohärenz` 23/24, `ANP` 1/18, `EP` 1/23, `Schlüsselkonzepte` 4/5, `TSDP` 23/30, `KI-Ethik` 1/2.
