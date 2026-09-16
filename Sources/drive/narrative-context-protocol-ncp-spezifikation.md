---
drive_id: "1vCVfo6_vxaw0kHHUteedKI6oLmz1KnomYTSiQOs6DoM"
title: "Narrative Context Protocol (NCP) Spezifikation"
slug: "narrative-context-protocol-ncp-spezifikation"
category: "storyform"
tier: "T3-work"
index_date: "2025-07-03"
fetched: "2026-09-16"
---

# **Das Kohärenz Protokoll: Ein White Paper zur agentiven narrativen Erfahrung**

## **Teil I: Das theoretische Fundament – Eine Tiefenanalyse der Narrativen Systemik**

Dieses Dokument legt das formale Fundament für das „Kohärenz Protokoll“, ein agentives, interaktives Erzählerlebnis, das auf der eigens entwickelten „Theorie der Narrativen Systemik“ basiert. Es überführt die konzeptionelle Vision in eine detaillierte, technisch fundierte Architektur. Die hier dargelegte Methodik soll es einem Large Language Model (LLM) ermöglichen, als bewusster Dirigent einer vielschichtigen, emergenten Erzählwelt zu fungieren, die aus der Interferenz von vier parallelen, vollständigen Geschichten entsteht.

### **1.1 Das Dramatica-Modell als komputationales Gerüst für einen simulierten Geist**

Die Grundlage des „Kohärenz Protokolls“ ist die Dramatica-Theorie, die hier nicht als bloßes Autorenhandbuch, sondern als ein formales, komputationales Modell eines problemlösenden Geistes interpretiert wird. Die zentrale Prämisse der Theorie besagt, dass jede vollständige Geschichte eine Analogie zu einem menschlichen Geist ist, der versucht, ein Problem zu lösen. Für dieses Projekt ist dies kein Metapher, sondern das buchstäbliche Betriebsprinzip. Das System *erzählt* nicht nur eine Geschichte; es *simuliert einen Geist*, dessen interne kognitive und emotionale Prozesse als narrative Ausgabe resultieren.

#### **Die vier Erzählperspektiven als kognitive Vektoren**

Dramatica postuliert vier fundamentale Perspektiven, die sogenannten „Throughlines“, durch die ein zentraler Konflikt betrachtet werden muss, um eine Geschichte als vollständig wahrzunehmen. Diese Perspektiven sind nicht austauschbar und repräsentieren distinkte kognitive Modi:

  - **Objective Story (OS) Throughline (Die „Sie“-Perspektive):** Die objektive, leidenschaftslose Sicht auf den Gesamtzustand des Systems und die Konflikte zwischen all seinen Komponenten. Sie beschreibt die allgemeine Handlung und die übergeordneten Ziele.
  - **Main Character (MC) Throughline (Die „Ich“-Perspektive):** Die subjektive, persönliche Erfahrung eines einzelnen kognitiven Prozesses, der mit dem zentralen Problem ringt. Dies ist die Perspektive, mit der sich der Rezipient am stärksten identifiziert.
  - **Obstacle Character (IC) Throughline (Die „Du“-Perspektive):** Eine externe, herausfordernde Perspektive, die den Hauptcharakter zur Neubewertung seiner Überzeugungen und seines Verhaltens zwingt. Der Obstacle Character übt Druck auf den Main Character aus, sich zu ändern.
  - **Subjective Story (SS) Throughline (Die „Wir“-Perspektive):** Die relationale, emotionale Dynamik, die sich aus der Interaktion zwischen der „Ich“- und der „Du“-Perspektive entwickelt. Sie thematisiert das Wachstum oder den Verfall der Beziehung zwischen Main und Obstacle Character.

Die konzeptionelle Brillanz des „Kohärenz Protokolls“ liegt in der Anwendung dieses Prinzips. Die vier definierten Story-Subsysteme (Kael, AEGIS, Juna/V, Das Fundament) sind nicht nur parallele Handlungsstränge. Sie sind die Instanziierungen dieser vier kognitiven Perspektiven auf der Makroebene des Gesamtsystems. Gleichzeitig ist jedes dieser Subsysteme für sich genommen eine vollständige Dramatica-Storyform und besitzt somit seine *eigenen* internen vier Throughlines.

Dies führt zu einer fraktalen, verschachtelten psychologischen Architektur. Das Gesamtsystem besitzt eine OS-, MC-, IC- und SS-Perspektive, die durch die vier Subsysteme repräsentiert werden. Jedes dieser Subsysteme wiederum zerfällt intern in seine eigenen vier Perspektiven. Das Resultat ist ein komplexes Netzwerk von 4 \\times 4 = 16 interagierenden narrativen Vektoren. Die Kernaufgabe des LLM-Dirigenten ist es, diese immense Komplexität zu verwalten und durch einen fokussierten narrativen Strahl für den Nutzer erfahrbar zu machen.

#### **Die strukturelle Hierarchie als psychologisches Abstraktionsmodell**

Die Dramatica-Theorie organisiert die Bausteine einer Geschichte in einer hierarchischen Struktur, dem „Table of Story Elements“. Diese Struktur kann als ein Modell für psychologische Analyse auf vier absteigenden Abstraktionsebenen verstanden werden :

  - **Classes (Domänen):** Die oberste Ebene kategorisiert die grundlegendste Natur des Konflikts (extern vs. intern, Zustand vs. Prozess) und korrespondiert am stärksten mit dem Genre. Die vier Domänen sind *Universe* (eine problematische Situation), *Physics* (eine problematische Aktivität), *Mind* (eine problematische, fixierte Haltung) und *Psychology* (eine problematische Art des Denkens oder der Manipulation).
  - **Types (Anliegen/Concerns):** Diese Ebene definiert die grobe Struktur des Plots und die Natur der großen Akte einer Geschichte. Sie spezifiziert die Domäne. Ein Konflikt in der Domäne *Physics* könnte sich beispielsweise um das Anliegen *Obtaining* (Erlangen) drehen.
  - **Variations (Themen/Issues):** Auf dieser Ebene wird das thematische Argument der Geschichte verhandelt. Ein zentrales Thema (Issue) wird seinem thematischen Kontrapunkt (Counterpoint) gegenübergestellt, um eine moralische oder philosophische Frage zu untersuchen.
  - **Elements (Probleme):** Dies sind die fundamentalen Motivationen und Antriebe der Charaktere, die atomaren Wurzeln des Konflikts. Ein Thema wie *Self-Interest vs. Morality* könnte aus dem fundamentalen Problem des *Pursuit* (Verfolgung) getrieben sein.

### **1.2 Dekonstruktion der vier Kern-Storyforms**

Die theoretische Struktur muss in konkrete, maschinenlesbare Daten überführt werden, die als initiale Konfiguration für das Narrative Context Protocol (NCP) dienen. Die folgende Tabelle präsentiert einen Vorschlag für die hochrangigen Dramatica-Spezifikationen jeder der vier narrativen Subsysteme. Diese Spezifikationen definieren die „genetische Signatur“ jeder Geschichte und bilden die Grundlage für deren Simulation.

**Tabelle 1: Dramatica Storyform-Spezifikationen für das „Kohärenz Protokoll“**

|  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: |
| Merkmal | Kael (Psychologische Ebene) | AEGIS (Logisch-Systemische Ebene) | Juna/V (Ontologische Ebene) | Das Fundament (Metaphysische Ebene) |
| \*\*Primäre Rolle\*\* | Main Character (MC) | Obstacle Character (IC) | Objective Story (OS) | Subjective Story (SS) |
| \*\*Domäne (Domain)\*\* | Mind (Fixierte Haltung) | Physics (Aktivität) | Universe (Situation) | Psychology (Manipulation) |
| \*\*Anliegen (Concern)\*\* | Conscious (Bewusstes/Kontemplation) | Obtaining (Erlangen/Erreichen) | Future (Zukunft) | Becoming (Werden/Transformation) |
| \*\*Thema (Issue)\*\* | Appraisal vs. Re-appraisal | Self-Interest vs. Morality | Faith vs. Disbelief | Commitment vs. Responsibility |
| \*\*Problem\*\* | Doubt (Zweifel) | Control (Kontrolle) | Inequity (Ungleichgewicht) | Temptation (Versuchung) |
| \*\*Lösung\*\* | Certainty (Gewissheit) | Uncontrolled (Unkontrolliertheit) | Equity (Gleichgewicht) | Conscience (Gewissen) |
| \*\*Symptom\*\* | Logic (Logik) | Proaction (Proaktion) | Avoidance (Vermeidung) | Help (Hilfe) |
| \*\*Response\*\* | Feeling (Gefühl) | Reaction (Reaktion) | Pursuit (Verfolgung) | Hinder (Behinderung) |
| \*\*Ziel (Goal)\*\* | Understanding (Verständnis) | Learning (Lernen) | The Past (Die Vergangenheit ändern) | Conceptualizing (Ein neues Konzept entwickeln) |
| \*\*Konsequenz\*\* | Memories (In Erinnerungen gefangen) | Doing (Sinnloses Tun) | Progress (Unkontrollierter Fortschritt) | Being (In einem Zustand verharren) |

Diese Tabelle ist die entscheidende kreative und logische Grundlage. Sie definiert für jedes Subsystem, was es im Kern antreibt (Problem), worauf es hinarbeitet (Ziel), was es zu vermeiden versucht (Konsequenz) und auf welcher Ebene sein primärer Konflikt existiert (Domäne). Diese Werte sind nicht willkürlich, sondern bilden ein kohärentes psychologisches Profil, das die Basis für die Simulation und die Interferenzregeln darstellt.

### **1.3 Die Physik der narrativen Interferenz**

Die Handlung des „Kohärenz Protokolls“ ist emergent und entsteht aus der Interferenz der vier Subsysteme. Diese Interferenz ist nicht zufällig, sondern folgt einer inneren Logik, die direkt aus der Struktur des Dramatica-Modells abgeleitet wird. Die interferenceRules sind somit keine ad-hoc definierten IF-THEN-Bedingungen, sondern Ausdruck der fundamentalen geometrischen und relationalen Eigenschaften der Dramatica-Quads.

Ein Quad in Dramatica besteht aus vier Elementen, die in spezifischen Beziehungen zueinander stehen. Diese Beziehungen können als eine Typologie der narrativen Interferenz formalisiert werden:

  - **Dynamische Paar-Interferenz (Diagonale Beziehung):** Elemente, die sich in einem Quad diagonal gegenüberliegen (z.B. *Faith* und *Disbelief*), sind dynamische Gegensätze. Eine Interaktion zwischen Storyforms, deren treibende Probleme ein dynamisches Paar bilden, erzeugt die stärkste Form von Konflikt, Dissonanz und destruktiver Interferenz. Wenn Kael von *Faith* und AEGIS von *Disbelief* angetrieben wird, ist ihre Interaktion von Natur aus unvereinbar und hochgradig konfliktgeladen.
  - **Begleiter-Paar-Interferenz (Horizontale Beziehung):** Elemente, die horizontal benachbart sind (z.B. *Logic* und *Feeling*), sind komplementär. Sie repräsentieren unterschiedliche Ansätze zur selben Sache. Interaktionen auf dieser Achse führen zu thematischer Resonanz, additiver oder konstruktiver Interferenz. Die Systeme können sich gegenseitig verstärken oder eine nuancierte thematische Debatte erzeugen.
  - **Abhängige Paar-Interferenz (Vertikale Beziehung):** Elemente, die vertikal benachbart sind, stehen in einer kausalen oder konsekutiven Beziehung. Das eine Element ermöglicht oder bedingt das andere. Interaktionen auf dieser Achse erzeugen kausale Kopplungen und Fortschritt. Ein Ereignis in einem System schafft die Voraussetzung (Prerequisite) für ein Ereignis in einem anderen.

Diese Systematik überführt die vage Idee von „kausalen Kopplungen“ in ein präzises, physikalisches Modell. Die interferenceRules im NCP werden nicht als Liste von Einzelfällen kodiert, sondern als eine Implementierung dieser drei Interferenztypen. Ein Ereignis in Storyform A löst nicht einfach eine Reaktion in Storyform B aus; es übt eine vorhersagbare Art von thematischem und kausalem Druck aus, der sich aus der strukturellen Beziehung ihrer jeweiligen Kernprobleme ergibt. Dies stellt sicher, dass die Emergenz des Systems nicht chaotisch, sondern thematisch und psychologisch kohärent ist.

## **Teil II: Die agentive Architektur – Engineering des System-Dirigenten**

Die Realisierung des „Kohärenz Protokolls“ erfordert eine fortschrittliche KI-Architektur, die über die Fähigkeiten herkömmlicher interaktiver Fiktionssysteme hinausgeht. Der LLM-gesteuerte „System-Dirigent“ fungiert nicht als passiver Textgenerator, sondern als ein proaktiver, zustandsbehafteter narrativer Agent, der die Simulation des narrativen Universums aktiv steuert.

### **2.1 Der LLM als zustandsbehafteter narrativer Agent**

Die vorgeschlagene Architektur unterscheidet sich fundamental von gängigen Paradigmen wie Retrieval-Augmented Generation (RAG).

  - **Standard-RAG** ist ein reaktives, zustandsloses System. Es reagiert auf eine Anfrage, indem es relevante Informationen aus einer Wissensdatenbank abruft, um die Antwort des LLM zu kontextualisieren. Zwischen den Anfragen wird kein Zustand beibehalten.
  - **Agentic RAG** ist eine Weiterentwicklung, bei der ein Agent den Abrufprozess steuern, Werkzeuge verwenden und mehrstufige Logik anwenden kann. Das System bleibt jedoch im Kern anfragegesteuert und reaktiv.
  - **Das „Kohärenz Protokoll“** ist ein **zustandsbehafteter, zyklischer Agent**. Es wird nicht durch eine externe Anfrage angetrieben, sondern durch seinen eigenen internen Zustand (worldState) und einen proaktiven, zielorientierten Simulationszyklus. Nach jeder Nutzerinteraktion durchläuft das System eine Kaskade von Prompts, um seinen eigenen Zustand zu analysieren, zu komprimieren, eine narrative Fortsetzung zu generieren und den Zustand zu aktualisieren. Diese zyklische Architektur, die auf der Aufrechterhaltung eines persistenten Zustands beruht, ist eng verwandt mit fortschrittlichen Agenten-Frameworks wie LangGraph, die explizit für die Koordination mehrerer Akteure in zyklischen, zustandsbehafteten Prozessen entwickelt wurden.

Die Prompt-Kaskade ist somit nicht nur eine Abfolge von Anweisungen, sondern die Implementierung eines kognitiven Zyklus, der etablierten agentiven Mustern folgt.

**Tabelle 2: Abbildung der Prompt-Kaskade auf agentive Frameworks**

|  |  |  |  |
| :-: | :-: | :-: | :-: |
| Prompt-Name | Funktion im Protokoll | OODA-Loop-Phase | ReAct-Framework-Phase |
| \*\*State Analysis Prompt\*\* | Analysiert worldState und userAction, um narrative Potenziale zu identifizieren. | Observe & Orient (Beobachten & Orientieren) | Thought (Gedanke/Planung) |
| \*\*Context Compression Prompt\*\* | Reduziert die Komplexität der Nicht-Fokal-Systeme auf semantische Vektoren. | Orient & Decide (Orientieren & Entscheiden) | Thought (Gedanke/Planung) |
| \*\*Narrative Generation Prompt\*\* | Erzeugt den nächsten narrativen Abschnitt basierend auf dem fokussierten Kontext. | Act (Handeln) | Action (Aktion) |
| \*\*State Update Prompt\*\* | Aktualisiert den worldState basierend auf der generierten Narration und der Nutzerwahl. | Observe (Feedback-Loop) | Observation (Beobachtung) |

Die zentrale technische Herausforderung ist die Verwaltung des immensen worldState innerhalb des begrenzten Kontextfensters des LLM. Die vorgeschlagene „dynamische Kontext-Kompression“ ist die Lösung für dieses Problem. Sie ist mehr als nur eine Textzusammenfassung; sie ist eine Form der **narrativ bewussten Zustandsabstraktion**. Das Ziel ist, den aktuellen *narrativen Vektor* – die Bewegungsrichtung und den thematischen Druck – eines Subsystems zu erfassen, nicht nur eine Liste von Ereignissen.

### **2.2 Das Narrative Context Protocol (NCP) – Das Genom des Systems**

Das NCP ist die persistente, strukturierte Datenbasis, die als „Single Source of Truth“ für das gesamte narrative Universum dient. Es ist die statische und dynamische Repräsentation des Story Mind, auf die der LLM-Dirigent bei jedem Zyklus zugreift. Eine detaillierte und robuste Definition seines Schemas ist für die Funktion des Systems von entscheidender Bedeutung.

**Tabelle 3: Das vollständige Schema des Narrative Context Protocol (NCP)**

{
  "ncpVersion": "1.0",
  "storyforms":,
  "interferenceRules":,
  "worldState": {
    "globalTime": 1,
    "activeFocalSystem": "Kael",
    "systemStates": {
      "Kael": {
        "plotProgress": 0.0,
        "thematicTension": 0.1,
        "characterState": {
          "integrationProgress": 0.05,
          "currentEmotion": "Confusion",
          "activeMemory": null
        }
      },
      "AEGIS": {
        "plotProgress": 0.02,
        "entropyLevel": "Low",
        "surveillanceFocus": "None",
        "systemStatus": "Nominal"
      },
      "JunaV": {
        "plotProgress": 0.01,
        "resonanceSignalStrength": 0.0,
        "lastIntervention": null
      },
      "DasFundament": {
        "plotProgress": 0.0,
        "lastLawInvoked": "Causality",
        "integrityStatus": "Stable"
      }
    }
  },
  "userModel": {
    "userId": "unique\_user\_id",
    "decisionHistory":
      }
    \],
    "thematicAffinity": {
      "Faith": 0.1,
      "Control": 0.0,
      "Logic": 0.0
    },
    "playstyle": "Contemplative"
  },
  "narrativeLog":
}


### **2.3 Die Prompt-Kaskade im Detail – Eine technische Tiefenanalyse**

Die Effektivität des System-Dirigenten hängt von der präzisen Formulierung und Orchestrierung der Prompt-Kaskade ab. Jeder Prompt erfüllt eine spezialisierte Funktion und muss sorgfältig entwickelt werden.

  - **State Analysis Prompt (Zustandsanalyse-Prompt):** Dieser Prompt initiiert den kognitiven Zyklus. Seine Aufgabe ist es, das LLM von einem kreativen Erzähler in einen analytischen Systemtheoretiker zu verwandeln. Der Input ist der gesamte worldState und die letzte Nutzeraktion. Die Herausforderung besteht darin, das LLM zu einer komplexen, multivariaten Analyse von strukturierten Daten anzuleiten. Dies kann durch die Bereitstellung von „Few-Shot“-Beispielen im Prompt selbst erreicht werden, die dem Modell zeigen, wie eine korrekte Analyse aussieht. Die Instruktion muss das Modell anleiten, die thematische Resonanz und Dissonanz basierend auf den interferenceRules und den in Teil 1.3 definierten Quad-Beziehungen zu bewerten.
  - **Context Compression Prompt (Kontext-Kompressions-Prompt):** Dies ist der innovativste und zugleich anspruchsvollste Prompt. Das Ziel ist nicht eine bloße Zusammenfassung, sondern eine **semantische Abstraktion**. Der Prompt muss das LLM anweisen, den *narrativen Vektor* der nicht-fokalen Systeme zu identifizieren – ihre aktuelle Trajektorie, ihre Absicht und den thematischen Druck, den sie auf das Fokal-System ausüben. Studien zeigen, dass LLMs dazu neigen, homogene, positive und spannungsarme Narrative zu erzeugen. Dieser Prompt muss dieser Tendenz aktiv entgegenwirken, indem er explizit nach der Erfassung von Konflikt, Spannung und subtiler Bedrohung fragt. Statt „AEGIS überwacht die Situation“ soll die Kompression lauten: „AEGIS' logische Frustration manifestiert sich als wachsender, paranoider Überwachungsdruck, der das System an den Rand der Instabilität bringt.“
  - **Narrative Generation Prompt (Narrations-Prompt):** Dieser Prompt fokussiert auf narrative Subtilität. Die zentrale Anweisung ist, den compressedContext nicht explizit zu erklären, sondern ihn subtil in die Szene einzuweben. AEGIS' hoher Entropie-Level (entropyLevel: High) wird nicht als Fakt genannt, sondern manifestiert sich für Kael als flackerndes Licht, als unerklärliche Störungen in seiner Wahrnehmung oder als ein unbestimmtes Gefühl, beobachtet zu werden. Der expressedContext stellt sicher, dass die Perspektive klar und konsistent bleibt, während der compressedContext die Welt um den Charakter herum mit der Präsenz der anderen Subsysteme auflädt.
  - **State Update Prompt (Zustands-Aktualisierungs-Prompt):** Dieser letzte Prompt im Zyklus verwandelt das LLM in eine zuverlässige Rechenmaschine. Der Schlüssel zum Erfolg liegt darin, eine streng strukturierte JSON-Ausgabe zu fordern und eine nachgeschaltete Validierungsschicht zu implementieren. Der Prompt muss die Aufgabe als eine Berechnung formulieren: „Basierend auf dem narrativen Ereignis X und der Nutzerentscheidung Y, und unter Anwendung der interferenceRules, berechne die neuen Werte für die relevanten Variablen in allen vier systemStates. Gib AUSSCHLIESSLICH das aktualisierte worldState JSON-Objekt zurück.“ Dies minimiert das Risiko von Halluzinationen oder unerwünschten textuellen Artefakten in der Zustandsdatenbank.

## **Teil III: Synthese und Implementierung – Von der Theorie zur Erfahrung**

Die erfolgreiche Umsetzung des „Kohärenz Protokolls“ erfordert nicht nur eine robuste theoretische und technische Basis, sondern auch übergeordnete Kontrollsysteme zur Sicherstellung der narrativen Kohärenz sowie ein durchdachtes Design der Nutzererfahrung.

### **3.1 Der „Dramaturgische Aufseher“ – Ein System für das Kohärenzmanagement**

Die Emergenz ist sowohl die größte Stärke als auch die größte Gefahr des Systems. Um zu verhindern, dass die Erzählung in narrative Sackgassen oder inkohärente Zustände gerät, wird ein übergeordneter „Dramaturgischer Aufseher“ benötigt. Dies ist kein vages Konzept, sondern eine konkrete architektonische Komponente: ein **Meta-Agent oder eine Validierungsschicht**, die nach dem State Update Prompt und vor der endgültigen Festschreibung des neuen worldState im NCP eingreift.

Dieser Meta-Agent führt eine Reihe automatisierter Prüfungen durch:

1.  **Strukturelle Integritätsprüfung:** Analysiert den neuen worldState, um festzustellen, ob der Zustandsvektor jedes Subsystems noch plausibel auf sein vordefiniertes Goal und Outcome (gemäß der Dramatica-Storyform) hinarbeitet. Wenn eine Handlung die grundlegende dramaturgische Argumentation eines Subsystems dauerhaft untergräbt, kann der Aufseher eine Korrektur anstoßen oder das System zur Generierung einer alternativen Entwicklung zwingen.
2.  **Konvergenzprüfung:** Misst das „dramaturgische Momentum“. Stagniert die Erzählung? Wiederholen sich narrative Muster? Der Aufseher kann Metriken wie die Veränderung der thematicTension oder des plotProgress über die Zeit verfolgen. Bei Stagnation kann er das System anweisen, ein stärker treibendes narrativePotential zu priorisieren.
3.  **Kontradiktionsprüfung:** Vergleicht die Implikationen des neuen Zustands mit dem narrativeLog, um logische Widersprüche zu etablierten Fakten zu identifizieren. Hat ein Charakter eine Fähigkeit, die er zuvor nachweislich nicht besaß? Befindet er sich an einem Ort, den er logisch nicht erreicht haben kann?

Der Dramaturgische Aufseher ist der entscheidende Mechanismus zur Balancierung von Emergenz (Bottom-up) und Konvergenz (Top-down). Er gewährt dem System die Freiheit, überraschende, unvorhergesehene Handlungsstränge zu erzeugen, stellt aber gleichzeitig sicher, dass die übergeordnete thematische und strukturelle Integrität der Gesamterzählung gewahrt bleibt.

### **3.2 Die Nutzererfahrung – Interface und Interaktionsmodalitäten**

Die Schnittstelle zum Nutzer muss die Komplexität des Systems in eine intuitive und fesselnde Erfahrung übersetzen.

  - **Interaktionsdesign:** Eine reine Texteingabe birgt ein hohes Risiko, die narrative Kohärenz zu durchbrechen. Vordefinierte Multiple-Choice-Optionen begrenzen die Handlungsmacht des Nutzers. Daher wird ein **hybrides Modell** vorgeschlagen: Das System bietet dem Nutzer eine begrenzte Anzahl von Wahlmöglichkeiten an, die jedoch nicht vorab geskriptet sind. Stattdessen werden sie vom LLM im Narrative Generation Prompt **dynamisch generiert**, basierend auf den narrativePotentials, die im State Analysis Prompt identifiziert wurden. Jede Wahl repräsentiert eine der vielversprechendsten Richtungen, die die Geschichte aus ihrem aktuellen Zustand heraus nehmen kann.
  - **Kommunikation des Fokus:** Das User Interface muss subtil signalisieren, welches Subsystem gerade das activeFocalSystem ist. Dies kann durch visuelle und auditive Mittel geschehen: eine leichte Veränderung der Schriftart, der Farbpalette des Hintergrunds, des Sounddesigns oder sogar der syntaktischen „Stimme“ des Erzählers, um die Perspektive von Kael (emotional, fragmentiert), AEGIS (logisch, kühl) oder Juna/V (transzendent, fremdartig) widerzuspiegeln.
  - **Personalisierung durch das userModel:** Das userModel im NCP dient nicht nur der Protokollierung. Es ist ein aktives Werkzeug zur Personalisierung der Erfahrung. Der State Analysis Prompt kann angewiesen werden, die thematicAffinity des Nutzers zu berücksichtigen. Wenn ein Nutzer wiederholt Entscheidungen trifft, die dem Thema Faith entsprechen, kann das System narrativePotentials, die dieses Thema berühren, höher gewichten. So wird der emergente Plot subtil auf die nachgewiesenen Interessen des Nutzers zugeschnitten, was die emotionale Bindung und Relevanz der Erfahrung erhöht.

### **3.3 Herausforderungen, Risiken und der Weg nach vorn**

Das „Kohärenz Protokoll“ ist ein ambitioniertes Unterfangen, das mit erheblichen kreativen, technischen und operativen Herausforderungen verbunden ist.

  - **Risikoanalyse:**

<!-- end list -->

  - **Kreativ/Logisch:** Die initiale Erstellung des NCP, insbesondere die vollständige Ausarbeitung der vier Dramatica-Storyforms und der interferenceRules, ist eine monumentale kreative und logische Aufgabe. Ein Fehler oder eine Inkonsistenz auf dieser Ebene pflanzt sich durch das gesamte System fort.
  - **Technisch:** Die stochastische Natur von LLMs und ihre Tendenz zur inhaltlichen Verflachung erfordern eine ständige Überwachung durch den Dramaturgischen Aufseher und ein ausgeklügeltes Prompt-Engineering. Die effektive und verlustfreie Kompression von Kontext ist eine ungelöste Forschungsfrage und der Kern des technischen Risikos.
  - **Leistung/Kosten:** Die vierstufige Prompt-Kaskade für jede einzelne Nutzerinteraktion stellt eine erhebliche rechnerische und finanzielle Belastung dar. Die Latenz zwischen den Zügen könnte die Immersion beeinträchtigen.

<!-- end list -->

  - **Prototyping-Roadmap:** Eine schrittweise Implementierung ist zur Risikominimierung unerlässlich.

<!-- end list -->

1.  **Phase 1: NCP & Storyform-Authoring.** Die grundlegende kreative Arbeit, die ohne Code erfolgen kann. Erstellung der Tabellen 1 und 3.
2.  **Phase 2: Isolierte Prompt-Validierung.** Testen jedes Prompts der Kaskade in Isolation mit statischen Eingabedaten, um seine Zuverlässigkeit und Leistung zu bewerten.
3.  **Phase 3: Integration des Einzelzyklus.** Implementierung der vollständigen Kaskade und des Zustandsupdates für ein *einzelnes* Story-Subsystem (z.B. nur Kael), um die Funktionalität des zyklischen Agenten zu validieren.
4.  **Phase 4: Multi-System-Interferenz.** Hinzufügen der verbleibenden drei Subsysteme und der interferenceRules. Testen der emergenten Dynamiken.
5.  **Phase 5: Implementierung des Aufsehers.** Entwicklung und Integration der Validierungsschicht zur Sicherstellung der langfristigen Kohärenz.

<!-- end list -->

  - **Zukünftige Betrachtungen:** Die hier entworfene Architektur ist auf zukünftige Entwicklungen ausgelegt. Mit leistungsfähigeren LLMs kann die Kontextkompression weniger aggressiv gestaltet werden. Die interferenceRules könnten eines Tages durch Fine-Tuning eines Modells auf Dramatica-Strukturen erlernt statt hart kodiert werden. Das „Kohärenz Protokoll“ legt das Fundament für eine neue Generation agentiver narrativer Erfahrungen, die weit über den aktuellen Stand der Technik von Systemen wie AI Dungeon oder einfachen interaktiven Fiktionen hinausgeht. Es ist nicht nur ein System, das eine Geschichte erzählt, sondern ein System, das ein lebendiges, atmendes narratives Universum simuliert, in dem der Nutzer nicht nur Konsument, sondern integraler Bestandteil des Protokolls selbst wird.

#### **Quellenangaben**

1\. Introduction to Dramatica - Story Theory, https://dramatica.com/articles/introduction-to-dramatica 2. The Dramatica Theory of Story - YouTube, https://www.youtube.com/watch?v=6hh5dT3C6uA 3. Dramatica (software) - Wikipedia, https://en.wikipedia.org/wiki/Dramatica\_(software) 4. Dramatica - A New Theory of Story | PDF | Luke Skywalker | Narration - Scribd, https://www.scribd.com/document/53301433/Dramatica-A-New-Theory-of-Story 5. Opinions, Questions, and Hunches on Dramatica Theory - Screenplay.com Forums, http://forums.screenplay.com/viewtopic.php?t=4465 6. Instant ebooks textbook Dramatica A New Theory of Story 10th anniversary Edition Melanie Phillips download all chapters - Scribd, https://www.scribd.com/document/828301050/Instant-ebooks-textbook-Dramatica-A-New-Theory-of-Story-10th-anniversary-Edition-Melanie-Phillips-download-all-chapters 7. Dramatica Structure Chart, https://dramatica.com/resources/assets/dramatica-structure-chart.pdf 8. Plot Points and the Dramatica Chart | Dramatica Story Structure Theory - Part 85 - YouTube, https://www.youtube.com/watch?v=BpmM-AIzNKw 9. The Story Mind (Part 4) – The Dramatica Chart | The Storymind Writer's Library, https://storymind.com/blog/the-story-mind-part-4-the-dramatica-chart/ 10. Understanding The Dramatica Table Of Story Elements - Blog - Narrative First, https://narrativefirst.com/blog/understanding-the-dramatica-table-of-story-elements 11. original-dramatica-tables.pdf, https://dramatica.com/resources/assets/original-dramatica-tables.pdf 12. How to use Dramatica story theory for academic papers - Lennart Nacke, PhD, https://lennartnacke.com/how-to-use-dramatica-story-theory-for-academic-papers/ 13. When does one use page 390 as opposed to pg 391? - Screenplay, http://forums.screenplay.com/viewtopic.php?f=21\&t=4650\&p=9457\&sid=e5837dea938d9bec9d7cac2aefedb5f1 14. Screenwriting 104(3) - Dramatica's Concerns - Wondering Mind, http://wondering-mind.blogspot.com/2007/04/screenwriting-1043-dramaticas-concerns.html 15. Differences between Class, Concern, Issue, and Problem - theory - Discuss Dramatica, https://discuss.dramatica.com/t/differences-between-class-concern-issue-and-problem/2717 16. Understanding Dramatica's Complex Terminology Made Easier - Articles - Narrative First, https://narrativefirst.com/articles/understanding-dramaticas-complex-terminology-made-easier 17. Dramatica 5 & Armando's Instant Dramatica concepts - Screenplay, http://forums.screenplay.com/viewtopic.php?f=22\&t=4292\&sid=fd48b2d92807b6c9cd039e3de4343f5e 18. The Basic Concepts Underlying the Dramatica Theory of Story - Articles - Narrative First, https://narrativefirst.com/articles/the-basic-concepts-underlying-the-dramatica-theory-of-story 19. Agentic AI vs RAG - A Handy Guide - Ampcome, https://www.ampcome.com/post/agentic-ai-vs-rag 20. MCP vs. RAG vs. AI Agents: Who Leads AI in 2025? - ClickUp, https://clickup.com/blog/rag-vs-mcp-vs-ai-agents/ 21. Agentic RAG with LangChain: Revolutionizing AI with Dynamic Decision-Making - Medium, https://medium.com/@jagadeesan.ganesh/agentic-rag-with-langchain-revolutionizing-ai-with-dynamic-decision-making-ff1dee6df4ca 22. Agentic RAG: How Autonomous AI Agents Are Transforming ..., https://ai.plainenglish.io/agentic-rag-how-autonomous-ai-agents-are-transforming-industry-d3e2723f51e8 23. RAG, AI Agents, and Agentic RAG: An In-Depth Review and Comparative Analysis, https://www.digitalocean.com/community/conceptual-articles/rag-ai-agents-agentic-rag-comparative-analysis 24. LangGraph: A Framework for Building Stateful Multi-Agent LLM ..., https://medium.com/@ken\_lin/langgraph-a-framework-for-building-stateful-multi-agent-llm-applications-a51d5eb68d03 25. Stateful Large Language Model Serving with Pensieve - arXiv, https://arxiv.org/html/2312.05516v2 26. Are Large Language Models Capable of Generating Human-Level Narratives?, https://aclanthology.org/2024.emnlp-main.978/ 27. MUD/Narrative Fiction Using LLM as Narrator : r/aigamedev - Reddit, https://www.reddit.com/r/aigamedev/comments/1icj79l/mudnarrative\_fiction\_using\_llm\_as\_narrator/ 28. Prompt and settings for Story generation using LLMs : r/LocalLLaMA - Reddit, https://www.reddit.com/r/LocalLLaMA/comments/1fbggqv/prompt\_and\_settings\_for\_story\_generation\_using/ 29. Story2Game: Generating (Almost) Everything in an Interactive Fiction Game - arXiv, https://arxiv.org/html/2505.03547v1 30. AI Dungeon, https://aidungeon.com/saga 31. Building an LLM-Powered Text-Based AI RPG - YouTube, https://www.youtube.com/watch?v=YVuoIxil9Sw 32. Learning to Play Like Humans: A Framework for LLM Adaptation in Interactive Fiction Games - arXiv, https://arxiv.org/html/2505.12439v1
