# Brief — readings from monstergruppe-primzahlen-plot-blueprint

Document 43: `Sources/drive/monstergruppe-primzahlen-plot-blueprint.md`, dated 2025-04-26 by the manifest, 512 lines, German.
**„Kohärenz Protokoll: Finaler Plot-Blueprint"** — 39 chapters in three acts (Anomalie / Eindämmung,
Paradoxon / Emergenz, Integration / Konfrontation) on one premise: the Monstergruppe M is the
„Betriebssystem" of the simulation AEGIS runs, Kael's core resonates with it, his dissociation is the
product of AEGIS' attempt to analyse him, and AEGIS reads everything through a prime-number metaphor —
factorisation, misclassification — that the document says describes AEGIS' limit, not reality. Every
chapter has seven bullets (Konzeptfokus, Plot-Zusammenfassung, M-als-Fundament, Kael's Resonanz, K-J
Verbindung, AEGIS & Primzahl-Metapher, Genre-Elemente); Kapitel 33–35 share one entry; an overview table
closes it. Name it in prose as **„the Primzahl-Blueprint"**. It is the oldest whole-novel plan read.

**Its standing, recorded, never applied**: it calls itself „den finalen, detaillierten Plot-Blueprint"
and „verbindlich" (L15), yet hedges inside nearly every chapter („könnte", „möglicherweise",
„vielleicht") and leaves AEGIS' fate (Kapitel 31) and Kael's (Kapitel 32) among options. Say so where a
reading depends on an option.

**Read first:** `Sources/notes/monstergruppe-primzahlen-plot-blueprint.md` (33 verified quotations), the census's end, and
`Plan/runs/monstergruppe-primzahlen-plot-blueprint/05-verify.txt`; then the document whole: `python3 scripts/read.py monstergruppe-primzahlen-plot-blueprint`.

**Names it does not write**: no figure but Kael and AEGIS is named. Juna is only `J` (J111); no alter,
Guardian, world, `Konstrukt-Stadt`, `KW1`, `Genesis`, `734`, `DKT`, `K1`/`K0`, `Landauer`, heat or cold,
`Knöchel`, `Vortex` — `grep -cw` counts are in `05-verify.txt`. A record entry from this document is
usually its silence, stated with a count, or its own shape (Wächter as AEGIS' constructs; J's
separateness left open).

**What it says that the records and pages care about** (verify each against the text):
„Wächter" (Guardians) introduced by AEGIS in Kapitel 4 as „subtile Manipulationen der simulierten
Realität oder KI-Konstrukte, die als normale Bewohner der Kernwelt getarnt sind" (L60), a damaged one in
Kapitel 16 (L184) — Q4, Q1, C4, `guardians`; AEGIS „die Wächter-KI" (L17) — `aegis`; Kael's dissociation
caused by AEGIS' analysis (L17, L84) — `did`, `alters`, `kael`, C3 only if its record is about AEGIS'
origin rather than Kael's; the K-J Verbindung (J110 → `moonshine-link`); the Potentialmeer beyond M
(Kapitel 17, 37; L194, L195, L254, L396) — `potentialmeer`; „Jenseits der Mauer" (Kapitel 17's title) —
`grosse-mauer` only if the chapter's text is about the wall itself; Risse in the Kernwelt (Kapitel 5,
13) — `risse`; the alters fusing „zu einem kohärenten Ganzen" (L298) — `multiplizitaet` and C-records on
fusion; one Kernwelt, and in Kapitel 22 „mehreren verbundenen Kernwelten" (L244) — `kern-welten`, Q3.

Rules that apply: **J110** (new) — the K-J Verbindung „manifestiert sich als spezifische
Moonshine-Signatur" (L17): its passages go on `moonshine-link`, the name recorded there. **J111** (new) —
`J` is placed on `juna` as the figure under an initial; every such reading says the document writes only J.
**J108** — `Kapitel N` readings on the chapter pages; „Kapitel 33-35" (L373) is one entry for three
chapters: a reading on each of kap-33, kap-34 and kap-35 saying so. **J20** — Wächter/Guardian. **J9** —
chapter titles are titles. J56/J23, J51. Sweep calls are recorded: a reading on `did` (L17).

**Your own scratch folder.** Each reader keeps helper scripts in its own subfolder of the session
scratchpad; never overwrite another's.

## Rules

1. **Never run any git command** (no stash, no checkout, no commit, no add, no diff that writes). Other
   readers are editing other files in the same tree. Edit only the files you are given.
2. Add one section per page **per document that speaks to it**, placed after the page's last `## Reading — …` section of a document dated
   on or before 2025-04-26, **in date order** (it is dated 2025-04-26: after the 2025-04-17 and 2025-04-18 documents, before every reading of later 2025 and 2026) and before `## Where the sources differ` /
   `## Open` / `## Occurrences only`:
   `## Reading — \`monstergruppe-primzahlen-plot-blueprint\`, 2025-04-26, the Primzahl-Blueprint — <what it adds>`
   If the page is not in date order, put it after the last reading and say nothing about order.
3. English prose around German quotations. Every quotation verbatim in „…" followed by
   `^[monstergruppe-primzahlen-plot-blueprint.md:Lnn]` — the qualified form, always. **Every line
   number from** `python3 scripts/read.py monstergruppe-primzahlen-plot-blueprint --find "<exact words>"`;
   never type one. Table cells: quote a short span that is unique, and check it with `--find`. Never
   translate. Never merge two statements (no „…" joining two sentences into one quotation). No quotation
   for an absence: state it with a `grep -cw` count and append the command and its output as one line to
   `Plan/runs/monstergruppe-primzahlen-plot-blueprint/05-verify-readers.txt` (create if missing;
   prefix the line with your page name).
4. A reading says what **this** document says about the page's subject: definitions, where it places it
   (storyform, throughline, act, Kernwelt, chapter, beat), what it retires, reduces or keeps open, and its
   status words. For a chapter: what happens, where (Kernwelt, act, journey), who, and what it establishes. Short and precise: 3–12 quotations for a central page, 1–4 for a minor one.
5. Frontmatter: append `"monstergruppe-primzahlen-plot-blueprint"` to `ingested:`, add 1 to
   `sources:` and `readings:` (pages that carry `readings:`).
6. Keep the page true: if its lead or `## Where the sources differ` states a claim this document
   falsifies („only X", „every source", „no read source …", a count of sources), correct it and say which
   source moved it. Where the page has `## Where the sources differ`, add one line where this document
   takes a side or a new position, naming it „the Primzahl-Blueprint". **Never resolve a difference.**
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
`## 2026-09-27 — \`monstergruppe-primzahlen-plot-blueprint\`, 2025-04-26, the Primzahl-Blueprint`
Then a bold one-line summary of the document's position and the quotations, and one closing line saying which
row/side of the record it stands on, in the record's own terms. Add 1 to `sources:`, and append the slug where the record keeps a list of
documents in frontmatter, once. If the document does not speak to the record, write nothing and report
„not changed: <why, with a `grep -cw` count>".

## Chapter rules (`Wiki/chapters/kap-NN.md`)

A reading goes on a chapter page only where the document says something about **that chapter itself**
(what happens there, whose, which act, what it establishes) — a range boundary alone does not. Format:
`Wiki/chapters/README.md`, and the existing readings on the page. Place it among the readings in date
order (2025-04-26, before the readings of later 2025 and 2026), before `## Where the sources differ`.
Frontmatter: append to `ingested:`, add 1 to `sources:`. Never edit the four navigation sections (What
this chapter is about, Questions for this chapter, Candidate sources, Raw qmd answers). Then
`python3 scripts/chapters.py` (it may complain the document is not reconciled — ignore only that) and
`python3 scripts/quotes.py <page>`.
