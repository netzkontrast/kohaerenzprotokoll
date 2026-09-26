# Brief — readings from kp-kap25-2026-09-14-md

Document 29: `Sources/drive/kp-kap25-2026-09-14-md.md`, dated 2026-09-14 by the manifest. **A chapter file of Kap 25
„Wegkreuzung"**, and **research, not text for the novel** — the author's word for every narrative text
(„Those arent Texts for the novel - only Research"). It has two voices, and a reading names which it quotes:

- **the apparatus** (L11–48): the file's own escaped frontmatter (`created: "2026-06-12"`, `status:
  "revised"`, `pov: "Kael / A‖B Bridge (\~25 %)"`), a summary, an outline (Akt, Storyform,
  Kapitelauftrag), a three-scene plan, continuity rules, and a hidden HTML comment „Draft v0.2
  (2026-09-14)" (L48) citing canon sections and decisions — its claims about other documents,
  recorded, never applied (decision 006);
- **the prose** (L52–296), a first person the prose never names. `Kael` and `AEGIS` stand only in the
  apparatus (`05-verify.txt`). **Never supply a name the prose does not write**: a reading says what the
  text renders and in which register — the Ich, a line in italics with no speaker (L119), three unnamed
  „Einer" (L137), the system's capital-letter lines (L56, L211, L217) — and, where the apparatus names
  the speaker, says that it is the apparatus that names him. Where the prose renders something without
  its word (air „scharf und elektrisch" and no `Ozon`; „Die Stille kommt" with a handset and no
  `Telefon`; „die vier Abende" and no `Juna`), say so with the `grep -cw` count from `05-verify.txt`,
  and say that the identification is the reading's, not the text's.

The session log of the same run (document 28, `2026-09-14-kap25-vertiefung-md`, already reconciled) reports
what this revision changed. You may name it in one clause where your page already carries its reading
(„as the session log reports"), but **quote only this document**.

Italic lines at L64–69 are lines of the counter-register the item contains, not the narrator's
observations: „Fenster 03, Luft warm" is the register's warmth.

Rules already decided that apply here: J50 (Wohneinheit 734 is `kaels-wohneinheit`), J80 (a bare
numbered label like `EINHEIT 734` is decided by its passage; do not merge), J53 (a shared head is not a
shared referent: the prose's „Knoten" and „Ebene" are not `datenverarbeitungsknoten-7g` or
`realitaetsebenen`), J62 (a passage is placed by what it states), J9 (the `work_slug` title is not the term).

**Read first:** the note `Sources/notes/kp-kap25-2026-09-14-md.md` and `Plan/runs/kp-kap25-2026-09-14-md/05-verify.txt`. Then read the document
whole — it is 296 lines: `python3 scripts/read.py kp-kap25-2026-09-14-md`.

## Rules

1. **Never run any git command** (no stash, no checkout, no commit). Other readers are editing
   other files in the same tree. Edit only the files you are given.
2. Add one section per page, placed after the page's last `## Reading — …` section and before a
   `## Where the sources differ` / `## Open` / `## Occurrences only` that follows it (where the
   page interleaves, after its latest-dated reading):
   `## Reading — \`kp-kap25-2026-09-14-md\`, 2026-09-14, the Kap-25 chapter file — <what it adds>`
3. English prose around German quotations. Every quotation verbatim in „…" followed by
   `^[kp-kap25-2026-09-14-md.md:Lnn]` — the qualified form, always. **Every
   line number from** `python3 scripts/read.py kp-kap25-2026-09-14-md --find "<exact words>"`;
   never type one. Table cells: quote a short span, and check it with `--find`. Never translate.
   Never merge two statements. No quotation for an absence: state it with a `grep -cw` count and
   add the command and its output as a line to `Plan/runs/kp-kap25-2026-09-14-md/05-verify-readers.txt`
   (append; create if missing; one line per count, prefixed with your page name).
4. A reading says what **this** document says about the page's subject: definitions, where it
   places it (world, act, chapter), what it retires or keeps open, and its status words
   (the apparatus's `status: "revised"`, „Draft v0.2", „muss", „ausdrücklich"). Where the apparatus cites other documents („Canon-Kernwelten §12", „Canon §0"), say it is its claim about them.
5. Frontmatter: append `"kp-kap25-2026-09-14-md"` to `ingested:`, add 1 to
   `sources:` and `readings:` (pages); for records see the record rules below.
6. Keep the page true: if its lead or `## Where the sources differ` states a claim this document
   falsifies („only X", „every source", „no read source …"), correct it and say which source moved
   it. Where the page has `## Where the sources differ`, add one line where this document takes a
   side or a new position, naming it „the Kap-25 chapter file". **Never resolve a difference.**
7. No page reads this document yet; the 2026-09-25 scan did not touch it.
8. Run `python3 scripts/quotes.py <file>` until 0 unresolved and 0 unchecked, and
   `python3 scripts/relations.py >/dev/null` (a `[[link]]` must point at an existing page).
9. Report per file: the heading, lines cited, any lead/differ claim changed and why, anything in
   the document that contradicts a page claim you did NOT change, and anything that looks like a
   new conflict (do not create records).

## Record rules (conflicts `Wiki/conflicts/`, questions `Wiki/questions/`)

Records are append-only, in date order of the entries' writing. Append at the end:
`## 2026-09-26 — \`kp-kap25-2026-09-14-md\`, 2026-09-14, the Kap-25 chapter file`
then a bold one-line summary of its position and the quotations, and one closing line saying
which row/side of the record it stands on, in the record's own terms. Add 1 to `sources:`. If the
document does not speak to the record, write nothing and report „not changed: <why, with a count>".

## Chapter rules (`Wiki/chapters/kap-NN.md`)

A reading goes on a chapter page only where the document says something about **that chapter
itself** (what happens there, whose, what it hooks into) — a word count alone does not, a named chapter with content does. Format: `Wiki/chapters/README.md`, and the existing
readings on the page. Place it among the readings in date order (2026-09-14; it is the newest document read, so it is last), before `## Where the sources differ`. Frontmatter: append to `ingested:`,
add 1 to `sources:`. The chapter pages also carry four navigation sections written by a script
(What this chapter is about, Questions, Candidate sources, Raw qmd answers) — never edit those.
Then `python3 scripts/chapters.py` (it will complain the document is not reconciled — ignore
only that complaint) and `python3 scripts/quotes.py <page>`.
