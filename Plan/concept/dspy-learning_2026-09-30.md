# DSPy in der Lern-Pipeline — wo Optimierung hier etwas lernen kann

**Konzept, 2026-09-30.** Anlass: „Denke über /dspy nach — und wie sich das einsetzen lässt in
der Pipeline fürs Learning", dann „ggf. Promptoptimierung für OpenRouter und Jules?".
Grundlage:
- `.agents/skills/dspy`;
- die Läufe vom 2026-09-25 (`Plan/concept/dspy-optimization_2026-09-25.md`);
- was heute gebaut wurde: `ask.py`, `askdb.py`, `askextract.py`, `aliases.py`.

Nichts hier ist gelaufen. Jede Zahl unten ist eine frühere Messung und nennt ihre Datei.
Jede Schätzung ist als Schätzung markiert.

## Der Grundsatz, der die Auswahl bestimmt

DSPy lernt nur, wo es drei Dinge gibt:

- eine **Metrik, die fallen kann**;
- **Beispiele mit Gold**, das nicht dieselbe Hand geschrieben hat, die bewertet wird;
- ein **Budget**, das die Messung trägt.

Der 25.09. hat gezeigt, was fehlt, wenn eines davon schwach ist. Ein Free-Modell schlug den Boden
nach Score, 0,741 gegen 0,698, und verschmolz dabei siebzehn Paare, J5 `Negentropie`/`Entropie`
darunter. Deshalb bekommt jede Metrik unten einen **Veto-Term**, der nie im Mittel verschwindet
(P15, P23).

Bei Prompt-Optimierung geht es hier fast immer um den **Anweisungstext** (die Regelkarte, das
Briefing, die Präambel), nicht um Few-Shot-Demos. Dafür ist GEPA gebaut, oder
`gepa.optimize_anything` für einen Text ohne DSPy-Programm (`references/text-artifacts.md`).
Jede Ausgabe von `ask.verify()` trägt schon einen **Grund in Worten**, etwa „the words stand on
L412, which the pack did not send". Genau diesen Text braucht GEPAs Reflexion.

## Fünf Stellen, nach Nutzen und Preis

### 1. Die `ask`-Regelkarte je Backend — die Antwort auf „OpenRouter"

**Was optimiert wird:** `RULES` in `scripts/ask.py`. `build_pack` nimmt sie seit heute als
Parameter, also ohne Umbau. Je Backend eine Karte: ein gepinntes Free-Modell über `route/…`,
dazu `claude-cli/haiku`.

**Die Metrik**, aus `verify()`, ohne zweites Urteil:

- **Präzision** = platzierte Zitate / alle Zitate. `unresolved` und `outside-window` sind Fehler.
- **Gold-Treffer** = die Gold-Zeilen des Records, die eine platzierte Behauptung trifft, geteilt
  durch die Gold-Zeilen, die das Paket überhaupt gesendet hat (`meta.shown`). So misst der Term
  die Antwort und nicht das Routing.
- **Veto:**
  - `schema-invalid` oder `unparsed` zählen als „could not score", nie als 0 und nie als 1;
  - ein Zitat, das auf keiner Zeile des Dokuments steht (`unresolved` mit „no single line"),
    ist eine Erfindung und wird getrennt gezählt, nie gemittelt.

**Die Beispiele:** die 24 Bench-Fälle, jeder Record vorher aus dem Graphen entfernt (`ask.py
bench`). Dazu die fünf gelandeten Antworten als Anschauung, nie als Gold.

**Einschränkung:** Record und Seiten schrieb dieselbe Hand, derselbe Vorbehalt wie bei
`graphrag.py bench`. Deshalb zählt die Präzision voll und der Gold-Treffer nur als zweiter Term,
denn Regel 10 gilt: Was im Record fehlt, ist nicht falsch.

**Das Budget, geschätzt:**

- Ein Paket hat 60.000 Zeichen, etwa 15.000 Token.
- GEPA `light` braucht für einen Prädiktor rund 380 + 4 × Valset Metrik-Aufrufe (Fakt 5 im Skill).
- Mit Free-Modellen, 6–98 s pro Aufruf (gemessen am 25.09.) und einem Tageslimit (veröffentlicht,
  nicht gemessen), ist das zu viel.
- Deshalb: **Pakete mit Budget 20.000** und **`max_metric_calls` 150**, fest angegeben.
- Aufteilung: 16 Fälle zum Trainieren, 8 zurückgehalten.
- Die Reflexion macht `claude-cli/sonnet` mit Denken; sie sieht die Paketauszüge unter
  Entscheidung 017.

**Zustimmung:** Entscheidung 017 deckt Pakete an Free-Modelle (`purposes.ask` in
`Plan/runs/route/consent.json`). Ein Optimierungslauf schickt dieselben Pakete, nur öfter. Dass das
noch ein Probelauf im Sinne von 017 ist, steht unten.

### 2. Jules — übertragen, nicht im Loop optimieren

Jules passt nicht in eine Optimierungsschleife:

- Eine Sitzung dauert Minuten bis Stunden.
- Sie hat ein Plan-Gate und läuft asynchron.
- Heute ließ eine ihre Arbeit in der VM (`recover_silent_fail`).

Deshalb zwei getrennte Dinge:

- **Die Antwortqualität** kommt von der Karte aus Punkt 1. Die kompilierte Karte geht per
  `raw.jules.json`-Weg an Jules, auf drei zurückgehaltenen Fällen, und wird mit demselben
  `verify()` gemessen. Das ist Transfer, gemessen, nicht angenommen.
- **Die Arbeitsweise:** Jules' Fehler sind prozedural, nicht sprachlich. Das Werkzeug ist nicht
  aufgerufen, die Arbeit liegt in der VM, der Branch fehlt. Dagegen helfen Regeln im Code, und
  die gibt es: `jules.py lint`, `verify`, `triage`.

Optimierbar wird die **Präambel** erst, wenn es 5 bis 20 **echte, festgehaltene Fehlschläge**
gibt. Das ist die Regel für Job 4 in `text-artifacts.md`. Heute gibt es einen. Deshalb: Jede
Jules-Sitzung schreibt ihr `triage`-Ergebnis in `Plan/runs/jules/ledger.jsonl`. Das ist der
Datensatz, und er kostet nichts.

### 3. Anfrage-Umschreibung — der größte Hebel für den Recall

Sechs der 24 Bench-Fälle finden **keinen Seed**. Ihre Titel sind Englisch (`knuckles`, `Flight`,
`blind spot`, `Be-er/Do-er`), die Oberflächen Deutsch. Der Recall liegt bei Dokument 0,27 und
Zeile 0,09 (`Plan/runs/ask/bench-2026-09-30-60000.json`).

Ein kleines Programm `Umschreiben(frage, oberflächen) → begriffe` wählt deutsche Begriffe aus der
**Liste der Seitenoberflächen**, als `Literal`, das Code baut. So kann es keinen Begriff
erfinden (Fakt 7).

- **Metrik:** der Paket-Recall aus `bench`, ohne Antwortmodell.
- **Gesendet werden** nur Frage und Oberflächen, so wie `pairs.py` Oberflächen sendet
  (Entscheidung 011); keine Dokumentzeile.
- **Preis:** Ein Paket zu bauen dauert rund 25 s, gemessen: 24 Fälle in 10 Minuten. Deshalb ist
  der erste Schritt `LabeledFewShot` oder `BootstrapFewShot` mit Leave-one-out, nicht GEPA.
- **Beiwerk:** Die zweisprachigen Glossen aus `Plan/runs/bilingual/stated.jsonl` sind schon
  Vorschläge dafür (`graphrag.py ask --gloss`). Die Umschreibung braucht sie als Baseline: Ein
  Programm, das die Glossen nicht schlägt, lernt nichts.

### 4. Alias-Lernen — `pairs.py`s Leiter für den Rest, kein zweiter Richter

Die Experimente in `aliases.py` sind heute gelaufen (`Plan/runs/aliases-2026-09-30/`):

- **Auf dem Ledger** sind nur die Regeln sicher: Plural mit P 0,929 und R 0,295. `gloss` erzeugt
  drei falsche Merges und trifft einen Kanarienvogel.
- **Auf Seitenpaaren** erreicht die Trigramm-Ähnlichkeit ab 0,736 R 0,241 ohne falschen Merge.

Für den Rest gibt es schon ein DSPy-Programm: `pairs.py`. BootstrapFewShot mit Haiku erreichte
0,884, mit einem falschen Merge (J74). Also:

- `aliases.py` fragt für den Rest nach Regeln und `chars` **das kompilierte Programm von
  `pairs.py`** (`final`). Es baut keinen eigenen Richter (P6).
- **Neu dazu:** die 133 positiven Seitenpaare als Trainingsmaterial, mit harten Negativen von
  anderen Seiten. Das verdoppelt die Positiven, ist aber wieder dieselbe Hand. Die
  Kanarienvögel bleiben Veto.
- **Das Ergebnis** sind `P_ALIAS_OF`-Kanten im Store: Vorschläge, getrennt von den belegten
  Kanten. Sie werden nie zu einem Merge, der Knoten zusammenlegt. Ein Merge bleibt das Urteil
  einer Person (`judgements.jsonl`). Die Vorschläge lassen nur zu, dass eine Anfrage über
  `Concept`-Knoten alle Schreibweisen findet, gekennzeichnet.

### 5. Extraktion — das Labor der Parallelsitzung

Die Metrik gibt es: `agree.py` (F1 und Anteil gehalten) gegen die Gold-Listen aus `gold.py`.
Optimierbar ist das Briefing (`Plan/briefings/extract.md`) als Text, über `optimize_anything`.

- **Nur mit Claude:** Keine Zustimmung deckt Extraktion über Free-Modelle, und Entscheidung 017
  gilt nur für `ask`.
- **Wer es führt:** Das gehört der Parallelsitzung (PR #120), deren Reader-Lab die Arme schon
  vergleicht. Jules läuft dort heute als ein Arm (Sitzung `11706769508284644788`). Hier kommt
  nur das Werkzeug her: `build_pack(rules=…, schema=…)` und `verify()`.

## Reihenfolge, empfohlen

1. **Jetzt, ohne Modell:** `ask.score(verify_result, gold, shown)` als Metrik mit Veto und
   Selbsttest. Der Fall, an dem sie scheitern muss: eine Antwort, die ein richtiges Zitat außerhalb
   des Fensters bringt.
2. **Die Umschreibung (3)**, Leave-one-out auf 24 Fällen. Sie ist billig, und eine gemessene
   Verbesserung hilft allen Backends.
3. **Die Regelkarte (1)** auf einem gepinnten Free-Modell: GEPA, 150 Aufrufe, 16/8.
   `baseline.py compare` gegen die handgeschriebene Karte als Boden.
4. **Transfer auf Jules (2)**, drei zurückgehaltene Fälle, dieselbe Metrik.
5. **Alias-Rest über `pairs.py` (4)**, sobald `P_ALIAS_OF` im Store steht.

## Was das nicht darf

- Eine optimierte Karte ändert nichts daran, was eine Antwort ist: eine Modell-Lesart, Tier
  `M-ask`. Jedes Zitat bleibt von Code platziert.
- Kein Score landet in `Sources/ask/`. Eine Antwort aus einem Optimierungslauf landet nur, wenn
  jemand sie landen lässt.
- Keine Karte wird zur Standardkarte, bevor `baseline.py compare` sie über dem Boden sieht, und
  zwar auf den zurückgehaltenen Fällen.

## Die eine Zustimmungsfrage, nach Entscheidung 018 selbst beantwortet

Ist ein Optimierungslauf mit rund 150 Aufrufen pro Free-Modell noch ein „Probelauf" im Sinne von
Entscheidung 017? **Ja.** 017 sagt für OpenRouter und Jules: „hier kannst Du frei experimentieren".
Ein Optimierungslauf ist ein Experiment: Er schickt dieselben Pakete wie ein einzelner Lauf, nur
öfter, und landet nichts von selbst.

Die Grenze bleibt, was 017 nicht deckt: Extraktion über Free-Modelle (Punkt 5). Der Autor kann
diese Antwort mit einem Wort zurücknehmen; dann bleiben die Schritte, die kein Paket senden.
