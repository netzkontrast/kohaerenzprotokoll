# Rules — the testbed's results

> Rules — a rule, a constraint or an invariant the document states, with the sentence that states it.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: GOAL.md: the plot model as checkable rules. A rule the documents state — what a system may never do, what must hold
> before something can happen — is a checkable statement, and no relation of the graph carries it.
> measured against: the rules a person lists in the wiki's records and the plot pages; a rule whose subject resolves to a wiki term is the attachable subset. A quote is placed by read.py --find (P26).
> may not: enforce a rule, check one against the novel, or say two rules conflict — that is read by a person; a rule is a P_HE_RULE proposal
> retire when: on three documents a person keeps no rule that the wiki's records do not already hold

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/rules-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.059, 21.6 s. **5 rows**: 5 candidates, 0 refused, 0 duplicates.

Beside the Haiku pilot of 2026-09-30 on this document: the candidates stand on 4 lines here and 5 there, 1 of them the same.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Das | der Leser im realen Leben unterbrochen wird | if_then | asserts | Das passiert immer dann, wenn der Leser im realen Leben unterbrochen wird | 20 |
| 2 | relation_reading | candidate | Kael | zerfällt die Welt in Textfragmente oder unklare Schemen | if_then | asserts | Wenn Kael zu schnell rennt oder in Regionen vordringt, die noch nicht „beschrieben“ wurden, zerfällt die Welt in Textfragmente oder unklare Schemen. | 34 |
| 3 | relation_reading | candidate | System | der Verstand des Beobachters (des Lesers) an seine eigenen kognitiven Grenzen stößt | if_then | asserts | Wenn das System unentscheidbar wird, liegt das daran, dass der Verstand des Beobachters (des Lesers) an seine eigenen kognitiven Grenzen stößt. | 35 |
| 4 | relation_reading | candidate | Die Welt | existiert nur so weit, wie der Leser sie sich vorstellen kann | only_if | asserts | Die Welt existiert nur so weit, wie der Leser sie sich vorstellen kann. | 35 |
| 5 | relation_reading | candidate | er | aufhören zu atmen | if_then | asserts | Wenn der letzte Punkt gesetzt ist, wird er aufhören zu atmen. | 48 |

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
