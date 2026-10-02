# How the `ask` pack spends its budget — 2026-10-01

On the author's „Überlege wie die ask packs optimiert werden können". Three offline measurements on the frozen
cases (`Plan/eval/retrieval-cases-v1.json`, sha256 `b37d8010…`), each case's own record removed from the graph as
`ask.py bench` does. No model, no corpus reading. Gold is the records' cited lines (circular, evaluation audit §0):
these numbers say what the pack *sends*, not what an answer uses, and they are regression measurements.

## 1. The packing step — `pack_variants.py`

The route is held fixed and the packing replayed. `current` reproduces `build_pack` exactly (24 of 24 cases: the
same documents and the same lines).

| budget (chars of windows) | `current` line / doc recall | `body` (no frontmatter anchors) | `ranked` (strongest anchors first under the 60-line cap) | `fill` (trim instead of cut) | `all` |
|---|---|---|---|---|---|
| 15 000 | 0.061 / 0.167 | ±0.000 | ±0.000 | −0.007 [−0.016, +0.002], 1 better / 5 worse | −0.007 |
| 30 000 | 0.081 / 0.225 | ±0.000 | +0.000 (1 / 0) | −0.000 | −0.004 |
| 60 000 | 0.100 / 0.301 | ±0.000 | ±0.000 | ±0.000 | ±0.000 |

**No packing variant improves anything.**

- Frontmatter anchors are real (7 of 1 211 anchors, in 3 cases) but hold no gold.
- The 60-line cap rarely binds.
- At the default budget, 2.4 documents a case are cut; trimming them instead adds nothing.
- At 15 000, trimming is slightly worse: a trimmed document displaces whole later ones that held gold.

## 2. The route's ceiling — `finder_yield.py`

The same anchors, with no budget and no per-document cap: **line recall 0.102, document recall 0.307**. The
60 000-character pack already sends 0.100 — **98 % of what the route finds**. **73 %** of the anchored lines are in
documents that hold no gold line for the case.

| finder | anchors | characters of its spans | gold lines | gold only it reaches | cases with gold | gold per 10 000 chars |
|---|---|---|---|---|---|---|
| `graph-evidence` | 144 | 157 758 | 39 | 33 | 11 | **2.47** |
| `bm25-lines` | 720 | 532 854 | 64 | 51 | 15 | 1.20 |
| `parallel` | 181 | 129 484 | 12 | 10 | 7 | 0.93 |
| `co-mention` | 166 | 403 898 | 14 | 6 | 4 | **0.35** |
| `entity-unread` | 0 | — | — | — | — | no anchor on any of the 24 questions |

## 3. The co-mention finder's share — `finder_budget.py`

The real pack (`build_pack`, 60 000), whole-pack characters.

| setting | line recall | doc recall | gold lines sent | characters per pack | cases better / worse than default |
|---|---|---|---|---|---|
| co-mention 10 paragraphs (default) | 0.1002 | 0.301 | 109 | 48 010 | — |
| co-mention 3 | 0.0973 | 0.298 | 111 | 41 915 (−13 %) | 2 / 1 |
| co-mention off | 0.0957 | 0.289 | 105 | 38 048 (−21 %) | 1 / 3 |

## What follows

1. **Packing is not where recall is lost; routing is.** Optimising the packer for recall is the wrong target.
   Its job is cost and honesty:
   - one budget over the whole serialized pack;
   - an explicit `incomplete`;
   - frontmatter dropped;
   - duplicates sent once.
   `SPEC.md` §4.3 keeps those and drops span-level trimming, which this measurement does not support.
2. **The budget can shrink where a backend charges for it.** Halving the window budget to 30 000 costs 0.019 line
   recall on these cases. Capping co-mention at 3 paragraphs cuts the pack by 13 % with the same gold lines.
   - That is a finder default, which the author holds (`NOW.md`, question 2(4)), so the measurement goes there and
     the default is unchanged.
3. **Recall is won in the route.**
   - Most anchored text sits in documents with no gold.
   - `bm25-lines` finds the most gold, `graph-evidence` the most per character.
   - `entity-unread` contributes nothing on these questions.
   The next measurements belong there: per-finder budgets by yield, the query the BM25 finder builds (one of
   four query builders, `SPEC.md` step 5), and novelgraph as a finder (step 6). Each is measured on an
   independent set before any of them is called an improvement (`SPEC.md` §6, G1–G2), because on this bench
   `graph-evidence`'s lead is partly the circularity.
