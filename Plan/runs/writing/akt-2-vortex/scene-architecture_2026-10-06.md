# scene-architecture (Planungs- und Prüfmodus) — Treatment Akt II, Akt III und Vortex, 2026-10-06

**Eingabe:** `Manuscript/plot/treatment.md`, L199–L479 (2b, Kap 14–39), Stand von Commit `ccabe67c`.
Kurzform in diesem Bericht: `:Lnnn` meint `Manuscript/plot/treatment.md:Lnnn`.
**Vertrag:** `Plan/storyform/overview.md` (generiert, Weaving L80–L126, Anteile L138–L171, Journeys L173–L202),
`Plan/storyform/weave.json`, `Manuscript/kanon.md`, Entscheidung 025 Schritte 27, 39, 43–47.
`development.json` und `anteile.json` sind Arbeitsgrundlage, kein Vertrag. `python3 scripts/storyform.py --check`
lief am selben Commit: `ok` (das prüft Storypoint-Zuordnung und Frische, nicht die Qualität der Szenen).
**Nicht wiederholt:** Akt I (Kap 0–13), geprüft in `Plan/runs/writing/akt-1/scene-architecture_2026-10-05.md`.

**Vorbehalt:** Das Treatment stammt aus einer anderen Sitzung **desselben Modells**. Diese Prüfung hat einen frischen
Kontext, ist aber kein unabhängiger Leser: Dieselben Gewohnheiten können auf beiden Seiten sitzen. Eine echte
Gegenlesung kommt erst vom `beta-reader-panel` auf Prosa oder von dir.

Drei Urteile, getrennt: **Struktur** (dient der Absatz den Signposts, die das Weaving dem Kapitel gibt?),
**Kausalität** (trägt die Naht?), **Leser** (was spürt jemand, der nur das bisher Erzählte kennt?). Alles Folgende sind
Vorschläge. Keiner ändert eine Storyform, einen Kanonsatz oder deinen Text.

---

## 1. Struktur — passt es zum Weaving?

### Was sitzt

- **Die Signposts von A sitzen in fast jedem hard-a-Kapitel.** Kap 15 und 23 MC·Subconscious, Kap 17 und 25
  IC·Progress, Kap 19 und 24 RS·Doing, Kap 20 OS·Becoming, Kap 27 und 29 MC·Preconscious (das Lenken der Reflexe,
  `:L350`, ist eine genaue Übersetzung), Kap 30 und 33 RS·Obtaining, Kap 37 OS·Conceptualizing.
- **Die Storypoints deiner Schritte 45 und 46 stehen an ihren Stellen:** Inhibitor Denial Kap 18, Forewarnings Kap 23,
  Catalyst Threat Kap 27, Requirements und Critical Flaw Oppose Kap 28 (`:L358–L359`), Dividends Kap 31, Actuality
  Kap 32, Consequence Kap 34 und 39. Die Story Costs von A stehen nur an den Wenden 26 und 34.
- **Die Treiber an den Aktgrenzen halten H11 (Schritt 27):** 26 entscheidet Kael, 28 handelt AEGIS; 34 entscheidet
  Kael, 35 konvergiert der Sweep (`:L425`).
- **Kaels Lügen werden zu Taten, je an ihrer Stelle:** „Wenn ich nichts fühle …“ im Filter (Kap 24), „Wer mir nah ist,
  wird verletzt“ in Kap 34 (`:L419–L420`), „Solange der Tag richtig ist …“ wird in Kap 39 aufgelöst (`:L474`).
- **Change ist nicht verletzt.** Kap 34 wählt Kael das alte Muster noch einmal; der Umschlag liegt in Kap 35. Das ist
  ausdrücklich so beschlossen (Schritt 27) und keine verfrühte oder verpasste Wende. Ebenso ist die lokale Frist in
  Junas Gegenwart (`:L321`) kein Konflikt mit dem Optionlock.

### Wo der Absatz sein Signpost nicht trägt

| Kap | Weaving | Befund | Art |
|---|---|---|---|
| 16 | B OS·Learning („Erkunden“) | AEGIS sweept, sichert, scheitert. Ein Erkunden, ein Untersuchen des Unlöschbaren, steht nicht im Absatz (`:L227–L234`) | Lücke |
| 18 | bridge, B IC·Memory | Die Seite von B ist ein Satz: „Auf der Ebene von B schimmert das Cluster der Genesis nur“ (`:L253`) | **bewusst** (Schritt 39: die Nacht ohne Ursache) — kein Fehler |
| 23 | A MC·Subconscious (Sehnsucht) | Kaels Ziel ist defensiv („handlungsfähig bleiben“, `:L302`), Rhys handelt, Kael „muss den Verlust tragen“ (`:L304`). Was Kael *will*, zeigt das Kapitel nicht | Lücke |
| 26 | bridge, B MC·Present, B IC·Memory | Kein Satz über AEGIS im Absatz (`:L328–L334`); nur der Hook-out nennt den Purge | Lücke |
| 28 | B MC·Progress („Countdown: … das Abwärmebudget fällt“, `overview.md:L195`) | Der größte Sweep des Buchs kostet laut Absatz Gedächtnis, aber **kein Abwärmebudget** (`:L361–L362`) | Lücke, siehe Uhr B |
| 32 | bridge, B IC·Preconscious | Kein AEGIS im Absatz (`:L398–L403`) | Lücke |
| 34 | bridge, B MC·Progress, IC·Preconscious | AEGIS nur als „Zugriff“ im Ziel und im Hook-out | schwach |
| 36 | A IC·Future | „Juna ist gegenwärtig“ (`:L445`) ist Präsenz, keine Zukunft; `development.json` stellt dieselbe Frage offen | schwach |
| 38 | bridge, B RS·Becoming | Kein AEGIS im Absatz (`:L462–L466`) | Lücke |

**Muster:** Vier Bridge-Kapitel (26, 32, 38, schwächer 34) tragen nur ihre A-Hälfte. Für das Weaving heißt „bridge“
beide Ebenen in einer Szene (`overview.md:L82`). Vorschlag: In jedem dieser Kapitel **eine** AEGIS-Spur, die Kael
sieht oder die ihn etwas kostet. Am billigsten ist die Hitze (siehe Uhr B), weil sie schon beide Ebenen verbindet.

### Die Archetypen verschwinden nach Kap 14

- **A:** Mara, Dorn, die alte Frau und die Kollegin bleiben in KW1 zurück (`:L212`). Das ist deine offene Vorliebe
  (`decisions/025-dramatica-is-the-recipe.md:L210`). Ab Kap 14 hat Storyform A damit keinen Guardian, keinen
  Contagonist, keinen Sidekick und keinen Skeptic mehr, über 25 Kapitel. Help/Conscience, Hinder/Temptation,
  Support/Faith und Oppose/Disbelief argumentieren nicht mehr in der OS.
- **B:** W10-B besetzt Sophia, LogOS, Kairos und Cerberus (`kanon.md:L26`). In Kap 14–39 handelt von ihnen nur Mnemosyne
  (Kap 16). Cerberus ist ein Ortsname, Sophia, LogOS und Kairos kommen nicht vor.
- **Kein Verstoß:** Dramatica verlangt keine Archetypen in jedem Kapitel. Aber ein Ensemble, das beschlossen ist und
  nicht spielt, ist ein strukturelles Leck. Optionen, keine Empfehlung: (a) die Funktionen gehen ausdrücklich an
  Anteile über (Selene trägt etwas von Mara, Dorn kehrt als Versuchung in Oblivion wieder); (b) einer der vier Menschen
  kehrt einmal zurück, als Erinnerung oder in Kap 39/40; (c) Sophia und Kairos bekommen im Purge (Kap 28) je eine
  Gegenstimme, Gewissen und Zweifel, das wären ihre Funktionen genau dort, wo AEGIS Juna gefährdet.

### Kleine Widersprüche im Treatment selbst (Abfragen, keine Urteile)

- **„Der letzte sichere Rückzugsort“** entfällt in Kap 26 (`:L333`), danach entfällt in Kap 34 noch „Der Schutz der
  Abwehr“ als Rückzugsort (`:L423`). Die Uhr von A zählt beide (`decisions/025-dramatica-is-the-recipe.md:L244–L245`).
  „Letzte“ in Kap 26 nimmt Kap 34 die Kraft.
- **„das letzte Sweep“** heißt der Purge in Kap 28 (`:L359`). Die Journey B-OS 34/35 legt den letzten Sweep an den
  Vortex (`overview.md:L193`), und Kap 34 lässt den Sweep sich noch zusammenziehen (`:L425`). Welcher ist der letzte?
- **Wo ist Kael in Kap 28?** „Er findet einen Riss nach KW4, und der Riss schließt sich hinter ihm“ (`:L351`) — Kael ist
  am Ende von Kap 27 in KW4. Der Kanon führt KW3 bis Kap 28 (`kanon.md:L31`), das Weaving gibt Kap 28 die Welt KW3
  (`overview.md:L114`). Läuft der Purge in einer Welt, die Kael schon verlassen hat? Lösbar mit einem Satz, aber er
  fehlt.
- **Kiko** steht im Lager der Suche (`kanon.md:L29`). Kap 29 nennt Kikos Angst „das letzte Aufflammen der Vermeidung“
  (`:L370`); `anteile.json` sagt nur „vor dem Weg“ (`overview.md:L162`). Bewusster Riss (ein Suche-Anteil zeigt
  Vermeidung) oder Verwechslung?
- **„Es ist seine erste eigene Wahl“** (`:L250`) steht so in Schritt 47 (`decisions/025-dramatica-is-the-recipe.md:L269`)
  und ist damit gedeckt. Gegen das eigene Treatment liest es sich aber falsch: Kap 13 verweigert er, Kap 14 nimmt er
  den Weg. Gemeint ist die erste Wahl aus *Suche* statt aus Abwehr. Ein Wort im Absatz würde das sagen.
- **Kap 16, Hook-out:** „Mnemosynes Bewahren öffnet Kael eine Tür“ (`:L235`) ist ein Satz aus AEGIS' Ich. Was dieses Ich
  wissen darf, ist offen (C14). Entweder sieht AEGIS die Tür, dann ist das Wissen; oder der Satz gehört in Kap 17.

## 2. Kausalität — die Nähte 13→14 bis 39→40

| Naht | trägt? | Befund | Vorschlag (Operation, keine Prosa) |
|---|---|---|---|
| 13 → 14 | ja, deshalb | Verweigerung → Welle (H11) | — |
| 14 → 15 | ja, deshalb | KW1 verloren → er will zurück | — |
| 15 → 16 | ja, deshalb | Die Spur gerät in AEGIS' Prüfung | — |
| 16 → 17 | ja, deshalb | Mnemosynes Tür (Wissensfrage oben) | — |
| 17 → 18 | ja, aber | Juna braucht keine Rettung → er will wissen, was gelöscht wurde | — |
| 18 → 19 | ja, deshalb | Der gerettete Rest erlaubt den Kanal | — |
| 19 → 20 | ja, deshalb | Verratener Standort → Eingriff | — |
| 20 → 21 | knapp | Das Echo ist ein Fund, keine Folge der Spaltung | Silas ist im „verbliebenen Zugang“ allein, *weil* die anderen Lager gegangen sind: die Spaltung sichtbar zur Ursache machen |
| 21 → 22 | ja, deshalb | Der Test liefert AEGIS die Klassifizierung | — |
| 22 → 23 | ja, deshalb | Verschoben nach KW3 | — |
| 23 → 24 | ja, deshalb | Rhys scheitert, die Abwehr übernimmt → Kontrolle | — |
| 24 → 25 | **halb** | Der Filter blockt die Wärme; Kap 25 will „ohne den Filter“ verstehen (`:L318`). Was das Ablegen des Filters kostet, sagt niemand. In Kap 24 hat er AEGIS' Ortung verringert (`:L312`) | **Das Ablegen des Filters macht ihn wieder ortbar.** Dann kostet Kap 25 etwas, und Kap 26 steht unter AEGIS' Druck statt nur unter Junas Frist |
| 25 → 26 | ja, deshalb | Junas Entscheidung naht, hier kann er nichts tun | — |
| 26 → 27 | ja, deshalb | Wahl → Weg im Labyrinth | — |
| 27 → 28 | ja, deshalb | Riss nach KW4 → Purge (Ortsfrage oben) | — |
| 28 → 29 | ja, deshalb | Purge läuft → Wettlauf. Aber die Gefahr für Juna bleibt abstrakt (siehe Leser) | — |
| 29 → 30 | **halb** | „Alex stellt sich vor den Weg“ (`:L374`) liest sich als Blockade; Kap 30: „Alex schützt den Weg, mit Stimme“ (`:L379`). Eine Wende ohne Grund, und die Abwehr schützt den Weg zur Nähe | Alex' Motiv nennen: Er schützt **gegen den Purge**, nicht zu Juna hin. Dann bleibt die Abwehr sich treu, und Kap 34 wird vorbereitet |
| 30 → 31 | ja, deshalb | Oblivion und Silas greifen nach demselben Signal | — |
| 31 → 32 | ja, deshalb | Juna erreichbar → Begegnung | — |
| 32 → 33 | knapp | „gefährdet“ → einen Ort halten wollen | — |
| 33 → 34 | **schwach** | Der Hook-out verrät die Tat („Kael lässt sie gehen“, `:L414`) statt sie zu erzwingen. Die Ursache in Kap 33 ist „AEGIS' Reserve fällt sichtbar“ (`:L412`): Ein schwächerer AEGIS macht Juna nicht von selbst gefährdeter | **Der Sweep zieht sich auf Junas Ort zusammen** (in Kap 34 ohnehin der Hook-out). Den Druck eine Szene früher setzen: Der Ort, den sie geteilt haben, ist der Ort, den AEGIS jetzt sieht |
| 34 → 35 | ja, deshalb | Die Nacht wiederholt sich → er will die Wiederholung beenden | — |
| 35 → 36 | **Lücke** | Kap 34 trennt Kael die Verbindung. Kap 36 trägt er „die Wiederverbindung“ (`:L443`), und Juna ist da. Wer hat wieder verbunden? | **Juna verbindet wieder**, aus eigenem Entschluss. Das schließt die Lücke, gibt ihr in Kap 36 eine Tat (W0) und ist das Steadfast der IC: Ihre Haltung bleibt, auch gegen seinen Schnitt. Erfindung, nur Vorschlag |
| 36 → 37 | und dann, **bewusst** | „Es wird ruhig“ → falscher Friede | Als erklärte Ausnahme festhalten (Ruhe vor dem Rauschen), damit spätere Prüfungen sie nicht als Fehler werten |
| 37 → 38 | **und dann** | „Das Rauschen kommt“ (`:L458`): Was es ist und woher es kommt, sagt das Treatment nicht. Es wirkt auch in Kap 38 nichts | Das Rauschen an den Preis von Kap 37 binden (die verlorene Wachsamkeit lässt es herein) **oder** an AEGIS (siehe Uhr B) |
| 38 → 39 | halb | Die Vereinbarung hat eine Folge, gut. AEGIS erlischt in Kap 39, aber nichts in 37/38 führt dorthin | **Das Rauschen ist AEGIS' Sterben**, hörbar auf Kaels Seite: eine Operation, die 37→38 und 38→39 zugleich schließt und die Uhr B bis zum Ende trägt |
| 39 → 40 | ja | Rahmen | — |

**Bilanz:** Akt II und Akt III tragen fast durchgehend. Die Schwachstellen liegen an drei Orten: 24→25 (ein Preis
fehlt), 33→35 (der Druck vor dem Schnitt und die Rückkehr danach) und 37→39 (das Rauschen).

## 3. Leser — wie es wirkt (vorhergesagt, ohne Prosa)

### Wo Kael handelt und wo er getragen wird

| Kap | 14 | 15 | 17 | 18 | 19 | 20 | 21 | 23 | 24 | 25 | 26 | 27 | 29 | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Kael | flieht | sucht | folgt | **wählt** | getragen | fehlt | fehlt | getragen | handelt | sucht | **wählt** | handelt | **wählt** | handelt | fehlt | handelt | handelt | **wählt** | getragen | gibt nach | gemischt | handelt | handelt |

- **Die frühere Sorge stimmt nur für Akt II.** Akt III ist aktiv: Kap 27, 29, 30, 32, 34 sind Kaels Handlungen mit
  Preis. Das Tragen von Kiko (Kap 29) ist die stärkste kleine Wahl im ganzen Plan.
- **Das Loch ist Kap 19–23, fünf Kapitel um die Mitte des Buchs.** Dort wählen die Anteile (`:L263`), AEGIS handelt,
  Silas testet, Rhys scheitert. Kael ist nicht da oder trägt. Genau dort sitzt der Midpoint.
  - Vorschlag für **Kap 20:** Kael entscheidet, *welcher* der zwei Zugänge geschützt wird, und die Gruppe zerbricht an
    seiner Wahl. Damit wird der Zerfall der Lager seine Tat und sein Preis.
  - Vorschlag für **Kap 23:** Kael will etwas für Moros, Rhys führt es aus. Dann scheitert Kaels Wunsch, nicht nur
    Rhys' Hilfe, und das Kapitel trägt MC·Subconscious.
- **Der Pivot in Kap 35 geschieht an Kael.** „Kael will die Wiederholung der Löschung beenden“ (`:L431`), aber
  „Oblivion steht vor der Wahl“ (`:L432`). Weil Oblivion ein Anteil Kaels ist, ist das kein Strukturfehler. Für den Leser
  aber fällt die Entscheidung des Buchs in einer Nebenfigur. Operation: Kaels Kap-13-Geste nach innen wenden — er
  bestätigt Oblivions Löschung nicht mehr, und Oblivion hört *darauf* auf. Der Bogen von RÜCKFRAGE zu RÜCKFRAGE
  schließt sich dann in seiner Hand.
- **Kap 26:** Kael gehört selbst zur Vermeidung (`kanon.md:L29`). Der Absatz sagt nur, dass die Vermeidung ihn
  „halten“ will (`:L329`). Wenn er sein eigenes Lager verlässt, ist das der Kern der Wahl. Der Absatz sollte es sagen.

### Die zwei Uhren

- **Uhr A (Rückzugsorte, Risse)** ist gut spürbar in Kap 14, 15, 22, 27 und 34. **In Kap 23–25 fehlt der Ort, den
  Kap 26 aufgibt.** „Der sichere Rückzugspunkt“ wird nie gezeigt, bevor er entfällt. Vorschlag: ihn in Kap 23 oder 24
  sichtbar machen (der Filter, oder was Rhys für Moros sichert), damit Kap 26 etwas Gesehenes opfert.
- **Uhr B (Abwärmebudget)** steht in Kap 16, 22, 31, 33, 35 und 36. Drei Schwächen:
  1. **Kap 28, der Purge, verbraucht nichts.** Das ist das Kapitel, dessen Signpost der Countdown ist.
  2. **Das Budget hat keine Größe.** „sinkt“, „fällt sichtbar“, „aufgebraucht“: Ein Hard-SF-Leser, dem Kap 1 Bit und
     Joule gegeben hat, bekommt hier keinen Zähler. Vorschlag: eine wiederkehrende, messbare Größe, in jedem AEGIS-Kapitel
     einmal.
  3. **Aufgebraucht in Kap 35, erloschen in Kap 39.** Dazwischen stottert AEGIS (`:L446`) und schweigt dann zwei Kapitel.
     Eine Uhr, die abläuft, und vier Kapitel lang geschieht nichts, entwertet sich. Q8 legt das Erlöschen fest auf
     Kap 39; das Rauschen als hörbarer Rest des Budgets (Abschnitt 2) hält die Uhr bis dahin hörbar. Abfrage nebenbei:
     Schritt 43 legt die Landauer-Hitze auf Beat 4 (`decisions/025-dramatica-is-the-recipe.md:L239`), das Treatment
     verbraucht das Budget in Kap 35 und lässt die Hitze in Kap 36 noch einmal kommen (`:L446`). Welches Kapitel trägt
     Beat 4?
- **Die Hitze als gemeinsame Währung ist der stärkste Brückenmechanismus des Plans:** Oblivions Löschen erzeugt sie
  (Kap 31), AEGIS bezahlt mit ihr. Sie würde auch die leeren Bridge-Kapitel füllen.

### Juna als volle Figur (W0)

- **Stark:** Kap 17 (sie hat sich den Ort genommen), Kap 25 (sie spricht), Kap 32 (sie verfolgt ihr eigenes Vorhaben),
  Kap 38 (sie verhandelt). Damit ist W0 über weite Strecken eingelöst.
- **Schwach:**
  - **Kap 26–31 ist sie Gefahrenobjekt.** Die Gefahr für Juna steht dreimal (`:L335`, `:L363`, `:L373`), worin die
    Gefahr besteht, nie. „Derselbe Zugriff, der schützt, gefährdet Juna“ (`:L360`). Was verliert sie, wenn der Purge
    sie trifft? Ohne Antwort ist die Spannung von Akt III abstrakt. Junas Ontologie soll offen bleiben
    (`development.json:L790`); die *Wirkung* auf sie kann trotzdem sichtbar sein, etwa an dem Ort aus Kap 17.
  - **Kap 30:** „und sie antwortet“ (`:L380`). Antwortet sie wissend, dass sie sich damit sichtbar macht? Dann ist der
    Preis ihr Entschluss, nicht nur Kaels Folge.
  - **Kap 33 nimmt Kap 25 zurück.** „Beide wissen, was sie wollen, und keiner sagt es“ (`:L411`), nachdem sie in Kap 25
    spricht, wo sie früher schwieg (`:L319–L320`) und ihr Need „sprechen statt schweigen“ ist (`kanon.md:L27`). Bewusster
    Rückfall unter Druck, oder Versehen? Wenn bewusst, braucht der Leser den Grund.
  - **Kap 34:** Kael trennt die Verbindung selbst (`:L421`). Was Juna dazu tut, sagt der Absatz nicht. Widerspricht sie,
    ist der Schnitt die Lüge „Wer mir nah ist, wird verletzt“ *gegen ihren Willen*, und das Kapitel wird härter.
  - **Junas Frist aus Kap 25 wird nie eingelöst.** „Die Trennung in ihrer Gegenwart läuft noch, und sie wird bald
    entscheiden“ (`:L321`). Danach entscheidet sie in keinem Absatz. Ihr Bogen auf der Karte endet „heute droht die
    Trennung aus Liebe“ (`kanon.md:L27`). Vorschlag: Ihre Entscheidung fällt irgendwo zwischen Kap 32 und 38, und sie
    ist ihre. Kap 38 darf sie offen lassen, aber dann als Entscheidung, die sie offen lässt.

### Druckabfall und Unschärfe

- **Kap 19–23** (siehe oben) ist der eine echte Durchhänger. Die Ideen sind da, nur trägt sie niemand, dem der Leser
  folgt.
- **Kap 33–39 sind die Handlungen Platzhalter:** „eine praktische Aufgabe“ (`:L410`), „eine begrenzte gemeinsame
  Handlung“ (`:L434`), „eine begrenzte nächste Handlung“ (`:L464`), „eine alltägliche Aufgabe“ (`:L470`). Vier
  unbenannte Tätigkeiten im Höhepunkt und in der Auflösung. Vorschlag: **eine einzige Aufgabe**, die durch alle vier
  läuft. Am nächsten liegt der Ort (gewollt 4, hergegeben 11, genommen 17, geteilt 33), oder die Zuweisung aus Kap 1,
  die in Kap 39 nicht auf null steht.
- **Kap 31** gibt dem Leser die Lösung vier Kapitel vor dem Pivot: „Das Löschen selbst lässt sich wählen“ (`:L389`).
  OS·Conceiving verlangt den Einfall, aber `development.json` warnt für Kap 18: „Oblivions Pivot nicht vorziehen“
  (`development.json:L676`). Operation: Der Einfall ist der Teil des Signals, der in der Hitze verloren geht. Der Leser
  hat ihn gesehen, Kael nicht mehr, und Kap 35 muss ihn wiederfinden.
- **Unerklärte Wörter:** „Drachenkampf“ (`:L444`), „Rauschen“ (`:L458`), „Er bleibt im Garten“ (`:L372`, unklar, ob er
  zurückbleibt oder ankommt). Im Treatment harmlos, in der Prosa braucht jedes einen Gegenstand.
- **Lose Fäden:** Argus findet einen echten Widerspruch, „und niemand will ihn hören“ (`:L275`). Danach kommt Argus
  nicht mehr vor, bis zum Wir. Die linke Hand (Kap 14) kommt nicht wieder, auch nicht im Spiegel von Kap 39. Beide
  warten auf eine Einlösung oder auf deine Entscheidung, dass sie offen bleiben.

## 4. Wissen über die Nähte (kurz)

| nach Kap | Kael weiß | der Leser weiß zusätzlich | was nicht mehr geht |
|---|---|---|---|
| 14 | KW1 ist weg | — | KW1, die linke Hand |
| 17 | Juna lebt ohne ihn weiter | — | das wartende Gegenüber |
| 18 | die Nacht von innen | das Cluster der Genesis schimmert | das Datum der Nacht |
| 22 | — | AEGIS erkannte 734 einen Satz lang | KW2 |
| 26 | er verlässt die Ordnung | — | der sichere Rückzugspunkt (nie gezeigt) |
| 30 | Juna antwortet | — | ihr Schutz durch Unwissen |
| 31 | — (Signal verloren) | das Löschen ist wählbar | ein Teil des Signals |
| 34 | er hat geschnitten | — | eine Möglichkeit der Beziehung, der Schutz der Abwehr |
| 35 | die zehn Jahre | AEGIS' Budget ist leer | die Amnesie |
| 39 | der Tag ist nicht falsch | AEGIS ist plural | die volle Null |

Offen bleibt in dieser Tabelle, was Kael über 734 erfährt. Kap 22 sagt es dem Leser vielleicht, Kael nie ausdrücklich.

## 5. Die Stellen, die **neu** sind

| Kap | Stelle | Urteil |
|---|---|---|
| 17 | Juna hat sich den Ort genommen (`:L241–L242`) | **Tragend.** Macht IC·Progress konkret und gibt Juna eine eigene Tat ohne Kael. Annehmen empfohlen |
| 18 | Lia hält einen Rest fest (`:L252`) | Gut, solange Kaels Abstieg die Wahl des Kapitels bleibt. Die Rettung mit Lia gemeinsam, nicht an seiner Stelle |
| 18 | Das Datum der Nacht ist gelöscht (`:L256`) | Konkreter Preis. Offen: Kommt das Datum in Kap 35 zurück? Dann ist es ein Pfand, sonst nur ein Verlust |
| 20 | Zwei Zugänge, Kanal und Weg zum Rest (`:L273`) | Bindet 19→20 sauber. Stärker, wenn Kael zwischen ihnen wählt (Abschnitt 3) |
| 25 | Juna spricht, wo sie früher schwieg (`:L319–L320`) | **Tragend**, trifft ihr Need genau. Erzeugt aber den Widerspruch zu Kap 33, den du klären solltest |
| 33 | Die Aufgabe an Junas Ort, sie lässt ihn hinein (`:L410`) | Starke Einlösung des Ortsmotivs. Die Aufgabe selbst ist noch leer; und dass sie ihn hineinlässt, verträgt sich schlecht mit dem gemeinsamen Schweigen derselben Szene, außer das Hineinlassen *ist* ihr Sprechen |
| 39 | Etwas steht nicht auf null, der Tag ist nicht falsch (`:L474`) | **Stärkster Schluss im Plan**: löst Kaels Lüge und spiegelt Kap 1. Risiko: zu glatt, wenn das „etwas“ beliebig bleibt. Es sollte das Ding aus der durchlaufenden Aufgabe sein |

## Was du entscheiden kannst

1. **Kap 19–23:** Soll Kael in Kap 20 entscheiden, welcher Zugang geschützt wird, damit der Zerfall der Lager seine Tat
   ist? Und in Kap 23 der Wunsch für Moros seiner sein?
2. **Kap 35:** Hört Oblivion von selbst auf, oder auf Kaels Nicht-Bestätigung hin, die RÜCKFRAGE von Kap 13 nach innen
   gewendet?
3. **Kap 34–36:** Widerspricht Juna dem Schnitt, und ist sie es, die in Kap 36 wieder verbindet?
4. **Uhr B:** Kostet der Purge in Kap 28 Budget, bekommt das Budget eine Größe, und ist das Rauschen in Kap 37–38 AEGIS'
   Sterben?
5. **Die Archetypen:** Bleiben die vier Menschen und Sophia, LogOS, Kairos ab Kap 14 stumm, oder gehen ihre Funktionen
   an jemanden über?
6. **Junas Frist aus Kap 25:** Entscheidet sie über die Trennung, und in welchem Kapitel?
