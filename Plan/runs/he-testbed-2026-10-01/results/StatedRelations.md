# StatedRelations — the testbed's results

> StatedRelations — relations one document states in a sentence, each with that sentence.
> provisional — first design, 2026-09-24; never run on the corpus
> derived from: no gold. The wiki's [[links]] mark terms a page names and are untyped, so
> nothing here measures a typed relation. This is a trial that lets the graph tools
> (knowledge-graph-extract, grawiki, graphify) be compared on equal terms.
> may not: become a [[link]] — a link is never inferred (CLAUDE.md) — detect a conflict,
> or supply a count. A relation whose quote read.py --find cannot place is dropped by code.
> retire when: on documents 5 and 6 a person keeps none of its relations as a candidate edge

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/statedrelations-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.084, 34.9 s. **16 rows**: 16 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | quote | lines |
|---|---|---|---|---|---|---|---|
| 1 | relation | candidate | Kael | Große Stille | names | Kael nennt dies die „Große Stille“. | 20 |
| 2 | relation | candidate | AEGIS | Signal | waits_for | AEGIS agiert nicht als autonomer Gott, sondern als Verwalter, der auf ein „Signal“ wartet. | 25 |
| 3 | relation | candidate | AEGIS | Primären Beobachtungs-Einheit | speaks_of | AEGIS spricht in seinen Statusberichten oft von der „Primären Beobachtungs-Einheit“ oder dem „Externen Taktgeber“. | 27 |
| 4 | relation | candidate | AEGIS | Externen Taktgeber | speaks_of | AEGIS spricht in seinen Statusberichten oft von der „Primären Beobachtungs-Einheit“ oder dem „Externen Taktgeber“. | 27 |
| 5 | relation | candidate | AEGIS | Kohärenz Protokoll | justifies | Er rechtfertigt seine harten Maßnahmen (das Kohärenz Protokoll) damit, dass die „Einheit“ sonst das Interesse verlieren und das System abschalten könnte. | 27 |
| 6 | relation | candidate | AEGIS | Zuklappen des Buches | fears | AEGIS hat Angst vor dem Zuklappen des Buches. | 28 |
| 7 | relation | candidate | Ordnungssucht | Leser | tries_to_retain | Seine Ordnungssucht ist ein verzweifelter Versuch, den Leser (den Beobachter) bei der Stange zu halten, damit das System weiter mit „Aufmerksamkeit“ (Energie) versorgt wird. | 28 |
| 8 | relation | candidate | Kael | Leser | manifestation_of | Um den finalen Twist vorzubereiten – dass Kael die Manifestation des Lesers ist und seine Welt mit dem Zuklappen des Buches stirbt –, müssen wir subtile „Glitch-Momente“ und systemische Hinweise einbauen. | 13 |
| 9 | relation | candidate | Juna | Kael | whispers_truth_to | Juna ist diejenige, die Kael die Wahrheit flüstert. | 39 |
| 10 | relation | candidate | Kael | Leser | probe_of | Sie macht ihm klar: Kael ist die Sonde, die der Leser in das Trauma geschickt hat. | 42 |
| 11 | relation | candidate | Kael | Leser | tool_of | Er ist das Werkzeug, mit dem der Leser versucht, seine eigene Dissoziation (seine Trennung von der Welt) zu heilen. | 42 |
| 12 | relation | candidate | Zuklappen des Buches | Wärmetod des Universums | framed_as | Das Zuklappen des Buches wird als der „Wärmetod des Universums“ (Entropie) geframt. | 46 |
| 13 | relation | candidate | Welt | Leser | depends_on | Die Welt existiert nur so weit, wie der Leser sie sich vorstellen kann. | 35 |
| 14 | relation | candidate | System | Verstand des Beobachters | caused_by | Wenn das System unentscheidbar wird, liegt das daran, dass der Verstand des Beobachters (des Lesers) an seine eigenen kognitiven Grenzen stößt. | 35 |
| 15 | relation | candidate | AEGIS-Protokolle | Beobachtungsstatus | queries | Nutze Kursivschrift für AEGIS-Protokolle, die den „Beobachtungsstatus“ abfragen. | 54 |
| 16 | relation | candidate | Kael | Welt | causes_disintegration_of | Wenn Kael zu schnell rennt oder in Regionen vordringt, die noch nicht „beschrieben“ wurden, zerfällt die Welt in Textfragmente oder unklare Schemen. | 34 |

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
