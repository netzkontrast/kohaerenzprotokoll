# Brief — readings from document 357 (step 6)

1 document, one reader, one batch: `ingest-358`. Files go to `Plan/runs/ingest-358/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 357 | `an-introduction-to-the-concepts-of-coherence-protocol` | 2025-11-03 | „the concepts introduction“ (an unsigned English orientation text) | introduces a newcomer to the novel's key players and concepts in six sections: AEGIS's Logic of Exclusion against Kael's Logic of Integration, AEGIS, Kael's alters in a table, the four Kernwelten, Juna/V and the Moonshine-Link, Das Fundament; no source, date or canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (103 lines for `an-introduction-to-the-concept`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An orientation text: write „the concepts introduction describes …“; it is a reader's guide, deciding nothing. Quote the English as written; cut before straight quotes, bold marks and table escapes. The Kernwelt names are worlds, not the Guardians. For Juna/V use the name, not a pronoun.

## Pages — document 357, `an-introduction-to-the-concepts-of-coherence-protocol`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L23, L26, L28, L30, L32, L34, … (20 lines). central (3–6): its Logic of Exclusion, order only by eliminating all contradictions (L23); the primary antagonist (L30); its purpose to maintain order by minimising entropy, born from a chaotic Sea of Potentiality, its destructive acts the result of its flawed programming (L34); its rigid control making chaos, the Risse (L45).
- **`alters`** (minor, 1–4): the census's surfaces — `alters` L55. minor (1–3): the parts called alters (L55), the table header „Key Part (Alter)“ (L63).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L55. minor (1–3): Kael's dissociative identity structure, abbreviated DID (L55).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L90, L92. minor (1–3): Juna/V as an external entity or anomaly outside AEGIS's control (L92) and the coherence of connection it represents (L92).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L24, L45, L47, L49, L51, L55, … (17 lines). central (3–6): the Logic of Integration, holding true contradictions without collapse (L24); a dissociative identity structure, the goal functional multiplicity, a state of inner harmony (L55); Kael (Host) managing everyday life (L64).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L72, L74. minor (1–3): the Kernwelten as sophisticated simulated realities created by AEGIS, externalised psychological landscapes (L74); the table of four (L79–L82).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L67. minor (1–3): Kiko (The Child) in the alters table (L67).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: an occurrence (see below).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L65. minor (1–3): Lex (The Analyst) in the alters table (L65).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L92. minor (1–3): the Moonshine-Link as a bond of resonance and empathy (L92).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L66. minor (1–3): Nyx (The Protector) holding the trauma-response of righteous anger and aggressive defence (L66).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L45. minor (1–3): the glitches named Risse where AEGIS's rigid control makes chaos (L45).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L68. minor (1–3): Selene (The Integrator) in the alters table (L68).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alex`: `ontological exploit` (near `alex`). occurrence: the Kernwelt names are worlds, not the Guardians; `ontological exploit` is read on juna or aegis, not alex; `Kohärenz Protokoll` is the title.
- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: the Kernwelt names are worlds, not the Guardians; `ontological exploit` is read on juna or aegis, not alex; `Kohärenz Protokoll` is the title.
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: the Kernwelt names are worlds, not the Guardians; `ontological exploit` is read on juna or aegis, not alex; `Kohärenz Protokoll` is the title.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the Kernwelt names are worlds, not the Guardians; `ontological exploit` is read on juna or aegis, not alex; `Kohärenz Protokoll` is the title.
- `logos`: `Logos-Prime` (near `logos`). occurrence: the Kernwelt names are worlds, not the Guardians; `ontological exploit` is read on juna or aegis, not alex; `Kohärenz Protokoll` is the title.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: the Kernwelt names are worlds, not the Guardians; `ontological exploit` is read on juna or aegis, not alex; `Kohärenz Protokoll` is the title.


**Pages not read:** `kohaerenz` (L15 the title) — an occurrence.

**Record entries:** none.

**Not promoted:** Logic of Exclusion and Logic of Integration as labels, Sea of Potentiality, the table headers, ontological exploit, the lens concepts.

**One reader**: aegis, kael, alters, did, juna, kern-welten, kiko, lex, moonshine-link, nyx, risse, selene.

**Chapter readings**: none.
