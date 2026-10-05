---
source: Sources/drive/kohaerenz-protokoll-projekt-rekonstruktion.md
drive_id: "1eFcWv-ocVo0YkB28wS-ZjsG91iSupow3dHfygifsK0M"
title: "Kohärenz Protokoll: Projekt-Rekonstruktion"
category: audit
index_date: "2026-03-26"
extracted: "2026-10-05"
candidates: 125    # the terms capture.py counted
---

# Term census — Kohärenz Protokoll: Projekt-Rekonstruktion

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py kohaerenz-protokoll-projekt-rekonstruktion`

```
  lines                328  (frontmatter ends at 0)
  body words           4889
  headings             26   bold-only lines 5
  table rows           54   code fences 0
  question marks       20
  backslash escapes    79
  typographic marks    89   ascii quotes 36
  invisible characters none
  math symbol lines    0
  glued ref numbers    19
  repeated labels      AI-Partner x5, Datum x5, Entscheidungen (Ja) x5, Kernthemen x5, Status x5
  longest line         1106 chars
```

## Stance, read per passage

The document is one report that speaks as an inventory and ends in three documents it generates itself. Observed: the census category is `audit`, as the manifest gives it; the text calls itself a report (L7).

L1 to L9, report and mandate: the text calls itself „Der vorliegende Bericht operiert als exakte Ausführung dieses Auftrags“ ^[L7] and says it „etabliert eine verbindliche, kanonische Wahrheit („Golden Sources“)“ ^[L7].

L11 to L43, report of method, then a register of sources: the method is „Dateinamen-Suchen, Volltext-Analysen und Ordner-Traversierungen“ ^[L13]. The register lists the sources as Q-01 to Q-16, each with a type, a date and a decision column; every date in it reads „Unbestimmt“ ^[L28]. The text gives the reason: „Da exakte Erstellungsdaten in den Metadaten fehlen“ ^[L17].

L45 to L126, synthesis in the present tense. It restates what its sources are said to contain; the numbers glued to its sentences in the export are the footnote numbers of the reference list at L316 to L327. It marks one of its findings against an assumption: „Entgegen der Annahme, das Projekt befinde sich in einem rein konzeptionellen Stadium“ ^[L114].

L128 to L193, lock: three embedded documents, the first headed `CANON STATE`. The text says they act as „verbindliche Wahrheit“ ^[L130] and „lösen jegliche historischen Widersprüche endgültig auf“ ^[L130]. Its two tables are headed `HARD CANON — Unveränderlich` (L138) and `SOFT CANON — Bestätigt, aber nuancierbar` (L158), with rows coded HC- and SC- and a column `Primärquelle`.

L195 to L259, questions: `OFFENE FRAGEN`, sorted under the headings `KRITISCH`, `WICHTIG` and `NICE-TO-HAVE` (L199, L225, L241), each as `OQ-nn` with a `Spezifikation` and an `Impact-Analyse`. The closing section reports one question answered: „Vollständig gelöst.“ ^[L259] under `Status OQ-02`.

L261 to L308, history, reconstructed: `SESSION-HISTORIE` with five phases, each with the labels `Datum`, `AI-Partner`, `Kernthemen`, `Entscheidungen (Ja)` and `Status`. It says of itself: „Aufgrund fehlender Zeitstempel in originären Drive-Dokumenten wurde die Historie anhand logischer Abhängigkeiten der Architekturentwicklungen iterativ rekonstruiert.“ ^[L265]. The phase it calls the current intervention is dated 2026-03-26 (L303) and carries the status „Abgeschlossen mit der Publikation dieses Synthese-Berichts“ ^[L308].

L310 to L314, recommendation and standing: „Die dargelegten Golden-Source-Dokumente stellen ab sofort die alleinige, verbindliche Architektur“ ^[L314] for all later writing. This is the document's claim about its own standing; it is recorded and applied to nothing.

L316 to L327, references: ten numbered titles with Drive links.

## Candidates and counts

125 candidates, written while reading and frozen by the count (`Plan/runs/kohaerenz-protokoll-projekt-rekonstruktion/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `kohaerenz-protokoll-projekt-rekonstruktion.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kohärenz Protokoll` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#9] | 9 | 11 | 1, 5, 21, 47, 96, 132, 195, 261, 322, 326, 327 |  |
| `Kohärenz Protokolls` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 21, 96 |  |
| `System Kael` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#4] | 4 | 4 | 5, 33, 214, 321 |  |
| `NovelOS` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#3] | 3 | 5 | 7, 36, 130, 304, 314 | `NovelOS-Frameworks` ×1, `NovelOS-Protokolls` ×1 |
| `NovelOS-Framework` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#0] | 0 | 1 | 130 | `NovelOS-Frameworks` ×1 |
| `Context Rot` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#3] | 3 | 3 | 5, 36, 305 |  |
| `Golden Sources` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#4] | 4 | 4 | 7, 128, 305, 306 |  |
| `Golden-Source-Dokumente` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 9, 314 |  |
| `K-Juna-Paradoxon` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 2 | 7, 33 | `K-Juna-Paradoxons` ×1 |
| `AEGIS` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#38] | 38 | 44 | 7, 28, 31, 37, 53, 55, 70, 72, 82, 88, 100, 107 … | `AEGIS-Subplots` ×2, `AEGIS-Evolution` ×1, `AEGIS-Ende` ×1, `AEGIS-Log` ×1 |
| `Kael` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#21] | 21 | 34 | 5, 28, 33, 41, 43, 53, 55, 63, 65, 66, 72, 76 … | `Kaels` ×12, `Kael-System` ×1 |
| `Juna` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#16] | 16 | 19 | 7, 33, 55, 90, 101, 118, 151, 155, 163, 192, 201, 205 … | `Junas` ×1 |
| `Hard Canon` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#5] | 5 | 5 | 21, 49, 51, 61, 275 |  |
| `Soft Canon` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#4] | 4 | 4 | 21, 59, 61, 257 |  |
| `Moonshine-Link` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 3 | 30, 55, 255 | `Moonshine-Links` ×1 |
| `The Foundation` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 30, 255 |  |
| `Foundation-Code` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#0] | 0 | 1 | 205 | `Foundation-Codes` ×1 |
| `External Level` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 30 |  |
| `Nichts Rauschen` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 57, 154 |  |
| `ontologische Vertigo` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 57, 154 |  |
| `Algorithmische Melancholie` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 144, 223 |  |
| `Algorithmischen Melancholie` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 53 |  |
| `pathologisches Lernen` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 53 |  |
| `parakonsistente Logik` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 53 |  |
| `Syntaxfehler` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 55 |  |
| `Zombie-System` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 53 |  |
| `tragischer Gott` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 53 |  |
| `tragischer Schöpfergott` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 156 |  |
| `Der Juna/V-Exploit` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 155 |  |
| `ontologischen Exploit` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 55 |  |
| `Kernwelten` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#3] | 3 | 3 | 31, 61, 282 |  |
| `Core Worlds` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 61 |  |
| `KW1` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#7] | 7 | 8 | 31, 65, 84, 107, 165, 176, 282 |  |
| `KW2` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#4] | 4 | 4 | 66, 165, 215, 247 |  |
| `KW3` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#3] | 3 | 3 | 67, 89, 165 |  |
| `KW4` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#3] | 3 | 4 | 31, 68, 165, 282 |  |
| `Logos-Prime` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#4] | 4 | 4 | 65, 80, 192, 231 |  |
| `Mnemosyne-Archipel` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 66, 215 |  |
| `Die Grenzfeste / Cerberus-Labyrinth` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 67 |  |
| `Cerberus-Labyrinth` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 67, 89 |  |
| `Kairos-Potentialis` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 68 |  |
| `LogOS` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#3] | 3 | 3 | 65, 152, 166 | `Logos-Prime` ×4 |
| `Mnemosyne` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#3] | 3 | 5 | 66, 152, 166, 215 | `Mnemosyne-Archipel` ×2 |
| `Cerberus` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 4 | 67, 89, 166 | `Cerberus-Labyrinth` ×2 |
| `Kairos` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 2 | 68, 166 | `Kairos-Potentialis` ×1 |
| `Sophia` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 166 |  |
| `Guardians` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#3] | 3 | 3 | 72, 152, 166 |  |
| `Guardian LogOS` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 65 |  |
| `Konstrukt-Stadt` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 108 |  |
| `dialethische Logik` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 68 |  |
| `akustischer Druck ohne Ton` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 70 |  |
| `Ästhetik der Ohnmacht` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 70 |  |
| `Alters` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#9] | 9 | 13 | 35, 43, 74, 78, 143, 146, 168, 185, 214, 243, 274, 289 |  |
| `Alter-Topografie` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 306 |  |
| `Peripherie-Alters` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 243 |  |
| `Anscheinend Normale Persönlichkeitsanteile` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#3] | 3 | 3 | 35, 65, 78 |  |
| `ANP` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#5] | 5 | 9 | 35, 65, 78, 80, 81, 84, 86, 92, 122 |  |
| `Emotionale Persönlichkeitsanteile` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 35, 78 |  |
| `EP` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#5] | 5 | 6 | 35, 78, 83, 92, 179, 259 |  |
| `funktionale Multiplizität` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 147 |  |
| `funktionalen Multiplizität` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 76 |  |
| `Der Suchende / Host` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 80 |  |
| `Der Architekt` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 81 |  |
| `Der Wächter (Alex)` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 82 |  |
| `Das Kind (Echo / EP)` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 83 |  |
| `Der Analytiker (Lex / ANP)` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 84 |  |
| `Die Schatten-Instanz (Nyx / Persecutor)` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 85 |  |
| `Der Beobachter (Argus / ANP)` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 86 |  |
| `Der Vermittler` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 87 |  |
| `Die Erinnerungs-Säule` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 88 |  |
| `Der Taktiker` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 89 |  |
| `Das Fragment (V-Bezug)` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 90 |  |
| `Archivar der Narben` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 86, 184 |  |
| `Silas` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#6] | 6 | 7 | 40, 78, 184, 259, 290 | `Silas-Funktion` ×1 |
| `Lex` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#5] | 5 | 5 | 43, 84, 123, 168, 274 |  |
| `Alex` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#5] | 5 | 5 | 43, 82, 123, 168, 274 |  |
| `Echo` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#8] | 8 | 8 | 43, 83, 110, 117, 168, 191, 274 |  |
| `Nyx` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#4] | 4 | 4 | 43, 85, 168, 184 |  |
| `Argus` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#11] | 11 | 11 | 35, 40, 43, 78, 86, 168, 184, 259, 290 |  |
| `Moros` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#4] | 4 | 4 | 35, 92, 247, 259 |  |
| `Rhys` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#5] | 5 | 5 | 39, 92, 247, 325 |  |
| `Selene` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 35, 92 |  |
| `Lia` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 243, 247 |  |
| `Oblivion` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#4] | 4 | 5 | 41, 80, 243, 247, 259 | `Oblivion-Zustand` ×1 |
| `Oblivion-Zustand` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 80 |  |
| `Universal Reboot` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 41, 80 |  |
| `Kudzu-Metapher` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 39 |  |
| `Dual-Kernel-Theorie` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#5] | 5 | 5 | 32, 84, 98, 164, 281 |  |
| `DKT` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 32, 98 |  |
| `Kernel` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 9 | 32, 84, 98, 100, 101, 164, 281, 318 |  |
| `Narrative Hard Rules` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 96, 171 |  |
| `thermische Risse` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 151, 176 |  |
| `Landauer-Risse` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 231 |  |
| `Quanten-Unitarität` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 178 |  |
| `Schwarzschild-Protokoll` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 110, 179 |  |
| `Bekenstein-Schranke` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#3] | 3 | 3 | 109, 180, 281 |  |
| `Unsichtbares Panoptikum` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 169 |  |
| `unsichtbares Panoptikum` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 72, 290 |  |
| `Entropie-Fehler` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 37 |  |
| `Existenzielle Fusion` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 186 |  |
| `Foreshadowing-System` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 120 |  |
| `Resonanzmatrix` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 124 |  |
| `Therapeutische Isomorphie` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 126 |  |
| `Host-ANP` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 122 |  |
| `Genesis im Echo der Leere` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 117, 191 |  |
| `Instrumente der Ordnung` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 118, 192 |  |
| `Vorwort` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#4] | 4 | 4 | 42, 116, 190, 297 |  |
| `Prolog` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#3] | 3 | 4 | 42, 117, 191, 297 |  |
| `ENTSCHEIDUNGS-LOG` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 182 |  |
| `neue Kohärenz` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 223 |  |
| `Heldinnenreise` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 33 |  |
| `Architectural Storytelling` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 108 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `TSDP` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#4] | 4 | 8 | 5, 28, 72, 76, 126, 143, 273, 274 | `TSDP-Modells` ×1, `TSDP-Zustand` ×1, `TSDP-Behandlung` ×1, `TSDP-Systems` ×1 |
| `Theorie der strukturellen Dissoziation der Persönlichkeit` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 76 |  |
| `IFS` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#0] | 0 | 3 | 28, 143, 273 |  |
| `Internal Family Systems` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 143 |  |
| `Landauer-Prinzip` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 4 | 32, 107, 176, 281 | `Landauer-Prinzips` ×2 |
| `Gödelsche Unvollständigkeitssatz` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 108 |  |
| `Gödelsche Unvollständigkeit` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 2 | 108, 177 |  |
| `Quantenverschränkung` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#2] | 2 | 2 | 55, 155 |  |
| `Prehension` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 55 |  |
| `Alfred North Whiteheads` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 55 |  |
| `Depersonalisation` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 86 |  |
| `ergodische Strukturen` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 149 |  |
| `Persecutor` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] | 1 | 1 | 85 |  |

## What the extraction ran into

**Zeros, three, all inflection or compound, none an absence.** `NovelOS-Framework` stands 0 times alone because the line writes it with an ending: `NovelOS-Frameworks` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] (L130). `Foundation-Code` likewise: `Foundation-Codes` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] (L205). `IFS` stands alone 0 times; the document writes it only as the first part of a compound, `IFS-Integration` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] (L28) and `IFS-Therapiemodells` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] (L273), and spells it out once at L143 (`Internal Family Systems` is on the list).

**Standing alone less often than with compounds (22 terms).** Each is a name the document also carries into a compound or an inflection: `AEGIS` into `AEGIS-Subplots` and others, `Kael` into `Kaels`, `TSDP` into `TSDP-Modells` and three more, `Landauer-Prinzip` into `Landauer-Prinzips`. `Kernel` is marked as a substring by the count: it stands 2 times alone and 9 times anywhere, because the kernels are written `-Kernel` after a lost symbol and inside `Dual-Kernel-Theorie`; L318 is the title of a reference.

**Export damage, observed.** The export lost symbols: the two kernel symbols are missing at L32, L100, L101 and L103, and the line reads `Der -Kernel (Kohärenz)` ^[L100]. A list cannot write a symbol the line does not hold. Digits glued to words were dropped when lines are shown through `read.py --find` (the list writes `KW1` to `KW4` as the count finds them). The glued reference numbers (19 in the profile) are footnote numbers. Backslash escapes (79) stand in the tables' header cells and in `CANON\_STATE` (L306). The heading at L199 has two damaged characters in front of `KRITISCH`. Two tables have an empty header row (L25, L140).

**Repeated labels.** `AI-Partner`, `Datum`, `Entscheidungen (Ja)`, `Kernthemen` and `Status` each stand five times as the profile says: they are the five fields of each of the five history phases (L269 to L308), a template and not terms.

**Row codes.** The register and the tables carry the codes Q-, HC-, SC- and OQ- as row labels. They are the document's own labels and are not on the list.

**A name in two forms.** The Alters are written as a role and a name: `Der Wächter (Alex)` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1], `Das Kind (Echo / EP)` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1]. Both forms are listed, and each name stands alone as well (`Lex` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#5], `Alex` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#5]). `Der Juna/V-Exploit` ^[kohaerenz-protokoll-projekt-rekonstruktion.md:#1] joins two names with a slash.

**Other sources by title only.** The register names sixteen sources by title and the reference list ten; the titles are not on the list, nor are the Drive links.

**Zeros:** 3 — `NovelOS-Framework`, `Foundation-Code`, `IFS`.

**Standing alone less often than with compounds:** 22 — `Kohärenz Protokoll` 9/11, `NovelOS` 3/5, `K-Juna-Paradoxon` 1/2, `AEGIS` 38/44, `Kael` 21/34, `Juna` 16/19, `Moonshine-Link` 2/3, `KW1` 7/8, `KW4` 3/4, `Mnemosyne` 3/5, `Cerberus` 2/4, `Kairos` 1/2, `Alters` 9/13, `ANP` 5/9, `EP` 5/6, `Silas` 6/7, `Oblivion` 4/5, `Kernel` 2/9, `Prolog` 3/4, `TSDP` 4/8, `Landauer-Prinzip` 2/4, `Gödelsche Unvollständigkeit` 1/2.
