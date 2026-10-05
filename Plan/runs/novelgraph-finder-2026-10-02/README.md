# novelgraph as an `ask` finder — gate G2, step 6 of SPEC.md, 2026-10-02

`ask.route` has a finder `novelgraph` (off by default). It takes novelgraph's hybrid `heading@v1` chunks, 8 per
question, and turns every line of each chunk into a hit for the pack. It runs in novelgraph's own venv through
`novelgraph search --batch`, one subprocess that loads the model once. A finder that was asked for and cannot run
refuses; it is never skipped. `g2.py` measures it against the default finders on the 24 frozen cases at the same
budget (72 000 bytes over the whole pack). No model call, no corpus reading.

## Paired comparison at the same budget

| | default finders | + novelgraph | paired Δ (90 % CI) | better / worse |
|---|---|---|---|---|
| line recall | 0.113 | 0.130 | **+0.018** [+0.007, +0.029] | 8 / 1 |
| document recall | 0.324 | 0.340 | **+0.016** [+0.007, +0.026] | 9 / 1 |

What the extra finder adds and what it pushes out:

- **Novel gold:** 32 gold lines the novelgraph pack sends and the default pack does not. 14 of them lie in documents
  that only novelgraph found; those are the closest thing this bench has to discovery.
- **Displaced:** 5 gold lines the default pack sent and the novelgraph pack had no room for.
- **Documents only novelgraph found:** 86 sent, over the 24 cases.
- **Cost:** about 10 s for the first question, while the model loads; 8 s for the other 23 in one batch. A single
  `ask.py pack` call pays the cold price every time.

## Reading it

The interval excludes zero, and only one case is worse. By SPEC.md §6, G2 asks for exactly this: novel gold at an
equal byte budget, with the cost reported. G1 still limits what this measurement can claim:
- the cases are one dependent cluster;
- 92 % of their gold is lines the wiki pages already quote.

The 14 lines from novelgraph-only documents are the part the circularity does not explain.

**The default stays off.** The finder defaults are the author's (NOW.md question 2(4)). Turning it on would make
`.venv-novelgraph` and a built index — 0.5 GB of embedder and about 3 minutes from nothing — a requirement of every
`ask` call. The measurement and the trade go to the author. `ask.py bench --with novelgraph` reproduces it.
