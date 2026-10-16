# Brief — chapter readings backfill from `2026-09-14-kap25-vertiefung-md`

The document was read and reconciled before chapter readings were part of every ingest (`Wiki/compare/reconcile-29-2026-09-14-kap25-vertiefung-md.md`). `python3 scripts/chapters.py missing 2026-09-14-kap25-vertiefung-md` measured 4 chapters it names singly with no reading on the chapter's page. This batch writes those readings, nothing else.

**The document:** dated 2026-09-14; name it in prose „the Kap 25 deepening“. Read its head (first 30 lines) to say in one clause what it is.

**Stance — record, never apply.** A source is not canon (`Manuscript/kanon.md` decides canon): write „the Kap 25 deepening places … in Kap N“ / „sets for Kap N …“, and end each reading with „Recorded, not canon.“ If a line names the chapter only as a pointer with nothing about it, say so briefly („names Kap N only as …“). Ranges (Kap 1–13) are not readings of each chapter.

**Chapters and lines** (from `chapters.named`, single mentions only):
- Kap 0: L17, L47
- Kap 27: L59
- Kap 28: L59
- Kap 30: L17

For chapters with many lines, select what the document says *about that chapter*; 2–8 quotations.

**Format:** one file per chapter, `Plan/runs/kapback-2026-09-14-kap25-vertiefung-md/readings/kap-NN--2026-09-14-kap25-vertiefung-md.md`, exactly as the files in `Plan/runs/kapback-welt-sensorik/readings/` (frontmatter `page`, `document`, `date: 2026-09-14`; heading `## Reading — \`2026-09-14-kap25-vertiefung-md\`, 2026-09-14, the Kap 25 deepening — <what it sets for this chapter>`; quotations „…“ ^[?] obtained with `read.py --find`).
**Hard rules:** no real person's name and no concept, strand or theory named after a person (write „the heat strand“, „the self-refuting-logic strand“, never the surname); no gendered pronoun for Kael, Juna, AEGIS or any alter in our own prose; never the author or „the user“; no trauma-symbol detail (Kissen, Gelb — only „Kernwunde“); world codes after mathematicians stay codes; quotations verbatim, cut before bold, italics, escaped asterisks and inner quotes; never quote a span containing a person's name.
