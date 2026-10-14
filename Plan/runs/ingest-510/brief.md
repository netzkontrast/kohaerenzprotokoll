# Brief — readings from document 510 (step 6)

1 document, one reader, one batch: `ingest-510`. Files go to `Plan/runs/ingest-510/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 510 | `aegis-genesis-krise-prosa-auftrag-formulieren` | 2025-04-29 | „the four-stage Genesis-crisis report“ (an unsigned German planning report) | 40 theory areas, 7 clusters, a strategic prose plan and a final prose commission (L584–L652) for scenes of AEGIS's Genesis-Krise, with no scene itself; it asks that the commission be used as a binding guideline (L671), a claim recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (678 lines for `aegis-genesis-krise-prosa-auft`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A planning report: write „the four-stage Genesis-crisis report plans/reads …“. Its `Eignung/Relevanz` lines apply borrowed theories; the context list (L596–L601) reports given material, marked „[Kontext]“ in part. Theory names after real people stand on many lines (e.g. L351): never write a name, never quote a span containing one or a possessive formed from one. No gendered pronoun for Kael or AEGIS in our own prose.

## Pages — document 510, `aegis-genesis-krise-prosa-auftrag-formulieren`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L17, L21, L30, L36, L45, … (108 lines); `Kontrollinstanz` L434. central (4–8): the Genesis-Krise a fundamental event in AEGIS's ontogenesis, where its core paradox manifests catastrophically (L21); AEGIS's whole system acting like an ANP trying to control the triggered Ursprungs-Ich (EP) (L63); the paradox „Fehlausgerichtete Kohärenz“ as AEGIS's hamartia (L189) and the crux of the crisis (L660); in the context list a highly complex, potentially autopoietic AI defined by negation of the Leere (L596), its paradox also named „Kohärenz durch Entfremdung“ (L599), reading the internal resonance as catastrophic failure and starting the Kohärenz Protokoll as a panic reaction (L601); its thinking shown as a logical but paradoxical cascade, the protocol not as malicious (L541).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L433, L484, L485. minor (1–4): DID as the census lists it (L433, L484, L485 — read one or two).
- **`emergenz`** (central, 3–12 quotations): the census's surfaces — `Emergenz` L67, L71, L224, L229, L406, L424, … (15 lines). minor (1–4): the emergence or self-organisation of a new structure from the fragments (L532); the closing should hint at Kael's emergence (L670); further emergence lines as the census lists them (L67, L71).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L76. not read: an occurrence — entropy in a theory definition (L76).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Julia` alone on L677. not read: an occurrence — a real person's given name in the reference list (L677); Juna does not occur.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L21, L36, L63, L72, L162, … (30 lines). central (4–8): the crisis as the point of origin of the entity Kael (L21); implicit fragments surviving the destruction of the Ursprungs-Ich's narrative self and forming the basis for Kael (L162); whether Kael is the same identity or a successor built from its remains posed as a question (L351 — quote only name-free spans); „Kein fertiger Kael“ (L532), step 7 „Erwachen von Kael“ (L613), the ending only hinting at Kael's emergence (L670).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L612. minor (1–4): step 6, reboot and partitioning of the Ursprungs-Ich, hints at „die Basis für spätere Kernwelten“ (L612).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L17. not read: an occurrence — the paradox and the Protokoll are read on aegis.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L45, L596. minor (1–4): AEGIS defined by negation of the Leere („Nichts Rauschen“) (L596); L45 as the census lists it.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L607. minor (1–4): the opening view from outside, „Leere/Potentialmeer“, AEGIS stable but with latent echoes (L607).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L58, L62, L405, L485, L622. minor (1–4): TSDP applied to the crisis as the census lists it (L58, L62, L405, L485, L622 — read two).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L54. not read: an occurrence — `Simulation` in a theory definition (L54).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). an occurrence: the crisis as AEGIS's, read on aegis.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz Protokolls` (near `koharenz`), `Fehlausgerichtete Kohärenz` (near `koharenz`), `Fehlausgerichteten Kohärenz` (near `koharenz`), `Kohärenz durch Entfremdung` (near `koharenz`), `Kohärenz-Metriken` (near `koharenz`). read on aegis (above).
- `residual-echos`: `Echos` (near `residualechos`). an occurrence: the „latente Echos“ are the report's own term for implicit trauma memories, not the page's residual echoes.


**Record entries** (one file, formatted as earlier entries):
- **`c16-kael-origin`**: the four-stage Genesis-crisis report plans Kael's origin in the crisis (L21), implicit fragments of the Ursprungs-Ich forming the basis for Kael (L162), and only the awakening of a fragmented structure, not a finished Kael (L613); recorded, not applied.

**No chapter readings**: `Kap` 0, `Kapitel` 0.

**Not promoted:** Ursprungs-Ich, Entität, latente Echos, Kernparadoxon, Kohärenz durch Entfremdung, the cluster and stage labels, NZT-Modus, the 7-step trajectory, and the 40 theory areas (several named after people).

**One reader**: every page above and the C16 entry.
