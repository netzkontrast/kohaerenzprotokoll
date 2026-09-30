# 03 — Die Fixpunkte und die offenen Weichen (research reader, 2026-09-30)

**Zweck.** Für eine neue, kapitelweise Plot-Behandlung: was der Autor wirklich geschlossen hat, was nur *berichtet*
wird, was die Quellen einhellig tragen, was offen ist, und welche Regeln des Buchs sich prüfen lassen.
**Nichts hier entscheidet etwas.** Jede „Default"-Zeile ist `PROVISIONAL` und trägt ihre Alternative.
Gelesen wurden: `CLAUDE.md`, `NOW.md`, `Plan/concept/novel-writing-plan_2026-09-29.md`, `Plan/weichen/w2-motor.md`,
`GOAL.md` (§1, §5, Anhang A–C), alle `Plan/decisions/*.md`, `Wiki/overview/plot.md`, die Köpfe und Positionstabellen der
Konflikte C1–C15 und Fragen Q1–Q9, die 41 Kapitelseiten (nur `records:` und die Zahl der Differenzen). **Kein neues
Dokument wurde gelesen.** Zitate `^[slug.md:Lnn]` sind mit `scripts/read.py --find` erfragt; Zeilenangaben wie „NOW.md L14"
oder „GOAL §5.4" sind die Zeilen/Abschnitte der Datei selbst.

**Statusschlüssel** (jede Zeile unten trägt einen):

| Marke | Bedeutung |
|---|---|
| **AUTOR** | Der Autor hat es in eigenen Worten geschlossen; Wortlaut, Datum und Datei stehen dabei. |
| **BERICHTET** | Eine Quelle *sagt*, der Autor habe es gelockt (2026-05-07, -30, -31). Die Logs selbst (`Entscheidungs-Log_2026-05-30 (+_2)`, `Konzept_Kapitel-40_Lesart-Dualitaet_2026-05-30`) sind **nicht** in `Sources/` (GOAL Anhang C1); nach Entscheidung 006 zählt kein Lock durch Datum oder Selbstanspruch. Billig wieder bestätigbar. |
| **BRIEFING** | Steht in `GOAL.md`, dessen Kopf sagt: „Verfasst von: einer vorherigen Claude-Sitzung … Autor: Michael". Auftrag des Autors, aber Formulierungen der Sitzung; Anhang A ist ausdrücklich Tier `M`. |
| **QUELLE** | Vorschlag/Regel eines Quelldokuments (auch wenn es sich `[K]` nennt). |
| **SESSION** | Vorschlag einer Claude-Sitzung (Schreibplan, W2-Blatt, Audit). |

---

## 1 · Vom Autor geschlossen — und was nur berichtet wird

### 1.1 AUTOR: die Zeile, die wirklich zählt

| Datum | Wortlaut des Autors | Wo | Was es schließt — und was nicht |
|---|---|---|---|
| 2026-09-16 | (Reset; Wortlaut nicht zitiert, Entscheidung „decided by: the author") | `Plan/decisions/001-reset-to-two-layers.md` | „`Manuscript/` is parked with it; its prose does not continue." Der Roman ruht; `Canon/` verliert den normativen Status. Ändert sich erst, wenn Fragen vor allem Kapitel/Plot betreffen — Bedingung der Entscheidung selbst. |
| 2026-09-23 | „Die Quellen sind in `Sources/`" (nach `GOAL.md`, Kopf von Anhang C1: „Der Autor hat am 2026-09-23 festgelegt") | `GOAL.md` Anh. C1 | `Sources/` ist Ausgangslage für alle Drive-Dokumente. **Offen** bleibt der Landeweg für Manuskript, NCP, claude.ai-Exporte. |
| 2026-09-24 | „Alle alten Entwürfe kommen wieder in Frage und müssen diskutiert werden — sources wird die neue Ausgangslage." | `Plan/decisions/006-every-draft-is-back-in-question.md` | Kein Dokument, kein Datum, kein „Source-of-Truth"-Anspruch beendet eine Position. Tiers/„newer wins" in `GOAL.md` §3.2 **suspendiert**. Jeder Konflikt ist Gesprächspunkt und schließt nur durch Autorwort. |
| 2026-09-24 | Gefragt: „*Sollen die fünf wiederkommen, bleibt es bei zwei, oder ist es etwas Drittes?*" — Antwort: **five**; bestätigt: „five Guardians — LogOS, Mnemosyne, Cerberus, Kairos and Sophia" | `Wiki/conflicts/c6-guardians-count-and-pairing.md`, Abschnitt „2026-09-24 — decided by the author: five Guardians" | **Nur Zahl und Namen.** Offen laut Record: wie sie zu den vier Kern-Welten stehen (Q5) und der *Erasure-Pol*. Die 2026-Lesarten „zwei", „absorbiert", „latent" bleiben Lesarten. |
| 2026-09-24 | „Ne stop - es ist nur kw1" (Korrektur der ersten Antwort „Die ganze Simulation") | `Wiki/conflicts/c9-konstrukt-stadt-scale.md`, Abschnitt „corrected by the author: KW1 only" | Die Konstrukt-Stadt ist **KW1**. Offen laut Record: wie KW1 sonst heißt (Q5) — und ob Akt II *ihre* Verwaltungstopologie behält (OQ-25-F, hier W8); C9 beantwortet das nicht. |
| 2026-09-24 | „Notiere in Zukunft einfach deine Fragen und setze fort" / „Sammle alle Fragen und fahre fort" | `NOW.md` L14–L16 | Prozess: Fragen notieren, weiterarbeiten. |
| 2026-09-26 | „Those arent Texts for the novel - only Research" und „Yes, 22 and 23 are research too" | `NOW.md` L23–L26 | Narrative Quelltexte (Kap-0/40-Fassungen, Kap-25-Datei …) sind Forschung, nie Romantext, nie Stimm-Referenz. |
| 2026-09-27 | „every subagent runs on Sonnet" (sinngemäß, so in `NOW.md`) | `NOW.md` L1138 | Prozess. |
| 2026-09-28 | „Dont start any new documents" | `NOW.md` L1039 | Kein neues Dokument wird gelesen (Schreibplan Frage D: Ausnahmen nur auf Ja, empfohlen D2). **Gilt für diese Arbeit.** |
| 2026-09-29 | „The novel in Legacy is Not the quality I want" | `NOW.md` L31–L33; Plan §2, §11 | Der geparkte Septemberentwurf wird nicht revidiert, seine Prosa ist nie Stimm-Referenz. Ob seine *Ideen* (Doran, `A-0001`, Gegenregister) zurückkommen, ist Frage B — **offen**. |
| 2026-09-29 | „I dont Like that the novel does Not Flow Like a scifi novel - i want more Action - its a question of the Plot" | `NOW.md` L35–L38; Plan §5 | Urteil über den **Plot**, nicht über Sätze. Folge (SESSION-Vorschlag, nicht entschieden): W2 zuerst; jeder Treatment-Absatz zeigt ein physisches Ereignis; Eskalations-Ledger pro Akt. |
| 2026-09-29 | „Install https://github.com/netzkontrast/writing-skills/tree/main into this repo", dann „But optimieren ihn für dieses repo" | `CLAUDE.md` (Abschnitt „The writing skills are adapted") | 13 lesende Skills + `writing-skills`; **keiner schreibt Prosa**; Kanon = Autorentscheidungen + freigegebene Kapitel, nie die Lesarten des Wiki. |
| 2026-09-29 | „Think about how to Write the novel and come up with a plan" (Auftrag, **keine** Entscheidung) | `Plan/concept/novel-writing-plan_2026-09-29.md` Kopf | Der Plan ist „Nothing in it is decided"; W1–W16 und A–D sind offen. |
| 2026-09-25 | „Extend the Wiki Pages with new Overview Pages - and start to Focus on Plot and the Chapters a Bit more" | `Plan/decisions/013-the-chapter-is-a-unit.md` | Das Kapitel ist Einheit neben dem Begriff; Differenzen stehen auf den Kapitelseiten, nicht als Records. |

**Kein Autor-Abschluss** (Delegationen an die Sitzung, betreffen nur die Werkzeugkette, keine Story-Frage):
008 („Answer the questions for me yourself"), 010 („Do what IS Best"), 012 („Beantworte die Fragen selber- und fahre fort"),
009 (auf Anweisung, Sitzung entscheidet). 007, 011, 014: Einwilligungen zu Modellaufrufen/Jules, keine Story-Inhalte.
Entscheidung 002–005: Pipeline.

**Nicht entschieden, obwohl es so wirken kann:** W1–W16 (alle offen; `Plan/weichen/` hat nur das W2-Blatt, `NOW.md` L104–L115,
keine Antwort des Autors bis `git log` 2026-09-30). Die Septemberlogs D-15 („F1 = Ereignis-Rückgrat von Akt I") und
53 weitere Entscheidungen traf die Sitzung auf „entscheide selbst" — Plan §2, W2-Blatt: „Das war eine der 53 Entscheidungen,
die die Sitzung selbst traf, keine von dir. Sie bindet nichts."
C1–C5, C7, C8, C10–C15, Q1–Q9: `status: open` im Frontmatter; C6 „decided — the count", C9 „decided — KW1 only".

### 1.2 BERICHTET: Locks, die Quellen dem Autor zuschreiben (wieder bestätigbar, Entscheidung 006)

Wer berichtet: das **storyform-und-outline** (2026-06-10, nennt sich „Einzige Grundlage für das Weiterschreiben des Romans"
^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L13], „bei Konflikt gewinnt das Neuere" — Anspruch, nicht angewandt),
das **Kapitel-Kompendium** (2026-05-31), **welt-sensorik-drafting** (2026-06-10), **begriffe-und-konzepte**, **kernwelten vollständig**,
die **Plot-Konkretisierung** (Vorschlag) und das **Dramatica-Status-PDF** (2026-05-07). Die *Quellen der Locks* (Entscheidungs-Logs
2026-05-30, Kap-40-Lesart) liegen nicht vor. **Empfehlung: dem Autor die Liste als ein Blatt „bestätigen / ändern / streichen" geben**
(Plan §4 Phase 1 sagt dasselbe: „re-confirming an earlier decision is the cheapest decision there is").

| # | Lock (wie berichtet) | Datum laut Quelle | Wortlaut | Berichtet von |
|---|---|---|---|---|
| L1 | Approach gespiegelt: A Be-er, B Do-er (+ Driver-Konstanz, IC-Träger-Präzisierung) | 2026-05-07 (Lock-In) | „A: Be-er (vorher Do-er). B: Do-er (vorher Be-er)." ^[dramatica-dual-storyform-status-2026-05-07-md.md:L29] | Status-Bericht; Charakter-Bibel (Tag danach) trägt noch das „Vorher" → **C8 offen** |
| L2 | Hybrid-Option-3 (Hard-Routing pro POV + Bridge-Szenen mit Soft-Layering) | 2026-05-07 | storyform L205 | storyform-und-outline |
| L3 | Erstsatz Kap 1 = letzter Satz, den Kael schreibt: „Das Licht ist schon da, als ich erwache." | 2026-05-30 | „Kap 1 ↔ Kap 39 (erster Satz = letzter Satz, den Kael schreibt; gelockt: …)" ^[kapitel-kompendium-gather-2026-05-31-md.md:L92]; storyform L127 | Kompendium, storyform, philosophie-im-detail, welt-sensorik L633 |
| L4 | Prosa-Regel Kap 1 (Akt I, verschärft Kap 1–13): Amnesie nie erwähnt; **eine** konkrete Falschheit pro Kapitel; Philosophie unter dem Konkreten; KW1 Metaphernverbot/assertorisch; „ein Mensch, ein konkreter Tag … ein Körper, eine Routine" | 2026-05-31 („aus User-Feedback") | „PROSA-REGEL KAP 1 (gelockt 2026-05-31, aus User-Feedback)" ^[kapitel-kompendium-gather-2026-05-31-md.md:L33]; „Die Amnesie wird nie erwähnt." ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L58] | Kompendium, storyform |
| L5 | Keine AEGIS-Stimme in Kap 1 (nur sterile Konsolen-Direktiven) | 2026-05-30 | „AEGIS-Stimme in Kap 1 (Lock 2026-05-30): keine." ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L208] | storyform |
| L6 | Schicht-1/Schicht-2 = 80/20; „Einheit 734" genau einmal, unkommentiert; Silas-Halbsatz „Etwas in der Frequenz der Lüftung schien zu—"; Ozon kalt/scharf, **keine Wärme in Kap 1** | 2026-05-30 | storyform L306 („Kap-1-Locks (2026-05-30)") | storyform; Plot-Konkretisierung nennt sie `[K]` |
| L7 | Blutung der Knöchel lebt **nur in Kap 0**; „Kap 1 bleibt spurlos" | 2026-05-30/31 | „Kap 0 alone … Kap 1 bleibt spurlos" ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L459]; ^[kohaerenz-protokoll-kernwelten-vollstaendig-2026-06-10-md.md:L141] | storyform, kernwelten, drafting manual, Alter-Profile — **13+ Quellen sehen es anders** (C10) |
| L8 | Naht: Kap 0 endet „Ich falle… in unzählige Scherben…", harter Schnitt auf den Erstsatz | 2026-05-30 | storyform L298 („**Naht-Lock:** harter Schnitt auf den gelockten Kap-1-Erstsatz") | storyform |
| L9 | Hitze-Polaritätsregel: kaltes Ozon = AEGIS-Unterdrückung (Landauer-Signatur, überall); Wärme = Junas ununterdrückbare Spur, **Debüt Kap 3**; Landauer-Wärme-Spike allein in Vortex 1 Beat 4; „nie mischen" | 2026-05-30 (OQ-B) | „Kaltes Ozon = AEGIS-Unterdrückung …" ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L64]; „Der Landauer-Wärme-Spike bleibt kanonisch allein für Vortex-1-Beat-4" ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L458]; R-5 ^[kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md:L1067] | storyform, welt-sensorik; Gegenposition in 41 Quellen (C11) |
| L10 | Slot 16: Akt I Hard-A-Default, **ein** Hard-B-Kapitel in Kap 5–8 mit AEGIS-**1.-Person**-Innensicht; Position beim Weaving zu pinnen; es enthüllt AEGIS, nicht Kaels Vielheit | 2026-05-30 | „Slot-16-Lock (2026-05-30), Akt I: Hard-A-Default; ein Kapitel Kap 5–8 ist Hard-B mit AEGIS-1.-Person-Innensicht" ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L207] | storyform, begriffe; Gegenposition C14 (31 Quellen) |
| L11 | Juna: „nie Subjekt, nur Wirkung"; gestaffelte Grammatik (Abwesenheits-Phase Akt I → Präsenz-Phase Akt II+ → direkt Kap 38); zwei Anker: Telefon-Stille (ruht bis Vortex, eingelöst Kap 39) und Silas; Revelation-Timing KW2/KW3 (Akt II), „Juna-Seed seit Kap 1, aber namenlos" | 2026-05-30 | „Grammatik-Regel: nie Subjekt, nur Wirkung." ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L286]; R-10 ^[kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md:L1087] | storyform, welt-sensorik; GOAL B11 nennt Widersprüche |
| L12 | Kap 40 doppellesbar (Reset ‖ Transfiguration); „Projektion erlauben, nie bestätigen" | 2026-05-30 (Kap-40-Lesart) | ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L68] | storyform; GOAL B17: Präzisierung, kein Konflikt |
| L13 | Genesis-Cluster-Flashbacks in Kap 18/21/22 („gesetzt"); Z1–Z3 = 15–17/18–20/21–23 | 2026-05-08 Konzept | GOAL Anh. A (OQ-Tabelle, `[M]`); storyform §7.3 „bleibt unberührt kanonisch" | Konzept; storyform |
| L14 | Sechs Ebenen: vier Kernwelten + Überwelt + Externe Ebene; Kernwelten als Akt-Marker | 2026-06-10 | kernwelten L13 („Sechs Ebenen …") | kernwelten, welt-sensorik; **Q3/Q5/Q6 offen**, **C9 (KW1) und C6 (fünf) sind Autorwort und haben Vorrang** |
| L15 | 10 „Hard-Constraints" der Projekt-Anleitung (kein didaktischer Schluss, AEGIS nie Bösewicht, Juna nie „Liebes-Interesse", keine Theorie nackt …) | Projekt-Anleitung 2026-05-08 | ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L81] … L84 | storyform L76–L85; welt-sensorik L1215ff |

Auch **BRIEFING** (Tier M, `GOAL.md` Anh. A, „zu verifizieren"): AEGIS als System-Ebene-ANP (T2-Setzung 2026-05-03), Moonshine-Link überträgt
MI/Resonanz/Zeugenschaft, nicht Daten/Nachrichten/Rettung (OQ-F **offen**), „Dekanonisiert: … LogOS, Cerberus, Kairos und Sophia als Figuren".
**Letzteres ist durch C6 (Autor, 2026-09-24) überholt** — siehe §4, Regel R-Dek.

---

## 2 · Die strukturellen Konstanten — was die meisten Quellen teilen

Alle Bereichsangaben so, wie `Wiki/overview/plot.md` sie mit geprüften Zitaten führt (Abschnitte „Where the sources agree / differ", L394–L412).
Alles hier ist **QUELLE**, nie Autorwort.

| Konstante | Was die Mehrheit sagt | Wer abweicht (nach `plot.md`) | Bemerkung für das Treatment |
|---|---|---|---|
| **Drei Teile à 13** | Kap 1–13 / 14–26 / 27–39 (Primzahl-Blueprint 2025, Ultra-Plot, Hard-SF-Outline, AEGIS-Subplots, strukturierter Outline, Editorial Dossier) | Duale Storyform-Synthese (04-28): Teile „bei Kap 26" verzahnt; **Akt-III-Beginn**: 27 (storyform, Dossier, die meisten) · „ab ~28" (Hintergründe L308) · **29** (kernwelten L408) ; **KW3 = späte Akt II (23–28)** in worldbuilding, kernwelten, Sprach-DNA, master report | Kap 1–26 tragfähig; 27–29 tragen eine Weiche (W8). |
| **Kapitelzahl** | **41 Bewegungen** = Kap 0 + 1–39 + Kap 40 („Bewegungen — Kap 0 (Genesis-Prolog), Kap 1–39 (Hauptroman), Kap 40 (geheilte Genesis als Coda)" ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L2]; Kompendium L13; „jeder andere 2026-Plan" dieser Lesung) | **39 ohne Rahmen**: Primzahl-Blueprint, Ultra-Plot, Hard-SF-Outline, AEGIS-Subplots, *master report* (2026-05-08, selbes Datum wie das 41-Konzept), 39-Kapitel-Spec, worldbuilding, Hintergründe, philosophischer Bericht; ohne Zählung: Systems Narrative Analysis u. a.; Kohärenz-Protokoll-Narrativ: 22 Kapitel, kein Kap 13. Das Iteration-Genesis-Dokument nennt die Erweiterung selbst: das Spec „(drei Modi, 39 Kapitel) muss um Kap 0 und Kap 40 erweitert werden" (plot.md L400) | **W4.** Kap 1–34 sind in beiden Fassungen gleich → dort ist das Treatment formunabhängig. |
| **Vortex** | **Vortex 1 = Kap 35–36, fünf Beats**: Convergence / Pivot / Silence / Heat Spike / Rotation (storyform L366ff; GOAL B9: die neueren Dokumente folgen „Anhang B"); Beat 3 = „Strukturell notwendige Pause — nicht mit Inhalt füllen" (storyform); Truth-Rotation hier | **Anzahl**: *einer* (+ Resolution 37–39): master report, 39-Spec, worldbuilding, Hintergründe, philosophischer Bericht, Systems Narrative Analysis, die vier weiteren 2026-05-08-Berichte, Dramatica-Synthese und AEGIS-Analyse (04-30); *zwei* (Vortex 2 = 38–39, Kap 37 trügerischer Sieg): konsolidiertes Konzept und „jeder andere 2026-Plan"; philosophy-catalogue hat zwei ohne Kap 37; die drei ältesten Pläne nennen kein „Vortex". Zwei Beat-Listen für Vortex 1 (B9); welche Beats in Kap 35 vs 36: Nach `NOW.md` L363–L368 unsicher | **W4.** Kap 37 existiert nur im Zwei-Vortex-Plan. |
| **Storyform-Wendung B→A** | „echt" bei **34/35** (Kompendium, storyform L116) oder **35/36** (strukturierter Outline L103, konsolidiertes L781) | 36/37 (39-Spec L634); Dramatica-Synthese: Driver-*Flip* (vs. Lock-In: Pivot *als Storyform-Übergang*, GOAL §5.2) | „Drei Übergänge nie verwechseln" (GOAL §5.1, BRIEFING): 13/14 und 26/27 = Modus; 34/35 = Storyform; 36/37 = Konsolidierung. **Diagnose-Ebene (W1).** |
| **Modi** | Heldinnenreise innen 1–13 · Zyklen 14–26 (Z1 15–17, Z2 18–20, Z3 21–23, Genesis-Flashbacks 18–22; „unberührt kanonisch" storyform L460) · Heldenreise außen 27–39 | s. o. (Akt-III-Beginn; Kap 14 „Bruch", 24 K-J-Thema, 25–26 Wendepunkt sind Quell-Setzungen) | **W1** entscheidet, ob Modi Rezept oder Diagnose sind. |
| **Rahmen Kap 0 ↔ Kap 40** | „ein einziger Atem in zwei Richtungen" ^[kap0-kap40-doppelklammer-abhandlung-2026-05-08-md.md:L25]; Genesis-Klammer; Kap 40 = geheilte Genesis, doppellesbar | Kein Kap 0/40 in den 14 „Nicht-41"-Plänen; **Ouroboros**: Kap 1↔Kap 39 (Erstsatz) vs. Kap 0↔Kap 40 (Seite `ouroboros-struktur`, `NOW.md` L380) | Beide Klammern parallel tragbar (storyform: „Zwei Klammern"; GOAL §5.1). |
| **Letztes Bild Kap 40** | „Wir tragen die Scherben — und sie sind das Mosaik, das die Welt hält. Liebe bleibt. Wie der Schmerz." (storyform L426; strukturierter Outline L1244; Abhandlung L372) | „Wir tragen die Welt; Liebe bleibt, wie der Schmerz; das Universum hält" (konsolidiertes Konzept ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L1040], Iteration-Genesis). **Die lange Form enthält beide Wörter** — „Scherben" *und* „Welt" schließen einander dort nicht aus. | W14. |
| **Kap-1-Fixpunkte** | Erstsatz; 80/20; „Einheit 734" einmal; Silas-Halbsatz; keine Wärme, kein Telefon, keine Blutung, keine AEGIS-Stimme; Schluss-Triade „Es sind einundzwanzig Grad. / Es ist still. / Ich schlafe." (BRIEFING `[M]`, nur im Septemberentwurf bestätigt) | Nur die Blutung hat echte Gegenpositionen (C10: Kap 1, nur Kap 0, „in keinem Kapitel", „Nyx' Stimme") | alle **BERICHTET** (L3–L8); Kap 1 ist der dichteste Lock-Block des Buchs. |
| **Genesis** | Vier Beats Einheit → Cluster/Komponente-734-Funktionalisierung → Trennungsprotokoll → Wir-AEGIS-plural (Kap 39) (konsolidiertes Konzept, Kompendium, storyform L298) | **Drei Beats, Kael *als* 734**: Charakter-Bibel, master report, philosophischer Bericht (C12); vierter Beat „offen"/„ungelöst": worldbuilding, philosophischer Bericht; ein dritter Kandidat „Erinnerungs-Versiegelung" (Hintergründe); **734 vor oder aus dem Trennungsprotokoll** (C12) | **W12.** Flashback-Kapitel 18/21/22 sind schon in beiden Fassungen gesetzt. |
| **Dual-Storyform A‖B** | simultan, nie A vor B encoden; A MC Kael (Change/Start, Success/Good), B MC AEGIS (Steadfast/Stop, Failure/Bad w. Dividend) (GOAL §5.2) | Duale Storyform-Synthese 04-28: Kael MC *beider*, AEGIS IC von B; Dramatica-Synthese: H1 „AEGIS MC in Universe", AEGIS ohne Approach; C8 | **Diagnose** (W1); Beschlussgegenstand nur, wo Prosa daran hängt. |
| **Kernwelten** | vier Regime (KW1 Konstrukt-Stadt = **AUTOR**, C9) + Überwelt + Externe Ebene (Köln 2026 „nie Bühne, nur Fragment, Geruch, Telefonton" — *alle* Quellen teilen das, C13) | Namen/Skalen C5, Q6; Überwelt als KW3 „Überwelt/Nexus" und KW4 „Externe Ebene" (philosophischer Bericht L437–443); KW2 „Resonanz-Landschaft" vs „Mnemosyne-Archipel" (`NOW.md` L284) | W8, W11. |
| **Kast** | dreizehn Alters (ANP: Kael, Lex, Alex, Rhys, Selene · EP: Nyx, Kiko, Lia, Isabelle, Moros · Argus · Spiegel Silas, Oblivion) in jeder Quelle ab 2026-05-08 | **elf**: Ultra-Plot 2026-02-26, Inquiry 2025; Charakter-Kompilation streicht Silas und Oblivion („Silas: Dekanonisiert." ^[charakter-kompilation-fuer-kohaerenz-protokoll.md:L322]) | W10. |

**Differenzen pro Kapitelseite** (aus `## Where the sources differ`, `records:` der Seiten), Stand heute: die meisten haben Kap 1 (8), Kap 8 (8), Kap 3 (7), Kap 35 (7), Kap 2 (6), Kap 9 (6), Kap 10 (6). Kapitel **ohne** Record, aber mit Differenzen:
2, 10, 13, 15, 16, 23, 27, 28, 35 — dort sind es Titel-/Weltdifferenzen, die nach Plan §3 beim Absatz entschieden werden. Gesamt: 156 Kapitel-Differenzen, 8 auf `plot.md` (Plan §1).

---

## 3 · Die offenen Weichen

**Regel für das Treatment bei Ungelöstem.** (a) Jeder Absatz trägt am Kopf die Weichen, von denen er abhängt, z. B. `⟨W5, W9⟩`.
(b) Wo eine Weiche offen ist, schreibt der Absatz den **Default** als `PROVISIONAL[Wn=…]` und darunter **eine** Alternativzeile `ALT[Wn=…]`; das Ereignis,
das den Absatz trägt, soll — wo möglich — unter beiden Fassungen stehen bleiben (*Ereignis zuerst, Weichenwert als austauschbare Sensorik/Benennung*).
(c) Nie „entschieden" schreiben; nie einen Default aus Datum, Selbstanspruch oder Zahl der Quellen begründen (Entscheidung 006). Ein Default wird hier nur nach
drei Kriterien vorgeschlagen: **(i) Autorwort, (ii) bereits berichteter Lock (billig zu bestätigen), (iii) kleinster Schaden, falls falsch**.
(d) Ein Register `Plan/runs/plot-2026-09-30/switches` (oder die Tabelle unten) bleibt die einzige Stelle, an der ein Wert steht; Absätze verweisen nur.

### 3.1 Die sechzehn Weichen des Schreibplans

Format: **Weiche — Optionen mit belegten Positionen — Verhalten bei Nichtentscheidung (PROVISIONAL) — Kapitel.**

| Weiche | Optionen (belegt) | Wenn ungelöst: Default `PROVISIONAL` / Alternative | Kapitel |
|---|---|---|---|
| **W1 Theorie: Rezept oder Diagnose** | *Diagnose*: „Story-First … Theorie ist Diagnose, nicht Rezept" (GOAL §1.5, **BRIEFING**). *Rezept*: die Kapitelseiten und der strukturierte Outline führen vier simultane Strukturebenen je Kapitel (GOAL §5.1; storyform §1 „drei simultane Ebenen" `[K]`); Plot-Konkretisierung: die Bedeutungs-Architektur ist im Überfluss, „Handlungs-Substanz im Mangel" ^[kp-plot-konkretisierung-13-ideen-f1-faden-2026-06-10-md.md:L29] | **PROVISIONAL: Diagnose.** Absätze tragen Ereignisse; Dramatica/Modi/Kishōtenketsu erscheinen nur als nachgelagerte Spalte „Struktur-Befund" (Plan 2e). **ALT:** Struktur als Vorgabe pro Kapitel. Folge des Defaults: Modusgrenzen 13/14, 26/27, Storyform-Wende 34/35 bleiben Befunde, nicht Gebote. | alle |
| **W2 Motor** | A F1 „Sachbearbeiter der Abweichung" ^[kp-plot-konkretisierung-13-ideen-f1-faden-2026-06-10-md.md:L112] (durch „Der Apparat ist nie bedrohlich, immer höflich" leise by design); B Reise/Einbruch/Flucht (Hard-SF-Outline 2026-04-08: Kap 13 Sturz, Kap 24 Einbruch, Kap 26 Flucht; setzt W8 voraus, vorkanonisch); C Löschung als Gegner mit sichtbarer Uhr (SESSION-Vorschlag im W2-Blatt, „in keiner Quelle belegt"; Bausteine: Wartungsfenster L68, „Timelock — der Erasure-Countdown läuft." ^[dramatica-dual-storyform-status-2026-05-07-md.md:L238], „Der Leser erlebt B-Timelock äußerlich" ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L536]); D frei | **Kein sinnvoller Kapitel-für-Kapitel-Default ohne W2** (es ändert jedes Kapitel). PROVISIONAL für *Treatment v0*: **engine-neutrales Skelett** — alle BERICHTET/AUTOR-Fixpunkte und die zwischen A/B/C gemeinsamen Ereignisse (Kael erwacht; Wärme-Debüt Kap 3; Schleier-Fall Kap 13; Vortex; Kap 0/40), je Absatz eine Zeile `Motor: A / B / C`. Das W2-Blatt empfiehlt „C, mit A als Innenleben" — SESSION-Empfehlung, nicht Autorwort. Die Frist-Mechanik („zwei Uhren", Optionlock A / Timelock B) ist schon als `[K]` berichtet (storyform L144) und stützt C/A, **aber** C verlangt eine Antwort auf W7 (was weiß Kael über die Fenster?). | alle |
| **W3 Stimme** | Erste Person Präsens Kael: Erstsatz „… als ich erwache" (L3), Kap 0 Funken-Ich; dritte Person Vergangenheit: drei frühere Kap-1-Anfänge (Plan §2: 2025-04-19, 2026-02-22 …). Weitere Sichten: POV-Träger → Storyform (Alters außer Spiegel → A; AEGIS → B; Silas/Oblivion Bridge; Argus A mit Kommentar) (GOAL §5.2, BRIEFING); „Stimmen werden **nie** gelabelt" (GOAL §5.4). | **PROVISIONAL: Ich-Erzähler Kael, Präsens** — weil der berichtete Lock L3 dies impliziert (Erstsatz, *Kael schreibt* den Bericht/das Buch, storyform L414) und es die kleinste Verschiebung ist. **ALT:** dritte Person Präteritum. Der Septemberentwurf *war* Ich/Präsens (Dev-Editor-Gutachten, Profil) — **kein** Argument (Entscheidung 001, Urteil 2026-09-29). | alle; Kap 0/40 Wir; AEGIS-Kapitel s. W6 |
| **W4 Gestalt** | 41 Bewegungen/zwei Vortices (konsolidiertes Konzept u. a.) · 39 Kapitel/ein Vortex (master report, 39-Spec, worldbuilding …) · 39 + Rahmen mit *einem* Vortex existiert **nicht** als Quelle (master: kein Rahmen) — außer die 39-Spec wird um Kap 0/40 erweitert, wie Genesis L818 es beschreibt | **PROVISIONAL: 41 Bewegungen, Kap 0 + 1–39 + Kap 40, Vortex 1 = 35–36, Kap 37 trügerischer Sieg, Vortex 2 = 38–39** (meiste Quellen der Kanon-Ära *und* trägt den Rahmen, den der BERICHTETE Erstsatz-Lock mitdenkt). **ALT:** 39 Kapitel, ein Vortex 35–36, Resolution 37–39 (kein Kap 37-Sieg). Kap 1–34 unverändert; nur 0, 35–40 hängen daran. | 0, 35–40 |
| **W5 Hitze/Kälte** | Kalt=AEGIS/Wärme=Juna, Landauer-Wärme nur Vortex 1 Beat 4 (L9, storyform, welt-sensorik R-5) · Landauer-Wärme in Kap 6/36 (konsolidiertes Konzept, strukturierter Outline) · beides als *eine* Signatur „Hitze und Ozon" (master report, Sprach-DNA „spürbar als Ozon-Geruch oder Hitzeschlieren") · Wärme auch für Silas (Alter-Profile) · Juna-Wärme schon in Kap 0 (Abhandlung/Fassung) — C11, 41 Quellen | **PROVISIONAL: Polaritätsregel L9** (berichtet, in `rules.json`-Form als „Lock gewinnt für die Prosa-Sensorik" schon GOAL B5). Offene Autor-Frage laut GOAL B5: ist „Hitze/Temperatur-Spike ohne Wärme-Qualität" zulässig? **ALT:** Kap 6/36 Landauer-Wärme. Absätze schreiben das Ereignis (Sweep, Fenster, Stillstand), Sensorik als `⟨W5: kalt-Ozon | Wärme⟩`. | 0, 1, 3, 6, 8, 11, 12, 25, 36, 37, 38 (Plan), + Kap 22 (Fund) |
| **W6 AEGIS auf der Seite** | Dritte Person/Logs, nie `ich` (Charakter-Bibel, konsolidiertes Konzept L425, kernwelten, Alter-Profile, master report) · ein Kapitel 5–8 in der ersten Person (storyform L207, begriffe) · „Protokollform ohne Ich" (Plot-Konkretisierung Idee 12; GOAL B6 „Tertium") · „nie Ich", aber Operative Interiorität (Sprach-DNA) · erste Person durch ganz B, dritte in Vortex (philosophischer Bericht) — C14, 31 Quellen | **PROVISIONAL: genau ein Hard-B-Kapitel in Kap 5–8, AEGIS in Protokollform ohne `ich`** (kleinster Bruch *beider* Lager, liefert zugleich den „Löschung von innen"-Generator = physisches Ereignis). Position im Fenster 5–8 **nicht pinnen** (Lock sagt: beim Weaving). **ALT:** keine AEGIS-Innensicht; nur Logs/Konsolen. Kap 1: keine AEGIS-Stimme (L5) gilt in beiden. | 0, 5–8, 14, 22, 25, 34 |
| **W7 Schleier** | Klartext-Diagnose erst Kap 13 (welt-sensorik R-3; GOAL B10), „~Kap 10" in der Projekt-Anleitung (L15 #6), Wir-Geflecht nicht vor Kap 9 (L15 #8); erste leserseitige Benennung erst Kap 25 im Septemberentwurf (OQ-25-B); DKT-Vokabular „in den ersten 50 Seiten" nicht vs. „bis Kap 13" (`rules.json`, GOAL §5.4) | **PROVISIONAL: Fall des Schleiers Kap 13; Wir-Andeutung frühestens Kap 9; Begriffe Alter/Fragment/ANP/EP/TSDP/DID nicht vor Kap 13; AEGIS-Name: offen (OQ-25-A)** — alle vier Werte stehen als Lock-Berichte und liegen im Bereich der Quellen (GOAL B10 „Aussprache ~10, Klartext ab 13"). **ALT:** Kap 10 / Kap 25. Trifft W2=C hart (öffentliche Frist vs. Schleier). | 1–13 und darüber |
| **W8 Wo Akt II spielt** | KW2 = 14–22, KW3 = 23–28, die Welten sind Orte, die durchreist werden (Kanon-Plan, worldbuilding, Sprach-DNA L185, master report ~20–26) · „Die Welten sind Filter, nicht Orte. Kael bewegt sich nicht durch verschiedene Räume" (`kohaerenz-protokoll-kernwelten-vollstaendig-2026-06-10-md.md:L955`; ebenso „Kein Multiverse. Eine Realität, mehrere Filter" L901) · „Filterregime statt Ortswechsel"? ^[2026-09-14-kap25-vertiefung-md.md:L60] (Kap-25-Log, OQ-25-F) · KW3 hat im strukturierten Outline **kein** Kapitel | **PROVISIONAL: Filter-Lesart mit benannten Regimen pro Zyklus** (Kernwelten vollständig, Welt-Sensorik „Kernwelten sind Akt-Marker", und vereinbar mit C9/KW1-only, da KW1 ein *Regime* ist). **ALT:** physische Reise KW2→KW3 (verlangt von W2=B, stützt „mehr Action"). Jeder Akt-II-Absatz trägt ein Feld `Ort: ⟨Regime/Ort⟩`; das **Ereignis** (Bruch Kap 14, Zyklen Z1–Z3, Flashbacks 18–22) ist in beiden identisch. Akt-III-Beginn: 27 (PROVISIONAL) / 28 / 29. | 14–28 |
| **W9 Juna** | Erste direkte Erscheinung **Kap 38 Beat 3**, Kap 33 = Wirkung (strukturierter Outline L1385; storyform; kernwelten; Sprach-DNA) · einmal ca. Kap 33 (Charakter-Bibel L280 „Im gesamten Roman taucht Juna einmal in einer Szene auf …") · Offenbarung in Akt II, kein Kapitel (master report) · Kap 34 Eintritt ins System (Hard-SF-Outline) · nie Subjekt/Körper (L11, R-10, **BERICHTET**). Ursprungs-Ich: ist Juna das abgespaltene Ich, oder was es traf (J68, drei Antworten) | **PROVISIONAL: Kap 38 Beat 3 als erste direkte Erscheinung („einfach da", keine Beschreibung), Kap 33 als Wirkung; Juna nie Subjekt/Körper; J68 nicht verwendet** (Treatment sagt nie „Juna = Ursprungs-Ich"). **ALT:** Kap-33-Szene, bzw. Juna-Offenbarung ohne Kapitelnummer in Akt II. | 0, 3, 12, 22, 26, 33, 34, 38 |
| **W10 Die Besetzung** | dreizehn Alters (ab 2026-05-08) · elf (Ultra-Plot, Inquiry, Kompilation strikt: Silas/Oblivion dekanonisiert) · Silas und Oblivion als Spiegel-Alters (storyform, Status-Bericht L332 „ontologisch Doppelfiguren") · **Doran** nur im Septemberentwurf und seinem Record — in `Sources/` und `Wiki/` 0 Treffer (Plan Appendix) · **Mira** nur im Abhandlungs-Satz „Lex, Nyx, Kiko, Mira, alle" ^[kap0-kap40-doppelklammer-abhandlung-2026-05-08-md.md:L327] · Alex: im Trennungsmoment oder davor (C12/Kap-0-Annotation „Konzept-Konflikt?") | **PROVISIONAL: dreizehn, Silas/Oblivion = Spiegel-Alters; *weder Doran noch Mira* im Treatment** (ohne Autorwort, B/Figurenkarten). **ALT:** elf; Doran als Seismograph der Glättung (nur falls Frage B = B1 und Autor ja). | alle (Stimmen), bes. 2, 3, 8, 31–33 |
| **W11 Guardians auf der Seite** | **Anzahl: fünf — AUTOR.** Figuren in Szenen vs. Komponenten von AEGIS (Q1; Q5: „KEIN Guardian-1:1" 2026 vs. je Welt 2025; Erasure-Pol „Name offen, Forschungsfrage" ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L217]; `Wächter` vierfach, Q4); Kap 31 „Auflösung der Guardians" (Plural) | **PROVISIONAL: fünf Namen gesetzt (AUTOR); Status „AEGIS-Architektur-Komponente, die in Szenen *wirkt*, nicht Figur mit Wunsch" in Kap 25, 29–32, 36; keine Welt-Paarung; Erasure-Pol = Funktion ohne Namen.** **ALT:** je Welt gepaart (Kairos+Sophia teilen KW4); Guardians als Figuren. Regel R-Dek ist zu reparieren (§4). | 25, 29–32, 36 |
| **W12 Genesis** | vier Beats (konsolidiertes Konzept, storyform L298, Kompendium) · drei (Charakter-Bibel) — **Kael als 734 oder dessen Rest** (Abhandlung/Fassung: Rest; annotierte Kap 0: „wird Kael") — Herkunft AEGIS C3: aus dem Nichts / aus der Simulationsdynamik / aus Kaels Abwehr / aus Fragmenten in der Leere | **PROVISIONAL: vier Beats; Flashbacks Kap 18/21/22, Beat 4 in Kap 39; Verhältnis Kael–734 *im Treatment unbenannt* (nur „Komponente 734 wird getrennt") bis Autorwort** (vermeidet die schärfere, schadensreichere Setzung). **ALT:** drei Beats mit Kael = Ergebnis der Trennung. Q7 (was 734 benennt): Kap 1/2/10/25/22. | 0, 18–22, 24, 39, 40 |
| **W13 AEGIS nach dem Vortex** | plurale Übernahme „Funktion bleibt" (GOAL §5.2, BRIEFING); Oblivion übernimmt AEGIS' Funktion in Kaels Innensystem: „Wenn AEGIS in der Truth-Rotation kollabiert, übernimmt Oblivion AEGIS' Funktion in Kaels Innensystem" ^[dual-storyform-hintergruende-md.md:L372]; lebendes Relikt/erloschen/verwandelt (Q8); Name der Form offen (OQ-A, `Wir-AEGIS-plural` = Arbeitsbegriff, storyform L475) | **PROVISIONAL: AEGIS-monolithisch erlischt in Kap 36; plurale Übernahme in Kap 39; Name der Form ungenannt („das Wir"); Oblivion-Rolle offen.** **ALT:** Oblivion übernimmt; AEGIS als lebendes Relikt. | 36–40 |
| **W14 Kap 40 / Außen-Ebene** | doppellesbar (L12, **BERICHTET**) · letztes Bild: lange Form (Scherben+Welt) vs. „Wir tragen die Welt" (s. §2) · Köln 2026 „nicht außerhalb" (4 Quellen) vs. Basisrealität „jenseits der Simulation" (2) — C13 · Abhandlung: drei „Setzungen" zur Bestätigung (Vermittler-Stimme = Wir-AEGIS-plural, Wärme-Spur in Kap 0, dieselben Scherben an beiden Enden) | **PROVISIONAL: doppellesbar (Projektion erlauben, nie bestätigen); letztes Bild = lange Form; Köln 2026 nur als Fragment/Geruch/Telefonton, Lage *nicht benannt*.** **ALT:** „Wir tragen die Welt"; Basisrealität jenseits. Die drei Setzungen bleiben *Fragen an den Autor*, nicht im Treatment. | 0, 39, 40 |
| **W15 Moonshine-Link** | MI/Resonanz/Zeugenschaft übertragbar, **nicht** Daten/Nachrichten/Rettung (BRIEFING `[M]`, OQ-F „vor RS-Throughline-Encoding klären" ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L480]) · Plot-Konkretisierung Idee 4 „Leitung, die in keinem Plan steht" (ein Kanal) · GOAL B11: „Der Kap-30-Kanal ist kein Auftritt, prüfen" · Q9 | **PROVISIONAL: Es geht nur Wirkung über (Wärme, Telefon-Stille, Silas-Resonanz), keine Nachricht.** **ALT:** eine Leitung trägt Information (Idee 4). Hier Kollision mit W2-Plot-Wünschen. | jedes Kapitel mit Juna-Spur (3, 7, 12, 22, 24, 30, 33, 34, 38, 39) |
| **W16 Länge** | Plan: nach dem Piloten messen. | **PROVISIONAL: offen bis Kap 1–3.** Treatment misst keine Wortzahl. | alle |

### 3.2 Weichen und Fragen, die ein Kapitel-Plot berührt und die der Schreibplan *nicht* als Weiche führt

Der Schreibplan §5 nennt: C8, C10, C15 werden *am Kapitel* entschieden; C1, C2, C4, C5, Q2, Q4, Q6 sind Forschungsfragen, nur wo ein Kapitel sie braucht. Hier die, die der Plot **tatsächlich anfassen muss**, plus Funde aus `NOW.md`/den Records, die keine Weiche tragen:

| Schalter | Optionen (belegt) | Default `PROVISIONAL` / ALT | Kapitel |
|---|---|---|---|
| **C10 Knöchel-Blutung** | Kap 1 (Charakter-Bibel, Hard-SF-Outline 2026-04-08) · **nur Kap 0** (storyform, Kompendium, drafting manual, Alter-Profile — **BERICHTET** L7) · „Eröffnungsbild, nicht Kap-1-Zeile" (konsolidiertes Konzept) · Eigenschaft ohne Kapitel (strukturierter Outline, master report, Sprach-DNA) · Kap 0 *ohne* Knöchel/Nyx (Kap-0-Entwurf 2026-05-08) | **PROVISIONAL: Kap 0 allein, in Nyx' Stimme; Kap 1 spurlos; Wiederkehr am Ende „OQ-Knöchel" offen.** ALT: Durchgangsfaden Kap 0→1→39/40 (Kap-40-Notiz 2026-05-30). | 0, 1, 4, 9, 39 |
| **C8 AEGIS-Approach in B** | Be-er (Charakter-Bibel) · Do-er (Lock-In-PDF, konsolidiertes Konzept, Kompendium, master report) · kein Approach (Dramatica-Synthese, Duale Synthese) | **PROVISIONAL: Do-er** (L1: Lock-In-Bericht nennt das Be-er *als Vorher*). Trifft keinen Plot-Absatz, nur Wortwahl der AEGIS-Handlungen („AEGIS handelt, statt zu sein"). | B-Kapitel |
| **C15 Flight-Riss** | Kiko (+Lia) · Lia+Isabelle · implizit | Erst beim Kapitel der Träger; bis dahin `⟨C15⟩` ohne Namen. | Kapitel mit Riss-Szenen |
| **C5/Q6 Garten, Überwelt** | Garten = ganze Kernwelt / Ort in KW4 / beides; Nexus=Überraum=Überwelt? | Nur am Kapitel (33, 35–36, 38–39): Setting benennen mit **dem Wort der jeweiligen Quelle** + `⟨C5/Q6⟩`. | 13, 20, 33–39 |
| **Q3 Kernwelt ↔ Alter** | Welten = Akt-Marker (welt-sensorik §3, Alters an Riss-Typen *nach Trigger*) vs. Zuordnung | **PROVISIONAL: Akt-Marker, Alters nach Trigger.** | alle Akt-II/III-Kapitel |
| **Q7 Was „734" benennt** | Komponente 734 / Wohneinheit 734 / absichtlich beides; Plot-Konkretisierung: Fund in Kap 22 „Er wohnt in der Akte seiner eigenen Quarantäne" (`[V]`) | **PROVISIONAL: „Einheit 734" in Kap 1 einmal unkommentiert (L6); Deutung offen bis Kap 22 (ALT: Fund-Szene wie F1)**. Anker 734: Kap 1→2→10→25→22 (GOAL Anh. A `[M]`). | 1, 2, 10, 22, 25 |
| **Funktionale Multiplizität — wo erreicht** | Kap 33 (FM-Achievement, Status-Bericht L361; master report; worldbuilding) · Kap 39 (philosophie-im-detail „Plurale Apotheose") · im Vortex (Companion Guide, Systems Narrative Analysis) | **PROVISIONAL: Kap 33 Teilerreichen, Kap 39 Vollzug** (beide Linien vereinbar). Keine Record → Frage an den Autor. | 33, 35–36, 39 |
| **Wann entscheidet das Wir zu bleiben** | Kap 38 (Tabelle), Kap 38 Beat 5, Kap 39 (Text) — philosophie-im-detail | PROVISIONAL: Kap 38 Beat 5 Entscheidung, Kap 39 Vollzug. | 38–39 |
| **Cache-Konflikt** | Kap 6 (Tabelle) vs. Kap 18 (Titel, Iteration-Genesis) | PROVISIONAL: Kap 6 (Akt I „Echos im Fundament", storyform L311); Kap 18 Z2-Titel offen. | 6, 18 |
| **Mosaik-Herz** | Kap-11-Beat vs. Kap-34-Ort | `⟨Mosaik-Herz: Kap 11 | Kap 34 | beides⟩` | 11, 34 |
| **KW3 hat in einem Plan kein Kapitel** | strukturierter Outline: Cerberus-Labyrinth nur in der Weltentabelle; drafting manual: „Späte Akt II (Kap 23–28)" + Überwelt-Nexus Kap 33 | PROVISIONAL: KW3 = Kap 23–28 (Regime), siehe W8. | 23–28 |
| **F1-Setzung „Abweichungen = K₁-Spuren"** | blockierend für F1 (Plot-Konkretisierung L262), W2-Blatt: „hängt an einer ontologischen Setzung" | An W2 gekoppelt; Treatment zeigt Abweichungen als *Ereignis* (Ticket, Fenster), nicht als Ontologie. | 2–13, 22 |
| **Domänen der Throughlines** (OS-A Physics/OS-B Mind vs. OS-A Psychology/OS-B Physics) | zwei Berichte gleichen Datums | Diagnose-Ebene (W1=Diagnose) → nicht ins Treatment. | — |
| **Wer bringt das Paradox im Vortex** | Kael bringt es; im philosophischen Bericht AEGIS | PROVISIONAL: Kael (alle anderen lesenden Quellen). | 35–36 |
| **Rhys' Bogen** | „Anker Akt I → Kudzu Akt II" vs. „Akt-II-Anker → Kudzu" | unbenannt, bis W10. | Akt I–II |
| **Kap-25-Log OQ-25-A…F** | an den Autor gerichtet: AEGIS-Benennung, Schleier-Satz „Hier sitzt mehr als einer.", Klick, Szenenplan, Station 7, **KW-Mapping (= W8)** | wie W7/W8; übrige: nicht ins Treatment, als Fragen weitergeben. | 24–28 |
| **C1–C4, Q1, Q2, Q4** | Forschung (AEGIS-Akronym, Entropie, Emergenz, blinder Fleck, Protokoll-Begriffe, `Wächter`) | Nur falls ein Absatz sie *benutzt*: dann das Wort der einen zitierten Quelle + `⟨Cn⟩`; sonst fern halten (Theorie nie nackt). | — |
| **Frage A–D (Schreibplan §11)** | Prosa: A1/A2/A3 · September-Ideen: B1/B2 · Ort: C1/C2/C3 · Lesen: D1/D2/D3 | **Kein Treatment-Default nötig** — berührt Prozess, nicht Plot. Aber **B** bestimmt, ob Doran/`A-0001`/Gegenregister zitierbar sind; **D** bestimmt, ob ein Plot-Loch per Lesen oder per Weiche geschlossen wird (Autor 2026-09-28: keine neuen Dokumente). | — |

---

## 4 · Die Regeln des Buchs als prüfbare Nebenbedingungen

Jede Zeile: Regel · Scope · Herkunft (Marke §0) · **Prüfart**: `code` = entscheidbar per Programm (Zeichenfolge/Zählung/Parser-frei), `heur` = Heuristik (Wortlisten, Parser), `man` = nur Autor/Lektüre. Die Felder folgen `GOAL.md` §5.4 (ID, Scope, Quelle, Lock-Datum, Prüfart).

### 4.1 Gelockte Kap-1-Einträge (alle BERICHTET)

| ID | Regel | Scope | Herkunft | Prüfart |
|---|---|---|---|---|
| K1-1 | Erster Satz von Kap 1 = „Das Licht ist schon da, als ich erwache." Letzter Satz, den Kael in Kap 39 schreibt, = derselbe | Kap 1, 39 | L3 (2026-05-30) | **code** (Zeichenvergleich) |
| K1-2 | „EINHEIT 734" genau einmal, ohne Kommentar, Kael reagiert nicht | Kap 1 | L6 | **code** (Zählung) + man (Kommentarlosigkeit) |
| K1-3 | Silas-Halbsatz „Etwas in der Frequenz der Lüftung schien zu—" wörtlich | Kap 1 | L6 | **code** |
| K1-4 | Keine Wärme, kein Telefon, keine Blutung in Kap 1 | Kap 1 | L6, L7 | **heur** (Wortliste: warm, Hitze, Telefon, Blut …) |
| K1-5 | Keine AEGIS-Stimme: nur sterile Konsolen-Direktiven, keine 3.-Person-Systemlog-Stimme | Kap 1 | L5 | **heur/man** |
| K1-6 | 80/20 Schicht 2 : Schicht 1; eine Schicht pro Szene; Ozon = Szene 3, dichte Stille = Szene 4 | Kap 1 | L6 | **man** (Anteil), **heur** (Szenen-Marker) |
| K1-7 | Amnesie nie erwähnt („ich erinnere mich nicht" verboten); **eine** konkrete Falschheit pro Kapitel | Akt I (Kap 1–13) | L4 (2026-05-31) | **heur** (Verbformen), **man** (Falschheit zählen) |
| K1-8 | Metaphernverbot, assertorische Sätze in KW1 (Stilebene 1) | KW1-Kapitel | L4; welt-sensorik L75 | **heur** (Vergleichspartikel), **man** |
| K1-9 | Naht: Kap 0 endet „Ich falle… in unzählige Scherben…", Kap 1 beginnt mit dem Erstsatz | Kap 0/1 | L8 | **code** |
| K1-10 | Schluss-Triade „Es sind einundzwanzig Grad. / Es ist still. / Ich schlafe." | Kap 1 | BRIEFING `[M]` (nur im Septemberentwurf) — **nicht einmal berichtet von einer Kanon-Quelle** | **code**, aber *Status unsicher* |

### 4.2 Sensorik, Stimme, Figur

| ID | Regel | Scope | Herkunft | Prüfart |
|---|---|---|---|---|
| R-Hitze | Kaltes Ozon = AEGIS/Landauer; Wärme = Junas Spur, **Debüt Kap 3**; nie in einer Stelle mischen; Ausnahme Vortex 1 Beat 4 | alle | L9; welt-sensorik R-5 ^[kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md:L1067]; **C11 offen (41 Quellen)** | **heur** (Wort-Kookkurrenz warm+Ozon in einer Szene), **man** (Semantik) |
| R-Juna | Juna nie grammatisches Subjekt, nie physisch beschrieben, nie Liebes-Interesse, nie Deus ex machina; erste direkte Erscheinung „einfach da", keine Beschreibung | alle; Kap 38 | L11; R-10 ^[kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md:L1087]; storyform L286 | **heur** (Parser: Subjekt-Position von „Juna"), **man** (Liebes-Interesse) |
| R-Juna-Timing | Abwesenheits-Phase Akt I, Präsenz-Phase ab Akt II; Seed ab Kap 1 namenlos; Offenbarung in KW2/KW3; `rules.json` hat „Juna" in `veil_allowed_names` (GOAL B11 Widerspruch) | Akt I/II | L11 | **code** (Name in Kap n) + man |
| R-Schleier | Kein Alter/Fragment/ANP/EP/TSDP/DID-Vokabular in Akt I; Klartext-Diagnose erst Kap 13; Wechsel durch Syntax-Bruch, nie durch Header/Label | 1–13 | welt-sensorik R-3 ^[kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md:L1059]; GOAL B10 (~10 vs 13) | **code** (Wortliste), **heur** (Label) |
| R-Wir | Kein bewusstes Wir vor Kap 9; Stimmen nie gelabelt; Stilcode-Einbrüche ab Kap 2–3 | 1–9 | L15 #8 ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L83]; GOAL §5.4 | **heur** |
| R-Bridge | Max. drei Stimmen-Mikrocues pro Bridge-Szene; Bridge-Stapelung Akt I ≤ ~10 % | Akt I | welt-sensorik R-4; L15 #7 | **man** (Cue-Zählung heur) |
| R-AEGIS | Nie Bösewicht; tragisch unschuldig; kein moralisches/affektives Vokabular in Logs; spricht nie metaphorisch (Mnemosyne darf) | alle | L15 #2; welt-sensorik R-8 | **heur** (Wortliste), **man** |
| R-AEGIS-Stimme | `ich`-Verbot und Hard-B-Kapitel stehen gegeneinander | 5–8 | **C14 offen** | **man** — bis W6 gesetzt ist, *nicht automatisch prüfen* |
| R-Theorie | Theorie nie nackt: Bild/Raum/Verhalten; keine DKT-Begriffe (Bereich 50 Seiten vs. Kap 13); Landauer als Ozon/Temperatur, nie als Gleichung | Akt I | L15 #10; GOAL §5.4 (Abweichung „zu prüfen") | **code** (Wortliste), **man** |
| R-Szene | Max. 1 Konzept pro Szene; max. 1 Genesis-Echo pro Szene; eine Schicht pro Szene; Genesis-Formel nie wörtlich wiederholt (nur strukturell) | alle | welt-sensorik R-6, R-7, R-9 ^[kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md:L1083] | **code** (R-9: Zeichenkette der Formel), **man** (R-6/7) |
| R-Ton | Tonale Achse „Liebe bleibt, wie der Schmerz" — jede Szene daran geprüft; Heilung = Akzeptanz, nicht Tilgung; kein didaktischer Schluss; keine Resolution-Glättung in Kap 37 | alle; Kap 37, 39/40 | L15 #1, #4, #9; GOAL §5.3 | **man** |
| R-Kap40 | Doppellesbar; „Projektion erlauben, nie bestätigen": kein Erzähler-Satz, der Reset als Tatsache markiert; keine als Tatsache gezeigte Figuren-Amnesie am Schluss | Kap 39/40 | L12 ^[kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md:L68] | **man** |
| R-Anker | Telefon-Stille: Kap 7 → 24 → 30 → 39 (BRIEFING `[M]`; welt-sensorik L470 `[K]`, „ruht bis Vortex"); 734: 1 → 2 → 10 → 25, Fund Kap 22; Silas aktiv ab ~31/32; Wärme ab Kap 3; Klick höchstens vier explizite Nennungen (F1, `[V]`) | siehe | BRIEFING/QUELLE | **code** (Ledger) |
| R-Dek | „Dekanonisierte Namen nie aktiv" (GOAL §5.4; Anh. A nennt u. a. LogOS, Cerberus, Kairos, Sophia) | alle | BRIEFING `[M]` — **durch C6 (AUTOR, 2026-09-24) für diese vier Namen *hinfällig***. Eine Prüfung, die sie flaggt, würde die Autor-Entscheidung verletzen. | **Liste neu schneiden** vor jedem `code`-Einsatz |
| R-Block4 | Der reale Name des Autors nie in der Prosa; nur „Stille" (GOAL §5.4 „Block-4-Anker"; Anh. B3 nennt Block-4-Konsistenz) | alle | BRIEFING, Provenienz unklar | **code** (Namensliste, falls der Name gegeben wird) |

### 4.3 Anforderungen an das Treatment selbst (Plan, alle SESSION bzw. AUTOR-Urteil)

| ID | Regel | Herkunft | Prüfart |
|---|---|---|---|
| T-Phys | Jeder Absatz zeigt **ein physisches Ereignis** (jemand tut etwas, etwas widersteht, etwas geht verloren/wird gewonnen); rein innere/ideelle Kapitel nur als erklärte Pause | Autor-Urteil 2026-09-29 → SESSION-Ausformung (Plan §5) | **heur** (Verb-/Objektprüfung), **man** (Autor) |
| T-Crit | Die 6 Kriterien „eine Figur, eine wiederholbare Handlung, ein Objekt, ein Ort, ein Verlust, eine Eskalationsrichtung" ^[kp-plot-konkretisierung-13-ideen-f1-faden-2026-06-10-md.md:L29] | QUELLE (`[V]`) | **code** (Felder ausgefüllt), **man** |
| T-Hook | Hook-in/Hook-out als Ereignis, nicht Thema; Ledger: Anker gepflanzt → geechot → bezahlt; Leser-Wissen je Akt | Plan 2b/2c; GOAL §5.5 Readiness Gate (8 Punkte) | **code** (Ledger-Vollständigkeit), **man** |
| T-Cite | Jeder Satz zitiert Lesart/Entscheidung mit Zeile aus `read.py --find` oder ist **new** | Plan §3; GOAL §1.10 | **code** (`quotes.py`) |
| T-Switch | Jeder Absatz nennt seine offenen Weichen; nie „entschieden" | dieses Papier | **code** (Register-Abgleich) |
| T-Range | Kapitelzahlen/Akte/Modi nur innerhalb des gewählten Werts von W4/W8 | W4, W8 | **code** |
| T-Geo | Wenn W8=Filter: kein Ortswechsel-Verb zwischen Regimen; wenn W8=Reise: benannter Übergang | W8 | **heur** |

### 4.4 Was keine Regel ist (Fallen)

- **„Bei Konflikt gewinnt das Neuere"** (storyform L13; GOAL §3.2) ist ein Quellenanspruch, **suspendiert** durch Entscheidung 006. Kein Default darf daraus folgen, auch nicht für C10/C11.
- **`rules.json`/Skill-Kanon** (`chapter-draft-engine`, `chapter-briefing-architect`) sind älter als 006; Plan §7 und GOAL B3/B4/B7: Prozedur ja, Kanon nein.
- Der **Septemberentwurf** ist weder Kanon noch Stimm-Referenz (Autor 2026-09-29; Plan §2). Seine Entscheidungen D-01…D-53 sind Sitzungsentscheidungen.
- **Logs/Briefing** als `BRIEFING`/`[M]` dürfen keine `[K]` werden (GOAL §1.4).

---

## 5 · Kurz: was ein Treatment-Autor heute *weiß*

1. **Geschlossen (AUTOR):** fünf Guardians (Namen); Konstrukt-Stadt = KW1; alle Entwürfe wieder in Frage; der Roman im Legacy ist nicht die gewünschte Qualität; Plot braucht mehr Action/SF-Fluss; keine neuen Dokumente lesen; narrative Quelltexte sind Forschung.
2. **Nicht geschlossen, aber die dichteste Schicht:** 15 BERICHTETE Locks (§1.2) — ein Bestätigungsblatt würde W5, W6, W7, W9, W12, W14 (Teile) und alle Kap-1-Regeln auf einen Schlag sichern.
3. **Kein Motor (W2)** → nur ein engine-neutrales Treatment-Skelett v0 ist ehrlich herstellbar; das Skelett kann Kap 0/1/3/13/35–40 und Regel-Verankerungen tragen.
4. **Formunabhängig** in beiden Plan-Fassungen (W4): Kap 1–34. Formabhängig: Kap 0, 35–40.
5. **Drei Stellen, an denen Briefing und Autorwort kollidieren:** R-Dek (LogOS … „dekanonisiert" vs. C6), Anh. A „keine Guardian-Reiche" vs. offene Paarung Q5, und „Kernwelten = Akt-Marker" vs. das Septembermodell „KW2 14–22" (W8).
6. **Zeilenzitate** in dieser Datei stammen aus `read.py --find` oder den Dateien selbst; keine Zahl ist neu gemessen. Zahlen wie „41 Quellen" sind das `sources:`-Feld der Records.
