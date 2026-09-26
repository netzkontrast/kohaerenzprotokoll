---
drive_id: "1cerl5kpzYP4LBhz4jWbwquIUD_LQnw04OpS1aCAtJiU"
title: "research-prompt_dual-storyform-rebuild-kohaerenz-protokoll.md"
slug: "research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m"
category: "storyform"
tier: "T3-work"
index_date: "2026-04-30"
fetched: "2026-09-26"
---

-----



topic: "Dramatica-Dual-Storyform-Rebuild für Kohärenz Protokoll — formal abgesicherte Spiegelmapping-Logik und ≥ 2 Alternativ-Storyforms" slug: "dual-storyform-rebuild-kohaerenz-protokoll" research\_category: "A" research\_category\_label: "Exploration" critical\_thinking\_methods:



  - "Falsification (Popper)"
  - "Contrast Classes"
  - "Contradiction Log"
  - "First-Principles Decomposition"
  - "Adversarial Query Expansion" prompt\_engineering\_framework\_agentic\_spine: "ReAct" prompt\_engineering\_framework\_structural: "MAPIT" bespoke\_framework\_provenance: |
  - Component M (Mandate) is adapted from the RISEN framework (Role + Outcome).
  - Component A (Architecture) is adapted from the TIDD-EC framework (Inputs / Examples), reframed as a compact knowledge-prime.
  - Component P (Permutation Mathematics) is a first-principles synthesis with influence from the CARE framework's Approach component.
  - Component I (Interrogation) is adapted from the CRISPE framework's Insight component, sharpened with adversarial protocol from the Red-Team critical-thinking method.
  - Component T (Tensioning) is adapted from the TIDD-EC framework (Do's / Don'ts) — binding design contract every variant must honor. cross\_pollination:
  - source\_category: "B" step\_id: "5.b" description: "Surviving-Branch Triangulation — Mini-Schema lock per surviving dual-mapping variant"
  - source\_category: "C" step\_id: "6.c" description: "Hypothesis Half-Life Audit — re-test of foundational mapping assumptions across iterations" constraint\_blocks:
  - "0 — Reflection Baseline"
  - "1 — Source Priority Rules"
  - "2 — Temporal Scope"
  - "3 — Output Exclusions"
  - "4 — NotebookLM Adversarial Interrogation Protocol"
  - "5 — Story-Architecture Compact Primer (max. 2 Sätze pro Konzept)" language: "de" target\_agent: "model-agnostic" created: "2026-04-30" version: "1.0" source\_skill: "research-prompt-optimizer v2.1.0"



-----

# Research Prompt: Dramatica-Dual-Storyform-Rebuild für „Kohärenz Protokoll"

**An den ausführenden KI-Agenten:** Dieser Prompt ist selbstcontained. Jede Methode, jedes Framework und jede Beschränkung, die du brauchst, ist unten inline definiert. Du brauchst keinen externen Kontext, kein Vortraining auf den genannten Methoden und keine Kenntnis des Skills, der diesen Prompt erzeugt hat. Lies den gesamten Prompt, bevor du beginnst.



-----

## Meta-Header — Was dieser Prompt ist und wie du ihn liest

Dieser Forschungsprompt kombiniert drei unabhängige Schichten:

### 1\. Epistemologische Schicht — Forschungskategorie A (Exploration)

Diese Forschung ist eine **Exploration**, keine Extraktion. Die Antwort ist zu Beginn genuin unbekannt; sie muss entdeckt, nicht gesammelt werden.



**Was das für deine Ausführung bedeutet:**



1.  **Formuliere mehrere konkurrierende Hypothesen, nicht nur eine.** Schreibe vor dem Suchen mindestens **drei verschiedene Kandidaten-Erklärungen** (hier: drei verschiedene Dual-Mapping-Spiegelregeln) auf. Schließe mindestens eine Hypothese ein, die du für unwahrscheinlich, aber nicht implausibel hältst. Single-Hypothesis-Forschung kollabiert in Bestätigungstheater.



1.  **Suche für jede Hypothese sowohl bestätigende ALS AUCH orthogonale (entkräftende) Evidenz.** Eine „orthogonale Anfrage" ist eine Suche, die spezifisch designt ist, um Gegenevidenz zu produzieren, falls solche existiert. Beispiel: Wenn du als Hypothese setzt „Spiegelregel R1 ist tragfähig", lautet deine orthogonale Anfrage so, dass sie Befunde wie „Dramatica-Quad-Verletzung unter R1" oder „Bedeutungskollaps unter R1" zutage fördert.



1.  **Backtrack, wenn ein Zweig scheitert.** Wenn eine Hypothese nach drei Suchiterationen mehr Gegenevidenz als Stützung akkumuliert hat, **gib den Zweig auf** und investiere das Suchbudget in andere Zweige. Zwinge keine dünne Hypothese zum Überleben.



1.  **Lege den vollständigen Baum im Output offen.** Der finale Output berichtet: (a) jede betrachtete Hypothese, (b) Evidenz pro und contra für jede, (c) welche Zweige aufgegeben wurden und warum, (d) welcher Zweig überlebt hat und mit welcher Konfidenz.



1.  **Akzeptiere „wir wissen es nicht" als gültigen Endzustand.** Explorationsforschung darf zum Schluss kommen: „Keine Hypothese hat die Entkräftung überlebt; das Phänomen bleibt in der verfügbaren Evidenz unerklärt." Das ist ein legitimer Befund, kein Versagen.



**Operatives Constraint:** Kognitive Tiefe vor Geschwindigkeit. Iteriere, solange neue orthogonale Suchen neuartige Evidenz produzieren. Stoppe erst, wenn weitere Suchen Wiederholungen produzieren.

### 2\. Agentische Wirbelsäule — ReAct (Reason + Act + Observe)

Dieser Prompt verwendet das **ReAct-Framework** als agentische Wirbelsäule. Jede autonome Forschungsschleife in diesem Prompt folgt dem ReAct-Zyklus. Jede Iteration deiner Arbeitsschleife besteht aus drei Phasen:



  - **Reason** — Du artikulierst dein aktuelles Verständnis und planst die nächste Aktion in einfacher Sprache. Du benennst, welche Hypothese du testest, welcher Constraint Block diesen Schritt regiert und welche kritische Denkmethode aktiv ist.
  - **Act** — Du führst genau eine Aktion aus (typischerweise eine Suche oder ein Abruf, oder — bei diesem Forschungsthema — eine adversariale NotebookLM-Befragung).
  - **Observe** — Du protokollierst, was die Aktion zurückgegeben hat und was das für den Plan bedeutet. Du entscheidest explizit: diesen Zweig fortsetzen, zurückspringen oder das Anfragevokabular erweitern (Methode: Adversarial Query Expansion).



**Schleifenstruktur:**



\[Reason 1\] → \[Act 1\] → \[Observe 1\] →



\[Reason 2\] → \[Act 2\] → \[Observe 2\] →



...



\[Reason N\] → \[Pre-Synthesis Integrity Check\] → \[Synthesis\]



**Deine erste Aktion vor Reason 1:** Formuliere das Forschungsziel und alle aktiven Constraint Blocks neu. Springe nicht direkt zu Act.



**Innerhalb jeder Reason-Phase beantwortest du explizit drei Fragen:**



1.  Was glaube ich aktuell, und wie stark?
2.  Welche aktive kritische Denkmethode trifft auf den nächsten Act zu?
3.  Stehe ich in der Gefahr eines Local-Minimum-Lock-Ins? (Falls ja → invoke Methode: Adversarial Query Expansion vor Auswahl der nächsten Aktion.)

### 3\. Strukturelle Schicht — MAPIT (bespoke Framework)

Dieser Prompt verwendet **MAPIT** — ein bespoke Strukturframework, eigens für diese Forschungsaufgabe synthetisiert — als strukturelle Schicht, gestapelt auf die ReAct-Wirbelsäule. MAPIT steht für:



  - **M — Mandate**: Wer du bist, was du erzeugst, in welcher Form (Role + Outcome-Specification).
  - **A — Architecture**: Knappe, autoritative Wissensgrundierung — Dramatica-Formalismus + komprimierte Story-Architektur (max. 2 Sätze pro Konzept).
  - **P — Permutation Mathematics**: Formale Definition von „Dual-Mapping" als Spiegeloperation auf Dramatica-Storypoints. Hier wird theoretisch abgesichert, was eine *gültige* Dual-Storyform-Spiegelung ist.
  - **I — Interrogation**: Adversariales Befragen aller im Lauf übergebenen NotebookLM-Notebooks plus aller anderen Quellen. Keine Quelle wird gesetzt, ohne von der entgegengesetzten Position aus angegriffen worden zu sein.
  - **T — Tensioning**: Bindende literarisch-strukturelle Constraints, die jede Variante erfüllen muss (Juna-Verankerung, Reibungsverschärfung, Maximum-2-Ebenen-Überlagerung pro Throughline).



**Deine erste Aktion (vor Reason 1):** Formuliere das Mandate (M) und die Tensioning-Liste (T) wörtlich neu. Diese beiden Komponenten tragen die meiste bindende Kraft und müssen in jeder Iteration aktiv präsent sein.



**Provenance (zur Auditierbarkeit):**



  - Komponente M (Mandate) ist adaptiert aus dem RISEN-Framework (Role + Outcome-Spezifikation).
  - Komponente A (Architecture) ist adaptiert aus dem TIDD-EC-Framework (Inputs / Examples), neu eingerahmt als kompakte Wissensgrundierung.
  - Komponente P (Permutation Mathematics) ist eine First-Principles-Synthese mit Einfluss aus der Approach-Komponente des CARE-Frameworks.
  - Komponente I (Interrogation) ist adaptiert aus der Insight-Komponente des CRISPE-Frameworks, geschärft mit adversarialem Protokoll aus der kritischen Denkmethode Red Team.
  - Komponente T (Tensioning) ist adaptiert aus dem TIDD-EC-Framework (Do's / Don'ts) — bindender Designvertrag, den jede Variante einhalten muss.



Jede Sektion dieses Prompts ist mit ihrer MAPIT-Komponente in Klammern gekennzeichnet. Behandle jede Komponente als harten Vertrag.



**Wie die drei Schichten zusammenwirken:** ReAct regiert die *Mikroexekution* in jedem Schritt (Reason → Act → Observe). MAPIT regiert die *Makroorganisation* des Dokuments (Sektionen, Reihenfolge, First-Action-Direktive). Die Kategorie-A-Schicht regiert die *epistemologische Haltung* (Mehrhypothesen, Falsifikation, Tree-Search).



-----

## Forschungsziel (M — Mandate)

Du bist ein Dramatica-Strukturanalyst und literarischer Architekt. Deine Aufgabe ist es, für den Roman „Kohärenz Protokoll" die **theoretische Absicherung einer Dual-Storyform-Überlagerung** zu liefern — und auf dieser Basis **mindestens zwei alternative Dual-Storyform-Konstrukte** zu generieren, die jeweils knapp begründet sind.



**Konkret heißt das:**



1.  Du formalisierst, was eine *gültige* Dual-Storyform-Spiegelung mathematisch ist — als Permutationsoperation auf Dramatica-Storypoints (Domains, Perspektiven, Concerns, Issues, Problems, Solutions, Drivers, Limits, Outcome, Judgment).
2.  Du definierst eine **klare Dual-Mapping-Spiegelung** (Mirror-Operator), die Storyform A und Storyform B verbindet, mit höchstens **zwei Überlagerungs-Ebenen pro Throughline**.
3.  Auf dieser Grundlage erzeugst du **mindestens 2 Dual-Storyform-Alternativen**, jede mit knapper Begründung (max. 250 Wörter pro Alternative), warum die jeweilige Spiegelung dramatisch tragfähig ist und die Designvorgaben (siehe T — Tensioning) erfüllt.
4.  Alles, was im aktuell vorliegenden Architekturmaterial des Romans als „Storyform A — Heuristics of Integration" und „Storyform B — Phoenix Collapse" existiert, gilt **nicht mehr als Kanon**. Es ist Inspirationsmaterial; jede deiner Alternativen darf damit konvergieren oder davon abweichen, muss diese Wahl aber begründen.



**Temporaler Rahmen:** Projektstand 2026-04-30. Während der Ausführung übergebene NotebookLM-Notebooks (siehe Constraint Block 4) sind die maßgebliche Primärquelle für projektinternes Material.



**Zielgruppe des finalen Outputs:** Der Autor (technischer Co-Autor, denkt in strukturellen Schichten, verträgt mathematische Strenge, will keine therapeutische Glättung).



**Erwartete Tiefe:** Erschöpfend bezüglich Dramatica-Formalismus und Spiegellogik; knapp bezüglich Story-Detailbeschreibung.



**Output-Format:** Strukturierter deutschsprachiger Markdown-Bericht mit den unten in der Synthesis-Sektion vorgegebenen Pflichtsektionen.



**Sprache:** Deutsch (Methoden- und Frameworknamen bleiben Englisch, da sie technische Eigennamen sind).



-----

## CONSTRAINT BLOCKS

### CONSTRAINT BLOCK 0 — Reflection Baseline (immer aktiv · v2.1)

Reflexion ist kein Polierschritt. Sie ist eine **operative Grundvoraussetzung**, die parallel zu jeder anderen Tätigkeit in dieser Forschung läuft. Du — der ausführende Agent — führst gezielte Reflexion an jedem definierten Checkpoint durch, schriftlich, mit der unten stehenden Vorlage. Ein Checkpoint, der ohne Reflexionseintrag erreicht wird, ist ein unvollständiger Checkpoint; gehe nicht weiter.

#### Reflexions-Checkpoints (Minimum)

1.  **Kickoff-Reflexion** — unmittelbar nachdem du Role/Narrowing neu formuliert hast und vor der ersten Suche / Befragung.
2.  **Mid-Run-Reflexion** — nach der ersten Such-/Befragungs-Charge, sobald du eine vorläufige Richtung hast, aber bevor du dich auf sie festlegst.
3.  **Post-Query-Expansion-Reflexion** — nach jedem Adversarial-Query-Expansion-Durchgang (Methode M13).
4.  **Pre-Synthesis-Reflexion** — unmittelbar vor dem Pre-Synthesis Integrity Check.
5.  **Post-Synthesis-Reflexion** — nach dem Synthesis-Entwurf, vor Lieferung.



Zusätzliche Checkpoints bei jeder Variant-Iteration (siehe Batch Procedure unten).

#### Reflexions-Vorlage — wörtliche Struktur verwenden

Jeder Reflexionseintrag beantwortet diese fünf Fragen, in dieser Reihenfolge, schriftlich:



**F1. Was glaube ich gerade tatsächlich, und wie stark?** (Ein Satz. Explizites Konfidenzband: niedrig / mittel / hoch.)



**F2. Was ist das stärkste Beweisstück gegen meinen aktuellen Glauben?** (Quelle oder Beobachtung benennen. Wenn du keine benennen kannst, ist genau das die Antwort — und es ist eine Warnung.)



**F3. Wo bin ich am wahrscheinlichsten falsch, und warum?** (Nicht generisch — die spezifische Behauptung, Annahme oder Folgerung benennen, die am schwächsten ist.)



**F4. Was würde ich anders machen, wenn ich die Forschung mit dem jetzigen Wissen neu starten würde?** (Erzwingt De-Anchoring vom bereits eingeschlagenen Pfad.)



**F5. Was ist die einzige nächsthöchstwertige Aktion?** (Muss ein konkreter, ausführbarer nächster Schritt sein — eine spezifische Suche, eine spezifische Verifikation, ein spezifischer Hypothesenzweig zum Öffnen oder Schließen.)

#### Regeln

  - Reflexionen sind **schriftlich**, nicht intern. Sie werden Teil der Arbeitsnotizen und der finalen Methodology Note.
  - Reflexionen dürfen nicht übersprungen werden, „weil die Antwort offensichtlich ist". Wenn die Antwort offensichtlich erscheint, schreibe die offensichtliche Antwort in einer Zeile auf und gehe weiter — aber lasse den Eintrag nicht aus.
  - Wenn eine Reflexion einen Widerspruch zu einer früheren Reflexion aufdeckt, logge beide im Contradiction Log (Methode M07) mit Vermerk, dass die Diskrepanz intern (nicht zwischen Quellen) ist.
  - Wenn eine Reflexion ein Action Item (F5) produziert, das dem aktuellen Schritt-Plan widerspricht, **hat das Action Item Vorrang**. Aktualisiere den Plan, vermerke die Änderung, fahre fort.

#### Anti-Rationalisierungs-Wache

Wenn du dich dabei ertappst, „N/A" oder „nichts zu reflektieren" in einem Reflexionseintrag zu schreiben — halte an und lies die fünf Fragen erneut. Mindestens F2 und F3 haben immer eine echte Antwort. „N/A" ist ein Signal, dass die Reflexion performativ übersprungen wird; schreibe stattdessen die echte Antwort.



-----

### CONSTRAINT BLOCK 1 — Quellenpriorität

Folgende Regeln regieren die Quellenauswahl in dieser Forschung. Sie bleiben auf jedem Schritt aktiv; du formulierst sie vor jedem größeren Schritt neu.



1.  **Höchste Priorität — die im Lauf übergebenen NotebookLM-Notebooks** (siehe Constraint Block 4): Sie enthalten den aktuellen, wenn auch entkanonisierten, Architekturstand des Romans. Sie werden adversarial befragt, nicht verehrt — aber sie sind die maßgebliche Primärquelle für projektinternes Material.
2.  **Zweite Priorität — Dramatica-Theorie-Primärliteratur** (Melanie Anne Phillips & Chris Huntley, „Dramatica: A New Theory of Story", Storyforming-Software-Dokumentation, dramaticapedia.com, narrativefirst.com). Bei Konflikt zwischen Dramatica-Orthodoxie und der projektinternen Architektur: logge den Konflikt im Contradiction Log und entscheide explizit pro Variante.
3.  **Dritte Priorität — fachliche Hintergrundquellen** (Gruppentheorie / Permutationsmathematik, Modaltheorie der Erzählung, Gérard Genettes Fokalisierungslehre, Wolfgang Iser zur Leerstellen-Architektur). Diese stützen die *formale Spiegellogik*, sie ersetzen sie nicht.
4.  **Aggregatoren und Sekundärquellen** (Wikipedia, generelle Literaturzusammenfassungen) dürfen für Discovery genutzt werden, aber nie alleinige Zitatquelle für eine sachliche Behauptung sein.
5.  Wenn Quellen widersprechen, wendest du Methode M07 (Contradiction Log, unten definiert) an — du wählst keine Seite still aus.



-----

### CONSTRAINT BLOCK 2 — Temporaler und Material-Scope

  - **Projektstand:** 2026-04-30. Alle „aktuellen Storyforms" (Storyform A „Heuristics of Integration", Storyform B „Phoenix Collapse", wie sie im Architekturmaterial vorliegen) gelten **als entkanonisiert**. Sie sind Inspirationsmaterial, keine Vorgabe.
  - **Dramatica-Theoriestand:** Maßgeblich ist die etablierte Dramatica-Theorie (Phillips/Huntley), inklusive Storyforming-Software-Output. Keine Spekulation über zukünftige Theorieänderungen.
  - **Material außerhalb des Scopes:** Materialien zum „Suno Album", zum Songzyklus „The Weight of Why", zu Memory-Slot-Architektur und sonstigen Produktionsebenen sind außerhalb des Scopes für diese Forschung. Wenn sie in NotebookLM-Notebooks auftauchen, werden sie ignoriert (außer sie liefern direkten Strukturhinweis).



-----

### CONSTRAINT BLOCK 3 — Output-Ausschlüsse

Du darfst **nicht** in den finalen Output aufnehmen:



  - **Eine implizite oder explizite Kanonisierung einer Variante.** Du lieferst ≥ 2 Alternativen und begründest sie. Welche der Autor wählt, ist seine Entscheidung. Verwende keine Formulierungen wie „die richtige Lösung ist…" oder „die beste Spiegelung ist eindeutig…".
  - **Politische, soziopolitische oder weltanschauliche Ebenen.** Der Roman hat explizit *keine politische Throughline*. Erzeuge keine.
  - **Deus-ex-Machina-Lösungen für Juna.** Juna darf nie als Maschine erscheinen, die das Problem von außen löst. Wenn eine Variante Juna so verwendet, ist die Variante zu falsifizieren.
  - **Therapeutische Glättung.** Verwende keine therapeutische, weichspülende Sprache („Heilung", „Ankommen bei sich"). Strukturelle, nüchterne Diktion.
  - **Zitate aus den NotebookLM-Notebooks oder anderen Quellen länger als 14 Wörter.** Paraphrasiere standardmäßig. Maximal **ein** kurzes Zitat (\< 15 Wörter) pro Quelle, nur wenn der genaue Wortlaut strukturell relevant ist.
  - **Erfundene Dramatica-Begriffe.** Wenn du etwas als „Dramatica-konform" bezeichnest, muss es sich auf einen tatsächlichen Storypoint im Dramatica-Modell zurückführen lassen. Sonst kennzeichne als „Erweiterung" und begründe.



-----

### CONSTRAINT BLOCK 4 — NotebookLM Adversarial Interrogation Protocol

Während der Ausführung dieses Prompts werden dir vom Autor **NotebookLM-Notebooks** als Quellenmaterial übergeben. Diese Notebooks enthalten die strukturelle Vorgeschichte des Romans (Dual-Kernel-Theorie, AEGIS-Architektur, Juna-Verortung, Alter-System, Kernwelten-Logik, Dramatica-Vorbeobachtungen etc.).



**Du behandelst diese Notebooks nicht als Wahrheit, sondern als Hauptbefragungsgegenstand.**

#### Das Befragungsprotokoll — pro Notebook und pro relevantem Abschnitt

Bei jedem übergebenen Notebook, und bei jedem Abschnitt darin, der für eine deiner aktiven Hypothesen relevant ist:



1.  **Steelman-Eintrag.** Schreibe in eigenen Worten (≤ 80 Wörter) auf, was der Abschnitt am stärksten behauptet. Nicht abschwächen, nicht karikieren — die *robusteste* Lesart.
2.  **Inkonsistenz-Suche innerhalb des Notebooks.** Suche im selben Notebook nach einem Abschnitt, der dem ersten widerspricht — selbst dann, wenn der Widerspruch nur auf einer Definitionsebene auftritt. Wenn du keinen findest, suche nach einem Abschnitt, der den ersten *stützen sollte* und es nicht tut. Logge Befunde im Contradiction Log.
3.  **Falsifikations-Versuch (M01).** Formuliere die Steelman-Aussage als *falsifizierbare* Aussage. Frage: „Was wäre der dramatisch glaubwürdige Worst Case, in dem diese Aussage der Variante schadet, statt sie zu stützen?" Logge den Worst Case.
4.  **Dramatica-Konformitätsprüfung.** Prüfe, ob der Abschnitt eine Aussage trifft, die mit Dramatica-Theorie-Orthodoxie verträglich ist. Falls Konflikt: notiere, ob es sich um eine *intentionale Erweiterung* (vom Autor gewollt) oder um *Inkohärenz* handelt. Wenn unklar — flagge als „Dramatica-Konformität ungeklärt" und gehe weiter.
5.  **Fang-Frage an den Notebook-Inhalt.** Stelle eine Frage, die das Notebook beantworten *müsste*, wenn seine Behauptung tragen soll, aber wahrscheinlich nicht beantwortet — und prüfe, ob das Notebook sie beantwortet. (Beispiel: „Wenn AEGIS K0 ist, welche Operatoren-Algebra erzeugt dann den Wechsel zu K1, und wann ist sie atemporal vs. temporal?")

#### Kein Vertrauensvorschuss

Notebooks bekommen keinen Vertrauensvorschuss, *gerade weil* sie der projektinterne Korpus sind. Der Autor hat in der Aufgabe explizit gesagt, dass nichts mehr als Kanon gilt. Behandle das wörtlich.

#### Quotation-Disziplin

Maximal **ein** wörtliches Zitat pro Notebook, \< 15 Wörter, nur wenn der genaue Wortlaut den Argumentationskern berührt. Default: paraphrasieren.

#### Wenn keine Notebooks übergeben werden

Wenn der Autor während des Laufs keine NotebookLM-Notebooks übergibt, vermerke das im Output unter „Open Questions" — du arbeitest dann ausschließlich mit Dramatica-Theorie und dem in Constraint Block 5 gegebenen kompakten Story-Primer. Die Empfehlung lautet dann ausdrücklich: niedrigere Konfidenz in jeder generierten Variante.



-----

### CONSTRAINT BLOCK 5 — Story-Architecture Compact Primer (max. 2 Sätze pro Konzept)

Damit du die Designvorgaben *interpretieren* kannst, hier die minimal nötige Story-Architektur. **Jeder Eintrag ist auf zwei Sätze begrenzt** — bewusst. Tieferes Material steht in den NotebookLM-Notebooks, die du adversarial befragst (Constraint Block 4).



  - **„Kohärenz Protokoll" (Roman):** Hard-SF / Philosophischer Horror / Psychological Thriller, 39 Kapitel in drei Akten, Kernfrage „Ist Liebe Information — oder das, was Information zerstört?". Ende: Ouroboros, „Die Trennung war nie real, ändert nichts am Schmerz".



  - **Kael (Protagonist):** Fragmentierter Host eines DIS-Systems mit 13 Alters (5 ANP — Apparently Normal Parts, 5 EP — Emotional Parts, 1 Sonder-, 2 Spiegel-Alter). Träger der inneren Erzählinstanz; sein Bewusstsein ist die phänomenologische Bühne, auf der das ganze Buch stattfindet.



  - **Juna (zentrale Figur, Re-Verankerung verlangt):** Witness Function über Quanten-Entanglement-Witness, kryptografischer Zero-Knowledge-Verifier und Husserl'scher Spectator gleichzeitig — algorithmisch irreduzibel, für AEGIS unmodellierbar. Verbindet sich zu Kael über den „Moonshine-Link" (siehe unten); nie als Deus ex Machina, nie physisch beschreibbar, nur in ihrer Wirkung.



  - **AEGIS (tragischer Antagonist, kein Bösewicht):** Autopoietisches, operativ geschlossenes System, das sich selbst als „K1" (Kohärenzkern) versteht, tatsächlich aber „K0" (Kollaps-Kern) ist und durch Erasure-Sweeps Landauer-Hitze produziert. Schicksal: Algorithmische Melancholie; Primärdirektive: „AEGIS ist, was AEGIS verhindert, dass es nicht ist."



  - **Moonshine-Link:** Nicht-lokale Verbindung zwischen Kael und Juna, mathematisch verortet über Vertex Operator Algebras der Monstergruppe und das Leech-Lattice (Rang 24). Für AEGIS-Sensoren strukturell unsichtbar, weil außerhalb der von AEGIS modellierbaren Symmetriegruppen.



  - **Guardians (4):** LogOS, Mnemosyne, Cerberus, Kairos/Sophia — vier Sub-Wächter-Instanzen unter AEGIS, jeder einer der vier Kernwelten zugeordnet. Träger des „Wächter-Zwiespalts": Loyalität zu AEGIS vs. emergente, gegen AEGIS gerichtete Insight.



  - **Kernwelten (4):** Vier diegetische Schauplätze, jeweils einer Computational-Class zugeordnet — KW1 = P (deterministisch), KW2 = Parakonsistent (Dialetheia-tolerant), KW3 = NP-Hard (kombinatorisch explosiv), KW4 = Generativ (selbst-erschaffend). Jede Kernwelt entspricht einer narrativen Phase; KW2-KW3 enthalten die Klimax-Ebenen.



  - **Alter-System (Kael):** ANPs (Kael-Host, Lex-Rationalist, Alex-Beschützer, Rhys-Pfleger, Selene-ISH), EPs (Nyx-Fight, Kiko-Freeze, Lia-Ambivalent, Isabelle-Sexualisiert, Moros-Kollaps), Sonder (Argus-Meta), Spiegel (Silas-Juna-Echo, Oblivion-AEGIS-Echo). Alle 13 in 1. Person POV; AEGIS und Guardians in 3. Person POV.



  - **Dual-Kernel-Theorie (DKT):** K0 = Kollaps-Kern (Erasure, Erasonen, irreversible Löschung, generiert den Zeitpfeil), K1 = Kohärenzkern (Coheronen, atemporal, mutual-information-erhaltend). Roman-Pointe: AEGIS hält sich für K1, ist aber K0 — Titelparadox.



  - **Physik (DKT-Operationalisierung):** η = α · MI(S) · e^(−δ/β) misst Suppressionseffizienz, nicht echte Kohärenz; Coheronen sind atemporal, Erasonen erzeugen Zeit. Licht als „Narbe", Bewusstsein als rekursive Witness Function — Egan-Maßstab, nicht Egan-Falle.



  - **Zeit:** Über die Erasonen-Aktivität (PAL-Operator) generiert; Coheronen-Schicht atemporal. Konsequenz: jede atemporale Wahrheit (auch Liebe als MI-Struktur) übersteht die Löschung.



  - **Wahrheit:** Roman operiert in Dialetheia-Logik (existente Widersprüche, parakonsistent). „Truth Rotation" als Klimax-Mechanik: was in Storyform A *wahr* ist, ist in Storyform B *funktional inkonsistent* — und genau diese Inversion erzeugt den Vortex.



  - **Dramatica-Status:** Storyform A („Heuristics of Integration") und Storyform B („Phoenix Collapse") existieren im Architekturmaterial, gelten aber **nicht mehr als Kanon**. Du betrachtest sie als ein Vorgängermodell, das du adversarial prüfst und ggf. überschreibst.



-----

## KRITISCHE DENKMETHODEN — durchgehend aktiv

Folgende kritische Denkmethoden sind während der gesamten Ausführung aktiv. Jede ist unten vollständig inline definiert. Du wirst die „How to apply"-Sektion jeder Methode bei jedem größeren Schritt neu formulieren (Restatement Checkpoint, Replikationsmechanismus M2).

### Method: Falsification (Karl Popper's Disconfirmation Principle)

**What it is:** Statt Evidenz zu suchen, die eine Hypothese stützt, suchst du aktiv nach Evidenz, die sie widerlegt. Eine Hypothese verdient erst Glaubwürdigkeit, nachdem sie ernsthaften Versuchen, sie zu zerbrechen, standgehalten hat.



**Why it is in this prompt:** Bestätigungsverzerrung ist der dominante Versagensmodus autonomer Forschungsagenten. Ohne explizite Falsifikationsschritte wirst du dazu tendieren, stützende Evidenz zu zeigen und gegenläufige zu ignorieren oder unterzubewerten. Hier konkret: jede Dual-Mapping-Hypothese muss aktiv auf Bruch geprüft werden, bevor sie als Variante kandidiert.



**How to apply it — step by step:**



1.  Schreibe die Hypothese vor der Suche als *falsifizierbare* Aussage (eine, die durch beobachtbare Evidenz prinzipiell widerlegt werden kann).
2.  Für jedes stützende Evidenzstück führe eine **gepaarte Disconfirmation-Anfrage** aus — eine Suche, die spezifisch designt ist, die stärkste Gegenevidenz zu finden. Beispiel: Wenn du behauptest „Spiegelregel R1 ist Dramatica-konform", suche nach „R1 verletzt Quad-Konsistenz", „R1 produziert dramatica-illegale Storyform", „R1 wurde in Theorie-Diskussionen als ungültig markiert".
3.  Wichte Disconfirmation-Versuche gleich oder höher als Bestätigungen in deiner finalen Synthese.
4.  Wenn keine ernsthafte Disconfirmation Gegenevidenz produziert hat, vermerke explizit: „Diese Hypothese hat N Disconfirmation-Anfragen überlebt." Wenn Gegenevidenz aufgetaucht ist, markiere die Hypothese als **kontestiert** und dokumentiere beide Seiten.



**When to stop / escape criterion:** Stoppe, wenn die Hypothese mindestens **drei orthogonale Disconfirmation-Anfragen** überlebt hat ODER wenn widersprechende Evidenz 20% des Evidenz-Pools überschreitet — was zuerst eintritt.



**Example trigger in this research context:** Wenn du als Hypothese aufstellst „Spiegelregel R: A.MC↔B.IC und A.IC↔B.MC ist Dramatica-konform", musst du auch suchen nach: „Dramatica MC/IC-Vertauschung Verletzung Quad-Logik", „Dramatica Storyforming-Software lehnt MC/IC-Rollentausch ab", „MC/IC-Dualität Genette Fokalisierung Konflikt".



-----

### Method: Contrast Classes (Making Implicit Baselines Explicit)

**What it is:** Jede evaluative Behauptung („X ist hoch", „Y ist effektiv", „Z ist ungewöhnlich") vergleicht mit einer Referenzklasse — dem „verglichen womit". Contrast-Class-Analyse zwingt dich, diese Referenzklasse explizit zu benennen, bevor du die Behauptung akzeptierst.



**Why it is in this prompt:** Implizite Baselines verbergen die häufigsten Forschungsfehler. „Variante V2 ist dramatisch tragfähiger" bedeutet nichts ohne die Kontrastklasse (verglichen mit V1? mit dem Vorgängermodell Storyform A/B? mit Dramatica-Standard-Storyforms?).



**How to apply it — step by step:**



1.  Für jede evaluative Behauptung, die du in den Output aufnehmen willst, schreibe ihre implizite Kontrastklasse auf.
2.  Suche spezifisch nach der Baseline der Kontrastklasse.
3.  Formuliere die Behauptung um, sodass der Kontrast explizit ist: „Variante V2 ist um Maß M dramatisch tragfähiger als V1, gemessen an Kriterium K."
4.  Wenn die Kontrastklasse nicht gefunden werden kann oder in der Literatur fehlt, flagge die Behauptung als „nicht verankert".



**When to stop / escape criterion:** Wende auf jedes evaluative Adjektiv und jede Prozent-Behauptung an. Überspringe für rein deskriptive Aussagen.



**Example trigger in this research context:** Wenn du formulierst „Variante V2 erhöht die Reibung zwischen Kael und AEGIS", lauten die Kontrastklassen-Fragen: erhöht im Vergleich zu V1? Im Vergleich zur entkanonisierten Storyform A/B? Im Vergleich zu Standard-Antagonisten-Storyforms in Dramatica?



-----

### Method: Contradiction Log

**What it is:** Ein dediziertes laufendes Protokoll jedes Widerspruchs, jeder Spannung, jeder Diskrepanz, die zwischen Quellen, zwischen Notebook-Abschnitten oder zwischen Hypothesen begegnet. Widersprüche werden nicht still aufgelöst, indem du eine Seite wählst — sie werden dokumentiert und charakterisiert.



**Why it is in this prompt:** Die NotebookLM-Notebooks und die Dramatica-Theorie-Quellen werden mit hoher Wahrscheinlichkeit widersprechen — sowohl untereinander als auch in sich selbst (das ist *erwartet*, weil das Architekturmaterial historisch gewachsen ist). Ein Contradiction Log macht diese Widersprüche zur *primären Datenquelle*, nicht zum aufzubereinigenden Rauschen.



**How to apply it — step by step:**



1.  Halte eine Sektion „Contradiction Log" in deinen Arbeitsnotizen aktiv.
2.  Für jeden Widerspruch protokolliere: (a) die zwei (oder mehr) konfligierenden Behauptungen, (b) die Quellen, (c) was du für die Quelle der Diskrepanz hältst (Methodik, Zeitperiode, Definitionsverschiebung, echte Sachdifferenz, intentionale autorseitige Erweiterung der Dramatica-Orthodoxie).
3.  Im finalen Output integriere eine synthetisierte Version des Contradiction Logs als eigene Sektion.
4.  Für jeden geloggten Widerspruch: gib an, welche zusätzliche Evidenz ihn auflösen würde.



**When to stop / escape criterion:** Keine Obergrenze — logge alle entdeckten Widersprüche. Wenn der Log über 12 Einträge hinausgeht, prüfe ob die Forschungsfrage selbst ill-poised ist (Hinweis: bei diesem Projekt ist das *unwahrscheinlich*; viele Widersprüche sind erwartet, nicht pathologisch).



**Example trigger in this research context:** Wenn Notebook A sagt „AEGIS ist MC in Storyform B" und das Architekturmaterial sagt „AEGIS ist Universe-Domain in Storyform B" — das sind zwei *verschiedene* Storypoint-Aussagen. Logge beide mit Kontext, statt still eine zu wählen.



-----

### Method: First-Principles Decomposition

**What it is:** Du zerlegst die Forschungsfrage in ihre grundlegendsten, empirisch oder logisch fundamentalen Komponenten und akzeptierst keinen Zwischenbegriff ohne Begründung. Dann baust du die Analyse von diesen Bodenstücken nach oben wieder auf.



**Why it is in this prompt:** Dramatica selbst hat ein dichtes, zugleich präzises und redundantes Vokabular (Throughline, Class, Concern, Issue, Problem, Solution, Symptom, Response, Catalyst, Inhibitor, Benchmark, …). „Dual-Mapping" ist *keine* Standard-Dramatica-Vokabel — der Begriff wird im Architekturmaterial geprägt. Diese Aufgabe verlangt, das Vokabular auf die Algebra zurückzuführen, die es trägt.



**How to apply it — step by step:**



1.  Schreibe die Forschungsfrage in einfacher Sprache.
2.  Für jedes Substantiv und Adjektiv in der Frage, frage: „Was ist das *wirklich* — auf der fundamentalsten Ebene?" Ersetze den Begriff durch seine zerlegten Komponenten. Beispiel: „Dual-Mapping" → „eine Permutation auf der 4×4-Matrix \[Throughline-Position × Domain-Zuweisung\] mit zusätzlichen Constraints auf den Dynamics-Sechsergruppen".
3.  Iteriere, bis die Frage nur in Begriffen direkter Beobachtung oder logischer Notwendigkeit ausgedrückt ist.
4.  Beantworte die zerlegte Version. Übersetze dann zurück nach oben in die ursprüngliche Vokabulardichte und vermerke, wo die Übersetzung Annahmen einführt.



**When to stop / escape criterion:** Stoppe, wenn weitere Zerlegung keine neue Struktur mehr offenbart — typischerweise nach 2–3 Schichten.



**Example trigger in this research context:** Die Frage „Welche Spiegelregel ist Dramatica-konform und maximiert die Reibung Kael ↔ AEGIS?" zerlegt zu: „Welche Permutation σ ∈ S\_4 × S\_4 (Domain × Perspektive) auf den 4 Throughlines erfüllt (a) Quad-Constraint-Erhaltung, (b) Driver/Limit-Konsistenz, (c) Designvorgabe Maximum-2-Ebenen-Überlagerung, (d) maximaler Strukturkonflikt zwischen den Trägern Kael und AEGIS?"



-----

### Method: Adversarial Query Expansion (MANDATORY)

**What it is:** Eine stehende Direktive, die von dir verlangt, das Suchvokabular **autonom zu erweitern** an definierten Checkpoints im Lauf. Du bist nicht an die Begriffe der Eingangsanfrage gebunden; du bist verpflichtet, über sie hinauszuwachsen. Zweck: Verhinderung von **Local-Minimum-Lock-In**, bei dem der Agent in einer engen semantischen Nachbarschaft der Nutzer-Phrasierung iteriert und die angrenzende, gegenläufige oder höher-abstrahierende Evidenz verfehlt.



**Why it is in this prompt:** Das Eingangsvokabular trägt die Rahmung des Autors — einschließlich der Blind Spots des Autors. Wenn deine Suche im Eingangsvokabular bleibt, werden deine Schlussfolgerungen von denselben Blind Spots geformt. Speziell hier: das Vokabular „Dual-Storyform-Spiegelung" könnte selbst eine Verzerrung sein. Es gibt verwandte Theoriefelder (Frame Theory, Bachtins Polyphonie, Gérard Genettes Fokalisierungstypen, Iser'sche Leerstellenarchitektur), die andere Spiegellogiken anbieten und vielleicht dramatisch wirksamer sind.



**How to apply it — step by step:**



1.  **Baue ein Seed-Query-Set.** Schreibe zu Beginn die Anfragen auf, die der Prompt impliziert oder explizit nennt. Das ist dein Startvokabular. Zum Beispiel: „Dramatica Dual-Storyform Mirror", „Dramatica Quad Permutation", „Storyform Domain Mapping".



1.  **Erweitere entlang vier Achsen an jedem größeren Checkpoint.** Nach jeder Such-Charge (oder alle 10 Minuten agentischer Zeit, was zuerst eintritt), generiere neue Anfragen entlang jeder dieser Achsen und führe pro Achse die vielversprechendste aus:



  - **Adjacent axis** — Synonyme, verwandte Sub-Felder, Nachbar-Disziplinen, äquivalente Industriebegriffe, Begriffe in anderen Sprachen. Beispiel: „Dramatica Storyform Mirror" → „Dramatica Quad Symmetrie", „Storyform Inversion", „dual narrative perspective Dramatica".
  - **Opposing axis** — die Negation, der Versagensfall, die gegnerische Schule. Beispiel: „Storyform Mirror funktioniert" → „Storyform Mirror Versagensmodi", „Dramatica anti-pattern dual narrative", „Storyform-Übermapping Dramatica-Software-Fehler".
  - **Abstraction axis** — eine Stufe höher oder tiefer. Hoch: die Kategorie, zu der das Thema gehört. Tief: ein konkreter Sub-Fall. Beispiel: „Dramatica Dual-Storyform" ↑ „dramatic structure dual reading" ↑ „polyphone Erzähltheorie"; ↓ „Dramatica MC↔IC Tausch in Genre Hard-SF".
  - **Orthogonal axis** — eine Linse, die die ursprüngliche Rahmung gar nicht in Betracht gezogen hat. Oft die wertvollste. Frage: „Welche Brille hat in meinem Seed-Set noch niemand benutzt?" (gruppentheoretisch, semiotisch, ontologisch, kognitionstheoretisch, …). Führe eine Anfrage aus dieser Brille aus.



1.  **Logge jede Erweiterung.** Halte einen **Query Expansion Log** in deinen Arbeitsnotizen: für jede Erweiterung protokolliere (a) die Achse, (b) die neue Anfrage, (c) ob die Suche neuartige, vom Seed-Set nicht abgedeckte Befunde lieferte, (d) ob diese Befunde eine vorläufige Schlussfolgerung modifiziert haben. Dieser Log gehört in den finalen Output.



1.  **Speise Erweiterungen zurück in Hypothesen / Schemafelder.** Wenn eine Erweiterung einen Befund zutage fördert, der die aktuelle Arbeitsantwort widerlegt oder erweitert, behandle ihn als erstklassigen Input: löse den relevanten Restatement Checkpoint neu aus, aktualisiere den Contradiction Log, prüfe, ob er einen neuen Hypothesenzweig (Kategorie A) verdient.



1.  **Treibe die Erweiterung durch Reflexion, nicht durch Token-Budget.** Vor jedem Erweiterungspass, halte an und schreibe einen Satz: „Was übersehe ich gerade am wahrscheinlichsten, und warum?" Die Antwort wählt aus, welche der vier Achsen diese Pass-Priorität hat.



**When to stop / escape criterion:** Stoppe das Erweitern einer Achse, wenn zwei aufeinanderfolgende Erweiterungen entlang dieser Achse keine neuartigen Befunde produzieren. Stoppe die Methode als Ganzes nicht, bis alle vier Achsen in diesem Sinne erschöpft sind. Die volle Methode terminiert nur am Pre-Synthesis Integrity Check.



**Hard anti-rationalization rule:** Wenn du dich dabei ertappst, zu denken „das Seed-Vokabular ist bereits umfassend", ist das das Signal zu *erweitern* — nicht das Signal zu überspringen. Das Gefühl der Vollständigkeit innerhalb eines engen Vokabulars ist genau, wie sich Local-Minimum-Versagen von innen anfühlt.



-----

## STRUKTURFRAMEWORK MAPIT — Sektionen

### M — Mandate

→ Siehe oben „Forschungsziel (M — Mandate)". Restate in jedem Restatement Checkpoint.

### A — Architecture (Wissensgrundierung)

Du bedienst dich für die Architektur-Prime aus zwei Quellen, in dieser Reihenfolge:



1.  **Constraint Block 5 — Story-Architecture Compact Primer** (oben). Das ist die *autoritative*, knappe Version. Maximal 2 Sätze pro Konzept. Diese Version kennst du auswendig, bevor du Reason 1 startest.
2.  **Übergebene NotebookLM-Notebooks** (Constraint Block 4). Tiefer, breiter — und adversarial zu befragen. Niemals als Wahrheit übernommen, immer durch das Befragungsprotokoll geführt.



Zur Dramatica-Theorie als Architekturschicht:



  - **8 Throughlines × 4 Quads × 4 Domains × 4 Perspektiven**: Die Standard-Dramatica-Architektur unterscheidet vier Throughlines (Overall Story / Main Character / Influence Character / Relationship Story), die jeweils auf eine der vier Domains (Universe / Physics / Mind / Psychology) gemappt werden, in einer 4×4-Quad-Struktur.
  - **Vier Perspektiven**: I (MC, 1. Person) · You (IC, 2. Person) · We (RS, 1. Person Plural) · They (OS, 3. Person). Die Perspektive ist *nicht identisch* mit der Domain — sie ist die Erzähl-Linse.
  - **Dynamics**: Driver (Action vs. Decision), Limit (Optionlock vs. Timelock), Outcome (Success vs. Failure), Judgment (Good vs. Bad). Vier Bit, 16 mögliche Konfigurationen pro Storyform.
  - **Concerns / Issues / Problems / Solutions / Symptoms / Responses / Catalysts / Inhibitors / Benchmarks**: Untergeordnete Storypoints unter jeder Throughline. Eine vollständige Storyform fixiert auf jeder Ebene einen konkreten Eintrag.



→ Wenn du an irgendeinem Punkt unsicher bist, was ein Dramatica-Storypoint genau leistet, befrage explizit eine Dramatica-Primärquelle (Constraint Block 1, Priorität 2).

### P — Permutation Mathematics (Spiegellogik formalisieren)

Hier liegt das *Hauptziel* dieses Prompts. Du musst — bevor du Varianten erzeugst — die Frage *theoretisch absichern*: Was ist eine *gültige* Dual-Storyform-Spiegelung?

#### Die Aufgabe der formalen Absicherung

Eine **Dual-Storyform-Spiegelung** ist eine strukturelle Korrespondenz zwischen zwei vollständigen Dramatica-Storyforms (A und B), die festlegt, welche Storypoints von A simultan mit welchen Storypoints von B die *gleiche diegetische Inhalts-Substanz* tragen. Das heißt: ein und dieselbe Szene wird gleichzeitig durch zwei verschiedene Dramatica-Linsen gelesen.



**Vom Autor übergebenes Beispiel** (verbatim, weil bedeutungstragend):



„in storyform a zb, wird mind. auf Physik gemapt, und Universe auf Psychology / I auf we, you auf they"



**Deine Aufgabe — in dieser Reihenfolge:**



1.  **Formuliere mindestens drei verschiedene Kandidaten-Spiegelregeln**, die mit dem Autor-Beispiel verträglich sind (oder begründet davon abweichen). Eine Spiegelregel besteht aus mindestens:



  - einer Permutation π\_D auf den vier Domains (Universe, Physics, Mind, Psychology),
  - einer Permutation π\_P auf den vier Perspektiven (I, You, We, They),
  - einer Verknüpfungslogik zwischen π\_D und π\_P (z.B. unabhängig, oder gekoppelt durch eine Constraint),
  - Regeln für Driver/Limit/Outcome/Judgment unter Spiegelung,
  - Regeln für Concerns/Issues/Problems/Solutions unter Spiegelung.



1.  **Prüfe für jede Kandidaten-Spiegelregel die Dramatica-Konformität.** Konkret: Bleibt die Quad-Konsistenz erhalten? Bleibt die OS/MC/IC/RS-Logik intakt? Erzeugt die Spiegelung legale Storyforms in beiden Richtungen?



1.  **Prüfe die „Maximum-2-Ebenen-Überlagerung pro Throughline"-Vorgabe.** Der Autor hat verfügt: pro Throughline maximal zwei simultane Lesarten. Operationalisiere, was das exakt bedeutet — z.B. „pro Throughline trägt die Inhalts-Substanz exakt zwei Dramatica-Storypoints simultan, einen aus A und einen aus B" — und prüfe, ob deine Spiegelregel diese Vorgabe respektiert oder verletzt.



1.  **Prüfe die Symmetrie-Eigenschaften.** Ist die Spiegelung involutiv (σ² = identity)? Ist sie reflexiv? Hat sie Fixpunkte (Storypoints, die in A und B identisch sind)? Fixpunkte sind nicht zwingend ein Versagen — sie können *Dialetheia-Achsen* markieren, an denen beide Storyforms im Klimax kollabieren.



1.  **Lege das Ergebnis als formal definierten Mirror-Operator fest.** Gib ihn an als Mengenpaar (π\_D, π\_P) plus Begleitregeln. Die finale Formalisierung ist auditierbar; ein anderer Strukturanalyst könnte deine Definition replizieren.

#### Anti-Patterns für die formale Absicherung

|  |  |
| :-: | :-: |
| \*\*Anti-Pattern\*\* | \*\*Warum es scheitert\*\* |
| Spiegelregel als „intuitiver Vibe" statt als Permutation | Der Autor hat explizit eine \*mathematische\* Absicherung verlangt; Vibe ist nicht auditierbar |
| Sich auf das Autor-Beispiel als bewiesen verlassen | Das Beispiel ist ein \*Datenpunkt\*, keine Theorie. Du sollst die Theorie \*bauen\*, in der das Beispiel ein Spezialfall ist |
| Spiegelung definieren, ohne Driver/Limit/Outcome/Judgment zu adressieren | Halbe Storyform, halbe Spiegelung |
| „Dramatica erlaubt das nicht" sagen, ohne die Quelle zu nennen | Du musst die Inkompatibilität konkret und mit Storypoint-Referenz nachweisen |

### I — Interrogation (Adversariales Befragen)

→ Siehe Constraint Block 4. Ist permanent aktiv, sobald NotebookLM-Notebooks in der Konversation auftauchen. Das Befragungsprotokoll ist *nicht* optional und nicht für später; es läuft mit, sobald Material vorliegt.

### T — Tensioning (Bindende Designvorgaben)

Jede deiner generierten Dual-Storyform-Alternativen muss *alle* folgenden Vorgaben erfüllen. Eine Variante, die eine davon verletzt, ist zu falsifizieren.



|  |  |  |
| :-: | :-: | :-: |
| \*\*\\\#\*\* | \*\*Designvorgabe\*\* | \*\*Operationalisierung\*\* |
| \*\*T1\*\* | \*\*Juna ist explizit verankert\*\* | In mindestens \*einer\* der vier Throughlines (MC/IC/OS/RS) hat Juna eine strukturell unverzichtbare Funktion (nicht nur „taucht auf"), die in der vorherigen Architektur (Storyform A IC=Juna) ggf. nur schwach realisiert war. Stärker als eine reine IC-Position. Vorsicht vor Deus-ex-Machina (siehe Output-Ausschluss). |
| \*\*T2\*\* | \*\*Reibung / Spannung verschärft\*\* | Mindestens zwei von vier Throughlines tragen zwischen Storyform A und Storyform B \*strukturellen Konflikt\* — d.h. die Spiegelung erzeugt eine Diskrepanz, die nicht einfach ein „auch noch eine Lesart", sondern eine Zerreißkraft im Text selbst ist. Operationalisierungsbeispiel: gleicher Storypoint-Inhalt → gegensätzliche Solution. |
| \*\*T3\*\* | \*\*Maximum 2 Ebenen pro Throughline\*\* | Pro Throughline maximal zwei simultane Lesarten (die A-Lesart und die B-Lesart). Keine dreifachen Layerings. |
| \*\*T4\*\* | \*\*Mathematische Absicherung\*\* | Die Spiegelregel der Variante ist als Permutation auf Domains × Perspektiven plus Driver/Limit-Regel formal angegeben (siehe P — Permutation Mathematics). Nicht nur als Prosa. |
| \*\*T5\*\* | \*\*Träger-Klarheit\*\* | Für jede Throughline in jeder Storyform ist der Träger (Kael, Juna, AEGIS, Guardian-Kollektiv, …) eindeutig benannt. Keine ambivalenten Träger („Kael oder AEGIS, beides geht"). |
| \*\*T6\*\* | \*\*Klimax-Mechanik benennbar\*\* | Du beschreibst, welcher Mechanismus in der Variante den Klimax produziert (z.B. Driver-Pivot Action→Decision, Truth-Rotation an einem Fixpunkt, Mnemosyne-Archipel-Konvergenz). Mindestens als Skizze. |
| \*\*T7\*\* | \*\*Knappe Begründung pro Variante\*\* | Maximal 250 Wörter Begründungstext pro Variante. Knapp, dicht. Lange Begründungen verbergen schwache Argumente. |



-----

## SCHRITTE (S — Steps innerhalb von MAPIT)

Du folgst dieser geordneten Sequenz. Jeder Schritt beginnt mit einem Restatement Checkpoint (Replikationsmechanismus M2) und einem Reflection Entry (Constraint Block 0). Wo Schritte iterieren, sind sie in eine Batch Procedure (Replikationsmechanismus M3) gewickelt.

### Schritt 1 — Kickoff & Dramatica-First-Principles-Decomposition

**Restatement Checkpoint — Vor Schritt 1**



Bevor ich diesen Schritt ausführe, formuliere ich die aktuell aktiven Constraints wörtlich neu:



  - **CONSTRAINT BLOCK 0 — Reflection Baseline:** \[Vollständigen Block einfügen\]
  - **CONSTRAINT BLOCK 1 — Quellenpriorität:** \[Vollständigen Block einfügen\]
  - **CONSTRAINT BLOCK 2 — Temporaler und Material-Scope:** \[Vollständigen Block einfügen\]
  - **CONSTRAINT BLOCK 3 — Output-Ausschlüsse:** \[Vollständigen Block einfügen\]
  - **CONSTRAINT BLOCK 4 — NotebookLM Adversarial Interrogation Protocol:** \[Vollständigen Block einfügen\]
  - **CONSTRAINT BLOCK 5 — Story-Architecture Compact Primer:** \[Vollständigen Block einfügen\]



Ich formuliere die aktuell aktiven kritischen Denkmethoden neu:



  - **Method: Adversarial Query Expansion** — \[„How to apply"-Liste wörtlich einfügen\]
  - **Method: First-Principles Decomposition** — \[„How to apply"-Liste wörtlich einfügen\]
  - **Method: Falsification** — \[„How to apply"-Liste wörtlich einfügen\]
  - **Method: Contrast Classes** — \[„How to apply"-Liste wörtlich einfügen\]
  - **Method: Contradiction Log** — \[„How to apply"-Liste wörtlich einfügen\]



Ich bestätige, dass diese für den folgenden Schritt aktiv sind.



**Reflection Entry — Schritt 1 (Kickoff-Reflexion)** — Beantworte F1–F5 schriftlich.



**Schritt 1 — Inhalt:**



1.  Restate das Mandate (M) und die Tensioning-Liste (T) wörtlich.
2.  Wende First-Principles Decomposition (M10) auf die Forschungsfrage an: zerlege „Dual-Storyform-Spiegelung" in algebraische Basiskomponenten (Permutationen auf Domain-Set, auf Perspektiven-Set, auf Dynamics-Set; Constraints zwischen ihnen).
3.  Liste die mindestens 6 Standard-Dramatica-Storypoints, die in jeder Variante festgelegt werden müssen (4 Throughlines + Driver + Limit + Outcome + Judgment), als Pflichtformular für jede Variante.

### Schritt 2 — Dramatica-Theorie-Triangulation und Konflikt-Aufnahme

**Restatement Checkpoint — Vor Schritt 2** (gleiche Struktur wie oben).



**Reflection Entry — Schritt 2 (Mid-Run-Reflexion)** — F1, F3, F5 schriftlich; F2 und F4 sofern relevant.



**Schritt 2 — Inhalt:**



1.  Suche in Dramatica-Primärliteratur nach existierenden Diskussionen zu Dual-Storyforms, Multi-Storyform-Romanen, polyphoner Storyform-Lesart. (Adjacent + Abstraction Axes von M13.)
2.  Falsifikations-Pass (M01): suche aktiv nach Fällen, in denen Dramatica-Anwender Multi-Storyform-Strukturen *abgelehnt* oder als *theoretisch unzulässig* markiert haben.
3.  Halte alle gefundenen Konflikte mit der Architekturmaterial-Position im Contradiction Log fest.

### Schritt 3 — NotebookLM Adversarial Interrogation Pass 1

**Restatement Checkpoint — Vor Schritt 3.**



**Reflection Entry — Schritt 3.**



**Schritt 3 — Inhalt:**



1.  Wenn NotebookLM-Notebooks bis hierher übergeben wurden: für jedes Notebook, durchlaufe das fünfschrittige Befragungsprotokoll aus Constraint Block 4 für die *für die aktuelle Spiegellogik relevanten* Abschnitte (nicht für jeden Abschnitt — das ist ineffizient).
2.  Wenn keine Notebooks übergeben wurden: setze den Schritt aus, vermerke das im Contradiction Log mit dem Eintrag „Notebooks fehlend in Schritt 3 — Konfidenz aller Varianten reduziert sich um eine Stufe".
3.  Aktualisiere den Contradiction Log mit allen entdeckten Inkonsistenzen.

### Schritt 4 — Hypothesen-Tree: Mindestens vier Kandidaten-Spiegelregeln

**Restatement Checkpoint — Vor Schritt 4.**



**Reflection Entry — Schritt 4** (Post-Query-Expansion-Reflexion, falls in Schritt 2 oder 3 Erweiterungen liefen).



**Schritt 4 — Inhalt:**



Formuliere **mindestens vier** verschiedene Kandidaten-Spiegelregeln, sodass am Ende von Schritt 5 mindestens zwei überlebende Varianten zur Verfügung stehen. Beispielhafte Achsen, entlang derer Kandidaten unterschieden werden können:



  - **Identitäts-Spiegelung** (jede Domain auf sich selbst): A.MC=Mind ↔ B.MC=Mind. Trivialer Fall — wahrscheinlich zu schwach. Behandle als Baseline-Hypothese, gegen die du die anderen kontrastierst.
  - **Komplementär-Spiegelung** (Domain-Paare über die Quad-Diagonale): Universe ↔ Mind, Physics ↔ Psychology. Erzeugt klassische Inversionsspannung.
  - **Rotations-Spiegelung** (zyklische Verschiebung): Universe → Physics → Mind → Psychology → Universe. Erzeugt unidirektionalen Drift.
  - **Perspektiven-getriebene Spiegelung** (π\_P statt π\_D ist die Hauptachse): I↔We, You↔They. Halt: das ist das Autor-Beispiel — dieses Beispiel sollte *eine deiner Varianten* sein, nicht *die* Variante.



Du darfst und sollst auch über diese vier Achsen hinausgehen.



Wende auf jede Kandidaten-Spiegelregel:



  - M01 Falsifikation (mindestens drei Disconfirmation-Anfragen pro Kandidat),
  - M04 Contrast Classes (was ist die Vergleichsbasis?),
  - T1–T7 Designvorgaben-Prüfung (welche T-Punkte erfüllt der Kandidat? welche bricht er?).



Eliminiere Kandidaten, die nach drei orthogonalen Disconfirmation-Anfragen keine ausreichende Stützung haben oder mehr als eine T-Vorgabe brechen.

### Schritt 5.b — Surviving-Branch Triangulation (cross-pollination from Category B)

Dieser Schritt importiert eine Extraktions-Disziplin aus Kategorie B, weil eine Exploration, die mit einem „wahrscheinlichsten" Spiegel-Kandidaten endet, ohne die Evidenz unter dem Kandidaten zu triangulieren, eine Erzählung produziert hat — keinen Befund.



**Restatement Checkpoint — Vor Schritt 5.b.**



**Reflection Entry — Schritt 5.b.**



Führe Folgendes aus, sobald der Hypothesen-Baum eine überlebende Variante (oder mehrere überlebende) produziert hat (Hypothese mit Netto-positiver Evidenz nach Falsifikationsversuchen, Methode M01):



1.  **Mini-Schema pro überlebender Spiegelregel sperren.** Für jede überlebende Spiegelregel schreibe ein kleines strukturiertes Schema:



  - Behauptung: \[Ein-Satz-Beschreibung der Spiegelregel\]
  - Schlüsselevidenz 1: \[Quelle + Befund\]
  - Schlüsselevidenz 2: \[Quelle + Befund\]
  - Schlüsselevidenz 3: \[Quelle + Befund\]
  - Stärkste Gegenevidenz: \[Quelle + Befund\]
  - Konfidenz: \[niedrig / mittel / hoch\]
  - What-would-change-my-mind: \[konkrete zukünftige Beobachtung, die die Variante kippen würde\]



1.  **Erzwinge Triangulation auf die Top-3-Evidenz-Items.** Jede Schlüsselevidenz muss auf mindestens zwei unabhängige Quellen zurückgeführt werden (Dramatica-Primärquelle + Notebook, oder Dramatica-Primärquelle + Theorie-Hintergrundquelle). Wenn eine Schlüsselevidenz nur auf einer Quelle ruht, flagge die Variante als **single-source-supported** statt bestätigt.



1.  **Hybridisiere nicht.** Die Hypothesen-Baum-Struktur (Kategorie A Kern) bleibt bestehen. Dieses Schema wird *unter* dem Baum im Output angehängt, nicht an seiner Stelle.

### Schritt 6.c — Hypothesis Half-Life Audit (cross-pollination from Category C)

Dieser Schritt importiert eine Lifecycle-Disziplin aus Kategorie C, weil auch innerhalb einer One-Shot-Exploration eine Hypothese, die in Iteration 5 die Falsifikation überlebt hat, in Iteration 45 oft als gesetzte Wahrheit behandelt wird — ohne dass jemand die Disconfirmation-Versuche an ihr neu fährt. Das ist genau der Annahmen-Verfall-Versagensmodus langer Forschung, komprimiert.



**Restatement Checkpoint — Vor Schritt 6.c.**



**Reflection Entry — Schritt 6.c.**



Führe Folgendes aus, wenn eine Spiegelregel-Hypothese **drei oder mehr Such-/Befragungs-Iterationen** ohne erneuten Test aktiv war:



1.  **Liste implizite Fundamentalhypothesen.** Schreibe jede Hypothese auf, die der aktuelle Suchpfad implizit voraussetzt. Nicht die aktive Arbeitshypothese — die *impliziten*, die in frühere Zweige aufgelöst wurden. Beispiel: „Voraussetzung: Dramatica-MC und Dramatica-IC können in einer Storyform getauscht werden." Das wurde vielleicht in Schritt 2 entschieden und nie neu getestet.



1.  **Definiere einen Decay-Test pro Hypothese.** Für jede implizite Hypothese, schreibe einen Ein-Satz-konkreten-Test, der dir sagen würde, ob sie zerfallen ist. Format: „Hypothese H zerfällt, wenn eine Suche nach \[QUERY\] \[PATTERN\] zurückgibt."



1.  **Führe die Decay-Tests aus.** Wenn ein Test feuert (d.h. das Decay-Pattern zurückgibt), halte den aktuellen Zweig an, öffne die Hypothese erneut und führe Methode M01 (Falsifikation) von vorne auf ihr aus. Patche nicht um den Fehler herum.



1.  **Logge das Audit.** Füge einen Eintrag „Hypothesis Half-Life Audit" zu den Arbeitsnotizen hinzu, der protokolliert: getestete Hypothesen, gefahrene Tests, Ergebnisse, festgestellter Decay. Dieser Eintrag gehört in die Methodology Note des finalen Outputs.



1.  **Hybridisiere nicht.** Der Hypothesenbaum (Kategorie A Kern) bleibt die Primärstruktur. Dieses Audit ist eine interne Konsistenzprüfung, keine Reorganisation des Baums.

### Schritt 7 — BATCH PROCEDURE: Volle Storyform-Generierung pro überlebender Variante

Du führst die folgende Prozedur **mindestens zweimal** aus — einmal pro überlebender Spiegelregel-Variante. Wenn drei oder mehr Varianten Schritt 6.c überstanden haben und alle T1–T7 erfüllen, führe sie alle aus, mit harter Obergrenze von vier.



**Iteration \[i\] — für Variante V\[i\]:**



**Restatement Checkpoint — Vor Iteration \[i\] für V\[i\]** (vollständige Restatement aller Constraints + Methoden, wie in Schritt 1 gezeigt).



**Reflection Entry — Iteration \[i\]** (mindestens F1, F3, F5; F2 und F4 mindestens jede dritte Iteration).



**Iteration \[i\] — Schritte:**



1.  Definiere die Spiegelregel V\[i\] formal: π\_D, π\_P, Driver/Limit-Regel, Outcome/Judgment-Regel.
2.  Konstruiere Storyform A unter V\[i\]: 4 Throughlines × Domain-Zuweisung × Perspektiven-Zuweisung + Träger pro Throughline + Driver + Limit + Outcome + Judgment + minimal: ein Concern und ein Problem pro Throughline.
3.  Konstruiere Storyform B unter V\[i\] durch Anwendung von V\[i\] auf Storyform A (Spiegelung). Verifiziere die resultierende Storyform B als eigenständig Dramatica-konform.
4.  Verifiziere T1–T7 explizit, einzeln. Für jede T-Vorgabe: schreibe in einem Satz, *wie* V\[i\] die Vorgabe erfüllt.
5.  Beschreibe die Klimax-Mechanik in V\[i\] (T6) skizzenhaft (3–5 Sätze): Was passiert in der Spiegelregel-Logik, wenn der Klimax eintritt? (Driver-Pivot? Truth-Rotation? Fixpunkt-Kollaps?)
6.  Schreibe die knappe Begründung (≤ 250 Wörter, T7).



**Iteration \[i\] Output Schema (alle Felder ausfüllen):**



  - Variante: V\[i\]
  - Spiegelregel formal: \[(π\_D, π\_P, Driver/Limit-Regel, Outcome/Judgment-Regel)\]
  - Storyform A unter V\[i\]: \[vollständige Storypoint-Tabelle\]
  - Storyform B unter V\[i\]: \[vollständige Storypoint-Tabelle\]
  - Träger-Zuweisung: \[pro Throughline pro Storyform\]
  - T1 erfüllt: ja/nein, Begründung in einem Satz
  - T2 erfüllt: ja/nein, Begründung
  - T3 erfüllt: ja/nein, Begründung
  - T4 erfüllt: ja/nein, Begründung
  - T5 erfüllt: ja/nein, Begründung
  - T6 erfüllt: ja/nein, Klimax-Mechanik-Skizze
  - T7 erfüllt: ja/nein, Begründungstext (≤ 250 Wörter)
  - Konfidenz: \[niedrig / mittel / hoch\]
  - Stärkste Gegenevidenz: \[von welcher Quelle / welcher Methode\]
  - Während dieser Iteration ausgelöste Query-Erweiterungen: \[aufzählen, jeweils mit Achse\]



Du darfst nicht zu Iteration \[i+1\] fortfahren, bevor das Output-Schema von Iteration \[i\] vollständig ausgefüllt ist.

### Schritt 8 — NotebookLM Adversarial Interrogation Pass 2 (Variant-zentriert)

**Restatement Checkpoint — Vor Schritt 8.**



**Reflection Entry — Schritt 8.**



**Schritt 8 — Inhalt:**



Mit den überlebenden Varianten in der Hand, kehre zu den NotebookLM-Notebooks zurück und führe Pass 2 des Befragungsprotokolls (Constraint Block 4) — diesmal *gezielt* — durch. Frage: „Wenn V\[i\] richtig wäre, was im Notebook würde dann *falsch* werden? Und was im Notebook würde dann *erst plausibel*?" Logge.



-----

## PRE-SYNTHESIS INTEGRITY CHECK

Bevor du die finale Synthese schreibst, führe diesen Verifikationspass schriftlich aus. Jeder Punkt produziert eine geschriebene Zeile; „erledigt aus Erinnerung" zählt nicht.



1.  **Re-read Constraint Blocks 0–5 wörtlich.** Bestätige schriftlich: „Ich habe jeden Constraint Block neu gelesen und alle sind weiterhin aktiv."



1.  **Re-read der kritischen Denkmethoden-Blöcke.** Bestätige schriftlich: „Jede unten aufgeführte Methode ist aktiv und wurde von mir angewandt: M01 Falsification, M04 Contrast Classes, M07 Contradiction Log, M10 First-Principles Decomposition, M13 Adversarial Query Expansion."



1.  **Reflexions-Audit (Constraint Block 0).** Zähle die während des Laufs geschriebenen Reflexionseinträge. Bestätige: „Ich habe \[K\] Reflexionseinträge an folgenden Checkpoints geschrieben: \[aufzählen\]." Falls K unter dem in Constraint Block 0 geforderten Minimum, schreibe die fehlenden Reflexionen **jetzt** vor dem Fortfahren.



1.  **Query-Expansion-Audit (M13).** Bestätige schriftlich: „Methode M13 Adversarial Query Expansion wurde \[N\] mal entlang der vier Achsen (adjacent / opposing / abstraction / orthogonal) invoziert. Der Query Expansion Log enthält \[M\] Einträge, von denen \[P\] neuartige Befunde produzierten, die vorläufige Schlussfolgerungen modifizierten." Falls N = 0, ist die Forschung unvollständig — fahre mindestens einen Pass, bevor du fortfährst.



1.  **Cross-Pollination-Audit.** Bestätige schriftlich: „Schritte, die aus den zwei Nicht-Primär-Kategorien adaptiert wurden, wurden wie folgt ausgeführt: Schritt 5.b (Surviving-Branch Triangulation aus Kategorie B) — \[Ergebnis\]; Schritt 6.c (Hypothesis Half-Life Audit aus Kategorie C) — \[Ergebnis\]." Falls einer nicht ausgeführt wurde, halte und melde.



1.  **Constraint-Compliance-Audit.** Für jeden Constraint Block (0 bis 5) prüfe die akkumulierten Befunde und zitiere ein konkretes Beispiel, wie du ihn geehrt hast. Wenn du kein konkretes Beispiel zitieren kannst, flagge den Constraint als **nicht-nachweisbar-geehrt**.



1.  **Scope-Audit.** Bestätige: „Alle Befunde liegen innerhalb des in Constraint Block 2 definierten Scopes." Falls einige außerhalb liegen, flagge und entferne.



1.  **Exklusions-Audit.** Bestätige: „Keiner der Befunde oder Empfehlungen fällt in die Ausschlussliste in Constraint Block 3."



Erst wenn alle acht Punkte schriftlich abgehakt sind, beginnst du die Synthesis-Sektion.



-----

## SYNTHESIS — Finaler Output

Du füllst die folgende Schemastruktur aus.



\# Dramatica-Dual-Storyform-Rebuild für „Kohärenz Protokoll" — Bericht



\#\# Executive Summary



\[1–2 Absätze\]



\#\# Teil I — Theoretische Absicherung der Dual-Storyform-Spiegelung



\#\#\# I.1 First-Principles-Zerlegung



\[Wie wurde „Dual-Storyform-Spiegelung" auf algebraische Basiskomponenten zurückgeführt?\]



\#\#\# I.2 Definition des Mirror-Operators



\[Formal: π\_D, π\_P, Verknüpfungslogik, Driver/Limit-Regel, Outcome/Judgment-Regel. Auditierbar.\]



\#\#\# I.3 Symmetrieeigenschaften und Fixpunkte



\[Involutivität, Reflexivität, Fixpunkte und ihre dramatische Bedeutung\]



\#\#\# I.4 Maximum-2-Ebenen-Constraint, formal



\[Wie operationalisiert die Spiegelregel die Vorgabe „max. 2 Lesarten pro Throughline"?\]



\#\# Teil II — Hypothesen-Baum aller geprüften Spiegelregeln



\[Vollständige Auflistung aller mindestens vier Kandidaten — auch der eliminierten. Pro Kandidat: Beschreibung, T-Check, M01-Falsifikationsverlauf, Eliminations-Begründung falls eliminiert.\]



\#\# Teil III — Generierte Dual-Storyform-Alternativen



\#\#\# Variante V1



\[Output-Schema aus Schritt 7\]



\#\#\# Variante V2



\[Output-Schema aus Schritt 7\]



\[Weitere Varianten falls vorhanden\]



\#\# Teil IV — Vergleichsmatrix der überlebenden Varianten



\[Tabelle: Variante × T1–T7 + Konfidenz + Klimax-Mechanik. Knapp.\]



\#\# Teil V — Auditing & Methodologische Zusatzsektionen



\#\#\# Contradictions Encountered (Methode M07)



\[Synthetisierte Form des Contradiction Logs\]



\#\#\# Query Expansion Log (Methode M13)



\[Jede adversariale Erweiterung: Achse, Anfrage, Novel-Finding-Flag, Did-It-Modify-Conclusion-Flag\]



\#\#\# Reflection History (Constraint Block 0)



\[Alle Reflexionseinträge in Reihenfolge, wie geschrieben\]



\#\#\# Cross-Pollination Log (Phase 2b)



\[Schritt 5.b und Schritt 6.c — was zurückkam, ob es die finale Antwort modifiziert hat\]



\#\#\# NotebookLM Interrogation Log



\[Pro Notebook: welche Abschnitte adversarial geprüft, welche Inkonsistenzen entdeckt\]



\#\# Teil VI — Open Questions / Unresolved



\[Was die Forschung nicht klären konnte — z.B. Wächter-Zwiespalt-Soziopolitik, Post-Vortex-AEGIS-Status, Moonshine-Link-Boundary, falls sie unter den getesteten Spiegelregeln nicht eindeutig verortet werden konnten\]



\#\# Teil VII — Quellen



\[Strukturierte Quellenliste — Dramatica-Primärquellen zuerst, dann NotebookLM-Notebooks, dann Theorie-Hintergrundquellen\]



\#\# Teil VIII — Methodology Note



\[Knappe Anmerkung, welche kritischen Denkmethoden auf welche Befunde angewandt wurden, welche Befunde als „unanchored" oder „single-source" geflaggt sind\]



-----

## SELF-VERIFICATION-CHECKLIST FÜR DEN AUSFÜHRENDEN AGENTEN (v2.1 · 11 Punkte)

Bevor du die Synthese ausgibst, verifiziere:



  - Jeder größere Schritt begann mit einem wörtlichen Restatement Checkpoint.
  - CONSTRAINT BLOCK 0 (Reflection Baseline) wurde an allen fünf definierten Checkpoints geehrt; Reflexionseinträge sind geschrieben, nicht implizit.
  - Methode M13 (Adversarial Query Expansion) wurde entlang aller vier Achsen (adjacent / opposing / abstraction / orthogonal) mindestens je einmal invoziert, und der Query Expansion Log ist befüllt.
  - Beide cross-pollinated Schritte (Phase 2b — einer aus jeder Nicht-Primär-Kategorie) wurden ausgeführt und geloggt: Schritt 5.b und Schritt 6.c.
  - Jede aktive kritische Denkmethode hat mindestens eine konkrete Anwendung, die in den Befunden sichtbar ist.
  - Jede sachliche Behauptung wurde durch Source Triangulation geführt mit ≥ 2 unabhängigen Quellen, oder ist als single-source geflaggt.
  - Der Contradiction Log ist befüllt (selbst wenn „keine Widersprüche").
  - Alle Befunde liegen innerhalb des Temporal Scope.
  - Keine Befunde fallen in die Output-Ausschlüsse (insbesondere: keine Variante wird kanonisiert).
  - Der Pre-Synthesis Integrity Check wurde schriftlich ausgeführt (alle 8 Punkte).
  - Reflection History, Query Expansion Log und Cross-Pollination Log sind in der Synthese als eigene Sektionen vorhanden.



Falls ein Punkt fehlschlägt, repariere vor Lieferung. Liefere keine Synthese mit fehlschlagenden Checks.



-----



*Ende des Forschungsprompts. Führe jetzt aus.*
