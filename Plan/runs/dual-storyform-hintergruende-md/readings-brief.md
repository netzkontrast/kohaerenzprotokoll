# Brief — readings from dual-storyform-hintergruende-md

Document 30: `Sources/drive/dual-storyform-hintergruende-md.md`, dated 2026-05-08 by the manifest,
497 lines. **„Dual-Storyform — Hintergründe & konzeptuelle Genealogie"**: the companion to the
Dramatica status report of 2026-05-07 (`dramatica-dual-storyform-status-2026-05-07-md`, already
read). It explains *why* the novel has two storyforms: the thesis that forces them (§1), the
Klein-c-Inversion between them (§2), three audit corrections of 2026-05-07 — Approach, Driver, the IC
bearer in B (§3), per-chapter POV routing locked as „Hybrid Option 3" (§4), the Vortex's five beats
(§5), the reader as a substrate layer (§6), open research questions it restates from a „Reset-Doc
2026-04-30" (§7), a dated genealogy (§8), what fell away (§9) and a glossary of ten terms (L478–489).

Name it in prose as **„the Dual-Storyform background document"** (short: „the background document").

**Its standing, recorded, never applied** (decision 006): it ranks itself last — „Dieses Dokument \<
Status-PDF \< Reset-Doc 2026-04-30 \< Memory-Slots" (L29) — and says it supplies reasons, not values.
Where it restates other documents (the Reset-Doc's F8–F10 and Appendix C points, its §10, the
timeline in §8, „Memory Slot 5"), a reading says it is this document's claim about them. Where it
labels a position — „Alte Lesart (verworfen)", „Reset-Lesart", „Audit-Korrektur 2026-05-07",
„Lock-In 2026-05-07", „Empfehlung", „Reduziert auf", „Ersetzt durch" — the reading keeps the label.
Recommendations („Empfehlung: …") and research questions („F9 — …?") are open, not decided: a
question has no reading of its answer.

**Read first:** the note `Sources/notes/dual-storyform-hintergruende-md.md` (126 verified quotations
to start from) and `Plan/runs/dual-storyform-hintergruende-md/05-verify.txt`. Then read the document
whole: `python3 scripts/read.py dual-storyform-hintergruende-md`.

Rules already decided that apply here:
- **J98, J99** — a bare `K1`/`K0` with a plain digit is the Kohärenz-/Kollaps-Kernel in this
  document („AEGIS glaubt K1 (Kohärenz-Wächter) zu sein. Es ist tatsächlich K0 (Kollaps-Operator)",
  L82; „K1-Einheit"/„K0-Einheit" for Coheron and Erason, L480–481). Placed by the sentence.
- **J70** — a compound naming a bearer's role („Pivot Kael", „Kaels Innenwelt", „Juna-POV") is a
  reading on the bearer. **J86** — an arrow between two names („Kael↔Juna") states a relation.
- **J76–J78** — `Genesis-Flashbacks`, `Genesis-Krise`, `Genesis-Enthüllung` are not aliases of the
  Genesis; what the passage states about the Genesis is a reading on `genesis`.
- **J90** — the beat „5 Rotation" is the beat; its content is a reading on `truth-rotation`.
- **J93** — Erason-Op = Erason-Operator; „Oblivion = Erason-Operator" (L306) is a reading on `oblivion`.
- **J62/J53/J81** — a passage is placed by what it states; the Landauer-Hitze glossary line (L483)
  and „Heat-Spike (Landauer→∞)" (L359) go where the pages already keep heat (`landauer-signatur`,
  `hitze-polaritaetsregel`) by what they state.
- **J71** — `Moonshine`: „Moonshine-Boundary" (L426) and „Moonshine-Link" (L485) are the link;
  `Monstergruppe`/`Leech-Lattice`/`VOA` (L470) are the mathematics it drops.
- **J8/J9/J57** — „Kohärenz Protokoll" is the title; „Kohärenz-Wächter", „Erasure-Protokoll" are not
  `kohaerenz`.
- The Klein-c-Inversion has no page and gets none from this document: its own §9 says the Klein
  mapping „Hat im Roman keine Funktion — keine diegetische Erwähnung" (L471).

## Rules

1. **Never run any git command** (no stash, no checkout, no commit, no add). Other readers are editing
   other files in the same tree. Edit only the files you are given.
2. Add one section per page, placed after the page's last `## Reading — …` section of a document dated
   on or before 2026-05-08, **in date order** (the page's readings are in date order; the documents of
   2026-05-08 are several — put this one after them) and before `## Where the sources differ` /
   `## Open` / `## Occurrences only`:
   `## Reading — \`dual-storyform-hintergruende-md\`, 2026-05-08, the Dual-Storyform background document — <what it adds>`
   If the page is not in date order, put it after the last reading and say nothing about order.
3. English prose around German quotations. Every quotation verbatim in „…" followed by
   `^[dual-storyform-hintergruende-md.md:Lnn]` — the qualified form, always. **Every line number from**
   `python3 scripts/read.py dual-storyform-hintergruende-md --find "<exact words>"`; never type one.
   Table cells: quote a short span that is unique, and check it with `--find`. Never translate. Never
   merge two statements. No quotation for an absence: state it with a `grep -cw` count and append the
   command and its output as one line to `Plan/runs/dual-storyform-hintergruende-md/05-verify-readers.txt`
   (create if missing; prefix the line with your page name).
4. A reading says what **this** document says about the page's subject: definitions, where it places
   it (storyform, throughline, act, chapter, beat), what it retires, reduces or keeps open, and its
   status words. Short and precise: 3–12 quotations for a central page, 1–4 for a minor one.
5. Frontmatter: append `"dual-storyform-hintergruende-md"` to `ingested:`, add 1 to `sources:` and
   `readings:` (pages that carry `readings:`).
6. Keep the page true: if its lead or `## Where the sources differ` states a claim this document
   falsifies („only X", „every source", „no read source …", a count of sources), correct it and say
   which source moved it. Where the page has `## Where the sources differ`, add one line where this
   document takes a side or a new position, naming it „the Dual-Storyform background document".
   **Never resolve a difference.**
7. If, after reading, the document says nothing about a page's subject beyond an occurrence (a word in
   a list, a title), do **not** write a reading — report „not read: <why, with the line>".
8. Run `python3 scripts/quotes.py <file>` until 0 unresolved and 0 unchecked for your new quotations,
   and `python3 scripts/relations.py >/dev/null` (a `[[link]]` must point at an existing page; link
   a term at most once per page, only where the prose already names it).
9. Report per file: the heading, lines cited, any lead/differ claim changed and why, anything in the
   document that contradicts a page claim you did NOT change, and anything that looks like a new
   conflict (do not create records).

## Record rules (conflicts `Wiki/conflicts/`, questions `Wiki/questions/`)

Records are append-only. Append at the end:
`## 2026-09-27 — \`dual-storyform-hintergruende-md\`, 2026-05-08, the Dual-Storyform background document`
then a bold one-line summary of its position and the quotations, and one closing line saying which
row/side of the record it stands on, in the record's own terms. Add 1 to `sources:`, and append the
slug where the record keeps a list of documents in frontmatter. If the document does not speak to the
record, write nothing and report „not changed: <why, with a `grep -cw` count>".

## Chapter rules (`Wiki/chapters/kap-NN.md`)

A reading goes on a chapter page only where the document says something about **that chapter itself**
(what happens there, whose, which act, what it establishes) — a range boundary alone does not.
Format: `Wiki/chapters/README.md`, and the existing readings on the page. Place it among the readings
in date order (2026-05-08; after the other readings of that date), before `## Where the sources differ`.
Frontmatter: append to `ingested:`, add 1 to `sources:`. Never edit the four navigation sections
(What this chapter is about, Questions for this chapter, Candidate sources, Raw qmd answers).
Then `python3 scripts/chapters.py` (it may complain the document is not reconciled — ignore only that)
and `python3 scripts/quotes.py <page>`.
