---
source: Sources/drive/spec-entwicklung-fuer-agentische-roman-entwicklung.md
read: "2026-10-12, the whole document (L1 to L498) through read.py with line numbers, in ranges; by a document-reader subagent (Sonnet)"
stance_markers: ["Akzeptiert", "Falsifikations-Test", "Verworfene Alternativen"]
stance_marker_count: 12
reads_as: "a specification artefact in German with English technical terms that turns the Dramatica model into schemas, rules and phase gates for an agent system, followed by a part of decision records and evaluation reports about that specification; it names no figure, place or chapter of any particular novel"
---

# Note — Spec-Entwicklung für agentische Roman-Entwicklung

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document speaks as a specification that gives rules, and in its second part as a report about itself.

## 1 · What kind of text this is, and how it marks itself

- The document calls itself an executable artefact: „Sie fungiert als primäres, ausführbares Artefakt im Sinne des Spec-Driven Design (SDD)“ ^[L15].
- It names two requirements as its foundation: „Die Architekturvorgabe (Komponente A) verlangt zwingend“ ^[L15].
- The second part is set off by its own heading: „Systemic Architectural Audit and Evaluative Records“ ^[L374]. Of its evaluation blocks the document says: „Sie dokumentieren die konzeptionelle Belastbarkeit der Architektur“ ^[L376].
- **Observed:** the decision records carry a repeated template of labels. `Akzeptiert` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#8] stands eight times, `Falsifikations-Test` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] twice and `Verworfene Alternativen` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] twice; the template is the document's own, not a term of a story world.
- **Observed:** the second part reads as a narrated past (six evaluation blocks, `Evaluierungsblock` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#6]), the first part as rules in the present.

## 2 · The Dramatica model as the document applies it

- The document gives the theory's central picture: „Die Dramatica-Theorie betrachtet eine vollständige Geschichte als Analogie für einen einzelnen menschlichen Verstand“ ^[L23]. The sentence reports the theory; the document then builds its schema on it.
- Time structure of each throughline: „Die zeitliche Gliederung durch vier Signposts und drei dazwischenliegende Journeys“ ^[L112].
- The categories are tabled as a closed set, and the document says why: „wird der Choice-Space hart limitiert“ ^[L133].
- Concerns are described as „spezifische Typen, die als primärer thematischer Fokus innerhalb einer Domain dienen“ ^[L141].
- Characters are defined through the elements: „Charaktere sind Agenten, die diese Elemente repräsentieren“ ^[L143].
- Story dynamics values appear only as a generic list of pairs (Success/Failure, Good/Bad and others) at L142; **observed:** no value is assigned to any particular story anywhere in the document.

## 3 · The rules the document lays down

- Diagonal domains: „Domain(Main Character) und Domain(Influence Character) müssen im Dramatica-Modell diagonal gegenüberliegen“ ^[L156]. The same line adds „Gleiches gilt zwingend für Domain(Objective Story) und Domain(Relationship Story)“ ^[L156].
- Growth: „Wenn Domain(OS) und Domain(MC) beide intern oder beide extern sind, muss der Growth-Wert“ ^[L159] the value Stop (the line continues past the quotation).
- INV-01: „Keine zwei Throughlines dürfen zu irgendeinem Zeitpunkt dieselbe Domain belegen“ ^[L171].
- INV-02: „Ein Story Outcome von Success in Kombination“ ^[L182] with a judgment of Good requires that the main character's solution is applied in the fourth signpost; the severity given is WARNING.
- INV-04: „Die Entwicklung der Handlung muss streng den vier Signposts pro Throughline folgen“ ^[L204].
- The rules together are called `Coherence-Invarianten` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2]; the document says that it „definiert diese Spezifikation narrative Kontinuität als die Erhaltung struktureller Invarianten unter Transformation“ ^[L165].
- Of the five INV rules the evaluation part says they „die den Kern der Ausfallsicherheit (Chaos-Resilienz) dieser Spezifikation bilden“ ^[L442].

## 4 · Contradiction classes, questions to the human, phase gates

- The document demands „zwingt das Agenten-System zur Implementierung einer dreistufigen, aktiven Widerspruchserkennung“ ^[L222].
- The structural class is defined as „Formale Regelbrüche gegen die Dramatica-Ontologie“ ^[L226]; the content class may be intended: „Inhaltliche Widersprüche können gelegentlich stilistisch gewollt sein“ ^[L235]; the pragmatic class is „Meta-narrative Widersprüche, bei denen lokale Szenenhandlungen die globale thematische Prämisse untergraben“ ^[L240].
- A question to the human is triggered when the evaluator „meldet eine Klasse-2-Contradiction mit einem CRS (Consistency Risk Score) von über 85%“ ^[L251].
- The protocol forbids open questions: „Agenten dürfen keine offenen Freitextfragen stellen“ ^[L424].
- Phase transitions are gated: „Ein Phasenübergang erfolgt nur, wenn alle Akzeptanzkriterien“ ^[L290] are met. The four phases are named `Storyforming` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#4] (as a word), `Story Encoding` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1], `Story Weaving` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] and `Story Reception` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1].
- The first phase table cell says the agent computes „Der Agent berechnet die 75 Appreciations“ ^[L297], and the last phase delivers „Das finale Manuskript des Romans“ ^[L300].

## 5 · Memory, failure modes, and the reasons given for decisions

- State is split as „Er trennt strikt zwischen immutable (Storyform) und ephemeral (Notes) Zuständen“ ^[L416].
- Failure row FM-09: „Das Token-Verhältnis zwischen OS und RS im Weaving weicht um mehr als 60% ab“ ^[L363].
- The format decision (ADR-01) picks a hybrid container: „Option C wurde gewählt“ ^[L388], and sets its own test: „Würden Agenten wiederholt halluzinieren, weil sie YAML innerhalb von Markdown fehlerhaft parsen“ ^[L388].
- ADR-02 chooses the four-phase model: „Die Übernahme dieser Stufen als agentische Phasen erzeugt die höchste logische Kohärenz“ ^[L396].
- ADR-03 gives validation timing and a reason: „Kontinuierliche semantische Prüfungen übersteigen das Token-Budget“ ^[L400].
- ADR-04 rejects a purely LLM-based detector „da LLMs bekanntermaßen Probleme mit exakten Zähl- und Logikaufgaben haben“ ^[L412].

## 6 · Said two ways, or left open — recorded, not resolved

- The document says what the enumerations are, yet **observed:** the YAML blocks give `enum:` with nothing after it at L50, L51 and L70 to L73, so the values of perspective, focus, driver, limit, outcome and judgment are not in the exported text; the table at L142 lists the dynamics pairs.
- The document claims for itself: „Die Konfidenz in die Robustheit der Architektur erreichte hier ein sehr hohes Niveau“ ^[L442], and at the close that it „behält durch die Hybridstruktur aus Markdown und strukturierten Datenschemata ihre Singularität als selbsttragendes Artefakt“ ^[L448]. These are the document's claims about its own standing; recorded, not applied.
- It states that it fulfils „alle aufgestellten Qualitätsinvarianten (Q1-Q10)“ ^[L448]; **observed:** `Q2` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#0] stands 0 times, so the ten Q invariants are not listed in the text.
- Its own admission of fragility: „Die Spezifikation ist inhärent instabil“ ^[L368], said of asynchronous corrections.

## 7 · Absent, counted

- No chapter is named: `Kap` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#0] and `Kapitel` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#0] stand 0 times as words.
- The project's own title `Kohärenz-Protokoll` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#0] stands 0 times. The word `Kohärenz` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] stands twice, in the sense of the specification's own logical coherence, for example „erzeugt die höchste logische Kohärenz“ ^[L396].
- **Observed:** the sample question at L266 to L283 uses the placeholder `Charakter X`; no figure of any novel is named.
