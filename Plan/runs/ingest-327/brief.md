# Brief — readings from document 326 (step 6)

1 document, one reader, one batch: `ingest-327`. Files go to `Plan/runs/ingest-327/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 326 | `genesis-finale-prosa-angepasste-ich-natur` | 2025-04-29 | „the final Genesis prose“ (an unsigned German first-person prose narrative) | the Genesis story as finished prose in three parts and 13 scenes, italic first-person passages alternating with AEGIS's report voice: from a spark of coherence in the Rauschen through AEGIS's emergence and the fragment Komponente 734, Anomalie and Entität Sigma, to the Kohärenz Protokoll Gamma-Exekution and Kael waking amid the Kernwelten; no claim about its standing |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (208 lines for `genesis-finale-prosa-angepasst`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Finished prose of a story already read as a draft (documents 323 and 324): write „the final Genesis prose narrates … in Szene N …“, say whether a quotation is the italic first-person voice or AEGIS's report voice, and read only where this version adds to what the draft gave — the component's own voice, the Gamma-Exekution, Kael waking amid the Kernwelten. Cut quotations before glued digits and escaped characters.

## Pages — document 326, `genesis-finale-prosa-angepasste-ich-natur`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L45, L47, L59, L63, L77, L79, … (30 lines). minor (1–3): the decision „Aktiviere Kohärenz Protokoll Gamma-Exekution.“ (L179) — AEGIS's report voice; only lines this version adds.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L55. not read: the final prose tells what the draft (document 323) already gave on this page.
- **`genesis`** (minor, 1–4): the census's surfaces — `Genesis` L11. not read: occurrence — `Genesis` (L11) is the title.
- **`grosse-mauer`** (minor, 1–4): the census's surfaces — `Systemgrenze` L65. not read: occurrence — `Systemgrenze` (L65) is AEGIS's own boundary in the report voice.
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L201, L207. minor (1–3): named only in the last scene: „Etwas Neues ist hier. Kael. Nicht kohärent. Eine Potentialität.“ (L207).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L203, L207. minor (1–3): the place of the last scene, first as a question, „Kernwelten? Verwirrung“ (L203), Kael waking amid them (L207).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — `Kohärenz` L19, L41, L107, L113, L137, L157, … (8 lines). not read: the final prose tells what the draft (document 323) already gave on this page.
- **`komponente-734`** (central, 3–12 quotations): the census's surfaces — `Komponente 734` L71, L73, L75, L77, L87, L91, … (18 lines). central (3–6): the report voice designating the original fragment `Komponente 734` and the italic voice taking it up, „Ich bin... ein Teil. Komponente 734.“ (L75); its latent signature; the Gamma-Exekution against it (L179) — only lines this version adds.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L73, L113, L119. not read: the final prose tells what the draft (document 323) already gave on this page.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L99, L101, L103, L107, L147, L149, … (7 lines). not read: the final prose tells what the draft (document 323) already gave on this page.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `dkt`: `Kern` (near `dualkerneltheoriedkt`). occurrence: as in document 323; not read.
- `entropie-resonanz`: `Resonanz` (near `entropieresonanz`), `Resonanz` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz` (near `entropieresonanzprotokolle`). occurrence: as in document 323; not read.
- `kael-julia-bindung`: `Bindung` (near `kaeljuliabindung`), `Bindung` (near `kjbindung`). occurrence: as in document 323; not read.
- `kohaerenz-kernel`: `Kern` (near `kohaerenzkernel`), `Kern` (near `koharenzkernel`), `Kern` (near `koharenzkernelk1`). occurrence: as in document 323; not read.
- `kollaps-kernel`: `Kern` (near `kollapskernel`), `Kern` (near `kollapskernelk0`). occurrence: as in document 323; not read.
- `mosaik-herz`: `Mosaik` (near `mosaikherz`). occurrence: as in document 323; not read.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: as in document 323; not read.
- `resonanz-landschaft`: `Resonanz` (near `resonanzlandschaft`). occurrence: as in document 323; not read.


**Record entries:** none — its account of Komponente 734 and Kael is the draft's, already on C16 and Q7 from document 323.

**Not promoted:** the Ich-Konstrukt, the latente Signatur, Anomalie and Entität Sigma, the Protokoll Gamma-Exekution, the scenes and parts.

**One reader**: aegis, kael, kern-welten, komponente-734.

**Chapter readings**: none — its parts and scenes are its own, not the novel's chapters.
