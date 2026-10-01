# Quantities — the testbed's results

> Quantities — a number the document binds to what it counts, measures or names, with that sentence.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the wiki's question on what the number 734 names, and the chapter counts the sources give differently (39 or 40).
> A number is not a term, so the mechanical MENTIONS relation never carries one; the subject a number belongs to is a
> reading of the sentence.
> measured against: the numbers the wiki's pages and conflict records quote; a value that stands inside its quote is the precise subset, and code checks it. A quote is placed by read.py --find (P26).
> may not: compare two documents' numbers — a difference between them is a conflict, and conflicts are read, never detected — or decide which is right
> retire when: on three documents a person keeps no quantity beyond what the pages already quote

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/quantities-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0568, 20.7 s. **5 rows**: 5 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | „Stasis-Lücken“ | Teil 1 | duration | asserts | Das Phänomen der „Stasis-Lücken“ (Teil 1) | 15 |
| 2 | relation_reading | candidate | „Höhere Metrik“ | Teil 2 | duration | asserts | AEGIS und die „Höhere Metrik“ (Teil 2) | 23 |
| 3 | relation_reading | candidate | „Rendering-Grenzen“ | Teil 1 & 2 | duration | asserts | Die „Rendering-Grenzen“ (Teil 1 & 2) | 30 |
| 4 | relation_reading | candidate | Kael spürt, dass die Aufmerksamkeit schwindet | Kapitel 39 | duration | asserts | In Kapitel 39 müssen wir beschreiben, wie Kael spürt, dass die Aufmerksamkeit schwindet. | 48 |
| 5 | relation_reading | candidate | Beobachter-Fokus | 85% | parameter | asserts | Beobachter-Fokus bei 85% | 58 |

## `2026-09-14-kap25-vertiefung-md`

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.2003, 88.0 s. **39 rows**: 30 candidates, 9 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | refused: surface absent from document | Kapiteldateien | 41 | count | asserts | Wortzahlen aller 41 Kapiteldateien erhoben. | 17 |
| 2 | relation_reading | refused: surface absent from document | Kap 25 | 1.137 Wörtern | count | asserts | Kap 25 war mit **1.137 Wörtern** das schwächste Kapitel des Manuskripts | 17 |
| 3 | relation_reading | refused: surface absent from document | Kap 30 | 1.141 | count | asserts | Kap 30 folgt mit 1.141 | 17 |
| 4 | relation_reading | candidate | Zukunftsverluste | zwei | count | cites | die Masterplan-Zeile 25 verlangt „zwei genuine Zukunftsverluste | 17 |
| 5 | relation_reading | refused: quote not placed | Wegkreuzung | 25 | identifier | asserts | Kapitel 25 „Wegkreuzung“ |  |
| 6 | relation_reading | candidate | abgeben/splitten | zwei bzw. vier Wochen | duration | asserts | abgeben/splitten sind seit zwei bzw. vier Wochen graue Felder ohne Ton | 22 |
| 7 | relation_reading | candidate | Vorgänge | zwei weitere | count | asserts | Die Einheit von Station 7 hängt die Priorität-1-Wasserführung und zwei weitere Vorgänge auf sich um | 22 |
| 8 | relation_reading | candidate | Station | 7 | identifier | asserts | Die Einheit von Station 7 hängt die Priorität-1-Wasserführung | 22 |
| 9 | relation_reading | candidate | EINHEIT | 734 | identifier | asserts | EINHEIT 734: BEARBEITUNGSPROFIL ABWEICHEND. | 22 |
| 10 | relation_reading | candidate | Abzweigung | Platte 204 | identifier | asserts | Abzweigung bei Platte 204 | 23 |
| 11 | relation_reading | candidate | Schild | elf | count | asserts | Schild mit elf vorgesehenen Kennungen | 23 |
| 12 | relation_reading | candidate | Stufen | drei | count | asserts | Kael geht drei Stufen hinunter | 23 |
| 13 | relation_reading | candidate | Anker | 734 | identifier | asserts | Anker 734 dritte Wiederkehr | 23 |
| 14 | relation_reading | candidate | Anker 734 | dritte Wiederkehr | duration | asserts | Anker 734 dritte Wiederkehr | 23 |
| 15 | relation_reading | refused: surface absent from document | Restzahl nach Schichtende | 34 | parameter | asserts | die Restzahl steht nach Schichtende bei 34 statt 31 | 25 |
| 16 | relation_reading | refused: surface absent from document | Restzahl morgen früh | sechs | parameter | denies | die Restzahl steht nach Schichtende bei 34 statt 31 und wird morgen früh nicht bei sechs stehen | 25 |
| 17 | relation_reading | candidate | Klick | sechsmal | count | asserts | der Klick wird als **Abwesenheit** hörbar (sechsmal | 25 |
| 18 | relation_reading | refused: surface absent from document | Zahl am Montag | achtundvierzig | parameter | cites | Am Montag steht die Zahl bei achtundvierzig | 25 |
| 19 | relation_reading | candidate | Platten | 204 | count | asserts | 204 Platten | 27 |
| 20 | relation_reading | candidate | Zeilen | 260 | count | asserts | 260 Zeilen | 27 |
| 21 | relation_reading | refused: ambiguous quote: choose its passage | Regel | 6 | identifier | asserts | Regel 6 | 27, 31, 47 |
| 22 | relation_reading | candidate | Station | 11/12/7 | identifier | asserts | Station 11/12/7 | 27 |
| 23 | relation_reading | candidate | bewusste Wahl | Kap 26 | duration | asserts | bewusste Wahl, Kap 26 | 38 |
| 24 | relation_reading | candidate | Mikrocues in der Handszene | drei | count | asserts | drei Mikrocues in der Handszene | 47 |
| 25 | relation_reading | candidate | Deutungssätze | zwei | count | asserts | zwei Deutungssätze entschärft | 47 |
| 26 | relation_reading | candidate | Genesis-Echo je Szene | max. ein | threshold | asserts | max. ein Genesis-Echo je Szene | 47 |
| 27 | relation_reading | candidate | Konzept je Szene | ein | parameter | asserts | ein Konzept je Szene | 47 |
| 28 | relation_reading | refused: surface absent from document | Inhaltserfassung | 02:10–02:14 | duration | asserts | die Inhaltserfassung lief 02:10–02:14 in einer Nacht | 47 |
| 29 | relation_reading | candidate | objektive Falschheit | eine | count | asserts | **eine** objektive Falschheit | 47 |
| 30 | relation_reading | candidate | Kapitel | 25 | identifier | denies | Kapitel 25 ist in keiner der beiden Dateien encodiert | 51 |
| 31 | relation_reading | candidate | Abende | vier | count | asserts | die vier Abende | 47 |
| 32 | relation_reading | candidate | Benennungslock | Kap 1–13 | parameter | asserts | Der Benennungslock gilt für Kap 1–13. | 55 |
| 33 | relation_reading | candidate | gedrafteten Kapitel | 14–26 | identifier | asserts | Die gedrafteten Kapitel 14–26 benennen die Instanz trotzdem nirgends | 55 |
| 34 | relation_reading | candidate | Template-Kopf | drei Szenen | count | asserts | Der Template-Kopf führt weiterhin drei Szenen | 58 |
| 35 | relation_reading | candidate | Prosa | sieben | count | asserts | die Prosa hat sieben | 58 |
| 36 | relation_reading | candidate | KW2 | 14–22 | duration | asserts | Der Canon weist 14–22 KW2 und 23–28 KW3 zu | 60 |
| 37 | relation_reading | candidate | KW3 | 23–28 | duration | asserts | Der Canon weist 14–22 KW2 und 23–28 KW3 zu | 60 |
| 38 | relation_reading | candidate | gedrafteten Kapitel | 14–26 | duration | asserts | die gedrafteten Kapitel 14–26 spielen durchgehend in der Verwaltungstopologie der Konstrukt-Stadt | 60 |
| 39 | relation_reading | candidate | Wohneinheit | 734 | identifier | asserts | Wohneinheit 734 | 60 |
