# Nächste wichtige Aufgabe

## Codex- und Wiki-Architektur für kontext-effiziente Romanarbeit

**Priorität:** hoch  
**Status:** geplant  
**Arbeitsmodus:** eigener Codex-Migrations-PR; nicht mit normaler Wiki-Pflege
vermischen

### Ziel

Ein verbindliches Informationsmodell für `Canon/`, `Codex/`, `Wiki/`, NCP,
Manuskript und Provenienzgraph entwickeln. Bei der Romanarbeit soll daraus das
kleinste ausreichende, kapitel- und spoilersichere Kontextpaket geladen werden
können, ohne vollständige Glossare oder Rohquellen in den Arbeitskontext zu
ziehen.

### Reihenfolge für die nächste Session

- [x] Vollständige Codex-Inventur erstellen: Dateien, Größen, Generatoren,
  Graph-Entitäten, manuelle Inhalte und alle Verbraucher/Verweise.
  → [Plan/codex-architecture/codex-inventory_2026-09-16.md](Plan/codex-architecture/codex-inventory_2026-09-16.md)
  (2026-09-16). Reine Bestandsaufnahme, keine Entscheidung — die
  Autoritätsmatrix (nächster Punkt) ist noch offen.
- [ ] Autoritätsmatrix beschließen: Welche Schicht ist für welche Information
  die einzige Quelle der Wahrheit?
- [ ] Überschneidungen und Drift zwischen Canon, Codex, Wiki, NCP und
  Manuskript erfassen.
- [ ] Stabile Codex-Entitäten und Pflichtfelder definieren, bevor Ordner
  angelegt werden.
- [ ] Wissensdimensionen sauber trennen: objektive Wahrheit, Figurenwissen,
  Leserwissen, erzählerische Enthüllung und zeitliche Gültigkeit.
- [ ] Zielstruktur ausschließlich aus stabilen Entitäts- und Graphfeldern
  ableiten; keine frei erfundenen Themenordner.
- [ ] Link- und Promotionvertrag zwischen Wiki, Codex und Canon definieren.
- [ ] Für ein reales Kapitel ein minimales Kontextpaket prototypisch erzeugen.
- [ ] Bestehende Skills, Commands und Skripte gegen das neue Modell prüfen.
- [ ] Separaten `codex-maintenance`-Skill und einen sicheren, schrittweisen
  Migrationsplan entwerfen.

### Zu klärende Architekturfragen

1. Welche Inhalte bleiben ausschließlich in `Canon/`, welche werden als
   kompakte Codex-Projektion gerendert?
2. Welche Entitätstypen werden benötigt, zum Beispiel Character, Location,
   World, WorldAxiom, StoryEvent, System, Motif oder NarrativeConstraint?
3. Welche Felder bilden `introduced_in`, erzählerische Gültigkeit,
   `writer_safe_from`, `revealed_in` und Figurenwissen ab?
4. Welche bisherigen Pfade müssen während der Migration kompatibel bleiben?
5. Wie werden Widersprüche sichtbar gemacht, ohne sie automatisch aufzulösen?

### Migrationsregeln

- Den aktuellen Codex nicht direkt oder als Big Bang umbauen.
- Erst Inventur, Verbraucherkarte, Zielvertrag und Rückfallstrategie erstellen.
- Neue Renderer zunächst parallel zu den alten Ansichten betreiben.
- Generierte Codex-Dateien niemals von Hand pflegen.
- Wiki-Maintenance darf Codex-Probleme dokumentieren, aber keine Codex-Dateien
  verschieben oder aufteilen.
- Den Umbau in einem eigenen Branch und PR durchführen.

### Akzeptanzkriterien

- Für jede Informationsart gibt es genau eine benannte Autoritätsquelle.
- Jede Codex-Ausgabe lässt sich auf Graph- oder Canon-Quellen zurückführen.
- Ein Schreibagent kann ein frühes Kapitel bearbeiten, ohne Wissen aus späteren
  Kapiteln zu erhalten.
- Das Kontextpaket enthält nur relevante Regeln, Entitäten, offene Fragen und
  bei Bedarf genaue Belegstellen.
- Kein normaler Workflow muss das vollständige `Codex/GLOSSARY.md` oder eine
  vollständige Rohquelle laden.
- Bestehende Verbraucher sind migriert, kompatibel angebunden oder ausdrücklich
  als zu ersetzend dokumentiert.
- Renderer-, Link-, Drift- und Kontextpaket-Tests laufen reproduzierbar.

### Leitender Praxistest

> Kann ein Agent Kapitel 3 kohärent bearbeiten, ohne das vollständige Glossar
> zu laden und ohne Wissen aus Kapitel 20 zu verwenden?

Wenn dieser Test reproduzierbar besteht, erfüllt die neue Struktur ihren
eigentlichen Zweck.

---

# Weitere Aufgaben (niedrigere Priorität)

## Vendorte generische worldcodex-Skills gegen novel-architect-* prüfen

**Priorität:** niedrig  
**Status:** zurückgestellt (2026-09-16, aus dem Workflow-Simplify-Pass)  
**Herkunft:** Altitude-Review der Skill-Landschaft (PR #42) schlug vor, die
vendorten generischen worldcodex-Skills (`auditing-canon`, `designing-worlds`
usw.) zu entfernen, wo sie von projekteigenen `novel-architect-*`-Skills
bereits abgedeckt sind. Auf Nachfrage bewusst zurückgestellt: braucht ein
eigenes Paar-für-Paar-Audit, kein Schnelldurchlauf, da manche vendorten
Skills (`canon-rules`, `deep-reading`, `cross-checking`) echte
Querschnitts-Utilities sind und nicht pauschal entfernt werden dürfen.

Wenn aufgegriffen: pro Skill-Paar prüfen, ob der projekteigene Skill den
vendorten wirklich vollständig ersetzt (nicht nur überlappt), erst dann
Retirement vorschlagen — Rule 0, kein automatisches Löschen.
