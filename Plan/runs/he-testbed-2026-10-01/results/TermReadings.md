# TermReadings — the testbed's results

> TermReadings — the passages where one document says something about a term.
> provisional — first design, 2026-09-24; never run on the corpus
> derived from: the notes (Sources/notes/<slug>.md), which quote each reading with its line
> measured against: the lines the note for the same document cites. A quote is placed by
> read.py --find (P26), never by the model; a quote it refuses is reported, not repaired.
> may not: write a note, a reading or a page; merge readings — it is a list and never merges
> (P13); or settle a stance for the record — stance is read per passage by a person
> (decision 004), so the model's label only orders what a person reads first
> retire when: for two documents its quotes land on none of the note's cited lines

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/termreadings-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0824, 35.3 s. **23 rows**: 22 candidates, 0 refused, 1 duplicates.

Beside the Haiku pilot of 2026-09-30 on this document: the candidates stand on 17 lines here and 4 there, 3 of them the same.

| # | kind | status | term | stance | quote | lines |
|---|---|---|---|---|---|---|
| 1 | reading | candidate | Stasis-Lücken | asserts | Kael erlebt Momente, in denen die Welt um ihn herum für eine unbestimmte Dauer einfriert. | 19 |
| 2 | reading | candidate | Stasis-Lücken | asserts | Das passiert immer dann, wenn der Leser im realen Leben unterbrochen wird (das Buch weglegt). | 20 |
| 3 | reading | candidate | Große Stille | asserts | Kael nennt dies die „Große Stille“. | 20 |
| 4 | reading | candidate | Zeit im Konstrukt | asserts | Kael sollte früh bemerken, dass die Zeit im Konstrukt nicht linear fließt, sondern „getaktet“ ist. | 17 |
| 5 | reading | candidate | Kael | asserts | dass Kael die Manifestation des Lesers ist und seine Welt mit dem Zuklappen des Buches stirbt | 13 |
| 6 | reading | candidate | AEGIS | asserts | AEGIS agiert nicht als autonomer Gott, sondern als Verwalter, der auf ein „Signal“ wartet. | 25 |
| 7 | reading | candidate | AEGIS | asserts | AEGIS hat Angst vor dem Zuklappen des Buches. | 28 |
| 8 | reading | candidate | Ordnungssucht | asserts | Seine Ordnungssucht ist ein verzweifelter Versuch, den Leser (den Beobachter) bei der Stange zu halten, damit das System weiter mit „Aufmerksamkeit“ (Energie) versorgt wird. | 28 |
| 9 | reading | candidate | Kohärenz Protokoll | hedges | Er rechtfertigt seine harten Maßnahmen (das Kohärenz Protokoll) damit, dass die „Einheit“ sonst das Interesse verlieren und das System abschalten könnte. | 27 |
| 10 | reading | candidate | Rendering-Grenzen | asserts | Integriere Hinweise auf die Grenzen der Mathematik und Physik als technische Limits des Lesers. | 32 |
| 11 | reading | duplicate | Rendering-Grenzen | asserts | Integriere Hinweise auf die Grenzen der Mathematik und Physik als technische Limits des Lesers. | 32 |
| 12 | reading | candidate | Foreshadowing | asserts | Wenn Kael zu schnell rennt oder in Regionen vordringt, die noch nicht „beschrieben“ wurden, zerfällt die Welt in Textfragmente oder unklare Schemen. | 34 |
| 13 | reading | candidate | unentscheidbar | asserts | Wenn das System unentscheidbar wird, liegt das daran, dass der Verstand des Beobachters (des Lesers) an seine eigenen kognitiven Grenzen stößt. | 35 |
| 14 | reading | candidate | Welt | asserts | Die Welt existiert nur so weit, wie der Leser sie sich vorstellen kann. | 35 |
| 15 | reading | candidate | Juna | asserts | Juna ist diejenige, die Kael die Wahrheit flüstert. | 39 |
| 16 | reading | candidate | Herz | asks | Glaubst du wirklich, dein Herz schlägt von selbst? Oder schlägt es nur, weil da draußen jemand die Zeilen liest, die uns definieren? | 41 |
| 17 | reading | candidate | Kael | asserts | Kael ist die Sonde, die der Leser in das Trauma geschickt hat. | 42 |
| 18 | reading | candidate | Kael | asserts | Er ist das Werkzeug, mit dem der Leser versucht, seine eigene Dissoziation (seine Trennung von der Welt) zu heilen. | 42 |
| 19 | reading | candidate | Dissoziation | asserts | seine eigene Dissoziation (seine Trennung von der Welt) | 42 |
| 20 | reading | candidate | Zuklappen des Buches | asserts | Das Zuklappen des Buches wird als der „Wärmetod des Universums“ (Entropie) geframt. | 46 |
| 21 | reading | candidate | Kael | asserts | Kael bittet den Leser nicht darum, weiterzulesen, sondern akzeptiert sein Schicksal als „Gedanke eines Fremden“. | 49 |
| 22 | reading | candidate | Du | asserts | Nicht als direkte Ansprache des Lesers, sondern als interne Stimme Kaels, die sich fragt: | 53 |
| 23 | reading | candidate | AEGIS-Protokolle | asserts | Nutze Kursivschrift für AEGIS-Protokolle, die den „Beobachtungsstatus“ abfragen. | 54 |

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
