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
  → [Plan/codex-architecture/codex-inventory_2026-09-16.md](Plan/codex-architecture/codex-inventory_2026-09-16.md)
  (2026-09-16). Reine Bestandsaufnahme, keine Entscheidung — die
  Autoritätsmatrix (nächster Punkt) ist noch offen.
- [x] Autoritätsmatrix beschließen: Welche Schicht ist für welche Information
  die einzige Quelle der Wahrheit?
  → [Plan/codex-architecture/authority-matrix_2026-09-16.md](Plan/codex-architecture/authority-matrix_2026-09-16.md)
  (2026-09-16). 13 Informationsarten entschieden; 2 davon (aufgeteilter
  `kind=concept`-Bucket, Aufnahme von Figurenwissen-Tracking) waren echte
  neue Weichenstellungen und gingen per Rückfrage an den Autor, bevor sie
  als entschieden markiert wurden.
- [x] Überschneidungen und Drift zwischen Canon, Codex, Wiki, NCP und
  Manuskript erfassen.
  → [Plan/codex-architecture/overlaps-drift_2026-09-16.md](Plan/codex-architecture/overlaps-drift_2026-09-16.md)
  (2026-09-16). Zwei konkrete, verifizierte Funde: eine veraltete
  `CodexEntry` (Slot-16-Lock vom 2026-09-11 nie ins Graph übernommen —
  Fix braucht Agency-MCP-Zugriff, in dieser Session nicht verfügbar) und
  eine Fehlzitierung zwischen zwei nicht deckungsgleichen
  Regel-Nummerierungen (R-Serie vs. DR-Serie), in `docs/worldcodex-integration.md`
  bereits korrigiert. Stichprobe, kein vollständiges Audit — siehe Datei
  §Method.
- [x] Stabile Codex-Entitäten und Pflichtfelder definieren, bevor Ordner
  angelegt werden.
  → [Plan/codex-architecture/entity-model-proposal_2026-09-16.md](Plan/codex-architecture/entity-model-proposal_2026-09-16.md)
  (2026-09-16). 8 neue `entity_type`-Werte + 4 unveränderte `kind`-Werte;
  zweiphasig (Body-Feld jetzt, echte Engine-`kind`-Erweiterung später nur
  wenn `agency_doctor`/`get_schema` das bestätigen — in dieser Session
  nicht prüfbar). Alle 3 Weichenstellungen gingen an den Autor; die
  `R-N`/`DR-N`-Frage bleibt bewusst offen für Punkt 9.
- [x] Wissensdimensionen sauber trennen: objektive Wahrheit, Figurenwissen,
  Leserwissen, erzählerische Enthüllung und zeitliche Gültigkeit.
  → [Plan/codex-architecture/knowledge-dimensions_2026-09-16.md](Plan/codex-architecture/knowledge-dimensions_2026-09-16.md)
  (2026-09-16). 4 von 5 Dimensionen bereits durch Punkt 4 abgedeckt; eine
  echte Lücke gefunden (keine aggregierte "Leserwissen bis Szene N"-Abfrage)
  und offen für Punkt 10 oder eine künftige Engine-Fähigkeit dokumentiert,
  nicht hier behoben.
- [ ] Zielstruktur ausschließlich aus stabilen Entitäts- und Graphfeldern
  ableiten; keine frei erfundenen Themenordner.
  ⚠ **Zwei Entwürfe stehen sich gegenüber, einer davon ist bereits gebaut.**
  PR #42 (gemerged) schlägt in `entity-model-proposal_2026-09-16.md` ein
  geschlossenes `entity_type`-Vokabular vor, das die 16 `Kategorie:`-Werte auf
  8 Typen zusammenfasst (`rule`+`guidance`+`defect` → `narrative-constraint`,
  `motif`+`theme`+`voice` → `motif`), und baut bewusst nichts.
  PR #41 (offen) hat statt dessen auf `**Kategorie:**` unverändert partitioniert
  — 22 Kategorien, ein Verzeichnis je Kategorie, `_misfiled` für alles
  Undeklarierte — und das gerenderte Ergebnis liegt bereits unter `Codex/`.
  Beide Wege sind vertretbar; sie sind nicht kombinierbar, weil jeder die
  Partitionsdimension anders wählt. Welcher normativ ist, entscheidet der Autor.
  Die Umstellung ist billig: `Graph/schema.yaml` + `tools/kpcodex` ändern und
  neu rendern, die Datensätze selbst bleiben unberührt.
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

---

# Weitere Aufgaben (niedrigere Priorität)

## Offene Punkte aus Item 1–4 (brauchen Agency-MCP/CLI-Zugriff)

**Priorität:** mittel — beide sind bereits diagnostiziert, nur die Ausführung
fehlt.

- [ ] `slot-16-hard-b-etablierungskapitel`-CodexEntry (`codexentry:6e51dc32`)
  aktualisieren: Body spiegelt noch den Vor-Lock-Zustand ("Kap 5–8, Position
  offen"), obwohl der Canon-Lock vom 2026-09-11 auf Kapitel 5 fixiert ist
  ([overlaps-drift_2026-09-16.md](Plan/codex-architecture/overlaps-drift_2026-09-16.md)
  Finding 1). `update_codex_entry(entry_id="codexentry:6e51dc32", body=<Autor-Lock-2026-09-11-Wortlaut>)`,
  dann `render_codex_views.py`.
- [ ] Prüfen, ob der `CodexEntry.kind`-Enum (Spec 132) über `agency_doctor`/
  `get_schema` erweiterbar ist ("Phase B" in
  [entity-model-proposal_2026-09-16.md](Plan/codex-architecture/entity-model-proposal_2026-09-16.md)).
  Wenn ja: `entity_type`-Werte schrittweise in echte `kind`-Werte migrieren.
  Wenn nein: Phase A (Body-Feld) bleibt die dauerhafte Struktur, dokumentiert
  als solche.

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
