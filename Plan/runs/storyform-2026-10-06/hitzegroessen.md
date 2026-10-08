# Die Hitzegrößen — jede Erwähnung, mit Einheit und Träger, 2026-10-06

**Status:** Arbeitsmaterial, kein Kanon, keine Entscheidung. Die Tabelle ordnet, was dasteht. Sie wählt keine
Mechanik und ändert keinen Wert. Was daraus folgt, entscheidest du in der Weiche zur Hitzebuchführung (W24; in der
kritischen Durchsicht heißt sie W-D).

**Anlass:** `Plan/runs/storyform-2026-10-06/kritische-durchsicht.md`, Befunde P3, M4 und S4 sowie §6 Punkt 4.

**Eingaben:** Commit `ce26003a`. Keine der gelesenen Dateien weicht im Arbeitsbaum davon ab. Gelesen habe ich `Manuscript/kap-01/entwurf-j-rueckfrage.md` (J),
`Manuscript/kap-02/entwurf-a-die-rolle-haelt.md` (K2), `Manuscript/plot/treatment.md` (T), `Plan/storyform/clock-b.json`
(CB), `Plan/storyform/b.json`, `Plan/storyform/a.json`, `Plan/storyform/development.json` (D), `Manuscript/kanon.md`
und `Manuscript/welt/*.md`. Nur zur Herkunft eines Worts kam eine Zeile aus `Manuscript/kap-01/entwurf-g-vorkuehlung-2.md`
(G) dazu. Die Zeilen sind mit `nl -ba` und `rg -n` erhoben. Bei D steht das Kapitel, in dessen Objekt die Zeile steht.

**Aufgenommen:** Joule, Bit, die an Löschkosten hängen, Prozent der Reserve, das Abwärmebudget, Vorkühlung, Kühlung,
Temperatur als Puffer, Landauer sowie Wärme und Hitze, wo sie als Größe oder Budget gemeint sind.
**Nicht aufgenommen:** Wärme im Sinn von Gefühl oder Nähe: T:L46, T:L314–L315, D:L911 (Kap 24). Ebenfalls nicht aufgenommen
ist die Quellregel „keine Wärme in Kap 1“ (`kanon.md:L48`), weil sie ausdrücklich nicht bindet. Kaels kalte Finger
(K2:L40) und die kalte Hand (K2:L184) sind Körperempfinden ohne Buchführung und stehen nur der Vollständigkeit halber
in einer Zeile.

**Träger:** *Zeile* = ein einzelner Löschposten, *Sektor* = Sektor 04 der Stadt, ihre Fenster und ihre Kühlung,
*AEGIS* = AEGIS' Reserve, *Kael* = in Kael, *unklar* = der Text sagt es nicht.

## 1. Die Tabelle

| Beleg | Kap | Größe, wie sie dasteht | Einheit | Träger | Was sie ändert |
|---|---|---|---|---|---|
| J:L23 | 1 | Raumtemperatur „07:02 · 20,6 °C“ | °C | Sektor (WE 0418) | Vorkühlung vor dem Fenster |
| J:L25 | 1 | „einundzwanzig Grad, immer“ | °C | Sektor | Sollwert, ohne Fenster |
| J:L35 | 1 | „07:14 · 20,6 °C“ | °C | Sektor | Vorkühlung |
| J:L47 | 1 | „VORKÜHLUNG LÄUFT · 20,2 °C“ | °C | Sektor | Fenster 16:40–16:43 (J:L46) |
| J:L49 | 1 | „Morgens ist es dann kühl“ | — | Sektor | Kalender: „Alle paar Wochen ist ein Sektor dran“ |
| J:L61 | 1 | „der Umfang in Bit und die Abwärme in Joule“: 2,1 × 10¹¹ Bit, 0,00000000059 J | Bit, J | Zeile | Löschung (Ausgleich) |
| J:L74–L75 | 1 | „UMFANG 2,2 × 10²⁹ BIT“, „ABWÄRME 6,18 × 10⁸ J“ (WE 0418) | Bit, J | Zeile (Anschluss) | Löschung im Fenster 16:40 |
| J:L83 | 1 | „ein paar Millionstel Joule“ als Höchstwert sonst; „sechshundertachtzehn Millionen“; „fast zwei Tonnen Wasser“ | J, kg | Zeile | Vergleich, Kaels Rechnung |
| J:L85 | 1 | „kühlt die Stadt den ganzen Sektor herunter, um Platz zu schaffen für die Wärme“ | — | Sektor | Vorkühlung als Puffer für die Löschwärme |
| J:L97 | 1 | „VORKÜHLUNG SEKTOR 04 BEREITS ERFOLGT“ | — | Sektor | Rückfrage |
| J:L98 | 1 | „ABWÄRMEBUDGET 6,18 × 10⁸ J WIRD UMVERTEILT“ | J | Sektor, je Fenster | Rückfrage: Umverteilung auf andere Posten |
| J:L104–L110 | 1 | sieben Posten von 1,9 × 10²⁷ bis 6,6 × 10¹⁷ Bit (Bank 3,1 × 10¹⁹) | Bit | Zeilen | Umverteilung ins Fenster 16:40 |
| J:L112–L113 | 1 | „41 207 WEITERE“, „SUMME 2,2 × 10²⁹ BIT“ | Bit | Sektor (Fenster) | Umverteilung |
| J:L116 | 1 | „Die Stadt hat die Kälte schon bezahlt“ | — | Sektor | Vorkühlung, die verbraucht werden muss |
| J:L125 | 1 | „sieben Milliarden“ Bänke | Verhältnis | Zeile | Kaels Rechnung: Bit ÷ Bit |
| J:L149 | 1 | „16:34 · 20,1 °C“ | °C | Sektor | Vorkühlung |
| J:L181 | 1 | „zwanzig Komma eins“ → „21,0 °C“ | °C | Sektor | Fenster 16:40–16:43, Löschwärme |
| J:L185 | 1 | „Einundvierzigtausend Dinge, und es ist nicht einmal warm geworden“ | — | Sektor | Fenster |
| J:L223 | 1 | „21,0 °C“ in der Wohneinheit | °C | Sektor | nach dem Fenster |
| J:L229 | 1 | „wie schwer es ist. Sieben Milliarden Bänke.“ | Verhältnis | Zeile (Anschluss) | — |
| J:L237 | 1 | „VORKÜHLUNG SEKTOR 04 BEGINNT“ | — | Sektor | verschobenes Fenster 06:10 |
| J:L245 | 1 | „20,9“ | °C | Sektor | Vorkühlung |
| K2:L15 | 2 | „20,6 °C“ um 06:10 | °C | Sektor | Vorkühlung der Nacht |
| K2:L21 | 2 | „VORKÜHLUNG SEKTOR 04 AUSGESETZT“ | — | Sektor | Prüfung statt Fenster |
| K2:L30 | 2 | „In der Nacht vor dem Fenster … kühlen, um neun Zehntel Grad“ | K | Sektor | Kalender: nächstes reguläres Fenster |
| K2:L32 | 2 | „20,7. 20,8. … 21,0“ | °C | Sektor | Vorkühlung ausgesetzt |
| K2:L40 | 2 | „Meine Finger sind kalt, obwohl die Luft einundzwanzig Grad hat“ | °C | Kael (Körper) | — |
| K2:L48 | 2 | „ANHAFTENDES OHNE EINTRAG · 1 POSTEN · 2,8 × 10¹⁹ BIT“ | Bit | Zeile | Löschung im Fenster vom Vortag |
| K2:L55 | 2 | „3,1 × 10¹⁹ … Neun Zehntel davon waren nicht die Bank“ | Bit | Zeile | Kaels Rechnung |
| K2:L125 | 2 | „sechshundertachtzehn Millionen Joule“ | J | Zeile (Anschluss) | Kaels Ursache gegenüber der Kollegin |
| K2:L173 | 2 | „21,0 °C“ | °C | Sektor | — |
| T:L57 | 2a | „AEGIS' Abwärmebudget ist aufgebraucht“ (Vortex) | — | AEGIS | — |
| T:L74–L75 | 0 | „Das Abwärmebudget steht bei 71 %“ | % | AEGIS | Löschung, Prüfung |
| T:L85 | 1 | „Er rechnet aus Bit und Joule den Preis der Kälte aus“ | Bit, J | Zeile, Sektor | — |
| T:L108 | 3 | „Eine Wärme, die nicht in die Stadt passt“ | — | unklar | — |
| T:L133 | 6 | „sinkt auf 64 %“ | % | AEGIS | erster Sweep |
| T:L147 | 8 | „Zugang zu den Kühlschächten“ | — | Sektor (Anlage) | — |
| T:L155 | 9 | „Die Luft steigt auf exakt 21,0 °C zurück“ | °C | Sektor (welcher, offen) | Löschung eines Namens im Fenster |
| T:L235 | 16 | „sinkt auf 47 %“ | % | AEGIS | Sweep, der scheitert, Checkpoint |
| T:L297 | 22 | „sinkt auf 31 %“ | % | AEGIS | Klassifizierung |
| T:L364 | 28 | „von 31 auf 9 %“ | % | AEGIS | Purge |
| T:L392 | 31 | „Die Landauer-Hitze steigt“ | — | Kael (Oblivion löscht) | inneres Löschen |
| T:L395 | 31 | „AEGIS' Abwärmebudget sinkt“ (ohne Zahl) | — | AEGIS | Kaels inneres Löschen? |
| T:L418 | 33 | „AEGIS' Reserve fällt sichtbar“ | — | AEGIS | ohne genannte Ursache, Kapitel hard-a |
| T:L442 | 35 | „auf 0 %: die Landauer-Hitze, Beat 4“ | % | AEGIS | „im selben Moment“, in dem Oblivion aufhört |
| T:L454 | 36 | „Die Stille nach der Hitze von Kap 35“ | — | AEGIS, Kael? | — |
| T:L473 | 38 | „Was das Abwärmebudget nicht mehr hält, kommt als Rauschen herein“ | — | AEGIS → Kael | Erlöschen |
| CB:L3 | 35 | „Beat 4, die Landauer-Hitze, in Kap 35“ | — | AEGIS | — |
| CB:L4 | — | „Prozent der thermodynamischen Reserve“ | % | AEGIS | — |
| CB:L5–L12 | 0–35 | 71, 64, 47, 31, 9, 0 bei Kap 0, 6, 16, 22, 28, 35 | % | AEGIS | Sweeps, Purge |
| b.json:L303 | — | Herkunft: „begrenzte thermodynamische Reserve“, „Entwurf G's Abwärmebudget“ | — | AEGIS (aus Sektor) | — |
| b.json:L309 | — | „das Abwärmebudget: AEGIS' thermodynamische Reserve; jeder Sweep verbraucht sie“ | — | AEGIS | jeder Sweep |
| a.json:L175 | — | Dorn, „the cynic who believes in thermodynamics“ | — | — | — |
| a.json:L176 | — | „dass seine Schwester in Sektor 04 nicht kocht“ | — | Sektor | Fenster, Welle? |
| a.json:L329 | — | MC-Fähigkeit: „rechnet aus Bit und Joule den Preis aus“ | Bit, J | Zeile | — |
| D:L22 | 0 | „Abwärmebudget steht danach bei 71 %“ | % | AEGIS | Prüfung |
| D:L232 | 6 | „sinkt … bei 64 %“ | % | AEGIS | Sweep |
| D:L297 | 8 | „Zugang zu den Kühlschächten“ | — | Sektor | — |
| D:L326 | 9 | „Rollen, Frist und Vorkühlung blockieren“ | — | Sektor | Vorkühlung läuft in Kap 9 |
| D:L328 | 9 | „exakt 21,0 °C“ | °C | Sektor | Fenster |
| D:L584 | 16 | „bei 47 %“ | % | AEGIS | Sweep |
| D:L831 | 22 | „bei 31 %“ | % | AEGIS | Klassifizierung |
| D:L1064 | 28 | „mehr Abwärmebudget als jeder Sweep zuvor“ | — | AEGIS | Purge |
| D:L1066 | 28 | „bei 9 %“ | % | AEGIS | Purge |
| D:L1189 | 31 | „die Landauer-Hitze steigt“ | — | Kael | Spiegel-Anteile am selben Signal |
| D:L1191 | 31 | „AEGIS' Abwärmebudget sinkt“ | — | AEGIS | Kaels inneres Löschen? |
| D:L1196 | 31 | „Wie viel Hitze verträgt eine Szene …?“ | — | Kael | offene Frage |
| D:L1294 | 33 | „AEGIS' Reserve fällt sichtbar“ | — | AEGIS | — |
| D:L1380 | 35 | „Im selben Moment ist AEGIS' Abwärmebudget aufgebraucht“ | — | AEGIS | — |
| D:L1381 | 35 | „AEGIS' Budget steht auf 0 %“ | % | AEGIS | — |
| D:L1425 | 36 | „die Stille nach der Hitze von Kap 35“ | — | unklar | — |
| D:L1492 | 38 | „Was das Abwärmebudget nicht mehr hält“ | — | AEGIS | — |
| kanon.md:L34 | — | Q8: „ihre Uhr ist das Abwärmebudget“ (Storyform B) | — | AEGIS | — |
| welt/loeschwaerme.md:L11 | — | „Vergessen kostet Wärme.“ | — | allgemein | Löschung |
| welt/loeschwaerme.md:L15 | — | „Nichts entschieden. … Weiche W5“ | — | — | — |
| welt/loeschwaerme.md:L19–L22 | — | F/G: Vorkühlung, „Kälte ist die Uhr“; H: Radiatorflügel; Plot-Entwürfe 1/2: Spindel, Mauer | — | Sektor, Stadt | — |
| welt/grenzfeste.md:L19 | — | „die Mauer ist ein Kühler“ (Plot-Entwurf 2) | — | Welt | — |
| G:L69, G:L92 | 1 | „ABWÄRME 618 000 J“ bei 2,2 × 10²⁶ Bit; „ABWÄRMEBUDGET 618 000 J“ | J | Zeile, Sektor | Vorlage von J und von b.json:L303 |

## 2. Die Rechnungen

Die Landauer-Grenze ist E = k·T·ln 2 mit k = 1,380649 × 10⁻²³ J/K. Die Temperaturen stehen im Entwurf.

| T | k·T·ln 2 |
|---|---|
| 20,1 °C = 293,25 K (J:L149) | 2,806 × 10⁻²¹ J/Bit |
| 20,6 °C = 293,75 K (J:L23) | 2,811 × 10⁻²¹ J/Bit |
| 21,0 °C = 294,15 K (J:L181) | 2,815 × 10⁻²¹ J/Bit |

1. **Die Messreihe (J:L61):** 2,1 × 10¹¹ × 2,806 × 10⁻²¹ = 5,89 × 10⁻¹⁰ J, bei 21,0 °C 5,91 × 10⁻¹⁰ J. Im Entwurf steht
   0,00000000059 J = 5,9 × 10⁻¹⁰ J. **Stimmt.**
2. **Der Anschluss (J:L74–L75):** 2,2 × 10²⁹ × k·T·ln 2 = 6,174 × 10⁸ J (20,1 °C), 6,185 × 10⁸ J (20,6 °C), 6,193 × 10⁸ J
   (21,0 °C). Im Entwurf steht 6,18 × 10⁸ J. **Stimmt.** Am genauesten trifft es bei 20,6 °C. Die zwei Stellen von 2,2
   lassen 6,0 bis 6,3 × 10⁸ J zu.
3. **Folge aus 1 und 2:** Beide Zeilen rechnen die Löschung *genau* an der Landauer-Grenze, mit dem Wirkungsgrad 1.
   Der Text sagt das nirgends. Ein Hard-SF-Leser, der nachrechnet, findet, dass die Stadt ideal löscht.
4. **Zwei Tonnen Wasser (J:L83):** 6,18 × 10⁸ J ÷ (4186 J/(kg·K) × 80 K, von 20 auf 100 °C) = 1845 kg. „Fast zwei
   Tonnen“ **stimmt** für das Erhitzen zum Kochpunkt. Verdampfen würde es nur etwa 238 kg.
5. **„Ein paar Millionstel Joule“ (J:L83):** 3 × 10⁻⁶ J entsprechen etwa 1 × 10¹⁵ Bit. Das verträgt sich mit L61.
6. **Sieben Milliarden (J:L125, J:L229):** 2,2 × 10²⁹ ÷ 3,1 × 10¹⁹ = 7,10 × 10⁹. **Stimmt.**
7. **Neun Zehntel (K2:L55):** 2,8 × 10¹⁹ ÷ 3,1 × 10¹⁹ = 0,903. **Stimmt.** In Joule ist die Bank 3,1 × 10¹⁹ × 2,81 × 10⁻²¹ ≈ 0,087 J
   und das Anhaftende etwa 0,079 J. Diese Joule-Werte stehen nicht im Text.
8. **Die Liste (J:L104–L113):** Die sieben genannten Posten ergeben 2,36 × 10²⁷ Bit, also 1,07 % der Summe. Die
   „41 207 WEITERE“ tragen dann 2,18 × 10²⁹ Bit, im Mittel 5,3 × 10²⁴ Bit je Posten. Das ist kein Widerspruch.
   7 + 41 207 = 41 214 passt zu „Einundvierzigtausend Dinge“ (J:L185).
9. **Die Umverteilung ist energieneutral:** Die Summe der Liste (J:L113) ist gleich dem Umfang der Anschlusszeile
   (J:L74). Also ist die Wärme dieselbe, 6,18 × 10⁸ J, und das deckt sich mit J:L98 und J:L116.
10. **°C gegen J:** Das Fenster hebt die Luft von 20,1 auf 21,0 °C, um 0,9 K (J:L181). K2:L30 nennt dieselben „neun
    Zehntel Grad“ (**stimmt**). Wenn 6,18 × 10⁸ J diese 0,9 K auffüllen, hat der Sektor eine Wärmekapazität von
    6,9 × 10⁸ J/K. Bei Luft allein (etwa 1,2 kJ/(m³·K)) wären das rund 5,7 × 10⁵ m³. Den Rauminhalt des Sektors nennt der
    Text nicht, darum lässt sich das nicht prüfen. Es widerspricht aber auch nichts.
11. **Abgeleitet, nicht geschrieben:** Wenn das nächste reguläre Fenster wieder um 0,9 K vorkühlt (K2:L30) und der Sektor
    dieselbe Wärmekapazität hat, fasst ein reguläres Fenster von Sektor 04 etwa 6,2 × 10⁸ J. Das ist genau die
    Anschlusszeile.
12. **Prozent gegen Joule:** Nicht rechenbar. Keine Zeile nennt, wie viel Joule 100 % der Reserve sind.
13. **G gegen J:** G hat 2,2 × 10²⁶ Bit und 618 000 J (G:L68–L69). Das ist ebenfalls Landauer-genau, bei 20 °C etwa 6,17 × 10⁵ J.
    J hat Bit und Joule beide mit 1000 multipliziert.

## 3. Was die Tabelle zeigt

**Fünf Größen und ein Ereignisname.**
1. Die *Abwärme einer Zeile* in J, aus dem *Umfang* in Bit nach Landauer (J:L61, J:L74–L75, K2:L125, a.json:L329).
2. Das *Abwärmebudget eines Sektorfensters* in J, das sich umverteilen lässt (J:L98, J:L116).
3. Die *Vorkühlung*, also die Raumtemperatur in °C als physischer Puffer des Sektors (J, K2, T:L155, D:L326–L328).
4. *AEGIS' thermodynamische Reserve* in Prozent (CB, b.json:L309, T, D, kanon.md:L34).
5. Die *Landauer-Hitze in Kael*, ohne Einheit (T:L392, D:L1189).
6. Dazu kommt „*die Landauer-Hitze, Beat 4*“ als Name für das Ereignis „Reserve auf 0 %“ (CB:L3, b.json:L309, T:L442).

Die Größen 1 bis 3 hängen zahlenmäßig zusammen (§2, Punkte 2, 9 und 10). Die Größen 4 und 5 hängen an nichts davon.

**Gleich benannt:**
- „*Abwärmebudget*“ steht in J:L98 für Größe 2 (Sektor, Joule). Überall sonst steht es für Größe 4, auch im Kanon
  (kanon.md:L34: „ihre Uhr ist das Abwärmebudget“). b.json:L303 nennt als Herkunft der Uhr ausdrücklich „Entwurf G's
  Abwärmebudget“, also eine Sektorgröße (G:L92).
- „*Landauer-Hitze*“ steht für Größe 5 (Kael, Kap 31) und für das Ereignis 6 (AEGIS, Kap 35).
- „*Reserve*“ (T:L418, D:L1294) und „*Budget*“ (D:L1381) meinen Größe 4.

**Fehlende Umrechnungen:** Prozent ↔ Joule (§2, Punkt 12). Kaels Landauer-Hitze ↔ AEGIS' Prozent: T:L395 und D:L1191
koppeln sie nur durch das Wort „sinkt“ im selben Kapitel. Die Gleichung zwischen °C und Joule (Wärmekapazität des Sektors)
ist nur erschließbar, nicht geschrieben (§2, Punkt 10).

**Der monotone Fall von clock-b:** Die Werte 71 > 64 > 47 > 31 > 9 > 0 fallen streng, und kein Kapitel nennt einen
Anstieg. Gebrochen oder nicht gedeckt ist Folgendes:
- **Kap 1 und 2:** Die Sektorwärme wird umverteilt (J:L98) und die Vorkühlung ausgesetzt (K2:L21). Auf Sektorebene
  verbraucht die Rückfrage nichts, und nichts davon erreicht die Prozentuhr.
- **Kap 14:** Die erste Welle löscht Sektor 04 Abschnitt für Abschnitt (T:L206). Das ist der größte Sweep in Akt II,
  und er hat keinen Wert, weil das Kapitel hard-a ist (`weave.json`). Ob der Fall von 64 auf 47 % zwischen Kap 6 und
  Kap 16 die Welle enthält, steht nirgends.
- **Bridge-Kapitel mit B-Anteil:** Kap 13, 18, 21, 26, 31, 32 und 34 haben keinen Wert, obwohl „jeder Sweep“
  verbraucht (b.json:L309). Kap 31 und Kap 33 sagen „sinkt“ und „fällt sichtbar“ (T:L395, T:L418) ohne Zahl, im
  Intervall von 9 auf 0 %. Die Richtung stimmt. Kap 33 ist hard-a, und wer dort den Fall sieht, bleibt offen.
- **Kap 35:** Das ist P3. Wenn Kaels inneres Löschen in Kap 31 AEGIS' Budget senkt, müsste das Ende dieses Löschens in
  Kap 35 die Reserve schonen. Trotzdem steht sie „im selben Moment“ auf 0 % (T:L442).
- **Kap 36–39:** Die Uhr ist in Kap 35 abgelaufen, aber B läuft bis Kap 39 (kanon.md:L34). Kap 38 lässt das Budget
  noch etwas „nicht mehr halten“ (T:L473).
- **Kalender:** J:L49 („alle paar Wochen“), K2:L30 (die nächste Vorkühlung) und b.json:L220 („Wartungsfenster werden
  dichter“) beschreiben einen Takt. clock-b fällt aber nur mit Handlungen (S4).

**Offene Fragen für W24 (Hitzebuchführung):**
1. Ist AEGIS' Reserve (Prozent) die Summe oder die Grenze der Sektorbudgets (Joule)? Wie viel Joule sind dann 100 %,
   und soll das Wort „Abwärmebudget“ nur eine der beiden Größen bezeichnen?
2. Ist Kaels Landauer-Hitze (Kap 31) ein Abzug von AEGIS' Reserve? Wenn ja: Was entleert die Reserve in Kap 35, im
   Moment, in dem Oblivion aufhört?
3. Fällt die Reserve auch mit dem Kalender, mit jedem geplanten Fenster? Und was kostet die Welle von Kap 14 in Prozent?
