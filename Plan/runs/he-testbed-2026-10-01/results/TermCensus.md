# TermCensus — the testbed's results

> TermCensus — the terms of one document, as the document writes them.
> provisional — first design, 2026-09-24; never run on the corpus
> derived from: the reader's lists (Plan/runs/<slug>/03-candidates.md) and the entity-lists
> reader prompt (.claude/workflows/entity-lists.js), whose entity kinds it keeps
> may not: seed or replace a reader's 03-candidates.md, create a page, supply a count,
> or merge two surfaces. No field carries a line: names in, lines by code (P26).
> retire when: on documents 5 and 6 it scores below the Haiku entity lists against the
> same gold (entities.py score: F1 0.25 and 0.69)

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/termcensus-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0586, 25.1 s. **18 rows**: 0 candidates, 0 refused, 0 duplicates, 18 not staged.

Staging refused the run: `candidate lacks nonempty string fields: term, quote, stance`

| # | kind | status | term | type | scope | quote | lines |
|---|---|---|---|---|---|---|---|
| 1 | item | not staged | Kael | person | world |  |  |
| 2 | item | not staged | AEGIS | system | world |  |  |
| 3 | item | not staged | Große Stille | concept | world |  |  |
| 4 | item | not staged | Glitch-Momente | concept | world |  |  |
| 5 | item | not staged | Primären Beobachtungs-Einheit | concept | world |  |  |
| 6 | item | not staged | Externen Taktgeber | concept | world |  |  |
| 7 | item | not staged | Einheit | concept | world |  |  |
| 8 | item | not staged | Kohärenz Protokoll | system | world |  |  |
| 9 | item | not staged | Juna | person | world |  |  |
| 10 | item | not staged | AEGIS-Protokolle | system | world |  |  |
| 11 | item | not staged | Beobachtungsstatus | concept | world |  |  |
| 12 | item | not staged | Gedanke eines Fremden | concept | world |  |  |
| 13 | item | not staged | Grenzen der Mathematik | work | lens |  |  |
| 14 | item | not staged | Wärmetod des Universums | concept | lens |  |  |
| 15 | item | not staged | Entropie | concept | lens |  |  |
| 16 | item | not staged | Dissoziation | concept | lens |  |  |
| 17 | item | not staged | Foreshadowing | concept | lens |  |  |
| 18 | item | not staged | Beobachter-Fokus | concept | world |  |  |

## `2026-09-14-kap25-vertiefung-md`

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.2226, 108.9 s. **122 rows**: 0 candidates, 0 refused, 0 duplicates, 122 not staged.

Staging refused the run: `candidate lacks nonempty string fields: term, quote, stance`

| # | kind | status | term | type | scope | quote | lines |
|---|---|---|---|---|---|---|---|
| 1 | item | not staged | Plan/sessions/2026-09-14-kap25-enrichment-packet.md | work | world |  |  |
| 2 | item | not staged | git branch -r | technology | lens |  |  |
| 3 | item | not staged | claude/kap-*-Branch | other | world |  |  |
| 4 | item | not staged | Akt-II-Arc | concept | world |  |  |
| 5 | item | not staged | Masterplan | work | world |  |  |
| 6 | item | not staged | Schleier | concept | world |  |  |
| 7 | item | not staged | Schleier-Disziplin | concept | world |  |  |
| 8 | item | not staged | Canon | concept | world |  |  |
| 9 | item | not staged | Arc-Auflage | concept | world |  |  |
| 10 | item | not staged | Optionlock | system | world |  |  |
| 11 | item | not staged | Station 7 | place | world |  |  |
| 12 | item | not staged | Priorität-1-Wasserführung | concept | world |  |  |
| 13 | item | not staged | Restwertschwelle | concept | world |  |  |
| 14 | item | not staged | Kael | person | world |  |  |
| 15 | item | not staged | AEGIS | system | world |  |  |
| 16 | item | not staged | EINHEIT 734: BEARBEITUNGSPROFIL ABWEICHEND. KEINE MASSNAHME. | other | world |  |  |
| 17 | item | not staged | KW3 | concept | world |  |  |
| 18 | item | not staged | Platte 204 | place | world |  |  |
| 19 | item | not staged | Delta-Sieben | place | world |  |  |
| 20 | item | not staged | Canon-Weltanker | concept | world |  |  |
| 21 | item | not staged | Anker 734 | concept | world |  |  |
| 22 | item | not staged | Stehen an der Schwelle | concept | world |  |  |
| 23 | item | not staged | der Tritt darüber | concept | world |  |  |
| 24 | item | not staged | Hook-in | concept | world |  |  |
| 25 | item | not staged | Hook-out | concept | world |  |  |
| 26 | item | not staged | Regel 6 | concept | world |  |  |
| 27 | item | not staged | Station 11/12/7 | place | world |  |  |
| 28 | item | not staged | Frontmatter | other | world |  |  |
| 29 | item | not staged | Template-Kopf | other | world |  |  |
| 30 | item | not staged | Canon/…storyform-und-outline | work | world |  |  |
| 31 | item | not staged | …kernwelten-vollstaendig | work | world |  |  |
| 32 | item | not staged | …welt-sensorik-drafting | work | world |  |  |
| 33 | item | not staged | …anteile-profile-sprach-dna | work | world |  |  |
| 34 | item | not staged | Plan/drafting/drafting-brief.md | work | world |  |  |
| 35 | item | not staged | akt2-arc-optimized | work | world |  |  |
| 36 | item | not staged | chapter-enrichment-masterplan | work | world |  |  |
| 37 | item | not staged | decision-log_akt2-3 | work | world |  |  |
| 38 | item | not staged | D23-02/03/04 | other | world |  |  |
| 39 | item | not staged | written-chapters-audit | work | world |  |  |
| 40 | item | not staged | sources/KP_Plot-Konkretisierung_13-Ideen_F1-Faden | work | world |  |  |
| 41 | item | not staged | Die Niederlegung | concept | world |  |  |
| 42 | item | not staged | KW3-Sensorik | concept | world |  |  |
| 43 | item | not staged | Sensorik-Lookup | concept | world |  |  |
| 44 | item | not staged | Self-Review | concept | world |  |  |
| 45 | item | not staged | R-Regeln | concept | world |  |  |
| 46 | item | not staged | Hitze-Polarität | concept | world |  |  |
| 47 | item | not staged | Warteschlange | concept | world |  |  |
| 48 | item | not staged | Datensatz ohne Datentyp | concept | world |  |  |
| 49 | item | not staged | Stufen-Modell | concept | world |  |  |
| 50 | item | not staged | Wechselmechanik | concept | world |  |  |
| 51 | item | not staged | Pflicht-Checks | concept | world |  |  |
| 52 | item | not staged | Alex | person | world |  |  |
| 53 | item | not staged | Lex | person | world |  |  |
| 54 | item | not staged | kohärenz protokoll | work | world |  |  |
| 55 | item | not staged | Google Drive | system | lens |  |  |
| 56 | item | not staged | Kohärenz Protokoll | work | world |  |  |
| 57 | item | not staged | The Agency System | work | lens |  |  |
| 58 | item | not staged | Wegkreuzung | concept | world |  |  |
| 59 | item | not staged | interner Wahlpunkt | concept | world |  |  |
| 60 | item | not staged | Schritt ins Ungewisse | concept | world |  |  |
| 61 | item | not staged | KW-Kanon | concept | world |  |  |
| 62 | item | not staged | Schleusen des Misstrauens | place | world |  |  |
| 63 | item | not staged | Gänge der Paranoia | place | world |  |  |
| 64 | item | not staged | Panoptikum | place | world |  |  |
| 65 | item | not staged | Guardians | concept | world |  |  |
| 66 | item | not staged | Cerberus | person | world |  |  |
| 67 | item | not staged | Nox | person | world |  |  |
| 68 | item | not staged | Echo | person | world |  |  |
| 69 | item | not staged | Limina | person | world |  |  |
| 70 | item | not staged | TSDP | concept | lens |  |  |
| 71 | item | not staged | Schutz-Anteil | concept | lens |  |  |
| 72 | item | not staged | Aktionssystem | concept | lens |  |  |
| 73 | item | not staged | ANP | concept | lens |  |  |
| 74 | item | not staged | ANP-Alltagssystem | concept | lens |  |  |
| 75 | item | not staged | Kai | person | world |  |  |
| 76 | item | not staged | inneres Tauziehen | concept | world |  |  |
| 77 | item | not staged | Co₁ | concept | world |  |  |
| 78 | item | not staged | McL | concept | world |  |  |
| 79 | item | not staged | B | concept | world |  |  |
| 80 | item | not staged | Ly | concept | world |  |  |
| 81 | item | not staged | Abwehr-Welt-Ästhetik | concept | world |  |  |
| 82 | item | not staged | Umgebung als Antagonist | concept | world |  |  |
| 83 | item | not staged | [S]-Quellen | concept | world |  |  |
| 84 | item | not staged | [K]-Repo-Canon | concept | world |  |  |
| 85 | item | not staged | Ein-Falschheits-Regel | concept | world |  |  |
| 86 | item | not staged | Telefon-Stille-Anker | concept | world |  |  |
| 87 | item | not staged | Genesis-Echo | concept | world |  |  |
| 88 | item | not staged | Juna | person | world |  |  |
| 89 | item | not staged | ncp-author | system | world |  |  |
| 90 | item | not staged | ncp.json | other | world |  |  |
| 91 | item | not staged | ncp-b.json | other | world |  |  |
| 92 | item | not staged | Storyform-Slots | concept | lens |  |  |
| 93 | item | not staged | Resolve | concept | lens |  |  |
| 94 | item | not staged | Growth | concept | lens |  |  |
| 95 | item | not staged | Approach | concept | lens |  |  |
| 96 | item | not staged | Driver | concept | lens |  |  |
| 97 | item | not staged | Limit | concept | lens |  |  |
| 98 | item | not staged | Outcome | concept | lens |  |  |
| 99 | item | not staged | Judgment | concept | lens |  |  |
| 100 | item | not staged | agency-CLI | technology | world |  |  |
| 101 | item | not staged | agency-Capability-Verben | technology | world |  |  |
| 102 | item | not staged | .agency/session.db | technology | world |  |  |
| 103 | item | not staged | MCP-Server | technology | world |  |  |
| 104 | item | not staged | Benennungslock | concept | world |  |  |
| 105 | item | not staged | Akt I | concept | world |  |  |
| 106 | item | not staged | Akt II | concept | world |  |  |
| 107 | item | not staged | Akt III | concept | world |  |  |
| 108 | item | not staged | [AEGIS v{X.X} // LOG_{0xHEX}] | other | world |  |  |
| 109 | item | not staged | Sprach-DNA | concept | world |  |  |
| 110 | item | not staged | Klick | concept | world |  |  |
| 111 | item | not staged | Vortex 1 | concept | world |  |  |
| 112 | item | not staged | Delta-Sieben-Figur | other | world |  |  |
| 113 | item | not staged | Einheit | person | world |  |  |
| 114 | item | not staged | KW2 | concept | world |  |  |
| 115 | item | not staged | Verwaltungstopologie | concept | world |  |  |
| 116 | item | not staged | Konstrukt-Stadt | place | world |  |  |
| 117 | item | not staged | Datenknoten | place | world |  |  |
| 118 | item | not staged | Wohneinheit 734 | place | world |  |  |
| 119 | item | not staged | Treppenkopf | place | world |  |  |
| 120 | item | not staged | Wartungsebene | place | world |  |  |
| 121 | item | not staged | KW-Progression | concept | world |  |  |
| 122 | item | not staged | Filterregime | concept | world |  |  |
