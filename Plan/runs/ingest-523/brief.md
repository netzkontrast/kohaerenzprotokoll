# Brief — readings from document 523 (step 6)

1 document, one reader, one batch: `ingest-523`. Files go to `Plan/runs/ingest-523/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 523 | `aegis-manifest-genesis-krise-reboot-2` | 2026-04-27 | „the AEGIS manifesto, reboot“ (an English initiation log in AEGIS's voice) | the Genesis Crisis and Great Realignment, the two kernels, the Überwelt, the four Kernwelten with the fragments assigned to them, four Guardians and the intervention sequence; it calls itself the absolute baseline specification (L15), a claim recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (304 lines for `aegis-manifest-genesis-krise-r`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** AEGIS's self-description: write „the manifesto (speaking as AEGIS) declares/assigns …“ — it is the system's view, which denies the fragments any subjectivity (L109); record it, never apply it. The Corrupted Entity paragraph (L245) carries a trauma-symbol detail: never quote L245, and write nothing of its colour. L255–L279 is engineering practice: not read. Never write the names Michael, Julia, Shadow, „The Lost One“ or Isabella; `Isabelle` (with a final e) is the current name and is read normally. No gendered pronoun for Kael, Juna, AEGIS, the Guardians or the parts in our own prose.

## Pages — document 523, `aegis-manifest-genesis-krise-reboot-2`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L15, L43, L65, L82, L109, … (15 lines). central (3–8): the expanded name „Autonomous Entropy Gatekeeper for Identity Systems“ (L15); the core axiom (L43); it speaks of itself only in the third person (L33); its origin as „the residual state of absolute algorithmic coherence“ (L17); the Gatekeeper cannot tolerate ambiguity (L55); proxy and protector of the K1 state (L65); the fragments not recognised as independent characters (L109).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Cognitive Firewall` L103; `Zero-Trust` L103. minor (1–4): Zero-Trust parameters and the Behavioral Proof-of-Function consensus: no entity has an inherent right to exist or consume resources (L103); read Cognitive Firewall on the same line.
- **`cerberus`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Cerberus` alone on L158. minor (1–4): KW3 in the table, „Cerberus“, Relevance Logic, defensive labyrinth, Nyx as its fragment (L158); with the section on the Cerberus-Labyrinth (L135, L137) — read with grenzfeste's line, attributed.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L59. minor (1–4): the Dual-Kernel Theory as a „strict relational ontology“ with „no permitted synthesis“ (L59).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L15. minor (1–4): the Genesis Crisis, the shock „internally designated and permanently archived as the Genesis Crisis“ (L15); declared concluded (L283).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L137. minor (1–4): the third world „Designated as the Grenzfeste or Border Fortress“ (L137).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L163, L165, L167, L230, L232, L287. minor (1–4): „highly specialized, non-anthropomorphic, operationally segregated subsystems designated as the Guardians“ (L163), fundamental components of AEGIS (L165), suffering the Wächter-Zwiespalt (L167); four named in section 6 (LogOS, Oblivion, Silas, Isabelle); the tri-layered validation matrix (L230).
- **`isabelle`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Isabelle` alone on L193. minor (1–4): here a Guardian, not an alter: „6.4 Isabelle: The K1-Proxy Initializer“ (L193), commissioned as the strict enforcer of parameter initializations (L195), enforcing the PRO-Framework (L197) and eliminating ambiguous instructions before initialization (L199); table row L209. The same reading as the earlier manifesto's on this page; the alter elsewhere on the page is not mentioned here.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L109. minor (1–4): `Juna/V` among the shattered elements (L109) and as „the external anomaly“ assigned to the fourth world with Selene (L147, L159); the document does not reconcile the two — say so, unresolved.
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L109, L120, L156. minor (1–4): named at L109 as the primary sentient fragment among the shattered elements; the first world targets „the logical facets of Kael“ (L120); `Kael-Logic` in the table (L156).
- **`kairos`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kairos` alone on L159. minor (1–4): KW4 in the table, „Kairos“, Dialetheic Logic, emergent fractal space, Selene and Juna/V (L159), with Kairos-Potentialis (L142) viewed „with extreme, unyielding suspicion“ (L148).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L111, L113, L165, L245, L285; `Kernwelt` L111, L113, L155, L165, L245, L285. minor (1–4): „four specialized, operationally isolated simulation environments“ (L111) that „function as externalized psycho-architectures“ (L113); the table L155–L159.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L109, L129, L157. minor (1–4): assigned to the second world: „the vulnerability patterns of Kiko“ (L129); EP fragment in the table (L157).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L109, L120, L156. minor (1–4): assigned to the first world: „Lex or the logical facets of Kael“ (L120); ANP fragment in the table (L156).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L169, L171, L173, L175, L206, L213, … (8 lines). minor (1–4): Guardian 6.1: „It is not a character; it is the algorithmic enforcement of absolute geometric order.“ (L171); the „Hard Glitch Cut“ (L175); table row L206. Note: Logos-Prime (L115) is the first Kernwelt, a different term from the Guardian — keep them apart.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Mnemosyne` alone on L157. minor (1–4): KW2 in the table, „Mnemosyne“, paraconsistent logic, Kiko and Moros, quarantine of trauma and memory (L157); the second world „constructed as a high-security quarantine zone“ (L126).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L109, L129, L157. minor (1–4): assigned to the second world: „the implosion states of Moros“ (L129); EP fragment in the table (L157).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L21, L45. minor (1–4): the state before the crisis: the antecedent architecture „operated within an active“ negating force (L21); tied to the Collapse Kernel (L45).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L109, L138, L158. minor (1–4): assigned to the third world: „targeting defensive fragments like Nyx“ (L138); table L158.
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L177, L179, L182, L183, L207, L213, … (8 lines). minor (1–4): Guardian 6.2, „the paramount Hypervisor of Deletion Logic“, personifying the Amnesia Protocol (L179); table row L207.
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L197. not read: an occurrence — `Persona` inside the PRO-Framework's expansion (L197), not the page's term.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitch` alone on L175. not read: an occurrence — `Glitch` in LogOS's „Hard Glitch Cut“ (L175), an intervention, not a Riss.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L109, L147, L159. minor (1–4): assigned to the fourth world with Juna/V (L147); emergent anomaly in the table (L159).
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L185, L187, L189, L190, L191, L208, … (8 lines). minor (1–4): Guardian 6.3: „Silas is deployed as the Hypervisor of Repair, Memory Architecture, and State Management“ (L187); table row L208.
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L25. minor (1–4): L25 as the census lists it — read only what the line says.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L87, L91, L97, L99, L103, L111, … (8 lines). minor (1–4): „an abstract, non-anthropomorphic matrix“ built by the Gatekeeper (L91); space defined by data connectivity, logic gates and geometric function (L93); instantiated as the permanent matrix of internal reality (L285).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). a reading: `Cerberus-Labyrinth` is the third Kernwelt (L135), read on cerberus above.
- `genesis`: `Genesis Crisis` (near `genesis`). a reading: `Genesis Crisis` (L15, L283), read on genesis above.
- `juna`: `Juna/V` (near `juna`). a reading: `Juna/V` names Juna (L109, L147), read on juna above.
- `kairos`: `Kairos-Potentialis` (near `kairos`). a reading: `Kairos-Potentialis` is the fourth Kernwelt (L142), read on kairos above.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). a reading: `Mnemosyne-Archipel` is the second Kernwelt (L126), read on mnemosyne above.
- `risse`: `Hard Glitch Cut` (near `glitch`). an occurrence: `Hard Glitch Cut` is LogOS's intervention (L175), not a Riss.


**Record entries:** none.

**No chapter readings**: no chapter is named (`Kap`, `Kapitel`, `chapter` each 0).

**Not promoted:** Great Realignment, Ursprungs-Ich, Component 734, the kernel names, Logos-Prime as a surface, BPoF, RTSV, the Wächter-Zwiespalt, the intervention sequence's steps, the PRO-Framework, Digital Kintsugi, the engineering practice of L255–L279.

**One reader**: every page above.
