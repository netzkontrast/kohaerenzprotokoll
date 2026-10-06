# Brief — chapter readings from document 100

Document: `roman-entwicklung-kohaerenz-und-leitfragen`, date `2026-02-23` (manifest), prose name „the Leitfragen report“. A review of other documents: write „the Leitfragen report cites …“, „asks …“ — what it says of a chapter is its account of a source it numbers, never the chapter as planned by itself; keep its question marks. Read `Plan/runs/ingest-100/brief.md`'s stance paragraph first. The report names chapters only in its running prose („Kapitel 3“, „Kapitel 36-39“): every reading cites the line that names the chapter.

One file per chapter: `Plan/runs/ingest-100-kap/readings/kap-NN--roman-entwicklung-kohaerenz-und-leitfragen.md` (NN two digits), frontmatter `page: kap-NN`, `document: roman-entwicklung-kohaerenz-und-leitfragen`, `date: 2026-02-23`, then one section:

```
## Reading — `roman-entwicklung-kohaerenz-und-leitfragen`, 2026-02-23, the Leitfragen report — <what it says of the chapter, in a few words>

- the one or two short quotations from the line that names the chapter, and which Leitfrage it sits under ^[?Lnn]
```

The chapters and their lines:

- Kap 1 — L81: the Konstrukt-Stadt established by architectural storytelling.
- Kap 2 — L85: the fragment „Kapitel 2: Resonanz“, falling through the system noise.
- Kap 3 — L25 and L35: Kael, Elite-Cybersoldat of the Aegis Coalition, ordered to eliminate Nova Ardent, a Data-Runnerin.
- Kap 11, 12, 13 — L48: graph theory and IFS parts in Kapitel 11–13; Kap 11 also L83 (the transition between worlds).
- Kap 18 — L83: the transition between worlds.
- Kap 26, 27, 28, 29 — L107: Kairos, the Möglichkeits-Weber, in the Lyons-Welt.
- Kap 31 — L131: Kael synchronising abilities from different caches.
- Kap 36, 37, 38, 39 — L69: the finale, the living Gödel-Satz and the Parakonsistentes Gambit; Kap 37 also L73 (the collapse in the Lyons-Welt or the Potentialmeer); Kap 37 and 38 also L157 (the Gödel-Gambit); Kap 39 also L153 (Kishōtenketsu, 39 → 40/0).
- Kap 40 — L117 and L153: Kapitel 40/0, the Neon Ashes of New Zenith, the recursive reset.

Twenty-one files. Quote around glued footnote digits. Ask for the citation with `python3 scripts/read.py roman-entwicklung-kohaerenz-und-leitfragen --find "<the words>"`, never type it; before finishing, `python3 scripts/readings.py check ingest-100-kap` must be clean.
