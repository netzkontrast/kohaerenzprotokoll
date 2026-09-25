---
document: kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md
against: 93 pages, 12 conflicts
ran: "2026-09-25"
candidates: 539
decisions: 595
by_lookup: 346
judgements: 249
new_pages: 0
new_readings: 53
---

# Reconciliation 17 — `kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md` against the wiki

`python3 scripts/reconcile.py kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md`

539 candidates after folding, 595 decisions — **346 by lookup, 249 to judgement.**
Document 16, „Welt, Sensorik, Drafting-Disziplin" ^[kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md:L11] of 2026-06-10, calls itself the
„Viertes Dokument im Repo-Quartett." ^[kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md:L13] It is a drafting manual: a world bible per
level, sensory lookups, Riss types, foreshadowing strands, a reveal timeline, hard
rules and a master index of locks with their dates and sources. It claims
„Canon-Dateien sind Source-of-Truth." ^[kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md:L1410] — recorded, not applied (decision 006).

Chosen because it spoke to more open records than any other unread canon-era
document: 14 lines with `Ozon` (C11), 6 with `Knöchel` (C10), 13 with `734` (C12)
(`grep -c`, substrings, orientation only).

## No new pages

Most of its 542 candidates are its own method — templates, checks, genre modes,
lock labels, a repository layout it calls „Vorschlag, kein Lock. User-Entscheidung."
^[kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md:L1245] Its world vocabulary lands on pages that exist. What it names without a page is a
one-row sub-location, a narrative device (five strands, five Genesis motifs, the
anchors), a lock restated from another document, or a name the wiki has declined
before (J47/J73, J59). `reconcile.json` lists each under `not_promoted` with its
lines.

## Readings — 53 pages

44 pages the lookup reached, and nine by existing rules: `kaels-wohneinheit` (J50),
`datenverarbeitungsknoten-7g` (J65), `logos`, `kairos`, `cerberus` (J49), `sophia`,
`kern-welten`, `moonshine-link`, `alters` (J84). Every citation names this document
and was located by `read.py`'s own comparison, not typed.

Not given a reading: `rhys` and `selene` occur only in a template's question,
„Rhys↔Selene?" ^[kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md:L951]; `kohaerenz` only as the name of a protocol (J57); `michael`
is a surface of `kael`, whose reading carries the lock row `Kein Michael` (L1188).

## What moved

- **C6** — two Guardians, „Mnemosyne + Erasure-Pol (frühere fünf sind
  dekanonisiert)" ^[kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md:L1183]. The author's decision for five stands; the entry records a
  source of 2026-06-10 for the other side.
- **Q5** — the pairing retired by name: „KW1=LogOS, KW4=Kairos/Sophia" ^[kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md:L42],
  „Beides ist dekanonisiert" ^[kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md:L42].
- **C11** — the cold-ozone lock, restated three times with its date. And a tension
  inside the document: foreshadowing strand 1 is named `Landauer` with the theme
  „Hitze als Symptom der Wahrheitsvertuschung" ^[kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md:L445], accumulating in Kap 6. J81 keeps
  the strand and the signature apart; whether the strand's heat is the lock's cold is
  C11's question, asked by one document of itself.
- **C10** — Kap 0 alone, four times, dated to the Kompendium's lock of 2026-05-31.
- **C12** — a Genesis-4-Beat restated without Komponente 734 as a beat, and a
  Genesis conflict the document names itself: Alex before the separation or in it
  (L1456–L1466).
- **C7** — Kap 33 an effect („Setting der Juna-Wirkung (Kap 33)" ^[kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md:L327]), Kap 38 an
  appearance („Juna erscheint direkt" ^[kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md:L593]).
- **C5** — both scales again: a name of KW4 and a place inside it.
- **C4, C9, Q1–Q4** — AEGIS' blindness; KW1 as decided; the Guardians inside
  AEGIS' Überwelt without the word *component*; three protocols, none of Q2's eight;
  thirteen Alters and four worlds as act markers; `Wächter` only in compounds.
- **KW3 has chapters here** — „Späte Akt II (Kap 23–28)." ^[kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md:L175] — the gap `NOW.md`
  recorded for the strukturierter Outline is that document's, not the plan's.
- **Mosaik-Herz** — only the Kap-34 place; no Kap-11 beat.

Read and unchanged: C1 (no expansion), C2 (no `Entropie`), C3 (no origin stated),
C8 (deferred to the storyform document, L1164).

## Judgements

J80 (`Einheit 734` placed under the dwelling once and as Komponente 734 twice —
left open), J81 (a strand named after Landauer is not the Landauer-Signatur), J82
and J84 (a leading numeral counting a term is a reading on it), J83 (`Polaritätsregel`
is the Hitze-Polaritätsregel's short form, by content). The other near matches were
decided by recorded rules; `reconcile.json` names them.
