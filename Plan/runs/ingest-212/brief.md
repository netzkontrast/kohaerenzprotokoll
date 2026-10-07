# Brief — readings from document 212 (step 6)

1 document, one reader, one batch: `ingest-212`. Files go to `Plan/runs/ingest-212/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 212 | `charaktermodellierung-mit-aieos-schema` | 2026-02-28 | „the AIEOS evaluation“ (an unsigned evaluation report) | a German evaluation of the AIEOS character schema v1.2.0 against the novel's characters: five of Kael's eleven parts mapped as case studies, the schema strong on isolated traits and weak on relations and non-human entities, four extensions proposed — what it says of the novel it reports from its references; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (222 lines for `charaktermodellierung-mit-aieo`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An evaluation that reports the novel from its sources: write „the AIEOS evaluation describes, citing its sources, …“ and keep the schema's vocabulary (`neural_matrix`, `triggers`, `dominance_score`) as the report's own. German — quote as written; cut before glued footnote digits (`konstituiert wird.2`) and inner straight quotes; the export dropped the kernel symbols (`Kohärenz-Kernel ()`, L17) — never quote across them; schema field names carry escaped underscores (`neural\_matrix`).

## Pages — document 212, `charaktermodellierung-mit-aieos-schema`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L19, L27, L33, L59, L71, … (19 lines). central (2–5): the AI AEGIS, whose aim is absolute coherence and the elimination of the Nichts Rauschen, operating „paradoxerweise auf Basis einer extremen Korrespondenztheorie der Wahrheit“ (L27) — a reversal of the other documents' attribution, record it; the paradox of modelling AEGIS (L71) — read the section; AEGIS losing control in the third act (L178).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L69, L190. minor (1–3): the protection front of Nyx and Alex, existing in relation to Kiko and Lia (L69); a switch from host Kael to the protector Alex (L190).
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L57, L192. minor (1–3): Kael suffering „unter dem“ Cache Kohärenz problem, a massive inconsistency of his memories and beliefs (L57) — cut before the inner quotes.
- **`chaitin-konstante`** (minor, 1–4): the census's surfaces — `Chaitin-Konstante` L35, L193. minor (1–3): the algorithmic uncomputability of the Chaitin-Konstante, „welche durch die Anomalie“ Juna personified (L35) — quote around the bold.
- **`dkt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Dual-Kernel-Theorie (DKT)` alone on L17. minor (1–3): the Protokoll operating on the Dual-Kernel-Theorie, reality as the interaction of an ordering and an entropic kernel (L17) — never across the dropped symbols.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L83. minor (1–3): Moros as the approach to the thermodynamic zero point, maximal entropy and standstill (L83); Lex's irrational fears „Entropie“ and Juna (L104) — read the table row.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Externe Ebene` alone on L176. minor (1–3): the third act's meta-narrative: the Externe Ebene as „der Realität des Autors/Lesers im Köln des Jahres 2026“ (L178) — read the line; the section heading (L176); Kael overwriting into the reality of Köln 2026 (L180).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L53. minor (1–3): the sexualized fight/attachment reaction of the EP Isabelle compensating powerlessness by control (L53).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L35, L104, L122, L193. minor (1–3): the Chaitin-Konstante personified by the anomaly Juna (L35); Juna as absolute entropy and the Kollaps-Kernel for Lex (L104) — read the table row; Kiko needing the resonance Juna or Rhys offer (L122).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L29, L33, L39, L47, L51, … (20 lines). central (2–5): the protagonist Kael „ist keine singuläre“ — read L17; Kael learning methodological coherentism, his healing and the final existential fusion in chapter 38 (L29); the eleven parts of System Kael (L39, L69); Kael overwriting into Köln 2026 (L180).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L69, L108, L110, L122, L124, L128, … (9 lines). minor (1–3): Kiko and Lia as the vulnerable parts the protection front exists for (L69); the case study `Kiko (Kind / Angst / Freeze EP)` (L108); Kiko needing Juna's or Rhys's resonance (L122).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. occurrence: the Protokoll's name (L15); the AI's aim of absolute coherence is read on aegis (L27).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L17, L180. minor (1–3): an ordering Kohärenz-Kernel against an entropic Kollaps-Kernel (L17) — never across the dropped symbols; read L180.
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L17, L104, L199. minor (1–3): the entropic Kollaps-Kernel (L17); Juna as the Kollaps-Kernel for Lex (L104); the Nichts Rauschen named as Kollaps-Kernel (L199) — cut before the inner quotes.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L33, L51, L106, L169, L178. minor (1–3): „Die Architektur der Konstrukt-Stadt ist keine bloße Kulisse“, with undecidable zones after Gödel (L33); the city's world defined by Wittgenstein's limit (L51); the boundaries between Konstrukt-Stadt, Überwelt and the external level blurring (L178).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L35, L89, L91, L104, L106, L191, … (7 lines). minor (1–3): the case study `Lex (Der Rationale ANP)`: the analyst and strategist, finding false safety in AEGIS's order (L91); his logic meeting the halting problem (L35); his values collapsing in the Konstrukt-Stadt (L106).
- **`lia`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Lia` alone on L69. minor (1–3): Kiko and Lia as the vulnerable parts (L69).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L59. minor (1–3): „Der Guardian“ Mnemosyne manages the data streams of memory (L59) — read the line.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L79, L81, L83. minor (1–3): the Moros paradox: Moros as the ultimate collapse, the deepest trauma reaction (L81); Moros as Sartre's Nichts and the thermodynamic zero point (L83).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L145. minor (1–3): Selene striving for the „funktionalen Multiplizität“ of the whole system (L145) — cut before the inner quotes.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L69, L126, L128, L141. minor (1–3): the case study `Nyx (Der Kämpfer EP)` (L126); Nyx and Alex as protection front (L69); the schema cannot bind Nyx's triggers to Kiko's state (L141).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L122. minor (1–3): Kiko needing the resonance „der pflegende Anteil Rhys“ offers (L122).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L87. minor (1–3): read L87 — „die architektonischen Risse in der AIEOS-Struktur“ — decide: the schema's cracks are an occurrence unless the line means the world's Risse.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L143, L145, L152, L158. minor (1–3): Selene as Inner Self Helper, operating under AEGIS's radar, the core self (L145) — cut before the inner quotes; a holistic, integrative principle (L152); a meta-cognitive instance above the system (L158).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L17, L87, L186. minor (1–3): the depth-psychological concepts of the TSDP operationalised in the case studies (L87); the TSDP structure of System Kael (L186).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L178. minor (1–3): the boundaries between the Konstrukt-Stadt, „der Überwelt“ and the external level blurring in the third act (L178).

- **`nichts-rauschen`** (minor, 1–2): AEGIS's aim, the elimination of the „Nichts Rauschens“ (L27); the Nichts Rauschen as the Kollaps-Kernel (L199) — quote around the inner quotes.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `dkt`: `Dual-Kernel-Theorie` (near `dualkerneltheoriedkt`). read on dkt (L17).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Paradoxon der Fehlausgerichteten Kohärenz` (near `koharenz`). occurrences: the Protokoll's name; the Paradoxon der Fehlausgerichteten Kohärenz is AEGIS's, read on aegis if the line is read.
- `multiplizitaet`: `funktionalen Multiplizität` (near `multiplizitat`). read on multiplizitaet (L145).
- `nichts-rauschen`: `Nichts Rauschens` (near `nichtsrauschen`). a reading — see the extra page below.


**Record entries** (one file each):

- **`c13-externe-ebene-beyond-the-simulation`**: the external level as the reality of the author and reader in Köln 2026, where Kael overwrites (L176, L178, L180).
- **`q3-how-many-kern-welten-and-alters`**: the eleven parts of System Kael (L39, L69, L197); five mapped as case studies.
- **`q5-guardians-and-kern-welten`**: „Der Guardian“ Mnemosyne managing the data streams of memory (L59).

**Not promoted:** the AIEOS schema and its fields, the four extensions (SystemDynamics and others), the borrowed theories (Gödel, Turing, Chaitin beyond its page, Wittgenstein, Page-Wootters, Sartre, Bertalanffy), Köln 2026 (on externe-ebene).

**Two readers**, disjoint: (1) kael, lex, kiko, nyx, alex, lia, rhys, isabelle, moros, selene, tsdp, multiplizitaet, juna and the record q3; (2) aegis, konstrukt-stadt, ueberwelt, externe-ebene, kohaerenz-kernel, kollaps-kernel, nichts-rauschen, dkt, entropie, risse, cache-kohaerenz, chaitin-konstante, mnemosyne and the records c13, q5.

**Chapter reading**: one, Kap 38, by the session (`Plan/runs/ingest-212-kap/`).
