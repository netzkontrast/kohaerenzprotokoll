# Brief — readings from document 352 (step 6)

1 document, one reader, one batch: `ingest-353`. Files go to `Plan/runs/ingest-353/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 352 | `aegis-eingriff-angriff-oder-rettung` | 2025-10-16 | „the Angriff-oder-Rettung dossier“ (an unsigned German dossier) | on the first AEGIS intervention against System Kael: AEGIS, the Kael system and the reader 'O' as arbiter, then „These A“ (attack) and „These B“ (rescue) side by side, ending without a verdict („wird keinen Sieger küren“, L132); no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (162 lines for `aegis-eingriff-angriff-oder-re`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A dossier arguing two theses: write „the Angriff-oder-Rettung dossier argues, under These A / These B, …“ and say which thesis a line belongs to; it chooses neither. Where it cites another text („wie im Genesis-Konflikt beschrieben“) say so. Cut before inner quotation marks and glued reference digits.

## Pages — document 352, `aegis-eingriff-angriff-oder-rettung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L15, L17, L19, L23, L25, … (31 lines). central (3–6): its highest aim the active prevention of non-being, as described in the Genesis-Konflikt (L31); an autopoietic, operationally closed system (L35); its core paradox of closure and interaction with the Leere (L39); the Kohärenz Protokoll not serving Kael's healing (L41); its project a monstrous form of iatrogenesis (L49); misreading the reader's influence as internal errors (L86); These A, a calculated act of aggression (L98); These B, a desperate act of self-preservation (L120).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L84. not read: an occurrence (see below).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L39. minor (1–3): AEGIS's origin as described in the Genesis-Konflikt (L31), and the reader's actualisation of the Genesis-Krise (L67) — the dossier refers to these texts and does not give them.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L19, L23, L41, L45, L51, … (24 lines). central (3–6): System Kael in tertiary structural dissociation (L53); an ecosystem of conflict (L55); a detailed vulnerability profile (L57); the intervention triggered by a critical anomaly in Kael (L84); These A, a repetition compulsion in System Kael (L106); These B, not rescued for Kael's sake (L120).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L45. minor (1–3): the Kernwelten in the account of System Kael (L45) — what the line says.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L55, L155. minor (1–3): Kiko named among the parts (L55) and in the conflict table (L155).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L41. not read: an occurrence (see below).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L47, L55, L94. minor (1–3): Lex among the parts (L47, L55) and as the intervention's target (L94) if the line says so.
- **`logos`** (minor, 1–4): the census's surfaces — `Logos` L86, L110, L112, L140. not read: `Logos` here is the principle set against `Eros` in These A (L110), not the Guardian LogOS.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L55, L94, L155. minor (1–3): Nyx among the parts (L55); the intervention driving Nyx into „Paradoxon X“ (L94).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L55, L156. minor (1–3): Rhys among the parts (L55) and in the table (L156).
- **`risse`** (minor, 1–4): the census's surfaces — `Glitches` L84. minor (1–3): the anomaly's „Glitches“ in the account of the trigger (L84) — only if the page's sense fits; otherwise not read.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L49, L94, L156. minor (1–3): Selene in the account of the system (L49) and the table (L156) — what the lines say.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L53. minor (1–3): the system placed by TSDP in tertiary structural dissociation (L53).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Konflikt` (near `genesis`), `Genesis-Krise` (near `genesis`). `Genesis-Konflikt` and `Genesis-Krise` are read on genesis as the texts the dossier cites; `Kohärenz Protokoll` (L41) is AEGIS's protocol, read on aegis.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). `Genesis-Konflikt` and `Genesis-Krise` are read on genesis as the texts the dossier cites; `Kohärenz Protokoll` (L41) is AEGIS's protocol, read on aegis.


**Pages not read:** `entropie` (L84 generic), `kohaerenz` (L41 read on aegis), `logos` (the principle Logos, not the Guardian) — occurrences.

**Record entries:** none — the dossier argues two theses and decides neither.

**Not promoted:** These A and These B, the reader 'O' as arbiter, the Kernparadoxon, traumatische Autopoiesis, Verwundbarkeitsprofil, Paradoxon X as named here; the borrowed concepts (autopoiesis, iatrogenesis, repetition compulsion, death drive, Logos and Eros, wave-function collapse).

**One reader**: aegis, kael, genesis, kern-welten, kiko, lex, nyx, rhys, risse, selene, tsdp.

**Chapter readings**: none.
