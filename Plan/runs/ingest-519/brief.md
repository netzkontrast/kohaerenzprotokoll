# Brief — readings from document 519 (step 6)

1 document, one reader, one batch: `ingest-519`. Files go to `Plan/runs/ingest-519/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 519 | `projekt-ockham-narrative-systemik-reduktion` | 2026-01-02 | „the NovelOS 2.0 report“ (an unsigned German technical report) | moves a fiction-writing multi-agent system from one director agent to isolated agents, built on a two-kernel theory, a knowledge graph, YAML schemas and a checking agent; section 7.0 (L301–L318) uses the novel as the system's stress test; a technical report, no canon claim beyond saying its appendix comes from unnamed „Golden Source“ documents (L330)|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (445 lines for `projekt-ockham-narrative-syste`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A technical report: write „the NovelOS 2.0 report casts/maps …“; outside section 7.0, Kael and Juna appear only as sample data — say so („in sample data“). The project's name carries a person's name: never write it, never quote a span containing it (e.g. L303) or a philosopher's name (L37, L40), and never write the named gambit (L314 — quote only the paradox sentence). No gendered pronoun for Kael, Juna or AEGIS in our own prose; quotations stay verbatim (the document writes „Er“).

## Pages — document 519, `projekt-ockham-narrative-systemik-reduktion`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L154, L305, L309, L314, L317. minor (1–4): in the case study a KI-Gott enforcing rigid logic, Kael's opponent (L305); mapped to the first kernel, classical logic, unable to process paradoxes, and to the Librarian and Hard Canon (L309); in the simulated climax the AEGIS agent crashing on the paradox, the defeat following from the world's rules (L317, L318).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L305. minor (1–4): Kael as „ein fragmentiertes System von Identitäten (Alters)“ (L305).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L33, L35; `Dual-Kernel-Theorie (DKT)` L33, L35. minor (1–4): the Dual-Kernel-Theorie as the central ordering principle of the software, not only a literary theme of the novel (L35).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L17. not read: an occurrence — a general use in the introduction (L17).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L314. not read: the page's term carries a person's name; under the project's privacy rule no reading is written onto it from this document.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L79, L127, L155, L167, L276. minor (1–4): only in sample data: a second spawned character agent (L79); Kael's sample belief „Juna ist eine Verbündete.“, marked as a possibly false belief (L155), and the consistency rule drawn from it (L167).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L79, L84, L90, L97, L98, L126, … (19 lines). central (4–8): in the case study the protagonist, „ein fragmentiertes System von Identitäten (Alters)“ fighting a KI-Gott (L305); mapped to the second kernel, paraconsistent logic, able to hold contradictory truths, and to the Sensory Drafter and Soft Canon (L310); in the simulated climax presenting the paradox „Ich bin eins und ich bin viele.“ (L314 — quote only that); in sample data a desire „Finde die Naht in der Welt.“ (L157), a belief „Realität ist ein Konstrukt von AEGIS.“ (L154), and the archetype label „Protagonist / Broken Mirror“ (L344).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L17. not read: an occurrence — the novel's title and a theory of truth.
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L37. minor (1–4): L37 as the census lists it — the first kernel's role; quote only a name-free span.
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L38. minor (1–4): L38 as the census lists it — the second kernel's role; quote only a name-free span.
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Persona` alone on L80. not read: an occurrence — an agent persona in the software (L80).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L46. minor (1–4): the source narrative: a protagonist with a dissociative identity structure modelled after TSDP (L46).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L29. not read: an occurrence — `Simulation` in a general sense (L29).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie`: `Narrative Entropie` (near `entropie`). an occurrence: `Narrative Entropie` in a general use.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenztheorie der Wahrheit` (near `koharenz`). an occurrence: the title and a theory of truth.
- `mnemosyne-server-architektur`: `Architekt` (near `mnemosyneserverarchitektur`). an occurrence: `Architekt` is a software role.
- `rsa`: `AutoGen` (near `rsarekursivesemantischeautogenese`). an occurrence: `AutoGen` is a software framework.


**Record entries** (one file, formatted as earlier entries):
- **`q8-aegis-after-the-vortex`**: the NovelOS 2.0 report simulates the climax as the AEGIS agent crashing on Kael's paradox, the defeat following deterministically from the world's rules (L317, L318); a software stress test, recorded, not applied.

**No chapter readings**: `Kapitel` stands only in examples (L29, L211).

**Not promoted:** NovelOS, ARCHON, the Coherence Loop, the Librarian, the Sensory Drafter, Hard/Soft Canon, the YAML schemas, BDI-Modell, Shadow Git, Aktives Vergessen, the Golden Source, and the concepts named after people.

**One reader**: every page above and the Q8 entry.
