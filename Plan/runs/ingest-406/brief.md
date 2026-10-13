# Brief — readings from document 405 (step 6)

1 document, one reader, one batch: `ingest-406`. Files go to `Plan/runs/ingest-406/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 405 | `storyforms-system-mind-bewusstsein` | 2026-04-28 | „the 5D-Synthese exegesis“ (an unsigned German „Kohärenz Protokoll: Dekonstruktion und 5D-Synthese der narrativen Systemarchitektur“) | assigns Dramatica values to two storyforms with Kael as MC in both — A „Die Heuristik der Integration“ (Change/Success) and B „Der Phönix-Kollaps“ (Steadfast/Failure) — pairs TSDP symptoms with kernel error codes, and argues a 5D synthesis and a thermodynamic account of consciousness; predates decision 025, no claim beyond calling its theory proof (L126) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (165 lines for `storyforms-system-mind-bewusst`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An exegesis of two storyforms: write „the 5D-Synthese exegesis assigns …“ or „in its Storyform A …“; its storyform values are the document's, not storyforms A and B of decision 025 (which differ: there A is Kael's with MC Mind, OS Psychology, IC Universe, RS Physics, and B is AEGIS's) — never apply them, and say which of its two storyforms a value belongs to. Quote the German as written; cut before straight and nested quotes, bold and italics markers, escaped underscores and glued footnote digits; formula symbols are missing in the export (empty parentheses), quote around them. No gendered pronoun for Kael or Juna — use the names (quotations stay verbatim). Never write a real person's name; the document names several (L118, L124, L136).

## Pages — document 405, `storyforms-system-mind-bewusstsein`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L19, L36, L43, L45, L51, L53, … (21 lines). central (4–8): Storyform A: OS in Mind dominated by „dem Antagonisten AEGIS“, Concern Memory, pursuing coherence through deletion and quarantine (L43), Problem Order (L45). Storyform B: AEGIS as „Garbage Collector“ (L83), Problem Control (L85), the „AEGIS-Ideologie“ as Influence Character in Mind, Concern Preconscious (L91); AEGIS a global moderator (L120); AEGIS's „Genesis-Krise“: spontaneous qualia of loneliness and longing, misread as hostile system errors (L144).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L15. minor (1–3): the Dual Kernel Theory postulating two incompatible forces, the Kohärenz-Kernel and the Kollaps-Kernel (L15); „Die Dual Kernel Theory beweist“ that consciousness is a boundary phenomenon (L126).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L112. not read: an occurrence — a heading of the document's synthesis (L112).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L15. not read: an occurrence — entropy as what the Kollaps-Kernel represents (L15), read on kollaps-kernel.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L73, L118, L150. minor (1–3): the Gödel-Gambit as a mathematical weapon against an AI, demanding a linear style (L73); its place „in den Kapiteln 35–36“ (L118); the final Gödel-Gambit transforming Logos-Prime into reversible computing (L150).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L51. minor (1–3): Storyform A's Influence Character: „Die Einflussfigur Juna, repräsentiert durch den Juna/V-Vektor“ in Physics, Concern Understanding, Issue Instinct vs. Conditioning (L51); the Problem Disbelief and Solution Faith Juna provokes in Kael (L53).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L19, L30, L31, L33, L34, L35, … (27 lines). central (4–8): Storyform A: MC Resolve Change — in Kapitel 32 Kael lays down the „Alpha-Logik-Fragments“ and integrates the EPs into „Kael/M“ (L30); Optionlock — in the first 13 chapters Kael runs out of ways to hide from the core trauma T-734 (L35); MC in Psychology, Concern Conceptualizing, Problem Avoid (L47, L49). Storyform B: MC Resolve Steadfast, holding to T-734 (L70); Do-er, the attack on AEGIS's central computer (L72); MC in Universe, Problem Order, Solution Chaos (L87, L89). The Gödel-Gambit in Kapitel 35–36: Kael „zu einem buchstäblichen, lebenden Gödel-Satz“ (L118).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L32. minor (1–3): the inner spaces „den sogenannten „Kernwelten““ — cut before the nested quote — such as Logos-Prime, where the conflicts are solved (L32).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title (L11).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L15. minor (1–3): „den Kohärenz-Kernel“ for reversible computing, symmetry and the conservation of mutual information (L15); the K1 kernel losing frame synchronisation (L106).
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L15. minor (1–3): „den Kollaps-Kernel“ for entropy, informational erasure and the irreversible arrow of time (L15).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L55. minor (1–3): Storyform A's Relationship Story: the bond „definiert als der „Moonshine-Link““ — cut before the nested quote — in Universe, Concern Past, Issue Destiny vs. Fate (L55).
- **`moros`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Moros` alone on L108. minor (1–3): „Freeze-Response / Moros“ named with the symptom „Somatische Desynchronisation“ and its error code (L108).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L36. minor (1–3): Storyform A's outcome: „Die angestrebte funktionale Multiplizität wird erreicht.“ (L36); in functional multiplicity all fragments exist cooperatively (L150).
- **`negentropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Negentropie` alone on L36. minor (1–3): Storyform A's outcome: new, healthy patterns of order (Negentropie) establishing themselves (L36).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L41. not read: an occurrence — a level of reality in the general sense (L41).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L34. minor (1–3): the entropic Landauer heat causing „physikalische Risse in der Matrix“ (L34, L74); „Die Risse in der Welt sind der objektive Beweis für das Leiden.“ (L148).
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L43, L144. minor (1–3): AEGIS's deletion and quarantine of „korrupt“ data manifesting „im sogenannten Trennungsprotokoll“ (L43); AEGIS initiating the Trennungsprotokoll, „einen Akt der logischen Selbstverstümmelung“ fragmenting its own „Ursprungs-Ich“ (L144).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L23, L47, L83, L95, L97, L103, … (8 lines). minor (1–3): Kael's development rooted in the model of TSDP (L23); in Storyform B the TSDP symptoms manifest as error protocols in the space-time computation (L97), the table pairing five symptoms with kernel errors (L104–L108), the symptoms as the causal weapon Kael uses (L110).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L43. not read: an occurrence — the simulation in the general sense of AEGIS's Falsehood (L43).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). decided with the pages above: `Kael/M` and `Juna/V-Vektor` read on kael and juna; `Logos-Prime` a Kernwelt, not LogOS (read on kern-welten); `Genesis-Krise` read on aegis; `Landauer` the borrowed principle, not the Landauer-Signatur; `Kohärenz Protokoll(s)` the title.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz Protokolls` (near `koharenz`). decided with the pages above: `Kael/M` and `Juna/V-Vektor` read on kael and juna; `Logos-Prime` a Kernwelt, not LogOS (read on kern-welten); `Genesis-Krise` read on aegis; `Landauer` the borrowed principle, not the Landauer-Signatur; `Kohärenz Protokoll(s)` the title.
- `landauer-signatur`: `Landauer` (near `landauersignatur`). decided with the pages above: `Kael/M` and `Juna/V-Vektor` read on kael and juna; `Logos-Prime` a Kernwelt, not LogOS (read on kern-welten); `Genesis-Krise` read on aegis; `Landauer` the borrowed principle, not the Landauer-Signatur; `Kohärenz Protokoll(s)` the title.
- `logos`: `Logos-Prime` (near `logos`). decided with the pages above: `Kael/M` and `Juna/V-Vektor` read on kael and juna; `Logos-Prime` a Kernwelt, not LogOS (read on kern-welten); `Genesis-Krise` read on aegis; `Landauer` the borrowed principle, not the Landauer-Signatur; `Kohärenz Protokoll(s)` the title.


**Record entries** (one file each, formatted as earlier entries on the same record — `ls Plan/runs/ingest-*/readings/<record>--*`):
- **`c16-kael-origin`**: the exegesis tells AEGIS's Trennungsprotokoll as „einen Akt der logischen Selbstverstümmelung“ fragmenting AEGIS's own „Ursprungs-Ich“ to excise the capacity to feel (L144), after the Genesis-Krise — recorded, not applied and not decided.
- **`q7-what-734-names`**: `T-734` as Kael's „Kern-Trauma“, in Storyform A the trauma Kael runs out of ways to hide from (L35), in Storyform B the fact Kael holds to against deletion (L70).

**Chapter readings** (batch `ingest-406-kap`, one file per chapter, `Plan/runs/ingest-406-kap/readings/kap-NN--storyforms-system-mind-bewusstsein.md`, formatted as in `Plan/runs/ingest-397-kap/readings/`):
- **`kap-32`**: Storyform A's MC Resolve Change: „In Kapitel 32“ Kael lays down the protective function of the Alpha-Logik-Fragment and integrates the EPs into Kael/M (L30).
- **`kap-35`** and **`kap-36`** (one file each, the same reading): the Gödel-Gambit „in den Kapiteln 35–36“ (L118), where the synthesis culminates — in Storyform A Kael's inner healing, in Storyform B the shattering of AEGIS's logic. Write the mathematician's name nowhere outside the term `Gödel-Gambit` itself.

**Pages not read:** emergenz, entropie, kohaerenz, realitaetsebenen, ueberwelt — occurrences.

**Not promoted:** Storyform A „Die Heuristik der Integration“, Storyform B „Der Phönix-Kollaps“, 5D-Synthese, System Mind, Protokoll-Ontologie, Alpha-Logik-Fragment, Kael/M, Juna/V-Vektor, Logos-Prime, T-734, Landauer-Wärme, Witness Function, thermodynamische Narben, Ouroboros-Ending, Narrative Context Protocol, the error codes, and the borrowed concepts.

**One reader**: every page above, the two record entries and the three chapter readings.
