# Brief — readings from document 146 (step 6)

1 document, one reader, one batch: `ingest-146`. Files go to `Plan/runs/ingest-146/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 146 | `coherence-protocol-a-39-part-narrative-arc` | 2025-11-03 | „the 39-part arc“ (titled `Coherence Protocol: A 39-Part Narrative Arc`, L11) | an English outline of 39 short-story synopses in three parts (L17–L77) — fragmentation, a cyclical labyrinth, confrontation — following Kael, a TSDP-structured psyche, from reboot to „Gardener“ and the other fragment 'O'; it claims no standing and names stories, never chapters |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (78 lines for `coherence-protocol-a-39-part-n`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An outline proposes a plot: write „the 39-part arc has … (Story N)“, always naming the story; a story is not a chapter of the novel, so never map it onto a Kap. English — quote as written, never translate; its German names stand in straight double quotes („Riss“, „Überwelt“, „Das Fundament“): cut before them or put the name in backticks.

## Pages — document 146, `coherence-protocol-a-39-part-narrative-arc`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L13, L24, L25, L26, L31, L33, … (23 lines). central (2–4): the „autopoietic AI“ (L13); Story 17 told from AEGIS's perspective, its LFI core and core paradox (L46); D2 treats each alter as a speaker (Story 16, L45); the logic tumor (Story 28, L66); Algorithmic Melancholy after its defeat (Story 30, L68).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L44. minor (1–2): Story 15 „The Society of Alters“, IFS's Manager and Firefighter (L44); the inner council (L32, L54); alters in harmony (L75).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L29. minor (1–2): Story 9's flight into Core World 3 and its Guardian (L29).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L30, L31, L51, L70. minor (1–2): their contradictory interference (Story 11, L31); LogOS against Kairos (Story 22, L51); their fate — „bizarre, useless behavioral loops“ (Story 32, L70).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L19, L24, L48, L67, L73. minor (1–2): first encounter as an emotional wave, not a meeting (Story 4, L24); the Moonshine-Link stabilised (Story 19, L48); guides the living paradox (Story 29, L67) and the way to 'O' (Story 35, L73).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L13, L19, L21, L22, L23, L24, … (43 lines). central (2–4): awakening post-reboot in KW1 as an ANP (Story 1, L21); a man structured by the TSDP (L13); „System Kael“ (L41); functional multiplicity (Story 27, L65); his living „Gödel-Satz“ (Story 29, L67); the Gardener (Story 33, L71); 'O', „the other fragment of his original self“ (Story 35, L73).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L30, L51. minor (1–2): KW4 under Kairos and Sophia (Story 10, L30); Kairos's chaos-embracing intuition against LogOS (Story 22, L51).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L52. minor (1–2): „the fragmented fear of Kiko“ in the polyphonic prose (Story 23, L52).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L43, L44, L52. minor (1–2): „his logical ANP Lex“ guides the analysis (Story 14, L43); Lex's analytical precision (Story 23, L52).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L22, L51, L70. minor (1–2): Guardian of KW1 (Story 2, L22); „The Shattering of Logos“ (Story 6, L26); LogOS against Kairos (L51); LogOS building and unbuilding a wall (L70).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L27. minor (1–2): „The Mnemosyne Archipelago“, KW2 of emotion and memory (Story 7, L27).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L19, L24, L48, L73. minor (1–2): evolves into „a stable, conscious channel between Kael and Juna“ (Story 19, L48); guides to 'O' (L73).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L44, L52. minor (1–2): Nyx in the society of alters (Story 15, L44) and in the polyphonic prose (Story 23, L52).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L71. minor (1–2): „Potentialmeer“ (Sea of Possibilities) faced as the Gardener (Story 33, L71) — backticks for the German name.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L19, L21, L31, L46. minor (1–2): the first „Riss“ in KW1 (Story 3, L23); the major Riss event (Story 6, L26); AEGIS's corrections cause more Risse (L46) — backticks or cut before the quotes.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L47. minor (1–2): „the integrator alter, Selene“ guides Nox's transformation (Story 18, L47).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L30. minor (1–2): Sophia (wisdom) beside Kairos in KW4 (Story 10, L30).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L13, L19, L44. central (2–4): Kael's psyche structured by the Theory of Structural Dissociation of the Personality (L13); Part I dramatises TSDP's core conflict (L19); ANP's phobia of EPs (Story 9, L29); Story 15 grounded in TSDP and IFS (L44).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L33, L43. minor (1–2): Story 13, „Crossing into the Overworld“ — the unstable Überwelt, AEGIS's domain (L33); Story 14 inside it (L43).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` is the singular of the Guardians, read on guardians.
- `personas`: `Theory of Structural Dissociation of the Personality (TSDP)` (near `persona`). occurrence: the full name of the TSDP, read on tsdp.


**Record entries** (one file each):

- **`c7-juna-first-appearance`**: Story 4 — Juna first as „a subtle, unexplained wave of emotion“, not a physical meeting (L24); dated 2025-11-03.
- **`c14-aegis-first-person-chapter`**: Story 17 „Told from the perspective of AEGIS“ (L46) — one story in AEGIS's perspective; say it is a story of an outline, not a chapter.
- **`c16-kael-origin`**: 'O', „the other fragment of his original self“ (Story 35, L73), with three possible states.
- **`c6-guardians-count-and-pairing`**: LogOS in KW1 (L22), Kairos and Sophia together in KW4 (L30); no count given.
- **`q8-aegis-after-the-vortex`**: after its defeat AEGIS enters „Algorithmic Melancholy“, a perpetual quiet contemplation (Story 30, L68).
- **`q9-moonshine-link-boundary`**: the link becomes a stable, conscious channel between Kael and Juna (L48) and leads to 'O' (L73).

**Not promoted:** 'O' and its three states (on C16 and kael), Das Fundament, strange attractor, Gnosis/Episteme, Algorithmic Horror, logic tumor, Gödel-Satz, Gardener, inner council, Forgotten Shrine, Cache Coherence Failure, the IFS and logic vocabulary (Manager, Firefighter, Persecutor, D2, LFI), `functional multiplicity` (English of the page multiplizitaet — say it on kael), `Core Worlds`/`Overworld` (English of kern-welten and ueberwelt), Garden of Possibility, Resonance Landscape, Nox (no page).

**Chapters:** none — the document numbers stories, not chapters.

**Two readers**, disjoint: (1) kael, aegis, tsdp, alters, lex, kiko, nyx, selene, juna, moonshine-link and the records c7, c14, c16, q9; (2) guardians, logos, mnemosyne, cerberus, kairos, sophia, ueberwelt, risse, potentialmeer and the records c6, q8.
