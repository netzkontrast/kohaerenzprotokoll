---
name: typesafe
description: Build with TypeSafe's Jev — a model that answers typed questions (noul = P(yes), choice = one of a set with a distribution, score = position on ordered levels) over a state, instead of generating text. Covers how to word a question so its probability means something, how to compose answers in code, the thresholds and limits the TypeSafe cookbooks measured, the Python SDK as installed here, and where in this project a Jev answer may direct attention and where it may never enter the record. Use when considering, designing, calling or evaluating Jev or TypeSafe for anything — ranking passages, choosing the next document, a second opinion on a near match, flagging stance — and before sending any corpus text to the API.
---

# TypeSafe — typed judgements from Jev, composed in code

Derived from TypeSafe's own skill (`typesafe-ai/skills`, v0.5.7, MIT — `LICENSE`
here) and rewritten from a full read of the nineteen cookbooks at
docs.typesafe.ai/cookbooks on 2026-09-23. What each cookbook measured, with its
conditions, is in `references/cookbooks.md`. Numbers below carry the cookbook
they came from; **none of them was measured on this corpus.**

## What it is

`POST https://api.typesafe.ai/v1/systemone` takes a `state` (a string or any JSON)
and a map of named questions, and returns one typed answer per name. Jev does not
write. It returns probabilities that code consumes. **The model judges; code
decides** — every cookbook keeps thresholds, precedence and actions in code, which
also means a policy can be re-run over stored answers with no new call.

## Choose the type by the shape of the decision

| type | answer | use when | trap |
|---|---|---|---|
| `Noul` | `.noul` ∈ [0,1] | a condition that holds or not, independent of other options | 0.5 means "as likely yes as no", not "medium" |
| `Choice` | `.choice`, `.probabilities`, `.confidence` | exactly one of a closed set | **probabilities sum to 1, so something always wins** — even when nothing fits |
| `Score` | `.score` (expected level), `.probabilities`, `.confidence`, `.legend` | ordered outcomes, especially with a labelled middle | levels must describe concrete situations, each standing alone |

Hard limits the cookbooks hit: **a Choice takes at most 255 options**
(pre-parsed; "reliably up to roughly 240" — classification), and **a Score at most
10 levels — eleven is a server error** (autoresearch). Above either, go two-stage:
pick a window or a parent first, then choose inside it (semantic_find,
hierarchical).

## Wording a question

These are the lessons the recipes paid for, in the order they bite.

**Name the narrowest fact that decides it.** Asking whether two lines were "the
same paragraph" scored unmarked list items 0.77–0.91; asking whether the second
line "picks up mid-sentence" separated them (autoformat). A topical question
inflates every probability — the skill-suggestion gate had to ask whether an
*action* was wanted, because a subject question "will not separate *explain what a
monad is*".

**Make yes mean the thing you are checking for.** Every row then reads the same
way (consistency_noul). For a verifier, make **true mean wrong** so one confident
flag can fire (sde_cascade).

**Write the false criterion as the close-but-wrong case.** Re-ranking legal
passages: false is "merely on a similar topic or doctrine; it does not supply the
specific proposition". Topical similarity is exactly what the lexical stage
already rewarded (rerank).

**Give absence an answer.** A `none` option on every pick (pre-parsed, date), a
`says_nothing` beside `supports`/`contradicts` (citation_check), a separate
existence `Noul` beside a Choice over lines — the Choice ranked a line at 0.86
for a question the document does not answer, and the Noul said 0.14
(semantic_find). A `stated?` Noul before any argument, "without it, the choice
would have to name some window, and it would have named one confidently"
(function_calling).

**Separate neighbouring labels in their descriptions**, and keep keys short.
Where the state already holds the text — line ids — a criterion may be `None`
(semantic_find). Where labels are terse, describe richly: "{umbrella} — includes:
{members}" (classification). **Option order is part of the question**
(hierarchical).

**Word the idea, not the parameter.** "Which resolution?" gives the input nothing
to match; roles sharing a value set need spelling out — "the one being measured,
named first" (function_calling).

**The middle level of a Score is the policy.** In entity alignment, "the wording
of the middle level is what moves pairs between the curator and the pairs left
unlinked" — and routing to the nearest level needs no fitted threshold at all.

**Put structure in the state, not prose.** Name the parts (`entity_a`/`entity_b`,
`query`/`passage`) so a question is about the *pair*; write ids into text
(`L052| …`) and refer to them; reference nested state with backticked paths.
Keep the state byte-identical while the question varies.

**Let code do what code can read.** Exact quote match before asking whether a
quote supports a claim (citation_check), BM25 before re-ranking, regex candidates
before picking a span — the model "cannot invent a value or transpose a digit"
when it can only choose among spans code found (pre-parsed). Arithmetic, dates,
punctuation, blank lines: code (entity, date, autoformat).

## Composing answers

- **Every question about one state in one request.** Each is scored on its own —
  answers were identical batched or not — and the state is paid once: 13
  questions cost 12.2× less and ran 10× faster in one call (parallel_questions).
  Ask companion and speculative questions up front and read only the relevant
  ones; an extra question is cheap, an extra round trip is not (autoformat).
- **Aggregate conservatively.** Confidence of a composite is the **minimum** over
  its parts, not the product (function_calling, date). A battery of "is it wrong"
  flags fires on the **max**, "not a mean, so one confident red flag is enough"
  (sde_cascade). A path through a hierarchy scores by length-normalised geometric
  mean, with beam search, because greedy "cannot recover" one early mistake
  (hierarchical).
- **Three outcomes, not two.** Every recipe that acts routes a band to a person:
  noul 0.30–0.70 (consistency_noul), top probability < 0.60 (consistency_choice),
  confidence < 0.8 (citation_check), < 0.60 (date), < 0.9 → report the parent
  class instead (classification). **All of these are stated as illustrative.** Set
  a threshold from labelled examples and the cost of each error, never from a
  cookbook.
- **`confidence` and the winner's probability are different.** "A winner at 0.45
  with a runner-up at 0.44, and a winner at 0.45 with the rest scattered thinly
  are different situations" (classification). Decide which one a gate reads and
  say so.
- **Rank wide, then re-check a shortlist with richer criteria**, and let either
  stage return nothing (skill_suggestion). A later stage can only reject what the
  earlier one handed it (skill_suggestion, rerank).

## What the numbers do and do not show

- **Repeatability is not correctness.** Jev's probabilities moved by a mean
  std-dev of about 0.01 over 15 identical repeats — and a borderline question
  still crossed 0.5 (`covered` 0.43–0.53). One LLM was *more* repeatable and that
  "does not imply correctness" (consistency_noul, consistency_choice).
- **A confident wrong answer is more persuasive than none** (skill_suggestion).
  An injection score is "a filter … nothing here is a security boundary"
  (classifying_rag_passages).
- **`jev-latest` is an alias.** It resolved to `jev-1.13.0` here on 2026-09-23;
  the cookbooks ran on `jev-1.12`. Record `response.model` with every result.
- Several recipes report no accuracy against their own labels (entity_alignment
  loads `known_same_as` and never scores it; function_calling shows 14 correct and
  no metric). Treat a recipe as a shape to try, not as evidence it works here.

## The SDK, as installed

`typesafe-sdk` 0.7.1 in `.venv-typesafe` (setup in `CLAUDE.md`). Verified against
the installed package, not the docs:

```python
from typesafe_sdk import TypeSafeClient, Noul, NoulCriteria, Choice, Score, RetryPolicy

with TypeSafeClient() as client:            # key from TYPESAFE_API_KEY, model jev-latest
    r = client.system_one(
        state={"a": "...", "b": "..."},
        questions={
            "same": Noul(instructions="...", criteria=NoulCriteria(true="...", false="...")),
        },
    )
r.model                     # the resolved version — record it
r.answers["same"].noul      # or r.nouls["same"] / r.choices[...] / r.scores[...]
r.usage.input_tokens        # output tokens were priced at 0 in every cookbook
```

- **Default timeout is 10s**; the cookbooks set 30–120s for long states.
  `RetryPolicy(max_retries=5, backoff_initial=1.0, backoff_max=20.0)` is what
  hierarchical used.
- **Rate limit:** "the public endpoint rate-limits above roughly eight" concurrent
  (entity_alignment); the recipes used 4–8 workers.
- **Offline replay:** `TypeSafeClient(transport=...)` accepts an `httpx2`
  transport, so recorded responses can be served by `httpx2.MockTransport` with no
  key and no network. That is how a check built on Jev satisfies P5. Every
  cookbook cached calls keyed on a hash of state plus questions, so editing a
  question invalidates its cache.
- Errors are typed: `TypeSafeRateLimitError`, `TypeSafeAuthenticationError`,
  `TypeSafeAPITimeoutError`, … A call that never returned is **not** an answer
  (P15) — report it as unreached, never as a low probability.

## In this repository

**One test calls Jev:** `scripts/jev_entities.py`, entity candidates on two
documents, measured in `NOW.md`. Nothing in the pipeline does. Where it may go is reasoned in
`Plan/concept/jev-in-ingestion_2026-09-23.md`; this skill does not restate it
(P6). Four things hold regardless:

1. **A Jev answer may direct attention, never enter the record.** No candidate
   list, page, reading, link, conflict or count is written from a probability.
   Conflict detection is never mechanised and a link is never inferred —
   `CLAUDE.md` says why.
2. **Sending corpus text to TypeSafe is an author decision (P0)** and has not been
   made. Term surfaces alone are a smaller exposure than passages; neither has
   been approved. The environment's permission check blocks it, correctly.
3. **Scored before trusted.** Each use is measured against labels this repository
   already holds — `Plan/runs/judgements.jsonl`, the passages each
   `Wiki/questions/` page names — and reported as two difference lists, not one
   number (P27).
4. **The key comes from the environment** and is never written to a file here.

Three recipes map onto this project closely enough to name:

| recipe | here |
|---|---|
| semantic_find — `L052\|` ids in the state, a Choice over lines plus an existence Noul | `read.py` already prints `NNN\|` file lines; the same shape could find the line that answers an open question, and say when a document has none |
| entity_alignment — a 3-level Score with a written middle for the curator | the near-match ledger: *one term* / *related, a person decides* / *two terms* fits `judgements.jsonl` better than a bare Noul |
| rerank — BM25 shortlist, one Noul per pair, false = "merely on a similar topic" | choosing the next document from qmd `search` hits, which is exactly where BM25 is known to miss |

## Provisional

```yaml
name: typesafe          # provisional
# may not: write anything into Sources/ or Wiki/, decide a near match,
#          detect a conflict, or run on corpus text without the author's yes
# retire when: a first measured use shows it adds nothing over fold() and qmd
```
