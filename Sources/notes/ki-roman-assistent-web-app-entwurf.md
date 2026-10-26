---
source: Sources/drive/ki-roman-assistent-web-app-entwurf.md
read: "2026-10-19, the whole document (L1 to L238) through read.py with line numbers; by a document-reader subagent (Sonnet)"
stance_markers: ["Verhaltensregeln und Methodik", "Phase 1", "Phase 2", "Phase 3", "Phase 4", "Zusammenfassung und Schlussfolgerung"]
stance_marker_count: 6
reads_as: "a design specification for a web console, calling itself a Spezifikation, that maps the novel's terms onto interface tools, a skill definition and colour tokens"
---

# Note — KI-Roman-Assistent: Web-App-Entwurf

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document is a software specification that borrows the novel's terms as interface vocabulary; it is a plan for a tool, not a narrative.

## 1 · What kind of text this is, and how it marks itself

- The document states its own genre in the title: „Architektonische Spezifikation und Systementwurf“ ^[L11]
- It says what it defines: „Die vorliegende Spezifikation definiert die architektonischen, ästhetischen und technologischen Grundlagen“ ^[L15]
- **Observed:** the body is organised by headings, a tool table (L59 to L66), a skill definition in a code-like block with a section headed `Verhaltensregeln und Methodik` ^[ki-roman-assistent-web-app-entwurf.md:#1], four workflow steps headed `Phase 1` ^[ki-roman-assistent-web-app-entwurf.md:#1], `Phase 2` ^[ki-roman-assistent-web-app-entwurf.md:#1], `Phase 3` ^[ki-roman-assistent-web-app-entwurf.md:#1] and `Phase 4` ^[ki-roman-assistent-web-app-entwurf.md:#1], a colour-token table (L139 to L147), a closing section `Zusammenfassung und Schlussfolgerung` ^[ki-roman-assistent-web-app-entwurf.md:#1] and a numbered reference list from L196. The reference list names web pages and other texts; those are not harvested.
- **Observed:** the export lost symbols. The kernel names are empty parentheses in L29, L103, L149 and L157, so which symbol belonged to which kernel is not recoverable from this file. The tool table writes the kernel enum as `K0`/`K1` in L63 with backslash escapes.

## 2 · The Kohärenz-Protokoll as the thing the console serves

- The third module works from the rules of the „Welt-Bibel“ ^[L29] and watches the consistency of the Kernwelten.
- The skill description says it „Wendet das Kohärenz-Protokoll auf Manuskripte an“ ^[L89]
- The skill text gives the role name „Novel Writing Assistent“ ^[L97], set in single quotation marks.
- The document writes the protocol's name two ways: `Kohärenz-Protokoll` (hyphen) and `Kohärenz Protokoll` (space) are both in the text; see the census counts.

## 3 · The four modules

- „Axis Mundi Dashboard“ ^[L25] is the first module; L25 describes it as the central chronological and logical structure of the novel.
- „Charakter-Nexus und das TSDP-Geflecht“ ^[L27] is the second module; it is a network visualisation of the parts of Kael.
- „Metaphysische und Physikalische Constraint-Engine“ ^[L29] is the third module.
- „Kintsugi-Integrationswerkstatt“ ^[L31] is the fourth, meant for writing blocks and narrative gaps.

## 4 · Figures and their roles

- Kael is given as having „elf distinkten Anteilen (Alters)“ ^[L27]
- Lex is described as „ein primärer ANP, der durch absolute Logik Kontrolle erzwingen will“ ^[L47]
- The tool table gives archetypes: „Nyx als Krieger, Selene als Heilerin“ ^[L62]
- Lia is called „ein Trickster-Kind-EP“ ^[L68]
- The skill asks whether Nyx shows reasons that break a protector role: „Zeigt Nyx unbegründete Verletzlichkeit“ ^[L104]
- Moros appears in an example inconsistency, an action that ignores the collapse of this EP: „des EP Moros ignoriert“ ^[L171]
- L157 speaks of the „Einwirken der Entität“ ^[L157] and names Juna inside inner quotation marks right after; the same line says the interface then turns organic.
- AEGIS is named as a controlling force: „der kontrollierenden Kraft von AEGIS“ ^[L157]; the empty canvas is dominated by a grid pattern: „Gittermuster von AEGIS dominiert“ ^[L159]
- **Observed:** Isabelle is absent: `Isabelle` ^[ki-roman-assistent-web-app-entwurf.md:#0]

## 5 · The Dual-Kernel-Theorie and its checks

- The skill's analysis step is named „Dual-Kernel-Evaluierung“ ^[L103], and the same line pairs „Ordnung/AEGIS“ ^[L103] with „Chaos/Juna“ ^[L103].
- The plot tool checks the theory: „Überprüfung, ob die Dual-Kernel-Theorie verletzt wurde“ ^[L63]
- The tool table lists an enum of two kernels (L63) and a metrics tool `updateMetaphysicalState` (L66) with entropy, AEGIS control and Juna presence fields.

## 6 · The tools, the skill and the workflow

- The interface API is described as „semantische Brücke zwischen den literarischen Konzepten“ ^[L53]
- The document, with a reference number glued to the sentence, states of skills in general: „Skills in Claude Code sind keine ausführbaren Skripte“ ^[L72]
- A caution against over-prescription: „zu präskriptive Instruktionen“ ^[L74]
- The workflow begins with „Ingestion und Evaluierung im Terminal“ ^[L169]
- **Observed:** the example commit message in L178 names a chapter number: `Chapter 14` ^[ki-roman-assistent-web-app-entwurf.md:#1]; it is an invented example for a commit, with no chapter content.

## 7 · Colour tokens and the trauma symbol

The document also holds a palette of semantic colour tokens that is tied to a trauma symbol (Kernwunde) and to named parts. This material is not harvested here.

## 8 · The document's own standing

- It praises its design: „Die herausragende Leistung dieses Entwurfs“ ^[L190]
- It describes the console as „der physisch manifestierte, digitale Partner“ ^[L192]

Both are the document's self-description; neither is applied.

## 9 · Said two ways, or left open — recorded, not resolved

- **Observed:** the protocol's name is written with a hyphen in L11 and L25 and with a space in L15 and L97.
- **Observed:** the document names the kernel symbols only as empty parentheses, so the pairing of each kernel with order or chaos rests on L103's „Ordnung/AEGIS“ ^[L103] alone.

## 10 · Absent, counted

- `Isabelle` ^[ki-roman-assistent-web-app-entwurf.md:#0]
