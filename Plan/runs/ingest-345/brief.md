# Brief — readings from document 344 (step 6)

1 document, one reader, one batch: `ingest-345`. Files go to `Plan/runs/ingest-345/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 344 | `a-definitive-architectural-blueprint-of-the-kohaerenz-protok` | 2025-10-15 | „the architectural blueprint“ (an unsigned English analytical exposition titled „A Definitive Architectural Blueprint“) | an exposition of the novel in sections 1.0–6.3 — AEGIS as thesis, Kael as antithesis, a table of the alters, the Moonshine-Link and Das Fundament, a table of the four Kernwelten, the form of the novel and the Gödel-Gambit climax; its „Definitive“ recorded, not applied; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (143 lines for `a-definitive-architectural-blu`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analytical exposition in English: write „the architectural blueprint describes / says …“; it is its own account, not a decision. Quote the English as written. The alters table (L67–L77) gives a classification and function for each alter: one line per page. The Kernwelt names (Logos-Prime, Mnemosyne-Archipel, Cerberus-Labyrinth, Kairos-Potentialis) are worlds, not the Guardians of the same stems.

## Pages — document 344, `a-definitive-architectural-blueprint-of-the-kohaerenz-protok`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L19, L25, L27, L29, L33, … (27 lines). central (3–6): the novel's thesis embodied by AEGIS's worldview (L19); emerging from the Nichts Rauschen (L33); its self-definition „AEGIS is what AEGIS prevents from not being.“ (L35); misreading Kael's healing as entropy, Paradoxon X, ontological blindness (L43); its D2 module (L41); its methods (L49–L51); the climax forcing paraconsistent logic (L135) and its end as Algorithmic Melancholy (L137, L138).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L72. minor (1–3): the table's Alex as a calculated crisis manager (L72).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L63. minor (1–3): the section „The Society of Alters: A Functional Roster“ (L63) and the goal of co-consciousness among all alters (L81).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L31. minor (1–3): AEGIS's genesis and prime directive, an identity forged in opposition (L31, heading) and the Nichts Rauschen it emerged from (L33).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L125, L127, L135. minor (1–3): the climax framed as the Gödel-Gambit (L127); Kael as a living Gödel sentence (L131); AEGIS forced to adopt paraconsistent logic (L135).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L89. minor (1–3): Juna/V as the external anomaly, linked to Kael by the Moonshine-Link (L89, L91).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L21, L23, L41, L43, L50, L51, … (26 lines). central (3–6): Kael embodying emergent, bottom-up coherence (L23); classified as tertiary structural dissociation with AEGIS as externalised perpetrator introject (L61); the table's Kael managing daily life (L70); the goal functional multiplicity, co-consciousness, not fusion (L81); Kael's final state as a living Gödel sentence (L131); the conclusion (L142).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L50, L103, L105; `Kernwelt` L50, L103, L105, L109. minor (1–3): the Kernwelten as externalised psychological landscapes AEGIS creates (L50), functional psychological architectures (L105), and the table of four with their principles (L110–L113).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L75, L117. minor (1–3): the table's row for Kiko (L75) and Kiko's fragmented, paratactic syntax in the polyphonic prose (L117).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence (see below).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L41, L71, L117. minor (1–3): the table's Lex embodying cold logic (L71); „Lex asserts P“ in AEGIS's D2 module (L41); Lex's sentences in the polyphonic prose (L117).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L89, L91. minor (1–3): the Moonshine-Link as the primary catalyst for change (L91), a non-local, sub-protocollar connection AEGIS cannot see (L91), felt as a wave, hot and painful (L91).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L76. minor (1–3): the table's Moros as the frozen EP, the deepest trauma response of collapse (L76).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L33. minor (1–3): AEGIS emerging from the „Nichts Rauschen“, an acoustic pressure without sound (L33).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L41, L74, L117. minor (1–3): the table's row for Nyx (L74); Nyx asserting not-P in the D2 module (L41); Nyx's syntax in the polyphonic prose (L117).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L73. minor (1–3): the table's Rhys as the caregiver ANP, mediating and nurturing (L73).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L77. minor (1–3): the table's Selene as the Internal Self Helper, mediator of the system's potential for healing (L77).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L61, L69. minor (1–3): Kael rigorously modelled on TSDP (L61); the table's ANP/EP classes (L69).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L45. not read: an occurrence (see below).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: the Kernwelt names are worlds, not the Guardians of the same stems; `Inkohärenz` generic; the TSDP's full name is read on tsdp, not personas; `Juna/V` is read on juna.
- `juna`: `Juna/V` (near `juna`). occurrence: the Kernwelt names are worlds, not the Guardians of the same stems; `Inkohärenz` generic; the TSDP's full name is read on tsdp, not personas; `Juna/V` is read on juna.
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: the Kernwelt names are worlds, not the Guardians of the same stems; `Inkohärenz` generic; the TSDP's full name is read on tsdp, not personas; `Juna/V` is read on juna.
- `kohaerenz`: `Inkohärenz` (near `koharenz`). occurrence: the Kernwelt names are worlds, not the Guardians of the same stems; `Inkohärenz` generic; the TSDP's full name is read on tsdp, not personas; `Juna/V` is read on juna.
- `logos`: `Logos-Prime` (near `logos`). occurrence: the Kernwelt names are worlds, not the Guardians of the same stems; `Inkohärenz` generic; the TSDP's full name is read on tsdp, not personas; `Juna/V` is read on juna.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: the Kernwelt names are worlds, not the Guardians of the same stems; `Inkohärenz` generic; the TSDP's full name is read on tsdp, not personas; `Juna/V` is read on juna.
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`). occurrence: the Kernwelt names are worlds, not the Guardians of the same stems; `Inkohärenz` generic; the TSDP's full name is read on tsdp, not personas; `Juna/V` is read on juna.


**One page beyond the draft:** `algorithmische-melancholie` (minor, 1–3): AEGIS's final, tragic state as „Algorithmic Melancholy“ (L138), processing the truth without experiencing it — the English name for the page's term.

**Pages not read:** `kohaerenz` (L11 the title), `ueberwelt` (L45 a heading on AEGIS's simulation methods) — occurrences.

**Record entries:** none.

**Not promoted:** Paradoxon X as named here, the D2 module, Paraiyas, polyphonic prose, the Protocol of the Reader, ineffiziente Schönheit; the borrowed concepts (Principle of Explosion, prehension, qualia, paraconsistent logic, IIT).

**One reader**: aegis, kael, alex, alters, genesis, goedel-gambit, juna, kern-welten, kiko, lex, moonshine-link, moros, nichts-rauschen, nyx, rhys, selene, tsdp, algorithmische-melancholie.

**Chapter readings**: none — the exposition names no chapter or part of the novel.
