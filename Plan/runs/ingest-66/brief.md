# Brief — readings from document 66 (step 6)

1 document, one reader, one batch: `ingest-66`. Files go to `Plan/runs/ingest-66/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 66 | `plotanalyse-kohaerenz-protokoll-szenario` | 2025-04-23 | „the Plotanalyse“ | a German review report of 2025-04-23 that assesses a plot idea — the AEGIS/Monster(Kael/Juna) scenario — taken from a commissioning text it cites as `User Query` with a section number; a concept-to-plot matrix (L37–L61), a section per element (L63–L130), strengths and weaknesses, comparisons with literature and film, a verdict and a recommendation, 99 references |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (356 lines for `plotanalyse-kohaerenz-protokol`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** **Two voices on one line.** What the scenario *is* comes from the commissioning text, marked by a trailing `[User Query …]` bracket: write „the scenario, as the Plotanalyse cites its User Query, …“. What a concept *means for it* (autopoiesis, Gödel, IFS, NET, the Monster group's properties) is the report's own reading: write „the Plotanalyse reads …“. The scenario differs from much of the wiki: AEGIS analyses an entity M through four simulated Kernwelten, Kael is M's human avatar, and his DID is the result of AEGIS's fragmentation (L74, L92, L119). Say exactly that, attributed, and never reconcile it with another page's origin story — the reconciler records the difference. Footnote digits glued to words: quote around them. The report's question marks (L113–L115) are open questions it asks, not positions.

## Pages — document 66, `plotanalyse-kohaerenz-protokoll-szenario`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L17, L41, L42, L43, L44, … (70 lines). central (4–7): AEGIS as „das zentrale Protagonistensystem der Erzählung“ (L67); its principle, cited from the User Query (L69); the decision to analyse M through four simulated Kernwelten, read as structural coupling (L70); paraconsistent logic and Gödel's limits as its analytic limits (L71, L72); fragmenting a sentient entity, Kael as manifestation of M, read as an alignment problem (L74); methodological reductionism against M's holism (L125). Differ line: in this scenario AEGIS fragments an external entity's avatar to analyse it.
- **`alex`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alex` alone on L196. not read: sweep occurrence (Alex Garland, L196).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L46, L87, L92, L130. minor (1–2): the Monster group's pariahs as metaphor for integrating all of Kael's aspects, his `Alters` in inner straight marks — quote around them (L87); and L130 if it names them.
- **`did`** (minor, 1–4): the census's surfaces — `DID` L46, L92, L130, L142, L148, L175, … (7 lines). minor-to-central (2–3): Kael's DID as explicitly not natural but the result of AEGIS's attempt to decompose M's complexity onto a human psyche (L92, cited from the User Query); the matrix row (L46).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L55, L115, L125. minor (1): emergence as a possible property of the Potentialmeer and the explanation of M's holistic nature (L55, L115). No C3 entry — the report does not say where AEGIS emerges from.
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L52, L69, L109, L114, L115. minor (1–2): the Potentialmeer's high entropy against AEGIS's striving for order (L52, L115), information-theoretic. No C2 entry unless the digest's senses lack this one.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L11, L17, L41, L44, L73, L97, … (12 lines). central (2–4): the Kael-Juna link as a central mystery and possible key to the resolution (L99); its function as catalyst or anchor of Kael's integration (L103). Juna's own nature is not given; say so if the lines do not.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L11, L17, L40, L41, L44, L46, … (45 lines). central (4–7): „Die Entität M und ihre menschliche Manifestation Kael“ as AEGIS's counter-pole (L78); the Monster group's properties as metaphors for M/Kael — irreducible, unique (L85, L86); Kael's DID induced by AEGIS (L92); IFS and NET as models of his inner world and healing (L93, L94); his identity as the Ship of Theseus (L130). Differ line: in this scenario Kael is the human avatar of an external entity M, fragmented by AEGIS.
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L46, L47, L48, L61, L70, L92, … (19 lines). central (2–4): AEGIS analyses M „über vier simulierte Kernwelten“ (L70, User Query); „Die vier Kernwelten sind von AEGIS geschaffene, kontrollierte Simulationen, die als Labore zur Analyse von M/Kael dienen“ (L119); the matrix: Kernwelten as representation of the fragments (L46) and as isolated parts (L47); KW3 as fear and safety (L49). Differ line: worlds as AEGIS's labs for analysing M.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. minor (1–3): M's coherence by integration against AEGIS's by demarcation — `Kohärenz durch Integration` (L40, L84) and `Kohärenz durch Abgrenzung` (count it); true coherence includes the shadow (L95).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Moonshine-Link` alone on L97. central (2–4): the heading „Kael-Juna-Verbindung (Der Moonshine-Link)“ (L97); Monstrous Moonshine as metaphor of a deep, non-local link AEGIS cannot explain (L41, L101); entanglement as metaphor of an instantaneous, cross-simulation link (L44, L102); the link as catalyst of integration (L103).
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L51, L52, L55, L58, L69, L105, … (19 lines). central (3–5): „ein Meta-Raum reiner Potentialität, prä-realer Möglichkeit, hoher Entropie“ (L109, cited from the User Query); the report's three open ontologies — Aristotelian potentiality, an informational field, a quantum vacuum (L113–L115), as questions; the matrix rows (L51, L52, L58).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L61. not read: sweep occurrence (L61).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L159. minor (1): AEGIS's system destabilised by its analysis of M, the „Risse“ of the User Query (L159).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L61. not read: sweep occurrence (L61).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz durch Abgrenzung` (near `koharenz`), `Kohärenz durch Integration` (near `koharenz`). reading, above.
- `personas`: `transpersonalen Psychologie` (near `persona`). occurrence: transpersonal psychology, borrowed (L57).
- `risse`: `Rissen` (near `risse`). reading, above; `Rissen` L71 is the report's word for flaws in AEGIS's logic — check the line and include it only if it is AEGIS's rifts.
- `ueberwelt`: `Simulationshypothese` (near `simulation`). occurrence: the simulation hypothesis (L61).


**Record entries** (one file each in `Plan/runs/ingest-66/readings/`):

- **`q9-moonshine-link-boundary`**: what crosses and between whom — the link non-local and cross-simulation (L44, L102), possibly supplying resonance, compassion or information Kael needs (L103). One entry, the report's terms.
- **`q3-how-many-kern-welten-and-alters`**: four simulated Kernwelten (L70, L119), Kael's parts unnumbered (L87, L93). One short entry.

The new difference — Kael as the avatar of an external entity M against Kael as AEGIS's own fragments — is the reconciler's to record (a new conflict record); write no record for it, but say it in each differ line on kael and aegis.
