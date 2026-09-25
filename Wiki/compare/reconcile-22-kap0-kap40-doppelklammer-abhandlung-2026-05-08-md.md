---
document: kap0-kap40-doppelklammer-abhandlung-2026-05-08-md
against: 105 pages, 15 conflicts
ran: "2026-09-25"
candidates: 183
decisions: 189
by_lookup: 112
judgements: 77
new_pages: 1
new_readings: 14
---

# Reconciliation 22 — `kap0-kap40-doppelklammer-abhandlung-2026-05-08-md` against the wiki

`python3 scripts/reconcile.py kap0-kap40-doppelklammer-abhandlung-2026-05-08-md`

183 candidates, 181 counted, 189 decisions — **112 by lookup, 77 to judgement** — and one
sweep hit. Document 21, „Die Doppel-Klammer Kap 0 / Kap 40" ^[kap0-kap40-doppelklammer-abhandlung-2026-05-08-md.md:L11] of 2026-05-08: a
treatise arguing that Kap 0 and Kap 40 are one frame and must be skeletoned together. It
decides nothing and asks for three decisions, „Bestätigung der drei Setzungen" ^[kap0-kap40-doppelklammer-abhandlung-2026-05-08-md.md:L616].

Chosen because the handover named it: two plans of 2026-05-08 disagree on the Kap 0 /
Kap 40 frame. It is also one of the ten documents the 2026-09-25 scan quoted without a
census, so this reconciliation gives the pages that already quoted it the census they
lacked. And it starts from the 105 pages the scan left, so `account.py order` holds again.

## One new page — `formel-inversion`

The document gives it a mirror point of its own, „### V.5 Die Formel-Inversion" ^[kap0-kap40-doppelklammer-abhandlung-2026-05-08-md.md:L337], and calls it
„die mechanische Achse der gesamten Klammer" ^[kap0-kap40-doppelklammer-abhandlung-2026-05-08-md.md:L348]. `corpus.py count` finds the
name in 8 documents, and all eight are read. Six earlier readers listed it and no record
says why it had no page. The page gathers all eight, one commit each. The sources agree
on both sentences word for word and part on where the second falls: at the turn from Kap
39 to Kap 40, in Vortex 2 or Kap 39, or — here alone — at Kap 40's Klick.

Every other candidate that matched no page is under `not_promoted` in `reconcile.json`.
One of them should be read next: `Ursprungs-Ich` is in 53 landed documents, and six read
ones, and has no page. This document only names it as Beat 1's subject.

## Readings — 14 pages, and four the scan had

The lookup reached `aegis`, `kael`, `juna`, `alters`, `nichts-rauschen`, `k0-existenz`,
`potentialmeer`, `genesis`, `trennungsprotokoll`, `lex`, `nyx` and `kiko`; recorded rules
reached `drei-ontologische-schichten` and `hitze-polaritaetsregel` (J62, placed by what the
passage states). `genesis-klammer`, `vermittler-stimme`, `residual-echos` and
`komponente-734` already carried a reading from this document, written by the scan; those
readings stand, and each page's closing note now names this reconciliation. `ouroboros-struktur`
cites the document only to contrast it — the frame is not a circle — and takes no reading.

Looked up and not read: `risse` (`Riss` is the Genesis' split and a crack in a draft's
prose), `mosaik-herz` (`Mosaik` is Kap 40's carried shards), `entropie-resonanz` and
`resonanz-landschaft` (`Resonanz` is Juna's), and two substrings of `Einheit`. The sweep's
one hit, `Kohärenz` L17, is the title.

## What moved

- **C12** — four beats, and a place for each: „Beats 2 und 3 sind Kap 0." ^[kap0-kap40-doppelklammer-abhandlung-2026-05-08-md.md:L169] „Beat 4 ist Kap 39." ^[kap0-kap40-doppelklammer-abhandlung-2026-05-08-md.md:L173]
  Beat 1 is told nowhere. The konsolidiertes Konzept's count and order; what it adds is
  that Kap 0 tells only two of the four.
- **C11** — warmth as the substance of Juna's resonance in Kap 0, the `Wärme-Spur`,
  proposed and named as coming from a chat turn (L315). Cold is AEGIS' manner, not a
  sensation (L442); no ozone, no Landauer.
- **C8** — Be-er in A, Do-er in B, and Kap 0 / Kap 40 built on the pair (L392, L396).
- **C14** — Kap 0 in the first person of the Funken-Ich, scaling into description of AEGIS
  (L430); no AEGIS chapter is named.
- **C7** — Juna is felt as resonance in Kap 0 and recalled in Kap 40; no appearance is
  placed, and she is not the narrator (L243).
- **Q3** — `Mira`, among the Wir's voices (L327), stands in no other landed document.

Read and unchanged: C1–C6, C9, C10, C13, C15, Q1, Q2, Q4, Q5 — the document names no
Guardian, no Kern-Welt, no Entropie and no riss type (`records_read_and_not_changed`).

## The plot and the chapters

Readings went onto Kap 0, 39 and 40, and `plot.md` has a reading of its own. **Kap 40's
last image moved.** The document gives it as „Kap 40 endet (laut Konzept) auf:" ^[kap0-kap40-doppelklammer-abhandlung-2026-05-08-md.md:L368]
„Wir tragen die Scherben" ^[kap0-kap40-doppelklammer-abhandlung-2026-05-08-md.md:L372]. But both concept documents of its date read here, the
Konzept-Iteration Genesis and the konsolidiertes Konzept, end on „Wir tragen die Welt" ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L1040].
So the „Konzept" it quotes is neither of them as landed. That is recorded under
`## Where the sources differ` on Kap 40. On Kap 0 it
disputes a reading it attributes to a `Storyweaving-Dokument`: B is not active before the
Klick either (L112). `chapters.py` holds with 0 defects.

## Judgements

One new row. **J94**: `Doppel-Klammer` is the Genesis-Klammer, the same two chapters as
one frame, and becomes its alias. Every other near match was decided by a recorded rule,
named in `reconcile.json` — J47 and J73 for the AEGIS compounds, J83 for `Reinform`,
J62 for passages placed by what they state, J53 for shared heads, J76 for sequences named
for a thing.

## What the reading ran into

**Four candidates counted zero because the list wrote them in the nominative** —
`großer Wandel`, `fallendes Glas`, `theoretischer Beobachter`, and `Beat 2` / `Beat 3`
for „Beats 2 und 3" ^[kap0-kap40-doppelklammer-abhandlung-2026-05-08-md.md:L169]. The list was committed before the count and left as written; the
correction is in `05-verify.txt`. The briefing already asks that a surface be written as
the document writes it; an inflected phrase is the case it does not name.

**A claim about the text was wrong, and a grep caught it while the C11 entry was
written — not `quotes.py`**: the census first said no `kalt` stands in the document. It stands three
times, as AEGIS' manner. Census, page and C11 were corrected before the reconciliation
was closed. `quotes.py` checks what is quoted; an absence can only be checked by
counting, and the count was in `05-verify.txt` for ozone and Landauer, not for cold.
