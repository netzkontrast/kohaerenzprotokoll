# 015 — Decision sheets are cross-read first and put to the author in rounds

**Date:** 2026-09-30 · **Decided by:** the author, four answers to `AskUserQuestion`
(each the session's recommended option) · **Status:** in use

## What was asked

> Überleg mal wie wir den Prozess rund um die w1-wirgendwas entscheidungsblätter gemeinsam angehen wollen … wie sähe ein guter Prozess aus diese auch gegeneinander und mit passenden skills zu analysieren und so aufzubereiten das wir beide bequem via askuser Tool daran arbeiten können - welche Fragen sind wirklich zu klären?

The proposal is `Plan/concept/entscheidungsprozess_2026-09-30.md`.

## What was chosen

- **Cross-read first.** Before a round the session checks the sheets against each other
  (dependencies, conflicts between recommendations, records and reported locks) and puts to
  the author only the key questions, reported locks to confirm, and a few switches.
- **Unanswered means `PROVISIONAL` with an `ALT` line.** A recommendation the session carries
  as a working assumption is marked in the text and never counts as decided.
- **One decision file per round**, in `Plan/decisions/`, plus the sheet's `status` and the
  record the answer closes where there is one (C6 and C9 are the pattern).
- **Sheets get a front-matter head** (`id`, `status`, `hängt_ab_von`, `schaltet_frei`, `kapitel`,
  `frage_art`, `auslöser`, `empfehlung`). Provisional: the fields come from eleven sheets, not
  from a rule. **A checking script is proposed only after the first round has used the fields.**

## What was rejected

Sheet by sheet as before; stopping when a sheet is unanswered; recording only in the sheets
or only in the records; building the head and the script before use (P3, P4).

## What would change our mind

A round in which the head fields were not used, or a cross-read that found nothing the sheets
alone did not show. Either retires the field or the step.
