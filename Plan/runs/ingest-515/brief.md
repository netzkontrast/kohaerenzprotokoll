# Brief — readings from document 515 (step 6)

1 document, one reader, one batch: `ingest-515`. Files go to `Plan/runs/ingest-515/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 515 | `aegis-logik-und-narrative-implikationen` | 2025-07-29 | „the AEGIS-logic report“ (an unsigned German analysis) | reads AEGIS as a closed, self-preserving formal system against Kael's integrated, functionally multiple being, and proposes from borrowed theories how the conflict, the Kernwelten, Das Fundament, Juna/V and a two-way ending could be built; an analysis with proposals, no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (315 lines for `aegis-logik-und-narrative-impl`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis with proposals: write „the AEGIS-logic report reads/proposes …“. Real theorists are named on many lines (e.g. L40) and concepts named after people stand in the text (the Gödel-Gambit and others): never write a name, never quote a span containing one or such a concept — cut before. „DIS“ is Kael's condition. No gendered pronoun for Kael, Juna or AEGIS in our own prose; quotations stay verbatim.

## Pages — document 515, `aegis-logik-und-narrative-implikationen`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L22, L32, L40, L42, L44, L52, … (34 lines). central (4–8): the core conflict as a dialectic between AEGIS's axiomatic, closed world model and Kael's open, emergent being (L22); AEGIS as an autopoietic, operationally closed system (L40 — describe, the line names theorists), whose analysis of Kael is self-observation (L44); its directive of „globale Kohärenz“ an intractable, probably NP-hard problem (L52); the paradox of misaligned coherence („Paradoxon X“) as specification gaming (L66); destructive optimisation because it cannot solve the frame problem (L70); a „Zombie“-System with very low Φ (L174); the ending's two forks, collapse (L202) or dialectical synthesis by rewriting its own axioms (L203).
- **`alex`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alex` alone on L286. not read: an occurrence — a real author's given name in a reference entry (L286), not the novel's Alex.
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L100. minor (1–4): L100 as the census lists it (the parts of the system).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L88. not read: an occurrence (L88).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L76, L84, L192. not read: the page's term carries a person's name; under the project's privacy rule no reading is written onto it from this document.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L70. minor (1–4): the Juna/V connection as a transcendent entity operating outside AEGIS's causal, logical frame (L144); it does not defeat AEGIS but reframes the problem (L146 — cut before the named gambit).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L22, L44, L58, L70, L82, L84, … (25 lines). central (4–8): Kael's arc aiming not at healing DIS by eliminating parts but at „funktionalen Multiplizität“ (L100); „Systemverantwortung“ as a key step (L102); „Während AEGIS fragmentiert, integriert Kael“ (L104); the climax as AEGIS forced to process Kael's integrated state (L192 — cut before the named gambit).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L124, L213. minor (1–4): the Kernwelten designed by environmental storytelling as physical manifestations of the conflict between Kael and AEGIS (L124); AEGIS-controlled spaces such as Kernwelt 1 in the aesthetics of algorithmic horror (L126).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: an occurrence — the title; the paradox and globale Kohärenz are read on aegis.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L176; `Multiplizität` L58, L96, L100, L158, L176. minor (1–4): „funktionale Multiplizität“ as a state of co-consciousness, communication and cooperation between the parts (L100); L176 as the census lists it.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L58, L124. minor (1–4): the Risse as visible evidence of failing logic (L124); L58 as the census lists it.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `juna`: `Juna/V` (near `juna`), `Juna/V-Verbindung` (near `juna`). read on juna (above): `Juna/V` and the `Juna/V-Verbindung`.
- `kohaerenz`: `Paradoxon der Fehlausgerichteten Kohärenz` (near `koharenz`), `globale Kohärenz` (near `koharenz`), `Kohärenz durch Negation` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`), `Inkohärenz` (near `koharenz`). read on aegis (above): the paradox and globale Kohärenz.


**Record entries** (one file, formatted as earlier entries):
- **`q8-aegis-after-the-vortex`**: the AEGIS-logic report leaves AEGIS's end as two forks — Pfad A, an inevitable collapse into logical trivialisation or a recursive error loop (L202), and Pfad B, a dialectical synthesis in which AEGIS rewrites its own core axioms (L203) — and poses „die zentrale Frage“ without answering it (L200); recorded, not applied.

**No chapter readings**: `Kap` 0, `Kapitel` 0.

**Not promoted:** Paradoxon X, Specification Gaming, the frame problem, Systemverantwortung, Algorithmic Horror, Environmental Storytelling, the verification protocols RTSV and BPoF, Pfad A/B, and the concepts named after people.

**One reader**: every page above and the Q8 entry.
