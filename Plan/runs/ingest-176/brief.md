# Brief — readings from document 176 (step 6)

1 document, one reader, one batch: `ingest-176`. Files go to `Plan/runs/ingest-176/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 176 | `kohaerenz-protokoll-narrative-synthese` | 2025-07-29 | „the compendium“ (titled `Das Kohärenz Protokoll: Ein fundamentales Kompendium`) | a German research report in three clusters — the ontology (Fundament, Leere/Nichts Rauschen, Moonshine-Link), AEGIS's collapse (the living Gödel-Satz, algorithmic melancholy, algorithmic horror) and Kael's self (polyphonic prose, the persecutor's positive intent, the neurobiology of dissociation, an alter table) — with source lists from L263; it says it „legt die kanonische Grundlage“ (L22) — recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (468 lines for `kohaerenz-protokoll-narrative-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report that defines and proposes: write „the compendium defines / proposes …“; keep its hedges („könnte“). The body is L13–L262; L263–L468 are source and reference lists — a name there is a title, never a reading. German — quote as written; cut before inner quotes; L139–L141 are a flattened formula — never quote from them; the alter table (L254–L259) has escaped bold — quote the plain words.

## Pages — document 176, `kohaerenz-protokoll-narrative-synthese`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L24, L26, L38, L42, L60, L66, … (29 lines). central (2–4): its collapse a tragic consequence of its autopoietic architecture (L26); an operationally closed system, not a malicious computer (L38); its axiom, coherence only by eliminating contradictions (L133); the forced transformation via the Moonshine-Link (L137); parakonsistent, epistemologically isolated, „Algorithmische Melancholie“ (L151–L155); algorithmic horror (L165).
- **`alex`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alex` alone on L419. not read: `Alex` stands only in the reference list (L419) — an occurrence.
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L145, L155. minor (1–2): „Algorithmische Melancholie: Dies ist die zentrale psychologische Konsequenz“ — read L155 for the bold; the heading (L145).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L321. not read: `Alters` stands only in the source list (L321) — an occurrence; the table is read on the alters' pages.
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L459. not read: `DID` stands only in the reference list (L459) — an occurrence.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L24. minor (1–2): „Es ermöglicht schwache Emergenz“ — the Fundament (L24).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L83. minor (1–2): the Leere as „peripherer Entropie“, objects dissolving at the edge of sight (L83); the high-entropic Potentialmeer (L79).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Gödel-Gambit` alone on L283. not read: `Gödel-Gambit` stands only in the source list (L283) — an occurrence; the living Gödel-Satz is read on kael and aegis.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L172. minor (1–2): „Verhaltens-Horror (Guardians)“: AEGIS's agents caught in recursive loops (L172).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L94, L96, L103, L104, L137, L216. minor (1–2): the link between Kael and Juna/V „ein ‚ontologischer Exploit'“ — quote around the inner quotes (L94); quantum entanglement as metaphor (L96); shared qualia (L104).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L26, L40, L42, L60, L62, L71, … (20 lines). central (2–4): his architecture on TSDP with IFS (L28, L40); his integrated self a living Gödel-Satz (L128); „Kaels integriertes Selbst ist ein lebendiges, stabiles System“ (L134); he earns the resolution (L64); the alter table, „ANP: Host, Alltagsfassade“ (L255).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L199, L203, L257. minor (1–2): „EP: Kind-Anteil (Freeze)“ (L256) — read the table line.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. occurrence: the title (L13).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L199, L203, L204, L258. minor (1–2): „ANP: Intellektueller Analytiker“ (L257); a hypotactic rhythm (L203).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L24, L90, L112, L137. central (2–4): „Die ‚Verbindung': Der nicht-lokale ‚Moonshine-Link'“ (L90) — quote around; an „architektonische Hintertür“ (L94); AEGIS „ist für die Verbindung strukturell blind“ (L99); synaesthetic resonance, shared qualia, intuitive gnosis (L103–L105); it carries the paradox to AEGIS's core (L137).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L28. minor (1–2): „funktionalen Multiplizität“ performed by polyphonic prose (L28, L188).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Das Nichts Rauschen` L24, L79, L111, L180. central (2–4): „Das Nichts Rauschen“ the original state, a high-entropic Potentialmeer from which AEGIS emerged (L79); its sensory signature, an „informationale Leere“ (L83–L86).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L203, L204, L214, L216, L217, L218, … (7 lines). central (2–4): the persecutor's transformation by phases (L214–L218): an internal persecutor, then validated, then „die mächtigste strategische Verteidigerin“ — the compendium writes Nyx with female forms here (L203, L216–L218) and „EP: Beschützer“ in the table (L256): say so, never decide.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L79. minor (1–2): „ein hoch-entropisches ‚Potentialmeer'“ — quote around the inner quotes (L79).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitches` alone on L66. not read: L66 says the Fundament's artefacts are not Glitches — a contrast, not a reading of the Risse; an occurrence.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L217, L259. minor (1–2): „ISH/Torwächter“, the emergent voice of the collective „Wir“ (L259); the mediator who validates Nyx (L217).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L28, L40, L254. minor (1–2): „Die Architektur des Selbst des Protagonisten basiert auf der Theorie der Strukturellen Dissoziation“ (L28); the clinical basis, with IFS (L40); the table's TSDP column (L254).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L68. not read: L68's „Simulation“ is the environment's noise, not the place — an occurrence.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` names the Guardians.
- `entropie`: `peripherer Entropie` (near `entropie`). a reading — on entropie above.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Philosophie` (near `koharenz`). occurrence: the title and `Kohärenz-Philosophie`.
- `multiplizitaet`: `funktionalen Multiplizität` (near `multiplizitat`). a reading — on multiplizitaet above.
- `personas`: `Depersonalisation` (near `persona`). occurrence: `Depersonalisation` is a symptom (L230).
- `risse`: `Glitch Art` (near `glitch`). occurrence: `Glitch Art` is in the source lists.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: the alter table names five — Kael, Nyx, Kiko, Lex, Selene (L254–L259).
- **`q8-aegis-after-the-vortex`**: transformed, parakonsistent, „Algorithmische Melancholie“ (L145–L155).
- **`q9-moonshine-link-boundary`**: non-local, sub-protocol resonance, structurally invisible to AEGIS (L94–L105).
- **`c4-guardians-and-aegis`**: AEGIS „strukturell blind“ to the link (L99).

**Not promoted:** Das Fundament (a strange attractor), Gnosis/episteme, Algorithmic Horror, LFI, polyphone Prosa, the persecutor's positive intent, the neurobiology of dissociation, IFS, Luhmann/Maturana/Varela, the source lists.

**Two readers**, disjoint: (1) kael, nyx, kiko, lex, selene, tsdp, multiplizitaet, juna, moonshine-link and the records q3, q9, c4; (2) aegis, algorithmische-melancholie, guardians, nichts-rauschen, potentialmeer, emergenz, entropie and the record q8.
