# Brief — readings from document 527 (step 6)

1 document, one reader, one batch: `ingest-527`. Files go to `Plan/runs/ingest-527/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 527 | `kohaerenz-protokoll-system-realitaet-leser` | 2026-04-26 | „the isomorphic analysis“ (an unsigned German analysis) | maps the novel onto the DKT, an AI agent architecture, Dramatica and TSDP; it writes `Aegis` mixed-case, names no other figure, and claims the line between literary simulation and psychological reality has been torn down (L142), a claim recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (192 lines for `kohaerenz-protokoll-system-rea`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An outside analysis: write „the isomorphic analysis maps/reads …“; its mappings onto an AI architecture and a clinical framework are its own, never the novel's facts. Section 7 (L107–L122) and the reference list (L154–L191) are not read. The document's prose uses „er“ for Aegis (L43, L49, L70, L82): cut quotations before the pronoun, and use none in our own prose. Never write a real person's name or a concept named after a person (L13 and others: cut before).

## Pages — document 527, `kohaerenz-protokoll-system-realitaet-leser`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `Aegis` L27, L43, L45, L47, L49, L51, … (20 lines). central (3–8): the antagonist as the instance of the agency system's prefrontal cortex and amygdala (L43); „Aegis ist nicht einfach nur ein Bösewicht“ (L43, cut before the pronoun); fighting to erase every trace of the nichts Rauschen (L43, L45); a deeply tragic protagonist (L49); fighting „ausschließlich für den Erhalt der Zeugenfunktion“ (L49); „Aegis (Tragischer Protagonist)“ in the table (L58); the drive for structure, misreading the Inequity as an external error (L70); the over-controlling ANP isolating the noise as EP (L82, L84); suspended when the app closes (L148).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L17, L21, L23, L49, L56, L68, … (8 lines). minor (1–4): the physics of the universe read through the DKT (L17): K₁ as the „lesbare Dateisystem“ of reality (L19), erasure as a file transfer from K₁ to K₀ (L21), consciousness as the file reader or witness function of K₁ (L23).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L19. minor (1–4): L19 as the sweep found it, and L49: entropy cannot be destroyed, only shifted — read only the name-free span, if it fits; otherwise an occurrence.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title (L11).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `nichts Rauschen` L43, L45, L51, L70, L82, L118, … (8 lines). minor (1–4): `nichts Rauschen` as the narrative world's counterpart of K₀ in the table (L58); what Aegis fights to erase (L43, L45); the traumatic core, isolated as EP (L82, L84); the Inequity Aegis misreads (L70); fading in RAM when the app closes (L148).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L72, L74, L82, L90, L103, L130, … (7 lines). minor (1–4): the clinical framework the novel is said to use (L72, L74); the agency system as an artificial form of TSDP, Aegis the ANP, the noise the EP (L82, L84); one strand of the system the document calls hermetically closed (L130).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L13. not read: an occurrence — `Simulation` as „literarischer Simulation“ (L13), not the page's term.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz-Protokoll` (near `koharenz`), `Quantendekohärenz` (near `koharenz`). an occurrence: `Kohärenz-Protokoll` the title; `Quantendekohärenz` physics, not the page's term.
- `kohaerenz-kernel`: `Kernel` (near `kohaerenzkernel`), `Kernel` (near `koharenzkernel`), `Kernel` (near `koharenzkernelk1`). an occurrence: `Kernel` alone is generic; K₁ is read on dkt.
- `kollaps-kernel`: `Kernel` (near `kollapskernel`), `Kernel` (near `kollapskernelk0`). an occurrence: `Kernel` alone is generic; K₀ is read on dkt.


**Record entries:** none.

**No chapter readings**: no chapter is named (`Kap`, `Kapitel` 0).

**Not promoted:** the AI agent architecture and its brain-region modules, the Dramatica and TSDP vocabulary as surfaces, Aegis Cortex, Selbst-Löschung, the witness function as a surface, the app framing, the concepts named after people, Section 7 and the reference list.

**One reader**: every page above.
