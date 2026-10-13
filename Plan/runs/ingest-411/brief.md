# Brief — readings from document 410 (step 6)

1 document, one reader, one batch: `ingest-411`. Files go to `Plan/runs/ingest-411/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 410 | `multidimensionale-narrative-strukturmodelle-entwickeln` | 2025-07-03 | „the multidimensional-models report“ (an unsigned German research report) | builds a general model for several parallel storyforms from borrowed theories, with Dramatica as frame, and applies it to „System Kael“ as a case study (L110, L129, L143, L192, L210–L214, L277–L279); L306–L507 are sources, prompts and references; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (508 lines for `multidimensionale-narrative-st`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A research report using the novel as a case study: write „the multidimensional-models report reads … as a case of …“; its readings of the novel are illustrations of its model, citing a source (the footnote 1), never the novel itself. Read only the case-study lines; nothing from the source, prompt or reference lists (L306–L507), and never mention who brought the project in (L32). Quote the German as written; cut before straight and nested quotes, bold markers and glued footnote digits. No gendered pronoun for Kael or Juna — use the names (quotations stay verbatim). Never write a real person's name.

## Pages — document 410, `multidimensionale-narrative-strukturmodelle-entwickeln`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L110, L143, L210, L212, L277, L279, … (14 lines). central (3–6): the entity AEGIS as „ein übergeordnetes Meta-System“ trying to regulate and control the Kernwelten, the „Paradoxon der fehlausgerichteten Kohärenz“ arising because AEGIS reads their functions as errors or entropy (L110); the thesis of the dialectic, AEGIS's „Kohärenz Protokoll“ of top-down control (L210); AEGIS as „die fehlerhafte, traumatisierte Meta-Erzählung“ born from the Nichts Rauschen out of fear (L277); Kael's journey a revolt against AEGIS's totalising narrative (L279).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L74. not read: an occurrence — emergence in the report's general sense (L74).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L110. not read: an occurrence — what AEGIS calls the Kernwelten's functions (L110), read on aegis.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L318. not read: an occurrence — a source-list title (L318).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L143. minor (1–3): the „Juna/V Verbindung“ seeming to fulfil a rhizomatic function, a mode of being outside AEGIS's hierarchical control that can destabilise and transform the whole system (L143).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L32, L110, L129, L143, L192, L210, … (21 lines). central (3–6): Kael's psychological integration on the basis of TSDP entangled with the stability of the Kernwelten (L129); the ANPs „wie Kael (Host) und Lex (Analytiker)“ as persona, and Kael's journey to integrate the traumatised shadow parts (L192); the antithesis: „Kaels psychologischer Heilungsprozess“ (L212); the nested storyforms as Kael's inner parts trying to heal (L277).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L110, L129, L192, L410, L414. minor (1–3): the Kernwelten, e.g. the world of logic and the world of emotions, as autopoietic storyforms each representing a psychological function (L110); their stability entangled with Kael's inner state (L129); the Kernwelten as externalisations of the psychic domains (L192).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L192. minor (1–3): among the EPs, „Kiko (Kind/Angst)“, the repressed shadow (L192).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L48. not read: an occurrence — coherence in the general sense of autopoietic systems (L48).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L36, L40, L192. minor (1–3): among the ANPs, „Lex (Analytiker)“, embodying the persona (L192).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L277, L418. minor (1–3): AEGIS's origin „aus dem „Nichts Rauschen““ — cut before the nested quote — establishing it as a system born of fear (L277).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L192. minor (1–3): among the EPs, „Nyx (Kämpfer)“, the repressed shadow carrying traumatic memories (L192).
- **`personas`** (minor, 1–4): the census's surfaces — `Persona` L172, L174, L175, L190, L192, L222, … (9 lines). not read: an occurrence — persona in the borrowed depth-psychological sense (L192), not the page's term.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L129, L322, L410, L414, L420, L504. minor (1–3): Kael's psychological integration process „auf Basis der TSDP“ (L129).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L326. not read: an occurrence — a source-list title (L326).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `juna`: `Juna/V Verbindung` (near `juna`). decided with the pages above: `System Kael` and `Kaels` read on kael; `Juna/V Verbindung` read on juna; `Riss` read on risse (below); `Paradoxon der fehlausgerichteten Kohärenz` and `Kohärenz Protokoll` read on aegis; `These`, `Antithese`, `Synthese` the dialectic's terms; `Storyforms` the plural.
- `kaels-wohneinheit`: `Kaels` (near `kaelswohneinheit`), `Kaels` (near `kaelswohneinheit10`). decided with the pages above: `System Kael` and `Kaels` read on kael; `Juna/V Verbindung` read on juna; `Riss` read on risse (below); `Paradoxon der fehlausgerichteten Kohärenz` and `Kohärenz Protokoll` read on aegis; `These`, `Antithese`, `Synthese` the dialectic's terms; `Storyforms` the plural.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Paradoxon der fehlausgerichteten Kohärenz` (near `koharenz`). decided with the pages above: `System Kael` and `Kaels` read on kael; `Juna/V Verbindung` read on juna; `Riss` read on risse (below); `Paradoxon der fehlausgerichteten Kohärenz` and `Kohärenz Protokoll` read on aegis; `These`, `Antithese`, `Synthese` the dialectic's terms; `Storyforms` the plural.
- `risse`: `Riss` (near `risse`). decided with the pages above: `System Kael` and `Kaels` read on kael; `Juna/V Verbindung` read on juna; `Riss` read on risse (below); `Paradoxon der fehlausgerichteten Kohärenz` and `Kohärenz Protokoll` read on aegis; `These`, `Antithese`, `Synthese` the dialectic's terms; `Storyforms` the plural.


**Pages beyond the draft:**
- **`risse`** (minor, 1): a breakthrough in Kael's inner world could instantly heal „einen „Riss““ — cut before the nested quote — in the outer world, with no physical chain of cause (L129).

**Record entries:** none.

**Pages not read:** personas, emergenz, entropie, genesis, kohaerenz, ueberwelt — occurrences.

**Not promoted:** System Kael, Paradoxon der fehlausgerichteten Kohärenz, Juna/V Verbindung, Meta-Erzählung, Storyform, the dialectic's terms, Das Fundament, and the borrowed concepts.

**One reader**: aegis, kael, lex, nyx, kiko, kern-welten, nichts-rauschen, tsdp, juna, risse.

**Chapter readings**: none — the document names no chapter.
