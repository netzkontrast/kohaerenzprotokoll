# Brief — readings from document 441 (step 6)

1 document, one reader, one batch: `ingest-442`. Files go to `Plan/runs/ingest-442/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 441 | `prompt-entwicklung-fuer-kohaerenz-erzaehlstrang` | 2025-10-15 | „the strand-integration analysis“ (an unsigned German analysis with a prompt, „Prompt-Entwicklung für Kohärenz Erzählstrang“) | joins an external plot (a simulated reality breaking down, with Aris Thorne, Silus and Aethelred, from a plot draft named „Kohärenz-Protokoll-Glitch“) and Kael's TSDP strand, weighs three integration models, recommends Model C — Aris Thorne and Kael the same person — and gives an AI prompt; a recommendation (L191, L224), no claim of canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (388 lines for `prompt-entwicklung-fuer-kohaer`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A proposal: write „the strand-integration analysis proposes …“ or „its recommended Model C …“; Model C (Aris Thorne and Kael one system) is its recommendation, not the novel's decision; Aris Thorne, Silus, Elara Vance and Aethelred belong to the external plot draft it merges and have no wiki page — name them only where a reading needs them. Its part roles are „hypothetische Rollen“ (L108). Quote the German as written; cut before straight quotes, bold markers, escaped table markup and glued footnote digits. No gendered pronoun for Kael, AEGIS or any part — use the names (quotations stay verbatim). Never write a real person's name (it quotes one thinker) nor a term carrying one.

## Pages — document 441, `prompt-entwicklung-fuer-kohaerenz-erzaehlstrang`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L158, L226, L259, L311. minor (1–4): Model A's antagonist „Silus/AEGIS“, the administrator of the simulation (L226); mapping 3: Silus/Aethelred as external controller = AEGIS as „Internalisierter Unterdrücker“ (L259); the prompt: external antagonist Silus mirrors inner conflict AEGIS (L311) — AEGIS read here as an internal oppressor, the analysis's mapping, recorded, not applied.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L22, L89, L97, L108, L158, L166, … (17 lines). central (4–8): the inner strand: a fundamental conflict inside the protagonist Kael, built on structural dissociation (L89, L97); five named parts with hypothetical roles (L108); Model A sets Kael and the inner system wholly inside the decaying simulation Aris Thorne experiences (L158); the recommended Model C: „Aris Thorne und Kael sind dieselbe Person“, Aris Thorne the outward primary ANP of the system called Kael (L200); example: Aris/Lex must solve a logical puzzle in the first Kernwelt (L360).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelt` L360. minor (1–4): example 1: a logical puzzle „in der Kernwelt“ with the first world's code (L360 — quote around the nested quote); the second world's code named once (L361).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L124, L137, L260, L312, L349, L361, … (7 lines). minor (1–4): holds fear, grief and abandonment, carrying pain and the attachment need (L124).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L18. not read: occurrences — the introduction's heading „Die Dualität der Kohärenz“ (L18) and the title (L24); coherence in philosophical and physical senses (L26, L27) is the document's lens.
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L114, L137, L179, L257, L260, L261, … (10 lines). minor (1–4): „Der hyper-rationale, kontrollierende Logiker“, phobic of emotion and loss of control (L114); example: Aris/Lex solving a logic puzzle in the first Kernwelt (L360).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L115, L125, L137, L260, L312, L347, … (8 lines). minor (1–4): holds anger and aggression linked to the fight reaction, protecting the system by defence (L125).
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L276. not read: an occurrence — „Persona/Ton“ is the prompt's style field (L276).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L115, L261, L313, L348, L361, L378. minor (1–4): „Der soziale Mediator und Harmoniestifter“, phobic of conflict and of Nyx's aggression (L115).
- **`risse`** (minor, 1–4): the census's surfaces — `Glitch` L22, L63, L158, L179, L227, L260, … (9 lines); `Glitches` L63, L158, L179, L309. minor (1–4): the external plot's „Glitches“ are no random anomalies but a philosophical crisis manifesting physically (L63 — cut before the straight quote); the source plot draft named after them (L22).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L22, L89, L93, L97, L210, L257, … (9 lines). minor (1–4): the inner strand built on the TSDP model (L89); Kael's psyche read as tertiary structural dissociation (L97); Model C makes Aris Thorne the outward ANP (L200).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Simulation` L81, L137, L158, L179, L200, L208, … (14 lines). minor (1–4): the discovery that reality is a simulation run by Silus (L81); Kael inside the decaying simulation (Model A, L158); Silus keeps his simulation coherent by censoring (L137).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz Protokolls` (near `koharenz`), `Kohärenztheorie der Wahrheit` (near `koharenz`), `Quanten-Dekohärenz` (near `koharenz`). occurrences: the title, its genitive, a borrowed theory of truth and a physics process.


**Record entries:** none.

**Not promoted:** Aris Thorne, Silus, Elara Vance, Aethelred (figures of the external plot draft), Kai (no page exists), Modell A/B/C, Mandela-Effekt, Basisrealität, Quellcode, heilsame Lüge, partizipatorisches Universum, Bindungsproblem, Datenanomalie, Laborunfall, ANP/EP, and the borrowed concepts.

**One reader**: every page above.

**Chapter readings**: none — the document names no chapter.
