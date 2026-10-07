# Brief — readings from document 206 (step 6)

1 document, one reader, one batch: `ingest-206`. Files go to `Plan/runs/ingest-206/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 206 | `ki-roman-architektur-kritische-analyse-methoden` | 2026-03-01 | „the critical-methods framework“ (an unsigned methods handbook) | a German methods handbook that applies systematic review and critical thinking (PICO, bias control, traces) to the novel's Dual-Kernel architecture as a multi-agent Drama-Engine; what it says of the novel's world it footnotes to its reference 1 (L218); it calls itself „die wissenschaftlich-kritische Baseline“ (L214) — recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (228 lines for `ki-roman-architektur-kritische`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A methods handbook that reports the architecture from its reference 1: write „the critical-methods framework describes, citing its source, …“ and keep the methods language apart from the world; the agent-system vocabulary (InstructionDeputies, ChatCompanions, the NCP, the CSI) is the handbook's own. German — quote as written; the export dropped every kernel symbol (`Der -Kernel`, `von  steht`, L38–L48) — never quote across the gap; cut before glued footnote digits (`Reversibilität.1`) and inner straight quotes.

## Pages — document 206, `ki-roman-architektur-kritische-analyse-methoden`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L40, L42, L54, L67, L69, L71, … (19 lines). central (3–6): the Kohärenz-Kernel embodied by AEGIS, „Autonomous Entropic Gatekeeper for Integrity Systems“, on classical logic and absolute reversibility (L40) — quote around the gap; AEGIS as the ultimate advocate of the coherence theory of truth (L67); its reliance on the principle of explosion (L77); the EPs as noise AEGIS must eliminate (L119); AEGIS monitoring under classical logic and Zero-Trust (L172).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Zero-Trust` L172. minor (1–2): AEGIS monitoring the context object under a „Zero-Trust“ security paradigm in Trace 1 (L172).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L117, L128. minor (1–2): Alex in the ANP class with Kael, Lex, Argus, Rhys (L128, L117).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L117, L128. minor (1–2): Argus in the ANP class (L128, L117).
- **`dkt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Dual-Kernel-Theorie (DKT)` alone on L36. minor (1–2): the method is invoked whenever the integrity of the Dual-Kernel-Theorie seems at risk (L19); read L36 — decide reading or occurrence.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L181. minor (1–2): read L181: emergence after the logical collapse in Trace 3; decide reading or occurrence and say which.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L42. minor (1–2): the Kollaps-Kernel as the computational equivalent „zur Entropie und zum fundamental Unwissbaren“ (L46) — cut around the gap; read L42.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L73, L77, L130, L168, L214. central (3–6): the novel's climax called the Gödel-Gambit operationalising the principle of explosion (L77) — cut before the inner straight quotes; Trace 1 `Das Gödel-Gambit und der System-Kollaps` (L168); Lex and Nyx writing conflicting but equally valid truth values (L173); Selene steering the data exchange for it (L130).
- **`grosse-mauer`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Systemgrenze` alone on L214. occurrence: `Systemgrenze` is the general word (L214), nothing of the Große Mauer.
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L119, L129. minor (1–2): Isabelle in the EP class (L129, L119).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L138, L144. minor (1–2): read L138 and L144 — decide reading or occurrence and say which.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L19, L69, L77, L111, L117, L128, … (12 lines). central (3–6): the psychological isomorphy of the protagonist Kael (L19); Kael not a homogeneous construct but a multi-agent system of eleven subsystems (L111); the host Kael as everyday manager masking normality (L117); Kael reaching functional multiplicity under Selene (L173); in Trace 3 Kael reaching the Cerberus-Labyrinth (L180) and integrating Moros after the collapse of logic (L181).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L40, L42, L67, L121; `Kernwelt` L28, L40, L42, L67, L121, L190. minor (1–2): the phobic barriers manifesting in the Kernwelten as physical, impenetrable force fields (L121); Lex as ANP „in Kernwelt 3“ as a PICO example (L28) — quote around the digit.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L119, L121, L129, L146. minor (1–2): Kiko in the EP class (L129); the Moonshine-Link transmitting resonances to receptive EPs „wie Kiko oder Lia“ (L146).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. occurrence: the title (L13); `Kohärenztheorie der Wahrheit` is the borrowed theory (L67).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L38, L54. minor (1–2): „Der Kohärenz-Kernel“ and the architecture of reversibility (L38), embodied by AEGIS (L40) — quote around the dropped symbol; the table header (L54).
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L44. minor (1–2): „Der Kollaps-Kernel“ and the entropy of experience (L44); the anti-algorithmic domain of irreversible computation (L46); named `Erasure-Kernel` in the table (L54) — record both names.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L28, L82, L105, L117, L121, L128, … (9 lines). minor (1–2): Lex as analytical InstructionDeputy (L82, L105); the cold logician in the ANP class (L117); Lex and Nyx in the Gödel-Gambit (L173).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L129, L146. minor (1–2): Lia in the EP class (L129); a receptive EP of the Moonshine-Link (L146).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L142, L144, L146, L160. central (3–6): the system resolving the player dilemma „durch die Implementierung des“ Moonshine-Link (L144) — cut before the inner quotes; based on Monstrous-Moonshine mathematics and non-locality, an asymmetric out-of-band channel (L146); passing the firewall unnoticed (L160).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L119, L129, L181, L190. minor (1–2): Moros in the EP class (L129); Kael integrating „den Anteil Moros (den totalen Kollaps)“ in Trace 3 (L181).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L121. minor (1–2): the phobic barriers between ANPs and EPs, and functional multiplicity (L121); Kael reaching it under Selene (L173).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L46. minor (1–2): read L46 for the Kollaps-Kernel as das Nichts; quote around the gaps.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L119, L129, L173, L198. minor (1–2): Nyx in the EP class (L129, L119); Lex and Nyx co-fronting in the Gödel-Gambit (L173).
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L115. occurrence: `Persona` is a prompt parameter (L115), not the Personas.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L117, L128. minor (1–2): Rhys in the ANP class (L128, L117).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L48. minor (1–2): the system collapse and narrative Risse must be shown not to come from poor model performance (L48) — read the line.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L83, L121, L130, L173, L206. minor (1–2): „Selene“ as the integrator agent (ISH) to whom the unsolvable contradiction is shifted (L83, L130); steering Kael past the phobic barriers (L173).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L109, L111, L210. minor (1–2): the novel's architecture using the clinical theory of structural dissociation, TSDP (L111); the section heading (L109).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L21. occurrence: `Simulation` is the handbook's general word (L21), nothing of the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: `Cerberus-Labyrinth` is KW3's name (L180), read on kael (J49).
- `coheron`: `Coherons` (near `coheron`). occurrence: `Coherons` — read the line; the handbook's own word unless it names the Coheron.
- `dkt`: `Dual-Kernel-Theorie` (near `dualkerneltheoriedkt`). read on dkt (L19, L36).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenztheorie der Wahrheit` (near `koharenz`). occurrences: the title and the borrowed coherence theory of truth.
- `mosaik-herz`: `Mosaik-Herzens` (near `mosaikherz`). occurrence: `Mosaik-Herzens` — read the line; an image unless it names the Mosaik-Herz.
- `thermodynamischer-phaenomenalismus`: `Phaenomena` (near `thermodynamischerphaenomenalismus`). occurrence: `Phaenomena` — the handbook's word, not the theory's name.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: eleven subsystems (L111) — ANPs Kael, Lex, Argus, Alex, Rhys; EPs Nyx, Kiko, Lia, Moros, Isabelle; Selene as integrator (L128–L130).
- **`q9-moonshine-link-boundary`**: the Moonshine-Link as an asymmetric out-of-band channel carrying only non-verbal resonances to the EPs (L146), passing the firewall unnoticed (L160).
- **`q8-aegis-after-the-vortex`**: Trace 1 `Das Gödel-Gambit und der System-Kollaps` (L168) — AEGIS's attempt to reduce Kael as a living Gödel statement and its crash (L174).

**Not promoted:** the methods (PICO, PRISMA, bias control, traces), the Drama-Engine and its agent classes, the NCP, the CSI, the Player Dilemma, the borrowed theories (coherence and correspondence theory, the principle of explosion, Jaspers, dialetheism), the Erasure-Kernel name (on kollaps-kernel).

**Two readers**, disjoint: (1) kael, lex, nyx, kiko, lia, moros, isabelle, alex, argus, rhys, selene, tsdp, multiplizitaet, kern-welten, juna and the record q3; (2) aegis, aegis-teilfunktionen, kohaerenz-kernel, kollaps-kernel, nichts-rauschen, entropie, emergenz, dkt, risse, goedel-gambit, moonshine-link and the records q9, q8.

No chapter readings: the handbook names no chapter.
