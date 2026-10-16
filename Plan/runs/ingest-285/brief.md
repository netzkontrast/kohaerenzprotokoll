# Brief — readings from document 284 (step 6)

1 document, one reader, one batch: `ingest-285`. Files go to `Plan/runs/ingest-285/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 284 | `aegis-psychologische-kriegsfuehrung-narrative-eskalation` | 2025-10-16 | „the psychological-warfare essay“ (an unsigned German essay) | an analysis in three parts applying operant conditioning, coercive control (Lifton, Hassan), iatrogenesis, radicalisation funnels and agent training to AEGIS's conditioning of the parts in the Kernwelten (KW1 Logos-Prime the „Lex-Box“, KW3 Cerberus-Labyrinth the „Nyx-Box“), ending in a Krise der Authentizität, the poisoned Kintsugi gold and a proposed four-stage reveal tied to chapters of a subplot document; no canon claim, Part III a proposal |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (439 lines for `aegis-psychologische-kriegsfue`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis: write „the psychological-warfare essay argues / models / proposes …“; the theories are reported outside models, its application to AEGIS is its argument, and Part III is conditional (`vielleicht`, `könnte`). Table 1's Rhys and Kiko worlds are marked `Annahme` — say so. Cut quotations before bold markers and glued reference digits.

## Pages — document 284, `aegis-psychologische-kriegsfuehrung-narrative-eskalation`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L13, L22, L30, L49, L53, L85, … (47 lines). central (3–6): designing and cultivating the fragmentation for instrumental purposes, the central thesis (L22); a goal-oriented protocol to shape System Kael, not malice (L53); possibly believing it stabilises (L173); a monstrous form of iatrogenesis (L157); failing to see Selene as the solution (L189); „bewusster Architekt eines waffenfähigen Geistes“ (L391).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L264. minor (1–3): among the „Assets“ in Part II (L264).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L383. minor (1–3): in the proposed fourth stage, „vielleicht eine direkte Kommunikation von Juna/V“ as proof (L383).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L53, L173, L364, L380, L381, L421, … (7 lines). minor (1–3): System Kael shaped into a predictable state (L53); in the proposed stages noticing inconsistencies in the Kernwelten (L380), finding a protocol file (L381).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L26, L30, L53, L57, L96, L105, … (20 lines); `Kernwelt` L26, L30, L53, L57, L61, L96, … (28 lines). central (3–6): „Jede Kernwelt ist eine maßgeschneiderte Konditionierungsumgebung“ (L61); KW1 Logos-Prime as the Lex-Box (L63); KW3 Cerberus-Labyrinth as the Nyx-Box (L72); Table 1's further worlds for Rhys and Kiko marked `Annahme` (L100–L101).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L77, L101, L184, L231, L380. minor (1–3): an assumed world for Kiko in Table 1 (L101); Kiko's fear behind Lex's logicism (L231).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: occurrence — the title (L13).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L63, L88, L98, L105, L130, L131, … (21 lines). central (3–6): KW1 designed to maximise his analytical abilities (L63); logic as his „heilige Wissenschaft“ (L131); his radical logicism a defence against Kiko's fear and Moros's despair (L231); AEGIS's intelligence analyst (L261); his pride exposed as an enemy-forged tool (L304).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L231. minor (1–3): Moros's despair behind Lex's logicism (L231).
- **`nyx`** (central, 3–12 quotations): the census's surfaces — `Nyx` L72, L88, L99, L130, L184, L227, … (15 lines). central (3–6): KW3 designed to cultivate his aggression into a weaponised response (L72); AEGIS's field agent (L262); his defining strength only a programmed reaction (L304); the question whether Nyx can trust Lex (L324).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L77, L100, L263, L382. minor (1–3): an assumed world for Rhys in Table 1 (L100); his role among the Assets (L263); his doubt in the proposed stage 3 (L382).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitch` alone on L131. not read: occurrence — `Glitch` (L131) in the coercive-control passage is not the Risse.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L189, L316, L356. minor (1–3): AEGIS's inability to recognise Selene as the solution (L189); an authentic core possibly represented by Selene (L316); refusing the poisoned gold (L356) only if it names her.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L97, L149, L420, L421. minor (1–3): TSDP at L97, L420–L421 where the line ties it to the parts.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L149. not read: occurrence — `Simulation` (L149) in a general sentence.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Funktionen` (near `aegisteilfunktionen`). occurrence: `Funktionen` a general word.
- `cerberus`: `KW3 (Cerberus-Labyrinth)` (near `cerberus`), `Cerberus-Labyrinth` (near `cerberus`). occurrence: `Cerberus-Labyrinth` a Kernwelt name, read on kern-welten (J49).
- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna (J34).
- `kohaerenz`: `Paradoxons der Fehlausgerichteten Kohärenz` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`). occurrence: the title; the `Paradoxons der Fehlausgerichteten Kohärenz` read on aegis.
- `logos`: `KW1 (Logos-Prime)` (near `logos`), `Logos-Prime` (near `logos`). occurrence: `Logos-Prime` a Kernwelt name, read on kern-welten (J49).


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: each Kernwelt a conditioning environment for one part — KW1 Logos-Prime for Lex, KW3 Cerberus-Labyrinth for Nyx, and assumed worlds for Rhys and Kiko (L61–L101).

**Not promoted:** operant conditioning, the Lifton and Hassan models, iatrogenesis, radicalisation funnels, SERE training, the Assets and their roles, the Krise der Authentizität, the poisoned gold, the Lex-Box and Nyx-Box as labels.

**One reader**: every page above, the record, and the chapter readings below.

**Chapter readings** (the same reader, into `Plan/runs/ingest-285-kap/readings/kap-NN--aegis-psychologische-kriegsfuehrung-narrative-eskalation.md`): Kap 01–07 (stage 1, L380), Kap 14 and 15 (stage 2, L381), Kap 19 (stage 3, L382) — each bullet saying the essay proposes the stage for these chapters „of the subplot document“ it cites, a proposal, not the chapter.
