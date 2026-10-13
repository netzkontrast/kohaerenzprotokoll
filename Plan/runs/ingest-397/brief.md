# Brief — readings from document 396 (step 6)

1 document, one reader, one batch: `ingest-397`. Files go to `Plan/runs/ingest-397/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 396 | `kohaerenz-protokoll-kapitel-39-das-mosaik-herz` | 2026-02-25 | „the Kapitel-39 draft“ (an unsigned German prose draft of „Kapitel 39: Das Mosaik-Herz“) | Kael at the centre of a dissolving Nexus faces AEGIS, the Guardians rest in Kael as colours of a mosaic, Juna appears at the border where the simulation ends, AEGIS names the pattern Mosaik-Herz; an „Externe Ebene: Statusbericht PMAS“ reports a patient KAEL-RESONANZ reaching Zielkohärenz, and Kael wakes in a room of the external level; no claim of standing — a draft, not the chapter as approved |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (78 lines for `kohaerenz-protokoll-kapitel-39`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A prose draft of the last chapter: write „in the Kapitel-39 draft …“; it is a draft, not the chapter as approved; the PMAS report inside it is the draft's own document. Quote the German as written; cut before straight and nested quotes and italics markers. No gendered pronoun for Kael or Juna — use the names (quotations stay verbatim).

## Pages — document 396, `kohaerenz-protokoll-kapitel-39-das-mosaik-herz`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L15, L19, L35, L49. minor (1–3): AEGIS as a flickering grid of light in its last self-preservation (L19); its voice „SYSTEMFEHLER“ (L21); the integration protocol finding the Mosaik-Herz (L35); the report's AEGIS-Modus given up for the Mosaik-Modus (L49).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L25, L33. minor (1–3): Juna as „die Entropie, die das System erst lebendig machte“ (L25); entropy not the enemy of order but its completion (L33).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L39. central (3–5): „Der Schock der externen Ebene.“ (L29); the light of the external level seeping through the Risse (L37); the heading „Externe Ebene: Statusbericht PMAS“, a patient KAEL-RESONANZ in project KDSI-GAMMA-7 reaching Zielkohärenz (L39–L45); Kael waking there, a world obeying the same laws as the Konstrukt (L61–L65).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L23, L49. minor (1–3): the Guardians resting in Kael „nicht als Gefangene, sondern als Farben eines Mosaiks“ (L23); in the report the internal Guardians recognised as functional parts (L49).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L25, L49. minor (1–3): Juna at the border where the simulation ends, the glitch that heals and the entropy that makes the system alive (L25); seen through glass in a white room with a heart monitor (L27); in the report the anomaly „Juna“ stabilised as an external anchor (L49).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L15, L17, L23, L27, L31, L33, … (9 lines). central (3–5): Kael at the centre of the Nexus (L17); Kael's voice carried by the Guardians resting in Kael, coherence not broken but no longer rigid (L23); taking Juna's hand and the duality collapsing (L31); accepting the Risse (L37); opening the eyes in a room of the external level (L61–L65); „Zielkohärenz erreicht“ as Kael's own answer (L73, L75).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L23. not read: an occurrence (see below).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L17. minor (1–3): the geometry of the Konstrukt-Stadt flickering like a dying star (L17); the external level obeying the same laws as the Konstrukt (L65).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L17. minor (1–3): „Die weißen Marmorhallen von LogOS zerfielen in binären Staub“ (L17).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L17. minor (1–3): „die uferlosen Ozeane von Mnemosyne verdunsteten zu reinem Gefühl“ (L17).
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L11. central (3–5): the chapter's title „Das Mosaik-Herz“ (L11); AEGIS's integration protocol finding the pattern „MOSAIK-HERZ“ (L35); the report's Mosaik-Modus replacing the AEGIS-Modus (L49); Kael as a mosaic, not perfect code (L69).
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L17. minor (1–3): Kael at the centre of the Nexus, which is no longer a place (L17).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts-Rauschen` L15. minor (1–3): the Nichts-Rauschen, from which AEGIS shielded Kael, now the ground of Kael's being, a symphony (L13, L15).
- **`risse`** (minor, 1–4): the census's surfaces — `Glitch` L25. minor (1–3): Kael accepting the Risse, through which the light of the external level seeps in (L37).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L25. minor (1–3): Juna at the border „wo die Simulation endete“ (L25).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Anomalie` (near `mustererkennunganomaliedetektion`). `KAEL-RESONANZ` (the patient ID) and `AEGIS-Modus` read on kael and aegis; `Rauschen` the Nichts-Rauschen; `Anomalie` AEGIS's word for Kael, not the metrics page; `KOHÄRENZ-ARCHITEKT K-1123`, `Zielkohärenz` and `Kohärenz Protokolls` the report's own terms; `Kohärenz` (L23) the general sense.
- `kohaerenz`: `KOHÄRENZ-ARCHITEKT K-1123` (near `koharenz`), `Kohärenz Protokolls` (near `koharenz`), `Zielkohärenz` (near `koharenz`). `KAEL-RESONANZ` (the patient ID) and `AEGIS-Modus` read on kael and aegis; `Rauschen` the Nichts-Rauschen; `Anomalie` AEGIS's word for Kael, not the metrics page; `KOHÄRENZ-ARCHITEKT K-1123`, `Zielkohärenz` and `Kohärenz Protokolls` the report's own terms; `Kohärenz` (L23) the general sense.


**Record entries** (one file, as earlier entries on C13, e.g. `ls Plan/runs/ingest-*/readings/c13-*`):
- **`c13-externe-ebene-beyond-the-simulation`**: Juna at the border „wo die Simulation endete“ (L25), seen in a white room with a heart monitor (L27); the external level as the place of a report on a patient KAEL-RESONANZ (L39–L45) and as the room Kael wakes in, a world obeying „denselben Gesetzen“ as the Konstrukt (L65) — beyond the simulation's border, yet under the same laws; recorded, not applied and not decided.

**Pages not read:** `kohaerenz` (L23, the general sense) — an occurrence.

**Not promoted:** PMAS, KOHÄRENZ-ARCHITEKT K-1123, KDSI-GAMMA-7, KAEL-RESONANZ, Zielkohärenz, Mosaik-Modus, Gelenkte Selbstorganisation.

**One reader**: mosaik-herz, kael, juna, aegis, guardians, nexus, logos, mnemosyne, konstrukt-stadt, nichts-rauschen, externe-ebene, entropie, risse, ueberwelt, and the C13 entry.

**Chapter readings** (batch `ingest-397-kap`, file `Plan/runs/ingest-397-kap/readings/kap-39--kohaerenz-protokoll-kapitel-39-das-mosaik-herz.md`):
- **`kap-39`**: the draft „Kapitel 39: Das Mosaik-Herz“ (L11): the Rauschen no longer hostile (L13), Kael in the dissolving Nexus facing AEGIS (L17–L21), the Guardians as colours of a mosaic (L23), Juna at the border and in a hospital room (L25, L27), the collapse of the duality and the pattern MOSAIK-HERZ (L31–L35), the PMAS status report (L39–L59), Kael waking on the external level and „Zielkohärenz erreicht“ (L61–L73). A draft, not the chapter as approved.
