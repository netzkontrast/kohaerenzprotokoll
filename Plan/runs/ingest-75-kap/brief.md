# Brief — chapter readings from document 75

Document: `romanstruktur-und-philosophische-einleitung`, date `2025-12-18` (manifest), prose name „the three-part analysis“. It retells every chapter in the present tense as if the novel existed: write „the three-part analysis tells …“, never as what the novel is; keep its hedges (`vermutlich`, `vielleicht`). Read `Plan/runs/ingest-75/brief.md`'s stance paragraph first.

One file per chapter: `Plan/runs/ingest-75-kap/readings/kap-NN--romanstruktur-und-philosophische-einleitung.md` (NN two digits), frontmatter `page: kap-NN`, `document:`, `date: 2025-12-18`, then one section:

```
## Reading — `romanstruktur-und-philosophische-einleitung`, 2025-12-18, the three-part analysis — <the chapter's title in a few words>

Title: „<the chapter heading's title, without the parenthesis>“ ^[?Lnn]
Position: Teil <I/II/III>, <its archetype stage, the heading's parenthesis> ^[?Lnn]

- Story: one or two short quotations from the chapter's paragraphs ^[?Lnn]
- <one more line only if the document speaks of this chapter elsewhere: Tabelle 1 (L119–L130), or a back-reference in a later chapter>
```

Every quotation through `python3 scripts/read.py romanstruktur-und-philosophische-einleitung --find "…"`, written `^[?Lnn]`; 2–4 quotations per chapter. Look at an existing `Wiki/chapters/kap-NN.md` reading only for format. Headings (prose in the lines after each):

Kap 1 L37 · 2 L45 · 3 L51 · 4 L59 · 5 L65 (Tabelle L125) · 6 L71 · 7 L77 · 8 L83 (L129) · 9 L89 · 10 L95 · 11 L101 (L125) · 12 L107 (L130) · 13 L113 · Teil II L132 · 14 L142 · 15 L148 · 16 L154 · 17 L160 · 18 L166 · 19 L172 · 20 L178 · 21 L184 · 22 L190 · 23 L196 · 24 L200 · 25 L206 · 26 L212 · Teil III L218 · 27 L228 · 28 L232 · 29 L236 · 30 L240 · 31 L244 · 32 L248 · 33 L252 · 34 L258 · 35 L262 · 36 L266 · 37 L270 · 38 L274 · 39 L278 (L294).

**Kap 0 and Kap 40** both take `Kapitel 40/0` (L284–L310): „epilogue and prologue at once“ (L288), the Genesis reprise, the Trennungsprotokoll as necessity (L296), Kael waking in KW1 (L306). One reading on each page, the same content, each saying the document makes them one chapter. The introduction names it at L17 and L25.
