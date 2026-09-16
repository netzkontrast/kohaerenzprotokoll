# Nächste wichtige Aufgabe

## Codex- und Wiki-Architektur für kontext-effiziente Romanarbeit

**Priorität:** hoch  
**Status:** Struktur steht (PR #41); Restpunkte unten offen  
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
- [x] Autoritätsmatrix beschließen: Welche Schicht ist für welche Information
  die einzige Quelle der Wahrheit?
- [x] Überschneidungen und Drift zwischen Canon, Codex, Wiki, NCP und
  Manuskript erfassen.
- [x] Stabile Codex-Entitäten und Pflichtfelder definieren, bevor Ordner
  angelegt werden.
- [ ] Wissensdimensionen sauber trennen: objektive Wahrheit, Figurenwissen,
  Leserwissen, erzählerische Enthüllung und zeitliche Gültigkeit.
- [x] Zielstruktur ausschließlich aus stabilen Entitäts- und Graphfeldern
  ableiten; keine frei erfundenen Themenordner.
- [ ] Link- und Promotionvertrag zwischen Wiki, Codex und Canon definieren.
- [x] Für ein reales Kapitel ein minimales Kontextpaket prototypisch erzeugen.
- [x] Bestehende Skills, Commands und Skripte gegen das neue Modell prüfen.
- [ ] Separaten `codex-maintenance`-Skill und einen sicheren, schrittweisen
  Migrationsplan entwerfen.

### Stand nach PR #41

Umgesetzt: `Graph/schema.yaml` ist der Vertrag (22 Kategorien, Partitionspfad,
Always-on-Menge, Fensterregel), `tools/kpcodex` die Implementierung,
`Codex/` die Ausgabe — Wurzeldateien nur Navigation, Inhalte je eine abrufbare
Einheit pro Datei unter `entries/`, `axioms/`, `timeline/`.
`scripts/context_packet.py --chapter N` liefert das Paket.

**Der leitende Praxistest besteht:** Kapitel 3 lädt ~21.700 Token über 232
Dateien statt ~84.400 für alle Codex-Bodies, und ein Eintrag, der erst später
ausgelöst wird, kann nicht in ein früheres Paket geraten.

Noch offen:

- [ ] Wissensdimensionen vollständig trennen: `spoiler_until` je Eintrag ist in
  `Graph/schema.yaml` als `not-implemented` erfasst und hängt an Story-Encoding,
  Weaving und Worldbuilding. Die Fenster-Mitgliedschaft deckt den Fall „früh
  eingeführt, erklärt aber eine späte Enthüllung" nicht ab.
- [ ] Link- und Promotionvertrag zwischen Wiki, Codex und Canon definieren.
- [ ] Separaten `codex-maintenance`-Skill entwerfen. Die Codex-Regeln liegen
  derzeit im `wiki-maintenance`-Skill als Abgrenzung.
- [ ] Entscheiden, ob die 643 generierten `Codex/`-Dateien versioniert bleiben
  oder in `.gitignore` gehören.
- [ ] `always_on_categories` prüfen: sechs Kategorien sind 8.943 der 21.713
  Token eines Kapitelpakets — der größte Hebel auf die Paketgröße.

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
  vollständige Rohquelle laden. (Erfüllt: `Codex/GLOSSARY.md` ist reine
  Navigation und enthält keinen Eintragstext mehr.)
- Bestehende Verbraucher sind migriert, kompatibel angebunden oder ausdrücklich
  als zu ersetzend dokumentiert.
- Renderer-, Link-, Drift- und Kontextpaket-Tests laufen reproduzierbar.

### Leitender Praxistest

> Kann ein Agent Kapitel 3 kohärent bearbeiten, ohne das vollständige Glossar
> zu laden und ohne Wissen aus Kapitel 20 zu verwenden?

Wenn dieser Test reproduzierbar besteht, erfüllt die neue Struktur ihren
eigentlichen Zweck.
