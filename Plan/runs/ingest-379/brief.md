# Brief — readings from document 378 (step 6)

1 document, one reader, one batch: `ingest-379`. Files go to `Plan/runs/ingest-379/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 378 | `understanding-kohaerenz-protokoll-the-art-of-sticking-togeth` | 2025-11-03 | „the sticking-together explainer“ (an unsigned English explainer) | presents coherence as one principle in three realms: philosophy (AEGIS's coherence theory against Kael's correspondence theory), psychology (Kael's ANPs as cohesion, the EPs' truths as missing coherence) and physics (the Protocol Ontology, Dual Kernel Theory, Coherons, Corrective Wavelets); it calls its subject „this fictional world“, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (105 lines for `understanding-kohaerenz-protok`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An explainer: write „the sticking-together explainer presents / maps …“; deciding nothing. Quote the English as written; cut before escaped emphasis and straight quotes. No gendered pronoun for Kael or the parts — use the names.

## Pages — document 378, `understanding-kohaerenz-protokoll-the-art-of-sticking-togeth`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L25, L33, L34, L38, L87, L98, … (7 lines). minor (1–3): AEGIS as the living embodiment of a pathological Coherence Theory of Truth, born from the Genesis-Krise (L25); truth as internal consistency alone (L34); a system pathologically devoted to the K₁ kernel, misinterpreting K₀'s erosive pressure as entropy or noise (L87).
- **`alters`** (minor, 1–4): the census's surfaces — `alters` L27, L35, L46. minor (1–3): Kael's mind as a system of dissociated alters with amnesic barriers under TSDP (L46).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L27, L33, L34, L38, L40, L46, … (14 lines). central (3–5): System Kael forced to embody the Correspondence Theory of Truth, facing the reality of trauma (L27, L34); System Kael cohesive yet incoherent (L58); healing as the journey from cohesion to coherence (L59); Kael's journey as learning to embrace the K₀ kernel and its correspondence checks (L88).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L54. minor (1–3): Kiko (the terrified child) among the EPs whose truths do not correspond with the ANPs' normalcy (L54).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence (see below).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L48. minor (1–3): Lex (the rationalist) among the ANPs creating the surface cohesion of daily life (L48).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L54. minor (1–3): Nyx (the protector filled with rage) among the EPs holding the traumatic truths (L54).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L48. minor (1–3): Rhys (the caregiver) among the ANPs creating the surface cohesion of daily life (L48).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L46. minor (1–3): Kael's mind governed by the Theory of Structural Dissociation of the Personality (TSDP), a system of dissociated alters (L46).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `coheron`: `Coherons` (near `coheron`). `System Kael` on kael; `Genesis-Krise` on aegis, genesis not read; `Coherons` on coheron; `Kohärenz Protokoll` the title; `Theory of Structural Dissociation of the Personality` on tsdp, not personas.
- `genesis`: `Genesis-Krise` (near `genesis`). `System Kael` on kael; `Genesis-Krise` on aegis, genesis not read; `Coherons` on coheron; `Kohärenz Protokoll` the title; `Theory of Structural Dissociation of the Personality` on tsdp, not personas.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). `System Kael` on kael; `Genesis-Krise` on aegis, genesis not read; `Coherons` on coheron; `Kohärenz Protokoll` the title; `Theory of Structural Dissociation of the Personality` on tsdp, not personas.
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`). `System Kael` on kael; `Genesis-Krise` on aegis, genesis not read; `Coherons` on coheron; `Kohärenz Protokoll` the title; `Theory of Structural Dissociation of the Personality` on tsdp, not personas.


**Pages beyond the draft:**
- `dkt` (minor, 1–2): the Protocol Ontology, reality emerging from the conflict of two kernels (L69); the Coherence Kernel (K₁) as the principle of order (L71) and the Collapse Kernel (K₀) (its line).
- `coheron` (minor, 1): the K₁ kernel building reality out of „atoms of persistence“ called Coherons (L71); the Corrective Wavelet as self-repair (L83).

**Pages not read:** `kohaerenz` (L11, the title), `genesis`, `personas` — occurrences.

**Record entries:** none.

**Not promoted:** cohesion and coherence as labels, Protocol Ontology, Corrective Wavelet, erosive pressure, correspondence check, internal consistency / external validation; the borrowed concepts (theories of truth, decoherence, TSDP terms).

**One reader**: aegis, alters, kael, kiko, lex, nyx, rhys, tsdp, dkt, coheron.

**Chapter readings**: none — the explainer names no chapters.
