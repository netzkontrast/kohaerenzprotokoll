---
document: 2-kohaerenz-protokoll-konzeptentwicklung
against: 106 pages, 16 conflicts
ran: "2026-10-05"
candidates: 89
decisions: 99
by_lookup: 62
judgements: 37
new_pages: 0
new_readings: 29
---

# Reconciliation 97 — `2-kohaerenz-protokoll-konzeptentwicklung` against the wiki

`python3 scripts/reconcile.py 2-kohaerenz-protokoll-konzeptentwicklung`

89 candidates, 99 decisions — **62 by lookup, 37 to judgement**. Dated 2025-05-03 by the manifest: a German concept plan, `Gesamtkonzept: Kohärenz Protokoll`, written in the role `Konzept-Entwickler & Narrativer Stratege` — premise, four thematic fields, three core themes, the central question and the subplots (Teil 1), then one block per chapter from Chapter P to Chapter 39 in four fields (Teil 2), and a reference list. It claims no canon; its chapter blocks hedge throughout.

## No new page

A concept plan whose 39 new surfaces are its method and borrowed concepts — TSDP's vocabulary (ANP, EP, Phobien, Ko-Bewusstsein, Realisation, Synthese), the paradoxes it cites (Paradox of Control, Paradox der Toleranz, AI Alignment Paradox), genre tropes (Unreliable Narrator, Threshold Guardian, Cosmic Horror) and its own labels (Kernparadoxon, Ursprungsparadoxon, Beschützer-Anteil, Fürsorger-Anteil, Meta-Beobachter); everything it names in the novel's world already has a page.

## Judgements

No new judgement. Every near match was decided by an existing rule (`Plan/runs/judgements.md`): J9 (the title: Kohärenz), J12 and J16 (a compound with its own sense is its own token: Fehlausgerichtete Kohärenz and its inflections — AEGIS's paradox, read on aegis — AEGIS-Paradoxon, System Kael, Kael-Hosts, Guardian LogOS, Guardian Mnemosyne, Guardian Cerberus, Konstrukt-Welten (KWs), Kybernetik zweiter Ordnung), J34 (a slash form is the name: Juna/V), J49 (a world named for its Guardian: Logos-Prime, Mnemosyne-Archipel, Cerberus-Labyrinth, Kairos-Potentialis), J56 and J23 (plurals and inflections: Risse/Riss, AEGIS-Paradoxons, AI Alignment Paradoxes, funktionaler Multiplizität), J100–J102 (English placed by the sentence: Glitches and Glitch in the Matrix on risse); `Echo` is the original whole of Chapter P, not the residual echoes; `Simulation Hypothesis` a borrowed concept, not the Überwelt.

## Readings — 29 pages

`aegis`, `alex`, `argus`, `cerberus`, `emergenz`, `entropie`, `externe-ebene`, `genesis`, `grenzfeste`, `guardians`, `juna`, `kael`, `kairos`, `kiko`, `lex`, `lia`, `logos`, `mnemosyne`, `moros`, `multiplizitaet`, `nichts-rauschen`, `nyx`, `realitaetsebenen`, `rhys`, `risse`, `selene`, `sophia`, `tsdp`, `ueberwelt`.

Chapter pages: Kap 0, Kap 1, Kap 2, Kap 3, Kap 4, Kap 5, Kap 6, Kap 7, Kap 8, Kap 9, Kap 10, Kap 11, Kap 12, Kap 13, Kap 14, Kap 15, Kap 16, Kap 17, Kap 18, Kap 19, Kap 20, Kap 21, Kap 22, Kap 23, Kap 24, Kap 25, Kap 26, Kap 27, Kap 28, Kap 29, Kap 30, Kap 31, Kap 32, Kap 33, Kap 34, Kap 35, Kap 36, Kap 37, Kap 38, Kap 39.
`plot.md` cites it nowhere.
Conflicts with an entry from it: C3, C7, C14, C16. Questions: Q1, Q3, Q5, Q8.

## Sweep

`DID` L56 occurrence — only in Chapter 1's keyword line, `Passive Influence DID/OSDD`; the block says nothing more; `Entropie` L181 reading — Juna/V as a source of potential entropy or new order; read on entropie; `Externe Ebene` L314 reading — one of three guesses at the new reality in Chapter 38, with a question mark; read on externe-ebene; `Genesis` L44 reading — Chapter P is titled [Genesis], AEGIS's emergence from chaos and fear; read on genesis; `Grenzfeste` L107 reading — Chapter 9's title „Die Mauern der Grenzfeste“ beside KW3 `Cerberus-Labyrinth`; read on grenzfeste; `Juna` L9 reading — `Juna/V`, the mysterious external connection of the premise; read on juna; `Kohärenz` L1 occurrence — the novel's title (J9); `Multiplizität` L15 reading — the potential multiplicity of consciousness; read on multiplizitaet with L312, L319; `Realitätsebene` L9 reading — the search for an ultimate level of reality, glossed as the Fundament; read on realitaetsebenen.

## New conflict — C17, Kael's gender

The plan writes System Kael as „einer Protagonistin“ ^[2-kohaerenz-protokoll-konzeptentwicklung.md:L9] and as `sie` through its chapter blocks. Three outlines of the same day, read as documents 88, 91 and 92, do the same, and their gender had been recorded nowhere; before them and after them Kael is male, and the codex of 2025-11-03 (document 96) resolves *Protagonist Identity* as the male host. Under the stop rule of the ingest goal the session stopped and asked; the author chose a new record (2026-10-05). [[c17-kael-gender|C17]] holds six sources and decides nothing; whether the author's figure card may stand as its resolution is in `Plan/questions-for-the-author.md`.

## What the readers noticed and no record holds

**The census's title.** `quotes.py --strict` counts the quotation marks in the document's own title, which `census.py draft` writes into the census's frontmatter and heading, as two uncited quotations; the plain `quotes.py` that CI runs passes. Document 91 shows the same. A tool limit, not a reading.
