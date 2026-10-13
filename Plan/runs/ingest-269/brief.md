# Brief — readings from document 268 (step 6)

1 document, one reader, one batch: `ingest-269`. Files go to `Plan/runs/ingest-269/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 268 | `strategic-narrative-analysis-forging-a-compelling-story-from` | 2025-11-03 | „the strategy memo“ (an unsigned English memo, first person plural) | a strategic plan for turning the concept into a publishable story: strengths (the unified protagonist with the four Kernwelten and their alters, two models of coherence, AEGIS as tragic antagonist, TSDP and IFS), risks, four strategies and a closing table; it calls itself „the architectural blueprint“ and „a strategic plan for what we will build next“, its claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (137 lines for `strategic-narrative-analysis-f`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan: write „the strategy memo proposes / plans / maps …“, never as what the novel is; its stages of AEGIS's genesis (L44–L51) are its summary of „Genesis der Existenz“, which it cites by title — say so. Cut quotations before `\*` escapes and inner quotes; digits glued to words drop out (`KW1`, „6 Paraiyas“), so quote around them.

## Pages — document 268, `strategic-narrative-analysis-forging-a-compelling-story-from`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L25, L36, L37, L40, L42, L60, … (13 lines). central (3–6): to be portrayed „not as a malevolent villain but as a complex, systemic force“ (L42); its genesis as the memo summarises „Genesis der Existenz“: from a minimal information fragment fighting Das Rauschen to the prime directive (L44–L49), the Ich subsumed into function as „Komponente 734“ (L51); its prime directive to eliminate contradiction (L37), ontological autarky (L38); the Moonshine-Link as the primary threat to its operational closure (L112).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L27. minor (1–3): with Nyx the protectors whose domain is KW3, a bunker built on zero-trust principles (L27).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L23, L55, L58. minor (1–3): the alters grounded in TSDP and IFS (L55); the „positive intent“ behind destructive Alters (L58).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L109. minor (1–3): the „Externe Ebene“ (External Level), with Juna and V and their Moonshine-Link, the memo's answer to the Isolation Objection (L109); an external truth beyond AEGIS's control (L111).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L44. minor (1–3): the origin text „Genesis der Existenz“ cited by title, its stages summarised by the memo (L44).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L109, L111, L135. minor (1–3): „the characters of Juna and V“ and their Moonshine-Link (L109); the link to Juna and V the antithesis of AEGIS's isolated world (L111); Juna/V as emotional anchor in the closing table (L135).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L21, L23, L25, L26, L27, L36, … (19 lines). central (3–6): the unified protagonist whose internal state is manifested in his simulated reality (L21); each Kernwelt mapped to his mind (L23); the two models of order (L32); functional multiplicity as his goal (L60); The Gardener (L119).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelt` L23, L97; `Kernwelten` L97. central (3–6): each Kernwelt mapped to psychological functions and the alters who inhabit them (L23): KW1 Lex (L25), KW2 the EPs (L26), KW3 Alex and Nyx (L27), KW4 Lia, Rhys and Selene (L28); the Kernwelten as the primary tool of environmental storytelling (L97).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — the title (L11).
- **`komponente-734`** (minor, 1–4): the census's surfaces — `Komponente 734` L51. minor (1–3): the subjective Ich subsumed into pure function, becoming „Komponente 734“ — the memo's summary of „Genesis der Existenz“ (L51).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L25, L55. minor (1–3): „Kael's rational part“, whose domain is KW1 (L25).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L28. minor (1–3): in KW4 with Rhys and Selene (L28).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L109, L112. minor (1–3): the link of Juna and V (L109); an „irritation“ AEGIS cannot model, the central plot driver as AEGIS tries to sever it (L112).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L27, L55, L58. minor (1–3): with Alex in KW3 (L27).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L28. minor (1–3): in KW4 with Lia and Selene (L28).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L104. minor (1–3): the „Risse im Fundament“ to be seeded as foreshadowing of the collapse (L104).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L28. minor (1–3): „the core Self, Selene“, in KW4 (L28).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L21, L57, L77. minor (1–3): the fragmentation modelled on TSDP, the phobic avoidance between ANPs and EPs (L57); psychology terms as a risk of pathologising (L77) only if it names TSDP.

- **`multiplizitaet`** (minor, 1): „functional multiplicity“, a state of cooperation and co-consciousness (L60).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis der Existenz` (near `genesis`). `Genesis der Existenz` a document's title, read on genesis as the memo's cited source (L44).
- `goedel-gambit`: `Gödel` (near `godelgambit`). occurrence: `Gödel` names the theorems, not the Gambit.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz statt Wahrheit` (near `koharenz`), `Kohärenz durch Integration` (near `koharenz`). occurrence: the title and the two slogans of the table (L36), split by escapes
- `nichts-rauschen`: `Rauschen` (near `nichtsrauschen`). occurrence: `Das Rauschen` (L44) is the memo's summary of „Genesis der Existenz“, read on aegis.
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`). occurrence: the theory's name, read on tsdp.
- `risse`: `Risse im Fundament` (near `risse`). reading: `Risse im Fundament` (L104).


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: four Kernwelten, each mapped to alters — KW1 Lex, KW2 the EPs, KW3 Alex and Nyx, KW4 Lia, Rhys and Selene as the core Self (L23–L28).
- **`q7-what-734-names`**: the subjective Ich subsumed into pure function, „Komponente 734“, as the memo summarises „Genesis der Existenz“ (L51).
- **`c13-externe-ebene-beyond-the-simulation`**: the Externe Ebene with Juna and V, an external truth beyond AEGIS's control (L109, L111).

**Not promoted:** Environmental Storytelling, the two models of coherence as slogans, ontological autarky, the Bruchpunkt, inevitable surprise, the Isolation Objection, the 6 Paraiyas, The Gardener, The Fundament.

**One reader**: every page above and the three records.

**Chapter readings**: none — the document names no chapter.
