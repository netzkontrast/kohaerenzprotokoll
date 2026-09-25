---
document: kohaerenz-protokoll-konzept-master-md
against: 93 pages, 15 conflicts
ran: "2026-09-25"
candidates: 480
decisions: 510
by_lookup: 286
judgements: 224
new_pages: 1
new_readings: 46
---

# Reconciliation 21 — `kohaerenz-protokoll-konzept-master-md` against the wiki

`python3 scripts/reconcile.py kohaerenz-protokoll-konzept-master-md`

480 candidates, 471 after six surface groups folded, 510 decisions — **286 by lookup,
224 to judgement**, and three sweep hits. Document 20, the `Konzeptioneller
Master-Report` of 2026-05-08 (L11): the novel's theory in sixteen chapters — the physics, the
truth theories, the dissociation model, AEGIS, Juna, the Kern-Welten, the dual
storyform and the reader. It calls earlier PDFs `Steinbruch` and itself the
`Fundament` (L29), under a status line `Canon-Sync 2026-05-07` (L21). Both are its
claims about itself, recorded and not applied (decision 006).

Chosen because the previous handover named it: C8, C10, C11, C12, C14, C15 and Q5 all
had a word in it. It spoke to thirteen of the fifteen conflicts and all five questions.

## One new page — `truth-rotation`

The document gives the inversion a section of its own, „### II.6 Die Truth-Rotation — Warum AEGIS = K₀ und Kael = K₁" ^[kohaerenz-protokoll-konzept-master-md.md:L212],
and defines it by a table of what AEGIS believes against what holds (L218–L226).
`corpus.py count` finds the name in 20 documents. Seven of them were read, and none had
paged it. The page gathers all eight read sources, one commit each. They part on
what the name points at: the master report writes the inversion itself under it, and
four later sources call the inversion the `Große Inversion`, the mechanical
source of a Truth-Rotation that is the moment in the Vortex the reading turns (J91).
What holds, AEGIS = K₀ and Kael = K₁, they agree on. So the page records the
difference and no conflict record was opened.

`Witness-Funktion` is defined here too, as a three-layer `Komposit-Mechanik` (L627).
It stays on `juna`, where the glossary's reconciliation placed it: it is Juna's
function. Every other candidate that matched no page is listed with its reason under
`not_promoted` in `reconcile.json`.

## Readings — 46 pages

41 the lookup reached, and five more by recorded rules: `genesis` (J76–J79),
`landauer-signatur` (J62), `multiplizitaet` (J28), `atemporalitaet` by what the axis
states, and `blinder-fleck` and `did` by what their passages state. The sweep's three
hits are readings, each already on its page: `Entropie` L63, `Genesis` L998,
`Kohärenz` L38. Looked up and not read: `ueberwelt` (J39: `Simulation` here is the city),
`hitze-polaritaetsregel` (no polarity is stated), `drei-ontologische-schichten` (its
Schicht 1–3 are narrative layers) and `mosaik-herz` (`Mosaik` is the novel's form).

## What moved

- **C15** — row 8: „Flight (implizit Lia/Isabelle)" ^[kohaerenz-protokoll-konzept-master-md.md:L1049]. It is the only source that calls the
  assignment an inference. And its own roster has no alter with Flight (L393–L397).
- **C11** — heat and ozone as one signature of AEGIS' erasure: „Landauer wird zu Hitze und Ozon, nicht zu Gleichungen." ^[kohaerenz-protokoll-konzept-master-md.md:L1024]
  No warmth is Juna's or Silas', and Kap 6 is not named.
- **C7** — no chapter. „**Revelation-Timing:** KW2/KW3 (Akt II), nicht früher." ^[kohaerenz-protokoll-konzept-master-md.md:L571]
  Earlier than both Kap 33 and Kap 38, and the modes of appearance are open (L994).
- **C12** — three beats, locked, 734 the separation's remainder (L457–L469, L998). That
  is the character bible's count, on the date the konsolidiertes Konzept counts four.
- **C8** — Do-er in B, under the lock-in of 2026-05-07 the status line names as an
  `Approach-Korrektur` (L21).
- **C14** — third person for AEGIS and the Guardians, no exception (L404, L877).
- **C10** — the knuckles in the premise, in no chapter (L51).
- **C6, Q5** — two Guardians, the five of earlier drafts absorbed into Mnemosyne and
  the Erasure-Pol, without saying which into which (L504–L513); the worlds are act markers, „nicht "eine pro Guardian"" ^[kohaerenz-protokoll-konzept-master-md.md:L665]. The author's five stand.
- **C2, C3, C4, C5, C9** — AEGIS is the entropy, K₀ the condition of events (L63,
  L107); the Genesis is an episode of AEGIS' coming-to-be, Kael its remainder (L459,
  L465); the blindness is AEGIS' alone (L477); KW4 is the whole Möglichkeits-Garten
  (L661); KW1 is the Konstrukt-Stadt of Akt I (L658).
- **Q1–Q4** — the two Guardians as K₀ sub-operators in B's overall story (L961–L962);
  twelve protocols become three, none of the eight (L517); exactly thirteen alters and
  act-marker worlds, with world ranges for the alters in the matrix (L383, L665,
  L952–L958); `Wächter` for Mnemosyne and in an open point (L508, L1002).

Read and unchanged: C1 (AEGIS is not expanded) and C13 (no Basisrealität, Externe
Ebene or Köln).

## The plot and the chapters

**Two claims of `Wiki/overview/plot.md` were no longer true, and are corrected there.**
It said every 2026 plan read counts 41 movements. This one counts „39 Kapitel, 3 Akte, Vortex Kap 35–36" ^[kohaerenz-protokoll-konzept-master-md.md:L21],
with no Kap 0 and no Kap 40. And it said the plans agree on Vortex 1, a false victory
and Vortex 2. This one has one Vortex and a resolution, „Nur A aktiv, Konsolidierung" ^[kohaerenz-protokoll-konzept-master-md.md:L907].
Both on the date the konsolidiertes Konzept counts 41 movements and two Vortices.

Readings went onto Kap 4, 13, 28, 33, 35 and 36. Kap 14 stays off: the document names
it only as the start of KW2's range. `chapters.py` holds with 0 defects.

## Judgements

Three new rows. **J89**: `Flight (implizit Lia/Isabelle)` is the riss type, and its
parenthesis is an inferred claim about bearers, never an alias. **J90**: `Rotation`, the
Vortex's fifth beat, is the beat and not the Truth-Rotation. **J91**: `Große Inversion`
is not an alias of `Truth-Rotation` in the sources that name one the source of the
other. Every other near match was decided by a recorded rule, named in
`reconcile.json`. `judgements.py` replays 91 rows: 8 agree, 0 disagree.

## What the reading ran into

`quotes.py` stopped one defect before it was committed: `eine fremde Entität in der
Leere`, a nominative written for the line's `einer fremden Entität` (L463). That is the
defect the check was built for.
