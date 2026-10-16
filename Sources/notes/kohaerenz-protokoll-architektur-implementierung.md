---
source: Sources/drive/kohaerenz-protokoll-architektur-implementierung.md
read: "2026-10-12, the whole document (L1 to L196) through read.py with line numbers, by a document-reader subagent (Sonnet)"
stance_markers: ["Phase I", "Phase II", "Phase III", "Phase IV", "Fazit", "Referenzen"]
stance_marker_count: 6
reads_as: "a German analysis and phased implementation plan for a writing assistant, built on three software ecosystems and mapped onto terms of the novel, closed by a Fazit and a numbered reference list"
---

# Note — Kohärenz Protokoll: Architektur & Implementierung

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document speaks as an analysis that argues for a plan; the novel's terms enter as the world the software is said to mirror.

## 1 · What kind of text this is, and how it marks itself

- The document describes its own task as an evaluation: „Die vorliegende exhaustive Analyse evaluiert die Nutzbarkeit“ ^[L15]
- The plan part is headed by phases; the four phase headings read „Phase I: Die Architektonische Grenzziehung“ ^[L106], „Phase II: Instanziierung der Existenz“ ^[L114], „Phase III: Die Deterministische Härte“ ^[L123] and „Phase IV: Die Fusion der Ebenen“ ^[L131].
- **Observed:** the stance labels `Phase I` ^[kohaerenz-protokoll-architektur-implementierung.md:#1], `Phase II` ^[kohaerenz-protokoll-architektur-implementierung.md:#1], `Phase III` ^[kohaerenz-protokoll-architektur-implementierung.md:#1] and `Phase IV` ^[kohaerenz-protokoll-architektur-implementierung.md:#1] each stand once, `Fazit` ^[kohaerenz-protokoll-architektur-implementierung.md:#1] and `Referenzen` ^[kohaerenz-protokoll-architektur-implementierung.md:#1] once each, in the headings.
- The closing section is headed „Fazit: Die Grenze als Motor der Erkenntnis und Funktion“ ^[L139], and its first paragraph says that the synthesis „beweist, dass technologische Werkzeuge weit mehr sein können“ ^[L141]. This is the document's claim about its own result; it is recorded, not applied.
- **Observed:** after the Fazit comes a reference list of 47 numbered entries (L149 to L195). Of them, `Zugriff am Februar 27, 2026` ^[kohaerenz-protokoll-architektur-implementierung.md:#38] stands in 38 entries, the web sources; the remaining entries are bare titles. Entries 1, 2, 7, 12, 17, 18, 25, 27 and 31 are bare titles, among them „Roman-Synthese mit Dual Kernel Theorie“ ^[L149], „Charaktere“ ^[L150] and „Kohärenz Protokoll: Master-Outline“ ^[L173]. They are the document's list of the texts it says it drew on; their content is not here.

## 2 · The novel as the document describes it

- The document calls the novel a simulation: „tiefgreifende ontologische, physikalische und psychologische Simulation“ ^[L13]
- It names the protagonist and the entity behind his trauma: „Die Geschichte des Protagonisten Kael“ ^[L13]. The line goes on to say that his psyche is split into eleven parts, with `TSDP` ^[kohaerenz-protokoll-architektur-implementierung.md:#3] (the abbreviation of the long form that stands once on L13) and the entity `AEGIS` ^[kohaerenz-protokoll-architektur-implementierung.md:#6].
- The conflict is stated as two kernels: the first is „ordnungsschaffenden, deterministischen“ ^[L13] and the second „stochastischen, entropischen“ ^[L13]. The line assigns the first to AEGIS and the second to Juna. The export lost the kernel symbols there (the line reads „(, repräsentiert durch AEGIS)“ ^[L13]), so the line holds `Kohärenz-Kernel` ^[kohaerenz-protokoll-architektur-implementierung.md:#1] and `Kollaps-Kernel` ^[kohaerenz-protokoll-architektur-implementierung.md:#1] without their symbols.
- The document claims the software must mirror this: „muss sich unmittelbar in der Code-Basis des Assistenten widerspiegeln“ ^[L13]
- For the psyche it reports a theory: „Die psychologische Struktur des Protagonisten Kael folgt“ ^[L49]. In that sentence the parts are two kinds, `Anscheinend Normale Persönlichkeitsanteile` ^[kohaerenz-protokoll-architektur-implementierung.md:#1] (abbreviated `ANPs` ^[kohaerenz-protokoll-architektur-implementierung.md:#2]) and `Emotionale Persönlichkeitsanteile` ^[kohaerenz-protokoll-architektur-implementierung.md:#1] (abbreviated `EPs` ^[kohaerenz-protokoll-architektur-implementierung.md:#2]), and the line says „Sein Geist ist in elf Entitäten zersplittert“ ^[L49]
- Parts named in the document: Kael and Lex as ANPs; Nyx, Kiko and Moros as EPs (L49); Selene appears in a list of the eleven parts (L119) with `Selene` ^[kohaerenz-protokoll-architektur-implementierung.md:#1] standing once. The document names only some of the eleven.
- The EP „Nyx“ is described as fighting reaction and the ANP Lex as fearing emotions and loss of control, on L51; the document writes both names inside quotation marks, so the note quotes neither.

## 3 · The software mapped onto the novel

- ZeroClaw is given a narrative role: „als die programmatische Manifestation von AEGIS“ ^[L41]. The table before it ends its security row with „Absolute kausale Geschlossenheit“ ^[L38] as the narrative counterpart of the Rust runtime's security model; the same row names the `Kollaps-Kernel` ^[kohaerenz-protokoll-architektur-implementierung.md:#1] as what is suppressed.
- The Fazit repeats the identification: ZeroClaw „verkörpert den rigorosen Kontrollzwang der KI AEGIS“ ^[L143]
- The Drama Engine is given the psyche: „kann die Drama Engine die komplexen ANP-EP-Phobien abbilden“ ^[L51], and each of the eleven parts is said to be its own instance of the `ChatCompanion` ^[kohaerenz-protokoll-architektur-implementierung.md:#2] class (L51).
- The amnesia between parts is a filter: „Dadurch wird algorithmisch erzwungen, dass Kiko“ ^[L59] stays blind to parts of the story. The mechanism is the `InstructionDeputy` ^[kohaerenz-protokoll-architektur-implementierung.md:#2], and in Phase II the plural `InstructionDeputies` ^[kohaerenz-protokoll-architektur-implementierung.md:#2] is the build step „Amnesie-Implementierung“ ^[L121].
- The delegation feature is introduced as „Ein herausragendes Merkmal der Drama Engine“ ^[L57], with the words `Shells` ^[kohaerenz-protokoll-architektur-implementierung.md:#1] and `Deputies` ^[kohaerenz-protokoll-architektur-implementierung.md:#1] set in quotation marks by the document.

## 4 · The storage table: three products, three ontological correspondences

- **Observed:** the table on L79 to L84 has three columns, the third headed with the document's words for an ontological and narrative correspondence (L81); it assigns one correspondence to each of `Vercel Postgres` ^[kohaerenz-protokoll-architektur-implementierung.md:#2], `Vercel KV` ^[kohaerenz-protokoll-architektur-implementierung.md:#2] and `Vercel Blob` ^[kohaerenz-protokoll-architektur-implementierung.md:#1].
- Postgres is paired with `Das Blockuniversum` ^[kohaerenz-protokoll-architektur-implementierung.md:#1]: „Alle Ereignisse der Geschichte existieren simultan als fixierte Fakten“ ^[L82]
- KV is paired with the `Phänomenale Jetzt` ^[kohaerenz-protokoll-architektur-implementierung.md:#1]: „Der flüchtige, stetig wechselnde Aufmerksamkeitsfokus“ ^[L83], of the active parts.
- Blob is paired with `Die Physische Materialität` ^[kohaerenz-protokoll-architektur-implementierung.md:#1]: „Ablage der manifesten, unumkehrbaren Artefakte“ ^[L84]. The line is cut by the export at the point where a symbol for the space of possibilities stood (it ends „()“).
- The persistence of workflows is said to mirror a time model: „Die Zeit im System fließt nicht kontinuierlich, sondern akkumuliert“ ^[L86]. The model is `Ledger-Time-Modell` ^[kohaerenz-protokoll-architektur-implementierung.md:#2] and the document names its author, which this note does not repeat.

## 5 · Truth theories as a verification rule

- The document divides generated text by two theories: the first sentence of the correspondence item reads „Ein generierter Satz ist nur dann als“ ^[L92], with the continuation „wahr“ in quotation marks, true when it matches the database; the item for the coherence theory begins with a creative generation by the LLM, which the line assigns to the `Kollaps-Kernel` ^[kohaerenz-protokoll-architektur-implementierung.md:#1] (here written „-Kollaps-Kernel“ ^[L93], with a lost symbol).
- The rule for new ideas: „Ein neuer Einfall ist dann“ ^[L93] acceptable when it fits the system of beliefs without contradiction. The term pair is `Korrespondenztheorie` ^[kohaerenz-protokoll-architektur-implementierung.md:#3] and `Kohärenztheorie` ^[kohaerenz-protokoll-architektur-implementierung.md:#3].

## 6 · The phases mapped to the novel's structure

- Phase I is said to correspond to an event of the novel: „Dies entspricht der Etablierung des“ ^[L108] followed by `Konstrukts` ^[kohaerenz-protokoll-architektur-implementierung.md:#1] (in quotation marks in the document), by AEGIS.
- Phase IV is said to reflect an act: „Dies spiegelt Akt III des Romans wider“ ^[L133]. The line gives the content as acceptance of entropy and fusion into a functional multiplicity.
- A failure case is placed in a chapter: the loop of the engine is compared to „ähnlich dem Versagen parakonsistenter Logik in Kapitel 12“ ^[L100]. This is the only place the document gives a chapter number.

## 7 · Said two ways, or left open — recorded, not resolved

- **Observed:** the security paragraph (L19 to L21) says the repositories under one namespace and associated domains were identified by the core developers as illegitimate forks; the document says it uses only the original repository. This is a statement about a software source, not about the novel, and it is recorded as the document's claim: „ausschließlich auf das verifizierte Original-Repository“ ^[L21]
- **Observed:** the table on L33 to L39 writes the memory figure of the Node-based frameworks as more than 300 MB (L36), while the prose on L27 says about 390 MB. The two figures stand on different lines and are not reconciled in the document.
- **Observed:** the figures for the Vercel AI SDK versions are lost on L67 (the line reads „in den Versionen und“ ^[L67]), and the kernel symbols on L13, L38, L84 and L93 are lost, so the export damaged what the lines say about them.

## 8 · Absent, counted

- The document has no chapter list or `Kap` ^[kohaerenz-protokoll-architektur-implementierung.md:#0] abbreviation. The word `Kapitel` ^[kohaerenz-protokoll-architektur-implementierung.md:#1] stands once, in „Kapitel 12“ ^[L100]; the only other act or chapter reference is `Akt III` ^[kohaerenz-protokoll-architektur-implementierung.md:#1] on L133.
