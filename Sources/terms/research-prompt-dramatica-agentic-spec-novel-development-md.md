---
source: Sources/drive/research-prompt-dramatica-agentic-spec-novel-development-md.md
drive_id: "1zqtFIKUakv5cIgPZUHzhPgEQ7Ndskpmqk1mPEsNVpxc"
title: "research-prompt_dramatica-agentic-spec-novel-development.md"
category: storyform
index_date: "2026-04-26"
extracted: "2026-10-12"
candidates: 57    # the terms capture.py counted
---

# Term census — research-prompt_dramatica-agentic-spec-novel-development.md

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py research-prompt-dramatica-agentic-spec-novel-development-md`

```
  lines                1738  (frontmatter ends at 9)
  body words           6735
  headings             32   bold-only lines 15
  table rows           13   code fences 0
  question marks       44
  backslash escapes    443
  typographic marks    158   ascii quotes 204
  invisible characters none
  math symbol lines    11
  glued ref numbers    40
  repeated labels      How to apply it — step by step x5, What it is x5, When to stop / escape criterion x5, Why it is in this prompt x5, Example trigger in this research context x4
  longest line         777 chars
```

## Stance, read per passage

**This is a research prompt, not a report.** It is addressed to an executing AI and asks for work to be done; everything it says about the future spec is a requirement, and nothing in it is a finding. It reports no result, names no figure, place or chapter of the novel, and gives no storyform value for any story. Passages, by lines:

The header block (L15 to L36) is a flattened list of fields: the export has run the frontmatter keys into one paragraph and escaped their underscores with a backslash. Its field `topic` asks for a „Spec-Driven Specification Artifact“ ^[L15] and its fields name the frameworks and constraint blocks the prompt then applies.

The address to the executing AI (L44): „Dieser Prompt ist selbsttragend“ ^[L44]. The same line says what is asked for as a deliverable.

The meta-header (L50 to L244) states three layers, and the first is a requirement list, not a report: it declares itself an exploration („Diese Recherche ist eine“ ^[L60]) and orders competing architecture hypotheses, backtracking and an accepted end state of unachievability (L196 to L220).

The ReAct passage (L246 to L352) is a procedure the AI is to follow: „Dieser Prompt verwendet das“ ^[L252] ReAct as its spine, with a loop of Reason, Act, Observe.

The DRACO passage (L354 to L768) defines five components D, R, A, C, O as obligations and ends with an instruction: „Honoriere jede Komponente als harten Vertrag“ ^[L768]. This is the prompt's own claim about its authority over the executing AI, and it is recorded here, applied to nothing.

The Research Objective (L778 to L828) is a list of seven things the spec must solve; its first item lists the theory layers the spec must cover (L788), and its opening line is „Entwickle eine vollständige, agentic-executable“ ^[L780].

The constraint blocks 0 to 5 (L832 to L959) are rules: a reflection baseline, source priority, temporal scope, output exclusions, ten spec-quality invariants in a table (L937 to L949), and the single-artifact mandate (L953). The exclusions say what the spec is not: „Die Spec ist ein Werkzeug, kein Roman“ ^[L924].

The five critical-thinking methods (L963 to L1130) each repeat the same labels: What it is, Why it is in this prompt, How to apply it, When to stop and Example trigger. These repeated labels are the template, not terms. Their example triggers are samples of what the AI might write, not statements about a story.

The DRACO sections (L1135 to L1560) hold templates: a decision-record template with `Status`, `Context`, `Options Considered`, `Decision`, `Consequences` (L1213 to L1257), the outline of the spec to be written (L1284 to L1516), and two expanded components. The outline carries bracketed placeholders in square brackets, which are fields to be filled by the AI, not text of a story.

The integrity check (L1566 to L1583), the delivery schema (L1589 to L1703) and the self-verification checklist (L1709 to L1729) are again requirements. The last line closes the prompt: „Ende des Research-Prompts“ ^[L1737].

## Candidates and counts

57 candidates, written while reading and frozen by the count (`Plan/runs/research-prompt-dramatica-agentic-spec-novel-development-md/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `research-prompt-dramatica-agentic-spec-novel-development-md.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `ReAct` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#4] | 4 | 7 | 23, 246, 248, 252, 256, 368, 772 | `ReAct-Framework` ×1, `ReAct-Zyklus` ×1, `ReAct-Spine` ×1 |
| `DRACO` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#9] | 9 | 28 | 23, 276, 324, 354, 356, 360, 368, 764, 772, 844, 856, 1010 … | `DRACO-A` ×7, `DRACO-Komponente` ×3, `DRACO-R` ×3, `DRACO-D` ×2 |
| `Decompose` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#4] | 4 | 4 | 24, 372, 772, 1137 | `decomposed` ×1 |
| `Reconcile` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#4] | 4 | 4 | 25, 428, 772, 1211 | `reconciled` ×1 |
| `Architect` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#4] | 4 | 11 | 26, 188, 464, 472, 772, 903, 1036, 1046, 1213, 1278, 1619 | `Architectural` ×4, `Architectures` ×2, `architectural` ×1, `Architecture` ×1 |
| `Contradiction-handling` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#4] | 4 | 4 | 27, 548, 772, 1522 |  |
| `Operationalize` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#4] | 4 | 4 | 28, 592, 772, 1542 |  |
| `Architectural Decision Record` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#2] | 2 | 4 | 188, 464, 1213, 1619 |  |
| `Reflection Baseline` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#3] | 3 | 3 | 31, 834, 1716 |  |
| `Adversarial Query Expansion` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#5] | 5 | 5 | 23, 308, 352, 1075, 1717 |  |
| `Pre-Mortem Analysis` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#2] | 2 | 2 | 20, 994 |  |
| `Red Team` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#5] | 5 | 5 | 21, 240, 905, 1021, 1719 |  |
| `First-Principles Decomposition` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#2] | 2 | 2 | 22, 1048 |  |
| `Falsification` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#5] | 5 | 6 | 19, 905, 967, 1253, 1679, 1719 | `Falsifications-Audit` ×1 |
| `Surviving-Branch Triangulation` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#4] | 4 | 4 | 29, 1174, 1647, 1718 |  |
| `Hypothesis Half-Life Audit` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#4] | 4 | 4 | 30, 1200, 1651, 1718 |  |
| `Pre-Synthesis Integrity Check` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#4] | 4 | 4 | 316, 847, 1125, 1724 |  |
| `Single-Artifact-Mandat` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#5] | 5 | 5 | 36, 794, 951, 1703 |  |
| `Methodology Appendix` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#3] | 3 | 3 | 1615, 1703, 1725 |  |
| `Spec-Quality-Invarianten` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#2] | 2 | 4 | 35, 931, 1578, 1721 | `Spec-Quality-Invarianten-Audit` ×2 |
| `Coherence-Invarianten` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#6] | 6 | 6 | 15, 480, 790, 943, 1508 |  |
| `Clarifying-Question-Protokoll` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#6] | 6 | 7 | 15, 524, 620, 756, 792, 945, 1552 | `Clarifying-Question-Protokolle` ×1 |
| `Clarifying-Question Protocol` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#1] | 1 | 1 | 1440 |  |
| `Phase-Transition-Contracts` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#5] | 5 | 5 | 604, 789, 946, 1046, 1548 |  |
| `Working-State-Schema` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#2] | 2 | 3 | 532, 756, 1556 | `Working-State-Schemas` ×1 |
| `Working-State Schema` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#1] | 1 | 1 | 1488 |  |
| `Phase-Definitions` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#3] | 3 | 3 | 476, 528, 1456 |  |
| `Choice-Space` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#1] | 1 | 2 | 504, 1376 | `Choice-Space-Schema` ×1 |
| `Interaction-Constraints` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#1] | 1 | 2 | 508, 1384 | `Interaction-Constraints-Schema` ×1 |
| `Failure-Modes Catalog` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#1] | 1 | 1 | 1496 |  |
| `Regression-Checks` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#2] | 2 | 2 | 544, 1504 |  |
| `Self-Verification Test Suite` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#1] | 1 | 1 | 1512 |  |
| `Query Expansion Log` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#5] | 5 | 5 | 44, 818, 1113, 1635, 1725 |  |
| `Contradiction Log` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#5] | 5 | 5 | 44, 818, 957, 1671, 1725 |  |
| `Reflection History` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#4] | 4 | 4 | 44, 818, 1627, 1725 |  |
| `Strukturelle Contradictions` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#3] | 3 | 3 | 560, 1424, 1528 |  |
| `Inhaltliche Contradictions` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#2] | 2 | 2 | 1428, 1532 |  |
| `Pragmatische Contradictions` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#3] | 3 | 3 | 572, 1432, 1536 |  |
| `BLOCKER` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#6] | 6 | 6 | 584, 791, 1412, 1528, 1532, 1536 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Dramatica` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#21] | 21 | 40 | 15, 24, 29, 42, 64, 208, 380, 436, 452, 500, 692, 780 … | `Dramatica-Theorie` ×5, `Dramatica-Primärquellen` ×3, `Dramatica-basierte` ×2, `Dramatica-Schichten` ×2 |
| `Story Mind` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#2] | 2 | 2 | 452, 788 |  |
| `Throughlines` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#5] | 5 | 5 | 560, 788, 1388, 1528 |  |
| `Concerns` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#2] | 2 | 2 | 788, 1388 |  |
| `Quad-Modell` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#1] | 1 | 1 | 788 |  |
| `Story Driver` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#1] | 1 | 1 | 788 |  |
| `Story Limit` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#1] | 1 | 1 | 788 |  |
| `Story Outcome` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#2] | 2 | 2 | 788, 1054 |  |
| `Story Judgment` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#1] | 1 | 1 | 788 |  |
| `Story Goal` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#7] | 7 | 7 | 576, 788, 1019, 1105, 1536 |  |
| `Grand Argument` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#2] | 2 | 2 | 788, 1536 |  |
| `Author's Audience` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#1] | 1 | 1 | 788 |  |
| `Author's Argument` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#1] | 1 | 1 | 788 |  |
| `Plot Sequencing` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#1] | 1 | 1 | 788 |  |
| `Story Logic` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#1] | 1 | 1 | 788 |  |
| `Story Feeling` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#1] | 1 | 1 | 788 |  |
| `Signposts` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#2] | 2 | 2 | 788, 1073 |  |
| `Journeys` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#2] | 2 | 2 | 788, 1073 |  |

## What the extraction ran into

**Zeros:** 0.

**Standing alone less often than with compounds:** 11 — `ReAct` 4/7, `DRACO` 9/28, `Architect` 4/11, `Architectural Decision Record` 2/4, `Falsification` 5/6, `Spec-Quality-Invarianten` 2/4, `Clarifying-Question-Protokoll` 6/7, `Working-State-Schema` 2/3, `Choice-Space` 1/2, `Interaction-Constraints` 1/2, `Dramatica` 21/40.

Standing: no candidate counts zero, so no inflection or export damage hides a listed term. Each gap between the standing-alone and the compound count is a hyphenated or inflected compound the table lists under its surfaces (for example `DRACO-A` and `Dramatica-Theorie`); `Architect` also stands inside `Architectural` and `Architectures`, which is the substring the count marks.

**What the document lacks, counted.** It writes no chapter: `Kap` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#0] and `Kapitel` ^[research-prompt-dramatica-agentic-spec-novel-development-md.md:#0] both stand 0 times, and a list of numbered items in it (L1265 to L1272) numbers architecture conflict axes for the spec, not chapters. It names no figure, place or object of the novel, and gives no Dramatica storyform value for any story: the Dramatica words it writes are the theory's layers, listed as a requirement (L788) and used in generic examples such as „zwei Throughlines auf“ ^[L560]. The candidates under the lens heading are exactly these borrowed layers. The prompt excludes narrative content itself: „Die Spec ist ein Werkzeug, kein Roman“ ^[L924].

**Repeated labels.** The profile's five repeated labels (How to apply it, What it is, When to stop / escape criterion, Why it is in this prompt, Example trigger) are the methods' template and are not listed as candidates.

**Export damage.** The profile counts 443 backslash escapes: the export escapes asterisks and hash signs, so bold headings read `\*\*...\*\*` and markdown headings inside the prompt read `\#\#`; the frontmatter keys are run together into one paragraph with their underscores escaped (L15, L23). Quotations in the note stop before such markup. Many lines are separated by blank lines, so a sentence wraps over several file lines (for example L60 to L84), and a quotation can only cover the fragment on one line. The profile counts 40 glued reference numbers; I did not trace each of them, and the one line I looked at (L1270) holds a technology name, not a footnote.

**Wrapped and hyphen-split terms.** Some phrases wrap across lines, such as a hyphenated compound broken at the end of a line (L120 to L124); the whole form stands on no single line, and none of these is a candidate.

**Spelling variants the document writes both ways.** The spec section is headed „Clarifying-Question Protocol“ ^[L1440] while the requirement list writes the German-hyphenated `Clarifying-Question-Protokoll`; likewise `Working-State Schema` and `Working-State-Schema`. Both forms are listed as written, and the census does not decide that they name one thing.

**The document's own standing.** It calls itself self-contained („Dieser Prompt ist selbsttragend“ ^[L44]) and binds the executing AI by contract (L768 above). These are claims about the prompt, recorded and applied to nothing.
