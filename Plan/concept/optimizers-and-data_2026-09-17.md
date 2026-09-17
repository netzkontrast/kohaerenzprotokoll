# Which optimizer, and what has to be recorded before any of them can run

*2026-09-17. Measured against DSPy 3.3.1 in `.venv-dspy`, not against documentation.*

## Where this project actually stands

| dataset | size | shape | usable |
|---|--:|---|---|
| one-term-or-two | **26** | balanced 13/13, all carrying a rule in words | yes |
| candidate extraction | **1** | one gold list written while reading | no — n=1 is a spot check |

32 judgements in the ledger, 31 with a stated rule, across 5 documents.
The `fold()` baseline on the 26 is **17/26 = 65%**, measured live.

**Nothing here is large enough for the optimizers that get talked about.**
`MIPROv2` wants 100+ and `BootstrapFewShotWithRandomSearch` 50+. So the question
is not which optimizer is best but which one is honest at n=26.

## The ladder that fits, in order of what it costs

| | optimizer | needs | LM calls | why it fits here |
|--:|---|---|---|---|
| 0 | `LabeledFewShot(k)` | nothing but the trainset | **~0** | the floor. Puts labelled pairs in the prompt and nothing else. If this does not beat `fold()`'s 65%, no optimizer will rescue the task |
| 1 | `BootstrapFewShot` | a scalar metric | tens | the standard choice at „~10+ examples". `max_bootstrapped_demos=4` by default |
| 2 | **`InferRules`** | a scalar metric | tens × `num_candidates` | see below — the one that fits this project specifically |
| 3 | `SIMBA` | a scalar metric | medium | „a reflective pass cheaper than GEPA". **Caution: `bsize` defaults to 32, larger than the whole trainset** |
| 4 | `GEPA` | 5-arg metric returning `Prediction(score, feedback)` | high, plus a reflection LM | its row in the selection table names no example count, and this project already writes the feedback |

Ruled out and why: `MIPROv2` (100+), `BootstrapRS` (50+), `BootstrapFinetune`
(needs a finetunable model; free API models are not), `KNNFewShot` (needs a
`dspy.Embedder`, which is a new dependency — though qmd now has a local
embedding model, so this becomes cheap if step 0–2 disappoint), `AvatarOptimizer`
and `BetterTogether` (not this shape of problem), `Ensemble` (nothing to ensemble
yet).

## `InferRules` is the one that fits this project, and it is not in the table

`dspy.teleprompt.InferRules` extends `BootstrapFewShot`. Read from the source: it
**induces rules in natural language** from the trainset, appends them to the
signature's instructions, and keeps the candidate that scores best on a
validation split.

That matters here more than anywhere else, because **`Plan/runs/judgements.jsonl`
already stores a human-written rule for 31 of 32 judgements.** So the induced
rules and the human rules are directly comparable, which no other optimizer
offers:

- Does the machine find the same rule a person wrote — „a leading German definite
  article is never a term boundary", „a compound is placed by what it names,
  never by its head"?
- Where it finds a *different* rule that scores as well, that is a finding about
  the corpus, not about the model.
- And an induced rule that survives is a candidate for `fold()` itself — at which
  point `judgements.py` replays every recorded decision against it. **The project
  already has the acceptance test for a machine-written rule.**

It is absent from `dspy-optimizer-selection`'s table. Worth reporting upstream to
`netzkontrast/dspy-agent-skills`.

**One trap, read from its source:** `compile()` splits the trainset 50/50 when no
`valset` is passed. At n=26 that is 13 train and 13 validation, silently, with no
canary held back at all.

## What has to be recorded before any of this runs

Six things. The first is a correctness requirement; the rest are what make an
optimizer's result mean something.

### 1. An explicit, recorded split — train / validation / canary

`scripts/trainset.py` has none today, and `InferRules` will invent one if it is
not given one. The canary must be **frozen, named, and never trained on**: the
`Negentropie`/`Entropie` pair belongs in it, because a model that merges two
opposites while matching the baseline's score is worse than the baseline at the
same number, and only a held-out canary showed that.

Written into the ledger as a field, not into a script, so the split survives the
script.

### 2. The evidence a decision rested on, as fields rather than prose

This is the gap that most limits what any optimizer can learn. Today a judgement
records two surfaces and a paragraph of `action` text. **The person decided using
things the input does not contain.** `J20` turned on a distribution — `Guardian`
22 times across analytic fields, `Wächter` 3 times and never in analysis — and
that is prose in `action`, invisible to a program.

An optimizer can only learn from what is in the example's input. So each
judgement needs the evidence structured:

```
counts:        {"Guardian": {"word": 22, "in": 63}, "Wächter": {"word": 2, "in": 3}}
co_occur:      how many lines hold both surfaces
fold_keys:     what fold() produced for each
markers:       article | plural | compound | prefix | hyphen | abbreviation | camelcase
document_role: which field or section each surface appears in
```

`capture.py` already computes the counts and the surfaces. Nothing carries them
into the ledger.

### 3. The pairs that were considered and rejected

The ledger records decisions made. It does not record the near-matches a person
looked at and dismissed as not worth recording. **A classifier trained only on
cases interesting enough to write down learns the wrong prior.**
`reconcile.py` already prints every `needs_judgement` pair; the ones that do not
become a judgement should be recorded as such, with one line of reason.

### 4. Rejected candidates, attached to the gold list

`reconcile.json` carries `not_promoted` per document — 11 terms for document 5,
each a real negative. The gold candidate list itself carries only positives. For
extraction, **the negatives are half the signal**: a term proposed while reading
and then withdrawn is exactly the case a model will get wrong.

### 5. Cost and wall-clock per run

The retired pipeline's numbers are the only data on what this work costs at
scale: 53 LM calls, 54 minutes, $8.38 for three sources. Nothing current records
either. **An optimizer's gain is not interpretable without its price**, and the
first question about any improvement over a 65% baseline will be what it cost.

### 6. A fixture that proves the metric can fail

Taken from the retired `compile_fixture.py`, which defined the exact feedback
strings a deliberately defective input must produce and asserted each appeared.
Neither `quotes.py` nor `fold()` has one. A metric nobody has seen fail is the
same defect as the coverage term that was pinned at 1.0.

## What is still true at the end of all this

Extraction stays untrainable until two or three more documents are read by hand.
Nothing above changes that, and the ladder's step 0 — `LabeledFewShot`, ~0 LM
calls — is the one thing that can be run the moment the split exists.

**Run step 0 before anything else.** If putting 16 labelled pairs in a prompt
does not beat 65%, the problem is the task's framing and no amount of reflection
will fix it.
