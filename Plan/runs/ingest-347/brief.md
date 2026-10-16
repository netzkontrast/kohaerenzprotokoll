# Brief — readings from document 346 (step 6)

1 document, one reader, one batch: `ingest-347`. Files go to `Plan/runs/ingest-347/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 346 | `an-architecture-of-the-self-a-critical-review-of-kohaerenz-p` | 2025-10-15 | „the critical review“ (an unsigned English critical review titled „An Architecture of the Self“) | a review of the novel's premise, structure and figures — the unified protagonist, AEGIS as externalised perpetrator introject, the two orders, the alters, the triple helix — closing with a table of strengths and risks and the verdict that the novel „largely succeeds“; it reports the novel's claims and judges them, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (80 lines for `an-architecture-of-the-self-a-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A review: write „the critical review reports that the novel … / judges …“; what it reports of the novel is its account, and its verdicts are its own. Quote the English as written; cut before straight quotes.

## Pages — document 346, `an-architecture-of-the-self-a-critical-review-of-kohaerenz-p`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L15, L25, L35, L46, L59. minor (1–3): AEGIS conceived as an externalized perpetrator introject, its villainy not from malice, its actions tragic, reflexive attempts at dissonance reduction (L15); AEGIS's order, coherence instead of truth (L35); its cold, clinical reports in the perspective shift (L59).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L44. minor (1–3): the depiction of Kael's internal system of dissociated parts, five alters with roles (L44), grounded in established psychological models (L44).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L77. minor (1–3): the strengths table: a respectful and credible depiction of DID (L77), beside L5's naming of the condition as TSDP — the review does not say whether they are one.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L5, L13, L15, L23, L27, L36, … (11 lines). central (3–6): the protagonist's condition externalised, the glitches as its causal manifestation (L5); the premise that the world is a function of the protagonist's mind (L11); Kael's order, coherence through integration (L36); Kael's ultimate role not as a destroyer, The Gardener (L38); the goal, not the erasure of parts but functional multiplicity (L46).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L59. minor (1–3): the simulated Core Worlds, „Kernwelten“, in the perspective-shift sentence (L59).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L44. minor (1–3): Kiko named with a role in the alters sentence (L44).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L1. not read: an occurrence (see below).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L44. minor (1–3): Lex named with a role in the alters sentence (L44).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L44. minor (1–3): Nyx named with a role in the alters sentence (L44).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L44. minor (1–3): Rhys named with a role in the alters sentence (L44).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L13. minor (1–3): the „Risse“ in reality as the externalised struggle, a technique the novel terms Environmental Storytelling (L13).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L44. minor (1–3): Selene named with a role in the alters sentence (L44).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L5, L44, L57. minor (1–3): the protagonist's condition named TSDP (L5); the parts grounded in the model (L44); the tertiary structural dissociation (L57) if the line says so.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L9. not read: an occurrence (see below).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `nichts-rauschen`: `Rauschen` (near `nichtsrauschen`). occurrence: `Rauschen` generic; TSDP's full names and the Emotional Personality parts are read on tsdp and alters, not personas.
- `personas`: `Tertiary Structural Dissociation of the Personality` (near `persona`), `Emotional Personality parts` (near `persona`), `Theory of Structural Dissociation of the Personality` (near `persona`). occurrence: `Rauschen` generic; TSDP's full names and the Emotional Personality parts are read on tsdp and alters, not personas.


**Pages not read:** `kohaerenz` (L1 the title), `ueberwelt` (L9 the generic simulation) — occurrences.

**Record entries:** none.

**Not promoted:** the unified protagonist, Environmental Storytelling, the triple helix, the strengths and risks table, The Gardener as a label, the lens concepts (IFS, autopoiesis, second-order cybernetics, dialetheism, paraconsistent logic, process philosophy, Gödel).

**One reader**: kael, aegis, alters, did, kern-welten, kiko, lex, nyx, rhys, selene, risse, tsdp.

**Chapter readings**: none — the review names the novel's three parts, not chapters.
