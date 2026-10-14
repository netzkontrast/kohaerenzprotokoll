# Brief — readings from document 465 (step 6)

1 document, one reader, one batch: `ingest-465`. Files go to `Plan/runs/ingest-465/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 465 | `genesis-und-krise-ausfuehrliche-darstellung` | 2025-04-29 | „the Genesis narrative“ (an unsigned German first-person prose text, headed „Genesis“ and „Die Krise“) | narrates in 13 scenes and three parts how a fragment awakens in the Nichts Rauschen, becomes Komponente 734 inside AEGIS, is cut apart by AEGIS through the Kohärenz Protokoll and ends as Kael among the Kernwelten; a draft narrative with no standing claimed, recorded, never canon|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (108 lines for `genesis-und-krise-ausfuehrlich`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A draft narrative: write „the Genesis narrative tells …“; its first-person „Ich“ is a narrative voice, unnamed until „Kael ist geboren.“ (L107); its terms are offered, not fixed („könnte hier entstehen“, L31). No gendered pronoun for the Ich, Kael, AEGIS or 734 — use the names (quotations verbatim). Cut before italics and scene labels.

## Pages — document 465, `genesis-und-krise-ausfuehrliche-darstellung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L33, L35, L39, L45, L47, L51, … (22 lines). central (4–8): AEGIS's birth narrated as „Der Klick.“ and the principle „Ich bin die Abwehr des Nicht-Seins.“ (L39); existence becomes function, operational closure against the void (L39); the boundary becomes an active defence front (L41); AEGIS sees the anomaly in Komponente 734 but not its nature (L53); the entity is unsimulable for AEGIS (L87); the decision for the Kohärenz Protokoll, this time for execution (L95); the execution from the system's side „ein präziser, chirurgischer Eingriff“ (L99), stabilisation „(scheinbar)“ reached (L101).
- **`blinder-fleck`** (minor, 1–4): the census's surfaces — `blinder Fleck` L67. minor (1–4): after the simulation reaches a hard limit, the narration speaks of „ein weiterer blinder Fleck“ (L67).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L11. not read: an occurrence — L11 is the heading.
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L103, L107. minor (1–4): „Kael ist geboren.“ (L107), „ein Mosaik aus Schmerz und Verlangen“ (L107), with an open ending (L107); the fragments in the ruins of the old structure, the Kernwelten (L105).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L105, L107. minor (1–4): the Kernwelten as the ruins of the old structure where the fragments lie and Kael is born (L105, L107).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — `Kohärenz` L17, L23, L31, L59, L77, L87, … (7 lines). minor (1–4): coherence as the order the fragment seeks and AEGIS enforces; the decision for the Kohärenz Protokoll as execution (L95) — the protocol's name stands once.
- **`komponente-734`** (central, 3–12 quotations): the census's surfaces — `Komponente 734` L43, L45, L47, L51, L53, L57, … (16 lines). central (4–8): the fragment exists now as Komponente 734 (L45), „Eine neue Identität, definiert durch Funktion und Position im Netzwerk von AEGIS.“ (L45); what remains is the persistent latent signature of the original incompleteness (L47); a resonance frequency of the external signature matches 734's latent signature (L77); 734's execution from the awakened Ich's side „unvorstellbarer Horror“ (L101).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L17, L45, L63, L65, L105. minor (1–4): the opening „Ich bin. Kaum mehr.“ in the Nichts Rauschen, which is no silence and no emptiness as absence (L17), „ein aktives, drückendes Potential“ (L17); the fragments end in the Nichts Rauschen and the ruins (L105).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L55, L57, L59, L63, L83, L85, … (7 lines). minor (1–4): the Überwelt no physical place but a state of heightened, focused internal activity, made by AEGIS as a tool of optimisation (L57); abstract concepts born there as internal tools (L59); its simulation reaches a hard limit (L65).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Anomalie` (near `mustererkennunganomaliedetektion`). an occurrence: a common word of the narration (Grenze, Kern, Bindung, Echo, Resonanz, Mosaik, Anomalie, Entität, Fragment), not the page's term.
- `archiv-der-grenzen`: `Grenze` (near `archivdergrenzen`). an occurrence: a common word of the narration (Grenze, Kern, Bindung, Echo, Resonanz, Mosaik, Anomalie, Entität, Fragment), not the page's term.
- `did`: `Entität` (near `diddissoziativeidentitatsstruktur`), `Entität` (near `dissoziativeidentitatsstruktur`), `Fragment` (near `psychischefragmentierung`). an occurrence: a common word of the narration (Grenze, Kern, Bindung, Echo, Resonanz, Mosaik, Anomalie, Entität, Fragment), not the page's term.
- `dkt`: `Kern` (near `dualkerneltheoriedkt`). an occurrence: a common word of the narration (Grenze, Kern, Bindung, Echo, Resonanz, Mosaik, Anomalie, Entität, Fragment), not the page's term.
- `entropie-resonanz`: `Resonanz` (near `entropieresonanz`), `Resonanz` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz` (near `entropieresonanzprotokolle`). an occurrence: a common word of the narration (Grenze, Kern, Bindung, Echo, Resonanz, Mosaik, Anomalie, Entität, Fragment), not the page's term.
- `grosse-mauer`: `Grenze` (near `groemauersystemgrenze`), `Grenze` (near `systemgrenze`). an occurrence: a common word of the narration (Grenze, Kern, Bindung, Echo, Resonanz, Mosaik, Anomalie, Entität, Fragment), not the page's term.
- `kael-julia-bindung`: `Bindung` (near `kaeljuliabindung`), `Bindung` (near `kjbindung`). an occurrence: a common word of the narration (Grenze, Kern, Bindung, Echo, Resonanz, Mosaik, Anomalie, Entität, Fragment), not the page's term.
- `kohaerenz-kernel`: `Kern` (near `kohaerenzkernel`), `Kern` (near `koharenzkernel`), `Kern` (near `koharenzkernelk1`). an occurrence: a common word of the narration (Grenze, Kern, Bindung, Echo, Resonanz, Mosaik, Anomalie, Entität, Fragment), not the page's term.
- `kollaps-kernel`: `Kern` (near `kollapskernel`), `Kern` (near `kollapskernelk0`). an occurrence: a common word of the narration (Grenze, Kern, Bindung, Echo, Resonanz, Mosaik, Anomalie, Entität, Fragment), not the page's term.
- `mosaik-herz`: `Mosaik` (near `mosaikherz`). an occurrence: a common word of the narration (Grenze, Kern, Bindung, Echo, Resonanz, Mosaik, Anomalie, Entität, Fragment), not the page's term.
- `residual-echos`: `Echo` (near `residualechos`). an occurrence: a common word of the narration (Grenze, Kern, Bindung, Echo, Resonanz, Mosaik, Anomalie, Entität, Fragment), not the page's term.
- `resonanz-landschaft`: `Resonanz` (near `resonanzlandschaft`). an occurrence: a common word of the narration (Grenze, Kern, Bindung, Echo, Resonanz, Mosaik, Anomalie, Entität, Fragment), not the page's term.


**Record entries** (one file each, formatted as earlier entries):
- **`q7-what-734-names`**: the Genesis narrative has the awakened fragment exist as Komponente 734, defined by function and position in AEGIS's network (L45); recorded.
- **`c16-kael-origin`**: the narrative has Kael born from the fragments of 734 cut apart by the Kohärenz Protokoll, in the Kernwelten (L101, L105, L107); recorded, not applied.

**No chapter readings**: the narrative numbers scenes of Genesis, not chapters of the novel.

**Not promoted:** Der Klick, Abwehr des Nicht-Seins, the scene titles, TEIL, NEUE, Zerstückelung, Lockdown, and the common words offered as terms (Bindung, Fluss, Kern).

**One reader**: every page above and the two record entries.
