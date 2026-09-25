# 011 — DSPy runs may use Claude through the CLI, and OpenRouter's free models through route.py

**Date:** 2026-09-24/25 · **Decided by:** the author — „Use dspy Optimierung on the Scripts", then „Add openrouter free Models in the mix" — with the session applying the repository's precedent for Claude · **Status:** chosen; enforced by `scripts/lmrun.py` (`approval=`), `scripts/claude_lm.py` (no tools) and `scripts/route.py` (free only, `data_collection: deny`, the twelve-word guard, a pinned model); reversible by the author at any time

## What was chosen

The DSPy programs in `scripts/` had never run against a real model, because every
model they could reach was a third party and each run waited on the author's yes
(`NOW.md`, *Which model runs are allowed*). The author asked for the optimizers to
run, and then for OpenRouter's free models to be part of it. Two routes:

| route | what it is | what may reach it | held by |
|---|---|---|---|
| `claude-cli/<haiku\|sonnet\|opus>` | Claude through `claude -p`, the CLI that runs this session | anything a DSPy program here sends | `claude_lm.py`: no tools, no MCP, no skills, no settings, no session written, an empty working directory |
| `route/<free model>` | an OpenRouter model whose listed price is 0, through `route.py`'s proxy, **pinned** to that model | what `pairs.py`'s program sends: two term surfaces, the person's recorded rule sentences, the instructions and the optimizers' own prompts built from them — **never a passage of a document** | `route.py`: free only, `data_collection: deny`, every call recorded, a charged call stops the run, and any twelve consecutive words of a landed document outside decision 007's two refused before sending |

Every call through either route still goes through `lmrun.call` or the optimizer
it runs inside, and `lmrun.call` refuses a real model without `approval=`; runs under
this decision pass `approval="decision 011"`.

## Why Claude needs no new yes

The repository already treats Claude as the one model that keeps corpus text
inside its boundary. Document 14's second readers ran „with Claude as the model so
no text left" (`CLAUDE.md`), the entity lists are Haiku readers, and `NOW.md` says of
the new tools as second readers: „No corpus text leaves: the model is Claude."
`claude -p` is the same provider, reached the same way this session is; its JSON
reports `"provider": "firstParty"`. This decision applies that precedent to DSPy
rather than extending it — the author may narrow it.

**What it costs is the author's.** Claude calls draw on the same usage as this
session: the session's own readers hit the account's usage limit on 2026-09-24, and
nothing about a CLI call is free. Every run records its cost (`total_cost_usd`,
summed into the `baselines.jsonl` row), and a run is sized before it starts.

## Why the free models are pinned

`route.py`'s proxy answers any request with *some* free model — the right thing for
a tool that only needs an answer. A run that measures a model must not be answered
by another one (P16), so a caller key ending `:<attempt>:pin` gets the model it
names or nothing; a rate-limited pinned model is waited for, and a daily limit ends
the call as unreached (P15). Because the proxy replays a recorded answer to an
identical request, each repeat of a held-out row is its own attempt number (P18).

## What it does not cover

- A passage, a line or a whole document to a free model: `graphrag.py ask --answer`
  (quotations), `rlm_ingest.py` (a document), and any pair program that carries
  evidence lines. Those run on Claude, or ask again.
- Paid OpenRouter models, and any other provider.
- Anything to Notion.

## What would change our mind

The author. A free endpoint found keeping prompts despite `data_collection: deny`,
or a charged free call (`route.py` already stops the run). For Claude: a usage
limit reached again by a run, which says the runs must be smaller before they are
repeated.
