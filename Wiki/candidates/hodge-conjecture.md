---
term: Hodge conjecture
status: candidate
sources: 2
readings: 2
conflict: none yet
ingested: ["openai-math-contents", "openai-math-readme"]
aliases: ["Hodge Conjecture", "rational Hodge conjecture"]
gathered: "2026-10-07"
---

# Hodge conjecture

**A borrowed concept from algebraic geometry, not part of the novel's world: that rational Hodge classes are algebraic; the github.com/openai/math collection (decision 026) reports it proved for CM abelian varieties and for products of K3 surfaces.** Each reading below is one document's, attributed and unmerged; the catalogue reports the result as proved, and how far it was checked is the [[lean-formalization|Lean formalization]] page's question.

## Reading — `openai-math-contents`, 2026-10-06, the manuscript map — family 032, the rational Hodge conjecture for CM abelian varieties and for products of K3 surfaces

The description reports the conjecture proved for one class in full: it „Proves the rational Hodge conjecture for every complex CM abelian variety, in every dimension and codimension.“ ^[openai-math-contents.md:L317] Through other theorems it claims consequences beyond Hodge: „Through Milne's theorems, this also gives the Tate conjecture for all abelian varieties over finite fields and the Hodge standard conjecture for abelian varieties in every characteristic.“ ^[openai-math-contents.md:L317]

The CM manuscript's abstract: „We prove the rational Hodge conjecture for complex abelian varieties with complex multiplication: every rational Hodge class on such a variety is a rational linear combination of algebraic cycle classes.“ ^[openai-math-contents.md:L329] A second manuscript takes another class: „We prove the rational Hodge conjecture for every finite product of projective complex K3 surfaces: every rational Hodge class is algebraic.“ ^[openai-math-contents.md:L321]

The catalogue claims the conjecture for these classes, not in general; it carries no `Lean` link for the family.

## Reading — `openai-math-readme`, 2026-10-06, the openai/math readme — the CM case as an exception to the procedure

The readme names the proof as outside the fixed procedure: „Exceptions to this fixed procedure include work on a zero-free region for the Riemann zeta function and proof of the Hodge Conjecture for CM abelian varieties.“ ^[openai-math-readme.md:L52] It says nothing of how that proof was produced instead.
