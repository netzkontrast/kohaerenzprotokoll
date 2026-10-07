---
document: openai-math-contents
against: 110 pages, 17 conflicts
ran: "2026-10-07"
candidates: 202
decisions: 198
by_lookup: 192
judgements: 6
new_pages: 8
new_readings: 10
---

# Reconciliation 205 — `openai-math-contents` against the wiki

`python3 scripts/reconcile.py openai-math-contents`

202 candidates, 198 decisions — **192 by lookup, 6 to judgement**. Dated 2026-10-06 by the manifest. The manuscript map of github.com/openai/math (decision 026): it calls itself „Mathematics manuscript collection“ ^[openai-math-contents.md:L11] and holds „722 manuscripts covering 372 result families.“ ^[openai-math-contents.md:L13] Each family's description reports its result in the collection's voice as proved, disproved or constructed; each abstract speaks for its manuscript. It names no producer and no verification, and claims no standing beyond reporting.

## New pages

`birch-swinnerton-dyer`, `hilberts-tenth-problem`, `hodge-conjecture`, `langlands`, `mezard-parisi-formula`, `navier-stokes`, `quasi-riemann-hypothesis`, `unique-games-conjecture`. Eight of 189 new terms, chosen as the author asked — the most important: the two results the readme names as exceptions (quasi-Riemann, Hodge, which also took the readme's line L52), two of the oldest open problems the catalogue claims (Hilbert's tenth over ℚ, Birch–Swinnerton-Dyer in low Selmer corank), the Unique Games Conjecture and the Mézard–Parisi formula (each with a reasoning summary still to be read), the Navier–Stokes construction of a fluid that computes, and Langlands, which the novel's own sources already write. Each lead says it is a borrowed concept and not the novel's world. The other 181 stay in the census with their counts.

## Judgements

J126, J127, recorded in `Plan/runs/judgements.jsonl`. J126: a prefix naming a weaker statement makes a different term — the Riemann hypothesis is no alias of the quasi-Riemann page. J127: an eponym inside a result's name is a different term; `companion paper` is the catalogue's `companion`. `Lean` was settled by J124.

## Readings — 10 pages

`birch-swinnerton-dyer`, `hilberts-tenth-problem`, `hodge-conjecture`, `langlands`, `lean-formalization`, `mathematics-manuscript-collection`, `mezard-parisi-formula`, `navier-stokes`, `quasi-riemann-hypothesis`, `unique-games-conjecture`.

No chapter page.
`plot.md` cites it nowhere.
Conflicts with an entry from it: none. Questions: none.

## Sweep

`Simulation` L1347 occurrence — a family title, one-tape time simulation by a machine — the computational sense, not the novel's simulated world.

## What the readers noticed and no record holds

The reader found that `read.py --count` does not fold the typographic apostrophe of the headings into the straight one of the abstracts, so `Milne's rationality conjecture` counts its heading separately; that `--find` drops fragments under four characters; and that the catalogue's heading numbers skip five values.
