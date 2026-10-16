---
source: Sources/drive/dramatica-dual-storyform-mapping-analyse.md
drive_id: "123qT1AdmUxfud2RkW4O4M5UWkLjl2eHfl1tmu0GU5HQ"
title: "Dramatica Dual-Storyform Mapping Analyse"
category: storyform
index_date: "2026-04-30"
extracted: "2026-10-11"
candidates: 107    # the terms capture.py counted
---

# Term census — Dramatica Dual-Storyform Mapping Analyse

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py dramatica-dual-storyform-mapping-analyse`

```
  lines                281  (frontmatter ends at 9)
  body words           4636
  headings             21   bold-only lines 6
  table rows           35   code fences 0
  question marks       7
  backslash escapes    228
  typographic marks    97   ascii quotes 31
  invisible characters U+200Bx14
  math symbol lines    3
  glued ref numbers    52
  repeated labels      none
  longest line         1044 chars
```

## Stance, read per passage

The document is a research report in German with English method labels, presented as a plan-and-result analysis: it states its goal, a formal validity definition, a tree of hypotheses with verdicts, two surviving candidates, and its own logs. It reports the work of an analysis run; it does not narrate the novel.

- Executive summary (L13 to L17): reports that two mapping candidates survived. It says the earlier canonical solution was to be rejected as „obsolet“ ^[L15] by a methodological directive, and that the solution space was re-mapped.
- Formal definition (L19 to L43): a definition with numbered axioms and a validity criterion; a table marks two inversion types as allowed and two as „(Verboten)“ ^[L42].
- Hypothesis tree (L45 to L79): four branches, each with the labels `Evidenz Pro` ^[dramatica-dual-storyform-mapping-analyse.md:#4] and its Contra counterpart, and a verdict `Ergebnis` ^[dramatica-dual-storyform-mapping-analyse.md:#7]: two read „Zweig verworfen“ ^[L55] and two „Zweig überlebt“ ^[L63].
- Mini-schemata and alternatives (L81 to L159): each candidate carries a self-rated `Konfidenz` ^[dramatica-dual-storyform-mapping-analyse.md:#7] and a „What-would-change-my-mind“ ^[L93] line; the Alternatives add a table per candidate and a Begründung.
- Baseline and friction (L161 to L181): a steelman of the rejected construction and a friction analysis per candidate.
- Logs (L183 to L247): a Contradiction Log, a Query Expansion Log, a Cross-Pollination Log, a Hypothesis Half-Life Audit, five reflections and a rationalisation audit, each a self-review of the run's method.
- Open questions (L249 to L255): headed „Offene Fragen / Unresolved“ ^[L249], three questions left for a next phase.
- Methodology note and references (L257 to L280): names its method frame and lists 18 references, of which several are web sources with access dates and several are the project's own notebook documents.

A canon claim: the report calls the earlier construction „kanonische Konstruktion“ ^[L163] and calls it rejected; it records that rejection as its own directive's result. That is recorded here and applied nowhere. It also leaves the choice between its two alternatives to the author ^[L253].

## Candidates and counts

107 candidates, written while reading and frozen by the count (`Plan/runs/dramatica-dual-storyform-mapping-analyse/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `dramatica-dual-storyform-mapping-analyse.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kohärenz Protokoll` ^[dramatica-dual-storyform-mapping-analyse.md:#5] | 5 | 5 | 11, 15, 25, 264, 265 |  |
| `Kael` ^[dramatica-dual-storyform-mapping-analyse.md:#15] | 15 | 26 | 59, 60, 62, 67, 88, 91, 100, 111, 119, 120, 122, 133 … | `Kaels` ×10, `Kael-zentrierten` ×1 |
| `Juna` ^[dramatica-dual-storyform-mapping-analyse.md:#20] | 20 | 33 | 17, 33, 52, 54, 61, 69, 90, 100, 114, 118, 120, 122 … | `Juna-Anker` ×4, `Juna-Verankerung` ×3, `Junas` ×3, `Juna-Anker-Mechanismus` ×2 |
| `AEGIS` ^[dramatica-dual-storyform-mapping-analyse.md:#37] | 37 | 39 | 53, 59, 61, 67, 69, 75, 78, 88, 90, 100, 103, 111 … | `AEGIS-Signatur` ×1, `AEGIS-Analyse` ×1 |
| `Guardians` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 75, 103 |  |
| `LogOS` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 75 |  |
| `Mnemosyne` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 75 |  |
| `Cerberus` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 75 |  |
| `Kairos/Sophia` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 75 |  |
| `Konstrukt-Stadt` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 98, 171 |  |
| `Alter` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 19 | 11, 17, 62, 91, 105, 107, 109, 121, 135, 147, 169, 176 … | `Alternative` ×8, `Alternativen` ×4, `Alters` ×2 |
| `TSDP` ^[dramatica-dual-storyform-mapping-analyse.md:#4] | 4 | 6 | 60, 62, 91, 93, 145, 234 | `TSDP-Dissoziation` ×2 |
| `Dual-Kernel-Theorie` ^[dramatica-dual-storyform-mapping-analyse.md:#3] | 3 | 3 | 15, 31, 89 |  |
| `DKT` ^[dramatica-dual-storyform-mapping-analyse.md:#3] | 3 | 5 | 15, 17, 89, 93, 203 |  |
| `Dual-Kernel-Modell` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 53 |  |
| `Heuristics of Integration` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 15, 163 |  |
| `Phoenix Collapse` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 15, 163 |  |
| `Phönix-Kollaps` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 129 |  |
| `Alt-Kanon` ^[dramatica-dual-storyform-mapping-analyse.md:#3] | 3 | 6 | 17, 49, 190, 234, 238, 259 | `Alt-Kanons` ×2, `Alt-Kanon-Struktur` ×1 |
| `Landauer-Hitze` ^[dramatica-dual-storyform-mapping-analyse.md:#5] | 5 | 5 | 17, 53, 78, 240, 244 |  |
| `Erasure-Sweeps` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 53, 145 |  |
| `Erasure-Sweep` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 3 | 53, 99, 145 | `Erasure-Sweeps` ×2 |
| `Moonshine-Link` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 3 | 90, 122, 255 | `Moonshine-Link-Konstrukt` ×1, `Moonshine-Links` ×1 |
| `Vertex-Operator-Algebra` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 90, 255 |  |
| `Leech-Lattice` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 90, 255 |  |
| `Quanten-Witness` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 54 |  |
| `Gödel-Satz` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 54 |  |
| `Witness-Funktionen` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 17 |  |
| `Witness Function` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 227, 232 |  |
| `Zero-Knowledge-Proofs` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 17 |  |
| `Zero-Knowledge Proof` ^[dramatica-dual-storyform-mapping-analyse.md:#4] | 4 | 6 | 69, 179, 191, 205, 236, 245 |  |
| `ZKP` ^[dramatica-dual-storyform-mapping-analyse.md:#8] | 8 | 11 | 146, 179, 191, 193, 205, 236, 245 |  |
| `Dialetheia` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 3 | 133, 181, 192 | `Dialetheia-Toleranz` ×1 |
| `Holarchie` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 3 | 97, 180, 192 | `Holarchie-Emergenz` ×1 |
| `Algorithmischen Melancholie` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 254 |  |
| `Vortex-Inversion` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 61 |  |
| `Wahrheits-Rotation` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 31 |  |
| `Truth-Rotation` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 232 |  |
| `PSM` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 193 |  |
| `Phänomenales Selbstmodell` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 193 |  |
| `parakonsistenten Raum` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 17, 165 |  |
| `Orbifold-Konstruktion` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 165 |  |
| `Ontologische Transposition` ^[dramatica-dual-storyform-mapping-analyse.md:#4] | 4 | 5 | 17, 57, 85, 109, 169 |  |
| `Prozessuale Transposition` ^[dramatica-dual-storyform-mapping-analyse.md:#5] | 5 | 6 | 17, 65, 95, 135, 176, 244 |  |
| `Dual-Storyform-Mapping` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 11, 21 |  |
| `Dual-Storyform-Spiegelung` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 2 | 15, 25 | `Dual-Storyform-Spiegelungen` ×1 |
| `Zustands-Involution` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 40 |  |
| `Prozess-Involution` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 41 |  |
| `Lateral-Intern` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 42 |  |
| `Lateral-Extern` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 43 |  |
| `Domain-Bijektion` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 27 |  |
| `Pronomen-Inversion` ^[dramatica-dual-storyform-mapping-analyse.md:#6] | 6 | 6 | 28, 113, 139, 159, 234, 238 |  |
| `Schichten-Restriktion` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 29 |  |
| `Überlagerungs-Tensor` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 29 |  |
| `Thermodynamische Asymmetrie` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 31, 203 |  |
| `Triple-Stack` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 3 | 29, 236, 247 | `Triple-Stack-Ebene` ×1, `Triple-Stacks` ×1 |
| `Juna-Anker` ^[dramatica-dual-storyform-mapping-analyse.md:#4] | 4 | 6 | 114, 118, 140, 144, 172, 179 | `Juna-Anker-Mechanismus` ×2 |
| `Sekundär-Schicht` ^[dramatica-dual-storyform-mapping-analyse.md:#4] | 4 | 6 | 15, 114, 140, 172, 174, 181 | `Sekundär-Schicht-Reibung` ×2 |
| `Reibungs-Topologie` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 167, 236 |  |
| `Hypothesen-Baum` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 45 |  |
| `Contradiction Log` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 183, 259 |  |
| `Query Expansion Log` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 195 |  |
| `Cross-Pollination Log` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 207 |  |
| `Hypothesis Half-Life Audit` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 212 |  |
| `Reflection History` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 230 |  |
| `Rationalisierungs-Audit` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 3 | 238, 242, 259 | `Rationalisierungs-Audits` ×1 |
| `MIRROR` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 242, 259 |  |
| `ReAct` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 259 |  |
| `Methodology Note` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 257 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Dramatica` ^[dramatica-dual-storyform-mapping-analyse.md:#29] | 29 | 57 | 15, 17, 21, 23, 25, 29, 30, 33, 42, 43, 54, 61 … | `Dramatica-Theorie` ×4, `Dramatica-Diagonal-Gesetze` ×2, `Dramatica-Storyform-Architektur` ×1, `Dramatica-Domains` ×1 |
| `Storyform` ^[dramatica-dual-storyform-mapping-analyse.md:#4] | 4 | 14 | 11, 15, 21, 25, 27, 105, 161, 190, 227, 238, 263, 270 | `Storyforms` ×1, `Storyform-Auflösung` ×1 |
| `Storymind` ^[dramatica-dual-storyform-mapping-analyse.md:#6] | 6 | 8 | 17, 54, 165, 268, 274, 275, 277, 278 | `Storyminds` ×2 |
| `Throughline` ^[dramatica-dual-storyform-mapping-analyse.md:#9] | 9 | 19 | 15, 23, 27, 29, 52, 54, 114, 118, 140, 144, 159, 165 … | `Throughlines` ×4, `Throughline-Kreuzungen` ×2, `throughlines` ×1 |
| `Domain` ^[dramatica-dual-storyform-mapping-analyse.md:#9] | 9 | 30 | 15, 17, 23, 27, 29, 39, 60, 62, 71, 87, 89, 93 … | `Domain-Muster` ×3, `Domains` ×1, `Domain-Bijektion` ×1, `Domain-Schichten` ×1 |
| `Universe` ^[dramatica-dual-storyform-mapping-analyse.md:#38] | 38 | 44 | 15, 23, 40, 43, 51, 53, 59, 60, 62, 70, 71, 87 … | `Universe-Domain` ×5, `Universe-Prämisse` ×1 |
| `Physics` ^[dramatica-dual-storyform-mapping-analyse.md:#35] | 35 | 36 | 15, 17, 23, 41, 43, 51, 61, 67, 68, 69, 87, 97 … |  |
| `Mind` ^[dramatica-dual-storyform-mapping-analyse.md:#33] | 33 | 36 | 15, 23, 40, 42, 51, 59, 60, 61, 87, 88, 89, 97 … | `Mind-Domain` ×1, `Mindestens` ×1, `Mind-Symmetrie` ×1 |
| `Psychology` ^[dramatica-dual-storyform-mapping-analyse.md:#24] | 24 | 25 | 15, 23, 41, 42, 51, 63, 67, 87, 93, 97, 113, 119 … | `Psychology-Domain` ×1 |
| `MC` ^[dramatica-dual-storyform-mapping-analyse.md:#15] | 15 | 24 | 23, 30, 51, 53, 69, 75, 76, 79, 87, 97, 119, 133 … |  |
| `IC` ^[dramatica-dual-storyform-mapping-analyse.md:#20] | 20 | 27 | 23, 30, 52, 54, 69, 87, 97, 100, 120, 133, 146, 159 … |  |
| `OS` ^[dramatica-dual-storyform-mapping-analyse.md:#15] | 15 | 19 | 23, 30, 51, 63, 70, 71, 75, 78, 87, 93, 97, 98 … |  |
| `RS` ^[dramatica-dual-storyform-mapping-analyse.md:#11] | 11 | 12 | 23, 30, 61, 87, 90, 97, 122, 133, 148, 172, 232 |  |
| `Main Character` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 23, 214 |  |
| `Influence Character` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 2 | 23, 236 |  |
| `Objective Story` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 23 |  |
| `Relationship Story` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 23 |  |
| `Pronomen-Achse` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 3 | 15, 23, 247 | `Pronomen-Achsen` ×2 |
| `Quad-Algebra` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 21, 232 |  |
| `Dramatica-Quad-Axiom` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 23 |  |
| `Dynamik-Tupel` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 23 |  |
| `Driver` ^[dramatica-dual-storyform-mapping-analyse.md:#3] | 3 | 6 | 23, 43, 124, 150, 163, 254 | `Driver-Pivot` ×2 |
| `Limit` ^[dramatica-dual-storyform-mapping-analyse.md:#4] | 4 | 5 | 23, 33, 71, 124, 150 | `limitiert` ×3, `limitierenden` ×1 |
| `Outcome` ^[dramatica-dual-storyform-mapping-analyse.md:#3] | 3 | 5 | 23, 31, 124, 150, 203 | `Outcomes` ×2 |
| `Judgment` ^[dramatica-dual-storyform-mapping-analyse.md:#3] | 3 | 3 | 23, 124, 150 |  |
| `Optionlock` ^[dramatica-dual-storyform-mapping-analyse.md:#4] | 4 | 5 | 23, 98, 128, 154, 254 | `Optionlock-Erschöpfung` ×1 |
| `Timelock` ^[dramatica-dual-storyform-mapping-analyse.md:#5] | 5 | 6 | 23, 71, 98, 129, 155, 254 | `Timelock-Countdown` ×1 |
| `Fixed Attitude` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 61 |  |
| `Problem-Solving-Style` ^[dramatica-dual-storyform-mapping-analyse.md:#0] | 0 | 1 | 88 | `Problem-Solving-Style-Theorem` ×1 |
| `Landauer’s Principle` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 69, 159 |  |
| `Landauer-Limit` ^[dramatica-dual-storyform-mapping-analyse.md:#0] | 0 | 1 | 33 | `Landauer-Limits` ×1 |
| `Mutual Information` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 99 |  |
| `Hard Problem of Consciousness` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 107 |  |
| `Gödel-Unvollständigkeit` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 165 |  |
| `Steelmanning` ^[dramatica-dual-storyform-mapping-analyse.md:#2] | 2 | 2 | 163, 259 |  |
| `First-Principles Decomposition` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 259 |  |
| `Falsification` ^[dramatica-dual-storyform-mapping-analyse.md:#1] | 1 | 1 | 259 |  |
| `Multiplizität` ^[dramatica-dual-storyform-mapping-analyse.md:#3] | 3 | 3 | 17, 41, 137 |  |

## What the extraction ran into

**Zeros, explained.** `Problem-Solving-Style` ^[dramatica-dual-storyform-mapping-analyse.md:#0] is an inflection: the document writes only the compound `Problem-Solving-Style-Theorem` ^[dramatica-dual-storyform-mapping-analyse.md:#1] (L88). `Landauer-Limit` ^[dramatica-dual-storyform-mapping-analyse.md:#0] is an inflection too: the document writes `Landauer-Limits` ^[dramatica-dual-storyform-mapping-analyse.md:#1] (L33). Neither term is absent.

**The standing-alone gaps.** Most of the 40 are compounds and inflections, not different things: `Kael` with `Kaels`, `Juna` with `Juna-Anker`, `Junas`, `Dramatica` with `Dramatica-Theorie`, the four domain names with `Universe-Domain`, `Domain-Muster` and the like, and the lens roles `MC`, `IC`, `OS`, `RS` with possessive and hyphenated uses. `Alter` (2 alone, 19 anywhere) is a substring trap: the 19 include `Alternative` and `Alternativen`, and only the 2 standing alone are the document's `13 Alter`-system noun (L62, L91); it also holds `Alters`. `Storyform` stands alone 4 times against 14 anywhere because the document uses it mostly inside `Dual-Storyform-…` and `Dramatica-Storyform-Architektur`.

**Export damage.** The conversion lost every mathematical symbol: the names of the two storyforms, the mapping symbol, the domain and pronoun sets and the arrows are gaps, so a table cell reads with a double space between the two domain names where an arrow stood (L40). The headings and table cells of the alternatives are cut the same way: `Alternative` is followed by a gap where a symbol stood (L109). The two storyforms therefore cannot be listed by name; the document's own words for them survive only as `Storyform` and the Alternative labels. Table cells carry escaped asterisks (`\*\*`) and invisible zero-width characters in the header cells (L39, L118, L144); 228 backslash escapes and 14 zero-width characters are in the profile. Inline reference numbers are glued to the words they follow (52 in the profile), so a sentence ends in a digit. The tables' header rows are empty cells above the real header (L37, L116).

**Whose words.** The body quotes the project's own notebook sources by number only (`1` to `5` in the text, named in the reference list at L263 to L267), so a statement tagged with such a number is that source's, reported by this document. The Contradiction Log names them again with a number and a short title each (L190 to L193). The names `Heuristics of Integration` and `Phoenix Collapse` stand in quotation marks as the name of the rejected construction (L163).

**The two voices.** The text of the report is also marked, in its logs, by the reflections of the run itself (the Reflection History, L230 to L240): these are the analysis speaking about its own confidence, not statements about the novel's world.

**Candidates that stand only in a table or heading.** `Zustands-Involution`, `Prozess-Involution`, `Lateral-Intern`, `Lateral-Extern` stand only in the first column of the table at L40 to L43. `Hypothesen-Baum`, `Reibungs-Topologie`, `Contradiction Log`, `Query Expansion Log`, `Cross-Pollination Log`, `Reflection History` and `Methodology Note` head sections.

**Lens.** The `## lens` part of the list holds the Dramatica roles and domains and the borrowed information-theory and method terms; none of them is the novel's own naming. `Dramatica` is a framework the document applies to the world.

**Not listed.** The names of the 18 references and their addresses, the numbered axioms `M.1` to `M.6` and the step labels were left out; the abbreviations `Alt 1` and `Alt 2` are used for the two alternatives (L202, L204) and were not listed as candidates.

**Zeros:** 2 — `Problem-Solving-Style`, `Landauer-Limit`.

**Standing alone less often than with compounds:** 40 — `Kael` 15/26, `Juna` 20/33, `AEGIS` 37/39, `Alter` 2/19, `TSDP` 4/6, `DKT` 3/5, `Alt-Kanon` 3/6, `Erasure-Sweep` 1/3, `Moonshine-Link` 1/3, `Zero-Knowledge Proof` 4/6, `ZKP` 8/11, `Dialetheia` 2/3, `Holarchie` 2/3, `Ontologische Transposition` 4/5, `Prozessuale Transposition` 5/6, `Dual-Storyform-Spiegelung` 1/2, `Triple-Stack` 1/3, `Juna-Anker` 4/6, `Sekundär-Schicht` 4/6, `Rationalisierungs-Audit` 2/3, `Dramatica` 29/57, `Storyform` 4/14, `Storymind` 6/8, `Throughline` 9/19, `Domain` 9/30, `Universe` 38/44, `Physics` 35/36, `Mind` 33/36, `Psychology` 24/25, `MC` 15/24, `IC` 20/27, `OS` 15/19, `RS` 11/12, `Influence Character` 1/2, `Pronomen-Achse` 1/3, `Driver` 3/6, `Limit` 4/5, `Outcome` 3/5, `Optionlock` 4/5, `Timelock` 5/6.
