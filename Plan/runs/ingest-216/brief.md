# Brief — readings from document 216 (step 6)

1 document, one reader, one batch: `ingest-216`. Files go to `Plan/runs/ingest-216/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 216 | `roman-synthese-mit-dual-kernel-theorie` | 2026-02-25 | „the DKT synthesis“ (an unsigned analysis) | a German analysis that applies its Dual-Kernel-Theorie to a 39-chapter plot, each chapter read on four labelled levels (narrative, systemic, scientific, DKT), then sections on the characters, the Guardians, thermodynamics and philosophy, from numbered references — no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (497 lines for `roman-synthese-mit-dual-kernel`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis of a plan: write „the DKT synthesis reads / analyses …“ and name the chapter (Kapitel N) or section a line belongs to; the four levels are its own frame. German — quote as written; the export dropped every kernel symbol (`zwei rechnerischen Substraten entsteht: , dem Kernel`) — never quote across a gap; cut before glued footnote digits (`Amnesie.3`) and inner quotes; `--find` drops digits (`Sektor 04`, `K1`) — quote around them.

## Pages — document 216, `roman-synthese-mit-dual-kernel-theorie`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L13, L24, L38, L56, L69, L119, … (21 lines). central (3–8): the table pairing „AEGIS / LogOS“ with coherence and the maintenance of structure (L24); from AEGIS's view Juna is the „Absolute Entropie“ (L411) — cut before the inner quotes; AEGIS's attempts to cleanse Kael's psyche overheat the simulation (L429); the Bekenstein bound limiting what AEGIS can simulate (L433); the Guardians as „AEGIS' Ausführungsorgane“ (L413).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `SIS` L148. minor (1–3): read L148 — the K1-Kernel failure and the transition into the SIS-Zustand (Secure Isolation State); decide reading or occurrence.
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L19, L315, L433. minor (1–3): Kael's DID (L19) — read the line; the cooperation of the alters under the self's leadership (L315); AEGIS's cache procedures — alters only loaded when needed (L433).
- **`archiv-der-grenzen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Archiv der Grenzen` alone on L154. minor (1–3): chapter 14 `Das Archiv der Grenzen` (L154) — read its levels.
- **`blinder-fleck`** (minor, 1–4): the census's surfaces — `Blinder Fleck` L415. minor (1–3): the Guardians' shared „Blinder Fleck“, the inability to process non-logical relationality (L415) — cut before the inner quotes.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L419. minor (1–3): „Cerberus: Implementiert Sicherheitsprotokolle in der Grenzfeste“, reading vulnerability as attack (L419).
- **`chaitin-konstante`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Chaitin-Konstante` alone on L462. minor (1–3): „Juna ist die personifizierte Chaitin-Konstante“ (L462) — cut before the colon if needed.
- **`did`** (minor, 1–4): the census's surfaces — `DID` L19, L152, L462. minor (1–3): Kael's dissociative identity disorder (DID) read through the DKT (L19); Kael exploring his internal system (DID) in act II (L152); the DID as a survival architecture, not a pathology (L462).
- **`dkt`** (central, 3–12 quotations): the census's surfaces — `DKT` L13, L40, L49, L58, L67, L76, … (42 lines). The sweep found `Dual-Kernel-Theorie (DKT)` alone on L13. central (3–8): „unter strikter Anwendung der Dual-Kernel-Theorie (DKT)“ (L13); the theory postulating reality from the tension of two computational substrates (L17) — never across the dropped symbols; the DKT level under every chapter (L40 and on); the DKT letting the reader read Kael's DID as survival architecture (L462).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L17. minor (1–3): the kernel of irreversible collapse and entropy (L17) — read around the gaps; Juna as „Absolute Entropie“ for AEGIS (L411).
- **`evaluierungseinheit`** (minor, 1–4): the census's surfaces — `Evaluierungseinheit` L145. minor (1–3): „Kael wird in die Evaluierungseinheit transferiert“ (Kap 13, L145) — cut before the inner quotes.
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L288, L419. minor (1–3): „Kael konfrontiert Nox, den Alter des Traumas, in der Grenzfeste“ (L288); Cerberus's security protocols in the Grenzfeste (L419).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L413, L415, L484, L496. central (3–8): „Die Guardians: AEGIS' Ausführungsorgane“ (L413); specialised filter algorithms each watching one aspect of coherence (L415); the five named with their domains — LogOS, Mnemosyne, Cerberus, Kairos, Sophia (L417–L421).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L13, L25, L51, L53, L56, L134, … (23 lines). central (3–8): Juna as relationality and the intrusion of meaning in the table (L25); „Juna – Das flüchtige Echo“ (Kap 3, L51); LogOS cannot see Juna because she lies outside the axiomatic basis (L134); Juna as „Mosaik-Herz“ of chaos (L264); Juna as a part in the table, the transcendence vector and interface to the external level (L406); Juna as the personified Chaitin-Konstante (L462).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L13, L19, L26, L31, L35, L37, … (62 lines). central (3–8): Kael's DID (L19); Kael feeling the cold architecture and amnesia (Kap 1, L37); Kael transferred into the Evaluierungseinheit (L145); Kael confronting Nox in the Grenzfeste (L288); Kael as the witness function, from unknowing host to conscious architect (L398); Kael recognising the Risse as the breathing pause of reality (L462).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L420. minor (1–3): „Kairos: Steuert die kreativen Prozesse im Möglichkeiten-Garten“ (L420).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L298. minor (1–3): the collapse of the protective zones between the Kernwelten (L298).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. occurrence: the Protokoll's name (L13).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L13. minor (1–3): read L13 — „zwischen dem Kohärenz-Kernel () und“ — quote before the gap.
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L13. minor (1–3): read L13 for the Kollaps-Kernel — quote around the gap.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L17, L31, L239, L324, L417, L480. minor (1–3): the Konstrukt-Stadt read in the DKT (L17) — read the line; LogOS guarding the logic of the Konstrukt-Stadt (L417); the city's architecture bounded by the Bekenstein bound (L433).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L24, L47, L134, L306, L417. minor (1–3): „AEGIS / LogOS“ in the table (L24); LogOS cannot see Juna (L134); „LogOS verstummt“, the last logical barrier collapses (L306); LogOS guarding the Konstrukt-Stadt's logic, failing on Gödel (L417).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L110, L219, L418. minor (1–3): Mnemosyne monitoring emotional coherence but blind to the traumatic context (L110); „Mnemosynes Archiv wird gehackt“ (L219); managing the data streams of memory (L418).
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L264, L338, L344. minor (1–3): „Juna als“ Mosaik-Herz of chaos, the key to integration (L264) — cut before the inner quotes; chapter 34 `Das Mosaik-Herz` (L338); the integrated Mosaik-Herz as the solution of the coherence crisis (L344).
- **`negentropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Negentropie` alone on L317. minor (1–3): „Psychische Negentropie als Zustand geordneter mentaler Energie“ (L317).
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L333. minor (1–3): „Rückzug in den Nexus; Schutz von Juna vor dem finalen Löschbefehl“ (L333) — decide reading or occurrence by the page's sense.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts-Rauschen` L71, L369. minor (1–3): „Der Raum löst sich auf; nur noch das“ Nichts-Rauschen remains (L369) — cut before the inner quotes; read L71.
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L143. occurrence: `Persona` at L143 is the collapse of the first persona — read the line; an occurrence unless it means the page's Personas.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L19, L27, L230, L429, L462. minor (1–3): the Landauer principle: every erasure of information produces heat, leading to the thermal Risse (L19) — cut before the inner quotes; the Risse as thermodynamic relief points (L429); the Risse as the breathing pause of reality (L462).
- **`sektor-04`** (minor, 1–4): the census's surfaces — `Sektor 04` L65. minor (1–3): a deadlock in the subroutine architecture of Sektor 04 (L65) — quote around the digits.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L421. minor (1–3): „Sophia: Repräsentiert die systemimmanente Weisheit der Überwelt“, integration as elimination of deviation (L421).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L421. minor (1–3): Sophia representing the system-immanent wisdom „der Überwelt“ (L421).
- **`verschraenkungs-insel`** (minor, 1–4): the census's surfaces — `Verschränkungs-Insel` L331. minor (1–3): „Kael erschafft eine“ Verschränkungs-Insel, causal isolation from the system (L331) — cut before the inner quotes.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie`: `Absolute Entropie` (near `entropie`), `Psychische Negentropie` (near `entropie`). `Absolute Entropie` read on entropie (L411); `Psychische Negentropie` read on negentropie (L317).
- `kohaerenz`: `Zielkohärenz` (near `koharenz`), `Cache-Inkohärenz` (near `koharenz`). occurrences: `Zielkohärenz` (a chapter title) and `Cache-Inkohärenz`.
- `negentropie`: `Psychische Negentropie` (near `negentropie`). read on negentropie (L317).
- `thermodynamischer-phaenomenalismus`: `Phaenomena` (near `thermodynamischerphaenomenalismus`). occurrence: `Phaenomena` is the document's word.


**Record entries** (one file each):

- **`q5-guardians-and-kern-welten`**: five Guardians with their domains — LogOS the Konstrukt-Stadt's logic, Mnemosyne the memory streams, Cerberus the Grenzfeste, Kairos the Möglichkeiten-Garten, Sophia the Überwelt (L417–L421).
- **`c4-guardians-and-aegis`**: the Guardians as „AEGIS' Ausführungsorgane“, filter algorithms with a shared blind spot (L413, L415).
- **`q3-how-many-kern-welten-and-alters`**: a table of five parts — Host (Kael), Manager, Nox, Juna, Kind (L403–L407); Nox as „den Alter des Traumas“ (L288).
- **`c16-kael-origin`**: Juna listed as a part of the system, the transcendence vector and interface to the external level (L406).

**Not promoted:** the four levels, the RTSV cycle, the SIS state (unless read on aegis-teilfunktionen), the Bekenstein bound, Landauer, Page-Wootters and the other borrowed physics, the Wir-Geflecht, Nox, the Manager and the Kind (on q3), the reference list.

**Two readers**, disjoint: (1) kael, juna, alters, did, grenzfeste, evaluierungseinheit, archiv-der-grenzen, mosaik-herz, verschraenkungs-insel, nexus, chaitin-konstante, personas, negentropie and the records q3, c16; (2) aegis, aegis-teilfunktionen, dkt, kohaerenz-kernel, kollaps-kernel, entropie, risse, nichts-rauschen, konstrukt-stadt, kern-welten, guardians, blinder-fleck, logos, mnemosyne, cerberus, kairos, sophia, ueberwelt, sektor-04 and the records q5, c4.

**Chapter readings**: 39, written by the session (`Plan/runs/ingest-216-kap/`).
