---
document: kontext-outline
against: 106 pages, 16 conflicts
ran: "2026-10-05"
candidates: 87
decisions: 97
by_lookup: 69
judgements: 28
new_pages: 0
new_readings: 31
---

# Reconciliation 88 — `kontext-outline` against the wiki

`python3 scripts/reconcile.py kontext-outline`

87 candidates, 97 decisions — **69 by lookup, 28 to judgement**. Dated 2025-05-03 by the manifest: a briefing for a commissioned outline, in German with English field labels — a core-concept paragraph, a project context, a „Basis-Glossar (Zur Orientierung für den Autor)“ that tells the commissioned author to refine it (L24), and an outline of a prologue and Chapter 1–39 in three acts, each chapter with `Core Theme`, `Plot Summary`, `Kael Sys Focus`, `AEGIS Focus` and `Setting`. It leaves open points as question marks. A commission, not a canon.

Eighth of batch 2. Candidate list, census and note by a Sonnet `document-reader`; `rlm_ingest` not run. Readings by two Sonnet `wiki-reader`s in turn — 31 pages and 5 record entries — and chapter readings by two more, Kap 1–39 (`chapters.py missing` does not see English „Chapter N“); each its own commit naming the document.

## No new page

A commission briefing in the wiki's vocabulary plus its own scaffolding: its 43 new surfaces are the abbreviations of its glossary (KW, ANP, EP, Anteile), narrative craft (Drei-Akt-Struktur, Heroine's Journey, Hero's Journey, Panoptismus) and the thinkers it lists as philosophical hints (Hume, Kant, Hobbes, Sartre, Buber, Luhmann, Parfit). Its readings went onto 31 pages and 5 records; no name of the novel's world is defined here that the wiki lacks.

## Judgements

No new judgement. Every near match was decided by an existing rule (`Plan/runs/judgements.md`): J9 (a title or label containing a term: Paradox (AEGIS), Fehlausgerichtete Kohärenz, Kohärenz Protokoll), J12 and J16 (a compound or a qualified label is its own token: System Kael, Kael System, Host (Kael)), J49 (worlds named for Guardians: Logos-Prime, Mnemosyne-Archipel, Cerberus-Labyrinth, Kairos-Potentialis), J34 and J43 (a slash in a name the wiki has: Juna/V), J24 and J46 (a plural or inflection is no boundary: Guardians / Guardian, Fehlausgerichteten / Fehlausgerichtete Kohärenz, funktionaler Multiplizität, Riss / Risse), J69 (a match only after folding: Guardian / Integrity Guardian), J53 (a shared head noun is not a shared referent: Gödel against the Gödel-Gambit).

## Readings — 31 pages

`aegis`, `alex`, `argus`, `cerberus`, `emergenz`, `externe-ebene`, `genesis`, `grenzfeste`, `guardians`, `juna`, `kael`, `kairos`, `kiko`, `komponente-734`, `konstrukt-stadt`, `lex`, `lia`, `logos`, `mnemosyne`, `moros`, `multiplizitaet`, `nichts-rauschen`, `nyx`, `realitaetsebenen`, `resonanz-landschaft`, `rhys`, `risse`, `selene`, `sophia`, `tsdp`, `ueberwelt`.

Chapter pages: Kap 1, Kap 2, Kap 3, Kap 4, Kap 5, Kap 6, Kap 7, Kap 8, Kap 9, Kap 10, Kap 11, Kap 12, Kap 13, Kap 14, Kap 15, Kap 16, Kap 17, Kap 18, Kap 19, Kap 20, Kap 21, Kap 22, Kap 23, Kap 24, Kap 25, Kap 26, Kap 27, Kap 28, Kap 29, Kap 30, Kap 31, Kap 32, Kap 33, Kap 34, Kap 35, Kap 36, Kap 37, Kap 38, Kap 39.
`plot.md` cites it nowhere.
Conflicts with an entry from it: C6. Questions: Q3, Q5, Q7, Q8.

## Sweep

`Emergenz` L71 reading — read on emergenz; `Grenzfeste` L164 reading — Chapter 9's title, read on grenzfeste; `Kohärenz` L11 occurrence — the novel's title (J9); `Konstrukt-Stadt` L87 reading — Chapter 2's title, read on konstrukt-stadt; `Realitätsebene` L18 reading — read on realitaetsebenen; `Resonanz-Landschaft` L120 reading — Chapter 5's title, read on resonanz-landschaft.

## What the readers noticed and no record holds

**Five guardians over four worlds.** The glossary pairs LogOS, Mnemosyne, Cerberus and Kairos with KW1–KW4 and gives KW4 two guardians, Kairos and Sophia (L30–L33), then lists five (L50). Recorded on `guardians`, C6 and Q5.

**Alex as protector, Nyx a question.** The glossary calls Alex „Beschützer-Anteil“ (L40) and Nyx „Aggressiver/kämpferischer Anteil (?)“ (L43); the question mark is the briefing's own. Recorded on `alex` and `nyx`; the pages carry both readings side by side and no chapter turns on it, so no new question.
