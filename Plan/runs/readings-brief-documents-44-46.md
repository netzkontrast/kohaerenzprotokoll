# Brief — readings from documents 44–46

Three documents, reconciled together, read by readers split by page group.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 44 | `duale-storyform-synthese-kohaerenz-protokoll` | 2026-04-28 | „the Duale Storyform-Synthese" | two complete Dramatica storyforms on the axis Change/Success against Steadfast/Failure, joined in a „5D" phase space |
| 45 | `dramatica-storyform-synthese-aegis-analyse` | 2026-04-30 | „the AEGIS-Analyse" | the earlier run of document 40's report: AEGIS the MC of B (H1), eight encodings, a five-beat Vortex in Kapitel 35–36, the Witness Function |
| 46 | `m-als-fundament-der-simulation` | 2025-04-26 | „the M-Fundament-Blueprint" | a plot blueprint in 39 beats on the Monstergruppe as the simulation's physics, the companion of document 43 |

For each: read `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and
`Plan/runs/<slug>/05-verify.txt` first, then the document: `python3 scripts/read.py <slug>`.

**Their standing, recorded, never applied.** 44 and 45 rate and resolve their own storyforms and cite a
corpus they do not contain („Memory-Kanon", „PDF-Kanon", „Project Codex", a NotebookLM corpus) — say so
where a reading rests on it. 45 recommends changing Growth in A to Stop; 44 gives Judgment Good in B, 45
Bad. 46 hedges every beat and leaves its ending among options.

**What they say that the records care about** (verify each against the text):
- **44:** A — Kael MC in Psychology, Juna IC in Physics („Juna/V-Vektor"), AEGIS OS in Mind, RS Universe
  (the Moonshine-Link); B — Kael MC in Universe, AEGIS **IC** in Mind, OS Physics, RS Psychology (the K-J
  Vektor). The Approach is Kael's in both, Be-er in A, Do-er in B (C8 is about AEGIS' Approach: 44 gives
  AEGIS none). Kael/M in Kapitel 32; T-734 the core trauma (J112); thirteen alters named in its corpus
  „(Alpha, Mosaik-Herz, Schatten, T-734, K-J Vektor etc.)" (Q3); Juna's nature open — external anomaly or
  exiled part (C7's companion question, and `juna`); „AEGIS laut Werk-Anker emergent aus Kael" (C3); the
  Kernwelten as inner rooms, Logos-Prime and the Cerberus-Labyrinth (J49); the ending image „Die Trennung
  war nie real. Das ändert nichts am Schmerz." (`ouroboros-struktur`); the telephone silence as key image
  (`telefon-stille`); Landauer-Wärme as driver (C11); exodus into the Potentialmeer; three parts, Kap 1-13,
  14-26, 26-39 (`plot.md`); Kapitel 8, 9, 11, 18, 24, 28, 32, 35–36 named.
- **45:** AEGIS MC of B in Universe, Mnemosyne as a Guardian MC rejected (H2, C6/Q1/Q4), „Wächterin des
  Resonanz-Archipels" (J49 for the archipelago); AEGIS' „algorithmischer Einsamkeit" and an „I"-position
  (C14); B ends Failure/**Bad**; the Driver-Pivot in Kapitel 35–36; Beat 1 cold — „in den Minusbereich"
  (C11), Beat 4 the heat spike; Lex, Nyx, Kiko, Moros do not fuse (Beat 2); Witness layers in Beats 2, 3, 5
  (document 40 has 2, 3, 4 on the `vortex` and `juna` pages); AEGIS after the Vortex a broken loop, not a
  consciousness (`algorithmische-melancholie` — document 40 says a proto-consciousness); the
  Moonshine-Boundary universal in principle, exclusive in the narrative; Growth Stop recommended; kernel
  glyphs lost (J98/J99).
- **46:** the Monstergruppe as physics (J110 for the K-J connection → `moonshine-link`); AEGIS existing by
  negation of the Potentialmeer; isolated Kernwelten as AEGIS' experiments (`kern-welten`); Kael's
  fragmentation an IFS stress response, alters as protector parts, lost time (`did`, `alters`); **Alters
  and Guardians as AEGIS' agents** (Beats 3, 10, 38 — `alters`, `guardians`, C4, Q1); J only an initial
  (J111) with three possible natures (Beat 18); AEGIS perhaps a VOA construct misunderstanding its purpose
  (Beat 23, C3); the ending between integration and separation (Beat 29).

Rules that apply: **J112** (new) — `T-734` is placed on `komponente-734` as this source's sense of the
number (Kael's core trauma, once a fragment), never as a second name of the component. J49, J50, J53
(Stille is not Telefon-Stille unless the sentence says telephone), J60, J61, J62, J86, J91, J97, J98/J99,
J100 (English names by the sentence), J107, J108, J110, J111, J20 (Wächter/Guardian). Sweep calls are
recorded: readings on `entropie` from 44 (L15) and 45 (L59).

**Your own scratch folder.** Each reader keeps helper scripts in its own subfolder of the session
scratchpad; never overwrite another's.

## Rules

1. **Never run any git command**, not even a read-only one. Other readers are editing other files.
   Edit only the files you are given. Do not run `wiki_index.py`, `link.py` or `chapters.py overview`.
2. One section per page **per document that speaks to it**:
   `## Reading — \`<slug>\`, <date>, <prose name> — <what it adds>`. Where a page is in date order,
   place it by date (46: 2025-04-26; 44: 2026-04-28; 45: 2026-04-30) before `## Where the sources differ` /
   `## Open` / `## Occurrences only`; if the page is not in date order, after its last reading.
3. English prose around German quotations. Every quotation verbatim in „…" followed by
   `^[<slug>.md:Lnn]`, always qualified. **Every line number from**
   `python3 scripts/read.py <slug> --find "<exact words>"`; never type one. Never translate. Never join two
   sentences into one quotation, and never put an inner „…" inside a quotation — split it. Never put a
   straight `"` in prose between two quotations. No quotation for an absence: state it with a
   `grep -cw` count and append the command and its output, prefixed with your page name, to
   `Plan/runs/<slug>/05-verify-readers.txt`.
4. A reading says what **this** document says about the page's subject: definitions, where it places it
   (storyform, throughline, act, Kernwelt, chapter, beat), what it keeps open, and its status words. 3–12
   quotations for a central page, 1–4 for a minor one.
5. Frontmatter: append the slug to `ingested:`, add 1 to `sources:` and `readings:` (where present).
6. Keep the page true: if a lead or `## Where the sources differ` states a claim a document falsifies
   („only", „every source", a count of sources), correct it and say which source moved it. Add one line
   under `## Where the sources differ` where a document takes a side or a new position, by its prose name.
   **Never resolve a difference.**
7. If a document says nothing about a page's subject beyond an occurrence, write no reading; report
   „not read: <why, with the line or a count>".
8. After each file: `python3 scripts/quotes.py <file>` shows 0 unresolved and 0 unchecked for your
   quotations. At the end `python3 scripts/relations.py >/dev/null` (a `[[link]]` points at an existing
   page, chapter pages as `[[kap-NN|…]]`, never a path; a term linked at most once per page).
9. Report per file: the heading, lines cited, lead/differ claims changed and why, contradictions left in
   place, anything that looks like a new conflict (do not create records).

## Record rules (`Wiki/conflicts/`, `Wiki/questions/`)

Append-only, at the end: `## 2026-09-27 — \`<slug>\`, <date>, <prose name>`, then a bold one-line summary
of the document's position, the quotations, and one closing line saying where it stands in the record's
own terms. Add 1 to `sources:`, and append the slug where the record keeps a document list. If a document
does not speak to the record, write nothing and report „not changed: <why, with a count>".

## Chapter rules (`Wiki/chapters/kap-NN.md`)

A reading only where the document says something about that chapter itself. Format as the existing
readings and `Wiki/chapters/README.md`; frontmatter `ingested:` and `sources:`; never edit the four
navigation sections. Then `python3 scripts/chapters.py` (ignore only „not reconciled"/„not read"/stale
overview) and `python3 scripts/quotes.py <page>`.
