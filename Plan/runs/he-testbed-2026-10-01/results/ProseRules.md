# ProseRules — the testbed's results

> ProseRules — a rule for how the book is written — voice, diction, device, lock, formatting, ban — with its scope and the sentence.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the plan's rulebook (Phase 2d: the prose rules the author keeps, each with its chapter range and a mark for whether code can check it), GOAL.md 5.4's
> discipline table and the drafting brief's R-1 to R-10, all of which count as proposals; and writing-skills rule 4: a designed crack is not a slip,
> so the line-editor, copy-editor and continuity-editor each take a list of pre-cleared devices from the rulebook, and until it exists ask the author.
> measured against: the rulebook once the author has decided it; until then, a rule whose subject and constraint stand inside its quote is the precise subset. A quote is placed by read.py --find (P26).
> may not: clear a device, keep a rule or say a rule is decided — the rulebook is the author's; a rule here is a P_HE_PROSERULE proposal; nor write a line of prose to show a rule
> retire when: on three documents the author's rulebook keeps no rule offered

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/proserules-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0661, 26.8 s. **4 rows**: 4 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | den finalen Twist | müssen wir subtile „Glitch-Momente“ und systemische Hinweise einbauen | structure | asserts | Um den finalen Twist vorzubereiten – dass Kael die Manifestation des Lesers ist und seine Welt mit dem Zuklappen des Buches stirbt –, müssen wir subtile „Glitch-Momente“ und systemische Hinweise einbauen. | 13 |
| 2 | relation_reading | candidate | Kapitel 39 | beschreiben, wie Kael spürt, dass die Aufmerksamkeit schwindet | structure | asserts | In Kapitel 39 müssen wir beschreiben, wie Kael spürt, dass die Aufmerksamkeit schwindet. | 48 |
| 3 | relation_reading | candidate | das „Du“ | in Schlüsselmomenten | pov | asserts | Nutze in Schlüsselmomenten das „Du“. | 53 |
| 4 | relation_reading | candidate | AEGIS-Protokolle | Kursivschrift | format | asserts | Nutze Kursivschrift für AEGIS-Protokolle, die den „Beobachtungsstatus“ abfragen. | 54 |

## `2026-09-14-kap25-vertiefung-md`

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.1713, 66.7 s. **17 rows**: 11 candidates, 6 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Kap 25–26 | Schleier-Disziplin | structure | asserts | Canon §0 Schleier-Disziplin verlangt genau das für Kap 25–26 | 21 |
| 2 | relation_reading | candidate | Juna | nie Subjekt, nie Name, nie Körper, nie Stimme | diction | asserts | R-10 Juna nie Subjekt, nie Name, nie Körper, nie Stimme | 47 |
| 3 | relation_reading | candidate | Direktiven | ohne Metapher, Moral, Affekt | diction | asserts | R-8 Direktiven ohne Metapher, Moral, Affekt | 47 |
| 4 | relation_reading | refused: surface absent from document | Vielheit, Kapitel 25–26 | kanonisch gefordert, ohne klinisches Vokabular, ohne Header, ohne Sprecher-Tags | device | asserts | Vielheit wird benannt, **kanonisch gefordert** für 25–26, ohne klinisches Vokabular, ohne Header, ohne Sprecher-Tags | 47 |
| 5 | relation_reading | candidate | kaltes Ozon | nur in der Abmeldeszene, Wärme dort nicht | structure | asserts | kaltes Ozon **nur** in der Abmeldeszene, Wärme dort nicht | 47 |
| 6 | relation_reading | refused: surface absent from document | Mikrocues in der Handszene | drei, am Limit, nicht darüber | structure | asserts | drei Mikrocues in der Handszene, am Limit, nicht darüber | 47 |
| 7 | relation_reading | candidate | Szene | ein Konzept je Szene | structure | asserts | ein Konzept je Szene | 47 |
| 8 | relation_reading | candidate | Genesis-Echo | max. ein Genesis-Echo je Szene | structure | asserts | max. ein Genesis-Echo je Szene | 47 |
| 9 | relation_reading | candidate | Kap-0-Zitate | keine wörtlichen Kap-0-Zitate | diction | asserts | keine wörtlichen Kap-0-Zitate | 47 |
| 10 | relation_reading | candidate | Ein-Falschheits-Regel | eine objektive Falschheit | structure | asserts | Ein-Falschheits-Regel: **eine** objektive Falschheit | 47 |
| 11 | relation_reading | candidate | Restzahl-Anstieg | bewusst erklärbar gehalten | number | asserts | der Restzahl-Anstieg ist bewusst **erklärbar** gehalten | 47 |
| 12 | relation_reading | candidate | Kaels Signatur | bricht nur dort, wo ein Wechsel gemeint ist | pov | asserts | Kaels Signatur bricht nur dort, wo ein Wechsel gemeint ist | 47 |
| 13 | relation_reading | candidate | Benennungslock | gilt für Kap 1–13 | lock | asserts | Der Benennungslock gilt für Kap 1–13. | 55 |
| 14 | relation_reading | refused: surface absent from document | Schleier-Benennung in Kap 25–26 | offen benannt | structure | cites | Canon verlangt „offen benannt | 56 |
| 15 | relation_reading | refused: surface absent from document | Schleier-Benennung (Kap 25) | der Satz „Hier sitzt mehr als einer.“ mitten in der Handszene | lock | hedges | Gesetzt ist der Satz „Hier sitzt mehr als einer. | 56 |
| 16 | relation_reading | refused: surface absent from document | Template-Kopf | keine Änderungen außer status | format | cites | Der Drafting-Brief verbietet Änderungen am Kopf außer status. | 58 |
| 17 | relation_reading | refused: quote not placed | Einheit Station 7 | bleibt namenlos („Einheit“), wie es Akt I verlangt | diction | cites | bleibt aber namenlos („Einheit“), wie es Akt I verlangt |  |
