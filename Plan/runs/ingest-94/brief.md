# Brief — readings from document 94 (step 6)

1 document, one reader, one batch: `ingest-94`. Files go to `Plan/runs/ingest-94/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 94 | `charaktere` | 2025-07-29 | „the character concept“ (`Charaktere`) | a German character-concept document of 2025-07-29 in the first person of a „Narrativer Architekt“, answering one commission three times over (L15, L112–L248, L250 on): Kael's trauma biography through AEGIS, the eleven Anteile of System Kael (TSDP), AEGIS and its paradox, Juna/V, the Guardians per world and secondary figures (L359 on), with prose recommendations; it calls itself a „Bauplan“, names no source by title, claims no canon, and hedges AEGIS and Juna/V (`dürfte`, `möglicherweise`) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (398 lines for `charaktere`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A design: write „the character concept describes …“ or „proposes …“; keep its hedges. **Three answers, one file — name the answer you read** (the first L15–L110, the second L112–L248, the third L250 on); they order the eleven differently (Lex tenth at L74, fourth at L286; Lia fifth at L49, eighth at L314) and give Nyx two genders (`Er` L42, L153; `Ihre Rolle` L282) — record each where it falls, never reconcile. A twelfth name, `Nox`, stands once as a persecutor (L96). **Two Lexes:** the external construct „Der Archivar / Einheit 734 / „Lex“ (Externe Entität)“ in KW1 (L371) beside Kael's inner Lex, a doubling the document calls deliberate (L373) — record both, on `lex` and on Q7. `--find` refuses names under four characters (`Nox`, `DID`, `ISH`): quote a longer phrase around them. The document names no chapter.

## Pages — document 94, `charaktere`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L19, L21, L27, L32, L43, … (44 lines). central (4–6): AEGIS as „Autonomous Entropic Gatekeeper for Integrity Systems“, its existence defined by negating the Nichts Rauschen (L21); its Genesis-Krise as the primary cause of Kael's fragmentation (L116); its paradox; the Guardians as its entities (L363).
- **`alex`** (central, 3–12 quotations): the census's surfaces — `Alex` L64, L67, L89, L101, L136, L160, … (10 lines). minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L262, L263, L342, L391. minor (2): the eleven Anteile („Elf Seelen in einem System“, L125) and the twelfth name `Nox` (L96).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L79, L82, L211, L335. minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L33. minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L367. minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`did`** (minor, 1–4): the census's surfaces — `DID` L19, L256, L263. minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L349. minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L230. minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L17. minor (1–2): the Genesis-Krise of AEGIS as the primary cause of Kael's fragmentation (L116); section I's heading (L17).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L246, L359, L363. minor (2–3): section V (L359 on): AEGIS entities, one per Kernwelt — LogOS, Mnemosyne, Cerberus, Kairos & Sophia (L363–L367).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L54, L57, L89, L168, L171, L321. minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L100, L161, L197, L348, L352, L354, … (8 lines). minor (2–3): Juna/V as the document hedges it (L348–L356), Juna/V-Allianzen among the parts.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L11, L15, L17, L19, L21, L23, … (61 lines). central (4–6): Kael's trauma biography through AEGIS's hand (section I, L17 on), the TSDP foundation (L112 on), the way to Funktionale Multiplizität (L232 on).
- **`kairos`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kairos` alone on L368. minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L116, L246, L346, L363. minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`kiko`** (central, 3–12 quotations): the census's surfaces — `Kiko` L42, L44, L47, L89, L93, L94, … (24 lines). minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: the title — occurrence (J9).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L67, L74, L77, L89, L93, L99, … (22 lines). central (4–5): the rational ANP (L74 in the first answer, L286 in the third) — and the external construct Archivar / Einheit 734 / „Lex“ in KW1 (L371) with the author's note on the deliberate doubling (L373).
- **`lia`** (central, 3–12 quotations): the census's surfaces — `Lia` L42, L49, L52, L89, L94, L100, … (16 lines). minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L365. minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L366. minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L356. minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`moros`** (central, 3–12 quotations): the census's surfaces — `Moros` L59, L62, L73, L89, L135, L136, … (15 lines). minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L102, L234, L262. minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`nyx`** (central, 3–12 quotations): the census's surfaces — `Nyx` L39, L42, L89, L93, L94, L101, … (24 lines). minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L327. minor (1) only if L327 uses `Persona` in the page's sense; else occurrence, say why.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L393. minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`rhys`** (central, 3–12 quotations): the census's surfaces — `Rhys` L69, L72, L89, L93, L100, L144, … (16 lines). minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`selene`** (central, 3–12 quotations): the census's surfaces — `Selene` L34, L37, L100, L102, L136, L139, … (11 lines). minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`sophia`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Sophia` alone on L368. minor (1–2): what the character concept says of it — 1–3 quotations, naming the answer.
- **`tsdp`** (central, 3–12 quotations): the census's surfaces — `TSDP` L31, L36, L41, L46, L51, L56, … (27 lines). central (3–4): TSDP as the foundation of the fragmentation (L112 on) and each Anteil's TSDP-Typ.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L393. not read unless L393 uses `Simulation` for the Überwelt itself: occurrence, say why.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). `Genesis-Krise` is read on `genesis` above (J12 keeps it a compound; the reading names it).
- `kairos`: `Kairos & Sophia` (near `kairos`), `Kairos-Potentialis` (near `kairos`). `Kairos & Sophia` and `Kairos-Potentialis`: readings on kairos and sophia — the KW4 guardians (L367) (J49).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Paradoxon der Fehlausgerichteten Kohärenz` (near `koharenz`), `innere Kohärenz` (near `koharenz`). occurrences: the title and compounds (J9, J12).
- `nichts-rauschen`: `Nichts Rauschens` (near `nichtsrauschen`). a reading on `nichts-rauschen`: AEGIS defined by negating it (L21) — `Nichts Rauschens` is its genitive (J24).
- `potentialmeer`: `Potentialmeers` (near `potentialmeer`). a reading on `potentialmeer`: the same line, „oder Potentialmeers“ (L21) (J24).
- `sophia`: `Kairos & Sophia` (near `sophia`). a reading, as kairos.


**Record entries** (one file each; write one only where the concept speaks to the record's question):

- **`q7-what-734-names`**: the external construct „Einheit 734“ named „Lex“ in KW1 (L371, L373).
- **`q3-how-many-kern-welten-and-alters`**: eleven Anteile (L125) and the twelfth name Nox (L96); four Kernwelten.
- **`c6-guardians-count-and-pairing`** and **`q5-guardians-and-kern-welten`**: the guardian per world, two in KW4 (L363–L367).
- **`c16-kael-origin`**: the Genesis-Krise of AEGIS as the primary cause of Kael's fragmentation (L116), if it speaks to his origin.

**Split into two readers, one after the other:**
- Reader 1: aegis, kael, juna, genesis, guardians, kern-welten, logos, mnemosyne, cerberus, kairos, sophia, nichts-rauschen, potentialmeer, moonshine-link, cache-kohaerenz, entropie, emergenz, realitaetsebenen, ueberwelt, personas, and the five records.
- Reader 2: the alters' pages (lex, alex, argus, isabelle, kiko, lia, moros, nyx, rhys, selene, alters), tsdp, did, multiplizitaet.
