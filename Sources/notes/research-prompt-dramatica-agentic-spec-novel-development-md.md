---
source: Sources/drive/research-prompt-dramatica-agentic-spec-novel-development-md.md
read: "2026-10-12, the whole document (L1 to L1737) through read.py with line numbers; by a document-reader subagent (Sonnet)"
stance_markers: ["What it is", "Why it is in this prompt", "How to apply it — step by step", "When to stop / escape criterion", "Example trigger in this research context"]
stance_marker_count: 24
reads_as: "a research prompt addressed to an executing AI: requirements, templates and methods for a specification to be written, with no findings and no story content"
---

# Note — research-prompt_dramatica-agentic-spec-novel-development.md

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document is a prompt: it asks, it does not report, so each sentence below records what is asked, not what is true.

## 1 · What kind of text this is, and how it marks itself

- The document addresses an executing AI and calls itself complete: „Dieser Prompt ist selbsttragend“ ^[L44]
- It asks for one deliverable, a specification: „Entwickle eine vollständige, agentic-executable“ ^[L780]
- It sets the specification apart from a story: „Die Spec ist ein Werkzeug, kein Roman“ ^[L924]
- **Observed:** the five labels `What it is` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#5], `Why it is in this prompt` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#5], `How to apply it — step by step` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#5], `When to stop / escape criterion` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#5] and `Example trigger in this research context` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#4] repeat as the template of the critical-thinking methods (L963 to L1130). They are the template, not terms of a story world.
- **Observed:** the header block (L15 to L36) is the prompt's own metadata flattened by the export into one paragraph with escaped underscores.

## 2 · The frameworks it applies to the executing AI

- It uses ReAct as its agentic spine: „Dieser Prompt verwendet das“ ^[L252]
- It builds a structural layer called DRACO with five components, Decompose, Reconcile, Architect, Contradiction-handling and Operationalize (L372 to L592). It binds the AI to them: „Honoriere jede Komponente als harten Vertrag“ ^[L768]
- The component Architect is named the main artifact: „Das ist das Hauptartefakt dieses Prompts“ ^[L480]
- Decisions are to be recorded as ADRs; the minimum is set: „Acht ADRs“ ^[L1261]

## 3 · What the specification must contain

- The prompt lists the Dramatica layers the spec must map, among them the story points named in L788: `Story Mind` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#2], `Story Goal` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#7] and `Grand Argument` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#2]. The list itself stands on one line: „vier Throughlines mit Domain-Permutation“ ^[L788]
- The number of throughline mentions across the document: `Throughlines` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#5]. A generic example it gives: „zwei Throughlines auf“ ^[L1528]
- Coherence invariants are demanded with a minimum: „Mindestens fünf Coherence-Invarianten“ ^[L943]
- Three contradiction classes are named: `Strukturelle Contradictions` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#3], `Inhaltliche Contradictions` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#2] and `Pragmatische Contradictions` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#3]. Severity is graded: „Schweregrad-Klassifikation“ ^[L584]
- The contradiction-handling component demands explicit mechanisms, set off by dashes: „keine Hoffnung“ ^[L552]
- The single-file requirement can be escaped if impossible: „Falls sich erweist, dass das Single-Artifact-Mandat“ ^[L794]. The term `Single-Artifact-Mandat` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#5] recurs in the constraint blocks.
- Style: „Die Spec ist deklarativ und präzise“ ^[L806]

## 4 · The sources it names for the executing AI

- It ranks primary sources for the theory: „Primärquellen Dramatica“ ^[L897]. The sources include a website named in the same line.
- It limits the time window of the theory's sources: „Dramatica-Primärquellen“ ^[L826]
- It gives the agentic-practice literature precedence over classical specification practice: „die agentic-Praxis-Literatur hat Vorrang“ ^[L905]

## 5 · Said two ways, or left open — recorded, not resolved

- The spec section is headed „Clarifying-Question Protocol“ ^[L1440] but the requirement list writes `Clarifying-Question-Protokoll` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#6]. The document does not say whether they are one thing.
- **Observed:** the document uses `Working-State-Schema` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#2] and `Working-State Schema` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#1] in the same way.
- The prompt allows that the whole request may be unachievable: „Akzeptiere“ ^[L196]

## 6 · Absent, counted

- The prompt names no chapter: `Kap` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#0] and `Kapitel` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#0].
- It names none of the novel's figures that were asked about: `Kael` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#0] and `AEGIS` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#0].
- It gives no storyform value for any story. Its Dramatica words are the theory's layers in a requirement list (L788) and in generic examples, as in the contradiction example about a story goal (L1536).
- The document excludes story content itself: „Anwendung auf spezifische Schreibprojekte“ ^[L925]
