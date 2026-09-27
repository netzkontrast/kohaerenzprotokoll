---
document: worldbuilding-konzept-kohaerenzprotokoll-md
against: 106 pages, 15 conflicts
ran: "2026-09-26"
candidates: 385
decisions: 424
by_lookup: 280
judgements: 144
new_pages: 0
new_readings: 66
---

# Reconciliation 27 — `worldbuilding-konzept-kohaerenzprotokoll-md` against the wiki

`python3 scripts/reconcile.py worldbuilding-konzept-kohaerenzprotokoll-md`

418 candidates, 385 after seventeen surface groups folded, 424 decisions — **280 by lookup,
144 to judgement** — and four sweep hits, all readings. Document 26 is a world bible of
2026-05-08: „**Stand:** 8. Mai 2026 · Post-Reset-Kanon (2026-04-30) · inkl. Storyform-Korrekturen 2026-05-07" ^[worldbuilding-konzept-kohaerenzprotokoll-md.md:L17].
It calls itself „*Steinbruch*, nicht Korsett" ^[worldbuilding-konzept-kohaerenzprotokoll-md.md:L21] and ranks itself last: „Diese Datei dient als operative Referenz, nicht als Source-of-Truth." ^[worldbuilding-konzept-kohaerenzprotokoll-md.md:L968]
Recorded, not applied (decision 006). Chosen as next on NOW.md's reading suggestion: the
vector search had placed it for 25 chapters, and the 2026-09-25 scan had quoted it on six pages.

## No new page

The world it builds lands on pages that exist — 55 reached by lookup. What matched no page
is its method (encoding phases, Lesersteuerung, Computational Class, style levels), borrowed
mathematics and philosophy, fifteen names it calls *Dekanonisiert* (L423), sub-locations without a
chapter (document 11's rule), and terms many read documents already name with no page: the
Erasure-Pol in fourteen, the Witness-Funktion in eight, the Fragmentierungsnacht and the
Ursprungs-Ich in seven. Every earlier reading left those unpaged; whether one should become a
page is put to the author in NOW.md. Recorded rules settled every near match — no new judgement.

## Readings — 56 pages, `plot.md`, nine chapters, and every record but C8

Seven Claude readers in the container wrote them, one set each, from
`Plan/runs/worldbuilding-konzept-kohaerenzprotokoll-md/readings-brief.md`; every line number came from `read.py --find`, every
stated absence is a count in `05-verify.txt` or `05-verify-readers.txt`, and the session
reviewed each file and committed it on its own. The six scan readings of 2026-09-25 were
checked against the full document: every quotation stood; `goedel-gambit`'s said *two
sentences* and quoted one, and `vortex`'s *Open* gave the document one answer about the
witness layers where it holds three (L340, L813–L821, L350). Both corrected.

**Leads made true again.** Five Guardian pages said nothing else read names the figure; each
now gives the count. `mosaik-herz`, `garten-der-stillen-praesenz`, the four world pages and
`nexus` had counts or pairings this document moved. `plot.md` said every plan but two has a
Kap 40 and two Vortices: this is a third 39-chapter plan with one Vortex, „39-Kapitel-Map." ^[worldbuilding-konzept-kohaerenzprotokoll-md.md:L954]
`evaluierungseinheit` carried a false citation of another document, found by its reader and corrected.

## What moved

**C1** — the expansion „*Autonomous Entropic Gatekeeper for Integrity Systems*" ^[worldbuilding-konzept-kohaerenzprotokoll-md.md:L166].
**C2** — AEGIS is the entropy it fights. **C3** — AEGIS as Kael's own defence architecture made
world (L188). **C5** — both scales, KW4 as a garden and the Möglichkeits-Garten in it. **C6** —
two Guardians, the five named as the old drafts' „Lore-Last" ^[worldbuilding-konzept-kohaerenzprotokoll-md.md:L192]; the author's decision
for five stands. **C7** — revelation in Akt II, a nameless seed from Ch1, acceptance at the
Mosaik-Herz in Ch34; no Kap 38. **C9** — KW1, as decided. **C10** — the knuckles in the premise,
the physics and KW1's Risse, in no chapter. **C11** — heat and ozone one Landauer signature of
the erasure (L82). **C12** — three beats, the fourth „offen … Lock-In steht aus" ^[worldbuilding-konzept-kohaerenzprotokoll-md.md:L184].
**C13** — not outside the simulation, and it also writes „Basisrealität Köln" ^[worldbuilding-konzept-kohaerenzprotokoll-md.md:L431]. **C14** —
AEGIS only in logs. **C15** — „(Flight, Lia/Isabelle)" ^[worldbuilding-konzept-kohaerenzprotokoll-md.md:L682]. **Q1–Q5** each have an entry.
**C8** is not changed: no Approach for AEGIS is stated.

## A tension inside the document

Juna is the „transzendente Anomalie" ^[worldbuilding-konzept-kohaerenzprotokoll-md.md:L179] the Ursprungs-Ich meets in the Genesis, and the
Ursprungs-Ich itself, „Es spaltet das Ursprungs-Ich (Juna) ab" ^[worldbuilding-konzept-kohaerenzprotokoll-md.md:L435]. The document does
not relate the two. It is the question NOW.md holds as J68 and J75, here a month before the
glossary that led to it.

## What the reading ran into

**The checker had a blind spot, and a page stood on it.** A cited quotation under eight
characters matched nothing, so „(Ch13)" on `evaluierungseinheit` — cited to a line of another
document that does not hold it — was neither checked nor counted. `quotes.py` now checks every
cited quotation; 72 more were checked across the tree, none unresolved. Three self-test cases,
the first failing on the old code.

**Much of it is the konsolidiertes Konzept's text.** The readers found the System Kael part,
the riss table, the world sections and the Landauer sentence word for word in the concept
document of the same date; `reconcile.json` lists what each has that the other lacks.
