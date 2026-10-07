---
term: Lean formalization
status: candidate
sources: 2
readings: 2
conflict: none yet
ingested: ["openai-math-readme", "openai-math-contents"]
aliases: ["Lean formalizations", "Lean library", "formalization catalogue"]
gathered: "2026-10-07"
---

# Lean formalization

**A borrowed concept: a proof written in the Lean proof assistant and checked by machine, as the github.com/openai/math collection (decision 026) uses it to mark which of its results are formally verified.** Each reading below is one document's, attributed and unmerged.

## Reading — `openai-math-readme`, 2026-10-06, the openai/math readme — formal proofs for some results, and a warning about the rest

Formal proof is partial: „Not all have accompanying Lean formalizations.“ ^[openai-math-readme.md:L17] and „Many, but not all, of the manuscripts have been formalized.“ ^[openai-math-readme.md:L29] More are promised: „We will continue to update this repository with Lean formalizations as we obtain them.“ ^[openai-math-readme.md:L17]

The readme ties the lack of one to a risk: „Some of the unformalized results could have issues.“ ^[openai-math-readme.md:L19] It names the apparatus — the `Lean library` ^[openai-math-readme.md:#1], the `formalization catalogue` ^[openai-math-readme.md:#1] and the `Comparator instructions` ^[openai-math-readme.md:#1] — which „describe the available formal proofs, their associated papers, and verification configurations“ ^[openai-math-readme.md:L29] and give „additional checking instructions“ ^[openai-math-readme.md:L29]. It gives no number of formalized results and names none.

## Reading — `openai-math-contents`, 2026-10-06, the manuscript map — a link label on 235 of 372 families, never explained

`Lean` ^[openai-math-contents.md:#235] stands once at the end of a family's description, as a link to a scope file, as on the quasi-Riemann family: „([Lean](lean/docs/003.md))“ ^[openai-math-contents.md:L43]. 235 families carry it and 137 do not. The catalogue writes no sentence about what the label means: `formalized` ^[openai-math-contents.md:#0] and `proof assistant` ^[openai-math-contents.md:#0] do not stand in it, so which claims are machine-checked, and how far, is left to the linked files.
