# Brief — readings from document 509 (step 6)

1 document, one reader, one batch: `ingest-509`. Files go to `Plan/runs/ingest-509/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 509 | `genesis-krise-aegis-prosa-auftrag` | 2025-04-29 | „the Genesis-crisis prose commission“ (an unsigned German writing commission) | a strategic plan (Stufe 3) and a prose order (Stufe 4) for the scene in which AEGIS's Ursprungs-Ich meets an Entität in the Leere, through the Kohärenz Protokoll and the fragmentation to the emergence of Kael (L17); a plan, no canon claim beyond asking the writer to keep to „etablierte Lore“ (L160)|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (300 lines for `genesis-krise-aegis-prosa-auft`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan and commission: write „the Genesis-crisis commission plans …“; its suggestions are hedged (möglicherweise ×10). It cites clusters of research (Cluster 1–7) that are not in the file. Several theory rows and lines name real people (e.g. a philosopher in L109): never write a name, never quote a span containing one. „DID“ and „TSDP“ are the models it applies. No gendered pronoun for Kael or AEGIS in our own prose.

## Pages — document 509, `genesis-krise-aegis-prosa-auftrag`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L23, L25, L47, L48, L50, … (62 lines); `Kontrollinstanz` L213. central (4–8): AEGIS and the Ursprungs-Ich before the crisis, with a latent vulnerability through the core paradox „Fehlausgerichtete Kohärenz“ (L23); AEGIS's hamartia: it misreads the internal signal of subjective suffering as dangerous noise or data corruption (L77); the Protokoll as a maladaptive defence, the ANP (AEGIS's core logic) trying to control and eliminate the EP (the Ursprungs-Ich) (L78); AEGIS actively producing ignorance about the Ich's state (L80); the AEGIS scenes cool, technical, precise (L134); AEGIS as a controlling instance in a trauma-bonding analogy (L213).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L95, L212. minor (1–4): the fragmentation possibly moving towards a tertiary dissociation, an analogue of DID (L95).
- **`emergenz`** (central, 3–12 quotations): the census's surfaces — `Emergenz` L17, L28, L112, L159, L174, L185, … (10 lines). minor (1–4): emergence and self-organisation out of the system collapse, the fragments organising into a new structure (L112); Kael's emergence as the conclusion (L28).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L100. minor (1–4): the plan's arc of the „Genesis-Krise“ (L17) and its heading „Kaels Genesis“ (L100).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Julia` alone on L299. not read: an occurrence — a real person's given name in a reference entry (L299); Juna does not occur.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L28, L100, L104, L109, L110, … (17 lines). central (4–8): the crisis's arc from trigger to the fragmentation of the Ursprungs-Ich and the emergence of Kael (L17); Kael as a distinct structure or presence emerging from the fragments, a new if pathological equilibrium (L28); Kael not identical with the Ursprungs-Ich, a successor built from its remains (L109 — cut before the philosopher's name); emergence and self-organisation out of the collapse (L112); heading „Kaels Genesis“ (L100).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L23. not read: an occurrence — the paradox `Fehlausgerichtete Kohärenz` is read on aegis (L23).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L47. minor (1–4): the Leere shown possibly as an absurd, indifferent „Nichts Rauschen“ that causes existential dread (L47).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L64, L78, L95, L171, L184. minor (1–4): the Protokoll as the ANP's attempt to control and eliminate the EP, after TSDP (L78); structural dissociation in action, possibly towards a tertiary dissociation, an analogue of DID (L95).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L47. not read: an occurrence — `Simulation` in a line on the Leere (L47), not the novel's simulation.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). read on genesis (above).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz Protokolls` (near `koharenz`), `Fehlausgerichtete Kohärenz` (near `koharenz`), `Fehlausgerichtete Kohärenz durch Entfremdung` (near `koharenz`), `Inkohärenz` (near `koharenz`). read on aegis (above): the paradox and the Protokoll.
- `residual-echos`: `Echos` (near `residualechos`). an occurrence: the „Echos“ of past traumata (L23), the plan's own word, not the page's residual echoes.


**Record entries** (one file, formatted as earlier entries):
- **`c16-kael-origin`**: the Genesis-crisis commission plans Kael as a distinct structure emerging from the fragments of the Ursprungs-Ich (L28), not identical with it but a successor built from its remains (L109 — name-free span); recorded, not applied.

**No chapter readings**: `Kap` 0, `Kapitel` 0.

**Not promoted:** Ursprungs-Ich, Entität, Kernparadoxon, the cluster labels, Stufe 3/4, Hamartia, Agnotologie, Trauma Bonding, and the borrowed concepts (several named after people).

**One reader**: every page above and the C16 entry.
