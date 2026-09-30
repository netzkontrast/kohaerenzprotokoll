# E2b — the normalised co-mention relation

E2 found that pages standing in one paragraph, weighted by their normalised pointwise mutual information over documents, raise recall@8 at a large weight while the raw pair count lowers it. This sweeps what that depends on: the number of documents a pair must stand together in (2, 3, 5), the scale (npmi, its square), the sparsification (every pair, or a pair kept only when it is among either page's 5, 10 or 20 strongest), and the weight against the stated `links` at 1.0. The 14 best of 96 configurations by recall@8 + recall@16 are printed; every one is a row of the ledger. Choosing the best of many on the cases it is scored on overstates it, so the last rows leave each case out and let the other 23 choose.

### recall of the wiki's own labels

| configuration | recall@8 | precision@8 | recall@16 | vs the floor: mean, 90 % interval | up / down / same |
|---|---|---|---|---|---|
| floor: the stated relations at their default weights | 0.688 | 0.273 | 0.810 | +0.000 [+0.000, +0.000] | 0 / 0 / 24 |
| ≥2 documents, npmi, every pair (239 pairs), weight 30.0 | 0.788 | 0.381 | 0.836 | +0.100 [+0.030, +0.177] | 6 / 1 / 17 |
| ≥2 documents, npmi, top 10 per page (231 pairs), weight 30.0 | 0.788 | 0.381 | 0.836 | +0.100 [+0.030, +0.177] | 6 / 1 / 17 |
| ≥2 documents, npmi, top 20 per page (239 pairs), weight 30.0 | 0.788 | 0.381 | 0.836 | +0.100 [+0.030, +0.177] | 6 / 1 / 17 |
| ≥3 documents, npmi, every pair (215 pairs), weight 30.0 | 0.788 | 0.381 | 0.836 | +0.100 [+0.030, +0.177] | 6 / 1 / 17 |
| ≥3 documents, npmi, top 10 per page (208 pairs), weight 30.0 | 0.788 | 0.381 | 0.836 | +0.100 [+0.030, +0.177] | 6 / 1 / 17 |
| ≥3 documents, npmi, top 20 per page (215 pairs), weight 30.0 | 0.788 | 0.381 | 0.836 | +0.100 [+0.030, +0.177] | 6 / 1 / 17 |
| ≥2 documents, npmi², every pair (239 pairs), weight 30.0 | 0.794 | 0.381 | 0.829 | +0.105 [+0.040, +0.178] | 6 / 0 / 18 |
| ≥2 documents, npmi², top 10 per page (231 pairs), weight 30.0 | 0.794 | 0.381 | 0.829 | +0.105 [+0.040, +0.178] | 6 / 0 / 18 |
| ≥2 documents, npmi², top 20 per page (239 pairs), weight 30.0 | 0.794 | 0.381 | 0.829 | +0.105 [+0.040, +0.178] | 6 / 0 / 18 |
| ≥3 documents, npmi², every pair (215 pairs), weight 30.0 | 0.794 | 0.381 | 0.829 | +0.105 [+0.040, +0.178] | 6 / 0 / 18 |
| ≥3 documents, npmi², top 10 per page (208 pairs), weight 30.0 | 0.794 | 0.381 | 0.829 | +0.105 [+0.040, +0.178] | 6 / 0 / 18 |
| ≥3 documents, npmi², top 20 per page (215 pairs), weight 30.0 | 0.794 | 0.381 | 0.829 | +0.105 [+0.040, +0.178] | 6 / 0 / 18 |
| ≥5 documents, npmi², every pair (187 pairs), weight 30.0 | 0.794 | 0.381 | 0.829 | +0.105 [+0.040, +0.178] | 6 / 0 / 18 |
| ≥5 documents, npmi², top 10 per page (182 pairs), weight 30.0 | 0.794 | 0.381 | 0.829 | +0.105 [+0.040, +0.178] | 6 / 0 / 18 |
| chosen leaving each case out, over all 96 configurations and the floor | 0.752 | 0.352 | 0.819 | +0.064 [-0.013, +0.146] | 6 / 2 / 16 |
| co-mention alone, ≥2 documents, every pair | 0.757 | 0.392 | 0.807 | +0.069 [-0.004, +0.151] | 6 / 3 / 15 |
| co-mention alone, ≥3 documents, every pair | 0.716 | 0.420 | 0.786 | +0.027 [-0.066, +0.123] | 6 / 5 / 13 |
| co-mention alone, ≥5 documents, every pair | 0.736 | 0.426 | 0.797 | +0.048 [-0.034, +0.138] | 6 / 4 / 14 |

Leaving each case out, the configuration the other 23 preferred was: ≥2 documents, npmi, every pair, weight 30.0 ×20, ≥2 documents, npmi², every pair, weight 30.0 ×2, ≥2 documents, npmi, every pair, weight 10.0 ×1, ≥5 documents, npmi, top 5 per page, weight 30.0 ×1.
