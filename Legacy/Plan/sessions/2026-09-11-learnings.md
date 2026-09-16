# Session-Learnings 2026-09-11 — Phase-1 MC-Encoding

> Kontext: Session in Claude Code (Windows, Desktop-App) über den `novel-architect`-Skill. Ergebnis: `Plan/encoding/phase1-mc-a-b_2026-09-11.md` (PR #8).
> Format wie `novel-architect/references/learnings.md`: Trigger · Lesson · Action.

---

## 1. KRITISCH: Das Repo ist der Canon-Stand, nicht der Skill-Snapshot

**Trigger:** Der Bootstrap las den Canon aus dem installierten Skill (Stand 2026-05-03). Das Encoding wurde dagegen entworfen. Erst beim PR-Erstellen zeigte `origin/main` den normativen Canon vom 2026-06-10: signierte Storyform, Approach-Spiegelung (A Be-er / B Do-er), AEGIS als 3.-Person-Log, Hitze-Polaritätsregel, Slot-16-Lock, 41 Bewegungen (Kap 0–40). Der Erst-Entwurf widersprach dem in sechs Punkten und musste abgeglichen werden (siehe §4 der Encoding-Datei).

**Lesson:** Das ist derselbe Fehler wie der Bootstrap-Skim vom 2026-05-03, eine Ebene höher: Man arbeitet gegen einen älteren Snapshot, obwohl der aktuelle Stand erreichbar ist. Ein lokaler Klon ohne gemeinsame Historie mit `origin` ist ein Warnsignal, keine leere Leinwand.

**Action:**
- `novel-architect` SKILL.md, Bootstrap **Schritt 0** (vor allem anderen): `git fetch`, `origin/main` lesen, Datum des jüngsten Canon-Commits (`Canon/`, `Manuscript/…/dramatica.md`) mit dem Skill-`progress.md` vergleichen. Der neuere Stand gewinnt, der Skill-Canon ist dann nur Snapshot.
- Normative Quelle im Repo: `Canon/kohaerenz-protokoll_storyform-und-outline_2026-06-10.md` (laut `Canon/README.md` „wins on conflict").

## 2. Bootstrap setzt die claude.ai-Sandbox voraus

**Trigger:** Das Bootstrap-Skript nutzt `/home/claude/...` und `/mnt/skills/...`. Beides existiert in Claude Code auf Windows nicht.

**Lesson:** Der Workspace muss umgebungsabhängig sein. Lokal ist das Git-Repo selbst der Workspace (Versionsgeschichte statt Skill-Packaging).

**Action:** Umgebungs-Weiche im Bootstrap: Fehlt `/home/claude`, dann Workspace = dieses Repo, Outputs nach `Plan/…`, Packaging durch Commit/PR ersetzen. Keine Canon-Kopie anlegen — sie wird sofort zur zweiten, veraltenden Quelle.

## 3. Windows kann das Repo nicht vollständig auschecken

**Trigger:** `git worktree add` und `git read-tree` scheitern an Dateinamen mit `:` (Kap 21 `…genesis-flashback:-trennungsprotokoll.md`, Kap 22 `…genesis-flashback:-komp-734.md`, Kap 34 `…konfrontation:-zwei-arten…`). Ein Plumbing-Commit mit leerem Index hätte beinahe das ganze Repo gelöscht. Er wurde vor dem Push bemerkt.

**Lesson:** Unter Windows ist ein Commit ohne Checkout nur mit `git -c core.protectNTFS=false` für die reinen Index-Operationen möglich. Danach **immer** `git diff --stat origin/main <branch>` prüfen, bevor gepusht wird.

**Action:** Die drei Kapitel-Dateien umbenennen (`:` → `-`) und `scripts/materialize_manuscript.py` so anpassen, dass es keine `:` in Dateinamen erzeugt. Offen, nicht Teil dieses PRs.

## 4. Vocabulary-Referenz reicht nicht für Element-Legalität

**Trigger:** Die `element-quads.md` des `dramatica-vocabulary`-Skills ist als Extension markiert und verortet die Problem-Quads unter Psychology-Types. Ob Pursuit/Avoid unter Mind/Memory und Logic/Feeling unter Universe/Progress legal sitzen, lässt sich damit nicht bestätigen.

**Action:** Im throughline-encoding-Workflow setzt jede Element-Ebenen-Aussage (Symptom/Response, Crucial Element, Benchmark, Signposts) Pflicht-Marker `[Prüfen]` → Validierung in P1–P5 gegen die Dramatica-Engine.

## Positiv, beibehalten

- Der Abgleich vor dem PR (statt den veralteten Entwurf zu pushen) hat die verwertbaren Teile gerettet: OQ-D-Vorschlag, Crucial-Element-Vorschlag und die Keime, die sich an die Canon-Locks anpassen ließen.
- Die Widerspruchs-Tabelle (§4 der Encoding-Datei) macht die Korrekturen für Reviewer nachvollziehbar und verhindert Re-Litigation.
