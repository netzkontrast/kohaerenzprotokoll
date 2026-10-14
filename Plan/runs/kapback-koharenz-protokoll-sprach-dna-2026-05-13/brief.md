# Brief — chapter readings backfill from `koharenz-protokoll-sprach-dna-2026-05-13-md`

The document was read and reconciled before chapter readings were part of every ingest (`Wiki/compare/reconcile-20-koharenz-protokoll-sprach-dna-2026-05-13-md.md`). `python3 scripts/chapters.py missing koharenz-protokoll-sprach-dna-2026-05-13-md` measured 7 chapters it names singly with no reading on the chapter's page. This batch writes those readings, nothing else.

**The document:** dated 2026-05-13; name it in prose „the speech-DNA manual of 2026-05-13“. Read its head (first 30 lines) to say in one clause what it is.

**Stance — record, never apply.** A source is not canon (`Manuscript/kanon.md` decides canon): write „the speech-DNA manual of 2026-05-13 places … in Kap N“ / „sets for Kap N …“, and end each reading with „Recorded, not canon.“ If a line names the chapter only as a pointer with nothing about it, say so briefly („names Kap N only as …“). Ranges (Kap 1–13) are not readings of each chapter.

**Chapters and lines** (from `chapters.named`, single mentions only):
- Kap 0: L27, L205
- Kap 9: L171
- Kap 13: L69, L241
- Kap 37: L197
- Kap 38: L61
- Kap 39: L173
- Kap 40: L27, L29, L205

For chapters with many lines, select what the document says *about that chapter*; 2–8 quotations.

**Format:** one file per chapter, `Plan/runs/kapback-koharenz-protokoll-sprach-dna-2026-05-13/readings/kap-NN--koharenz-protokoll-sprach-dna-2026-05-13-md.md`, exactly as the files in `Plan/runs/kapback-welt-sensorik/readings/` (frontmatter `page`, `document`, `date: 2026-05-13`; heading `## Reading — \`koharenz-protokoll-sprach-dna-2026-05-13-md\`, 2026-05-13, the speech-DNA manual of 2026-05-13 — <what it sets for this chapter>`; quotations „…“ ^[?] obtained with `read.py --find`).
**Hard rules:** no real person's name and no concept, strand or theory named after a person (write „the heat strand“, „the self-refuting-logic strand“, never the surname); no gendered pronoun for Kael, Juna, AEGIS or any alter in our own prose; never the author or „the user“; no trauma-symbol detail (Kissen, Gelb — only „Kernwunde“); world codes after mathematicians stay codes; quotations verbatim, cut before bold, italics, escaped asterisks and inner quotes; never quote a span containing a person's name.
