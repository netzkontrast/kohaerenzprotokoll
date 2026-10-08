# Brief — readings from document 218 (step 6)

1 document, one reader, one batch: `ingest-218`. Files go to `Plan/runs/ingest-218/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 218 | `kael-system-tsdp-analyse-und-profile` | 2025-04-28 | „the TSDP profile report“ (an unsigned report) | a German report that reads the eleven parts of System Kael through the TSDP — their tensions with each other, with the Kernwelten, AEGIS and Juna/V — gives eleven template profiles (section 3) and recommendations; it hedges most readings (`wahrscheinlich`, `könnte`) and names a user query and an unreproduced research context as its sources; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (459 lines for `kael-system-tsdp-analyse-und-p`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A hedged report: write „the TSDP profile report reads / suggests …“ and keep `wahrscheinlich`, `könnte`, `möglicherweise` — its readings are proposals; each part's profile is in section 3 (Kael from L188, the others follow in the order of L15), with fields `TSDP-Rolle & Funktion`, `Trigger & Phobien`, `Beziehung zu AEGIS & Juna/V`, `Bedürfnisse & Integrationshindernisse` — quote the content, not the field labels. German — cut before glued footnote digits (`definiert.4`) and inner quotes; tables carry escaped bold.

## Pages — document 218, `kael-system-tsdp-analyse-und-profile`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L66, L102, L104, L106, L107, … (33 lines). central (3–5): AEGIS as a systemic antagonist built to exploit TSDP weaknesses — control, manipulation, gaslighting, surveillance (L104); attacking ANP weaknesses (L106); triggering EPs (L107); gaslighting (L108); actions that might trigger AEGIS's Paradoxon X (L109) — cut before the inner quotes.
- **`alex`** (central, 3–12 quotations): the census's surfaces — `Alex` L15, L37, L56, L67, L89, L99, … (29 lines). central (2–5): the profile of Alex in section 3 — its TSDP role, triggers and phobias, and its relation to AEGIS and Juna/V; its tension lines in section 1 (L66–L121); keep the hedges.
- **`argus`** (central, 3–12 quotations): the census's surfaces — `Argus` L15, L38, L69, L89, L98, L99, … (20 lines). central (2–5): the profile of Argus in section 3 — its TSDP role, triggers and phobias, and its relation to AEGIS and Juna/V; its tension lines in section 1 (L66–L121); keep the hedges.
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L129, L389. minor (1–2): the Cache Kohärenz problem — the lack of shared memory and co-consciousness making integration hard (L129) — cut before the inner quotes; plot points from it (L389).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L452. occurrence: `DID` at L452 is a reference title.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L95. occurrence: `Emergenz` at L95 is the label of the world Ly (Potentialität/Emergenz) — read on kern-welten.
- **`isabelle`** (central, 3–12 quotations): the census's surfaces — `Isabelle` L15, L34, L47, L57, L74, L79, … (28 lines). central (2–5): the profile of Isabelle in section 3 — its TSDP role, triggers and phobias, and its relation to AEGIS and Juna/V; its tension lines in section 1 (L66–L121); keep the hedges.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L15. minor (1–3): the connection to Juna/V as „externes Bindungsobjekt“ that activates the attachment system within Kael (L113); Rhys, Kiko and Lia drawn to it (L115); Juna/V as a turning point and possible external resource for healing (L385).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L11, L15, L19, L23, L34, L36, … (57 lines). central (3–6): System Kael's eleven identified parts (L15); Kael as the primary ANP and host (the profile from L188, L192); Kael as AEGIS's primary target for manipulation (L197); the Cache Kohärenz conflicts around Kael's decisions (L389).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L15, L93, L95, L141, L375, L384, … (8 lines). minor (1–3): the fictional Kernwelten — Co₁ Ordnung, McL Netzwerk/Wissen, B Chaos/Trauma, Ly Potentialität/Emergenz — as externalised representations of inner conflicts that trigger specific dynamics (L95) — quote around the subscript; B as the most direct trigger world (L99); the Kernwelten as catalysts (L384).
- **`kiko`** (central, 3–12 quotations): the census's surfaces — `Kiko` L15, L34, L35, L37, L47, L56, … (45 lines). central (2–5): the profile of Kiko in section 3 — its TSDP role, triggers and phobias, and its relation to AEGIS and Juna/V; its tension lines in section 1 (L66–L121); keep the hedges.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the Protokoll's name in the title (L11).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L15, L35, L36, L47, L56, L57, … (51 lines). central (2–5): the profile of Lex in section 3 — its TSDP role, triggers and phobias, and its relation to AEGIS and Juna/V; its tension lines in section 1 (L66–L121); keep the hedges.
- **`lia`** (central, 3–12 quotations): the census's surfaces — `Lia` L15, L34, L37, L47, L56, L57, … (43 lines). central (2–5): the profile of Lia in section 3 — its TSDP role, triggers and phobias, and its relation to AEGIS and Juna/V; its tension lines in section 1 (L66–L121); keep the hedges.
- **`moros`** (central, 3–12 quotations): the census's surfaces — `Moros` L15, L34, L36, L37, L47, L56, … (37 lines). central (2–5): the profile of Moros in section 3 — its TSDP role, triggers and phobias, and its relation to AEGIS and Juna/V; its tension lines in section 1 (L66–L121); keep the hedges.
- **`nyx`** (central, 3–12 quotations): the census's surfaces — `Nyx` L15, L34, L35, L47, L56, L57, … (56 lines). central (2–5): the profile of Nyx in section 3 — its TSDP role, triggers and phobias, and its relation to AEGIS and Juna/V; its tension lines in section 1 (L66–L121); keep the hedges.
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L90. occurrence: `Persona` at L90 is Isabelle's persona of control, not the Personas.
- **`rhys`** (central, 3–12 quotations): the census's surfaces — `Rhys` L15, L36, L56, L66, L89, L97, … (42 lines). central (2–5): the profile of Rhys in section 3 — its TSDP role, triggers and phobias, and its relation to AEGIS and Juna/V; its tension lines in section 1 (L66–L121); keep the hedges.
- **`selene`** (central, 3–12 quotations): the census's surfaces — `Selene` L15, L84, L85, L90, L91, L99, … (39 lines). central (2–5): the profile of Selene in section 3 — its TSDP role, triggers and phobias, and its relation to AEGIS and Juna/V; its tension lines in section 1 (L66–L121); keep the hedges.
- **`tsdp`** (central, 3–12 quotations): the census's surfaces — `TSDP` L17, L19, L21, L23, L27, L30, … (38 lines). central (2–4): the TSDP of Van der Hart, Nijenhuis and Steele as the report's theoretical basis (L17) — cut before the glued digit; Lex as a primary ANP (L336); read L19.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna (J34).


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: eleven identified parts (L15); four Kernwelten with their own labels — B as Chaos/Trauma (L95), where other documents make B defence — and parts resonating with each world (L97–L100), proposed, not assigned.
- **`c16-kael-origin`**: Juna/V as an external attachment object (L113) — external, not a part.

**Not promoted:** the template fields, the PP- codes, the borrowed theories (Bowlby, Ainsworth, Luhmann, IFS), Paradoxon X, the recommendations.

**Two readers**, disjoint: (1) kael, selene, nyx, kiko, lia, isabelle and the record q3; (2) moros, alex, rhys, lex, argus, aegis, juna, tsdp, kern-welten, cache-kohaerenz and the record c16.

No chapter readings.
