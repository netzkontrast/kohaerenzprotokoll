# Brief — readings from document 260 (step 6)

1 document, one reader, one batch: `ingest-260`. Files go to `Plan/runs/ingest-260/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 260 | `kernwelten-fuer-kohaerenz-protokoll` | 2025-04-27 | „the Kernwelten design report“ (an unsigned German report) | a design report working out the four worlds Co₁, McL, B and Ly from borrowed concepts (sporadic groups, Gödel, chaos, emergence, IFS, Jung's shadow), each with aesthetics, system logic, „Kaels Schmelztiegel“ and a guardian profile, then AEGIS, the K-J connection, a comparison table and recommendations; it calls itself a conceptual blueprint (L493), not canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (685 lines for `kernwelten-fuer-kohaerenz-prot`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A design proposal: write „the Kernwelten design report proposes …“; hedged descriptions („könnte“, „vielleicht“) stay hedged. It reports a brief (`User Prompt`, `Briefing`) it does not reproduce: say so where a line marks it. The world names Co₁, McL, B, Ly and the guardian names are its own. Cut quotations before reference numbers glued to words and inner quotes; the subscript in Co₁ survives `--find`, digits glued to words may not.

## Pages — document 260, `kernwelten-fuer-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L16, L29, L53, L69, L230, … (25 lines). central (3–6): using the Kernwelten as laboratories to isolate facets of „der Entität M (manifestiert als Kael)“ (L408); its control possibly imperfect, itself subject to Gödelian limits (L410); transitions between worlds often involuntary, initiated by AEGIS (L387).
- **`cache-kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Cache Kohärenz` L15, L16, L149, L182, L213, L263, … (14 lines). central (3–6): Kael's identity split into incoherent caches, each dominant in one world (L149); the central character dynamic the worlds must enable (L153); each world mapped to an IFS part type — Co₁ Manager-dominant, McL relational parts, B exile/firefighter-dominant, Ly Self/creative parts (L182).
- **`emergenz`** (central, 3–12 quotations): the census's surfaces — `Emergenz` L61, L93, L105, L332, L338, L344, … (17 lines). minor (1–4): „Emergenz als Kernmechanik“ for one world (L332 or the heading line); L61, L93 only if they speak of the worlds.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L16. minor (1–4): one guardian per world, written `Wächter`: LogOS-Supervisor (L225), Netzweber (L275), Chaos-Regulator (L324), Möglichkeits-Weber (L373); „Die vier Wächter sind als distinkte Entitäten konzipiert“ (L482); their roles from antagonistic rule-enforcer to catalyst (L440–L442).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L29, L45, L69, L89, L97, … (66 lines). central (3–6): his identity split into caches (L149); „Kaels Schmelztiegel“ in each world; B as a projection of his inner chaos (L301); M manifested as Kael (L408).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L11, L15, L408, L458, L478, L493. central (3–6): four worlds Co₁, McL, B and Ly, each a self-contained simulation (L478); headings by theme — order and perfection (L184), networks and trust (L233), chaos and shadow (L283), and the fourth; Co₁'s perfect order containing the seed of its own dissolution (L204); AEGIS's laboratories (L408).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — the title (L11).
- **`logos`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `LogOS` alone on L280. minor (1–4): the `LogOS-Supervisor`, guardian of Co₁ (L225); the Netzweber giving no direct orders „wie LogOS“ (L280).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Potentialmeer` alone on L352. minor (1–4): the creative world's environment as a „Potentialmeer“ where forms arise (L352).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L69. minor (1–4): „Gödelsche Risse“ in Co₁, perfect order producing undecidable statements (L197, L204); L69.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L478. not read: occurrence — `Simulation` at L478 calls each world a self-contained simulation, read on kern-welten.

- **`kael-julia-bindung`** (minor, 1–3): the K-J-Verbindung as the mechanism for coherent information transfer across world borders and cache separations, marked as from the brief (L418); possibly a psychic connection (L419), probably of limited bandwidth (L421); J never defined.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Cache Kohärenz Manifestation` (near `koharenz`). occurrence: the title; `Cache Kohärenz Manifestation` a heading label read on cache-kohaerenz.
- `logos`: `LogOS-Supervisor` (near `logos`). `LogOS-Supervisor` read on logos.
- `risse`: `Gödelsche Risse` (near `risse`). `Gödelsche Risse` read on risse.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: four worlds Co₁, McL, B, Ly, each mapped to an IFS part type, not to named alters (L182, L478).
- **`q4-waechter-four-bearers`**: `Wächter` as the document's word for the four world guardians (L482).
- **`q5-guardians-and-kern-welten`**: one guardian per world — LogOS-Supervisor for Co₁, Netzweber for McL, Chaos-Regulator for B, Möglichkeits-Weber for Ly (L225, L275, L324, L373).
- **`c16-kael-origin`**: „der Entität M (manifestiert als Kael)“ (L408).

**Not promoted:** Co₁, McL, B, Ly as pages of their own, the guardian names Netzweber, Chaos-Regulator, Möglichkeits-Weber, Kaels Schmelztiegel, Dominanter Cache, the sporadic groups, the borrowed concepts.

**One reader**: kern-welten, kael, aegis, cache-kohaerenz, guardians, logos, kael-julia-bindung, potentialmeer, risse, emergenz and the records q3, q4, q5, c16. `kohaerenz` and `ueberwelt` are occurrences.

**Chapter readings**: none — `Kapitel` stands nowhere.
