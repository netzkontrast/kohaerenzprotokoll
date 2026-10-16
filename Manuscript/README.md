# Manuscript

<!-- readme-context:start -->
Directory guide. Current work is in NOW.md; CLAUDE.md defines the session
contract. Counts with state markers are checked by `python3 scripts/state.py --prose`.

[Project](../README.md) · [Current work](../NOW.md) · [Canon](kanon.md)
<!-- readme-context:end -->

Der Arbeitsplatz des Romans. Hier steht **nur Kanon und Arbeitsstand**, nie eine Lesart aus den Quellen. Die
Recherche lebt im Wiki; eine Karte darf auf ihre Wiki-Seite zeigen, aber nichts von dort gilt hier.

Angelegt am 2026-10-04 auf deine Anweisung „Füge eine manuscript Section in der [App] ein – und speichere deine
Entwürfe in einem Ordner manuscript“ (Entscheidung 023). Am 2026-10-05 wurde daraus der Arbeitsplatz für den ganzen
Roman, mit Kapiteln, Figuren und Welt (Entscheidung 024).

## Zwei Schichten

- **Kanon** steht an genau einer Stelle: in [`kanon.md`](kanon.md). Dort stehen deine Entscheidungen über das Buch,
  jede mit Datum, und die Kapitel, die du freigegeben hast. Der aktuelle Umfang steht in der Entscheidungstabelle; kein Kapitel ist
  freigegeben. Eine Karte oder ein Kapitel gilt nur dann als Kanon, wenn es eine `id` aus diesem Verzeichnis nennt.
- **Arbeitsstand** ist alles andere: Entwürfe, Plots, Karten, Vorschläge. Nichts davon gilt, bis du es freigibst.
  Wer einen Entwurf geschrieben hat, steht in seinem Kopf. Bisher war es jedes Mal eine Claude-Sitzung, auf deinen
  ausdrücklichen Auftrag. Wer die Prosa grundsätzlich schreibt, ist offen (Frage A in `NOW.md`).

## Was wo liegt

| Ordner | Stand |
|---|---|
| [kanon.md](kanon.md) | das aktuelle Kanon-Verzeichnis: Figuren, Kernwelten, Genesis, Juna, AEGIS und Autorentscheidungen; kein Kapitel freigegeben |
| [kap-01/](kap-01/README.md) | zehn Entwürfe: A–G (KW1 als Stadt); H, die Neuausrichtung als Space Opera (KW1 als Spindel im All); I, frische Ideen (Grauzonentaucher); zuletzt J, aus dem Treatment geschrieben (G nach Q7 und den Prüfungen); bewertet in `Plan/runs/writing/opening/agent-first-pages_2026-10-03.md` |
| [kap-02/](kap-02/README.md) | ein Entwurf: A, „Die Rolle hält“, aus dem Treatment, im Anschluss an J (2026-10-06) |
| [plot/](plot/plot-entwurf-01-die-rueckgabe.md) | Plot-Entwurf 1, „Die Rückgabe“: ein vollständig neuer Plot für den ganzen Roman (33 Kapitel in vier Teilen); ein Vorschlag, kein Treatment |
| [plot/](plot/plot-entwurf-02-die-mauer.md) | Plot-Entwurf 2, „Die Mauer“: eine ganz andere Geschichte im selben Universum, erzählt von einer Grenzsoldatin in KW3 (29 Kapitel und fünf Prüfprotokolle in drei Teilen); Kael nur am Rand; ein Vorschlag, kein Treatment |
| `figuren/` | eine Karte pro Figur: was entschieden ist, was die Entwürfe aus ihr machen, was offen ist |
| `welt/` | eine Karte pro Ort, Regel oder Mechanismus, gebaut wie die Figurenkarten |
| [plot/](plot/plot-entwurf-03-die-wendung.md) | Plot-Entwurf 3, „Die Wendung“: Vorschlag zur Bedeutungswende, verknüpft mit W33; keine Entscheidung |
| [Treatment](plot/treatment.md) | Arbeitsgrundlage für Kapitelentwürfe; offene Ausführung bleibt Vorschlag |
| [Storyforms](../Plan/storyform/README.md) | beschlossene Struktur und ausdrücklich getrennte Ausführungsvorschläge |

## Wie eine Karte gebaut ist

```yaml
---
name: Cerberus
kind: figur            # figur | welt
kanon: ["C6"]          # ids aus kanon.md; leer heißt: nichts entschieden
match: ["Cerberus"]    # Wörter, die die App in den Entwürfen zählt
wiki: cerberus         # die Recherche-Seite, nur als Verweis
---
```

Darunter stehen drei Abschnitte: `## Kanon` (nur, was in `kanon.md` steht), `## Arbeitsstand` (eine Zeile pro
Entwurf, mit der Datei) und `## Offen`. Die App fügt eine Tabelle hinzu, wie oft die Figur in jedem Entwurf vorkommt.
Diese Zahl ist gezählt, nicht gedeutet.

## Was hier nie steht

- **Befunde.** Was die Schreib-Skills über einen Entwurf sagen (Lektüre, Zeilenlektorat, Gutachten), steht in
  `Plan/runs/writing/<ziel>/`. Die App zeigt die Befunde neben den Entwürfen, aber kein Skill schreibt in diesen Ordner.
- **Lesarten der Quellen.** Die Entwürfe zitieren keine Quelle mit `^[Lnn]`, und nichts aus dem Wiki wird durch sie
  wahr. Wo ein Entwurf bewusst gegen die Quellen entscheidet, sagt das die `README.md` des Kapitels.

## Was als Nächstes ansteht

W0 ist entschieden und steht im [Kanon](kanon.md). Die verbleibenden Weichen werden
mit dem Autor anhand der [Entscheidungsvorlage](../Plan/runs/storyform-2026-10-06/entscheidungsvorlage.md)
bearbeitet. Danach wird das Treatment aktweise freigegeben; erst daraus werden
konkrete Kapitelereignisse abgeleitet. [NOW.md](../NOW.md) hält die aktuellen
Arbeitsaufträge. Frühere Entwurfsbegründungen bleiben datierte Vorschläge.
