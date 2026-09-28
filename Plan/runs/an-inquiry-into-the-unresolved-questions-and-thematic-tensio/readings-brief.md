# Brief — readings from document 51

One document, read by readers split by page group.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 51 | `an-inquiry-into-the-unresolved-questions-and-thematic-tensio` | 2025-10-15 (manifest) | „the Inquiry file" | an English file of about fourteen reports of 2025, three of them twice: an Inquiry into open questions, a Concept Paper, an Editorial & Stylistic Guide, a Dramaturgical Framework, a Definitive Blueprint, `From Archetype to Architecture`, a Psychological Exposé, an untitled three-act text, a thematic analysis, a Case Study, a Psychological Assessment (dated April 28, 2025), „An Architecture of the Self" |

Read `Sources/notes/an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md`, the end of
`Sources/terms/an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md` („What the extraction ran into")
and `Plan/runs/an-inquiry-into-the-unresolved-questions-and-thematic-tensio/05-verify.txt` first, then the
document: `python3 scripts/read.py an-inquiry-into-the-unresolved-questions-and-thematic-tensio`.

**It is several reports, so name the report.** A reading says which report a passage comes from (the Guide, the
Blueprint, the Exposé, the Assessment, …) — the reports disagree with each other, above all on the cast. The
Inquiry stands twice (L11–102 and L103–193), the Concept Paper twice (L195–313 and L621–738), the Case Study
twice (L1277–1414 and L1415–1552), identical to the line. `read.py --find` then names two lines: **cite the
first copy**, and never count one passage twice.

**Its standing, recorded, never applied.** The Guide calls itself „the single source of truth" and its roster
„the single, canonical, and unalterable reference"; the Blueprint „This 11-alter model is the ground truth." Say
so where a reading rests on it. English throughout — quote it as written, never translate, and never render an
English surface as the page's German term inside a quotation.

**It has no chapter** (`Kap`, `Kapitel`, `Chapter`, `Vortex` 0): no chapter-page reading. Acts only.

**What it says that the pages care about** (verify each against the text):
- **Two rosters.** The Concept Paper, the Guide, the Framework and „An Architecture of the Self" list eight
  alters with `Praetor` (no page — never create one; mention on `alters` only) and `Oblivion`; the Blueprint and
  the Assessment list eleven with Alex, Lia, Isabelle, Moros and Argus and no Praetor or Oblivion (Q3). The last
  report names the split's sources (L1718). The Assessment's alter table gives `Flucht` to Kiko and Lia (C15;
  `Flight` 0).
- **Lex** is once „Dr. Aris Thorne" (J119 — on `lex`, not a surface). **Nyx** is „Her" in the Exposé (L1042) and
  „his" elsewhere — state it with the lines, do not resolve it.
- **AEGIS** expanded, „Autonomous Entropic Gatekeeper for Integrity Systems" (L1210, C1); its formula in German
  (L1212) and in English (L217); genesis as a minimal Ich against „The Nothingness Noise" (`nichts-rauschen`); the
  Guide's rules for AEGIS' voice, „cold, clinical, technical, and distant" (C14 — say only what the passages
  say about voice/person); „Negentropie-Fehlinterpretation" (`negentropie`); algorithmic melancholy
  (`algorithmische-melancholie`); autopoietic, operationally closed.
- **Kael** a fragment of AEGIS' „Origin-Self" („Ursprungs-Ich"), from its „Zerstückelung" in the „Genesis
  Crisis" (C12, `genesis`, `trennungsprotokoll` only where the passage describes the separation — J114: the
  Assessment's „erzwungenen Kohärenz-Partitionierung" goes on `trennungsprotokoll` by the sentence); Kael as
  „The Gardener" at the end; the Gödel-Gambit in the Überwelt (L602).
- **Juna/V** a „transcendent entity" from an „External Level" (`juna`, `externe-ebene`, C13); „The Foundation"
  (no page); the Moonshine-Link an „ontological exploit" (`moonshine-link`); „Potential Sea" (`potentialmeer`).
- **The worlds** under two schemes: „KW1: Logos-Prime (The Construct City)" … (J118, J120 — each world on its
  paged world, the English name not a surface), once by Guardian alone, „Kernwelt 1 (LogOS)", „Kernwelt 4
  (Kairos/Sophia)" (Q5, C6 — the author's five Guardians stand; C9 — the author's KW1 stands); KW4 also „The
  Garden of Potential" (L971); the logics per world (classical, paraconsistent, relevance, dialetheic). The
  Guardians twice, unnamed, building „a perfect wall" (L1151 / L609).
- **Scan pages.** `goedel-gambit`, `tsdp` and `komponente-734` already quote this document from the 2026-09-25
  scan. Check those quotations against the text; then add this document to the exceptions in the closing
  „Gathered 2026-09-25 …" line, naming `Sources/terms/an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md`
  and `Wiki/compare/reconcile-52-an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md`, as the line
  already does for other documents. Add a reading only where the page lacks one from this document.

Rules that apply: **J119, J120** (new), J118, J49, J68, J114, J20 (Wächter/Guardian), J100–J102 (an English
name on the German page by the sentence). Sweep calls in `Plan/runs/sweep.jsonl` put readings on `alters`,
`did`, `genesis`, `juna`, `kairos`, `sophia`.

## Rules

1. **Never run any git command**, not even a read-only one. Other readers are editing other files. Edit only
   the files you are given. Do not run `wiki_index.py`, `link.py` or `chapters.py overview`. Keep helper
   scripts in your own scratch folder.
2. One section per page **per document that speaks to it**: `## Reading — \`<slug>\`, <date>, <prose name> —
   <what it adds>`. Where a page is in date order, place it by date (2025-10-15) before `## Where the sources differ` / `## Open` / `## Occurrences only`; if the page is not in
   date order, after its last reading. First grep the page for the slug.
3. English prose around German quotations (49 is English — quote it as written). Every quotation verbatim in
   „…" followed by `^[<slug>.md:Lnn]`, always qualified. **Every line number from**
   `python3 scripts/read.py <slug> --find "<exact words>"`; never type one. Never translate. Never join two
   passages in one quotation, with […] or otherwise — quote each piece separately. Never put a straight `"`
   in prose between two quotations. No quotation for an absence: state it with a `grep -cw` count and append
   the command and its output, prefixed with your page name, to `Plan/runs/<slug>/05-verify-readers.txt`.
4. A reading says what **this** document says about the page's subject. 3–12 quotations for a central page,
   1–4 for a minor one.
5. Frontmatter: append the slug to `ingested:`, add 1 to `sources:` and `readings:` (where present).
6. Keep the page true: if a lead or `## Where the sources differ` states a claim a document falsifies
   („only", „every source", a count of sources), correct it and say which source moved it. Add one line under
   `## Where the sources differ` where a document takes a side or a new position, by its prose name. **Never
   resolve a difference, and never claim a position the text does not take** — no ordinal counts („a fifth
   title") you have not counted, no „a new position on Cn" unless the record's question is what the passage
   answers.
7. If a document says nothing about a page's subject beyond an occurrence, write no reading; report
   „not read: <why, with the line or a count>".
8. After each file: `python3 scripts/quotes.py <file>` shows 0 unresolved and 0 unchecked. At the end
   `python3 scripts/relations.py >/dev/null` (a `[[link]]` points at an existing page, chapter pages as
   `[[kap-NN|…]]`, never a path; a term linked at most once per page).
9. Report per file: the heading, lines cited, lead/differ claims changed and why, contradictions left in
   place, anything that looks like a new conflict (do not create records).

## Record rules (`Wiki/conflicts/`, `Wiki/questions/`)

Append-only, at the end: `## 2026-09-28 — \`<slug>\`, <date>, <prose name>`, then a bold one-line summary of
the document's position, the quotations, and one closing line saying where it stands in the record's own
terms. Add 1 to `sources:`, and append the slug where the record keeps a document list. If a document does
not speak to the record, write nothing and report „not changed: <why, with a count>".
