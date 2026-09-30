# 017 — `ask` answers are logged and treated like sources; OpenRouter and Jules may answer

**Date:** 2026-09-30 · **Decided by:** the author, in two sentences · **Status:** being built

## What was asked

`Plan/concept/ask-sources_2026-09-30.md` §6 asked five questions: free models, Jules, the
default backend, how an answer may be used, GraphQLite's reach. The author answered:

> Die Antworten werden protokolliert und sind wie sources zu behandeln

> Darüber hinaus dürfen auch openrouter und Jules für entsprechende Fragen genutzt werden - die nutzt Du immer vielleicht erst mal als Probelauf - hier kannst Du frei experimentieren

## What was chosen

1. **An answer is logged and treated like a source.** It lands once, is never edited
   afterwards, carries a checksum and an entry in its own manifest, and is written by
   code only — the rules of `Sources/drive/`. It is cited with a line like any source,
   so `quotes.py` can check a quotation of it.
   **Where:** `Sources/ask/<id>.md`, manifest `Sources/ask/manifest.jsonl`, written by
   `scripts/ask.py land` and nothing else; `.claude/settings.json` denies hand edits
   there as it does for `Sources/drive/`. Its tier is `M-ask`: a model's reading of
   other sources, never the author's. The corpus counts (`sources.total`, `landed`) do
   not include it.
2. **OpenRouter's free models may receive `ask` packs**, whatever documents the pack
   holds. `Plan/runs/route/consent.json` gains a purpose entry; `route.py` honours it
   for purpose `ask` only. Free only and `data_collection: deny` stay as in decision 007.
3. **Jules may answer `ask` questions**; each dispatch names this decision as its
   approval. Jules holds the whole repository, corpus included.
4. **Both run as trials first**, alongside the default, and the session may experiment
   freely with them. A trial's answer lands like any other, with its backend named.

## Read as unanswered, and so the proposal's defaults

- **Default backend:** claude-cli with Sonnet (the only one whose isolation is enforced).
- **GraphQLite's reach:** `ask` and the decision sheets; replacing `graphrag.py`'s own
  PageRank waits on the parity bench and another word from the author.

## What would change our mind

Answers that land with quotations the checker cannot place; a free model or Jules
leaking the pack's purpose into unrelated work; the parity bench showing GraphQLite
worse than the code it would replace.
