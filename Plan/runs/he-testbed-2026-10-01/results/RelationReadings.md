# RelationReadings — the testbed's results

> provisional — source-specific relation readings, 2026-09-30; synthetic tests only
> derived from: StatedRelations and TermReadings; the former drops hedges and questions
> may not: resolve conflicts, write wiki links, merge sources, or establish a verified fact
> retire when: two reviewed pilots find no useful proposals beyond TermReadings

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/relationreadings-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0684, 27.5 s. **32 rows**: 31 candidates, 1 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Kael | der Leser | is_manifestation_of | asserts | dass Kael die Manifestation des Lesers ist | 13 |
| 2 | relation_reading | candidate | Kael | seine Welt | world_dies_when_book_closes | asserts | seine Welt mit dem Zuklappen des Buches stirbt | 13 |
| 3 | relation_reading | candidate | Kael | Zeit im Konstrukt | perceives_as_clocked_not_linear | hedges | Kael sollte früh bemerken, dass die Zeit im Konstrukt nicht linear fließt, sondern „getaktet“ ist. | 17 |
| 4 | relation_reading | candidate | Kael | Welt um ihn herum | experiences_freezing_of | asserts | Kael erlebt Momente, in denen die Welt um ihn herum für eine unbestimmte Dauer einfriert. | 19 |
| 5 | relation_reading | candidate | Stasis-Lücken | der Leser | occurs_when_interrupted | asserts | Das passiert immer dann, wenn der Leser im realen Leben unterbrochen wird (das Buch weglegt). | 20 |
| 6 | relation_reading | candidate | Kael | Große Stille | names | asserts | Kael nennt dies die „Große Stille“. | 20 |
| 7 | relation_reading | candidate | AEGIS | autonomer Gott | does_not_act_as | denies | AEGIS agiert nicht als autonomer Gott, sondern als Verwalter, der auf ein „Signal“ wartet. | 25 |
| 8 | relation_reading | candidate | AEGIS | Signal | waits_for | asserts | sondern als Verwalter, der auf ein „Signal“ wartet. | 25 |
| 9 | relation_reading | candidate | AEGIS | Primären Beobachtungs-Einheit | mentions_in_status_reports | asserts | AEGIS spricht in seinen Statusberichten oft von der „Primären Beobachtungs-Einheit“ oder dem „Externen Taktgeber“. | 27 |
| 10 | relation_reading | candidate | AEGIS | Kohärenz Protokoll | justifies_with_possible_loss_of_interest | asserts | Er rechtfertigt seine harten Maßnahmen (das Kohärenz Protokoll) damit, dass die „Einheit“ sonst das Interesse verlieren und das System abschalten könnte. | 27 |
| 11 | relation_reading | candidate | Einheit | System | might_shut_down | hedges | dass die „Einheit“ sonst das Interesse verlieren und das System abschalten könnte. | 27 |
| 12 | relation_reading | candidate | AEGIS | Zuklappen des Buches | fears | asserts | AEGIS hat Angst vor dem Zuklappen des Buches. | 28 |
| 13 | relation_reading | candidate | AEGIS | der Leser | tries_to_keep_attention_of | asserts | Seine Ordnungssucht ist ein verzweifelter Versuch, den Leser (den Beobachter) bei der Stange zu halten | 28 |
| 14 | relation_reading | candidate | Aufmerksamkeit | System | supplies_energy_to | asserts | damit das System weiter mit „Aufmerksamkeit“ (Energie) versorgt wird. | 28 |
| 15 | relation_reading | candidate | Grenzen der Mathematik und Physik | der Leser | are_technical_limits_of | asserts | Integriere Hinweise auf die Grenzen der Mathematik und Physik als technische Limits des Lesers. | 32 |
| 16 | relation_reading | candidate | Kael | Welt | causes_disintegration_of | asserts | Wenn Kael zu schnell rennt oder in Regionen vordringt, die noch nicht „beschrieben“ wurden, zerfällt die Welt in Textfragmente oder unklare Schemen. | 34 |
| 17 | relation_reading | candidate | Welt | Leser | exists_only_as_far_as_imagined_by | asserts | Die Welt existiert nur so weit, wie der Leser sie sich vorstellen kann. | 35 |
| 18 | relation_reading | candidate | System | Verstand des Beobachters (des Lesers) | undecidability_caused_by_cognitive_limits_of | asserts | Wenn das System unentscheidbar wird, liegt das daran, dass der Verstand des Beobachters (des Lesers) an seine eigenen kognitiven Grenzen stößt. | 35 |
| 19 | relation_reading | candidate | Juna | Kael | whispers_truth_to | asserts | Juna ist diejenige, die Kael die Wahrheit flüstert. | 39 |
| 20 | relation_reading | candidate | Kael | Herz | heart_beats_by_itself | asks | Glaubst du wirklich, dein Herz schlägt von selbst? | 41 |
| 21 | relation_reading | candidate | Herz | Leser | beats_only_because_read_by | asks | Oder schlägt es nur, weil da draußen jemand die Zeilen liest, die uns definieren? | 41 |
| 22 | relation_reading | candidate | Leser | Kael | sent_as_probe_into_trauma | asserts | Kael ist die Sonde, die der Leser in das Trauma geschickt hat. | 42 |
| 23 | relation_reading | candidate | Leser | Kael | uses_as_tool_to_heal_dissociation | asserts | Er ist das Werkzeug, mit dem der Leser versucht, seine eigene Dissoziation | 42 |
| 24 | relation_reading | candidate | Zuklappen des Buches | Wärmetod des Universums | is_framed_as | asserts | Das Zuklappen des Buches wird als der „Wärmetod des Universums“ (Entropie) geframt. | 46 |
| 25 | relation_reading | candidate | Kael | Aufmerksamkeit | senses_fading_of | asserts | wie Kael spürt, dass die Aufmerksamkeit schwindet | 48 |
| 26 | relation_reading | refused: surface absent from document | Kael | letzter Punkt | will_stop_breathing_when_set | asserts | Wenn der letzte Punkt gesetzt ist, wird er aufhören zu atmen. | 48 |
| 27 | relation_reading | candidate | Kael | Leser | does_not_ask_to_continue_reading | denies | Kael bittet den Leser nicht darum, weiterzulesen | 49 |
| 28 | relation_reading | candidate | Kael | Gedanke eines Fremden | accepts_fate_as | asserts | sondern akzeptiert sein Schicksal als „Gedanke eines Fremden“. | 49 |
| 29 | relation_reading | candidate | Du | Leser | is_not_direct_address_to | denies | Nicht als direkte Ansprache des Lesers, sondern als interne Stimme Kaels | 53 |
| 30 | relation_reading | candidate | Du | Kael | is_internal_voice_of | asserts | sondern als interne Stimme Kaels, die sich fragt: | 53 |
| 31 | relation_reading | candidate | AEGIS-Protokolle | Beobachtungsstatus | query | asserts | Nutze Kursivschrift für AEGIS-Protokolle, die den „Beobachtungsstatus“ abfragen. | 54 |
| 32 | relation_reading | candidate | narrative Spannung | System-Abschaltung | raised_to_prevent | asserts | Erhöhe narrative Spannung, um System-Abschaltung zu verhindern. | 58 |

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
