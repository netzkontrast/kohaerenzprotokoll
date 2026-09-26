---
document: kp-kap25-2026-09-14-md
against: 106 pages, 15 conflicts
ran: "2026-09-26"
candidates: 162
decisions: 154
by_lookup: 100
judgements: 54
new_pages: 0
new_readings: 11
---

# Reconciliation 30 — `kp-kap25-2026-09-14-md` against the wiki

`python3 scripts/reconcile.py kp-kap25-2026-09-14-md`

166 candidates, 162 after four surface groups folded, 154 decisions — **100 by lookup, 54 to
judgement** — and no sweep hit. Document 29 is the chapter file the session log of the same run
(document 28) reports on: Kap 25, titled `Wegkreuzung`, a file created 2026-06-12 and revised in a
„Draft v0.2 (2026-09-14)" ^[kp-kap25-2026-09-14-md.md:L48]. **Research, not text for the novel**, by
the author's word for every narrative text. It has two voices: an apparatus (L11–48) — frontmatter,
summary, outline, a three-scene plan, continuity rules and a hidden note citing canon sections — and
prose (L52–296) in a first person that never names itself. `Kael` and `AEGIS` stand only in the
apparatus (`Plan/runs/kp-kap25-2026-09-14-md/05-verify.txt`).

## No new page

The apparatus is a template, and the prose names only things of one day in one chapter: an item
numbered 734-A-0244, a counter-register, a note surface, Stations 7, 11 and 12, Delta-Sieben, a stair
to the maintenance level, a handset, a bed module. Nothing is defined. The near matches were decided
by existing rules — J8 for `AEGIS-Personalisierung`, J9 for the work slug, J50 and J80 for the
numbered labels, J53 for the prose's „Knoten" and „Ebene", J62 for the handset and the silence — so no
judgement is new.

## Readings — 9 pages, two chapters, three conflicts

Written by three Claude readers in the container from one brief, each file reviewed, quote-checked and
committed on its own. Every reading says which voice it quotes, and none supplies a name the prose
does not write.

- **Figures and system:** `kael` (named only by the apparatus: „Kael / A‖B Bridge" ^[kp-kap25-2026-09-14-md.md:L19];
  the prose's „Ich tue nichts." ^[kp-kap25-2026-09-14-md.md:L145]), `aegis` (the system only in
  capital-letter lines — „EINHEIT 734: BEARBEITUNGSPROFIL ABWEICHEND. KEINE MASSNAHME." ^[kp-kap25-2026-09-14-md.md:L217]),
  `alters` („Hier sitzt mehr als einer." ^[kp-kap25-2026-09-14-md.md:L135], three unnamed parts, a line
  in a grammar the Ich disowns), `komponente-734` (a shift, a processing profile, a dwelling, an anchor —
  never the component; its lead narrowed to the sources that name both).
- **Places and signatures:** `kaels-wohneinheit` (the evening at home), `konstrukt-stadt` („in dieser
  Stadt" ^[kp-kap25-2026-09-14-md.md:L125], unnamed), `kern-welten` (KW3 only in the hidden note), `telefon-stille` („Die Stille kommt.
  Sie hat ihre Seite." ^[kp-kap25-2026-09-14-md.md:L277], a handset, no `Telefon`),
  `hitze-polaritaetsregel` (air „scharf und elektrisch" ^[kp-kap25-2026-09-14-md.md:L221] at the
  sign-off, no `Ozon`; warmth only in a register line).
- **Chapters:** Kap 25 (the chapter scene by scene, each line's voice named) and Kap 26 („Kap 26 trägt
  die Konsequenz; Kap 25 selbst bleibt still." ^[kp-kap25-2026-09-14-md.md:L46]).
- **Records:** C9, C11 and C14; every other record checked and not changed, each with its count
  (`Plan/runs/kp-kap25-2026-09-14-md/reconcile.json`). `plot.md` unchanged: the apparatus puts Kap 25 in
  Akt II, as every plan does.

## What moved

- **C11:** the cold side rendered without its word — sharp, electric air at the sign-off, „wie an den
  Tagen, an denen etwas bereinigt wird" ^[kp-kap25-2026-09-14-md.md:L221], cold hands, cool air below —
  and no warmth in any scene; `warm` stands once, in a line of the counter-register.
- **C9:** the prose says „in dieser Stadt" ^[kp-kap25-2026-09-14-md.md:L125] and names no city; the apparatus puts the stair in KW3.
  Identifying the city is the reading's; the author's decision stands.
- **C14:** no inner view and no logs for the system — capital-letter directives, and the Ich's „Es ist
  keine Warnung. Es ist eine Feststellung" ^[kp-kap25-2026-09-14-md.md:L219].
- **Kap 25's differences:** a title, and a thought the strukturierter Outline gives Kap 25 — that 734 is
  an address or a name — which this Kap 25 does not render.

## Tensions inside the document

Its apparatus plans three scenes and its prose has seven breaks, eight parts; the session log of the
same run says seven. Its hidden note places the stair in KW3; its prose says only „in dieser Stadt" ^[kp-kap25-2026-09-14-md.md:L125].

## Retrieval

Unchanged: PageRank recall@8 0.637, every case as after document 28.

## What the reading ran into

- **A file whose names are all in its apparatus.** The same shape as the annotated Kap-0 text and its
  prose: the grammar is the only label in the prose, and briefing v14's question held — no name went on
  the list that the prose does not write.
- **Renderings without words.** Ozone, the Telefon-Stille and Juna's evenings are each rendered and
  never named; each reading says the identification is its own, with the count.
- **Italic lines are a register, not the narrator.** „Fenster 03, Luft warm" ^[kp-kap25-2026-09-14-md.md:L69]
  is a line of the counter-register inside the item; the warmth is the register's.
