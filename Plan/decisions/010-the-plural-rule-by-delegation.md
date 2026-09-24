# 010 — The plural rule's reach, decided by the session on the author's delegation

**Date:** 2026-09-24 · **Decided by:** this session, because the author said „Do what IS Best" · **Status:** chosen; a scored rule in `scripts/pairs.py`, not part of `fold()`; reversible by the author at any time

## What was chosen

`NOW.md` held the question of how much morphology `fold()` may claim, and said
the next improvement on one-term-or-two is a rule, not a model. Asked what DSPy
could learn in this project, the session measured such a rule offline first.
The author answered the offer to record it with „Do what IS Best". So the reach
is decided the way decision 008 decided: on the conservative side, sending
nothing out of the container and merging nothing in the pipeline that was not
merged before.

`pairs.RULES["plural"]` is `fold()`, plus the rule the ledger already states in
words — J4, „a German plural ending is not a term boundary", and J23, „an English
plural -s is never a term boundary" — within this reach:

- an ending from a closed set, `-s` `-es` `-e` `-en` `-n`, appended to the whole
  shorter surface after folding;
- `-n` only after `-e` (`Anomalie`/`Anomalien`, `Erasure-Welle`/`Erasure-Wellen`);
- a stem of at least four letters (`Riss`/`Risse` needs four);
- the ending written in lower case in the longer surface.

It is a row on the ledger and the rule `pairs.py run --rule plural` asks before a
model is asked anything. **It is not in `fold()`.** Reconciliation, the index,
the relations and `graphrag.py`'s seeding decide exactly what they decided
before.

## What it measured, 2026-09-24

- **41 of 57 labelled pairs, against `fold()`'s 33.** No false merge: all 29
  pairs the ledger calls two terms stay apart. No canary merged.
  `Plan/runs/baselines.jsonl`, `rule:plural`; `python3 scripts/baseline.py
  compare one-term-or-two --floor rule:fold` says `ok`.
- **No merge between two pages.** The 160 folded surfaces of the 92 pages in
  `Wiki/index.json` stay on their pages.
- **23 new merges among all 13 candidate lists** (1,392 terms, 1,338 distinct
  after folding), read one by one, and every one a singular and its plural:
  `Alter`/`Alters`, `Erason`/`Erasonen`, `Glitch`/`Glitch(es)`,
  `Trennungsprotokoll`/`Trennungsprotokolle` and nineteen like them.

What it leaves for a model is 16 pairs the person called one term. Read by the
session, seven carry a recorded rule a program could state: a slash between
names the wiki already has (J6, J14, J34, J43), an acronym and the expansion its
sentence gives (J60), a numbered instance of a class (J26, J37). The other nine
were decided from the passage (`Basisrealität`/`Externe Ebene`,
`Therapie-Schnittstelle Gamma`/`Alpha`), and `pairs.py`'s program is given only
the two surfaces. That is the next thing to change before a model run can learn
them, and it is not a model either.

## What was rejected, and why

- **`-er`.** It also makes a noun of a verb: `Spiel` is in 61 landed documents
  and `Spieler` in 13, a game and a player. `("Spiel", "Spieler")` is now a
  canary in `selftest.MUST_NOT_MERGE`.
- **An ending in any case.** `fold()` spells the Guardian `LogOS` `logos`, so a
  case-blind `-s` would put `Logo` — a visual logo, „AEGIS/Cerberus-Logo?", in 3
  documents — on the Guardian's page. `("Logo", "LogOS")` is now a canary. The
  lower-case test is what keeps them apart.
- **`-n` after `-er` or `-el`, and the canary that was meant to guard it.**
  `Alter`/`Altern` was going to be a canary, and the corpus refused it:
  „der Konflikt zwischen den Altern", „Kaels dissoziierten Altern". Here
  `Altern` is the dative plural of `Alter`, one term. The ending stays out
  anyway, so a person still decides the pair — the safe direction, the one
  `fold()` has always missed in.
- **A stemmer.** It merges `Negentropie` with `Entropie`, which is why `fold()`
  is not one. This rule never removes anything from the shorter surface.
- **Umlaut plurals** (`Stadt`/`Städte`). No instance in the ledger (P4).
- **Putting the rule into `fold()` now.** That changes what every reconciliation
  merges by lookup, and the author named `fold()`'s morphology as the question.
  The ledger row is the evidence that question now has, not its answer.

`pairs.py selftest` shows the veto failing: the rule with `-er` added is vetoed
on `Spiel`/`Spieler`, and the rule without the lower-case test on `Logo`/`LogOS`.
Before this decision the four canaries were all out of any plural rule's reach,
so nothing could have shown the veto fire on one.

## What would change our mind

- **A judgement that calls a plural pair two terms.** The rule's row falls, and
  `pairs.py score --rule plural` names the pair.
- **A canary it merges.** The row is vetoed and `baseline.py compare` fails it.
- **The author**, adopting it into `fold()`, widening it to `Altern`, or taking
  it out.
