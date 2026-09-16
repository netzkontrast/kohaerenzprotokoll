---
drive_id: "1GehDbl2CIZIr7lJJ8sFWF3dymlckaSoLSdXyB2Yae4Q"
title: "Kohärenz Protokoll: Analyse und Verständnis"
slug: "kohaerenz-protokoll-analyse-und-verstaendnis"
category: "kernkonzept"
tier: "T3-work"
index_date: "2025-04-25"
fetched: "2026-09-16"
---

# **Analyse von Kohärenzprotokollen in Computersystemen**

**1. Einleitung: Verständnis von „Kohärenz Protokoll“ als Cache-Kohärenz**

**1.1. Primäre Definition**

Der Begriff „Kohärenz Protokoll“ wird im Deutschen primär im Kontext der Computerarchitektur verwendet und bezeichnet dort das „Cache Coherence Protocol“.1 Diese Protokolle sind grundlegende Hardware- oder Firmware-Mechanismen, die in Mehrprozessor- und Multi-Core-Systemen eingesetzt werden, um die Konsistenz von Daten zu gewährleisten, die in mehreren lokalen Caches gespeichert sind.2 Caches sind kleine, schnelle Speicher, die nahe an den Prozessorkernen liegen und dazu dienen, Zugriffszeiten auf häufig verwendete Daten zu verkürzen.5 In Systemen, in denen mehrere Prozessoren oder Kerne auf einen gemeinsamen Hauptspeicher zugreifen und dabei jeweils eigene Caches verwenden, ist die Aufrechterhaltung der Datenkonsistenz zwischen diesen Caches eine zentrale Herausforderung.1 Cache-Kohärenzprotokolle definieren die Regeln und Mechanismen, nach denen diese Konsistenz sichergestellt wird.

**1.2. Das fundamentale Problem: Dateninkonsistenz**

Die Kernherausforderung, die Cache-Kohärenzprotokolle adressieren, ist die potenzielle Dateninkonsistenz, die entsteht, wenn mehrere Prozessoren Kopien derselben Daten aus dem Hauptspeicher in ihren lokalen Caches halten und diese unabhängig voneinander modifizieren können.1 Wenn beispielsweise Prozessor A einen Datenwert in seinem Cache ändert, muss sichergestellt werden, dass Prozessor B, der möglicherweise eine Kopie desselben Datenwerts in seinem Cache hält, nicht mit einer veralteten Version weiterarbeitet.1 Ohne einen Mechanismus zur Synchronisation dieser Cache-Inhalte könnten Prozessoren inkonsistente Sichten auf die Daten haben („stale data“), was zu fehlerhaften Berechnungen, unvorhersehbarem Programmverhalten und potenziellen Systemabstürzen führen kann.2 Dieses Problem ist inhärent in Shared-Memory-Mehrprozessorsystemen, die zur Leistungssteigerung private Caches nutzen.1 Die Notwendigkeit, diese Inkonsistenzen zu vermeiden, treibt die Entwicklung und Implementierung von Kohärenzprotokollen an.

**1.3. Geltungsbereich und Kontext**

Während der Begriff „Kohärenz“ auch in anderen wissenschaftlichen Disziplinen eine Rolle spielt, etwa in der Physik zur Beschreibung fester Phasenbeziehungen zwischen Wellen oder in der Signalverarbeitung zur Quantifizierung der Korrelation zwischen Signalen 10, konzentriert sich dieser Bericht auf seine spezifische und kritische Anwendung in Computersystemen, nämlich die Cache-Kohärenz. In diesem Kontext bezieht sich „Kohärenz“ auf die Einheitlichkeit und Konsistenz von Daten über mehrere Caches hinweg.2 Der Begriff „Protokoll“ bezeichnet hierbei ein festes Regelwerk, das die Kommunikation und die Zustandsverwaltung zwischen den beteiligten Systemkomponenten – Caches, Hauptspeicher und dem Verbindungssystem (Interconnect) – steuert, um diese Einheitlichkeit zu gewährleisten.2

**1.4. Bedeutung und Zielsetzung**

Cache-Kohärenzprotokolle spielen eine entscheidende Rolle für die korrekte Funktion und die Leistungsfähigkeit moderner Multi-Core-Prozessoren und Mehrprozessorsysteme.1 Sie sind fundamental, um parallele Verarbeitung auf Basis eines gemeinsamen Speicherbereichs (Shared Memory) effizient und fehlerfrei zu gestalten.1 Ohne sie wäre das weit verbreitete Shared-Memory-Programmiermodell auf solcher Hardware praktisch nicht umsetzbar, da die Illusion eines einzigen, konsistenten Speicherraums für alle Prozessoren verloren ginge.16 Cache-Kohärenz ist somit nicht nur eine Fehlerkorrekturmaßnahme, sondern eine grundlegende Technologie, die das dominante Paradigma der parallelen Programmierung auf moderner Hardware erst ermöglicht. Das Ziel dieses Berichts ist es, eine umfassende technische Analyse von Cache-Kohärenzprotokollen zu liefern, die ihre Definition, die zugrundeliegenden Prinzipien, gängige Implementierungen, Vergleiche mit verwandten Konzepten und aktuelle Entwicklungstrends abdeckt.

**2. Das Konzept der Kohärenz in verschiedenen Disziplinen**

**2.1. Kohärenz in der Physik (Optik, Quantenmechanik)**

In der Physik, insbesondere in der Optik, beschreibt Kohärenz eine feste Phasenbeziehung zwischen Wellen gleicher Frequenz.10 Zwei Lichtstrahlen gelten als kohärent, wenn die Phasendifferenz zwischen ihren Wellen konstant ist. Diese Eigenschaft ist die Voraussetzung für die Entstehung stabiler Interferenzmuster, wie sie beispielsweise im Youngschen Doppelspaltexperiment beobachtet werden.10 Man unterscheidet zwischen zeitlicher Kohärenz, die die Korrelation der Phase einer Welle mit sich selbst zu verschiedenen Zeitpunkten beschreibt und mit der Monochromatizität (Farbreinheit) der Quelle zusammenhängt, und räumlicher Kohärenz, die die Korrelation der Phase über verschiedene Punkte im Raum beschreibt.11 Laserlicht ist ein Beispiel für hoch kohärentes Licht, bei dem die emittierten Photonen eine feste Phasenbeziehung zueinander aufweisen.10

In der Quantenmechanik bezieht sich Kohärenz auf die Fähigkeit von Quantenzuständen (beschrieben durch Wellenfunktionen), stabile Phasenbeziehungen aufrechtzuerhalten.20 Diese quantenmechanische Kohärenz ist die Grundlage für Phänomene wie die Superposition (Überlagerung) von Zuständen, bei der ein Quantenobjekt gleichzeitig in mehreren Zuständen existieren kann, und die Quanteninterferenz.18 Quantenkohärenz ist jedoch fragil und geht durch Wechselwirkung mit der Umgebung oder durch Messung verloren – ein Prozess, der als Dekohärenz bezeichnet wird.20 In beiden physikalischen Kontexten bezeichnet Kohärenz also eine stabile Phasenbeziehung, die vorhersagbare Interaktionen (Interferenz) ermöglicht.

**2.2. Kohärenz in der Signalverarbeitung**

In der Signalverarbeitung ist Kohärenz ein statistisches Maß, das die lineare Korrelation oder den Zusammenhang zwischen zwei Signalen als Funktion der Frequenz quantifiziert.12 Die Kohärenzfunktion, oft als Cxy​(f) oder γxy2​(f) bezeichnet, wird typischerweise aus den Leistungsdichtespektren (PSD) der Einzelsignale (Gxx​(f), Gyy​(f)) und dem Kreuzleistungsdichtespektrum (CSD) zwischen den Signalen (Gxy​(f)) berechnet:

Cxy​(f)=Gxx​(f)Gyy​(f)∣Gxy​(f)∣2​

.12 Der Wert der Kohärenzfunktion liegt zwischen 0 und 1.11 Ein Wert von 1 bei einer bestimmten Frequenz f bedeutet, dass die beiden Signale bei dieser Frequenz perfekt linear korreliert sind; das Ausgangssignal y(t) kann bei dieser Frequenz vollständig durch eine lineare Transformation des Eingangssignals x(t) erklärt werden.12 Ein Wert von 0 bedeutet, dass die Signale bei dieser Frequenz völlig unkorreliert sind.12 Werte dazwischen geben den Anteil der Leistung im Ausgangssignal an, der linear durch das Eingangssignal bei dieser Frequenz erklärt werden kann.12 Abweichungen von 1 können auf Rauschen in den Signalen, nichtlineare Zusammenhänge oder zusätzliche, unberücksichtigte Eingänge hinweisen.12 Kohärenz wird hier also verwendet, um die Stärke und Linearität eines statistischen Zusammenhangs zwischen Signalen frequenzabhängig zu bewerten.

**2.3. Cache-Kohärenz in der Informatik**

In der Informatik, speziell in der Computerarchitektur, bezeichnet Cache-Kohärenz die Sicherstellung der Einheitlichkeit (Uniformity) von gemeinsam genutzten Daten (Shared Data), die in mehreren lokalen Caches gespeichert sind.1 Das Ziel ist es, dass alle Prozessoren zu jeder Zeit eine konsistente Sicht auf die Daten im Speicher haben.1 Dies wird oft über das Konzept der "kohärenten Speichersicht" definiert: Eine Leseoperation eines Prozessors P1 auf eine Speicheradresse X, die auf eine Schreiboperation eines anderen Prozessors P2 auf dieselbe Adresse X folgt (wobei keine anderen Schreiboperationen auf X dazwischen liegen und die Operationen ausreichend zeitlich getrennt sind), muss immer den von P2 geschriebenen Wert zurückgeben.2 Dies erfordert, dass Schreiboperationen auf dieselbe Speicherstelle effektiv serialisiert werden und ihre Auswirkungen zeitnah im gesamten System propagiert werden.2

Das zugrundeliegende Problem ist die Inkonsistenz, die entsteht, wenn ein Prozessor Daten in seinem Cache modifiziert, während andere Prozessoren noch veraltete Kopien dieser Daten in ihren Caches halten.1 Dies kann zu "stale reads" (Lesen veralteter Werte) oder "lost writes" (Überschreiben von Änderungen, die nie von anderen gesehen wurden) führen.8 Cache-Kohärenzprotokolle sind daher unerlässlich für die korrekte Ausführung paralleler Programme auf Shared-Memory-Systemen.1 Sie ermöglichen nicht nur die Korrektheit, sondern auch die Leistung, indem sie die Verwendung schneller lokaler Caches erlauben, während sie gleichzeitig die Konsistenz gewährleisten.1 Die "Zeitnähe" (timeliness), mit der Änderungen propagiert werden 2, ist dabei ein wichtiger Aspekt. Protokolle müssen nicht nur die Konsistenz *irgendwann* herstellen, sondern dies auch effizient genug tun, um die Leistungsvorteile des Cachings nicht zunichte zu machen. Diese Balance zwischen Korrektheit und Leistung ist ein zentrales Thema im Design von Kohärenzprotokollen, was sich in der Vielfalt der Ansätze und Optimierungen widerspiegelt.2 Die Bedeutung von Cache-Kohärenz ist besonders hoch in Echtzeitsystemen, wo die zeitgerechte und korrekte Verarbeitung von Daten kritisch ist.1

**3. Die Rolle von Protokollen in technischen Systemen**

**3.1. Allgemeine Funktion von Protokollen**

Ein Protokoll im technischen Sinne ist eine formale Sammlung von Regeln, Prozeduren und Datenformaten, die die Kommunikation und Interaktion zwischen verschiedenen Entitäten oder Komponenten innerhalb eines Systems regeln. Ähnlich wie Netzwerkprotokolle 14 definieren sie, wie Nachrichten ausgetauscht werden, welche Aktionen bei bestimmten Ereignissen ausgeführt werden und wie Zustände verwaltet werden, um ein geordnetes, vorhersagbares und koordiniertes Verhalten des Gesamtsystems sicherzustellen. Sie sind essenziell für das Funktionieren komplexer, verteilter Systeme, in denen mehrere unabhängige Komponenten zusammenarbeiten müssen.

**3.2. Spezifische Funktion von Cache-Kohärenzprotokollen**

Cache-Kohärenzprotokolle sind spezialisierte Protokolle, die die Regeln für die Aufrechterhaltung der Datenkonsistenz in den Caches eines Mehrprozessorsystems festlegen. Ihre spezifischen Aufgaben umfassen:

  - **Zustandsverfolgung:** Sie definieren eine Reihe von Zuständen (z. B. Modified, Exclusive, Shared, Invalid im MESI-Protokoll), die jeder Cache-Zeile (der kleinsten Einheit der Datenübertragung zwischen Cache und Speicher) zugeordnet werden, um deren Status bezüglich Gültigkeit und Modifikation im Verhältnis zum Hauptspeicher und anderen Caches zu verfolgen.1
  - **Reaktion auf lokale Operationen:** Sie legen fest, wie ein Cache auf Lese- (PrRead) und Schreibanforderungen (PrWrite) des lokalen Prozessors reagieren muss, abhängig vom aktuellen Zustand der betroffenen Cache-Zeile.31 Dies kann beinhalten, Daten direkt bereitzustellen, eine Leseanforderung an den Bus/Interconnect zu senden oder eine Schreibberechtigung anzufordern.
  - **Kommunikationsdefinition:** Sie definieren die spezifischen Nachrichten oder Transaktionen (z. B. BusRd, BusRdX, Invalidate, Flush/Writeback), die über den Systembus oder das Interconnect-Netzwerk ausgetauscht werden, um Daten anzufordern, Änderungen zu signalisieren oder Cache-Zustände zu synchronisieren.2
  - **Reaktion auf entfernte Operationen:** Sie schreiben vor, wie Cache-Controller auf beobachtete (gesnoopte) Transaktionen anderer Prozessoren oder auf Nachrichten von einer zentralen Directory reagieren müssen, um ihren lokalen Zustand anzupassen und die systemweite Konsistenz aufrechtzuerhalten.2
  - **Implementierung der Kohärenz-Invarianten:** Letztendlich implementieren diese Regeln die gewählte Definition von Kohärenz, indem sie sicherstellen, dass bestimmte Invarianten, wie die Single-Writer, Multiple-Reader (SWMR)-Invariante (nur ein Prozessor darf gleichzeitig schreiben, aber mehrere dürfen lesen), eingehalten werden.17

Cache-Kohärenzprotokolle agieren im Grunde als verteilte Algorithmen, die über mehrere unabhängige Cache-Controller und Speicher-Controller hinweg operieren.1 Sie müssen mit Nebenläufigkeit (Concurrency), potenziellen Wettlaufsituationen (Race Conditions) und in manchen Fällen auch mit Fehlern umgehen (obwohl Fehlerbehandlung wie in 14 oft als separate Schicht betrachtet wird), um eine globale Konsistenzeigenschaft aufrechtzuerhalten. Die Komplexität dieser Protokolle ergibt sich maßgeblich aus dieser verteilten Natur und der Notwendigkeit, Konsistenz trotz paralleler Zugriffe zu garantieren. Aus diesem Grund sind formale Verifikationsmethoden, wie Model Checking oder Theorem Proving, oft unerlässlich, um die Korrektheit (Safety- und Liveness-Eigenschaften) dieser komplexen verteilten Interaktionen nachzuweisen.15

**4. Fundamentale Mechanismen zur Aufrechterhaltung der Cache-Kohärenz**

Zur Implementierung der Cache-Kohärenz haben sich zwei grundlegende Mechanismen etabliert: Snooping-basierte und Verzeichnis-basierte Protokolle.

**4.1. Snooping-basierte Protokolle**

  - **Mechanismus:** Bei diesem Ansatz überwacht („snoopt“) jeder Cache-Controller kontinuierlich einen gemeinsamen Bus oder ein Interconnect-Medium auf Speicherzugriffe, die von anderen Prozessoren oder I/O-Geräten initiiert werden.2 Der Bus dient als Broadcast-Medium, über das alle relevanten Transaktionen für alle Caches sichtbar gemacht werden.
  - **Operation:** Wenn ein Cache-Controller eine Transaktion auf dem Bus erkennt, die eine Speicheradresse betrifft, die er selbst gecacht hat, prüft er den Zustand seiner lokalen Kopie und reagiert gemäß den Protokollregeln. Bei einem Schreibzugriff eines anderen Prozessors auf eine geteilte Cache-Zeile könnte ein Cache beispielsweise seine eigene Kopie invalidieren (Write-Invalidate-Protokoll) oder mit den neuen Daten aktualisieren (Write-Update-Protokoll).2 Gängige Protokolle wie MSI, MESI und MOESI werden oft in Snooping-basierten Systemen implementiert.1
  - **Vor- und Nachteile:** Snooping-Protokolle ermöglichen typischerweise schnelle Reaktionen auf Kohärenzereignisse, da alle relevanten Informationen direkt über den Bus ausgetauscht werden und keine zentrale Instanz involviert ist, vorausgesetzt, die Busbandbreite ist ausreichend.2 Ihr Hauptnachteil ist die begrenzte Skalierbarkeit. Da jede potenziell relevante Transaktion an alle Caches gesendet werden muss (Broadcast), steigt die erforderliche Busbandbreite mit der Anzahl der Prozessoren stark an und wird schnell zum Engpass.2 Daher eignen sich reine Snooping-Ansätze meist nur für Systeme mit einer relativ geringen Anzahl von Prozessoren.

**4.2. Verzeichnis-basierte Protokolle (Directory-based)**

  - **Mechanismus:** Im Gegensatz zum Snooping verwenden verzeichnisbasierte Protokolle eine zentrale oder verteilte Datenstruktur, das „Directory“ (Verzeichnis), um den globalen Zustand der Cache-Zeilen zu verfolgen.2 Für jeden Speicherblock (oder jede Cache-Zeile) speichert das Directory Informationen darüber, welche Prozessoren eine Kopie halten und in welchem Zustand sich diese Kopien befinden (z. B. ungültig, geteilt, exklusiv/modifiziert).4
  - **Operation:** Wenn ein Prozessor auf einen Speicherblock zugreifen möchte (Lesen oder Schreiben), sendet sein Cache eine Anfrage an das Directory (typischerweise an den Teil des Directories, der für die betreffende Speicheradresse zuständig ist, oft am „Home Node“ des Speicherblocks angesiedelt). Das Directory prüft den aktuellen Zustand und koordiniert die notwendigen Aktionen. Anstatt eine Nachricht an alle Caches zu senden (Broadcast), sendet das Directory gezielte Nachrichten (Punkt-zu-Punkt) nur an die Caches, die tatsächlich eine Kopie des Blocks halten, um beispielsweise Invalidierungen durchzuführen oder Daten weiterzuleiten.2 Verzeichnisbasierte Protokolle sind aufgrund ihrer besseren Skalierbarkeit die bevorzugte Wahl für große Mehrprozessorsysteme mit vielen Kernen oder Sockets.29
  - **Vor- und Nachteile:** Der Hauptvorteil ist die Skalierbarkeit, da die Kommunikation gezielt erfolgt und die Bandbreitenanforderungen weniger stark mit der Prozessorzahl wachsen als bei Snooping.2 Ein potenzieller Nachteil ist die höhere Latenz, da Zugriffe oft einen zusätzlichen Kommunikationsschritt über das Directory erfordern (Indirektion).2 Zudem stellt der Speicherbedarf für das Directory selbst eine Herausforderung dar, da für jeden Speicherblock Kohärenzinformationen gespeichert werden müssen, was bei großen Speichersystemen erheblichen Overhead bedeuten kann.7

Die strikte Trennung zwischen Snooping und Directory weicht in modernen Systemen zunehmend auf. Insbesondere in großen, hierarchisch aufgebauten Systemen (z. B. Multi-Socket-Server) kommen oft hybride Ansätze zum Einsatz. Beispielsweise kann Snooping innerhalb eines einzelnen Chips oder Sockets verwendet werden, wo die Latenz kritischer ist und die Anzahl der Kerne begrenzt ist, während ein Verzeichnisprotokoll die Kohärenz *zwischen* den Sockets verwaltet, wo Skalierbarkeit wichtiger ist.17 Optimierungen wie "Snoop-Filter" 41 oder "Directory Caches" versuchen ebenfalls, Elemente beider Ansätze zu kombinieren, um eine bessere Balance zwischen Leistung und Skalierbarkeit in komplexen Speicherhierarchien zu erreichen. Diese Entwicklung zeigt, dass die Wahl des Kohärenzmechanismus stark von der Systemarchitektur und den spezifischen Anforderungen abhängt und sich ständig weiterentwickelt.

**5. Analyse wichtiger Cache-Kohärenzprotokolle**

Viele der am weitesten verbreiteten Cache-Kohärenzprotokolle basieren auf der Zuweisung von Zuständen zu Cache-Zeilen und verwenden Invalidierungsnachrichten, um sicherzustellen, dass zu jedem Zeitpunkt höchstens ein Prozessor Schreibzugriff auf eine bestimmte Cache-Zeile hat (Write-Invalidate-Ansatz).

**5.1. Zustandsbasierte Invalidierungsprotokolle als Grundlage**

Protokolle wie MSI, MESI und MOESI bilden eine Familie von zustandsbasierten Invalidierungsprotokollen, die auf ähnlichen Prinzipien beruhen. Sie definieren einen Satz von Zuständen für jede Cache-Zeile und Regeln für Übergänge zwischen diesen Zuständen basierend auf lokalen Prozessoroperationen und beobachteten Bustransaktionen.

**5.2. Vertiefung: Das MESI-Protokoll**

  - **Einführung:** Das MESI-Protokoll (Modified, Exclusive, Shared, Invalid) ist ein fundamentales und weit verbreitetes zustandsbasiertes Invalidierungsprotokoll.1 Es optimiert den einfachen MSI-Ansatz durch die Einführung eines "Exclusive"-Zustands.
  - **Zustände:** Die vier Zustände im MESI-Protokoll sind 4:

<!-- end list -->

  - **Modified (M):** Die Cache-Zeile wurde lokal modifiziert ("dirty"). Sie ist die einzige gültige Kopie im System, und der Wert im Hauptspeicher ist veraltet. Der Cache ist verantwortlich für das Zurückschreiben der Daten in den Hauptspeicher bei Verdrängung oder bei einer Leseanforderung durch einen anderen Prozessor.
  - **Exclusive (E):** Die Cache-Zeile ist die einzige Kopie im System, aber sie ist "clean", d. h., der Wert stimmt mit dem Hauptspeicher überein. Ein lokaler Schreibzugriff kann ohne Bustransaktion erfolgen, wobei der Zustand zu M wechselt. Bei einem Lesezugriff durch einen anderen Prozessor wechselt der Zustand zu S.
  - **Shared (S):** Es können mehrere Kopien der Cache-Zeile in verschiedenen Caches existieren. Alle Kopien sind "clean" und konsistent mit dem Hauptspeicher. Ein lokaler Schreibzugriff erfordert eine Bustransaktion (BusRdX), um alle anderen Kopien zu invalidieren, bevor der Zustand zu M wechselt.
  - **Invalid (I):** Die Cache-Zeile enthält keine gültigen Daten. Jeder Zugriff (Lesen oder Schreiben) erfordert das Laden der Daten vom Hauptspeicher oder einem anderen Cache über eine Bustransaktion.

<!-- end list -->

  - **Zustandsübergänge und Bustransaktionen:** Die Dynamik des MESI-Protokolls wird durch die Übergänge zwischen diesen Zuständen bestimmt, die durch lokale Prozessoraktionen (PrRead, PrWrite) und durch auf dem Bus beobachtete (gesnoopte) Transaktionen anderer Prozessoren (BusRd, BusRdX) ausgelöst werden.31 Wichtige Bustransaktionen sind 31:

<!-- end list -->

  - **Bus Read (BusRd):** Wird von einem Cache gesendet, der Daten lesen möchte, die sich im Zustand I befinden. Andere Caches snoopen. Wenn ein Cache die Daten im Zustand M hält, muss er die Daten auf den Bus legen (Flush) und wechselt typischerweise zu S. Wenn kein Cache M hat, liefert der Hauptspeicher die Daten. Der anfordernde Cache geht in den Zustand E, wenn kein anderer Cache die Daten teilt (kein Shared-Signal), sonst in den Zustand S.
  - **Bus Read Exclusive (BusRdX):** Wird von einem Cache gesendet, der Daten schreiben möchte und sich im Zustand I oder S befindet. Alle anderen Caches, die die Daten im Zustand M, E oder S halten, müssen ihre Kopie invalidieren (Zustand I). Wenn ein Cache die Daten im Zustand M hatte, muss er sie vorher auf den Bus schreiben (Writeback/Flush). Der anfordernde Cache geht in den Zustand M.
  - **Flush / Writeback:** Eine Aktion, bei der ein Cache im Zustand M die modifizierten Daten auf den Bus legt, entweder als Antwort auf einen BusRd oder BusRdX eines anderen Caches oder bei Verdrängung der Cache-Zeile.
  - **Invalidate Signal:** Implizit Teil von BusRdX; signalisiert anderen Caches, ihre Kopien zu invalidieren.

Die folgende Tabelle fasst die wichtigsten Zustandsübergänge im MESI-Protokoll zusammen:

\\begin{table}\[h\!\]

\\centering

\\caption{MESI-Zustandsübergangstabelle (vereinfacht)}

\\label{tab:mesi}

\\begin{tabular}{|l|l|l|l|l|}

\\hline

\\textbf{Aktueller} & \\multicolumn{4}{c|}{\\textbf{Ereignis}} \\ \\cline{2-5}

\\textbf{Zustand} & \\textbf{Lokales Lesen} & \\textbf{Lokales Schreiben} & \\textbf{BusRd Snoop} & \\textbf{BusRdX Snoop} \\ \\hline

\\textbf{Modified (M)} & M / - & M / - & S / Flush Data & I / Flush Data \\ \\hline

\\textbf{Exclusive (E)} & E / - & M / - & S / - & I / - \\ \\hline

\\textbf{Shared (S)} & S / - & M / BusRdX & S / - & I / - \\ \\hline

\\textbf{Invalid (I)} & E oder S / BusRd & M / BusRdX & I / - & I / - \\ \\hline

\\end{tabular}

\\textit{Anmerkung: '/' trennt den nächsten Zustand von der ausgelösten Busaktion. '-' bedeutet keine Busaktion. Der Übergang von I nach einem lokalen Lesen hängt davon ab, ob andere Caches die Daten teilen.}

\\end{table}

  - **Tabelle/Abbildung: MESI-Zustandsübergangsdiagramm/Tabelle.** Die Tabelle \\ref{tab:mesi} ist entscheidend für das Verständnis der Protokolldynamik. Sie visualisiert, wie jeder Zustand auf verschiedene Ereignisse reagiert und welche Aktionen daraus resultieren. Dies erleichtert das Verständnis der Kernlogik, wie MESI die Konsistenz (insbesondere die Single-Writer-Invariante) aufrechterhält, indem es die komplexen Interaktionen 31 zusammenfasst und eine klare Referenz bietet.

**5.3. Gängige Variationen**

  - **MSI:** Eine vereinfachte Version ohne den Exclusive-Zustand.1 Ein Lesezugriff führt immer in den Shared-Zustand. Das bedeutet, dass selbst wenn ein Cache die einzige Kopie hält, vor einem Schreibzugriff immer eine BusRdX-Transaktion (Invalidierung) erforderlich ist. Dies ist ineffizient für Daten, die primär von einem Prozessor gelesen und geschrieben werden.8
  - **MOSI:** Erweitert MSI um den Owned-Zustand.4 Eine Cache-Zeile im Owned-Zustand ist modifiziert ("dirty"), aber andere Caches dürfen Kopien im Shared-Zustand halten. Der "Owner" ist dafür verantwortlich, Leseanfragen anderer Caches direkt zu bedienen, was die Belastung des Hauptspeichers reduzieren kann.4
  - **MOESI:** Kombiniert die Vorteile von MESI (Exclusive-Zustand für effiziente private Schreibzugriffe) mit dem Owned-Zustand von MOSI (effiziente Bedienung von Leseanfragen bei geteilten, modifizierten Daten).1 Gilt als umfassenderes, aber auch komplexeres Protokoll.4
  - **MESIF:** Eine Erweiterung von MESI, die in einigen Intel-Protokollen verwendet wird.41 Fügt einen "Forward" (F)-Zustand hinzu. Wenn mehrere Caches eine Zeile im Shared-Zustand halten, wird eine davon als F-Zustand markiert. Diese ist dann dafür verantwortlich, die Daten bei einer weiteren Leseanforderung weiterzuleiten. Dies reduziert den Datenverkehr zum Hauptspeicher im Vergleich dazu, dass der Hauptspeicher oder mehrere Shared-Caches antworten müssten.

**5.4. Überblick über weitere bemerkenswerte Protokolle**

Die Vielfalt der Kohärenzprotokolle geht weit über die MESI-Familie hinaus und spiegelt die unterschiedlichen Optimierungsziele und Herausforderungen wider:

  - **Token Coherence:** Entkoppelt Korrektheitsmechanismen (Safety, Liveness) von Leistungsoptimierungen durch die Verwendung von "Tokens", die Zugriffsrechte repräsentieren.16 Ziel ist verbesserte Leistung und Verifizierbarkeit.
  - **Delta Coherence:** Nutzt logische Zeitstempel und "Isotach-Garantien" (gleiche Nachrichtenlaufzeit in logischer Zeit), um Zugriffe zu koordinieren und hohe Parallelität bei gleichzeitiger Gewährleistung sequenzieller Konsistenz zu ermöglichen.44
  - **Kontext-sensitive / Sharing-Pattern-Aware Protokolle:** Optimieren den Kohärenzverkehr basierend auf dem beobachteten Kommunikationsmuster der Anwendung (z. B. Produzent-Konsument-Muster), etwa durch dynamische Verlagerung der Directory-Verantwortung (Delegation) zum Produzenten-Knoten.29
  - **Interconnect-Aware Protokolle:** Nutzen Kenntnisse über heterogene Verbindungsnetzwerke (unterschiedliche Latenz, Bandbreite, Energie pro Übertragung), um kritische Kohärenznachrichten auf schnelle Pfade und weniger kritische auf energieeffiziente Pfade zu legen.29
  - **WiDir (Wireless Directory):** Erweitert ein drahtgebundenes Verzeichnisprotokoll um drahtlose Transaktionen (über On-Chip-Wireless-Netzwerke), um häufiges Lesen und Schreiben durch mehrere Kerne (Frequent Read-Write Sharing) effizienter zu unterstützen.38
  - **POPS (Protocol Optimization for Private and Shared data):** Optimiert Zugriffe auf private und geteilte Daten durch Entkopplung von Daten und Metadaten und ermöglicht die Delegation der Kohärenzverantwortung an L1-Caches oder lokale Last-Level-Cache-Slices.45
  - **Rainbow:** Ein komponierbares Protokoll für Multi-Chip- oder Multi-Socket-Systeme, das Token-Zählung und hybride Directory/Filter-Strukturen (D|F-LLC, D|F-MEM) verwendet, um Komplexität, Skalierbarkeit und Leistung auszubalancieren.39
  - **RCP (Reversible Coherence Protocol):** Erweitert bestehende Kohärenzprotokolle (wie MESI) um spekulative Zustände und Rücksetzmechanismen.47 Ziel ist es, spekulative Speicherzugriffe auf der Kohärenzebene unsichtbar oder reversibel zu machen, um transiente Ausführungsangriffe (wie Spectre) mit geringem Overhead abzuwehren.50
  - **Ghostwriter:** Nutzt Konzepte des Approximate Computing und Wertähnlichkeit in fehlertoleranten Anwendungen, um Kohärenzverkehr und Cache-Misses zu reduzieren, indem für approximierbare Daten eine begrenzte, kontrollierte Inkohärenz zugelassen wird.28
  - **SELCC (Shared-Exclusive Latch Cache Coherence):** Ein Protokoll speziell für disaggregierte Speichersysteme, das RDMA-Atomoperationen und eingebettete Metadaten nutzt, um Kohärenz ohne signifikante Rechenlast auf der entfernten Speicherseite aufrechtzuerhalten.51

Diese Bandbreite an Protokollen verdeutlicht, dass Cache-Kohärenz kein abgeschlossenes Problem mit einer einzigen Universallösung ist. Das Design von Kohärenzprotokollen stellt einen komplexen Kompromiss dar, der zwischen Leistung (Latenz, Bandbreite), Skalierbarkeit (Anzahl der Kerne, Interconnect-Topologie), Komplexität (Verifikation, Implementierungskosten), Energieverbrauch und zunehmend auch Sicherheitsaspekten abwägen muss. Die Evolution von einfachen Protokollen wie MSI/MESI hin zu spezialisierten Lösungen für Skalierbarkeit 29, Sicherheit 47, neue Architekturen 38 oder neue Anwendungsdomänen 28 zeigt, dass der Designraum riesig ist und sich ständig weiterentwickelt, da sich die Anforderungen und die zugrundeliegende Technologie ändern.

**6. Cache-Kohärenz im Verhältnis zu anderen Konzepten**

**6.1. Cache-Kohärenz vs. Speicherkonsistenzmodelle**

  - **Cache-Kohärenz:** Bezieht sich auf die Konsistenz der Daten für eine *einzelne* Speicheradresse über alle Caches hinweg. Sie stellt sicher, dass Schreiboperationen auf dieselbe Adresse irgendwann für alle Prozessoren sichtbar werden und dass diese Schreiboperationen in einer gewissen sequenziellen Reihenfolge erscheinen.1 Sie garantiert eine einheitliche Sicht auf den Wert einer Speicherzelle.
  - **Speicherkonsistenzmodell:** Definiert die Regeln für die zulässige Reihenfolge von Lese- und Schreiboperationen auf *verschiedene* Speicheradressen, wie sie von den Prozessoren im System beobachtet werden können.1 Ein bekanntes Beispiel ist die Sequenzielle Konsistenz (Sequential Consistency, SC), die fordert, dass das Ergebnis jeder Ausführung so ist, als ob die Operationen aller Prozessoren in einer einzigen, globalen sequenziellen Reihenfolge ausgeführt wurden, wobei die Programmreihenfolge jedes einzelnen Prozessors erhalten bleibt.2
  - **Beziehung:** Cache-Kohärenz ist eine notwendige, aber nicht hinreichende Bedingung für Speicherkonsistenz (insbesondere für strengere Modelle wie SC).1 Ein System kann kohärent sein (jeder sieht den letzten Schreibwert für Adresse X), aber nicht sequenziell konsistent, wenn verschiedene Prozessoren unterschiedliche Reihenfolgen für Operationen auf Adressen X und Y beobachten. Kohärenz fokussiert auf die Datenwerte einer Adresse, während Konsistenz die globale Reihenfolge von Operationen über Adressen hinweg regelt. Viele Kohärenzprotokolle sind jedoch so konzipiert, dass sie zusammen mit der Prozessorarchitektur ein bestimmtes Konsistenzmodell, oft SC oder ein relaxierteres Modell, implementieren.44

**6.2. Cache-Kohärenzprotokolle vs. Synchronisationsprimitive**

  - **Cache-Kohärenz (Hardware-Grundlage):** Operiert typischerweise transparent auf der Hardware-Ebene und verwaltet automatisch die Datenkonsistenz für *alle* Zugriffe auf gemeinsam genutzten Speicher.2 Sie stellt die grundlegende Garantie dar, dass Speicheransichten (eventuell mit Verzögerung) konsistent werden.
  - **Synchronisationsprimitive (Software/Hardware-Koordination):** Sind explizite Konstrukte (wie Locks/Mutexes, Semaphore, Barrieren) oder atomare Hardware-Instruktionen (wie Compare-and-Swap (CAS), Test-and-Set, Load-Linked/Store-Conditional (LL/SC)), die von Programmierern verwendet werden, um den Zugriff auf kritische Abschnitte (Codebereiche, die auf geteilte Ressourcen zugreifen) zu koordinieren, Race Conditions zu verhindern und die Ausführungsreihenfolge paralleler Threads oder Prozesse zu steuern.8
  - **Zusammenspiel:** Synchronisationsprimitive sind auf die zugrundeliegende Cache-Kohärenz angewiesen, um korrekt zu funktionieren.8 Wenn ein Prozessor beispielsweise versucht, eine Sperre (Lock) mittels einer atomaren Operation (z. B. CAS auf eine Lock-Variable) zu erwerben, sorgt das Kohärenzprotokoll dafür, dass dieser Prozessor exklusiven Zugriff auf die Cache-Zeile erhält, die die Lock-Variable enthält, und dass die Änderung (z. B. das Setzen des Locks) für andere Prozessoren sichtbar wird.8 Atomare Operationen selbst lösen Kohärenzaktionen aus. Darüber hinaus interagieren Speicherbarrieren (Memory Fences/Barriers), die oft zusammen mit Synchronisationsprimitiven verwendet werden, mit dem Speichersystem (einschließlich Caches und Kohärenzprotokoll), um sicherzustellen, dass Speicheroperationen in einer bestimmten Reihenfolge sichtbar werden, die über die Garantien der reinen Kohärenz hinausgeht.8 In einigen Architekturen kann die Hardware-Unterstützung für Synchronisation sogar direkt Kohärenzmechanismen nutzen, z. B. Verzeichnisinformationen zur Implementierung verteilter Locks.54

Die Leistung von Synchronisationsprimitiven hängt entscheidend von der Effizienz des zugrundeliegenden Cache-Kohärenzprotokolls ab. Operationen wie der Erwerb einer Sperre (Lock Acquisition) beinhalten oft atomare Lese-Modifizier-Schreib-Operationen auf eine gemeinsam genutzte Variable. Die Latenz dieser Operationen wird direkt davon beeinflusst, wie schnell das Kohärenzprotokoll exklusiven Zugriff gewähren, andere Kopien invalidieren und die Aktualisierung propagieren kann.40 Hohe Latenzen im Kohärenzprotokoll, beispielsweise durch hohe Contention (Konflikte um den Zugriff) oder langsame Kommunikation zwischen Sockets in NUMA-Systemen, führen direkt zu einer schlechten Leistung der Synchronisation und begrenzen die Skalierbarkeit paralleler Anwendungen.40 Eine ineffiziente Kohärenz manifestiert sich also unmittelbar in ineffizienter Synchronisation; ihre Leistungsaspekte sind eng miteinander verknüpft.

**7. Herausforderungen, Optimierung und zukünftige Trends**

Die Entwicklung von Cache-Kohärenzprotokollen steht vor anhaltenden Herausforderungen, treibt aber auch kontinuierliche Optimierungen und neue Forschungsrichtungen voran.

**7.1. Skalierbarkeitsengpässe**

  - **Verkehrsaufkommen (Traffic):** Mit steigender Anzahl von Prozessorkernen nimmt der Kommunikationsaufwand für die Kohärenzhaltung (Invalidierungs-/Update-Nachrichten, Verzeichnisanfragen und -antworten) zu. Dieser Kohärenzverkehr belastet das Interconnect-Netzwerk und kann dessen Bandbreite limitieren.2
  - **Speicheroverhead:** Insbesondere bei verzeichnisbasierten Protokollen wächst der Speicherbedarf für das Verzeichnis selbst mit der Größe des Hauptspeichers und potenziell mit der Anzahl der Kerne, was einen signifikanten Hardware-Overhead darstellen kann.17
  - **Latenz:** In großen Systemen, insbesondere solchen mit Non-Uniform Memory Access (NUMA)-Architekturen, steigen die Latenzen für Speicherzugriffe und Kohärenzoperationen, vor allem bei Kommunikation über Chip- oder Socket-Grenzen hinweg. Dies beeinträchtigt nicht nur den direkten Datenzugriff, sondern verlangsamt auch Synchronisationsoperationen erheblich.14

**7.2. Techniken zur Leistungsoptimierung**

Als Reaktion auf die Skalierungsherausforderungen wurden zahlreiche Optimierungstechniken entwickelt:

  - **Protokoll-Spezialisierung:** Der Trend geht zu Protokollen, die für spezifische Zugriffsmuster (z. B. Produzent-Konsument 29), Datentypen (privat vs. geteilt 45) oder Hardware-Gegebenheiten (drahtlose Interconnects 38, Multi-Chip-Module 39) optimiert sind.
  - **Delegation:** Mechanismen, bei denen die Verantwortung für die Kohärenzhaltung einer Cache-Zeile dynamisch an einen Knoten verlagert wird, der näher an den zugreifenden Kernen liegt (z. B. Delegation an den Produzenten-Knoten 29 oder an einen L1-Cache 45), um die Latenz und den Verkehr zu reduzieren.
  - **Filterung und Vorhersage:** Einsatz von Strukturen wie Bloom-Filtern (z. B. in Rainbow 46) oder Snoop-Filtern 41, um unnötigen Broadcast-Verkehr oder Verzeichniskommunikation zu vermeiden, indem approximative Informationen über den Cache-Status genutzt werden.
  - **Hardware-Unterstützung für Synchronisation:** Integration von Mechanismen zur Beschleunigung von Synchronisationsprimitiven direkt in die Kohärenz-Hardware, beispielsweise durch Nutzung von Verzeichnisinformationen für effiziente verteilte Locks.54

**7.3. Verifikation und Korrektheit**

Die zunehmende Komplexität moderner Kohärenzprotokolle macht deren Design und Verifikation extrem anspruchsvoll. Subtile Wettlaufsituationen (Race Conditions) zwischen nebenläufigen Kohärenztransaktionen können zu schwer auffindbaren Fehlern führen.16 Daher ist der Einsatz formaler Methoden unerlässlich geworden. Techniken wie Model Checking, Theorem Proving und spezialisierte Frameworks (z. B. Hemiola in Coq 32) werden verwendet, um die Korrektheit der Protokolle rigoros nachzuweisen, insbesondere hinsichtlich Safety-Eigenschaften (z. B. keine Inkonsistenzen) und Liveness-Eigenschaften (z. B. Zugriffsanfragen werden irgendwann bedient).15

**7.4. Sicherheitsimplikationen**

In den letzten Jahren hat sich gezeigt, dass die Interaktion zwischen spekulativer Ausführung (einer wichtigen Performance-Technik moderner Prozessoren) und dem Cache-Speichersystem gravierende Sicherheitslücken schaffen kann. Transiente Ausführungsangriffe (wie Spectre und Meltdown) nutzen aus, dass spekulativ ausgeführte Instruktionen, auch wenn sie später verworfen werden, beobachtbare Spuren im mikroarchitektonischen Zustand (z. B. im Cache) hinterlassen können. Diese Spuren können über Seitenkanäle ausgelesen werden, um sensible Daten zu lecken.49 Cache-Kohärenzprotokolle spielen hier eine Rolle, da sie den Zustand der Caches verwalten, der für diese Angriffe ausgenutzt wird. Als Reaktion darauf werden neue Kohärenzprotokolle wie RCP (Reversible Coherence Protocol) entwickelt.47 Diese zielen darauf ab, die Auswirkungen spekulativer Speicherzugriffe auf der Kohärenzebene reversibel oder unsichtbar zu machen, indem sie spekulative Zustände puffern und bei Bedarf zurückrollen (Purge) oder bestätigen (Merge). Solche Ansätze versprechen, Schutz vor diesen Angriffen zu bieten, idealerweise mit geringerem Leistungs-Overhead als rein softwarebasierte oder einfachere Hardware-Mitigationen.

**7.5. Aufkommende Paradigmen**

Die Forschung im Bereich Cache-Kohärenz passt sich kontinuierlich an neue Technologien und Anwendungsbereiche an:

  - **Approximative Kohärenz:** Für fehlertolerante Anwendungen (z. B. in maschinellem Lernen oder Multimedia) werden Protokolle wie Ghostwriter 28 erforscht, die bewusst eine begrenzte Inkohärenz zulassen, um Leistung und Energieeffizienz zu verbessern, indem sie die Ähnlichkeit von Werten ausnutzen und unnötigen Kohärenzverkehr vermeiden.
  - **Kohärenz für disaggregierten Speicher:** Mit dem Aufkommen von Architekturen, bei denen Speicher von den Rechenknoten physisch getrennt ist (Memory Disaggregation), entstehen neue Herausforderungen für die Kohärenzhaltung über potenziell langsamere Netzwerke und mit begrenzten Rechenressourcen auf der Speicherseite. Protokolle wie SELCC 51 adressieren dies durch Nutzung von Technologien wie RDMA und speziellen Metadatenstrukturen.
  - **Kohärenz mit neuartigen Interconnects:** Die Integration neuer Verbindungstechnologien wie drahtloser Netzwerke auf dem Chip (Wireless Network-on-Chip, WNoC) wird erforscht, um traditionelle drahtgebundene Interconnects für den Kohärenzverkehr zu ergänzen und Engpässe zu überwinden (z. B. WiDir 38).
  - **Kohärenz und Heterogenität:** Die Verwaltung der Kohärenz in Systemen mit unterschiedlichen Arten von Prozessorkernen (z. B. Performance- und Effizienz-Kerne) oder integrierten Beschleunigern (wie GPUs oder FPGAs), die möglicherweise eigene Cache-Hierarchien und Kohärenzanforderungen haben, stellt eine wachsende Herausforderung dar.14

Diese Entwicklungen deuten darauf hin, dass die Zukunft der Cache-Kohärenz in einer engeren Koppelung und einem gemeinsamen Design (Co-Design) mit anderen Systemkomponenten und der Software liegt. Während frühere Protokolle oft auf Transparenz abzielten 17, müssen zukünftige Lösungen zunehmend Aspekte wie die Interconnect-Topologie 29, Anwendungsmuster 29, Sicherheitsanforderungen 47, das Potenzial für Approximation 28 und sogar das Programmiermodell oder die Synchronisationsstrategie berücksichtigen. Ein isoliertes Design der Kohärenzschicht erscheint angesichts der Komplexität moderner Systeme und der vielfältigen Anforderungen nicht mehr ausreichend. Stattdessen ist ein ganzheitlicher Ansatz erforderlich, der die Kohärenz als integralen Bestandteil des Gesamtsystems betrachtet und optimiert.

**8. Schlussfolgerung**

**8.1. Zusammenfassung der Ergebnisse**

Die Analyse hat gezeigt, dass der Begriff „Kohärenz Protokoll“ im technischen Sprachgebrauch der Informatik äquivalent zu „Cache Coherence Protocol“ ist. Diese Protokolle sind unverzichtbare Mechanismen in modernen Mehrprozessor- und Multi-Core-Systemen, die das fundamentale Problem der Dateninkonsistenz lösen, welches durch die Verwendung privater Caches in einer Shared-Memory-Umgebung entsteht. Die Kernaufgabe besteht darin, eine einheitliche und konsistente Sicht auf gemeinsam genutzte Daten über alle Prozessoren hinweg zu gewährleisten. Die beiden grundlegenden Ansätze zur Implementierung sind Snooping-basierte Protokolle, die auf der Überwachung eines gemeinsamen Busses beruhen, und Verzeichnis-basierte Protokolle, die einen zentralen oder verteilten Informationsspeicher (Directory) nutzen, um den Zustand und die Verteilung von Cache-Zeilen zu verfolgen.

**8.2. Rekapitulation wichtiger Protokolle und Vergleiche**

Protokolle wie MESI stellen eine wichtige Basis dar und illustrieren die Kernprinzipien zustandsbasierter Invalidierungsprotokolle. Variationen wie MSI, MOESI und MESIF bieten unterschiedliche Kompromisse hinsichtlich Effizienz und Komplexität. Die darüber hinausgehende Vielfalt an Protokollen (z. B. Token Coherence, Delta Coherence, RCP, WiDir, Rainbow, Ghostwriter, SELCC) spiegelt die kontinuierliche Forschung und Entwicklung wider, die darauf abzielt, spezifische Herausforderungen in Bereichen wie Skalierbarkeit, Leistung unter bestimmten Zugriffsmustern, Sicherheit gegenüber neuen Angriffen oder Anpassung an neuartige Hardware-Architekturen (wie Multi-Chip-Module oder disaggregierten Speicher) zu adressieren. Es ist wichtig, Cache-Kohärenz (Gewährleistung der Datenkonsistenz für einzelne Adressen) von Speicherkonsistenzmodellen (Definition der globalen Reihenfolge von Speicheroperationen über Adressen hinweg) zu unterscheiden. Ebenso muss zwischen Cache-Kohärenzprotokollen (automatische Hardware-Grundlage) und Synchronisationsprimitiven (explizite Koordinationsmechanismen) differenziert werden, wobei letztere auf ersteren aufbauen und deren Leistung stark von der Effizienz der Kohärenzmechanismen abhängt.

**8.3. Abschließende Bemerkungen**

Cache-Kohärenz bleibt eine zentrale und kritische Technologie für die Realisierung von hochleistungsfähigem Parallel-Computing auf Basis des Shared-Memory-Modells. Obwohl die grundlegenden Prinzipien etabliert sind, befindet sich das Feld in ständiger Weiterentwicklung. Die Bewältigung der Herausforderungen in Bezug auf Skalierbarkeit (Verkehr, Latenz, Speicheroverhead), Leistung, Energieeffizienz, Verifikationskomplexität und Sicherheit erfordert fortlaufende Innovationen im Design von Kohärenzprotokollen. Zukünftige Entwicklungen werden wahrscheinlich durch ein engeres Co-Design mit anderen Systemschichten, die Anpassung an neue Hardware-Technologien und die Berücksichtigung spezifischer Anwendungsanforderungen geprägt sein. Die Forschung an Kohärenzprotokollen ist somit weiterhin ein aktives und relevantes Gebiet der Computerarchitektur.

#### **Referenzen**

1.  Cache-Kohärenz: Konzepte & Bedeutung - StudySmarter, Zugriff am April 25, 2025, <https://www.studysmarter.de/studium/informatik-studium/systemarchitektur/cache-kohaerenz/>
2.  Cache coherence - Wikipedia, Zugriff am April 25, 2025, <https://en.wikipedia.org/wiki/Cache_coherence>
3.  Cache Coherence | GeeksforGeeks, Zugriff am April 25, 2025, <https://www.geeksforgeeks.org/cache-coherence/>
4.  Cache Coherence Protocols in Multiprocessor System ..., Zugriff am April 25, 2025, <https://www.geeksforgeeks.org/cache-coherence-protocols-in-multiprocessor-system/>
5.  Richtiger Vergleich von CPU-Geschwindigkeiten - InoNet Wiki, Zugriff am April 25, 2025, <https://wiki.inonet.com/richtiger-vergleich-von-cpu-geschwindigkeiten>
6.  Abstrakte Interpretation (AbsInt) - LMU, Informatik, TCS, Zugriff am April 25, 2025, <https://www2.tcs.ifi.lmu.de/~abel/lehre/SS09/ProSem/Ausarbeitungen/Pleintinger.pdf>
7.  Cache Coherence - Redis, Zugriff am April 25, 2025, <https://redis.io/glossary/cache-coherence/>
8.  A Primer on Cache Coherence Protocols - Jyotiprakash's Blog, Zugriff am April 25, 2025, <https://blog.jyotiprakash.org/a-primer-on-cache-coherence-protocols>
9.  How do cache coherence protocols improve performance in multi-core CPUs? - FastNeuron, Zugriff am April 25, 2025, <https://fastneuron.com/forum/showthread.php?tid=4811&action=nextnewest>
10. Coherence | Wave Theory, Interference & Diffraction - Britannica, Zugriff am April 25, 2025, <https://www.britannica.com/science/coherence>
11. Coherence (physics) - Wikipedia, Zugriff am April 25, 2025, <https://en.wikipedia.org/wiki/Coherence_(physics)>
12. Coherence (signal processing) - Wikipedia, Zugriff am April 25, 2025, <https://en.wikipedia.org/wiki/Coherence_(signal_processing)>
13. A unifying view of coherence in signal processing - Cyclostationary, Zugriff am April 25, 2025, <https://cyclostationarity.com/wp-content/uploads/2022/12/202210131027.pdf>
14. Tightly-Coupled and Fault-Tolerant Communication in Parallel Systems, Zugriff am April 25, 2025, <https://d-nb.info/990095762/34>
15. Cache Coherence Protocol Verification using Ωmega Cache Coherence Protocol Verification using mega - PDXScholar, Zugriff am April 25, 2025, <https://pdxscholar.library.pdx.edu/cgi/viewcontent.cgi?article=1215&context=compsci_fac>
16. Verifying Safety of a Token Coherence Implementation by Parametric Compositional Refinement - Architecture and Compilers Group, Zugriff am April 25, 2025, <https://acg.cis.upenn.edu/papers/vmcai05_verifying_token_coherence_safety-extended.pdf>
17. Why On-Chip Cache Coherence is Here to Stay - CMU School of Computer Science, Zugriff am April 25, 2025, <http://www.cs.cmu.edu/~15740-f20/papers/cacm12-martin-coherence.pdf>
18. Classical and quantum coherence | Quantum Optics Class Notes - Fiveable, Zugriff am April 25, 2025, <https://library.fiveable.me/quantum-optics/unit-3/classical-quantum-coherence/study-guide/U4us6bVmQe5jn4xM>
19. Optics basics: Coherence | Skulls in the Stars, Zugriff am April 25, 2025, <https://skullsinthestars.com/2008/09/03/optics-basics-coherence/>
20. What is quantum coherence? | Argonne National Laboratory, Zugriff am April 25, 2025, <https://www.anl.gov/article/what-is-quantum-coherence>
21. Optical coherence versus quantum coherence - Physics Stack Exchange, Zugriff am April 25, 2025, <https://physics.stackexchange.com/questions/438287/optical-coherence-versus-quantum-coherence>
22. Coherence -Fundamentals of Signal Processing - VRU, Zugriff am April 25, 2025, <https://vru.vibrationresearch.com/lesson/coherence-signal-analysis/>
23. What is meant by "correlation" when referring to spectral coherence, Zugriff am April 25, 2025, <https://dsp.stackexchange.com/questions/35629/what-is-meant-by-correlation-when-referring-to-spectral-coherence>
24. Coherence Mathematics - Understanding Waveform Relationships - VRU, Zugriff am April 25, 2025, <https://vru.vibrationresearch.com/lesson/coherence-mathematics/>
25. Coherence Function | Mathematics of the DFT - DSPRelated.com, Zugriff am April 25, 2025, <https://www.dsprelated.com/freebooks/mdft/Coherence_Function.html>
26. The Coherence Function - A Brief Review - Crystal Instruments, Zugriff am April 25, 2025, <https://www.crystalinstruments.com/blog/2015/1/12/the-coherence-function-a-brief-review>
27. Coherence and the Cross Spectrum - YouTube, Zugriff am April 25, 2025, <https://m.youtube.com/watch?v=igRrGrxbg-Y>
28. Ghostwriter: A Cache Coherence Protocol for Error-Tolerant Applications - Prof. Joshua San Miguel, Zugriff am April 25, 2025, <https://jsm.ece.wisc.edu/docs/kao-icppems2021.pdf>
29. CONTEXT-AWARE COHERENCE PROTOCOLS FOR FUTURE PROCESSORS - CiteSeerX, Zugriff am April 25, 2025, <https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=fc98fb7f1e271f6b32486b61d5ed94d316a8213e>
30. Cache-Kohärenz in hart echtzeitfähigen Mehrkern-Prozessoren - Eldorado - Repository of the TU Dortmund, Zugriff am April 25, 2025, <https://eldorado.tu-dortmund.de/bitstream/2003/34097/1/Dissertation.pdf>
31. MESI – Wikipedia, Zugriff am April 25, 2025, <https://de.wikipedia.org/wiki/MESI>
32. Structural Design and Proof of Hierarchical Cache-Coherence Protocols Joonwon Choi - DSpace@MIT, Zugriff am April 25, 2025, <https://dspace.mit.edu/bitstream/handle/1721.1/130759/1252059400-MIT.pdf?sequence=1&isAllowed=y>
33. Verifikation reaktiver Systeme, Zugriff am April 25, 2025, <https://es.cs.rptu.de/publications/datarsg/BuKS04.pdf>
34. Erweiterung des Threadmodelles für den Einsatz in verteilten und heterogenen Systemumgebungen - EPub Bayreuth, Zugriff am April 25, 2025, <https://epub.uni-bayreuth.de/490/1/nagelraik.pdf>
35. Hardwareunterstützung für nicht-blockierende Synchronisation, Zugriff am April 25, 2025, <http://www4.cs.fau.de/Lehre/SS09/HS_AKSS/papers/02_Ausarbeitung_Martin_Hoffmann.pdf>
36. Design and Implementation of a Directory based Cache Coherence Protocol - ICS Publications, Zugriff am April 25, 2025, <https://publications.ics.forth.gr/tech-reports/2011/2011.TR418_Directory_based_Cache_Coherence_Protocol.pdf>
37. What's different about a directory based cache coherence protocol? - Stack Overflow, Zugriff am April 25, 2025, <https://stackoverflow.com/questions/35342036/whats-different-about-a-directory-based-cache-coherence-protocol>
38. WiDir: A Wireless-Enabled Directory Cache Coherence Protocol - The i-acoma group at UIUC, Zugriff am April 25, 2025, <https://iacoma.cs.uiuc.edu/iacoma-papers/hpca21.pdf>
39. Rainbow: A Composable Coherence Protocol for Multi-Chip Servers - ResearchGate, Zugriff am April 25, 2025, <https://www.researchgate.net/publication/339163873_Rainbow_A_Composable_Coherence_Protocol_for_Multi-Chip_Servers>
40. Everything You Always Wanted to Know About Synchronization but Were Afraid to Ask - acm sigops, Zugriff am April 25, 2025, <https://sigops.org/s/conferences/sosp/2013/papers/p33-david.pdf>
41. Which cache-coherence-protocol does Intel and AMD use? - Stack Overflow, Zugriff am April 25, 2025, <https://stackoverflow.com/questions/31876808/which-cache-coherence-protocol-does-intel-and-amd-use>
42. Kapitel 1 Einleitung und Stand der Technik, Zugriff am April 25, 2025, <https://d-nb.info/1015354440/34>
43. Cache coherency ensures that the behavior is correct, but every time a cache i... | Hacker News, Zugriff am April 25, 2025, <https://news.ycombinator.com/item?id=33760314>
44. Delta Coherence Protocols - DTIC, Zugriff am April 25, 2025, <https://apps.dtic.mil/sti/tr/pdf/ADA480418.pdf>
45. POPS: Coherence Protocol Optimization for both Private and Shared Data - Department of Computer Science : University of Rochester, Zugriff am April 25, 2025, <https://www.cs.rochester.edu/u/sandhya/papers/pact11_pops.pdf>
46. \[2002.03944\] Rainbow: A Composable Coherence Protocol for Multi-Chip Servers - arXiv, Zugriff am April 25, 2025, <https://arxiv.org/abs/2002.03944>
47. Low-overhead Reversible Coherence Protocol - IEEE Computer Society, Zugriff am April 25, 2025, <https://www.computer.org/csdl/journal/tq/5555/01/10858001/23VCjghyG2s>
48. \[2006.16535\] RCP: A Low-overhead Reversible Coherence Protocol - arXiv, Zugriff am April 25, 2025, <https://arxiv.org/abs/2006.16535>
49. ReversiSpec: Reversible Coherence Protocol for Defending Transient Attacks, Zugriff am April 25, 2025, <https://www.researchgate.net/publication/342587793_ReversiSpec_Reversible_Coherence_Protocol_for_Defending_Transient_Attacks>
50. You Wu, Zugriff am April 25, 2025, <https://superyou.github.io/>
51. \[2409.02088\] Cache Coherence Over Disaggregated Memory - arXiv, Zugriff am April 25, 2025, <https://arxiv.org/abs/2409.02088>
52. Lamport clocks: verifying a directory cache-coherence protocol - Scholars@Duke publication, Zugriff am April 25, 2025, <https://scholars.duke.edu/individual/pub799686>
53. Synchronization in timestamp-based cache coherence protocols - DSpace@MIT, Zugriff am April 25, 2025, <https://dspace.mit.edu/handle/1721.1/106086>
54. A Comparison of Software and Hardware Synchronization Mechanisms for Distributed Shared Memory Multiprocessors, Zugriff am April 25, 2025, <https://www.cs.utah.edu/docs/techreports/1996/pdf/UUCS-96-011.pdf>
