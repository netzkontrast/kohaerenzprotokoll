---
source: Sources/drive/openai-math-contents.md
drive_id: "github:openai/math@adc7f12/CONTENTS.md"
title: "OpenAI math — Mathematics manuscript collection (manuscript map)"
category: theorie-mathematik
index_date: "2026-10-06"
extracted: "2026-10-07"
candidates: 202    # the terms capture.py counted
---

# Term census — OpenAI math — Mathematics manuscript collection (manuscript map)

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py openai-math-contents`

```
  lines                3708  (frontmatter ends at 9)
  body words           67493
  headings             2   bold-only lines 1
  table rows           0   code fences 0
  question marks       0
  backslash escapes    0
  typographic marks    623   ascii quotes 0
  invisible characters none
  math symbol lines    24
  glued ref numbers    11
  repeated labels      none
  longest line         1143 chars
```

## Stance, read per passage

The text is a catalogue and never argues: each passage below is one kind of line, and the kind is its stance. Quotations are English, as written.

**Opening and orientation, L11 to L21.** The file names itself, „Mathematics manuscript collection“ ^[L11], states one total in bold, „722 manuscripts covering 372 result families.“ ^[L13], points to a PDF, „Read the overview PDF“ ^[L15], and heads the rest „Manuscript map“ ^[L17]. Its only statement about its own layout is „Each result description is followed by its constituent manuscripts and their abstracts.“ ^[L19] This is an index's orientation: it plans the reader's route and asserts no result. **Observed:** L21 is a leftover HTML header cell of the removed table (profile: table rows 0), the one trace of the original markup.

**Family headings and their descriptions (L23 to L3702).** Each of the numbered families opens with a bold number, a title and a one-paragraph description in the document's own voice, in the third person and the present tense, reporting a result as achieved: „Proves Milne's rationality conjecture for abelian varieties“ ^[L23]. The verbs that carry this are `Proves` ^[openai-math-contents.md:#165], `Resolves` ^[openai-math-contents.md:#41], `Constructs` ^[openai-math-contents.md:#44] and `Disproves` ^[openai-math-contents.md:#18], as counted whole words; a refutation is reported in the same voice, „Constructs a singular normal affine complex surface with free rank-two tangent sheaf“ ^[L543]. The headings write their own numbering, and the tail of many descriptions carries a link label, `Lean` ^[openai-math-contents.md:#235], with a path to a file beside the description. The document does not say what that file is or what it checks; the label is all it gives.

**Paper-title lines and abstracts.** Under each family description, a line with the paper's title as link text and a PDF path, then the abstract in the first person plural, a report of what the manuscript itself claims: „We prove Milne's rationality conjecture for abelian varieties“ ^[L27]. So each family has two voices, the description (the collection's summary of the family) and the abstract (the manuscript's own voice). **Observed:** each PDF path runs through a folder whose name ends in a month, day and year (for instance in L25), and the title lines are counted by `grep` in `05-verify.txt`.

**Limits and hedges stated inside abstracts.** The descriptions and abstracts often say what a result does not claim: „it does not assert classical modularity“ ^[L113], „The result does not assert ellipticity, Arthur-packet classification, or a multiplicity formula.“ ^[L153], „The theorem concerns existing flip sequences; it does not assert the existence of all contractions or flips.“ ^[L607], „The proof is nonquantitative and does not supply explicit constants.“ ^[L1733], „We give no quantitative bound on the required depth or efficient angle-selection procedure.“ ^[L2875]. `does not assert` ^[openai-math-contents.md:#4] and `do not assert` ^[openai-math-contents.md:#1] stand in five places together. A hypothesis is also named as open: „The existence of the initial correspondence remains a hypothesis.“ ^[L349].

**Conditional results.** Some abstracts prove a theorem only under inputs stated elsewhere, in the manuscript's own formulation: „Assuming the stated deterministic critical-reference estimates, we prove“ ^[L2091]. `Assuming` ^[openai-math-contents.md:#8] stands in eight places. The conditions are the manuscript's; the document only reports them.

**Reports of other texts and people.** The document credits and cites others in its descriptions and abstracts: „We credit Gaia Carenini with priority for resolving the threshold-existence conjecture“ ^[L2309], with `priority` ^[openai-math-contents.md:#3] standing three times; „This conclusion was previously announced by Cao–Deng–Hacon–Păun.“ ^[L633]; and one description opens „Gives an alternative to“ ^[L3011] a construction by another author, whose name is written inside a link text. In each of these lines the credit, the announcement or the earlier construction is the other party's, and the document is the one reporting it.

**Cross-references between families.** One family points at another by its number: „Together with result 032“ ^[L23] and „With result 006“ ^[L29]. `Together with` ^[openai-math-contents.md:#13] and `companion` ^[openai-math-contents.md:#35] recur in the document's sentences about related manuscripts.

**A manuscript marked as secondary.** One link is labelled by the collection itself as `secondary writeup` ^[openai-math-contents.md:#1] (L1095), the only manuscript so labelled.

## Candidates and counts

202 candidates, written while reading and frozen by the count (`Plan/runs/openai-math-contents/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `openai-math-contents.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Mathematics manuscript collection` ^[openai-math-contents.md:#1] | 1 | 1 | 11 |  |
| `Manuscript map` ^[openai-math-contents.md:#1] | 1 | 1 | 17 |  |
| `result families` ^[openai-math-contents.md:#1] | 1 | 1 | 13 |  |
| `Lean` ^[openai-math-contents.md:#235] | 235 | 235 | 43, 67, 83, 89, 95, 137, 143, 183, 215, 241, 247, 259 … |  |
| `secondary writeup` ^[openai-math-contents.md:#1] | 1 | 1 | 1095 |  |
| `companion paper` ^[openai-math-contents.md:#8] | 8 | 9 | 165, 303, 973, 1405, 2017, 2047, 2321, 2503, 3319 |  |
| `Milne's rationality conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 23, 25, 27 |  |
| `Birch–Swinnerton-Dyer` ^[openai-math-contents.md:#4] | 4 | 4 | 29, 31, 33, 39 |  |
| `Selmer corank` ^[openai-math-contents.md:#3] | 3 | 5 | 29, 39, 41, 65, 77 |  |
| `quasi-Riemann hypothesis` ^[openai-math-contents.md:#4] | 4 | 4 | 43, 47, 51 |  |
| `Landau–Siegel zeros` ^[openai-math-contents.md:#3] | 3 | 3 | 51, 53, 55 |  |
| `Hilbert's tenth problem` ^[openai-math-contents.md:#2] | 2 | 2 | 57, 61 |  |
| `Catalan's constant` ^[openai-math-contents.md:#3] | 3 | 3 | 67, 69, 71 |  |
| `Goldfeld's conjecture` ^[openai-math-contents.md:#1] | 1 | 1 | 73 |  |
| `Chowla conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 83, 87 |  |
| `corrected Elliott conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 83, 87 |  |
| `Deligne–Drinfeld conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 89, 93 |  |
| `Bogomolov–Pop reconstruction` ^[openai-math-contents.md:#3] | 3 | 3 | 95, 99, 107 |  |
| `Fontaine–Mazur` ^[openai-math-contents.md:#3] | 3 | 3 | 109, 119, 121 |  |
| `Emerton's dimension conjecture` ^[openai-math-contents.md:#1] | 1 | 1 | 117 |  |
| `Ford–Konyagin–Luca conjecture` ^[openai-math-contents.md:#1] | 1 | 1 | 123 |  |
| `Erdős–Pomerance joint Dickman conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 137, 141 |  |
| `Ostmann's inverse Goldbach conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 143, 147 |  |
| `restricted geometric Langlands` ^[openai-math-contents.md:#3] | 3 | 3 | 149, 157, 169 |  |
| `Ramanujan` ^[openai-math-contents.md:#11] | 11 | 14 | 149, 153, 159, 161, 165, 1691, 1693, 1695 | `Ramanujan-Arthur` ×1, `Ramanujan-Arthur-Decompositions-of-Cuspidal-Functions-at-Full-Finite-Level-September-24-2026` ×1 |
| `Zilber–Pink` ^[openai-math-contents.md:#9] | 9 | 9 | 197, 199, 201, 203, 205, 209, 211, 213 |  |
| `Flint–Hills series` ^[openai-math-contents.md:#2] | 2 | 2 | 215, 219 |  |
| `Margulis–Platonov conjecture` ^[openai-math-contents.md:#6] | 6 | 6 | 221, 223, 225, 227, 229 |  |
| `section conjecture` ^[openai-math-contents.md:#5] | 5 | 6 | 231, 237, 239, 1749 |  |
| `Jacobsthal's function` ^[openai-math-contents.md:#1] | 1 | 1 | 249 |  |
| `Duffin–Schaeffer conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 253, 257 |  |
| `Patterson's first moment` ^[openai-math-contents.md:#1] | 1 | 1 | 259 |  |
| `Egyptian fractions` ^[openai-math-contents.md:#3] | 3 | 3 | 271, 273 |  |
| `Gaussian moat conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 289, 293 |  |
| `Artin's primitive root conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 295, 299 |  |
| `Uchida's conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 311, 315 |  |
| `Hodge conjecture` ^[openai-math-contents.md:#10] | 10 | 12 | 317, 319, 321, 327, 329, 331, 333, 337, 339, 341 |  |
| `Kuga–Satake` ^[openai-math-contents.md:#11] | 11 | 11 | 317, 323, 325, 331, 333, 347, 349 |  |
| `Iitaka subadditivity` ^[openai-math-contents.md:#11] | 11 | 11 | 351, 353, 355, 365, 367, 373, 375, 377, 385 |  |
| `log abundance` ^[openai-math-contents.md:#7] | 7 | 7 | 373, 377, 389, 401, 431, 435 |  |
| `Fujita's freeness conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 469, 471, 473 |  |
| `Nagata's conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 477, 479 |  |
| `Seshadri constants` ^[openai-math-contents.md:#4] | 4 | 4 | 475, 481, 489 |  |
| `Bloch's conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 493, 497 |  |
| `strong hyperkähler SYZ conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 499, 505, 507 |  |
| `Hikita conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 521, 523, 525 |  |
| `Shafarevich` ^[openai-math-contents.md:#12] | 12 | 13 | 29, 33, 37, 41, 65, 77, 527, 531, 533, 535 |  |
| `Zariski cancellation` ^[openai-math-contents.md:#1] | 1 | 1 | 537 |  |
| `Lipman–Zariski` ^[openai-math-contents.md:#3] | 3 | 3 | 543, 547 |  |
| `Stable Coordinate conjecture` ^[openai-math-contents.md:#1] | 1 | 1 | 549 |  |
| `Abhyankar–Sathaye` ^[openai-math-contents.md:#3] | 3 | 3 | 549, 553, 557 |  |
| `Griffiths' positivity conjecture` ^[openai-math-contents.md:#1] | 1 | 1 | 559 |  |
| `Kobayashi's canonical-ampleness conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 565, 569 |  |
| `Beauville's splitting conjecture` ^[openai-math-contents.md:#1] | 1 | 1 | 571 |  |
| `Pixton completeness` ^[openai-math-contents.md:#2] | 2 | 2 | 581, 583 |  |
| `Kuznetsov's rationality conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 587, 591 |  |
| `Bridgeland stability` ^[openai-math-contents.md:#4] | 4 | 4 | 593, 597, 601 |  |
| `Campana's abelianity conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 625, 629 |  |
| `Kollár–Pardon conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 639, 643 |  |
| `Zariski's multiplicity conjecture` ^[openai-math-contents.md:#1] | 1 | 1 | 649 |  |
| `Global Spherical Shell conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 659, 663 |  |
| `LeBrun–Salamon conjecture` ^[openai-math-contents.md:#4] | 4 | 4 | 665, 667, 669 |  |
| `generalized Mukai conjecture` ^[openai-math-contents.md:#4] | 4 | 4 | 671, 673, 675 |  |
| `Virasoro conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 683, 691 |  |
| `Shokurov's bounded-klt-complement conjecture` ^[openai-math-contents.md:#1] | 1 | 1 | 697 |  |
| `Campana–Peternell conjecture` ^[openai-math-contents.md:#4] | 4 | 4 | 703, 705, 707 |  |
| `quantum geometric Langlands` ^[openai-math-contents.md:#4] | 4 | 4 | 739, 741, 743 |  |
| `Koebe's circle-domain conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 745, 753 |  |
| `Brennan's conjecture` ^[openai-math-contents.md:#4] | 4 | 4 | 755, 757, 759 |  |
| `Falconer distance conjecture` ^[openai-math-contents.md:#4] | 4 | 4 | 765, 767, 769 |  |
| `Kakeya` ^[openai-math-contents.md:#6] | 6 | 8 | 771, 773, 775, 777, 779 |  |
| `Bochner–Riesz` ^[openai-math-contents.md:#6] | 6 | 6 | 811, 813, 815 |  |
| `local smoothing` ^[openai-math-contents.md:#5] | 5 | 5 | 809, 817, 819, 821 |  |
| `Carleson` ^[openai-math-contents.md:#3] | 3 | 3 | 823, 827, 831 |  |
| `Erdős similarity conjecture` ^[openai-math-contents.md:#6] | 6 | 6 | 859, 861, 863, 865, 867 |  |
| `Mahler conjecture` ^[openai-math-contents.md:#4] | 4 | 6 | 881, 883, 885, 889, 893 |  |
| `Petty's projection-volume conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 895, 899 |  |
| `Lax conjecture` ^[openai-math-contents.md:#4] | 4 | 4 | 961, 965, 969 |  |
| `Gaussian propeller conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 975, 979 |  |
| `Steinitz–Bergström` ^[openai-math-contents.md:#3] | 3 | 3 | 981, 983, 985 |  |
| `Unique Games Conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 1031, 1035 |  |
| `Lang–Plaut problem` ^[openai-math-contents.md:#2] | 2 | 2 | 987, 991 |  |
| `edit distance` ^[openai-math-contents.md:#5] | 5 | 5 | 993, 997, 1217, 1221 |  |
| `2-to-1 Games Conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 1077, 1081 |  |
| `mean-payoff games` ^[openai-math-contents.md:#4] | 4 | 4 | 1059, 1063, 1069, 1073 |  |
| `Brunn–Minkowski` ^[openai-math-contents.md:#6] | 6 | 6 | 933, 935, 937 |  |
| `isotropic constant` ^[openai-math-contents.md:#4] | 4 | 6 | 1025, 1027, 1029 |  |
| `Turyn's` ^[openai-math-contents.md:#2] | 2 | 2 | 787, 799 |  |
| `Littlewood polynomials` ^[openai-math-contents.md:#6] | 6 | 6 | 787, 789, 791, 793, 797 |  |
| `Courtade–Kumar conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 1201, 1205 |  |
| `Hellinger conjecture` ^[openai-math-contents.md:#2] | 2 | 3 | 1201, 1209 |  |
| `Sensitivity Conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 1297, 1301 |  |
| `Weisfeiler–Leman` ^[openai-math-contents.md:#9] | 9 | 10 | 1303, 1305, 1307, 1309, 1311, 1313, 1315, 1317, 1319 |  |
| `Hilbert's sixteenth problem` ^[openai-math-contents.md:#3] | 3 | 3 | 1407, 1411 |  |
| `Banach's simple Lebesgue-spectrum problem` ^[openai-math-contents.md:#2] | 2 | 2 | 1417, 1421 |  |
| `Rokhlin's multiple-mixing problem` ^[openai-math-contents.md:#3] | 3 | 3 | 1423, 1425, 1427 |  |
| `Birkhoff conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 1435, 1443 |  |
| `Borsuk's conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 1517, 1521 |  |
| `Hadwiger's conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 1523, 1525, 1527 |  |
| `Hadwiger–Nelson problem` ^[openai-math-contents.md:#1] | 1 | 1 | 1537 |  |
| `Sidorenko's conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 1559, 1561, 1563 |  |
| `Ryser's covering conjecture` ^[openai-math-contents.md:#4] | 4 | 4 | 1565, 1569, 1571, 1573 |  |
| `Hindman's finite sums and products conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 1575, 1579 |  |
| `Harary–Hill conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 1581, 1585 |  |
| `Zarankiewicz` ^[openai-math-contents.md:#3] | 3 | 3 | 1581, 1591 |  |
| `distinct-distances conjecture` ^[openai-math-contents.md:#4] | 4 | 4 | 1595, 1597, 1599 |  |
| `Seymour's second-neighborhood conjecture` ^[openai-math-contents.md:#1] | 1 | 1 | 1649 |  |
| `Kahn–Kalai conjecture` ^[openai-math-contents.md:#4] | 4 | 4 | 1679, 1681, 1683 |  |
| `Barnette's conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 1703, 1707 |  |
| `Kaplansky's zero-divisor conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 1819, 1823 |  |
| `Auslander–Reiten conjecture` ^[openai-math-contents.md:#1] | 1 | 1 | 1853 |  |
| `Donovan's conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 1881, 1885 |  |
| `Saxl's conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 1897, 1905 |  |
| `Foulkes' conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 1943, 1945, 1947 |  |
| `Kadison's similarity conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 2929, 2933 |  |
| `Toms–Winter` ^[openai-math-contents.md:#4] | 4 | 4 | 2959, 2967, 2971, 2975 |  |
| `bicentralizer conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 2949, 2953 |  |
| `Cannon's conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 2493, 2497 |  |
| `Boone–Higman conjecture` ^[openai-math-contents.md:#4] | 4 | 4 | 2521, 2523, 2525, 2529 |  |
| `Thompson's group F` ^[openai-math-contents.md:#4] | 4 | 4 | 2509, 2511, 2513 |  |
| `Kervaire conjecture` ^[openai-math-contents.md:#1] | 1 | 1 | 2585 |  |
| `Hilbert–Smith conjecture` ^[openai-math-contents.md:#4] | 4 | 4 | 3061, 3063, 3065 |  |
| `Hovey–Strickland conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 3119, 3123 |  |
| `Singer conjecture` ^[openai-math-contents.md:#4] | 4 | 4 | 3143, 3145, 3147 |  |
| `Curtis's conjecture` ^[openai-math-contents.md:#1] | 1 | 1 | 3153 |  |
| `Borel conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 3189, 3193 |  |
| `Tingley's problem` ^[openai-math-contents.md:#2] | 2 | 2 | 3201, 3205 |  |
| `Crouzeix conjecture` ^[openai-math-contents.md:#4] | 4 | 4 | 3223, 3227, 3231 |  |
| `Yau's uniformization conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 3349, 3353 |  |
| `Katok's entropy rigidity conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 3355, 3359 |  |
| `nearby Lagrangian conjecture` ^[openai-math-contents.md:#4] | 4 | 4 | 3361, 3363, 3365 |  |
| `Blaschke conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 3389, 3393 |  |
| `Arnold conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 3427, 3431 |  |
| `Penrose inequality` ^[openai-math-contents.md:#17] | 17 | 17 | 2609, 2611, 2625, 2631, 2633, 2639, 2641, 2643, 2645, 2647, 2649, 2651 … |  |
| `Anderson model` ^[openai-math-contents.md:#2] | 2 | 2 | 2667 |  |
| `Lieb–Thirring` ^[openai-math-contents.md:#8] | 8 | 8 | 2677, 2679, 2681, 2683, 2685, 2687, 2689 |  |
| `Haldane gap` ^[openai-math-contents.md:#3] | 3 | 3 | 2761, 2763 |  |
| `strong cosmic censorship` ^[openai-math-contents.md:#1] | 1 | 1 | 2705 |  |
| `Bose–Einstein condensation` ^[openai-math-contents.md:#5] | 5 | 5 | 2739, 2741, 2743, 2759 |  |
| `Sherrington–Kirkpatrick` ^[openai-math-contents.md:#22] | 22 | 22 | 2069, 2071, 2073, 2075, 2077, 2211, 2213, 2217, 2219, 2221, 2223, 2225 … |  |
| `Schramm–Loewner evolution` ^[openai-math-contents.md:#1] | 1 | 1 | 2271 |  |
| `Mézard–Parisi` ^[openai-math-contents.md:#4] | 4 | 4 | 2129, 2131, 2133 |  |
| `De Giorgi's conjecture` ^[openai-math-contents.md:#4] | 4 | 4 | 3659, 3661, 3663 |  |
| `Navier–Stokes` ^[openai-math-contents.md:#8] | 8 | 8 | 3665, 3673, 3675, 3687, 3691, 3693, 3697, 3701 |  |
| `hot spots conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 3623, 3627 |  |
| `Lane–Emden conjecture` ^[openai-math-contents.md:#2] | 2 | 3 | 3629, 3633 |  |
| `Mumford–Shah` ^[openai-math-contents.md:#4] | 4 | 4 | 3601, 3603, 3605 |  |
| `Ball–Evans approximation problem` ^[openai-math-contents.md:#4] | 4 | 4 | 3613, 3617, 3621 |  |
| `Calderón problem` ^[openai-math-contents.md:#2] | 2 | 2 | 3593, 3599 |  |
| `Bernoulli problem` ^[openai-math-contents.md:#2] | 2 | 2 | 3607, 3611 |  |
| `Brenier maps` ^[openai-math-contents.md:#1] | 1 | 1 | 3653 |  |
| `Gaia Carenini` ^[openai-math-contents.md:#3] | 3 | 3 | 2309, 2313, 2325 |  |
| `Tanaka` ^[openai-math-contents.md:#1] | 1 | 1 | 3011 |  |
| `ECCC` ^[openai-math-contents.md:#1] | 1 | 1 | 2309 |  |
| `Schramm` ^[openai-math-contents.md:#17] | 17 | 17 | 745, 749, 1993, 2001, 2003, 2007, 2161, 2177, 2267, 2271, 2275, 2283 … |  |
| `Erdős` ^[openai-math-contents.md:#36] | 36 | 36 | 127, 137, 141, 265, 269, 271, 275, 277, 281, 799, 859, 861 … |  |
| `Khot` ^[openai-math-contents.md:#2] | 2 | 2 | 1031, 1077 |  |
| `Oka classification` ^[openai-math-contents.md:#1] | 1 | 1 | 509 |  |
| `overview PDF` ^[openai-math-contents.md:#1] | 1 | 1 | 15 |  |
| `constituent manuscripts` ^[openai-math-contents.md:#1] | 1 | 1 | 19 |  |
| `Paper titles` ^[openai-math-contents.md:#1] | 1 | 1 | 19 |  |
| `counterexample` ^[openai-math-contents.md:#56] | 56 | 92 | 527, 533, 543, 549, 553, 557, 559, 563, 581, 583, 895, 901 … | `counterexamples` ×14, `Counterexamples` ×12, `Counterexamples-to-weak-chromatic-splitting-sphere-kernels-and-descent-exponents-September-27-2026` ×1, `Counterexamples-to-the-Hahn-Wilson-conjecture-at-height-two-September-26-2026` ×1 |
| `computer-assisted` ^[openai-math-contents.md:#1] | 1 | 1 | 2733 |  |
| `interval arithmetic` ^[openai-math-contents.md:#2] | 2 | 2 | 927, 931 |  |
| `verification pipeline` ^[openai-math-contents.md:#1] | 1 | 1 | 2733 |  |
| `exact certificate` ^[openai-math-contents.md:#1] | 1 | 1 | 2737 |  |
| `deduction traces` ^[openai-math-contents.md:#1] | 1 | 1 | 1777 |  |
| `alternative proof` ^[openai-math-contents.md:#2] | 2 | 2 | 2313, 2957 |  |
| `independent proof` ^[openai-math-contents.md:#1] | 1 | 1 | 633 |  |
| `companion` ^[openai-math-contents.md:#35] | 35 | 35 | 43, 165, 213, 303, 337, 973, 1005, 1123, 1405, 1439, 1723, 1917 … |  |
| `priority` ^[openai-math-contents.md:#3] | 3 | 3 | 2309, 2313, 2325 |  |
| `NP-hard` ^[openai-math-contents.md:#13] | 13 | 15 | 975, 1031, 1039, 1043, 1047, 1051, 1077, 1081, 1083, 1087, 1185, 1189 … | `NP-hardness` ×2 |
| `quasipolynomial` ^[openai-math-contents.md:#7] | 7 | 16 | 1063, 1065, 1067, 1069, 1071, 1073, 1075, 1223, 1225, 1227, 1231, 1543 | `quasipolynomial-time` ×5, `Quasipolynomial-Bounds-for-Arithmetic-Progressions-September-23-2026` ×1 |
| `Poisson–Dirichlet` ^[openai-math-contents.md:#2] | 2 | 2 | 123, 131 |  |
| `Hanner polytopes` ^[openai-math-contents.md:#2] | 2 | 2 | 881, 885 |  |
| `Gaussian free field` ^[openai-math-contents.md:#15] | 15 | 15 | 2051, 2067, 2197, 2199, 2201, 2283, 2287, 2289, 2291, 2295, 2297, 2301 |  |
| `Liouville quantum gravity` ^[openai-math-contents.md:#4] | 4 | 4 | 1953, 1961, 1969, 1977 |  |
| `conformal loop ensemble` ^[openai-math-contents.md:#2] | 2 | 2 | 1969, 1973 |  |
| `measure rigidity` ^[openai-math-contents.md:#1] | 1 | 1 | 191 |  |
| `Bott–Chern cohomology` ^[openai-math-contents.md:#2] | 2 | 2 | 441, 445 |  |
| `Fourier restriction` ^[openai-math-contents.md:#3] | 3 | 3 | 801, 803, 805 |  |
| `Unique Games Theorem` ^[openai-math-contents.md:#1] | 1 | 1 | 1033 |  |
| `Hodge standard conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 317, 329 |  |
| `Tate conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 317, 329 |  |
| `Riemann hypothesis` ^[openai-math-contents.md:#0] | 0 | 4 | 43, 47, 51 |  |
| `Szemerédi` ^[openai-math-contents.md:#3] | 3 | 3 | 1543, 1735, 1743 |  |
| `van der Waerden numbers` ^[openai-math-contents.md:#2] | 2 | 2 | 1553 |  |
| `Ramsey number` ^[openai-math-contents.md:#5] | 5 | 9 | 1623, 1627, 1631, 1633, 1637, 1639, 1641, 1773, 1775 |  |
| `Kaplansky's direct-finiteness conjecture` ^[openai-math-contents.md:#2] | 2 | 2 | 1833, 1841 |  |
| `Baum–Connes` ^[openai-math-contents.md:#7] | 7 | 7 | 2899, 2901, 2903, 2909, 2911 |  |
| `Kadison–Kastler` ^[openai-math-contents.md:#5] | 5 | 5 | 2935, 2937, 2939, 2947 |  |
| `Jiang–Su stability` ^[openai-math-contents.md:#9] | 9 | 9 | 2959, 2963, 2969, 2971, 3023, 3045, 3053 |  |
| `Zauner` ^[openai-math-contents.md:#2] | 2 | 2 | 2729, 2733 |  |
| `mutually unbiased bases` ^[openai-math-contents.md:#4] | 4 | 4 | 2729, 2731, 2737 |  |
| `Hamiltonian fixed points` ^[openai-math-contents.md:#3] | 3 | 3 | 3411, 3415, 3423 |  |
| `Ricci flow` ^[openai-math-contents.md:#5] | 5 | 5 | 3467, 3469, 3471, 3473, 3475 |  |
| `Calabi flow` ^[openai-math-contents.md:#4] | 4 | 4 | 3481, 3483, 3485 |  |
| `Cartan–Hadamard` ^[openai-math-contents.md:#5] | 5 | 5 | 3339, 3341, 3343, 3347 |  |
| `Kerr` ^[openai-math-contents.md:#13] | 13 | 19 | 2623, 2625, 2629, 2631, 2633, 2705, 2707, 2709, 2711, 2713, 2715, 2717 |  |
| `Alperin weight conjecture` ^[openai-math-contents.md:#3] | 3 | 3 | 1875, 1879 |  |
| `Cohen–Macaulay` ^[openai-math-contents.md:#6] | 6 | 6 | 1813, 1815, 1817 |  |
| `Gersten's conjecture` ^[openai-math-contents.md:#4] | 4 | 4 | 1935, 1937, 2593, 2597 |  |

## What the extraction ran into

**Zeros:** 1 — `Riemann hypothesis`.

**Standing alone less often than with compounds:** 17 — `companion paper` 8/9, `Selmer corank` 3/5, `Ramanujan` 11/14, `section conjecture` 5/6, `Hodge conjecture` 10/12, `Shafarevich` 12/13, `Kakeya` 6/8, `Mahler conjecture` 4/6, `isotropic constant` 4/6, `Hellinger conjecture` 2/3, `Weisfeiler–Leman` 9/10, `Lane–Emden conjecture` 2/3, `counterexample` 56/92, `NP-hard` 13/15, `quasipolynomial` 7/16, `Ramsey number` 5/9, `Kerr` 13/19.

**The one zero is a hyphen, not an absence.** `Riemann hypothesis` stands 0 times alone and 4 times inside the compound `quasi-Riemann hypothesis` ^[openai-math-contents.md:#4] (L43, L47, L51): a hyphen on its left, so the compound is the document's own name for the result, and `Riemann zeta function` ^[openai-math-contents.md:#1] is a separate phrase. Of the 202 listed terms, this is the only row with a zero in the first column. The term was a surface I took from the family title and wrote shorter than the document writes it.

**Counts that differ between `word` and `in`, by cause.** Each case was read on its lines.

Plural forms, one or more letters longer: `companion papers` ^[openai-math-contents.md:#1] (L2047) against `companion paper` 8/9; `Hodge conjectures` ^[openai-math-contents.md:#2] (L331, L333) against 10/12; `Mahler conjectures` ^[openai-math-contents.md:#2] (both on L881) against 4/6; `isotropic constants` ^[openai-math-contents.md:#2] (L1025, L1027) against 4/6; `Hellinger conjectures` ^[openai-math-contents.md:#1] (L1201) against 2/3; `Ramsey numbers` ^[openai-math-contents.md:#4] (L1623, L1631, L1773, L1775) against 5/9; and `Hénon–Lane–Emden conjectures` ^[openai-math-contents.md:#1] (L3629) against `Lane–Emden conjecture` 2/3, whose two standing-alone occurrences are L3629 and the `Hénon–Lane–Emden conjecture` ^[openai-math-contents.md:#1] of L3633.

A hyphen glued to the term, which `word` excludes: `k-Weisfeiler–Leman` ^[openai-math-contents.md:#1] (L1315) against `Weisfeiler–Leman` 9/10; `NP-hardness` ^[openai-math-contents.md:#2] against `NP-hard` 13/15; `quasipolynomial-time` ^[openai-math-contents.md:#5] against `quasipolynomial` 7/16, whose remaining four are in the lowercase paper-path slugs of the PDF links; `Near-Kerr` ^[openai-math-contents.md:#1] (L2715) and five paper-path slugs against `Kerr` 13/19, where `Kerr–Newman` ^[openai-math-contents.md:#6] with its en dash is inside the 13; `Ramanujan-Arthur` and two slugs (L159, L1693) against `Ramanujan` 11/14, where `Ramanujan–Arthur` ^[openai-math-contents.md:#2] with an en dash is inside the 11; two paper-path slugs against `Kakeya` 6/8 (L773, L777); and `Selmer corank` 3/5, where two occurrences (L65, L77) are joined by a hyphen to a formula that ends just before them. `counterexample` 56/92 is explained by `counterexamples` ^[openai-math-contents.md:#14] and by 22 hyphen-joined occurrences, 20 in dated paper-path slugs and two in `naimark-counterexample-zfc` and `wall-d2-counterexample`; capitalised `Counterexamples` ^[openai-math-contents.md:#12] and `Counterexample` ^[openai-math-contents.md:#8] are other whole words that the case-sensitive count does not add.

A substring inside a different word: `section conjecture` 5/6, where the sixth is the end of `intersection conjectures` ^[openai-math-contents.md:#1] (L1749), a different subject.

One name for two things: `Shafarevich` 12/13 stands for the `Tate–Shafarevich` ^[openai-math-contents.md:#6] group six times and `Shafarevich–Tate` ^[openai-math-contents.md:#1] once (the arithmetic object in families 002, 004 and 006, L29 to L77), and five times for the Shafarevich conjecture of family 046 (L527 to L535); the thirteenth is the slug at L533. The census row does not separate them, so a reader of this table must go to the lines.

**What the reading met besides.** **Observed:** the family numbering is not consecutive: five numbers are missing (045, 061, 070, 123, 163) and the last family is 377, while the bold total „722 manuscripts covering 372 result families.“ ^[L13] matches the 372 headings and the 722 PDF-link lines counted with `grep` in `05-verify.txt`. The document does not comment on the gaps. **Observed:** the title under family 302 at L3047, „Filtered products and boundary-preserving compression in complex cobordism“ ^[L3047], stands first among that family's manuscripts, whose description (L3045) is about the radius of comparison and mean dimension; the second title, L3051, matches the heading. **Observed:** one title is written twice in family 056, „Finite ordinary minimal model programs on compact Kähler fourfolds“ ^[L617] (also L621), with two different dated paths.

Export damage: headings write the apostrophe typographically, „Milne’s rationality conjecture and algebraic specialization“ ^[L23], while abstracts write a straight one in the same name (the profile reports 0 ASCII quotes and 623 typographic marks). `read.py --find` folds the two apostrophes together and the count does not: `Milne's rationality conjecture` ^[openai-math-contents.md:#3] counts the straight forms, and the curly form `Milne’s rationality conjecture` ^[openai-math-contents.md:#1] of the heading is a separate occurrence. Superscripts are dropped in the plain text, so an exponent is glued to its base as in „whose predecessors have no prime factor exceeding xδ“ ^[L127] and „the critical L3 estimate holds with every positive Sobolev loss“ ^[L817]; the profile counts 11 digits glued to words. Formulas stay as LaTeX inside backtick-dollar spans, and display formulas stand on their own lines; no candidate quotes across one, and a term that stands only in a formula (a symbol, a group, an operator) is not listed. The lowercase `lean` ^[openai-math-contents.md:#235] stands as often as `Lean` ^[openai-math-contents.md:#235] because each Lean link repeats the word in its path.

**The document's standing.** It makes no claim about its own authority: it counts and orders manuscripts, and each family description reports results as proved with `Proves` ^[openai-math-contents.md:#165]. That is the document's report of what its manuscripts claim, recorded and never applied. The document does not say who or what produced the manuscripts: `OpenAI` ^[openai-math-contents.md:#0] stands 0 times.
