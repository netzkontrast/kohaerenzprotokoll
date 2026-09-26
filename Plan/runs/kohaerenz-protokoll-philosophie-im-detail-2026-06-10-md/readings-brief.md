# Brief — readings from kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md

Document 27: `Sources/drive/kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md.md`, dated 2026-06-10 by the manifest and in its own
text („Stand: 2026-06-10", L2). A catalogue of the philosophical schools under the novel, school
by school — Kern, Funktion im Roman, Drafting-Disziplin, Wo im Roman — mapped onto figures,
Kernwelten and chapters (the tables of §14, L614–739, flattened by the export into one cell per
line), with an Anti-Kanon (§13), drafting prohibitions (§16) and open questions (§17). It calls
itself „Fünftes Dokument im Repo-Quartett-plus-eins" and „Werkbank, nicht Schaufenster" (L2) and
labels **sections, not passages**, `[K]` kanonisch · `[V]` Vorschlag · `[S]` Steinbruch-gefiltert ·
`[L]` Lücke — so a reading names the label of the section it quotes from. Its `[K]` is its claim
— **record it, never apply it** (decision 006: no date or claim to be canon settles anything; the
author decided C6 for five Guardians and C9 for the Konstrukt-Stadt as KW1, and nothing here
reverses that — a reading states what the document says).

Most of it is lens: a philosopher is not a term of the world. A reading on a page quotes what the
document says **about the page's subject** (a figure, a world, a chapter, a mechanism), and may
name the school it maps it to. It places some things twice and does not flag it — the ANP/EP
barriers dissolve „in Kap 35 (Vortex 1)" (L210) and „in Vortex 1 Beat 2" (L581); the Gödel-Gambit
begins in Kap 30 (L302) and stands at Kap 35 as „Vortex Beat 2" (L723); Kap 16 is „Diktatur der
Komplexität" (L335) and „Diktatur der physikalischen Zeit" (L705); it counts „39 fragmentierte
Kapitel" (L527) and maps Kap 0 and Kap 40. Where your page is concerned, give both.

**Read first:** the note `Sources/notes/kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md.md` and the
counts `Plan/runs/kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md/05-verify.txt`. Then read the whole
passages that concern your pages: `python3 scripts/read.py kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md --from N --to M`.

## Rules

1. **Never run any git command** (no stash, no checkout, no commit). Other readers are editing
   other files in the same tree. Edit only the files you are given.
2. Add one section per page, placed after the page's last `## Reading — …` section and before a
   `## Where the sources differ` / `## Open` / `## Occurrences only` that follows it (where the
   page interleaves, after its latest-dated reading):
   `## Reading — \`kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md\`, 2026-06-10, the philosophy catalogue — <what it adds>`
3. English prose around German quotations. Every quotation verbatim in „…" followed by
   `^[kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md.md:Lnn]` — the qualified form, always. **Every
   line number from** `python3 scripts/read.py kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md --find "<exact words>"`;
   never type one. Table cells: quote a short span, and check it with `--find`. Never translate.
   Never merge two statements. No quotation for an absence: state it with a `grep -cw` count and
   add the command and its output as a line to `Plan/runs/kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md/05-verify-readers.txt`
   (append; create if missing; one line per count, prefixed with your page name).
4. A reading says what **this** document says about the page's subject: definitions, where it
   places it (world, act, chapter), what it retires or keeps open, and its status words
   (its section label `[K]`/`[V]`/`[S]`/`[L]`, „offen", „kanonisch verortet", „Anti-Pattern", „nicht kanonisch"). Where the document relates other
   documents („Welt-Doku §8", „Steinbruch-Outline", „einer früheren Outline"), say it is the document's claim about them.
5. Frontmatter: append `"kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md"` to `ingested:`, add 1 to
   `sources:` and `readings:` (pages); for records see the record rules below.
6. Keep the page true: if its lead or `## Where the sources differ` states a claim this document
   falsifies („only X", „every source", „no read source …"), correct it and say which source moved
   it. Where the page has `## Where the sources differ`, add one line where this document takes a
   side or a new position, naming it „the philosophy catalogue". **Never resolve a difference.**
7. **A page that already reads this document** (the 2026-09-25 scan wrote readings from it on
   `vortex`, `komponente-734`, `goedel-gambit`, `genesis-klammer`, `ouroboros-struktur`,
   `kishotenketsu`, `chaitin-konstante`):
   do not add a second section. Check every quotation and claim in the existing reading against
   the full document, fix what is wrong, add what the full document says that the reading misses,
   and make its closing line say it was checked against the full document and that the document
   now has a census (`Sources/terms/…`) and a reconciliation (reconcile-28). Frontmatter unchanged
   except `ingested:` if the slug is missing.
8. Run `python3 scripts/quotes.py <file>` until 0 unresolved and 0 unchecked, and
   `python3 scripts/relations.py >/dev/null` (a `[[link]]` must point at an existing page).
9. Report per file: the heading, lines cited, any lead/differ claim changed and why, anything in
   the document that contradicts a page claim you did NOT change, and anything that looks like a
   new conflict (do not create records).

## Record rules (conflicts `Wiki/conflicts/`, questions `Wiki/questions/`)

Records are append-only, in date order of the entries' writing. Append at the end:
`## 2026-09-26 — \`kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md\`, 2026-06-10, the philosophy catalogue`
then a bold one-line summary of its position and the quotations, and one closing line saying
which row/side of the record it stands on, in the record's own terms. Add 1 to `sources:`. If the
document does not speak to the record, write nothing and report „not changed: <why, with a count>".

## Chapter rules (`Wiki/chapters/kap-NN.md`)

A reading goes on a chapter page only where the document says something about **that chapter
itself** (what happens there, which theory it anchors, which beat) — a range like „Kap 18–22" alone
does not, a named chapter with content does. The chapter table §14.3 (L688–739) is three cells per
chapter: chapter, theory, function. Format: `Wiki/chapters/README.md`, and the existing
readings on the page. Place it among the readings in date order (2026-06-10; after other
2026-06-10 readings), before `## Where the sources differ`. Frontmatter: append to `ingested:`,
add 1 to `sources:`. The chapter pages also carry four navigation sections written by a script
(What this chapter is about, Questions, Candidate sources, Raw qmd answers) — never edit those.
Then `python3 scripts/chapters.py` (it will complain the document is not reconciled — ignore
only that complaint) and `python3 scripts/quotes.py <page>`.
