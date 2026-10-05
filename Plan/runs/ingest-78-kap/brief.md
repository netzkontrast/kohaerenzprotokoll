# Brief — chapter readings from document 78

Document: `kohaerenz-protokoll-kapitel-outline-erstellung`, date `2026-04-30` (manifest), prose name „the dual-storyform outline“. A generated plan: write „the outline plans …“, never as what the novel is. Read `Plan/runs/ingest-78/brief.md`'s stance paragraph first.

One file per chapter: `Plan/runs/ingest-78-kap/readings/kap-NN--kohaerenz-protokoll-kapitel-outline-erstellung.md` (NN two digits), frontmatter `page: kap-NN`, `document:`, `date: 2026-04-30`, then one section:

```
## Reading — `kohaerenz-protokoll-kapitel-outline-erstellung`, 2026-04-30, the dual-storyform outline — <the chapter's title>

Title: „<the heading's title>“ ^[?Lnn]
Position: Akt <I/II/III>, POV as the chapter's POV field gives it ^[?Lnn]

- Story: one or two short quotations from `Was passiert` ^[?Lnn]
- Concepts: the `Eingeführte Konzepte` field, briefly ^[?Lnn]
- <Pivot-Marker, only if the chapter carries one: one line>
```

Every quotation through `python3 scripts/read.py kohaerenz-protokoll-kapitel-outline-erstellung --find "…"` — the title words may also stand in the blurb (L13–L17) or the appendices: check the line falls inside the chapter's block. Quote plain spans: cut before inner „…“, emphasis asterisks or a glued reference digit. 3–5 quotations per chapter. Look at an existing `Wiki/chapters/kap-NN.md` reading only for format.

Chapter blocks (heading line; the block runs to the next heading): 1 L23 · 2 L53 · 3 L81 · 4 L109 · 5 L137 · 6 L165 · 7 L193 · 8 L227 · 9 L255 · 10 L283 · 11 L311 · 12 L339 · 13 L367 · Akt II L401 · 14 L405 · 15 L439 · 16 L467 · 17 L495 · 18 L523 · 19 L551 · 20 L579 · 21 L613 · 22 L641 · 23 L669 · 24 L697 · 25 L725 · 26 L753 · Akt III L787 · 27 L791 · 28 L824 · 29 L852 · 30 L880 · 31 L908 · 32 L936 · 33 L970 · 34 L1003 · 35 L1035 · 36 L1074 · 37 L1114 · 38 L1142 · 39 L1170 (Anhänge from L1202).
