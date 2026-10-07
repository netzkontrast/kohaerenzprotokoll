---
source: Sources/drive/romanidee-als-interaktiver-prototyp.md
read: "2026-10-06, the whole document (L1 to L303) through read.py with line numbers, by a document-reader subagent (Sonnet)"
stance_markers: ["Szenario", "Interaktion"]
stance_marker_count: 10
reads_as: "a design proposal for an interactive CAVE prototype of the novel's first act: an analysis of the novel's architecture from one outline, a specification of a state-tracking protocol, a chapter plan and recommendations"
---

# Note — Romanidee als interaktiver Prototyp

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document speaks as a proposal: it analyses the novel from one reference and recommends a design, and where it reports the novel's world it reports that reference.

## 1 · What kind of text this is, and how it marks itself

- The document names its single reference as „Outline“ ^[L302], and a digit glued to the end of sentences points to it, so part I reports that outline's world and does not invent one. **Observed:** the digit follows sentences on L30, L32, L34 and L44.
- The first part presents itself as an analysis of the architecture: „Dekonstruktion der Narrativen Architektur“ ^[L18].
- The document calls its own product the „Quellcodes“ ^[L22] of the narrative, from which the logic of the interactive experience is derived.
- The chapter plan marks its scenes with the labels `Szenario` ^[romanidee-als-interaktiver-prototyp.md:#4] and `Interaktion` ^[romanidee-als-interaktiver-prototyp.md:#6]; the heading says the breakdown is an „Auszug“ ^[L197].
- Recommendations are labelled lines: „Leitprinzip“ ^[L295] and, among others, `Priorität` ^[romanidee-als-interaktiver-prototyp.md:#3].

## 2 · The conflict between AEGIS and Kael

- Reporting its outline, the document describes AEGIS as an intelligence whose purpose is coherence: „eine autopoietische, informationsbasierte Intelligenz“ ^[L30].
- Reporting its outline, it says of Kael: „Seine Entwicklung zielt auf die Realisierung einer alternativen, emergenten Form der Kohärenz“ ^[L30], and names that state `funktionale Multiplizität` ^[romanidee-als-interaktiver-prototyp.md:#3].
- Reporting its outline, it says the flaw driving AEGIS is the `Paradoxon der Fehlausgerichteten Kohärenz` ^[romanidee-als-interaktiver-prototyp.md:#2], and that the instabilities appear in the world as „Risse“ ^[L32].
- Its own reading is that Kael's integration is a weapon: „Die Heilung wird zur Waffe“ ^[L50]. This is the document's interpretation of its outline, put as a design principle for the prototype.

## 3 · System Kael and funktionale Multiplizität

- In the outline's terms, „System Kael“ ^[L44] is described as modelled after a theory the document abbreviates `TSDP` ^[romanidee-als-interaktiver-prototyp.md:#1].
- Reporting its outline, the line gives the number of parts: „elf detailliert ausgearbeiteten Anteilen“ ^[L44]. The parts are split into `ANPs` ^[romanidee-als-interaktiver-prototyp.md:#1] and `EPs` ^[romanidee-als-interaktiver-prototyp.md:#2].
- Reporting its outline, it says of the prose: „Die Prosa des Romans selbst soll diesen Zustand performen“ ^[L46].
- It calls the state more than a goal: „ist nicht nur ein psychologisches Ziel, sondern eine narrative Waffe“ ^[L48].
- Named parts are Nyx, Lex, Kiko, Rhys and Alex. **Observed:** `Nyx` ^[romanidee-als-interaktiver-prototyp.md:#8], `Lex` ^[romanidee-als-interaktiver-prototyp.md:#12], `Kiko` ^[romanidee-als-interaktiver-prototyp.md:#9], `Rhys` ^[romanidee-als-interaktiver-prototyp.md:#4] and `Alex` ^[romanidee-als-interaktiver-prototyp.md:#1] stand in the variable table and the examples; the document names no more than these five of the eleven.

## 4 · AEGIS as a tragic figure and its protocols

- Reporting its outline, the line describes AEGIS as „ist keine simple, böswillige KI“ ^[L58].
- Its protocols are named with their spelled-out names: `Zero Trust Environment Mandate` ^[romanidee-als-interaktiver-prototyp.md:#1] and `Recursive Trust Signature Verification` ^[romanidee-als-interaktiver-prototyp.md:#1], abbreviated `ZTEM` ^[romanidee-als-interaktiver-prototyp.md:#1] and `RTSV` ^[romanidee-als-interaktiver-prototyp.md:#1].
- The document says AEGIS' protocols are defences: „Seine Protokolle sind nicht nur technische Spezifikationen“ ^[L60].
- The `SIS-Protokoll` ^[romanidee-als-interaktiver-prototyp.md:#1] is spelled out in the line as „Systemic Isolation Shield“ ^[L60], and the same line says it seals off whole Kernwelten; the document equates this with dissociation.
- Reporting its outline, the fate named for AEGIS is `algorithmische Melancholie` ^[romanidee-als-interaktiver-prototyp.md:#1], which L58 writes in the inflected form „algorithmischer Melancholie“ ^[L58].

## 5 · Juna/V and Das Fundament

- Reporting its outline, the document says the two are meta-levels: „Das Fundament“ ^[L70] and the `Juna/V-Verbindung` ^[romanidee-als-interaktiver-prototyp.md:#2], whose link to Kael it calls the `Moonshine-Link` ^[romanidee-als-interaktiver-prototyp.md:#2].
- Of Das Fundament, reporting its outline, it says: „Es ist keine Entität oder ein Ort“ ^[L70].
- Reporting its outline, the document says the two are to be earned: „Ihr Potenzial muss durch Kaels eigene psychologische Entwicklung“ ^[L72] activated.
- It reads them as an alternative game physics: `Spielphysik` ^[romanidee-als-interaktiver-prototyp.md:#1].

## 6 · The worlds and the Risse

- Reporting its outline, the document names „sechs identifizierten Realitätsebenen“ ^[L84]: four Kernwelten (`KW1` ^[romanidee-als-interaktiver-prototyp.md:#10], `KW2` ^[romanidee-als-interaktiver-prototyp.md:#7], `KW3` ^[romanidee-als-interaktiver-prototyp.md:#2], `KW4` ^[romanidee-als-interaktiver-prototyp.md:#1]), the Überwelt and the Externe Ebene.
- Reporting its outline, the document says: „AEGIS hat die Kernwelten explizit geschaffen“ ^[L86].
- It proposes that the Risse are „Debugging- oder Korrekturversuche“ ^[L86] by AEGIS and a language the player decodes: „Die „Risse“ werden zu einer Art Sprache“ ^[L90].

## 7 · The Narrative Context Protocol

- The document defines the NCP: „wird als ein zentrales, serverseitiges State-Tracking-System definiert“ ^[L106]. The term stands in full `Narrative Context Protocol` ^[romanidee-als-interaktiver-prototyp.md:#5] and as `NCP` ^[romanidee-als-interaktiver-prototyp.md:#14].
- It says the protocol serves as „Single Source of Truth“ ^[L106] for the state of the simulation. This is the document's claim about its own proposed system, recorded and not applied.
- The variables sit in a matrix, `Key-Variable-Matrix` ^[romanidee-als-interaktiver-prototyp.md:#3], with stems such as `Kael.System.Cohesion` ^[romanidee-als-interaktiver-prototyp.md:#8] and `AEGIS.Intervention.Level` ^[romanidee-als-interaktiver-prototyp.md:#4].
- The document says what the matrix does: „Die Matrix schafft eine klare und nachvollziehbare Kausalkette“ ^[L134].
- The feedback loop is shown by one example, introduced with „Ein konkretes Beispiel soll diesen Prozess verdeutlichen“ ^[L142].

## 8 · The prototype plan

- The plan covers the first act: „Dies ist der Höhepunkt und das Finale des ersten Aktes“ ^[L232] is said of chapter 13.
- The chapter list gives four scenes, of chapters 1, 3, 7 and 13, with titles such as `Konstrukt-Stadt` ^[romanidee-als-interaktiver-prototyp.md:#1] and `Archivar` ^[romanidee-als-interaktiver-prototyp.md:#2].
- The inner council is a mechanic: „Der Prototyp basiert auf drei zentralen, wiederkehrenden Gameplay-Schleifen“ ^[L188] includes `Interne Verhandlung` ^[romanidee-als-interaktiver-prototyp.md:#1] with the `Inneren Konferenzraum` ^[romanidee-als-interaktiver-prototyp.md:#2].
- The `Datenriss` ^[romanidee-als-interaktiver-prototyp.md:#1] of chapter 3 is a timed minigame, and the threshold of chapter 13 is „als kooperatives Rätsel konzipiert“ ^[L233].
- Sensory design is given for KW1 and KW2 in three channels each; for KW1: „Die Wände der CAVE projizieren eine hyper-realistische“ ^[L245] architecture, and for KW2 „Eine dichte, polyphone Klanglandschaft“ ^[L256].

## 9 · Recommendations

- Priorities: `Priorität` ^[romanidee-als-interaktiver-prototyp.md:#3] 1 is the NCP framework, priority 2 the CAVE implementation of KW1.
- Acts II and III are sketched only as ideas. For act III the document says the final confrontation would not be a boss fight: „kein traditioneller“ ^[L285] one but a „logischer Kampf“ ^[L285].
- The ethics section recommends: „Es wird dringend empfohlen, Fachexperten“ ^[L276] to be involved.
- The principle is that the player is not to be punished: „Die Interaktivität darf niemals dazu führen“ ^[L295].

## 10 · Said two ways, or left open — recorded, not resolved

- The document gives the same state in two surfaces, `funktionale Multiplizität` ^[romanidee-als-interaktiver-prototyp.md:#3] and `funktionalen Multiplizität` ^[romanidee-als-interaktiver-prototyp.md:#2]; the heading capitalises it.
- It names the inner council as `Innerer Rat` ^[romanidee-als-interaktiver-prototyp.md:#2] and `Inneren Rat` ^[romanidee-als-interaktiver-prototyp.md:#2] and as the „Inneren Konferenzraum“ ^[L191].
- The Guardians are named in table rows and in the example: `Guardians` ^[romanidee-als-interaktiver-prototyp.md:#2]. One row pairs them with others: „Direkte Konfrontationen mit Guardians oder anderen AEGIS-Agenten“ ^[L129].

## 11 · Absent, counted

- The document writes no question mark (profile: 0).
- `Selene` ^[romanidee-als-interaktiver-prototyp.md:#1] appears once, at L191, as a later role of the player; the document does not describe her.
