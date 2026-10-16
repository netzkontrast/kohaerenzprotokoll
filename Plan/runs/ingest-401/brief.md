# Brief — readings from document 400 (step 6)

1 document, one reader, one batch: `ingest-401`. Files go to `Plan/runs/ingest-401/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 400 | `ki-roman-design-mechaniken` | 2026-03-02 | „the game-design analysis“ (an unsigned German report on AI-driven interactive novels) | surveys drama management, storylets, lorebooks and guardrails in general (L11–L150), then proposes four player mechanics for the Kohärenz Protokoll as an interactive game (L152–L184); a proposal, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (266 lines for `ki-roman-design-mechaniken`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A proposal for a game: write „the game-design analysis proposes …“ or „its premise for the game gives …“; what it says of the novel's figures is the premise it states for its game mechanics (L154–L156, L169) or the mechanic itself — never the novel as written. Read only from L152–L184; the general survey before it names nothing of the novel. Quote the German as written; cut before straight and nested quotes, italics markers and glued footnote digits. No gendered pronoun for Kael or Juna — use the names (quotations stay verbatim). Name no real game, product, company or person.

## Pages — document 400, `ki-roman-design-mechaniken`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L156, L165, L183. minor (1–3): the Kohärenz-Kernel stands for order, information and the control structure of „der Entität AEGIS“ (L156); the AEGIS-Matrix absorbing Kael's consciousness (L165); system errors as AEGIS manipulating the matrix to deceive Kael (L183).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L169. minor (1–3): eleven sealed-off parts (Alters) of Kael's psyche (L169); the player negotiates which of the eleven takes the executive system (L171); a „Trauma-Holding-Alter“ such as Praetor, afraid of absorption by the system (L172).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L154. minor (1–3): the document calls it „die fiktive „Dual Kernel Theory“ (DKT)“ — cut before the nested quote — one of the project's strands (L154); player input validated against the laws of the Dual Kernel Theory (L179).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L156. not read: an occurrence — entropy as what the Kollaps-Kernel stands for (L156), read on kollaps-kernel.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L156, L184. minor (1–3): the Kollaps-Kernel stands for entropy, emotional pain, organic truth and „die Entität Juna“ (L156); in the interface, another face showing through behind the figure Juna (L184).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L156, L165, L169, L183. minor (1–3): the premise: the protagonist Kael suffers from TSDP and stands in a conflict between the Kohärenz-Kernel and the Kollaps-Kernel (L156); in the game, Kael's consciousness absorbed by the AEGIS-Matrix when K1 passes a threshold (L165); Kael's psyche split into eleven sealed-off parts (L169); telling „Systemfehler“ from „Ich-Fehler“ (L183).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L89. not read: an occurrence — coherence over hundreds of rounds of a general AI system (L89).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L156. minor (1–3): „Kohärenz-Kernel (K1)“: unrelenting order, information, AEGIS's control structure (L156); in the game a metric for coherence — logical, cold, structure-preserving (L164).
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L156. minor (1–3): „Kollaps-Kernel (K0)“: entropy, emotional pain, but also organic truth, and Juna (L156); in the game a metric — emotional, entropic, trauma-based (L164); the „Void“ as the collapse domain (L178).
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Personas` alone on L23. not read: an occurrence — personas of the general survey (L23).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitches` alone on L127. not read: an occurrence — glitches as a visual device for players (L127).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L156. minor (1–3): the premise: Kael suffers from „Tertiärer Struktureller Dissoziation der Persönlichkeit (TSDP)“ (L156).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L17. not read: an occurrence — simulation in the literary-theory sense (L17).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alex`: `Authorial Experience Manager` (near `alex`). occurrence: the survey's own or a general sense (`Authorial Experience Manager` a drama-management system, not Alex; `RASE` an engine name; `Glitch-Ästhetik` a design device; `Rauschen` general; `Kohärenz Protokoll` the title).
- `garten-der-stillen-praesenz`: `RASE` (near `gartenderstillenprasenz`). occurrence: the survey's own or a general sense (`Authorial Experience Manager` a drama-management system, not Alex; `RASE` an engine name; `Glitch-Ästhetik` a design device; `Rauschen` general; `Kohärenz Protokoll` the title).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the survey's own or a general sense (`Authorial Experience Manager` a drama-management system, not Alex; `RASE` an engine name; `Glitch-Ästhetik` a design device; `Rauschen` general; `Kohärenz Protokoll` the title).
- `nichts-rauschen`: `Rauschen` (near `nichtsrauschen`). occurrence: the survey's own or a general sense (`Authorial Experience Manager` a drama-management system, not Alex; `RASE` an engine name; `Glitch-Ästhetik` a design device; `Rauschen` general; `Kohärenz Protokoll` the title).
- `risse`: `Glitch-Ästhetik` (near `glitch`). occurrence: the survey's own or a general sense (`Authorial Experience Manager` a drama-management system, not Alex; `RASE` an engine name; `Glitch-Ästhetik` a design device; `Rauschen` general; `Kohärenz Protokoll` the title).


**Record entries:** none.

**Pages not read:** entropie, kohaerenz, personas, risse, ueberwelt — occurrences.

**Not promoted:** Gamma-7, Void, Praetor, Echo von Panik, Trauma-Holding-Alter, Story Mind, Exekutivsystem, Systemische Stabilität, Fokus-Slider, and the general survey's terms.

**One reader**: kael, aegis, juna, kohaerenz-kernel, kollaps-kernel, dkt, tsdp, alters.

**Chapter readings**: none — the document names no chapter.
