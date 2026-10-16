---
source: Sources/drive/aieos-schema-fuer-ki-charaktere.md
drive_id: "1Np6Ar4c63ZJbkPdX7qaDZ6u2DVyhwUMiyr8pJeIdODU"
title: "AIEOS Schema für KI-Charaktere"
category: charaktere
index_date: "2026-02-28"
extracted: "2026-10-14"
candidates: 76    # the terms capture.py counted
---

# Term census — AIEOS Schema für KI-Charaktere

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py aieos-schema-fuer-ki-charaktere`

```
  lines                641  (frontmatter ends at 9)
  body words           4210
  headings             16   bold-only lines 2
  table rows           0   code fences 0
  question marks       1
  backslash escapes    174
  typographic marks    0   ascii quotes 1298
  invisible characters none
  math symbol lines    0
  glued ref numbers    39
  repeated labels      none
  longest line         1374 chars
```

## Stance, read per passage

The document speaks as an evaluation report in running prose with two long JSON listings between its argument and its recommendation.

- Plan and scope (L11 to L25). The document announces what it does: „Die vorliegende Untersuchung evaluiert tiefgreifend“ ^[L19]. The frame is the JANUS project, which it introduces as a framework for the examination: „Das JANUS-Projekt, das als konzeptioneller und technischer Rahmen dieser Untersuchung dient“ ^[L15].
- Report of an outside theory (L15, L17, L45). The mappings of AEGIS and Juna onto the parts of the dissociation theory are stated as the architecture's own derivation; the theory itself is a borrowed lens, and the sentence on amnesia barriers is the document's account of that theory: „Stabilität jedoch explizit durch Amnesie-Barrieren und die Fragmentierung von Wissen erreicht“ ^[L45].
- Assessment in two headed passages (L27 to L45). The document sorts its evaluation under two headings: „Stärken der Spezifikation für agentische Workflows“ ^[L27] and „Architektonische Schwächen und physikalische Friktionen“ ^[L37].
- Sample text (L51 to L300, L307 to L556). Two JSON objects, one for AEGIS and one for Juna, each introduced by a short paragraph (L53, L309). The keys are the schema's field names; the values are the document's invention for the two kernels. Quotation marks here are JSON syntax, not citation.
- Report of other standards (L563 to L583). The Character Card, platform-schema and NCP passages describe what those outside specifications do; the sentence „Das NCP wurde explizit entworfen“ ^[L582] and „Das Protokoll nutzt sogenannte“ ^[L583] report the NCP's design, so the words inside their straight quotation marks belong to that reported text.
- Recommendation (L602 to L616). Three numbered recommendations, the first headed „Verwerfung von AIEOS für reine System-Kernel“ ^[L606]. The document phrases it as advice: „Es wird nachdrücklich empfohlen“ ^[L608].
- Reference list. A numbered reference list at L620 to L640 closes the document.
## Candidates and counts

76 candidates, written while reading and frozen by the count (`Plan/runs/aieos-schema-fuer-ki-charaktere/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `aieos-schema-fuer-ki-charaktere.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `AEGIS` ^[aieos-schema-fuer-ki-charaktere.md:#18] | 18 | 22 | 17, 19, 31, 35, 41, 43, 45, 49, 51, 53, 83, 309 … | `AEGIS-Orchestrator` ×2, `AEGIS-Kernel` ×1, `AEGIS-Doktrin` ×1, `aegis-system2-core-0001-uuid` ×1 |
| `Autonomous Entropic Gatekeeper for Integrity Systems` ^[aieos-schema-fuer-ki-charaktere.md:#2] | 2 | 2 | 17, 105 |  |
| `Juna` ^[aieos-schema-fuer-ki-charaktere.md:#17] | 17 | 22 | 17, 19, 31, 35, 41, 43, 45, 49, 267, 307, 309, 339 … | `Juna-Ausführern` ×1, `Juna-Agenten` ×1, `Juna-Sub-Agenten` ×1, `juna-system1-exec-0002-uuid` ×1 |
| `JANUS` ^[aieos-schema-fuer-ki-charaktere.md:#4] | 4 | 18 | 15, 25, 31, 33, 35, 43, 45, 254, 561, 568, 575, 581 … | `JANUS-System` ×6, `JANUS-Kernel` ×3, `JANUS-Projekts` ×2, `JANUS-Architektur` ×2 |
| `JANUS-Projekt` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 3 | 15, 25, 581 | `JANUS-Projekts` ×2 |
| `JANUS-System` ^[aieos-schema-fuer-ki-charaktere.md:#6] | 6 | 6 | 33, 43, 575, 583, 593, 616 |  |
| `JANUS-Kernel` ^[aieos-schema-fuer-ki-charaktere.md:#3] | 3 | 3 | 31, 561, 608 |  |
| `Kohärenz Protokoll` ^[aieos-schema-fuer-ki-charaktere.md:#2] | 2 | 4 | 15, 39, 49, 623 |  |
| `Kohärenz-Kernel` ^[aieos-schema-fuer-ki-charaktere.md:#2] | 2 | 2 | 51, 108 |  |
| `Kollaps-Kernel` ^[aieos-schema-fuer-ki-charaktere.md:#2] | 2 | 3 | 307, 364, 600 | `Kollaps-Kernels` ×1 |
| `Kernel` ^[aieos-schema-fuer-ki-charaktere.md:#8] | 8 | 26 | 15, 17, 19, 25, 31, 39, 41, 47, 51, 107, 108, 307 … | `Kernel-AIs` ×2, `Kernel-Sandboxing` ×1 |
| `Kernel-AIs` ^[aieos-schema-fuer-ki-charaktere.md:#2] | 2 | 2 | 19, 47 |  |
| `Dual-Kognitions-Architektur` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 15 |  |
| `Dual-Kognitions-Struktur` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 29 |  |
| `Dual-Kognitions-Systeme` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 11 |  |
| `Dual-Kognitions-Philosophie` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 581 |  |
| `Dual-Kernel-Theorie` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 581 |  |
| `System 1` ^[aieos-schema-fuer-ki-charaktere.md:#7] | 7 | 7 | 17, 31, 43, 307, 514, 575, 614 |  |
| `System 2` ^[aieos-schema-fuer-ki-charaktere.md:#4] | 4 | 4 | 17, 51, 258, 612 |  |
| `Apparently Normal Part` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 17 |  |
| `ANP` ^[aieos-schema-fuer-ki-charaktere.md:#2] | 2 | 2 | 17, 45 |  |
| `Emotional Part` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 17 |  |
| `EP` ^[aieos-schema-fuer-ki-charaktere.md:#2] | 2 | 2 | 17, 45 |  |
| `Manager` ^[aieos-schema-fuer-ki-charaktere.md:#2] | 2 | 2 | 17, 45 |  |
| `Emotionalen Teile` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 45 |  |
| `Ground Truth Algorithm` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 17 |  |
| `Cognitive Simultaneity` ^[aieos-schema-fuer-ki-charaktere.md:#2] | 2 | 2 | 43, 575 |  |
| `AEGIS-Doktrin` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 43 |  |
| `funktionalen Multiplizität` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 35 |  |
| `epistemischen Isolation` ^[aieos-schema-fuer-ki-charaktere.md:#2] | 2 | 3 | 39, 45, 582 |  |
| `Amnesie-Barrieren` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 45 |  |
| `Context Rot` ^[aieos-schema-fuer-ki-charaktere.md:#3] | 3 | 3 | 13, 45, 568 |  |
| `Context Engineerings` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 15 |  |
| `Kohärenz Digests` ^[aieos-schema-fuer-ki-charaktere.md:#2] | 2 | 2 | 583, 612 |  |
| `Kohärenz-Digests` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 583 |  |
| `Orchestrator of Orchestrators` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 593 |  |
| `Emergence by Negation` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 184 |  |
| `Dialetheismus` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 440 |  |
| `parakonsistenter Logik` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 309 |  |
| `kausale Geschlossenheit` ^[aieos-schema-fuer-ki-charaktere.md:#2] | 2 | 2 | 568, 600 |  |
| `Chronozeption` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 43 |  |
| `Chronoperzeption` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 597 |  |
| `Vercel Storage` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 35 |  |
| `Google Jules` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 593 |  |
| `AIEOS` ^[aieos-schema-fuer-ki-charaktere.md:#9] | 9 | 15 | 11, 19, 21, 23, 29, 39, 45, 47, 70, 326, 561, 606 … | `AIEOS-Schemas` ×3, `AIEOS-Schema` ×2, `AIEOS-Implementierungsbeispiele` ×1 |
| `AI Entity Object Specification` ^[aieos-schema-fuer-ki-charaktere.md:#2] | 2 | 2 | 19, 626 |  |
| `Narrative Context Protocol` ^[aieos-schema-fuer-ki-charaktere.md:#4] | 4 | 4 | 577, 579, 610, 612 |  |
| `NCP` ^[aieos-schema-fuer-ki-charaktere.md:#8] | 8 | 8 | 577, 579, 581, 582, 610, 612, 616 |  |
| `Storyform` ^[aieos-schema-fuer-ki-charaktere.md:#3] | 3 | 3 | 579, 581, 612 |  |
| `Storytelling` ^[aieos-schema-fuer-ki-charaktere.md:#3] | 3 | 3 | 579, 581, 612 |  |
| `Narrative Entropy` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 582 |  |
| `God Mode` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 582 |  |
| `Character Card` ^[aieos-schema-fuer-ki-charaktere.md:#2] | 2 | 3 | 563, 565, 633 |  |
| `Lorebooks` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 565 |  |
| `Inworld AI` ^[aieos-schema-fuer-ki-charaktere.md:#11] | 11 | 11 | 41, 570, 572, 575, 627, 628, 634, 635, 636, 637, 638 |  |
| `ZeroClaw` ^[aieos-schema-fuer-ki-charaktere.md:#7] | 7 | 7 | 595, 600, 614, 616 |  |
| `NullClaw` ^[aieos-schema-fuer-ki-charaktere.md:#3] | 3 | 3 | 595, 599 |  |
| `OpenClaw` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 591 |  |
| `Nanobot` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 591 |  |
| `TinyClaw` ^[aieos-schema-fuer-ki-charaktere.md:#2] | 2 | 2 | 593 |  |
| `repomix` ^[aieos-schema-fuer-ki-charaktere.md:#2] | 2 | 3 | 33, 583, 612 | `repomix-Technologie` ×1 |
| `CodeAct` ^[aieos-schema-fuer-ki-charaktere.md:#0] | 0 | 3 | 45, 575, 591 | `CodeAct-Schleifen` ×1, `CodeAct-Sicherheit` ×1, `CodeAct-Operationen` ×1 |
| `SKILL.md` ^[aieos-schema-fuer-ki-charaktere.md:#0] | 0 | 1 | 33 | `SKILL.md-Protokoll` ×1 |
| `STATE.md` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 286 |  |
| `AGENTS.md` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 612 |  |
| `Constitutional AI` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 612 |  |
| `anthropomorphem Overhead` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 39 |  |
| `thermodynamischen Ineffizienz` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 43 |  |
| `Needle-in-a-Haystack` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 45 |  |
| `Zero-Trust` ^[aieos-schema-fuer-ki-charaktere.md:#0] | 0 | 1 | 35 | `Zero-Trust-Sicherheit` ×1 |
| `Lawful Neutral` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 182 |  |
| `Chaotic Neutral` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 438 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Landauer-Prinzip` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 2 | 43, 597 | `Landauer-Prinzips` ×1 |
| `Dual-Prozess-Theorie` ^[aieos-schema-fuer-ki-charaktere.md:#1] | 1 | 1 | 15 |  |
| `strukturellen Dissoziation der Persönlichkeit` ^[aieos-schema-fuer-ki-charaktere.md:#2] | 2 | 2 | 15, 45 |  |
| `TSDP` ^[aieos-schema-fuer-ki-charaktere.md:#2] | 2 | 2 | 15, 45 |  |

## What the extraction ran into


**Zeros:** 3 — `CodeAct`, `SKILL.md`, `Zero-Trust`.

**Standing alone less often than with compounds:** 12 — `AEGIS` 18/22, `Juna` 17/22, `JANUS` 4/18, `JANUS-Projekt` 1/3, `Kohärenz Protokoll` 2/4, `Kollaps-Kernel` 2/3, `Kernel` 8/26, `epistemischen Isolation` 2/3, `AIEOS` 9/15, `Character Card` 2/3, `repomix` 2/3, `Landauer-Prinzip` 1/2.

**Zeros, explained.** `CodeAct` stands only inside hyphen compounds (`CodeAct-Schleifen`, `CodeAct-Sicherheit`, `CodeAct-Operationen`, L45, L575, L591); `SKILL.md` only as `SKILL.md-Protokoll` (L33); `Zero-Trust` only as `Zero-Trust-Sicherheit` (L35). The word count refuses a hyphen on either side, so each is an inflection-like compound surface, not an absence; the three stand in the „in“ column.

**Alone less often than with compounds, explained.** Every one of the twelve is a head word that the document extends by a hyphen or a suffix: `AEGIS-Orchestrator`, `Juna-Agenten`, `JANUS-System`, `Kernel-AIs`, `AIEOS-Schema`, `repomix-Technologie`, `Landauer-Prinzips` and the like, as the surfaces column shows. `epistemischen Isolation` also meets the capitalised adjective form at L582 as a heading-like bullet; the case-sensitive word count does not join them.

**Export damage.** The export backslash-escapes underscores and brackets in the JSON field names (`neural\_matrix`-style keys), which is why such keys are not on the list. Empty JSON arrays lost their brackets, leaving keys with no value (L89, for example). At L581 two symbols standing for the kernels are lost, leaving a gap in the sentence about the dual-kernel theory. Footnote numbers are glued to sentence ends (L13 and many more), and nearly all quotation marks are straight ASCII glyphs. The reference list is numbered text with links and escapes.

**Surface notes.** `Kohärenz Digests` and `Kohärenz-Digests` stand both on L583 and are listed as written. `ANP` and `EP` stand in parentheses after the spelled-out `Apparently Normal Part` and `Emotional Part` (L17) and again in the later sentence (L45); `NCP` stands in parentheses after `Narrative Context Protocol`. `System 1` and `System 2` stand with a digit; the heading at L51 and L307 pairs each with the nicknames `Kohärenz-Kernel` and `Kollaps-Kernel`. `Chronozeption` (L43) and `Chronoperzeption` (L597) are two spellings of one word in the document. `JANUS` is the system's name; `JANUS-Projekt`, `JANUS-System` and `JANUS-Kernel` are the document's compounds.

**Standing claims.** The document claims no canon status for itself. Its recommendation (L608, L612, L614) is advice for the JANUS project, recorded here and applied nowhere.
