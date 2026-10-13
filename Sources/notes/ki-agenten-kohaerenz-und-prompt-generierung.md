---
source: Sources/drive/ki-agenten-kohaerenz-und-prompt-generierung.md
read: "2026-10-12, the whole document (L1 to L367) through read.py with line numbers; by a document-reader subagent (Sonnet)"
stance_markers: ["Wir postulieren", "Unsere zentrale Hypothese", "wird erwartet", "Man kann sich vorstellen", "Ausblick"]
stance_marker_count: 7
reads_as: "a German whitepaper that proposes a protocol and a meta-prompt for AI agents over a note-based knowledge graph; a technical specification, not a text about the novel's world"
---

# Note — KI-Agenten: Kohärenz und Prompt-Generierung

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document speaks as a research proposal: it postulates, designs and expects, and it reports other authors' work in its theory section.

## 1 · What kind of text this is, and how it marks itself

- It presents itself as a paper that sets out a two-part solution: „stellt einen neuartigen, zweigeteilten Lösungsansatz vor“ ^[L22]. It calls itself `Whitepaper` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2] twice.
- Its hypothesis is introduced as a postulate, `Wir postulieren` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2] twice, and „Unsere zentrale Hypothese lautet daher“ ^[L79].
- It states its results as expectation: „wird erwartet, dass der Agent ein kohärentes Verständnis entwickelt“ ^[L293].
- **Observed:** the document names none of the novel's figures; `Kael` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#0] and `AEGIS` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#0] stand in no line. It is about AI agents and knowledge bases, so its terms are the document's own engineering vocabulary.
- **Observed:** the reference list (L341 to L367) ends the document; `Zugriff am August 5, 2025` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#24] stands in its entries. They are titles of cited works.

## 2 · Kohärenz-Protokoll

- The document's own account of the term: „eine formale, maschinenlesbare Spezifikation“ ^[L24] for navigation of an external, graph-based knowledge base.
- It says it coins the name itself: „Wir nennen diesen Regelsatz das“ ^[L87] and then sets the name in quotation marks.
- It describes the protocol as an external executive system that forces systematic exploration; the line calls it a „Exekutivsystem“ ^[L87].
- It describes the protocol as built from rule-bound tools: „Der Agent kann die Regeln nicht brechen“ ^[L213]. The same line says an own server is the only instance with read and write access to the knowledge base.
- The paper divides the protocol into phases: „Das Protokoll selbst lässt sich in fünf konzeptionelle Phasen unterteilen“ ^[L215]. The phases are headed `Orientierung am Anker-Dokument` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1], `Navigation über MOCs` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2], `Fokussierung auf atomare Notizen` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1], `Kontext-Kapselung` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] and `Selbst-Aktualisierung` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1].
- The first phase begins with a fixed file: „beginnt zwingend mit dem Lesen des Wurzel-Dokuments“ ^[L217].
- The last phase integrates new insights through named tools; the line writes „Neue atomare Zettel werden mit dem“ ^[L221] followed by the tool name. The tool names are `update\_note\_status` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] in that line, while `create\_note` and `update\_note\_links` stand there inside a longer word with `-Tool` (see the census).
- The gap the protocol addresses is named `Kohärenz-Lücke` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2] twice.

## 3 · Meta-Prompt and the cognitive constitution

- The paper's account: the meta-prompt works as „als eine Art Verfassung für die kognitive Autonomie des Agenten dient“ ^[L95].
- It insists the meta-prompt is permanent: „Der Meta-Prompt ist kein einmaliger Befehl“ ^[L229].
- The articles are given as a table headed „Tabelle: Die Artikel der kognitiven Verfassung“ ^[L233]; the titles of the three articles are `Kognitive Direktive` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1], `Mandat zur Selbst-Evaluation` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] and `Mandat zur Prompt-Generierung` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2].
- Article 1 is quoted as an instruction to the agent in the second person: „Dein oberstes Ziel ist das Streben nach tiefem Verständnis“ ^[L244]. The speaker of that sentence is the prompt text the document proposes, not the document describing.
- The document says its constitution differs from the borrowed concept in aim: it „zielt nicht primär auf Sicherheit oder Ethik ab“ ^[L175].
- The constitutional-AI concept is attributed by the document to researchers at another organisation, and the document says „Wir adaptieren diesen Ansatz für unsere Zwecke“ ^[L175]. The borrowed term stands as `Konstitutionellen KI` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2] and `Konstitutionelle KI` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1].

## 4 · Knowledge base, Zettelkasten and Maps of Content

- The document gives the knowledge graph as the base: „Ein wesentlich robusterer Ansatz ist die Verwendung eines Knowledge Graph“ ^[L121].
- The Zettelkasten method is called „Die Zettelkasten-Methode als Implementierungsparadigma“ ^[L125]; three principles follow, headed `Atomizität` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] and `Emergente Struktur` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] and an explicit-linking principle.
- Maps of Content are introduced as „Hier kommen“ ^[L149] followed by the name; the heading calls them „als Navigations-Kortex“ ^[L137]. The document writes `MOCs` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#17] seventeen times.
- The root file is called by the document a map of maps: `MOC der MOCs` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2].
- The navigation order is top-down: „Die Navigation erfolgt systematisch Top-Down“ ^[L157].

## 5 · The gardener agent and the agent roles

- The document reports a planned component of an architecture plan: „Ein konkretes Beispiel hierfür ist der im Architekturplan vorgesehene“ ^[L197]. The plan itself is a cited reference, a separate text, so the component is that text's, reported here.
- The document describes this agent as a watcher: „Dieser "Gärtner"-Agent überwacht die Wissensbasis“ ^[L197]. The role is later written „digitaler Gärtner“ ^[L283].
- Table 2 assigns roles; the document says of it „eine Multi-Agenten-Architektur vorgeschlagen“ ^[L248]. Rows: „Analysiert unverarbeitete Notizen“ ^[L263] for the prioritizing role, „Identifiziert atomare Ideen aus der Analyse“ ^[L265] for the synthesizing role, „Nutzt die regelbasierten Tools“ ^[L266] for the writing role, and „Führt die in Artikel“ ^[L267] for the orchestrator.

## 6 · Said two ways, or left open — recorded, not resolved

- The document states a design property of its protocol in the present tense, „Der Agent kann die Regeln nicht brechen“ ^[L213], and states the multi-agent collaboration as only imaginable, „Man kann sich vorstellen, wie mehrere solcher Agenten zusammenarbeiten“ ^[L334]. The two are different registers (specification and outlook), and the document does not connect them.
- The document claims for its approach a standing: its log files „bieten eine beispiellose Transparenz“ ^[L337]. This is the document's own claim and is recorded, not applied.
- **Observed:** `Hypothese` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#5] stands five times, and the results section is written in expectation (`wird erwartet` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1]); the lines read do not report a test.

## 7 · Absent, counted

- The novel's figures and world words are not in this document: `Kael` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#0], `AEGIS` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#0] and `Kern-Welt` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#0] each stand in no line.
