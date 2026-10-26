# Brief — readings from document 548 (step 6)

1 document, one reader, one batch: `ingest-548`. Files go to `Plan/runs/ingest-548/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 548 | `ergaenze-aegis-protokoll-und-selbstrekusive-defini` | 2025-04-17 | „the opening-chapter brief“ | a commissioning brief for an opening chapter that runs from a reflection on emptiness to AEGIS's universal reboot, with a context summary of AEGIS, an AEGIS protocol v1.4 and a recursive self-definition as input; no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (143 lines for `ergaenze-aegis-protokoll-und-s`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A brief: write „the opening-chapter brief describes …“; never canon. **Never cite L27** (earlier names) **nor L51–L94** (the protocol text, which uses clinical vocabulary about identity systems). Do not quote the flattened formula (L99).

## Pages — document 548, `ergaenze-aegis-protokoll-und-selbstrekusive-defini`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L26, L31, L35, L46, L50, … (23 lines); `Entropic Gatekeeper` L35, L55, L112, L129. central: the opening's Part 4: AEGIS registers „nicht-lokale Nicht-Existenz“ and initiates a universal reboot (L26); the name's expansion (L35); a non-anthropomorphic control core, perceptible only indirectly (L36); regulates the passage from order to disorder (L37); potentially blind to useful complexity (L38); the self-definition (L98, L100, L102, L103).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Integrity Guardian` L70; `Cognitive Firewall` L71; `SIS` L87. not read: its surfaces stand only in the protocol text L51–L94, which is not cited.
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L37, L38, L42, L46, L129. minor: AEGIS regulates the passage to disorder („**Entropie**“) (L37); may misread useful complexity as dangerous entropy (L38); the Überwelt manifests order vs. entropy (L46).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `(an earlier name)` alone on L27. not read: an earlier name on L27.
- **`kael`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `(an earlier name)` alone on L27. not read: an earlier name on L27.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L87. not read: an occurrence in the protocol text (L87).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L46. minor: digital entropy as glitches, noise, decay („Risse“) (L46).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L27, L36, L42, L46. minor: AEGIS as control core of a digital „Überwelt“ (L36); purely digital, information-based, rigidly structured (L46).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Systemkohärenz` (near `koharenz`). an occurrence.


**Record entries:** none.

**Not promoted:** universal reboot, nicht-lokale Nicht-Existenz, the protocol's acronyms, Ontologische Position, Rekursive Signatur, the opening's four parts.

**One reader**: every page above.
