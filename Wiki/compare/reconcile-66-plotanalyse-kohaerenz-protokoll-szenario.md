---
document: plotanalyse-kohaerenz-protokoll-szenario
against: 106 pages, 15 conflicts
ran: "2026-10-05"
candidates: 55
decisions: 56
by_lookup: 46
judgements: 10
new_pages: 0
new_readings: 12
---

# Reconciliation 66 — `plotanalyse-kohaerenz-protokoll-szenario` against the wiki

`python3 scripts/reconcile.py plotanalyse-kohaerenz-protokoll-szenario`

55 candidates, 56 decisions — **46 by lookup, 10 to judgement**. Dated 2025-04-23 by the manifest: a German review report, a „kritische, forschungsbasierte Bewertung“ ^[plotanalyse-kohaerenz-protokoll-szenario.md:L17] of the plot idea of a commissioning text it cites as `User Query` — the AEGIS/Monster(Kael/Juna) scenario — with a concept-to-plot matrix, a section per element, strengths, weaknesses, comparisons with literature and film, and a recommendation to pursue it (L239). It claims no canon. The scenario's elements are the User Query's; the concepts' meanings are the report's.

It is the document record 62's research report analysed as its reference 87, read on the question record 62 put to the author. Candidate list, census and note by a Sonnet `document-reader` from the full-ingest task, no count before the list; the session read sections A–D against the note and corrected nothing. 14 files by one Sonnet `wiki-reader` from `Plan/runs/ingest-66/brief.md`, each its own commit naming the document.

## No new page

A review report: its candidates are the concepts it applies (Monstrous Moonshine, Gödel, autopoiesis, IFS, NET, Jung's shadow, holism, Church-Turing) and the scenario's elements the wiki already pages (AEGIS, Kael, Juna, the link, the Potentialmeer, the Kernwelten). The one element no page holds, the entity M, stands here as the commissioning text's and as the report's metaphor; M already appears on kael as Kael/M and in C16, and one review is not the source that defines it.

## Judgements

No new judgement. Every near match was decided by an existing rule (`Plan/runs/judgements.md`): J9 (a title containing a term: Tiefenanalyse und Bewertung der Plot-Idee, the work title in quotation marks), J12 and J16 (a compound is its own token: Kael-Juna-Verbindung, AEGIS-System, K-J-Verbindung), J24 and J97 (a plural or case ending is no boundary: Kaels, Potentialmeers, Rissen), J28 and J32 (a compound is placed by what it names: Kohärenz durch Integration, Kohärenz durch Abgrenzung), J37 (a numbered instance is a reading on its class: Kernwelt 3), J69 (a match only after folding: transpersonalen Psychologie / personas), J88 (a common noun for a page's referent is placed by the sentence: Simulationshypothese).

## Readings — 12 pages

`aegis`, `alters`, `did`, `emergenz`, `entropie`, `juna`, `kael`, `kern-welten`, `kohaerenz`, `moonshine-link`, `potentialmeer`, `risse`.

No chapter page.
`plot.md` cites it nowhere.
Conflicts with an entry from it: none; **opened: C16**. Questions: Q3, Q9.

## Sweep

`Alex` L196 occurrence — Alex Garland, the director of a film the report compares; `Kohärenz` L11 reading — L11 is the title (J9), but the report states two kinds of coherence, `Kohärenz durch Integration` and `Kohärenz durch Abgrenzung` (L40, L84), M's against AEGIS's — read by the sentence; `Moonshine-Link` L97 reading — the heading of the section on the Kael-Juna link (L97–L103), which says what the link is and does — the page's subject; `Realitätsebenen` L61 occurrence — a table cell naming the general question of levels of reality the simulation hypothesis raises; no statement about the page's levels; `Risse` L159 reading — AEGIS's system destabilised by the analysis of M, `Risse` in quotation marks with the User Query cited (L159) — the page's subject, read by the sentence; `Simulation` L61 occurrence — the simulation hypothesis as a lens for the Kernwelten (L61, L119); the report never speaks of the Überwelt.

## What the readers noticed and no record holds

**C16, opened.** In this scenario AEGIS analyses an external entity M through four simulated Kernwelten, and „Die Entität M und ihre menschliche Manifestation Kael stellen den Gegenpol zu AEGIS dar.“ ^[plotanalyse-kohaerenz-protokoll-szenario.md:L78]; Kael's DID is the result of AEGIS's fragmentation (L92). The wiki already held that origin from two documents of the same weeks (`kohaerenz-protokoll`, `m-als-fundament-der-simulation`), and the opposite — Kael as the remainder of AEGIS's own split self — from documents of 2026 read today and before. No record held the difference; `Wiki/conflicts/c16-kael-origin.md` now does, nine rows, deciding nothing, and the four pages it touches name it in their frontmatter, each its own commit.

The Kernwelten as AEGIS's labs for analysing M (L119) belong to the same origin and are recorded on `kern-welten`.
