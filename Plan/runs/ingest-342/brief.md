# Brief — readings from document 341 (step 6)

1 document, one reader, one batch: `ingest-342`. Files go to `Plan/runs/ingest-342/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 341 | `trauma-archaeologie-interdisziplinaere-konzeptentwicklung-do` | 2025-08-05 | „the Trauma-Archäologie report“ (an unsigned German research report, docx export) | develops four hypotheses and four worked concepts for the origin of a „fragmentierte Protagonistenidentität“ in a simulated cosmos grounded on Fundament/Leere and watched by a controlling Entität, under its central term „Traumatisierung durch Existenz“; it names neither Kael nor AEGIS, chooses no concept, and ends in a web reference list; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (524 lines for `trauma-archaeologie-interdiszi`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A research report of hypotheses: write „the Trauma-Archäologie report proposes …“ and keep its conditional. It never names the protagonist or the entity; say „the report's unnamed protagonist system“ and „the controlling Entität“, never Kael or AEGIS. Its Genesis is marked hypothetical (L29). Cut before inner quotation marks and glued reference digits.

## Pages — document 341, `trauma-archaeologie-interdisziplinaere-konzeptentwicklung-do`

- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L130. minor (1–3): in concept 1 the psyche splitting to hold the paradox, one part holding the awareness of the Leere (L130), compared to the function of Alters in DID (L130); the parts as roles in the conditional for concept 2 (L139).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L130. minor (1–3): the comparison of the protagonist system's parts to the function of Alters in the Dissoziative Identitätsstörung (L130) — a borrowed clinical frame.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L35. not read: an occurrence (see below).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L67. not read: an occurrence (see below).
- **`genesis`** (minor, 1–4): the census's surfaces — `Genesis` L27, L29, L33, L53, L270. minor (1–3): the section „Dekonstruktion der Genesis“ (L27) working from a hypothetical Genesis narrative fragment or deriving it from the cosmology (L29).
- **`risse`** (minor, 1–4): the census's surfaces — `Glitches` L47, L120, L156, L236. minor (1–3): the question whether early signs of the reality's artificiality or its „Glitches“ could lead to existential dissonance (L47) — only if the page's sense of Risse fits; otherwise not read.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L46, L67, L101, L280, L281, L305. not read: an occurrence (see below).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Simulation` L17, L47, L51, L53, L61, L81, … (32 lines). not read: an occurrence (see below).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `did`: `Entität` (near `diddissoziativeidentitatsstruktur`), `Entität` (near `dissoziativeidentitatsstruktur`), `Fragmentierung` (near `psychischefragmentierung`). occurrence: the report's own terms (`Emergenzparadox`, `Trauma der gewaltsamen/fehlerhaften Emergenz`, `Emergenz als ontologischer Bruch`), its generic `Entität` and `Fragmentierung`, and the borrowed `Depersonalisation` — not the pages' terms.
- `emergenz`: `Emergenzparadox` (near `emergenz`), `Trauma der gewaltsamen/fehlerhaften Emergenz` (near `emergenz`), `Emergenz als ontologischer Bruch` (near `emergenz`). occurrence: the report's own terms (`Emergenzparadox`, `Trauma der gewaltsamen/fehlerhaften Emergenz`, `Emergenz als ontologischer Bruch`), its generic `Entität` and `Fragmentierung`, and the borrowed `Depersonalisation` — not the pages' terms.
- `personas`: `Depersonalisation` (near `persona`). occurrence: the report's own terms (`Emergenzparadox`, `Trauma der gewaltsamen/fehlerhaften Emergenz`, `Emergenz als ontologischer Bruch`), its generic `Entität` and `Fragmentierung`, and the borrowed `Depersonalisation` — not the pages' terms.


**Pages not read:** `emergenz` (L35 the report's own emergence trauma), `entropie` (L67 generic), `sophia` (the Gnostic Sophia, a borrowed myth, not the Guardian), `ueberwelt` (the report's simulated cosmos, unnamed and not tied to AEGIS) — occurrences.

**Record entries:** none.

**Not promoted:** Traumatisierung durch Existenz, the four hypotheses and concepts, the controlling Entität, Verbindung zum Fundament/Leere, Schlüsselwörter; the borrowed concepts (Gnostic Sophia, Neoplatonism, demiurge, Fall and Eden, It from Bit, C-PTSD, depersonalisation, panopticon, gaslighting).

**One reader**: alters, did, genesis, risse.

**Chapter readings**: none — the report names no chapter of the novel.
