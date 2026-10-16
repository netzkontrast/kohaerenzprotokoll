# Brief — chapter readings backfill from `kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md`

The document was read and reconciled before chapter readings were part of every ingest (`Wiki/compare/reconcile-18-kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md.md`). `python3 scripts/chapters.py missing kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md` measured 15 chapters it names singly with no reading on the chapter's page. This batch writes those readings, nothing else.

**The document:** dated 2026-06-10; name it in prose „the parts-profiles and speech-DNA manual“. Read its head (first 30 lines) to say in one clause what it is.

**Stance — record, never apply.** A source is not canon (`Manuscript/kanon.md` decides canon): write „the parts-profiles and speech-DNA manual places … in Kap N“ / „sets for Kap N …“, and end each reading with „Recorded, not canon.“ If a line names the chapter only as a pointer with nothing about it, say so briefly („names Kap N only as …“). Ranges (Kap 1–13) are not readings of each chapter.

**Chapters and lines** (from `chapters.named`, single mentions only):
- Kap 0: L125, L917, L1079
- Kap 1: L159, L729, L926, L992, L1063, L1081, L1129
- Kap 2: L105, L1063
- Kap 3: L703, L1042, L1063
- Kap 9: L929
- Kap 10: L105, L1063
- Kap 13: L157, L930, L1059
- Kap 14: L931
- Kap 25: L105, L1063
- Kap 31: L731, L1075
- Kap 32: L731, L788, L1075
- Kap 33: L788
- Kap 35: L149
- Kap 38: L1028
- Kap 39: L91, L934, L1129

For chapters with many lines, select what the document says *about that chapter*; 2–8 quotations.

**Format:** one file per chapter, `Plan/runs/kapback-kohaerenz-protokoll-anteile-profile-spra/readings/kap-NN--kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md.md`, exactly as the files in `Plan/runs/kapback-welt-sensorik/readings/` (frontmatter `page`, `document`, `date: 2026-06-10`; heading `## Reading — \`kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md\`, 2026-06-10, the parts-profiles and speech-DNA manual — <what it sets for this chapter>`; quotations „…“ ^[?] obtained with `read.py --find`).

**Hard rules:** no real person's name and no concept, strand or theory named after a person (write „the heat strand“, „the self-refuting-logic strand“, never the surname); no gendered pronoun for Kael, Juna, AEGIS or any alter in our own prose; never the author or „the user“; no trauma-symbol detail (Kissen, Gelb — only „Kernwunde“); world codes after mathematicians stay codes; quotations verbatim, cut before bold, italics, escaped asterisks and inner quotes; never quote a span containing a person's name.
