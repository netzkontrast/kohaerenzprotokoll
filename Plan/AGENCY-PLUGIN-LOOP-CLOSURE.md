# Agency-Plugin — Loop-Closure auf den Fehlerbericht

> Antwortdokument auf [`AGENCY-PLUGIN-FEHLERBERICHT.md`](./AGENCY-PLUGIN-FEHLERBERICHT.md).
> Zwei vollständige Brainstorm → Design → Spec-Panel → Reflect → TDD-Schleifen
> haben die im Fehlerbericht dokumentierten Hürden adressiert. PR liegt unter
> [netzkontrast/agency#14](https://github.com/netzkontrast/agency/pull/14).

## Tabellarische Statusübersicht

| # | Titel | Schweregrad (Fehlerbericht) | Status nach Loop 1/2 | Beleg |
|---|---|---|---|---|
| F1 | Kein MCP-Verb zum Anlegen eines Intent | **Hoch (Blocker)** | **GESCHLOSSEN** — `intent_bootstrap` Substrat-Tool | Spec 029 §A; Test `test_mcp_bootstrap.py` (4 Tests incl. MCP≡CLI-Isomorphie) |
| F2 | `JULES_API_KEY` wird nicht gelesen | **Hoch** | **GESCHLOSSEN** (Doku/Diagnose) — neue Fehlermeldung benennt `user_config.jules_api_key` + Plugin-Reload; `agency_doctor` bestätigt Inheritance | Spec 030 §A+B; Tests `test_jules_key_error.py`, `test_agency_doctor.py` |
| F3 | Code-Mode-Sandbox-Timeout → Duplikate | **Mittel** | **VERTAGT** auf Spec 031 — braucht Idempotenz-Key + Streaming-Return-Arbeit (eigenständige Spec) | Non-goal in Spec 029 + 030; tracking-issue |
| F4 | `reflect.batch_note` `scope` als geschlossenes Enum undokumentiert | **Niedrig** | **GESCHLOSSEN** — Enum-Domäne in `note`/`batch_note`-Docstrings + damit auch im Brief-Slice + `get_schema` | Spec 029 §C; Test `test_reflect_scope_enum_in_doc.py` |
| F5 | System-`python3` ohne Deps → stiller Fehlschlag | **Mittel** | **GESCHLOSSEN** (Doku + Diagnose) — AGENTS.md-Eintrag + `agency_doctor` meldet fehlende Deps mit copy-pasteable Fix | Spec 030 §D; AGENTS.md-Abschnitt "Dev"; `test_agency_doctor.py::test_doctor_marks_ok_when_all_present` |
| F6 | `intent_id`-Pflicht ohne Discovery-Pfad | **Mittel (DX)** | **GESCHLOSSEN** — SERVES-Guard-Fehlermeldung nennt `intent_bootstrap` + `agency_welcome`; stateful Welcome ist die kanonische Erst-Call-Oberfläche | Spec 029 §B + Spec 030 §C; Tests `test_serves_guard_message.py`, `test_welcome_state.py` |

**Zusätzlich umgesetzt** (über den Fehlerbericht hinaus, auf Nutzerwunsch):
- `agency_install(target=None)` — der angeforderte Install-Verb, der `.agency/` + einen marker-begrenzten Onboarding-Snippet in der CLAUDE.md des Ziel-Repos schreibt. Idempotent. Re-runs ersetzen nur zwischen den Markern — Nutzer-Inhalt außerhalb wird nie angerührt.
- `agency_welcome` als state-aware Erstkontakt-Tool (`state: "fresh" | "in_progress"`) — subsumiert den im Fehlerbericht noch implizit gewünschten Empty-Graph-Hint.

## Was sich konkret geändert hat (für einen späteren Dogfood-Lauf)

Statt:

```
ValueError: intent_id 'x' is not an Intent node
```

steht jetzt:

```
ValueError: intent_id 'x' is not an Intent node. Mint one with the
`intent_bootstrap` MCP substrate tool (purpose, deliverable,
acceptance) or `python -m agency.cli intent ...` (bash side-pipe).
Call `agency_welcome` for the full onboarding payload.
```

Statt eines Bash-CLI-Hops zum Bootstrap:

```python
# Pure MCP, kein Bash mehr
await call_tool('agency_welcome', {})                # erkennt fresh vs. in_progress
await call_tool('agency_install', {})                # scaffolded .agency/ + CLAUDE.md
r = await call_tool('intent_bootstrap', {
    'purpose': '...', 'deliverable': '...', 'acceptance': '...'})
await call_tool('capability_plugin_help', {'intent_id': r['intent_id']})
```

Statt eines Silent-Fail bei System-`python3` ohne Deps:

```
agency_doctor → {
  "deps": {"fastmcp": "3.3.1", "graphqlite": "missing"},
  "next_steps": [
    "graphqlite missing — install the plugin venv: pip install -e .[dev] from the agency repo (F5: system python3 silent-fail)",
    ...
  ]
}
```

## Was über den Fehlerbericht hinaus aufgefallen ist

Die Reflektion über zwei Schleifen hinweg hat drei strukturelle Hinweise sichtbar gemacht, die im Fehlerbericht selbst nicht thematisiert waren:

1. **Substrat-Tool-Konvention fehlt.** Mit `intent_bootstrap`, `agency_install`, `agency_welcome`, `agency_doctor` neben den bestehenden `lifecycle_gate` / `memory_graph_provenance` sind sechs flach benannte Tools entstanden. Drei davon haben den `agency_`-Präfix, drei nicht. Per Spec-Panel-Diskussion (Fowler) ist das die Naming-Schwelle. Empfehlung: CORE.md um einen Abschnitt "Substrate tools" erweitern, der den Namespace dokumentiert (offene Aufgabe, non-blocking).

2. **Provenance-Asymmetrie zwischen MCP-Bootstrap und Capability-Calls.** `intent_bootstrap` legt einen `Intent`-Knoten an, aber bewusst **keinen** `Invocation` — er umgeht `Registry.invoke` (sonst entstünde ein Self-Loop-`SERVES` auf den gerade frisch geminteten Intent). Test `test_bootstrap_records_no_invocation` macht diese Asymmetrie explizit. Audit-Spur "wer hat bootstrap gerufen?" lebt jetzt in MCP-Server-Logs, nicht im Graphen — bewusste Entscheidung, dokumentiert in Spec 029 §A.

3. **Token-Effizienz als harte Test-Invariante.** Der erste Wurf des `agency_welcome`-Payloads (`{capability: [verb,...]}`) landete bei 1.2 KB allein dadurch, dass die `jules`-Capability 21 Verben hat. Lösung: nur Namen, Verben on-demand via `capability_plugin_help` oder `search`. Netto-Ersparnis ~800 B pro Erstkontakt. `test_welcome_token_budget_under_1kb` hält die Invariante als Regressionsgate.

## Was im Fehlerbericht gut funktionierte (Meta-Reflexion)

- **Reproduzierbarkeit pro Befund:** jeder Eintrag (F1–F6) hatte Symptom + Ursache + Auswirkung + Vorschlag. Das Spec-Schreiben war dadurch eine 1:1-Übersetzung statt einer Detektivarbeit.
- **Schweregrad-Differenzierung:** "Hoch (Blocker)" auf F1 ist tatsächlich der schmerzhafteste Punkt gewesen; ihn zuerst zu adressieren hat Loop 1 ein klares Done-Kriterium gegeben.
- **Trennung von Plugin-Reibung und Eigenfehler** (im Schwesterdokument `SESSION-REFLECTION.md`) hat verhindert, dass der Bericht in Schuldzuweisung kippt; das wiederum hat die Implementierung sachlich gehalten.

## Was noch offen bleibt

- **Spec 031 — F3 (Idempotenz für `effect`-Verben).** Der gefährlichste Korrektheitspunkt im Fehlerbericht — er hat real zu Duplikat-PRs geführt. Erfordert eine eigene Spec mit Idempotenz-Key-Konvention + streaming Rückgabe der Session-IDs aus laufenden Batch-Dispatches. Bewusst nicht in dieser PR mitgenommen, weil die Lösung architektonisch eigene Designentscheidungen braucht.
- **CORE.md-Update** zur Substrat-Tool-Namenskonvention (siehe oben Punkt 1).

---

*Eingebracht im Loop-Modus des Nutzerauftrags: "brainstorm → Design → spec Panel → reflect → implementation, dann Loop again, bis self-explanatory & easy to use & token-saving". Beleg: PR #14 (Spec 029 + 030, 24+ Commits, 333 Tests grün, 12 Reflection-Knoten im Provenance-Graphen).*
