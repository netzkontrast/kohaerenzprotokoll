# Brief — readings from document 333 (step 6)

1 document, one reader, one batch: `ingest-334`. Files go to `Plan/runs/ingest-334/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 333 | `bewerte-kishotenketsu-als-zentrales-narrativ` | 2025-07-29 | „the Kishōtenketsu evaluation“ (an unsigned German evaluation with a verdict) | lays the four acts Ki, Shō, Ten, Ketsu onto the novel's plot, lists strengths and demands, and recommends the form as the central frame („Meine definitive Empfehlung lautet“); its mapping is its own reading of the plot, its standing („eine strukturelle Notwendigkeit“) recorded, not applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (86 lines for `bewerte-kishotenketsu-als-zent`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An evaluation: write „the Kishōtenketsu evaluation maps / recommends …“; the plot it lays onto the acts is its own reading, not a record of the novel. Say which act a line belongs to. Quotations inside its own „…“ quotation marks are cut before the inner marks.

## Pages — document 333, `bewerte-kishotenketsu-als-zentrales-narrativ`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L28, L37, L46, L55, L62, L63, … (8 lines). minor (1–3): Ki: AEGIS's rigid order as the status quo (L28); AEGIS as the externalisation of the inner conflict (L62); Ten: an influence incomprehensible to AEGIS (L46).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L46. minor (1–3): Ten: the Juna/V connection manifesting as a strong influence (L46); its identity among the mysteries to sustain (L73).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L28, L37, L46, L55, L62, L72, … (8 lines). minor (1–3): Ki: Kael met in his fragmented state (L28); Ketsu: Kael does not defeat AEGIS in a final battle (L55); the form centring the story on Kael's psychological journey (L62).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L37. minor (1–3): Shō: Kael beginning to understand the rules of the Kernwelten (L37).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L37. minor (1–3): the same Shō line naming Kiko among Kael's inner parts (L37).
- **`kishotenketsu`** (minor, 1–4): the census's surfaces — `Kishōtenketsu` L11, L15, L19, L62, L83, L85. minor (1–3): the form as a four-act structure from Chinese and Japanese poetry, generating tension without confrontation (L19); the verdict, ideal structure mirroring „Integration vs. Negation“ (L15); the closing recommendation and its claim of structural necessity (L83, L85).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: an occurrence (see below).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L37. minor (1–3): Shō: Kael becoming aware of his inner parts, named Lex, Nyx, Kiko (L37) — one line shared by lex, nyx, kiko.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L55. minor (1–3): Ketsu: Kael reaching „funktionale Multiplizität“ as the resolution (L55).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L37. minor (1–3): the same Shō line naming Nyx among Kael's inner parts (L37).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L46. not read: an occurrence (see below).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L37. minor (1–3): Shō: Kael experiencing the „Risse“ more intensely (L37).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L72. not read: an occurrence (see below).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `juna`: `Juna/V-Verbindung` (near `juna`), `Juna/V` (near `juna`). `Juna/V` and `Juna/V-Verbindung` are read on juna; `Kohärenz Protokoll` is the novel's title, an occurrence.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). `Juna/V` and `Juna/V-Verbindung` are read on juna; `Kohärenz Protokoll` is the novel's title, an occurrence.


**Pages not read:** `kohaerenz` (L15 the title), `realitaetsebenen` (L46 generic), `ueberwelt` (L72 generic simulation) — occurrences.

**Record entries:** none.

**Not promoted:** the acts Ki, Shō, Ten, Ketsu as labels, the three-act contrast, „der lebende Gödel-Satz“, the strengths and demands.

**One reader**: kishotenketsu, kael, aegis, juna, multiplizitaet, kern-welten, risse, lex, nyx, kiko.

**Chapter readings**: none — the evaluation maps acts, not chapters.
