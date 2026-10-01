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

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.3002, 145.8 s. **97 rows**: 85 candidates, 12 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Kap 25 | Manuskript | is_weakest_chapter_of | asserts | das schwächste Kapitel des Manuskripts | 17 |
| 2 | relation_reading | candidate | Kap 0 | Manuskript | excluded_from_weakest_chapter_comparison | asserts | Kap 0 ausgenommen, eigene Rahmenpoetik | 17 |
| 3 | relation_reading | candidate | Kap 30 | Kap 25 | follows_in_weakness | asserts | Kap 30 folgt mit 1.141 | 17 |
| 4 | relation_reading | candidate | git branch -r | claude/kap-\*-Branch | shows_no_open | denies | git branch -r zeigt keinen offenen claude/kap-\*-Branch | 17 |
| 5 | relation_reading | candidate | Akt-II-Arc | getragene Schwellensequenz | requires | asserts | Akt-II-Arc verlangt für 24–26 eine getragene Schwellensequenz | 17 |
| 6 | relation_reading | candidate | Masterplan-Zeile 25 | zwei genuine Zukunftsverluste | requires | asserts | zwei genuine Zukunftsverluste | 17 |
| 7 | relation_reading | candidate | Masterplan-Zeile 25 | physische Verzweigung | requires | asserts | physische Verzweigung | 17 |
| 8 | relation_reading | candidate | Masterplan-Zeile 25 | Körperbogen | requires | asserts | einen Körperbogen | 17 |
| 9 | relation_reading | candidate | die Hand | das Bestätigungsfeld | moves_toward | asserts | bewegt sich um 10:58 die Hand von selbst auf das Bestätigungsfeld | 21 |
| 10 | relation_reading | candidate | einer zweiten Spannung im selben Unterarm | die Hand | stops | asserts | wird von einer zweiten Spannung im selben Unterarm gestoppt | 21 |
| 11 | relation_reading | candidate | die Nicht-Handlung | Entscheidung | is_readable_as | asserts | Damit ist die Nicht-Handlung als **Entscheidung** lesbar statt als Freeze | 21 |
| 12 | relation_reading | candidate | die Nicht-Handlung | Freeze | is_not_readable_as | denies | Damit ist die Nicht-Handlung als **Entscheidung** lesbar statt als Freeze | 21 |
| 13 | relation_reading | candidate | Canon §0 Schleier-Disziplin | Kap 25–26 | requires_veil_lifting_for | asserts | Canon §0 Schleier-Disziplin verlangt genau das für Kap 25–26 | 21 |
| 14 | relation_reading | candidate | die alte Fassung | Canon §0 Schleier-Disziplin | does_not_fulfil | denies | die alte Fassung löste das nicht ein | 21 |
| 15 | relation_reading | candidate | Die Einheit von Station 7 | die Priorität-1-Wasserführung | takes_over | asserts | Die Einheit von Station 7 hängt die Priorität-1-Wasserführung und zwei weitere Vorgänge auf sich um | 22 |
| 16 | relation_reading | candidate | Die Einheit von Station 7 | Eigennutz | is_motivated_by | asserts | aus nachvollziehbarem **Eigennutz** (Restwertschwelle → Besuch der technischen Ebene), nicht aus Güte | 22 |
| 17 | relation_reading | candidate | Die Einheit von Station 7 | Güte | is_not_motivated_by | denies | aus nachvollziehbarem **Eigennutz** (Restwertschwelle → Besuch der technischen Ebene), nicht aus Güte | 22 |
| 18 | relation_reading | candidate | Restwertschwelle | Besuch der technischen Ebene | leads_to | asserts | Restwertschwelle → Besuch der technischen Ebene | 22 |
| 19 | relation_reading | candidate | Kaels Verweigerung | einem Dritten | imposes_price_on | asserts | Kaels Verweigerung hat einen bezifferten Preis bei einem Dritten | 22 |
| 20 | relation_reading | candidate | der Apparat | die Abweichung | registers | asserts | registriert der Apparat die Abweichung, ohne zu handeln | 22 |
| 21 | relation_reading | candidate | der Apparat | die Abweichung | does_not_act_on | denies | registriert der Apparat die Abweichung, ohne zu handeln | 22 |
| 22 | relation_reading | candidate | Canon §5 | AEGIS bemerkt Kaels neue Klarheit | requires | asserts | Canon §5 verlangt „AEGIS bemerkt Kaels neue Klarheit | 22 |
| 23 | relation_reading | candidate | Abzweigung | Platte 204 | located_at | asserts | Abzweigung bei Platte 204 | 23 |
| 24 | relation_reading | candidate | Schild | elf vorgesehenen Kennungen | displays | asserts | Schild mit elf vorgesehenen Kennungen | 23 |
| 25 | relation_reading | candidate | kühlere Luft | Treppenschacht | comes_from | asserts | kühlere Luft aus dem Treppenschacht | 23 |
| 26 | relation_reading | candidate | Kael | drei Stufen | walks_down | asserts | Kael geht drei Stufen hinunter | 23 |
| 27 | relation_reading | candidate | Kael | Delta-Sieben | does_not_check_beneath | denies | sieht **nicht** in der allgemeinen Ebene nach, was unter Delta-Sieben liegt | 23 |
| 28 | relation_reading | candidate | Das | Canon-Weltanker | fulfills | asserts | Das löst den Canon-Weltanker für Kap 25 ein | 23 |
| 29 | relation_reading | candidate | Stehen an der Schwelle | der Tritt darüber | is_distinguished_from | asserts | (Kap 26) trennscharf | 23 |
| 30 | relation_reading | candidate | Das | Masterplan-Zeile | realizes | asserts | realisiert die Masterplan-Zeile | 23 |
| 31 | relation_reading | candidate | Hook-in | Kap 24 | originates_from | asserts | Hook-in aus Kap 24 explizit | 25 |
| 32 | relation_reading | candidate | der Klick | Abwesenheit | becomes_audible_as | asserts | der Klick wird als **Abwesenheit** hörbar | 25 |
| 33 | relation_reading | refused: surface absent from document | die Restzahl | 34 | stands_at_after_shift_end | asserts | die Restzahl steht nach Schichtende bei 34 statt 31 | 25 |
| 34 | relation_reading | candidate | die Restzahl | sechs | will_not_stand_at | denies | wird morgen früh nicht bei sechs stehen | 25 |
| 35 | relation_reading | candidate | neuer Hook-out | Kap 26 | carries_directly_into | asserts | trägt direkt in Kap 26 | 25 |
| 36 | relation_reading | candidate | Kap 25 | Schwelle | is | cites | Kap 25: Schwelle, nicht Konfrontation | 31 |
| 37 | relation_reading | candidate | Kap 25 | Konfrontation | is_not | denies | Kap 25: Schwelle, nicht Konfrontation | 31 |
| 38 | relation_reading | candidate | Wegkreuzung/Tore | interner Ort der Entscheidungsfindung | symbol_shifts_from_external_threshold_to_internal_place | asserts | von extern auferlegter Schwelle → interner Ort der Entscheidungsfindung | 38 |
| 39 | relation_reading | refused: quote not placed | Tiefenanalyse von „The Agency System“ | Wegkreuzung | is_motif_origin_of | asserts | Motivherkunft „Wegkreuzung“ = \*\*interner Wahlpunkt\*\* |  |
| 40 | relation_reading | refused: quote not placed | Wegkreuzung | Schritt ins Ungewisse | is_distinguished_from | asserts | Abgrenzung zu „Schritt ins Ungewisse“ (= bewusste Wahl, Kap 26) |  |
| 41 | relation_reading | refused: surface absent from document | Tiefenanalyse von „The Agency System“ | Kapitels | carries_axis_of | asserts | trägt die Achse des Kapitels | 38 |
| 42 | relation_reading | candidate | KW3-Unterorte | Kontrollpunkt-/Überwachungslogik | serves_as_background_for | asserts | als Hintergrund für Kontrollpunkt-/Überwachungslogik | 39 |
| 43 | relation_reading | refused: surface absent from document | dekanonisierte Guardians (Cerberus, Nox, Echo, Limina) | Orte-Konzept für „Kohärenz Protokoll“ | not_adopted_from | denies | dekanonisierte Guardians (Cerberus, Nox, Echo, Limina) \*\*nicht\*\* übernommen | 39 |
| 44 | relation_reading | candidate | Schutz-Anteil | ANP-Alltagssystem | acts_as_defense_system_against | asserts | Schutz-Anteil als Aktionssystem (Verteidigung) gegen ANP-Alltagssystem | 40 |
| 45 | relation_reading | refused: quote not placed | inneres Tauziehen | Unterarm | is_body_image_for_opposing_tension_in | asserts | „inneres Tauziehen“ als Körperbild für die gegenläufige Spannung im Unterarm |  |
| 46 | relation_reading | candidate | Co₁/McL/B/Ly-Taxonomie | aktuelle KW-Kanon | is_not | denies | Co₁/McL/B/Ly-Taxonomie ist nicht der aktuelle KW-Kanon | 41 |
| 47 | relation_reading | refused: joined or shortened quote | Material aus \[S\]-Quellen | Kanon | was_not_treated_as | denies | Kein Material aus \[S\]-Quellen wurde als Kanon behandelt | 43 |
| 48 | relation_reading | refused: joined or shortened quote | alles Weltkonkrete der Prosa | \[K\]-Repo-Canon | derives_from | asserts | alles Weltkonkrete der Prosa stammt aus \[K\]-Repo-Canon | 43 |
| 49 | relation_reading | candidate | alles Weltkonkrete der Prosa | bereits gedrafteten Nachbarkapiteln | derives_from | asserts | oder aus den bereits gedrafteten Nachbarkapiteln | 43 |
| 50 | relation_reading | candidate | R-2 | Deutungssätze | defused | asserts | zwei Deutungssätze entschärft | 47 |
| 51 | relation_reading | candidate | Vielheit | 25–26 | required_by_canon_for | asserts | Vielheit wird benannt, **kanonisch gefordert** für 25–26 | 47 |
| 52 | relation_reading | candidate | drei Mikrocues | Handszene | appear_in | asserts | drei Mikrocues in der Handszene | 47 |
| 53 | relation_reading | candidate | kaltes Ozon | Abmeldeszene | appears_only_in | asserts | kaltes Ozon **nur** in der Abmeldeszene | 47 |
| 54 | relation_reading | candidate | Wärme | Abmeldeszene | does_not_appear_in | denies | Wärme dort nicht | 47 |
| 55 | relation_reading | candidate | Wärmespur | ozonfreien Szene | appears_only_as_backreference_in | asserts | Wärmespur nur als Rückverweis | 47 |
| 56 | relation_reading | candidate | Juna | Subjekt | is_never | denies | Juna nie Subjekt, nie Name, nie Körper, nie Stimme | 47 |
| 57 | relation_reading | candidate | Juna | Name | is_never | denies | Juna nie Subjekt, nie Name, nie Körper, nie Stimme | 47 |
| 58 | relation_reading | candidate | Juna | Körper | is_never | denies | Juna nie Subjekt, nie Name, nie Körper, nie Stimme | 47 |
| 59 | relation_reading | candidate | Juna | Stimme | is_never | denies | Juna nie Subjekt, nie Name, nie Körper, nie Stimme | 47 |
| 60 | relation_reading | refused: surface absent from document | Inhaltserfassung | 02:10–02:14 | ran_during | asserts | die Inhaltserfassung lief 02:10–02:14 | 47 |
| 61 | relation_reading | candidate | Kael | Nacht | was_awake_and_counting_during | asserts | Kael nachweislich wach war und zählte | 47 |
| 62 | relation_reading | refused: surface absent from document | Restzahl-Anstieg | zweite Falschheit | kept_explainable_to_avoid | asserts | der Restzahl-Anstieg ist bewusst **erklärbar** gehalten | 47 |
| 63 | relation_reading | candidate | Telefon-Stille-Anker | gebrochen | was_not_broken | denies | Telefon-Stille-Anker getragen, nicht gebrochen | 47 |
| 64 | relation_reading | candidate | Kaels Signatur | Wechsel | breaks_only_where_intended | asserts | Kaels Signatur bricht nur dort, wo ein Wechsel gemeint ist | 47 |
| 65 | relation_reading | candidate | ncp.json | players, scenes, storybeats, moments | has_empty | asserts | ncp.json und ncp-b.json: players, scenes, storybeats, moments sind leer | 51 |
| 66 | relation_reading | candidate | ncp-b.json | players, scenes, storybeats, moments | has_empty | asserts | ncp.json und ncp-b.json: players, scenes, storybeats, moments sind leer | 51 |
| 67 | relation_reading | candidate | Prosavertiefung | Storyform-Slots | does_not_touch | denies | die Storyform-Slots sind von einer Prosavertiefung nicht berührt | 51 |
| 68 | relation_reading | candidate | Kapitel 25 | ncp.json | is_not_encoded_in | denies | Kapitel 25 ist in keiner der beiden Dateien encodiert | 51 |
| 69 | relation_reading | candidate | Kapitel 25 | ncp-b.json | is_not_encoded_in | denies | Kapitel 25 ist in keiner der beiden Dateien encodiert | 51 |
| 70 | relation_reading | candidate | agency-Capability-Verben | Lauf | were_not_available_in | denies | Die agency-Capability-Verben standen in diesem Lauf nicht zur Verfügung | 51 |
| 71 | relation_reading | candidate | Provenienz | .agency/session.db | was_not_written_to | denies | Provenienz wurde daher **nicht** in .agency/session.db geschrieben | 51 |
| 72 | relation_reading | candidate | Benennungslock | Kap 1–13 | applies_to | asserts | Der Benennungslock gilt für Kap 1–13. | 55 |
| 73 | relation_reading | candidate | Kapitel 14–26 | die Instanz | does_not_name_to_reader | denies | benennen die Instanz trotzdem nirgends leserseitig | 55 |
| 74 | relation_reading | refused: joined or shortened quote | Kapitel 14–26 | \[AEGIS v{X.X} // LOG\_{0xHEX}\]-Format | does_not_use | denies | verwenden auch kein \[AEGIS v{X.X} // LOG\_{0xHEX}\]-Format | 55 |
| 75 | relation_reading | candidate | Sprach-DNA | \[AEGIS v{X.X} // LOG\_{0xHEX}\]-Format | provides_for | asserts | obwohl die Sprach-DNA es | 55 |
| 76 | relation_reading | candidate | Kap 25 | Nachbarkapitel | follows_practice_of | asserts | Kap 25 folgt der Praxis der Nachbarkapitel | 55 |
| 77 | relation_reading | candidate | der Name | Akt II | may_be_released_to_reader_in | asks | Soll der Name — und das Log-Format — irgendwo in Akt II leserseitig freigegeben werden | 55 |
| 78 | relation_reading | candidate | Schleier-Benennung | Wohneinheit | alternative_placement | hedges | Alternativen wären eine spätere Setzung (Wohneinheit, ruhiger) | 56 |
| 79 | relation_reading | candidate | Schleier-Benennung | Kap 26 | alternative_relocation_to | hedges | die Verlagerung nach Kap 26 | 56 |
| 80 | relation_reading | candidate | Kap 25 | Abwesenheit des Klicks | uses_locally | asserts | Kap 25 verwendet die **Abwesenheit** des Klicks lokal | 57 |
| 81 | relation_reading | candidate | Vortex 1 Beat 3 | das Fehlen des Klicks | has_canonical_sensory_anchor | asserts | Kanonischer sensorischer Anker von Vortex 1 Beat 3 ist | 57 |
| 82 | relation_reading | candidate | lokale Vorform | Eskalationsstufe | is_intended_as | asks | Ist die lokale Vorform hier gewollte Eskalationsstufe oder vorweggenommenes Material? | 57 |
| 83 | relation_reading | candidate | Template-Kopf | drei Szenen | lists | asserts | Der Template-Kopf führt weiterhin drei Szenen, die Prosa hat sieben. | 58 |
| 84 | relation_reading | candidate | Drafting-Brief | Kopf | forbids_changes_except_status | asserts | Der Drafting-Brief verbietet Änderungen am Kopf außer status. | 58 |
| 85 | relation_reading | candidate | Szenenplan | Outline-Pass | should_be_updated_in | asks | Soll der Szenenplan in einem separaten Outline-Pass nachgezogen werden? | 58 |
| 86 | relation_reading | candidate | Einheit Station 7 | Figur mit eigenem Ziel | is | asserts | Sie ist jetzt eine Figur mit eigenem Ziel | 59 |
| 87 | relation_reading | refused: surface absent from document | Einheit Station 7 | Namenlosigkeit | remains_nameless | asserts | bleibt aber namenlos | 59 |
| 88 | relation_reading | candidate | Akt I | Einheit Station 7 | requires_namelessness_of | asserts | wie es Akt I verlangt | 59 |
| 89 | relation_reading | candidate | Einheit Station 7 | Kennung | could_receive_from_Akt_II | hedges | Ab Akt II könnte sie eine Kennung bekommen. | 59 |
| 90 | relation_reading | candidate | Einheit Station 7 | Akt III | carries_on_in | asks | Trägt sie in Akt III weiter (Kap 27/28) oder bleibt sie eine Delta-Sieben-Figur? | 59 |
| 91 | relation_reading | candidate | Der Canon | KW2 | assigns_chapters_to | asserts | Der Canon weist 14–22 KW2 und 23–28 KW3 zu | 60 |
| 92 | relation_reading | candidate | Der Canon | KW3 | assigns_chapters_to | asserts | Der Canon weist 14–22 KW2 und 23–28 KW3 zu | 60 |
| 93 | relation_reading | candidate | die gedrafteten Kapitel 14–26 | Verwaltungstopologie der Konstrukt-Stadt | set_in | asserts | die gedrafteten Kapitel 14–26 spielen durchgehend in der Verwaltungstopologie der Konstrukt-Stadt | 60 |
| 94 | relation_reading | candidate | Kap 25 | KW3 | fulfills_sensorily | asserts | Kap 25 löst KW3 jetzt | 60 |
| 95 | relation_reading | candidate | Kap 25 | Ort | does_not_change | denies | ohne den Ort zu wechseln | 60 |
| 96 | relation_reading | candidate | KW-Progression | Filterregime statt Ortswechsel | intended_reading_is | asks | Ist das die gewünschte Lesart der KW-Progression (Filterregime statt Ortswechsel) | 60 |
| 97 | relation_reading | candidate | 14–26 | KW2/KW3 | should_be_shifted_toward | asks | sollen 14–26 in einem eigenen Pass stärker nach KW2/KW3 verschoben werden | 60 |
