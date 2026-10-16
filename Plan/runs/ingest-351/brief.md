# Brief — readings from document 350 (step 6)

1 document, one reader, one batch: `ingest-351`. Files go to `Plan/runs/ingest-351/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 350 | `how-a-sci-fi-epic-redefines-storytelling-5-surprising-takeaw` | 2025-10-15 | „the five-takeaways essay“ (an unsigned English essay) | reports five points from „the conceptual blueprint“ of the novel: AEGIS as a self-closed antagonist, the four Core Worlds as a map of Kael's mind, healing as functional multiplicity, the Gödel-Gambit as the climax, the reader as co-author; phrases in its ASCII quotes are the blueprint's words as it reports them; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (71 lines for `how-a-sci-fi-epic-redefines-st`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An essay reporting a blueprint: write „the five-takeaways essay reports …“; it reports another text's account and decides nothing. Quote the English as written; cut before ASCII quotes. The Core World names are worlds, not the Guardians.

## Pages — document 350, `how-a-sci-fi-epic-redefines-storytelling-5-surprising-takeaw`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L21, L23, L25, L27, L35, L54, … (8 lines). minor (1–3): its core directive not born of malice, to prevent its own non-existence by absolute coherence (L21); reacting only to its own internal state, ontologically blind, its enforced order generating chaos (L23); its axiom that coherence requires eliminating contradiction and multiplicity (L54).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L44. minor (1–3): Kael's condition reported as Dissociative Identity Disorder, with ANPs and EPs, in one line (L44).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L52, L64, L70. minor (1–3): a formal system unable to process a truth that is real but unprovable (L54); Kael as living proof that AEGIS's axiom is false (L56); collapse or transformation (L56).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L23, L31, L35, L36, L37, L38, … (13 lines). central (3–6): the four worlds as externalised representations of Kael's fragmented psyche (L31); Kael's condition as DID (L44); healing not fusion but bridges between the parts (L46); alters sharing control to combine skills (L48); the living proof that AEGIS's core axiom is false (L56).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: an occurrence (see below).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L48. minor (1–3): Lex in the one example phrase of alters sharing control (L48), unexplained.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L48. minor (1–3): Nyx in the same example phrase (L48), unexplained.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L23. minor (1–3): the Risse in the essay's account of AEGIS's failing order (L23) — what the line says of them.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: the Core World names are worlds, not the Guardians; `Kohärenz Protokoll` is the novel's title.
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: the Core World names are worlds, not the Guardians; `Kohärenz Protokoll` is the novel's title.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the Core World names are worlds, not the Guardians; `Kohärenz Protokoll` is the novel's title.
- `logos`: `Logos-Prime` (near `logos`). occurrence: the Core World names are worlds, not the Guardians; `Kohärenz Protokoll` is the novel's title.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: the Core World names are worlds, not the Guardians; `Kohärenz Protokoll` is the novel's title.


**One page beyond the draft:** `kern-welten` (minor, 1–2): the setting as the story (L31) and the four worlds KW1–KW4 introduced for Kael's journey (L33, L35, L36).

**Pages not read:** `kohaerenz` (L15 the title) — an occurrence.

**Record entries:** none.

**Not promoted:** the blueprint as named here, the five takeaways as labels, the reader as co-author, the lens concepts (autopoiesis, uncanny valley, rhizomatic self, Gödel sentence).

**One reader**: aegis, kael, did, goedel-gambit, lex, nyx, risse, kern-welten.

**Chapter readings**: none.
