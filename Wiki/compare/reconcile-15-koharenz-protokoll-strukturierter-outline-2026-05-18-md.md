---
document: koharenz-protokoll-strukturierter-outline-2026-05-18-md
against: 92 pages, 12 conflicts
ran: "2026-09-24"
candidates: 569
decisions: 587
by_lookup: 357
judgements: 230
new_pages: 0
new_readings: 43
---

# Reconciliation 15 — `koharenz-protokoll-strukturierter-outline-2026-05-18-md` against the wiki

`python3 scripts/reconcile.py koharenz-protokoll-strukturierter-outline-2026-05-18-md`

569 candidates after folding, 587 decisions — **357 by lookup, 230 to judgement.**
Document 14, the „Strukturierter Outline aller 41 Bewegungen" ^[koharenz-protokoll-strukturierter-outline-2026-05-18-md.md:L11] of 2026-05-18: one
entry per chapter from Kap 0 to Kap 40, each on the same template.

## Why this one

It speaks to more open records than any other unread canon-era document: C7
(Juna's first appearance), C10 (the knuckles), C11 (Landauer warmth), C12 (the
Genesis), Q5 (the Erasure-Pol) and the Mosaik-Herz question. A chapter outline is
where a chapter placement is the plan rather than an aside.

## What kind of document this is

**A plan, asserted, that names its sources and which of them wins.** „Stand der
Quellen: 2026-05-08 (Konzept-Konsolidierung, Storyweaving-Startdokument),
2026-05-07 (Dual-Storyform-Lock-In)" ^[koharenz-protokoll-strukturierter-outline-2026-05-18-md.md:L13]; „Bei Konflikt zwischen Quellen gewinnt
das Konzept-Dokument 2026-05-08." ^[koharenz-protokoll-strukturierter-outline-2026-05-18-md.md:L1393] **Recorded, not applied** (decision 006).
No passage labels, no questions in prose; its open questions are a table, OQ-A to
OQ-G, the same letters as the konsolidiertes Konzept's.

## No pages, by the rule an outline supplies

An outline places; it defines almost nothing it does not also name as known. Its
cast (§1) is the wiki's already — the thirteen Alters, AEGIS, Juna, Mnemosyne —
plus the Erasure-Pol, whose name it marks open (L161, J59). Its worlds (§2) carry
the bearers' names (J49). The rest is its own structure (the four levels, the
modes, Bridge, chapter and beat titles — J31, J9), Dramatica slot vocabulary, and
names used without being explained (Controlled Fragmentation Protocol, Stress-Test
Delta-7, Lyons-Welt, Babymonster-Welt, Gödel-Gambit). `Komponente 734` stays a
reading on [[kael]]. The Vortex architecture — „Vortex 1 ist operativ …, Vortex 2
ist ontologisch" ^[koharenz-protokoll-strukturierter-outline-2026-05-18-md.md:L31] — is the nearest thing to a definition and waits for a source
that defines it rather than schedules it.

## Readings — 43 pages

The 37 lookup hits, and six reached by rule: [[genesis]] and [[landauer-signatur]]
(their subjects, C12 and C11), [[externe-ebene]] (Basisrealität, J54),
[[kaels-wohneinheit]] (J50), [[kohaerenz]] (Kap 34's two kinds of coherence) and
[[kael-julia-bindung]] (`K-J-Verbindung`, J13). `reconcile.json` lists each page's
lines.

## What it adds to the open records

**Ten conflicts and four questions.** The ones that move:

| | this document | line |
|---|---|--:|
| C7 | Juna's first direct appearance is Kap 38 Beat 3, stated five times; Kap 33 does not name her | 121, 1174 |
| C10 | **a third position**: the knuckles are a standing trait of the Host, in no chapter — neither Kap 0 nor Kap 1 | 125 |
| C11 | warm in Kap 6, 22 and 36, in the konsolidiertes Konzept's words for Kap 36, twelve days before the cold-ozone lock | 385, 1128 |
| C12 | both orders — 734 before the separation in Kap 0, after it in the flashbacks — and a fourth beat, two weeks before the Kapitel-Kompendium, which has the same | 230, 765, 1208 |
| Q5 | two accounts of the absorption in one document (LogOS into the Erasure-Pol and into Mnemosyne; Kairos absorbed and latent) — and **Sophia placed**: latent, in KW4 | 161, 172, 175 |
| Q4 | two bearers: AEGIS as the Genesis' Wächter, Selene's Wächterin-Funktion | 237, 649 |

C1 (position 1), C3 (an origin inside the Genesis), C5 (the world side), C6 (two,
after the author's five), C8 (the lock-in's values), C9 (consistent with the
decision), Q1 (Sub-Antagonisten, no component statement) and Q3 (worlds answer to
classes of Alters) take a reading each. **C2, C4 and Q2** were read against it and
not changed: Entropie occurs only in the AEGIS expansion, no blind spot is named,
none of the eight protocols occurs.

## For the author's questions in `NOW.md`

- **The Ursprungs-Ich (J68 → J75).** Here it is AEGIS: „AEGIS (Ursprungs-Ich →
  Wächter)" ^[koharenz-protokoll-strukturierter-outline-2026-05-18-md.md:L237]. A third position beside the glossary's gloss as Juna and its
  own passage where it resonates with Juna.
- **Mosaik-Herz** stands in both chapters of one document, Kap 11 (L489) and
  Kap 34 (L1057), without saying whether it is one thing.
- **The final form's name** is again a working term, OQ-A (L1369).

## Judgements

J69–J75. The rest of the 230 were decided by J9, J10, J15, J16, J20, J21, J24,
J26, J28, J29, J31, J44, J47, J49, J51, J52, J54, J55, J57, J59, J60 —
`reconcile.json` names the rule for each group of pairs. The `fold()` baseline moved
58% → 57% (33/57 → 36/63): the three new one-term pairs are ones it cannot see.

## Found while reading, fixed before quoting

- **Chapter numbers were invisible to the quotation check.** The footnote rule
  dropped a number after a word on both sides, so `Kap 33 Beat 3` resolved against
  a line reading `Kap 38 Beat 3` — and this document carries 268 such numbers and
  no footnote. `quotes.py` and `read.py --find` now compare numbers on their own;
  measured before the change, none of the 298 verified quotations with a number
  had one its line lacked.
- **`capture.py` left three candidates out of the count** without saying so —
  titles with a comma, a beat with a period. It now names what it reads as prose.

## Second readers

The tools installed on 2026-09-24 read this document after its candidate list
was committed, each with Claude as the model — `Plan/runs/koharenz-protokoll-strukturierter-outline-2026-05-18-md/second-readers/`
has what they produced and how each scored against the reader's list. None of
their output entered a page.
