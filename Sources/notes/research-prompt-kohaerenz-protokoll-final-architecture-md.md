---
source: Sources/drive/research-prompt-kohaerenz-protokoll-final-architecture-md.md
read: "2026-10-16, the whole document (L1 to L936) through read.py with line numbers; by a document-reader subagent (Sonnet)"
stance_markers: ["Abort criterion", "Pass condition", "Fail condition", "Example seed questions"]
stance_marker_count: 30
reads_as: "a self-contained research prompt for an autonomous research agent: context, role, hard constraint blocks, research axes, execution steps and an output schema, with the novel's architecture as its subject"
---

# Note — research-prompt_kohaerenz-protokoll-final-architecture.md

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document is an instruction addressed to a research agent, not a narrative: its statements about the novel's world are the prompt's own description of the project, and its statements about earlier material are reports of that material.

The stance markers stand `Abort criterion` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#17] times, `Pass condition` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#3] times, `Fail condition` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#3] times and `Example seed questions` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#7] times, which sum to 30.

## 1 · What kind of text this is, and how it marks itself

- The document describes itself as one that „assumes you have no prior knowledge of the project“ ^[L52], and it asks that an undefined term be treated as „a prompt defect“ ^[L52].
- It names the work as „a long-form novel project“ ^[L113], „planned at roughly 39 chapters across three acts“ ^[L113]. It writes no `Kap` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#0] and no `Kapitel` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#0]; the English word appears twice (`chapters` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#2]), and there is no chapter-by-chapter outline.
- Its own labels mark what a passage does: a step ends with an abort criterion, a gate has a pass and a fail condition, and the axes carry seed questions. Section 6 calls its example questions „seeds for adversarial query expansion“ ^[L378].
- **Observed:** the frontmatter (L11 to L44) is a flattened list of the prompt's own metadata; the export has escaped underscores and joined several fields on single lines.
- **Observed:** the document also holds a section of confidential material about the work's private origin (Section 1.4, L137 to L153) and two constraint blocks that fence it off (Blocks 4 and 5). It is personal material and is not harvested here.

## 2 · AEGIS

- The document expands the name as „Autonomous Entropic Gatekeeper for Integrity Systems“ ^[L126].
- It calls AEGIS „a tragic god“ ^[L126] and says it is not „the antagonist in a moral sense“ ^[L126].
- It describes AEGIS as „a structure that emerged to preserve the protagonist“ ^[L126].
- Storyform B is „the functional tragedy of AEGIS attempting to maintain the simulation“ ^[L132].
- The Moonshine-Link is said to leave AEGIS „ontologically blind to it“ ^[L427].
- The document reports a rotation the existing material has: „AEGIS = K₁, Kael's EPs = K₀“ ^[L393], and asks what follows if that is wrong.

## 3 · Kael

- Kael is „the Main Character“ ^[L127].
- The document glosses TSDP as „a clinical model in which the personality is divided into Apparently Normal Parts that handle daily life and Emotional Parts that hold trauma“ ^[L127]. This is a gloss of a borrowed model, given as part of the project's description.
- Storyform A is „the phenomenological journey of Kael toward functional multiplicity“ ^[L131].
- The document names the lived loops „the dissociative loops of return-and-suffer“ ^[L133] and says they are revealed to have preserved „mutual information across trauma“ ^[L133].
- Axis 5 names a possible Witness in a storyform: „Kael's emergent multiplicity (Kael/M)“ ^[L450]. `Kael/M` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#1] stands once and is not defined elsewhere.

## 4 · Juna

- Juna is an entity who „operates outside AEGIS's perceptual range“ ^[L128], linked by a non-local Moonshine-Link.
- The document reports that the existing material has described Juna in several ways, and describes the ontological status as „deliberately unsettled“ ^[L128] for this run.
- Gate 2 asks whether Juna is the Influence Character in both storyforms, in one, or in „a fifth structural position“ ^[L282].
- Candidate ontologies are listed (L491 to L496). Among them: „Juna is the IC in both storyforms“ ^[L491]; „Juna is *outside* both storyforms“ ^[L492]; „intentionally unmodelable“ ^[L493]; „Juna is the diegetic stand-in for the Reader's substrate-function“ ^[L495]; and „some layered combination of the above“ ^[L496].
- Axis 8 is described as „The deliberately unresolved axis“ ^[L483]; elsewhere the document says the research must produce a defensible verdict (L500). `Juna` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#22] stands 22 times.

## 5 · The kernels and the physics

- Dual-Kernel Theory „serves as the in-world physics“ ^[L125] and says „Reality is constituted by two computational substrates“ ^[L125].
- K₁ is the Coherence Kernel, K₀ the Collapse / Erasure Kernel (L125); the document writes the subscripted forms, `K₁` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#20] and `K₀` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#17] standing alone.
- The Vortex Inversion is „The central narrative move“ ^[L133]: „at the climax, the two storyforms invert“ ^[L133]. The document requires that it be „expressible as a specific moment in the plot“ ^[L273]. `Vortex Inversion` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#17] stands 17 times.
- The Moonshine-Link is a connection modeled on Quantum Entanglement and described as „a direct, intuitive grasping“ ^[L128].

## 6 · The Witness Function and the Reader

- The Witness Function has three layers (L282, L441): `Quantum Entanglement Witness` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#2], `Cryptographic Zero-Knowledge Verifier` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#2] and `Phenomenological Disinterested Spectator` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#2].
- Who the Witness is stays a question in the document: „Who or what is the Witness in each storyform?“ ^[L450]
- The Reader as Substrate: „The reader holds the paradox; the reader is the fifth dimension“ ^[L135].
- Gate 3 requires: „the reader experiences the inversion, not merely reads about it“ ^[L291], and names possible mechanisms such as „contradictory footnotes, multiple mutually exclusive epilogues“ ^[L291].

## 7 · Truth theories and the rotation

- The conflict is „literalized as a war“ between two theories of truth ^[L134]; the document says the existing material „maps K₁ to Coherence and K₀ to Correspondence Check“ ^[L134] and that the rotation must be tested „explicitly“ ^[L134].
- The worked example inverts the mapping: „Inversion Superior“ ^[L888] with respect to the Vortex Inversion, with the canonical mapping kept as „the first-act surface“ ^[L888].
- The example states the cascade: „AEGIS migrates from K₁ to K₀ across the work“ ^[L892] and „Kael migrates from K₀ to K₁“ ^[L892].
- The example names a unit: „Each return is a Coheron“ ^[L880]; `Coheron` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#1] stands once.

## 8 · The German terms

- The document asks for German that is „not a translation“ ^[L243] but „a cultural-tonal mirror“ ^[L243], and names the terms to prefer in L908 to L915: `Risse` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#2], `Nichts-Rauschen` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#2], `Algorithmische Melancholie` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#2], `Funktionale Multiplizität` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#1], `Zeuge-Funktion` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#1], `Mosaik-Herz` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#1] and `Wahrheits-Vortex` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#1].
- The last of these is offered as „a candidate German term for the Vortex Inversion at the truth-theory level“ ^[L915].

## 9 · Said two ways, or left open — recorded, not resolved

- The Foundation and the Sea of Potentiality are called „existing in-world entities outside AEGIS's domain“ ^[L788] and are to be placed by the synthesis. `Foundation` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#1] and `Sea of Potentiality` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#1] stand once each, in the output schema, and are not described elsewhere.
- **Observed:** The status of Juna is both held open (L128, L483) and required to be decided (L500); the document does not reconcile the two.
- The document's statement of its own standing: „This run produces canon.“ ^[L319]. This is recorded as the document's claim about itself and decides nothing here. It places the run against a standing principle that concepts only „name what already exists in the story“ ^[L157], which it says is suspended for this pass ^[L157].

## 10 · Absent, counted

- The document writes no `Kap` ^[research-prompt-kohaerenz-protokoll-final-architecture-md.md:#0]; no chapter is named or outlined.
- Section 1.4 holds personal material of a kind not harvested here; the note records only that it exists.
