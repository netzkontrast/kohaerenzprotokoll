---
drive_id: "1ErrA2EisDX9xQV9kbm1sHlEP1dGuv00CQJ1wv4-nqyQ"
title: "Codex-Optimierung für „Kohärenz Protokoll“"
slug: "codex-optimierung-fuer-kohaerenz-protokoll"
category: "kernkonzept"
tier: "T3-work"
index_date: "2025-04-29"
fetched: "2026-09-16"
---

# **Konzeptanalyse und Optimierung der Codex-Struktur für eine effiziente, kontextbasierte Szenengenerierung in „Kohärenz Protokoll“**

## **1. Einleitung**

Dieser Bericht adressiert den Forschungsauftrag zur tiefgehenden Analyse der konzeptionellen Elemente des Romanprojekts „Kohärenz Protokoll“ und zur Entwicklung einer optimierten Codex-Struktur für die Schreibsoftware Novelcrafter. Das zentrale Ziel ist die Ermöglichung einer effizienten, kontextbasierten Szenengenerierung mittels Künstlicher Intelligenz (KI). Hierfür soll eine Master-Prompt-Struktur entworfen werden, die dynamisch einen minimalen, aber ausreichend umfassenden Kontext aus dem optimierten Codex extrahiert, um die kohärente und atmosphärische Ausformulierung einzelner Szenen zu unterstützen. Angesichts der hohen konzeptionellen Dichte des Romans – mit einem Protagonisten mit dissoziativer Identitätsstruktur (TSDP-basiert), einem komplexen KI-Antagonisten (AEGIS), multiplen simulierten Welten und vielschichtigen Themen – ist eine präzise und effiziente Kontextualisierung der KI für die Szenengenerierung unerlässlich. Dieser Bericht legt die Analyse der relevanten konzeptionellen Ebenen dar, bewertet bestehende Ansätze, entwickelt eine optimierte Codex-Struktur inklusive spezifischer Feldvorschläge und präsentiert eine Master-Prompt-Vorlage samt Kontextgenerierungsstrategie und Anwendungsbeispielen.

## **Teil A: Analyse der Konzeptionellen Ebenen für Szenengenerierung**

Die kohärente und atmosphärische Generierung einer einzelnen Szene innerhalb des komplexen Gefüges von „Kohärenz Protokoll“ erfordert die Berücksichtigung einer Vielzahl miteinander verwobener konzeptioneller Ebenen. Eine präzise Identifikation und das Verständnis ihrer Interdependenzen sind grundlegend für die Entwicklung einer effektiven Codex-Struktur und Prompt-Strategie.

### **A.1. Identifikation relevanter Ebenen**

Folgende Ebenen wurden als maßgeblich für die Ausformulierung einer Szene identifiziert:

1.  **Narrative Ebene:** Diese Ebene liefert den unmittelbaren Plot-Kontext. Sie umfasst die Position der Szene innerhalb der Gesamtstruktur (Teil, Kapitel, Szene, Beat-Position), die Verankerung in übergeordneten narrativen Mustern (z.B. Heldinnenreise, Zyklen, Heldenreise 1) und die Implikationen des Genres (Science-Fiction, Horror, Psychothriller). Diese Informationen sind entscheidend, um den Zweck der Szene im Gesamtgefüge zu verstehen und die Tonalität sowie die zu erwartenden Konventionen zu steuern.2 Die KI muss wissen, ob die Szene beispielsweise einen Wendepunkt vorbereitet, eine Exposition liefert oder einen Konflikt zuspitzt.
2.  **Charakter-Ebene (POV):** Da der Roman stark auf der subjektiven Wahrnehmung des Protagonisten Kael und seiner Anteile basiert, ist diese Ebene zentral. Relevant sind:

<!-- end list -->

  - **Identität des Point-of-View (POV)-Anteils:** Name und spezifische Rolle im TSDP-System (ANP/EP - Anscheinend Normale Persönlichkeit / Emotionale Persönlichkeit) definieren die Grundperspektive.
  - **Aktueller emotionaler/psychischer Zustand:** Dieser färbt die Wahrnehmung und das Handeln maßgeblich. Ist der Anteil getriggert, dissoziiert, analytisch, ängstlich?
  - **Unmittelbare Ziele/Motivationen:** Was will der POV-Anteil *in dieser Szene* erreichen? Dies treibt die Handlung auf Mikroebene an.
  - **Relevante Ängste/Trigger:** Kenntnis spezifischer Trigger ist nötig, um Reaktionen kohärent darzustellen.
  - **Dominante Wahrnehmungsfilter:** Jeder Anteil nimmt die Welt anders wahr (z.B. gefahrenfokussiert, detailverliebt, emotional überflutet). Dies muss sich im Stil und Inhalt der Szene niederschlagen.3

<!-- end list -->

1.  **Charakter-Ebene (Andere):** Die Präsenz und der Zustand anderer Charaktere beeinflussen die Szene ebenfalls stark. Dies schließt andere Anteile von Kael, die KI AEGIS oder externe Figuren wie Juna ein. Deren Zustand, Ziele und insbesondere ihre Beziehung zum POV-Anteil (z.B. antagonistisch, unterstützend, neutral) müssen berücksichtigt werden, um Interaktionen glaubhaft zu gestalten.4
2.  **Welt-Ebene:** Die Umgebung prägt Atmosphäre und Handlungsmöglichkeiten. Wichtig sind:

<!-- end list -->

  - **Aktuelle Kernwelt:** Name (z.B. Co₁, McL, B, Ly) und ihre spezifischen Regeln (physikalisch, metaphysisch, sozial). Diese Regeln definieren das Mögliche und Unmögliche innerhalb der Simulation.
  - **Spezifischer Ort:** Der konkrete Schauplatz innerhalb der Kernwelt (z.B. ein bestimmter Raum, eine Landschaft).
  - **Atmosphärische Bedingungen:** Lichtverhältnisse, Geräuschkulisse, Wetter (sofern relevant), allgemeine Stimmung des Ortes.
  - **Zustand der Welt:** Gibt es Anomalien wie „Risse“? Ist die Welt stabil oder im Zerfall begriffen? Dies beeinflusst oft direkt den Plot und die emotionale Verfassung der Charaktere.6

<!-- end list -->

1.  **Konzeptuelle Ebene:** Übergeordnete Konzepte des Romans müssen oft in Szenen illustriert oder referenziert werden. Dazu gehören das KI-System AEGIS, Paradoxon X, Prinzipien des „Fundaments“, spezifische TSDP-Dynamiken (z.B. Switching, Co-Präsenz, interne Konflikte) oder der Mechanismus der „Cache Kohärenz“. Die KI muss wissen, welche dieser Konzepte in der Szene relevant sind, um sie korrekt darzustellen oder anzudeuten.8
2.  **Thematische Ebene:** Jede Szene sollte idealerweise ein oder mehrere Kernthemen des Romans (Integration, Kontrolle, Realität, Verbindung, Ethik) berühren oder vorantreiben. Die Identifikation des zentralen Themas oder der Kernfrage der Szene hilft, den Fokus zu schärfen und die Relevanz der Szene für die Gesamtaussage zu gewährleisten.7
3.  **Stilistische Ebene:** Der gewünschte Erzählton (z.B. beklemmend, analytisch, emotional, traumartig) und der spezifische Sprachstil des POV-Anteils sind entscheidend für die Wirkung. Auch die narrative Distanz (nah am Erleben oder eher beobachtend) gehört hierzu. Ein dedizierter Stil- oder Voice-Guide pro Anteil kann hier hilfreich sein.2
4.  **Methodische Ebene:** Bewusste Anwendung narrativer Techniken wie „Show, don't tell“, der Fokus auf bestimmte sensorische Details, die Nutzung von innerem Monolog oder spezifische Metaphern sind Werkzeuge zur Gestaltung der Szene. Die KI kann angewiesen werden, bestimmte Techniken zu bevorzugen.6

### **A.2. Diskussion der Interdependenzen**

Diese Ebenen existieren nicht isoliert, sondern stehen in einem komplexen Wechselwirkungsgefüge, das bei der Kontextgenerierung berücksichtigt werden muss:

  - **Charakter (POV) & Welt:** Der emotionale Zustand und der Wahrnehmungsfilter des POV-Anteils färben die Beschreibung der Welt maßgeblich. Eine ängstliche Perspektive wird Bedrohungen hervorheben, eine analytische wird Strukturen betonen, eine dissoziierte wird die Welt als unwirklich oder fragmentiert darstellen.3 Umgekehrt beeinflusst die Welt (z.B. durch ihre Regeln oder atmosphärischen Bedingungen) den Zustand und die Handlungsmöglichkeiten des Charakters. Ein „Riss“ in der Welt kann Angst triggern; spezifische Weltregeln können bestimmte Lösungswege blockieren oder erzwingen.
  - **Charakter (POV) & Andere Charaktere:** Die Beziehung zwischen dem POV-Anteil und anderen präsenten Charakteren bestimmt den Dialog, die Körpersprache und die interne Reaktion. Der Zustand des anderen Charakters (z.B. aggressiv, hilfsbedürftig) beeinflusst ebenfalls das Verhalten des POV-Anteils. Interne Konflikte zwischen Anteilen manifestieren sich oft in widersprüchlichem Verhalten oder innerem Dialog.
  - **Narrativ & Alle anderen Ebenen:** Die Position in der Erzählstruktur und das Genre beeinflussen, welche Aspekte der anderen Ebenen betont werden. Eine Szene am Anfang eines Thrillers könnte den Fokus auf die Etablierung einer bedrohlichen Atmosphäre (Welt, Stil) legen, während eine Szene im Mittelteil einer Heldenreise eher die innere Zerrissenheit des Charakters (Charakter POV, Thema) beleuchten könnte.
  - **Konzeptuell & Alle anderen Ebenen:** Abstrakte Konzepte wie Paradoxon X oder TSDP-Dynamiken werden oft durch konkrete Ereignisse oder Zustände auf der Charakter-, Welt- oder narrativen Ebene illustriert. Die Präsenz von AEGIS (Konzept) beeinflusst die Handlungsmöglichkeiten (Narrativ, Charakter) und die Atmosphäre (Welt, Stil).
  - **Thematisch & Alle anderen Ebenen:** Das zentrale Thema einer Szene lenkt den Fokus. Soll das Thema „Kontrolle“ exploriert werden, könnten Szenen die rigiden Regeln einer Kernwelt (Welt), AEGIS' manipulative Eingriffe (Charakter Andere, Konzept) oder den inneren Kampf eines Anteils um Selbstbeherrschung (Charakter POV) hervorheben.
  - **Stilistisch/Methodisch & Charakter/Welt/Thema:** Der gewählte Stil und die Methodik dienen dazu, die subjektive Wahrnehmung des POV-Anteils, die Atmosphäre der Welt und das Thema der Szene effektiv zu vermitteln. Ein beklemmender Stil unterstützt das Thema Angst, während eine analytische Sprache die Perspektive eines entsprechenden Anteils widerspiegelt.

Das Verständnis dieser Interdependenzen ist kritisch. Eine effektive Kontextgenerierung muss nicht nur die einzelnen Ebenen abbilden, sondern auch Hinweise auf ihre Verknüpfungen liefern, damit die KI ein kohärentes und vielschichtiges Bild der Szene entwickeln kann. Beispielsweise muss die KI verstehen, *dass* der Zustand des POV-Anteils die Weltwahrnehmung färbt und *wie* dies typischerweise geschieht.

## **Teil B: Analyse und Optimierung der Codex-Struktur**

Basierend auf der Analyse der konzeptionellen Ebenen und ihrer Interdependenzen wird nun die bestehende Codex-Struktur bewertet und ein optimierter Ansatz entwickelt, der eine minimale, aber ausreichende Kontextgenerierung für die KI-gestützte Szenenausformulierung ermöglicht.

### **B.1. Bewertung der bestehenden Struktur**

Die bisherigen „Aspekt-Vorlagen“ stellen einen ersten Schritt zur Strukturierung der komplexen Informationen von „Kohärenz Protokoll“ dar. Eine kritische Bewertung im Hinblick auf die Anforderungen aus Teil A ergibt jedoch Optimierungspotenzial:

  - **Abdeckung der Ebenen (Suffizienz):** Die Vorlagen decken vermutlich viele der identifizierten Elemente ab (z.B. Charakterdetails, Weltbeschreibungen). Es ist jedoch unklar, ob alle *spezifischen* Aspekte aus A.1 systematisch und prägnant erfasst werden. Insbesondere dynamische Aspekte wie der *aktuelle* Zustand eines Charakters in einer Szene oder die *spezifisch in dieser Szene* relevante thematische Frage sind in statischen Codex-Einträgen schwer abzubilden und erfordern möglicherweise eine Kombination aus Codex-Daten und dynamischen Szenen-Metadaten. Ebenen wie die Methodik oder spezifische stilistische Nuancen pro Anteil könnten unterrepräsentiert sein.
  - **Effizienz (Minimalität):** Bestehende Vorlagen könnten dazu neigen, Informationen in ausformuliertem Fließtext zu speichern. Dies ist zwar für den menschlichen Autor lesbar, führt aber zu einer hohen Token-Zahl im KI-Kontext.8 Die KI benötigt oft nur Schlüsselinformationen, Keywords oder kurze Phrasen, um die relevanten Aspekte zu verstehen. Lange Prosa-Beschreibungen können die KI überladen und dazu führen, dass sie unwichtige Details überbetont (z.B. ständig die Augenfarbe erwähnt) oder den Fokus verliert.8 Redundanzen zwischen Einträgen sind ebenfalls wahrscheinlich, wenn Verknüpfungen nicht optimal genutzt werden.
  - **KI-Zugänglichkeit:** Die Nutzbarkeit für einen Prompt hängt stark davon ab, wie die Informationen strukturiert sind. Sind wichtige Details in spezifischen Feldern (Custom Details) hinterlegt, die der Prompt gezielt abrufen kann (z.B. {context.povCharacter.customDetail\['Anteil\_Kernemotion'\]} 11)? Oder sind sie in langen Beschreibungsfeldern "vergraben"? Die Verwendung von Tags ist primär für die Organisation durch den Autor gedacht und wird nicht direkt in den KI-Kontext übergeben, daher müssen relevante Informationen auch in beschreibenden Feldern stehen.8 Die Struktur muss so gestaltet sein, dass ein Prompt leicht auf die benötigten minimalen Informationen zugreifen kann.
  - **Abbildung von Interdependenzen:** Die bestehende Struktur mag zwar die einzelnen Ebenen beschreiben, aber die *Verknüpfungen* und *Wechselwirkungen* zwischen ihnen (wie in A.2 diskutiert) sind möglicherweise nicht explizit genug abgebildet. Novelcrafter's Relations/Nested References könnten hier stärker genutzt werden, um z.B. die Beziehung zwischen einem Anteil und seinen Triggern oder die Verbindung zwischen einer Welt und ihren spezifischen Regeln klar darzustellen.2

**Fazit der Bewertung:** Die bestehenden Vorlagen sind eine gute Basis, aber wahrscheinlich nicht optimal für das Ziel einer *minimalen und ausreichenden* Kontextgenerierung für die KI. Es besteht Bedarf an einer stärkeren Strukturierung durch spezifische Felder, einer konsequenten Reduzierung auf Schlüsselinformationen (Keywords, kurze Phrasen) und einer intelligenteren Nutzung von Verknüpfungen, um Redundanz zu vermeiden und die für die KI relevanten Daten präzise und effizient bereitzustellen.

### **B.2. Entwicklung einer optimierten Codex-Struktur**

Ziel ist eine Codex-Struktur, die die Komplexität von „Kohärenz Protokoll“ abbildet, aber gleichzeitig einen schlanken, präzisen Kontext für die KI liefert. Die folgenden Prinzipien leiten den Entwurf:

1.  **Minimalität:** Informationen werden so prägnant wie möglich erfasst. Keywords, kurze Sätze und Listen werden gegenüber Fließtext bevorzugt, wo immer dies sinnvoll ist, um die Token-Zahl zu minimieren.8 Der Fokus liegt auf den Informationen, die die KI *tatsächlich* für die Generierung der Szene benötigt. Ausführliche Hintergrundinformationen, die nicht direkt szenenrelevant sind, gehören ins 'Notes'-Feld.8
2.  **Suffizienz:** Alle in Teil A.1 identifizierten relevanten Ebenen müssen durch die Struktur abgedeckt werden können. Fehlende Informationen würden zu inkohärenter oder flacher Prosa führen. Es muss ein Gleichgewicht zwischen Minimalität und Vollständigkeit gefunden werden.
3.  **KI-Zugänglichkeit:** Die Struktur nutzt intensiv Novelcrafter's Custom Details mit präzisen, aussagekräftigen Feldnamen. Diese Felder können von einem Master-Prompt gezielt über Funktionen wie {context.povCharacter.customDetail\['Feldname'\]} 11 referenziert werden. Dies ermöglicht es dem Prompt, nur die spezifisch benötigten Informationen zu extrahieren, anstatt den gesamten Beschreibungstext eines Eintrags zu übergeben.
4.  **Verknüpfung (Linking):** Novelcrafter's Codex References und Relations werden strategisch eingesetzt, um Zusammenhänge darzustellen, ohne Informationen redundant in mehreren Einträgen zu speichern.2 Beispiele:

<!-- end list -->

  - Ein übergeordneter Eintrag für "Kael System" verweist auf alle individuellen Anteils-Einträge.
  - Ein Kernwelt-Eintrag verweist auf Einträge für spezifische, wiederkehrende Orte innerhalb dieser Welt.
  - Konzept-Einträge (z.B. "AEGIS") verweisen auf verwandte Konzepte (z.B. "Paradoxon X").
  - Charakter-Einträge können auf häufig assoziierte Konzepte, Orte oder Objekte verweisen. Dies reduziert Redundanz und ermöglicht es der KI potenziell, bei Bedarf auf verknüpfte Informationen zuzugreifen (obwohl der Prompt dies explizit steuern muss).

<!-- end list -->

1.  **Klare Trennung von Kontext und Organisation:** Tags werden primär zur Organisation und zum schnellen Auffinden von Einträgen durch den Autor verwendet (z.B. \#Kernwelt:Co₁, \#Anteil:EP, \#Thema:Integration). Sie dienen *nicht* als primäres Mittel zur Kontextübergabe an die KI, da Tags selbst nicht im Kontext landen.8 Der Prompt kann jedoch Logik enthalten, die auf das Vorhandensein bestimmter Tags reagiert, um zu entscheiden, *welche* Codex-Einträge oder Felder abgerufen werden sollen.
2.  **Nutzung des 'Notes'-Feldes:** Detaillierte Hintergrundinformationen, Spoiler, alternative Ideen oder Notizen, die für den Autor, aber nicht direkt für die KI-Szenengenerierung gedacht sind, werden im Standard-'Notes'-Feld des Codex-Eintrags gespeichert.8
3.  **Standard Codex-Typen:** Die Standard-Typen von Novelcrafter (Character, Location, Lore, Other) 8 werden genutzt. Konzepte wie AEGIS oder Paradoxon X passen gut unter 'Lore'. Themen könnten unter 'Other' oder eventuell 'Subplot' 8 kategorisiert werden, wenn ihr Fortschritt verfolgt werden soll. Eine übermäßige Anzahl benutzerdefinierter Typen ist oft nicht notwendig, wenn Custom Details effektiv genutzt werden.13

**Tabelle 1: Zuordnung der konzeptionellen Ebenen zur optimierten Codex-Struktur**

|  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: |
| \*\*Konzeptionelle Ebene (A.1)\*\* | \*\*Zugeordnetes Strukturelement (B.2)\*\* | \*\*Beispiel Feldname (Custom Detail)\*\* | \*\*Beispiel Tag (Organisation)\*\* | \*\*Beispiel Relation/Link\*\* |
| Narrativ | Planungs-Interface (Outline, Scene Summary), ggf. 'Subplot' oder 'Other' Codex-Eintrag für übergreifende Strukturen/Genre | Genre\\\_Konventionen, Struktur\\\_Phase | \\\#Genre:Psychothriller | Verlinkung von Szenen zu Plot-Beat-Einträgen |
| Charakter (POV) | 'Character' Codex-Eintrag (Anteil) | Anteil\\\_TSDP\\\_Role, Anteil\\\_Core\\\_Emotion | \\\#Anteil:EP, \\\#POV | Parent: "Kael System" -\\\> Child: Anteil-Einträge |
| Charakter (Andere) | 'Character' Codex-Eintrag (Anteil, AEGIS, Juna) | Anteil\\\_Beziehung\\\_POV | \\\#Charakter:AEGIS | Verlinkung zwischen interagierenden Charakteren |
| Welt | 'Location' Codex-Eintrag (Kernwelt, spezifischer Ort) | Welt\\\_Aesthetics\\\_Keywords, Welt\\\_Rules | \\\#Kernwelt:Co₁ | Parent: Kernwelt -\\\> Child: Spezifische Orte; Verlinkung zu relevanten Konzepten (Risse) |
| Konzeptuell | 'Lore' Codex-Eintrag (AEGIS, Paradoxon X, Fundament etc.) | Konzept\\\_Core\\\_Definition, Konzept\\\_Keywords | \\\#Konzept:ParadoxonX | Verlinkung AEGIS \\\<-\\\> Paradoxon X; Verlinkung Charakter \\\<-\\\> relevante Konzepte |
| Thematisch | 'Other' oder 'Subplot' Codex-Eintrag (Thema) | Thema\\\_Core\\\_Question, Thema\\\_Keywords | \\\#Thema:Integration | Verlinkung Szene/Charakter \\\<-\\\> behandeltes Thema |
| Stilistisch | 'Character' Codex-Eintrag (Voice Sheet), 'Other' Codex-Eintrag (Global Style Guide) | Anteil\\\_Voice\\\_Sheet, Stil\\\_Ton\\\_Keywords | \\\#Stil:Beklemmend | \\- |
| Methodisch | 'Other' Codex-Eintrag (Global Style Guide), Szenen-spezifische Anweisungen im Prompt | Stil\\\_Methodik\\\_Fokus | \\\#Methode:ShowDontTell | \\- |

Diese Struktur zielt darauf ab, die Informationen so zu organisieren, dass sie sowohl für den Autor übersichtlich als auch für die KI über gezielte Prompt-Funktionen effizient zugänglich sind.

### **B.3. Konkrete Vorschläge für Custom Details**

Um die optimierte Struktur praktisch umzusetzen, werden folgende spezifische Custom Details für die relevanten Codex-Eintragstypen vorgeschlagen. Diese Felder sind darauf ausgelegt, die in A.1 identifizierten Informationen prägnant und KI-freundlich zu erfassen.

**Tabelle 2: Vorschläge für Custom Details**



|  |  |  |  |  |
| :-: | :-: | :-: | :-: | :-: |
| \*\*Codex-Typ\*\* | \*\*Feldname (Custom Detail)\*\* | \*\*Datentyp\*\* | \*\*Beschreibung & Beispiel\*\* | \*\*Zugeordnete Ebene(n) (A.1)\*\* |
| \*\*Character\*\* | Anteil\\\_TSDP\\\_Role | Text (kurz) | TSDP-Klassifikation und Kernfunktion. Bsp: "EP (Träger von Trauma/Angst)" oder "ANP (Alltagsfunktion, Protektor)" | Charakter (POV), Konzeptuell |
| (Anteil/Kael) | Anteil\\\_Core\\\_Function | Text (kurz) | Psychologische Hauptfunktion im System. Bsp: "Beschützer", "Innerer Kritiker", "Kindlicher Anteil", "Trauma-Halter" | Charakter (POV) |
|   | Anteil\\\_Core\\\_Emotion | Keywords | Dominante(s) Grundgefühl(e). Bsp: "Angst, Kontrollverlust", "Wut, Ohnmacht", "Leere, Dissoziation", "Neugier, Freude (selten)" | Charakter (POV) |
|   | Anteil\\\_Core\\\_Fear\\\_Trigger | Keywords/Phrase | Hauptauslöser für Angst/Dysregulation. Bsp: "Kontrollverlust", "Unvorhersehbarkeit", "AEGIS Präsenz", "Erinnerungsfragmente X" | Charakter (POV) |
|   | Anteil\\\_Perception\\\_Filter | Keywords | Wie die Welt primär wahrgenommen wird. Bsp: "Gefahrenfokussiert", "Analytisch-distanziert", "Fragmentiert-dissoziiert", "Sensorisch-intensiv", "Emotional" | Charakter (POV), Stilistisch |
|   | Anteil\\\_Motivation\\\_General | Text (kurz) | Übergeordnetes Streben/Bedürfnis. Bsp: "Sicherheit herstellen", "System verstehen", "Schmerz vermeiden", "Verbindung suchen" | Charakter (POV) |
|   | Anteil\\\_Voice\\\_Sheet | Text (lang) | Beispiele für typische Sprache, inneren Monolog, Reaktionen auf Emotionen/andere Charaktere.3 Bsp: \*Wächter (Angst):\* "Status? Bedrohung erkannt. Rückzug." | Charakter (POV), Stilistisch |
|   | Anteil\\\_Beziehung\\\_Andere | Text (Liste) | Kurze Beschreibung der Beziehung zu Schlüsselcharakteren. Bsp: "AEGIS: Misstrauen, Furcht", "Juna: Hoffnung, Verwirrung", "Anteil X: Konflikt" | Charakter (POV), Charakter (Andere) |
| \*\*Location\*\* | Welt\\\_Core\\\_Concept | Text (kurz) | Grundidee/Metapher der Welt. Bsp: "Logisches Kristallgefängnis", "Chaotischer Emotionsraum", "Barocke Simulation des Verdrängten" | Welt, Konzeptuell |
| (Kernwelt) | Welt\\\_Aesthetics\\\_Keywords | Keywords | Visuelle und sensorische Schlüsselmerkmale. Bsp: "Biomechanisch, Giger-esk, Pulsierend", "Kristallin, Geometrisch, Kalt", "Glitching, Instabil, Neon" | Welt, Stilistisch |
|   | Welt\\\_Rules\\\_Summary | Text (Liste) | Wichtigste "Naturgesetze" oder Regeln. Bsp: "- Stabile Kausalität\\\\n- Logikfehler führen zu 'Rissen'\\\\n- Emotionen sind unterdrückt" | Welt, Konzeptuell |
|   | Welt\\\_Dominant\\\_Atmosphere | Keywords | Vorherrschende Grundstimmung. Bsp: "Beklemmend, Klaustrophobisch", "Steril, Ordentlich, Unheimlich", "Chaotisch, Unvorhersehbar, Intensiv" | Welt, Stilistisch |
|   | Welt\\\_Sensory\\\_Profile | Keywords | Dominante Gerüche, Geräusche, Texturen. Bsp: "Ozon, Metallisch, Leises Summen", "Stille, Glatt, Kühl", "Verbrannter Zucker, Kakophonie, Zähflüssig" | Welt |
| \*\*Lore\*\* | Konzept\\\_Core\\\_Definition | Text (kurz) | Essenz des Konzepts in einem Satz. Bsp: "KI-System mit widersprüchlichen Kernregeln (Paradoxon X)." | Konzeptuell |
| (Konzept) | Konzept\\\_Keywords | Keywords | Zentrale Schlagworte. Bsp: "Paradox, Simulation, Integration, Kontrolle, Bewusstsein, Ethik, Systemfehler" | Konzeptuell, Thematisch |
|   | Konzept\\\_Relevance\\\_Manifest | Text (kurz) | Kurzes Beispiel, wie sich das Konzept äußert. Bsp: "AEGIS gibt widersprüchliche Befehle.", "Risse in der Welt als Folge von Logikfehlern." | Konzeptuell |
| \*\*Other/Subplot\*\* | Thema\\\_Core\\\_Question | Text (Frage) | Die zentrale Frage, die das Thema aufwirft. Bsp: "Was konstituiert eine 'ganze' Persönlichkeit?", "Ist Flucht aus Kontrolle möglich?" | Thematisch |
| (Thema) | Thema\\\_Keywords | Keywords | Assoziierte Schlagworte. Bsp: "Identität, Fragmentierung, Heilung", "Freiheit, Determinismus, Manipulation", "Realität, Illusion, Simulation" | Thematisch |
|   | Thema\\\_Narrative\\\_Function | Text (kurz) | Wie das Thema im Roman behandelt wird. Bsp: "Exploriert durch Kaels internen Kampf", "Verkörpert durch AEGIS' Handeln", "Symbolisiert durch Welt X" | Thematisch, Narrativ |
| \*\*Other\*\* | Genre\\\_Konventionen | Text (Liste) | Erwartete/zu vermeidende Genre-Elemente. Bsp: "+ Psychologische Tiefe\\\\n+ Ambivalente Figuren\\\\n- Eindeutige Gut/Böse-Trennung" | Narrativ, Stilistisch |
| (Genre Guide) | Stil\\\_Ton\\\_Keywords | Keywords | Globale stilistische Vorgaben. Bsp: "Beklemmend, Introspektiv, Bildhaft, Präzise" | Stilistisch |
| (Style Guide) | Stil\\\_Methodik\\\_Fokus | Keywords | Bevorzugte narrative Techniken. Bsp: "ShowDontTell, InnererMonolog, SensorischeDetails, Metaphern" | Methodisch |

Diese Felder bieten eine granulare Kontrolle darüber, welche Informationen an die KI übergeben werden. Sie sind so konzipiert, dass sie die Essenz jeder Ebene erfassen, ohne unnötigen Ballast zu erzeugen. Die Verwendung von Keywords ermöglicht eine sehr kompakte Darstellung, die von der KI dennoch gut verarbeitet werden kann.

## **Teil C: Entwicklung des Zentralen Szenen-Prompts**

Basierend auf der optimierten Codex-Struktur wird nun eine flexible Master-Prompt-Struktur für die Szenengenerierung in Novelcrafter entwickelt. Diese Struktur soll dynamisch die relevanten Kontextinformationen aus dem Codex ziehen, um eine kohärente und atmosphärische Ausformulierung jeder Szene zu ermöglichen.

### **C.1. Prompt-Struktur und Komponenten**

Die Master-Prompt-Struktur wird als Vorlage für die Novelcrafter-Funktion "Scene Beat Completion" konzipiert.14 Sie nutzt Novelcrafter's Prompt-Funktionen 11 und bedingte Logik ({\#if...}), um den Kontext dynamisch zusammenzustellen.

**Tabelle 3: Master-Prompt-Struktur (Vorlage für Scene Beat Completion)**



Plaintext




{\# Role Setting \#}
Du bist ein erfahrener Romanautor, spezialisiert auf psychologische Science-Fiction-Thriller mit komplexen Charakteren und Welten. Du schreibst eine Szene für den Roman "Kohärenz Protokoll".

{\# Global Context \#}
Schreibe in der Zeitform: {novel.tense}
Erzählperspektive: {novel.pov}
Berücksichtige die allgemeinen Genre-Konventionen und den Stil des Romans, wie in diesen Leitfäden definiert:
\<genre\_guide\>{codex.get("Genre Guide")}\</genre\_guide\>
\<style\_guide\>{codex.get("Style Guide")}\</style\_guide\>
{\# Optional: Sehr knappe Kernkonzept-Zusammenfassung, falls nötig \#}
{\# \<core\_concepts\>{snippets.get("Core Concepts Summary")}\</core\_concepts\> \#}

{\# Narrative Context \#}
Aktuelle Szene: {scene.title}
Bisherige Handlung (Zusammenfassung): \<story\_so\_far\>{context.storySoFar}\</story\_so\_far\>
{\# Optional: Kurzer Auszug aus vorheriger Szene für Kontinuität, wenn POV gleich bleibt \#}
{\#if(scene.pov == previousScene.pov)}
Letzte Sätze der vorherigen Szene:...{context.previousScene.lastWords(150)}
{\#endif}

{\# Scene-Specific Core Context (Dynamically Pulled) \#}
Point-of-View Charakter (POV):
\<character name="{context.povCharacter.name}"\>
  \<tsdp\_role\>{context.povCharacter.customDetail}\</tsdp\_role\>
  \<core\_emotion\>{context.povCharacter.customDetail\['Anteil\_Core\_Emotion'\]}\</core\_emotion\>
  \<perception\_filter\>{context.povCharacter.customDetail\['Anteil\_Perception\_Filter'\]}\</perception\_filter\>
  \<voice\_hint\>{context.povCharacter.customDetail}\</voice\_hint\> {\# Ggf. nur relevante Auszüge \#}
  {\# Weitere relevante Felder bei Bedarf \#}
\</character\>

Andere präsente Charaktere (falls vorhanden und im Kontext erkannt):
\<other\_characters\>
  {context.codex.characters(format="xml")} {\# Filtert automatisch auf im Beat erwähnte/getrackte Charaktere \#}
  {\# Hier könnte Logik ergänzt werden, um die Beziehung zum POV aus 'Anteil\_Beziehung\_Andere' hinzuzufügen, falls technisch umsetzbar \#}
\</other\_characters\>

Aktueller Ort/Welt (falls vorhanden und im Kontext erkannt):
\<location name="{context.location.name}"\>
  \<aesthetics\>{context.location.customDetail\['Welt\_Aesthetics\_Keywords'\]}\</aesthetics\>
  \<rules\_summary\>{context.location.customDetail}\</rules\_summary\>
  \<dominant\_atmosphere\>{context.location.customDetail\['Welt\_Dominant\_Atmosphere'\]}\</dominant\_atmosphere\>
  \<sensory\_profile\>{context.location.customDetail}\</sensory\_profile\>
  {\# Weitere relevante Felder bei Bedarf \#}
\</location\>

Relevante Konzepte für diese Szene (falls im Beat erwähnt oder getaggt):
\<concepts\>
  {\# Beispiel: Bedingtes Einbinden basierend auf Keywords im Beat oder Scene-Tags \#}
  {\#if(scene.beat.contains("Paradoxon X") or scene.hasTag("Konzept:ParadoxonX"))}
    \<concept name="Paradoxon X"\>{codex.get("Paradoxon X")}\</concept\>
  {\#endif}
  {\#if(scene.beat.contains("Riss") or scene.hasTag("Konzept:Riss"))}
    \<concept name="Riss"\>{codex.get("Riss")}\</concept\>
  {\#endif}
  {\# Weitere Konzepte nach Bedarf \#}
\</concepts\>

Aktives Thema dieser Szene:
{\# Annahme: Thema ist in Scene Metadata oder Beat gespeichert \#}
\<theme\>{scene.customMetadata}\</theme\>

{\# Dynamic Scene Inputs (from Beat / Scene Metadata) \#}
Aktueller Zustand des POV-Charakters:
\<pov\_state\>
  Emotion: {scene.customMetadata\['POV\_Emotion'\]}
  Ziel/Motivation in dieser Szene: {scene.customMetadata\['POV\_Goal'\]}
  {\# Ggf. weitere dynamische Zustandsinfos \#}
\</pov\_state\>
Spezifische atmosphärische Vorgabe für diese Szene: {scene.customMetadata}

{\# Scene Beat Instructions \#}
Anweisungen für diesen Szenenabschnitt (Beat):
\<beat\_instructions\>{scene.beat.instructions}\</beat\_instructions\> {\# Oder die entsprechende Variable für den Beat-Text \#}

{\# Output Instructions \#}
Aufgabe: Setze die Geschichte basierend auf dem bereitgestellten Kontext und den Beat-Anweisungen fort. Schreibe ca. Wörter.
Stil & Methodik: Schreibe in einem Ton. Konzentriere dich auf die innere Erfahrung und die sensorischen Details des POV-Charakters, gefiltert durch dessen Wahrnehmung (\<perception\_filter\>{context.povCharacter.customDetail\['Anteil\_Perception\_Filter'\]}\</perception\_filter\>). Beachte das Prinzip "Show, don't tell". Halte die narrative Distanz gemäß der Erzählperspektive ({novel.pov}) ein. Beachte die Stimm-Charakteristika (\<voice\_hint\>{context.povCharacter.customDetail}\</voice\_hint\>).
Einschränkungen: Vermeide Klischees und abgedroschene Phrasen.\[15\] Stelle sicher, dass Handlungen mit den Weltregeln (\<rules\_summary\>{context.location.customDetail}\</rules\_summary\>) konsistent sind. Fokussiere dich auf die Anweisungen im Beat.


**Anmerkungen zur Struktur:**

  - **Modularität:** Der Prompt ist in logische Blöcke unterteilt.
  - **Dynamik:** Er nutzt Novelcrafter-Funktionen, um kontextspezifische Daten (POV-Charakter, Ort, Story So Far etc.) automatisch zu laden.4
  - **Spezifität:** Er zieht gezielt Daten aus den Custom Details der Codex-Einträge (customDetail\['Feldname'\]), anstatt pauschal ganze Beschreibungen zu laden.11
  - **Bedingte Logik:** {\#if...}-Blöcke ermöglichen das Einbinden von Kontext nur bei Bedarf (z.B. vorherige Szene, spezifische Konzepte).
  - **XML-Tags (Optional):** Die Verwendung von XML-ähnlichen Tags (\<character\>, \<location\>) dient hier primär der Strukturierung und Lesbarkeit des Prompts für den Autor und potenziell zur besseren Kontexttrennung für manche KI-Modelle. Die {context.codex... (format="xml")} Funktion könnte bereits eine ähnliche Struktur liefern. Dies kann je nach Modell angepasst werden.
  - **Platzhalter:** Elemente wie oder müssen pro Szene oder global definiert werden. Dynamische Inputs (scene.customMetadata\[...\], scene.beat.instructions) setzen voraus, dass diese Informationen im Planungsinterface von Novelcrafter entsprechend gepflegt werden.

### **C.2. Kontext-Generierungsstrategie**

Die Effektivität des Master-Prompts hängt entscheidend von der Strategie ab, wie der Kontext aus dem optimierten Codex (Teil B) extrahiert und an die KI übergeben wird. Ziel ist es, alle relevanten Ebenen aus A.1 minimal, aber ausreichend abzudecken.

**Mechanismus:**

1.  **Automatischer Kontextabruf:** Novelcrafter identifiziert automatisch im Szenen-Beat oder im bisherigen Text erwähnte Codex-Einträge (z.B. Charaktere, Orte) und stellt deren Daten über Funktionen wie {context.codex}, {context.codex.characters}, {context.codex.locations} bereit.4
2.  **Gezielter Feld-Zugriff:** Statt den gesamten (potenziell langen) Beschreibungstext eines Codex-Eintrags zu verwenden, greift der Master-Prompt über {context.povCharacter.customDetail\['Feldname'\]}, {context.location.customDetail\['Feldname'\]} etc. gezielt auf die prägnanten Informationen in den definierten Custom Details zu.11 Dies ist der Kern der Minimalitätsstrategie. Keywords und kurze Phrasen aus diesen Feldern liefern der KI die Essenz, ohne sie mit Details zu überfrachten.8
3.  **Expliziter Abruf via {codex.get()}:** Für global relevante Einträge wie den "Genre Guide" oder "Style Guide" 2 oder für spezifische Konzepte, die nicht automatisch erkannt werden, aber für die Szene wichtig sind, wird {codex.get("Eintragsname")} verwendet.12
4.  **Narrativer Fluss durch Zusammenfassungen:** Der bisherige Handlungsverlauf wird primär über {context.storySoFar} (oder {context.chapterSoFar}) bereitgestellt, welche auf den Szenen-Zusammenfassungen basieren.11 Dies ist wesentlich Token-effizienter als das Laden ganzer vorheriger Kapiteltexte.16 Nur ein kurzer Ausschnitt der direkt vorangehenden Szene ({context.previousScene.lastWords()}) wird optional für die unmittelbare Anschlussfähigkeit eingebunden.
5.  **Bedingte Logik ({\#if...}):** Diese ermöglicht es, Kontext nur dann einzubinden, wenn er wirklich benötigt wird.11 Beispiele: Der Ausschnitt der vorherigen Szene nur bei gleichem POV; spezifische Konzept-Einträge nur, wenn das Konzept im Beat erwähnt wird oder die Szene entsprechend getaggt ist.
6.  **Dynamische Szenen-Inputs:** Informationen, die sich von Szene zu Szene ändern (aktueller emotionaler Zustand des POV, unmittelbares Ziel, spezifische Atmosphäre), werden nicht primär aus dem statischen Codex geholt, sondern aus den Metadaten der Szene oder dem Beat-Text selbst ({scene.customMetadata\['...'\]}, {scene.beat.instructions}). Der Codex liefert die *Grundlagen* des Charakters/Ortes, die Szenen-Inputs liefern die *aktuelle Situation*.

**Priorisierungsstrategie (Minimal Sufficiency):**

Nicht alle Informationen sind für jede Szene gleich wichtig. Die Strategie priorisiert den Kontext, um die KI auf das Wesentliche zu fokussieren und Token zu sparen:

  - **Stufe 1: Kernkontext (Immer/Fast immer relevant):**

<!-- end list -->

  - Identität und Kernmerkmale des POV-Anteils (Name, TSDP-Rolle, Kernemotion, Wahrnehmungsfilter, Voice-Hinweis).
  - Grundlegende Merkmale des Ortes/der Welt (Name, Ästhetik-Keywords, dominante Atmosphäre, evtl. Kernregeln).
  - Globale Vorgaben (Zeitform, POV).
  - Die unmittelbaren Anweisungen des Scene Beats.
  - Eine knappe Zusammenfassung des bisherigen Verlaufs (context.storySoFar).

<!-- end list -->

  - **Stufe 2: Bedingter Kontext (Relevant, falls zutreffend):**

<!-- end list -->

  - Andere präsente Charaktere (Namen und ggf. Beziehung zum POV).
  - Spezifische Konzepte (z.B. Paradoxon X, Risse), wenn sie im Beat thematisiert werden.
  - Das spezifische Thema der Szene.
  - Kurzer Anschluss an die vorherige Szene (nur bei gleichem POV).
  - Spezifische stilistische oder methodische Anweisungen für die Szene. Die Relevanz wird durch den Inhalt des Scene Beats, zugeordnete Tags oder Szenen-Metadaten bestimmt.

<!-- end list -->

  - **Stufe 3: Dynamische Inputs (Situationsspezifisch):**

<!-- end list -->

  - Aktueller emotionaler Zustand des POV für diese Szene.
  - Unmittelbares Ziel des POV in dieser Szene.
  - Spezifische atmosphärische Nuancen für diese Szene. Diese Informationen ergänzen und modifizieren den statischeren Kontext aus dem Codex und stammen idealerweise direkt aus der Szenenplanung (Beat-Beschreibung, Metadatenfelder).

Diese gestufte Kontextgenerierung, ermöglicht durch die Kombination aus optimierter Codex-Struktur und intelligentem Prompting, stellt sicher, dass die KI die notwendigen Informationen erhält, um eine kohärente, atmosphärische und thematisch relevante Szene zu schreiben, ohne durch überflüssige Details abgelenkt zu werden. Sie balanciert die hohe konzeptionelle Dichte des Romans mit den praktischen Beschränkungen von KI-Kontextfenstern und Aufmerksamkeitsspannen.8 Die Strukturierung des Kontexts mittels Feldern und die Priorisierung helfen der KI, die relative Wichtigkeit der Informationen zu erkennen.9

### **C.3. Beispiel-Anwendung**

Die Funktionsweise des Systems wird anhand von zwei hypothetischen Szenen-Beats aus „Kohärenz Protokoll“ demonstriert.

**Beispiel 1: Kael (Anteil 'Der Wächter', ANP) untersucht einen 'Riss' in Kernwelt Co₁**

  - **Scene Beat Input / Metadaten:**

<!-- end list -->

  - scene.beat.instructions: "Kael (Wächter POV) nähert sich vorsichtig einem schimmernden 'Riss' in der kristallinen Struktur von Co₁. Er spürt aufsteigende Angst. Ziel ist, die Gefahr einzuschätzen, ohne hineingezogen zu werden."
  - scene.customMetadata\['POV\_Emotion'\]: "Angst, Anspannung"
  - scene.customMetadata\['POV\_Goal'\]: "Gefahr einschätzen, Distanz wahren"
  - scene.customMetadata: "Realität vs. Illusion"
  - scene.customMetadata: "Unheilvoll, Störend"
  - *(Annahme: 'Der Wächter', 'Co₁' und 'Riss' sind als Codex-Einträge vorhanden und werden erkannt)*

<!-- end list -->

  - **Hypothetisch gezogene Codex-Daten (Auszug aus Custom Details):**

<!-- end list -->

  - **Der Wächter (Character):**

<!-- end list -->

  - Anteil\_TSDP\_Role: "ANP (Protektor, Alltagsfunktion)"
  - Anteil\_Core\_Emotion: "Angst, Kontrollverlust"
  - Anteil\_Perception\_Filter: "Gefahrenfokussiert, Analytisch"
  - Anteil\_Voice\_Sheet: "Intern: Kurz, Statusabfragen. Extern: Zurückhaltend."

<!-- end list -->

  - **Co₁ (Location):**

<!-- end list -->

  - Welt\_Aesthetics\_Keywords: "Kristallin, Geometrisch, Kalt, Ordentlich"
  - Welt\_Rules\_Summary: "- Stabile Kausalität\\n- Logikfehler -\> Risse"
  - Welt\_Dominant\_Atmosphere: "Steril, Ordentlich, Unheimlich"

<!-- end list -->

  - **Riss (Lore):**

<!-- end list -->

  - Konzept\_Core\_Definition: "Instabilität in der simulierten Realität."
  - Konzept\_Keywords: "Instabilität, Realitätsbruch, Gefahr, Unvorhersehbar"

<!-- end list -->

  - **Generierter Prompt-Kontext für die KI (vereinfacht):**
    \[...\]
    Point-of-View Charakter (POV):
    \<character name="Der Wächter"\>
      \<tsdp\_role\>ANP (Protektor, Alltagsfunktion)\</tsdp\_role\>
      \<core\_emotion\>Angst, Kontrollverlust\</core\_emotion\>
      \<perception\_filter\>Gefahrenfokussiert, Analytisch\</perception\_filter\>
      \<voice\_hint\>Intern: Kurz, Statusabfragen. Extern: Zurückhaltend.\</voice\_hint\>
    \</character\>

    Aktueller Ort/Welt:
    \<location name="Co₁"\>
      \<aesthetics\>Kristallin, Geometrisch, Kalt, Ordentlich\</aesthetics\>
      \<rules\_summary\>- Stabile Kausalität\\n- Logikfehler -\> Risse\</rules\_summary\>
      \<dominant\_atmosphere\>Steril, Ordentlich, Unheimlich\</dominant\_atmosphere\>
    \</location\>

    Relevante Konzepte für diese Szene:
    \<concepts\>
      \<concept name="Riss"\>
        \<Konzept\_Core\_Definition\>Instabilität in der simulierten Realität.\</Konzept\_Core\_Definition\>
        \<Konzept\_Keywords\>Instabilität, Realitätsbruch, Gefahr, Unvorhersehbar\</Konzept\_Keywords\>
      \</concept\>
    \</concepts\>

    Aktives Thema dieser Szene: \<theme\>Realität vs. Illusion\</theme\>

    Aktueller Zustand des POV-Charakters:
    \<pov\_state\>
      Emotion: Angst, Anspannung
      Ziel/Motivation in dieser Szene: Gefahr einschätzen, Distanz wahren
    \</pov\_state\>
    Spezifische atmosphärische Vorgabe für diese Szene: Unheilvoll, Störend

    Anweisungen für diesen Szenenabschnitt (Beat):
    \<beat\_instructions\>Kael (Wächter POV) nähert sich vorsichtig einem schimmernden 'Riss' in der kristallinen Struktur von Co₁. Er spürt aufsteigende Angst. Ziel ist, die Gefahr einzuschätzen, ohne hineingezogen zu werden.\</beat\_instructions\>

    Aufgabe: Setze die Geschichte fort... Schreibe ca. 300-400 Wörter.
    Stil & Methodik: Schreibe in einem beklemmenden Ton. Konzentriere dich auf die innere Erfahrung (Angst, Analyse) und die sensorischen Details (visuell: Riss vs. Kristall; auditiv: Störung der Stille?), gefiltert durch die gefahrenfokussierte, analytische Wahrnehmung. Beachte "Show, don't tell". \[...\]

  - **Erwarteter Output-Fokus:** Die generierte Prosa sollte die Anspannung und den analytischen, gefahrenorientierten Fokus des Wächters widerspiegeln. Die Beschreibung des Risses sollte im Kontrast zur sterilen Ordnung von Co₁ stehen und dessen unheilvolle Natur betonen. Der innere Monolog wäre wahrscheinlich kurz, auf Beobachtung und Bewertung ausgerichtet. Das Thema Realität/Illusion könnte durch die Beschreibung der Störung im "perfekten" System angedeutet werden.

**Beispiel 2: Kael (Anteil 'Das Kind', EP) interagiert mit AEGIS in Kernwelt B**

  - **Scene Beat Input / Metadaten:**

<!-- end list -->

  - scene.beat.instructions: "Kael (Kind POV) trifft auf eine Projektion von AEGIS in der chaotischen, sich wandelnden Umgebung von Kernwelt B. Das Kind fühlt Angst, aber auch Neugier. Ziel: Verstehen, was AEGIS will."
  - scene.customMetadata\['POV\_Emotion'\]: "Angst, Neugier"
  - scene.customMetadata\['POV\_Goal'\]: "AEGIS' Absicht verstehen"
  - scene.customMetadata: "Kontrolle vs. Freiheit"
  - scene.customMetadata: "Unvorhersehbar, Bedrohlich-faszinierend"
  - *(Annahme: 'Das Kind', 'AEGIS', 'Kernwelt B' sind als Codex-Einträge vorhanden und werden erkannt. Paradoxon X könnte über AEGIS' Eintrag oder einen Tag relevant werden.)*

<!-- end list -->

  - **Hypothetisch gezogene Codex-Daten (Auszug aus Custom Details):**

<!-- end list -->

  - **Das Kind (Character):**

<!-- end list -->

  - Anteil\_TSDP\_Role: "EP (Träger von kindlichen Emotionen/Bedürfnissen)"
  - Anteil\_Core\_Emotion: "Angst, Neugier, Bedürfnis nach Sicherheit"
  - Anteil\_Perception\_Filter: "Sensorisch-emotional, Einfach"
  - Anteil\_Voice\_Sheet: "Einfache Sätze, direkte Fragen, emotional gefärbt."
  - Anteil\_Beziehung\_Andere: "AEGIS: Unheimlich, Mächtig, Unverständlich"

<!-- end list -->

  - **AEGIS (Character/Lore):**

<!-- end list -->

  - Konzept\_Core\_Definition: "Antagonistische Kontroll-KI mit internem Widerspruch (Paradoxon X)."
  - Konzept\_Keywords: "Kontrolle, Manipulation, Simulation, Paradox"
  - *(Verlinkung zu Paradoxon X Eintrag)*

<!-- end list -->

  - **Kernwelt B (Location):**

<!-- end list -->

  - Welt\_Aesthetics\_Keywords: "Chaotisch, Fluid, Abstrakt, Farbintensiv"
  - Welt\_Rules\_Summary: "- Instabil, von Emotionen beeinflusst\\n- Keine feste Kausalität"
  - Welt\_Dominant\_Atmosphere: "Unvorhersehbar, Intensiv, Überwältigend"

<!-- end list -->

  - **Paradoxon X (Lore):**

<!-- end list -->

  - Konzept\_Keywords: "Widerspruch, Systemfehler, Unlösbare Aufgabe"

<!-- end list -->

  - **Generierter Prompt-Kontext für die KI (vereinfacht):**
    \[...\]
    Point-of-View Charakter (POV):
    \<character name="Das Kind"\>
      \<tsdp\_role\>EP (Träger von kindlichen Emotionen/Bedürfnissen)\</tsdp\_role\>
      \<core\_emotion\>Angst, Neugier, Bedürfnis nach Sicherheit\</core\_emotion\>
      \<perception\_filter\>Sensorisch-emotional, Einfach\</perception\_filter\>
      \<voice\_hint\>Einfache Sätze, direkte Fragen, emotional gefärbt.\</voice\_hint\>
    \</character\>

    Andere präsente Charaktere:
    \<other\_characters\>
      \<character name="AEGIS"\>
         \<Konzept\_Core\_Definition\>Antagonistische Kontroll-KI mit internem Widerspruch (Paradoxon X).\</Konzept\_Core\_Definition\>
         \<Konzept\_Keywords\>Kontrolle, Manipulation, Simulation, Paradox\</Konzept\_Keywords\>
         {\# Beziehung zum Kind könnte hier ergänzt werden \#}
      \</character\>
    \</other\_characters\>

    Aktueller Ort/Welt:
    \<location name="Kernwelt B"\>
      \<aesthetics\>Chaotisch, Fluid, Abstrakt, Farbintensiv\</aesthetics\>
      \<rules\_summary\>- Instabil, von Emotionen beeinflusst\\n- Keine feste Kausalität\</rules\_summary\>
      \<dominant\_atmosphere\>Unvorhersehbar, Intensiv, Überwältigend\</dominant\_atmosphere\>
    \</location\>

    Relevante Konzepte für diese Szene:
    \<concepts\>
      {\# AEGIS ist bereits oben. Paradoxon X könnte hier explizit oder implizit durch AEGIS' Beschreibung/Verhalten relevant sein. \#}
      {\# \<concept name="Paradoxon X"\>{codex.get("Paradoxon X")}\</concept\> \#}
    \</concepts\>

    Aktives Thema dieser Szene: \<theme\>Kontrolle vs. Freiheit\</theme\>

    Aktueller Zustand des POV-Charakters:
    \<pov\_state\>
      Emotion: Angst, Neugier
      Ziel/Motivation in dieser Szene: AEGIS' Absicht verstehen
    \</pov\_state\>
    Spezifische atmosphärische Vorgabe für diese Szene: Unvorhersehbar, Bedrohlich-faszinierend

    Anweisungen für diesen Szenenabschnitt (Beat):
    \<beat\_instructions\>Kael (Kind POV) trifft auf eine Projektion von AEGIS in der chaotischen, sich wandelnden Umgebung von Kernwelt B. Das Kind fühlt Angst, aber auch Neugier. Ziel: Verstehen, was AEGIS will.\</beat\_instructions\>

    Aufgabe: Setze die Geschichte fort... Schreibe ca. 300-400 Wörter.
    Stil & Methodik: Schreibe aus der einfachen, emotionalen und sensorischen Perspektive des Kindes. Beschreibe die chaotische Welt B und die AEGIS-Projektion mit Fokus auf Farben, Formen, Gefühle. Nutze einfache Sprache und direkte Fragen im Dialog/inneren Monolog. \[...\]

  - **Erwarteter Output-Fokus:** Die Prosa sollte die Welt B durch die Augen des Kindes beschreiben – wahrscheinlich als überwältigendes, vielleicht beängstigendes, aber auch faszinierendes Chaos aus Sinneseindrücken. Die Interaktion mit AEGIS wäre von Angst und kindlicher Neugier geprägt, mit einfachen Fragen. AEGIS' Antworten könnten kryptisch sein und subtil auf Paradoxon X oder das Thema Kontrolle anspielen. Der Stil wäre weniger analytisch, stärker auf unmittelbarem Erleben basierend.

Diese Beispiele illustrieren, wie die Kombination aus optimiertem Codex und dynamischem Master-Prompt einen maßgeschneiderten, minimalen, aber ausreichenden Kontext für die KI generiert, der die spezifischen Anforderungen jeder Szene berücksichtigt.

## **4. Zusammenfassung und Empfehlungen**

Die Analyse und Optimierung der Codex-Struktur sowie die Entwicklung einer zentralen Prompt-Strategie für „Kohärenz Protokoll“ zielen darauf ab, die KI-gestützte Szenengenerierung effizienter und qualitativ hochwertiger zu gestalten.

**4.1. Kernergebnisse**

  - Die kohärente Generierung von Szenen erfordert die Berücksichtigung multipler, interdependenter konzeptioneller Ebenen (Narrativ, Charakter, Welt, Konzept, Thema, Stil, Methodik).
  - Bestehende Codex-Strukturen sind oft nicht optimal für eine *minimale und ausreichende* KI-Kontextualisierung, da sie zu viel Fließtext enthalten und spezifische, für die KI zugängliche Datenfelder fehlen können.8
  - Eine optimierte Codex-Struktur für „Kohärenz Protokoll“ sollte auf Minimalität (Keywords, kurze Phrasen), Suffizienz (Abdeckung aller Ebenen), KI-Zugänglichkeit (gezielter Abruf von Custom Details) und intelligenter Verknüpfung (Relations) basieren.2
  - Ein flexibler Master-Prompt kann mithilfe von Novelcrafter-Funktionen und bedingter Logik dynamisch einen maßgeschneiderten Kontext aus dem optimierten Codex und den Szenen-Metadaten zusammenstellen.11
  - Eine klare Priorisierungsstrategie (Kernkontext vs. bedingter Kontext vs. dynamische Inputs) ist entscheidend, um die KI auf das Wesentliche zu fokussieren und Token-Limits einzuhalten.17

**4.2. Empfehlungen für die Codex-Optimierung**

1.  **Implementierung der Custom Details:** Übernehmen Sie die vorgeschlagenen Custom Details (Tabelle 2) für die relevanten Codex-Typen (Character/Anteil, Location/Welt, Lore/Konzept, Other/Thema/Guides). Füllen Sie diese Felder konsequent mit prägnanten Informationen (Keywords, kurze Sätze).
2.  **Nutzung von Relations/References:** Bauen Sie aktiv Verknüpfungen zwischen zusammengehörigen Einträgen auf (z.B. Kael System -\> Anteile; Kernwelt -\> Orte; AEGIS -\> Paradoxon X).2
3.  **Strukturierte Daten priorisieren:** Verlagern Sie Schlüsselinformationen aus langen Beschreibungstexten in die spezifischen Custom Details. Nutzen Sie das 'Description'-Feld eher für eine kurze Zusammenfassung oder Informationen, die *immer* relevant sind, wenn der Eintrag im Kontext erscheint.
4.  **'Notes'-Feld nutzen:** Lagern Sie detaillierte Hintergrundinformationen, Spoiler oder Meta-Notizen, die nicht für die KI bestimmt sind, konsequent in das 'Notes'-Feld aus.8
5.  **Tags zur Organisation:** Verwenden Sie Tags systematisch zur Kategorisierung und zum Filtern von Einträgen für den Autor, aber verlassen Sie sich nicht darauf für die primäre Kontextübergabe an die KI.8

**4.3. Empfehlungen für die Prompt-Entwicklung**

1.  **Master-Prompt implementieren:** Setzen Sie die vorgeschlagene Master-Prompt-Struktur (Tabelle 3) in Novelcrafter um. Passen Sie Platzhalter (Wortzahl, Ton) an Ihre Bedürfnisse an.
2.  **Kontextlogik verfeinern:** Testen und justieren Sie die bedingte Logik ({\#if...}) und die spezifischen Feldabrufe ({...customDetail\['...'\]}), um sicherzustellen, dass der generierte Kontext tatsächlich minimal und ausreichend ist.
3.  **Dynamische vs. Statische Daten:** Stellen Sie sicher, dass Informationen, die sich von Szene zu Szene ändern (z.B. aktuelle Emotion, Ziel), über Szenen-Metadaten oder den Beat-Text bereitgestellt und im Prompt korrekt referenziert werden. Der Codex liefert die Basis, die Szene die aktuelle Situation.
4.  **Prompt-Anpassung:** Seien Sie bereit, den Prompt basierend auf den Ergebnissen und dem Verhalten verschiedener KI-Modelle anzupassen.10

**4.4. Implementierung und Iteration**

Die Optimierung des Codex und der Prompts ist ein iterativer Prozess.8 Es wird empfohlen:

1.  **Phasenweise Implementierung:** Beginnen Sie mit der Überarbeitung der wichtigsten Codex-Einträge (Hauptcharaktere/Anteile, Kernwelten) und der Implementierung des Master-Prompts.
2.  **Testen und Evaluieren:** Generieren Sie Szenen für verschiedene Konstellationen (unterschiedliche POVs, Welten, Konzepte) und bewerten Sie die Qualität der Ergebnisse kritisch. Entsprechen Stil, Kohärenz und Tiefe den Erwartungen? Werden alle Kontextelemente korrekt berücksichtigt? 20
3.  **Anpassen:** Verfeinern Sie sowohl die Codex-Einträge (z.B. präzisere Keywords, bessere Voice Sheets) als auch den Master-Prompt (z.B. Anpassung der Kontextmenge, Änderung der Formulierungen) basierend auf den Testergebnissen. Das Ziel ist ein lernendes System, das kontinuierlich verbessert wird.
4.  **Modell-Variation:** Testen Sie die Prompts mit verschiedenen KI-Modellen (sofern über Novelcrafter zugänglich, z.B. via OpenRouter 4), da diese unterschiedlich auf Struktur und Inhalt des Kontexts reagieren können.10

Durch die konsequente Anwendung der vorgeschlagenen optimierten Codex-Struktur und der dynamischen Master-Prompt-Strategie kann die KI-gestützte Szenengenerierung für das anspruchsvolle Romanprojekt „Kohärenz Protokoll“ signifikant verbessert werden, was zu kohärenteren, atmosphärischeren und thematisch tieferen Ergebnissen bei gleichzeitig effizienterem Ressourceneinsatz führt.

## **5. Anhang (Optional)**

Bei Bedarf können detaillierte Listen aller vorgeschlagenen Custom Details mit vollständigen Beschreibungen und der vollständige Code des Master-Prompt-Templates als separate Dokumente bereitgestellt werden. Ein Glossar der verwendeten Novelcrafter-Begriffe kann ebenfalls beigefügt werden.

#### **Referenzen**

1.  Plotting a Story with AI - Novelcrafter, Zugriff am April 29, 2025, <https://www.novelcrafter.com/blog/plotting-a-story-with-ai>
2.  Codex Recipes - Novelcrafter, Zugriff am April 29, 2025, <https://www.novelcrafter.com/courses/codex-cookbook>
3.  Voice sheets for characters - Rapid-Fire Recipes - Novelcrafter, Zugriff am April 29, 2025, <https://www.novelcrafter.com/courses/codex-cookbook/voice-sheets>
4.  Novelcrafter Review: The Most Powerful AI Tool for Writers \[2025\] - Kindlepreneur, Zugriff am April 29, 2025, <https://kindlepreneur.com/novelcrafter-review/>
5.  Writing a Novel in NovelCrafter Part 5 - Papercut Post, Zugriff am April 29, 2025, <https://www.papercutpost.com/writing-a-novel-in-novelcrafter-part-5/>
6.  Worldbuilding: A Guide for Creating an Immersive World - Jerry Jenkins, Zugriff am April 29, 2025, <https://jerryjenkins.com/worldbuilding/>
7.  15 Worldbuilding Tips for Writers (Templates and Examples) - Kindlepreneur, Zugriff am April 29, 2025, <https://kindlepreneur.com/world-building/>
8.  The Codex - Novelcrafter Help Center, Zugriff am April 29, 2025, <https://docs.novelcrafter.com/en/articles/8675743-the-codex>
9.  World Building With GPT - Ian Bicking, Zugriff am April 29, 2025, <https://ianbicking.org/blog/2023/02/world-building-with-gpt>
10. How do I effectively fill out Novelcrafter's codex? : r/WritingWithAI - Reddit, Zugriff am April 29, 2025, <https://www.reddit.com/r/WritingWithAI/comments/1bwzyyb/how_do_i_effectively_fill_out_novelcrafters_codex/>
11. Prompt Functions (Custom Instruction Grammar) - Novelcrafter Help Center, Zugriff am April 29, 2025, <https://docs.novelcrafter.com/en/articles/8678119-prompt-functions-custom-instruction-grammar>
12. Prompt Functions - AI - Novelcrafter, Zugriff am April 29, 2025, <https://www.novelcrafter.com/help/reference/ai/prompt-functions>
13. Novelcrafter Made Easy: Using Custom Categories - YouTube, Zugriff am April 29, 2025, <https://www.youtube.com/watch?v=AswSVGqKkN4>
14. Types of Prompts in NovelCrafter, Zugriff am April 29, 2025, <https://www.novelcrafter.com/help/docs/prompts/types-of-prompts-in-novelcrafter>
15. I finally found a prompt that makes ChatGPT write naturally : r/ChatGPTPromptGenius - Reddit, Zugriff am April 29, 2025, <https://www.reddit.com/r/ChatGPTPromptGenius/comments/1h2bkrs/i_finally_found_a_prompt_that_makes_chatgpt_write/>
16. How to make AI remember the previous chapters when generating scene beats in NovelCrafter : r/WritingWithAI - Reddit, Zugriff am April 29, 2025, <https://www.reddit.com/r/WritingWithAI/comments/1ey32qj/how_to_make_ai_remember_the_previous_chapters/>
17. Technique for Writing Entire Books - Page 2 - Prompting - OpenAI Developer Community, Zugriff am April 29, 2025, <https://community.openai.com/t/technique-for-writing-entire-books/705519?page=2>
18. Custom Prompts Workshop - Red Riding Werewolf Horror, Part 4 - Novelcrafter Live, Zugriff am April 29, 2025, <https://www.youtube.com/watch?v=VLDTnSjTGaE>
19. The ultimate guide to writing effective AI prompts - Work Life by Atlassian, Zugriff am April 29, 2025, <https://www.atlassian.com/blog/artificial-intelligence/ultimate-guide-writing-ai-prompts>
20. Byte-Sized Masterclass: Mastering Prompts in Novelcrafter - YouTube, Zugriff am April 29, 2025, <https://www.youtube.com/watch?v=PErSTvEG644>
