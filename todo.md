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

**Überholt durch PR #41**, das alle 27 entfernt hat. Die Konzepte, die dabei
mitgingen, sind unter „Workflows neu denken" am Ende dieser Datei gesichert.

## Workflows neu denken — was aus den 27 Agency-Skills tragfähig war

**Priorität:** hoch (Grundlage für die nächste Session)  
**Status:** Konzepte gesichert, nichts entschieden  
**Herkunft:** PR #41 hat 27 Skills in einem Commit entfernt (`692ec19`), davon
20 vendorte generische worldcodex-Skills. Die Entfernung war richtig — die
Generatoren zielten auf ein anderes Projekt (Alien-Biome, Planetensysteme,
Institutionen aus Speziesbiologie). Verloren gingen dabei aber **Konzepte**,
die nichts mit Worldcodex zu tun hatten, sondern echte Querschnitts-Mechanik
waren. Die stehen hier, damit die nächste Session die Workflows dieses Repos
aus einem vollständigen Bild neu schneiden kann. Wiederherstellbar sind alle
Originale mit `git show 692ec19^:.claude/skills/<name>/SKILL.md`.

### A — Sofort verwertbar, weil sie eine bekannte Lücke schließen

1. **Autoritätsordnung bei Widersprüchen** (`cross-checking`). Die Skill
   führte eine explizite Rangfolge: Manuskript-Prosa (telling details) >
   `Plan/drafting`-Entscheidungen > Canon (storyform-und-outline normativ) >
   NCP > `Codex/`-Views > Legacy. Das ist **feiner als CLAUDE.md**, wo für
   Manuskriptarbeit pauschal storyform-und-outline gewinnt: die Skill sagt,
   dass bereits geschriebene Prosa bei *Details* gewinnt und man dann meldet
   statt umzuschreiben. Zu entscheiden: gilt diese Differenzierung, und wenn
   ja, gehört sie in CLAUDE.md.

2. **Die „by design, kein Widerspruch"-Ausschlussliste** (`cross-checking`).
   Fünf Fälle, die wie Widersprüche aussehen und keine sind: Storyform A vs B,
   unterschiedliche Kernwelt-Regime, unterschiedliche Wahrnehmung je Anteil,
   AEGIS' Lesart eines Ereignisses gegenüber Kaels (Kap 5 vs Kap 4), und
   Kapitel, die legitim weniger wissen dürfen (Reveal-Timeline §6.2).
   **Das Widerspruchs-Ledger aus PR #41 hat diesen Filter nicht.** Ohne ihn
   wird es genau diese fünf Klassen als offene Widersprüche protokollieren und
   den Autor mit Nicht-Befunden beschäftigen. Höchster Einzelwert auf dieser
   Liste.

3. **Entity-Extraktion: ein Entity pro Datei** (`extracting-entities`).
   Regel war: ganze Quelle lesen, Extraktionsplan vorlegen, erst nach Freigabe
   schreiben, Quellinhalt nie zusammenfassen. Das ist die direkte Antwort auf
   den Probe-Befund, dass **4 von 4 Source-Pages das 1000-Wort-Budget reißen**
   (1530/1504/2918/2695) — eine Auditquelle trägt mehr Entities als eine Seite
   fassen darf.

4. **Entity-Kompilierung über das ganze Repo** (`compiling-entities`). Alle
   Erwähnungen eines benannten Entity einsammeln, `[K]/[V]/[L]`-Marker je Fakt
   mitführen, Widersprüche melden, ohne Freigabe nichts schreiben. Das ist der
   Lesepfad, den der Entity-Baum des Widerspruchs-Ledgers
   (`contradictions/entity/<slug>.md`) voraussetzt und noch nicht hat.

### B — Struktur, die dem Repo fehlt

5. **Abhängigkeits-Walkthrough in Schichtordnung** (`interrogating-design`).
   Jede Designfrage wird gegen die Schichten dieses Romans geprüft, in dieser
   Reihenfolge: DKT-Fundament (K₀/K₁, Atemporalität, Große Inversion) →
   Storyform (gesperrte Slots, Signpost-Ordnung, Vortex-Mechanik) →
   Kernwelt-Regime und Sensorik (Logik-Regime, Hitze-Polarität, Riss-Mandat) →
   Anteile und Reveal-Disziplin (Sprach-DNA, Multiplizitäts-Schleier,
   Wissens-Fences) → bestehende Prosa. Dazu OODA als Schleife und die Regel
   „Prosa gewinnt bei Details — melden, nicht umschreiben". `/tetraframe`
   liefert vier Positionen, `/clarify` schärft Begriffe; diese Schichtprüfung
   fehlt als eigener Schritt.

6. **„Abgeleitet oder importiert?"** (`auditing-human-assumptions`). Die Skill
   prüfte Beschreibungen, Vokabular und Sozialstrukturen darauf, ob sie aus
   den Voraussetzungen der Welt abgeleitet oder aus vertrautem Kontext
   übernommen wurden — ausdrücklich **auch für Menschen in fremder Umgebung**
   (moderne westliche Institutionen, Erd-Ökonomie, vertraute politische
   Formen als Default angenommen). Für Köln 2026 und die Kernwelt-Bewohner
   ist das die schärfere Variante des Re-Derivations-Audits, das `/kp-world`
   heute nur als Bautyp kennt.

7. **Forschungsintegration als nachvollziehbare Kette** (`integrating-research`).
   Reales Prinzip → was es über die Realität aussagt → kreative Analogie →
   welche Canon-Sektion es füllt. Die Wiki-Concept-Pages haben für diese Kette
   kein Feld; `canon_status` sagt nur, ob geprüft wurde, nicht *wie* die
   Brücke gebaut wurde. Für die DKT-Erdung der tragende Punkt.

8. **Content-Map vor dem Bearbeiten** (`deep-reading`). Ganze Datei lesen,
   dann Abschnitte mit Zeilenbereichen, benannte Entities und Lückenanalyse
   gegen Codex/Canon ausgeben. Die maschinelle Hälfte davon macht die
   Extraktion im Ingest bereits; für Canon-Dokumente, die von Hand bearbeitet
   werden, gibt es nichts Vergleichbares.

9. **Planungspflicht ab mehr als drei Dateien** (`planning-worldbuilding`).
   Zieldateien, Verifikationskriterien und Abhängigkeitsordnung vor dem ersten
   Schreiben, eine Aufgabe je Datei, Freigabe vor Ausführung.

### C — Gates und Phasen

10. **Vollständigkeits-Checkliste je Artefakt** (`verifying-completion`).
    Neun Punkte, von denen mehrere heute schon Skripte sind
    (`lint_chapter.py`, `check_enrichment.py`, `render_codex_views.py --check`).
    Nicht abgedeckt sind: „jede Abweichung von Plan oder Canon trägt einen
    D-xx-Eintrag", „jeder neue Begriff hat einen Codex-Eintrag mit Triggern",
    „datierte Fakten sind StoryTimeEvents" und der Statuswechsel
    `drafted → revised → final` erst nach dem lit-critic-Gate ohne offenen
    `critical`-Befund.

11. **Die Drei-Tier-Gate-Leiter** (aus dem Agency-CLAUDE.md, über PR #42 noch
    auf `main` sichtbar). Dieselben neun Prüfungen, gruppiert nach dem, wofür
    sie Reife bezeugen — draft-ready, edit-ready, publish-ready — mit der
    ausdrücklichen Regel, den Status jeder einzelnen Prüfung zu berichten und
    neun Prüfungen nie zu einem Pass/Fail-Bit zusammenzufassen. Die Tiers
    sind übertragbar; die Verben darunter (`pre_draft_gate`,
    `developmental_gate`, `line_gate`, `copy_gate`) sind es nicht.

12. **Phasen-Workflows mit deklarierten Ein- und Ausgaben** (agency
    `skill_walk`). Jeder Workflow war eine feste Phasenfolge, jede Phase
    konsumierte deklarierte Schlüssel aus den Ergebnissen der vorigen, und die
    Abschlussphase verlangte ausdrückliche Autor-Freigabe: `novel-concept` (10
    Phasen), `world-bible-architect` (5, canon-lock), `storyform-build` (6),
    `scene-writer` (5), `scene-bridge-auditor` (5), `developmental-editor` (5),
    `line-editor` (4), `character-architect` (4), `publish-prep` (4).
    `/kp-world` ist bereits so gebaut (Checkpoint je Schicht). Die Frage für
    die nächste Session ist, ob das die allgemeine Form für `/kp-write` und
    `/research-ingest` werden soll.

### D — Konkreter Fund nebenbei

13. **`WRITING.md` ist nicht verdrahtet.** Die Datei existiert und ist
    maschinenlesbar (Sprachen je Ebene, Dokumenttypen, Voice, Tempus,
    Frontmatter-Felder, Statuswerte, Marker). Gelesen wird sie von keinem
    Skript — `lint_chapter.py` enthält 0 Treffer — während CLAUDE.md sagt,
    `lint_chapter.py` sei die einzige Kodierung der R-Regeln. Damit bestehen
    zwei Kodierungen derselben Prosaregeln nebeneinander, und die
    `last-synced`-Angabe (2026-09-15) ist die einzige Verbindung. Zu
    entscheiden: entweder `lint_chapter.py` liest `WRITING.md`, oder
    `WRITING.md` wird als generierte Ansicht gekennzeichnet.

### Was bewusst nicht übernommen wird

Die Generatoren `designing-worlds`, `designing-lore`, `writing-worldbuilding`,
`writing-science` und `deriving-social-systems` zielten auf Biome, Planeten,
Mythologien und Institutionen aus Speziesbiologie. Dieses Repo hat sieben
fertige Ebenen mit 111 Axiomen und braucht keine Generatoren, sondern
Ableitungsketten mit Autor-Checkpoints — das ist `/kp-world`. Aus
`deriving-social-systems` bleibt allein das Prinzip erhalten, das unter Punkt 6
schon steht. `code-clarifier` und `researching-papers` sind durch
`scripts/research-tool.py` und normale Entwicklungsarbeit abgedeckt.

### Verhältnis zum zurückgestellten Skill-Audit

Der Punkt „Vendorte generische worldcodex-Skills gegen novel-architect-* prüfen"
weiter oben ist durch PR #41 überholt: die Skills sind entfernt. Was dort als
Grund für die Zurückstellung genannt wurde — `canon-rules`, `deep-reading`,
`cross-checking` seien echte Querschnitts-Utilities — war richtig, und genau
diese drei stehen hier unter A und B wieder auf der Liste. `canon-rules` selbst
liegt vollständig als `docs/canon-rules/` im Repo.
