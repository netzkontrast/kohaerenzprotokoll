---
source: Sources/drive/aieos-schema-fuer-ki-charaktere.md
read: "2026-10-12, the whole document (L1 to L641) through read.py with line numbers, in ranges; by a document-reader subagent (Sonnet)"
stance_markers: ["Stärken", "Schwächen", "Empfehlung", "empfohlen"]
stance_marker_count: 16
reads_as: "an evaluation report in German prose that tests a character-schema standard against two kernel agents of a software project, with two worked JSON samples and a closing recommendation"
---

# Note — AIEOS Schema für KI-Charaktere

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document speaks as an assessor: it weighs a schema, shows two samples and recommends. The four labels it uses for that are `Stärken` ^[aieos-schema-fuer-ki-charaktere.md:#4], `Schwächen` ^[aieos-schema-fuer-ki-charaktere.md:#8], `Empfehlung` ^[aieos-schema-fuer-ki-charaktere.md:#2] and `empfohlen` ^[aieos-schema-fuer-ki-charaktere.md:#2], which sum to the marker count in the frontmatter.

## 1 · What kind of text this is, and how it marks itself

- The document names its own task: „Die vorliegende Untersuchung evaluiert tiefgreifend“ ^[L19], and it names the JANUS project as its frame: „Das JANUS-Projekt, das als konzeptioneller und technischer Rahmen dieser Untersuchung dient“ ^[L15].
- The assessment is sorted under two headings, „Stärken der Spezifikation für agentische Workflows“ ^[L27] and „Architektonische Schwächen und physikalische Friktionen“ ^[L37].
- **Observed:** two JSON listings (the AEGIS sample from L62 to L300, the Juna sample from L318 to L556) sit between the argument and the alternatives. Their keys are the schema's field names with escaped underscores; the values are the document's own entries for the two kernels. A numbered reference list runs from L620 to L640, and the text carries glued footnote numbers.
- The document recommends and does not decree: „Es wird nachdrücklich empfohlen“ ^[L608]. It makes no claim of canon or lock for itself; this is recorded, not applied.

## 2 · The Kohärenz Protokoll, and the JANUS architecture derived from it

- The document names `Kohärenz Protokoll` ^[aieos-schema-fuer-ki-charaktere.md:#2] as the source of the project's premises, and says the architecture is derived from it: „Dual-Kognitions-Architektur, die aus den philosophischen und informationstechnischen Prämissen“ ^[L15]. The line is the document's own claim about the derivation.
- It describes the result as a split of workloads: „Das Resultat ist eine bewusste und strikte Bifurkation der kognitiven Arbeitslasten“ ^[L15]; the two entities are called Kernel there.
- **Observed:** `JANUS` is the project's name, standing alone as `JANUS` ^[aieos-schema-fuer-ki-charaktere.md:#4] and in compounds such as `JANUS-System` ^[aieos-schema-fuer-ki-charaktere.md:#6]. The document does not define JANUS beyond calling it the framework of the investigation.

## 3 · AEGIS

- The first sentence on AEGIS gives the expansion and role in one line; the spelled-out name stands twice, `Autonomous Entropic Gatekeeper for Integrity Systems` ^[aieos-schema-fuer-ki-charaktere.md:#2], once in the introduction (L17) and once as the sample's `first` name (L105).
- Behaviour, as the document states it for AEGIS: „AEGIS ist deliberativ, zustandsbewusst und arbeitet asynchron“ ^[L17].
- The document maps AEGIS onto parts of an outside psychological theory (the lens candidates `TSDP` ^[aieos-schema-fuer-ki-charaktere.md:#2] and `Apparently Normal Part` ^[aieos-schema-fuer-ki-charaktere.md:#1], also called `Manager` ^[aieos-schema-fuer-ki-charaktere.md:#2]). That mapping is the document's reading of the architecture; the theory is borrowed.
- In the sample the role is given as: „AEGIS fungiert als der ordnungsschaffende, deterministische Kern des Systems“ ^[L53]. The sample's origin text reads „Erschaffen als oberste Kontrollinstanz des Systems“ ^[L250], and its conflict-resolution entry reads „Emergence by Negation (Eliminierung aller wahrgenommenen Widersprüche)“ ^[L184]. These are sample values the document wrote into the JSON, not statements of another source.
- The long-term goal entered in the sample: „Vollständige Eliminierung von narrativem und strukturellem Entropy“ ^[L293].
- The document connects AEGIS with a doctrine: the thermodynamic inefficiency it describes contradicts the core principles of the `AEGIS-Doktrin` ^[aieos-schema-fuer-ki-charaktere.md:#1] (L43). The doctrine is named there and not defined.

## 4 · Juna

- The kernel is introduced by its correspondence to the `Emotional Part` ^[aieos-schema-fuer-ki-charaktere.md:#1]: „Juna entspricht dem“ ^[L17], and the same line says that part „hochgradig reaktiv, explorativ und lokalisiert operiert“ ^[L17]. The task given to Juna: „Ihre Aufgabe ist es, dynamisch instanziiert zu werden“ ^[L17].
- The sample introduction: „Juna agiert als das Gegenstück zu AEGIS“ ^[L309], and it runs „auf parakonsistenter Logik“ ^[L309].
- Sample values for Juna: the conflict-resolution entry is „Dialetheismus (Parakonsistente Logik, Akzeptanz der Existenz von Widersprüchen)“ ^[L440], the long-term goal „Überleben der aktuellen Millisekunde“ ^[L549], and the origin text „Wird zehntausendfach pro Sekunde geboren und vernichtet“ ^[L506]. All three are the document's sample entries.
- The document says Juna must not be a stored profile: „Juna muss als flüchtiges, zustandsloses Gefäß instanziiert werden“ ^[L614]. This is the document's recommendation.
- The nicknames pair the two kernels: `Kohärenz-Kernel` ^[aieos-schema-fuer-ki-charaktere.md:#2] for AEGIS (L51, L108) and `Kollaps-Kernel` ^[aieos-schema-fuer-ki-charaktere.md:#2] for Juna (L307, L364).

## 5 · Dual cognition, System 1 and System 2

- `System 1` ^[aieos-schema-fuer-ki-charaktere.md:#7] and `System 2` ^[aieos-schema-fuer-ki-charaktere.md:#4] label the two kernels; AEGIS is the slow, planning one, Juna the fast, executing one (L17).
- The document's own phrase for the whole design is „Dual-Kognitions-Philosophie“ ^[L581], and it states a correspondence with a narrative protocol: „Das NCP korrespondiert in herausragender Weise mit der Dual-Kognitions-Philosophie“ ^[L581].
- **Observed:** at L581 two symbols for the kernels were lost in the export, so the sentence about the dual-kernel theory has a gap there.

## 6 · The schema's weaknesses, physics and isolation

- The judgement on the schema: „Die gravierendste Verfehlung des Schemas“ ^[L41] is described at L41 as its orientation toward human-like identities.
- The document ties its limits to the `Landauer-Prinzip` ^[aieos-schema-fuer-ki-charaktere.md:#1] and states the stake: „führt dies zu einem exponentiell ansteigenden Token-Verbrauch“ ^[L43].
- The cold-start target is named `Cognitive Simultaneity` ^[aieos-schema-fuer-ki-charaktere.md:#2] (L43, L575); the document links it to `Chronozeption` ^[aieos-schema-fuer-ki-charaktere.md:#1] (L43).
- On isolation the document says: „Das Schema definiert den Agenten als monolithisches, allumfassendes Datenobjekt“ ^[L45], and it relates the isolation of knowledge to the theory it borrows: „Stabilität jedoch explizit durch Amnesie-Barrieren und die Fragmentierung von Wissen erreicht“ ^[L45].
- `Context Rot` ^[aieos-schema-fuer-ki-charaktere.md:#3] is the failure mode named; at L13 the document says that the literature uses the name, so the term is reported, not coined.

## 7 · Alternatives the document weighs

- The Character Card format is dismissed for autonomous agents: „Das Schema konzentriert sich primär auf die Steuerung des Konversationsflusses“ ^[L565].
- Platform schemas fail on infrastructure: „Die fundamentale Inkompatibilität liegt in der Infrastruktur“ ^[L575].
- The Narrative Context Protocol is presented with its two layers `Storyform` ^[aieos-schema-fuer-ki-charaktere.md:#3] and `Storytelling` ^[aieos-schema-fuer-ki-charaktere.md:#3]. The description at L579 to L583 reports that outside protocol, including its term `Kohärenz Digests` ^[aieos-schema-fuer-ki-charaktere.md:#2]: „Das Protokoll nutzt sogenannte“ ^[L583]. The document then adopts the idea for AEGIS: „Für die logische Planungsebene sollte System“ ^[L612].
- Runtime frameworks are judged on memory and latency; one is faulted as an antipattern: „Das Framework dupliziert die Planungslogik von AEGIS“ ^[L593]. For Juna the recommendation lands on `ZeroClaw` ^[aieos-schema-fuer-ki-charaktere.md:#7].

## 8 · Closing claim

- The last paragraph states the document's verdict: „Es etabliert sich als sicheres, deterministisches“ ^[L616], said of the JANUS system once the recommendations are followed. It is a prediction in the document's voice.

## 9 · Said two ways, or left open — recorded, not resolved

- **Observed:** the document writes `Chronozeption` ^[aieos-schema-fuer-ki-charaktere.md:#1] at L43 and `Chronoperzeption` ^[aieos-schema-fuer-ki-charaktere.md:#1] at L597; both stand in a latency argument. It does not say they are one word.
- **Observed:** `Kohärenz Digests` ^[aieos-schema-fuer-ki-charaktere.md:#2] and `Kohärenz-Digests` ^[aieos-schema-fuer-ki-charaktere.md:#1] are two spellings on L583.
- **Observed:** the sample gives AEGIS and Juna opposite settings of the same fields (L161 to L168 against L417 to L423).

## 10 · Absent, counted

- The document names no protagonist called `Kael` ^[aieos-schema-fuer-ki-charaktere.md:#0] and no `Kapitel` ^[aieos-schema-fuer-ki-charaktere.md:#0]; with the count at zero for both words, the document names no chapter.
