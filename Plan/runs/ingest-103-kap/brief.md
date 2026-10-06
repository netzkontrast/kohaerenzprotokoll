# Brief — chapter readings from document 103

Document: `finales-kausales-plot-geruest`, date `2025-07-29` (manifest), prose name „the causal beat sheet“. A beat sheet: write „the beat sheet places …“, keep `könnte`, `möglicherweise`; Kael is male here. Read `Plan/runs/ingest-103/brief.md`'s stance paragraph first. Each beat names a range of chapters in its heading (`Beat 1.2: … (Kapitel 3-4)`); every chapter in the range gets the beat's reading, and says the beat spans the range.

One file per chapter, Kap 01 to Kap 39: `Plan/runs/ingest-103-kap/readings/kap-NN--finales-kausales-plot-geruest.md`, frontmatter `page: kap-NN`, `document: finales-kausales-plot-geruest`, `date: 2025-07-29`, then one section:

```
## Reading — `finales-kausales-plot-geruest`, 2025-07-29, the causal beat sheet — Beat N.M, <its title> (Kapitel a–b)

- Beat: the heading's title, quoted around its digits ^[?Lnn]
- Event: the `Beschreibung`, one or two short quotations ^[?Lnn]
- Cause: the `Kausale Verknüpfung`, one short quotation ^[?Lnn]
- Throughlines: one short quotation from the OS or MC line that names what changes ^[?Lnn]
```

The beats and their heading lines: 1.1 Kap 1–2 L24 · 1.2 Kap 3–4 L37 · 1.3 Kap 5–6 L50 · 1.4 Kap 7–9 L63 · 1.5 Kap 10–12 L76 · 1.6 Kap 13 L89 (Plot Point 1) · 2.1 Kap 14–17 L106 · 2.2 Kap 18–21 L119 · 2.3 Kap 22–24 L132 · 2.4 Kap 25–26 L145 (Midpoint) · 3.1 Kap 27–29 L162 · 3.2 Kap 30–32 L175 · 3.3 Kap 33–35 L188 · 3.4 Kap 36–37 L201 · 3.5 Kap 38–39 L214. Every quotation cites a line inside its beat. `read.py` drops digits glued to words: quote around them.

**Split into two readers, one after the other:** Reader A: Kap 01–19. Reader B: Kap 20–39.

Ask for the citation with `python3 scripts/read.py finales-kausales-plot-geruest --find "<the words>"`, never type it; before finishing, `python3 scripts/readings.py check ingest-103-kap` must be clean.
