# Brief — readings from document 313 (step 6)

1 document, one reader, one batch: `ingest-314`. Files go to `Plan/runs/ingest-314/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 313 | `emergenz-autonomer-systeme-aegis-forschung` | 2025-04-27 | „the AEGIS fundamental-research report“ (an unsigned German report with 75 web references) | a review of borrowed complexity concepts (emergence, self-organisation, autopoiesis, dissipative structures) against thirteen Spannungsfelder, then „Kohärenz aus Entropie“ as a speculative AEGIS concept and six speculative architecture principles; it says no established definition of AEGIS exists in the literature and calls it „ein neuartiges theoretisches Konstrukt“ (L443) and a speculative construct (L517), its claim — a sibling report to document 312, not a copy |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (598 lines for `emergenz-autonomer-systeme-aeg`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A research report on a speculative construct: write „the AEGIS fundamental-research report conceptualises / asks …“; its `AEGIS-Relevanz` passages are largely questions — keep them as questions. The borrowed concepts are lens. Cut quotations before glued reference numbers.

## Pages — document 313, `emergenz-autonomer-systeme-aegis-forschung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L21, L23, L39, L41, L47, … (62 lines). central (3–6): „ein neuartiges theoretisches Konstrukt“ with no established definition (L443); a system or protocol producing and keeping internal coherence from higher entropy (L445); framed as a dissipative structure (L449); asked: monolithic or decentralised (L252), inner awareness (L301), its boundary (L385); „einen vielversprechenden, wenn auch ambitionierten Kandidaten“ (L484); a speculative construct (L517).
- **`emergenz`** (central, 3–12 quotations): the census's surfaces — `Emergenz` L17, L43, L49, L53, L55, L58, … (26 lines). minor (1–3): weak and strong emergence „von entscheidender Bedeutung“, the report asking which AEGIS aims at (L58).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L33. minor (1–3): `Kohärenz aus Entropie` as the core concept, coherence produced from a state of higher entropy (L445) — say speculative; L33 is a cluster heading.
- **`grosse-mauer`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Systemgrenze` alone on L392. not read: occurrence — `Systemgrenze` (L392) is the abstract system's boundary in the synthesis.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L59. not read: occurrence — `Kohärenz` (L59) is a key feature of emergence in a borrowed definition; the core concept is read on entropie and aegis.
- **`negentropie`** (minor, 1–4): the census's surfaces — `Negentropie` L390. minor (1–3): only where negentropy is tied to AEGIS; else not read.
- **`nexus`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Nexus` alone on L582. not read: occurrence — `Nexus` (L582) is a journal name in the reference list.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L165. not read: occurrence — `Simulation` (L165) is the simulation of cosmogenesis in a highly speculative technology item.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `ars`: `Reentry` (near `arsautopoietischereentrysegmentierung`). occurrence: the report's labels and borrowed terms (`AEGIS-Projekt`, `AEGIS-Protokoll`, `AEGIS-Framework`, `AEGIS-Relevanz`, `selbstgenerierendes Kohärenzsystem`, `Kohärenzentropie`, `Kohärenzkern`, `Kohärenzmaximierung / Entropieminimierung`, weak and strong emergence, `Reentry`) — read with the page's reading where they add, not promoted; `Kohärenzkern` is the report's word, not the Kohärenz-Kernel.
- `entropie`: `Kohärenz aus Entropie` (near `entropie`), `Kohärenzentropie` (near `entropie`), `Kohärenzmaximierung / Entropieminimierung` (near `entropie`). occurrence: the report's labels and borrowed terms (`AEGIS-Projekt`, `AEGIS-Protokoll`, `AEGIS-Framework`, `AEGIS-Relevanz`, `selbstgenerierendes Kohärenzsystem`, `Kohärenzentropie`, `Kohärenzkern`, `Kohärenzmaximierung / Entropieminimierung`, weak and strong emergence, `Reentry`) — read with the page's reading where they add, not promoted; `Kohärenzkern` is the report's word, not the Kohärenz-Kernel.
- `kohaerenz`: `selbstgenerierendes Kohärenzsystem` (near `koharenz`), `Kohärenz aus Entropie` (near `koharenz`), `Kohärenzentropie` (near `koharenz`), `Kohärenzkern` (near `koharenz`), `Kohärenzmaximierung / Entropieminimierung` (near `koharenz`). occurrence: the report's labels and borrowed terms (`AEGIS-Projekt`, `AEGIS-Protokoll`, `AEGIS-Framework`, `AEGIS-Relevanz`, `selbstgenerierendes Kohärenzsystem`, `Kohärenzentropie`, `Kohärenzkern`, `Kohärenzmaximierung / Entropieminimierung`, weak and strong emergence, `Reentry`) — read with the page's reading where they add, not promoted; `Kohärenzkern` is the report's word, not the Kohärenz-Kernel.
- `kohaerenz-kernel`: `Kohärenzkern` (near `koharenzkernel`), `Kohärenzkern` (near `koharenzkernelk1`). occurrence: the report's labels and borrowed terms (`AEGIS-Projekt`, `AEGIS-Protokoll`, `AEGIS-Framework`, `AEGIS-Relevanz`, `selbstgenerierendes Kohärenzsystem`, `Kohärenzentropie`, `Kohärenzkern`, `Kohärenzmaximierung / Entropieminimierung`, weak and strong emergence, `Reentry`) — read with the page's reading where they add, not promoted; `Kohärenzkern` is the report's word, not the Kohärenz-Kernel.


**Record entries** (one file each):

- **`c2-entropie-sense`**: AEGIS producing coherence from a state of higher entropy (L445), framed as a dissipative structure (L449) — speculative; say which position it sits nearer, deciding nothing.

**Not promoted:** the thirteen Spannungsfelder and their labels, the six speculative architecture principles, the universal protocol architecture, and the borrowed concepts.

**One reader**: every page above and the record entry.

**Chapter readings**: none — the document names no chapter.
