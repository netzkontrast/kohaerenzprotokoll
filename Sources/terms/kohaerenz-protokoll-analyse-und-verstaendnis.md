---
source: Sources/drive/kohaerenz-protokoll-analyse-und-verstaendnis.md
drive_id: "1GehDbl2CIZIr7lJJ8sFWF3dymlckaSoLSdXyB2Yae4Q"
title: "Kohärenz Protokoll: Analyse und Verständnis"
category: kernkonzept
index_date: "2025-04-25"
extracted: "2026-10-12"
candidates: 51    # the terms capture.py counted
---

# Term census — Kohärenz Protokoll: Analyse und Verständnis

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py kohaerenz-protokoll-analyse-und-verstaendnis`

```
  lines                302  (frontmatter ends at 9)
  body words           5939
  headings             2   bold-only lines 33
  table rows           0   code fences 0
  question marks       10
  backslash escapes    8
  typographic marks    28   ascii quotes 32
  invisible characters U+200Bx10
  math symbol lines    0
  glued ref numbers    76
  repeated labels      none
  longest line         1259 chars
```

## Stance, read per passage

The document is an analytical report on cache coherence in computer systems, numbered in sections 1 to 8 with sub-sections; it names no figure, place or event of a novel world. It speaks in one register throughout: explanation, with a reference number glued to the end of many sentences.

**Opening (L13 to L29).** It states what it is about and what it will do. It reads `Kohärenz Protokoll` as a term of computer architecture: the term „wird im Deutschen primär im Kontext der Computerarchitektur verwendet“ ^[L17]. It announces its aim in its own words: „Das Ziel dieses Berichts ist es, eine umfassende technische Analyse von Cache-Kohärenzprotokollen zu liefern“ ^[L29].

**Scope (L25, L31 to L51).** It sets the word `Kohärenz` beside physics and signal processing and then narrows: „konzentriert sich dieser Bericht auf seine spezifische und kritische Anwendung in Computersystemen“ ^[L25]. Section 2 is a comparison of three disciplines, each given as a definition.

**Definition and mechanism passages (L53 to L87, L97 to L118).** Bold list labels such as „Vor- und Nachteile“ ^[L79] repeat under each mechanism; they are the report's template, not terms. The state names Modified, Exclusive, Shared and Invalid are given as bold labels with a one-letter form in brackets.

**Table (L120 to L152).** A transition table is announced: „Die folgende Tabelle fasst die wichtigsten Zustandsübergänge im MESI-Protokoll zusammen“ ^[L120]. It reaches the file as LaTeX source (`\\begin{tabular}`), not as a markdown table. Its note starts „Anmerkung“ ^[L148].

**Survey list (L154 to L176).** Variants and named protocols are listed one per bullet, each a short definition. The closing paragraph generalises: „Cache-Kohärenz kein abgeschlossenes Problem mit einer einzigen Universallösung ist“ ^[L176].

**Comparison and outlook (L178 to L230).** Two comparison sections set coherence beside memory consistency models and synchronisation primitives. Section 7 is a forward-looking survey; its last paragraph says: „Ein isoliertes Design der Kohärenzschicht erscheint angesichts der Komplexität moderner Systeme“ ^[L230] and the line goes on to call it not sufficient.

**Conclusion (L232 to L244).** It reports its own result: „Die Analyse hat gezeigt, dass der Begriff“ ^[L236] `Kohärenz Protokoll` equals the English `Cache Coherence Protocol` in computer science usage. It makes no claim of canon or authority for itself.

**References (L246 to L301).** The heading „Referenzen“ ^[L246] opens a numbered list of web and paper sources with an access date each. The sentences the report builds from them carry those numbers; the sources' own words are not in the document.

## Candidates and counts

51 candidates, written while reading and frozen by the count (`Plan/runs/kohaerenz-protokoll-analyse-und-verstaendnis/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `kohaerenz-protokoll-analyse-und-verstaendnis.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kohärenz Protokoll` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#3] | 3 | 3 | 13, 17, 236 |  |
| `Cache Coherence Protocol` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#7] | 7 | 9 | 17, 236, 251, 255, 262, 275, 283, 285 |  |
| `Cache-Kohärenz` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#21] | 21 | 36 | 13, 17, 21, 25, 29, 47, 49, 51, 59, 61, 69, 71 … | `Cache-Kohärenzprotokolle` ×10, `Cache-Kohärenzprotokollen` ×4, `Cache-Kohärenzprotokolls` ×1 |
| `Cache-Kohärenzprotokolle` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#10] | 10 | 14 | 17, 21, 29, 51, 59, 61, 69, 89, 91, 186, 196, 219 … | `Cache-Kohärenzprotokollen` ×4 |
| `Kohärenzprotokolle` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#5] | 5 | 25 | 11, 17, 21, 29, 51, 59, 61, 69, 89, 91, 163, 172 … | `Kohärenzprotokollen` ×6 |
| `Dateninkonsistenz` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#3] | 3 | 3 | 19, 21, 236 |  |
| `Shared Memory` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#2] | 2 | 2 | 29, 301 |  |
| `Cache-Zeile` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#14] | 14 | 17 | 63, 64, 78, 83, 91, 95, 104, 105, 106, 107, 117, 157 … | `Cache-Zeilen` ×3 |
| `Hauptspeicher` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#12] | 12 | 14 | 17, 21, 25, 63, 104, 105, 106, 107, 115, 157, 159, 201 | `Hauptspeichers` ×2 |
| `Interconnect` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#2] | 2 | 11 | 25, 64, 65, 77, 168, 176, 200, 208, 227, 230 | `Interconnects` ×3, `Interconnect-Netzwerk` ×2, `Interconnect-Topologie` ×2, `Interconnect-Medium` ×1 |
| `Snooping-basierte Protokolle` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#2] | 2 | 2 | 75, 236 |  |
| `Verzeichnis-basierte Protokolle` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#3] | 3 | 3 | 73, 81, 236 |  |
| `Directory` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#15] | 15 | 18 | 66, 81, 83, 84, 85, 87, 167, 169, 171, 236, 283, 285 | `Directory-based` ×1, `Directory-Verantwortung` ×1 |
| `Home Node` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1] | 1 | 1 | 84 |  |
| `Snoop-Filter` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1] | 1 | 2 | 87, 210 | `Snoop-Filtern` ×1 |
| `Zustandsverfolgung` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1] | 1 | 1 | 63 |  |
| `Kohärenz-Invarianten` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1] | 1 | 1 | 67 |  |
| `Write-Invalidate-Protokoll` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1] | 1 | 1 | 78 |  |
| `Write-Update-Protokoll` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1] | 1 | 1 | 78 |  |
| `MESI-Protokoll` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#5] | 5 | 6 | 63, 97, 99, 100, 111, 120 | `MESI-Protokolls` ×1 |
| `MESI` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#10] | 10 | 21 | 63, 78, 95, 97, 99, 100, 111, 120, 126, 152, 158, 159 … | `MESI-Protokoll` ×5, `MESIF` ×2, `MESI-Protokolls` ×1, `MESI-Zustandsübergangstabelle` ×1 |
| `MSI` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#6] | 6 | 7 | 78, 95, 99, 156, 157, 176, 240 |  |
| `MOSI` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#2] | 2 | 2 | 157, 158 |  |
| `MOESI` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#4] | 4 | 4 | 78, 95, 158, 240 |  |
| `MESIF` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#2] | 2 | 2 | 159, 240 |  |
| `Modified (M)` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#2] | 2 | 2 | 104, 138 |  |
| `Exclusive (E)` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#2] | 2 | 2 | 105, 140 |  |
| `Shared (S)` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#2] | 2 | 2 | 106, 142 |  |
| `Invalid (I)` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#2] | 2 | 2 | 107, 144 |  |
| `Bus Read (BusRd)` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1] | 1 | 1 | 115 |  |
| `Bus Read Exclusive (BusRdX)` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1] | 1 | 1 | 116 |  |
| `Flush / Writeback` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1] | 1 | 1 | 117 |  |
| `Invalidate Signal` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1] | 1 | 1 | 118 |  |
| `Token Coherence` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#3] | 3 | 3 | 165, 240, 263 |  |
| `Delta Coherence` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#3] | 3 | 3 | 166, 240, 291 |  |
| `Interconnect-Aware Protokolle` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1] | 1 | 1 | 168 |  |
| `WiDir` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#4] | 4 | 4 | 169, 227, 240, 285 |  |
| `POPS` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#2] | 2 | 2 | 170, 292 |  |
| `Rainbow` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#5] | 5 | 6 | 171, 210, 240, 286, 293 |  |
| `RCP` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#4] | 4 | 4 | 172, 219, 240, 295 |  |
| `Reversible Coherence Protocol` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#5] | 5 | 5 | 172, 219, 294, 295, 296 |  |
| `Ghostwriter` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#4] | 4 | 4 | 173, 225, 240, 275 |  |
| `SELCC` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#3] | 3 | 3 | 174, 226, 240 |  |
| `Speicherkonsistenzmodell` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1] | 1 | 3 | 180, 183, 240 | `Speicherkonsistenzmodelle` ×1, `Speicherkonsistenzmodellen` ×1 |
| `Synchronisationsprimitive` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#3] | 3 | 7 | 186, 189, 190, 192, 211, 240 | `Synchronisationsprimitiven` ×4 |
| `Approximative Kohärenz` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1] | 1 | 1 | 225 |  |
| `Kohärenz für disaggregierten Speicher` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1] | 1 | 1 | 226 |  |
| `Delegation` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#4] | 4 | 4 | 167, 170, 209 |  |
| `Dekohärenz` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1] | 1 | 1 | 37 |  |
| `Kohärenzfunktion` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#2] | 2 | 2 | 41, 45 |  |
| `Skalierbarkeitsengpässe` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#1] | 1 | 1 | 198 |  |

## What the extraction ran into

**Zeros:** 0.

**Standing alone less often than with compounds:** 15 — `Cache Coherence Protocol` 7/9, `Cache-Kohärenz` 21/36, `Cache-Kohärenzprotokolle` 10/14, `Kohärenzprotokolle` 5/25, `Cache-Zeile` 14/17, `Hauptspeicher` 12/14, `Interconnect` 2/11, `Directory` 15/18, `Snoop-Filter` 1/2, `MESI-Protokoll` 5/6, `MESI` 10/21, `MSI` 6/7, `Rainbow` 5/6, `Speicherkonsistenzmodell` 1/3, `Synchronisationsprimitive` 3/7.

Two facts from the draft, explained below. The first fact: the document has no zero, because every candidate was checked with `read.py --find` against its line before the count. The second: the 15 terms that stand alone less often than with compounds are inflections and compounds, not different things. `Kohärenzprotokolle` stands alone 5 times and 25 times with compounds, because the document mostly writes the compound `Cache-Kohärenzprotokolle` and the dative plural `Kohärenzprotokollen`. Likewise `Cache-Kohärenz` stands alone 21 times against 36 with compounds, the others being `Cache-Kohärenzprotokolle` and its inflected forms. `Interconnect` stands alone 2 times against 11 with compounds such as `Interconnect-Netzwerk`, `Interconnect-Topologie` and the plural `Interconnects`. `Synchronisationsprimitive`, `Speicherkonsistenzmodell` and `Snoop-Filter` appear in the plural or dative plural as well.

Export artifacts. The export glues reference numbers to the end of sentences (76 such spots in the profile), for example the digit after `Cache Coherence Protocol` in L17; a quotation therefore has to stop before the glued digit. The formulas of section 2.2 lost their symbols: L45 reads „zwischen und“ ^[L45] where the report gave the values 0 and 1. The table of section 5.2 is LaTeX source (L122 to L150) and its backslashes are doubled by the export. There are ten zero-width characters. The reference list has `Zugriff am April` ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:#54] times, one per entry, and the digits of the access date are lost in the export. Reference 15 (L262) shows a doubled title where the export dropped a symbol.

Candidate scope. The report's own terms are English and German mixed: protocol names (`MESI`, `Token Coherence`, `Ghostwriter`) are written in English inside German sentences, and the German section labels (`Snooping-basierte Protokolle`, `Verzeichnis-basierte Protokolle`) are headings. `Hemiola` is named in L215 as a framework and left off the list as a one-time citation of a tool. The physics and signal-processing uses of `Kohärenz` (sections 2.1 and 2.2) are borrowed concepts the report names only to separate them from its subject; `Dekohärenz` and `Kohärenzfunktion` are listed as the words it writes there.

Standing. The report claims no authority beyond being an analysis (L29, L236); it contains no label such as canon, lock or decision.
