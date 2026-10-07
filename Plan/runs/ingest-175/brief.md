# Brief — readings from document 175 (step 6)

1 document, one reader, one batch: `ingest-175`. Files go to `Plan/runs/ingest-175/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 175 | `narrativ` | 2025-07-30 | „the architect's compendium“ (two German texts in one file: a craft compendium by a „Narrativer Architekt“, L11–L113, and a synthesis by a „Konzept-Dramaturg“, L115–L238) | prose rules for Kael, AEGIS and the Kernwelten, ethics and reader guidance, then a blueprint of AEGIS, System Kael, the Fundament and Juna/V, the six levels, Dramatica and Kishōtenketsu and the project's status; the second calls itself „unser oberstes Architekturdokument“ (L117) and says „Der Bauplan steht“ (L236) — recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (239 lines for `narrativ`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Two voices: the compendium (L11–L113) directs prose — „the compendium directs …“; the dramaturg's blueprint (L115–L238) states the design — „the dramaturg's blueprint sets …“. Style rules are rules for writing, never the world. German — quote as written; the document uses straight quotes — cut before them; glued digits and bracketed reference lists (L117) follow sentences.

## Pages — document 175, `narrativ`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L38, L40, L42, L48, L52, L53, … (32 lines). central (2–4): „AEGIS (Autonomous Epistemic Guardian for Integrity Systems)“ — the expansion, quote it (L125), a C1 entry; its defence against Nicht-Sein (L125); recursive self-verification (L127); the core protocols v1.5 (L129–L137); Paradoxon X (L139); an externalised perpetrator introject (L141); its prose style before and after transformation (L42–L51).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `SIS` L137. minor (1–2): the core protocols: ZTEM, RTSV, BPoF, EIC, Integrity Validation, Entropic Management, „Systemic Isolation Shield (SIS)“ (L131–L137).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `algorithmische Melancholie` L51. minor (1–2): AEGIS's post-transformation rhythm conveys its „algorithmische Melancholie“ — cut before the quotes (L51).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L73. minor (1–2): the alters' development traced to their trauma function (L73); „Elf detaillierte Anteile“ (L149).
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L151. minor (1–2): Kael the host and his Cache Kohärenz (L151); the MESI protocol and Cache-Kohärenz across the worlds (L180) — read the lines.
- **`did`** (minor, 1–4): the census's surfaces — `DID` L19, L70, L72, L227. minor (1–2): Kael's DID on the TSDP model shapes the narrating voice (L19); the ethics of portraying DID (L70–L78, L227).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L113. minor (1–2): the tension „zwischen Kontrolle und Emergenz“ as a creative field (L113); the Fundament as a source of rules for Emergenz (L165).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L65, L136, L139, L184. minor (1–2): „Entropic Management“ rejecting incoherence as „Entropie“ (L136); Paradoxon X, resisting entropy by control (L139); Risse and entropy manifestations (L184).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L182. minor (1–2): „Die Externe Ebene: Eine mysteriöse, dritte Realitätsebene“, the source of the Juna/V link (L182).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L181. minor (1–2): RTSV validates through „das Guardian-Netzwerk“ (L132); L63 — the Grenzwächter of KW3 — read the line.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L161. central (2–4): „Juna/V ist eine externe Entität oder Anomalie“, catalyst or „ontologischer Exploit“ (L167); Impact Character (L194); the Subjective Story Kael ↔ Juna/V (L195); Ten, the turn (L201).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L19, L23, L25, L57, L61, … (38 lines). central (2–4): the polyphonic prose of his fragmented self, from fragments to the collective „Wir“ (L17–L36); „Tertiäre Strukturelle Dissoziation“ (L145); „Kael (Host)“, the primary ANP (L151); Main Character (L193); the „Gärtner“ after his transformation (L229).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L55, L57, L59, L137, L169, L175, … (7 lines). central (2–4): „epistemologische Landschaften“ (L57); the four with KW1 as Logos-Prime (L61–L64) and, in the second text, KW1 as Konstrukt-Stadt (L177–L180) — the file names KW1 two ways, say so.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L35, L36, L155. minor (1–2): „Ein kindlicher EP“ holding early trauma; integrated, a source of creativity (L155).
- **`kishotenketsu`** (minor, 1–4): the census's surfaces — `Kishōtenketsu` L197. minor (1–2): „Die Anwendung von Kishōtenketsu wird als zentrales, tragendes Gerüst empfohlen“ (L197); Ki, Shō, Ten, Ketsu (L199–L202).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. minor (1–2): „Kohärenz vs. Resonanz“, AEGIS's coherence by negation against Kael's and Juna's by acceptance (L226).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L177, L236. minor (1–2): „KW1 (Konstrukt-Stadt / Logik)“, classical logic, prone to glitches (L177).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L35, L36, L153, L177. minor (1–2): an analytic ANP seeking control by logic; integrated, the system's analyst (L153).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L19. minor (1–2): „Funktionale Multiplizität als Heilungsziel“, not fusion (L147); the late phase's prose (L32–L36).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L24, L35, L154. minor (1–2): „Ein EP“, an aggressive protector; integrated, strategic defence (L154).
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L117. not read: `Persona` stands only as a tag in L117's bracketed reference list — an occurrence.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — `Realitätsebenen` L169, L173, L175. minor (1–2): „Die Sechs Realitätsebenen“ (L173), then three numbered entries — four Kernwelten, the Digitale Überwelt, the Externe Ebene (L175–L182).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L65, L139, L177, L184, L236. minor (1–2): „Risse & Entropie-Manifestationen“: glitches, distortions, logic errors (L184); Risse in the worlds' physics (L65).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L152. minor (1–2): „Innere Helferin“ (ISH) or „Torwächter“ — cut before the quotes (L152).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L19, L145. minor (1–2): Kael's DID „basierend auf dem TSDP-Modell“ (L19); his state a tertiary structural dissociation (L145).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Überwelt` alone on L171. minor (1–2): the world as „Digitale Überwelt“ — cut before the quotes (L171); the AEGIS network (L181).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: KW3's name (L63, L179), on kern-welten.
- `entropie-resonanz`: `Resonanz` (near `entropieresonanz`), `Resonanz` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz` (near `entropieresonanzprotokolle`). occurrence: `Resonanz` is the counterpart of AEGIS's logic (L226), not the protocols.
- `juna`: `Juna/V` (near `juna`). a reading — on juna above.
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: KW4's name (L64, L180), on kern-welten.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the project's name.
- `logos`: `Logos-Prime` (near `logos`). occurrence: KW1's name (L61), on kern-welten.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: KW2's name (L62, L178), on kern-welten.
- `resonanz-landschaft`: `Resonanz` (near `resonanzlandschaft`). occurrence: `Resonanz` is not the world.
- `ueberwelt`: `Digitale Überwelt` (near `uberwelt`). a reading — on ueberwelt above.


**Record entries** (one file each):

- **`c1-aegis-expansion`**: „Autonomous Epistemic Guardian for Integrity Systems“ (L125) — a further expansion; the record adds a row and decides nothing.
- **`c9-konstrukt-stadt-scale`**: „KW1 (Konstrukt-Stadt / Logik)“ (L177), and KW1 as Logos-Prime in the first text (L61).
- **`q3-how-many-kern-welten-and-alters`**: „Elf detaillierte Anteile“ with five named (L149–L155); four Kernwelten among „Sechs Realitätsebenen“, three listed (L173–L182).

**Not promoted:** the core protocols' other names (BPoF, EIC, ZTEM, RTSV — on aegis-teilfunktionen), Fragment 'O', Das Fundament, Paraiyas, Dialetheismus, the MESI protocol, Novelcrafter, NCP, the prose rules, Dramatica throughlines (Plan/storyform/ holds them).

**Two readers**, disjoint: (1) kael, alters, did, tsdp, multiplizitaet, lex, nyx, kiko, selene, juna, externe-ebene, emergenz and the record q3; (2) aegis, aegis-teilfunktionen, algorithmische-melancholie, entropie, guardians, kern-welten, konstrukt-stadt, realitaetsebenen, risse, ueberwelt, kishotenketsu, kohaerenz, cache-kohaerenz and the records c1, c9.
