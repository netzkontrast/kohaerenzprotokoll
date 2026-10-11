# Brief — readings from document 259 (step 6)

1 document, one reader, one batch: `ingest-259`. Files go to `Plan/runs/ingest-259/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 259 | `arbeitshilfe-kohaerenz-protokoll-kapitel-2` | 2025-04-20 | „the chapter-2 expert analysis“ (an unsigned German report) | „ergänzende Expertenanalyse“ (L17) of a working aid (the Arbeitshilfe) for chapter 2, part 1: Kael's state in the transition out of KW1, the alters, liminality, Environmental Storytelling, the system's intervention, a beat table 1.X–1.Z and five recommendations; proposals, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (342 lines for `arbeitshilfe-kohaerenz-protoko`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Three voices: the Arbeitshilfe's demands as the analysis reports them („the working aid, as reported, asks …“), cited research (glued reference numbers), and the analysis's own conditional proposals („the analysis proposes …“). Question marks after alter names in the beats mark suggestions; keep them. Chapter pages are written by the session (`Plan/runs/ingest-259-kap/`). Cut quotations before reference numbers glued to words and inner quotes.

## Pages — document 259, `arbeitshilfe-kohaerenz-protokoll-kapitel-2`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L17, L75, L183, L185, L187, L191, … (9 lines). minor (1–4): the system's interventions, as the working aid demands, manifesting as environmental effects or anomalies (L187); what the transition space may reveal about AEGIS (L183); interventions possibly feeling hostile, against the helpful-AI trope (L206).
- **`alters`** (central, 3–12 quotations): the census's surfaces — `Alters` L17, L23, L45, L51, L53, L55, … (19 lines). central (3–6): the working aid wanting the influence of Limina, Nox, Praetor and Echo/Silas shown (L51); alters defined from cited research (L53); passive influence and co-consciousness (L55–L56); Praetor's attempt at control and Echo/Silas carrying the pain of loss, as proposals (L59); phobic avoidance between alters (L61).
- **`did`** (central, 3–12 quotations): the census's surfaces — `DID` L15, L45, L51, L53, L56, L61, … (10 lines). minor (1–4): the borrowed terms for Kael's DID — passive influence, co-consciousness, phobic avoidance (L55–L61); a possible overlap (L45).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L187. minor (1–4): the Guardians among the system's interventions the working aid wants shown as environmental effects (L187).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L17, L19, L21, L23, L27, … (60 lines). central (3–6): the collapse of KW1 a severe trauma for Kael (L27); possible emotional emptiness (L30); his inner state shaping the description of his surroundings (L45); his transition possibly feeling like death and rebirth (L112); the environment a manifestation of his psyche (L181); his perception unreliable from trauma and dissociation, an unreliable narrator (L189, L204).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kern-Welten` L47, L183. minor (1–4): the transition between simulated Kern-Welten paralleled with VR research (L47); the collapse of KW1 (L27); the first hints of KW2's identity and rules (L280).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — the title (L11).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitches` alone on L107. not read: occurrence — `Glitches` at L107 is one auditory motif among others for the transition space.
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L51, L59, L225, L267. minor (1–4): `Echo/Silas` among the alters the working aid names (L51); carrying the emotional pain of loss, as a proposal (L59); a beat focus (L225, L267).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L47. not read: occurrence — `Simulation` at L47 is the simulated Kern-Welten paralleled with VR research, read on kern-welten.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title.
- `kollaps-kernel`: `Kollaps` (near `kollapskernel`), `Kollaps` (near `kollapskernelk0`). occurrence: `Kollaps` is the collapse of KW1, not the kernel.
- `personas`: `Depersonalisation` (near `persona`). occurrence: Depersonalisation is a symptom, not the Personas.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` is the alter Echo/Silas, read on silas.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: four alters named for chapter 2 — Limina, Nox, Praetor, Echo/Silas (L51); KW1 collapsing and KW2 at the threshold (L223, L280); no count.

**Not promoted:** the Arbeitshilfe, Übergangsraum, Liminalität, Environmental Storytelling, Show, Don't Tell, the beats 1.X–1.Z, Limina, Nox, Praetor (alter names without pages), Datensturm.

**One reader**: kael, alters, did, silas, aegis, guardians, kern-welten and the record q3; `risse` is an occurrence. `kohaerenz` and `ueberwelt` are occurrences.

**Chapter readings**: Kap 2, by the session (`Plan/runs/ingest-259-kap/`).
