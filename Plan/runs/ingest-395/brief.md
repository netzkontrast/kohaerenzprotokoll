# Brief — readings from document 394 (step 6)

1 document, one reader, one batch: `ingest-395`. Files go to `Plan/runs/ingest-395/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 394 | `kapitel-eins-1-kohaerenz-protokoll` | 2026-02-22 | „the Kapitel-Eins draft“ (an unsigned German prose draft of „Kapitel Eins – Der Kristalline Käfig“) | close third person on Kael: waking in a sterile room, Juna's image demanding a status report, a wave of grief at the word LogOS, a ride through the Konstrukt-Stadt, an organic anomaly deleted, and the sound of splintering glass; no label, no claim of standing — a draft, not the chapter as approved |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (98 lines for `kapitel-eins-1-kohaerenz-proto`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A prose draft: write „in the Kapitel-Eins draft …“; it is a draft, not the chapter as approved, and its events are what the draft narrates. Quote the German as written; cut before the stray full stops after closing marks and before italics markers. No gendered pronoun for Kael or Juna — use the names (quotations stay verbatim).

## Pages — document 394, `kapitel-eins-1-kohaerenz-protokoll`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L65, L71, L91. minor (1–3): the omnipresence of AEGIS and LogOS (L65); AEGIS erasing entropic anomalies in a data centre (L71); AEGIS's sensor network scanning Kael (L91).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L81. minor (1–3): AEGIS erasing „entropische Anomalien“ deep inside a data block (L71).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L33, L43, L49, L57. minor (1–3): the image of Juna materialising on the wall, flawless but artificial (L33, L35); „Statusbericht Kael“ (L37) and the synchronisation with LogOS (L43); the image flickering, another desperate face behind it, the voice breaking (L49, L51).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L17, L23, L27, L29, L37, … (18 lines). central (3–5): Kael waking as „reines, körperloses Gewahrsein“ (L15); the impulse to scratch the perfection suppressed by „Logische Korrektur“ (L27, L29); the rehearsed status report (L39); the wave of longing and grief at the word LogOS (L45, L47); the „Manager-Anteil“ translating the anomaly into logic (L85); „Er war eine Komponente.“ (L95) and the splintering glass inside (L97).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L61, L67. minor (1–3): the transit corridor of the Konstrukt-Stadt as a triumph of determinism (L61); its outer world of fractal geometry and crystalline towers (L67, L69).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L43, L45, L65, L89. minor (1–3): „Synchronisation mit LogOS erfolgt.“ (L43); the grief striking at the syllable LogOS (L45); the omnipresence of AEGIS and LogOS in the routed traffic (L65); „LogOS war unfehlbar.“ (L89).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitch` alone on L87. minor (1–3): „Ein Riss in der Realität.“ (L77): an organic form materialising and being deleted (L79–L83); the inner voice calling it a „Glitch“ (L87); the Risse running deep in Kael's own foundation (L93).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `komponente-734`: `Komponente` (near `komponente734`). `Komponente` (L95, „Er war eine Komponente.“) names no number — not read on komponente-734.


**Pages not read:** `komponente-734` — an occurrence.

**Record entries:** none.

**Not promoted:** Logische Korrektur, Systeminterferenz, Transitkorridor, Zuteilungs-Hub and the draft's other places; `Uncanny Valley`.

**One reader**: kael, juna, logos, aegis, konstrukt-stadt, entropie, risse.

**Chapter readings** (batch `ingest-395-kap`, file `Plan/runs/ingest-395-kap/readings/kap-01--kapitel-eins-1-kohaerenz-protokoll.md`):
- **`kap-01`**: the draft „Kapitel Eins – Der Kristalline Käfig“ (L11): Kael waking in a sterile room (L13–L25), Juna's image demanding a status report (L33–L43), grief at the word LogOS and Juna's image breaking (L45–L51), the transit through the Konstrukt-Stadt (L61–L71), a Riss with an organic form deleted (L77–L83), and the closing sound of splintering glass (L97). A draft, not the chapter as approved.
