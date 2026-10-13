# Brief — readings from document 262 (step 6)

1 document, one reader, one batch: `ingest-262`. Files go to `Plan/runs/ingest-262/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 262 | `kohaerenz-protokoll-the-official-master-story-guide-2` | 2025-10-15 | „the Master Story Guide“ (an unsigned English design guide) | „The Official Master Story Guide“: the novel's argument, laws, AEGIS, the 11-alter System Kael, the Kernwelten and the prose rules as requirements; it calls itself „the canonical blueprint“ (L15) and its alter table „the ground truth“ (L121) — its claims, not the project's canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (205 lines for `kohaerenz-protokoll-the-offici`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A guide that claims authority: write „the Master Story Guide prescribes / tabulates …“ and never repeat its „canonical“ as fact. Its requirements are its own (must, mandatory). Alter rows come from one table (L126–L136): quote the classification cell. Cut quotations before escaped asterisks, `\<br\>` and inner quotes; digits glued to words drop out (`KW1`).

## Pages — document 262, `kohaerenz-protokoll-the-official-master-story-guide-2`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L29, L39, L50, L59, L64, … (30 lines). central (3–6): a tragic, autopoietic system trapped by its own logic, not a villain (L75); its axiom „AEGIS is what AEGIS prevents itself from not being“ (L83); Discursive Logic treating each alter as a separate speaker (L93); the Paradox of Misaligned Coherence, reading Kael's healing as rising entropy (L95); the Gödel-Gambit and Algorithmic Melancholy (L101).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L128, L132, L134. minor (1–3): the alter table's row: „ANP (Protector)“ (L132); only the classification and, if it adds, motivation/fear.
- **`alters`** (minor, 1–4): the census's surfaces — `alters` L93, L134, L140, L142, L192, L202. minor (1–3): the „Canonical Society of Alters“, eleven rows (L125–L136); the arc as co-consciousness and shared responsibility, functional multiplicity (L140); integration as an offensive weapon (L142).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L136. minor (1–3): the alter table's row: „ANP/EP (Observer)“ (L136); only the classification and, if it adds, motivation/fear.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L77. not read: occurrence — `Genesis` at L77 is the heading „Ontological Genesis“; read on aegis if the section adds.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L101. minor (1–3): AEGIS's final arc, Kael as a „living Gödel-sentence“ (L101).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L133, L134. minor (1–3): the alter table's row: „EP (Sexualized/Control“ (L134); only the classification and, if it adds, motivation/fear.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L130. minor (1–3): `Juna/V` only in the relationship cells of Rhys and Lia (L130, L133), no row, no definition.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L21, L29, L40, L60, L91, L93, … (26 lines). central (3–6): „must not be treated as a singular character“ but as System Kael, modelled on TSDP (L108); the host row „ANP (Host)“ (L126); healing as the mechanism rewriting the physics of his prison (L21); the Dialetheical Mind; the arc to functional multiplicity (L140); his voice from aborted sentences to a choric we (L190).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L146, L154, L156; `Kernwelt` L146, L154, L156, L160. minor (1–3): „specialized simulated realities“ created by AEGIS (L156); the table of four: Logos-Prime, Mnemosyne-Archipel, Cerberus-Labyrinth, Kairos-Potentialis (L161–L164).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L126, L127, L128, L129, L130, L134, … (7 lines). minor (1–3): the alter table's row: „EP (Child/Freeze-Response)“ (L129); only the classification and, if it adds, motivation/fear.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — the title (L11).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L126, L127, L128, L129, L130, L132, … (9 lines). minor (1–3): the alter table's row: „ANP (Analyst)“ (L127); only the classification and, if it adds, motivation/fear.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L128, L130, L133, L134. minor (1–3): the alter table's row: „EP (Child/Ambivalent-Reaktion)“ (L133); only the classification and, if it adds, motivation/fear.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L62, L64. minor (1–3): „a non-local, sub-protocol phenomenon“ (L64), structurally invisible to AEGIS's sensors (L69).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L135. minor (1–3): the alter table's row: „EP (Collapse-Reaktion)“ (L135); only the classification and, if it adds, motivation/fear.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Das Nichts Rauschen` L41, L58. minor (1–3): the Nothingness Roar, written „Das Nichts Rauschen“, defined as high-entropy (L41, L58).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L126, L127, L128, L129, L132, L134, … (8 lines). minor (1–3): the alter table's row: „EP (Fight-Response)“ (L128); only the classification and, if it adds, motivation/fear.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L127, L129, L130, L133, L135, L136. minor (1–3): the alter table's row: „ANP (Carer)“ (L130); only the classification and, if it adds, motivation/fear.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L152. minor (1–3): the Risse at L152, with the Überwelt.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L126, L131, L135. minor (1–3): „ANP/EP (Integrator)“, „The only alter who actively works towards integration“ (L131).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L108, L110, L112, L125. minor (1–3): the psyche modelled on TSDP (L108); ANPs and EPs (L110–L112); the table's column „TSDP Classification & Function“ (L125).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L150, L152. minor (1–3): „The Überwelt is the purely information-based reality“ (L152); L150.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: a Kernwelt name in the table (L161–L164), read on kern-welten, not this page.
- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna (J34).
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: a Kernwelt name in the table (L161–L164), read on kern-welten, not this page.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title.
- `logos`: `Logos-Prime` (near `logos`). occurrence: a Kernwelt name in the table (L161–L164), read on kern-welten, not this page.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: a Kernwelt name in the table (L161–L164), read on kern-welten, not this page.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: eleven alters in a table it calls „the ground truth“ (L121, L126–L136); four Kernwelten, KW1 Logos-Prime, KW2 Mnemosyne-Archipel, KW3 Cerberus-Labyrinth, KW4 Kairos-Potentialis (L161–L164).
- **`q9-moonshine-link-boundary`**: „a non-local, sub-protocol phenomenon“ (L64), structurally invisible to AEGIS's sensors (L69).

**Not promoted:** the two orders, the Dialetheical Mind, LFI, Discursive Logic, the Paradox of Misaligned Coherence, the Kernwelt names, the prose rules, the metafictional techniques, Coherence Protocol.

**One reader**: aegis, kael, alters, the eleven alters' pages (lex, nyx, kiko, rhys, selene, alex, lia, isabelle, moros, argus), tsdp, kern-welten, ueberwelt, risse, moonshine-link, nichts-rauschen, goedel-gambit, juna and the records q3, q9.

**Chapter readings**: none.
