# Brief — readings from document 174 (step 6)

1 document, one reader, one batch: `ingest-174`. Files go to `Plan/runs/ingest-174/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 174 | `kohaerenz-analyse-kapitel-2` | 2025-12-28 | „the analysis report“ (titled `Analysebericht: Narrative Architektur und Systemkohärenz im Projekt "Kohärenz Protokoll"`) | a German analysis report: the ontology of the Nichts and AEGIS's genesis, AEGIS and the Guardians, Kael as a DID system with named alters, an analysis of Kapitel 1 and Kapitel 2 (its 40 resonance moments in four phases), Juna and Monstrous Moonshine, and eight numbered recommendations to the author; it summarises its cited sources (glued reference digits, L239–L248) and calls itself a „Fundament für die weitere Ausarbeitung“ (L233) — recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (249 lines for `kohaerenz-analyse-kapitel-2`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analyst reporting sources and recommending: write „the analysis report reads / reports / recommends …“; where it says „Die Analyse der Genesis-Texte“ or cites a document by name, it is that source's claim as the report gives it. Recommendations (L206–L231) are recommendations, never the world. German — quote as written; the document uses straight quotes throughout — cut before them, never quote across them; glued reference digits follow sentences — end before them.

## Pages — document 174, `kohaerenz-analyse-kapitel-2`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L23, L25, L27, L31, L33, … (26 lines). central (2–4): not made but evolved from a consciousness fragment's struggle in the Nichts (L25); „Der große Wandel“ from feeling to functioning (L27); trauma as basis, cold rationality a defence (L31); an autopoietic system (L33); the Zero-Trust model (L47); the Landauer trap (L51); the Universal Reboot as controlled collapse (L57).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Zero-Trust` alone on L83. minor (1–2): AEGIS operates on „einem strikten“ Zero-Trust model (L47); Cerberus's Zero-Trust approach prevents healing (L83).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L41, L96, L207, L212. minor (1–2): the alters named — Limina, Nox, Praetor, Echo, Oblivion, with Index (L104–L131); the alters' bleeding effect (L207); their speech styles (L212–L218).
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache-Kohärenz` L41, L244. minor (1–2): „Cache-Kohärenz in Multi-Core-Prozessoren“ as the image of Kael's alters or the Kernwelten holding different states (L41).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L79, L83, L114, L218. minor (1–2): Cerberus (Grenzfeste / KW3): security and paranoia, the immune system of AEGIS, every integration step an „Intrusion“ (L79–L83).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L35, L92. minor (1–2): Kael „eine wörtliche Verkörperung der“ DID within a digital world (L92); his trauma a fractal image of AEGIS's (L35).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L21. minor (1–2): stability thermodynamically expensive (L21); AEGIS sees entropy as death, for Kael it is life — recommendation 8 (L231).
- **`genesis`** (minor, 1–4): the census's surfaces — `Genesis` L13, L19, L25, L57, L178, L226. minor (1–2): „Die Analyse der Genesis-Texte“ (L25); the genesis of the Leere (L13, L19); the document „Genesis im Echo der Leere“ (L57) — a title, say so.
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L79, L114. minor (1–2): Cerberus's world, KW3 (L79); Nox lives there (L114).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L43, L61, L63, L191, L242. central (2–4): „keine eigenständigen KI-Persönlichkeiten, sondern spezialisierte Subroutinen von AEGIS“ (L63); their inability to see Juna (L63); Juna is noise to them (L191).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L39, L63, L76, L83, L119, L141, … (15 lines). central (2–4): „eine ‚nicht-lokale Integritätsverletzung'“ — quote around the inner quotes (L189); an anchor for Kael, noise for the Guardians (L191); she brings new energy (L192); Kapitel 1's conversation and her flickering image (L141); recommendation 5 (L222).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L35, L41, L59, L69, L77, L83, … (39 lines). central (2–4): „ein fragmentiertes System“ (L92); the host, ANP, amnesic (L98–L102); Kael as „der ‚M-Entity'“ fragmented by the CFP (L96) — quote around the inner quotes; the „Wir-Geflecht“ (L127–L131); his trauma fractal to AEGIS's (L35).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L85, L87. minor (1–2): Kairos & Sophia (Möglichkeits-Garten / Überwelt / KW4); Kairos permits productive chaos, „nützliche Entropie“ (L85, L87).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L33, L41. minor (1–2): AEGIS creates its own conditions by simulating the Kernwelten (L33); the Guardians' worlds (L65–L85); learning the languages of the worlds (L183).
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L11, L17, L37, L39, L41, L202, … (11 lines). central (2–4): „Kohärenz“ as „operative Variable für die Integrität der Realität“ — cut before the quotes (L39); sinking coherence metrics make Risse (L39); the closing, coherence not by elimination but by weaving (L233).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L59, L65, L139, L158, L208, L226, … (7 lines). minor (1–2): LogOS's world, KW1 (L65); its „sterile Perfektion“ from the reboot (L59); Kapitel 1's „verstörender Perfektion“ (L139); recommendation 3, the city as antagonist (L208).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L65, L68, L69, L70, L216. minor (1–2): LogOS (Konstrukt-Stadt / KW1), the „Chef-Diagnostiker“, blind to paradox and emotion (L65–L70).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L72, L77. minor (1–2): Mnemosyne (Resonanz-Landschaft / KW2), archivist of emotional data; to her Juna is a corrupt record (L72–L77).
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L85. minor (1–2): „Kairos & Sophia (Möglichkeits-Garten / Überwelt / KW4)“ (L85) — KW4 set beside the Überwelt.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Multiplizität` L102, L129. minor (1–2): from Teil 2 Kael develops „funktionalen Multiplizität“, cooperation not fusion (L129).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L17, L39. minor (1–2): the Nichts not passive absence but „Nichts Rauschen“ — read L17 for the bold; existence as resistance (L19).
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L108, L122, L125. minor (1–2): „Oblivion: Repräsentiert den“ Freeze state, a catatonic part holding the worst memories (L125).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L72, L124. minor (1–2): Mnemosyne's world, KW2 (L72); Echo lives there (L124).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L37, L39, L51, L207. central (2–4): „Wenn die Kohärenzmetriken sinken, entstehen“ Risse, ontological injuries (L39); Kapitel 1's first Riss in the transit corridor (L142); recommendation 2, the physics of the Risse (L207).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L85, L88. minor (1–2): „Sophia: Repräsentiert die Metakognition und Synthese“, limited by the axiom Seele=Info (L88).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L85. minor (1–2): KW4 set beside the Überwelt in Kairos & Sophia's heading (L85) — read the line.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Anomalie` (near `mustererkennunganomaliedetektion`). occurrence: `Anomalie` is Juna as the Guardians see her (L63), on juna.
- `aegis-teilfunktionen`: `Zero-Trust-Modell` (near `zerotrust`). a reading — on aegis-teilfunktionen above.
- `entropie`: `nützliche Entropie` (near `entropie`), `positiver Entropie` (near `entropie`). a reading: Kairos's „nützliche Entropie“ (L87) and AEGIS's view of entropy — on entropie above.
- `kaels-wohneinheit`: `Das Nein` (near `kaelswohneinheit`), `Das Nein` (near `kaelswohneinheit10`). occurrence: `Das Nein` is Kael's later refusal (L182), not the dwelling.
- `personas`: `Depersonalisation` (near `persona`). occurrence: `Depersonalisation` is a symptom (L140).
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` is a child alter (L124).


**Record entries** (one file each):

- **`c16-kael-origin`**: Kael „der ‚M-Entity'“, an integrated human soul fragmented by AEGIS's CFP (L96) — quote around the inner quotes.
- **`c4-guardians-and-aegis`**: the Guardians cannot see the anomaly Juna (L63); to them she is noise (L191).
- **`c6-guardians-count-and-pairing`**: LogOS–KW1, Mnemosyne–KW2, Cerberus–KW3, Kairos & Sophia–KW4/Überwelt (L65–L88).
- **`q1-guardians-and-aegis`**: „spezialisierte Subroutinen von AEGIS, die abgespalten wurden“ (L63).
- **`q3-how-many-kern-welten-and-alters`**: Kael, Limina, Nox, Praetor, Echo, Oblivion, with Index named (L98–L131); a triad in Kapitel 2 (L168).
- **`q5-guardians-and-kern-welten`**: the same pairing, two Guardians for KW4 (L65–L88).
- **`q9-moonshine-link-boundary`**: Monstrous Moonshine as „eine akausale Symmetrie“, orthogonal to the system's logic (L196, L198).

**Chapter readings** are written by the session: Kap 1 (L135–L146) and Kap 2 (L148–L178).

**Not promoted:** Limina, Nox, Praetor, Echo, Index (alter names, on Q3), the CFP, the B-Welt / Beta-Rho-5, Omega-Prime, Ly-Welt, Universal Reboot (on aegis), Wir-Geflecht (on multiplizitaet), Das Nein, the eight recommendations, Monstrous Moonshine, Landauer, autopoiesis.

**Two readers**, disjoint: (1) kael, juna, alters, did, oblivion, multiplizitaet, kohaerenz, cache-kohaerenz, risse, entropie, nichts-rauschen, genesis and the records c16, q3, q9, c4; (2) aegis, aegis-teilfunktionen, guardians, logos, mnemosyne, cerberus, kairos, sophia, kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten, ueberwelt and the records c6, q1, q5.
