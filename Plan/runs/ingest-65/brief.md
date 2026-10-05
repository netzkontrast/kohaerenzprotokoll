# Brief — readings from document 65 (step 6)

1 document, one reader, one batch: `ingest-65`. Files go to `Plan/runs/ingest-65/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 65 | `einleitung-genesis-der-existenz` | 2025-04-29 | „the Genesis narrative“ (its own title, `Einleitung: Genesis der Existenz`) | a German prose text in four parts — Vorwort, Genesis, Dazwischen, Die Krise — in which a fragment in the void forms clusters, becomes Komponente 734 of AEGIS, and AEGIS meets a foreign entity and answers with the Kohärenz Protokoll; the writer's own working remarks stand inside it; it claims no standing |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (198 lines for `einleitung-genesis-der-existen`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** **A narrative text, and research by the author's word** (2026-09-26: the narrative texts among the sources are research, never the novel's prose). A reading says what *this narrative tells*, quoting its sentences, and names the voice: the first-person narrator (the fragment, then Komponente 734) in the Genesis part and at L165–L175, L193–L197; a reporting past tense in „Die Krise“ (L137 on). The writer's working remarks (`nicht Spoilern`, `besserer Begriff?`, `Satz löschen, oder weniger foreshadowing`) are not the story — mention one only where it bears on a page. Footnote digits glued to words: `--find` drops them; quote around them. Document 60, `textanalyse-existenz-system-und-leid`, is a commentary on this very narrative: you may say so, citing it `^[textanalyse-existenz-system-und-leid.md:L22]`, and never compare further.

## Pages — document 65, `einleitung-genesis-der-existenz`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L89, L102, L106, L114, L116, L118, … (30 lines). central (4–8): the click of closure, „Ein fundamentales Einrasten im gesamten System.“ (L87); the principle in italics, „AEGIS ist, was AEGIS verhindert, dass es nicht ist.“ (L89) and „Die Existenz wird zur Funktion.“ (L89); the border as the system (L93); the turn inward to inner coherence (L114); AEGIS in „Die Krise“ as an information structure whose essence is inner coherence (L141); its ontology knew no qualia and read the resonance as a fault (L157, L159); its answer, the protocol (L161 on).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L147. not read: sweep occurrence (L147, the entity's emergence from the Potentialmeer).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L106. not read: sweep occurrence (L106).
- **`genesis`** (minor, 1–4): the census's surfaces — `Genesis` L29. central (4–8): the narrative's own sequence — the preface on the Nichts (L15–L27), the Rauschen and the fragment (L31–L39), resonance and clusters, the Triade (L45–L65), resistance (L67), the click and AEGIS's principle (L87–L93), the fragment become Komponente 734 (L100–L108), the Überwelt (L116–L124), „Dazwischen“ (L133–L135), the crisis: the foreign entity (L147), the misread resonance (L157), the protocol and the fragmentation of the Ursprungs-Ich (L161–L197). Give the order with lines; count no beats the text does not count.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L114. minor (1–3): the inward turn — true stability requires „tiefere, innere Kohärenz“ (L114); AEGIS's essence in the maintenance of inner coherence (L141); falling coherence metrics (L159); the narrator's last line „Die Kohärenz, die AEGIS sucht, ist mein Tod.“ (L197). `Kohärenz Protokoll` goes to trennungsprotokoll (J57).
- **`komponente-734`** (minor, 1–4): the census's surfaces — `Komponente 734` L100, L102, L104, L108, L120, L126. central (2–4): the heading „Komponente 734: Funktion an der Grenze“ (L100), the narrator become „Komponente 734“, a „Funktionseinheit“ (L102), at the closure (L87–L95), before the crisis; its being at the border (L106); the echo of loneliness and fear turned into a risk marker (L104, L108). Say the narrative makes the component at closure and the protocol comes later (L161, L187).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L141, L151. minor-to-central (2–4): the Rauschen the narrator is (L31, L33), the active Nichts (L37, L39), and „Nichts Rauschen“ as AEGIS's name for the void (L141).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Potentialmeer` alone on L141. minor (1–2): the void as „ein Potentialmeer unendlicher Zustände“ (L141), and the entity's emergence from it (L147).
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L187. central (2–5): the heading „Das Trennungsprotokoll: Fragmentierung als Heilung“ (L187) over the part that tells the `Kohärenz Protokoll` (L161, L189); the protocol as „ein radikaler, invasiver Eingriff“ (L161), its activation „kein Schalter“ but a sequence (L189); the narrator's experience (L193–L197). Say the narrative uses both names, one in a heading, without saying they are one thing; the protocol's number, `Kohärenz Protokoll 1.0`, stands once (count it).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L116, L120, L122, L124. central (2–4): „die Überwelt“ (L116), an inner simulated space, „ein Labor nach innen“ (L118), „Immunsystem und Metabolismus zugleich“ (L122), with a „Binnen-Physik“ (L124).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `ars`: `autopoietische` (near `arsautopoietischereentrysegmentierung`). occurrence: `autopoietische` is a common adjective (J69).
- `did`: `Entität` (near `diddissoziativeidentitatsstruktur`), `Entität` (near `dissoziativeidentitatsstruktur`). occurrence: the `Entität` is the foreign entity (L147), not DIS/DID.
- `kohaerenz`: `Kohärenzfeld` (near `koharenz`), `Kohärenzmetriken` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`), `Kohärenz Protokolls` (near `koharenz`), `Paradoxon der Fehlausgerichteten Kohärenz` (near `koharenz`), `Systemischer Kollaps: Die Auflösung der Kohärenz` (near `koharenz`). `Kohärenzfeld`, `Kohärenzmetriken` are compounds (J12); `Kohärenz Protokoll` goes to trennungsprotokoll (J57); `Paradoxon der Fehlausgerichteten Kohärenz` is read on kohaerenz only if the narrative states it as a sentence (find its line).


**Pages the lookup did not list, added by the reconciler:**

- **`residual-echos`** (1–2): the narrator's „alten Echos der Herkunft“ that are not erased (L95), and the „latenten Echos“ called the remains of the Ursprungs-Ich (L143). The narrative does not write `Residual-Echos` (count it).

**Record entry:** **`c12-genesis-beats`** (`Plan/runs/ingest-65/readings/c12-genesis-beats--einleitung-genesis-der-existenz.md`): the narrative's order — closure and the narrator become Komponente 734 (L87–L102), the Überwelt (L116), then the crisis, the entity, and the Kohärenz Protokoll under a heading naming the Trennungsprotokoll (L147–L189). The component precedes the protocol. It counts no beats.

Checked and not touched: Q7 (what 734 names) — the narrative names the narrator 734 and says nothing of the number; C3 — no position on AEGIS's emergence by that word.
