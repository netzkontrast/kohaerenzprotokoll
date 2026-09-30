# E5 — what the HyperExtract contracts read

620 claims from the contracts' pilot runs are in the store; they touch 36 of the wiki's 106 pages, and 25 of the 48 distinct gold pages of the 24 cases. From them: page pairs a claim relates (its source and its target each contain a page), and pairs of pages one claim holds together. Each set is added to every case's graph as a term–term relation beside the stated ones, which keep their default weights. The pilot ran eight documents, so the size of what could move is bounded by the pairs, not by the weights.

### recall of the wiki's own labels

| configuration | recall@8 | precision@8 | recall@16 | vs the floor: mean, 90 % interval | up / down / same |
|---|---|---|---|---|---|
| floor: the stated relations at their default weights | 0.688 | 0.273 | 0.810 | +0.000 [+0.000, +0.000] | 0 / 0 / 24 |
| contrast pairs (6 pairs, 1 not already `links`), weight 0.1 | 0.688 | 0.273 | 0.810 | +0.000 [+0.000, +0.000] | 0 / 0 / 24 |
| contrast pairs (6 pairs, 1 not already `links`), weight 0.3 | 0.688 | 0.273 | 0.810 | +0.000 [+0.000, +0.000] | 0 / 0 / 24 |
| contrast pairs (6 pairs, 1 not already `links`), weight 1.0 | 0.688 | 0.273 | 0.810 | +0.000 [+0.000, +0.000] | 0 / 0 / 24 |
| contrast pairs (6 pairs, 1 not already `links`), weight 3.0 | 0.688 | 0.273 | 0.810 | +0.000 [+0.000, +0.000] | 0 / 0 / 24 |
| role pairs (8 pairs, 4 not already `links`), weight 0.1 | 0.688 | 0.273 | 0.810 | +0.000 [+0.000, +0.000] | 0 / 0 / 24 |
| role pairs (8 pairs, 4 not already `links`), weight 0.3 | 0.688 | 0.273 | 0.810 | +0.000 [+0.000, +0.000] | 0 / 0 / 24 |
| role pairs (8 pairs, 4 not already `links`), weight 1.0 | 0.688 | 0.273 | 0.810 | +0.000 [+0.000, +0.000] | 0 / 0 / 24 |
| role pairs (8 pairs, 4 not already `links`), weight 3.0 | 0.694 | 0.278 | 0.810 | +0.006 [+0.000, +0.018] | 1 / 0 / 23 |
| every relation pair (19 pairs, 5 not already `links`), weight 0.1 | 0.688 | 0.273 | 0.810 | +0.000 [+0.000, +0.000] | 0 / 0 / 24 |
| every relation pair (19 pairs, 5 not already `links`), weight 0.3 | 0.688 | 0.273 | 0.810 | +0.000 [+0.000, +0.000] | 0 / 0 / 24 |
| every relation pair (19 pairs, 5 not already `links`), weight 1.0 | 0.694 | 0.278 | 0.810 | +0.006 [+0.000, +0.018] | 1 / 0 / 23 |
| every relation pair (19 pairs, 5 not already `links`), weight 3.0 | 0.694 | 0.278 | 0.806 | +0.006 [+0.000, +0.018] | 1 / 0 / 23 |
| co-read: pages one claim holds together (38 pairs, 12 not already `links`), weight 0.1 | 0.688 | 0.273 | 0.810 | +0.000 [+0.000, +0.000] | 0 / 0 / 24 |
| co-read: pages one claim holds together (38 pairs, 12 not already `links`), weight 0.3 | 0.694 | 0.278 | 0.806 | +0.006 [+0.000, +0.018] | 1 / 0 / 23 |
| co-read: pages one claim holds together (38 pairs, 12 not already `links`), weight 1.0 | 0.694 | 0.278 | 0.806 | +0.006 [+0.000, +0.018] | 1 / 0 / 23 |
| co-read: pages one claim holds together (38 pairs, 12 not already `links`), weight 3.0 | 0.653 | 0.273 | 0.810 | -0.036 [-0.119, +0.012] | 1 / 1 / 22 |

Gold pages a case could not reach before and can reach with the pairs added (walking the new type at weight 1): every relation pair: 0, co-read: pages one claim holds together: 0.
