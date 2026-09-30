# E4 — the hubs

The diagnosis (`diagnose.md`) found most missed pages reached by the walk and outranked by eight others, and the pages that outrank them are the hubs — `aegis`, `juna`, `kael`, `vortex`. Two corrections, both in `graphrag.pagerank` and both off by default: **hub** divides each node's rank by its degree to the power a (the walk's stationary mass grows with degree); **spec** divides each seed's restart weight by its degree to the power b, so a seed touching everything pulls less (HippoRAG's node specificity). The same 24 cases, seeds and stated weights throughout.

### recall of the wiki's own labels

| configuration | recall@8 | precision@8 | recall@16 | vs the floor: mean, 90 % interval | up / down / same |
|---|---|---|---|---|---|
| floor: no correction | 0.688 | 0.273 | 0.810 | +0.000 [+0.000, +0.000] | 0 / 0 / 24 |
| hub 0.0, spec 0.25 | 0.688 | 0.273 | 0.806 | +0.000 [+0.000, +0.000] | 0 / 0 / 24 |
| hub 0.0, spec 0.5 | 0.640 | 0.261 | 0.802 | -0.049 [-0.132, +0.000] | 0 / 2 / 22 |
| hub 0.0, spec 1.0 | 0.629 | 0.250 | 0.792 | -0.059 [-0.139, -0.004] | 0 / 3 / 21 |
| hub 0.1, spec 0.0 | 0.694 | 0.278 | 0.816 | +0.006 [+0.000, +0.018] | 1 / 0 / 23 |
| hub 0.1, spec 0.25 | 0.694 | 0.278 | 0.816 | +0.006 [+0.000, +0.018] | 1 / 0 / 23 |
| hub 0.1, spec 0.5 | 0.633 | 0.256 | 0.808 | -0.056 [-0.139, +0.000] | 0 / 2 / 22 |
| hub 0.1, spec 1.0 | 0.629 | 0.250 | 0.804 | -0.059 [-0.139, -0.004] | 0 / 3 / 21 |
| hub 0.25, spec 0.0 | 0.709 | 0.290 | 0.816 | +0.021 [+0.005, +0.042] | 3 / 0 / 21 |
| hub 0.25, spec 0.25 | 0.692 | 0.278 | 0.812 | +0.004 [-0.014, +0.021] | 2 / 1 / 21 |
| hub 0.25, spec 0.5 | 0.644 | 0.267 | 0.808 | -0.045 [-0.128, +0.015] | 2 / 2 / 20 |
| hub 0.25, spec 1.0 | 0.634 | 0.256 | 0.804 | -0.055 [-0.136, +0.005] | 1 / 3 / 20 |
| hub 0.5, spec 0.0 | 0.699 | 0.284 | 0.818 | +0.011 [-0.017, +0.040] | 4 / 2 / 18 |
| hub 0.5, spec 0.25 | 0.654 | 0.273 | 0.808 | -0.035 [-0.118, +0.030] | 4 / 4 / 16 |
| hub 0.5, spec 0.5 | 0.654 | 0.273 | 0.814 | -0.035 [-0.118, +0.030] | 4 / 4 / 16 |
| hub 0.5, spec 1.0 | 0.647 | 0.267 | 0.810 | -0.041 [-0.124, +0.026] | 4 / 4 / 16 |
| hub 0.75, spec 0.0 | 0.685 | 0.273 | 0.804 | -0.003 [-0.050, +0.046] | 2 / 3 / 19 |
| hub 0.75, spec 0.25 | 0.685 | 0.273 | 0.800 | -0.003 [-0.050, +0.046] | 2 / 3 / 19 |
| hub 0.75, spec 0.5 | 0.683 | 0.273 | 0.778 | -0.005 [-0.055, +0.047] | 3 / 4 / 17 |
| hub 0.75, spec 1.0 | 0.576 | 0.244 | 0.790 | -0.112 [-0.217, -0.017] | 2 / 6 / 16 |
| hub 1.0, spec 0.0 | 0.570 | 0.222 | 0.737 | -0.118 [-0.207, -0.040] | 1 / 7 / 16 |
| hub 1.0, spec 0.25 | 0.570 | 0.222 | 0.737 | -0.118 [-0.207, -0.040] | 1 / 7 / 16 |
| hub 1.0, spec 0.5 | 0.530 | 0.216 | 0.731 | -0.159 [-0.262, -0.062] | 1 / 9 / 14 |
| hub 1.0, spec 1.0 | 0.512 | 0.205 | 0.689 | -0.176 [-0.279, -0.078] | 1 / 10 / 13 |
| chosen leaving each case out (each case scored by the pair the others prefer) | 0.701 | 0.284 | 0.816 | +0.013 [-0.011, +0.038] | 3 / 1 / 20 |

The best pair on all 24 cases is hub 0.25, spec 0.0 — chosen on the cases it is scored on, so an upper bound. Leaving each case out, the pair the other 23 preferred was: hub 0.25 spec 0.0 ×23, hub 0.5 spec 0.0 ×1.
