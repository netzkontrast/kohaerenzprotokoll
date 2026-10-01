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

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.228, 102.8 s. **70 rows**: 65 candidates, 5 refused, 0 duplicates.

| # | kind | status | term | stance | quote | lines |
|---|---|---|---|---|---|---|
| 1 | reading | candidate | Kap 25 | asserts | Kap 25 war mit **1.137 Wörtern** das schwächste Kapitel des Manuskripts | 17 |
| 2 | reading | candidate | Kap 0 | asserts | Kap 0 ausgenommen, eigene Rahmenpoetik | 17 |
| 3 | reading | candidate | Akt-II-Arc | cites | Akt-II-Arc verlangt für 24–26 eine getragene Schwellensequenz | 17 |
| 4 | reading | refused: quote not placed | Masterplan-Zeile 25 | cites | die Masterplan-Zeile 25 verlangt „zwei genuine Zukunftsverluste“, eine „physische Verzweigung“ und einen Körperbogen |  |
| 5 | reading | candidate | Nicht-Handlung | asserts | Damit ist die Nicht-Handlung als **Entscheidung** lesbar statt als Freeze (Arc-Auflage) | 21 |
| 6 | reading | candidate | Entscheidung | asserts | Jetzt bewegt sich um 10:58 die Hand von selbst auf das Bestätigungsfeld — mit eigener Syntax (Verb vorn, keine Bedingung) und eigener Somatik (Schulter, Kiefer, flacher Atem) | 21 |
| 7 | reading | candidate | Schleier | asserts | Anschließend fällt der Schleier leserseitig | 21 |
| 8 | reading | candidate | Schleier-Disziplin | cites | Canon §0 Schleier-Disziplin verlangt genau das für Kap 25–26 | 21 |
| 9 | reading | candidate | Optionlock | asserts | Der Optionlock wird zählbar (abgeben/splitten sind seit zwei bzw. vier Wochen graue Felder ohne Ton) | 22 |
| 10 | reading | candidate | Eigennutz | asserts | aus nachvollziehbarem **Eigennutz** (Restwertschwelle → Besuch der technischen Ebene), nicht aus Güte | 22 |
| 11 | reading | candidate | Einheit von Station 7 | asserts | Die Einheit von Station 7 hängt die Priorität-1-Wasserführung und zwei weitere Vorgänge auf sich um | 22 |
| 12 | reading | candidate | Kaels Verweigerung | asserts | Kaels Verweigerung hat einen bezifferten Preis bei einem Dritten | 22 |
| 13 | reading | candidate | Nebenfigur | asserts | Damit trägt eine Nebenfigur eine eigene Handlung mit eigenem Ziel | 22 |
| 14 | reading | candidate | Apparat | asserts | Zusätzlich registriert der Apparat die Abweichung, ohne zu handeln | 22 |
| 15 | reading | candidate | Wegkreuzung | asserts | Die Wegkreuzung wird physisch, und KW3 wird sensorisch aktiv. | 23 |
| 16 | reading | candidate | KW3 | asserts | Die Wegkreuzung wird physisch, und KW3 wird sensorisch aktiv. | 23 |
| 17 | reading | candidate | Canon-Weltanker | asserts | Das löst den Canon-Weltanker für Kap 25 ein (KW3, Wartungsschächte, Anker 734 dritte Wiederkehr) | 23 |
| 18 | reading | candidate | Hook-in | asserts | Hook-in aus Kap 24 explizit (die einrastende Verkleidung) | 25 |
| 19 | reading | candidate | Vorgang ohne Datentyp | asserts | der Vorgang ohne Datentyp wird gegrüßt (Finger daneben, nicht darauf) | 25 |
| 20 | reading | candidate | Klick | asserts | der Klick wird als **Abwesenheit** hörbar (sechsmal vor dem siebten Bestand, danach nicht mehr) | 25 |
| 21 | reading | candidate | Hook-out | asserts | neuer Hook-out: die Restzahl steht nach Schichtende bei 34 statt 31 und wird morgen früh nicht bei sechs stehen | 25 |
| 22 | reading | candidate | Kap 25 | cites | Kap 25: Schwelle, nicht Konfrontation; Schleier offen benannt; Hitze-Polarität; R-Regeln | 31 |
| 23 | reading | candidate | Warteschlange | cites | Warteschlange als einziges bewegtes Element | 31 |
| 24 | reading | candidate | Wegkreuzung | asserts | interner Wahlpunkt | 38 |
| 25 | reading | candidate | Wegkreuzung/Tore | asserts | von extern auferlegter Schwelle → interner Ort der Entscheidungsfindung | 38 |
| 26 | reading | candidate | Schritt ins Ungewisse | asserts | bewusste Wahl, Kap 26 | 38 |
| 27 | reading | candidate | KW3-Unterorte | asserts | Schleusen des Misstrauens, Gänge der Paranoia, Panoptikum — als Hintergrund für Kontrollpunkt-/Überwachungslogik | 39 |
| 28 | reading | candidate | Lichtführung | asserts | harte Kontraste, tiefe Schatten | 39 |
| 29 | reading | candidate | Schutz-Anteil | asserts | Schutz-Anteil als Aktionssystem (Verteidigung) gegen ANP-Alltagssystem | 40 |
| 30 | reading | candidate | inneres Tauziehen | asserts | als Körperbild für die gegenläufige Spannung im Unterarm | 40 |
| 31 | reading | candidate | TSDP-Analyse: Kaels innere Welt | asserts | älteres Roster (Kai), nur strukturell genutzt | 40 |
| 32 | reading | candidate | Co₁/McL/B/Ly-Taxonomie | asserts | Co₁/McL/B/Ly-Taxonomie ist nicht der aktuelle KW-Kanon, nur Sensorik entnommen | 41 |
| 33 | reading | refused: surface absent from document | Tiefenanalyse von „The Agency System“ | asserts | trägt die Achse des Kapitels | 38 |
| 34 | reading | refused: joined or shortened quote | \[S\]-Quellen | asserts | Kein Material aus \[S\]-Quellen wurde als Kanon behandelt | 43 |
| 35 | reading | refused: joined or shortened quote | \[K\]-Repo-Canon | asserts | alles Weltkonkrete der Prosa stammt aus \[K\]-Repo-Canon oder aus den bereits gedrafteten Nachbarkapiteln | 43 |
| 36 | reading | candidate | Vielheit | asserts | Vielheit wird benannt, **kanonisch gefordert** für 25–26, ohne klinisches Vokabular, ohne Header, ohne Sprecher-Tags | 47 |
| 37 | reading | candidate | Mikrocues | asserts | drei Mikrocues in der Handszene, am Limit, nicht darüber | 47 |
| 38 | reading | candidate | kaltes Ozon | asserts | kaltes Ozon **nur** in der Abmeldeszene, Wärme dort nicht | 47 |
| 39 | reading | refused: quote not placed | Wärmespur | asserts | Wärmespur nur als Rückverweis („die vier Abende“) in einer ozonfreien Szene |  |
| 40 | reading | candidate | Genesis-Echo | asserts | max. ein Genesis-Echo je Szene | 47 |
| 41 | reading | candidate | Direktiven | asserts | Direktiven ohne Metapher, Moral, Affekt | 47 |
| 42 | reading | candidate | Kap-0-Zitate | asserts | keine wörtlichen Kap-0-Zitate | 47 |
| 43 | reading | candidate | Juna | asserts | Juna nie Subjekt, nie Name, nie Körper, nie Stimme | 47 |
| 44 | reading | candidate | Ein-Falschheits-Regel | asserts | **eine** objektive Falschheit (die Inhaltserfassung lief 02:10–02:14 in einer Nacht, in der Kael nachweislich wach war und zählte) | 47 |
| 45 | reading | candidate | Restzahl-Anstieg | asserts | der Restzahl-Anstieg ist bewusst **erklärbar** gehalten, damit keine zweite entsteht | 47 |
| 46 | reading | candidate | Telefon-Stille-Anker | asserts | Telefon-Stille-Anker getragen, nicht gebrochen | 47 |
| 47 | reading | candidate | Kaels Signatur | asserts | Kaels Signatur bricht nur dort, wo ein Wechsel gemeint ist. | 47 |
| 48 | reading | candidate | Storyform-Slots | asserts | die Storyform-Slots sind von einer Prosavertiefung nicht berührt | 51 |
| 49 | reading | candidate | Kapitel 25 | asserts | Kapitel 25 ist in keiner der beiden Dateien encodiert. | 51 |
| 50 | reading | candidate | Aligned | asserts | Slot-Werte (Resolve/Growth/Approach/Driver/Limit/Outcome/Judgment) unverändert. → **Aligned.** | 51 |
| 51 | reading | candidate | agency-Capability-Verben | asserts | Die agency-Capability-Verben standen in diesem Lauf nicht zur Verfügung | 51 |
| 52 | reading | candidate | Benennungslock | asserts | Der Benennungslock gilt für Kap 1–13. | 55 |
| 53 | reading | candidate | AEGIS-Benennung | asserts | Die gedrafteten Kapitel 14–26 benennen die Instanz trotzdem nirgends leserseitig | 55 |
| 54 | reading | candidate | Sprach-DNA | cites | obwohl die Sprach-DNA es | 55 |
| 55 | reading | candidate | Kap 25 | asserts | Kap 25 folgt der Praxis der Nachbarkapitel (nur VERSALIEN-Direktiven). | 55 |
| 56 | reading | candidate | AEGIS-Benennung | asks | Soll der Name — und das Log-Format — irgendwo in Akt II leserseitig freigegeben werden | 55 |
| 57 | reading | candidate | Schleier-Benennung | hedges | Alternativen wären eine spätere Setzung (Wohneinheit, ruhiger) oder die Verlagerung nach Kap 26. | 56 |
| 58 | reading | candidate | Klick-Motiv | asserts | Kap 25 verwendet die **Abwesenheit** des Klicks lokal (eine Station, ein Tag). | 57 |
| 59 | reading | candidate | Klick-Motiv | cites | Kanonischer sensorischer Anker von Vortex 1 Beat 3 ist | 57 |
| 60 | reading | candidate | Klick-Motiv | asks | Ist die lokale Vorform hier gewollte Eskalationsstufe oder vorweggenommenes Material? | 57 |
| 61 | reading | candidate | Header-Szenenplan | asserts | Der Template-Kopf führt weiterhin drei Szenen, die Prosa hat sieben. | 58 |
| 62 | reading | candidate | Header-Szenenplan | cites | Der Drafting-Brief verbietet Änderungen am Kopf außer status. | 58 |
| 63 | reading | candidate | Header-Szenenplan | asks | Soll der Szenenplan in einem separaten Outline-Pass nachgezogen werden? | 58 |
| 64 | reading | candidate | Einheit Station 7 | asserts | Sie ist jetzt eine Figur mit eigenem Ziel, bleibt aber namenlos | 59 |
| 65 | reading | candidate | Einheit Station 7 | hedges | Ab Akt II könnte sie eine Kennung bekommen. | 59 |
| 66 | reading | candidate | Einheit Station 7 | asks | Trägt sie in Akt III weiter (Kap 27/28) oder bleibt sie eine Delta-Sieben-Figur? | 59 |
| 67 | reading | candidate | KW2 | cites | Der Canon weist 14–22 KW2 und 23–28 KW3 zu | 60 |
| 68 | reading | candidate | KW3 | asserts | Kap 25 löst KW3 jetzt **sensorisch** ein (Treppenkopf, Wartungsebene), ohne den Ort zu wechseln. | 60 |
| 69 | reading | candidate | KW-Progression | asks | Ist das die gewünschte Lesart der KW-Progression (Filterregime statt Ortswechsel) | 60 |
| 70 | reading | candidate | Verwaltungstopologie der Konstrukt-Stadt | asserts | die gedrafteten Kapitel 14–26 spielen durchgehend in der Verwaltungstopologie der Konstrukt-Stadt (Datenknoten, Delta-Sieben, Wohneinheit 734) | 60 |
