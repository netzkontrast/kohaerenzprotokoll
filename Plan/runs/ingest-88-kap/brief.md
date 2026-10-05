# Brief — chapter readings from document 88

Document: `kontext-outline`, date `2025-05-03` (manifest), prose name „the outline commission“. A commission: write „the commission plans …“, never as what the novel is; keep its question marks and hedges (`?`, `latent?`, `ggf.`). Read `Plan/runs/ingest-88/brief.md`'s stance paragraph first. `chapters.py missing` does not see these chapters (English „Chapter N“): that is why this brief exists.

One file per chapter: `Plan/runs/ingest-88-kap/readings/kap-NN--kontext-outline.md` (NN two digits), frontmatter `page: kap-NN`, `document: kontext-outline`, `date: 2025-05-03`, then one section:

```
## Reading — `kontext-outline`, 2025-05-03, the outline commission — <the chapter's bracketed title>

Title: the bracketed title ^[?Lnn] — Act <1/2/3> ^[?Lnn]
Position: `Setting` ^[?Lnn]

- Theme: the `Core Theme`, one short quotation ^[?Lnn]
- Story: the `Plot Summary`, one or two short quotations ^[?Lnn]
- Foci: `Kael Sys Focus` and `AEGIS Focus`, one short quotation each ^[?Lnn]
- Notes: a `+ Subplot Focus`, `+ Philo Hint` or `+ Trope Note` line where it adds a name ^[?Lnn]
```

Each chapter is a `### **Chapter N: \[…\]**` heading and the field lines up to the next heading; every quotation must cite a line inside that block. `read.py` drops digits glued to words (`KW1`, `Chapter 13`): quote around them, and give the chapter by the bracketed title's words, not its number. A heading carrying its own inner „…“ cannot be quoted whole: quote the inner part. No uncited „…“ in a heading: use backticks. 3–5 quotations per chapter. The Prologue (L63) has no chapter page: write no file for it.

Chapter headings: Act 1 L74 · 1 L76 · 2 L87 · 3 L98 · 4 L109 · 5 L120 · 6 L131 · 7 L142 · 8 L153 · 9 L164 · 10 L175 · 11 L186 · 12 L198 · 13 L209 · Act 2 L221 · 14 L223 · 15 L234 · 16 L245 · 17 L256 · 18 L267 · 19 L279 · 20 L290 · 21 L302 · 22 L313 · 23 L324 · 24 L335 · 25 L346 · 26 L357 · Act 3 L368 · 27 L370 · 28 L380 · 29 L391 · 30 L402 · 31 L413 · 32 L423 · 33 L434 · 34 L445 · 35 L457 · 36 L468 · 37 L477 · 38 L489 · 39 L497 (to L504).

Ask for the citation with `python3 scripts/read.py kontext-outline --find "<the words>"`, never type it; before finishing, `python3 scripts/readings.py check ingest-88-kap` must be clean.
