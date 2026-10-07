---
document: openai-math-readme
against: 106 pages, 17 conflicts
ran: "2026-10-07"
candidates: 51
decisions: 43
by_lookup: 31
judgements: 12
new_pages: 4
new_readings: 4
---

# Reconciliation 204 — `openai-math-readme` against the wiki

`python3 scripts/reconcile.py openai-math-readme`

51 candidates, 43 decisions — **31 by lookup, 12 to judgement**. Dated 2026-10-06 by the manifest. The short readme of github.com/openai/math, the first source from outside Drive (decision 026), in English and in an unnamed „we“. It says what the repository holds — „mathematical manuscripts and supporting proof artifacts produced by an internal OpenAI model“ ^[openai-math-readme.md:L13] — and claims no more standing for them than „different stages of verification“ ^[openai-math-readme.md:L17]. Nothing in it is about the novel.

## New pages

`internal-openai-model`, `lean-formalization`, `mathematics-manuscript-collection`, `reasoning-summaries`. Four, all real-world entities and named so in each lead: the model that produced the collection, the collection and its families, the Lean formalizations that verify part of it, and the reasoning summaries. Each is read here, not merely named. The Riemann zeta zero-free region and the Hodge Conjecture (L52) waited for the manuscript map, which defines them; when document 205 opened `quasi-riemann-hypothesis` and `hodge-conjecture`, this line went on both. Not promoted, with lines in `reconcile.json`: `OpenAI` alone (J122), the ten table titles (J125), and the file pointers.

## Judgements

J122, J123, J124, J125, recorded in `Plan/runs/judgements.jsonl`. J122: an adjective of status never makes a second referent, and an institution named only inside its product's name is an occurrence. J123: a qualifier naming a different apparatus makes a second term. J124: a tool named only as the qualifier of its products is read on the product's page, and a surface that folds onto a common English word (`lean`) is no alias. J125: a result's title and the object inside it are two terms, and a title in a table is an occurrence.

## Readings — 4 pages

`internal-openai-model`, `lean-formalization`, `mathematics-manuscript-collection`, `reasoning-summaries`.

No chapter page.
`plot.md` cites it nowhere.
Conflicts with an entry from it: none. Questions: none.

## Sweep

No hit the census did not list.

## What the readers noticed and no record holds

The reader found that a markdown link counts twice (its text and its target), so `overview` and `preprints` stand at 2 for one use, and that the document spells `catalogue` and `catalog`.
