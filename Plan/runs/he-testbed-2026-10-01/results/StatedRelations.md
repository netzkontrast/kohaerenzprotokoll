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

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.2378, 106.6 s. **27 rows**: 19 candidates, 8 refused, 0 duplicates.

| # | kind | status | source | target | type | quote | lines |
|---|---|---|---|---|---|---|---|
| 1 | relation | candidate | Kap 25 | Manuskript | weakest_chapter_of | Kap 25 war mit **1.137 Wörtern** das schwächste Kapitel des Manuskripts (Kap 0 ausgenommen, eigene Rahmenpoetik; Kap 30 folgt mit 1.141). | 17 |
| 2 | relation | candidate | Akt-II-Arc | Schwellensequenz | requires | Akt-II-Arc verlangt für 24–26 eine getragene Schwellensequenz | 17 |
| 3 | relation | candidate | Canon §0 Schleier-Disziplin | Kap 25–26 | requires_for | Canon §0 Schleier-Disziplin verlangt genau das für Kap 25–26; die alte Fassung löste das nicht ein. | 21 |
| 4 | relation | candidate | Einheit von Station 7 | Priorität-1-Wasserführung | reroutes_to_itself | Die Einheit von Station 7 hängt die Priorität-1-Wasserführung und zwei weitere Vorgänge auf sich um — aus nachvollziehbarem **Eigennutz** (Restwertschwelle → Besuch der technischen Ebene), nicht aus Güte. | 22 |
| 5 | relation | refused: quote not placed | Apparat | Abweichung | registers | Zusätzlich registriert der Apparat die Abweichung, ohne zu handeln (**EINHEIT 734: BEARBEITUNGSPROFIL ABWEICHEND. KEINE MASSNAHME.**) — Canon §5 verlangt „AEGIS bemerkt Kaels neue Klarheit“; das fehlte. |  |
| 6 | relation | refused: quote not placed | Canon §5 | AEGIS bemerkt Kaels neue Klarheit | requires | Zusätzlich registriert der Apparat die Abweichung, ohne zu handeln (**EINHEIT 734: BEARBEITUNGSPROFIL ABWEICHEND. KEINE MASSNAHME.**) — Canon §5 verlangt „AEGIS bemerkt Kaels neue Klarheit“; das fehlte. |  |
| 7 | relation | candidate | Abzweigung | Platte 204 | located_at | Neue Szene am Ende des Gangs: Abzweigung bei Platte 204, Schild mit elf vorgesehenen Kennungen (seine fehlt), kühlere Luft aus dem Treppenschacht, fettig-metallischer Geruch, rauer Handlauf ohne Beschichtung, Scharren von unten, Licht, das an einer Kante aufhört. | 23 |
| 8 | relation | candidate | Schild | Kennungen | has | Neue Szene am Ende des Gangs: Abzweigung bei Platte 204, Schild mit elf vorgesehenen Kennungen (seine fehlt), kühlere Luft aus dem Treppenschacht, fettig-metallischer Geruch, rauer Handlauf ohne Beschichtung, Scharren von unten, Licht, das an einer Kante aufhört. | 23 |
| 9 | relation | candidate | Hook-out | Kap 26 | carries_into | neuer Hook-out: die Restzahl steht nach Schichtende bei 34 statt 31 und wird morgen früh nicht bei sechs stehen → trägt direkt in Kap 26 | 25 |
| 10 | relation | refused: quote not placed | Kap 25 | Die Niederlegung | has_title | Kap 25 = „Die Niederlegung“ |  |
| 11 | relation | candidate | Schleusen des Misstrauens | KW3 | part_of | KW3-Unterorte: Schleusen des Misstrauens, Gänge der Paranoia, Panoptikum | 39 |
| 12 | relation | candidate | Gänge der Paranoia | KW3 | part_of | KW3-Unterorte: Schleusen des Misstrauens, Gänge der Paranoia, Panoptikum | 39 |
| 13 | relation | candidate | Panoptikum | KW3 | part_of | KW3-Unterorte: Schleusen des Misstrauens, Gänge der Paranoia, Panoptikum | 39 |
| 14 | relation | candidate | Schutz-Anteil | ANP-Alltagssystem | opposes | Schutz-Anteil als Aktionssystem (Verteidigung) gegen ANP-Alltagssystem | 40 |
| 15 | relation | refused: joined or shortened quote | Weltkonkrete der Prosa | [K]-Repo-Canon | derived_from | alles Weltkonkrete der Prosa stammt aus \[K\]-Repo-Canon oder aus den bereits gedrafteten Nachbarkapiteln. | 43 |
| 16 | relation | refused: joined or shortened quote | Weltkonkrete der Prosa | Nachbarkapiteln | derived_from | alles Weltkonkrete der Prosa stammt aus \[K\]-Repo-Canon oder aus den bereits gedrafteten Nachbarkapiteln. | 43 |
| 17 | relation | refused: joined or shortened quote | Weltkonkrete der Prosa | \[K\]-Repo-Canon | derived_from | Kein Material aus \[S\]-Quellen wurde als Kanon behandelt; alles Weltkonkrete der Prosa stammt aus \[K\]-Repo-Canon oder aus den bereits gedrafteten Nachbarkapiteln. | 43 |
| 18 | relation | refused: joined or shortened quote | Weltkonkrete der Prosa | gedrafteten Nachbarkapiteln | derived_from | Kein Material aus \[S\]-Quellen wurde als Kanon behandelt; alles Weltkonkrete der Prosa stammt aus \[K\]-Repo-Canon oder aus den bereits gedrafteten Nachbarkapiteln. | 43 |
| 19 | relation | refused: joined or shortened quote | \[S\]-Quellen | Kanon | not_treated_as | Kein Material aus \[S\]-Quellen wurde als Kanon behandelt; alles Weltkonkrete der Prosa stammt aus \[K\]-Repo-Canon oder aus den bereits gedrafteten Nachbarkapiteln. | 43 |
| 20 | relation | candidate | Benennungslock | Kap 1–13 | applies_to | Der Benennungslock gilt für Kap 1–13. | 55 |
| 21 | relation | candidate | Kap 25 | Nachbarkapitel | follows_practice_of | Kap 25 folgt der Praxis der Nachbarkapitel (nur VERSALIEN-Direktiven). | 55 |
| 22 | relation | candidate | Kap 25 | Abwesenheit des Klicks | uses | Kap 25 verwendet die **Abwesenheit** des Klicks lokal (eine Station, ein Tag). | 57 |
| 23 | relation | candidate | Drafting-Brief | Kopf | prohibits_changes_to | Der Drafting-Brief verbietet Änderungen am Kopf außer status. | 58 |
| 24 | relation | candidate | Canon | KW2 | assigns_to | Der Canon weist 14–22 KW2 und 23–28 KW3 zu; die gedrafteten Kapitel 14–26 spielen durchgehend in der Verwaltungstopologie der Konstrukt-Stadt (Datenknoten, Delta-Sieben, Wohneinheit 734). | 60 |
| 25 | relation | candidate | Canon | KW3 | assigns_to | Der Canon weist 14–22 KW2 und 23–28 KW3 zu; die gedrafteten Kapitel 14–26 spielen durchgehend in der Verwaltungstopologie der Konstrukt-Stadt (Datenknoten, Delta-Sieben, Wohneinheit 734). | 60 |
| 26 | relation | candidate | Kapitel 14–26 | Verwaltungstopologie der Konstrukt-Stadt | set_in | Der Canon weist 14–22 KW2 und 23–28 KW3 zu; die gedrafteten Kapitel 14–26 spielen durchgehend in der Verwaltungstopologie der Konstrukt-Stadt (Datenknoten, Delta-Sieben, Wohneinheit 734). | 60 |
| 27 | relation | candidate | Kap 25 | KW3 | realizes | Kap 25 löst KW3 jetzt **sensorisch** ein (Treppenkopf, Wartungsebene), ohne den Ort zu wechseln. | 60 |
