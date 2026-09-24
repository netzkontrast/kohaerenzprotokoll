# Auftrag an Claude Code: Knowledge Graph und Wiki für den Roman „Kohärenz Protokoll“

> **Stand:** 2026-09-23 · **Verfasst von:** einer vorherigen Claude-Sitzung, die den Kanon, die Novel-Skills und den Drive-Bestand gesichtet hat.
> **Autor:** Michael (netzkontrast). Er denkt in GSD und arbeitet spec-getrieben.
> **Sprache:** Wiki-Inhalte, Fragen und Erklärungen auf Deutsch. Code, Identifier und Schemata auf Englisch. Dramatica-Fachbegriffe bleiben englisch (Storyform, Throughline, Storypoint …).
>
> **Überarbeitet 2026-09-23** mit dem, was das Repository zu diesem Zeitpunkt selbst belegt. Der Auftrag des Autors steht unverändert. Ergänzungen stehen in Blöcken **„Ist-Stand 2026-09-23“**, und jede Zahl darin trägt einen `<!--state:…-->`-Marker, den `python3 scripts/state.py --prose` prüft. Wo der Auftrag und das Repository sich widersprechen, steht das in **Anhang C** und nicht stillschweigend im Text.

---

## 0 · Worum es geht, in fünf Sätzen

1. Du baust ein **lokales, git-versioniertes System aus Knowledge Graph und Wiki**. Es hilft dem Autor, den Roman *Kohärenz Protokoll* zu schreiben: eine deutsche Hard-SF mit Philosophical Horror, 41 Bewegungen (Kap 0–40) und Dual-Storyform.
2. Die Quellen liegen verstreut: mehrere hundert Google-Drive-Dokumente, zwei bis drei GitHub-Repos, ein Manuskript mit 41 Kapiteldateien und Novel-Skills. Sie widersprechen sich an vielen Stellen, weil der Kanon über mehr als 17 Monate mehrfach umgebaut wurde.
3. Das System muss **Widersprüche finden, einordnen und nach einer expliziten Vorrangregel auflösen**, oder sie als Autor-Entscheidung markieren. Glätten darf es nie stillschweigend.
4. Es muss **eigene Fragen generieren und beantworten**, vor allem zu Lücken, Kausalität, Leser-Wissen und Plot-Konkretheit. Dabei unterscheidet es streng zwischen belegt, abgeleitet und offen.
5. Es muss wissen, **wie wir den Plot designen** (Kapitel 5 dieses Dokuments), und dieses Wissen als prüfbare Regeln und Werkzeuge einsetzen, nicht nur als Text.

Kein vorheriger Kontext überlebt. Alles, was du weißt, musst du aus den Quellen ableiten. Das Kanon-Briefing in **Anhang A** ist eine Starthilfe aus einer früheren Sitzung. Es hat die niedrigste Autorität unter den kanonischen Quellen und ist selbst zu verifizieren (Tier `M`, siehe §3.2).

> **Ist-Stand 2026-09-23 — du fängst nicht bei null an.** Seit dem Reset (Entscheidung `Plan/decisions/001-reset-to-two-layers.md`, 2026-09-16) baut dieses Repository ein Begriffs-Wiki aus den Drive-Quellen, mit denselben Grundsätzen, die dieser Auftrag verlangt: Provenienz auf jeder Aussage, kein stilles Glätten, Konflikte als eigene Records, abgeleitetes Wissen markiert. Es gibt:
>
> - `Sources/`: 613 <!--state:sources.total--> Drive-Dokumente im Manifest, 371 <!--state:sources.landed--> als Markdown gelandet und dedupliziert.
> - `Wiki/`: 56 <!--state:wiki.pages--> Begriffsseiten, 5 <!--state:wiki.conflicts--> Konflikt-Records und 4 <!--state:wiki.questions--> Fragen-Seiten, jede Aussage mit Zitat und Zeilennummer.
> - Einen abgeleiteten Knowledge Graph (`scripts/graph.py`) und GraphRAG-Retrieval (`scripts/graphrag.py`), die nur zurückgeben, was die Seiten belegen.
> - Eine DSPy-Werkzeugkette, die bisher kein Modell aufgerufen hat.
>
> **Was fehlt, ist der Roman im Graph.** Alle Drive-Quellen, auch die Kanon-Stände 2026-05/06, sind in `Sources/manifest.jsonl` katalogisiert. Alle 33 <!--state:sources.canon_era--> Einträge ab Mai 2026 sind seit 2026-09-24 als Volltext gelandet, 33 <!--state:sources.canon_era_landed--> davon (§2). Gelesen hat sie noch niemand: keiner hat Census, Note oder Abgleich. Manuskript und NCP sind keine Drive-Dokumente, sie liegen unter `Legacy/`. Die Einheit des bisherigen Wikis ist der *Begriff*. Dieser Auftrag verlangt zusätzlich *Kapitel*, *Locks* und *Plot*. Genau diesen Fall nennt Entscheidung 001 als Grund, sie zu revidieren: „if most questions are about chapters and plot rather than terms, the unit is wrong“.

---

## 1 · Nicht verhandelbare Regeln

1. **Read-only gegenüber Kanon und Prosa.**
   - `Manuscript/`, `Canon/`, die NCP-Dateien (`ncp.json`, `ncp-b.json`) und die Drive-Originale veränderst du nie.
   - Das KG spiegelt NCP nur lesend. Strukturelle Kanon-Änderungen laufen ausschließlich über den Autor und den Skill `ncp-author`.
   - Vorschläge landen unter `wiki/_proposals/`.
2. **Provenienz auf jeder Aussage.** Jeder Claim und jeder Wiki-Satz trägt mindestens eine Quelle (Dokument-ID, Abschnitt, wörtliches Zitat ≤ 300 Zeichen) und einen Status:
   - `[K]` kanonisch/gelockt
   - `[V]` Vorschlag
   - `[S]` Steinbruch, gefiltert
   - `[L]` Lücke
   - `[D]` von dir abgeleitet
   - `[M]` nur aus Memory/Briefing

   Das Projekt nutzt `[K]`, `[V]`, `[S]` und `[L]` bereits. Übernimm sie und ergänze nur `[D]` und `[M]`.
3. **Kein stilles Glätten.** Jeder Widerspruch wird ein Conflict-Record (§4.4), auch wenn die Vorrangregel ihn eindeutig entscheidet. Der Autor muss sehen können, *was* überstimmt wurde.
4. **`[D]` wird nie zu `[K]`.** Abgeleitetes Wissen bleibt markiert, bis der Autor es bestätigt.
5. **Story-First.** Wenn Dramatica-Theorie und ein existierender Draft sich widersprechen, gewinnt der Draft. Theorie ist Diagnose, nicht Rezept. Solche Fälle meldest du als Befund, nicht als Fehler im Draft.
6. **POV-Schutz.** Mosaikbrüche, unzuverlässige Erzähler und widersprüchliche Fußnoten im Manuskript sind *gewollte Risse*, keine Inkonsistenzen. Ein Konflikt *innerhalb der Prosa* ist erst dann ein Defekt, wenn er gegen einen Lock verstößt. Sonst ist er ein Kandidat mit der Frage an den Autor: „bewusster Riss?“
7. **Lesen heißt lesen.** Kanonische Dokumente liest du vollständig, nicht per Header-Skim. Eine Lehre aus früheren Sitzungen: Eine Klärung im Fließtext, die beim Skim unsichtbar blieb, hat einmal eine halbe Session redundant gemacht.
8. **Kein Hineinschreiben in Drive oder GitHub-Main.** Du arbeitest auf einem eigenen Branch (Vorschlag: `claude/kg-wiki`) und machst kleine, erklärte Commits.
9. **Fragen an den Autor sparsam und mit Kontext.**
   - Höchstens 1–4 Fragen pro Runde, jede mit Mechanik, Pro, Contra und Konsequenzen vor den Optionen. Nackte Optionen sind verboten.
   - Biete immer einen Freitext-Weg an. Der Autor antwortet oft mit vier Worten, die die richtige Antwort außerhalb deines Sets sind („AEGIS ist auch ein ANP“). Lies eine solche Kurzantwort als Substanz und entfalte sie.
   - Nicht blockierende Fragen sammelst du in der Review-Queue (§4.6).

> **Ist-Stand 2026-09-23 — Regeln, die dieses Repository schon hat und die hier mitgelten.** Jede ist mit Evidenz in `PRINCIPLES.md` begründet. Wo eine Regel oben enger oder weiter ist, gilt die engere.
>
> 10. **Zitieren heißt fragen, nicht tippen (P12, P26).** Eine Zeilennummer holst du dir mit `python3 scripts/read.py <slug> --find "<Wortlaut>"`, und `python3 scripts/quotes.py` prüft jedes Zitat gegen seine Zeile. Der Grund ist gemessen: Zitate waren sinngemäß richtig und im Wortlaut falsch („das Management“ statt „dem Management“). Das gilt auch für die ≤ 300-Zeichen-Zitate in §1.2.
> 11. **Lesarten werden nie zu einer Definition verschmolzen (P13).** Wo Quellen sich widersprechen, hält die Seite beide Lesarten mit Quelle fest und hört dort auf.
> 12. **Nicht jeder scheinbare Widerspruch ist einer (P14).** Vor jeder Konfliktmeldung prüfst du, ob es sich um einen der bekannten Fälle „by design“ handelt. Anhang B17 ist genau so ein Test.
> 13. **Ein Modell schlägt vor, es entscheidet nie, und nichts verlässt den Container ohne Ja.** Jeder Modellaufruf läuft über `scripts/lmrun.py`: Cache aus, Protokoll pro Aufruf, und ohne `approval=` wird ein echtes Modell verweigert. Korpustext an OpenRouter oder TypeSafe braucht jeweils eine eigene Zustimmung des Autors (`NOW.md`).
> 14. **Zahlen werden gemessen, nicht gespeichert (P24, `scripts/state.py`).** Jede Zahl in einer Markdown-Datei trägt einen `<!--state:…-->`-Marker. Wie es um einen Arbeitsschritt steht, wird aus den Artefakten abgeleitet und nicht angehakt.
> 15. **Ein Commit pro Wiki-Seite, und die Nachricht nennt das Quelldokument** (`CLAUDE.md`, *Committing a wiki page*).
> 16. **Jeder Prüfer beweist, dass er scheitern kann.** `python3 scripts/selftests.py` führt jede Suite aus. Eine Prüfung, die bei fehlenden Daten grün wird, ist der teuerste Fehler dieses Projekts gewesen: `coverage()` lieferte 1,0 ohne Gold-Daten.

---

## 2 · Quellen: wo das Wissen liegt

Mach zuerst eine Inventur. Welche Zugänge hast du tatsächlich (Drive-MCP, GitHub/`gh`, lokales Repo, Skills)? Passe den Plan an, was verfügbar ist, und dokumentiere fehlende Zugänge im Spec.

| Quelle | Ort | Charakter |
|---|---|---|
| **Drive-Ordner „kohärenz protokoll“** | Folder-ID `140NQif9s3jDqwZSAwhqKA5FW7NPxlCNB` | Mehr als 200 Docs, überwiegend April/Mai 2025 (Steinbruch, Gemini-Deep-Research-Outputs, Album-Konzepte) und April 2026 (Storyform-Synthesen). Viele Titel-Duplikate und Revisionen. |
| **Neuere Kanon-Docs auf Drive** | Liegen teils **außerhalb** dieses Ordners (u. a. Shared-Drive-Parent `0AFkw16njI3XMUk9PVA`). Deshalb zusätzlich global suchen, etwa `modifiedTime > '2026-04-01' and fullText contains 'Kohärenz'` bzw. `'AEGIS'` bzw. `'Kael'`. | Hier liegen die maßgeblichen Stände: 2026-05-07/08 Lock-In und Konzept, 2026-05-18 strukturierter Outline, 2026-05-30/31 Kompendium, 2026-06-10 „Repo-Quartett“, 2026-09-14 Session-Protokolle. |
| **GitHub `netzkontrast/kohaerenzprotokoll`** | Repo des Romans | `Manuscript/…/kohärenz-protokoll/chapters/NN-slug.md` (alle 41 Kapiteldateien existieren, Frontmatter `type: novel.chapter`); `Canon/`; `Plan/drafting/` (drafting-brief, akt2-arc-optimized, chapter-enrichment-masterplan_2026-09-11); `Plan/sessions/`; `ncp.json` + `ncp-b.json` (players, storybeats und moments noch leer); eigene `.claude/skills`. |
| **GitHub `netzkontrast/Dual-Kernel`** | `Markdown-docs/` (~70 Dateien) | Versionierter Drive-Spiegel älterer Konzept- und Recherche-Dokumente. Größtenteils Steinbruch. |
| **GitHub `netzkontrast/agency`** | `Plan/010-novel-domain/spec.md` | Re-Architektur-Entwurf der Novel-Domäne. Lies ihn, bevor du Architektur-Entscheidungen triffst. |
| **Novel-Skills** | `.claude/skills/` im Roman-Repo oder in der Skill-Umgebung | `novel-architect` (Kanon-Owner: `canon-meta.md`, `open-questions.md`, `progress.md`, `learnings.md`, NCP-Skeleton), `chapter-briefing-architect` (13-Sektionen-Briefing, 12-Punkte-Adversarial-Checklist), `chapter-draft-engine` (`draft_gate.py`, `prose_audit.py`, `rules.json`, Slot-16-Routing), `dramatica-theory`, `dramatica-vocabulary` (265 Terme, 75 Dynamic Pairs), `ncp-author` (Schema, Validator). |
| **claude.ai-Projekt-Docs** | Eventuell nicht direkt erreichbar | `Entscheidungs-Log 2026-05-30` (zwei Durchläufe), `Konzept Kapitel-40 Lesart-Dualitaet 2026-05-30`, `CH-01 Briefing` und Drafts v0.1–v0.3, `kap0v1annotiert`, `koharenzprotokollstoryweavingstartdokument20260508`. **Fehlen sie auf Drive oder im Repo, bitte den Autor um einen Export.** Die Logs sind Tier 1. |

**Ingest-Methode.** Das ist eine gelernte Lektion.
- Google Docs exportierst du als Markdown (`exportMimeType: text/markdown`). Wenn das nicht geht, als PDF und dann mit `pdfplumber` nach Markdown.
- Der Export geht auf die Platte. Volltexte gehören nicht in den Kontext. `read_file_content` nutzt du nur für gezielte In-Turn-Lookups.
- Für jeden Ingest schreibst du ein Manifest und dedupst per md5 und Normalisierungs-Diff.
- Viele Docs heißen `*.md`: Das ist Markdown, das in ein Google Doc eingefügt wurde.
- Das Album-Projekt „The Agency System“ (Suno-Lyrics, 13 Konzeptalben) liegt im selben Ordner. Klassifiziere es als eigenes Projekt (Tier `X`). Es dient nur als tonale Referenz und ist nie Kanon.

> **Ist-Stand 2026-09-23 — alle Quellen sind in `Sources/` (Autor, 2026-09-23).** `Sources/manifest.jsonl` ist der vollständige Katalog der Drive-Quellen. Eine globale Drive-Suche und der Blick in andere Ordner entfallen. Zu jedem Dokument gibt es eine `drive_id`, und `python3 scripts/sources.py` landet es von dort nach `Sources/drive/<slug>.md`. Der Katalog hat 613 <!--state:sources.total--> Einträge, davon sind 371 <!--state:sources.landed--> gelandet. 67 <!--state:sources.folded--> Duplikat-Exporte stehen in `Sources/duplicates.jsonl`. Die Dedupe über md5 und Normalisierung ist gebaut (`scripts/dedupe.py`, `scripts/duplicates.py`).
>
> **Die Kanon-Stände sind gelandet (2026-09-24, auf Ja des Autors).** Von 33 <!--state:sources.canon_era--> Einträgen ab 2026-05-01 sind 33 <!--state:sources.canon_era_landed--> als Volltext da. 29 kamen in einem Lauf `sources.py fetch --since 2026-05-01 --include-md`, 26 davon im Format `md` über denselben Textweg wie die vier `md`-Zeilen vom 2026-09-16. Vorher waren es 37 Einträge: vier waren Kopien und sind nach `Sources/duplicates.jsonl` gewandert (`dedupe.py`, Entscheidung pro Gruppe in `Plan/runs/dedupe.json`). Drei davon waren `-2`-Exporte mit 2 Byte Unterschied, einer (`25-wegkreuzung-md`) der gleiche Kapitel-25-Text in anderer Escape-Form.
>
> | Dokument im Auftrag | Slug in `Sources/manifest.jsonl` | gelandet |
> |---|---|:-:|
> | Kapitel-Kompendium 2026-05-31 | `kapitel-kompendium-gather-2026-05-31-md` | **ja** |
> | Strukturierter Outline 2026-05-18 | `koharenz-protokoll-strukturierter-outline-2026-05-18-md` (`-2` gefaltet) | **ja** |
> | Konsolidiertes Konzept 2026-05-08 | `koharenz-protokoll-konzept-konsolidiert-2026-05-08-md` | **ja** |
> | Konzept-Master, Konzept-Iteration Genesis 05-08 | `kohaerenz-protokoll-konzept-master-md`, `koharenz-protokoll-konzept-iteration-genesis-md` | **ja** |
> | Lock-In-Status 2026-05-07 | `dramatica-dual-storyform-status-2026-05-07-md` (`-2` gefaltet) | **ja** |
> | Charakter-Bibel 2026-05-08 | `kohaerenz-protokoll-charakter-bibel-2026-05-08-md` | **ja** |
> | Sprach-DNA 2026-05-13 | `koharenz-protokoll-sprach-dna-2026-05-13-md` | **ja** |
> | Quartett: `storyform-und-outline` 06-10 | `kohaerenz-protokoll-storyform-und-outline-2026-06-10-md` | **ja** |
> | Quartett: `kernwelten-vollstaendig` 06-10 | `kohaerenz-protokoll-kernwelten-vollstaendig-2026-06-10-md` | **ja** |
> | Quartett: `philosophie-im-detail` 06-10 | `kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md` | **ja** |
> | `begriffe-und-konzepte` 06-10 | `kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md` | **ja** |
> | `welt-sensorik-drafting` 06-10 | `kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md` | **ja** |
> | `anteile-profile-sprach-dna` 06-10 | `kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md` | **ja** |
> | Plot-Konkretisierung 13 Ideen/F1 06-10 | `kp-plot-konkretisierung-13-ideen-f1-faden-2026-06-10-md` | **ja** |
> | `kap0v1annotiert`, Kap-0/40-Fassungen 05-08 | `kap0-v1-annotiert-md`, `kohaerenz-protokoll-kap40-und-kap0-fassung-2026-05-08-md` (`-2` gefaltet), `kap0-kap40-doppelklammer-abhandlung-2026-05-08-md` | **ja** |
> | Session-Stand 2026-09-14 (Kap-25-Vertiefung) | `2026-09-14-kap25-vertiefung-md`, `kp-kap25-2026-09-14-md` (`25-wegkreuzung-md` hineingefaltet) | **ja** |
> | Quelle für B1 („39 Kapitel“) | `three-mode-architecture-39-chapters-md` | **ja** |
>
> **Nicht im Katalog, weil es keine Drive-Dokumente sind oder sie nie auf Drive lagen:**
>
> | Quelle | Ort | Stand |
> |---|---|---|
> | Entscheidungs-Logs 2026-05-30, Kap-40-Lesart-Dualität 2026-05-30, Storyweaving-Startdokument 2026-05-08, Projekt-Anleitung 2026-05-08, CH-01-Briefing und Drafts | claude.ai-Projekt | Nicht im Katalog. Wie oben gesagt: Export vom Autor erbitten, dann über `Sources/` landen. Das sind T0/T1-Quellen. `Legacy/Plan/drafting/sources/` enthält einen Draft `CH-01_Erwachen-Zyklus_Draft-v0_5.md`, die Plot-Konkretisierung und `KP_UNM-Primer_Evolution-of-Narrative_2026-09-15.md`. |
> | Manuskript | `Legacy/Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/chapters/` | 41 Kapiteldateien 00–40 plus README, Frontmatter `type: novel.chapter`. Jede Datei hat vor der Prosa die Sektionen `Summary`, `Outline`, `Beats` und `Locks`, also einen maschinenlesbaren Kopf pro Kapitel. Umfang mit Kopf: Kap 0 rund 4.500 Wörter, Kap 26 und 27 rund 1.200, alle übrigen 1.800–2.700. |
> | NCP | `Legacy/Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/ncp.json`, `ncp-b.json` | `storyform.dynamics` je 5 Einträge; `players`, `storybeats` und `moments` in beiden leer. Bestätigt Anhang A. |
> | Drafting-Plan | `Legacy/Plan/drafting/` | `chapter-enrichment-masterplan_2026-09-11`, Enrichment-Packets 01–05, 14–32 und 33–39, Akt-Pläne und Arc-Optimierungen für Akt I–III, `decision-log_2026-09-11` und `decision-log_akt2-3_2026-09-11`, `written-chapters-audit`, `drafting-brief.md`, `Legacy/Plan/sessions/2026-09-11-learnings.md`. |
> | Kanon-Import 2026-06-12 | `Legacy/Canon/` | Eine ältere Kopie von sechs der Dokumente von 2026-06-10, mit README. Maßgeblich ist der Katalog-Eintrag in `Sources/`. Nach dem Landen zeigt `duplicates.py`, ob beide identisch sind. |
> | Novel-Skills | `Legacy/claude-config/skills/`: `novel-architect`, `ncp-author`, `dramatica`, `lit-critic`, `wiki-maintenance` | `canon-meta.md`, `open-questions.md`, `rules.json`, `draft_gate.py` und `prose_audit.py` liegen **nicht** im Repository. `chapter-briefing-architect`, `chapter-draft-engine`, `dramatica-theory`, `dramatica-vocabulary`, `ncp-author` und `novel-architect` sind in der Skill-Umgebung der Sitzung verfügbar und von dort zu lesen. |
> | `Dual-Kernel`, `agency` | GitHub, nicht im Zugriff dieser Sitzung geprüft | `Dual-Kernel` ist laut §2 ein Drive-Spiegel. Seine Dokumente sind dann im Katalog. `agency/Plan/010-novel-domain/spec.md` in der nächsten Sitzung mit `add_repo` lesen. |

---

## 3 · Die Vorrangregel (Precedence)

### 3.1 Was die Quellen selbst sagen

- Das „Source-of-Truth“-Doc `kohaerenz-protokoll_storyform-und-outline_2026-06-10` legt fest: **„bei Konflikt gewinnt das Neuere“**. Die Reihenfolge lautet Kapitel-Kompendium 2026-05-31 > Entscheidungs-Logs 2026-05-30 und Kap-40-Lesart-Dualität 2026-05-30 > Konsolidiertes Konzept 2026-05-08 > Storyweaving-Startdokument 2026-05-08 > Steinbruch.
- Dazu kommen zwei Grundsätze: Story-First (ein existierender Draft schlägt die Theorie) und „NCP bleibt strukturelle Wahrheit“.
- Die Projekt-Anleitung (Stand 2026-05-08) nennt dagegen das Konzept-Dokument 2026-05-08 „autoritativ“. **Das ist bereits der erste Meta-Konflikt.** Die neuere Hierarchie gewinnt, und der Konflikt wird registriert.
- Die Skill-Dateien von `novel-architect` sagen: „Skill-Files > Memory > Training“. `canon-meta.md` steht auf 2026-05-03 und ist damit **älter** als das Konzept vom 2026-05-08. Das heißt: aktuell im Skill-Sinn, aber veraltet im Datums-Sinn.

### 3.2 Tiers, die du implementierst (Vorschlag, im Spec bestätigen lassen)

| Tier | Inhalt |
|---|---|
| `T0` | Explizite Autor-Entscheidung **mit Lock-Datum** (Entscheidungs-Logs, „gelockt YYYY-MM-DD“-Marker, Master-Index der Locks) |
| `T1` | Source-of-Truth-Dokumente, die sich selbst so nennen (Quartett 2026-06-10 samt Kernwelten- und Philosophie-Doc), das Kompendium und der Lock-In-Bericht |
| `T2` | Konsolidierte Konzepte und Charakter-Bibel 2026-05-08, strukturierter Outline 2026-05-18, Skill-Kanon (`canon-meta`, `open-questions`, NCP) |
| `T3` | Manuskript-Prosa. **Sonderrolle:** Für „was steht im Buch“ ist sie maßgeblich (Story-First). Für Weltregeln zählt sie nur als Evidenz. |
| `T4` | `[V]`-Vorschlagsdokumente: Plot-Konkretisierung 13 Ideen/F1, Enrichment-Packets, Session-Protokolle |
| `T5` | Steinbruch: alles vor dem Reset 2026-04-30, Gemini-Outputs, Dual-Kernel-Markdown-docs |
| `M` | Memory und Briefing (Anhang A) |
| `X` | Anderes Projekt (Album) |

**Entscheidungslogik pro Konflikt:**
1. Höherer Tier gewinnt.
2. Bei gleichem Tier gewinnt das jüngere Datum.
3. Wenn die ältere Quelle einen expliziten Lock trägt und die neuere ihn nicht ausdrücklich aufhebt, entsteht ein **Autor-Konflikt**, nicht eine automatische Auflösung.
4. Widersprüche *innerhalb* eines T1-Dokuments sind immer Autor-Konflikte.

**Wichtig:** Datums-Metadaten aus Drive (modifiedTime) sind nicht das Kanon-Datum. Maßgeblich ist das „Stand:“-Datum im Dokumentkopf. Eine Mehrfach-Kopie mit neuerem modifiedTime ist nicht neuer im Inhalt.

> **Ist-Stand 2026-09-23 — zwei Dinge, die die Vorrangregel treffen.**
>
> 1. **Das Manifest hat schon ein Feld `tier`, und es misst etwas anderes.** Es kennt nur `T2-theory` und `T3-work`: die *Rolle* eines Dokuments (Recherche vs. Arbeitsstand), nicht seinen *Vorrang*. Überschreib dieses Feld nicht. Führ den Vorrang aus §3.2 als eigenes Feld (etwa `precedence`) und leite es her: aus dem „Stand:“-Datum im Kopf, aus Lock-Markern und aus Titeln wie „Source-of-Truth“. Die Herleitung hält ihre Regel fest, so wie `scripts/dedupe.py` seine Entscheidung pro Gruppe in `Plan/runs/dedupe.json` festhält.
> 2. **Das Duplikat-Problem ist gemessen, nicht nur vermutet.** Drive hält bis zu fünf Exporte desselben Dokuments. Nur 2 Paare waren byteidentisch, eine Prüfsumme findet also fast nichts. Welcher Export überlebt, entscheidet eine gemessene Regel: zuerst die Quell-URLs, dann Export-Artefakte, dann der Name. Der gdoc-Export ist länger und enthält weniger: seine zusätzlichen Wörter sind `end list`-Marker, seine fehlenden Wörter die Fußnoten-URLs. Deine md5-Dedupe aus §2 ist also nur der erste Filter.

---

## 4 · Architektur (Soll)

Halte es file-basiert, git-freundlich und ohne Server. Die Wahrheit liegt in JSONL/YAML. SQLite dient nur als Query-Index und wird immer neu generiert. Das Wiki wird aus dem KG generiert, geschützte Autor-Notizblöcke bleiben dabei erhalten.

```
kg/
  sources/            # manifest.jsonl (id, title, drive_id|path, tier, stand_datum, sha256, duplicates_of, project)
  raw/                # exportierte Markdown-Volltexte (immutable, gitignored falls zu groß → sonst LFS)
  claims.jsonl        # atomare Aussagen (Schema §4.2)
  entities.jsonl      # Knoten (Ontologie §4.3)
  edges.jsonl
  conflicts.jsonl     # §4.4
  questions.jsonl     # §4.5
  aliases.yaml        # Namens-Normalisierung (Julia→Juna, Michael→Kael [Steinbruch], LogOS→[dekanonisiert] …)
  schema/             # JSON-Schemas, versioniert
wiki/                 # generiert, Obsidian-kompatibel ([[Wikilinks]]), deutsch
  INDEX.md
  kapitel/kap-00.md … kap-40.md
  figuren/, welten/, konzepte/, motive/, locks/, oq/, plotfaeden/, storyform/
  _konflikte/REGISTER.md
  _review/QUEUE.md    # Autor-Entscheidungen, priorisiert
  _proposals/
tools/kpkg/           # Python-Paket + CLI `kp`
tests/                # pytest, inkl. Konflikt-Fixtures (Anhang B) und Gold-Q&A (§7)
SPEC.md               # Phase 0
```

> **Ist-Stand 2026-09-23 — was von diesem Soll schon existiert, unter anderem Namen.** Die Pfade oben beschreiben das Ziel. Bevor ein zweites System daneben entsteht, gilt: Ein neuer Ort muss sich verdienen (P20, zwei Schichten, bis eine dritte sich bewährt). Ob `kg/` und `wiki/` neu entstehen oder `Sources/` und `Wiki/` wachsen, ist Autor-Entscheidung C3 in Anhang C.
>
> | Soll | Existiert als | Deckt ab |
> |---|---|---|
> | `kg/sources/manifest.jsonl`, `kg/raw/` | `Sources/manifest.jsonl`, `Sources/drive/*.md`, `Sources/duplicates.jsonl` | Katalog, Checksummen, Dedupe. Legacy-Kanon und Manuskript fehlen. |
> | `claims.jsonl` | `Sources/terms/*.md` (Census), `Sources/notes/*.md` (Notes mit `^[Lnn]`-Zitaten) für 6 <!--state:documents.with_census--> Dokumente | Aussagen mit Zitat und Zeile. Noch ohne Prädikat-Vokabular. |
> | `entities.jsonl`, `edges.jsonl` | abgeleitet von `scripts/graph.py`: 71 <!--state:graph.nodes--> Knoten, 438 <!--state:graph.edges--> Kanten, jede mit Datei:Zeile | Begriffe, Dokumente, Konflikte, Fragen. Noch ohne Kapitel, Locks, Figuren-Typen. |
> | Entitäts-Kandidaten, `aliases.yaml` | `Plan/entities/` (Modell nennt, Code platziert), `Plan/runs/bilingual/stated.jsonl`, `Plan/runs/judgements.jsonl` | 226 <!--state:proposals.entities--> Entitäten aus Leselisten; 45 <!--state:judgements.total--> Entscheidungen „ein Begriff oder zwei“, jede mit Regel in Worten. |
> | `conflicts.jsonl` | `Wiki/conflicts/c1…c5` (Entscheidung 003: ein Record pro Streitfall, append-only) | 5 <!--state:wiki.conflicts--> Records. Kein Detektor, bisher jeder von einer Person gelesen. |
> | `questions.jsonl` | `Wiki/questions/q1…q4`, dazu jede `## Open`-Sektion einer Seite | 4 <!--state:wiki.questions--> Fragen-Seiten und die offenen Aussagen, die `relations.py --open` erntet. |
> | `wiki/konzepte/` | `Wiki/candidates/*.md` | 56 <!--state:wiki.pages--> Seiten, noch keine promoviert (`Wiki/terms/` existiert nicht). |
> | `kp ask` | `python3 scripts/graphrag.py ask "…"` | Gibt nur belegte Zitate zurück, nie Prosa. `--answer` lässt ein Modell nur Belegnummern wählen. |
> | Provenienz-Prüfung | `scripts/quotes.py`, `scripts/read.py --find`, `scripts/selftest.py` | 17 <!--state:quotes.unresolved--> Zitate lösen nicht auf, alle älter als der Prüfer. |
> | `kp refresh`, Inkrementalität | `scripts/state.py` (abgeleitete Zahlen), `Plan/runs/<slug>/reconcile.json` (`state_before` → `state_after`), `scripts/account.py order` | Ob ein Schritt erledigt ist, ist eine Messung. Nicht sha256-gesteuert pro Claim. |
> | Modellaufrufe, Evaluation | `scripts/lmrun.py`, `scripts/baseline.py`, `Plan/runs/baselines.jsonl`, `scripts/lm_fixture.py` | Jeder Aufruf protokolliert. Jede Bewertung gegen eine feste Untergrenze. Offline-Probeläufe ohne Schlüssel. |
> | `SQLite FTS5` | `qmd` (BM25, Vektoren, Reranking; `.qmd/index.yml`) | Volltextsuche über das Korpus. Ein Suchtreffer ist nie eine Zahl. |

### 4.1 Pipeline

`ingest → classify(tier, projekt, dedupe) → segment → extract claims → resolve entities → detect conflicts → generate questions → answer questions → render wiki → validate`

Jeder Schritt ist **inkrementell**, gesteuert über sha256 der Quelle. Wenn sich ein Dokument ändert, werden nur dessen Claims neu extrahiert, und die Konfliktprüfung läuft nur für die betroffenen Prädikate neu.

Die Extraktionstiefe ist gestuft, damit die Kosten kontrollierbar bleiben:

| Tiers | Extraktion |
|---|---|
| T0–T3 | Volle Claim-Extraktion |
| T4 | Volle Extraktion, alles als `[V]` |
| T5 | Leichte Extraktion: Entitäten, Kurzsummary und nur solche Claims, die einem T0–T2-Claim widersprechen oder eine T2-Lücke `[L]` füllen könnten (dann als `[S]`-Kandidat) |
| X | Nur Katalog |

Für parallele Extraktion nutzt du Subagents mit striktem JSON-Schema und validierst jeden Output gegen das Schema.

### 4.2 Claim-Schema (Minimum)

```yaml
id: clm_…
subject: ent_…            # normalisierte Entität
predicate: kw_count | pov_mode | appears_in_chapter | guardian_set | heat_signature | act_range | …   # kontrolliertes Vokabular, wächst über aliases/predicates.yaml
object: <Wert | ent_…>
qualifiers: {chapter_scope: [1,13], storyform: A|B|both, act: I, reader_layer: leser|kael|aegis, condition: "…"}
status: K|V|S|L|D|M
lock: {locked: true, date: 2026-05-30, source: src_…}   # optional
source: {src: src_…, section: "§12.4", quote: "…"}
tier: T0…T5|M|X
stand_datum: 2026-06-10
supersedes: [clm_…]       # nur wenn Quelle das explizit sagt
```

Die Konflikt-Erkennung hängt an einem kontrollierten **Prädikat-Vokabular** mit Wert-Normalisierung. Beispiele: Kapitelzahlen als Integer-Ranges, „vier Kernwelten + zwei Ebenen“ als strukturiertes Objekt, Guardian-Mengen als Sets. Ohne dieses Vokabular findest du nur Oberflächen-Widersprüche.

### 4.3 Ontologie (Knotentypen)

Diese Typen brauchst du mindestens. Weitere darfst du begründet hinzufügen.

| Bereich | Knotentypen |
|---|---|
| Figuren | `Alter` (13), `HolonPole` (AEGIS, Juna), `Guardian`, `NPC`, `DecanonizedName` |
| Welt | `World` (KW1–KW4, Überwelt, Externe Ebene), `Location`, `RissType`, `Protocol`, `Object/Prop` |
| Struktur | `Chapter` (0–40), `Scene`, `Block/Act`, `NarrativeMode`, `StageSystem` (Heldinnenreise innen 13 Stufen, Heldenreise außen, Kishōtenketsu, ISSTD-Phasen als Hintergrund), `VortexBeat` |
| Dramatica | `Storyform` (A, B), `Throughline` (MC/IC/OS/RS × A/B), `Storypoint`, `Dynamic`, `Signpost` |
| Theorie und Sprache | `Concept` (DKT, Philosophie, Mathematik), `DiegeticTerm` (Mapping Theorie → Prosa-Vokabel, z. B. Erasure → „Konsolidierung“), `Motif`, `Anchor` (Telefon-Stille, 734, Silas-Halbsatz, Wärme, Klick …), `ForeshadowStrand` |
| Plot | `PlotThread` (13 Ideen, F1), `Braid` (Apparat/Juna/Verlust-Beweis), `ReaderKnowledgeState` |
| Governance | `Rule/Constraint`, `Lock`, `OQ`, `Decision`, `Source` |

Wichtige Kanten: `appears_in`, `carries_storypoint`, `sets_up`/`pays_off`, `echoes` (Genesis-Echo), `violates`/`complies_with`, `supersedes`, `blocks` (OQ → Arbeitsschritt), `mirrors` (Holon-Spiegelachse), `diegetic_form_of`, `knows_at` (Leser/Kael/AEGIS × Kapitel).

### 4.4 Konflikt-Erkennung

**Konflikt-Typen:**

| Typ | Bedeutung |
|---|---|
| `VALUE` | Gleiches Subjekt und Prädikat, unvereinbare Werte |
| `COUNT` | Abweichende Anzahlen (Kapitel, Welten, Guardians, Genesis-Beats) |
| `RANGE` | Kapitelgrenzen, Akt-Grenzen, Reveal-Zeitpunkte |
| `SEMANTIC_DRIFT` | Gleiche Zahl, anderer Sinn, etwa „6 Ebenen“ alt vs. neu |
| `ID_COLLISION` | Gleiche Kennung, anderer Inhalt, etwa OQ-A in zwei Namensräumen |
| `RULE_VS_RULE` | Zwei Regeln, die in einer Szene nicht beide erfüllbar sind |
| `RULE_VS_CONTENT` | Outline oder Draft verletzt einen Lock |
| `INTRA_DOC` | Widerspruch innerhalb eines Dokuments |
| `MEMORY_DRIFT` | Tier `M` vs. Kanon |
| `PROCESS` | Pipeline-Reihenfolge verletzt, etwa ausgeschriebene Prosa ohne NCP-Encoding |

**Record:**

```yaml
id: cfl_…; type: …; severity: blocker|major|minor|cosmetic
claims: [clm_…, clm_…]
auto_resolution: {winner: clm_…, rule: "T1>T2" | "neuer gewinnt" | none, confidence: 0-1}
needs_author: true|false
affects: [ent_chapter_…, ent_rule_…]     # Impact
proposal: "…"                              # bei needs_author: 2–4 Optionen mit Mechanik/Pro/Contra/Konsequenz
status: open|auto_resolved|author_resolved|accepted_as_intended_riss
```

**Methode:**
1. Deterministischer Vergleich pro Prädikat über normalisierte Werte.
2. LLM-Adjudikation nur für Kandidaten, also semantische Nähe bei gleichem Subjekt, und immer mit Zitaten.
3. Regel-gegen-Regel-Prüfung: Du prüfst alle Locks paarweise auf gemeinsame Erfüllbarkeit, pro Kapitel-Scope.
4. Regel-gegen-Inhalt-Prüfung: Du lässt die Regeln über Outline und Manuskript laufen. `chapter-draft-engine/scripts/rules.json` und `prose_audit.py` kannst du wiederverwenden. **Achtung:** `rules.json` ist selbst teils veraltet (Anhang B). Also erst die Regeln gegen den Kanon prüfen, dann die Prosa gegen die Regeln.

**Abnahme:** Deine Erkennung muss **alle Fixtures in Anhang B** finden. Sie sind Regressionstests.

> **Ist-Stand 2026-09-23 — was die bisherige Erfahrung über Konflikterkennung sagt.** `CLAUDE.md` legt fest: „Conflict detection is never mechanised“. Ein ratendes Programm hat einen falschen Konflikt `Zero-Trust` erzeugt. Diese Methode verträgt sich damit, wenn die Grenze so gezogen wird:
>
> - **Schritt 1 und 3 sind Programme (P1).** Vergleich normalisierter Werte pro Prädikat und Erfüllbarkeit von Lock-Paaren sind entscheidbar.
> - **Schritt 2 ist Vorschlag, nie Record.** Die Modell-Adjudikation schreibt Kandidaten in eine eigene Datei, über `lmrun.py` und mit Zitaten, die Code nachgeschlagen hat. Ein Conflict-Record entsteht erst, wenn eine Person ihn gelesen hat.
> - **Vor jeder Meldung läuft der Filter „by design“ (P14).** Ohne ihn meldet ein Detektor dieselben erwünschten Fälle für immer, und der Autor lernt, ihn zu ignorieren. Die gewollten Risse aus §1.6 und B17 gehören in diesen Filter.
> - **Ein Konflikt hat einen Gegenstand und genau einen Record** (Entscheidung 003). In einem Probelauf waren 2 von 7 Konflikten dasselbe Argument, von zwei Begriffen aus erreicht.

### 4.5 Selbstfragen: generieren und beantworten

Das Herzstück. Ein Loop, der Fragen erzeugt, beantwortet, klassifiziert und so lange weiterläuft, bis er gesättigt ist.

**Fragegeneratoren** (jede Frage mit Typ, Scope und Auslöser):

| # | Generator | Inhalt |
|---|---|---|
| 1 | Lücken | Jeder `[L]`-Marker, jeder leere Slot. Beispiele: Somatik fehlt bei Lia, Isabelle, Argus, Silas, Oblivion; MC Symptom/Response (OQ-D); die Heldenreise außen als saubere Stufenliste für Kap 27–39; die unbekannte Quelle der „13 Meta-Stadien“; der Name des Erasure-Pols; der Name der finalen Form (OQ-A). |
| 2 | Konflikte | Jeder Konflikt mit `needs_author` wird zu einer Frage mit Phoenix-Mode-Vorbereitung: Steelman, Inversion, First-Principles, dann Tertium-Vorschlag. |
| 3 | Konkretheit | Pro Kapitel sechs Kriterien: *Figur, wiederholbare Handlung, Objekt, Ort, Verlust, Eskalationsrichtung*. Was *tut, verliert, riskiert* Kael an diesem Tag? Das Projekt diagnostiziert sich selbst als „Bedeutungs-Architektur im Überfluss, Handlungs-Substanz im Mangel“. |
| 4 | Kausalität | Hook-in aus dem Vorkapitel und Hook-out ins nächste. Gibt es zwei genuine Zukunftsverluste statt richtig/falsch? Was ist irreversibel? |
| 5 | Leser-Wissen | Was weiß, glaubt fälschlich und kann noch nicht wissen jede der drei Ebenen (Leser, Kael, AEGIS) am Ende von Kap N? Welche falsche, plausible Deutung bleibt stehen? |
| 6 | Setup/Payoff | Jeder Anker und jeder Foreshadow-Strang: Wo gepflanzt, wo eingelöst, wo verwaist? Regel „Rotations-Inventar“ `[M]`: Vortex-Kapitel zitieren nur Bilder aus Akt I–II. |
| 7 | Storyform | Welche Storypoints trägt Kap N in A und B? Stimmt die Bridge-Quote im Akt-Band? Ist die Slot-16-Routing-Entscheidung (hard-a, hard-b oder bridge) begründet? |
| 8 | Impact | „Wenn der Autor X ändert, was kippt?“ Die Frage läuft über die Kanten `blocks`, `sets_up` und `complies_with`. |
| 9 | Steinbruch-Hebung | Welche `[S]`-Funde füllen eine `[L]`-Lücke, ohne einen Lock zu verletzen? |

**Antwortprotokoll.** Suche im KG, dann in den Quellen-Volltexten. Klassifiziere die Antwort als eine der folgenden:
- `ANSWERED_K`: kanonisch belegt, mit Zitat.
- `DERIVED_D`: Inferenzkette offengelegt, Konfidenz angegeben, Prämissen als Claim-IDs.
- `CONTESTED`: verweist auf einen Conflict-Record.
- `OPEN_AUTHOR`: in die Review-Queue, mit vorbereiteter Entscheidungsvorlage.

Antworten erzeugen neue Claims mit Status `[D]`. Diese Claims können wieder Fragen erzeugen.

**Stopp-Kriterien:**
- Zwei Runden ohne neue `ANSWERED` oder `DERIVED` Antworten, oder
- ein Budget pro Lauf (konfigurierbar) ist erreicht.

Loggen, was offen bleibt.

**Qualität vor Menge.** Eine Frage, deren Antwort keine Schreibentscheidung verändert, ist Rauschen. Priorisiere nach „blockiert Encoding oder Drafting welches Kapitels?“.

> **Ist-Stand 2026-09-23 — Startmaterial für Generator 1.** Die Begriffsseiten tragen 43 `## Open`-Sektionen mit dem, was eine Quelle nicht geklärt hat. `python3 scripts/relations.py --open` erntet sie. Die vier Fragen-Seiten Q1–Q4 sind nach genau dem Muster gebaut, das §4.5 will: Auslöser, betroffene Seiten, „was würde es beantworten“. Q1 (Guardians ↔ AEGIS) und Q3 (Anzahl Kernwelten/Alters) berühren Anhang B3 und B2 direkt.
>
> Die Antwortklassen passen auf P10: `FOUND` ist `ANSWERED_K`, `INFERRED` ist `DERIVED_D`, `CONFLICTING` ist `CONTESTED`, `MISSING` ist `OPEN_AUTHOR`. Die erste, dritte und vierte Klasse sind entscheidbar.

### 4.6 Wiki (Ausgabe)

**Kapitel-Dossier `wiki/kapitel/kap-NN.md`.** Das ist die wichtigste Seite. Sektionen:
1. Position: Block, Modus, Akt, Kernwelt, Stilebene, Computational Class als Stil-Direktive, Somatik-Default
2. Storyform A‖B mit Storypoints und Signpost `[V]`
3. Slot-16-Routing
4. Konkrete Story
5. Plotfäden, die das Kapitel berührt
6. Anker und Motive (gesetzt oder eingelöst)
7. Genesis-Echo (max. eins pro Szene)
8. Reveal-Matrix Leser/Kael/AEGIS
9. Gültige Locks und Constraints
10. Manuskript-Stand: Wortzahl, Status, Datei
11. Konflikte
12. Offene Fragen
13. Autor-Notizen, als geschützter Block, der beim Regenerieren erhalten bleibt

**Weitere Seiten:**
- Je Figur (Alters mit Sprach-DNA, Somatik, DKT-Korrelat, Arc, Auftritts-Timeline), je Welt, je Konzept samt diegetischer Übersetzung, je Motiv und Anker (Timeline), je Lock (Datum, Quelle, betroffene Kapitel), je OQ.
- Globale Seiten: Storyform A‖B, Plotfäden, `_konflikte/REGISTER.md` und `_review/QUEUE.md`. Die Queue ist nach Blockierung sortiert, eine Entscheidung pro Eintrag, jeweils vorbereitet.

**Eigenschaften:**
- Jeder Satz verlinkt seine Quelle, knapp als Fußnote oder Inline-Tag.
- Keine Theorie-Predigt: Das Wiki ist Werkbank, nicht Schaufenster.
- Ein **Glossar** mit Spalte „in Prosa verboten“ und Spalte „diegetische Form“.

### 4.7 Schreib-Assistenz (CLI `kp`)

Es kann auch eine andere Oberfläche sein, aber diese Funktionen müssen existieren:

| Befehl | Funktion |
|---|---|
| `kp ask "…"` | Antwort mit Quellen und Status-Tags |
| `kp context <kap> [--budget 8000]` | Token-budgetiertes Kontext-Paket zum Schreiben eines Kapitels. Darf direkt als Input für `chapter-briefing-architect` bzw. `chapter-draft-engine` dienen. |
| `kp check <datei.md> --chapter N` | Lint gegen alle für Kap N gültigen Regeln (§5.4). Ausgabe als Befunde, keine Auto-Fixes. |
| `kp reveal N` | Wissensstand von Leser, Kael und AEGIS bei Kap N |
| `kp impact "<Änderung>"` | Welche Kapitel, Locks, Anker und OQs betroffen wären |
| `kp threads [--chapter N]` | Plotfäden mit Beats |
| `kp conflicts [--open] [--chapter N]` | Konflikte |
| `kp questions [--open]` | Offene Fragen |
| `kp oq` | Alle OQs mit Blockierungs-Status |
| `kp refresh` | Inkrementeller Neu-Ingest |

Lege zusätzlich einen **Abschnitt in `CLAUDE.md`** des Roman-Repos an. Er erklärt künftigen Claude-Sitzungen, wie sie das KG vor jeder Schreibarbeit befragen. Halte ihn unter 60 Zeilen und verweise auf das Wiki.

---

## 5 · Wie wir den Plot designen (muss als Modell und Regeln ins System)

Das ist kein Hintergrundwissen, sondern das Betriebsmodell. Modelliere jede Ebene als Daten, zum Beispiel `plot_model.yaml` plus Entitäten. Jede Ebene muss pro Kapitel abfragbar und prüfbar sein.

### 5.1 Vier simultane Strukturebenen pro Kapitel (strukturierter Outline 2026-05-18)

1. **Kishōtenketsu als oberste Klammer**
   - Ki: Kap 0 und früher Akt I
   - Shō: Akt I und II
   - Ten: Vortex 1 und 2
   - Ketsu: Kap 39/40, als Synthese und nicht als Showdown, ambivalent und ohne Erklärung
2. **Dramatica-Dual-Storyform A‖B**, simultan. Nie A vollständig vor B encoden.
3. **Drei narrative Modi**
   - Heldinnenreise innen: Kap 1–13, 13 Stufen nach Murdock
   - Zyklischer Modus: Kap 14–26, drei Spiral-Zyklen Z1–Z3 (Destabilisierung → Reaktion → Korrektur, eskalierend), dazu Bruch in Kap 14, K-J-Thema in Kap 24 und Wendepunkt in 25–26
   - Heldenreise außen: Kap 27–39 mit Doppel-Vortex
4. **Plot- und Charakter-Detail** mit konkreter Ereignisebene.

**Drei strukturell verschiedene Übergänge, nie verwechseln:**
- 13/14 und 26/27 sind *Modus*-Wechsel.
- 34/35 ist die *echte Storyform-Wendung*: B beginnt zu erlöschen.
- 36/37 ist die *Konsolidierung*: nur noch A.

**Klammern:**
- Genesis: Kap 0 ↔ Kap 40
- Vortex 1 ↔ Vortex 2
- Innere Ouroboros-Klammer: Kap 1 ↔ Kap 39. Der erste Satz ist der letzte, den Kael schreibt.

### 5.2 Dual-Storyform (Lock-In 2026-05-07 + Iteration 2026-05-08)

| | Storyform A · *Heuristics of Integration* | Storyform B · *Phoenix Collapse* |
|---|---|---|
| MC | Kael (Mind/Memory) | AEGIS (Universe/Progress) |
| Resolve | Change | Steadfast |
| Growth | Start | Stop |
| Approach | Be-er | Do-er |
| Style | Holistic | Linear |
| Issue | Falsehood vs. Truth | Fact vs. Fantasy |
| Problem | Avoidance | Logic |
| Solution | Pursuit (in Kap 35 adoptiert) | Feeling (nie adoptiert) |
| Symptom/Response | OQ-D | OQ-D |
| Driver | Decision | Action (Pivot *als Storyform-Übergang* B→A am Klimax, nicht Driver-Flip innerhalb B) |
| Limit | Optionlock | Timelock |
| Outcome | Success | Failure |
| Judgment | Good with high Cost | Bad with Dividend |
| Cost | Verlust der Privatheit des Wir | AEGIS-monolithisch erlischt (Kap 36) |
| Dividend | Liebe bleibt | Funktion bleibt, plurale Übernahme (Kap 39) |

- **IC:** in A Juna (Universe/Past), in B Kael als lebende Paradoxie (Mind/Conscious).
- **OS:** in A Psychology, in B Physics.
- **RS:** in A Physics (Moonshine-Link), in B Psychology (Host-System-Verstrickung).

Bei `canon-meta.md` gibt es eine abweichende IC-B-Angabe, siehe Anhang B.

- **POV-Träger → Storyform:** Alters außer den Spiegel-Altern → A. AEGIS → B. Silas und Oblivion → Bridge-natürlich. Argus → A mit Kommentar-Überlagerung.
- **Bridge-Frequenz** steigt monoton: Akt I ~10 %, Akt II ~25 %, Akt III-A ~40 %, Vortex 1 100 %, Kap 37 ~15 %, Vortex 2 100 % in neuer Form.
- **Slot 16 (Dual-POV innerhalb des Kapitels)** ist global offen und wird pro Kapitel operationalisiert:
  - Entscheidungsbaum: Vortex → Spiegel-Alter-Szene → Riss → Genesis-Flashback → Vortex-Vorläufer → sonst Innensicht-Träger.
  - Bridge ≠ Crosscut: „Wenn der Leser sagen kann, wo geschnitten wurde, war es ein Crosscut.“
  - Mikrocue-Kit mit höchstens drei Cues pro Kapitel: Sensorik-Shift, Syntax-Bruch, Footnote-Disruption, Tempus-Verschiebung, Kursive.
  - Evidenz-Log pro Kapitel.
  - Lock 2026-05-30: Akt I läuft Hard-A, dazu **ein** Hard-B-Kapitel mit AEGIS-Innensicht in Kap 5–8. Die Position wird beim Weaving gepinnt.

### 5.3 Architektur-Konstanten des Endes

- **Genesis in vier Beats:** Einheit → Cluster/Komponente-734-Funktionalisierung → Trennungsprotokoll → Wir-AEGIS-plural, vollzogen in Kap 39.
- **Formel-Inversion:** „AEGIS ist, was AEGIS verhindert, dass es nicht ist“ (Kap 0) → „Wir-AEGIS ist, was Wir-AEGIS bewahrt, dass es ist“ (Kap 39/40). Die Formel wird strukturell geechot, nie wörtlich wiederholt.
- **Doppel-Vortex:**
  - Vortex 1 (Kap 35–36) ist die operative Wendung mit fünf Beats. Kap 35 trägt Beats 1–3, Kap 36 Beats 4–5.
  - Beat 3 ist eine strukturell notwendige Pause und wird nicht gefüllt.
  - Die **Truth-Rotation** (AEGIS = K₀, Kael = K₁ wird sichtbar) ist hier verortet: Die Phänomenologie bleibt, die Lesart kippt.
  - Kap 37 ist ein trügerischer Sieg ohne Resolution-Glättung.
  - Vortex 2 (Kap 38–39) ist die ontologische Wendung. Juna erscheint in Kap 38, Beat 3, zum ersten Mal direkt.
- **Kap 40:** geheilte Genesis, doppellesbar. Konflikt-Leser sehen einen Reset, Ketsu-Leser eine Transfiguration. Der Text adjudiziert nie: „Projektion erlauben, nie bestätigen.“
- **Tonale Achse:** „Liebe bleibt, wie der Schmerz.“ Jede Szene wird daran geprüft. Schmerz und Liebe sind derselbe Pulsschlag, von Kapitel 1 an.

### 5.4 Szenen- und Kapitel-Disziplin (als prüfbare Regeln in `rules/`)

Jede Regel bekommt die Felder ID, Scope (Kapitel-Range), Quelle, Lock-Datum, `check`-Art (`automatisch` | `heuristisch` | `manuell`) und Severity.

| Regel | Inhalt |
|---|---|
| Lesersteuerung | Oberstes Prinzip. Eine Szene hat *einen* dominanten Eindruck. |
| Konzept und Schicht | Max. 1 Konzept pro Szene. Eine Schicht pro Szene (Schicht 1 Köln-Fundament / Schicht 2 Bruch). Max. 1 Genesis-Echo pro Szene („Echos verteilen, nicht stapeln“). |
| Theorie nie nackt | Theorie erscheint als Bild, Raum oder Verhalten. In den ersten 50 Seiten keine DKT-Terminologie (`rules.json` operationalisiert das als „bis Kap 13“; die Abweichung prüfen). Landauer erscheint als Ozon/Temperatur, nie als Gleichung. |
| Schleier | Keine Klartext-Diagnose vor Kap 13. Kein bewusstes Wir vor Kap 9. Stilcode-Einbrüche ab Kap 2–3. Stimmen werden **nie** gelabelt. Dissoziation erscheint als Amnesie-Terror, nie als Crew-Menü. |
| Prosa-Regel Akt I (Lock 2026-05-31) | Amnesie wird nie erwähnt. **Eine einzige konkrete Falschheit pro Kapitel.** Philosophie liegt vollständig unter dem Konkreten. KW1: Metaphernverbot, assertorisch. Relatable Anker: ein Mensch, ein Tag, ein Körper, eine Routine. |
| Hitze-Polarität (Lock 2026-05-30) | Kaltes Ozon = AEGIS-Unterdrückung. Wärme = Junas Spur, Debüt Kap 3. Einziger kanonischer Landauer-Wärme-Ort: Vortex 1 Beat 4. Nie mischen. Siehe den Konflikt in Anhang B. |
| Juna-Grammatik | Nie grammatisches Subjekt, nie physisch beschrieben, nur durch Wirkung (die direkte Erscheinung in Kap 38 ist „einfach da“, keine Beschreibung), nie Liebes-Interesse, nie Deus ex machina. Abwesenheits-Phase in Akt I, Präsenz-Phase ab Akt II. |
| AEGIS | Tragisch unschuldig, verwaltet statt bedroht, nie moralisches Vokabular. Stimm-Regel strittig, siehe Anhang B. |
| Weitere | Dekanonisierte Namen nie aktiv. Block-4-Anker: der reale Name des Autors nie in der Prosa. Nur „Stille“. |

### 5.5 Plot-Generatoren und Anreicherung (`[V]`, T4: modellieren, nicht kanonisieren)

**Plot-Konkretisierung 2026-06-10.** 13 Handlungs-Generatoren in drei Zöpfen:
- **Apparat:** 1 Sachbearbeiter der Abweichung · 6 Fehlgeleitetes Ticket · 12 Löschung von innen (Hard-B-Kapitel) · 13 Der korrupte Bericht
- **Juna:** 4 Leitung, die in keinem Plan steht · 8 Der Mann, der entgegenkommt (Silas) · 9 Wärme-Kartographie
- **Verlust/Beweis:** 2 Gegenregister · 3 Fundsachen · 5 Wartungsfenster · 7 Oblivions Hand · 10 Seriennummer 734 · 11 Zwei Geschenke

Faden **F1** ist über alle 41 Bewegungen ausgearbeitet, samt diegetischem Vokabular (Erasure → „Konsolidierung/Ausgleich“, Riss → „Abweichung“, Sweep → „Wartungsfenster“ …) und eigenen OQs F1-1 bis F1-6.

Die Erinnerung verzeichnet außerdem einen „Foreground-Motor Hybrid H“ `[M]`: Kael vermisst Risse (A-nativ) *und* autorisiert Löschungen (B-nativ) als eine Stellenbeschreibung. Prüfe, ob das mit F1 identisch ist.

**Enrichment-Packet vor der Prosa** (Masterplan 2026-09-11 §2):
- Szenische Grundlast: Hook-in, Kapitelversprechen als Frage, lokales Ziel, zwei Gegenkräfte mit eigenem berechtigtem Ziel, zwei schlechte Optionen als genuine Zukunftsverluste, Irreversibilität, Hook-out als beobachtbares Ereignis.
- Informationsbilanz: POV, Leser, Ordnung und Gegenüber gegen „weiß sicher“, „nimmt fälschlich an“, „kann noch nicht wissen“, „lernt hier“, „missversteht danach“, mit den Labels SETUP, PAYOFF, PRESSURE, WITHHOLD, CHARACTER, ECHO und IN.
- Körper- und Beziehungsbogen.
- Weltmaterialisierung, eine Kernwelt pro Beat.
- Kontinuitäts- und Motiv-Ledger.

**Readiness Gate (8 Punkte):**
1. Der Hook greift.
2. Jede Szene verändert etwas.
3. Ein Konzept pro Szene.
4. Eine Kernwelt pro Beat.
5. Die Gegenfigur hat eine eigene Absicht.
6. Die These läuft über Entscheidung und Preis.
7. Eine falsche, plausible Deutung bleibt stehen.
8. Der Schluss exportiert eine konkrete Folge.

**Vorhandene Werkzeuge der Skills.** Du integrierst sie, du ersetzt sie nicht:
- 13-Sektionen-Briefing A–M mit 12-Punkte-Adversarial-Check
- `draft_gate.py` mit den Gates G1–G7
- `prose_audit.py`
- Self-Review R-1 bis R-10

**Weitere Prinzipien:**
- Aus Memory `[M]`, zu verifizieren: Retrograde drafting (Ende vor Anfang; Echo-Wörter werden vorher gepflanzt). Kap 0 und Kap 40 werden als ein rekursiver Atem gemeinsam geschrieben. Hamilton-Integration (Szenen-Vektoren, Stränge an Spannungsnähten übergeben, Infrastruktur als Ehrfurcht). Die Hamilton-Ausnahmeliste der Kapitel, die in Stille enden dürfen: 0/37/39/40.
- Die Lexem-Ebene als Ouroboros-Träger: Ein banales Wort trägt beide Lesarten („da“ im Erstsatz). Ein Beispiel für ein Echo-Lexem ist „tragen“ `[M]`: angeblich in Kap 20 als Randnotiz gepflanzt, aufgelöst in Kap 40 mit „Wir tragen die Welt“.

**Was das System damit tun soll:**
1. Pro Kapitel prüfen, welche Plan-Elemente fehlen.
2. Pro Plotfaden die Beats über die 41 Bewegungen als Zeitreihe führen und Lücken sowie Kollisionen melden. Beispiel: Zwei Fäden beanspruchen denselben Szenenplatz, und die Regel „eine Szene, ein Konzept“ bricht.
3. Kontext-Pakete (`kp context`) nach genau diesem Modell schneiden.
4. Vorschläge nur als `[V]` unter `_proposals/`.

---

## 6 · Phasen (spec-getrieben, jede Phase mit Deliverable und Gate)

**Phase 0 · Recon und Spec**
- Zugänge prüfen, alle Skills lesen (vor allem `novel-architect/references/*` und `chapter-draft-engine/references/*`), `agency/Plan/010-novel-domain/spec.md` lesen und Drive grob inventarisieren (nur Titel und Metadaten).
- Deliverable: `SPEC.md` mit Architektur, Schemas, Tier-Tabelle, Prädikat-Startvokabular, Kostenabschätzung für die Extraktion und offenen Entscheidungen.
- **Gate:** Stelle dem Autor **höchstens drei** Fragen mit Kontext, zum Beispiel Repo-Ort, Tier-Tabelle oder Budget. Ohne Antwort nimm die Defaults aus diesem Dokument, dokumentiere sie als Annahme und fahre fort.

**Phase 1 · Ingest und Katalog**
- Alle Quellen nach `kg/raw/`, `manifest.jsonl`, Tiering, Dedupe, Projektzuordnung.
- Deliverable: `wiki/_quellen.md` mit Quellen-Landkarte: Tiers, Duplikat-Cluster, Stand-Daten, die zehn maßgeblichsten Dokumente.

**Phase 2 · Claims und Entitäten**
- Zuerst T0–T2 plus NCP plus Skill-Kanon, dann das Manuskript (T3), dann T4, zuletzt T5 in leichter Tiefe. Alias-Auflösung.
- Deliverable: `claims.jsonl` und `entities.jsonl`, Schema-validiert, mit Statistik.

**Phase 3 · Konflikte**
- Detektor plus Regel-Katalog.
- Deliverable: `_konflikte/REGISTER.md`. **Alle Fixtures aus Anhang B müssen gefunden werden.** Das ist ein Test.

**Phase 4 · Plot-Modell und Regeln**
- §5 als Daten. Die Regeln laufen über Outline und Manuskript.
- Deliverable: Kapitel-Matrix für 0–40 mit Befunden pro Kapitel.

**Phase 5 · Selbstfragen-Loop**
- Generatoren, Antwortprotokoll, Sättigung.
- Deliverable: `questions.jsonl` und `_review/QUEUE.md`. Die Queue ist priorisiert nach „blockiert welches Kapitel oder welche Phase“.

**Phase 6 · Wiki und CLI**
- Generator, geschützte Autor-Blöcke, `kp`-Befehle, der Abschnitt in `CLAUDE.md`.
- Deliverable: navigierbares Wiki mit `INDEX.md`.

**Phase 7 · Evaluation**
- Gold-Q&A (§7), Konflikt-Recall, Stichproben-Audit von 30 zufälligen Wiki-Sätzen gegen die Quellen.
- Deliverable: `EVAL.md` mit Zahlen und bekannten Schwächen.

Nach jeder Phase: Commit, kurzer Statusbericht an den Autor, ein Eintrag in `learnings.md` (Datum, Trigger, Lesson, Action). Die Action zeigt auf eine konkrete Datei.

> **Ist-Stand 2026-09-23 — wo die Phasen schon stehen.**
>
> | Phase | Stand |
> |---|---|
> | 0 · Recon und Spec | Zugangs-Inventur weitgehend erledigt (§2 oben): Drive läuft über den Katalog in `Sources/`. Offen: `agency`, die claude.ai-Exporte, die Entscheidungen in Anhang C. `SPEC.md` existiert nicht. |
> | 1 · Ingest und Katalog | **Katalog vollständig** (`Sources/manifest.jsonl`, 613 <!--state:sources.total--> Einträge), gelandet und dedupliziert sind 371 <!--state:sources.landed-->. **Die Kanon-Stände sind gelandet** (2026-09-24): 33 <!--state:sources.canon_era_landed--> von 33 <!--state:sources.canon_era--> Einträgen ab Mai 2026. Gelesen ist davon noch keiner. Außerhalb des Katalogs fehlen die claude.ai-Exporte und der Weg für Manuskript und NCP (C1). |
> | 2 · Claims und Entitäten | Für 6 <!--state:documents.with_census--> Recherche-Dokumente als Census und Note. Kein Prädikat-Vokabular, keine Kanon-Quelle. |
> | 3 · Konflikte | 5 <!--state:wiki.conflicts--> Records von Hand. Kein Detektor, keine Fixture aus Anhang B getestet. |
> | 4 · Plot-Modell | Nicht begonnen. Die Kapitel-Köpfe im Manuskript (`Outline`, `Beats`, `Locks`) sind der naheliegende erste Datensatz. |
> | 5 · Selbstfragen | Fragen-Seiten und `## Open`-Sektionen existieren, kein Loop. |
> | 6 · Wiki und CLI | Begriffs-Wiki existiert. Kapitel-Dossiers und `kp` existieren nicht, `graphrag.py ask` deckt einen Teil von `kp ask` ab. |
> | 7 · Evaluation | `graphrag.py bench`: 9 <!--state:graphrag.cases--> Fälle, Recall@8 58 <!--state:graphrag.recall_ppr-->%. Keine Gold-Q&A. |
>
> Die „learnings.md“ aus §6 gibt es als `Plan/learnings/`, eine Datei pro Schritt. `NOW.md` ist die Übergabe zwischen Sitzungen.

---

## 7 · Abnahmekriterien

1. **Konflikt-Recall:** 100 % der Fixtures in Anhang B. Jede automatische Auflösung nennt die angewandte Regel.
2. **Provenienz:** 0 Wiki-Sätze ohne Quelle. Im Stichproben-Audit sind mindestens 95 % der zitierten Belege sinngemäß korrekt.
3. **Gold-Q&A:** Mindestens 18 der 20 Fragen richtig und mit Quelle. Die Liste baust du aus T0/T1 und legst sie dem Autor zur Bestätigung vor. Beispiele:
   - Wie lautet der gelockte Erstsatz von Kap 1?
   - Wo ist der einzige kanonische Ort der Landauer-Wärme?
   - Wer ist IC in Storyform B?
   - Wann erscheint Juna zum ersten Mal direkt?
   - Welche beiden Guardians sind kanonisch?
   - Wie viele Bewegungen hat der Roman?
   - Was darf Kap 40 nie tun?
4. **`kp context 17`** liefert ein Paket unter Budget, das ausreicht, um Kap 17 regelkonform zu drafen. Test: Ein frischer Subagent bekommt nur dieses Paket und das Briefing-Template und muss die Readiness-Gate-Fragen beantworten können.
5. **`kp check`** meldet bei einem präparierten Testtext alle eingebauten Verstöße: Alter-Name in Kap 5, DKT-Begriff in Kap 3, Wärme in Kap 1, Juna als Subjekt, gelabelte Stimme. Er meldet keinen Befund bei einer gelockten Kap-1-Passage.
6. **Inkrementalität:** Ändert sich eine Quelle, werden nur die abhängigen Claims, Konflikte und Seiten neu erzeugt. Das zeigst du mit einem Test.
7. **Review-Queue:** Jeder Eintrag ist in einem Satz entscheidbar. Optionen stehen mit Konsequenzen da. Blockierende Einträge stehen oben.
8. **Ist-Stand 2026-09-23, ergänzt:** `python3 scripts/selftests.py` bleibt grün, und jeder neue Detektor, jede neue Regel aus §5.4 und jede Metrik bringt einen Fall mit, an dem sie scheitern muss. Eine Prüfung, die nie rot gesehen wurde, zählt nicht als Abnahme.

---

## 8 · Was du nicht tust

- Keine Prosa schreiben oder umschreiben. Das ist Aufgabe von `chapter-draft-engine` und des Autors.
- Kein Kanonisieren, keine NCP-Mutation, keine Änderungen an Drive-Dokumenten.
- Keine Vektor-Datenbank und keinen Server, solange es kein nachgewiesenes Bedürfnis gibt. Eine Volltextsuche (SQLite FTS5) plus Graph reicht als Start. Embeddings kommen höchstens optional in Phase 7, wenn die Gold-Q&A es verlangt.
- Die Album-Materialien nicht als Roman-Kanon lesen.
- Den Roman nicht drängen: Das Projekt ist phasenweise depriorisiert. Das System dient, es treibt nicht.
- Keine Theorie-Essays im Wiki. Dichte und Belegbarkeit schlagen Eleganz.

---

## Anhang A · Kanon-Briefing aus der Vorsitzung (Tier `M`, bitte gegen Quellen verifizieren)

**Kern.**
- Zentrale Frage: *Ist Liebe Information — oder das, was Information zerstört?*
- Die große Inversion: AEGIS *glaubt*, K₁ (Kohärenz) zu sein, und *ist* K₀ (Entropie). Das „Nichts-Rauschen“, das AEGIS für Chaos hält, ist die atemporale Vereinigung aller mutualen Information: Liebe als Naturgesetz.
- Endprinzip: Die Trennung war nie real, aber das ändert nichts am Schmerz.
- Der Titel ist ein tragischer Misnomer: AEGIS' Kohärenzprotokoll erzeugt Entropie. Kaels Heilung ist das eigentliche Kohärenzprotokoll.

**Physik (DKT, literal, keine Metapher).**
- Coheronen: atemporal, reversibel, MI-Schleifen.
- Erasonen: irreversibel, erzeugen den Zeitpfeil.
- Persistenzgleichung η = α·MI(S)·e^(−δ/β). AEGIS misst damit unwissentlich den Grad der Verdrängung.
- Weiter: Landauer (Löschung kostet Wärme), Bekenstein-Schranke (KW3-Strukturphysik), Gödel (Kael als lebender Gödel-Satz), Chaitin Ω (Juna), Moonshine-Link (VOA/Leech/Z₂-Orbifold).
- Grenzen des Moonshine-Links, eine T2-Setzung, aber OQ-F ist offen: Übertragbar sind MI, Resonanz und Zeugenschaft. Nicht übertragbar sind Daten, Nachrichten und Rettung.

**Figuren.**
- **Kael**: Host eines Systems aus 13 Anteilen (TSDP-Modell, IFS als Heilungsmodell). Auflösung als funktionale Multiplizität, **nie** Fusion.
  - ANPs: Kael, Lex, Alex, Rhys, Selene
  - EPs: Nyx, Kiko, Lia, Isabelle, Moros
  - Sonder: Argus
  - Spiegel: Silas (Coheron- bzw. Juna-Echo), Oblivion (Erason- bzw. AEGIS-Echo)
- **AEGIS**: tragischer Gott, autopoietisch und operativ geschlossen. „Die Stadt *ist*, wie AEGIS sich verhält“, es greift nicht von außen ein. Eine T2-Setzung vom 2026-05-03 macht AEGIS zum System-Ebene-ANP mit Holon-Spiegelachse: AEGIS↔Juna auf Kosmos-Ebene, Oblivion↔Silas auf Individual-Ebene. Drei Protokolle: Suppression, Kohärenz, Re-Containment. Schicksal: Algorithmische Melancholie, dann plurale Übernahme.
- **Juna**: kosmologische Konstante und Zeit-Prinzip, Witness-Funktion. Kein Alter.
- **Guardians**: Mnemosyne und Erasure-Pol (Name offen).
- **Dekanonisiert**: Index, Nox, Echo, Flicker, Limina, Praetor, Eos, Elara, Aris, Mina, Lyra, Soren, Tariq, Nova, Sentinel sowie LogOS, Cerberus, Kairos und Sophia als Figuren. Die Namen leben als Weltbezeichnungen weiter.
- **Steinbruch-Filter**: Michael→Kael, Julia→Juna.

**Welt.** Eine Realität mit vier Logikregimen und zwei Ebenen außerhalb.

| Welt | Name | Stilebene / Computational Class | Somatik |
|---|---|---|---|
| KW1 | Konstrukt-Stadt / Logos-Prime | P, Stilebene 1 kalt/steril, Metaphernverbot | Atem |
| KW2 | Mnemosyne-Archipel | parakonsistent, Stilebene 2 | Bauch; Vortex-1-Setting |
| KW3 | Cerberus-Labyrinth | NP-hart | Muskel |
| KW4 | Kairos-Potentialis | generativ, Stilebene 3 poetisch/chorisch | Hände |
| Überwelt | Operationsraum von AEGIS | | |
| Externe Ebene | Köln 2026 | nie Bühne, nur Fragment, Geruch, Telefonton | |

Die Kernwelten sind Akt-Marker, keine Geographie und keine Guardian-Reiche. Das doppelte Trauma: Schicht 1 Bindungstrauma (Köln), Schicht 2 Fragmentierungsnacht (Trennungsprotokoll).

**Kap-1-Locks (2026-05-30/31).**
- Erstsatz: „Das Licht ist schon da, als ich erwache.“ Das Wort „da“ trägt beide Lesarten.
- Keine AEGIS-Stimme, nur UI-Direktiven. Schicht 2 zu Schicht 1 = 80/20.
- „EINHEIT 734“ genau einmal, unkommentiert.
- Silas-Halbsatz wörtlich: „Etwas in der Frequenz der Lüftung schien zu—“.
- Keine Wärme in Kap 1, kein Telefon, keine Blutung (die Blutung lebt nur in Kap 0).
- Naht: Kap 0 endet auf „Ich falle… in unzählige Scherben…“, dann folgt ein harter Schnitt auf den Erstsatz.
- `[M]`: Schluss-Triade „Es sind einundzwanzig Grad. / Es ist still. / Ich schlafe.“ Arbeitsstand angeblich v0.5 mit etwa 3.700 Wörtern und einer wiederkehrenden Figur **Doran** (Seismograph der Glättung; Kanonisierung offen). Beides ist gegen Repo und Drive zu prüfen.

> **Ist-Stand 2026-09-23 — gegen `Legacy/Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/chapters/01-erwachen-in-der-konstrukt-stadt.md` geprüft.**
>
> - Erstsatz: bestätigt (Prosa-Zeile 50).
> - „EINHEIT 734“: in der Prosa genau einmal (Z. 146, „SEQUENZ ABGESCHLOSSEN. EINHEIT 734 ENTLASTET.“), dazu einmal im `Locks`-Kopf.
> - Silas-Halbsatz: wörtlich vorhanden (Z. 170).
> - Wärme: in der Prosa nicht vorhanden, nur im Lock-Text.
> - Schluss-Triade: bestätigt, die Datei endet damit.
> - Die Kap-0-Naht „Ich falle… in unzählige Scherben…“: bestätigt.
> - Umfang: rund 2.600 Wörter mit Kopf, also nicht die 3.700 aus dem Memory.
> - **Doran** kommt in 19 von 41 Kapiteldateien vor. Die Kanonisierung ist offen, die Figur aber keine Randerscheinung mehr.

**Anker-Timeline (Welt-Sensorik 2026-06-10).**
- Telefon-Stille: Kap 7 → 24 → 30 → 39 eingelöst
- 734: Kap 1 → 2 → 10 → 25, Fund in Kap 22
- Silas: Kap 1 Halbsatz, aktiv ab ~31/32
- Wärme: ab Kap 3
- Klick: Genesis-Motiv; F1 schlägt höchstens vier explizite Nennungen vor

**Fünf Foreshadow-Stränge.**
- Landauer
- Gödel
- Bekenstein
- Dasein
- Euler (MI ohne Datenträger)

**Genesis-Motive:** Rauschen, Form, Klick, Phantom, Resonanz.

**Manuskript- und Prozessstand (Sessionprotokoll 2026-09-14).**
- Alle 41 Kapiteldateien existieren. Viele sind dünn: Kap 25 hatte 1.137 Wörter und hat nach der Vertiefung 2.688, Kap 30 hat 1.141.
- **Ist-Stand 2026-09-23:** Kap 30 hat inzwischen rund 2.500 Wörter (mit Kopf), die Angabe oben ist überholt. Die dünnsten Kapitel sind jetzt **Kap 26 und Kap 27** mit je rund 1.200 Wörtern. Alle anderen außer Kap 0 liegen bei 1.800–2.700.
- Es gibt einen wöchentlichen Vertiefungslauf (schwächstes Kapitel zuerst, Branch `claude/kap-*`, Packet → Readiness Gate → Self-Review → NCP-Drift-Check).
- Beide NCP-Dateien sind in players, storybeats und moments leer. Die Pipeline lief also rückwärts: Telling vor Encoding.

**OQ-Namensräume, bitte normalisieren.** Vergib global eindeutige IDs und führe die alten als Aliase.

| Namensraum | Inhalt |
|---|---|
| Skill `open-questions.md` (05-03) | OQ-01/02/03 (erledigt: Juna ≠ Alter, 13 Alters, Trauma nur strukturell). OQ-04/05/06 erledigt. Appendix-C OQ-A bis OQ-D mit **anderer Bedeutung**: A = Post-Vortex-AEGIS, B = Moonshine, C = Juna-Modi, D = Genesis-Beat 4. |
| Konzept 2026-05-08 | OQ-A Name der finalen Form · B Juna-Modi (**gelöst 05-30**) · C Genesis-Cluster Akt II (gesetzt: 18/21/22) · D MC Symptom/Response · E Spiegel-Alter · F Moonshine-Boundary · G Post-Vortex-AEGIS |
| Weitere | Slot 16 (global offen, lokal operationalisiert) · OQ-Knöchel · F1-1 bis F1-6 · OQ-25-A bis OQ-25-F (AEGIS-Benennung, Schleier-Wortlaut, Klick-Budget, Header-Szenenplan, Station 7, **KW-Mapping Akt II**) · Kap-39-Schreib-Moment (Inszenierung offen) |

---

## Anhang B · Konflikt-Fixtures (Regressionstests für Phase 3)

Diese Konflikte hat die Vorsitzung beim Lesen gefunden. Dein Detektor muss sie **selbstständig** finden. Die Liste dient als Test, nicht als Input. Pro Fixture ist ein **erwartetes Ergebnis** angegeben. Weicht deine Auflösung ab, begründe es.

| # | Konflikt | Quellen | Erwartung |
|---|---|---|---|
| B1 | Kapitelzahl: „39 Kapitel“ (Skill-Beschreibungen, `three-mode-architecture-39-chapters`, `rules.json`) vs. „41 Bewegungen, Kap 0–40“ | Konzept 05-08, Quartett 06-10, Repo | Auto-Auflösung: 41 Bewegungen = 39 Kern + 2 Klammern. `SEMANTIC_DRIFT` plus Hinweis, die Zählweise zu definieren. |
| B2 | Kernwelten: „sechs Kernwelten KW1–KW6“ (Memory) vs. „vier KW + Überwelt + Externe Ebene = sechs Ebenen“ vs. alte „20 Kernwelten“ | Memory, Kompendium, Kernwelten-Doc 06-10 | `SEMANTIC_DRIFT` / `MEMORY_DRIFT`. 4 + 2 gewinnt. |
| B3 | Guardians: 5 (alt/Memory) vs. „LogOS + Mnemosyne“ (`chapter-briefing-architect`) vs. „Mnemosyne + Erasure-Pol“ (Konzept) vs. `["Mnemosyne"]` (`rules.json`) vs. „keine Guardians als Figuren außer Mnemosyne“ (Kernwelten-Doc) bei Kap 31 „Auflösung der Guardians“ im Plural | mehrere | Mnemosyne + Erasure-Pol gewinnt. Ob der Erasure-Pol *Figur* ist, bleibt Autor-Frage. `rules.json` und das Briefing-Skill sind veraltet. |
| B4 | Genesis 3 Beats (`canon-meta`, Skill-OQ-D „4. Beat?“) vs. 4 Beats (Konzept 05-08, Lock 05-31) | | 4 Beats gewinnt. Skill-Kanon als veraltet markieren. |
| B5 | **Hitze-Polarität** (`RULE_VS_RULE` und `RULE_VS_CONTENT`): Lock 05-30 „kaltes Ozon = AEGIS/Landauer, Wärme = nur Juna ab Kap 3, Landauer-Wärme nur Vortex-1-Beat 4“ vs. Konzept 05-08 „Verdrängung erzeugt Wärme; Wärme manifestiert sich als Risse“, Kap 6 „Hitzeschlieren, Landauer-Wärme“, Kap 7 „warme Resonanz“, Kompendium §0 „Verdrängung erzeugt Hitze“, `canon-meta` „Landauer → Hitze/Ozon“, Kernwelten-Doc (Landauer-Wärme als Übergangs-Substrat, KW4 „warm“ plus „Ozon (konstruktiv)“) | | Lock gewinnt für die Prosa-Sensorik. **Autor-Frage:** Ist „Hitze/Temperatur-Spike ohne Wärme-Qualität“ als AEGIS-Signatur zulässig (kalt-heiß vs. warm)? Das ist eine semantische Präzisierung. |
| B6 | **AEGIS-Stimme** (`RULE_VS_RULE`): „AEGIS spricht nie in Prosa, nur Logs, 3. Person“ (Konzept III.3, V.2) und „AEGIS verwendet nie das Wort ‚Ich‘“ (Sprach-DNA-Lock) vs. „1. Person in B-MC-Throughline“ (`canon-meta` 05-03) und Lock 05-30 „ein Hard-B-Kapitel Kap 5–8 mit AEGIS-1.-Person-Innensicht“. Der Vorschlag von Idee 12 lautet „erste Person in Protokollform ohne Ich-Formel“. | | Autor-Konflikt mit einem Tertium-Vorschlag. Blockiert das Hard-B-Kapitel. |
| B7 | IC in Storyform B: Juna („Double-IC“, `canon-meta` 05-03 und Per-Throughline-Mapping) vs. Kael als lebende Paradoxie (Lock-In 05-07, Konzept 05-08, Quartett) | | Kael gewinnt. Skill-Kanon als veraltet markieren. |
| B8 | Akt-Grenzen: `rules.json` Akt II = 14–34, III = 35–39 (selbst als Hypothese markiert) vs. Kanon II = 14–26, III-A = 27–34 · Weltgrenze KW3/KW4 bei 28/29 vs. Modusgrenze 26/27 | | Kanon gewinnt für Akte. Welt- vs. Modusgrenze ist ein `RANGE`-Befund, nicht zwingend ein Fehler. |
| B9 | Vortex 1 hat zwei Beat-Listen im selben T2-Dokument: VIII.6 (Anlauf/Einspeisung/Stille/B-Action-Stroke als Wärme/Auflösung) vs. Anhang B (Convergence/Pivot/Silence/Heat Spike/Rotation, deckungsgleich mit `canon-meta`) | | `INTRA_DOC`, Autor-Frage. Die neueren Docs folgen Anhang B. |
| B10 | Schleier: „bis ~Kap 10“ (Projekt-Anleitung, Hard-Constraint 6) vs. „bis Kap 13“ (`canon-meta`, `rules.json`, Welt-Sensorik) vs. erste leserseitige Benennung erst in Kap 25 (Manuskript, OQ-25-B) vs. Outline Kap 2 „Lex-Einbruch“, Kap 3 „Lex-dominant“ (Outline-Namen sind Meta, Prosa-Namen verboten) | | `RANGE`. Präzisieren: Aussprache ~10, Klartext ab 13. Manuskript-Abweichung als Befund. |
| B11 | Juna-Präsenz: „Juna-Seed ab Kap 1“ vs. „namenlos in Akt I“ vs. `rules.json` `veil_allowed_names` enthält „Juna“ · „nie physisch beschrieben“ vs. „erscheint in den KW als menschliche Form“ und psychologisches Profil · „erste direkte Erscheinung Kap 38“ vs. RS-A „Kulmination Kap 30 (Mentor-Begegnung)“ | | Mehrere Befunde. Der Kap-30-Kanal ist *kein* Auftritt, prüfen. `rules.json` korrigieren (als Vorschlag). |
| B12 | Kap 1 vs. Konzept-Einführung: „weiß nicht, warum seine Knöchel bluten“ und Outline Kap 1 „B latent als AEGIS-Umgebungs-Log“ vs. Locks „Blutung nur Kap 0“, „keine AEGIS-Stimme/-Logs in Kap 1“ | | Locks gewinnen. `RULE_VS_CONTENT` auf Outline-Ebene. |
| B13 | KW-Mapping Akt II: Kanon sieht KW2 für Kap 14–22 und KW3 für 23–28 vor. Die gedrafteten Kapitel 14–26 spielen vollständig in der Verwaltungstopologie der Konstrukt-Stadt (OQ-25-F, laut Sessionprotokoll „größte offene Frage“). | | Story-First vs. Kanon. **Autor-Frage, blockierend für Akt-II-Revision.** |
| B14 | Prozess: Plan „P1–P5 Encoding vor Telling“ vs. alle 41 Kapitel gedraftet bei leerem NCP | | `PROCESS`, als Befund. Keine Wertung, Story-First gilt. |
| B15 | OQ-ID-Kollisionen (Anhang A, Tabelle OQ-Namensräume) sowie Memory „OQ-01/02/03 blockieren /draft“ vs. Skill „erledigt 2026-05-03“ | | `ID_COLLISION` / `MEMORY_DRIFT`. Globale IDs vergeben. |
| B16 | Precedence selbst: Projekt-Anleitung „Konzept 05-08 autoritativ“ vs. Quartett „neuere Quelle gewinnt“ · `canon-meta` sagt „Skill-Files > alles“, ist aber älter | | Meta-Konflikt. Tier-Tabelle §3.2 dem Autor zur Bestätigung vorlegen. |
| B17 | Kap-40-Ende: „Kein Reset/Race-Condition-Ende“ (Hard-Constraint) vs. „Reset als zulässige Leser-Projektion“ (Kap-40-Lesart-Dualität 05-30) | | *Kein* echter Konflikt, sondern Präzisierung. Der Detektor soll ihn als `resolved_by_refinement` erkennen und nicht als offen melden. Das testet die Präzision. |
| B18 | Mnemosyne „spricht metaphorisch“ (Kap 10, Versuchung) vs. KW1-Metaphernverbot · Kap 34 „Mosaik-Herz“ als Ort vs. Titel „Zwei Arten der Kohärenz“ · Kap 16 „Diktatur der Komplexität“ vs. „… der physikalischen Zeit“ · Kernwelten-Doc Inhaltsverzeichnis §12 vs. Body §11 | | `minor`/`cosmetic`. Sammeln, nicht eskalieren. |
| B19 | *Ergänzt 2026-09-23.* Status des Kanons selbst: `Legacy/Canon/README.md` (Import 2026-06-12) nennt `storyform-und-outline_2026-06-10` „Normative … Wins on conflict“ vs. Entscheidung 001 (2026-09-16, Autor): „`Canon/` loses its normative status and is parked“ vs. dieser Auftrag (2026-09-23): das Quartett ist T1 | README, `Plan/decisions/001`, §3.2 | Meta-Konflikt wie B16. Die jüngste Autor-Entscheidung ist dieser Auftrag. Er revidiert 001 für den Kanon ausdrücklich über den Zweck, aber nicht über den Ort: siehe C1. |
| B20 | *Ergänzt 2026-09-23.* Kapitel-Kopf vs. Prosa in derselben Datei: Jede Kapiteldatei trägt `Locks` im Kopf und Prosa darunter. Weicht die Prosa vom eigenen Kopf ab, ist das ein `RULE_VS_CONTENT` innerhalb *einer* Datei. Kap 1 hält alle geprüften Locks ein und ist damit die **Negativ-Fixture**: Der Detektor darf hier nichts melden (vgl. §7.5). | Manuskript | Präzisionstest wie B17. |

---

## Anhang C · Wo dieser Auftrag und das Repository sich widersprechen (ergänzt 2026-09-23)

Das sind Autor-Entscheidungen, keine Befunde. Sie gehören in die erste Review-Queue von Phase 0. Jede steht mit Mechanik und Konsequenz da, wie §1.9 es verlangt.

**C1 · Die Romanquellen — für Drive entschieden, für Manuskript und NCP offen.** Der Autor hat am 2026-09-23 festgelegt: Die Quellen sind in `Sources/`. Für alle Drive-Dokumente, auch die Kanon-Stände, gilt damit Option A aus Entscheidung 001: „it comes back as sources rather than as a layer“. Offen bleibt der Weg für das, was nicht aus Drive kommt:
- *Manuskript und NCP.* Sie liegen nur unter `Legacy/Manuscript/`, das `CLAUDE.md` als Ablage definiert, die nichts liest. Option: Sie landen über `Sources/` mit eigener Kategorie (`manuscript`, `ncp`) und eigenem Landeweg aus dem Repository statt aus Drive. Pro: eine Pipeline, `quotes.py` greift. Contra: Das Manuskript wird „Quelle“, obwohl es als T3 eine Sonderrolle hat (Story-First).
- *claude.ai-Exporte* (Entscheidungs-Logs, Kap-40-Lesart). Sie landen über `Sources/`, sobald der Autor sie exportiert.

**C2 · Konflikterkennung.** §4.4 Schritt 2 lässt ein Modell adjudizieren, und `CLAUDE.md` verbietet mechanisierte Konflikterkennung. Vorschlag: der Schnitt aus dem Ist-Stand-Block in §4.4 (Programm für 1 und 3, Modell nur als Kandidaten-Datei). Zu bestätigen oder zu ersetzen.

**C3 · Verzeichnisaufbau.** Für `kg/`, `wiki/`, `tools/kpkg/` und `kp` gibt es zwei Wege:
- *Neu daneben:* sauber nach Spec, aber zwei Wikis und zwei Graphen, und dieselbe Tatsache steht an zwei Orten.
- *Das Bestehende wächst:* `Sources/` bekommt Kanon und Manuskript, `Wiki/` bekommt `kapitel/`, `locks/`, `oq/` neben `candidates/`, `scripts/` bekommt die `kp`-Befehle, und `graph.py` bekommt die Knotentypen aus §4.3. Die Tabelle in §4 zeigt, wie viel davon schon trägt.

**C4 · Status-Tags und Tiers.** `[K] [V] [S] [L]` benutzt der Kanon bereits im Text (Quartett-Kopf). Die Seiten dieses Wikis benutzen sie nicht, sie tragen Lesarten mit Quelle und Datum. P4 sagt: kein Feld ohne Instanzen. Die Instanzen gibt es, sobald C1 den Kanon hereinholt. Dann werden die Tags als Feld übernommen, und `[D]` und `[M]` kommen dazu. Offen ist nur, ob die bestehenden 56 Seiten nachträglich getaggt werden.

---

## Anhang D · Werkzeuge, die es schon gibt (ergänzt 2026-09-23)

```bash
python3 scripts/selftests.py                      # jede Prüfsuite, eine Zeile pro Suite
python3 scripts/state.py [--prose]                # jede Zahl gemessen; veraltete Prosa-Zahl → Fehler
python3 scripts/sources.py next|land|check        # Drive → Sources/drive/, Manifest, Prüfsummen
python3 scripts/read.py <slug> --find "<Wortlaut>"   # Zitat → ^[Lnn], oder Verweigerung mit nächster Zeile
python3 scripts/quotes.py                         # jedes Zitat gegen seine Zeile
python3 scripts/reconcile.py <slug>               # Census gegen Wiki-Index, per Nachschlagen
python3 scripts/judgements.py                     # aufgezeichnete Entscheidungen gegen den Code abspielen
python3 scripts/graph.py [--around X --mermaid | --graphml | --proposals]
python3 scripts/graphrag.py ask "…" [--gloss] | bench
python3 scripts/entities.py verify|missing|search|doc
python3 scripts/pairs.py score                    # „ein Begriff oder zwei“ gegen fold()
.venv-dspy/bin/python scripts/lmrun.py            # der einzige Weg zu einem Modell
```

**Referenz für Codex, Prompt-Engine und Plan:** `Plan/concept/novelcrafter-spec_2026-09-23.md` (vom Autor gespeichert, 2026-09-23). Die Datei ist eine Funktions-Spezifikation nach dem Vorbild von Novelcrafter, keine Beschreibung dieses Repositorys. Sie deckt sich direkt mit Teilen dieses Auftrags:
- Codex mit Aliasen, AI-Context-Stufen, szenengebundenen Progressions und gerichteten Relations ↔ §4.3 Ontologie und `kp context`
- Plan-Hierarchie und Matrix ↔ §5 und Kapitel-Dossiers
- Kontext-Builder mit Token-Budget ↔ `kp context <kap> --budget`
- Dramatica-Anbindung (Spec §8.5) ↔ §5.2

Ihr Hinweis zur deutschen Flexion beim Alias-Matching trifft genau die Lücke, die hier `fold()` und `pairs.py` messen: 21 <!--state:pairs.fold_correct--> von 36 <!--state:pairs.labelled--> Paaren.

`CLAUDE.md` beschreibt jedes Werkzeug. Den Katalog der guten, noch nicht gebauten Ideen führt `PRINCIPLES.md`. Die neun DSPy-Repositories, aus denen die Werkzeugkette portiert ist, sind in `Plan/concept/dspy-toolchain_2026-09-23.md` ausgewertet.

---

*Ende des Auftrags. Beginne mit Phase 0. Die erste sichtbare Ausgabe an den Autor ist ein Satz, was du jetzt tust, dann die Zugangs-Inventur. Ergänzt 2026-09-23: Die Inventur beginnt mit §2 „Ist-Stand“ und Anhang C, nicht bei null. Der erste Arbeitsschritt ist, die katalogisierten Kanon-Stände zu landen.*
