# 018 — The open process questions, answered by the session on the author's delegation

**Date:** 2026-09-30 · **Decided by:** the session, on the author's delegation · **Status:** in use

## What was asked

> Alle anderen Fragen darfst du dir erst mal selbst beantworten

> Glaub An dich

The delegation covers the questions this session had put to the author and that decisions
016 and 017 left open. It does **not** cover a Weiche (W1–W16, WP): those stay the
author's (decision 006, P0) and run as `PROVISIONAL` with an `ALT` line (decision 016).
Every answer below is revisable by one word from the author.

## What was chosen

| question | answer | why |
|---|---|---|
| Sperren-Blatt first, or K0–K4 first? | **Neither before the missing sheets:** prepare W12 and W15 with `ask`, then the Sperren-Blatt, then put K0–K4 and the Sperren-Blatt to the author in one round | `askdb.py sheets` shows W12 and W15 named by other sheets with no sheet of their own, and the sheets form a cycle; a round that cannot see them would be decided blind |
| Where to cut the W3–W10 cycle | **W7 first** in round 1 | it unlocks five sheets, more than any other (`askdb.py sheets`) |
| Default `ask` backend | **claude-cli with Sonnet** | the only one with enforced isolation; 8/8 quotations placed in the first trial |
| GraphQLite's reach | **`ask` and the sheets; `graphrag.py` keeps its own PageRank** until a parity bench shows GraphQLite at least as good | P6: one encoding only after the numbers |
| Free models and Jules | **trials beside every bench run**, never the only answer to a question | decision 017 allows them; the first free-model trial placed 1 of 2 |
| The stale prose numbers on main | **not touched** by this session: they record step 6 of the pipeline plan half done (documents with a census but no reconciliation), which is another session's work in progress | correcting them would hide a true state |

## What would change our mind

A word from the author on any row; a bench showing claude-cli worse than a free model; W12
or W15 turning out not to be needed once written.
