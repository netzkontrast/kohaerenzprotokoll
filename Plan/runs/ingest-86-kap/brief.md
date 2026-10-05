# Brief — chapter readings from document 86

Document: `kohaerenz-protokoll-kapitel-outline-generierung-2`, date `2026-04-30` (manifest), prose name „the dual-storyform outline“. A plan: write „the dual-storyform outline plans …“, never as what the novel is. Read `Plan/runs/ingest-86/brief.md`'s stance paragraph first.

One file per chapter: `Plan/runs/ingest-86-kap/readings/kap-NN--kohaerenz-protokoll-kapitel-outline-generierung-2.md` (NN two digits), frontmatter `page: kap-NN`, `document: kohaerenz-protokoll-kapitel-outline-generierung-2`, `date: 2026-04-30`, then one section:

```
## Reading — `kohaerenz-protokoll-kapitel-outline-generierung-2`, 2026-04-30, the dual-storyform outline — <the chapter's title>

Title: „<title>“ ^[?Lnn] — Akt <I/II/III> ^[?Lnn]; `Pivot-Kapitel` where marked ^[?Lnn]

- Story: the summary paragraph, one or two short quotations ^[?Lnn]
- Storyforms: the `Storyform B` and `Storyform A` lines, each with its position in backticks (`MC: Universe/Past`) and a short quotation ^[?Lnn]
- Scene and pacing: the `Szenen-Keim` and the `Pacing` label ^[?Lnn]
```

Each chapter is a `### **Kapitel N: …**` heading and the lines up to the next heading; every quotation must cite a line inside that block — `read.py --find` may match the same words elsewhere. Footnote digits glued to sentence ends (`…Bewusstsein“.8`) are not part of the text: quote around them; `--find` drops digits glued to words (`Sektor 0`). Kap 37 and 39 carry only A lines and Kap 38 two A lines: record what is there, never supply the missing one. No uncited „…“ in a heading: use backticks. 4–6 quotations per chapter.

Chapter headings: Akt I L59 · 1 L63 · 2 L72 · 3 L81 · 4 L89 · 5 L97 · 6 L105 · 7 L113 · 8 L122 · 9 L130 · 10 L138 · 11 L146 · 12 L154 · 13 L162 · Akt II L171 · 14 L175 · 15 L183 · 16 L191 · 17 L199 · 18 L207 · 19 L215 · 20 L223 · 21 L232 · 22 L240 · 23 L248 · 24 L256 · 25 L264 · 26 L272 · Akt III L281 · 27 L285 · 28 L293 · 29 L301 · 30 L309 · 31 L317 · 32 L325 · 33 L333 · 34 L341 · 35 L349 · 36 L357 · 37 L365 · 38 L373 · 39 L381 (to L388).

Ask for the citation with `python3 scripts/read.py kohaerenz-protokoll-kapitel-outline-generierung-2 --find "<the words>"`, never type it; before finishing, `python3 scripts/readings.py check ingest-86-kap` must be clean.
