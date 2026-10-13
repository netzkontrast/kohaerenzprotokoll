---
source: Sources/drive/narrative-context-protocol-ncp-spezifikation.md
read: "2026-10-12, the whole document (L10 to L223) through read.py with line numbers; by a document-reader subagent (Sonnet)"
stance_markers: ["Vorschlag", "vorgeschlagene"]
stance_marker_count: 3
reads_as: "a German white paper in three parts that proposes a specification for the Kohärenz Protokoll: Dramatica values for four subsystems, a JSON schema, a four-prompt cascade and an oversight component, with its own risks and roadmap"
---

# Note — Narrative Context Protocol (NCP) Spezifikation

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document speaks as a proposal that rates itself as foundational: its stance words are `Vorschlag` ^[narrative-context-protocol-ncp-spezifikation.md:#1] and `vorgeschlagene` ^[narrative-context-protocol-ncp-spezifikation.md:#2].

## 1 · What kind of text this is, and how it marks itself

- The document describes its object as „ein agentives, interaktives Erzählerlebnis“ ^[L15].
- It introduces its table as a proposal: „Die folgende Tabelle präsentiert einen Vorschlag für die hochrangigen Dramatica-Spezifikationen“ ^[L45].
- It states its own architecture as proposed: „Die vorgeschlagene Architektur unterscheidet sich fundamental von gängigen Paradigmen“ ^[L83].
- It ranks Table 1 itself: „Diese Tabelle ist die entscheidende kreative und logische Grundlage.“ ^[L63]. This is the document's claim about its own standing and is recorded, not applied.
- Observed: the document has three parts (headings L13, L77, L169), 16 headings by the profile, and no labels on passages and no named speaker. The prose in L10 to L219 is the document's own; the numbered list after L221 is a list of references.

## 2 · The four subsystems of the novel and their Dramatica values

- The document names the four subsystems of the novel in one parenthesis: „Die vier definierten Story-Subsysteme (Kael, AEGIS, Juna/V, Das Fundament)“ ^[L30].
- It says the four stand for the four throughlines of the whole system. The Dramatica theory it applies is the one that postulates the throughlines: „Dramatica postuliert vier fundamentale Perspektiven, die sogenannten“ ^[L23].
- It states the literal reading of the model for this project: „Für dieses Projekt ist dies kein Metapher, sondern das buchstäbliche Betriebsprinzip.“ ^[L19].
- Table 1 header row names the four columns: „Kael (Psychologische Ebene) | AEGIS (Logisch-Systemische Ebene) | Juna/V (Ontologische Ebene) | Das Fundament (Metaphysische Ebene)“ ^[L51].
- The table's row `Primäre Rolle` gives, in the order Kael, AEGIS, Juna/V, Das Fundament: „Main Character (MC) | Obstacle Character (IC) | Objective Story (OS) | Subjective Story (SS)“ ^[L52].
- Domain: „Mind (Fixierte Haltung) | Physics (Aktivität) | Universe (Situation) | Psychology (Manipulation)“ ^[L53].
- Concern: „Conscious (Bewusstes/Kontemplation) | Obtaining (Erlangen/Erreichen) | Future (Zukunft) | Becoming (Werden/Transformation)“ ^[L54].
- Issue: „Appraisal vs. Re-appraisal | Self-Interest vs. Morality | Faith vs. Disbelief | Commitment vs. Responsibility“ ^[L55].
- Problem: „Doubt (Zweifel) | Control (Kontrolle) | Inequity (Ungleichgewicht) | Temptation (Versuchung)“ ^[L56].
- Solution: „Certainty (Gewissheit) | Uncontrolled (Unkontrolliertheit) | Equity (Gleichgewicht) | Conscience (Gewissen)“ ^[L57].
- Symptom: „Logic (Logik) | Proaction (Proaktion) | Avoidance (Vermeidung) | Help (Hilfe)“ ^[L58].
- Response: „Feeling (Gefühl) | Reaction (Reaktion) | Pursuit (Verfolgung) | Hinder (Behinderung)“ ^[L59].
- Goal: „Understanding (Verständnis) | Learning (Lernen) | The Past (Die Vergangenheit ändern) | Conceptualizing (Ein neues Konzept entwickeln)“ ^[L60].
- Consequence: „Memories (In Erinnerungen gefangen) | Doing (Sinnloses Tun) | Progress (Unkontrollierter Fortschritt) | Being (In einem Zustand verharren)“ ^[L61].
- It describes the values as a profile: „Diese Werte sind nicht willkürlich, sondern bilden ein kohärentes psychologisches Profil“ ^[L63].
- It assigns each subsystem a stylistic voice: „Kael (emotional, fragmentiert), AEGIS (logisch, kühl) oder Juna/V (transzendent, fremdartig)“ ^[L190].
- Observed: the document gives each subsystem one set of storyform values (L51 to L61) and no values for the further three throughlines inside each subsystem that L30 says exist.

## 3 · Interference of the subsystems

- The document names three types of interference after the relations inside a Dramatica quad. The first: „Elemente, die sich in einem Quad diagonal gegenüberliegen“ ^[L71].
- It applies the diagonal pair to two of the subsystems: „Wenn Kael von Faith und AEGIS von Disbelief angetrieben wird, ist ihre Interaktion von Natur aus unvereinbar“ ^[L71]. Faith and Disbelief stand in Table 1 as Issue of one subsystem and Issue of another (L55); the sentence uses them as the driving problems.
- Second type: „Elemente, die horizontal benachbart sind“ ^[L72].
- Third type: „Elemente, die vertikal benachbart sind, stehen in einer kausalen oder konsekutiven Beziehung.“ ^[L73].
- Observed: the three types are headed `Dynamische Paar-Interferenz`, `Begleiter-Paar-Interferenz` and `Abhängige Paar-Interferenz` (L71 to L73).

## 4 · The Narrative Context Protocol and its state

- The document defines the protocol's role: „Das NCP ist die persistente, strukturierte Datenbasis“ ^[L105], and puts „Single Source of Truth“ ^[L105] in quotation marks as its standing. Recorded, not applied.
- The system is described as „ist ein zustandsbehafteter, zyklischer Agent“ ^[L87].
- Observed: the schema block (L109 to L157) holds `worldState` with `activeFocalSystem` set to Kael (L115) and the four system states Kael (L117), AEGIS (L126), JunaV (L132) and DasFundament (L137). Initial values given there: AEGIS has `entropyLevel` Low (L128), JunaV has `resonanceSignalStrength` 0.0 (L134), DasFundament has `lastLawInvoked` Causality (L139).
- Observed: `thematicAffinity` in `userModel` lists Faith, Control and Logic (L150 to L152), the names that appear as values in Table 1.

## 5 · The prompt cascade

- The cascade is four prompts: State Analysis Prompt, Context Compression Prompt, Narrative Generation Prompt and State Update Prompt, listed with their loop phases in Table 2 (L96 to L99). One row reads „Observe & Orient (Beobachten & Orientieren)“ ^[L96].
- The compression prompt is to counter a tendency that the document attributes to studies it reports: „Studien zeigen, dass LLMs dazu neigen, homogene, positive und spannungsarme Narrative zu erzeugen.“ ^[L165]. The studies' claim is theirs, reported by the document.
- The narration prompt is to let a subsystem's state show without naming it: „wird nicht als Fakt genannt, sondern manifestiert sich für Kael als flackerndes Licht“ ^[L166].

## 6 · The Dramaturgische Aufseher

- Declared as a component: „Dies ist kein vages Konzept, sondern eine konkrete architektonische Komponente“ ^[L175].
- Its role: „Der Dramaturgische Aufseher ist der entscheidende Mechanismus zur Balancierung von Emergenz (Bottom-up) und Konvergenz (Top-down).“ ^[L183].
- One of its three checks compares with the log: „Vergleicht die Implikationen des neuen Zustands mit dem narrativeLog“ ^[L181].
- Observed: the three checks are named `Strukturelle Integritätsprüfung` (L179), `Konvergenzprüfung` (L180) and `Kontradiktionsprüfung` (L181).

## 7 · The user, the risks, the roadmap

- The user model has a stated effect: „Wenn ein Nutzer wiederholt Entscheidungen trifft, die dem Thema Faith entsprechen“ ^[L191].
- One risk is named open: „ist eine ungelöste Forschungsfrage“ ^[L202].
- Roadmap: „Eine schrittweise Implementierung ist zur Risikominimierung unerlässlich.“ ^[L207]. Its five phases begin with „NCP & Storyform-Authoring. Die grundlegende kreative Arbeit, die ohne Code erfolgen kann.“ ^[L211] and end with „Entwicklung und Integration der Validierungsschicht zur Sicherstellung der langfristigen Kohärenz.“ ^[L215].
- Phase 4 adds the other subsystems: „Hinzufügen der verbleibenden drei Subsysteme und der interferenceRules.“ ^[L214].
- Closing claim: „legt das Fundament für eine neue Generation agentiver narrativer Erfahrungen“ ^[L219].

## 8 · Said two ways, or left open — recorded, not resolved

- Observed: the subsystem the prose and Table 1 write `Juna/V` (L30, L51) is `JunaV` in the schema (L132), and `Das Fundament` is `DasFundament` (L137).
- Observed: L30 calls each subsystem a full storyform with its own four throughlines; the table gives each subsystem a single primary role (L52). The document does not reconcile these two statements.
- Observed: the schema's array contents (`storyforms`, `interferenceRules`, `narrativeLog`) were lost in the export (L111, L112, L156), so the document as stored does not show the rules it says the protocol holds.

## 9 · Absent, counted

- No chapter is named: `Kap` ^[narrative-context-protocol-ncp-spezifikation.md:#0] and `Kapitel` ^[narrative-context-protocol-ncp-spezifikation.md:#0].
- `OODA-Loop-Phase` ^[narrative-context-protocol-ncp-spezifikation.md:#1] and `ReAct-Framework-Phase` ^[narrative-context-protocol-ncp-spezifikation.md:#1] stand once each, in the Table 2 header (L95); `OODA-Loop` ^[narrative-context-protocol-ncp-spezifikation.md:#0] and `ReAct` ^[narrative-context-protocol-ncp-spezifikation.md:#0] do not stand alone.
