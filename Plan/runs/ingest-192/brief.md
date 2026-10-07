# Brief — readings from document 192 (step 6)

1 document, one reader, one batch: `ingest-192`. Files go to `Plan/runs/ingest-192/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 192 | `recherche-ueberwelt` | 2025-04-17 | „the Überwelt commission“ (titled `Recherche- und Konzeptentwicklungsauftrag: Gestaltung einer Digitalen Überwelt`) | a German research commission — a prompt: it supplies the AEGIS Functional Protocol v1.4 and five Guardian descriptions as given context (L15–L79), asks questions in five tasks it does not answer (L81–L180), and closes with an `Erweiterter Kontext` on the Überwelt's narrative role (L184–L197) — light pass: readings only from that closing passage |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (198 lines for `recherche-ueberwelt`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** **Light pass.** A prompt: the protocol text and the Guardian descriptions stand in earlier read documents (the Zero-Trust Execution Model in 19 landed documents, among them 111, 141, 148, 154, 190), and the tasks are questions — read neither. Read only L184–L197, the commission's account of the Überwelt's role in the novel, as „the Überwelt commission describes …“. It names the protagonist `Michael` and the partner `Julia`, read on kael and juna. German — quote as written; cut before inner straight quotes („Risse“, „Himmel“ stand in them).

## Pages — document 192, `recherche-ueberwelt`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L17, L19, L21, L22, L32, … (28 lines). not read: light pass — the document is a prompt; its lines here are given context or questions.
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Integrity Guardian` L36, L86; `Cognitive Firewall` L37, L86, L125; `SIS` L53, L125, L143. not read: light pass — the document is a prompt; its lines here are given context or questions.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L77, L85, L134, L188. not read: light pass — the document is a prompt; its lines here are given context or questions.
- **`did`** (minor, 1–4): the census's surfaces — `DID` L188. not read: light pass — the document is a prompt; its lines here are given context or questions.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L78. not read: light pass — the document is a prompt; its lines here are given context or questions.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L195. minor (1–2): the fundamental counterpart of the Überwelt, associated with Julia, emotion and connection (L195).
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L13, L71, L85, L86, L107, L115, … (14 lines). minor (1–2): the Überwelt as „die primäre Realitätsebene der Guardians“, from which they watch the four Kern-Welten (L188); their reactions, despair or discord in part 3 (L194).
- **`juna`** (minor, 1–4): the census's surfaces — `Julia` L188, L194, L195, L197. minor (1–2): `Julia`: the Externe Ebene „die mit Julia assoziiert ist“ (L195).
- **`kael`** (minor, 1–4): the census's surfaces — `Michael` L188, L192, L193, L194, L197. minor (1–2): `Michael` (C17): his (perhaps unintended) entry into the Überwelt at the end of part 1 (L192); his confrontation with the Guardians and his flawed mission, the „Suche nach der Realität“, in part 2 (L193) — cut before inner quotes; he acts in the Kern-Welten in part 3 (L194).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L78, L134, L188. not read: light pass — the document is a prompt; its lines here are given context or questions.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kern-Welten` L152, L188, L194. not read: light pass — the document is a prompt; its lines here are given context or questions.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L53. not read: light pass — the document is a prompt; its lines here are given context or questions.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L75, L85, L115, L134, L188. not read: light pass — the document is a prompt; its lines here are given context or questions.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L76, L115, L134, L188. not read: light pass — the document is a prompt; its lines here are given context or questions.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L188. not read: light pass — the document is a prompt; its lines here are given context or questions.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L139, L143, L170, L192. minor (1–2): Risse appearing in the Überwelt too at the end of part 1 (L192) — quote around the inner quotes.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L79, L134, L188. not read: light pass — the document is a prompt; its lines here are given context or questions.
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L11, L13, L17, L73, L97, L99, … (22 lines). central (2–4): „Die“ Überwelt as far more than another setting (L186) — cut before the inner quotes; the Guardians' primary level of reality from which they watch the four Kern-Welten (L188); the manifestation of the system's paradigm and its limits (L189); a catalyst of plot turns in parts 1–3 (L192–L194); the counterpoint to the Externe Ebene (L195).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz-programm`: `Programm` (near `kohaerenzprogramm`), `Programm` (near `koharenzprogramm`). occurrence: `Programm` is a generic word, not the Kohärenz-Programm.


**Record entries** (one file):

- **`q6-nexus-ueberraum-ueberwelt`**: the Überwelt as the Guardians' primary level of reality and the system's manifestation, set against the Externe Ebene (L188, L189, L195).

**Not promoted:** the protocol's labels (ZTEM, RTSV, BPoF, EIC, SVI, LCA, RIK, DRI), the tasks and the requested output structure.

**One reader**: ueberwelt, guardians, kael, juna, externe-ebene, risse and the record q6.
