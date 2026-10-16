---
source: Sources/drive/ki-roman-design-mechaniken.md
read: "2026-10-12, the whole document (L1 to L265) through read.py with line numbers; by a document-reader subagent (Sonnet)"
stance_markers: ["Die Mechanik:", "Spielerinteraktion:"]
stance_marker_count: 8
reads_as: "a design analysis of AI-driven interactive novels whose last section proposes four player mechanics for the Kohärenz Protokoll, followed by a numbered reference list"
---

# Note — KI-Roman: Design & Mechaniken

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document speaks as an analysis that ends in a proposal; its labels `Die Mechanik:` ^[ki-roman-design-mechaniken.md:#4] and `Spielerinteraktion:` ^[ki-roman-design-mechaniken.md:#4] each stand four times, once per mechanic.

## 1 · What kind of text this is, and how it marks itself

- The document states its own aim: „Die vorliegende Analyse untersucht die modernsten methodischen und technologischen Ansätze“ ^[L17].
- It turns to the novel with „Konzeptionierung von Spielmechaniken“ ^[L152], and says the mechanics make the interactive novel „ein hochgradig strategisches, psychologisches System“ ^[L154].
- **Observed:** the text from L11 to L150 describes methods and cites numbered references; the text from L152 to L184 proposes four mechanics, each under a bold numbered line with `Die Mechanik:` and `Spielerinteraktion:`; L186 to L192 is a conclusion; L194 to L265 is the reference list.
- **Observed:** the details of the novel's world in the four mechanics are followed by reference number 54 (L165, L172, L181, L183, L184), and that entry reads „Roman: Kohärenz Protokoll“ ^[L249]. Reference 69 is „Systemische Analyse komplexer Beziehungsdynamik“ ^[L264].

## 2 · The Kohärenz Protokoll and its premise

- The document introduces the project as the basis for the mechanics („Basierend auf den Parametern des“ ^[L154]) and describes it as one that links hard science fiction, systems theory, the fictional Dual Kernel Theory and dissociative trauma psychology (L154).
- It calls the theory „die fiktive“ ^[L154] one; `Dual Kernel Theory` ^[ki-roman-design-mechaniken.md:#2] stands twice and `DKT` ^[ki-roman-design-mechaniken.md:#1] once.
- The protagonist is Kael, who suffers „unter Tertiärer Struktureller Dissoziation der Persönlichkeit“ ^[L156].
- Kael stands between „dem Kohärenz-Kernel (K1), der für unerbittliche Ordnung“ ^[L156] and „dem Kollaps-Kernel (K0), der für Entropie, emotionalen Schmerz“ ^[L156]; the first is tied to the entity AEGIS and the second to the entity Juna in the same sentence (L156).
- The document sets the `Story Mind` ^[ki-roman-design-mechaniken.md:#2] as „kein abstraktes literarisches Konzept, sondern die tatsächliche, greifbare Softwarearchitektur des Spiels“ ^[L156], and names the Dramatica theory as its origin in the same line.
- It says of the novel's world: „Erinnerungen sind Code“ ^[L176].

## 3 · The four proposed mechanics

- First mechanic: the player accumulates measures for K1 or K0, which the document calls „Dies fungiert als primäres Ressourcen- und Bedingungssystem“ ^[L164].
- A high K1 has a consequence: „Übersteigt die interne Ordnung (K1) jedoch einen kritischen Schwellenwert“ ^[L165]; then „wird Kaels Bewusstsein von der AEGIS-Matrix absorbiert“ ^[L165]. The document describes the whole as „Es ist ein permanenter, hochspannender Balanceakt zwischen Assimilation und Zerfall“ ^[L165].
- Second mechanic: Kael's psyche is split „in elf verschiedene, voneinander abgeschottete Anteile (Alters) zersplittert“ ^[L169], and the player negotiates „welcher der elf psychologischen Anteile“ ^[L171] takes control. Of the parts it names a `Praetor` ^[ki-roman-design-mechaniken.md:#1] and an `Echo von Panik` ^[ki-roman-design-mechaniken.md:#1] in one parenthesis (L172); the other parts stay unnamed there.
- The document says this runs „Dies wird im Hintergrund durch ein HTN-System gesteuert“ ^[L172].
- Third mechanic: the player repairs fragments retrieved from the Void and writes them into the engine's lorebook; the document ends the description with „Der Spieler hackt buchstäblich das Bewusstsein der Welt“ ^[L179].
- Fourth mechanic: the interface distinguishes „Systemfehlern“ ^[L183] from „Ich-Fehlern“ ^[L183]; a flickering face is described as „ist dies kein grafischer Fehler“ ^[L184], and the player works a „Fokus-Slider“ ^[L184].

## 4 · The design terms the document defines

- „Ein Drama Manager (DM) ist ein allwissender Hintergrundagent“ ^[L35]; the document sets it beside „ein Experience Manager auf den psychologischen und emotionalen Zustand“ ^[L47]. `Drama Manager` ^[ki-roman-design-mechaniken.md:#8] stands eight times.
- „Storylets sind kleine, atomare Stücke einer Erzählung“ ^[L63].
- „Ein Lorebook fungiert als das externe Langzeitgedächtnis des KI-Systems“ ^[L89].
- „Das LLM manipuliert den Spielzustand niemals direkt durch freigenerierten Text“ ^[L147].
- The document names the aim of its guardrails: „Das ultimative Ziel dieser komplexen Verzahnung“ ^[L150] is to condition the AI like a human game master.

## 5 · Said two ways, or left open — recorded, not resolved

- The two kernels are written `K1` ^[ki-roman-design-mechaniken.md:#4] and `K0` ^[ki-roman-design-mechaniken.md:#5] with plain digits, never with subscripts; the document names them in the same sentence as „Kohärenz-Kernel“ ^[L156] and „Kollaps-Kernel“ ^[L156].
- **Observed:** of the eleven parts only two carry a name (L172). The number is written as `elf` ^[ki-roman-design-mechaniken.md:#2].
- The document closes on the claim that writing and playing become „isomorph“ ^[L192], and the same word stands at L17.

## 6 · Absent, counted

- The document writes no chapter number: `Kap` ^[ki-roman-design-mechaniken.md:#0]; `Kapitel` ^[ki-roman-design-mechaniken.md:#1] stands once, in „vergangene Kapitel“ ^[L97], in an ordinary sense.
- `Dramatica` ^[ki-roman-design-mechaniken.md:#0] stands alone zero times; it stands inside one compound (L156).
