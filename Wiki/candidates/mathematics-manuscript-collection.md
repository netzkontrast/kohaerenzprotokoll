---
term: Mathematics manuscript collection
status: candidate
sources: 2
readings: 2
conflict: none yet
ingested: ["openai-math-readme", "openai-math-contents"]
aliases: ["manuscript map", "result family", "result families"]
gathered: "2026-10-07"
---

# Mathematics manuscript collection

**A real-world entity, not part of the novel's world: the collection of mathematics manuscripts OpenAI published at github.com/openai/math on 2026-10-06 (landed 2026-10-07, decision 026), grouped into numbered result families.** What each of its documents says about it is below, attributed and unmerged.

## Reading — `openai-math-readme`, 2026-10-06, the openai/math readme — 722 manuscripts in 372 families, at different stages of verification

Size and unit: „The current catalogue contains 722 manuscripts organized into 372 families.“ ^[openai-math-readme.md:L24] A family is defined: „A family groups related papers, which may include a principal result, companion arguments, consequences, or alternative proofs.“ ^[openai-math-readme.md:L24] and „Each family is classified by mathematical discipline.“ ^[openai-math-readme.md:L24]

The readme states the collection's standing in its own words, and it is uneven: „This collection includes results at different stages of verification.“ ^[openai-math-readme.md:L17] and „Some of the unformalized results could have issues.“ ^[openai-math-readme.md:L19] It calls no result proved or refuted (`proved` ^[openai-math-readme.md:#0], `refuted` ^[openai-math-readme.md:#0]).

The collection is versioned: „We will preserve the public release history of this collection.“ ^[openai-math-readme.md:L56] and „Corrections and revisions will be recorded as new versions, with previously released versions remaining accessible.“ ^[openai-math-readme.md:L56] It may move: „We are also exploring community-hosted repositories for these materials.“ ^[openai-math-readme.md:L20]

## Reading — `openai-math-contents`, 2026-10-06, the manuscript map — the catalogue itself: 372 families, proved and disproved, and silent about who produced them

The file names itself „Mathematics manuscript collection“ ^[openai-math-contents.md:L11] and states its size: „722 manuscripts covering 372 result families.“ ^[openai-math-contents.md:L13] Its layout: „Each result description is followed by its constituent manuscripts and their abstracts.“ ^[openai-math-contents.md:L19] The numbered headings run to 377 with five numbers absent (045, 061, 070, 123, 163); the catalogue never mentions the gaps.

A description speaks in the collection's voice and reports results as settled — `Proves` ^[openai-math-contents.md:#165], `Disproves` ^[openai-math-contents.md:#18], `Resolves` ^[openai-math-contents.md:#41], `Constructs` ^[openai-math-contents.md:#44] — while each abstract speaks in its authors' first person plural, as „We prove Milne's rationality conjecture for abelian varieties“ ^[openai-math-contents.md:L27]. Some families report refutations, as „Borsuk's conjecture fails in dimension nine“ ^[openai-math-contents.md:L1517] and „disproving Kaplansky's zero-divisor conjecture“ ^[openai-math-contents.md:L1819]. Some lean on computation: „The exclusion is a complete certified computation under the stated binary64 arithmetic and compiler conditions.“ ^[openai-math-contents.md:L2729]

The catalogue names no producer and no verification: `OpenAI` ^[openai-math-contents.md:#0] and `verified` ^[openai-math-contents.md:#0] do not stand in it.
