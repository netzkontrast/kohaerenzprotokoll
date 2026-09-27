# Brief — readings from worldbuilding-konzept-kohaerenzprotokoll-md

Document 26: `Sources/drive/worldbuilding-konzept-kohaerenzprotokoll-md.md`, dated 2026-05-08
by the manifest and in its own text („Stand: 8. Mai 2026 · Post-Reset-Kanon (2026-04-30) ·
inkl. Storyform-Korrekturen 2026-05-07", L17). A consolidated world bible that calls itself
„Steinbruch, nicht Korsett" (L21) and ranks itself below „Memory" and a „Reset-Doc" and „nicht
als Source-of-Truth" (L968) — **record that claim, never apply it** (decision 006: no date or
claim to be canon settles anything; the author decided C6 for five Guardians and C9 for the
Konstrukt-Stadt as KW1, and nothing here reverses that — a reading states what the document says).

**Read first:** the note `Sources/notes/worldbuilding-konzept-kohaerenzprotokoll-md.md` and the
counts `Plan/runs/worldbuilding-konzept-kohaerenzprotokoll-md/05-verify.txt`. Then read the whole
passages that concern your pages: `python3 scripts/read.py worldbuilding-konzept-kohaerenzprotokoll-md --from N --to M`.

## Rules

1. **Never run any git command** (no stash, no checkout, no commit). Other readers are editing
   other files in the same tree. Edit only the files you are given.
2. Add one section per page, placed after the page's last `## Reading — …` section and before a
   `## Where the sources differ` / `## Open` / `## Occurrences only` that follows it (where the
   page interleaves, after its latest-dated reading):
   `## Reading — \`worldbuilding-konzept-kohaerenzprotokoll-md\`, 2026-05-08, the worldbuilding concept — <what it adds>`
3. English prose around German quotations. Every quotation verbatim in „…" followed by
   `^[worldbuilding-konzept-kohaerenzprotokoll-md.md:Lnn]` — the qualified form, always. **Every
   line number from** `python3 scripts/read.py worldbuilding-konzept-kohaerenzprotokoll-md --find "<exact words>"`;
   never type one. Table cells: quote a short span, and check it with `--find`. Never translate.
   Never merge two statements. No quotation for an absence: state it with a `grep -cw` count and
   add the command and its output as a line to `Plan/runs/worldbuilding-konzept-kohaerenzprotokoll-md/05-verify-readers.txt`
   (append; create if missing; one line per count, prefixed with your page name).
4. A reading says what **this** document says about the page's subject: definitions, where it
   places it (world, act, chapter), what it retires or keeps open, and its status words
   („offen", „Lock-In steht aus", „kanonisch", „Vorgeschlagen"). Where the document relates older
   drafts („Die alten Drafts hatten …"), say it is the document's claim about them.
5. Frontmatter: append `"worldbuilding-konzept-kohaerenzprotokoll-md"` to `ingested:`, add 1 to
   `sources:` and `readings:` (pages); for records see the record rules below.
6. Keep the page true: if its lead or `## Where the sources differ` states a claim this document
   falsifies („only X", „every source", „no read source …"), correct it and say which source moved
   it. Where the page has `## Where the sources differ`, add one line where this document takes a
   side or a new position, naming it „the worldbuilding concept". **Never resolve a difference.**
7. **A page that already reads this document** (the 2026-09-25 scan wrote readings from it on
   `ouroboros-struktur`, `vortex`, `tsdp`, `chaitin-konstante`, `goedel-gambit`, `komponente-734`):
   do not add a second section. Check every quotation and claim in the existing reading against
   the full document, fix what is wrong, add what the full document says that the reading misses,
   and make its closing line say it was checked against the full document and that the document
   now has a census (`Sources/terms/…`) and a reconciliation (reconcile-27). Frontmatter unchanged
   except `ingested:` if the slug is missing.
8. Run `python3 scripts/quotes.py <file>` until 0 unresolved and 0 unchecked, and
   `python3 scripts/relations.py >/dev/null` (a `[[link]]` must point at an existing page).
9. Report per file: the heading, lines cited, any lead/differ claim changed and why, anything in
   the document that contradicts a page claim you did NOT change, and anything that looks like a
   new conflict (do not create records).

## Record rules (conflicts `Wiki/conflicts/`, questions `Wiki/questions/`)

Records are append-only, in date order of the entries' writing. Append at the end:
`## 2026-09-26 — \`worldbuilding-konzept-kohaerenzprotokoll-md\`, 2026-05-08, the worldbuilding concept`
then a bold one-line summary of its position and the quotations, and one closing line saying
which row/side of the record it stands on, in the record's own terms. Add 1 to `sources:`. If the
document does not speak to the record, write nothing and report „not changed: <why, with a count>".

## Chapter rules (`Wiki/chapters/kap-NN.md`)

A reading goes on a chapter page only where the document says something about **that chapter
itself** (what happens there, where, whose view, which beat) — a range like „Ch1–13" alone does
not, a named chapter with content does. Format: `Wiki/chapters/README.md`, and the existing
readings on the page. Place it among the readings in date order (2026-05-08; after other
2026-05-08 readings), before `## Where the sources differ`. Frontmatter: append to `ingested:`,
add 1 to `sources:`. The chapter pages also carry four navigation sections written by a script
(What this chapter is about, Questions, Candidate sources, Raw qmd answers) — never edit those.
Then `python3 scripts/chapters.py` (it will complain the document is not reconciled — ignore
only that complaint) and `python3 scripts/quotes.py <page>`.
