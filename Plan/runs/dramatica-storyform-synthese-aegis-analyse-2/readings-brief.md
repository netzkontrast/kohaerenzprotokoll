# Brief — readings from dramatica-storyform-synthese-aegis-analyse-2

Document 40: `Sources/drive/dramatica-storyform-synthese-aegis-analyse-2.md`, dated 2026-04-30 by the manifest (the reset date), 524 lines,
German. **„Vollständige Synthese der dualen Dramatica-Storyformen für „Kohärenz Protokoll" mit
Verifikationstest der AEGIS-Throughline-Position in Storyform B"** — a research report: three
hypotheses on AEGIS' throughline in B (H1, AEGIS the MC in Universe, survives; H2 with Mnemosyne as MC
and H3 with a façade are rejected), eight per-throughline encodings (table, three scene seeds, two key
images, two rooms, a Block-4 check, a DKT-Korrelat), the dynamics with the Driver-Pivot at „Kapitel
35–36", a five-beat Vortex sheet, the Witness Function's three layers mapped onto beats, three open
questions answered with confidence, and method logs. Name it in prose as **„the Dramatica-Synthese"**.

**Its standing, recorded, never applied**: it confirms „Hypothese H1 (Status Quo des Kanons)" by its
own falsification; its sources are „Projekt-Kanon" PDFs and „User-Memory / Projekt-Wissen"; its
verdicts and confidences are its own. A scene seed is a proposal; say so.

**Read first:** `Sources/notes/dramatica-storyform-synthese-aegis-analyse-2.md` (55 verified quotations), the census's end, and
`Plan/runs/dramatica-storyform-synthese-aegis-analyse-2/05-verify.txt`; then the document whole: `python3 scripts/read.py dramatica-storyform-synthese-aegis-analyse-2`.

**Export damage that matters:** the kernel glyphs are gone — „Erasure Kernel ()", „(-Coherence Kern",
„Das -System", „-Knoten", „Chaitin .1" (Ω lost). Quote what stands; say the symbol is missing; place the
passage by the sentence (J98/J99: Coherence Kernel / Erasure Kernel, K1/K0).

Rules that apply: **J107** (new) — `Möglichkeiten-Garten` (L187, „ein Areal") is the Möglichkeits-Garten,
a reading about scale (C5); J50 (Kael's Wohneinheit, L91, on `kaels-wohneinheit`); J97 („Nichts-Rauschens"
genitive, on `nichts-rauschen`); J61 (a plural or other scale is a reading about scale — AEGIS' „massive
Trennungsprotokolle" in the OS (L205) and the „Trennungs-Protokolle" of H3 (L57) go on
`trennungsprotokoll` as this document's use of the name for AEGIS' ongoing operations); J70, J86, J90,
J91, J98/J99, J100, J49, J51.

**Your own scratch folder.** Each reader keeps helper scripts in its own subfolder of the session
scratchpad; never overwrite another's.

## Rules

1. **Never run any git command** (no stash, no checkout, no commit, no add, no diff that writes). Other
   readers are editing other files in the same tree. Edit only the files you are given.
2. Add one section per page **per document that speaks to it**, placed after the page's last `## Reading — …` section of a document dated
   on or before 2026-04-30, **in date order** (it is dated 2026-04-30: before every reading of May 2026) and before `## Where the sources differ` /
   `## Open` / `## Occurrences only`:
   `## Reading — \`dramatica-storyform-synthese-aegis-analyse-2\`, 2026-04-30, the Dramatica-Synthese — <what it adds>`
   If the page is not in date order, put it after the last reading and say nothing about order.
3. English prose around German quotations. Every quotation verbatim in „…" followed by
   `^[dramatica-storyform-synthese-aegis-analyse-2.md:Lnn]` — the qualified form, always. **Every line
   number from** `python3 scripts/read.py dramatica-storyform-synthese-aegis-analyse-2 --find "<exact words>"`;
   never type one. Table cells: quote a short span that is unique, and check it with `--find`. Never
   translate. Never merge two statements (no „…" joining two sentences into one quotation). No quotation
   for an absence: state it with a `grep -cw` count and append the command and its output as one line to
   `Plan/runs/dramatica-storyform-synthese-aegis-analyse-2/05-verify-readers.txt` (create if missing;
   prefix the line with your page name).
4. A reading says what **this** document says about the page's subject: definitions, where it places it
   (storyform, throughline, act, Kernwelt, chapter, beat), what it retires, reduces or keeps open, and its
   status words. Short and precise: 3–12 quotations for a central page, 1–4 for a minor one.
5. Frontmatter: append `"dramatica-storyform-synthese-aegis-analyse-2"` to `ingested:`, add 1 to
   `sources:` and `readings:` (pages that carry `readings:`).
6. Keep the page true: if its lead or `## Where the sources differ` states a claim this document
   falsifies („only X", „every source", „no read source …", a count of sources), correct it and say which
   source moved it. Where the page has `## Where the sources differ`, add one line where this document
   takes a side or a new position, naming it „the Dramatica-Synthese". **Never resolve a difference.**
7. If, after reading, the document says nothing about a page's subject beyond an occurrence (a word in a
   list, a title), do **not** write a reading — report „not read: <why, with the line>".
8. Run `python3 scripts/quotes.py <file>` until 0 unresolved and 0 unchecked for your new quotations, and
   `python3 scripts/relations.py >/dev/null` (a `[[link]]` must point at an existing page; link a term at
   most once per page, only where the prose already names it).
9. Report per file: the heading, lines cited, any lead/differ claim changed and why, anything in the
   document that contradicts a page claim you did NOT change, and anything that looks like a new conflict
   (do not create records).

## Record rules (conflicts `Wiki/conflicts/`, questions `Wiki/questions/`)

Records are append-only. Append at the end:
`## 2026-09-27 — \`dramatica-storyform-synthese-aegis-analyse-2\`, 2026-04-30, the Dramatica-Synthese`
Then a bold one-line summary of the document's position and the quotations, and one closing line saying which
row/side of the record it stands on, in the record's own terms. Add 1 to `sources:`, and append the slug where the record keeps a list of
documents in frontmatter, once. If the document does not speak to the record, write nothing and report
„not changed: <why, with a `grep -cw` count>".

## Chapter rules (`Wiki/chapters/kap-NN.md`)

A reading goes on a chapter page only where the document says something about **that chapter itself**
(what happens there, whose, which act, what it establishes) — a range boundary alone does not. Format:
`Wiki/chapters/README.md`, and the existing readings on the page. Place it among the readings in date
order (2026-04-30, before the readings of May 2026), before `## Where the sources differ`.
Frontmatter: append to `ingested:`, add 1 to `sources:`. Never edit the four navigation sections (What
this chapter is about, Questions for this chapter, Candidate sources, Raw qmd answers). Then
`python3 scripts/chapters.py` (it may complain the document is not reconciled — ignore only that) and
`python3 scripts/quotes.py <page>`.
