# Running the RLM on the one question this corpus is known to trip people on

**Date:** 2026-09-17. First time an LM has been run against this corpus at all.

## The setup now exists

Four things had to be true and now are:

| piece | state |
|---|---|
| Deno (the Pyodide sandbox `dspy.RLM` needs) | installed via `Legacy/scripts/setup_dspy.sh --deno`; **does not survive a container** |
| dspy | 3.3.1 in `.venv-dspy/` |
| an LM with no API key | `Legacy/tools/kpwiki/local_lm.py` — the `ClaudeLM` bridge, `claude -p` per call |
| an API key | OpenRouter, in the git-ignored `.env` |

`local_lm.py` is the same `Hmbown/dspy-local` pattern the `dspy-local-runtime`
skill teaches. **This project had already built it and parked it in `Legacy/`.**

## The question

The census for `guardians-und-kern-welten-konzept` records a trap. The document
says „die vier zentralen Hüter" ^[L15] and „die vier Guardian/Welt-Paare" ^[L135]
and **names five Guardians**. It resolves this itself, once, in a parenthesis:

> „Kairos und Sophia werden als zwei distinkte, aber komplementäre Guardians
> dargestellt, die gemeinsam über diese Domäne wachen." ^[L96]

Four *pairs*, five Guardians. Miss that parenthesis and the count is wrong.

So: *name exactly the Guardians in this document.* Truth is five.

## What happened

| run | configuration | result |
|---|---|---|
| `dspy.RLM` | haiku via `claude -p`, `max_iters=4`, REPL over the text | **4/5 — missed Sophia** |
| direct prompt | `nex-agi/nex-n2.5-pro:free`, full document in context | 5/5 |
| direct prompt | `nex-agi/nex-n2.5-mini:free`, full document in context | 5/5 |
| direct prompt | `nvidia/nemotron-3.5-lightning:free`, full document in context | 3/5 — missed Kairos and Sophia |

**Four runs, two right. And both failures are partly mine**: the RLM had four
iterations to work with, and the nemotron answer was cut off mid-reasoning by a
120-token cap. Neither is evidence that a model cannot do this.

**Eleven of fifteen free models did not answer at all** — 404, 429, 403, or a
response with no `choices`. The free tier is not a benchmark surface.

## What is actually worth carrying

**The RLM reproduced the document's own off-by-one.** That is the interesting
failure, because it is the *document* that is misleading, not the task. A reader
who trusts the prose gets four.

The census got five, and not by being cleverer — by cross-checking **three**
independent signals that a chunk-and-summarise pass has no reason to connect:

1. the two „vier" statements in the framing text,
2. the parenthetical at L96 that reconciles them,
3. the duplicate `### A.` heading — ^[L98] „A. Guardian Kairos" and ^[L110]
   „A. Guardian Sophia" both sit under section IV.

Signal 3 is a *structural* artifact, not a semantic one. It is in
`rules/structure.py`'s output and in no summary of the text.

**So the argument this measurement supports is narrow and real:** when the
question is a count, and the document contradicts itself about that count, the
answer depends on noticing structure the prose does not state. That is what the
census step is for, and it is the part an RLM's slice-and-summarise loop is
weakest at — not because the model is weak, but because the connecting evidence
is spread across L15, L96, L98, L110 and L135.

## What this does not argue

Nothing here says an LM should be kept out of this pipeline. Two models got it
right in one shot. It says the *count* questions are the risky ones, and that a
verification pass for them should check structure rather than re-read prose.

## Cost note

The `claude -p` bridge re-creates prompt cache per process — a trivial call
measured $0.078. An RLM loop is many such calls. Budget before looping.
