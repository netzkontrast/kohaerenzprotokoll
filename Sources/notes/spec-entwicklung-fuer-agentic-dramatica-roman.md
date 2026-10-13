---
source: Sources/drive/spec-entwicklung-fuer-agentic-dramatica-roman.md
read: "2026-10-12, the whole document (L1 to L593) through read.py with line numbers, by a document-reader subagent (Sonnet)"
stance_markers: ["BLOCKER", "WARNING", "NOTICE"]
stance_marker_count: 19
reads_as: "a specification for a multi-agent system that writes novels through the four Dramatica phases, with a method appendix of decision records, reflections and audits, in German prose with English identifiers"
---

# Note — Spec-Entwicklung für Agentic Dramatica-Roman

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document is a rulebook and a record of its own making; it names no figure, place or chapter of any particular novel.

## 1 · What kind of text this is, and how it marks itself

- The document calls itself „als primäres, maschinenlesbares und unmittelbar ausführbares Artefakt“ ^[L15].
- Its version line reads „2.1.0 (NCP-Integrated & State-Freezing Optimized)“ ^[L17].
- Its rules carry severity labels in the tables: `BLOCKER` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#9], `WARNING` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#9] and `NOTICE` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1]. **Observed:** the labels head the Severity column of the contradiction table (L206 to L211) and of the failure catalogue (L375 to L387); they say how a breach is handled, not what a term means.
- The method appendix opens: „Dieser Appendix dokumentiert die epistemologische Genese der Spezifikation“ ^[L408].
- **Observed:** the Reflection History (L450 to L481) is a numbered list in the first person with the markers F1 to F5, and names no speaker.

## 2 · The state object and the layers

- The document names the Narrative Context Protocol as its ontological basis: „Die ontologische Basis dieser Spezifikation bildet das Narrative Context Protocol (NCP)“ ^[L26].
- It says the protocol „und erzwingt narrative Kohärenz.“ ^[L26].
- The schema of L39 to L112 gives four layers: `version_layer`, `author_intent_layer`, `storyform_layer`, `beat_layer`. **Observed:** these are written with backslash-escaped underscores in the export (L42), and the enum lists of the story dynamics are empty (L64 to L71).
- It states its decision for one central state object: „SSOT über das Narrative Context Protocol (NCP), verwaltet als zentrales JSON-Objekt.“ ^[L434].

## 3 · The Dramatica vocabulary it applies

- It reports an update of vocabulary: „Die veraltete Metapher des“ ^[L28] is followed in the line by the replacement terms; the schema marks the old names as former: „Ehemals Mental Sex “ ^[L67].
- The Choice-Space is closed: „operiert das agentische System in einem absolut geschlossenen Choice-Space“ ^[L117].
- Each throughline takes one concern: „Jede Throughline erfordert exakt ein Concern“ ^[L125].
- The row of classes lists „Universe, Physics, Mind, Psychology“ ^[L124].
- The document says of the Dramatica theory: „Die Dramatica-Theorie basiert auf relationaler Ontologie.“ ^[L131].
- **Observed:** no value is assigned to any throughline of a particular story; the lists at L124 to L127 are the generic choice space, and the example at L236 is a placeholder (`Charakter X`).

## 4 · Constraints, invariants, contradictions

- IC-04 couples growth to the domains: „Wenn domain(OS) und domain(MC) beide intern oder beide extern sind, MUSS growth == Stop sein.“ ^[L141].
- INV-01 forbids a shared domain: „Keine zwei Throughlines dürfen zu irgendeinem Zeitpunkt dieselbe Domain belegen.“ ^[L151].
- INV-04 binds outcome to the fourth signpost: „erfordert zwingend, dass im vierten Signpost das solution-Element des Main Characters narrativ ausgeführt wird.“ ^[L184]; the resolution is that „Der Mensch muss entscheiden, ob das Ende reklassifiziert“ ^[L187].
- The contradictions come in three classes: „Das System implementiert eine dreistufige Architektur“ ^[L202]; the table names them `Strukturelle Contradictions` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1], `Inhaltliche Contradictions` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] and `Pragmatische Contradictions` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1].
- Agents may not ask free questions: „Agenten dürfen keine offenen Freitextfragen stellen.“ ^[L215].

## 5 · Phases and context management

- The phases are gated; the document says: „Ein Übergang erfolgt erst, wenn alle Acceptance Criteria (Gates) erfüllt sind.“ ^[L259]. The four phases are `Storyforming` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#5], `Story Encoding` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2], `Storyweaving` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#3] and `Story Reception` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2].
- Phase 1 locks its object: „gegen Schreibzugriffe gesperrt“ ^[L277].
- Phase 3 requires „Exakt 4 Signposts pro Throughline sind definiert.“ ^[L306].
- The line budget is stated: „Die primäre SKILL.md Datei ist hart auf“ ^[L340] 500 lines (the number follows on the same line).
- `State Freezing` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#11] and `Context Rot` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#15] are the two mechanisms the appendix returns to most.

## 6 · Said two ways, or left open — recorded, not resolved

- The document names its own conflict: „Die Spannung wurde in ADR-06 und ADR-07 gelöst.“ ^[L553]. **Observed:** the conflict is between the holistic story mind and progressive disclosure (L553); the resolution is the document's own claim.
- It keeps the structure rigid but allows flexibility inside it: „Die Architektur bleibt starr“ ^[L541].
- Two limits stay open: „Hier existiert ein Restrisiko.“ ^[L549] and „Hier besteht ein Restrisiko für Bias in der automatisieren Evaluierung.“ ^[L562].
- **Observed:** the Falsifikations-Audit reports a study (L557) as the evidence for the hypothesis being falsified; the study is the source of that evidence, the verdict „Die Hypothese wurde massiv falsifiziert.“ ^[L557] is the document's.

## 7 · Claims about its own standing — recorded, never applied

- „Das NCP als Single Source of Truth ist nicht verhandelbar.“ ^[L462]; `Single Source of Truth` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#3] stands three times in the document.
- „Die Spec übersteigt die Qualität des Vorgängers massiv“ ^[L481].

## 8 · Absent, counted

The document names no chapter and no figure of any particular novel. `Kap` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#0] and `Kapitel` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#0] stand zero times; so do `Kael` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#0], `AEGIS` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#0], `Nexus` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#0] and `Guardians` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#0]. `Kohärenz` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] stands once, in the ordinary sense of L26.
