# Brief — readings from document 555 (step 6)

1 document, one reader, one batch: `ingest-555`. Files go to `Plan/runs/ingest-555/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 555 | `ki-roman-assistent-web-app-entwurf` | 2026-02-26 | „the web-console design“ | a design specification for a web console that applies the project's terms to a manuscript — four modules, a tool API, a skill, a colour palette and a workflow; the novel's terms serve as interface vocabulary; self-praise recorded, not applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (238 lines for `ki-roman-assistent-web-app-ent`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A software design: write „the web-console design …“; never canon. Read only what it says about figures as examples (L27, L47, L68, L103, L157). **Never cite L29** (a person's name), **L127, L146, L149, L233** (earlier names) **nor the colour-token table**.

## Pages — document 555, `ki-roman-assistent-web-app-entwurf`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L63, L103, L149, L157, L159, L190. minor: the controlling force of AEGIS against the protagonist's living parts, translated into CSS (L157); Ordnung/AEGIS against Chaos/Juna (L103).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L27, L104. minor: the protagonist with „elf distinkten Anteilen (Alters)“ (L27).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L66. not read: interface vocabulary only, or on a barred line.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L103, L157, L204. minor: „(Chaos/Juna)“ as one side of the dual-kernel evaluation (L103).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L27, L97, L112. minor: „Kael eine fragmentierte Psyche mit elf distinkten Anteilen (Alters)“ (L27).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L29, L97. not read: interface vocabulary only, or on a barred line.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: interface vocabulary only, or on a barred line.
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L29. not read: interface vocabulary only, or on a barred line.
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L29, L142. not read: interface vocabulary only, or on a barred line.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L47, L104, L157. minor: Lex „(ein primärer ANP, der durch absolute Logik Kontrolle erzwingen will)“ as an example of a rule check (L47).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L68, L143. minor: „Lia“ as „(ein Trickster-Kind-EP)“ in an example (L68).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L171, L178. not read: interface vocabulary only, or on a barred line.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L147. not read: interface vocabulary only, or on a barred line.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L19. not read: interface vocabulary only, or on a barred line.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L62, L104, L144. not read: interface vocabulary only, or on a barred line.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L63. not read: interface vocabulary only, or on a barred line.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L62, L147. not read: interface vocabulary only, or on a barred line.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L19, L27, L62, L97, L153, L159. minor: amnesia and dissociation in TSDP as active barriers (L159).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L29. not read: interface vocabulary only, or on a barred line.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `dkt`: `Dual-Kernel-Theorie` (near `dualkerneltheoriedkt`). an occurrence.
- `kaels-wohneinheit`: `Kaels` (near `kaelswohneinheit`), `Kaels` (near `kaelswohneinheit10`). an occurrence.
- `kohaerenz`: `Kohärenz-Protokoll` (near `koharenz`), `Kohärenz-Protokolls` (near `koharenz`), `Cache-Inkohärenz` (near `koharenz`). an occurrence.
- `multiplizitaet`: `Funktionalen Multiplizität` (near `multiplizitat`). an occurrence.
- `nexus`: `Charakter-Nexus und das TSDP-Geflecht` (near `nexus`). an occurrence.


**Record entries:** none.

**Not promoted:** the four modules, the tool API, A2UI, Generative UI, Kintsugi, Axis Mundi, Welt-Bibel, the skill, the workflow phases.

**One reader**: every page above.
