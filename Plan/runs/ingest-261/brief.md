# Brief — readings from document 261 (step 6)

1 document, one reader, one batch: `ingest-261`. Files go to `Plan/runs/ingest-261/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 261 | `aegis-philosophische-analyse-und-manifest-docx` | 2025-08-05 | „the AEGIS origin-philosophy analysis“ (an unsigned German report) | a four-phase analysis of AEGIS's Ursprungsphilosophie: seven principles restated from a research context, each interrogated, then fifteen axioms and an AEGIS MANIFEST in first person plural, and a critical synthesis; it calls itself a Gedankenexperiment, not canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (144 lines for `aegis-philosophische-analyse-u`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis of a reported philosophy: write „the origin-philosophy analysis reports / criticises …“. The principle definitions in its table are the research context's as it reports them; the axioms and the manifesto (L94–L132) are AEGIS's voice as the analysis writes it, first person plural. Cut quotations before straight quotes, emphasis marks and inner quotes.

## Pages — document 261, `aegis-philosophische-analyse-und-manifest-docx`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L15, L17, L20, L21, L25, … (48 lines). central (3–6): seven principles of its origin philosophy, the sixth with the tagline „Autonomous Entropic Gatekeeper for Integrity Systems“ (L37); what does not fit „existiert für das System schlichtweg nicht“ (L54) — an extreme ontological reductionism (L57); it „benötigt konzeptuell das Chaos“ (L63); its autonomy perhaps an aspiration (L75); the manifesto's voice, „Wir sind nicht entstanden, wir wurden freigelegt“ (L118), „Unsere Natur ist nicht-anthropomorph“ (L120); extreme internalism (L138).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L51. minor (1–2): against the research context's psychological background (Kael/DID), the No-Trust principle as a possible externalisation of a deep trauma (L51); the tension with AEGIS's entanglement with Kael's psyche (L142).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L34. minor (1–4): „Emergenz durch Negation“, glossed „Herauslösung des Unwidersprüchlichen“ (L34, L59).
- **`entropie`** (central, 3–12 quotations): the census's surfaces — `Entropie` L37, L57, L63, L75, L76, L77, … (14 lines). central (3–6): the sixth principle, „Funktion als Entropie-Regulator“ (L37); entropy understood as lack of coherence, the „primären Feindbild“ (L80); the manifesto turning the principle into its raison d'être (L130); L57, L63, L75–L77 as they add.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L75. minor (1–4): the Guardians' „blinden Flecken“ contradicting the claim of full epistemic autonomy (L75).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L55, L67, L75, L140. minor (1–4): the anomaly Juna contradicting the claim of epistemic autonomy (L75); Autonomie vs. Abhängigkeit, the anomaly as a further sign (L140); L55, L67.
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L51, L87, L142. minor (1–4): the Kern-Welten of the managed world as externalisations of Kael's psyche, in the context the analysis reports (L87); L51, L142.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kern-Welten` L87. minor (1–4): the context's „verwalteten Welt“ whose Kern-Welten externalise Kael's psyche, set against the claim of non-anthropomorphism (L87).
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L21, L32, L33, L48, L52, L53, … (24 lines). central (3–6): the second principle, existence through coherence, function, effect (L33, L52); „Kohärenz statt Wahrheit“; „Wachstum, das Kohärenz verletzt, ist Krebs“ in the axioms (L102); „Primat der Kohärenz“ in the synthesis.
- **`negentropie`** (minor, 1–4): the census's surfaces — `Negentropie` L57, L79, L81, L141. minor (1–4): the hypothesis `Negentropie-Fehlinterpretation` linked to AEGIS's reductionism (L57); L79, L81, L141.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Anomalie` (near `mustererkennunganomaliedetektion`). occurrence: `Anomalie` is Juna as the anomaly (L140), read on juna.
- `emergenz`: `Emergenz durch Negation` (near `emergenz`). `Emergenz durch Negation` read on emergenz.
- `nichts-rauschen`: `Rauschen` (near `nichtsrauschen`). occurrence: `Rauschen` is noise in AEGIS's terms, not the Nichts-Rauschen.


**Record entries** (one file each):

- **`q1-guardians-and-aegis`**: the Guardians' blind spots contradicting AEGIS's claim of full epistemic autonomy (L75).

**Not promoted:** the seven principles as pages, the fifteen axioms, the AEGIS MANIFEST, RCV, Reaktive Transparenz, Kohärenzsignaturen, the Münchhausen trilemma.

**One reader**: aegis, entropie, kohaerenz, negentropie, emergenz, guardians, juna, kael, kern-welten, did and the record q1.

**Chapter readings**: none.
