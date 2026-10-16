# Brief — readings from document 285 (step 6)

1 document, one reader, one batch: `ingest-286`. Files go to `Plan/runs/ingest-286/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 285 | `fragen-zu-existenz-agency-und-realitaet` | 2025-11-13 | „the 39-questions synthesis“ (an unsigned German report) | a synthesis answering 39 numbered questions in three parts: the genesis of AEGIS (Leere, Genesis-Krise, Komponente 734, Überwelt, Kernwelten, Kohärenz Protokoll), a fourth act „Agency-Protokoll“ over chapters 40–52 with a 13-row table, and real-world physics and philosophy; much of it retells cited sources by reference mark; it calls its table „die kritische Blaupause für Akt IV“ (L180), its claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (309 lines for `fragen-zu-existenz-agency-und-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A synthesis that retells cited sources: write „the 39-questions synthesis retells / proposes …“; where a sentence carries a reference mark (1, 4, 6, 7), it reports that source — say so. The fourth act (chapters 40–52) is a proposed continuation beyond the 39 chapters, not the novel as decided. Cut quotations before bold markers and glued reference digits.

## Pages — document 285, `fragen-zu-existenz-agency-und-realitaet`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L22, L28, L32, L63, L75, L77, … (32 lines). central (3–6): its self-definition by negation, an autopoietic loop (L63); its rigid identity making the catastrophe inevitable (L71); the unclassifiable truth as an unsolvable paradox (L75); its only answer to complexity isolation, fragmentation and negation (L99); in the fourth act still the antagonist, but changed (L134); the reorganised AEGIS's offer refused (L165) — retold from cited sources.
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L190. minor (1–3): „Argus (Der metakognitive Beobachter)“ in the table's row for chapter 43 (L190).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L53. minor (1–3): the heading „Emergenz aus der Leere“ for the genesis of the Ich (L53), with the section's lines if they add.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L22. minor (1–3): the Genesis-Krise as the document retells it (L71–L79).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L177. minor (1–3): the Catalyst Provocateur throughline, Juna/V demanding a shared trauma truth instead of „falsche Kohärenz“ (L177); „Juna/V (Das Exil)“ in chapter 48's row (L195).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L22, L99, L117, L132, L150, L151, … (15 lines). central (3–6): the fourth act as Rubedo, the multiplicity turned from a pathology into the main operative strength (L117, L132); in chapter 40 the multiplicity once a bug (L150); in chapter 45 an inner conflict triggered (L152); in chapter 47 a coordinated action (L154).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L91, L96, L249. minor (1–3): „isolierte Sub-Simulationen“ (L91), part of AEGIS's pattern of isolation (L99).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L22. not read: occurrence — `Kohärenz` (L22) within the title phrase.
- **`komponente-734`** (minor, 1–4): the census's surfaces — `Komponente 734` L75, L79, L97, L165, L291. minor (1–3): the Ich fragment, „jetzt“ Komponente 734, fragmented by force as the ultimate act of self-preservation (L79); split off by the Kohärenz Protokoll as an internal threat (L97).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L132, L153, L154, L193. minor (1–3): in chapter 46 trying cold, rational system-to-system negotiation (L153).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L132, L165. minor (1–3): functional multiplicity from a pathology to the primary operative strength (L132); chapter 51 (L165) only if it adds.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L132, L152, L153, L154, L192. minor (1–3): named among the parts in the fourth act (L132, L152–L154); chapter 45's row (L192) only if it adds.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L42, L89, L95, L302, L303. minor (1–3): the Leere not the philosophical nothing but „ein aktives, energetisches Substrat“ (L42); L89, L95 only if they name the Potentialmeer.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L132, L152, L153, L154, L191. minor (1–3): named among the parts in the fourth act (L132, L152–L154); his table row (L191) only if it adds.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L197. minor (1–3): „Selene (Die Integratorin/Puffer-ANP)“ in chapter 50's row (L197).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L32, L89, L91, L95. minor (1–3): „Sie ist keine physische Realität“ (L89); part of AEGIS's isolating pattern (L99).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). reading: `Genesis-Krise`, as retold (L71).
- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna (J34).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `falsche Kohärenz` (near `koharenz`), `Dekohärenz` (near `koharenz`). occurrence: the title, `falsche Kohärenz` (read on juna), `Dekohärenz` a physics term.
- `kollaps-kernel`: `Kollaps` (near `kollapskernel`), `Kollaps` (near `kollapskernelk0`). occurrence: `Kollaps` a general word.
- `nichts-rauschen`: `Rauschen` (near `nichtsrauschen`). occurrence: `Rauschen` not the Nichts Rauschen, unless the line names it.
- `persistenzgleichung`: `Persistenz` (near `persistenzgleichung`). occurrence: `Persistenz` a general word.
- `thermodynamischer-phaenomenalismus`: `dynamis` (near `thermodynamischerphaenomenalismus`), `dynamis` (near `thermodynamischerphanomenalismus`). occurrence: `dynamis` a Greek word.


**Record entries** (one file each):

- **`q7-what-734-names`**: the Ich fragment, „jetzt“ Komponente 734 (L79), split off as an internal threat (L97) — retold.
- **`q8-aegis-after-the-vortex`**: in a proposed fourth act AEGIS is still the antagonist but changed (L134), and the reorganised AEGIS makes an offer that is refused (L165).

**Not promoted:** the Agency-Protokoll and its three pillars, Rubedo, the Kintsugi-Protokoll, the Widerstandszelle, the Catalyst Provocateur throughline, chapters 41–52 as chapters (there are no pages for them), the quantum foam.

**One reader**: every page above, the two records and the chapter reading below.

**Chapter readings** (the same reader, into `Plan/runs/ingest-286-kap/readings/kap-40--fragen-zu-existenz-agency-und-realitaet.md`): Kap 40 only — „Die Qualia der Freiheit“ (L150), the first chapter of a proposed fourth act (L138). Chapters 41–52 have no pages; say so in the reading.
