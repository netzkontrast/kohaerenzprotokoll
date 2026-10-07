---
term: Navier–Stokes
status: candidate
sources: 1
readings: 1
conflict: none yet
ingested: ["openai-math-contents"]
aliases: ["Navier-Stokes"]
gathered: "2026-10-07"
---

# Navier–Stokes

**A borrowed concept from fluid dynamics, not part of the novel's world: the equations of viscous flow, in which the github.com/openai/math collection (decision 026) reports a construction of universal computation — a forced fluid whose particle reaches a region exactly when a Turing machine halts.** Each reading below is one document's, attributed and unmerged; the catalogue reports the result as proved, and how far it was checked is the [[lean-formalization|Lean formalization]] page's question.

## Reading — `openai-math-contents`, 2026-10-06, the manuscript map — family 376, a fluid that computes

The family's heading is „Universal computation in forced Navier–Stokes flows.“ ^[openai-math-contents.md:L3665] Its description says the flows are built, not found: it „Constructs viscous incompressible flows starting from rest on a fixed flat three-dimensional domain that perform universal computation under smooth external forcing.“ ^[openai-math-contents.md:L3665] How a machine becomes a flow: „A terminating compiler turns a Turing machine and input into a finite program for the force, so a designated particle reaches a fixed region exactly when the machine halts.“ ^[openai-math-contents.md:L3665] The family carries a `Lean` link.

A manuscript's abstract states the same as a test on one particle: „a fixed particle enters a fixed open set exactly when a prescribed Turing machine halts“ ^[openai-math-contents.md:L3673]. Another says the fluid's velocity field „detects whether a prescribed machine halts“ ^[openai-math-contents.md:L3693]. The family does not claim the Navier–Stokes existence and smoothness problem; it is a construction of computation inside the equations.
