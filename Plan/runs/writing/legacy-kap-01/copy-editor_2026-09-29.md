# Korrektorat — Kap 1 (Legacy-Entwurf), copy-editor

- **Eingabe:** `Legacy/Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/chapters/01-erwachen-in-der-konstrukt-stadt.md`, Zeilen 48–210 (Zeilen 1–47 sind Metadaten und wurden nur für die Locks gelesen)
- **Commit:** `9bb5c92`
- **Datum:** 2026-09-29
- **Skill:** `.agents/skills/copy-editor` nach den gemeinsamen Regeln in `.agents/skills/writing-skills`

Dies ist ein Smoke-Test der Adaption des Skills am geparkten September-Entwurf, von dem du gesagt hast, er sei nicht die gewünschte Qualität — kein Gutachten über das Buch.

## Intake (vorab beantwortet)

1. **Hilfestufe:** Flag + Regel + die Standardkorrektur genannt.
2. **Hausstil:** keiner erklärt — aus dem Text erschlossen; was erschlossen wurde, steht im Stylesheet unten.
3. **Vorab freigegeben** (im Stylesheet erfasst, nie als Fehler markiert): die drei gelockten Zeilen — L50, L146 (Direktive mit „EINHEIT 734“), L170 (der kursive Halbsatz, der im Strich abbricht); das Zählen des Erzählers und Zahlen als Stimme; kursive Selbstanweisungen; Direktiven in fetten Versalien.
4. **Umfang:** vollständiger Durchgang.

**Zur Zitierweise der Regeln.** Das amtliche Regelwerk und der Duden liegen im Repository nicht vor. Die Regeln sind deshalb nach ihrem Gegenstand benannt (z. B. „Regelwerk, Zeichensetzung: Anführungszeichen“), nicht nach Paragrafennummer — eine aus dem Gedächtnis getippte Paragrafennummer wäre ein getipptes, kein belegtes Zitat.

Alle Zitate sind wortgetreu, Zeichen für Zeichen; wo nur ein Teil der Zeile zitiert ist, steht der zitierte Teil unverändert in der Zeile. Kurzform der Quelle: `01-erwachen-in-der-konstrukt-stadt.md`.

---

## Korrekturen

### K1 — Schließende Anführungszeichen: gerades Schreibmaschinenzeichen statt „…“

Alle elf schließenden Anführungszeichen der wörtlichen Rede sind das gerade Zeichen `"` (U+0022); die öffnenden sind korrekt `„` (U+201E). Das Paar ist damit gemischt.

- `„Bereit", sagt er.` — 01-erwachen-in-der-konstrukt-stadt.md:L96
- `„Bereit", sage ich.` — 01-erwachen-in-der-konstrukt-stadt.md:L98
- `„Wie viele gestern?"` — 01-erwachen-in-der-konstrukt-stadt.md:L100
- `„Dreihundertsechs."` — 01-erwachen-in-der-konstrukt-stadt.md:L102
- `Er zieht die Mundwinkel nach unten. So lächelt Doran. „Dreihundertsechs ist stabil."` — 01-erwachen-in-der-konstrukt-stadt.md:L104
- `„Dreihundertsechs ist stabil."` — 01-erwachen-in-der-konstrukt-stadt.md:L106
- `„Und wenn es einmal dreihundertsieben wären", sagt er, „dann würdest du es mir nicht sagen."` — 01-erwachen-in-der-konstrukt-stadt.md:L108 (zwei Vorkommen)
- `„Dann würde ich es dir nicht sagen."` — 01-erwachen-in-der-konstrukt-stadt.md:L110
- `„Großzügig heute", sagt er zu seiner Fläche.` — 01-erwachen-in-der-konstrukt-stadt.md:L136
- `„Er mag uns", sage ich zu meiner.` — 01-erwachen-in-der-konstrukt-stadt.md:L138

**Regel:** Regelwerk, Zeichensetzung: Anführungszeichen bei wörtlicher Rede; Duden, Textverarbeitung und Typografie: die deutschen Anführungszeichen sind das Paar „ (unten) und “ (oben, U+201C).
**Standardkorrektur:** jedes schließende `"` durch `“` ersetzen. Die Stellung der Kommas nach dem schließenden Zeichen (L96, L98, L108, L136, L138) ist richtig und bleibt.

### K2 — Überschrift: Geviertstrich statt Halbgeviertstrich

- `# Kapitel 1 — Erwachen in der Konstrukt-Stadt` — 01-erwachen-in-der-konstrukt-stadt.md:L48

**Regel:** Duden, Textverarbeitung und Typografie: der deutsche Gedankenstrich ist der Halbgeviertstrich (–, U+2013) mit je einem Leerzeichen; der Geviertstrich (—, U+2014) ist eine englische Konvention.
**Standardkorrektur:** `—` durch `–` ersetzen, die Leerzeichen bleiben. (Der zweite Geviertstrich des Textes steht im gelockten Halbsatz L170 und ist nicht Gegenstand dieser Korrektur, siehe Stylesheet.)

---

## Zum Umformulieren

### U1 — Bezug des Pronomens „er“ nicht eindeutig

- `Das dauert kürzer als das Verfahren, weil er die Finger hebt, bevor der Verteiler fertig ist, und weil ich nehme, bevor er fertig ist.` — 01-erwachen-in-der-konstrukt-stadt.md:L134

Das zweite „er“ kann sich auf Doran beziehen (der die Finger hebt) oder auf den unmittelbar zuvor genannten „Verteiler“; beide sind maskulin, und die Satzparallele („bevor der Verteiler fertig ist“ / „bevor er fertig ist“) legt beide Lesarten nahe.
**Regel:** Grammatik, Bezug der Pronomen (Duden, Richtiges und gutes Deutsch: Pronomen beziehen sich auf das nächststehende passende Bezugswort, sonst entsteht Mehrdeutigkeit).
Die Lösung verlangt eine Formulierungsentscheidung; der Satz gehört dir. Ist die Doppeldeutigkeit gewollt, bleibt er.

---

## Rückfragen

### R1 — „Er“ für „Delta-Sieben“

- `Delta-Sieben ist leer, als ich hinaustrete. Er ist um diese Zeit immer leer,` — 01-erwachen-in-der-konstrukt-stadt.md:L74

Im Text ist „Delta-Sieben“ an dieser Stelle noch keinem Substantiv zugeordnet; das Maskulinum „Er“ setzt „Korridor“ voraus, das erst in L80 fällt (`An den Stellen, an denen der Korridor Fenster hat,` — 01-erwachen-in-der-konstrukt-stadt.md:L80). Grammatisch ist „Er“ richtig, sobald man „der Korridor Delta-Sieben“ mitdenkt (Kongruenz nach dem gemeinten Gattungswort). Gewollt — der Erzähler denkt den Namen als Korridor —, dann bleibt es.

### R2 — Großschreibung nach Doppelpunkt

- `Vier Sekunden hinein: die Sequenz kommt, die Ränder, die Mitte. Sechs Sekunden hinaus: die Bestätigung, die nächste.` — 01-erwachen-in-der-konstrukt-stadt.md:L128

Nach dem Doppelpunkt schreibt man groß, wenn ein Ganzsatz folgt (Regelwerk, Groß- und Kleinschreibung nach Doppelpunkt). „die Sequenz kommt“ ist ein Ganzsatz; der Text schreibt ihn klein, dagegen in L58 nach Doppelpunkt groß (`Sieben ist eine Zahl, bei der man gut aufhört: Man hat lange genug gelegen,` — 01-erwachen-in-der-konstrukt-stadt.md:L58). Die Kleinschreibung könnte gewollt sein: als Aufzählung parallel zu „die Bestätigung, die nächste“. Wird es als Satz gelesen, ist die Standardform „Die“; wird es als Aufzählung gelesen, bleibt es.

### R3 — Genus von „Klick“

- `*Klick.*` — 01-erwachen-in-der-konstrukt-stadt.md:L164
- `Ich könnte es Doran sagen. Morgen, nach dem Satz. Den Geruch, die Kante, das Klick.` — 01-erwachen-in-der-konstrukt-stadt.md:L196

Der Duden führt das Substantiv als Maskulinum („der Klick“). „das Klick“ liest sich als substantivierte Lautmalerei (wie „das Ach“) und nimmt das kursive Geräusch aus L164 wörtlich auf. Gewollt? Dann bleibt es, und das Stylesheet hält „das Klick“ für das ganze Buch fest.

### R4 — „auf derselben Stelle“

- `Das Glas steht auf der Ablage, gefüllt bis knapp unter den Rand, auf derselben Stelle wie am Morgen.` — 01-erwachen-in-der-konstrukt-stadt.md:L182

Üblich ist „an derselben Stelle“ (Duden, Stichwort „Stelle“); „auf der Stelle“ ist als Wendung für „sofort“ bzw. „ohne Ortswechsel“ belegt. „auf“ nimmt aber den Kreis auf der Ablage aus L64 auf (`Ich stelle das Glas genau auf den Kreis, den es auf der Ablage nicht hinterlassen hat.` — 01-erwachen-in-der-konstrukt-stadt.md:L64). Gewollt? Dann bleibt es.

### R5 — Zählstände auf dem Weg (Zahlenkonsistenz, bewusster Riss?)

- `Zweihundertvier Platten bis zur ersten Abzweigung. Es sind jeden Morgen zweihundertvier.` — 01-erwachen-in-der-konstrukt-stadt.md:L76
- `Bei einhundertdreißig bin ich im Datenknoten.` — 01-erwachen-in-der-konstrukt-stadt.md:L90
- `und das ist egal, denn von hier sind es bis zur Tür zweihundertvier.` — 01-erwachen-in-der-konstrukt-stadt.md:L178

Morgens sind es 204 Platten von der Tür bis zur ersten Abzweigung; abends sind es 204 von einer Stelle in Delta-Sieben (L158), an der der Erzähler stehen bleibt, bis zur Tür. Und „einhundertdreißig“ am Datenknoten liegt unter 204, ohne dass der Text sagt, ob nach der Abzweigung neu gezählt wird. Das Zählen ist vorab freigegebene Stimme; die Rückfrage gilt nur der Übereinstimmung der Zahlen untereinander. Bewusster Riss (die Linie, die „nicht ankommt“, L86)? Dann bleibt es.

### R6 — Ausgeklammerte Präpositionalgruppe am Kapitelende

- `Es ist zerbrochen und fällt noch, in viele Stücke, so viele, dass man sie nicht zählen könnte, und keines geht dabei verloren.` — 01-erwachen-in-der-konstrukt-stadt.md:L204

„in viele Stücke“ gehört der Sache nach zu „zerbrochen“, steht aber hinter „fällt noch“ und lässt sich so auch als „fällt in viele Stücke“ lesen. Die Kommasetzung ist richtig (Nachtrag). Gewollt — die Doppellesart als Bild? Dann bleibt es.

---

## Stylesheet

**Orthografischer Standard (erschlossen):** amtliches Regelwerk, reformierte Schreibung; wo der Text Varianten wählt, stehen sie unten. ß wird gesetzt („Großzügig“, L136; „draußen“ als „Draußen“, L80).

**Anführungszeichen (erschlossen):** deutsche Anführungszeichen „…“ (öffnend durchgehend korrekt; schließend siehe K1). Keine Guillemets, keine verschachtelten Anführungen im Kapitel.

**Wörtliche Rede (erschlossen):** Komma nach dem schließenden Anführungszeichen vor dem Begleitsatz (L96, L98, L136, L138); eingeschobener Begleitsatz mit Kommas auf beiden Seiten (L108); Handlungssatz statt Begleitsatz mit Punkt in der Rede (L104; ebenso L140 ohne Rede). Alles regelgerecht.

**Gedanken und innere Stimmen (erschlossen, vorab freigegeben):** kursiv, ohne Anführungszeichen — Selbstanweisung L62 als eine kursive Spanne mit zwei Sätzen, L174 geteilt um den Begleitsatz „denke ich“ (Komma nach der kursiven Spanne). Der abbrechende Gedanke L170 kursiv. Kursiv steht auch das Geräusch *Klick.* (L164). Offener Punkt für dich: Kursive trägt damit zwei Funktionen, Gedanke und Laut.

**Systemdirektiven (vorab freigegeben):** fette Versalien, Punkt am Satzende: L116, L146.

**Gelockte Zeilen (vorab freigegeben, nicht geprüft, so wie sie stehen):**
- `Das Licht ist schon da, als ich erwache.` — 01-erwachen-in-der-konstrukt-stadt.md:L50
- `**SEQUENZ ABGESCHLOSSEN. EINHEIT 734 ENTLASTET.**` — 01-erwachen-in-der-konstrukt-stadt.md:L146
- `*Etwas in der Frequenz der Lüftung schien zu—*` — 01-erwachen-in-der-konstrukt-stadt.md:L170 — Abbruch mit Geviertstrich, ohne Leerzeichen, innerhalb der Kursive. Es ist der einzige Abbruch im Kapitel; ob diese Form die Buchkonvention für Abbrüche ist, legst du fest, sobald ein zweiter vorkommt.

**Kommas, freigestellte (erschlossen):** Komma zwischen mit „und“ verbundenen Hauptsätzen wird gesetzt (z. B. L60, L76, L112, L176); Komma zwischen gleichrangigen, mit „oder“ verbundenen Nebensätzen zur Gliederung gesetzt (L172). Komma vor erweitertem Infinitiv ohne Einleitewort gesetzt (`versuche ich, mir den ganzen Weg auf einmal vorzustellen` — 01-erwachen-in-der-konstrukt-stadt.md:L86). Asyndetisch gereihte Hauptsätze mit Komma (L80, L158) — im Deutschen korrekt.

**Großschreibung nach Doppelpunkt (erschlossen):** groß bei Ganzsatz (L58), klein bei Aufzählung oder Satzteil (L66, L134, L150, L184); L128 siehe R2.

**Zahlen (erschlossen, vorab freigegeben als Stimme):** in der Erzählung und der Rede ausnahmslos in Worten, auch große Zahlen und Maße („drei Meter zwanzig“, „einundzwanzig Grad“). Die einzige Ziffernfolge ist „734“ in der gelockten Direktive L146. Kardinalzahl als Zahl klein: „bei eins“ (L178); satzanfangs „Eins.“ (L58).

**Getrennt/zusammen:** „stehen bleibe“ / „stehen geblieben“ getrennt (wörtlich); „davorstehe“, „nebeneinanderlege“ zusammen; „jedes Mal“ getrennt; „Wie viele“ getrennt.

**Substantivierungen:** „im Stehen“, „beinahe Stehen“, „dieses Etwas“ groß; „etwas“ als Pronomen klein; „die beiden“ klein.

**Genitiv von Namen:** „Dorans“ ohne Apostroph (L134) — korrekt.

### Wortliste

Erstes Vorkommen im Kapitel, weitere in Klammern. „Mehrdeutig“ heißt: dasselbe Wort steht im Text für zwei Dinge — festgehalten, nicht beanstandet.

| Eintrag | Form im Text | Zeilen |
|---|---|---|
| Konstrukt-Stadt | mit Bindestrich; nur in der Überschrift | L48 |
| Delta-Sieben | mit Bindestrich, Zahlwort ausgeschrieben; maskulin behandelt (R1) | L74 (L158) |
| Datenknoten / Knoten | Kurzform „Knoten“ ab L94 | L90 (L94, L112) |
| Einheit | mehrdeutig: Wohnraum (L64, L182, L192), Person (L74, L78), Bezeichnung des Erzählers in Versalien (L116, L146) | L64 |
| EINHEIT 734 | Versalien, Ziffern; gelockt | L146 |
| Bettmodul | | L60 (L64, L186) |
| Ablage | | L60 (L64, L66, L182) |
| Wandfläche | „spiegelnde Wandfläche“ | L60 (L64) |
| Hygienezelle | Kurzform „Zelle“ in L64 | L64 |
| Konsole | | L64 (L184) |
| Ausgabe | Essensausgabe | L68 (L142, L182) |
| Overall | Anglizismus, eingedeutscht groß | L66 |
| Morgenration / Abendration | zusammengeschrieben | L68 / L182 |
| Riegel, Gel | | L68 (L142, L182) |
| Fläche | mehrdeutig: Arbeitsbildschirm („meiner Fläche“, L80 u. ö.) und Himmel („eine graue Fläche“, L80, L186) | L80 |
| Korridor | | L80 (L128, L158, L172) |
| Abzweigung, Säule, der lange Gang | Wegmarken | L76, L86 (L154) |
| Türme | | L80 (L124, L154, L186) |
| Station | Arbeitsplatz | L86 (L118, L134, L142) |
| Verteiler | maskulin; „Er mag uns“ (L138) meint ihn | L118 (L134) |
| Sequenz | | L126 (L128, L132, L134, L194, L200) |
| Umlaufbilanz | zusammengeschrieben | L124 (L130, L132) |
| Zähler | | L128 |
| Zuweisung | | L134 |
| Entlastung / ENTLASTET | Mittagspause bzw. Direktive | L142 / L146 |
| Takte der Lüftung / Lüftung | | L124 (L170) |
| Zeitanzeige / Anzeige | | L186 / L142 (L184) |
| Sensor-Rekalibrierung | mit Bindestrich, kursiv | L62 (L174) |
| Standardprotokoll | zusammengeschrieben, kursiv | L62 (L174) |
| Doran | Genitiv „Dorans“ | L94 (L134 u. ö.) |
| Klick | kursiv als Laut; „das Klick“ neutrum (R3) | L164 (L196) |
| einundzwanzig Grad | Worte | L56 (L192, L206) |
| drei Meter zwanzig | Worte | L52 (L202) |
| vier / sechs Sekunden | Atemtakt; Kurzform „Vier hinein. Sechs hinaus.“ | L54 (L128; L188) |
| sieben | Zählschritte beim Aufstehen | L58 |
| neun Quadratmeter | | L64 |
| elf Bissen / dreizehn Bissen | morgens / abends | L68 / L182 |
| zweihundertvier | Platten; zwei Bezugsstrecken (R5) | L76 (L86, L178) |
| achtzig | | L78 |
| einhundertdreißig | (R5) | L90 |
| dreihundertsechs | Sequenzen pro Tag | L102 (L104, L106, L144, L148, L184, L200) |
| dreihundertsieben | hypothetisch | L108 |
| einhundertzwei, einhundertdrei | | L128 |
| einhundertsieben | erste Umlaufbilanz schließt | L130 |
| einhundertvierzehn | die Abweichung | L132 (L168) |
| einhundertsechzig | | L134 |
| zweihundert, zweihundertvierzig, zweihundertneunzig | | L144 |
| sechs Minuten | Entlastung | L142 |
| zwei Finger | Geste Dorans | L134 (L150) |
