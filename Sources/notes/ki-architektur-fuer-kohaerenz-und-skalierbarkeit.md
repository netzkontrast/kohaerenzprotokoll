---
source: Sources/drive/ki-architektur-fuer-kohaerenz-und-skalierbarkeit.md
read: "2026-10-12, the whole document (L1 to L348) through read.py with line numbers, by a document-reader subagent (Sonnet)"
stance_markers: ["postuliert", "schlagen wir"]
stance_marker_count: 3
reads_as: "a proposal report on an external knowledge architecture that keeps generated stories consistent, with a design, role tables and a reference list"
---

# Note — KI-Architektur für Kohärenz und Skalierbarkeit

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible and the claim rests on the lines or counts it names. The document speaks as a proposing report, and much of its content is reported research, which the note marks as the cited source's.

## 1 · What kind of text this is, and how it marks itself

- The document announces its thesis in the first person plural of a report: „Dieser Bericht postuliert den Übergang zu einer“ ^[L17]. The verb `postuliert` ^[ki-architektur-fuer-kohaerenz-und-skalierbarkeit.md:#1] stands once.
- It marks its role table as its own proposal: „schlagen wir folgende Rollenverteilung vor“ ^[L188], and the phrase `schlagen wir` ^[ki-architektur-fuer-kohaerenz-und-skalierbarkeit.md:#2] stands twice.
- It says how it was built: „Wir synthetisieren Erkenntnisse aus über 120 Forschungsquellen“ ^[L17]. The reference list holds 45 entries, each with an access date: `Zugriff am Januar` ^[ki-architektur-fuer-kohaerenz-und-skalierbarkeit.md:#45].
- **Observed:** the document has no chapter of a novel, no figure and no place of a story; `Kap` ^[ki-architektur-fuer-kohaerenz-und-skalierbarkeit.md:#0]. Its examples (a dead character, a dragon, an innkeeper) are illustrations of the method, not world content.

## 2 · The problem: drift and the snowball

- The document gives the drift term as the research's: „Es wird in der Forschung als“ ^[L23] `Contextual Feature Drift` named, which the document then describes as a decay of internal representation over long input.
- It gives the length effect with a footnote to its first reference, a paper on the drift: „Je länger die Eingabesequenz, desto schwächer wird die Bindung“ ^[L23].
- It describes a self-reinforcing error in its own heading: „Die Kooperative Falle und der Schneeballeffekt“ ^[L27]. `Schneeballeffekt` stands 3 times (L27, L29, L282).
- The remedy is aimed at the environment, not the model: „Das Ziel ist nicht, das Modell“ ^[L35] cleverer, but to make the environment stricter, as the line goes on.

## 3 · Exogenous truth, correspondence and coherence

- The document makes the story's database the stand-in for reality: „Die Lösung liegt in einer Hybridisierung“ ^[L49].
- It describes what that does to the check: „Diese Verschiebung ermöglicht den Einsatz deterministischer Validierungsmechanismen“ ^[L51].
- The term `Exogenen Ontologie` ^[ki-architektur-fuer-kohaerenz-und-skalierbarkeit.md:#1] stands once (L49); `Source of Truth` ^[ki-architektur-fuer-kohaerenz-und-skalierbarkeit.md:#4] stands 4 times.
- `Korrespondenztheorie` and `Kohärenztheorie` are borrowed from philosophy and applied to fiction, in the heading „Korrespondenztheorie vs. Kohärenztheorie in der KI“ ^[L41].

## 4 · Formstabilisierung and the Vortex cycle

- The document gives the concept to a named architecture and not to itself: „wie er im Kontext der Vortex-Architektur diskutiert wird“ ^[L55]. The cycle (Druck, Entscheidung, Leap, Stabilisierung) is reported in the same passage; the later table names five phases, and its fifth is `Schwerkraft (Gravity)` ^[ki-architektur-fuer-kohaerenz-und-skalierbarkeit.md:#1].
- The text states what happens without the stabilising step: „Ohne diesen Stabilisierungsschritt bleibt jede Generierung flüchtig und anfällig für Entropie“ ^[L64].
- **Observed:** the cycle has four steps in the list (L59 to L62) and five phases in Tabelle 2 (L296 to L300). The document does not say it changes the count; the fifth phase, Schwerkraft, stands in the earlier prose as the effect of the form (L55).

## 5 · The roles and the shared board

- The agent roles are the document's proposal: `Der Direktor (Orchestrator)`, `Der Ontologe (Knowledge Keeper)`, `Die Autoren (Specialists)`, `Der Kritiker (Evaluator)` stand as table cells in L193 to L196.
- It names a shared state board, citing its source: „Die Kommunikation zwischen diesen Agenten sollte nicht nur über Textnachrichten erfolgen“ ^[L200]; the board is `Pulsar Field`, in the heading at L198.
- Conflict between agents is reported as a research finding: „Interessanterweise zeigen Forschungen“ ^[L204], and the proposal drawn from it follows: „Das System sollte daher“ ^[L204] allow `Productive Friction`.

## 6 · The enforcement and the human's place

- The validation cycle replaces a human role: „Dieser Zyklus ersetzt den menschlichen Editor“ ^[L236].
- Candidate facts are made canonical by confidence: „Nur Fakten mit hoher Bestätigung werden“ ^[L262] canonical.
- The conclusion changes the language model's role: „Das LLM wird vom“ ^[L272] author to renderer.

## 7 · Said two ways, or left open — recorded, not resolved

- **Observed:** the human is a "source of truth" that cannot scale (L15, L33) and in Tabelle 1 the human's role in the target architecture is architect of the ontology and meta director (L283); the document does not reconcile the two statements.
- **Observed:** SHACL is introduced with a code example whose export is flattened (L126 to L143); the rule it shows cannot be quoted as written.

## 8 · The document's standing

- The closing claim is absolute: „Dies ist der einzige Weg, um komplexe, langlebige narrative Universen zu schaffen“ ^[L272]. Recorded as the document's claim of its own standing, never applied.
- The conclusion is also a claim about the field: „Die hier skizzierte Architektur markiert das Ende des“ ^[L270] prompt engineering.

## 9 · Absent, counted

- The document names no chapter (`Kap` ^[ki-architektur-fuer-kohaerenz-und-skalierbarkeit.md:#0]); `Kapitel` ^[ki-architektur-fuer-kohaerenz-und-skalierbarkeit.md:#1] stands once, for its own chapters (L104).
- The census counts 0 zeros among its 53 candidates.
