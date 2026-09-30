# E2c — the wiki's own links as a second label set

91 pages each link or are linked from at least three pages (1011 linked pages in all). For each, the page is the seed, every `links` edge touching it is removed, and the walk ranks the other pages; the gold is the pages it was linked to. The page itself is left out of what it ranks. The floor is the stated relations at their default weights; each row adds the counted co-mention relation (239 pairs standing in one paragraph in at least two documents, weighted by the scale named) at the weight given. The labels are the same hand's as the pages; the relation is counted over the source documents and never over the wiki, so no link enters it.

### recall of the wiki's own links

| configuration | recall@8 | precision@8 | recall@16 | vs the floor: mean, 90 % interval | up / down / same |
|---|---|---|---|---|---|
| floor: the stated relations at their default weights, the page's own links removed | 0.395 | 0.437 | 0.572 | +0.000 [+0.000, +0.000] | 0 / 0 / 91 |
| co-mention, ≥2 documents, npmi², weight 1.0 | 0.407 | 0.448 | 0.587 | +0.012 [+0.002, +0.025] | 12 / 4 / 75 |
| co-mention, ≥2 documents, npmi², weight 3.0 | 0.421 | 0.459 | 0.594 | +0.025 [+0.008, +0.044] | 22 / 6 / 63 |
| co-mention, ≥2 documents, npmi², weight 10.0 | 0.416 | 0.460 | 0.588 | +0.021 [-0.002, +0.043] | 27 / 11 / 53 |
| co-mention, ≥2 documents, npmi², weight 30.0 | 0.391 | 0.434 | 0.556 | -0.004 [-0.037, +0.029] | 28 / 28 / 35 |
| co-mention, ≥2 documents, npmi², weight 100.0 | 0.323 | 0.357 | 0.496 | -0.072 [-0.108, -0.037] | 18 / 50 / 23 |
| co-mention, ≥2 documents, npmi, weight 1.0 | 0.415 | 0.456 | 0.598 | +0.020 [+0.001, +0.039] | 20 / 4 / 67 |
| co-mention, ≥2 documents, npmi, weight 3.0 | 0.427 | 0.468 | 0.599 | +0.032 [+0.012, +0.052] | 26 / 10 / 55 |
| co-mention, ≥2 documents, npmi, weight 10.0 | 0.394 | 0.445 | 0.577 | -0.001 [-0.030, +0.026] | 27 / 21 / 43 |
| co-mention, ≥2 documents, npmi, weight 30.0 | 0.354 | 0.391 | 0.533 | -0.041 [-0.077, -0.005] | 25 / 40 / 26 |
| co-mention, ≥2 documents, npmi, weight 100.0 | 0.258 | 0.308 | 0.434 | -0.137 [-0.178, -0.098] | 16 / 60 / 15 |
| co-mention, ≥2 documents, one per pair, weight 0.1 | 0.398 | 0.438 | 0.589 | +0.003 [-0.007, +0.012] | 4 / 3 / 84 |
| co-mention, ≥2 documents, one per pair, weight 0.3 | 0.411 | 0.449 | 0.600 | +0.016 [+0.002, +0.031] | 13 / 7 / 71 |
| co-mention, ≥2 documents, one per pair, weight 1.0 | 0.426 | 0.467 | 0.584 | +0.031 [+0.007, +0.056] | 28 / 11 / 52 |
| co-mention, ≥2 documents, one per pair, weight 3.0 | 0.401 | 0.446 | 0.582 | +0.006 [-0.026, +0.036] | 30 / 25 / 36 |
| co-mention, ≥2 documents, one per pair, weight 10.0 | 0.343 | 0.379 | 0.535 | -0.052 [-0.088, -0.018] | 20 / 40 / 31 |
| co-mention, ≥2 documents, log2(1+documents), weight 0.1 | 0.417 | 0.462 | 0.586 | +0.022 [+0.003, +0.041] | 23 / 8 / 60 |
| co-mention, ≥2 documents, log2(1+documents), weight 0.3 | 0.413 | 0.462 | 0.575 | +0.018 [-0.009, +0.044] | 27 / 13 / 51 |
| co-mention, ≥2 documents, log2(1+documents), weight 1.0 | 0.393 | 0.434 | 0.544 | -0.002 [-0.035, +0.030] | 30 / 28 / 33 |
| co-mention, ≥2 documents, log2(1+documents), weight 3.0 | 0.363 | 0.402 | 0.522 | -0.032 [-0.068, +0.002] | 27 / 37 / 27 |
| co-mention, ≥2 documents, log2(1+documents), weight 10.0 | 0.337 | 0.371 | 0.496 | -0.058 [-0.096, -0.020] | 26 / 46 / 19 |
| chosen leaving each case out, over all 20 configurations and the floor | 0.427 | 0.468 | 0.599 | +0.032 [+0.012, +0.052] | 26 / 10 / 55 |
| co-mention alone (every stated type off), npmi², weight 1 | 0.198 | 0.316 | 0.300 | -0.197 [-0.243, -0.152] | 14 / 66 / 11 |

Leaving each case out, the configuration the others preferred was: npmi 3.0 ×91.

### recall of the wiki's own links, with the page pairs the HyperExtract contracts read added

| configuration | recall@8 | precision@8 | recall@16 | vs the floor: mean, 90 % interval | up / down / same |
|---|---|---|---|---|---|
| floor: the stated relations at their default weights, the page's own links removed | 0.395 | 0.437 | 0.572 | +0.000 [+0.000, +0.000] | 0 / 0 / 91 |
| causal pairs (15 pairs, 4 not already `links`), weight 0.3 | 0.395 | 0.438 | 0.573 | +0.000 [+0.000, +0.001] | 1 / 0 / 90 |
| causal pairs (15 pairs, 4 not already `links`), weight 1.0 | 0.397 | 0.442 | 0.570 | +0.002 [+0.000, +0.004] | 3 / 0 / 88 |
| causal pairs (15 pairs, 4 not already `links`), weight 3.0 | 0.398 | 0.441 | 0.568 | +0.003 [+0.000, +0.007] | 5 / 2 / 84 |
| contrast pairs (22 pairs, 5 not already `links`), weight 0.3 | 0.399 | 0.441 | 0.575 | +0.003 [+0.000, +0.008] | 3 / 0 / 88 |
| contrast pairs (22 pairs, 5 not already `links`), weight 1.0 | 0.403 | 0.446 | 0.575 | +0.008 [+0.002, +0.014] | 8 / 1 / 82 |
| contrast pairs (22 pairs, 5 not already `links`), weight 3.0 | 0.404 | 0.444 | 0.565 | +0.009 [+0.002, +0.017] | 8 / 3 / 80 |
| role pairs (8 pairs, 4 not already `links`), weight 0.3 | 0.395 | 0.437 | 0.571 | +0.000 [+0.000, +0.000] | 0 / 0 / 91 |
| role pairs (8 pairs, 4 not already `links`), weight 1.0 | 0.395 | 0.440 | 0.571 | +0.000 [+0.000, +0.001] | 2 / 0 / 89 |
| role pairs (8 pairs, 4 not already `links`), weight 3.0 | 0.395 | 0.438 | 0.571 | +0.000 [-0.000, +0.001] | 2 / 1 / 88 |
| every relation pair (42 pairs, 12 not already `links`), weight 0.3 | 0.399 | 0.441 | 0.576 | +0.004 [+0.001, +0.009] | 3 / 0 / 88 |
| every relation pair (42 pairs, 12 not already `links`), weight 1.0 | 0.407 | 0.453 | 0.573 | +0.012 [+0.005, +0.019] | 10 / 1 / 80 |
| every relation pair (42 pairs, 12 not already `links`), weight 3.0 | 0.407 | 0.452 | 0.565 | +0.012 [+0.003, +0.022] | 13 / 6 / 72 |
| co-read: pages one claim holds together (106 pairs, 44 not already `links`), weight 0.3 | 0.399 | 0.441 | 0.584 | +0.004 [-0.002, +0.011] | 6 / 3 / 82 |
| co-read: pages one claim holds together (106 pairs, 44 not already `links`), weight 1.0 | 0.415 | 0.455 | 0.569 | +0.020 [+0.006, +0.035] | 14 / 4 / 73 |
| co-read: pages one claim holds together (106 pairs, 44 not already `links`), weight 3.0 | 0.416 | 0.453 | 0.542 | +0.021 [+0.005, +0.038] | 22 / 13 / 56 |

**How the relation and the links overlap.** The wiki holds 512 linked pairs of pages; the relation holds 239 pairs, of which 102 are linked (43%); and 102 of the 512 links (20%) stand in one paragraph in at least two documents.

**Pairs the corpus holds together that no page links** — the 40 with the highest normalised PMI. A proposal for the author to read, never a link: a link is never inferred.

| pair | documents | npmi |
|---|---|---|
| `kiko` — `nyx` | 222 | 0.75 |
| `archiv-der-grenzen` — `mnemosyne-server-architektur` | 4 | 0.72 |
| `cerberus` — `kairos` | 106 | 0.68 |
| `kiko` — `lex` | 210 | 0.65 |
| `kairos` — `logos` | 102 | 0.57 |
| `partnerin` — `ueberraum` | 6 | 0.57 |
| `kaels-wohneinheit` — `vergessener-schrein` | 3 | 0.57 |
| `personas` — `ueberraum` | 8 | 0.55 |
| `cerberus` — `sophia` | 80 | 0.54 |
| `grenzfeste` — `moeglichkeits-garten` | 29 | 0.53 |
| `lex` — `rhys` | 151 | 0.53 |
| `grenzfeste` — `resonanz-landschaft` | 31 | 0.52 |
| `moeglichkeits-garten` — `resonanz-landschaft` | 25 | 0.52 |
| `argus` — `isabelle` | 69 | 0.51 |
| `lia` — `moros` | 97 | 0.51 |
| `isabelle` — `moros` | 79 | 0.50 |
| `alex` — `lia` | 93 | 0.49 |
| `alex` — `rhys` | 104 | 0.49 |
| `logos` — `sophia` | 80 | 0.48 |
| `alex` — `argus` | 84 | 0.46 |
| `kiko` — `moros` | 132 | 0.46 |
| `alex` — `isabelle` | 73 | 0.45 |
| `argus` — `lia` | 76 | 0.44 |
| `kiko` — `rhys` | 131 | 0.43 |
| `alex` — `lex` | 132 | 0.42 |
| `lia` — `rhys` | 88 | 0.42 |
| `alex` — `moros` | 93 | 0.41 |
| `argus` — `rhys` | 82 | 0.41 |
| `nyx` — `rhys` | 135 | 0.41 |
| `moros` — `rhys` | 95 | 0.40 |
| `argus` — `lex` | 111 | 0.40 |
| `mnemosyne-server-architektur` — `truth-rotation` | 3 | 0.40 |
| `moros` — `nyx` | 126 | 0.37 |
| `konstrukt-stadt` — `resonanz-landschaft` | 36 | 0.36 |
| `algorithmische-melancholie` — `truth-rotation` | 13 | 0.36 |
| `rhys` — `selene` | 92 | 0.35 |
| `alex` — `kiko` | 115 | 0.35 |
| `lex` — `moros` | 123 | 0.34 |
| `silas` — `telefon-stille` | 11 | 0.33 |
| `argus` — `moros` | 71 | 0.33 |
