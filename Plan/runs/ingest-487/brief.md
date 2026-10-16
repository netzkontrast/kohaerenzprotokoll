# Brief — readings from document 487 (step 6)

1 document, one reader, one batch: `ingest-487`. Files go to `Plan/runs/ingest-487/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 487 | `the-kohaerenz-protokoll-an-isomorphic-architecture-for-agent` | 2026-01-02 | „the NovelOS white paper“ (an unsigned English white paper, „The Kohärenz Protokoll: An Isomorphic Architecture for Agentic Fiction“) | presents NovelOS, a multi-agent framework for novel-length fiction built as an isomorphism of the story's psychology and physics, with character, location and event schemas; a software proposal that restates the story's premises as its model, no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (202 lines for `the-kohaerenz-protokoll-an-iso`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A software proposal: write „the NovelOS white paper models …“ or „restates …“; its schema lines (beliefs, desires, intentions in first person) are sample data of a character model, never a character's words in the story. Quote the English as written; cut before bold, escaped asterisks, dollar-sign formulas and inner quotes. No gendered pronoun for Kael, Juna or AEGIS — use the names. Never write about the novel's author; the white paper's remarks on authorship are about a writer's role in such a system.

## Pages — document 487, `the-kohaerenz-protokoll-an-isomorphic-architecture-for-agent`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L17, L21, L22, L24, L34, L74. minor (1–4): AEGIS embodies the Coherence Kernel: Existence via Negation, born from an Ontological Horror of the void, an autopoietic system achieving Operational Closure (L21 — describe around the formula and bold); AEGIS's objective but flawed world state against a character's subjective truth (L34); sample intention to resist assimilation by AEGIS (L74 — a schema example).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L24. minor (1–4): AEGIS's Genesis Trauma from the Void in the mapping table (L24); the event schema The Genesis Crisis codifies the foundational trauma connecting the antagonist to the protagonist (L116, L118).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L166. minor (1–4): the orchestrator's filtered perception as the technical implementation of the Kael-Juna/V relation (L166) — Juna stands only in that compound.
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L24, L40, L48, L166, L185. minor (1–4): the character schema System Kael (L40, L48) with its concern Who am I (L54); TSDP as a direct blueprint for System Kael, raising questions of authentic representation (L185); Kael's emerging paraconsistent logic as the end state (L24).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L80. minor (1–4): one sample intention of the System Kael schema: to establish a stable connection via the Moonshine-Link (L80 — a schema example).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L22. minor (1–4): the Collapse Kernel associated with the Nichts Rauschen (Nothingness Noise), a high-entropy Sea of Potentiality eroding AEGIS's boundaries (L22 — describe around the bold).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L66, L78. minor (1–4): sample EP truth: the Risse as portals to an undeniable reality, not errors (L66); sample intention to investigate the Risse (L78) — both schema examples.
- **`tsdp`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `TSDP` alone on L22. minor (1–4): TSDP as a direct blueprint for System Kael (L185); the psychological side of the isomorphism modelled on TSDP (L22).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L195. not read: an occurrence — L195 is complex-systems simulation in general, an application of the framework.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `The Genesis Crisis` (near `genesis`), `Genesis Trauma` (near `genesis`). a reading: The Genesis Crisis event schema, read on genesis.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). an occurrence: the title.
- `logos`: `KW1: Logos-Prime` (near `logos`), `Logos-Prime` (near `logos`). an occurrence: Logos-Prime names KW1, a location schema, not LogOS.
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`). an occurrence: the borrowed theory's name.


**Pages beyond the draft:**
- **`kohaerenz-kernel`** (minor, 1–2): the Coherence Kernel K₁ as the force of order, structure and information preservation, embodied by AEGIS (L21 — the line writes the symbol as a formula; describe it).
- **`kollaps-kernel`** (minor, 1–2): the Collapse Kernel K₀ as entropy, chaos and the Correspondence-Check of external reality, the narrative's ultimate source of objective truth (L22 — describe around the formula).

**Record entries:** none.

**No chapter readings**: the white paper names no chapter.

**Not promoted:** NovelOS, Epistemic Isolation, Environment Loop, the schema field names, Grand Argument Story, Existence via Negation, Operational Closure, Logos-Prime, System Architect, and the borrowed concepts (one carries a person's name).

**One reader**: every page above.
