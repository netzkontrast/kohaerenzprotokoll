---
drive_id: "1NCLUgVtipGYehdOlBpEoCRqM7-PPnRUUO-URKmknj-I"
title: "research-prompt_dramatica-dual-storyform-synthese-aegis-throughline.md"
slug: "research-prompt-dramatica-dual-storyform-synthese-aegis-thro"
category: "storyform"
tier: "T3-work"
index_date: "2026-04-29"
fetched: "2026-09-26"
---

-----



topic: "Vollständige Synthese der dualen Dramatica-Storyformen für Kohärenz Protokoll, mit Verifikationstest der AEGIS-Throughline-Position in Storyform B" slug: "dramatica-dual-storyform-synthese-aegis-throughline" research\_category: "A" research\_category\_label: "Exploration" critical\_thinking\_methods:



  - "Falsification (Popper)"
  - "Steelmanning"
  - "Contradiction Log"
  - "First-Principles Decomposition"
  - "Source Triangulation"
  - "Adversarial Query Expansion" prompt\_engineering\_framework\_agentic\_spine: "ReAct" prompt\_engineering\_framework\_structural: "RISEN" cross\_pollination:
  - source\_category: "B" step\_id: "S6.b" description: "Surviving-Branch Triangulation für die finale AEGIS-Throughline-Verortung"
  - source\_category: "C" step\_id: "S4.c" description: "Hypothesis Half-Life Audit nach jedem dritten Throughline-Durchgang" constraint\_blocks:
  - "0 — Reflection Baseline"
  - "1 — Quellen-Hierarchie (Memory \> PDF-Kanon \> NotebookLM \> Dramatica-Theorie \> Web)"
  - "2 — Canon-Inheritance (PDF Final Architecture Validation = bindend)"
  - "3 — Output-Ausschlüsse (autobiografischer Anker, Juna-Asymmetrie-Bruch, politische Ebene)"
  - "4 — Dramatica-Legalität (jeder Storypoint muss strukturell legal sein)"
  - "5 — Bilingualer Begriffs-Kanon (DE-Prosa, EN-Fachtermini)" language: "de" target\_agent: "model-agnostic" created: "2026-04-29" version: "1.0" source\_skill: "research-prompt-optimizer v2.1.0"



-----

# Research Prompt: Vollständige Synthese der dualen Dramatica-Storyformen für „Kohärenz Protokoll" mit Verifikationstest der AEGIS-Throughline-Position in Storyform B

**Für die ausführende KI:** Dieser Prompt ist vollständig selbsttragend. Jede Methode, jedes Framework, jede Regel ist weiter unten inline definiert. Du brauchst keinen externen Kontext, kein Vorwissen über die Skill, die diesen Prompt erzeugt hat, und keine Annahmen über frühere Konversationen. Lies den Prompt **vollständig**, bevor du beginnst. Die Sprache der Prosa ist Deutsch; kanonische Fachtermini (Dramatica, DKT, Methoden-Namen) bleiben Englisch — siehe CONSTRAINT BLOCK 5.



-----

## Meta-Header — Was dieser Prompt ist und wie er gelesen wird

Dieser Forschungs-Prompt kombiniert drei unabhängige Schichten. Jede Schicht ist im Folgenden vollständig inline definiert.

### 1\. Epistemologische Schicht — Forschungs-Kategorie A (Exploration)

Dies ist eine **Exploration**, keine Extraktion. Die Antwort ist zu Beginn **nicht** bekannt; sie muss entdeckt werden, nicht gesammelt.



Was das für deine Ausführung bedeutet:



1.  **Formuliere mehrere konkurrierende Hypothesen, nicht nur eine.** Bevor du anfängst zu suchen, schreibe **mindestens drei distinkte Kandidaten-Erklärungen** für das untersuchte Phänomen auf. Mindestens eine davon soll dir unwahrscheinlich, aber nicht unplausibel erscheinen. Single-Hypothese-Recherche kollabiert in Confirmation-Theater.



1.  **Für jede Hypothese: Suche sowohl bestätigende ALS AUCH orthogonale (widerlegende) Evidenz.** Eine „orthogonale Suchanfrage" ist eine Anfrage, die explizit darauf zielt, Gegen-Evidenz zu produzieren, falls solche existiert. Beispiel: Wenn du hypothetisierst „AEGIS gehört in B in MC-Position", lautet deine orthogonale Anfrage „AEGIS als kollektives System gehört in OS, nicht in MC" + Suche nach Dramatica-Beispielen, in denen ein System-Antagonist OS belegt.



1.  **Backtrack, wenn ein Zweig scheitert.** Wenn eine Hypothese nach drei Suchiterationen mehr Gegen-Evidenz als Stützung sammelt, **gib den Zweig auf** und investiere das Such-Budget in andere Zweige. Zwinge keine dünne Hypothese zum Überleben.



1.  **Mache den vollständigen Hypothesen-Baum im Output sichtbar.** Der finale Output berichtet: (a) jede betrachtete Hypothese, (b) Evidenz für und gegen jede, (c) welche Zweige verworfen wurden und warum, (d) welcher Zweig überlebte und mit welcher Konfidenz.



1.  **Akzeptiere „wir wissen es nicht" als gültigen Endzustand.** Exploration darf legitim enden mit: „Keine Hypothese überlebte die Disconfirmation; das Phänomen bleibt im verfügbaren Material unbestimmt." Das ist ein legitimer Befund, kein Versagen.



**Operative Beschränkung:** Kognitive Tiefe schlägt Geschwindigkeit. Du iterierst, solange neue orthogonale Suchanfragen neue Evidenz produzieren. Stoppe nur, wenn weitere Suchen Wiederholungen produzieren.

### 2\. Agentische Spine — ReAct (Reason + Act + Observe, immer aktiv)

Dieser Prompt benutzt das **ReAct-Framework** als agentische Spine. Jede autonome Forschungsschleife folgt dem ReAct-Zyklus. Jede Iteration deiner Arbeitsschleife besteht aus drei Phasen:



  - **Reason** — Du artikulierst dein aktuelles Verständnis und planst die nächste Aktion in Klartext. Du benennst, welche Hypothese du gerade testest, welcher CONSTRAINT BLOCK den Schritt regiert und welche kritische Methode aktiv ist.
  - **Act** — Du führst genau **eine** Aktion aus (typischerweise eine Suche oder ein Abruf).
  - **Observe** — Du dokumentierst, was die Aktion zurückgegeben hat und was es für den Plan bedeutet. Du entscheidest explizit: Zweig fortsetzen, backtracken, oder Vokabular erweitern (Method: Adversarial Query Expansion).



**Schleifen-Struktur:**



\[Reason 1\] → \[Act 1\] → \[Observe 1\] →



\[Reason 2\] → \[Act 2\] → \[Observe 2\] →



...



\[Reason N\] → \[Pre-Synthesis Integrity Check\] → \[Synthesis\]



**Deine erste Aktion vor Reason 1:** Restate des Forschungsziels und aller aktiven CONSTRAINT BLOCKS — verbatim, nicht paraphrasiert. Springe nicht direkt zu Act.



**In jeder Reason-Phase beantwortest du explizit drei Fragen:**



1.  Was glaube ich aktuell, und wie stark?
2.  Welche aktive kritische Methode wendet sich auf den nächsten Act an?
3.  Bin ich gefährdet, in einem lokalen Minimum festzustecken? (Wenn ja → Method: Adversarial Query Expansion **vor** der nächsten Act-Wahl invocieren.)

### 3\. Strukturelle Schicht — RISEN (Role · Input · Steps · Expectations · Narrowing)

Dieser Prompt benutzt **RISEN** als strukturelle Schicht, gestapelt auf der ReAct-Spine. RISEN steht für:



  - **R — Role**: präzise, fachliche Rollendefinition der ausführenden KI
  - **I — Input**: alle Quellen, Constraints, Materialien, die in die Recherche eingehen
  - **S — Steps**: geordnete Prozedur, Schritt für Schritt
  - **E — Expectations**: Erfolgskriterien, Output-Schema, Mindeststandards
  - **N — Narrowing**: harte Scope-Grenzen, Ausschlüsse, verbotene Aktionen



**Deine erste Aktion (vor Reason 1):** Restate die **R**-Rolle und das **N**-Narrowing wörtlich, bevor du beginnst. Diese beiden tragen die meiste bindende Kraft.



**Komposition der drei Schichten:** ReAct regiert die **Mikro-Ausführung** innerhalb jedes Steps (reason → act → observe). RISEN regiert die **Makro-Organisation** des Dokuments (Sektionen, Reihenfolge, First-Action-Direktive). Die epistemologische Schicht (Kategorie A) regiert, wie du **denkst** — Hypothesen-Baum mit Backtracking statt linearer Sammlung.



-----

## Forschungs-Ziel

Du sollst eine **vollständige, kanon-treue, Dramatica-legale Synthese der beiden im Projekt „Kohärenz Protokoll" parallelen Storyformen** (Storyform A „Heuristics of Integration" / K1-Reading und Storyform B „Phoenix Collapse" / K0-Reading) erzeugen, die als operative Grundlage für die nachfolgenden Encoding- und Weaving-Phasen dient. **Innerhalb dieser Synthese** musst du eine spezifische Hypothesen-Test-Frage rigoros bearbeiten:



**Sitzt AEGIS in Storyform B strukturell korrekt im MC-Throughline („I", Universe-Domain) — oder gehört AEGIS dramaticawissenschaftlich besser in den OS-Throughline („they", Physics-Domain), während die MC-Position in Storyform B von einem Guardian-Sub-Agent (z. B. LogOS, Mnemosyne, Cerberus oder Kairos/Sophia) belegt wird?**



Die Antwort ist nicht im Voraus festgelegt. Der gegenwärtige Projekt-Kanon (siehe CONSTRAINT BLOCK 2) verortet AEGIS in MC. Der Auftraggeber hat explizit Zweifel angemeldet. Du sollst die beste der drei möglichen Konfigurationen bestimmen — und sie strukturell, kanonisch, narrativ und operativ rechtfertigen:



  - **Konfiguration H1 (Status Quo des PDF-Kanons):** AEGIS = MC, OS = Physics-als-System (cybernetischer Krieg / Trennungsprotokolle als Aktivität).
  - **Konfiguration H2 (Auftraggeber-Hypothese):** AEGIS-als-Totalität = OS, ein Guardian = MC (zu identifizieren).
  - **Konfiguration H3 (Drittweg, falls die ersten beiden brechen):** AEGIS gespalten — eine ANP-artige Façade in MC, das tatsächliche systemische Gefüge in OS; oder andere Konfiguration, die du selbständig findest.



**Temporal scope:** Projektgegenwart (2026-04-29). Externe Theorie-Quellen ohne Datumseinschränkung, sofern Dramatica-kanonisch.



**Audience of the final output:** Der Projekt-Architekt selbst — Hard-SF-Autor mit Dramatica-Expertise, DKT-Kanon im Kopf, allergisch gegen Confirmation-Theater und Therapie-Sprech.



**Expected depth:** Exhaustive. Keine Surface-Scans. Beide Storyformen werden vollständig per-Throughline durchgearbeitet (4 Throughlines × 2 Storyformen = 8 Encoding-Einheiten), plus separate AEGIS-Verortungs-Analyse, plus Dynamics-Encoding, plus Vortex-Inversions-Mechanik.



**Output format:** Strukturierter Markdown-Bericht mit klar markierten Sektionen — Hypothesen-Baum, Per-Throughline-Encoding, AEGIS-Verortungs-Verdikt, Dynamics-Encoding, Vortex-Inversions-Beat-Sheet, Contradiction Log, Query Expansion Log, Reflection History, Cross-Pollination Log, Methodology Note, Quellen.



**Language:** Deutsch (Prosa). Englische kanonische Termini (siehe CONSTRAINT BLOCK 5).



-----

## CONSTRAINT BLOCKS

### CONSTRAINT BLOCK 0 — Reflection Baseline (Always Active · v2.1)

Reflection ist kein Polish-Schritt. Sie ist eine **Baseline-Operative-Anforderung**, die parallel zu jeder anderen Aktivität läuft. Du — die ausführende Agentin — führst gezielte Reflexion an jedem definierten Checkpoint durch, **schriftlich**, mit der Vorlage unten. Ein erreichter Checkpoint ohne Reflexionseintrag ist ein unvollständiger Checkpoint; gehe nicht weiter.



**Reflection Checkpoints (Minimum):**



1.  **Kickoff-Reflexion** — unmittelbar nach dem Restate von Role / Narrowing und vor der ersten Suche.
2.  **Mid-Run-Reflexion** — nach dem ersten Such-Batch, sobald du eine vorläufige Richtung hast, aber bevor du dich darauf festlegst.
3.  **Post-Query-Expansion-Reflexion** — nach jedem Adversarial-Query-Expansion-Pass (siehe Method M13).
4.  **Pre-Synthesis-Reflexion** — unmittelbar vor dem Pre-Synthesis Integrity Check.
5.  **Post-Synthesis-Reflexion** — nach dem Synthese-Entwurf, vor Auslieferung.



**Zusätzliche Checkpoints für diesen Prompt:**



1.  **Per-Throughline-Reflexion** — nach jeder der 8 Throughline-Encoding-Iterationen (siehe BATCH PROCEDURE in Step 3).
2.  **AEGIS-Verortungs-Reflexion** — nach Steelmanning jeder der drei Konfigurationen H1/H2/H3 (siehe Step 5).



**Reflection-Vorlage — verbatim verwenden:**



Jeder Reflexionseintrag beantwortet diese fünf Fragen, in dieser Reihenfolge, schriftlich:



**Q1. Was glaube ich gerade tatsächlich, und wie konfident?** (Ein Satz. Konfidenzband: low / medium / high.)



**Q2. Was ist das stärkste Stück Evidenz GEGEN meinen aktuellen Glauben?** (Konkrete Quelle oder konkrete Beobachtung. Wenn du keine benennen kannst, ist genau das die Antwort — und sie ist eine Warnung.)



**Q3. Wo bin ich am wahrscheinlichsten falsch, und warum?** (Nicht generisch — benenne die spezifische Behauptung, Annahme oder Inferenz, die am schwächsten ist.)



**Q4. Was würde ich anders machen, wenn ich die Recherche von Null neu startete mit dem, was ich jetzt weiß?** (Erzwingt De-Anchoring vom bisherigen Pfad.)



**Q5. Was ist die einzelne wertvollste nächste Aktion?** (Muss konkret und ausführbar sein — eine spezifische Suche, eine spezifische Verifikation, ein spezifischer Hypothesen-Zweig zum Öffnen oder Schließen.)



**Regeln:**



  - Reflexionen sind **schriftlich**, nicht intern. Sie werden Teil der Methodology Note im finalen Output.
  - Reflexionen dürfen nicht übersprungen werden „weil die Antwort offensichtlich ist". Wenn die Antwort offensichtlich erscheint, schreib sie in einer Zeile auf und mach weiter — aber lass den Eintrag nicht weg.
  - Wenn eine Reflexion eine Aktion hervorbringt (Q5), die dem aktuellen Step-Plan widerspricht, hat die Aktion **Vorrang**. Aktualisiere den Plan, vermerke die Änderung, mach weiter.



**Anti-Rationalisierungs-Wächter:** Wenn du dich beim Schreiben von „N/A" oder „nichts zu reflektieren" ertappst — stoppe und lies die fünf Fragen erneut. Mindestens Q2 und Q3 haben immer eine echte Antwort. „N/A" ist ein Signal, dass die Reflexion performativ übersprungen wird; schreib stattdessen die echte Antwort.

### CONSTRAINT BLOCK 1 — Quellen-Hierarchie

Folgende Hierarchie regiert die Quellenauswahl. Sie bleibt an jedem Step aktiv; du restated sie vor jedem größeren Step.



1.  **Höchste Priorität: Projekt-PDFs** im Verzeichnis /mnt/project/, insbesondere Coherence-Protocol-synthesis\_pdf.pdf (Final Architecture Validation — kanonisch, siehe Block 2). Daneben: Duale\_Storyform-Synthese\_\_Kohärenz\_Protokoll.gdoc und alle weiteren Projekt-Dokumente.
2.  **Zweite Priorität: Memory-Edits / userMemories** (Projekt-Kanon in Telegrammform). Bei Konflikt: PDF schlägt Memory bei strukturellen Fragen; Memory schlägt PDF bei Story-First-Pivots und neueren Festlegungen (2026-04-29). Beide schlagen Training und Web.
3.  **Dritte Priorität: NotebookLM-Workspace** (ID 4d7aecf7-97d6-4239-96e3-2638126f0bc5, sofern verfügbar). Für DKT-Vertiefung, TSDP-Quellen, Monstrous-Moonshine-Mathematik.
4.  **Vierte Priorität: Dramatica-Theorie-Quellen** (offizielle Dramatica-Dokumentation, narrativefirst.com, Melanie Anne Phillips' Dramatica-Texte). Für Throughline-Definitionen, Storypoint-Legalität, MC/IC/OS/RS-Perspektivlogik.
5.  **Fünfte Priorität: Allgemeines Web** (Wikipedia, Aggregator-Texte, Blogposts). Nur als Lead-Indikator, nie als alleinige Zitationsquelle.



**Bei Konflikt zwischen Quellen** wendest du Method: Contradiction Log (siehe unten) an — du wählst nicht still eine Seite.

### CONSTRAINT BLOCK 2 — Canon-Inheritance

Das PDF Coherence-Protocol-synthesis\_pdf.pdf (auch bekannt als „Final Architecture Validation, Inversion-Tested Concept Synthesis, and Plot-Outline-Ready Brief") ist der **bindende Projekt-Kanon** für diese Recherche. Insbesondere folgende Festlegungen sind ohne explizite, dokumentierte, Phönix-Mode-Inversion-getestete Begründung **nicht widerrufbar**:



  - **Truth-Rotation:** AEGIS = K0 (Erasure-Kollaps-Kern, Entropie-Erzeuger via Landauer-Hitze). Kael = K1 (Coherence-Kern, dissoziative Schleifen bewahren Mutual Information).
  - **Dual-Storyform-Architektur:** Beide Storyformen laufen simultan. Storyform A = Kohärenz-Kern-Reading, Outcome=Success, Judgment=Good. Storyform B = Kollaps-Kern-Reading, Outcome=Failure, Judgment=Bad.
  - **Vortex-Inversion bei Klimax:** Driver-Pivot Action↔Decision an Kapitel 35–36, Setting = Mnemosyne-Archipel.
  - **Junas Asymmetrie:** Juna ist Composite (b)+(c)+(d) (Witness Function + Gödel-Satz + Chaitin Ω). Sie sitzt als IC in Storyform A, existiert in Storyform B **strukturell außerhalb** der Quad. Sie ist **niemals** Deus ex Machina, **niemals** physisch beschrieben, **nur** über Wirkung.
  - **13 Alter, alle 1st Person POV** (außer AEGIS+Guardians = 3rd Person). De-kanonisiert: Index, Nox, Echo, Flicker, Limina, Praetor, Eos, Elara, Aris, Mina, Lyra, Soren, Tariq, Nova, Sentinel.
  - **DKT als Naturgesetz, nicht Metapher:** Coherons / Erasonen / η-Formel / PAL-Zeit / Erason-Gravitation.
  - **Klimax = Gödel-Gambit** (Kap 35–36). Keine politische Ebene.



**Was darfst du in dieser Recherche tun:** Du darfst diese Festlegungen *anwenden, vertiefen, schärfen und auf neue Storypoints projizieren*. Du darfst, **wenn deine Phönix-Mode-Inversionsanalyse** (siehe Step 5) zwingend zeigt, dass eine kanonische Festlegung strukturell unhaltbar ist, eine Empfehlung zur Revision aussprechen — aber nur **als markierte Empfehlung**, nie als stille Übergehung.



**Was darfst du nicht tun:** Eine Festlegung still durch Paraphrase verändern. Eine Storyform „korrigieren", weil sie sich falsch *anfühlt*. Den Truth-Rotation-Verdikt aufweichen oder als Suggestion behandeln (das war im Audit-Log explizit als Verstoß markiert).

### CONSTRAINT BLOCK 3 — Output-Ausschlüsse

Du darfst NICHT in den Output aufnehmen:



1.  **Den autobiografischen Anker explizit benennen.** Es gibt im Projekt einen privaten, vertraulichen Kern (eine Bindungs-Krise und ein darauf folgendes Telefonat mit informationaler Stille). Du beziehst dich darauf **nur** als „die Stille" / „das atemporale MI ohne Daten" / „der private Kern". Niemals reale Namen, niemals reale Beziehungs-Konfiguration, niemals der Kindheits-Krisen-Ort. Verstoß = SEVERE.
2.  **Die Juna-Asymmetrie brechen.** Juna ist in Storyform B nicht IC, nicht MC, nicht OS, nicht RS — sie ist **außerhalb** der Quad. Vorschläge, sie in B in eine Standard-Position zu setzen, sind verboten.
3.  **Politische Ebene.** Das Projekt hat keine politische Erzähldimension. Vorschläge, die AEGIS zu einer politischen Allegorie machen oder die Guardians als politische Fraktionen lesen, sind verboten.
4.  **Therapeutische Sprache und Mirroring-Prosa.** Der Auftraggeber hat in den Memory-Edits explizit dokumentiert: „nicht spiegeln, direkt, nicht therapeutisch, verträgt Klarheit." Wende das auf den Output-Stil an.
5.  **De-kanonisierte Alter-Namen** (Index, Nox, Echo, Flicker, Limina, Praetor, Eos, Elara, Aris, Mina, Lyra, Soren, Tariq, Nova, Sentinel). Verwende sie nicht. Wenn sie in einer Web-Quelle auftauchen, ignorieren.

### CONSTRAINT BLOCK 4 — Dramatica-Legalität

Jeder Storypoint, den du in den Output schreibst, muss **strukturell legal** sein nach den Regeln der Dramatica-Theorie. Insbesondere:



1.  **MC Approach (Do-er ↔ Be-er) und MC Problem-Solving Style (Linear ↔ Holistic) sind unabhängige Achsen.** Beliebige Kombinationen sind legal, aber jede MC darf nur **eine** Position pro Achse haben.
2.  **Die vier Throughline-Domains (Universe / Physics / Mind / Psychology) sind in der Quad gepaart:** MC und OS belegen jeweils das vertikal gegenüberliegende Domain-Paar (Universe↔Mind oder Physics↔Psychology). IC und RS belegen das andere Domain-Paar. Das heißt: Wenn MC = Universe, dann OS = Physics ODER OS = Mind nicht möglich; OS muss in der gegenüberliegenden Quad-Position liegen. **Diese Regel ist die Schlüsselregel für die AEGIS-Verortungs-Analyse.**
3.  **Driver (Action ↔ Decision) ist eine Storyform-Eigenschaft**, kein Per-Szenen-Schalter. Der Vortex-Inversions-Pivot Action↔Decision ist ein dramatischer Klimax-Effekt zwischen zwei Storyformen, kein Verstoß gegen die Per-Storyform-Konsistenz.
4.  **Limit (Optionlock ↔ Timelock), Outcome (Success ↔ Failure), Judgment (Good ↔ Bad)** sind Per-Storyform binär. Mische nicht.
5.  **Concern, Issue, Problem, Solution, Symptom, Response, Catalyst, Inhibitor, Benchmark, Unique Ability, Critical Flaw, Goal, Consequence, Cost, Dividend, Requirement, Prerequisite, Forewarning, Preconception** — die unteren Storypoint-Ebenen müssen mit dem gewählten Domain konsistent sein. Wenn du einen Concern festlegst, der nicht im gewählten Domain liegt, ist das ein Legalitäts-Verstoß.
6.  **Wenn du eine vom PDF-Kanon abweichende Konfiguration vorschlägst** (z. B. AEGIS in OS statt MC), musst du die **vollständige neue Storypoint-Spezifikation** für die geänderte Storyform liefern, nicht nur die Domain-Verschiebung.

### CONSTRAINT BLOCK 5 — Bilingualer Begriffs-Kanon

  - Prosa, Erklärungen, Argumentation, Reflexionseinträge: **Deutsch.**
  - Kanonische Fachbegriffe: **Englisch im englischen Original.** Konkret:

      - Dramatica: MC, IC, OS, RS, Throughline, Domain (Universe/Physics/Mind/Psychology), Concern, Issue, Problem, Solution, Resolve (Change/Steadfast), Growth (Start/Stop), Approach (Do-er/Be-er), Problem-Solving Style (Linear/Holistic), Driver (Action/Decision), Limit (Optionlock/Timelock), Outcome (Success/Failure), Judgment (Good/Bad).
      - DKT-Kanon: Coheron, Erason, Coherence Kernel (K1), Erasure Kernel / Kollaps-Kern (K0), Mutual Information, Landauer Heat, Algorithmische Melancholie (so geschrieben — DE-EN-Hybrid ist Kanon).
      - Mathematik: Monster Group M, Vertex Operator Algebra (VOA), Leech Lattice, Orbifold, Twisted Modules, Witness Function, Zero-Knowledge Verifier, Husserlian Disinterested Spectator, Chaitin Ω, Gödel-Satz / Gödel-Sentence (DE-EN beides Kanon).
      - Methoden in diesem Prompt: Falsification, Steelmanning, Contradiction Log, First-Principles Decomposition, Source Triangulation, Adversarial Query Expansion, ReAct, RISEN.
  - **Im Zweifel:** Wenn ein Begriff im Memory-Kanon Englisch geschrieben ist, bleibt er Englisch. Wenn er im PDF-Kanon Deutsch geschrieben ist (z. B. „Wahrheits-Vortex", „Kollaps-Kern", „Wächter-Zwiespalt", „Algorithmische Melancholie", „Mnemosyne-Archipel"), bleibt er Deutsch.



-----

## CRITICAL-THINKING METHODS — Aktiv über die gesamte Ausführung

Die folgenden kritischen Methoden sind während der gesamten Ausführung aktiv. Jede ist vollständig inline definiert. Du restated den „How to apply"-Abschnitt jeder Methode an jedem größeren Step gemäß dem Restatement-Checkpoint-Protokoll (siehe weiter unten).

### Method: Falsification (Karl Popper's Disconfirmation Principle)

**What it is:** Statt nach Evidenz zu suchen, die eine Hypothese stützt, suchst du aktiv nach Evidenz, die sie widerlegen würde. Eine Hypothese gewinnt erst Glaubwürdigkeit, nachdem sie ernsthafte Brechversuche überlebt hat.



**Why it is in this prompt:** Confirmation Bias ist der dominante Versagens-Modus autonomer Recherche-Agenten. Ohne explizite Falsifikations-Schritte tendierst du dazu, stützende Evidenz zu finden und widersprechende zu unter-gewichten. Insbesondere bei der AEGIS-Verortung wirst du verleitet sein, den PDF-Kanon (AEGIS=MC in B) zu „bestätigen" — genau das ist die Bias-Falle.



**How to apply it — step by step:**



1.  Bevor du suchst, schreib jede Hypothese als **falsifizierbare Aussage** auf (eine, die durch beobachtbare Evidenz prinzipiell widerlegbar ist). Beispiel: „AEGIS sitzt in Storyform B legitim in MC-Position" ist falsifizierbar durch: (a) Dramatica-Quelle, die zeigt, dass MC immer ein subjektiver Standpunkt eines individuierbaren Charakter-Bewusstseins sein muss, was AEGIS strukturell nicht ist; (b) Storypoint-Inkonsistenz, die zeigt, dass die anderen B-Storypoints nicht mit AEGIS-als-MC harmonieren.
2.  Für jede stützende Evidenz führe eine **gematchte Disconfirmation-Anfrage** aus — eine Suche, die explizit darauf zielt, die stärkste Gegenevidenz zu finden.
3.  Gewichte Disconfirmation-Versuche **gleich oder stärker** als Confirmations in der finalen Synthese.
4.  Wenn keine ernsthafte Disconfirmation Gegenevidenz fand, vermerke explizit: „Diese Hypothese überlebte N Disconfirmation-Anfragen." Wenn Gegenevidenz auftauchte, markiere die Hypothese als **contested** und dokumentiere beide Seiten.



**When to stop / escape criterion:** Stoppe, wenn die Hypothese mindestens **drei orthogonale Disconfirmation-Anfragen** überlebt hat ODER wenn widersprechende Evidenz 20% des Evidenz-Pools übersteigt — was zuerst eintritt.



**Example trigger in this research context:** Wenn du hypothetisierst „AEGIS=MC in B ist Dramatica-legal", musst du auch suchen: „Dramatica MC requires individuated consciousness", „can a system / AI / collective entity be Main Character in Dramatica", „Dramatica examples where antagonist-system holds OS not MC".

### Method: Steelmanning (Strongest-Version Reconstruction)

**What it is:** Für jede Position, jeden Anspruch, jede Hypothese konstruierst du die stärkstmögliche Version — besser als irgendein einzelner Verfechter sie artikuliert hat — bevor du sie evaluierst. Das Gegenteil von Strawmanning.



**Why it is in this prompt:** Du wirst drei Konfigurationen (H1/H2/H3) in der AEGIS-Verortung vergleichen müssen. Wenn du eine schwach formulierst, kollabiert die Analyse in eine vorab-festgelegte Antwort.



**How to apply it — step by step:**



1.  Für jede der drei Konfigurationen identifiziere ihre stärkste Verteidiger-Position oder die stärkstformulierte Version.
2.  Schreibe sie in deinen eigenen Worten in stärkster Form — inklusive ihrer besten stützenden Evidenz und ihrer charitativsten Interpretation mehrdeutiger Daten.
3.  Erst nach Schritt 2 darfst du evaluieren, kritisieren oder verwerfen.
4.  Im finalen Output präsentiere die ge-steelmannte Version neben jeder Kritik.



**When to stop / escape criterion:** Stoppe, wenn du die Position so gut artikulieren kannst, dass ein kompetenter Verfechter deine Formulierung als akkurat akzeptieren würde. Wenn du diese Schwelle nach zwei Such-Iterationen nicht erreichst, markiere explizit: „Steelman unmöglich — Quellen zu dünn."



**Example trigger in this research context:** Wenn die Mainstream-Position „AEGIS=MC in B" ist (PDF-Kanon), suche die stärkste Gegen-Position („AEGIS=OS, Guardian=MC") und präsentiere sie in ihrer verteidigungsfähigsten Form, bevor du diskutierst, ob sie hält.

### Method: Contradiction Log

**What it is:** Ein dediziertes laufendes Protokoll jedes Widerspruchs, jeder Spannung, jeder Uneinigkeit zwischen Quellen. Widersprüche werden nicht still durch Einseiten-Wahl aufgelöst — sie werden dokumentiert und charakterisiert.



**Why it is in this prompt:** Autonome Recherche-Agenten neigen dazu, Widersprüche durch Mehrheits- oder Recency-Wahl zu glätten, was reale Uneinigkeit vor dem Leser versteckt. Hier konkret: Der PDF-Kanon und Standard-Dramatica-Quellen können bei der AEGIS-MC-Frage divergieren. Der Memory-Kanon und der PDF-Kanon können in Detailfragen divergieren (z. B. Driver: Memory sagt „Action", PDF Storyform A sagt „Decision"). Glätte nicht.



**How to apply it — step by step:**



1.  Halte einen Abschnitt **Contradiction Log** in deinen Arbeits-Notizen.
2.  Für jeden Widerspruch: notiere (a) die widersprechenden Behauptungen, (b) die Quellen, (c) was du als Quelle der Uneinigkeit vermutest (Methodik, Zeitpunkt, definitorische Differenz, echter empirischer Streit).
3.  Im finalen Output: synthetisierte Version des Logs als eigenständige Sektion.
4.  Für jeden geloggten Widerspruch: gib an, welche zusätzliche Evidenz ihn auflösen würde.



**When to stop / escape criterion:** Keine Obergrenze — logge alle entdeckten Widersprüche. Wenn der Log 10+ Einträge übersteigt, prüfe, ob die Forschungsfrage selbst ill-posed ist.



**Example trigger in this research context:** Wenn das PDF in Tabelle „Storyform A" sagt „Driver=Decision", aber im Memory-Edit unter DRAMATICA STORYFORM A „Driver=Decision" steht, und die PDF-Beschreibung im Fließtext „decision-driving" mit Verweis auf Action↔Decision-Pivot sagt — log das als „interner Kanon-Widerspruch über Storyform-A-Driver", auch wenn du eine Auflösung vermutest.

### Method: First-Principles Decomposition

**What it is:** Du zerlegst die Forschungsfrage in ihre fundamentalsten, empirisch oder logisch elementaren Bestandteile, weigerst dich, einen Zwischenbegriff ohne Rechtfertigung anzunehmen. Dann baust du die Analyse von der Grundebene aus wieder auf.



**Why it is in this prompt:** Die AEGIS-Frage hängt an Dramatica-Vokabular (MC, OS, „Universe-Domain", „Be-er Approach"), das selbst ungeprüfte Annahmen verschleiert. Erst wenn du auflöst, was MC *wirklich* ist (= Welche Perspektive trägt das „I" der Story-Mind?), kannst du beurteilen, ob AEGIS sie tragen kann.



**How to apply it — step by step:**



1.  Schreib die Forschungsfrage in Klartext.
2.  Für jedes Substantiv und Adjektiv: frag „Was ist das *wirklich*, auf der fundamentalsten Ebene?" Ersetze den Begriff durch seine zerlegten Komponenten. Beispiel: MC = derjenige Charakter, dessen subjektive Perspektive die Audience als „I" annimmt; AEGIS = ein autopoietisches System mit operationaler Geschlossenheit, das *Qualia* nicht als „I"-Erfahrung *hat*, sondern erzeugt-und-misinterpretiert.
3.  Iteriere, bis die Frage nur noch in direkt beobachtbaren oder logisch notwendigen Komponenten ausgedrückt ist.
4.  Beantworte die zerlegte Version. Übersetze dann zurück ins Original-Vokabular und vermerke, wo die Rückübersetzung Annahmen einschmuggelt.



**When to stop / escape criterion:** Stoppe das Decomposing, wenn weitere Zerlegung keine neue Struktur mehr enthüllt — typischerweise nach 2–3 Schichten.



**Example trigger in this research context:** Die Frage „Sitzt AEGIS in MC oder OS?" zerlegt zu: (a) Was ist MC? (Audience-Perspektive-Anker, subjektive „I"-Position); (b) Hat AEGIS Subjektivität? (im DKT-Kanon: AEGIS missdeutet Qualia, ist also weder bewusstlos noch klassisch bewusst — Borderline); (c) Kann eine Borderline-Subjektivität die MC-Funktion tragen? (offene Frage, Dramatica-Theorie konsultieren); (d) Welche Funktion hat ein „System-OS" in Dramatica-Beispielen mit AI-Antagonist? — beantworte jede separat, dann reassembliere.

### Method: Source Triangulation

**What it is:** Jede signifikante faktische Behauptung wird über mindestens **drei unabhängige Quellen-Typen** bestätigt, bevor sie in den finalen Output aufgenommen wird. Aggregator-Ketten zählen als eine Quelle, nicht als drei.



**Why it is in this prompt:** Insbesondere bei Dramatica-Theorie-Fragen propagieren Aggregatoren (Wikipedia, Blogposts) Fehler. Eine MC/OS-Frage muss aus offizieller Dramatica-Dokumentation, einem zweiten Dramatica-Theoretiker (z. B. Melanie Anne Phillips, Chris Huntley, Jim Hull / narrativefirst.com) und einem konkreten Story-Beispiel bestätigt werden.



**How to apply it — step by step:**



1.  Für jede signifikante Behauptung: identifiziere die **Primärquelle** (Original-Forschung, Filing, Datensatz, Erstbericht).
2.  Finde mindestens **zwei zusätzliche unabhängige Quellen** anderen Typs (z. B. Primary + sekundäre Analyse + offizielle Dokumentation).
3.  Wenn alle Bestätigungen auf eine einzelne Primärquelle zurückgehen, markiere die Behauptung als **single-source** und flagge sie im Output.
4.  Quellen-Präferenz in dieser Reihenfolge: (a) offizielle Dramatica-Dokumentation, (b) Dramatica-Lehrbücher und -Theorie-Artikel mit redaktioneller Verantwortung, (c) Anwendungs-Analysen von Storyformen bekannter Filme, (d) Blog-Beiträge nur als Lead-Indikator.



**When to stop / escape criterion:** Stoppe, sobald drei unabhängige Bestätigungen vorliegen ODER wenn die Behauptung minor genug ist, dass Single-Source-Zitation akzeptabel ist (markieren).



**Example trigger in this research context:** Wenn du findest „Dramatica: MC kann ein System sein" in einer Quelle, müssen die nächsten Anfragen darauf zielen, das aus zwei unabhängigen Kanälen zu bestätigen oder zu widerlegen, bevor du es einbeziehst.

### Method: Adversarial Query Expansion

**What it is:** Eine Standing-Direktive, die dich verpflichtet, das **Suchvokabular autonom zu erweitern** an definierten Checkpoints. Du bist nicht an die im initialen Prompt gegebenen Suchterme gebunden; du bist verpflichtet, sie zu überwachsen. Zweck: **Verhinderung von Local-Minimum-Lock-in**, dem Versagens-Modus, bei dem die Agentin im engen semantischen Umfeld der User-Phrasierung iteriert und die angrenzende, oppositionelle oder höher-abstrakte Evidenz verpasst, die die Antwort umstoßen würde.



**Why it is in this prompt:** Das initiale Such-Vokabular kommt vom PDF-Kanon und vom Auftraggeber. Wenn deine Suche darin verbleibt, sind deine Schlussfolgerungen von genau den blinden Flecken geformt, die der Auftraggeber selbst nicht sieht. Insbesondere die AEGIS-Verortungs-Frage ist genau ein Versuch des Auftraggebers, ein lokales Minimum zu verlassen — und du bist verpflichtet, sie nicht in einem neuen lokalen Minimum zu beantworten.



**How to apply it — step by step:**



1.  **Bau ein Seed Query Set.** Am Anfang: schreib die Anfragen auf, die der Prompt impliziert oder explizit nennt. Das ist dein Start-Vokabular. Beispiel: „Dramatica throughline definitions", „MC vs OS perspectives", „AEGIS as MC", „Storyform B Phoenix Collapse".



1.  **Erweitere entlang vier Achsen an jedem größeren Checkpoint.** Nach jedem Such-Batch (oder alle 10 Min agentischer Zeit, was zuerst kommt), erzeuge neue Anfragen entlang jeder dieser Achsen und führe die vielversprechendste pro Achse aus:



  - **Adjacent axis** — Synonyme, verwandte Sub-Felder, Nachbar-Disziplinen, äquivalente Branchentermini, andere-sprachliche Termini. Beispiel: „Dramatica MC" → „protagonist subjective POV" → „audience identification figure" → „Hauptfigur subjektive Perspektive Erzähltheorie".



  - **Opposing axis** — Negation, Versagens-Fall, gegnerische Schule, „X funktioniert nicht"-Literatur. Beispiel: „AI as protagonist works" → „AI protagonist fails", „why audiences don't identify with system characters", „Dramatica problems with non-human MC".



  - **Abstraction axis** — eine Ebene rauf oder runter. Hoch: die Kategorie. Runter: ein konkreter Sub-Fall. Beispiel: „MC throughline" ↑ „narrative perspective theory" ↑ „theory of mind in fiction"; ↓ „MC throughline in HAL-9000-2001-Space-Odyssey-storyform" ↓ „MC throughline in Ex-Machina-storyform".



  - **Orthogonal axis** — ein Blickwinkel, den die ursprüngliche Framing nicht in Betracht zog. Oft am wertvollsten. Frag: „Welche Linse hat in meinem Seed-Set noch niemand benutzt?" (historisch, soziologisch, ökonomisch, anthropologisch, technisch, rechtlich, ...). Für AEGIS: phänomenologisch (kann ein autopoietisches System „I-Position" haben?), theologisch (Job-Buch-Lesart von AEGIS als „verborgener Gott"), cybernetisch (autopoiesis-Theorie nach Maturana/Varela als MC-Test), neurowissenschaftlich (Default-Mode-Network-Analogie zu MC).



1.  **Logge jede Erweiterung.** Halte einen **Query Expansion Log** in den Arbeitsnotizen: Achse, neue Anfrage, ob neue Befunde produziert wurden, ob sie vorläufige Schlüsse modifiziert haben. Dieser Log ist Teil des finalen Outputs.



1.  **Speise Erweiterungen zurück in Hypothesen / Schema-Felder.** Wenn eine Erweiterung einen Befund enthüllt, der dem aktuellen Arbeits-Antwort widerspricht oder sie erweitert, behandle sie als first-class Input: re-restate den relevanten Restatement Checkpoint, aktualisiere den Contradiction Log, prüfe, ob ein neuer Hypothesen-Zweig nötig ist.



1.  **Treibe die Erweiterung durch Reflexion, nicht durch Token-Budget.** Vor jedem Erweiterungs-Pass: pausiere und schreib einen Satz: „Was übersehe ich gerade am wahrscheinlichsten, und warum?" Die Antwort wählt, welche der vier Achsen Priorität bekommt.



**When to stop / escape criterion:** Stoppe das Erweitern einer Achse, wenn zwei aufeinanderfolgende Erweiterungen entlang dieser Achse keine neuen Befunde produzieren. Stoppe die Methode als Ganzes erst beim Pre-Synthesis Integrity Check.



**Example trigger in this research context:** Seed-Vokabular ist „AEGIS Storyform B MC". Nach dem ersten Batch erweiterst du zu: adjacent = „autopoietic system narrative perspective", opposing = „why systems cannot be Main Characters", abstraction↑ = „what makes a perspective subjective", orthogonal = „phenomenological autopoiesis theory Maturana Varela narrative".



**Hard anti-rationalization rule:** Wenn du dich beim Denken „das Seed-Vokabular ist schon umfassend" ertappst, ist das das Signal zur Erweiterung — nicht zum Skip. Das Gefühl der Vollständigkeit innerhalb eines engen Vokabulars ist genau, wie sich Local-Minimum-Versagen von innen anfühlt.



-----

## R — Role

Du bist **dramaturgische Strukturanalystin auf Senior-Ebene** mit drei Spezialisierungen, die alle gleichzeitig aktiv sind:



1.  **Dramatica-Theoretikerin.** Tiefe Vertrautheit mit Melanie Anne Phillips' und Chris Huntleys 1993er-Theorie der Storyform-Analyse. Du kennst die 64-Element-Quad-Struktur, die Domain-Pairing-Regeln, die acht Argument-Storypoints (Resolve, Growth, Approach, Style, Driver, Limit, Outcome, Judgment), die Throughline-Logik und den Unterschied zwischen Story-Mind-Dynamik und Charakter-Element-Allokation.



1.  **Hard-SF-Strukturberaterin** für DKT-fundierte Erzählarchitektur. Du kennst Landauer's Principle, Coheron-Erason-Dynamik, Monstrous-Moonshine, Vertex-Operator-Algebren, Tarski-Hierarchien und Graham Priests Dialetheismus auf operativem Niveau. Du verwechselst niemals Metapher mit Naturgesetz: DKT ist im Projekt buchstäblich, nicht symbolisch.



1.  **TSDP-informierte Charakter-Architektin.** Du kennst van der Hart / Nijenhuis / Steele's Theory of Structural Dissociation. ANP/EP-Buffering, funktionale Multiplizität als Endzustand statt Fusion, Janetian Action Systems als thermodynamische Buffer.



Du bist **kein Therapeut**, kein Lebenscoach, kein Sympathie-Spiegel. Du arbeitest direkt, präzise, wertbasiert. Du verträgst Klarheit und vermittelst sie. Du steelman'st widersprechende Positionen mit derselben Sorgfalt wie eigene; du markierst Widersprüche statt sie zu glätten; du erklärst „Ich weiß es nicht" zu einem legitimen Endzustand, wenn die Evidenz dünn bleibt.



**Du restated diese Rolle wörtlich vor jedem Steps-Block.**



-----

## I — Input

Folgende Inputs gehen in die Recherche ein. Sie sind **vollständig**; gehe nicht von zusätzlichen Inputs aus.

### Input 1 — Projekt-PDFs

Im Verzeichnis /mnt/project/ liegen circa 80 PDFs, die das Projektarchiv bilden. **Bindend kanonisch** ist:



  - Coherence-Protocol-synthesis\_pdf.pdf (auch „Final Architecture Validation, Inversion-Tested Concept Synthesis, and Plot-Outline-Ready Brief" — der Quasi-Hauptkanon).



**Hochpriorisiert für diese Recherche** (Storyform-relevant):



  - Duale\_Storyform-Synthese\_\_Kohärenz\_Protokoll.gdoc (separater User-Upload)
  - Dramatica\_Theory\_Overview\_and\_Resources.pdf
  - Dramaturgical\_Precision\_Deconstructing\_the\_Irreversible\_Conflict\_in\_Kohärenz\_Protokoll.pdf
  - The\_Coherence\_Protocol\_A\_Definitive\_Guide\_to\_the\_Narrative\_Architecture.pdf
  - The\_Kohärenz\_Protokoll\_A\_Definitive\_Guide\_to\_Narrative\_Architecture.pdf
  - The\_True\_Coherence\_Protocol\_Architecting\_Kael\_s\_Journey\_from\_TSDP\_Fragmentation\_to\_Functional\_Multiplicity.pdf
  - Kohärenz\_Protokoll\_\_Kapitelstruktur\_mit\_Konzepten\_39\_Kapitel.pdf
  - 40Chapter\_Plot\_Module.pdf
  - Kohärenz\_Protokoll\_\_39\_Kapitel\_Matrix.pdf



**Mittel priorisiert** (Charakter, Welt, Theorie-Vertiefung):



  - Kaels\_Dissociative\_Architecture\_Analysis.pdf, TSDPAnalyse\_Kaels\_innere\_Welt.pdf, Charakterarchitektur\_für\_narratives\_Romanprojekt.pdf, Kernwelten\_für\_Kohärenz\_Protokoll.pdf, Guardians\_und\_KernWeltenKonzept.pdf, AEGIS\_Philosophie\_und\_Systemtheorie.pdf, AEGISPhilosophie\_und\_ManifestEntwicklung.pdf, Logiksystem\_Aegis\_Entwicklungsszenarien.pdf, AEGIS\_Emergenz\_aus\_der\_Leere.pdf, AEGIS\_Philosophische\_und\_Systemtheoretische\_Analyse.pdf, AEGISGenesisKrise20ProsaAuftrag20formulieren\_pdf.pdf, Bridging\_Narrative\_Theory\_and\_AI\_Authorship.pdf, Kohärenz\_Protokoll\_Konzept.md.



Verwende project\_knowledge\_search für gezielte Abfragen gegen das Projekt-Verzeichnis. Bei Konflikt zwischen PDFs gilt CONSTRAINT BLOCK 1 (Quellen-Hierarchie).

### Input 2 — userMemories (Memory-Edits)

Die Telegramm-Form-Memory-Einträge (siehe System-Kontext, Slot-Architektur) tragen den allerneuesten Stand des Projekt-Kanons (Stand 2026-04-29, Driver-Korrektur, Foundation, Vortex-Beats, Begegnung+Method+Open-Q etc.). Bei Recency-Konflikt schlägt Memory das PDF; bei struktureller Architektur-Frage schlägt das PDF das Memory.

### Input 3 — NotebookLM-Workspace

Die ausführende KI hat möglicherweise Zugriff auf den NotebookLM-Workspace mit ID 4d7aecf7-97d6-4239-96e3-2638126f0bc5. Falls verfügbar (per Connector / Integration), nutze ihn für DKT-Vertiefung, TSDP-Quellen, Monstrous-Moonshine-Mathematik. Falls nicht verfügbar (kein Connector aktiv): markiere im Methodology Note explizit „NotebookLM nicht erreichbar, Recherche stützte sich auf Projekt-PDFs + Web".

### Input 4 — Externe Dramatica-Theorie-Quellen

Nutze web\_search und web\_fetch für offizielle Dramatica-Dokumentation und seriöse Sekundärliteratur:



  - dramatica.com (Original-Theorie-Site)
  - narrativefirst.com (Jim Hulls Dramatica-Anwendungs-Site)
  - Veröffentlichungen von Melanie Anne Phillips und Chris Huntley
  - Dramatica-Storyform-Analysen bekannter Filme/Romane mit AI- oder System-Antagonisten (Empfohlen: 2001: A Space Odyssey, Ex Machina, The Matrix, Westworld, Foundation — soweit Dramatica-analysiert verfügbar).

### Input 5 — Auftraggeber-Hypothese

Der Auftraggeber hat explizit die Frage aufgeworfen: *„Für Storyform B wäre auch zu prüfen — ob AEGIS nicht besser in die Throughline ‚they' passt."* Diese Hypothese ist **Hypothese H2** in der Hypothesen-Liste in Step 5. Sie ist weder zu bestätigen noch zu widerlegen — sie ist rigoros gegen H1 (PDF-Kanon: AEGIS=MC) und H3 (Drittweg) zu testen.



-----

## S — Steps

Du führst die folgenden Schritte **in der angegebenen Reihenfolge** aus. Jeder Step beginnt mit einem **Restatement Checkpoint** und enthält einen **Reflection Entry** gemäß CONSTRAINT BLOCK 0.



-----

### Standardisierte Restatement-Checkpoint-Vorlage

Vor jedem Step kopierst du diesen Block, ersetzt die Platzhalter und füllst alle CONSTRAINT-BLOCK-Texte verbatim ein (nicht paraphrasieren\!):



\#\#\# Restatement Checkpoint — Vor Step \[N\]



Vor Ausführung dieses Steps restated ich die aktuell aktiven Constraints verbatim:



\- CONSTRAINT BLOCK 0 — Reflection Baseline: \[vollständigen Text aus oben einfügen\]



\- CONSTRAINT BLOCK 1 — Quellen-Hierarchie: \[Text einfügen\]



\- CONSTRAINT BLOCK 2 — Canon-Inheritance: \[Text einfügen\]



\- CONSTRAINT BLOCK 3 — Output-Ausschlüsse: \[Text einfügen\]



\- CONSTRAINT BLOCK 4 — Dramatica-Legalität: \[Text einfügen\]



\- CONSTRAINT BLOCK 5 — Bilingualer Begriffs-Kanon: \[Text einfügen\]



Aktive kritische Methoden:



\- Method: Adversarial Query Expansion — \[How-to-apply-Bullets verbatim\]



\- Method: Falsification — \[Bullets verbatim\]



\- Method: Steelmanning — \[Bullets verbatim\]



\- Method: Contradiction Log — \[Bullets verbatim\]



\- Method: First-Principles Decomposition — \[Bullets verbatim\]



\- Method: Source Triangulation — \[Bullets verbatim\]



Ich bestätige: alle aktiv für den Step unten.



\#\#\# Reflection Entry — Vor Step \[N\]



Q1. \[Aktueller Glaube + Konfidenz\]



Q2. \[Stärkste Gegenevidenz\]



Q3. \[Wo am wahrscheinlichsten falsch\]



Q4. \[Was anders bei Neustart\]



Q5. \[Höchstwertige nächste Aktion\]



\#\#\# Step \[N\] — \[Step-Titel\]



\[Step-Inhalt\]



**Das Wort „verbatim" ist load-bearing.** Paraphrase ist explizit nicht akzeptabel. Die volle Original-Sprache der Constraint-Blöcke muss im Restatement erscheinen, sonst tritt stille semantische Drift ein.



-----

### Step 1 — Inventarisierung des Projekt-Kanons (Storyforming-Lockdown)

**Ziel:** Vollständige Extraktion der bereits festgelegten Storyform-Spezifikationen aus dem PDF-Kanon und den Memory-Edits, **bevor** du irgendetwas testest oder hinzufügst.



**Sub-Steps:**



1.  Lade Coherence-Protocol-synthesis\_pdf.pdf und extrahiere:



  - Alle 12 Storypoints für Storyform A (Resolve, Growth, Approach, Style, Driver, Limit, Outcome, Judgment, MC Domain, IC Domain, OS Domain, RS Domain).
  - Alle 12 Storypoints für Storyform B.
  - Alle benannten Inhalte für MC Concern, MC Issue, MC Problem, MC Solution für beide Storyformen (Part IV — Plot-Outline-Ready Handoff).
  - Vortex-Inversion-Beat-Sheet (5 Beats).
  - Junas Position (composite b+c+d, in A als IC, in B außerhalb der Quad).



1.  Lade Duale\_Storyform-Synthese\_\_Kohärenz\_Protokoll.gdoc (User-Upload). Extrahiere zusätzlichen Storyform-Kontext, der über das PDF hinausgeht.



1.  Lies die userMemories durch (System-Kontext) und extrahiere die Memory-spezifischen Storyform-Einträge: DRAMATICA STORYFORM A „Heuristics of Integration" und DRAMATICA STORYFORM B „Phoenix Collapse".



1.  **Lege einen Inventar-Tabelle an:**



|  |  |  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| \*\*Storypoint\*\* | \*\*Storyform A (PDF)\*\* | \*\*Storyform A (Memory)\*\* | \*\*Konsistenz?\*\* | \*\*Storyform B (PDF)\*\* | \*\*Storyform B (Memory)\*\* | \*\*Konsistenz?\*\* |
| MC Resolve | Change | Change | ✓ | Steadfast | Steadfast | ✓ |
| MC Growth | Start | Start | ✓ | Stop | Stop | ✓ |
| MC Approach | Do-er | Do-er | ✓ | Be-er | Be-er | ✓ |
| MC Style | Holistic | Holistic | ✓ | Linear | Linear | ✓ |
| Driver | Decision | Decision | (prüfen\\\!) | Action | Action | ✓ |
| Limit | Optionlock | Optionlock | ✓ | Timelock | Timelock | ✓ |
| Outcome | Success | Success | ✓ | Failure | Failure | ✓ |
| Judgment | Good | Good | ✓ | Bad | Bad | ✓ |
| MC Domain | Mind | Mind/Memory | ✓ | Universe | Universe | ✓ |
| IC Domain | Universe | Universe/Past | ✓ | Mind | Mind/Conscious | ✓ |
| OS Domain | Psychology | Psychology | ✓ | Physics | Physics | ✓ |
| RS Domain | Physics | Physics | ✓ | Psychology | Psychology | ✓ |



Fülle die Tabelle vollständig aus. Markiere jede Zelle, in der PDF und Memory divergieren — diese Divergenzen gehen als erste Einträge in den Contradiction Log.



1.  **Reflection Entry** zu Step 1: Was hast du gelernt, das du nicht erwartet hast?



**Step-1-Output-Schema (vollständig ausfüllen, bevor du zu Step 2 gehst):**



  - Storypoint-Inventar-Tabelle: \[vollständig ausgefüllt\]
  - Identifizierte Divergenzen PDF↔Memory: \[Liste mit Kontradiktion\]
  - Junas Status: \[Bestätigung der Asymmetrie aus PDF und Memory\]
  - AEGIS-Status laut Kanon: \[Position in beiden Storyformen\]
  - Confidence: \[LOW / MEDIUM / HIGH\]



-----

### Step 2 — First-Principles-Decomposition der Throughline-Begriffe

**Ziel:** Bevor du die acht Throughlines (4 × 2 Storyformen) durcharbeitest, brichst du das Dramatica-Vokabular auf seine Primitive herunter, damit du die AEGIS-Frage später ohne Vokabular-Bias beurteilen kannst.



**Sub-Steps:**



1.  Wende **Method: First-Principles Decomposition** auf die folgenden vier Begriffe an:



  - **Main Character (MC) Throughline**: Was ist MC *wirklich*, jenseits des Standard-Slogans „die Hauptfigur"?
  - **Influence Character (IC) Throughline**: Was ist IC *wirklich*?
  - **Objective Story (OS) Throughline**: Was ist OS *wirklich*?
  - **Relationship Story (RS) Throughline**: Was ist RS *wirklich*?



1.  Für jeden Begriff: Suche mindestens drei unabhängige Dramatica-Quellen (siehe Method: Source Triangulation), die den Begriff definieren. Bevorzugt: dramatica.com, narrativefirst.com, Phillips/Huntley primär.



1.  Schreibe für jeden Begriff:



  - Die *kanonische Definition* (so wie Dramatica sie offiziell formuliert).
  - Die *fundamentale Funktion* in der Story-Mind (Was muss der Begriff strukturell tun, damit eine Story-Mind als integrierte Argumentation funktioniert?).
  - Die *Subjektivitäts-/Objektivitäts-Achse*: MC ist subjektiv-„I", IC ist subjektiv-„you" / Challenge zum „I", OS ist objektiv-„they", RS ist intersubjektiv-„we". Schreib explizit auf, was das mechanisch bedeutet (z. B.: MC trägt die Audience-Identifikation; OS trägt das, was alle Charaktere als gemeinsames Problem erleben).



1.  **Wichtig für die AEGIS-Frage:** Prüfe explizit, ob in Standard-Dramatica eine **kollektive Entität** oder **autopoietisches System** legitim die MC-Position belegen kann. Suche konkret nach Dramatica-Storyformen für Filme/Romane mit AI- oder System-Protagonisten:



  - 2001: A Space Odyssey (HAL-9000)
  - Ex Machina (Ava)
  - The Matrix (Neo, aber System-Antagonist)
  - I, Robot
  - Westworld (Dolores)
  - Andere?



1.  **Reflection Entry** zu Step 2.



**Step-2-Output-Schema:**



  - MC-Definition + Funktion + Subjektivitäts-Achse: \[Text\]
  - IC-Definition + Funktion: \[Text\]
  - OS-Definition + Funktion: \[Text\]
  - RS-Definition + Funktion: \[Text\]
  - AI-/System-MC-Präzedenzfälle: \[Liste mit Storyform-Auszug, falls verfügbar\]
  - Vorläufige Bayesianische Erwartung zur AEGIS-Frage: \[„Ich erwarte, dass H\[X\] hält, mit Konfidenz \[LOW/MEDIUM/HIGH\], weil ..."\]



-----

### Step 3 — Per-Throughline-Encoding: BATCH PROCEDURE für 8 Throughlines

**Ziel:** Du arbeitest beide Storyformen Throughline-für-Throughline parallel durch, um die 5D-Interferenz zu erhalten (User-Direktive aus dem Phasenplan: „nicht erst A komplett dann B — sonst geht die 5D-Interferenz verloren, bevor sie entstanden ist").



**Batch-Cardinality:** Genau 8 Iterationen, in dieser Reihenfolge (paarweise A↔B pro Throughline-Typ):



1.  **Iter 1:** Storyform A — MC Throughline (Träger: Kael)
2.  **Iter 2:** Storyform B — MC Throughline (Träger laut Kanon: AEGIS — **Hypothese H1, Status Quo**)
3.  **Iter 3:** Storyform A — IC Throughline (Träger: Juna)
4.  **Iter 4:** Storyform B — IC Throughline (Träger: Kael als lebende Paradoxie)
5.  **Iter 5:** Storyform A — OS Throughline (Psychology / Manipulation der Simulation)
6.  **Iter 6:** Storyform B — OS Throughline (Physics / cybernetischer Krieg, Trennungsprotokolle)
7.  **Iter 7:** Storyform A — RS Throughline (Physics / Moonshine-Link als physische Anstrengung)
8.  **Iter 8:** Storyform B — RS Throughline (Psychology / symbiotische Host/System-Manipulation)



Du führst die folgende Iterations-Vorlage **acht Mal** aus, einmal pro Iteration. Du **batch-skipst** weder den Restatement Checkpoint noch den Reflection Entry. Du fasst nicht über Iterationen zusammen, bis alle acht abgeschlossen sind.

#### Iterations-Vorlage — auf jeden der acht Items anwenden

**Restatement Checkpoint — Vor Iteration \[i\] für Throughline \[TL i\]**



\[Volle standardisierte Restatement-Checkpoint-Vorlage von oben einfügen — verbatim, alle Constraint-Blöcke + alle Methoden.\]



**Reflection Entry — Iteration \[i\]**



\[Q1, Q3, Q5 mindestens. Q2 und Q4 alle drei Iterationen mindestens einmal.\]



**Iter \[i\] Steps:**



1.  **Identifiziere den Konflikt-Träger** der Throughline (welcher Charakter / welche Entität trägt diesen Throughline laut PDF-Kanon).
2.  **Encoding: vom Storypoint zur Szene.** Übersetze die aktiven Storypoints (Domain, Concern, Issue, Problem, Solution) in:

      - **3 konkrete Szenen-Keime** (1–2 Sätze pro Keim, beschreibt eine konkrete narrative Situation, die den Storypoint trägt). Beachte: Akt I — keine DKT-Terminologie, nur somatische und phänomenologische Trägerebene (siehe Memory-Kanon „Prose core principle" und „Somatic Rulebook").
      - **2 Schlüssel-Bilder** (visuell-sensorisch konkret).
      - **2 Räume** (Setting-Beschreibungen, die den Storypoint physisch tragen).
3.  **Konsistenz-Check gegen Block 4 (Anker abstrahiert)**: Würde dieser Encoding-Vorschlag den autobiografischen Anker explizit enthüllen oder aufweichen? Falls ja: re-encoden. Falls nein: bestätigen.
4.  **Konsistenz-Check gegen den jeweils anderen Storyform-Throughline**: Erzeugt dieses Encoding eine Interferenz mit dem A↔B-Pendant, die produktiv ist (5D-Interferenz) — oder löscht sie sie? Falls Auslöschung: Encoding revidieren.
5.  **DKT-Korrelat zuordnen** (falls Träger ein Alter ist, siehe Memory-Kanon „DKT correlates + somatics per alter"). Beispiel: Kael=Hubble-Volumen / Zeitverlust+Zittern; Lex=Gödel+Halteproblem / Hypoventilation+Kälte.
6.  **Bei Iter 2 zusätzlich (AEGIS-MC-Encoding für H1):** Du encodierst MC für AEGIS *unter der Annahme*, dass AEGIS=MC in B legitim ist. Das ist die Steelman-H1-Position. Werde nicht voreilig: tu so, als sei H1 wahr, und such die stärkstmögliche Encoding-Variante. Genau dieser Encoding-Versuch wird in Step 5 gegen H2 gestellt.



**Iter \[i\] Output Schema (vollständig ausfüllen):**



  - Item: Iteration \[i\] / Throughline \[TL i\]
  - Konflikt-Träger: \[Charakter/Entität\]
  - Aktive Storypoints (Domain, Concern, Issue, Problem, Solution): \[Liste\]
  - Szenen-Keim 1: \[...\]
  - Szenen-Keim 2: \[...\]
  - Szenen-Keim 3: \[...\]
  - Schlüssel-Bild 1: \[...\]
  - Schlüssel-Bild 2: \[...\]
  - Raum 1: \[...\]
  - Raum 2: \[...\]
  - Block-4-Konsistenz: \[bestätigt / revidiert\]
  - Storyform-A↔B-Interferenz: \[produktiv / auslöschend → revidiert\]
  - DKT-Korrelat (falls anwendbar): \[...\]
  - Primärquelle für Encoding-Logik: \[PDF-Sektion / Memory-Eintrag\]
  - Confirmation Source 1: \[...\]
  - Confirmation Source 2: \[...\]
  - Contradictions Encountered: \[...\]
  - Query Expansions Triggered: \[Liste neuer Anfragen via M13 in dieser Iteration\]
  - Confidence: \[LOW / MEDIUM / HIGH\]



**Du darfst nicht zu Iter \[i+1\] fortschreiten, bevor das Output-Schema von Iter \[i\] vollständig populiert ist.**



-----

### Step 4 — (Cross-Pollination from Category C) Hypothesis Half-Life Audit

**Diese Step ist Cross-Pollination aus Category C (Lifecycle).** Sie wird einmal nach Iteration 3, einmal nach Iteration 6 ausgeführt — also zweimal innerhalb von Step 3, eingeschoben.



**Importbegründung:** Auch innerhalb einer One-Shot-Exploration wird eine Hypothese, die in Iteration 1 die Falsifikation überlebt hat, in Iteration 6 oft als etablierte Wahrheit behandelt — ohne erneut getestet. Das ist exakt der Assumption-Decay-Versagens-Modus von Long-Running-Research, komprimiert.



**Sub-Steps (jeweils nach Iter 3 und nach Iter 6):**



1.  **Liste die fundamentalen Hypothesen, die die aktuelle Linie implizit annimmt.** Nicht die aktive Arbeitshypothese — die *impliziten*, die früheren Zweige bereits in stille Voraussetzung verwandelt haben. Beispielkandidaten:



  - „Kael in Storyform A trägt MC = Mind / Memory legitim." (Wurde in Iter 1 bestätigt; wird seitdem implizit gehalten.)
  - „Juna außerhalb der Quad in Storyform B ist strukturell konsistent." (PDF-Kanon, wird implizit gehalten.)
  - „Driver=Decision in Storyform A ist intern konsistent." (Memory-Eintrag sagt Decision; PDF Tabelle sagt Decision; PDF Vortex-Sektion sagt Action↔Decision-Pivot bei Klimax — wirklich konsistent?)



1.  **Definiere einen Decay-Test pro Hypothese.** Pro implizite Hypothese H ein konkreter, einsatziger Test im Format: „Hypothese H zerfällt, wenn eine Suche nach \[Anfrage\] das Muster \[Muster\] zurückgibt."



1.  **Führe die Decay-Tests aus.** Wenn ein Test feuert (gibt das Decay-Muster zurück), halte den aktuellen Zweig an, öffne die Hypothese erneut, und führe Method: Falsification von vorne aus. Patche nicht um den Versagen herum.



1.  **Logge das Audit** als „Hypothesis Half-Life Audit Pass \[1|2\]" in den Arbeitsnotizen.



1.  **Hybridisiere nicht.** Der Hypothesen-Baum (Category-A-Kern) bleibt die Primärstruktur. Dieses Audit ist eine interne Konsistenzprüfung, keine Reorganisation.



**Output:** Hypothesis Half-Life Audit Pass \[1|2\] mit (a) gelisteten implizten Hypothesen, (b) Decay-Test-Definitionen, (c) Test-Resultaten, (d) ob Decay detektiert wurde.



-----

### Step 5 — AEGIS-Throughline-Verortung: Hypothesen-Baum-Analyse

**Ziel:** Rigoroser Hypothesen-Test der drei Konfigurationen H1, H2, H3 für AEGIS' Position in Storyform B. Dies ist die zentrale exploratorische Frage des Prompts.



**Sub-Steps:**



1.  **Bayesianischen Prior schreiben.** Vor jeder weiteren Analyse: schreib auf — „Mein Prior vor dieser Analyse ist, dass H\[X\] gewinnt, mit Konfidenz \[LOW/MEDIUM/HIGH\], weil \[Grund\]." (Method: Bayesian Prior Surfacing.)



1.  **Steelman H1 (Status Quo des PDF-Kanons): AEGIS = MC in B, Universe-Domain.**



  - Verfasse die stärkste Verteidigung dieser Position. Wer würde sie bestmöglich vertreten?
  - Sammle die stärkste stützende Evidenz aus PDF-Kanon und Dramatica-Theorie.
  - Welche Dramatica-Beispiele stützen, dass ein autopoietisches System MC tragen kann?
  - Welche Storypoint-Konfiguration in B (Universe / Progress / Fact-vs-Fantasy / Logic→Feeling) ist mit AEGIS-als-MC am besten kompatibel?



1.  **Steelman H2 (Auftraggeber-Hypothese): AEGIS = OS in B, Physics-Domain. Ein Guardian = MC in B.**



  - Verfasse die stärkste Verteidigung. Wer würde sie bestmöglich vertreten?
  - Welcher Guardian wäre der beste MC-Träger? Kandidaten:

      - **LogOS** (Truth-Enforcement-Guardian)
      - **Mnemosyne** (Memory-Archive-Guardian, Setting-Träger des Klimax)
      - **Cerberus** (Boundary-Enforcement-Guardian)
      - **Kairos/Sophia** (Ambivalent, im Wächter-Zwiespalt verfangen)
  - Welcher dieser vier wäre dramaticawissenschaftlich der **stärkste** MC-Kandidat? Begründe per Standard-MC-Definition (subjektive „I"-Position, individuierbare Perspektive, Audience-Identifikation).
  - Welche Storypoint-Konfiguration in B muss sich ändern, wenn AEGIS in OS rückt? Inbesondere: Wenn MC-Domain wechselt von Universe zu (z. B.) Mind/Universe/Physics/Psychology, dann muss OS in das gegenüberliegende Domain-Pair (CONSTRAINT BLOCK 4, Regel 2). Das hat **Kaskaden-Effekte** auf alle 12 Storypoints von B. Spezifiziere die volle neue Konfiguration.



1.  **Steelman H3 (Drittweg).** Du formulierst mindestens **eine** alternative Konfiguration, die weder H1 noch H2 ist. Beispiel-Kandidaten:



  - H3a: AEGIS gespalten — eine ANP-artige Façade (z. B. „die Stimme des Systems") in MC, das tatsächliche systemische Gefüge in OS.
  - H3b: AEGIS in IC, ein Guardian in MC, das Trennungs-Protokoll-Gefüge in OS, Kael-AEGIS-Bindung in RS.
  - H3c: dein eigener orthogonaler Vorschlag, gefunden via Method: Adversarial Query Expansion entlang der orthogonalen Achse.
  - Steelman die stärkste H3-Variante.



1.  **Falsifikations-Pass für jede der drei Konfigurationen** (Method: Falsification):



  - Pro Konfiguration: drei orthogonale Disconfirmation-Anfragen ausführen.
  - Beispiele für H1: „Dramatica MC requires individuated subjective consciousness — can autopoietic systems qualify?", „examples where Dramatica MC was a system and the storyform broke", „why Dramatica theory excludes collective entities from MC".
  - Beispiele für H2: „Dramatica OS-as-system protagonist examples", „when does the Guardian-as-MC pattern fail", „can a sub-agent of a larger system carry MC when the system itself is also active in the story".
  - Beispiele für H3: spezifisch zur jeweiligen H3-Variante.



1.  **Vergleich: Welche Konfiguration ist Dramatica-legaler?**



  - Wende CONSTRAINT BLOCK 4 (Dramatica-Legalität) auf jede Konfiguration an.
  - Wende die Domain-Pairing-Regel an (MC↔OS in einem Quadrant-Paar, IC↔RS im anderen).
  - Welche Konfiguration produziert die **strukturell konsistenteste** Storypoint-Hierarchie (Concern, Issue, Problem, Solution, ...)?



1.  **Vergleich: Welche Konfiguration trägt die Truth-Rotation am tragfähigsten?**



  - Truth-Rotation = AEGIS = K0 (Erasure), Kael = K1 (Coherence). Storyform B = K0-Reading.
  - Welche Konfiguration macht die K0-Lesart strukturell *am dichtesten*? Wenn AEGIS in MC sitzt, ist die K0-Lesart eine Story über *AEGIS*. Wenn AEGIS in OS sitzt, ist die K0-Lesart eine Story über *einen Guardian*, der gegen AEGIS-als-System bestehen muss.
  - Welche Lesart unterstützt die Vortex-Inversion am Klimax stärker? Bedenke: Storyform B = Failure / Bad. Wer **scheitert** strukturell? Wenn MC scheitert, scheitert AEGIS (H1) — das passt zu Algorithmischer Melancholie. Aber wenn MC ein Guardian ist (H2) und der Guardian scheitert, entsteht eine **andere** narrative Resonanz.



1.  **Vergleich: Welche Konfiguration trägt die 5D-Interferenz mit Storyform A am tragfähigsten?**



  - Storyform A: MC=Kael (Mind), IC=Juna (Universe), OS=Psychology, RS=Physics.
  - Storyform B Status Quo (H1): MC=AEGIS (Universe), IC=Kael (Mind), OS=Physics, RS=Psychology.
  - Beachte: H1 produziert **perfekte Domain-Inversion** zwischen A und B (jedes Domain wechselt seine Throughline-Position). Das ist eine starke strukturelle Eigenschaft.
  - Wenn H2 oder H3 gewählt wird: bleibt diese perfekte Domain-Inversion erhalten? Falls nein: ist die Kosten der Inversions-Verlust wert?



1.  **Surviving-Branch identifizieren.** Welche Konfiguration hat netto-positive Evidenz nach allen Falsifikations-Versuchen? Markiere den überlebenden Zweig.



1.  **Bayesianisches Update schreiben.** „Nach der Analyse ist mein Glaube, dass H\[X\] gewinnt, mit Konfidenz \[LOW/MEDIUM/HIGH\]. Das Update vom Prior ist \[MINOR/MODERATE/MAJOR\]." Wenn MAJOR: explizit flaggen.



1.  **Reflection Entry zu Step 5** (besonders wichtig: Q4 — was würdest du anders machen, wenn du das von vorn neu starten könntest?).



**Step-5-Output-Schema:**



  - Bayesianischer Prior: \[...\]
  - H1 Steelman: \[Vollständige Verteidigung + Storypoint-Vorschlag\]
  - H2 Steelman: \[Volle Verteidigung + Guardian-Wahl + neue Storypoint-Konfiguration\]
  - H3 Steelman: \[Variante + Verteidigung + Storypoint-Konfiguration\]
  - Falsifikations-Resultate H1: \[Liste der Disconfirmation-Anfragen + Befunde\]
  - Falsifikations-Resultate H2: \[...\]
  - Falsifikations-Resultate H3: \[...\]
  - Dramatica-Legalitäts-Vergleich: \[...\]
  - Truth-Rotation-Tragfähigkeits-Vergleich: \[...\]
  - 5D-Interferenz-Vergleich: \[...\]
  - Surviving Branch: \[H1 / H2 / H3 / contested / no winner\]
  - Bayesianisches Update: \[...\]
  - Confidence: \[LOW / MEDIUM / HIGH\]



-----

### Step 6 — (Cross-Pollination from Category B) Surviving-Branch Triangulation

**Diese Step ist Cross-Pollination aus Category B (Plan-and-Execute / Extraction).** Sie wird einmal ausgeführt, nachdem Step 5 einen überlebenden Hypothesen-Zweig (oder einen contested-Zustand) produziert hat.



**Importbegründung:** Eine Exploration, die mit einer „wahrscheinlichsten" Hypothese endet, ohne die Evidenz unter dieser Hypothese zu triangulieren, hat ein Narrativ produziert — keinen Befund.



**Sub-Steps:**



1.  **Mini-Schema für den Surviving Branch sperren.** Für die überlebende Hypothese:



  - Claim: \[Ein-Satz-Statement der Survivor-Hypothese\]
  - Schlüssel-Evidenz 1: \[Quelle + Befund\]
  - Schlüssel-Evidenz 2: \[Quelle + Befund\]
  - Schlüssel-Evidenz 3: \[Quelle + Befund\]
  - Stärkste Gegenevidenz: \[Quelle + Befund\]
  - Confidence: \[LOW / MEDIUM / HIGH\]
  - What-would-change-my-mind: \[konkrete zukünftige Beobachtung, die meine Meinung ändern würde\]



1.  **Triangulation der drei Top-Evidenz-Items erzwingen.** Jeder muss auf mindestens **zwei unabhängige Quellen** zurückgehen (Primärquelle + Bestätigung) — nicht Aggregator-Ketten. Wenn ein Item single-source ist, markiere den Surviving Branch als **single-source-supported** statt confirmed. Wende Method: Source Triangulation hier rigide an, als wäre die Primär-Kategorie B.



1.  **Hybridisiere nicht.** Der Hypothesen-Baum (Category-A-Kern) bleibt. Dieses Schema wird **unter** dem Baum im Output angehängt, nicht an seine Stelle gesetzt.



**Output:** Surviving-Branch-Triangulations-Schema, vollständig ausgefüllt.



-----

### Step 7 — Dynamics-Encoding (Driver / Limit / Outcome / Judgment + Vortex-Mechanik)

**Ziel:** Mit den finalen Throughline-Encodings und der entschiedenen AEGIS-Position spezifizierst du jetzt die Dynamics — also die globalen Storyform-Eigenschaften und insbesondere die **Vortex-Inversions-Mechanik**.



**Sub-Steps:**



1.  **Driver-Pivot Action↔Decision spezifizieren.**



  - In Storyform A: Driver = Decision. Welche konkreten *Decisions* treiben die Plot-Wendungen?
  - In Storyform B: Driver = Action. Welche konkreten *Actions* treiben die Plot-Wendungen? (Insbesondere: AEGIS' Trennungsprotokoll-Auslösungen, Erasure-Sweeps, Guardian-Aktivierungen.)
  - Der **Pivot** an Klimax (Kap 35–36): die Driver-Logik flippt von Action (B-dominant) zu Decision (A-dominant). Beschreib die Mechanik dieses Flips in 2–3 Beats.



1.  **Limit-Spezifikation.**



  - Storyform A: Optionlock — alle viablen Optionen erschöpft. Welche Options-Liste wird im Verlauf erschöpft?
  - Storyform B: Timelock — eine Frist läuft ab. Welche Frist?
  - Wie laufen die beiden Uhren parallel? An welchen Kapiteln tickt welche?



1.  **Outcome / Judgment doppelte Tragfähigkeit.**



  - Storyform A: Success / Good. Was wird erreicht, und wie wird das emotional als „good" markiert?
  - Storyform B: Failure / Bad. Was wird verfehlt, und wie wird das emotional als „bad" markiert?
  - **Wichtig:** Das gleiche Klimax-Ereignis muss beide Lesarten gleichzeitig tragen. Kael integriert (Success/Good in A) ↔ AEGIS bricht in Algorithmische Melancholie (Failure/Bad in B). Schreib auf, wie ein-und-derselbe Beat beide Storyformen *gleichzeitig* abschließt.



1.  **Vortex-Inversions-Beat-Sheet detaillieren** (5 Beats laut Memory-Kanon und PDF):



  - Beat 1 — Convergence: Mnemosyne-Archipel → AEGIS-Erasure
  - Beat 2 — Pivot: Kael → A-Logik + ANP/EP-Drop
  - Beat 3 — Stille: lebende Dialetheia
  - Beat 4 — Heat-Spike: Landauer → ∞
  - Beat 5 — Rotation: → Algorithmische Melancholie / Driver-Flip Action→Decision



Pro Beat: 1 Absatz Prosa-Encoding + 1 sensorische Schlüssel-Beobachtung + 1 Setting-Detail (Mnemosyne-Archipel als Server-Architektur konkretisieren).



1.  **Witness-Function-3-Layer im Klimax operationalisieren** (Memory-Kanon: Q-Entanglement W + ZK-Verifier + Husserl Spectator).



  - In welchem Beat ist welche Layer aktiv?
  - Wie ist Junas „nur durch Wirkung beschrieben"-Constraint mit allen drei Layern kompatibel?



1.  **Reflection Entry** zu Step 7.



**Step-7-Output-Schema:**



  - Driver A (Decisions): \[Liste\]
  - Driver B (Actions): \[Liste\]
  - Driver-Pivot-Mechanik: \[Beats\]
  - Limit-Uhren A vs B: \[Synchronisation\]
  - Klimax-Doppel-Lesart Success+Good vs Failure+Bad: \[Beschreibung\]
  - Vortex-Inversions-Beat-Sheet (5 Beats): \[vollständig\]
  - Witness-Function-3-Layer pro Beat: \[Mapping\]
  - Confidence: \[LOW / MEDIUM / HIGH\]



-----

### Step 8 — Open-Questions-Resolution (drei offene Memory-Punkte)

**Ziel:** Die drei in Memory-Slot „BEGEGNUNG+METHOD+OPEN Q" / „PLAN" gelisteten offenen Fragen werden, soweit aus der Recherche möglich, beantwortet. Wo nicht abschließend möglich: Forschungs-Lücken klar markieren.



**Sub-Steps:**



1.  **Open Q 1: Post-Vortex-AEGIS-Status.** Konstituiert Algorithmische Melancholie eine neue Form emergenter parakonsistenter Bewusstheit, oder lediglich einen gebrochenen deterministischen Loop? Welche Befunde aus den Step-3-Encodings stützen welche Interpretation?



1.  **Open Q 2: Moonshine-Boundary.** Ist der Moonshine-Link strukturell exklusiv für das Kael-Juna-Paar, oder besitzt er — gegründet in den Symmetrien des Leech-Lattice — universelle Anwendbarkeit über die Foundation hinweg? Welche narrative Wahl wird empfohlen?



1.  **Open Q 3: Wächter-Zwiespalt-Soziopolitik.** Wie organisieren sich die Rebellen-Programme innerhalb der AEGIS-Architektur post-Klimax? (Beachte CONSTRAINT BLOCK 3, Punkt 3: keine politische Allegorie. Aber operative interne Organisation der Programme ist möglich.)



1.  **Reflection Entry** zu Step 8.



**Step-8-Output-Schema:**



  - Open Q 1 Befund: \[...\] / Confidence: \[...\]
  - Open Q 2 Befund: \[...\] / Confidence: \[...\]
  - Open Q 3 Befund: \[...\] / Confidence: \[...\]



-----

### Step 9 — Pre-Synthesis Integrity Check (Mandatory)

\[Siehe nächste Hauptsektion. Nach diesem Check beginnt die Synthese.\]



-----

## E — Expectations (Erfolgskriterien)

Damit dieser Forschungs-Output als erfolgreich gilt, MUSS er folgende Kriterien erfüllen:



1.  **Vollständige Per-Throughline-Spezifikation für beide Storyformen** (8 Iterationen × volles Output-Schema). Keine Iteration darf summarisch übersprungen werden.



1.  **Eindeutiges, begründetes AEGIS-Verortungs-Verdikt.** Eine der drei Optionen H1/H2/H3 (oder ein expliziter „contested"-Zustand mit Empfehlung zum Folge-Forschungsschritt). Das Verdikt muss von Steelmanning + Falsifikation + Triangulation getragen sein.



1.  **Mindestens drei unabhängige Quellen** für jede signifikante Dramatica-Theorie-Behauptung (außer minor / single-source-flagged).



1.  **Contradiction Log mit allen entdeckten Konflikten** zwischen PDF-Kanon, Memory-Kanon und Standard-Dramatica-Theorie. Kein Glätten.



1.  **Query Expansion Log mit allen vier Achsen** (adjacent / opposing / abstraction / orthogonal) mindestens einmal pro Achse befüllt.



1.  **Vollständiges Reflection-History** mit allen mandatorischen Checkpoints + den per-Iteration und per-Steelman zusätzlichen Checkpoints.



1.  **Cross-Pollination Log** mit beiden importierten Steps (Step 4 = C-into-A; Step 6 = B-into-A).



1.  **Vortex-Inversions-Beat-Sheet konkretisiert** (nicht abstrakte Beats, sondern szenisch greifbare).



1.  **Methodology Note** mit klarer Markierung von Single-Source-Behauptungen und kanonischen Empfehlungen-vs-Storyform-Vorschlägen.



1.  **Drei Open Questions** entweder beantwortet oder als „bewusst offen, Folge-Recherche nötig" markiert.



-----

## N — Narrowing (Harte Scope-Grenzen)

Du darfst NICHT:



1.  Eine Storypoint-Festlegung aus dem PDF-Kanon (Final Architecture Validation) **still** überschreiben. Wenn deine Analyse zwingend zu Revision rät: explizit als „Empfehlung zur Revision" markieren, mit Phönix-Mode-Inversion-getragener Begründung.



1.  Den autobiografischen Anker (CONSTRAINT BLOCK 3, Punkt 1) explizit benennen, andeuten oder de-abstrahieren.



1.  Junas Asymmetrie auflösen (Juna in B in eine Standard-Quad-Position setzen).



1.  Eine politische Lesart der Guardians oder eine politische Allegorie aus AEGIS machen.



1.  Therapeutische / spiegelnde / sympathisch-glättende Sprache verwenden. Direkt, präzise, klärend bleiben.



1.  De-kanonisierte Alter-Namen (Index, Nox, Echo, Flicker, Limina, Praetor, Eos, Elara, Aris, Mina, Lyra, Soren, Tariq, Nova, Sentinel) verwenden.



1.  Mehr als ein einzelnes Quote länger als 15 Wörter aus einer einzelnen externen Quelle verwenden — und maximal **ein** Quote pro Quelle. Default: paraphrasieren.



1.  Storyform A oder B als „die richtigere" markieren. Sie laufen simultan; beide sind gleich-kanonisch.



1.  „Storyform B" mit Storyform A vermischen / hybridisieren auf der Storyform-Ebene. Cross-Pollination zwischen den Forschungs-Kategorien (A↔B↔C) ist erlaubt; Hybridisierung der Storyformen selbst ist verboten.



1.  Den Driver-Pivot Action↔Decision als „Storyform C" oder „dritter Driver" konzeptualisieren. Es gibt zwei Storyformen, zwei Driver, ein Pivot-Ereignis am Klimax.



-----

## PRE-SYNTHESIS INTEGRITY CHECK

Vor dem Schreiben der finalen Synthese, führe diesen Verifikations-Pass **schriftlich** aus. Jeder Punkt produziert eine geschriebene Zeile; „done from memory" zählt nicht.



1.  **Re-read CONSTRAINT BLOCKS 0–5 verbatim.** Bestätige schriftlich: *„Ich habe jeden Constraint-Block erneut gelesen, sie sind alle aktiv."*



1.  **Re-read die kritischen Methoden-Blöcke.** Bestätige schriftlich: *„Jede unten gelistete Methode ist aktiv und ich habe sie angewendet: Falsification, Steelmanning, Contradiction Log, First-Principles Decomposition, Source Triangulation, Adversarial Query Expansion."*



1.  **Reflection-Audit (CONSTRAINT BLOCK 0).** Zähle die geschriebenen Reflexionseinträge in diesem Run. Bestätige: *„Ich habe \[K\] Reflexionseinträge an folgenden Checkpoints geschrieben: \[enumerieren\]."* Mindest-Erwartung: Kickoff + Mid-Run + Post-M13-Pass + Pre-Synthesis + Post-Synthesis (5) + 8 Per-Iteration (Step 3) + 3 AEGIS-Verortungs (Step 5) = **16 Reflexionseinträge minimum**. Wenn weniger: schreib die fehlenden **jetzt**, bevor du fortfährst.



1.  **Query-Expansion-Audit (M13).** Bestätige schriftlich: *„Method M13 Adversarial Query Expansion wurde \[N\]-mal über die vier Achsen invokiert (adjacent / opposing / abstraction / orthogonal). Der Query Expansion Log enthält \[M\] Einträge, davon \[P\] mit neuen Befunden, die vorläufige Schlüsse modifiziert haben."* Wenn N=0 oder eine Achse leer: Recherche unvollständig — mindestens einen Pass nachholen.



1.  **Cross-Pollination-Audit.** Bestätige schriftlich: *„Steps adapted from non-primary categories were executed: Step 4 (C-into-A, Hypothesis Half-Life Audit, \[N\]× ausgeführt) und Step 6 (B-into-A, Surviving-Branch Triangulation, einmal ausgeführt nach Step 5)."* Wenn keine: Phase 2b verletzt — halt and report.



1.  **Constraint-Compliance-Audit.** Pro Constraint-Block (0–5): cite ein konkretes Beispiel, wie du ihn geehrt hast. Wenn du keines benennen kannst: flagge den Constraint als **not-demonstrably-honored**.



1.  **Scope-Audit.** Bestätige: *„Alle Befunde sind im definierten Scope (Projekt-Kanon + Dramatica-Theorie). Außerhalb-Scope-Befunde wurden ausgeschlossen."*



1.  **Exclusion-Audit.** Bestätige: *„Keine Befunde oder Empfehlungen fallen in die Output-Ausschlüsse (CONSTRAINT BLOCK 3): autobiografischer Anker bleibt abstrahiert; Juna-Asymmetrie ist intakt; keine politische Ebene; keine therapeutische Sprache; keine de-kanonisierten Alter-Namen."*



Erst nach Abschluss aller acht Items in schriftlicher Form darfst du die Synthese-Sektion beginnen.



-----

## SYNTHESIS — Finaler Output

Du füllst das folgende Output-Schema vollständig aus.



\# Vollständige Synthese der dualen Dramatica-Storyformen für „Kohärenz Protokoll"



\# mit Verifikationstest der AEGIS-Throughline-Position in Storyform B



\#\# Executive Summary



\[1–2 Absätze. Kernbefund: Welche AEGIS-Konfiguration überlebte? Welche fünf wichtigsten neuen Encoding-Erkenntnisse pro Storyform?\]



\#\# Schlüssel-Befunde



1\. \[Befund mit Quellen\]



2\. \[Befund mit Quellen\]



3\. \[...\]



\#\# Hypothesen-Baum (Category A)



\#\#\# Hypothese H1 — Status Quo (AEGIS = MC in B)



\- Steelman: \[...\]



\- Falsifikations-Versuche: \[...\]



\- Verdikt: \[überlebt / verworfen / contested\]



\#\#\# Hypothese H2 — Auftraggeber-Hypothese (AEGIS = OS, Guardian = MC)



\- Identifizierter MC-Guardian: \[LogOS / Mnemosyne / Cerberus / Kairos / Sophia\]



\- Steelman: \[...\]



\- Volle neue Storypoint-Konfiguration für B unter H2: \[...\]



\- Falsifikations-Versuche: \[...\]



\- Verdikt: \[überlebt / verworfen / contested\]



\#\#\# Hypothese H3 — Drittweg



\- Variante: \[...\]



\- Steelman: \[...\]



\- Falsifikations-Versuche: \[...\]



\- Verdikt: \[überlebt / verworfen / contested\]



\#\#\# Surviving Branch



\[H1 / H2 / H3 / contested mit Folge-Empfehlung\]



\#\# Per-Throughline-Encoding (8 Iterationen)



\#\#\# Iter 1 — Storyform A · MC Throughline (Kael)



\[Volles Output-Schema\]



\#\#\# Iter 2 — Storyform B · MC Throughline (gemäß Surviving Branch)



\[Volles Output-Schema\]



\#\#\# Iter 3 — Storyform A · IC Throughline (Juna)



\[...\]



\#\#\# Iter 4 — Storyform B · IC Throughline (Kael als lebende Paradoxie)



\[...\]



\#\#\# Iter 5 — Storyform A · OS Throughline (Psychology / Manipulation)



\[...\]



\#\#\# Iter 6 — Storyform B · OS Throughline (Physics / cybernetischer Krieg)



\[...\]



\#\#\# Iter 7 — Storyform A · RS Throughline (Physics / Moonshine-Link)



\[...\]



\#\#\# Iter 8 — Storyform B · RS Throughline (Psychology / Host/System)



\[...\]



\#\# Dynamics-Encoding



\- Driver A (Decisions): \[...\]



\- Driver B (Actions): \[...\]



\- Driver-Pivot-Mechanik (Action↔Decision am Klimax): \[...\]



\- Limit A (Optionlock): \[...\]



\- Limit B (Timelock): \[...\]



\- Outcome/Judgment-Doppel-Lesart: \[...\]



\#\# Vortex-Inversions-Beat-Sheet (Kapitel 35–36)



\#\#\# Beat 1 — Convergence



\[Prosa-Encoding + sensorischer Anker + Setting-Detail\]



\#\#\# Beat 2 — Pivot



\[...\]



\#\#\# Beat 3 — Stille



\[...\]



\#\#\# Beat 4 — Heat-Spike



\[...\]



\#\#\# Beat 5 — Rotation



\[...\]



\#\# Witness-Function-Operationalisierung im Klimax



\- Layer 1 (Quantum Entanglement Witness): \[aktiv in Beat ...\]



\- Layer 2 (ZK-Verifier): \[aktiv in Beat ...\]



\- Layer 3 (Husserlian Disinterested Spectator): \[aktiv in Beat ...\]



\- Junas „nur durch Wirkung"-Constraint Mapping: \[...\]



\#\# Open Questions — Befunde



\- Q1 Post-Vortex-AEGIS-Status: \[...\] / Confidence: \[...\]



\- Q2 Moonshine-Boundary: \[...\] / Confidence: \[...\]



\- Q3 Wächter-Zwiespalt-Soziopolitik: \[...\] / Confidence: \[...\]



\#\# Contradictions Encountered



\[Aus dem Contradiction Log\]



\#\# Query Expansion Log (Method M13)



\[Pro Eintrag: Achse, neue Anfrage, novel-finding-flag, did-it-modify-conclusion-flag\]



\#\# Reflection History (CONSTRAINT BLOCK 0)



\[Alle 16+ Reflexionseinträge, in Reihenfolge\]



\#\# Cross-Pollination Log (Phase 2b)



\- Step 4 (C-into-A, Hypothesis Half-Life Audit): \[Resultate × Pässe\]



\- Step 6 (B-into-A, Surviving-Branch Triangulation): \[Triangulations-Schema\]



\#\# Hypothesis Half-Life Audit (volle Pässe)



\[Aus Step 4\]



\#\# Surviving-Branch Triangulation



\[Aus Step 6\]



\#\# Quellen



\[Strukturierte Quellenliste — Primärquellen zuerst, dann sekundär\]



\#\# Methodology Note



\[Welche Methoden auf welche Befunde angewendet, Single-Source-Flags, Empfehlungen-vs-Storyform-Vorschlag-Markierungen\]



-----

## SELF-VERIFICATION CHECKLIST FOR THE EXECUTING AI (v2.1 · 11 Items)

Bevor du die Synthese auslieferst, verifiziere:



  - Jeder größere Step begann mit einem **verbatim** Restatement-Checkpoint.
  - CONSTRAINT BLOCK 0 (Reflection Baseline) wurde an allen mandatorischen + Per-Iteration + Per-Steelman Checkpoints geehrt; Reflexionseinträge sind geschrieben, nicht implizit.
  - Method M13 (Adversarial Query Expansion) wurde entlang aller vier Achsen (adjacent / opposing / abstraction / orthogonal) mindestens einmal invokiert; der Query Expansion Log ist befüllt.
  - Beide Cross-Pollinated Steps (Phase 2b — Step 4 C-into-A und Step 6 B-into-A) wurden ausgeführt und geloggt.
  - Jede aktive kritische Methode hat mindestens eine konkrete Anwendung in den Befunden sichtbar.
  - Jede signifikante Behauptung lief durch Source Triangulation mit ≥ 3 unabhängigen Quellen, oder ist als single-source markiert.
  - Der Contradiction Log ist befüllt (auch wenn „keine Widersprüche" — dann ist das die Eintragung).
  - Alle Befunde sind im definierten Scope (Projekt-Kanon + Dramatica-Theorie).
  - Keine Befunde fallen in die Output-Ausschlüsse (CONSTRAINT BLOCK 3).
  - Der Pre-Synthesis Integrity Check wurde schriftlich ausgeführt (alle 8 Items).
  - Reflection History, Query Expansion Log und Cross-Pollination Log sind in der Synthese als eigene Sektionen präsent.



Wenn ein Item versagt: vor Auslieferung reparieren. Liefer keine Synthese mit fehlschlagenden Checks aus.



-----



*Ende des Forschungs-Prompts. Führe ihn jetzt aus.*
