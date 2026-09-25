---
document: kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md
against: 93 pages, 13 conflicts
ran: "2026-09-25"
candidates: 334
decisions: 343
by_lookup: 236
judgements: 107
new_pages: 0
new_readings: 38
---

# Reconciliation 18 — `kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md` against the wiki

`python3 scripts/reconcile.py kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md`

334 candidates after folding, 343 decisions — **236 by lookup, 107 to judgement**,
and one sweep hit. Document 17, „Anteile, Profile, Sprach-DNA" ^[kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md.md:L11] of 2026-06-10: the
thirteen Alters profiled field by field, the voices outside them, and the rules for
switching between them. It names its source, „Charakter-Bibel 2026-05-08
(autoritativ)" ^[kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md.md:L13] — recorded, not applied (decision 006). The first document read under the list rule of
decision 012.

Chosen because the drafting manual sends its reader here for the Alex conflict and the
exact roster of the thirteen Alters.

## No new pages

Every figure it profiles has a page. What else it lists is profile fields, the borrowed
physics each Alter is mapped to (recorded as a reading on that Alter's page), the log
format, and fifteen names it names only to exclude them. `reconcile.json` lists each
under `not_promoted`.

## Readings — 38 pages

32 the lookup reached; `ueberwelt` (`Simulation`, J39) and `kohaerenz` (a log field)
were looked up and not read. Six more by recorded rules: `kaels-wohneinheit` (J58),
`externe-ebene` (J54), `kern-welten` (J37), `genesis`, `atemporalitaet` (J85) and
`hitze-polaritaetsregel` (J83, the Polaritäts-Lock). The sweep found one page the
census missed as a surface, `risse` at L890, and it is a reading.

## What moved

- **C11** — heat placed three ways in one document: as Juna's Coheron-Spur (L1042);
  Silas' warmth as „die einzige diegetische Wärme im KP außerhalb des
  Vortex-Beat-4-Heat-Spike" ^[kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md.md:L703], under the same lock; and Landauer heat
  from the Silas–Oblivion conflict, „entsteht Landauer-Hitze." ^[kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md.md:L837] The document
  does not relate them.
- **C6, Q5** — two Guardians; „Die alten Cerberus-/LogOS-/Kairos-Funktionen sind hier
  absorbiert." ^[kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md.md:L1016] Sophia is not named. The author's five stand.
- **C12** — four beats, cited to the Kompendium, and the Alex conflict from the
  profile's side (L219, L1079).
- **C7** — Kap 38, as a mode locked on 2026-05-30. **C10** — Kap 0 only, in Kael's profile.
- **C4** — AEGIS cannot grasp Silas and knows nothing of Oblivion; Argus alone names its
  flaw.
- **Q1, Q3, Q4** — Mnemosyne works for AEGIS, inside its system; thirteen Alters, none
  bound to a world; Selene is a „Starre Wächterin" ^[kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md.md:L361].

Read and unchanged: C1, C2, C3, C5, C8, C9, C13, Q2 — `reconcile.json` says why each.
C13 was recorded on main while this document was being read. It gets no entry here:
the document names `Basisrealität Köln` and takes no side on whether it lies beyond
the simulation.

## Judgements

J85 (`Atemporal` is the Atemporalität page's property, as an adjective) and J86 (`Juna ↔
AEGIS` states a relation; an arrow is not an alias, unlike the slash of J34 and J43). The
other near matches were decided by recorded rules, named in `reconcile.json`. Neither
matching rule makes a false merge on the 73 labelled pairs; the fold baseline stays at 58 %.
