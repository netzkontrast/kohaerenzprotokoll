# Brief — readings from document 95 (step 6)

1 document, one reader, one batch: `ingest-95`. Files go to `Plan/runs/ingest-95/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 95 | `strukturelle-dissoziation-system-kael-analyse` | 2025-04-28 | „the TSDP analysis“ (titled `Detaillierte Analyse der Spannungspunkte und Ausarbeitung der Charakterprofile für System Kael basierend auf der Theorie der Strukturellen Dissoziation`) | a German research report of 2025-04-28, the most complete of four TSDP analyses of that day: Teil 1 maps tension points between the Anteile (L21–L56, with Tabelle 1 of five conflict pairs), against the four Kernwelten Co₁, McL, B, Ly (L58–L96), AEGIS (L98–L118), Juna/V (L120–L138) and Integration/Selene (L140–L171); Teil 2 sums up TSDP and trauma research (L173–L221); Teil 3 profiles all eleven Anteile on one template, each with an earlier name (`ehem.`, L246–L518, Tabelle 2 at L231); Teil 4 gives plot, character and world recommendations (L520–L562); 35 web references, among them blogs, WebMD and Reddit beside research; it calls itself „eine umfassende psychologische Grundlage“ (L568), claims no canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (607 lines for `strukturelle-dissoziation-syst`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A research report that applies a theory: write „the TSDP analysis classifies …“, „proposes …“; its statements about the system are hedged (`wahrscheinlich`, `könnte`, `möglicherweise`) — keep the hedge. It predates the canon's worlds: its Kernwelten are `Co₁`, `McL`, `B`, `Ly`, symbolic (Ordnung, Netzwerk/Wissen, Chaos/Trauma, Potentialität) — record them as the document's names, never map them onto KW1–KW4. AEGIS is here an outside manipulator that exploits the split (L100); later documents differ — record, do not reconcile. Selene is modelled on the IFS „Selbst“ (L274): say so where read. The footnote digits glued to sentence ends (`…entwickelt wurde.1`) are reference marks: quote around them. `--find` does not match the subscript in `Co₁`: quote around it. **Each profile names an earlier name with `ehem.`** (Kael ehem. Michael L246, Selene ehem. Die Wächterin L272, Nyx ehem. Shadow L295, Kiko ehem. Der Kleine L321, Lia ehem. Isabella – jüngere Form L347, Isabelle ehem. Isabella – ältere Form / Sexual Alter L372, Moros ehem. The Lost One L397, Alex ehem. Alexander L422, Rhys ehem. Stefan L447, Lex ehem. Data L473, Argus ehem. Beobachter/Kritiker L499): each alter's reading records its earlier name. The document names no chapter.

## Pages — document 95, `strukturelle-dissoziation-system-kael-analyse`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L98, L100, L102, L104, L106, … (35 lines). central (3–5): section 1.3 — AEGIS's control, manipulation and gaslighting as an outside threat that exploits the dissociative structure (L100–L102), its lever per Anteil (L106–L116), and its role in the overall dynamic (L530).
- **`alex`** (central, 3–12 quotations): the census's surfaces — `Alex` L15, L25, L36, L45, L56, L85, … (30 lines). central (3–4): its profile in Teil 3 — the earlier name (`ehem.`), TSDP type, action systems, core phobias — and one conflict pair or AEGIS lever it carries.
- **`argus`** (central, 3–12 quotations): the census's surfaces — `Argus` L15, L75, L116, L136, L168, L196, … (12 lines). central (2–3): profile 3.11 — Argus ehem. Beobachter/Kritiker (L499), „Entstehender ANP/EP-Mix oder Metakognitiver Anteil“ (L501).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L15, L196, L573, L575, L580, L594, … (9 lines). minor (1–2): tertiary dissociation as typical for DID (L15, L196).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L89. minor (1) only if L89 says something of Emergenz as the wiki's term (Ly as „Potentialität/Emergenz“); else occurrence, say why.
- **`isabelle`** (central, 3–12 quotations): the census's surfaces — `Isabelle` L15, L25, L30, L44, L84, L94, … (19 lines). central (3–4): its profile in Teil 3 — the earlier name (`ehem.`), TSDP type, action systems, core phobias — and one conflict pair or AEGIS lever it carries.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L15. minor (2): section 1.4 — the link to Juna/V as a counterpole to AEGIS that activates disorganised attachment (L122); Selene's view of Juna/V as co-regulation (L135).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L11, L15, L19, L25, L29, L31, … (59 lines); `Michael` L246. central (3–5): profile 3.1 — Kael ehem. Michael (L246) as primary ANP, host (L248), his phobia of the EPs and amnesia (L250); the system as tertiary structural dissociation from chronic, probably early-childhood interpersonal trauma (L526).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L15, L58, L60, L96, L530, L540, … (9 lines). minor (2): section 1.2 — the four Kernwelten as `Co₁`, `McL`, `B`, `Ly` (L60–L89), symbolic inner landscapes; record the names and what each stands for, as the document's own.
- **`kiko`** (central, 3–12 quotations): the census's surfaces — `Kiko` L15, L25, L32, L43, L55, L67, … (44 lines). central (3–4): its profile in Teil 3 — the earlier name (`ehem.`), TSDP type, action systems, core phobias — and one conflict pair or AEGIS lever it carries.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: the novel's title — occurrence (J9).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L15, L25, L29, L33, L36, L40, … (43 lines). central (3–4): profile 3.10 — Lex ehem. Data (L473), typed „Primärer ANP“ like Kael (L475): record both primaries, decide nothing; the conflict pairs Lex vs. Nyx and Kiko vs. Lex (L40, L43).
- **`lia`** (central, 3–12 quotations): the census's surfaces — `Lia` L15, L25, L32, L44, L67, L84, … (32 lines). central (3–4): its profile in Teil 3 — the earlier name (`ehem.`), TSDP type, action systems, core phobias — and one conflict pair or AEGIS lever it carries.
- **`moros`** (central, 3–12 quotations): the census's surfaces — `Moros` L15, L25, L31, L41, L53, L76, … (36 lines). central (3–4): its profile in Teil 3 — the earlier name (`ehem.`), TSDP type, action systems, core phobias — and one conflict pair or AEGIS lever it carries.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L142, L211. minor (2): integration is not fusion but „funktionale Multiplizität“ (L142, L211).
- **`nyx`** (central, 3–12 quotations): the census's surfaces — `Nyx` L15, L25, L30, L32, L40, L45, … (43 lines). central (3–4): its profile in Teil 3 — the earlier name (`ehem.`), TSDP type, action systems, core phobias — and one conflict pair or AEGIS lever it carries.
- **`rhys`** (central, 3–12 quotations): the census's surfaces — `Rhys` L15, L25, L31, L32, L36, L41, … (38 lines). central (3–4): its profile in Teil 3 — the earlier name (`ehem.`), TSDP type, action systems, core phobias — and one conflict pair or AEGIS lever it carries.
- **`selene`** (central, 3–12 quotations): the census's surfaces — `Selene` L15, L42, L54, L93, L115, L135, … (38 lines). central (3–4): profile 3.2 — Selene ehem. Die Wächterin (L272), typed as „Modifizierter ANP mit EP-Komponenten oder Repräsentation des Integrationspotenzials“ and likened to the IFS „Selbst“ (L274).
- **`tsdp`** (central, 3–12 quotations): the census's surfaces — `TSDP` L15, L17, L19, L51, L142, L144, … (26 lines). central (4–6): Teil 2 — ANP and EP, the spectrum primary/secondary/tertiary (L194–L196: System Kael as tertiary with four ANPs and five-plus EPs), action systems, the defence cascade (L202), the six phobias (L29–L34), the three-phase treatment (L215–L217).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie-resonanz`: `Resonanz` (near `entropieresonanz`), `Resonanz` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz` (near `entropieresonanzprotokolle`). occurrence: `Resonanz` is the ordinary word (J53).
- `juna`: `Juna/V` (near `juna`), `Beziehung zu Juna/V` (near `juna`). readings, above: `Juna/V` is the slash form of the name (J34); `Beziehung zu Juna/V` a heading (J9).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title (J9).
- `personas`: `Depersonalisation` (near `persona`). occurrence: `Depersonalisation` is the clinical term, not the page (J69).
- `resonanz-landschaft`: `Resonanz` (near `resonanzlandschaft`). occurrence: `Resonanz` alone is not the world (J53).


**Record entries** (one file each; write one only where the analysis speaks to the record's question):

- **`q3-how-many-kern-welten-and-alters`**: eleven Anteile (L15), four ANPs and five-plus EPs with Selene and Argus as mixed forms (L196), Tabelle 2 (L231–L242); four Kernwelten named Co₁, McL, B, Ly (L60).
- **`c16-kael-origin`**: the system's origin in „chronisches, wahrscheinlich frühkindliches interpersonelles Trauma“ (L526), with AEGIS an outside force that exploits the split (L100).

**Split into two readers, one after the other:**
- Reader 1: aegis, kael, juna, kern-welten, tsdp, multiplizitaet, did, emergenz, selene, argus, and the two records.
- Reader 2: lex, alex, isabelle, kiko, lia, moros, nyx, rhys.
