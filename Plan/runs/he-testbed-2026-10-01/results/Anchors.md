# Anchors — the testbed's results

> Anchors — a motif or fact the source plants, echoes, pays off or closes, with the place and the sentence.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: GOAL.md 4.3 (`Anchor`, `ForeshadowStrand`; edges `sets_up`, `pays_off`, `echoes`) and the plan's anchor ledger (Phase 2c: planted, echoed, paid
> or closed). The continuity-editor's deferred reveals and the developmental-editor's payoff test both need it; the stated graph has none,
> and no mechanical relation can tell a plant from a mention.
> measured against: the anchors a plan names (a telephone silence, a number, a half-sentence, a warmth); a pair whose anchor and place stand inside its quote is the precise subset. A quote is placed by read.py --find (P26).
> may not: decide that a plant is paid or that a payoff is missing — every anchor planted is paid or deliberately left open is the author's gate, read by a person; an anchor here is a P_HE_ANCHOR candidate
> retire when: on three documents a person keeps no anchor beyond what the plan's own motif list holds

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/anchors-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0492, 15.7 s. **0 rows**: 0 candidates, 0 refused, 0 duplicates.

Staging refused the run: `empty or invalid candidate list: not a successful extraction`

Beside the Haiku pilot of 2026-09-30 on this document: the candidates stand on 0 lines here and 6 there, 0 of them the same.

The model returned no row on this document.

## `2026-09-14-kap25-vertiefung-md`

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.1577, 56.2 s. **10 rows**: 7 candidates, 3 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Canon §0 Schleier-Disziplin | Kap 25–26 | pays_off | denies | Canon §0 Schleier-Disziplin verlangt genau das für Kap 25–26; die alte Fassung löste das nicht ein. | 21 |
| 2 | relation_reading | candidate | ihr Vorbeigehen an der Tür | Kap 26 | pays_off | asserts | ihr Vorbeigehen an der Tür in Kap 26 ist vorbereitet | 22 |
| 3 | relation_reading | candidate | Canon-Weltanker | Kap 25 | pays_off | asserts | Das löst den Canon-Weltanker für Kap 25 ein (KW3, Wartungsschächte, Anker 734 dritte Wiederkehr) | 23 |
| 4 | relation_reading | candidate | die einrastende Verkleidung | Kap 24 | echoes | asserts | Hook-in aus Kap 24 explizit (die einrastende Verkleidung) | 25 |
| 5 | relation_reading | candidate | die Restzahl steht nach Schichtende bei 34 statt 31 | Kap 26 | plants | asserts | neuer Hook-out: die Restzahl steht nach Schichtende bei 34 statt 31 und wird morgen früh nicht bei sechs stehen → trägt direkt in Kap 26 | 25 |
| 6 | relation_reading | refused: quote not placed | Wärmespur | einer ozonfreien Szene | echoes | asserts | Wärmespur nur als Rückverweis („die vier Abende“) in einer ozonfreien Szene |  |
| 7 | relation_reading | candidate | die Instanz | Kapitel 14–26 | withholds | asserts | Die gedrafteten Kapitel 14–26 benennen die Instanz trotzdem nirgends leserseitig | 55 |
| 8 | relation_reading | refused: quote not placed | das Fehlen des Klicks | Vortex 1 Beat 3 | plants | asserts | Kanonischer sensorischer Anker von Vortex 1 Beat 3 ist „das Fehlen des Klicks“ global. |  |
| 9 | relation_reading | refused: surface absent from document | Einheit Station 7 | Akt III (Kap 27/28) | echoes | asks | Trägt sie in Akt III weiter (Kap 27/28) oder bleibt sie eine Delta-Sieben-Figur? | 59 |
| 10 | relation_reading | candidate | KW3 | Kap 25 | pays_off | asserts | Kap 25 löst KW3 jetzt | 60 |
