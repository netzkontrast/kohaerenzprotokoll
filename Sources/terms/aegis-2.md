---
source: Sources/drive/aegis-2.md
drive_id: "1n7bk15RlotaCNhy1uCFONLNwo_Agdr_Y"
title: "aegis"
category: aegis
index_date: "2025-08-21"
extracted: "2026-10-21"
candidates: 19    # the terms capture.py counted
---

# Term census — aegis

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py aegis-2`

```
  lines                80  (frontmatter ends at 9)
  body words           88
  headings             0   bold-only lines 0
  table rows           0   code fences 0
  question marks       0
  backslash escapes    2
  typographic marks    0   ascii quotes 0
  invisible characters none
  math symbol lines    0
  glued ref numbers    0
  repeated labels      none
  longest line         67 chars
```

## Stance, read per passage

The document is a chart exported as text, with no sentences. Its title line names the chart and its two pairs of poles: „Aegis Entity Mapping: Existence vs. Experience | Structure vs. Flow“ ^[L13]. The axes are written as „Structure (-) \<--\> Flow (+)“ ^[L59], and numeric tick values (1.0, 0.5, 0.0, -0.5, -1.0) stand on separate lines. Entity labels sit in the plot area: „Host (Organic Core) Aegis (Machine Core)“ ^[L29], „Protector Alter Gatekeeper“ ^[L33], „Creative Alter Logic/Analyst Alter Trauma Holder“ ^[L35] and „Al Agent (LLM) Integrated Self (Ideal)“ ^[L37]. Each label is a plot marker, an `X` on its own line follows several. The last line is „Image labels: [Plot; Screenshot; Diagram; Chart; Map]“ ^[L79], which reads as an automatic description of the image, not as a statement of the document.

## Candidates and counts

19 candidates, written while reading and frozen by the count (`Plan/runs/aegis-2/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `aegis-2.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Aegis Entity Mapping` ^[aegis-2.md:#1] | 1 | 1 | 13 |  |
| `Existence` ^[aegis-2.md:#2] | 2 | 2 | 11, 13 |  |
| `Experience` ^[aegis-2.md:#2] | 2 | 2 | 11, 13 |  |
| `Structure` ^[aegis-2.md:#2] | 2 | 2 | 13, 59 |  |
| `Flow` ^[aegis-2.md:#2] | 2 | 2 | 13, 59 |  |
| `Host (Organic Core)` ^[aegis-2.md:#2] | 2 | 2 | 15, 29 |  |
| `Host` ^[aegis-2.md:#2] | 2 | 2 | 15, 29 |  |
| `Organic Core` ^[aegis-2.md:#2] | 2 | 2 | 15, 29 |  |
| `Aegis (Machine Core)` ^[aegis-2.md:#2] | 2 | 2 | 29, 69 |  |
| `Aegis` ^[aegis-2.md:#3] | 3 | 3 | 13, 29, 69 |  |
| `Machine Core` ^[aegis-2.md:#2] | 2 | 2 | 29, 69 |  |
| `Creative Alter` ^[aegis-2.md:#2] | 2 | 2 | 21, 35 |  |
| `Child Alter` ^[aegis-2.md:#2] | 2 | 2 | 23, 31 |  |
| `Protector Alter` ^[aegis-2.md:#2] | 2 | 2 | 27, 33 |  |
| `Gatekeeper` ^[aegis-2.md:#2] | 2 | 2 | 33, 49 |  |
| `Logic/Analyst Alter` ^[aegis-2.md:#2] | 2 | 2 | 35, 65 |  |
| `Trauma Holder` ^[aegis-2.md:#2] | 2 | 2 | 35, 41 |  |
| `Al Agent (LLM)` ^[aegis-2.md:#2] | 2 | 2 | 37, 61 |  |
| `Integrated Self (Ideal)` ^[aegis-2.md:#2] | 2 | 2 | 37, 57 |  |

## What the extraction ran into

No candidate counts zero and none stands alone less often than with compounds. Each label stands twice in the body, because the chart text repeats every label once as a plot marker and once as a legend or axis-side label. `Aegis` stands three times, twice inside the joined form `Aegis (Machine Core)` and once in the title line. `Host` and `Organic Core` are listed beside their joined form `Host (Organic Core)`, as are `Aegis` and `Machine Core` beside `Aegis (Machine Core)`.

Export damage: the arrows in the axis lines carry backslash escapes (2 lines, L11 and L59), as the profile counts. The label `Al Agent (LLM)` is written with a lower-case L where an I would be expected; it is listed as written (`Al Agent` counts 2). The chart carries no axis explanation, no definition and no sentence, so the document defines none of its labels and gives no coordinates in words; the positions are only visible as the order of tick values and markers, which the flattened text does not preserve. The document makes no claim about its own standing.

**Zeros:** 0.

**Standing alone less often than with compounds:** 0.
