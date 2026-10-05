# Brief — chapter readings from document 84

Document: `ai-assisted-narrative-coherence`, date `2025-10-15` (manifest), prose name „the scene outline“ of „the English compilation“. Only its scene outline (L1273–L1669) places events in chapters; it is a plan: write „the scene outline plans …“, never as what the novel is. Read `Plan/runs/ingest-84/brief.md`'s stance paragraph first. Quote the English as written.

One file per chapter: `Plan/runs/ingest-84-kap/readings/kap-NN--ai-assisted-narrative-coherence.md` (NN two digits), frontmatter `page: kap-NN`, `document: ai-assisted-narrative-coherence`, `date: 2025-10-15`, then one section:

```
## Reading — `ai-assisted-narrative-coherence`, 2025-10-15, the scene outline of the English compilation — <the chapter's title>

Title: „<title>“ ^[?Lnn] — Act <I/II/III> ^[?Lnn]
Position: POV and place from the scene's fields where it has them ^[?Lnn]

- Story: the scene's goal, conflict or beats, one or two short quotations ^[?Lnn]
- Turn: the scene's `Outcome & Turn` where it has one ^[?Lnn]
```

Chapters given as a range (Chapters 4-5, 6-7, 9-10, 11-13; Act III's sequences 27-30, 31-33, 34-36, 37-38) are one entry: write the same reading on each chapter of the range and say in the heading „one entry shared with Kap NN–NN“. Every quotation must cite a line inside that chapter's block — `read.py --find` may match the same words elsewhere (the blueprint and the summary at L1801 repeat words). No uncited „…“ in a heading: use backticks. Kap 1–3 are not named by number (scenes 1.1–1.3 sit under Act I, Chapters 1-13, L1279): write no file for them. 3–5 quotations per chapter.

Chapter blocks: Act I L1279 · 4–5 L1335 · 6–7 L1352 · 8 L1369 · 9–10 L1386 · 11–13 L1404 · Act II L1424 · 14 L1430 · 15 L1451 · 16 L1471 · 17 L1489 · 18 L1506 · 19 L1509 · 20 L1526 · 21 L1529 · 22 L1532 · 23 L1535 · 24 L1553 · 25 L1556 · 26 L1572 · Act III L1578 · 27–30 L1584 · 31–33 L1602 · 34–36 L1620 · 37–38 L1636 · 39 L1653 (to about L1669).

Ask for the citation with `python3 scripts/read.py ai-assisted-narrative-coherence --find "<the words>"`, never type it; before finishing, `python3 scripts/readings.py check ingest-84-kap` must be clean.
