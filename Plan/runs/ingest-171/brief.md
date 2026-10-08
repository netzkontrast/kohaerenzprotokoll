# Brief — readings from document 171 (step 6)

1 document, one reader, one batch: `ingest-171`. Files go to `Plan/runs/ingest-171/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 171 | `kael-charakterarchitektur-und-konfliktdynamik` | 2025-04-28 | „the character architecture“ (titled `Kael: Charakterarchitektur und Konfliktdynamik für „Kohärenz Protokoll“ (Novelcrafter-Vorlage)`) | a German design report of 2025-04-28: an eleven-field profile for Kael as host and six personas in Novelcrafter codex format, built from IFS, TSDP and Jung, a map of Pressure Points and a matrix, open tensions posed as questions and three proposed figures; a design proposal, hedged throughout |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (423 lines for `kael-charakterarchitektur-und-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A design proposal: write „the character architecture profiles / proposes / asks …“; keep its hedges („könnte“, „legt nahe“, „Es ist denkbar“); section 5.1 (L313–L319) asks questions — a question is never an answer. Each persona has a role name and a quoted name (`Der Logiker / „Lex“`, L48): quote the role words, never across the inner quotes. German — quote as written; cut before inner quotes; glued reference digits follow sentences; the matrix is a markdown table with escaped bold (L292–L305).

## Pages — document 171, `kael-charakterarchitektur-und-konfliktdynamik`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L17, L31, L34, L35, L38, … (46 lines). central (2–4): Kael's interactions with AEGIS marked by control, manipulation and surveillance (L38); AEGIS's fragmentation of Kael possibly „eine gezielte Optimierung“, each persona a specialist for one world (L142); it reads the Moonshine-Link as error or instability (L232); read the persona-versus-AEGIS Pressure Points.
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L17, L33, L38, L142, L257, L303, … (8 lines). central (2–4): Kael's fragmented identity, „dem ‚Cache Kohärenz'-Problem“ — cut before the inner quotes (L17); „Cache Kohärenz als Konflikt (Der Fragmentierungs-Effekt)“ (L257); the matrix row (L303).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L32. minor (1–2): Kael corresponds to the „Host“ of DID models (L32).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L55. minor (1–2): Lex in conflict with the creative part, „Regeln vs. Emergenz“ (L55); the core conflict „Emergenz vs. Rigidität“ (L198).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L67, L72, L83, L99, L104, L203, … (9 lines). minor (1–2): the dominant world of the personas named there (L67, L72, L83) — read the lines.
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L38, L56, L72, L88, L104, L120, … (14 lines). central (2–4): „Die Guardians stellen Autoritäten dar, die mal als Bedrohung, mal als potenzielle Verbündete erscheinen“ (L38); the personas' conflicts with them (L56, L72, L88) — read the lines.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L34. minor (1–2): Kael's motive to keep or deepen the link to Juna/V (L34); Juna/V's role for Kael (L38); the ambivalence asked (L316).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L11, L15, L17, L21, L23, L24, … (72 lines). central (2–4): the host who „durch die von AEGIS auferlegten simulierten Realitäten“ navigates (L31); the DID host (L32); he experiences all Kernwelten, filtered by the dominant persona (L33); from passive victim to active participant (L40); the avatar of „M“ (L318).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L22, L32, L33, L38, L142, L319, … (7 lines). minor (1–2): Kael experiences „alle Kernwelten“ (L33); each persona tied to a world, perhaps AEGIS's „gezielte Optimierung“ (L142).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L64, L165, L212, L261, L294, L299, … (7 lines). central (2–4): „Das Kind / „Kiko““ — quote the role words (L64): read its profile (L64–L78) for function, world and Pressure Points.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (L11).
- **`konstrukt-stadt`** (central, 3–12 quotations): the census's surfaces — `Konstrukt-Stadt` L51, L56, L67, L72, L83, L99, … (14 lines). central (2–4): Lex's world, „Lex fühlt sich in dieser logikbasierten Welt zu Hause“ (L51); the other personas' relations to it (L56, L67, L72) — read the lines.
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L48, L49, L51, L156, L165, L183, … (13 lines). central (2–4): „Der Logiker“ (L48); at home in the Konstrukt-Stadt (L51); in conflict with the Shadow and the creative part (L55); its Pressure Points (L156, L165) — read the lines.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L232, L316. central (2–4): „Diese Personas können den ‚Moonshine-Link' spüren“ — Kai and Rhys (L232), quote around the inner quotes; AEGIS's blind spot (L236); its ambivalence asked (L316).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L40. minor (1–2): the integration path toward „funktionale Multiplizität“ (L40) — read the line.
- **`nyx`** (central, 3–12 quotations): the census's surfaces — `Nyx` L80, L146, L156, L174, L221, L241, … (13 lines). central (2–4): „Der Schatten“ (L80): read its profile (L80–L94) and Pressure Points (L156, L174, L221).
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Personas` alone on L15. minor (1–2): the report's „internen Anteile (Personas)“ (L15): Personas as Kael's inner parts — the page carries other documents' senses; say this one.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L318, L319, L354. minor (1–2): the question whether M connects to the Potentialmeer (L318); the simulated worlds against the external level and the Potentialmeer (L319) — questions.
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L51, L56, L67, L83, L99, L104, … (8 lines). minor (1–2): the dominant world of the personas named there (L51, L56, L67) — read the lines.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L96, L146, L174, L203, L232, L261, … (9 lines). minor (1–2): „Der Relationale Anteil“ (L96); with Kai it perceives the Moonshine-Link (L232).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L33. minor (1–2): Kael's interaction with the worlds marked by confusion — L33, read the line; the creative part's actions may cause unexpected „Risse“ (L120).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L128, L250, L302. minor (1–2): „Die Wächterin“, analogous to the IFS Self (L128).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L22, L32, L40, L50, L66, L82, … (9 lines). minor (1–2): TSDP explains the origin of fragmentation as a result of trauma (L22); the profiles' TSDP fields — read the lines.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L39. not read: L39's „Simulation vs. Authentizität“ is a theme, not the place — an occurrence.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` names the Guardians here, on guardians.
- `juna`: `Juna/V` (near `juna`), `Ambivalenz von Juna/V` (near `juna`). a reading — on juna above.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title.
- `risse`: `Der Glitch im System` (near `glitch`). occurrence: `Der Glitch im System` is a proposed figure's name (L347), a trickster archetype, not the Risse.


**Record entries** (one file each):

- **`c16-kael-origin`**: „die ursprüngliche Entität ‚M', deren Avatar Kael ist“ — quote around the inner quotes (L318), posed as a question of M's nature.
- **`c4-guardians-and-aegis`**: the Moonshine-Link „AEGIS' blinder Fleck“ (L236).
- **`q3-how-many-kern-welten-and-alters`**: six personas — Lex, Kiko, Nyx, Rhys, Kai, Selene (L48–L128) — each tied to a world (L142).
- **`q9-moonshine-link-boundary`**: Kai and Rhys can feel the link (L232); its ambivalence asked (L316).

**Not promoted:** Kai (no page; on Q3 and moonshine-link), the persona role names (Der Logiker, Das Kind, Der Schatten, Der Relationale Anteil, Der Kreativ-Intuitive, Die Wächterin), Pressure Points and their matrix, Novelcrafter, IFS, Jung, Positive Absicht, the three proposed figures, Paradoxon X, Heldinnenreise.

**Two readers**, disjoint: (1) kael, did, tsdp, multiplizitaet, lex, kiko, nyx, rhys, selene, personas, juna, moonshine-link and the records c16, q3, q9, c4; (2) aegis, cache-kohaerenz, guardians, kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, potentialmeer, emergenz, risse.
