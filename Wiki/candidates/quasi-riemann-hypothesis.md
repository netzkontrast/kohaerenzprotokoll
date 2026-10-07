---
term: quasi-Riemann hypothesis
status: candidate
sources: 2
readings: 2
conflict: none yet
ingested: ["openai-math-contents", "openai-math-readme"]
aliases: ["zero-free half-plane", "Landau–Siegel zeros"]
gathered: "2026-10-07"
---

# quasi-Riemann hypothesis

**A borrowed concept from number theory, not part of the novel's world: a fixed half-plane free of zeros of the Riemann zeta function and the Dirichlet L-functions, which the github.com/openai/math collection (decision 026) reports proved at 7/8.** Each reading below is one document's, attributed and unmerged; the catalogue reports the result as proved, and how far it was checked is the [[lean-formalization|Lean formalization]] page's question.

## Reading — `openai-math-contents`, 2026-10-06, the manuscript map — family 003, a zero-free half-plane at 7/8 and a second proof at 11/12

The family's heading is „The quasi-Riemann hypothesis.“ ^[openai-math-contents.md:L43] and its description reports it resolved: every Dirichlet L-function, the zeta function included, is zero-free beyond 7/8, „resolving the quasi-Riemann hypothesis“ ^[openai-math-contents.md:L43]. A companion „gives a different proof of the zero-free half-plane“ ^[openai-math-contents.md:L43] at 11/12; the family carries a `Lean` link.

The first manuscript's abstract says, in the first person plural of its authors: „In particular, the Riemann zeta function is zero-free in this half-plane, proving the quasi-Riemann hypothesis.“ ^[openai-math-contents.md:L47] The second, the alternate proof, adds a consequence: „In particular, this rules out the existence of Landau–Siegel zeros.“ ^[openai-math-contents.md:L51] A third manuscript states that exclusion uniformly: „We prove the uniform exclusion of Landau–Siegel zeros.“ ^[openai-math-contents.md:L55]

The catalogue reports these as proved; it does not say how any was checked, and the readme's caution about unformalized results is that document's, not this one's.

## Reading — `openai-math-readme`, 2026-10-06, the openai/math readme — an exception to the procedure, and a human-edited writeup

The readme names the work as outside the fixed procedure: „Exceptions to this fixed procedure include work on a zero-free region for the Riemann zeta function and proof of the Hodge Conjecture for CM abelian varieties.“ ^[openai-math-readme.md:L52] One writeup on the zero-free region „was human edited for readability“ ^[openai-math-readme.md:L52]. It does not say which result the work proved or how the procedure differed.
