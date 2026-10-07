---
source: Sources/drive/openai-math-contents.md
read: "2026-10-07, the whole document (L1 to L3708) through read.py with line numbers, in ranges; by a document-reader subagent (Sonnet)"
stance_markers: ["Manuscript map", "Lean", "secondary writeup"]
stance_marker_count: 237
reads_as: "a catalogue of numbered result families: for each, a one-paragraph description in the collection's own voice, then the titles of its manuscripts as links to PDFs, each followed by that manuscript's abstract in the first person plural"
---

# Note — OpenAI math — Mathematics manuscript collection (manuscript map)

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document is English prose about mathematics and has no world of a novel; its terms are the named problems, conjectures and results of its families, and its own words for the work. Its stance is a report: a contents page that states, family by family, what its manuscripts are said to prove or disprove. The three stance markers are its own labels, `Manuscript map` ^[openai-math-contents.md:#1], `Lean` ^[openai-math-contents.md:#235] and `secondary writeup` ^[openai-math-contents.md:#1], which sum to the `stance_marker_count` of 237 (`05-verify.txt`).

## 1 · What kind of text this is, and how it marks itself

- The file names itself „Mathematics manuscript collection“ ^[L11] and heads its body „Manuscript map“ ^[L17].
- The document states its own size in one bold line: „722 manuscripts covering 372 result families.“ ^[L13]
- The document describes its layout in one sentence: „Each result description is followed by its constituent manuscripts and their abstracts.“ ^[L19]
- The document points to a separate file: „Read the overview PDF“ ^[L15].
- **Observed:** the stated total agrees with the structure. The file has 372 numbered bold headings and 722 lines that link a PDF (both counted with `grep`, `05-verify.txt`).
- **Observed:** the heading numbers are not consecutive. Five numbers are missing (045, 061, 070, 123, 163) and the last heading is 377; no sentence of the document mentions the gaps.
- **Observed:** L21 holds one leftover HTML header cell, `<thead><tr><th>Result</th></tr></thead>`, the single remnant of the table markup that the landing removed.

## 2 · How a family describes a result

- A family description reports its result in the collection's own voice, in the third person: „Proves Milne's rationality conjecture for abelian varieties“ ^[L23].
- The verbs of result are counted as whole words: `Proves` ^[openai-math-contents.md:#165], `Resolves` ^[openai-math-contents.md:#41], `Constructs` ^[openai-math-contents.md:#44] and `Disproves` ^[openai-math-contents.md:#18].
- The manuscript's own abstract, which follows the title link, speaks in the first person plural: the abstract of the first manuscript of family 001 says „We prove Milne's rationality conjecture for abelian varieties“ ^[L27].
- One family refers to another by its number, in the description's voice: „Together with result 032“ ^[L23].
- Another description does the same for a different pair: „With result 006“ ^[L29].
- A link label `Lean` ^[openai-math-contents.md:#235] stands once at the end of the description of each family that carries one. **Observed:** 235 headings carry it and 137 do not (`grep`, `05-verify.txt`); the document gives no sentence about what the linked file holds, and `proof assistant` ^[openai-math-contents.md:#0] and `formalized` ^[openai-math-contents.md:#0] do not stand in it.

## 3 · Named results the descriptions report as proved

- Family 003 reports the quasi-Riemann hypothesis as resolved: „resolving the quasi-Riemann hypothesis“ ^[L43].
- Family 004 reports a negative answer for the rational numbers: „no algorithm decides whether an integer-coefficient polynomial in an arbitrary number of variables has a rational zero“ ^[L57].
- Family 002 reports the full Birch–Swinnerton-Dyer formula for a class of curves, including a finiteness statement: „including finiteness of the Tate–Shafarevich group“ ^[L29].
- Family 102 states in one short sentence that a named conjecture is proved: „Proves Khot's Unique Games Conjecture.“ ^[L1031]
- Family 158 is headed by its own result: „The Euclidean plane cannot be colored with five colors.“ ^[L1537]
- Family 016 reports a named conjecture as proved: „Proves the abelian Zilber–Pink conjecture“ ^[L197].
- Family 287 reports the free group factor isomorphism problem as resolved; its heading is „Isomorphism of the free group factors“ ^[L2923].

## 4 · Named results the descriptions report as disproved or refuted

- Family 196: the description says „disproving Kaplansky's zero-divisor conjecture“ ^[L1819].
- Family 156 is headed „Borsuk's conjecture fails in dimension nine“ ^[L1517].
- Family 095: „Disproves the Projected Lax conjecture“ ^[L961].
- Family 161: „Disproves Sidorenko's conjecture“ ^[L1559].
- Family 340: „Disproves the unrestricted nearby Lagrangian conjecture.“ ^[L3361]
- Family 109 reports a refutation of an optimality conjecture: „This disproves the Schönhage–Strassen“ ^[L1109].
- Family 054 names its target: „This disproves Kuznetsov's rationality conjecture“ ^[L587].
- Family 047: the description says „disproving affine-space cancellation over ℂ in dimension four“ ^[L537].
- Family 305 states a failure in the present tense: „The unrestricted four-dimensional disk-embedding conjecture fails“ ^[L3067].

## 5 · Computation and certificates that the texts mention

- The description of family 266 states how its upper bound was obtained: „The exclusion is a complete certified computation under the stated binary64 arithmetic and compiler conditions.“ ^[L2729]
- The abstract of the manuscript under that family says of its own result: „The upper bound is computer-assisted“ ^[L2733], with `computer-assisted` ^[openai-math-contents.md:#1] standing once.
- An abstract of family 189 says programs and traces accompany the paper: „Complete programs and deduction traces accompany the paper.“ ^[L1777]
- An abstract of family 090 says its sign conditions are proved „using rigorous interval arithmetic“ ^[L927].
- A description reports a construction that turns a machine into a force: „A terminating compiler turns a Turing machine and input into a finite program for the force“ ^[L3665].

## 6 · Limits and hedges the texts state about their own results

- The abstract under family 010 limits what its result asserts: „it does not assert classical modularity“ ^[L113].
- The abstract under family 014 limits it again: „The result does not assert ellipticity, Arthur-packet classification, or a multiplicity formula.“ ^[L153]
- The abstract under family 056 limits an existence claim: „The theorem concerns existing flip sequences; it does not assert the existence of all contractions or flips.“ ^[L607]
- The abstract under family 183 says what its proof does not supply: „The proof is nonquantitative and does not supply explicit constants.“ ^[L1733]
- The abstract under family 281 says what it does not give: „We give no quantitative bound on the required depth or efficient angle-selection procedure.“ ^[L2875]
- The abstract under family 032 names its input as open: „The existence of the initial correspondence remains a hypothesis.“ ^[L349]
- The abstract under family 218 names its inputs: „Assuming the stated deterministic critical-reference estimates, we prove“ ^[L2091].
- The limiting phrases are counted as whole words, `does not assert` ^[openai-math-contents.md:#4] and `do not assert` ^[openai-math-contents.md:#1].

## 7 · Companion papers, priority and other people's work

- The abstract under family 014 ties its proof to another manuscript: „The proof extends the unramified Ramanujan theorem of a companion paper to all ramified places.“ ^[L165]
- The abstract under family 142 ties its proof to a named companion paper: „The proof uses the uniform Hecke zero-free theorem from the companion paper“ ^[L1405].
- The description of family 235 credits another author in the collection's voice: „We credit Gaia Carenini with priority for resolving the threshold-existence conjecture“ ^[L2309], with `priority` ^[openai-math-contents.md:#3] standing three times and the report archive `ECCC` ^[openai-math-contents.md:#1] once.
- An abstract of the same family describes itself as another proof: „This paper gives an alternative proof“ ^[L2313].
- The abstract under family 057 reports an earlier announcement by named others: „This conclusion was previously announced by Cao–Deng–Hacon–Păun.“ ^[L633]
- The description of family 297 opens by pointing to another author's construction; the document writes „Gives an alternative to“ ^[L3011] and names `Tanaka` ^[openai-math-contents.md:#1] in the link text that follows.
- One link is labelled by the collection `secondary writeup` ^[openai-math-contents.md:#1] (L1095).

## 8 · Said two ways, or left open — recorded, not resolved

- Family 002 is headed with an acronym, „The full BSD formula from low Selmer corank“ ^[L29], and the same description spells the name out; `BSD` ^[openai-math-contents.md:#2] and `Birch–Swinnerton-Dyer` ^[openai-math-contents.md:#4] are both the document's surfaces, and the text does not say that one abbreviates the other.
- One name, two statements: the description of family 209 says „Disproves unrestricted integral Gersten injectivity in degrees“ ^[L1933] and the description of family 258 says „Proves Gersten's conjecture“ ^[L2593]. **Observed:** the two descriptions state different things under the same name (`Gersten's conjecture` ^[openai-math-contents.md:#4]), one about K-theory classes, the other about one-relator groups, and the document does not distinguish them.
- Family 003's description says „A companion gives a different proof of the zero-free half-plane“ ^[L43], and names a second half-plane in a formula. The document does not say how its two statements relate.
- An abstract of family 235 says another manuscript improves it: „the companion paper on random 3-SAT sharpens this“ ^[L2321]. The document leaves both statements standing.
- **Observed:** the first manuscript title under family 302, „Filtered products and boundary-preserving compression in complex cobordism“ ^[L3047], does not match that family's description (L3045), which concerns radius of comparison and mean dimension. The second title, „Radius of comparison equals half the mean dimension“ ^[L3051], does.
- **Observed:** family 056 lists one title twice, „Finite ordinary minimal model programs on compact Kähler fourfolds“ ^[L617], under two paths (L617 and L621).

## 9 · Absent, counted

- The document does not name its producer: `OpenAI` ^[openai-math-contents.md:#0] and `internal model` ^[openai-math-contents.md:#0] do not stand in it.
- The document does not use the words of checking, review or release: `verified` ^[openai-math-contents.md:#0], `checked` ^[openai-math-contents.md:#0], `peer` ^[openai-math-contents.md:#0], `referee` ^[openai-math-contents.md:#0], `reviewed` ^[openai-math-contents.md:#0] and `released` ^[openai-math-contents.md:#0] all stand 0 times.
- The singular `result family` ^[openai-math-contents.md:#0] stands 0 times and the plural `result families` ^[openai-math-contents.md:#1] once, in the bold total at L13; this is the plural of the same words, not an absence of the idea.
