# Brief — chapter readings backfill from `kohaerenz-protokoll-charakter-bibel-2026-05-08-md`

The document was read and reconciled before chapter readings were part of every ingest (`Wiki/compare/reconcile-09-kohaerenz-protokoll-charakter-bibel-2026-05-08-md.md`). `python3 scripts/chapters.py missing kohaerenz-protokoll-charakter-bibel-2026-05-08-md` measured 17 chapters it names singly with no reading on the chapter's page. This batch writes those readings, nothing else.

**The document:** dated 2026-05-08; name it in prose „the character bible“. Read its head (first 30 lines) to say in one clause what it is.

**Stance — record, never apply.** A source is not canon (`Manuscript/kanon.md` decides canon): write „the character bible places … in Kap N“ / „sets for Kap N …“, and end each reading with „Recorded, not canon.“ If a line names the chapter only as a pointer with nothing about it, say so briefly („names Kap N only as …“). Ranges (Kap 1–13) are not readings of each chapter.

**Chapters and lines** (from `chapters.named`, single mentions only):
- Kap 1: L351, L1112
- Kap 2: L311, L1054
- Kap 6: L1054
- Kap 10: L202, L311, L1054
- Kap 12: L1054
- Kap 13: L349, L848, L1050, L1185
- Kap 14: L1054
- Kap 16: L1054
- Kap 22: L1114
- Kap 24: L1054
- Kap 25: L311, L1054
- Kap 27: L1115
- Kap 30: L1113
- Kap 33: L280, L844, L850
- Kap 34: L1054
- Kap 35: L1113
- Kap 39: L850

For chapters with many lines, select what the document says *about that chapter*; 2–8 quotations.

**Format:** one file per chapter, `Plan/runs/kapback-kohaerenz-protokoll-charakter-bibel-2026/readings/kap-NN--kohaerenz-protokoll-charakter-bibel-2026-05-08-md.md`, exactly as the files in `Plan/runs/kapback-welt-sensorik/readings/` (frontmatter `page`, `document`, `date: 2026-05-08`; heading `## Reading — \`kohaerenz-protokoll-charakter-bibel-2026-05-08-md\`, 2026-05-08, the character bible — <what it sets for this chapter>`; quotations „…“ ^[?] obtained with `read.py --find`).

**Hard rules:** no real person's name and no concept, strand or theory named after a person (write „the heat strand“, „the self-refuting-logic strand“, never the surname); no gendered pronoun for Kael, Juna, AEGIS or any alter in our own prose; never the author or „the user“; no trauma-symbol detail (Kissen, Gelb — only „Kernwunde“); world codes after mathematicians stay codes; quotations verbatim, cut before bold, italics, escaped asterisks and inner quotes; never quote a span containing a person's name.
