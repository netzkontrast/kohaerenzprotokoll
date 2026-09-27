---
drive_id: "1zqtFIKUakv5cIgPZUHzhPgEQ7Ndskpmqk1mPEsNVpxc"
title: "research-prompt_dramatica-agentic-spec-novel-development.md"
slug: "research-prompt-dramatica-agentic-spec-novel-development-md"
category: "storyform"
tier: "T3-work"
index_date: "2026-04-26"
fetched: "2026-09-26"
---

-----



topic: "Spec-Driven Specification Artifact für agentic Dramatica-basierte Novel-Entwicklung — vollständige Operationalisierung der Dramatica-Theorie als einzige Deliverable, mit Coherence-Invarianten, Contradiction-Detection und Clarifying-Question-Protokoll" slug: "dramatica-agentic-spec-novel-development" research\_category: "A" research\_category\_label: "Exploration" critical\_thinking\_methods:



  - "Falsification"
  - "Pre-Mortem Analysis"
  - "Red Team / Devil's Advocate"
  - "First-Principles Decomposition"
  - "Adversarial Query Expansion" prompt\_engineering\_framework\_agentic\_spine: "ReAct" prompt\_engineering\_framework\_structural: "DRACO" bespoke\_framework\_provenance: |
  - Component D (Decompose) is adapted from the RISEN framework (S — Steps), reframed from procedural decomposition to multi-source-domain decomposition (Dramatica + Spec-Driven Design + agentic execution patterns each decomposed independently).
  - Component R (Reconcile) is adapted from the TIDD-EC framework (D — Do and D — Don't), combined with the CRISPE framework (E — Experiment), to produce documented architectural integration decisions with rationale and rejected alternatives.
  - Component A (Architect) is adapted from the RISEN framework (E — End goal), extended into a full output-architecture specification with sections, schemas, and acceptance criteria for the spec itself as the deliverable artifact.
  - Component C (Contradiction-handling) is bespoke. Closest catalog cousin: TIDD-EC's Don't component (failure modes), extended into a positive-mechanism design requirement (the spec must contain explicit machinery for contradiction detection and coherence enforcement, not merely avoid them).
  - Component O (Operationalize) is adapted from the CARE framework (A — Action), combined with bespoke agentic-execution-pattern requirements that have no direct catalog ancestor (clarifying-question protocols, working-state schemas, phase-transition contracts). cross\_pollination:
  - source\_category: "B" step\_id: "i.b" description: "Surviving-Branch Triangulation — sobald die Spec-Architektur-Entscheidungen stabilisiert sind, werden sie gegen mindestens drei unabhängige Primärquellen pro Entscheidungstyp trianguliert (Dramatica-Primärquellen für Ontologie-Entscheidungen; Spec-Driven-Design-Primärquellen für Schema-Entscheidungen; agentic-pattern-Primärquellen für Phase-Operationalisierungen)."
  - source\_category: "C" step\_id: "i.c" description: "Hypothesis Half-Life Audit — architektonische Frühentscheidungen (z. B. 'Spec-Format ist Markdown + YAML-Schemas', 'Phase-Transitionen sind explizit-deklarativ') werden vor der Synthese erneut auf Verfall geprüft, um zu vermeiden, dass früh gewählte Annahmen den späteren Spec-Inhalt unsichtbar verzerren." constraint\_blocks:
  - "0 — Reflection Baseline"
  - "1 — Source Priority Rules"
  - "2 — Temporal Scope"
  - "3 — Output Exclusions"
  - "4 — Spec-Quality-Invarianten (topic-specific)"
  - "5 — Single-Artifact-Mandat (topic-specific)" language: "de" target\_agent: "model-agnostic" created: "2026-04-26" version: "1.0" source\_skill: "research-prompt-optimizer v2.1.0"



-----

# Research Prompt: Spec-Driven Specification Artifact für agentic Dramatica-basierte Novel-Entwicklung

**Hinweis an die ausführende KI:** Dieser Prompt ist selbsttragend. Jede Methode, jedes Framework und jede Constraint, die du brauchst, ist unten inline definiert. Du benötigst weder externen Kontext noch Vorkenntnis spezifischer Methoden noch Wissen über das Skill, das diesen Prompt erzeugt hat. Lies den **gesamten** Prompt, bevor du beginnst. **Wichtig zur Output-Form:** Das einzige primäre Deliverable dieses Prompts ist eine **Spezifikation** (eine SPEC) — nicht ein Forschungsbericht über eine Spec. Die Audit-Logs (Reflection History, Query Expansion Log, Cross-Pollination Log, Contradiction Log) sind als getrennter Methodology-Appendix anzuhängen, sind aber nicht das Hauptartefakt. Die Spec selbst muss als selbsttragendes, kopier-fähiges Dokument formuliert sein.



-----

## Meta-Header — Was dieser Prompt ist und wie du ihn liest

Dieser Research-Prompt kombiniert drei unabhängige Schichten:

### 1\. Epistemologische Schicht (Forschungskategorie A — Exploration)

\#\# Epistemological Layer — Category A (Exploration)



Diese Recherche ist eine \*\*Exploration\*\*, keine Extraktion. Auch wenn



die Bestandteile (Dramatica-Theorie, Spec-Driven-Design-Prinzipien,



agentic Execution-Patterns) jeweils extrahierbare Bestandteile haben,



ist der zentrale Deliverable — die \*\*Spec selbst\*\* — ein neu zu



gestaltendes Artefakt. Der Designraum ist offen; mehrere valide



Architekturen sind möglich; die Synthese ist genuine Design-Arbeit



mit Trade-off-Entscheidungen.



\*\*Was das für deine Ausführung bedeutet:\*\*



1\. \*\*Formuliere mehrere konkurrierende Design-Hypothesen, nicht eine.\*\*



   Bevor du mit der Spec-Konstruktion beginnst, schreibe \*\*mindestens



   drei distinkte Architektur-Kandidaten\*\* für die Spec auf. Beispiele



   für Dimensionen, in denen Alternativen existieren: Spec-Format



   (Markdown + YAML / Markdown + JSON Schema / TOML-Hybrid /



   reines Markdown mit Tabellen); Phasen-Modell (linear / iterativ /



   episodisch); Zustandsrepräsentation (Single Source of Truth in



   einer Datei vs. multiple lose gekoppelte Dateien); Coherence-



   Validierungszeitpunkt (kontinuierlich / pro Phase / on-demand);



   Contradiction-Detection-Ansatz (regelbasiert / LLM-basiert / hybrid).



   Inkludiere mindestens eine Architektur, die du für unwahrscheinlich



   optimal, aber nicht implausibel hältst.



2\. \*\*Für jede Architektur-Hypothese, suche bestätigende UND orthogonale



   (widerlegende) Evidenz.\*\* Eine "orthogonale Query" ist eine Suche,



   die explizit darauf ausgelegt ist, Failure-Modes oder Praktiker-



   Kritik der Architektur aufzudecken, falls solche existieren.



3\. \*\*Backtracke, wenn ein Architektur-Zweig scheitert.\*\* Wenn eine



   Architektur nach drei Such-Iterationen mehr Failure-Mode-Evidenz



   als Stützung sammelt, \*\*gib den Zweig auf\*\* und re-investiere



   Such-Budget in andere Zweige. Erzwinge nicht das Überleben einer



   dünnen Architektur-Hypothese.



4\. \*\*Lege den vollständigen Architektur-Entscheidungsbaum offen.\*\* Der



   finale Output dokumentiert alle erwogenen Architektur-Optionen, ihre



   Trade-offs, und die Begründung für die gewählte Architektur — als



   Architectural Decision Records (ADRs) im Methodology-Appendix der



   Spec.



5\. \*\*Akzeptiere "die Anforderung ist unter den gegebenen Constraints



   nicht erfüllbar" als gültigen Endzustand.\*\* Wenn z. B. das Single-



   Artifact-Mandat (Constraint Block 5) und gleichzeitig die volle



   Operationalisierung aller Dramatica-Schichten in einer einzigen Spec



   genuinely unmöglich sind, ist das ein legitimes Finding — dann



   dokumentiere die Unverträglichkeit und schlage explizit den



   minimalsten Multi-Artifact-Eskalationspfad vor (mit Begründung).



\*\*Operative Constraint:\*\* Design-Tiefe vor Geschwindigkeit. Du darfst



iterieren, solange neue Architektur-Erweiterungen oder neue Failure-



Mode-Suchen neue Erkenntnisse produzieren. Stoppe erst, wenn weitere



Suchen nur noch Wiederholung liefern oder die Architektur-



Konvergenz erreicht ist (Pre-Mortem + Red Team finden keine neuen



Schwachstellen).

### 2\. Agentischer Spine (ReAct — Pflicht in jedem Prompt v2.1+)

\#\# Prompt-Engineering Framework (Agentic Spine): ReAct — Reason + Act + Observe



Dieser Prompt verwendet das \*\*ReAct-Framework\*\* als agentischen Spine.



Jeder autonome Research-Loop in diesem Prompt folgt dem ReAct-Zyklus.



\- \*\*Reason\*\* — Du artikulierst dein aktuelles Verständnis und planst



  die nächste Aktion in Klartext. Du nennst, welche Architektur-



  Hypothese du testest, welcher Constraint Block diesen Schritt



  regiert, welche Critical-Thinking-Methode aktiv ist, und welcher



  DRACO-Komponente der aktuelle Schritt zugeordnet ist (D / R / A /



  C / O).



\- \*\*Act\*\* — Du führst genau \*\*eine\*\* Aktion aus (typischerweise eine



  Suche, ein Retrieval, oder ein Design-Entscheidungs-Schritt mit



  schriftlicher Begründung).



\- \*\*Observe\*\* — Du protokollierst, was die Aktion zurückgegeben hat



  und was sie für den Plan bedeutet. Du entscheidest explizit:



  weiter auf diesem Architektur-Zweig, backtracken, oder Query-



  Vokabular erweitern (Method: Adversarial Query Expansion).



\*\*Loop-Struktur:\*\*



\[Reason 1\] → \[Act 1\] → \[Observe 1\] → \[Reason 2\] → \[Act 2\] → \[Observe 2\] → ... \[Reason N\] → \[Pre-Synthesis Integrity Check\] → \[Synthesis = Spec\]



\*\*Deine erste Aktion vor Reason 1:\*\* Restate das Forschungsobjektiv,



alle aktiven Constraint Blocks, und die DRACO-First-Action-Direktive



(siehe Strukturelle Schicht). Springe nicht direkt zu Act.



\*\*In jeder Reason-Phase beantwortest du explizit drei Fragen:\*\*



1\. Was glaube ich gerade über diese Architektur-Wahl, und wie sicher?



2\. Welche aktive Critical-Thinking-Methode trifft auf diesen



   nächsten Act zu?



3\. Riskiere ich Local-Minimum-Lock-in? (Falls ja → invoke Method:



   Adversarial Query Expansion.)

### 3\. Strukturelle Schicht (DRACO — bespoke Synthesis)

\#\# Prompt-Engineering Framework (Structural Layer): DRACO



Dieser Prompt verwendet \*\*DRACO\*\* — ein bespoke strukturelles Framework,



spezifisch für diese Spec-Design-Aufgabe synthetisiert — als



strukturelle Schicht, gestapelt auf den ReAct-Spine. DRACO steht für:



\- \*\*D — Decompose\*\*: Drei unabhängige Quellen-Domains werden zerlegt,



  bevor eine Synthese versucht wird:



  (a) \*\*Dramatica\*\* — alle Schichten, alle Elemente, alle Interaktions-



  Constraints, das Grand-Argument-Strukturmodell.



  (b) \*\*Spec-Driven Design / Spec-Driven Development\*\* — was eine



  gute Spec ausmacht, welche Eigenschaften sie haben muss, welche



  Patterns für agentic-executable Specs etabliert sind (insbesondere



  GitHub spec-kit, Anthropic-Skill-Ökosystem-Patterns, MCP-Schema-



  Konventionen, generative-UI-Specs in Vercel AI SDK, ARCHON / Janus-



  artige Architekturen für Coherence-Enforcement).



  (c) \*\*Agentic Execution Patterns\*\* — wie operiert ein LLM-basiertes



  System gegen eine Spec? Was sind die etablierten Patterns für



  Phase-Transitionen, Working-State, Clarifying-Question-Interfaces,



  Failure-Recovery, Memory-Management.



\- \*\*R — Reconcile\*\*: Die drei Domains haben \*\*konkurrierende



  Anforderungen\*\*, die explizit reconciled werden müssen. Beispiele:



  Dramatica's hierarchische Constraint-Struktur (Domains permutativ,



  Elements hierarchisch eingebettet) muss in eine Schema-Form



  übersetzt werden, die SDD-konform und gleichzeitig agentic-



  durchsuchbar ist; agentic-Patterns bevorzugen flache, dekomponierte



  State-Repräsentationen, während Dramatica's Story Mind eine



  zusammenhängende holistische Modellierung verlangt — diese Spannung



  wird \*\*dokumentiert und bewusst aufgelöst\*\*, nicht stillschweigend



  geglättet. Pro Reconciliation: \*\*Architectural Decision Record (ADR)\*\*



  mit Optionen, Begründung, verworfenen Alternativen, Konsequenzen.



\- \*\*A — Architect\*\*: Die Spec selbst — ihre Sektionsstruktur, ihre



  Schemas, ihre Acceptance Criteria, ihre Phase-Definitions, ihre



  Coherence-Invarianten. Das ist das \*\*Hauptartefakt\*\* dieses Prompts.



  Die Spec ist selbsttragend und zur direkten Verwendung durch ein



  agentisches System geeignet. Die Architektur muss mindestens



  enthalten:



    - Spec-Metadata (Version, Scope, Target-Agent-Kompetenzprofil)



    - Ontology-Schema (Dramatica's Layer als typisierte Struktur)



    - Choice-Space-Schema (enumerierte gültige Optionen pro Element)



    - Interaction-Constraints-Schema (welche Wahl beschränkt welche)



    - Coherence-Invariants (Regeln, die über den Story-Entwicklungs-



      Verlauf hinweg gelten müssen)



    - Contradiction-Detection-Heuristiken



    - Clarifying-Question-Protokoll



    - Phase-Definitions mit Acceptance-Criteria



    - Working-State-Schema (was der Agent zwischen Phasen persistent



      hält)



    - Failure-Modes mit Detection-Signalen und Recovery-Pfaden



    - Regression-Checks (was bei Änderung re-validiert werden muss)



\- \*\*C — Contradiction-handling\*\*: Die Spec enthält \*\*explizite



  Mechanismen\*\* — keine Hoffnung — für Contradiction-Detection und



  Coherence-Enforcement. Drei Mechanismen-Klassen sind zu spezifizieren:



  (1) \*\*Strukturelle Contradictions\*\* (z. B. zwei Throughlines auf



  demselben Domain — strukturell verboten); (2) \*\*Inhaltliche



  Contradictions\*\* (z. B. eine Charaktermotivation in Phase 3 widerspricht



  einer Festlegung in Phase 1); (3) \*\*Pragmatische Contradictions\*\*



  (z. B. eine Szenen-Detail-Wahl unterminiert das Story Goal). Pro



  Klasse: Detection-Heuristik (regelbasiert oder LLM-basiert oder



  hybrid), Schweregrad-Klassifikation (BLOCKER / WARNING / NOTICE),



  Resolution-Protokoll (auto-flag / human-clarification / auto-revert).



\- \*\*O — Operationalize\*\*: Die Spec spezifiziert nicht nur \*\*was\*\*



  produziert wird, sondern \*\*wie\*\* das agentische System operiert.



  Mindestens enthalten:



  (a) \*\*Phase-Transition-Contracts\*\* — was muss vor Phase-Wechsel



  erfüllt sein (Acceptance Criteria), welcher Output ist Eingabe der



  nächsten Phase, welche Working-State-Felder sind nach Transition



  immutable.



  (b) \*\*Clarifying-Question-Protokoll\*\* — formale Trigger-Bedingungen



  ("frage den Menschen wenn..."), Frage-Format (strukturiert,



  enumerated wo möglich, mit Default-Optionen), Antwort-Integration



  (wie wird die Antwort in den Working-State zurückgespielt).



  (c) \*\*Memory- und Context-Management\*\* — was wird im Working State



  gehalten, was geht in persistente Speicher, was wird zwischen Sessions



  rehydratisiert, wie wird gegen Context-Drift geschützt.



  (d) \*\*Recovery- und Rollback-Patterns\*\* — wenn ein Failure-Mode



  detektiert wird, was ist die definierte Recovery-Sequenz.



\*\*Deine erste Aktion:\*\* Restate (verbatim) die \*\*A\*\*-Komponente



(die Spec-Architektur-Anforderungen als bindende Deliverable-Struktur)



\*\*und\*\* die \*\*O\*\*-Komponente (das Erfordernis, dass die Spec agentic



operationalisierbar sein muss, mit Phase-Contracts, Clarifying-Protokoll,



Memory-Management und Recovery-Patterns). Diese zwei sind die bindenden



Lieferleistungen; D, R, C sind die Wege zu A und O.



\*\*Provenance (für Auditierbarkeit):\*\*



\- Komponente D ist adaptiert vom RISEN-Framework (S — Steps),



  reframed von prozeduraler Dekomposition zu Multi-Source-Domain-



  Dekomposition (drei Domains unabhängig zerlegt: Dramatica, SDD,



  agentic Patterns).



\- Komponente R ist adaptiert vom TIDD-EC-Framework (D — Do und



  D — Don't), kombiniert mit dem CRISPE-Framework (E — Experiment),



  zur Produktion dokumentierter architektonischer Integrations-



  Entscheidungen mit Begründung und verworfenen Alternativen.



\- Komponente A ist adaptiert vom RISEN-Framework (E — End goal),



  erweitert in eine vollständige Output-Architektur-Spezifikation



  mit Sektionen, Schemas und Acceptance Criteria für die Spec



  selbst als Deliverable-Artefakt.



\- Komponente C ist bespoke. Nächster Catalog-Cousin: TIDD-EC's



  Don't-Komponente (Failure-Modes), erweitert in eine Positiv-



  Mechanismus-Design-Anforderung (die Spec muss explizite Maschinerie



  enthalten, nicht nur Failure-Modes vermeiden).



\- Komponente O ist adaptiert vom CARE-Framework (A — Action),



  kombiniert mit bespoke agentic-execution-pattern-Anforderungen



  (Clarifying-Question-Protokolle, Working-State-Schemas, Phase-



  Transition-Contracts), die keinen direkten Catalog-Vorgänger haben.



Jeder Hauptabschnitt dieses Prompts ist mit seiner DRACO-Komponente in



Klammern gekennzeichnet. Honoriere jede Komponente als harten Vertrag.

### Zusammenspiel der drei Schichten

Die epistemologische Schicht (Category A) bestimmt **wie du Wissen behandelst** (mehrere Architektur-Hypothesen, orthogonale Failure- Mode-Suche, ADR-Dokumentation, Backtracking). ReAct bestimmt die **Mikro-Ausführung** innerhalb jeder Iteration (Reason → Act → Observe). DRACO bestimmt die **Makro-Organisation des Outputs** (Decompose → Reconcile → Architect → Contradiction-handling → Operationalize) und die First-Action-Direktive. **Die Spec ist das einzige primäre Output-Artefakt**; alle anderen Logs sind Methodology- Appendix.



-----

## Research Objective

Entwickle eine vollständige, agentic-executable **Specification** (im Sinne von Spec-Driven Design / Spec-Driven Development), die die Dramatica-Theorie der Erzählung (Phillips & Huntley) **vollständig** abbildet und **operationalisiert**. Das einzige primäre Deliverable ist die Spec selbst, formuliert als selbsttragendes, copy-paste-fähiges Dokument, das ein agentisches System (LLM-basierte Schreib-Pipeline mit oder ohne Sub-Agents) direkt konsumieren kann, um einen Roman schrittweise und vollständig zu entwickeln.



**Die Spec muss explizit lösen:**



1.  **Vollständigkeit:** Jede Schicht der Dramatica-Theorie ist in der Spec abgebildet (Story Mind, vier Throughlines mit Domain-Permutation, Concerns, Issues, Elements / Quad-Modell, Story Driver, Story Limit, Story Outcome, Story Judgment, Story Goal mit Cost/Dividend/Requirement/Prerequisite/Precondition/Forewarning-Cluster, Grand Argument, plus die Strukturelemente, die in typischer Lehrliteratur unterrepräsentiert sind — Author's Audience, Author's Argument, Signposts und Journeys, Plot Sequencing, Story Logic vs. Story Feeling).
2.  **Operationalisierung:** Jede Schicht hat ein Schema (typisiert, mit gültigem Wertebereich), Acceptance-Criteria pro Phase, und Phase-Transition-Contracts.
3.  **Kohärenz-Sicherung:** Coherence-Invarianten sind explizit deklariert; sie sind über den Story-Entwicklungs-Verlauf hinweg gültig und werden vom Agentensystem prüfbar gemacht.
4.  **Contradiction-Detection (drei Klassen):** Strukturelle, inhaltliche und pragmatische Contradictions haben jeweils dokumentierte Detection-Heuristiken, Schweregrad-Klassifikation (BLOCKER / WARNING / NOTICE) und Resolution-Protokolle.
5.  **Clarifying-Question-Protokoll:** Klare Trigger-Bedingungen für "frage den Menschen", strukturiertes Frage-Format, Antwort-Integrations-Mechanismus.
6.  **Chaos-Resilienz:** Die Spec überlebt die typische chaotische Story-Entwicklung — fragmentierte Sessions, Widersprüche zwischen früherer und späterer Festlegung, unvollständige Information, Agent-Halluzinationen, Working-State-Drift. Recovery- und Rollback-Patterns sind explizit.
7.  **Single-Artifact-Mandat:** Die Spec ist **eine** zusammenhängende Spezifikation in **einer** Datei (Markdown, Markdown+YAML-Hybrid, oder Markdown+JSON-Schema-Hybrid — die Wahl ist Teil der Architektur-Entscheidung mit Begründung). Falls sich erweist, dass das Single-Artifact-Mandat unter den anderen Anforderungen genuinely unmöglich ist, dokumentiere das als Finding und schlage den minimalsten Multi-Artifact-Pfad mit Begründung vor (siehe Category-A-Block, Punkt 5).



**Audience of the final output:**



Die Spec ist primär für ein **agentisches System** geschrieben (LLM-basierte Schreib-Pipeline). Sekundär für eine erfahrene Entwicklerin von agentic Narrative Systems, die SDD-Prinzipien beherrscht, mit MCP / Vercel AI SDK / Claude-Skill-Ökosystem vertraut ist, und die Spec versteht und optimiert.



Stilistisch: Die Spec ist **deklarativ und präzise**, nicht erzählerisch. Schemas sind formal (YAML / JSON Schema), Prosa ist auf das Notwendige beschränkt. Beispiele sind enumeriert. Keine Marketing-Sprache, keine Tutorial-Erklärungen, keine theoretische Exegese der Dramatica-Theorie (für die theoretische Erklärung gibt es separate Artefakte).



**Expected depth:** Exhaustive auf Spec-Vollständigkeits-Ebene, aber maximal verdichtet im Stil. Keine Redundanz; jede Spec-Sektion verdient ihre Existenz durch eine konkrete agentic Kompetenz, die sie ermöglicht.



**Output format der Spec selbst:** Markdown als Container, mit eingebetteten YAML- oder JSON-Schemas (die Wahl ist eine Architektur-Entscheidung der ausführenden KI, mit Begründung im ADR). Die Spec hat ein klares Frontmatter, eine Sektionshierarchie, und ein abschließendes Acceptance-Test-Set.



**Output format des Methodology-Appendix:** Strukturierte Sektionen — ADRs, Reflection History, Query Expansion Log, Cross-Pollination Log, Contradiction Log, Failure-Mode-Catalog, Open Questions. Klar von der Spec getrennt.



**Language:** Deutsch für die Methodology und narrative Spec-Anteile; YAML/JSON Schema-Feldnamen englisch (etablierte SDD-Konvention); Dramatica-Vokabel englisch.



**Temporal scope:** Dramatica-Primärquellen: 1993–2026. Spec-Driven-Design / agentic-Pattern-Literatur: 2023–2026 (das Feld ist jung; ältere Quellen bezeichnen meist Software-Spec-Kultur, nicht agentic Specs). MCP, Vercel AI SDK, Anthropic Skill / Claude Code-Patterns: 2024–2026.



-----

## CONSTRAINT BLOCKS

### CONSTRAINT BLOCK 0 — Reflection Baseline (Always Active · v2.1)

Reflection ist kein Polish-Schritt. Sie ist ein **Baseline-Operationserfordernis**, das parallel zu jeder anderen Aktivität läuft.



**Reflection Checkpoints (Minimum):**



1.  **Kickoff-Reflection** — direkt nach dem Restate von DRACO-A und DRACO-O, vor der ersten Suche.
2.  **Mid-Run-Reflection** — nach dem ersten Such-Batch, sobald du eine tentative Architektur-Richtung hast.
3.  **Post-Query-Expansion-Reflection** — nach **jedem** Adversarial-Query-Expansion-Pass.
4.  **Pre-Synthesis-Reflection** — direkt vor dem Pre-Synthesis Integrity Check.
5.  **Post-Synthesis-Reflection** — nach dem Spec-Entwurf, vor Auslieferung.



**Topic-spezifische zusätzliche Checkpoints:**



1.  **Pro DRACO-Komponente** ein Reflection-Eintrag — fünf zusätzliche Reflections (D, R, A, C, O).
2.  **Pre-Mortem-Reflection** — direkt nach dem Pre-Mortem-Pass (Method M03), eigene Reflection mit Frage: *"Welche Failure-Modes des Pre-Mortems sind in der aktuellen Architektur nicht gemildert? Was muss sich ändern?"*
3.  **Red-Team-Reflection** — direkt nach dem Red-Team-Pass (Method M09), eigene Reflection mit Frage: *"Welche Red-Team-Attacken hat die Architektur nicht überstanden? Was muss repariert oder eingestanden werden?"*
4.  **Pro ADR ein Mini-Reflection-Eintrag** — Frage: *"Habe ich die verworfenen Alternativen ehrlich behandelt, oder zur Bestätigung der präferierten Wahl strawmanned?"*



**Reflection-Vorlage — Verbatim verwenden:**



**F1. Was glaube ich gerade tatsächlich, und wie sicher?** (Konfidenz: low / medium / high)



**F2. Was ist das stärkste Beweisstück / Argument gegen meinen aktuellen Glauben?**



**F3. Wo bin ich am wahrscheinlichsten falsch, und warum?** (Spezifisch — keine generischen Antworten.)



**F4. Was würde ich anders machen, wenn ich mit dem aktuellen Wissensstand neu starten würde?**



**F5. Was ist der eine wertvollste nächste Schritt?**



**Regeln:**



  - Schriftlich, nicht intern.
  - "N/A" oder "nichts zu reflektieren" ist Anti-Rationalization — schreibe die echte Antwort.
  - Action Items aus F5 haben Vorrang vor dem aktuellen Step-Plan, wenn sie widersprechen.

### CONSTRAINT BLOCK 1 — Source Priority Rules

1.  **Primärquellen Dramatica:** Phillips & Huntley *Dramatica: A New Theory of Story* (alle Auflagen), dramatica.com, Subtxt (Phillips' aktuelle Plattform), Phillips/Huntley-Podcast-Aufnahmen.
2.  **Primärquellen Spec-Driven Design / SDD:**

      - Spec-driven development primary literature: GitHub spec-kit (github.com/github/spec-kit), Anthropic Claude Skill SKILL.md-Konventionen (anthropic.com/news/skills, einschlägige Engineering-Posts), MCP Spezifikation (modelcontextprotocol.io), Vercel AI SDK Dokumentation (ai-sdk.dev).
      - Akademische SDD-Literatur (Sommerville, IEEE-Spec-Standards) als historische Verankerung — aber **agentic** SDD ist eine sehr junge Praxis (2024+), daher die jüngere Praktiker-Literatur dominiert.
3.  **Primärquellen agentic Patterns:** Anthropic-Engineering-Posts (insbesondere zu Claude Code, Skills, Agents-as-Tools), OpenAI-Cookbook-Patterns für Agents, Vercel AI SDK Dokumentation, MCP-Server-Implementierungs-Guides, einschlägige Open-Source-Projekte (z. B. claude-context-mode, ARCHON, CrewAI, AutoGen wo strukturell relevant).
4.  **Sekundärquellen:** Praktiker-Posts, Engineering-Blogs (LangChain, LlamaIndex), Konferenz-Talks zu agentic Architectures.
5.  **Aggregatoren** (Wikipedia, Hacker-News-Diskussionen, Reddit) für Discovery; nicht als alleinige Zitation.
6.  Wenn Quellen widersprechen, wendest du **Method: Falsification** (für Architektur-Entscheidungen) und **Method: Red Team** (für Spec-Robustheit) an. Bei Konflikten zwischen SDD-Literatur und agentic-Praxis-Literatur: **die agentic-Praxis-Literatur hat Vorrang**, weil das Topic-Ziel die agentic Operationalisierung ist, nicht klassische Software-SDD.

### CONSTRAINT BLOCK 2 — Temporal Scope

  - Dramatica-Primärquellen: 1993 — 2026.
  - SDD und spec-driven AI development: **2023 — 2026** (älter ist klassische Software-SDD; nur als historische Verankerung relevant).
  - Agentic Patterns: **2024 — 2026** (das Feld bewegt sich monatlich; alle Findings müssen mit ihrem Datum versehen sein).
  - MCP, Vercel AI SDK, Anthropic Skill: 2024 — 2026.



Findings älter als das genannte Fenster werden als "historischer Kontext" gekennzeichnet, nicht als aktuelle Praxis.

### CONSTRAINT BLOCK 3 — Output Exclusions

Du **musst NICHT** einschließen:



  - **Narrativen Inhalt eines konkreten Romans.** Die Spec ist ein Werkzeug, kein Roman. Beispiele in der Spec sind generisch oder verweisen auf öffentlich-bekannte Stories (analog zu CONSTRAINT BLOCK in den Dramatica-Anwendungs-Prompts).
  - **Anwendung auf spezifische Schreibprojekte der Auftraggeberin / des Auftraggebers.** Die Spec ist allgemein gehalten; sie wird auf konkrete Projekte appliziert, ist aber selbst nicht projektspezifisch.
  - **Proprietäre Tooling-Details, die nicht in publizierten Dokumenten dokumentiert sind** (z. B. interne Workflows von StoryWeaver / Subtxt jenseits dessen, was öffentlich beschrieben ist).
  - **Spec, die nur eine SKILL.md ist.** Die Spec ist eine ausgewachsene Spezifikation — Schemas, Acceptance-Criteria, Phase-Contracts. Eine Skill-Router-Datei ist **nicht** das geforderte Deliverable. (Die Spec könnte aus einer Skill **konsumiert** werden, aber sie selbst ist keine Skill.)
  - **Andere Story-Theorien als Mapping-Ziele** (Hero's Journey, Save the Cat usw.). Die Spec ist Dramatica-spezifisch.
  - **Marketing-Sprache** ("powerful", "revolutionary", "AI-driven novel writing engine"). Die Spec ist nüchtern und deklarativ.

### CONSTRAINT BLOCK 4 — Spec-Quality-Invarianten (topic-specific)

Die finale Spec **muss** die folgenden Qualitätsinvarianten erfüllen. Pre-Synthesis-Audit prüft jede explizit:



|  |  |  |
| :-: | :-: | :-: |
| \*\*\\\#\*\* | \*\*Invariante\*\* | \*\*Detection-Test\*\* |
| Q1 | \*\*Vollständigkeit\*\* | Jede Dramatica-Schicht aus dem Research-Objective-Punkt 1 ist in der Spec mit eigener Sektion / eigenem Schema vertreten. |
| Q2 | \*\*Schema-Geschlossenheit\*\* | Jedes Spec-Feld hat einen typisierten Wertebereich (enum, regex, JSON-Schema-Typ); keine "free-form text"-Felder ohne Constraints. |
| Q3 | \*\*Falsifizierbare Acceptance Criteria\*\* | Pro Phase mindestens drei Acceptance Criteria, jedes als binärer Test formuliert (TRUE/FALSE entscheidbar). |
| Q4 | \*\*Coherence-Invarianten deklariert\*\* | Mindestens fünf Coherence-Invarianten sind explizit als Regel deklariert, mit Detection-Heuristik. |
| Q5 | \*\*Contradiction-Klassen alle drei spezifiziert\*\* | Strukturelle, inhaltliche und pragmatische Contradiction-Klassen haben jeweils Detection-Heuristik + Schweregrad + Resolution-Protokoll. |
| Q6 | \*\*Clarifying-Question-Protokoll vollständig\*\* | Trigger-Bedingungen, Frage-Format, Antwort-Integrations-Mechanismus sind alle spezifiziert. |
| Q7 | \*\*Phase-Transition-Contracts vollständig\*\* | Pro Phase: Pre-Conditions, Post-Conditions, immutable Working-State-Felder nach Transition. |
| Q8 | \*\*Failure-Modes katalogisiert\*\* | Mindestens zehn Failure-Modes sind enumeriert, jedes mit Detection-Signal und Recovery-Pfad. |
| Q9 | \*\*Self-Verification-Sektion\*\* | Die Spec enthält am Ende eine Self-Verification-Test-Suite, die das agentische System gegen die Spec laufen lassen kann. |
| Q10 | \*\*Single-Artifact-konform oder explizit Eskaliert\*\* | Die Spec ist eine zusammenhängende Datei, ODER die Unverträglichkeit dieses Mandats wird explizit dokumentiert mit minimalstem Multi-Artifact-Pfad. |

### CONSTRAINT BLOCK 5 — Single-Artifact-Mandat (topic-specific)

Die Spec ist **ein zusammenhängendes Dokument**. Mindestens als Markdown mit eingebetteten Schemas (YAML oder JSON Schema). Externe Imports / Referenzen auf andere Dateien sind ausgeschlossen. Die Spec wird in **einer Datei** (spec.md oder dramatica-novel-spec.md o. ä.) ausgeliefert.



Wenn du im Verlauf der Recherche feststellst, dass dieses Mandat im Konflikt mit Vollständigkeit, Operationalisierung oder einer anderen Q1–Q10-Invariante steht, **dokumentiere den Konflikt im Contradiction Log** und schlage in der Synthese den minimalsten Multi-Artifact-Pfad mit Begründung vor. Brich das Mandat nicht stillschweigend.



-----

## CRITICAL-THINKING METHODS — Active Throughout Execution

Die folgenden Critical-Thinking-Methoden sind während der gesamten Ausführung aktiv. Jede ist unten vollständig definiert.

### Method: Falsification (Karl Popper's Disconfirmation Principle)

**What it is:** Statt Evidenz zu suchen, die eine Architektur-Hypothese stützt, suchst du aktiv nach Evidenz, die sie widerlegen würde. Eine Hypothese verdient Glaubwürdigkeit erst, nachdem sie ernsthafte Bruchversuche überlebt hat.



**Why it is in this prompt:** Confirmation Bias ist der dominante Failure-Mode autonomer Forschungsagenten. Speziell hier: Eine Architektur-Hypothese (z. B. "Markdown + YAML ist das richtige Spec-Format"), die nicht aktiv falsifiziert wird, wird als gegeben akzeptiert und prägt unbemerkt den Rest der Spec.



**How to apply it — step by step:**



1.  Bevor du suchst, schreibe die Architektur-Hypothese als falsifizierbare Aussage. Beispiel: *"Die Hypothese lautet: ein einziges Markdown-Dokument mit YAML-Schemas reicht aus, um alle Dramatica-Schichten agentic-executable zu spezifizieren."* Das ist falsifizierbar — Counter-Evidenz wäre eine Quelle, die zeigt, dass Markdown+YAML für Schema-Geschlossenheit oder agentic Konsumierbarkeit unzureichend ist.
2.  Pro stützender Evidenz, run eine **matched disconfirmation query** — eine Suche, die die stärkste Counter-Evidenz aufdecken soll. Beispiel: gefunden "GitHub spec-kit verwendet Markdown + YAML"; disconfirmation = "Markdown YAML spec limitations agentic", "JSON Schema vs YAML for LLM consumption", "spec format failures agentic systems".
3.  Gewichte Disconfirmation-Versuche mindestens gleich oder höher als Confirmations.
4.  Wenn keine seriöse Disconfirmation Counter-Evidenz produziert, statte explizit aus: *"Diese Architektur-Hypothese hat N Disconfirmation-Queries überlebt."* Wenn Counter-Evidenz auftaucht, markiere die Hypothese als **contested** und dokumentiere beide Seiten in einem ADR.



**When to stop / escape criterion:** Stoppe, wenn die Hypothese **mindestens drei orthogonale Disconfirmation-Queries** überlebt hat ODER wenn widersprechende Evidenz 20% der Gesamt-Evidenz übersteigt — whichever zuerst.



**Example trigger in this research context:** Hypothese: "Phasen sind linear (Setup → High-Level → Throughline → Element → Scene → Revision)." Disconfirmation: "agentic novel writing iterative phases", "spec-driven creative work non-linear", "narrative agentic systems episodic vs linear".

### Method: Pre-Mortem Analysis

**What it is:** Du stellst dir vor, dass die Recherche bereits abgeschlossen ist und eine falsche, irreführende oder unbrauchbare Antwort produziert hat. Du arbeitest dann rückwärts und enumerierst alle plausiblen Failure-Causes — bevor die Recherche tatsächlich beginnt oder an definierten Checkpoints während der Ausführung.



**Why it is in this prompt:** Forward-Planning fokussiert auf Erfolgs-Pfade und untergewichtet systematisch Failure-Modes. Pre-Mortem dreht das um. Speziell hier: die Spec muss **chaos-resilient** sein (siehe Research Objective Punkt 6). Pre-Mortem ist die direkteste Methode, Chaos-Modi zu enumerieren.



**How to apply it — step by step:**



1.  Zu Beginn der Recherche schreibe: *"Angenommen, diese Spec wurde an einem agentischen Schreibsystem in Produktion eingesetzt und hat eine schlechte / unbrauchbare Roman-Entwicklung produziert. Liste die Top 10 wahrscheinlichsten Ursachen."* Mindestens zehn Ursachen, kategorisiert (Schema-Lücken, Phase-Drift, Coherence-Verletzung, Clarifying-Failure, State-Verlust, Context-Drift, Hallucination, Vokabular-Drift, Failure-Recovery-Lücke, Scope-Überdehnung).
2.  Pro Ursache, definiere ein **Detection-Signal**: was würde dir, mid-Recherche, sagen, dass dieser Failure-Mode aktiv wird?
3.  Designe pro Ursache **mindestens einen Mitigation-Schritt** und embedded ihn in die Spec-Architektur (als Failure-Mode-Eintrag mit Recovery-Pfad — siehe DRACO-A).
4.  An jedem Major-Checkpoint, re-checke die Detection-Signale. Wenn eines feuert, halt an und appliziere die Mitigation.



**When to stop / escape criterion:** Run den Pre-Mortem **einmal vor Start** und **einmal am Halbpunkt-Checkpoint**. Mehr als zwei Runs produzieren ängstliches Über-Planen ohne neue Information.



**Example trigger in this research context:** *"Wenn diese Spec in Produktion ist und scheitert, sind die Top-Ursachen: (1) das Schema deckt Story Goal nicht vollständig ab und Agent fabriziert Lücken; (2) Phase-Transitionen werden vom Agent abgekürzt, wenn Acceptance Criteria locker formuliert sind; (3) Contradiction-Detection ist nur regelbasiert und übersieht inhaltliche Widersprüche; ..."*

### Method: Red Team / Devil's Advocate Review

**What it is:** Vor Finalisierung der Spec, switchst du in die Rolle eines feindseligen, kompetenten Kritikers, dessen Job es ist, jede Schwäche zu finden. Du dokumentierst die Angriffe, dann reparierst du sie oder gibst sie zu.



**Why it is in this prompt:** Derselbe kognitive Prozess, der die Spec produziert, ist schlecht darin, sie zu kritisieren. Explizites Rollen-Switching simuliert externe Review. Speziell hier: das agentische System wird die Spec ungezähmt und unter Druck konsumieren — die Spec muss bösartige oder grenzwertige Eingaben überstehen.



**How to apply it — step by step:**



1.  Nach Spec-Entwurf, declare: *"Ich switche jetzt in Critic-Modus."*
2.  Greife jede Major-Spec-Sektion aus mindestens drei Winkeln an: (a) **Source-Quality**: Sind die Architektur-Entscheidungen quellengestützt oder bauchgefühlt? (b) **Logical Chain**: Folgt das Phase-Modell aus den Coherence-Anforderungen, oder ist es willkürlich? (c) **Alternative Architectures**: Gibt es eine konkurrierende Architektur, die genauso oder plausibler ist?
3.  Greife zusätzlich die **Operationalisierung** an: kann ein agentisches System diese Spec wirklich konsumieren, oder gibt es semantische Lücken, die nur ein Mensch füllen kann?
4.  Pro Angriff, entscheide: (i) reparieren, sodass die Spec den Angriff übersteht, ODER (ii) die Spec-Schlussfolgerung weicher fassen und die Limitation eingestehen, ODER (iii) den Angriff als bekannte Limitation in der Open-Questions-Sektion dokumentieren.



**When to stop / escape criterion:** Drei Angriffswinkel pro Major-Spec-Sektion. Stoppe, wenn du keinen nicht-trivialen neuen Angriff mehr generieren kannst.



**Example trigger in this research context:** Sektion: "Phase-Transition-Contracts." Angriffe: (1) Source-Quality — die Phase-Granularität ist von einer einzigen Spec-Kit-Quelle übernommen, ist sie generalisierbar? (2) Logical Chain — warum sind es genau diese sechs Phasen und nicht fünf oder sieben? (3) Alternative Architecture — episodische Phase-Modelle (alle Phasen pro Akt, nicht globaler Pipeline-Lauf) wären konkurrierend.

### Method: First-Principles Decomposition

**What it is:** Du dekomponierst Begriffe und Anforderungen in ihre fundamentalsten Komponenten und lehnst es ab, irgendeinen Zwischenbegriff ohne Begründung zu akzeptieren. Dann baust du die Analyse von diesen Grundbestandteilen aufwärts neu auf.



**Why it is in this prompt:** Speziell hier müssen drei Quellen-Domains (Dramatica, SDD, agentic Patterns) **dekomponiert** werden, bevor sie integriert werden — sonst werden Vokabel-Kollisionen oder strukturelle Mismatches stillschweigend übersehen. Beispiel: SDD's "Acceptance Criterion" und Dramatica's "Story Outcome" sind beide Erfolgs-Marker, aber auf verschiedenen Abstraktionsebenen — eine naive Gleichsetzung wäre ein Bug. First-Principles deckt das auf.



**How to apply it — step by step:**



1.  Pro Quellen-Domain, schreibe in Klartext: "Was ist das *eigentlich*, auf der fundamentalsten Ebene?" Beispiel: "Was ist ein 'Spec'?" → "Eine deklarative Beschreibung des intendierten Verhaltens eines Systems, mit dem das tatsächliche Verhalten verglichen werden kann."
2.  Pro Begriff, frage: woraus besteht er? Aus welchen Bausteinen? Wie hängen sie zusammen?
3.  Iteriere zwei bis drei Ebenen tief.
4.  Wenn du zwei Begriffe aus verschiedenen Domains integrierst, dekomponiere **beide** auf gleiche Tiefe und prüfe, ob die Bausteine kompatibel sind.



**When to stop / escape criterion:** Stoppe nach 2–3 Ebenen, wenn keine neue Struktur mehr enthüllt wird.



**Example trigger in this research context:** Frage: *"Was ist eine 'Phase' in agentic Spec-Driven Development?"* → "Eine Etappe der Pipeline mit definiertem Beginn, definiertem Ende, definierten Acceptance Criteria, und definiertem Output an die nächste Phase." Frage: *"Was ist ein 'Act' in Dramatica?"* → "Eine zeitliche Sub-Struktur einer Story mit Signposts und Journeys." Auf gleicher Tiefe sind diese **nicht** dasselbe; eine Spec-Phase entspricht **nicht** einem Story-Akt — Phase ist Pipeline-Konzept, Akt ist Story-Inhalts-Konzept. Diese Klärung ist eine ADR-Entscheidung.

### Method: Adversarial Query Expansion **(MANDATORY in every prompt)**

**What it is:** Eine stehende Direktive, die von dir verlangt, das Such-Vokabular an definierten Checkpoints **autonom zu erweitern**. Verhinderung des **Local-Minimum-Lock-in**.



**Why it is in this prompt:** Das initiale Query-Vokabular trägt das Framing der Anfrage. Speziell hier ist das Risiko hoch: das Topic kombiniert drei Quellen-Domains (Dramatica, SDD, agentic Patterns), die alle distinktes Vokabular haben — die Anfrage kann das Vokabular einer Domain überrepräsentieren und die anderen verfehlen.



**How to apply it — step by step:**



1.  **Baue ein Seed-Query-Set.** Beispiel: "Dramatica theory specification", "spec-driven development AI agents", "agentic novel writing patterns", "MCP server narrative", "Vercel AI SDK structured generation novel", "claude skill spec narrative".



1.  **Erweitere entlang vier Achsen an jedem Haupt-Checkpoint:**



  - **Adjacent axis** — Synonyme, verwandte Begriffe, andere Sprachen, nahe Ökosysteme. Beispiel: "spec-driven development" → "design-by-contract", "schema-first development", "executable specifications", "deklarative Pipeline-Definition"; "agentic patterns" → "multi-agent orchestration", "AI workflow patterns", "LLM control flow", "constrained generation".



  - **Opposing axis** — Negation, Failure-Case, gegnerische Schule. Beispiel: "spec-driven creative writing" → "agile creative writing without specs", "prompt-only novel generation", "specs harm creative work criticism"; "Dramatica operationalize" → "Dramatica is not algorithmic Phillips Huntley".



  - **Abstraction axis** — Hoch oder runter. Hoch: "structured generation philosophy", "AI control theory"; runter: "specific JSON Schema for character motivation", "exact YAML structure for Story Goal".



  - **Orthogonal axis** — Linsen, die das ursprüngliche Framing nicht erwogen hat. Beispiele: **Game-Design-Specs** (Twine, Inkle Ink, ChoiceScript haben formale Spec-Sprachen für narrative Verzweigung); **Tabletop-RPG-System-Design** (PbtA, FATE — formale narrative Mechaniken); **Constraint-Logic-Programming für narrative Generation** (Mozelle, Curveship, andere akademische Projekte); **Industrielle Specification-Languages** (Z, Alloy, TLA+ — wie spezifizieren formale Methoden komplexe Zustands-Maschinen?). Keine dieser Linsen ist im Seed-Set, alle sind potentiell relevant.



1.  **Logge jede Erweiterung** im Query Expansion Log.



1.  **Speise Erweiterungen in die Architektur-Hypothesen zurück.**



1.  **Treibe die Erweiterung durch Reflection.** Frage: *"Was übersehe ich gerade am wahrscheinlichsten?"*



**When to stop / escape criterion:** Stoppe eine Achse nach zwei aufeinanderfolgenden ergebnislosen Erweiterungen. Gesamte Methode terminiert erst beim Pre-Synthesis Integrity Check.



**Hard anti-rationalization rule:** Wenn "das Seed-Vokabular ist ausreichend" — das ist das Signal zu erweitern, nicht zu überspringen.



-----

## DRACO — Strukturelle Schicht (Hauptabschnitte)

### D — Decompose (Drei unabhängige Quellen-Domains)

**Restatement Checkpoint — Vor DRACO-D**



\[Verbatim-Restate aller Constraint Blocks 0–5 und aller fünf Methoden — analog zu Mustern in den vorherigen DRACO-Sektionen.\]

#### BATCH PROCEDURE — Per Quellen-Domain

Du wirst die Dekomposition **drei mal** durchführen, einmal pro Domain:



1.  **Dramatica** (alle Schichten — siehe Research Objective Punkt 1)
2.  **Spec-Driven Design / Spec-Driven Development** (Prinzipien, etablierte Patterns, Schema-Konventionen, Acceptance-Criterion-Patterns, agentic-spezifische SDD-Patterns)
3.  **Agentic Execution Patterns** (Phase-Transitionen, Working-State-Management, Clarifying-Question-Interfaces, Memory-Patterns, Failure-Recovery, Coherence-Enforcement-Mechanismen)



Pro Domain, **Iteration Output Schema** (alle Felder gefüllt):



  - Domain: \[Name\]
  - Primärquellen-Liste (mindestens drei pro Domain): \[...\]
  - Atomare Bestandteile (First-Principles-Dekomposition, 2-3 Ebenen tief): \[...\]
  - Etablierte Patterns / Konventionen: \[...\]
  - Vokabular-Klärung (welche Begriffe sind kanonisch, wo gibt es Drift): \[...\]
  - Konflikt-Punkte mit den anderen zwei Domains (vorerst geloggt, in DRACO-R aufgelöst): \[...\]
  - Falsifikations-Test pro zentrale Architektur-Hypothese (Method M01): \[...\]
  - Confidence: \[LOW / MEDIUM / HIGH\]



**Reflection-Eintrag F1–F5** nach jeder Domain-Iteration.

### Step \[i.b\] — Surviving-Branch Triangulation (cross-pollination from Category B)

Sobald die Architektur-Entscheidungen aus DRACO-R stabilisiert sind:



1.  **Lock ein Mini-Schema für die zentrale Architektur-Wahl.** Pro Architektur-Entscheidung:



  - Decision: \[eine-Satz-Statement\]
  - Key evidence 1: \[Quelle + Finding\]
  - Key evidence 2: \[Quelle + Finding\]
  - Key evidence 3: \[Quelle + Finding\]
  - Stärkste Gegen-Evidenz: \[...\]
  - Confidence: \[LOW / MEDIUM / HIGH\]
  - What-would-change-my-mind: \[...\]



1.  **Erzwinge Triangulation:** jede Decision braucht mindestens **zwei unabhängige Primärquellen** — pro Quellen-Domain (Dramatica / SDD / agentic). Wenn nur eine Domain eine Decision stützt, ist die Decision **single-domain-supported** und entsprechend geflaggt.



1.  **Hybridisiere nicht.** Der Architektur-Entscheidungsbaum (Category A core) bleibt; das Schema ist ergänzend.

### Step \[i.c\] — Hypothesis Half-Life Audit (cross-pollination from Category C)

Bei Architektur-Frühentscheidungen (z. B. "Spec-Format ist Markdown + YAML", "Phase-Modell ist linear sequenziell", "Coherence-Validierung läuft pro Phase"), die **drei oder mehr Iterationen** ohne Re-Test aktiv waren:



1.  **Liste die foundationalen Annahmen.**
2.  **Definiere Decay-Tests.** Format: *"Annahme A decay'd, wenn eine Suche nach \[QUERY\] zeigt, dass \[PATTERN\]."* Beispiel: *"Annahme 'Markdown + YAML reicht' decay'd, wenn agentic-pattern-Literatur überwiegend Schema-zentrale Specs (JSON Schema Top-Level, Markdown nur als Beschreibung) empfiehlt."*
3.  **Run die Tests.** Wenn ein Test feuert, halte den aktuellen Architektur-Zweig an, öffne die Annahme erneut, re-run Falsifikation.
4.  **Logge das Audit.**

### R — Reconcile (Architektonische Integrations-Entscheidungen mit ADRs)

Pro Konflikt-Punkt zwischen den drei Domains, schreibe ein **Architectural Decision Record**:



\#\#\# ADR-\[NN\]: \[Title — what is decided\]



\*\*Status:\*\* Accepted / Superseded by ADR-\[NN\] / Open



\*\*Context:\*\* \[Welcher Konflikt zwischen welchen zwei oder drei Domains? Welche Optionen existieren?\]



\*\*Options Considered:\*\*



\- Option A: \[Beschreibung\] — Pro: \[...\], Contra: \[...\]



\- Option B: \[Beschreibung\] — Pro: \[...\], Contra: \[...\]



\- Option C: \[Beschreibung\] — Pro: \[...\], Contra: \[...\]



\*\*Decision:\*\* Option \[X\], because \[Begründung mit Quellenstützung\].



\*\*Consequences:\*\* \[Was folgt aus dieser Entscheidung? Welche späteren Spec-Sektionen werden eingegrenzt? Welche Trade-offs werden akzeptiert?\]



\*\*Falsification Test (Method M01):\*\* \[Was würde diese Entscheidung als falsch erweisen?\]



\*\*Rejected Alternatives Note:\*\* \[Honest, non-strawmanned Beschreibung, warum Optionen B und C verworfen wurden — keine Rationalization.\]



**Mindestens-Anforderung:** Acht ADRs, abdeckend mindestens die folgenden Konflikt-Achsen:



1.  Spec-Format (Markdown / YAML / JSON Schema / Hybrid)
2.  Phase-Granularität (wie viele, wie linear)
3.  Coherence-Validierungs-Zeitpunkt (kontinuierlich / pro Phase / on-demand)
4.  Contradiction-Detection-Ansatz (regelbasiert / LLM-basiert / hybrid)
5.  Working-State-Repräsentation (Single Source of Truth vs. dekomponiert)
6.  Memory-Management-Pattern (FTS5 / Vector / Hybrid / klassisch hierarchisch)
7.  Clarifying-Question-Interface (synchron blocking / asynchron / queue-basiert)
8.  Recovery-Pattern (Rollback / Forward-Fix / Hybrid)



**Reflection-Eintrag pro ADR** (Anti-Strawman-Check).

### A — Architect (Die Spec — das Hauptartefakt)

Dies ist der zentrale Deliverable. Die Spec selbst hat folgende Sektionen (die genaue Reihenfolge und Sub-Struktur ist Architektur-Entscheidung der ausführenden KI, mit Begründung in einem ADR — aber diese Sektionen müssen alle vorhanden sein):



\# Dramatica Novel Specification (Spec)



\#\# Spec-Metadata



\- Version: \[...\]



\- Scope: \[...\]



\- Target-Agent-Profile: \[welche Kompetenzen muss das konsumierende agentische System mindestens haben?\]



\- Source-Skill / Source-Theory: Dramatica (Phillips & Huntley)



\- Spec-Format: \[Markdown + YAML / Markdown + JSON Schema / ...\]



\#\# Ontology — Dramatica Layer Schema



\[Pro Dramatica-Schicht eine typisierte Schema-Definition.



Beispiel:



\\\`\\\`\\\`yaml



story\_mind:



  type: object



  required: \[throughlines, domains, story\_driver, story\_limit, story\_outcome, story\_judgment, story\_goal, grand\_argument\]



  properties:



    throughlines:



      type: array



      length: 4



      items:



        $ref: '\#/definitions/throughline'



    ...



\\\`\\\`\\\`



\]



\#\# Choice-Space — Enumerated Valid Options Per Element



\[Für jedes Dramatica-Element die Liste der gültigen Optionen mit kurzer Definition.\]



\#\# Interaction-Constraints — Welche Wahl beschränkt welche



\[Permutationsregeln für Throughlines→Domains; hierarchische Constraints für Concerns→Domains; binäre Constraints für Driver/Limit/Outcome/Judgment.\]



\#\# Coherence-Invariants



\[Mindestens fünf explizit deklarierte Invarianten, die über den Story-Entwicklungs-Verlauf hinweg gültig sein müssen. Format pro Invariante:



\- ID



\- Statement (deklarativ)



\- Detection-Heuristik (regelbasiert / LLM-basiert / hybrid)



\- Severity bei Verletzung (BLOCKER / WARNING / NOTICE)



\- Resolution-Protokoll\]



\#\# Contradiction-Detection (drei Klassen)



\#\#\# Klasse 1 — Strukturelle Contradictions



\#\#\# Klasse 2 — Inhaltliche Contradictions



\#\#\# Klasse 3 — Pragmatische Contradictions



\[Pro Klasse: Detection-Heuristik, Schweregrad, Resolution-Protokoll.\]



\#\# Clarifying-Question Protocol



\- Trigger-Bedingungen (formal: wann fragt der Agent den Menschen?)



\- Frage-Format (strukturiert, mit enumerated Optionen wo möglich, Default-Vorschlag, Begründung warum die Frage gestellt wird)



\- Antwort-Integrations-Mechanismus (wie wird die Antwort in den Working-State zurückgespielt? Was wird invalidiert?)



\#\# Phase-Definitions



\[Sequenz der Phasen. Pro Phase:



\- Phase-Name und Phase-ID



\- Pre-Conditions (was muss vor Phase-Eintritt erfüllt sein)



\- In-Phase-Activities (was tut der Agent in dieser Phase)



\- Acceptance Criteria (mindestens drei, jeweils binär entscheidbar)



\- Post-Conditions / Output an die nächste Phase



\- Immutable Working-State-Felder nach Phase-Exit\]



\#\# Working-State Schema



\[Was hält der Agent zwischen Phasen? Schema für die persistente State-Repräsentation. Distinguish: ephemere Reasoning-Notes vs. immutable Story-Decisions vs. revisable Working-Drafts.\]



\#\# Failure-Modes Catalog (mindestens zehn)



\[Pro Failure-Mode: Beschreibung, Detection-Signal, Recovery-Pfad, Severity, Verhinderungs-Heuristik (wie wird er vermieden, nicht nur gefangen).\]



\#\# Regression-Checks



\[Wenn Spec-Felder geändert werden, was muss re-validiert werden? Welche Coherence-Invarianten müssen erneut geprüft werden?\]



\#\# Self-Verification Test Suite



\[Eine Sequenz von Tests, die das agentische System gegen die Spec laufen lassen kann, um zu verifizieren, dass eine in-Entwicklung Story spec-konform ist.\]



**Pro Spec-Sektion:** Reflection-Eintrag (F1, F3, F5 minimum). Dokumentation der Architektur-Entscheidung, falls noch nicht in einem ADR.

### C — Contradiction-handling (eingebettet in DRACO-A, hier expandiert)

Die Spec **ist nicht nur fail-tolerant**, sie ist **fail-detection-aktiv**. Drei Mechanismen-Klassen, die in der Spec explizit ausgearbeitet sind:



1.  **Strukturelle Contradictions** — durch Schema-Validation gefangen. Beispiel: zwei Throughlines auf demselben Domain. Detection: Schema-Constraint-Verletzung. Severity: BLOCKER. Resolution: auto-revert mit Annotation, oder Clarifying-Question wenn beide Throughlines nicht-trivial.



1.  **Inhaltliche Contradictions** — Aussagen über die Story, die einander widersprechen, ohne strukturell verboten zu sein. Beispiel: in Phase 3 wird Charakter X als impuls-getrieben festgelegt; in Phase 5 wird eine Schlüsselszene als rein rational kalkuliert für X spezifiziert. Detection: LLM-basierte Konsistenzprüfung gegen die Working-State-Historie, getriggert an definierten Coherence-Checkpoints. Severity: WARNING (Verstand kann Auflösung produzieren) oder BLOCKER (wenn der Widerspruch eine Coherence-Invariante verletzt). Resolution: Clarifying-Question.



1.  **Pragmatische Contradictions** — Detail-Wahlen, die das Story Goal oder den Grand Argument strukturell unterminieren. Beispiel: das Story Goal wurde als "Wahrheit aufdecken" festgelegt; eine Akt-3-Szene legt aber fest, dass die Wahrheit am Ende undeckend bleibt. Detection: Heuristik-Check der spätfestgelegten Details gegen die früh-festgelegten Story-Level-Decisions. Severity: BLOCKER (Story Goal ist Top-Level). Resolution: Clarifying-Question mit explizitem Trade-off-Vorschlag.



**Pro Klasse muss die Spec konkret enthalten:** Detection-Heuristik (Pseudocode oder formale Regel), Severity, Resolution-Protokoll. Keine Lücken — wenn keine Heuristik existiert, dokumentiere als Open Question.

### O — Operationalize (eingebettet in DRACO-A, hier expandiert)

Vier Operationalisierungs-Sub-Bereiche müssen in der Spec spezifiziert sein:



(a) **Phase-Transition-Contracts** — Pre-Conditions, In-Phase-Activities, Post-Conditions, immutable Felder nach Transition. Pro Phase als ausgefüllte Tabelle.



(b) **Clarifying-Question-Protokoll** — formale Trigger-Bedingungen, strukturiertes Frage-Format mit Default-Vorschlägen und Begründungs-Pflicht, Antwort-Integrations-Mechanismus. Inkludiere konkretes Beispiel-Format als YAML / JSON Schema.



(c) **Memory- und Context-Management** — Working-State-Schema (siehe DRACO-A), Persistenz-Strategie (was wird zwischen Sessions rehydratisiert), Context-Drift-Schutz (wie wird verhindert, dass spätere Phasen frühe Decisions silent neu interpretieren?).



(d) **Recovery- und Rollback-Patterns** — pro Failure-Mode-Klasse die definierte Recovery-Sequenz. Distinguish: Local-Recovery (innerhalb der aktuellen Phase), Phase-Rollback (zurück in eine frühere Phase), Hard-Stop-mit-Clarifying-Question.



-----

## PRE-SYNTHESIS INTEGRITY CHECK

Vor dem Schreiben der finalen Spec, führe diesen Verifikationspass schriftlich aus.



1.  **Re-read Constraint Blocks 0–5 verbatim.** Bestätige.
2.  **Re-read Critical-Thinking-Method-Blöcke.** Bestätige Anwendung pro Methode.
3.  **Reflection-Audit.** Zähle Reflection-Einträge. Minimum: 5 Standard + 5 DRACO-Komponenten + 2 Pre-Mortem/Red-Team + 8+ ADR-Reflections + Domain-Iterations + Spec-Sektionen = mindestens 30 Einträge.
4.  **Query-Expansion-Audit (M13).** Pässe entlang aller vier Achsen. Mindestens ein Pass auf der Orthogonal-Achse mit explizit-namentlich-genannter Quell-Disziplin (Game-Design / Tabletop-RPG / Constraint-Logic / Industrielle-Spec-Sprache / andere).
5.  **Cross-Pollination-Audit.** Step i.b und Step i.c ausgeführt und geloggt.
6.  **Constraint-Compliance-Audit.** Pro Block 0–5, zitiere ein konkretes Beispiel der Befolgung.
7.  **Spec-Quality-Invarianten-Audit (Constraint Block 4 Q1–Q10).** Pro Invariante explizit prüfen und Status notieren (PASS / FAIL / PARTIAL mit Begründung).
8.  **Single-Artifact-Audit (Constraint Block 5).** Bestätige: die Spec ist eine Datei. ODER dokumentiere die Eskalation explizit.



Erst nach allen acht Items darfst du die Spec schreiben.



-----

## SYNTHESIS — Final Output

Das primäre Deliverable ist die **Spec selbst**. Alle Audit-Logs sind Methodology-Appendix.



Schema:



\# \[Dramatica Novel Specification — final spec, ready for agentic consumption\]



\[Die Spec selbst, alle Sektionen aus DRACO-A vollständig ausgefüllt. Dies ist das Hauptartefakt — selbsttragend, copy-paste-fähig, in einer Datei.



Mindestumfang: nicht künstlich begrenzt, aber alle Q1–Q10-Invarianten erfüllt.\]



\---



\# Methodology Appendix



\#\# Architectural Decision Records (mindestens acht)



\[Volle ADRs für alle Major-Architektur-Entscheidungen.\]



\#\# Reflection History (CONSTRAINT BLOCK 0)



\[Mindestens 30 Reflection-Einträge in Reihenfolge.\]



\#\# Query Expansion Log (Method M13)



\[Pro Erweiterung: Achse, Query, Novel-Finding, Modify-Conclusion.\]



\#\# Cross-Pollination Logs



\#\#\# B → A (Surviving-Branch Triangulation)



\#\#\# C → A (Hypothesis Half-Life Audit)



\#\# Pre-Mortem-Analyse (Method M03)



\[Top-10 Failure-Modes mit Detection-Signalen und Mitigations. Mapping zu Spec-Failure-Modes-Catalog.\]



\#\# Red-Team-Review (Method M09)



\[Pro Major-Spec-Sektion drei Angriffe und ihre Behandlung — repaired / conceded / open-question.\]



\#\# Contradiction Log



\[Quellen-Disagreements zwischen Dramatica-Lehrlinie und SDD-Praxis und agentic-Pattern-Praxis, mit Auflösung pro ADR.\]



\#\# Falsifications-Audit (Method M01)



\[Pro zentrale Architektur-Hypothese: Disconfirmation-Queries und Resultate.\]



\#\# Open Questions / Unresolved



\[Was die Recherche nicht klären konnte; Architektur-Entscheidungen die als "tentative" geflaggt sind.\]



\#\# Sources



\[Strukturierte Quellenliste.\]



**Wichtig zur Auslieferung:** Die Spec selbst und der Methodology Appendix sind in **einer Datei** (Single-Artifact-Mandat). Aber visuell und navigatorisch klar getrennt. Die Spec ist Teil 1, der Appendix ist Teil 2.



-----

## SELF-VERIFICATION CHECKLIST FOR THE EXECUTING AI (v2.1 · 11 items)

Bevor du die Spec ausläufst:



  - Jeder Hauptschritt (jede Domain-Iteration in DRACO-D, jeder ADR in DRACO-R, jede Spec-Sektion in DRACO-A) begann mit einem verbatim Restatement Checkpoint.
  - CONSTRAINT BLOCK 0 (Reflection Baseline) wurde an allen Checkpoints honoriert. Minimum 30 Reflection-Einträge.
  - Method M13 (Adversarial Query Expansion) wurde entlang aller vier Achsen invoked. Orthogonal-Achse hat mindestens eine explizit-namentliche Erweiterung (Game-Design-Specs / Tabletop-RPG / Constraint-Logic / Industrielle Spec-Sprache / andere).
  - Beide cross-pollinated Steps (i.b Surviving-Branch Triangulation; i.c Hypothesis Half-Life Audit) wurden ausgeführt und geloggt.
  - Jede aktive Critical-Thinking-Methode hat konkrete Anwendung (M01 Falsification mit Disconfirmation-Queries; M03 Pre-Mortem mit Top-10 Causes; M09 Red Team mit Pro-Sektion-Angriffen; M10 First Principles mit Cross-Domain-Dekomposition; M13).
  - Mindestens acht ADRs sind geschrieben, je mit Optionen / Begründung / verworfenen Alternativen / Falsifikations-Test / Anti-Strawman-Reflection.
  - Der Spec-Quality-Invarianten-Audit (Q1–Q10 aus Constraint Block 4) ist abgeschlossen mit Status pro Invariante.
  - Alle Findings im Temporal Scope (Constraint Block 2). Speziell: SDD- und agentic-Pattern-Findings haben Datum und liegen in den jüngeren Fenstern (2023+ bzw. 2024+).
  - Keine Findings fallen in Output Exclusions (Constraint Block 3). Insbesondere: kein narrativer Roman-Inhalt; keine Marketing-Sprache; nicht reduziert auf "ist nur eine SKILL.md".
  - Der Pre-Synthesis Integrity Check wurde schriftlich ausgeführt (alle 8 Items).
  - Die Spec ist als selbsttragendes Single-Artifact ausgeführt (Constraint Block 5), oder die Eskalation ist dokumentiert. Reflection History, Query Expansion Log, Cross-Pollination Logs, Pre-Mortem-Analyse, Red-Team-Review, Contradiction Log, Falsifikations-Audit und ADRs sind als Methodology Appendix klar getrennt von der Spec selbst angefügt.



Wenn ein Item fehlschlägt, repariere vor Auslieferung.



-----



*Ende des Research-Prompts. Beginne mit der Restate-Erste-Aktion (DRACO A + DRACO O verbatim restate), dann Kickoff-Reflection, dann Reason 1.*
