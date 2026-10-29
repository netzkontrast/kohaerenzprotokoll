# Pilot Kap 1, Szene 1 — run once by hand (2026-10-27)

The author's instruction of 2026-10-27: run the scene loop of decision 030 once, by hand, before any change to the
Schreibtisch; build only what this run shows is missing. This file is the run's ledger: the timings, the friction
as it happened, and what each friction entry led to. It is written as the run goes; nothing in it is a judgement of
the prose.

## Timings

Times are UTC, from the session's clock and from git. "Author time" is the time between a question put to the
author and the answer, not the author's working minutes, which the session cannot see.

| step | started | ended | note |
|---|---|---|---|
| session claimed, inputs read, briefing regenerated | 09:34 | 09:50 | the regenerated briefing differed only in its date |
| Weichen round 1 put to the author (W2, W3, W7, W5) | ~09:55 | 10:58 | four answers, all the recommended option; the time includes two worker restarts |
| answers recorded (`weiche.py answer`) | 10:58 | 11:00 | committed `d82c0d92`, pushed 11:39 |
| CI red on the stale briefing; defect found and fixed | 11:49 | 12:05 | see F6, F7 |
| Weichen round 2 put to the author (W28, W21, W20, SP) | ~11:10 | 12:03 | four answers, all the recommended option |
| answers recorded, rules carried into `regeln.jsonl`, briefing regenerated | 12:03 | 12:06 | 25 rules: 17 bestätigt, 1 verworfen, 2 ersetzt, 5 offen (L9, L12, L15a, L15c, W7a) |
| beats: scope and falsity asked, six beats proposed, author removed the Anschluss | ~12:20 | 18:28 | `manuscript.py beats 1 1`; the wait includes worker restarts |
| Szene 1 written, draft frozen (`szene-1/entwurf.md`, 779 words), both checks, two editor reports | 18:28 | 18:31 | `manuscript.py check 1 1`: 0 Fehler, 0 Rückfragen |

## Friction, as it happened

| # | where | what happened | led to |
|---|---|---|---|
| F1 | briefing § Offen | Option text is shown for 6 of the 11 Weichen; SP, W3, W5, W7 and W33 show only a recommendation letter. To put them to the author the session had to open each sheet. | Schreibtisch candidate: the options of every Weiche, read from the sheet's prose where it has no list |
| F2 | briefing § Offen | No Weiche carries the source lines it rests on; the author asked for them. The session took them from each sheet's quotations by hand. | Schreibtisch candidate: each open Weiche with the cited lines of its sheet |
| F3 | briefing § Offen | Eleven Weichen are listed because each sheet names the chapter, not because Szene 1 needs them: W17 and W18 concern Act II, W33 the method. The session had to sort them by hand to ask the scene's questions first. | Schreibtisch candidate: open Weichen ordered by what the scene needs, the rest marked as such |
| F4 | the app | The questions could not be put in the app: the website answers 503 until PR #198 is merged (decision 032), and the Schreibtisch offers a copyable answer prompt, not an answer. They were put in the conversation instead. | not built: the answer channel is decision 031's question; recorded here as the run's evidence for it |
| F5 | `weiche.py show` | For W3, W5 and W7 the tool lists no options; their options exist only as prose in the sheet. | same as F1 |
| F6 | after answering | Answering changed the briefing's inputs; nothing told the session to regenerate the briefing, and CI went red on `briefings, live`. | the loop's order: answer, then `brief.py kap N`, then commit — to be stated in the Schreibtisch's answer prompt |
| F7 | `brief.py` | **Defect.** An answered Weiche appeared under *Entschieden* only when its words named the chapter or a figure; W2 and W3, answered for Kap 1, and the older W12 were missing — from the one text a scene may be written from. | fixed in `brief.py`: every answered Weiche that touches the chapter stands under *Entschieden*; a selftest case that fails on the old rule |
| F8 | SP answer → `prose_rules.py` | The author's SP answer confirms the remaining locks "für Szene 1"; the rule register has no scope field, so a confirmation reads as for the whole book. The session confirmed only rules whose text fits Kap 1 and left L9, L12, L15a, L15c and W7a open rather than widen the author's words. Carrying an answer into the register is a second, manual step the author never sees. | Schreibtisch candidate: an answer that names rules shows which ones it confirms before it is recorded |
| F9 | briefing § Offen | W17, W18 and W33 stay open; none is needed for Szene 1, and the session did not put them (see F3). | not asked in this run; they remain open in the briefing |
| F10 | beats proposal | W28 („In Szene 1 steht der Abschnitt auf der Löschliste“) and W20 („Szene 1 braucht eine Zeile, die das zeigt“) are the author's answers in § Entschieden; the session proposed the beats from § Vorgeschlagen only, the author approved them, and the draft lacks both lines. Found by the continuity read, not by any check. | Schreibtisch candidate: the beats form lists every decided obligation that names the scene, beside the proposal |
| F11 | `continuity.py`, `prose_rules.py` | Both checks pass with 0 findings on a draft that misses two decided obligations: neither reads an answer's „Szene N braucht …“ clause. A green check here proves only the rules it encodes. | candidate check: an obligation that names a scene and no line of its prose answers it is a query |
| F12 | the draft | The woman's moving lips (`szene-1-das-licht.md:L82`) are not in the approved beats; the session added them. Named in the line-editor report, left for the author. | none — the author's mark decides |

## What follows

The author's answer on F10 (amend the beats, or keep them), then the author's marks and edits in the Schreibtisch, the
diff, and approval in the author's words. The Schreibtisch changes wait until the run is through.
