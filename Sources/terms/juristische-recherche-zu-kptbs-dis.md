---
source: Sources/drive/juristische-recherche-zu-kptbs-dis.md
drive_id: "10HYYFk6fTeDDzvUYD8kyrarQmtkoPnoluBAK37mz5II"
title: "Juristische Recherche zu kPTBS/DIS"
category: theorie-psychologie
index_date: "2025-05-26"
extracted: "2026-10-21"
candidates: 13    # the terms capture.py counted
---

# Term census — Juristische Recherche zu kPTBS/DIS

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py juristische-recherche-zu-kptbs-dis`

```
  lines                775  (frontmatter ends at 9)
  body words           14223
  headings             1   bold-only lines 21
  table rows           7   code fences 0
  question marks       49
  backslash escapes    26
  typographic marks    41   ascii quotes 130
  invisible characters none
  math symbol lines    0
  glued ref numbers    51
  repeated labels      none
  longest line         2519 chars
```

## Stance, read per passage

The document is a research report on the social-law assessment of real diagnoses; it is headed „Juristische Analyse der Begutachtung komplexer Traumafolgestörungen im deutschen Sozialrecht“ ^[L11]. It speaks as a report in sections: a summary under „I. TL;DR (Management Summary / Kernaussagen)“ ^[L13], a discussion of a first research stage, then answers to numbered research questions such as „II.A.1.a Welche allgemeinen Anforderungen stellt die Rechtsprechung“ ^[L106], a synthesis of argument lines (L283 to L326), and a source list from L328 to the end. It does not mention the novel's world, a figure, a chapter or a system. The candidates are therefore clinical concepts the document applies, all under lens; the passage on real diagnoses and their legal handling is not harvested.

## Candidates and counts

13 candidates, written while reading and frozen by the count (`Plan/runs/juristische-recherche-zu-kptbs-dis/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `juristische-recherche-zu-kptbs-dis.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `kPTBS` ^[juristische-recherche-zu-kptbs-dis.md:#79] | 79 | 84 | 15, 21, 23, 27, 36, 77, 82, 84, 86, 92, 95, 140 … | `kPTBS-Diagnose` ×1 |
| `PTBS` ^[juristische-recherche-zu-kptbs-dis.md:#36] | 36 | 121 | 15, 21, 23, 27, 36, 56, 77, 82, 84, 86, 92, 94 … | `PTBS-Diagnose` ×1 |
| `DIS` ^[juristische-recherche-zu-kptbs-dis.md:#65] | 65 | 66 | 15, 21, 23, 27, 77, 82, 84, 86, 92, 95, 140, 155 … |  |
| `DSO` ^[juristische-recherche-zu-kptbs-dis.md:#14] | 14 | 17 | 23, 77, 86, 161, 162, 163, 166, 170, 176, 226, 232, 281 … |  |
| `ICD-11` ^[juristische-recherche-zu-kptbs-dis.md:#47] | 47 | 50 | 17, 23, 36, 86, 92, 110, 157, 161, 162, 163, 165, 166 … | `ICD-11-Kriterien` ×2 |
| `Störungen der Selbstorganisation` ^[juristische-recherche-zu-kptbs-dis.md:#9] | 9 | 9 | 23, 77, 86, 92, 161, 162, 170, 290, 296 |  |
| `Psychotraumatologie` ^[juristische-recherche-zu-kptbs-dis.md:#4] | 4 | 4 | 77, 84, 289 |  |
| `Dissoziation` ^[juristische-recherche-zu-kptbs-dis.md:#5] | 5 | 10 | 77, 165, 194, 195, 200, 309, 498, 528, 647 | `Dissoziation-Forum` ×5, `dissoziation-forum` ×3 |
| `Identitätswechsel` ^[juristische-recherche-zu-kptbs-dis.md:#6] | 6 | 7 | 93, 165, 195, 197, 198, 202, 313 | `Identitätswechseln` ×1 |
| `Verdecktheit` ^[juristische-recherche-zu-kptbs-dis.md:#4] | 4 | 4 | 185, 189, 307, 311 |  |
| `Chronizität` ^[juristische-recherche-zu-kptbs-dis.md:#16] | 16 | 16 | 21, 65, 66, 123, 127, 128, 132, 153, 206, 210, 231, 246 … |  |
| `Multimorbidität` ^[juristische-recherche-zu-kptbs-dis.md:#15] | 15 | 15 | 15, 19, 42, 43, 95, 115, 119, 214, 218, 233, 248, 285 … |  |
| `Synergieeffekte` ^[juristische-recherche-zu-kptbs-dis.md:#7] | 7 | 18 | 19, 42, 45, 115, 119, 214, 218, 226, 231, 233, 248, 295 | `Synergieeffekten` ×11 |

## What the extraction ran into

Zeros: none; all 13 candidates stand alone at least four times. Where the standing-alone count is lower than the count with compounds, the difference is hyphen compounds (`kPTBS-Diagnose`, `PTBS-Diagnose`, `ICD-11-Kriterien`, `Dissoziation-Forum`) and inflection (`Synergieeffekten`, `Identitätswechseln`), as the surfaces column lists; `Dissoziation-Forum` is a web source name in the source list, not a term. The export shows markup artifacts: list-break comments such as „<!-- end list -->“ ^[L34], a table whose cells carry escaped asterisks (L50 to L56), glued reference numbers after words (51 in the profile), and source-list entries marked „CAPTCHA, kein Inhalt“ ^[L558] or „Identisch mit“ ^[L368]. The source list holds titles and addresses of real documents; none is a term of the novel. The document makes no claim about its own standing as canon.

**Zeros:** 0.

**Standing alone less often than with compounds:** 8 — `kPTBS` 79/84, `PTBS` 36/121, `DIS` 65/66, `DSO` 14/17, `ICD-11` 47/50, `Dissoziation` 5/10, `Identitätswechsel` 6/7, `Synergieeffekte` 7/18.
