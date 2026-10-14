# Brief — readings from document 488 (step 6)

1 document, one reader, one batch: `ingest-488`. Files go to `Plan/runs/ingest-488/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 488 | `the-minds-behind-the-machine-a-psychological-guide-to-system` | 2026-01-02 | „the System-Kael guide“ (an unsigned English guide, „The Minds Behind the Machine: A Psychological Guide to ‚System Kael‘“) | introduces the cast through two borrowed trauma frameworks, gives a roster of six alters with roles, the transformations of Nyx and Kiko, functional multiplicity and AEGIS's undoing; an interpretive guide, no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (57 lines for `the-minds-behind-the-machine-a`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An interpretive guide: write „the System-Kael guide reads …“ or „assigns …“. The roster at L31 is a flattened table on one line; quote only short spans of it. L52 carries a figure named after a logician — never quote a span containing it. Quote the English as written; cut before bold, escaped asterisks, `$…$` formulas and inner quotes. No gendered pronoun for Kael, AEGIS or any alter in our own prose — the guide itself uses them; quotations stay verbatim.

## Pages — document 488, `the-minds-behind-the-machine-a-psychological-guide-to-system`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L15, L23, L31, L52. minor (1–4): AEGIS the hyper-logical AI, refuted by the internal journey (L15); the daily-life parts mirror Coherence, the drive for order embodied by AEGIS (L23 — describe around formulas); AEGIS operating on classical logic, forced into Algorithmische Melancholie (L52).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L31. minor (1–4): Alex an ANP, the protector, a proactive strategic defender who plans defenses and manages crises (L31).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L52. minor (1–4): AEGIS forced into Algorithmische Melancholie, a cognitive shutdown that liberates Kael (L52).
- **`alters`** (minor, 1–4): the census's surfaces — `alters` L19, L48. minor (1–4): System Kael as one individual fragmented into distinct consciousnesses called alters or parts, a Society of Self (L19); the roster of six alters with TSDP roles (L31); the goal not to merge all alters (L48).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L11, L15, L19, L29, L31, L43, … (10 lines). central (4–8): Kael as the ANP host, the primary front-runner who keeps an illusion of unity and normalcy (L31); the arc toward functional multiplicity, not merger (L48); Kael learning to give Nyx's fire a hearth (L43) and to sit with Kiko in the fear (L44); Kael's paraconsistent logic as the weapon against AEGIS (L52 — quote only spans without the name).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L31, L41, L44. minor (1–4): Kiko an EP, the child, the Freeze response, holding the earliest memories of terror and abandonment (L31); transformed from Fragile Child into a source of Playfulness and Intuition (L44 — describe around the bold).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L31. minor (1–4): Lex an ANP, the rationalist, mirroring AEGIS's logic on a micro-scale, viewing emotional parts as system errors (L31).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L31. minor (1–4): Moros an EP, the persecutor, internalized shame and self-hatred mimicking the abuser's voice; the integration noted as the system's most difficult task (L31).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L31, L37, L41, L43. minor (1–4): Nyx an EP, the fighter, holding the system's rage (L31); in the guide's frame a protector forced into an extreme role (L37); transformed from Fighter into Guardian, the system's Chief of Security (L43 — describe around the bold).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L15, L21, L23, L27, L31, L37, … (7 lines). minor (1–4): TSDP as the diagnostic framework explaining why a personality fragments (L23); ANPs and EPs (L27); TSDP gives the what, the second framework the how (L56).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). an occurrence: `Guardian` is Nyx's transformed role, not the subfunction.
- `grosse-mauer`: `System` (near `groemauersystemgrenze`), `System` (near `systemgrenze`). an occurrence: `System` means System Kael, not the wall.
- `guardians`: `Guardian` (near `guardians`). an occurrence: `Guardian` is Nyx's transformed role (L43), not the Guardians.
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`). an occurrence: the borrowed theory's name.
- `system-monitor`: `System` (near `groersystemmonitor`), `System` (near `groesystemmonitor`), `System` (near `systemmonitor`). an occurrence: `System` means System Kael.


**Pages beyond the draft:**
- **`kohaerenz-kernel`** (minor, 1–2): the daily-life parts mirror Coherence (K₁), the drive for order and control embodied by AEGIS (L23 — the line writes the symbol as a formula; describe).
- **`kollaps-kernel`** (minor, 1–2): the trauma-holding parts correspond to Collapse (K₀), the chaotic but truthful reality of entropy AEGIS seeks to deny (L23 — describe around the formula).

**Record entries:** none.

**No chapter readings**: the guide names no chapter.

**Not promoted:** System Kael, Society of Self, Unburdening, Burdens, Functional Multiplicity, its three principles, Paraconsistent Logic, Principle of Explosion, the alters' transformed roles, and the borrowed concepts (one carries a person's name).

**One reader**: every page above.
