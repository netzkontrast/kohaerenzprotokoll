---
source: Sources/drive/kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md
drive_id: "1qD41Bh12bM9tbu_v2IauIE3ngq5_H5PIGXbhsO8CVbg"
title: "kohaerenz-protokoll_welt-sensorik-drafting_2026-06-10.md"
category: worldbuilding
index_date: "2026-06-10"
extracted: "2026-09-25"
candidates: 1084
---

# Term census — kohaerenz-protokoll_welt-sensorik-drafting_2026-06-10.md

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md`

```
  lines                1503  (frontmatter ends at 9)
  body words           7655
  headings             62   bold-only lines 19
  table rows           246   code fences 0
  question marks       52
  backslash escapes    1172
  typographic marks    167   ascii quotes 50
  invisible characters none
  math symbol lines    16
  glued ref numbers    48
  repeated labels      none
  longest line         754 chars
```

**A drafting manual in fourteen sections, mostly tables.** §1 describes six
levels — KW1 to KW4, the Überwelt and the Externe Ebene — each on the same
fields (Konzept, Akt-Dominanz, Ästhetik, Sensorik, Logik, Stilebene,
Somatik-Default, Risse, Sub-Lokalitäten); §2 the sensory library and the
thermal rule; §3 two typologies of Risse; §4 five foreshadowing strands and four
anchor trackers; §5 five Genesis motifs; §6 who knows what when; §7 the
Ouroboros mirrors; §8 Mnemosyne's temptation; §9 a thirteen-section chapter
briefing template (L725–L1039); §10 the hard rules R-1 to R-10; §11 genre per
act; §12 a master index of locks with their sources; §13 a proposed repository
layout; §14 the points it leaves open.

**The 1172 backslash escapes are the export's table markup** — every header
cell is `\*\*…\*\*`, and a label inside a table is triple-escaped, `\\\[L\\\]`.
The §9 template is markdown written as text: its headings and list markers
arrive escaped (`\#\# A. Strukturelle Position`, `\- \*\*Block:\*\*`), so the
profile counts 62 real headings and none of the template's. **The 48 `glued ref
numbers` are its own numbering** — `KW` 1–4, `Kap`, `Ebene`, `Schicht`, `Stil`,
`Vortex`, `Beat` — not footnotes; the file carries no URL. 0 invisible
characters.

## Stance — a drafting manual that labels its passages and ranks canon above its quarry

It states what it is for on its first line: „Schließt die Lücken zwischen
Outline, Glossar und Anteile-Profil für das Drafting über Claude Code." ^[L13]
The same line calls it the „Viertes Dokument im Repo-Quartett." ^[L13], names
the three others by file name, and defines four labels: `[K]` kanonisch, `[V]`
Vorschlag, `[S]` Steinbruch-gefiltert, `[L]` Lücke. **Counted over every
escaping, beyond that legend: 30 `[K]`, 11 `[V]`, 0 `[S]`, 11 `[L]`.** Nine
headings carry `[K]`; `[V]` and `[L]` stand on single table rows and on the
waypoints of §5.2, where a chain runs `[K]` for Kap 0 and `[V]` for the acts
after it (L535–L547).

**It ranks its sources.** §12 is „Alle bisher gesetzten Locks, chronologisch
und mit Quelle." ^[L1154], each lock with the document or log it came from.
§13 says of itself „Vorschlag, kein Lock. User-Entscheidung." ^[L1245] and
gives a precedence rule for the files it proposes: „Canon-Dateien sind
Source-of-Truth." ^[L1410], „Bei Konflikt zwischen Steinbruch und Canon gewinnt
Canon." ^[L1411] §1 opens by de-canonising two readings of its quarry:
„Beides ist dekanonisiert." ^[L42]

**Hedging is located, not spread.** 19 `offen`, 7 `Vorschlag`, 1 `TBD`, and 52
question marks, most of them in the §9 template (whose prompts are questions)
and in §14: „Diese Punkte schließt auch dieses Dokument nicht." ^[L1420] Its
closing note makes an absence a label: „Was nicht zu finden ist, ist" ^[L1488]
`[L]`.

## Candidates

1092 candidates, written while reading and before any count
(`Plan/runs/kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md/03-candidates.md`); `capture.py --count` counted
1084 and read eight as prose (a sentence, a rule title with a comma, a line the
document quotes). Line numbers are **file** lines; the frontmatter ends at L9.

| term | word | incl. compounds | first lines |
|---|--:|--:|---|
| `Kohärenz Protokoll` | 1 | 1 | 11 |
| `Welt-Bibel` | 4 | 4 | 13, 21, 40, 851 |
| `Sensorik` | 13 | 19 | 11, 13, 22, 58, 125, 183 … |
| `Drafting-Disziplin` | 3 | 3 | 11, 708, 1484 |
| `Outline` | 4 | 4 | 13, 1015, 1261, 1481 |
| `Glossar` | 2 | 2 | 13, 1429 |
| `Anteile-Profil` | 3 | 4 | 13, 855, 1185, 1456 |
| `Claude Code` | 5 | 5 | 13, 33, 1243, 1396, 1477 |
| `Foreshadowing-Tracker` | 1 | 1 | 13 |
| `Stränge` | 5 | 6 | 13, 24, 434, 436, 438, 466 |
| `Anker` | 9 | 36 | 13, 100, 101, 158, 326, 384 … |
| `Genesis-Motive` | 1 | 4 | 13, 25, 458, 514 |
| `Genesis-Motive-Choreografie` | 2 | 2 | 13, 25 |
| `Reveal-Disziplin` | 4 | 4 | 13, 26, 563, 935 |
| `Ouroboros-Spiegelungen` | 2 | 2 | 27, 614 |
| `Ouroboros-Spiegelungs-Tabellen` | 1 | 1 | 13 |
| `Kapitel-Briefing-Vorlage` | 3 | 3 | 13, 29, 725 |
| `Self-Review-Regelwerk` | 3 | 3 | 13, 30, 1045 |
| `Master-Index aller Locks` | 3 | 3 | 13, 32, 1152 |
| `Repo-Architektur-Empfehlung` | 3 | 3 | 13, 33, 1243 |
| `Repo-Quartett` | 2 | 2 | 13, 1477 |
| `storyform-und-outline_2026-06-10.md` | 0 | 0 |  |
| `begriffe-und-konzepte_2026-06-10.md` | 0 | 0 |  |
| `anteile-profile-sprach-dna_2026-06-10.md` | 0 | 0 |  |
| `Provenienz` | 1 | 1 | 13 |
| `[K]` | 0 | 0 |  |
| `[V]` | 0 | 0 |  |
| `[S]` | 0 | 0 |  |
| `[L]` | 0 | 0 |  |
| `kanonisch` | 8 | 9 | 13, 94, 152, 351, 539, 543 … |
| `Vorschlag` | 6 | 7 | 13, 1245, 1247, 1429, 1430, 1450 … |
| `Steinbruch-gefiltert` | 1 | 1 | 13 |
| `Lücke` | 2 | 4 | 13, 547, 573 |
| `KW1` | 11 | 11 | 21, 42, 44, 79, 83, 358 … |
| `KW2` | 8 | 11 | 21, 111, 148, 359, 369, 385 … |
| `KW3` | 5 | 5 | 21, 169, 205, 360, 420 |
| `KW4` | 8 | 8 | 21, 42, 225, 261, 361, 370 … |
| `Überwelt` | 3 | 4 | 21, 42, 175, 280 |
| `Externe Ebene` | 3 | 3 | 21, 42, 305 |
| `Sensorik-Bibliothek` | 2 | 2 | 22, 335 |
| `Stilebene` | 10 | 11 | 22, 75, 140, 197, 253, 335 … |
| `Risse-Phänomenologie` | 2 | 2 | 23, 395 |
| `Foreshadowing-Programm` | 2 | 2 | 24, 434 |
| `Rauschen` | 9 | 12 | 25, 384, 456, 474, 523, 535 … |
| `Form` | 16 | 22 | 25, 231, 361, 370, 458, 523 … |
| `Klick` | 4 | 6 | 25, 525, 543, 626 |
| `Phantom` | 6 | 13 | 25, 388, 457, 526, 547, 573 … |
| `Resonanz` | 15 | 23 | 25, 111, 136, 225, 328, 370 … |
| `Bewusstseins-Schichten` | 2 | 2 | 26, 563 |
| `Mnemosynes Versuchung` | 5 | 5 | 28, 686, 719, 1440, 1442 |
| `Anti-Heilung` | 2 | 2 | 28, 686 |
| `Hard-Rules` | 3 | 3 | 30, 1045, 1231 |
| `R-1` | 4 | 7 | 30, 1045, 1051, 1087, 1098, 1108 … |
| `Genre-Modus` | 2 | 2 | 31, 1126 |
| `Locks` | 5 | 10 | 13, 32, 1152, 1154, 1156, 1167 … |
| `Wirklich-offene Punkte` | 2 | 2 | 34, 1418 |
| `Sechs Ebenen einer Realität` | 1 | 1 | 40 |
| `Realitätsebenen` | 1 | 1 | 42 |
| `Steinbruch` | 3 | 4 | 13, 42, 1411 |
| `Guardian-zugeordnete Welten` | 0 | 0 |  |
| `LogOS` | 1 | 1 | 42 |
| `Kairos` | 1 | 2 | 42, 225 |
| `Sophia` | 1 | 1 | 42 |
| `dekanonisiert` | 4 | 5 | 42, 1183, 1184, 1185, 1297 |
| `Logikregime` | 0 | 1 | 42 |
| `psychologische Landschaften` | 1 | 1 | 42 |
| `Akt-Marker` | 1 | 1 | 42 |
| `Guardian-Reich` | 1 | 1 | 42 |
| `Konstrukt-Stadt` | 2 | 2 | 44, 539 |
| `Logos-Prime` | 1 | 1 | 44 |
| `K₁-Umgebung` | 1 | 1 | 46 |
| `K₁` | 2 | 8 | 46, 113, 397, 523, 574, 590 … |
| `K₀-Erosion` | 1 | 1 | 46 |
| `K₀` | 0 | 3 | 46, 397, 1175 |
| `ANP-Vermeidung` | 1 | 1 | 46 |
| `ANP` | 1 | 3 | 46, 955, 1059 |
| `Phaenomena` | 1 | 1 | 46 |
| `Kant` | 0 | 1 | 46 |
| `AEGIS` | 34 | 56 | 46, 75, 101, 159, 217, 280 … |
| `kognitiver Apparat` | 0 | 0 |  |
| `Akt-Dominanz` | 4 | 4 | 50, 117, 175, 231 |
| `Akt I` | 20 | 55 | 50, 117, 160, 161, 163, 175 … |
| `Multiplizitäts-Schleier` | 4 | 5 | 50, 887, 1059, 1063, 1225 |
| `Architektur als Kontrolle` | 1 | 1 | 54 |
| `Summen` | 2 | 2 | 62, 358 |
| `Ozon` | 11 | 15 | 63, 346, 358, 369, 382, 418 … |
| `Desinfektionsmittel` | 2 | 2 | 63, 358 |
| `Polaritätsregel` | 1 | 4 | 63, 337, 1067, 1196 |
| `Landauer-Signatur` | 3 | 3 | 63, 346, 382 |
| `Recycelte Luft` | 1 | 1 | 65 |
| `Systemhum` | 2 | 2 | 66, 358 |
| `21°C` | 2 | 3 | 67, 358, 383 |
| `Bilanzgrenze` | 1 | 1 | 67 |
| `diegetische Bilanzgrenze` | 1 | 1 | 67 |
| `Computational Class P` | 1 | 1 | 71 |
| `Polynomial` | 1 | 1 | 71 |
| `Ebene 1` | 1 | 1 | 75 |
| `Metaphernverbot` | 2 | 2 | 75, 368 |
| `AEGIS-Logs` | 3 | 3 | 75, 368, 1079 |
| `Somatik-Default` | 4 | 4 | 79, 144, 201, 257 |
| `Kael-Host` | 1 | 1 | 79 |
| `Kael` | 32 | 41 | 79, 101, 102, 105, 159, 448 … |
| `Atem-Zählung` | 1 | 1 | 79 |
| `Lex` | 4 | 8 | 79, 446, 637, 951, 1202, 1233 … |
| `Hypoventilation` | 1 | 1 | 79 |
| `Risse` | 15 | 21 | 23, 83, 104, 148, 205, 261 … |
| `Riss` | 4 | 31 | 23, 83, 104, 148, 205, 261 … |
| `Logikparadoxien` | 2 | 2 | 87, 417 |
| `Escher-Geometrien` | 2 | 2 | 87, 417 |
| `Kausalitätsschleifen` | 2 | 2 | 88, 417 |
| `Inkonsistente Regelanwendung` | 1 | 1 | 89 |
| `Blutende Knöchel` | 1 | 1 | 90 |
| `Kap-0-Lock` | 2 | 2 | 90, 386 |
| `Kap 0` | 27 | 27 | 27, 90, 445, 486, 516, 522 … |
| `Kap 1` | 34 | 55 | 27, 50, 90, 101, 102, 103 … |
| `Sub-Lokalitäten` | 6 | 6 | 94, 152, 209, 265, 290, 319 |
| `Wohneinheit 734` | 1 | 1 | 101 |
| `Einheit 734` | 3 | 3 | 101, 487, 1200 |
| `Konsolen-Zeile` | 4 | 4 | 101, 487, 661, 1200 |
| `Datenverarbeitungsknoten Epsilon` | 1 | 1 | 102 |
| `Transitkorridor Delta-7` | 1 | 1 | 103 |
| `Sektor 04` | 1 | 1 | 104 |
| `Archivar-Klasse-II-Arbeitsraum` | 1 | 1 | 105 |
| `Komponente 734` | 2 | 2 | 105, 661 |
| `Archivar Klasse II` | 1 | 1 | 105 |
| `Foreshadowing-Anker` | 2 | 2 | 101, 488 |
| `Kapitel-Anker` | 2 | 2 | 100, 158 |
| `erster Riss` | 1 | 1 | 104 |
| `Mnemosyne-Archipel` | 2 | 2 | 111, 159 |
| `Resonanzlandschaft` | 1 | 1 | 111 |
| `Klimax-Setting` | 1 | 2 | 111, 1427 |
| `Mnemosyne` | 8 | 20 | 28, 111, 159, 162, 163, 298 … |
| `Erinnerung als Schauplatz` | 0 | 0 |  |
| `gespeicherte K₁` | 1 | 1 | 113 |
| `Erasure` | 2 | 12 | 113, 171, 282, 298, 346, 382 … |
| `K₁-Substrat` | 2 | 2 | 113, 397 |
| `Vortex-1-Setting` | 1 | 1 | 113 |
| `Vortex 1` | 11 | 11 | 117, 351, 445, 446, 449, 508 … |
| `Akt II` | 22 | 35 | 117, 160, 161, 163, 175, 231 … |
| `Wälder des Flüsterns` | 1 | 1 | 121 |
| `Ozeane der Trauer` | 1 | 1 | 121 |
| `Lichtkegel` | 1 | 3 | 121, 359, 385 |
| `Architektonische Palimpseste` | 1 | 1 | 121 |
| `Echos` | 3 | 3 | 129, 359, 539 |
| `feuchte Erde` | 1 | 1 | 359 |
| `verblassendes Parfum` | 1 | 1 | 359 |
| `Nicht-lineare Zeit` | 1 | 1 | 132 |
| `Parakonsistent` | 1 | 1 | 136 |
| `Trivialismus` | 1 | 1 | 136 |
| `Tarski-Hierarchie` | 1 | 1 | 136 |
| `Ebene 2` | 4 | 4 | 140, 197, 547, 879 |
| `Bauchreaktionen` | 1 | 1 | 144 |
| `Viszerales Erinnern` | 1 | 1 | 144 |
| `Temporale Risse` | 1 | 1 | 148 |
| `Kiko` | 3 | 4 | 148, 405, 406, 1235 |
| `Kiko-Trigger` | 1 | 1 | 148 |
| `spatiale Risse` | 1 | 1 | 148 |
| `Lia` | 3 | 3 | 148, 406, 1235 |
| `Isabelle` | 2 | 3 | 148, 408, 1235 |
| `Das Archiv der Grenzen` | 2 | 2 | 159, 1211 |
| `Wald des Flüsterns` | 1 | 1 | 160 |
| `Erinnerungslandschaft` | 1 | 1 | 160 |
| `Ozean-Becken` | 1 | 1 | 161 |
| `Mnemosyne-Server-Architektur` | 2 | 2 | 162, 1427 |
| `Vortex-Setting` | 1 | 1 | 162 |
| `Inselgruppe` | 1 | 1 | 162 |
| `Server-Halle` | 1 | 1 | 162 |
| `Memorialarchitektur` | 1 | 1 | 162 |
| `Zirbeldrüse` | 1 | 1 | 162 |
| `Encoding` | 1 | 5 | 162, 727, 759, 1422, 1427 |
| `Mnemosynes Audienz-Raum` | 1 | 1 | 163 |
| `Mnemosynen-Versuchung` | 1 | 1 | 163 |
| `Cerberus-Labyrinth` | 1 | 1 | 169 |
| `Grenzfeste` | 1 | 1 | 169 |
| `Cerberus` | 0 | 1 | 169 |
| `Schutzraum` | 1 | 1 | 171 |
| `Quarantäne` | 1 | 1 | 171 |
| `Kontrollzentrum` | 1 | 1 | 171 |
| `EP-Protektoren` | 1 | 1 | 171 |
| `EP` | 1 | 6 | 171, 369, 399, 403, 955, 1059 |
| `Erasure-Pol` | 2 | 3 | 171, 298, 1183 |
| `Erasure-Pol-Logik` | 1 | 1 | 171 |
| `Überwelt-Nexus` | 1 | 1 | 175 |
| `Approach-Inmost-Cave-Beat` | 1 | 1 | 175 |
| `Kap 33` | 5 | 5 | 175, 299, 327, 547, 590 |
| `Ewiges Dämmerlicht` | 1 | 1 | 179 |
| `Niemandsland` | 1 | 1 | 179 |
| `Schießpulver-Geruch` | 1 | 1 | 179 |
| `Hyperalert-Gefühl` | 1 | 1 | 189 |
| `Bedrohungsanalyse` | 1 | 1 | 193 |
| `Verteidigungsprotokolle` | 1 | 1 | 193 |
| `Mustererkennung` | 1 | 1 | 193 |
| `NP-Hard` | 1 | 1 | 193 |
| `Ebene 2+` | 1 | 1 | 197 |
| `Stakkato` | 1 | 1 | 197 |
| `Brace for Impact` | 1 | 1 | 201 |
| `Bruxismus` | 1 | 1 | 201 |
| `Hypertonus` | 1 | 1 | 201 |
| `gravitationale Risse` | 1 | 1 | 205 |
| `kinetische Risse` | 1 | 1 | 205 |
| `Zitadelle` | 1 | 1 | 216 |
| `Inneres Bollwerk` | 1 | 1 | 216 |
| `Wartungsschächte` | 1 | 1 | 217 |
| `Die unbewachten Tore` | 1 | 1 | 218 |
| `Evaluierungseinheit` | 1 | 1 | 219 |
| `Kap 13` | 7 | 7 | 50, 219, 462, 573, 585, 1059 |
| `Kairos-Potentialis` | 1 | 1 | 225 |
| `Resonanz-Kontinuum` | 1 | 1 | 225 |
| `Möglichkeits-Garten` | 2 | 2 | 225, 272 |
| `Coheronen` | 1 | 1 | 227 |
| `Coheron` | 1 | 5 | 227, 347, 409, 506, 527 |
| `Emergenz statt Erhaltung` | 1 | 1 | 227 |
| `Ruinengarten der Möglichkeit` | 1 | 1 | 227 |
| `Funktionale Multiplizität` | 2 | 2 | 227, 1186 |
| `Akt III` | 13 | 13 | 231, 370, 374, 438, 447, 498 … |
| `Synästhesie` | 2 | 2 | 235, 408 |
| `Vermischung der Sinnesfelder` | 1 | 1 | 243 |
| `Warmes Licht` | 1 | 1 | 244 |
| `Generativ` | 2 | 3 | 249, 261 |
| `Computational Class` | 4 | 4 | 71, 136, 193, 249 |
| `Ebene 3` | 1 | 1 | 253 |
| `Wir-Pronomen` | 1 | 1 | 253 |
| `Stilles Wachsen` | 1 | 1 | 257 |
| `Generative Risse` | 1 | 1 | 261 |
| `innere Praxis` | 0 | 0 |  |
| `Nexus` | 1 | 2 | 175, 273 |
| `Realitätsstränge` | 1 | 1 | 273 |
| `Mosaik-Herz` | 1 | 1 | 274 |
| `Kap 34` | 2 | 2 | 274, 539 |
| `vor Vortex` | 3 | 3 | 274, 604, 700 |
| `finale Selbst-Schöpfung` | 0 | 0 |  |
| `AEGIS' Maschinenraum` | 1 | 1 | 280 |
| `Operationsraum` | 1 | 1 | 282 |
| `Datenstrom-Kathedrale` | 1 | 1 | 282 |
| `Guardians` | 2 | 2 | 282, 1183 |
| `zwei Guardians` | 1 | 1 | 282 |
| `abstrakte Entitäten` | 1 | 1 | 282 |
| `Logs` | 2 | 6 | 75, 282, 368, 428, 1079, 1190 |
| `Erasure-Sweeps` | 1 | 1 | 282 |
| `Datenströme` | 1 | 1 | 286 |
| `Lichtbahnen` | 1 | 1 | 286 |
| `Wächter-Konsolen` | 1 | 1 | 286 |
| `Schnittstelle zu den Kernwelten` | 1 | 1 | 297 |
| `Kernwelten` | 1 | 1 | 297 |
| `KWs` | 2 | 2 | 218, 297 |
| `Wächter-Registry` | 1 | 1 | 298 |
| `Wächter` | 0 | 2 | 286, 298 |
| `Jenseits-des-Ereignishorizonts-Bereich` | 1 | 1 | 299 |
| `Verschränkungs-Insel` | 1 | 1 | 299 |
| `Köln 2026` | 3 | 3 | 305, 315, 1441 |
| `Köln` | 4 | 4 | 305, 315, 326, 1441 |
| `außerhalb der Simulation` | 1 | 1 | 307 |
| `Simulation` | 1 | 1 | 307 |
| `die andere Seite des Spiegels` | 1 | 1 | 307 |
| `Substrat-Durchbruch` | 1 | 1 | 307 |
| `Kap 36` | 2 | 2 | 307, 592 |
| `Plattenbauten` | 1 | 1 | 311 |
| `S-Bahn-Geräusche` | 1 | 1 | 311 |
| `Telefon` | 3 | 15 | 311, 315, 384, 449, 456, 470 … |
| `Bühne` | 1 | 1 | 315 |
| `Erinnerungsfragment` | 1 | 1 | 315 |
| `Telefonton` | 1 | 1 | 315 |
| `Junas Ankerpunkt` | 1 | 1 | 326 |
| `Juna` | 15 | 30 | 326, 327, 347, 370, 384, 449 … |
| `Garten der stillen Präsenz` | 1 | 1 | 327 |
| `Juna-Wirkung` | 2 | 2 | 327, 1117 |
| `Quelle des Flüsterns` | 1 | 1 | 328 |
| `Unkartiertes Territorium` | 1 | 1 | 329 |
| `Hitze-Polaritätsregel` | 3 | 3 | 337, 1067, 1196 |
| `gelockt` | 1 | 1 | 337 |
| `thermische Signaturen` | 1 | 1 | 339 |
| `Signatur` | 6 | 13 | 63, 339, 345, 346, 368, 382 … |
| `Ontologie` | 1 | 1 | 345 |
| `Akt-Aktivität` | 1 | 1 | 345 |
| `Kaltes Ozon` | 2 | 2 | 346, 1067 |
| `AEGIS-Unterdrückung` | 1 | 1 | 346 |
| `Erasure-Aktivität` | 3 | 3 | 346, 382, 674 |
| `Default-Signatur` | 1 | 1 | 346 |
| `Wärme` | 8 | 12 | 347, 351, 502, 506, 676, 859 … |
| `Junas ununterdrückbare Spur` | 1 | 1 | 347 |
| `Coheron-Verdrängung` | 1 | 1 | 347 |
| `Hauttemperatur ohne Wärmequelle` | 1 | 1 | 347 |
| `Tiefenempfindung` | 1 | 1 | 347 |
| `Geruchserinnerungen ohne Geruchsquelle` | 1 | 1 | 347 |
| `Debüt Kap 3` | 1 | 2 | 347, 1196 |
| `Kap 3` | 4 | 45 | 117, 162, 175, 274, 299, 307 … |
| `Hitzen` | 1 | 1 | 351 |
| `Vortex 1 Beat 4` | 4 | 4 | 351, 445, 508, 1067 |
| `Heat Spike` | 3 | 3 | 351, 445, 508 |
| `Suppression` | 3 | 6 | 351, 397, 428, 574, 674, 1184 |
| `MI-dichtes Ziel` | 0 | 0 |  |
| `MI` | 2 | 3 | 351, 449, 523 |
| `Sensorik-Lookup` | 2 | 2 | 353, 363 |
| `grüne Erde` | 1 | 1 | 361 |
| `Stille mit innerem Klang` | 1 | 1 | 361 |
| `Musik aus Form` | 1 | 1 | 361 |
| `Stil 1` | 1 | 1 | 374 |
| `Stil 2` | 0 | 0 |  |
| `Stil 3` | 2 | 2 | 374 |
| `EP-Domäne` | 1 | 1 | 369 |
| `Juna-Stil` | 1 | 1 | 370 |
| `klassische Logik` | 1 | 1 | 368 |
| `Beispiel-Vokabular` | 1 | 1 | 367 |
| `Triggerbrüche` | 1 | 1 | 369 |
| `NP-hart` | 1 | 1 | 369 |
| `chorisch` | 3 | 4 | 370, 604, 743, 1138 |
| `Form-die-atmet` | 1 | 1 | 370 |
| `Diegetische Wiederkehr-Sensorik` | 1 | 1 | 376 |
| `Foreshadowing-Default` | 1 | 1 | 376 |
| `Ozon-Geruch` | 1 | 1 | 382 |
| `21°C-Schwelle` | 1 | 1 | 383 |
| `thermisches Versagen` | 1 | 1 | 383 |
| `Riss-Vorzeichen` | 1 | 1 | 383 |
| `Telefon-Rauschen` | 2 | 2 | 384, 456 |
| `Telefon-Stille` | 4 | 7 | 449, 470, 474, 477, 967, 1119 … |
| `Junas Anker` | 1 | 2 | 326, 384 |
| `Staub-Bewegung in Lichtkegeln` | 1 | 1 | 385 |
| `KW2-Erinnerungs-Markierung` | 1 | 1 | 385 |
| `Knöchel-Blutung` | 3 | 3 | 386, 445, 678 |
| `Quellenloses Licht beim Erwachen` | 1 | 1 | 387 |
| `Kap 39` | 15 | 15 | 387, 449, 477, 539, 543, 547 … |
| `Ouroboros` | 1 | 8 | 13, 27, 387, 614, 631, 911 … |
| `Komponente` | 7 | 8 | 105, 368, 388, 457, 482, 661 … |
| `Phantom-Bilanz` | 3 | 3 | 388, 457, 547 |
| `System-Verstrickung` | 1 | 1 | 388 |
| `Zahl 734` | 1 | 1 | 389 |
| `Kap 2` | 4 | 12 | 101, 104, 175, 231, 389, 447 … |
| `Kap 10` | 7 | 7 | 101, 163, 551, 573, 700, 1225 … |
| `Kap 25` | 2 | 2 | 101, 588 |
| `Inversion` | 2 | 3 | 397, 668, 1099 |
| `Suppression-Versagen` | 3 | 3 | 397, 428, 574 |
| `Atmen der Realität` | 1 | 1 | 397 |
| `K₀-Architektur` | 1 | 1 | 397 |
| `EP-Trigger` | 2 | 2 | 399, 403 |
| `Riss-Typ` | 3 | 4 | 399, 403, 416, 425 |
| `Anteils-Risse` | 1 | 1 | 399 |
| `Sensorische Signatur` | 1 | 1 | 403 |
| `Nyx` | 2 | 2 | 404, 951 |
| `Fight` | 1 | 1 | 404 |
| `Freeze` | 1 | 1 | 405 |
| `Flight` | 1 | 1 | 406 |
| `Moros` | 2 | 2 | 407, 1235 |
| `Collapse` | 2 | 2 | 407, 1161 |
| `kinetisch` | 1 | 2 | 205, 404 |
| `temporal` | 2 | 5 | 253, 405, 410, 574, 603 |
| `spatial` | 1 | 2 | 148, 406 |
| `gravitativ` | 2 | 2 | 407, 410 |
| `sensorisch` | 3 | 3 | 339, 408, 649 |
| `Silas` | 5 | 8 | 409, 492, 498, 875, 951, 1195 … |
| `Coheron-Echo` | 1 | 1 | 409 |
| `relational/warm` | 1 | 1 | 409 |
| `Oblivion` | 6 | 7 | 410, 719, 951, 1428, 1430 |
| `Erason-Operator` | 1 | 1 | 410 |
| `Erason` | 0 | 1 | 410 |
| `Welt-Risse` | 2 | 2 | 412, 959 |
| `Akt-Default-Risse` | 1 | 1 | 412 |
| `Welt-Riss-Typ` | 1 | 1 | 416 |
| `logisch` | 1 | 13 | 42, 417, 601, 927, 1087, 1135 … |
| `KW1→KW2-Übergang` | 1 | 1 | 418 |
| `thermisch` | 1 | 3 | 339, 383, 418 |
| `wässrig / mnemonisch` | 1 | 1 | 419 |
| `paranoid` | 2 | 2 | 197, 420 |
| `Kompositions-Regel für Riss-Szenen` | 1 | 1 | 423 |
| `Riss-Szenen` | 1 | 1 | 423 |
| `Storyform-Pull` | 1 | 1 | 425 |
| `Sensorische Verzerrung` | 1 | 1 | 426 |
| `Foreshadowing-Stränge` | 1 | 1 | 438 |
| `erste Spur` | 1 | 1 | 438 |
| `Akkumulation` | 2 | 3 | 438, 444, 462 |
| `Erntung` | 2 | 2 | 438, 444 |
| `Strang` | 2 | 3 | 438, 444, 1449 |
| `Landauer` | 1 | 4 | 63, 346, 382, 445 |
| `Wahrheitsvertuschung` | 1 | 1 | 445 |
| `Ozon-Atmosphäre` | 1 | 1 | 445 |
| `Kap 6` | 2 | 2 | 445, 539 |
| `Cache-Konflikt` | 1 | 1 | 445 |
| `Kap 19` | 1 | 1 | 445 |
| `AEGIS-Eskalation` | 1 | 1 | 445 |
| `Heat Spike → ∞` | 1 | 1 | 445 |
| `Gödel` | 1 | 2 | 446 |
| `Lex-Kap-Momente` | 1 | 1 | 446 |
| `widersprüchliche Klassifikationen` | 1 | 1 | 446 |
| `Kap 18` | 2 | 2 | 446, 587 |
| `Hartes Problem` | 1 | 1 | 446 |
| `Gödel-Gambit` | 1 | 1 | 446 |
| `Kap 30` | 3 | 3 | 446, 476, 589 |
| `Bekenstein` | 1 | 2 | 447, 1449 |
| `Pixelierung` | 3 | 3 | 447, 456, 1449 |
| `Detailrand` | 1 | 1 | 447 |
| `Kap 22` | 1 | 1 | 447 |
| `Phase A` | 2 | 4 | 447, 1138, 1195 |
| `Architektur-Kollaps` | 1 | 1 | 447 |
| `Dasein` | 2 | 2 | 448, 637 |
| `Existentielle Unverankerung` | 1 | 1 | 448 |
| `Kael-Reflexionen` | 1 | 1 | 448 |
| `Sartre` | 1 | 1 | 448 |
| `Heidegger` | 0 | 1 | 448 |
| `Kap 27` | 2 | 2 | 448, 1138 |
| `Ordinary World` | 1 | 1 | 448 |
| `Euler` | 1 | 1 | 449 |
| `Mathematische Schönheit` | 1 | 1 | 449 |
| `verlorene Sprache` | 1 | 1 | 449 |
| `Junas Erscheinungen` | 1 | 1 | 449 |
| `MI ohne Datenträger` | 1 | 1 | 449 |
| `Vortex 1 Beat 3` | 1 | 1 | 449 |
| `Show-don't-Tell` | 1 | 1 | 451 |
| `Drei Ebenen des Show-don't-Tell` | 1 | 1 | 451 |
| `Sprachliche Spuren` | 2 | 2 | 457, 879 |
| `Strukturelle Markierungen` | 1 | 1 | 458 |
| `Verlorene Sekunden` | 1 | 1 | 457 |
| `Antwortlatenzen` | 1 | 1 | 457 |
| `Stilbrüche` | 1 | 1 | 457 |
| `AEGIS-Log-Format` | 1 | 1 | 458 |
| `Stilbruch-Choreografie` | 1 | 1 | 458 |
| `Genesis-Motive-Wiederkehr` | 1 | 1 | 458 |
| `Akkumulations-Regel` | 1 | 1 | 462 |
| `Schleier-Fall` | 1 | 1 | 462 |
| `Twist-Anforderung` | 1 | 1 | 466 |
| `DID-Architektur` | 1 | 1 | 466 |
| `DID` | 1 | 3 | 466, 1059 |
| `Cosmic Horror` | 1 | 1 | 466 |
| `Reread` | 1 | 1 | 466 |
| `DID-Symptome` | 1 | 1 | 466 |
| `Anker-Tracker` | 1 | 1 | 468 |
| `Telefon-Stille-Anker` | 3 | 3 | 470, 967, 1119 |
| `Kap 7` | 2 | 2 | 474, 551 |
| `Die Stimme im Rauschen` | 2 | 2 | 474, 551 |
| `K-J-Verbindung` | 2 | 2 | 474, 476 |
| `Kap 24` | 1 | 1 | 475 |
| `A-Prerequisite` | 1 | 1 | 476 |
| `Telefon-Anker` | 2 | 2 | 478, 875 |
| `Komponente-734-Anker` | 1 | 1 | 482 |
| `Komp-734-Bezeichnung` | 1 | 1 | 486 |
| `Komp 734` | 2 | 2 | 572, 581 |
| `Reader-only-Echo` | 2 | 2 | 487, 1200 |
| `Silas-Halbsatz-Anker` | 1 | 1 | 492 |
| `Frequenz der Lüftung` | 2 | 2 | 496, 1201 |
| `Schicht-2-gekoppelt` | 1 | 1 | 496 |
| `Echo-Prosa` | 1 | 1 | 497 |
| `aktiver Transmitter` | 0 | 0 |  |
| `Kap 31` | 3 | 3 | 498, 543, 1428 |
| `Kap 32` | 0 | 0 |  |
| `OQ-E` | 2 | 3 | 498, 1428, 1488 |
| `Wärme-Debüt-Anker` | 1 | 1 | 502 |
| `Coheron-Spur` | 1 | 1 | 506 |
| `Polaritäts-Lock 2026-05-30` | 1 | 1 | 506 |
| `Polaritäts-Lock` | 1 | 1 | 506 |
| `Erstereignisse` | 2 | 2 | 516, 626 |
| `Erstereignis` | 1 | 3 | 516, 522, 626 |
| `Motiv` | 3 | 17 | 13, 25, 458, 514, 516, 518 … |
| `Nichts-Rauschen` | 1 | 1 | 523 |
| `K₁-Reinform` | 3 | 3 | 523, 574, 1175 |
| `Chaos` | 1 | 1 | 523 |
| `Cluster-Bildung` | 2 | 2 | 524, 539 |
| `Auflösung` | 2 | 2 | 524, 674 |
| `Schwelle` | 4 | 7 | 370, 383, 525, 543, 641, 943 |
| `Schalter` | 1 | 1 | 525 |
| `Trauma als Resonanz ohne Quelle` | 1 | 1 | 526 |
| `Junas Spur` | 1 | 1 | 526 |
| `Liebe als Coheron` | 1 | 1 | 527 |
| `Korrelat-Achse` | 2 | 2 | 527, 572 |
| `Wegmarken` | 1 | 1 | 529 |
| `Wiederkehrmuster` | 1 | 1 | 531 |
| `Reinform-Stille` | 1 | 1 | 535 |
| `Ozon-Reaktion` | 1 | 1 | 535 |
| `Kap 37` | 3 | 3 | 535, 1140, 1228 |
| `Kap 38` | 4 | 4 | 535, 551, 593, 1141 |
| `Kap 40` | 12 | 12 | 535, 551, 572, 595, 616, 618 … |
| `Anti-Form` | 1 | 1 | 539 |
| `Echos im Fundament` | 1 | 1 | 539 |
| `Form-Motiv` | 1 | 1 | 539 |
| `Kohärenz-Mantra` | 1 | 1 | 539 |
| `Umgebungs-Logik` | 1 | 1 | 539 |
| `falsche Form` | 1 | 1 | 539 |
| `zwei Arten von Form` | 1 | 1 | 539 |
| `Orkan` | 1 | 1 | 539 |
| `Sphäre` | 1 | 1 | 539 |
| `das Wir` | 1 | 1 | 539 |
| `plurale Form` | 1 | 1 | 539 |
| `Trennungs-Klick` | 1 | 1 | 543 |
| `Schwellen-Bruch` | 1 | 1 | 543 |
| `Klick-Motiv` | 1 | 1 | 543 |
| `Vortex 1 Beat 2` | 1 | 1 | 543 |
| `Pivot` | 2 | 2 | 543, 591 |
| `Trennung` | 4 | 14 | 543, 547, 551, 572, 627, 628 … |
| `Sehnen-ohne-Adresse` | 1 | 1 | 547 |
| `Kap 4` | 1 | 13 | 535, 547, 551, 572, 595, 616 … |
| `Pforten` | 1 | 1 | 547 |
| `Phantom-Motiv` | 2 | 2 | 547 |
| `Hintergrundrauschen` | 1 | 2 | 547 |
| `Komp-734-Hintergrundrauschen` | 1 | 1 | 547 |
| `Trennungsprotokoll` | 7 | 9 | 551, 572, 627, 628, 1174, 1456 … |
| `Resonanz-Motiv` | 1 | 1 | 551 |
| `Moonshine-Resonanz` | 1 | 1 | 551 |
| `Vortex 2` | 3 | 3 | 551, 1141, 1173 |
| `Motiv-Echo` | 2 | 3 | 555, 557, 871 |
| `Allegorie` | 2 | 2 | 555, 1075 |
| `Genesis-Echo` | 5 | 6 | 557, 839, 983, 1027, 1075, 1114 |
| `Kernfrage` | 1 | 1 | 565 |
| `Lesersteuerung` | 2 | 2 | 565, 919 |
| `tragische Ironie` | 3 | 3 | 565, 582, 1108 |
| `Drei Schichten` | 1 | 1 | 567 |
| `Schicht` | 3 | 15 | 26, 496, 563, 567, 571, 899 … |
| `Bewusst` | 1 | 6 | 26, 497, 563, 571, 589, 680 |
| `Spürt` | 1 | 1 | 571 |
| `Blind` | 1 | 1 | 571 |
| `Resonanz-Quelle` | 1 | 1 | 572 |
| `Schleier-Lüftung` | 2 | 2 | 572, 584 |
| `Spiegel-Konflikt` | 1 | 1 | 572 |
| `Reset` | 4 | 5 | 572, 595, 1178, 1187, 1203 |
| `Transfiguration` | 3 | 3 | 572, 595, 1203 |
| `Lesart-Dualität` | 2 | 2 | 572, 1203 |
| `Atmosphären-Drift` | 1 | 1 | 573 |
| `Stilcode-Einbrüche` | 1 | 1 | 573 |
| `Stilcode` | 0 | 1 | 573 |
| `Phantom-Resonanz` | 1 | 1 | 573 |
| `Multiplizität` | 6 | 12 | 50, 227, 573, 588, 590, 815 … |
| `Junas Identität` | 1 | 1 | 573 |
| `Mandat` | 1 | 2 | 574, 589 |
| `η-Werte` | 1 | 1 | 574 |
| `Erasure-Bilanzen` | 1 | 1 | 574 |
| `Juna strukturell` | 1 | 1 | 574 |
| `atemporal` | 2 | 2 | 253, 574 |
| `uncorrelated noise` | 2 | 2 | 574, 582 |
| `die eigene Genesis` | 1 | 1 | 574 |
| `Genesis` | 5 | 29 | 13, 25, 458, 514, 557, 574 … |
| `Reveal-Timeline` | 1 | 1 | 576 |
| `Kapitel-Range` | 1 | 1 | 580 |
| `Slot-16-Lock` | 1 | 1 | 583 |
| `Kap 5` | 3 | 3 | 583, 1197, 1431 |
| `Kap 8` | 1 | 1 | 584 |
| `1.-Person-Innensicht` | 1 | 1 | 583 |
| `Modi` | 2 | 3 | 584, 1146, 1195 |
| `Stimmungs-Drifts` | 1 | 1 | 584 |
| `Anteile` | 3 | 8 | 13, 584, 855, 1185, 1428, 1456 … |
| `Phase-Wechsel` | 1 | 1 | 585 |
| `Eskalation` | 1 | 3 | 445, 585, 1138 |
| `Kap 14` | 4 | 4 | 117, 159, 586, 1137 |
| `Erasure-Welle` | 1 | 1 | 586 |
| `AEGIS-Dossiers` | 1 | 1 | 586 |
| `Lernarchiv Theta-9` | 1 | 1 | 586 |
| `Erasure-Phase 2` | 1 | 1 | 586 |
| `Genesis-Flashbacks` | 1 | 1 | 587 |
| `Bridge` | 2 | 6 | 587, 603, 1063, 1111, 1165, 1226 |
| `Kap 26` | 0 | 0 |  |
| `Countdown` | 1 | 1 | 588 |
| `Moonshine-Bewusstsein` | 1 | 1 | 589 |
| `K-J-Kanal` | 1 | 1 | 589 |
| `Mandat-Krise` | 1 | 1 | 589 |
| `direkte Berührung K₁` | 1 | 1 | 590 |
| `FM-Achievement` | 1 | 1 | 590 |
| `funktionale Multiplizität` | 1 | 1 | 590 |
| `parakonsistente Logik` | 1 | 1 | 590 |
| `Kap 35` | 4 | 4 | 117, 162, 591, 1139 |
| `Truth-Rotation` | 1 | 1 | 591 |
| `Trauma ohne Dissoziation` | 1 | 1 | 591 |
| `Beat 5` | 1 | 1 | 592 |
| `Rotation` | 1 | 2 | 591, 592 |
| `Wer spricht?` | 1 | 1 | 592 |
| `algorithmische Melancholie` | 1 | 1 | 592 |
| `plurale Apotheose` | 2 | 2 | 594, 1187 |
| `Wir-AEGIS-plural` | 6 | 6 | 594, 595, 661, 1173, 1174, 1212 |
| `Erzähl-Stimme` | 1 | 1 | 595 |
| `Iser-Layer-Disziplin` | 1 | 1 | 597 |
| `Iser` | 0 | 3 | 597, 608, 923 |
| `Narratologisch` | 2 | 2 | 601, 927 |
| `Leser-Bedeutungs-Montage` | 1 | 1 | 601 |
| `Phänomenologisch` | 2 | 2 | 601, 927 |
| `Leser-Erleben` | 1 | 1 | 601 |
| `Operativ` | 2 | 2 | 601, 927 |
| `kognitiver Aufwand` | 1 | 1 | 601 |
| `monophone Kael-Erzählung` | 1 | 1 | 602 |
| `Uncanny Valley` | 2 | 2 | 602, 1136 |
| `Leerstellen` | 1 | 2 | 602, 604 |
| `Zeitverlust` | 1 | 1 | 602 |
| `Fußnoten` | 3 | 3 | 602, 603, 1450 |
| `polyphon` | 1 | 2 | 603, 1138 |
| `Bridges` | 1 | 1 | 603 |
| `Doppellesarten` | 1 | 1 | 603 |
| `Desorientierung` | 1 | 1 | 603 |
| `Glitches` | 1 | 1 | 603 |
| `widersprüchliche Fußnoten` | 1 | 1 | 603 |
| `temporales Scrambling` | 1 | 1 | 603 |
| `Wir-Geflecht` | 1 | 2 | 604, 1227 |
| `Leerstellen-Dichte` | 1 | 1 | 604 |
| `Sog` | 1 | 1 | 604 |
| `Hard-Rule` | 1 | 4 | 30, 608, 1045, 1231 |
| `Canon` | 3 | 5 | 608, 1410, 1411 |
| `Reader-Funktion` | 1 | 1 | 608 |
| `Bedingung der Möglichkeit` | 1 | 1 | 608 |
| `Storyform-Position` | 1 | 1 | 608 |
| `Genesis-Klammer` | 2 | 2 | 616, 1176 |
| `plurale Heilung` | 0 | 0 |  |
| `Kap-0-Bewegung` | 1 | 1 | 624 |
| `Kap-40-Echo` | 1 | 1 | 624 |
| `Vorwort` | 1 | 2 | 625 |
| `Lesehaltungs-Anleitung` | 1 | 1 | 625 |
| `Leser-Adressierung` | 1 | 1 | 625 |
| `Echo des Vorworts` | 1 | 1 | 625 |
| `Erzähler` | 1 | 4 | 625, 1051, 1059, 1098 |
| `Frage → Zeugnis` | 1 | 1 | 625 |
| `Genesis-Bewegungen` | 1 | 1 | 626 |
| `Echo der Genesis` | 1 | 1 | 626 |
| `Werdung` | 2 | 2 | 626, 627 |
| `Krise` | 2 | 4 | 589, 627, 895 |
| `Stille Wacht` | 1 | 1 | 627 |
| `Perturbation` | 1 | 1 | 627 |
| `Algorithmischer Schrecken` | 1 | 1 | 627 |
| `Resonanzkaskade` | 1 | 1 | 627 |
| `Systemischer Kollaps` | 1 | 1 | 627 |
| `Echo der Krise` | 1 | 1 | 627 |
| `Echo des Trennungsprotokolls` | 1 | 1 | 628 |
| `Scherben` | 2 | 3 | 628, 629 |
| `Scherben-Fall` | 1 | 1 | 629 |
| `Letztes Bild` | 1 | 1 | 629 |
| `Mosaik` | 1 | 2 | 274, 629 |
| `Resolution-ohne-Erklärung` | 1 | 1 | 629 |
| `innere Ouroboros-Klammer` | 1 | 1 | 631 |
| `Erstsatz-Lock 2026-05-30` | 1 | 1 | 633 |
| `Erstsatz-Lock` | 1 | 1 | 633 |
| `Erstsatz` | 0 | 3 | 633, 645, 1202 |
| `Lexem-Echo` | 2 | 2 | 637, 1202 |
| `da` | 7 | 101 | 13, 63, 71, 113, 136, 161 … |
| `Welt-Subjekt` | 1 | 1 | 641 |
| `Das Licht` | 3 | 3 | 633, 641, 1202 |
| `Junas Grammatik` | 1 | 1 | 641 |
| `Drei Tests` | 1 | 1 | 645 |
| `Erst-Read` | 1 | 1 | 649 |
| `schleier-sicher` | 1 | 1 | 649 |
| `Zweit-Read` | 1 | 1 | 650 |
| `Schreibbar` | 1 | 1 | 651 |
| `indirektes quellenloses Licht` | 0 | 0 |  |
| `Sensorium` | 1 | 1 | 658 |
| `Spiegelbild-Mikroverzögerung` | 1 | 1 | 659 |
| `Anker-Wort` | 1 | 1 | 660 |
| `Stille` | 16 | 28 | 66, 257, 261, 358, 361, 370 … |
| `Selbst-Bezeichnung` | 3 | 3 | 661, 680 |
| `Phantom-Spur` | 1 | 1 | 662 |
| `Resonanz mit Adresse` | 1 | 1 | 662 |
| `Memory-Anker` | 1 | 1 | 666 |
| `Stille-Anker` | 1 | 4 | 470, 666, 967, 1119 |
| `Inversions-Mechanik` | 1 | 1 | 668 |
| `zentrale Bilder` | 1 | 1 | 668 |
| `Coda` | 3 | 3 | 672, 739, 1142 |
| `Quellenloses Licht` | 2 | 2 | 387, 673 |
| `Stille-mit-Substanz` | 1 | 1 | 677 |
| `OQ-Knöchel` | 2 | 2 | 678, 1439 |
| `Zähl-Manie` | 1 | 1 | 679 |
| `Kacheln` | 2 | 2 | 368, 679 |
| `Vermeidungs-Stütze` | 1 | 1 | 679 |
| `Wir-Pluralität` | 2 | 2 | 680, 1141 |
| `den Schmerz löschen` | 1 | 1 | 692 |
| `Heilung durch Auslöschung` | 1 | 1 | 692 |
| `AEGIS' Methode` | 1 | 1 | 692 |
| `Trauma` | 3 | 4 | 526, 539, 591, 692 |
| `überfordert` | 1 | 1 | 696 |
| `AEGIS-System` | 1 | 1 | 696 |
| `Subtext` | 1 | 1 | 696 |
| `Setting der Versuchung` | 1 | 1 | 700 |
| `Charakter-Bibel-Anker` | 1 | 1 | 700 |
| `Charakter-Bibel` | 2 | 3 | 700, 1269, 1460 |
| `Guardian-Stimme` | 1 | 1 | 704 |
| `Stilebene 2` | 1 | 1 | 704 |
| `Antagonistin` | 1 | 1 | 712 |
| `Geschenk` | 1 | 1 | 713 |
| `AEGIS' Logik` | 2 | 2 | 297, 715 |
| `Konflikt-Anker` | 1 | 1 | 719 |
| `System-Ebene` | 1 | 1 | 719 |
| `Kapitel-Briefing` | 1 | 4 | 13, 29, 725, 731 |
| `Sektionen` | 2 | 2 | 29, 725 |
| `Format-Quelle` | 1 | 1 | 727 |
| `CH-01_Erwachen-Zyklus_Briefing.md` | 0 | 0 |  |
| `Template` | 1 | 1 | 727 |
| `Briefings` | 2 | 2 | 727, 1390 |
| `Storyform-Encoding` | 1 | 1 | 727 |
| `Telling` | 1 | 1 | 727 |
| `Strukturelle Position` | 1 | 1 | 735 |
| `Block` | 1 | 4 | 739, 755, 963, 1119 |
| `HR innen` | 1 | 1 | 739 |
| `zyklisch` | 2 | 3 | 475, 739, 743 |
| `HR außen` | 1 | 1 | 739 |
| `Vortex` | 17 | 23 | 113, 117, 162, 274, 351, 445 … |
| `Reward` | 1 | 2 | 739, 1140 |
| `Apotheose` | 6 | 6 | 594, 739, 1141, 1173, 1187, 1224 |
| `Modus` | 2 | 7 | 31, 79, 625, 743, 1126, 1142 … |
| `linear-introspektiv` | 1 | 1 | 743 |
| `zyklisch-rekursiv` | 1 | 1 | 743 |
| `linear-aufsteigend` | 1 | 1 | 743 |
| `vortex-still` | 1 | 1 | 743 |
| `HR-Stufe` | 1 | 1 | 747 |
| `HR-Bogen` | 1 | 1 | 747 |
| `HR` | 2 | 4 | 739, 747 |
| `Zyklus-Position` | 1 | 1 | 751 |
| `Z1-Trigger` | 1 | 1 | 751 |
| `Z1-Reaktion` | 1 | 1 | 751 |
| `Z1-Korrektur` | 1 | 1 | 751 |
| `Block-Sequenz-Position` | 1 | 1 | 755 |
| `Eröffnung` | 1 | 1 | 755 |
| `Schwellpunkt` | 1 | 1 | 755 |
| `Dramatica-Encoding` | 1 | 1 | 759 |
| `Dramatica` | 0 | 1 | 759 |
| `Throughline` | 2 | 4 | 763, 767, 1162, 1163 |
| `Storyform-Status` | 2 | 2 | 763, 1015 |
| `A‖B` | 2 | 2 | 763, 1015 |
| `A-Storypoint` | 1 | 1 | 767 |
| `B-Storypoint` | 1 | 1 | 767 |
| `Storypoint` | 0 | 3 | 767, 991 |
| `Aktivität` | 1 | 5 | 345, 346, 382, 674, 767 |
| `latent` | 1 | 1 | 767 |
| `aktiv` | 4 | 8 | 498, 582, 608, 767, 791, 951 … |
| `dominant` | 1 | 4 | 767, 811, 1019, 1199 |
| `Szenen-Keim` | 1 | 1 | 767 |
| `MC` | 2 | 3 | 775, 1162, 1432 |
| `IC` | 1 | 2 | 779, 1163 |
| `OS` | 1 | 2 | 42, 783 |
| `RS` | 1 | 1 | 787 |
| `Psychology` | 2 | 2 | 783, 787 |
| `Physics` | 2 | 2 | 783, 787 |
| `Dynamics-Check` | 1 | 1 | 791 |
| `Storyform` | 2 | 14 | 425, 608, 727, 763, 791, 1015 … |
| `Approach` | 2 | 3 | 175, 791, 1164 |
| `Driver` | 2 | 2 | 791, 1164 |
| `Limit` | 2 | 3 | 791, 1027, 1164 |
| `Resolve` | 2 | 2 | 791, 1164 |
| `Style` | 2 | 2 | 791, 1164 |
| `POV & Stimme` | 1 | 1 | 795 |
| `POV` | 1 | 8 | 795, 807, 939, 1019, 1120, 1165 … |
| `Pronomenpraxis` | 1 | 1 | 799 |
| `Tempus` | 1 | 1 | 803 |
| `Syntax-Signatur` | 2 | 2 | 807, 1120 |
| `POV-Träger` | 3 | 4 | 807, 939, 1019, 1120 |
| `Sprach-DNA-Anker` | 2 | 2 | 811, 1019 |
| `Sprach-DNA` | 2 | 4 | 811, 1019, 1231, 1483 |
| `dominanter Anteil` | 0 | 0 |  |
| `Anteil` | 1 | 13 | 13, 399, 584, 811, 855, 951 … |
| `Multiplizitäts-Tarnung` | 1 | 1 | 815 |
| `Schleier-Pegel` | 1 | 1 | 819 |
| `vollständig intakt` | 1 | 1 | 819 |
| `erste interne Lüftung` | 1 | 1 | 819 |
| `partiell offen` | 1 | 1 | 819 |
| `offen benannt` | 2 | 2 | 588, 819 |
| `Prosa-Stil` | 1 | 1 | 831 |
| `Stilebene-Default` | 1 | 1 | 835 |
| `Kompositionsregel pro Szene` | 1 | 1 | 839 |
| `Tonale Achse` | 1 | 1 | 843 |
| `Schmerz-Liebe-Substrat` | 1 | 1 | 843 |
| `KW-Default-Sensorik` | 1 | 1 | 851 |
| `Anteils-Somatik` | 1 | 1 | 855 |
| `Anteile-Profile` | 1 | 1 | 855 |
| `Hitze-Polaritäts-Check` | 2 | 2 | 859, 1023 |
| `Aktive Spuren` | 1 | 1 | 867 |
| `Genesis-Motiv-Echo` | 1 | 1 | 871 |
| `Anker-Verwendung` | 1 | 1 | 875 |
| `734-Anker` | 1 | 2 | 482, 875 |
| `Silas-Anker` | 1 | 1 | 875 |
| `Wärme-Spur` | 1 | 1 | 875 |
| `Vortex-Vorbereitungen` | 1 | 1 | 883 |
| `Genesis-Krise-Splitter` | 1 | 1 | 895 |
| `Schicht-2-Spuren` | 1 | 1 | 899 |
| `Algorithmische-Melancholie-Vorausschau` | 1 | 1 | 903 |
| `Ouroboros-Spiegelung` | 1 | 4 | 13, 27, 614, 911 |
| `Reader-Architektur` | 1 | 1 | 919 |
| `Iser-3-Layer` | 1 | 1 | 923 |
| `Konflikt-Topologie` | 1 | 1 | 947 |
| `Anteil-Konflikt` | 1 | 1 | 951 |
| `Rhys` | 1 | 1 | 951 |
| `Selene` | 1 | 1 | 951 |
| `ANP-EP-Phobie-Pegel` | 1 | 1 | 955 |
| `ANP-EP-Phobie` | 0 | 1 | 955 |
| `Block-4-Anker-Check` | 2 | 2 | 963, 1119 |
| `Block 4` | 0 | 0 |  |
| `Risiko-/Adversarial-Check` | 1 | 1 | 971 |
| `R-Regel` | 1 | 2 | 975, 1039 |
| `Soft-Drift-Risiken` | 1 | 1 | 979 |
| `Stapelungs-Risiken` | 1 | 1 | 983 |
| `Stimmen-Brüche` | 1 | 1 | 983 |
| `Cross-References` | 1 | 1 | 987 |
| `Vorgänger-Kapitel` | 0 | 1 | 995 |
| `Offene Fragen` | 1 | 1 | 999 |
| `OQ` | 1 | 10 | 498, 678, 1007, 1195, 1428, 1429 … |
| `Checkliste` | 1 | 2 | 1011, 1102 |
| `Genesis-Echo-Limit` | 1 | 1 | 1027 |
| `Reveal-Schicht` | 1 | 1 | 1031 |
| `Ouroboros-Pflicht` | 1 | 1 | 1035 |
| `R-Regel-Vorab-Check` | 1 | 1 | 1039 |
| `Kap-0-Annotation` | 3 | 3 | 1047, 1089, 1461 |
| `Defekt` | 2 | 3 | 1047, 1089, 1146 |
| `Globale Hard Rules` | 1 | 1 | 1049 |
| `R-1 — Tragische Ironie nicht auflösen` | 1 | 1 | 1051 |
| `AEGIS hat die Geburt für den Tod gehalten` | 1 | 1 | 1051 |
| `Erzähler-Hinweis` | 2 | 2 | 1051, 1059 |
| `Klammer-Kommentare` | 1 | 1 | 1055 |
| `meta-narrative Einschübe` | 0 | 0 |  |
| `R-3 — Multiplizitäts-Schleier intakt halten` | 1 | 1 | 1059 |
| `Alter` | 2 | 3 | 1059, 1185, 1428 |
| `Fragment` | 1 | 2 | 1059, 1460 |
| `TSDP` | 1 | 1 | 1059 |
| `Syntax-Bruch` | 1 | 1 | 1059 |
| `R-4 — Maximal drei Stimmen-Mikrocues pro Bridge-Szene` | 1 | 1 | 1063 |
| `Stimmen-Mikrocues` | 1 | 1 | 1063 |
| `Bridge-Szene` | 1 | 2 | 1063, 1226 |
| `Stimmen-Einbrüche` | 1 | 1 | 1063 |
| `R-5 — Hitze-Polaritätsregel` | 1 | 1 | 1067 |
| `R-6 — Maximal 1 Konzept pro Szene` | 1 | 1 | 1071 |
| `R-7 — Maximal 1 Genesis-Echo pro Szene` | 1 | 1 | 1075 |
| `R-8 — AEGIS spricht nie metaphorisch` | 1 | 1 | 1079 |
| `R-9 — Genesis-Stil-Marker werden nie wörtlich wiederholt` | 1 | 1 | 1083 |
| `Genesis-Stil-Marker` | 1 | 1 | 1083 |
| `Defekt-Kategorien` | 1 | 1 | 1089 |
| `Schweregrad` | 1 | 1 | 1091 |
| `Kritisch` | 1 | 1 | 1098 |
| `M-1` | 1 | 1 | 1098 |
| `M-2` | 1 | 1 | 1099 |
| `M-3` | 1 | 1 | 1098 |
| `M-4` | 2 | 2 | 1098, 1100 |
| `M-5` | 1 | 1 | 1099 |
| `Mittel` | 3 | 3 | 1099, 1450, 1452 |
| `Niedrig` | 1 | 1 | 1100 |
| `N-1` | 1 | 1 | 1100 |
| `N-2` | 1 | 1 | 1100 |
| `N-3` | 1 | 1 | 1100 |
| `Erzähler-Wertung` | 1 | 1 | 1098 |
| `Reviewer` | 2 | 2 | 1099, 1100 |
| `Self-Review-Checkliste` | 1 | 1 | 1102 |
| `R-1-Check` | 1 | 1 | 1108 |
| `R-10-Check` | 1 | 1 | 1117 |
| `Tonale-Achse-Check` | 1 | 1 | 1118 |
| `POV-Konsistenz-Check` | 1 | 1 | 1120 |
| `Grundlinie` | 1 | 1 | 1128 |
| `Hard-SF` | 1 | 1 | 1128 |
| `Philosophical Horror` | 2 | 2 | 1128, 1135 |
| `Psychological Thriller` | 1 | 1 | 1128 |
| `Egan` | 1 | 2 | 1128, 1138 |
| `Chiang` | 1 | 1 | 1128 |
| `Lem` | 1 | 2 | 1128, 1136 |
| `Tarkowski` | 1 | 2 | 1128, 1138 |
| `Kawabata` | 1 | 2 | 1128, 1141 |
| `VanderMeer` | 1 | 1 | 1128 |
| `Watts` | 1 | 2 | 1128, 1137 |
| `PKD` | 1 | 1 | 1128 |
| `Physik-Rigor` | 1 | 1 | 1128 |
| `KI-Tragödie` | 1 | 1 | 1128 |
| `Bildhaftigkeit` | 1 | 2 | 1128, 1138 |
| `japanische Erzähllogik` | 1 | 1 | 1128 |
| `kognitive Härte` | 1 | 1 | 1128 |
| `Realitätsbruch` | 1 | 1 | 1128 |
| `Genre-Akzent` | 1 | 1 | 1134 |
| `ontologische Grundlegung` | 1 | 1 | 1135 |
| `kosmische Schauder` | 1 | 1 | 1135 |
| `SF-Mechanik` | 1 | 1 | 1135 |
| `Literary SF` | 1 | 1 | 1136 |
| `Horror-Anflug` | 1 | 1 | 1136 |
| `Lem-Tonalität` | 1 | 1 | 1136 |
| `Thriller-Pacing` | 2 | 2 | 1136, 1146 |
| `Technothriller-Kippe` | 1 | 1 | 1137 |
| `algorithmisches Gefängnis` | 0 | 0 |  |
| `Watts-Härte` | 1 | 1 | 1137 |
| `Sentimentalität` | 1 | 1 | 1137 |
| `chorisches Drama` | 1 | 1 | 1138 |
| `kosmische Konfrontation` | 1 | 1 | 1138 |
| `Vor-Vortex-Spannung` | 1 | 1 | 1138 |
| `Egan-Rigor` | 1 | 1 | 1138 |
| `Tarkowski-Bildhaftigkeit` | 1 | 1 | 1138 |
| `Akt-II-Eskalation` | 1 | 1 | 1138 |
| `metaphysischer Klimax` | 1 | 1 | 1139 |
| `stille Mechanik` | 1 | 1 | 1139 |
| `Soft-Layering` | 1 | 2 | 1139, 1165 |
| `Dialetheia` | 1 | 1 | 1139 |
| `trügerischer Pastoralismus` | 1 | 1 | 1140 |
| `Reward-Beat` | 1 | 1 | 1140 |
| `kristallisierte Ruhe` | 1 | 1 | 1140 |
| `spirituelle Apotheose` | 1 | 1 | 1141 |
| `Kawabata-Erzähllogik` | 1 | 1 | 1141 |
| `ketsu` | 1 | 1 | 1141 |
| `Theorie-Predigt` | 1 | 1 | 1141 |
| `geheilte Genesis` | 1 | 1 | 1142 |
| `Erläuterungs-Modus` | 1 | 1 | 1142 |
| `Genre-Disziplin` | 1 | 1 | 1146 |
| `Akt-Modus` | 1 | 1 | 1146 |
| `Erzählformen` | 1 | 1 | 1146 |
| `Lock` | 13 | 33 | 13, 32, 90, 326, 386, 478 … |
| `Storyform-Locks` | 1 | 1 | 1156 |
| `Lock-In 2026-05-07` | 2 | 2 | 1156, 1161 |
| `Dual-Storyform` | 2 | 2 | 1161, 1501 |
| `Heuristics of Integration` | 1 | 1 | 1161 |
| `Phoenix Collapse` | 1 | 1 | 1161 |
| `Storyforming Lock-In 2026-05-07` | 1 | 1 | 1161 |
| `MC-Throughlines` | 1 | 1 | 1162 |
| `Mind/Memory` | 1 | 1 | 1162 |
| `Universe/Progress` | 1 | 1 | 1162 |
| `IC-Throughlines` | 1 | 1 | 1163 |
| `Universe/Past` | 1 | 1 | 1163 |
| `Mind/Conscious` | 1 | 1 | 1163 |
| `Growth` | 1 | 1 | 1164 |
| `Outcome` | 1 | 1 | 1164 |
| `Judgment` | 1 | 1 | 1164 |
| `Storyform-Dokument` | 1 | 1 | 1164 |
| `POV-Architektur` | 1 | 1 | 1165 |
| `Hybrid Option 3` | 1 | 1 | 1165 |
| `Hard-Routing-Default` | 1 | 1 | 1165 |
| `Bridge-Soft-Layering` | 1 | 1 | 1165 |
| `Genesis-Iteration-Locks` | 1 | 1 | 1167 |
| `Cost/Dividend` | 1 | 1 | 1172 |
| `A-Cost` | 1 | 1 | 1172 |
| `A-Dividend` | 1 | 1 | 1172 |
| `B-Cost` | 1 | 1 | 1172 |
| `B-Dividend` | 1 | 1 | 1172 |
| `Verlust der Privatheit des Wir` | 1 | 1 | 1172 |
| `Liebe bleibt` | 3 | 3 | 629, 1172, 1187 |
| `AEGIS-monolithisch` | 1 | 1 | 1172 |
| `plurale Übernahme` | 1 | 1 | 1172 |
| `Konzept konsolidiert 2026-05-08` | 1 | 1 | 1172 |
| `Plurale Apotheose` | 1 | 1 | 1173 |
| `Synthese (c)` | 1 | 1 | 1173 |
| `Genesis-4-Beat` | 1 | 1 | 1174 |
| `Einheit` | 4 | 4 | 101, 487, 1174, 1200 |
| `Cluster` | 1 | 4 | 524, 539, 1174, 1464 |
| `Drei ontologische Schichten` | 1 | 1 | 1175 |
| `K₀-Existenz` | 1 | 1 | 1175 |
| `Juna als Zeit-Prinzip` | 1 | 1 | 1175 |
| `Reset-Locks` | 1 | 1 | 1178 |
| `Architektur-Reduktion` | 1 | 1 | 1178 |
| `Zwei Guardians` | 1 | 1 | 1183 |
| `Drei Protokolle` | 1 | 1 | 1184 |
| `Suppression-Protokoll` | 0 | 0 |  |
| `Kohärenz` | 2 | 3 | 11, 539, 1184 |
| `Re-Containment` | 1 | 1 | 1184 |
| `13 Alter` | 1 | 1 | 1185 |
| `Roster` | 1 | 1 | 1185 |
| `dekanonisierte Namen` | 1 | 1 | 1185 |
| `Kein Final Fusion` | 1 | 1 | 1186 |
| `Final Fusion` | 1 | 1 | 1186 |
| `Verschmelzung` | 1 | 1 | 1186 |
| `Kein Reset/Race-Condition-Ende` | 1 | 1 | 1187 |
| `Race-Condition` | 0 | 1 | 1187 |
| `Kein Michael` | 1 | 1 | 1188 |
| `Michael` | 1 | 1 | 1188 |
| `Hauptfigur` | 1 | 1 | 1188 |
| `2026-05-30-Locks` | 1 | 1 | 1190 |
| `Entscheidungs-Logs` | 1 | 1 | 1190 |
| `OQ-B` | 1 | 1 | 1195 |
| `Juna-Modi` | 1 | 1 | 1195 |
| `gestaffelte Grammatik` | 1 | 1 | 1195 |
| `Abwesenheits-Phase` | 1 | 1 | 1195 |
| `Präsenz-Phase` | 1 | 1 | 1195 |
| `Log 2026-05-30` | 1 | 1 | 1195 |
| `Wärme-Debüt` | 1 | 2 | 502, 1196 |
| `Slot-16` | 1 | 2 | 583, 1197 |
| `Hard-A-Default` | 1 | 1 | 1197 |
| `Hard-B-Kapitel` | 1 | 2 | 1197, 1431 |
| `AEGIS-Stimme` | 3 | 3 | 1100, 1115, 1198 |
| `UI-Direktiven` | 1 | 1 | 1198 |
| `3.-P-Systemlog-Stimme` | 1 | 1 | 1198 |
| `80/20 Schicht-1/Schicht-2` | 1 | 1 | 1199 |
| `Schicht-1` | 1 | 1 | 1199 |
| `Schicht-2` | 1 | 4 | 496, 899, 1199 |
| `Schicht-2-dominant` | 1 | 1 | 1199 |
| `Silas-Halbsatz` | 1 | 2 | 492, 1201 |
| `Kap-1-Erstsatz` | 1 | 1 | 1202 |
| `Ouroboros-Lock` | 1 | 1 | 1202 |
| `Doppellesbares Finale Kap 40` | 1 | 1 | 1203 |
| `Konflikt-Leser` | 1 | 1 | 1203 |
| `Ketsu-Leser` | 1 | 1 | 1203 |
| `Konzept Kap 40 Lesart-Dualität` | 1 | 1 | 1203 |
| `2026-05-31-Locks` | 1 | 1 | 1205 |
| `Kompendium` | 1 | 2 | 1205, 1211 |
| `Blutungs-Faden` | 1 | 1 | 1210 |
| `Akt-II-Titel-Schichten` | 1 | 1 | 1211 |
| `Kompendium-Theorie-Titel` | 1 | 1 | 1211 |
| `Turing-Mechanik` | 1 | 1 | 1211 |
| `Zyklus-Funktion` | 1 | 1 | 1211 |
| `Genesis-Beat-Anzahl` | 1 | 1 | 1212 |
| `Beat 4` | 5 | 5 | 351, 445, 508, 1067, 1212 |
| `Hard-Constraints` | 1 | 1 | 1214 |
| `Projekt-Anleitung` | 1 | 1 | 1216 |
| `didaktischer Tonfall` | 1 | 1 | 1220 |
| `Bösewicht` | 1 | 1 | 1221 |
| `Liebes-Interesse` | 1 | 1 | 1222 |
| `Bridge-Szenen-Stapelung` | 1 | 1 | 1226 |
| `Kap 9` | 1 | 1 | 1227 |
| `Wir-Geflecht-Etablierung` | 1 | 1 | 1227 |
| `Resolution-Glättung` | 1 | 1 | 1228 |
| `Hard-Rules der Sprach-DNA` | 1 | 1 | 1231 |
| `Alex` | 3 | 5 | 1234, 1456, 1460, 1461, 1465 |
| `Kopf runter` | 1 | 1 | 1234 |
| `Stimmen werden nie gelabelt` | 1 | 1 | 1237 |
| `Lexikon` | 1 | 1 | 1237 |
| `Somatik` | 2 | 7 | 79, 144, 201, 257, 847, 855 … |
| `Repo-Architektur` | 0 | 3 | 13, 33, 1243 |
| `Datei-Struktur` | 1 | 1 | 1247 |
| `User-Entscheidung` | 1 | 1 | 1245 |
| `canon/` | 1 | 5 | 1257, 1401, 1402, 1404 |
| `Source-of-Truth` | 2 | 2 | 1257, 1410 |
| `locks/` | 1 | 2 | 1277, 1404 |
| `kap-1-locks_2026-05-30.md` | 0 | 0 |  |
| `kap-40-lesart-dualitaet.md` | 1 | 1 | 1285 |
| `master-index_2026-06-10.md` | 0 | 0 |  |
| `archive/` | 1 | 1 | 1293 |
| `steinbruch/` | 1 | 1 | 1297 |
| `briefings/` | 1 | 2 | 1301, 1403 |
| `CH-00_Genesis-Prolog.md` | 0 | 0 |  |
| `CH-01_Erwachen-Zyklus.md` | 0 | 0 |  |
| `CH-40_Geheilte-Genesis.md` | 0 | 0 |  |
| `Genesis-Prolog` | 0 | 1 | 1305 |
| `Erwachen-Zyklus` | 0 | 2 | 727, 1309 |
| `Geheilte Genesis` | 0 | 0 |  |
| `drafts/` | 1 | 2 | 1321, 1405 |
| `kap-00_v1-annotiert.md` | 0 | 0 |  |
| `kap-00_v2.md` | 0 | 0 |  |
| `kap-01_v0-3.md` | 0 | 0 |  |
| `kap-39_v1.md` | 0 | 0 |  |
| `kap-40_v1.md` | 0 | 0 |  |
| `reviews/` | 1 | 1 | 1349 |
| `Self-Reviews` | 1 | 1 | 1349 |
| `encoding/` | 1 | 1 | 1361 |
| `NCP-Schicht` | 1 | 1 | 1361 |
| `NCP` | 0 | 2 | 1361, 1409 |
| `Storyform-JSON` | 1 | 1 | 1361 |
| `ncp.json` | 1 | 1 | 1365 |
| `ncp-author` | 1 | 2 | 1365, 1409 |
| `ncp-author-Skill` | 1 | 1 | 1409 |
| `snapshots/` | 1 | 1 | 1369 |
| `notes/` | 1 | 1 | 1373 |
| `Phoenix-Mode` | 0 | 1 | 1373 |
| `Phoenix-Mode-Diskussionen` | 1 | 1 | 1373 |
| `oq-tracker.md` | 1 | 1 | 1377 |
| `learnings.md` | 1 | 1 | 1381 |
| `Naming-Konventionen` | 1 | 1 | 1387 |
| `Sessions-Bootstrap-Reihenfolge` | 1 | 1 | 1394 |
| `Hard-Stops` | 1 | 1 | 1407 |
| `Canon-Dateien` | 1 | 1 | 1410 |
| `Canon-Mutationen` | 1 | 1 | 1410 |
| `Entscheidungs-Log` | 1 | 2 | 1190, 1410 |
| `Encoding-blockierend` | 1 | 1 | 1422 |
| `KW2-Klimax-Setting` | 1 | 1 | 1427 |
| `Vortex-1-Encoding` | 1 | 1 | 1427 |
| `Spiegel-Alter` | 0 | 1 | 1428 |
| `Spiegel-Alter-POV-Anteile` | 1 | 1 | 1428 |
| `OQ-F` | 1 | 1 | 1429 |
| `Moonshine-Boundary` | 1 | 1 | 1429 |
| `OQ-G` | 1 | 1 | 1430 |
| `Post-Vortex-AEGIS-Status` | 1 | 1 | 1430 |
| `lebende Reliquie` | 1 | 1 | 1430 |
| `Oblivion-Übernahme` | 1 | 1 | 1430 |
| `Hard-B-Kapitel-Position` | 1 | 1 | 1431 |
| `Slot 16` | 1 | 1 | 1431 |
| `Storyweaving` | 1 | 1 | 1431 |
| `MC Symptom & Response` | 1 | 1 | 1432 |
| `TBD-Slots` | 1 | 1 | 1432 |
| `14-Frage-Sequenz` | 1 | 1 | 1432 |
| `OQ-D` | 1 | 1 | 1432 |
| `P5` | 1 | 1 | 1432 |
| `Blutungs-Wiederkehr` | 1 | 1 | 1439 |
| `Junas Erscheinungsmodus` | 1 | 1 | 1441 |
| `Ankerpunkt-Lock` | 1 | 1 | 1441 |
| `Bekenstein-Strang` | 1 | 1 | 1449 |
| `Temporal Scrambling` | 1 | 1 | 1451 |
| `Sich-ausschließende Epiloge` | 1 | 1 | 1452 |
| `Genesis-Konflikt` | 1 | 1 | 1454 |
| `Alex-vor-Trennungsprotokoll-Konflikt` | 1 | 1 | 1456 |
| `Fragmentierung` | 1 | 1 | 1460 |
| `Alex-Vorform` | 1 | 1 | 1461 |
| `Bewegung 4` | 1 | 1 | 1461 |
| `Konzept-Konflikt` | 1 | 1 | 1462 |
| `Kap-0-Pass` | 1 | 1 | 1462 |
| `Funktion vor Person` | 1 | 1 | 1464 |
| `Stimmen-Vorformen` | 1 | 1 | 1464 |
| `Proto-Cluster` | 1 | 1 | 1464 |
| `13 Meta-Stadien` | 1 | 1 | 1467 |
| `Meta-Stadien` | 1 | 1 | 1467 |
| `ontologischer Heilungs-Bogen` | 1 | 1 | 1469 |
| `Heldinnenreise` | 1 | 1 | 1469 |
| `Lock-Entscheidung` | 1 | 1 | 1469 |
| `Hintergrund-Konzept` | 1 | 1 | 1469 |
| `Beat-Mapping` | 1 | 1 | 1469 |
| `Schluss-Notiz` | 1 | 1 | 1475 |
| `KI-System` | 1 | 1 | 1488 |
| `OQ-Entscheidung` | 1 | 1 | 1488 |
| `ontologische Tiefe` | 1 | 1 | 1492 |
| `tragische Unschuldsstruktur` | 1 | 1 | 1492 |
| `schmerzhaft-liebevolle Tonalität` | 1 | 1 | 1492 |
| `ontologische Heilungs-Schleife` | 1 | 1 | 1500 |
| `Form der Trennung` | 1 | 1 | 1501 |
| `Wiederzusammenfinden` | 1 | 1 | 1501 |

### What the count corrected

| term | word | incl. compounds | what it means |
|---|--:|--:|---|
| `[K]`, `[V]`, `[S]`, `[L]` | 0 | 0 | escaped, `\[K\]` in prose and `\\\[L\\\]` in tables — counted above over every escaping |
| the ten file names (`storyform-und-outline_2026-06-10.md`, `CH-01_Erwachen-Zyklus_Briefing.md`, `kap-00_v2.md` …) | 0 | 0 | escaped, `storyform-und-outline\_2026-06-10.md` |
| `Guardian-zugeordnete Welten`, `kognitiver Apparat`, `innere Praxis`, `finale Selbst-Schöpfung`, `MI-dichtes Ziel`, `aktiver Transmitter`, `plurale Heilung`, `dominanter Anteil`, `meta-narrative Einschübe`, `algorithmisches Gefängnis`, `indirektes quellenloses Licht` | 0 | 0 | the reader's nominative; the document declines them (`kognitiven Apparat` L46, `MI-dichtem Ziel` L351) |
| `Erinnerung als Schauplatz` | 0 | 0 | emphasis inside: „Erinnerung als *Schauplatz*" ^[L113] |
| `Stil 2`, `Kap 26`, `Kap 32`, `Block 4` | 0 | 0 | only in ranges and compounds: „Stil 1 und 2" ^[L374], `Kap 25–26`, `Kap 31/32`, `Block-4-Anker-Check` |
| `Geheilte Genesis` | 0 | 0 | lower case in the genre table (L1142), hyphenated in a file name (L1317) |
| `Suppression-Protokoll` | 0 | 0 | the reader's name for the first of the „Drei Protokolle" ^[L1184], Suppression, Kohärenz and Re-Containment |
| `Cerberus`, `Wächter`, `Kant`, `Heidegger`, `Erason`, `Iser`, `NCP`, `Dramatica`, `Logikregime`, `K₀` and eleven more | 0 | ≥1 | only inside compounds or inflected: `Cerberus-Labyrinth` (L169), `Wächter-Konsolen` and `Wächter-Registry` (L286, L298), `Kants` (L46), `Erason-Operator` (L410) |

## Surfaces — one thing wearing several names

- **Every world has two or three names.** „KW1 — Konstrukt-Stadt
  (Logos-Prime)" ^[L44], „KW2 — Mnemosyne-Archipel (Resonanzlandschaft,
  Klimax-Setting)" ^[L111], „KW3 — Cerberus-Labyrinth (Grenzfeste)" ^[L169],
  „KW4 — Kairos-Potentialis / Resonanz-Kontinuum / Möglichkeits-Garten"
  ^[L225], „Überwelt — AEGIS' Maschinenraum" ^[L280], also
  `Datenstrom-Kathedrale` (L282), and „Externe Ebene — Köln 2026" ^[L305].
- **`Komponente 734`, `Komp 734`, `Komp-734`, `Einheit 734`, `Wohneinheit 734`,
  `Zahl 734`, `734-Anker`.** Kael's designation, its abbreviations, the console
  line and his flat (L101, L105, L486–L489).
- **The thermal rule has four names**: `Hitze-Polaritätsregel` (L337),
  `Polaritätsregel` (L63), `Polaritäts-Lock 2026-05-30` (L506) and
  `R-5 — Hitze-Polaritätsregel` (L1067); its check is the
  `Hitze-Polaritäts-Check` (L859).
- **The knuckles**: `Blutende Knöchel` (L90), `Knöchel-Blutung` (L386, L445,
  L678), `Blutungs-Faden (Knöchel)` (L1210), `OQ-Knöchel` (L678, L1439).
- **`K-J-Verbindung` and `K-J-Kanal`** (L474, L476, L589).
- **`Verschränkungs-Insel` and `Jenseits-des-Ereignishorizonts-Bereich`** name one
  place (L299).
- **`funktionale Multiplizität`, `Funktionale Multiplizität`, `FM-Achievement`**
  (L227, L590, L1186).
- **The veil**: `Multiplizitäts-Schleier` (L50), `Schleier-Fall` (L462),
  `Schleier-Lüftung` (L572), `Schleier-Pegel` (L819).

## Boundaries — one name wearing several things

- **`Ebene` numbers three series.** The six levels of one reality (§1); the
  three style levels, where „Ebene 2 — heiß, fragmentiert." ^[L140]; and the
  three levels of „Drei Ebenen des Show-don't-Tell" ^[L451], where Ebene 2 is the
  linguistic traces — „Phantom-Bilanz als sprachliche Spur (Ebene 2)" ^[L547].
- **`Schicht` numbers two.** The „drei Bewusstseins-Schichten" ^[L563] of §6 are
  reader, Kael and AEGIS (L563–L574); `Schicht-2-gekoppelt` (L496), `Schicht-2-Spuren`
  (L899) and „80/20 Schicht-1/Schicht-2 in Kap 1" ^[L1199] use another,
  defined nowhere here.
- **`Nexus`** is a KW4 place, „Knotenpunkt mehrerer Realitätsstränge" ^[L273],
  and the `Überwelt-Nexus` of Kap 33, written into KW3's section: „Auch:
  Überwelt-Nexus im Approach-Inmost-Cave-Beat (Kap 33)." ^[L175]
- **`Mosaik`** is the KW4 place `Mosaik-Herz` (L274) and Kap 40's last image,
  „das Mosaik, das die Welt hält" ^[L629].
- **`Resonanz`** is a Genesis motif (L527), a name of KW4
  (`Resonanz-Kontinuum`), KW2's `Resonanzlandschaft`, and a crisis beat of Kap 0
  (`Resonanzkaskade`, L627).
- **`Echo`** is a sound in KW2 (L129), a Spiegel-Alter's kind
  (`Coheron-Echo`, L409), the relation of Kap 40 to Kap 0 (`Kap-40-Echo`, L624),
  and a unit of the drafting rules (`Motiv-Echo`, `Genesis-Echo`,
  `Reader-only-Echo`, `Lexem-Echo`).
- **`Erasure`** is AEGIS' activity (`Erasure-Sweeps`, `Erasure-Welle`,
  `Erasure-Phase 2`, `Erasure-Bilanzen`) and one of two Guardians,
  `Erasure-Pol`.
- **`da`** — the document names the double meaning itself: „Licht-an/präsent ↔ Dasein/Sein" ^[L637].

## Gaps — used as known, defined nowhere here

Used as known: `K₀`, `K₁`, `K₁-Reinform`, `Coheron`, `Erason`, `MI` (L351, L449,
L523), `Moonshine-Resonanz`, `Korrelat-Achse`, `Landauer-Signatur`,
`Multiplizitäts-Schleier`, `Slot-16`, `Truth-Rotation`, `Gödel-Gambit`,
`Bridge`, `HR-Stufe`, `Z1-Trigger`, `TSDP`, `ANP`, `EP`, `Lernarchiv
Theta-9`, `Cache-Konflikt`, `NCP`, `ncp-author`, the OQ letters B, D, E, F and
G, the defect codes M-1 to M-5 and N-1 to N-3, `P5`, the `14-Frage-Sequenz`,
and the `Projekt-Anleitung §10` it mirrors in §12.6.

Named as sources and not in the document: its three siblings (L13), the
`Charakter-Bibel` (L700, L1460), the `Kap-0-Annotation` (L1047, L1461), the
`Kompendium` (§12.5), the `Log 2026-05-30` (L1195), the `Storyforming Lock-In
2026-05-07` (L1161), `Konzept konsolidiert 2026-05-08` (L1172),
`Konzept Kap 40 Lesart-Dualität` (L1203) and `CH-01_Erwachen-Zyklus_Briefing.md`
(L727).

Marked as gaps by the document itself: the Mnemosyne-Server-Architektur's image
(L162, L1427), `Junas Ankerpunkt` in Köln (L326, L1441), the form of the
knuckles' return (L678, L1439), and whether the counting mania ends (L679).

## Self-consistency

- **It de-canonises „6 Realitätsebenen" ^[L42] under the heading
  „Sechs Ebenen einer Realität" ^[L40].** Its own distinction is one reality
  with four logic regimes „plus Überwelt und Externe Ebene" ^[L42], so six
  levels of one reality.
- **It de-canonises the Guardian-assigned worlds (L42) and keeps the Guardians'
  names in the worlds' names** — Logos-Prime, Mnemosyne-Archipel,
  Cerberus-Labyrinth, Kairos-Potentialis — without a word on why.
- **Landauer is heat in one table and cold in another.** The strand is
  „Hitze als Symptom der Wahrheitsvertuschung" ^[L445]; the polarity rule files
  the Landauer-Signatur under cold ozone, „AEGIS-Unterdrückung /
  Landauer-Signatur" ^[L346], as KW1's sensory default does: „Polaritätsregel:
  Ozon = kalt/scharf, Landauer-Signatur" ^[L63]. It calls both signatures
  „die beiden Hitzen" ^[L351], and the world riss of the KW1→KW2 transition is
  thermal with „Hitze-Spitzen, Ozon-Konzentration" ^[L418], beside a rule that
  the two are never mixed after Kap 1 (L351).
- **Two riss typologies, and §1 mixes them.** §3.1 types Risse by the Alter who
  triggers them, §3.2 by world. §1 gives KW2 „Temporale Risse (Kiko-Trigger),
  spatiale Risse (Lia/Isabelle-Trigger)." ^[L148] and KW3 spatial,
  gravitational and kinetic ones (L205), where §3.2 gives KW2 `wässrig /
  mnemonisch` and KW3 `paranoid` (L419, L420). The spatial trigger is
  Lia/Isabelle in §1 and „Kiko/Lia (Flight)" ^[L406] in §3.1, where Isabelle's
  type is sensory (L408).
- **AEGIS in the first person without „Ich".** Kap 5–8 is where the reader
  „sieht AEGIS in 1. Person" ^[L583]; the Sprach-DNA rules say „AEGIS verwendet
  nie das Wort" ^[L1236] „Ich". The document does not relate the two.
- **The knuckles are a KW1 riss that lives in Kap 0** (L90), and KW1 is Akt I,
  Kap 1–13 (L50).
- **Kap 0's Genesis is counted three ways, on three axes, without conflict**:
  four beats, „Einheit → Cluster → Trennungsprotokoll → Wir-AEGIS-plural"
  ^[L1174], again „vier Beats (mit Wir-AEGIS-plural als Beat 4)" ^[L1212]; five
  motifs as first events (L516–L527); a crisis in six steps from Stille Wacht to
  Trennungsprotokoll (L627).
- **It names one conflict of its own sources** (§14.4): the Charakter-Bibel has
  Alex arise „in der Sekunde der Fragmentierung" ^[L1460], the Kap-0-Annotation has an
  Alex-Vorform before the Trennungsprotokoll (L1460–L1461), and it leaves two
  options open.
