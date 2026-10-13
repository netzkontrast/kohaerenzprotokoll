---
source: Sources/drive/archon-ai-narrative-coherence-framework.md
read: "2026-10-12, the whole document (L1 to L336) through read.py with line numbers; by a document-reader subagent (Sonnet)"
stance_markers: ["proposed", "case study"]
stance_marker_count: 11
reads_as: "an English-language analytic report on a proposed AI framework for narrative coherence in general, whose section V proposes the novel as a test case"
---

# Note — ARCHON: AI Narrative Coherence Framework

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document speaks as a report on a proposed framework, and about the novel only as a proposed test.

## 1 · What kind of text this is, and how it marks itself

- The document names its own genre: „This report provides a comprehensive analysis“ ^[L24] of ARCHON, which it calls „a proposed solution“ ^[L24].
- Its conclusion names the source it reports on: „as outlined in the research proposal“ ^[L268]. `proposed` ^[archon-ai-narrative-coherence-framework.md:#5] and `case study` ^[archon-ai-narrative-coherence-framework.md:#6] are the labels that stand for its status.
- **Observed:** this is a document about AI narrative tools in general. Sections I to IV and VI to VII (L18 to L176, L220 to L270) never name the novel Kohärenz Protokoll; only section V (L184 to L216) does. `Kohärenz Protokoll` ^[archon-ai-narrative-coherence-framework.md:#2] stands twice (L184, L212).
- It claims for itself: „represents a paradigm shift“ ^[L270]. This is the document's own claim about its standing, recorded and not applied.
- **Observed:** 63 reference entries follow the heading `Referenzen` ^[archon-ai-narrative-coherence-framework.md:#1], each with the label `Zugriff am` ^[archon-ai-narrative-coherence-framework.md:#63].

## 2 · The framework's terms (the document's own)

- The document spells out the name as „Agentic Reasoning & Coherent Hypergraph Orchestration for Narratives“ ^[L24]; `ARCHON` ^[archon-ai-narrative-coherence-framework.md:#36] stands 36 times.
- It names three pillars, of which the first is „A formal, computable model of authorial intent derived from Dramatica narrative theory“ ^[L26].
- The NCP is introduced as „an open, standardized, application-agnostic JSON schema“ ^[L109]; `NCP` ^[archon-ai-narrative-coherence-framework.md:#16] stands 16 times, `Narrative Context Protocol` ^[archon-ai-narrative-coherence-framework.md:#5] five.
- The document says what the NCP standardizes and what it leaves out: „not its creative expression or“ ^[L111].
- The memory is „a hierarchical Knowledge Hypergraph“ ^[L27]; the document later also writes `Narrative Hypergraph` ^[archon-ai-narrative-coherence-framework.md:#3], and the table writes „Hierarchical Knowledge Hypergraph (Facts + Themes)“ ^[L256].
- It organises the hypergraph in „a four-level hierarchy“ ^[L141]; the four layers are `The Source Layer` ^[archon-ai-narrative-coherence-framework.md:#1], `The Factual Layer` ^[archon-ai-narrative-coherence-framework.md:#1], `The Thematic Layer` ^[archon-ai-narrative-coherence-framework.md:#1] and `The Global Summary Layer` ^[archon-ai-narrative-coherence-framework.md:#1] (L143 to L146).
- The agent is „the Narrative Director, an autonomous agent built upon the ReAct“ ^[L154] pattern; `Narrative Director` ^[archon-ai-narrative-coherence-framework.md:#6] stands six times.
- Its critique step is „a separate, secondary LLM call dedicated to critique“ ^[L162], run by the `Self-Reflection Module` ^[archon-ai-narrative-coherence-framework.md:#1].
- The document says the critique is „not a subjective assessment of quality“ ^[L162], and that a failing output „is discarded“ ^[L162].
- Context management rests on `thematic resonance` ^[archon-ai-narrative-coherence-framework.md:#2], described as „a highly specialized form of Retrieval-Augmented Generation“ ^[L170].

## 3 · The case study — where the novel enters

- The proposal is conditional: the framework „is proposed to be tested against“ a case study ^[L184].
- The document gives the basis of the test: the world-building „incorporates metaphysical rules derived from computational complexity theory“ ^[L212] (of `Kohärenz Protokoll`, written without markup).
- The protagonist is introduced as „The protagonist of the case study“ ^[L192], characterised by `Dissociative Identity Disorder` ^[archon-ai-narrative-coherence-framework.md:#1] and modeled, in the document's words, on `Theory of Structural Dissociation` ^[archon-ai-narrative-coherence-framework.md:#2]. The document does not give the protagonist a name (`Kael` ^[archon-ai-narrative-coherence-framework.md:#0]).
- The part names are the theory's, which the document reports: `Apparently Normal Parts` ^[archon-ai-narrative-coherence-framework.md:#1] and `Emotional Parts` ^[archon-ai-narrative-coherence-framework.md:#1] (L192); the multiple states are written `Alters` ^[archon-ai-narrative-coherence-framework.md:#1] (L194).
- The antagonist: „The antagonist of the case study is an AI, AEGIS“ ^[L202] (`AEGIS` ^[archon-ai-narrative-coherence-framework.md:#2]). The document proposes that the NCP encode its motivation as a formal process and its failure through a `Gödel statement` ^[archon-ai-narrative-coherence-framework.md:#1] (L204); this is a modelling proposal for the framework, not a statement about the novel's text.
- World rules: „the fictional“ `Core Worlds` ^[archon-ai-narrative-coherence-framework.md:#1] ^[L214]. The document gives an example rule only as an illustration of what could be stored: „magical rituals are NP-complete problems“ ^[L214].
- The three pillars are called „a profound meta-test“ ^[L216], and the document ends the section with a question: „can a system for creating order successfully narrate stories about the breakdown of order“ ^[L216].

## 4 · Borrowed concepts the document applies

- Dramatica is reported as the basis: its „Story Mind“ analogy is introduced in a heading ^[L82]; the four throughlines are a bulleted list, each opening with its label, e.g. „Overall Story (OS) Throughline“ ^[L96]. `Dramatica` ^[archon-ai-narrative-coherence-framework.md:#27] stands 27 times.
- The document reports the critics of Dramatica and answers them: „Common critiques center on its perceived rigidity“ ^[L119].
- `ReAct` ^[archon-ai-narrative-coherence-framework.md:#3] is cited as the planning pattern of the agent (L154), with its references at L315 and L316.

## 5 · The comparison with other tools

- The document says of the current state: „The dominant paradigm for AI in creative writing is that of an assistant“ ^[L232].
- It describes `Sudowrite` ^[archon-ai-narrative-coherence-framework.md:#7] with a „Story Bible“ feature ^[L234] and `Novelcrafter` ^[archon-ai-narrative-coherence-framework.md:#5] as centred on the Codex, „an internal wiki or story bible“ ^[L235]. These are reports about commercial tools, not about the novel's world.
- ARCHON's role is stated as a shift „from a passive assistant to an active collaborator“ ^[L243].

## 6 · Said two ways, or left open — recorded, not resolved

- The document describes the case study in the future-conditional ( „Successfully modeling TSDP would demonstrate“ ^[L194] ), so no passage reports a result of the test.

## 7 · Absent, counted

- The protagonist's name is not written: `Kael` ^[archon-ai-narrative-coherence-framework.md:#0].
- The document has no test result: the case study stands `proposed` ^[archon-ai-narrative-coherence-framework.md:#5] throughout.
