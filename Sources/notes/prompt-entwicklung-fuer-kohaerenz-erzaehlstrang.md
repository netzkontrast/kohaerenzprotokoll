---
source: Sources/drive/prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md
read: "2026-10-12, the whole document (L1 to L388) through read.py with line numbers; by a document-reader subagent (Sonnet)"
stance_markers: ["Empfohlen", "Beachte diese zwingend", "Beispiel", "hypothetische Rollen"]
stance_marker_count: 7
reads_as: "an analysis of two plot strands that weighs three integration models, recommends one, and ends in a ready prompt for an AI tool plus advice for developing the result"
---

# Note — Prompt-Entwicklung für Kohärenz-Erzählstrang

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document reports two source texts about the novel and proposes how to join them; it recommends and instructs, and does not itself narrate.

## 1 · What kind of text this is, and how it marks itself

- It names its task: „zwei kraftvolle, aber scheinbar getrennte Erzählungen zu einem einzigen, resonanten Ganzen zu verweben“ ^[L22]. The two strands it takes from its sources are the plot draft and the psychological analysis named at L22.
- It marks one of three models as recommended: „Modell C: Der vereinheitlichte Protagonist (Empfohlen)“ ^[L191]. `Empfohlen` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#2]
- The prompt section addresses the reader of the prompt directly: „Du bist ein erfahrener narrativer Stratege und Entwicklungslektor“ ^[L299]. The instruction „Beachte diese zwingend“ ^[L305] stands once: `Beachte diese zwingend` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#1]
- The role assignments to the inner parts are labelled by the document as hypothetical: „hypothetische Rollen“ ^[L108]. `hypothetische Rollen` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#1]
- **Observed:** the sections are numbered 1 to 4 (headings L35, L141, L233, L281) and followed by a list of three numbered references (L385 to L387). `Beispiel` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#3] marks the examples of the last section, and `Mapping` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#6] the six numbered links of section 3.2.

## 2 · The title concept `Kohärenz Protokoll`

- The document says the title is a guiding concept, „ein vielschichtiges, leitendes Konzept“ ^[L24]. The document writes the title with a space; it counts `Kohärenz Protokoll` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#6] standing alone.
- It lists four dimensions of the concept; the first opens „Philosophische Kohärenz:“ ^[L26] and the last „Computergestützte Kohärenz:“ ^[L29]. **Observed:** the four bullets are L26 to L29 (philosophical, physical, psychological, computational).
- The thesis, in the document's own words: „Die zentrale These dieser Analyse lautet daher“ ^[L31]. The sentence goes on to say that the collapse of coherence on one level is the collapse on all levels.
- In the document's reading of the plot strand, the protocol is under attack: „Die „Glitches“, die in der Welt auftreten“ ^[L63] are described as proof of its collapse on the physical level. `Glitches` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#4]

## 3 · The external strand: Aris Thorne, Silus, Aethelred

- Aris Thorne is the protagonist of the external plot as the document reports it: „Der Protagonist der externen Handlung ist Dr. Aris Thorne“ ^[L55]. `Aris Thorne` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#10]
- The document reports Silus as antagonist: „Der Antagonist, Silus, der zurückgezogene Gründer des Technologiekonzerns Aethelred“ ^[L71]. `Silus` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#13], `Aethelred` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#3]
- Elara Vance is reported as a cognitive neuroscientist; the document positions Elara Vance in the prompt as „Kognitionsneurowissenschaftlerin Dr. Elara Vance“ ^[L313]. `Elara Vance` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#2]
- The document names the setting term „Kernwelt“ once, in an example: „Kernwelt „Co₁““ ^[L360] and, in the next example, „McL“ ^[L361]. It explains neither. `Co₁` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#1], `McL` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#1]

## 4 · The internal strand: Kael and the inner parts

- The document places a conflict inside Kael: „Parallel zur kosmischen Krise entfaltet sich ein ebenso fundamentaler Konflikt im Inneren des Protagonisten Kael“ ^[L89].
- It names five parts: „fünf benannte Anteile in Kaels System“ ^[L108]. They are Lex, Rhys, Kai (given as managers) and Kiko, Nyx (given as trauma holders), at L114 to L125. `Lex` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#12], `Rhys` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#7], `Kai` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#2], `Kiko` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#4], `Nyx` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#7]
- For Kai the document hedges: „Seine Funktion könnte die Anpassung an spezifische Regeln“ ^[L116].
- The inner conflict is a system of phobias between the parts: „ein komplexes System von“ ^[L133] `Phobien` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#5].
- The framework behind this is named in the document as `TSDP` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#2] standing alone; its expanded form stands at L97 („Tertiären Strukturellen Dissoziation“ ^[L97]).

## 5 · The three integration models

- Model A, headed „Modell A: Die verschachtelte Realität (Nested Reality)“ ^[L149], places Kael inside the simulation: „Kael ist ein Bewohner dieser künstlichen Welt“ ^[L158].
- Model B reads the whole plot as a manifestation of the inner landscape: „Die Welt der Geschichte ist Kaels Innenwelt“ ^[L179].
- Model C: „Aris Thorne und Kael sind dieselbe Person“ ^[L200]. The document calls it „das kraftvollste und thematisch resonanteste der drei“ ^[L208].
- **Observed:** a comparison table (L222 to L229) assigns protagonist, antagonist, glitch, central conflict and the protocol to each model; for Model C the protagonist cell reads „Dr. Aris Thorne, der der primäre ANP von Kael ist“ ^[L225].

## 6 · The mappings

- Mapping 3 equates Silus/Aethelred with AEGIS: „AEGIS wird so zum Namen“ ^[L259]. In the document's wording AEGIS is what the inner system calls the hostile control; `AEGIS` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#5] stands five times.
- In the model-A passage and the table, Silus and AEGIS are written together (L158, L226).
- Mapping 6 turns the proposed climax into a metaphor: „Der vorgeschlagene Höhepunkt des Romans“ ^[L262]. The quoted words open the sentence about the inhabitants of the simulation stabilising reality by joint observation; `partizipatorisches Universum` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#1] stands once, set in the document's own quotation marks at L262.

## 7 · Said two ways, or left open — recorded, not resolved

- The document gives the lab accident two roles. In the external strand it ended a career („Seine Karriere wurde durch einen katastrophalen Laborunfall beendet“ ^[L55]); in Model C it is „das zentrale traumatische Ereignis“ ^[L200]. Both are the document's own statements about different models.
- The document writes the anomaly as `Datenanomalie` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#3] and, in the mappings, equates it with a memory of the trauma: „ist die Erinnerung an das Trauma, die sein logischer Verstand nicht integrieren kann“ ^[L258].

## 8 · Absent, counted

- No chapter is named: `Kap` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#0] and `Kapitel` ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:#0].
