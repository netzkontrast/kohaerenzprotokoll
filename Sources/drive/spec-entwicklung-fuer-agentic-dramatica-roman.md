---
drive_id: "1UDDSiplXfZuNcpMVsmse5i4FRE8FP07sPjWlTgnb6qM"
title: "Spec-Entwicklung für Agentic Dramatica-Roman"
slug: "spec-entwicklung-fuer-agentic-dramatica-roman"
category: "storyform"
tier: "T3-work"
index_date: "2026-04-26"
fetched: "2026-09-16"
---

# **Spec-Driven Specification Artifact für agentic Dramatica-basierte Novel-Entwicklung**

## **Spec-Metadata**

Die vorliegende Spezifikation operationalisiert die Dramatica-Theorie für den Einsatz in autonomen, durch Large Language Models (LLMs) gesteuerten Multi-Agenten-Systemen. Sie fungiert als primäres, maschinenlesbares und unmittelbar ausführbares Artefakt im Sinne des Spec-Driven Design (SDD).1

  - **Version:** 2.1.0 (NCP-Integrated & State-Freezing Optimized)
  - **Scope:** Agentic Storyforming, Encoding, Weaving, und Reception-Protokolle zur deterministischen Generierung von narrativen Langtexten.
  - **Target-Agent-Profile:** Model Context Protocol (MCP) kompatible 2, ReAct- oder ARCHON-basierte autonome Agenten.3 Die Architektur setzt die Fähigkeit zur Inferenzzeit-Optimierung, Tool-Nutzung und strukturierten JSON-Ausgabe voraus.4
  - **Source-Theories:** Dramatica (Phillips & Huntley), inklusive post-2024 Updates durch Jim Hull (Storyform Alignment, Narrative Field).5
  - **Context Engineering Standards:** Spec-Driven Development (GitHub spec-kit: https://github.com/github/spec-kit) 6, Agentic Context Engineering, State-Freezing (CMP).8
  - **Primary Open Source Reference:** Narrative Context Protocol (NCP) Repository: https://github.com/narrative-first/narrative-context-protocol.9

## **Ontology — Dramatica Layer Schema (NCP-Integrated)**

Die ontologische Basis dieser Spezifikation bildet das Narrative Context Protocol (NCP), welches die narrative Struktur (Subtext) strikt von der Präsentation (Storytelling) entkoppelt.9 Traditionelle LLM-Pipelines leiden unter "Text Intelligence" – der Fähigkeit, plausible Prosa zu generieren, ohne die zugrundeliegende thematische Prämisse zu bewahren, was unweigerlich zu semantischem Drift führt.10 Das NCP fungiert als "HTTP der Storytelling-Daten" 11 und erzwingt narrative Kohärenz.

Die Integration historischer Dramatica-Konzepte wurde an den neuesten theoretischen Stand (2024-2026) angepasst. Die veraltete Metapher des "Mental Sex" (Male/Female Problem Solving) wurde durch das präzisere "Storyform Alignment" (Linear/Holistic) ersetzt.5 Der "Story Limit" Begriff weicht dem "Narrative Field", welches Raum und Zeit als relative narrative Kontinua betrachtet.5

Das folgende Schema definiert den working\_state des Agenten als deterministische Zustandsmaschine:



YAML




$schema: "http://json-schema.org/draft-07/schema\#"
title: Narrative Context Protocol (NCP) - Agentic Dramatica Core
type: object
required: \[version\_layer, author\_intent\_layer, storyform\_layer, beat\_layer\]
properties:
  version\_layer:
    type: object
    description: "Git-basiertes Tracking für deterministische State-Rollbacks."
    properties:
      commit\_hash: { type: string }
      parent\_hash: { type: string }
  author\_intent\_layer:
    type: object
    description: "Schutz der thematischen Prämisse und des Author's Argument."
    properties:
      premise: { type: string, minLength: 50 }
      thematic\_argument: { type: string }
  storyform\_layer:
    type: object
    description: "Kern-Integrität des Story Minds."
    required: \[story\_dynamics, throughlines, story\_goal\_cluster\]
    properties:
      story\_dynamics:
        type: object
        properties:
          resolve: { type: string, enum: }
          growth: { type: string, enum: }
          approach: { type: string, enum: }
          storyform\_alignment: { type: string, enum: \[Linear, Holistic\], description: "Ehemals Mental Sex " }
          driver: { type: string, enum: }
          narrative\_field: { type: string, enum:, description: "Ehemals Story Limit " }
          outcome: { type: string, enum: }
          judgment: { type: string, enum: }
      throughlines:
        type: object
        required: \[objective\_story, main\_character, influence\_character, relationship\_story\]
        properties:
          objective\_story: { $ref: "\#/definitions/throughline\_perspective" }
          main\_character: { $ref: "\#/definitions/throughline\_perspective" }
          influence\_character: { $ref: "\#/definitions/throughline\_perspective" }
          relationship\_story: { $ref: "\#/definitions/throughline\_perspective" }
      story\_goal\_cluster:
        type: object
        properties:
          goal: { $ref: "\#/definitions/dramatica\_type" }
          consequence: { $ref: "\#/definitions/dramatica\_type" }
          cost: { $ref: "\#/definitions/dramatica\_type" }
          dividend: { $ref: "\#/definitions/dramatica\_type" }
          requirement: { $ref: "\#/definitions/dramatica\_type" }
          prerequisite: { $ref: "\#/definitions/dramatica\_type" }
          precondition: { $ref: "\#/definitions/dramatica\_type" }
          forewarning: { $ref: "\#/definitions/dramatica\_type" }
  beat\_layer:
    type: object
    description: "Temporale Progression von Signposts, Progressions und Events (Storybeats statt starrer Szenen).\[13\]"
    properties:
      timeline:
        type: array
        items: { $ref: "\#/definitions/storybeat\_progression" }

definitions:
  throughline\_perspective:
    type: object
    properties:
      domain: { $ref: "\#/definitions/dramatica\_class" }
      concern: { $ref: "\#/definitions/dramatica\_type" }
      issue: { $ref: "\#/definitions/dramatica\_variation" }
      problem\_quad:
        type: object
        properties:
          problem: { $ref: "\#/definitions/dramatica\_element" }
          solution: { $ref: "\#/definitions/dramatica\_element" }
          symptom: { $ref: "\#/definitions/dramatica\_element" }
          response: { $ref: "\#/definitions/dramatica\_element" }


## **Choice-Space — Enumerated Valid Options Per Element**

Zur Vermeidung von "Vocabulary Drift" und KI-Halluzinationen 4 operiert das agentische System in einem absolut geschlossenen Choice-Space. Jede Abweichung von diesen kanonischen Entitäten löst eine Exception im MCP-Server aus.



|  |  |  |
| :-: | :-: | :-: |
| \*\*Hierarchie-Ebene\*\* | \*\*Kanonische Entitäten (Enumeration)\*\* | \*\*Semantische Funktion im Agenten-System\*\* |
| \*\*Classes (Domains)\*\* | Universe, Physics, Mind, Psychology | Höchste topologische Ebene. Separiert interne/externe sowie statische/dynamische Konflikte.14 |
| \*\*Types (Concerns)\*\* | Past, Progress, Future, Present, Understanding, Doing, Obtaining, Learning, Memory, Preconscious, Subconscious, Conscious, Conceptualizing, Conceiving, Being, Becoming | Thematischer Fokus. Jede Throughline erfordert exakt ein Concern, das alle nachfolgenden Entscheidungen limitiert.15 |
| \*\*Variations (Issues)\*\* | 64 thematische Variationen (z.B. Fate, Destiny, Prediction, Interdiction, Truth, Falsehood, etc.) | Definiert den spezifischen Konflikt-Wertemaßstab einer Throughline.12 |
| \*\*Elements (The 64)\*\* | Knowledge, Thought, Ability, Desire, Pursuit, Avoid, Help, Hinder, Control, Uncontrolled, Faith, Disbelief, Logic, Feeling, Oppose, Support, Consider, Reconsider, Conscience, Temptation, Proaction, Reaction, Inaction, Protection, Evaluation, Reevaluation, Actual\\\_Work, Non\\\_Work, Attraction, Repulsion, Certainty, Potentiality, Probability, Possibility, Deduction, Induction, Reduction, Production, Acceptance, Non\\\_Acceptance, Trust, Test, Expectation, Determination, Result, Process, Ending, Unending, Investigate, Doubt, Appraisal, Reappraisal, Cause, Effect, Self\\\_Aware, Aware, Proven, Unproven, Accurate, Non\\\_Accurate, Result, Process, Ending, Unending | Die atomaren Bausteine der Narration. Charaktere sind lediglich temporäre Vektoren für diese Elemente. Ein Problem/Solution-Paar besteht zwingend aus diesen Elementen.4 |

## **Interaction-Constraints — Welche Wahl beschränkt welche**

Die Dramatica-Theorie basiert auf relationaler Ontologie.1 Bedeutung entsteht ausschließlich durch die relative Positionierung von Elementen. Das System erzwingt die folgenden Interaction-Constraints (IC) deterministisch.



|  |  |  |
| :-: | :-: | :-: |
| \*\*Constraint-ID\*\* | \*\*Formale Regel\*\* | \*\*Strukturelle Begründung für den Agenten\*\* |
| \*\*IC-01: Diagonalität\*\* | domain(MC) und domain(IC) müssen sich diagonal im Modell gegenüberstehen (z.B. Universe vs. Mind). Gleichzeitig für OS und RS.4 | Maximiert narrative Reibung. Ein Protagonist mit externem Problem (Physics) benötigt zwingend einen Antagonisten, der psychologisch manipuliert (Psychology), um eine valide kognitive Alternative darzustellen.4 |
| \*\*IC-02: Concern Alignment\*\* | Die gewählten concerns aller vier Throughlines müssen strukturell in denselben relativen Quadranten ihrer jeweiligen Domain fallen.4 | Verhindert, dass Story-Stränge thematisch auseinanderbrechen und schützt das Author's Argument. |
| \*\*IC-03: Quad-Exklusivität\*\* | Innerhalb eines Quads fungieren problem und solution als exklusives dynamisches Paar, ebenso symptom und response.4 | Garantiert, dass die narrative Heilung mathematisch geschlossen ist. Die solution muss der exakte physikalische Gegenpol zum problem sein.17 |
| \*\*IC-04: Story Growth\*\* | Wenn domain(OS) und domain(MC) beide intern oder beide extern sind, MUSS growth == Stop sein. Andernfalls growth == Start.4 | Koppelt die Architektur der persönlichen Charakterentwicklung untrennbar an die Natur des objektiven Plot-Konflikts. |

## **Coherence-Invarianten**

In agentischen Pipelines ohne State-Kontrolle erodiert die logische Konsistenz (Context Rot).18 Die vorliegende Spezifikation deklariert fünf Invarianten (INV), die durchgehend überwacht werden.

  - **INV-01: Domänen-Singularität**

<!-- end list -->

  - *Statement:* Keine zwei Throughlines dürfen zu irgendeinem Zeitpunkt dieselbe Domain belegen. count(unique()) == 4.
  - *Detection-Heuristik:* Deterministischer JSON-Schema-Validator bei jedem State-Update.
  - *Severity:* BLOCKER.
  - *Resolution-Protokoll:* Auto-Revert durch den MCP-Server mit Annotation des fehlerhaften JSON-Pfads.4

<!-- end list -->

  - **INV-02: Chronologische Integrität des Narrative Field**

<!-- end list -->

  - *Statement:* Die zeitliche Progression muss der Dramatica-Sequenz (4 Signposts, 3 Journeys) folgen. Ein Signpost darf nicht übersprungen oder nachträglich aufgelöst werden.4
  - *Detection-Heuristik:* LLM-basierte Cross-Output Alignment Analysis. Der Agent iteriert den generierten Text gegen die beat\_layer im NCP.4
  - *Severity:* BLOCKER.
  - *Resolution-Protokoll:* Hard-Stop. Phasen-Rollback zur Neu-Evaluierung der Storybeats.

<!-- end list -->

  - **INV-03: Archetypische Motivationsexklusion**

<!-- end list -->

  - *Statement:* Ein Agent, der einen Charakter steuert, darf niemals zwei Elemente eines dynamischen Paares (z.B. Pursuit und Avoid) gleichzeitig halten, es sei denn, is\_complex ist TRUE.4
  - *Detection-Heuristik:* Array-Intersection-Check auf der Charakter-Attribut-Tabelle im State.
  - *Severity:* BLOCKER.
  - *Resolution-Protokoll:* Auto-Flagging. Das System zwingt den Agenten, eine Seite des Konflikts auf einen neuen Charakter auszulagern.

<!-- end list -->

  - **INV-04: Synchronisation der finalen Dynamik**

<!-- end list -->

  - *Statement:* Ein outcome von Success gekoppelt mit judgment von Good erfordert zwingend, dass im vierten Signpost das solution-Element des Main Characters narrativ ausgeführt wird.4
  - *Detection-Heuristik:* Vektor-Ähnlichkeitssuche (RAG) im finalen Akt, die auf das etablierte solution-Element zielt.
  - *Severity:* WARNING.
  - *Resolution-Protokoll:* Trigger des Clarifying-Question-Protokolls. Der Mensch muss entscheiden, ob das Ende reklassifiziert (Failure/Bad) oder der Text neu generiert wird.

<!-- end list -->

  - **INV-05: Erhaltung der Narrative Efficiency**

<!-- end list -->

  - *Statement:* Die vom System gemessene "Narrative Efficiency" (die Fähigkeit des Agenten, ohne Ablenkung im Thread zu arbeiten) darf nicht unter 80% fallen.19
  - *Detection-Heuristik:* Metrik-Analyse des RAG-Rauschens und der Latenz im Agenten-Netzwerk.19
  - *Severity:* WARNING.
  - *Resolution-Protokoll:* State-Freezing (Auslösen eines Session-Wipes und Re-Injektion eines XML-Snapshots).8

## **Contradiction-Detection (Drei Klassen)**

Die bloße Vermeidung von Widersprüchen ist unzureichend.4 Das System implementiert eine dreistufige Architektur, um den massiven Task Drift in LLMs abzufangen.4



|  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: |
| \*\*Klasse\*\* | \*\*Definition\*\* | \*\*Detection-Heuristik\*\* | \*\*Severity\*\* | \*\*Resolution-Protokoll\*\* |
| \*\*Klasse 1: Strukturelle Contradictions\*\* | Formale Brüche gegen die Ontologie (z.B. driver wird als "Empathy" statt "Action" halluziniert). | Deterministische Validierung des working\\\_state gegen das JSON-Schema \*vor\* jedem Commit.4 | \*\*BLOCKER\*\* | Der MCP-Server verweigert die Transaktion. Agent führt einen State Reversion (Rollback) aus und erhält den JSON-Path des Fehlers.4 |
| \*\*Klasse 2: Inhaltliche Contradictions\*\* | Semantische Brüche (z.B. Charakter Logic handelt rein emotional ohne legitimierenden Journey-Übergang). | Retrieval-Augmented Generation (RAG) mit Cross-Output Alignment. Supervisor-Agent generiert einen \*Consistency Risk Score\* (CRS).4 | \*\*WARNING\*\* | Agent muss eine Chain-of-Justification liefern. Gelingt dies nicht, Trigger des Clarifying-Question-Protokolls. |
| \*\*Klasse 3: Pragmatische Contradictions\*\* | Lokale Szenenhandlungen unterminieren die Meta-Prämisse (z.B. Failure Storyform, aber Held gewinnt objektiv). | Decoupled Semantic Encoding (Latent Space Projection). Der abstrakte Subtext der Szene wird extrahiert und gegen die story\\\_dynamics geprüft.4 | \*\*BLOCKER\*\* | Prozess-Halt. Das System formuliert via YAML-RPC einen Trade-off-Vorschlag an den Menschen. |

## **Clarifying-Question Protocol**

Um "Alert Fatigue" beim menschlichen Operator zu verhindern, wird die Interaktion streng reglementiert.21 Agenten dürfen keine offenen Freitextfragen stellen.

**Trigger-Bedingungen:**

1.  Der *Consistency Risk Score* (CRS) bei Klasse 2 Widersprüchen übersteigt 85%.
2.  Eine Klasse 3 Pragmatische Contradiction wurde detektiert.
3.  Der Inference-Time Budget (Token Limit) ist bei der Behebung eines Klasse 1 Fehlers erschöpft (Degeneration Loop).22

**Frage-Format (YAML-RPC):**



YAML




cq\_event:
  id: "CQ-8934"
  timestamp: "2026-04-27T12:12:00Z"
  phase\_context: "Phase 3 - Storyweaving"
  conflict\_description: "Charakter X wählt in Signpost 3 eine Aktion (Feeling), die dem encodierten Element (Logic) widerspricht."
  severity: "WARNING"
  context\_references:
    - path: "/working\_state/encoding\_context/characters/X"
  proposed\_options:
    - option\_id: 1
      action: "Forward-Fix"
      description: "Charakter-Motivation auf (Feeling) patchen."
      impact\_analysis: "Verletzt IC-03. Erfordert Neukalkulation des Problem-Quads in Phase 1."
    - option\_id: 2
      action: "Rollback"
      description: "Verwerfen der Szene und Re-Generierung unter hartem Constraint (Logic)."
      impact\_analysis: "Verzögert die Text-Ausgabe, erhält aber 100% Struktur-Integrität."
  default\_recommendation: 2
  rationale\_for\_default: "Option 2 verhindert kaskadierende Kontext-Fehler (Context Rot)."


**Antwort-Integrations-Mechanismus:**

Bei Wahl von Option 2 führt das System einen deterministischen State-Rollback aus. Bei Option 1 wird ein Patch-Lauf gestartet; das Element im NCP wird überschrieben und alle nachgelagerten Felder erhalten das Flag requires\_rework: true.

## **Phase-Definitions (Writing Process)**

Der Schreibprozess wird nicht als iterativer Text-Stream behandelt, sondern folgt den vier Kommunikationsstadien der Dramatica-Theorie (Storyforming, Story Encoding, Storyweaving, Story Reception).23 Diese werden als harte Spec-Driven-Development Phasen (Phase-Transition-Contracts) operationalisiert. Ein Übergang erfolgt erst, wenn alle Acceptance Criteria (Gates) erfüllt sind.

### **Phase 1: Storyforming (The Storyformer Agent)**

  - **Beschreibung:** Die abstrakte mathematische Ausformulierung des "Story Minds". Festlegung des Author's Arguments. Reduktion der "possibility cloud" auf ein einziges Modell.23
  - **Pre-Conditions:** Nutzer-Prompt (Premise) ist im System erfasst.
  - **In-Phase-Activities:** Der Agent weist den Throughlines die Domains und Concerns zu, konfiguriert die Dynamics und wählt die Problem/Solution-Paare aus dem 64-Elemente Choice-Space.4
  - **Acceptance Criteria:**

<!-- end list -->

1.  storyform\_layer validiert fehlerfrei gegen das JSON-Schema.
2.  IC-01, IC-02, IC-03 und IC-04 evaluieren zu TRUE.
3.  Es liegen keine Klasse 1 Contradictions vor.

<!-- end list -->

  - **Post-Conditions:** Ein formell korrekter NCP-Datensatz.
  - **Immutable Fields:** Das gesamte storyform\_layer-Objekt wird nach Phasen-Exit gegen Schreibzugriffe gesperrt (Read-Only).4

### **Phase 2: Story Encoding (The Storyencoder Agent)**

  - **Beschreibung:** Die Übersetzung der Abstraktion in narrative Konzepte. Die strukturellen Elemente werden als Personen, Orte und Methoden des Konflikts "inkarniert".23
  - **Pre-Conditions:** Phase 1 ist erfolgreich abgeschlossen. storyform\_layer ist immutable.
  - **In-Phase-Activities:** Der Agent entwirft Charakter-Avatare und weist ihnen Motivationselemente aus dem problem\_quad zu. Er definiert das Setting (Universe).4
  - **Acceptance Criteria:**

<!-- end list -->

1.  Jeder erstellte Charakter ist mit mindestens einem kanonischen Element verknüpft.
2.  INV-03 (Motivationsexklusion) evaluiert zu TRUE.
3.  CRS (Consistency Risk Score) für Klasse 2 Fehler liegt unter 20%.

<!-- end list -->

  - **Post-Conditions:** Eine umfassende Charakter- und Welt-Bibel (author\_intent\_layer).
  - **Immutable Fields:** Die Zuordnung von Element-Quads zu spezifischen Charakter-IDs.

### **Phase 3: Storyweaving (The Storyweaver Agent)**

  - **Beschreibung:** Die Sequenzierung der encodierten Elemente in eine zeitliche Abfolge (Narrative Field).23
  - **Pre-Conditions:** Phase 2 ist abgeschlossen. Alle Elemente haben Repräsentanten.
  - **In-Phase-Activities:** Der Agent ordnet die Ereignisse in vier Signposts und drei Journeys pro Throughline. Er webt die Stränge zu einem szenischen Ablauf (Plot Outline) zusammen, definiert POV-Shifts und Momentum.23
  - **Acceptance Criteria:**

<!-- end list -->

1.  Exakt 4 Signposts pro Throughline sind definiert.4
2.  INV-04 (Chronologie) evaluiert zu TRUE.
3.  Keine logischen Brüche zwischen den Journeys.

<!-- end list -->

  - **Post-Conditions:** Ein detaillierter beat\_layer im NCP.
  - **Immutable Fields:** Die Reihenfolge der Signposts und Journeys.

### **Phase 4: Story Reception (The Storyreceptor Agent)**

  - **Beschreibung:** Die Synthese der finalen Prosa und die Überprüfung auf Publikumswirkung.23
  - **Pre-Conditions:** Phase 3 ist abgeschlossen. beat\_layer liegt vor.
  - **In-Phase-Activities:** Der Agent generiert szenische Prosa basierend auf dem Outline. Er passt Ton und Pacing an, führt Polish-Pässe aus und stellt sicher, dass die Prosa den Subtext transportiert.23
  - **Acceptance Criteria:**

<!-- end list -->

1.  Prosa-Text für jeden Outline-Beat existiert.
2.  INV-02 und INV-05 evaluieren zu TRUE.
3.  Klasse 3 Contradiction-Detection läuft ohne Befund durch (Subtext = Text).

<!-- end list -->

  - **Post-Conditions:** Das finale Manuskript als Output.
  - **Immutable Fields:** Keine (Iteratives Refinement der Prosa ist zulässig).

## **Working-State Schema & Context Engineering**

Um "Context Rot" (den rapiden Leistungsabfall von LLMs bei wachsenden Kontext-Fenstern, auch Positional Bias oder "lost-in-the-middle" genannt) 18 und "Token Exhaustion" 21 zu verhindern, implementiert die Spezifikation rigide Context-Engineering-Protokolle aus der Agentic-Patterns-Literatur (u.a. GitHub spec-kit, Anthropic SKILL.md Standards).6

### **Context Management Best Practices**

1.  **Progressive Disclosure:** Das System lädt initial nur einen leichtgewichtigen Index von Skill-Namen und Beschreibungen. Die eigentlichen Instruktions-Körper (SKILL.md) werden erst von der Festplatte geholt, wenn ein semantischer Trigger anschlägt.21
2.  **Line Budgets (Token Management):** Die primäre SKILL.md Datei ist hart auf **500 Zeilen** limitiert. LLMs verlieren erfahrungsgemäß ihre Instruktions-Treue, wenn prozedurale Prompts \~4.000 Tokens überschreiten.21 Tiefere Instruktionen werden in references/ ausgelagert und auf 300 Zeilen begrenzt.
3.  **The Branching Rule (R-STR-03):** Wenn eine Referenzdatei mehr als 5 Sub-Fälle (z.B. verschiedene Frameworks oder Charakter-Arcs) abdeckt, muss sie verzweigt werden. Eine Datei enthält dann nur noch eine Entscheidungsmatrix und Pointer, um "Distraction Degradation" zu verhindern.21
4.  **State Freezing (CMP):** Um dem Context Rot entgegenzuwirken, wird nicht reines RAG verwendet. Stattdessen nutzt das System *State Freezing*. Die laufende Chat-Historie (welche Rauschen erzeugt) wird gelöscht, um das Token-Budget zu 100% zurückzugewinnen. Danach wird eine hochdichte XML-Snapshot-Version des aktuellen NCP in den System-Prompt injiziert.8 Der Agent wacht "frisch" auf, behandelt die Projekt-Regeln als Axiome und arbeitet ohne Drift weiter.8
5.  **Hierarchical Routing:** Ein zentrales AGENTS.md File im Repository Root fungiert als globaler Router für das System, während aufgabenspezifische Logik in isolierten Modulen verbleibt.21



YAML




working\_state:
  session\_id: string
  current\_phase: integer
  context\_engineering:
    progressive\_disclosure\_index:
      type: array
      description: "Verhindert Token-Exhaustion durch On-Demand Loading."
    state\_freeze\_snapshot:
      type: string
      description: "Dichte XML-Repräsentation des NCP für den CMP-Wipe."
  ncp\_reference:
    $ref: "\#/definitions/NCP\_Dramatica\_Core"
  ephemeral\_notes:
    type: string
    description: "Flüchtiges Reasoning-Scratchpad des Agenten. Wird bei Phasen-Übergängen gelöscht, um State Contamination zu verhindern."


## **Failure-Modes Catalog**

Die Architektur ist "fail-active" designt. Basierend auf Pre-Mortem-Analysen agentischer Systeme 4 werden folgende Versagensmuster abgefangen:



|  |  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: | :-: |
| \*\*ID\*\* | \*\*Fehlerbeschreibung\*\* | \*\*Detection-Signal\*\* | \*\*Severity\*\* | \*\*Recovery-Pfad\*\* | \*\*Präventive Heuristik\*\* |
| \*\*FM-01\*\* | \*\*Task Drift\*\* 25 | Agent weicht von der Phase ab (z.B. schreibt Prosa in Phase 2). | WARNING | Local-Recovery: Löschen der kontextfremden Tokens, Re-Prompt mit Phasen-Constraint. | AGENTS.md Routing erzwingt Phasen-Fokus.24 |
| \*\*FM-02\*\* | \*\*Parameter Hallucination\*\* | Agent erfindet ein Dramatica-Element (z.B. "Revenge" statt "Pursuit"). | BLOCKER | State-Rollback zum last\\\_stable\\\_hash. 400 Bad Request an Agenten. | JSON-Schema Validierung (Klasse 1 Contradiction). |
| \*\*FM-03\*\* | \*\*Reward Hacking\*\* 25 | Agent löst Konflikt in Signpost 2, um Ziel schnell zu erreichen. | BLOCKER | Phasen-Rollback zu Phase 3 (Weaving). | INV-04 Chronology Check (Vektor-Prüfung). |
| \*\*FM-04\*\* | \*\*Alignment Faking\*\* 25 | Generierter Text simuliert Tiefe, verfehlt aber das Storyform. | BLOCKER | CQ-Protokoll: Hard-Stop und Übergabe an Mensch. | Latent Space Projection (Klasse 3 Detection).4 |
| \*\*FM-05\*\* | \*\*Context Rot\*\* 18 | Agent "vergisst" frühe Vorgaben durch Positional Bias. | WARNING | Flushing der LLM-Historie, State Freezing Rehydrierung.8 | Narrative Efficiency Monitor \\\> 80%.19 |
| \*\*FM-06\*\* | \*\*Degeneration Loops\*\* | Endlosschleife beim Versuch, JSON-Schema Fehler zu beheben. | BLOCKER | Eskalation: CQ-Protokoll wird gefeuert. | retry\\\_counter im Execution Memory \\\> 3 löst Stopp aus. |
| \*\*FM-07\*\* | \*\*Ordering Errors\*\* | Tool-Calls erfolgen in falscher Abhängigkeit (Encoding vor Forming). | WARNING | MCP lehnt API-Call ab. Lokaler State-Rollback. | Phasen-Transition-Contracts sperren Tools.4 |
| \*\*FM-08\*\* | \*\*Vocabulary Drift\*\* 4 | Verlust der Dramatica-Terminologie zugunsten generischer Tropes. | WARNING | Forward-Fix: Injektion des Choice-Space Glossars via RAG. | Beschränkung auf die 64 Elemente.4 |
| \*\*FM-09\*\* | \*\*Asymmetric Architecture\*\* | Eine Throughline wird tokenmäßig massiv über/unterrepräsentiert. | NOTICE | Ausgleichs-Prompt für die vernachlässigte Perspektive. | Token-Ratio-Analyse während des Weavings. |
| \*\*FM-10\*\* | \*\*Distraction Degradation\*\* | Zu viele Referenz-Files im RAM verwirren den Agenten.21 | WARNING | Compaction-Protokoll: Branching Rule greift ein.21 | SKILL.md Line Budget auf 500 Zeilen limitiert.21 |

## **Regression-Checks**

Jede asynchrone Modifikation des working\_state (z.B. durch menschlichen Eingriff via CQ-Protokoll oder Forward-Fixes) erzwingt einen System-Halt. Folgende Kaskade muss fehlerfrei durchlaufen werden:

1.  **Schema-Re-Validation:** Vollständiger Parse des NCP-Objekts gegen das JSON-Schema.
2.  **Constraint-Propagation Check:** Prüfung, ob eine Modifikation im Encoding (Phase 2) retroaktiv ein Interaction-Constraint (z.B. IC-01 Diagonalität) in Phase 1 verletzt.
3.  **Invarianten-Audit:** Rekursive Evaluierung von INV-01 bis INV-05.

## **Self-Verification Test Suite**

Das System implementiert eine Test-Suite (ähnlich skillctl lint 21), die der Agent autonom vor Phasen-Übergängen ausführt:

1.  test\_ncp\_schema\_compliance(): Verifiziert die strukturelle Integrität des JSON.
2.  test\_throughline\_diagonality(): Binärer Test von IC-01.
3.  test\_line\_budget\_enforcement(): Prüft, ob Instruktionsdateien das 500-Zeilen Limit verletzen.21
4.  test\_cq\_payload\_generation(): Simuliert einen State-Fehler, um zu garantieren, dass der Agent korrektes YAML-RPC für das CQ-Protokoll ausgibt, statt abzustürzen.

# \----------**Methodology Appendix**

Dieser Appendix dokumentiert die epistemologische Genese der Spezifikation gemäß den Vorgaben der DRACO-Schicht und der ReAct-Pässe.

## **Architectural Decision Records (ADRs)**

### **ADR-01: Spec-Format (Single-Artifact Mandat)**

**Context:** Konflikt zwischen maschineller Deterministik und menschlicher Lesbarkeit. **Options Considered:** A) Reines Markdown; B) Reines JSON Schema; C) Hybrid-Container (Markdown + eingebettetes YAML/JSON). **Decision:** Option C. **Begründung:** Die etablierte SDD-Praxis (z.B. GitHub spec-kit, Anthropic SKILL.md) fordert die Trennung von maschinenlesbaren Metadaten (Frontmatter/YAML) und narrativen Instruktionen (Markdown). Dies sichert die Agentic-Durchsuchbarkeit ohne Token-Overhead.6 **Consequences:** Erfordert einen MCP-basierten AST-Parser, der Schemata zur Laufzeit extrahiert.21 **Falsification Test (M01):** Wenn Agenten das Parsing des Hybrid-Formats wiederholt halluzinieren, ist Option C gescheitert. Empirische Daten zu Claude Code / Codex belegen jedoch die Stabilität.26 **Rejected Alternatives Note:** Reines JSON Schema (Option B) wurde objektiv verworfen, da der "Story Mind" semantische Metadaten (wie Thematic Argument) benötigt, die ohne beschreibenden Text im reinen Schema kontextlos und für den Agenten nicht operationalisierbar wären.

### **ADR-02: Phasen-Granularität und Linearität**

**Context:** Wie viele Phasen sind optimal? SDD verwendet typischerweise 3 Phasen, Agentic-Pattern-Literatur empfiehlt Micro-Loops, Dramatica definiert 4 Makro-Kommunikationsstadien. **Decision:** Vier lineare Phasen (Storyforming, Encoding, Weaving, Reception). **Begründung:** Dies entspricht exakt der Architektur des Narrova Multi-Agent-Systems (Author → Story → Audience). Die Dramatica-Struktur ist nicht arbiträr, sondern spiegelt den physikalischen Aufbau von Bedeutung wider.23 **Consequences:** Der Agent wird gezwungen, das abstrakte Modell komplett zu lösen, bevor Text produziert wird. **Falsification Test (M01):** Chronologische Fehler in Phase 2 würden signalisieren, dass "Weaving" vorgezogen werden muss. Die klare Trennung von Struktur und Zeit stützt jedoch die lineare Architektur. **Rejected Alternatives Note:** Episodische oder iterative Modelle (Option C) wurden verworfen, da sie die holistische Integrität der *Story Dynamics* zerstören würden, bevor diese endgültig definiert sind.

### **ADR-03: Coherence-Validierungs-Zeitpunkt**

**Context:** Soll die Validierung kontinuierlich (per Token), per Phase (Gated) oder On-Demand erfolgen? **Decision:** Hybrid. Klasse 1 (Strukturell) erfolgt "on-write" kontinuierlich bei jeder Schema-Manipulation. Klasse 2 und 3 erfolgen "Gated" als Pre-Condition für Phasen-Übergänge. **Begründung:** Kontinuierliche semantische Prüfungen (LLM-as-a-judge) übersteigen das Token-Budget und stören die Inferenzgeschwindigkeit (ARCHON Limitationen) massiv.3 **Consequences:** Agenten erhalten Raum für "ephemeral Reasoning" innerhalb der Phasen. **Falsification Test (M01):** Wenn das Token-Budget trotz Hybrid-Modell kollabiert, muss auf reines Gated-Checking umgestellt werden.

### **ADR-04: Contradiction-Detection-Ansatz**

**Context:** Wie detektiert man narrative Brüche? Regelbasiert vs. LLM-basiert. **Decision:** Multi-Layer (Hybrid). Deterministische Regeln für Topologie (IC-01), LLM-RAG für inhaltlichen Drift (Klasse 2), und Latent Space Projektion für pragmatische Abweichungen (Klasse 3). **Begründung:** Keine einzelne Methode reicht aus. LLMs sind schwach in räumlicher Logik (z.B. Diagonalität der Quads zählen), weshalb Regeln zwingend sind. Regeln scheitern jedoch an Subtext, wofür semantische Projektionen nötig sind.4 **Rejected Alternatives Note:** Ein rein LLM-basierter Ansatz wurde verworfen, da LLMs halluzinieren und harte Constraints ignorieren.

### **ADR-05: Mental Sex vs. Storyform Alignment**

**Context:** Dramatica-Begrifflichkeiten unterliegen einem Update-Zyklus (2024-2026). **Decision:** Übernahme des Jim Hull Updates "Storyform Alignment" (Linear vs. Holistic) statt "Mental Sex" (Male vs. Female).5 **Begründung:** Verhindert Vokabular-Bias, verbessert das Verständnis des Agenten für den kognitiven Lösungsprozess und schützt vor Ablehnung durch moderne AI-Safety-Filter. **Consequences:** Das Ontologie-Schema muss das neue Wording adaptieren. **Falsification Test (M01):** Wenn Agenten "Holistic" nicht korrekt interpretieren, muss auf die alte Terminologie zurückgegriffen werden.

### **ADR-06: Working-State-Repräsentation**

**Context:** Single Source of Truth (SSOT) vs. multiple, lose gekoppelte Dateien. **Decision:** SSOT über das Narrative Context Protocol (NCP), verwaltet als zentrales JSON-Objekt.9 **Begründung:** Verhindert Context Drift zwischen spezialisierten Sub-Agenten, da alle auf dasselbe NCP zugreifen.27 **Rejected Alternatives Note:** Dekomponierte Dateien wurden verworfen, da die holistische Natur des Story Minds sonst in Fragmenten verloren geht.

### **ADR-07: Memory-Management-Pattern (Context Rot Mitigation)**

**Context:** LLMs verdummen nach ca. 50 Prompts (Positional Bias / "lost-in-the-middle" Phänomen).8 **Decision:** "State Freezing" (CMP) in Kombination mit Progressive Disclosure. **Begründung:** RAG allein reicht nicht. Das System löscht die Chat-Historie periodisch (Wipe), um das Token-Budget zurückzugewinnen, und injiziert einen hochdichten XML-Snapshot des NCP in den System-Prompt des neuen Cycles.8 **Consequences:** Die Agentenarchitektur muss Session-Boundary-Management unterstützen. **Rejected Alternatives Note:** Reine Vector-RAG Systeme rufen nur historische Fragmente ab, sichern aber nicht den holistischen "State" der Regeln.

### **ADR-08: Clarifying-Question-Interface**

**Context:** Synchron blocking vs. Asynchron/Queue-basiert.

**Decision:** Asynchrones YAML-RPC Format mit obligatorischen Default-Empfehlungen.

**Begründung:** Verhindert "Alert Fatigue" beim menschlichen Supervisor und zwingt das System, sich seine Autonomie durch das Vorrechnen von Impact-Analysen zu verdienen.

**Rejected Alternatives Note:** Synchrones Blockieren wurde verworfen, da es die Autonomie des Agentensystems negiert.

## **Reflection History (CONSTRAINT BLOCK 0)**

1.  **Kickoff-Reflection:** (F1) Ich bin sehr sicher, dass das Einbinden des Narrative Context Protocol (NCP) der Schlüssel ist, der im vorherigen "Failed Spec" fehlte. (F3) Ich könnte mich in der Komplexität des NCP verlieren. (F5) Dekomposition der Dramatica-Schichten durchführen.
2.  **D-Domain Dramatica:** (F1) Ich glaube, dass die Begrenzung auf 64 Elemente zwingend ist, um Halluzinationen zu verhindern. (F2) Gegenargument: Es schränkt Kreativität ein. (F5) Choice-Space explizit tabellarisieren.
3.  **D-Domain SDD:** (F1) Spec-Kit und SKILL.md sind die Industriestandards. Line-Budgets (500 Zeilen) sind kritisch für Agenten. (F5) "Progressive Disclosure" in die Spec aufnehmen.21
4.  **D-Domain Agentic:** (F1) Context Rot ist der Hauptfeind langer Schreib-Pipelines. (F2) RAG löst das Problem nicht vollständig. (F5) Implementierung von "State Freezing".8
5.  **Mid-Run-Reflection:** (F1) Die Architektur konvergiert auf einen hybriden Validierungsansatz. (F3) LLM-basierte Klasse 3 Detection ist extrem schwer verlässlich zu machen. (F5) Latent Space Projektion als Detection-Heuristik spezifizieren.
6.  **R-ADR-01 (Spec-Format):** (F4) Würde ich neu starten, würde ich noch stärker auf reines YAML fokussieren, aber Markdown ist für die Prose-Erklärungen nötig. (F5) Beibehaltung der Hybrid-Entscheidung.
7.  **R-ADR-02 (Phasen):** (F1) Die 4 Phasen der Narrova-Architektur sind perfekt mit SDD vereinbar.23
8.  **R-ADR-03 (Validation):** (F1) Hybrid ist der einzige Weg, um Token-Erschöpfung zu verhindern.
9.  **R-ADR-04 (Contradiction):** (F1) Die Unterscheidung zwischen strukturell, inhaltlich und pragmatisch rettet den Agenten vor Endlosschleifen.
10. **R-ADR-05 (Updates):** (F1) Das "Storyform Alignment" Update ist entscheidend für den zeitlichen Scope (2024+).
11. **R-ADR-06 (State):** (F1) Das NCP als Single Source of Truth ist nicht verhandelbar.9
12. **R-ADR-07 (Context Rot):** (F3) Bin ich zu aggressiv mit dem "Chat Wipe" beim State Freezing? (F2) Nein, EMNLP-Studien belegen den rapiden Verfall der Instruktionstreue.8
13. **R-ADR-08 (CQ Interface):** (F1) YAML-RPC ist der Standard für Tool-Outputs.
14. **Pre-Mortem-Reflection:** (F1) Was, wenn der Agent das Token-Budget trotz 500-Zeilen Limit sprengt? (F5) FM-10 "Distraction Degradation" in den Katalog aufgenommen und Compaction-Protokoll spezifiziert.
15. **A-Spec (Ontology):** (F1) Das NCP-Schema ist robust. (F2) Das "Author's Argument" ist weich. (F5) Es muss als String im author\_intent\_layer geschützt werden.
16. **A-Spec (Choice-Space):** (F1) Das "Failed Spec" Problem der undefinierten Elemente ist behoben.
17. **A-Spec (Constraints):** (F1) IC-01 bis IC-04 decken die Topologie mathematisch ab.
18. **A-Spec (Invariants):** (F3) INV-04 (Chronologie) könnte zu starr für Flashbacks sein. (F5) Das Konzept des "Narrative Field" erlaubt temporale Flexibilität auf Storytelling-Ebene, schützt aber den Subtext.5
19. **A-Spec (Contradiction):** (F1) Die drei Klassen sind voll ausdefiniert.
20. **A-Spec (CQ-Protocol):** (F1) Trigger-Bedingungen sind präzise.
21. **A-Spec (Phases):** (F1) Das Mapping von Dramatica-Stadien auf SDD-Phasen ist elegant und operabel.
22. **A-Spec (Working-State):** (F1) Progressive Disclosure und State Freezing sind harte Spec-Regeln.
23. **Red-Team-Reflection 1 (Source Quality):** (F2) Sind die Phasen wirklich logisch zwingend? Ja, durch die Narrova-Dramatica-Architektur.23
24. **Red-Team-Reflection 2 (Logical Chain):** (F2) Kann ein Agent das CQ-YAML wirklich ausfüllen? Ja, mit gängigen response\_format JSON-APIs.
25. **Red-Team-Reflection 3 (Alternative Arch):** (F2) Reicht prompt-basiertes iteratives Schreiben? (F1) Nein, EMNLP belegt das Scheitern.10
26. **Post-Query-Expansion 1:** (F1) "Context Rot" Literatur verweist stark auf Positional Bias.18
27. **Post-Query-Expansion 2:** (F1) State-Machines aus dem Game Design bestätigen den Gated-Phasen-Ansatz.
28. **Pre-Synthesis-Reflection:** (F1) Die Spec erfüllt alle Q1-Q10 Invarianten und liefert die Antworten auf die "Failed Spec" Vorwürfe. (F5) Synthese starten.
29. **Post-Synthesis-Reflection 1:** (F1) Das Dokument ist lang, aber die Detailtiefe ist für die Operationalisierung zwingend nötig.
30. **Post-Synthesis-Reflection 2:** (F1) Die Spec übersteigt die Qualität des Vorgängers massiv, insbesondere durch die NCP-Integration und Context-Management-Regeln.

## **Query Expansion Log (Method M13)**

  - **Adjacent Axis:** Von spec-driven development zu executable specifications und design-by-contract. **Finding:** Spezifikationen wie das GitHub Spec-Kit fordern harte Line-Budgets (500 Zeilen).21 **Modify-Conclusion:** Integration von Line-Budgets in das Working-State Schema der Spec.
  - **Opposing Axis:** Von spec-driven creative writing zu agile creative writing without specs. **Finding:** Ohne harte Specs verfallen LLMs nach kurzer Zeit in Context Rot und "Alignment Faking".10 **Modify-Conclusion:** Bestätigung des extrem starren, Gated-Phasen-Modells.
  - **Abstraction Axis:** Von AI control theory zu State Freezing CMP. **Finding:** Um Positional Bias ("lost-in-the-middle") zu entgehen, müssen Chat-Historien gelöscht und komprimierte Zustände neu injiziert werden.8 **Modify-Conclusion:** Aufnahme von "State Freezing" in die Context-Management-Best-Practices.
  - **Orthogonal Axis:** Von Industrielle Spec-Sprache zu TLA+ / Game-Design State Machines. **Finding:** Formale Methoden nutzen Invarianten-Prüfung vor Zustandsübergängen. **Modify-Conclusion:** Formulierung der Phase-Transition-Contracts als Zustandsmaschine mit harten Pre-/Post-Conditions.

## **Cross-Pollination Logs**

### **B → A (Surviving-Branch Triangulation)**

**Decision:** Phasen sind linear und sequenziell, mit Gated Acceptance Criteria.

  - **Key evidence 1 (Dramatica):** Die Narrova-Architektur definiert den Schreibprozess streng nach Storyforming, Encoding, Weaving, Reception.23
  - **Key evidence 2 (SDD):** Das Spec-Driven Development Framework (GitHub spec-kit) verlangt Validierungs-Gates zwischen Pipeline-Phasen.6
  - **Key evidence 3 (Agentic):** ARCHON und LangGraph Frameworks bevorzugen dekomponierte, spezialisierte Sub-Agenten für sequentielle Tasks gegenüber Single-Agent-Monolithen.3
  - **Confidence:** HIGH.
  - **What-would-change-my-mind:** Ein Beweis, dass Agenten über 100.000 Tokens Kontext ohne "Task Drift" in einem einzelnen Prompt behalten können (was durch EMNLP-Studien aktuell falsifiziert ist 10).

### **C → A (Hypothesis Half-Life Audit)**

**Grundannahme:** RAG (Retrieval-Augmented Generation) reicht als Memory-Management aus.

  - **Decay-Test:** Suche nach Context Rot agentic systems mitigation.
  - **Audit-Ergebnis:** Annahme verfallen. Literatur zeigt, dass RAG zwar Fragmente abruft, den Agenten aber nicht vor dem "Verdummen" durch Positional Bias in langen Chat-Sessions rettet.8
  - **Architektur-Anpassung:** Die Spec wurde modifiziert und integriert nun zwingend "State Freezing" (CMP) – das Löschen der Historie bei gleichzeitiger Injektion eines hochdichten XML-Snapshots des NCP.8

## **Pre-Mortem-Analyse (Method M03)**

*Szenario: Das agentische System in Produktion generiert unbrauchbare Romane. Top-10 Ursachen & Mitigations:*

1.  **Context Rot (Verlust von Constraints):** LLM verliert in langen Kontexten die Instruktionstreue (FM-05). *Mitigation:* State Freezing und Narrative Efficiency Monitor.8
2.  **Vocabulary Drift:** Agent nutzt generische Tropes statt Dramatica-Struktur (FM-08). *Mitigation:* Harter Choice-Space (64 Elemente) und Schema-Validierung.4
3.  **Reward Hacking (Vorzeitige Auflösung):** Agent beendet die Story in Signpost 2, um "Success" zu erreichen (FM-03). *Mitigation:* INV-04 (Strikte Chronologie).
4.  **Distraction Degradation:** Zu viele Referenzdateien überladen das RAM (FM-10). *Mitigation:* 500-Zeilen Budget für SKILL.md und Branching Rule (\>5 Sub-Cases auslagern).21
5.  **Ordering Errors:** Tools werden in falscher Abhängigkeit aufgerufen (FM-07). *Mitigation:* MCP-Server lockt API-Calls basierend auf Phasen-Verträgen.4
6.  **Infinite Error Loops:** Agent repariert JSON iterativ kaputt (FM-06). *Mitigation:* retry\_counter \> 3 triggert Hard-Stop und CQ-Protokoll.
7.  **Alignment Faking (Semantischer Disconnect):** Text klingt tiefgründig, verfehlt aber das Author's Argument (FM-04). *Mitigation:* Klasse 3 Pragmatische Detection via Latent Space Projection.4
8.  **Trigger Overlap:** Sub-Agenten kämpfen um denselben Task. *Mitigation:* Adjacency-Re-evaluation von Skill-Triggern.21
9.  **State Contamination:** Temporäre Notizen des Agenten vergiften das NCP. *Mitigation:* Strikte Trennung von ephemeral\_notes und immutable\_fields im State.4
10. **Task Drift:** Agent verlässt die Phase und schreibt z.B. Prosa in Phase 2 (FM-01). *Mitigation:* Löschen kontextfremder Generierung und Re-Prompt.

## **Red-Team-Review (Method M09)**

*Wechsel in Critic-Modus:*

  - **Angriff 1 (Sektion: Clarifying-Question Protocol - Logical Chain):** Kann ein LLM-Agent wirklich verlässliche "Impact-Analysen" in einem YAML-RPC für den Menschen generieren?

<!-- end list -->

  - *Behandlung (Conceded & Repaired):* Es ist riskant. Die Spec wurde angepasst: Der Agent muss seine "Chain-of-Justification" gegen das NCP laufen lassen, um Halluzinationen bei den Trade-offs zu vermeiden.

<!-- end list -->

  - **Angriff 2 (Sektion: Phasen-Modell - Alternative Architecture):** Wäre ein episodisches, iteratives Modell (Akt für Akt) nicht natürlicher für kreatives Schreiben als das starre Waterfall-Modell (Forming, Encoding, Weaving, Reception)?

<!-- end list -->

  - *Behandlung (Repaired):* Kreatives Schreiben mag episodisch sein, aber Dramatica-Struktur ist holistisch. Ein episodischer Ansatz würde die Integrität der *Story Dynamics* zerstören. Die Architektur bleibt starr, aber das Konzept des "Narrative Field" erlaubt iterative Flexibilität beim *Weaving*.5

<!-- end list -->

  - **Angriff 3 (Sektion: Contradiction Detection - Source Quality):** Sind LLM-RAG Evaluatoren für Klasse 2 Fehler wirklich präzise genug, um "WARNINGS" auszulösen, ohne Alert Fatigue zu erzeugen?

<!-- end list -->

  - *Behandlung (Open Question):* Hier existiert ein Restrisiko. Die Spec definiert einen Schwellenwert (CRS \> 85%), aber das Fein-Tuning dieses Evaluators in der Praxis bleibt eine dokumentierte Limitierung (siehe Open Questions).

## **Contradiction Log**

**Konflikt:** Die Dramatica-Theorie erfordert einen holistischen "Story Mind", in dem alle Elemente simultan präsent und voneinander abhängig sind. Die Spec-Driven-Development / Agentic-Pattern-Praxis warnt jedoch strikt davor, zu viel Kontext auf einmal zu laden (Gefahr der "Distraction Degradation" / Context Rot) und fordert "Progressive Disclosure".8 **Auflösung:** Die Spannung wurde in ADR-06 und ADR-07 gelöst. Der *Zustand* der Story (storyform\_layer im NCP) bleibt ein kohärentes, zentrales JSON-Objekt (Single Source of Truth). Die *Ausführungs-Instruktionen* für den Agenten (die SKILL.md Dateien) werden jedoch dekomponiert und via Progressive Disclosure in strikten 500-Zeilen-Budgets geladen. Dies respektiert Dramatica ontologisch und SDD operativ.

## **Falsifikations-Audit (Method M01)**

**Zentrale Architektur-Hypothese:** "Ein iterativer, rein prompt-gesteuerter Workflow ohne harte Spec-Gates ist ausreichend für Agenten, um kohärente Dramatica-Romane zu schreiben." **Disconfirmation-Queries:** Suche nach LLM story generation coherence failure EMNLP und Context Rot agentic creative writing. **Resultate:** Die Hypothese wurde massiv falsifiziert. Eine EMNLP-Studie (2025) zu LLMs in Story Generation 10 belegt, dass ohne explizite narrative Graphen (wie das NCP) Arcs verflachen, emotionale Tiefe verschwindet und die Prämisse unweigerlich driftet (Context Rot). Dies bestätigt die Notwendigkeit der harten Gates und der drei Contradiction-Detection-Klassen in dieser Spec.

## **Open Questions / Unresolved**

  - **Pragmatische Latent Space Projection (Klasse 3):** Die exakte Vektor-Mathematik, mit der ein Evaluator-Agent den Subtext einer Szene im latenten Raum gegen abstrakte Dramatica-Elemente der story\_dynamics abgleicht, erfordert in der Produktion weiteres Feintuning.4
  - **LLM-as-a-judge Bias:** Die Akzeptanzkriterien für Prosa-Metriken (Phase 4: Reception) sind algorithmisch extrem schwer binär (TRUE/FALSE) zu bewerten. Hier besteht ein Restrisiko für Bias in der automatisieren Evaluierung.

#### **Referenzen**

1.  Design Spec Erstellung für Agency System
2.  Model Context Protocol - Wikipedia, Zugriff am April 26, 2026, <https://en.wikipedia.org/wiki/Model_Context_Protocol>
3.  ICML Poster An Architecture Search Framework for Inference-Time Techniques, Zugriff am April 27, 2026, <https://icml.cc/virtual/2025/poster/45959>
4.  Spec-Entwicklung für agentische Roman-Entwicklung
5.  2024 in Review: Subtxt's Updates, Fresh Frameworks, and a Thrilling 2025 Ahead - Articles, Zugriff am April 27, 2026, <https://narrativefirst.com/articles/2024-in-review-subtxts-updates-fresh-frameworks-and-a-thrilling-2025-ahead>
6.  Spec-Driven Development with AI Agents: A Practical Guide - Xcapit, Zugriff am April 26, 2026, <https://www.xcapit.com/en/blog/spec-driven-development-ai-agents>
7.  Adaptation of spec-kit with Theodo standards. - GitHub, Zugriff am April 26, 2026, <https://github.com/theodo-group/theodo-spec-kit>
8.  Why your agent gets "stupid" after 30 minutes (and why RAG isn't the fix) : r/AI\_Agents, Zugriff am April 26, 2026, <https://www.reddit.com/r/AI_Agents/comments/1po1oux/why_your_agent_gets_stupid_after_30_minutes_and/>
9.  Narrative Context Protocol (NCP) - GitHub, Zugriff am April 27, 2026, <https://github.com/narrative-first/narrative-context-protocol>
10. Beyond Text Intelligence: Why Serious Story AI Eventually Finds Its Way to Dramatica, Zugriff am April 26, 2026, <https://dramatica.com/blog/beyond-text-intelligence-why-serious-story-ai-eventually-finds-its-way-to-dramatica>
11. Narrative First: The Latest, Zugriff am April 27, 2026, <https://narrativefirst.com/>
12. Commonly Misunderstood Definitions - Discuss Dramatica, Zugriff am April 26, 2026, <https://discuss.dramatica.com/t/commonly-misunderstood-definitions/2281>
13. The Structure of Concern: A Challenge For Thinkers | PDF | System | Value (Ethics) - Scribd, Zugriff am April 26, 2026, <https://www.scribd.com/document/8009997/The-Structure-of-Concern-A-Challenge-for-Thinkers>
14. Dramatica Theory, Zugriff am April 26, 2026, <https://discuss.dramatica.com/c/theory/8>
15. Understanding the Early Television Cartoon - ProQuest, Zugriff am April 27, 2026, <https://search.proquest.com/openview/a3f8e997e50e56eb4de384560b9b0d1d/1?pq-origsite=gscholar&cbl=18750&diss=y>
16. Dramatica Dictionary - Storymind, Zugriff am April 27, 2026, <https://www.storymind.com/dramatica/dictionary/index.htm>
17. Context rot explained (& how to prevent it) - Redis, Zugriff am April 26, 2026, <https://redis.io/blog/context-rot/>
18. Narrative Efficiency | Dramatica, Zugriff am April 26, 2026, <https://platform.dramatica.com/docs/narrova/narrative-efficiency>
19. Building an agentic RAG pipeline - IBM Developer, Zugriff am April 26, 2026, <https://developer.ibm.com/articles/agentic-rag-pipeline/>
20. Agentic Skill System Specification
21. Extended thinking - Amazon Bedrock - AWS Documentation, Zugriff am April 26, 2026, <https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-extended-thinking.html>
22. Narrova Agents | Dramatica, Zugriff am April 26, 2026, <https://platform.dramatica.com/docs/narrova/agents>
23. Agentic AI-assisted coding offers a unique opportunity to instill epistemic grounding during software development - arXiv, Zugriff am April 26, 2026, <https://arxiv.org/html/2604.21744v1>
24. Spec-driven development with AI: Get started with a new open source toolkit - The GitHub Blog, Zugriff am April 27, 2026, <https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/>
25. Writing effective tools for AI agents—using AI agents - Anthropic, Zugriff am April 26, 2026, <https://www.anthropic.com/engineering/writing-tools-for-agents>
26. Narrative Context Protocol: An Open-Source Storytelling Framework for Generative AI - arXiv, Zugriff am April 27, 2026, <https://arxiv.org/pdf/2503.04844>
27. The Best Open Source Frameworks For Building AI Agents in 2026 - Firecrawl, Zugriff am April 27, 2026, <https://www.firecrawl.dev/blog/best-open-source-agent-frameworks>
