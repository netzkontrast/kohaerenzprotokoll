---
source: Sources/drive/research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md
read: "2026-10-11, the whole document (L1 to L1211) through read.py with line numbers, a light pass; by a document-reader subagent (Sonnet)"
stance_markers: ["Restatement Checkpoint", "Reflection Entry", "Example trigger in this research context"]
stance_marker_count: 26
reads_as: "a research prompt, instructions to an executing AI agent: a compact primer of the novel's architecture, a design contract (T1 to T7) and a long method scaffold"
---

# Note — research-prompt_dual-storyform-rebuild-kohaerenz-protokoll.md

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **Observed**, no quotation is possible and the claim rests on the lines it names. The document is instructions to another agent and speaks in the imperative; the few passages that state the novel's world are the Compact Primer (L347 to L399), and the note reports those as the prompt's own report of the project's architecture.

**Light pass.** The note harvests only what the prompt asserts about the novel's world, its cast and its two storyforms: stated canon, hypotheses, constraints. The method sections were left out on purpose: the critical-thinking method blocks (Falsification, Contrast Classes, Contradiction Log, First-Principles Decomposition, Adversarial Query Expansion), the Reflection Baseline, the step scaffold, the output schema and the checklists. They are instructions on how an agent should work and say nothing about the world; the census keeps their names as the document's own terms, the note does not read them.

## 1 · What kind of text this is, and how it marks itself

- The prompt describes itself: „Dieser Prompt ist selbstcontained“ ^[L44].
- It names the kind of research it asks for: „Diese Forschung ist eine Exploration, keine Extraktion“ ^[L56].
- It marks the sections of its own structure as MAPIT components: „Behandle jede Komponente als harten Vertrag“ ^[L160].
- **Observed:** the prompt marks its repeated labels (`Restatement Checkpoint` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#13], `Reflection Entry` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#9], `Example trigger in this research context` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#4]); these are template labels, not terms of the world.
- It ends: „Ende des Forschungsprompts. Führe jetzt aus.“ ^[L1210]

## 2 · The novel and its question

- The Primer's first bullet gives the genre line and the core question: „Ist Liebe Information — oder das, was Information zerstört?“ ^[L351]
- The ending the Primer gives: „Die Trennung war nie real, ändert nichts am Schmerz“ ^[L351]
- The Primer limits each entry on purpose and says where deeper material sits: „Tieferes Material steht in den NotebookLM-Notebooks“ ^[L347]

## 3 · Cast and world, as the Compact Primer states them

- `Kael` is described as „Fragmentierter Host eines DIS-Systems“ ^[L355].
- `Juna` is described as „algorithmisch irreduzibel, für AEGIS unmodellierbar“ ^[L359], and the same line says of her: „nie als Deus ex Machina, nie physisch beschreibbar“ ^[L359].
- `AEGIS` is described as „Autopoietisches, operativ geschlossenes System“ ^[L363]; the line gives its primary directive as „AEGIS ist, was AEGIS verhindert, dass es nicht ist“ ^[L363].
- The `Moonshine-Link` is described as „Nicht-lokale Verbindung zwischen Kael und Juna“ ^[L367].
- The `Guardians` are described as „vier Sub-Wächter-Instanzen unter AEGIS“ ^[L371]; the same line names `LogOS`, `Mnemosyne`, `Cerberus` and `Kairos/Sophia`.
- The `Kernwelten` are described as „Vier diegetische Schauplätze, jeweils einer Computational-Class zugeordnet“ ^[L375], the four written `KW1` to `KW4`.
- The `Alter-System` line writes each alter joined to a role word, for example `Lex-Rationalist`, `Silas-Juna-Echo` and `Oblivion-AEGIS-Echo`, and gives the groups ANP, EP, Sonder and Spiegel ^[L379]; **Observed:** the single names are not written alone, see section 8.
- The `Dual-Kernel-Theorie` gives the `Roman-Pointe`: „AEGIS hält sich für K1, ist aber K0“ ^[L383].
- The `Physik` bullet says the efficiency measure „misst Suppressionseffizienz, nicht echte Kohärenz“ ^[L387].
- The `Zeit` bullet draws a consequence: „jede atemporale Wahrheit“ ^[L391] survives the erasure.
- The `Wahrheit` bullet: „Roman operiert in Dialetheia-Logik“ ^[L395]; and for the climax, what is true in Storyform A is „funktional inkonsistent“ ^[L395] in Storyform B.

## 4 · The two earlier storyforms, and the prompt's claim about their standing

- The prompt names them `Storyform A` (`Heuristics of Integration`) and `Storyform B` (`Phoenix Collapse`) and says of the existing material: „gilt nicht mehr als Kanon“ ^[L183].
- It calls them „Inspirationsmaterial, keine Vorgabe“ ^[L284].
- The Primer repeats the status: „ein Vorgängermodell, das du adversarial prüfst“ ^[L399].
- It reports the author as having said so: „dass nichts mehr als Kanon gilt“ ^[L331].
- The word `Kanon` stands `Kanon` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#3] times. This is the prompt's own claim about the status of the earlier storyforms, recorded and applied to nothing.
- The first design constraint is headed „Juna ist explizit verankert“ ^[L685]; its row writes the earlier architecture as „Storyform A IC=Juna“ ^[L685] and says Juna's function was there perhaps only weakly realised.

## 5 · What the prompt asks of any new dual storyform: constraints and the author's example

- The author's own example, marked verbatim: „in storyform a zb, wird mind. auf Physik gemapt, und Universe auf Psychology / I auf we, you auf they“ ^[L628].
- The prompt warns against reading that as proof: „Das Beispiel ist ein Datenpunkt, keine Theorie“ ^[L668].
- Of the four candidate mirror axes it names, the perspective-driven one is „das ist das Autor-Beispiel“ ^[L805], with the other three called `Identitäts-Spiegelung`, `Komplementär-Spiegelung` and `Rotations-Spiegelung` ^[L802].
- The design constraint on layering: „Pro Throughline maximal zwei simultane Lesarten“ ^[L687].
- The design constraint on friction: „gleicher Storypoint-Inhalt → gegensätzliche Solution“ ^[L686] is given as an operational example.
- The design constraint on bearers: „Keine ambivalenten Träger“ ^[L689], with the bearers named Kael, Juna, AEGIS and the Guardian collective.
- The climax mechanisms named as examples: „Mnemosyne-Archipel-Konvergenz“ ^[L690].
- `Dual-Mapping` is called „keine Standard-Dramatica-Vokabel“ ^[L508].

## 6 · Output exclusions the prompt sets

- No canonising of any variant: „Eine implizite oder explizite Kanonisierung einer Variante“ ^[L298].
- No political layer: „Der Roman hat explizit keine politische Throughline“ ^[L299].
- No machine rescuer for Juna: „Juna darf nie als Maschine erscheinen, die das Problem von außen löst“ ^[L300].
- Production-level material is out of scope: „Material außerhalb des Scopes“ ^[L286] names the `Suno Album`, the song cycle `The Weight of Why` and the `Memory-Slot-Architektur`.

## 7 · Said two ways, or left open — recorded, not resolved

- **Observed:** the number of candidate mirror rules differs between passages: „Formuliere mindestens drei verschiedene Kandidaten-Spiegelregeln“ ^[L636] against „Formuliere mindestens vier verschiedene Kandidaten-Spiegelregeln“ ^[L798] and the step heading „Mindestens vier Kandidaten-Spiegelregeln“ ^[L784].
- **Observed:** L605 labels the standard architecture with a bold phrase that begins with a digit and the word Throughlines, while its own sentence says „Die Standard-Dramatica-Architektur unterscheidet vier Throughlines“ ^[L605]; the digit label and the sentence give different numbers of throughlines.
- **Observed:** L746 asks for a minimum count of storypoints in the form „Standard-Dramatica-Storypoints, die in jeder Variante festgelegt werden müssen“ ^[L746] and the parenthesis on the same line lists the four throughlines plus four dynamics, which is more than the digit it opens with.
- The output template's last section lists, as examples of what may stay unresolved, „Post-Vortex-AEGIS-Status“ ^[L1160], „Moonshine-Link-Boundary“ ^[L1160] and `Wächter-Zwiespalt-Soziopolitik` ^[L1160]; these are placeholders of the template, not findings.

## 8 · Absent, counted

- `Lex` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#0] and `Silas` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#0] stand zero times alone; each stands once inside a hyphenated compound (see section 3).
- `Kapitel` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] stands once, in the genre line of the Primer.
