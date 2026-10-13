# Brief — readings from document 229 (step 6)

1 document, one reader, one batch: `ingest-229`. Files go to `Plan/runs/ingest-229/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 229 | `projektanalyse-kohaerenz-protokoll-dis` | 2025-12-05 | „the project analysis“ (an unsigned German report) | a German report that reads the project's files and the novel's world together, ranks twenty files as „Golden Sources“ and gives three recommendations; most of it reads the work through a real person, which the wiki does not take up; very light pass: readings only on what it states of the novel's world, apart from any person |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (270 lines for `projektanalyse-kohaerenz-proto`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** **Privacy first.** Most of this report reads the work through a real person — its workflow sections (3, 4, 5) and its framing (sections 1, 2, 8). Nothing of that goes on any page: no quotation, no paraphrase, no mention that it does so, no word about any person's condition, workflow or safety. A reading may only state what the report says of the novel's world itself, and only where the sentence carries no reference to a person — cut every quotation before such a clause, and if a sentence cannot be cut cleanly, do not use it. Write „the project analysis describes …“. Its ranking of files and its canon claims about files are not readings. `--find` drops `$K\_1$`-style subscripts — quote around them.

## Pages — document 229, `projektanalyse-kohaerenz-protokoll-dis`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L34, L93, L100, L107, L108, L150, … (13 lines). not read: very light pass, privacy — its sentences about AEGIS frame the novel's conflict through a person.
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L100, L197, L224. not read: very light pass, privacy — named in the file ranking and recommendations (L100, L197, L224).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L19, L107. not read: very light pass, privacy — named in passages about the work's process (L19, L107).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L241. occurrence: `DID` stands in a reference title (L241).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L32. minor (1): Kollaps as „Das Prinzip der Entropie, der Informationslöschung und des irreversiblen Verfalls“ (L32) — the first clause only.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L166. occurrence: `Juna` stands in a listed file's title (L166).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L23, L34, L38, L40, L92, … (19 lines). not read: very light pass, privacy — its sentences about Kael frame him through a person; the only clean statement, the ANP-EP-Phobie as physical law, is read on risse.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L80. minor (1): „Die vier Kernwelten“ named with Logos-Prime and Mnemosyne (L80) — the first clause only, before the container framing.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L32, L85. not read: very light pass, privacy — named only within the K0 passage (L32) and a process passage (L85).
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L11, L15, L17, L31, L108, L137, … (34 lines). minor (1): Kohärenz as „Das Prinzip der Ordnung, der Informationserhaltung und der reversiblen Berechnung“ (L31) — the first sentence only; the title and file names are occurrences.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L31, L84, L88, L93. not read: very light pass, privacy — its sentences about Lex frame him through a person's process.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L85. not read: very light pass, privacy — named once in a process passage (L85).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L80, L85. not read: very light pass, privacy — named only beside the Kernwelten (L80, L85); read on kern-welten.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L32. not read: very light pass, privacy — named only in the K0 passage (L32).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L197. not read: very light pass, privacy — named only in the recommendations (L197).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L32, L107. not read: very light pass, privacy — named only in the K0 passage and a process passage (L32, L107).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L40, L99, L225. minor (1): the ANP-EP-Phobie „wird im Roman als physische Gesetzmäßigkeit dargestellt“: when Kael touches a trauma, „Risse“ arise in reality (L40) — cut before the sentence that follows.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L15, L36, L38, L200. minor (1): TSDP as the model by which „System Kael“ is constructed, ANPs and EPs (L38).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L199. occurrence: `Simulation` stands in a ranked file's gloss, „Simulation der Charaktere“ (L199).

- **`dkt`** (minor, 1): „Die "Dual Kernel Theory" (DKT) teilt die Realität in zwei Domänen“ — quote around the inner straight quotes (L29); Kohärenz and Kollaps (L31–L32), first clauses only.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `dkt`: `Dual-Kernel-Theorie` (near `dualkerneltheoriedkt`). a reading — the Dual Kernel Theory dividing reality into Kohärenz and Kollaps (L29–L32); minor, see the extra page below.
- `genesis`: `Genesis-Krise` (near `genesis`). occurrence: `Genesis-Krise` stands in a file title or gloss; not read.
- `juna`: `Juna/V` (near `juna`). occurrence: `Juna/V` stands in file titles; not read.
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: `Kairos-Potentialis` stands in a file title or gloss; not read.
- `kollaps-kernel`: `Kollaps` (near `kollapskernel`), `Kollaps` (near `kollapskernelk0`). occurrence: `Kollaps` is the K0 domain, read on dkt.
- `logos`: `Logos-Prime` (near `logos`). occurrence: `Logos-Prime` is named in a container passage (L84); not read (privacy).


**Record entries:** none — what the report says about records is entangled with its reading of a person.

**Not promoted:** everything — its constructs describe a workflow, not the novel's world.

**Written by the session** (very light pass, privacy first): dkt, kohaerenz, entropie, risse, kern-welten, tsdp.

**Chapter readings**: none.
