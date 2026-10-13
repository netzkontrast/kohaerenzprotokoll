# Brief — readings from document 271 (step 6)

1 document, one reader, one batch: `ingest-272`. Files go to `Plan/runs/ingest-272/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 271 | `tsdp-analyse-kohaerenz-protokoll-charaktere` | 2025-04-28 | „the TSDP tension analysis“ (an unsigned German report) | an analysis of the tension points and profiles of System Kael's eleven parts by the theory of structural dissociation: theory (section 2), internal conflicts, system interactions with the Kernwelten, AEGIS and Juna/V (section 3), one profile per part (section 4, L216–L292), plot recommendations (section 5); much of it hedged, and many statements cite an unshown brief as `User Query`; it calls itself a „direkt nutzbare Referenz“ (L29), its claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (423 lines for `tsdp-analyse-kohaerenz-protoko`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis: write „the TSDP tension analysis describes / sorts / proposes …“ and keep its hedges (`wahrscheinlich`, `möglicherweise`, `scheint`). Where a line ends in `User Query` or a code (PP-…), the statement is the unshown brief's as the analysis reports it — say so. The theory's definitions (section 2) are reported theory, not the novel. Section 5 is advice. Read each part from its profile in section 4, its opening definition first.

## Pages — document 271, `tsdp-analyse-kohaerenz-protokoll-charaktere`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L25, L106, L112, L180, L184, … (35 lines). central (3–6): „scheint eine zentrale externe oder internalisierte Kraft“ (L186); apparently prefers Lex's mode (L188); a kind of toxic manager in the inner family system (L193); sees Selene as anomaly or threat, as the brief has it (L191); Paradoxon X under its influence (L190, L233); „AEGIS als Störfaktor“ (L321) and the Kohärenz Protokoll (L371).
- **`alex`** (central, 3–12 quotations): the census's surfaces — `Alex` L41, L51, L62, L107, L126, L130, … (22 lines). central (3–6): „sekundäre ANPs“ with Rhys (L41); the profile „Alex ist ein sekundärer ANP“ on protection and defence (L265–L271).
- **`argus`** (central, 3–12 quotations): the census's surfaces — `Argus` L45, L62, L107, L140, L282, L286, … (11 lines). central (3–6): „ein sich entwickelnder Anteil“ (L45); the profile, metacognitive observer and critic, an emerging ANP/EP mix (L286–L292).
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L124, L218, L400. minor (1–3): the cache-coherence problem probably mirrors Kael's struggle for a coherent identity (L124); the metaphor in the synthesis (L218 or the 5.x line).
- **`isabelle`** (central, 3–12 quotations): the census's surfaces — `Isabelle` L45, L52, L62, L107, L147, L148, … (23 lines). central (3–6): among the EPs (L45); the profile, an EP from specific sexual trauma as the brief has it, sexualised fight and control (L251–L257).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L21, L25, L195, L197, L199, L200, … (16 lines). central (3–6): „Juna/V stellen als externe Interaktionspartner“ triggers and relationship figures (L195–L201); Juna/V as catalyst (L354).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L21, L25, L29, L31, L41, … (72 lines). central (3–6): eleven parts (L17); Kael and Lex as primary ANPs (L41); tertiary structural dissociation (L62); the profile „Kael ist der primäre ANP“, responsible yet a stranger in his own system (L216–L222); cache coherence (L124).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L21, L25, L176, L178, L182, L373. minor (1–3): the Kernwelten named in the brief (L178): Co₁ „(Logisch/AEGIS-konform?)“ (L180), McL „(Chaotisch/Emotional?)“ (L181), the other two by analogy (L182); heading „(Co₁, McL, B, Ly)“ (L176); advice (L373).
- **`kiko`** (central, 3–12 quotations): the census's surfaces — `Kiko` L45, L52, L62, L107, L109, L124, … (39 lines). central (3–6): among the EPs (L45); the profile „Kiko ist ein klassischer kindlicher EP“ (L237–L243).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — the title (L11).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L41, L51, L62, L107, L109, L110, … (49 lines). central (3–6): Kael and Lex primary ANPs (L41); AEGIS prefers Lex's mode (L188); the profile „Lex ist ein primärer ANP“, cognitive control and logic (L279–L285).
- **`lia`** (central, 3–12 quotations): the census's surfaces — `Lia` L45, L52, L62, L107, L126, L146, … (27 lines). central (3–6): among the EPs (L45); the profile, a child EP of broken trust as the brief has it (L244–L250).
- **`moros`** (central, 3–12 quotations): the census's surfaces — `Moros` L45, L52, L62, L107, L124, L126, … (30 lines). central (3–6): among the EPs (L45); the profile, freeze, submission, collapse; „Moros braucht vor allem“ Zeugenschaft (L258–L264).
- **`nyx`** (central, 3–12 quotations): the census's surfaces — `Nyx` L45, L52, L62, L107, L109, L110, … (40 lines). central (3–6): among the EPs (L45); the profile, the fight part, a paradoxical relation to the child parts (L230–L236); his activation under AEGIS leading to Paradoxon X (L233).
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L255. not read: occurrence — `Persona` (L255) is Isabelle's controlling persona in general use, not the page's term.
- **`rhys`** (central, 3–12 quotations): the census's surfaces — `Rhys` L41, L51, L62, L107, L127, L130, … (40 lines). central (3–6): secondary ANP with Alex (L41); the profile „Rhys ist ein sekundärer ANP“, attachment and care (L272–L278).
- **`selene`** (central, 3–12 quotations): the census's surfaces — `Selene` L21, L45, L62, L94, L107, L128, … (26 lines). central (3–6): „modifizierter ANP mit EP-Komponenten“ (L45); her role tied to integration potential, hedged (L94); the profile heading „(Modifizierter ANP / Integratorin?)“ with its own question mark (L223), a specialised protecting ANP (L225), internal Wächterin and gatekeeper (L226), her arc (L228); AEGIS sees her as anomaly or threat, as the brief has it (L191).
- **`tsdp`** (central, 3–12 quotations): the census's surfaces — `TSDP` L11, L17, L21, L25, L31, L49, … (28 lines). central (3–6): the frame of the analysis (L23–L25); ANPs and EPs (L39–L45); action systems (L47–L52); the three levels, tertiary the most complex (L54–L62); integration not erasing parts (L94) — reported theory, applied to the system.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: `Kohärenz Protokoll` the title and, at L321 and L371, a heading read on aegis.
- `personas`: `Depersonalisation` (near `persona`). occurrence: `Depersonalisation` a dissociative symptom, not a persona.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: „elf identifizierten Persönlichkeitsanteile“ (L17), sorted into primary and secondary ANPs, EPs, Selene modified and Argus emerging (L41–L45); the Kernwelten Co₁, McL, B, Ly (L176), two analysed with question marks (L180–L181).

**Not promoted:** Paradoxon X, the PP-codes, the action systems, phobias between parts, the matrix of internal conflicts, Zeugenschaft, the integration table, the plot recommendations.

**One reader**: every page above and the record q3.

**Chapter readings**: none — the document names no chapter.
