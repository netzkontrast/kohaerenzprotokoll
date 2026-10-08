# Erklärvideo „Kohärenz Protokoll“: Skript und Szenenplan

*Entwurf vom 2026-10-08, zum Plan in `README.md`. Deutsch, 16:9, 5:00, 580 Wörter Sprechertext.*

## Die Zahlen, die das Video nennt

Jede Zahl trägt den Marker ihrer Messung. `python3 scripts/state.py --prose` schlägt fehl, sobald eine nicht mehr stimmt. Vor der
Aufnahme wird neu gemessen, und der Sprechertext folgt dieser Tabelle, nicht umgekehrt.

| Zahl | Was | Szene |
|---|---|---|
| 586 <!--state:sources.landed--> | Dokumente gelandet | 2 |
| 93 <!--state:sources.folded--> | doppelte Exporte aussortiert | 2 |
| 219 <!--state:documents.with_census--> | Dokumente gelesen, mit Begriffsliste und Notiz | 4 |
| 106 <!--state:wiki.pages--> | Begriffsseiten im Wiki | 5 |
| 17 <!--state:wiki.conflicts--> | Konfliktberichte | 6 |
| 9 <!--state:wiki.questions--> | offene Fragen im Wiki | 7 |
| 340 <!--state:graph.nodes--> | Knoten im Netz | 7 |
| 11238 <!--state:graph.edges--> | Verbindungen | 7 |
| 21902 <!--state:graph.evidence_verified--> | geprüfte Zitate als Belege | 7 |

## Die Belege, die auf dem Bildschirm stehen

Jede Platte setzt die echte Zeile. Abgetippt wird nichts: `python3 scripts/read.py <slug>` liefert die Zeile mit ihrer Nummer.

| Platte | Quelle | Zeile |
|---|---|---|
| „Kairos und Sophia werden als zwei distinkte, aber komplementäre Guardians dargestellt, die gemeinsam über diese Domäne wachen.“ | `guardians-und-kern-welten-konzept` | L96 |
| „bei Konflikt gewinnt das Neuere“ | `kohaerenz-protokoll-storyform-und-outline-2026-06-10-md` | L13 |
| „Architektur (post-Reset): zwei Guardians (Mnemosyne + Erasure-Pol)“ | `kohaerenz-protokoll-storyform-und-outline-2026-06-10-md` | L282 |
| C6 · 2026-09-24 · „Es gibt fünf Guardians: LogOS, Mnemosyne, Cerberus, Kairos und Sophia.“ | `Manuscript/kanon.md` | Zeile C6 |
| „Freigegebene Kapitel: Keines.“ | `Manuscript/kanon.md` | Abschnitt „Freigegebene Kapitel“ |

## Szenen

Pro Szene: Zeitfenster, Sprechertext, Bild, Layout. Ein Bildwechsel kommt alle 8 bis 10 Sekunden, das ist der Takt, den OpenMontages
`script-director` verlangt. Regieanweisungen für die Stimme stehen in eckigen Klammern.

### 1 · Hook · 0:00–0:20

> [ruhig, ohne Anlauf] Eine Maschine, die einen Roman schreibt? Hier schreibt sie keinen einzigen Satz. [Pause] Sie tut etwas
> Bescheideneres. Und Schwierigeres: Sie findet Widersprüche. Und dann hält sie an. [Pause] Das ist das Kohärenz Protokoll.
> Folgen wir einem Dokument.

- **Bild:** Papier. „Hier schreibt sie keinen einzigen Satz.“ in Archivo Black, Zeile für Zeile hart geschnitten. Bei „hält sie
  an“ bleibt ein blinkender Cursor stehen. Danach der Titel klein in Mono oben links: `KOHÄRENZ PROTOKOLL / ERKLÄRT`.
- **Layout:** zentrierte Achse.

### 2 · Das Problem · 0:20–0:50

> Hinter dem Roman liegen fünfhundertsechsundachtzig Dokumente. Konzepte, Weltentwürfe, Figurenbibeln, Kapitelpläne, geschrieben
> über mehr als ein Jahr. Viele gab es mehrfach, von manchen bis zu fünf Exporte: Dreiundneunzig Kopien wurden aussortiert.
> [Pause] Und die Dokumente sind sich
> nicht einig. Was in einem steht, widerruft das nächste. Wer daraus ein Buch machen will, muss zuerst wissen, wer was gesagt hat.
> Und wann.

- **Bild:** ein Raster aus 586 kleinen Rechtecken (je ein Dokument), die Zahl groß darüber. 93 Rechtecke werden grau und fallen
  heraus. Bei „widerruft“ blitzen zwei Rechtecke kurz rot auf, die einzigen roten Pixel vor Szene 6.
- **Layout:** asymmetrisches Bento, links die Zahl über acht Spalten, rechts gestapelt die Kategorien in Mono.

### 3 · Landen · 0:50–1:30

> [Geräusch: Papier] Unser Dokument heißt „Guardians und Kern-Welten“. Geschrieben im April 2025. Es kommt aus Google Drive in
> einen Ordner namens Sources, und von da an wird es nie wieder verändert. Eine Prüfsumme hält fest, dass jedes Byte noch
> dasselbe ist. [Pause] Das klingt pedantisch. Es ist die Grundlage für alles Weitere: Wenn später jemand fragt, „Wo steht
> das?“, muss die Antwort auf eine Zeile zeigen, die es wirklich gibt.

- **Bild:** Die Titelzeile des Dokuments als Papierplatte. Darunter tippt Mono den Pfad
  `Sources/drive/guardians-und-kern-welten-konzept.md`, dann eine Prüfsumme, deren Zeichen einrasten.
- **Layout:** Editorial Split, links groß „UNVERÄNDERLICH“, rechts die Platte.

### 4 · Lesen · 1:30–2:10

> Dann wird gelesen. Für jedes Dokument entstehen zwei Dinge: eine Liste der Begriffe, die es selbst benutzt, und eine Notiz,
> was es über sie sagt. Immer mit Zeilennummer. Und die Liste wird geschrieben, bevor jemand nachsieht, was schon bekannt ist.
> Sonst würde das Bekannte entscheiden, was ein neues Dokument sagen darf. [Pause] Zeile sechsundneunzig: Kairos und Sophia wachen gemeinsam über eine
> Welt. [Pause] Ein Programm prüft jedes dieser Zitate gegen seine Zeile. Wer falsch zitiert, fällt auf. Zweihundertneunzehn
> Dokumente sind so gelesen.

- **Bild:** Die Platte mit der Zeile 96, die Nummer `L96` in `--ink-muted` am Rand. Ein Mono-Zeiger springt vom Zitat in der
  Notiz auf die Zeile im Dokument, beide hellen gleichzeitig auf. Zum Schluss die Zahl 219.
- **Layout:** zentrierte Achse.

### 5 · Abgleichen · 2:10–2:50

> Erst danach kommt das Gelesene ins Wiki. Für jeden Begriff gibt es eine Seite, hundertsechs sind es heute. Auf der Seite
> „Guardians“ steht nun, was unser Dokument sagt. Daneben, was jedes andere sagt. [Pause] Nichts wird zusammengefasst, nichts
> geglättet. Jede Lesart behält ihren Absender. Wo zwei Wörter vielleicht dasselbe meinen, entscheidet ein Mensch, und seine
> Entscheidung wird festgehalten, damit ein Programm sie später nachprüfen kann. Denn eine Zusammenfassung müsste entscheiden, welche Quelle recht hat. Und
> genau das darf das System nicht.

- **Bild:** Ein Ablaufdiagramm mit vier Kästen (Sources, Lesen, Wiki, Kanon), 1-px-Linien. Es **bleibt stehen**, während
  Dokumentplatten von links hindurchlaufen und in Spalten auf der Seite „Guardians“ landen, jede mit Absender und Jahr.
- **Layout:** gepinnte Bühne, einmal im ganzen Video.

### 6 · Der Widerspruch · 2:50–3:30

> [langsamer] Und hier wird es interessant. Ein Jahr später, im Juni 2026, sagt ein neues Dokument: Es gibt nicht fünf
> Guardians. Es gibt zwei. Ein drittes zählt vier. [Pause] Und das neue fügt hinzu: Bei Konflikt gewinnt das Neuere. [Pause]
> Ein Dokument, das sich selbst zur Wahrheit erklärt. [Pause] Das System glaubt ihm nicht. Es legt einen Konfliktbericht an,
> C6, stellt alle Fassungen nebeneinander und hört auf. [lange Pause] Hier endet die Maschine. Siebzehn solcher Konflikte gibt
> es.

- **Bild:** **Der eine Bewegungsmoment.** Links die Platte von 2025 („fünf“), rechts die von 2026 (L282, „zwei Guardians“). Beide
  gleiten heran und bleiben 40 px voreinander stehen. Dazwischen zieht sich die rote Linie, dann der Schreibmaschinenanschlag,
  die Musik setzt aus. Bei „gewinnt das Neuere“ erscheint L13 als Mono-Zeile über der rechten Platte und wird rot
  durchgestrichen. Am Ende `C6` groß, darunter die Zahl 17.
- **Layout:** volle Fläche.

### 7 · Das Netz · 3:30–4:10

> [Musik kommt zurück] Aus allen Seiten entsteht ein Netz: dreihundertvierzig Knoten, über elftausend Verbindungen. Jede
> Verbindung kann auf die Zeile zeigen, die sie begründet, belegt durch über einundzwanzigtausend geprüfte Zitate. [Pause] Wer
> fragt, „Was wissen wir über die Guardians?“, bekommt keine Antwort in schönen Sätzen. Er bekommt die Belege, die Konflikte,
> die offenen Fragen. [Pause] Und das Netz stellt selbst Fragen. Wo die Quellen schweigen oder nicht zusammenpassen, entsteht eine
> offene Frage an den Autor. Neun stehen gerade im Wiki. Das Urteil bleibt beim Menschen.

- **Bild:** Das Netz wächst als schwarze Punkte und Linien auf Papier, der Knoten „Guardians“ in der Mitte. Ein Klick auf eine
  Linie öffnet ihre Belegzeile als Mono-Etikett. Rot leuchtet nur die Kante, die zu C6 führt.
- **Layout:** asymmetrisches Bento, Netz über acht Spalten, rechts die drei Zahlen.

### 8 · Kanon · 4:10–4:40

> Und der Mensch hat entschieden. Am 24. September 2026 legt der Autor fest: Es sind fünf. LogOS, Mnemosyne, Cerberus, Kairos
> und Sophia. [Pause] Diese Zeile steht jetzt im Kanon, der einzigen Datei, die für den Roman gilt. Nicht, weil eine Quelle es
> behauptet. Nicht, weil die Mehrheit es sagt. Sondern weil der Autor es entschieden hat. [Pause] Der Roman selbst entsteht erst
> jetzt, in einem eigenen Ordner. Auch dort gilt: Kein Entwurf wird Kanon, nur weil er geschrieben wurde.

- **Bild:** Die Zeile C6 aus `kanon.md` als Tabellenzeile: id, Datum, „Was gilt“. Die fünf Namen erscheinen nacheinander in
  Archivo Black. Die rote Linie aus Szene 6 wird schwarz, denn der Konflikt ist entschieden.
- **Layout:** Editorial Split.

### 9 · Schluss · 4:40–5:00

> [leise] Freigegebene Kapitel: keines. [Pause] Noch. [Pause] Das Kohärenz Protokoll baut keinen Roman. Es baut den Boden, auf
> dem einer stehen kann. Zeile für Zeile, belegt, und mit jedem Widerspruch an seinem Platz.

- **Bild:** „Freigegebene Kapitel: Keines.“ in Mono, dann „Noch.“ in Archivo Black. Schnitt auf den Titel: `KOHÄRENZ PROTOKOLL`
  auf Papier, darunter eine einzelne 1-px-Linie.
- **Layout:** zentrierte Achse.

## Was der Sprechertext nicht ist

Kein Satz des Sprechertexts ist Romanprosa, und keiner gibt eine Lesart als Tatsache über die Welt des Romans aus. Er sagt, was
Quellen sagen und was der Autor entschieden hat. Die zitierten Wendungen („bei Konflikt gewinnt das Neuere“, „zwei Guardians“)
sind kürzer als zwölf Wörter. Das prüft der Test von Entscheidung 027 vor jedem Aufruf.
