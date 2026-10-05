# NCP-Audit der Storyform-Dateien — 2026-10-05

**Auftrag des Autors (2026-10-05):** NCP-Audit, Weaving als Moments, NCP-3-Delta — „Alle drei". Durchgeführt nach dem
Audit-Pfad des `ncp-author`-Skills (Version 0.4.0, Schema 1.3.0, gepinnter Upstream `0b9ab12`).

## Was geprüft wurde

1. **Schema:** Der Validator des Skills (`scripts/validate.js`, ajv) prüft beide Dateien.
2. **Die semantischen Regeln §1–§6** aus `references/validation-rules.md`, mit einem Prüfskript dieser Sitzung:
   - §1.1 jede `perspective_id` löst auf, §1.2 jede `storybeat_id` eines Moments löst auf, §1.3 und §4.1 Throughline und
     Appreciation stimmen überein;
   - §2 jede Dynamik hat einen zulässigen Vektor;
   - §3.1 Sequenzgrenzen je Scope, §3.2 keine Kollision von (Throughline, Scope, Sequenz), §3.3 Beat und Appreciation
     stimmen überein;
   - §4.2 Story-Appreciations ohne Throughline, §4.3 holistische Aliase nur bei `holistic`;
   - §5 keine leeren Pflichtfelder, §6 der Status passt zum Stand.
3. **Quad, Dynamic Pairs, KTAD:** Das NCP kodiert sie nicht. Der Skill verweist dafür auf `dramatica-vocabulary`. Hier
   prüft das `scripts/dramatica.py` gegen die Tafel von 1995/1999 (R1–R8: Elemente unter ihrer Variation, Problem und
   Lösung als Paar, Focus/Direction als das andere Paar desselben Quads). `storyform.py` weigert sich, eine Storyform zu
   schreiben, die das verletzt. Jede NCP-Datei ist also aus einer geprüften Storyform erzeugt.

## Befund vor dieser Sitzung (Commit `0f303da1`)

| Prüfung | A | B |
|---|---|---|
| Schema | PASS | PASS |
| §1–§5 | keine Verletzung | keine Verletzung |
| §6.2 (draft → complete) | `players[]` leer, obwohl `a.json` vier Players hat | `players[]` leer, obwohl `b.json` zwei hat |
| Quad/Paare | gehalten (`storyform.py --check`) | gehalten |
| `storytelling` | keine Moments, keine Overviews | keine Moments, keine Overviews |

**Ein Befund, keine stille Korrektur:** Der Generator schrieb `players: []` fest, obwohl die Besetzung (Schritte 17–18)
in den JSON-Dateien stand. Ein NCP-Leser sah also keine Besetzung.

## Was danach geändert wurde

`scripts/storyform.py` schreibt jetzt zusätzlich:
- **Players** aus `players` (A: Kael, Juna, Selene, Oblivion; B: AEGIS, Kael) mit ihren OS-Elementen als `motivations`.
  `visual`, `audio` und `bio` tragen „offen“-Platzhalter, die §5 im Entwurf zulässt. Die Figurenkarten sind nicht
  bestätigt, und erfunden wird nichts.
- **Overviews** `Logline` und `Genre` (Schritt 22).
- **Moments** aus `weave.json` (Schritt 23): einen je Kapitel, das Stränge dieser Storyform trägt. Das sind 35 in A
  (Kap 0, 6, 16, 22, 28 und 40 tragen keinen A-Strang) und 16 in B. Jeder Moment nennt Akt, Reihenfolge, Route und Anker
  und verweist auf die Signpost-Beats seines Akts. `synopsis`, `setting` und `timing` sind „offen — das Treatment“.
  Entschieden sind nur Route und Stränge.

**Danach:** Schema PASS für beide, §1–§6 ohne Befund. Der Selbsttest von `storyform.py` prüft jetzt auch, dass das
Weaving Moments ergibt und kein Moment auf einen Beat zeigt, den es nicht gibt (§1.2).

## Was das Audit nicht sagt

- Der Status bleibt `draft`. Nach §6.1 wäre `complete` mit „offen“-Platzhaltern inkohärent.
- Ob die Reihenfolge der Signposts strukturell begründet ist, kann keine Prüfung sagen. Sie ist lizenzierte
  Dramatica-Logik und nicht berechenbar (`engine-rules.md`). Hier ist sie die Wahl des Autors nach der Quellensuche.
- Die Archetypen jenseits von Protagonist und Antagonist fehlen (W10 C). Die Players sind also unvollständig, und das
  steht in `a.json` als offener Punkt.
