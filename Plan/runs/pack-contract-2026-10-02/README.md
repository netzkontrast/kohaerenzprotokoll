# The pack contract, step 4 of SPEC.md — fidelity and measurement, 2026-10-02

`fidelity.py` builds the `ask` pack of each of the 24 frozen cases (`Plan/eval/retrieval-cases-v1.json`, each case's
own record removed from the graph as `ask.py bench` does) and records the text's sha256, its size and which documents
and lines it sent. No model, no corpus reading.

| file | code | result |
|---|---|---|
| `before.json` | `main` at `e35009c0`, before step 4 | mean 48 690 bytes, max 69 175 |
| `after-a.json` | `build_pack` rewritten over `pack.hits` / `pack.fit`, rules unchanged (frontmatter kept, 60 000 characters of windows) | **24 of 24 packs byte-identical** to `before.json`, same documents and lines sent |
| `after-b.json` | the contract: 72 000 bytes over the whole pack, frontmatter anchors dropped, the omitted documents named | every pack within budget (max 71 404 bytes) |

`after-b.json` was recorded before the per-document share cap (`ask.DOC_SHARE`) existed. That run showed what the cap is
for: in C6 one block of very long lines (`digitale-uberwelt`, 44 238 bytes) fitted the larger byte budget, and the
pack went from 28 documents to 10. Document recall fell from 0.301 to 0.298. With the cap — no document over a quarter
of the window budget — the bench (`Plan/runs/ask/bench-2026-10-02-72000-66c21ef1.json`) reads **0.303 / 0.101**
against 0.301 / 0.100 before. No case is worse, and Q1 is better: 12 → 33 documents, because a giant block had
crowded it before too.

    .venv-graphqlite/bin/python Plan/runs/pack-contract-2026-10-02/fidelity.py <out.json>
