---
document: kohaerenz-protokoll-hard-sf-horror-thriller
against: 106 pages, 15 conflicts
ran: "2026-10-05"
candidates: 294
decisions: 307
by_lookup: 200
judgements: 107
new_pages: 0
new_readings: 31
---

# Reconciliation 61 — `kohaerenz-protokoll-hard-sf-horror-thriller` against the wiki

`python3 scripts/reconcile.py kohaerenz-protokoll-hard-sf-horror-thriller`

294 candidates, 307 decisions — **200 by lookup, 107 to judgement**. Dated 2026-03-29 by the manifest: a German „Konzeptdokument und Ontologischer Pitch“ ^[kohaerenz-protokoll-hard-sf-horror-thriller.md:L11] for the novel as a hybrid of Hard-SF, Cosmic Horror and Psycho-Thriller, written in the present tense as a finished design, with nine references. It says of itself that it „dient dem Autor als unverrückbare Referenz“ ^[kohaerenz-protokoll-hard-sf-horror-thriller.md:L19] and calls the project „ein literarischer, transdisziplinärer Formalbeweis“ ^[kohaerenz-protokoll-hard-sf-horror-thriller.md:L165] — claims recorded, never applied (decision 006).

The second document of the author's go of 2026-10-05 and of step 6's sample. Census and note by a Sonnet `document-reader` from the R5 setup; the session read ten of the note's claims against their lines (L19, L41, L47, L105, L109, L123, L125, L129, L153, L161) and all held. Its 33 readings were written by one Sonnet `wiki-reader` from `Plan/runs/ingest-61/brief.md`, placed by `readings.py apply` with every check held, each page its own commit naming the document.

## No new page

A pitch that names the novel's design in the vocabulary the wiki already pages — DKT, the two kernels, Gödel-Gambit, System Kael and six parts, the four Kernwelten, AEGIS, Juna, the Moonshine-Link, Mosaik-Herz, Algorithmische Melancholie. What has no page is borrowed theory (Landauer, Bekenstein, Hawking, replica wormholes, Jaspers, Heidegger, Erikson, Frankl, IFS, Dramatica's throughlines) or the pitch's own one-off labels (Sensory Rulebook, Frakturierte Untersuchung, Lure Pattern, Specification Gaming, ineffiziente Schönheit); none is defined twice or used by a second read source, so none opens a page.

## Judgements

J121, new: `Isabella` / `Isabelle` — a name differing by one letter, given to a part of Kael's system, is placed on the page by the sentence when the system and the function agree; one source's spelling is no surface, and a different role is a reading (J51, J100, J119). The pitch puts her among the ANPs as a „Daten-Spezialistin“ ^[kohaerenz-protokoll-hard-sf-horror-thriller.md:L84]; the page's other sources make her an EP. `Isabella` stands in 12 landed documents, `Isabelle` in 104 (`corpus.py count`).

Every other near match was decided by an existing rule (`Plan/runs/judgements.md`): J9 (a title containing a term: Kohärenz Protokoll, Konzeptdokument und Ontologischer Pitch), J12 and J16 (a compound is its own token: AEGIS-Architektur, AEGIS-Manifest, Zero-Trust-Umgebung), J17 (a quoted work title names the work: `Kohärenz Protokoll` in quotation marks), J19 and J97 (an article or case ending is no boundary: Kaels, funktionalen Multiplizität), J24 and J46 (a plural is no boundary: ANPs, EPs, Verschränkungsinseln), J28 and J32 (a compound is placed by what it names: Paradox der fehlausgerichteten Kohärenz, Kohärenztheorie der Wahrheit, Datenkorruption (Entropie)), J49 (a world name built from a bearer's name is not the bearer: Logos-Prime, Mnemosyne-Archipel, Cerberus-Labyrinth, Kairos-Potentialis), J60 (an acronym and its expansion: AEGIS / Autonomous Entropic Gatekeeper for Integrity Systems, DKT, TSDP), J69 (a match only after folding: Depersonalisation / personas, Hitze / hitze-polaritaetsregel), J72 (a parenthetical index is part of the label: Kael (Host), Kiko (Exile/Vulnerability), Emergenz durch Negation (Axiom 4)), J88 (a common noun for a page's referent is placed by the sentence: Simulation, Kernel, Glitch), J113 (a slash joining a name to a role names the figure: Juna/V), J118 (a world named by a Guardian-built name and a KW number is read on the paged world of that number).

## Readings — 31 pages

`aegis`, `algorithmische-melancholie`, `alters`, `dkt`, `emergenz`, `entropie`, `genesis`, `goedel-gambit`, `grenzfeste`, `guardians`, `isabelle`, `juna`, `kael`, `kern-welten`, `kiko`, `kohaerenz-kernel`, `kohaerenz`, `kollaps-kernel`, `konstrukt-stadt`, `lex`, `moeglichkeits-garten`, `moonshine-link`, `moros`, `mosaik-herz`, `multiplizitaet`, `nichts-rauschen`, `nyx`, `resonanz-landschaft`, `risse`, `tsdp`, `ueberwelt`.

No chapter page.
`plot.md` cites it nowhere.
Conflicts with an entry from it: none. Questions: Q3, Q9.

## Sweep

`Emergenz` L29 reading — the Kollaps-Kernel as the precondition of consciousness and evolutionary emergence (L29), with the manifesto's Emergenz durch Negation (L112) — the pitch's position on where emergence comes from; `Kohärenz` L11 reading — L11 is the title (J9, an occurrence), but the pitch states what coherence is in its sentences — embodied (L91), the Paradox der fehlausgerichteten Kohärenz (L115), reached only by addition (L169); read by the sentence.

## What the readers noticed and no record holds

**Isabella, ANP or EP.** The spelling is one source's; the camp is a reading that differs from the rest of the `isabelle` page and is recorded there and put to the author (`Plan/questions-for-the-author.md`), not made a conflict record from one source.

**Six named parts in two camps, no total** — Kael, Lex, Isabella as ANPs; Nyx, Kiko, Moros as EPs (L84–L85): the Q3 entry holds it.

**AEGIS's origin.** The pitch has AEGIS crystallise „aus demselben gespaltenen Ursprungs-Selbst wie Kael“ ^[kohaerenz-protokoll-hard-sf-horror-thriller.md:L105] in the Genesis-Krise; C3 already holds that position, so no entry. **Juna** is „das exilierte Ursprungs-Ich von Kael“ ^[kohaerenz-protokoll-hard-sf-horror-thriller.md:L123], the IC of the Dramatica quad, with AEGIS the Subjective Story (L146–L147) — on the pages; C8 asks about AEGIS's Approach, which the pitch does not give.

C2: the pitch's entropy is thermodynamic and informational, tied to the Kollaps-Kernel, which C2 already holds as a sense — no entry. C6, C14: nothing.
