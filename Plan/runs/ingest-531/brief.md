# Brief — readings from document 531 (step 6)

1 document, one reader, one batch: `ingest-531`. Files go to `Plan/runs/ingest-531/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 531 | `kapitel-13-momente` | 2025-04-20 | „the chapter-13 moments“ (a planning list) | plans Kapitel 13 as Step 1.13 of Blueprint V2, the close of Part 1: five groups of moments — Kael at the abyss before Cerberus, the Juna-Resonanz, Kael defying, AEGIS's Universal Reboot from v1.4 to v1.5, the world dissolving; proposals, no canon claim|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (61 lines for `kapitel-13-momente`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan: write „the chapter-13 moments plan …“; every moment is a proposal under an old outline's numbering (Blueprint V2, Step 1.13), never canon. **Never cite L30** (an earlier name). No gendered pronoun for Kael, Juna, AEGIS or Cerberus in our own prose; quotations stay verbatim, preferably cut before pronouns.

## Pages — document 531, `kapitel-13-momente`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L13, L40, L42, L44, L45, L46, … (9 lines). minor (1–4): registers the massive Juna-Resonanz as an uncontrollable anomaly and the failure of Cerberus's containment; „Protokoll v1.4 ist gescheitert.“ (L44); its core logic reads an existential risk and resets to v1.5 (L45); initiates the Universal Reboot (L46); the transition to AEGIS v1.5 and Part 2 (L58).
- **`cerberus`** (central, 3–12 quotations): the census's surfaces — `Cerberus` L11, L13, L19, L20, L27, L33, … (12 lines). central (3–8): Kael cornered by Cerberus at the abyss (L13, L19); Cerberus's triumph, systems signalling the final grab (L20); the Wächter's irritation — protocols built for predictable threats (L39); caught by the reboot, glitching and stopping the attack (L52).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `(an earlier name)` alone on L30. minor (1–4): only in compounds: the Juna-Verbindung's unexpectedly strong resonance at Kael's lowest point (L13); the Juna-Motiv returning „kraftvoll, rein, leuchtend“ (L28); the Juna-Resonanz as the one fixed point Kael clings to (L56). Never cite L30.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L11, L13, L19, L21, L22, L23, … (19 lines). central (3–8): the lowest point, facing defeat by Cerberus at the abyss (L13); the inner capitulation voiced by Nox (L22); the bond recognised as „seine tiefste Wahrheit und Quelle seiner Resilienz“ (L32 — that span); the changed stance (L37); clinging to the Juna-Resonanz as the world dissolves (L56); fate uncertain in the reboot (L58).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L31. not read: an occurrence — „Moment innerer Kohärenz“ (L31), not the page's term.
- **`protokoll-v14`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Protokoll v1.4` alone on L44. minor (1–4): „Protokoll v1.4 ist gescheitert.“ (L44) — the reboot to v1.5 follows (L45).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie-resonanz`: `Resonanz` (near `entropieresonanz`), `Resonanz` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz` (near `entropieresonanzprotokolle`). an occurrence: `Resonanz` here is the Juna-Resonanz, not the page's term.
- `juna`: `Juna-Resonanz` (near `juna`), `Juna-Verbindung` (near `juna`), `Juna-Motiv` (near `juna`). a reading: `Juna-Resonanz`, `Juna-Verbindung`, `Juna-Motiv` — read on juna above.
- `residual-echos`: `Echo` (near `residualechos`). an occurrence: `Echo` names an inner voice (L31), not the page's term.
- `resonanz-landschaft`: `Resonanz` (near `resonanzlandschaft`). an occurrence: `Resonanz` here is the Juna-Resonanz.


**Record entries:** none.

**Chapter readings** (batch `ingest-531-kap`, `Plan/runs/ingest-531-kap/readings/kap-13--kapitel-13-momente.md`, formatted as the files in `Plan/runs/ingest-490-kap/readings/`), the plan's proposal for that chapter, never canon:
- **kap-13**: Kapitel 13 as Step 1.13 „Der Abgrund und der Ruf“ of Blueprint V2, closing Part 1 after Kapitel 12 (L11); its goal (L13); the five groups A–E of moments (L17, L25, L35, L42, L48); the last image of Part 1 and the cut to the reboot (L57, L58). Never cite L30.

**Not promoted:** the moment list as a list, the inner voices Nox, Praetor and Echo, Schattenlabyrinth, KW3 as a surface, Universal Reboot, AEGIS v1.5, Blueprint V2 and its steps.

**One reader**: every page above and the chapter reading.
