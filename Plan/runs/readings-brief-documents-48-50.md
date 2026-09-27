# Brief — readings from documents 48–50

Three documents, reconciled together, read by readers split by page group.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 48 | `charakter-kompilation-fuer-kohaerenz-protokoll` | 2026-03-31 | „the Charakter-Kompilation" | a model's consolidated character bible: eleven Anteile in fixed fields with gaps marked, Juna, AEGIS, the Guardians, a relation matrix, its own contradiction register |
| 49 | `the-sensory-rulebook-the-body-as-a-measuring-device-in-the-p` | 2025-11-03 | „the Sensory Rulebook" | an English essay: the four Kernwelten as psycho-architectures, each named twice, with a Guardian, a sensory signature and a somatic motif |
| 50 | `ki-prompt-analyse-hard-problem-of-consciousness` | 2026-04-28 | „the Hard-Problem-Analyse" | a model's report: two Dramatica storyforms (K1, K0) as the Hard Problem of Consciousness, crossed through the Trennungsprotokoll and the Landauer-Wärme |

For each: read `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and
`Plan/runs/<slug>/05-verify.txt` first, then the document: `python3 scripts/read.py <slug>`.

**Their standing, recorded, never applied.** 48 is a model's compilation that calls a status report „Hard
Canon", ranks documents by maturity, cites its own bracket numbers ([31, 32, …]) that are not this corpus's,
and „Dekanonisiert" names — say so where a reading rests on it. 50 rates its own storyforms (A 5.0, B 4.75)
and cites a corpus it does not contain (a „Hard Canon Masterfile", NotebookLM). 49 asserts and never hedges.

**Two of them were scanned on 2026-09-25**: pages already quote 48 and 50 (`goedel-gambit`,
`kishotenketsu`, `komponente-734`, `ouroboros-struktur`, `thermodynamischer-phaenomenalismus`, `tsdp`), and
their closing „Gathered 2026-09-25 …" line says the scanned documents have no census and no reconciliation.
On those pages: check the existing quotations of 48 and 50 against the text, then add 48/50 to the list of
exceptions in that closing line, naming `Sources/terms/<slug>.md` and the reconciliation
(`Wiki/compare/reconcile-49-charakter-kompilation-fuer-kohaerenz-protokoll.md`,
`Wiki/compare/reconcile-51-ki-prompt-analyse-hard-problem-of-consciousness.md`), as the line already does for
earlier documents. Add a reading only where the page lacks one from that document; if the scan reading
already covers it, say „not read: already read from the scan, checked".

**What they say that the pages care about** (verify each against the text):
- **48:** eleven Anteile — Kael [ANP/Host], Lex [ANP/Rationalist] „Komponente 734", Alex [ANP/Protector]
  „Wächter an der Grenze", Rhys [ANP/Caregiver], Selene [ANP/Integrator/ISH] „von einer starren Wächterin
  (Blockade) zur Architektin", Nyx [EP/Fight], Kiko [EP/Freeze/Child], Lia [EP/Ambivalent/Child]
  „Flucht-Annäherung-Ambivalenz", Isabelle [EP/Sexualisiert], Moros [EP/Kollaps] whose Riss makes the
  temperature sink, Argus [Sonder/Meta-Kognitiv] — each with a DKT correlate, a Riss-Typ, a somatic marker,
  and „[Fehlt in den Dokumenten - Lücke]" where it has none. No alter carries Flight (C15). Juna an external
  entity of the Externe Ebene *and* Kael's „exilierte Ursprungs-Ich" (J68; its own „Juna/V Paradoxon"). AEGIS
  expanded (C1), its Primal Directive in English, the Trennungsprotokoll as AEGIS dismembering its own
  Ursprungs-Ich (C12). Guardians: LogOS KW1, Mnemosyne KW2, Cerberus KW3, Kairos & Sophia KW4 (C6, Q5 — the
  author's five stands). Silas and Oblivion „Dekanonisiert"; Eos, Nox, Limina, Praetor legacy names tied to
  the four worlds. Its contradiction register: Rhys ANP or EP, Isabelle's class, 11 vs. 13+ alters (Q3).
- **49:** KW1 Logos-Prime = Konstrukt-Stadt (C9 — the author's decision KW1 stands), KW2 Mnemosyne-Archipel =
  Resonanz-Landschaft, KW3 Cerberus-Labyrinth = Grenzfeste, KW4 Kairos-Potentialis = Möglichkeits-Garten (J118,
  J49); Guardians LogOS, Mnemosyne, Cerberus, Kairos and Sophia (Q5, C6); somatic motifs per world; KW4 has
  „Geruch von Ozon oder frischer Erde" and „warmes, dynamisches Licht" — ozone and warmth together, Juna's
  world (C11); KW2 „plötzliche Kälte oder Wärme"; AEGIS as „externalisiertes Täterintrojekt".
- **50:** A — MC Psychology (Kael), IC Universe (AEGIS), OS Physics (Landauer-Wärme), RS Mind
  (Trennungsprotokoll); B — MC Universe (AEGIS), IC Psychology (Kael), OS Mind, RS Physics; MC Approach Be-er
  in A, **Do-er in B, where the MC is AEGIS** (C8); Driver Action in both, „Hitze treibt" in B (C11); „Kael
  und AEGIS kommunizieren an keiner Stelle des Werks durch direkten verbalen Dialog" (C14); Kapitel 13
  „Dance in the Garden", Kapitel 32 „Kael/M", Kapitel 35–36 the Gödel-Gambit; „Das T-734 Trauma" (J112); K1 and
  K0 in plain digits (J98, J99 — place on `kohaerenz-kernel` and `kollaps-kernel` by the sentence);
  Landauer-Wärme (J117 — on `landauer-signatur` and `hitze-polaritaetsregel` by the sentence); the telephone
  silence (`telefon-stille`); the Ouroboros ending; AEGIS' algorithmische Melancholie; „13 Alters (inkl.
  Moros/Oblivion)" in its corpus (Q3); Juna pure K1.

Rules that apply: **J117, J118** (new), J49, J68, J88, J98, J99, J100, J108 (Kapitel N on kap-NN), J112, J20
(Wächter/Guardian: Alex „Wächter an der Grenze", Selene „starre Wächterin" — Q4). Sweep calls are recorded in
`Plan/runs/sweep.jsonl` (readings on `alters`, `entropie`, `risse`, `guardians`, `genesis`).

## Rules

1. **Never run any git command**, not even a read-only one. Other readers are editing other files. Edit only
   the files you are given. Do not run `wiki_index.py`, `link.py` or `chapters.py overview`. Keep helper
   scripts in your own scratch folder.
2. One section per page **per document that speaks to it**: `## Reading — \`<slug>\`, <date>, <prose name> —
   <what it adds>`. Where a page is in date order, place it by date (49: 2025-11-03; 48: 2026-03-31; 50:
   2026-04-28) before `## Where the sources differ` / `## Open` / `## Occurrences only`; if the page is not in
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

Append-only, at the end: `## 2026-09-27 — \`<slug>\`, <date>, <prose name>`, then a bold one-line summary of
the document's position, the quotations, and one closing line saying where it stands in the record's own
terms. Add 1 to `sources:`, and append the slug where the record keeps a document list. If a document does
not speak to the record, write nothing and report „not changed: <why, with a count>".

## Chapter rules (`Wiki/chapters/kap-NN.md`)

A reading only where the document says something about that chapter itself (50: Kapitel 13, 32, 35–36).
Format as the existing readings and `Wiki/chapters/README.md`; frontmatter `ingested:` and `sources:`; never
edit the four navigation sections. Then `python3 scripts/chapters.py` (ignore only „not reconciled"/„not
read"/stale overview) and `python3 scripts/quotes.py <page>`.
