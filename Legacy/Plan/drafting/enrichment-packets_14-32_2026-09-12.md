# Fokussierte Enrichment Packets — Kapitel 14–32 (Welle 2)

> Stand: 2026-09-12 · Operative Drafting-Schicht. Normativ bleiben Canon,
> `decision-log_akt2-3_2026-09-11.md` (D23-01…D23-18) und die Akt-Arcs. Erfüllt die
> Masterplan-Regel „Ein Kapitel ohne ausgefülltes Enrichment Packet ist nicht draftbereit".
> Grundlage: `docs/superpowers/specs/2026-09-12-chapter-enrichment-design.md`.

## 1. Blockbefund

19 Kapitel, 19.908 Wörter, Schnitt **1.047**. Akt I liegt bei 1.677 und wurde gegen ein
ausdrückliches Budget geschrieben; für Akt II und III nennt kein Plan eine Wortzahl. Die
Kapitel sind darum nicht schlecht, sondern **unausgeführt**: jeder Beat wird einmal gesetzt
und verlassen.

Was fehlt, benennt der Audit: Weltmaterial dünnt in Akt II/III aus (Defekt 3), Körperkosten
verschwinden, je philosophischer ein Kapitel wird (Defekt 5), Nebenfiguren bleiben
Funktionen (Defekt 4), Hooks sind Themen statt Ereignisse (Defekt 6), und 14–23 drohen zur
Seminarfolge zu werden (Defekt 8).

## 2. Bindende Regeln für den ganzen Block

1. **Nur einfügen, nie umschreiben.** Jeder Satz des bestehenden Drafts muss wortgleich und
   in derselben Reihenfolge erhalten bleiben. Neues Material steht **zwischen** vorhandenen
   Sätzen. Absätze dürfen geteilt werden, um dazwischen einzufügen; Sätze nicht.
   Maschinell geprüft mit `python3 scripts/check_enrichment.py --base HEAD "NN-*.md"` —
   der Lauf muss OK melden, bevor ein Kapitel abgegeben wird.
2. **Keine neue Handlung.** Kein neuer Beat, keine neue Figur, kein neues Weltelement, keine
   neue Zahl, die eine bestehende Rechnung verändert. Anreicherung vertieft Vorhandenes.
3. **R-2 ist die Hauptgefahr.** Ein Theoriekapitel zu verdoppeln ist der direkte Weg zum
   Seminar. Jedes Kapitel unten führt **verbotene Erklärungen**; sie gelten auch dann, wenn
   Platz da wäre.
4. **Theorie wird gelesen, angewandt oder erlitten — nie referiert.** Jedes Kapitel 14–23
   braucht ein Objekt, eine Arbeitshandlung und einen Verlust. Wo ein Gedanke auftaucht,
   muss er an einem Gegenstand hängen, den eine Hand anfassen kann.
5. **Die zwei Uhren nie als Theorie.** B-Timelock über Wartungsfrequenz und Schlangenlänge;
   A-Optionlock über schrumpfende unveränderte Lesepfade. Erlebbar an Restzahlen,
   Zugriffsrechten, geschlossenen Wegen, Wartungsintervallen — nie erklärt (D23-03).
6. **R-5 Wärme/kaltes Ozon.** Nie in derselben Szene. **Juna-Wärme** (hautwarm, quellenlos)
   ist an Leitung und drittem Fenster kanonisch und dort erlaubt, wo kein Ozon ist — Kap 24
   und 30 tragen sie. **Silas-Wärme ist verbraucht**: der eine erlaubte Cue außerhalb des
   Heat Spike steht in Kap 34 (D23-18). In Welle 2 bleibt Silas rein syntaktisch.
7. **R-10 Juna.** Nie grammatisches Subjekt, nie Name, nie Stimme, nie Körper. D23-04: der
   Kanal überträgt Präsenz, Salienz, Gleichzeitigkeit, affektiven Druck — **keine Wörter,
   Erinnerungen, Koordinaten, Fakten, Befehle**.
8. **R-8 / AEGIS.** Bewahrungsfunktion, kein Charakter. Eingriffe erscheinen als Wartung,
   Rechtekorrektur, Konsolidierung, Selbstdiagnose — nie als Drohung mit Persönlichkeit.
9. **R-6** max. ein dominantes Konzept pro Szene. Ein angereichertes Kapitel bekommt mehr
   Szenen, keine dichteren.
10. **Bridge-Anteil** ~25 % in 14–26, ~40 % ab 27. Stimmen über Syntax, Körper und Handlung,
    **nie** über Header, Sprecher-Tags oder Crew-Inszenierung. Genesis-Flashbacks
    ausschließlich in 18, 21, 22.
11. **Frontmatter und Template-Kopf unverändert**, außer der Draft-Kommentar
    (`v0.2 (2026-09-12)` + Anreicherungsvermerk).
12. Stimme: Kael 1. Person Präsens (14–26), Wir-Kael ab 27. Nüchtern, beobachtend, konkret,
    zählend. Empfinden liegt im Körper, in Zahlen, in Auslassung — nie benannt. Kein Pathos,
    kein Erzählerkommentar, keine Ironie, keine Metapher aus fremden Welten.

## 3. Die zehn Szenenformen (14–23) — das Mittel gegen die Seminarfolge

Jedes Kapitel hat eine **andere Form**. Die Anreicherung muss die Form schärfen, nicht
verwischen. Wer bei der Erweiterung in „Kael liest und denkt nach" zurückfällt, hat das
Kapitel beschädigt.

| Kap | Form | Die Handlung, an der die These hängt |
|---|---|---|
| 14 | Zugang / Archiv | einen Zugang behalten, der einem nicht gehört |
| 15 | Dialogtest | ein Gegenüber prüfen, das nicht Beweisstück sein will |
| 16 | Systemeingriff | reparieren und dadurch anderswo beschädigen |
| 17 | Wahrnehmungsentscheidung | einem Bestand nach unten folgen, statt ihn wegzuräumen |
| 18 | Übersetzungsexperiment | etwas übertragen, das beim Übertragen verliert |
| 19 | Belagerung / Isolation | Verbindungen werden getrennt, eine hält trotzdem |
| 20 | Schöpfungswerkstatt | etwas herstellen, das ein falsches Nebenprodukt hat |
| 21 | Grenzprobe | eine Probe, die sich nicht zurücknehmen lässt |
| 22 | Herkunftskollision | zwei gültige Ursprünge derselben Sache |
| 23 | gemeinsamer Bau | aus unvereinbaren Teilen etwas Tragendes bauen |

## 4. Was jedes Kapitel bekommt (Grundlast)

Statt pro Kapitel zu wiederholen — gilt für alle 19, mit den kapitelspezifischen Zusätzen
in §6:

- **Körperkosten.** Der Konflikt verändert Atem, Gang, Temperatur, Schmerz, Berührung oder
  Zeitgefühl. Je philosophischer das Kapitel, desto strenger diese Pflicht.
- **Weltmaterialisierung.** Pro Beat genau **eine** Kernwelt mit sechs Parametern (Licht,
  Material, Temperatur, Geruch, Geräusch, Zeitgefühl), einem benutzbaren Objekt, einem
  räumlichen Hindernis, einer durch Handlung entstandenen Veränderung und einem Detail, das
  nur diese Fokalisierung bemerken würde. Sensorik anderer Kernwelten **nie** importieren.
- **Nebenfigur mit eigenem Ziel.** Mindestens eine Figur oder Kraft handelt aus eigener
  Absicht, nicht als Hindernis, Angebot, Spiegel oder Kanal.
- **Konkreter Hook-out.** Ein beobachtbares Ereignis — Frist, Spur, falsche Zuordnung,
  fehlende Person, unumkehrbare Handlung. Nie ein Thema, nie eine rhetorische Frage.
- **Uhren-Tick.** Eine Restzahl, ein geschlossener Pfad, ein Wartungsintervall oder ein
  Zugriffsrecht, das sich seit dem Vorkapitel verändert hat.

## 5. Zielbänder

| Kapitel | Band | Begründung |
|---|---|---|
| 14–23 | 1.900–2.200 | Zyklen Z1–Z3; je eine Szenenform |
| 24–26 | 2.000–2.300 | Modusgrenze, höchste emotionale Last vor Akt III |
| 27–32 | 1.900–2.200 | Akt-III-Aufbau; Konfrontationsfähigkeit, noch nicht Klimax |

## 6. Kapitelweise

### Kap 14 — Das Archiv der Grenzen · 1.483 → 1.900–2.200 · Form: Zugang/Archiv
**Zusätzlich:** Das Wartungsfenster als Stadtereignis ausbauen — drei Minuten Stillstand,
wie er aussieht, wer stehen bleibt, was danach fehlt. Die verschwundene Abkürzung muss
körperlich kosten (Kael zählt neu, der Weg wird länger). Theta-9 als nüchternes Archiv, nicht
als Schatzkammer: Regalordnung, Zugriffslatenz, Verzeichnisstruktur.
**Verboten:** dass Kael rebelliert (es ist eine Unterlassung); jede Bewertung des Fehlers;
zu erklären, was Theta-9 später bedeuten wird.

### Kap 15 — Turing-Mechanik · 1.248 → 1.900–2.200 · Form: Dialogtest
**Zusätzlich:** Der Test braucht zwei mögliche schädliche Ausgänge, beide sichtbar. Das
Gegenüber will nicht Beweisstück sein — dieser Widerstand ist der Kern und muss Handlung
werden. Antwortlatenz als Material; das Frageobjekt anfassbar.
**Verboten:** das Turing-Problem zu benennen oder zu referieren; zu entscheiden, ob das
Gegenüber „echt" ist.

### Kap 16 — Die Diktatur der Komplexität · 1.275 → 1.900–2.200 · Form: Systemeingriff
**Zusätzlich:** Drei kleine Reparaturen, jede konkret, jede an ihrem Ort; der entfernte
Ausfall dreimal derselbe. Verantwortung statt Überforderung: Kael merkt, dass er es war.
**Verboten:** Komplexitätstheorie; jede Aussage darüber, dass Systeme grundsätzlich so sind.

### Kap 17 — Phaenomena vs. Noumena · 1.009 → 1.900–2.200 · Form: Wahrnehmungsentscheidung
**Zusätzlich:** Der Weg nach unten durch die Verweisebenen ist die beste Szene des Kapitels
und zu kurz: jede Ebene braucht ihren Fund und ihre Körperfolge. Die 2,4 Sekunden
Validatorlauf sind ein Ereignis — das Warten davor ausbauen.
**Verboten:** Kant, Noumenon, Phänomen; jede Erklärung, was die zwei Ebenen „bedeuten".

### Kap 18 — Qualia-Informationsparadox · 1.017 → 1.900–2.200 · Form: Übersetzungsexperiment
**Zusätzlich:** Der Datensatz muss jemandem konkret gehören; die Kompression muss etwas
Benennbares verlieren. Genesis-Flashback nur hier erlaubt, durch Trigger verdient.
**Verboten:** das Wort Qualia; jede Theorie über Bewusstsein; aufzulösen, was der Rest ist.

### Kap 19 — Z2-AEGIS-Intervention · 900 → 1.900–2.200 · Form: Belagerung/Isolation
**Zusätzlich:** Die Intervention ist logisch zwingende Antwort auf die vorherige Belastung,
kein Angriff. Schutz, der sich als Einkesselung anfühlt — beides gleichzeitig zeigen. Kaltes
Ozon gehört hierher (dann **keine** Wärme im Kapitel).
**Verboten:** AEGIS Absicht oder Bosheit zuschreiben; zu erklären, warum eine Verbindung hält.

### Kap 20 — Z2-Lyons-Kreativität · 1.066 → 1.900–2.200 · Form: Schöpfungswerkstatt
**Zusätzlich:** Das Gegenüber braucht eigenes Risiko und Ablehnungsrecht. Die dritte
Operation entsteht aus Material, das im Raum liegt; das falsche Nebenprodukt ist konkret.
**Verboten:** Kreativität zu preisen; das Nebenprodukt zu deuten.

### Kap 21 — Z3-Simulationsgrenze + Genesis-Flashback · 970 → 1.900–2.200 · Form: Grenzprobe
**Zusätzlich:** Die Probe muss unwiderruflich sein und vorher als solche erkennbar. Die
Trennung kommt als gegenwärtige Körperreaktion, nicht als Rückblende-Infodump.
**Verboten:** die Simulationsgrenze zu erklären; das Zeitparadox aufzulösen; D23-04 verletzen.

### Kap 22 — Z3-AEGIS-Eskalation + Genesis-Flashback · 991 → 1.900–2.200 · Form: Herkunftskollision
**Zusätzlich:** Eskalation und Flashback beantworten **dieselbe** Ursache-Wirkung-Frage. Die
zwei gültigen Ursprünge derselben Komponente sind beide belegbar.
**Verboten:** zu entscheiden, welcher Ursprung stimmt; alte Funktionalität moralisch zu werten.

### Kap 23 — Z3-Mosaik als Schöpfung · 1.078 → 1.900–2.200 · Form: gemeinsamer Bau
**Zusätzlich:** Das Gebaute muss **nutzbar** sein, nicht schönes Symbol — es trägt, weil die
Teile unvereinbar sind. Autorschaft verteilt sich; niemand besitzt das Ergebnis allein.
**Verboten:** das Mosaik als Metapher auszulegen; Harmonie behaupten.

### Kap 24 — Telefon-Stille · 1.171 → 2.000–2.300
**Zusätzlich:** Die Stille muss eine Entscheidung erzwingen: weiter warten oder ohne Antwort
handeln. Nähe auf Distanz; Schweigen weder Ablehnung noch Trost. Juna-Wärme kanonisch
erlaubt (kein Ozon im Kapitel). Die Leitung als Material: Hörer, Gewicht, Kontaktfläche.
**Verboten:** jede Auskunft durch den Kanal (D23-04); die Stille zu deuten.

### Kap 25 — Wegkreuzung · 897 → 2.000–2.300
**Zusätzlich:** Zwei echte Zukunftsverluste, kein richtig/falsch. Jede Wahl schützt einen
Anteil und verletzt einen anderen — beide Anteile müssen im Körper vorkommen.
**Verboten:** die Wahl als weise markieren; den nicht gewählten Weg abwerten.

### Kap 26 — Schritt ins Ungewisse · 943 → 2.000–2.300
**Zusätzlich:** Ressourcen, Verbündete, offene Schulden, Ziel benennen — als Packvorgang,
nicht als Aufzählung. Drei Gegenstände mitgenommen, einer bleibt zurück; der eine, der
bleibt, trägt das Kapitel. Hoffnung als Vorbereitung unter Unsicherheit.
**Verboten:** Aufbruchspathos; zu sagen, worauf er hofft.

### Kap 27 — Autoren-Feder · 1.064 → 1.900–2.200
**Zusätzlich:** Rückkehr darf nicht Wiederholung sein: gleiche Aufgabe, neue plurale Methode.
Die alte Kael-Routine kollidiert mit dem Wir-Rhythmus — das ist eine Reibung mit Kosten.
**Verboten:** Autorschaft zu feiern; das Wir zu erklären.

### Kap 28 — AEGIS' Eskalation · 947 → 1.900–2.200
**Zusätzlich:** Die Eskalation zielt auf Beziehungskanten, nicht auf Körper oder Ort. Die
Schutzentscheidung verteilt Schmerz ungleich; der Konflikt im Wir bleibt offen.
**Verboten:** einen Schuldigen markieren; den Konflikt im Wir auflösen.

### Kap 29 — Angst des Kindes · 960 → 1.900–2.200
**Zusätzlich:** Das Kind hat ein konkretes Jetzt-Ziel. Bezeugen statt beruhigen — die
erwachsene Funktion darf **nicht** übernehmen. Der enge Schutzraum mit sechs Sensoren.
**Verboten:** das Kind niedlich machen; Angst therapieren; Diagnosesprache.

### Kap 30 — Junas Kanal · 894 → 1.900–2.200
**Zusätzlich:** Der Kanal überträgt eine begrenzte Möglichkeit mit Kosten, keine Lösung. Das
Gegenüber behält Eigenständigkeit; Nähe ist nicht Verschmelzung. Juna-Wärme kanonisch
erlaubt (kein Ozon im Kapitel).
**Verboten:** jede Information durch den Kanal (D23-04); Verschmelzung; Trost.

### Kap 31 — Auflösung der Guardians · 970 → 1.900–2.200
**Zusätzlich:** Beide Guardians bieten **echte** Entlastung und zeigen je eine Person, der
sie geholfen haben. Erinnern und Löschen werden als Fähigkeiten übernommen, nicht besiegt.
**Erste sustained Silas-Bridge (D23-05)** — rein syntaktisch, ohne Wärme.
**Verboten:** die Guardians als Gegner; die Nicht-Unterschrift als Sieg.

### Kap 32 — Logische Labyrinthe · 1.025 → 1.900–2.200
**Zusätzlich:** Provenienztest mit drei Kandidaten und einem falschen Zwischenergebnis. Der
Fehler wird nicht romantisiert — er verletzt jemanden konkret. **Oblivion-Fokalisierung
beginnt (D23-06)**: kurz, funktional, ohne Name und Motiv. Silas klarer als in 31.
**Verboten:** den Fehler als lehrreich markieren; Perfektion und Wahrheit gegeneinander
ausspielen, statt es an den drei Kandidaten zu zeigen.

## 7. Readiness Gate — je Kapitel vor Abgabe

1. `check_enrichment.py` meldet OK (jeder Satz erhalten, nur Einfügungen).
2. Eröffnung greift den Hook-out des Vorkapitels konkret auf.
3. Jede Szene verändert Ziel, Wissen, Beziehung oder Risiko.
4. Genau ein dominantes Konzept pro Szene (R-6).
5. Pro Beat genau eine Kernwelt mit sechs Parametern.
6. Mindestens eine Gegenfigur oder Kraft handelt aus eigener Absicht.
7. Die These wird durch Entscheidung und Preis gezeigt, nie ausgesprochen (R-2).
8. Mindestens eine falsche, aber plausible Deutung bleibt bestehen.
9. Ein Uhren-Tick ist sichtbar, ohne erklärt zu werden.
10. Der Schluss exportiert eine konkrete beobachtbare Folge.
11. Keine der verbotenen Erklärungen steht im Text.
12. Wortzahl im Band; Frontmatter und Template-Kopf unverändert.
