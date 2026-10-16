# Brief — readings from document 256 (step 6)

1 document, one reader, one batch: `ingest-256`. Files go to `Plan/runs/ingest-256/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 256 | `kohaerenz-protokoll-kapitel-39-die-letzte-instanz` | 2026-02-25 | „the chapter-39 draft“ (unsigned German prose) | „Kapitel 39: Die letzte Instanz“: a short chapter in the second person in which Kael and AEGIS break the fourth wall and a boxed system report (PMAS) hands the Protokoll to the reader; a draft, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (66 lines for `kohaerenz-protokoll-kapitel-39`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Prose: write „in the chapter-39 draft …“; name the voice (narration in the second person, Kael's speech, AEGIS's speech in capitals, the PMAS report). The „du“ is the narrative's reader inside the fiction, not the author. Chapter pages are written by the session (`Plan/runs/ingest-256-kap/`). Cut quotations before inner quotes and emphasis marks.

## Pages — document 256, `kohaerenz-protokoll-kapitel-39-die-letzte-instanz`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L19. minor (1–2): whispering „SYSTEMFEHLER“, its voice no longer from the Nexus: the observer instance has entered the system, coherence can no longer be held purely internal (L19).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L17. minor (1–2): the Guardians' despair become the reader's cognitive effort to hold the story together (L17).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L21. minor (1–2): Kael looks not at Juna but out of the text (L21).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L15, L21, L41, L53, L57, L59. minor (1–2): no longer „da drüben“ (L15); looking out of the text at the reader (L21); „Ich bin nicht die Simulation eines Mannes mit DIS“, the externalisation of the reader's own search for wholeness (L27); the reader as the instance woken from his ruins (L59).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kern-Welt` L27. minor (1–2): in Kael's speech, L27, only if a `Kern-Welt` line adds.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — `KOHÄRENZ` L19, L37, L65. minor (1–2): the PMAS report: „ZIELKOHÄRENZ ÜBERTRAGEN“ (L37) and „ZIELKOHÄRENZ ERREICHT“ (L65); AEGIS's coherence no longer held purely internal (L19).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L17. minor (1–2): its geometry collapsed into a two-dimensional surface (L17).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L17. minor (1–2): the monumental halls of LogOS only ink and light pixels (L17).
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L45. minor (1–2): the PMAS report: the „Mosaik-Herz“ now beats in the reader's chest (L45).
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L19, L29. minor (1–2): AEGIS's voice no longer from the Nexus (L19); the light in the Nexus goes out and becomes real (L29).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Nichts-Rauschen` alone on L55. minor (1–2): the reader's room a set built to cover the Nichts-Rauschen of reality (L55).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Simulation` L13, L27, L45. not read: occurrence — `Simulation` names the novel itself („Die Simulation „Roman““, L45) and the simulation's speakers (L13), not the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie-resonanz`: `Protokoll` (near `entropieresonanzentropieresonanzprotokolleerp`), `Protokoll` (near `entropieresonanzprotokolle`). occurrence: `Protokoll` is the Kohärenz Protokoll the reader runs, not this page.
- `mnemosyne-server-architektur`: `Architekt` (near `mnemosyneserverarchitektur`). occurrence: `Architekt` is the reader (L27, L33).
- `nichts-rauschen`: `Rauschen` (near `nichtsrauschen`). occurrence: `Rauschen` is the noise everywhere (L13, L49); `Nichts-Rauschen` read on nichts-rauschen (L55).
- `nullpunkt-protokoll`: `Protokoll` (near `nullpunktprotokoll`). occurrence: `Protokoll` is the Kohärenz Protokoll the reader runs, not this page.
- `personas`: `Instanz` (near `bewusstseinsinstanzen`). occurrence: `Instanz` is the reader as instance and AEGIS's observer instance, not the Personas.
- `protokoll-v14`: `Protokoll` (near `protokollv14`). occurrence: `Protokoll` is the Kohärenz Protokoll the reader runs, not this page.
- `trennungsprotokoll`: `Protokoll` (near `trennungsprotokoll`). occurrence: `Protokoll` is the Kohärenz Protokoll the reader runs, not this page.


**Record entries** (one file each):

- **`c13-externe-ebene-beyond-the-simulation`**: the PMAS report: the simulation „Roman“ ended, „Die externe Ebene – deine Ebene –“ now the active test field for the Kohärenz Protokoll (L45) — the reader's level as the external one.

**Not promoted:** PMAS, the Beobachter-Instanz, Instanz, ZIELKOHÄRENZ.

**One reader**: kael, aegis, juna, guardians, konstrukt-stadt, logos, nexus, kohaerenz, mosaik-herz, nichts-rauschen, kern-welten and the record c13. `ueberwelt` is an occurrence.

**Chapter readings**: Kap 39, by the session (`Plan/runs/ingest-256-kap/`).
