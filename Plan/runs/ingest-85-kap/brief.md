# Brief — chapter readings from document 85

Document: `outline`, date `2025-07-30` (manifest), prose name „the outline“. A plan: write „the outline plans …“, never as what the novel is; keep its hedges (`möglicherweise`, `z.B.`, `oder`). Read `Plan/runs/ingest-85/brief.md`'s stance paragraph first.

One file per chapter: `Plan/runs/ingest-85-kap/readings/kap-NN--outline.md` (NN two digits), frontmatter `page: kap-NN`, `document: outline`, `date: 2025-07-30`, then one section:

```
## Reading — `outline`, 2025-07-30, the outline — <the chapter's title>

Title: „<title>“ ^[?Lnn] — Teil <1/3> ^[?Lnn]
Position: POV from `Erzählperspektive` ^[?Lnn]; journey stage from `Reisestufe` (Teil 3) ^[?Lnn]

- Story: the `Inhalt` (Teil 1) or `Plot` (Teil 3), one or two short quotations ^[?Lnn]
- Question: the `Thematische Kernfrage` where it has one ^[?Lnn]
```

Each chapter is a bold `Kapitel N` heading and its field lines up to the next heading; every quotation must cite a line inside that block — `read.py --find` may match the same words elsewhere (Kap 29 and Kap 31 share one sentence, L178 and L196: cite each chapter's own line). Teil 3's titles join alternatives with „/“: quote the title whole, decide nothing. `--find` drops digits glued to words (`KW1`, `Stufe 12`): quote around them. L174 is missing a word („in abweicht“): quote around it, do not repair. No uncited „…“ in a heading: use backticks. 3–5 quotations per chapter. Teil 2 (Kap 14–26) has no chapter list: write no file for those chapters.

Chapter headings: Teil 1 L17 · 1 L21 · 2 L27 · 3 L33 · 4 L39 · 5 L44 · 6 L49 · 7 L54 · 8 L59 · 9 L64 · 10 L69 · 11 L74 · 12 L79 · 13 L84 · Teil 3 L154 · 27 L158 · 28 L167 · 29 L176 · 30 L185 · 31 L194 · 32 L203 · 33 L212 · 34 L221 · 35 L230 · 36 L239 · 37 L248 · 38 L257 · 39 L266.

Ask for the citation with `python3 scripts/read.py outline --find "<the words>"`, never type it; before finishing, `python3 scripts/readings.py check ingest-85-kap` must be clean.
