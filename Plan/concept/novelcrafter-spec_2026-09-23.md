# Funktions-Spezifikation: KI-gestützter Novel-Writing-Assistent nach dem Vorbild von Novelcrafter

Nachbauen lässt sich Novelcrafter am besten als drei gekoppelte Subsysteme: ein **Codex** (Wiki mit Alias-Erkennung, szenengebundenen Progressions und der Einstellung „AI Context“), eine **Prompt-Template-Engine** (Ausdrücke in `{…}`, Funktionen mit Namespaces, `#if`-Blöcke, Inputs, Components, Presets) und ein **Plan** mit der Hierarchie Act > Chapter > Scene (Ansichten Grid, Matrix, Outline). Ein Kontext-Builder verbindet die drei: Er löst für jede KI-Aktion die aktuelle Position im Manuskript auf und baut daraus einen XML-strukturierten Prompt.

## TL;DR

- **Kern des Codex:** Einträge haben einen festen Typ (Character, Location, Object, Lore, Subplot, Other), Aliase und Custom Details. Die Option „AI Context“ hat vier Stufen: *Always include*, *Include when detected* (Default), *Don't include when detected*, *Never include*. Progressions sind an Szenen gebunden und für die KI erst ab dieser Szene sichtbar. Relations sind gerichtet und ziehen verknüpfte Einträge rekursiv nach.
- **Kern der Prompts:** Es gibt vier Prompt-Typen (Scene Beat Completion, Scene Summarization, Text Replacement, Workshop Chat) plus Prompt Components. Jeder Prompt besteht aus einer System-Message und beliebig vielen User-/AI-Messages. Die Template-Sprache hat über 150 dokumentierte Funktionen, darunter `storySoFar`, `codex.get` und `input`. Sie ist case-insensitiv, nutzt Typ-Koerzion und kennt nur die Operatoren `+`, `is` und `in`.
- **Empfehlung:** Die Mechanik der Engine ist offiziell gut dokumentiert und kann nachgebaut werden. Als Referenz für die Kontext-Injektion taugt SillyTavern World Info am besten. Wer mit TypeScript/Web forken will, sollte sich The Story Nexus bzw. dessen Forks ansehen. In Python gibt es keinen gleichwertigen KI-Fork, novelWriter dient dort nur als Studienobjekt für Datenformat und Struktur.

---

## 0. Konventionen

- **[OFFIZIELL]** = Novelcrafter-Doku, Referenz, Changelog oder Kurse. **[COMMUNITY]** = Drittquellen. **[ABGELEITET]** = eigene Ableitung bzw. Designvorschlag.
- Quellen stehen als Pfad unter `novelcrafter.com/…`. Englische UI-Labels bleiben im Original.
- Stand: September 2026. Die Prompt-Doku bezeichnet sich selbst als „Work in Progress“.

---

## 1. Gesamtarchitektur

| Bereich | Zweck | Zentrale Entitäten |
|---|---|---|
| Plan | Struktur des Romans | Novel, Act, Chapter, Scene, Label, POV |
| Write | Manuskript-Editor und KI-Prosa | Scene-Inhalt, Scene Beat, Section, Text Replacement |
| Codex | Story Bible, Kontextquelle | CodexEntry, Alias, Detail, Relation, Progression, Category, Tag |
| Chat (Workshop) | Brainstorming mit Kontext | ChatThread, Message, Context-Auswahl |
| Snippets | Freie Notizen | Snippet |
| Prompt Library | Prompts, Presets, Personas, Components, Model Collections | Prompt, Preset, Persona, Component, Input, ModelConfig |
| Organization/IO | Archiv, Revisionen, Import/Export, Cover, Extract | Revision, ArchiveItem |

**Datenhaltung [OFFIZIELL]:** Novelcrafter läuft zurzeit nur mit aktiver Internetverbindung. Laut Hersteller ist ein Offline-Modus vorgesehen, einen Termin gibt es nicht (`/help/faq/general/can-i-use-nc-in-ofline-mode`). Der Changelog erwähnt Sync-Fehler und read-only-Novels, was auf einen serverseitig synchronisierten Zustand schließen lässt. **[ABGELEITET]** Für die Portierung ist local-first sinnvoll (SQLite oder IndexedDB mit optionalem Sync) – ein echter Vorteil gegenüber dem Original.

---

## 2. CODEX (höchste Priorität)

### 2.1 Eintragstypen [OFFIZIELL]
Quelle: `/help/docs/codex/codex-types`

| Typ | Semantik | Besonderheit |
|---|---|---|
| Character | Personen, auch Tiere oder Roboter | Nur Characters können als POV gesetzt werden |
| Location | Orte vom Raum bis zur Galaxie | – |
| Object | Gegenstände („Object/Item“ in der Funktionsreferenz) | – |
| Lore | Weltwissen, Magiesysteme, Geschichte | – |
| Subplot | Nebenhandlungen | Verlauf über Progressions, Anzeige in der Matrix |
| Other | Sammelbecken (Fraktionen, Genre-Infos …) | – |

Die Typen sind vom System vorgegeben und nicht erweiterbar, weil Features an ihnen hängen. Frei organisiert wird über **Custom Categories**; ein Eintrag darf in **mehreren Custom Categories** zugleich stehen (`/changelog/new-codex-tracking-options`).

### 2.2 Anatomie eines Eintrags [OFFIZIELL]
Quelle: `/help/docs/codex/anatomy-codex-entry`

- **Name** und **Aliases** (Vorname, Spitzname, Titel).
- **Description**: Freitext, den die KI sieht.
- **Notes**: für den Autor; im Prompt trotzdem über `codex.notes` abrufbar.
- **Tags**: nur für Suche und Filter; die KI sieht sie nicht, relevantes Wissen muss zusätzlich in ein Feld oder Detail.
- **Thumbnail**: genau ein Bild pro Eintrag (Upload, Zuschnitt, Positionierung), darunter eine Mention-Heatmap.
- **Tabs**: Details, Tracking, Relations, Mentions, dazu Progressions. Außerdem Farbe und Anzeige von Dropdown-Details in der Sidebar (2.5).

### 2.3 Aliases und Erwähnungs-Erkennung [OFFIZIELL]
Quellen: `/help/docs/codex/aliases`, `/help/docs/codex/codex-tracking`, Changelog

1. Gesucht werden Name und alle Aliase, standardmäßig **ohne Beachtung der Groß-/Kleinschreibung**.
2. **Auto-Pluralisation** nur für englischsprachige Novels: „Goblin“ findet „Goblins“; unregelmäßige Plurale („Wolves“) als Alias anlegen.
3. **Case-sensitive matching** (Toggle) gegen Fehltreffer bei Namen wie „Will“, „May“ oder „Don“.
4. **Exclusions**: kommagetrennte Phrasen, die nie zählen („May I“, „don't“); gleiche Case-Regel wie der Name.
5. Treffer werden in Manuskript, Plan und Snippets **unterstrichen**; Klick öffnet eine Preview-Card, zweiter Klick schließt sie.
6. Wortgrenzen nennt die Doku nicht. **[ABGELEITET]** Whole-Word-Matching mit Unicode-Wortgrenzen; im Deutschen zusätzlich eine Flexions- oder Alias-Strategie („Annas“).

**Mentions-Tab** (`/help/docs/codex/codex-mentions`): alle Erwähnungen, aufgeschlüsselt nach Manuscript, Scene Summaries, Codex Entries, Snippets und Chat Threads.

### 2.4 Codex Tracking und „AI Context“ [OFFIZIELL]
Quelle: `/help/docs/codex/codex-tracking` (Stand 19.03.2026)

| Einstellung | Wirkung |
|---|---|
| **Track this entry by name/alias** (Default an) | Unterstreichung, Zählung im Mentions-Tracker des Codex-Headers, Appearance Heatmap |
| **Case-sensitive matching** / **Exclusions** | siehe 2.3 |
| **AI Context → Always include** | in jedem Prompt; früher „global entry“, `codex.global` |
| **AI Context → Include when detected** (Default) | Aufnahme, wenn Name oder Alias im **ausgewählten Text, in Scene Beats oder in der Chat-Nachricht** vorkommt |
| **AI Context → Don't include when detected** | bei Erkennung nicht aufgenommen, aber manuell als Szenen-Kontext oder über eine Relation möglich |
| **AI Context → Never include** | nie an die KI (Spoiler, private Notizen) |

Edge Case: Tracking aus schaltet auch die Erkennung für *Include when detected* ab. Soll die KI den Eintrag ohne Unterstreichung sehen, ist *Always include* richtig.

### 2.5 Custom Details [OFFIZIELL]
Quellen: `/help/docs/codex/codex-details`, `/help/docs/codex/character-codex-details`

- Aufruf: Zahnrad in der Sidebar → „custom details“ oder am Eintrag „add details“ → „manage custom details“.
- **Feldtypen**: `text` (mehrere Absätze), `line` (einzeilig), `dropdown` (Optionen mit Farbe und Reihenfolge, Wert optional in der Sidebar), `Codex reference` (Verweis; zieht den Eintrag **nicht** in den Prompt – dafür sind Relations da).
- **Scope**: Buch oder Serie. **Gültig für**: Auswahl von Codex-Typen.
- **AI-Sichtbarkeit pro Detail**: always seen / never included / only included when using NSFW prompts.
- **Quick Create** für Details: Vorlagen wie „Backstory“ oder „Story Role“; die vollständige Liste wurde nicht gefunden.
- Laut Doku lohnt ein Detail vor allem, wenn Inhalt vor moderierten Modellen verborgen oder eine sehr wichtige Information herausgelöst werden soll; Einsteigern wird die Description mit Überschriften empfohlen.
- Im Prompt: `codex.detail(entries…, details)`, gerendert als XML, z. B. `<character name="Alice"><appearance>…</appearance></character>`.

**Quick Create für Einträge** (Kurs „Setting up the Codex“): „Story Genre“ und Style-Guides entstehen mit ausgeschaltetem Tracking und *Always include*.

### 2.6 Relations [OFFIZIELL]
Quelle: `/help/docs/codex/codex-relations`, Codex-Cookbook

- Früher „nested references“. `+ Add Entry` mit Suche, „-“ entfernt, der **Doppelpfeil** tauscht die Richtung (Parent).
- **Semantik**: Ist der Parent im Kontext, kommt das Child mit. Keine Familienbeziehungen; die Art der Beziehung erfährt die KI nicht.
- **Gerichtet und rekursiv** [Cookbook]: Bei A→C und C→E zieht A sowohl C als auch E nach. Die App warnt vor Kaskaden.
- Im Prompt: `withRelations(…)` (rekursiv), `codex.relations(…)`, `codex.isRelatedTo(…)`.

### 2.7 Progressions / Additions [OFFIZIELL]
Quellen: `/help/docs/codex/progressions-additions`, `/help/docs/codex/progressions-codex-details`, FAQ `track-character-changes`, `chat-multiple-scenes`

- **Zweck**: Veränderungen im Zeitverlauf (Narbe, Besessenheit, Beziehung), ohne dass die KI sie zu früh erfährt.
- **Anlegen** im Write-Interface an einer Szene: Text, Codex-Eintrag (jeder Typ), im Actions-Menü **ergänzen** (Addition, Default) oder **ersetzen** (Replacement).
- **Sichtbarkeit**: nur beim Arbeiten an dieser oder einer späteren Szene; in früheren Szenen fehlt sie im Prompt.
- **Mehrere Szenen im Kontext**: Auflösung bis zur chronologisch **letzten** Szene im Plan (Szene 2 und 5 gewählt → Stand von Szene 5).
- **Progressions auf Details**: pro Detail analog zur Description.
- **Anzeige**: Indikatoren am Eintrag, an welcher Szene eine Progression hängt; in der Matrix erscheinen Subplot-Additions je Szene.
- **Keine Plot-Punkte**: Handlung gehört in Summaries und Beats. Tricks: Eintrag „edits“ als Überarbeitungs-To-do; für Subplot-Chats die letzte Szene als Kontext wählen.

### 2.8 Series Codex [OFFIZIELL, teils nur Snippet]
Series-Einträge gelten in allen Büchern einer Serie. Actions-Menü: „move to series“ / „move to book“. Tabs **all / series / book**; im Series-Tab angelegte Einträge gehören direkt zur Serie (Banner). Für Vorgängerbände empfiehlt das Cookbook einen eigenen Eintrag mit *Always include* (`/help/docs/codex/series-codex`).

### 2.9 Description Guidelines [OFFIZIELL]
Klein anfangen und nur bei inkonsistenter Prosa ergänzen; Aussehen eher in die Notes, weil die KI lebhafte Details wiederholt; Form (Absatz oder Stichpunkte) ist laut Doku kaum relevant; Veränderungen in Progressions statt Überschreiben; kleine Codizes sparen Tokens (`/help/docs/codex/guidelines-for-descriptions`).

### 2.10 Extraktion und Befüllung [OFFIZIELL]
- **Extract** (`/help/docs/organization/the-extract-feature`) ist ein **Werkzeug ohne KI**: Es zerlegt ein Snippet oder eine Chat-Nachricht anhand von Überschriften und Textblöcken in **Codex Entries, Scene Summaries oder Scene Beats**. Kandidaten erscheinen als Karten zum An- und Abwählen; Standardtyp „character“, änderbar einzeln oder per „Change Type for All“.
- **Detect characters** als Szenen-Aktion (5.6); zusätzlich eine FAQ zum KI-gestützten Befüllen.

### 2.11 Codex als Wort-Tracker und AI-isms [OFFIZIELL]
Quellen: `/help/faq/ai-and-prompting/ai-isms`, Cookbook `tracking-words-with-the-codex`

Dokumentiertes Muster: ein Eintrag „AI-isms“ mit typischen KI-Phrasen als Aliasen. Sie werden im Text unterstrichen und lassen sich per `{codex.get("AI-isms")}` als „vermeide diese Phrasen“ in Prompts einsetzen. Da keine KI nötig ist, steht es in allen Tiers zur Verfügung. Die Features-Seite bewirbt zusätzlich „Smart Highlighting“ für Füllwörter, KI-Muster und Dialog-Tags. **[ABGELEITET]** Ein eigenes AI-isms-Feature gibt es nicht, es ist ein Muster aus Codex, Aliasen und Prompt.

### 2.12 Wie der Codex im Prompt landet [OFFIZIELL + ABGELEITET]
- Die **Codex-Kontextmenge** (`codex.context`) umfasst Always-include-Einträge, erkannte Einträge (Beat, Auswahl, Chat-Nachricht), manuell zugefügte Einträge und Szenen-Referenzen (POV und Referenzen), jeweils plus Relations. Abgezogen werden *Never include* und bei *Don't include when detected* die nur erkannten Einträge.
- Ausgabe als XML pro Eintrag, z. B. `<character name="Doris" occupation="Waitress">…</character>`; welche Details als Attribute oder Kinder erscheinen, ist nicht vollständig dokumentiert.
- Progressions werden relativ zur aktuellen Szene aufgelöst (2.7); `codex.get(…)` entfernt „hidden entries“ (vermutlich *Never include*).

---

## 3. PROMPT-SYSTEM (höchste Priorität)

### 3.1 Prompt-Typen [OFFIZIELL]
Quellen: `/help/docs/prompts/prompt-types`, `/help/docs/prompts/prompt-library`

| Typ | Aufruf in der UI | Typischer Kontext |
|---|---|---|
| **Scene Beat Completion** | Scene-Beat-Block im Editor | Beat-Text (`message`), Text davor/danach, storySoFar, Codex, POV/Tense |
| **Scene Summarization** | Summarise-Aktion einer Szene | Volltext der Szene; laut `/help/docs/prompts/prompt-types` fasst der System-Prompt Szenen auf etwa 80 Wörter zusammen |
| **Text Replacement** („Laser Tools“) | Textauswahl, **mindestens 4 Wörter** | Auswahl (`message`), Umgebungstext; System-Prompts Expand, Rephrase, Shorten |
| **Workshop Chat** | Chat-Interface | Nachricht, gewählter Kontext (Szenen, Kapitel, Acts, Snippets, Codex), Persona |
| **Prompt Components** | per `include()` | wiederverwendbare Bausteine mit Logik |

Seit Mai 2025 lassen sich an Beats, Replacements, Chats und Summaries beliebige Kontextoptionen hängen – mehrere Szenen, Kapitel, Acts, Snippets oder ein Outline für einen POV (`/blog/may-2025-new-prompting-system-update`).

### 3.2 Prompt Library [OFFIZIELL]
- **Links**: Suche und Filter, „Neu“, Bereiche für Model Collections, Defaults (Novel, Serie, Account), Personas, Prompts (nach Typ: System, eigene, übernommene) und Components. **Rechts**: Detail-Editor bzw. Startseite mit zuletzt genutzten Prompts.
- **Clone**: System-Prompts sind schreibgeschützt und werden vor dem Anpassen geklont.
- **Sharing / „Add from Clipboard“**: Prompts, Presets, Personas, Model Banks und einzelne Input-Konfigurationen als kodierter String.
- **Submenüs** für Auswahlmenüs (`/help/docs/prompts/organize-your-prompts-into-submenus`; Syntax nicht verifiziert).
- **Default Prompts**: pro Novel, Serie oder Account und Prompt-Typ.

### 3.3 Prompt-Detail-Tabs [OFFIZIELL]
Quelle: `/help/docs/prompts/prompt-detail-tabs`

1. **General** – *Presets* (Name, Default-Model aus der Model Bank, feste Input-Werte; „Recently Used“ lässt sich als Preset speichern). *Models* (Clone/Copy/Delete, `+ Add Model`, `Add from Clipboard`; pro Modell Name, Modell je nach verbundenen Anbietern, Parameter – leer = Anbieter-Default –, Advanced Settings, `+ Attach a Collection`). *General Settings* (Prompt-Typ, Moderationsverhalten, Thinking avoid/prefer).
2. **Instructions** – eine **System Message** plus beliebig viele **User-/AI-Messages** (Rolle umschaltbar, kopieren, löschen, `Add Message`). **Aufeinanderfolgende Messages gleicher Rolle werden zusammengeführt**, ebenso bei einer leeren Message dazwischen. **Versionshistorie** für den ganzen Prompt.
3. **Advanced** – Inputs anlegen, „Add missing“ (legt im Template referenzierte Inputs an), Input aus Zwischenablage, **Included Components**, **Prompt Preview** mit Live-Auswertung.
4. **Description** – für Menschen, **nie** für die KI.
5. **Usages** – nur bei Components: welche Prompts sie einbinden.

### 3.4 Prompt Inputs [OFFIZIELL]
Quellen: `/help/docs/prompt-inputs/*`

- **Zweck**: Variablen, die Nutzer vor dem Senden setzen (Wortzahl, Rephrase-Art, Zusatzkontext).
- **Felder**: Name, Description (nicht für die KI), „Must be filled out“, **Allowed content** (*Custom Content* mit Text und/oder Dropdown sowie Kontexttypen wie Szenen, Snippets, Codex, Full Novel/Outline).
- **Dropdown**: Labels per `Add Label`, Unterkategorien per Präfix („sci-fi: space opera“); pro Option über die Sprechblase Hilfetext und **eigener Inhalt**, der das Label im Prompt ersetzt.
- **Defaults** nur für Text, Dropdown und Full Novel/Outline. Ein rotes Dreieck markiert definierte, aber ungenutzte Inputs.
- **Referenz**: `{input("genre")}`; Name normalisiert (klein, ohne Leerzeichen, `/` → `.`); fehlt der Input, kommt eine leere Liste. Gemischte Inhalte lassen sich mit `isAct`, `isChapter`, `isScene` filtern.
- Seit Mai 2025 sind Inputs vor dem Generieren direkt im Write- oder Chat-View editierbar.

### 3.5 Prompt Components [OFFIZIELL]
Wiederverwendbare Template-Bausteine (System oder eigene, z. B. `Novelcrafter/Chat/DefaultContext`), eingebunden mit `{include("Prose Guides")}`. Normalisierung: „Prose Guides“ = „proseguides“, „A/B“ = „a.b“. Sie werden im Kontext des aufrufenden Prompts ausgewertet und können Logik enthalten.

### 3.6 Presets und Personas [OFFIZIELL]
- **Preset** („custom prompts lite“): gespeicherte Kombination aus Prompt, Modell und Input-Werten, direkt im Auswahlmenü – z. B. „Full Scene“ für den Scene-Beat-Prompt (`/help/docs/prompt-presets/prompt-preset-uses`).
- **Persona**: Rolle für den Chat, unabhängig vom Prompt wählbar; `personas` liefert die verfügbaren je Prompt-Typ und Projekt.
- **Unterschied**: Die Persona ändert das „Wer antwortet“, das Preset das „Wie läuft dieser Prompt“. In Persona-Texten wird **keine Template-Syntax** ausgewertet.

### 3.7 Modelle, Parameter, Thinking [OFFIZIELL]
Quellen: `/help/docs/prompts/tuning-model-settings`, `/help/docs/models/thinking-settings`, `/help/docs/models/model-collections`

- **Parameter**: Temperature, Top P, Max Tokens (bricht hart ab; für Längen ein Input verwenden), Frequency, Presence und Repetition Penalty (je nach Modell), Thinking/Reasoning Effort. Tuning-Reihenfolge: Temperature, dann Top P, Penalties nur bei Schleifen.
- **Thinking (Beta)**: General Settings → Experimental Features → „Customize AI Thinking“; dann „prefer/avoid thinking“ pro Interaktion, Preset und Prompt. Reasoning Effort standardmäßig „medium“, pro Modell in der Model Collection. Gedanken werden weder angezeigt noch an die nächste Chat-Nachricht weitergegeben.
- **Model Collections**: benannte Modell-Bündel für Prompts; neue Modelle für System-Prompts kommen über eine Collection hinein.
- **NSFW**: Details „nur NSFW-Prompts“ und `prompt.nsfw`. `prompt.model` erlaubt modellspezifische Anweisungen, z. B. `{#if "qwen" in lowercase(prompt.model)}…{#endif}`.

### 3.8 AI Connections [OFFIZIELL]
Dokumentierte Anbieter: **Anyscale Endpoints, Claude (Anthropic), Groq, LM Studio, Ollama, OpenAI, OpenAI API Compatible, OpenRouter** (`/help/docs/ai-connections/*`). Bring-Your-Own-Key: KI-Kosten zahlt man direkt beim Anbieter. Ein Hilfeartikel „It says i'm out of AI credits“ existiert; ob Novelcrafter eigene Credits anbietet, blieb unklar. **[ABGELEITET]** Felder pro Connection: Provider-Typ, API-Key, Base-URL (LM Studio, Ollama, OpenAI-kompatibel), abgerufene Modellliste.

### 3.9 Prompt Preview und Token [OFFENER PUNKT]
Die Preview zeigt die aufgelösten Instructions (`/help/docs/prompts/prompt-preview`). Token-Zählung und Kontext-Budget sind nicht belastbar dokumentiert; die FAQ „Why are my messages costing so much?“ deutet darauf hin, dass Nutzer die Größe selbst steuern.

---

## 4. TEMPLATE-SPRACHE — REFERENZ

### 4.1 Syntax [OFFIZIELL]
Quelle: `/help/reference/prompts/terminology`

| Element | Syntax | Regeln |
|---|---|---|
| Ausdruck | `{expr}` | inline oder eigene Zeile; fehlende `}` = Fehler |
| Funktion | `{pov}`, `{novel.title}` | Namespace per Punkt, **keine** Property-Zugriffe; C-Stil, case-insensitiv, **nicht verkettbar** |
| Parameter | `{codex.detail(pov, "Appearance")}` | Auswertung von innen nach außen, Kommas trennen |
| Koerzion | `codex.detail("Alice", …)` | automatische Umwandlung (Text → Eintrag per Name/Alias, POV → Character) |
| String | `"…"` oder `'…'` | gegenseitig als Escape; **keine typografischen Anführungszeichen** |
| Operator `+` | `"Chapter " + chapter.number + " Notes"` | Verkettung |
| Operator `is` | `pov.character is "Alice"` | Gleichheit |
| Operator `in` | `"Time: Morning" in scene.labels` | Enthaltensein |
| Kommentar | `{! … !}` | wird nicht gesendet |
| Bedingung | `{#if cond} … {#endif}` | offiziell belegt |
| Else-Zweige | `{#elseif cond}`, `{#else}` | [COMMUNITY] nur in Community-Kopien der System-Prompts, nicht offiziell verifiziert |
| XML | freie Tags wie `<storySoFar>…</storySoFar>` | ausdrücklich empfohlen; eigene XML-Elemente erlaubt |
| Editor-Blöcke | HTML-Elemente mit Präfix `nc-` | `/help/reference/prompts/editor-blocks`; Details nicht verifiziert |
| JSON | – | nicht unterstützt; doppelte geschweifte Klammern bleiben literal |

**Rückgabetypen**: List[…], Text Container (Titel, Inhalt, Attribute, Referenz), Outline (*Summaries* oder *Content*), Boolean, Number. **Render-Formate**: XML (rekursiv), Markdown, Plain Text, Inherited. Listen haben einen **Matching-Modus** „all“/„any“ (relevant für `contains`).

**Legacy [OFFIZIELL]**: Vor Mai 2025 lautete die Syntax `{context.storySoFar}`, `args.includeAllText` usw.; ein Migrations-Widget übersetzt sie, `context.codex.getAdditions` hat keinen Ersatz.

### 4.2 Funktionen (vollständige Liste laut Referenz, Stand 2026)
Quelle: `/help/reference/prompts/prompt-functions`. `f(...elements)` = variadisch; ohne Argument gilt der aktuelle Scope.

| Gruppe | Funktionen | Anmerkungen |
|---|---|---|
| **Acts** | `act`, `act.fullText`, `act.name`, `act.next`, `act.number`, `act.previous`, `act.summary`, `act.title`, `isAct` | akzeptieren Chapter, Scene, Codex Entry/Category/Detail, Label, Novel, Outline, POV, Series, Text; Romanreihenfolge |
| **Chapters** | `chapter`, `chapter.fullText`, `chapter.name`, `chapter.next`, `chapter.number`, `chapter.previous`, `chapter.summary`, `chapter.title`, `isChapter` | `chapter.summary` → `<chapter title number><scene number>…</scene></chapter>`; `number` fehlt bei ausgeschalteter Nummerierung |
| **Codex** | `codex.aliases`, `codex.all`, `codex.category`, `codex.characters`, `codex.context`, `codex.description`, `codex.detail(...entries, details)`, `codex.get`, `codex.global`, `codex.has`, `codex.hasDetail(...entries, details)`, `codex.hasTag(...entries, tags)`, `codex.inCategory(...entries, categories)`, `codex.isCharacter`, `codex.isLocation`, `codex.isLore`, `codex.isObject`, `codex.isOfType(...entries, types)`, `codex.isOther`, `codex.isRelatedTo(...entries, related)`, `codex.isSubplot`, `codex.locations`, `codex.lore`, `codex.mentions(text…)`, `codex.name`, `codex.notes`, `codex.objects`, `codex.other`, `codex.relations`, `codex.subplots`, `withRelations` | `get`/`all`/`mentions` liefern eindeutige Einträge ohne versteckte; `codex.name` → „Peter Miller (Pete)“; `description`/`notes` in Markdown |
| **Composition** | `include(name)`, `input(name)`, `local(name, value?)` | `local` = Prompt-lokaler Speicher (case-**sensitiv**), merkt sich Werte zwischen Aufrufen derselben Sitzung |
| **Context** | `hasMessage`, `hasTextAfter`, `hasTextBefore`, `isEndOfText`, `isStartOfText`, `message`, `storySoFar(outlines…, povs…)`, `storyToCome(…)`, `textAfter`, `textBefore`, `textSoFar(…)`, `textToCome(…)` | `storySoFar` = Summaries bis zur vorherigen Szene; mehrere Argumente = **Schnittmenge** (`storySoFar(act, pov)`); `textSoFar` = Volltext als XML mit `title`, `subtitle`, `number`, `pointOfView` |
| **Lists** | `all`, `any`, `count`, `join`, `takeFirst(..., n)`, `takeLast(..., n)`, `without(..., x)` | z. B. letzte 3 Summaries per `takeLast` |
| **Logic** | `and`, `contains(...haystack, needle)`, `either`, `endsWith`, `ifs(c1,v1,c2,v2,fallback)`, `isEmpty`, `isEqual`, `isGreaterOrEqual(expected, actual)`, `isGreaterThan`, `isLessOrEqual`, `isLessThan`, `isNotEqual`, `not`, `or`, `startsWith` | String-Vergleiche case-insensitiv; `either` = erstes nicht-leeres Argument |
| **Math** | `ceil`, `divide`, `floor`, `isNumber`, `max`, `min`, `multiply`, `round` | – |
| **Novels** | `novel`, `novel.author`, `novel.fullText`, `novel.hasSeries`, `novel.language`, `novel.outline`, `novel.tense`, `novel.title` | `novel.language` steuert u. a. die Rechtschreibvariante |
| **Other** | `date.today`, `personas` | – |
| **Point of View** | `pov`, `pov.character`, `pov.isFirstPerson`, `pov.isLimited`, `pov.isOmniscient`, `pov.isOverwrite`, `pov.isSecondPerson`, `pov.isThirdPerson`, `pov.type` | `{pov}` → `<pointOfView>Write in third person omniscient.</pointOfView>`; Fallback dritte Person |
| **Prompts** | `prompt.model`, `prompt.nsfw` | – |
| **Scenes** | `isScene`, `nextBeat`, `previousBeat`, `scene`, `scene.fullText`, `scene.fullTitle`, `scene.hasLabel`, `scene.hasMention`, `scene.hasReference`, `scene.hasSubtitle`, `scene.hasSummary`, `scene.hasText`, `scene.labels`, `scene.next`, `scene.nextSamePOV`, `scene.number`, `scene.previous`, `scene.previousSamePOV`, `scene.references`, `scene.subtitle`, `scene.summary`, `scene.title` | `previousSamePOV` nützlich für Multi-POV |
| **Series** | `series`, `series.description`, `series.title` | – |
| **Snippets** | `snippets.get(name)`, `snippets.has(name)` | z. B. Stilprobe |
| **Text** | `asList`, `asMarkdown`, `asNumberedList`, `asPlainText`, `asXml`, `content`, `firstWords`, `lastWords`, `lowercase`, `pluralize`, `removePunctuation`, `removeWhitespace`, `title`, `uppercase`, `wordCount`, `wordsAfter`, `wordsBefore` | Formatumwandlung |

### 4.3 Beispiele [OFFIZIELL]
```
{#if codex.has("Chapter " + chapter.number + " Details")}
Reference the following for extra details:
{codex.get("Chapter " + chapter.number + " Details")}
{#endif}

{storySoFar(act, pov)}
{asList(codex.aliases(codex.category("Nicknamed Characters")))}
{! Stilhinweis !}While writing, avoid the following AI-isms: {codex.get("AI-isms")}
```

### 4.4 Verfügbarkeit nach Prompt-Typ [ABGELEITET]
Die Referenz nennt keine Zuordnung. Aus der Semantik: Positionsfunktionen (`textBefore`, `textAfter`, `hasTextBefore`, `isStartOfText`, `nextBeat`, `previousBeat`) sind bei Beat- und Replacement-Prompts sinnvoll; `message` ist Beat-Text, Auswahl oder Chat-Nachricht; die Summarization hat die Szene als Scope; im Chat hängt der Scope an der Kontext-Szene. **Empfehlung**: Nicht verfügbare Funktionen liefern leer statt Fehler, wie das Original bei fehlenden Einträgen.

---

## 5. PLANUNGS-INTERFACE (höchste Priorität)

### 5.1 Hierarchie und Grundfunktionen [OFFIZIELL]
Quellen: `/help/docs/plan/the-plan-interface`, `/blog/planning-your-outline`

- Novel → **Acts** → **Chapters** → **Scenes**, alles per Drag & Drop sortierbar; Einfügen zwischen bestehenden Elementen möglich (FAQ). Act-Header bleiben beim Scrollen oben, damit „+ New Chapter“ erreichbar ist.
- **Toolbar**: View/Appearance, Add Act, Create Outline, Import, Actions Menu, **Keyword Search** (Summaries, Inhalte, Labels, Codex-Namen und Aliase).

### 5.2 Views [OFFIZIELL]
Quelle: `/help/docs/plan/plan-views`

| View | Verhalten |
|---|---|
| **Grid** (Default) | Szenen-Karten nach Kapiteln und Acts; Achse horizontal oder vertikal |
| **Matrix** | Szenen auf einer Achse, über das **„Show“-Menü** gewählte Dimensionen auf der anderen; Layout tauschbar |
| **Outline** | schlichte Liste mit Fokus auf Summaries |

### 5.3 Matrix im Detail [OFFIZIELL]
Quelle: `/help/docs/plan/planning-with-the-matrix`

- **Show → Codex-Einträge** (Default, nach Typ): Zellen zeigen Vorkommen als Erwähnung oder Referenz.
- **Show → POV**: POV einer Szene mit **einem Klick** umschalten, statt „Edit scene POV“ im Szenenmenü.
- **Show → Label**: Labels (z. B. Überarbeitungsstatus) pro Szene setzen. **Show → Custom Categories**: Spalten nach eigenen Kategorien.
- **Subplots**: Additions eines Subplot-Eintrags je Szene – die Matrix wird zur Timeline der Nebenhandlungen und dient der Konsistenzprüfung („Dämon taucht in Kapitel 6 im Feenreich auf“).
- **Zell-Semantik** [ABGELEITET]: zwei Quellen – automatische Erwähnungen aus dem Text und manuelle Referenzen an der Szene. „auto-detect references in the scene“ im View-Menü steuert, ob Erwähnungen als Referenz gelten; `scene.hasMention` vs. `scene.hasReference` bestätigt die Trennung.

### 5.4 Szenen-Karten [OFFIZIELL]
Quelle: `/help/docs/plan/changing-plan-appearance`

- **Inhalt**: Titel/Nummer, Subtitle, **Summary**, POV, Labels, Codex-Referenzen, Wortzahl.
- **View-Menü** (Grid/Matrix): Achse, **Kartenhöhe und -breite**, **Referenzen automatisch erkennen**.
- **Labels** (`/help/docs/organization/labeling-scenes`): farbige Labels für Menschen („Draft“, „Time: Morning“), im Prompt über `scene.labels`/`scene.hasLabel`.
- **Archivieren und Löschen**: Szenen archivieren und wiederherstellen, Acts/Chapters/Scenes auch in Masse löschen (`/help/docs/organization/*`).

### 5.5 Create from Outline [OFFIZIELL + ABGELEITET]
Quelle: `/help/docs/plan/create-from-outline`

- Am **Seitenende** von Grid und Outline; das Ergebnis wird **ans Ende** der Novel angehängt.
- **Vorlagen**: 3 Act Structure, Save the Cat, Hero's Journey, Freytag's Pyramid, Dan Harmon's Story Circle, Fichtean Curve, Derek Murphy's 24 Chapters, Story Clock; andere Strukturen im gleichen Format.
- Vorschau wie der Import-View: große Überschriften = Acts, kleinere = Chapters, Text = Summaries.
- **Syntax [ABGELEITET, nicht im Text belegt]**:
```
# Act 1
## Chapter 1: Titel
Summary Szene 1 …

Summary Szene 2 …   (Absatz/Leerzeile = neue Szene? – unverifiziert)
```
- **Parsing-Regeln für die Portierung**: `#` → Act, `##` → Chapter, Absatzblöcke → Szenen mit Summary; fehlt ein Act, impliziten Act anlegen; leere Kapitel erlaubt; Vorschau mit Bestätigung.
- Der Chat kann per **Extract** ein passendes Outline erzeugen (`/help/docs/organization/chat-with-plan`).

### 5.6 Actions-Menü [TEILWEISE OFFIZIELL]
`/help/docs/plan/plan-actions-menu` war nicht abrufbar. Belegt aus Blog und Manuscript-Doku:
- **Plan-Ebene**: Nummerierung an/aus, Export, Löschen, **merge chapters**, **split acts**.
- **Szenen-Menü**: Custom POV („Edit scene POV“), Subtitle, Duplicate Scene, Export, **Summarise**, **Detect characters**, **Chat with scene**, **Szene von der KI ausschließen** (Anhänge, Vorworte), Revision History.

### 5.7 Scene Summaries, Beats, POV, Subplots [OFFIZIELL]
- **Summary**: Planungsebene und Basis für `storySoFar`/`storyToCome`; nach dem Schreiben per KI erzeugbar.
- **Scene Beats**: Anweisungsblöcke im Manuskript, aus denen Prosa entsteht. Das Kurs-Cookbook unterscheidet einfache und detaillierte Beats; laut FAQ `/help/faq/write/beats-per-scene` hat der System-Prompt einen Standard von 400 Wörtern, für mehr oder weniger Text ändert man die Wortzahl-Auswahl am Scene Beat.
- **POV/Tense**: Default auf Novel-Ebene (`novel.tense`, `pov`), pro Szene überschreibbar (`pov.isOverwrite`), POV-Character nur vom Typ Character.
- **Subplots**: Codex-Einträge vom Typ Subplot mit Aliasen wie „SP1“ und Progressions pro Szene (`/help/docs/write/subplots`).

### 5.8 Zusammenspiel Plan ↔ Write ↔ Codex ↔ Chat
```
Plan (Summary, POV, Labels, Referenzen) ──► storySoFar / storyToCome / scene.*
Write (Prosa, Beats, Progressions)     ──► textBefore/After, message, Progression-Auflösung
Codex (Einträge, Tracking, Relations)  ──► codex.context → XML im Prompt
Chat (Kontext-Auswahl) ──Extract──►  Codex-Einträge / Summaries / Beats / Outline
```

---

## 6. WEITERE FUNKTIONEN

- **Write-Interface [OFFIZIELL]** (`/help/docs/write/*`, `/features`): Rich Text (fett, kursiv, unterstrichen, Listen, Überschriften, Zitate); anpassbares Format-Menü (Abstände, legasthenie-freundliche Schrift, Größe); Dark Mode; **Focus Mode**; **Marker/Highlighter** und **Marker Timeline** (Sprungnavigation mit proportionalen Szenenlängen); **Sections** für Notizen oder Alternativen. **Generating Prose**: Beat → Prompt/Preset → Inputs → Generierung mit Fade-in, dazu Fortsetzung am Textende. **Revision History** pro Szene. Find-and-Replace ist laut FAQ geplant.
- **Chat / Workshop [OFFIZIELL]**: Kontext-Button (Szenen, Kapitel, Acts, Snippets; Progressions bis zur letzten gewählten Szene), Persona/Prompt/Preset wechselbar, gespeicherte Threads (im Mentions-Tab durchsuchbar), Extract (`/help/docs/chat/transfering-information`). Einsatz: Brainstorming, Charakter-Gespräche, Beta-Reader, Outline-Analyse (`/help/docs/chat/uses-for-chat`). Chat und Manuskript lassen sich nebeneinander öffnen.
- **Snippets, Pinning, Layout [OFFIZIELL]**: Freitexte mit Codex-Erkennung, im Prompt über `snippets.get`; anheftbare und geteilte Panels (`/help/docs/app/pinning`, `/help/docs/app/app-layout`); reduziertes Mobil-Layout.
- **Review [OFFIZIELL, Features-Seite]**: Appearance Heatmap, Charaktere pro Szene, Wortstatistiken; laut Drittquellen „basic“ vs. „advanced“ je nach Tier.
- **Series, Templates, Cover**: Serien mit geteiltem Codex, **persönliche Novel Templates**, Covers (`/help/docs/organization/adding-a-cover-to-your-novel`), POV/Tense-Einstellungen. Pen Names nur als Codex-Anwendungsfall auf der Romance-Seite erwähnt.
- **Import/Export [OFFIZIELL]**: Import Word (.docx), Markdown, Apple Pages (Features-Seite zusätzlich HTML); Export Novel (auch einzelne Acts/Chapters/Scenes), **Scrivener**, **Atticus**. **[ABGELEITET]** Überschriften-Ebenen → Act/Chapter wie bei Create from Outline; exakte Regeln nicht verifiziert.
- **Collaboration**: Co-Authoring und Teams (`/help/docs/app/collaboration-and-coauthoring`); laut Drittquellen braucht jeder schreibende Mitarbeiter ein eigenes Abo, Team-Management im Specialist-Tier; read-only-Novels laut Changelog. Feineres Rollenmodell nicht verifiziert.

**Pricing und Feature-Gating [OFFIZIELL + DRITTQUELLEN]**

| Tier | Preis/Monat | Umfang |
|---|---|---|
| Scribe | $4 | Schreiben, Plan, Codex, unbegrenzt Bücher und Serien, Basic Review, **keine KI** |
| Hobbyist | $8 | + BYOK-KI (Beats, Replacements, eigene Prompts) |
| Artisan | $14 | + volle Workshop-Chat-Funktionen, Advanced Review |
| Specialist | $20 | + Collaboration, Team-Management, Priority Support |

Laut Pricing-Seite gibt es 21 Tage uneingeschränkten Zugriff auf alle Funktionen ohne Kreditkarte, bei Jahreszahlung „2 Months off“ und „No special sales, discounts or holiday promotions“. Die Feature-Zuordnung steht auf der offiziellen Seite `novelcrafter.com/pricing`: Scribe mit unbegrenzten Büchern, Series & Universes und Basic Review; Hobbyist mit „AI (Bring your own Key)“, KI-Szenen-Zusammenfassung, KI-Charakterextraktion, Generierung aus Scene Beats und Live Chat; Artisan mit Chat Features und Advanced Review (in der Vergleichstabelle als „Advanced (planned)“ markiert); Specialist mit Collaborative Writing, Teams und Priority Support.

**Neuere Features 2025–2026 [OFFIZIELL]**: Mai 2025 neues Prompting-System (Inputs, Presets, Kontextoptionen für alle Typen, `local()`, case-insensitive Funktionen, eigene XML-Elemente, Migrationstool, Clipboard-Import); Codex-Tracking mit Case-sensitive, Exclusions, Mehrfachkategorien; Januar 2026 Doku zu Thinking und Model-Tuning; Blog-Modelltests (GPT-5, Sonnet 4.5, Opus 5, NSFW) und „Why I love the Codex“ (August 2026).

---

## 7. OPEN-SOURCE-ALTERNATIVEN

### 7.1 Lorebook-Mechanik als Vorlage für den Kontext-Builder

**SillyTavern World Info [OFFIZIELL, docs.sillytavern.app/usage/core-concepts/worldinfo]**

- **Keys**: Keywords, standardmäßig case-insensitiv; Regex im JS-Stil (`/…/flags`).
- **Optional Filter (Secondary Keys)** mit Selective Logic **AND ANY**, **AND ALL**, **NOT ANY**, **NOT ALL**.
- **Content**: Nur dieser Text wird eingefügt – Einträge müssen für sich allein verständlich sein.
- **Insertion Order**: höhere Werte näher am Prompt-Ende, stärkere Wirkung.
- **Insertion Position**: Before/After Char Defs, Before/After Example Messages, Top/Bottom of Author's Note, `@ D` mit Tiefe und Rolle, **Outlet** (`{{outlet::Name}}` sammelt Inhalte für eine frei gewählte Stelle).
- **Strategy**: Constant (🔵), Keyword (🟢), Vectorized (🔗, Embedding-Ähnlichkeit). **Probability** 0–100 %.
- **Inclusion Groups**: nur ein Eintrag pro Gruppe – per Group Weight, Prioritize Inclusion oder Group Scoring (meiste Key-Treffer).
- **Scan Depth**: gescannte Nachrichten, pro Eintrag überschreibbar.
- **Budget** (Context % oder feste Tokenzahl): zuerst Constant, dann höhere Order; direkte Treffer vor rekursiven; optional „Alert on overflow“.
- **Recursion**: Inhalt aktivierter Einträge wird erneut gescannt; pro Eintrag Non-recursable, Prevent further recursion, Delay until recursion (mit Level); **Max Recursion Steps** und **Min Activations** schließen sich aus.
- **Match whole words** (Default an; schädlich bei Sprachen ohne Leerzeichen); **Timed Effects** Sticky, Cooldown, Delay (in Nachrichten); Character Filter, Trigger nach Generierungsart, Quellen-Reihenfolge Chat → Persona → Character/Global.

**NovelAI Lorebook [OFFIZIELL docs.novelai.net + COMMUNITY]** (proprietär, als Konzept lehrreich): Keys auch als Regex, `&` verlangt mehrere Keys im Suchfenster, Always On, Suchbereich bis 10.000 Zeichen; Insertion Order (niedrige Werte fallen bei Platzmangel weg), Reserved Tokens (absolut oder Anteil unter 1), Insertion Position und Type (Token/Satz/Zeile); Cascading Activation, Phrase Bias pro Eintrag, Categories mit **Subcontext**. Neuere Updates ersetzen erweiterte Einfügeoptionen durch „Advanced Conditions“.

**Mapping auf Novelcrafter [ABGELEITET]**:

| Novelcrafter | World Info |
|---|---|
| Aliases | Keys |
| Always include | Constant |
| Include when detected | Keyword-Strategie, Scan-Quelle = Beat/Auswahl/Nachricht |
| Relations | Rekursion, aber explizit statt textbasiert |
| Progressions | Timed Effects, aber an die Plan-Position gebunden statt an Nachrichten |

Novelcrafter hat kein Token-Budget, keine Probability und keine Inclusion Groups – genau diese Lücke kann ein Nachbau schließen.

### 7.2 Vergleichstabelle

| Projekt | Repo | Lizenz | Stack | Aktivität 2026 | Kernfeatures | Bewertung |
|---|---|---|---|---|---|---|
| **The Story Nexus (Tauri)** | github.com/vijayk1989/TheStoryNexusTauriApp | nicht verifiziert | Tauri, React/TS | aktiv (MSI-Releases) | Kapitel-Editor, Lorebook-Matching, Prompts, Scene Beats, Brainstorm, Agent-Pipelines, local-first | **Fork-Kandidat TS** |
| **The Story Nexus (Web-Fork)** | github.com/JonSilver/TheStoryNexus | nicht verifiziert | Express, SQLite/Drizzle, React, Vite, Lexical | aktiv | Lorebook, Custom Prompts, Scene Beat (Alt+S), OpenAI/Gemini/OpenRouter/lokal, Docker | **Fork-Kandidat TS (Web)** |
| **Story Labyrinth** | github.com/bloodgrv/story-labyrinth | nicht verifiziert | Express + SQLite | aktiv | Codex-State mit Propose→Approve, Snapshots, RAG (FTS5 + sqlite-vec), MCP, Multi-Provider | studieren (Continuity/RAG) |
| **Grimodex** | github.com/kazormia296/Grimodex | nicht verifiziert | Electron, React, SQLite FTS5 | aktiv | „Novelcrafter follower“: Codex, Extract aus Chat, Snippets, Herkunft human/ai, Ollama, MCP; Japanisch-Fokus | studieren (Extract, Attribution) |
| **Novel-Engine** | github.com/Jackela/Novel-Engine | nicht verifiziert | Fastify/TS + React | sehr aktiv (PRs Sep. 2026) | Beats, Lorebook mit Budget, Review, Lorebook-Wizard | studieren (OpenSpec-Specs) |
| **SillyTavern** | github.com/SillyTavern/SillyTavern | AGPL-3.0 (laut GitHub-Organisation und offizieller Doku; über 300 Contributors) | Node/JS | sehr aktiv (Update 15.09.2026, rund 33.600 Stars) | World Info, Prompt Manager, Makros | **Referenzimplementierung** (`public/scripts/world-info.js`); AGPL beachten |
| **novelWriter** | github.com/saga-soft/novelWriter (früher vkbo/novelWriter) | GPL-3.0-or-later (laut PyPI zusätzlich Apache-2.0, CC-BY-4.0, ISC für Bestandteile) | Python ≥ 3.11, Qt6/PyQt6 | aktiv (letztes Release auf PyPI am 05.09.2026; Milestone „Release 26.3 Beta 1“ im September 2026) | Plain-Text-Projekte, Markdown-artige Syntax mit Meta-Tags, VCS-freundlich; keine KI | studieren (Python, Datenformat) |
| **bibisco** | github.com/andreafeccomandi/bibisco | Open Source, Lizenz nicht verifiziert | Desktop | Community Edition gepflegt | Figuren-Interviews, Prämisse, Fabula, Erzählstränge, Export; keine KI | studieren (Planungs-UX) |
| **Manuskript** | – | GPL (nicht verifiziert) | Python/Qt | nicht verifiziert | Outliner, Snowflake, Figuren, Plots | nur studieren |
| **Lore Codex** | github.com/KantikPotatoe/Lore-Codex | nicht verifiziert | Desktop (Windows) | aktiv | Lore-Wiki, isolierte DB pro Welt mit `.lore`-Spiegelung, offline | nur Idee |

Stars, Lizenzen und letzte Commits ließen sich für die meisten Repos nicht verifizieren – vor dem Forken `LICENSE` und Historie prüfen. Obsidian Longform, Obsidian-KI-Plugins, KoboldAI World Info und Plotbunni wurden nicht im Detail geprüft.

### 7.3 Empfehlung
- **TypeScript/Web**: Datenmodell und Template-Engine dieser Spezifikation **neu bauen**; Editor-Stack (Lexical oder TipTap, SQLite/Drizzle) und Lorebook-Matching aus **The Story Nexus (JonSilver-Fork)** übernehmen oder forken. Den Aktivierungsalgorithmus bei SillyTavern **studieren**, wegen AGPL aber nicht kopieren, falls die eigene Lizenz inkompatibel ist.
- **Python**: kein tragfähiger KI-Fork. Das Plain-Text-Format von **novelWriter** inspiriert ein Git-freundliches Speicherformat; Backend (Context-Builder, Template-Engine, Provider-Abstraktion) selbst bauen.
- **Über Novelcrafter hinaus übernehmen**: Token-Budget und Priorisierung (World Info), Herkunft human/ai (Grimodex), Propose→Approve für KI-Änderungen am Codex (Story Labyrinth), local-first.

---

## 8. PORTIERUNGS-HINWEISE FÜR CLAUDE CODE

### 8.1 Datenmodell (TypeScript-Skizze) [ABGELEITET]
```ts
type ID = string;
type CodexType = 'character'|'location'|'object'|'lore'|'subplot'|'other';
type AIContextMode = 'always'|'whenDetected'|'notWhenDetected'|'never';

interface Novel { id: ID; seriesId?: ID; title: string; author?: string; language: string;
  defaultPov: PovSetting; tense: 'past'|'present'; }
interface Act { id: ID; novelId: ID; order: number; name?: string; numbered: boolean; }
interface Chapter { id: ID; actId: ID; order: number; name?: string; numbered: boolean; }
interface Scene { id: ID; chapterId: ID; order: number; subtitle?: string; summary?: string;
  content: EditorDoc;               // Rich-Text inkl. BeatNodes, SectionNodes, Marker
  povOverride?: PovSetting; labelIds: ID[]; manualReferenceIds: ID[];
  excludeFromAI: boolean; archived: boolean; }
interface PovSetting { type: 'first'|'second'|'third'; mode?: 'limited'|'omniscient'; characterId?: ID; }

interface CodexEntry { id: ID; scope: {novelId?: ID; seriesId?: ID}; type: CodexType;
  name: string; aliases: string[]; description: string; notes: string; tags: string[];
  categoryIds: ID[]; color?: string; thumbnailUrl?: string;
  tracking: { enabled: boolean; caseSensitive: boolean; exclusions: string[] };
  aiContext: AIContextMode; details: {definitionId: ID; value: string}[]; }
interface DetailDefinition { id: ID; name: string; kind: 'text'|'line'|'dropdown'|'codexRef';
  appliesTo: CodexType[]; aiVisibility: 'always'|'never'|'nsfwOnly';
  options?: {label: string; color?: string}[]; }
interface Relation { parentId: ID; childId: ID; }   // gerichtet, rekursiv
interface Progression { id: ID; entryId: ID; sceneId: ID; detailId?: ID; mode: 'add'|'replace'; text: string; }

type ContextRef = {kind:'scene'|'chapter'|'act'|'snippet'|'codex'|'novelOutline'|'fullNovel'; id?: ID};
type PromptType = 'sceneBeat'|'summary'|'textReplacement'|'chat'|'component';
interface Prompt { id: ID; name: string; type: PromptType; system: string;
  messages: {role:'user'|'assistant'; template: string}[]; inputs: PromptInput[];
  models: ModelConfig[]; thinking?: 'avoid'|'prefer'; builtIn: boolean; }
interface PromptInput { name: string; required: boolean;
  allowed: { text?: boolean; dropdown?: {label: string; content?: string}[]; contextKinds?: ContextRef['kind'][] };
  default?: unknown; }
interface Preset { id: ID; promptId: ID; name: string; modelConfigId?: ID; inputValues: Record<string, unknown>; }
interface ModelConfig { id: ID; connectionId: ID; modelId: string; temperature?: number; topP?: number;
  maxTokens?: number; frequencyPenalty?: number; presencePenalty?: number; reasoningEffort?: string; }
interface AIConnection { id: ID; provider: 'openai'|'anthropic'|'openrouter'|'groq'|'ollama'|'lmstudio'|'openaiCompatible';
  apiKey?: string; baseUrl?: string; }
```
Weitere Entitäten analog: Series, Label, CodexCategory, Snippet, ChatThread (Kontext-Refs, Messages, Persona), Persona, Defaults (account/series/novel × Prompt-Typ), PromptVersion.

### 8.2 Anforderungen an die Template-Engine
1. **Parser**: Text mit `{…}`, `{! !}`-Kommentaren und verschachtelbaren Blöcken `{#if}`/`{#elseif}`/`{#else}`/`{#endif}`. Doppelte geschweifte Klammern bleiben literal. Straight Quotes; typografische Anführungszeichen erzeugen einen klaren Fehler.
2. **Ausdrücke**: `ns.name(args…)` oder ohne Klammern, case-insensitiv; Operatoren `+`, `is`, `in`; keine Verkettung.
3. **Typsystem**: `List<T>` mit Modus all/any, `TextContainer{title, content, attrs, ref, format}`, `Outline{mode}`, Entitäts-Referenzen; **Koerzionstabelle** pro Parametertyp nach dem Muster „Can collect from“ der Referenz.
4. **Renderer**: XML (rekursiv, Attribute), Markdown, Plain Text; leere Ergebnisse werden leerer String, **nie Fehler**.
5. **Registry**: Funktionen als Plugins mit Signatur, Doku und Beispielen für Autocomplete nach `{` (Original: ↑/↓, Tab/Enter, Ctrl+Space).
6. **Scope pro Aufruf**: `{novel, act, chapter, scene, cursorOffset, message, selection, contextRefs, inputs, promptModel, nsfw, locals}`.
7. **Message-Assembly**: leere Messages entfernen, aufeinanderfolgende gleiche Rollen verbinden.
8. **Validierung**: ungenutzte oder fehlende Inputs, fehlende Components, Legacy-Syntax.

### 8.3 Logik des Kontext-Builders
```
buildContext(scope, prompt):
 1. position := scope.scene (bei Mehrfachkontext: chronologisch letzte Szene)
 2. scanText := message + selection + beatText  (optional: textBefore-Fenster)
 3. detected := match(scanText, Einträge mit tracking.enabled)
      Name+Aliase, caseSensitive?, Exclusions zuerst maskieren, Wortgrenzen,
      (EN) Auto-Plural; deutsche Flexion über Aliase/Stemmer [Designentscheidung]
 4. base := {aiContext=always} ∪ {detected mit whenDetected}
          ∪ manuelle ContextRefs ∪ scene.manualReferenceIds ∪ POV-Character
 5. expanded := closure(base über parent→child), visited-Set gegen Zyklen, Warnung ab N
 6. filter: never raus; nur erkannte notWhenDetected raus; Szenen mit excludeFromAI raus
 7. resolveProgressions(entry, position):
      progs := Progressions mit planOrder(scene) <= planOrder(position), sortiert
      desc := description; je p: p.mode=='replace' ? p.text : desc+"\n"+p.text
      analog pro Detail; Details nach aiVisibility filtern (nsfwOnly ⇢ prompt.nsfw)
 8. storySoFar := Summaries vor position (ohne excludeFromAI/archived), Schnittmenge optionaler Filter
 9. Budget [Erweiterung]: Tokens schätzen; Priorität always > direkt erkannt > Relation;
      storySoFar von vorn kürzen bzw. zu Kapitel-Summaries verdichten; Overflow-Warnung
10. Template rendern → Messages → Provider-Adapter (Streaming, Abbruch, Thinking-Flag)
```

### 8.4 Implementierungs-Reihenfolge
1. **MVP**: Novel/Act/Chapter/Scene mit Grid, Outline und Drag & Drop; Rich-Text-Editor mit Scene-Beat-Node; Codex (Typen, Aliase, Description/Notes, AI Context, Matching mit Unterstreichung und Preview-Card); eine OpenAI-kompatible Connection (deckt Ollama, LM Studio, OpenRouter ab); Template-Engine mit Kernfunktionen (`storySoFar`, `codex.context`, `codex.get`, `pov`, `message`, `textBefore`, `#if`); vier System-Prompts; Streaming.
2. **Stufe 2**: Progressions, Relations, Custom Details, Categories/Tags, Mentions-Tab; Matrix (POV, Labels, Codex, Subplots); Prompt Library (Klonen, Inputs, Presets, Components, Defaults, Preview, Versionen).
3. **Stufe 3**: Chat mit Kontextauswahl und Personas; Extract, Create from Outline; Summarization, Detect Characters; Revision History, Archiv, Import (docx/md), Export (docx/md/Scrivener).
4. **Stufe 4**: Series-Codex, Heatmap/Statistiken, Thinking, Model Collections, Sharing per String, Collaboration/Sync, Token-Budget, RAG.

### 8.5 Anbindung einer Dramatica-Pipeline [ABGELEITET]
- **Storyform und Throughlines** (OS/MC/IC/RS) als Codex-Einträge vom Typ Subplot oder Lore, mit Aliasen wie „OS“, „MC-TL“ und Dropdown-Details für Domain, Concern, Issue, Problem. Progressions pro Szene bilden den Signpost-/Journey-Fortschritt ab; die Matrix zeigt pro Szene die aktive Throughline.
- **Beats und Signposts** als Scene Labels („Signpost 2“, „Throughline: IC“), im Prompt per `#if "Throughline: MC" in scene.labels`.
- **Import**: Planungsdaten als Markdown im Create-from-Outline-Format (Act/Chapter/Summary); Szenen-Metadaten über eine eigene JSON-Import-API (über das Original hinaus).
- **Deutsch**: Flexion (Genitiv-s, Adjektivendungen) ist beim Alias-Matching die größte Lücke gegenüber dem Original, das nur englische Plurale automatisch erkennt.

### 8.6 Offene Punkte (nicht belastbar recherchiert)
- Exakte Eingabesyntax von Create from Outline (nur Screenshot) und Szenentrennung beim Import.
- Vollständiges Plan-Actions-Menü; Seite nicht abrufbar.
- Offizieller Status von `{#elseif}`/`{#else}`; Seite zur Conditional Logic nicht abrufbar.
- Wortgrenzen und nicht-englisches Matching.
- Genaue XML-Ausgabe von Details und Progressions; Reihenfolge der Codex-Einträge im Prompt.
- Token-Zählung und Budget im Original; Semantik der „AI credits“.
- Quick-Create-Vorlagen für Details; Submenü-Syntax; `nc-`-Editor-Blöcke.
- Rollenmodell der Collaboration; Feature-Zuordnung zu Tiers (überwiegend Drittquellen).
- Lizenzen, Stars und letzter Commit der meisten Open-Source-Repos.
