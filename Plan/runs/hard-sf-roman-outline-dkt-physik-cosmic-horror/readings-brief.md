# Brief — readings from hard-sf-roman-outline-dkt-physik-cosmic-horror

Document 41: `Sources/drive/hard-sf-roman-outline-dkt-physik-cosmic-horror.md`, dated 2026-04-08 by the manifest, 265 lines, German.
**„Das Kohärenz Protokoll: Architektonik eines multidimensionalen Romans"** — a research report that is a
whole-novel plan: the premise (the TSDP disguised as AEGIS' hostile system for half the book), the world's
physics as four set-pieces (Landauer heat and ozone as AEGIS' weapon, Verlinde's entropic gravity, the
Bekenstein bound and the Island-Formel, ER=EPR as the bond between Kael and Juna), three tables (four
Kernwelten each with a „Zugeordneter Guardian", thirteen alters with ANP/EP category, AEGIS' twelve
protocols), the pacing and twist architecture, „Das Plot-Outline (Kapitel 1 – 39)" in three acts — Akt I
Murdock, Akt II cyclic, Akt III Campbell — one paragraph per chapter, and a checklist of thirteen
„Fixpunkte". Name it in prose as **„the Hard-SF-Outline"**. It is dated before the reset of 2026-04-30 and before
every canon-era document; say so where the order matters.

**Its standing, recorded, never applied**: no canon label; it calls itself „den vollständigen, detaillierten
Bauplan" (L13) and its checklist claims to embed „13 geforderten Fixpunkte" (L210) — required by whom, it
does not say. Every chapter paragraph is its plan, not the novel.

**Read first:** `Sources/notes/hard-sf-roman-outline-dkt-physik-cosmic-horror.md` (62 verified quotations), the census's end, and
`Plan/runs/hard-sf-roman-outline-dkt-physik-cosmic-horror/05-verify.txt`; then the document whole: `python3 scripts/read.py hard-sf-roman-outline-dkt-physik-cosmic-horror`.

**Export damage that matters:** 92 reference numbers glued to words („entstand.4", „Ozon.7") — quote the
words without the number; the Landauer relation (L25) and the Bekenstein bound (L174) stand as empty „()".
Tables escape their bold as `\*\*`; quote a short span of a cell and check it with `--find`.

**What it says that the records care about** (verify every one against the text before using it):
the knuckles bloody in Kapitel 1 (L94) and healed scars in Kapitel 39 (L206) — C10; Juna flickers in
Kapitel 3 (L98), sends coordinates in Kapitel 10 (L120), appears as a hologram in Kapitel 22 (L156) and
enters the system in Kapitel 34 (L190) — C7; a Guardian per Kernwelt, LogOS/Mnemosyne/Cerberus/„Kairos /
Sophia" (L40–43), Kairos and Sophia „die Guardians der Weisheit" (L178) — C6, C4, Q1, Q5; twelve AEGIS
protocols (L64–80) — Q2 and `aegis-teilfunktionen` (IntegrityGuardian L73, CogFirewall = „Cognitive
Firewall" L74, SIS L76); AEGIS a Täter-Introjekt „aus der Genesis-Krise (der Fragmentierungsnacht)" (L64)
and „aus dem Protagonisten selbst" (L158) — C3, C1; heat and ozone as erasure, Akt I cold, Akt II hot, KW4
„warmes Licht", Kapitel 37 heat cooling to warmth (L200) — C11; entropy made by suppression (L64) — C2;
the Fragmentierungsnacht as the twist of Kapitel 24 and the origin trauma's second layer (L160, L224) —
C12 and `genesis`; four Kernwelten and thirteen alters (Q3); KW4 an „Überwucherter Ruinengarten" (L43,
L172) — C5 only if a page or record already treats KW4's garden as the Möglichkeits-Garten.

Rules that apply: **J108** (new) — `Kapitel N` is a chapter label; its readings go on
`Wiki/chapters/kap-NN.md`, and `Kapitel 1` is not `Kapitel 10`. **J49** — Logos-Prime,
Mnemosyne-Archiv, Cerberus-Zitadelle, Kairos-Potentialis are world names: readings on `kern-welten`, and
on the Guardian's page only for what the Guardian column or a sentence says about the Guardian. **J60** —
an acronym is identified by the expansion its row gives: CogFirewall („Cognitive Firewall") is on
`aegis-teilfunktionen`; ZTEM („Zero-Tolerance Error Management") is not Zero-Trust. **J62** — Juna-Echo,
Coheron-Echo on `silas`, AEGIS-Echo on `oblivion`, by what they state. **J103** — „Kairos / Sophia" is a
reading on both. **J9** — chapter titles („Kollaps der Kohärenz", „Jenseits der Kohärenz",
„Fragmentierung") are titles, not the term. **J76–J78** — Genesis-Krise placed by its sentence. J56/J23
(plurals: Coherons, Erasonen, Alters), J97, J98/J99 (K1/K0 with plain digits on the kernel pages), J51.
Sweep calls are recorded: readings on `alters` (L29), `entropie` (L64), `guardians` (L178); `coheron` L61,
`erason` L62, `emergenz` L43 are occurrences.

**Your own scratch folder.** Each reader keeps helper scripts in its own subfolder of the session
scratchpad; never overwrite another's.

## Rules

1. **Never run any git command** (no stash, no checkout, no commit, no add, no diff that writes). Other
   readers are editing other files in the same tree. Edit only the files you are given.
2. Add one section per page **per document that speaks to it**, placed after the page's last `## Reading — …` section of a document dated
   on or before 2026-04-08, **in date order** (it is dated 2026-04-08: before every reading of late April and May 2026) and before `## Where the sources differ` /
   `## Open` / `## Occurrences only`:
   `## Reading — \`hard-sf-roman-outline-dkt-physik-cosmic-horror\`, 2026-04-08, the Hard-SF-Outline — <what it adds>`
   If the page is not in date order, put it after the last reading and say nothing about order.
3. English prose around German quotations. Every quotation verbatim in „…" followed by
   `^[hard-sf-roman-outline-dkt-physik-cosmic-horror.md:Lnn]` — the qualified form, always. **Every line
   number from** `python3 scripts/read.py hard-sf-roman-outline-dkt-physik-cosmic-horror --find "<exact words>"`;
   never type one. Table cells: quote a short span that is unique, and check it with `--find`. Never
   translate. Never merge two statements (no „…" joining two sentences into one quotation). No quotation
   for an absence: state it with a `grep -cw` count and append the command and its output as one line to
   `Plan/runs/hard-sf-roman-outline-dkt-physik-cosmic-horror/05-verify-readers.txt` (create if missing;
   prefix the line with your page name).
4. A reading says what **this** document says about the page's subject: definitions, where it places it
   (storyform, throughline, act, Kernwelt, chapter, beat), what it retires, reduces or keeps open, and its
   status words. For a chapter: what happens, where (Kernwelt, act, journey), who, and what it establishes. Short and precise: 3–12 quotations for a central page, 1–4 for a minor one.
5. Frontmatter: append `"hard-sf-roman-outline-dkt-physik-cosmic-horror"` to `ingested:`, add 1 to
   `sources:` and `readings:` (pages that carry `readings:`).
6. Keep the page true: if its lead or `## Where the sources differ` states a claim this document
   falsifies („only X", „every source", „no read source …", a count of sources), correct it and say which
   source moved it. Where the page has `## Where the sources differ`, add one line where this document
   takes a side or a new position, naming it „the Hard-SF-Outline". **Never resolve a difference.**
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
`## 2026-09-27 — \`hard-sf-roman-outline-dkt-physik-cosmic-horror\`, 2026-04-08, the Hard-SF-Outline`
Then a bold one-line summary of the document's position and the quotations, and one closing line saying which
row/side of the record it stands on, in the record's own terms. Add 1 to `sources:`, and append the slug where the record keeps a list of
documents in frontmatter, once. If the document does not speak to the record, write nothing and report
„not changed: <why, with a `grep -cw` count>".

## Chapter rules (`Wiki/chapters/kap-NN.md`)

A reading goes on a chapter page only where the document says something about **that chapter itself**
(what happens there, whose, which act, what it establishes) — a range boundary alone does not. Format:
`Wiki/chapters/README.md`, and the existing readings on the page. Place it among the readings in date
order (2026-04-08, before the readings of May 2026), before `## Where the sources differ`.
Frontmatter: append to `ingested:`, add 1 to `sources:`. Never edit the four navigation sections (What
this chapter is about, Questions for this chapter, Candidate sources, Raw qmd answers). Then
`python3 scripts/chapters.py` (it may complain the document is not reconciled — ignore only that) and
`python3 scripts/quotes.py <page>`.
