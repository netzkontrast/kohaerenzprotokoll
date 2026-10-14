# Brief — readings from document 472 (step 6)

1 document, one reader, one batch: `ingest-472`. Files go to `Plan/runs/ingest-472/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 472 | `blueprint-for-narrative-coherence` | 2025-10-15 | „the English Chapter 1 draft“ (an unsigned English prose chapter, „The Whisper of Construct City“, L13, with eight references) | Kael notices a flicker of light and a smell of rain in Construct City, which a maintenance drone scrubs away; an explaining voice ties the moments to Kiko, the Foundation, the Moonshine-Link and Juna; a draft, recorded, never canon|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (77 lines for `blueprint-for-narrative-cohere`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A draft chapter: write „the English Chapter 1 draft narrates …“; its explaining voice (L35, L39, L51) is the draft's own gloss. Quote the English as written; cut before italics and straight quotes. No gendered pronoun for Kael, Juna, Kiko or AEGIS — use the names (quotations verbatim). The reference titles (L69–L76) are other texts' words, never read.

## Pages — document 472, `blueprint-for-narrative-coherence`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L39, L51. minor (1–4): the organic patterns as the Foundation's first fingerprints against AEGIS's world (L39); a feeling AEGIS cannot perceive (L51).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L51. minor (1–4): the wave of emotion as a shared quale from an entity named Juna, transmitted across the Moonshine-Link (L51).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L17, L19, L23, L25, L31, L53, … (7 lines). minor (1–4): Kael functions within the perceived normalcy of Kernwelt 1 (L19); Kael's coping read as the survival strategy of the Apparently Normal Part (L35); Kael's own label for the unease, a post-reboot artifact (L35); the chapter ends on a single, coherent doubt (L65).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L39, L51. minor (1–4): the stuttering light as the bleed-through of Kiko, the terrified child-part in a freeze response (L39); the wave of feeling as Kiko, the child alter, activated by a frequency of empathy that AEGIS cannot perceive (L51).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L71. not read: an occurrence — L71 is a reference title.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L51. minor (1–4): „the non-local, acausal bond of the Moonshine-Link“ carrying a shared quale (L51).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L23. minor (1–4): the system defends itself against the pressure of the Nothingness Noise from which it was born, the German Nichts Rauschen beside it (L23).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kern-welten`: `Kernwelt 1` (near `kernwelt`). a reading: `Kernwelt 1` — read on kern-welten (below).
- `logos`: `Logos-Prime` (near `logos`). an occurrence: `Logos-Prime` is the city's name, read on konstrukt-stadt.
- `nexus`: `central nexus` (near `nexus`). an occurrence: `central nexus` is a place in the city, not the Nexus.


**Pages beyond the draft:**
- **`konstrukt-stadt`** (minor, 1–3): the city named Logos-Prime and The Construct City in neighbouring sentences (L21); no weather (L21); a world built on Coherence through Negation (L21) with an aesthetic of Algorithmic Horror (L23); the hum as the first law of physics (L17).
- **`kern-welten`** (minor, 1): Kael's function within the perceived normalcy of Kernwelt 1 (L19).

**Record entries:** none.

**Chapter readings** (batch `ingest-472-kap`, `Plan/runs/ingest-472-kap/readings/kap-01--blueprint-for-narrative-coherence.md`, formatted as the files in `Plan/runs/ingest-466-kap/readings/`): **kap-01** — the English draft „The Whisper of Construct City“ (L13): Kael notices the flickering light and a smell of rain; a maintenance drone scrubs the scent away (L59); the chapter ends on a single coherent doubt (L65).

**Not promoted:** Coherence through Negation, Algorithmic Horror, Nothingness Noise, Logos-Prime as a name, the Foundation, maintenance drone, central nexus, and the borrowed concepts.

**One reader**: every page above and the chapter reading.
