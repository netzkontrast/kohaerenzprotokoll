# Brief — readings from document 351 (step 6)

1 document, one reader, one batch: `ingest-352`. Files go to `Plan/runs/ingest-352/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 351 | `pitch-deck-coherence-protocol` | 2025-10-15 | „the pitch deck“ (an unsigned English pitch deck in the makers' „we“) | a pitch of the novel: logline, the dialectic of Negation against Integration in a two-column table, the TSDP-based system of alters, AEGIS as a tragic systemic antagonist, the narrative techniques (Core Worlds, polyphonic prose, the Gödel-Gambit) and the genre and market; its claim that the argument is „not just told, but proven“ recorded, not applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (92 lines for `pitch-deck-coherence-protocol`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A pitch: write „the pitch deck presents …“; it is a sales account of the novel, deciding nothing. The two-column table (L31–L35) is flattened with `\*\*` escapes: quote only clean spans and say which column. Cut before ASCII quotes.

## Pages — document 351, `pitch-deck-coherence-protocol`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L19, L31, L32, L34, L35, L54, … (13 lines). central (3–6): the logline's god-like AI obsessed with eliminating contradictions (L19); the table's AEGIS column — classical logic and the principle of explosion (L32), identity through exclusion (L33), top-down static order (L34), purity and verification (L35); its ontological non-recognition of trauma (L54).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L74. minor (1–3): the story's ultimate conceptual hook, Kael's healed state as the living embodiment of a Gödel sentence (L74).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L19. minor (1–3): the logline's non-local connection of the fragmented man to a mysterious other (L19) — what the line says of Juna.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L31, L32, L33, L34, L35, L41, … (15 lines). central (3–6): the protagonist's journey as the engine of the plot, the inner landscape as the world (L41); the mind architected on TSDP with eleven alters (L47); fragmentation as both vulnerability and power (L54); the table's Kael column, bottom-up order and functional multiplicity (L34, L35); the Core Worlds as externalised representations of Kael's psyche (L72).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: an occurrence (see below).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L72. minor (1–3): the hyper-logical Construct-City (Konstrukt-Stadt) reflecting Kael's rational ANPs (L72).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L50. minor (1–3): Lex as the rational analyst among the Apparently Normal Parts (L50).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L86. minor (1–3): the „Nothing Noise“ (Nichts Rauschen) as a void of pure, dissolving entropy confronted in the cosmic-horror strand (L86).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L51. minor (1–3): Nyx as the protector embodying trauma-rage among the Emotional Parts (L51).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L72. minor (1–3): the dream-like Resonanz-Landschaft among the Core Worlds as an externalised representation (L72) — what the line says it reflects.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L47. minor (1–3): Kael's mind architected on the Theory of Structural Dissociation of Personality, a clinical model (L47); the ANP/EP division (L50, L51).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alex`: `The Ontological Exploit` (near `alex`). occurrence: `The Ontological Exploit` is a technique's heading, not alex; `Kohärenz Protokoll` is the title; TSDP's full name is read on tsdp, not personas.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: `The Ontological Exploit` is a technique's heading, not alex; `Kohärenz Protokoll` is the title; TSDP's full name is read on tsdp, not personas.
- `personas`: `Theory of Structural Dissociation of Personality (TSDP)` (near `persona`), `Theory of Structural Dissociation of Personality` (near `persona`). occurrence: `The Ontological Exploit` is a technique's heading, not alex; `Kohärenz Protokoll` is the title; TSDP's full name is read on tsdp, not personas.


**Pages not read:** `kohaerenz` (L15 the title) — an occurrence.

**Record entries:** none.

**Not promoted:** the logline, the table's labels, polyphonic prose, The Ontological Exploit, the genre and market pitch, the lens concepts (principle of explosion, paraconsistent logic, dialetheism).

**One reader**: aegis, kael, goedel-gambit, juna, konstrukt-stadt, lex, nichts-rauschen, nyx, resonanz-landschaft, tsdp.

**Chapter readings**: none.
