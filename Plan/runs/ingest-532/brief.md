# Brief — readings from document 532 (step 6)

1 document, one reader, one batch: `ingest-532`. Files go to `Plan/runs/ingest-532/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 532 | `erstelle-eine-liste-mit-allen-plot-points-formu` | 2025-04-17 | „the plot summary (V4)“ | a three-part plot summary of an earlier plot idea under the working title „Das Seelen-Kohärenz-Protokoll“ (L15): episodes from the persona realities, the Guardians' intervention from the Überraum, the hunt for the outside and an inner integration; a summary of a plan, no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (60 lines for `erstelle-eine-liste-mit-allen-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A summary of an earlier plot idea: write „the plot summary (V4) …“ and word every reading as what that plan proposes, never as what happens in the novel. **Never cite L11** (it addresses whoever asked for the summary). The protagonist is „nicht näher definiert“ (L17): never put Kael's name on it. No gendered pronoun for the Partnerin, the Guardians or the personas in our own prose; quotations stay verbatim, preferably cut before pronouns.

## Pages — document 532, `erstelle-eine-liste-mit-allen-plot-points-formu`

- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L24, L36. minor (1–4): one of the five Guardians assigned to the persona realities, observing subtly (L24); in Part 2 explains the problem from its specialised view (L36 — Cerberus is listed in the order Logik, Erinnerung, Sicherheit, Potenzial, Wissen; say only that L36 gives the five views in the same order as the names, quote „aus seiner spezialisierten Sicht“).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L11, L17, L24, L30, L35, L38, … (8 lines). minor (1–4): higher entities in the Überraum (L17 — quote only a span without the reader's address); they analyse the crisis and name the fragmentation as cause of the „Risse“ (L30, L35); find no data on the Partnerin and declare an anomaly or projection (L38); equip the personas with „Integrations-Werkzeugen“ (L39); warn against the hunt and reach their limits (L51).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L24, L36. minor (1–4): one of the five Guardians assigned to the persona realities, observing subtly (L24); in Part 2 explains the problem from its specialised view (L36 — Kairos is listed in the order Logik, Erinnerung, Sicherheit, Potenzial, Wissen; say only that L36 gives the five views in the same order as the names, quote „aus seiner spezialisierten Sicht“).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L39. not read: occurrences — the working title (L15), „interne Kohärenz“ of the tools (L39) and „funktionale Kohärenz“ as the ending's state (L54) use the word, not the page's term (J9).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L24, L36. minor (1–4): one of the five Guardians assigned to the persona realities, observing subtly (L24); in Part 2 explains the problem from its specialised view (L36 — LogOS is listed in the order Logik, Erinnerung, Sicherheit, Potenzial, Wissen; say only that L36 gives the five views in the same order as the names, quote „aus seiner spezialisierten Sicht“).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L24, L36. minor (1–4): one of the five Guardians assigned to the persona realities, observing subtly (L24); in Part 2 explains the problem from its specialised view (L36 — Mnemosyne is listed in the order Logik, Erinnerung, Sicherheit, Potenzial, Wissen; say only that L36 gives the five views in the same order as the names, quote „aus seiner spezialisierten Sicht“).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Multiplizität` L30, L54, L55. minor (1–4): the protagonist-system becoming aware of its multiplicity (L30); the final integration as acceptance of the personas' multiplicity (L54); the end „stabiler, funktionaler Multiplizität“ (L55).
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L30. minor (1–4): the Überraum glossed as „Meta-Realität/Schaltzentrale/Nexus“ (L30).
- **`partnerin`** (central, 3–12 quotations): the census's surfaces — `Partnerin` L11, L17, L23, L26, L38, L39, … (15 lines). central (3–8): present in every Part-1 episode, adapted to each reality, an emotional anchor (L23); the bond seemingly cut at the „Bruch der Realitäten“ (L26); the Guardians find no data on her (L38) and ignore her (L39); returns with a disturbed bond (L49); seems not subject to „Seele = Information“ (L50); the twist: refusing to accept the transcendent bond feeds the cracks (L53); the ending lives the bond (L54, L55).
- **`personas`** (central, 3–12 quotations): the census's surfaces — `Personas` L17, L21, L22, L30, L37, L38, … (13 lines); `Persona` L17, L21, L22, L24, L25, L26, … (16 lines). central (3–8): the fragmented core consciousness as „Personas“ (L17); the five core personas Architekt, Echo, Wächter, Funke, Sucher, each unaware of its fragmentation (L21); intrusions from other personas' realities (L22); confronted with their nature (L37); repair attempts across the persona worlds (L48); the hunt for the outside (L51); turning inward to cooperation (L54).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L17, L25, L35, L39, L50, L52, … (7 lines); `Glitches` L21, L25. minor (1–4): instabilities caused by the fragmentation (L17); glitches, intrusions and cracks escalating over the 13 episodes (L25); cracks in the simulation structure (L35); the hunt causes larger cracks (L52) and is the twist's main cause (L53).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L24, L36. minor (1–4): one of the five Guardians assigned to the persona realities, observing subtly (L24); in Part 2 explains the problem from its specialised view (L36 — Sophia is listed in the order Logik, Erinnerung, Sicherheit, Potenzial, Wissen; say only that L36 gives the five views in the same order as the names, quote „aus seiner spezialisierten Sicht“).
- **`ueberraum`** (minor, 1–4): the census's surfaces — `Überraum` L17, L26, L28, L30. minor (1–4): the „Bruch der Realitäten“ triggers an alarm in the Überraum (L26); Part 2's perspective shift to the Überraum as meta-reality (L28, L30).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L11. not read: an occurrence — `Simulation` on L11 is the summary's address line; the premise's simulation (L17) is not named Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis`: `Wächter` (near `wachterdersystemischenstabilitat`). an occurrence: `Wächter` is one of the five core personas (L21), not AEGIS.
- `did`: `Fragmentierung` (near `psychischefragmentierung`). an occurrence: the fragmentation of the protagonist's core consciousness (L17), no diagnosis named.
- `kohaerenz`: `Seelen-Kohärenz-Protokoll` (near `koharenz`), `Seelen-Kohärenz-Programm` (near `koharenz`), `funktionale Kohärenz` (near `koharenz`). occurrences: the working title, the programme and the ending's state — read on none (J9, J16).
- **`kohaerenz-programm`** (minor, 1–4), a reading by the sentence: `Seelen-Kohärenz-Programm` (near `koharenzprogramm`). a reading: the „Seelen-Kohärenz-Programm“ that keeps simulated existences stable and is destabilised by the fragmentation (L17, L35).
- `mnemosyne-server-architektur`: `Architekt` (near `mnemosyneserverarchitektur`). an occurrence: `Architekt` is a core persona (L21).
- `residual-echos`: `Echo` (near `residualechos`). an occurrence: `Echo` is a core persona (L21).
- `ztv`: `Das Außen` (near `ztvvertrauenlosevalidierung`). an occurrence: „Das Außen“ is the simulation's outside sought in Part 3 (L51).


**Record entries:** none.

**Not promoted:** Kern-Bewusstsein, Funke, Sucher, Intrusionen, Hüter, Meta-Narrator, Bruch der Realitäten, Integrations-Werkzeuge, Seele = Information, Jagd nach der Realität, Die Naht im Selbst, Klarheit, Protagonisten-System, the part titles.

**One reader**: every page above, including `kohaerenz-programm`.
