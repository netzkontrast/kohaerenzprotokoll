# Brief — readings from document 506 (step 6)

1 document, one reader, one batch: `ingest-506`. Files go to `Plan/runs/ingest-506/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 506 | `aegis-protokolle-kritische-evaluation-neukonzeption` | 2025-04-19 | „the AEGIS protocol critique“ (an unsigned German report) | an explicitly hypothetical, a-priori critique of AEGIS protocol sketches it does not hold (L15, L17), measured against AEGIS's core philosophy principle by principle, with a synthesis and recommendations; it names no figure of the novel; a critique, no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (289 lines for `aegis-protokolle-kritische-eva`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A hypothetical critique: write „the AEGIS protocol critique states/argues …“; what it says of the sketches is conjecture by its own account (L17). The sketch acronyms (AFP v1.4, ZTEM, RTSV, SVI, …) are named, not explained. Never write a person's name or quote a span containing one (several lines name scientists or concepts after them — cut before). No gendered pronoun for AEGIS in our own prose.

## Pages — document 506, `aegis-protokolle-kritische-evaluation-neukonzeption`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L15, L21, L29, L32, L33, … (42 lines). central (4–8): AEGIS's core philosophy as the critique's measure: „AEGIS postuliert Kohärenz als Existenzbedingung“ (L33); inconsistency must lead to non-existence or non-integration (L79); the founding problem as P-INIT in disguise (L105); AEGIS demanding a purely internal perspective (L137) and robustness as an emergent property of the coherent system (L138); the principles discussed — P-INIT (L40), P-ENTROPY (L50), Ontologische Exklusion (L60), Funktionale Ontologie (L108), Operative Geschlossenheit (L116), Entropisches Gatekeeping (L124).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `SIS` alone on L15. not read: an occurrence — `SIS` is one acronym in an unexplained list of protocol sketches (L15).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L34. not read: an occurrence — emergence in a general remark on redundancy (L34).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L56. minor (1–4): AEGIS might need a non-standard, purely informational definition of entropy and a re-evaluation of operational closure (L56 — quote only a name-free span).
- **`kael`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Michael` alone on L217. not read: an occurrence — a real person's given name in a reference-list entry (L217); never written.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L31. minor (1–4): coherence as AEGIS's condition of existence (L33); the critique's concern that the sketches define „Kohärenz“ inconsistently — structurally, functionally or relationally (L31).
- **`negentropie`** (minor, 1–4): the census's surfaces — `Negentropie` L128. minor (1–4): models of disorder may assume an external source of order (Negentropie) or an external sink for entropy, contradicting operational closure and P-ENTROPY (L128 — cut before the named analogy).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L209. not read: an occurrence — `Simulation` in a reference title (L209).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `emergenz`: `Emergenz durch Negation` (near `emergenz`). an occurrence: `Emergenz durch Negation` named as an AEGIS principle, read on aegis.
- `kohaerenz`: `Kohärenz als Existenzbedingung` (near `koharenz`). read on kohaerenz (above): `Kohärenz als Existenzbedingung` (L33).


**Record entries:** none.

**No chapter readings**: `Kap` 0.

**Not promoted:** the protocol-sketch acronyms (AFP v1.4, ZTEM, RTSV, SVI, …), the principle labels P-INIT and P-ENTROPY, BFT, the label pair Kritikpunkt/Wissenschaftlicher Kontext, and the borrowed concepts (several named after people).

**One reader**: aegis, kohaerenz, entropie, negentropie.
