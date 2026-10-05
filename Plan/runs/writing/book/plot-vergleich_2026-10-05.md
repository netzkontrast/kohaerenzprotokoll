# Zwei Ausführungen des Plots im Vergleich (2026-10-05)

**Auftrag des Autors:** „compare the second Plot draft to your own“.

**Verglichen werden:**
- **Meine Ausführung:** `scene-architecture_akt-1_2026-10-05.md`, `scene-architecture_akt-2_2026-10-05.md` und
  `ereignis-wissen_akt-1_2026-10-05.md`, also Kap 0–26.
- **Die zweite Ausführung (D2):** `Plan/storyform/development.json` aus PR #170, also Kap 0–26 sowie 28, 32, 34, 35,
  38 und 39.

Beide sind Vorschläge, kein Kanon. Die Storyform geht vor (Schritt 38).

## Was D2 ist

D2 ist meine Liste, umgeschrieben in eine einheitliche Form: Ziel, Widerstand, Handlung, Wende, Preis, Wissen, Leser,
Folge, Zeit, Offen. Die Ziele sind fast überall meine, oft wörtlich (Kap 1, 3, 5, 9, 13, 14, 15, 26). D2 ist keine
unabhängige zweite Lesung, sondern eine Bearbeitung. Wo beide übereinstimmen, ist das keine Bestätigung.

## Was D2 besser macht

| Punkt | Kapitel | Gewinn |
|---|---|---|
| **eine Preisspalte in jedem Kapitel** | alle | Jede Wende kostet etwas Benennbares. Das ist die Spirale über den Preis, durchgehend |
| **konkrete Aufgaben** | 19 Bergung, 20 zwei Zugänge schützen, 24 Filter | Das antwortet auf die Durchsicht von #169: Der Streit der Anteile läuft während einer Handlung |
| **ein stärkeres AEGIS** | 0, 6, 16, 22, 28 | Seine Maßnahmen gelingen und kosten Gedächtnis („Ein Schaden wird verhindert“, Kap 6). Das passt zu B-Costs Memory, der Unique Ability Control und der Uhr |
| **eine eigenständige Juna** | 4, 17 | Sie handelt aus eigenem Willen („Folge einer Entscheidung, die Juna ohne seine Zustimmung getroffen hat“, Kap 17), nach W0 |
| **Hilfe durch andere** | 7, 9 | Kael muss jemanden um Hilfe bitten; Verlässlichkeit wird geteilt |
| **Akt III und Vortex angelegt** | 28, 32, 34, 35, 38, 39 | Ein erster Faden über Kap 26 hinaus |

## Was D2 verliert

| Punkt | Kapitel | was fehlt |
|---|---|---|
| **das Konkrete** | 2, 9, 15, 21, 23 | Die Bank, die noch einmal gelöscht werden müsste; 21,0 °C; „vergisst die Zahl der Schritte“; Silas' „Bin ich echt …“; Rhys und Moros. D2 schreibt „ein Mensch“, „eine Möglichkeit“, „eine Strategie“ |
| **die Anteile mit Namen** | 14–26 | Wer handelt, steht in `anteile.json`, aber D2 nennt es selten. Die Szenen verlieren ihre Träger |
| **der Mechanismus der Ereignistabelle** | 1, 2, 6, 12 | Drei Löschziele, die bis Kap 12 eins werden; die Frist 06:10 wird zur Prüfung bis zum Wartungsfenster. D2 hat in Kap 2 eine andere Probe („Register gegen einen Gegenstand vor Ort“) und keine durchgehende Frist |
| **dein Preis in Kap 14** | 14 | Die linke Hand (Schritt 39) ist zu „eine verfügbare Möglichkeit entfällt“ verallgemeinert |
| **die Uhren** | — | Das Abwärmebudget (Schritt 43) kommt in D2 nicht vor; D2 entstand vorher |

## Wo D2 einer Entscheidung widerspricht oder nachziehen muss

- **Kap 35:** „AEGIS bleibt bei seiner Ordnung und kollabiert“. Nach Schritt 43 läuft B bis Kap 39, und dort erlischt
  AEGIS-monolithisch und wird plural. „Kollabiert“ in Kap 35 muss ein Teil-Kollaps sein, sonst kollidiert es.
- **Kap 39:** Der vierte Schritt der Genesis ist eingetragen (Abgleich W12); die B-Seite fehlt (die Notiz von
  `storyform.py`).
- **Storypoints:** 39 gewobene Stränge haben keinen Verweis (die Notizen von `storyform.py`).

## Was zusammen das Stärkste wäre

Die **Form von D2** (Preis, Aufgabe, Wissen, die Stärke von AEGIS, Junas Eigenständigkeit) mit dem **Konkreten
meiner Liste**: Namen der Anteile, Zahlen, die Bank, die Mechanik der drei Löschziele und die Frist bis zum
Wartungsfenster. Dazu die Uhr von B (Abwärmebudget) als Spalte für Akt II und III. Das ergäbe eine Ausführung in
`development.json`, die die Szenenlisten ersetzt. Das ist deine Wahl.
