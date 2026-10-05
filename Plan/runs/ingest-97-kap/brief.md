# Brief — chapter readings from document 97

Document: `2-kohaerenz-protokoll-konzeptentwicklung`, date `2025-05-03` (manifest), prose name „the concept development“. A plan: write „the concept development plans …“, never as what the novel is; keep its hedges and question marks (`möglicherweise`, `könnte`, `Kiko?`). It writes Kael female (`ihre`, `sie`): quote it as written, never correct it (C17). Read `Plan/runs/ingest-97/brief.md`'s stance paragraph first. `chapters.py missing` does not see these chapters (English „Chapter N“): that is why this brief exists. `Chapter P: [Genesis]` is Kap 0.

One file per chapter: `Plan/runs/ingest-97-kap/readings/kap-NN--2-kohaerenz-protokoll-konzeptentwicklung.md` (NN two digits, 00–39), frontmatter `page: kap-NN`, `document: 2-kohaerenz-protokoll-konzeptentwicklung`, `date: 2025-05-03`, then one section:

```
## Reading — `2-kohaerenz-protokoll-konzeptentwicklung`, 2025-05-03, the concept development — <the chapter's bracketed title, or its focus label when it has none>

Focus: the `Central Conceptual Focus` label and one short quotation ^[?Lnn]

- Story: the `Narrative & Reader Psychology Strategy`, one or two short quotations — where it is, who acts, which KW and Guardian ^[?Lnn]
- Concept: the `Research & Concept Application`, one short quotation naming its TSDP step or paradox ^[?Lnn]
- Act: only where the block says it (`Ende von Akt 1` in Chapter 13, `Ende von Akt 2` in Chapter 26, `Beginn von Akt 3` in Chapter 27) ^[?Lnn]
```

Each chapter is a `### **Chapter N:**` heading and its four field lines up to the next heading; every quotation must cite a line inside that block. Skip the `Recherche-Keywords` line unless it carries a name nothing else in the block does. `read.py` drops digits glued to words (`KW1`, `Chapter 13`): quote around them. A heading carrying its own inner „…“ cannot be quoted whole: quote the inner part. No uncited quotation, no count.

Chapter headings: P (Kap 0) L44 · 1 L51 · 2 L58 · 3 L65 · 4 L72 · 5 L79 · 6 L86 · 7 L93 · 8 L100 · 9 L107 · 10 L114 · 11 L121 · 12 L128 · 13 L135 · 14 L142 · 15 L149 · 16 L156 · 17 L163 · 18 L170 · 19 L177 · 20 L184 · 21 L191 · 22 L198 · 23 L205 · 24 L212 · 25 L219 · 26 L226 · 27 L233 · 28 L240 · 29 L247 · 30 L254 · 31 L261 · 32 L268 · 33 L275 · 34 L282 · 35 L289 · 36 L296 · 37 L303 · 38 L310 · 39 L317

**Split into two readers, one after the other:** Reader A: Kap 00–19. Reader B: Kap 20–39.

Ask for the citation with `python3 scripts/read.py 2-kohaerenz-protokoll-konzeptentwicklung --find "<the words>"`, never type it; before finishing, `python3 scripts/readings.py check ingest-97-kap` must be clean.
