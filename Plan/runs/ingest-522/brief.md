# Brief — readings from document 522 (step 6)

1 document, one reader, one batch: `ingest-522`. Files go to `Plan/runs/ingest-522/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 522 | `research-prompt-kohaerenz-protokoll-verification-md` | 2026-04-29 | „the verification prompt“ (an English research prompt with a German title) | tells a research agent to audit the framework's theoretical axes against published sources; the world's names occur only inside the claims it reports the framework making („The framework claims“); it calls itself ready for autonomous research execution (L1421), a claim recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (1428 lines for `research-prompt-kohaerenz-prot`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan for an audit that reports claims: write „the verification prompt reports the framework as claiming …“ — the claims are the framework's as the prompt quotes them, never established and never the prompt's own; the prompt excludes the story itself from the audit (L125, L135). Real thinkers and researchers are named on several lines (L100, L114, L129 and others) and concepts carry people's names (`Landauer heat`, `Landauer's Principle`): never write a name, never quote a span containing one — cut before, or write the reading without the quotation. No gendered pronoun for Kael, Juna, AEGIS or the parts in our own prose; L1053's quotation contains one: cut before it.

## Pages — document 522, `research-prompt-kohaerenz-protokoll-verification-md`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L342, L656, L1053, L1074, L1078. minor (1–4): the reported claims: AEGIS seeks coherence as K\_0 in an example trigger setting Axis I against Axis II (L342); AEGIS's attempt to erase the dense structure overloading its own hardware (L1053, cut the span free of names and of the pronoun); AEGIS „not destroyed but enters a state of permanent, broken paradox“ (L1078), under the step heading Algo Melancholie (L1074).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L1047. minor (1–4): named in the Phase 6 heading with Climax Inversion and Autobiographical Anchor (L1047); the step it heads reports AEGIS in terminal self-reflection (L1074, L1078).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L98, L129, L245, L362, L498, L640, … (9 lines). minor (1–4): one of the seed axes (L362, L498); the prompt asks whether DKT is an established framework or the framework's own synthesis (L640) and to log it if novel (L644); the example trigger reports DKT treating trauma as a K\_1 structure buffering against K\_0 erasure (L245).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L538, L871, L875. minor (1–4): „Juna as observational lens“ under Axis VII & VIII (L538); the reported claim that the orbifold construction is the mechanism for Juna's observation, allowing access to erased data (L871, L875).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L125, L656, L1053. minor (1–4): the reported claim about the energy source for Kael's self-repair mechanisms (L656 — quote only the first span, the second names a person's concept); Kael dropping the amnesic barriers between Lex, Nyx, Kiko and Lia (L1053 — cut before the pronoun); the exclusion example (L125) is an occurrence.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L724, L1053. minor (1–4): one of four alters the framework is reported to model as discrete functional modules (L724, L728); named among the barriers Kael drops (L1053).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L724, L1053. minor (1–4): one of four alters the framework is reported to model as discrete functional modules (L724, L728); named among the barriers Kael drops (L1053).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L724, L1053. minor (1–4): one of four alters the framework is reported to model as discrete functional modules (L724, L728); named among the barriers Kael drops (L1053).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L845, L849, L1173. minor (1–4): the reported claim that the relation 196884 = 196883 + 1 validates the Moonshine-Link (L845, L849); listed as a major assumption to falsify (L1173).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts-Rauschen` L990. minor (1–4): the reported claim that the reader's cognitive effort in resolving 39 fragmented chapters and conflicting footnotes is the literal repair energy counteracting the Nichts-Rauschen (nothingness static) (L990).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L724, L1053. minor (1–4): one of four alters the framework is reported to model as discrete functional modules (L724, L728); named among the barriers Kael drops (L1053).
- **`tsdp`** (central, 3–12 quotations): the census's surfaces — `TSDP` L100, L114, L125, L129, L362, L370, … (25 lines). central (3–8): one of the seed axes (L362, L498); the framework is reported to use TSDP to model four alters as „discrete functional modules“ with „informational firewalls“ (L728); TSDP applicability as a major assumption to falsify (L1173); the prompt's search vocabulary for its limits (L370). Lines L100, L114 and L129 name people: not quoted.
- **`vortex`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Vortex` alone on L1049. minor (1–4): the step heading „Verify Vortex Inversion mechanics“ (L1049) — the reported Climax Inversion; read only if the page's Vortex is the same thing, otherwise not read: an occurrence.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). an occurrence: `Mnemosyne-Archipel` is the reported server substrate (L625), a different term from the page's; the prompt itself warns against assuming it is published (L1273).
- `vortex`: `Vortex Inversion` (near `vortex`). read on vortex above (L1049), if the reader finds the page's term is the same.


**Record entries:** none.

**No chapter readings**: no chapter is named (`Kapitel` 0, `Kap` 0; „39 fragmented chapters“ at L990 is a count, read on nichts-rauschen).

**Not promoted:** the audit's machinery (Contradiction Log, Hidden Contradiction Discovery Protocol, Assumption Stability Audit, Source Triangulation, Adversarial Query Expansion, ReAct, RISEN), the axis names, the mathematical and psychological borrowed concepts, the foundational phone call's Silence, and the concepts named after people.

**One reader**: every page above.
