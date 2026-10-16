# Brief — readings from document 273 (step 6)

1 document, one reader, one batch: `ingest-274`. Files go to `Plan/runs/ingest-274/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 273 | `ui-konzept-fuer-roman-entwicklungssystem` | 2026-02-27 | „the UI concept“ (an unsigned German design concept) | a design concept for writing software around the novel, in five interface spheres, each figure given an interface role; it calls the software the novel's „methodologische Manifestation“ (L153), its claim; a tool's design, read lightly: only its statements about the novel's world |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (230 lines for `ui-konzept-fuer-roman-entwickl`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Light pass: a software design. Write readings only where the UI concept says something about the novel's world — the two kernels, AEGIS and Juna, Kael's eleven subsystems, Selene's role — „the UI concept places / describes …“; the interface roles (dashboards, linters, permissions, glitches in the UI) are the software's, not the novel's, and are not read. The export lost the kernel symbols (empty parentheses): quote around them.

## Pages — document 273, `ui-konzept-fuer-roman-entwicklungssystem`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L87, L93, L111, L113, L115, … (17 lines). minor (1–2): „Autonomous Entropic Gatekeeper for Integrity Systems“ and the driving force of the Kohärenz-Kernel, its need absolute stability and control (L113).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L138, L208. not read: an interface role in the software, not the novel's world.
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L136. not read: an interface role in the software, not the novel's world.
- **`chaitin-konstante`** (minor, 1–4): the census's surfaces — `Chaitin-Konstante` L121. minor (1–2): Juna as the personified Chaitin constant: logically incomputable, incompressible, metaphysically necessary and „wahr“ (L121).
- **`dkt`** (minor, 1–4): the census's surfaces — `Dual-Kernel-Theorie (DKT)` L17, L109; `DKT` L17, L107, L109. minor (1–2): „die Dual-Kernel-Theorie (DKT) des Romans“ as the novel's central tension (L17).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L65. not read: an interface role in the software, not the novel's world.
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L75. not read: an interface role in the software, not the novel's world.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L17, L89, L119, L121, L123, L124, … (9 lines). minor (1–2): „Juna repräsentiert den Kollaps-Kernel“ and absolute entropy, the personified Chaitin constant (L121).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L29, L53, L88, L97, L117, … (13 lines). minor (1–2): Kael's psyche split by a tertiary structural dissociation into eleven specialised subsystems (L129).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L139, L159. not read: an interface role in the software, not the novel's world.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: an interface role in the software, not the novel's world.
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L17, L113. minor (1–2): AEGIS the driving force of the Kohärenz-Kernel (L113).
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L17, L121. minor (1–2): Juna represents the Kollaps-Kernel and absolute entropy (L121).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L67, L97, L105, L137. not read: an interface role in the software, not the novel's world.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L139. not read: an interface role in the software, not the novel's world.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L93, L140. not read: an interface role in the software, not the novel's world.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L141. minor (1–2): Selene striving for functional multiplicity (L141).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts-Rauschen` L73, L159. not read: an interface role in the software, not the novel's world.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L87, L97, L138, L159. not read: an interface role in the software, not the novel's world.
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Personas` alone on L29. not read: an interface role in the software, not the novel's world.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitches` alone on L124. not read: an interface role in the software, not the novel's world.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L141, L143, L165. minor (1–2): „(Innere Helferin / ISH)“, core self striving for functional multiplicity, in the table's profile column (L141); not her interface role.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L29, L81, L109, L127, L129, L135, … (7 lines). minor (1–2): Tertiäre Strukturelle Dissoziation (TSDP) splitting Kael's psyche into eleven subsystems (L129).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L13. not read: an interface role in the software, not the novel's world.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie`: `Entropie-Kartografie` (near `entropie`), `Thermale Entropie-Maps` (near `entropie`), `Entropie-Toleranz` (near `entropie`). occurrence: a software term or label, not read.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Konstrukt` (near `koharenz`), `Paradoxon der Fehlausgerichteten Kohärenz` (near `koharenz`), `Kohärenztheorie` (near `koharenz`). occurrence: a software term or label, not read.
- `ueberwelt`: `Ontologische Simulationsumgebung` (near `simulation`). occurrence: a software term or label, not read.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: Kael's psyche „in elf spezialisierte Subsysteme zersplittert“ (L129).

**Not promoted:** everything of the software — the five spheres, the Drama Engine, the Codex, the Tribunal, the dashboards and interface roles, Platonia, the Landauer metaphor for deletion.

**One reader**: the pages given a reading above and the record q3.

**Chapter readings**: none — the document names no chapter.
