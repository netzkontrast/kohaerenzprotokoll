# Brief — chapter readings backfill from `kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md`

The document was read and reconciled before chapter readings were part of every ingest (`Wiki/compare/reconcile-14-kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md`). `python3 scripts/chapters.py missing kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md` measured 19 chapters it names singly with no reading on the chapter's page. This batch writes those readings, nothing else.

**The document:** dated 2026-06-10; name it in prose „the terms-and-concepts companion“. Read its head (first 30 lines) to say in one clause what it is.

**Stance — record, never apply.** A source is not canon (`Manuscript/kanon.md` decides canon): write „the terms-and-concepts companion places … in Kap N“ / „sets for Kap N …“, and end each reading with „Recorded, not canon.“ If a line names the chapter only as a pointer with nothing about it, say so briefly („names Kap N only as …“). Ranges (Kap 1–13) are not readings of each chapter.

**Chapters and lines** (from `chapters.named`, single mentions only):
- Kap 0: L91, L152, L533, L551, L569, L605, L622, L635, L638, L641, L654, L716, L812
- Kap 1: L394, L429, L625, L631, L635, L638
- Kap 3: L429
- Kap 9: L647
- Kap 10: L289
- Kap 13: L289
- Kap 15: L735
- Kap 17: L726
- Kap 18: L744
- Kap 24: L373
- Kap 31: L276
- Kap 32: L276, L277
- Kap 33: L277, L416
- Kap 35: L502, L595, L596, L597
- Kap 36: L598, L599
- Kap 37: L589, L605
- Kap 38: L370, L611
- Kap 39: L92, L149, L280, L283, L370, L373, L572, L612, L625, L647
- Kap 40: L551, L572, L622, L628, L812, L817

For chapters with many lines, select what the document says *about that chapter*; 2–8 quotations.

**Format:** one file per chapter, `Plan/runs/kapback-kohaerenz-protokoll-begriffe-und-konzept/readings/kap-NN--kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md`, exactly as the files in `Plan/runs/kapback-welt-sensorik/readings/` (frontmatter `page`, `document`, `date: 2026-06-10`; heading `## Reading — \`kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md\`, 2026-06-10, the terms-and-concepts companion — <what it sets for this chapter>`; quotations „…“ ^[?] obtained with `read.py --find`).
**Hard rules:** no real person's name and no concept, strand or theory named after a person (write „the heat strand“, „the self-refuting-logic strand“, never the surname); no gendered pronoun for Kael, Juna, AEGIS or any alter in our own prose; never the author or „the user“; no trauma-symbol detail (Kissen, Gelb — only „Kernwunde“); world codes after mathematicians stay codes; quotations verbatim, cut before bold, italics, escaped asterisks and inner quotes; never quote a span containing a person's name.
