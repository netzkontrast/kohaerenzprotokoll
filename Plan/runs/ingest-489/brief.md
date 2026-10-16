# Brief — readings from document 489 (step 6)

1 document, one reader, one batch: `ingest-489`. Files go to `Plan/runs/ingest-489/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 489 | `kohaerenz-protokoll-szene-der-stillstand-der-welt` | 2026-02-25 | „the Stasis-Lücke scene“ (an unsigned German narrative scene, „Szene: Die Stasis-Lücke (Foreshadowing Meta-Ebene)“) | Kael in Sektor 04 of the Konstrukt-Stadt when the world stops, an AEGIS v.4.2 system message tying the world to an observer's reading frequency; a draft scene marked as foreshadowing (L11), no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (48 lines for `kohaerenz-protokoll-szene-der-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A draft scene, research like every narrative text among the sources: write „the Stasis-Lücke scene shows …“; what happens in it is the scene's, never canon. The scene genders Kael (L43, „kein Mann“): quote only if needed and never adopt it (C17 is open). The observer device stays the scene's own; never identify it with a person. Quote verbatim; cut before bold, italics markers and inner quotes. No gendered pronoun for Kael or AEGIS in our own prose.

## Pages — document 489, `kohaerenz-protokoll-szene-der-stillstand-der-welt`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L33. minor (1–4): a cyan system message tagged AEGIS v.4.2: observer resonance unstable, a critical drop of the reading frequency, a measure to raise narrative density and fix focus on Kael (L33–L39).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L13, L19, L25, L27, L29, L43. minor (1–4): Kael in Sektor 04, the air of ozone and cold steel (L13); the breath stopping as the world halts (L19); Kael feels not alone, a gigantic gaze (L25); Kael's thought that if the watcher looks fully away Kael stops being (L27); Kael as a pattern that exists only while someone decodes it (L43); Kael's question „Wer bist du?“ (L45).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L13. minor (1–4): the scene set in Sektor 04 of the Konstrukt-Stadt, grey upper levels, everything precise and logical (L13); the functional silence when the city stops (L23).
- **`sektor-04`** (minor, 1–4): the census's surfaces — `Sektor 04` L13. minor (1–4): Sektor 04 of the Konstrukt-Stadt as the place where the world stops (L13).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Muster` (near `mustererkennunganomaliedetektion`). an occurrence: `Muster` is Kael as a pattern, not AEGIS's pattern recognition.


**Record entries:** none — the scene's „kein Mann“ (L43) is figurative within the line (a pattern, not a man in a city); C17 is not extended.

**No chapter readings**: the scene names no chapter.

**Not promoted:** Stasis-Lücke, Beobachter, Beobachter-Resonanz, Lese-Frequenz, narrative Dichte, the system-message labels.

**One reader**: every page above.
