# Brief — readings from document 236 (step 6)

1 document, one reader, one batch: `ingest-236`. Files go to `Plan/runs/ingest-236/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 236 | `kohaerenz-protokoll-finale-pfeiler` | 2025-07-29 | „the final pillars report“ (an unsigned German synthesis report) | a German synthesis report in five parts on how the novel's ending should be built — the Fundament reached through Gnosis, AEGIS's two paths, Kael's functional multiplicity, Juna/V as a living Gödel-Satz, the title read as Kael's journey; it offers options (Pfad A/B) without choosing; a proposal, not canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (312 lines for `kohaerenz-protokoll-finale-pfe`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A synthesis that prescribes and offers options: write „the final pillars report proposes …“; Pfad A and Pfad B are options it leaves open. Its alter table repeats the one of the detailed research report (223) row for row — do not read it again. It cites a research task by glued number `1` — quote around it; borrowed theory (Whitehead, Bachtin, Deleuze/Guattari) is its lens.

## Pages — document 236, `kohaerenz-protokoll-finale-pfeiler`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L30, L54, L62, L66, L70, L78, … (33 lines). central (2–4): „AEGIS ist als autopoietisches System konzipiert“ (L78); defined by negation of the entropic Nichts Rauschen (L82); Pfad A, collapse, „Das System wird trivial“ (L102); Pfad B, transformation, „Sie wäre etwas Neues“ (L110–L112), left ambivalent for the reader (L112); AEGIS operating only on Episteme (L54); its directive „gefährlich unvollständig und schlecht spezifiziert“ (L249).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L144. occurrence: `DID` is the clinical gloss of the TSDP model (L144).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L42. occurrence: `Emergenz` stands in „schwache Emergenz“, the Fundament's mode (L42), not AEGIS's emergence.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L88. minor (1–3): the Gödel-Gambit named as the climax mechanism (L88); Juna/V and Kael's integrated state as „der lebende Gödel-Satz für das formale System AEGIS“ (L92).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L56, L88, L92, L102, L114, L191, … (14 lines). central (2–4): „Juna/V ist der Gödel-Satz in lebender Form“ (L216); the connection between Kael and Juna/V „ist kein Datensignal“ (L203), modelled as Whitehead's prehension and structural resonance (L205), AEGIS „ontologisch blind“ to it (L208); its power „nicht interventionistisch, sondern existenziell“ (L195).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L44, L54, L56, L60, L62, L82, … (38 lines). central (2–4): „Kael hingegen erlangt Zugang durch Gnosis“ (L56); his psyche structured by the TSDP model (L144); co-fronting as the outward form of integration (L152); his inner world staged as a polyphonic novel (L160).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L125. minor (1–3): in Pfad A, the dissolution of the Kernwelten into chaos (L125).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L144, L185. not read: the same table row as the detailed research report (L185).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. occurrence: the title (L13); `Kohärenz-Inseln` a figure of the argument.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L144, L152, L170, L186. not read: the same table row as the detailed research report (L186).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L132, L148. minor (1–3): „Funktionale Multiplizität“ as a heading of the report (L132, L148) — quote around the escapes; co-fronting, several parts sharing control at once (L152).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L82, L290. minor (1–3): AEGIS defining itself by what it excludes, „das entropische "Nichts Rauschen"“ — quote around the inner quotes (L82).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L144, L152, L170, L184. not read: the same table row as the detailed research report (L184).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L30, L102, L127, L268. minor (1–3): in Pfad A AEGIS ends „Zerstört, in das "Potentialmeer" zurückgefallen, nicht-existent“ — quote around the inner quotes (L127).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L22. minor (1–3): the question of „der ultimativen Realitätsebene“, the Fundament, as the ontological pivot (L22).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L102, L125. minor (1–3): in Pfad A, „Eskalierende "Risse" im System“ — quote around the inner quotes (L125).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L187. not read: the same table row as the detailed research report (L187).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L140, L144, L182. not read: the same TSDP account as the detailed research report (L144); read on kael.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L22. occurrence: `Simulation` stands in the Fundament's definition, not a further simulation level (L22, L30), not the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `emergenz`: `schwache Emergenz` (near `emergenz`). occurrence: `schwache Emergenz` is the Fundament's mode (L42).
- `kohaerenz`: `Kohärenz-Inseln` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`). occurrence: the title and `Kohärenz-Inseln`, a figure of the argument.


**Record entries** (one file each):

- **`q8-aegis-after-the-vortex`**: two options left open — Pfad A, collapse back into the Potentialmeer; Pfad B, a new, ambivalent paraconsistent entity (L102–L112, L125–L127).
- **`q9-moonshine-link-boundary`**: the Kael–Juna/V connection not a data signal, AEGIS ontologically blind to it (L203–L208).

**Not promoted:** Das Fundament, Gnosis/Episteme, Kohärenz-Inseln, co-fronting, the polyphonic and rhizomatic self, the reading of the title, the ethics section.

**One reader**: aegis, kael, juna, goedel-gambit, kern-welten, multiplizitaet, nichts-rauschen, potentialmeer, realitaetsebenen, risse and the records q8, q9.

**Chapter readings**: none — the report names no chapter.
