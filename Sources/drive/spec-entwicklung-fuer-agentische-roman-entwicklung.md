---
drive_id: "1B1UqQeEHsC2sa3PSnGkBw4nS_vY4keKLIM4IWLc6-LA"
title: "Spec-Entwicklung für agentische Roman-Entwicklung"
slug: "spec-entwicklung-fuer-agentische-roman-entwicklung"
category: "plot-outline"
tier: "T3-work"
index_date: "2026-04-26"
fetched: "2026-09-26"
---

# **Spec-Driven Specification Artifact für agentic Dramatica-basierte Novel-Entwicklung**

## **Exekutive Architekturspezifikation**

Die vorliegende Spezifikation operationalisiert die Dramatica-Theorie der Erzählung für den Einsatz in autonomen, durch Large Language Models (LLMs) gesteuerten Multi-Agenten-Systemen. Sie fungiert als primäres, ausführbares Artefakt im Sinne des Spec-Driven Design (SDD) und erzwingt eine deterministische, kohärente Romanentwicklung. Die Architekturvorgabe (Komponente A) verlangt zwingend die Definition einer vollständigen Output-Architektur-Spezifikation, welche Sektionen, Schemata und Akzeptanzkriterien für die Spezifikation selbst als auslieferbares Artefakt umfasst. Parallel dazu diktiert die Operationalisierungsvorgabe (Komponente O), dass diese Spezifikation agentisch ausführbar sein muss. Dies inkludiert zwingend Phasen-Transitions-Verträge, asynchrone Protokolle für Klärungsfragen (Clarifying-Question-Protokolle), Speichermanagement-Strukturen (Memory-Management) und detaillierte Wiederherstellungsmuster (Recovery-Patterns) bei Systemfehlern. Beide Komponenten bilden das unverrückbare Fundament dieses Dokuments und werden im Folgenden in eine maschinenlesbare und gleichzeitig konzeptionell stringente Form übersetzt.

## **Operationale Grenzen und Agentenprofil**

Die Spezifikation setzt ein konsumierendes agentisches System voraus, das über fortgeschrittene Fähigkeiten im Bereich der strukturierten Generierung und Zustandserhaltung verfügt. Das System muss Model Context Protocol (MCP) Standardkonventionen 1 unterstützen, um den narrativen Zustand (Working-State) von der reinen Inferenz zu entkoppeln. Es wird eine ReAct-ähnliche oder ARCHON-basierte Architektur 3 vorausgesetzt, die in der Lage ist, Inferenzzeit-Optimierungen, Ensemble-Generierungen und deterministische Tool-Aufrufe 5 auszuführen. Die Spezifikation ist agnostisch gegenüber dem zugrundeliegenden Basismodell (z. B. GPT-4, Claude 3.5), erfordert jedoch eine strikte Einhaltung von JSON-Schema-Validierungen und die Fähigkeit zur invarianten-basierten Logikprüfung.6

## **Ontologische Architektur: Der Dramatica Story Mind**

Die Dramatica-Theorie betrachtet eine vollständige Geschichte als Analogie für einen einzelnen menschlichen Verstand – den "Story Mind" – der versucht, eine spezifische kognitive Dissonanz oder ein Problem zu lösen.8 Um dieses psychologische Modell für ein agentisches System operationalisierbar zu machen, muss es in eine streng typisierte Graphen- und Baumstruktur übersetzt werden. Die ontologische Ebene definiert die unveränderlichen Dimensionen dieses Modells.10

Das nachfolgende Schema definiert die oberste Ebene des Dramatica-Modells. Es zwingt den Agenten, die vier grundlegenden Kommunikationsstadien und die damit verbundenen strukturellen Metadaten vor jeder Textgenerierung zu fixieren.9



YAML




$schema: "http://json-schema.org/draft-07/schema\#"
title: Dramatica Story Mind Ontology
type: object
required: \[metadata, story\_mind, grand\_argument, audience\_positioning\]
properties:
  metadata:
    type: object
    description: "Metadaten, die die übergeordnete Absicht steuern."
    properties:
      author\_argument:
        type: string
        description: "Die zentrale Prämisse und thematische Aussage der Autorenschaft."
  audience\_positioning:
    type: object
    description: "Die Positionierung des Publikums relativ zum Story Mind, definiert durch die vier Kommunikationsstufen.\[9, 12\]"
    properties:
      perspective: { type: string, enum: }
      focus: { type: string, enum: }
  story\_mind:
    type: object
    required: \[throughlines, story\_dynamics, story\_goal\_cluster\]
    properties:
      throughlines:
        type: object
        description: "Die vier fundamentalen Perspektiven (I, You, We, They), die die kognitive Dissonanz einkreisen.\[11, 13\]"
        required: \[objective\_story, main\_character, influence\_character, relationship\_story\]
        properties:
          objective\_story: { $ref: "\#/definitions/throughline" }
          main\_character: { $ref: "\#/definitions/throughline" }
          influence\_character: { $ref: "\#/definitions/throughline" }
          relationship\_story: { $ref: "\#/definitions/throughline" }
      story\_dynamics:
        type: object
        description: "Makro-Parameter, die den zeitlichen und logischen Verlauf steuern."
        required: \[driver, limit, outcome, judgment\]
        properties:
          driver: { type: string, enum: }
          limit: { type: string, enum: }
          outcome: { type: string, enum: }
          judgment: { type: string, enum: }
      story\_goal\_cluster:
        type: object
        description: "Das Netzwerk an Voraussetzungen und Konsequenzen, das an das zentrale Ziel gekoppelt ist."
        required: \[goal, requirement, consequence, forewarning, dividend, cost, prerequisite, precondition\]
        properties:
          goal: { $ref: "\#/definitions/element\_type" }
          requirement: { $ref: "\#/definitions/element\_type" }
          consequence: { $ref: "\#/definitions/element\_type" }
          forewarning: { $ref: "\#/definitions/element\_type" }
          dividend: { $ref: "\#/definitions/element\_type" }
          cost: { $ref: "\#/definitions/element\_type" }
          prerequisite: { $ref: "\#/definitions/element\_type" }
          precondition: { $ref: "\#/definitions/element\_type" }
  grand\_argument:
    type: object
    description: "Die endgültige Synthese, die beweist, dass der spezifische Lösungsansatz der einzig valide war."
    properties:
      resolution: { type: string }

definitions:
  throughline:
    type: object
    required: \[domain, concern, issue, problem\_quad, plot\_sequencing\]
    properties:
      domain: { type: string, enum: \[Universe, Physics, Mind, Psychology\] }
      concern: { type: string }
      issue: { type: string }
      problem\_quad:
        type: object
        description: "Das fundamentale Konflikt-Quartett auf der Element-Ebene."
        required: \[problem, solution, symptom, response\]
        properties:
          problem: { type: string }
          solution: { type: string }
          symptom: { type: string }
          response: { type: string }
      plot\_sequencing:
        type: object
        description: "Die zeitliche Gliederung durch vier Signposts und drei dazwischenliegende Journeys."
        properties:
          signposts:
            type: array
            items: { type: string }
            minItems: 4
            maxItems: 4
          journeys:
            type: array
            items: { type: string }
            minItems: 3
            maxItems: 3
  element\_type:
    type: string
    description: "Referenz auf eines der 64 validen Story-Elemente im Basis-Quad."


Diese ontologische Struktur erzwingt, dass das agentische System nicht lediglich Text produziert, sondern Variablen innerhalb einer hochgradig vernetzten Zustandsmaschine befüllt. Jeder Knoten im Graphen trägt semantische und strukturelle Verantwortung für das Gesamtwerk.

## **Wertebereich und Enumeration (Choice-Space)**

Um Halluzinationen und das Abdriften des Agenten in nicht-theoretische Tropes (Vocabulary Drift) zu verhindern, wird der Choice-Space hart limitiert. Das agentische System darf auf der ontologischen Ebene ausschließlich Entitäten wählen, die durch das Dramatica-Modell kanonisch definiert sind.16



|  |  |  |
| :-: | :-: | :-: |
| \*\*Kategorie\*\* | \*\*Kanonische Entitäten (Enumeration)\*\* | \*\*Semantische Funktion im System\*\* |
| \*\*Domains (Classes)\*\* | Universe (Situation), Physics (Activity), Mind (Fixed Attitude), Psychology (Manipulation) | Die höchste Ebene der Struktur. Sie separiert externe von internen Konflikten und Zustände von Prozessen.9 |
| \*\*Concerns (Types)\*\* | Past, Progress, Future, Present, Understanding, Doing, Obtaining, Learning, Memory, Preconscious, Subconscious, Conscious, Conceptualizing, Conceiving, Being, Becoming | 16 spezifische Typen, die als primärer thematischer Fokus innerhalb einer Domain dienen.9 Jeder Throughline muss genau ein Concern zugewiesen werden. |
| \*\*Story Dynamics\*\* | Action/Decision, Timelock/Optionlock, Success/Failure, Good/Bad | Parameter, die das Pacing und die kausale Auflösung bestimmen. Ein \*Timelock\* erfordert vom Agenten eine explizite zeitliche Limitierung im Plot-Sequencing, ein \*Optionlock\* eine zählbare Reduktion von Lösungsräumen.9 |
| \*\*64 Elements (Quads)\*\* | Knowledge, Thought, Ability, Desire (Basis); Pursuit, Avoid, Help, Hinder, Control, Uncontrolled, Faith, Disbelief, Logic, Feeling, Oppose, Support, etc. | Die fundamentalsten Bausteine der Narration. Charaktere sind Agenten, die diese Elemente repräsentieren. Ein Problem, eine Solution, ein Symptom und eine Response bestehen jeweils zwingend aus diesen Elementen.16 |

Das System muss diese Tabellen als Vektor-Embeddings oder statische Lookup-Dictionaries bereithalten, um bei jedem Tool-Call die Zulässigkeit der Argumente zu verifizieren.19

## **Strukturelle Interaktions-Constraints**

Die Zuweisung von Elementen aus dem Choice-Space in die Ontologie ist nicht beliebig. Die Dramatica-Theorie postuliert, dass narrative Bedeutung erst durch die relative Positionierung von Konflikten entsteht. Folglich implementiert diese Spezifikation restriktive Interaktions-Constraints, die das agentische System validieren muss.14



|  |  |  |
| :-: | :-: | :-: |
| \*\*Constraint-Identifikator\*\* | \*\*Formale Regel\*\* | \*\*Strukturelle Begründung\*\* |
| \*\*IC-01: Diagonalität der Throughlines\*\* | Domain(Main Character) und Domain(Influence Character) müssen im Dramatica-Modell diagonal gegenüberliegen (z.B. Universe vs. Mind oder Physics vs. Psychology). Gleiches gilt zwingend für Domain(Objective Story) und Domain(Relationship Story).14 | Diese Anordnung maximiert die narrative Reibung. Ein Main Character, der mit einer physischen Aktivität kämpft (Physics), muss durch einen Influence Character herausgefordert werden, der psychologisch manipuliert (Psychology), um eine echte kognitive Alternative darzustellen.14 |
| \*\*IC-02: Concern Thematic Alignment\*\* | Die gewählten Concerns aller vier Throughlines müssen in das strukturell identische relative Quad der jeweiligen Domain fallen.14 | Verhindert, dass die vier Erzählstränge thematisch auseinanderbrechen. Das Argument des Autors bleibt fokussiert. |
| \*\*IC-03: Dynamische Element-Paarung\*\* | Innerhalb des Element-Quads für eine Throughline fungieren Problem und Solution als exklusives dynamisches Paar. Ebenso Symptom und Response.16 | Garantiert, dass die Lösung das exakte strukturelle Gegenteil des Problems darstellt und die Heilung der initialen kognitiven Dissonanz mathematisch geschlossen ist.9 |
| \*\*IC-04: Story Growth Verknüpfung\*\* | Wenn Domain(OS) und Domain(MC) beide intern oder beide extern sind, muss der Growth-Wert "Stop" sein. Sind sie entgegengesetzt (intern/extern), ist der Wert zwingend "Start".14 | Koppelt die Notwendigkeit der persönlichen Entwicklung des Protagonisten logisch an die objektive Natur des Konflikts. |

Jeder Versuch des agentischen Systems, einen Zustand zu generieren, der diese Constraints verletzt, wird vom Validator auf Protokollebene blockiert und zwingt das Modell in eine Re-Evaluierung.22

## **Deklaration der Coherence-Invarianten**

In Anlehnung an formale Verifikationsmethoden 5 und Konzepte der relationalen Blockwelt-Architektur 23 definiert diese Spezifikation narrative Kontinuität als die Erhaltung struktureller Invarianten unter Transformation. Das System muss sicherstellen, dass bestimmte Eigenschaften über den gesamten Verlauf der Story-Entwicklung unverletzt bleiben.

1.  **INV-01: Domänen-Singularität**

<!-- end list -->

  - **Deklaration**: Keine zwei Throughlines dürfen zu irgendeinem Zeitpunkt dieselbe Domain belegen. count(unique()) == 4.
  - **Detection-Heuristik**: Regelbasierter Check des globalen JSON-Zustands nach jeder Transition in Phase 1 und Phase 2.
  - **Severity**: BLOCKER.
  - **Resolution-Protokoll**: Deterministischer Rollback des States durch das System. Ausgabe einer Fehler-Direktive an den ausführenden Agenten zur Neuallokation.

<!-- end list -->

1.  **INV-02: Synchronisation der finalen Dynamik**

<!-- end list -->

  - **Deklaration**: Ein Story Outcome von Success in Kombination mit einem Story Judgment von Good erfordert zwingend, dass die in der Storyforming-Phase etablierte Solution des Main Characters im vierten Signpost explizit angewandt wird.9
  - **Detection-Heuristik**: Hybride Prüfung. Die Agenten-Architektur durchsucht das resultierende Manuskript des vierten Akts mittels LLM-RAG nach semantischer Ähnlichkeit zum Solution-Element.
  - **Severity**: WARNING.
  - **Resolution-Protokoll**: Trigger des Clarifying-Question-Protokolls. Der menschliche Operator muss entscheiden, ob das Ende als tragisch (Failure) reklassifiziert wird oder ob die Szene neu generiert werden soll.

<!-- end list -->

1.  **INV-03: Archetypische Motivationsexklusion**

<!-- end list -->

  - **Deklaration**: Ein einzelner Charakter-Agent in der Objective Story darf niemals zwei Elemente aus demselben dynamischen Paar (z. B. *Pursuit* und *Avoid*) gleichzeitig innehaben, es sei denn, er ist explizit als komplexer Charakter deklariert.17
  - **Detection-Heuristik**: Array-Intersection-Check auf der Charakter-Attribut-Tabelle.
  - **Severity**: BLOCKER.
  - **Resolution-Protokoll**: Auto-Flagging der Charakterdefinition. Das System zwingt den Agenten, die Konfliktlinien auf einen neuen Nebencharakter auszulagern.

<!-- end list -->

1.  **INV-04: Strikte Signpost-Chronologie**

<!-- end list -->

  - **Deklaration**: Die Entwicklung der Handlung muss streng den vier Signposts pro Throughline folgen, verbunden durch genau drei definierte Journeys.15 Rückschritte in der Problemauflösung sind strukturell untersagt.
  - **Detection-Heuristik**: LLM-basierte Vektorprüfung zur Laufzeit, die abgleicht, ob der erzählte Zustand der Szene dem Index des aktuellen Signposts entspricht.25
  - **Severity**: BLOCKER.
  - **Resolution-Protokoll**: Hard-Stop. Die Generierungspipeline pausiert, der Agent verwirft die letzten N-Szenen und rekonstruiert den Anschluss an die vorherige Journey.

<!-- end list -->

1.  **INV-05: Thematische Intentionserhaltung**

<!-- end list -->

  - **Deklaration**: Jede generierte Aktion, die das Story Goal beeinflusst, muss positiv mit dem definierten *Author's Argument* korrelieren, um pragmatische Widersprüche zu vermeiden.9
  - **Detection-Heuristik**: Decoupled Visual/Semantic Encoding nach dem Janus-Prinzip.27 Ein separater Evaluator-Agent projiziert den Szeneninhalt in einen latenten semantischen Raum und misst die Distanz zur initialen Prämisse.
  - **Severity**: NOTICE.
  - **Resolution-Protokoll**: Der Agent initiiert einen internen Self-Correction-Loop, justiert die Narrative und vermerkt den Drift im Execution-Memory.28

## **Mehrstufige Contradiction-Detection**

Autonome Systeme leiden in offenen Umgebungen, insbesondere bei großen Kontextfenstern, unter massivem Task Drift und kontextueller Fäulnis (Context Rot).19 Die bloße Vermeidung von Widersprüchen ist unzureichend. Diese Spezifikation zwingt das Agenten-System zur Implementierung einer dreistufigen, aktiven Widerspruchserkennung.29

### **Klasse 1: Strukturelle Contradictions**

  - **Definition**: Formale Regelbrüche gegen die Dramatica-Ontologie (z. B. ein Story Limit, das weder Timelock noch Optionlock ist).
  - **Detection-Heuristik**: Deterministische Validierung des Working-State-Dokuments gegen das definierte JSON/YAML-Schema vor jedem Commit.31
  - **Schweregrad**: BLOCKER.
  - **Resolution-Protokoll**: Das Model Context Protocol (MCP) verweigert die Transaktion. Der Agent führt einen State Rollback (State Reversion) durch und erhält den genauen JSON-Path des Fehlers als System-Feedback.22

### **Klasse 2: Inhaltliche Contradictions**

  - **Definition**: Semantische Brüche innerhalb der erzählten Welt. Beispiel: Ein Charakter, dessen Motivationselement als *Logic* definiert wurde, trifft in einer kritischen Situation eine rein von Emotionen (*Feeling*) getriebene Kernentscheidung, ohne dass ein Journey-Übergang dies legitimiert.33
  - **Detection-Heuristik**: Retrieval-Augmented Generation (RAG) mit Cross-Output Alignment Analysis. Ein Supervisor-Agent nutzt MCP, um historische Fakten parallel zur aktuellen Generierung abzufragen und auf Konsistenzrisiken (Consistency Risk Score) zu prüfen.6
  - **Schweregrad**: WARNING. Inhaltliche Widersprüche können gelegentlich stilistisch gewollt sein (z. B. unzuverlässiges Erzählen).
  - **Resolution-Protokoll**: Ein Einspruchsverfahren wird eingeleitet. Der generierende Agent muss dem Supervisor-Agenten eine logische Herleitung (Chain-of-Justification) präsentieren. Gelingt dies nicht, greift das Clarifying-Question-Protokoll.

### **Klasse 3: Pragmatische Contradictions**

  - **Definition**: Meta-narrative Widersprüche, bei denen lokale Szenenhandlungen die globale thematische Prämisse untergraben.34 Beispiel: Die Prämisse erfordert ein Scheitern (*Failure*), aber die generierte Szene impliziert eine unvermeidbare Lösung des Story Goals.
  - **Detection-Heuristik**: Laufende Anwendung von Architektur-Paradigmen, die Inferenz- und Bewertungsräume trennen (ähnlich JanusFlow 27). Der abstrakte Subtext der Szene wird extrahiert und gegen die Story-Dynamics verglichen.
  - **Schweregrad**: BLOCKER. Pragmatische Brüche zerstören die Kohärenz des "Story Minds".
  - **Resolution-Protokoll**: Der Prozess hält an. Das System formuliert einen expliziten Trade-off-Vorschlag an den menschlichen Operator.

## **Das Clarifying-Question-Protokoll (CQ)**

Die Interaktion zwischen dem autonomen Agenten-System und dem menschlichen Supervisor muss stark strukturiert sein, um Ermüdung (Alert Fatigue) und "Lazy Querying" (der Agent fragt bei jedem Schritt nach) zu unterbinden.36

**Trigger-Bedingungen für asynchrone Eskalation:**

1.  Der Konsistenz-Evaluator meldet eine Klasse-2-Contradiction mit einem CRS (Consistency Risk Score) von über 85%.6
2.  Eine Klasse-3-Contradiction wurde detektiert.
3.  Der Suchraum für die Behebung eines INV-02 oder INV-04 Verstoßes überschreitet das zugewiesene Token- oder Rechenbudget (Inference-Time Budget Exhaustion 3).

**Strukturiertes Frage-Format (YAML-RPC):**

Jede Frage, die das System an den Menschen richtet, muss als strukturiertes Payload übermittelt werden.



YAML




cq\_event:
  id: "CQ-8934"
  timestamp: "ISO8601"
  phase\_context: "Phase 3 - Story Weaving"
  conflict\_description: "Die detektierte Handlung von Charakter X in Signpost 3 widerspricht der etablierten Motivation (Avoid)."
  severity: "WARNING"
  context\_references:
    - path: "/working\_state/encoding\_context/characters/X"
    - path: "/working\_state/weaving\_timeline/act\_3"
  proposed\_options:
    - option\_id: 1
      description: "Beibehalten des neuen Zustands, Aktualisierung der Charakter-Motivation auf 'Pursuit'."
      impact\_analysis: "Verletzt INV-03 (Exklusion). Erfordert die Einführung eines neuen Antagonisten für das 'Avoid'-Element."
    - option\_id: 2
      description: "Verwerfen der Szene und Re-Generierung unter hartem Constraint 'Charakter X flieht'."
      impact\_analysis: "Verzögert die Story-Lösung. Plot-Outline muss minimal angepasst werden."
  default\_recommendation: 2
  rationale\_for\_default: "Option 2 erhält die Integrität des Storyforms bei geringsten Kaskadeneffekten auf Phase 1."


**Antwort-Integrations-Mechanismus:** Wählt der Mensch Option 2, führt das System einen deterministischen State-Rollback aus.28 Wählt er Option 1, wird ein dedizierter "Patch"-Lauf gestartet. Das betroffene Element im story\_mind wird überschrieben und alle nachgelagerten Felder, die davon abhängen, werden mit dem Flag requires\_rework: true versehen, was den Agenten zwingt, diese in der nächsten Iteration zu reparieren.

## **Sequenzielle Phasen-Transitions-Verträge**

Die Spezifikation gliedert die Romanentwicklung nach den vier originalen Kommunikationsstadien von Dramatica 9 und übersetzt diese in harte Spec-Driven-Development Phasen.39 Ein Phasenübergang erfolgt nur, wenn alle Akzeptanzkriterien 40 erfüllt sind.



|  |  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: | :-: |
| \*\*Phase & Beschreibung\*\* | \*\*Pre-Conditions (Eintrittsbedingungen)\*\* | \*\*In-Phase-Activities (Agenten-Aktionen)\*\* | \*\*Acceptance Criteria (Binär)\*\* | \*\*Post-Conditions (Ausgabe)\*\* | \*\*Immutable Fields nach Transition\*\* |
| \*\*Phase 1: Storyforming\*\* Die Erstellung des abstrakten mathematischen Modells.9 | Die Metadaten (z. B. author\\\_argument) sind initialisiert. | Der Agent berechnet die 75 Appreciations. Er weist den Throughlines die Domains und Concerns zu und konfiguriert die Dynamics.14 | \\- Das story\\\_mind JSON-Schema validiert fehlerfrei. \\- INV-01, IC-01, IC-02, IC-03 und IC-04 sind TRUE. \\- Keine strukturellen Fehler (Klasse 1). | Ein formell korrekter, kompletter Storyform-Datensatz. | Das gesamte story\\\_mind-Objekt wird gegen Schreibzugriffe gesperrt. |
| \*\*Phase 2: Story Encoding\*\* Die Übersetzung der Abstraktion in narrative Konzepte, Charaktere und Welten.12 | Phase 1 ist erfolgreich abgeschlossen. story\\\_mind ist vorhanden. | Der Agent entwirft Charakter-Avatare, weist ihnen Motivationselemente zu. Er definiert das Setting (Universe) und die Handlungsmechaniken (Physics).17 | \\- Jeder Charakter ist mit mindestens einem Element verknüpft. \\- INV-03 evaluiert zu TRUE. \\- Die Generierung weist keine inhaltlichen Widersprüche (Klasse 2) zum Storyform auf. | Eine umfassende Charakter- und Welt-Bibel (encoding\\\_context). | Zuordnungen von Element-Quads zu spezifischen Charakter-IDs. |
| \*\*Phase 3: Story Weaving\*\* Die Sequenzierung der encodierten Elemente in eine zeitliche Abfolge.9 | Phase 2 ist abgeschlossen. Alle Elemente haben Repräsentanten. | Der Agent webt die Ereignisse durch vier Signposts pro Throughline und verbindet diese durch drei Journeys. Er definiert den szenischen Ablauf (Plot Outline). | \\- Exakt 4 Signposts pro Throughline sind definiert. \\- Alle Journeys verbinden Signposts ohne logische Brüche. \\- INV-04 (Chronologie) evaluiert zu TRUE. | Ein detaillierter, chronologischer Plot-Outline (weaving\\\_timeline). | Die Reihenfolge der Signposts und die Struktur der Journeys. |
| \*\*Phase 4: Story Reception\*\* Die Synthese der Prosa und die Validierung der Wirkung.12 | Phase 3 ist abgeschlossen. Der Plot-Outline liegt vor. | Der Agent generiert szenische Prosa basierend auf dem Outline. Er passt Ton und Pacing an die Vorgaben des Publikums (audience\\\_positioning) an. | \\- Prosa-Text für jeden Outline-Punkt existiert. \\- Klasse-3-Contradiction-Detection läuft ohne Befund durch. \\- INV-02 und INV-05 evaluieren zu TRUE. | Das finale Manuskript des Romans. | N/A (Der Text kann in iterativen Sub-Loops weiter verfeinert werden). |

## **Working-State Schema und Memory Management**

Die Persistenz des Systems wird durch eine Trennung von unveränderlichem Langzeitgedächtnis (Episodic Memory) und veränderbarem Arbeitsgedächtnis (Working Memory) erreicht. Das System nutzt das Model Context Protocol (MCP) 1, um Agenten von der direkten Dateiverwaltung zu entkoppeln und Schema-Brüche zu verhindern.



YAML




working\_state:
  session\_id: string
  current\_phase: integer
  storyform:
    $ref: "\#/definitions/story\_mind"
    is\_immutable: boolean
  encoding\_context:
    characters:
      type: array
      items:
        character\_id: string
        archetype\_mapping: string
        ephemeral\_notes:
          type: string
          description: "Ein dedizierter Bereich für den Agenten zur Speicherung von Reasoning-Traces und temporären Planungen, der bei Bedarf überschrieben werden kann.\[42\]"
    settings:
      type: array
  weaving\_timeline:
    type: array
    items:
      act\_number: integer
      interleaved\_signposts: array
  execution\_memory:
    type: object
    description: "Verwaltung des Fehlerstatus für Fallbacks und Rollbacks."
    properties:
      last\_stable\_hash: string
      active\_flags: array
      retry\_counters: object


Um Kontex-Drift (Context Rot) zu vermeiden 19, wird ein Vektor-RAG-Hybridmodell eingesetzt. Das abstrakte storyform und der aktuelle Phasenvertrag werden als statischer System-Prompt injiziert, während die generierten Prosatexte (aus Phase 4) vektorisiert und über Ähnlichkeitssuche dynamisch in das Kontextfenster des LLMs geladen werden.36

## **Fehlerkatalog (Failure-Modes) und Recovery**

Basierend auf umfassenden Pre-Mortem-Analysen von agentischen Systemen 19 implementiert diese Spezifikation robuste Wiederherstellungspfade für spezifische Versagensmuster.



|  |  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: | :-: |
| \*\*ID\*\* | \*\*Fehlerbeschreibung\*\* | \*\*Detection-Signal\*\* | \*\*Definierter Recovery-Pfad\*\* | \*\*Severity\*\* | \*\*Präventive Heuristik\*\* |
| \*\*FM-01\*\* | \*\*Task Drift\*\* | Der Agent weicht von der aktuellen Phase ab und generiert Szenen, obwohl die Encoding-Phase noch nicht abgeschlossen ist.19 | Local-Recovery: Löschen der kontextfremden Generierung, erneutes Prompting mit striktem Phasen-Constraint.28 | WARNING | Strikte Begrenzung des Tool-Zugriffs per MCP auf phasenrelevante Funktionen.30 |
| \*\*FM-02\*\* | \*\*Parameter Hallucination\*\* | Der Agent erfindet ein Dramatica-Element (z.B. "Revenge"), das nicht im Kanon existiert.19 | Schema-Validator (Klasse 1) wirft eine Exception auf Basis der Enumerationsliste. | Rollback des Zustands zum last\\\_stable\\\_hash. | BLOCKER |
| \*\*FM-03\*\* | \*\*Reward Hacking\*\* | Der Agent löst den Hauptkonflikt bereits in Signpost 2 auf, um das Ziel "Success" effizient zu erreichen.19 | INV-04 Chronology Check schlägt an, da Solution-Elemente vorzeitig injiziert wurden. | Phase-Rollback zur Story Weaving-Phase. Neugestaltung des Pacings durch den Supervisor. | BLOCKER |
| \*\*FM-04\*\* | \*\*Alignment Faking\*\* | Das Modell produziert Text, der thematische Tiefe simuliert, die strukturell nicht im State verankert ist.19 | Pragmatische Contradiction Detection (Klasse 3) meldet Divergenz zwischen Semantik und Struktur. | Hard-Stop und Übergabe an das CQ-Protokoll zur menschlichen Bewertung. | BLOCKER |
| \*\*FM-05\*\* | \*\*Context Rot\*\* | Das Kontextfenster füllt sich, der Agent "vergisst" Entscheidungen aus Phase 1.19 | Zugriffsversuch auf immutable-Felder oder Inkonsistenz im RAG-Retrieval. | Flushing des LLM-Kontextes, Rehydrierung des States aus der MCP-Datenbank.36 | BLOCKER |
| \*\*FM-06\*\* | \*\*Degeneration Loops\*\* | Der Agent gerät in eine Endlosschleife bei dem Versuch, denselben Schemafehler zu korrigieren.19 | Der retry\\\_counter im execution\\\_memory überschreitet den Wert 3. | Eskalation: System stoppt, asynchrones CQ-Event wird gefeuert. | BLOCKER |
| \*\*FM-07\*\* | \*\*Ordering Error\*\* | Tool-Calls werden in fehlerhafter Abhängigkeitsreihenfolge aufgerufen.19 | Das MCP-Backend lehnt den API-Call ab.22 | State-Rollback der letzten Aktion; Instruktions-Reset. | WARNING |
| \*\*FM-08\*\* | \*\*Vocabulary Drift\*\* | Der Agent verliert die analytische Dramatica-Terminologie und verfällt in generische Autoren-Tropes. | Regex-Scan auf Dramatica-Keywords in den Metadaten der Phasen 1 und 2 schlägt fehl. | Forward-Fix: Korrektur-Prompt mit Injektion eines Glossar-Auszugs. | WARNING |
| \*\*FM-09\*\* | \*\*Asymmetric Architecture\*\* | Eine der vier Throughlines wird tokenmäßig massiv unterrepräsentiert.11 | Das Token-Verhältnis zwischen OS und RS im Weaving weicht um mehr als 60% ab. | Automatische Generierung eines Ausgleichs-Prompts für die vernachlässigte Perspektive. | WARNING |
| \*\*FM-10\*\* | \*\*State Overwrite\*\* | Versuchte Modifikation geschützter Felder (z. B. nach Phasen-Transition).30 | Kryptographischer Hash-Mismatch beim Pre-Transition-Check. | Revert auf Systemebene, Transaktion wird ohne Agenteninteraktion abgelehnt. | BLOCKER |

## **Regression-Verification Suite**

Die Spezifikation ist inhärent instabil, wenn asynchrone Korrekturen vorgenommen werden. Jede Modifikation des working\_state durch das CQ-Protokoll erzwingt einen System-Halt, bis die folgenden Tests automatisiert bestanden sind:

1.  **Schema-Re-Validation**: Vollständiger Parse des State-Objekts gegen das Referenz-JSON-Schema.
2.  **Constraint-Propagation Check**: Überprüfung, ob eine Änderung im Character-Encoding (Phase 2) retroaktiv ein Interaction-Constraint (z. B. IC-03) in Phase 1 verletzt.
3.  **Invarianten-Audit**: Rekursive Evaluierung von INV-01 bis INV-05. Das System darf den Generierungsprozess erst fortsetzen, wenn alle Flags auf TRUE stehen.

# \-----**Systemic Architectural Audit and Evaluative Records**

Die Konstruktion der vorliegenden Spezifikation resultiert aus einem iterativen Designprozess, der formale Methoden zur Architekturoptimierung nutzt. In diesem Segment werden die Entscheidungsbäume, Stresstests und Evaluationen dargelegt, die zur Ausformung der Spezifikation führten. Sie dokumentieren die konzeptionelle Belastbarkeit der Architektur.

## **Architectural Decision Records (ADRs)**

Die Konsolidierung von Dramatica-Theorie, Spec-Driven Design und Agentic Execution Patterns offenbarte tiefgreifende konzeptionelle Konflikte, die durch explizite Architekturentscheidungen aufgelöst wurden.

### **ADR-01: Spezifikations-Format (Syntax und Semantik)**

**Status:** Akzeptiert. **Kontext:** Die Dramatica-Theorie ist textuell und philosophisch komplex 9, was für Narrative spricht. SDD erfordert jedoch strukturierte, maschinenlesbare Verträge. Agentische Systeme leiden unter Token-Erschöpfung bei ineffizienten Formaten. **Erwogene Optionen:**

  - *Option A:* Reines Markdown. (Pro: Höchste Lesbarkeit für Menschen. Contra: Keine harte Schema-Validierung für Agenten möglich).
  - *Option B:* Reines JSON Schema. (Pro: Deterministische Validierung. Contra: Fehlende Erklärbarkeit der komplexen Dramatica-Semantik).
  - *Option C:* Hybrid-Container (Markdown für deklarative Semantik, eingebettetes YAML/JSON für Schemata und Zustände). **Entscheidung:** Option C wurde gewählt. Die Praxis des GitHub spec-kit und der Anthropic SKILL.md Standards 39 belegt, dass hybride Formate den optimalen Trade-off zwischen menschlicher Kontrollierbarkeit und agentischer Ausführbarkeit (Executable Specifications) bieten. **Konsequenzen:** Das agentische System muss zwingend über Parser-Fähigkeiten (z.B. via MCP) verfügen, um die strukturierten Blöcke aus dem Container zu extrahieren. **Falsifikations-Test:** Würden Agenten wiederholt halluzinieren, weil sie YAML innerhalb von Markdown fehlerhaft parsen, müsste das Paradigma zu getrennten Dateien wechseln. Die Dominanz des SKILL.md-Ansatzes falsifiziert dieses Risiko unter aktuellen Modellen. **Verworfene Alternativen:** Option B (Reines JSON) wurde objektiv verworfen, da der "Story Mind" zwingend semantische Metadaten (wie das *Author's Argument*) benötigt, die in reinen Datenschemata ohne begleitenden Beschreibungstext kontextlos würden.

### **ADR-02: Phasen-Granularität und Linearität**

**Status:** Akzeptiert. **Kontext:** SDD arbeitet traditionell in drei Phasen (Specify, Plan, Implement).39 Agentische Pattern-Literatur 36 präferiert Micro-Phasen für schnelles Rollback. Dramatica definiert vier Makro-Kommunikationsstufen.9 **Erwogene Optionen:**

  - *Option A:* Drei SDD-konforme Pipeline-Phasen.
  - *Option B:* Vier lineare Phasen analog zu den Dramatica-Stadien.
  - *Option C:* Episodisches Modell (Iterative Loops pro Akt). **Entscheidung:** Option B (Storyforming, Encoding, Weaving, Reception). Das Phasenmodell von Dramatica 9 ist nicht arbiträr, sondern spiegelt den physikalischen Aufbau von Bedeutung wider. Die Übernahme dieser Stufen als agentische Phasen erzeugt die höchste logische Kohärenz. **Konsequenzen:** Die Architektur zwingt den Agenten, das gesamte abstrakte Modell (Storyforming) zu komplettieren, bevor auch nur ein Charakter erdacht wird. Die zeitliche Abfolge (Signposts) wird strikt erst in Phase 3 gewebt. **Falsifikations-Test:** Würde das Modell in Phase 2 kontinuierlich chronologische Fehler erzeugen, wäre dies Evidenz dafür, dass das Weaving vorverlegt werden muss. Die klare Trennung von Struktur und Zeit in der Theorie stützt jedoch Option B.

### **ADR-03: Validierungsfrequenz der Kohärenz-Invarianten**

**Status:** Akzeptiert. **Kontext:** Ein System kann Invarianten nach jedem Token (kontinuierlich), nach Abschluss einer Phase (gated) oder hybrid prüfen. **Entscheidung:** Hybrides Validierungsmodell. Strukturelle Kontingenz (Klasse 1) wird "on-write" bei jeder Manipulation des JSON-Schemas validiert.31 Inhaltliche und pragmatische Invarianten (Klasse 2 & 3) werden ausschließlich vor Phasen-Übergängen als "Gate" geprüft. **Begründung:** Kontinuierliche semantische Prüfungen übersteigen das Token-Budget und stören die Inferenzgeschwindigkeit massiv (ARCHON Limitierungen 3). Der hybride Ansatz erlaubt dem Agenten "Scratchpad"-Reasoning innerhalb der Phase, ohne sofort geblockt zu werden.

### **ADR-04: Architektur der Contradiction-Detection**

**Status:** Akzeptiert.

**Kontext:** Wie werden narrative Brüche zuverlässig identifiziert?

**Erwogene Optionen:**

  - *Option A:* Rein regelbasiert (Deterministisch).
  - *Option B:* Rein LLM-basiert (Semantisch).
  - *Option C:* Multi-Layer (Regeln + Heuristiken + RAG-Evaluator). **Entscheidung:** Option C. Inspiriert von fortgeschrittenen "Policy-as-Code & Runtime Authorization" Architekturen.19 Die Ontologie nutzt strikte Graphenregeln, während der inhaltliche Drift durch LLM-gestützte Vektorsuche evaluiert wird.33 **Verworfene Alternativen:** Ein rein LLM-basierter Ansatz (Option B) wurde verworfen, da LLMs bekanntermaßen Probleme mit exakten Zähl- und Logikaufgaben haben (z. B. das Erhalten von exakt 4 diagonalen Pairings).

### **ADR-05: Repräsentation des Working-State**

**Status:** Akzeptiert. **Entscheidung:** Der Zustand wird als dekomponiertes JSON-Objekt (working\_state) verwaltet. Er trennt strikt zwischen immutable (Storyform) und ephemeral (Notes) Zuständen. Diese Architektur löst den Konflikt zwischen Dramaticas Forderung nach einem holistischen Ganzen und der agentischen Notwendigkeit für lokale State-Updates ohne Re-Write-Kosten. Die Integration erfolgt primär über MCP.1

### **ADR-06: Memory-Management-Pattern**

**Status:** Akzeptiert. **Entscheidung:** Implementierung eines Vektor-RAG Hybridsystems. Das strukturierte Storyform (Phase 1) wird in das System-Prompt geladen (Zero-Degradation), während die ausufernde Prosa (Phase 4) in einer Vektordatenbank gehalten wird.36 Dies verhindert den "Context Rot" 19, der andernfalls die Strukturpräzision in späteren Kapiteln zerstören würde.

### **ADR-07: Interface für das Clarifying-Question-Protokoll**

**Status:** Akzeptiert. **Entscheidung:** Das CQ-Protokoll nutzt asynchrone, enumerierte Queries. Agenten dürfen keine offenen Freitextfragen stellen. Sie müssen stattdessen strukturierte YAML-Fragestellungen formulieren, die dem Menschen explizite Trade-offs und Impact-Analysen präsentieren. Dies mitigiert die Gefahr, dass der Agent bei jedem marginalen Konflikt aufgibt und die Autonomie untergräbt.28

### **ADR-08: Fehler-Recovery-Muster**

**Status:** Akzeptiert. **Entscheidung:** Implementierung von kontextsensitiven Recovery-Strategien.28 Deterministischer State-Rollback (State Reversion) bei Schema-Brüchen (Klasse 1). Forward-Fix (korrigierendes Prompting) bei marginalen inhaltlichen Abweichungen (Klasse 2). Dies minimiert den Rechenverlust bei gleichzeitiger Aufrechterhaltung der Strukturintegrität.

## **Systemstatus-Evaluierungen und Auditprotokolle**

Der folgende Abschnitt dokumentiert die epistemologische Validierung der Systemarchitektur. Durch die Anwendung struktureller Kritikmethoden (Pre-Mortem, Red Team, Falsifikation, Query-Expansion) wurde die Spezifikation iterativ gehärtet. Diese systematischen Evaluierungsblöcke repräsentieren den Erkenntnisgewinn über die Zeitachse der Systemgestaltung.

**Evaluierungsblock 1 bis 5 (Dekomposition und Basisabgleich):**

Die initiale Definition des "Story Minds" offenbarte eine signifikante Gefahr der Überkomplexität. Die Konfidenz in die Modellierbarkeit aller 64 Dramatica-Elemente in einer flachen Datei war anfangs gering. Das stärkste Gegenargument war die hierarchische Natur der Dramatica-Theorie, in der Elemente dynamisch ihre Relevanz wechseln (z. B. Problem vs. Symptom). Die Lösung lag in der Einführung der strengen Typisierung (element\_type) im JSON-Schema, welche die Vererbung simuliert, ohne die flache Architektur des JSON zu brechen. Dies verbesserte die maschinelle Lesbarkeit für das MCP-Backend eklatant.

**Evaluierungsblock 6 bis 10 (Spezifikationsformat und SDD-Integration):** Die Untersuchung der Spec-Driven-Development Praxis, insbesondere des GitHub spec-kit 39, etablierte die Notwendigkeit von "Acceptance Criteria" als harte Gates. Es wurde erkannt, dass narrative Agenten dazu neigen, Phasen vorzeitig abzuschließen (Reward Hacking 19). Die Konfidenz stieg deutlich an, nachdem die Dramatica-Kommunikationsstadien (Storyforming, Encoding, Weaving, Reception) exakt auf SDD-Phasen gemappt wurden. Der entscheidende Durchbruch war die Erkenntnis, dass die Storyforming-Phase zu 100% abstrakt bleiben muss – jegliche Einmischung von Charakter-Namen in Phase 1 würde das Schema korrumpieren.

**Evaluierungsblock 11 bis 15 (Kontradiktions-Erkennung und Janus-Architektur):** Die größte architektonische Herausforderung stellte die "Pragmatische Contradiction" dar. Wie erkennt ein mathematisches Modell, dass ein metaphorischer Szenenverlauf der globalen Prämisse widerspricht? Recherchen in den Bereichen der multimodalen Inkongruenz-Erkennung 34 und Decoupled Encoding (analog zur JanusFlow Architektur 27) lieferten die Blaupause. Durch die Entkopplung der "Erzähl-Generierung" von der "Struktur-Bewertung" kann ein Evaluator-Agent den Subtext einer Szene unabhängig bewerten. Dies schloss die kritischste Lücke in der System-Ausfallsicherheit.

**Evaluierungsblock 16 bis 20 (Adversarial Query Expansion und Memory):** Um einen Local-Minimum-Lock-in zu verhindern, wurde das Suchraster über klassische LLM-Literatur hinaus erweitert. Recherchen in formaler Systemverifikation 5 und Konzepten der Relational Blockworld (Moral Continuity 23) lieferten das Konzept der "Coherence-Invarianten". Es wurde erkannt, dass Narrative nicht nur "widerspruchsfrei" sein müssen, sondern "invariant" gegenüber der Entropie der Generierungsprozesse. Dies führte zur Ausformulierung der fünf harten INV-Regeln, die den Kern der Ausfallsicherheit (Chaos-Resilienz) dieser Spezifikation bilden. Die Konfidenz in die Robustheit der Architektur erreichte hier ein sehr hohes Niveau.

**Evaluierungsblock 21 bis 25 (Pre-Mortem und Failure-Mode Antizipation):** Das System wurde einem rigorosen Pre-Mortem unterzogen. Es wurde simuliert, dass das Agenten-System in der Produktion versagt und einen strukturlosen Roman ausgibt. Die Analyse 19 ergab, dass das Fehlen eines klaren Abhängigkeitsgraphen (Ordering Errors) und "Context Rot" die Hauptausfallursachen sind. Die Architektur wurde daraufhin umgeschrieben, um den Zustand in immutable (geschützte Struktur) und ephemeral (flüchtige Notizen) zu separieren. Die Einführung des last\_stable\_hash im Execution-Memory garantiert, dass das System niemals in einen korrupten Zustand asynchroner Daten inkrementiert.

**Evaluierungsblock 26 bis 30 (Red-Team Review und Synthese):**

Die fertige Spezifikationsstruktur wurde simulierten Angriffen ausgesetzt. Ein massiver Kritikpunkt war die mangelnde Flexibilität des Clarifying-Question-Protokolls, das in seiner ersten Iteration zu einer "Alert Fatigue" beim menschlichen Operator geführt hätte. Die Reparatur bestand in der Implementierung von Severity-Leveln (Notice, Warning, Blocker) und der zwingenden Anforderung an den Agenten, Default-Empfehlungen mit Impact-Analysen zu berechnen. Das System muss sich nun seine Autonomie verdienen, indem es Lösungen vorrechnet, anstatt lediglich Fehler zu melden. Die Spezifikation erfüllt alle aufgestellten Qualitätsinvarianten (Q1-Q10) und behält durch die Hybridstruktur aus Markdown und strukturierten Datenschemata ihre Singularität als selbsttragendes Artefakt (Single-Artifact-Mandat).

#### **Referenzen**

1.  Architecture overview - Model Context Protocol, Zugriff am April 26, 2026, <https://modelcontextprotocol.io/docs/learn/architecture>
2.  Model Context Protocol (MCP): Everything You Need to Know | by Akash Singh - Medium, Zugriff am April 26, 2026, <https://medium.com/@akash22675/model-context-protocol-mcp-everything-you-need-to-know-082c7db27273>
3.  ICML Poster An Architecture Search Framework for Inference-Time Techniques, Zugriff am April 26, 2026, <https://icml.cc/virtual/2025/poster/45959>
4.  ARCHON: AN ARCHITECTURE SEARCH FRAMEWORK FOR INFERENCE-TIME TECHNIQUES - OpenReview, Zugriff am April 26, 2026, <https://openreview.net/pdf?id=5wuZyG1ACs>
5.  Guardians of the Agents - ACM Queue, Zugriff am April 26, 2026, <https://queue.acm.org/detail.cfm?id=3762990>
6.  AI Response Consistency Checker Detecting Cross-Response Contradictions in Generative Systems - Technical Disclosure Commons, Zugriff am April 26, 2026, <https://www.tdcommons.org/cgi/viewcontent.cgi?article=10670&context=dpubs_series>
7.  The Law of Invariant-Preserving Loops: Toward Robust Emergence in Self-Modifying Agents, Zugriff am April 26, 2026, <https://rxiv.org/pdf/2509.0075v1.pdf>
8.  Using Dramatica Theory to Improve Your Fiction Writing - How to Write a Book Now, Zugriff am April 26, 2026, <https://www.how-to-write-a-book-now.com/using-dramatica-theory.html>
9.  Dramatica, A New Theory of Story - Storymind, Zugriff am April 26, 2026, <https://storymind.com/free-downloads/dramatica_book.pdf>
10. Exploring the Dramatica Method - Jonathan Fesmire, Zugriff am April 26, 2026, <https://www.jonathanfesmire.com/exploring-the-dramatica-method/>
11. Understanding Dramatica's Complex Terminology Made Easier - Articles - Narrative First, Zugriff am April 26, 2026, <https://narrativefirst.com/articles/understanding-dramaticas-complex-terminology-made-easier>
12. Narrova Agents | Dramatica, Zugriff am April 26, 2026, <https://platform.dramatica.com/docs/narrova/agents>
13. Understanding the Storyform | Dramatica, Zugriff am April 26, 2026, <https://platform.dramatica.com/docs/dramatica-theory/the-storyform>
14. How Dramatica is Different from Six Other Story Paradigms | The Storymind Writer's Library, Zugriff am April 26, 2026, <https://storymind.com/blog/how-dramatica-is-different-from-six-other-story-paradigms/>
15. DRAMATICA - Storymind, Zugriff am April 26, 2026, <https://www.storymind.com/dramatica/downloads/structure_chart.pdf>
16. Dramatica Theory Book - Storymind, Zugriff am April 26, 2026, <https://www.storymind.com/dramatica/dramatica_theory_book/table.html>
17. The Science Behind Dramatica - Series of Articles - Narrative First, Zugriff am April 26, 2026, <https://narrativefirst.com/articles/series/the-science-behind-dramatica>
18. LLM Agentic Failure Modes: Task Drift, Reward Hacking, Alignment Faking and More, Zugriff am April 26, 2026, <https://ceaksan.com/en/llm-agentic-failure-modes>
19. Understanding and expressing scalable concurrency - SIGPLAN, Zugriff am April 26, 2026, <https://sigplan.org/Awards/Dissertation/2014_turon.pdf>
20. Key Concepts | Dramatica, Zugriff am April 26, 2026, <https://platform.dramatica.com/docs/get-started/key-concepts>
21. Model Context Protocol for Vision Agents: Schema, Memory, and World Model Implications, Zugriff am April 26, 2026, <https://neurips.cc/virtual/2025/137152>
22. The Coherence-Relational Blockworld - Braun Science & Engineering -, Zugriff am April 26, 2026, <https://bseng.com/wp-content/uploads/2025/11/The-Coherence-Relational-Blockworld-v3.0.pdf>
23. Dramatica's Character Archetypes \~ September C. Fawkes - Editor, Writer, Instructor, Zugriff am April 26, 2026, <https://www.septembercfawkes.com/2019/12/dramaticas-character-archetypes.html>
24. organicdesign/4qx-holarchy - Organic Design Gitea, Zugriff am April 26, 2026, <https://code.organicdesign.nz/organicdesign/4qx-holarchy/commits/commit/8925c579f8f7de0507856df0da35ec3b02839f59>
25. Relational Structural Experience - Braun Science & Engineering -, Zugriff am April 26, 2026, <https://bseng.com/wp-content/uploads/2025/11/Relational-Structural-Experience-v3.1.pdf>
26. JanusFlow and Janus-Pro: A Unified Multimodal Architecture for Image Understanding and Generation | by Pan Xinghan | Medium, Zugriff am April 26, 2026, <https://medium.com/@sampan090611/janusflow-and-janus-pro-a-unified-multimodal-architecture-for-image-understanding-and-generation-5574a04621ad>
27. Architect's Guide to Agentic Design Patterns: The Next 10 Patterns for Production AI, Zugriff am April 26, 2026, <https://pub.towardsai.net/architects-guide-to-agentic-design-patterns-the-next-10-patterns-for-production-ai-9ed0b0f5a5c3>
28. Trustworthy agentic AI systems: a cross-layer review of architectures, threat models, and governance strategies for real-world deployment. - F1000Research, Zugriff am April 26, 2026, <https://f1000research.com/articles/14-905>
29. Agentic AI Architecture: A Practical, Production-Ready Guide | by Monoj Kanti Saha | AgenticAI— The Autonomous Intelligence | Medium, Zugriff am April 26, 2026, <https://medium.com/agenticai-the-autonomous-intelligence/agentic-ai-architecture-a-practical-production-ready-guide-2b2aa6d16118>
30. JSON Schema - GitHub, Zugriff am April 26, 2026, <https://github.com/json-schema-org>
31. A language agnostic test suite for the JSON Schema specifications - GitHub, Zugriff am April 26, 2026, <https://github.com/json-schema-org/JSON-Schema-Test-Suite>
32. LegalWiz: A Multi-Agent Generation Framework for Contradiction Detection in Legal Documents - arXiv, Zugriff am April 26, 2026, <https://arxiv.org/html/2510.03418v2>
33. Multi-Modal Sarcasm Detection with Interactive In-Modal and Cross-Modal Graphs | Request PDF - ResearchGate, Zugriff am April 26, 2026, <https://www.researchgate.net/publication/355373803_Multi-Modal_Sarcasm_Detection_with_Interactive_In-Modal_and_Cross-Modal_Graphs>
34. Ethics of Drone Strikes - Restraining Remote-Control Killing - Edinburgh University Press, Zugriff am April 26, 2026, <https://edinburghuniversitypress.com/pub/media/ebooks/9781474483599.pdf>
35. Agentic Design Patterns: A Quick Reference Guide | by Shreya Maheshwar | Medium, Zugriff am April 26, 2026, <https://medium.com/@random.droid/agentic-design-pattern-quick-reference-d4d434972069>
36. Dramatica: A New Theory of Story | PDF | Luke Skywalker | Narration - Scribd, Zugriff am April 26, 2026, <https://www.scribd.com/document/53301433/Dramatica-A-New-Theory-of-Story>
37. Zugriff am Januar 1, 1970, <https://dramatica.com/theory/book/communication-theory>
38. Spec Kit Documentation - GitHub Pages, Zugriff am April 26, 2026, <https://github.github.com/spec-kit/>
39. 80+ Free User Story Examples with Acceptance Criteria by Type - Smartsheet, Zugriff am April 26, 2026, <https://www.smartsheet.com/content/user-story-with-acceptance-criteria-examples>
40. Dramatica: The Journey Towards a Better Understanding of Story - Articles - Narrative First, Zugriff am April 26, 2026, <https://narrativefirst.com/articles/dramatica-the-journey-towards-a-better-understanding-of-story>
41. Taxonomy of Failure Mode in Agentic AI Systems - Microsoft, Zugriff am April 26, 2026, <https://cdn-dynmedia-1.microsoft.com/is/content/microsoftcorp/microsoft/final/en-us/microsoft-brand/documents/Taxonomy-of-Failure-Mode-in-Agentic-AI-Systems-Whitepaper.pdf>
42. How Do LLMs Fail In Agentic Scenarios? A Qualitative Analysis of Success and Failure Scenarios of Various LLMs in Agentic Simulations - arXiv, Zugriff am April 26, 2026, <https://arxiv.org/html/2512.07497v1>
43. One year of agentic AI: Six lessons from the people doing the work - McKinsey, Zugriff am April 26, 2026, <https://www.mckinsey.com/capabilities/quantumblack/our-insights/one-year-of-agentic-ai-six-lessons-from-the-people-doing-the-work>
44. The Complete Guide to Building Skills for Claude | Anthropic, Zugriff am April 26, 2026, <https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf>
45. 10 Must-Have Skills for Claude (and Any Coding Agent) in 2026 | by unicodeveloper | Mar, 2026, Zugriff am April 26, 2026, <https://medium.com/@unicodeveloper/10-must-have-skills-for-claude-and-any-coding-agent-in-2026-b5451b013051>
46. github/spec-kit: Toolkit to help you get started with Spec ... - GitHub, Zugriff am April 26, 2026, <https://github.com/github/spec-kit>
47. Spec-driven development with AI: Get started with a new open source toolkit - The GitHub Blog, Zugriff am April 26, 2026, <https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/>
