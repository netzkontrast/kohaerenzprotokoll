---
description: >-
  Critically assess a decision before it is taken: generate four isolated
  positions on the decision predicate (P, not-P, both, neither), map where
  they contradict or complement, and synthesize a framing that preserves the
  tension instead of averaging it. Mandatory for contested canon decisions
  (D-xx) and for wiki changes that supersede, merge or contradict existing
  pages. The program never decides; the author does.
  Usage: /tetraframe [decision statement | Wiki/questions page | proposed wiki change]
argument-hint: "[the decision, the question page, or the proposed wiki change]"
---

# TetraFrame — four corners before a decision

Port of Hmbown/tetraframe-dspy (MIT, `docs/tetraframe-LICENSE.txt`) as the
DSPy program `tools/kpwiki/tetraframe.py` (skill `dspy-tetraframe`). Use it
where a pro/con list would flatten the problem: canon decisions, contested
question pages, and wiki changes that change what we hold to be true.

## When it is mandatory

| Situation | Seed |
|---|---|
| a `Wiki/questions/` page escalates to a D-xx decision | the question, with Canon passage and the research claims as context |
| `/promote-to-canon` on a claim with a `contradicts` edge or a `critical` conflict | "Claim X should supersede Canon passage Y" |
| `/wiki-understand` proposes merging two concepts or marking one `superseded` | "Concepts A and B are one concept" / "A supersedes B" |
| a storyform or world-rule change (ncp*.json, WorldAxiom) | the rule change as a predicate |
| any decision the author calls contested | as stated |

Not for: lookups, single-source facts, style choices, anything with clear ground truth.

## Step 1: Write the seed (human, with `/clarify` first if vague)

A seed carries a genuine tension: "We keep framing X as A-or-B, but …";
"Canon says X, three later documents assume Y"; "We cannot decide between
merging A into B or keeping both because Z". Attach context: the Canon
passages, the claims with citations, the relevant D-xx history. Run
`/clarify` on the seed when its terms are not glossary-bound.

## Step 2: Run (dry-run first; nothing is written to Wiki or Canon)

```bash
.venv-dspy/bin/python -m tools.kpwiki.tetraframe_cli --seed "<seed>" \
    [--context-file Canon/<file>.md ...] [--out Plan/decisions/tetraframe/<slug>.json] [--dry-run]
```

`--dry-run` prints the assembled seed and context. The live run writes the
run artefact (distilled seed, predicate, four corners, cartography, P*,
verification) to `--out` and prints the verification table.

## Step 3: Read the verification before reading P*

| metric | threshold | if below |
|---|---|---|
| branch independence | 0.90 | corners leaked into each other; rerun stage 2 (fresh rollouts) |
| rigor of both | 0.78 | "both" is a compromise, not a typed co-holding; rerun both |
| rigor of neither | 0.78 | "neither" is evasion, no replacement frame; rerun neither |
| contradiction honesty | 0.75 | cartography erased a real contradiction |
| transformation quality | 0.82 | P* is an average; rerun transform |
| fake novelty | 0.70 | P* uses terms no corner supports |
| slop | 0.70 | mush words ("nuanced", "balanced", "consider") |

Below threshold → follow the retry recommendation; do not present a run that
fails branch independence.

## Step 4: Present, never decide

Show the author, in this order: the predicate as chosen; P, not-P, both
(with its basis: temporal / scale / role / ontology / context split, layered
causality, admissible paradox), neither (with its failure mode and the
replacement frame); the contradiction map and the evidence discriminators
(what evidence would settle it); then P*. Ask with `AskUserQuestion`. P* is a
candidate framing, not the decision.

## Step 5: Record

- Decision: the D-xx entry cites the run file and states which corner or P*
  the author chose and why (one sentence each for the survivors from P and
  not-P, and the dissolved false frame, if any).
- Question page: P, not-P, both, neither become the "Candidate answers"
  section; evidence discriminators become the "Evidence needed" list.
- `Wiki/log.md`: `## [YYYY-MM-DD] tetraframe | <slug> | aggregate=<score> chosen=<corner|P*|none>`.

## Rules

- The four corners are generated in isolation; never paste one corner into another's input.
- "Both" must name its split basis; "neither" must name its failure mode and a replacement predicate. Without those they are invalid, not weak.
- Compromise language ("middle ground", "balanced approach", "on the one hand") is a defect in P*, not a virtue.
- Canon quotes stay German inside corners; engineering prose is English.
- A run is evidence for a decision log entry, never a substitute for the author's decision.
