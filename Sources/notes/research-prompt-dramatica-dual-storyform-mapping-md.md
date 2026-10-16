---
source: Sources/drive/research-prompt-dramatica-dual-storyform-mapping-md.md
read: "2026-10-11, the whole document (L1 to L1040) through read.py with line numbers, in three ranges; by a document-reader subagent (Sonnet)"
stance_markers: ["Restate", "WICHTIG", "Spezial-Erinnerung", "Forschungsprompt"]
stance_marker_count: 10
reads_as: "a research prompt for an executing agent, in its own word a Forschungsprompt that asks for and specifies a Dramatica dual-storyform mirroring for the novel; it reports no result"
---

# Note — research-prompt_dramatica-dual-storyform-mapping.md

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document is a prompt: it asks, instructs and specifies, and its sentences about the novel are a brief handed to an agent, not a finding.

## 1 · What kind of text this is, and how it marks itself

- The document names itself and its reader: „Dieser Prompt ist vollständig selbsthaltend.“ ^[L45]
- It ends with an order, not a conclusion: „Ende des Forschungsprompts. Führe jetzt aus.“ ^[L1039]
- The word `Forschungsprompt` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] stands once as a name for itself in running text, and `Restate` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#7] seven times as an instruction word. **Observed:** the stance markers are the imperative verbs and the labels of the template (`WICHTIG` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1], `Spezial-Erinnerung` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1]); no passage reports a finding.
- It classifies its own task as exploring, not collecting: „Diese Recherche ist eine Exploration, keine Extraktion.“ ^[L57]
- The Synthesis section is an empty output template with bracketed placeholders: „Fülle das folgende Schema vollständig aus.“ ^[L809] **Observed:** L813 to L997 hold headings and bracketed instructions only.
- The five methods repeat five labels each (the profile lists them). **Observed:** the labels are template fields, `What it is`, `Why it is in this prompt`, `How to apply it`, `When to stop` and `Example trigger`, not terms of the novel.

## 2 · The mirroring (Dual-Storyform-Spiegelung) — what the prompt asks to be defined

- The primary task, in the imperative: „Definiere eine klare, mathematisch konsistente Dual-Mapping-Spiegelung“ ^[L167]
- Its formal definition is given as a tuple of two storyforms with an inversion map; the prompt labels this definition „Spiegelungs-Definition (formal)“ ^[L527]
- Domain inversion is one of five properties, with sample inversions, and the choice among them is left to the hypothesis: „Welche Inversion gewählt wird, ist Teil der Mapping-Hypothese.“ ^[L531]
- The pronoun axis is inverted too, with sample pairs: „Die Pronomen-Achse erfährt ebenfalls eine wohldefinierte Spiegelung.“ ^[L532]
- A hard limit on layers is stated as a rule: „Drei oder mehr Ebenen sind verboten“ ^[L533] — the prompt calls it a user constraint in the same line.
- The two storyforms may differ in ending: „Outcome-Asymmetrie ist erlaubt“ ^[L535]
- The deliverable is counted by a heading of the output template: „Mindestens zwei vollständige Dual-Storyform-Alternativen“ ^[L849]
- The template bounds the count above in a bracketed instruction: „Maximum vier insgesamt“ ^[L909]

## 3 · MIRROR and the prompt's own method vocabulary

- The structural frame is the prompt's own synthesis: „bespoke Framework synthetisiert“ ^[L121]
- Its six parts are traced to named prompt frameworks: „Provenienz (für Auditierbarkeit)“ ^[L142]. **Observed:** `RISEN`, `TIDD-EC`, `CRISPE`, `CARE` and `CO-STAR` stand only in the front matter and in this provenance list (L24 to L29, L146 to L151, plus L121); they are borrowed labels, not the prompt's structure.
- The agentic loop is named ReAct and has three phases: „Jede Iteration besteht aus drei Phasen“ ^[L77]
- The reflection rule is a gate: „Ein erreichter Checkpoint ohne schriftlichen Reflexions-Eintrag ist ein unvollständiger Checkpoint“ ^[L235]
- The prompt names a checkpoint at which constraints and methods are restated before each step: `Restatement Checkpoint` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#3] stands three times.
- Two steps are described as imports from other prompt categories: „Dieser Step importiert eine Lifecycle-Disziplin aus Kategorie C“ ^[L717]
- The label `M13` stands 6 times and `M01` twice, as a short name for a method that the method headings do not number: `M13` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#6], `M01` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#2]. **Observed:** the headings of the methods carry no number.

## 4 · The novel's world, as the brief states it

The Story-Hintergrund block is a set of capsule descriptions that the prompt tells the agent to honour as constraints and not to elaborate. Each capsule is the prompt's own summary of the novel, not a reading with evidence.

- The block's purpose: „WICHTIG: Dieser Block dient“ ^[L189] — the line goes on to say that the agent should know the central concepts and not elaborate them.
- The prompt describes AEGIS in a few terms: „Tragischer Gott, autopoietisch, operativ geschlossen“ ^[L197]
- The prompt gives AEGIS a way of acting: „löscht durch Funktionieren statt durch Gewalt“ ^[L197]
- The prompt says what AEGIS does to qualia: „missdeutet Qualia als Rauschen“ ^[L197]
- It names a „Wahrer Kollaps-Kern“ ^[L197] for AEGIS, with the index written `K0` in the export.
- Kael is described as bearer of an axis: „Träger der psychologischen Integrationsachse“ ^[L193]
- Juna is described as a composite: „Komposit aus Quanten-Witness“ ^[L201]
- The same capsule gives her properties: „algorithmisch irreduzibel, wahr und aktiv“ ^[L201]
- It adds that AEGIS cannot model her: „für AEGIS unmodellierbar“ ^[L201]
- Moonshine-Link: the prompt calls it a non-local connection between Kael and Juna: „Nicht-lokale Verbindung“ ^[L205], and says that AEGIS cannot see it: `AEGIS-unsichtbar` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1].
- The Guardians are four subsystems of AEGIS: „Vier funktionale Untersysteme von AEGIS“ ^[L209]
- The prompt says they correlate with the Kernwelten: „korrelieren mit den vier“ ^[L209]
- The Alter-System is described as thirteen alters: „13 Alter mit eindeutigen Funktionen“ ^[L213]
- The capsule gives the writing a duty: „Polyphonie ist narrative Pflichtleistung“ ^[L213]
- Dual-Kernel-Theorie: the prompt says every act of control makes the entropy it fights: „jeder Kontroll-Akt erzeugt die Entropie“ ^[L217]
- Vortex-Inversion is described as a pivot of the driver with two endings at once: „duale Outcomes simultan“ ^[L221]

## 5 · Juna — what the prompt asks of her anchoring

- A secondary goal is stated: „Juna explizit stärker in der Geschichte verankern“ ^[L175]
- The earlier construction is reported by the prompt as placing her outside the quad: „außerhalb der Quad“ ^[L175]
- The capsule gives her a fifth position: „Operationalisiert als 5. Position außerhalb der Standard-Dramatica-Quad“ ^[L201]
- The prompt asks what anchoring means formally: „Eine Quad-Position, eine Sekundär-Schicht oder eine außer-Quad-Position?“ ^[L637] — the options are put as a question, not decided.
- Friction at her anchor is a mapping task: „Wo wird Juna explizit verankert?“ ^[L131]
- `Juna-Anker` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#3] is the prompt's own name for the anchor point and appears as a column of the output table.

## 6 · Dramatica terms as borrowed theory

- The quad axiom is stated for the agent to restate: „Jede Dramatica-Throughline besetzt genau eine der vier Domains“ ^[L511]
- The prompt calls the dynamic tuple a set of four axes: „Diese vier Achsen produzieren 16 Dynamik-Kombinationen.“ ^[L519]
- It says of the Dramatica words Domain, Throughline and Storyform that they only seem atomic: „wirken, als wären sie atomar“ ^[L427]
- The abbreviations MC, IC, OS and RS are written in the formal block (L511, L515); **observed:** the document never writes the word `Influence`, count 0 (`Influence` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#0]), and uses `Impact-Charakter` once, for Juna, at L201.

## 7 · The status of earlier storyforms, and of the prompt itself

- The prompt reports a user directive with a date: „Keiner der bisherigen Storyforms gilt als Kanon.“ ^[L225]
- The earlier storyforms are named in the exclusion list, which forbids reproducing them as canon: „Heuristics of Integration“ ^[L306] is the title given to storyform A there
- The same list gives storyform B a title: „Phoenix Collapse“ ^[L306]
- The steelman of the earlier construction is defined as a baseline: „Die Steelman-Form ist Vergleichspunkt, nicht Lösung.“ ^[L683]
- **Observed:** `Kanon` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#4] stands four times (L163, L225, L683, L797), each about the earlier storyforms or the steelman, none about the prompt itself. These are the prompt's statements and are recorded, not applied.

## 8 · Said two ways, or left open — recorded, not resolved

- Juna's place, one way: the capsule says „außerhalb der Standard-Dramatica-Quad“ ^[L201]
- The formal axiom, another frame: „MC, IC, OS, RS belegen jede eine andere Domain“ ^[L511] — four throughlines, none of them named Juna.
- A third form is a sample of an invented notebook answer, not a claim about the novel: „Juna ist IC in Storyform A“ ^[L419] — the line sets it beside another invented answer that places her outside the quad. **Observed:** the prompt puts the alternatives and decides none.
- The capsule gives the two storyforms different endings: „Storyform A endet Success/Good“ ^[L221]

## 9 · Absent, counted

- The document has no filled output. **Observed:** the Synthesis headings at L813 to L997 carry bracketed placeholders only.
- **Observed:** the prompt reports no result. The word `Kernwelt` stands once, in the list of story concepts, and `Kernwelten` once, in the Guardians capsule: `Kernwelt` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1], `Kernwelten` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1].
- `Chaitin` stands alone 0 times (it is written `Chaitin-Ω`): `Chaitin` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#0]
