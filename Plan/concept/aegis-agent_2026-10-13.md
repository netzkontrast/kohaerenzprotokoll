# AEGIS als Agent, Autorenwerkzeug und spielbare Romaninstanz

Stand: 13.10.2026. Untersuchung von `netzkontrast/kohaerenzprotokoll`, Main-Commit `82a9a42d60528ac474d98a603738ffb480e726b2`. Dies ist ein Implementierungsvorschlag, keine Kanonentscheidung. Die genannten neuen Befehle und Dateien existieren noch nicht.

## Empfehlung

AEGIS zuerst als begrenzten Figuren-Agenten in einer lokalen, reproduzierbaren Szenensimulation bauen. Dieselbe Simulation unterstützt anschließend das Schreiben und eine spielbare Romanfassung. Der verbindende Kern sind Figurenwissen, beobachtbare Handlungen und dauerhafte Konsequenzen.

AEGIS ist dabei eine Figur mit einer falschen Vorstellung davon, was die Welt braucht. Die Software, die seine Handlungen ausführt, muss zuverlässiger sein als die Figur. AEGIS darf Erinnerungen innerhalb einer Simulation unterdrücken; es erhält keine Rechte, Forschungsquellen, Manuskript oder Kanon zu löschen. Der menschliche Autor entscheidet weiterhin über den Roman.

Der erste Prototyp benötigt keine neue Graphdatenbank, keinen MCP-Server und keinen permanent laufenden Agentenschwarm. Er braucht einen kleinen deterministischen Ablauf, einen erlaubnisgefilterten Kontext und gespeicherte Modellvorschläge. Modellaufrufe bleiben seriell; mehrere simulierte Figuren bedeuten keine parallelen kostenpflichtigen Aufrufe.

## 1. Was im Repository schon trägt

| Vorhanden | Nutzen für den Agenten | Grenze |
|---|---|---|
| `Manuscript/kanon.md` | Autorentscheidungen als oberste Inhaltsgrundlage | Arbeitskarten und Quellen sind dadurch nicht automatisch Kanon |
| `Plan/storyform/a.json`, `b.json`, `weave.json`, `development.json`, NCP | Rollen, Aktrhythmus und geplante dramatische Aufgaben | Formale Zulässigkeit beweist keine literarische Qualität |
| `Manuscript/figuren/aegis.md` | Erste Motivation und vorgeschlagene Stimme | Die Karte nennt sich Arbeitsstand; ihre Kanonsektion ist leer |
| `Plan/storyform/clock-b.json` | Vorlage für AEGIS’ Abwärme-Uhr | Prozentwerte sind ausdrücklich Vorschläge, keine physikalisch validierte Simulation |
| `scripts/ask.py`, `pack.py`, `kg.py` | Evidenz suchen und begrenzt verpacken | Forschungspacks sind noch keine erlaubnisgefilterten Figurenkontexte; `pack.py` budgetiert UTF-8-Bytes |
| `scripts/lmrun.py`, `he_claude.py` | Vorhandene Modellpfade und Aufrufprotokollierung | `lmrun.py` ist DSPy-bezogen; ein CLI-Aufruf braucht einen tatsächlich passenden Adapter |
| `scripts/sessions.py`, `ui.py`, `web.py`, `agents/`-Exporte | Arbeitskoordination und statische Darstellung | Das Session-Board verwaltet Entwicklungsarbeit, keine Romanfiguren |
| `.agents/skills/writing-skills/` und spezialisierte Schreibskills | Figurenkarten, Dialogübungen, Szenenarchitektur, Kritik | Autorenhilfe, kein nachgewiesener autonomer Romanautor |

Wichtige Aktualitätsfalle: `SPEC.md` und ältere Konzeptseiten enthalten historische Zustände. Beispielsweise nennt SPEC fehlende Kanonregeln, während inzwischen `Manuscript/kanon.md` existiert. Die Figurenkarte lässt den Zustand nach dem Vortex offen, der Kanon hat Q8 aber beantwortet. Implementierung gegen konkrete aktuelle Dateien prüfen, nicht gegen die älteste Beschreibung.

## 2. Die relevanten Quellen in `Sources/`

Die folgenden Dokumente wurden gezielt untersucht. Das ist eine Forschungslektüre für diesen Plan, kein neuer vollständiger Ingest mit Census und Reconciliation.

| Quelle | Verwendbare Idee | Kritischer Vorbehalt |
|---|---|---|
| [UI-Konzept für Roman-Entwicklungssystem](https://github.com/netzkontrast/kohaerenzprotokoll/blob/82a9a42d60528ac474d98a603738ffb480e726b2/Sources/drive/ui-konzept-fuer-roman-entwicklungssystem.md), insbesondere Z. 21–41 und 71–165 | Novelcrafter: Codex und zeitliche Progressions; Articy:draft: Handlungsfluss; Autor als Dirigent | Das Dokument ist Forschung. Es verwendet elf Anteile statt der aktuellen dreizehn und vertauscht in §6.2 die Wahrheitspositionen. Seine Aussagen über Produkte sind historische Bewertungen, keine aktuelle Marktprüfung |
| [Dramatica, Agentic Storyform Interactive Novel](https://github.com/netzkontrast/kohaerenzprotokoll/blob/82a9a42d60528ac474d98a603738ffb480e726b2/Sources/drive/dramatica-agentic-storyform-interactive-novel.md), Z. 165–244 | Director, begrenzte NPC-Beliefs, getrennte Weltzustände, Storyform-Lookup, Konsequenzen | Die behauptete automatische thematische Kohärenz ist keine gemessene Garantie. Ein Storyform-Problem lässt sich nicht generell wie ein einfaches lösbares Planungsziel behandeln |
| [An Isomorphic Architecture for Agent-Based Narrative Systems](https://github.com/netzkontrast/kohaerenzprotokoll/blob/82a9a42d60528ac474d98a603738ffb480e726b2/Sources/drive/the-kohaerenz-protokoll-an-isomorphic-architecture-for-agent.md), Z. 34–38 und 148–173 | Epistemische Isolation; Kommunikation über eine Environment Loop | Beschriebene Gemini-Prozesse, Librarian und Shadow Git sind Quellenvorschläge, keine nachgewiesene aktuelle Repo-Implementierung. Keine automatische Auswahl eines „Gewinnerplots“ als Kanon |
| [KI-Agenten: Kohärenz und Prompt-Generierung](https://github.com/netzkontrast/kohaerenzprotokoll/blob/82a9a42d60528ac474d98a603738ffb480e726b2/Sources/drive/ki-agenten-kohaerenz-und-prompt-generierung.md), Z. 25–27, Abschnitte zu MOCs und Meta-Prompting | Kleiner aufgabenbezogener Kontext; persistente Erinnerung; Promptverbesserungen vorschlagen | Autonome Selbstoptimierung ist hier eine Hypothese. Verbesserungen gegen feste Fälle messen; keine selbstgeschriebenen Systemregeln ungeprüft übernehmen |
| [Spec-Entwicklung für Agentic Dramatica Roman](https://github.com/netzkontrast/kohaerenzprotokoll/blob/82a9a42d60528ac474d98a603738ffb480e726b2/Sources/drive/spec-entwicklung-fuer-agentic-dramatica-roman.md), Phasen/Failure Modes, Z. 590 | Phasenrechte, Recovery, Tool-Verträge; Verweis auf Anthropic-Tooldesign | Die MCP-Architektur ist kein Bedarf dieses Projekts. CLI/Funktionsadapter erfüllen denselben Zweck |
| [The Writer’s Room Blueprint](https://github.com/netzkontrast/kohaerenzprotokoll/blob/82a9a42d60528ac474d98a603738ffb480e726b2/Sources/drive/the-writer-s-room-blueprint-coherence-protocol.md), Z. 35–122 | Szenen als Ziel, Konflikt und Konsequenz statt bloßer Beschreibung | Ältere Handlungsversion; keinen alten Ausgang oder Figurenstatus in den aktuellen Plot zurückimportieren |

Zusätzlich entdeckt: `Sources/drive/kael-charakterarchitektur-und-konfliktdynamik.md` ist ausdrücklich als Novelcrafter-Vorlage angelegt. `prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md` behandelt vor allem die Synthese älterer Erzählstränge, einschließlich Aris Thorne und Silus. Das Wort „Prompt“ im Titel macht es nicht zur aktuellen Agentenspezifikation.

## 3. Was AEGIS tatsächlich simulieren soll

In Storyform B ist AEGIS Main Character, Protagonist und Reason. Es ist Do-er und Steadfast; seine Unique Ability ist Control, sein Critical Flaw Oppose. B hat Failure/Bad und läuft laut Q8 bis Kap 39. Das ist ein wesentlich interessanterer Agent als ein generischer böser Chatbot: Er verfolgt ein nachvollziehbares Ziel und verschlimmert seine Lage durch die eigene Methode.

Der Kanon hält fünf Guardians fest: LogOS, Mnemosyne, Cerberus, Kairos und Sophia. Die Dramatica-Funktion „Guardian“ ist davon verschieden: In B trägt Sophia den Guardian-Archetyp, Mnemosyne Contagonist, LogOS Sidekick, Kairos Skeptic; Cerberus ist ohne Archetyp. Diese Begriffe beim Agentenrouting auseinanderhalten.

AEGIS erhält pro Szene beobachtete Anomalien, Aufträge, bekannte Behauptungen und erlaubte Operationen. Es kann beispielsweise prüfen, eine Grenze sichern, einen Sweep beantragen, eine Erinnerung maskieren oder eine Operation zurückstellen. Der Ablauf entscheidet über Reichweite, Kosten und sichtbare Folgen. Innere Prosa Kaels und unveröffentlichte Autorentscheidungen stehen ihm nicht pauschal zur Verfügung.

Nach Kap 39 erlischt AEGIS-monolithisch und AEGIS-plural entsteht; Oblivion übernimmt in Kael die Funktion wählend. Ein freundlicher Selbstreflexionsprompt darf diesen festgelegten B-Verlauf nicht schon in Akt I „heilen“. Für eine alternative spielbare Adaption wäre eine andere Entwicklung ausdrücklich als Variante zu kennzeichnen.

AEGIS’ Ich in Kap 0, 6, 16, 22, 28 ist entschieden. Was es dort weiß und die genaue Stimme bleiben offen. Das vorgeschlagene brüchige Protokoll ist eine geeignete Teststimme, aber noch kein verbindliches Stilgesetz.

## 4. Dynamische Agentenverwaltung

„Dynamisch“ heißt: Ein Figurenprofil wird nur dann ausgeführt, wenn es auf ein konkretes Ereignis reagieren kann. Seine Identität und Erinnerung überleben die Pause. Der Agent ist keine dauerhaft lebende Modellverbindung.

Der minimale Lebenszyklus: inaktiv → bereit → ausgeführt → pausiert; außerdem blockiert bei fehlender Grundlage und beendet nach einem erzählerischen Abschluss. Aktivierung entsteht durch Szene, Ort, zugestellte Nachricht oder einen expliziten Simulationsauftrag. Ein Trigger zeigt seinen Grund. Kein LLM entscheidet frei, neue kanonische Figuren anzulegen.

Zunächst nur zwei Profile instanziieren: AEGIS und eine Gegenfigur. Weitere Profile verdienen sich ihren Platz durch konkrete Szenen. Guardians können anfangs feste Operationen sein; erst bei eigener Entscheidungssituation werden sie eigenständige Agenten. Arbeitsagenten wie Editor oder Quellenleser bleiben von Figurenprofilen getrennt.

Ein Profil braucht nur Felder, die die ersten Fälle verwenden: Identität, Rolle, erlaubte Aktionen, Wissenssicht und Promptversion. Zustand enthält Szene, subjektive Behauptungen, aktuelle Absicht und zugestellte Ereignisse. Faktenwissen und falsche Überzeugung bleiben unterscheidbar. Eine Aussage Kaels ist zunächst eine erhaltene Aussage, keine objektive Weltwahrheit.

Die Ausführung verwendet frische Kontexte aus dem gespeicherten Zustand. Figuren erhalten keinen Repository-Zugriff; bei einem CLI-Modellpfad Tools deaktivieren und ausschließlich den gefilterten Pack einspeisen. Ein Prompt „du weißt das Ende nicht“ reicht nicht, wenn das Ende trotzdem im Kontext oder über ein Suchwerkzeug erreichbar ist.

## 5. Werkzeugplan

Alle Namen in dieser Tabelle sind vorgeschlagene Funktionen bzw. CLI-Unterbefehle. Zuerst nur die Funktionen implementieren, die die zwei Pilotfälle tatsächlich brauchen.

| Werkzeug | Vertrag | Umsetzung |
|---|---|---|
| `scene_context` | Szene und Autorgrundlage mit Status und Provenienz | Liest Kanon/Storyform; kennzeichnet Arbeitsvorschläge |
| `perceive` | Nur für diese Figur sichtbare Fakten und Ereignisse | Deterministischer Filter vor dem Modellaufruf |
| `storypoint` | Exakter Lookup eines vorhandenen JSON-Pfades | Kein semantischer RAG-Aufruf für bekannte Storyform-Felder |
| `propose_action` | Typisierte Aktion, Ziel, benötigte Beobachtungen, kurzer erklärter Grund | Modell liefert Vorschlag; keine Weltmutation |
| `validate_action` | Zulässigkeit, Voraussetzungen, Kosten, explizite Fehler | Code prüft harte Regeln; literarische Angemessenheit bleibt Urteil |
| `apply_event` | Akzeptierte Aktion plus erwartete Zustandsversion | Ein Schreiber; atomare Speicherung; doppelte Aktion nur einmal |
| `agent_status` | Ausführbare Figuren und Aktivierungsgründe | Aus Zustand und Ereignissen abgeleitet |
| `replay` / `fork` | Verlauf rekonstruieren bzw. explorative Variante starten | Ereignisse und eingefrorene Modellantworten; keine neue Inferenz für Replay |
| `export_scene` | Spielverlauf als Arbeitsmaterial mit Referenzen | Kein automatisches Umschreiben oder Promoten des Manuskripts |

`ask` bleibt das Autorenwerkzeug für Forschung. Figurenretrieval braucht einen zusätzlichen Berechtigungsfilter, der auch Suchergebnisse und Toolantworten abdeckt. Jeder Kontext markiert ausgelassene Inhalte; fehlende Evidenz wird nicht durch freie Lore-Erfindung aufgefüllt.

Lean ist später als optionale formale Prüfschicht für wenige modellierte Invarianten sinnvoll. Beispielsweise lässt sich eine Ressourcenbilanz oder eine definierte Übergangsregel prüfen. Daraus folgt weder, dass ein AEGIS-Log literarisch überzeugend ist, noch dass die ganze Romanontologie bewiesen wurde. Literarisch beschädigte Logs und technische Ausführungsprotokolle separat speichern.

## 6. Prompting und Verbesserung

Den Prompt aus sechs versionierten Bestandteilen zusammensetzen: Figurenrolle; gültige Szene; begrenztes Figurenwissen; gegenwärtige Absicht; erlaubte Aktionen; Ausgabeformat mit wenigen geprüften Beispielen. Den gesamten Forschungsgraphen oder den ganzen NCP in jeden Figurenprompt zu laden wäre teuer und würde Spoiler verteilen.

Die Ausgabe trennt Aktion, gesprochene Worte und optionalen literarischen Logtext. Gesprochene Worte dürfen täuschen; die technische Aktion darf das Schema nicht verletzen. Ein kurzer Entscheidungsgrund genügt zur Prüfung; private Gedankengänge sind kein benötigtes Produktartefakt.

Selbstkritik nur bei einem benannten Fehler und mit begrenzter Wiederholung. Nach wiederholtem Scheitern bleibt die Szene unverändert und zeigt den Fehler. Promptverbesserungen aus der Meta-Prompt-Quelle als Kandidaten speichern; feste Gegenbeispiele und bislang ungesehene Fälle vergleichen. DSPy kommt erst hinzu, wenn genügend bewertete Fälle und eine geeignete Metrik existieren. Die spätere Optimierung darf weder Figurenwissen erweitern noch AEGIS’ festgelegte Entwicklung überschreiben.

Externe Grundlagen: [Anthropic: Context Engineering](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents), [Tooldesign](https://www.anthropic.com/engineering/writing-tools-for-agents), [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents). Daraus übernehme ich die Empfehlung kleiner, klar unterscheidbarer Werkzeuge und eines einfachen Ablaufs vor komplexer Autonomie. Das ist eine Designableitung, kein Nachweis narrativer Qualität.

## 7. Spielbare Romanfassung und Autorenoberfläche

Zwei Modi teilen denselben Simulationszustand. Im Autorenmodus sind Voraussetzungen, Figurenwissen, verworfene Aktionen und Kosten sichtbar. Im Spielmodus sind nur erlebte Szene, Handlungen und wahrnehmbare Konsequenzen sichtbar. Die Autorenrechte bleiben auch bei einer Figurenperspektive jederzeit erreichbar; fiktionale Amnesie darf das reale Schreiben nicht blockieren.

Für den ersten spielbaren Ausschnitt: eine eigenständige Testsituation mit einer Anomalie, zwei oder drei Handlungen und einer späteren Konsequenz. Wer einen Sweep auslöst, erhält kurzfristig Ordnung, verliert aber Zugriff auf eine Information und verbraucht Reserve. Wer die Anomalie bestehen lässt, bewahrt die Information und verändert die Bedrohungslage. Diese Regeln sind Pilotannahmen, noch kein neuer Romanplot.

Zuerst vorgefertigte oder vom Autor freigegebene Texte. Ink plus inkjs ist ein geeigneter Kandidat für lokale Entscheidungen und browserbasierte Wiedergabe; Inky bietet Schreib- und Testoberfläche. Quellen: [Ink](https://github.com/inkle/ink), [Inky](https://github.com/inkle/inky), [inkjs](https://github.com/y-lohse/inkjs). Dabei muss ein gemeinsamer Zustandseigentümer festgelegt werden: Ink steuert Textverzweigungen, der Simulationskern Weltkonsequenzen; dieselbe Ressource darf nicht in beiden unabhängig verändert werden.

NCP ist Strukturgrundlage, kein fertiges Spieleformat. Die erste Adaption hält die zentrale Argumentation fest und variiert lokale Wege, Wissenszugang und Kosten. Freie Enden wären ein eigenes Adaptionsprojekt, weil sie andere Storyforms und deutlich mehr Autorenarbeit verlangen.

Die aktuelle App ist statisch. Ein lokaler oder vorgerenderter Pilot passt dazu. Echtzeit-LLM-Aufrufe aus der veröffentlichten Seite brauchen eine neue Architekturentscheidung, einen geschützten Modellzugang und ein Kostenlimit; Schlüssel gehören nie ins Browserbundle. Bis dahin: lokale CLI-Ausführung, JSON-Export, statisches Replay und optional browserlokaler Spielstand.

Für die Oberfläche zunächst eine einzige Szenenansicht: Szene lesen; Handlung auswählen; Konsequenz sehen. Der Autorenmodus ergänzt Figurenwissen und Versionsvergleich. Ein großes Netzwerkdiagramm wird erst nötig, wenn es eine konkrete Frage besser beantwortet als die Ereignistabelle. Text bleibt lesbar; ein literarischer Glitch verändert weder Schaltflächen noch Navigation. Vorgeschlagene Routen: `#/lab/aegis` und `#/play/pilot`; sie sind noch nicht gebaut.

## 8. Lieferfolge mit überprüfbaren Abschlüssen

| Schritt | Liefergegenstand | Abschlusskriterium |
|---|---|---|
| 1. Zwei Fälle von Hand | Ein korrekter, ein unzulässiger Handlungsvorschlag; explizite Wissenssicht | Beide Fälle haben erwartete Zustände und eine bezeichnete Autorenannahme |
| 2. Offline-Kern | Kleine Standardbibliothek-CLI, Profile, Ereignisjournal, Mock-Modell | Wissenfilter, Kosten und Replay funktionieren ohne Schlüssel und Netz |
| 3. AEGIS-Modelladapter | Ein serieller Aufruf über passenden vorhandenen Modellpfad | Eingaben, Ausgaben, Promptversion, Status und tatsächlicher Verbrauch aufgezeichnet; keine zusätzlichen Korpusübertragungen ohne bestehende Freigabe |
| 4. Zweite Figur | Kontextisolation und vermittelte Nachrichten | Die Gegenfigur erfährt nur zugestellte Folgen; Pause/Neustart erhält ihre Erinnerung |
| 5. Autoren-Replay | Statische Ansicht und exportierbarer Szenenvergleich | Gleicher Verlauf führt zum gleichen Weltzustand; keine Behauptung neuer Agentenfunktionen ohne Beispiel |
| 6. Spielbarer Ausschnitt | Kurzer Ink/inkjs-Pilot mit dauerhafter Konsequenz | Unterschiedliche Entscheidungen verändern späteren Informationszugang oder Ressourcen; Speichern/Laden erhält das Ergebnis |

Sinnvolle Offline-Prüfungen: unerlaubtes Wissen fehlt im Pack; fehlende Voraussetzung verwirft eine Aktion ohne Mutation; abgelaufene Zustandsversion wird abgelehnt; doppelte Aktions-ID erzeugt keine doppelte Löschung; Reserve kann nicht negativ werden; Szenenvariante verändert den Ausgangskanon nicht; Replay benötigt keine Modellaufrufe; Monolith-AEGIS ist nach seinem definierten Ende nicht weiter ausführbar.

Modellqualität separat messen: Spoiler und unbegründetes Wissen, gültige Aktionen, Stimmenurteil des Autors, lokale Konsequenzen, Wiederholungen, tatsächliche Kosten und Wartezeit. Ein mechanisch gültiger Sweep kann dramaturgisch langweilig sein. Fehlender Modellzugang ist nicht als schlechter Text zu bewerten.

## 9. Konkreter erster Auftrag für Claude Code

> Lies AGENTS.md, NOW.md, CLAUDE.md, PRINCIPLES.md und SPEC.md. Initialisiere die Reader-Werkzeuge und prüfe das Session-Board; claim eine eigene AEGIS-Pilot-Session, bevor du Änderungen beginnst. Baue ausschließlich einen lokalen Offline-Piloten mit AEGIS und einer Gegenfigur. Definiere zuerst zwei konkrete Fälle mit expliziten Pilotannahmen. Leite Rollen aus Manuscript/kanon.md und Plan/storyform/b.json ab; Arbeitskarten und ältere Quellen werden nicht zu Kanon. Implementiere einen Figurenwissenfilter, typisierte Handlungsvorschläge, deterministische Validierung, atomare Ereignisfortschreibung mit Zustandsversion und idempotenten Aktionen sowie Replay mit eingefrorenen Antworten. Modelle zunächst vollständig mocken. Füge keine neue Datenbank, kein MCP und keine laufenden Modellprozesse hinzu. Zeige erlaubte und abgelehnte Handlung sowie Pause/Neustart in einer Offline-Fixture. Dokumentiere neue Befehle erst, wenn sie ausführbar sind. Keine Manuskriptänderung und keine automatische Kanonpromotion. Ein Live-Modelladapter und ein spielbarer Ausschnitt folgen erst als getrennte Erweiterungen.

Für später zu entscheiden: Wer wird gespielt — Kael, ein Beobachter oder AEGIS? Bleibt der große Ausgang fest? Welche Wissensgrenzen gelten für AEGIS’ Ich? Der technische Pilot benötigt diese endgültigen Romanentscheidungen noch nicht; er verwendet klar gekennzeichnete Testannahmen.

## Prüfgrenze dieser Untersuchung

Repositorydateien und ausgewählte Quellen wurden gelesen; das Session-Board konnte den GitHub-Zustand abrufen. Der Reader-Initializer wurde gestartet. Eine vollständige Runtime-Installation, Live-Modellausführung oder Prüfung der veröffentlichten UI wurde für diesen Architekturplan nicht als erfolgreich verifiziert. Keine neue Source-Reconciliation, kein Manuskriptpatch, kein Repository-Commit und keine Veröffentlichung wurden vorgenommen.
