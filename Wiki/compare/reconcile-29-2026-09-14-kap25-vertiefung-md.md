---
document: 2026-09-14-kap25-vertiefung-md
against: 106 pages, 15 conflicts
ran: "2026-09-26"
candidates: 153
decisions: 146
by_lookup: 111
judgements: 35
new_pages: 0
new_readings: 19
---

# Reconciliation 29 — `2026-09-14-kap25-vertiefung-md` against the wiki

`python3 scripts/reconcile.py 2026-09-14-kap25-vertiefung-md`

153 candidates, 146 decisions — **111 by lookup, 35 to judgement** — and two sweep hits, one
reading and one title. Document 28 is the newest document in the corpus: the log of one
unattended drafting run of 2026-09-14 that revised a manuscript's Kap 25, „Unbeaufsichtigter
Wochenlauf. Arbeitssprache Deutsch. Ein Kapitel, substanziell." ^[2026-09-14-kap25-vertiefung-md.md:L13]
It does not contain the chapter. It reports what the run changed and why, the sources it used and
how it ranked them — a repository „Repo (normativ/" ^[2026-09-14-kap25-vertiefung-md.md:L31] `[K]`,
four older Drive documents `[S]` — a self-review against ten drafting rules, a storyform drift
check, and six open decisions for the author. Every `Canon verlangt` in it is its claim about
other documents: recorded, not applied (decision 006).

## No new page

Every candidate that matched no page is the run's vocabulary for the chapter (Schwellensequenz,
Nicht-Handlung, Optionlock, Restzahl), a rule it checked against (R-1…R-10,
Ein-Falschheits-Regel, Benennungslock), a place named once (Platte 204, Treppenschacht,
Wartungsebene, Station 7), or a name it quotes in order to drop it (Nox, Limina, Kai). Nothing is
defined. The near matches were decided by existing rules — J8/J28 for compounds, J83 by analogy
for `Hitze-Polarität`, J77 for `Genesis-Echo`, J53 for `Echo`, J50 and J80 for the numbered
dwelling and unit, J62 and J9 for the TSDP row — so no judgement is new.

## Readings — 15 pages, `plot.md`, three chapters, four conflicts and one question

Written by three Claude readers in the container from one brief, each file reviewed, quote-checked
and committed on its own; `plot.md` by the session.

- **Figures:** `kael` (the decision given a bearer — the hand at 10:58 and a second tension in the
  same forearm — and the veil sentence „Hier sitzt mehr als einer." ^[2026-09-14-kap25-vertiefung-md.md:L21]),
  `aegis` (the directive registering the deviation without a measure; OQ-25-A: unnamed in drafted
  Akt II), `juna` (R-10, and warmth only as a back-reference), `alex`, `lex` (signatures the run
  says it used, in a suspended compound).
- **Places and worlds:** `konstrukt-stadt`, `kern-welten`, `kaels-wohneinheit`, `komponente-734` —
  OQ-25-F, its canon's KW2 for 14–22 and KW3 for 23–28 against a drafted Akt II set wholly in the
  Konstrukt-Stadt, „Das ist die größte offene Frage des Laufs." ^[2026-09-14-kap25-vertiefung-md.md:L60]
- **Rules and motifs:** `hitze-polaritaetsregel` (R-5: cold ozone only in the sign-off scene;
  a contested line), `telefon-stille`, `vortex` (the missing click of Vortex 1 Beat 3, and a local
  pre-form in Kap 25), `tsdp`.
- **Guardians:** `guardians`, `cerberus` — „gefiltert: dekanonisierte Guardians (Cerberus, Nox,
  Echo, Limina) nicht übernommen" ^[2026-09-14-kap25-vertiefung-md.md:L39]. The grouping is the
  log's: read sources have Nox, Echo and Limina as Alters, and Cerberus is one of the author's five.
- **Chapters:** Kap 25 (a second title, `Wegkreuzung`, beside the Plot-Konkretisierung's `Die Niederlegung`), Kap 24 and Kap 26 (the threshold sequence 24–26, the hook in and the hook out).
- **Records:** C6, C9, C11, C14 and Q5; the other ten conflicts and four questions checked and not
  changed, each with the count that shows it (`Plan/runs/2026-09-14-kap25-vertiefung-md/reconcile.json`).
- **`plot.md`:** a manuscript of 41 chapter files, Kap 0 among them; Kap 27/28 in Akt III.

## What moved

- **C9** gains its sharpest statement yet from the drafting side: the chapters its canon assigns to
  KW2 and KW3 all play in the Konstrukt-Stadt, and the log asks whether that is `Filterregime statt Ortswechsel`. The author's decision — the Konstrukt-Stadt is KW1 — stands; the log's question is
  recorded as its own.
- **C6:** one more source that reduces the Guardians, by calling an older concept's four names
  `dekanonisiert` — three of which are not Guardians in any read source.
- **C11:** the post-lock separation applied in one chapter, with neither signature given a bearer.

## Tensions inside the document

None within itself. It differs from its sources on two points it states as fact: the four names
it calls Guardians, and a log format it says the Sprach-DNA provides `ab Akt II`, which a reader
found in neither landed Sprach-DNA document.

## Retrieval moved

PageRank recall@8 0.643 → 0.637, one case: C4 0.556 → 0.444. `cerberus` left C4's top eight and
`alters` entered it — the readings on `cerberus`, `guardians` and `kern-welten` each link
`[[alters]]`, and the hub rose again, the same mechanism as document 27's fall. Recorded with
`bench --record`.

## What the reading ran into

- **A log about a chapter, not the chapter.** Every reading says `the log reports` or `it says its canon requires`; the chapter's prose is document 29, reconciled after this one.
- **A lens term from memory.** `Dramatica` was listed while reading and stands 0 times; it was
  removed before the count (`05-verify.txt`).
- **Quotation marks in two glyphs.** It closes a cited phrase with an ASCII mark inside „…", so
  `read.py --find` refuses a span that contains one.
- **A number at the start of a quotation.** `41 Kapiteldateien` did not resolve against its line
  in `quotes.py`, while `Wortzahlen aller 41 Kapiteldateien` did: the glued-footnote rule drops a
  number after a word on the line side, so a quotation that begins with that number keeps it and the
  line does not. Worked around here by quoting from the word before; noticed, not fixed.
- **`kern-welten`'s frontmatter** held one more `ingested:` entry than `sources:` before this
  reading; both moved by one, and the gap stands.
