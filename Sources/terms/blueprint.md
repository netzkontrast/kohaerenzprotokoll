---
source: Sources/drive/blueprint.md
drive_id: "13kobkrXirVlspszCwcJxWakWjkFH9U9QAChHF3j4HtU"
title: "Blueprint"
category: plot-outline
index_date: "2025-07-29"
extracted: "2026-10-12"
candidates: 57    # the terms capture.py counted
---

# Term census — Blueprint

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py blueprint`

```
  lines                97  (frontmatter ends at 9)
  body words           1583
  headings             8   bold-only lines 0
  table rows           0   code fences 0
  question marks       0
  backslash escapes    0
  typographic marks    49   ascii quotes 6
  invisible characters none
  math symbol lines    0
  glued ref numbers    2
  repeated labels      none
  longest line         912 chars
```

## Stance, read per passage

The whole document is one voice, a first-person adviser who calls itself „Ihr Narrativer Architekt“ ^[L11] and announces „Hier ist die detaillierte Architektur unseres Romans“ ^[L13]. It is a plan: eight numbered sections, I to VIII, each headed in the document's own labels (the headings carry bold markers in the export).

- Opening, L11 to L13: a statement of purpose. The document calls its subject „die ultimative Synthese und den Leitfaden für unser gesamtes Vorhaben“ ^[L11], which is the document's claim about its own standing; it is recorded here and applied nowhere.
- Section I, L15 to L17: the document describes itself as „das übergeordnete Architekturdokument“ ^[L17] and says that a 39-chapter plot blueprint „bereits existiert“ ^[L17]; that blueprint is reported, not present.
- Sections II and III, L19 to L32: vision, thesis and principles, in the plan's own register („sind folgende Leitprinzipien maßgebend“ ^[L27]).
- Section IV, L34 to L47: the concepts of the world (AEGIS, Kael, Juna/V, Das Fundament, the Kernwelten), written as definitions in bullets that open with a bold label and a colon. Several statements are marked as postulated or as a requirement for the narrative, for example „Postuliert als die tiefste Realitätsebene“ ^[L41].
- Section V, L49 to L69: a list of paired tensions joined by an arrow; a list, not a sentence about a term.
- Section VI, L71 to L84: craft instructions and recommendations (technique labels such as Kishōtenketsu with „empfohlen“ ^[L83]).
- Section VII, L86 to L90: project status and tools, reported as fact; „Ein finaler, umfassender und schreibfertiger Plot-Blueprint in 39 Kapiteln ist bereits ausgearbeitet“ ^[L88] is a claim about another text.
- Section VIII, L92 to L96: open points under „Nächste Schritte“ ^[L92] and a closing line, „Der Bauplan steht“ ^[L96].

The document asks no question (the profile counts 0 question marks) and holds no sample prose.

## Candidates and counts

57 candidates, written while reading and frozen by the count (`Plan/runs/blueprint/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `blueprint.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kohärenz Protokoll` ^[blueprint.md:#4] | 4 | 4 | 11, 21, 39, 88 |  |
| `Gesamt-Blueprint` ^[blueprint.md:#2] | 2 | 3 | 11, 15, 17 | `Gesamt-Blueprints` ×1 |
| `Oberste Architekturdokument` ^[blueprint.md:#1] | 1 | 1 | 15 |  |
| `Architekturdokument` ^[blueprint.md:#2] | 2 | 2 | 15, 17 |  |
| `AEGIS-Manifest` ^[blueprint.md:#1] | 1 | 1 | 21 |  |
| `AEGIS` ^[blueprint.md:#17] | 17 | 18 | 21, 23, 30, 32, 38, 39, 40, 41, 42, 45, 46, 75 … | `AEGIS-Manifest` ×1 |
| `Kael` ^[blueprint.md:#6] | 6 | 14 | 23, 30, 32, 39, 40, 41, 42, 75, 77, 82, 84, 94 | `Kaels` ×8 |
| `Juna/V` ^[blueprint.md:#5] | 5 | 5 | 40, 84, 94 |  |
| `Lex` ^[blueprint.md:#1] | 1 | 1 | 39 |  |
| `Nyx` ^[blueprint.md:#1] | 1 | 1 | 39 |  |
| `Selene` ^[blueprint.md:#1] | 1 | 1 | 39 |  |
| `Moonshine-Link` ^[blueprint.md:#2] | 2 | 2 | 40, 79 |  |
| `Potentialmeer` ^[blueprint.md:#1] | 1 | 1 | 38 |  |
| `Paradoxon der Fehlausgerichteten Kohärenz` ^[blueprint.md:#1] | 1 | 1 | 38 |  |
| `Kohärenz Protokoll 1.0` ^[blueprint.md:#1] | 1 | 1 | 39 |  |
| `funktionalen Multiplizität` ^[blueprint.md:#2] | 2 | 2 | 39, 82 |  |
| `dialetheischen Geist` ^[blueprint.md:#1] | 1 | 1 | 39 |  |
| `ontologischer Exploit` ^[blueprint.md:#1] | 1 | 1 | 40 |  |
| `Das Fundament` ^[blueprint.md:#1] | 1 | 1 | 41 |  |
| `seltsamer Attraktor` ^[blueprint.md:#1] | 1 | 1 | 41 |  |
| `Paraiyas` ^[blueprint.md:#1] | 1 | 1 | 41 |  |
| `schwache Emergenz` ^[blueprint.md:#1] | 1 | 1 | 41 |  |
| `Kernwelten` ^[blueprint.md:#2] | 2 | 2 | 42, 44 |  |
| `KWs` ^[blueprint.md:#2] | 2 | 2 | 42, 45 |  |
| `KW1` ^[blueprint.md:#1] | 1 | 2 | 44 |  |
| `Konstrukt-Stadt` ^[blueprint.md:#1] | 1 | 1 | 44 |  |
| `Guardian` ^[blueprint.md:#1] | 1 | 1 | 44 |  |
| `Überwelt` ^[blueprint.md:#1] | 1 | 1 | 45 |  |
| `Externe Ebene` ^[blueprint.md:#1] | 1 | 1 | 46 |  |
| `Realitätsebenen` ^[blueprint.md:#3] | 3 | 3 | 32, 42 |  |
| `Risse` ^[blueprint.md:#2] | 2 | 2 | 47, 77 |  |
| `Resonanz-Gefüge` ^[blueprint.md:#1] | 1 | 1 | 79 |  |
| `Cache Kohärenz` ^[blueprint.md:#1] | 1 | 1 | 79 |  |
| `Monstergruppe` ^[blueprint.md:#1] | 1 | 1 | 79 |  |
| `Symmetrie` ^[blueprint.md:#1] | 1 | 1 | 79 |  |
| `Meta-Erzähler` ^[blueprint.md:#1] | 1 | 2 | 75, 94 | `Meta-Erzählers` ×1 |
| `Dissoziative Identitätsstörung` ^[blueprint.md:#1] | 1 | 1 | 39 |  |
| `TSDP` ^[blueprint.md:#1] | 1 | 1 | 39 |  |
| `Dramatica-Throughlines` ^[blueprint.md:#2] | 2 | 2 | 84 |  |
| `Overall Story` ^[blueprint.md:#1] | 1 | 1 | 84 |  |
| `Main Character` ^[blueprint.md:#1] | 1 | 1 | 84 |  |
| `Impact Character` ^[blueprint.md:#1] | 1 | 1 | 84 |  |
| `Subjective Story` ^[blueprint.md:#1] | 1 | 1 | 84 |  |
| `Novelcrafter` ^[blueprint.md:#1] | 1 | 1 | 90 |  |
| `Codex-Struktur` ^[blueprint.md:#1] | 1 | 1 | 90 |  |
| `Matrix View` ^[blueprint.md:#1] | 1 | 1 | 90 |  |
| `Single Source of Truth` ^[blueprint.md:#1] | 1 | 1 | 90 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Specification Gaming` ^[blueprint.md:#1] | 1 | 1 | 38 |  |
| `Kishōtenketsu` ^[blueprint.md:#1] | 1 | 1 | 83 |  |
| `Prehension` ^[blueprint.md:#1] | 1 | 1 | 40 |  |
| `Deus ex Machina` ^[blueprint.md:#1] | 1 | 1 | 41 |  |
| `Gödels Unvollständigkeitssätze` ^[blueprint.md:#1] | 1 | 1 | 38 |  |
| `Value-Alignment-Problem` ^[blueprint.md:#1] | 1 | 1 | 68 |  |
| `Kontrollproblem` ^[blueprint.md:#1] | 1 | 1 | 68 |  |
| `Environmental Storytelling` ^[blueprint.md:#1] | 1 | 1 | 77 |  |
| `Polyphone/Chorische Prosa` ^[blueprint.md:#1] | 1 | 1 | 82 |  |
| `autopoietisches System` ^[blueprint.md:#1] | 1 | 1 | 38 |  |

## What the extraction ran into

The count has no zero, so no surface is written differently from the list. The five terms that stand alone less often than with compounds are each an inflection or a compound, not damage: `Gesamt-Blueprint` also stands as `Gesamt-Blueprints` (L11, genitive), `AEGIS` also as `AEGIS-Manifest` (L21), `Kael` as `Kaels` eight times (the genitive), `KW1` inside `KW1-4` (L44), and `Meta-Erzähler` as `Meta-Erzählers` (L94).

Export artifacts: the profile counts 2 glued reference numbers and 6 ASCII quotes beside 49 typographic marks. `Novelcrafter` is followed directly by the word unterstützt and `Prompt Engineering` by „ist“ with no space (L90), so those two words are glued to the next word in the export; the list holds `Novelcrafter` and the count finds it as a whole word, so the glue did not hide it. Bold markers wrap most of the section-IV labels; the list writes them plain.

Short names: `Lex`, `Nyx` and `Selene` each stand once, in one parenthesis on L39, and are named there without a definition beyond a role word.

Boundaries and gaps. `Das Fundament` is the document's name for a deepest layer and is also an ordinary noun; it is listed as the capitalised heading of a bullet. The word `Fundament` stands 3 times alone. The document says the nature of `Juna/V` and of the `Externe Ebene` is still to be pinned down (L94), and names the origin of Kaels trauma and of the simulation as a step still to define; the reading takes that as the document's own list of open points. The 39-chapter plot blueprint it reports is not in this document, and the document counts `Kapiteln` once.

Standing claims: „Single Source of Truth“ ^[L90] is the document's phrase for a codex kept accurately, in a passage on a writing tool, and the opening calls the whole document „die ultimative Synthese“ ^[L11]. Both are recorded as the document's claim about itself or its tools and are applied nowhere.

Skipped from the list: the 17 tension pairs of section V (L53 to L69), except the two borrowed concepts named in the parenthesis on L68, and craft labels used in their ordinary sense. Nothing autobiographical stands in the document, so nothing was skipped for that reason.

**Zeros:** 0.

**Standing alone less often than with compounds:** 5 — `Gesamt-Blueprint` 2/3, `AEGIS` 17/18, `Kael` 6/14, `KW1` 1/2, `Meta-Erzähler` 1/2.
