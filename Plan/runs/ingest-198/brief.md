# Brief — readings from document 198 (step 6)

1 document, one reader, one batch: `ingest-198`. Files go to `Plan/runs/ingest-198/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 198 | `kohaerenz-protokoll-narrative-architektur` | 2025-07-29 | „the System-Mind analysis“ (titled `Kohärenz Protokoll: Narrative Architektur`, „Eine definitive Analyse der System-Mind-Architektur“, L13) | a German analysis that lays the novel out as a Dramatica storyform — OS AEGIS, MC Kael, IC Juna/V, SS Kael and Juna/V — argues each part from borrowed theories, gives AEGIS two paths in the Gödel-Gambit, Kael's alters by the TSDP, Das Fundament, the four Kernwelten and the Fragment 'O', and answers the request's architect questions; it calls its table „die finale Dramatica Storyform“ (L24) — recorded, never applied; the author's storyforms are their own (decision 025) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (333 lines for `kohaerenz-protokoll-narrative-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis that calls itself definitive: write „the System-Mind analysis argues / proposes …“, never as settled. German — quote as written; cut before glued reference digits, before `\[User Query\]` and before inner quotes (its own „…“ stand inside many lines — the note shows where to cut).

## Pages — document 198, `kohaerenz-protokoll-narrative-architektur`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L22, L29, L42, L50, L52, L54, … (35 lines). central (2–4): the OS, „wird in der systemischen Entität AEGIS verankert“ (L42); its directive „ist daher kein von außen programmierter Befehl“ (L52); „Seine Handlungen sind keine Bosheit“ (L54); its tragedy, working perfectly as designed (L58); a hybrid cognitive architecture proposed (L66); after the Gödel-Gambit, Pfad A collapse or Pfad B transformation (L90, L92) — „eine tragische, erzwungene Evolution, keine Erlösung“ (L94).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L300. occurrence: `DID` stands only in a reference title (L300).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L32. occurrence: the general word in the table's summary (L32).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L80, L84, L112. minor (1–2): the confrontation named „Gödel-Gambit“ (L84); its two outcomes for AEGIS (L90, L92); read L80 or L112.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L102. minor (1–2): „Seine Guardians, die nun auf parakonsistenter Logik operieren“ in the transformed AEGIS (L102).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L22, L31, L32, L58, L86, L113, … (12 lines). central (2–4): Juna/V as the IC, one of four „Existenz-Matrizen“ (L22); the connection „ist kein Kommunikationskanal, sondern ein“ ontological exploit, an „architektonische Hintertür“ (L184); „Die bewusste narrative Ambivalenz bezüglich“ her nature (L194).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L22, L30, L32, L54, L58, L68, … (38 lines). central (2–4): the MC (L22); „Kaels innere Struktur ist rigoros nach dem Modell der TSDP“ (L129); his healing aims at functional multiplicity, not fusion (L139); Gnosis against AEGIS's Episteme (L210); his new role as Gärtner (L266) — cut before inner quotes; the Fragment 'O' as his final test (L241).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L102, L222, L226. minor (1–2): „sind nicht nur Schauplätze, sondern thematische Resonanzräume“ (L226); each world with a throughline — Logos-Prime OS, Mnemosyne-Archipel MC, Cerberus-Labyrinth SS, Kairos-Potentialis IC (L230–L233).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L129, L164, L264. minor (1–2): in the alter table (L164) — read the row.
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L13, L22, L74, L84, L94, L113, … (12 lines). central (2–4): the ultimate argument that „Kohärenz“ is not a static property but „sondern eine Aktivität“ (L278); read L74 or L113 for coherence in the argument.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L70, L76, L129, L139, L165, L264. minor (1–2): in the alter table (L165) — read the row; read L70 or L76.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L86, L113, L180, L184. minor (1–2): the Moonshine-Link as ontological exploit and „architektonische Hintertür“ (L184); read L86 or L113.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L76, L206. minor (1–2): healing aimed at „funktionalen Multiplizität“, not fusion (L139); read L76 or L206.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L52, L90. minor (1–2): read L52 and L90, where the Nichts Rauschen stands beside AEGIS's directive and Pfad A.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L72, L76, L129, L139, L163, L265. minor (1–2): in the alter table (L163) — read the row; read L72.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitches` alone on L104. minor (1–2): the `Glitches` at L104 — read the line (the transformed AEGIS).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L166, L278. minor (1–2): in the alter table (L166); the reader cast „in die Rolle von Kaels integrierendem Selbst (Selene)“ (L278).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L121, L129, L161. minor (1–2): „Kaels innere Struktur ist rigoros nach dem Modell der TSDP“ (L129); AEGIS as „externalisiertes Täterintrojekt“ (L131); the alter table's classifications (L161).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: the world's name (L232), on kern-welten.
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: the world's name (L233), on kern-welten.
- `logos`: `Logos-Prime` (near `logos`). occurrence: Logos-Prime is a world (L230), J49 — on kern-welten.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). occurrence: the world's name (L231), on kern-welten.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: five alters in the table — Kael (Host), Nyx, Kiko, Lex, Selene (L159–L166); four Kernwelten (L230–L233).
- **`q8-aegis-after-the-vortex`**: Pfad A collapse or Pfad B transformation, „eine tragische, erzwungene Evolution, keine Erlösung“ (L90–L94); its Guardians on paraconsistent logic (L102).
- **`q9-moonshine-link-boundary`**: an ontological exploit, an architectural back door (L184).

**Not promoted:** the Dramatica storyform and its terms (the author's storyforms are in Plan/storyform/, decision 025), Das Fundament as strange attractor, the Fragment 'O' and its three scenarios, Episteme and Gnosis, the Täterintrojekt, polyphone Prosa, the borrowed theories.

**Two readers**, disjoint: (1) kael, juna, moonshine-link, kiko, lex, nyx, selene, tsdp, multiplizitaet and the records q3, q9; (2) aegis, guardians, goedel-gambit, nichts-rauschen, kern-welten, kohaerenz, risse and the record q8.
