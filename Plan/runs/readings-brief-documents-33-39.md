# Brief — readings from seven documents of 2026-05-08 (documents 33–39)

Seven English documents, all dated 2026-05-08 by the manifest, all read by the session with a
candidate list, census and note. **Read each one whole before writing** — they are short (42–228
lines): `python3 scripts/read.py <slug>`. Their notes (`Sources/notes/<slug>.md`) hold verified
quotations to start from, and each census ends with „What the extraction ran into";
`Plan/runs/<slug>/05-verify.txt` has the absence counts.

| n | slug | prose name | what it is |
|---|---|---|---|
| 33 | `mining-report-kohaerenz-protokoll-plot-outline-construction` | the Plot/Outline Mining-Report | eleven seeds per throughline, a K0-log/K1-sensation table, the telephone call, the Vortex (Chapters 35–36) in five points, four alters' somatics |
| 34 | `mining-report-kohaerenz-protokoll-narrative-building-blocks` | the Narrative Building Blocks report | twenty seeds per throughline, the Kernwelten with LogOS, Mnemosyne, Cerberus as carriers („The Cerberus Labyrinth (KW3)"), the 12 Protocols, the Vortex (Ch35-36) in five beats, somatic gaps, a contradiction log (Juna „an exiled part of Kael's Ursprungs-Ich") |
| 35 | `systemic-architecture-specification-the-coherence-protocol-w` | the Systemic Architecture Specification | a world bible calling itself „the binding rulebook": DKT, Great Inversion, AEGIS, Genesis-Crisis in three beats with Component 734 „the precursor to Kael", two Guardian Sub-Systems (Mnemosyne, Erasure-Pol), the log protocol, Juna, a thirteen-alter table with somatic filters, the four Core Worlds with names (Construct-City/Logos-Prime, Mnemosyne-Archipelago/Resonance Landscape, Cerberus-Labyrinth/Border Fortress, Kairos-Potentialis/Garden of Possibilities), Risse mapped to EPs (no Flight), the External Level (Cologne 2026), the Vortex (Chapters 35–36), the Ouroboros Chapter 39 ↔ Chapter 1 |
| 36 | `companion-guide-to-the-coherence-protocol-understanding-love` | the Companion Guide | an explanatory guide: love as Coheron, the DKT, Landauer as somatic filter („The Smell of Ozon", bleeding knuckles), AEGIS with two Guardians, the thirteen alters, Juna, the Vortex (Chapters 35-36), the Ouroboros (a phone ringing, a choice to speak) |
| 37 | `the-architecture-of-fracture-a-compendium-of-the-kael-system` | the Architecture of Fracture | a compendium of the Kael system: DKT, Great Inversion, thirteen alters (Selene „Entanglement Islands", Rhys „Anker Akt I → Kudzu Akt II"), the two-layered trauma (Cologne; Fragmentation Night, Juna banished as the original „Ich"), two Guardians (the Erasure-Pol „absorbing the functions of logic and temporal control"), Kernwelten, no Vortex |
| 38 | `editorial-style-dossier-somatic-and-linguistic-implementatio` | the Editorial Style Dossier | writing rules: somatic filter table, computational classes as syntax, Spiegel alters, acts with chapter ranges (Ch. 1-13, 14-26, 27-39), Juna's and AEGIS' constraints („AEGIS never speaks in prose"), five mandates |
| 39 | `the-physics-of-heartbreak-5-surprising-takeaways-from-the-ko` | the Physics of Heartbreak | a popular essay: the opening image (21 degrees, ozone, „hemorrhaging knuckles"), AEGIS as „Kael’s own defense architecture externalized", love as Coheron, heat, a Dramatica translation, the Ouroboros ending |

**Their standing, recorded, never applied** (decision 006): 33 and 34 mark every seed
„Kanon-Kompatibel"/„KANON-KOMPATIBEL" against „the 2026-05-08 Kanon"; 35 calls itself „the binding
rulebook"; 36, 37 and 39 cite nothing; 38 gives mandates. What a document says its sources say is its
claim. A seed („Lever:") is a proposal; a sample sentence in a voice (38's cheat sheet) is diction.

**They are English.** Quote them verbatim in English (and the German words they write as written);
never translate. Their English names for what the wiki pages in German — Construct-City, Garden of
Possibilities, Mnemosyne-Archipelago, Resonance Landscape, Separation Protocol, Component 734,
Phone-Silence, Coherence/Collapse Kernel, Coherons/Erasons, Algorithmic Melancholy, Functional
Multiplicity — go on the German page **by the sentence** (J100–J102: a translation is not a surface);
the reading says the document writes the English name. **J49**: a world named for a Guardian
(Logos-Prime, Cerberus-Labyrinth, Kairos-Potentialis) is not the Guardian; a sentence making a
Guardian a world's carrier (34's „Carrier: LogOS") is a reading on the Guardian.

Rules already decided that apply: J60 (the AEGIS expansion), J70 (a role compound on its bearer),
J74 and J93 (Erason-Operator, AEGIS-Echo on oblivion; Coheron-Echo, Juna-Echo on silas), J76–J78 (the
Genesis-Crisis is not the Genesis; what it states of the Genesis is a reading on genesis), J86, J90
(a Vortex beat placed by what it states), J53/J62/J81 (heat, ozone), J71 (Moonshine), J98/J99 (K1/K0
plain digits are the kernels by the sentence), J104 (RS-A is not RSA), J51.

**Sweep calls already made** (put these readings on the pages): the Companion Guide's `Genesis` L43
(what AEGIS did in the Genesis Crisis) on `genesis`, its `The 13 Alters` L56 on `alters`, its Vortex
L98 on `vortex`; the Architecture of Fracture's „The Two Guardians" L49 on `guardians`; the Editorial
Style Dossier's „Spiegel Alters" L40 on `alters`.

## Rules

1. **Never run any git command** (no stash, no checkout, no commit, no add, no diff that writes). Other
   readers are editing other files in the same tree. Edit only the files you are given.
2. Add one section per page **per document that speaks to it**, placed after the page's last `## Reading — …` section of a document dated on
   or before 2026-05-08, **in date order** (all seven are dated 2026-05-08: put them after every reading of that date already on the page,
   in the order of the table below) and before `## Where the sources differ` /
   `## Open` / `## Occurrences only`:
   `## Reading — \`<slug>\`, 2026-05-08, <the document's prose name> — <what it adds>`
   If the page is not in date order, put it after the last reading and say nothing about order.
3. English prose around German quotations. Every quotation verbatim in „…" followed by
   `^[<slug>.md:Lnn]` — the qualified form, always. **Every line
   number from** `python3 scripts/read.py <slug> --find "<exact words>"`;
   never type one. Table cells: quote a short span that is unique, and check it with `--find`. Never
   translate. Never merge two statements (no „…" joining two sentences into one quotation). No quotation
   for an absence: state it with a `grep -cw` count and append the command and its output as one line to
   `Plan/runs/<slug>/05-verify-readers.txt` (create if missing;
   prefix the line with your page name).
4. A reading says what **this** document says about the page's subject: definitions, where it places it
   (storyform, throughline, act, Kernwelt, chapter, beat), what it retires, reduces or keeps open, and its
   status words. Short and precise: 3–12 quotations for a central page, 1–4 for a minor one.
5. Frontmatter: append `"<slug>"` to `ingested:`, add 1 to
   `sources:` and `readings:` (pages that carry `readings:`).
6. Keep the page true: if its lead or `## Where the sources differ` states a claim this document
   falsifies („only X", „every source", „no read source …", a count of sources), correct it and say which
   source moved it. Where the page has `## Where the sources differ`, add one line where this document
   takes a side or a new position, naming it „<the document's prose name>". **Never resolve a difference.**
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
`## 2026-09-27 — \`<slug>\`, 2026-05-08, <the document's prose name>`
Then a bold one-line summary of the document's position and the quotations, and one closing line saying which
row/side of the record it stands on, in the record's own terms. Add 1 to `sources:`, and append the slug where the record keeps a list of
documents in frontmatter, once. If the document does not speak to the record, write nothing and report
„not changed: <why, with a `grep -cw` count>".

## Chapter rules (`Wiki/chapters/kap-NN.md`)

A reading goes on a chapter page only where the document says something about **that chapter itself**
(what happens there, whose, which act, what it establishes) — a range boundary alone does not. Format:
`Wiki/chapters/README.md`, and the existing readings on the page. Place it among the readings in date
order (2026-05-08; after the other readings of that date), before `## Where the sources differ`.
Frontmatter: append to `ingested:`, add 1 to `sources:`. Never edit the four navigation sections (What
this chapter is about, Questions for this chapter, Candidate sources, Raw qmd answers). Then
`python3 scripts/chapters.py` (it may complain the document is not reconciled — ignore only that) and
`python3 scripts/quotes.py <page>`.
