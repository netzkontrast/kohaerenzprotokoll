---
term: Hilbert's tenth problem
status: candidate
sources: 1
readings: 1
conflict: none yet
ingested: ["openai-math-contents"]
aliases: ["Hilbert’s tenth problem"]
gathered: "2026-10-07"
---

# Hilbert's tenth problem

**A borrowed concept from logic and number theory, not part of the novel's world: whether an algorithm can decide if a polynomial equation has a solution; the github.com/openai/math collection (decision 026) reports a negative answer over the rational numbers.** Each reading below is one document's, attributed and unmerged; the catalogue reports the result as proved, and how far it was checked is the [[lean-formalization|Lean formalization]] page's question.

## Reading — `openai-math-contents`, 2026-10-06, the manuscript map — family 004, a negative answer over the rationals

The description reports an undecidability result: it „Proves that no algorithm decides whether an integer-coefficient polynomial in an arbitrary number of variables has a rational zero, resolving Hilbert's tenth problem over ℚ negatively.“ ^[openai-math-contents.md:L57]

The manuscript's abstract says the same in its authors' voice: „We give a negative answer to Hilbert's tenth problem over the rational numbers: no algorithm decides whether a polynomial with integer coefficients has a rational zero.“ ^[openai-math-contents.md:L61] It adds one condition: „The number of variables is part of the input.“ ^[openai-math-contents.md:L61] The family carries no `Lean` link.
