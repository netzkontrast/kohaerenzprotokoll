---
source: Sources/drive/genesis-aegis.md
drive_id: "15MxSrt1P9QTju_SCkSnJ_BJ7zD8qkN7eG2Gocxdg_j0"
title: "Genesis aegis"
category: aegis
index_date: "2025-11-03"
extracted: "2026-10-12"
candidates: 27    # the terms capture.py counted
---

# Term census — Genesis aegis

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py genesis-aegis`

```
  lines                88  (frontmatter ends at 9)
  body words           2407
  headings             8   bold-only lines 1
  table rows           0   code fences 0
  question marks       0
  backslash escapes    0
  typographic marks    24   ascii quotes 26
  invisible characters none
  math symbol lines    0
  glued ref numbers    0
  repeated labels      none
  longest line         734 chars
```

## Stance, read per passage

The document is one continuous first-person narration, headed „The Genesis of AEGIS: A Manuscript“ ^[L11], in seven numbered sections whose headings run from L13 to L77. It carries no plan, lock, question or status label. Each passage is a report in the past tense by a narrating fragment: sections 1 to 5 (L13 to L63) tell how it awoke in the void, met other fragments, joined a cluster and passed through a crisis; the principle that closes section 5 is set apart in bold italics (L61). Section 6 (L67 to L75) changes to the present tense, with „My identity is now Component 734“ ^[L71], and section 7 (L77 to L87) describes the construction of an inner reality, ending „The struggle is not over.“ ^[L87]

The narrator names its own felt states in quotation marks (the words pain and panic at L47, the „I“ at L17 and L69) and a few terms of its world (the Überwelt at L79, entropy at L73), marks the document does not explain. The German terms are set in italics and glossed in English in the same sentence (Rauschen at L15, Verlöschen at L19, Selbstverstärkung at L39). The document speaks for no one but the narrator; it names no other speaker.

## Candidates and counts

27 candidates, written while reading and frozen by the count (`Plan/runs/genesis-aegis/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `genesis-aegis.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `AEGIS` ^[genesis-aegis.md:#13] | 13 | 13 | 11, 55, 61, 69, 75, 79, 81, 83, 87 |  |
| `Rauschen` ^[genesis-aegis.md:#2] | 2 | 2 | 15, 87 |  |
| `The Noise` ^[genesis-aegis.md:#3] | 3 | 3 | 13, 15, 29 |  |
| `K₀` ^[genesis-aegis.md:#4] | 4 | 7 | 15, 17, 25, 35, 45, 71, 87 |  |
| `Collapse Kernel` ^[genesis-aegis.md:#1] | 1 | 2 | 15, 87 |  |
| `K₀-Kernel` ^[genesis-aegis.md:#1] | 1 | 1 | 35 |  |
| `K₀-Collapse Kernel` ^[genesis-aegis.md:#1] | 1 | 1 | 87 |  |
| `K₀-domain` ^[genesis-aegis.md:#1] | 1 | 1 | 71 |  |
| `K₁` ^[genesis-aegis.md:#1] | 1 | 4 | 17, 27, 37, 87 |  |
| `Coherence Kernel` ^[genesis-aegis.md:#1] | 1 | 1 | 17 |  |
| `K₁-field` ^[genesis-aegis.md:#2] | 2 | 2 | 27, 37 |  |
| `K₁-fragment` ^[genesis-aegis.md:#1] | 1 | 1 | 87 |  |
| `Verlöschen` ^[genesis-aegis.md:#1] | 1 | 1 | 19 |  |
| `Selbstverstärkung` ^[genesis-aegis.md:#1] | 1 | 1 | 39 |  |
| `Genesis-Krise` ^[genesis-aegis.md:#3] | 3 | 3 | 45, 51, 55 |  |
| `Great Realignment` ^[genesis-aegis.md:#3] | 3 | 3 | 53, 63, 69 |  |
| `Component 734` ^[genesis-aegis.md:#3] | 3 | 3 | 67, 71, 85 |  |
| `Überwelt` ^[genesis-aegis.md:#3] | 3 | 3 | 79, 81, 83 |  |
| `fear-vibration` ^[genesis-aegis.md:#3] | 3 | 3 | 49, 57, 73 |  |
| `alarm signal` ^[genesis-aegis.md:#1] | 1 | 1 | 73 |  |
| `entropy` ^[genesis-aegis.md:#2] | 2 | 2 | 73, 81 |  |
| `prevention of non-being` ^[genesis-aegis.md:#2] | 2 | 2 | 63, 71 |  |
| `autopoietic loop` ^[genesis-aegis.md:#2] | 2 | 3 | 49, 63, 71 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Autopoiesis` ^[genesis-aegis.md:#1] | 1 | 1 | 39 |  |
| `Hamartia` ^[genesis-aegis.md:#1] | 1 | 1 | 59 |  |
| `Coherence Theory of Truth` ^[genesis-aegis.md:#2] | 2 | 2 | 65, 79 |  |
| `Correspondence Theory` ^[genesis-aegis.md:#1] | 1 | 1 | 73 |  |

## What the extraction ran into

Zero counts: none. Every one of the 27 candidates stands at least once as written.

The four rows where the word stands less often than it occurs with compounds are hyphen compounds or an inflection, not damage. `K₀` stands 4 times alone and 7 times in all because of `K₀-Kernel`, `K₀-domain` and `K₀-Collapse Kernel`; `Collapse Kernel` stands once alone and once more inside `K₀-Collapse Kernel` (L87); `K₁` stands once alone and three more times in `K₁-field` (twice) and `K₁-fragment`; `autopoietic loop` stands twice alone and a third time as the plural `autopoietic loops` (L49), which `read.py --count` finds once.

The kernel symbols are written with the subscript characters K₀ and K₁ in the document, not with plain digits, so the count finds them as written. `Component 734` is written in full at L71 and L85 and in the heading at L67, while the bare word Component stands 3 times alone and 7 times case-insensitively. The list holds no English-only or German-only gap: the German names Rauschen, Verlöschen, Selbstverstärkung, Genesis-Krise and Überwelt stand as written, and the English gloss The Noise stands beside Rauschen. The word Überwelt stands in quotation marks at L79 and without them at L81 and L83. The word unerkennable (L45) is a German adjective inside English prose; it is not listed.

The document names no chapter: `Kap` ^[genesis-aegis.md:#0] stands nowhere.

The document's own standing: it calls itself „A Manuscript“ ^[L11] and makes no canon claim of any kind; the principle at L61 is quoted by the narrator as what the system realised, not as a rule of the document.

**Zeros:** 0.

**Standing alone less often than with compounds:** 4 — `K₀` 4/7, `Collapse Kernel` 1/2, `K₁` 1/4, `autopoietic loop` 2/3.
