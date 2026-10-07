# Brief — readings from document 213 (step 6)

1 document, one reader, one batch: `ingest-213`. Files go to `Plan/runs/ingest-213/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 213 | `analyse-des-romanprojekts-kohaerenz-protokoll` | 2025-11-03 | „the project analysis“ (an unsigned analytic essay) | a German analytic essay in four parts and eleven numbered Kapitel of its own — not the novel's chapters — reading the project through physics, philosophy and clinical psychology, with three tables and a three-act plan, from nine numbered reference texts; no canon claim, two cells marked `Annahme` |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (250 lines for `analyse-des-romanprojekts-koha`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis that reports its sources: write „the project analysis reads / reports …“; its `Kapitel N` are the essay's sections, never the novel's chapters; keep `(Annahme)` and `(Integratorin?)`. German — quote as written; cut before glued footnote digits (`definiert“.4`) and inner quotes; tables carry escaped bold and `KW\\_Rhys` — never quote across them; `--find` drops the digit in `KW1` — quote around it.

## Pages — document 213, `analyse-des-romanprojekts-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L44, L48, L58, L60, L62, L64, … (27 lines). central (3–6): the Genesis-Krise forming AEGIS as an ontological wound (L44); its fragmentation the consequence of an unsolvable logical paradox (L48); the Überwelt operating literally on the coherence theory (L58); AEGIS as the „ultimative Kohärentist“ (L62) — quote around the inner quotes; its methods as psychological engineering, the Kernwelten as Skinner boxes (L107); its tragedy unavoidable, an eternal re-enactment of its first defence (L99).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L176. minor (1–3): Alex as ANP (Beschützer), protecting the vulnerable parts (L176).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L184. minor (1–3): Argus as „ANP/EP-Mix“, metacognitive observation and criticism (L184).
- **`dkt`** (minor, 1–4): the census's surfaces — `Dual-Kernel-Theorie (DKT)` L30; `DKT` L30. minor (1–3): the conceptual frame of the Dual-Kernel-Theorie with a Kohärenz-Kernel and a Kollaps-Kernel (L30) — read the line.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L36. minor (1–3): the cycle of intrusion, correction and reconfiguration, „Rekonfiguration (Emergenz)“ (L36) — cut around the arrows and subscripts.
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L30, L46, L64, L75. minor (1–3): „Entropie“ with a double meaning: the physical collapse of the K₀ kernel and every truth that does not fit AEGIS's model (L64) — quote around the subscript; the table row (L75).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L238. minor (1–3): the Genesis-Krise as the founding event that forms AEGIS and the whole reality, an ontological wound (L44) — cut before the inner quotes; L238 is a reference title, an occurrence.
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L181. minor (1–3): Isabelle as EP (Sexualisiert) (L181).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L60, L62, L64, L74, L99, L107, … (26 lines). central (3–6): the protagonist Kael forced to become „ein Agent der Korrespondenz“ (L62) — quote around the inner quotes; the TSDP as the rule set for System Kael's consciousness (L139); the eleven identified parts of System Kael as an inner society (L151); Kael as ANP (Host) (L174); the act II journey into the Risse of the Überwelt (L215).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L107, L109. minor (1–3): the Kernwelten as environmental Skinner boxes (L107) and totalitarian milieus (L109); the table of Kernwelt, target part and reinforcement (L119–L123) — KW1 (Logos-Prime) for Lex, KW3 (Cerberus-Labyrinth) for Nyx, two worlds marked `Annahme` for Rhys and Kiko — quote around the digits and escapes.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L76, L123, L163, L178, L179, L181. minor (1–3): Kiko as EP (Kind) — flight, freeze, attachment cry (L179); a Kernwelt for Kiko marked `Annahme` (L123) — describe, do not quote across the escape.
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L13, L22, L26, L30, L32, L36, … (22 lines). central (3–6): Kohärenz against Kollaps as the primal duality (L26, L30); the Überwelt operating on the coherence theory of truth (L58); the duality table, Kohärenz against Entropie/Korrespondenz (L75); the Kohärenz Protokoll as AEGIS's absolute control (L78).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L30. minor (1–3): read L30 for the Kohärenz-Kernel in the DKT.
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L30, L46. minor (1–3): read L30 and L46 for the Kollaps-Kernel.
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L76, L107, L109, L113, L120, L151, … (16 lines). central (3–6): Lex as ANP (Rationalist), phobia of irrationality (L175); the target part of KW1 (Logos-Prime) (L120); Lex's pride in his logic as a product of hostile programming (L113); the conflict between Lex and Rhys as a miniature of AEGIS against correspondence (L167).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L178, L180, L181. minor (1–3): Lia as EP (Kind), ambivalent attachment (L180).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L163, L165, L182. minor (1–3): Moros as EP (Kollaps), carrier of hopelessness (L182); Nyx's fight against Moros's collapse (L165).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L77. minor (1–3): read L77 — the table row on unity against diversity; decide reading or occurrence.
- **`nyx`** (central, 3–12 quotations): the census's surfaces — `Nyx` L76, L107, L113, L121, L151, L163, … (11 lines). central (3–6): Nyx as EP (Kampf), protecting Kiko and Lia (L178); the target part of KW3 (Cerberus-Labyrinth) (L121); Nyx's identification with his strength as a product of programming (L113); Lex against Nyx and Kiko (L76).
- **`rhys`** (central, 3–12 quotations): the census's surfaces — `Rhys` L78, L122, L164, L167, L174, L175, … (10 lines). central (3–6): Rhys striving for acceptance and connection (L78); a Kernwelt for Rhys marked `Annahme` (L122) — describe; the conflict between Lex and Rhys (L164, L167).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L60, L215. minor (1–3): „Die in dieser Welt auftretenden“ Risse as physical manifestations of the isolation objection (L60) — cut before the inner quotes; the Risse of the Überwelt in act II (L215).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L183, L228. minor (1–3): Selene as „ANP (Integratorin?)“, a buffer whose integrative nature threatens AEGIS (L183) — keep the question mark; read L228 — decide.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L119, L135, L139, L141, L153, L173, … (8 lines). minor (1–3): the TSDP as the basic rule set for System Kael's consciousness (L139); ANPs and EPs (L141); the chapter heading (L135).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L58, L215. minor (1–3): the domain controlled by AEGIS, „die“ Überwelt, operating on the coherence theory (L58) — quote around the inner quotes; the Risse of the Überwelt (L215).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `KW3 (Cerberus-Labyrinth)` (near `cerberus`), `Cerberus-Labyrinth` (near `cerberus`). occurrence: `Cerberus-Labyrinth` is KW3's name (L121), read on kern-welten (J49).
- `coheron`: `Coherons` (near `coheron`), `Coheron-Netzwerke` (near `coheron`). occurrence: `Coherons` and `Coheron-Netzwerke` — read on coheron only if a reader finds a line that adds; otherwise an occurrence in the physics frame.
- `genesis`: `Genesis-Krise` (near `genesis`). `Genesis-Krise` read on genesis (L44).
- `logos`: `KW1 (Logos-Prime)` (near `logos`), `Logos-Prime` (near `logos`). occurrence: `Logos-Prime` is KW1's name (L120), read on kern-welten (J49).


**Record entries** (one file each):

- **`q5-guardians-and-kern-welten`**: Kernwelten as conditioning environments for target parts — KW1 (Logos-Prime) for Lex, KW3 (Cerberus-Labyrinth) for Nyx, two assumed worlds for Rhys and Kiko (L119–L123); no Guardian named.
- **`q3-how-many-kern-welten-and-alters`**: „Die elf identifizierten Anteile“ (L151) and the table of eleven (L174–L184) against „mindestens vier ANPs und fünf klaren EPs“ (L141) — record both; no KW2 in the table.

**Not promoted:** the essay's own Kapitel 1–11, the reference texts, Skinner boxes and thought reform (Lifton, Hassan), the borrowed theories, the anti-fragility argument.

**Two readers**, disjoint: (1) kael, lex, nyx, rhys, kiko, lia, moros, isabelle, alex, argus, selene, tsdp, multiplizitaet and the record q3; (2) aegis, kohaerenz, kohaerenz-kernel, kollaps-kernel, dkt, emergenz, entropie, genesis, risse, ueberwelt, kern-welten and the record q5.

No chapter readings: its `Kapitel` are the essay's sections.
