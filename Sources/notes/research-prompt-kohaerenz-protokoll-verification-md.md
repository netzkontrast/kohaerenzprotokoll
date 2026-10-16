---
source: Sources/drive/research-prompt-kohaerenz-protokoll-verification-md.md
read: "2026-10-16, the whole document (L1 to L1428) through read.py with line numbers; a document-reader subagent (Sonnet)"
stance_markers: ["The framework claims", "Reason", "Observe"]
stance_marker_count: 70
reads_as: "a research prompt in English with a German title: a plan for an agent that audits a narrative framework against published sources; the world's names occur only inside the claims it says the framework makes"
---

# Note — research-prompt_kohaerenz-protokoll-verification.md

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible and the claim rests on the lines or counts it names. The document is an instruction, not a narrative: it tells an agent what to verify and what to leave alone, and it reports the framework's claims rather than making them.

## 1 · What kind of text this is, and how it marks itself

- It describes itself as layered: „This research prompt uses“ ^[L34] three layers, an epistemological one, an agentic spine and a structural one.
- It calls the task an extraction: „This research is an extraction, not an exploration.“ ^[L175]
- **Observed:** the plan's steps use the labels `Reason` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#28] and `Observe` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#26], and the framework's claims are introduced by `The framework claims` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#16]. The three sum to the stance_marker_count in the frontmatter.
- It states its own standing as a tool: „This prompt is ready for autonomous research execution.“ ^[L1421] That is the document's claim about itself and decides nothing here.

## 2 · What the audit excludes

- It rules the story out of scope: „Narrative application is the writer's responsibility; your task is framework verification.“ ^[L135]
- It forbids assuming the framework's own vocabulary is published: „Assume framework-internal terminology“ ^[L1273] is a Do NOT item, and its example is the substrate name in section 3.

## 3 · The world's names, as the document reports them

The prompt reports the framework's claims in „Reason“ lines; the speaker of each claim is the framework, which the prompt introduces with `The framework claims`.

- AEGIS: the framework is reported as claiming that „AEGIS is not destroyed but enters a state of permanent, broken paradox“ ^[L1078], and the example trigger sets one axis against another with „AEGIS seeks coherence, which is K“ ^[L342]. The document counts `AEGIS` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#5] times.
- Kael: named in the reported claim „verify the energy source for Kael's self-repair mechanisms“ ^[L656] and in the exclusion at ^[L125]. `Kael` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#3].
- Juna: the input list gives „Juna as observational lens“ ^[L538] and the reported claim of an orbifold mechanism „for Juna's observation“ ^[L875]. `Juna` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#3].
- The four alters: the document names them in a step heading: „Verify applicability to the framework's Alter system (Lex, Nyx, Kiko, Lia)“ ^[L724]; the reported claim is that they act as „discrete functional modules“ ^[L728].
- The substrate: the framework is reported as applying its two kernels, described as „(coherence/erasure kernels)“ ^[L625], to a server substrate that the line names `Mnemosyne-Archipel`. `Mnemosyne-Archipel` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#3] stands in this line, in a search string and in the Do NOT list.
- The foundational phone call: the reported claim treats „The Silence of the foundational phone call must be treated as a high-density informational bedrock“ ^[L1104] as a kernel substrate (step heading at ^[L1100]).
- The world and the chapters: **Observed:** the document writes `Kap` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#0] times and `Kapitel` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#0] times; its one mention of chapters is the English plural `chapters` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] time, inside the reported claim about the reader's effort ^[L990]. No world code appears.

## 4 · The theories the framework is reported to rest on

- The input list assigns the framework's axes to theories: „Axis VII & VIII: Participatory Universe and The Witness Function“ ^[L538].
- Dual-Kernel Theory is questioned as to its origin: „Is DKT an established framework with published papers, or is it the framework's own synthesis?“ ^[L640]. If it is novel, the instruction is to log it: „If DKT is novel, note this in the Contradiction Log“ ^[L644].
- For several mathematical or psychological mechanisms the prompt asks whether they are literal or figurative: „Is this a valid mathematical mechanism, or is the framework using mathematical language metaphorically?“ ^[L889] and „Is this grounded in AI theory or computer science, or is it poetic language?“ ^[L1092].
- It requires a division of what is established from what is novel: „Distinguish "established theory" from "novel author synthesis."“ is a Do item at ^[L1283].

## 5 · Said two ways, or left open — recorded, not resolved

- **Observed:** the prompt speaks of seven axes (`7 axes` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#7] times, `seven axes` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#3] times) while its input list heads the groups Axis I, II, III & IV, V & VI and VII & VIII (L534 to L538). It does not say how the numerals up to VIII make seven; the document leaves the numbering open.
- It defines Contradiction Log as a running record: „Every contradiction enters the final Contradiction Log, not a silent note.“ ^[L167] The term stands `Contradiction Log` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#16] times.
- The document makes no statement about the framework's canon status; it only calls itself ready to run (see section 1).

## 6 · Absent, counted

- **Observed:** no chapter is named by `Kap` or `Kapitel` (counts in section 3); the document defines no world code.
- The document also names real thinkers and a real field of clinical research as the sources to verify; that material is not harvested here.
