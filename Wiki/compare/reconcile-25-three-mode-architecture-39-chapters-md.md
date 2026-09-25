---
document: three-mode-architecture-39-chapters-md
against: 106 pages, 15 conflicts
ran: "2026-09-25"
candidates: 338
decisions: 341
by_lookup: 179
judgements: 162
new_pages: 0
new_readings: 29
---

# Reconciliation 25 — `three-mode-architecture-39-chapters-md` against the wiki

`python3 scripts/reconcile.py three-mode-architecture-39-chapters-md`

338 candidates, 333 after two surface groups folded, 341 decisions — **179 by lookup, 162
to judgement** — and three sweep hits: one reading, two occurrences. Document 24 is a
workflow spec for encoding: „Companion zur generischen Workflow-Spec." ^[three-mode-architecture-39-chapters-md.md:L13]
It sets 39 chapters in three narrative modes of thirteen, orthogonal to the dual
storyform, and tables all 39. It never narrates, and it gives no date in its text.

Chosen because NOW.md named it twice: as possibly the 39-chapter spec another plan says
it extends, and as one of the ten documents the 2026-09-25 scan quoted. Five pages
already carried it; each reading was checked against the full document and stands.

## Is it the spec of 2026-05-08 another plan names?

Very likely. The Konzept-Iteration Genesis names „Das Spec-Dokument vom 2026-05-08 (drei Modi, 39 Kapitel)" ^[koharenz-protokoll-konzept-iteration-genesis-md.md:L818] as the one it extends with Kap 0 and Kap 40. This document is a spec of
three modes and 39 chapters; the manifest dates it 2026-05-08. And its cells stand in the
Konzept-Iteration Genesis word for word: Kap 6, „Hitzeschlieren, verzerrte Physik (Landauer-Wärme)" ^[three-mode-architecture-39-chapters-md.md:L183],
and Kap 36, „Landauer-Wärme als Schluss-Markierung; Stille danach" ^[three-mode-architecture-39-chapters-md.md:L341].
It names no date of its own, so the identification is the reconciliation's and is not
the document's claim.

## No new page

What matched no page is its encoding apparatus (modes, bridge share, riss scenes as a
technique, mikrocues, P1–P7, anti-patterns) and the stage names of the two borrowed
journeys. The stage names are chapter titles, so they go on the chapter pages.
`not_promoted` in `Plan/runs/three-mode-architecture-39-chapters-md/reconcile.json` has
each group. No new judgement was needed; recorded rules settled every near match.

## Readings — 29 pages, and 39 chapters

The lookup reached `aegis`, `juna`, `kael`, `moonshine-link`, `multiplizitaet`, `alters`,
`did`, `mosaik-herz`, `kern-welten`, `telefon-stille`, `trennungsprotokoll`, `guardians`,
`algorithmische-melancholie` and the twelve alters. Recorded rules reached `genesis`,
`landauer-signatur` and `potentialmeer` (J62), and the sweep reached `risse`, through
„Glitches, Stimmverschiebungen, ungewollte Handlungen" ^[three-mode-architecture-39-chapters-md.md:L171].

**Every chapter from Kap 1 to Kap 39 got a reading**, built from its table row: its stage
as the title, its mode, its bearer, its accent in each storyform, and its leitmotif.
Kap 35 and 36 also carry the beats, Kap 18–22 the Genesis flashbacks, and Kap 39 the rule
of the open ending. `chapters.py missing` could not have found them: the rows are
numbered without `Kap`.

## `plot.md` was wrong once more

It said the end game — a false victory in Kap 37 and Vortex 2 in Kap 38–39 — holds
in every plan but one, the master report. This spec is a second:
„**Drei Modi, zwei Storyforms, ein Vortex.**" ^[three-mode-architecture-39-chapters-md.md:L634]
Corrected to two, and the spec has its own reading there.

## Its storyform boundary, twice

„**Kap 34 → 35** ist die **eigentliche Storyform-Wendung**." ^[three-mode-architecture-39-chapters-md.md:L83]
„Die Storyform-Grenze liegt bei 36/37." ^[three-mode-architecture-39-chapters-md.md:L634]
L84 calls 36 → 37 the consolidation, so these may be a turn's start and its end. The
document does not reconcile them, and neither does the wiki.

## What moved

- **C11** — warmth in Kap 6 and Kap 36 Beat 4, in nearly the konsolidiertes Konzept's
  words, on its date; ozone as Part 1's air, never cold, never Landauer.
- **C12** — „Einheit → Trennungsprotokoll → Kael=Komp 734" ^[three-mode-architecture-39-chapters-md.md:L278]:
  the character bible's three steps, as flashbacks in Kap 18–22.
- **C14** — AEGIS-POV scenes from Kap 14 on, dominant in Kap 22; the person is not said.
- **C7** — Juna placed nowhere as an appearance: an echo, a witness, in danger.
- **Q1** — the Guardians as „OS-Physics: Guardians als Sub-Antagonisten" ^[three-mode-architecture-39-chapters-md.md:L337] in Kap 32, unnamed.
- **Q3** — thirteen alters by storyform, no world counted.
- **Q4** — a Wächterin, unnamed, in Kap 8 and Kap 17.

Read and unchanged: C1–C6, C8–C10, C13, C15, Q2 and Q5 (`records_read_and_not_changed`).

## What the reading ran into

**No zeros.** Briefing v13's steps held: every phrase was asked of `read.py --find` first,
and the three candidates the count could not take are counted by hand in `05-verify.txt`.

**A table cell escapes its emphasis and its tilde** (`\\\~10 %`). A quotation that
includes them fails, and one without them passes. The three bridge-share cells on
`plot.md` are quoted without the number, which is given beside them.
