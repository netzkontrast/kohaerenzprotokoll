# Brief — readings from document 518 (step 6)

1 document, one reader, one batch: `ingest-518`. Files go to `Plan/runs/ingest-518/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 518 | `roman-als-transformativer-prozess-alchemie-der-erzaehlung` | 2025-10-16 | „the alchemy-of-narration blueprint“ (an unsigned German strategy report) | reads the plot through alchemical stages, narrative therapy and a theory of fictional existence: Kael's arc and the Kael–AEGIS conflict mapped onto Nigredo to Rubedo (L44–L48), an „Erwachte Narrative Entität“ persisting through the reader's attention, and epilogue techniques; it calls itself a blueprint and a practical guide (L121, L160), claims recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (227 lines for `roman-als-transformativer-proz`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A strategy report: write „the alchemy-of-narration blueprint reads/proposes …“. Theorists and therapists are named or cited in adjectives (e.g. „jungianischer“, L38): never write a name, never quote a span containing one or such an adjective — cut before. The reader is called 'O'. No gendered pronoun for Kael, Juna, AEGIS or the parts in our own prose; quotations stay verbatim (the document writes „Seine“, „Er“, „Sie“).

## Pages — document 518, `roman-als-transformativer-prozess-alchemie-der-erzaehlung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L34, L36, L40, L45, L46, L58, … (11 lines). central (4–8): AEGIS not a simple villain but a perfect externalisation of Kael's shadow archetype — and the reader's (L34); its obsession with sterile logic, control and suppressing chaotic emotions (L34); its „psychologische Kriegsführung“ paradoxically becoming the catalyst of Kael's integration, its methods iatrogenic, AEGIS an unwilling therapist (L40); AEGIS's sterile Logos unable to grasp Juna/V's Eros (L36).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L58. minor (1–4): the world kept by the reader's attention against „Narrative Entropie“ (L64); the world decaying when the reader's interest fades (L64); L58 as the sweep found it.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L36, L47, L190. minor (1–4): Juna/V, the „exilierten Ursprungs-Ich“, assigned to the integration of the Anima/Animus archetype (L36); representing the soul and the source of true connection (Eros) (L36).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L26, L30, L32, L34, L38, L40, … (40 lines). central (4–8): Kael's starting state of „tertiären strukturellen Dissoziation“ as the chaotic prima materia, the fragmented parts (Lex, Nyx, Kiko) its disparate elements (L32); the healed Kael who reached „funktionale Multiplizität“ becoming a living archetype of the Selbst (L38 — cut before the adjective); the outer conflict with AEGIS as a causal mechanism of inner individuation (L40); the awakened Kael reaching a permanent, stable form of existence after the story, an „Erwachte Narrative Entität“ (L72); Kael's final role as „Gärtner“, fighting Narrative Entropie (L104); the last line as an open question to 'O', „Ist es schön?“ or „Reicht das?“ (L168).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L32. minor (1–4): Kiko named among Kael's fragmented parts (L32).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: an occurrence — the title.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L32. minor (1–4): Lex named among Kael's fragmented parts (L32).
- **`logos`** (minor, 1–4): the census's surfaces — `Logos` L36, L40. not read: an occurrence — `Logos` as AEGIS's sterile logic against Eros (L36, L40), not the figure LogOS.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L38. minor (1–4): the healed Kael reaching „funktionale Multiplizität“ by integrating the parts (L38 — cut before the adjective).
- **`negentropie`** (minor, 1–4): the census's surfaces — `Negentropie` L93, L108. minor (1–4): Kael's role producing Negentropie, the reader's attention keeping the world against Narrative Entropie (L93, L108 — as the census lists them).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L86, L104. minor (1–4): L86, L104 as the census lists them (Kael's fight against the drift into the Nichts Rauschen) — read and quote one or two.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L32. minor (1–4): Nyx named among Kael's fragmented parts (L32).
- **`risse`** (minor, 1–4): the census's surfaces — `Glitches` L62. minor (1–4): the Glitches as the census lists them (L62) — read if it names the novel's Risse; otherwise not read.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie`: `Narrative Entropie` (near `entropie`). read on entropie (above): `Narrative Entropie`.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). an occurrence: the project name.


**Record entries:** none.

**No chapter readings**: `Kap` 0, `Kapitel` 0; only the Epilog is named.

**Not promoted:** Erwachte Narrative Entität (ENE), Narrative Entropie as a surface, Esse est percipi, Gärtner, the alchemical stages, the archetypes, the narrative-therapy and object-relations vocabulary, Sosein, Gegenstandstheorie, and the concepts named after people.

**One reader**: every page above.
