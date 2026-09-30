# Other documents on the pages `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik` reads onto

`python3 scripts/crossdoc.py doc kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`: whole-word counts of each page's surfaces over every landed document (`corpus.py`), never a search rank. A document that writes a name may say nothing about the thing: open the line before using it.

| page | read on it | read, not on it | unread that write it | the unread, most first (count, line) |
|---|---|---|---|---|
| `kael` | 48 | 2 | 431 | `ai-assisted-narrative-coherence` 436× L157; `romanplot-uberarbeitung-kohaerenz-protokoll-teil-1` 216× L27; `leserzentrierte-roman-outline-generierung-kohaeren` 204× L15; `romanarchitektur-kael-aegis-entropie-docx` 172× L11; `kohaerenz-protokoll-detailliertes-roman-outline-leserzentrie` 169× L19 |
| `aegis` | 50 | 1 | 440 | `ai-assisted-narrative-coherence` 411× L97; `aegis-singularitaet-jenseits-entropiegleichung-2` 342× L11; `romanarchitektur-kael-aegis-entropie-docx` 232× L11; `romanplot-kohaerenz-protokoll-entwicklung` 231× L17; `kohaerenz-protokoll-plotideen-extraktion` 229× L15 |
| `juna` | 45 | 2 | 374 | `juna-resilienz-zyklus-konzeptentwicklung` 102× L15; `juna-kael-system-analyse-und-rettungsplan-docx` 87× L15; `junas-liebe-kaels-trauma-aegis-docx` 67× L11; `plot-konzepte-kohaerenz-protokoll-generierung` 64× L23; `juna-kael-system-krisenanalyse-und-rettungsplan` 60× L15 |
| `entropie` | 31 | 1 | 243 | `emergenz-autonomer-systeme-aegis-forschung` 41× L33; `aegis-singularitaet-jenseits-entropiegleichung-2` 41× L25; `umfassendes-lokalitaeten-konzept-fuer-roman` 38× L34; `paradoxien-der-kohaerenz-protokoll-entwicklung` 32× L19; `lokalitaeten-konzept-fuer-roman-simulation` 31× L37 |
| `kohaerenz` | 18 | 4 | 469 | `roman-outline-leserlebnis-und-tiefe` 127× L11; `aegis-genesis-krise-prosa-auftrag-2` 71× L17; `plot-konzepte-kohaerenz-protokoll-generierung` 62× L11; `ai-assisted-narrative-coherence` 60× L94; `aegis-genesis-krise-konzeptioneller-rahmen` 59× L33 |
| `risse` | 39 | 2 | 351 | `orte-konzept-fuer-kohaerenz-protokoll` 81× L25; `romanplot-uberarbeitung-kohaerenz-protokoll-teil-1` 66× L21; `physik-fuer-simulierte-realitaet` 43× L23; `umfassendes-lokalitaeten-konzept-fuer-roman` 42× L44; `roman-blueprint-seelen-kohaerenz-protokoll` 30× L23 |
| `konstrukt-stadt` | 29 | 0 | 114 | `charakterkonzepte-fuer-kohaerenz-protokoll` 28× L26; `nichts-ordnung-fragmentierung-resonanz-nebel` 24× L15; `romanentwurf-kohaerenz-protokoll-teil-1` 18× L21; `kael-charakterarchitektur-und-konfliktdynamik-2` 18× L32; `romanentwurf-ruf-des-abenteuers` 17× L15 |
| `evaluierungseinheit` | 6 | 0 | 1 | `roman-synthese-mit-dual-kernel-theorie` 1× L145 |
| `kaels-wohneinheit` | 16 | 0 | 5 | `roman-lokalitaeten-konzept-und-ausarbeitung-2` 2× L341; `roman-lokalitaeten-konzept-und-ausarbeitung-3` 2× L342; `umfassendes-lokalitaeten-konzept-fuer-roman` 2× L172; `lokalitaeten-konzept-fuer-roman-simulation` 1× L263; `orte-konzept-fuer-kohaerenz-protokoll` 1× L205 |
| `grosse-mauer` | 2 | 0 | 16 | `kohaerenz-protokoll-konzeptionelle-ausarbeitung` 2× L228; `genesis-ein-implementierungsleitfaden-prosa-version` 2× L221; `genesis-mehrstufige-recherche-und-ausformulierung` 2× L211; `emergenz-autonomer-systeme-aegis-forschung` 1× L392; `genesis-finale-prosa-angepasste-ich-natur` 1× L65 |
| `system-monitor` | 1 | 0 | 0 | — |
| `vergessener-schrein` | 3 | 0 | 8 | `lokalitaeten-konzept-fuer-roman-simulation` 4× L274; `umfassendes-lokalitaeten-konzept-fuer-roman` 4× L33; `orte-konzept-fuer-kohaerenz-protokoll` 3× L207; `outline` 1× L187; `roman-lokalitaeten-konzept-und-ausarbeitung-2` 1× L355 |

**Related, not named (`P_BM25`)** — lines that share a page's words and write none of its names. Each may be a tension, a parallel, the same thing, or noise: judge it with `python3 scripts/bm25rel.py label <id> tension|parallel|same|noise --by "<you>"`.

- `kael` → `line:protokoll-der-offenbarung:426` — SUBJEKT MICHAEL: ÜBERLASTUNG DETEKTIERT. (`bm25:53096c04a2e9`)
- `kael` → `line:protokoll-der-offenbarung:589` — KERN-EINHEIT MICHAEL: SIGNALVERLUST DROHT. (`bm25:838b14036c87`)
- `kael` → `line:protokoll-der-offenbarung:645` — KERN-EINHEIT MICHAEL: SIGNALVERLUST IMMINENT. (`bm25:828577b4e1fb`)
- `aegis` → `line:charakterkonzepte-fuer-kohaerenz-protokoll:273` — \* Blinder Fleck: Könnte die Notwendigkeit von emotionaler Verarbeitung für Heilung unterschätzen. Ihre rigide Kontrolle kann notwendige Kom (`bm25:c987d3156263`)
- `aegis` → `line:paradoxien-der-kohaerenz-protokoll-entwicklung:345` — | 3 | Der Logik-Wächter | Agenten-Theorie, Ashby's Law \\\[Erweiterter Kontext: 2\\\] | Guardian (Logik), Kern-Welt 1 | Guardian agiert nach (`bm25:dc0e6d2b31c8`)
- `aegis` → `line:kohaerenz-protokoll-konzept:119` — | "Der Archivar" | Gatekeeper | Kontrolliert Zugang zu Erinnerungen/Alters, managt Switching, bewahrt Stabilität | Emotionslos, analytisch,  (`bm25:b6ebd704dc96`)
- `juna` → `line:protokoll-der-offenbarung:31` — ZIELPERSON: JULIA. (`bm25:7cc842f86dc3`)
- `juna` → `line:protokoll-der-offenbarung:428` — KONSEQUENZ: VERBINDUNGSABBRUCH ZU EXTERNEM SUBJEKT JULIA. (`bm25:0051f15cf415`)
- `juna` → `line:protokoll-der-offenbarung:1063` — ENTSCHEIDUNGSPHASE IV: ÜBERMITTLUNG AN SUBJEKT JULIA. (`bm25:20925301dc37`)
- `kohaerenz` → `line:kap0-v1-annotiert-md:533` — KOHÄRENZ:  0.998 (`bm25:aa74987116b1`)
- `kohaerenz` → `line:kap0-v1-annotiert-md:741` — KOHÄRENZ:                0.21 (`bm25:02a3be98f1b3`)
- `kohaerenz` → `line:kap0-v1-annotiert-md:873` — KOHÄRENZ:   0.21 (`bm25:a04050be9fb2`)
- `risse` → `line:roman-outline-transformation-in-keyword-tags:841` — - Beat: Spiegel\_Glitch \[identitaet\_hume, unreliable\_narrator, wahrnehmung\_unzuverlaessig, glitches\_wahrnehmung, spiegel, aegis\_kontro (`bm25:0035df977c17`)
- `evaluierungseinheit` → `line:kohaerenz-protokoll:220` — BITTE ZUR EVALUIERUNGSEINHEIT EPSILON-GAMMA-12 BEGEBEN. (`bm25:05c84b00f5c1`)
- `kaels-wohneinheit` → `line:umfassendes-lokalitaeten-konzept-fuer-roman:108` — - \*\*1. Kaels Initiale Wohneinheit \*\* (`bm25:0765ad6d0373`)
- `kaels-wohneinheit` → `line:roman-lokalitaeten-konzept-und-ausarbeitung-2:216` — **1. Kaels Initiale Wohneinheit (KW1)** (`bm25:78e804f2d7fe`)
- `kaels-wohneinheit` → `line:roman-lokalitaeten-konzept-und-ausarbeitung-3:217` — **1. Kaels Initiale Wohneinheit (KW1)** (`bm25:157ba52b3157`)
- `grosse-mauer` → `line:roman-lokalitaeten-konzept-und-ausarbeitung:371` — - **Design Inspirations:** Berliner Mauer, Chinesische Mauer, Festungsarchitektur, Gefängnismauern, Grenzanlagen, dystopische Architekturen  (`bm25:e1b18b3e2235`)
- `grosse-mauer` → `line:umfassendes-lokalitaeten-konzept-fuer-roman:408` — - \*\*21. Zerfallende Mauer / Riss-Zone \*\* (`bm25:0f45023d78ef`)
- `grosse-mauer` → `line:roman-blueprint-seelen-kohaerenz-protokoll:236` — - **1.03 - Schatten an der Mauer** (`bm25:d8b106463584`)
- `system-monitor` → `line:monstergruppe-primzahlen-plot-blueprint:437` — | 8 | Eskalation, M-Erfahrung | Massive M-Resonanzwelle, Große Anomalie | Überwältigende M-Immersion | Konfrontiert mit großer Anomalie | Fa (`bm25:8cf39404ae39`)
- `system-monitor` → `line:kohaerenz-protokoll-als-algorithmische-grundlage-fuer-narrat:770` — Kohärenz großer Sprachmodelle. (`bm25:2e2ab2841efd`)
- `system-monitor` → `line:romanplot-kohaerenz-protokoll-entwicklung:346` — **Schritt 19: Emergenz von Systemfehlern ("Risse" werden größer)** (`bm25:98717ef0532a`)
- `vergessener-schrein` → `line:juna-resilienz-zyklus-konzeptentwicklung:312` — Ein warmer Schauer, längst vergessener Schein. (`bm25:baf610bf3e43`)
- `vergessener-schrein` → `line:kohaerenz-protokoll-outline-revision-2026-05-01-md:116` — | Kiko | Ch 11 (Kindterror im Schrein) | Ch 13 | (`bm25:093f1272c47b`)
- `vergessener-schrein` → `line:roman-lokalitaeten-konzept-und-ausarbeitung-2:223` — **2. Der "Vergessene Schrein" / Ort des Kern-Traumas (KW2)** (`bm25:17a5d66bbe3e`)

**Read, but not on the page** — each is a sweep to re-check or an occurrence:

- `kael` ← `aegis-subplots-kapitelweise-system-exploration-docx` 154× L13
- `kael` ← `kohaerenzprotokoll-aegis-und-systementropie` 25× L15
- `kael` ← `ki-narrative-kollaps-kohaerenz-paradoxie` 8× L50
- `kael` ← `kohaerenz-protokoll-audit-und-verifizierung` 8× L53
- `kael` ← `technical-audit-research-mandate-the-kohaerenz-protokoll-fra` 7× L7
- `aegis` ← `aegis-subplots-kapitelweise-system-exploration-docx` 257× L11
- `aegis` ← `ki-narrative-kollaps-kohaerenz-paradoxie` 43× L21
- `aegis` ← `kohaerenz-protokoll-audit-und-verifizierung` 27× L27
- `aegis` ← `technical-audit-research-mandate-the-kohaerenz-protokoll-fra` 12× L7
- `aegis` ← `ontologische-inversion-von-aegis-kritisches-framework` 11× L13
- `juna` ← `kohaerenzprotokoll-aegis-und-systementropie` 14× L15
- `juna` ← `kohaerenz-protokoll-audit-und-verifizierung` 11× L111
- `juna` ← `aegis-subplots-kapitelweise-system-exploration-docx` 9× L126
- `juna` ← `technical-audit-research-mandate-the-kohaerenz-protokoll-fra` 6× L20
- `entropie` ← `aegis-subplots-kapitelweise-system-exploration-docx` 32× L60
- `entropie` ← `ki-narrative-kollaps-kohaerenz-paradoxie` 13× L59
- `entropie` ← `ontologische-inversion-von-aegis-kritisches-framework` 5× L19
- `entropie` ← `kohaerenz-protokoll-audit-und-verifizierung` 5× L23
- `kohaerenz` ← `roman-lokalitaeten-konzept-und-ausarbeitung` 22× L11
- `kohaerenz` ← `ki-narrative-kollaps-kohaerenz-paradoxie` 16× L15
- `kohaerenz` ← `ontologische-inversion-von-aegis-kritisches-framework` 7× L15
- `kohaerenz` ← `kohaerenz-protokoll-audit-und-verifizierung` 7× L37
- `kohaerenz` ← `aegis-subplots-kapitelweise-system-exploration-docx` 2× L177
- `risse` ← `aegis-subplots-kapitelweise-system-exploration-docx` 11× L93
- `risse` ← `m-als-fundament-der-simulation` 9× L56
- `risse` ← `kohaerenz-protokoll-audit-und-verifizierung` 3× L81
- `risse` ← `technical-audit-research-mandate-the-kohaerenz-protokoll-fra` 1× L26
