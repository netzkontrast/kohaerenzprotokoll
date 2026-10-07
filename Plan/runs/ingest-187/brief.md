# Brief — readings from document 187 (step 6)

1 document, one reader, one batch: `ingest-187`. Files go to `Plan/runs/ingest-187/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 187 | `kohaerenz-protokoll-weltkonzept-synthese` | 2025-04-23 | „the final world concept“ (titled `Kohärenz Protokoll: Finales Weltkonzept`) | a German synthesis in six sections — the Potentialmeer, AEGIS with its Guardians and the Kernwelten, Kael from a Kohärenz-Insel, the Kael-Juna-Verbindung by Resonanz, and the central paradox of coherence by Abgrenzung against coherence by Integration; it calls itself „definitive Referenz“ (L13) and „verbindliche Referenz“ (L169) yet hedges throughout (`wahrscheinlich` 19 times) — recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (170 lines for `kohaerenz-protokoll-weltkonzep`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A synthesis that calls itself definitive: write „the final world concept defines / describes …“, never as settled, and keep its hedges (`wahrscheinlich`, `möglicherweise`, the question marks after OBP, PMAS, SARM). It cites a „Finalen Plot-Blueprint“ it never reproduces — that is its report. German — quote as written; cut before inner quotes; KW numbers lose their digit in `--find` — quote around them; the table at L138–L143 has escaped bold — quote the plain words.

## Pages — document 187, `kohaerenz-protokoll-weltkonzept-synthese`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L22, L23, L24, L25, L26, … (66 lines). central (2–4): „eine emergente, nicht-menschliche, informationsbasierte Entität“ that arose autopoietically from the Potentialmeer by drawing a boundary (L34); its Kern-Direktive „Sein durch Abgrenzung“ (L36), driven by the Potentialmeer's self-erasure (L26); it perceives the Kohärenz-Insel / Kael-Juna-Verbindung as a threat (L48); likely bound by Gödelian limits (L50); its strength is the source of its weakness (L53).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L63, L64, L85. minor (1–2): Kael's psyche fragmented into „Alters“ after DID or possibly IFS (L64) — cut before the quotes; dialogue between Alters as narrative mechanics (L85).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L43, L74, L85. minor (1–2): Guardian of KW3 Schattenlabyrinth (L43, L74).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L47, L63, L64, L85, L165. minor (1–2): „analog zur Dissoziativen Identitätsstörung (DID)“ or possibly IFS (L64); the DID/IFS model as narrative mechanics (L85).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L33. occurrence: „Emergenz“ in the heading of AEGIS's definition (L33) is AEGIS's arising, read on aegis — not the wiki's Emergenz.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L21. minor (1–2): the Potentialmeer's „extrem hohe Entropie“ (L21); AEGIS perceives the Potentialmeer as chaos and entropy (L46) and Kael's connection as entropy (L81).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L25, L95, L97, L107. minor (1–2): Juna as the anchor of Kael's connection to the Kohärenz-Insel „und damit zur“ Externe Ebene/Nexus (L96); a possible narrative endpoint, a symbol of liberation (L107).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L42, L43, L55, L83. minor (1–2): „spezialisierte Subsysteme oder Agenten von AEGIS“, each managing one Kernwelt (L43); their „blinden Flecken“ inherited from their world (L44) — cut before the quotes; fault lines within AEGIS (L55).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L41, L44, L48, L50, L52, L53, … (31 lines); `Julia` L95, L96. central (2–4): „Juna (oder Julia)“, the anchor of Kael's connection to the Kohärenz-Insel, the embodiment of the integrative principle and the guide of his integration (L96); her influence by Resonanz, „sub-protokollarischen“ (L97) — cut before the quotes; Kael-Juna's coherence by integration (L132).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L24, L40, L41, L45, L47, … (48 lines). central (2–4): his „menschliche (?) Essenz“ comes not from AEGIS's realities but from a Kohärenz-Insel in the Potentialmeer (L62) — cut around the question mark if needed; fragmented after DID (L64); his arc from dissociation to wholeness (L66); a component AEGIS must contain (L80); his origin is the source of his potential for integration (L84); the living interface between the two principles (L165).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L43, L75. minor (1–2): Guardian of KW4 Möglichkeitsstrom (L43, L75).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L25, L38, L40, L43, L47, L55, … (15 lines); `Kernwelt` L25, L38, L40, L43, L44, L47, … (16 lines). central (2–4): simulated realities generated by AEGIS but „fundamental Externalisierungen von Kaels fragmentierter Psyche“ (L68); KW1 Konstrukt-Stadt, KW2 Resonanz-Nebel, KW3 Schattenlabyrinth, KW4 Möglichkeitsstrom with what each represents (L72–L75); the interface between Kael's state and AEGIS (L83).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the project's name in the title (L11).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L43, L72. minor (1–2): KW1, logic, order, hyper-rationality, managed by LogOS (L72).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L43, L55, L72. minor (1–2): Guardian of KW1 Konstrukt-Stadt (L43, L72).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L43, L55, L73, L85. minor (1–2): Guardian of KW2 Resonanz-Nebel, emotion, trauma, memory (L43, L73).
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L25, L93, L95, L96, L97, L107. minor (1–2): „Externe Ebene/Nexus“ as one plane joined to Juna and the Kohärenz-Insel (L96, L107).
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L15, L17, L20, L21, L23, L24, … (22 lines). central (2–4): the most fundamental layer of existence, „Raum reinen logischen Potentials“ (L20) — cut before the quotes; unending potential, logical chaos, very high entropy, a tendency to self-erasure (L21); the absolute base of the ontology (L25); the background of the two forms of coherence (L27); its self-erasure the cause of AEGIS's directive (L26).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L43. minor (1–2): named among the Guardians' examples (L43) — read what L43 says of her.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L25, L35, L37, L38, L93. minor (1–2): „AEGIS' Operationsdomäne“, an abstract informational layer distinct from the Potentialmeer and the Kernwelten (L38).

**A page the census reaches by another surface** (read it too):

- **`kael-julia-bindung`** (central, 2–4): the `Kael-Juna-Verbindung` (J13: the page's name is open) as „das Herzstück des alternativen Kohärenzprinzips“ (L89); the strength of the „Kael-Juna-Bindung“ from relational complexity (L104); coherence by integration against AEGIS's by Abgrenzung, the table (L131–L143); AEGIS cannot grasp it (L134).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` (L72–L75) is the Guardians' title, read on guardians.
- `entropie-resonanz`: `Protokolle` (near `entropieresonanzentropieresonanzprotokolleerp`), `Protokolle` (near `entropieresonanzprotokolle`), `Resonanz` (near `entropieresonanz`), `Resonanz` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz` (near `entropieresonanzprotokolle`). occurrence: `Protokolle` and `Resonanz` are AEGIS's protocols and Juna's mode of influence (L97–L101), read on aegis and juna — not the Entropie-Resonanz-Protokolle.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Insel` (near `koharenz`), `Kohärenz-Inseln` (near `koharenz`), `Kohärenz-Insel / Kael-Juna-Verbindung` (near `koharenz`), `integrative Kohärenz` (near `koharenz`). occurrence: the Protokoll's name; the Kohärenz-Insel and integrative Kohärenz are the document's own constructs, read on kael, juna and kael-julia-bindung (not promoted).
- `resonanz-landschaft`: `Resonanz` (near `resonanzlandschaft`). occurrence: `Resonanz` is Juna's mode of influence (L97), not the Resonanz-Landschaft.


**Record entries** (one file each):

- **`c4-guardians-and-aegis`**: Guardians as subsystems of AEGIS whose blind spots are fault lines within AEGIS (L43, L44, L55).
- **`c6-guardians-count-and-pairing`**: LogOS–KW1, Mnemosyne–KW2, Cerberus–KW3, Kairos–KW4; Sophia named among the examples (L43, L72–L75).
- **`c16-kael-origin`**: Kael's essence comes from a Kohärenz-Insel in the Potentialmeer, not from AEGIS's simulated realities (L62, L84).
- **`q1-guardians-and-aegis`**: „spezialisierte Subsysteme oder Agenten von AEGIS“ (L43).
- **`q5-guardians-and-kern-welten`**: one Guardian per Kernwelt (L43, L72–L75).
- **`q9-moonshine-link-boundary`**: Resonanz as „sub-protokollarisch“, bypassing AEGIS's formal systems; AEGIS perceives it as noise (L97, L101).

**Not promoted:** the Kohärenz-Insel — the document's ground for Kael's origin; 16 landed documents write it 119 times (`corpus.py count`), and no page holds it yet: a candidate for a page of its own, left for the author; Resonanz as Juna's mode, Sein durch Abgrenzung and integrative Kohärenz, the Monstergruppen-Metapher, the protocol names OBP, PMAS, SARM, RIVE, CCPP, Autopoiesis, the Finaler Plot-Blueprint.

**Two readers**, disjoint: (1) aegis, guardians, logos, mnemosyne, cerberus, kairos, sophia, ueberwelt, potentialmeer, entropie and the records c4, c6, q1, q5; (2) kael, juna, kael-julia-bindung, alters, did, kern-welten, konstrukt-stadt, externe-ebene, nexus and the records c16, q9.
