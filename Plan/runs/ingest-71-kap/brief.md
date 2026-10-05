# Brief — chapter readings from document 71

Document: `kohaerenz-protokoll-outline-revision-2026-05-01-md`, date `2026-04-30` (manifest), prose name „the outline revision of 2026-05-01“. A plan: write „the outline places / plans …“, never as what the novel is. Read `Plan/runs/ingest-71/brief.md`'s stance paragraph first; it holds here too.

One file per chapter: `Plan/runs/ingest-71-kap/readings/kap-NN--kohaerenz-protokoll-outline-revision-2026-05-01-md.md` (NN two digits), frontmatter `page: kap-NN`, `document:`, `date: 2026-04-30`, then one section:

```
## Reading — `kohaerenz-protokoll-outline-revision-2026-05-01-md`, 2026-04-30, the outline revision of 2026-05-01

Title: „<the chapter heading's title>“ ^[?Lnn]
Position: Akt <I/II/III>, POV <A/B> as the entry's POV line writes it ^[?Lnn]

- Story: one or two short quotations from `Was passiert` ^[?Lnn]
- Encoding: „Encoding A: …“ only if short; else omit
- <one more line only if the document says something about this chapter elsewhere: the seeding table (L137–L144), the POV table (L57–L95), foreshadowing (L354–L358), pacing (L366–L374), open points (L382–L384)>
```

Every quotation through `python3 scripts/read.py kohaerenz-protokoll-outline-revision-2026-05-01-md --find "…"`, written `^[?Lnn]`; a chapter entry is one long line, so quote short phrases from it. 3–5 quotations per chapter. Look at an existing `Wiki/chapters/kap-NN.md` reading only for format, never for content. The chapter's lines, from `chapters.py missing`:

Kap 1 L158–L160 (also L21, L302, L338, L342, L384) · Kap 2 L162–L164 (L21, L358) · Kap 3 L166–L168 (L302) · Kap 4 L170–L172 · Kap 5 L174–L176 · Kap 6 L178–L180 · Kap 7 L182–L184 (L144) · Kap 8 L186–L188 · Kap 9 L190–L192 · Kap 10 L194–L196 (L358) · Kap 11 L198–L200 (L22, L366) · Kap 12 L202–L204 · Kap 13 L206–L208 (L20, L126, L366) · Kap 14 L218–L220 · Kap 15 L222–L224 · Kap 16 L226–L228 · Kap 17 L230–L232 · Kap 18 L234–L236 (L370) · Kap 19 L238–L240 (L370) · Kap 20 L242–L244 · Kap 21 L246–L254 · Kap 22 L256–L258 · Kap 23 L260–L262 (L22) · Kap 24 L264–L266 · Kap 25 L268–L270 (L370, L382) · Kap 26 L272–L274 (L370) · Kap 27 L284–L286 (L22) · Kap 28 L288–L290 · Kap 29 L292–L294 · Kap 30 L296–L298 · Kap 31 L300–L302 · Kap 32 L304–L306 · Kap 33 L308–L314 (L22, L26, L383) · Kap 34 L316–L318 · Kap 35 L320–L322 · Kap 36 L324–L326 (L374, L382) · Kap 37 L328–L330 · Kap 38 L332–L334 · Kap 39 L336–L342 (L384)

Act lines: Akt I L154–L156, Akt II L214–L216, Akt III L280–L282.
