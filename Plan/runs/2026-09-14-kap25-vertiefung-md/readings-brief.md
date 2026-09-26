# Brief — readings from 2026-09-14-kap25-vertiefung-md

Document 28: `Sources/drive/2026-09-14-kap25-vertiefung-md.md`, dated 2026-09-14 by the manifest and in its own title
(„Sessionprotokoll — 2026-09-14", L11), the newest document in the corpus. **A log of one unattended
drafting run** that revised a manuscript's Kap 25 „Wegkreuzung" from 1,137 to 2,688 words (L19).
It does **not** contain the chapter — it reports what the run changed and why (L21–27), which
sources it used and how it ranked them (L29–43: a repository „normativ/[K]", four older Drive
documents `[S]`), a self-review against rules R-1…R-10 (L47), a storyform drift check (L51) and six
open decisions for the author, OQ-25-A…F (L55–60). So a reading says **what the log reports about the
chapter, or what it says its canon requires** — „the session log reports that the revised Kap 25 …",
„it says Canon §5 requires …" — and never presents the chapter's prose as quoted here. Every
„Canon verlangt" is its claim about other documents — **record it, never apply it** (decision 006;
the author decided C6 for five Guardians and C9 for the Konstrukt-Stadt as KW1, and nothing here
reverses that). Its six open decisions are its own questions; quote them where your page is
concerned. The chapter's prose is another document (`kp-kap25-2026-09-14-md`), not yet reconciled —
**do not read or cite it.**

Quotation marks: the document closes cited phrases with an ASCII `"` inside „…", so `--find` refuses a
span that contains one of them; quote up to it, or around it.

**Read first:** the note `Sources/notes/2026-09-14-kap25-vertiefung-md.md` (every line of the document is in it, cited) and
`Plan/runs/2026-09-14-kap25-vertiefung-md/05-verify.txt`. The document is 60 lines: read it whole,
`python3 scripts/read.py 2026-09-14-kap25-vertiefung-md`.

## Rules

1. **Never run any git command** (no stash, no checkout, no commit). Other readers are editing
   other files in the same tree. Edit only the files you are given.
2. Add one section per page, placed after the page's last `## Reading — …` section and before a
   `## Where the sources differ` / `## Open` / `## Occurrences only` that follows it (where the
   page interleaves, after its latest-dated reading):
   `## Reading — \`2026-09-14-kap25-vertiefung-md\`, 2026-09-14, the Kap-25 session log — <what it adds>`
3. English prose around German quotations. Every quotation verbatim in „…" followed by
   `^[2026-09-14-kap25-vertiefung-md.md:Lnn]` — the qualified form, always. **Every
   line number from** `python3 scripts/read.py 2026-09-14-kap25-vertiefung-md --find "<exact words>"`;
   never type one. Table cells: quote a short span, and check it with `--find`. Never translate.
   Never merge two statements. No quotation for an absence: state it with a `grep -cw` count and
   add the command and its output as a line to `Plan/runs/2026-09-14-kap25-vertiefung-md/05-verify-readers.txt`
   (append; create if missing; one line per count, prefixed with your page name).
4. A reading says what **this** document says about the page's subject: definitions, where it
   places it (world, act, chapter), what it retires or keeps open, and its status words
   („normativ", `[K]`, `[S]`, „kanonisch gefordert", „Autorentscheid nötig", „dekanonisierte"). Where the document relates other
   documents („Canon §5 verlangt …", „Canon/…storyform-und-outline §0", the `[S]` table), say it is the document's claim about them.
5. Frontmatter: append `"2026-09-14-kap25-vertiefung-md"` to `ingested:`, add 1 to
   `sources:` and `readings:` (pages); for records see the record rules below.
6. Keep the page true: if its lead or `## Where the sources differ` states a claim this document
   falsifies („only X", „every source", „no read source …"), correct it and say which source moved
   it. Where the page has `## Where the sources differ`, add one line where this document takes a
   side or a new position, naming it „the Kap-25 session log". **Never resolve a difference.**
7. No page reads this document yet; the 2026-09-25 scan did not touch it.
8. Run `python3 scripts/quotes.py <file>` until 0 unresolved and 0 unchecked, and
   `python3 scripts/relations.py >/dev/null` (a `[[link]]` must point at an existing page).
9. Report per file: the heading, lines cited, any lead/differ claim changed and why, anything in
   the document that contradicts a page claim you did NOT change, and anything that looks like a
   new conflict (do not create records).

## Record rules (conflicts `Wiki/conflicts/`, questions `Wiki/questions/`)

Records are append-only, in date order of the entries' writing. Append at the end:
`## 2026-09-26 — \`2026-09-14-kap25-vertiefung-md\`, 2026-09-14, the Kap-25 session log`
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
