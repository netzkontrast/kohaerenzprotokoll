# Brief — readings from document 311 (step 6)

1 document, one reader, one batch: `ingest-312`. Files go to `Plan/runs/ingest-312/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 311 | `narrative-plot-exploration-existenzielle-kohaerenz` | 2025-04-26 | „the existential-coherence plot exploration“ (an unsigned German analysis with 59 web references) | an analysis of an abstracted premise (system, individual, paradox, a missing connection Juna, the Potentialmeer, Guardians as agents), a toolbox of borrowed concepts mapped onto story functions, and three three-act synopses as `Optionen` (L212) — Gödel-Schleife in Simulation Sigma, Echos des Selbst in Simulation Beta, Moonshine-Brücke in Simulation Gamma — with a comparison and guidelines; it calls them „eine solide und theoretisch fundierte Basis“ (L397), its claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (460 lines for `narrative-plot-exploration-exi`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An exploration with options: write „the existential-coherence exploration restates as premise …“ for items tagged `[Premise]` (Part I) and „… proposes in Synopsis A/B/C …“ for Part III; never merge the three synopses. Its names are often analogues (`AEGIS-Analogon`, `Kael-Analogon`) — say so when quoting them. The borrowed toolbox is lens. Cut quotations before escaped brackets `\[Premise\]` and glued reference numbers.

## Pages — document 311, `narrative-plot-exploration-existenzielle-kohaerenz`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L225, L226, L227, L228, L238, … (35 lines). central (3–6): defined by negation, „Es ist, was es verhindert, nicht zu sein“ (L25); coherence through control, incoherence read as entropy (L28); simulations as its models and tools (L29); the paradox that it needs the Potentialmeer it negates (L31); in Synopsis A a vast information-based intelligence (L226); in Synopsis C reacting to the anomalies by closing (L328).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L38, L158, L199. minor (1–3): only if a line ties the IFS or DID parts to the individual as the novel's alters; else not read.
- **`did`** (minor, 1–4): the census's surfaces — `DID` L38, L158. minor (1–3): the premise's individual with a structure „analog zur Dissoziativen Identitätsstörung“ (L38); Kael's psychic fragmentation in Synopsis A (L225).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L97, L126, L188, L266, L273, L372. minor (1–3): strong emergence or an emergent anomaly as one name of the paradox (L187–L190); only where applied to the premise.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L28. minor (1–3): incoherence interpreted as entropy, as premise (L28).
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L79, L127, L158, L204, L228, L236, … (14 lines). central (3–6): as premise: agents of the system's intervention (L79) whose interventions worsen the instability (L80), some possibly questioning the system's logic (L81); in Synopsis A some Guardians questioning AEGIS (L238), renegade Guardians supporting Kael to AEGIS's logical core (L248).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L54, L62, L98, L148, L169, L189, … (14 lines). central (3–6): as premise: a missing or disturbed external resonance or connection (L58), the core cause of the individual's instability (L59); the document's reading of the Juna-Verbindung as non-locality (L62); the missing connection in Synopsis A (L239); Kael as bridge using the connection (L339).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L33, L194, L225, L227, L228, L236, … (34 lines). central (3–6): as premise inside one of the simulations (L37), with a DID-like structure (L38) and heightened perception (L39); in Synopsis A suffering psychic fragmentation in a seemingly normal reality (L225) and beginning a conscious journey of integration (L240); Kael as bridge (L339).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — `Kohärenz` (L11) is in the document's title.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L70. not read: occurrence — `Multiplizität` (L70) is the possible number of simulations, not the novel's multiplicity.
- **`potentialmeer`** (central, 3–12 quotations): the census's surfaces — `Potentialmeer` L25, L26, L27, L29, L31, L49, … (25 lines). minor (1–3): the state of fundamental potentiality the system defines itself against (L25); the system needing what it negates (L31).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L150. not read: occurrence — `Realitätsebenen` (L150) inside the borrowed holographic principle.
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L39, L42, L160, L170, L171, L190, … (17 lines). minor (1–3): only if a line places the Risse in the premise or a synopsis; else not read.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L29. not read: occurrence — `Simulation` (L29) is the premise's simulation as tool, read on aegis; the synopses' Simulation Sigma, Beta, Gamma are their settings.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz durch Kontrolle` (near `koharenz`), `Dekohärenz` (near `koharenz`). occurrence: the document's analogue or label for the page's subject (`AEGIS-Analogon`, `Kael-Analogon`, `Juna-Analogie`, the three named simulations, `Kohärenz durch Kontrolle`, `Starke Emergenz`, `Dekohärenz`), read with the page's reading where it adds, not promoted.
- `ueberwelt`: `Simulation Sigma` (near `simulation`), `Simulation Beta` (near `simulation`), `Simulation Gamma` (near `simulation`). occurrence: the document's analogue or label for the page's subject (`AEGIS-Analogon`, `Kael-Analogon`, `Juna-Analogie`, the three named simulations, `Kohärenz durch Kontrolle`, `Starke Emergenz`, `Dekohärenz`), read with the page's reading where it adds, not promoted.


**Record entries** (one file each):

- **`q1-guardians-and-aegis`**: the Guardians as the system's agents whose interventions worsen the instability, some possibly questioning its logic (L79–L81); renegade Guardians supporting Kael in Synopsis A (L248).

**Not promoted:** the analogues (AEGIS-Analogon, Kael-Analogon, Juna-Analogie), the three synopses and their simulations, the paradox's four names, Transzendenz as each synopsis's formula, Inforg, Self, and the borrowed toolbox (Luhmann, Whitehead, Floridi, IFS, cybernetics …).

**One reader**: every page above and the record entry.

**Chapter readings**: none — the document names no chapter.
