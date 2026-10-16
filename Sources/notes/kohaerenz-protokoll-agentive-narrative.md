---
source: Sources/drive/kohaerenz-protokoll-agentive-narrative.md
read: "2026-10-12, the whole document (L1 to L670) through read.py with line numbers, in three ranges; by a document-reader subagent (Sonnet)"
stance_markers: ["Aufgaben", "Mitigation", "Empfehlung"]
stance_marker_count: 9
reads_as: "an architecture report that proposes a data schema, a prompt cascade, a symbolic overseer and a technology stack for an LLM-driven interactive narrative, mapping four narrative layers onto Dramatica storyforms and borrowed psychological and philosophical models"
---

# Note — Kohärenz Protokoll: Agentive Narrative

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document speaks as a recommendation about how to build the project, and it reports phrases of an earlier brief that it answers; where a sentence below gives such a phrase, it says so.

## 1 · What kind of text this is, and how it marks itself

- The document names itself an architectural draft: „Das vorliegende Dokument stellt den grundlegenden architektonischen Entwurf für das Projekt“ ^[L22]
- It says what it will do with the brief it answers: „Er validiert die Kernkonzepte des Auftrags“ ^[L26]
- Its stance labels are the field names of the plan and risk lists: `Aufgaben` ^[kohaerenz-protokoll-agentive-narrative.md:#4], `Mitigation` ^[kohaerenz-protokoll-agentive-narrative.md:#3] and, for a choice, `Empfehlung` ^[kohaerenz-protokoll-agentive-narrative.md:#2]. Together these stand 9 times.
- **Observed:** the body falls into four parts (headings Teil I to Teil IV, L30, L120, L362, L453), then a Schlussfolgerung (L571) and a numbered reference list of 88 web titles (L583 to L670) that the body points to by glued numbers.

## 2 · The four layers and the theory behind them

- The document says the four layers are not only parallel plot strands but „distinkte ontologische Schichten einer einheitlichen narrativen Realität“ ^[L34]
- Table 1 sets the four layers in its header row as „Psychologische Ebene (Kael)“ ^[L57] and, in the same row, „Logisch-Systemische Ebene (AEGIS)“ ^[L57], „Ontologische Ebene (Juna/V)“ ^[L57] and „Metaphysische Ebene (Das Fundament)“ ^[L57].
- The document calls the Table 1 assignments „statische, aber grundlegende Datenbasis“ ^[L51] for the schema's storyforms array.

## 3 · Kael (psychological layer)

- The document quotes the brief's phrase for Kael's story: „Heilungsreise eines fragmentierten Bewusstseins“ ^[L80]
- A state variable measures progress: „Misst den Fortschritt von Kaels psychologischer Integration“ ^[L299]
- Phase 1 of the build plan is Kael alone: „Vollständige Ausarbeitung der Dramatica-Storyform für Kael“ ^[L539]

## 4 · AEGIS (logical-systemic layer)

- The document reports the brief's phrase „traumatisierten Wächter-KI“ ^[L92] and then gives its own reasoning: „eine nicht-biologische Entität kein Trauma im menschlichen, psychologischen Sinne erfahren kann“ ^[L92]
- Its own modelling choice follows: „als eine Form von tiefgreifendem, systemischem und logischem Schaden modelliert“ ^[L92]
- The state of AEGIS is described by „Zielkonflikte, kaskadierende Fehler und logische Inkonsistenzen“ ^[L92]
- The variable `AEGIS.protocolAdherence` is defined by: „Gibt an, wie starr AEGIS an ihren fehlerhaften Kernprotokollen festhält“ ^[L302]
- For the focus on AEGIS the interface becomes a „parser-basierte Kommandozeile“ ^[L520]

## 5 · Juna/V (ontological layer)

- The document reports the brief's description of Juna/V as „transzendente, resonanzbasierte Kraft“ ^[L102], and draws from it that this points to „deutet auf eine Form der Intervention hin, die nicht auf direkter physischer Kausalität beruht“ ^[L102]
- The variable `JunaV.resonanceFrequency` is defined as: „Repräsentiert das spezifische narrative Thema“ ^[L303]
- In the interface proposal, Juna/V is the passive mode: „Die Benutzeroberfläche wird passiv und nicht-interaktiv“ ^[L522]

## 6 · Das Fundament (metaphysical layer)

- The document defines the layer: „Sie ist nicht eine Geschichte, sondern die Grammatik, nach der alle Geschichten geschrieben werden.“ ^[L113]
- It ties the layer to the schema's rules: „interferenceRules sind Ausdruck dieser tiefen Strukturen“ ^[L116]
- In the interface proposal the layer is mostly not interactive: „Diese Ebene ist typischerweise nicht direkt interaktiv“ ^[L523]
- Phase 3 adds the last two layers: „Hinzufügen von Juna/V und Das Fundament“ ^[L557]

## 7 · The Narrative Kontext Protokoll (NCP)

- The document gives the schema a standing: „Das NCP ist die alleinige Quelle der Wahrheit für das gesamte System“ ^[L132] This is the document's own claim about a proposed schema, recorded and not applied.
- The world's dynamic state is kept apart from the static storyforms; the variable dictionary is introduced as „ein klares Wörterbuch der worldState-Variablen“ ^[L292]
- For storage it proposes two databases: „Es wird daher eine hybride Datenbankstrategie empfohlen“ ^[L314]

## 8 · The prompt cascade and the overseer

- The cascade is read as a cognitive loop: „implementiert einen agentiven kognitiven Kreislauf“ ^[L327]
- The document judges the compression step of the brief weak: „stellt den verwundbarsten Punkt des gesamten Systems dar“ ^[L349]
- It answers the brief's implicit assumption with a second view: „Der konzeptionelle Auftrag identifiziert korrekt die Notwendigkeit eines übergeordneten“ ^[L374] overseer; the assumption that the overseer be a prompt is, in the document's word, a design error: „stellt jedoch einen kritischen Designfehler dar“ ^[L374]
- Its own proposal for the overseer: „sollte nicht als LLM-Prompt, sondern als separates, symbolisches Logikmodul implementiert werden“ ^[L378]
- Its sample correction instruction (a prompt text for the system, not a passage of the story) names Kael: „Erzähle eine Szene, in der Kael ein plötzliches, unerklärliches Gefühl des Unheils verspürt“ ^[L388]

## 9 · Build order

- „Eine schrittweise Implementierung wird dringend empfohlen“ ^[L533]
- Phase 2 adds the second layer: „Entwicklung der AEGIS-Storyform und ihrer Zustandsvariablen“ ^[L548]

## 10 · Said two ways, or left open — recorded, not resolved

- **Observed:** the sentence that frames the overseer as part of the brief („Der konzeptionelle Auftrag identifiziert korrekt die Notwendigkeit“ ^[L374]) and the document's counter-proposal are two voices in one section; the first reports the brief, the second is the document's own.

## 11 · Absent, counted

- The document names no chapters: `Kapitel` ^[kohaerenz-protokoll-agentive-narrative.md:#0] and `Kap` ^[kohaerenz-protokoll-agentive-narrative.md:#0] stand 0 times.
- The world is given only as four layers; the document writes `Nexus` ^[kohaerenz-protokoll-agentive-narrative.md:#0] 0 times, and describes no place or event of the story.
