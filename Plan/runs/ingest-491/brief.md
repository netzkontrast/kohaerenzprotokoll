# Brief — readings from document 491 (step 6)

1 document, one reader, one batch: `ingest-491`. Files go to `Plan/runs/ingest-491/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 491 | `kohaerenz-protokoll-outline-revision-pacing-2026-05-01-md` | 2026-04-30 | „the pacing revision“ (an unsigned German memo, „Kohärenz Protokoll — 39-Kapitel-Outline (Revision Pacing 2026-05-01)“) | lists four structural changes to a 39-chapter outline: POV alternation per chapter (withdrawn by a correction note, L19), a multiplicity veil until Kap 13, Juna seeding from Kap 1, functional multiplicity moved to Kap 33; it says its base contents stay valid (L27), recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (33 lines for `kohaerenz-protokoll-outline-re`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A revision memo: write „the pacing revision moves …“ or „plans …“; never canon. L19 is a correction note naming a person's role — never quote L19 and never write who made it; describe it as „a correction note dated 2026-05-01 (L19)“ that withdraws the per-chapter alternation and asks for both storyforms in each chapter. The lines carry escaped asterisks (\*\*): cut before them. No gendered pronoun for Kael, Juna or AEGIS in our own prose.

## Pages — document 491, `kohaerenz-protokoll-outline-revision-pacing-2026-05-01-md`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L17, L21. minor (1–4): even chapters planned as Storyform B POV with AEGIS, Guardians and system telemetry (L17), withdrawn by the correction note (L19); AEGIS has the system terms, Kael does not (L21).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L17. minor (1–4): even chapters planned as Storyform B POV, among them the Guardians (L17), withdrawn by the correction note (L19).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L17, L23, L25, L27. minor (1–4): odd chapters Juna-near (L17); Juna seeding from Kap 1: a word without referent, a balance anomaly in Kap 2, single phenomena in Kap 3, 5, 7, manifesting first in Kap 7 as a resonance break in the shrine (L23); Kap 33 an encounter with Juna in the garden, functional multiplicity carried by Juna's Witness function (L25).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L17, L21. minor (1–4): odd chapters Storyform A POV with Kael (L17); until Kapitel 13 Kael is not marked as a system and the system terms do not fall, instead modes, echoes, drifts, gaps (L21); only in Kap 13 the curtain falls (L21).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the title.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L25. minor (1–4): functional multiplicity moved to Kap 33, after a first mosaic intimation in Kap 11, tactical polyphony in Kap 23, practised dialetheism in Kap 27; Kap 33 the state in which all 13 are present and cooperative at once (L25).
- **`telefon-stille`** (minor, 1–4): the census's surfaces — `Telefon-Stille` L23. minor (1–4): Telefon-Stille as one of the single phenomena of Juna seeding in Kap 3, 5, 7 (L23 — the line does not say which chapter).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L21. minor (1–4): TSDP among the terms that do not fall before Kapitel 13 (L21).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alters`: `Alter` (near `alters`), `Alter-Surface-Timeline` (near `alters`). a reading: `Alter` among the system terms withheld until Kapitel 13 (L21); the Alter-Surface-Timeline stays valid (L27) — read on alters.
- `did`: `Fragment` (near `psychischefragmentierung`). an occurrence: `Fragment` among the withheld terms, not the page's term.
- `garten-der-stillen-praesenz`: `Garten` (near `gartenderstillenpraesenz`), `Garten` (near `gartenderstillenprasenz`). an occurrence: the memo says only „im Garten“ (L25), which garden is not said.
- `moeglichkeits-garten`: `Garten` (near `moeglichkeitsgarten`), `Garten` (near `moglichkeitsgarten`). an occurrence: the memo says only „im Garten“ (L25), which garden is not said.
- `residual-echos`: `Echos` (near `residualechos`). an occurrence: `Echos` as one of the substitute words (L21).
- `vergessener-schrein`: `Schrein` (near `vergessenerschrein`), `Schrein` (near `vergessenerschreintraumalokus`). an occurrence: the memo says only „im Schrein“ (L23), which shrine is not said.


**Pages beyond the draft:**
- **`alters`** (minor, 1–2): `Alter` among the system terms withheld until Kapitel 13 (L21); Kap 33: all 13 present and cooperative at once (L25 — the line does not say what the 13 are).

**Record entries:** none.

**Chapter readings** (batch `ingest-491-kap`, `Plan/runs/ingest-491-kap/readings/kap-NN--kohaerenz-protokoll-outline-revision-pacing-2026-05-01-md.md`, formatted as the files in `Plan/runs/ingest-490-kap/readings/`), each the revision's plan, never canon:
- **kap-01**: Juna seeding begins, a word without referent (L23).
- **kap-02**: a balance anomaly (L23).
- **kap-03**, **kap-05**, **kap-07**: one single phenomenon each, from anomalous temperature, slowly falling dust, telephone silence — the line does not assign them (L23).
- **kap-07**: also Juna manifests first as a resonance break in the shrine (L23).
- **kap-11**: a first mosaic intimation (L25).
- **kap-13**: until Kapitel 13 Kael is not marked as a system; in Kap 13 the curtain falls (L21).
- **kap-23**: tactical polyphony (L25).
- **kap-27**: practised dialetheism (L25).
- **kap-33**: middle of Act III, encounter with Juna in the garden, all 13 present and cooperative at once, carried by Juna's Witness function (L25).
The odd/even POV rule (L17) is withdrawn by the correction note (L19): no chapter reading for it.

**Not promoted:** POV-Alternation, Multiplizitäts-Schleier, Juna seeding, Bilanz-Anomalie, Mosaik-Ahnung, taktische Polyphonie, praktizierter Dialetheismus, Dual-POV, Alter-Surface-Timeline, Juna-Seeding-Layer, Pacing-Profil.

**Two readers**: one for every page above; one for the chapter readings.
