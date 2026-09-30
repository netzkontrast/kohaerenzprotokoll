# Zwei vorläufige NCP-Dateien — Storyform A und B

**Stand 2026-09-30. Forschungsposition, kein Kanon, keine Entscheidung des Autors.** Erzeugt von `build.py` aus einer Tabelle; jeder Wert ist der Tabelle des Status-Berichts vom 2026-05-07 entnommen (`Sources/drive/dramatica-dual-storyform-status-2026-05-07-md.md`, §II.1), und jede Datei sagt das in ihrem `storytelling`-Feld. Nichts hier ist Prosa.

```bash
python3 build.py <ncp-author>/assets/template-storyform.json   # schreibt beide Dateien
node <ncp-author>/scripts/validate.js storyform-a.provisional.ncp.json   # PASS
node <ncp-author>/scripts/validate.js storyform-b.provisional.ncp.json   # PASS
```

Beide Dateien bestehen das Schema des `ncp-author`-Skills (gepinnter Upstream `0b9ab12`, NCP 1.3.0). Der Validator prüft nur die Struktur: Er sagt nicht, dass die Werte theoretisch stimmen (Skill, *Limits*, Nr. 1).

## Was drin steht

- vier Perspektiven je Storyform (MC, IC, OS, RS) mit ihrem Träger;
- acht der neun Dynamiken (Driver, Outcome, Judgment, Limit, Problem-solving style, MC Resolve, MC Growth, MC Approach);
- neun Storypoints: MC Domain, Concern, Issue, Problem, Solution; IC Domain, Concern; OS Domain; RS Domain.

## Was fehlt, weil keine Quelle es sagt

| Lücke | Stand |
|---|---|
| `influence_character_resolve` (neunte Dynamik) | in keiner Quelle; die Dateien erreichen deshalb nicht `draft` |
| Story Goal, Requirements, Consequence, Forewarnings, Costs, Dividends, Prerequisites, Preconditions | in keinem der fünf Storyform-Dokumente; Kandidaten stehen in `Plan/weichen/wp-plot-story-points.md`, **nicht** hier, bis der Autor antwortet |
| Pivotal Element / Critical Flaw (Crucial Element) | offen; der Skill und der Bericht widersprechen sich für B, siehe dasselbe Blatt |
| OS-Concern und OS-Issue, RS-Concern und RS-Issue, IC-Issue, IC-Problem | die Synthese vom 2026-04-28 nennt Werte, aber für eine andere Klassen-Verteilung von A; nicht übernommen |
| Players | schwere Objekte (zehn Pflichtfelder); die Besetzung ist W10 und offen |
| Storybeats und Moments | die 16 Signposts stehen leer; ihre Reihenfolge ist im Blatt WP als Vorschlag, nicht als Wert |

## Warum zwei Dateien

NCP kennt mehrere Narratives in einem Dokument, der Skill hat das aber nicht geübt (*Limits*, Nr. 4). Die zwei Dateien folgen dem Muster des geparkten Entwurfs (`Legacy/…/ncp.json`, `ncp-b.json`), dessen Storyforms leer waren.
