# ChapterBeats — the testbed's results

> ChapterBeats — what a document says happens in a numbered chapter, with the participants, each with that sentence.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: decision 013: the chapter is a unit beside the term, and 98 chapter mentions in read documents still have no reading on their
> chapter's page; 218 plot-outline documents are unread. The mechanical NAMES_CHAPTER relation says a line names a chapter,
> not what happens there or who takes part.
> measured against: the readings on the chapter pages (`Wiki/chapters/kap-NN.md`); a beat whose chapter is a page of the wiki is the attachable subset. A quote is placed by read.py --find (P26).
> may not: write a chapter reading, decide what a chapter is about, or reconcile two plans' chapters — a beat is a P_HE_BEAT candidate for a reader
> retire when: on three plot-outline documents a person keeps no beat beyond what the chapter pages already quote

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/chapterbeats-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0498, 17.2 s. **1 rows**: 1 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Kapitel 39 | Kael spürt, dass die Aufmerksamkeit schwindet | event | hedges | In Kapitel 39 müssen wir beschreiben, wie Kael spürt, dass die Aufmerksamkeit schwindet. | 48 |

## `2026-09-14-kap25-vertiefung-md`

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.1928, 84.1 s. **23 rows**: 21 candidates, 2 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Kap 25 | das schwächste Kapitel des Manuskripts | event | asserts | Kap 25 war mit **1.137 Wörtern** das schwächste Kapitel des Manuskripts | 17 |
| 2 | relation_reading | candidate | 24–26 | eine getragene Schwellensequenz | event | asserts | Akt-II-Arc verlangt für 24–26 eine getragene Schwellensequenz | 17 |
| 3 | relation_reading | candidate | Kap 25–26 | Schleier-Disziplin | event | cites | Canon §0 Schleier-Disziplin verlangt genau das für Kap 25–26 | 21 |
| 4 | relation_reading | candidate | Kap 26 | Vorbeigehen an der Tür | event | asserts | ihr Vorbeigehen an der Tür in Kap 26 ist vorbereitet | 22 |
| 5 | relation_reading | candidate | Kap 25 | Canon-Weltanker | resolves | asserts | Das löst den Canon-Weltanker für Kap 25 ein | 23 |
| 6 | relation_reading | refused: quote not placed | Kap 26 | der Tritt darüber | involves | asserts | der Tritt darüber“ (Kap 26) |  |
| 7 | relation_reading | candidate | Kap 24 | die einrastende Verkleidung | event | asserts | Hook-in aus Kap 24 explizit (die einrastende Verkleidung) | 25 |
| 8 | relation_reading | candidate | Kap 26 | die Restzahl steht nach Schichtende bei 34 statt 31 | event | asserts | neuer Hook-out: die Restzahl steht nach Schichtende bei 34 statt 31 und wird morgen früh nicht bei sechs stehen → trägt direkt in Kap 26 | 25 |
| 9 | relation_reading | candidate | Kap 25 | Schwelle, nicht Konfrontation | event | cites | Kap 25: Schwelle, nicht Konfrontation | 31 |
| 10 | relation_reading | candidate | Kap 26 | bewusste Wahl | event | asserts | bewusste Wahl, Kap 26 | 38 |
| 11 | relation_reading | candidate | 25–26 | Vielheit wird benannt | event | asserts | Vielheit wird benannt, **kanonisch gefordert** für 25–26 | 47 |
| 12 | relation_reading | candidate | Kap 1–13 | Benennungslock | event | asserts | Der Benennungslock gilt für Kap 1–13. | 55 |
| 13 | relation_reading | candidate | Kapitel 14–26 | die Instanz | event | denies | Die gedrafteten Kapitel 14–26 benennen die Instanz trotzdem nirgends leserseitig | 55 |
| 14 | relation_reading | candidate | Kap 25 | VERSALIEN-Direktiven | event | asserts | Kap 25 folgt der Praxis der Nachbarkapitel (nur VERSALIEN-Direktiven). | 55 |
| 15 | relation_reading | refused: quote not placed | 25–26 | offen benannt | event | cites | Canon verlangt „offen benannt“ in 25–26. |  |
| 16 | relation_reading | candidate | Kap 26 | Verlagerung | event | hedges | oder die Verlagerung nach Kap 26 | 56 |
| 17 | relation_reading | candidate | Kap 25 | Abwesenheit | event | asserts | Kap 25 verwendet die **Abwesenheit** des Klicks lokal | 57 |
| 18 | relation_reading | candidate | Kap 27/28 | sie | involves | asks | Trägt sie in Akt III weiter (Kap 27/28) | 59 |
| 19 | relation_reading | candidate | Kapitel 14–26 | Verwaltungstopologie der Konstrukt-Stadt | involves | asserts | die gedrafteten Kapitel 14–26 spielen durchgehend in der Verwaltungstopologie der Konstrukt-Stadt | 60 |
| 20 | relation_reading | candidate | Kap 25 | KW3 | event | asserts | Kap 25 löst KW3 jetzt | 60 |
| 21 | relation_reading | candidate | 14–22 | KW2 | involves | cites | Der Canon weist 14–22 KW2 | 60 |
| 22 | relation_reading | candidate | 23–28 | KW3 | involves | cites | 23–28 KW3 zu | 60 |
| 23 | relation_reading | candidate | 14–26 | KW2/KW3 | turns | asks | sollen 14–26 in einem eigenen Pass stärker nach KW2/KW3 verschoben werden | 60 |
