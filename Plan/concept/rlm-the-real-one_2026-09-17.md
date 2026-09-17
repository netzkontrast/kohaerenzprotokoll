# The actual RLM, read — what maps, what does not, and the one constraint it lacks

*2026-09-17, after reading `netzkontrast/rlm` (the MIT OASYS reference
implementation, `pip install rlms`). Until now I had been transferring the idea
from a description. The implementation is more specific, and one of its
assumptions does not hold here.*

## What an RLM actually gives the model

From `rlm/utils/prompts.py`, the REPL a model is handed:

| primitive | what it is |
|---|---|
| `context` | the long input, **as a variable**, `str` or `list[str]` |
| `llm_query(prompt)` | one sub-LLM completion; sub-context ≈ 500K chars |
| `llm_query_batched(prompts)` | the same, concurrent, order preserved |
| `rlm_query(prompt)` | a **recursive** sub-RLM — the child gets its own REPL |
| `SHOW_VARS()` | what exists in the environment |
| `answer = {"content": "", "ready": False}` | the termination protocol |

And the discipline, which is the part that makes it work:

> „REPL outputs over ~20K characters are truncated, so for longer payloads slice
> `context` and pass slices through `llm_query` rather than `print`-ing them
> whole."

**The environment enforces it.** The model cannot print the corpus into its own
context even if it tries.

## What this project already has, and what it does not

| RLM | here | |
|---|---|---|
| `context` as a variable | `Plan/derived/*.json`, `Wiki/index.json` | ✓ |
| never print the payload | `corpus.py` returns counts, dates, slugs — **never document text** | ✓, and structurally: the tool has no path that emits a body |
| `answer` / `ready` | the census, the note, the page | ✓ by another name |
| `llm_query` | **nothing** | ✗ |
| `llm_query_batched` | **nothing** | ✗ |
| `rlm_query` | **nothing** | ✗ |
| the model writing the code | fixed programs I wrote | ✗ **deliberately, for now** |

So: the **environment half is built and the language-model half is not.** Every
query here is a program someone wrote, replayable and checkable against
`judgements.jsonl` — which is the trade. The cost is that an unanticipated
question needs a new subcommand instead of a new prompt.

Their truncation is a *limit*; mine is *structural*. A model using their REPL
could print 19K characters of corpus. `corpus.py` has no code path that returns a
document body at all.

## The constraint the generic RLM does not have

RLM's whole premise is that the context is too large to read, so it must be
sliced and delegated. **At the document level here, that premise is false and
acting on it would break the method.**

A source document is ~6,700 words. Reading it whole is possible — and it is
*required*, because the census rule is that a reader proposes candidates **before
anything counts**. Counting first decides what gets seen, and roughly half the
twenty-one special cases found so far are invisible to any pattern a slicing
strategy would start from.

So an RLM-style document census would be cheaper and would find less. **The loop
belongs at the corpus level, not the document level** — and that distinction is
this project's, not something the RLM prompt could tell me.

## Where it does belong, with the number

„What does the corpus say about AEGIS?" is exactly the RLM case, and
`corpus.py plan` now computes the strategy instead of improvising it:

```
AEGIS — 315 documents, 14,676,980 chars
41 sub-calls at 400,000 chars each
```

Nothing was read to produce that. The document set comes from the surface index,
the sizes from the manifest.

**That is the shape of the missing step.** Today a term page carries readings
from the four documents that happened to be read — 1% of the corpus. The other
99% is addressable: `llm_query_batched` over 41 batches, merge, and a term page
could cite what 315 documents say without 315 documents entering anyone's context.

It already corrected the wiki once without any model at all: `Kael-Julia-Bindung`
is on a page and appears in **one** document, while `Kael-Juna-Verbindung` appears
in nine across fourteen months.

## What wiring it costs, honestly

- `pip install rlms` into `.venv-tools`, never the system Python.
- A backend and a key. The relevant price is the retired pipeline's **$2.79 and 18
  minutes per document** — 41 sub-calls over 14.7M chars is a different shape, but
  it is not free, and the project has no measured number for it.
- `rlm_query` recursion needs a model that can plan. `llm_query_batched` over a
  computed plan does not, and is the cheaper first thing to try.

**None of it is worth doing before the hand pass finishes.** The four documents
are producing the rules the sub-calls would need to be given, and a sub-call sent
without them would reproduce the pipeline that already failed — 19 quoting defects
in 141 claims, because nobody had written down what a quote had to be.

## The one idea worth stealing immediately

`SHOW_VARS()`. The environment tells the model what it has. Here, nothing tells a
reader what the derived cache already knows — `scripts/derive.py --stale` shows
what is missing, and there is no counterpart for what is *present*. A reader
wanting to know whether a question is already answered has to read the code.
