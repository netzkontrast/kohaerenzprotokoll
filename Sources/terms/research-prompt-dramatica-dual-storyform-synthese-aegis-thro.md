---
source: Sources/drive/research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md
drive_id: "1NCLUgVtipGYehdOlBpEoCRqM7-PPnRUUO-URKmknj-I"
title: "research-prompt_dramatica-dual-storyform-synthese-aegis-throughline.md"
category: storyform
index_date: "2026-04-29"
extracted: "2026-10-11"
candidates: 180    # the terms capture.py counted
---

# Term census — research-prompt_dramatica-dual-storyform-synthese-aegis-throughline.md

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py research-prompt-dramatica-dual-storyform-synthese-aegis-thro`

```
  lines                1857  (frontmatter ends at 9)
  body words           9647
  headings             44   bold-only lines 31
  table rows           15   code fences 0
  question marks       67
  backslash escapes    519
  typographic marks    329   ascii quotes 197
  invisible characters none
  math symbol lines    13
  glued ref numbers    135
  repeated labels      Example trigger in this research context x6, How to apply it — step by step x6, Sub-Steps x6, What it is x6, When to stop / escape criterion x6, Why it is in this prompt x6, Ziel x6
  longest line         608 chars
```

## Stance, read per passage

The text is addressed to another AI throughout, in the second person; it does not narrate the novel. Its metadata block (L15 to L32) lists `research_category`, methods and constraint blocks as fields, and its opening note on the reader declares: „Dieser Prompt ist vollständig selbsttragend.“ ^[L40] It sorts itself under „Meta-Header — Was dieser Prompt ist und wie er gelesen wird“ ^[L46] and says of the task: „Dies ist eine Exploration, keine Extraktion.“ ^[L52]

- **Plan and instruction (L46 to L146, L542 to L1466):** the three layers (category A, ReAct, RISEN), the Role, Input, Steps, Expectations and Narrowing sections are instructions to the executing AI. Here the prompt speaks in imperatives and templates; statements about the novel inside them are the prompt's own claims about its project, not narrative.
- **Question and open hypothesis (L150 to L170, L629 to L631):** the research question is asked as a question (L156), and the prompt says of it: „Die Antwort ist nicht im Voraus festgelegt.“ ^[L160] The client's hypothesis is marked as one of three to be tested: „Sie ist weder zu bestätigen noch zu widerlegen“ ^[L631].
- **Lock (L277 to L309):** Constraint Blocks 2 and 3 are written as binding lists. Block 2 calls the PDF „bindende Projekt-Kanon“ ^[L279]. The prompt records this as its own claim about that PDF; nothing here applies it.
- **Method definitions (L339 to L538):** six method blocks, each under the same repeated labels (`What it is`, `Why it is in this prompt`, `How to apply it — step by step`, `When to stop / escape criterion`, `Example trigger in this research context`). The fields are the template, not terms. The examples inside them mention the novel's terms as sample triggers.
- **Report templates with empty slots (L894 to L1280, L1472 to L1822):** the output schemas hold placeholders in square brackets such as „Bayesianischer Prior: [...]“ ^[L1140]; no finding is filled in. The prompt introduces the final document with „Du füllst das folgende Output-Schema vollständig aus.“ ^[L1474]
- **Checklist and close (L1828 to L1856):** „SELF-VERIFICATION CHECKLIST FOR THE EXECUTING AI“ ^[L1828] and the last line, „Ende des Forschungs-Prompts. Führe ihn jetzt aus.“ ^[L1856]

Register: a quotation inside an example trigger or a template slot belongs to the template. For example the table at L787 to L801 is a blank-for-the-reader inventory the prompt pre-fills with a PDF column and a Memory column; those cells are the prompt's report of two other sources, and the prompt itself marks the Driver row for checking (`prüfen`).

## Candidates and counts

180 candidates, written while reading and frozen by the count (`Plan/runs/research-prompt-dramatica-dual-storyform-synthese-aegis-thro/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `AEGIS` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#51] | 51 | 85 | 15, 25, 38, 64, 156, 160, 164, 165, 166, 178, 182, 217 … | `AEGIS-Frage` ×4, `AEGIS-Throughline-Position` ×3, `AEGIS-Throughline-Verortung` ×2, `AEGIS-Verortungs-Analyse` ×2 |
| `Kael` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#12] | 12 | 17 | 283, 593, 604, 904, 907, 947, 1002, 1076, 1107, 1117, 1118, 1236 … | `Kaels` ×1, `Kael-AEGIS-Bindung` ×1, `Kael-Juna-Paar` ×1 |
| `Juna` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#7] | 7 | 17 | 30, 286, 306, 771, 819, 906, 1003, 1117, 1261, 1300, 1394, 1462 … | `Junas` ×6, `Juna-Asymmetrie` ×2, `Juna-Asymmetrie-Bruch` ×1 |
| `Junas Asymmetrie` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 2 | 286, 1394 |  |
| `Juna-Asymmetrie` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 3 | 30, 306, 1462 | `Juna-Asymmetrie-Bruch` ×1 |
| `Guardian` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#9] | 9 | 21 | 156, 165, 287, 307, 395, 604, 1055, 1060, 1062, 1063, 1064, 1076 … | `Guardians` ×4, `Guardian-Sub-Agent` ×1, `Guardian-as-MC` ×1, `Guardian-Wahl` ×1 |
| `Guardians` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#4] | 4 | 4 | 287, 307, 604, 1398 |  |
| `LogOS` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 156, 1062, 1534 |  |
| `Mnemosyne` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 7 | 156, 285, 333, 1063, 1244, 1252, 1534 | `Mnemosyne-Archipel` ×4 |
| `Cerberus` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 156, 1064, 1534 |  |
| `Kairos/Sophia` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 2 | 156, 1065 |  |
| `Kairos` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 156, 1065, 1534 |  |
| `Sophia` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 156, 1065, 1534 |  |
| `Mnemosyne-Archipel` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#4] | 4 | 4 | 285, 333, 1244, 1252 |  |
| `Wächter-Zwiespalt` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 4 | 333, 1065, 1304, 1754 | `Wächter-Zwiespalt-Soziopolitik` ×2 |
| `Trennungsprotokolle` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 2 | 164, 909 |  |
| `Trennungs-Protokoll-Gefüge` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 1076 |  |
| `Erasure-Sweeps` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 1215 |  |
| `Truth-Rotation` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 5 | 283, 297, 1103, 1107, 1148 | `Truth-Rotation-Verdikt` ×1, `Truth-Rotation-Tragfähigkeits-Vergleich` ×1 |
| `Wahrheits-Vortex` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 333 |  |
| `Kollaps-Kern` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 4 | 283, 284, 330, 333 | `Kollaps-Kern-Reading` ×1 |
| `Erasure Kernel` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 330 |  |
| `Coherence Kernel` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 330 |  |
| `K0` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 8 | 152, 283, 330, 1107, 1108 |  |
| `K1` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 4 | 152, 283, 330, 1107 |  |
| `Algorithmische Melancholie` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#5] | 5 | 5 | 330, 333, 1236, 1248, 1296 |  |
| `Algorithmischer Melancholie` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 1109 |  |
| `Coheron` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 3 | 288, 330, 552 | `Coherons` ×1, `Coheron-Erason-Dynamik` ×1 |
| `Coherons` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 288 |  |
| `Erason` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 4 | 288, 330, 552 | `Erasonen` ×1, `Erason-Gravitation` ×1 |
| `Erasonen` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 288 |  |
| `η-Formel` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 288 |  |
| `PAL-Zeit` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 288 |  |
| `Erason-Gravitation` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 288 |  |
| `Landauer Heat` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 330 |  |
| `Landauer-Hitze` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 283 |  |
| `Mutual Information` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 2 | 283, 330 |  |
| `DKT` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#4] | 4 | 13 | 40, 174, 269, 288, 330, 449, 552, 616, 942, 947, 968 |  |
| `Monster Group M` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 331 |  |
| `Vertex Operator Algebra` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 331 |  |
| `VOA` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 331 |  |
| `Leech Lattice` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 331 |  |
| `Orbifold` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 331 |  |
| `Twisted Modules` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 331 |  |
| `Witness Function` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 2 | 286, 331 |  |
| `Zero-Knowledge Verifier` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 331 |  |
| `Husserlian Disinterested Spectator` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 2 | 331, 1734 |  |
| `Chaitin` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 2 | 286, 331 |  |
| `Gödel-Satz` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 2 | 286, 331 |  |
| `Gödel-Sentence` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 331 |  |
| `Gödel-Gambit` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 289 |  |
| `Monstrous-Moonshine` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 3 | 269, 552, 616 | `Monstrous-Moonshine-Mathematik` ×2 |
| `Moonshine-Link` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 910, 1300, 1634 |  |
| `Dialetheia` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 1246 |  |
| `Dialetheismus` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 552 |  |
| `Phoenix Collapse` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 152, 492, 779 |  |
| `Heuristics of Integration` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 2 | 152, 779 |  |
| `Storyform A` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#25] | 25 | 25 | 152, 284, 286, 403, 422, 767, 789, 904, 906, 908, 910, 1002 … |  |
| `Storyform B` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#33] | 33 | 33 | 15, 38, 152, 156, 284, 286, 306, 357, 492, 532, 631, 768 … |  |
| `Vortex-Inversion` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 11 | 178, 182, 285, 319, 770, 1109, 1202, 1240, 1278, 1366, 1678 | `Vortex-Inversions-Beat-Sheet` ×5, `Vortex-Inversions-Mechanik` ×2, `Vortex-Inversions-Pivot` ×1, `Vortex-Inversion-Beat-Sheet` ×1 |
| `Driver-Pivot` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 5 | 285, 1210, 1275, 1422, 1662 | `Driver-Pivot-Mechanik` ×2 |
| `Heat-Spike` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 2 | 1247, 1706 |  |
| `Convergence` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 2 | 1244, 1682 |  |
| `Rotation` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 7 | 283, 297, 1103, 1107, 1148, 1248, 1714 |  |
| `Stille` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#4] | 4 | 4 | 305, 1246, 1698 |  |
| `Phönix-Mode-Inversion` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#0] | 0 | 3 | 279, 293, 1386 | `Phönix-Mode-Inversion-getestete` ×1, `Phönix-Mode-Inversionsanalyse` ×1, `Phönix-Mode-Inversion-getragener` ×1 |
| `Klimax` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#10] | 10 | 14 | 285, 289, 319, 1004, 1063, 1109, 1216, 1236, 1256, 1277, 1304, 1422 … | `Klimax-Effekt` ×1, `Klimax-Ereignis` ×1, `Klimax-Doppel-Lesart` ×1 |
| `ANP` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 4 | 166, 556, 1075, 1245 |  |
| `ANP/EP-Buffering` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 556 |  |
| `funktionale Multiplizität` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 556 |  |
| `Janetian Action Systems` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 556 |  |
| `ANP-artige Façade` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 2 | 166, 1075 |  |
| `Alter` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 5 | 287, 309, 947, 1406, 1462 | `Alter-Namen` ×3, `alternative` ×1 |
| `Witness-Function-3-Layer` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 2 | 1256, 1279 |  |
| `Q-Entanglement` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 1256 |  |
| `Somatic Rulebook` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 942 |  |
| `Prose core principle` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 942 |  |
| `Hubble-Volumen` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 947 |  |
| `Halteproblem` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 947 |  |
| `Lex` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 947 |  |
| `Index` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 287, 309, 1406 |  |
| `Nox` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 287, 309, 1406 |  |
| `Echo` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 287, 309, 1406 |  |
| `Flicker` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 287, 309, 1406 |  |
| `Limina` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 287, 309, 1406 |  |
| `Praetor` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 287, 309, 1406 |  |
| `Eos` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 287, 309, 1406 |  |
| `Elara` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 287, 309, 1406 |  |
| `Aris` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 287, 309, 1406 |  |
| `Mina` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 287, 309, 1406 |  |
| `Lyra` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 287, 309, 1406 |  |
| `Soren` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 287, 309, 1406 |  |
| `Tariq` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 287, 309, 1406 |  |
| `Nova` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 287, 309, 1406 |  |
| `Sentinel` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 287, 309, 1406 |  |
| `Deus ex Machina` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 286 |  |
| `5D-Interferenz` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#4] | 4 | 5 | 896, 946, 1113, 1149 | `5D-Interferenz-Vergleich` ×1 |
| `H1` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#20] | 20 | 21 | 164, 217, 376, 631, 905, 948, 1032, 1044, 1071, 1087, 1109, 1118 … |  |
| `H2` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#18] | 18 | 18 | 165, 217, 376, 631, 948, 1032, 1055, 1071, 1088, 1109, 1120, 1142 … |  |
| `H3` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#14] | 14 | 19 | 166, 217, 376, 631, 1032, 1071, 1075, 1076, 1077, 1078, 1089, 1120 … |  |
| `H3a` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 1075 |  |
| `H3b` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 1076 |  |
| `H3c` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 1077 |  |
| `Surviving Branch` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#5] | 5 | 5 | 1150, 1172, 1186, 1574, 1594 |  |
| `Hypothesis Half-Life Audit` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#7] | 7 | 7 | 26, 984, 1016, 1024, 1450, 1786, 1794 |  |
| `Surviving-Branch Triangulation` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#5] | 5 | 5 | 25, 1158, 1450, 1790, 1802 |  |
| `Query Expansion Log` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#7] | 7 | 7 | 182, 516, 1354, 1446, 1766, 1836, 1844 |  |
| `Contradiction Log` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#13] | 13 | 13 | 21, 182, 275, 332, 397, 411, 520, 699, 805, 1350, 1438, 1762 … |  |
| `Reflection Entry` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#9] | 9 | 9 | 639, 715, 809, 875, 915, 927, 1132, 1265, 1308 |  |
| `Restatement Checkpoint` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#5] | 5 | 5 | 520, 639, 651, 915, 919 |  |
| `Pre-Synthesis Integrity Check` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#5] | 5 | 5 | 110, 207, 528, 1324, 1843 |  |
| `Bayesianischer Prior` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 1140 |  |
| `Cross-Pollination` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#9] | 9 | 10 | 182, 984, 986, 1158, 1160, 1362, 1418, 1450, 1782, 1844 | `Cross-Pollination-Audit` ×1 |
| `Reflection Baseline` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#4] | 4 | 4 | 27, 194, 659, 1835 |  |
| `Quellen-Hierarchie` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#4] | 4 | 4 | 28, 261, 608, 663 |  |
| `Canon-Inheritance` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 29, 277, 667 |  |
| `Output-Ausschlüsse` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#5] | 5 | 5 | 30, 299, 671, 1462, 1842 |  |
| `Dramatica-Legalität` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#4] | 4 | 5 | 31, 311, 675, 1097, 1147 | `Dramatica-Legalitäts-Vergleich` ×1 |
| `Bilingualer Begriffs-Kanon` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 3 | 32, 324, 679 |  |
| `Falsification` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#7] | 7 | 7 | 19, 332, 343, 691, 1012, 1082, 1438 |  |
| `Steelmanning` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#7] | 7 | 7 | 20, 217, 332, 370, 695, 1342, 1438 |  |
| `First-Principles Decomposition` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#6] | 6 | 6 | 22, 332, 424, 703, 837, 1438 |  |
| `Source Triangulation` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#8] | 8 | 8 | 23, 332, 451, 707, 848, 1186, 1438, 1839 |  |
| `Adversarial Query Expansion` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#10] | 10 | 10 | 24, 90, 124, 332, 478, 687, 1077, 1438, 1446, 1836 |  |
| `ReAct` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#4] | 4 | 7 | 24, 82, 84, 128, 144, 332 | `ReAct-Framework` ×1, `ReAct-Zyklus` ×1, `ReAct-Spine` ×1 |
| `RISEN` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#6] | 6 | 6 | 24, 126, 128, 144, 332 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Dramatica` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#15] | 15 | 60 | 15, 28, 31, 38, 40, 64, 152, 170, 174, 270, 311, 313 … | `Dramatica-Theorie` ×6, `Dramatica-Storyformen` ×4, `Dramatica-Legalität` ×4, `Dramatica-Dokumentation` ×4 |
| `Throughline` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#26] | 26 | 54 | 15, 25, 26, 38, 156, 178, 182, 216, 270, 318, 329, 548 … | `Throughlines` ×3, `Throughline-Durchgang` ×1, `Throughline-Encoding-Iterationen` ×1, `Throughline-Definitionen` ×1 |
| `Storypoint` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#6] | 6 | 27 | 31, 270, 293, 313, 321, 322, 357, 548, 767, 768, 789, 817 … | `Storypoints` ×6, `Storypoint-Konfiguration` ×5, `Storypoint-Legalität` ×1, `Storypoint-Ebenen` ×1 |
| `Storyform` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#62] | 62 | 102 | 15, 38, 152, 156, 178, 267, 284, 286, 297, 306, 319, 320 … | `Storyformen` ×14, `Storyform-Eigenschaft` ×1, `Storyform-A-Driver` ×1, `Storyform-Analyse` ×1 |
| `Main Character` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 3 | 368, 532, 841 |  |
| `Influence Character` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 842 |  |
| `Objective Story` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 843 |  |
| `Relationship Story` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 844 |  |
| `MC` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#76] | 76 | 95 | 64, 156, 160, 164, 165, 166, 270, 306, 317, 318, 322, 329 … |  |
| `IC` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#19] | 19 | 27 | 270, 286, 301, 306, 318, 329, 339, 422, 767, 771, 779, 799 … |  |
| `OS` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#38] | 38 | 46 | 64, 156, 164, 165, 166, 270, 306, 318, 322, 329, 368, 395 … |  |
| `RS` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#16] | 16 | 18 | 270, 306, 318, 329, 767, 801, 844, 858, 886, 910, 911, 1076 … |  |
| `Story-Mind` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#3] | 3 | 4 | 430, 548, 857 | `Story-Mind-Dynamik` ×1 |
| `Domain` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#14] | 14 | 29 | 156, 318, 321, 322, 329, 430, 548, 767, 798, 799, 800, 801 … | `Domain-Paar` ×2, `Domain-Inversion` ×2, `Domain-Verschiebung` ×1, `Domain-Pairing-Regeln` ×1 |
| `Universe` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#13] | 13 | 16 | 156, 318, 329, 430, 798, 799, 1044, 1051, 1067, 1117, 1118 | `Universe-Domain` ×3, `universelle` ×1 |
| `Physics` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#15] | 15 | 18 | 156, 164, 318, 329, 800, 801, 909, 910, 1055, 1067, 1117, 1118 … | `Physics-Domain` ×2, `Physics-als-System` ×1 |
| `Mind` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#12] | 12 | 21 | 60, 135, 259, 318, 329, 430, 548, 798, 799, 857, 1002, 1067 … | `mindestens` ×13, `Mindestens` ×3, `Mindeststandards` ×1, `Mindest-Erwartung` ×1 |
| `Psychology` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#14] | 14 | 14 | 318, 329, 800, 801, 908, 911, 1067, 1117, 1118, 1618, 1642 |  |
| `Concern` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#7] | 7 | 7 | 321, 329, 769, 940, 958, 1099 |  |
| `Issue` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#6] | 6 | 6 | 321, 329, 769, 940, 958, 1099 |  |
| `Problem` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#7] | 7 | 9 | 317, 321, 329, 769, 858, 940, 958, 1099 | `Problem-Solving` ×2, `problems` ×1 |
| `Solution` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#6] | 6 | 6 | 321, 329, 769, 940, 958, 1099 |  |
| `Symptom` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 321 |  |
| `Response` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 321 |  |
| `Catalyst` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 321 |  |
| `Inhibitor` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 321 |  |
| `Benchmark` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 321 |  |
| `Unique Ability` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 321 |  |
| `Critical Flaw` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 321 |  |
| `Resolve` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#4] | 4 | 4 | 329, 548, 767, 790 |  |
| `Growth` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#4] | 4 | 4 | 329, 548, 767, 791 |  |
| `Approach` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#6] | 6 | 6 | 317, 329, 430, 548, 767, 792 |  |
| `Do-er` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#4] | 4 | 4 | 317, 329, 792 |  |
| `Be-er` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#5] | 5 | 5 | 317, 329, 430, 792 |  |
| `Problem-Solving Style` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 2 | 317, 329 |  |
| `Linear` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#4] | 4 | 4 | 317, 329, 793 | `linearer` ×1 |
| `Holistic` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#4] | 4 | 4 | 317, 329, 793 |  |
| `Driver` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#18] | 18 | 27 | 285, 319, 329, 403, 422, 548, 612, 767, 794, 1004, 1200, 1210 … | `Driver-Pivot` ×3, `Driver-Pivot-Mechanik` ×2, `Driver-Korrektur` ×1, `Driver-Logik` ×1 |
| `Action` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#16] | 16 | 20 | 144, 285, 319, 329, 403, 422, 556, 794, 1004, 1210, 1215, 1216 … | `Actions` ×3 |
| `Decision` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#18] | 18 | 23 | 285, 319, 329, 403, 422, 794, 1004, 1210, 1214, 1216, 1248, 1273 … | `Decisions` ×3, `Decision-Pivot` ×2, `decision-driving` ×1 |
| `Limit` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#8] | 8 | 10 | 320, 329, 548, 767, 795, 1200, 1220, 1276, 1666, 1670 | `Limit-Spezifikation` ×1, `Limit-Uhren` ×1 |
| `Optionlock` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#6] | 6 | 6 | 320, 329, 795, 1224, 1666 |  |
| `Timelock` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#6] | 6 | 6 | 320, 329, 795, 1225, 1670 |  |
| `Outcome` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#10] | 10 | 10 | 284, 320, 329, 548, 767, 796, 1200, 1230, 1674 |  |
| `Success` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#8] | 8 | 8 | 284, 320, 329, 796, 1234, 1236, 1277 |  |
| `Failure` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#9] | 9 | 9 | 284, 320, 329, 796, 1109, 1235, 1236, 1277 |  |
| `Judgment` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#9] | 9 | 10 | 284, 320, 329, 548, 767, 797, 1200, 1230, 1674 | `Judgment-Doppel-Lesart` ×1 |
| `Good` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#8] | 8 | 8 | 284, 320, 329, 797, 1234, 1236, 1277 |  |
| `Bad` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#9] | 9 | 9 | 284, 320, 329, 797, 1109, 1235, 1236, 1277 |  |
| `TSDP` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#0] | 0 | 5 | 269, 556, 593, 604, 616 | `TSDP-Quellen` ×2, `TSDP-informierte` ×1, `TSDPAnalyse` ×1 |
| `Theory of Structural Dissociation` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 556 |  |
| `Landauer's Principle` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#1] | 1 | 1 | 552 |  |
| `autopoietisches System` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#4] | 4 | 4 | 439, 512, 862, 1050 |  |
| `Qualia` ^[research-prompt-dramatica-dual-storyform-synthese-aegis-thro.md:#2] | 2 | 2 | 439, 449 |  |

## What the extraction ran into

**Zeros, 2.** `Phönix-Mode-Inversion` and `TSDP` both stand 0 times alone (`read.py --count` says 0 whole word, case-insensitive 0) and appear only inside longer hyphenated or glued words: `Phönix-Mode-Inversion-getestete`, `Phönix-Mode-Inversionsanalyse` and `Phönix-Mode-Inversion-getragener` (3 in), and `TSDP-Quellen`, `TSDP-informierte` and `TSDPAnalyse` (5 in, one of them a file name with the export gluing the words). Both are inflection or compounding, not absence: the document uses the term, only never alone.

**Standing alone less often than with compounds, 47.** The fact lists them; reading the surfaces shows the pattern is mostly hyphen compounds that name a method or a section (`AEGIS-Frage`, `AEGIS-Throughline-Verortung`, `Storypoint` in `Storypoint-Inventar-Tabelle`) and, for the short Dramatica symbols `MC`, `IC`, `OS`, `RS`, the symbols inside compounds such as `MC-Throughline` and `MC-Guardian`. Short symbols (`H1`, `K0`, `K1`, `MC`, `OS`) also stand inside other words, which the substring mark says.

**Export artifacts.** 519 backslash escapes (`\_` in file names, `\[` and `\]` in the report templates, `\>` in the constraint list at L28) and 135 glued reference numbers in the profile. The glued numbers matter for two candidates: `read.py --find` drops digits glued to words, so it prints `K` for `K0` and `K1` (L283) and `H` for `H1` (L164); the counts for `K0`, `K1`, `H1`, `H2`, `H3` come from the raw file. The file name `Coherence-Protocol-synthesis\_pdf.pdf` is written in the export with an escaped underscore and was not listed.

**Compound and suspended forms.** `Kairos/Sophia` is listed joined and as `Kairos` and `Sophia`. `Erasure Kernel` is written in the line as „Erasure Kernel / Kollaps-Kern (K0)“ ^[L330], so both halves are listed; `Coherence Kernel (K1)` is listed as `Coherence Kernel`, `K1`. `Algorithmische Melancholie` and `Algorithmischer Melancholie` are two inflected surfaces of one name and both are listed. The Dramatica terms are listed under `## lens` because the prompt applies them to the novel's two storyforms.

**The de-canonised names.** The fifteen names in the exclusion lists (L287, L309, L1406) are listed as candidates because the document names them; each stands exactly three times, all inside those lists. They are listed names of figures the prompt forbids using, not figures it describes.

**Claims about its own standing.** The prompt calls the Final Architecture Validation PDF the „bindende Projekt-Kanon“ ^[L279] and elsewhere names the same PDF `Quasi-Hauptkanon` (L580). It also writes that Storyform A and B are „gleich-kanonisch“ ^[L1414]. These are claims inside a prompt for another AI. They are recorded and not applied.

**One exclusion is a constraint, nothing more.** The prompt's output exclusions include an anchor it forbids naming: „Den autobiografischen Anker explizit benennen.“ ^[L305] It is not on the candidate list, and the census says nothing further about it.

**Internal tension.** The prompt states, for the Dramatica legality rules, „MC und OS belegen jeweils das vertikal gegenüberliegende Domain-Paar“ ^[L318]; its own Storyform A assignment at L1117 gives MC a Mind domain and OS a Psychology domain. Recorded in the note; the census applies neither.

**Template labels.** The six-times-repeated labels in the profile (`Example trigger in this research context`, `How to apply it — step by step`, `Sub-Steps`, `What it is`, `When to stop / escape criterion`, `Why it is in this prompt`, `Ziel`) are the template of the method blocks and steps, and are not terms.

**Zeros:** 2 — `Phönix-Mode-Inversion`, `TSDP`.

**Standing alone less often than with compounds:** 47 — `AEGIS` 51/85, `Kael` 12/17, `Juna` 7/17, `Juna-Asymmetrie` 2/3, `Guardian` 9/21, `Mnemosyne` 3/7, `Wächter-Zwiespalt` 2/4, `Truth-Rotation` 3/5, `Kollaps-Kern` 2/4, `K0` 3/8, `K1` 3/4, `Coheron` 1/3, `Erason` 1/4, `DKT` 4/13, `Monstrous-Moonshine` 1/3, `Vortex-Inversion` 2/11, `Driver-Pivot` 3/5, `Rotation` 2/7, `Klimax` 10/14, `ANP` 2/4, `Alter` 2/5, `5D-Interferenz` 4/5, `H1` 20/21, `H3` 14/19, `Cross-Pollination` 9/10, `Dramatica-Legalität` 4/5, `ReAct` 4/7, `Dramatica` 15/60, `Throughline` 26/54, `Storypoint` 6/27, `Storyform` 62/102, `Main Character` 2/3, `MC` 76/95, `IC` 19/27, `OS` 38/46, `RS` 16/18, `Story-Mind` 3/4, `Domain` 14/29, `Universe` 13/16, `Physics` 15/18 ….
