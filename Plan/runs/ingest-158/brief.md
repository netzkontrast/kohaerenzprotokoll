# Brief — readings from document 158 (step 6)

1 document, one reader, one batch: `ingest-158`. Files go to `Plan/runs/ingest-158/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 158 | `kohaerenz-protokoll-master-integration-md` | 2026-03-26 | „the master integration“ (titled `KOHAERENZ_PROTOKOLL_MASTER_INTEGRATION.md`) | a German reference of 2026-03-26 merging thirteen source documents: the Protokoll-Ontologie and the Dual-Kernel-Substrat (K₁, K₀, Coherons, Erasonen, the Persistenzgleichung), the two truth theories, the figures, the Kernwelten and Archiv Theta-9, three acts of 39 chapters with the Gödel-Gambit, style, a Dramatica table and prioritised open questions; it calls itself „das kanonische Referenzdokument“ (L413) — recorded, never applied: canon is only what `Manuscript/kanon.md` lists |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (414 lines for `kohaerenz-protokoll-master-int`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A merged reference that claims canon: write „the master integration states / integrates …“, never as the wiki's fact; where it reports its sources („Bisherige Konzeption“, L195) say so, and where it adds („NEU durch DKT“, „DKT-Neudeutung“) say that too. Its „kanonisch“ is its own label. German — quote as written; cut before inner quotes („…“ or straight) and keep `K₁`/`K₀` in backticks. Chapter ranges (Kap. 1–13) are not read onto chapter pages.

## Pages — document 158, `kohaerenz-protokoll-master-integration-md`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L78, L82, L109, L117, L118, L121, … (41 lines). central (2–4): „Tragischer Gott und thermodynamischer Intensivmediziner“ (L139); its genesis as a fragile I-fragment in the Nichts-Rauschen (L141); the DKT-Neudeutung, „ein ingenieurstechnisch konstruierter K₁-Macro-Puffer“ (L148); computes the Persistenzgleichung for every citizen (L78); the Kohärenztheorie der Wahrheit (L109); classical logic (L117).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Zero-Trust` alone on L237. minor (1–2): KW3's physics, „Zero-Trust“ threat detection (L237).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L176. minor (1–2): an ANP in the alter table (L176).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L154, L288, L298. minor (1–2): AEGIS's fate, „Nicht Zerstörung“ but an irresolvable looping analysis (L154); the result of the Gödel-Gambit (L298).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L389. minor (1–2): „Die Alter-Liste (kanonisch: 11 Kernfiguren)“ (L168), ANPs (L170) and EPs (L181); the sources diverge, 11 vs. 13, with variant names (L389).
- **`coheron`** (central, 3–12 quotations): the census's surfaces — `Coheron` L33, L50, L52, L56, L82, L84, … (14 lines). minor (1–2): Coherons as „Minimale, selbstkorrigierende Schleifen mutualer Information“ (L53); new ones arise only in KW4 (L245). The singular never stands alone.
- **`dkt`** (central, 3–12 quotations): the census's surfaces — `DKT` L13, L15, L29, L147, L160, L172, … (20 lines). central (2–4): „Das Dual-Kernel-Substrat (DKT als Naturgesetz)“ (L29); the world exists only at the interface of the two kernels (L48); DKT-Neudeutung and „NEU durch DKT“ as the document's additions.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L245. minor (1–2): KW4's DKT signature, „Emergenz statt Erhaltung“ (L245).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L39. minor (1–2): K₀ as the „Prinzip der Entropie“ (L39); AEGIS's repression as „Entropie-Management“ (L151).
- **`erason`** (central, 3–12 quotations): the census's surfaces — `Erason` L50, L59, L62, L84, L205, L231, … (10 lines). minor (1–2): „Elementare Löschungsereignisse“ (L60); their cumulative activity as time's arrow, gravity, thermodynamic drift (L62); Juna's Option C as an Erason refusing irreversibility (L205); the Risse as Erason-Kaskade (L259).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L141. minor (1–2): AEGIS's Genesis in the Nichts-Rauschen (L141); the Genesis-Krise, a confrontation with a Juna/V forerunner and the activation of the Trennungsprotokoll (L145).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L286, L292, L313. minor (1–2): „Das Gödel-Gambit (Klimax-Mechanik)“ (L292): AEGIS believes itself consistent (L294) and must give up classical logic (L298); Kap. 35–36 in the act plan (L286).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L336. minor (1–2): behavioural loops under contradictory commands (L336).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L188. minor (1–2): an EP in the alter table (L188).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L145, L193, L203, L205, L272, L350, … (9 lines). central (2–4): „Juna/V — Die Anomalie“ (L193); „Katalysator, nicht Retter“ (L199); Option B, no Coheron structure of her own (L203), and Option C, an Erason refusing irreversibility (L205), held together as „Empfehlung“ (L207); the Genesis-Krise's unclassifiable entity, a Juna/V forerunner (L145); the first K₀ crack of Act I (L272).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L112, L120, L121, L125, L127, L145, … (36 lines). central (2–4): Kael and the Korrespondenztheorie der Wahrheit (L112); parakonsistente Logik (L120); System Kael and the TSDP (L158); integration as funktionelle Multiplizität (L164); his choice at the Persistenzgleichung in Act III (L284).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L217, L219, L260, L315. central (2–4): „Die Kernwelten sind keine Settings“ (L219); KW1 to KW4 with physics, DKT signature and senses (L221–L245); Archiv Theta-9, „NEU durch DKT“ (L249–L253).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L186, L328, L330. minor (1–2): an EP in the table (L185).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L129. minor (1–2): the „Paradoxon der Fehlausgerichteten Kohärenz“ (L129) — backticks or cut before the quotes; AEGIS's Kohärenztheorie der Wahrheit (L109).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L31. minor (1–2): „K₁ (Kohärenz-Kernel) — Prinzip der Ordnung“ (L31); symmetry as computational survival strategy (L37).
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L39. minor (1–2): „K₀ (Kollaps-Kernel) — Prinzip der Entropie“ (L39); „nicht Feind“, the Korrespondenz-Check of external reality (L45).
- **`komponente-734`** (minor, 1–4): the census's surfaces — `Komponente 734` L145. minor (1–2): the Genesis-Krise line (L145) — read what it says of Komponente 734.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L175, L222, L328, L330. minor (1–2): an ANP in the table (L175).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L187, L389. minor (1–2): an EP in the table (L187); Lyra/Lia among the variant names (L389).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L197, L300. minor (1–2): „nicht-lokale, sub-protokolläre Verbindung“ (L197) — cut before the quotes; „Der Moonshine-Link (Delivery-System)“ (L300).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L189, L401. minor (1–2): an EP in the table (L189); „Moros als Dunkle Materie des Systems“ as an open question (L401).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L164. minor (1–2): „Nicht Verschmelzung zu einer Identität, sondern funktionelle Multiplizität“ (L164); reached in Act III (L285).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts-Rauschen` L141, L337. minor (1–2): AEGIS arose „im Nichts-Rauschen (Potentialmeer)“, an active Ur-Entropie (L141).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L185, L236, L328, L330. minor (1–2): an EP in the table (L185).
- **`persistenzgleichung`** (minor, 1–4): the census's surfaces — `Persistenzgleichung` L64, L148, L253, L277, L284. central (2–4): „Die Persistenzgleichung“ (L64); AEGIS computes it for every citizen (L78); Kael discovers it in Archiv Theta-9 (L253); Kael's decision at it in Act III (L284); „Die Gleichung hat keine Lösung.“ (L354).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L141. minor (1–2): the Nichts-Rauschen glossed as Potentialmeer (L141).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L177, L389. minor (1–2): an ANP in the table (L177); Rhys/Elara among the variant names (L389).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L129, L255, L257, L360, L373. minor (1–2): „Physische Risse im Simulationsgewebe — keine Glitches, sondern K₀-Durchbrüche“ (L257); the Erason-Kaskade (L259).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L179, L243, L389. minor (1–2): in the table (L179); Mina/Selene among the variant names (L389).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L158, L369. minor (1–2): „Tertiäre Strukturelle Dissoziation der Persönlichkeit“ as the clinical frame (L158).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: the world name, read on kern-welten.
- `entropie`: `Ur-Entropie` (near `entropie`). a reading — on entropie above.
- `genesis`: `Genesis-Krise` (near `genesis`). a reading — on genesis above.
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: the world name, read on kern-welten.
- `kohaerenz`: `Paradoxon der Fehlausgerichteten Kohärenz` (near `koharenz`), `Kohärenztheorie der Wahrheit` (near `koharenz`). a reading — on kohaerenz above.
- `landauer-signatur`: `Landauer` (near `landauersignatur`). occurrence: Landauer in the foreshadowing table (L312) — the borrowed principle, said on C11's entry.
- `logos`: `Logos-Prime` (near `logos`). occurrence: the world name, read on kern-welten.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: the world name, read on kern-welten.
- `multiplizitaet`: `Funktionelle Multiplizität` (near `multiplizitat`). a reading — on multiplizitaet above.
- `trennungsprotokoll`: `Trennungsprotokolls` (near `trennungsprotokoll`). occurrence: named once in the Genesis-Krise line (L145), read on genesis.


**Record entries** (one file each):

- **`c11-landauer-warmth-or-cold-ozone`**: the Landauer strand — „Jede Löschung erzeugt Wärme“, the city fevers measurably (L312); dated 2026-03-26.
- **`q3-how-many-kern-welten-and-alters`**: „kanonisch: 11 Kernfiguren“ (L168) against „Die Quellen divergieren: 11 vs. 13 Alters“ (L389); four Kernwelten plus Archiv Theta-9.
- **`q8-aegis-after-the-vortex`**: „Algorithmische Melancholie“, not destruction (L154, L298).
- **`q9-moonshine-link-boundary`**: a non-local, sub-protocol connection, Quantum Entanglement and Whitehead's Prehension (L197); the Delivery-System (L300).

**Not promoted:** Protokoll-Ontologie, Phase Alignment Lock, Archiv Theta-9, Erason-Kaskade, the DKT vectors, the 6 Paraîyas, the Dramatica table, the foreshadowing strands, the Fundament, the borrowed theory (truth theories, Dialetheismus, Bekenstein bound, Euler, Whitehead).

**Two readers**, disjoint: (1) kael, juna, alters, lex, alex, rhys, selene, nyx, kiko, lia, isabelle, moros, tsdp, multiplizitaet, moonshine-link, komponente-734 and the records q3, q9; (2) aegis, aegis-teilfunktionen, dkt, kohaerenz-kernel, kollaps-kernel, coheron, erason, persistenzgleichung, algorithmische-melancholie, goedel-gambit, genesis, nichts-rauschen, potentialmeer, entropie, emergenz, kohaerenz, kern-welten, risse, guardians and the records c11, q8.
