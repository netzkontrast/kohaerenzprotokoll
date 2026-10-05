---
source: Sources/drive/research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md
drive_id: "1WatAbHnlO_wbW8oLdWzM6S6OOjvW7Sh15WuM4d0JyfA"
title: "research-prompt_kohaerenz-protokoll-39kap-dual-storyform-outline.md"
category: storyform
index_date: "2026-04-30"
extracted: "2026-10-05"
candidates: 218    # the terms capture.py counted
---

# Term census — research-prompt_kohaerenz-protokoll-39kap-dual-storyform-outline.md

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out`

```
  lines                1299  (frontmatter ends at 9)
  body words           6371
  headings             50   bold-only lines 24
  table rows           37   code fences 0
  question marks       19
  backslash escapes    408
  typographic marks    248   ascii quotes 115
  invisible characters U+00ADx1
  math symbol lines    30
  glued ref numbers    90
  repeated labels      Wann stoppen x4, Warum es im Prompt ist x4, Was es ist x4, Wie anwenden — Schritt für Schritt x4
  longest line         469 chars
```

## Stance, read per passage

The document is a prompt addressed to an executing AI, not a narrative and not a report: it opens „An die ausführende KI: Dieser Prompt ist vollständig in sich geschlossen.“ ^[L38] Its passages fall into five registers, each marked by its own heading words.

**Frontmatter and title (L15 to L36).** Observed: the YAML header was flattened into one run-on line with escaped underscores (`research\_category`, `critical\_thinking\_methods`), so keys and values stand together on L15 and L30. It names the prompt's methods and a `constraint_blocks` list; the world is not named there.

**Meta-Header (L44 to L140): the document says what kind of task this is.** it names the research an extraction and forbids new hypotheses: „Du generierst keine neuen Hypothesen.“ ^[L50] It marks the output schema as a lock: „Das Output-Schema ist gelockt“ ^[L62]. Two frameworks are named as its layers, ReAct and RISEN, both applied to the executing AI, not to the novel.

**Forschungsziel and Constraint Blocks 0 to 5 (L144 to L576): lock, rule and template.** The blocks carry the label `verbindlich` in their headings (Block 1, 4 and 5) and the Pivot list. Block 4 sets values for two storyforms in two tables (L295 to L334) as given, not to be derived. Block 5 is a template whose fields are written in square brackets with placeholders; the same template is also written in escaped markdown (`\#\#\# Kapitel 1 — \[Arbeitstitel\]`), so those lines are the document's model of output, not output.

**Critical-thinking methods (L580 to L706): rule blocks with a fixed four-label pattern.** Each method repeats `Was es ist`, `Warum es im Prompt ist`, `Wie anwenden — Schritt für Schritt` and `Wann stoppen` (the four repeated labels of the profile, four times each); these are the template, not terms.

**R, I, S, E, N and the checks (L710 to L1290): plan, expectation, narrowing, audit.** Role is „Story Architect“ ^[L712]. The Steps are a numbered procedure whose Step 7 is a loop: „Du führst die folgende Prozedur exakt 39-mal aus, einmal pro Kapitel.“ ^[L971] The Pre-Synthesis check and the 11-item self-verification list are audits the executing AI must write out. The closing sentence `Ausführung jetzt.` ends the document at L1298.

**No sample text, no narrative voice.** The novel's world appears only as lists of seed words (L860 to L896), as the ten numbered canon points (L743 to L752), and as table values (L295 to L334). Nothing in the document is a scene or a passage in the novel's own voice. Questions: the 19 question marks of the profile stand in the five reflection questions of the template (L200 to L216) and in question-formed template fields; the Kernfrage the document reports as one of the points the canon defines, „Ist Liebe Information — oder das, was Information zerstört?“ ^[L749] is the document's own statement of the novel's question.

**Standing.** The document marks the canon it points to as the highest authority: „das übergebene Kanon-Trio ist absolute Wahrheit“ ^[L723]. This is the document's claim about three documents it does not contain; it is recorded, not applied here.

## Candidates and counts

218 candidates, written while reading and frozen by the count (`Plan/runs/research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kohärenz Protokoll` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 4 | 15, 36, 146, 364 |  |
| `Konstrukt-Stadt` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 743, 860 |  |
| `Mnemosyne-Archipel` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 344, 860 |  |
| `Sektor 04` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 860 |  |
| `Köln 2026` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 860 |  |
| `thermische Risse` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 860 |  |
| `Glitches` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 860 |  |
| `Pixelierung` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 860 |  |
| `Architektur als Antagonist` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 860 |  |
| `Kernwelten` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 860 |  |
| `Universal Reboot` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 860, 896 |  |
| `Universal Re-Connecting` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 860 |  |
| `Kael` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#8] | 8 | 9 | 293, 298, 308, 326, 329, 339, 345, 745, 864 | `Kaels` ×1 |
| `Juna` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#10] | 10 | 14 | 240, 305, 308, 338, 412, 570, 743, 746, 849, 876, 945, 1021 | `Juna-Komplex` ×2, `Juna-Resonanz` ×1, `Juna-Charakteristika` ×1 |
| `AEGIS` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#14] | 14 | 19 | 240, 307, 314, 319, 329, 339, 344, 348, 412, 570, 743, 745 … | `AEGIS-Komplex` ×2, `AEGIS-Erasure-Sweep` ×1, `AEGIS-territorium` ×1, `AEGIS-internen` ×1 |
| `Guardians` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 3 | 307, 745, 848 | `Guardians-Liste` ×1 |
| `Lex` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 864 |  |
| `Alex` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 864 |  |
| `Rhys` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 864 |  |
| `Selene` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 864 |  |
| `Nyx` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 864 |  |
| `Kiko` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 864 |  |
| `Lia` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 864 |  |
| `Isabelle` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 864 |  |
| `Moros` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 864 |  |
| `Argus` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 864 |  |
| `Silas` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 864 |  |
| `Oblivion` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 864 |  |
| `ANP` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 345, 864 |  |
| `EP` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 4 | 345, 767, 773, 864 |  |
| `TSDP` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 747, 864 |  |
| `13-Alter-System` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 747 |  |
| `Alter` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 10 | 240, 264, 412, 570, 747, 847, 864, 927, 945, 1021 | `Alter-Name` ×2, `alternativen` ×1, `Alter-System` ×1, `alternative` ×1 |
| `Funktionale Multiplizität` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 682, 747, 864 |  |
| `Host` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 329, 864 |  |
| `Wir-Geflecht` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 864 |  |
| `We-Voice` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 864 |  |
| `Polyphonie` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 3 | 416, 864, 1007 | `Polyphonie-Bruch` ×2 |
| `Komponente 734` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 745, 872 |  |
| `Index` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 266, 868, 1128 |  |
| `Nox` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 266, 868, 1128 |  |
| `Echo` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 266, 868, 1128 |  |
| `Flicker` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 266, 868, 1128 |  |
| `Limina` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 266, 868, 1128 |  |
| `Praetor` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 266, 868, 1128 |  |
| `Eos` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 266, 868, 1128 |  |
| `Elara` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 266, 868, 1128 |  |
| `Aris` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 266, 868, 1128 |  |
| `Mina` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 266, 868, 1128 |  |
| `Lyra` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 266, 868, 1128 |  |
| `Soren` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 266, 868, 1128 |  |
| `Tariq` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 266, 868, 1128 |  |
| `Nova` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 266, 868, 1128 |  |
| `Sentinel` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 266, 868, 1128 |  |
| `LogOS` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 872 |  |
| `Mnemosyne` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 3 | 344, 860, 872 | `Mnemosyne-Archipel` ×2 |
| `Cerberus` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 872 |  |
| `Kairos` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 872 |  |
| `Sophia` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 872 |  |
| `Genesis-Krise` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 306, 746, 872 |  |
| `Genesis-Sequenz` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 745, 896 |  |
| `Algorithmische Melancholie` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 745, 872 |  |
| `Algorithmischer Melancholie` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 348 |  |
| `Primal Directive` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 872 |  |
| `Trennungsprotokoll` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 3 | 328, 745, 872 | `Trennungsprotokolle` ×1 |
| `Trennungsprotokolle` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 328 |  |
| `Erasure-Sweeps` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 745, 872 |  |
| `Erasure-Sweep` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#0] | 0 | 3 | 344, 745, 872 | `Erasure-Sweeps` ×2 |
| `ZTEM` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 872 |  |
| `RTSV` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 872 |  |
| `BPoF` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 872 |  |
| `EIC` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 872 |  |
| `IntegrityGuardian` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 872 |  |
| `CogFirewall` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 872 |  |
| `ConsensusEnf` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 872 |  |
| `SIS` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 3 | 872, 1162, 1206 |  |
| `EntropicMgmt` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 872 |  |
| `RIVE` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 872 |  |
| `PMAS` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 872 |  |
| `SARM` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 872 |  |
| `Moonshine-Link` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 308, 876 |  |
| `Witness-Funktion` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 746, 876 |  |
| `Witness-Moment` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 346 |  |
| `Gödel-Eigenschaft` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 339, 746, 876 |  |
| `B+C-Superposition` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 876 |  |
| `MI-Ghost` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 876 |  |
| `Phantom-Resonanz` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 746, 876 |  |
| `Telefon-Stille` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 746, 876 |  |
| `Mosaik-Herz` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 876 |  |
| `Impact Character` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 876 |  |
| `Fragmentierungsnacht` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 876 |  |
| `lebende Paradoxie` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 326, 339 |  |
| `Dual-Kernel-Theorie` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 743, 880 |  |
| `DKT` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 9 | 240, 280, 372, 743, 850, 880, 927, 960, 1127 |  |
| `K0` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 5 | 314, 743, 745, 850, 880 |  |
| `K1` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 5 | 293, 743, 745, 850, 880 |  |
| `Coherence-Domain` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 743 |  |
| `Collapse-Domain` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 743 |  |
| `Coheron` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 850, 880 |  |
| `Erason` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 850, 880 |  |
| `Landauer-Limit` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 850, 880 |  |
| `Landauer-Hitze` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 347, 745 |  |
| `Bekenstein-Schranke` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 850, 880 |  |
| `Hawking-Strahlung` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 880 |  |
| `Chaitin-Konstante` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 880 |  |
| `Halteproblem` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 880 |  |
| `Gödel-Unvollständigkeit` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 880 |  |
| `Russell-Antinomie` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 880 |  |
| `η-Formel` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 850, 880 |  |
| `MI(S)` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 743, 880 |  |
| `Suppression-Effizienz` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 743 |  |
| `Strange Attractor` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 880 |  |
| `holographisches Prinzip` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 880 |  |
| `BRST` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 880 |  |
| `VOA` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 880 |  |
| `Leech-Lattice` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 880 |  |
| `Klein-Vierergruppe` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 880 |  |
| `Klein'sche Vierergruppe` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 241 |  |
| `Domain-Inversion` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 746 |  |
| `Riss-Mandat` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 884 |  |
| `Fundament` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 743, 884 |  |
| `Gardener's Axiom` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 884 |  |
| `Guardian's Dilemma` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 884 |  |
| `Driver-Pivot` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 5 | 334, 352, 884, 1004, 1082 | `Driver-Pivot-Markierung` ×1 |
| `Optionlock` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 5 | 310, 480, 884, 1001, 1154 | `Optionlock-Hinweis` ×1 |
| `Timelock` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 5 | 331, 480, 884, 1002, 1154 | `Timelock-Hinweis` ×1 |
| `Vortex-Inversion` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 336, 884 |  |
| `Storyforming` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 884 |  |
| `Vortex` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 15 | 242, 334, 336, 342, 561, 744, 748, 884, 1004, 1026, 1049, 1082 … | `Vortex-Beats` ×2, `Vortex-Inversion` ×2, `Vortex-Beat-Zuordnung` ×2, `Vortex-Architektur` ×1 |
| `Convergence` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 344, 1004 |  |
| `Pivot` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 23 | 334, 345, 352, 468, 472, 554, 556, 566, 884, 1003, 1004, 1025 … | `Pivot-Marker` ×3, `Pivot-Vorschlag` ×3, `Pivot-Marker-Block` ×2, `Pivots` ×2 |
| `Stille als lebende Dialetheia` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 346, 1004 |  |
| `Heat-Spike` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 347, 1004 |  |
| `Rotation` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 348, 1004 |  |
| `Ouroboros` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#0] | 0 | 7 | 492, 750, 852, 896, 1005, 1027, 1083 | `Ouroboros-Marker` ×4, `Ouroboros-Schluss` ×1, `Ouroboros-Phänomenologie` ×1, `Ouroboros-Ende` ×1 |
| `Ouroboros-Ende` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 896 |  |
| `Ouroboros-Schluss` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 750 |  |
| `Ouroboros-Marker` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 4 | 492, 1005, 1027, 1083 |  |
| `Pivot-Marker` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 5 | 472, 556, 1003, 1025, 1081 | `Pivot-Marker-Block` ×2 |
| `Limit-Marker` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 480, 1003 |  |
| `Outcome-Marker` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 484, 1003 |  |
| `Driver-Status` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 476, 1003 |  |
| `Vortex-Beat-Zuordnung` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 1026, 1082 |  |
| `Pivot-Kapitel` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 4 | 468, 554, 1081, 1153 | `Pivot-Kapiteln` ×1, `Pivot-Kapitel-Liste` ×1 |
| `IC-Asymmetrie` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 336 |  |
| `Interferenz-Engine` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 340 |  |
| `Storyform A` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#6] | 6 | 6 | 146, 293, 338, 420, 746, 1023 |  |
| `Storyform B` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#6] | 6 | 6 | 146, 314, 339, 444, 746, 1024 |  |
| `Heuristics of Integration` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 4 | 146, 293, 420, 896 |  |
| `Phoenix Collapse` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 4 | 146, 314, 444, 896 |  |
| `39-Kapitel-Matrix` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 896 |  |
| `Spiegel-Effekt` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 896 |  |
| `Köln-Bridge` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 896 |  |
| `epistemologische Eskalation` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 896 |  |
| `Ästhetik der Ohnmacht` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 744, 896, 1000 |  |
| `Anatomie der Spaltung` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 744, 896, 1000 |  |
| `Existenzielle Fusion` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 744, 1000 |  |
| `Computational Class` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 278, 1126 |  |
| `Somatic Rulebook` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 279, 1126 |  |
| `Lesersteuerung` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 888 |  |
| `Reader-Substrate` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 8 | 150, 416, 719, 888, 1007, 1022 | `Reader-Substrate-Mechanismus` ×2, `Reader-Substrate-Mechanismen` ×1, `Reader-Substrate-Theorie` ×1 |
| `Leerstellen` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 719, 888 |  |
| `Foreshadowing-Patterns` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 888 |  |
| `Fußnoten-System` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 888 |  |
| `unreliable narrators` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 719, 752 |  |
| `Temporal Scrambling` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 888 |  |
| `Mosaik-Form` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 719, 752, 888 |  |
| `Stilbruch-Akte` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 888 |  |
| `fraktale Zeitstruktur` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 719, 888 |  |
| `Egan-Falle` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 888 |  |
| `Ted-Chiang-Maßstab` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 888 |  |
| `Lesersog` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 888 |  |
| `Throughline` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#14] | 14 | 18 | 174, 242, 265, 298, 305, 307, 308, 319, 326, 328, 329, 424 … | `Throughlines` ×1 |
| `Signpost` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 7 | 174, 428, 452, 1001, 1023, 1024 | `Signpost-Beat` ×2, `Signposts` ×1 |
| `Concern` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#10] | 10 | 10 | 174, 299, 306, 320, 327, 432, 456, 1001, 1023, 1024 |  |
| `Issue` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#8] | 8 | 8 | 174, 300, 321, 436, 460, 1001, 1023, 1024 |  |
| `Driver` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#5] | 5 | 19 | 174, 309, 330, 334, 352, 440, 464, 476, 884, 1001, 1002, 1003 … | `Driver-Trigger` ×5, `Driver-Pivot` ×4, `Driver-Status` ×2, `Driver-Pivot-Markierung` ×1 |
| `Limit` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#6] | 6 | 10 | 174, 310, 331, 480, 628, 850, 880, 1001, 1002, 1003 | `Limit-Marker` ×2 |
| `Outcome` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#5] | 5 | 7 | 174, 311, 332, 484, 1001, 1002, 1003 | `Outcome-Marker` ×2 |
| `Judgment` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 4 | 312, 333, 1001, 1002 |  |
| `Storypoint` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 4 | 297, 318, 716, 851 | `Storypoints` ×1 |
| `Storypoints` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 2 | 716, 851 |  |
| `Steadfast` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 325 |  |
| `Brücke` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#8] | 8 | 11 | 244, 281, 416, 572, 574, 1005, 1007, 1016, 1129, 1142 | `Brücken-Beats` ×1, `Brücken-Vorschläge` ×1, `Brücken-Markierung` ×1 |
| `Vorschlag` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#6] | 6 | 11 | 281, 412, 566, 570, 1003, 1006, 1021, 1081, 1129, 1142 | `vorschlagen` ×1 |
| `nicht in Quellen` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 416, 1007, 1142 |  |
| `Pivot-Vorschlag` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 566, 1003, 1081 |  |
| `single-source` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#7] | 7 | 7 | 540, 600, 605, 1028, 1103, 1264, 1281 | `Single-Source-Befunde` ×1 |
| `Kanon-Trio` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#16] | 16 | 17 | 26, 238, 248, 264, 265, 532, 570, 601, 723, 735, 745, 841 … | `Kanon-Trios` ×1 |
| `Kanon-Snapshot` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 5 | 27, 158, 258, 789, 1192 | `Kanon-Snapshot-Datum` ×3 |
| `Kanon-Drift-Check` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 4 | 24, 935, 946, 1184 |  |
| `Reflection Baseline` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 4 | 25, 182, 781, 1277 |  |
| `Source Triangulation` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#5] | 5 | 5 | 19, 584, 813, 999, 1281 |  |
| `Contradiction Log` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#12] | 12 | 12 | 20, 70, 607, 621, 692, 817, 927, 928, 1029, 1085, 1244, 1282 |  |
| `What Would Change My Mind` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 21, 630, 821 |  |
| `Adversarial Query Expansion` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#7] | 7 | 7 | 22, 88, 122, 659, 809, 1095, 1278 |  |
| `M13` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#8] | 8 | 11 | 190, 659, 856, 1030, 1085, 1095, 1172, 1180, 1240, 1278 |  |
| `Hidden-Items / Schema-Gap Sanity Pass` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 23, 917 |  |
| `Seed Query Set` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#7] | 7 | 7 | 673, 841, 856, 900, 904, 927, 1094 |  |
| `Anti-Rationalization Guard` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 224 |  |
| `Pre-Synthesis Integrity Check` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#5] | 5 | 5 | 108, 191, 700, 1059, 1285 |  |
| `Restatement Checkpoint` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#7] | 7 | 7 | 582, 767, 769, 773, 975, 979, 1276 |  |
| `Query Expansion Log` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#6] | 6 | 6 | 688, 1085, 1180, 1236, 1278, 1286 |  |
| `Reflection History` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 1085, 1228, 1286 |  |
| `Methodology Note` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 220, 1085, 1260 |  |
| `Verworfenes Legacy-Material` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 623, 1085, 1212 |  |
| `Story Architect` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 712 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Dramatica` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 14 | 146, 154, 174, 280, 376, 681, 716, 927, 960, 1086, 1127, 1155 | `Dramatica-Termini` ×3, `Dramatica-Vokabular` ×3, `Dramatica-Storyform-Encoding-Phase` ×1, `Dramatica-Storyforms` ×1 |
| `ReAct` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 6 | 22, 80, 82, 126 | `ReAct-Framework` ×1, `ReAct-Zyklus` ×1, `ReAct-Wirbelsäule` ×1 |
| `RISEN` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 5 | 22, 124, 126 | `RISEN-Framework` ×1 |
| `IFS` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#0] | 0 | 2 | 682, 718 |  |
| `Iser` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#4] | 4 | 4 | 719, 751, 888, 892 |  |
| `Greg Egan` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 717, 751, 892 |  |
| `Ted Chiang` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#3] | 3 | 3 | 717, 751, 892 |  |
| `Jeff VanderMeer` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#2] | 2 | 2 | 751, 892 |  |
| `Heidegger Sein-zum-Tode` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 892 |  |
| `Wittgenstein Grenzen des Sagbaren` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 892 |  |
| `Kant Phaenomena/Noumena` ^[research-prompt-kohaerenz-protokoll-39kap-dual-storyform-out.md:#1] | 1 | 1 | 892 |  |

## What the extraction ran into

**Zeros:** 3 — `Erasure-Sweep`, `Ouroboros`, `IFS`. Each is a term the document writes only joined to another word or inflected, none is absent. `Erasure-Sweep` stands in `AEGIS-Erasure-Sweep` (L344) and as the plural `Erasure-Sweeps` (L745, L872); `read.py --count` gives 0 standing alone and 3 including compounds. `Ouroboros` stands 0 times alone and 7 times in compounds (`Ouroboros-Marker`, `Ouroboros-Schluss`, `Ouroboros-Ende`, `Ouroboros-Phänomenologie`), lines 492, 750, 852, 896, 1005, 1027, 1083. `IFS` stands twice joined, in `IFS-Failure` (L682) and `IFS-aware` (L718): 0 alone, 2 including compounds.

**Standing alone less often than with compounds:** 36 rows, listed by the draft below. They are mostly Dramatica field names and prompt labels that the document extends into compounds (`Pivot` 4 alone, 23 anywhere; `Driver` 5 alone, 19 anywhere; `Dramatica` 2 alone, 14 anywhere). They are one thing wearing several surfaces, which a count that did not report both numbers would split.

**`- ` lines read as prose and not counted:** 3 — Falsehood vs. Truth · Fact vs. Fantasy · Philip K. Dick. Each carries a period and a space, so `capture.py` read it as a sentence. They are candidates: `Falsehood vs. Truth` stands 1 time ^[L300] as the MC Issue of Storyform A, `Fact vs. Fantasy` 1 time ^[L321] as that of Storyform B, and `Philip K. Dick` 2 times, both among the genre anchors ^[L751]. The ordinal term `5. Position` ^[L884] is also outside the table; it stands once.

**Export damage.** Observed: 408 backslash escapes in the profile, most of them `\*\*` around the table cells and `\[` `\]` in the template; the two tables of Block 4 are flattened into pipe tables with an empty header row and bold cells. The profile's 90 glued reference numbers are the digits dropped from `K0`, `K1`, `13 Alter`, `39 Kapitel` by the export: where the document says K0 and K1 it writes them with plain digits and never subscripted, so what they name has to be read from the sentence (L743 gives them as the two kernels of the Dual-Kernel-Theorie). The symbol Ω of the Chaitin constant was lost in the export, so the term stands as `Chaitin-Konstante`. One soft hyphen (U+00AD) stands in the text. The alter names are listed once, on L864, with the reference to a canon document that is not here, so every one of the 13 stands once or, for the dekanonisiert names, three times as a list of names to discard.

**The dekanonisiert names.** `Index`, `Nox`, `Echo`, `Flicker`, `Limina`, `Praetor`, `Eos`, `Elara`, `Aris`, `Mina`, `Lyra`, `Soren`, `Tariq`, `Nova`, `Sentinel` each stand three times (L266, L868, L1128) and only as names to throw away; the document says „diese Namen sind ungültig und werden bei Auftauchen verworfen“ ^[L266]. They are on the list because the document names them, not because it uses them.

**Terms named and not explained.** Almost every in-world term stands once in a seed list and is defined nowhere here (for example `LogOS`, `Cerberus`, `Kairos`, `Sophia`, `ZTEM`, `RTSV`, `BPoF`, `EIC`, `SARM` on L872). The document's own root term, `Kohärenz Protokoll`, is the project title only, never explained. The document says where to look: „siehe Kanon-Dok für vollständige Liste“ ^[L864].

**Claims about its own standing.** It sets the Kanon-Trio above the sources it tells the executing AI to search: „Sie sind die alleinige Wahrheitsquelle für alle Kanon-Aussagen.“ ^[L238] and gives the conflict rule „Legacy verwerfen, nicht harmonisieren“ ^[L248]. It dates its status apart: the „Reset 2026-04-30“ is named as the measure of which older material stays valid ^[L260]. These are the document's claims about three other documents; they are recorded and not applied.

**Zeros:** 3 — `Erasure-Sweep`, `Ouroboros`, `IFS`.

**Standing alone less often than with compounds:** 36 — `Kael` 8/9, `Juna` 10/14, `AEGIS` 14/19, `Guardians` 2/3, `EP` 1/4, `Alter` 4/10, `Polyphonie` 1/3, `Mnemosyne` 1/3, `Trennungsprotokoll` 2/3, `SIS` 1/3, `DKT` 2/9, `K0` 4/5, `K1` 4/5, `Driver-Pivot` 4/5, `Optionlock` 4/5, `Timelock` 4/5, `Vortex` 4/15, `Pivot` 4/23, `Pivot-Marker` 3/5, `Pivot-Kapitel` 2/4, `Reader-Substrate` 4/8, `Throughline` 14/18, `Signpost` 4/7, `Driver` 5/19, `Limit` 6/10, `Outcome` 5/7, `Storypoint` 2/4, `Storypoints` 1/2, `Brücke` 8/11, `Vorschlag` 6/11, `Kanon-Trio` 16/17, `Kanon-Snapshot` 2/5, `M13` 8/11, `Dramatica` 2/14, `ReAct` 3/6, `RISEN` 4/5.

**`- ` lines read as prose and not counted:** 3 — Falsehood vs. Truth · Fact vs. Fantasy · Philip K. Dick.
