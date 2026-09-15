# Kohärenz Protokoll

Deutschsprachiges Romanprojekt im Genre **Hard SciFi / Cosmic Horror / Psychological Thriller**. Dieses Repository enthält Kapitel, verbindliche Welt- und Storyform-Dokumente sowie die Planung für die weitere Ausarbeitung.

## Lesen

- [Kapitel 1 — Erwachen in der Konstrukt-Stadt](Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/koh%C3%A4renz-protokoll/chapters/01-erwachen-in-der-konstrukt-stadt.md) bietet den Einstieg in Kaels Perspektive.
- [Alle Kapitel](Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/koh%C3%A4renz-protokoll/chapters/) sind nach Kapitelnummer geordnet. Die Dateien enthalten auch Planungsinformationen; der jeweilige Bearbeitungsstatus steht im Dateikopf.
- [Canon-Übersicht](Canon/README.md) erschließt die Hintergrunddokumente. **Canon und Planung enthalten Spoiler.**

## Orientierung im Repository

| Bereich | Inhalt |
| --- | --- |
| [Manuscript](Manuscript/) | Kapiteldateien, Prämisse und Storyform-Daten |
| [Canon](Canon/) | Verbindliche Referenzen zu Handlung, Welten, Begriffen, Philosophie, Sensorik und Stimmen |
| [Plan/drafting](Plan/drafting/) | Drafting-Brief, Szenenplan, Entscheidungen und Quellen |
| [Plan/encoding](Plan/encoding/) | Planung zur Storyform-Kodierung |
| [Plan/ingest](Plan/ingest/) | Extraktionen und Importprotokolle |
| [Plan/sessions](Plan/sessions/) | Festgehaltene Erkenntnisse aus Arbeitssitzungen |
| [Plan/quality](Plan/quality/) | Berichte der Qualitäts-Gates, u. a. [lit-critic](Plan/quality/lit-critic/) |
| [scripts](scripts/) | Werkzeuge für Canon-Import, Manuskript-Materialisierung und Qualitäts-Gates |
| [tools/lit-critic](tools/lit-critic/) | CANON.md und STYLE.md — die Regeln, gegen die lit-critic prüft |
| [tests](tests/) | Tests der Repo-Werkzeuge (`pytest tests/`) |
| [CLAUDE.md](CLAUDE.md) | Arbeitsvereinbarung und technische Referenz für den Agency-Workflow |

## Am Manuskript arbeiten

Vor Änderungen an Kapitelprosa den [Drafting-Brief](Plan/drafting/drafting-brief.md) vollständig lesen. Er verweist auf die erforderlichen Stimm-Referenzen und legt Perspektive, harte Regeln, Dateiformat und Selbstprüfung fest.

- Der [Akt-I-Szenenplan](Plan/drafting/akt1-plan_2026-09-11.md) und das [Entscheidungslog](Plan/drafting/decision-log_2026-09-11.md) dokumentieren die konkrete Ausarbeitung.
- Bei Widersprüchen ist [Storyform und Outline](Canon/kohaerenz-protokoll_storyform-und-outline_2026-06-10.md) normativ.
- Kanonische Prosa bleibt deutsch. Offene Kanon-, Figuren- und Handlungsentscheidungen vor Änderungen klären.
- Die Agency-Arbeitsweise und Voraussetzungen der Skripte sind in [CLAUDE.md](CLAUDE.md) beschrieben.

### Qualitäts-Gates

Bevor ein Kapitel den Status wechselt (`drafted` → `revised` → `final`), laufen der Reihe nach:

1. `python3 scripts/check_enrichment.py` — eine Anreicherung darf Prosa nur einfügen, nie umschreiben.
2. Readiness Gate, [Enrichment-Masterplan](Plan/drafting/chapter-enrichment-masterplan_2026-09-11.md) §F.
3. `python3 scripts/lit_critic_gate.py --chapter N` — [lit-critic](https://github.com/lit-pack/lit-critic)
   liest die Prosa durch sieben redaktionelle Linsen gegen [tools/lit-critic/CANON.md](tools/lit-critic/CANON.md)
   und [STYLE.md](tools/lit-critic/STYLE.md). Einmalig einrichten mit `scripts/setup_lit_critic.sh`;
   benötigt `ANTHROPIC_API_KEY`. Nur `critical`-Findings blockieren.
   Berichte: [Plan/quality/lit-critic/](Plan/quality/lit-critic/).
4. Die Agency-Gate-Leiter (`line_gate`, `copy_gate`, …).

Findings sind Vorschläge, keine Urteile — die Triage-Regeln stehen in der
[lit-critic-Skill](.claude/skills/lit-critic/SKILL.md).

## Lizenz

Siehe [LICENSE](LICENSE) — CC0 1.0 Universal.
