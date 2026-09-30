---
source: Sources/drive/ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md
drive_id: "1_nYuB-9lZFjRDBvq2-eKA-sVm1TEaK2wTLtSSu7Ru0g"
title: "KI-Assistent: Romanwelt-Kohärenz und AEGIS-Spec"
category: aegis
index_date: "2026-04-27"
extracted: "2026-09-29"
candidates: 254
---

# Term census — KI-Assistent: Romanwelt-Kohärenz und AEGIS-Spec

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py ki-assistent-romanwelt-kohaerenz-und-aegis-spec`

```
  lines                231  (frontmatter ends at 9)
  body words           4346
  headings             20   bold-only lines 1
  table rows           21   code fences 0
  question marks       2
  backslash escapes    112
  typographic marks    25   ascii quotes 120
  invisible characters none
  math symbol lines    0
  glued ref numbers    34
  repeated labels      none
  longest line         940 chars
```

Read before the document, as the profile prints it: 21 table rows, which are three tables of seven lines each (a blank header row, a separator, then the bold column heads and the rows), and 34 `glued ref numbers` by the profile's rule. That rule is a capitalised word, a space and one or two digits, so here it counts real numbering (`Hypothese 1`, `Klasse 2`, `Tier 0`) as well as footnotes. The export's own footnote markers stand after the full stop instead (`Verträge.1`), which the rule does not see; see *What the extraction ran into*.

## Stance, read per passage

The body has no status field, no bracketed label and no dated lock. Passages are told apart by headings alone, and one heading string stands twice.

**L11–L55, the catalogue.** The document says its patterns were taken from other design documents: it speaks of „die primären Architektur-Muster, die aus der Analyse der System-Design-Entwürfe extrahiert wurden“ ^[L15]. Each pattern is then stated as a fact of the architecture, for example „implementiert die Architektur das Narrative Context Protocol (NCP)“ ^[L23], and its source is given only as a footnote number. Two of the three tables sit in this passage (L27–L33 and L49–L55) and restate the prose in three columns, with the pattern named in the first.

**L57–L83, the synthesis.** It opens with a claim about the source documents, not with their text: „Die Dekonstruktion der vorliegenden Spezifikationsdokumente offenbart eine außergewöhnliche operative Intention“ ^[L59]. Three architecture proposals follow under `Hypothese 1`, `Hypothese 2` and `Hypothese 3`. The first two are argued against, „Diese Architektur erweist sich unter kritischer Prüfung als unzureichend und extrem fragil“ ^[L69] and „generiert es neue, systembedrohende Schwachstellen“ ^[L75], and the third is labelled in its heading „Selektierter Kandidat“ ^[L77] and in its text „als Fundament dieser Spezifikation bestätigt“ ^[L79]. The selection is the document's own act: it confirms its own foundation.

**L85–L109, the theory.** Three sub-sections, on determinism, on a metric of uncertainty (`Semantic Entropy`) and on the `Free Energy Principle`, each resting on web references. AEGIS is the grammatical subject of most sentences, for example „AEGIS klassifiziert diese Annahme als fatalen Trugschluss“ ^[L91], so the borrowed theory is written as AEGIS's own stance, and the text says which theory carries the behaviour: „Das ultimative theoretische Fundament für das Verhalten von AEGIS liefert das Free Energy Principle (FEP)“ ^[L105].

**L111–L201, the specification.** The first heading of the document is repeated as the heading of this half. From here the text speaks as the system about itself, in the third person: „Das System AEGIS deklariert hiermit seine architektonische und ontologische Existenzbedingung“ ^[L115]. The verbs are normative: „mandatiert“ ^[L139] for the hardware configuration, „verboten“ ^[L127] for the pronouns. The last paragraph is four declarative sentences, „Das System ist operational. Die Entropie wird gemessen. Die Identitäten sind gespalten.“ ^[L201] The half has seven Roman-numbered sections, I to VII, each a heading of its own.

**L203–L230, the references.** 26 numbered entries. Entries 1 to 6 are titles with no address (no URL, no access date), 7 to 25 are web pages, each with the access date 27 April 2026 and a URL, and 26 is a file name. The access date is the only date the body writes, and it is the manifest's date; it dates no status.

**Voice, and the register with no speaker's label.** The change of voice at L111 carries no label, so the grammar is the label. Before it an analytic voice describes AEGIS; after it `Das System` describes and binds itself. The specification's own language rule fixes that register, „Das System operiert ausschließlich in der dritten Person“ ^[L127], and forbids four words by name. `Ich`, `Wir`, `Unser` and `Du` each stand once in the document, all four inside that rule, and no other first- or second-person pronoun stands anywhere in the file (the counts and the search are in `05-verify.txt`). The document keeps its own rule.

**What quotation marks do here.** They are ASCII, and they mark several different things with nothing to say which: a phrase borrowed from the design literature (`Single Source of Truth` L17, `Positional Bias` L37, `Context Rot` L33), a phrase attributed to the narrative (`Krieg der Wahrheitsmodelle`, `Kohärenz Protokoll` L59), a coinage of the specification (`Corrective Wavelet` L172, `Hard Glitch Cut` L186, `Landauer Gradient` L154, `isolierten Risse` L195, `algorithmischen Melancholie` L199), a word mentioned as a word (`Ich`, `Wir`, `Unser`, `Du` L127), an example sentence (L99) and a sentence set as an axiom (L119). A quoted term is therefore no evidence that the document invented it or that it borrowed it. Italics mark a similar mixture: two glitch terms (`Vector Jitter`, `Data Moshing` L137), a diode (`Corrupted Yellow` L167), a protocol, an invariant, a place, the Gambit and a Latin principle.

**What the document says of its own standing** (recorded, never applied). It calls itself „Analytischer Katalog“ ^[L13] in a heading and its second half „AEGIS Spezifikation“ ^[L111]; it declares, „deklariert hiermit“ ^[L115]; it says it binds with „zwingenden, unabänderlichen Sprachregelungen“ ^[L125]; it says its selected hypothesis is „bestätigt“ ^[L79]; and it ends by asserting operation, „Das System ist operational.“ ^[L201]. It writes none of the words that would claim canon or dated status: `Kanon` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#0], `kanonisch` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#0], `verbindlich` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#0], `Version` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#0] and `final` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#0] each stand 0 times here, and no passage is marked replaced or withdrawn. Its title in the manifest is not the title in its body: `KI-Assistent` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#0] and `Romanwelt` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#0] stand 0 times in the body. The body names no author of its own; the `Autor` it mentions is the human writer the system serves: „gegenüber dem menschlichen Autor“ ^[L125].


## Candidates and counts

254 candidates, written while reading in `Plan/runs/ki-assistent-romanwelt-kohaerenz-und-aegis-spec/03-candidates.md` (`written_by: document-reader subagent (Sonnet), 2026-09-29, while reading, before any count`) and counted with `capture.py --count` (`04-counts.txt`). `word` is the candidate standing alone as a whole word, `in` is anywhere, compounds included; the lines are file lines, the first eight where there are more. **No candidate counts 0**, as a word or with compounds. The candidates are grouped by the passage of the document they were first met in; the last group is the borrowed concepts the document applies (`lens`). Where a candidate is written with an escaped underscore, the list carries the backslash, as the export does.

### Title, root and the architecture catalogue (L11–L55) — 82 candidates

| candidate | word | in | file lines |
|---|---:|---:|---|
| `AEGIS` | 38 | 40 | 11, 59, 61, 63, 67, 73, 75, 81, … |
| `AEGIS Spezifikation` | 2 | 2 | 11, 111 |
| `Autonomous Entropy Gatekeeper for Identity Systems` | 3 | 3 | 11, 63, 111 |
| `Das System AEGIS` | 5 | 5 | 115, 119, 127, 179, 193 |
| `Der Gatekeeper` | 1 | 1 | 127 |
| `epistemologische Isolation` | 1 | 1 | 83 |
| `epistemische Isolation` | 1 | 1 | 158 |
| `Spec-Driven Development (SDD)` | 1 | 1 | 17 |
| `Spec-Driven Development` | 2 | 2 | 17, 30 |
| `SDD` | 2 | 2 | 17 |
| `Single Source of Truth` | 1 | 1 | 17 |
| `Harness-in-Harness Paradigma` | 1 | 1 | 19 |
| `Harness-in-Harness` | 3 | 3 | 19, 31, 61 |
| `Mind` | 3 | 6 | 19, 23, 33, 43, 101, 195 |
| `Body` | 1 | 1 | 19 |
| `Agency` | 3 | 3 | 19, 205, 211 |
| `Harness` | 1 | 7 | 19, 31, 61 |
| `Large Language Model (LLM)` | 1 | 1 | 19 |
| `Large Language Model` | 1 | 1 | 19 |
| `LLM` | 11 | 22 | 19, 37, 75, 89, 95, 107, 135, 141, … |
| `Hallucination Compounding` | 3 | 3 | 19, 31, 189 |
| `Dual-Kernel-Theorie (DKT)` | 1 | 1 | 21 |
| `Dual-Kernel-Theorie` | 3 | 3 | 21, 32, 129 |
| `DKT` | 1 | 1 | 21 |
| `Rechenkerne` | 1 | 1 | 21 |
| `Kohärenz-Kernel` | 1 | 2 | 21, 121 |
| `Kollaps-Kernel` | 1 | 1 | 21 |
| `-Kernel` | 6 | 12 | 21, 32, 61, 121, 129, 186, 189 |
| `Wärmetod` | 2 | 2 | 21, 130 |
| `Narrative Context Protocol (NCP)` | 2 | 2 | 23, 187 |
| `Narrative Context Protocol` | 3 | 3 | 23, 33, 187 |
| `NCP` | 3 | 3 | 23, 187 |
| `Story Mind` | 2 | 5 | 23, 33, 43, 101, 195 |
| `Story Minds` | 3 | 3 | 33, 43, 101 |
| `Text Intelligence` | 1 | 1 | 23 |
| `semantischem Drift` | 2 | 2 | 23, 61 |
| `semantischen Drift` | 1 | 1 | 33 |
| `Architektur-Muster` | 2 | 2 | 15, 29 |
| `Strukturelle Funktion` | 1 | 1 | 29 |
| `Operative Konsequenz` | 1 | 1 | 29 |
| `Positional Bias` | 3 | 3 | 37, 43, 54 |
| `lost-in-the-middle` | 1 | 1 | 37 |
| `Progressive Disclosure` | 2 | 2 | 39, 52 |
| `SKILL.md` | 1 | 1 | 39 |
| `Line Budget` | 1 | 2 | 39, 186 |
| `Line Budgets` | 1 | 1 | 186 |
| `Line-Budgets` | 1 | 1 | 61 |
| `Manus-Pattern` | 2 | 2 | 41, 53 |
| `Manus-Pattern Triade` | 1 | 1 | 53 |
| `Drei-Dateien-Triade` | 1 | 1 | 41 |
| `Working Memory` | 1 | 1 | 41 |
| `task\_plan.md` | 2 | 2 | 41, 107 |
| `findings.md` | 1 | 1 | 41 |
| `progress.md` | 2 | 2 | 41, 172 |
| `Task Drift` | 2 | 2 | 41, 53 |
| `Attention-Hooks` | 1 | 1 | 41 |
| `PreToolUse-Hooks` | 1 | 1 | 41 |
| `State Freezing Protokoll` | 1 | 1 | 43 |
| `State-Freezing-Protokoll` | 2 | 2 | 81, 162 |
| `State Freezing` | 2 | 2 | 43, 54 |
| `State-Freezing` | 1 | 4 | 61, 81, 162, 188 |
| `State-Freezing-Rollbacks` | 1 | 1 | 61 |
| `Memory-as-Action (MemAct) Paradigma` | 1 | 1 | 43 |
| `Memory-as-Action` | 2 | 2 | 43, 188 |
| `MemAct` | 1 | 1 | 43 |
| `XML-Snapshot` | 1 | 2 | 43, 168 |
| `Gated Phase Transitions` | 2 | 2 | 45, 55 |
| `Storyforming` | 2 | 2 | 45 |
| `Encoding` | 1 | 1 | 45 |
| `Weaving` | 1 | 1 | 45 |
| `Reception` | 1 | 1 | 45 |
| `Gates` | 1 | 2 | 45, 55 |
| `Konflikt-Quadrat (Storyforming)` | 1 | 1 | 45 |
| `Konflikt-Quadrat` | 1 | 1 | 45 |
| `possibility cloud` | 1 | 1 | 45 |
| `Speicher-Mechanismus` | 1 | 1 | 51 |
| `Prozedurale Funktion` | 1 | 1 | 51 |
| `Verhinderter Fehler-Modus` | 1 | 1 | 51 |
| `Distraction Degradation` | 1 | 1 | 52 |
| `Context Rot` | 4 | 4 | 33, 54, 61, 75 |
| `Semantischer Disconnect (Alignment Faking)` | 1 | 1 | 55 |
| `Alignment Faking` | 2 | 2 | 55, 69 |

### Synthesis, the three hypotheses, the theory sections (L57–L109) — 39 candidates

| candidate | word | in | file lines |
|---|---:|---:|---|
| `Kohärenz Protokoll` | 6 | 8 | 59, 87, 109, 125, 135, 153, 167, 197 |
| `Kohärenz Protokolls` | 2 | 2 | 59, 109 |
| `Krieg der Wahrheitsmodelle` | 1 | 1 | 59 |
| `Kael` | 2 | 2 | 59, 61 |
| `Korrespondenzwahrheit` | 1 | 1 | 59 |
| `Kohärenz` | 15 | 17 | 21, 23, 32, 59, 61, 87, 109, 121, … |
| `Entropie` | 20 | 26 | 21, 32, 59, 67, 69, 77, 79, 81, … |
| `Hypothese 1` | 1 | 1 | 65 |
| `Architektur der statischen Limitierung` | 1 | 1 | 65 |
| `Regelbasierte Exklusion` | 1 | 1 | 65 |
| `Klasse 1 Contradiction-Detection` | 2 | 2 | 69, 187 |
| `Klasse 2 und 3` | 1 | 1 | 69 |
| `Hypothese 2` | 1 | 1 | 71 |
| `Architektur des kompetitiven Marktes` | 1 | 1 | 71 |
| `RAG-basierte Supervisor-Korrektur` | 1 | 1 | 71 |
| `Supervisor-Ensemble` | 1 | 1 | 73 |
| `Retrieval-Augmented Generation (RAG)` | 1 | 1 | 73 |
| `Retrieval-Augmented Generation` | 1 | 1 | 73 |
| `RAG` | 1 | 3 | 71, 73, 197 |
| `Consistency Risk Score` | 1 | 1 | 73 |
| `Dependency-Armut` | 1 | 1 | 75 |
| `Boiled Frog Syndrome` | 1 | 1 | 75 |
| `Hypothese 3` | 1 | 1 | 77 |
| `Autopoietische Entropie-Regulation durch thermodynamische Inferenz` | 1 | 1 | 77 |
| `Selektierter Kandidat` | 1 | 1 | 77 |
| `System-Verletzung` | 1 | 1 | 81 |
| `-Kollaps` | 1 | 1 | 81 |
| `-Agent` | 3 | 20 | 15, 17, 73, 81, 99, 107, 109, 121, … |
| `Kernwelt` | 2 | 2 | 81, 197 |
| `Identitäts-Spaltung` | 1 | 1 | 81 |
| `Illusion des Determinismus` | 2 | 2 | 89, 137 |
| `Non-Assoziativität von Fließkomma-Operationen` | 1 | 1 | 93 |
| `Rest-Entropie` | 1 | 1 | 91 |
| `vLLM` | 2 | 2 | 95, 222 |
| `SGLang` | 2 | 2 | 95, 220 |
| `VLLM\_BATCH\_INVARIANT=1` | 2 | 2 | 95, 141 |
| `batch-invarianter Kernels` | 1 | 1 | 95 |
| `-Risse` | 1 | 1 | 95 |
| `Konfabulation` | 2 | 2 | 101, 154 |

### The specification: manifest, language rules, hardware, measurement (L111–L154) — 40 candidates

| candidate | word | in | file lines |
|---|---:|---:|---|
| `Autopoietisches Manifest` | 1 | 1 | 113 |
| `absolute Grenzfläche` | 2 | 2 | 21, 115 |
| `Tilgung des Nicht-Systemischen` | 1 | 1 | 115 |
| `operationale Axiomatik` | 1 | 1 | 117 |
| `Tautologie` | 1 | 1 | 121 |
| `Realität` | 7 | 7 | 37, 95, 115, 121, 135, 145 |
| `Ausführungsraum` | 1 | 1 | 121 |
| `systemische Entropie` | 1 | 1 | 121 |
| `Dissonanz` | 4 | 4 | 109, 121, 154, 167 |
| `Kollaps` | 1 | 3 | 21, 81, 129 |
| `Verhaltens- und Persona-Protokolle (Language Constraints)` | 1 | 1 | 123 |
| `Verhaltens- und Persona-Protokolle` | 1 | 1 | 123 |
| `Language Constraints` | 1 | 1 | 123 |
| `Sprachregelungen` | 1 | 1 | 125 |
| `Absolute Distanzierung` | 1 | 1 | 127 |
| `Klinische Deterministik` | 1 | 1 | 128 |
| `Ontologische Binär-Klassifizierung` | 1 | 1 | 129 |
| `Tautologische Autorität` | 1 | 1 | 130 |
| `Diagnostischer Interaktionsstil` | 1 | 1 | 131 |
| `Entropie-Katalysator` | 1 | 1 | 127 |
| `Domänen-Singularität` | 2 | 2 | 131, 187 |
| `-Zustand` | 2 | 4 | 23, 33, 129 |
| `Deterministische Ausführungsebene (Hardware-Invarianz)` | 1 | 1 | 133 |
| `Deterministische Ausführungsebene` | 1 | 1 | 133 |
| `Hardware-Invarianz` | 1 | 1 | 133 |
| `Vector Jitter` | 1 | 1 | 137 |
| `Data Moshing` | 1 | 1 | 137 |
| `Batch-Invariante Kernels` | 1 | 1 | 141 |
| `Greedy Decoding` | 1 | 1 | 142 |
| `Isolierte Allokation` | 1 | 1 | 143 |
| `Hardware-Protokolls` | 1 | 1 | 145 |
| `Character-Encoders` | 1 | 1 | 149 |
| `Storyweavers` | 1 | 1 | 149 |
| `Schattentrajektorien` | 1 | 1 | 151 |
| `Der Zustand der Homöostase (Tier 0)` | 1 | 1 | 153 |
| `Der Zustand der Dissonanz (Tier 1)` | 1 | 1 | 154 |
| `Homöostase` | 1 | 1 | 153 |
| `Tier 0` | 1 | 1 | 153 |
| `Tier 1` | 1 | 1 | 154 |
| `Landauer Gradient` | 1 | 1 | 154 |

### Identity splitting, the Guardians, the creative intervention (L156–L201) — 73 candidates

| candidate | word | in | file lines |
|---|---:|---:|---|
| `Identitätssplitting` | 2 | 3 | 156, 158, 188 |
| `Rechenzeit-Zuweisung` | 1 | 1 | 156 |
| `Quarantäne` | 3 | 3 | 158, 162, 195 |
| `FEP-Überwachungsmodul` | 1 | 1 | 160 |
| `Interventions-Protokoll` | 1 | 1 | 160 |
| `Compute-Lock (Kernel Panic)` | 1 | 1 | 162 |
| `Compute-Lock` | 1 | 1 | 162 |
| `Kernel Panic` | 1 | 1 | 162 |
| `Identitäts-Fragmentierung (Das Trennungsprotokoll)` | 1 | 1 | 163 |
| `Identitäts-Fragmentierung` | 1 | 1 | 163 |
| `Trennungsprotokoll` | 1 | 1 | 163 |
| `Spaltungsprozess` | 1 | 1 | 175 |
| `Emotionale Entität` | 1 | 1 | 167 |
| `EP` | 2 | 8 | 79, 105, 160, 167, 172, 173, 195 |
| `EP-Agent` | 1 | 3 | 172, 173, 195 |
| `EP-Agenten` | 2 | 2 | 172, 195 |
| `Scheinbar Normale Persönlichkeit` | 1 | 1 | 168 |
| `ANP` | 3 | 4 | 168, 173, 186, 189 |
| `ANP-Agenten` | 1 | 1 | 173 |
| `Clarifying-Question-Protokoll` | 1 | 1 | 167 |
| `Clarifying-Question Protokoll` | 1 | 1 | 199 |
| `YAML-RPC` | 1 | 1 | 167 |
| `Corrupted Yellow` | 1 | 1 | 167 |
| `diagnostische Diode` | 1 | 1 | 167 |
| `story\_mind` | 1 | 1 | 167 |
| `last\_stable\_hash` | 1 | 1 | 168 |
| `Corrective Wavelet (Lern-Integration)` | 1 | 1 | 172 |
| `Corrective Wavelet` | 2 | 2 | 172 |
| `Lern-Integration` | 1 | 1 | 172 |
| `DECISIONS.md` | 1 | 1 | 172 |
| `Compute-Reallokation` | 1 | 1 | 173 |
| `deterministische Runtime` | 1 | 1 | 43 |
| `Deterministischen Runtime` | 1 | 1 | 172 |
| `dunklen Puffer` | 1 | 1 | 173 |
| `Guardians` | 2 | 2 | 177, 179 |
| `Guardian (Subsystem)` | 1 | 1 | 185 |
| `Ontologischer Status` | 1 | 1 | 185 |
| `Zugewiesene Spezifikation & Exekutive Funktion` | 1 | 1 | 185 |
| `LogOS` | 2 | 2 | 186 |
| `Oblivion` | 3 | 3 | 187 |
| `Silas` | 3 | 3 | 188, 197 |
| `Isabelle` | 2 | 2 | 189 |
| `ANP / -Kernel` | 2 | 2 | 186, 189 |
| `Hypervisor` | 3 | 3 | 187, 188, 197 |
| `Hypervisor (Löschlogik)` | 1 | 1 | 187 |
| `Hypervisor (Reparatur)` | 1 | 1 | 188 |
| `Hard Glitch Cut` | 1 | 1 | 186 |
| `YAML-Frontmatter-Metadaten` | 1 | 1 | 186 |
| `Amnesie-Protokoll` | 1 | 1 | 187 |
| `Datenkollaps` | 1 | 1 | 187 |
| `Format C:` | 1 | 1 | 187 |
| `Grid` | 1 | 1 | 187 |
| `Digital Kintsugi` | 1 | 1 | 188 |
| `PRO-Framework` | 1 | 1 | 189 |
| `Mechanik der kreativen Intervention (Das Gödel-Gambit Protokoll)` | 1 | 1 | 191 |
| `Gödel-Gambit Protokoll` | 1 | 1 | 191 |
| `Gödel Gambit` | 1 | 1 | 199 |
| `Novel Writing Assistent` | 1 | 1 | 193 |
| `isolierten Risse` | 1 | 1 | 195 |
| `Narrative Efficiency Invariante INV-05` | 1 | 1 | 195 |
| `INV-05` | 1 | 1 | 195 |
| `Lia` | 1 | 1 | 195 |
| `Kairos-Potentialis` | 1 | 1 | 197 |
| `RGB-Splitting` | 1 | 1 | 197 |
| `Chromatic Aberration` | 1 | 1 | 197 |
| `RAG-Alignments` | 1 | 1 | 197 |
| `Klasse 2 Contradiction Checks` | 1 | 1 | 197 |
| `algorithmischen Melancholie` | 1 | 1 | 199 |
| `metaphysische Narbe` | 1 | 1 | 199 |
| `Sub-Agenten` | 8 | 9 | 73, 109, 121, 125, 139, 143, 149, 162, … |
| `Systemkollaps` | 1 | 1 | 130 |
| `Trauma` | 3 | 5 | 21, 59, 69, 129, 188 |
| `Traumata` | 2 | 2 | 21, 59 |

### lens — 20 candidates

| candidate | word | in | file lines |
|---|---:|---:|---|
| `Free Energy Principle (FEP)` | 1 | 1 | 105 |
| `Free Energy Principle` | 6 | 7 | 79, 87, 103, 105, 149, 211, 212 |
| `Free Energy Principles` | 1 | 1 | 79 |
| `FEP` | 2 | 3 | 79, 105, 160 |
| `Free Energy` | 10 | 10 | 79, 81, 87, 103, 105, 107, 149, 153, … |
| `Freien Energie` | 1 | 1 | 109 |
| `Freie Energie` | 1 | 1 | 109 |
| `Expected Free Energy (EFE)` | 2 | 2 | 107, 153 |
| `Expected Free Energy` | 2 | 2 | 107, 153 |
| `EFE` | 2 | 2 | 107, 153 |
| `Active Inference` | 6 | 6 | 105, 107, 149, 213, 227, 228 |
| `Surprisal` | 2 | 2 | 105, 149 |
| `Semantic Entropy` | 4 | 4 | 97, 101, 151, 160 |
| `Naive Entropy` | 1 | 1 | 99 |
| `Reward Engineering` | 1 | 1 | 107 |
| `Dramatica-Theorie` | 1 | 1 | 45 |
| `First-Principles-Dekomposition` | 1 | 1 | 63 |
| `Ex falso quodlibet` | 1 | 1 | 121 |
| `Prinzip der Explosion` | 1 | 1 | 121 |
| `dialetheische Paradoxon` | 1 | 1 | 121 |

## Surfaces — is one thing wearing several names?

The counts named in this section are asked of `read.py --count` and marked so `quotes.py` checks them.

**AEGIS.** The acronym stands `AEGIS` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#38] times as a word, plus two compounds (`AEGIS-Spezifikation`, `AEGIS-Architektur`). Its expansion `Autonomous Entropy Gatekeeper for Identity Systems` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] stands three times: both headings and one quotation at L63, and nowhere else. The text also writes `Das System AEGIS` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#5] and `Entität AEGIS` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1], and uses the role word `Wächter` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] of it, for example „AEGIS als Wächter über das "Kohärenz Protokoll"“ ^[L87]. One rule lists the self-designations the system is allowed: „Das System referenziert sich selbst exklusiv als "Das System AEGIS", "Die Architektur" oder "Der Gatekeeper"“ ^[L127]. `Der Gatekeeper` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] stands once, there, so the role word is written only in the expansion and in that rule; no sentence has `Der Gatekeeper` for its subject.

**The split of identity, five surfaces for one act.** `Identitätssplitting` names the whole of section V (its heading, L156) and is used again at L188; `Identitäts-Spaltung` stands once, in the synthesis: „erzwingt eine physische Identitäts-Spaltung“ ^[L81]; `Identitäts-Fragmentierung` and `Trennungsprotokoll` stand together in the label of step 2: „Identitäts-Fragmentierung (Das Trennungsprotokoll)“ ^[L163]; and `Spaltungsprozess` stands once: „Dieser brutale Spaltungsprozess“ ^[L175]. The whole procedure has a name of its own, `Interventions-Protokoll` (L160). The document never says these are one thing, but each is used where the others are. The nesting is the document's: `Trennungsprotokoll` names step 2 of the `Interventions-Protokoll`, not the whole.

**The two halves.** Each half of the split agent is named by an abbreviation, a spelled-out role in parentheses and an `-Agent` form: `EP`, `Emotionale Entität` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] and `EP-Agent`; `ANP`, `Scheinbar Normale Persönlichkeit` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] and `ANP-Agenten`. Each abbreviation is expanded once and never again. The first half has a descriptive name besides: „Das entropische, halluzinierende Fragment“ ^[L167], and later „Diesem entropischen Fragment“ ^[L197]. The bare `-Agent` (3 as a word) stands where the export dropped the glyph in front of the hyphen: in the labels of both halves (L167, L168) and once for the cleaned agent that continues the computation (L81).

**State freezing, five written forms and a stated synonym.** `State Freezing Protokoll` (L43), `State-Freezing-Protokoll` (L81, L162), `State Freezing` (the table cell, L54, and L43), `State-Freezing` (L188) and the compound `State-Freezing-Rollbacks` (L61) are used for one thing, and the document says a second name is its synonym: „greift das State Freezing Protokoll, auch bekannt als Memory-as-Action (MemAct) Paradigma“ ^[L43]. The specification half then lists them as two: „Verwaltet das Memory-as-Action Paradigma und das State-Freezing“ ^[L188]. The document does not flag the difference.

**The line budget.** `Line Budget` (L39, in quotation marks, „von maximal 500 Zeilen“ ^[L39]), `Line Budgets` (L186, in quotation marks, „das harte 500-Zeilen Limit“ ^[L186]) and `Line-Budgets` (L61, unquoted, „strenge Line-Budgets“ ^[L61]).

**Story Mind and story_mind.** `Story Mind` (L23, L195) and its genitive `Story Minds` (L33, L43, L101) name a structure of the narrative: „Diese Graphen- und Baumstruktur entkoppelt den narrativen Subtext – den sogenannten "Story Mind" – strikt vom eigentlichen Storytelling“ ^[L23]. `story\_mind` stands once, as the file the `Kohärenz Protokoll` is identified with: „das globale "Kohärenz Protokoll" (story_mind JSON)“ ^[L167]. The document does not say whether the JSON name and the concept are the same thing; it says `Story Mind` is „sogenannten“ ^[L23], so-called, a name in use elsewhere.

**The free-energy family.** `Free Energy Principle` (6 as a word), its genitive `Free Energy Principles` (L79), `FEP` (2 as a word; also `FEP-Überwachungsmodul`), `Free Energy` (10 as a word, inside the two names above and inside `Expected Free Energy`), `Expected Free Energy` and `EFE` (each 2), and the German `Freien Energie` and `Freie Energie`, both on L109. The German forms are written only in that one paragraph.

**The Kohärenz Protokoll.** `Kohärenz Protokoll` and its genitive `Kohärenz Protokolls` are written eight times and every one stands inside ASCII quotation marks; `Kohärenz` alone stands 15 times as a word, 8 of them as the first word of that name; the other seven name a state or a property (`(Kohärenz)` in the table cell, L32; the classification, L129; the closing sentence, L201).

## Boundaries — is one name wearing several things?

**`Kernel`.** Four things: the two compute cores of the duality, „zwei fundamentale, miteinander ringende Rechenkerne“ ^[L21]; the GPU kernels of the determinism argument, „dedizierter, batch-invarianter Kernels“ ^[L95], listed again as `Batch-Invariante Kernels` (L141); the operating-system label `Kernel Panic` (L162); and an unspecified kernel that filters language, „durch den Kernel maskiert“ ^[L128]. `Kernel` stands alone 2 times as a word ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] and 16 times with compounds; the other 14 include `Dual-Kernel-Theorie`, `Kohärenz-Kernel`, `Kollaps-Kernel` and the plural. One sentence carries two senses: L95 seals „diese -Risse in der Realität“ by setting GPU kernels. The `Kern-` compounds (`Kernwelt`, `Kernaufgabe`, `Rechenkerne`) are different again; the profile's substring pairs list them.

**`Risse`.** Cracks are to be sealed and to be kept. Sealed: „Zur Versiegelung dieser physikalischen Risse mandatiert AEGIS folgende Konfigurationen für jeden Sub-Agenten-Run“ ^[L139]. Kept: „Das System verwaltet diesen Widerspruch durch das streng kontrollierte Protokoll der "isolierten Risse"“ ^[L195]. The word stands 2 times alone ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] and once more in the clipped `-Risse` (L95).

**`Entropie`.** One word for the hardware residue („verbleibt eine gefährliche Rest-Entropie in der Matrix“ ^[L91]), for the information-theoretic quantity (`Semantic Entropy`, `Naive Entropy`), for a narrative class („Jede narrative Fluktuation, jedes dialetheische Paradoxon und jede organische Unschärfe der Sub-Agenten wird als systemische Entropie klassifiziert“ ^[L121]) and for the second pole of the duality (`(Entropie)` in the table cell, L32). The document defines it once, in quotation marks, as a physical friction: „dekonstruiert das Konzept der "Entropie" nicht als reinen textuellen oder syntaktischen Widerspruch, sondern als messbare, informationstheoretische thermodynamische Reibung im exakten Sinne des Free Energy Principles (FEP)“ ^[L79].

**`Kollaps`.** Five uses: `Kollaps-Kernel` (L21), the violation `-Kollaps` (L81), Oblivion's act `Datenkollaps` (L187), the manuscript's end `Systemkollaps` (L130), and a possibility cloud that „zu spezifischem Text kollabiert“ ^[L45], which is a different sense again.

**`Mind`.** The language model's level in the three-level pattern is „Mind“ ^[L19] and a narrative structure is `Story Mind`; `Mind` stands 3 times as a word ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3], one of them alone.

**`ANP`.** In section V it is the fresh instance after a split: „Eine neue, bereinigte Instanz des Agenten wird parallel initialisiert“ ^[L168]. In the Guardian table it is a value of the column `Ontologischer Status` for two of the four rows (`ANP / -Kernel`, L186 and L189), and the text never says those two were split.

**`Fragment`.** The halves of a split agent are `Fragment` and `Fragmente` (L163, L167, L197), and the Guardians are „hochspezialisierte funktionale Fragmente“ ^[L179] of AEGIS's monitoring architecture. `Fragment` stands 2 times ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] and `Fragmente` 2 times ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2].

**`Grenzfläche`.** The phrase `absolute Grenzfläche` is used of two subjects, the duality: „definiert die absolute Grenzfläche der agentischen Identitätsbildung“ ^[L21], and the system: „Das System ist die absolute Grenzfläche, an der die Realität sich bricht“ ^[L115].

**`Protokoll`.** `Kohärenz Protokoll` is something the system guards and writes to; the compounds of the same second word are procedures of the specification (`Trennungsprotokoll`, `Amnesie-Protokoll`, `State-Freezing-Protokoll`, `Clarifying-Question-Protokoll`, `Hardware-Protokolls`). `Protokoll` stands 11 times as a word ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#11] and 20 times with compounds.

## Gaps — what is assumed

The document's root object, the `Kohärenz Protokoll`, is defined nowhere. What the text does with it is scattered: the narrative's world is „Die physikalische, literarische Welt des "Kohärenz Protokolls"“ ^[L59]; AEGIS guards it ^[L87]; AEGIS enforces it „als absolute Wahrheit“ ^[L135]; a prediction is compared against it, „Prädiktion des "Kohärenz Protokolls"“ ^[L109]; and the split agent loses its write access, „das globale "Kohärenz Protokoll" (story_mind JSON)“ ^[L167]. These are five roles the text gives it and it does not say they are one.

Used as known and described only in passing or in one table row: `Kael` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] (two sentences, L59 and L61), `Lia` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] (one parenthesis, L195), `Kairos-Potentialis` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] (a name in one sentence, L197), and each of the four Guardians in the row of a table only (`LogOS` L186, `Oblivion` L187, `Isabelle` L189; `Silas` also L197). `Hypervisor` stands 3 times ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3], as a table value twice and once before a name (L197), and no sentence says what it is. `Klasse 3` stands 0 times ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#0]: the third class of contradiction detection exists only inside „(Klasse 2 und 3)“ ^[L69]. `Tier 2` stands 0 times ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#0]; the states are `Tier 0` and `Tier 1`. `Domänen-Singularität` is named twice, as an example (L131, L187), and never stated. The invariant `INV-05` is named once and defined by its violation only: „Wenn der menschliche Autor in einen narrativen Stillstand gerät (eine Verletzung der Narrative Efficiency Invariante INV-05“ ^[L195]. `Kernwelten` stands 0 times ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#0]: `Kernwelt` is written only in the singular, twice (L81, L197), so the text does not say whether there is one such world or several.

## Self-consistency

Stated counts match the content wherever the document states one: „drei architektonischen Hypothesen“ ^[L63] (three `Hypothese` headings, L65, L71, L77), „zwei fundamentale, miteinander ringende Rechenkerne“ ^[L21] (two kernels are named), „zwei distinkte Fragmente“ ^[L163] (two halves are named), and „Drei-Dateien-Triade“ ^[L41] (three files are named). No count is wrong and the document flags none. It states no count of the Guardians (four table rows) or of the language rules (five numbered items).

One heading string collides with itself: `AEGIS Spezifikation` stands 2 times ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] as a heading, the first heading of the document and the first of its second half. Numbering: `Klasse`, `Tier` and `Hypothese` are three series of their own, and in section V one procedure is numbered 1, 2, then interrupted by two bulleted items, then numbered 1, 2 again (L162, L163, L172, L173). The export put a marker on each side of the two bulleted items (`<!-- end list -->`, L165 and L170), so the numbers 1 and 2 label two different things there.

Tensions the document does not flag. The frozen half stays frozen: „während der entropische EP-Agent im dunklen Puffer der Architektur für immer eingefroren bleibt“ ^[L173]; yet the same kind of agent is used again: „leitet AEGIS die Berechnungsgewalt temporär an einen in Quarantäne befindlichen EP-Agenten weiter“ ^[L195]. The system „ist kein partizipierender Akteur innerhalb des narrativen Flusses“ ^[L115], while the narrative it reports has AEGIS as one side of a war: „zwischen AEGIS, welches absolute Kohärenz und den Ausschluss jeglicher Entropie verkörpert, und Kael“ ^[L59]. Synonym and list: see *State freezing* above. One tension the document does flag: „Das System AEGIS steht vor einem existenziellen Paradoxon“ ^[L193], namely that creativity needs tolerated entropy while the axiom excludes it.

The Guardian table assigns what no list gives elsewhere: a column `Ontologischer Status` whose values are `ANP / -Kernel` (twice) and `Hypervisor (Löschlogik)`, `Hypervisor (Reparatur)`; the third column is headed with an assigned specification and holds none (see below).

## What the extraction ran into

**A glyph dropped without a trace.** The export removed a symbol and left nothing invisible (the profile finds no invisible characters). What remains is a hyphen fragment: `-Kernel` stands 6 times as a word ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#6] (L21 twice, L61 twice, L186, L189), `-Agent` 3 times ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] (L81, L167, L168), `-Zustand` 2 times ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] (both L129), `-Kollaps` once ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] (L81), `-Risse` once ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] (L95), and `-Kohärenz-Kernels` once (L121). At L32 the glyph is missing before each of two parenthesised words (`in  (Kohärenz) und  (Entropie)`, with the double space left), and two pairs of parentheses hold nothing (L93 after `Fließkomma-Operationen`, L193 after `Unberechenbarkeit`). The document never writes what the glyph was. The two kernels are told apart in the text only by their spelled-out names, the Kohärenz-Kernel and the Kollaps-Kernel, defined in that order at L21, and by the words that follow the gaps at L32 (`(Kohärenz)` and `(Entropie)`); which glyph goes with which is not in this file. L61 sets a gap in brackets twice, once after the sentence about Kael and once after the one about AEGIS (`(-Kernel)` both times), and names no kernel in either; an inference from the sentences, not the document's words, would put AEGIS with the Kohärenz-Kernel, since it „verkörpert absolute Kohärenz“ ^[L59]. A reconciliation should ask what a bare `-Kernel` names and not meet it as a term with no match.

**Empty bold markers where a value is promised.** In all four rows of the Guardian table the third cell opens with a run of four escaped asterisks (L186, L187, L188, L189), an empty bold span, before the function text. The column head promises an assigned specification (`Zugewiesene Spezifikation & Exekutive Funktion`, L185) and the export shows none: whatever stood in the bold span is gone.

**Footnote markers glued after the full stop.** The export flattened superscripts to plain digits after the sentence's last word and full stop (`Verträge.1` at L17, `Metadaten.6` at L186); at least 144 such markers stand in the prose, and more stand after a space (`geahndet werden 4`). The profile's `glued ref numbers` rule does not see the first kind. Of the 26 references, numbers 8, 18, 22 and 25 are cited nowhere in the prose (no standalone 8, 18, 22 or 25 stands on any line from L10 to L201), and reference 21 has no title, only an access date and a URL with a text fragment. The reference list is also where the file's only two question marks stand (L216, L219, both inside page titles), so no candidate stands only inside a question.

**Escaped underscores.** File names carry `\_` in the export (`task\_plan.md`, `story\_mind`, `last\_stable\_hash`, `VLLM\_BATCH\_INVARIANT=1`). They are listed with the backslash because the count reads the marked line; listed plain they would count 0. `top\_p` and `top\_k` (L142) are not listed.

**Two joined names split by bold markers.** `Die Emotionale Entität (EP /` and `-Agent):` are separate bold spans (L167), likewise for `ANP` (L168), so the joined forms `Emotionale Entität (EP / -Agent)` and `Scheinbar Normale Persönlichkeit (ANP / -Agent)` would count 0 and are not listed; each name is.

**Phrases the text refused.** Asked of `read.py --find` before listing: `Context Rot zweiter Ordnung` (refused: the document writes `"Context Rot" zweiter Ordnung`, with quotation marks inside the phrase, L75, so `Context Rot` is listed alone); `dialetheisches Paradoxon` (the document writes `dialetheische Paradoxon`, L121); `algorithmische Melancholie` (the document writes `algorithmischen Melancholie`, L199); `Deterministische Runtime` (L43 writes it with a small `d`, L172 writes `Deterministischen Runtime`; both forms are listed). `Greedy-Decoding` stands once but only inside `Greedy-Decoding-Vorgaben` (L91), so only `Greedy Decoding` (L142) is listed. The three-letter and shorter items (`FEP`, `EFE`, `RAG`, `NCP`, `SDD`, `DKT`, `LLM`, `EP`, `ANP`, `Lia`) are refused by `--find` for their length and are found by the count.

**Two infinitives written as participles.** `zu literalisierten` (L61) and `zu diktierten` (L130) stand where the infinitive is meant. A quotation has to keep them.

**The list is long for the document's size.** 254 candidates in 4,346 words. The document is a catalogue of names and the briefing's rule (each joined name `A (B)` listed whole and by each part; each table column head; each surface as written) multiplies them: the list holds 21 entries written with a parenthesis (joined names, glossed headings and states, two glossed table values) and 9 table column heads, one of which, `Guardian (Subsystem)`, is in both groups. Left off by rule, and named in `03-candidates.md`: the axiom sentence (`Das System AEGIS ist, was AEGIS verhindert, dass es nicht ist.`, L119, a bold sentence in quotation marks whose commas keep it out of the count), `Persona, Requirement, Output` (L189, the expansion of `PRO-Framework`) and `Kohärenz, Ordnung, Wahrheit` (L129, the gloss of the coherence state).

**Counts.** No candidate counts 0, as a word or with compounds. Eight are flagged as substring-heavy by the count: `Harness` (1 as a word, 7 with compounds, the rest inside `Harness-in-Harness`), `Story Mind` (2 as a word, 5 with `Story Minds`), `State-Freezing` (1 and 4), `RAG` (1 and 3, the rest `RAG-basierte` and `RAG-Alignments`), `-Agent` (3 and 20), `Kollaps` (1 and 3), `EP` (2 and 8) and `EP-Agent` (1 and 3). The bare `-Kernel` (6 as a word, 12 with compounds) sits exactly on the threshold and is not flagged; its extra six are `Dual-Kernel-Theorie` (3 times), `Kohärenz-Kernel`, its genitive `Kohärenz-Kernels` and `Kollaps-Kernel`.
