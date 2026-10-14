# Brief — chapter readings backfill from `kohaerenz-protokoll-master-integration-md`

The document was read and reconciled before chapter readings were part of every ingest (`Wiki/compare/reconcile-158-kohaerenz-protokoll-master-integration-md.md`). `python3 scripts/chapters.py missing kohaerenz-protokoll-master-integration-md` measured 2 chapters it names singly with no reading on the chapter's page. This batch writes those readings, nothing else.

**The document:** dated 2026-03-26; name it in prose „the master integration“. Read its head (first 30 lines) to say in one clause what it is.

**Stance — record, never apply.** A source is not canon (`Manuscript/kanon.md` decides canon): write „the master integration places … in Kap N“ / „sets for Kap N …“, and end each reading with „Recorded, not canon.“ If a line names the chapter only as a pointer with nothing about it, say so briefly („names Kap N only as …“). Ranges (Kap 1–13) are not readings of each chapter.

**Chapters and lines** (from `chapters.named`, single mentions only):
- Kap 6: L316
- Kap 14: L316

For chapters with many lines, select what the document says *about that chapter*; 2–8 quotations.

**Format:** one file per chapter, `Plan/runs/kapback-kohaerenz-protokoll-master-integration-m/readings/kap-NN--kohaerenz-protokoll-master-integration-md.md`, exactly as the files in `Plan/runs/kapback-welt-sensorik/readings/` (frontmatter `page`, `document`, `date: 2026-03-26`; heading `## Reading — \`kohaerenz-protokoll-master-integration-md\`, 2026-03-26, the master integration — <what it sets for this chapter>`; quotations „…“ ^[?] obtained with `read.py --find`).
**Hard rules:** no real person's name and no concept, strand or theory named after a person (write „the heat strand“, „the self-refuting-logic strand“, never the surname); no gendered pronoun for Kael, Juna, AEGIS or any alter in our own prose; never the author or „the user“; no trauma-symbol detail (Kissen, Gelb — only „Kernwunde“); world codes after mathematicians stay codes; quotations verbatim, cut before bold, italics, escaped asterisks and inner quotes; never quote a span containing a person's name.
