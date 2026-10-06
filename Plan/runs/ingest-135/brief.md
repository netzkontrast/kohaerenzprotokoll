# Brief — readings from document 135 (step 6)

1 document, one reader, one batch: `ingest-135`. Files go to `Plan/runs/ingest-135/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 135 | `plot-generation-framework-for-the-coherence-protocol` | 2025-11-03 | „the plot framework“ (titled `Plot Generation Framework for "The Coherence Protocol"`, L11) | an English outline of 2025-11-03 giving two 39-part architectures of one story: a „Narrative Mosaic“ of 39 stories, each with Core Concept, Assigned POV and Summary (L15–L227), and a linear „Novel Plot“ of 39 chapters, one commission each (L229–L285), both in three acts of 13; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (286 lines for `plot-generation-framework-for-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An outline proposes: write „the plot framework assigns / plans …“; it is English — quote as written, never translate; distinguish the Mosaic's stories („Story N“) from the Novel Plot's chapters („Chapter N“). Inner straight quotes ("Moonshine-Link", "Ursprungs-Ich", "living Gödel-Satz") — cut before them. --find drops digits: cut before „Kernwelt 1“ digits. Kael is male. Chapter pages are done by the session.

## Pages — document 135, `plot-generation-framework-for-the-coherence-protocol`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L13, L36, L37, L51, L52, L57, … (51 lines). central (2–4): AEGIS System Logs as POV (L36, L52); Chapter 14's POV „AEGIS's core logic (Component 734)“ (L255); the transformed remnant of AEGIS in a new dialogue (Chapter 38); the Genesis-Krise log (Chapter 32).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Zero-Trust` L118, L122, L260. minor (1–2): Zero-Trust: Chapter 19 „The Zero-Trust Fortress“ with Cerberus (L260); L118, L122.
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L32, L141, L142. minor (1–2): find Alex's lines (L32, L141) — what the framework gives him.
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L81, L82, L156, L157, L248, L267. minor (1–2): Chapter 12: „the observer part, Argus“ (L246); Chapter 26 Argus pieces the clues together (L267).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L121, L122, L260. minor (1–2): Chapter 19: Cerberus, Guardian of Kernwelt 3 (L260); but Story POV „The Chaos-Regulator (Guardian of Kernwelt“ 3) (L136) — record both, do not merge.
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L201, L202. minor (1–2): Story 34's POV, „a part who understands power dynamics“ (L202).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L57, L61, L62, L117, L132, L152, … (7 lines). minor (1–2): Kael's „intuitive connection to Juna/V“ (L57); Act I „catalyzed by the mysterious connection to Juna/V“ (L234).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L13, L17, L21, L26, L27, L37, … (65 lines). central (2–4): Chapter 1 „The Host's Burden“ (L235); the climax embodying a living Gödel-Satz (L280) — cut before the straight quote; „The Gardener“ (L211, L282) — say it is the framework's name for his role.
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L126, L261. minor (1–2): Chapter 20: „Kairos/Sophia, the Guardian of Kernwelt“ 4 (L261); also „The Possibility-Weaver (Guardian of KW4)“ (L166) — record both.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L41, L42, L240. minor (1–2): Chapter 4: a traumatic intrusion „from a child-part, Kiko“ (L238).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. occurrence: the project's name (L13, J9).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L31, L32, L42, L142, L238. minor (1–2): Chapter 2 „Introduce Lex's cold, logical control“ (L236).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L66, L67, L245. minor (1–2): Chapter 9: Lia shifting from fear to longing (L243).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L101, L102, L256. minor (1–2): Chapter 15: „LogOS, the Guardian of Kernwelt“ 1 (L256) — cut before the digit.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L106, L107, L257. minor (1–2): Chapter 16: Mnemosyne, Guardian of Kernwelt 2, dialetheic logic (L257).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L52, L55, L67, L132, L242, L243. minor (1–2): Chapter 7 establishes it „as a real plot device and a source of ho“pe — find the line (L242); foreshadowed in Chapter 6 (L241).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L196, L197, L279. minor (1–2): Chapter 33: Kael's deepest despair (Moros) (L279).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L147. minor (1–2): L147 — what it says.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L76, L77, L247. minor (1–2): Chapter 11: „the aggressive protector, Nyx“ (L245).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L145, L147, L265. minor (1–2): „The cosmic horror of the“ Potentialmeer (Sea of Potentiality) (L145); beyond a Riss (L147); revealed in Chapter 24 (L265).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L46, L47, L67, L151, L152, L241. minor (1–2): Chapter 5 introduces Rhys, compassion (L239).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L146. minor (1–2): a Guardian stationed at a Riss in the simulation's fabric (L147) — cut before the straight quote.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L71, L72. minor (1–2): find Selene's lines (L71–L72).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L126, L261. minor (1–2): the same lines (L126, L261).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L25, L70. minor (1–2): „Tertiary Structural Dissociation (TSDP)“ (L25).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L97, L206. minor (1–2): the Überwelt simulation maintained by Component 734 (L97); „The Überwelt Simulation Core“ as POV (L206).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). a reading, minor (1), by Reader 1: Chapter 32, Kael uncovers „the log detailing AEGIS's“ Genesis-Krise (L278).
- `kern-welten`: `Kernwelt 1` (near `kernwelt`), `Kernwelt 2` (near `kernwelt`), `Kernwelt 3` (near `kernwelt`), `Kernwelt 4` (near `kernwelt`). a reading, minor (1–2), by Reader 1: the Guardians of Kernwelt 1–4 (L101, L106, L121, L126) and two more Guardians named for KW3 and KW4 (L136, L166).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence (J9).


**Record entries** (one file each):

- **`q7-what-734-names`**: „Component 734 (AEGIS Core Logic)“ (L96), the AEGIS component „that was once its“ Ursprungs-Ich (L97); Chapter 14's POV (L255) — 734 names an AEGIS component here.
- **`c14-aegis-first-person-chapter`**: Story 14 and Chapter 14 told from AEGIS's core logic (L96, L255); AEGIS logs as POV (L36) — dated 2025-11-03.
- **`c6-guardians-count-and-pairing`**: one Guardian per Kernwelt (LogOS 1, Mnemosyne 2, Cerberus 3, Kairos/Sophia 4) and, in the Mosaic, the Chaos-Regulator for Kernwelt 3 (L136) and the Possibility-Weaver for KW4 (L166) — the framework does not say whether these are the same.
- **`q8-aegis-after-the-vortex`**: AEGIS's axioms dissolve (Chapter 35); a dialogue with „the transformed remnant of AEGIS“ (Chapter 38).

**Not promoted:** Narrative Mosaic, Qualia-Space, Chaos-Regulator, Possibility-Weaver (on C6), The Gardener (on kael), IFS, dialetheism, Hero's/Heroine's Journey.

**Split into two readers, at the same time on disjoint pages:**
- Reader 1: aegis, aegis-teilfunktionen, ueberwelt, logos, mnemosyne, cerberus, kairos, sophia, kern-welten, potentialmeer, nichts-rauschen, risse, genesis, juna, moonshine-link, and the entries q7, c14, c6, q8.
- Reader 2: kael, lex, rhys, kiko, lia, nyx, argus, moros, isabelle, alex, selene, tsdp.
