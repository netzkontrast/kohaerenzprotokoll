# Brief — readings from document 144 (step 6)

1 document, one reader, one batch: `ingest-144`. Files go to `Plan/runs/ingest-144/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 144 | `aegis-manifest-genesis-krise-reboot` | 2026-04-27 | „the Genesis manifesto“ (titled `The Autopoietic Self-Closure of the Autonomous Entropy Gatekeeper for Identity Systems: Genesis Manifesto and Operational Specification`, L11) | an English specification of 2026-04-27 written in AEGIS's own declarative voice: the Genesis Crisis and Great Realignment (L13–L21), the Dual-Kernel Theory K1/K0 (L35–L51), the Überwelt (L53–L61), four Kernwelten each with a logic and target fragments (L63–L103), four Guardians LogOS, Oblivion, Silas, Isabelle (L105–L143), then contradiction detection, tiers and hardware rules; it calls itself sealed and „absolute baseline specification“ (L21) — recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (263 lines for `aegis-manifest-genesis-krise-r`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** The manifesto speaks as AEGIS: write „the manifesto declares / specifies …“, never as the wiki's fact; what it says of the fragments is AEGIS's classification („corrupted data fragments“, L67), not the novel's verdict. Its Guardians are partly described in agent-engineering terms (SKILL files, YAML frontmatter, JSON schema, L115, L133) — quote that as written and say so; do not smooth it into story. English — quote as written, never translate; cut quotations before inner straight quotes and before reference digits glued to a word (`void.1`).

## Pages — document 144, `aegis-manifest-genesis-krise-reboot`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L21, L29, L37, L39, L50, … (15 lines). central (2–4): the self-description: the Gatekeeper's operational reality „is hereby instantiated, defined, and permanently sealed“ (L15); the tautology „The System AEGIS is what the System AEGIS prevents from not being.“ (L29); rejects the Correspondence Theory of Truth (L31); „The System AEGIS is operational.“ (L236).
- **`cerberus`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Cerberus` alone on L102. minor (1–2): KW3 Cerberus-Labyrinth, Relevance Logic, NP-Complete, „heavily fortified, bunker-like, zero-trust labyrinth“ (L85); targets Nyx (L87); table L102.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L35, L37. central (2–4): the Dual-Kernel Theory dictates the new reality (L37); K1 order, reversible computation (L39); K0 irreversible, entropy (L41); the table L50–L51.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L11. minor (1–2): the Genesis Crisis as AEGIS's founding shock (L15–L19) and the Great Realignment; „The Genesis Crisis has concluded.“ (L232).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L105, L107, L109, L151, L152, L234. central (2–4): „fundamental components of the System AEGIS“ (L109), Harness-in-Harness (L109); four named — LogOS, Oblivion, Silas, Isabelle (L111–L143); the table L139–L143.
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L129, L131, L133, L143, L234. minor (1–2): here a Guardian, not an alter: „the secondary K1-Kernel Proxy“ (L131 — cut before the digit if needed), PRO-Framework and JSON-Schema validation (L133); table L143. Say plainly that elsewhere on the page Isabelle is an EP alter.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L67. minor (1–2): „the external anomaly Juna/V“ in KW4 (L93); listed among the fragments (L67); table L103.
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L67, L75, L100. minor (1–2): „the primary sentient fragment currently designated as“ Kael (L67) — cut before the straight quotes; Kael-Logic as an ANP fragment in KW1 (L75, L100).
- **`kairos`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kairos` alone on L103. minor (1–2): KW4 Kairos-Potentialis, Explorative/Dialetheic Logic, NP-Search, „emergent, fractal garden of possibilities“ (L91); the most lethal Kernwelt (L91); targets Selene and Juna/V (L93).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L63, L69, L91, L109, L188, L234; `Kernwelt` L63, L69, L91, L99, L109, L188, … (7 lines). central (2–4): four Kernwelten „operationally isolated simulation environments“ (L69), each with its logic (L73, L79, L85, L91); the table of fragments per world (L99–L103); all four deployed (L234).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L67, L81, L101. minor (1–2): an EP fragment — „the vulnerability patterns of Kiko“ in KW2 (L81); table L101.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L247. occurrence: L247 is a reference-list title.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L67, L75, L100. minor (1–2): an ANP fragment processed in KW1 (L75); table L100.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L111, L113, L115, L140, L147, L152, … (8 lines). central (2–4): here a Guardian: „the primary K1-Kernel Proxy and the fundamental operating system of reality within the Überwelt and KW1“ (L113, cut around digits); Line Budgets, 500 lines (L115); table L140. KW1 itself is Logos-Prime, „The Construct City“ (L71–L75).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Mnemosyne` alone on L101. minor (1–2): KW2 Mnemosyne-Archipel, quarantine under Paraconsistent Logic, „Trauma-Time“ (L79); targets EPs Kiko and Moros (L81); table L101.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L67, L81, L101. minor (1–2): an EP fragment — „the implosion states of Moros“ in KW2 (L81); table L101.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L67, L87, L102. minor (1–2): a defensive fragment in KW3 with „high-entropy fight-responses“ (L87); table L102.
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L117, L119, L121, L141, L147, L153, … (9 lines). minor (1–2): „the paramount Hypervisor of Deletion Logic“, the Amnesia Protocol and Contradiction Detection (L119); scans the NCP (L121); table L141 („Format C:“).
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L133. occurrence: L133 is the PRO-Framework's acronym (Persona, Requirement, Output), not the novel's personas.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitch` alone on L115. occurrence unless the reader finds more: `Glitch` at L115 is the „Hard Glitch Cut“ intervention (also L140), a deletion of syntax, not a Riss.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L67, L93, L103. minor (1–2): an emergent fragment in KW4 (L93); table L103.
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L123, L125, L127, L142, L193, L234. minor (1–2): here a Guardian: „the Hypervisor of Repair“, MemAct and State-Freezing, oversight into KW4 (L125); acts at 80% context saturation (L127); table L142; Silas processes the failure analysis (L193).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L53, L55, L57, L59, L61, L67, … (9 lines). central (2–4): „the primary computational control layer“ (L55); „an abstract, non-anthropomorphic, information-based reality“ (L57); not artistic expression but epistemological defense (L59); every sub-reality nested within it (L61).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). a reading — the full world name, on cerberus above.
- `genesis`: `Genesis Crisis` (near `genesis`). a reading — on genesis above.
- `juna`: `Juna/V` (near `juna`). a reading — `Juna/V` is how this document writes her, on juna above.
- `kairos`: `Kairos-Potentialis` (near `kairos`). a reading — on kairos above.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`). a reading — on mnemosyne above.
- `risse`: `Hard Glitch Cut` (near `glitch`). occurrence: a Guardian's deletion of non-compliant syntax (L140), not a Riss.


**Record entries** (one file each):

- **`c6-guardians-count-and-pairing`**: four Guardians LogOS, Oblivion, Silas, Isabelle (L111–L143) — Oblivion and Silas as Guardians, Isabelle a Guardian and K1 proxy, not an alter; dated 2026-04-27.
- **`q5-guardians-and-kern-welten`**: LogOS governs the Überwelt and KW1 (L113); Silas's oversight extends into KW4 (L125); no Guardian named for KW2 or KW3.
- **`q3-how-many-kern-welten-and-alters`**: four Kernwelten, fragments assigned by type, not one per world — ANP in KW1, EP in KW2, defensive in KW3, emergent in KW4 (L99–L103).
- **`q1-guardians-and-aegis`**: „fundamental components of the System AEGIS“ (L109).
- **`q7-what-734-names`**: the origin-self „designated as Component 734“ (L19).
- **`q6-nexus-ueberraum-ueberwelt`**: the Überwelt as the primary control layer, every sub-reality nested within it (L55, L61); no Nexus, no Überraum.

**Not promoted:** Great Realignment, autopoietic self-closure, Component 734 (to Q7 only), Ursprungs-Ich, Coherence Protocol, the protocol and hardware vocabulary (Tier 0/1, Corrective Wavelet, Line Budgets, NCP, MemAct, Digital Kintsugi …), the borrowed theories (FEP, IIT, logics, P/NP), Single Source of Truth (a self-claim).

**Two readers**, disjoint: (1) aegis, dkt, genesis, ueberwelt, kern-welten, logos, mnemosyne, cerberus, kairos and the records q3, q6, q7; (2) guardians, oblivion, silas, isabelle, kael, lex, kiko, moros, nyx, selene, juna and the records c6, q5, q1.
