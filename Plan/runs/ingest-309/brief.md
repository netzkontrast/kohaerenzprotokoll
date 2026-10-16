# Brief — readings from document 308 (step 6)

1 document, one reader, one batch: `ingest-309`. Files go to `Plan/runs/ingest-309/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 308 | `monstergruppe-metapher-auf-mathematische-kohaerenz` | 2025-04-25 | „the Monster-metaphor validation report“ (an unsigned German report with 33 web references) | a „Validierungsbericht“ (L11) setting the group theory of the Monstergruppe, the Baby-Monster-Gruppe, subquotients and Monstrous Moonshine against the novel's metaphor as a request (`Nutzeranfrage`) states it, answering „NEIN“, proposing an alternative plot (`Strategie B1`) and recommending revision; it excludes narrative aspects from its scope (L16) and claims no canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (194 lines for `monstergruppe-metapher-auf-mat`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A validation of a metaphor: write „the Monster-metaphor validation report judges / proposes …“. What it says of Kael, Juna, AEGIS and the K-J Verbindung it takes from the request it answers — mark those phrases as the request's (the report's own quotation marks). Its verdict and `Strategie B1` are its claim, never applied. Cut quotations before inner „…“ marks and glued digits.

## Pages — document 308, `monstergruppe-metapher-auf-mathematische-kohaerenz`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L90, L92, L103, L114, L143, L151. minor (1–3): the narrative contrast between M and AEGIS called too simple (L92); in the report's own proposal `Strategie B1`, AEGIS as „hyperrationale KI“ (L143) — its proposal.
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L103. not read: occurrence — `DID` (L103) is in the report's heading on Kael's fragmentation, read on kael.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L113. minor (1–3): the emergence of the connection from a substrate as „der potenziell am ehesten passende Aspekt“ of the metaphor (L113).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L96, L100, L111, L132, L134, L143. minor (1–3): the request's presentation of Kael and Juna as representatives of the Baby-Monster-Gruppen (L100), which the report says contradicts the mathematical relation (L101).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L96, L100, L103, L111, L132, L134, … (7 lines). minor (1–3): the request's presentation of Kael and Juna as representatives of the Baby-Monster-Gruppen (L100) and the report's verdict that it contradicts the mathematics (L101); on Kael's fragmentation, a guess at what the request means, „Möglicherweise ist gemeint“ (L103).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — `Kohärenz` (L11) is in the report's title on mathematical coherence.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L103. not read: occurrence — `Simulation` (L103) inside the heading on Kael's fragmentation.

- **`moonshine-link`** (central, 3–6): the report's critique of the `K-J Verbindung` as `Emergenter Moonshine` — „der mathematisch problematischste Aspekt der Metapher“ (L111); Moonshine „hochstrukturiert, keine generische Resonanz“ (L65); the use of the word devaluing the phenomenon (L115); emergence from a substrate the most apt part (L113); in `Strategie B1` the connection as a `Moonshine-Signatur` in data (L143) — its proposal. A critique of the metaphor, not a reading of the link as the novel has it; say so.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Idealbild integrierter Kohärenz` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`). occurrence: `Idealbild integrierter Kohärenz` the request's words in a heading (L84); `Kohärenz Protokoll` the project's name.
- `moonshine-link`: `Moonshine` (near `moonshinelink`). a reading — see the extra page below.


**Record entries:** none.

**Not promoted:** the Monstergruppe, the Baby-Monster-Gruppe, the Happy Family and the Pariahs, subquotients and the group-theory lens, the Moonshine-Modul and Verallgemeinerter Moonshine, the verdict NEIN, and Strategie B1.

**One reader**: every page above and the extra page.

**Chapter readings**: none — the document names no chapter.
