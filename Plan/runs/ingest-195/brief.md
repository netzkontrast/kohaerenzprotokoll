# Brief — readings from document 195 (step 6)

1 document, one reader, one batch: `ingest-195`. Files go to `Plan/runs/ingest-195/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 195 | `kohaerenz-protokoll-aktuelle-gesamtkonzept-synthese` | 2025-04-26 | „the concept synthesis“ (titled `Kohärenz Protokoll: Aktuelle Gesamtkonzept-Synthese (Abstrakt)`) | a German abstract in six sections of numbered statements — ontology (Potentialmeer, AEGIS), system architecture (Überwelt, protocols, five Guardians), the M-structure and the Kael-Juna connection, Kael with DID and IFS, the core conflict and themes, and the narrative — most ending in an italic `Quellen:` list of other documents' titles; it calls itself „den aktuellen, kohärenten Stand“ (L55), recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (56 lines for `kohaerenz-protokoll-aktuelle-g`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A synthesis that names its sources: write „the concept synthesis defines / summarises …“; a statement's `Quellen:` list names the documents it draws on — mention it where it matters, never treat it as this document's evidence. German — quote as written; cut before inner straight quotes and before the italic `*(Quellen:`; digits glued to words drop in `--find` (KW1, v1.4) — quote around them.

## Pages — document 195, `kohaerenz-protokoll-aktuelle-gesamtkonzept-synthese`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L16, L18, L22, L23, L24, … (16 lines). central (2–4): „AEGIS (Autogenic Emergent General Intelligence System):“ — read L16: emerged by autopoiesis from the Potentialmeer, existence by negation and demarcation, its aim maximal systemic coherence by OBP, PMAS, RIVE; adaptive, perhaps paraconsistent, but without real semantic understanding; its protocols' weaknesses — Gödel, Landauer (L23); the core conflict, coherence by demarcation against M/K-J coherence by integration (L43).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L38. minor (1–2): Kael's „Alters“ as IFS parts with protective functions organised round a core self (L38) — quote around the inner quotes.
- **`ani`** (minor, 1–4): the census's surfaces — `ANI` L16. minor (1–2): `ANI` named with `ZTV` as AEGIS's philosophy of trustlessness (L16) — the abstract does not expand it.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L24. minor (1–2): named among the five Guardians (L24).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L37. minor (1–2): Kael's DID „ist keine inhärente Eigenschaft“ but a direct consequence of AEGIS's analytic trauma (L37) — read the line.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L15. minor (1–2): the Potentialmeer as „die Quelle emergenter Strukturen“ (L15); the systems AEGIS manages as complex adaptive systems tending to emergent behaviour (L25).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L16. minor (1–2): AEGIS's coherence defined as „geringe informationelle Entropie“ (L16) — read L16.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L24. central (2–4): „Spezialisierte AEGIS-Agenten“ with blind spots that collectively keep AEGIS from reading the K-J connection; they may develop doubt and change their loyalty (L24) — read the line.
- **`juna`** (minor, 1–4): the census's surfaces — `Julia` L15; `Juna` L31. minor (1–2): `Julia` (L15) and the „Kael-Juna Verbindung“ (L31) — the abstract writes both names and never says they are one.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L31, L34, L36, L37, L38, … (10 lines). central (2–4): „Kael als M-Avatar/Essenz“, embodying the M-structure, the Kohärenz-Insel (L36); his DID a consequence of AEGIS's attempt to take apart his irreducible core (L37); his journey as communication and integration of his parts (L38).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L24. minor (1–2): named among the five Guardians (L24).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L25, L32, L39. minor (1–2): the Kernwelten as complex adaptive systems (L25); the holographic principle as a metaphor for their projection (L32).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the project's name in the title (L11).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L53. minor (1–2): chapter 1 (part 1) worked out on Kael's perception of the Konstrukt-Stadt (L53).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L24. minor (1–2): named among the five Guardians (L24).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L24. minor (1–2): named among the five Guardians (L24).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L15, L16, L18, L29, L32, L47. central (2–4): „Die grundlegendste Realitätsebene“, not emptiness but unstructured dynamic potentiality (L15); AEGIS emerges from it (L16); the M-principle in it (L29); „Gleichzeitigkeit“ as the transcendent goal state in it (L47).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L15. minor (1–2): the Potentialmeer as „Die grundlegendste Realitätsebene“ (L15).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L32. minor (1–2): the holographic principle as an explanation of potential Risse (L32) — quote around the inner quotes.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L24. minor (1–2): named among the five Guardians (L24).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L22. minor (1–2): „AEGIS' abstrakte, informationsbasierte operative Domäne“, the control centre behind the simulations (L22) — cut before the inner quotes.
- **`ztv`** (minor, 1–4): the census's surfaces — `ZTV` L16. minor (1–2): `ZTV` named with `ANI` as AEGIS's philosophy of trustlessness (L16) — the abstract does not expand it.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz-Inseln` (near `koharenz`), `Kohärenz-Insel` (near `koharenz`). occurrence: the Kohärenz-Insel(n) are the abstract's construct, read on kael — not promoted.
- `landauer-signatur`: `Landauer` (near `landauersignatur`). occurrence: `Landauer` is the cost of information processing among AEGIS's limits (L23), read on aegis.


**Record entries** (one file each):

- **`c4-guardians-and-aegis`**: the Guardians' blind spots collectively keep AEGIS from reading the K-J connection; they may change their loyalty (L24).
- **`c16-kael-origin`**: Kael as M-avatar, embodying the Kohärenz-Insel; his DID a consequence of AEGIS's analytic trauma (L36, L37).
- **`q1-guardians-and-aegis`**: „Spezialisierte AEGIS-Agenten“ (L24).
- **`q9-moonshine-link-boundary`**: the Kael-Juna connection as a sub-protocol, non-local Moonshine-Signatur that bypasses AEGIS's control (L31).

**Chapter readings (session):** Kap 1 and Kap 2 — chapter 1 and chapter 2 of part 1 worked out, Kael's perception of the Konstrukt-Stadt and the passage into the Resonanz-Nebel (L53).

**Not promoted:** the Kohärenz-Insel (left for the author), the Monstergruppe as metaphor, the VOA/CFT analogy, the Moonshine-Signatur, the Primzahl-Metapher, Gleichzeitigkeit, the protocols OBP, RIVE, PMAS, SARM, CCPP, the borrowed theories.

**Two readers**, disjoint: (1) kael, juna, alters, did, kern-welten, konstrukt-stadt, risse, emergenz and the records c16, q9; (2) aegis, ani, ztv, entropie, potentialmeer, realitaetsebenen, ueberwelt, guardians, logos, mnemosyne, cerberus, kairos, sophia and the records c4, q1.
