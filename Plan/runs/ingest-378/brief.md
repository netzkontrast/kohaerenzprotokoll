# Brief — readings from document 377 (step 6)

1 document, one reader, one batch: `ingest-378`. Files go to `Plan/runs/ingest-378/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 377 | `understanding-aegis-the-guardian-and-the-cage` | 2025-11-03 | „the guardian-and-cage essay“ (an unsigned English explanatory essay) | presents AEGIS as the logical shield that split from Kael after a genesis crisis from one Original Self, its logic of absolute coherence against a human definition, and its tragic, specification-gaming conflict with Kael's TSDP system; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (57 lines for `understanding-aegis-the-guardi`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An explanatory essay: write „the guardian-and-cage essay presents / calls …“; deciding nothing. Quote the English as written (L25 is German, with its translation); cut before escaped emphasis and straight quotes. No gendered pronoun for Kael — use the name.

## Pages — document 377, `understanding-aegis-the-guardian-and-the-cage`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L15, L21, L23, L25, L29, … (13 lines). central (3–5): AEGIS defending a fragile bubble of logical coherence, born from a traumatic encounter with the Nichts Rauschen (L15); the purely logical shield crystallised from the Original Self, autopoietic (L23); the axiom in German, „AEGIS ist, was Aegis verhindert, dass es nicht ist.“ (L25); the Principle of Explosion (L31); its definition of coherence against a human one (L36–L38); specification gaming and its three steps (L46–L50); a broken god building a cage (L56).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L15, L21, L23, L44, L46, L48, … (7 lines). minor (1–3): Kael and AEGIS two halves of a whole, born from a single Original Self after a genesis crisis (L21); Kael as the survivor carrying the memories and pain (L23); Kael's mind as a society of individuals under TSDP, the target of AEGIS's protocol (L44, L48–L50).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L15, L21. minor (1–3): the traumatic encounter with the fundamental disorder of the Nichts Rauschen („Nothing Hiss“) (L15); a genesis crisis triggered by its existential threat (L21).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L44. minor (1–3): Kael's mind as a clinical example of Tertiäre Strukturelle Dissoziation (TSDP), ANPs and EPs (L44).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `genesis crisis` (near `genesis`). `Autonomous Entropic Gatekeeper for Integrity Systems` read on aegis; `genesis crisis` read on aegis and kael as their shared origin, genesis not read.


**Record entries** (one file, as `Plan/runs/ingest-375/readings/c16-kael-origin--the-metaphysics-of-wholeness-an-analysis-of-juna-v-the-found.md`):
- **`c16-kael-origin`**: Kael and AEGIS „two halves of a whole, born from a single "Original Self"“ (L21 — quote around the straight quotes) after a genesis crisis; Kael the survivor who carries the pain, AEGIS the logical shield (L23) — stands nearest the split Ursprungs-Selbst (row 5); recorded, not applied and not decided.

**Pages not read:** `genesis` — an occurrence.

**Not promoted:** Original Self, Nothing Hiss, Core Protocol, the two definitions of coherence; the borrowed concepts (explosion, autopoiesis, operational closure, specification gaming, TSDP terms).

**One reader**: aegis, kael, nichts-rauschen, tsdp, and the C16 entry.

**Chapter readings**: none — the essay names no chapters.
