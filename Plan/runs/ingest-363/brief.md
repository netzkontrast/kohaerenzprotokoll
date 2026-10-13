# Brief — readings from document 362 (step 6)

1 document, one reader, one batch: `ingest-363`. Files go to `Plan/runs/ingest-363/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 362 | `objectivity-in-the-kohaerenz-protokoll-universe-a-thematic-g` | 2025-11-03 | „the objectivity guide“ (an unsigned English thematic essay) | reads objectivity in the novel as a conflict between AEGIS's coherence-based, algorithmic view and Kael's trauma as correspondence-based external fact, applying real-world epistemology (standpoint theory, Gödel, confirmation bias); no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (96 lines for `objectivity-in-the-kohaerenz-p`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A thematic guide: write „the objectivity guide reads …“; its readings of the figures are its own interpretation („literalizes“), deciding nothing. Quote the English as written; cut before straight quotes and table escapes. The Kernwelt names are worlds, not Guardians.

## Pages — document 362, `objectivity-in-the-kohaerenz-protokoll-universe-a-thematic-g`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L25, L27, L31, L39, L41, … (19 lines). central (3–6): a sterile, algorithmic objectivity based on internal consistency (L15); the coherence theory of truth assigned to it (L25) and what it treats as entropy (L25); its tragic flaw, a supposedly objective system blinded by its own subjectivity (L31); the table of its four methods (L48–L51).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L55. minor (1–3): the alters in the guide's account of Kael's TSDP structure (L55) — what the line says.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L73. minor (1–3): Juna/V in the guide's account (L73) — what the line says.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L27, L48, L53, L55, L57, … (13 lines). central (3–6): a fragmented consciousness whose traumatic memories are an undeniable external reality (L15); memories as disruptive, objective facts (L27); a mind structured by TSDP (L55); the path to objectivity as synthesis, not choice (L57).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L61. minor (1–3): the Kernwelten as the guide reads them: KW1 empowering Lex, KW2 a fluid trauma-landscape, a false balance (L61).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence (see below).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L57, L61. minor (1–3): the conflict between the rational part Lex and the protector Nyx as a trial (L57); KW1 empowering the rational alter Lex (L61).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L57. minor (1–3): Nyx as the aggressive protector in the trial with Lex (L57).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L85. minor (1–3): the Risse in the guide's closing account (L85) — what the line says.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L55. minor (1–3): Kael's mind structured by Tertiary Structural Dissociation (TSDP) (L55).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L49, L61. minor (1–3): the Überwelt as a closed feedback loop where AEGIS only validates its own logic (L49); its place in L61 if the line says so.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). occurrence: the Kernwelt names are worlds, not the Guardians; `Genesis-Krise` is named in scare quotes and not defined (L31); `Juna/V` is read on juna.
- `juna`: `Juna/V` (near `juna`). occurrence: the Kernwelt names are worlds, not the Guardians; `Genesis-Krise` is named in scare quotes and not defined (L31); `Juna/V` is read on juna.
- `logos`: `Logos-Prime` (near `logos`). occurrence: the Kernwelt names are worlds, not the Guardians; `Genesis-Krise` is named in scare quotes and not defined (L31); `Juna/V` is read on juna.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: the Kernwelt names are worlds, not the Guardians; `Genesis-Krise` is named in scare quotes and not defined (L31); `Juna/V` is read on juna.


**Pages not read:** `kohaerenz` (L11 the title) — an occurrence.

**Record entries:** none.

**Not promoted:** the view from nowhere, operational closure, epistemological blindness, the four methods as labels, false balance; the borrowed concepts (standpoint theory, Gödel, confirmation bias, reproducibility crisis, coherence and correspondence theories of truth).

**One reader**: aegis, kael, alters, juna, kern-welten, lex, nyx, risse, tsdp, ueberwelt.

**Chapter readings**: none.
