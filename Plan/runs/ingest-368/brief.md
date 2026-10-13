# Brief — readings from document 367 (step 6)

1 document, one reader, one batch: `ingest-368`. Files go to `Plan/runs/ingest-368/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 367 | `strategy-of-fragmentation-a-narrative-implementation-plan-fo` | 2025-11-03 | „the fragmentation plan“ (an unsigned English narrative implementation plan) | plans the novel as a performative narrative: the coherence/correspondence conflict, a three-act „Triple Helix“ (Chapters 1-13, 14-26, 27-39), a Voice Protocol Matrix for Lex, Rhys, Nyx, Kiko, Moros and the AEGIS Protocols, three irreversible costs for Act II and four Gestalt principles; it calls itself „the definitive strategic blueprint“ — recorded, not applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (100 lines for `strategy-of-fragmentation-a-na`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan: write „the fragmentation plan plans / proposes …“, in its future tense; its claim to be definitive is recorded and not applied. Quote the English as written; cut before escaped emphasis and straight quotes. No gendered pronoun for Kael, Lex, Rhys, Nyx or Moros — use the names.

## Pages — document 367, `strategy-of-fragmentation-a-narrative-implementation-plan-fo`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L25, L26, L37, L38, L55, … (11 lines). central (3–6): AEGIS „Coherence instead of Truth“ against Kael (L25); the Coherence Theory of Truth, operationally closed and autopoietic, a defence born from the Genesis-Krise, classifying contradictory data (trauma, emotion, the Juna/V connection) as entropy or Rauschen (L26); in Act II misreading instability as a system error and triggering a reboot (L37); the AEGIS Protocols voice, cold and clinical, „Kael-Unit“, pathologising Kael's healing (L60).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L26. minor (1–3): Kael's integration of the contradictory truths held by the personality parts (Alters) (L26).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L26. minor (1–3): the Juna/V connection among the data AEGIS classifies as entropy (L26); the Moonshine-Link to the external figures Juna/V damaged with each cycle (L76); fragmented, static-filled messages from Juna/V as informational voids (L96).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L21, L25, L26, L34, L36, … (19 lines). central (3–6): the protagonist whose integration of a fragmented self mirrors the reader's assembly, a mind fractured by Tertiary Structural Dissociation (L17); „Coherence through Integration“, the Correspondence Theory of Truth (L25, L26); the three acts as Kael's Heroine's Journey, Act II cycles and Hero's Journey (L36–L38); the irreversible costs to System Kael (L74); the paradigm shift to integration, the Gardener role (L80).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L75, L95. minor (1–3): External World Decay: a permanent Riss or corruption in one of the Kernwelten (Core Worlds) per failed cycle (L75); a recurring glitch across different Kernwelten (L95).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L58. minor (1–3): Kiko (EP), the Terrified Child: a stream-of-consciousness rooted in terror, a traumatic Freeze state (L58).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence (see below).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L55, L56, L74, L94. minor (1–3): Lex (ANP), the Rationalist: analytical, detached, the flawed exclusionary logic of AEGIS's worldview (L55); possibly more rigid and paranoid with each cycle (L74); a Lex chapter placed beside an AEGIS log by proximity (L94).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L76. minor (1–3): Relational Erosion: the Moonshine-Link, the non-local intuitive connection to Juna/V, damaged with each cycle, fainter and harder to re-establish (L76).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L59. minor (1–3): Moros (EP), the Resigned/Collapse: an existential void, total psychic collapse and surrender to entropy, the counterpoint to Fight and Freeze (L59).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L57. minor (1–3): Nyx (EP), the Protector/Fight: aggressive, fragmented, the protective fury of a system under attack (L57).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L56, L74. minor (1–3): Rhys (ANP), the Caretaker: empathic, the Acceptance/Integration pole, foundational to the Gardener role (L56); the capacity for hope possibly diminished with each cycle (L74).
- **`risse`** (minor, 1–4): the census's surfaces — `glitch` L95. minor (1–3): a permanent Riss or corruption in one of the Kernwelten as a cost of the cycle (L75); a recurring glitch triggered by a specific trauma across Kernwelten and perspectives (L95).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L17, L88. minor (1–3): Kael's mind fractured by Tertiary Structural Dissociation of the Personality (TSDP) (L17); the narrative fragmented as Kael's mind is by TSDP (L88).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). `Genesis-Krise` is read on aegis as its trauma; `Juna/V` on juna; `Rauschen` (L26) is AEGIS's noise, read on aegis, not the Nichts Rauschen; `Tertiary Structural Dissociation of the Personality` is read on tsdp, not personas; `System Kael`, `Kael-Unit` on kael; `AEGIS Protocols` on aegis; `Riss` on risse; `Kohärenz Protokoll` the title.
- `juna`: `Juna/V` (near `juna`). `Genesis-Krise` is read on aegis as its trauma; `Juna/V` on juna; `Rauschen` (L26) is AEGIS's noise, read on aegis, not the Nichts Rauschen; `Tertiary Structural Dissociation of the Personality` is read on tsdp, not personas; `System Kael`, `Kael-Unit` on kael; `AEGIS Protocols` on aegis; `Riss` on risse; `Kohärenz Protokoll` the title.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). `Genesis-Krise` is read on aegis as its trauma; `Juna/V` on juna; `Rauschen` (L26) is AEGIS's noise, read on aegis, not the Nichts Rauschen; `Tertiary Structural Dissociation of the Personality` is read on tsdp, not personas; `System Kael`, `Kael-Unit` on kael; `AEGIS Protocols` on aegis; `Riss` on risse; `Kohärenz Protokoll` the title.
- `nichts-rauschen`: `Rauschen` (near `nichtsrauschen`). `Genesis-Krise` is read on aegis as its trauma; `Juna/V` on juna; `Rauschen` (L26) is AEGIS's noise, read on aegis, not the Nichts Rauschen; `Tertiary Structural Dissociation of the Personality` is read on tsdp, not personas; `System Kael`, `Kael-Unit` on kael; `AEGIS Protocols` on aegis; `Riss` on risse; `Kohärenz Protokoll` the title.
- `personas`: `Tertiary Structural Dissociation of the Personality` (near `persona`). `Genesis-Krise` is read on aegis as its trauma; `Juna/V` on juna; `Rauschen` (L26) is AEGIS's noise, read on aegis, not the Nichts Rauschen; `Tertiary Structural Dissociation of the Personality` is read on tsdp, not personas; `System Kael`, `Kael-Unit` on kael; `AEGIS Protocols` on aegis; `Riss` on risse; `Kohärenz Protokoll` the title.


**Pages not read:** `kohaerenz` (L11 the title), `genesis`, `nichts-rauschen`, `personas` — occurrences.

**Record entries:** none.

**Not promoted:** performative narrative, Triple Helix, Voice Protocol Matrix, functional multiplicity, irreversible costs and their three names, Gardener, narrative toolkit, ANP/EP labels; the borrowed concepts (theories of truth, Heroine's and Hero's Journey, Gestalt principles).

**One reader**: aegis, alters, juna, kael, kern-welten, kiko, lex, moonshine-link, moros, nyx, rhys, risse, tsdp.

**Chapter readings**: none — the plan gives only act ranges (Chapters 1-13, 14-26, 27-39, L36–L38) and no chapter's content, as for the dual-plot architecture.
