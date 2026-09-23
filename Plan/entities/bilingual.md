# German and English names — proposals, not merges

Written by `scripts/bilingual.py`. Every row is a pair of surfaces the corpus
contains, and every count below comes from the corpus search (whole-word,
case-sensitive). No count comes from a model.

- **stated**: the corpus writes the pair itself (`A (B)`, `A/B`). The cite is where.
- **proposed**: a free model (dots-studio/dots-3-note-preview:free, nvidia/nemotron-3-super-120b-a12b:free, poolside/laguna-s-2.1:free, qwen/qwen3.8-27b:free) suggested the
  counterpart from the **name alone**, with no corpus text, and code found it in the corpus.
- **p**: jev-1.13.0's probability for the relation, judged over the
  lines where the two occur. A probability directs attention; it decides nothing.

**Whether two surfaces are one term stays a person's call**
(`Plan/runs/judgements.jsonl`). Nothing here creates a page, a link or a merge.
The complete list, every judged entity with its counterparts or none, is
`bilingual.jsonl` beside this file: 6988 entities,
4111 with a counterpart.

```yaml
Plan/entities/bilingual: provisional
# may not: merge surfaces, create a page or link, supply a count, enter a census
# retire when: a person has reviewed the translation pairs into judgements.jsonl
```

## Translations — 2474 at p ≥ 0.8

The same entity named in two languages, most-used first.

| German | English | p | docs (de) | docs (en) | docs (both) | evidence |
|---|---|--:|--:|--:|--:|---|
| Kohärenz | Coherence | 0.93 | 295 | 119 | 95 | proposed |
| Theorie | Theory | 0.90 | 167 | 214 | 124 | proposed |
| Kohärenz | coherence | 0.94 | 295 | 85 | 66 | proposed |
| Protokoll | Protocol | 0.96 | 266 | 113 | 91 | proposed |
| Selbst | Self | 1.00 | 192 | 161 | 90 | stated in 4 doc(s) ^[optimierter-prompt-fuer-kohaerenz-protokoll.md:L211] ^[kernwelten-fuer-kohaerenz-protokoll.md:L180]; proposed |
| Welt | world | 0.88 | 228 | 112 | 49 | proposed |
| Welt | World | 0.92 | 228 | 102 | 69 | proposed |
| Bewusstsein | consciousness | 0.95 | 200 | 110 | 49 | proposed |
| Ordnung | Order | 0.96 | 221 | 84 | 46 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse-2.md:L135] ^[dramatica-storyform-synthese-aegis-analyse-2.md:L205] |
| Kohärenz | COHERENCE | 0.95 | 295 | 6 | 5 | proposed |
| Logik | LogOS | 0.85 | 233 | 67 | 50 | stated in 1 doc(s) ^[aegis-subplots-kapitelweise-system-exploration-docx.md:L152] |
| Ordnung | LogOS | 0.85 | 221 | 67 | 50 | stated in 1 doc(s) ^[kohaerenz-protokoll-projekt-rekonstruktion.md:L166] |
| Modell | model | 0.86 | 184 | 101 | 41 | proposed |
| Bewusstsein | Consciousness | 0.86 | 200 | 84 | 60 | proposed |
| Paradoxon | paradox | 0.95 | 148 | 135 | 62 | proposed |
| Dissoziation | Dissociation | 0.88 | 157 | 124 | 69 | proposed |
| Komplexität | Complexity | 0.86 | 218 | 62 | 49 | proposed |
| Modell | Model | 0.93 | 184 | 92 | 67 | proposed |
| Geschichte | Story | 0.95 | 163 | 105 | 74 | proposed |
| Paradoxon | Paradox | 0.92 | 148 | 119 | 72 | proposed |
| Kohärenz Protokoll | Coherence Protocol | 1.00 | 212 | 54 | 37 | stated in 1 doc(s) ^[deconstructing-reality-s-architecture.md:L15] |
| Prinzip | principle | 0.94 | 173 | 89 | 36 | proposed |
| Erinnerung | Mind | 0.92 | 130 | 131 | 51 | stated in 1 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L310] |
| Ziel | Goal | 1.00 | 227 | 34 | 12 | stated in 1 doc(s) ^[narrative-context-protocol-ncp-spezifikation.md:L60]; proposed |
| Gefühl | Qualia | 0.83 | 166 | 93 | 49 | stated in 1 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L1049] |
| Wahrheit | Truth | 0.98 | 168 | 90 | 40 | stated in 4 doc(s) ^[kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md.md:L72] ^[dramatica-storyform-synthese-aegis-analyse.md:L71]; proposed |
| Teile | Parts | 0.93 | 157 | 100 | 37 | proposed |
| Wahrheit | truth | 0.95 | 168 | 89 | 23 | proposed |
| Fragmentierung | fragmentation | 0.92 | 183 | 73 | 17 | proposed |
| Realität | REALITY | 0.81 | 247 | 6 | 5 | proposed |
| Prinzip | Principle | 0.94 | 173 | 78 | 28 | proposed |
| Prozess | Process | 0.93 | 212 | 35 | 25 | proposed |
| Resonanz | Resonance | 0.94 | 194 | 50 | 26 | proposed |
| Entropie | entropy | 0.97 | 152 | 89 | 30 | proposed |
| Fundament | Foundation | 1.00 | 166 | 65 | 34 | stated in 2 doc(s) ^[a-learner-s-glossary-for-the-world-of-kohaerenz-protokoll.md:L37] ^[thematic-architecture-of-kohaerenz-protokoll-a-conceptual-le.md:L24]; proposed |
| Fragmentierung | Fragmentation | 0.97 | 183 | 45 | 26 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L365]; proposed |
| Rauschen | Noise | 0.99 | 186 | 42 | 33 | stated in 1 doc(s) ^[textanalyse-existenz-system-und-leid.md:L46]; proposed |
| Komplexität | COMPLEXITY | 0.87 | 218 | 5 | 4 | proposed |
| Entropie | Entropy | 0.99 | 152 | 68 | 43 | proposed |
| Kollaps | collapse | 0.92 | 149 | 71 | 13 | proposed |
| Maschine | ANP | 0.87 | 73 | 145 | 19 | stated in 1 doc(s) ^[ki-antagonist-fragmentierte-gottheit-analyse.md:L70] |
| Kollaps | Collapse | 0.92 | 149 | 69 | 31 | proposed |
| Bewusstsein | Awareness | 0.87 | 200 | 16 | 14 | proposed |
| Kampf | Fight | 0.96 | 169 | 46 | 18 | stated in 3 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L70] ^[angst-und-vermeidung-in-dis-systemen.md:L53]; proposed |
| Perspektive | Throughline | 0.98 | 182 | 33 | 21 | stated in 1 doc(s) ^[coherence-critique-and-question-generation.md:L85] |
| Bewusstsein | Witness Function | 0.90 | 200 | 14 | 10 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L56] |
| Erleben | Qualia | 0.89 | 119 | 93 | 60 | stated in 15 doc(s) ^[kohaerenz-protokoll-themenanalyse-und-anreicheru.md:L160] ^[kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md.md:L366] |
| Potential | Potenzial | 0.99 | 64 | 148 | 27 | stated in 1 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L143] |
| Dissoziation | Spaltung | 0.88 | 157 | 53 | 47 | stated in 2 doc(s) ^[aegis-genesis-krise-konzeptioneller-rahmen.md:L57] ^[genesis-krise-aegis-prosa-auftrag.md:L78] |
| Strukturelle | Structural | 0.88 | 88 | 120 | 38 | proposed |
| Ketsu | Synthese | 0.97 | 5 | 199 | 5 | stated in 1 doc(s) ^[dramatica-und-kohaerenz-protokoll-analyse.md:L63] |
| Emergenz | Emergence | 0.97 | 127 | 75 | 32 | stated in 1 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L191]; proposed |
| Identität | IDENTITY | 0.86 | 189 | 6 | 5 | proposed |
| Persönlichkeit | Personality | 0.95 | 110 | 85 | 35 | proposed |
| Resonanz | Shared Experience | 0.87 | 194 | 1 | 1 | stated in 1 doc(s) ^[dramatica-storyform-kohaerenz-protokoll-analyse.md:L116] |
| Alters | Parts | 0.97 | 91 | 100 | 39 | stated in 3 doc(s) ^[gutachten-grad-der-behinderung-bei-dis.md:L63] ^[roman-entwicklung-ontologie-trauma-horror.md:L86] |
| Emergenz | emergence | 0.94 | 127 | 64 | 25 | proposed |
| Entstehung | Genesis | 0.93 | 77 | 112 | 38 | stated in 1 doc(s) ^[aegis-paradoxon-konzeption-und-analyse.md:L197] |
| Leere | Void | 1.00 | 147 | 39 | 25 | stated in 4 doc(s) ^[the-coherence-protocol-a-world-bible.md:L23] ^[genesis-recherche-anleitung-umsetzung.md:L1052] |
| Angst | Dread | 0.93 | 170 | 15 | 14 | stated in 6 doc(s) ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L190] ^[genesis-mehrstufige-recherche-und-ausformulierung.md:L180]; proposed |
| Geschichte | Grand Argument Story | 0.93 | 163 | 21 | 13 | stated in 2 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L15] ^[dual-kernel-erzaehlarchitektur-bewusstsein-symmetrie-ourobor.md:L266] |
| Risse | cracks | 0.99 | 164 | 19 | 18 | proposed |
| Anteil | Part | 0.99 | 97 | 85 | 25 | stated in 1 doc(s) ^[tattoo-konzept-symbolik-trauma-heilung.md:L134] |
| Beziehung | Relationship Story | 0.88 | 158 | 24 | 16 | stated in 1 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L17] |
| Integrität | Integrity | 0.93 | 115 | 67 | 31 | proposed |
| Strukturelle | structural | 0.82 | 88 | 94 | 38 | proposed |
| Architektur | ARCHITECTURE | 0.82 | 171 | 9 | 7 | proposed |
| Kollaps | Oblivion | 0.90 | 149 | 31 | 14 | stated in 1 doc(s) ^[roman-konzept-dualitaet-kohaerenz-spannung.md:L43] |
| Nichts | Nothingness | 0.98 | 151 | 29 | 24 | proposed |
| Fundament | Bulk | 0.84 | 166 | 13 | 11 | stated in 1 doc(s) ^[kohaerenz-protokoll-transzendenz-vektoren.md:L34] |
| Welten | Worlds | 0.84 | 116 | 63 | 20 | proposed |
| Konsistenz | Consistency | 0.82 | 154 | 24 | 12 | proposed |
| Anteilen | Parts | 0.98 | 77 | 100 | 24 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L29] |
| Zusammenbruch | Collapse | 0.94 | 107 | 69 | 12 | proposed |
| Theorie | theoretical framework | 0.80 | 167 | 9 | 0 | proposed |
| Risse | Rifts | 0.98 | 164 | 11 | 11 | stated in 3 doc(s) ^[integriertes-kohaerenz-protokoll-erstellung.md:L363] ^[deconstructing-reality-s-architecture.md:L208]; proposed |
| Risse | Cracks | 0.99 | 164 | 10 | 9 | stated in 1 doc(s) ^[systemic-architecture-specification-the-coherence-protocol-w.md:L78]; proposed |
| Kernwelten | Core Worlds | 0.99 | 134 | 39 | 31 | stated in 8 doc(s) ^[an-architecture-of-the-self-a-psycho-systemic-analysis-of-ko.md:L96] ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1773]; proposed |
| Wächter | Guardian | 0.82 | 82 | 89 | 44 | stated in 1 doc(s) ^[umfassendes-lokalitaeten-konzept-fuer-roman.md:L31]; proposed |
| Nichts | nothing | 0.87 | 151 | 20 | 14 | proposed |
| Paar Truth | Wahrheit | 0.97 | 1 | 168 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-duale-dramatica-storyform-synthese.md:L90] |
| Risse | Fissures | 1.00 | 164 | 2 | 2 | stated in 1 doc(s) ^[refining-dramatica-storyform-for-kohaerenz-protokoll.md:L116]; proposed |
| Dissoziation der Persönlichkeit | Structural Dissociation | 0.99 | 65 | 97 | 30 | proposed |
| SELBST | Self | 0.90 | 1 | 161 | 1 | proposed |
| Selbsterhaltung | Autopoiesis | 0.86 | 64 | 97 | 45 | stated in 2 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L1096] ^[aegis-philosophische-und-systemtheoretische-analyse-docx.md:L207] |
| Handlung | Overall Story | 0.81 | 147 | 13 | 6 | stated in 1 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L17] |
| Krise | crisis | 0.86 | 126 | 34 | 14 | proposed |
| Entropie | ENTROPY | 0.93 | 152 | 7 | 5 | proposed |
| Leere | emptiness | 0.81 | 147 | 12 | 5 | proposed |
| Wissen | Mass | 0.90 | 147 | 12 | 7 | stated in 1 doc(s) ^[kohaerenz-protokoll-dramatica-synthese-masterkonzept.md:L73] |
| Grenze | Boundary | 1.00 | 128 | 30 | 16 | stated in 2 doc(s) ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L25] ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L234] |
| Leser | reader | 0.89 | 116 | 42 | 6 | proposed |
| Krise | Crisis | 0.98 | 126 | 31 | 15 | proposed |
| Metamorphose | Transformation | 0.95 | 12 | 145 | 9 | proposed |
| Erzeugung | Genesis | 0.95 | 42 | 112 | 12 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L298] |
| Quest | Suche | 0.98 | 18 | 136 | 15 | stated in 1 doc(s) ^[kohaerenz-protokoll-2.md:L93] |
| Wir | We | 0.97 | 74 | 80 | 12 | proposed |
| Entscheidung | Decision | 0.97 | 115 | 38 | 23 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse.md:L106]; proposed |
| Herzstück | core | 0.86 | 21 | 132 | 3 | proposed |
| Gesamtsystem | Host | 0.90 | 55 | 96 | 16 | stated in 1 doc(s) ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L68] |
| Anomalie | Anomaly | 0.91 | 129 | 21 | 8 | proposed |
| Tacit Knowledge | Wissen | 0.84 | 2 | 147 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-thematische-tiefenanalyse.md:L25] |
| Wir | we | 0.96 | 74 | 75 | 10 | proposed |
| Wächter | Gatekeeper | 0.96 | 82 | 66 | 26 | proposed |
| Multiplizität | Multiplicity | 0.98 | 92 | 56 | 18 | proposed |
| Strukturelle Dissoziation | Structural Dissociation | 0.98 | 51 | 97 | 26 | proposed |
| Multiplizität | multiplicity | 1.00 | 92 | 55 | 6 | proposed |
| Leser | Reader | 0.94 | 116 | 29 | 16 | proposed |
| ANPs | Hosts | 0.93 | 122 | 18 | 10 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptentwicklung.md:L122] |
| Widersprüche | Dialetheias | 0.95 | 137 | 3 | 3 | stated in 1 doc(s) ^[integriertes-kohaerenz-protokoll-erstellung.md:L296] |
| Fragmente | Fragments | 0.88 | 103 | 35 | 22 | proposed |
| Auslöser | Trigger | 0.99 | 49 | 88 | 28 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L130] |
| Gedächtnis | Echo | 0.89 | 56 | 81 | 14 | stated in 1 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L1062] |
| Möglichkeiten | possibilities | 0.93 | 115 | 22 | 2 | proposed |
| Kernwelten | Four Core Worlds | 1.00 | 134 | 2 | 2 | stated in 1 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L288] ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L714] |
| Anomalie | ANOMALY | 0.80 | 129 | 5 | 5 | proposed |
| Gedächtnis | Memory | 0.85 | 56 | 78 | 16 | proposed |
| Schnittstelle | Interface | 0.96 | 75 | 58 | 23 | proposed |
| Perspektiven | Throughlines | 0.98 | 105 | 28 | 18 | stated in 1 doc(s) ^[kohaerenz-protokoll-dramatica-synthese.md:L67] |
| Domäne der Fixed Attitude | Mind | 0.85 | 1 | 131 | 1 | stated in 1 doc(s) ^[dramatica-und-kohaerenz-protokoll-analyse.md:L39] |
| Psychologische Struktur | Mind | 0.93 | 1 | 131 | 1 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse-2.md:L79] |
| Beobachter | observer | 0.87 | 103 | 28 | 7 | proposed |
| Netzwerk | network | 0.80 | 95 | 36 | 15 | proposed |
| Symmetrie | symmetry | 0.98 | 82 | 49 | 20 | proposed |
| Handlungsfähigkeit | Agency | 1.00 | 61 | 69 | 26 | stated in 1 doc(s) ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L268]; proposed |
| Vermeidung | Avoidance | 1.00 | 116 | 14 | 3 | stated in 1 doc(s) ^[narrative-context-protocol-ncp-spezifikation.md:L58]; proposed |
| Dissoziation der Persönlichkeit | Dissociation of the Personality | 0.99 | 65 | 65 | 24 | proposed |
| Domäne | Domain | 0.99 | 84 | 44 | 11 | stated in 1 doc(s) ^[narrative-context-protocol-ncp-spezifikation.md:L53] |
| Vergangenheit | Past | 0.94 | 102 | 26 | 10 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse.md:L79]; proposed |
| drei | Three | 0.91 | 111 | 17 | 6 | proposed |
| Beides | Paradox | 0.83 | 8 | 119 | 1 | stated in 1 doc(s) ^[dialetheismus-im-kohaerenz-protokoll.md:L106] |
| Integrative Verbindung | Moonshine | 0.86 | 1 | 126 | 1 | stated in 1 doc(s) ^[konzeptanalyse-kohaerenz-protokoll-s-fundament.md:L161] |
| Möglichkeiten | Possibilities | 0.98 | 115 | 12 | 3 | proposed |
| Anteile | Personas | 0.96 | 112 | 13 | 8 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-loglines.md:L80] |
| Barrieren | Firewalls | 0.81 | 98 | 27 | 18 | stated in 1 doc(s) ^[kohaerenz-prozess-grundlagen.md:L152] |
| Funktionale | functional | 0.88 | 54 | 71 | 3 | proposed |
| Landschaft | landscape | 0.98 | 83 | 42 | 7 | proposed |
| Beobachter | Observer | 0.95 | 103 | 21 | 12 | proposed |
| Internes | internal | 0.82 | 11 | 111 | 4 | proposed |
| Konstrukt | construct | 0.98 | 101 | 21 | 3 | proposed |
| Emergente | emergent | 0.85 | 28 | 93 | 17 | proposed |
| Reversible Kern | Coherence | 0.86 | 1 | 119 | 1 | stated in 1 doc(s) ^[dramatica-storyform-kohaerenz-protokoll-analyse.md:L44] |
| Funktionale | Functional | 0.81 | 54 | 66 | 12 | proposed |
| Erstarrung | Freeze | 1.00 | 45 | 74 | 22 | stated in 1 doc(s) ^[strukturelle-dissoziation-system-kael-analyse.md:L324] |
| Konstrukt | Construct | 0.96 | 101 | 17 | 3 | proposed |
| strukturelle Dissoziation | Structural Dissociation | 0.96 | 21 | 97 | 10 | proposed |
| Anagnorisis | Erkenntnis | 0.98 | 2 | 115 | 2 | stated in 1 doc(s) ^[aegis-paradoxon-konzeption-und-analyse.md:L55] |
| Grenzfeste | Cerberus | 0.99 | 32 | 85 | 26 | stated in 6 doc(s) ^[kohaerenz-protokoll-2.md:L77] ^[roman-lokalitaeten-konzept-und-ausarbeitung-2.md:L148] |
| Protokolle | Protocols | 0.93 | 95 | 22 | 5 | proposed |
| Bindung | Attachment | 0.99 | 82 | 34 | 18 | stated in 1 doc(s) ^[kohaerenz-protokoll-dramatica-synthese.md:L144]; proposed |
| Gefüge | structure | 0.83 | 29 | 86 | 6 | proposed |
| Maschine | Machine | 0.89 | 73 | 42 | 14 | proposed |
| Symmetrie | Symmetry | 0.87 | 82 | 32 | 20 | proposed |
| Anteile | Identity-States | 1.00 | 112 | 1 | 1 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L82] |
| Domänen | Class | 0.91 | 59 | 53 | 12 | stated in 1 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L133] |
| Netzwerk | Graph | 0.87 | 95 | 17 | 13 | stated in 2 doc(s) ^[kohaerenz-protokoll.md:L1142] ^[kohaerenz-protokoll-umfassendes-konzept.md:L30] |
| Ontologie | ONTOLOGY | 0.86 | 105 | 5 | 2 | proposed |
| Katalysator | catalyst | 0.99 | 84 | 24 | 3 | proposed |
| Homöostase | Gleichgewicht | 0.81 | 33 | 74 | 17 | stated in 2 doc(s) ^[juna-kael-system-krisenanalyse-und-rettungsplan.md:L37] ^[strukturelle-dissoziation-system-kael-analyse.md:L221] |
| Moros | Oblivion | 0.89 | 76 | 31 | 19 | stated in 1 doc(s) ^[ki-prompt-analyse-hard-problem-of-consciousness.md:L28] |
| Agenten | agents | 0.91 | 75 | 31 | 6 | proposed |
| Wachstum | Growth | 0.90 | 74 | 32 | 15 | proposed |
| Strukturelle Dissoziation der Persönlichkeit | Structural Dissociation | 0.89 | 9 | 97 | 3 | proposed |
| Hüter | Guardians | 0.99 | 15 | 88 | 9 | stated in 1 doc(s) ^[guardians-und-kern-welten-konzept.md:L15] |
| Landschaft | Landscape | 0.98 | 83 | 20 | 9 | proposed |
| Katalysator | Catalyst | 1.00 | 84 | 18 | 3 | stated in 1 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L306]; proposed |
| Mnemosyne | Resonance Landscape | 0.91 | 93 | 9 | 9 | stated in 2 doc(s) ^[the-psychological-mechanics-from-tertiary-structural-dissoci.md:L58] ^[an-ontological-and-systemic-overview-of-the-coherence-protoc.md:L90] |
| Autopoiese | Autopoiesis | 0.94 | 4 | 97 | 3 | stated in 1 doc(s) ^[aegis-logik-und-narrative-implikationen.md:L247] ^[aegis-logik-und-narrative-implikationen.md:L247]; proposed |
| Entscheidungen | Decisions | 0.90 | 95 | 6 | 5 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse.md:L89]; proposed |
| Auseinandersetzung | Storming the Castle Trope | 0.97 | 98 | 2 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptentwicklung.md:L380] |
| Shadow | Wut | 0.90 | 27 | 73 | 11 | stated in 1 doc(s) ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L309] ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L914] |
| Einsicht | Gnosis | 0.88 | 67 | 32 | 10 | stated in 1 doc(s) ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L258] ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L295] |
| Verkörperung | Embodiment | 0.97 | 81 | 18 | 9 | stated in 3 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L228] ^[flow-zustaende-und-dissoziative-identitaet.md:L106]; proposed |
| Wirt | Host | 0.88 | 3 | 96 | 1 | proposed |
| Gastgeber | Host | 0.98 | 2 | 96 | 2 | proposed |
| Reiz | Trigger | 1.00 | 10 | 88 | 2 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L61] |
| entropie | entropy | 0.96 | 9 | 89 | 5 | proposed |
| Agenten | Agents | 0.95 | 75 | 22 | 12 | proposed |
| Domain | Class | 0.96 | 44 | 53 | 18 | stated in 4 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L448] ^[dramatica-storyform-fuer-romananalyse.md:L49] |
| Gruppe | Group | 0.96 | 48 | 49 | 17 | proposed |
| Dissonanz | Dissonance | 0.99 | 79 | 17 | 9 | proposed |
| Verschränkung | Entanglement | 0.96 | 48 | 48 | 16 | proposed |
| Wächtern | Guardians | 0.97 | 8 | 88 | 6 | proposed |
| Identitätsstörung | identity disorder | 0.99 | 74 | 22 | 12 | proposed |
| Feld | Field | 0.85 | 70 | 25 | 10 | proposed |
| KOHÄRENZ | coherence | 0.99 | 10 | 85 | 0 | proposed |
| Status Quo | Universe | 0.97 | 19 | 76 | 11 | stated in 1 doc(s) ^[kohaerenz-protokoll-dramatica-synthese-masterkonzept.md:L172] |
| Informationstheorie | information theory | 0.98 | 60 | 34 | 18 | proposed |
| Eskalation | Escalation | 0.99 | 83 | 10 | 4 | proposed |
| Unvollständigkeit | Incompleteness | 0.99 | 51 | 42 | 17 | proposed |
| Kapitel | Slots | 0.83 | 83 | 10 | 10 | stated in 1 doc(s) ^[kohaerenz-protokoll-projekt-rekonstruktion.md:L148] |
| Akzeptanz der Wahrheit | Truth | 0.88 | 2 | 90 | 1 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse-2.md:L89] |
| Alters | Identified Personality Parts | 0.93 | 91 | 1 | 1 | stated in 1 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1603] |
| Alters | ages | 0.84 | 91 | 1 | 1 | proposed |
| Komponente | Component | 0.86 | 70 | 22 | 5 | proposed |
| Überwelt | Overworld | 1.00 | 82 | 10 | 10 | stated in 5 doc(s) ^[the-coherence-protocol-a-worldbuilding-bible.md:L99] ^[welt.md:L66]; proposed |
| Parakonsistente | paraconsistent | 0.98 | 36 | 56 | 16 | proposed |
| Axiome | axioms | 0.98 | 55 | 35 | 1 | proposed |
| Kohärenz-Protokoll | Coherence Protocol | 0.92 | 36 | 54 | 10 | proposed |
| Kernwelt | Core World | 1.00 | 73 | 17 | 9 | stated in 1 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L967]; proposed |
| Spiel | Game | 0.93 | 59 | 31 | 17 | proposed |
| Gittereffekte | Glitches | 0.95 | 3 | 87 | 2 | stated in 1 doc(s) ^[physik-fuer-simulierte-realitaet.md:L568] |
| Gruppe | group | 0.93 | 48 | 42 | 22 | proposed |
| kohaerenz | coherence | 0.96 | 5 | 85 | 1 | proposed |
| Kausalität | Causality | 0.99 | 76 | 13 | 5 | proposed |
| Korrespondenz | Correspondence | 0.94 | 42 | 47 | 13 | proposed |
| Rekonfiguration | Emergence | 0.80 | 14 | 75 | 6 | stated in 2 doc(s) ^[the-architecture-of-being-a-philosophical-thesis-on-the-core.md:L30] ^[causal-linkage-a-report-on-tsdp-cache-incoherence-and-the-me.md:L30] |
| Potentialität | Potentiality | 0.90 | 63 | 26 | 7 | proposed |
| Übergang | Threshold Zone | 0.99 | 88 | 1 | 1 | stated in 1 doc(s) ^[roman-outline-system-kael.md:L275] |
| C-System-Inkonsistenz | Glitches | 0.81 | 1 | 87 | 1 | stated in 1 doc(s) ^[parakonsistente-logik-im-seelen-protokoll.md:L322] |
| Erstarren | Freeze | 0.99 | 14 | 74 | 9 | stated in 3 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L32] ^[kohaerenz-protokoll-audit-und-verifizierung.md:L70] |
| Autonomie | autonomy | 0.95 | 77 | 10 | 6 | proposed |
| Klasse | Class | 0.99 | 34 | 53 | 5 | stated in 1 doc(s) ^[dramatica-und-kohaerenz-protokoll-analyse.md:L89]; proposed |
| Einfrieren | Freeze | 0.97 | 13 | 74 | 7 | proposed |
| Funktionale Multiplizität | Functional Multiplicity | 1.00 | 36 | 51 | 9 | proposed |
| Hoffnung | Hope | 0.97 | 76 | 11 | 6 | proposed |
| Inkohärenz | Incoherence | 0.91 | 80 | 7 | 2 | proposed |
| Verschränkung | entanglement | 0.96 | 48 | 39 | 17 | proposed |
| Autonomie | Autonomy | 0.97 | 77 | 9 | 6 | proposed |
| Bindung | binding | 0.85 | 82 | 4 | 0 | proposed |
| Stadt | City | 0.98 | 62 | 24 | 7 | proposed |
| Übereinstimmung | Correspondence | 0.94 | 39 | 47 | 7 | proposed |
| Kohaerenz | coherence | 0.89 | 1 | 85 | 0 | proposed |
| Riss | Rift | 0.99 | 83 | 3 | 3 | proposed |
| Systemtheorie | systems theory | 0.83 | 73 | 13 | 6 | proposed |
| Riss | Crack | 0.98 | 83 | 2 | 1 | proposed |
| Dissoziative Identitätsstörung | Dissociative Identity Disorder | 0.99 | 41 | 44 | 15 | proposed |
| Selbstorganisation | self-organization | 0.99 | 69 | 16 | 10 | proposed |
| Strukturelle Dissoziation | structural dissociation | 0.99 | 51 | 34 | 15 | proposed |
| Beschützer | Protector | 0.98 | 43 | 41 | 7 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L421]; proposed |
| Bindung | Binding | 0.89 | 82 | 2 | 0 | proposed |
| Tod | Death | 0.88 | 59 | 25 | 8 | proposed |
| Riss | Fissure | 0.95 | 83 | 1 | 1 | proposed |
| Verankerung | Grounding | 0.86 | 61 | 23 | 5 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L107]; proposed |
| Überwelt | OVERWORLD | 0.99 | 82 | 2 | 2 | proposed |
| parakonsistente Logik | Paraconsistent Logic | 1.00 | 38 | 46 | 14 | proposed |
| Selbsterhaltung | self-preservation | 0.85 | 64 | 20 | 0 | proposed |
| Unvollständigkeit | incompleteness | 0.99 | 51 | 33 | 19 | proposed |
| Quantenverschränkung | Quantum Entanglement | 0.80 | 49 | 34 | 12 | proposed |
| Außen | External | 0.94 | 40 | 42 | 6 | proposed |
| Dissoziativen Identitätsstörung | Dissociative Identity Disorder | 0.91 | 38 | 44 | 10 | proposed |
| Löschung | Erasure | 0.99 | 51 | 31 | 19 | proposed |
| Inkonsistenz | Inconsistency | 0.92 | 58 | 24 | 8 | proposed |
| Kausalität | causality | 0.99 | 76 | 6 | 0 | proposed |
| Potentialmeer | Sea of Potentiality | 1.00 | 70 | 12 | 7 | stated in 1 doc(s) ^[the-coherence-protocol-a-worldbuilding-bible.md:L121] |
| Ganzheit | Wholeness | 0.96 | 69 | 12 | 3 | proposed |
| Integriertes | integrated | 0.91 | 8 | 73 | 0 | proposed |
| Transzendenz | Transcendence | 0.90 | 68 | 13 | 8 | proposed |
| Anker | Anchor | 0.80 | 71 | 9 | 5 | proposed |
| Kognition | Cognition | 0.96 | 54 | 26 | 10 | proposed |
| Emotionale Teile | Emotional Parts | 0.91 | 2 | 78 | 1 | proposed |
| Fehlermodus | Glitch | 0.86 | 6 | 74 | 4 | stated in 1 doc(s) ^[kohaerenz-protokoll-transzendenz-vektoren.md:L132] ^[kohaerenz-protokoll-transzendenz-vektoren.md:L188] |
| Funke | Intrusion | 0.82 | 33 | 47 | 6 | stated in 1 doc(s) ^[in-teil-2-werden-die-persona-von-ihren-spezifis.md:L87] |
| Haltung | Attitude | 0.88 | 57 | 22 | 8 | proposed |
| emotionale Teile | Emotional Parts | 0.98 | 1 | 78 | 0 | proposed |
| Gleichgewicht | Equity | 0.98 | 74 | 5 | 3 | stated in 1 doc(s) ^[narrative-context-protocol-ncp-spezifikation.md:L57] |
| Ethik | Value Alignment Problem | 0.95 | 63 | 16 | 12 | stated in 2 doc(s) ^[aegis-paradoxon-neukonzeption-und-analyse-docx.md:L37] ^[aegis-paradoxon-konzeption-und-analyse.md:L54] |
| Last | Burden | 0.88 | 72 | 6 | 2 | proposed |
| Überwachung | Bus Snooping | 0.98 | 77 | 1 | 1 | stated in 1 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L203] |
| Domain | Klasse | 0.93 | 44 | 34 | 5 | stated in 1 doc(s) ^[dual-kernel-erzaehlarchitektur-bewusstsein-symmetrie-ourobor.md:L135] |
| Haltung | Fixed Attitude | 0.91 | 57 | 21 | 8 | stated in 1 doc(s) ^[duale-storyform-synthese-kohaerenz-protokoll.md:L70] |
| Flow | Fluss | 0.84 | 14 | 64 | 5 | stated in 1 doc(s) ^[projektanalyse-kohaerenz-protokoll-dis.md:L226] |
| IFS-Modell | Internal Family Systems | 0.99 | 21 | 57 | 17 | stated in 1 doc(s) ^[kohaerenz-protokoll-projekt-rekonstruktion.md:L143] |
| Nichts Rauschen | Nothingness Noise | 1.00 | 65 | 13 | 10 | stated in 2 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L776] ^[the-coherence-protocol-a-world-bible.md:L21] |
| Schicht | layer | 0.90 | 49 | 29 | 2 | proposed |
| Selbstorganisation | Self-organization | 0.99 | 69 | 9 | 7 | proposed |
| Systemtheorie | SystemTheory | 0.98 | 73 | 5 | 4 | proposed |
| Systemtheorie | Systems theory | 0.98 | 73 | 5 | 4 | proposed |
| Auslöschung | Oblivion | 0.99 | 46 | 31 | 3 | stated in 1 doc(s) ^[roman-konzept-kael-aegis-simulation.md:L264] |
| Domäne der Situation | Universe | 0.98 | 1 | 76 | 1 | stated in 1 doc(s) ^[dramatica-und-kohaerenz-protokoll-analyse.md:L39] |
| EP-Erstarrung | Freeze | 0.99 | 3 | 74 | 3 | stated in 1 doc(s) ^[tattoo-konzept-symbolik-trauma-heilung.md:L187] |
| emergenz | Emergence | 0.97 | 2 | 75 | 0 | proposed |
| Schicht | Layer | 0.91 | 49 | 28 | 6 | proposed |
| Stufe | Level | 0.86 | 37 | 40 | 6 | proposed |
| Parakonsistente Logik | Paraconsistent Logic | 1.00 | 31 | 46 | 18 | proposed |
| Potentialmeer | Potential Sea | 0.98 | 70 | 7 | 3 | proposed |
| Autopoietische | autopoietic | 0.98 | 26 | 50 | 5 | proposed |
| Dialetheismus | Dialetheism | 0.99 | 47 | 29 | 15 | proposed |
| Verteidigung | Fight-Response | 0.82 | 72 | 4 | 2 | stated in 1 doc(s) ^[hard-sf-roman-outline-dkt-physik-cosmic-horror.md:L53] |
| Torwächter | Gatekeeper | 0.98 | 10 | 66 | 6 | proposed |
| Mosaik | Mosaic | 0.96 | 58 | 18 | 12 | proposed |
| parakonsistent | Paraconsistent | 0.93 | 20 | 56 | 11 | proposed |
| Schatten | Persecutor | 0.88 | 58 | 18 | 3 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzept.md:L359] |
| Phänomenologie | Phenomenology | 0.89 | 52 | 24 | 13 | proposed |
| Systemtheorie | system theory | 0.98 | 73 | 3 | 0 | proposed |
| Bewegung | movement | 0.94 | 60 | 15 | 3 | proposed |
| Immobilisation | Freeze | 0.84 | 1 | 74 | 1 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L49] |
| Kaels Reise | Kael's journey | 0.93 | 46 | 29 | 0 | proposed |
| parakonsistente Logik | paraconsistent logic | 1.00 | 38 | 37 | 8 | proposed |
| Domänen | Classes | 0.90 | 59 | 15 | 10 | stated in 1 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L36] |
| Logiken | Logics | 0.82 | 44 | 30 | 14 | proposed |
| Resonanz-Landschaft | Mnemosyne-Archipel | 0.95 | 23 | 51 | 3 | stated in 1 doc(s) ^[welt.md:L96] |
| Phänomenologie | phenomenology | 0.99 | 52 | 22 | 12 | proposed |
| Entfremdung | Alienation | 0.89 | 65 | 8 | 3 | proposed |
| Beschützer | protector | 0.88 | 43 | 30 | 3 | proposed |
| Schatten | Firefighter | 0.87 | 58 | 15 | 6 | stated in 3 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik.md:L71] ^[kael-charakterarchitektur-und-konfliktdynamik-2.md:L71] |
| Modus | Mode | 0.81 | 46 | 27 | 6 | proposed |
| Agentur | Agency | 0.84 | 3 | 69 | 1 | proposed |
| Gefühl der Handlungsfähigkeit | Agency | 0.91 | 3 | 69 | 1 | stated in 1 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L75] |
| Gott | God | 0.93 | 38 | 34 | 7 | proposed |
| Agentschaft | Agency | 1.00 | 2 | 69 | 2 | stated in 1 doc(s) ^[emergenz-autonomer-systeme-aegis-forschung.md:L378]; proposed |
| Begründung | Justification | 0.84 | 55 | 16 | 4 | proposed |
| Kybernetik | Cybernetics | 0.98 | 50 | 21 | 19 | proposed |
| Korrespondenz | correspondence | 0.95 | 42 | 29 | 8 | proposed |
| Kohärenzprotokoll | Coherence Protocol | 0.85 | 16 | 54 | 4 | proposed |
| Irreversible Kern | Collapse | 0.86 | 1 | 69 | 1 | stated in 1 doc(s) ^[dramatica-storyform-kohaerenz-protokoll-analyse.md:L48] |
| Domänen | Domains | 0.81 | 59 | 11 | 3 | proposed |
| Genesis-Krise | Genesis Crisis | 0.99 | 57 | 13 | 3 | stated in 1 doc(s) ^[risikoanalysebericht-eine-systematische-bewertung-der-bedroh.md:L85] |
| Kael und Juna | Kael and Juna | 0.97 | 48 | 22 | 1 | proposed |
| Kognition | cognition | 0.93 | 54 | 16 | 8 | proposed |
| Melancholie | Melancholy | 0.99 | 54 | 16 | 3 | proposed |
| Monstergruppe | Monster group | 0.97 | 44 | 26 | 19 | proposed |
| Pfad | Path | 0.91 | 42 | 28 | 8 | proposed |
| Anscheinend Normalen Teilen | Apparently Normal Parts | 0.98 | 4 | 64 | 0 | proposed |
| Verhaltens | Behavioral | 0.87 | 34 | 34 | 7 | proposed |
| Kybernetik | cybernetics | 0.96 | 50 | 18 | 17 | proposed |
| Parakonsistente Logik | paraconsistent logic | 0.97 | 31 | 37 | 7 | proposed |
| Überlagerung | Superposition | 1.00 | 30 | 38 | 7 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L37] |
| Blindheit | Blindness | 0.96 | 52 | 15 | 2 | proposed |
| Kosmischer | Cosmic | 0.97 | 21 | 46 | 14 | proposed |
| Einbruch | Intrusion | 0.83 | 20 | 47 | 3 | proposed |
| Informationstheorie | Information theory | 0.99 | 60 | 7 | 6 | proposed |
| Nicht-Sein | Nothingness | 0.81 | 38 | 29 | 3 | proposed |
| Parakonsistent | Paraconsistent | 0.92 | 11 | 56 | 5 | proposed |
| Parakonsistent | paraconsistent | 0.97 | 11 | 56 | 4 | proposed |
| Abhängigkeit | Pratītyasamutpāda | 0.95 | 63 | 3 | 3 | stated in 2 doc(s) ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L98] ^[narrativ-existenzieller-kohaerenz-nzt-protokoll.md:L87] |
| Anscheinend Normale Teile | Apparently Normal Parts | 0.99 | 2 | 64 | 1 | proposed |
| Kohärenztheorie | Coherence Theory | 0.84 | 35 | 31 | 8 | proposed |
| Dissoziation der Persönlichkeit | DISSOCIATION OF THE PERSONALITY | 0.95 | 65 | 1 | 1 | proposed |
| emergenz | emergence | 0.94 | 2 | 64 | 0 | proposed |
| Rand | Boundary | 1.00 | 35 | 30 | 6 | stated in 2 doc(s) ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L52] ^[holographisches-prinzip-fuer-kohaerenz-protokoll-2.md:L52] |
| klassisch | Classical | 0.92 | 25 | 40 | 6 | proposed |
| Kontakt | Contact | 0.87 | 58 | 7 | 4 | proposed |
| Potentialität | Dunamis | 0.97 | 63 | 2 | 2 | stated in 1 doc(s) ^[ontologie-des-gelesenen-traumas.md:L193] |
| Erzähler | Narrator | 0.91 | 44 | 21 | 11 | proposed |
| Informationstheorie | Information_theory | 0.95 | 60 | 5 | 4 | proposed |
| Void | Nothing | 0.85 | 39 | 26 | 10 | stated in 1 doc(s) ^[thematic-architecture-of-kohaerenz-protokoll-a-conceptual-le.md:L25] |
| Theorie der Strukturellen Dissoziation | Theory of structural dissociation | 1.00 | 57 | 8 | 4 | proposed |
| Beides | both | 0.93 | 8 | 56 | 1 | proposed |
| Benutzeroberfläche | Interface | 0.80 | 6 | 58 | 6 | proposed |
| Dual-Kernel-Theorie | Dual Kernel Theory | 0.92 | 22 | 42 | 6 | proposed |
| Potentialität | Dynamis | 0.81 | 63 | 1 | 1 | stated in 1 doc(s) ^[rechercheauftrag-die-genesis-von-aegis.md:L29] |
| Gesamtsystem | integrated system | 0.92 | 55 | 9 | 0 | proposed |
| Gödel-Satz | Gödel-sentence | 0.98 | 56 | 8 | 3 | proposed |
| Schwingung | Resonance | 0.90 | 14 | 50 | 0 | proposed |
| Substrat | Substrate | 0.94 | 49 | 15 | 7 | proposed |
| Gesamtsystem | total system | 0.80 | 55 | 8 | 0 | proposed |
| Kernlogik | core logic | 0.92 | 45 | 18 | 0 | proposed |
| Logiken | logics | 0.93 | 44 | 19 | 9 | proposed |
| Metamorphose | transformation | 0.87 | 12 | 51 | 2 | proposed |
| zweite | Second | 0.92 | 36 | 27 | 10 | proposed |
| Substrat | substrate | 0.88 | 49 | 14 | 2 | proposed |
| Ambivalenz | Ambivalence | 0.98 | 55 | 7 | 4 | proposed |
| Löschung | deletion | 0.93 | 51 | 11 | 1 | proposed |
| Modul | Module | 0.92 | 30 | 32 | 7 | proposed |
| parakonsistente Logik | Paraconsistent logic | 0.97 | 38 | 24 | 9 | proposed |
| Relationaler | relational | 0.82 | 8 | 54 | 1 | proposed |
| Theorie der Strukturellen Dissoziation | theory of structural dissociation | 0.99 | 57 | 5 | 4 | proposed |
| Korrespondenztheorie | Correspondence Theory | 0.97 | 33 | 28 | 9 | proposed |
| Spezifikation | Specification | 0.95 | 27 | 34 | 12 | proposed |
| Substanz | substance | 0.89 | 51 | 10 | 0 | proposed |
| Kohärenztheorie der Wahrheit | Coherence Theory of Truth | 0.99 | 31 | 29 | 6 | stated in 2 doc(s) ^[dramatica-storyform-kohaerenz-protokoll-2.md:L15] ^[risikoanalysebericht-eine-systematische-bewertung-der-bedroh.md:L77]; proposed |
| Kosmischer Horror | Cosmic Horror | 0.99 | 21 | 39 | 14 | proposed |
| Kosmischer | cosmic | 1.00 | 21 | 39 | 10 | proposed |
| Mnemosyne-Archipel | Resonance Landscape | 0.96 | 51 | 9 | 5 | stated in 3 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L969] ^[aegis-manifest-genesis-krise-reboot.md:L77] |
| Neubewertung | Reframing | 0.98 | 44 | 16 | 4 | stated in 1 doc(s) ^[dissoziative-identitaet-sinnsuche-im-trauma.md:L183] |
| Spaltung | Splitting | 1.00 | 53 | 7 | 5 | stated in 1 doc(s) ^[dissoziative-identitaetsstoerung-unsichtbare-diagnose.md:L117]; proposed |
| Strukturellen Dissoziation der Persönlichkeit | structural dissociation of the personality | 0.95 | 46 | 14 | 9 | proposed |
| Interface | Arbeitsstation | 0.81 | 58 | 1 | 1 | stated in 1 doc(s) ^[lokalitaeten-konzept-fuer-roman-simulation.md:L270] |
| Konstrukt-Stadt | Construct City | 0.98 | 48 | 11 | 0 | proposed |
| Kategorien | Kinds | 0.92 | 55 | 4 | 3 | stated in 2 doc(s) ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L395] ^[aegis-genesis-krise-prosa-auftrag-formulieren-2.md:L395] |
| Meer | Sea | 0.91 | 35 | 24 | 1 | proposed |
| PTBS | PTSD | 0.81 | 27 | 32 | 19 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L241] |
| Protektor | Protector | 0.85 | 18 | 41 | 4 | proposed |
| Fassade | facade | 0.81 | 50 | 8 | 0 | proposed |
| Genesis-Krise | genesis crisis | 0.95 | 57 | 1 | 0 | proposed |
| Theorie der Strukturellen Dissoziation | Structural dissociation theory | 0.99 | 57 | 1 | 1 | proposed |
| Vakuum | vacuum | 0.89 | 45 | 13 | 2 | proposed |
| Axiome | Axioms | 0.94 | 55 | 2 | 1 | proposed |
| Kinder | Child | 0.82 | 17 | 40 | 3 | proposed |
| Funktionaler Multiplizität | Functional Multiplicity | 0.90 | 6 | 51 | 3 | proposed |
| Hierarchie | Hierarchy | 0.81 | 48 | 9 | 3 | proposed |
| Kaels Psyche | Kael's psyche | 0.96 | 40 | 17 | 0 | proposed |
| Skala | Scale | 0.89 | 34 | 23 | 4 | proposed |
| Vorhersagbarkeit | predictability | 0.90 | 50 | 7 | 0 | proposed |
| autopoietisches System | autopoietic system | 0.96 | 41 | 16 | 1 | proposed |
| Archipel | Archipelago | 0.86 | 52 | 4 | 2 | proposed |
| Löschung | Deletion | 0.97 | 51 | 5 | 0 | proposed |
| Spaltung | Fission | 0.89 | 53 | 3 | 3 | proposed |
| Quantenmechanik | quantum mechanics | 0.92 | 45 | 11 | 3 | proposed |
| Quantenverschränkung | Quantum entanglement | 0.99 | 49 | 7 | 7 | proposed |
| Substanz | Substance | 0.96 | 51 | 5 | 1 | proposed |
| Ahnung | Gnosis | 0.94 | 23 | 32 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-finale-pfeiler.md:L218] |
| Monstergruppe | monster group | 0.99 | 44 | 11 | 11 | proposed |
| Parakonsistente Logik | Paraconsistent logic | 0.98 | 31 | 24 | 15 | proposed |
| Verteidiger | Protector | 0.92 | 14 | 41 | 3 | proposed |
| Stufe | Step | 0.81 | 37 | 18 | 1 | proposed |
| Tragödie | tragedy | 0.98 | 39 | 16 | 5 | proposed |
| Erwachen | Awakening | 0.92 | 45 | 9 | 3 | proposed |
| Überzeugung | Belief | 0.91 | 39 | 15 | 4 | proposed |
| EPR-Vermutung | Quantenverschränkung | 0.83 | 5 | 49 | 3 | stated in 1 doc(s) ^[untersuche-in-wie-fern-juna-bzw-das-fundament-du.md:L131] |
| Entropie-Torwächter | Entropic Gatekeeper | 0.96 | 1 | 53 | 1 | proposed |
| Entropischer Torwächter | Entropic Gatekeeper | 0.95 | 1 | 53 | 1 | proposed |
| Entschlossenheit | Resolve | 1.00 | 35 | 19 | 3 | stated in 1 doc(s) ^[narrative-modelle-und-dramatica-erweiterung.md:L219] |
| Erstarrung | Freeze Response | 1.00 | 45 | 9 | 4 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L415] |
| Fragilität | fragility | 0.96 | 47 | 7 | 1 | proposed |
| Paradoxon X | Paradox of Misaligned Coherence | 0.87 | 33 | 21 | 3 | stated in 1 doc(s) ^[the-coherence-protocol-a-world-bible.md:L82] |
| Quantenverschränkung | Quantum_entanglement | 0.94 | 49 | 5 | 5 | proposed |
| Systemkollaps | system collapse | 0.99 | 42 | 12 | 0 | proposed |
| erweitert | Augmented | 0.83 | 42 | 11 | 1 | proposed |
| Betriebssystem | operating system | 0.88 | 32 | 21 | 1 | proposed |
| Überflutung | Flooding | 1.00 | 49 | 4 | 2 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L61]; proposed |
| Raumzeit | Spacetime | 0.95 | 45 | 8 | 7 | proposed |
| zweiter | Second | 0.97 | 26 | 27 | 6 | proposed |
| Strukturelle Dissoziation | Structural dissociation | 0.99 | 51 | 2 | 1 | proposed |
| Symmetrien | Symmetries | 0.90 | 46 | 7 | 5 | proposed |
| Unvollständigkeitssätze | incompleteness theorems | 1.00 | 32 | 21 | 11 | proposed |
| Boundary Fortress | Cerberus-Labyrinth | 0.96 | 5 | 47 | 4 | stated in 3 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L970] ^[aegis-manifest-genesis-krise-reboot.md:L83] |
| Depersonalization | Depersonalisation | 0.96 | 9 | 43 | 4 | proposed |
| Mnemosyne-Archipel | Swamp of Memory | 0.96 | 51 | 1 | 1 | stated in 1 doc(s) ^[welcome-to-the-coherence-protocol-a-beginner-s-guide.md:L72] |
| Strukturelle Dissoziation | structural dissociation of personality | 0.96 | 51 | 1 | 1 | proposed |
| Vakuum | Vacuum | 0.87 | 45 | 7 | 5 | proposed |
| Vektor | Vector | 0.88 | 33 | 19 | 7 | proposed |
| Erschöpfung | Burnout | 0.86 | 39 | 12 | 9 | stated in 1 doc(s) ^[emergenz-aegis-und-selbststrukturierung.md:L236] |
| Konstrukt-Stadt | Construct-City | 0.99 | 48 | 3 | 2 | stated in 1 doc(s) ^[pitch-deck-coherence-protocol.md:L72] |
| Schrecken | Dread | 0.94 | 36 | 15 | 6 | proposed |
| Fassade | Facade | 0.96 | 50 | 1 | 0 | proposed |
| Fragilität | Fragility | 0.97 | 47 | 4 | 1 | proposed |
| Integriertes | Integrated | 0.86 | 8 | 43 | 2 | proposed |
| Urteil | Judgment | 0.99 | 30 | 21 | 6 | stated in 1 doc(s) ^[narrative-modelle-und-dramatica-erweiterung.md:L220]; proposed |
| Vorhersagbarkeit | Predictability | 0.92 | 50 | 1 | 0 | proposed |
| Seele | soul | 0.85 | 40 | 11 | 2 | proposed |
| Korrespondenztheorie der Wahrheit | Correspondence Theory | 0.88 | 22 | 28 | 8 | stated in 1 doc(s) ^[dramatica-storyform-kohaerenz-protokoll-2.md:L15] |
| Rückzug | Cut-off | 0.99 | 47 | 3 | 3 | stated in 2 doc(s) ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L184] ^[beziehungsheilung-nach-trauma-konzeptpapier-3.md:L190] |
| Dramatica-Theorie | Dramatica Theory | 0.88 | 26 | 24 | 18 | proposed |
| Dual Kernel Theorie | Dual Kernel Theory | 0.99 | 8 | 42 | 0 | proposed |
| Fluktuationen | fluctuations | 0.98 | 40 | 10 | 2 | proposed |
| Garten der Möglichkeiten | Kairos-Potentialis | 0.88 | 8 | 42 | 4 | stated in 2 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L239] ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L517] |
| Knotenpunkt | Hub | 0.91 | 33 | 17 | 8 | proposed |
| Parakonsistenz | Paraconsistency | 0.96 | 35 | 15 | 8 | proposed |
| Attraktor | Attractor | 0.99 | 25 | 24 | 6 | proposed |
| Fortress of Fear | Cerberus-Labyrinth | 0.99 | 2 | 47 | 2 | stated in 1 doc(s) ^[welcome-to-the-coherence-protocol-a-beginner-s-guide.md:L78] |
| Denouement | Resolution | 0.87 | 7 | 42 | 3 | stated in 1 doc(s) ^[plotentwicklung-schluessigkeit-kohaerenz-konsistenz.md:L97] |
| Exklusion | exclusion | 1.00 | 23 | 26 | 0 | proposed |
| weder | Neither | 0.97 | 46 | 3 | 1 | proposed |
| Wahrscheinlichkeit | Probability | 0.81 | 41 | 8 | 1 | proposed |
| Systemintegrität | system integrity | 0.94 | 46 | 3 | 0 | proposed |
| Chaostheorie | Chaos Theory | 0.97 | 34 | 14 | 12 | proposed |
| Dekohärenz | decoherence | 1.00 | 27 | 21 | 3 | proposed |
| Diskrepanz | Mismatch | 1.00 | 41 | 7 | 2 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L137] |
| Kairos-Potentialis | Garden of Possibilities | 0.91 | 42 | 6 | 5 | stated in 1 doc(s) ^[the-architecture-of-fracture-a-compendium-of-the-kael-system.md:L67] |
| Gitter | Lattice | 0.97 | 32 | 16 | 5 | proposed |
| Gödels Unvollständigkeitssätze | Gödel's incompleteness theorems | 1.00 | 28 | 20 | 8 | proposed |
| Nicht-Existenz | non-existence | 0.90 | 39 | 9 | 2 | proposed |
| Raumzeit | Space Time | 0.86 | 45 | 3 | 1 | proposed |
| Raumzeit | Space-time | 0.86 | 45 | 3 | 2 | proposed |
| Tragödie | Tragedy | 0.99 | 39 | 9 | 7 | proposed |
| Ruf | Call | 0.98 | 26 | 21 | 5 | proposed |
| deterministisch | Deterministic | 0.95 | 35 | 12 | 5 | proposed |
| Dramatica-Klasse | Domain | 0.83 | 3 | 44 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-duale-dramatica-storyform-synthese.md:L64] ^[kohaerenz-protokoll-duale-dramatica-storyform-synthese.md:L88] |
| Epistemologie | Epistemology | 1.00 | 35 | 12 | 5 | proposed |
| KOHÄRENT | coherent | 0.95 | 1 | 46 | 0 | proposed |
| Nicht-Sein | non-being | 0.83 | 38 | 9 | 1 | proposed |
| Singularität | Singularity | 0.94 | 35 | 12 | 4 | proposed |
| Singularität | singularity | 0.97 | 35 | 12 | 5 | proposed |
| Strukturellen Dissoziation der Persönlichkeit | structural dissociation of personality | 0.95 | 46 | 1 | 1 | proposed |
| Systemintegrität | System integrity | 0.99 | 46 | 1 | 1 | proposed |
| Welle | Wave | 0.81 | 42 | 5 | 3 | proposed |
| operationale Geschlossenheit | operational closure | 0.82 | 26 | 21 | 2 | proposed |
| Bewahrer | Protector | 0.99 | 5 | 41 | 1 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L99] |
| kosmischer Horror | Cosmic Horror | 0.92 | 7 | 39 | 7 | proposed |
| Erforderliche Varietät | Law | 0.99 | 2 | 44 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-aktuelle-gesamtkonzept-synthese-abstrakt.md:L30] |
| Festung | Fortress | 1.00 | 26 | 20 | 3 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L182] |
| Fluktuationen | Fluctuations | 0.92 | 40 | 6 | 1 | proposed |
| Form der Kohärenz | form of coherence | 0.88 | 22 | 24 | 0 | proposed |
| Gruppen | Groups | 0.94 | 35 | 11 | 9 | proposed |
| Interferenz | interference | 0.93 | 35 | 11 | 1 | proposed |
| Persistenz | Persistence | 0.80 | 27 | 19 | 1 | proposed |
| Potenzialität | Potentiality | 0.85 | 20 | 26 | 3 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse.md:L67] |
| Quantenmechanik | Quantum mechanics | 0.99 | 45 | 1 | 1 | proposed |
| Rückkopplungsschleife | feedback loop | 0.98 | 31 | 15 | 0 | proposed |
| Aktive Integration der Fragmente | Change | 0.98 | 1 | 44 | 1 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse-2.md:L83] |
| Akzeptanz und Einstellungsänderung | Change | 0.99 | 1 | 44 | 1 | stated in 1 doc(s) ^[ki-prompt-analyse-hard-problem-of-consciousness.md:L103] |
| autopoietisch | Autopoietic | 0.93 | 21 | 24 | 4 | proposed |
| Einstellungsänderung | Change | 0.85 | 1 | 44 | 1 | stated in 1 doc(s) ^[ki-prompt-analyse-hard-problem-of-consciousness.md:L128] |
| Korrespondenztheorie der Wahrheit | Correspondence Theory of Truth | 1.00 | 22 | 23 | 5 | stated in 1 doc(s) ^[risikoanalysebericht-eine-systematische-bewertung-der-bedroh.md:L9] ^[risikoanalysebericht-eine-systematische-bewertung-der-bedroh.md:L77]; proposed |
| Zyklen | Cycles | 0.84 | 40 | 5 | 3 | proposed |
| Dramatica Klasse | Domain | 0.89 | 1 | 44 | 1 | stated in 1 doc(s) ^[dramatica-und-kohaerenz-protokoll-analyse.md:L43] |
| Rand | Edge | 0.99 | 35 | 10 | 3 | proposed |
| Glaube | Faith | 1.00 | 23 | 22 | 7 | stated in 1 doc(s) ^[dramatica-storyform-kohaerenz-protokoll-analyse.md:L103]; proposed |
| Hauptcharakter | Main Character | 0.95 | 6 | 39 | 4 | stated in 1 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L37]; proposed |
| Hauptfigur | Main Character | 0.81 | 6 | 39 | 3 | proposed |
| Schichten | Layers | 0.84 | 42 | 3 | 0 | proposed |
| Objektiv | Objective | 0.84 | 4 | 41 | 2 | proposed |
| Prinzip der Explosion | Principle of Explosion | 0.94 | 25 | 20 | 2 | proposed |
| Archetyp | Archetype | 0.97 | 28 | 16 | 8 | stated in 1 doc(s) ^[tattoo-konzept-symbolik-trauma-heilung.md:L134]; proposed |
| Verrat | Betrayal | 0.99 | 35 | 9 | 4 | proposed |
| Kritiker | Critic | 0.91 | 37 | 7 | 1 | proposed |
| Hypervigilanz | hypervigilance | 0.97 | 33 | 11 | 1 | proposed |
| Kritiker | critic | 0.96 | 37 | 7 | 1 | proposed |
| Landauer-Prinzip | Landauer Principle | 0.95 | 34 | 10 | 4 | proposed |
| Masse | Mass | 0.94 | 32 | 12 | 5 | stated in 1 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L67]; proposed |
| Parakonsistenz | paraconsistency | 0.98 | 35 | 9 | 5 | proposed |
| Topologie | topology | 0.99 | 35 | 9 | 4 | proposed |
| Verteidiger | protector | 0.90 | 14 | 30 | 2 | proposed |
| Kaskade | Cascading | 0.85 | 37 | 6 | 3 | proposed |
| Konsens | Consensus | 0.94 | 26 | 17 | 9 | proposed |
| Dekohärenz | Decoherence | 0.99 | 27 | 16 | 5 | proposed |
| Derealization | Derealisation | 0.95 | 5 | 38 | 3 | proposed |
| Glauben | Faith | 1.00 | 21 | 22 | 4 | stated in 1 doc(s) ^[kohaerenz-protokoll-duale-dramatica-storyform-synthese.md:L71] |
| Homöostase | Homeostasis | 1.00 | 33 | 10 | 3 | proposed |
| Knoten | Vertices | 0.99 | 40 | 3 | 2 | stated in 2 doc(s) ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L260] ^[aegis-genesis-krise-prosa-auftrag-formulieren-2.md:L260]; proposed |
| Ko-Bewusstsein | co-consciousness | 0.99 | 23 | 20 | 1 | proposed |
| Künstliche Intelligenz | artificial intelligence | 0.97 | 19 | 24 | 2 | proposed |
| Systemlogik | system logic | 0.96 | 42 | 1 | 0 | proposed |
| Unvollständigkeitssatz | incompleteness theorem | 0.94 | 39 | 4 | 2 | proposed |
| Übereinstimmung | Adaequatio | 0.95 | 39 | 3 | 2 | stated in 1 doc(s) ^[wahrheitstheorien-kohaerenz-vs-korrespondenz.md:L386] |
| Bruchstücke | Fragments | 0.88 | 7 | 35 | 2 | proposed |
| Kosmologie | Cosmology | 0.94 | 24 | 18 | 7 | proposed |
| Kopplung | Coupling | 1.00 | 39 | 3 | 3 | proposed |
| Externe Ebene | External Level | 1.00 | 33 | 9 | 3 | stated in 1 doc(s) ^[the-coherence-protocol-a-worldbuilding-bible.md:L120]; proposed |
| Rückkopplungsschleifen | Feedback Loops | 1.00 | 26 | 16 | 11 | stated in 1 doc(s) ^[aegis-philosophische-und-systemtheoretische-analyse-docx.md:L123] |
| Rechtfertigung | Justification | 0.87 | 26 | 16 | 7 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L64]; proposed |
| Kopplung | coupling | 1.00 | 39 | 3 | 1 | proposed |
| Krieg | Warfare | 0.93 | 36 | 6 | 0 | proposed |
| Verdrängung | Repression | 1.00 | 36 | 6 | 3 | stated in 2 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L39] ^[ki-antagonist-fragmentierte-gottheit-analyse.md:L100]; proposed |
| tragisch | Tragic | 0.83 | 11 | 31 | 0 | proposed |
| klassische Logik | Classical Logic | 1.00 | 23 | 18 | 3 | proposed |
| Komplexitätstheorie | Complexity Theory | 0.99 | 28 | 13 | 4 | proposed |
| Dämon | Demon | 0.98 | 23 | 18 | 10 | proposed |
| Dual-Kernel-Theorie | Dual-Kernel Theory | 0.83 | 22 | 19 | 2 | proposed |
| Epistemologie | epistemology | 0.96 | 35 | 6 | 3 | proposed |
| Interferenz | Interference | 0.92 | 35 | 6 | 3 | proposed |
| Loci | Orte | 0.98 | 4 | 37 | 3 | stated in 1 doc(s) ^[lokalitaeten-konzept-fuer-roman-simulation.md:L211] |
| Realitätsebene | Reality Level | 0.97 | 38 | 3 | 3 | proposed |
| Topologie | Topology | 0.93 | 35 | 6 | 3 | proposed |
| Aristoteles | Aristotle | 0.98 | 30 | 10 | 9 | proposed |
| Komplexes Trauma | Complex Trauma | 0.93 | 9 | 31 | 8 | proposed |
| Gitter | lattice | 0.97 | 32 | 8 | 4 | proposed |
| I-Perspektive | Main Character | 0.96 | 1 | 39 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L78] |
| Umkehrung | Inversion | 1.00 | 16 | 24 | 4 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse.md:L98]; proposed |
| Personifikation der Leere | Void | 0.95 | 1 | 39 | 1 | stated in 1 doc(s) ^[tattoo-konzept-symbolik-trauma-heilung.md:L225] |
| Semantik | Semantics | 0.96 | 34 | 6 | 5 | proposed |
| Semantik | semantics | 0.94 | 34 | 6 | 4 | proposed |
| Zersplitterung | Shattering | 1.00 | 33 | 7 | 1 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L364] |
| Übergänge | Transitions | 0.92 | 33 | 7 | 3 | proposed |
| Autopoiese | autopoiesis | 0.92 | 4 | 35 | 2 | proposed |
| Komputational | Computational | 0.93 | 1 | 38 | 0 | proposed |
| Fehlausgerichtete | Misaligned | 1.00 | 15 | 24 | 3 | proposed |
| Hypervigilanz | Hypervigilance | 0.99 | 33 | 6 | 3 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L366]; proposed |
| Programm | program | 0.82 | 28 | 11 | 0 | proposed |
| Schwebezustand | Superposition | 0.98 | 1 | 38 | 1 | stated in 1 doc(s) ^[charakter-kompilation-fuer-kohaerenz-protokoll.md:L214] |
| Stringtheorie | string theory | 0.99 | 29 | 10 | 7 | proposed |
| Algorithmische Melancholie | Algorithmic Melancholy | 0.86 | 25 | 13 | 2 | proposed |
| Glaube | Belief | 0.88 | 23 | 15 | 1 | proposed |
| Wärmetod | Big Freeze | 1.00 | 24 | 14 | 7 | stated in 1 doc(s) ^[roman-konzept-dualitaet-kohaerenz-spannung.md:L107] |
| Exklusion | Exclusion | 0.91 | 23 | 15 | 1 | proposed |
| Kohärenztheorie | coherence theory | 0.99 | 35 | 3 | 2 | proposed |
| Simulationshypothese | Simulation hypothesis | 0.95 | 18 | 20 | 11 | proposed |
| Systemarchitektur | system architecture | 0.99 | 35 | 3 | 0 | proposed |
| Toleranz | tolerance | 0.95 | 30 | 8 | 2 | proposed |
| Kapazität | Capacity | 0.94 | 31 | 6 | 1 | proposed |
| Kohärenztheorie | Coherence theory | 0.98 | 35 | 2 | 2 | proposed |
| Tiefpunkt | Death | 0.81 | 12 | 25 | 1 | stated in 1 doc(s) ^[argus-chronist-der-wandlung.md:L75] |
| Grauen | Dread | 0.98 | 22 | 15 | 8 | stated in 4 doc(s) ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L87] ^[genesis-mehrstufige-recherche-und-ausformulierung.md:L79] |
| Lähmung | Freeze-Response | 0.96 | 30 | 7 | 2 | stated in 1 doc(s) ^[gutachten-grad-der-behinderung-bei-dis.md:L261] |
| Gärtner | Gardener | 0.97 | 22 | 15 | 6 | proposed |
| Handlungsstrang | Throughline | 1.00 | 4 | 33 | 1 | stated in 1 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L27] |
| Handlungsstränge | Throughlines | 0.94 | 9 | 28 | 4 | stated in 1 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L33] |
| Konsens | consensus | 0.94 | 26 | 11 | 5 | proposed |
| Korrespondenztheorie | correspondence theory | 0.99 | 33 | 4 | 2 | proposed |
| Lokalität | locality | 0.97 | 28 | 9 | 1 | proposed |
| Reduktionismus | Reductionism | 0.92 | 31 | 6 | 4 | proposed |
| STRUKTURELLE DISSOZIATION | structural dissociation | 0.97 | 3 | 34 | 0 | proposed |
| Zweite | Second | 0.98 | 10 | 27 | 5 | proposed |
| Weltbild | Worldview | 0.97 | 30 | 7 | 1 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L48] |
| Fehlausgerichtete Kohärenz | Alignment Problem | 0.98 | 15 | 21 | 11 | stated in 2 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L384] ^[ki-rolle-aegis-genesis-fragestellungen.md:L361] |
| Analytiker | Analyst | 0.90 | 20 | 16 | 3 | proposed |
| Dialektik | Dialectic | 0.97 | 25 | 11 | 4 | proposed |
| Hartes Problem | Hard Problem | 0.99 | 2 | 34 | 1 | proposed |
| Homöostase | homeostasis | 1.00 | 33 | 3 | 2 | proposed |
| Systemzustand | Population | 0.91 | 32 | 4 | 1 | stated in 1 doc(s) ^[ki-narrative-kollaps-kohaerenz-paradoxie.md:L31] |
| Realismus | Realism | 0.82 | 25 | 11 | 4 | proposed |
| Sektor | Sector | 0.93 | 35 | 1 | 0 | proposed |
| Sektor | sector | 0.92 | 35 | 1 | 0 | proposed |
| Vektoren | vectors | 0.90 | 28 | 8 | 0 | proposed |
| Barriere | barrier | 0.82 | 29 | 6 | 0 | proposed |
| Cache Kohärenz | Cache Coherence | 0.99 | 24 | 11 | 0 | proposed |
| Korrespondenztheorie | Correspondence theory | 0.88 | 33 | 2 | 2 | proposed |
| Determinismus | determinism | 0.93 | 27 | 8 | 3 | proposed |
| Dissoziative Störungen | Dissociative Disorders | 0.99 | 11 | 24 | 7 | proposed |
| Prinzip der Explosion | Ex Contradictione Quodlibet | 1.00 | 25 | 10 | 6 | stated in 3 doc(s) ^[ki-narrative-kollaps-kohaerenz-paradoxie.md:L131] ^[kohaerenz-protokoll-hard-sf-horror-thriller.md:L115] |
| Funke | Spark | 0.85 | 33 | 2 | 0 | proposed |
| Gnosis | Quelle der Einsicht | 0.95 | 32 | 3 | 3 | stated in 1 doc(s) ^[kohaerenz-protokoll-forschungsaufgabe.md:L264] |
| schwieriges Problem | Hard Problem | 0.98 | 1 | 34 | 0 | proposed |
| Heldenreise | Hero's journey | 0.99 | 33 | 2 | 2 | proposed |
| Interner Konflikt | internal conflict | 0.94 | 9 | 26 | 0 | proposed |
| Isomorphie | isomorphism | 0.83 | 25 | 10 | 0 | proposed |
| Kleine | Little | 0.80 | 31 | 4 | 1 | proposed |
| Kollektiv | collective | 0.83 | 10 | 25 | 0 | proposed |
| Schwerkraft | gravity | 0.91 | 15 | 20 | 2 | proposed |
| Selbstregulation | self-regulation | 0.96 | 31 | 4 | 0 | proposed |
| Tertiär | Tertiary | 0.98 | 2 | 33 | 1 | proposed |
| Verkörperte | embodied | 0.89 | 5 | 30 | 0 | proposed |
| Sekundär TSDP-ANP | Apparently Normal Part | 0.80 | 3 | 31 | 3 | stated in 3 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik.md:L50] ^[kael-charakterarchitektur-und-konfliktdynamik-2.md:L50] |
| Attraktoren | Attractors | 0.92 | 26 | 8 | 5 | proposed |
| Begrenzungsfläche | Boundary | 0.99 | 4 | 30 | 1 | stated in 1 doc(s) ^[integriertes-kohaerenz-protokoll-erstellung.md:L230] |
| Beklemmung | Dread | 1.00 | 19 | 15 | 3 | stated in 2 doc(s) ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L303] ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L339] |
| Beobachterin | observer | 0.86 | 6 | 28 | 1 | proposed |
| Dual-Kernel-Theorie (DKT) | Dual Kernel Theory (DKT) | 0.89 | 14 | 20 | 1 | proposed |
| Umgebungs-Storytelling | Environmental Storytelling | 0.98 | 1 | 33 | 0 | proposed |
| Umwelt-Erzählung | Environmental Storytelling | 1.00 | 1 | 33 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-thematische-tiefenanalyse.md:L239] |
| Externe Ebene | external level | 0.98 | 33 | 1 | 0 | proposed |
| Feedbackschleifen | feedback loops | 0.99 | 27 | 7 | 0 | proposed |
| Gitter | Lattices | 0.94 | 32 | 2 | 2 | stated in 1 doc(s) ^[parakonsistente-logik-im-seelen-protokoll.md:L53]; proposed |
| Schwerkraft | Gravity | 0.97 | 15 | 19 | 1 | proposed |
| Heldenreise | hero's journey | 0.98 | 33 | 1 | 0 | proposed |
| Kohärenztheorie der Wahrheit | coherence theory of truth | 1.00 | 31 | 3 | 2 | proposed |
| Vermittler | Mediator | 0.99 | 21 | 13 | 3 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L113]; proposed |
| Realitätsebenen | Reality Layers | 0.99 | 33 | 1 | 0 | proposed |
| Selbstbezug | self-reference | 0.91 | 22 | 12 | 4 | proposed |
| Trennungsprotokoll | Separation Protocol | 1.00 | 23 | 11 | 9 | stated in 4 doc(s) ^[kohaerenz-protokoll-architecture-synthesis.md:L188] ^[risikoanalysebericht-eine-systematische-bewertung-der-bedroh.md:L85]; proposed |
| Simulationshypothese | Simulation_hypothesis | 0.85 | 18 | 16 | 9 | proposed |
| Tragisch | Tragic | 0.99 | 3 | 31 | 0 | proposed |
| Zerbrochene | broken | 0.92 | 5 | 29 | 0 | proposed |
| Anscheinend Normalen Teil | Apparently Normal Part | 1.00 | 2 | 31 | 0 | proposed |
| Anscheinend Normaler Teil | Apparently Normal Part | 1.00 | 2 | 31 | 0 | proposed |
| Befehl | Command | 0.91 | 28 | 5 | 1 | proposed |
| Belastungsstörung | stress disorder | 0.86 | 26 | 7 | 4 | proposed |
| Blockaden | Cognitive Firewall | 0.89 | 19 | 14 | 1 | stated in 1 doc(s) ^[recherche-ueberwelt.md:L125] |
| Schöpfer | Creator | 0.85 | 31 | 2 | 0 | proposed |
| Exekutive | Executive | 0.96 | 13 | 20 | 0 | proposed |
| Exilanten | Exiles | 1.00 | 9 | 24 | 4 | stated in 2 doc(s) ^[optimierter-prompt-fuer-kohaerenz-protokoll.md:L212] ^[kernwelten-fuer-kohaerenz-protokoll.md:L177]; proposed |
| Fraktale | Fractals | 0.82 | 24 | 9 | 3 | proposed |
| Gefrorene | Oblivion | 0.93 | 2 | 31 | 1 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L393] |
| Ungleichgewicht | Inequity | 0.99 | 19 | 14 | 6 | stated in 2 doc(s) ^[coherence-critique-and-question-generation.md:L86] ^[narrative-context-protocol-ncp-spezifikation.md:L56] |
| Zittern | Jitter | 0.95 | 26 | 7 | 1 | proposed |
| Monster-Gruppe | Monster group | 0.98 | 7 | 26 | 4 | proposed |
| Polyphonie | Polyphonic | 0.95 | 18 | 15 | 4 | proposed |
| Programm | Program | 0.90 | 28 | 5 | 0 | proposed |
| Rückkopplungsschleifen | feedback loops | 0.90 | 26 | 7 | 1 | proposed |
| Systemischer Kollaps | systemic collapse | 0.94 | 6 | 27 | 0 | proposed |
| Unvollständigkeitssätzen | incompleteness theorems | 0.99 | 12 | 21 | 4 | proposed |
| Zeuge | witness | 0.86 | 21 | 12 | 5 | proposed |
| Abfolge | Narrative Field | 0.92 | 31 | 1 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L299] |
| Metamorphose | Becoming | 1.00 | 12 | 20 | 4 | stated in 1 doc(s) ^[kohaerenz-protokoll-duale-dramatica-storyform-synthese.md:L143] |
| Benefizienz | Fürsorge | 0.92 | 4 | 28 | 2 | stated in 1 doc(s) ^[dis-diagnose-klinische-ethische-rechtliche-analyse.md:L174] ^[dis-diagnose-klinische-ethische-rechtliche-analyse.md:L177] |
| Bewusst | Conscious | 0.81 | 8 | 24 | 0 | proposed |
| Kanon | Canon | 0.84 | 12 | 20 | 6 | proposed |
| Kohärenz-Kern | Coherence Kernel | 0.80 | 5 | 27 | 2 | proposed |
| Dialetheische | Dialetheic | 0.92 | 5 | 27 | 0 | proposed |
| Echtzeit | Real-time | 0.95 | 22 | 10 | 1 | proposed |
| Steigerung | Escalation | 0.80 | 22 | 10 | 0 | proposed |
| Hamartia | Tragic Flaw | 1.00 | 20 | 12 | 4 | stated in 2 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L317] ^[ki-rolle-aegis-genesis-fragestellungen.md:L298] |
| Hybris | Übermut | 0.98 | 27 | 5 | 5 | stated in 2 doc(s) ^[aegis-paradoxon-neukonzeption-und-analyse-docx.md:L38] ^[aegis-paradoxon-konzeption-und-analyse.md:L55] |
| Insel | island | 0.89 | 26 | 6 | 0 | proposed |
| Komplexitätstheorie | complexity theory | 0.98 | 28 | 4 | 3 | proposed |
| Künstlicher Intelligenz | artificial intelligence | 0.96 | 8 | 24 | 1 | proposed |
| Lügner | Liar | 0.85 | 27 | 5 | 5 | proposed |
| Offenbarung | Midpoint | 0.84 | 24 | 8 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-plot-entwicklung-und-wahrheitsdualitaet.md:L206] |
| Zustand der Amnesie | Oblivion | 0.91 | 1 | 31 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-projekt-rekonstruktion.md:L259] |
| Resonanz-Landschaft | Resonance Landscape | 0.98 | 23 | 9 | 0 | proposed |
| Zimmer | Room | 0.87 | 13 | 19 | 5 | proposed |
| Selbstbezug | Self-Reference | 1.00 | 22 | 10 | 6 | stated in 1 doc(s) ^[monstergruppen-und-paradoxien-im-narrativ.md:L84] |
| Selbstreferenz | self-reference | 0.99 | 20 | 12 | 4 | proposed |
| Stringtheorie | String theory | 0.95 | 29 | 3 | 3 | proposed |
| Abgrund | Rock Bottom | 1.00 | 29 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-prozess-grundlagen.md:L102] |
| Barriere | Barrier | 0.94 | 29 | 2 | 0 | proposed |
| Volumen | Bulk | 0.82 | 18 | 13 | 6 | proposed |
| Cache Kohärenz | cache coherence | 0.98 | 24 | 7 | 0 | proposed |
| Fürsorger | Caregiver | 1.00 | 11 | 20 | 3 | proposed |
| Kanal | Channel | 0.84 | 27 | 4 | 0 | proposed |
| Komplexitätstheorie | Complexity theory | 0.99 | 28 | 3 | 2 | proposed |
| Determinismus | Determinism | 0.96 | 27 | 4 | 1 | proposed |
| Feedbackschleifen | Feedback loops | 0.84 | 27 | 4 | 3 | proposed |
| Gödels Unvollständigkeit | Gödel's incompleteness | 0.98 | 10 | 21 | 1 | proposed |
| schwieriges Problem des Bewusstseins | Hard Problem of Consciousness | 0.99 | 1 | 30 | 0 | proposed |
| Helfer | Helper | 0.83 | 12 | 19 | 0 | proposed |
| Kollision | collision | 0.93 | 23 | 8 | 0 | proposed |
| Künstlichen Intelligenz | artificial intelligence | 0.84 | 7 | 24 | 1 | proposed |
| Negentropie | Negentropy | 1.00 | 27 | 4 | 4 | proposed |
| Story Limit | Optionlock | 0.89 | 13 | 18 | 11 | stated in 1 doc(s) ^[kohaerenz-protokoll-architecture-synthesis.md:L149] |
| Verfolger | Persecutor | 1.00 | 13 | 18 | 4 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L291]; proposed |
| Polyphonie | Polyphony | 0.98 | 18 | 13 | 5 | proposed |
| Prozessphilosophie | Process Philosophy | 1.00 | 18 | 13 | 8 | proposed |
| Stufen | Stages | 0.84 | 20 | 11 | 2 | proposed |
| Allianz | Alliance | 0.98 | 22 | 8 | 5 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L370]; proposed |
| Einstellung | Attitude | 0.97 | 8 | 22 | 4 | proposed |
| Berührung | Contact | 0.89 | 23 | 7 | 0 | proposed |
| Korrektiv | Corrective | 0.96 | 10 | 20 | 0 | proposed |
| Dialetheisch | Dialetheic | 0.87 | 3 | 27 | 0 | proposed |
| Durchgangslinien | Throughlines | 1.00 | 2 | 28 | 2 | proposed |
| Ex Contradictione Quodlibet | Principle of Explosion | 0.99 | 10 | 20 | 3 | stated in 2 doc(s) ^[deconstructing-reality-s-architecture.md:L55] ^[aegis-manifest-genesis-krise-reboot-2.md:L51] |
| Kind-Anteil | Exile | 0.81 | 12 | 18 | 1 | stated in 1 doc(s) ^[dissoziative-identitaet-sinnsuche-im-trauma.md:L142] ^[dissoziative-identitaet-sinnsuche-im-trauma.md:L198] |
| Rückkopplungsschleifen | Feedback loops | 0.98 | 26 | 4 | 2 | proposed |
| Glaube | faith | 0.98 | 23 | 7 | 0 | proposed |
| Großes Argument | Grand Argument | 0.96 | 2 | 28 | 2 | proposed |
| Ignoranz | ignorance | 0.96 | 25 | 5 | 0 | proposed |
| Kosmischer Horror | cosmic horror | 1.00 | 21 | 9 | 2 | proposed |
| Sprachmodelle | Language Models | 0.92 | 8 | 22 | 3 | proposed |
| Negentropie | negentropy | 0.98 | 27 | 3 | 3 | proposed |
| Rekursion | recursion | 0.98 | 23 | 7 | 2 | proposed |
| zweiter Ordnung | Second-Order | 0.98 | 20 | 10 | 2 | proposed |
| Ignoranz | Agnotology | 0.83 | 25 | 4 | 3 | stated in 3 doc(s) ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L441] ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L502] |
| Berechenbarkeit | computability | 0.97 | 28 | 1 | 1 | proposed |
| Klassische Logik | Classical Logic | 0.99 | 11 | 18 | 3 | proposed |
| Ko-Bewusstsein | Co-Consciousness | 0.92 | 23 | 6 | 2 | stated in 1 doc(s) ^[2-kohaerenz-protokoll-konzeptentwicklung.md:L118] |
| Ko-Bewusstsein | Co-consciousness | 1.00 | 23 | 6 | 2 | stated in 1 doc(s) ^[the-minds-behind-the-machine-a-psychological-guide-to-system.md:L50]; proposed |
| Kern der Kohärenz | Coherence Kernel | 0.86 | 2 | 27 | 0 | proposed |
| Durchgehenden Handlungslinien | Throughlines | 1.00 | 1 | 28 | 1 | stated in 1 doc(s) ^[storyforms-system-mind-bewusstsein.md:L41] |
| Durchlinien | Throughlines | 1.00 | 1 | 28 | 1 | stated in 1 doc(s) ^[dual-kernel-erzaehlarchitektur-bewusstsein-symmetrie-ourobor.md:L84] |
| Emotionaler Teil | Emotional Part | 1.00 | 1 | 28 | 0 | proposed |
| Entität AEGIS | entity AEGIS | 0.94 | 28 | 1 | 0 | proposed |
| Existenzialismus | Existentialism | 0.94 | 10 | 19 | 5 | proposed |
| Rückkopplung | Feedback-Loop | 0.93 | 22 | 7 | 2 | proposed |
| Flackern | Z-Fighting | 0.92 | 22 | 7 | 2 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L274] |
| Vergessen | Forgetting | 0.93 | 21 | 8 | 3 | proposed |
| Gruppentheorie | group theory | 0.99 | 21 | 8 | 6 | proposed |
| Integrierte Informationstheorie | Integrated Information Theory | 0.99 | 6 | 23 | 2 | proposed |
| Isomorphie | Isomorphism | 0.95 | 25 | 4 | 0 | proposed |
| Klassische | classic | 0.86 | 19 | 10 | 0 | proposed |
| Meta-Ebene | Meta-level | 0.90 | 27 | 2 | 0 | proposed |
| Story Mind | Narrative System | 0.98 | 27 | 2 | 1 | stated in 1 doc(s) ^[refining-dramatica-storyform-for-kohaerenz-protokoll.md:L21] |
| Quarantäne | quarantine | 0.96 | 17 | 12 | 0 | proposed |
| Umdeutung | Reframing | 0.88 | 13 | 16 | 2 | stated in 1 doc(s) ^[ki-narrative-kollaps-kohaerenz-paradoxie.md:L91] |
| Ruf | Reputation | 0.84 | 26 | 3 | 0 | proposed |
| Vier Durchgangslinien | Throughlines | 0.98 | 1 | 28 | 1 | stated in 1 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L25] |
| Vermittler | mediator | 0.98 | 21 | 8 | 1 | proposed |
| Wärmetod | heat death | 0.98 | 24 | 5 | 0 | proposed |
| Ehrfurcht | Awe | 0.98 | 20 | 8 | 5 | stated in 2 doc(s) ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L87] ^[genesis-mehrstufige-recherche-und-ausformulierung.md:L79]; proposed |
| Cache Kohärenz | Cache coherence | 1.00 | 24 | 4 | 0 | proposed |
| Kohärenzkern | Coherence Kernel | 0.93 | 1 | 27 | 0 | proposed |
| Der Kollaps | The Collapse | 0.83 | 11 | 17 | 0 | proposed |
| Unglaube | Disbelief | 1.00 | 9 | 19 | 4 | stated in 3 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L239] ^[dramatica-storyform-validierung-und-synthese.md:L109] |
| Dramatica-Treiber | Driver | 0.95 | 1 | 27 | 1 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-verortung.md:L169] |
| Feedback-Schleife | feedback loop | 0.99 | 13 | 15 | 0 | proposed |
| Fenster | Window | 0.89 | 22 | 6 | 2 | proposed |
| Halteproblem | Halting Problem | 1.00 | 18 | 10 | 2 | proposed |
| Wärmetod | Heat Death | 1.00 | 24 | 4 | 4 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L21]; proposed |
| Hybris | Hubris | 0.99 | 27 | 1 | 1 | proposed |
| Hybris | hubris | 0.92 | 27 | 1 | 1 | proposed |
| Isomorphie | Strukturgleichheit | 0.90 | 25 | 3 | 3 | stated in 1 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L17] |
| Kognitive Dissonanz | cognitive dissonance | 0.97 | 11 | 17 | 1 | proposed |
| Prinzip der Explosion | Principle of explosion | 0.97 | 25 | 3 | 2 | proposed |
| Quantengravitation | Quantum Gravity | 0.87 | 19 | 9 | 6 | proposed |
| Rekursion | Recursion | 0.97 | 23 | 5 | 4 | proposed |
| Sekundärer | secondary | 0.89 | 11 | 17 | 1 | proposed |
| Selbstbezug | Self-reference | 0.90 | 22 | 6 | 3 | proposed |
| Unzuverlässigkeit | Unreliability | 0.97 | 26 | 2 | 0 | proposed |
| Missbrauch | Abuse | 0.90 | 22 | 5 | 3 | proposed |
| Death | Aridity | 0.89 | 25 | 2 | 1 | stated in 1 doc(s) ^[argus-chronist-der-wandlung.md:L75] |
| Autopoietisch | Autopoietic | 0.92 | 3 | 24 | 2 | proposed |
| Beeinflussung | Passive Influence | 0.98 | 25 | 2 | 1 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L102] |
| Beobachterin | Observer | 0.93 | 6 | 21 | 1 | proposed |
| Beziehungsgeschichte | Relationship Story | 1.00 | 3 | 24 | 2 | proposed |
| Dialektik | Dialectics | 0.93 | 25 | 2 | 2 | proposed |
| Dual Kernel Theorie | Dual-Kernel Theory | 0.87 | 8 | 19 | 1 | proposed |
| Exil | Exile | 0.96 | 9 | 18 | 5 | proposed |
| Ignoranz | Ignorance | 0.94 | 25 | 2 | 1 | proposed |
| Ko-Bewusstheit | co-consciousness | 0.99 | 7 | 20 | 0 | proposed |
| Ko-Bewusstseins | co-consciousness | 0.97 | 7 | 20 | 0 | proposed |
| fehlausgerichtet | Misaligned | 0.93 | 3 | 24 | 1 | proposed |
| Zufälligkeit | Randomness | 0.95 | 20 | 7 | 2 | proposed |
| Schiff | Ship | 0.98 | 18 | 9 | 5 | proposed |
| zweiter Ordnung | Second-order | 0.83 | 20 | 7 | 5 | proposed |
| Wechseln | Switching | 0.97 | 8 | 19 | 2 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L664] |
| Wellenfunktion | wave function | 0.93 | 24 | 3 | 0 | proposed |
| Katharsis | Catharsis | 0.99 | 20 | 6 | 5 | proposed |
| Domains | Classes | 0.86 | 11 | 15 | 3 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L124] |
| Distanzierung | Cut-off | 0.94 | 23 | 3 | 2 | stated in 2 doc(s) ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L185] ^[beziehungsheilung-nach-trauma-konzeptpapier-3.md:L191] |
| Dissoziativen Störungen | Dissociative Disorders | 0.91 | 2 | 24 | 2 | proposed |
| Verkörperte | Embodied | 0.88 | 5 | 21 | 1 | proposed |
| Erkenntnistheorie | Epistemology | 0.97 | 14 | 12 | 3 | proposed |
| Prinzip der Explosion | Ex Falso Quodlibet | 1.00 | 25 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-synthese-integration.md:L136] |
| Verbannte | Exiles | 1.00 | 2 | 24 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-thematische-tiefenanalyse.md:L115]; proposed |
| Explosionsprinzip | Principle of Explosion | 1.00 | 6 | 20 | 1 | proposed |
| Gruppentheorie | Group theory | 0.99 | 21 | 5 | 5 | proposed |
| Holographisches | Holographic | 0.95 | 12 | 14 | 4 | proposed |
| Isomorphie | Isomorphy | 0.95 | 25 | 1 | 0 | proposed |
| Kanäle | channels | 0.81 | 18 | 8 | 0 | proposed |
| Konjektur | Vermutung | 0.87 | 3 | 23 | 2 | stated in 2 doc(s) ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L47] ^[holographisches-prinzip-fuer-kohaerenz-protokoll-2.md:L47] |
| Labor | Laboratory | 0.82 | 20 | 6 | 0 | proposed |
| wechselseitige Information | Mutual Information | 0.97 | 3 | 23 | 1 | proposed |
| Retraumatisierung | Retraumatization | 0.97 | 25 | 1 | 1 | proposed |
| Retraumatisierung | retraumatization | 0.99 | 25 | 1 | 1 | proposed |
| Schiff | ship | 1.00 | 18 | 8 | 4 | proposed |
| Selbstproduktion | self-production | 0.80 | 25 | 1 | 0 | proposed |
| Selbstreferenz | Self-reference | 0.98 | 20 | 6 | 5 | proposed |
| Storyformen | Storyforms | 0.86 | 5 | 21 | 2 | proposed |
| transzendent | Transcendent | 0.97 | 14 | 12 | 0 | proposed |
| Trauma und Dissoziation | Trauma and Dissociation | 0.99 | 16 | 10 | 4 | proposed |
| Wahrheitstheorien | theories of truth | 0.95 | 15 | 11 | 0 | proposed |
| Zufälligkeit | randomness | 0.92 | 20 | 6 | 0 | proposed |
| Absenz | absence | 0.92 | 10 | 15 | 0 | proposed |
| Agentschaft | agency | 0.96 | 2 | 23 | 0 | proposed |
| Anziehungspunkt | Attractor | 0.80 | 1 | 24 | 0 | proposed |
| Architekten | Architects | 0.83 | 21 | 4 | 0 | proposed |
| Einwand | Objection | 0.92 | 12 | 13 | 4 | proposed |
| Existentialismus | Existentialism | 0.98 | 6 | 19 | 5 | proposed |
| Inversion | Gegen-Position | 0.94 | 24 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L820] |
| Wärmetod | Heat death | 0.96 | 24 | 1 | 1 | proposed |
| Helferin | Helper | 0.96 | 6 | 19 | 3 | proposed |
| Heuristik | Heuristic | 0.97 | 21 | 4 | 1 | proposed |
| Heuristik | heuristic | 0.99 | 21 | 4 | 0 | proposed |
| Maxwellscher Dämon | Maxwell's Demon | 1.00 | 12 | 13 | 3 | proposed |
| Mikrokosmos | microcosm | 0.99 | 16 | 9 | 0 | proposed |
| Spiegelung | Mirroring | 0.98 | 18 | 7 | 0 | proposed |
| Mit-Bewusstsein | co-consciousness | 0.98 | 5 | 20 | 5 | proposed |
| Nichtlokalität | Nonlocality | 0.99 | 19 | 6 | 6 | proposed |
| Psychotraumatologie | Psychotraumatology | 0.96 | 18 | 7 | 2 | proposed |
| Schwierige | difficult | 0.90 | 5 | 20 | 0 | proposed |
| Systemkohärenz | system coherence | 0.91 | 24 | 1 | 0 | proposed |
| Unheimlichkeit | Uncanny | 1.00 | 3 | 22 | 2 | stated in 1 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L422] |
| Wertausrichtung | Value Alignment | 0.99 | 6 | 19 | 6 | stated in 2 doc(s) ^[kohaerenz-protokoll-themenanalyse-und-anreicheru.md:L225] ^[aegis-singularitaet-jenseits-entropiegleichung-2.md:L47]; proposed |
| Achsen | Axes | 0.97 | 18 | 6 | 2 | proposed |
| Arithmetik | Arithmetic | 1.00 | 23 | 1 | 1 | proposed |
| Bibel | Bible | 0.89 | 5 | 19 | 2 | proposed |
| Schmetterlingseffekt | Butterfly effect | 0.96 | 19 | 5 | 5 | proposed |
| Fürsorger | Caretaker | 0.99 | 11 | 13 | 2 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L225] ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L473] |
| Dient der Erdung | Grounding | 0.97 | 1 | 23 | 1 | stated in 1 doc(s) ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L165] |
| Tun | Doing | 0.96 | 10 | 14 | 3 | proposed |
| EPs Exilanten | Exiles | 1.00 | 0 | 24 | 0 | stated in 1 doc(s) ^[ki-antagonist-fragmentierte-gottheit-analyse.md:L86] |
| Erdungstechniken | Grounding | 0.81 | 1 | 23 | 1 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L126] |
| Etablierung Somatischer Erdung | Grounding | 0.97 | 1 | 23 | 1 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L124] |
| Exilant | Exile | 0.94 | 6 | 18 | 4 | stated in 1 doc(s) ^[optimierter-prompt-fuer-kohaerenz-protokoll.md:L110]; proposed |
| Katharsis | catharsis | 1.00 | 20 | 4 | 3 | proposed |
| Kontrollsystem | control system | 0.93 | 22 | 2 | 0 | proposed |
| Korrespondenztheorie der Wahrheit | correspondence theory of truth | 0.99 | 22 | 2 | 0 | proposed |
| Mutuelle Information | Mutual Information | 0.98 | 1 | 23 | 1 | stated in 1 doc(s) ^[dramatica-storyform-kohaerenz-protokoll-analyse.md:L46] |
| Nichtlokalität | nonlocality | 0.99 | 19 | 5 | 5 | proposed |
| Philosophie des Geistes | philosophy of mind | 0.96 | 23 | 1 | 0 | proposed |
| Posttraumatische Belastungsstörung | Posttraumatic Stress Disorder | 0.97 | 15 | 9 | 3 | proposed |
| Protektoren | Protectors | 0.87 | 12 | 12 | 3 | proposed |
| Selbstdefinition | self-definition | 0.98 | 23 | 1 | 0 | proposed |
| Simulierte Realität | simulated reality | 1.00 | 1 | 23 | 0 | proposed |
| Somatisch | Somatic | 0.91 | 1 | 23 | 0 | proposed |
| Wechsels | Switch | 0.94 | 8 | 16 | 2 | stated in 1 doc(s) ^[projektplanung-fuer-kohaerenz-protokoll.md:L113] |
| Weltenbau | World Building | 1.00 | 19 | 5 | 2 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L583] |
| Artefakt | Artifact | 0.86 | 16 | 7 | 3 | proposed |
| Künstliche Intelligenz | Artificial intelligence | 0.98 | 19 | 4 | 0 | proposed |
| Autopoietisches System | autopoietic system | 0.96 | 7 | 16 | 0 | proposed |
| Behälter | Container | 0.94 | 8 | 15 | 0 | proposed |
| Beständigkeit | Steadfast | 1.00 | 9 | 14 | 2 | stated in 1 doc(s) ^[duale-storyform-synthese-kohaerenz-protokoll.md:L56] |
| Betreuer | Caregiver | 0.97 | 3 | 20 | 0 | proposed |
| blinder Fleck | Blind Spot | 0.97 | 13 | 10 | 1 | proposed |
| Fürsorgerin | Caregiver | 0.94 | 3 | 20 | 3 | stated in 3 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik.md:L340] ^[kael-charakterarchitektur-und-konfliktdynamik-2.md:L340] |
| Kollaps-Kern | Collapse Kernel | 0.86 | 4 | 19 | 1 | proposed |
| Kontrollsystem | Control System | 0.84 | 22 | 1 | 1 | proposed |
| Kosmischer Horror | Cosmic horror | 0.97 | 21 | 2 | 0 | proposed |
| Theorie der Verkörperung | Embodiment | 0.99 | 5 | 18 | 5 | stated in 5 doc(s) ^[aegis-genesis-krise-konzeptioneller-rahmen.md:L315] ^[aegis-genesis-krise-konzeptioneller-rahmen.md:L582] |
| Existenzialismus | existentialism | 0.94 | 10 | 13 | 4 | proposed |
| Fixierte Einstellung | Fixed Attitude | 0.98 | 2 | 21 | 1 | proposed |
| Friedens | peace | 0.85 | 11 | 12 | 0 | proposed |
| Halteproblem | Halting problem | 0.91 | 18 | 5 | 1 | proposed |
| IFS-Modell | IFS model | 0.90 | 21 | 2 | 0 | proposed |
| Inferenz | Inference | 0.90 | 9 | 14 | 3 | proposed |
| Juna/V-Verbindung | Juna/V connection | 0.92 | 16 | 7 | 1 | proposed |
| Kristall | crystal | 0.92 | 14 | 9 | 0 | proposed |
| Paare | Pairs | 0.94 | 16 | 7 | 5 | proposed |
| Quantenphysik | quantum physics | 0.91 | 16 | 7 | 0 | proposed |
| Quellcode | source code | 0.98 | 16 | 7 | 0 | proposed |
| Sektoren | sectors | 0.95 | 22 | 1 | 0 | proposed |
| Simulationshypothese | simulation hypothesis | 0.90 | 18 | 5 | 4 | proposed |
| strukturelle Kopplung | Structural Coupling | 0.81 | 21 | 2 | 1 | proposed |
| Strukturelle Dissoziation der Persönlichkeit | structural dissociation of the personality | 0.96 | 9 | 14 | 1 | proposed |
| Tal | Valley | 0.81 | 6 | 17 | 2 | proposed |
| Unbekanntes | Unknown | 0.96 | 16 | 7 | 1 | proposed |
| Puffer | Buffer | 0.98 | 13 | 9 | 2 | proposed |
| Einflusscharakter | Influence Character | 0.92 | 2 | 20 | 2 | stated in 1 doc(s) ^[narrative-modelle-und-dramatica-erweiterung.md:L48] |
| Einfrieren | Freeze Response | 1.00 | 13 | 9 | 1 | stated in 1 doc(s) ^[uberarbeitete-liste-der-anteile-von-kael-tsdp-basiert.md:L60] ^[uberarbeitete-liste-der-anteile-von-kael-tsdp-basiert.md:L102] |
| Exekutive | executive | 0.97 | 13 | 9 | 1 | proposed |
| Externen Ebene | external level | 0.99 | 21 | 1 | 0 | proposed |
| Feedbackschleife | feedback loop | 0.98 | 7 | 15 | 0 | proposed |
| Große Sprachmodelle | Large Language Models | 0.95 | 1 | 21 | 0 | proposed |
| Hacken | Hacking | 0.98 | 7 | 15 | 2 | proposed |
| Holismus | Holism | 0.99 | 18 | 4 | 2 | proposed |
| Intentionalität | intentionality | 0.98 | 19 | 3 | 3 | proposed |
| ungültig | Invalid | 0.87 | 14 | 8 | 4 | proposed |
| Kohärenzprotokoll | coherence protocol | 0.86 | 16 | 6 | 1 | proposed |
| Komplexes Trauma | complex trauma | 0.97 | 9 | 13 | 1 | proposed |
| Kriegsführung | Warfare | 0.91 | 16 | 6 | 1 | proposed |
| Persönlichkeitsstörung | personality disorder | 0.87 | 15 | 7 | 2 | proposed |
| Quantengravitation | quantum gravity | 0.97 | 19 | 3 | 3 | proposed |
| sekundär | Secondary | 0.95 | 12 | 10 | 1 | proposed |
| Somatischer | somatic | 0.82 | 6 | 16 | 0 | proposed |
| Unterwerfung | Total Submission | 0.92 | 20 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L70] |
| Trajektorie | trajectory | 0.96 | 13 | 9 | 0 | proposed |
| Unzuverlässiger Erzähler | Unreliable Narrator | 1.00 | 8 | 14 | 5 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L70]; proposed |
| unzuverlässiger Erzähler | Unreliable Narrator | 0.95 | 8 | 14 | 1 | proposed |
| KI-Ethik | AI ethics | 0.95 | 17 | 4 | 1 | proposed |
| Verlassenwerden | Abandonment Anxiety | 0.99 | 20 | 1 | 1 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L79] |
| Archetyp des Fürsorgers | Caregiver | 0.99 | 1 | 20 | 1 | stated in 1 doc(s) ^[tattoo-konzept-symbolik-trauma-heilung.md:L247] |
| Beides | Both | 0.97 | 8 | 13 | 0 | proposed |
| Beobachtereffekt | Observer effect | 0.99 | 17 | 4 | 4 | proposed |
| Membran | Brane | 1.00 | 17 | 4 | 2 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L58] |
| Raumvolumen | Bulk | 0.94 | 8 | 13 | 4 | stated in 1 doc(s) ^[integriertes-kohaerenz-protokoll-erstellung.md:L230] |
| Rifts | Cracks | 0.95 | 11 | 10 | 1 | stated in 1 doc(s) ^[the-coherence-protocol-a-worldbuilding-bible.md:L112] ^[the-coherence-protocol-a-worldbuilding-bible.md:L203] |
| Dual Kernel Theorie (DKT) | Dual Kernel Theory (DKT) | 1.00 | 1 | 20 | 0 | proposed |
| Vollstrecker | Enforcer | 0.99 | 10 | 11 | 2 | stated in 1 doc(s) ^[aegis-psychologische-kriegsfuehrung-narrative-eskalation.md:L262]; proposed |
| Ereignishorizont | Event horizon | 0.99 | 20 | 1 | 0 | proposed |
| Feedback-Schleife | Feedback Loop | 0.96 | 13 | 8 | 1 | proposed |
| Feedback-Schleifen | Feedback Loops | 0.88 | 5 | 16 | 1 | proposed |
| Schwankungen | Fluctuations | 0.98 | 15 | 6 | 1 | proposed |
| Tragischer Fehler | Hamartia | 0.98 | 1 | 20 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-synthese-integration.md:L70] |
| Harte SF | Hard Science Fiction | 0.86 | 1 | 20 | 1 | proposed |
| Holografisches | Holographic | 0.93 | 7 | 14 | 3 | proposed |
| Holographisches Prinzip | Holographic principle | 1.00 | 12 | 9 | 4 | proposed |
| Informationsparadoxon | information paradox | 0.98 | 12 | 9 | 7 | proposed |
| Intentionalität | Intentionality | 0.98 | 19 | 2 | 2 | proposed |
| Interdependenz | Pratītyasamutpāda | 0.86 | 18 | 3 | 3 | stated in 1 doc(s) ^[narrativ-existenzieller-kohaerenz-nzt-protokoll.md:L248] |
| Kernaxiome | core axioms | 0.94 | 14 | 7 | 0 | proposed |
| Rechenkerne | Kernels | 1.00 | 3 | 18 | 2 | stated in 1 doc(s) ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L29] |
| Kybernetik zweiter Ordnung | Second-order cybernetics | 0.96 | 14 | 7 | 5 | proposed |
| Mitbewusstsein | co-consciousness | 1.00 | 1 | 20 | 0 | proposed |
| Netzwerktheorie | network theory | 0.95 | 19 | 2 | 2 | proposed |
| Operatoren | Operators | 0.95 | 14 | 7 | 0 | proposed |
| Spieler | Player | 0.95 | 13 | 8 | 2 | proposed |
| Posttraumatische Belastungsstörung | Post-Traumatic Stress Disorder | 0.97 | 15 | 6 | 1 | proposed |
| Quarantäne | Quarantine | 0.95 | 17 | 4 | 0 | proposed |
| Schwach | Weak | 0.84 | 11 | 10 | 2 | proposed |
| Selbstbestimmung | self-determination | 0.96 | 19 | 2 | 0 | proposed |
| Selbstbewusstsein | self-consciousness | 0.95 | 17 | 4 | 2 | proposed |
| Zuschauer | Spectator | 0.92 | 9 | 12 | 0 | proposed |
| Tertiäre Strukturelle Dissoziation | tertiary structural dissociation | 0.92 | 20 | 1 | 0 | proposed |
| Verifizierer | Verifier | 1.00 | 6 | 15 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L161]; proposed |
| Zeugenfunktion | Witness Function | 0.98 | 7 | 14 | 6 | stated in 1 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L51]; proposed |
| Aktualität | Energeia | 0.91 | 19 | 1 | 1 | stated in 1 doc(s) ^[rechercheauftrag-die-genesis-von-aegis.md:L29] |
| algorithmische Melancholie | Algorithmic Melancholy | 0.92 | 7 | 13 | 0 | proposed |
| Arbeitsablauf | Workflow | 0.98 | 1 | 19 | 1 | proposed |
| Bedenken der KI-Sicherheit | Value Alignment | 0.97 | 1 | 19 | 1 | stated in 1 doc(s) ^[aegis-paradoxon-neukonzeption-und-analyse-docx.md:L75] |
| Buddhismus | Buddhism | 0.94 | 12 | 8 | 4 | proposed |
| verschränkt | Entangled | 0.97 | 12 | 8 | 1 | proposed |
| Erkenntnistheorie | epistemology | 0.90 | 14 | 6 | 1 | proposed |
| Feedback-Schleife | Feedback-Loop | 0.96 | 13 | 7 | 1 | proposed |
| Fehlausgerichtete | misaligned | 0.96 | 15 | 5 | 0 | proposed |
| Phenomenon of Leakage | Flashback | 0.90 | 1 | 19 | 1 | stated in 1 doc(s) ^[reality-s-isomorphic-architecture-explained.md:L125] |
| Fraktal | Fractal | 0.95 | 4 | 16 | 1 | proposed |
| Holismus | holism | 0.97 | 18 | 2 | 2 | proposed |
| Holographisches Prinzip | Holographic_principle | 1.00 | 12 | 8 | 3 | proposed |
| Klassisch | classic | 0.87 | 10 | 10 | 0 | proposed |
| Limit A | Optionlock | 0.81 | 2 | 18 | 2 | stated in 2 doc(s) ^[dramatica-storyform-synthese-aegis-analyse.md:L92] ^[dramatica-storyform-synthese-aegis-analyse-2.md:L266] |
| Maxwellschen | Maxwell's | 0.88 | 6 | 14 | 2 | proposed |
| Prozess der Protokoll-Erhaltung | Persistence | 0.92 | 1 | 19 | 0 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L95] |
| Phönix-Kollaps | Phoenix Collapse | 0.86 | 10 | 10 | 3 | proposed |
| Voreingenommenheit | Preconception | 0.98 | 15 | 5 | 1 | stated in 1 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L177] |
| Primzahlen | Primes | 0.96 | 15 | 5 | 2 | proposed |
| Quantengravitation | Quantum gravity | 0.98 | 19 | 1 | 0 | proposed |
| Quest | Queste | 0.99 | 18 | 2 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L470] |
| Relationen | Relations | 0.82 | 13 | 7 | 0 | proposed |
| Schwarze Löcher | black holes | 0.98 | 11 | 9 | 1 | proposed |
| Selbstbestimmung | Self-determination | 0.97 | 19 | 1 | 0 | proposed |
| Selbstgefühl | Sense of Self | 0.88 | 13 | 7 | 1 | proposed |
| Versuchung | Temptation | 1.00 | 14 | 6 | 2 | stated in 2 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L245] ^[narrative-context-protocol-ncp-spezifikation.md:L56] |
| KI-System | AI system | 0.95 | 10 | 9 | 0 | proposed |
| Angst und Hilflosigkeit | Dread | 0.90 | 4 | 15 | 2 | stated in 2 doc(s) ^[kosmischer-horror-in-kohaerenz-protokoll.md:L39] ^[kosmischer-horror-in-kohaerenz-protokoll-2.md:L41] |
| Beobachtereffekt | observer effect | 0.97 | 17 | 2 | 1 | proposed |
| Bewusstseinsstrom | Stream of Consciousness | 1.00 | 12 | 7 | 6 | stated in 3 doc(s) ^[kernwelten-und-fragmentierte-wahrnehmung.md:L63] ^[kernwelten-und-fragmentierte-wahrnehmung.md:L293]; proposed |
| Cache-Kohärenz | Cache Coherence | 0.84 | 8 | 11 | 4 | proposed |
| Dichotomie | Dichotomy | 0.95 | 16 | 3 | 0 | proposed |
| Edges | Kanten | 1.00 | 3 | 16 | 3 | stated in 2 doc(s) ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L260] ^[aegis-genesis-krise-prosa-auftrag-formulieren-2.md:L260] |
| Exil | exile | 0.99 | 9 | 10 | 3 | proposed |
| IFS Exilant | Exile | 0.83 | 1 | 18 | 1 | stated in 1 doc(s) ^[ki-antagonist-fragmentierte-gottheit-analyse.md:L117] |
| Existentialismus | existentialism | 0.98 | 6 | 13 | 3 | proposed |
| Fehlausgerichtete Kohärenz | misalignment | 0.89 | 15 | 4 | 0 | proposed |
| Feuerlöscher | Firefighters | 1.00 | 4 | 15 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-thematische-tiefenanalyse.md:L117] |
| Gleichgültigkeit | indifference | 0.98 | 18 | 1 | 0 | proposed |
| Heuristiken | Heuristics | 0.98 | 9 | 10 | 2 | proposed |
| Holographisches | holographic | 0.99 | 12 | 7 | 2 | proposed |
| Informationstheoretische Entropie | Shannon-Entropie | 0.87 | 3 | 16 | 1 | stated in 1 doc(s) ^[system-kael-konzeptentwicklung-und-analyse.md:L75] |
| Instanziierung | instantiation | 0.99 | 6 | 13 | 2 | proposed |
| Kern-Selbst | core self | 0.87 | 17 | 2 | 0 | proposed |
| Kontrollzentrum | control center | 0.95 | 18 | 1 | 0 | proposed |
| Leech-Gitter | Leech-Lattice | 0.96 | 13 | 6 | 1 | proposed |
| Leerstellen | gaps | 0.98 | 11 | 8 | 2 | proposed |
| Materialismus | Materialism | 0.92 | 7 | 12 | 0 | proposed |
| Membran | Membrane | 0.99 | 17 | 2 | 1 | proposed |
| Nichts-Rauschen | Nothing-Noise | 0.81 | 16 | 3 | 1 | stated in 1 doc(s) ^[the-architecture-of-fracture-a-compendium-of-the-kael-system.md:L43]; proposed |
| Operationale Geschlossenheit | Operational Closure | 0.99 | 9 | 10 | 0 | proposed |
| Partitionierung | partitioning | 0.88 | 13 | 6 | 1 | proposed |
| Partizipation | Teilhabe | 0.89 | 6 | 13 | 3 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L17] |
| Pfleger | caregiver | 0.99 | 9 | 10 | 0 | proposed |
| Primärer ANP | primary ANP | 1.00 | 15 | 4 | 1 | proposed |
| Quantenschaum | Quantum foam | 1.00 | 17 | 2 | 2 | proposed |
| Quantenschaum | quantum foam | 0.99 | 17 | 2 | 2 | proposed |
| Rationalisierung | Rationalization | 1.00 | 15 | 4 | 2 | stated in 1 doc(s) ^[ki-antagonist-fragmentierte-gottheit-analyse.md:L102] ^[ki-antagonist-fragmentierte-gottheit-analyse.md:L120]; proposed |
| Rigide Logik | rigid logic | 0.98 | 2 | 17 | 0 | proposed |
| Simulationstheorie | Simulation theory | 0.99 | 18 | 1 | 0 | proposed |
| Soziale Systeme | Social Systems | 0.99 | 6 | 13 | 4 | proposed |
| Unterbewusstsein | Subconscious | 1.00 | 10 | 9 | 2 | stated in 1 doc(s) ^[coherence-critique-and-question-generation.md:L86]; proposed |
| Zeitverlust | Time-loss | 0.87 | 18 | 1 | 0 | proposed |
| Wachsende | growing | 0.92 | 9 | 10 | 0 | proposed |
| Zahlentheorie | number theory | 0.97 | 17 | 2 | 0 | proposed |
| Anweisung | DIRECTIVE | 0.86 | 12 | 6 | 1 | proposed |
| Borderline-Persönlichkeitsstörung | borderline personality disorder | 0.95 | 12 | 6 | 1 | proposed |
| Chaos Theorie | Chaos Theory | 0.89 | 4 | 14 | 2 | proposed |
| Kristall | Crystal | 0.94 | 14 | 4 | 0 | proposed |
| Depersonalisierung | depersonalization | 0.99 | 8 | 10 | 0 | proposed |
| Exilanten | exiles | 0.81 | 9 | 9 | 4 | proposed |
| Feuerbekämpfer | Firefighter | 1.00 | 3 | 15 | 0 | proposed |
| Feuerbekämpfer | Firefighters | 0.80 | 3 | 15 | 2 | stated in 1 doc(s) ^[kernwelten-fuer-kohaerenz-protokoll.md:L179] |
| Feuerwehrmann | Firefighter | 0.99 | 3 | 15 | 1 | stated in 1 doc(s) ^[optimierter-prompt-fuer-kohaerenz-protokoll.md:L112]; proposed |
| Kämpfer | Fighter | 0.96 | 11 | 7 | 1 | proposed |
| Leerstellen | Gaps | 0.99 | 11 | 7 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-architecture-synthesis-2.md:L191]; proposed |
| Heuristik der Integration | Heuristics of Integration | 0.99 | 10 | 8 | 3 | proposed |
| holografisch | Holographic | 0.91 | 4 | 14 | 1 | proposed |
| Internes System | internal system | 0.90 | 1 | 17 | 0 | proposed |
| K-J Verbindung | K-J connection | 0.99 | 17 | 1 | 0 | proposed |
| KLASSIFIZIERT | classified | 0.80 | 1 | 17 | 0 | proposed |
| Korrektiv | corrective | 0.93 | 10 | 8 | 1 | proposed |
| Maschinelles Lernen | Machine Learning | 0.98 | 4 | 14 | 0 | proposed |
| Mitte | Middle | 0.84 | 12 | 6 | 1 | proposed |
| Monster-Gruppe | monster group | 0.89 | 7 | 11 | 1 | proposed |
| Operationale Schließung | Operational Closure | 1.00 | 8 | 10 | 2 | stated in 1 doc(s) ^[textanalyse-existenz-system-und-leid.md:L94]; proposed |
| Operative Geschlossenheit | Operational Closure | 0.93 | 8 | 10 | 1 | proposed |
| Persönlichkeitszustände | personality states | 1.00 | 17 | 1 | 0 | proposed |
| Pflegender | caregiver | 0.99 | 8 | 10 | 1 | proposed |
| Protokoll-Ontologie | Protocol Ontology | 1.00 | 5 | 13 | 0 | proposed |
| Schwarzen Lochs | black holes | 0.97 | 9 | 9 | 2 | proposed |
| Shannon-Entropie | Shannon entropy | 1.00 | 16 | 2 | 1 | proposed |
| Storyformen | storyforms | 0.92 | 5 | 13 | 1 | proposed |
| Subquotienten | Subquotients | 0.91 | 17 | 1 | 1 | proposed |
| Symmetriegruppe | symmetry group | 0.97 | 15 | 3 | 2 | proposed |
| Wertausrichtungsproblem | Value Alignment Problem | 1.00 | 2 | 16 | 2 | stated in 1 doc(s) ^[aegis-genesis-krise-konzeptioneller-rahmen.md:L116] |
| Werteausrichtungsproblem | Value Alignment Problem | 1.00 | 2 | 16 | 2 | stated in 2 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L178] ^[ki-rolle-aegis-genesis-fragestellungen.md:L131] |
| Verordnung | regulation | 0.86 | 9 | 9 | 0 | proposed |
| Verteidiger | defender | 0.93 | 14 | 4 | 0 | proposed |
| Vertex-Operator-Algebren | Vertex Operator Algebras | 0.86 | 13 | 5 | 2 | proposed |
| Wurmlöcher | Wormholes | 0.97 | 8 | 10 | 1 | proposed |
| Zeitdilatation | time dilation | 0.98 | 15 | 3 | 2 | proposed |
| Zeitpfeil | time arrow | 0.96 | 16 | 2 | 0 | proposed |
| Absurde | absurd | 0.81 | 8 | 9 | 1 | proposed |
| Lebensgeschichte | Biography | 0.96 | 13 | 4 | 0 | proposed |
| Blinder Fleck | Blind Spot | 1.00 | 7 | 10 | 1 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L50]; proposed |
| Komplexe Posttraumatische Belastungsstörung | Complex PTSD | 0.93 | 6 | 11 | 1 | proposed |
| Konstruktivismus | Constructivism | 0.91 | 14 | 3 | 2 | proposed |
| Gegenpol | Counterpoint | 0.84 | 14 | 3 | 1 | stated in 1 doc(s) ^[dramatica-und-kohaerenz-protokoll-analyse.md:L67] |
| Depersonalisierung | Depersonalization | 0.96 | 8 | 9 | 0 | proposed |
| Die Ontologie | ONTOLOGY | 0.90 | 12 | 5 | 0 | proposed |
| Diskurs | Discourse | 0.81 | 12 | 5 | 1 | proposed |
| Entlastung | Unburdening | 0.89 | 5 | 12 | 2 | proposed |
| Entropie-Management | entropy management | 0.99 | 16 | 1 | 0 | proposed |
| Erster Kontakt | First Contact | 1.00 | 12 | 5 | 4 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L456] |
| Fehlausrichtung der Werte | Value Alignment Problem | 0.99 | 1 | 16 | 1 | stated in 1 doc(s) ^[aegis.md:L51] |
| Feuerwehrmänner | Firefighters | 1.00 | 2 | 15 | 1 | stated in 1 doc(s) ^[optimierter-prompt-fuer-kohaerenz-protokoll.md:L214]; proposed |
| Fundamentale Gesetze | fundamental laws | 0.92 | 2 | 15 | 0 | proposed |
| Instanziierung | Instantiation | 0.93 | 6 | 11 | 2 | proposed |
| Invalidierung | Invalidation | 0.99 | 12 | 5 | 4 | proposed |
| Juna-Verbindung | Juna connection | 0.92 | 15 | 2 | 0 | proposed |
| Kind-Anteile | Littles | 0.83 | 14 | 3 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-forschungsaufgabe.md:L123] |
| Kybernetik zweiter Ordnung | second-order cybernetics | 0.80 | 14 | 3 | 1 | proposed |
| Leech-Gitter | Leech lattice | 0.99 | 13 | 4 | 2 | proposed |
| Sperre | Lock | 1.00 | 2 | 15 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L190]; proposed |
| Sinnstiftung | Meaning-making | 0.95 | 16 | 1 | 0 | proposed |
| Mikrokosmos | Microcosm | 0.99 | 16 | 1 | 0 | proposed |
| Neu-Rahmung | Reframing | 1.00 | 1 | 16 | 1 | stated in 1 doc(s) ^[dissoziative-identitaet-sinnsuche-im-trauma.md:L75] |
| Phasenraum | phase space | 0.95 | 16 | 1 | 0 | proposed |
| Planck-Skala | Planck scale | 1.00 | 13 | 4 | 3 | proposed |
| Posttraumatische Belastungsstörung | Post-traumatic stress disorder | 0.99 | 15 | 2 | 1 | proposed |
| pragmatisch | Pragmatic | 0.90 | 12 | 5 | 1 | proposed |
| Problem der Wertausrichtung | Value Alignment Problem | 0.99 | 1 | 16 | 1 | proposed |
| reversibel | Reversible | 0.85 | 2 | 15 | 1 | proposed |
| umkehrbar | Reversible | 0.88 | 2 | 15 | 1 | proposed |
| Sekundär | Secondary | 0.88 | 7 | 10 | 0 | proposed |
| Sinnstiftung | meaning-making | 0.88 | 16 | 1 | 0 | proposed |
| Stürme | Storms | 0.80 | 16 | 1 | 0 | proposed |
| Stürme | storms | 0.91 | 16 | 1 | 0 | proposed |
| Theologie | Theology | 0.86 | 5 | 12 | 3 | proposed |
| Torwächter | gatekeeper | 0.94 | 10 | 7 | 1 | proposed |
| Unentscheidbarkeit | Undecidability | 0.90 | 16 | 1 | 1 | proposed |
| Unentscheidbarkeit | undecidability | 0.95 | 16 | 1 | 1 | proposed |
| Wahrheitstheorie | theory of truth | 0.87 | 10 | 7 | 3 | proposed |
| Abruf | Retrieval | 0.97 | 5 | 11 | 0 | proposed |
| Archivar | Archivist | 0.82 | 14 | 2 | 0 | proposed |
| Atmosphäre der Furcht | Dread | 1.00 | 1 | 15 | 1 | stated in 1 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L113] ^[genesis-recherche-anleitung-umsetzung.md:L1134] |
| Attraktors | Attractors | 0.81 | 8 | 8 | 5 | proposed |
| Bewusstseinsstrom | Stream-of-Consciousness | 0.93 | 12 | 4 | 4 | stated in 3 doc(s) ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L61] ^[genesis-mehrstufige-recherche-und-ausformulierung.md:L59]; proposed |
| Co-Bewusstsein | Co-Consciousness | 0.87 | 10 | 6 | 2 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L177]; proposed |
| Co-Bewusstsein | Co-consciousness | 0.91 | 10 | 6 | 0 | proposed |
| Kontrolleur | Controller | 0.81 | 11 | 5 | 1 | proposed |
| Kernwelt 1 | Core World 1 | 1.00 | 13 | 3 | 0 | proposed |
| Rat | Council | 0.98 | 10 | 6 | 0 | proposed |
| Denkweise | Way of Thinking | 0.98 | 14 | 2 | 0 | proposed |
| diskursiv | Discursive | 0.80 | 1 | 15 | 0 | proposed |
| emergente Eigenschaften | Emergent Properties | 0.99 | 10 | 6 | 1 | proposed |
| Exilant | exile | 0.91 | 6 | 10 | 2 | proposed |
| externe Ebene | External Level | 0.97 | 7 | 9 | 0 | proposed |
| Fehlausrichtung | Misalignment | 0.85 | 13 | 3 | 0 | proposed |
| Feldtheorien | field theories | 0.82 | 13 | 3 | 1 | proposed |
| Fluidität | Fluidity | 0.83 | 15 | 1 | 0 | proposed |
| Gelb | Yellow | 1.00 | 11 | 5 | 2 | proposed |
| Holografisches Prinzip | Holographic principle | 1.00 | 7 | 9 | 3 | proposed |
| Hürde | Obstacle | 0.84 | 11 | 5 | 0 | proposed |
| Idealismus | Idealism | 0.87 | 13 | 3 | 3 | proposed |
| Informationserhaltung | Information conservation | 0.96 | 15 | 1 | 0 | proposed |
| Injektion | Injection | 0.96 | 10 | 6 | 0 | proposed |
| interne Verarbeitung | Internal Processing | 0.98 | 14 | 2 | 0 | proposed |
| Kind-Anteil | Little | 1.00 | 12 | 4 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-forschungsaufgabe.md:L137] |
| Varietät | Law of Requisite Variety | 0.89 | 6 | 10 | 4 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptionelle-ausarbeitung.md:L253] |
| Modularität | Modularity | 0.95 | 12 | 4 | 1 | proposed |
| Modulen | Modules | 0.81 | 9 | 7 | 1 | proposed |
| Phasenübergang | phase transition | 0.98 | 13 | 3 | 0 | proposed |
| Primärer ANP | Primary ANP | 0.97 | 15 | 1 | 0 | proposed |
| Psychoanalyse | Psychoanalysis | 0.96 | 8 | 8 | 1 | proposed |
| Vier Dimensionen | Quad | 0.88 | 1 | 15 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-dramatica-synthese-masterkonzept.md:L69] |
| Relativität | relativity | 0.91 | 8 | 8 | 0 | proposed |
| Schiff des Theseus | Ship of Theseus | 1.00 | 8 | 8 | 2 | proposed |
| standhaft | Steadfast | 0.99 | 2 | 14 | 2 | proposed |
| Zero-Trust Execution Model | Total Skepticism | 0.90 | 15 | 1 | 1 | stated in 1 doc(s) ^[the-architecture-of-a-misguided-god-a-biography-of-aegis.md:L39] |
| tragischer Fehler | Tragic Flaw | 0.91 | 4 | 12 | 0 | proposed |
| Trivialisierung | Trivialization | 0.94 | 15 | 1 | 0 | proposed |
| Wahrheits-Rotation | Truth-Rotation | 0.99 | 4 | 12 | 4 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse-2.md:L31] |
| Vagheit | vague | 0.85 | 11 | 5 | 0 | proposed |
| Varietät | Variety | 1.00 | 6 | 10 | 4 | proposed |
| Verfolger | persecutor | 0.98 | 13 | 3 | 1 | proposed |
| Weltanschauung | Worldview | 0.91 | 9 | 7 | 0 | proposed |
| Zeuge-Funktion | Witness Function | 0.90 | 2 | 14 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-synthese.md:L91] |
| Amygdala | Mandelkern | 0.91 | 14 | 1 | 1 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L37] |
| Ashbys Gesetz | Ashby's Law | 0.96 | 5 | 10 | 2 | proposed |
| Grundannahmen | Assumption-Decay | 0.96 | 14 | 1 | 1 | stated in 1 doc(s) ^[ki-prompt-analyse-hard-problem-of-consciousness.md:L297] |
| Belastungen | Burdens | 0.89 | 8 | 7 | 0 | proposed |
| Bewusstseinsstrom | Stream of consciousness | 0.97 | 12 | 3 | 3 | proposed |
| Lasten | Burdens | 1.00 | 8 | 7 | 5 | proposed |
| Cache-Kohärenz | cache coherence | 0.99 | 8 | 7 | 2 | proposed |
| Käfig | Cage | 0.81 | 9 | 6 | 1 | proposed |
| Kognitive Dissonanz | Cognitive dissonance | 1.00 | 11 | 4 | 2 | proposed |
| Datenpakete | data packets | 0.94 | 13 | 2 | 0 | proposed |
| Erledigen | Doing | 0.80 | 1 | 14 | 0 | proposed |
| Einklammerung | Epoché | 1.00 | 5 | 10 | 5 | stated in 1 doc(s) ^[kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md.md:L154] |
| Witness Function | Erhalt der Zeugenfunktion | 0.96 | 14 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L49] |
| Erster Kontakt | first contact | 0.83 | 12 | 3 | 0 | proposed |
| Funktionalismus | Functionalism | 0.93 | 12 | 3 | 3 | proposed |
| Generative KI | Generative AI | 0.98 | 2 | 13 | 0 | proposed |
| Grundannahmen | Priors | 0.97 | 14 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-duale-dramatica-storyform-synthese.md:L25] |
| Holografisch | Holographic | 0.93 | 1 | 14 | 0 | proposed |
| Holographisches Prinzip | holographic principle | 0.99 | 12 | 3 | 2 | proposed |
| Idealismus | idealism | 0.89 | 13 | 2 | 2 | proposed |
| Immunsystem | immune system | 0.93 | 10 | 5 | 1 | proposed |
| Informationsphysik | information physics | 0.97 | 11 | 4 | 0 | proposed |
| Interferenzmuster | interference pattern | 0.98 | 10 | 5 | 2 | proposed |
| innerer Zustand | Internal State | 0.98 | 12 | 3 | 0 | proposed |
| Invarianz | Invariance | 0.99 | 10 | 5 | 2 | proposed |
| Kerndirektive | core directive | 0.83 | 11 | 4 | 0 | proposed |
| Kerntrauma | core trauma | 0.94 | 13 | 2 | 0 | proposed |
| Klassischer | classic | 0.93 | 5 | 10 | 0 | proposed |
| Konstruktivismus | constructivism | 0.87 | 14 | 1 | 1 | proposed |
| Kontextfenster | context window | 1.00 | 8 | 7 | 1 | proposed |
| Logisches System | logical system | 0.97 | 3 | 12 | 0 | proposed |
| Modularität | modularity | 0.99 | 12 | 3 | 1 | proposed |
| Narratologie | Narratology | 0.80 | 13 | 2 | 0 | proposed |
| Nervensystem | nervous system | 0.99 | 13 | 2 | 1 | proposed |
| Nicht-Lokalität | Non-Locality | 0.89 | 11 | 4 | 0 | proposed |
| Nihilismus | nihilism | 0.93 | 9 | 6 | 1 | proposed |
| Orakel | Oracle | 0.93 | 13 | 2 | 1 | proposed |
| Panpsychismus | Panpsychism | 0.93 | 10 | 5 | 4 | proposed |
| Phasenübergang | Phase transition | 0.93 | 13 | 2 | 1 | proposed |
| Vierergruppen | Quads | 0.93 | 2 | 13 | 1 | stated in 1 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L42] |
| Russells Paradoxon | Russell's paradox | 0.96 | 9 | 6 | 3 | proposed |
| Selbstverifikation | self-verification | 0.83 | 9 | 6 | 0 | proposed |
| Solipsismus | solipsism | 1.00 | 13 | 2 | 1 | proposed |
| Tastendruck | Story Driver | 0.93 | 1 | 14 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L100] |
| Symbiose | Symbiosis | 0.98 | 14 | 1 | 0 | proposed |
| Vermittlerin | mediator | 0.85 | 7 | 8 | 0 | proposed |
| Vertex-Operator-Algebren | vertex operator algebras | 0.86 | 13 | 2 | 2 | proposed |
| Vollstrecker | enforcer | 1.00 | 10 | 5 | 0 | proposed |
| ANP und EP | ANP and EP | 0.99 | 10 | 4 | 0 | proposed |
| Aktionssysteme | action systems | 0.98 | 8 | 6 | 0 | proposed |
| Autarkie | autarky | 0.98 | 11 | 3 | 0 | proposed |
| Automorphismengruppe | Automorphism group | 0.89 | 13 | 1 | 1 | proposed |
| Beanstandung | Objection | 0.89 | 1 | 13 | 0 | proposed |
| Bekenstein-Schranke | Bekenstein bound | 0.98 | 10 | 4 | 2 | proposed |
| Bewusstseinsstrom | stream of consciousness | 0.94 | 12 | 2 | 0 | proposed |
| Kompression | Compression | 0.99 | 11 | 3 | 1 | proposed |
| Konditionierung | Conditioning | 0.91 | 9 | 5 | 5 | proposed |
| Kontrolltheorie | Control Theory | 0.98 | 7 | 7 | 2 | proposed |
| Verzögerung | Delay | 0.84 | 10 | 4 | 1 | proposed |
| Diskursive Logik | Discursive Logic | 1.00 | 3 | 11 | 0 | proposed |
| Drei-Akt-Struktur | Three-Act Structure | 1.00 | 12 | 2 | 0 | proposed |
| zerbrechlich | Fragile | 0.85 | 4 | 10 | 1 | proposed |
| Freie Energie | Free Energy | 0.95 | 1 | 13 | 1 | proposed |
| Friedens | Peace | 0.93 | 11 | 3 | 1 | proposed |
| Garten der Möglichkeiten | Garden of Possibilities | 1.00 | 8 | 6 | 0 | proposed |
| glückliche Familie | Happy Family | 0.84 | 1 | 13 | 1 | proposed |
| Holografisches | holographic | 0.92 | 7 | 7 | 2 | proposed |
| Hologramm | hologram | 0.99 | 10 | 4 | 3 | proposed |
| Unendlich | Infinite | 0.83 | 2 | 12 | 0 | proposed |
| Informationsparadoxon | Information paradox | 1.00 | 12 | 2 | 2 | proposed |
| Introjekt | Introject | 0.89 | 8 | 6 | 2 | proposed |
| Kaels Internes System | Kael's internal system | 1.00 | 1 | 13 | 0 | proposed |
| Kategorienfehler | category error | 0.98 | 9 | 5 | 0 | proposed |
| Kernaxiom | core axiom | 0.96 | 6 | 8 | 0 | proposed |
| Konditionierung | conditioning | 0.99 | 9 | 5 | 1 | proposed |
| Käfig | cage | 0.87 | 9 | 5 | 0 | proposed |
| Lügner-Paradox | Liar paradox | 1.00 | 12 | 2 | 2 | proposed |
| Lügner-Paradoxon | Liar paradox | 0.94 | 12 | 2 | 0 | proposed |
| Nichtlineare | Nonlinear | 0.99 | 6 | 8 | 3 | proposed |
| Ontologien | Ontologies | 0.93 | 10 | 4 | 0 | proposed |
| Partitionierung | Partitioning | 0.97 | 13 | 1 | 0 | proposed |
| Pragmatismus | pragmatism | 0.98 | 11 | 3 | 1 | proposed |
| Quanten-Nichtlokalität | Quantum nonlocality | 0.93 | 12 | 2 | 2 | proposed |
| Quanten-Nichtlokalität | quantum nonlocality | 0.98 | 12 | 2 | 2 | proposed |
| Quantenfeldtheorie | quantum field theory | 1.00 | 13 | 1 | 0 | proposed |
| Quantenkohärenz | quantum coherence | 0.98 | 8 | 6 | 2 | proposed |
| Raum-Zeit | Spacetime | 0.97 | 6 | 8 | 0 | proposed |
| Reinszenierung | Re-enactment | 1.00 | 13 | 1 | 1 | stated in 1 doc(s) ^[aegis-genesis-krise-konzeptioneller-rahmen.md:L59] |
| Tiefpunkt | Rock Bottom | 0.96 | 12 | 2 | 2 | proposed |
| Samen der Sicherheit | Unburdening | 0.93 | 2 | 12 | 1 | stated in 1 doc(s) ^[kael-s-dissociative-architecture-analysis.md:L156] |
| Selbst-Referenz | self-reference | 0.85 | 2 | 12 | 0 | proposed |
| Selbstzustände | self-states | 0.88 | 8 | 6 | 0 | proposed |
| Solipsismus | Solipsism | 0.94 | 13 | 1 | 1 | proposed |
| sporadisch | Sporadic | 0.96 | 5 | 9 | 4 | proposed |
| Stratege | Strategist | 0.93 | 11 | 3 | 0 | proposed |
| Strukturelle Dissoziation der Persönlichkeit | Structural Dissociation of Personality | 0.98 | 9 | 5 | 0 | proposed |
| Symmetriebrechung | symmetry breaking | 0.99 | 12 | 2 | 2 | proposed |
| Systemprotokolle | system protocols | 0.97 | 12 | 2 | 0 | proposed |
| Trajektorie | Trajectory | 0.95 | 13 | 1 | 0 | proposed |
| transformativ | Transformative | 0.83 | 9 | 5 | 0 | proposed |
| Unbewusst | unconscious | 0.97 | 6 | 8 | 0 | proposed |
| Vertex-Operator-Algebra | vertex operator algebra | 0.87 | 13 | 1 | 0 | proposed |
| Verzeichnis | directory | 0.97 | 6 | 8 | 1 | proposed |
| Rat | Advice | 0.81 | 10 | 3 | 0 | proposed |
| Aktionssystem | action system | 1.00 | 9 | 4 | 0 | proposed |
| Alben | Albums | 0.80 | 4 | 9 | 2 | proposed |
| Unwissenheit | Avidya | 0.96 | 11 | 2 | 1 | stated in 1 doc(s) ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L97] ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L187] |
| Informationsparadoxon Schwarzer Löcher | Black hole information paradox | 1.00 | 7 | 6 | 3 | proposed |
| Borderline-Persönlichkeitsstörung | Borderline personality disorder | 0.94 | 12 | 1 | 1 | proposed |
| Bruchpunkt | breaking point | 1.00 | 8 | 5 | 2 | proposed |
| Ko-Bewusstheit | Co-Consciousness | 0.92 | 7 | 6 | 1 | stated in 1 doc(s) ^[kael-uberarbeitung-des-konzepts-unter-tsdp.md:L33] |
| Ko-Bewusstheit | Co-consciousness | 0.86 | 7 | 6 | 0 | proposed |
| Ko-Bewusstseins | Co-consciousness | 0.89 | 7 | 6 | 0 | proposed |
| kognitive Verzerrungen | Cognitive Biases | 0.92 | 7 | 6 | 3 | proposed |
| Kontrollsysteme | Control Systems | 0.94 | 11 | 2 | 1 | proposed |
| Digitale Physik | Digital physics | 0.97 | 10 | 3 | 3 | proposed |
| Verzeichnis | Directory | 0.98 | 6 | 7 | 1 | proposed |
| Einwand der Isolation | Isolation Objection | 1.00 | 3 | 10 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-synthese-integration.md:L122] |
| Energie-Entladung | Unburdening | 0.94 | 1 | 12 | 1 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L273] |
| Folgerung | Entailment | 1.00 | 5 | 8 | 2 | stated in 1 doc(s) ^[parakonsistente-logik-fuer-kohaerenz-protokoll.md:L74]; proposed |
| Existenzielle Angst | existential anxiety | 0.99 | 8 | 5 | 0 | proposed |
| Gesetz der erforderlichen Vielfalt | Law of Requisite Variety | 1.00 | 3 | 10 | 3 | proposed |
| Globaler Arbeitsbereich | Global Workspace | 1.00 | 3 | 10 | 2 | proposed |
| Hologramm | Hologram | 0.84 | 10 | 3 | 3 | proposed |
| Identitätskrise | Identity Crisis | 1.00 | 10 | 3 | 2 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L225]; proposed |
| Unwissenheit | Ignorance | 0.89 | 11 | 2 | 1 | proposed |
| Induktion | Induction | 0.82 | 9 | 4 | 1 | proposed |
| Trägheit | Inertia | 1.00 | 10 | 3 | 2 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse-2.md:L87] ^[dramatica-storyform-synthese-aegis-analyse-2.md:L93]; proposed |
| Intersubjektivität | Intersubjectivity | 0.94 | 10 | 3 | 2 | proposed |
| Invarianz | invariance | 0.99 | 10 | 3 | 1 | proposed |
| Irreversibilität | Irreversibility | 0.93 | 10 | 3 | 1 | proposed |
| Kern-Trauma | core trauma | 0.97 | 11 | 2 | 0 | proposed |
| Kintsugi der Erinnerung | Narrative Integration | 0.88 | 1 | 12 | 1 | stated in 1 doc(s) ^[heilung-hirnchemie-kunst-trauma.md:L205] |
| Kognitionswissenschaft | cognitive science | 0.90 | 10 | 3 | 0 | proposed |
| Kompression | compression | 0.98 | 11 | 2 | 0 | proposed |
| Konjektur | conjecture | 1.00 | 3 | 10 | 0 | proposed |
| Kämpfer | Warrior | 0.88 | 11 | 2 | 1 | proposed |
| Lügner-Paradox | liar paradox | 0.99 | 12 | 1 | 0 | proposed |
| Lügner-Paradoxon | liar paradox | 0.98 | 12 | 1 | 1 | proposed |
| Mondschein | MOONSHINE | 0.99 | 8 | 5 | 2 | proposed |
| Managern | managers | 0.81 | 7 | 6 | 3 | proposed |
| Metamorphose | Metamorphosis | 0.95 | 12 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L527]; proposed |
| Minimales Selbst | Minimal self | 0.99 | 10 | 3 | 2 | proposed |
| Multiversum | Multiverse | 0.99 | 7 | 6 | 2 | proposed |
| Multiversum | multiverse | 0.98 | 7 | 6 | 1 | proposed |
| Nicht-lokal | Non-Local | 0.86 | 5 | 8 | 0 | proposed |
| Zettel | Note | 0.88 | 2 | 11 | 1 | proposed |
| Nullpunkt | Zero Point | 0.90 | 11 | 2 | 0 | proposed |
| partizipatorisch | Participatory | 0.89 | 3 | 10 | 1 | proposed |
| Verfolger | Persecutor-Rolle | 0.87 | 13 | 0 | 0 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L224] |
| Posttraumatischen Belastungsstörung | Post-traumatic stress disorder | 0.85 | 11 | 2 | 1 | proposed |
| Quantenkohärenz | Quantum Coherence | 0.98 | 8 | 5 | 0 | proposed |
| Quantenzustände | quantum states | 0.83 | 8 | 5 | 2 | proposed |
| Reaktivierung | Reactivation | 1.00 | 11 | 2 | 1 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L371]; proposed |
| Relevanzlogik | Relevance Logic | 0.99 | 6 | 7 | 2 | proposed |
| Reversibilität | reversibility | 0.99 | 10 | 3 | 0 | proposed |
| Selbstkorrektur | self-correction | 0.99 | 8 | 5 | 0 | proposed |
| Tertiären Strukturellen Dissoziation | tertiary structural dissociation | 0.81 | 12 | 1 | 0 | proposed |
| Theologie | theology | 0.94 | 5 | 8 | 3 | proposed |
| Tropfen Gefühl | Titration | 0.94 | 1 | 12 | 1 | stated in 1 doc(s) ^[heilung-hirnchemie-kunst-trauma.md:L147] |
| Tragischer Fehler | Tragic Flaw | 1.00 | 1 | 12 | 0 | proposed |
| Transzendent | Transcendent | 0.98 | 1 | 12 | 0 | proposed |
| Traumatheorie | trauma theory | 0.99 | 11 | 2 | 0 | proposed |
| Urknall | big bang | 0.96 | 12 | 1 | 1 | proposed |
| Verhinderung des Nicht-Seins | prevention of non-being | 0.96 | 9 | 4 | 0 | proposed |
| Zeugenfunktion | Witness-Function | 0.90 | 7 | 6 | 1 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-protokoll.md:L44] |
| Wurmloch | wormhole | 1.00 | 6 | 7 | 3 | proposed |
| Zombie-System | zombie system | 0.92 | 5 | 8 | 1 | proposed |
| Nicht-Dualität | Advaita | 0.80 | 6 | 6 | 4 | stated in 2 doc(s) ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L187] ^[narrativ-existenzieller-kohaerenz-nzt-protokoll.md:L72] |
| Akt der Beobachtung | act of observation | 0.99 | 11 | 1 | 0 | proposed |
| Alltagsmanager | Daily Life Managers | 0.91 | 10 | 2 | 0 | proposed |
| Appeasement | Submit | 0.85 | 1 | 11 | 1 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L53] |
| Künstlicher Intelligenz | Artificial intelligence | 0.93 | 8 | 4 | 0 | proposed |
| Bekenstein-Schranke | Bekenstein Bound | 0.99 | 10 | 2 | 1 | stated in 1 doc(s) ^[hard-sf-roman-outline-dkt-physik-cosmic-horror.md:L29]; proposed |
| Bifurkation | Bifurcation | 0.90 | 9 | 3 | 2 | proposed |
| Brutalismus | Brutalism | 0.88 | 8 | 4 | 4 | proposed |
| Pufferung | Buffering | 0.87 | 4 | 8 | 0 | proposed |
| Cache-Kohärenz | Cache coherence | 0.96 | 8 | 4 | 2 | proposed |
| Pfleger | Carer | 0.81 | 9 | 3 | 0 | proposed |
| Höhle | Cave | 0.89 | 6 | 6 | 2 | proposed |
| Kontrollproblem | Control Problem | 0.97 | 7 | 5 | 5 | proposed |
| Dissoziation und Trauma | Trauma and Dissociation | 0.90 | 2 | 10 | 1 | proposed |
| EP-Intrusionen | EP intrusions | 0.90 | 9 | 3 | 0 | proposed |
| Ökologie | Ecology | 0.92 | 6 | 6 | 0 | proposed |
| Erfordernis | Requisite | 0.99 | 2 | 10 | 0 | proposed |
| Feedback-Schleifen | feedback loops | 0.95 | 5 | 7 | 0 | proposed |
| Riese | Giant | 0.85 | 6 | 6 | 2 | proposed |
| Harmonisierer | Harmonizer | 0.92 | 11 | 1 | 1 | proposed |
| Harmonisierer | harmonizer | 0.93 | 11 | 1 | 0 | proposed |
| Induktion | induction | 0.92 | 9 | 3 | 0 | proposed |
| Instantiierung | Instantiation | 0.96 | 1 | 11 | 1 | proposed |
| interner Zustand | Internal State | 0.92 | 9 | 3 | 1 | proposed |
| Kernaspekt | core aspect | 0.97 | 11 | 1 | 0 | proposed |
| Kollisionen | collisions | 0.87 | 11 | 1 | 0 | proposed |
| Kolmogorov-Komplexität | Kolmogorov complexity | 1.00 | 10 | 2 | 2 | proposed |
| Kritikalität | criticality | 0.98 | 7 | 5 | 3 | proposed |
| Kryptographie | cryptography | 0.98 | 7 | 5 | 2 | proposed |
| Mentorenfigur | Mentor | 0.80 | 1 | 11 | 1 | proposed |
| Messproblem | measurement problem | 0.95 | 10 | 2 | 0 | proposed |
| Minimalismus | Minimalism | 0.86 | 7 | 5 | 3 | proposed |
| Nicht-Lokalität | Non-locality | 0.89 | 11 | 1 | 0 | proposed |
| Nicht-Lokalität | non-locality | 0.89 | 11 | 1 | 0 | proposed |
| Nichtlineare | nonlinear | 0.96 | 6 | 6 | 2 | proposed |
| Nihilismus | Nihilism | 0.87 | 9 | 3 | 1 | proposed |
| Pragmatismus | Pragmatism | 0.96 | 11 | 1 | 1 | proposed |
| Zuflucht | Refuge | 0.94 | 11 | 1 | 0 | proposed |
| Saiten | Strings | 1.00 | 2 | 10 | 1 | stated in 1 doc(s) ^[monstergruppe-kohaerenz-protokoll-fundament.md:L129]; proposed |
| Sekundärer ANP | Secondary ANP | 1.00 | 11 | 1 | 0 | proposed |
| Seelen | souls | 0.84 | 11 | 1 | 0 | proposed |
| Spaghettifizierung | Spaghettification | 0.83 | 7 | 5 | 2 | proposed |
| Stratege | strategist | 0.95 | 11 | 1 | 0 | proposed |
| Strukturelle Kopplung | Structural Coupling | 0.99 | 10 | 2 | 2 | stated in 1 doc(s) ^[aegis-seele-und-entropie.md:L31]; proposed |
| symmetrisch | Symmetric | 0.89 | 9 | 3 | 0 | proposed |
| Säule | pillar | 0.96 | 8 | 4 | 0 | proposed |
| Tautologie | tautology | 0.97 | 6 | 6 | 0 | proposed |
| Tore | gates | 0.81 | 8 | 4 | 0 | proposed |
| Trivialismus | Trivialism | 0.97 | 9 | 3 | 0 | proposed |
| Unbewusst | Unconscious | 0.97 | 6 | 6 | 0 | proposed |
| Unzuverlässiger Erzähler | Unreliable narrator | 0.88 | 8 | 4 | 3 | proposed |
| Vagheit | vagueness | 0.85 | 11 | 1 | 1 | proposed |
| Varietät | variety | 0.80 | 6 | 6 | 3 | proposed |
| Absenz | Absence | 0.84 | 10 | 1 | 0 | proposed |
| Richtigkeit | Accuracy | 0.80 | 9 | 2 | 0 | proposed |
| Adaptive Systeme | adaptive systems | 0.93 | 6 | 5 | 0 | proposed |
| Agentenbasierte | agent-based | 0.98 | 7 | 4 | 3 | proposed |
| Arbeitsgedächtnis | Working Memory | 0.88 | 6 | 5 | 2 | proposed |
| Aufhebung | Sublation | 1.00 | 10 | 1 | 1 | stated in 1 doc(s) ^[aegis-seele-und-entropie.md:L230]; proposed |
| Autopoiesis-Theorie | theory of autopoiesis | 0.99 | 6 | 5 | 0 | proposed |
| Bestätigungsfehler | Confirmation Bias | 1.00 | 3 | 8 | 2 | stated in 1 doc(s) ^[risikoanalysebericht-eine-systematische-bewertung-der-bedroh.md:L46]; proposed |
| Beweiser | Prover | 0.99 | 2 | 9 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L161]; proposed |
| Chinesisches Zimmer | Chinese Room | 0.97 | 7 | 4 | 2 | proposed |
| Zirkularität | Circularity | 0.99 | 10 | 1 | 1 | proposed |
| Kognitive Verzerrungen | Cognitive Biases | 0.96 | 5 | 6 | 2 | proposed |
| Conway-Gruppe | Conway group | 0.96 | 8 | 3 | 2 | proposed |
| Demonstration des Isolationseinwandes | Isolation Objection | 0.99 | 1 | 10 | 1 | stated in 1 doc(s) ^[risikoanalysebericht-eine-systematische-bewertung-der-bedroh.md:L81] |
| Diagonal | Dynamic Pairs | 0.81 | 5 | 6 | 1 | stated in 1 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L58] |
| Dialetheische Logik | Dialetheic Logic | 0.99 | 4 | 7 | 0 | proposed |
| EP-Phobie | EP phobia | 0.87 | 10 | 1 | 0 | proposed |
| EP-Phobien | EP phobias | 0.88 | 8 | 3 | 0 | proposed |
| Sunyata | Emptiness | 0.93 | 3 | 8 | 2 | stated in 1 doc(s) ^[narrative-plot-exploration-existenzielle-kohaerenz.md:L452] |
| Enaktivismus | Enactivism | 1.00 | 8 | 3 | 3 | proposed |
| Enaktivismus | enactivism | 1.00 | 8 | 3 | 3 | proposed |
| Ergosphäre | Ergosphere | 0.97 | 8 | 3 | 0 | proposed |
| Erklärungslücke | Explanatory Gap | 1.00 | 7 | 4 | 1 | proposed |
| Lebenstrieb | Eros | 0.88 | 3 | 8 | 3 | stated in 1 doc(s) ^[narrative-physik-attraktoren-leserbewusstsein.md:L132] |
| Externe Wahrheit | external truth | 0.96 | 1 | 10 | 0 | proposed |
| Freeze-Reaktion | Freeze Response | 0.93 | 2 | 9 | 1 | proposed |
| Gödels Unvollständigkeitssatz | Gödel's incompleteness theorem | 0.89 | 8 | 3 | 0 | proposed |
| Heiler | Healer | 0.97 | 9 | 2 | 0 | proposed |
| Informationsüberflutung | Information overload | 1.00 | 10 | 1 | 0 | proposed |
| Overworld | Instantiation of the Überwelt | 0.95 | 10 | 1 | 1 | stated in 1 doc(s) ^[aegis-manifest-genesis-krise-reboot.md:L53] |
| Integrierte Informationstheorie | Integrated information theory | 1.00 | 6 | 5 | 1 | proposed |
| Integrationspotenzial | Integration Potential | 0.99 | 9 | 2 | 1 | proposed |
| Irreversibilität | irreversibility | 0.98 | 10 | 1 | 0 | proposed |
| Isolations-Einwand | Isolation Objection | 1.00 | 1 | 10 | 0 | proposed |
| Juli | July | 0.84 | 10 | 1 | 0 | proposed |
| KI-Sicherheit | KI Safety | 0.97 | 9 | 2 | 2 | proposed |
| Kampf/Flucht | fight/flight | 0.99 | 7 | 4 | 1 | proposed |
| Landauer-Hitze | Landauer-Heat | 0.93 | 10 | 1 | 0 | proposed |
| Logikfehler | logic error | 0.80 | 10 | 1 | 0 | proposed |
| Messproblem | Measurement problem | 1.00 | 10 | 1 | 1 | proposed |
| Nicht-Euklidische | non-Euclidean | 0.99 | 6 | 5 | 1 | proposed |
| Partizipation | participation | 0.90 | 6 | 5 | 0 | proposed |
| Pflegende | caregiver | 0.99 | 1 | 10 | 0 | proposed |
| Psychologische Kriegsführung | Psychological Warfare | 1.00 | 9 | 2 | 0 | proposed |
| Quanten-Verschränkungs-Witness | Quantum Entanglement Witness | 0.99 | 3 | 8 | 0 | proposed |
| Quantenfluktuationen | quantum fluctuations | 1.00 | 10 | 1 | 1 | proposed |
| Quanteninformation | quantum information | 0.99 | 6 | 5 | 0 | proposed |
| Schutzraum | Refuge | 0.87 | 10 | 1 | 0 | proposed |
| Resonanzlandschaft | Resonance Landscape | 0.82 | 2 | 9 | 0 | proposed |
| Restrukturierung | Restructuring | 0.98 | 6 | 5 | 0 | proposed |
| Reversibilität | Reversibility | 0.94 | 10 | 1 | 0 | proposed |
| Richtigkeit | Rightness | 0.99 | 9 | 2 | 2 | stated in 2 doc(s) ^[kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md.md:L72] ^[wahrheitstheorien-kohaerenz-vs-korrespondenz.md:L326]; proposed |
| Zweiter Ordnung | Second-Order | 0.98 | 1 | 10 | 0 | proposed |
| Seltsame Attraktoren | Strange Attractors | 0.99 | 6 | 5 | 2 | proposed |
| Simulationsumgebungen | simulation environments | 0.95 | 7 | 4 | 0 | proposed |
| Sporadisch | Sporadic | 0.92 | 2 | 9 | 1 | proposed |
| Strukturelle Kopplung | Structural coupling | 0.99 | 10 | 1 | 0 | proposed |
| TSDP-Modell | TSDP framework | 0.80 | 8 | 3 | 0 | proposed |
| TSDP-Modell | TSDP model | 0.98 | 8 | 3 | 0 | proposed |
| topologisch | Topological | 0.95 | 4 | 7 | 1 | proposed |
| Tragischer Fehler | tragic flaw | 0.98 | 1 | 10 | 0 | proposed |
| Trainingsdaten | training data | 0.95 | 10 | 1 | 0 | proposed |
| Weltanschauung | Way of Thinking | 0.92 | 9 | 2 | 0 | proposed |
| Zeugenfunktion | Witness function | 0.95 | 7 | 4 | 1 | proposed |
| Wurmlöcher | wormholes | 0.96 | 8 | 3 | 1 | proposed |
| Zirkularität | circularity | 0.88 | 10 | 1 | 0 | proposed |
| Handlungssysteme | Action Systems | 0.97 | 4 | 6 | 3 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L43]; proposed |
| Aktive Inferenz | Active Inference | 0.96 | 1 | 9 | 0 | proposed |
| AdS/CFT-Korrespondenz | AdS/CFT correspondence | 0.97 | 7 | 3 | 3 | proposed |
| Ein anderer | Another | 0.86 | 5 | 5 | 0 | proposed |
| Bekenstein-Grenze | Bekenstein bound | 0.99 | 6 | 4 | 2 | proposed |
| Benutzeroberfläche | User Interface | 0.95 | 6 | 4 | 1 | proposed |
| Bewahren | PRESERVE | 0.94 | 2 | 8 | 0 | proposed |
| Blinder Fleck | blind spot | 1.00 | 7 | 3 | 0 | proposed |
| Blätter | Leaves | 0.82 | 5 | 5 | 1 | proposed |
| CFT-Korrespondenz | CFT correspondence | 0.95 | 7 | 3 | 3 | proposed |
| Kaskadierendes Versagen | Cascading failure | 1.00 | 4 | 6 | 2 | proposed |
| Komplexes Trauma | Complex trauma | 0.96 | 9 | 1 | 1 | proposed |
| Kontextfenster | Context Window | 0.98 | 8 | 2 | 1 | proposed |
| Kern-Welt 4 | Core World 4 | 1.00 | 5 | 5 | 0 | proposed |
| Korrelaten | Correlates | 0.93 | 3 | 7 | 0 | proposed |
| Kontrapunkt | Counterpoint | 1.00 | 7 | 3 | 1 | stated in 1 doc(s) ^[narrative-context-protocol-ncp-spezifikation.md:L40]; proposed |
| Koppelung | Coupling | 0.99 | 7 | 3 | 0 | proposed |
| Kreuzbestäubung | Cross-Pollination | 0.96 | 1 | 9 | 0 | proposed |
| Kryptographie | Cryptography | 0.96 | 7 | 3 | 1 | proposed |
| Dissipative Strukturen | Dissipative structures | 0.99 | 8 | 2 | 2 | proposed |
| Objektplatzierung | Dressing | 0.95 | 4 | 6 | 2 | stated in 1 doc(s) ^[lokalitaeten-konzept-fuer-roman-simulation.md:L163] |
| Rand des Chaos | Edge of Chaos | 1.00 | 6 | 4 | 2 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L50]; proposed |
| Einfrierens | Freeze Response | 0.94 | 1 | 9 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll.md:L1632] |
| Erklärungslücke | explanatory gap | 0.98 | 7 | 3 | 2 | proposed |
| Exkludierenden Ordnung | exclusionary order | 0.98 | 1 | 9 | 0 | proposed |
| Fehlertoleranz | Fault tolerance | 0.96 | 9 | 1 | 1 | proposed |
| Fehlertoleranz | fault tolerance | 0.99 | 9 | 1 | 1 | proposed |
| Handlungssysteme | action systems | 0.91 | 4 | 6 | 0 | proposed |
| Heiler | healer | 0.98 | 9 | 1 | 0 | proposed |
| Heuristiken | heuristics | 0.98 | 9 | 1 | 1 | proposed |
| Holografisches Prinzip | holographic principle | 1.00 | 7 | 3 | 2 | proposed |
| holographisches Prinzip | Holographic_principle | 0.99 | 2 | 8 | 0 | proposed |
| Homogenität | Homogeneity | 0.86 | 9 | 1 | 0 | proposed |
| Identitätsfragmentierung | Identity Fragmentation | 0.99 | 8 | 2 | 0 | proposed |
| Wachsende | Increasing | 0.86 | 9 | 1 | 0 | proposed |
| Infektion | infection | 0.95 | 7 | 3 | 2 | proposed |
| Interner Konflikt | Internal conflict | 0.98 | 9 | 1 | 0 | proposed |
| Ungültig | Invalid | 0.85 | 2 | 8 | 0 | proposed |
| Kael-Juna-Verbindung | Kael-Juna connection | 0.93 | 8 | 2 | 0 | proposed |
| Kontrollprotokolle | control protocols | 0.91 | 6 | 4 | 0 | proposed |
| Koppelung | coupling | 0.99 | 7 | 3 | 0 | proposed |
| Kunsttherapie | art therapy | 0.98 | 4 | 6 | 4 | proposed |
| Mikroebene | micro-level | 0.84 | 9 | 1 | 0 | proposed |
| Multi-Agenten-Systemen | multi-agent systems | 0.97 | 8 | 2 | 1 | proposed |
| NICHT-EXISTENZ | non-existence | 0.94 | 1 | 9 | 0 | proposed |
| NP-Suche | NP-Search | 0.97 | 2 | 8 | 0 | proposed |
| NP-vollständig | NP-complete | 0.93 | 5 | 5 | 3 | proposed |
| Ontologischer Exploit | Ontological Exploit | 1.00 | 1 | 9 | 0 | proposed |
| Parataxe | Parataxis | 0.95 | 5 | 5 | 1 | proposed |
| Physikalismus | Physicalism | 0.99 | 9 | 1 | 1 | proposed |
| Physikalismus | physicalism | 0.90 | 9 | 1 | 0 | proposed |
| Säule | Pillar | 0.96 | 8 | 2 | 0 | proposed |
| Progressionen | Signposts | 0.85 | 2 | 8 | 1 | stated in 1 doc(s) ^[dramatica-storyform-kohaerenz-protokoll-analyse.md:L137] |
| Quanteninformationstheorie | quantum information theory | 1.00 | 8 | 2 | 0 | proposed |
| Sandkasten | Sandbox | 0.98 | 2 | 8 | 0 | proposed |
| Schizophrenie | schizophrenia | 0.94 | 8 | 2 | 0 | proposed |
| Schwarm | Swarm | 0.99 | 7 | 3 | 1 | proposed |
| Zweite-Ordnung-Kybernetik | Second-order cybernetics | 1.00 | 3 | 7 | 2 | proposed |
| Strukturelle Dissoziation der Persönlichkeit | personality structural dissociation | 0.94 | 9 | 1 | 0 | proposed |
| Strukturelle Dissoziation der Persönlichkeit | structural dissociation of personality | 0.98 | 9 | 1 | 0 | proposed |
| Unzuverlässiger Erzähler | unreliable narrator | 0.98 | 8 | 2 | 0 | proposed |
| Ursprungstrauma | origin trauma | 0.96 | 9 | 1 | 0 | proposed |
| Wurmloch | Wormhole | 1.00 | 6 | 4 | 1 | proposed |
| Zero-Trust-Architektur | Zero Trust Architecture | 0.97 | 4 | 6 | 2 | proposed |
| dissoziative Identitätsstruktur | dissociative identity structure | 0.99 | 9 | 1 | 0 | proposed |
| 5D-Interferenz | 5D interference | 0.91 | 5 | 4 | 1 | proposed |
| AEGIS-Paradoxon | AEGIS Paradox | 0.81 | 7 | 2 | 2 | proposed |
| ANP-EP-Phobien | ANP-EP phobias | 0.81 | 6 | 3 | 0 | proposed |
| Agentenbasierte | Agent-based | 0.89 | 7 | 2 | 2 | proposed |
| Agnotologie | Agnotology | 0.98 | 5 | 4 | 4 | proposed |
| Zeitpfeils | Arrow of time | 0.90 | 8 | 1 | 0 | proposed |
| Grundgestein | Bedrock | 0.96 | 2 | 7 | 2 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-verortung.md:L155] ^[dramatica-storyform-synthese-aegis-verortung.md:L189]; proposed |
| Bestätigungsverzerrung | Confirmation Bias | 0.82 | 1 | 8 | 0 | proposed |
| Buddhistisches Anatta | Nicht-Selbst | 0.84 | 1 | 8 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md.md:L570] |
| Puffern | Buffering | 0.99 | 1 | 8 | 0 | proposed |
| Katatonie | Catatonia | 1.00 | 5 | 4 | 0 | proposed |
| Zelluläre | Cellular | 0.83 | 4 | 5 | 1 | proposed |
| Co-Bewusstseins | Co-consciousness | 0.98 | 3 | 6 | 0 | proposed |
| Komplexe Posttraumatische Belastungsstörung | Complex Post-Traumatic Stress Disorder | 0.97 | 6 | 3 | 0 | proposed |
| Regelungstechnik | Control Theory | 1.00 | 2 | 7 | 2 | stated in 1 doc(s) ^[aegis-genesis-krise-prosa-auftrag-2.md:L315] ^[aegis-genesis-krise-prosa-auftrag-2.md:L462] |
| Kritikalität | Criticality | 0.93 | 7 | 2 | 2 | proposed |
| Dopamin | Dopamine | 0.98 | 6 | 3 | 3 | proposed |
| EPR-Vermutung | EPR conjecture | 0.99 | 5 | 4 | 1 | proposed |
| Einfache Gruppe | simple group | 0.96 | 3 | 6 | 0 | proposed |
| Erinnerung/Emotion | memory and emotion | 0.99 | 6 | 3 | 0 | proposed |
| Erstkontakt | First Contact | 0.80 | 4 | 5 | 1 | proposed |
| Erstprinzipien | First-Principles | 0.98 | 1 | 8 | 0 | proposed |
| Existenzielle Krise | Existential Crisis | 1.00 | 2 | 7 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L155]; proposed |
| Exzision | excision | 0.91 | 6 | 3 | 0 | proposed |
| Feedback-Schleifen | Feedback loops | 0.92 | 5 | 4 | 1 | proposed |
| Freeze-Reaktion | Freeze-Response | 0.95 | 2 | 7 | 1 | proposed |
| Spieltheorie | Game Theory | 0.97 | 6 | 3 | 2 | proposed |
| Gewahrsein | Witnessing | 0.98 | 5 | 4 | 1 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L167] |
| Hafen | Secure Base | 1.00 | 8 | 1 | 1 | stated in 1 doc(s) ^[tattoo-konzept-archetypen-heilung-rebellion.md:L93] |
| Helferin | helper | 0.98 | 6 | 3 | 0 | proposed |
| Informationsparadoxon Schwarzer Löcher | black hole information paradox | 0.99 | 7 | 2 | 1 | proposed |
| Innere Helferin | Inner Self Helper | 1.00 | 3 | 6 | 1 | stated in 1 doc(s) ^[charaktermodellierung-mit-aieos-schema.md:L145] |
| Innerer Selbsthelfer | Internal Self-Helper | 1.00 | 1 | 8 | 1 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L223] |
| Integrierte Information | Integrated information | 0.98 | 4 | 5 | 1 | proposed |
| Integritätswächter | Integrity Guardian | 0.96 | 1 | 8 | 1 | proposed |
| Wächter der Integrität | Integrity Guardian | 0.98 | 1 | 8 | 0 | proposed |
| Internalisierter Täter | Introjekt | 0.89 | 1 | 8 | 1 | stated in 1 doc(s) ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L58] |
| Invarianten | Invariants | 0.93 | 8 | 1 | 1 | proposed |
| Kernselbst | core self | 0.96 | 7 | 2 | 0 | proposed |
| Kernsystem | core system | 0.90 | 7 | 2 | 0 | proposed |
| kinetisch | Kinetic | 0.84 | 4 | 5 | 1 | proposed |
| Wissensbasis | Knowledge Base | 0.81 | 6 | 3 | 0 | proposed |
| Wissensdatenbank | Knowledge Graph | 0.82 | 4 | 5 | 1 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L74] |
| Kohärentismus | coherentism | 0.82 | 8 | 1 | 0 | proposed |
| Kohärenzerhaltung | coherence preservation | 0.95 | 8 | 1 | 0 | proposed |
| Komplexe Adaptive Systeme | complex adaptive systems | 0.99 | 4 | 5 | 0 | proposed |
| Konsole | console | 0.97 | 6 | 3 | 0 | proposed |
| Koordinator | coordinator | 0.97 | 7 | 2 | 0 | proposed |
| Krümmung | curvature | 0.98 | 8 | 1 | 0 | proposed |
| Leckage | leakage | 0.90 | 5 | 4 | 0 | proposed |
| Logiksystem | logic system | 0.98 | 5 | 4 | 0 | proposed |
| Multi-Agenten-Systeme | multi-agent systems | 0.99 | 7 | 2 | 0 | proposed |
| Naht | Seam | 0.99 | 8 | 1 | 1 | proposed |
| Pfadabhängigkeit | Path Dependence | 1.00 | 7 | 2 | 2 | stated in 1 doc(s) ^[aegis-paradoxon-konzeption-und-analyse.md:L59]; proposed |
| Pfadabhängigkeit | Path dependence | 0.96 | 7 | 2 | 2 | proposed |
| Peripherie | periphery | 0.93 | 7 | 2 | 0 | proposed |
| Persönliche Identität | Personal identity | 0.94 | 4 | 5 | 3 | proposed |
| Portale | Portals | 0.86 | 8 | 1 | 0 | proposed |
| Postulat | Postulate | 0.94 | 8 | 1 | 0 | proposed |
| prozedural | Procedural | 0.89 | 4 | 5 | 2 | proposed |
| Quantenkohärenz | Quantum coherence | 1.00 | 8 | 1 | 0 | proposed |
| Quantenvakuum | Quantum vacuum | 0.97 | 8 | 1 | 1 | proposed |
| Quantenvakuum | quantum vacuum | 0.97 | 8 | 1 | 1 | proposed |
| Reine Logik | pure logic | 0.99 | 3 | 6 | 0 | proposed |
| Ruhezustand | Resting-State | 0.81 | 3 | 6 | 1 | proposed |
| SIS-Zustand | Secure Isolation State | 0.95 | 1 | 8 | 1 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-protokoll.md:L169] |
| Sicherheitsverhalten | Safety Behaviors | 0.96 | 5 | 4 | 3 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L40]; proposed |
| Sucher | Searcher | 0.89 | 7 | 2 | 0 | proposed |
| Selbstbewusstseins | self-consciousness | 0.82 | 5 | 4 | 0 | proposed |
| Self-Modification | Selbstmodifikation | 0.92 | 2 | 7 | 2 | proposed |
| Theseus-Schiff | Ship of Theseus | 0.91 | 1 | 8 | 0 | proposed |
| Simulationsargument | simulation argument | 1.00 | 5 | 4 | 2 | proposed |
| Singularitäten | singularities | 0.80 | 6 | 3 | 0 | proposed |
| Spaghettisierung | Spaghettification | 0.83 | 4 | 5 | 1 | proposed |
| Standardmodell | Standard Model | 0.99 | 6 | 3 | 1 | proposed |
| Startpunkt | starting point | 0.83 | 6 | 3 | 0 | proposed |
| Story-Ziel | Story Goal | 0.89 | 2 | 7 | 2 | proposed |
| Superintelligenz | Superintelligence | 0.96 | 4 | 5 | 2 | proposed |
| Symmetriebruch | symmetry breaking | 0.96 | 7 | 2 | 0 | proposed |
| Systemprotokoll | system protocol | 0.98 | 7 | 2 | 0 | proposed |
| Tertiär | tertiary | 0.99 | 2 | 7 | 1 | proposed |
| Vakuumfluktuationen | Vacuum fluctuations | 0.99 | 8 | 1 | 1 | proposed |
| Wahrheitswert | truth value | 0.99 | 8 | 1 | 1 | proposed |
| Zeitlichkeit | temporality | 0.88 | 7 | 2 | 0 | proposed |
| Zeugenfunktion | witness function | 0.96 | 7 | 2 | 1 | proposed |
| Zielfunktion | objective function | 0.80 | 5 | 4 | 0 | proposed |
| Abstraktionsebenen | Levels of Abstraction | 1.00 | 4 | 4 | 2 | proposed |
| Agnotologie | agnotology | 0.83 | 5 | 3 | 3 | proposed |
| Aussagenlogik | propositional logic | 1.00 | 7 | 1 | 0 | proposed |
| Bekenstein-Grenze | Bekenstein Bound | 0.98 | 6 | 2 | 0 | proposed |
| Benutzeroberfläche | user interface | 0.94 | 6 | 2 | 0 | proposed |
| Beschleunigte Expansion des Raumes | Big Rip | 0.98 | 1 | 7 | 1 | stated in 1 doc(s) ^[charakter-kompilation-fuer-kohaerenz-protokoll.md:L60] |
| Bifurkationen | Bifurcations | 0.92 | 6 | 2 | 1 | proposed |
| spröde | Brittle | 0.90 | 5 | 3 | 0 | proposed |
| Kaskadenausfall | Cascading_failure | 0.82 | 3 | 5 | 1 | proposed |
| Chaitin-Konstante | Chaitin's constant | 0.95 | 6 | 2 | 1 | proposed |
| Kind-EP | Child EP | 0.98 | 5 | 3 | 0 | proposed |
| Kohärenz-Kern (K₁) | Coherence Kernel (K₁) | 0.99 | 1 | 7 | 1 | proposed |
| Komplementarität | Complementarity | 0.99 | 7 | 1 | 1 | proposed |
| Komplexe Adaptive Systeme | Complex Adaptive Systems | 0.95 | 4 | 4 | 1 | proposed |
| Kontrolltheorie | Control theory | 0.98 | 7 | 1 | 0 | proposed |
| Koordinator | Coordinator | 0.93 | 7 | 1 | 0 | proposed |
| Kern-Welt 2 | Core World 2 | 0.99 | 5 | 3 | 0 | proposed |
| Kern-Welt 3 | Core World 3 | 0.99 | 5 | 3 | 0 | proposed |
| Kryptographisch | Cryptographic | 0.92 | 2 | 6 | 1 | proposed |
| kryptographisch | Cryptographic | 0.89 | 2 | 6 | 0 | proposed |
| Datenzerfall | data decay | 0.96 | 6 | 2 | 0 | proposed |
| Tiefe Ich-Perspektive | Deep POV | 0.95 | 2 | 6 | 2 | stated in 2 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L57] ^[prosaversion-von-genesis-erstellen.md:L133] |
| Diegese | diegesis | 0.89 | 7 | 1 | 0 | proposed |
| Schwierige | Difficult | 0.91 | 5 | 3 | 0 | proposed |
| Doktrin | Doctrine | 0.88 | 7 | 1 | 0 | proposed |
| dynamische Paare | Dynamic Pairs | 0.82 | 2 | 6 | 1 | proposed |
| Verkörperte Kognition | Embodied Cognition | 1.00 | 4 | 4 | 1 | stated in 1 doc(s) ^[lokalitaeten-konzept-fuer-roman-simulation.md:L103]; proposed |
| Emotionale Anteile | emotional parts | 0.97 | 4 | 4 | 1 | proposed |
| Emotionalen Teilen | emotional parts | 0.92 | 4 | 4 | 0 | proposed |
| Verschränkungsinseln | Entanglement Islands | 0.89 | 1 | 7 | 0 | proposed |
| existentielle Krise | Existential Crisis | 0.89 | 1 | 7 | 1 | proposed |
| Existenzielle Leere | existential emptiness | 0.96 | 3 | 5 | 0 | proposed |
| externe Anomalie | External Anomaly | 0.86 | 6 | 2 | 0 | proposed |
| Externe Anomalie | external anomaly | 1.00 | 4 | 4 | 0 | proposed |
| Feuerwehrmänner | firefighters | 0.93 | 2 | 6 | 1 | proposed |
| Gefrorene | frozen | 0.92 | 2 | 6 | 0 | proposed |
| Gewichtung | weighting | 0.93 | 6 | 2 | 0 | proposed |
| Granularität | Granularity | 0.97 | 6 | 2 | 2 | proposed |
| Granularität | granularity | 1.00 | 6 | 2 | 2 | proposed |
| Löschlogik | Hypervisor | 0.81 | 2 | 6 | 1 | stated in 1 doc(s) ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:L187] |
| Zeugenfunktion | Kaels Witness Function | 1.00 | 7 | 1 | 1 | stated in 1 doc(s) ^[dkt-fundament-kohaerenz-protokoll-md.md:L123] |
| Kaskadenversagen | cascade failure | 0.90 | 5 | 3 | 0 | proposed |
| Kein Vertrauen | No-Trust | 0.90 | 1 | 7 | 1 | proposed |
| Ko-Bewusstheit | co-awareness | 0.99 | 7 | 1 | 0 | proposed |
| Komplementarität | complementarity | 1.00 | 7 | 1 | 1 | proposed |
| Komplexe Posttraumatische Belastungsstörung | complex posttraumatic stress disorder | 0.87 | 6 | 2 | 0 | proposed |
| Kontrolltheorie | control theory | 0.97 | 7 | 1 | 0 | proposed |
| Konzept des Narrativen Systems | System Mind | 0.99 | 1 | 7 | 1 | stated in 1 doc(s) ^[dramatica-storyform-kohaerenz-protokoll-analyse.md:L19] |
| Landauer-Wärme | Landauer-Heat | 0.98 | 7 | 1 | 0 | proposed |
| Luhmanns Systemtheorie | Luhmann's systems theory | 0.99 | 5 | 3 | 0 | proposed |
| Maschinenbewusstsein | Machine Consciousness | 0.90 | 6 | 2 | 0 | proposed |
| Makrostruktur | macro-structure | 0.98 | 5 | 3 | 0 | proposed |
| Mannigfaltigkeit | manifold | 0.97 | 5 | 3 | 0 | proposed |
| Meta-Logik | Metalogic | 0.94 | 6 | 2 | 2 | proposed |
| Meta-Logik | metalogic | 0.88 | 6 | 2 | 2 | proposed |
| NP-schwere | NP-hard | 0.95 | 5 | 3 | 1 | proposed |
| Naturgesetz | law of nature | 0.88 | 6 | 2 | 0 | proposed |
| Nicht-Dualität | non-dualism | 1.00 | 6 | 2 | 2 | proposed |
| Nicht-Euklidische | Non-Euclidean | 0.99 | 6 | 2 | 1 | proposed |
| Parataxe | parataxis | 0.94 | 5 | 3 | 1 | proposed |
| Partizipation | Participation | 0.89 | 6 | 2 | 0 | proposed |
| Philosophie der Information | Philosophy of information | 0.96 | 6 | 2 | 0 | proposed |
| Protokoll v1.4 | Protocol v1.4 | 0.98 | 2 | 6 | 0 | proposed |
| Psycho-Architekturen | Psycho-Architectures | 0.85 | 3 | 5 | 0 | proposed |
| Realitätsschichten | Reality Layers | 0.96 | 7 | 1 | 0 | proposed |
| Rekursive Konsistenzvalidierung | Recursive Consistency Validation | 0.99 | 3 | 5 | 1 | proposed |
| Rhizom | Rhizome | 0.87 | 5 | 3 | 3 | proposed |
| heilig | Sacred | 0.91 | 3 | 5 | 0 | proposed |
| Schmelztiegel | crucible | 0.81 | 5 | 3 | 0 | proposed |
| Schrein | Shrine | 0.99 | 7 | 1 | 0 | proposed |
| Schwellen | Thresholds | 0.95 | 7 | 1 | 0 | proposed |
| Zweiter Hauptsatz | Second law | 1.00 | 7 | 1 | 1 | proposed |
| Sucher | Seeker | 0.83 | 7 | 1 | 0 | proposed |
| Selbst-Referenz | Self-reference | 0.88 | 2 | 6 | 1 | proposed |
| Selbstähnlichkeit | Self-similarity | 0.98 | 7 | 1 | 1 | proposed |
| Selbstähnlichkeit | self-similarity | 0.93 | 7 | 1 | 0 | proposed |
| Skinner-Boxen | Skinner boxes | 0.92 | 7 | 1 | 0 | proposed |
| Systemverantwortung | system responsibility | 0.81 | 5 | 3 | 0 | proposed |
| TSDP-Dynamiken | TSDP dynamics | 0.98 | 7 | 1 | 0 | proposed |
| Tautologie | Tautology | 0.94 | 6 | 2 | 0 | proposed |
| Verifizierer | verifier | 0.99 | 6 | 2 | 0 | proposed |
| Vertexoperatoralgebren | Vertex Operator Algebras | 0.86 | 3 | 5 | 1 | proposed |
| Virtuelle Realität | Virtual Reality | 0.99 | 2 | 6 | 1 | proposed |
| Wir-Stimme | We-Voice | 1.00 | 4 | 4 | 2 | stated in 1 doc(s) ^[systemic-architecture-specification-the-coherence-protocol-w.md:L77]; proposed |
| Zeugen-Funktion | Witness-Function | 0.89 | 2 | 6 | 0 | proposed |
| Zentralisatoren | centralizers | 0.97 | 6 | 2 | 2 | proposed |
| Non-Dualität | Advaita | 0.98 | 1 | 6 | 1 | stated in 1 doc(s) ^[narrativ-existenzieller-kohaerenz-nzt-protokoll.md:L249] |
| agentenbasiert | Agent-Based | 0.83 | 1 | 6 | 1 | proposed |
| Agentenbasierte Modellierung | agent-based modeling | 1.00 | 6 | 1 | 1 | proposed |
| Aristotelisch | Aristotelian | 0.92 | 2 | 5 | 0 | proposed |
| Prinzipal | Auftraggeber | 0.93 | 2 | 5 | 1 | stated in 1 doc(s) ^[aegis-paradoxon-neukonzeption-und-analyse-docx.md:L48] |
| Autopoiesis-Theorie | autopoiesis theory | 0.99 | 6 | 1 | 0 | proposed |
| Baby-Monstergruppe | Baby Monster group | 0.95 | 5 | 2 | 0 | proposed |
| Belohnungs-Hacking | Reward Hacking | 1.00 | 1 | 6 | 1 | stated in 1 doc(s) ^[optimierter-prompt-fuer-kohaerenz-protokoll.md:L147]; proposed |
| Beobachtung der Beobachtung | Reentry | 0.95 | 3 | 4 | 1 | stated in 1 doc(s) ^[emergenz-autonomer-systeme-aegis-forschung.md:L274] |
| Berechenbarkeitstheorie | computability theory | 0.98 | 6 | 1 | 0 | proposed |
| Bifurkationen | bifurcations | 0.99 | 6 | 1 | 1 | proposed |
| Blockuniversum | Eternalismus | 0.86 | 4 | 3 | 1 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L150] |
| Boltzmann-Konstante | Boltzmann constant | 1.00 | 5 | 2 | 0 | proposed |
| Branen | Branes | 0.93 | 3 | 4 | 0 | proposed |
| Isomorphismus der Last | Burden | 0.98 | 1 | 6 | 1 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L148] |
| Trauma-Last | Burden | 0.93 | 1 | 6 | 1 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L273] |
| Cache-Inkohärenz | Cache Incoherence | 0.92 | 4 | 3 | 0 | proposed |
| Feuerstelle | Campfire | 0.94 | 1 | 6 | 0 | proposed |
| Kaskadierendes Versagen | Cascading Failure | 1.00 | 4 | 3 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-inkubation-x.md:L129] |
| Chaitin-Konstante | Chaitin constant | 0.97 | 6 | 1 | 1 | proposed |
| Chaitin-Konstante | Chaitin-constant | 0.96 | 6 | 1 | 1 | proposed |
| Schach | Chess | 0.84 | 6 | 1 | 0 | proposed |
| Mitbewusstsein | Co-Consciousness | 1.00 | 1 | 6 | 1 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L98] |
| Ko-Regulation | Co-Regulation | 0.81 | 2 | 5 | 0 | proposed |
| Mitbewusstsein | Co-consciousness | 0.87 | 1 | 6 | 0 | proposed |
| Kollaps-Kern (K₀) | Collapse Kernel (K₀) | 1.00 | 1 | 6 | 0 | proposed |
| Komplexe Posttraumatische Belastungsstörung | Complex Posttraumatic Stress Disorder | 0.95 | 6 | 1 | 1 | proposed |
| Korrespondenz-Check | Correspondence-Check | 0.92 | 1 | 6 | 0 | proposed |
| Schmelztiegel | Crucible | 1.00 | 5 | 2 | 2 | proposed |
| Demiurg | Demiurge | 0.85 | 6 | 1 | 1 | proposed |
| Der Möglichkeits-Garten | The Garden of Possibilities | 1.00 | 3 | 4 | 0 | proposed |
| Derealisationsstörung | Derealization Disorder | 0.99 | 5 | 2 | 1 | proposed |
| Diegese | Ebene der Romanwelt | 0.83 | 7 | 0 | 0 | stated in 1 doc(s) ^[kohaerenz-protokoll-dramatica-synthese-masterkonzept.md:L100] |
| Diese Krise | Reproducibility Crisis | 0.89 | 6 | 1 | 1 | stated in 1 doc(s) ^[risikoanalysebericht-eine-systematische-bewertung-der-bedroh.md:L67] |
| Digitale Überwelt | Digital Overworld | 0.99 | 6 | 1 | 0 | proposed |
| Dynamikpaare | Dynamic Pairs | 0.99 | 1 | 6 | 1 | stated in 1 doc(s) ^[dual-kernel-erzaehlarchitektur-bewusstsein-symmetrie-ourobor.md:L82] |
| Dynamische Paare | Dynamic Pairs | 0.95 | 1 | 6 | 1 | stated in 1 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L82]; proposed |
| Einstein-Rosen-Brücke | Einstein-Rosen Bridge | 0.98 | 5 | 2 | 0 | proposed |
| emotionale Wahrheit | Emotional Truth | 0.92 | 5 | 2 | 1 | proposed |
| Ergodisch | Ergodic | 0.85 | 1 | 6 | 1 | proposed |
| Erhabene | sublime | 0.97 | 2 | 5 | 1 | proposed |
| Erste-Person-Perspektive | first-person perspective | 0.92 | 5 | 2 | 0 | proposed |
| Täter-Introjekt | Externalized Perpetrator Introject | 0.93 | 3 | 4 | 1 | stated in 1 doc(s) ^[ki-narrative-kollaps-kohaerenz-paradoxie.md:L87] |
| Kollaps der Wahrheiten | Flip | 0.91 | 1 | 6 | 1 | stated in 1 doc(s) ^[ki-narrative-kollaps-kohaerenz-paradoxie.md:L109] |
| fragmentierter Zustand | Fragmented State | 0.99 | 5 | 2 | 0 | proposed |
| Fähigkeiten-Fehlanpassung | Skill Mismatch | 1.00 | 4 | 3 | 3 | stated in 3 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik.md:L261] ^[kael-charakterarchitektur-und-konfliktdynamik-2.md:L261] |
| Gedächtnispalast | Memory Palace | 0.93 | 2 | 5 | 2 | proposed |
| Gewichtung | Weighting | 0.99 | 6 | 1 | 0 | proposed |
| Gezeitenkräfte | tidal forces | 0.96 | 4 | 3 | 0 | proposed |
| Gitterstruktur | lattice structure | 0.85 | 6 | 1 | 0 | proposed |
| Glitch-Ästhetik | Glitch_art | 0.88 | 2 | 5 | 2 | proposed |
| Graphentheorie | Graph theory | 0.98 | 6 | 1 | 0 | proposed |
| Haufen | heap | 0.82 | 5 | 2 | 1 | proposed |
| Hinder | Oppose | 0.88 | 4 | 3 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-duale-dramatica-storyform-synthese.md:L109] |
| Innerer Selbsthelfer | Inner Self Helper | 0.92 | 1 | 6 | 0 | proposed |
| integriertes Selbst | Integrated Self | 0.96 | 3 | 4 | 0 | proposed |
| Interner Zustand | Internal State | 0.92 | 4 | 3 | 0 | proposed |
| Kampf-oder-Flucht | fight-or-flight | 0.98 | 4 | 3 | 0 | proposed |
| Wissensgraphen | Knowledge Graph | 0.92 | 2 | 5 | 1 | proposed |
| Komplexen Adaptiven Systemen | complex adaptive systems | 0.96 | 2 | 5 | 0 | proposed |
| Konformen Feldtheorie | conformal field theory | 0.93 | 4 | 3 | 0 | proposed |
| Korrespondenz-Wahrheit | correspondence truth | 0.98 | 4 | 3 | 0 | proposed |
| Lyons-Gruppe | Lyons group | 0.99 | 6 | 1 | 1 | proposed |
| Mannigfaltigkeit | Manifold | 0.97 | 5 | 2 | 0 | proposed |
| Viele-Welten | Many-Worlds | 0.98 | 4 | 3 | 0 | proposed |
| Mathematische Universum-Hypothese | Mathematical Universe Hypothesis | 0.99 | 1 | 6 | 1 | proposed |
| Mathematische Universumshypothese | Mathematical Universe Hypothesis | 0.92 | 1 | 6 | 0 | proposed |
| Methode der Loci | Memory Palace | 0.99 | 2 | 5 | 2 | stated in 1 doc(s) ^[umfassendes-lokalitaeten-konzept-fuer-roman.md:L94] |
| Meta-Kognition | meta-cognition | 0.83 | 6 | 1 | 0 | proposed |
| Zeugenfunktion | Modell die Witness Function | 1.00 | 7 | 0 | 0 | stated in 1 doc(s) ^[storyforms-system-mind-bewusstsein.md:L130] |
| Monster-Lie-Algebra | monster Lie algebra | 0.93 | 6 | 1 | 1 | proposed |
| Weder | Neither | 1.00 | 4 | 3 | 1 | proposed |
| Neurobildgebung | Neuroimaging | 0.99 | 1 | 6 | 1 | proposed |
| Neuroplastizität | Neuroplasticity | 0.98 | 5 | 2 | 2 | proposed |
| Nicht-Dualität | non-duality | 1.00 | 6 | 1 | 1 | proposed |
| Nicht-Widerspruch | Non-Contradiction | 0.94 | 2 | 5 | 1 | proposed |
| Nonlokalität | Nonlocality | 0.98 | 1 | 6 | 1 | proposed |
| Nutzung der Leser-Reaktion | Reader-Response | 1.00 | 1 | 6 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-inkubation-x.md:L220] |
| P-Klasse | P-Class | 0.99 | 3 | 4 | 0 | proposed |
| Photonensphäre | Photon Sphere | 1.00 | 3 | 4 | 1 | proposed |
| Vorhersagefehlern | Prediction Errors | 0.95 | 5 | 2 | 1 | stated in 1 doc(s) ^[ki-prompt-analyse-hard-problem-of-consciousness.md:L56] |
| präfrontaler Kortex | Prefrontal Cortex | 0.97 | 2 | 5 | 0 | proposed |
| Rekursive Selbstverbesserung | Recursive Self-Improvement | 1.00 | 4 | 3 | 3 | proposed |
| Regelsatz | rule set | 0.88 | 5 | 2 | 0 | proposed |
| Restrukturierung | restructuring | 0.98 | 6 | 1 | 0 | proposed |
| Vorzeitige Auflösung | Reward Hacking | 0.98 | 1 | 6 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L516] |
| Robotik | Robotics | 0.95 | 4 | 3 | 0 | proposed |
| Sicherheitsverhalten | Safety Behavior | 0.98 | 5 | 2 | 2 | stated in 2 doc(s) ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L101] ^[projektanalyse-kohaerenz-protokoll-dis.md:L19]; proposed |
| Sage | Züge des Weisen | 0.95 | 4 | 3 | 3 | stated in 3 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik.md:L329] ^[kael-charakterarchitektur-und-konfliktdynamik-2.md:L329] |
| Selbsterhaltungstrieb | self-preservation drive | 0.97 | 6 | 1 | 0 | proposed |
| selbstorganisierend | Self-Organizing | 0.99 | 2 | 5 | 0 | proposed |
| Semiotik | Semiotics | 0.98 | 4 | 3 | 2 | proposed |
| Singularities | Singularitäten | 0.82 | 1 | 6 | 0 | proposed |
| Sonde | probe | 0.84 | 6 | 1 | 0 | proposed |
| Sporadische Gruppe | Sporadic_group | 1.00 | 1 | 6 | 0 | proposed |
| Surrealismus | Surrealism | 0.88 | 4 | 3 | 2 | proposed |
| Symbolischer Kern | symbolic core | 1.00 | 3 | 4 | 0 | proposed |
| Synchronizität | Synchronicity | 0.93 | 5 | 2 | 1 | proposed |
| Syntaxfehler | syntax error | 0.97 | 5 | 2 | 0 | proposed |
| Systemanalytiker | system analyst | 0.93 | 6 | 1 | 0 | proposed |
| Systemische Handlungsfähigkeit | Systematic Agency | 0.96 | 1 | 6 | 1 | stated in 1 doc(s) ^[aegis-singularitaet-jenseits-entropiegleichung-2.md:L162] |
| Systemik | Systemics | 0.93 | 6 | 1 | 0 | proposed |
| Systemneustart | system reboot | 0.97 | 4 | 3 | 0 | proposed |
| Systemprotokollen | system protocols | 0.93 | 5 | 2 | 0 | proposed |
| TSDP-Behandlung | TSDP therapy | 1.00 | 6 | 1 | 0 | proposed |
| Top-down-Kontrolle | top-down control | 0.95 | 1 | 6 | 0 | proposed |
| Totalität | totality | 0.97 | 4 | 3 | 1 | proposed |
| Umschwung | Turn | 0.80 | 1 | 6 | 0 | proposed |
| Verteidigungs-Aktionssystemen | defensive action systems | 0.99 | 5 | 2 | 0 | proposed |
| Weltbau | World Building | 0.87 | 2 | 5 | 0 | proposed |
| Werkstatt | workshop | 0.85 | 6 | 1 | 0 | proposed |
| Zelluläre | cellular | 0.98 | 4 | 3 | 1 | proposed |
| psychische Fragmentierung | psychic fragmentation | 0.83 | 6 | 1 | 0 | proposed |
| AEGIS-Kern | Zentraleinheit | 0.80 | 5 | 1 | 1 | stated in 1 doc(s) ^[lokalitaeten-konzept-fuer-roman-simulation.md:L244] |
| Adaptive Schicht | Adaptive Layer | 1.00 | 2 | 4 | 0 | proposed |
| Apollinisch | Apollonian | 0.86 | 3 | 3 | 2 | proposed |
| Auferstehung | Resurrection | 0.97 | 3 | 3 | 1 | proposed |
| Aussicht | prospect | 0.99 | 2 | 4 | 1 | proposed |
| Axiomatisierung | Axiomatizing | 0.98 | 5 | 1 | 0 | proposed |
| Beobachter-Effekt | Observer effect | 0.99 | 2 | 4 | 0 | proposed |
| Bestimmung der Vier Domänen | Four Throughlines | 1.00 | 1 | 5 | 1 | stated in 1 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L73] |
| Betreuer | Carer | 0.97 | 3 | 3 | 0 | proposed |
| Blockuniversum | Block Universe | 1.00 | 4 | 2 | 0 | proposed |
| Brane | Membrane | 0.86 | 4 | 2 | 1 | stated in 1 doc(s) ^[reality-s-isomorphic-architecture-explained.md:L68] |
| Bruxismus | Bruxism | 0.82 | 4 | 2 | 1 | proposed |
| Kontext-Fehler | Context Rot | 0.93 | 1 | 5 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L250] |
| Schwellenüberschreitung | Crossing the Threshold | 0.98 | 2 | 4 | 1 | proposed |
| Erzählstränge | Dramatica-Throughlines | 0.99 | 4 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-hard-sf-horror-thriller.md:L139] |
| Dynamische Systeme | dynamic systems | 1.00 | 4 | 2 | 0 | proposed |
| Einwand der Isolation | isolation objection | 0.91 | 3 | 3 | 0 | proposed |
| Verkörperte Kognition | Embodied cognition | 0.97 | 4 | 2 | 0 | proposed |
| Emotionale Teile | emotional parts | 0.89 | 2 | 4 | 0 | proposed |
| Energiedissipation | energy dissipation | 0.97 | 4 | 2 | 0 | proposed |
| Entlastung | Ritual des Unburdening | 0.82 | 5 | 1 | 1 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L152] |
| Erinnerungslandschaft | landscape of memory | 0.98 | 3 | 3 | 0 | proposed |
| Euklidische Geometrie | Euclidean Geometry | 0.92 | 5 | 1 | 0 | proposed |
| Verbannte | Exiled | 0.98 | 2 | 4 | 0 | proposed |
| existenzielle Wahl | Existential Choice | 0.98 | 3 | 3 | 2 | proposed |
| Externe Anomalie | External Anomaly | 1.00 | 4 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L218]; proposed |
| Faktorgruppe | Quotientengruppe | 0.85 | 2 | 4 | 2 | stated in 2 doc(s) ^[monstergruppe-babymonstergruppe-fragmentierung-erzaehlung.md:L95] ^[monstergruppe-metapher-auf-mathematische-kohaerenz.md:L41] |
| Verlassenheitsangst | Fear of abandonment | 0.98 | 5 | 1 | 0 | proposed |
| Feuerbekämpfer | firefighter | 0.95 | 3 | 3 | 0 | proposed |
| Feuerwehrmann | firefighter | 0.92 | 3 | 3 | 0 | proposed |
| Fixpunkte | fixed points | 0.99 | 5 | 1 | 1 | proposed |
| Flutung | Flooding | 0.93 | 2 | 4 | 0 | proposed |
| Fokalisierung | Focalization | 0.99 | 5 | 1 | 1 | proposed |
| Formalismus | formalism | 0.89 | 5 | 1 | 0 | proposed |
| Fragebogen | questionnaire | 0.91 | 5 | 1 | 0 | proposed |
| Freeze-Reaktion | freeze response | 0.99 | 2 | 4 | 1 | proposed |
| Gefrorene | Frozen | 0.91 | 2 | 4 | 0 | proposed |
| Frühwarnsystem | early warning system | 0.81 | 5 | 1 | 0 | proposed |
| Spiel des Lebens | Game of Life | 0.96 | 4 | 2 | 2 | proposed |
| Generative KI | generative AI | 0.97 | 2 | 4 | 0 | proposed |
| Gestaltwandler | Shapeshifter | 1.00 | 3 | 3 | 3 | stated in 3 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik.md:L351] ^[kael-charakterarchitektur-und-konfliktdynamik-2.md:L351] |
| Glitch-Kunst | Glitch_art | 0.98 | 1 | 5 | 1 | proposed |
| Gnostizismus | Gnosticism | 0.99 | 2 | 4 | 1 | proposed |
| HPA-Achse | HPA axis | 0.86 | 4 | 2 | 1 | proposed |
| Heilerin | Healer | 0.85 | 4 | 2 | 1 | proposed |
| Hyperaktivität | Hyperactivity | 0.94 | 3 | 3 | 1 | proposed |
| Thermodynamik der Information | Information thermodynamics | 0.98 | 4 | 2 | 1 | proposed |
| Integrierten Informationstheorie | Integrated information theory | 1.00 | 1 | 5 | 1 | proposed |
| Interferenzstruktur | interference structure | 0.93 | 5 | 1 | 0 | proposed |
| interner Prozess | Internal Process | 0.91 | 3 | 3 | 0 | proposed |
| Ungültigkeitserklärung | Invalidation | 1.00 | 1 | 5 | 1 | stated in 1 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L204] |
| Katatonie | catatonia | 0.98 | 5 | 1 | 0 | proposed |
| Kind-EP | child EP | 0.97 | 5 | 1 | 0 | proposed |
| Kinetisch | Kinetic | 0.91 | 1 | 5 | 0 | proposed |
| Künstliche Superintelligenz | Superintelligence | 0.95 | 1 | 5 | 0 | proposed |
| Leckage | Leakage | 0.97 | 5 | 1 | 0 | proposed |
| Token Management | Line Budgets | 0.83 | 1 | 5 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L340] |
| Logik des Paradoxons | Logic of Paradox | 0.93 | 1 | 5 | 0 | proposed |
| Schleifenquantengravitation | Loop Quantum Gravity | 0.99 | 3 | 3 | 3 | proposed |
| Maschinelles Lernen | Machine-Learning | 0.95 | 4 | 2 | 0 | proposed |
| Magier | Magician | 0.94 | 5 | 1 | 1 | proposed |
| Meta-Beobachtung | Meta-Observation | 1.00 | 5 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L209]; proposed |
| Metakognitiver | metacognitive | 0.90 | 5 | 1 | 0 | proposed |
| Multiple Persönlichkeitsstörung | Multiple Personality Disorder | 0.99 | 4 | 2 | 1 | proposed |
| Neuroplastizität | neuroplasticity | 1.00 | 5 | 1 | 1 | proposed |
| Nonlokalität | nonlocality | 0.99 | 1 | 5 | 1 | proposed |
| Ontischer Struktureller Realismus | Ontic structural realism | 0.98 | 3 | 3 | 2 | proposed |
| Ontischer Struktureller Realismus | ontic structural realism | 0.99 | 3 | 3 | 2 | proposed |
| Panoptismus | Panopticism | 0.82 | 4 | 2 | 2 | proposed |
| Pathologische Transformation | pathological transformation | 0.99 | 3 | 3 | 0 | proposed |
| Phänomenales Selbstmodell | Phenomenal Self-Model | 0.86 | 4 | 2 | 0 | proposed |
| Posttraumatisches Wachstum | Post Traumatic Growth | 0.98 | 4 | 2 | 1 | proposed |
| Posthumanismus | Posthumanism | 0.98 | 4 | 2 | 1 | proposed |
| Vorhersagefehler | Prediction Errors | 0.88 | 4 | 2 | 0 | proposed |
| Präfrontaler Kortex | Prefrontal Cortex | 0.97 | 1 | 5 | 0 | proposed |
| Proto-Bewusstsein | Proto-consciousness | 0.93 | 5 | 1 | 0 | proposed |
| Psychologische Landschaften | Psychological Landscapes | 1.00 | 2 | 4 | 1 | stated in 1 doc(s) ^[umfassendes-lokalitaeten-konzept-fuer-roman.md:L27]; proposed |
| Quantencomputing | quantum computing | 0.98 | 3 | 3 | 0 | proposed |
| Quantenzustand | quantum state | 0.99 | 5 | 1 | 0 | proposed |
| Zufluchtsort | Refuge | 0.88 | 5 | 1 | 1 | proposed |
| Schematherapie | Schema therapy | 1.00 | 2 | 4 | 1 | proposed |
| Schwarmintelligenz | Swarm intelligence | 1.00 | 5 | 1 | 1 | proposed |
| Schwerelosigkeit | Weightlessness | 0.95 | 5 | 1 | 0 | proposed |
| Segmentierung | Segmentation | 0.90 | 5 | 1 | 0 | proposed |
| Segmentierung | segmentation | 0.97 | 5 | 1 | 0 | proposed |
| Selbstorganisierte Kritikalität | self-organized criticality | 0.93 | 3 | 3 | 2 | proposed |
| Semantischer Drift | semantic drift | 0.99 | 2 | 4 | 0 | proposed |
| Signal-Rausch-Verhältnis | Signal-to-noise ratio | 1.00 | 5 | 1 | 1 | proposed |
| Simulationsfehler | Simulation Glitch | 0.93 | 5 | 1 | 0 | proposed |
| Skeptiker | Skeptic | 0.97 | 2 | 4 | 0 | proposed |
| Spezialisierte Module | Specialized Modules | 0.99 | 2 | 4 | 0 | proposed |
| Systemische Intervention | Systemic Intervention | 0.99 | 3 | 3 | 3 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L344]; proposed |
| Todestrieb | Thanatos | 1.00 | 3 | 3 | 3 | stated in 2 doc(s) ^[konzept-expose-schwarzschild-protokoll-optimierung.md:L251] ^[narrative-physik-attraktoren-leserbewusstsein.md:L131] |
| Toleranzfenster | Window of Tolerance | 1.00 | 3 | 3 | 2 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L59] |
| Tragischer Gott | Tragic God | 0.96 | 1 | 5 | 0 | proposed |
| tragischer Gott | Tragic God | 0.97 | 1 | 5 | 0 | proposed |
| Transhumanismus | Transhumanism | 0.95 | 4 | 2 | 2 | proposed |
| Transhumanismus | transhumanism | 0.98 | 4 | 2 | 1 | proposed |
| unbeabsichtigte Folgen | Unintended Consequences | 0.97 | 4 | 2 | 1 | proposed |
| Verlassenheitsangst | fear of abandonment | 1.00 | 5 | 1 | 0 | proposed |
| Vier Throughlines | four throughlines | 1.00 | 1 | 5 | 0 | proposed |
| Wahrheits-Rotation | truth rotation | 1.00 | 4 | 2 | 0 | proposed |
| Zero-Knowledge-Beweis | Zero-Knowledge Proof | 0.99 | 1 | 5 | 1 | proposed |
| Zugriffsrechte | access rights | 0.97 | 5 | 1 | 0 | proposed |
| Zweite-Ordnung-Kybernetik | second-order cybernetics | 0.93 | 3 | 3 | 1 | proposed |
| Erweiterung des Suchraums | Adversarial Query Expansion | 0.99 | 1 | 4 | 1 | stated in 1 doc(s) ^[ki-prompt-analyse-hard-problem-of-consciousness.md:L310] |
| Alben | albums | 0.94 | 4 | 1 | 0 | proposed |
| Algorithmische Opazität | Black Box | 0.99 | 1 | 4 | 1 | stated in 1 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L1127] |
| Kunsttherapie | Art therapy | 0.99 | 4 | 1 | 1 | proposed |
| Auge des Sturms | Eye of the Storm | 0.86 | 4 | 1 | 0 | proposed |
| Autopoiese | self-production | 0.93 | 4 | 1 | 0 | proposed |
| Axiomatische Restrukturierung | Systemanpassung | 0.90 | 3 | 2 | 2 | stated in 2 doc(s) ^[logik-trifft-transzendente-entitaet.md:L178] ^[logik-trifft-transzendente-entitaet-2.md:L176] |
| Benefizienz | Beneficence | 0.89 | 4 | 1 | 0 | proposed |
| Beobachter-Effekt | Observer Effect | 0.90 | 2 | 3 | 0 | proposed |
| Blockuniversum | block-universe | 1.00 | 4 | 1 | 0 | proposed |
| Spröde | Brittle | 0.89 | 2 | 3 | 0 | proposed |
| Katz-und-Maus-Spiel | Cat and Mouse Game | 1.00 | 4 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L382]; proposed |
| Kategorientheorie | Category theory | 0.96 | 4 | 1 | 0 | proposed |
| Zelluläre Automaten | Cellular automata | 1.00 | 4 | 1 | 1 | proposed |
| Verarbeitungskern | Central Processing Core | 0.99 | 3 | 2 | 1 | stated in 1 doc(s) ^[lokalitaeten-konzept-fuer-roman-simulation.md:L200] |
| Klasse P | Class P | 0.90 | 2 | 3 | 0 | proposed |
| Kollaps-Kern | Collapse-Kernel | 0.92 | 4 | 1 | 0 | proposed |
| Konforme Feldtheorie | Conformal Field Theory | 0.96 | 2 | 3 | 0 | proposed |
| Kontroll-Paradoxon | Control Paradox | 0.95 | 3 | 2 | 0 | proposed |
| Kernbetriebssystem | Core OS | 0.99 | 4 | 1 | 1 | stated in 1 doc(s) ^[ki-antagonist-fragmentierte-gottheit-analyse.md:L114] |
| Korrespondenz-Wahrheit | Correspondence truth | 0.94 | 4 | 1 | 0 | proposed |
| Rift | Crack | 0.99 | 3 | 2 | 1 | stated in 1 doc(s) ^[operationalizing-system-collapse-a-strategic-guide-to-aegis.md:L82] |
| Taoismus | Daoism | 0.97 | 3 | 2 | 0 | proposed |
| Dialektisch-Behavioralen Therapie | Dialectical Behavior Therapy | 0.96 | 4 | 1 | 0 | proposed |
| Dunkler Materie | dark matter | 0.98 | 3 | 2 | 1 | proposed |
| EP-Strukturen | EP structures | 0.86 | 2 | 3 | 0 | proposed |
| Eckpunkte | Vertices | 0.98 | 2 | 3 | 1 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L160] |
| Eigennatur | Svabhāva | 0.99 | 3 | 2 | 1 | stated in 1 doc(s) ^[narrative-plot-exploration-existenzielle-kohaerenz.md:L116] |
| Einfache Gruppe | Simple group | 1.00 | 3 | 2 | 1 | proposed |
| Emergenten Ordnung | emergent order | 0.96 | 1 | 4 | 0 | proposed |
| Emotionale Wahrheit | Emotional Truth | 0.99 | 3 | 2 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L317]; proposed |
| Emotionale Anteile | Emotional parts | 0.86 | 4 | 1 | 0 | proposed |
| Kapselung | Encapsulation | 1.00 | 4 | 1 | 0 | proposed |
| Energiefeld | energy field | 0.96 | 4 | 1 | 0 | proposed |
| Entropische Gravitation | Entropic gravity | 1.00 | 2 | 3 | 1 | proposed |
| Entropieminimierung | minimizing entropy | 1.00 | 4 | 1 | 0 | proposed |
| Erhabene | Sublime | 0.86 | 2 | 3 | 0 | proposed |
| Existenzielle Wahl | Existential Choice | 1.00 | 2 | 3 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L380]; proposed |
| Extradimensionen | extra dimensions | 0.99 | 4 | 1 | 0 | proposed |
| Kampfreaktion | Fight Response | 0.98 | 2 | 3 | 0 | proposed |
| Verbotenes Wissen | Forbidden Knowledge | 1.00 | 4 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L355]; proposed |
| Fragile Stabilität | fragile stability | 0.99 | 1 | 4 | 0 | proposed |
| Glitch-Kunst | Glitch-Art | 0.92 | 1 | 4 | 1 | proposed |
| Göttin | Goddess | 0.97 | 2 | 3 | 1 | proposed |
| Hacken des Zentralrechners | Hacking the Mainframe | 1.00 | 1 | 4 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L555]; proposed |
| Wärmetod des Universums | Heat death of the universe | 1.00 | 4 | 1 | 1 | proposed |
| Hegelsche Dialektik | Hegelian dialectic | 0.92 | 4 | 1 | 0 | proposed |
| Hegelsche Dialektik | the Hegelian dialectic | 0.96 | 4 | 1 | 0 | proposed |
| Heilerin | healer | 0.96 | 4 | 1 | 1 | proposed |
| Hermeneutik | hermeneutics | 0.97 | 2 | 3 | 1 | proposed |
| Immanenz | Immanence | 0.96 | 3 | 2 | 1 | proposed |
| Inaktivität | Inertia | 0.94 | 2 | 3 | 1 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse-2.md:L426] |
| Integriertes Selbst | Integrated Self | 0.96 | 1 | 4 | 0 | proposed |
| Interne Vermittlung | Internal Mediation | 0.99 | 2 | 3 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L83]; proposed |
| Interne Vermittlung | internal mediation | 1.00 | 2 | 3 | 0 | proposed |
| Kael-Juna Verbindung | Kael-Juna connection | 0.98 | 3 | 2 | 0 | proposed |
| Kaskadierendes Versagen | cascading failure | 0.98 | 4 | 1 | 0 | proposed |
| Katastrophales Vergessen | catastrophic forgetting | 0.89 | 3 | 2 | 2 | proposed |
| Kernbetriebssystem | core operating system | 0.98 | 4 | 1 | 0 | proposed |
| Wissenslücken | Knowledge Gaps | 0.99 | 4 | 1 | 0 | proposed |
| Konforme Feldtheorien | conformal field theories | 0.99 | 2 | 3 | 1 | proposed |
| Korrelate des Bewusstseins | correlates of consciousness | 0.85 | 4 | 1 | 1 | proposed |
| Korrelaten | correlates | 0.86 | 3 | 2 | 1 | proposed |
| Krieger | Warrior | 0.98 | 3 | 2 | 1 | proposed |
| Kristallisation | crystallization | 0.93 | 4 | 1 | 0 | proposed |
| Landauer-Kosten | Landauer costs | 0.93 | 3 | 2 | 0 | proposed |
| Liebende | Lover | 1.00 | 3 | 2 | 2 | stated in 2 doc(s) ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L249] ^[beziehungsheilung-nach-trauma-konzeptpapier-3.md:L255] |
| Logiken der Formalen Inkonsistenz | Logics of formal inconsistency | 1.00 | 4 | 1 | 1 | proposed |
| Logiken der Formalen Inkonsistenz | logics of formal inconsistency | 1.00 | 4 | 1 | 0 | proposed |
| Lorentz-Invarianz | Lorentz invariance | 0.94 | 4 | 1 | 1 | proposed |
| Manager und Firefighters | Managers and Firefighters | 0.99 | 1 | 4 | 0 | proposed |
| Speicherleck | Memory Leak | 0.98 | 2 | 3 | 1 | proposed |
| NP-schwer | NP-hard | 1.00 | 2 | 3 | 1 | proposed |
| Zusammenfassung der Storyform | Narrative Code | 0.98 | 1 | 4 | 1 | stated in 1 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L259] |
| Nicht-Algorithmische | non-algorithmic | 0.99 | 2 | 3 | 0 | proposed |
| Nicht-Assoziativität | non-associativity | 1.00 | 1 | 4 | 0 | proposed |
| Non-Lokalität | Non-Locality | 0.92 | 1 | 4 | 0 | proposed |
| Ortsgefühl | Sense of Place | 0.99 | 3 | 2 | 2 | stated in 2 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung-2.md:L342] ^[roman-lokalitaeten-konzept-und-ausarbeitung-3.md:L343]; proposed |
| Parasit | parasite | 0.94 | 4 | 1 | 0 | proposed |
| Wahrnehmungsmanipulation | Perception Manipulation | 1.00 | 3 | 2 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L119]; proposed |
| Persönliche Identität | personal identity | 0.95 | 4 | 1 | 0 | proposed |
| Platonismus | Platonism | 0.97 | 3 | 2 | 1 | proposed |
| Polyvagal-Theorie | Polyvagal theory | 1.00 | 4 | 1 | 0 | proposed |
| Posttraumatisches Wachstum | Posttraumatic Growth | 0.92 | 4 | 1 | 0 | proposed |
| Prädiktive Modellierung | Predictive Modeling | 0.97 | 1 | 4 | 0 | proposed |
| prädiktive Modellierung | Predictive Modeling | 0.89 | 1 | 4 | 0 | proposed |
| Prinzipal | Principal | 0.95 | 2 | 3 | 2 | proposed |
| Quotientengruppe | Quotient group | 0.99 | 4 | 1 | 1 | proposed |
| Rationaler ANP | Rational ANP | 0.92 | 4 | 1 | 0 | proposed |
| Rezeptionsästhetik | Reader-Response Theory | 1.00 | 3 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L153] |
| Wiedereintritt | Reentry | 1.00 | 1 | 4 | 0 | proposed |
| Romanze | romance | 0.91 | 1 | 4 | 0 | proposed |
| STRUKTURELLE DISSOZIATION | Structural dissociation | 0.99 | 3 | 2 | 0 | proposed |
| Suchender | Searcher | 0.94 | 3 | 2 | 0 | proposed |
| Selbstorganisierte Kritikalität | Self-organized criticality | 0.93 | 3 | 2 | 1 | proposed |
| Steinschleuder | Slingshot | 1.00 | 2 | 3 | 2 | proposed |
| Slingshot-Argument | Steinschleuder | 1.00 | 3 | 2 | 2 | stated in 1 doc(s) ^[wahrheitstheorien-kohaerenz-vs-korrespondenz.md:L73] |
| Strukturalismus | Structuralism | 0.96 | 3 | 2 | 2 | proposed |
| Strukturalismus | structuralism | 0.99 | 3 | 2 | 1 | proposed |
| Strukturellen Realismus | structural realism | 0.98 | 2 | 3 | 2 | proposed |
| Synchronität | Synchronicity | 0.93 | 3 | 2 | 0 | proposed |
| Systemneustart | System Reset | 1.00 | 4 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L568] |
| Taoismus | Taoism | 1.00 | 3 | 2 | 1 | proposed |
| Thermodynamik der Information | information thermodynamics | 0.92 | 4 | 1 | 0 | proposed |
| Token-Wahrscheinlichkeiten | token probabilities | 1.00 | 1 | 4 | 0 | proposed |
| totale Unterwerfung | Total Submission | 0.91 | 3 | 2 | 0 | proposed |
| Vagusnerv | Vagus nerve | 0.99 | 4 | 1 | 1 | proposed |
| Verbotenes Wissen | forbidden knowledge | 0.88 | 4 | 1 | 0 | proposed |
| Verstärkungslernen | reinforcement learning | 0.98 | 2 | 3 | 0 | proposed |
| Vertexoperatoralgebren | vertex operator algebras | 0.97 | 3 | 2 | 0 | proposed |
| Virtuelle Realität | Virtual reality | 0.99 | 2 | 3 | 1 | proposed |
| Zero-Knowledge-Beweise | Zero-Knowledge Proofs | 0.93 | 1 | 4 | 0 | proposed |
| Adaptive Schicht | adaptive layer | 0.97 | 2 | 2 | 0 | proposed |
| Semantischer Disconnect | Alignment Faking | 0.97 | 2 | 2 | 2 | stated in 1 doc(s) ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:L55] |
| Anhedonie | Anhedonia | 0.91 | 3 | 1 | 1 | proposed |
| Anomalieerkennung | Anomaly Detection | 0.99 | 3 | 1 | 0 | proposed |
| Anthropisches Prinzip | Anthropic Principle | 1.00 | 1 | 3 | 0 | proposed |
| Arbeiter | Worker | 0.85 | 3 | 1 | 0 | proposed |
| Aufseher | Overseer | 0.94 | 3 | 1 | 0 | proposed |
| Autopoietische Schließung | autopoietic closure | 0.82 | 3 | 1 | 0 | proposed |
| Weltenbaum | Axis Mundi | 1.00 | 2 | 2 | 2 | stated in 1 doc(s) ^[tattoo-konzept-symbolik-trauma-heilung.md:L32] |
| Theorie der Glaubensrevision | Belief Revision Theory | 1.00 | 2 | 2 | 2 | stated in 2 doc(s) ^[logik-trifft-transzendente-entitaet.md:L91] ^[logik-trifft-transzendente-entitaet-2.md:L91] |
| Glocke | Bell Jar | 1.00 | 2 | 2 | 1 | stated in 1 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L1050] |
| Beobachter-Effekt | observer effect | 0.98 | 2 | 2 | 0 | proposed |
| Beweiser | prover | 0.99 | 2 | 2 | 1 | proposed |
| Leibwächter | Bodyguard | 0.96 | 1 | 3 | 0 | proposed |
| Grenzfestung | Border Fortress | 1.00 | 1 | 3 | 0 | proposed |
| Kind-Alter | Child Alter | 0.88 | 2 | 2 | 0 | proposed |
| Chronometrische Agnosie | Verlust des Zeitgefühls | 0.89 | 1 | 3 | 1 | stated in 1 doc(s) ^[storyforms-system-mind-bewusstsein.md:L104] |
| Modell des Bewusstseins | Consciousness Model | 0.87 | 3 | 1 | 0 | proposed |
| Konstitutionelle KI | Constitutional AI | 1.00 | 1 | 3 | 1 | proposed |
| Konstruktstadt | Construct-City | 0.99 | 1 | 3 | 0 | proposed |
| Widerspruchserkennung | Contradiction-Detection | 0.90 | 2 | 2 | 0 | proposed |
| Conway Gruppe | Conway group | 1.00 | 1 | 3 | 1 | proposed |
| DNA-Methylierung | DNA methylation | 0.99 | 3 | 1 | 1 | proposed |
| Daoismus | Daoism | 0.89 | 2 | 2 | 0 | proposed |
| Daoismus | Taoism | 0.99 | 2 | 2 | 1 | proposed |
| Dateisystem | File System | 0.94 | 3 | 1 | 0 | proposed |
| Todestrieb | Death drive | 0.99 | 3 | 1 | 1 | proposed |
| Der Tiefpunkt | Rock Bottom | 0.97 | 2 | 2 | 0 | proposed |
| Entwicklungstrauma | Developmental Trauma | 0.93 | 3 | 1 | 1 | stated in 1 doc(s) ^[trauma-archaeologie-interdisziplinaere-konzeptentwicklung-do.md:L89] |
| Entwicklungstrauma | Developmental trauma | 0.99 | 3 | 1 | 1 | proposed |
| Domäne Physics | Domain Physics | 0.97 | 1 | 3 | 0 | proposed |
| Echtzeit-Selbstverifikation | Real-time self-verification | 0.94 | 1 | 3 | 0 | proposed |
| Emergentismus | Emergentism | 0.97 | 2 | 2 | 2 | proposed |
| Emotionalen Teil | emotional part | 0.91 | 2 | 2 | 0 | proposed |
| Emotionalen Teils | emotional part | 0.92 | 2 | 2 | 0 | proposed |
| Emotionsfokussierte Paartherapie | Emotionally Focused Couples Therapy | 0.97 | 2 | 2 | 2 | proposed |
| Erlebte Fragmentierung | Experienced Fragmentation | 1.00 | 3 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L56]; proposed |
| Erlebte Rede | Free Indirect Discourse | 1.00 | 3 | 1 | 1 | stated in 1 doc(s) ^[kernwelten-und-fragmentierte-wahrnehmung.md:L64] ^[kernwelten-und-fragmentierte-wahrnehmung.md:L294] |
| Erzählform | Narrative Form | 0.88 | 3 | 1 | 0 | proposed |
| Eternalismus | Eternalism | 0.88 | 3 | 1 | 0 | proposed |
| Eternalismus | eternalism | 1.00 | 3 | 1 | 0 | proposed |
| Exekutive Steuerung | executive control | 0.96 | 1 | 3 | 0 | proposed |
| Existenzieller Horror | Existential Horror | 0.98 | 3 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L369]; proposed |
| existenzieller Horror | Existential Horror | 0.91 | 3 | 1 | 0 | proposed |
| Existenzielle Krise | Existential crisis | 0.98 | 2 | 2 | 0 | proposed |
| Existenzielle Leere | existential void | 0.80 | 3 | 1 | 0 | proposed |
| Fight-Reaktion | Fight Response | 0.95 | 1 | 3 | 1 | proposed |
| Vier Kernwelten | Four Core Worlds | 0.96 | 2 | 2 | 0 | proposed |
| Fundamentalismus | Fundamentalism | 0.90 | 3 | 1 | 1 | proposed |
| Fundiertes Reagieren | Grounded Responding | 1.00 | 2 | 2 | 2 | stated in 2 doc(s) ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L193] ^[beziehungsheilung-nach-trauma-konzeptpapier-3.md:L199] |
| Garten Eden | Garden of Eden | 1.00 | 2 | 2 | 2 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L298]; proposed |
| Genesis-Event | Origin-Trauma | 0.89 | 2 | 2 | 1 | stated in 1 doc(s) ^[charakter-kompilation-fuer-kohaerenz-protokoll.md:L355] |
| Glitch-Ästhetik | glitch aesthetics | 0.82 | 2 | 2 | 0 | proposed |
| Zielabweichung | Goal Drift | 1.00 | 2 | 2 | 2 | stated in 2 doc(s) ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L341] ^[aegis-genesis-krise-prosa-auftrag-formulieren-2.md:L341]; proposed |
| harter Schnitt | Hard Cut | 0.96 | 3 | 1 | 0 | proposed |
| Hitzetod | Heat death | 0.96 | 3 | 1 | 0 | proposed |
| Hyperrealität | Hyperreality | 1.00 | 3 | 1 | 0 | proposed |
| Inkommensurabilität | Incommensurability | 0.95 | 3 | 1 | 1 | stated in 1 doc(s) ^[risikoanalysebericht-eine-systematische-bewertung-der-bedroh.md:L23]; proposed |
| Unvermeidbarkeit | Inevitability | 0.98 | 2 | 2 | 0 | proposed |
| Innere Helferin | inner helper | 1.00 | 3 | 1 | 0 | proposed |
| instrumentelle Konvergenz | Instrumental Convergence | 0.99 | 2 | 2 | 0 | proposed |
| Interne Barrieren | Internal Barriers | 1.00 | 3 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L110]; proposed |
| interne Vermittlung | Internal Mediation | 0.95 | 1 | 3 | 1 | proposed |
| Introjektion | Introjection | 0.93 | 2 | 2 | 0 | proposed |
| Introjektion | introjection | 0.97 | 2 | 2 | 0 | proposed |
| Kachelproblem | Tiling Problem | 0.99 | 2 | 2 | 2 | stated in 1 doc(s) ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:L76] |
| Konzept der Leerheit | Sunyata | 0.99 | 1 | 3 | 1 | stated in 1 doc(s) ^[aegis-philosophische-und-systemtheoretische-analyse-docx.md:L27] |
| Liebhaber | Lover | 0.95 | 2 | 2 | 2 | proposed |
| Liminalität | Liminality | 0.98 | 3 | 1 | 1 | proposed |
| Liminalität | liminality | 1.00 | 3 | 1 | 1 | proposed |
| Logische Konsistenzanalyse | Logical Consistency Analysis | 0.96 | 2 | 2 | 0 | proposed |
| Logotherapie | Logotherapy | 0.99 | 2 | 2 | 1 | proposed |
| Schleifenquantengravitation | Loop quantum gravity | 1.00 | 3 | 1 | 1 | proposed |
| MESI-Protokoll | MESI protocol | 0.98 | 2 | 2 | 1 | proposed |
| Viele-Welten-Interpretation | Many Worlds Interpretation | 1.00 | 3 | 1 | 0 | proposed |
| Viele-Welten-Interpretation | Many-Worlds-Interpretation | 1.00 | 3 | 1 | 0 | proposed |
| Viele-Welten-Interpretation | Many-worlds interpretation | 1.00 | 3 | 1 | 0 | proposed |
| Markov-Decke | Markov Blanket | 0.85 | 2 | 2 | 1 | proposed |
| Sinnhaftes Ausharren | Meaningful Endurance | 1.00 | 2 | 2 | 2 | stated in 2 doc(s) ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L194] ^[beziehungsheilung-nach-trauma-konzeptpapier-3.md:L200] |
| Mereologie | Mereology | 0.91 | 3 | 1 | 1 | proposed |
| Mereologie | Teil-Ganzes-Beziehungen | 0.90 | 3 | 1 | 1 | stated in 1 doc(s) ^[paradoxien-der-kohaerenz-protokoll-entwicklung.md:L44] |
| Metaebene | Meta-level | 0.99 | 2 | 2 | 0 | proposed |
| Methode der Loci | Method of loci | 1.00 | 2 | 2 | 2 | proposed |
| Milieukontrolle | environmental control | 0.99 | 3 | 1 | 0 | proposed |
| Missverständnis und Fehl-Einstimmung | Misattunement | 1.00 | 2 | 2 | 2 | stated in 2 doc(s) ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L286] ^[beziehungsheilung-nach-trauma-konzeptpapier-3.md:L292] |
| Mischen | Mixing | 0.98 | 3 | 1 | 0 | proposed |
| Moralische Ambiguität | Moral Ambiguity | 1.00 | 2 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L308]; proposed |
| NP-Schwer | NP-hard | 1.00 | 1 | 3 | 1 | stated in 1 doc(s) ^[p-vs-np-und-kohaerenz.md:L78]; proposed |
| Negativraum | Negative Space | 0.98 | 3 | 1 | 1 | proposed |
| Negativraum | Negative space | 0.99 | 3 | 1 | 1 | proposed |
| Netzweber | Systemmanipulator | 0.83 | 3 | 1 | 1 | stated in 1 doc(s) ^[kernwelten-fuer-kohaerenz-protokoll.md:L473] |
| Nicht-Algorithmischem | non-algorithmic | 0.98 | 1 | 3 | 0 | proposed |
| Nicht-Schaden | Non-Malefizienz | 0.98 | 2 | 2 | 2 | stated in 1 doc(s) ^[dis-diagnose-klinische-ethische-rechtliche-analyse.md:L174] ^[dis-diagnose-klinische-ethische-rechtliche-analyse.md:L178] |
| Null Entropie | Verlustfreie Erhaltung | 0.82 | 2 | 2 | 2 | stated in 2 doc(s) ^[dramatica-storyform-synthese-aegis-verortung.md:L34] ^[kohaerenz-protokoll-audit-und-verifizierung.md:L46] |
| Objektiver Reduktion | Objective Reduction | 0.99 | 1 | 3 | 0 | proposed |
| Ontologische Enthüllung | Ontological Revelation | 1.00 | 3 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L353]; proposed |
| Ursprungsparadoxon | Origin Paradox | 1.00 | 3 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L47] |
| Ortsbindung | Place Attachment | 1.00 | 2 | 2 | 2 | stated in 2 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung-2.md:L342] ^[roman-lokalitaeten-konzept-und-ausarbeitung-3.md:L343]; proposed |
| Ortsidentität | Place Identity | 1.00 | 2 | 2 | 2 | stated in 2 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung-2.md:L342] ^[roman-lokalitaeten-konzept-und-ausarbeitung-3.md:L343]; proposed |
| Paradox des Haufens | Sorites-Paradox | 0.93 | 1 | 3 | 1 | stated in 1 doc(s) ^[parakonsistenz-aegis-und-nicht-existenz.md:L97] |
| Photonensphäre | photon sphere | 1.00 | 3 | 1 | 0 | proposed |
| prädiktive Verarbeitung | Predictive Processing | 0.97 | 1 | 3 | 0 | proposed |
| Quellenkritik | Provenance and Bias Analysis | 1.00 | 2 | 2 | 2 | stated in 2 doc(s) ^[aegis-manifest-genesis-krise-reboot.md:L151] ^[aegis-manifest-genesis-krise-reboot-2.md:L232] |
| Quanten-Verschränkungs-Witness | Quantum-Entanglement Witness | 1.00 | 3 | 1 | 0 | proposed |
| Quantenbits | qubits | 0.85 | 1 | 3 | 0 | proposed |
| Subtile Wettlaufsituationen | Race Conditions | 1.00 | 1 | 3 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L215] |
| Wettlaufsituationen | Race Conditions | 0.98 | 1 | 3 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L69] |
| Rekonsolidierung | Reconsolidation | 0.98 | 2 | 2 | 2 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L372]; proposed |
| Rekursive Selbstverifikation | Recursive Self-Verification | 1.00 | 2 | 2 | 0 | proposed |
| Weg der Prüfungen | Road of Trials | 0.88 | 3 | 1 | 1 | proposed |
| Romanze | Romance | 0.94 | 1 | 3 | 0 | proposed |
| sicherer Hafen | Safe Haven | 0.88 | 3 | 1 | 0 | proposed |
| Salienz | Salience | 0.91 | 3 | 1 | 0 | proposed |
| Salienz | salience | 0.87 | 3 | 1 | 0 | proposed |
| Schwellenhüter | Threshold Guardian Trope | 0.97 | 2 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptentwicklung.md:L169] |
| Suchender | Seeker | 0.95 | 3 | 1 | 0 | proposed |
| Selbst-Transzendenz | self-transcendence | 0.96 | 1 | 3 | 0 | proposed |
| Sexualisierter EP | Sexualized EP | 0.99 | 2 | 2 | 0 | proposed |
| Signifikat | signified | 0.89 | 2 | 2 | 0 | proposed |
| Simulierte Realität | Simulated Reality | 1.00 | 1 | 3 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L368]; proposed |
| Zustand der Kohärenz | State of Coherence | 0.97 | 3 | 1 | 0 | proposed |
| Subagenten | sub-agents | 0.97 | 1 | 3 | 0 | proposed |
| Über-Ich | Superego | 1.00 | 3 | 1 | 1 | stated in 1 doc(s) ^[narrative-physik-attraktoren-leserbewusstsein.md:L89]; proposed |
| systemische Anomalie | Systemic Anomaly | 0.89 | 2 | 2 | 0 | proposed |
| Systemischer Konflikt | Systemic Conflict | 0.99 | 1 | 3 | 0 | proposed |
| Systemische Intervention | systemic intervention | 1.00 | 3 | 1 | 0 | proposed |
| TSDP-Fragmentierung | TSDP fragmentation | 0.98 | 2 | 2 | 0 | proposed |
| Telefon-Stille | silent phone | 0.99 | 3 | 1 | 0 | proposed |
| Theseus-Schiff | Theseus paradox | 0.97 | 1 | 3 | 0 | proposed |
| nicht entscheidbar | UNDECIDABLE | 0.93 | 2 | 2 | 0 | proposed |
| Unbeabsichtigte Folgen | Unintended Consequences | 1.00 | 2 | 2 | 1 | proposed |
| Unzuverlässige Erzählung | unreliable narrative | 0.98 | 3 | 1 | 0 | proposed |
| Wertschätzung des Unvollkommenen | Wabi-Sabi | 0.84 | 1 | 3 | 1 | stated in 1 doc(s) ^[roman-finale-ethik-existenz-schoepfer-geschoepf-beziehung.md:L152] |
| Zeuge-Funktion | witness function | 0.82 | 2 | 2 | 0 | proposed |
| Absoluter Nullpunkt | absolute zero | 0.89 | 1 | 2 | 0 | proposed |
| Aktive Agentschaft | Active Agency | 1.00 | 1 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L164] |
| Adaptive Komplexität | Erforderliche Varietät | 0.81 | 1 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptionelle-ausarbeitung.md:L406] |
| algorithmisch irreduzibel | Algorithmically Irreducible | 1.00 | 2 | 1 | 0 | proposed |
| Totaler Krieg | All-Out War | 1.00 | 2 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L485]; proposed |
| Allgemeine Systemtheorie | General Systems Theory | 0.97 | 2 | 1 | 1 | proposed |
| Ambivalenz der Ordnung | Ambivalence of Order | 1.00 | 2 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L335]; proposed |
| Anisotropie | Anisotropy | 0.95 | 2 | 1 | 1 | proposed |
| Apophatische Theologie | Negative Theology | 0.90 | 1 | 2 | 1 | proposed |
| Bindungsschrei | Attachment-Cry | 0.89 | 2 | 1 | 0 | proposed |
| Aussicht | Prospect | 1.00 | 2 | 1 | 1 | stated in 1 doc(s) ^[lokalitaeten-konzept-fuer-roman-simulation.md:L55]; proposed |
| Authentische Heilung | true healing | 0.86 | 1 | 2 | 0 | proposed |
| Verbannte | Banished | 0.96 | 2 | 1 | 0 | proposed |
| Beginnende Ko-Präsenz | Incipient Co-Presence | 1.00 | 2 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L137]; proposed |
| Behandlung traumatischer Erinnerungen | Treatment of Traumatic Memories | 0.98 | 2 | 1 | 0 | proposed |
| Beschützer ANP | Protector ANP | 0.97 | 1 | 2 | 0 | proposed |
| Bifurkationstheorie | Bifurcation theory | 0.97 | 2 | 1 | 1 | proposed |
| Bindungsdichte | binding density | 1.00 | 2 | 1 | 0 | proposed |
| Mahayana-Mitgefühl | Bodhicitta | 0.94 | 2 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md.md:L732] |
| Cache-Invalidierung | Cache Invalidation | 0.97 | 2 | 1 | 1 | proposed |
| zentrale Achse | Central Axis | 0.96 | 2 | 1 | 1 | proposed |
| Höhepunkt der Charakterentwicklung | Character Development Climax | 1.00 | 2 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L499]; proposed |
| Chronist | Chronicler | 0.96 | 2 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L410]; proposed |
| Theorie der kognitiven Dissonanz | Cognitive Dissonance Theory | 1.00 | 1 | 2 | 1 | proposed |
| Kern der Kohärenz | Coherence-Kernel | 0.98 | 2 | 1 | 0 | proposed |
| Komputationalismus | Computationalism | 0.97 | 2 | 1 | 0 | proposed |
| Nebenläufigkeit | Concurrency | 1.00 | 1 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L69]; proposed |
| Conformal Field Theories | Konforme Feldtheorien | 0.95 | 1 | 2 | 0 | proposed |
| Organisatorische Schließung | Constraint Closure | 0.97 | 1 | 2 | 1 | stated in 1 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L210] |
| Semantischer Drift | Context Bias | 0.93 | 2 | 1 | 1 | stated in 1 doc(s) ^[ki-narrative-kollaps-kohaerenz-paradoxie.md:L40] |
| Korrespondenzfehler | Correspondence Error | 1.00 | 2 | 1 | 0 | proposed |
| Schwellenüberschreitung | Crossing Threshold | 0.97 | 2 | 1 | 0 | proposed |
| Dämpfer | Dampeners | 0.88 | 2 | 1 | 1 | proposed |
| Daten-Nutzlast | Data-Payload | 0.88 | 2 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L53]; proposed |
| Defamiliarisierung | Defamiliarization | 0.95 | 1 | 2 | 1 | proposed |
| Vertikal | Dependent Pairs | 0.86 | 1 | 2 | 1 | stated in 1 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L60] |
| Verzeichnis-basierte Protokolle | Directory-based | 0.99 | 1 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L81] |
| dissoziierter Zustand | Dissociated State | 0.80 | 2 | 1 | 0 | proposed |
| Domäne Mind | Domain Mind | 0.97 | 1 | 2 | 0 | proposed |
| Domäne Universe | Domain Universe | 0.97 | 1 | 2 | 0 | proposed |
| Doppelter Boden | Double Bottom | 1.00 | 2 | 1 | 1 | stated in 1 doc(s) ^[the-architecture-of-fracture-a-compendium-of-the-kael-system.md:L40]; proposed |
| Dramatische Ironie | Dramatic Irony | 1.00 | 2 | 1 | 1 | proposed |
| Dual-Kernel-Modell | Dual Kernel Model | 0.93 | 2 | 1 | 0 | proposed |
| Einer Quantenfeldtheorie | quantum field theory | 1.00 | 2 | 1 | 0 | proposed |
| Eliminativismus | Eliminativism | 0.87 | 2 | 1 | 0 | proposed |
| Eliminativismus | eliminativism | 0.97 | 2 | 1 | 0 | proposed |
| Emotionale Teile | Emotional parts | 0.80 | 2 | 1 | 0 | proposed |
| Emotionaler Teil | emotional part | 0.99 | 1 | 2 | 0 | proposed |
| Enaktive | enactive | 0.94 | 1 | 2 | 0 | proposed |
| Entmischung | Unblending | 1.00 | 1 | 2 | 1 | stated in 1 doc(s) ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L98]; proposed |
| Entropische Bedrohung | entropic threat | 0.91 | 2 | 1 | 0 | proposed |
| Entropische Gravitation | entropic gravity | 1.00 | 2 | 1 | 1 | proposed |
| Erhabene | the sublime | 0.95 | 2 | 1 | 0 | proposed |
| Erkenntnissen der Standpunkttheorie | Standpoint Theory | 0.99 | 1 | 2 | 1 | stated in 1 doc(s) ^[risikoanalysebericht-eine-systematische-bewertung-der-bedroh.md:L97] |
| Erlösungsbogen | Redemption Arc | 1.00 | 2 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L411]; proposed |
| Ethik der Fürsorge | Ethics of care | 0.99 | 2 | 1 | 0 | proposed |
| Komparator | Evaluator | 0.80 | 1 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptionelle-ausarbeitung.md:L386] |
| Existenzielles Risiko | Existential risk | 0.93 | 1 | 2 | 0 | proposed |
| Existenzielle Krise | existential crisis | 1.00 | 2 | 1 | 0 | proposed |
| Äußere Rahmung | External Framing | 1.00 | 1 | 2 | 1 | stated in 1 doc(s) ^[narrative-modelle-und-dramatica-erweiterung.md:L239] |
| Falscher Erfolg | false success | 0.99 | 2 | 1 | 0 | proposed |
| Finale Transformation | Final Transformation | 0.97 | 2 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L362]; proposed |
| Fixierte Einstellung | fixed attitude | 1.00 | 2 | 1 | 0 | proposed |
| Negative Theology | Framework of Apophatic Metaphysics | 0.90 | 2 | 1 | 1 | stated in 1 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L651] |
| Freie indirekte Rede | Free Indirect Discourse | 1.00 | 2 | 1 | 0 | proposed |
| Freeze-Reaktion | Freeze response | 0.90 | 2 | 1 | 0 | proposed |
| Funktionalist | Functionalist | 0.93 | 1 | 2 | 0 | proposed |
| Fundamentale Transformation | fundamental transformation | 0.95 | 2 | 1 | 0 | proposed |
| Fundamentalität | Fundamentality | 0.94 | 2 | 1 | 1 | proposed |
| Trichter | Funnels | 1.00 | 2 | 1 | 1 | proposed |
| Gedächtnislöschung | memory erasure | 0.81 | 2 | 1 | 0 | proposed |
| Gekoppelte Oszillatoren | coupled oscillators | 1.00 | 2 | 1 | 1 | proposed |
| Gelebte Integration | Lived Integration | 1.00 | 2 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L389] |
| Großen Vereinheitlichten Theorie | Grand Unified Theory | 0.99 | 2 | 1 | 1 | proposed |
| Grenzen Formaler Systeme | limits of formal systems | 0.94 | 1 | 2 | 0 | proposed |
| Göttin | goddess | 0.85 | 2 | 1 | 1 | proposed |
| Hermeneutik | Hermeneutics | 1.00 | 2 | 1 | 1 | proposed |
| Holarchie | Holarchy | 0.92 | 2 | 1 | 0 | proposed |
| Hyperaktivitätsstörung | Hyperactivity Disorder | 0.97 | 1 | 2 | 0 | proposed |
| I-Perspektive | first-person perspective | 0.96 | 1 | 2 | 0 | proposed |
| OVERWORLD | INSTANTIATION OF THE ÜBERWELT | 0.97 | 2 | 1 | 1 | stated in 1 doc(s) ^[aegis-manifest-genesis-krise-reboot-2.md:L85] |
| Imaginäre | Imaginary | 0.98 | 2 | 1 | 1 | proposed |
| Imaginäre | imaginary | 1.00 | 2 | 1 | 1 | proposed |
| Inequities | Persönliche Dissonanzen | 1.00 | 2 | 1 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L67] |
| Informationszerstörung | Information Destruction | 0.87 | 2 | 1 | 0 | proposed |
| Innere Konferenz | Runder Tisch | 0.90 | 2 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-prozess-grundlagen.md:L114] |
| Innere Rahmung | Internal Framing | 1.00 | 1 | 2 | 1 | stated in 1 doc(s) ^[narrative-modelle-und-dramatica-erweiterung.md:L242]; proposed |
| Innere Verarbeitung | Internal Processing | 1.00 | 1 | 2 | 1 | stated in 1 doc(s) ^[narrative-modelle-und-dramatica-erweiterung.md:L241]; proposed |
| Integrationswiderstand | Integration Resistance | 1.00 | 2 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L236]; proposed |
| Internalisierung des Täter-Protokolls | Introjektion | 0.92 | 1 | 2 | 1 | stated in 1 doc(s) ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L589] |
| JSON-Objekt | JSON object | 0.95 | 2 | 1 | 0 | proposed |
| Kernparadoxie | core paradox | 0.85 | 1 | 2 | 0 | proposed |
| Ko-Regulation | co-regulation | 0.96 | 2 | 1 | 0 | proposed |
| Kobra-Effekt | Unbeabsichtigte Folgen | 0.95 | 1 | 2 | 1 | stated in 1 doc(s) ^[aegis-paradoxon-neukonzeption-und-analyse-docx.md:L42] |
| Konvention T | T-Schema | 0.94 | 1 | 2 | 1 | stated in 1 doc(s) ^[wahrheitstheorien-kohaerenz-vs-korrespondenz.md:L210] |
| Konzepts der Markov-Decke | Markov Blanket | 0.82 | 1 | 2 | 1 | stated in 1 doc(s) ^[roman-entwicklung-ontologie-trauma-horror.md:L25] |
| Langzeitgedächtnis | long-term memory | 0.99 | 2 | 1 | 0 | proposed |
| Stufenaufstieg | Level Up | 1.00 | 1 | 2 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L425] |
| Liminaler Raum | Liminal space | 0.98 | 1 | 2 | 1 | proposed |
| Sperre | Lock Acquisition | 0.85 | 2 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L192] |
| Logik des Traumas | Logic of Trauma | 0.98 | 1 | 2 | 0 | proposed |
| Logotherapie | logotherapy | 0.99 | 2 | 1 | 1 | proposed |
| Memetik | Memetics | 0.93 | 1 | 2 | 1 | proposed |
| Mentorenfigur | mentor | 0.94 | 1 | 2 | 0 | proposed |
| metaphysische Ebene | Metaphysical Dimension | 0.87 | 2 | 1 | 0 | proposed |
| Metaphysische Ebene | metaphysical level | 1.00 | 2 | 1 | 0 | proposed |
| moralische Ambiguität | Moral Ambiguity | 0.92 | 1 | 2 | 1 | proposed |
| Neurodivergenz | neurodivergence | 0.98 | 1 | 2 | 0 | proposed |
| Nicht entscheidbar | UNDECIDABLE | 1.00 | 1 | 2 | 0 | proposed |
| Nicht-Schaden | Non-Maleficence | 0.99 | 2 | 1 | 0 | proposed |
| Ontische Strukturelle Realismus | Ontic Structural Realism | 0.99 | 1 | 2 | 0 | proposed |
| Ontischen Strukturellen Realismus | Ontic Structural Realism | 0.87 | 1 | 2 | 0 | proposed |
| Ontologische Reibung | Ontological Friction | 1.00 | 2 | 1 | 1 | proposed |
| Parasympathikus | parasympathetic | 1.00 | 2 | 1 | 0 | proposed |
| Peripetie | Umschwung | 0.98 | 2 | 1 | 1 | stated in 1 doc(s) ^[aegis-paradoxon-konzeption-und-analyse.md:L55] |
| Täterintrojekte | Perpetrator Introjects | 1.00 | 2 | 1 | 1 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L113] |
| Philosophische Zombies | philosophical zombies | 0.94 | 2 | 1 | 0 | proposed |
| Verspielte | Playful | 0.85 | 1 | 2 | 0 | proposed |
| Potentialraum | Potential Space | 1.00 | 2 | 1 | 1 | proposed |
| Problem des Anderen | Problem of the Other | 0.97 | 2 | 1 | 1 | proposed |
| Prozedurale Generierung | Procedural Generation | 1.00 | 1 | 2 | 1 | proposed |
| Strafenden | Punitive | 0.98 | 2 | 1 | 1 | proposed |
| Quantenbits | Qubits | 0.83 | 1 | 2 | 1 | stated in 1 doc(s) ^[existenzforschung-fuer-roman-kohaerenz-protokoll.md:L174]; proposed |
| Quarantäne-Raum | quarantine room | 0.89 | 1 | 2 | 0 | proposed |
| Reader-Response-Theorie | Reader-Response Theory | 0.97 | 1 | 2 | 0 | proposed |
| Rekonsolidierung | reconsolidation | 1.00 | 2 | 1 | 1 | proposed |
| Rekursive Selbstverifikation | recursive self-verification | 1.00 | 2 | 1 | 0 | proposed |
| Wiederholungszwang | Repetition Compulsion | 0.97 | 2 | 1 | 0 | proposed |
| Slingshot-Arguments | Steinschleuder | 1.00 | 1 | 2 | 1 | stated in 1 doc(s) ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:L33] |
| Sonifikation | Sonification | 0.95 | 2 | 1 | 1 | proposed |
| Sonifikation | sonification | 0.95 | 2 | 1 | 1 | proposed |
| Spontane Symmetriebrechung | Spontaneous Symmetry Breaking | 1.00 | 2 | 1 | 1 | proposed |
| Standpunkttheorie | Standpoint Theory | 1.00 | 1 | 2 | 1 | proposed |
| Statistische Manual Psychischer Störungen | Statistical Manual of Mental Disorders | 0.95 | 2 | 1 | 0 | proposed |
| Steinschleuder | slingshot | 1.00 | 2 | 1 | 1 | proposed |
| Strukturellen Realismus | Structural realism | 0.93 | 2 | 1 | 1 | proposed |
| Subagenten | Sub-agents | 0.95 | 1 | 2 | 0 | proposed |
| Supersymmetrie | Supersymmetry | 1.00 | 1 | 2 | 1 | proposed |
| Symbolische Ordnung | symbolic order | 1.00 | 2 | 1 | 1 | proposed |
| Synergetik | Synergetics | 0.86 | 1 | 2 | 0 | proposed |
| Systemische Anomalie | Systemic Anomaly | 1.00 | 1 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L146]; proposed |
| Systemische Verantwortungsübernahme | Systemic Responsibility | 1.00 | 2 | 1 | 1 | stated in 1 doc(s) ^[the-minds-behind-the-machine-a-psychological-guide-to-system.md:L52] |
| Systemische Anomalie | systemic anomaly | 1.00 | 1 | 2 | 0 | proposed |
| Systemresilienz | system robustness | 0.93 | 2 | 1 | 0 | proposed |
| ÜBERWELT | THE DIGITAL OVERWORLD | 1.00 | 2 | 1 | 1 | stated in 1 doc(s) ^[aegis-genesis-crisis-self-definition.md:L97] |
| Telos | Ultimativer | 0.93 | 1 | 2 | 1 | stated in 1 doc(s) ^[aegis-singularitaet-jenseits-entropiegleichung-2.md:L54] |
| Verführerin | Temptress | 0.95 | 1 | 2 | 0 | proposed |
| Theorie der Berechenbarkeit | computability theory | 1.00 | 2 | 1 | 1 | proposed |
| verdrehte Module | Twisted Modules | 0.98 | 1 | 2 | 0 | proposed |
| Unentscheidbar | UNDECIDABLE | 0.98 | 1 | 2 | 0 | proposed |
| Umwelt-Erzählung | environmental story | 1.00 | 1 | 2 | 0 | proposed |
| Unbeabsichtigte Folgen | unintended consequences | 0.99 | 2 | 1 | 1 | proposed |
| unbeabsichtigte Konsequenzen | Unintended Consequences | 0.91 | 1 | 2 | 0 | proposed |
| V-Beziehung | V relationship | 0.97 | 1 | 2 | 0 | proposed |
| Verbannte | banished | 0.92 | 2 | 1 | 0 | proposed |
| Verifizierbare Berechnung | verifiable computation | 1.00 | 1 | 2 | 0 | proposed |
| Virtuelle Realität | virtual reality | 0.94 | 2 | 1 | 0 | proposed |
| Weißraum | Whitespace | 0.99 | 2 | 1 | 1 | stated in 1 doc(s) ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L737]; proposed |
| AEGIS Protokolle | AEGIS Protocols | 0.94 | 1 | 1 | 0 | proposed |
| Akzeptierte Komplexität | Accepted Complexity | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L398]; proposed |
| Adaptive Kontrolle | Adaptive Control | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[operationalizing-system-collapse-a-strategic-guide-to-aegis.md:L73] |
| Adaptive Komplexität | adaptive complexity | 0.94 | 1 | 1 | 0 | proposed |
| Adulte ADHS | Adult ADHD | 1.00 | 1 | 1 | 0 | proposed |
| Amnesie-Handlung | Amnesia Plot | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L141] |
| Buddhistisches Anatta | Anatta | 0.84 | 1 | 1 | 1 | proposed |
| Ankerheuristik | Anchoring Heuristic | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[risikoanalysebericht-eine-systematische-bewertung-der-bedroh.md:L47]; proposed |
| Angstüberwindung | Fear Transcendence | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L326] |
| Künstlicher Allgemeiner Intelligenz | Artificial general intelligence | 0.99 | 1 | 1 | 1 | proposed |
| Aufmerksamkeitsdefizit | Attention-Deficit | 0.99 | 1 | 1 | 0 | proposed |
| Ausfallmodus | Failure mode | 0.96 | 1 | 1 | 0 | proposed |
| Ausfallmodus | failure mode | 0.92 | 1 | 1 | 0 | proposed |
| Authentizitätskampf | Struggle for Authenticity | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L191] |
| Basisuntersuchungen | Mental Status Examination | 0.98 | 1 | 1 | 1 | stated in 1 doc(s) ^[dis-diagnose-klinische-ethische-rechtliche-analyse.md:L70] |
| Bedrohungsvektor | Threat Vector | 0.93 | 1 | 1 | 0 | proposed |
| Begleiter-Paar-Interferenz | Horizontale Beziehung | 0.90 | 1 | 1 | 1 | stated in 1 doc(s) ^[narrative-context-protocol-ncp-spezifikation.md:L72] |
| Belohnungs-Hacking | reward hacking | 0.95 | 1 | 1 | 1 | proposed |
| Bewusstseinsmodell | Consciousness Model | 1.00 | 1 | 1 | 0 | proposed |
| Bindung und Sicherheit | Safe Haven | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[charaktermodellierung-mit-aieos-schema.md:L122] |
| Bremser | Inhibitors | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L126] |
| CQ-Protokoll | CQ-Protocol | 0.90 | 1 | 1 | 1 | proposed |
| Cache Kohärenz Metapher | Cache Coherence Metaphor | 0.99 | 1 | 1 | 0 | proposed |
| Rückgrate | Candidate Storyforms | 0.86 | 1 | 1 | 1 | stated in 1 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L183] |
| Kartograf | Cartographer | 0.99 | 1 | 1 | 1 | proposed |
| Änderungspunkten | Change Point Detection | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-subplots-kapitelweise-system-exploration-docx.md:L182] |
| Charaktererkennung | Character Detection | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[entwicklungsstrategie-fuer-kohaerenz-protokoll.md:L39]; proposed |
| Charakter-System | Character System | 0.94 | 1 | 1 | 0 | proposed |
| Kohärenzkern | Coherence-Kernel | 0.81 | 1 | 1 | 0 | proposed |
| Komplexen Posttraumatischen Belastungsstörung | Complex Posttraumatic Stress Disorder | 0.83 | 1 | 1 | 1 | proposed |
| Konzept des Narrativen Systems | Concept of the Narrative System | 1.00 | 1 | 1 | 0 | proposed |
| Konzeptuelle Analogie | Conceptual Analogy | 0.98 | 1 | 1 | 0 | proposed |
| Konsolidierte Agentschaft | Consolidated Agency | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L281]; proposed |
| Kontext-Kompressions-Prompt | Context Compression Prompt | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[narrative-context-protocol-ncp-spezifikation.md:L165]; proposed |
| Kontrollierte Kreativität | Controlled Creativity | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L200]; proposed |
| kontrollierte Kreativität | Controlled Creativity | 0.83 | 1 | 1 | 0 | proposed |
| Kosmologische Konstante-Problem | Cosmological constant problem | 0.95 | 1 | 1 | 1 | proposed |
| DSM-Dissoziative Störungen | DSM Dissociative Disorders | 0.99 | 1 | 1 | 0 | proposed |
| Funnels | Dampeners | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L195] |
| Wahrheitsprotokoll | Dialetheism-Engine | 0.80 | 1 | 1 | 1 | stated in 1 doc(s) ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L201] |
| Die Aufhebung | Sublation | 1.00 | 1 | 1 | 0 | proposed |
| Dismissiv | Unsicher-Vermeidend | 0.89 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-thematische-tiefenanalyse.md:L138] |
| Doppel-IC | Double-IC | 0.87 | 1 | 1 | 0 | proposed |
| Doppelmuldenpotential | Double-Well Potential | 0.84 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L33]; proposed |
| EP Kollaps | EP Collapse | 0.94 | 1 | 1 | 0 | proposed |
| EP-Barrieren | EP barriers | 0.95 | 1 | 1 | 0 | proposed |
| Eichsymmetrien | Gauge Symmetries | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L112]; proposed |
| Elektroenzephalografie | Electroencephalography | 0.94 | 1 | 1 | 0 | proposed |
| Elektroenzephalographie | Electroencephalography | 0.97 | 1 | 1 | 0 | proposed |
| Elektroenzephalografie | electroencephalography | 0.99 | 1 | 1 | 0 | proposed |
| Elektroenzephalographie | electroencephalography | 1.00 | 1 | 1 | 0 | proposed |
| emergenter Raum | Emergent Space | 0.98 | 1 | 1 | 0 | proposed |
| Emergenten Ordnung | Emergent order | 0.97 | 1 | 1 | 0 | proposed |
| Emotionale Konfrontation | Emotional Confrontation | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L92]; proposed |
| emotionale Konfrontation | Emotional Confrontation | 0.91 | 1 | 1 | 0 | proposed |
| Emotionale Kohärenz | emotional coherence | 1.00 | 1 | 1 | 0 | proposed |
| Entropie-Architektur | Entropic Architecture | 0.99 | 1 | 1 | 0 | proposed |
| Erlösung des Bösewichts | Redeeming the Villain | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L569] |
| Ersatzmetrik-Ausnutzung | Proxy Gaming | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[optimierter-prompt-fuer-kohaerenz-protokoll.md:L146] |
| Erzwungene Allianz | Forced Alliance | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L239]; proposed |
| Ewige Objekte | eternal objects | 0.94 | 1 | 1 | 0 | proposed |
| Externalisierte Abwehr | Externalized Defense | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L128]; proposed |
| Externer Glitch | external glitch | 0.97 | 1 | 1 | 0 | proposed |
| Falschem Erwachen | False Awakenings | 0.90 | 1 | 1 | 1 | stated in 1 doc(s) ^[roman-entwicklung-ontologie-trauma-horror.md:L90] |
| Falscherinnerungen | false memories | 0.98 | 1 | 1 | 0 | proposed |
| Fern-vom-Gleichgewicht | Non-equilibrium | 0.95 | 1 | 1 | 0 | proposed |
| Fern-vom-Gleichgewicht | non-equilibrium | 0.97 | 1 | 1 | 0 | proposed |
| Fluss des Vergessens | Lethe-Strom | 0.87 | 1 | 1 | 1 | stated in 1 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L206] |
| Kraft der Fragmentierung | Force of Fragmentation | 0.99 | 1 | 1 | 0 | proposed |
| Vier Domänen | Four Domains | 0.99 | 1 | 1 | 0 | proposed |
| Framing-Effekt | Framing Effect | 0.86 | 1 | 1 | 1 | stated in 1 doc(s) ^[risikoanalysebericht-eine-systematische-bewertung-der-bedroh.md:L48]; proposed |
| Fundamentalen Realität | Fundamental reality | 0.88 | 1 | 1 | 0 | proposed |
| Fundamentalsatz der Arithmetik | Fundamental theorem of arithmetic | 1.00 | 1 | 1 | 1 | proposed |
| Fundamentalen Realität | fundamental reality | 0.98 | 1 | 1 | 0 | proposed |
| Fundamentalsatz der Arithmetik | fundamental theorem of arithmetic | 1.00 | 1 | 1 | 1 | proposed |
| Pilznetzwerk | Fungal Network | 0.83 | 1 | 1 | 0 | proposed |
| Fähigkeitenteilung | Skill Sharing | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L327] |
| Fühlende Umgebung | Sentient Environment | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L257]; proposed |
| Gedankenverschmelzung | Mind Meld | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L197] |
| Gegnermodellierung | opponent modeling | 0.99 | 1 | 1 | 1 | proposed |
| Generative Synthese | generative synthesis | 1.00 | 1 | 1 | 0 | proposed |
| Generative Systeme | generative systems | 0.95 | 1 | 1 | 0 | proposed |
| Gesunder Erwachsenenmodus | Healthy Adult Mode | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L171]; proposed |
| Wächter der KW1 | Guardian of KW1 | 1.00 | 1 | 1 | 0 | proposed |
| Hain der Symbole | Kreativ-Zone | 0.88 | 1 | 1 | 1 | stated in 1 doc(s) ^[orte-konzept-fuer-kohaerenz-protokoll.md:L316] ^[orte-konzept-fuer-kohaerenz-protokoll.md:L484] |
| Harter Schnitt | Hard Cut | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L1128]; proposed |
| Heldenhaftes Opfer | Heroic Sacrifice | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L526]; proposed |
| menschliches Feedback | Human Feedback | 0.91 | 1 | 1 | 0 | proposed |
| Ikarus-Paradox | Icarus paradox | 0.93 | 1 | 1 | 1 | proposed |
| Token Limit | Inference-Time Budget | 0.81 | 1 | 1 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L221] |
| innere Barrieren | Internal Barriers | 0.90 | 1 | 1 | 0 | proposed |
| Internes System | Internal system | 0.85 | 1 | 1 | 0 | proposed |
| Interpretation der Quantenmechanik | interpretation of quantum mechanics | 0.98 | 1 | 1 | 0 | proposed |
| Selbst-Realisierung | Kaels Finale Integration | 0.83 | 1 | 1 | 1 | stated in 1 doc(s) ^[m-als-fundament-der-simulation.md:L560] |
| Kampf um Authentizität | Struggle for Authenticity | 1.00 | 1 | 1 | 0 | proposed |
| Schlüsselteil | Key Part | 0.96 | 1 | 1 | 0 | proposed |
| Kohärenz-Erhaltung | coherence preservation | 0.97 | 1 | 1 | 0 | proposed |
| Konflikt der Wahrheitsmacher | Truthmaker Theory | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L187] |
| Konzept der Ontologischen Reibung | Ontological Friction | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[textanalyse-existenz-system-und-leid.md:L222] |
| Konzept der Theoriebeladenheit | Theory-Ladenness | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[risikoanalysebericht-eine-systematische-bewertung-der-bedroh.md:L19] |
| Konzeptuelle Analogie | Structure Mapping Theory | 0.87 | 1 | 1 | 1 | stated in 1 doc(s) ^[monstergruppe-babygruppe-und-kael.md:L143] |
| Korrelaten des Bewusstseins | correlates of consciousness | 0.96 | 1 | 1 | 1 | proposed |
| Kreativer Teil | creative part | 0.83 | 1 | 1 | 0 | proposed |
| Kuramoto-Modell | Kuramoto model | 0.98 | 1 | 1 | 1 | proposed |
| LOGISCHE PROTOKOLLE | logical protocols | 0.99 | 1 | 1 | 0 | proposed |
| Labyrinthläufer | Maze Runner | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L85] |
| Langsames Denken | Slow Thinking | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[ki-narrative-kollaps-kohaerenz-paradoxie.md:L128]; proposed |
| Narrative Sequenz | Lesereihenfolge | 0.94 | 1 | 1 | 1 | stated in 1 doc(s) ^[projektplanung-fuer-kohaerenz-protokoll.md:L288] |
| Logik-Paradoxon Anwendung | Logic Paradox Application | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L299] |
| Logik-Polizei | Logic Police | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L84]; proposed |
| Logik-Rätselbox | Logic Puzzle Box | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L256] |
| mehrwertige Logik | Many-Valued Logic | 0.84 | 1 | 1 | 0 | proposed |
| Membran Computing | Membrane Computing | 0.95 | 1 | 1 | 1 | proposed |
| Mentorenfigur | Mentor Figure | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L299] |
| Mentorenfigur | mentor figure | 0.98 | 1 | 1 | 0 | proposed |
| metaphysische Dimension | Metaphysical Dimension | 0.85 | 1 | 1 | 0 | proposed |
| Metaphysisches Subsystem | Metaphysical Subsystem | 0.98 | 1 | 1 | 0 | proposed |
| Metaphysik der Kausalität | Metaphysics of Causation | 0.98 | 1 | 1 | 0 | proposed |
| Mikrosprünge | Phasing | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[storyforms-system-mind-bewusstsein.md:L106] |
| Modelle der Posttraumatischen Reifung | Posttraumatic Growth | 0.95 | 1 | 1 | 1 | stated in 1 doc(s) ^[juna-kael-system-krisenanalyse-und-rettungsplan.md:L205] |
| Nachwirkende Leere | Resonant Void | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L371] |
| Narrative Generation Prompt | Narrations-Prompt | 0.97 | 1 | 1 | 1 | stated in 1 doc(s) ^[narrative-context-protocol-ncp-spezifikation.md:L166] |
| Narrative Ausrichtung | Narrative Alignment | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[narrative-modelle-und-dramatica-erweiterung.md:L222]; proposed |
| Notwendige Abwehr | Necessary Defense | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L74]; proposed |
| Neoplatonismus | Neoplatonism | 1.00 | 1 | 1 | 1 | proposed |
| Verschachtelte Realität | Nested Reality | 1.00 | 1 | 1 | 1 | proposed |
| verschachtelte Realität | Nested Reality | 0.99 | 1 | 1 | 1 | proposed |
| Non-Dualität | non-duality | 1.00 | 1 | 1 | 0 | proposed |
| Non-Lokalität | Non-locality | 0.97 | 1 | 1 | 0 | proposed |
| Non-Lokalität | non-locality | 0.97 | 1 | 1 | 0 | proposed |
| NullClaw | Zig | 0.84 | 1 | 1 | 1 | stated in 1 doc(s) ^[aieos-schema-fuer-ki-charaktere.md:L599] |
| Offene Konfrontation | Open Confrontation | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L290]; proposed |
| Ontologische Barometer | State Detection | 0.85 | 1 | 1 | 1 | stated in 1 doc(s) ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L191] |
| Organisationale Schließung | Organizational Closure | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-seele-und-entropie.md:L30]; proposed |
| Organisatorische Schließung | Organizational Closure | 1.00 | 1 | 1 | 0 | proposed |
| Überwacher | Overseer | 0.97 | 1 | 1 | 0 | proposed |
| Paradox-Motor | Paradox Engine | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-logik-in-der-leere-docx.md:L195]; proposed |
| Paradox-Enthüllung | Paradox Revelation | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L227]; proposed |
| Philosophical zombie | Philosophischer Zombie | 1.00 | 1 | 1 | 1 | proposed |
| Portal-Fantasie | Portal Fantasy | 0.87 | 1 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L211]; proposed |
| Pragmatische Wahrheitstheorie | Pragmatic Theory of Truth | 0.99 | 1 | 1 | 1 | proposed |
| Prompt-Funktionen | Prompt Functions | 0.82 | 1 | 1 | 1 | proposed |
| Psychologische Modularität | Psychological Modularity | 0.99 | 1 | 1 | 0 | proposed |
| Psychologische Theorie | Psychological Theory | 0.99 | 1 | 1 | 0 | proposed |
| Psychologische Resonanz | TSDP Dynamics | 0.85 | 1 | 1 | 1 | stated in 1 doc(s) ^[kernwelten-und-fragmentierte-wahrnehmung.md:L127] ^[kernwelten-und-fragmentierte-wahrnehmung.md:L169] |
| Punktuiertes Gleichgewicht | Punctuated Equilibrium | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L100]; proposed |
| Strafender Elternmodus | Punitive Parent Mode | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L170] |
| QBismus | Quanten-Bayesianismus | 0.92 | 1 | 1 | 1 | stated in 1 doc(s) ^[physik-fuer-simulierte-realitaet.md:L53] |
| Quanten-Bayesianismus | Quantum Bayesianism | 1.00 | 1 | 1 | 1 | proposed |
| Quantencomputation | quantum computation | 0.99 | 1 | 1 | 0 | proposed |
| Quantenunsicherheit | quantum uncertainty | 1.00 | 1 | 1 | 1 | proposed |
| Quantenvakuumzustand | Quantum vacuum state | 1.00 | 1 | 1 | 1 | proposed |
| Quarzstaublungenerkrankung | Silikose | 0.93 | 1 | 1 | 1 | stated in 1 doc(s) ^[juristische-recherche-zu-kptbs-dis.md:L680] |
| RIVE-Protokolle | Rekursive Integritätsprüfung | 0.82 | 1 | 1 | 1 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-protokoll.md:L168] |
| Wiedereintritt | Re-entry | 1.00 | 1 | 1 | 1 | proposed |
| Reaktionsbildung | Reaction Formation | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[ki-antagonist-fragmentierte-gottheit-analyse.md:L103]; proposed |
| Schutz und Versteckmöglichkeiten | Refuge | 0.96 | 1 | 1 | 1 | stated in 1 doc(s) ^[lokalitaeten-konzept-fuer-roman-simulation.md:L55] |
| Relationismus | relationism | 0.99 | 1 | 1 | 0 | proposed |
| Reproduzierbarkeitskrise | Reproducibility Crisis | 1.00 | 1 | 1 | 1 | proposed |
| Resonanzfeldtheorie | Resonance Field Theory | 0.98 | 1 | 1 | 1 | proposed |
| Resting-State-Aktivität | resting-state activity | 1.00 | 1 | 1 | 0 | proposed |
| Rundreiseproblem | traveling salesman problem | 1.00 | 1 | 1 | 0 | proposed |
| Räumliche Funktion | Spatial Function | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[lokalitaeten-konzept-fuer-roman-simulation.md:L80]; proposed |
| Räumliche Umschließung | Spatial Enclosure | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[lokalitaeten-konzept-fuer-roman-simulation.md:L79] |
| Räumliches Layout | Spatial Layout | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[lokalitaeten-konzept-fuer-roman-simulation.md:L81] |
| Salienz-Netzwerk | Salience Network | 1.00 | 1 | 1 | 0 | proposed |
| Schlaflähmung | Sleep Paralysis | 0.80 | 1 | 1 | 1 | stated in 1 doc(s) ^[roman-entwicklung-ontologie-trauma-horror.md:L90] |
| Schlafparalyse | Sleep Paralysis | 0.89 | 1 | 1 | 0 | proposed |
| Schwellenkonzepte | Threshold Concepts | 1.00 | 1 | 1 | 1 | proposed |
| Schwellenkonzepten | Threshold Concepts | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[narrativ-existenzieller-kohaerenz-nzt-protokoll.md:L189] |
| Sekundäre Dissoziation | Secondary Dissociation | 0.99 | 1 | 1 | 0 | proposed |
| sekundäre Dissoziation | Secondary Dissociation | 0.90 | 1 | 1 | 0 | proposed |
| sichere Basis | Secure Base | 0.85 | 1 | 1 | 1 | proposed |
| Selbstdiskrepanz | self-discrepancy | 1.00 | 1 | 1 | 1 | proposed |
| geteilte Daten | Shared Data | 0.98 | 1 | 1 | 1 | proposed |
| Zusammenbruch der Grundannahmen | Shattered Assumptions | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L166] |
| Soziale Phobie | Social Phobia | 0.94 | 1 | 1 | 1 | proposed |
| Upper Abdomen | Solar Plexus | 0.80 | 1 | 1 | 1 | stated in 1 doc(s) ^[tattoo-konzept-symbolik-trauma-heilung.md:L321] |
| Spiegel Alters | Vertical Symmetry Bridge | 0.94 | 1 | 1 | 1 | stated in 1 doc(s) ^[editorial-style-dossier-somatic-and-linguistic-implementatio.md:L40] |
| Zustandsanalyse-Prompt | State Analysis Prompt | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[narrative-context-protocol-ncp-spezifikation.md:L164]; proposed |
| Zustands-Aktualisierungs-Prompt | State Update Prompt | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[narrative-context-protocol-ncp-spezifikation.md:L167] |
| Stil-Anweisungen | Style Instructions | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[systemic-architecture-specification-the-coherence-protocol-w.md:L57] |
| Stilrichtlinien | Style Instructions | 0.94 | 1 | 1 | 0 | proposed |
| Strategische Angstbewältigung | Strategic Fear Management | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L254]; proposed |
| Sublation (Aufhebung) | Sublation | 0.99 | 1 | 1 | 1 | proposed |
| die Aufhebung | Sublation | 1.00 | 1 | 1 | 0 | proposed |
| Teilsummenproblem | Subset Sum | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[p-vs-np-und-kohaerenz.md:L66] |
| Überwachungskapitalismus | Surveillance capitalism | 0.99 | 1 | 1 | 1 | proposed |
| Symbolische Welt | World of Symbolism | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L126] |
| Synergetik | synergetics | 0.99 | 1 | 1 | 0 | proposed |
| Systemische Zyklen | Systemic Cycles | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L182]; proposed |
| Systemische Verantwortung | Systemic Responsibility | 0.95 | 1 | 1 | 0 | proposed |
| Tertiärer Struktureller Dissoziation | tertiary structural dissociation | 0.95 | 1 | 1 | 0 | proposed |
| Z-Buffer Fighting | Texture Flickering | 0.83 | 1 | 1 | 1 | stated in 1 doc(s) ^[gravitation-realitaet-simulation-wahrheit.md:L306] |
| Theorie der Vertex-Operator-Algebren | theory of vertex operator algebras | 0.95 | 1 | 1 | 0 | proposed |
| Theorie der Vertexoperatoralgebren | theory of vertex operator algebras | 0.83 | 1 | 1 | 0 | proposed |
| Topologischen Datenanalyse | Topological data analysis | 1.00 | 1 | 1 | 0 | proposed |
| Transaktionale Interpretation | Transactional interpretation | 0.98 | 1 | 1 | 1 | proposed |
| Transaktionale Interpretation | transactional interpretation | 1.00 | 1 | 1 | 1 | proposed |
| Unmappbarkeit | unmappable | 0.90 | 1 | 1 | 0 | proposed |
| Verifizierbare Berechnung | Verifiable Computation | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-philosophische-und-systemtheoretische-analyse-docx.md:L114]; proposed |
| Verletzlicher Kindmodus | Vulnerable Child Modes | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L169] |
| Verschränkungs-Analogie | entanglement analogy | 1.00 | 1 | 1 | 0 | proposed |
| Verwundete Aphrodite | Wounded Aphrodite | 1.00 | 1 | 1 | 1 | proposed |
| Vier Dimensionen | four dimensions | 0.96 | 1 | 1 | 0 | proposed |
| Wahrscheinlichkeitswellen | probability waves | 0.96 | 1 | 1 | 0 | proposed |
| Welt der Reinen Logik | world of pure logic | 0.96 | 1 | 1 | 0 | proposed |
| Weltzerstörender Höhepunkt | World-Shattering Climax | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L541]; proposed |
| Wähle-dein-eigenes-Abenteuer-Ende | Your Own Adventure Ending | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L582] |
| Zettelkasten-Methode | Zettelkasten method | 0.91 | 1 | 1 | 0 | proposed |
| Wiedereintritt | Konzept des Re-entry | 1.00 | 1 | 0 | 0 | stated in 1 doc(s) ^[textanalyse-existenz-system-und-leid.md:L178] |
| Prinzip des Nichtschadens | Non-Maleficence | 1.00 | 0 | 1 | 0 | stated in 1 doc(s) ^[dissoziative-identitaetsstoerung-unsichtbare-diagnose.md:L173] |

## Translations to read before trusting — 1311 below p 0.8

The sample checked on 2026-09-23 put the noise here: `Signposts`/`Transits` 0.63, `Subjective Story Throughline`/`We` 0.39.

| German | English | p | docs (de) | docs (en) | docs (both) | evidence |
|---|---|--:|--:|--:|--:|---|
| AEGIS | System | 0.61 | 269 | 309 | 245 | stated in 5 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L383] ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L252] |
| Ordnung | System | 0.60 | 221 | 309 | 208 | stated in 1 doc(s) ^[textanalyse-existenz-system-und-leid.md:L268] |
| Kairos | Integration | 0.50 | 78 | 287 | 68 | stated in 1 doc(s) ^[kohaerenz-protokoll-projekt-rekonstruktion.md:L166] |
| Chaos | EP | 0.47 | 214 | 140 | 89 | stated in 1 doc(s) ^[dramatica-storyform-kohaerenz-protokoll-analyse.md:L52] |
| EP | Teil | 0.76 | 140 | 210 | 72 | stated in 1 doc(s) ^[kohaerenz-protokoll-architecture-synthesis-2.md:L49] |
| EP | Ebene | 0.46 | 140 | 207 | 76 | stated in 1 doc(s) ^[aegis-subplots-kapitelweise-system-exploration-docx.md:L61] |
| Fundament | Sein | 0.59 | 166 | 181 | 99 | stated in 2 doc(s) ^[kohaerenz-protokoll-inkubation-x.md:L58] ^[kohaerenz-protokoll-transzendenz-vektoren.md:L88] |
| Maschine | AEGIS | 0.48 | 73 | 269 | 59 | stated in 1 doc(s) ^[ki-prompt-analyse-hard-problem-of-consciousness.md:L154] |
| AEGIS | Logos | 0.70 | 269 | 72 | 71 | stated in 1 doc(s) ^[narrative-physik-attraktoren-leserbewusstsein.md:L123] |
| Verbindung | Moonshine | 0.38 | 213 | 126 | 71 | stated in 1 doc(s) ^[primzahlen-als-metapher-in-kohaerenz-protokoll.md:L155] |
| Theorie | theory | 0.69 | 167 | 171 | 103 | proposed |
| AEGIS | LogOS | 0.48 | 269 | 67 | 62 | stated in 3 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L530] ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L260] |
| Selbst | self | 0.63 | 192 | 137 | 55 | proposed |
| AEGIS | Fusion | 0.40 | 269 | 54 | 50 | stated in 1 doc(s) ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L146] |
| ein | One | 0.67 | 267 | 55 | 39 | proposed |
| AEGIS-Analogon | System | 0.45 | 1 | 309 | 1 | stated in 1 doc(s) ^[narrative-plot-exploration-existenzielle-kohaerenz.md:L21] |
| Kern | Core | 0.72 | 203 | 105 | 43 | proposed |
| Kohärenz | Interne Konsistenz | 0.44 | 295 | 6 | 6 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L68] |
| EPs | Teile | 0.50 | 142 | 157 | 55 | stated in 1 doc(s) ^[aegis-genesis-krise-prosa-auftrag.md:L47] |
| Kohärenz | Nicht-Trivialität | 0.45 | 295 | 2 | 2 | stated in 1 doc(s) ^[parakonsistenz-aegis-und-nicht-existenz.md:L50] |
| Kohärenz | Coherency | 0.59 | 295 | 1 | 0 | proposed |
| Kohärenz | Psychologischer Mondschein | 0.39 | 295 | 1 | 1 | stated in 1 doc(s) ^[monstergruppe-als-narrative-inspiration.md:L116] |
| Logik | Logos-Prime | 0.49 | 233 | 62 | 33 | stated in 1 doc(s) ^[kohaerenz-protokoll-dramatica-synthese-masterkonzept.md:L104] |
| Teil | Part | 0.52 | 210 | 85 | 43 | proposed |
| Funktion | Function | 0.78 | 205 | 84 | 44 | proposed |
| Resonanz | Moonshine-Link | 0.61 | 194 | 89 | 47 | stated in 1 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L180] |
| Maxwellscher Dämon | AEGIS | 0.60 | 12 | 269 | 11 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L101] |
| Kernsystem | AEGIS | 0.72 | 7 | 269 | 6 | stated in 1 doc(s) ^[untersuche-in-wie-fern-juna-bzw-das-fundament-du.md:L161] |
| AEGIS | Exclusionary Order | 0.53 | 269 | 4 | 4 | stated in 1 doc(s) ^[project-status-report-kohaerenz-protokoll-canonical-state-st.md:L16] |
| AEGIS | Uncanny Valley KI | 0.54 | 269 | 2 | 2 | stated in 2 doc(s) ^[kosmischer-horror-in-kohaerenz-protokoll.md:L140] ^[kosmischer-horror-in-kohaerenz-protokoll-2.md:L148] |
| Antagonist-System | AEGIS | 0.59 | 1 | 269 | 1 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-analyse.md:L111] |
| Antagonistisches System | AEGIS | 0.53 | 1 | 269 | 1 | stated in 1 doc(s) ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L160] |
| Exkludierenden Ordnung | AEGIS | 0.49 | 1 | 269 | 1 | stated in 1 doc(s) ^[dual-kernel-erzaehlarchitektur-bewusstsein-symmetrie-ourobor.md:L106] |
| AEGIS | Force of Fragmentation | 0.66 | 269 | 1 | 1 | stated in 1 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1649] |
| AEGIS | Logical-Systemic Subsystem | 0.74 | 269 | 1 | 1 | stated in 1 doc(s) ^[dramatica-storyform-kohaerenz-protokoll-2.md:L43] |
| Weltmaschine | AEGIS | 0.70 | 1 | 269 | 1 | stated in 1 doc(s) ^[roman-entwicklung-ontologie-trauma-horror.md:L39] |
| Ziel | Objective | 0.62 | 227 | 41 | 27 | proposed |
| Erfahrung | Qualia | 0.60 | 174 | 93 | 66 | stated in 7 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L124] ^[prosaversion-von-genesis-erstellen.md:L31] |
| Struktur | Subtext | 0.67 | 248 | 15 | 14 | stated in 3 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L199] ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L26] |
| Realität | Steadfast | 0.51 | 247 | 14 | 12 | stated in 1 doc(s) ^[duale-storyform-synthese-kohaerenz-protokoll.md:L150] |
| Psyche | Mind | 0.71 | 128 | 131 | 60 | stated in 1 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L269] |
| Risse | Glitches | 0.65 | 164 | 87 | 67 | stated in 1 doc(s) ^[umfassendes-lokalitaeten-konzept-fuer-roman.md:L45] |
| Daten | Data | 0.66 | 180 | 70 | 40 | proposed |
| Paraiyas | Trauma | 0.43 | 18 | 232 | 11 | stated in 1 doc(s) ^[kohaerenz-protokoll-architecture-synthesis.md:L59] ^[kohaerenz-protokoll-architecture-synthesis.md:L67] |
| Negentropie | Ordnung | 0.45 | 27 | 221 | 26 | stated in 1 doc(s) ^[textanalyse-existenz-system-und-leid.md:L52] |
| Realität | Nested Reality | 0.42 | 247 | 1 | 1 | stated in 1 doc(s) ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:L149] |
| Sophia | Synthese | 0.50 | 49 | 199 | 32 | stated in 2 doc(s) ^[roman-outline-system-kael.md:L170] ^[system-kael-konzeptentwicklung-und-analyse.md:L54] |
| Welt | Location | 0.76 | 228 | 10 | 8 | stated in 1 doc(s) ^[codex-optimierung-fuer-kohaerenz-protokoll.md:L533] |
| Logik | P-Klasse | 0.38 | 233 | 3 | 3 | stated in 1 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L236] |
| Ziel | Story Goal | 0.58 | 227 | 7 | 5 | stated in 1 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L130] |
| Sein | Being | 0.78 | 181 | 51 | 28 | stated in 1 doc(s) ^[storyforms-system-mind-bewusstsein.md:L93]; proposed |
| Kohärenz Protokoll | Content | 0.60 | 212 | 20 | 7 | stated in 2 doc(s) ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L179] ^[master-konzept-kohaerenz-protokoll-analyse.md:L175] |
| Chaos | Uncontrolled | 0.70 | 214 | 15 | 11 | stated in 1 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L52] |
| Welt | Simulation Beta | 0.49 | 228 | 1 | 1 | stated in 1 doc(s) ^[narrative-plot-exploration-existenzielle-kohaerenz.md:L271] |
| Kern | CORE | 0.65 | 203 | 24 | 16 | proposed |
| Erinnerung | Mnemosyne | 0.67 | 130 | 93 | 51 | stated in 3 doc(s) ^[welten.md:L16] ^[kohaerenz-protokoll-projekt-rekonstruktion.md:L166] |
| Leere | Moros | 0.64 | 147 | 76 | 42 | stated in 1 doc(s) ^[tattoo-konzept-archetypen-heilung-rebellion.md:L95] ^[tattoo-konzept-archetypen-heilung-rebellion.md:L181] |
| Leere | Umwelt | 0.53 | 147 | 76 | 48 | stated in 3 doc(s) ^[aegis-genesis-krise-prosa-auftrag-2.md:L68] ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L72] |
| Entscheidungstheorie | Theory | 0.55 | 4 | 214 | 4 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L215] |
| Kohärenz Protokoll | coherence protocol | 0.60 | 212 | 6 | 3 | proposed |
| Irregularität | Chaos | 0.73 | 3 | 214 | 2 | stated in 1 doc(s) ^[emergenz-aegis-und-selbststrukturierung.md:L62] |
| Mutuale Information | Information | 0.32 | 3 | 214 | 3 | stated in 1 doc(s) ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:L106] |
| KW4 | Potenzial | 0.42 | 68 | 148 | 27 | stated in 3 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung-2.md:L91] ^[roman-lokalitaeten-konzept-und-ausarbeitung-3.md:L91] |
| Dynamik | Dynamics | 0.72 | 168 | 46 | 31 | proposed |
| Entropie | Unordnung | 0.72 | 152 | 56 | 53 | stated in 3 doc(s) ^[kohaerenz-protokoll-synthese-integration.md:L77] ^[aegis-paradoxon-konzeption-und-analyse.md:L37] |
| Erinnerung | Memory | 0.64 | 130 | 78 | 34 | stated in 1 doc(s) ^[storyforms-system-mind-bewusstsein.md:L43] |
| Resonanz | Schwingung | 0.47 | 194 | 14 | 12 | proposed |
| Bewusstsein | Für-sich | 0.44 | 200 | 7 | 7 | stated in 1 doc(s) ^[aegis-genesis-krise-prosa-auftrag-2.md:L175] |
| Kollaps | Failure | 0.49 | 149 | 58 | 40 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-verortung.md:L123] |
| Bewusstsein | Brahman | 0.44 | 200 | 6 | 6 | stated in 1 doc(s) ^[narrativ-existenzieller-kohaerenz-nzt-protokoll.md:L249] |
| Integrität | Guardian | 0.54 | 115 | 89 | 27 | stated in 1 doc(s) ^[paradoxien-der-kohaerenz-protokoll-entwicklung.md:L360] |
| Fehler | Hamartia | 0.68 | 182 | 20 | 16 | stated in 1 doc(s) ^[aegis-paradoxon-konzeption-und-analyse.md:L55] |
| POV | Perspektive | 0.74 | 20 | 182 | 14 | stated in 2 doc(s) ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L57] ^[genesis-mehrstufige-recherche-und-ausformulierung.md:L57] |
| Simulationstheorie | Simulation | 0.51 | 18 | 183 | 18 | stated in 1 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L89] |
| Kollaps | Löschung | 0.57 | 149 | 51 | 42 | stated in 2 doc(s) ^[kohaerenz-protokoll-architecture-synthesis.md:L131] ^[ontologische-inversion-von-aegis-kritisches-framework.md:L144] |
| Eintauchen | Simulation | 0.68 | 14 | 183 | 10 | stated in 2 doc(s) ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L441] ^[genesis-mehrstufige-recherche-und-ausformulierung.md:L497] |
| Selbst | Atman | 0.68 | 192 | 4 | 4 | stated in 1 doc(s) ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L97] |
| Beobachter-Kohärenz | Resonanz | 0.51 | 2 | 194 | 2 | stated in 1 doc(s) ^[duale-storyform-synthese-kohaerenz-protokoll.md:L239] |
| Juna | OQ-01 | 0.35 | 192 | 2 | 2 | stated in 1 doc(s) ^[dkt-fundament-kohaerenz-protokoll-md.md:L220] |
| Selbst | Solid Flexible Self | 0.64 | 192 | 2 | 2 | stated in 2 doc(s) ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L191] ^[beziehungsheilung-nach-trauma-konzeptpapier-3.md:L197] |
| Fragmentierung | division | 0.65 | 183 | 10 | 1 | proposed |
| ENDE | end | 0.49 | 7 | 185 | 2 | proposed |
| Wächterin | Self | 0.70 | 30 | 161 | 15 | stated in 1 doc(s) ^[dissoziative-identitaet-sinnsuche-im-trauma.md:L200] |
| Handlung | OS | 0.54 | 147 | 43 | 23 | stated in 1 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L46] |
| Schatten | Nyx | 0.50 | 58 | 129 | 19 | stated in 4 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik.md:L146] ^[kael-charakterarchitektur-und-konfliktdynamik.md:L156] |
| Leere | Nicht-Existenz | 0.54 | 147 | 39 | 29 | stated in 1 doc(s) ^[romananfang-leere-und-systemgenesis.md:L150] |
| Vortäuschen | Simulation | 0.68 | 2 | 183 | 2 | stated in 1 doc(s) ^[gutachten-grad-der-behinderung-bei-dis.md:L183] |
| Anteil | Alter | 0.48 | 97 | 87 | 37 | stated in 5 doc(s) ^[concept-paper-the-architectural-foundations-of-kohaerenz-pro.md:L136] ^[project-coherence-protocol-a-canon-of-core-identity-and-anta.md:L33] |
| Q13 | Simulation | 0.34 | 1 | 183 | 1 | stated in 1 doc(s) ^[coherence-critique-and-question-generation.md:L286] |
| Argus | Lex | 0.35 | 54 | 127 | 52 | stated in 3 doc(s) ^[kohaerenz-protokoll-konzeptentwicklung.md:L275] ^[2-kohaerenz-protokoll-konzeptentwicklung.md:L173] |
| Daten | Shared Data | 0.65 | 180 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L49] |
| Ego | Ich | 0.48 | 15 | 164 | 11 | stated in 2 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik.md:L32] ^[kael-charakterarchitektur-und-konfliktdynamik-3.md:L32] |
| Entropie | K₀ | 0.38 | 152 | 26 | 9 | stated in 1 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L82] |
| Kern-Selbst | Self | 0.59 | 17 | 161 | 10 | stated in 3 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik.md:L21] ^[kael-charakterarchitektur-und-konfliktdynamik-2.md:L21] |
| Möglichkeiten | Potentialität | 0.67 | 115 | 63 | 37 | stated in 1 doc(s) ^[monstergruppe-aegis-und-narrative-moeglichkeiten.md:L186] ^[monstergruppe-aegis-und-narrative-moeglichkeiten.md:L186] |
| Nichts Rauschen | Ende | 0.68 | 65 | 112 | 28 | stated in 1 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L288] |
| Reise | Journey | 0.75 | 116 | 61 | 25 | proposed |
| Nichts | Nothing | 0.59 | 151 | 26 | 22 | proposed |
| Entropie | Wärmetod | 0.46 | 152 | 24 | 23 | stated in 2 doc(s) ^[ki-narrative-kollaps-kohaerenz-paradoxie.md:L81] ^[ontologische-inversion-von-aegis-kritisches-framework.md:L89] |
| stark | Strong | 0.63 | 162 | 13 | 6 | proposed |
| Störungen | Glitches | 0.50 | 87 | 87 | 31 | stated in 2 doc(s) ^[roman-outline-system-kael.md:L39] ^[system-kael-konzeptentwicklung-und-analyse.md:L78]; proposed |
| Potenzial | Potentiality | 0.58 | 148 | 26 | 6 | stated in 1 doc(s) ^[dramatica-und-kohaerenz-protokoll-analyse.md:L69] |
| Kernwelten | Worldbuilding | 0.60 | 134 | 39 | 23 | stated in 1 doc(s) ^[entwicklungsstrategie-fuer-kohaerenz-protokoll.md:L131] |
| Tiefe | Z-Buffer | 0.53 | 167 | 4 | 2 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L274] |
| Wächter | Guardians | 0.52 | 82 | 88 | 49 | proposed |
| Agency-System | KI | 0.33 | 1 | 167 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L57] |
| Fundament | Fundamentality | 0.47 | 166 | 1 | 1 | proposed |
| Fundament | Metaphysical Subsystem | 0.51 | 166 | 1 | 1 | stated in 1 doc(s) ^[dramatica-storyform-kohaerenz-protokoll-2.md:L51] |
| Fundament | Wahre Metaphysische Gesetz | 0.43 | 166 | 1 | 1 | stated in 1 doc(s) ^[untersuche-in-wie-fern-juna-bzw-das-fundament-du.md:L89] |
| Fundament | fundament | 0.46 | 166 | 1 | 1 | proposed |
| Gefühl | Namenlos | 0.42 | 166 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzept.md:L120] |
| Widersprüche | Dialetheism | 0.55 | 137 | 29 | 18 | stated in 1 doc(s) ^[ki-rolle-aegis-genesis-fragestellungen.md:L102] |
| Möglichkeit | Potentiality | 0.73 | 140 | 26 | 8 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-verortung.md:L119] |
| Natur der Realität | Ontologie | 0.62 | 61 | 105 | 33 | stated in 1 doc(s) ^[kohaerenz-protokoll-umfassendes-konzept.md:L87] |
| Persönlichkeitsanteil | ANP | 0.56 | 18 | 145 | 17 | stated in 1 doc(s) ^[argus-chronist-der-wandlung.md:L19] |
| Spannungsfelder | Konflikte | 0.34 | 19 | 144 | 14 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L375] |
| Alters | Teilen | 0.42 | 91 | 69 | 25 | stated in 1 doc(s) ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L99] |
| Kollaps | Submit | 0.63 | 149 | 11 | 5 | stated in 1 doc(s) ^[kohaerenz-protokoll-synthese-integration.md:L47] |
| Konsistenz | Context Rot | 0.50 | 154 | 5 | 4 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L145] |
| Beobachter | Argus | 0.58 | 103 | 54 | 29 | stated in 1 doc(s) ^[kohaerenz-protokoll-projekt-rekonstruktion.md:L168] |
| Domäne | Kernwelt | 0.45 | 84 | 73 | 20 | stated in 1 doc(s) ^[roman-konzept-dualitaet-kohaerenz-spannung.md:L39] |
| Widersprüche | Dialetheia | 0.64 | 137 | 18 | 14 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-analyse.md:L181] |
| Leere | Emptiness | 0.69 | 147 | 8 | 7 | proposed |
| Leere | Deprivation | 0.71 | 147 | 7 | 5 | stated in 2 doc(s) ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L252] ^[genesis-mehrstufige-recherche-und-ausformulierung.md:L242] |
| Glaube | Mind | 0.77 | 23 | 131 | 12 | stated in 1 doc(s) ^[storyforms-system-mind-bewusstsein.md:L91] |
| Rissen | Glitches | 0.52 | 67 | 87 | 35 | stated in 1 doc(s) ^[guardians-und-kern-welten-konzept.md:L39] ^[guardians-und-kern-welten-konzept.md:L64] |
| Bauplan der Heilung | TSDP | 0.61 | 2 | 151 | 2 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L164] |
| Entropie | Information Überraschung | 0.40 | 152 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-dramatica-synthese-masterkonzept.md:L164] |
| Gott | Situation | 0.51 | 38 | 115 | 18 | stated in 1 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L287] |
| KW2 | Memory | 0.43 | 75 | 78 | 32 | stated in 1 doc(s) ^[deconstructing-reality-s-architecture.md:L274] |
| bewusst | Conscious | 0.65 | 128 | 24 | 4 | proposed |
| Nichts | Einfluss der Leere | 0.66 | 151 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-transzendenz-vektoren.md:L89] |
| Erasure-Kern | Kollaps | 0.54 | 2 | 149 | 2 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L93] |
| M-Eigenschaften | Aspekte | 0.53 | 3 | 147 | 3 | stated in 1 doc(s) ^[primzahlen-als-metapher-in-kohaerenz-protokoll.md:L96] |
| Wissen | Knowing | 0.68 | 147 | 3 | 1 | proposed |
| Kernbetriebssystem | ANP | 0.51 | 4 | 145 | 3 | stated in 1 doc(s) ^[ki-antagonist-fragmentierte-gottheit-analyse.md:L138] |
| Leere | Unwägbarkeiten der Außenwelt | 0.29 | 147 | 1 | 1 | stated in 1 doc(s) ^[textanalyse-existenz-system-und-leid.md:L174] |
| ANP | K1-Agent | 0.38 | 145 | 2 | 2 | stated in 2 doc(s) ^[aegis-manifest-genesis-krise-reboot.md:L189] ^[aegis-manifest-genesis-krise-reboot-2.md:L246] |
| EPs | Trauma-Halter | 0.49 | 142 | 5 | 3 | stated in 1 doc(s) ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:L120] |
| Fehlern | Glitches | 0.61 | 60 | 87 | 21 | stated in 1 doc(s) ^[kohaerenz-protokoll-inkubation-x.md:L270] |
| Benutzeroberfläche des Bewusstseins | ANP | 0.60 | 1 | 145 | 1 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L131] |
| Funktionalität | Function | 0.66 | 62 | 84 | 17 | proposed |
| Lex | Logiker | 0.49 | 127 | 19 | 8 | stated in 3 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik.md:L156] ^[kael-charakterarchitektur-und-konfliktdynamik.md:L183] |
| Trust | Vertrauen | 0.59 | 60 | 86 | 27 | stated in 1 doc(s) ^[storyforms-system-mind-bewusstsein.md:L89] |
| EPs | Trauma Holders | 0.70 | 142 | 3 | 3 | stated in 1 doc(s) ^[a-guide-to-the-society-of-self-understanding-system-kael.md:L71] |
| Heilung | Sharding | 0.38 | 141 | 4 | 1 | stated in 1 doc(s) ^[textanalyse-existenz-system-und-leid.md:L248] |
| Alters | Persönlichkeitsanteile | 0.79 | 91 | 53 | 20 | stated in 3 doc(s) ^[digitale-uberwelt-konzept-und-gestaltung.md:L100] ^[junas-liebe-kaels-trauma-aegis-docx.md:L19] |
| Emotionale Anteile | EP | 0.53 | 4 | 140 | 4 | stated in 1 doc(s) ^[ki-narrative-kollaps-kohaerenz-paradoxie.md:L132] |
| Emotionale Teile | EPs | 0.42 | 2 | 142 | 2 | stated in 1 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik-2.md:L32] |
| Schmerz | Pain | 0.74 | 136 | 7 | 4 | proposed |
| Alters | Identitäten | 0.63 | 91 | 51 | 19 | stated in 1 doc(s) ^[aegis-paradoxon-konzeption-und-analyse.md:L63] |
| Extinktionslernen | Heilung | 0.46 | 1 | 141 | 1 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L145] |
| Einfluss | Influence | 0.77 | 101 | 38 | 17 | proposed |
| Live | Plot | 0.73 | 10 | 129 | 8 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzept.md:L307] ^[kohaerenz-protokoll-konzept.md:L371] |
| Ängste | Cerberus | 0.37 | 53 | 85 | 16 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L254] |
| Nyx | PP-INT-01 | 0.37 | 129 | 8 | 8 | stated in 3 doc(s) ^[forschungsauftrag-spannungspunktanalyse-und-charakterausarbe.md:L197] ^[kael-system-tsdp-analyse-und-profile.md:L340] |
| Somatische Vertex Explosion | Schmerz | 0.61 | 1 | 136 | 1 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L273] |
| Handlungen | Doing | 0.50 | 122 | 14 | 7 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse.md:L63] |
| Fixierte Einstellung | Mind | 0.54 | 2 | 131 | 2 | stated in 2 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L65] ^[dramatica-storyform-validierung-und-synthese.md:L36] |
| Fixierte Haltung | Mind | 0.75 | 2 | 131 | 2 | stated in 1 doc(s) ^[narrative-context-protocol-ncp-spezifikation.md:L53] |
| Absolute Ideologie | Mind | 0.50 | 1 | 131 | 1 | stated in 1 doc(s) ^[duale-storyform-synthese-kohaerenz-protokoll.md:L188] |
| Beschützer | Guardian | 0.52 | 43 | 89 | 16 | proposed |
| KW4 | Potential | 0.79 | 68 | 64 | 27 | stated in 3 doc(s) ^[kohaerenz-protokoll-forschungsaufgabe.md:L228] ^[parakonsistente-logik-fuer-kohaerenz-protokoll.md:L280] |
| Beschützer | Guardians | 0.57 | 43 | 88 | 18 | proposed |
| Integrität | Justification | 0.55 | 115 | 16 | 7 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L157] |
| Netzwerk | Network | 0.75 | 95 | 36 | 26 | proposed |
| Emergenz | Unkontrolliertheit | 0.67 | 127 | 3 | 2 | stated in 1 doc(s) ^[dramatica-storyform-kohaerenz-protokoll-analyse.md:L102] |
| Chaos-Rand | Grenze | 0.38 | 1 | 128 | 1 | stated in 1 doc(s) ^[aegis-und-der-kollaps-kritische-analyse.md:L65] |
| KOHÄRENZ | Coherence | 0.61 | 10 | 119 | 3 | proposed |
| Lex | Logician ANP | 0.52 | 127 | 2 | 2 | stated in 2 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1201] ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1301] |
| Lex | Rationale ANP | 0.48 | 127 | 1 | 1 | stated in 1 doc(s) ^[charaktermodellierung-mit-aieos-schema.md:L89] |
| Verborgene Verbindungen | Moonshine | 0.36 | 2 | 126 | 2 | stated in 1 doc(s) ^[monstergruppe-als-denkmodell-der-komplexitaet.md:L253] |
| Widerspruch | Objection | 0.62 | 115 | 13 | 5 | proposed |
| Geist | Story Mind | 0.65 | 100 | 27 | 12 | stated in 1 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L33] |
| Verborgene Verbindung | Moonshine | 0.64 | 1 | 126 | 1 | stated in 1 doc(s) ^[monstergruppe-als-denkmodell-der-komplexitaet.md:L267] |
| InstructionDeputies | ANPs | 0.39 | 4 | 122 | 4 | stated in 1 doc(s) ^[ontologische-inversion-von-aegis-kritisches-framework.md:L165] |
| Herzstück | Core | 0.59 | 21 | 105 | 8 | proposed |
| ANPs | Daily Life Managers | 0.67 | 122 | 2 | 2 | stated in 1 doc(s) ^[a-guide-to-the-society-of-self-understanding-system-kael.md:L33] |
| Gastgeber | ANPs | 0.66 | 2 | 122 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-forschungsaufgabe.md:L126] |
| kohaerenz | Coherence | 0.62 | 5 | 119 | 1 | proposed |
| Innere Kind | Kiko | 0.48 | 2 | 122 | 2 | stated in 1 doc(s) ^[tattoo-konzept-archetypen-heilung-rebellion.md:L93] ^[tattoo-konzept-archetypen-heilung-rebellion.md:L141] |
| Dialetheische Koexistenz | Akzeptanz | 0.62 | 1 | 122 | 1 | stated in 1 doc(s) ^[dialetheismus-im-kohaerenz-protokoll.md:L253] |
| Jetzt-Raum | Präsenz | 0.66 | 7 | 116 | 5 | stated in 1 doc(s) ^[kohaerenz-protokoll.md:L1392] |
| Psychologische Kriegsführung | Psychology | 0.70 | 9 | 114 | 4 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse-2.md:L243] |
| Selbstproduktion | Autopoiesis | 0.78 | 25 | 97 | 24 | stated in 1 doc(s) ^[aegis-seele-und-entropie.md:L29] |
| K1-Kern | Coherence | 0.78 | 1 | 119 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L68] |
| Kohaerenz | Coherence | 0.77 | 1 | 119 | 0 | proposed |
| Erlebnisse | Qualia | 0.71 | 26 | 93 | 6 | stated in 1 doc(s) ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L103] |
| Hermeneutik | Interpretation | 0.78 | 2 | 117 | 2 | stated in 1 doc(s) ^[emergenz-aegis-und-selbststrukturierung.md:L163] |
| Protokolle | Logs | 0.50 | 95 | 24 | 13 | stated in 1 doc(s) ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L425] |
| Psychology | Internal Process | 0.56 | 114 | 3 | 3 | stated in 1 doc(s) ^[coherence-critique-and-question-generation.md:L87] |
| Vermeidung | Stasis-Loop | 0.71 | 116 | 1 | 1 | stated in 1 doc(s) ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L153] |
| Domäne Universe | Situation | 0.71 | 1 | 115 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-dramatica-synthese-masterkonzept.md:L100] |
| Kaels Trauma | Qualia | 0.67 | 23 | 93 | 10 | stated in 1 doc(s) ^[kohaerenz-protokoll-plot-entwicklung-und-wahrheitsdualitaet.md:L329] |
| Resonanz-Landschaft | Mnemosyne | 0.61 | 23 | 93 | 17 | stated in 6 doc(s) ^[kohaerenz-protokoll-2.md:L76] ^[roman-lokalitaeten-konzept-und-ausarbeitung-2.md:L137] |
| Psychologisches Hacking | Psychology | 0.54 | 2 | 114 | 2 | stated in 1 doc(s) ^[duale-storyform-synthese-kohaerenz-protokoll.md:L190] |
| Way of Thinking | Psychology | 0.54 | 2 | 114 | 2 | stated in 1 doc(s) ^[dramatica-storyform-kohaerenz-protokoll.md:L50] |
| Anteil | Exile | 0.56 | 97 | 18 | 8 | stated in 1 doc(s) ^[dissoziative-identitaet-sinnsuche-im-trauma.md:L125] ^[dissoziative-identitaet-sinnsuche-im-trauma.md:L194] |
| Außen | external | 0.79 | 40 | 75 | 1 | proposed |
| Geruch | Trigger | 0.57 | 27 | 88 | 12 | stated in 1 doc(s) ^[integriertes-kohaerenz-protokoll-erstellung.md:L275] |
| Internes | Internal | 0.58 | 11 | 103 | 6 | proposed |
| Anteile | Multiple Perspektiven | 0.58 | 112 | 1 | 1 | stated in 1 doc(s) ^[narrative-physik-attraktoren-leserbewusstsein.md:L234] |
| Objekt | Object | 0.77 | 101 | 12 | 4 | proposed |
| Wert | Value | 0.72 | 80 | 33 | 14 | proposed |
| World | Location | 0.43 | 102 | 10 | 8 | stated in 1 doc(s) ^[entwicklungsstrategie-fuer-kohaerenz-protokoll.md:L89] ^[entwicklungsstrategie-fuer-kohaerenz-protokoll.md:L89] |
| Bereich | Field | 0.76 | 85 | 25 | 7 | proposed |
| Kairos-Potentialis | KW4 | 0.65 | 42 | 68 | 37 | stated in 2 doc(s) ^[projektplanung-fuer-kohaerenz-protokoll.md:L87] ^[kohaerenz-protokoll-duale-dramatica-storyform-synthese.md:L111] |
| Konstrukt-Stadt | Logos-Prime | 0.67 | 48 | 62 | 10 | stated in 2 doc(s) ^[a-learner-s-glossary-for-the-world-of-kohaerenz-protokoll.md:L52] ^[welt.md:L38] |
| Glaube | Vertrauen | 0.49 | 23 | 86 | 12 | stated in 1 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L238] |
| Systemlogik | LogOS | 0.60 | 42 | 67 | 21 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptentwicklung.md:L80] |
| Meta-Ebene | Überwelt | 0.52 | 27 | 82 | 10 | stated in 3 doc(s) ^[kohaerenz-protokoll-konzeptentwicklung.md:L220] ^[2-kohaerenz-protokoll-konzeptentwicklung.md:L142] |
| Alters | Persönlichkeitszustände | 0.63 | 91 | 17 | 7 | stated in 2 doc(s) ^[monstergruppe-primzahlen-plot-blueprint.md:L80] ^[dissoziative-identitaet-invalidierung-im-gesundheitssystem.md:L88] |
| Wandel | Change | 0.79 | 64 | 44 | 17 | stated in 2 doc(s) ^[dramatica-storyform-synthese-aegis-verortung.md:L123] ^[storyforms-system-mind-bewusstsein.md:L19] |
| Zeitpunkt | Kairos | 0.58 | 30 | 78 | 8 | stated in 1 doc(s) ^[umfassendes-lokalitaeten-konzept-fuer-roman.md:L536] |
| Kognition | Thinking | 0.53 | 54 | 54 | 20 | proposed |
| Werkzeug | Systematic Agency | 0.47 | 102 | 6 | 3 | stated in 1 doc(s) ^[fragen-zu-existenz-agency-und-realitaet.md:L132] |
| Körper | Hardware | 0.54 | 77 | 30 | 7 | stated in 1 doc(s) ^[hard-sf-roman-outline-dkt-physik-cosmic-horror.md:L70] |
| Universe | Objective Story | 0.40 | 76 | 31 | 25 | stated in 1 doc(s) ^[kohaerenz-protokoll-dramatica-synthese.md:L158] |
| Vier Throughlines | Perspektiven | 0.79 | 1 | 105 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-dramatica-synthese-masterkonzept.md:L85] |
| Aggression | Fight | 0.60 | 59 | 46 | 16 | stated in 1 doc(s) ^[hard-sf-roman-outline-dkt-physik-cosmic-horror.md:L55] |
| Cerberus | Fortress | 0.71 | 85 | 20 | 16 | stated in 2 doc(s) ^[the-psychological-mechanics-from-tertiary-structural-dissoci.md:L59] ^[an-ontological-and-systemic-overview-of-the-coherence-protoc.md:L91] |
| Emergentes | emergent | 0.73 | 12 | 93 | 6 | proposed |
| Alters | Identitätszustände | 0.35 | 91 | 13 | 7 | stated in 1 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L252] |
| Alters | Persönlichkeitszuständen | 0.55 | 91 | 13 | 6 | stated in 2 doc(s) ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L204] ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L255] |
| Bewertung | Judgment | 0.77 | 83 | 21 | 4 | proposed |
| Hüter | Guardian | 0.73 | 15 | 89 | 8 | proposed |
| Nicht-Ich | Objekt | 0.60 | 3 | 101 | 3 | stated in 3 doc(s) ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L430] ^[aegis-genesis-krise-prosa-auftrag-formulieren-2.md:L432] |
| Amnesie | Oblivion-Zustand | 0.61 | 102 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-projekt-rekonstruktion.md:L80] |
| Co₁ | KW1 | 0.50 | 22 | 81 | 4 | stated in 2 doc(s) ^[the-coherence-protocol-a-worldbuilding-bible.md:L107] ^[erlebniswelten-der-anteile-uberlagerung-mit-kernwelten.md:L31] |
| Selbstbezogenheit | Autopoiesis | 0.49 | 5 | 97 | 3 | stated in 1 doc(s) ^[aegis-paradoxon-neukonzeption-und-analyse-docx.md:L86] |
| Mechanik | Mechanics | 0.79 | 60 | 42 | 7 | proposed |
| Autopoiesis | Prozess der Selbstproduktion | 0.79 | 97 | 4 | 3 | stated in 1 doc(s) ^[optimierter-prompt-fuer-kohaerenz-protokoll.md:L30] |
| Wechsel | Switches | 0.76 | 87 | 14 | 12 | stated in 1 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik-2.md:L33] |
| Alters | Modulen | 0.31 | 91 | 9 | 3 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse-2.md:L266] |
| Alters | Identitätszuständen | 0.54 | 91 | 7 | 5 | stated in 2 doc(s) ^[kohaerenz-protokoll-konzept.md:L59] ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L261] |
| Prinzip der Selbstreferentiellen Schließung | Autopoiesis | 0.65 | 1 | 97 | 1 | stated in 1 doc(s) ^[emergenz-aegis-und-selbststrukturierung.md:L388] |
| Prozess der Selbsterhaltung | Autopoiesis | 0.73 | 1 | 97 | 1 | stated in 1 doc(s) ^[narrative-kernentwicklung-aegis-und-system-kael.md:L97] |
| Datenarchive | Mnemosyne | 0.76 | 5 | 93 | 4 | stated in 2 doc(s) ^[digitale-uberwelt.md:L49] ^[recherche-ueberwelt.md:L134] |
| Familie | Family | 0.62 | 23 | 74 | 10 | proposed |
| Hüterin | Guardian | 0.41 | 8 | 89 | 6 | proposed |
| KW2 | McL | 0.47 | 75 | 22 | 5 | stated in 2 doc(s) ^[the-coherence-protocol-a-worldbuilding-bible.md:L108] ^[erlebniswelten-der-anteile-uberlagerung-mit-kernwelten.md:L32] |
| Kognition | thinking | 0.55 | 54 | 43 | 10 | proposed |
| Zerstörung | Shattering | 0.67 | 90 | 7 | 3 | proposed |
| Phänomenales Erleben | Qualia | 0.73 | 3 | 93 | 3 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L51] |
| Schnittstelle | interface | 0.79 | 75 | 21 | 6 | proposed |
| Bibliothek | library | 0.55 | 23 | 72 | 12 | proposed |
| Komplex | Complex | 0.56 | 13 | 82 | 8 | proposed |
| EINE | one | 0.60 | 6 | 89 | 1 | proposed |
| Familien | Family | 0.48 | 21 | 74 | 12 | proposed |
| Konstante | constant | 0.66 | 50 | 45 | 4 | proposed |
| We | Subjective Story | 0.53 | 80 | 15 | 5 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L292] |
| Außen | outside | 0.78 | 40 | 54 | 0 | proposed |
| Cosmic Horror des Bewusstseins | Qualia | 0.50 | 1 | 93 | 1 | stated in 1 doc(s) ^[roman-entwicklung-ontologie-trauma-horror.md:L124] |
| Stufe | level | 0.71 | 37 | 57 | 1 | proposed |
| Bindung | Verpflichtung | 0.47 | 82 | 11 | 5 | stated in 1 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L186] |
| Trägheit | Widerstand | 0.77 | 10 | 83 | 6 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse-2.md:L82] |
| Alters | Character Profiles | 0.62 | 91 | 1 | 1 | stated in 1 doc(s) ^[the-coherence-protocol-a-worldbuilding-bible.md:L144] |
| Parakonsistente | Paraconsistent | 0.71 | 36 | 56 | 21 | proposed |
| LogOS | Consistency | 0.53 | 67 | 24 | 6 | stated in 1 doc(s) ^[briefing-core-concepts-of-the-kohaerenz-protokoll-project.md:L133] |
| Schwäche | Hamartia | 0.48 | 71 | 20 | 8 | stated in 2 doc(s) ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L188] ^[aegis-genesis-krise-prosa-auftrag-formulieren-2.md:L188] |
| Endlosschleife | Freeze | 0.71 | 16 | 74 | 6 | stated in 3 doc(s) ^[logik-trifft-transzendente-entitaet.md:L180] ^[logik-trifft-transzendente-entitaet-2.md:L178] |
| Gesetz | Law | 0.76 | 46 | 44 | 12 | proposed |
| KW4 | Ly | 0.62 | 68 | 22 | 5 | stated in 2 doc(s) ^[the-coherence-protocol-a-worldbuilding-bible.md:L110] ^[erlebniswelten-der-anteile-uberlagerung-mit-kernwelten.md:L34] |
| Guardians | Autonomous Subsystems | 0.51 | 88 | 1 | 1 | stated in 1 doc(s) ^[aegis-manifest-genesis-krise-reboot.md:L105] |
| kognitiv | Cognitive | 0.78 | 17 | 72 | 4 | proposed |
| Gewahrsein | Consciousness | 0.70 | 5 | 84 | 3 | proposed |
| Trivialität | Explosion | 0.64 | 17 | 72 | 13 | stated in 1 doc(s) ^[parakonsistente-logik-fuer-kohaerenz-protokoll.md:L140] |
| Wächter-Programme | Guardians | 0.79 | 1 | 88 | 1 | stated in 1 doc(s) ^[m-als-fundament-der-simulation.md:L194] |
| Kontrollraum | Überwelt | 0.45 | 7 | 82 | 4 | stated in 1 doc(s) ^[paradoxien-der-kohaerenz-protokoll-entwicklung.md:L344] |
| Unterdrückung | Suppression | 0.54 | 80 | 9 | 2 | proposed |
| Alter | Key Part | 0.49 | 87 | 1 | 1 | stated in 1 doc(s) ^[an-introduction-to-the-concepts-of-coherence-protocol.md:L63] |
| Kernkonflikt | Paradoxon X | 0.56 | 55 | 33 | 12 | stated in 1 doc(s) ^[entwicklungsstrategie-fuer-kohaerenz-protokoll.md:L91] |
| Trivialisierung | Explosion | 0.74 | 15 | 72 | 10 | stated in 2 doc(s) ^[logik-trifft-transzendente-entitaet.md:L158] ^[logik-trifft-transzendente-entitaet-2.md:L158] |
| Innere Weite | Überwelt | 0.63 | 5 | 82 | 5 | stated in 1 doc(s) ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L837] ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L962] |
| Regelbefolgung | Order | 0.59 | 3 | 84 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-duale-dramatica-storyform-synthese.md:L71] |
| Wächter | guardian | 0.67 | 82 | 5 | 0 | proposed |
| TeV-Brane | Consciousness | 0.48 | 2 | 84 | 1 | stated in 1 doc(s) ^[reality-s-isomorphic-architecture-explained.md:L419] |
| Gefüge | Structure | 0.73 | 29 | 57 | 5 | proposed |
| Unterdrückung | Repression | 0.59 | 80 | 6 | 2 | proposed |
| Anker | Containment | 0.70 | 71 | 14 | 5 | stated in 1 doc(s) ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L197] |
| Berechnung | Computation | 0.74 | 66 | 19 | 9 | proposed |
| Unsicherheit | Free Energy | 0.52 | 72 | 13 | 5 | stated in 1 doc(s) ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:L81] |
| They | Objective Story Throughline | 0.53 | 78 | 7 | 3 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L39] ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L116] |
| Schatten | Shadow | 0.74 | 58 | 27 | 10 | proposed |
| Protektor | Alex | 0.54 | 18 | 66 | 15 | stated in 2 doc(s) ^[charaktermodellierung-mit-aieos-schema.md:L69] ^[weltenkonzept-fuer-kohaerenz-protokoll-tsdp-basiert.md:L61] |
| Überwelt | Code-Architekturen | 0.48 | 82 | 2 | 2 | stated in 2 doc(s) ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L273] ^[genesis-mehrstufige-recherche-und-ausformulierung.md:L263] |
| Guardian-Dimension | Überwelt | 0.40 | 2 | 82 | 2 | stated in 2 doc(s) ^[kohaerenz-protokoll-konzept.md:L219] ^[recherche-kohaerenz-protokoll.md:L23] |
| Inkohärenz | Vorhersagefehler | 0.47 | 80 | 4 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptionelle-ausarbeitung.md:L396] |
| Riss | fissure | 0.64 | 83 | 1 | 1 | proposed |
| Ausrichtung | Alignment | 0.67 | 33 | 50 | 9 | proposed |
| Überwelt | Digital Overworld | 0.56 | 82 | 1 | 1 | stated in 1 doc(s) ^[aegis-genesis-crisis-self-definition.md:L99] |
| tun | Do | 0.53 | 43 | 40 | 6 | proposed |
| Emergente | Emergent | 0.54 | 28 | 55 | 12 | proposed |
| Große System-Monitor | Überwelt | 0.67 | 1 | 82 | 1 | stated in 1 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L460] |
| Symmetrie | Verschachtelte Ordnung | 0.46 | 82 | 1 | 1 | stated in 1 doc(s) ^[konzeptanalyse-kohaerenz-protokoll-s-fundament.md:L223] |
| Löschungsangriff | Action | 0.52 | 1 | 81 | 1 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse.md:L91] |
| Aegis | Algorithmus | 0.44 | 34 | 48 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L122] |
| Kognitiv | Cognitive | 0.78 | 10 | 72 | 2 | proposed |
| Digitale | Digital | 0.62 | 25 | 57 | 9 | proposed |
| Personas | Teilen | 0.58 | 13 | 69 | 7 | stated in 3 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik.md:L21] ^[kael-charakterarchitektur-und-konfliktdynamik-2.md:L21] |
| Signatur | Signature | 0.53 | 70 | 12 | 4 | proposed |
| NP-Suche | Exploration | 0.65 | 2 | 79 | 1 | stated in 1 doc(s) ^[p-vs-np-und-kohaerenz.md:L413] |
| einfrieren | Freeze | 0.52 | 7 | 74 | 3 | proposed |
| We | Subjective Story Throughline | 0.39 | 80 | 1 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L39] ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L114] |
| Tod | death | 0.73 | 59 | 22 | 4 | proposed |
| Aussicht | view | 0.54 | 2 | 78 | 0 | proposed |
| Mentales Unbehagen | Dissonanz | 0.76 | 1 | 79 | 1 | stated in 1 doc(s) ^[aegis-genesis-krise-konzeptioneller-rahmen.md:L464] |
| Limina | Gatekeeper | 0.58 | 14 | 66 | 9 | stated in 2 doc(s) ^[charakter-kompilation-fuer-kohaerenz-protokoll.md:L326] ^[roman-konzept-dualitaet-kohaerenz-spannung.md:L40] |
| Klang | Resonance | 0.79 | 30 | 50 | 0 | proposed |
| KW2 | Archipelago | 0.46 | 75 | 4 | 4 | stated in 1 doc(s) ^[refining-dramatica-storyform-for-kohaerenz-protokoll.md:L220] |
| Beta | Effizienz | 0.40 | 7 | 72 | 4 | stated in 1 doc(s) ^[kohaerenz-protokoll.md:L1814] |
| Grenzfeste | Cerberus-Labyrinth | 0.51 | 32 | 47 | 8 | stated in 1 doc(s) ^[kohaerenz-protokoll-projekt-rekonstruktion.md:L67] |
| Memory | File System | 0.48 | 78 | 1 | 1 | stated in 1 doc(s) ^[comprehensive-systemic-architectural-and-psychological-conte.md:L71] |
| Trauma-Echos | Inkonsistenzen | 0.56 | 5 | 74 | 1 | stated in 1 doc(s) ^[hard-sf-roman-outline-dkt-physik-cosmic-horror.md:L73] |
| Archiv | Archive | 0.56 | 25 | 53 | 7 | proposed |
| LogOS | Construct City | 0.37 | 67 | 11 | 8 | stated in 1 doc(s) ^[an-ontological-and-systemic-overview-of-the-coherence-protoc.md:L89] |
| objektiv | Objective | 0.54 | 37 | 41 | 11 | proposed |
| Selbststrukturierung | Stabilisierung | 0.54 | 3 | 75 | 2 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L299] |
| Änderung | Change | 0.54 | 33 | 44 | 6 | proposed |
| entropie | Entropy | 0.77 | 9 | 68 | 5 | proposed |
| Universe | Fixed Situation | 0.63 | 76 | 1 | 1 | stated in 1 doc(s) ^[dramatica-storyform-kohaerenz-protokoll.md:L34] |
| KW2 | Mnemosyne Archipelago | 0.46 | 75 | 2 | 2 | stated in 1 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L446] |
| Zustands-Begrenzung | Universe | 0.78 | 1 | 76 | 1 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-analyse.md:L59] |
| Kind | Exile | 0.56 | 58 | 18 | 5 | stated in 3 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik.md:L55] ^[kael-charakterarchitektur-und-konfliktdynamik-2.md:L55] |
| Argus | Observer | 0.51 | 54 | 21 | 10 | stated in 3 doc(s) ^[thematic-architecture-of-kohaerenz-protokoll-a-conceptual-le.md:L77] ^[project-status-report-kohaerenz-protokoll-canonical-state-st.md:L11] |
| Entsprechung | Correspondence | 0.74 | 28 | 47 | 5 | proposed |
| Digitale | digital | 0.61 | 25 | 50 | 12 | proposed |
| Handlungssystemen Erstarrung | Freeze | 0.73 | 1 | 74 | 1 | stated in 1 doc(s) ^[kael-system-tsdp-analyse-und-profile.md:L240] |
| gefrieren | Freeze | 0.59 | 1 | 74 | 0 | proposed |
| Rationalismus | LogOS | 0.59 | 8 | 67 | 3 | stated in 1 doc(s) ^[roman-konzept-dualitaet-kohaerenz-spannung.md:L40] |
| Maschine | Person of Interest | 0.67 | 73 | 2 | 2 | stated in 1 doc(s) ^[romananfang-leere-und-systemgenesis.md:L60] |
| Bibliothek | Library | 0.73 | 23 | 51 | 3 | proposed |
| Einsturz | Collapse | 0.73 | 5 | 69 | 1 | proposed |
| Grund | ground | 0.56 | 52 | 22 | 1 | proposed |
| Handlungsfreiheit | Agency | 0.74 | 4 | 69 | 2 | stated in 1 doc(s) ^[narrative-modelle-und-dramatica-erweiterung.md:L425] |
| Logos-Prime | Construct City | 0.42 | 62 | 11 | 8 | stated in 2 doc(s) ^[the-architecture-of-fracture-a-compendium-of-the-kael-system.md:L64] ^[the-psychological-mechanics-from-tertiary-structural-dissoci.md:L57] |
| Eindringen | Intrusion | 0.67 | 26 | 47 | 8 | proposed |
| Shadow | Fight | 0.59 | 27 | 46 | 7 | stated in 1 doc(s) ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L264] ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L532] |
| K₀ | Intrusion | 0.37 | 26 | 47 | 6 | stated in 3 doc(s) ^[the-architecture-of-being-a-philosophical-thesis-on-the-core.md:L30] ^[a-critical-evaluation-of-the-coherence-protocol-frameworks-s.md:L65] |
| Direktive | Directive | 0.62 | 55 | 17 | 1 | proposed |
| Grenzfläche | Interface | 0.78 | 14 | 58 | 8 | stated in 2 doc(s) ^[kohaerenz-protokoll-synthese-integration.md:L103] ^[storyforms-system-mind-bewusstsein.md:L126]; proposed |
| Symmetrie des Selbst | Monster | 0.42 | 1 | 71 | 1 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L285] |
| Schatten | shadow | 0.67 | 58 | 14 | 8 | proposed |
| Protektor | Manager | 0.67 | 18 | 53 | 5 | stated in 1 doc(s) ^[kohaerenz-protokoll-synthese-integration.md:L39] |
| bewahren | PRESERVE | 0.52 | 63 | 8 | 1 | proposed |
| Ablehnung | Klassische Erzwingung | 0.71 | 69 | 1 | 1 | stated in 1 doc(s) ^[dialetheismus-im-kohaerenz-protokoll.md:L252] |
| Unterstreicht die Themen Handlungsfähigkeit | Agency | 0.46 | 1 | 69 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L585] |
| Zunehmende Handlungsfähigkeit | Agency | 0.73 | 1 | 69 | 1 | stated in 1 doc(s) ^[roman-konzept-kael-aegis-simulation.md:L115] |
| Bunker | Cerberus-Labyrinth | 0.62 | 23 | 47 | 6 | stated in 1 doc(s) ^[deconstructing-reality-s-architecture.md:L174] |
| Klassen | Class | 0.41 | 17 | 53 | 6 | proposed |
| Harte | hard | 0.61 | 14 | 56 | 4 | proposed |
| Überprüfung | Verification | 0.50 | 36 | 34 | 8 | proposed |
| Absicht | Intent | 0.77 | 50 | 19 | 6 | proposed |
| Anagnorisis | Einsicht | 0.78 | 2 | 67 | 2 | stated in 1 doc(s) ^[aegis-paradoxon-neukonzeption-und-analyse-docx.md:L38] |
| entropisch | Entropic | 0.68 | 8 | 61 | 4 | proposed |
| Rein | pure | 0.56 | 14 | 55 | 1 | proposed |
| Ausführung | Doing | 0.66 | 54 | 14 | 2 | proposed |
| C-System-Strategie | LogOS | 0.56 | 1 | 67 | 1 | stated in 1 doc(s) ^[parakonsistente-logik-im-seelen-protokoll.md:L241] |
| Unversehrtheit | Integrity | 0.70 | 1 | 67 | 0 | proposed |
| Modellierung | MODELING | 0.67 | 63 | 5 | 1 | proposed |
| Bewegung | motion | 0.55 | 60 | 7 | 1 | proposed |
| Dao | Fluss | 0.49 | 3 | 64 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md.md:L439] |
| Entfremdung | Defamiliarization | 0.78 | 65 | 2 | 2 | stated in 1 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L116] |
| Dualität | Duality | 0.66 | 55 | 12 | 5 | proposed |
| Eins | One | 0.50 | 12 | 55 | 0 | proposed |
| Instanz | instance | 0.75 | 51 | 16 | 1 | proposed |
| Institut | Institute | 0.56 | 12 | 55 | 2 | proposed |
| OR | Reduktion | 0.65 | 10 | 57 | 6 | stated in 1 doc(s) ^[kohaerenz-protokoll-inkubation-x.md:L66] |
| Entropisches Trauma | Nichts Rauschen | 0.45 | 1 | 65 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L92] |
| Eros | Liebe | 0.46 | 8 | 58 | 1 | stated in 1 doc(s) ^[junas-liebe-kaels-trauma-aegis-docx.md:L128] |
| Feldfluktuationen | Nichts Rauschen | 0.62 | 1 | 65 | 1 | stated in 1 doc(s) ^[genesis-finale-prosa-angepasste-ich-natur.md:L73] |
| Vielfalt | Law of Requisite Variety | 0.74 | 56 | 10 | 6 | stated in 1 doc(s) ^[aegis-singularitaet-jenseits-entropiegleichung-2.md:L68] |
| Stufe | stage | 0.54 | 37 | 29 | 0 | proposed |
| Vielfalt | Variety | 0.51 | 56 | 10 | 6 | proposed |
| Bewegung | Movement | 0.58 | 60 | 5 | 1 | proposed |
| Logos-Prime | Construct-City | 0.52 | 62 | 3 | 1 | stated in 1 doc(s) ^[systemic-architecture-specification-the-coherence-protocol-w.md:L59] |
| Traumatisches Wissen | Flashbacks | 0.48 | 2 | 63 | 2 | stated in 2 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L388] ^[ki-rolle-aegis-genesis-fragestellungen.md:L364] |
| Garten | Garden | 0.74 | 47 | 18 | 3 | proposed |
| Grund | Reason | 0.58 | 52 | 13 | 2 | proposed |
| Polyphonie | Intrusion | 0.76 | 18 | 47 | 3 | stated in 1 doc(s) ^[kernwelten-und-fragmentierte-wahrnehmung.md:L327] |
| Quantenverschränkung | quantum entanglement | 0.76 | 49 | 16 | 5 | proposed |
| Vermutung | hypothesis | 0.64 | 23 | 42 | 1 | proposed |
| Kern-Welten | Core Worlds | 0.72 | 25 | 39 | 1 | proposed |
| Grad | Degree | 0.65 | 53 | 11 | 3 | proposed |
| Kairos-Potentialis | Möglichkeits-Garten | 0.41 | 42 | 22 | 4 | stated in 1 doc(s) ^[welt.md:L59] ^[welt.md:L108] |
| Kreativ | creative | 0.54 | 13 | 51 | 4 | proposed |
| NP-Härte | Schwierigkeit | 0.50 | 1 | 63 | 1 | stated in 1 doc(s) ^[p-vs-np-und-kohaerenz.md:L328] |
| Tod | Abyssos | 0.74 | 59 | 4 | 1 | stated in 1 doc(s) ^[konzept-expose-schwarzschild-protokoll-optimierung.md:L229] |
| Bewegung | Motion | 0.65 | 60 | 3 | 1 | proposed |
| Kernwelt KW1 | Logos-Prime | 0.73 | 1 | 62 | 1 | stated in 1 doc(s) ^[narrative-physik-attraktoren-leserbewusstsein.md:L91] |
| Konstruktstadt | Logos-Prime | 0.74 | 1 | 62 | 1 | stated in 1 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L236] |
| Phänomenologie | Subjektive Erfahrung | 0.51 | 52 | 11 | 10 | stated in 1 doc(s) ^[kohaerenz-protokoll-thematische-tiefenanalyse.md:L298] |
| Meta-Beobachter | Argus | 0.62 | 8 | 54 | 7 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L156] |
| K₀-Dominant | Entropic | 0.48 | 1 | 61 | 1 | stated in 1 doc(s) ^[projektplanung-fuer-kohaerenz-protokoll.md:L43] |
| Schichten | layers | 0.71 | 42 | 20 | 2 | proposed |
| EINE | One | 0.69 | 6 | 55 | 1 | proposed |
| Schema | schema | 0.49 | 48 | 13 | 10 | proposed |
| Kairos-Potentialis | Garden | 0.76 | 42 | 18 | 9 | stated in 1 doc(s) ^[deconstructing-reality-s-architecture.md:L190] |
| Grund | Ground | 0.62 | 52 | 8 | 0 | proposed |
| unendlich | Infinite | 0.75 | 48 | 12 | 4 | proposed |
| Nicht-Lokalität | Quantenverschränkung | 0.54 | 11 | 49 | 7 | stated in 1 doc(s) ^[kohaerenz-protokoll-projekt-rekonstruktion.md:L155] |
| Grund | Base | 0.60 | 52 | 7 | 0 | proposed |
| Große | Big | 0.66 | 24 | 35 | 5 | proposed |
| Fassade | front | 0.74 | 50 | 9 | 0 | proposed |
| Kämpfen | Fight | 0.60 | 13 | 46 | 3 | proposed |
| Vermutung | Hypothesis | 0.77 | 23 | 36 | 1 | proposed |
| Mosaik | MOSAIC | 0.67 | 58 | 1 | 1 | proposed |
| Arten | Kinds | 0.75 | 54 | 4 | 2 | proposed |
| Konstante | Constant | 0.76 | 50 | 8 | 1 | proposed |
| UMWELT | environment | 0.69 | 1 | 57 | 0 | proposed |
| K0 | Erasure | 0.69 | 26 | 31 | 13 | stated in 1 doc(s) ^[kohaerenz-protokoll-architecture-synthesis-2.md:L23] |
| K₀ | Erasure | 0.43 | 26 | 31 | 9 | stated in 1 doc(s) ^[kohaerenz-protokoll-architecture-synthesis.md:L23] |
| Steuerung | Governance | 0.66 | 48 | 9 | 4 | proposed |
| Gödel-Satz | Gödel's theorem | 0.61 | 56 | 1 | 0 | proposed |
| Polyphonie | Impulse | 0.50 | 18 | 39 | 1 | stated in 1 doc(s) ^[kernwelten-und-fragmentierte-wahrnehmung.md:L328] |
| Analytiker | Rationalist | 0.47 | 20 | 36 | 7 | stated in 4 doc(s) ^[charaktere.md:L203] ^[forschungsauftrag-spannungspunktanalyse-und-charakterausarbe.md:L187] |
| Beschützer | Praetor | 0.71 | 43 | 13 | 4 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L419] |
| Gesamtsystem | Definition des Agency Systems | 0.52 | 55 | 1 | 1 | stated in 1 doc(s) ^[roman-assistenz-kohaerenz-und-weltgestaltung.md:L113] |
| Protector | Firefighter | 0.52 | 41 | 15 | 5 | stated in 1 doc(s) ^[kael-s-dissociative-architecture-analysis.md:L232] |
| Stufe | step | 0.73 | 37 | 19 | 0 | proposed |
| Angleichung | Alignment | 0.59 | 5 | 50 | 0 | proposed |
| Architekt | Architect | 0.79 | 44 | 11 | 2 | proposed |
| Furcht | Dread | 0.79 | 40 | 15 | 9 | stated in 2 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L67] ^[genesis-recherche-anleitung-umsetzung.md:L1079]; proposed |
| Drei | Three | 0.62 | 38 | 17 | 3 | proposed |
| Facetten | Personas | 0.52 | 42 | 13 | 3 | stated in 1 doc(s) ^[in-teil-2-werden-die-persona-von-ihren-spezifis.md:L13] |
| Gnosis | Insight | 0.70 | 32 | 23 | 2 | stated in 1 doc(s) ^[managing-ontological-risk-defining-the-narrative-integration.md:L24] |
| Voraussetzung | Requisite | 0.65 | 45 | 10 | 2 | proposed |
| ANP-Konstellation | Manager | 0.65 | 1 | 53 | 1 | stated in 1 doc(s) ^[neurochemische-lyrik-transzendenz-durch-klang.md:L59] |
| Wächterin | ISH | 0.55 | 30 | 24 | 5 | stated in 1 doc(s) ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L217] ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L721] |
| Intention | Intent | 0.50 | 35 | 19 | 4 | proposed |
| Nicht-Sein | nothingness | 0.74 | 38 | 16 | 3 | proposed |
| Resonanzlandschaft | Mnemosyne-Archipel | 0.77 | 2 | 51 | 2 | stated in 1 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L237] |
| Mnemosyne-Archipel | Swamp | 0.59 | 51 | 2 | 2 | stated in 1 doc(s) ^[deconstructing-reality-s-architecture.md:L159] |
| ursprünglich | Primordial | 0.56 | 48 | 5 | 0 | proposed |
| Sensoren | Sensors | 0.72 | 52 | 1 | 1 | proposed |
| Fassade | façade | 0.67 | 50 | 2 | 0 | proposed |
| Identitäten | Per-Alter Visual Identities | 0.60 | 51 | 1 | 1 | stated in 1 doc(s) ^[roman-assistenz-kohaerenz-und-weltgestaltung.md:L57] |
| Ursprungs-Ich | Innensicht | 0.44 | 48 | 4 | 3 | stated in 1 doc(s) ^[aegis-genesis-krise-konzeptioneller-rahmen.md:L798] |
| Vergessen | Oblivion | 0.66 | 21 | 31 | 6 | proposed |
| Betriebssystem | Workflow | 0.44 | 32 | 19 | 6 | stated in 1 doc(s) ^[projektanalyse-kohaerenz-protokoll-dis.md:L133] |
| Reparatur | Repair | 0.76 | 43 | 8 | 0 | proposed |
| Seele | Soul | 0.64 | 40 | 11 | 5 | proposed |
| Autopoietische | Autopoietic | 0.75 | 26 | 24 | 7 | proposed |
| Belastung | Burden | 0.61 | 44 | 6 | 0 | proposed |
| Cerberus-Labyrinth | Border Fortress | 0.71 | 47 | 3 | 3 | stated in 1 doc(s) ^[systemic-architecture-specification-the-coherence-protocol-w.md:L69] |
| Boundary-Korrelationen | Verschränkung | 0.45 | 2 | 48 | 2 | stated in 2 doc(s) ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L149] ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L191] |
| Klassisch | Classical | 0.79 | 10 | 40 | 4 | proposed |
| Dissoziativer Identitätsstörung | Dissociative Identity Disorder | 0.71 | 6 | 44 | 1 | proposed |
| Tun | Do | 0.66 | 10 | 40 | 1 | proposed |
| EPR-Paare | Quantenverschränkung | 0.62 | 1 | 49 | 1 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L92] |
| Ontologische Transposition | Alternative | 0.56 | 1 | 48 | 1 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-analyse.md:L17] ^[dramatica-dual-storyform-mapping-analyse.md:L169] |
| Aufmerksamkeit | Dual Awareness | 0.45 | 47 | 2 | 1 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L143] |
| Kollaps-Kernel | Erasure | 0.75 | 18 | 31 | 6 | stated in 1 doc(s) ^[kohaerenz-protokoll-synthese-integration.md:L98] |
| Fleck | Spot | 0.73 | 35 | 14 | 2 | proposed |
| Fragilität | brittleness | 0.59 | 47 | 2 | 0 | proposed |
| K1 | Mutual Information | 0.52 | 26 | 23 | 10 | stated in 1 doc(s) ^[systemic-architecture-specification-the-coherence-protocol-w.md:L21] |
| Knoten | nodes | 0.66 | 40 | 9 | 1 | proposed |
| Loch | hole | 0.76 | 32 | 17 | 8 | proposed |
| Rückzug | Withdrawal | 0.51 | 47 | 2 | 0 | proposed |
| Vektor | vector | 0.73 | 33 | 16 | 2 | proposed |
| Protektor | protector | 0.59 | 18 | 30 | 2 | proposed |
| Protokoll der Exzision | Rückzug | 0.53 | 1 | 47 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L119] |
| Außen | Outside | 0.68 | 40 | 7 | 3 | proposed |
| Kreativ | Creative | 0.76 | 13 | 34 | 6 | proposed |
| Gewebe | Fabric | 0.74 | 41 | 6 | 1 | proposed |
| Posttraumatische Belastungsstörung | PTSD | 0.42 | 15 | 32 | 10 | proposed |
| Stillstand | Stasis | 0.59 | 29 | 18 | 3 | proposed |
| Zeuge | Witness | 0.78 | 21 | 26 | 11 | proposed |
| Akte | Signposts | 0.71 | 38 | 8 | 1 | stated in 1 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L120] ^[dramatica-storyform-validierung-und-synthese.md:L326] |
| Beschützer | Feuerbekämpfer | 0.62 | 43 | 3 | 3 | stated in 1 doc(s) ^[tsdp-analyse-kohaerenz-protokoll-charaktere.md:L107] |
| Kernlogik | CLIK | 0.49 | 45 | 1 | 1 | stated in 1 doc(s) ^[aegis-logik-in-der-leere-docx.md:L211] |
| rechnerisch | Computational | 0.76 | 8 | 38 | 3 | proposed |
| Widerspruchsfreiheit | Consistency | 0.75 | 22 | 24 | 4 | proposed |
| Genre-Ebene | Domain | 0.63 | 2 | 44 | 1 | stated in 1 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L90] |
| Felder | Fields | 0.53 | 34 | 12 | 3 | proposed |
| Gödel-Gambit | Living Paradox | 0.54 | 42 | 4 | 3 | stated in 1 doc(s) ^[kael-s-dissociative-architecture-analysis.md:L244] |
| Herzstück | heart | 0.75 | 21 | 25 | 0 | proposed |
| Reste | remains | 0.53 | 10 | 36 | 0 | proposed |
| Verifizierung | Verification | 0.75 | 12 | 34 | 2 | proposed |
| Ausführen | Do | 0.54 | 5 | 40 | 0 | proposed |
| Erzwingen des System-Kollapses | Change | 0.76 | 1 | 44 | 1 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse-2.md:L155] |
| Einheiten | Slots | 0.70 | 35 | 10 | 2 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L61] |
| Kairos-Potentialis | Garden of Possibility | 0.66 | 42 | 3 | 1 | stated in 1 doc(s) ^[welcome-to-the-coherence-protocol-a-beginner-s-guide.md:L84] |
| Schichten | LoA | 0.67 | 42 | 3 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-themenanalyse-und-anreicheru.md:L182] |
| Koexistenz | Coexistence | 0.79 | 42 | 2 | 0 | proposed |
| Metaphysisches Subsystem | OS | 0.47 | 1 | 43 | 1 | stated in 1 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L63] |
| Systemischer Konflikt | OS | 0.46 | 1 | 43 | 1 | stated in 1 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L85] |
| OS | They-Throughline | 0.68 | 43 | 1 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L426] |
| Zweiter | Second | 0.77 | 17 | 27 | 2 | proposed |
| BMS | Firewall | 0.68 | 1 | 42 | 1 | stated in 1 doc(s) ^[aegis-logik-in-der-leere-docx.md:L191] |
| Kaskade | Cascade | 0.78 | 37 | 6 | 1 | proposed |
| komputational | Computational | 0.79 | 5 | 38 | 2 | proposed |
| Kairos-Potentialis | Emergent Space | 0.68 | 42 | 1 | 1 | stated in 1 doc(s) ^[aegis-manifest-genesis-krise-reboot-2.md:L142] |
| UMWELT | Environmental | 0.64 | 1 | 42 | 0 | proposed |
| GUT | Good | 0.55 | 3 | 40 | 0 | proposed |
| Kairos-Potentialis | Garden of Potential | 0.61 | 42 | 1 | 1 | stated in 1 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L971] |
| Griess | Generation | 0.41 | 12 | 31 | 5 | stated in 1 doc(s) ^[monstergruppe-als-denkmodell-der-komplexitaet.md:L60] |
| Horrors | TF-2 | 0.46 | 42 | 1 | 1 | stated in 1 doc(s) ^[roman-entwicklung-ontologie-trauma-horror.md:L140] |
| Nicht-Sein | Selbstauslöschung | 0.48 | 38 | 5 | 2 | stated in 1 doc(s) ^[aegis-logik-in-der-leere-docx.md:L55] |
| Schwelle | Threshold | 0.75 | 31 | 12 | 6 | proposed |
| Stasis | Stagnation | 0.50 | 18 | 25 | 3 | proposed |
| Vollständigkeit | Wholeness | 0.56 | 31 | 12 | 2 | stated in 1 doc(s) ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L63]; proposed |
| Außen | outward | 0.51 | 40 | 2 | 0 | proposed |
| Dramatica-Struktur | Storyform | 0.72 | 6 | 36 | 5 | stated in 1 doc(s) ^[kohaerenz-protokoll-dramatica-synthese-masterkonzept.md:L175] |
| Unvollständigkeitssatz | Gödel's incompleteness theorem | 0.76 | 39 | 3 | 1 | proposed |
| K1 | Storyform A | 0.50 | 26 | 16 | 8 | stated in 1 doc(s) ^[ki-prompt-analyse-hard-problem-of-consciousness.md:L352] |
| Knoten | vertices | 0.79 | 40 | 2 | 0 | proposed |
| Kohärenz-Protokoll | coherence protocol | 0.73 | 36 | 6 | 1 | proposed |
| Masse | Trägheit | 0.44 | 32 | 10 | 3 | stated in 1 doc(s) ^[kohaerenz-protokoll-dramatica-synthese-masterkonzept.md:L73] |
| Meister | Master | 0.45 | 7 | 35 | 2 | proposed |
| Schützer | Protector | 0.77 | 1 | 41 | 0 | proposed |
| Stufe | Stage | 0.71 | 37 | 5 | 1 | proposed |
| Toleranz | Tolerance | 0.73 | 30 | 12 | 4 | proposed |
| Verdrängung | repression | 0.54 | 36 | 6 | 3 | proposed |
| schwach | Weak | 0.76 | 32 | 10 | 2 | proposed |
| Befreiung | Unburdening | 0.59 | 29 | 12 | 2 | proposed |
| Fleck | spot | 0.60 | 35 | 6 | 1 | proposed |
| Wahrnehmungsmanipulation | Gaslighting | 0.63 | 3 | 38 | 3 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptentwicklung.md:L151] |
| Knoten | Prozess-Hub | 0.48 | 40 | 1 | 1 | stated in 1 doc(s) ^[logiksystem-aegis-entwicklungsszenarien-docx.md:L99] |
| Limit | Timelock-Countdown | 0.55 | 40 | 1 | 1 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-analyse.md:L71] |
| Währung des Unbekannten | Neugier | 0.56 | 1 | 40 | 1 | stated in 1 doc(s) ^[narrative-entropie-existenzielle-bedrohung-des-romans.md:L68] |
| Rationaler | Rationalist | 0.58 | 5 | 36 | 1 | proposed |
| Co₁ | Conway | 0.50 | 22 | 18 | 5 | stated in 1 doc(s) ^[kohaerenz-protokoll-umfassendes-konzept.md:L29] |
| Instantiation of the Kernwelten | Core Worlds | 0.72 | 1 | 39 | 1 | stated in 1 doc(s) ^[aegis-manifest-genesis-krise-reboot.md:L63] |
| I-Throughline | Main Character | 0.69 | 1 | 39 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L133] |
| IC | Repräsentiert die Impact Character | 0.41 | 39 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-detaillierte-recherche.md:L206] |
| Operationale | Operational | 0.56 | 20 | 20 | 2 | proposed |
| Relationaler | Relational | 0.40 | 8 | 32 | 2 | proposed |
| AEGIS-Botschaft | Gaslighting | 0.49 | 1 | 38 | 1 | stated in 1 doc(s) ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L913] |
| AEGIS-Intrusion | Gaslighting | 0.65 | 1 | 38 | 1 | stated in 1 doc(s) ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L813] |
| Aegis | Prefrontal Cortex | 0.50 | 34 | 5 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L82] |
| Rand | Border | 0.55 | 35 | 4 | 0 | proposed |
| Chaostheorie | Strange Attractors | 0.63 | 34 | 5 | 5 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L187] |
| Unwirklichkeit der Umwelt | Derealisation | 0.60 | 1 | 38 | 1 | stated in 1 doc(s) ^[narrativ-existenzieller-kohaerenz-nzt-protokoll.md:L82] |
| Gaslighting | Externe Manipulation | 0.50 | 38 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-themenanalyse-und-anreicheru.md:L54] |
| Leitlinien | Guidelines | 0.77 | 21 | 18 | 5 | proposed |
| Humes Problem der Induktion | Mustererkennung | 0.54 | 3 | 36 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L184] |
| Repräsentiert die Main Character | MC | 0.64 | 1 | 38 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-detaillierte-recherche.md:L204] |
| Ausbeutung | Exploit | 0.55 | 5 | 33 | 0 | proposed |
| Kreativer | Creative | 0.38 | 4 | 34 | 0 | proposed |
| Verdrängung | Displacement | 0.65 | 36 | 2 | 0 | proposed |
| Gruppen | Finite Simple Groups | 0.62 | 35 | 3 | 3 | stated in 1 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L99] |
| Funke | Ignition | 0.60 | 33 | 5 | 0 | proposed |
| Spielen | Gaming | 0.57 | 16 | 22 | 3 | proposed |
| Integratorin | ISH | 0.36 | 14 | 24 | 4 | stated in 2 doc(s) ^[charaktermodellierung-mit-aieos-schema.md:L143] ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:L53] |
| Offenbarung | Revelation | 0.77 | 24 | 14 | 4 | proposed |
| Stark | Strong | 0.76 | 25 | 13 | 4 | proposed |
| Logisches System | Aegis | 0.40 | 3 | 34 | 1 | stated in 1 doc(s) ^[aegis-seele-und-entropie.md:L114] |
| Bodenschicht | Elements | 0.78 | 1 | 36 | 1 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-analyse.md:L93] |
| Interne Konsistenz | Coherence Theory | 0.76 | 6 | 31 | 1 | stated in 1 doc(s) ^[narrative-kernentwicklung-aegis-und-system-kael.md:L115] |
| Erason-Operator | Oblivion | 0.58 | 6 | 31 | 6 | stated in 1 doc(s) ^[editorial-style-dossier-somatic-and-linguistic-implementatio.md:L45] |
| Glauben | beliefs | 0.40 | 21 | 16 | 0 | proposed |
| Inseln | Islands | 0.70 | 25 | 12 | 2 | proposed |
| Bewusstwerdung | K-J Verbindung | 0.58 | 19 | 17 | 3 | stated in 1 doc(s) ^[kohaerenz-protokoll.md:L797] |
| Schwarzes | black | 0.75 | 16 | 20 | 6 | proposed |
| Schöpfer | creator | 0.66 | 31 | 5 | 0 | proposed |
| Shutdown | Submit | 0.54 | 25 | 11 | 3 | stated in 1 doc(s) ^[kohaerenz-prozess-grundlagen.md:L173] |
| Sog | suction | 0.75 | 35 | 1 | 0 | proposed |
| Akzeptanz des Widerspruchs | Parakonsistente Logik | 0.74 | 4 | 31 | 3 | stated in 2 doc(s) ^[logik-trifft-transzendente-entitaet.md:L182] ^[logik-trifft-transzendente-entitaet-2.md:L180] |
| Verhaltensbezogen | Behavioral | 0.62 | 1 | 34 | 0 | proposed |
| Beschränkung | Constraint | 0.68 | 10 | 25 | 1 | proposed |
| Gefüge | Fabric | 0.76 | 29 | 6 | 0 | proposed |
| Funke | ignition | 0.51 | 33 | 2 | 0 | proposed |
| Funke | spark | 0.76 | 33 | 2 | 1 | proposed |
| Grenzfläche | interface | 0.58 | 14 | 21 | 0 | proposed |
| Richtlinien | Guidelines | 0.69 | 17 | 18 | 3 | proposed |
| Landauer-Prinzip | Preis der Information | 0.63 | 34 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-synthese-integration.md:L78] |
| Lüge | lie | 0.73 | 20 | 15 | 1 | proposed |
| Modul | module | 0.62 | 30 | 5 | 1 | proposed |
| Sturm | Storm | 0.69 | 30 | 5 | 3 | proposed |
| Domain Physics | Activity | 0.68 | 3 | 31 | 1 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse-2.md:L209] |
| Aufforderung | Prompt | 0.54 | 3 | 31 | 1 | proposed |
| Ausgestaltung | Soft Canon | 0.77 | 33 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-projekt-rekonstruktion.md:L21] |
| Ausschluss | LNC | 0.56 | 31 | 3 | 1 | stated in 1 doc(s) ^[dialetheismus-im-kohaerenz-protokoll.md:L307] |
| Betriebssystem | Co₁-Logik | 0.54 | 32 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll.md:L1898] |
| K0 | Erasure Kernel | 0.48 | 26 | 8 | 5 | stated in 1 doc(s) ^[ki-prompt-analyse-hard-problem-of-consciousness.md:L112] |
| K₀ | Erasure Kernel | 0.60 | 26 | 8 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-architecture-synthesis.md:L23] |
| Sprachmodelle | LLMs | 0.69 | 8 | 26 | 7 | stated in 5 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L156] ^[logik-trifft-transzendente-entitaet.md:L200] |
| Nox | Persecutor | 0.54 | 16 | 18 | 4 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L663] |
| seltsam | Strange | 0.66 | 12 | 22 | 0 | proposed |
| Abschaltung | Shutdown | 0.60 | 8 | 25 | 1 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L367] |
| Aussicht | View | 0.50 | 2 | 31 | 1 | proposed |
| Koordination | Coordination | 0.76 | 28 | 5 | 1 | proposed |
| Gebiet | Field | 0.60 | 8 | 25 | 1 | proposed |
| Groß | Grand | 0.48 | 1 | 32 | 0 | proposed |
| Kerne | Kernels | 0.74 | 15 | 18 | 1 | proposed |
| Labor | laboratory | 0.70 | 20 | 13 | 0 | proposed |
| Phaenomena | phenomena | 0.75 | 7 | 26 | 0 | proposed |
| Sturm | storm | 0.59 | 30 | 3 | 1 | proposed |
| Vermutung | conjecture | 0.56 | 23 | 10 | 3 | proposed |
| Klassen | Classes | 0.64 | 17 | 15 | 7 | proposed |
| Krisensituation | Crisis | 0.39 | 1 | 31 | 0 | proposed |
| Dämon | demon | 0.62 | 23 | 9 | 7 | proposed |
| Kanäle | EIC | 0.53 | 18 | 14 | 5 | stated in 1 doc(s) ^[aegis-analyse-und-manifest-postulation.md:L302] |
| K0-Druck | Erasure | 0.61 | 1 | 31 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L68] |
| Flackern | Flicker | 0.58 | 22 | 10 | 4 | proposed |
| Kanal | channel | 0.79 | 27 | 5 | 0 | proposed |
| Lokalität | Locality | 0.76 | 28 | 4 | 1 | proposed |
| somatisch | Somatic | 0.73 | 9 | 23 | 2 | proposed |
| Vektoren | Vectors | 0.59 | 28 | 4 | 1 | proposed |
| Maschinelles Lernen | Adaption | 0.54 | 4 | 27 | 2 | stated in 1 doc(s) ^[paradoxien-der-kohaerenz-protokoll-entwicklung.md:L368] |
| Amygdala | Threat | 0.60 | 14 | 17 | 3 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L162] |
| Beta-Rho-5-Chaos | Hardware | 0.53 | 1 | 30 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll.md:L1898] |
| Kollektiv | Collective | 0.53 | 10 | 21 | 1 | proposed |
| Desire | Subjective Story | 0.51 | 16 | 15 | 7 | stated in 1 doc(s) ^[kohaerenz-protokoll-dramatica-synthese.md:L158] |
| Erdung | Grounding | 0.73 | 8 | 23 | 3 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L88] |
| Insel | Island | 0.50 | 26 | 5 | 0 | proposed |
| Institut | institute | 0.57 | 12 | 19 | 0 | proposed |
| KI-Modell | LLM | 0.55 | 3 | 28 | 2 | stated in 2 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L305] ^[ki-rolle-aegis-genesis-fragestellungen.md:L280] |
| Pforten der Verurteilung | Prüfungen | 0.54 | 2 | 29 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll.md:L436] |
| Wiederholung | Restatement | 0.68 | 28 | 3 | 0 | proposed |
| Stufen | steps | 0.60 | 20 | 11 | 0 | proposed |
| Agnotologie | Ignoranz | 0.74 | 5 | 25 | 3 | stated in 2 doc(s) ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L355] ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L529] |
| Kanäle | Channels | 0.61 | 18 | 12 | 5 | proposed |
| Dramatica-Perspektiven | Throughlines | 0.69 | 2 | 28 | 2 | stated in 2 doc(s) ^[kohaerenz-protokoll-dramatica-synthese.md:L27] ^[kohaerenz-protokoll-dramatica-synthese-masterkonzept.md:L27] |
| Rückkopplung | Feedback Loop | 0.76 | 22 | 8 | 2 | proposed |
| Gleichung | equation | 0.63 | 25 | 5 | 0 | proposed |
| Helferin | ISH | 0.59 | 6 | 24 | 5 | stated in 1 doc(s) ^[charaktere.md:L36] |
| Hinterkopf | Selbstreflexion | 0.69 | 3 | 27 | 1 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L217] |
| Kampf-Reaktion | Persecutor | 0.53 | 12 | 18 | 3 | stated in 1 doc(s) ^[charaktere.md:L147] |
| Konstrukts | constructs | 0.75 | 11 | 19 | 0 | proposed |
| Logik der Formalen Inkonsistenz | LFI | 0.68 | 5 | 25 | 5 | stated in 4 doc(s) ^[kohaerenz-protokoll-analyse-und-synthese.md:L90] ^[kohaerenz-protokoll-detaillierte-recherche.md:L118] |
| Lochs | holes | 0.57 | 10 | 20 | 2 | proposed |
| Merkzeichen | Marker | 0.79 | 9 | 21 | 1 | proposed |
| Überraum | Nexus | 0.75 | 3 | 27 | 3 | stated in 1 doc(s) ^[in-teil-2-werden-die-persona-von-ihren-spezifis.md:L151] |
| Perioden der Stasis | Stillstand | 0.77 | 1 | 29 | 1 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L100] |
| Stufen | Steps | 0.79 | 20 | 10 | 1 | proposed |
| Antagonist-System | Entität AEGIS | 0.52 | 1 | 28 | 1 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-analyse.md:L53] |
| Pfleger | Caregiver | 0.59 | 9 | 20 | 1 | proposed |
| Externe Wahrheit | Correspondence Theory | 0.61 | 1 | 28 | 1 | stated in 1 doc(s) ^[narrative-kernentwicklung-aegis-und-system-kael.md:L115] |
| Offenbarung | Disclosure | 0.74 | 24 | 5 | 0 | proposed |
| Domänen-Verteilung | Throughlines | 0.78 | 1 | 28 | 1 | stated in 1 doc(s) ^[dramatica-storyform-kohaerenz-protokoll-analyse.md:L74] |
| Gleichung | Equation | 0.61 | 25 | 4 | 1 | proposed |
| Trauma-Halter | Exiles | 0.56 | 5 | 24 | 1 | stated in 1 doc(s) ^[roman-konzept-dualitaet-kohaerenz-spannung.md:L43] |
| Gewahrsein | awareness | 0.66 | 5 | 24 | 0 | proposed |
| Hindernis | Obstacle | 0.72 | 24 | 5 | 0 | proposed |
| Katharsis | Reinigung | 0.76 | 20 | 9 | 5 | stated in 1 doc(s) ^[aegis-paradoxon-konzeption-und-analyse.md:L55] |
| Kohärenz-Kern | K₁ | 0.43 | 5 | 24 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-architecture-synthesis.md:L27] |
| Protectors | Managers | 0.61 | 12 | 17 | 5 | stated in 2 doc(s) ^[m-als-fundament-der-simulation.md:L82] ^[reality-s-isomorphic-architecture-explained.md:L397] |
| zweites | Second | 0.49 | 2 | 27 | 0 | proposed |
| Somatischer | Somatic | 0.49 | 6 | 23 | 1 | proposed |
| Witness Function | Verifier | 0.66 | 14 | 15 | 10 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L179] |
| Autopoietische | self-producing | 0.72 | 26 | 2 | 0 | proposed |
| Sperre | Block | 0.70 | 2 | 26 | 1 | proposed |
| C-Systeme | LFI | 0.77 | 3 | 25 | 2 | stated in 1 doc(s) ^[parakonsistente-logik-fuer-kohaerenz-protokoll.md:L326] |
| Pflegender | Caregiver | 0.60 | 8 | 20 | 1 | proposed |
| Glitchwyrm | Leech | 0.52 | 1 | 27 | 1 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L596] ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L647] |
| Kernparadoxon | core paradox | 0.74 | 26 | 2 | 0 | proposed |
| Täter | Perpetrator | 0.73 | 19 | 9 | 3 | proposed |
| Plot-Ebene | Type | 0.53 | 4 | 24 | 2 | stated in 1 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L91] |
| TSDP-Modell | Tertiäre Strukturelle Dissoziation | 0.77 | 8 | 20 | 2 | stated in 1 doc(s) ^[duale-storyform-synthese-kohaerenz-protokoll.md:L158] |
| Abspaltung | Exzision | 0.75 | 21 | 6 | 1 | stated in 1 doc(s) ^[integriertes-kohaerenz-protokoll-erstellung.md:L51] |
| Assistent | Helper | 0.60 | 8 | 19 | 0 | proposed |
| C-System | LFI | 0.71 | 2 | 25 | 1 | stated in 1 doc(s) ^[parakonsistente-logik-fuer-kohaerenz-protokoll.md:L292] ^[parakonsistente-logik-fuer-kohaerenz-protokoll.md:L300] |
| Titration | Container | 0.59 | 12 | 15 | 5 | stated in 1 doc(s) ^[kohaerenz-protokoll-dramatica-synthese-masterkonzept.md:L228] |
| Wärmetod | Informational Heat Death | 0.72 | 24 | 3 | 3 | stated in 2 doc(s) ^[dramatica-storyform-synthese-aegis-analyse-2.md:L19] ^[kohaerenz-protokoll-audit-und-verifizierung.md:L13] |
| Inseln | islands | 0.77 | 25 | 2 | 1 | proposed |
| Konstrukten | constructs | 0.53 | 8 | 19 | 0 | proposed |
| Relation | RELATION | 0.76 | 26 | 1 | 0 | proposed |
| Glauben | Beliefs | 0.63 | 21 | 5 | 0 | proposed |
| Beziehungsgeschichte | RS | 0.70 | 3 | 23 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-architecture-synthesis-2.md:L72] |
| Echtzeit | real-time | 0.65 | 22 | 4 | 0 | proposed |
| Fraktale | fractals | 0.79 | 24 | 2 | 1 | proposed |
| Gleichung | formula | 0.53 | 25 | 1 | 0 | proposed |
| Heldinnenreise | heroine's journey | 0.71 | 25 | 1 | 1 | proposed |
| Kaels Trauma | Internal State | 0.65 | 23 | 3 | 1 | stated in 1 doc(s) ^[dramatica-storyform-kohaerenz-protokoll-analyse.md:L92] |
| Kern-Welten | Realitätstypen | 0.52 | 25 | 1 | 1 | stated in 1 doc(s) ^[guardians-und-kern-welten-konzept.md:L15] |
| Maxwellscher | Maxwell's | 0.76 | 12 | 14 | 3 | proposed |
| parakonsistent | PARACONSISTENT | 0.55 | 20 | 6 | 0 | proposed |
| Psychologisches Hacking | Relationship Story | 0.64 | 2 | 24 | 2 | stated in 1 doc(s) ^[storyforms-system-mind-bewusstsein.md:L93] |
| Ist die Boundary-Theorie | CFT | 0.51 | 0 | 25 | 0 | stated in 2 doc(s) ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L148] ^[holographisches-prinzip-fuer-kohaerenz-protokoll-2.md:L148] |
| Coheronen | Coherons | 0.62 | 3 | 22 | 0 | proposed |
| Endlosschleifen | Nicht-terminierende Algorithmen | 0.65 | 24 | 1 | 1 | stated in 1 doc(s) ^[genesis-finale-prosa-angepasste-ich-natur.md:L119] |
| Rückkopplungen | Feedback Loops | 0.68 | 9 | 16 | 5 | stated in 1 doc(s) ^[kohaerenz-protokoll-thematische-tiefenanalyse.md:L178]; proposed |
| Gesamtnetzwerk | Mutual Information | 0.76 | 2 | 23 | 1 | stated in 1 doc(s) ^[ontologische-inversion-von-aegis-kritisches-framework.md:L102] |
| Gruppentheorie | GroupTheory | 0.77 | 21 | 4 | 3 | proposed |
| Halt | Halting | 0.53 | 11 | 14 | 0 | proposed |
| Held | hero | 0.55 | 17 | 8 | 0 | proposed |
| Ungerechtigkeit | Inequity | 0.76 | 11 | 14 | 0 | proposed |
| Ladung | load | 0.56 | 13 | 12 | 0 | proposed |
| McL | Soziale Netzwerke | 0.51 | 22 | 3 | 1 | stated in 1 doc(s) ^[kernwelten-fuer-kohaerenz-protokoll.md:L303] |
| falsch ausgerichtet | Misaligned | 0.65 | 1 | 24 | 0 | proposed |
| Verstärkt | Augmented | 0.51 | 13 | 11 | 0 | proposed |
| Wächters | Guardian's | 0.70 | 14 | 10 | 0 | proposed |
| Möglichkeits-Garten | In KW4 | 0.36 | 22 | 2 | 2 | stated in 2 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung-2.md:L265] ^[roman-lokalitaeten-konzept-und-ausarbeitung-3.md:L266] |
| integrierte Informationstheorie | Integrated Information Theory | 0.79 | 1 | 23 | 0 | proposed |
| Managern | Managers | 0.57 | 7 | 17 | 5 | proposed |
| Neuheit | Salienz | 0.72 | 21 | 3 | 1 | stated in 1 doc(s) ^[heilung-hirnchemie-kunst-trauma.md:L140] |
| Resonanz-Landschaft | Resonance-Landscape | 0.73 | 23 | 1 | 1 | stated in 1 doc(s) ^[pitch-deck-coherence-protocol.md:L72]; proposed |
| Schranke | barrier | 0.65 | 18 | 6 | 0 | proposed |
| Unbekanntes | unknown | 0.74 | 16 | 8 | 0 | proposed |
| Verlassen | Abandonment | 0.76 | 15 | 8 | 0 | proposed |
| Anscheinend Normaler Persönlichkeitsanteil | Primärer ANP | 0.76 | 8 | 15 | 3 | stated in 3 doc(s) ^[forschungsauftrag-spannungspunktanalyse-und-charakterausarbe.md:L25] ^[strukturelle-dissoziation-system-kael-analyse.md:L248] |
| Architekten | architects | 0.69 | 21 | 2 | 0 | proposed |
| Haltung der Anomalien | Attitude | 0.63 | 1 | 22 | 1 | stated in 1 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L312] |
| Katalysatorin | Catalyst | 0.47 | 5 | 18 | 0 | proposed |
| beschädigt | Corrupted | 0.60 | 18 | 5 | 0 | proposed |
| EP-Funktionen | Unbewusste | 0.48 | 2 | 21 | 1 | stated in 1 doc(s) ^[weltenkonzept-fuer-kohaerenz-protokoll-tsdp-basiert.md:L43] |
| Vorhaben | Intent | 0.54 | 4 | 19 | 0 | proposed |
| Konvergenz | Top-down | 0.63 | 19 | 4 | 1 | stated in 1 doc(s) ^[narrative-context-protocol-ncp-spezifikation.md:L183] |
| Zirkularität | Regress | 0.65 | 10 | 13 | 1 | stated in 1 doc(s) ^[monstergruppen-und-paradoxien-im-narrativ.md:L85] |
| Schalter | Switch | 0.66 | 7 | 16 | 1 | proposed |
| Speicher | Storage | 0.50 | 22 | 1 | 1 | proposed |
| Zufälligkeit | chance | 0.62 | 20 | 3 | 0 | proposed |
| Akt des Lesens | act of reading | 0.72 | 12 | 10 | 1 | proposed |
| Klassische | Classic | 0.53 | 19 | 3 | 0 | proposed |
| Ereignishorizont | Schwarze Löcher der Information | 0.32 | 20 | 2 | 2 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-protokoll.md:L176] |
| Faden | Thread | 0.67 | 20 | 2 | 0 | proposed |
| Lochs | Holes | 0.45 | 10 | 12 | 3 | proposed |
| Persönlichkeitsanteil | Jeder Alter | 0.53 | 18 | 4 | 3 | stated in 1 doc(s) ^[projektplanung-fuer-kohaerenz-protokoll.md:L103] |
| Neuausrichtung | Realignment | 0.58 | 16 | 6 | 0 | proposed |
| Partnerin | partner | 0.72 | 15 | 7 | 2 | proposed |
| Protektoren | protectors | 0.79 | 12 | 10 | 0 | proposed |
| Rein | Pure | 0.68 | 14 | 8 | 0 | proposed |
| top-down | Top-down | 0.55 | 18 | 4 | 1 | proposed |
| Wachsende | increasing | 0.59 | 9 | 13 | 0 | proposed |
| AEGIS Paradoxon | AI Alignment | 0.38 | 4 | 17 | 3 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptentwicklung.md:L32] |
| AdS | Bulk | 0.42 | 8 | 13 | 6 | stated in 2 doc(s) ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L79] ^[holographisches-prinzip-fuer-kohaerenz-protokoll-2.md:L79] |
| Gewahrsein | Awareness | 0.73 | 5 | 16 | 1 | proposed |
| Pflegende | Caregiver | 0.59 | 1 | 20 | 0 | proposed |
| Dialetheie | Dialetheia | 0.59 | 3 | 18 | 0 | proposed |
| Kanäle | EICs | 0.43 | 18 | 3 | 3 | stated in 1 doc(s) ^[digitale-uberwelt.md:L49] |
| Ereignishorizont | event horizon | 0.56 | 20 | 1 | 0 | proposed |
| Falschinformation | Lüge | 0.72 | 1 | 20 | 1 | stated in 1 doc(s) ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L200] |
| Widerlegung | Falsification | 0.63 | 13 | 8 | 0 | proposed |
| K1 und K0 | Kernels | 0.27 | 3 | 18 | 1 | stated in 1 doc(s) ^[ki-prompt-analyse-hard-problem-of-consciousness.md:L305] |
| Modulen | modules | 0.77 | 9 | 12 | 2 | proposed |
| Netzwerktheorie | Network theory | 0.70 | 19 | 2 | 2 | proposed |
| RIVE | Validation Engine | 0.55 | 14 | 7 | 7 | stated in 2 doc(s) ^[kohaerenz-protokoll-duale-dramatica-storyform-synthese.md:L65] ^[aegis.md:L103] |
| Sekundärer | Secondary | 0.64 | 11 | 10 | 0 | proposed |
| Temporal | Stutter | 0.36 | 19 | 2 | 2 | stated in 2 doc(s) ^[charakter-kompilation-fuer-kohaerenz-protokoll.md:L187] ^[project-status-report-kohaerenz-protokoll-canonical-state-st.md:L70] |
| Antinomien | Logische Paradoxien | 0.69 | 4 | 16 | 1 | stated in 1 doc(s) ^[monstergruppen-und-paradoxien-im-narrativ.md:L92] |
| Auflösen | Resolve | 0.71 | 1 | 19 | 0 | proposed |
| Beobachtereffekt | Observer Effect | 0.78 | 17 | 3 | 2 | proposed |
| Bestand | Inventory | 0.64 | 11 | 9 | 1 | proposed |
| Deterministisches Chaos | Schmetterlingseffekt | 0.41 | 1 | 19 | 1 | stated in 1 doc(s) ^[paradoxien-der-kohaerenz-protokoll-entwicklung.md:L38] |
| Dopamin | Drive | 0.43 | 6 | 14 | 2 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L162] |
| ENDE | End | 0.68 | 7 | 13 | 0 | proposed |
| existenzielle Krise | Existential Crisis | 0.78 | 13 | 7 | 2 | proposed |
| Rückkopplungen | Feedback-Loops | 0.72 | 9 | 11 | 5 | proposed |
| Gastgeber | Hosts | 0.54 | 2 | 18 | 1 | proposed |
| Hüter | guardian | 0.59 | 15 | 5 | 0 | proposed |
| Kurzgeschichten | Slots | 0.76 | 10 | 10 | 5 | stated in 1 doc(s) ^[kohaerenz-protokoll-synthese-integration.md:L149] |
| Landauer-Prinzips | Landauer's Principle | 0.73 | 8 | 12 | 0 | proposed |
| Status Quo | Logic of the City | 0.73 | 19 | 1 | 1 | stated in 1 doc(s) ^[refining-dramatica-storyform-for-kohaerenz-protokoll.md:L160] |
| Nichtsein | non-being | 0.59 | 11 | 9 | 0 | proposed |
| Werteausrichtung | Value Alignment | 0.66 | 1 | 19 | 1 | stated in 1 doc(s) ^[aegis-seele-und-entropie.md:L218] |
| Arbeitsbereich | Workspace | 0.73 | 7 | 12 | 4 | proposed |
| Blueshift | Fast | 0.52 | 1 | 18 | 1 | stated in 1 doc(s) ^[gravitational-architecture-novel-structure.md:L354] |
| Boundary-Zustände | Regionen | 0.43 | 2 | 17 | 2 | stated in 2 doc(s) ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L150] ^[holographisches-prinzip-fuer-kohaerenz-protokoll-2.md:L150] |
| Komplexe PTBS | Complex PTSD | 0.73 | 8 | 11 | 3 | proposed |
| Feldtheorien | field theory | 0.51 | 13 | 6 | 2 | proposed |
| freie Energie | Free Energy | 0.70 | 6 | 13 | 3 | proposed |
| Gastgeber-Identitäten | Hosts | 0.76 | 1 | 18 | 1 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L181] |
| Hebel | Titration | 0.78 | 7 | 12 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-dramatica-synthese-masterkonzept.md:L192] |
| Leerheit | emptiness | 0.71 | 7 | 12 | 0 | proposed |
| Multi-Perspektivität | Polyphonie | 0.74 | 1 | 18 | 1 | stated in 1 doc(s) ^[projektplanung-fuer-kohaerenz-protokoll.md:L105] |
| Programms | program | 0.54 | 8 | 11 | 0 | proposed |
| KI-Ausrichtung | AI Alignment | 0.79 | 1 | 17 | 1 | proposed |
| Problem der KI-Ausrichtung | AI Alignment | 0.55 | 1 | 17 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptentwicklung.md:L12] |
| konform | Conformal | 0.77 | 13 | 5 | 0 | proposed |
| Unentscheidbarkeit | Epistemologischer Schock | 0.46 | 16 | 2 | 2 | stated in 2 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L385] ^[ki-rolle-aegis-genesis-fragestellungen.md:L362] |
| Regelungstechnik | Feedback Loops | 0.63 | 2 | 16 | 2 | stated in 1 doc(s) ^[aegis-subplots-kapitelweise-system-exploration-docx.md:L222] |
| Heldin | Heroine | 0.60 | 1 | 17 | 0 | proposed |
| Informationsmuster | information pattern | 0.60 | 16 | 2 | 0 | proposed |
| Jungianische | Jungian | 0.48 | 5 | 13 | 5 | proposed |
| Karten | Maps | 0.74 | 13 | 5 | 2 | proposed |
| Konnektive | Verknüpfungen | 0.63 | 2 | 16 | 1 | stated in 1 doc(s) ^[parakonsistente-logik-fuer-kohaerenz-protokoll.md:L56] |
| Nichts-Rauschen | K₁-Reinform | 0.59 | 16 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L73] |
| Selbstprüfung | RCV | 0.45 | 6 | 12 | 4 | stated in 1 doc(s) ^[aegis-philosophische-und-systemtheoretische-analyse-docx.md:L184] |
| Reversibel | Reversible | 0.63 | 3 | 15 | 0 | proposed |
| Unentscheidbarkeit | UNDECIDABLE | 0.58 | 16 | 2 | 0 | proposed |
| Vakuums | vacuum | 0.68 | 5 | 13 | 1 | proposed |
| Anscheinend Normaler Teil | Primärer ANP | 0.76 | 2 | 15 | 1 | stated in 1 doc(s) ^[charaktere.md:L267] |
| Architektin | architect | 0.72 | 3 | 14 | 0 | proposed |
| Auflösungen | Deus Ex Machina | 0.63 | 6 | 11 | 2 | stated in 1 doc(s) ^[plotentwicklung-schluessigkeit-kohaerenz-konsistenz.md:L214] |
| Bewertung der Funktionstüchtigkeit | BPoF | 0.63 | 1 | 16 | 1 | stated in 1 doc(s) ^[aegis-philosophie-und-systemtheorie.md:L160] |
| Basisrealität | Fundamental reality | 0.59 | 16 | 1 | 0 | proposed |
| Basisrealität | fundamental reality | 0.54 | 16 | 1 | 0 | proposed |
| Konstrukts | Constructs | 0.50 | 11 | 6 | 0 | proposed |
| Episteme | Logic and Analysis | 0.57 | 16 | 1 | 1 | stated in 1 doc(s) ^[an-introduction-to-the-world-of-kohaerenz-protokoll.md:L89] |
| Fehlausrichtung | misalignment | 0.74 | 13 | 4 | 0 | proposed |
| Geister | ghosts | 0.65 | 14 | 3 | 0 | proposed |
| Gelb | golden | 0.49 | 11 | 6 | 1 | proposed |
| Hüter | Informant | 0.41 | 15 | 2 | 2 | stated in 1 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L336] |
| Informationstheoretische Interpretation | Shannon-Entropie | 0.49 | 1 | 16 | 1 | stated in 1 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L48] |
| Knotenpunkte | vertices | 0.55 | 15 | 2 | 0 | proposed |
| Kurve | Titration | 0.68 | 5 | 12 | 2 | stated in 1 doc(s) ^[projektanalyse-kohaerenz-protokoll-dis.md:L198] |
| Lebensgeschichte | biography | 0.65 | 13 | 4 | 0 | proposed |
| Leerstellen | Reader-as-Substrate | 0.75 | 11 | 6 | 4 | stated in 1 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L657] |
| Parakonsistent | PARACONSISTENT | 0.58 | 11 | 6 | 0 | proposed |
| Verfolger | Persecutors | 0.67 | 13 | 4 | 3 | proposed |
| Primärdirektive | primary directive | 0.76 | 5 | 12 | 0 | proposed |
| Winter | Satire | 0.69 | 16 | 1 | 1 | stated in 1 doc(s) ^[narrative-physik-attraktoren-leserbewusstsein.md:L189] |
| Sphäre | Sphere | 0.67 | 13 | 4 | 0 | proposed |
| Unheimlichen Tals | Uncanny Valley | 0.73 | 1 | 16 | 1 | stated in 1 doc(s) ^[aegis-logik-und-narrative-implikationen.md:L126] |
| Unzuverlässige Erzählung | Unreliable Narrator | 0.72 | 3 | 14 | 2 | proposed |
| Werkstatt | Workshop | 0.66 | 6 | 11 | 0 | proposed |
| Zeugen | Witnessing | 0.74 | 13 | 4 | 1 | proposed |
| Amygdala | Angstzentrum | 0.51 | 14 | 2 | 2 | stated in 1 doc(s) ^[strukturelle-dissoziation-system-kael-analyse.md:L102] |
| Archivar | archivist | 0.63 | 14 | 2 | 1 | proposed |
| Bestand | inventory | 0.74 | 11 | 5 | 1 | proposed |
| Betreuer | Caretaker | 0.56 | 3 | 13 | 0 | proposed |
| Four Domains | Classes | 0.64 | 1 | 15 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L40] |
| Pivot | Dialetheic Choice | 0.53 | 10 | 6 | 5 | stated in 5 doc(s) ^[companion-guide-to-the-coherence-protocol-understanding-love.md:L105] ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L596] |
| UMWELT | Environment | 0.78 | 1 | 15 | 0 | proposed |
| Falsifikation | Falsification | 0.53 | 8 | 8 | 5 | proposed |
| Feedback-Schleifen | Feedback-Loops | 0.73 | 5 | 11 | 1 | proposed |
| Gebiete | Fields | 0.61 | 4 | 12 | 0 | proposed |
| Interne Politik | Firefighter | 0.45 | 1 | 15 | 1 | stated in 1 doc(s) ^[fragen-zu-existenz-agency-und-realitaet.md:L192] |
| Inciting Incident | Flicker | 0.38 | 6 | 10 | 1 | stated in 1 doc(s) ^[refining-dramatica-storyform-for-kohaerenz-protokoll.md:L168] |
| Geister | Ghosts | 0.57 | 14 | 2 | 0 | proposed |
| Goldene | Golden | 0.59 | 1 | 15 | 0 | proposed |
| Unendlichkeit | Infinity | 0.79 | 14 | 2 | 2 | proposed |
| Iser | Reader-as-Substrate | 0.50 | 10 | 6 | 6 | stated in 2 doc(s) ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L1074] ^[systemic-architecture-specification-the-coherence-protocol-w.md:L88] |
| Klein | Little | 0.76 | 12 | 4 | 0 | proposed |
| Quad | Throughline Configurations | 0.28 | 15 | 1 | 1 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse-2.md:L503] |
| Zustandsvalidierung | RIVE | 0.64 | 2 | 14 | 1 | stated in 1 doc(s) ^[p-vs-np-und-kohaerenz.md:L211] |
| Samen | Seeds | 0.65 | 13 | 3 | 1 | proposed |
| Storyforming-Lock-In | Storyform B | 0.58 | 1 | 15 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L353] |
| We-Perspektive | Subjective Story | 0.56 | 1 | 15 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L78] |
| We-Throughline | Subjective Story | 0.49 | 1 | 15 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L185] ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L315] |
| zwischen den Zeilen | Subtext | 0.62 | 1 | 15 | 0 | proposed |
| Territorium | territory | 0.70 | 12 | 4 | 0 | proposed |
| unzuverlässige Erzählung | Unreliable Narrator | 0.67 | 2 | 14 | 1 | proposed |
| Unwissenheit | ignorance | 0.77 | 11 | 5 | 0 | proposed |
| Verzerrung der Zeitwahrnehmung | Zeitdilatation | 0.75 | 1 | 15 | 1 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L32] |
| Verteidiger | Advocate | 0.61 | 14 | 1 | 0 | proposed |
| Amygdala | Emotionszentrum | 0.57 | 14 | 1 | 1 | stated in 1 doc(s) ^[ontologie-des-gelesenen-traumas.md:L126] |
| Fläche | Area | 0.61 | 8 | 7 | 0 | proposed |
| Wert B | Both | 0.56 | 2 | 13 | 2 | stated in 1 doc(s) ^[parakonsistente-logik-im-seelen-protokoll.md:L73] ^[parakonsistente-logik-im-seelen-protokoll.md:L111] |
| Konstruktive | Constructive | 0.78 | 7 | 8 | 1 | proposed |
| Kerntrauma | Core Trauma | 0.77 | 13 | 2 | 1 | proposed |
| Sinnloses Tun | Doing | 0.51 | 1 | 14 | 1 | stated in 1 doc(s) ^[narrative-context-protocol-ncp-spezifikation.md:L61] |
| Dualismus | Dualism | 0.76 | 13 | 2 | 1 | proposed |
| Dualismus | dualism | 0.69 | 13 | 2 | 0 | proposed |
| Leerheit | Emptiness | 0.71 | 7 | 8 | 4 | proposed |
| Endsaldo | Story Outcome | 0.78 | 1 | 14 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L100] |
| Existenzielle Angst | existential dread | 0.75 | 8 | 7 | 0 | proposed |
| Große Mauer | Systemgrenze | 0.57 | 1 | 14 | 1 | stated in 1 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L208] ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L358] |
| Kartographie | Maps | 0.75 | 10 | 5 | 1 | proposed |
| Limit B | Timelock | 0.63 | 2 | 13 | 2 | stated in 2 doc(s) ^[dramatica-storyform-synthese-aegis-analyse.md:L93] ^[dramatica-storyform-synthese-aegis-analyse-2.md:L267] |
| Misstrauens | distrust | 0.65 | 13 | 2 | 0 | proposed |
| Ontologien | ONTOLOGY | 0.57 | 10 | 5 | 0 | proposed |
| Schemata | schemas | 0.52 | 13 | 2 | 0 | proposed |
| Standhaftigkeit | Steadfast | 0.67 | 1 | 14 | 1 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-verortung.md:L123] |
| Wahrheitswertlücken | Unbestimmtheit | 0.62 | 1 | 14 | 1 | stated in 1 doc(s) ^[parakonsistente-logik-im-seelen-protokoll.md:L154] |
| Vorhersagefehler | Überraschung | 0.76 | 4 | 11 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptionelle-ausarbeitung.md:L141] |
| Zimmer | chamber | 0.65 | 13 | 2 | 0 | proposed |
| Überall | everywhere | 0.73 | 12 | 3 | 0 | proposed |
| Tier | Animal | 0.67 | 11 | 3 | 0 | proposed |
| Atomizität | Unteilbarkeit | 0.43 | 2 | 12 | 1 | stated in 1 doc(s) ^[primzahlen-als-metapher-in-kohaerenz-protokoll.md:L36] ^[primzahlen-als-metapher-in-kohaerenz-protokoll.md:L85] |
| Erweitert | Augmented | 0.71 | 3 | 11 | 0 | proposed |
| Automorphismengruppe | Gruppe der Symmetrien | 0.63 | 13 | 1 | 1 | stated in 1 doc(s) ^[monstergruppe-babygruppe-und-kael.md:L97] |
| Bewusstseinsinstanzen | Personas | 0.77 | 1 | 13 | 1 | stated in 1 doc(s) ^[guardians-und-kern-welten-konzept.md:L74] |
| Regress | Circularity | 0.62 | 13 | 1 | 1 | stated in 1 doc(s) ^[monstergruppen-und-paradoxien-im-narrativ.md:L85] |
| Konstrukten | Constructs | 0.53 | 8 | 6 | 0 | proposed |
| Statistische Manual Psychischer Störungen | DSM-5 | 0.54 | 2 | 12 | 2 | stated in 1 doc(s) ^[dis-diagnose-klinische-ethische-rechtliche-analyse.md:L54] |
| EP-Mix | Metakognitiver Anteil | 0.59 | 11 | 3 | 3 | stated in 1 doc(s) ^[uberarbeitete-liste-der-anteile-von-kael-tsdp-basiert.md:L157] |
| exklusiv | Exclusionary | 0.72 | 9 | 5 | 0 | proposed |
| Exekutive | PFC Online | 0.57 | 13 | 1 | 1 | stated in 1 doc(s) ^[heilung-hirnchemie-kunst-trauma.md:L192] |
| Friedens | of peace | 0.77 | 11 | 3 | 0 | proposed |
| Insider-Archetyp | Mentor | 0.47 | 3 | 11 | 3 | stated in 3 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik.md:L325] ^[kael-charakterarchitektur-und-konfliktdynamik-2.md:L325] |
| Kernwelt B | Location | 0.53 | 4 | 10 | 2 | stated in 1 doc(s) ^[codex-optimierung-fuer-kohaerenz-protokoll.md:L450] |
| Konstruktive | constructive | 0.78 | 7 | 7 | 1 | proposed |
| Kämpfer | fighter | 0.76 | 11 | 3 | 1 | proposed |
| Misstrauens | Suspicion | 0.76 | 13 | 1 | 0 | proposed |
| nonlinear | Nonlinear | 0.40 | 6 | 8 | 4 | proposed |
| Verfolger | Persecutor Parts | 0.69 | 13 | 1 | 1 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L113] |
| Phase II | Photon Sphere | 0.60 | 10 | 4 | 3 | stated in 1 doc(s) ^[projektanalyse-kohaerenz-protokoll-dis.md:L59] |
| Rekursive Selbstverifikation | RCV | 0.64 | 2 | 12 | 2 | stated in 1 doc(s) ^[aegis.md:L176] |
| Regelwerk | rule set | 0.57 | 12 | 2 | 0 | proposed |
| Relativität | Relativity | 0.70 | 8 | 6 | 0 | proposed |
| Signposts | Storybeats | 0.61 | 8 | 6 | 4 | stated in 1 doc(s) ^[dramatica-agentic-storyform-interactive-novel.md:L254] |
| unentscheidbar | UNDECIDABLE | 0.79 | 12 | 2 | 2 | proposed |
| Unterbewusstsein | subconscious | 0.78 | 10 | 4 | 0 | proposed |
| Verbannte | exiled | 0.67 | 2 | 12 | 0 | proposed |
| Verwalter | Administrator | 0.79 | 7 | 6 | 0 | proposed |
| Avatare | Avatars | 0.53 | 11 | 2 | 1 | proposed |
| Avatare | avatars | 0.71 | 11 | 2 | 0 | proposed |
| Komplexe Posttraumatische Belastungsstörung | C-PTSD | 0.71 | 6 | 7 | 0 | proposed |
| Klassisch | Classic | 0.51 | 10 | 3 | 0 | proposed |
| Kern-Trauma | Core Trauma | 0.72 | 11 | 2 | 1 | proposed |
| korrupt | Corrupted | 0.51 | 8 | 5 | 0 | proposed |
| Richtlinie | DIRECTIVE | 0.76 | 7 | 6 | 0 | proposed |
| Energy Discharge | Unburdening | 0.78 | 1 | 12 | 1 | stated in 1 doc(s) ^[reality-s-isomorphic-architecture-explained.md:L403] |
| Erster Kontakt | initial contact | 0.67 | 12 | 1 | 0 | proposed |
| Fragil | Fragile | 0.53 | 3 | 10 | 0 | proposed |
| Hüterin | guardian | 0.75 | 8 | 5 | 0 | proposed |
| Ursprungstrauma | K₀-Druck | 0.71 | 9 | 4 | 1 | stated in 1 doc(s) ^[dkt-fundament-kohaerenz-protokoll-md.md:L116] |
| Manager und Firefighters | Protectors | 0.49 | 1 | 12 | 1 | stated in 1 doc(s) ^[m-als-fundament-der-simulation.md:L82] |
| Maske | Mask | 0.62 | 11 | 2 | 1 | proposed |
| Männlichen | male | 0.74 | 7 | 6 | 0 | proposed |
| RAUSCHEN | NULL-STATE | 0.70 | 11 | 2 | 2 | stated in 2 doc(s) ^[genesis-aegis-und-logische-grenzen.md:L119] ^[genesis-aegis-und-logische-grenzen-2.md:L207] |
| nichtlinear | Nonlinear | 0.79 | 5 | 8 | 2 | proposed |
| Phaenomena | Phenomena | 0.59 | 7 | 6 | 0 | proposed |
| Schützer | Protectors | 0.62 | 1 | 12 | 0 | proposed |
| Radikal | Radical | 0.77 | 6 | 7 | 0 | proposed |
| Seelen | Souls | 0.74 | 11 | 2 | 0 | proposed |
| Teilung | Split | 0.63 | 3 | 10 | 0 | proposed |
| Vagheit | Vagueness | 0.76 | 11 | 2 | 1 | proposed |
| Vorläufer | precursor | 0.73 | 12 | 1 | 0 | proposed |
| Wacht | guard | 0.65 | 8 | 5 | 0 | proposed |
| Absurde | Absurd | 0.74 | 8 | 4 | 1 | proposed |
| Nicht-Dualität | Advaita Vedanta | 0.43 | 6 | 6 | 4 | stated in 1 doc(s) ^[aegis-seele-und-entropie.md:L17] |
| Algorithmische Komplexität | Kolmogorov | 0.38 | 2 | 10 | 2 | stated in 1 doc(s) ^[aegis-genesis-krise-prosa-auftrag-2.md:L351] ^[aegis-genesis-krise-prosa-auftrag-2.md:L470] |
| Zerbrochene | Broken | 0.50 | 5 | 7 | 0 | proposed |
| Chinesisches | Chinese | 0.49 | 7 | 5 | 2 | proposed |
| Konstruktstadt | Construct City | 0.68 | 1 | 11 | 0 | proposed |
| diskursive Logik | Discursive Logic | 0.71 | 1 | 11 | 0 | proposed |
| Durchsetzer | Enforcer | 0.70 | 1 | 11 | 0 | proposed |
| Einfache Gruppe | simple groups | 0.79 | 3 | 9 | 2 | proposed |
| Vollstrecker | Executor | 0.59 | 10 | 2 | 0 | proposed |
| Tore | Gates | 0.70 | 8 | 4 | 0 | proposed |
| Gerechtigkeit | Justice | 0.75 | 5 | 7 | 0 | proposed |
| Herbst | fall | 0.64 | 1 | 11 | 0 | proposed |
| Informationsphysik | physics of information | 0.79 | 11 | 1 | 0 | proposed |
| KI-gesteuerte Charaktere | NPCs | 0.69 | 1 | 11 | 1 | stated in 1 doc(s) ^[narrative-modelle-und-dramatica-erweiterung.md:L353] |
| Landauer-Wärme | Landauer Heat | 0.78 | 7 | 5 | 0 | proposed |
| Mentor | Mentor Figure | 0.77 | 11 | 1 | 1 | proposed |
| Meta-Kognitiv | Metacognitive | 0.55 | 7 | 5 | 0 | proposed |
| Metakognition | Meta-cognition | 0.70 | 11 | 1 | 0 | proposed |
| Metakognition | meta-cognition | 0.77 | 11 | 1 | 1 | proposed |
| Nicht-Lokalität | Prinzip der Quantenverschränkung | 0.43 | 11 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-synthese-integration.md:L198] |
| Sonder | Special | 0.60 | 5 | 7 | 0 | proposed |
| einheitlich | Unitary | 0.79 | 6 | 6 | 0 | proposed |
| Adrenalin-Flut | Hyperarousal | 0.62 | 1 | 10 | 1 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L78] |
| Allem | TOE | 0.79 | 9 | 2 | 2 | stated in 1 doc(s) ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L114] |
| Künstlichen Intelligenz | Artificial intelligence | 0.68 | 7 | 4 | 0 | proposed |
| Baby-Monstergruppe | Baby_monster_group | 0.70 | 5 | 6 | 2 | proposed |
| EP-Intrusion | EP intrusion | 0.71 | 9 | 2 | 0 | proposed |
| Einklammerung der Welturteile | Epoché | 0.67 | 1 | 10 | 1 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse-2.md:L315] |
| Einstein-Rosen-Brücke | Wurmloch | 0.62 | 5 | 6 | 4 | stated in 1 doc(s) ^[untersuche-in-wie-fern-juna-bzw-das-fundament-du.md:L60] ^[untersuche-in-wie-fern-juna-bzw-das-fundament-du.md:L94] |
| Verspielte | Flicker | 0.76 | 1 | 10 | 1 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L341] |
| Zerbrechlich | Fragile | 0.50 | 1 | 10 | 0 | proposed |
| Wachsende | Growing | 0.67 | 9 | 2 | 0 | proposed |
| Hafen | harbor | 0.71 | 8 | 3 | 0 | proposed |
| Zuständen des Sympathikus | Hyperarousal | 0.54 | 1 | 10 | 1 | stated in 1 doc(s) ^[kohaerenz-prozess.md:L133] |
| Konstatierungen | observations | 0.76 | 5 | 6 | 0 | proposed |
| Logiken der Formalen Inkonsistenz | LFIs | 0.59 | 4 | 7 | 2 | stated in 1 doc(s) ^[parakonsistenz-aegis-und-nicht-existenz.md:L123] ^[parakonsistenz-aegis-und-nicht-existenz.md:L337] |
| Logikfehler | logical error | 0.78 | 10 | 1 | 0 | proposed |
| Problem des MC | MC Problem | 0.69 | 1 | 10 | 1 | proposed |
| Meta-Kognitiv | meta-cognitive | 0.56 | 7 | 4 | 2 | proposed |
| Ursprungstrauma | OQ-03 | 0.48 | 9 | 2 | 2 | stated in 1 doc(s) ^[dkt-fundament-kohaerenz-protokoll-md.md:L224] |
| Odyssee | Odyssey | 0.70 | 6 | 5 | 0 | proposed |
| Paria | Pariah | 0.56 | 6 | 5 | 1 | proposed |
| Verweigerung | Refusal | 0.61 | 5 | 6 | 0 | proposed |
| Reste | residues | 0.67 | 10 | 1 | 0 | proposed |
| Revolte | rebellion | 0.70 | 4 | 7 | 0 | proposed |
| Schleusen | gates | 0.67 | 7 | 4 | 0 | proposed |
| Schutzraum | refuge | 0.75 | 10 | 1 | 0 | proposed |
| Sonder | special | 0.65 | 5 | 6 | 0 | proposed |
| Zettel | note | 0.79 | 2 | 9 | 0 | proposed |
| Bindungsruf-System | Attachment Cry | 0.52 | 1 | 9 | 1 | stated in 1 doc(s) ^[tsdp-analyse-kaels-innere-welt.md:L59] |
| Schmerzes und des Bindungsbedürfnisses | Attachment Cry | 0.58 | 1 | 9 | 1 | stated in 1 doc(s) ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:L124] |
| Gleichzeitigkeit | Concurrency | 0.61 | 8 | 2 | 0 | proposed |
| Gegenspieler | Contagonist | 0.61 | 3 | 7 | 1 | proposed |
| Korrespondenzwahrheit | Correspondence Truth | 0.61 | 4 | 6 | 0 | proposed |
| Offenlegung | Disclosure | 0.55 | 5 | 5 | 0 | proposed |
| Einstein-Rosen-Brücken | Wurmlöcher | 0.46 | 2 | 8 | 2 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L92] |
| Erasonen | Erasons | 0.54 | 7 | 3 | 0 | proposed |
| Äußere Ebene | External Level | 0.63 | 1 | 9 | 0 | proposed |
| Generationen | generations | 0.78 | 7 | 3 | 0 | proposed |
| Wacht | Guard | 0.53 | 8 | 2 | 0 | proposed |
| Gänge | Passages | 0.54 | 9 | 1 | 0 | proposed |
| Homogenität | homogeneity | 0.76 | 9 | 1 | 1 | proposed |
| Ikone | Ähnlichkeit | 0.42 | 1 | 9 | 1 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L115] |
| Kammer | chamber | 0.62 | 8 | 2 | 0 | proposed |
| Logikbombe | Trope | 0.63 | 1 | 9 | 1 | stated in 1 doc(s) ^[aegis-subplots-kapitelweise-system-exploration-docx.md:L300] |
| Modellieren | MODELING | 0.65 | 5 | 5 | 0 | proposed |
| Männlichen | Male | 0.67 | 7 | 3 | 1 | proposed |
| Mnemosyne-Archipelago | Resonance Landscape | 0.62 | 1 | 9 | 1 | stated in 1 doc(s) ^[systemic-architecture-specification-the-coherence-protocol-w.md:L64] |
| Ursprünglich | Primordial | 0.79 | 5 | 5 | 0 | proposed |
| Riese | giant | 0.67 | 6 | 4 | 0 | proposed |
| Roboter | Robot | 0.79 | 7 | 3 | 1 | proposed |
| Schwarm | swarm | 0.63 | 7 | 3 | 1 | proposed |
| Sonden | probes | 0.74 | 6 | 4 | 0 | proposed |
| Teilung | Splitting | 0.77 | 3 | 7 | 0 | proposed |
| Unterroutine | Subroutine | 0.69 | 1 | 9 | 0 | proposed |
| Zeitpfeils | arrow of time | 0.64 | 8 | 2 | 0 | proposed |
| Zero-Knowledge-Verifier | Zero-Knowledge Verifier | 0.68 | 2 | 8 | 0 | proposed |
| Zugriffsrechte | permissions | 0.54 | 5 | 5 | 0 | proposed |
| AEGIS-Avatar | NPC | 0.65 | 1 | 8 | 1 | stated in 1 doc(s) ^[orte-konzept-fuer-kohaerenz-protokoll.md:L291] ^[orte-konzept-fuer-kohaerenz-protokoll.md:L385] |
| Advaita Vedanta | Nondualism | 0.73 | 6 | 3 | 2 | stated in 1 doc(s) ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L481] |
| Anderer | Another | 0.63 | 4 | 5 | 0 | proposed |
| Anleihen | Bonds | 0.51 | 4 | 5 | 0 | proposed |
| Automat | Automaton | 0.72 | 3 | 6 | 0 | proposed |
| Banalität | Confirmation Bias | 0.61 | 1 | 8 | 1 | stated in 1 doc(s) ^[ki-prompt-analyse-hard-problem-of-consciousness.md:L407] |
| Bundesministerium | ministry | 0.50 | 7 | 2 | 0 | proposed |
| Komplexer Posttraumatischer Belastungsstörung | C-PTSD | 0.45 | 2 | 7 | 1 | stated in 1 doc(s) ^[trauma-archaeologie-interdisziplinaere-konzeptentwicklung-do.md:L107] |
| C-Systemen | LFIs | 0.63 | 2 | 7 | 2 | stated in 1 doc(s) ^[parakonsistente-logik-fuer-kohaerenz-protokoll.md:L103] ^[parakonsistente-logik-fuer-kohaerenz-protokoll.md:L111] |
| kaskadiert | Cascading | 0.66 | 3 | 6 | 0 | proposed |
| KOHÄRENT | Coherent | 0.75 | 1 | 8 | 0 | proposed |
| Kohärentismus | Coherentism | 0.79 | 8 | 1 | 0 | proposed |
| Kernel Panic | Compute-Lock | 0.73 | 5 | 4 | 3 | stated in 3 doc(s) ^[aegis-manifest-genesis-krise-reboot.md:L183] ^[aegis-manifest-genesis-krise-reboot-2.md:L240] |
| Konjektur | Conjecture | 0.68 | 3 | 6 | 2 | proposed |
| Logic of Trauma | Dialetheic Logic | 0.48 | 2 | 7 | 2 | stated in 2 doc(s) ^[concept-paper-the-architectural-foundations-of-kohaerenz-pro.md:L174] ^[the-sensory-rulebook-the-body-as-a-measuring-device-in-the-p.md:L103] |
| ER-Brücken | Wurmlöcher | 0.44 | 1 | 8 | 1 | stated in 1 doc(s) ^[hard-sf-roman-outline-dkt-physik-cosmic-horror.md:L31] |
| Fehlende Zeitliche Progression | Signposts | 0.54 | 1 | 8 | 1 | stated in 1 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L118] |
| Formalismus | Formalism | 0.62 | 5 | 4 | 1 | proposed |
| Hafen | Port | 0.59 | 8 | 1 | 0 | proposed |
| Metakognitiver | meta-cognitive | 0.66 | 5 | 4 | 0 | proposed |
| NP-schweres | NP-hard | 0.52 | 6 | 3 | 1 | proposed |
| Novelcrafter | Schreibsoftware | 0.76 | 6 | 3 | 3 | stated in 1 doc(s) ^[kohaerenz-protokoll-synthese-integration.md:L209] |
| Selbstprüfung | P5 | 0.67 | 6 | 3 | 1 | stated in 1 doc(s) ^[aegis-philosophie-und-manifest-entwicklung.md:L54] |
| Pragmatisch | Pragmatic | 0.75 | 4 | 5 | 0 | proposed |
| präfrontale | Prefrontal | 0.59 | 4 | 5 | 0 | proposed |
| Rhizom | rhizome | 0.64 | 5 | 4 | 4 | proposed |
| Schalter | switch | 0.68 | 7 | 2 | 0 | proposed |
| Signposts | Transits | 0.63 | 8 | 1 | 1 | stated in 1 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L193] |
| Systembewusstsein | System Mind | 0.63 | 2 | 7 | 0 | proposed |
| Verzeichnis | Catalog | 0.68 | 6 | 2 | 0 | proposed |
| Klassischer | Classic | 0.54 | 5 | 3 | 0 | proposed |
| Einheit des Wissens | Consilience | 0.73 | 1 | 7 | 0 | proposed |
| Kämpferin | Fighter | 0.45 | 1 | 7 | 0 | proposed |
| Form A | K₁-reading | 0.53 | 7 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-architecture-synthesis.md:L302] |
| Grenzwahrung | Ontologische Autarkie | 0.39 | 4 | 4 | 1 | stated in 1 doc(s) ^[aegis-analyse-und-manifest-postulation.md:L189] |
| Gödel-Satzes | Gödel's theorem | 0.36 | 7 | 1 | 0 | proposed |
| Gültig | Tautologie | 0.43 | 2 | 6 | 1 | stated in 1 doc(s) ^[parakonsistente-logik-fuer-kohaerenz-protokoll.md:L139] |
| Halbwertszeit | Half-Life | 0.68 | 1 | 7 | 0 | proposed |
| Hitzetod | heat death | 0.77 | 3 | 5 | 0 | proposed |
| Rumpf | Hull | 0.50 | 1 | 7 | 0 | proposed |
| Identitätstheorie | identity theory | 0.72 | 7 | 1 | 1 | proposed |
| Informationssystem | information system | 0.78 | 7 | 1 | 0 | proposed |
| MUH | Mathematische Struktur | 0.31 | 6 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-inkubation-x.md:L45] |
| Meta-Kognitiv | metacognitive | 0.74 | 7 | 1 | 0 | proposed |
| Naturgesetz | natural law | 0.79 | 6 | 2 | 0 | proposed |
| Pixelierung | Pixelation | 0.79 | 5 | 3 | 0 | proposed |
| Varietät | Reaktionsvielfalt | 0.33 | 6 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptionelle-ausarbeitung.md:L365] |
| Richter | judge | 0.65 | 6 | 2 | 0 | proposed |
| Zweiter Ordnung | Second-order | 0.70 | 1 | 7 | 0 | proposed |
| Stoff | Substance | 0.64 | 3 | 5 | 0 | proposed |
| Trauma-Halter | Trauma Holders | 0.69 | 5 | 3 | 0 | proposed |
| Trauma-Lokus | Vergessene Schrein | 0.50 | 4 | 4 | 2 | stated in 1 doc(s) ^[orte-konzept-fuer-kohaerenz-protokoll.md:L297] ^[orte-konzept-fuer-kohaerenz-protokoll.md:L389] |
| unitär | Unitary | 0.68 | 2 | 6 | 0 | proposed |
| Verwalter | administrator | 0.79 | 7 | 1 | 0 | proposed |
| Vestibulärer Mismatch | Übelkeit | 0.74 | 1 | 7 | 1 | stated in 1 doc(s) ^[gravitation-realitaet-simulation-wahrheit.md:L76] |
| Vorzeichen | sign | 0.53 | 6 | 2 | 0 | proposed |
| Agnotologie | Aktives Nicht-Wissen | 0.46 | 5 | 2 | 2 | stated in 2 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L388] ^[ki-rolle-aegis-genesis-fragestellungen.md:L364] |
| Aharonov-Lebowitz-Konstruktion | Page-Wootters | 0.49 | 1 | 6 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L31] |
| Helferin | Assistant | 0.70 | 6 | 1 | 0 | proposed |
| Austauschs | Landauer-Heat | 0.46 | 6 | 1 | 1 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-protokoll.md:L145] |
| Betriebssystems | of the operating system | 0.40 | 6 | 1 | 0 | proposed |
| Kommando | Command | 0.76 | 2 | 5 | 0 | proposed |
| Helfererschöpfung | Compassion Fatigue | 0.61 | 2 | 5 | 2 | stated in 1 doc(s) ^[juna-kael-system-krisenanalyse-und-rettungsplan.md:L41] |
| Konformen Feldtheorie | Conformal Field Theory | 0.74 | 4 | 3 | 0 | proposed |
| Wahl der Tiefen Ich-Perspektive | Deep POV | 0.45 | 1 | 6 | 1 | stated in 1 doc(s) ^[prosaversion-von-genesis-erstellen.md:L25] |
| Dramatica-Struktur | Dramatica Structure | 0.51 | 6 | 1 | 0 | proposed |
| Einbrechen des Realen | Systemischer Kollaps | 0.36 | 1 | 6 | 1 | stated in 1 doc(s) ^[gravitation-realitaet-simulation-wahrheit.md:L161] |
| Eingangsverarbeitung | Sensorium | 0.72 | 1 | 6 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptionelle-ausarbeitung.md:L384] |
| Energiedissipation | Wärmeabgabe | 0.40 | 4 | 3 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-thematische-tiefenanalyse.md:L195] |
| Fragebogen | Questionnaire | 0.78 | 5 | 2 | 1 | proposed |
| Goldene | golden | 0.64 | 1 | 6 | 1 | proposed |
| Hypothalamus-Hypophysen-Nebennierenrinden-Achse | HPA axis | 0.66 | 5 | 2 | 2 | proposed |
| Handlungssysteme | Janetian Action Systems | 0.70 | 4 | 3 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L63] |
| Hitzetod | Heat Death | 0.71 | 3 | 4 | 0 | proposed |
| Hitzeentwicklung | Landauer Heat | 0.57 | 2 | 5 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L27] |
| Richter | Judge | 0.71 | 6 | 1 | 0 | proposed |
| Wissensdatenbank | Knowledge Base | 0.77 | 4 | 3 | 0 | proposed |
| Kohärenz-Insel | M-Analogue | 0.47 | 6 | 1 | 1 | stated in 1 doc(s) ^[monstergruppe-kohaerenz-protokoll-fundament.md:L200] ^[monstergruppe-kohaerenz-protokoll-fundament.md:L204] |
| Konstatierungen | Observations | 0.74 | 5 | 2 | 0 | proposed |
| Mathematische Universum-Hypothese (MUH) | Mathematical Universe Hypothesis | 0.78 | 1 | 6 | 1 | proposed |
| Meta-Kognition | Meta-cognition | 0.65 | 6 | 1 | 0 | proposed |
| Männlich | male | 0.69 | 1 | 6 | 0 | proposed |
| OS-Domäne | OS Domain | 0.69 | 2 | 5 | 0 | proposed |
| Älteste | Oldest | 0.69 | 1 | 6 | 1 | proposed |
| älteste | Oldest | 0.38 | 1 | 6 | 0 | proposed |
| Organische Form | Rose | 0.59 | 1 | 6 | 1 | stated in 1 doc(s) ^[tattoo-konzept-symbolik-trauma-heilung.md:L140] |
| präfrontaler | Prefrontal | 0.60 | 2 | 5 | 0 | proposed |
| Prinzipal | principal | 0.77 | 2 | 5 | 2 | proposed |
| Realitätsprinzip | Über-Ich | 0.35 | 4 | 3 | 2 | stated in 1 doc(s) ^[narrative-physik-attraktoren-leserbewusstsein.md:L130] |
| Somatik | Somatics | 0.64 | 6 | 1 | 0 | proposed |
| Pfeil | Arrow | 0.70 | 1 | 5 | 0 | proposed |
| Verarbeitungseinheit | CPU | 0.68 | 2 | 4 | 1 | stated in 1 doc(s) ^[aegis-logik-in-der-leere-docx.md:L151] |
| Chinesisch | Chinese | 0.57 | 1 | 5 | 1 | proposed |
| Kohärenz-Kern | Coherence-Kernel | 0.69 | 5 | 1 | 0 | proposed |
| Komplexen Adaptiven Systemen | Complex Adaptive Systems | 0.64 | 2 | 4 | 1 | proposed |
| Konform | Conformal | 0.65 | 1 | 5 | 0 | proposed |
| Einklammerung | Enclosure | 0.56 | 5 | 1 | 0 | proposed |
| Wormhole | Einstein-Rosen Bridge | 0.75 | 4 | 2 | 1 | stated in 1 doc(s) ^[gravitational-architecture-novel-structure.md:L277] |
| Entwicklung der Beziehung | Internal Process | 0.79 | 3 | 3 | 1 | stated in 1 doc(s) ^[dramatica-storyform-kohaerenz-protokoll-analyse.md:L93] |
| Exekutive Steuerung | Prefrontal Cortex | 0.75 | 1 | 5 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L33] |
| Fragebogen | survey | 0.57 | 5 | 1 | 0 | proposed |
| Wärmetod des Antagonismus | Gleichgewichtszustand | 0.45 | 1 | 5 | 1 | stated in 1 doc(s) ^[ki-prompt-analyse-hard-problem-of-consciousness.md:L270] |
| Glitch-Ästhetik | Glitch-Art | 0.64 | 2 | 4 | 1 | proposed |
| Gravitation der Korrespondenz | Große Faktum | 0.50 | 2 | 4 | 1 | stated in 1 doc(s) ^[gravitation-realitaet-simulation-wahrheit-2.md:L54] |
| Haufen | Heap | 0.71 | 5 | 1 | 1 | proposed |
| Hegelsche | Hegelian | 0.78 | 4 | 2 | 1 | proposed |
| Inkubation | Incubation | 0.72 | 5 | 1 | 0 | proposed |
| Innere Bunker | Kernabwehr | 0.48 | 5 | 1 | 1 | stated in 1 doc(s) ^[orte-konzept-fuer-kohaerenz-protokoll.md:L309] ^[orte-konzept-fuer-kohaerenz-protokoll.md:L456] |
| Isolations-Problem | Märchen-Einwand | 0.56 | 3 | 3 | 2 | stated in 1 doc(s) ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L1358] |
| Koregulation | co-regulation | 0.61 | 5 | 1 | 0 | proposed |
| metakognitiv | Metacognitive | 0.54 | 1 | 5 | 0 | proposed |
| Muse-Lokus | Quelle der Inspiration | 0.41 | 1 | 5 | 1 | stated in 1 doc(s) ^[orte-konzept-fuer-kohaerenz-protokoll.md:L322] |
| P6 | Storyweaving | 0.42 | 3 | 3 | 2 | stated in 1 doc(s) ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L1243] |
| Platons | Plato's | 0.52 | 5 | 1 | 0 | proposed |
| Plurale Apotheose | Wir-AEGIS-plural | 0.33 | 3 | 3 | 3 | stated in 1 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L539] |
| Präfrontale | Prefrontal | 0.74 | 1 | 5 | 0 | proposed |
| Präfrontaler | Prefrontal | 0.56 | 1 | 5 | 0 | proposed |
| Rekursive Selbstverbesserung | Recursive self-improvement | 0.79 | 4 | 2 | 2 | proposed |
| Saiten | strings | 0.77 | 2 | 4 | 0 | proposed |
| Zufluchtsort | Sanctuary | 0.73 | 5 | 1 | 0 | proposed |
| Schwerelosigkeit | Zero-G | 0.75 | 5 | 1 | 1 | stated in 1 doc(s) ^[gravitation-realitaet-simulation-wahrheit.md:L93] |
| Stottern | Stutter | 0.55 | 4 | 2 | 0 | proposed |
| Syllogismus | Syllogism | 0.70 | 5 | 1 | 1 | proposed |
| Träger von Trauma | Trauma Holders | 0.79 | 3 | 3 | 0 | proposed |
| Unbeabsichtigte Folgen | unbeabsichtigte Folgen | 0.57 | 2 | 4 | 1 | proposed |
| Zeuge-Funktion | Witness function | 0.68 | 2 | 4 | 1 | proposed |
| Zufluchtsort | refuge | 0.76 | 5 | 1 | 1 | proposed |
| Analgesie | Schmerzunempfindlichkeit | 0.46 | 4 | 1 | 1 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L65] |
| Apophatik | Apophatic | 0.74 | 2 | 3 | 2 | proposed |
| Archivarin | Archivist | 0.78 | 3 | 2 | 0 | proposed |
| Automorphismen | Symmetriegruppen | 0.63 | 3 | 2 | 1 | stated in 1 doc(s) ^[m-als-fundament-der-simulation.md:L42] |
| Benefizienz | Prinzipien der Fürsorge | 0.40 | 4 | 1 | 1 | stated in 1 doc(s) ^[dis-berichtigung-umfassende-recherche-und-schreiben.md:L186] |
| Zentraleinheit | CPU | 0.74 | 1 | 4 | 0 | proposed |
| LFI-Kern | Central Processing Core | 0.38 | 3 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-architecture-synthesis.md:L187] ^[kohaerenz-protokoll-architecture-synthesis.md:L372] |
| Konformen Feldtheorie | Conformal field theory | 0.79 | 4 | 1 | 0 | proposed |
| Kontrollparadox | Control Paradox | 0.63 | 3 | 2 | 0 | proposed |
| Dionysisch | Dionysian | 0.64 | 2 | 3 | 1 | proposed |
| Emotionalen Teilen | Emotional parts | 0.63 | 4 | 1 | 0 | proposed |
| Emotionale Wahrheit | emotional truth | 0.79 | 3 | 2 | 0 | proposed |
| Entzug | Withdrawal | 0.71 | 3 | 2 | 1 | proposed |
| Motor der Erklärungs-Lücke | Explanatory Gap | 0.74 | 1 | 4 | 1 | stated in 1 doc(s) ^[ki-prompt-analyse-hard-problem-of-consciousness.md:L17] |
| Faktorgruppen | Quotientengruppen | 0.44 | 2 | 3 | 1 | stated in 1 doc(s) ^[monstergruppe-metapher-auf-mathematische-kohaerenz.md:L40] |
| Form B | K₀-reading | 0.71 | 4 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-architecture-synthesis.md:L302] |
| Garben-Theorie | Kategorientheorie | 0.50 | 1 | 4 | 1 | stated in 1 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L406] |
| Heisenbergsche Unschärferelation | Quantenunsicherheit | 0.75 | 4 | 1 | 1 | stated in 1 doc(s) ^[trauma-archaeologie-interdisziplinaere-konzeptentwicklung-do.md:L118] |
| Identifikation des Lesers | Narrative Transportation | 0.77 | 2 | 3 | 1 | stated in 1 doc(s) ^[narrative-physik-attraktoren-leserbewusstsein.md:L71] |
| Kernwelt Ly | Lyons-Welt | 0.40 | 2 | 3 | 1 | stated in 1 doc(s) ^[kernwelten-fuer-kohaerenz-protokoll.md:L332] ^[kernwelten-fuer-kohaerenz-protokoll.md:L464] |
| Madhyamaka Buddhismus | Madhyamaka Buddhist | 0.73 | 2 | 3 | 1 | proposed |
| Multiversale Verzweigungslogik | Many Worlds | 0.45 | 1 | 4 | 1 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L140] |
| Wert N | Neither | 0.70 | 2 | 3 | 2 | stated in 1 doc(s) ^[parakonsistente-logik-im-seelen-protokoll.md:L73] ^[parakonsistente-logik-im-seelen-protokoll.md:L131] |
| Neukalibrierung | Recalibration | 0.51 | 4 | 1 | 0 | proposed |
| Philosophische Zombies | P-Zombies | 0.60 | 2 | 3 | 2 | stated in 2 doc(s) ^[logik-trifft-transzendente-entitaet.md:L250] ^[logik-trifft-transzendente-entitaet-2.md:L248] |
| Planer | Planner | 0.60 | 4 | 1 | 0 | proposed |
| Verspielte | playful | 0.77 | 1 | 4 | 0 | proposed |
| Vertexoperatoralgebra | vertex operator algebra | 0.50 | 4 | 1 | 0 | proposed |
| ANP-Gruppe | Wächter der Kohärenz | 0.59 | 1 | 3 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-synthese-integration.md:L33] |
| Anhedonie | Dopamin-Dürre | 0.41 | 3 | 1 | 1 | stated in 1 doc(s) ^[heilung-hirnchemie-kunst-trauma.md:L114] |
| Assimilierte Transzendenz | Fundamentale Transformation | 0.63 | 2 | 2 | 2 | stated in 2 doc(s) ^[logik-trifft-transzendente-entitaet.md:L294] ^[logik-trifft-transzendente-entitaet-2.md:L292] |
| Autopoietische Isolation | autopoietic isolation | 0.73 | 3 | 1 | 0 | proposed |
| Bewertungsrahmen | evaluation framework | 0.65 | 2 | 2 | 0 | proposed |
| Bewusstseinsakt | Noesis | 0.77 | 1 | 3 | 1 | stated in 1 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L229] |
| Wattsnovel | Blindsight | 0.38 | 0 | 4 | 0 | stated in 1 doc(s) ^[hard-sci-fi-cosmic-horror-research-questions.md:L309] |
| Bruch der Immersion | Sünde der Inkohärenz | 0.61 | 2 | 2 | 1 | stated in 1 doc(s) ^[narrative-entropie-existenzielle-bedrohung-des-romans.md:L97] |
| Somatische Stimme | Cello | 0.49 | 1 | 3 | 1 | stated in 1 doc(s) ^[neurochemische-lyrik-transzendenz-durch-klang.md:L254] |
| Ladungen | Charges | 0.79 | 2 | 2 | 1 | stated in 1 doc(s) ^[dramatica-und-kohaerenz-protokoll-analyse.md:L29]; proposed |
| Risiko der Inkonsistenz | Consistency Risk Score | 0.72 | 2 | 2 | 0 | proposed |
| Conway-Welt | Kernwelt Co₁ | 0.70 | 1 | 3 | 1 | stated in 1 doc(s) ^[kernwelten-fuer-kohaerenz-protokoll.md:L184] ^[kernwelten-fuer-kohaerenz-protokoll.md:L464] |
| Digitalphysik | Digital physics | 0.57 | 1 | 3 | 0 | proposed |
| EP-Phobia | EP phobia | 0.67 | 3 | 1 | 0 | proposed |
| Einbruch der Bildwiederholrate | Framerate | 0.75 | 2 | 2 | 2 | stated in 2 doc(s) ^[gravitation-realitaet-simulation-wahrheit-2.md:L117] ^[konzept-expose-schwarzschild-protokoll-optimierung.md:L122] |
| Hiding | Encapsulation | 0.72 | 3 | 1 | 1 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L134] |
| Short-Term Memory | Episodic | 0.62 | 1 | 3 | 1 | stated in 1 doc(s) ^[dramatica-agentic-storyform-interactive-novel.md:L216] ^[dramatica-agentic-storyform-interactive-novel.md:L320] |
| Erason-Domäne | TEMPORAL | 0.72 | 2 | 2 | 2 | stated in 2 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L104] ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L164] |
| Flüssigkeit | Fluidity | 0.73 | 3 | 1 | 0 | proposed |
| Haufenparadox | Sorites-Paradox | 0.65 | 1 | 3 | 1 | stated in 1 doc(s) ^[paradoxien-der-kohaerenz-protokoll-entwicklung.md:L43] |
| Zischen | Hiss | 0.62 | 2 | 2 | 1 | proposed |
| Hyper-Kohärenz | Über-Strukturierung | 0.78 | 1 | 3 | 1 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L42] |
| K-J Vektor | K-J Vector | 0.66 | 2 | 2 | 1 | proposed |
| Kernwelt McL | McLaughlin-Welt | 0.77 | 3 | 1 | 1 | stated in 1 doc(s) ^[kernwelten-fuer-kohaerenz-protokoll.md:L233] ^[kernwelten-fuer-kohaerenz-protokoll.md:L464] |
| Komplexer Posttraumatischer Belastungsstörung | complex posttraumatic stress disorder | 0.69 | 2 | 2 | 0 | proposed |
| Kontrollstruktur | control structure | 0.69 | 3 | 1 | 0 | proposed |
| Männlich | Male | 0.76 | 1 | 3 | 0 | proposed |
| Mereologie | mereology | 0.79 | 3 | 1 | 1 | proposed |
| Mereologischer Fehler | Teilmengen-Paradoxon | 0.40 | 2 | 2 | 2 | stated in 2 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L287] ^[ki-rolle-aegis-genesis-fragestellungen.md:L227] |
| Mischen | Topologische Transitivität | 0.46 | 3 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptionelle-ausarbeitung.md:L71] |
| Mischen | mixing | 0.72 | 3 | 1 | 0 | proposed |
| Modell des Bewusstseins | Model of Consciousness | 0.73 | 3 | 1 | 0 | proposed |
| Ontologische Trägheit | Nachbeben | 0.63 | 1 | 3 | 1 | stated in 1 doc(s) ^[gravitation-realitaet-simulation-wahrheit.md:L185] |
| Orch-OR | Orchestrierung der Wellenfunktion | 0.66 | 3 | 1 | 1 | stated in 1 doc(s) ^[aegis-und-der-kollaps-kritische-analyse.md:L107] |
| Prinzips der Explosion | Principle of explosion | 0.70 | 1 | 3 | 1 | proposed |
| Psycho-Architektur | Psycho-Architecture | 0.77 | 2 | 2 | 0 | proposed |
| Wärmebad | Senke | 0.71 | 2 | 2 | 1 | stated in 1 doc(s) ^[aegis-protokolle-kritische-evaluation-neukonzeption.md:L129] |
| Signifikant | Zeichenform | 0.75 | 3 | 1 | 1 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L115] |
| Steiner-Systems | Witt-Design | 0.78 | 2 | 2 | 2 | stated in 1 doc(s) ^[monstergruppe-logik-und-metaphern.md:L179] |
| Strafenden | punishing | 0.55 | 2 | 2 | 0 | proposed |
| Systemarchitekt | System Architect | 0.65 | 2 | 2 | 0 | proposed |
| Akt IV | Rubedo-Phase | 0.51 | 2 | 1 | 1 | stated in 1 doc(s) ^[fragen-zu-existenz-agency-und-realitaet.md:L182] |
| Algorithmische Glättung | Harmonisierungs-Bias | 0.71 | 1 | 2 | 1 | stated in 1 doc(s) ^[ki-narrative-kollaps-kohaerenz-paradoxie.md:L41] |
| Amnesie-Lücken | Mikrosprünge | 0.70 | 2 | 1 | 1 | stated in 1 doc(s) ^[storyforms-system-mind-bewusstsein.md:L106] |
| Herbst | Autumn | 0.77 | 1 | 2 | 0 | proposed |
| BCI-Analogie | Computationale Schnittstelle | 0.47 | 2 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-inkubation-x.md:L180] |
| Beladene Sprache | Lifton | 0.78 | 1 | 2 | 1 | stated in 1 doc(s) ^[aegis-psychologische-kriegsfuehrung-narrative-eskalation.md:L132] |
| Belohnungs-Hacking | Reward hacking | 0.78 | 1 | 2 | 1 | proposed |
| Bindungsdichte | Information des Subsystems S | 0.76 | 2 | 1 | 1 | stated in 1 doc(s) ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L146] |
| Bootstrapping-Problem | P-INIT | 0.53 | 2 | 1 | 1 | stated in 1 doc(s) ^[aegis-protokolle-kritische-evaluation-neukonzeption.md:L105] |
| Handlungsbäume | Branching Narratives | 0.71 | 1 | 2 | 1 | stated in 1 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L199] |
| Spine | Central Axis | 0.52 | 2 | 1 | 1 | stated in 1 doc(s) ^[tattoo-konzept-symbolik-trauma-heilung.md:L283] |
| Chaitins Konstante | Chaitin-constant | 0.76 | 2 | 1 | 0 | proposed |
| Komplexer Posttraumatischer Belastungsstörung | Complex Posttraumatic Stress Disorder | 0.75 | 2 | 1 | 0 | proposed |
| Nutzlast | Data-Payload | 0.66 | 2 | 1 | 1 | proposed |
| Payload | Data-Payload | 0.59 | 2 | 1 | 1 | proposed |
| Datenfriedhof | Veraltete Infos | 0.54 | 2 | 1 | 1 | stated in 1 doc(s) ^[orte-konzept-fuer-kohaerenz-protokoll.md:L329] ^[orte-konzept-fuer-kohaerenz-protokoll.md:L525] |
| Dominoeffekt | Domino Effect | 0.76 | 2 | 1 | 1 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L540]; proposed |
| Drei Phasen des Protokolls | Isomorphe Progression | 0.55 | 2 | 1 | 1 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L196] |
| EP Relationale Spannungen | EP-EP Dynamiken | 0.57 | 1 | 2 | 1 | stated in 1 doc(s) ^[tsdp-analyse-kohaerenz-protokoll-charaktere.md:L142] |
| Energien des Es | Id | 0.72 | 1 | 2 | 1 | stated in 1 doc(s) ^[narrative-physik-attraktoren-leserbewusstsein.md:L89] |
| Failsafe-Mechanismus | Notabschaltung | 0.41 | 1 | 2 | 1 | stated in 1 doc(s) ^[aegis-subplots-kapitelweise-system-exploration-docx.md:L473] |
| Farbwahrnehmung | Greyout | 0.79 | 2 | 1 | 1 | stated in 1 doc(s) ^[gravitation-realitaet-simulation-wahrheit-2.md:L129] |
| Gedächtnispaläste | Methode der Loci | 0.78 | 1 | 2 | 1 | stated in 1 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L153] |
| Gekoppelte Oszillatoren | Kuramoto-Modell | 0.44 | 2 | 1 | 1 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L131] |
| Hyperativitätsstörung | Hyperactivity Disorder | 0.79 | 1 | 2 | 0 | proposed |
| Hypokortisolismus | Niedriges Kortisol | 0.54 | 2 | 1 | 1 | stated in 1 doc(s) ^[heilung-hirnchemie-kunst-trauma.md:L46] |
| Klassischer Kollaps | Hypothese B | 0.67 | 1 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-plot-entwicklung-und-wahrheitsdualitaet.md:L123] ^[kohaerenz-protokoll-plot-entwicklung-und-wahrheitsdualitaet.md:L144] |
| Informationsspeicher | information storage | 0.69 | 2 | 1 | 0 | proposed |
| Juna-Link | Juna connection | 0.37 | 1 | 2 | 0 | proposed |
| Kernabwehr | core defense | 0.70 | 1 | 2 | 0 | proposed |
| Komplexen Posttraumatischen Belastungsstörung | complex posttraumatic stress disorder | 0.75 | 1 | 2 | 0 | proposed |
| Kreativ-KI | creative AI | 0.74 | 2 | 1 | 0 | proposed |
| Kryptographische Achse | NP-Verifikation | 0.43 | 1 | 2 | 1 | stated in 1 doc(s) ^[storyforms-system-mind-bewusstsein.md:L135] |
| Makroskopische Ordnungsmuster | Ordnungsparameter | 0.56 | 1 | 2 | 1 | stated in 1 doc(s) ^[emergenz-aegis-und-selbststrukturierung.md:L386] |
| Melancholie-Zone | See der Tränen | 0.52 | 1 | 2 | 1 | stated in 1 doc(s) ^[orte-konzept-fuer-kohaerenz-protokoll.md:L299] |
| Metakognitiver Beobachter | meta-cognitive observer | 0.76 | 2 | 1 | 0 | proposed |
| Metaphysische Ebene | Metaphysical Dimension | 0.74 | 2 | 1 | 0 | proposed |
| Paradox-Maschine | Modell Alpha | 0.46 | 2 | 1 | 1 | stated in 1 doc(s) ^[logiksystem-aegis-entwicklungsszenarien-docx.md:L165] |
| Token-Wahrscheinlichkeiten | Naive Entropy | 0.62 | 1 | 2 | 1 | stated in 1 doc(s) ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:L99] |
| Namenlos | nameless | 0.72 | 1 | 2 | 0 | proposed |
| Non-Malefizienz | Patientenwürde und Nicht-Schaden | 0.42 | 2 | 1 | 1 | stated in 1 doc(s) ^[dis-berichtigung-umfassende-recherche-und-schreiben.md:L174] |
| Non-Malefizienz | Prinzip des Nicht-Schadens | 0.71 | 2 | 1 | 1 | stated in 1 doc(s) ^[dis-berichtigung-umfassende-recherche-und-schreiben.md:L172] |
| Ouroboros-Ende | Zyklische Auflösung | 0.77 | 2 | 1 | 1 | stated in 1 doc(s) ^[konsolidierung-des-hard-canon-protokolls.md:L34] |
| PMAS-Protokoll | Predictive Modality Alignment | 0.62 | 2 | 1 | 1 | stated in 1 doc(s) ^[hard-sf-roman-outline-dkt-physik-cosmic-horror.md:L118] |
| Vorhersagekraft | Predictive Psychology | 0.52 | 2 | 1 | 1 | stated in 1 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L154] |
| Rebell | Rebel | 0.78 | 2 | 1 | 0 | proposed |
| Schützer | guardians | 0.61 | 1 | 2 | 0 | proposed |
| Selbst-Schöpfung | self-creation | 0.75 | 2 | 1 | 0 | proposed |
| Somatosensorischer Kortex | Sensory Cortex | 0.57 | 1 | 2 | 0 | proposed |
| Simulacra | Zeichen und Symbole | 0.57 | 2 | 1 | 1 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L207] |
| Strafenden | punitive | 0.63 | 2 | 1 | 0 | proposed |
| Zufällige Netzwerk-Schließung | Szenario C | 0.33 | 1 | 2 | 1 | stated in 1 doc(s) ^[aegis-logik-in-der-leere-docx.md:L188] |
| Umwelt-Rauschen | environmental noise | 0.73 | 2 | 1 | 0 | proposed |
| Weltmodelle | World models | 0.75 | 1 | 2 | 0 | proposed |
| Zero-Trust-Architekturen | Zero Trust Architectures | 0.61 | 2 | 1 | 0 | proposed |
| Kernzone | AEGIS-Nexus | 0.53 | 1 | 1 | 1 | stated in 1 doc(s) ^[dkt-fundament-kohaerenz-protokoll-md.md:L164] |
| AEGIS-Unterdrückung | Landauer-Signatur | 0.74 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L428] |
| ANP Strategische Divergenz | ANP-ANP Konflikte | 0.55 | 1 | 1 | 1 | stated in 1 doc(s) ^[tsdp-analyse-kohaerenz-protokoll-charaktere.md:L132] |
| ASDS-1a | OSDD-1a | 0.33 | 1 | 1 | 1 | stated in 1 doc(s) ^[roman-konzept-kael-aegis-simulation.md:L76] |
| Abhängige Paar-Interferenz | Vertikale Beziehung | 0.66 | 1 | 1 | 1 | stated in 1 doc(s) ^[narrative-context-protocol-ncp-spezifikation.md:L73] |
| Aggressive Korrespondenz-Wahrheit | Fakt des Widerstands | 0.64 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-plot-entwicklung-und-wahrheitsdualitaet.md:L71] |
| Algorithmischer Bias | Computational Bias | 0.71 | 1 | 1 | 0 | proposed |
| Alpträume | Exile-Lasten | 0.58 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-thematische-tiefenanalyse.md:L277] |
| Approximationsgitter | Informationsgitter | 0.71 | 1 | 1 | 1 | stated in 1 doc(s) ^[parakonsistente-logik-im-seelen-protokoll.md:L56] |
| Authentische Heilung | genuine healing | 0.72 | 1 | 1 | 0 | proposed |
| Basisuntersuchung | MSE | 0.60 | 1 | 1 | 1 | stated in 1 doc(s) ^[dis-diagnose-klinische-ethische-rechtliche-analyse.md:L98] |
| Belohnungssignale | Reward Engineering | 0.50 | 1 | 1 | 1 | stated in 1 doc(s) ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:L107] |
| Cache Kohärenz Fehler | Falscherinnerungen | 0.64 | 1 | 1 | 1 | stated in 1 doc(s) ^[charaktermodellierung-mit-aieos-schema.md:L192] |
| Gedankenfolge | Chain of Thought | 0.64 | 1 | 1 | 0 | proposed |
| Chaos-Zone | E4 | 0.40 | 1 | 1 | 1 | stated in 1 doc(s) ^[roman-outline-system-kael.md:L275] |
| Negative Space | Charged Void | 0.65 | 1 | 1 | 1 | stated in 1 doc(s) ^[tattoo-konzept-symbolik-trauma-heilung.md:L102] |
| Charles Dodgson | Lewis Carroll | 0.37 | 1 | 1 | 1 | stated in 1 doc(s) ^[monstergruppe-als-narrative-inspiration.md:L217] |
| Schutzschalter-Funktion | Circuit-Breaking | 0.73 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L33] |
| Logik-Schleife | CogFirewall | 0.42 | 1 | 1 | 1 | stated in 1 doc(s) ^[hard-sf-roman-outline-dkt-physik-cosmic-horror.md:L122] |
| Conductor | System Lead | 0.57 | 1 | 1 | 1 | stated in 1 doc(s) ^[kael-s-dissociative-architecture-analysis.md:L230] |
| Memory-Management-Pattern | Context Rot Mitigation | 0.48 | 1 | 1 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L436] |
| Prompt Functions | Custom Instruction Grammar | 0.67 | 1 | 1 | 1 | stated in 1 doc(s) ^[codex-optimierung-fuer-kohaerenz-protokoll.md:L573] |
| Latent Space Projection | Decoupled Semantic Encoding | 0.51 | 1 | 1 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L211] |
| Diagonale Beziehung | Dynamische Paar-Interferenz | 0.41 | 1 | 1 | 1 | stated in 1 doc(s) ^[narrative-context-protocol-ncp-spezifikation.md:L71] |
| Dissoziative Derealisation | Vektor-Instabilität | 0.61 | 1 | 1 | 1 | stated in 1 doc(s) ^[storyforms-system-mind-bewusstsein.md:L105] |
| Träumerin | Dreamer | 0.72 | 1 | 1 | 0 | proposed |
| EP-Gruppe | Träger der Korrespondenz | 0.40 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-synthese-integration.md:L41] |
| EP-Intrusion2 | Interner Glitch | 0.68 | 1 | 1 | 1 | stated in 1 doc(s) ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:L260] |
| EPR Bridge | Safe Connection | 0.42 | 1 | 1 | 1 | stated in 1 doc(s) ^[reality-s-isomorphic-architecture-explained.md:L379] |
| Metzingers Theorie des Selbstmodells | Ego Tunnel | 0.61 | 1 | 1 | 1 | stated in 1 doc(s) ^[roman-entwicklung-ontologie-trauma-horror.md:L23] |
| Enaktive | Enactive | 0.70 | 1 | 1 | 0 | proposed |
| Externer Glitch | Versagen der Quanten-Dekohärenz1 | 0.59 | 1 | 1 | 1 | stated in 1 doc(s) ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:L260] |
| Schnelles Denken | Fast Thinking | 0.70 | 1 | 1 | 1 | stated in 1 doc(s) ^[ki-narrative-kollaps-kohaerenz-paradoxie.md:L128]; proposed |
| Fokus-Verlust | I They | 0.71 | 1 | 1 | 1 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-analyse.md:L113] |
| Thermische Objekte | Foreshadowing-Trigger | 0.64 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-projekt-rekonstruktion.md:L227] |
| Fundamentalsatz der Arithmetik | Fundamentale Bausteine | 0.62 | 1 | 1 | 1 | stated in 1 doc(s) ^[primzahlen-als-metapher-in-kohaerenz-protokoll.md:L41] |
| GAF-Skala | Global Assessment of Functioning | 0.65 | 1 | 1 | 1 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L188] |
| Gehirn-Computer-Schnittstellen | brain-computer interfaces | 0.69 | 1 | 1 | 1 | proposed |
| Isolations-Kollaps | I They | 0.63 | 1 | 1 | 1 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-analyse.md:L87] |
| Isolations-Inversion | I We | 0.47 | 1 | 1 | 1 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-analyse.md:L139] |
| Strikte Chronologie | INV-04 | 0.62 | 1 | 1 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L516] |
| Imaginatives Überschreiben | Technik des Imagery Rescripting | 0.62 | 1 | 1 | 1 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L173] |
| Inanna | Ishtar | 0.44 | 1 | 1 | 1 | stated in 1 doc(s) ^[tattoo-konzept-symbolik-trauma-heilung.md:L214] |
| Integrierte Sensorarchitektur | Integrated Sensor Architecture | 0.63 | 1 | 1 | 1 | proposed |
| Moonshine Resonance Vektor | K-J Vector | 0.44 | 0 | 2 | 0 | stated in 1 doc(s) ^[kohaerenz-protokoll-duale-dramatica-storyform-synthese.md:L125] |
| Schlüsselgenerierung | KeyGen | 0.46 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-philosophische-und-systemtheoretische-analyse-docx.md:L114] |
| Kintsugi-Knoten | Reparaturoperator | 0.60 | 1 | 1 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L82] |
| Kollaps der Kernwelten | Totale Auflösung der Realität | 0.34 | 1 | 1 | 1 | stated in 1 doc(s) ^[projektplanung-fuer-kohaerenz-protokoll.md:L199] |
| Konsens und Konfliktlösung | Zero-Trust Dynamik | 0.48 | 1 | 1 | 1 | stated in 1 doc(s) ^[digitale-uberwelt.md:L40] |
| Leere Menge | Null-Raum | 0.65 | 1 | 1 | 1 | stated in 1 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L195] |
| Leitende | Supervisors | 0.72 | 1 | 1 | 0 | proposed |
| Phantomschmerz der Identität | Lost Time | 0.79 | 1 | 1 | 1 | stated in 1 doc(s) ^[roman-konzept-dualitaet-kohaerenz-spannung.md:L71] |
| Unrealität der Zeit | McTaggarts Paradox | 0.79 | 1 | 1 | 1 | stated in 1 doc(s) ^[paradoxien-der-kohaerenz-protokoll-entwicklung.md:L47] |
| Pilznetzwerk | Mykorrhiza | 0.77 | 1 | 1 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L94] |
| N-Zustand | Unmappbarkeit | 0.57 | 1 | 1 | 1 | stated in 1 doc(s) ^[parakonsistente-logik-im-seelen-protokoll.md:L262] |
| Nicht-Kontrollierte Selbstinitialisierung | Nullpunkt-Protokoll | 0.69 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L42] |
| Ontologische Identitäts-Paradox | Ursprung des Bewusstseins | 0.51 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-projekt-rekonstruktion.md:L235] |
| Spezifikation der Ziele | Outer Alignment | 0.46 | 1 | 1 | 1 | stated in 1 doc(s) ^[m-als-fundament-der-simulation.md:L71] |
| State of Disruption | Outside Tolerances | 0.67 | 1 | 1 | 1 | stated in 1 doc(s) ^[global-research-for-kohaerenz-protokoll.md:L137] |
| Paradoxon des Seins | paradox of being | 0.74 | 1 | 1 | 0 | proposed |
| Phönix Mode | Phoenix Mode | 0.59 | 1 | 1 | 0 | proposed |
| Schreibanforderungen | PrWrite | 0.75 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L64] |
| Rational ANP | Rationale ANP | 0.60 | 1 | 1 | 0 | proposed |
| Rein Phänomenal | Reine K1-Zonen | 0.37 | 1 | 1 | 1 | stated in 1 doc(s) ^[ki-prompt-analyse-hard-problem-of-consciousness.md:L243] |
| Reizfilterung | Thalamus-Hyperaktivität | 0.34 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L91] |
| Soziale Teile | Relational-Emotional | 0.50 | 1 | 1 | 1 | stated in 1 doc(s) ^[kernwelten-fuer-kohaerenz-protokoll.md:L469] |
| SARM-Rekursion | Self-Axiomatizing Recursive Matrix | 0.53 | 1 | 1 | 1 | stated in 1 doc(s) ^[hard-sf-roman-outline-dkt-physik-cosmic-horror.md:L184] |
| sichere Verbindung | Safe Connection | 0.71 | 1 | 1 | 0 | proposed |
| Speicherbereichs | Shared Memory | 0.64 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L29] |
| Sonderfarbe | Spot-Farbe | 0.57 | 1 | 1 | 1 | stated in 1 doc(s) ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L661] |
| Stil-Anweisungen | style guidelines | 0.63 | 1 | 1 | 0 | proposed |
| Struktureller Ausschluss | structural barrier | 0.57 | 1 | 1 | 0 | proposed |
| systemische Verantwortung | Systemic Responsibility | 0.67 | 1 | 1 | 0 | proposed |
| Sünde der Vagheit | Verwässerung der Realität | 0.65 | 1 | 1 | 1 | stated in 1 doc(s) ^[narrative-entropie-existenzielle-bedrohung-des-romans.md:L109] |
| Unendliche Auflösung | Wenn die Wahrheit | 0.63 | 1 | 1 | 1 | stated in 1 doc(s) ^[gravitation-realitaet-simulation-wahrheit-2.md:L302] |
| Wahrheitswertüberlappungen | Überbestimmtheit | 0.61 | 1 | 1 | 1 | stated in 1 doc(s) ^[parakonsistente-logik-im-seelen-protokoll.md:L131] ^[parakonsistente-logik-im-seelen-protokoll.md:L155] |
| Wahrheit des Traumas | Akzeptanz der Korrespondenz | 0.48 | 1 | 0 | 0 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L227] |
| Auch Moralische Entkopplung | Moral Disengagement | 0.65 | 0 | 1 | 0 | stated in 1 doc(s) ^[trauma-archaeologie-interdisziplinaere-konzeptentwicklung-do.md:L107] |

## Abbreviations — 989

| long | short | p | docs (de) | docs (en) | docs (both) | evidence |
|---|---|--:|--:|--:|--:|---|
| Strukturellen Dissoziation der Persönlichkeit | TSDP | 1.00 | 46 | 151 | 45 | stated in 41 doc(s) ^[kohaerenz-protokoll-konzeptentwicklung.md:L11] ^[analyse-des-kohaerenz-protokolls.md:L26] |
| TSDP | Dissociation of the Personality | 1.00 | 151 | 65 | 63 | stated in 37 doc(s) ^[a-learner-s-glossary-for-the-world-of-kohaerenz-protokoll.md:L29] ^[a-learner-s-glossary-for-the-world-of-kohaerenz-protokoll.md:L101] |
| OS | Objective Story | 0.97 | 43 | 31 | 27 | stated in 22 doc(s) ^[briefing-core-concepts-of-the-kohaerenz-protokoll-project.md:L151] ^[coherence-critique-and-question-generation.md:L87] |
| DKT | Dual Kernel Theory | 0.96 | 60 | 42 | 33 | stated in 20 doc(s) ^[concept-paper-the-architectural-foundations-of-kohaerenz-pro.md:L23] ^[exploring-the-coherence-protocol.md:L166] |
| NCP | Narrative Context Protocol | 1.00 | 23 | 21 | 20 | stated in 19 doc(s) ^[briefing-core-concepts-of-the-kohaerenz-protokoll-project.md:L19] ^[briefing-core-concepts-of-the-kohaerenz-protokoll-project.md:L170] |
| Dissoziative Identitätsstörung | DIS | 0.97 | 41 | 53 | 28 | stated in 18 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L17] ^[kohaerenz-protokoll-dramatica-synthese.md:L21] |
| IIT | Integrated Information Theory | 0.99 | 29 | 23 | 21 | stated in 17 doc(s) ^[a-learner-s-glossary-for-the-world-of-kohaerenz-protokoll.md:L108] ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L385] |
| DID | Dissociative Identity Disorder | 0.79 | 100 | 44 | 36 | stated in 17 doc(s) ^[kohaerenz-prozess-grundlagen.md:L241] ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1594] |
| DKT | Dual-Kernel Theory | 0.72 | 60 | 19 | 17 | stated in 14 doc(s) ^[companion-guide-to-the-coherence-protocol-understanding-love.md:L17] ^[global-research-for-kohaerenz-protokoll.md:L13] |
| SS | Subjective Story | 0.96 | 19 | 15 | 14 | stated in 13 doc(s) ^[briefing-core-concepts-of-the-kohaerenz-protokoll-project.md:L154] ^[kohaerenz-protokoll-analyse-und-synthese.md:L48] |
| LFI | Logics of Formal Inconsistency | 0.94 | 25 | 20 | 18 | stated in 12 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L227] ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L653] |
| Dissoziativen Identitätsstörung | DIS | 0.92 | 38 | 53 | 22 | stated in 12 doc(s) ^[kohaerenz-protokoll-detaillierte-recherche.md:L195] ^[kohaerenz-protokoll-synthese-integration.md:L17] |
| TSDP | Tertiary Structural Dissociation | 0.76 | 151 | 30 | 29 | stated in 11 doc(s) ^[companion-guide-to-the-coherence-protocol-understanding-love.md:L54] ^[dramaturgical-precision-deconstructing-the-irreversible-conf.md:L15] |
| FEP | Free Energy Principle | 0.98 | 10 | 12 | 10 | stated in 9 doc(s) ^[global-research-for-kohaerenz-protokoll.md:L65] ^[kohaerenz-protokoll-konzeptionelle-ausarbeitung.md:L125] |
| Dissoziation der Persönlichkeit | TSDP | 0.96 | 65 | 151 | 60 | stated in 9 doc(s) ^[kohaerenz-protokoll-architecture-synthesis-2.md:L47] ^[aieos-schema-fuer-ki-charaktere.md:L15] |
| EP | Emotional Part | 0.96 | 140 | 28 | 28 | stated in 9 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L219] ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L75] |
| Vertex-Operator-Algebra | VOA | 0.93 | 13 | 31 | 11 | stated in 9 doc(s) ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L301] ^[kohaerenz-protokoll-architecture-synthesis.md:L27] |
| ANP | Apparently Normal Part | 0.87 | 145 | 31 | 31 | stated in 9 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L218] ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L75] |
| Grades der Behinderung | GdB | 0.87 | 9 | 11 | 9 | stated in 9 doc(s) ^[dis-berichtigung-umfassende-recherche-und-schreiben.md:L19] ^[dis-berichtigung-umfassende-recherche-und-schreiben.md:L234] |
| Dissoziativen Identitätsstörung | DID | 0.82 | 38 | 100 | 24 | stated in 9 doc(s) ^[kohaerenz-protokoll-konzept.md:L17] ^[kohaerenz-protokoll-konzept.md:L31] |
| Dual-Kernel-Theorie | DKT | 0.98 | 22 | 60 | 19 | stated in 8 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L31] ^[kohaerenz-protokoll-architecture-synthesis-2.md:L17] |
| Strukturelle Dissoziation | TSDP | 0.98 | 51 | 151 | 44 | stated in 8 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L209] ^[dramatica-storyform-synthese-aegis-verortung.md:L45] |
| GWT | Global Workspace Theory | 0.97 | 9 | 10 | 8 | stated in 8 doc(s) ^[global-research-for-kohaerenz-protokoll.md:L71] ^[global-research-for-kohaerenz-protokoll.md:L95] |
| TSDP | Theory of Structural Dissociation | 0.95 | 151 | 44 | 42 | stated in 8 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L827] ^[an-introduction-to-the-world-of-kohaerenz-protokoll.md:L35] |
| Tertiäre Strukturelle Dissoziation | TSDP | 0.87 | 20 | 151 | 20 | stated in 8 doc(s) ^[kohaerenz-protokoll-finale-pfeiler.md:L140] ^[charaktere.md:L112] |
| DMN | Default Mode Network | 0.96 | 7 | 7 | 7 | stated in 7 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L33] ^[dissoziative-identitaetsstoerung-unsichtbare-diagnose.md:L107] |
| Dissoziative Identitätsstörung | DID | 0.93 | 41 | 100 | 25 | stated in 7 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L112] ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L164] |
| SIS | Secure Isolation State | 0.81 | 15 | 8 | 8 | stated in 7 doc(s) ^[digitale-uberwelt.md:L49] ^[digitale-uberwelt.md:L49] |
| Dissoziation | TSDP | 0.75 | 157 | 151 | 95 | stated in 7 doc(s) ^[kohaerenz-protokoll-architecture-synthesis-2.md:L45] ^[kohaerenz-protokoll-architecture-synthesis-2.md:L214] |
| Large Language Model | LLM | 1.00 | 7 | 28 | 6 | stated in 6 doc(s) ^[dramatica-agentic-storyform-interactive-novel.md:L177] ^[narrative-context-protocol-ncp-spezifikation.md:L15] |
| MCP | Model Context Protocol | 0.96 | 9 | 6 | 6 | stated in 6 doc(s) ^[briefing-core-concepts-of-the-kohaerenz-protokoll-project.md:L173] ^[ki-agenten-kohaerenz-und-prompt-generierung.md:L356] |
| Anscheinend Normale Persönlichkeitsanteile | ANPs | 0.94 | 15 | 122 | 13 | stated in 6 doc(s) ^[charaktermodellierung-mit-aieos-schema.md:L17] ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:L41] |
| ISSTD | Trauma and Dissociation | 0.91 | 20 | 10 | 8 | stated in 6 doc(s) ^[juna-kael-system-krisenanalyse-und-rettungsplan.md:L172] ^[dis-berichtigung-umfassende-recherche-und-schreiben.md:L77] |
| Emotionale Persönlichkeitsanteile | EPs | 0.75 | 18 | 142 | 14 | stated in 6 doc(s) ^[charaktermodellierung-mit-aieos-schema.md:L17] ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:L41] |
| Emotionalen Persönlichkeitsanteile | EPs | 0.70 | 9 | 142 | 9 | stated in 6 doc(s) ^[charaktermodellierung-mit-aieos-schema.md:L43] ^[roman-outline-system-kael.md:L80] |
| CAS | Systeme | 0.48 | 15 | 175 | 13 | stated in 6 doc(s) ^[kohaerenz-protokoll-aktuelle-gesamtkonzept-synthese.md:L25] ^[logik-trifft-transzendente-entitaet.md:L178] |
| Sozialgerichtsgesetz | SGG | 1.00 | 5 | 6 | 5 | stated in 5 doc(s) ^[gutachten-grad-der-behinderung-bei-dis.md:L24] ^[juristische-recherche-zu-kptbs-dis.md:L418] |
| Versorgungsmedizin-Verordnung | VersMedV | 1.00 | 9 | 9 | 9 | stated in 5 doc(s) ^[dis-diagnose-klinische-ethische-rechtliche-analyse.md:L208] ^[dissoziative-identitaetsstoerung-unsichtbare-diagnose.md:L127] |
| VOA | Vertex Operator Algebra | 0.99 | 31 | 7 | 5 | stated in 5 doc(s) ^[kohaerenz-protokoll-aktuelle-gesamtkonzept-synthese.md:L30] ^[kohaerenz-protokoll-aktuelle-gesamtkonzept-synthese-abstrakt.md:L41] |
| DES | Dissociative Experiences Scale | 0.97 | 9 | 6 | 6 | stated in 5 doc(s) ^[neurochemische-lyrik-transzendenz-durch-klang.md:L340] ^[dis-berichtigung-umfassende-recherche-und-schreiben.md:L81] |
| Behandlung der Dissoziativen Identitätsstörung | DIS | 0.96 | 6 | 53 | 6 | stated in 5 doc(s) ^[kohaerenz-protokoll-konzept.md:L416] ^[juna-kael-system-analyse-und-rettungsplan-docx.md:L416] |
| IFS | Internal Family Systems | 0.92 | 68 | 57 | 54 | stated in 5 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L162] ^[kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md.md:L572] |
| D2 | Discursive Logic | 0.89 | 10 | 11 | 7 | stated in 5 doc(s) ^[thematic-architecture-of-kohaerenz-protokoll-a-conceptual-le.md:L132] ^[dramatica-und-kohaerenz-protokoll-analyse.md:L121] |
| Identitätsstörung | DIS | 0.83 | 74 | 53 | 37 | stated in 5 doc(s) ^[monstergruppe-aegis-und-narrative-moeglichkeiten.md:L15] ^[angst-und-vermeidung-in-dis-systemen.md:L15] |
| EPs | Emotional Parts | 0.81 | 142 | 78 | 73 | stated in 5 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1293] ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1431] |
| Posttraumatischen Belastungsstörung | PTBS | 0.78 | 11 | 27 | 11 | stated in 5 doc(s) ^[kohaerenz-prozess.md:L47] ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L31] |
| KW1 | Logos-Prime | 0.63 | 81 | 62 | 49 | stated in 5 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L571] ^[projektplanung-fuer-kohaerenz-protokoll.md:L42] |
| KW3 | Cerberus-Labyrinth | 0.47 | 69 | 47 | 37 | stated in 5 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L588] ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1064] |
| CTM | Computational Theory of Mind | 1.00 | 4 | 5 | 4 | stated in 4 doc(s) ^[aegis-genesis-krise-prosa-auftrag-2.md:L456] ^[aegis-genesis-krise-prosa-auftrag-2.md:L486] |
| MPD | Dissociative Identity Disorder | 0.99 | 5 | 44 | 5 | stated in 4 doc(s) ^[kohaerenz-protokoll-forschungsaufgabe.md:L344] ^[konzeptanalyse-kohaerenz-protokoll-s-fundament.md:L395] |
| TSDP | Structural Dissociation of Personality | 0.99 | 151 | 5 | 5 | stated in 4 doc(s) ^[briefing-core-concepts-of-the-kohaerenz-protokoll-project.md:L17] ^[pitch-deck-coherence-protocol.md:L47] |
| AEGIS | Gatekeeper for Identity Systems | 0.98 | 269 | 5 | 5 | stated in 4 doc(s) ^[aegis-manifest-genesis-krise-reboot.md:L15] ^[aegis-manifest-genesis-krise-reboot-2.md:L15] |
| Quantenmechanik | QM | 0.98 | 45 | 9 | 6 | stated in 4 doc(s) ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L35] ^[holographisches-prinzip-fuer-kohaerenz-protokoll-2.md:L35] |
| SDD | Spec-Driven Development | 0.97 | 5 | 5 | 5 | stated in 4 doc(s) ^[comprehensive-systemic-architectural-and-psychological-conte.md:L103] ^[aegis-manifest-genesis-krise-reboot.md:L214] |
| Resonanz-Landschaft | KW2 | 0.96 | 23 | 75 | 14 | stated in 4 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung-2.md:L35] ^[roman-lokalitaeten-konzept-und-ausarbeitung-3.md:L35] |
| EFE | Expected Free Energy | 0.94 | 4 | 5 | 4 | stated in 4 doc(s) ^[aegis-manifest-genesis-krise-reboot.md:L167] ^[aegis-manifest-genesis-krise-reboot-2.md:L219] |
| Komplexe Adaptive Systeme | CAS | 0.93 | 4 | 15 | 4 | stated in 4 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L88] ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L166] |
| Kernwelten | KW | 0.84 | 134 | 12 | 8 | stated in 4 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L401] ^[kohaerenz-protokoll-weltkonzept-synthese.md:L68] |
| Identitätsstörung | DID | 0.81 | 74 | 100 | 51 | stated in 4 doc(s) ^[kohaerenz-protokoll-architecture-synthesis-2.md:L49] ^[kael-charakterarchitektur-und-konfliktdynamik.md:L32] |
| Psychotraumatologie | DeGPT | 0.79 | 18 | 7 | 7 | stated in 4 doc(s) ^[dissoziative-identitaet-invalidierung-im-gesundheitssystem.md:L184] ^[dissoziative-identitaet-invalidierung-im-gesundheitssystem.md:L226] |
| ANPs | Apparently Normal Parts | 0.77 | 122 | 64 | 58 | stated in 4 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1292] ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1430] |
| Kern-Welten | KW1-4 | 0.74 | 25 | 10 | 7 | stated in 4 doc(s) ^[system-kael-konzeptentwicklung-und-analyse.md:L156] ^[orte-konzept-fuer-kohaerenz-protokoll.md:L17] |
| Tertiären Strukturellen Dissoziation | TSDP | 0.74 | 12 | 151 | 12 | stated in 4 doc(s) ^[kohaerenz-protokoll-finale-pfeiler.md:L144] ^[dramatica-und-kohaerenz-protokoll-analyse.md:L21] |
| K₁ | Coherence | 0.73 | 24 | 119 | 17 | stated in 4 doc(s) ^[concept-paper-the-architectural-foundations-of-kohaerenz-pro.md:L21] ^[kohaerenz-protokoll-architecture-synthesis.md:L231] |
| Möglichkeits-Garten | KW4 | 0.67 | 22 | 68 | 18 | stated in 4 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung-2.md:L35] ^[roman-lokalitaeten-konzept-und-ausarbeitung-3.md:L35] |
| Integrierte Informationstheorie | IIT | 0.63 | 6 | 29 | 6 | stated in 4 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L86] ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L460] |
| Konformen Feldtheorie | CFT | 0.59 | 4 | 25 | 4 | stated in 4 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L377] ^[kohaerenz-protokoll-aktuelle-gesamtkonzept-synthese.md:L30] |
| MID | Multidimensional Inventory of Dissociation | 1.00 | 4 | 4 | 4 | stated in 3 doc(s) ^[dis-berichtigung-umfassende-recherche-und-schreiben.md:L81] ^[dis-diagnose-klinische-ethische-rechtliche-analyse.md:L104] |
| SVI | Self-Verification Interface | 1.00 | 4 | 3 | 3 | stated in 3 doc(s) ^[recherche-ueberwelt.md:L43] ^[romananfang-leere-und-systemgenesis.md:L112] |
| Strukturelle Dissoziation der Persönlichkeit | TSDP | 1.00 | 9 | 151 | 9 | stated in 3 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L72] ^[charaktermodellierung-mit-aieos-schema.md:L17] |
| UNM | Universal Narrative Model | 1.00 | 4 | 4 | 3 | stated in 3 doc(s) ^[dramatica-agentic-storyform-interactive-novel.md:L90] ^[dramatica-agentic-storyform-interactive-novel.md:L101] |
| Borderline-Persönlichkeitsstörung | BPS | 0.99 | 12 | 12 | 4 | stated in 3 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L103] ^[angst-bei-komplexen-traumafolgen.md:L107] |
| DRI | Dynamic Role Instancing | 0.99 | 3 | 3 | 3 | stated in 3 doc(s) ^[recherche-ueberwelt.md:L49] ^[romananfang-leere-und-systemgenesis.md:L113] |
| Deutsche Rentenversicherung | DRV | 0.99 | 7 | 5 | 4 | stated in 3 doc(s) ^[gutachterprofil-und-alternativen-ptbs-dis.md:L65] ^[juristische-recherche-zu-kptbs-dis.md:L257] |
| Orch-OR | Orchestrated Objective Reduction | 0.99 | 3 | 3 | 3 | stated in 3 doc(s) ^[dual-kernel-erzaehlarchitektur-bewusstsein-symmetrie-ourobor.md:L27] ^[ki-narrative-kollaps-kohaerenz-paradoxie.md:L19] |
| Redundanzfreie Informationskapselung | RIK | 0.99 | 3 | 3 | 3 | stated in 3 doc(s) ^[recherche-ueberwelt.md:L48] ^[romananfang-leere-und-systemgenesis.md:L184] |
| MC | Main Character | 0.98 | 38 | 39 | 36 | stated in 3 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L442] ^[duale-storyform-synthese-kohaerenz-protokoll.md:L68] |
| RS | Relationship Story | 0.98 | 23 | 24 | 19 | stated in 3 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L445] ^[duale-storyform-synthese-kohaerenz-protokoll.md:L71] |
| SIS | Systemic Isolation Shield | 0.97 | 15 | 4 | 3 | stated in 3 doc(s) ^[digitale-uberwelt-konzept-und-gestaltung.md:L66] ^[aegis.md:L189] |
| Konstrukt-Welten | KWs | 0.96 | 4 | 9 | 4 | stated in 3 doc(s) ^[2-kohaerenz-protokoll-konzeptentwicklung.md:L39] ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L22] |
| ECQ | Ex Contradictione Quodlibet | 0.95 | 9 | 10 | 5 | stated in 3 doc(s) ^[dialetheismus-im-kohaerenz-protokoll.md:L90] ^[parakonsistente-logik-fuer-kohaerenz-protokoll.md:L19] |
| Künstliche Intelligenz | KI | 0.95 | 19 | 167 | 19 | stated in 3 doc(s) ^[prosaversion-von-genesis-erstellen.md:L91] ^[wahrheitstheorien-kohaerenz-vs-korrespondenz.md:L353] |
| Posttraumatische Belastungsstörung | PTBS | 0.95 | 15 | 27 | 13 | stated in 3 doc(s) ^[kohaerenz-prozess-grundlagen.md:L239] ^[kohaerenz-prozess-grundlagen.md:L240] |
| Vertex-Operator-Algebren | VOA | 0.95 | 13 | 31 | 11 | stated in 3 doc(s) ^[dramatica-dual-storyform-mapping-protokoll.md:L13] ^[dramatica-dual-storyform-mapping-protokoll.md:L36] |
| Störungen der Selbstorganisation | DSO | 0.94 | 6 | 7 | 5 | stated in 3 doc(s) ^[juristische-recherche-zu-kptbs-dis.md:L23] ^[juristische-recherche-zu-kptbs-dis.md:L77] |
| Agentenbasierte Modellierung | ABM | 0.93 | 6 | 3 | 3 | stated in 3 doc(s) ^[emergenz-autonomer-systeme-aegis-forschung.md:L412] ^[aegis-philosophie-und-systemtheorie.md:L80] |
| DDIS | Dissociative Disorders Interview Schedule | 0.92 | 3 | 3 | 3 | stated in 3 doc(s) ^[dis-berichtigung-umfassende-recherche-und-schreiben.md:L81] ^[dis-diagnose-klinische-ethische-rechtliche-analyse.md:L104] |
| K₀ | Collapse Kernel | 0.91 | 26 | 19 | 10 | stated in 3 doc(s) ^[exploring-the-coherence-protocol.md:L169] ^[the-coherence-protocol-a-worldbuilding-bible.md:L27] |
| Ontischer Struktureller Realismus | OSR | 0.91 | 3 | 5 | 3 | stated in 3 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L101] ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L162] |
| Versorgungsmedizinische Grundsätze | VMG | 0.91 | 6 | 7 | 5 | stated in 3 doc(s) ^[dis-berichtigung-umfassende-recherche-und-schreiben.md:L322] ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L246] |
| K1 | Coherence Kernel | 0.90 | 26 | 27 | 12 | stated in 3 doc(s) ^[ki-prompt-analyse-hard-problem-of-consciousness.md:L64] ^[aegis-manifest-genesis-krise-reboot.md:L50] |
| Vertexoperatoralgebra | VOA | 0.90 | 4 | 31 | 3 | stated in 3 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L377] ^[monstergruppe-aegis-und-narrative-moeglichkeiten.md:L108] |
| Multi-Agenten-Systeme | MAS | 0.89 | 7 | 5 | 3 | stated in 3 doc(s) ^[aegis-emergenz-aus-der-leere.md:L94] ^[emergenz-autonomer-systeme-aegis-forschung.md:L223] |
| K₁ | Coherence Kernel | 0.88 | 24 | 27 | 10 | stated in 3 doc(s) ^[exploring-the-coherence-protocol.md:L168] ^[the-coherence-protocol-a-worldbuilding-bible.md:L27] |
| Grenzfeste | KW3 | 0.85 | 32 | 69 | 23 | stated in 3 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L111] ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L283] |
| Anscheinend Normalen Persönlichkeitsanteile | ANPs | 0.84 | 5 | 122 | 5 | stated in 3 doc(s) ^[charaktermodellierung-mit-aieos-schema.md:L43] ^[tattoo-konzept-symbolik-trauma-heilung.md:L82] |
| Konstrukt-Stadt | KW1 | 0.83 | 48 | 81 | 24 | stated in 3 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L66] ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L111] |
| Katastrophales Vergessen | KI | 0.81 | 3 | 167 | 3 | stated in 3 doc(s) ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L310] ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L436] |
| LFIs | Logics of Formal Inconsistency | 0.77 | 7 | 20 | 6 | stated in 3 doc(s) ^[dialetheismus-im-kohaerenz-protokoll.md:L184] ^[parakonsistente-logik-fuer-kohaerenz-protokoll.md:L91] |
| EPs | Emotionalen Anteilen | 0.75 | 142 | 5 | 5 | stated in 3 doc(s) ^[kohaerenz-prozess-grundlagen.md:L33] ^[kohaerenz-protokoll-detaillierte-recherche.md:L197] |
| AGI | Artificial General Intelligence | 0.73 | 5 | 5 | 4 | stated in 3 doc(s) ^[comprehensive-systemic-architectural-and-psychological-conte.md:L91] ^[logik-trifft-transzendente-entitaet.md:L93] |
| Kern-Trauma | T-734 | 0.67 | 11 | 3 | 3 | stated in 3 doc(s) ^[duale-storyform-synthese-kohaerenz-protokoll.md:L83] ^[storyforms-system-mind-bewusstsein.md:L35] |
| Rekursive Konsistenzvalidierung | RCV | 0.67 | 3 | 12 | 3 | stated in 3 doc(s) ^[kohaerenz-protokoll-hard-sf-horror-thriller.md:L111] ^[aegis-philosophische-und-systemtheoretische-analyse-docx.md:L153] |
| Grenzfeste | In KW3 | 0.65 | 32 | 5 | 4 | stated in 3 doc(s) ^[kernwelten-und-fragmentierte-wahrnehmung.md:L384] ^[roman-lokalitaeten-konzept-und-ausarbeitung-2.md:L267] |
| MBO-Ä | Ärztinnen und Ärzte | 0.65 | 3 | 3 | 3 | stated in 3 doc(s) ^[dis-diagnose-klinische-ethische-bewertung.md:L169] ^[dis-diagnose-klinische-ethische-rechtliche-analyse.md:L138] |
| Traumatheorie | TSDP | 0.64 | 11 | 151 | 6 | stated in 3 doc(s) ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L405] ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L485] |
| ZTA | Zero Trust Architecture | 0.64 | 5 | 6 | 5 | stated in 3 doc(s) ^[digitale-uberwelt.md:L49] ^[digitale-uberwelt.md:L49] |
| Widerspruch | LNC | 0.63 | 115 | 3 | 3 | stated in 3 doc(s) ^[monstergruppe-logik-und-metaphern.md:L291] ^[dialetheismus-im-kohaerenz-protokoll.md:L36] |
| Kreativ-Intuitive | Kai | 0.60 | 4 | 10 | 4 | stated in 3 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik.md:L146] ^[kael-charakterarchitektur-und-konfliktdynamik-2.md:L146] |
| Korrektur | K₁ | 0.57 | 40 | 24 | 6 | stated in 3 doc(s) ^[the-architecture-of-being-a-philosophical-thesis-on-the-core.md:L30] ^[a-critical-evaluation-of-the-coherence-protocol-frameworks-s.md:L65] |
| K1 | Coherence | 0.55 | 26 | 119 | 18 | stated in 3 doc(s) ^[kohaerenz-protokoll-architecture-synthesis-2.md:L22] ^[the-architecture-of-fracture-a-compendium-of-the-kael-system.md:L17] |
| Logiken der Formalen Inkonsistenz | LFI | 0.54 | 4 | 25 | 4 | stated in 3 doc(s) ^[kohaerenz-protokoll-analyse-und-synthese.md:L159] ^[kohaerenz-protokoll-detaillierte-recherche.md:L178] |
| Anteilen | EPs | 0.50 | 77 | 142 | 49 | stated in 3 doc(s) ^[2-kohaerenz-protokoll-konzeptentwicklung.md:L74] ^[kohaerenz-protokoll-konzept.md:L152] |
| K₀ | Collapse | 0.43 | 26 | 69 | 19 | stated in 3 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L428] ^[the-coherence-protocol-a-comparative-analysis-across-the-sca.md:L59] |
| Kortex | PFC | 0.33 | 17 | 4 | 4 | stated in 3 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L31] ^[heilung-hirnchemie-kunst-trauma.md:L24] |
| OS | Universe | 0.33 | 43 | 76 | 33 | stated in 3 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L95] ^[duale-storyform-synthese-kohaerenz-protokoll.md:L30] |
| DUT | Dead Universe Theory | 1.00 | 2 | 3 | 2 | stated in 2 doc(s) ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L51] ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L257] |
| EIC | Encrypted Intent Channels | 1.00 | 14 | 11 | 11 | stated in 2 doc(s) ^[briefing-core-concepts-of-the-kohaerenz-protokoll-project.md:L73] ^[digitale-uberwelt-konzept-und-gestaltung.md:L93] |
| EOLSS | OF LIFE SUPPORT SYSTEMS | 1.00 | 3 | 2 | 2 | stated in 2 doc(s) ^[kohaerenz-protokoll-konzeptentwicklung.md:L563] ^[narrative-plot-exploration-existenzielle-kohaerenz.md:L453] |
| Einer Quantenfeldtheorie | QFT | 1.00 | 2 | 5 | 2 | stated in 2 doc(s) ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L52] ^[holographisches-prinzip-fuer-kohaerenz-protokoll-2.md:L52] |
| LCA | Logical Consistency Analysis | 1.00 | 4 | 2 | 2 | stated in 2 doc(s) ^[nichts-ordnung-fragmentierung-resonanz-nebel.md:L39] ^[romananfang-leere-und-systemgenesis.md:L182] |
| TSDP | Structural Dissociation | 1.00 | 151 | 97 | 88 | stated in 2 doc(s) ^[kohaerenz-protokoll-synthese.md:L299] ^[systemic-warfare-a-strategic-guide-to-dramatizing-the-psycho.md:L15] |
| USC | University of Southern California | 1.00 | 2 | 2 | 2 | stated in 2 doc(s) ^[aieos-schema-fuer-ki-charaktere.md:L579] ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L158] |
| AIRM | Attachment Injury Resolution Model | 0.99 | 2 | 2 | 2 | stated in 2 doc(s) ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L134] ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L348] |
| BDI | Belief-Desire-Intention | 0.99 | 2 | 2 | 2 | stated in 2 doc(s) ^[dramatica-agentic-storyform-interactive-novel.md:L80] ^[the-kohaerenz-protokoll-an-isomorphic-architecture-for-agent.md:L42] |
| CoLT | Computational Learning Theory | 0.99 | 2 | 2 | 2 | stated in 2 doc(s) ^[logik-trifft-transzendente-entitaet.md:L93] ^[logik-trifft-transzendente-entitaet-2.md:L93] |
| Datenschutz-Grundverordnung | DSGVO | 0.99 | 2 | 2 | 2 | stated in 2 doc(s) ^[dis-berichtigung-umfassende-recherche-und-schreiben.md:L147] ^[rechtliche-analyse-entlassungsbericht-und-dis.md:L32] |
| EMDR | Movement Desensitization and Reprocessing | 0.99 | 32 | 3 | 3 | stated in 2 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L185] ^[dissoziative-identitaet-invalidierung-im-gesundheitssystem.md:L226]; proposed |
| HS | Higman-Sims | 0.99 | 3 | 3 | 3 | stated in 2 doc(s) ^[monstergruppe-logik-und-metaphern.md:L63] ^[monstergruppe-narrative-cluster-und-metaphern.md:L170] |
| IC | Influence Character | 0.99 | 39 | 20 | 18 | stated in 2 doc(s) ^[duale-storyform-synthese-kohaerenz-protokoll.md:L69] ^[duale-storyform-synthese-kohaerenz-protokoll.md:L119] |
| IFS | Internal Family Systems Model | 0.99 | 68 | 10 | 10 | stated in 2 doc(s) ^[optimierter-prompt-fuer-kohaerenz-protokoll.md:L288] ^[kernwelten-fuer-kohaerenz-protokoll.md:L581] |
| Logische Konsistenzanalyse | LCA | 0.99 | 2 | 4 | 2 | stated in 2 doc(s) ^[recherche-ueberwelt.md:L47] ^[ergaenze-aegis-protokoll-und-selbstrekusive-defini.md:L81] |
| MOCs | Maps of Content | 0.99 | 2 | 3 | 2 | stated in 2 doc(s) ^[ki-agenten-kohaerenz-und-prompt-generierung.md:L137] ^[ki-agenten-kohaerenz-und-prompt-generierung.md:L334] |
| Memory-as-Action | MemAct | 0.99 | 5 | 5 | 5 | stated in 2 doc(s) ^[aegis-genesis-crisis-self-definition.md:L171] ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:L43] |
| Sozialgesetzbuch Neuntes Buch | SGB IX | 0.99 | 2 | 9 | 2 | stated in 2 doc(s) ^[rechtliche-analyse-entlassungsbericht-und-dis.md:L29] ^[rechtliche-analyse-entlassungsbericht-und-dis.md:L403] |
| TREs | Transformative Relationship Events | 0.99 | 2 | 2 | 2 | stated in 2 doc(s) ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L267] ^[beziehungsheilung-nach-trauma-konzeptpapier-3.md:L273] |
| Allgemeiner Relativitätstheorie | ART | 0.98 | 3 | 5 | 2 | stated in 2 doc(s) ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L35] ^[holographisches-prinzip-fuer-kohaerenz-protokoll-2.md:L35] |
| Wissenschaftlichen Medizinischen Fachgesellschaften | AWMF | 0.98 | 3 | 11 | 3 | stated in 2 doc(s) ^[dissoziative-identitaet-invalidierung-im-gesundheitssystem.md:L224] ^[gutachten-grad-der-behinderung-bei-dis.md:L41] |
| Analyse des Holographischen Prinzips | HP | 0.98 | 2 | 4 | 2 | stated in 2 doc(s) ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L15] ^[holographisches-prinzip-fuer-kohaerenz-protokoll-2.md:L15] |
| Bürgerlichen Gesetzbuch | BGB | 0.98 | 2 | 7 | 2 | stated in 2 doc(s) ^[dis-berichtigung-umfassende-recherche-und-schreiben.md:L133] ^[dis-diagnose-klinische-ethische-bewertung.md:L182] |
| Dysregulation der Hypothalamus-Hypophysen-Nebennierenrinden-Achse | HPA-Achse | 0.98 | 2 | 4 | 2 | stated in 2 doc(s) ^[dissoziative-identitaetsstoerung-unsichtbare-diagnose.md:L103] ^[flow-zustaende-und-dissoziative-identitaet.md:L110] |
| FDE | First Degree Entailment | 0.98 | 7 | 6 | 5 | stated in 2 doc(s) ^[parakonsistente-logik-fuer-kohaerenz-protokoll.md:L278] ^[parakonsistenz-aegis-und-nicht-existenz.md:L203] |
| Holographisches Prinzip | HP | 0.98 | 12 | 4 | 2 | stated in 2 doc(s) ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L188] ^[holographisches-prinzip-fuer-kohaerenz-protokoll-2.md:L188] |
| ISH | Inner Self Helper | 0.98 | 24 | 6 | 5 | stated in 2 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L537] ^[hard-sf-roman-outline-dkt-physik-cosmic-horror.md:L54] |
| IoT | Internet of Things | 0.98 | 4 | 3 | 2 | stated in 2 doc(s) ^[p-vs-np-und-kohaerenz.md:L498] ^[emergenz-aegis-und-selbststrukturierung.md:L103] |
| PE | Prolonged Exposure Therapy | 0.98 | 2 | 2 | 2 | stated in 2 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L1529] ^[prosaversion-von-genesis-erstellen.md:L354] |
| BDNF | Brain-Derived Neurotrophic Factor | 0.97 | 3 | 2 | 2 | stated in 2 doc(s) ^[heilung-hirnchemie-kunst-trauma.md:L54] ^[heilung-hirnchemie-kunst-trauma.md:L210] |
| Gedächtnisdiagnostik | IGD | 0.97 | 2 | 2 | 2 | stated in 2 doc(s) ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L677] ^[aegis-genesis-krise-prosa-auftrag-formulieren-2.md:L760] |
| Holographie und Quanteninformationstheorie | QIT | 0.97 | 2 | 2 | 2 | stated in 2 doc(s) ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L71] ^[holographisches-prinzip-fuer-kohaerenz-protokoll-2.md:L71] |
| Komplexes Trauma | K-PTBS | 0.97 | 9 | 2 | 2 | stated in 2 doc(s) ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L31] ^[beziehungsheilung-nach-trauma-konzeptpapier-3.md:L31] |
| SAND | Science and Nonduality | 0.97 | 2 | 2 | 2 | stated in 2 doc(s) ^[kohaerenz-protokoll-transzendenz-vektoren.md:L359] ^[hard-sci-fi-cosmic-horror-research-questions.md:L315] |
| GUT | Großen Vereinheitlichten Theorie | 0.96 | 3 | 2 | 2 | stated in 2 doc(s) ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L114] ^[realitaet-symmetrie-und-bewusstsein-monstergruppe.md:L252] |
| K-J | Kael-Juna | 0.96 | 34 | 25 | 6 | stated in 2 doc(s) ^[konzeptanalyse-kohaerenz-protokoll-s-fundament.md:L15] ^[konzeptanalyse-kohaerenz-protokoll-s-fundament.md:L97] |
| Suz | Suzuki | 0.96 | 3 | 3 | 3 | stated in 2 doc(s) ^[monstergruppe-logik-und-metaphern.md:L63] ^[monstergruppe-narrative-cluster-und-metaphern.md:L170] |
| Traumasensible Paartherapie | TSPT | 0.96 | 2 | 2 | 2 | stated in 2 doc(s) ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L128] ^[beziehungsheilung-nach-trauma-konzeptpapier-3.md:L132] |
| VOA | Vertex Operator Algebras | 0.96 | 31 | 5 | 4 | stated in 2 doc(s) ^[kohaerenz-protokoll-architecture-synthesis.md:L165] ^[kohaerenz-protokoll-synthese.md:L31] |
| Giulio Tononis Integrierte Informationstheorie | IIT | 0.95 | 1 | 29 | 1 | stated in 2 doc(s) ^[kohaerenz-protokoll-analyse-und-synthese.md:L279] ^[aegis-logik-und-narrative-implikationen.md:L168] |
| PTG | Post Traumatic Growth | 0.95 | 5 | 2 | 2 | stated in 2 doc(s) ^[genesis-mehrstufige-recherche-und-ausformulierung.md:L685] ^[prosaversion-von-genesis-erstellen.md:L354] |
| Anscheinend Normaler Persönlichkeitsanteil | ANP | 0.94 | 8 | 145 | 8 | stated in 2 doc(s) ^[roman-konzept-dualitaet-kohaerenz-spannung.md:L25] ^[ki-antagonist-fragmentierte-gottheit-analyse.md:L74] |
| Monster-Vertex-Operator-Algebra | VOA | 0.94 | 2 | 31 | 2 | stated in 2 doc(s) ^[monstergruppe-kohaerenz-protokoll-fundament.md:L78] ^[monstergruppe-narrative-cluster-und-metaphern.md:L59] |
| Large Language Models | LLMs | 0.93 | 21 | 26 | 15 | stated in 2 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L70] ^[konzept-expose-schwarzschild-protokoll-optimierung.md:L352] |
| OS | Overall Story | 0.93 | 43 | 13 | 13 | stated in 2 doc(s) ^[duale-storyform-synthese-kohaerenz-protokoll.md:L70] ^[duale-storyform-synthese-kohaerenz-protokoll.md:L120] |
| Rechtsprechung des Bundessozialgerichts | BSG | 0.92 | 3 | 5 | 3 | stated in 2 doc(s) ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L99] ^[sozialrechtliche-strategien-bei-traumafolgestoerungen.md:L158] |
| Behinderung und Gesundheit | ICF | 0.92 | 2 | 3 | 2 | stated in 2 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L17] ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L35] |
| Untersuchung Schwarzer Löcher | SL | 0.92 | 2 | 5 | 2 | stated in 2 doc(s) ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L35] ^[holographisches-prinzip-fuer-kohaerenz-protokoll-2.md:L35] |
| In Multi-Agenten-Systemen | MAS | 0.91 | 2 | 5 | 2 | stated in 2 doc(s) ^[digitale-uberwelt.md:L85] ^[aegis-philosophie-und-systemtheorie.md:L80] |
| Zero-Trust-Architektur | ZTA | 0.91 | 4 | 5 | 2 | stated in 2 doc(s) ^[aegis-emergenz-aus-der-leere.md:L67] ^[aegis-philosophische-und-systemtheoretische-analyse-docx.md:L113] |
| Anti-de-Sitter-Raum | AdS | 0.89 | 5 | 8 | 4 | stated in 2 doc(s) ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L51] ^[holographisches-prinzip-fuer-kohaerenz-protokoll-2.md:L51] |
| EFT | Emotionally Focused Couples Therapy | 0.88 | 2 | 2 | 2 | stated in 2 doc(s) ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L348] ^[beziehungsheilung-nach-trauma-konzeptpapier-3.md:L402] |
| Neuntes Buch | SGB IX | 0.87 | 3 | 9 | 3 | stated in 2 doc(s) ^[rechtliche-analyse-entlassungsbericht-und-dis.md:L459] ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L546] |
| Versorgungsmedizinischen Grundsätze | VMG | 0.87 | 5 | 7 | 3 | stated in 2 doc(s) ^[dissoziative-identitaetsstoerung-unsichtbare-diagnose.md:L139] ^[juristische-recherche-zu-kptbs-dis.md:L281] |
| Kaels Dissoziative Identitätsstörung | DID | 0.86 | 2 | 100 | 1 | stated in 2 doc(s) ^[kohaerenz-protokoll-aktuelle-gesamtkonzept-synthese.md:L37] ^[kohaerenzprotokoll-aegis-und-systementropie.md:L41] |
| Diagnose Dissoziative Identitätsstörung | DIS | 0.86 | 2 | 53 | 2 | stated in 2 doc(s) ^[dis-diagnose-klinische-ethische-bewertung.md:L11] ^[dis-diagnose-klinische-ethische-bewertung.md:L15] |
| Vertexoperatoralgebren | VOA | 0.86 | 3 | 31 | 3 | stated in 2 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L107] ^[kohaerenz-protokoll-audit-und-verifizierung.md:L109] |
| ITQ | International Trauma Questionnaire | 0.85 | 2 | 2 | 2 | stated in 2 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L103] ^[sozialrechtliche-strategien-bei-traumafolgestoerungen.md:L235] |
| Dissoziativen Symptomen | FDS | 0.84 | 2 | 6 | 2 | stated in 2 doc(s) ^[dissoziative-identitaetsstoerung-unsichtbare-diagnose.md:L43] ^[sozialrechtliche-strategien-bei-traumafolgestoerungen.md:L75] |
| RTSV | Real-time Self-Verification | 0.84 | 14 | 7 | 5 | stated in 2 doc(s) ^[briefing-core-concepts-of-the-kohaerenz-protokoll-project.md:L71] ^[digitale-uberwelt-konzept-und-gestaltung.md:L96] |
| Künstlicher Intelligenz | KI | 0.81 | 8 | 167 | 8 | stated in 2 doc(s) ^[codex-optimierung-fuer-kohaerenz-protokoll.md:L15] ^[kohaerenz-protokoll-system-realitaet-leser.md:L13] |
| Prinzip der Explosion | ECQ | 0.80 | 25 | 9 | 5 | stated in 2 doc(s) ^[monstergruppe-logik-und-metaphern.md:L268] ^[monstergruppe-logik-und-metaphern.md:L290] |
| Kollaps | K₀ | 0.80 | 149 | 26 | 12 | stated in 2 doc(s) ^[projektplanung-fuer-kohaerenz-protokoll.md:L29] ^[protokoll-ontologie-roman-konzeptentwicklung.md:L38] |
| Emotionsfokussierte Paartherapie | EFT | 0.79 | 2 | 2 | 2 | stated in 2 doc(s) ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L128] ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L134] |
| Vertex-Operator-Algebren | VOAs | 0.77 | 13 | 13 | 6 | stated in 2 doc(s) ^[m-als-fundament-der-simulation.md:L38] ^[monstergruppe-kohaerenz-protokoll-fundament.md:L104] |
| Kernwelten | KW1-KW4 | 0.74 | 134 | 4 | 3 | stated in 2 doc(s) ^[charaktere.md:L116] ^[kohaerenz-protokoll-projekt-rekonstruktion.md:L282] |
| Theorembeweiser | ATP | 0.73 | 2 | 3 | 2 | stated in 2 doc(s) ^[logik-trifft-transzendente-entitaet.md:L196] ^[logik-trifft-transzendente-entitaet-2.md:L194] |
| Diskursive Logik | D2 | 0.72 | 3 | 10 | 2 | stated in 2 doc(s) ^[kohaerenz-protokoll-analyse-und-synthese.md:L158] ^[kohaerenz-protokoll-detaillierte-recherche.md:L177] |
| RCI-Modell | Spezifische Beziehungsarchetypen | 0.72 | 2 | 2 | 2 | stated in 2 doc(s) ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L252] ^[beziehungsheilung-nach-trauma-konzeptpapier-3.md:L258] |
| CoDA | Codependents Anonymous | 0.70 | 2 | 2 | 2 | stated in 2 doc(s) ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L99] ^[beziehungsheilung-nach-trauma-konzeptpapier-3.md:L101] |
| ZKPs | Zero-Knowledge Proofs | 0.70 | 3 | 4 | 3 | stated in 2 doc(s) ^[global-research-for-kohaerenz-protokoll.md:L83] ^[dramatica-storyform-synthese-aegis-verortung.md:L61] |
| Lyons-Welt | Ly | 0.68 | 3 | 22 | 2 | stated in 2 doc(s) ^[kohaerenz-protokoll.md:L1966] ^[kohaerenz-protokoll.md:L1978] |
| DE | DRV | 0.67 | 17 | 5 | 5 | stated in 2 doc(s) ^[dissoziative-identitaetsstoerung-unsichtbare-diagnose.md:L268] ^[dissoziative-identitaetsstoerung-unsichtbare-diagnose.md:L324] |
| Umgebung | EST | 0.67 | 144 | 12 | 6 | stated in 2 doc(s) ^[p-vs-np-und-kohaerenz.md:L236] ^[p-vs-np-und-kohaerenz.md:L241] |
| Innere Helferin | ISH | 0.66 | 3 | 24 | 3 | stated in 2 doc(s) ^[kohaerenz-protokoll-forschungsaufgabe.md:L138] ^[charaktere.md:L274] |
| K0 | Collapse Kernel | 0.65 | 26 | 19 | 7 | stated in 2 doc(s) ^[aegis-manifest-genesis-krise-reboot.md:L51] ^[aegis-manifest-genesis-krise-reboot-2.md:L83] |
| DEM | Machina | 0.60 | 3 | 47 | 3 | stated in 2 doc(s) ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L251] ^[managing-ontological-risk-defining-the-narrative-integration.md:L15] |
| Emotionalen Teils | EP | 0.60 | 2 | 140 | 2 | stated in 2 doc(s) ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:L312] ^[konzeptionelle-transzendenz-fuer-kohaerenz-protokoll.md:L371] |
| Prinzip | HP | 0.60 | 173 | 4 | 4 | stated in 2 doc(s) ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L70] ^[holographisches-prinzip-fuer-kohaerenz-protokoll-2.md:L70] |
| Kohärenz-Kernel | K1 | 0.60 | 22 | 26 | 9 | stated in 2 doc(s) ^[editorial-style-dossier-somatic-and-linguistic-implementatio.md:L15] ^[roman-konzept-dualitaet-kohaerenz-spannung.md:L45] |
| MUH | Max Tegmarks Mathematischem Universum | 0.60 | 6 | 2 | 2 | stated in 2 doc(s) ^[aegis-logik-in-der-leere-docx.md:L21] ^[konzeptionelle-transzendenz-fuer-kohaerenz-protokoll.md:L50] |
| GWPs | Global Work Packages | 0.58 | 2 | 2 | 2 | stated in 2 doc(s) ^[global-research-for-kohaerenz-protokoll.md:L153] ^[dramatica-storyform-synthese-aegis-verortung.md:L195] |
| Kohärenz | K₁ | 0.56 | 295 | 24 | 16 | stated in 2 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L82] ^[kohaerenz-protokoll-architecture-synthesis.md:L131] |
| RTSV | Real-Time Self-Verification | 0.56 | 14 | 2 | 2 | stated in 2 doc(s) ^[aegis-manifest-genesis-krise-reboot-2.md:L103] ^[aegis-genesis-crisis-self-definition.md:L49] |
| Selbstmodell | PSM | 0.54 | 10 | 9 | 7 | stated in 2 doc(s) ^[dramatica-dual-storyform-mapping-protokoll.md:L44] ^[roman-entwicklung-ontologie-trauma-horror.md:L23] |
| Kaels Initiale Wohneinheit | KW1 | 0.53 | 3 | 81 | 3 | stated in 2 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung-2.md:L216] ^[roman-lokalitaeten-konzept-und-ausarbeitung-3.md:L217] |
| Virtuelle Realitäten | VR | 0.53 | 3 | 11 | 2 | stated in 2 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung-2.md:L41] ^[roman-lokalitaeten-konzept-und-ausarbeitung-3.md:L41] |
| CFSG | Gruppen | 0.52 | 2 | 35 | 2 | stated in 2 doc(s) ^[monstergruppe-als-denkmodell-der-komplexitaet.md:L43] ^[monstergruppe-logik-und-metaphern.md:L15] |
| V-Anomalie | Juna | 0.50 | 2 | 192 | 2 | stated in 2 doc(s) ^[optimierter-prompt-fuer-kohaerenz-protokoll.md:L42] ^[optimierter-prompt-fuer-kohaerenz-protokoll.md:L52] |
| Herzstück der Grenzfeste | KW3 | 0.49 | 2 | 69 | 2 | stated in 2 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung-2.md:L232] ^[roman-lokalitaeten-konzept-und-ausarbeitung-3.md:L233] |
| Versorgungsmedizinischen Grundsätzen | VMG | 0.49 | 5 | 7 | 4 | stated in 2 doc(s) ^[juristische-recherche-zu-kptbs-dis.md:L242] ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L374] |
| Strenge der Dual-Kernel-Theorie | DKT | 0.46 | 2 | 60 | 2 | stated in 2 doc(s) ^[ki-narrative-kollaps-kohaerenz-paradoxie.md:L19] ^[aegis-und-der-kollaps-kritische-analyse.md:L17] |
| IDEAS | RePEc | 0.45 | 2 | 2 | 2 | stated in 2 doc(s) ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L281] ^[aegis-subplots-kapitelweise-system-exploration-docx.md:L553] |
| Persönlichkeitsanteile | EPs | 0.37 | 53 | 142 | 34 | stated in 2 doc(s) ^[storyforms-system-mind-bewusstsein.md:L30] ^[dis-diagnose-klinische-ethische-bewertung.md:L86] |
| Ambulant Betreute Wohnen | ABW | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L119] |
| Ambulant Betreutes Wohnen | ABW | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L117] |
| Ambulante Psychiatrische Pflege | APP | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L176] ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L184] |
| Persönlichkeitsrecht | APR | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[rechtliche-analyse-entlassungsbericht-und-dis.md:L304] |
| Autopoietische Reentry-Segmentierung | ARS | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L70] |
| ASP | Answer Set Programming | 1.00 | 2 | 1 | 1 | stated in 1 doc(s) ^[konzept-expose-schwarzschild-protokoll-optimierung.md:L24] ^[konzept-expose-schwarzschild-protokoll-optimierung.md:L360] |
| Arbeitsunfähigkeit | AU | 1.00 | 4 | 1 | 1 | stated in 1 doc(s) ^[juristische-recherche-zu-kptbs-dis.md:L670] |
| BGH | Bundesgerichtshof | 1.00 | 3 | 1 | 1 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L172] |
| BSG | Bundessozialgericht | 1.00 | 5 | 3 | 3 | stated in 1 doc(s) ^[juristische-recherche-zu-kptbs-dis.md:L44] |
| BusRd | Bus Read | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L115] |
| C-PTSD | Complex PTSD | 1.00 | 7 | 11 | 3 | stated in 1 doc(s) ^[trauma-archaeologie-interdisziplinaere-konzeptentwicklung-do.md:L321]; proposed |
| C2 | Command and Control | 1.00 | 11 | 2 | 1 | stated in 1 doc(s) ^[aegis-subplots-kapitelweise-system-exploration-docx.md:L209] ^[aegis-subplots-kapitelweise-system-exploration-docx.md:L213] |
| CNM | Consensual Non-Monogamy | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[comprehensive-systemic-architectural-and-psychological-conte.md:L47]; proposed |
| CPTSD | Complex Post-Traumatic Stress Disorder | 1.00 | 9 | 3 | 3 | stated in 1 doc(s) ^[comprehensive-systemic-architectural-and-psychological-conte.md:L19] |
| CSI | Collapse Susceptibility Index | 1.00 | 5 | 4 | 4 | stated in 1 doc(s) ^[dkt-fundament-kohaerenz-protokoll-md.md:L110] |
| CWH | Corrective Wavelet Hypothesis | 1.00 | 1 | 2 | 1 | stated in 1 doc(s) ^[a-critical-evaluation-of-the-coherence-protocol-frameworks-s.md:L21] |
| Dissoziations-Fremdbeurteilungs-Liste | DiFL | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[dis-berichtigung-umfassende-recherche-und-schreiben.md:L269] |
| EDA | Event-Driven Architecture | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[comprehensive-systemic-architectural-and-psychological-conte.md:L109] |
| EStG | Einkommensteuergesetz | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[sozialrechtliche-strategien-bei-traumafolgestoerungen.md:L172] |
| ETC | Entertainment Technology Center | 1.00 | 1 | 2 | 1 | stated in 1 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L158] |
| Elektronische Musik und Akustik | IEM | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-singularitaet-jenseits-entropiegleichung-2.md:L533] |
| Entsprechender Grad der Behinderung | GdB | 1.00 | 1 | 11 | 1 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L107] |
| Exiting Secure Isolation State | SIS | 1.00 | 1 | 15 | 1 | stated in 1 doc(s) ^[romananfang-leere-und-systemgenesis.md:L218] |
| IFS | Exploring Internal Family Systems | 1.00 | 68 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-detaillierte-recherche.md:L406] |
| Flexible Assertive Community Treatment | FACT | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[juristische-recherche-zu-kptbs-dis.md:L713] |
| FEPS | Free Energy Projective Simulation | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-protokolle-kritische-evaluation-neukonzeption.md:L209] |
| Grundgesetz | GG | 1.00 | 4 | 2 | 1 | stated in 1 doc(s) ^[rechtliche-analyse-entlassungsbericht-und-dis.md:L31] |
| Grenz-Integritäts-Feld | GIF | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[logiksystem-aegis-entwicklungsszenarien-docx.md:L101] ^[logiksystem-aegis-entwicklungsszenarien-docx.md:L206] |
| Grad der Behinderung | GdB | 1.00 | 9 | 11 | 9 | stated in 1 doc(s) ^[dissoziative-identitaetsstoerung-unsichtbare-diagnose.md:L125] |
| Grad der Schädigungsfolgen | GdS | 1.00 | 1 | 4 | 1 | stated in 1 doc(s) ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L117] |
| Grenzziehung Fichtes Tathandlung | TF-1 | 1.00 | 0 | 1 | 0 | stated in 1 doc(s) ^[roman-entwicklung-ontologie-trauma-horror.md:L138] |
| HOT | Higher-Order Theories | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L79] ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L277] |
| HOT | Higher-Order Theory of Consciousness | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L73] |
| RLHF | Human Feedback | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[ki-narrative-kollaps-kohaerenz-paradoxie.md:L41] |
| IAS | Institute of Advanced Studies | 1.00 | 2 | 1 | 1 | stated in 1 doc(s) ^[global-research-for-kohaerenz-protokoll.md:L200] |
| IQG | Informational Quantum Gravity | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[konzeptionelle-transzendenz-fuer-kohaerenz-protokoll.md:L50] ^[konzeptionelle-transzendenz-fuer-kohaerenz-protokoll.md:L461] |
| ISA | Integrated Sensor Architecture | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[umfassendes-lokalitaeten-konzept-fuer-roman.md:L739] |
| In Quantum Resource Theories | QRT | 1.00 | 0 | 2 | 0 | stated in 1 doc(s) ^[the-coherence-protocol-the-hidden-rules-that-hold-reality-to.md:L35] |
| SIS | Initiating Secure Isolation State | 1.00 | 15 | 1 | 1 | stated in 1 doc(s) ^[romananfang-leere-und-systemgenesis.md:L196] |
| Kassenärztliche Bundesvereinigung | KBV | 1.00 | 2 | 1 | 1 | stated in 1 doc(s) ^[rechtliche-analyse-entlassungsbericht-und-dis.md:L440] |
| Kohärenz-Resonanz-Monitor | KRM | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[logiksystem-aegis-entwicklungsszenarien-docx.md:L117] ^[logiksystem-aegis-entwicklungsszenarien-docx.md:L220] |
| Kernwelt | KW | 1.00 | 73 | 12 | 8 | stated in 1 doc(s) ^[hard-sf-roman-outline-dkt-physik-cosmic-horror.md:L39] |
| LVC | Live Virtual Constructive | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[umfassendes-lokalitaeten-konzept-fuer-roman.md:L739] |
| MoCs | Maps of Content | 1.00 | 1 | 3 | 1 | stated in 1 doc(s) ^[ki-agenten-kohaerenz-und-prompt-generierung.md:L357] |
| McL | McLaughlin | 1.00 | 22 | 7 | 7 | stated in 1 doc(s) ^[kohaerenz-protokoll-umfassendes-konzept.md:L30] |
| OST | Objective Story Throughline | 1.00 | 1 | 7 | 1 | stated in 1 doc(s) ^[fragen-zu-existenz-agency-und-realitaet.md:L175] |
| Phänotyp-Kohärenz-Protokolle | PKP | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L24] |
| PP | Predictive Processing | 1.00 | 10 | 3 | 1 | stated in 1 doc(s) ^[aegis-analyse-und-manifest-postulation.md:L132] ^[aegis-analyse-und-manifest-postulation.md:L260] |
| PTK NRW | Psychotherapeutenkammer NRW | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[gutachterprofil-und-alternativen-ptbs-dis.md:L110] |
| RSD | Rejection Sensitive Dysphoria | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[comprehensive-systemic-architectural-and-psychological-conte.md:L21] |
| SBA | Schwerbehindertenausweis | 1.00 | 1 | 5 | 1 | stated in 1 doc(s) ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L178] |
| Sozialgesetzbuch | SGB | 1.00 | 5 | 11 | 5 | stated in 1 doc(s) ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L544] ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L545] |
| Störung der Intelligenzentwicklung | SIE | 1.00 | 1 | 4 | 1 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L234] |
| Strukturierte Nicht-Kontrolle | SNK | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L90] |
| Thompson-Gruppe | Th | 1.00 | 5 | 4 | 4 | stated in 1 doc(s) ^[monstergruppe-logik-und-metaphern.md:L64] |
| Theorie der Vertex-Operator-Algebren | VOAs | 1.00 | 1 | 13 | 1 | stated in 1 doc(s) ^[monstergruppe-als-narrative-inspiration.md:L88] |
| Theorie der Vertexoperatoralgebren | VOA | 1.00 | 1 | 31 | 1 | stated in 1 doc(s) ^[monstergruppe-als-denkmodell-der-komplexitaet.md:L129] |
| ToM | Theory of Mind | 1.00 | 3 | 9 | 3 | stated in 1 doc(s) ^[aegis-paradoxon-konzeption-und-analyse.md:L52] |
| Vertrauenlose Validierung | ZTV | 1.00 | 1 | 2 | 1 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L211] |
| WAP | Weak Anthropic Principle | 1.00 | 1 | 3 | 1 | stated in 1 doc(s) ^[exploring-the-coherence-protocol.md:L238] |
| WSNs | Wireless Sensor Networks | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[p-vs-np-und-kohaerenz.md:L498] |
| Zelluläre Automaten | ZA | 1.00 | 4 | 1 | 1 | stated in 1 doc(s) ^[kernwelten-fuer-kohaerenz-protokoll.md:L101] |
| ÄkNo | Ärztekammer Nordrhein | 1.00 | 1 | 2 | 1 | stated in 1 doc(s) ^[gutachterprofil-und-alternativen-ptbs-dis.md:L95] |
| ÄkWL | Ärztekammer Westfalen-Lippe | 1.00 | 1 | 1 | 1 | stated in 1 doc(s) ^[gutachterprofil-und-alternativen-ptbs-dis.md:L96] |
| Agentenbasierte Simulation | ABS | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[emergenz-aegis-und-selbststrukturierung.md:L366] |
| AIEOS | AI Entity Object Specification | 0.99 | 2 | 2 | 2 | stated in 1 doc(s) ^[aieos-schema-fuer-ki-charaktere.md:L19] |
| ASDLS | System Design Language Specification | 0.99 | 5 | 5 | 5 | stated in 1 doc(s) ^[roman-assistenz-kohaerenz-und-weltgestaltung.md:L15] |
| PMAS | Adaptive Strategy Protocol | 0.99 | 10 | 1 | 1 | stated in 1 doc(s) ^[aegis.md:L104] |
| Auch die Dissoziative Identitätsstörung | DIS | 0.99 | 1 | 53 | 1 | stated in 1 doc(s) ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L168] |
| BBT | Blind Brain Theory | 0.99 | 2 | 2 | 2 | stated in 1 doc(s) ^[roman-entwicklung-ontologie-trauma-horror.md:L112] |
| Bürgerliches Gesetzbuch | BGB | 0.99 | 1 | 7 | 1 | stated in 1 doc(s) ^[rechtliche-analyse-entlassungsbericht-und-dis.md:L15] ^[rechtliche-analyse-entlassungsbericht-und-dis.md:L27] |
| BPoF | Behavioral Proof-of-Function | 0.99 | 16 | 12 | 12 | stated in 1 doc(s) ^[briefing-core-concepts-of-the-kohaerenz-protokoll-project.md:L72] |
| BTZ | Bañados-Teitelboim-Zanelli | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[monstergruppe-kohaerenz-protokoll-fundament.md:L143] |
| CAPS-5 | Clinician-Administered PTSD Scale16 | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[neurochemische-lyrik-transzendenz-durch-klang.md:L194] |
| CBT | Cognitive-Behavioral Therapy | 0.99 | 7 | 1 | 1 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L267]; proposed |
| CRS | Consistency Risk Score | 0.99 | 1 | 2 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L210] ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L219] |
| Dopamin | DA | 0.99 | 6 | 3 | 1 | stated in 1 doc(s) ^[heilung-hirnchemie-kunst-trauma.md:L118] |
| Entropische Kohärenzregulation | ECR | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L56] |
| ES | Environmental Storytelling | 0.99 | 1 | 33 | 1 | stated in 1 doc(s) ^[monstergruppe-narrative-cluster-und-metaphern.md:L304] |
| GIM | Guided Imagery and Music | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L266] |
| GNW | Global Neuronal Workspace | 0.99 | 2 | 4 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-inkubation-x.md:L172]; proposed |
| HR | Herzfrequenz | 0.99 | 3 | 4 | 1 | stated in 1 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L1097] |
| IWMT | Integrated World Modeling Theory | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L491] |
| NIMH | Institute of Mental Health | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[trauma-archaeologie-interdisziplinaere-konzeptentwicklung-do.md:L335] |
| Kern-Identitäts-Nexus | KIN | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[logiksystem-aegis-entwicklungsszenarien-docx.md:L93] ^[logiksystem-aegis-entwicklungsszenarien-docx.md:L198] |
| Komplexe Posttraumatische Belastungsstörung | KPTBS | 0.99 | 6 | 2 | 1 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L21] ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L194] |
| Kernwelten | KWs | 0.99 | 134 | 9 | 3 | stated in 1 doc(s) ^[kohaerenz-protokoll-plot-entwicklung-und-wahrheitsdualitaet.md:L235] |
| Konzepte des Monstrous Moonshine | MM | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[monstergruppe-kohaerenz-protokoll-fundament.md:L15] |
| Korrelaten des Bewusstseins | NCC | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[existenzforschung-fuer-roman-kohaerenz-protokoll.md:L248] |
| Kosten der AEGIS-Verifikation | RCV | 0.99 | 1 | 12 | 1 | stated in 1 doc(s) ^[aegis-analyse-und-manifest-postulation.md:L259] |
| LSG | Landessozialgerichten | 0.99 | 6 | 1 | 1 | stated in 1 doc(s) ^[sozialrechtliche-strategien-bei-traumafolgestoerungen.md:L392] |
| Myers-Briggs-Typenindikator | MBTI | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[charaktermodellierung-mit-aieos-schema.md:L45] |
| MI | Mutuale Information | 0.99 | 10 | 3 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L46] |
| Noradrenalin | NA | 0.99 | 4 | 1 | 1 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L64] |
| NLCA | Natural Language Cognitive Architecture | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[comprehensive-systemic-architectural-and-psychological-conte.md:L89] ^[comprehensive-systemic-architectural-and-psychological-conte.md:L91] |
| NLP | Natural Language Processing | 0.99 | 2 | 3 | 1 | stated in 1 doc(s) ^[emergenz-aegis-und-selbststrukturierung.md:L175] |
| NovelOS | Universal Novel Operating System | 0.99 | 5 | 1 | 1 | stated in 1 doc(s) ^[comprehensive-systemic-architectural-and-psychological-conte.md:L61] ^[comprehensive-systemic-architectural-and-psychological-conte.md:L63] |
| Opferentschädigungsgesetz | OEG | 0.99 | 2 | 2 | 2 | stated in 1 doc(s) ^[rechtliche-analyse-entlassungsbericht-und-dis.md:L278] |
| Protomemetische Speicherbildung | PMS | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L77] |
| Prädiktive Simulations-Engine | PSE | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[logiksystem-aegis-entwicklungsszenarien-docx.md:L109] ^[logiksystem-aegis-entwicklungsszenarien-docx.md:L214] |
| Quantenvakuumfeld | QVF | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L168] ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L347] |
| RS | RELATION | 0.99 | 23 | 1 | 1 | stated in 1 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L377] |
| RFT | Resonance Field Theory | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[narrativ-existenzieller-kohaerenz-nzt-protokoll.md:L359] |
| RPKI | Resource Public Key Infrastructure | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[digitale-uberwelt.md:L149] ^[digitale-uberwelt.md:L193] |
| RTC | Recurse Theory of Consciousness | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-philosophische-und-systemtheoretische-analyse-docx.md:L297] |
| Ru | Rudvalis | 0.99 | 4 | 4 | 4 | stated in 1 doc(s) ^[monstergruppe-narrative-cluster-und-metaphern.md:L195] |
| Sozialgesetzbuch IX | SGB IX | 0.99 | 1 | 9 | 1 | stated in 1 doc(s) ^[dis-diagnose-klinische-ethische-rechtliche-analyse.md:L202] |
| SGP | Symbol Grounding Problem | 0.99 | 1 | 2 | 1 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L53] ^[aegis-emergenz-aus-der-leere.md:L225] |
| Spontane Symmetriebrechung | SSB | 0.99 | 2 | 3 | 1 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L35] |
| Schematherapie | ST | 0.99 | 2 | 3 | 2 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L165] |
| TGF | Thermodynamic Graph Fields | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[dkt-fundament-kohaerenz-protokoll-md.md:L151] |
| Tertiäre Strukturelle Dissoziation | TSD | 0.99 | 20 | 2 | 1 | stated in 1 doc(s) ^[tsdp-analyse-kaels-innere-welt.md:L23] ^[tsdp-analyse-kaels-innere-welt.md:L52] |
| WiDir | Wireless Directory | 0.99 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L169] |
| Verletzung des Allgemeinen Persönlichkeitsrechts | APR | 0.98 | 1 | 1 | 1 | stated in 1 doc(s) ^[rechtliche-analyse-entlassungsbericht-und-dis.md:L167] |
| Allgemeine Relativitätstheorie | ART | 0.98 | 6 | 5 | 1 | stated in 1 doc(s) ^[fragen-zu-existenz-agency-und-realitaet.md:L221] |
| IFS | About Internal Family Systems | 0.98 | 68 | 1 | 1 | stated in 1 doc(s) ^[narrative-plot-exploration-existenzielle-kohaerenz.md:L432] |
| BusRdX | Bus Read Exclusive | 0.98 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L116] |
| C-reaktivem Protein | CRP | 0.98 | 1 | 1 | 1 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L94]; proposed |
| CMP | State Freezing | 0.98 | 1 | 3 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L342] |
| CNT | Computational Narrative Technologies | 0.98 | 1 | 1 | 1 | stated in 1 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L201] |
| CPT | Cognitive Processing Therapy | 0.98 | 12 | 1 | 1 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L223] |
| Cn | Da Costas C-Systeme | 0.98 | 5 | 3 | 3 | stated in 1 doc(s) ^[parakonsistente-logik-fuer-kohaerenz-protokoll.md:L91] |
| Elektroenzephalogramm | EEG | 0.98 | 1 | 8 | 1 | stated in 1 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L1097] |
| EP | TSDP Emotional Part | 0.98 | 140 | 1 | 1 | stated in 1 doc(s) ^[2-kohaerenz-protokoll-konzeptentwicklung.md:L84] |
| EST | Environmental Storytelling | 0.98 | 12 | 33 | 8 | stated in 1 doc(s) ^[parakonsistente-logik-fuer-kohaerenz-protokoll.md:L258] |
| Echtzeit-Selbstverifikation | RTSV | 0.98 | 1 | 14 | 1 | stated in 1 doc(s) ^[aegis-analyse-und-manifest-postulation.md:L191] |
| FactsforFamilies | FFF-Guide | 0.98 | 0 | 1 | 0 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L507] |
| FÜR DIE ÜBERGEORDNETE SYSTEMANALYSE | PMAS | 0.98 | 1 | 10 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll.md:L1776] |
| Generalisierten Angststörung | GAD | 0.98 | 1 | 1 | 1 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L122]; proposed |
| Gesamt-Grades der Behinderung | GdB | 0.98 | 1 | 11 | 1 | stated in 1 doc(s) ^[juristische-recherche-zu-kptbs-dis.md:L19] |
| HHN-Achse | Hypothalamus-Hypophysen-Nebennierenrinden-Achse | 0.98 | 1 | 5 | 1 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L55] |
| HN | Harada-Norton-Gruppe | 0.98 | 5 | 5 | 4 | stated in 1 doc(s) ^[monstergruppe-logik-und-metaphern.md:L64] |
| HPA-Achse | Hypothalamus-Hypophysen-Nebennierenrinden-Achse | 0.98 | 4 | 5 | 4 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L37] |
| Held-Gruppe | He | 0.98 | 3 | 42 | 3 | stated in 1 doc(s) ^[monstergruppe-logik-und-metaphern.md:L64] |
| IDM | Intelligent Dance Music | 0.98 | 1 | 1 | 1 | stated in 1 doc(s) ^[argus-chronist-der-wandlung.md:L50] ^[argus-chronist-der-wandlung.md:L137] |
| KOOPERATIVE DATENSTROM-INTEGRATION | KDSI-GAMMA-7 | 0.98 | 1 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll.md:L1772] |
| LP | Logic of Paradox | 0.98 | 9 | 5 | 5 | stated in 1 doc(s) ^[parakonsistenz-aegis-und-nicht-existenz.md:L203] |
| Lyons | Ly | 0.98 | 9 | 22 | 8 | stated in 1 doc(s) ^[monstergruppe-narrative-cluster-und-metaphern.md:L196] |
| MBTI | Myers-Briggs | 0.98 | 1 | 1 | 1 | stated in 1 doc(s) ^[charaktermodellierung-mit-aieos-schema.md:L213] |
| MM | Monstrous Moonshine | 0.98 | 1 | 42 | 1 | stated in 1 doc(s) ^[monstergruppe-kohaerenz-protokoll-fundament.md:L260] |
| MUH | Tegmarks Mathematical Universe Hypothesis | 0.98 | 6 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-inkubation-x.md:L45] |
| Metzingers Phänomenales Selbstmodell | PSM | 0.98 | 1 | 9 | 1 | stated in 1 doc(s) ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L1365] |
| Neunte Buch Sozialgesetzbuch | SGB IX | 0.98 | 1 | 9 | 1 | stated in 1 doc(s) ^[dis-diagnose-klinische-ethische-bewertung.md:L209] |
| Nullpunktenergie | ZPE | 0.98 | 3 | 2 | 1 | stated in 1 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L59] ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L168] |
| Ontische Strukturelle Realismus | OSR | 0.98 | 1 | 5 | 1 | stated in 1 doc(s) ^[realitaet-symmetrie-und-bewusstsein-monstergruppe.md:L105] |
| Psychodynamisch Imaginative Traumatherapie | PITT | 0.98 | 1 | 1 | 1 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L153] ^[flow-zustaende-und-dissoziative-identitaet.md:L155] |
| RCV | Recursive Consistency Validation | 0.98 | 12 | 5 | 5 | stated in 1 doc(s) ^[dramaturgical-precision-deconstructing-the-irreversible-conf.md:L21] ^[dramaturgical-precision-deconstructing-the-irreversible-conf.md:L70] |
| RQD | Relational Quantum Dynamics | 0.98 | 1 | 1 | 1 | stated in 1 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L597] |
| SARM | Resource Management Protocol | 0.98 | 9 | 1 | 1 | stated in 1 doc(s) ^[aegis.md:L105] |
| Strukturgleichungsmodelle | SEM | 0.98 | 1 | 1 | 1 | stated in 1 doc(s) ^[physik-fuer-simulierte-realitaet.md:L305]; proposed |
| SG | Sozialgerichten | 0.98 | 5 | 3 | 1 | stated in 1 doc(s) ^[sozialrechtliche-strategien-bei-traumafolgestoerungen.md:L392] |
| SSOT | Single Source of Truth | 0.98 | 1 | 7 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L434] |
| Topologischen Datenanalyse | TDA | 0.98 | 1 | 2 | 1 | stated in 1 doc(s) ^[juna-v-exiliertes-ursprungs-ich.md:L181] |
| Ubiquitous Computing | Ubicomp | 0.98 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-subplots-kapitelweise-system-exploration-docx.md:L78]; proposed |
| ACC | Anterior Cingulate Cortex | 0.97 | 3 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L35] |
| ACE | Attempto Controlled English | 0.97 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-synthese.md:L314] |
| Nervensystem | ANS | 0.97 | 13 | 2 | 2 | stated in 1 doc(s) ^[heilung-hirnchemie-kunst-trauma.md:L221] |
| Allgemeiner Sozialer Dienst | ASD | 0.97 | 1 | 2 | 1 | stated in 1 doc(s) ^[dissoziative-identitaetsstoerung-unsichtbare-diagnose.md:L309] |
| Abstrakte Interpretation | AbsInt | 0.97 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L253] |
| KW1-4 | Core Worlds | 0.97 | 10 | 39 | 1 | stated in 1 doc(s) ^[briefing-core-concepts-of-the-kohaerenz-protokoll-project.md:L128] |
| DEM | Deus Ex Machina | 0.97 | 3 | 11 | 2 | stated in 1 doc(s) ^[plotentwicklung-schluessigkeit-kohaerenz-konsistenz.md:L166] ^[plotentwicklung-schluessigkeit-kohaerenz-konsistenz.md:L254] |
| Dual-Kernel-Modell | DKT | 0.97 | 2 | 60 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-synthese.md:L117] |
| UEBA | Entity Behavior Analytics | 0.97 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-subplots-kapitelweise-system-exploration-docx.md:L39] |
| MI | Mutual Information | 0.97 | 10 | 23 | 7 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse.md:L110] |
| Minimale Phänomenale Erfahrung | MPE | 0.97 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-genesis-krise-prosa-auftrag-2.md:L166] |
| Modifikationen der Schematherapie | ST | 0.97 | 1 | 3 | 1 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L163] |
| PANSS | Negative Syndrome Scale | 0.97 | 1 | 1 | 1 | stated in 1 doc(s) ^[neurochemische-lyrik-transzendenz-durch-klang.md:L341] |
| OALib | Open Access Library | 0.97 | 1 | 1 | 1 | stated in 1 doc(s) ^[m-als-fundament-der-simulation.md:L738] |
| QRT | Quantum Resource Theories | 0.97 | 2 | 2 | 2 | stated in 1 doc(s) ^[exploring-the-coherence-protocol.md:L60] |
| RAG | Retrieval-Augmented Generation | 0.97 | 11 | 8 | 7 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L504] |
| RCP | Reversible Coherence Protocol | 0.97 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L172] ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L219] |
| SE | Somatic Experiencing | 0.97 | 2 | 5 | 2 | stated in 1 doc(s) ^[kohaerenz-prozess.md:L127] |
| VEGD | Verlinde Entropic Gravity Drive | 0.97 | 1 | 1 | 1 | stated in 1 doc(s) ^[hard-sf-roman-outline-dkt-physik-cosmic-horror.md:L241] |
| Versorgungsmedizin-Verordnung | VMV | 0.97 | 9 | 3 | 3 | stated in 1 doc(s) ^[sozialrechtliche-strategien-bei-traumafolgestoerungen.md:L23] ^[sozialrechtliche-strategien-bei-traumafolgestoerungen.md:L27] |
| VR | Virtual Reality | 0.97 | 11 | 6 | 6 | stated in 1 doc(s) ^[umfassendes-lokalitaeten-konzept-fuer-roman.md:L583] |
| ZTEM | Zero-Trust Execution Model | 0.97 | 17 | 15 | 13 | stated in 1 doc(s) ^[briefing-core-concepts-of-the-kohaerenz-protokoll-project.md:L70] |
| Anscheinend Normale Anteile | ANP | 0.96 | 2 | 145 | 2 | stated in 1 doc(s) ^[ki-narrative-kollaps-kohaerenz-paradoxie.md:L132] |
| Allgemeine Systemtheorie | AST | 0.96 | 2 | 3 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-themenanalyse-und-anreicheru.md:L121] |
| Anwendung der Dual-Kernel-Theorie | DKT | 0.96 | 1 | 60 | 1 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-protokoll.md:L13] |
| SOC | Anwendung der Second-Order Cybernetics | 0.96 | 3 | 0 | 0 | stated in 1 doc(s) ^[2-kohaerenz-protokoll-konzeptentwicklung.md:L174] |
| Autogenese | RSA | 0.96 | 1 | 3 | 1 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L49] |
| Beeinträchtigung der Persönlichkeitsfunktionen | LL-SBPF | 0.96 | 1 | 1 | 1 | stated in 1 doc(s) ^[dis-diagnose-klinische-ethische-rechtliche-analyse.md:L314] |
| Co1 | Conway | 0.96 | 12 | 18 | 7 | stated in 1 doc(s) ^[monstergruppe-narrative-cluster-und-metaphern.md:L182] |
| DB | Datenbank | 0.96 | 4 | 23 | 2 | stated in 1 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L1097] |
| Disjunktiver Syllogismus | DS | 0.96 | 3 | 4 | 2 | stated in 1 doc(s) ^[dialetheismus-im-kohaerenz-protokoll.md:L141] |
| Elektrokardiogramm | EKG | 0.96 | 1 | 1 | 1 | stated in 1 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L1097] |
| FEP | Fristons Free Energy Principle | 0.96 | 10 | 1 | 1 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L60] |
| Grundlage der Versorgungsmedizin-Verordnung | VersMedV | 0.96 | 1 | 9 | 1 | stated in 1 doc(s) ^[dis-berichtigung-umfassende-recherche-und-schreiben.md:L234] |
| HIT | Holographic Interaction Topology | 0.96 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-inkubation-x.md:L355] |
| Invarianten | INV | 0.96 | 8 | 2 | 2 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L145] |
| JSON | JavaScript Object Notation | 0.96 | 17 | 1 | 1 | stated in 1 doc(s) ^[dramatica-agentic-storyform-interactive-novel.md:L109] |
| Korrelaten | NCC | 0.96 | 3 | 1 | 1 | stated in 1 doc(s) ^[existenzforschung-fuer-roman-kohaerenz-protokoll.md:L250] |
| LC-NE | Locus Coeruleus-Noradrenalin-System | 0.96 | 1 | 1 | 1 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L57] |
| MP | Modus Ponens | 0.96 | 1 | 4 | 1 | stated in 1 doc(s) ^[dialetheismus-im-kohaerenz-protokoll.md:L140] |
| Minimalen Phänomenalen Erfahrung | MPE | 0.96 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-genesis-krise-prosa-auftrag-2.md:L167] |
| Anscheinend Normale Persönlichkeitsanteil | ANP | 0.95 | 1 | 145 | 1 | stated in 1 doc(s) ^[kael-system-tsdp-analyse-und-profile.md:L192] |
| Deutscher Psychologinnen und Psychologen | BDP | 0.95 | 1 | 3 | 1 | stated in 1 doc(s) ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L557] |
| BMD | Ballistic Missile Defense | 0.95 | 1 | 1 | 1 | stated in 1 doc(s) ^[textanalyse-existenz-system-und-leid.md:L128] |
| Klassische Logik | CL | 0.95 | 11 | 1 | 1 | stated in 1 doc(s) ^[dialetheismus-im-kohaerenz-protokoll.md:L160] |
| CPTSD | Complex PTSD | 0.95 | 9 | 11 | 4 | stated in 1 doc(s) ^[heilung-hirnchemie-kunst-trauma.md:L255] |
| CTM | Computationalism | 0.95 | 4 | 1 | 1 | stated in 1 doc(s) ^[aegis-genesis-krise-prosa-auftrag-2.md:L288] |
| Dialektisch-Behavioralen Therapie | DBT | 0.95 | 4 | 6 | 4 | stated in 1 doc(s) ^[dis-berichtigung-umfassende-recherche-und-schreiben.md:L306] |
| Elektroenzephalographie | EEG | 0.95 | 1 | 8 | 1 | stated in 1 doc(s) ^[existenzforschung-fuer-roman-kohaerenz-protokoll.md:L252] |
| Erstes Buch | SGB I | 0.95 | 1 | 2 | 1 | stated in 1 doc(s) ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L544] |
| IC | Impact Character | 0.95 | 39 | 22 | 19 | stated in 1 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L443] |
| Internationale Klassifikation der Krankheiten | ICD | 0.95 | 4 | 14 | 4 | stated in 1 doc(s) ^[dis-diagnose-klinische-ethische-rechtliche-analyse.md:L39]; proposed |
| ISH | Internal Self Helper | 0.95 | 24 | 6 | 6 | stated in 1 doc(s) ^[briefing-core-concepts-of-the-kohaerenz-protokoll-project.md:L89] |
| K3 | Kleene | 0.95 | 3 | 3 | 1 | stated in 1 doc(s) ^[dialetheismus-im-kohaerenz-protokoll.md:L160] |
| Kaels Wohneinheit | KW1 | 0.95 | 7 | 81 | 7 | stated in 1 doc(s) ^[lokalitaeten-konzept-fuer-roman-simulation.md:L263] |
| Synthesis and Integration Center | MOSAIC | 0.95 | 1 | 1 | 1 | stated in 1 doc(s) ^[umfassendes-lokalitaeten-konzept-fuer-roman.md:L710] |
| NUMA | Non-Uniform Memory Access | 0.95 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L202] |
| OBP | Ontological Boundary Protocol | 0.95 | 8 | 5 | 5 | stated in 1 doc(s) ^[aegis-persona-and-manifest-generation.md:L33] |
| Präfrontaler Kortex | PFC | 0.95 | 1 | 4 | 1 | stated in 1 doc(s) ^[heilung-hirnchemie-kunst-trauma.md:L45] |
| Parakonsistente Logik | PL | 0.95 | 31 | 1 | 1 | stated in 1 doc(s) ^[parakonsistente-logik-im-seelen-protokoll.md:L25] |
| Primat der Strukturellen Dissoziation | TSDP | 0.95 | 1 | 151 | 1 | stated in 1 doc(s) ^[kael-uberarbeitung-des-konzepts-unter-tsdp.md:L11] |
| Theorie der Strukturellen Dissoziation | TSDP | 0.95 | 57 | 151 | 52 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptentwicklung.md:L44] |
| TSDP | Trauma and Structural Dissociation | 0.95 | 151 | 1 | 1 | stated in 1 doc(s) ^[thematic-architecture-of-kohaerenz-protokoll-a-conceptual-le.md:L68] |
| UI | User Interface | 0.95 | 3 | 4 | 2 | stated in 1 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L43]; proposed |
| Berufsordnungen der Ärzte | MBO-Ä | 0.94 | 1 | 3 | 1 | stated in 1 doc(s) ^[rechtliche-analyse-entlassungsbericht-und-dis.md:L15] |
| Klassischer Logik | CL | 0.94 | 1 | 1 | 1 | stated in 1 doc(s) ^[dialetheismus-im-kohaerenz-protokoll.md:L126] |
| KW1-KW4 | Core Worlds | 0.94 | 4 | 39 | 2 | stated in 1 doc(s) ^[systemic-architecture-specification-the-coherence-protocol-w.md:L55] |
| DES | Dissociative Experiences Scale27 | 0.94 | 9 | 1 | 1 | stated in 1 doc(s) ^[neurochemische-lyrik-transzendenz-durch-klang.md:L192] |
| Dezentrale Identitätssysteme | SSI | 0.94 | 1 | 1 | 1 | stated in 1 doc(s) ^[digitale-uberwelt.md:L89] |
| Elektroenzephalografie | EEG | 0.94 | 1 | 8 | 1 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L47] |
| Hard SF | Hard Science Fiction | 0.94 | 19 | 20 | 12 | stated in 1 doc(s) ^[hard-sci-fi-cosmic-horror-research-questions.md:L17] |
| Medizinischen Dienste | MD | 0.94 | 1 | 11 | 1 | stated in 1 doc(s) ^[juristische-recherche-zu-kptbs-dis.md:L257] |
| Tegmarks Hypothese | MUH | 0.94 | 1 | 6 | 1 | stated in 1 doc(s) ^[realitaet-symmetrie-und-bewusstsein-monstergruppe.md:L121] |
| MWI | Many Worlds Interpretation | 0.94 | 4 | 1 | 1 | stated in 1 doc(s) ^[hard-sci-fi-cosmic-horror-research-questions.md:L123] |
| Metzinger | PSM | 0.94 | 7 | 9 | 4 | stated in 1 doc(s) ^[kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md.md:L620] |
| Modellierung der Selbstvalidierung | RCV | 0.94 | 1 | 12 | 1 | stated in 1 doc(s) ^[aegis-analyse-und-manifest-postulation.md:L206] |
| Repräsentiert die Subjective Story | SS | 0.94 | 1 | 19 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-detaillierte-recherche.md:L205] |
| Transiente Hypofrontalität | THH | 0.94 | 1 | 1 | 1 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L77] |
| ZKP | Zero-Knowledge Proof | 0.94 | 5 | 5 | 5 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-analyse.md:L191] |
| Abstraktionsebenen | LoA | 0.93 | 4 | 3 | 2 | stated in 1 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L85] ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L348] |
| CFT | Conformal Field Theory | 0.93 | 25 | 3 | 3 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L131]; proposed |
| DPDR | Derealization Disorder | 0.93 | 1 | 2 | 1 | stated in 1 doc(s) ^[gravitational-architecture-novel-structure.md:L112] |
| EPR | Quantum Entanglement | 0.93 | 15 | 34 | 2 | stated in 1 doc(s) ^[gravitational-architecture-novel-structure.md:L277] |
| FDE | First-Degree Entailment | 0.93 | 7 | 3 | 3 | stated in 1 doc(s) ^[kohaerenz-protokoll-architecture-synthesis.md:L119] |
| PI | Floridis Philosophie der Information | 0.93 | 2 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-themenanalyse-und-anreicheru.md:L158] |
| LFI | Formal Inconsistency Logics | 0.93 | 25 | 1 | 1 | stated in 1 doc(s) ^[dramatica-und-kohaerenz-protokoll-analyse.md:L121] |
| Framework der Strukturellen Dissoziation | TSDP | 0.93 | 1 | 151 | 1 | stated in 1 doc(s) ^[forschungsauftrag-spannungspunktanalyse-und-charakterausarbe.md:L15] |
| ISH | Internal Self-Helper | 0.93 | 24 | 8 | 5 | stated in 1 doc(s) ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L50] |
| Lorentz-Invarianz | LI | 0.93 | 4 | 1 | 1 | stated in 1 doc(s) ^[physik-fuer-simulierte-realitaet.md:L213] |
| LP | Priests Logic of Paradox | 0.93 | 9 | 1 | 1 | stated in 1 doc(s) ^[parakonsistenz-aegis-und-nicht-existenz.md:L173] |
| OQ-E | Silas und Oblivion | 0.93 | 2 | 3 | 2 | stated in 1 doc(s) ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L443] |
| PTSD | Post-Traumatic Stress Disorder | 0.93 | 32 | 6 | 5 | stated in 1 doc(s) ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L663]; proposed |
| TSDP | Prinzipien der Strukturellen Dissoziation | 0.93 | 151 | 0 | 0 | stated in 1 doc(s) ^[genesis-krise-aegis-prosa-auftrag.md:L64] |
| A-DES | Adolescent Dissociative Experiences Scale | 0.92 | 1 | 1 | 1 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L39] |
| Beispiel der Dissoziativen Identitätsstörung | DIS | 0.92 | 1 | 53 | 1 | stated in 1 doc(s) ^[rechtliche-analyse-entlassungsbericht-und-dis.md:L383] |
| Bewertungsrahmen | VMG | 0.92 | 2 | 7 | 1 | stated in 1 doc(s) ^[dissoziative-identitaetsstoerung-unsichtbare-diagnose.md:L131] |
| OCEAN | Big Five | 0.92 | 1 | 2 | 1 | stated in 1 doc(s) ^[charaktermodellierung-mit-aieos-schema.md:L45] |
| IIT | Consciousness Model | 0.92 | 29 | 1 | 1 | stated in 1 doc(s) ^[briefing-core-concepts-of-the-kohaerenz-protokoll-project.md:L47] |
| HELM | Evaluation of Language Models | 0.92 | 1 | 1 | 1 | stated in 1 doc(s) ^[dramatica-agentic-storyform-interactive-novel.md:L548] |
| Künstliche Superintelligenz | KSI | 0.92 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-genesis-krise-prosa-auftrag-2.md:L328] |
| MUH | Mathematical Universe Hypothesis | 0.92 | 6 | 6 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-inkubation-x.md:L353] |
| OS | Objective Story Throughline | 0.92 | 43 | 7 | 6 | stated in 1 doc(s) ^[dual-kernel-erzaehlarchitektur-bewusstsein-symmetrie-ourobor.md:L88] |
| PS | Potential Space | 0.92 | 1 | 1 | 1 | stated in 1 doc(s) ^[logiksystem-aegis-entwicklungsszenarien-docx.md:L241] |
| Supersymmetrie | SUSY | 0.92 | 1 | 1 | 1 | stated in 1 doc(s) ^[physik-fuer-simulierte-realitaet.md:L176]; proposed |
| Validierung | ZTV | 0.92 | 71 | 2 | 2 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L88] |
| ZKP | Zero-Knowledge Proofs | 0.92 | 5 | 4 | 3 | stated in 1 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L161] |
| Schreckreflex | ASR | 0.91 | 1 | 1 | 1 | stated in 1 doc(s) ^[neurochemische-lyrik-transzendenz-durch-klang.md:L233] |
| Anti-de Sitter Raum | AdS | 0.91 | 1 | 8 | 1 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L130] |
| Einflusscharakter | IC | 0.91 | 2 | 39 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-architecture-synthesis-2.md:L72] |
| Interne Kohärenz | RCV | 0.91 | 4 | 12 | 2 | stated in 1 doc(s) ^[aegis-philosophie-und-systemtheorie.md:L129] |
| Internes Entropie-Management | P-ENTROPY | 0.91 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-protokolle-kritische-evaluation-neukonzeption.md:L50] |
| Kontext der Vertexoperatoralgebren | VOAs | 0.91 | 1 | 13 | 1 | stated in 1 doc(s) ^[monstergruppe-logik-und-metaphern.md:L104] |
| SSI | Self-Sovereign Identity | 0.91 | 1 | 1 | 1 | stated in 1 doc(s) ^[digitale-uberwelt.md:L49] ^[digitale-uberwelt.md:L155] |
| WIMPs | Weakly Interacting Massive Particles | 0.91 | 1 | 1 | 1 | stated in 1 doc(s) ^[physik-fuer-simulierte-realitaet.md:L118]; proposed |
| ZTA | Zero Trust Architectures | 0.91 | 5 | 1 | 1 | stated in 1 doc(s) ^[aegis-analyse-und-manifest-postulation.md:L142] |
| ZTEM | Zero-Trust Environment Mandate | 0.91 | 17 | 1 | 1 | stated in 1 doc(s) ^[digitale-uberwelt-konzept-und-gestaltung.md:L78] |
| Ambulanten Psychiatrischen Pflege | APP | 0.90 | 1 | 1 | 1 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L287] |
| Aktivierung des Kappa-Opioid-Rezeptors | KOR | 0.90 | 1 | 1 | 1 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L284] |
| CI | Intelligenz | 0.90 | 2 | 108 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-transzendenz-vektoren.md:L249] |
| Contradiction Log | M07 | 0.90 | 4 | 1 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L429] |
| DET | Differential Entangled Topology | 0.90 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-transzendenz-vektoren.md:L121] |
| IC | Interaction-Constraints | 0.90 | 39 | 1 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L131] |
| IC | Obstacle Character | 0.90 | 39 | 2 | 1 | stated in 1 doc(s) ^[narrative-context-protocol-ncp-spezifikation.md:L27] ^[narrative-context-protocol-ncp-spezifikation.md:L52] |
| Maps of Content | Identification of MOCs | 0.90 | 3 | 1 | 1 | stated in 1 doc(s) ^[reality-s-isomorphic-architecture-explained.md:L368] |
| Infohazards | Information Hazards | 0.90 | 2 | 2 | 1 | stated in 1 doc(s) ^[aegis-genesis-krise-konzeptioneller-rahmen.md:L370] ^[aegis-genesis-krise-konzeptioneller-rahmen.md:L592] |
| LeanRAG | Retrieval-Augmented Generation | 0.90 | 5 | 8 | 1 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L74] |
| Psychoneuroimmunologie | PNI | 0.90 | 1 | 1 | 1 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L90] |
| SELCC | Shared-Exclusive Latch Cache Coherence | 0.90 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L174] |
| Symmetriebrechung | SSB | 0.90 | 12 | 3 | 3 | stated in 1 doc(s) ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L113] ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L168] |
| Anscheinend Normale Persönlichkeitsanteile | ANP | 0.89 | 15 | 145 | 15 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L52] |
| ANP | Apparently Normal Personality | 0.89 | 145 | 2 | 2 | stated in 1 doc(s) ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L37] |
| BAG Selbsthilfe | Bundesarbeitsgemeinschaft Selbsthilfe | 0.89 | 1 | 1 | 1 | stated in 1 doc(s) ^[juristische-recherche-zu-kptbs-dis.md:L45] |
| Bewusstseins | DIS | 0.89 | 116 | 53 | 29 | stated in 1 doc(s) ^[integriertes-kohaerenz-protokoll-erstellung.md:L267] |
| Boolesche Erfüllbarkeit | SAT | 0.89 | 1 | 2 | 1 | stated in 1 doc(s) ^[p-vs-np-und-kohaerenz.md:L64] |
| CMP | State-Freezing | 0.89 | 1 | 6 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L21] |
| ECQ | Prinzips Ex Contradictione Quodlibet | 0.89 | 9 | 0 | 0 | stated in 1 doc(s) ^[parakonsistente-logik-im-seelen-protokoll.md:L25] |
| ES | Kernprinzipien des Environmental Storytelling | 0.89 | 1 | 1 | 1 | stated in 1 doc(s) ^[monstergruppe-narrative-cluster-und-metaphern.md:L302] |
| Genetische Algorithmen | GAs | 0.89 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptionelle-ausarbeitung.md:L177] |
| Leistungsdichtespektren | PSD | 0.89 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L41] |
| QP | Observer Effect | 0.89 | 1 | 3 | 1 | stated in 1 doc(s) ^[trauma-archaeologie-interdisziplinaere-konzeptentwicklung-do.md:L490] |
| PCT | Perceptual Control Theory | 0.89 | 2 | 2 | 2 | stated in 1 doc(s) ^[kohaerenz-prozess.md:L67] |
| RPKI | Resource Certification | 0.89 | 1 | 1 | 1 | stated in 1 doc(s) ^[digitale-uberwelt.md:L194] |
| SAP | Strong Anthropic Principle | 0.89 | 4 | 1 | 1 | stated in 1 doc(s) ^[exploring-the-coherence-protocol.md:L239] |
| Selbstkonsistenz | ZTV | 0.89 | 6 | 2 | 1 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L117] |
| AEDP | Accelerated Experiential Dynamic Psychotherapy | 0.88 | 1 | 1 | 1 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L168] |
| AL | Ashtekar-Lewandowski | 0.88 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-transzendenz-vektoren.md:L44] |
| Äußere Nicht-Identifikation | ANI | 0.88 | 1 | 2 | 1 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L83] |
| Allgemein | PL | 0.88 | 5 | 1 | 1 | stated in 1 doc(s) ^[parakonsistente-logik-im-seelen-protokoll.md:L113] ^[parakonsistente-logik-im-seelen-protokoll.md:L121] |
| Boundary Protocols | OBP | 0.88 | 1 | 8 | 1 | stated in 1 doc(s) ^[welt.md:L77] |
| Branching Rule | R-STR-03 | 0.88 | 1 | 1 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L341] |
| Polynomial | Class P | 0.88 | 6 | 3 | 3 | stated in 1 doc(s) ^[editorial-style-dossier-somatic-and-linguistic-implementatio.md:L27] |
| EP | Emotional Parts | 0.88 | 140 | 78 | 61 | stated in 1 doc(s) ^[kohaerenz-protokoll-hard-sf-horror-thriller.md:L85] |
| EST | Technik des Environmental Storytelling | 0.88 | 12 | 0 | 0 | stated in 1 doc(s) ^[roman-outline-system-kael.md:L39] |
| Richtlinien des Gemeinsamen Bundesausschusses | G-BA | 0.88 | 1 | 1 | 1 | stated in 1 doc(s) ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L49] |
| G24 | Golay-Code | 0.88 | 1 | 5 | 1 | stated in 1 doc(s) ^[monstergruppe-narrative-cluster-und-metaphern.md:L154] ^[monstergruppe-narrative-cluster-und-metaphern.md:L155] |
| Identität des Point-of-View | POV | 0.88 | 1 | 20 | 1 | stated in 1 doc(s) ^[codex-optimierung-fuer-kohaerenz-protokoll.md:L30] |
| KG | Knowledge Graph | 0.88 | 1 | 5 | 1 | stated in 1 doc(s) ^[ki-agenten-kohaerenz-und-prompt-generierung.md:L121] |
| Schleifenquantengravitation | LQG | 0.88 | 3 | 2 | 2 | stated in 1 doc(s) ^[physik-fuer-simulierte-realitaet.md:L192]; proposed |
| Persönlichkeitsstörung | MPD | 0.88 | 15 | 5 | 1 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L15] |
| Pre-Mortem-Analyse | Method M03 | 0.88 | 1 | 1 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L510] |
| Multiple-Reader | SWMR | 0.88 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L67] |
| NCP | Narrative Protocol | 0.88 | 23 | 1 | 1 | stated in 1 doc(s) ^[narrative-modelle-und-dramatica-erweiterung.md:L106] |
| Phänomenale Selbstmodell | PSM | 0.88 | 1 | 9 | 1 | stated in 1 doc(s) ^[charaktermodellierung-mit-aieos-schema.md:L192] |
| Phänomenales Selbstmodell | PSM | 0.88 | 4 | 9 | 4 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-analyse.md:L193] |
| Reasoning and Acting | ReAct-Frameworks | 0.88 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L5] |
| Soziale Phobie | SAD | 0.88 | 1 | 1 | 1 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L128] |
| Selbstorganisierte Kritikalität | SOC | 0.88 | 3 | 3 | 2 | stated in 1 doc(s) ^[aegis-subplots-kapitelweise-system-exploration-docx.md:L88] |
| Weltgesundheitsorganisation | WHO | 0.88 | 2 | 4 | 1 | stated in 1 doc(s) ^[dis-diagnose-klinische-ethische-rechtliche-analyse.md:L39]; proposed |
| Hyperaktivitätsstörung | ADHS | 0.87 | 1 | 5 | 1 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L21] ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L27] |
| BTHG | Reform des Bundesteilhabegesetzes | 0.87 | 2 | 1 | 1 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L119] |
| M04 | Contrast Classes | 0.87 | 1 | 3 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L427] |
| DES | Dissociation Experience Scale | 0.87 | 9 | 1 | 1 | stated in 1 doc(s) ^[sozialrechtliche-strategien-bei-traumafolgestoerungen.md:L75] |
| The-Handy-Math-Answer-Book | Handy | 0.87 | 1 | 2 | 1 | stated in 1 doc(s) ^[primzahlen-als-metapher-in-kohaerenz-protokoll.md:L273] |
| IIT | Performing Integrated Information Theory | 0.87 | 29 | 1 | 1 | stated in 1 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L383] |
| Klimax-Architektur | P7 | 0.87 | 2 | 3 | 2 | stated in 1 doc(s) ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L1245] |
| PAL | Lock | 0.87 | 4 | 15 | 3 | stated in 1 doc(s) ^[dkt-fundament-kohaerenz-protokoll-md.md:L76] |
| McLeans Anstalt | McL | 0.87 | 1 | 22 | 1 | stated in 1 doc(s) ^[tsdp-analyse-kaels-innere-welt.md:L88] |
| Signal-Rausch-Verhältnis | SNR | 0.87 | 5 | 1 | 1 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L117]; proposed |
| Transaktionale Interpretation | TIQM | 0.87 | 1 | 1 | 1 | stated in 1 doc(s) ^[physik-fuer-simulierte-realitaet.md:L325] ^[physik-fuer-simulierte-realitaet.md:L549] |
| AEGIS | Gatekeeper for Integrity Systems | 0.86 | 269 | 40 | 40 | stated in 1 doc(s) ^[the-k-j-connection-defining-the-non-algorithmic-mechanism-of.md:L15] |
| Anscheinend Normale Teile | ANP | 0.86 | 2 | 145 | 2 | stated in 1 doc(s) ^[tsdp-analyse-kaels-innere-welt.md:L27] |
| Bild der Dissoziativen Identitätsstörung | DID | 0.86 | 1 | 100 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-finale-pfeiler.md:L144] |
| Kaels Dissoziative Identitätsstörung | DIS | 0.86 | 2 | 53 | 1 | stated in 1 doc(s) ^[junas-liebe-kaels-trauma-aegis-docx.md:L27] |
| ERP | Entropie-Resonanz-Protokolle | 0.86 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L122] |
| Empfindlichkeit der Glukokortikoidrezeptoren | GR | 0.86 | 1 | 3 | 1 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L59] |
| Fünftes Buch | SGB V | 0.86 | 1 | 2 | 1 | stated in 1 doc(s) ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L545] |
| Protokollierung des Integritätsprüfungsmechanismus | M4 | 0.86 | 1 | 4 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-duale-dramatica-storyform-synthese.md:L149] |
| Medizinischen Dienst | MD | 0.86 | 1 | 11 | 1 | stated in 1 doc(s) ^[rechtliche-analyse-entlassungsbericht-und-dis.md:L181] |
| ZGTP | S THEORY OF PERSONALITY | 0.86 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L230] |
| Serotonin-Wiederaufnahmehemmer | SSRI | 0.86 | 1 | 1 | 1 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L181] |
| Commitment-Therapie | ACT | 0.85 | 1 | 3 | 1 | stated in 1 doc(s) ^[juna-kael-system-krisenanalyse-und-rettungsplan.md:L205] |
| AIF | Active Inference | 0.85 | 1 | 9 | 1 | stated in 1 doc(s) ^[aegis-protokolle-kritische-evaluation-neukonzeption.md:L33] |
| Anscheinend Normalen Persönlichkeitsanteil | ANP | 0.85 | 2 | 145 | 2 | stated in 1 doc(s) ^[strukturelle-dissoziation-system-kael-analyse.md:L181] |
| Mehrere Anscheinend Normale Persönlichkeitsanteile | ANPs | 0.85 | 1 | 122 | 1 | stated in 1 doc(s) ^[charaktere.md:L120] |
| AbW | Wohnen | 0.85 | 1 | 3 | 1 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L265] |
| DLT | Distributed Ledgers | 0.85 | 1 | 1 | 1 | stated in 1 doc(s) ^[digitale-uberwelt.md:L89] |
| Prinzips der Explosion | ECQ | 0.85 | 1 | 9 | 1 | stated in 1 doc(s) ^[parakonsistente-logik-fuer-kohaerenz-protokoll.md:L27] |
| Erfüllbarkeitsproblem der Aussagenlogik | SAT | 0.85 | 1 | 2 | 1 | stated in 1 doc(s) ^[aegis-logik-und-narrative-implikationen.md:L56] |
| Objektiver Kollaps | GRW | 0.85 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md.md:L494] |
| Kael und Juna | K-J | 0.85 | 48 | 34 | 7 | stated in 1 doc(s) ^[primzahlen-als-metapher-in-kohaerenz-protokoll.md:L24] |
| Leitlinie | S3 | 0.85 | 13 | 13 | 11 | stated in 1 doc(s) ^[dissoziative-identitaetsstoerung-unsichtbare-diagnose.md:L209] |
| MemAct | Manages the Memory-as-Action | 0.85 | 5 | 1 | 1 | stated in 1 doc(s) ^[aegis-persona-and-manifest-generation.md:L169] |
| McLaughlin-Welt | McL | 0.85 | 1 | 22 | 1 | stated in 1 doc(s) ^[kernwelten-fuer-kohaerenz-protokoll.md:L465] |
| Positronen-Emissions-Tomographie | PET | 0.85 | 1 | 1 | 1 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L47]; proposed |
| Tertiären Strukturellen Dissoziation | TSD | 0.85 | 12 | 2 | 2 | stated in 1 doc(s) ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:L97] |
| K₁ | Coherence-Kernel | 0.84 | 24 | 1 | 1 | stated in 1 doc(s) ^[the-thematic-architecture-of-kohaerenz-protokoll-a-conceptua.md:L27] |
| FLM | Lepowsky und Arne Meurman | 0.84 | 1 | 5 | 1 | stated in 1 doc(s) ^[monstergruppe-als-denkmodell-der-komplexitaet.md:L129] |
| Interne Selbstprüfung | RCV | 0.84 | 1 | 12 | 1 | stated in 1 doc(s) ^[aegis-philosophische-und-systemtheoretische-analyse-docx.md:L207] |
| KW4 | Welt Kairos-Potentialis | 0.84 | 68 | 0 | 0 | stated in 1 doc(s) ^[kohaerenz-protokoll-duale-dramatica-storyform-synthese.md:L182] |
| Loop Quantum Gravity | LQG | 0.84 | 3 | 2 | 2 | stated in 1 doc(s) ^[physik-fuer-simulierte-realitaet.md:L571] |
| RQFT | Relativistic Quantum Field Theory | 0.84 | 1 | 1 | 1 | stated in 1 doc(s) ^[global-research-for-kohaerenz-protokoll.md:L113] |
| RS | Relationship Story Throughline | 0.84 | 23 | 4 | 3 | stated in 1 doc(s) ^[dual-kernel-erzaehlarchitektur-bewusstsein-symmetrie-ourobor.md:L91] |
| Serotonin-Noradrenalin-Wiederaufnahmehemmer | SNRI | 0.84 | 1 | 1 | 1 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L181]; proposed |
| TSP | Traveling Salesperson Problem | 0.84 | 5 | 1 | 1 | stated in 1 doc(s) ^[the-psychological-mechanics-from-tertiary-structural-dissoci.md:L59]; proposed |
| Anscheinend Normalen Persönlichkeitsanteilen | ANPs | 0.83 | 8 | 122 | 6 | stated in 1 doc(s) ^[charaktere.md:L27] |
| Zelluläre Automaten | CA | 0.83 | 4 | 8 | 1 | stated in 1 doc(s) ^[emergenz-autonomer-systeme-aegis-forschung.md:L413] ^[emergenz-autonomer-systeme-aegis-forschung.md:L437] |
| Charakteristika der Dissoziativen Identitätsstörung | DIS | 0.83 | 1 | 53 | 1 | stated in 1 doc(s) ^[juna-kael-system-analyse-und-rettungsplan-docx.md:L47] |
| DAG | Directed Acyclic Graph | 0.83 | 1 | 1 | 1 | stated in 1 doc(s) ^[comprehensive-systemic-architectural-and-psychological-conte.md:L109] |
| FMEA | Modes and Effects Analysis | 0.83 | 3 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-transzendenz-vektoren.md:L359] |
| Gamma-Aminobuttersäure | GABA | 0.83 | 1 | 4 | 1 | stated in 1 doc(s) ^[neurochemische-lyrik-transzendenz-durch-klang.md:L145] |
| ICT | Information Closure Theory | 0.83 | 1 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-transzendenz-vektoren.md:L101] |
| Interne Semantik-Genese | RSA | 0.83 | 1 | 3 | 1 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L225] |
| Reflexions-Baseline-Mechanismus | M0 | 0.83 | 1 | 2 | 1 | stated in 1 doc(s) ^[dramatica-und-kohaerenz-protokoll-analyse.md:L19] |
| PIF | Primordial Informational Field | 0.83 | 1 | 1 | 1 | stated in 1 doc(s) ^[konzeptionelle-transzendenz-fuer-kohaerenz-protokoll.md:L50] |
| ADHD | Hyperactivity Disorder | 0.82 | 5 | 2 | 2 | stated in 1 doc(s) ^[comprehensive-systemic-architectural-and-psychological-conte.md:L21] |
| Adversariellen | K0 | 0.82 | 1 | 26 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L114] |
| CSI | Index | 0.82 | 5 | 28 | 5 | stated in 1 doc(s) ^[ontologische-inversion-von-aegis-kritisches-framework.md:L28] |
| K₀ | Collapse-Kernel | 0.82 | 26 | 1 | 1 | stated in 1 doc(s) ^[the-thematic-architecture-of-kohaerenz-protokoll-a-conceptua.md:L28] |
| Dissoziativer Identitätsstörung | DID | 0.82 | 6 | 100 | 4 | stated in 1 doc(s) ^[paradoxien-der-kohaerenz-protokoll-entwicklung.md:L282] |
| Dual Kernel Theorie | DKT | 0.82 | 8 | 60 | 8 | stated in 1 doc(s) ^[kohaerenz-protokoll-hard-sf-horror-thriller.md:L23] |
| Metaphorische System-Darstellungen | EST | 0.82 | 1 | 12 | 1 | stated in 1 doc(s) ^[paradoxien-der-kohaerenz-protokoll-entwicklung.md:L324] |
| Ontischen Strukturellen Realismus | OSR | 0.82 | 1 | 5 | 1 | stated in 1 doc(s) ^[realitaet-symmetrie-und-bewusstsein-monstergruppe.md:L101] |
| Standard AIEOS | AI Entity Object Specification | 0.81 | 1 | 2 | 1 | stated in 1 doc(s) ^[charaktermodellierung-mit-aieos-schema.md:L15] |
| Konzept der Konstitutionellen KI | CAI | 0.81 | 1 | 1 | 1 | stated in 1 doc(s) ^[ki-agenten-kohaerenz-und-prompt-generierung.md:L175] |
| Dissoziativer Identitätsstörung | DIS | 0.81 | 6 | 53 | 3 | stated in 1 doc(s) ^[dissoziative-identitaet-invalidierung-im-gesundheitssystem.md:L246] |
| IC | Influence Character Throughline | 0.81 | 39 | 4 | 4 | stated in 1 doc(s) ^[dual-kernel-erzaehlarchitektur-bewusstsein-symmetrie-ourobor.md:L90] |
| IMPLEMENTIERUNG EINES NEUEN INTEGRATIONS-PROTOKOLLS | IP-K1123 | 0.81 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll.md:L685] |
| Mathematische Universum-Hypothese | MUH | 0.81 | 1 | 6 | 1 | stated in 1 doc(s) ^[realitaet-symmetrie-und-bewusstsein-monstergruppe.md:L125] |
| Ribonukleinsäure | RNA | 0.81 | 1 | 3 | 1 | stated in 1 doc(s) ^[existenzforschung-fuer-roman-kohaerenz-protokoll.md:L208]; proposed |
| Theorie der Vertexoperatoralgebren | VOAs | 0.81 | 1 | 13 | 1 | stated in 1 doc(s) ^[monstergruppe-logik-und-metaphern.md:L108] |
| WASM | WebAssembly | 0.81 | 1 | 1 | 1 | stated in 1 doc(s) ^[aieos-schema-fuer-ki-charaktere.md:L45] |
| Anscheinend Normalen Teilen | ANP | 0.80 | 4 | 145 | 4 | stated in 1 doc(s) ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:L99] |
| Anscheinend Normaler Teil | ANP | 0.80 | 2 | 145 | 2 | stated in 1 doc(s) ^[ki-antagonist-fragmentierte-gottheit-analyse.md:L114] |
| AST | Abstract Syntax Tree | 0.80 | 3 | 1 | 1 | stated in 1 doc(s) ^[aieos-schema-fuer-ki-charaktere.md:L583] |
| Antagonist und Influence Character | IC | 0.80 | 1 | 39 | 1 | stated in 1 doc(s) ^[dramatica-storyform-kohaerenz-protokoll-analyse.md:L24] |
| Anwendung der Traumatheorie | TSDP | 0.80 | 0 | 151 | 0 | stated in 1 doc(s) ^[genesis-krise-aegis-prosa-auftrag.md:L171] |
| Atemporalität | PAL | 0.80 | 4 | 4 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md.md:L653] |
| CSP | Constraint Satisfaction Problem | 0.80 | 1 | 1 | 1 | stated in 1 doc(s) ^[p-vs-np-und-kohaerenz.md:L271]; proposed |
| Störungsbild der Dissoziativen Identitätsstörung | DID | 0.80 | 1 | 100 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-forschungsaufgabe.md:L105] |
| Identitätsstruktur | DIS | 0.80 | 30 | 53 | 14 | stated in 1 doc(s) ^[dissoziative-identitaet-invalidierung-im-gesundheitssystem.md:L327] |
| Fundamente der Dual-Kernel-Theorie | DKT | 0.80 | 1 | 60 | 1 | stated in 1 doc(s) ^[aegis-und-der-kollaps-kritische-analyse.md:L23] |
| Grundlagen der Dual-Kernel-Theorie | DKT | 0.80 | 1 | 60 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-architecture-synthesis.md:L131] |
| Emotionalen Persönlichkeitsanteil | EP | 0.80 | 2 | 140 | 2 | stated in 1 doc(s) ^[strukturelle-dissoziation-system-kael-analyse.md:L181] |
| Effizienz der Rekursiven Konsistenzvalidierung | RCV | 0.80 | 1 | 12 | 1 | stated in 1 doc(s) ^[aegis-philosophische-und-systemtheoretische-analyse-docx.md:L199] |
| KW2 | In the Mnemosyne-Archipel | 0.80 | 75 | 0 | 0 | stated in 1 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1064] |
| Komplexitätstheorie | SFI | 0.80 | 28 | 2 | 1 | stated in 1 doc(s) ^[aegis-genesis-krise-prosa-auftrag-2.md:L440] ^[aegis-genesis-krise-prosa-auftrag-2.md:L514] |
| NP-schwere Berechnungen des Handlungsreisenden-Problems | TSP | 0.80 | 1 | 5 | 1 | stated in 1 doc(s) ^[dramatica-und-kohaerenz-protokoll-analyse.md:L98] |
| Standardmäßige Retrieval-Augmented Generation | RAG | 0.80 | 1 | 11 | 1 | stated in 1 doc(s) ^[ki-agenten-kohaerenz-und-prompt-generierung.md:L119] |
| SAO | Sword Art Online | 0.80 | 1 | 1 | 1 | stated in 1 doc(s) ^[digitale-uberwelt.md:L49] |
| Transaktionalen Interpretation | TIQM | 0.80 | 1 | 1 | 1 | stated in 1 doc(s) ^[physik-fuer-simulierte-realitaet.md:L306] |
| Erweiterte Realität | AR | 0.79 | 1 | 2 | 1 | stated in 1 doc(s) ^[emergenz-aegis-und-selbststrukturierung.md:L295] |
| Bereich der Emotional Parts | EPs | 0.79 | 1 | 142 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzept.md:L195] |
| Glukosestoffwechsel | CMRglu | 0.79 | 1 | 1 | 1 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L63] |
| Mehrere Emotionale Persönlichkeitsanteile | EPs | 0.79 | 1 | 142 | 1 | stated in 1 doc(s) ^[charaktere.md:L121] |
| Generierung | RSA | 0.79 | 56 | 3 | 2 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L105] |
| Moonshine-Moduls und der Vertex-Operator-Algebren | VOA | 0.79 | 1 | 31 | 1 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse.md:L79] |
| Operationale Geschlossenheit und Autonomie | P6 | 0.79 | 1 | 3 | 1 | stated in 1 doc(s) ^[aegis-philosophie-und-manifest-entwicklung.md:L54] |
| Reha Aktuell | UVR | 0.79 | 1 | 1 | 1 | stated in 1 doc(s) ^[gutachten-grad-der-behinderung-bei-dis.md:L369] |
| Retrokausalität | TIQM | 0.79 | 1 | 1 | 1 | stated in 1 doc(s) ^[physik-fuer-simulierte-realitaet.md:L517] |
| Zero-Trust-Prinzip | ZTEM | 0.79 | 3 | 17 | 1 | stated in 1 doc(s) ^[aegis.md:L186] |
| RLAIF | AI Feedback | 0.78 | 1 | 2 | 1 | stated in 1 doc(s) ^[ki-agenten-kohaerenz-und-prompt-generierung.md:L245] ^[ki-agenten-kohaerenz-und-prompt-generierung.md:L365] |
| Bewusstseinsmodell | IIT | 0.78 | 1 | 29 | 1 | stated in 1 doc(s) ^[aegis-logik-und-narrative-implikationen.md:L230] |
| Kaels Dissoziativer Identitätsstörung | DID | 0.78 | 2 | 100 | 1 | stated in 1 doc(s) ^[monstergruppe-metapher-auf-mathematische-kohaerenz.md:L103] |
| ECQ | Explosion | 0.78 | 9 | 72 | 9 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse.md:L67] |
| Explosionsprinzip | ECQ | 0.78 | 6 | 9 | 2 | stated in 1 doc(s) ^[parakonsistente-logik-im-seelen-protokoll.md:L81] ^[parakonsistente-logik-im-seelen-protokoll.md:L85] |
| Emotionalen Teilen | EP | 0.78 | 4 | 140 | 4 | stated in 1 doc(s) ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:L100] |
| Lyons-Gruppe | Entspricht Ly | 0.78 | 6 | 0 | 0 | stated in 1 doc(s) ^[erlebniswelten-der-anteile-uberlagerung-mit-kernwelten.md:L20] |
| HDI | Heidelberger Dissoziationsinventar | 0.78 | 2 | 1 | 1 | stated in 1 doc(s) ^[dis-diagnose-klinische-ethische-bewertung.md:L73] |
| IMPLEMENTIERUNG EINES VERBESSERTEN INTEGRATIONSPROTOKOLLS | IP-KDSI-GAMMA-7 | 0.78 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll.md:L1778] |
| MWI | Many-Worlds-Interpretation | 0.78 | 4 | 1 | 1 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L147] |
| SN | Salience Network | 0.78 | 2 | 1 | 1 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L210] |
| Thermodynamische Maximierungsprinzipien | TMaxP | 0.78 | 1 | 1 | 1 | stated in 1 doc(s) ^[emergenz-autonomer-systeme-aegis-forschung.md:L449] |
| Begleit-Kanon | NCP | 0.77 | 1 | 23 | 1 | stated in 1 doc(s) ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L1221] |
| CRPS | Schmerzsyndrome | 0.77 | 2 | 4 | 1 | stated in 1 doc(s) ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L600] |
| Dissoziative Identitätsstruktur | DIS | 0.77 | 2 | 53 | 2 | stated in 1 doc(s) ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L17] |
| Möglichkeits-Garten | E5 | 0.77 | 22 | 2 | 1 | stated in 1 doc(s) ^[roman-outline-system-kael.md:L188] |
| Homotopietypentheorie | HoTT | 0.77 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-protokolle-kritische-evaluation-neukonzeption.md:L33] |
| Identitätsstruktur | TSDP | 0.77 | 30 | 151 | 12 | stated in 1 doc(s) ^[kohaerenz-protokoll-inkubation-x.md:L169] |
| M24 | Mathieu Gruppe | 0.77 | 3 | 1 | 1 | stated in 1 doc(s) ^[monstergruppe-narrative-cluster-und-metaphern.md:L282] |
| Narrative Expositionstherapie | NET | 0.77 | 2 | 3 | 1 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L175] |
| OCEAN | Traits | 0.77 | 1 | 1 | 1 | stated in 1 doc(s) ^[charaktermodellierung-mit-aieos-schema.md:L214] |
| Realitätsschichten | Wahrn | 0.77 | 7 | 1 | 1 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L284] |
| Anscheinend Normalen Persönlichkeitsanteilen | ANP | 0.76 | 8 | 145 | 8 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L29] |
| Beziehung | RS | 0.76 | 158 | 23 | 14 | stated in 1 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L46] ^[dramatica-storyform-validierung-und-synthese.md:L343] |
| Bundesrepublik Deutschland | GG | 0.76 | 7 | 2 | 1 | stated in 1 doc(s) ^[rechtliche-analyse-entlassungsbericht-und-dis.md:L406] |
| CAR | Cortisol Awakening Response | 0.76 | 1 | 1 | 1 | stated in 1 doc(s) ^[roman-entwicklung-ontologie-trauma-horror.md:L82] ^[roman-entwicklung-ontologie-trauma-horror.md:L138] |
| CFT | Compassion-Focused Therapy | 0.76 | 25 | 1 | 1 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L158] ^[angst-bei-komplexen-traumafolgen.md:L160]; proposed |
| Emotionale Teile | EP | 0.76 | 2 | 140 | 2 | stated in 1 doc(s) ^[tsdp-analyse-kaels-innere-welt.md:L28] |
| KIN | Emergent Closure | 0.76 | 1 | 1 | 1 | stated in 1 doc(s) ^[logiksystem-aegis-entwicklungsszenarien-docx.md:L247] |
| FMEA | Fehlermodi-Analyse | 0.76 | 3 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-transzendenz-vektoren.md:L138] |
| Herausforderung | IC | 0.76 | 122 | 39 | 9 | stated in 1 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L343] |
| M01 | Steelmanning | 0.76 | 2 | 7 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L426] |
| MAS | Space for Multi-Agent System | 0.76 | 5 | 1 | 1 | stated in 1 doc(s) ^[digitale-uberwelt.md:L135] |
| Turingmaschine | NTM | 0.76 | 6 | 1 | 1 | stated in 1 doc(s) ^[p-vs-np-und-kohaerenz.md:L56] |
| TAP | Test of Attentional Performance | 0.76 | 2 | 1 | 1 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L33] |
| Vertex-Operator Algebra | VOA | 0.76 | 1 | 31 | 1 | stated in 1 doc(s) ^[systemic-architecture-specification-the-coherence-protocol-w.md:L42] |
| Physik und Ontologie | DKT | 0.75 | 3 | 60 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L9] ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L30] |
| Impact Character | Double-IC | 0.75 | 22 | 1 | 1 | stated in 1 doc(s) ^[systemic-architecture-specification-the-coherence-protocol-w.md:L38] |
| Emotionaler Persönlichkeitsanteil | EP | 0.75 | 5 | 140 | 5 | stated in 1 doc(s) ^[kael-system-tsdp-analyse-und-profile.md:L224] |
| EPs | Emotionalen Anteile | 0.75 | 142 | 2 | 2 | stated in 1 doc(s) ^[kohaerenz-prozess-grundlagen.md:L73] |
| Techniken des Environmental Storytelling | EST | 0.75 | 2 | 12 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-weltkonzept-synthese.md:L68] |
| Informationsontologie | ISR | 0.75 | 9 | 3 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-aktuelle-gesamtkonzept-synthese-abstrakt.md:L17] |
| Multi-Agenten-Systemen | MAS | 0.75 | 8 | 5 | 4 | stated in 1 doc(s) ^[aegis-subplots-kapitelweise-system-exploration-docx.md:L52] ^[aegis-subplots-kapitelweise-system-exploration-docx.md:L274] |
| PMAS | Modeling and Analysis System | 0.75 | 10 | 1 | 1 | stated in 1 doc(s) ^[aegis-persona-and-manifest-generation.md:L41] |
| OBJECTIVE | OS | 0.75 | 3 | 43 | 1 | stated in 1 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L365] |
| FEP | Active Inference Agent | 0.74 | 10 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptionelle-ausarbeitung.md:L364] |
| Neurowissenschaftliche Begutachtung | DGNB | 0.74 | 1 | 1 | 1 | stated in 1 doc(s) ^[gutachterprofil-und-alternativen-ptbs-dis.md:L101] |
| Dysfunktionale Dissoziation | TSDP | 0.74 | 1 | 151 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptentwicklung.md:L140] |
| Nicht-lokale Informationsübertragung | FTL | 0.74 | 1 | 1 | 1 | stated in 1 doc(s) ^[physik-fuer-simulierte-realitaet.md:L509] |
| GR-Gen | NR3C1 | 0.74 | 1 | 2 | 1 | stated in 1 doc(s) ^[dissoziative-identitaetsstoerung-unsichtbare-diagnose.md:L105] |
| Virtuelle Realität | VR | 0.74 | 2 | 11 | 2 | stated in 1 doc(s) ^[emergenz-aegis-und-selbststrukturierung.md:L295] |
| Anteil | ANP | 0.73 | 97 | 145 | 72 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L273] |
| Datenanalyse | TDA | 0.73 | 14 | 2 | 2 | stated in 1 doc(s) ^[digitale-uberwelt-konzept-und-gestaltung.md:L35] |
| Desire | SS | 0.73 | 16 | 19 | 6 | stated in 1 doc(s) ^[kohaerenz-protokoll-dramatica-synthese.md:L207] |
| Posttraumatischen Belastungsstörung | SkPTBS | 0.73 | 11 | 1 | 1 | stated in 1 doc(s) ^[juristische-recherche-zu-kptbs-dis.md:L664] |
| Selbstverifikation | RTSV | 0.73 | 9 | 14 | 3 | stated in 1 doc(s) ^[aegis-analyse-und-manifest-postulation.md:L327] |
| Anscheinend Normale Anteile | ANPs | 0.72 | 2 | 122 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-synthese.md:L178] |
| Argus | Meta-Kog | 0.72 | 54 | 1 | 1 | stated in 1 doc(s) ^[editorial-style-dossier-somatic-and-linguistic-implementatio.md:L19] |
| Byzantinischer Fehlertoleranz | BFT | 0.72 | 1 | 2 | 1 | stated in 1 doc(s) ^[aegis-protokolle-kritische-evaluation-neukonzeption.md:L77] |
| Dezentrale Autonome Organisationen | DAOs | 0.72 | 1 | 2 | 1 | stated in 1 doc(s) ^[emergenz-autonomer-systeme-aegis-forschung.md:L223] |
| Psychosomatik und Nervenheilkunde | DGPPN | 0.72 | 2 | 12 | 2 | stated in 1 doc(s) ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L558] |
| Störung | DIS | 0.72 | 108 | 53 | 32 | stated in 1 doc(s) ^[dissoziative-identitaetsstoerung-unsichtbare-diagnose.md:L159] |
| Dritten | LEM | 0.72 | 8 | 1 | 1 | stated in 1 doc(s) ^[dialetheismus-im-kohaerenz-protokoll.md:L135] |
| Korrelate des Bewusstseins | NCCs | 0.72 | 4 | 3 | 3 | stated in 1 doc(s) ^[prosaversion-von-genesis-erstellen.md:L29] |
| Kybernetik | VSM | 0.72 | 50 | 2 | 2 | stated in 1 doc(s) ^[kohaerenz-prozess.md:L149] |
| Mustererkennung | PMAS | 0.72 | 36 | 10 | 2 | stated in 1 doc(s) ^[paradoxien-der-kohaerenz-protokoll-entwicklung.md:L350] |
| NPCs | Non-Player Characters | 0.72 | 11 | 1 | 1 | stated in 1 doc(s) ^[dramatica-agentic-storyform-interactive-novel.md:L165] |
| Psychologie der Strukturellen Dissoziation | TSDP | 0.72 | 1 | 151 | 1 | stated in 1 doc(s) ^[roman-finale-ethik-existenz-schoepfer-geschoepf-beziehung.md:L26] |
| RCV | Recursive Self-Verification | 0.72 | 12 | 2 | 2 | stated in 1 doc(s) ^[the-ontology-of-antagonism-the-function-of-paradox-in-kohaer.md:L27] ^[the-ontology-of-antagonism-the-function-of-paradox-in-kohaer.md:L41] |
| SIS-Protokolle | Systemic Identity Safeguard | 0.72 | 1 | 1 | 1 | stated in 1 doc(s) ^[hard-sf-roman-outline-dkt-physik-cosmic-horror.md:L162] |
| Belastungsstörungen | PTBS | 0.71 | 4 | 27 | 3 | stated in 1 doc(s) ^[ontologie-des-gelesenen-traumas.md:L124] |
| CLASSE | Cornell | 0.71 | 1 | 2 | 1 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L299] |
| KW1 | City | 0.71 | 81 | 24 | 18 | stated in 1 doc(s) ^[refining-dramatica-storyform-for-kohaerenz-protokoll.md:L152] |
| Fehlerkorrekturcodes | ECC | 0.71 | 6 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptionelle-ausarbeitung.md:L205]; proposed |
| Entität | PKP | 0.71 | 172 | 1 | 1 | stated in 1 doc(s) ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L46] |
| Inneren Familien Systeme | IFS | 0.71 | 1 | 68 | 1 | stated in 1 doc(s) ^[tsdp-analyse-kohaerenz-protokoll-charaktere.md:L104] |
| Sind die Konstrukt-Welten | KWs | 0.71 | 1 | 9 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptentwicklung.md:L13] |
| NPCs | Non-Player-Characters | 0.71 | 11 | 1 | 1 | stated in 1 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L201] |
| PSM | Phenomenal Self-Model | 0.71 | 9 | 2 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L744] |
| Belastungsstörung | SkPTBS | 0.70 | 26 | 1 | 1 | stated in 1 doc(s) ^[juristische-recherche-zu-kptbs-dis.md:L516] |
| Emotionalen Persönlichkeitsanteilen | EPs | 0.70 | 5 | 142 | 4 | stated in 1 doc(s) ^[charaktere.md:L27] |
| ESTD | Trauma and Dissociation | 0.70 | 1 | 10 | 1 | stated in 1 doc(s) ^[dissoziative-identitaet-invalidierung-im-gesundheitssystem.md:L232] |
| M24 | Mathieu | 0.70 | 3 | 5 | 2 | stated in 1 doc(s) ^[monstergruppe-narrative-cluster-und-metaphern.md:L183] |
| Vorgaben der Versorgungsmedizin-Verordnung | VMV | 0.70 | 1 | 3 | 1 | stated in 1 doc(s) ^[sozialrechtliche-strategien-bei-traumafolgestoerungen.md:L126] |
| BTHG | Umsetzung des Bundesteilhabegesetzes | 0.69 | 2 | 1 | 1 | stated in 1 doc(s) ^[dis-diagnose-klinische-ethische-bewertung.md:L326] |
| Bewertungsmaßstäbe der Versorgungsmedizin-Verordnung | VersMedV | 0.69 | 1 | 9 | 1 | stated in 1 doc(s) ^[gutachten-grad-der-behinderung-bei-dis.md:L26] |
| Emotionale Anteile | EPs | 0.69 | 4 | 142 | 4 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-synthese.md:L179] |
| GWT | Global Workspace | 0.69 | 9 | 10 | 8 | stated in 1 doc(s) ^[global-research-for-kohaerenz-protokoll.md:L91] |
| Gestaltung der Kern-Welten | KW1-4 | 0.69 | 4 | 10 | 4 | stated in 1 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L35] |
| Große Sprachmodelle | LLMs | 0.69 | 1 | 26 | 1 | stated in 1 doc(s) ^[ki-narrative-kollaps-kohaerenz-paradoxie.md:L15]; proposed |
| Möglichkeiten-Garten | KW4 | 0.69 | 5 | 68 | 1 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L111] ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L361] |
| LogOS | Logos-Prime | 0.69 | 67 | 62 | 25 | stated in 1 doc(s) ^[the-sensory-rulebook-the-body-as-a-measuring-device-in-the-p.md:L102] |
| PMAS | Predictive Modeling | 0.69 | 10 | 4 | 4 | stated in 1 doc(s) ^[paradoxien-der-kohaerenz-protokoll-entwicklung.md:L350] |
| Abgelegener Ort Sektor Gamma | E1 | 0.68 | 1 | 1 | 1 | stated in 1 doc(s) ^[roman-outline-system-kael.md:L274] |
| HOP | Higher-Order Perception | 0.68 | 1 | 1 | 1 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L79] |
| Klinische Diagnose | TSDP | 0.68 | 2 | 151 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L90] |
| Kollaps-Kernels | K₀ | 0.68 | 5 | 26 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L31] |
| NPCs | Non-Playable Characters | 0.68 | 11 | 1 | 1 | stated in 1 doc(s) ^[aieos-schema-fuer-ki-charaktere.md:L572] |
| PTSD | Posttraumatic Stress Disorder | 0.68 | 32 | 9 | 6 | stated in 1 doc(s) ^[kael-system-tsdp-analyse-und-profile.md:L453]; proposed |
| Psychotraumatologie | TSDP | 0.68 | 18 | 151 | 7 | stated in 1 doc(s) ^[dramatica-und-kohaerenz-protokoll-analyse.md:L171] |
| Künstlicher Allgemeiner Intelligenz | AGI | 0.67 | 1 | 5 | 1 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L36] |
| Gleichgewicht des Autonomen Nervensystems | ANS | 0.67 | 1 | 2 | 1 | stated in 1 doc(s) ^[heilung-hirnchemie-kunst-trauma.md:L55] |
| Grundlagen der Dissoziativen Identitätsstörung | DID | 0.67 | 1 | 100 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzept.md:L377] |
| McLaughlin-Gruppe | Entspricht McL | 0.67 | 3 | 0 | 0 | stated in 1 doc(s) ^[erlebniswelten-der-anteile-uberlagerung-mit-kernwelten.md:L18] |
| Künstlichen Intelligenz | KI | 0.67 | 7 | 167 | 6 | stated in 1 doc(s) ^[dialetheismus-im-kohaerenz-protokoll.md:L184] |
| MC | Main Character Throughline | 0.67 | 38 | 14 | 14 | stated in 1 doc(s) ^[dual-kernel-erzaehlarchitektur-bewusstsein-symmetrie-ourobor.md:L89] |
| Vom Universal Model | UNM | 0.67 | 1 | 4 | 1 | stated in 1 doc(s) ^[narrative-modelle-und-dramatica-erweiterung.md:L106] |
| Beobachtungsebene | LoA | 0.66 | 1 | 3 | 1 | stated in 1 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L489] |
| Informations-Thermodynamik und Dual-Kernel Theory | DKT | 0.66 | 1 | 60 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L17] |
| SBPM | Verfahren | 0.66 | 1 | 19 | 1 | stated in 1 doc(s) ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L556] |
| Baby-Monstergruppe | Entspricht B | 0.65 | 5 | 0 | 0 | stated in 1 doc(s) ^[erlebniswelten-der-anteile-uberlagerung-mit-kernwelten.md:L19] |
| GIF | Boundary | 0.65 | 1 | 30 | 1 | stated in 1 doc(s) ^[logiksystem-aegis-entwicklungsszenarien-docx.md:L248] |
| Konforme Feldtheorien | CFTs | 0.65 | 2 | 7 | 1 | stated in 1 doc(s) ^[m-als-fundament-der-simulation.md:L38] |
| Klassifikation und Versorgungsmedizinische Grundsätze | GdB | 0.65 | 1 | 11 | 1 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L95] |
| J1 | Janko | 0.65 | 2 | 4 | 2 | stated in 1 doc(s) ^[monstergruppe-narrative-cluster-und-metaphern.md:L194] |
| Umgebung | KW | 0.65 | 144 | 12 | 11 | stated in 1 doc(s) ^[roman-outline-system-kael.md:L227] |
| Logik | PL | 0.65 | 233 | 1 | 1 | stated in 1 doc(s) ^[parakonsistente-logik-im-seelen-protokoll.md:L105] |
| EP | Planck-Brane and Emotional Parts | 0.64 | 140 | 1 | 1 | stated in 1 doc(s) ^[reality-s-isomorphic-architecture-explained.md:L95] |
| Kollaps-Anteil | EPc | 0.64 | 4 | 1 | 1 | stated in 1 doc(s) ^[juna-kael-system-analyse-und-rettungsplan-docx.md:L83] |
| Emotionalität | KW2 | 0.64 | 16 | 75 | 4 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptentwicklung.md:L116] |
| M10 | First-Principles Decomposition | 0.64 | 2 | 4 | 1 | stated in 1 doc(s) ^[dramatica-theorie-mapping-auf-wahrheit-bewusstsein.md:L428] |
| OPE | Operator Product Expansion | 0.64 | 2 | 1 | 1 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-protokoll.md:L209] |
| ZTEM | Zero-Trust Execution | 0.64 | 17 | 16 | 13 | stated in 1 doc(s) ^[aegis-analyse-und-manifest-postulation.md:L191] |
| TF-4 | Bakkers Blind Brain Theory | 0.63 | 1 | 1 | 1 | stated in 1 doc(s) ^[roman-entwicklung-ontologie-trauma-horror.md:L140] |
| Psychologie | DGPs | 0.63 | 98 | 2 | 1 | stated in 1 doc(s) ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L557] |
| Emotionaler Teil | EP | 0.63 | 1 | 140 | 1 | stated in 1 doc(s) ^[ki-antagonist-fragmentierte-gottheit-analyse.md:L115] |
| Spekulative Nichtlokalität | FTL | 0.63 | 1 | 1 | 1 | stated in 1 doc(s) ^[physik-fuer-simulierte-realitaet.md:L576] |
| Kollaps-Kernel | K₀ | 0.63 | 18 | 26 | 3 | stated in 1 doc(s) ^[dkt-fundament-kohaerenz-protokoll-md.md:L28] |
| Konsistenz | P2 | 0.63 | 154 | 2 | 2 | stated in 1 doc(s) ^[aegis-philosophie-und-manifest-entwicklung.md:L56] |
| Multiplen Sklerose | MS | 0.63 | 1 | 2 | 1 | stated in 1 doc(s) ^[juristische-recherche-zu-kptbs-dis.md:L129] |
| Multipler Sklerose | MS | 0.63 | 2 | 2 | 2 | stated in 1 doc(s) ^[juristische-recherche-zu-kptbs-dis.md:L67] ^[juristische-recherche-zu-kptbs-dis.md:L246] |
| Moment | RCV | 0.63 | 143 | 12 | 3 | stated in 1 doc(s) ^[aegis-analyse-und-manifest-postulation.md:L298] |
| Psychologische Modelle der Dissoziation | TSDP | 0.63 | 1 | 151 | 1 | stated in 1 doc(s) ^[aegis-subplots-kapitelweise-system-exploration-docx.md:L40] |
| RTSV | Recursive Trust Signature Verification | 0.63 | 14 | 1 | 1 | stated in 1 doc(s) ^[digitale-uberwelt-konzept-und-gestaltung.md:L27] |
| Reine Logik | Welt der Reinen Logik | 0.63 | 3 | 1 | 1 | stated in 1 doc(s) ^[monstergruppe-aegis-und-narrative-moeglichkeiten.md:L151] |
| T-734 | Trauma | 0.63 | 3 | 232 | 3 | stated in 1 doc(s) ^[duale-storyform-synthese-kohaerenz-protokoll.md:L125] ^[duale-storyform-synthese-kohaerenz-protokoll.md:L232] |
| Theorie | TOE | 0.63 | 167 | 2 | 2 | stated in 1 doc(s) ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L365] |
| ANP | Solange Aegis | 0.62 | 145 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L84] |
| Input-Filterung | PL | 0.62 | 2 | 1 | 1 | stated in 1 doc(s) ^[parakonsistente-logik-im-seelen-protokoll.md:L256] |
| M13 | Query Expansion Log | 0.62 | 10 | 9 | 8 | stated in 1 doc(s) ^[kohaerenz-protokoll-synthese.md:L223] |
| Präsentation | SRCA | 0.62 | 16 | 1 | 1 | stated in 1 doc(s) ^[dramatica-theorie-narrativem-kontext-storyentwicklung.md:L148] |
| Salienz-Netzwerk | SN | 0.62 | 1 | 2 | 1 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L33] |
| Vertexoperatoralgebren | VOAs | 0.62 | 3 | 13 | 2 | stated in 1 doc(s) ^[monstergruppe-logik-und-metaphern.md:L21] ^[monstergruppe-logik-und-metaphern.md:L122] |
| Anti-de-Sitter-Raum | AdS₃ | 0.61 | 5 | 2 | 2 | stated in 1 doc(s) ^[monstergruppe-als-denkmodell-der-komplexitaet.md:L209] |
| CliniciansGuideOlderDriversComplete4thEdition | CliniciansGuide | 0.61 | 1 | 1 | 1 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L262] |
| Quantenphysik | DKT | 0.61 | 16 | 60 | 4 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L56] |
| KRM | Monitor | 0.61 | 1 | 12 | 1 | stated in 1 doc(s) ^[logiksystem-aegis-entwicklungsszenarien-docx.md:L258] |
| LP | Priest | 0.61 | 9 | 16 | 5 | stated in 1 doc(s) ^[dialetheismus-im-kohaerenz-protokoll.md:L160] |
| Selbstverifikation | RCV | 0.61 | 9 | 12 | 6 | stated in 1 doc(s) ^[aegis-philosophie-und-systemtheorie.md:L167] |
| Rekursive Selbstverifikation | RTSV | 0.61 | 2 | 14 | 2 | stated in 1 doc(s) ^[aegis.md:L187] |
| Zehntes Buch | SGB X | 0.61 | 1 | 1 | 1 | stated in 1 doc(s) ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L547] |
| BFT | Byzantine Fault Tolerance | 0.60 | 2 | 3 | 2 | stated in 1 doc(s) ^[the-coherence-protocol-a-world-bible.md:L80] |
| Balintgruppenleiter | DBG | 0.60 | 1 | 1 | 1 | stated in 1 doc(s) ^[gutachterprofil-und-alternativen-ptbs-dis.md:L151] |
| Beziehungsdynamik | RS | 0.60 | 17 | 23 | 2 | stated in 1 doc(s) ^[ki-prompt-analyse-hard-problem-of-consciousness.md:L19] |
| Cerberus | KW3 | 0.60 | 85 | 69 | 60 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L256] |
| Handlungsreisenden | TSP | 0.60 | 4 | 5 | 3 | stated in 1 doc(s) ^[aegis-logik-und-narrative-implikationen.md:L56] |
| Internationalen Klassifikation der Krankheiten | ICD-11 | 0.60 | 1 | 13 | 1 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L15] |
| Interviews | SKID-D | 0.60 | 6 | 3 | 3 | stated in 1 doc(s) ^[gutachten-grad-der-behinderung-bei-dis.md:L53] |
| Reflektions-Baseline | M0 | 0.60 | 1 | 2 | 1 | stated in 1 doc(s) ^[duale-storyform-synthese-kohaerenz-protokoll.md:L351] |
| Psychologische Modularität | TSDP | 0.60 | 1 | 151 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L55] |
| Selbstvalidierung | RCV | 0.60 | 10 | 12 | 4 | stated in 1 doc(s) ^[aegis-analyse-und-manifest-postulation.md:L200] |
| SDD | Sinne des Spec-Driven Design | 0.60 | 5 | 1 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L15] |
| Anscheinend Normalen Persönlichkeitsanteile | ANP | 0.59 | 5 | 145 | 5 | stated in 1 doc(s) ^[kohaerenz-protokoll-thematische-tiefenanalyse.md:L111] |
| Anscheinend Normalen Anteilen | ANPs | 0.59 | 1 | 122 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-detaillierte-recherche.md:L197] |
| R-ADR-04 | Contradiction | 0.59 | 1 | 33 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L460] |
| Emotionalen Persönlichkeitsanteilen | EP | 0.59 | 5 | 140 | 5 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L29] |
| Garten der Möglichkeiten | KW4 | 0.59 | 8 | 68 | 7 | stated in 1 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L426] |
| HPA-Achse | Störung der Hypothalamus-Hypophysen-Nebennierenrinden-Achse | 0.59 | 4 | 1 | 1 | stated in 1 doc(s) ^[heilung-hirnchemie-kunst-trauma.md:L26] |
| Priests LP | Logic of Paradox | 0.59 | 1 | 5 | 1 | stated in 1 doc(s) ^[m-als-fundament-der-simulation.md:L70] |
| Viele-Welten-Interpretation | MWI | 0.59 | 3 | 4 | 2 | stated in 1 doc(s) ^[physik-fuer-simulierte-realitaet.md:L45] |
| NCP | Narrative Context Protocols | 0.59 | 23 | 1 | 1 | stated in 1 doc(s) ^[ontologische-inversion-von-aegis-kritisches-framework.md:L46] |
| RS | Randall-Sundrum | 0.59 | 23 | 3 | 2 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L299] |
| Anscheinend Normalen Teil | ANP | 0.58 | 2 | 145 | 2 | stated in 1 doc(s) ^[tsdp-analyse-kaels-innere-welt.md:L23] |
| BCIs | Brain-Computer Interfaces | 0.58 | 2 | 2 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-inkubation-x.md:L180] |
| BPoF | Boundary Protocol of Failure | 0.58 | 16 | 1 | 1 | stated in 1 doc(s) ^[aegis.md:L189] |
| CFT | What Is Compassion-Focused Therapy | 0.58 | 25 | 1 | 1 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L261] |
| SCID-D | DSM Dissociative Disorders | 0.58 | 4 | 1 | 1 | stated in 1 doc(s) ^[dis-diagnose-klinische-ethische-rechtliche-analyse.md:L73] ^[dis-diagnose-klinische-ethische-rechtliche-analyse.md:L102] |
| EP | Exile | 0.58 | 140 | 18 | 10 | stated in 1 doc(s) ^[reality-s-isomorphic-architecture-explained.md:L383] |
| Galerie der Falschen Erinnerungen | KW2 | 0.58 | 1 | 75 | 1 | stated in 1 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L341] |
| Nicht-Anthropomorphismus | P8 | 0.58 | 2 | 3 | 1 | stated in 1 doc(s) ^[aegis-philosophie-und-manifest-entwicklung.md:L58] |
| Nullpunktenergien | ZPE | 0.58 | 1 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-inkubation-x.md:L56] |
| Realitätsstruktur | OSR | 0.58 | 5 | 5 | 2 | stated in 1 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L358] |
| POV | Point-of-View Charakter | 0.58 | 20 | 1 | 1 | stated in 1 doc(s) ^[codex-optimierung-fuer-kohaerenz-protokoll.md:L195] ^[codex-optimierung-fuer-kohaerenz-protokoll.md:L369] |
| Aegis | PFC | 0.57 | 34 | 4 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L118] |
| BCI | Computer Interface | 0.57 | 2 | 2 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-transzendenz-vektoren.md:L359] |
| Urteil des Bundessozialgerichts | BSG | 0.57 | 1 | 5 | 1 | stated in 1 doc(s) ^[gutachterprofil-und-alternativen-ptbs-dis.md:L69] |
| CFS | ME | 0.57 | 1 | 1 | 1 | stated in 1 doc(s) ^[juristische-recherche-zu-kptbs-dis.md:L21] ^[juristische-recherche-zu-kptbs-dis.md:L67] |
| Strukturellen Realismus | ESR | 0.57 | 2 | 1 | 1 | stated in 1 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L196] |
| Künstlicher Intelligenz | LLM | 0.57 | 8 | 28 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-synthese-integration.md:L183] |
| PAPA-Modell | Prompt-Kaskade | 0.57 | 1 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-synthese-integration.md:L186] |
| POV | Zugewiesener Narrativer Vektor | 0.57 | 20 | 1 | 1 | stated in 1 doc(s) ^[fragen-zu-existenz-agency-und-realitaet.md:L186] |
| Posttraumatisches Wachstum | PTG | 0.57 | 4 | 5 | 2 | stated in 1 doc(s) ^[prosaversion-von-genesis-erstellen.md:L113] |
| ZKP | Verification | 0.57 | 5 | 34 | 4 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-analyse.md:L193] |
| AI | Design of Artificial Intelligence | 0.56 | 138 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-finale-pfeiler.md:L309] |
| Kreuzleistungsdichtespektrum | CSD | 0.56 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-analyse-und-verstaendnis.md:L41] |
| UND STABILISIERUNGSPROTOKOLLS | ESP-K1123 | 0.56 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll.md:L1490] |
| K0 | Entropic Architecture | 0.56 | 26 | 1 | 1 | stated in 1 doc(s) ^[systemic-architecture-specification-the-coherence-protocol-w.md:L20] |
| Posttraumatischen Belastungsstörung | KPTBS | 0.56 | 11 | 2 | 2 | stated in 1 doc(s) ^[gutachterprofil-und-alternativen-ptbs-dis.md:L17] |
| QTEs | Quick-Time Events | 0.56 | 1 | 1 | 1 | stated in 1 doc(s) ^[lokalitaeten-konzept-fuer-roman-simulation.md:L143] |
| P-INIT | Bootstrapping | 0.55 | 1 | 5 | 1 | stated in 1 doc(s) ^[aegis-protokolle-kritische-evaluation-neukonzeption.md:L170] |
| Phänomenologie der CAR | Cortisol Awakening Response | 0.55 | 1 | 1 | 1 | stated in 1 doc(s) ^[roman-entwicklung-ontologie-trauma-horror.md:L104] |
| Gemäß der Dual-Kernel Theory | DKT | 0.55 | 1 | 60 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L162] |
| Dissoziatives Modul | TSDP | 0.55 | 1 | 151 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L76] |
| Klassische Explosion | ECQ | 0.55 | 1 | 9 | 1 | stated in 1 doc(s) ^[parakonsistente-logik-fuer-kohaerenz-protokoll.md:L346] |
| Hilflosigkeit | Merkzeichen H | 0.55 | 36 | 1 | 1 | stated in 1 doc(s) ^[sozialrechtliche-strategien-bei-traumafolgestoerungen.md:L170] |
| QVF | ZPE | 0.55 | 1 | 2 | 1 | stated in 1 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L370] ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L375] |
| ABW | Wohnen | 0.54 | 1 | 3 | 1 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L262] |
| LLM | Al Agent | 0.54 | 28 | 1 | 1 | stated in 1 doc(s) ^[aegis-2.md:L37] ^[aegis-2.md:L61] |
| Belastungsstörung | PTBS | 0.54 | 26 | 27 | 19 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L39] |
| DGPM | Medizin und Ärztliche Psychotherapie | 0.54 | 1 | 1 | 1 | stated in 1 doc(s) ^[dissoziative-identitaet-invalidierung-im-gesundheitssystem.md:L228] |
| Generative Systeme | LLMs | 0.54 | 1 | 26 | 1 | stated in 1 doc(s) ^[narrative-modelle-und-dramatica-erweiterung.md:L354] |
| Hauptcharakter | MC | 0.54 | 6 | 38 | 4 | stated in 1 doc(s) ^[kohaerenz-protokoll-architecture-synthesis-2.md:L72] |
| Integrierte Information | IIT | 0.54 | 4 | 29 | 4 | stated in 1 doc(s) ^[kohaerenz-protokoll-inkubation-x.md:L171] |
| Integrierten Informationstheorie | IIT | 0.54 | 1 | 29 | 1 | stated in 1 doc(s) ^[aegis-logik-und-narrative-implikationen.md:L164] |
| Kernwelten | KW1-4 | 0.54 | 134 | 10 | 2 | stated in 1 doc(s) ^[welt.md:L34] ^[welt.md:L84] |
| Kollaps-Kern | K₀ | 0.54 | 4 | 26 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-architecture-synthesis.md:L27] |
| NPCs | Nicht-Spieler-Charakteren | 0.54 | 11 | 1 | 1 | stated in 1 doc(s) ^[narrative-modelle-und-dramatica-erweiterung.md:L430] |
| ANP | Apparently Normal Parts | 0.53 | 145 | 64 | 50 | stated in 1 doc(s) ^[kohaerenz-protokoll-hard-sf-horror-thriller.md:L84] |
| Regulationsstörungen | BPS | 0.53 | 1 | 12 | 1 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L176] |
| Linse der Dissoziativen Identitätsstörung | DIS | 0.53 | 1 | 53 | 1 | stated in 1 doc(s) ^[dissoziative-identitaet-sinnsuche-im-trauma.md:L30] |
| DeGPT | Traumafolgen | 0.53 | 7 | 10 | 4 | stated in 1 doc(s) ^[gutachterprofil-und-alternativen-ptbs-dis.md:L123] |
| Domäne der EPs | Emotionale Persönlichkeitsanteile | 0.53 | 2 | 18 | 1 | stated in 1 doc(s) ^[welt.md:L47] |
| Generative KI | LLM | 0.53 | 2 | 28 | 1 | stated in 1 doc(s) ^[konzept-expose-schwarzschild-protokoll-optimierung.md:L365] |
| Kernwelten | Sim | 0.53 | 134 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-thematische-tiefenanalyse.md:L61] |
| Makro-Handlung | OS | 0.53 | 1 | 43 | 1 | stated in 1 doc(s) ^[ki-prompt-analyse-hard-problem-of-consciousness.md:L19] |
| Archiv der Grenzen | Ch14 | 0.52 | 2 | 3 | 1 | stated in 1 doc(s) ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L496] |
| Gehirn-Computer-Schnittstellen | BCIs | 0.52 | 1 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-transzendenz-vektoren.md:L259] |
| Collapse-Reaktion | EP | 0.52 | 1 | 140 | 1 | stated in 1 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L852] |
| TSDP | DISSOCIATION OF THE PERSONALITY | 0.52 | 151 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-audit-und-verifizierung.md:L230] |
| Konversionsstörungen | F44 | 0.52 | 4 | 7 | 4 | stated in 1 doc(s) ^[dissoziative-identitaet-invalidierung-im-gesundheitssystem.md:L310] |
| Informationsgeber und Feedback-Mechanismus | PCT | 0.52 | 1 | 2 | 1 | stated in 1 doc(s) ^[kohaerenz-prozess.md:L91] |
| Kernprinzipien | P1-P8 | 0.52 | 27 | 2 | 1 | stated in 1 doc(s) ^[aegis-philosophie-und-manifest-entwicklung.md:L28] |
| Kohärenz | RTSV | 0.52 | 295 | 14 | 13 | stated in 1 doc(s) ^[aegis-analyse-und-manifest-postulation.md:L207] |
| Operatorproduktentwicklung | OPE | 0.52 | 1 | 2 | 1 | stated in 1 doc(s) ^[m-als-fundament-der-simulation.md:L43] |
| ANS | Nervensystems | 0.51 | 2 | 6 | 2 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L43] |
| Bewusstlosigkeit | G-LOC | 0.51 | 1 | 2 | 1 | stated in 1 doc(s) ^[gravitation-realitaet-simulation-wahrheit.md:L272] |
| DDD | Domain-Driven Design | 0.51 | 2 | 1 | 1 | stated in 1 doc(s) ^[comprehensive-systemic-architectural-and-psychological-conte.md:L107] |
| DSM-Dissoziative Störungen | SCID-D | 0.51 | 1 | 4 | 1 | stated in 1 doc(s) ^[dissoziative-identitaetsstoerung-unsichtbare-diagnose.md:L41] |
| Funktionale Ontologie | P3 | 0.51 | 2 | 1 | 1 | stated in 1 doc(s) ^[aegis-philosophie-und-manifest-entwicklung.md:L58] |
| ITI | International Trauma Interview | 0.51 | 2 | 1 | 1 | stated in 1 doc(s) ^[angst-bei-komplexen-traumafolgen.md:L103] |
| Mnemosyne | Mnemosyne-Archipel | 0.51 | 93 | 51 | 51 | stated in 1 doc(s) ^[the-sensory-rulebook-the-body-as-a-measuring-device-in-the-p.md:L103] |
| Rolle des Overall Story | OS | 0.51 | 1 | 43 | 1 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-verortung.md:L83] |
| Anteil | EP | 0.50 | 97 | 140 | 69 | stated in 1 doc(s) ^[traumaheilung-neurochemie-adhs-dis-kunst.md:L274] |
| LOGISCHE PROTOKOLLE | CO1-TYP | 0.50 | 1 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll.md:L683] |
| CSPs | Constraint Satisfaction Problems | 0.50 | 1 | 1 | 1 | stated in 1 doc(s) ^[p-vs-np-und-kohaerenz.md:L185]; proposed |
| Emotionale Persönlichkeitsanteile | EP | 0.50 | 18 | 140 | 17 | stated in 1 doc(s) ^[angst-und-vermeidung-in-dis-systemen.md:L53] |
| Emotionalen Persönlichkeitsanteile | EP | 0.50 | 9 | 140 | 9 | stated in 1 doc(s) ^[kohaerenz-protokoll-thematische-tiefenanalyse.md:L111] |
| OS | Plot | 0.50 | 43 | 129 | 28 | stated in 1 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L343] |
| OS | Repräsentiert die Objective Story | 0.50 | 43 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-detaillierte-recherche.md:L203] |
| Tertiärer Struktureller Dissoziation | TSDP | 0.50 | 1 | 151 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-duale-dramatica-storyform-synthese.md:L82] |
| DID | Tertiary Dissociation | 0.49 | 100 | 2 | 2 | stated in 1 doc(s) ^[kael-s-dissociative-architecture-analysis.md:L56] |
| Klassifikation der Dissoziativen Identitätsstörung | DIS | 0.49 | 1 | 53 | 1 | stated in 1 doc(s) ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L79] |
| Heisenbergsche Unschärferelation | Unschärfe | 0.49 | 4 | 16 | 3 | stated in 1 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L80] |
| Kryptographische Zertifikate | ROAs | 0.49 | 1 | 1 | 1 | stated in 1 doc(s) ^[digitale-uberwelt.md:L49] |
| RS | Universe | 0.49 | 23 | 76 | 21 | stated in 1 doc(s) ^[duale-storyform-synthese-kohaerenz-protokoll.md:L92] |
| Anscheinend Normale Teil | ANP | 0.48 | 1 | 145 | 1 | stated in 1 doc(s) ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:L247] ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:L303] |
| Modulfunktionen und Konformer Feldtheorie | CFT | 0.48 | 1 | 25 | 1 | stated in 1 doc(s) ^[konzeptanalyse-kohaerenz-protokoll-s-fundament.md:L70] |
| Kaels Fragmentierung | DID | 0.48 | 25 | 100 | 17 | stated in 1 doc(s) ^[konzeptanalyse-kohaerenz-protokoll-s-fundament.md:L197] |
| Worldbuilding der Dual-Kernel-Theorie | DKT | 0.48 | 1 | 60 | 1 | stated in 1 doc(s) ^[hard-sf-roman-outline-dkt-physik-cosmic-horror.md:L19] |
| Fels | ZKP | 0.48 | 4 | 5 | 1 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-analyse.md:L146] |
| ISH | Gatekeeper | 0.48 | 24 | 66 | 14 | stated in 1 doc(s) ^[the-coherence-protocol-a-world-bible.md:L125] |
| Guardian-zu-Guardian Kommunikation | ZTEM-Konformität | 0.48 | 1 | 1 | 1 | stated in 1 doc(s) ^[digitale-uberwelt.md:L27] |
| HSOS | Homepages | 0.48 | 1 | 4 | 1 | stated in 1 doc(s) ^[juristische-recherche-zu-kptbs-dis.md:L678] |
| IIT | Model of Consciousness | 0.48 | 29 | 1 | 1 | stated in 1 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1173] ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1239] |
| Schattenlabyrinth | KW3 | 0.48 | 3 | 69 | 2 | stated in 1 doc(s) ^[welten.md:L67] |
| RS | Physics | 0.48 | 23 | 105 | 22 | stated in 1 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L95] |
| Audit | M4 | 0.47 | 17 | 4 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-duale-dramatica-storyform-synthese.md:L166] |
| R-ADR-07 | Context Rot | 0.47 | 1 | 5 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L463] |
| Trauma-Modell der Dissoziativen Identitätsstörung | DID | 0.47 | 1 | 100 | 1 | stated in 1 doc(s) ^[aegis-logik-und-erzaehlstruktur.md:L225] |
| Möglichkeiten | E5 | 0.47 | 115 | 2 | 2 | stated in 1 doc(s) ^[roman-outline-system-kael.md:L278] |
| Emotionalen Teil | EP | 0.47 | 2 | 140 | 2 | stated in 1 doc(s) ^[tsdp-analyse-kaels-innere-welt.md:L23] |
| FEP | Friston | 0.47 | 10 | 6 | 3 | stated in 1 doc(s) ^[spannungsfelder-und-aegis-meta-framework-analyse-docx.md:L264] |
| Info-Ontologie | LoA | 0.47 | 1 | 3 | 1 | stated in 1 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L529] |
| KI-Modelle | LLMs | 0.47 | 5 | 26 | 3 | stated in 1 doc(s) ^[aegis-seele-und-entropie.md:L216] |
| TSDP | Psychological Modularity | 0.47 | 151 | 1 | 1 | stated in 1 doc(s) ^[technical-audit-research-mandate-the-kohaerenz-protokoll-fra.md:L9] |
| RS | SS | 0.47 | 23 | 19 | 1 | stated in 1 doc(s) ^[dramatica-storyform-validierung-und-synthese.md:L32] |
| Persönlichkeitsanteils | ANP | 0.46 | 5 | 145 | 3 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzept.md:L254] |
| Autopoietische Netzwerk | Modell Beta | 0.46 | 1 | 1 | 1 | stated in 1 doc(s) ^[logiksystem-aegis-entwicklungsszenarien-docx.md:L177] |
| DAOs | Organisationen | 0.46 | 2 | 11 | 2 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L94] |
| V-Verbindung | Kael-Juna | 0.46 | 16 | 25 | 4 | stated in 1 doc(s) ^[kohaerenz-protokoll-themenanalyse-und-anreicheru.md:L201] |
| Kohärenz-Kernel | K₁ | 0.46 | 22 | 24 | 3 | stated in 1 doc(s) ^[dkt-fundament-kohaerenz-protokoll-md.md:L21] |
| We | Relationship Story | 0.46 | 80 | 24 | 7 | stated in 1 doc(s) ^[dramatica-dual-storyform-mapping-protokoll.md:L52] |
| AEGIS-Hub | E0 | 0.45 | 1 | 1 | 1 | stated in 1 doc(s) ^[roman-outline-system-kael.md:L191] |
| AExam | RS-AExam | 0.45 | 1 | 1 | 1 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L299] |
| ALife | Lebens | 0.45 | 1 | 61 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-inkubation-x.md:L79] |
| ASDS-1b | OSDD-1b | 0.45 | 1 | 1 | 1 | stated in 1 doc(s) ^[roman-konzept-kael-aegis-simulation.md:L77] |
| DES-T | DES-Taxon | 0.45 | 1 | 1 | 1 | stated in 1 doc(s) ^[dissoziative-identitaetsstoerung-unsichtbare-diagnose.md:L43] |
| Darstellung der Dissoziativen Identitätsstörung | DID | 0.45 | 3 | 100 | 2 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L19] |
| Umgebungen | EST | 0.45 | 68 | 12 | 6 | stated in 1 doc(s) ^[dialetheismus-im-kohaerenz-protokoll.md:L220] |
| Motivationsexklusion | INV-03 | 0.45 | 1 | 1 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L289] |
| Rauschen | K₀ | 0.45 | 186 | 26 | 16 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L51] |
| SS | MC and IC | 0.45 | 19 | 3 | 2 | stated in 1 doc(s) ^[dramatica-agentic-storyform-interactive-novel.md:L58] |
| P1 | No-Trust | 0.45 | 7 | 7 | 1 | stated in 1 doc(s) ^[aegis-philosophie-und-manifest-entwicklung.md:L39] ^[aegis-philosophie-und-manifest-entwicklung.md:L42] |
| Alltagsbewältigung | ANP | 0.44 | 25 | 145 | 19 | stated in 1 doc(s) ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L71] |
| DKT | Verknüpfung der Dual-Kernel Theory | 0.44 | 60 | 1 | 1 | stated in 1 doc(s) ^[dramatica-storyform-synthese-aegis-analyse-2.md:L17] |
| Q10 | Hard Problem | 0.44 | 2 | 34 | 1 | stated in 1 doc(s) ^[coherence-critique-and-question-generation.md:L285] |
| SEG6 | StellungnahmeverfahrenAuswertung2024-05-06alleStellungnahmen | 0.44 | 1 | 0 | 0 | stated in 1 doc(s) ^[sozialrechtliche-begutachtung-komplexer-traumafolgestoerunge.md:L587] |
| Versorgungsmedizinischen Grundsätze | VMV | 0.44 | 5 | 3 | 3 | stated in 1 doc(s) ^[juristische-recherche-zu-kptbs-dis.md:L19] ^[juristische-recherche-zu-kptbs-dis.md:L43] |
| CDM-Modell | Standardmodell der Kosmologie | 0.43 | 1 | 1 | 1 | stated in 1 doc(s) ^[fragen-zu-existenz-agency-und-realitaet.md:L227] |
| EST | Umwelt-Manifestationen | 0.43 | 12 | 1 | 1 | stated in 1 doc(s) ^[parakonsistente-logik-fuer-kohaerenz-protokoll.md:L276] |
| Verteidigungsnetzwerks der Grenzfeste | KW3 | 0.43 | 1 | 69 | 1 | stated in 1 doc(s) ^[lokalitaeten-konzept-fuer-roman-simulation.md:L287] |
| Konsistenz | LNC | 0.43 | 154 | 3 | 3 | stated in 1 doc(s) ^[dialetheismus-im-kohaerenz-protokoll.md:L178] |
| Mustererkennung | NET | 0.43 | 36 | 3 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll.md:L1662] |
| Algorithmische Melancholie | AEGIS | 0.42 | 25 | 269 | 25 | stated in 1 doc(s) ^[projektanalyse-kohaerenz-protokoll-dis.md:L197] |
| R-ADR-08 | CQ Interface | 0.42 | 1 | 1 | 1 | stated in 1 doc(s) ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:L464] |
| K₀ Kernel | Collapse | 0.42 | 1 | 69 | 1 | stated in 1 doc(s) ^[project-status-report-kohaerenz-protokoll-canonical-state-st.md:L24] |
| EPR | Teilchen | 0.42 | 15 | 41 | 8 | stated in 1 doc(s) ^[hard-sf-roman-outline-dkt-physik-cosmic-horror.md:L31] |
| Kohärenz-Kernels | K₁ | 0.42 | 3 | 24 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L31] |
| LBeWuSt | LitTheo | 0.42 | 1 | 1 | 1 | stated in 1 doc(s) ^[narrative-kernentwicklung-aegis-und-system-kael.md:L288] |
| Rekursiven Konsistenzvalidierung | RCV | 0.42 | 1 | 12 | 1 | stated in 1 doc(s) ^[aegis-philosophische-und-systemtheoretische-analyse-docx.md:L141] |
| Wade | Wade-Cortex2009-45-243-255-1 | 0.42 | 2 | 0 | 0 | stated in 1 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L1428] |
| Aharonov-Lebowitz | PAL | 0.41 | 3 | 4 | 3 | stated in 1 doc(s) ^[systemic-architecture-specification-the-coherence-protocol-w.md:L15] |
| EST | Umgebungsdesign | 0.41 | 12 | 4 | 2 | stated in 1 doc(s) ^[dialetheismus-im-kohaerenz-protokoll.md:L257] |
| Potentialität und Fluktuationen | ZPE | 0.41 | 1 | 2 | 1 | stated in 1 doc(s) ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L491] |
| Baby-Monster-Welt | Kernwelt B | 0.40 | 2 | 4 | 1 | stated in 1 doc(s) ^[kernwelten-fuer-kohaerenz-protokoll.md:L283] ^[kernwelten-fuer-kohaerenz-protokoll.md:L464] |
| KW3 | Cerberus Labyrinth | 0.40 | 69 | 1 | 1 | stated in 1 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L447] |
| DKT | Thermodynamics and Dual-Kernel Theory | 0.40 | 60 | 1 | 1 | stated in 1 doc(s) ^[technical-audit-research-mandate-the-kohaerenz-protokoll-fra.md:L3] |
| Störungen | F44 | 0.40 | 87 | 7 | 7 | stated in 1 doc(s) ^[juristische-recherche-zu-kptbs-dis.md:L265] |
| KG-gestützte RAG | KG-RAG | 0.40 | 1 | 1 | 1 | stated in 1 doc(s) ^[ki-agenten-kohaerenz-und-prompt-generierung.md:L121] |
| KW4 | Raum des Kairos-Potentialis | 0.40 | 68 | 0 | 0 | stated in 1 doc(s) ^[dramatica-und-kohaerenz-protokoll-analyse.md:L163] |
| MBO-Ä | Ärzte | 0.40 | 3 | 11 | 3 | stated in 1 doc(s) ^[rechtliche-analyse-entlassungsbericht-und-dis.md:L66] |
| Überwelt | KW1 | 0.39 | 82 | 81 | 35 | stated in 1 doc(s) ^[lokalitaeten-konzept-fuer-roman-simulation.md:L413] |
| Kishōtenketsu-Struktur | Ki-Shō-Ten-Ketsu | 0.39 | 4 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-duale-dramatica-storyform-synthese.md:L30] |
| Erinnerungslandschaft | E2 | 0.38 | 3 | 25 | 1 | stated in 1 doc(s) ^[roman-outline-system-kael.md:L104] ^[roman-outline-system-kael.md:L276] |
| EPf | EPs | 0.38 | 1 | 142 | 1 | stated in 1 doc(s) ^[juna-kael-system-analyse-und-rettungsplan-docx.md:L65] |
| ISH | Mediator | 0.38 | 24 | 13 | 4 | stated in 1 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L219] |
| K₁ Kernel | Coherence | 0.37 | 1 | 119 | 1 | stated in 1 doc(s) ^[project-status-report-kohaerenz-protokoll-canonical-state-st.md:L23] |
| UNM | Dramatica Storyform | 0.37 | 4 | 17 | 1 | stated in 1 doc(s) ^[dramatica-agentic-storyform-interactive-novel.md:L335] |
| Risse | KW2 | 0.37 | 164 | 75 | 57 | stated in 1 doc(s) ^[lokalitaeten-konzept-fuer-roman-simulation.md:L412] |
| Kael | TSDP | 0.37 | 251 | 151 | 147 | stated in 1 doc(s) ^[romanarchitektur-kael-aegis-entropie-docx.md:L168] ^[romanarchitektur-kael-aegis-entropie-docx.md:L383] |
| Conway Gruppe | Co1 | 0.36 | 1 | 12 | 1 | stated in 1 doc(s) ^[monstergruppe-narrative-cluster-und-metaphern.md:L281] |
| Typentheorie | HoTT | 0.36 | 5 | 1 | 1 | stated in 1 doc(s) ^[aegis-protokolle-kritische-evaluation-neukonzeption.md:L191] |
| IC | Ability | 0.35 | 39 | 14 | 12 | stated in 1 doc(s) ^[kohaerenz-protokoll-dramatica-synthese.md:L208] |
| ANP | Alltag | 0.32 | 145 | 42 | 28 | stated in 1 doc(s) ^[hard-sf-roman-outline-dkt-physik-cosmic-horror.md:L50] |
| Ängste | E4 | 0.26 | 53 | 1 | 1 | stated in 1 doc(s) ^[roman-outline-system-kael.md:L279] |
| C-PTSD | Complex Post-Traumatic Stress Disorder | 0.99 | 7 | 3 | 1 | proposed |
| GWP | Global Work Packages | 0.98 | 2 | 2 | 2 | proposed |
| MSE | Mental Status Examination | 0.96 | 1 | 1 | 1 | proposed |
| ML | Machine-Learning | 0.93 | 6 | 2 | 0 | proposed |
| Turing-Maschine | TM | 0.92 | 2 | 1 | 0 | proposed |
| Tera-Elektronenvolt | TeV | 0.79 | 1 | 2 | 1 | proposed |
| Benutzeroberfläche | UI | 0.78 | 6 | 3 | 1 | proposed |
| GAF | Global Assessment of Functioning | 0.77 | 1 | 1 | 1 | proposed |
| Internationalen Klassifikation der Krankheiten | ICD | 0.74 | 1 | 14 | 1 | proposed |
| Korrespondenz | Corresp | 0.70 | 42 | 1 | 1 | proposed |
| Gehirn-Computer-Schnittstellen | BCI | 0.69 | 1 | 2 | 1 | proposed |
| Landschaft | Resonanz-Landschaft | 0.61 | 83 | 23 | 23 | proposed |
| Juli | Jul | 0.58 | 10 | 1 | 0 | proposed |
| Komplexe PTBS | Complex Post-Traumatic Stress Disorder | 0.55 | 8 | 3 | 0 | proposed |
| Labor | Lab | 0.46 | 20 | 28 | 5 | proposed |
| Labor | lab | 0.44 | 20 | 3 | 0 | proposed |
| Ritual des Unburdening | Unburdening | 0.43 | 1 | 12 | 1 | proposed |
| Richtlinien des Gemeinsamen Bundesausschusses | Richtlinien | 0.39 | 1 | 17 | 1 | proposed |
| Unmodellierbarkeit | Unmodellierbarkeit des Subjektiven | 0.35 | 2 | 2 | 2 | proposed |

## Variants — 250

Same entity, same language: spelling, inflection, plural.

| a | b | p | docs (de) | docs (en) | docs (both) | evidence |
|---|---|--:|--:|--:|--:|---|
| Alignment-Problem | Alignment Problem | 1.00 | 7 | 21 | 4 | proposed |
| Flucht-Reaktion | Fluchtreaktion | 1.00 | 5 | 2 | 1 | proposed |
| Maximal-Plotter | Maximal Plotter | 1.00 | 9 | 1 | 1 | proposed |
| Resonanz-Landschaft | Resonanzlandschaft | 1.00 | 23 | 2 | 0 | proposed |
| Coheron-Echo | Coheron Echo | 0.99 | 7 | 1 | 0 | proposed |
| Ereignishorizont | Ereignishorizonts | 0.99 | 20 | 9 | 7 | proposed |
| Vertex-Operator Algebra | Vertex operator algebra | 0.99 | 1 | 3 | 0 | proposed |
| Vortex-Inversion | Vortex Inversion | 0.99 | 11 | 4 | 2 | proposed |
| augmented | Augmented | 0.98 | 3 | 11 | 1 | proposed |
| Cerberus-Labyrinth | Cerberus Labyrinth | 0.98 | 47 | 1 | 1 | proposed |
| Gödel-Gambit | Gödel Gambit | 0.98 | 42 | 8 | 3 | proposed |
| IC-Throughline | IC Throughline | 0.98 | 4 | 3 | 0 | proposed |
| Modules | Module | 0.97 | 7 | 32 | 0 | proposed |
| Tarskis | Tarski | 0.97 | 6 | 12 | 4 | proposed |
| Tarskis | Tarski's | 0.97 | 6 | 2 | 2 | proposed |
| Circuit-Breaking | Circuit Breaking | 0.96 | 1 | 1 | 1 | proposed |
| Vakuums | Vacuum | 0.96 | 5 | 7 | 2 | proposed |
| Antagonist-System | Antagonist System | 0.95 | 1 | 2 | 0 | proposed |
| Core | CORE | 0.95 | 105 | 24 | 4 | proposed |
| MC-Problem | MC Problem | 0.95 | 1 | 10 | 1 | proposed |
| Race-Condition | Race Conditions | 0.95 | 1 | 3 | 0 | proposed |
| Reader Response | Reader-Response | 0.95 | 2 | 6 | 2 | proposed |
| State-Freezing | State Freezing | 0.95 | 6 | 3 | 3 | proposed |
| Unendliche Auflösung | unendliche Auflösung | 0.95 | 1 | 1 | 0 | proposed |
| Dramatica-Matrix | Dramatica Matrix | 0.94 | 4 | 1 | 1 | proposed |
| Ego-Tunnel | Ego Tunnel | 0.94 | 1 | 1 | 1 | proposed |
| Exiles | Exile | 0.94 | 24 | 18 | 13 | stated in 1 doc(s) ^[isomorphe-architektur-der-realitaet-synthese-bericht.md:L140]; proposed |
| MC-Throughline | MC Throughline | 0.94 | 7 | 3 | 2 | proposed |
| Story Point | Storypoint | 0.94 | 2 | 9 | 0 | proposed |
| Storypoints | Story Points | 0.94 | 9 | 3 | 2 | proposed |
| Tarskis | Tarski’s | 0.94 | 6 | 2 | 1 | proposed |
| Conway Gruppe | Conway-Gruppe | 0.93 | 1 | 8 | 1 | proposed |
| predictive | PREDICTIVE | 0.93 | 20 | 5 | 2 | proposed |
| Posttraumatic Growth | Post Traumatic Growth | 0.93 | 1 | 2 | 0 | proposed |
| Rationaler ANP | Rationale ANP | 0.93 | 4 | 1 | 1 | proposed |
| Urknall | urknall | 0.93 | 12 | 1 | 1 | proposed |
| invalid | Invalid | 0.92 | 5 | 8 | 2 | proposed |
| Radikal | Radikale | 0.92 | 6 | 10 | 1 | proposed |
| Reentry | Re-entry | 0.92 | 4 | 1 | 0 | proposed |
| Bunker | Bunkers | 0.91 | 23 | 6 | 5 | proposed |
| Dramatica-Storyform | Dramatica Storyform | 0.91 | 8 | 17 | 6 | proposed |
| Feedback-Loops | Feedback Loops | 0.91 | 11 | 16 | 9 | proposed |
| JSON-Schema | JSON Schema | 0.91 | 10 | 3 | 2 | proposed |
| Managers | Manager | 0.91 | 17 | 53 | 16 | stated in 1 doc(s) ^[kohaerenz-protokoll-thematische-tiefenanalyse.md:L116]; proposed |
| polyvagal | Polyvagal | 0.91 | 3 | 6 | 3 | proposed |
| ANP-Host | ANP Host | 0.90 | 7 | 1 | 0 | proposed |
| Moonshine | MOONSHINE | 0.90 | 126 | 5 | 5 | proposed |
| Predictive | PREDICTIVE | 0.90 | 15 | 5 | 0 | proposed |
| Protektors | Protector | 0.90 | 2 | 41 | 1 | proposed |
| Vertexoperatoralgebra | Vertex Operator Algebra | 0.90 | 4 | 7 | 0 | proposed |
| preserve | PRESERVE | 0.89 | 26 | 8 | 2 | proposed |
| Protektor-ANP | Protector ANP | 0.89 | 3 | 2 | 0 | proposed |
| Unreliable narrator | Unreliable Narrator | 0.89 | 4 | 14 | 3 | proposed |
| Fight-Reaktion | Kampfreaktion | 0.88 | 1 | 2 | 0 | proposed |
| Julia | Juna | 0.88 | 25 | 192 | 7 | stated in 1 doc(s) ^[kohaerenz-protokoll-weltkonzept-synthese.md:L95] ^[kohaerenz-protokoll-weltkonzept-synthese.md:L96] |
| Landschaft | Resonanzlandschaft | 0.88 | 83 | 2 | 0 | proposed |
| Objekt | Objects | 0.88 | 101 | 10 | 3 | proposed |
| Preserve | PRESERVE | 0.88 | 1 | 8 | 0 | proposed |
| Storymind | Story Mind | 0.88 | 20 | 27 | 15 | proposed |
| Vertex-Operator-Algebra | Vertex operator algebra | 0.88 | 13 | 3 | 1 | proposed |
| Vertex-Operator Algebra | vertex operator algebra | 0.88 | 1 | 1 | 0 | proposed |
| Feedback-Loop | Feedback Loop | 0.87 | 7 | 8 | 4 | proposed |
| Mosaik-AEGIS | Wir-AEGIS | 0.87 | 2 | 3 | 2 | stated in 2 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L283] ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L1199] |
| jungian | Jungian | 0.86 | 12 | 13 | 12 | proposed |
| Kreativer | Kai | 0.85 | 4 | 10 | 3 | stated in 3 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik.md:L296] ^[kael-charakterarchitektur-und-konfliktdynamik.md:L297] |
| Reenactment | Re-enactment | 0.85 | 3 | 1 | 1 | proposed |
| Fleck | Flecken | 0.84 | 35 | 43 | 13 | proposed |
| Frame-Problem | Frame Problem | 0.84 | 4 | 4 | 2 | proposed |
| Intuitiver | Intuitive | 0.84 | 4 | 10 | 4 | proposed |
| Kaels | Kael's | 0.84 | 153 | 82 | 21 | proposed |
| Uncanny valley | Uncanny Valley | 0.84 | 3 | 16 | 3 | proposed |
| Vertexoperatoralgebra | Vertex operator algebra | 0.84 | 4 | 3 | 0 | proposed |
| Dorsaler | Dorsal | 0.83 | 1 | 3 | 0 | proposed |
| Radikale | Radical | 0.83 | 10 | 7 | 0 | proposed |
| Vertex-Operator-Algebra | Vertex Operator Algebra | 0.83 | 13 | 7 | 2 | proposed |
| Lichtfunke | Echo | 0.82 | 1 | 81 | 1 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L606] ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L648] |
| Reintegration | Re-Integration | 0.82 | 11 | 6 | 0 | proposed |
| JSON schema | JSON-Schema | 0.79 | 3 | 10 | 1 | proposed |
| Ursprungs-Ichs | Kael | 0.79 | 17 | 251 | 15 | stated in 2 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L369] ^[ki-rolle-aegis-genesis-fragestellungen.md:L346] |
| Prompt-Engineering | Prompt Engineering | 0.79 | 7 | 1 | 0 | proposed |
| Unbekanntes | unbekannte | 0.79 | 16 | 27 | 8 | proposed |
| Komplexen Adaptiven Systemen | CAS | 0.78 | 2 | 15 | 2 | stated in 1 doc(s) ^[narrative-plot-exploration-existenzielle-kohaerenz.md:L97] |
| Grenzfestung | Cerberus-Labyrinth | 0.77 | 1 | 47 | 1 | stated in 1 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L238] |
| unreliable narrator | Unreliable Narrator | 0.76 | 2 | 14 | 1 | proposed |
| Digitale Philosophie | Digitale Physik | 0.75 | 1 | 10 | 1 | stated in 1 doc(s) ^[physik-fuer-simulierte-realitaet.md:L141] |
| Unzerlegbarkeit | unzerlegbar | 0.75 | 2 | 2 | 1 | proposed |
| Chinesische | Chinese | 0.74 | 5 | 5 | 3 | proposed |
| Entropie | Rissen | 0.73 | 152 | 67 | 46 | stated in 1 doc(s) ^[orte-konzept-fuer-kohaerenz-protokoll.md:L548] |
| Unbekanntes | unbekannt | 0.73 | 16 | 23 | 4 | proposed |
| Algorithmische Komplexität | Kolmogorov-Komplexität | 0.72 | 2 | 10 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptionelle-ausarbeitung.md:L254] |
| Binden | Bind | 0.72 | 1 | 9 | 0 | proposed |
| Kael-System | Kael system | 0.72 | 22 | 4 | 0 | proposed |
| SGP | Symbol Grounding Problems | 0.72 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L107] |
| Gödelian | GÖDELIAN | 0.71 | 6 | 2 | 0 | proposed |
| Gödel's | Gödels | 0.70 | 45 | 53 | 23 | proposed |
| Partnerin | Partner | 0.70 | 15 | 25 | 4 | proposed |
| Schemata | Schemas | 0.70 | 13 | 5 | 2 | proposed |
| autonom | Autonomous | 0.69 | 22 | 67 | 10 | proposed |
| Gatekeepern | Gatekeepers | 0.69 | 1 | 3 | 0 | proposed |
| P versus NP Problem | P_versus_NP_problem | 0.69 | 1 | 5 | 1 | proposed |
| Alters | Anteils | 0.68 | 91 | 45 | 10 | stated in 1 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L60] |
| Meta-Kognitiv | Meta-cognitive | 0.68 | 7 | 1 | 0 | proposed |
| Trauma-Echos | Trauma Echoes | 0.68 | 5 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L101]; proposed |
| Unerwartete Verbindungen | unerwartete Verbindungen | 0.68 | 1 | 5 | 0 | proposed |
| Chaos | Zerfalls | 0.67 | 214 | 23 | 23 | stated in 1 doc(s) ^[kohaerenz-protokoll-2.md:L135] |
| Systemhütern | Guardians | 0.67 | 1 | 88 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzept.md:L29] |
| Kaels | Host | 0.67 | 153 | 96 | 53 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptentwicklung.md:L73] |
| Rationaler | Rational | 0.67 | 5 | 9 | 0 | proposed |
| binden | Bind | 0.66 | 10 | 9 | 0 | proposed |
| Core-Trauma | Core Trauma | 0.66 | 1 | 2 | 0 | proposed |
| Fakten | FACT | 0.66 | 46 | 1 | 1 | proposed |
| NPCs | Nichtspielercharakteren | 0.66 | 11 | 1 | 1 | stated in 1 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L75] |
| Resonanzlandschaft | Resonance-Landscape | 0.66 | 2 | 1 | 0 | proposed |
| Subroutinen | sub-routines | 0.66 | 21 | 2 | 0 | proposed |
| Präokkupiert | Unsicher-Ängstlich | 0.65 | 3 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-thematische-tiefenanalyse.md:L137] |
| Radikaler | Radical | 0.65 | 5 | 7 | 0 | proposed |
| Sporadische | Sporadic | 0.65 | 7 | 9 | 5 | proposed |
| Sorites-Paradoxon | Sorites-Paradox | 0.64 | 3 | 3 | 0 | proposed |
| unitary | Unitary | 0.64 | 4 | 6 | 4 | proposed |
| BSG | Bundessozialgerichts | 0.63 | 5 | 4 | 4 | stated in 1 doc(s) ^[sozialrechtliche-strategien-bei-traumafolgestoerungen.md:L392] |
| Chaos | Traumata | 0.63 | 214 | 82 | 60 | stated in 1 doc(s) ^[charakter-kompilation-fuer-kohaerenz-protokoll.md:L54] |
| Parias | Pariahs | 0.63 | 4 | 8 | 2 | proposed |
| Unbekanntes | Unbekannt | 0.63 | 16 | 11 | 3 | proposed |
| Unbewusst | unbewusst | 0.63 | 6 | 39 | 3 | proposed |
| Alters | Fragmenten | 0.62 | 91 | 49 | 17 | stated in 2 doc(s) ^[monstergruppe-primzahlen-plot-neukonstruktion.md:L122] ^[monstergruppe-primzahlen-plot-neukonstruktion-2.md:L120] |
| Programms | Program | 0.62 | 8 | 5 | 0 | proposed |
| Bürgerlichen Gesetzbuches | BGB | 0.61 | 1 | 7 | 1 | stated in 1 doc(s) ^[dis-berichtigung-umfassende-recherche-und-schreiben.md:L121] |
| Konnektive | Junktoren | 0.61 | 2 | 3 | 1 | stated in 1 doc(s) ^[dialetheismus-im-kohaerenz-protokoll.md:L108] |
| Maschinen | Machine | 0.61 | 19 | 42 | 4 | proposed |
| Makrozustand | Zustand | 0.61 | 1 | 235 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptionelle-ausarbeitung.md:L84] |
| Overworld | OVERWORLD | 0.61 | 10 | 2 | 2 | proposed |
| Unentscheidbar | Unentscheidbarkeit | 0.61 | 1 | 16 | 1 | proposed |
| Kaskaden | Cascade | 0.60 | 5 | 6 | 0 | proposed |
| Immobilisierung | Immobilisation | 0.60 | 1 | 1 | 0 | proposed |
| Kairos | Sophias | 0.59 | 78 | 6 | 5 | stated in 3 doc(s) ^[orte-konzept-fuer-kohaerenz-protokoll.md:L318] ^[umfassendes-lokalitaeten-konzept-fuer-roman.md:L446] |
| Vita3K | Vita3K-Android | 0.59 | 1 | 1 | 1 | stated in 1 doc(s) ^[gravitational-architecture-novel-structure.md:L445] |
| Intuitives | Intuitive | 0.58 | 1 | 10 | 0 | proposed |
| intuitives | Intuitive | 0.58 | 13 | 10 | 1 | proposed |
| Komplexen Posttraumatischen Belastungsstörung | KPTBS | 0.58 | 1 | 2 | 1 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L43] |
| Programm | Programme | 0.58 | 28 | 11 | 3 | proposed |
| Resonanzverbindung | Verbindung | 0.58 | 7 | 213 | 7 | proposed |
| Traveling Salesman Problem | Traveling Salesperson Problem | 0.58 | 1 | 1 | 0 | proposed |
| Trauma-Wut | Aggression | 0.57 | 3 | 59 | 3 | stated in 1 doc(s) ^[forschungsauftrag-spannungspunktanalyse-und-charakterausarbe.md:L71] |
| Dorsaler | dorsal | 0.57 | 1 | 2 | 0 | proposed |
| Hyperativitätsstörung | ADHS | 0.56 | 1 | 5 | 1 | stated in 1 doc(s) ^[dis-komorbiditaeten-und-alltagsbewaeltigung.md:L225] |
| Dialetheien | Dialetheias | 0.56 | 4 | 3 | 0 | proposed |
| Isabella | Lia | 0.56 | 9 | 63 | 6 | stated in 1 doc(s) ^[protokoll-der-offenbarung.md:L672] ^[protokoll-der-offenbarung.md:L702] |
| Logik | Rigide Logik | 0.56 | 233 | 2 | 2 | proposed |
| Logiken | Parakonsistenz | 0.56 | 44 | 35 | 19 | stated in 1 doc(s) ^[narrativ-existenzieller-kohaerenz-nzt-protokoll.md:L141] |
| Protektors | protector | 0.56 | 2 | 30 | 0 | proposed |
| Subroutinen | subroutines | 0.56 | 21 | 4 | 0 | proposed |
| Kohärenz-Balancierung | ECR | 0.55 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L110] |
| Guardian-Interface-Protokolle | Verfeinert | 0.55 | 2 | 1 | 1 | stated in 1 doc(s) ^[digitale-uberwelt.md:L95] |
| Rationaler ANP | Lex | 0.55 | 4 | 127 | 4 | stated in 2 doc(s) ^[charaktere.md:L74] ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:L55] |
| Objekte | Object | 0.55 | 60 | 12 | 4 | proposed |
| polyphon | Polyphonic | 0.55 | 3 | 15 | 1 | proposed |
| Multiple Personality Disorder | Dissociative Identity Disorder | 0.54 | 2 | 44 | 2 | stated in 2 doc(s) ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L969] ^[dissoziative-identitaet-invalidierung-im-gesundheitssystem.md:L272] |
| Dissoziation der Persönlichkeit | STRUKTURELLE DISSOZIATION | 0.54 | 65 | 3 | 3 | stated in 3 doc(s) ^[system-kael-konzeptentwicklung-und-analyse.md:L275] ^[aegis-singularitaet-jenseits-entropiegleichung-2.md:L547] |
| Kleine | Echo | 0.54 | 31 | 81 | 12 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L315] |
| Fassade | Façade | 0.54 | 50 | 1 | 0 | proposed |
| Genesis-Event | genesis event | 0.54 | 2 | 1 | 0 | proposed |
| Kael | Strukturen | 0.54 | 251 | 171 | 114 | stated in 2 doc(s) ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L72] ^[aegis-genesis-krise-prosa-auftrag-formulieren-2.md:L72] |
| Nox | Persecutors | 0.54 | 16 | 4 | 2 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L328] ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L432] |
| Solarplexus | Solar Plexus | 0.54 | 3 | 1 | 1 | proposed |
| Cache Kohärenz | Cache-Coherence | 0.53 | 24 | 2 | 0 | proposed |
| E3 | Mnemosyne-Archive | 0.53 | 1 | 1 | 1 | stated in 1 doc(s) ^[roman-outline-system-kael.md:L37] ^[roman-outline-system-kael.md:L273] |
| Schwellenhüterin | Wächterin | 0.53 | 1 | 30 | 1 | stated in 1 doc(s) ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L263] |
| EP-Dynamiken | ANP | 0.52 | 1 | 145 | 1 | stated in 1 doc(s) ^[kael-system-tsdp-analyse-und-profile.md:L95] |
| Architektin | Architect | 0.52 | 3 | 11 | 0 | proposed |
| Ashbys Gesetz | Kontroll-Paradoxon | 0.52 | 5 | 3 | 2 | stated in 2 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L297] ^[ki-rolle-aegis-genesis-fragestellungen.md:L267] |
| Cerberus | Cerberus-Labyrinth | 0.52 | 85 | 47 | 47 | stated in 1 doc(s) ^[the-sensory-rulebook-the-body-as-a-measuring-device-in-the-p.md:L104] |
| Emergentes | Emergent | 0.52 | 12 | 55 | 5 | proposed |
| intuitiv | Intuitive | 0.52 | 46 | 10 | 4 | proposed |
| conscious | Conscious | 0.51 | 33 | 24 | 8 | proposed |
| Kontrollproblems | Control Problem | 0.51 | 4 | 5 | 3 | proposed |
| FEP | Free Energy Principles | 0.51 | 10 | 1 | 1 | stated in 1 doc(s) ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:L79] |
| GWD | GWT | 0.51 | 1 | 9 | 1 | stated in 1 doc(s) ^[emergenz-autonomer-systeme-aegis-forschung.md:L272] |
| Gesamtsystem der Persönlichkeit | Kael | 0.51 | 3 | 251 | 3 | stated in 1 doc(s) ^[kael-uberarbeitung-des-konzepts-unter-tsdp.md:L21] |
| Griess-Algebra | Griess algebra | 0.51 | 7 | 3 | 3 | proposed |
| Alters | Anteilen | 0.50 | 91 | 77 | 27 | stated in 1 doc(s) ^[aegis-logik-und-narrative-implikationen.md:L100] |
| Alters | Identitätsanteilen | 0.50 | 91 | 2 | 2 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L76] |
| Barriere | Barriers | 0.50 | 29 | 11 | 0 | proposed |
| fragil | Fragile | 0.50 | 30 | 10 | 4 | proposed |
| Kael-Juna-Verbindung | Kohärenz-Insel | 0.50 | 8 | 6 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-weltkonzept-synthese.md:L48] |
| Kiko | Kindes | 0.50 | 122 | 18 | 9 | stated in 1 doc(s) ^[roman-konzept-dualitaet-kohaerenz-spannung.md:L69] |
| unintended consequences | Unintended Consequences | 0.50 | 1 | 2 | 1 | proposed |
| EP-Fight | EP fight | 0.49 | 3 | 2 | 0 | proposed |
| Intuitiver | intuitive | 0.49 | 4 | 63 | 4 | proposed |
| Vermittlerin | Mediator | 0.49 | 7 | 13 | 0 | proposed |
| Logos-Prime | Cage of Logic | 0.48 | 62 | 2 | 2 | stated in 1 doc(s) ^[welcome-to-the-coherence-protocol-a-beginner-s-guide.md:L66] |
| Kohärenzbalancierung | ECR | 0.48 | 1 | 1 | 1 | stated in 1 doc(s) ^[aegis-emergenz-aus-der-leere.md:L163] |
| Logisches Gitter | Wahrheitsgitter | 0.48 | 1 | 1 | 1 | stated in 1 doc(s) ^[parakonsistente-logik-im-seelen-protokoll.md:L55] |
| Schalter | Switches | 0.48 | 7 | 14 | 1 | proposed |
| Kreativ-Intuitiver | Kai | 0.47 | 3 | 10 | 3 | stated in 3 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik.md:L183] ^[kael-charakterarchitektur-und-konfliktdynamik.md:L194] |
| Kammer | Speicher | 0.47 | 8 | 22 | 3 | stated in 1 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L1063] |
| Kontrollpunkte | Schleusen | 0.47 | 6 | 7 | 4 | stated in 1 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L368] |
| Subquotient | Sektion | 0.47 | 7 | 20 | 1 | stated in 1 doc(s) ^[monstergruppe-metapher-auf-mathematische-kohaerenz.md:L42] ^[monstergruppe-metapher-auf-mathematische-kohaerenz.md:L42] |
| Intuitiv | Intuitive | 0.46 | 2 | 10 | 1 | proposed |
| KI-Ethik | Kontrollproblems | 0.46 | 17 | 4 | 4 | stated in 1 doc(s) ^[genesis-krise-aegis-prosa-auftrag.md:L94] |
| Resonanz-Modulation | Modulation | 0.46 | 1 | 3 | 1 | proposed |
| Unentscheidbarkeit | unentscheidbar | 0.46 | 16 | 12 | 6 | proposed |
| ANP | Hosts | 0.45 | 145 | 18 | 14 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzept.md:L205] |
| Alters | Anteile | 0.45 | 91 | 112 | 35 | stated in 1 doc(s) ^[kohaerenz-protokoll-2.md:L131] |
| Bunkeranlagen | Bunkers | 0.45 | 2 | 6 | 2 | proposed |
| Resonanzkaskade | Kaskade | 0.45 | 12 | 37 | 7 | proposed |
| Kontrollpunkt | Übergangsschleuse | 0.45 | 3 | 1 | 1 | stated in 1 doc(s) ^[umfassendes-lokalitaeten-konzept-fuer-roman.md:L348] ^[umfassendes-lokalitaeten-konzept-fuer-roman.md:L352] |
| Rauschen | Statik | 0.45 | 186 | 6 | 6 | stated in 1 doc(s) ^[genesis-recherche-anleitung-umsetzung.md:L1077] |
| AEGIS | Antagonisten | 0.44 | 269 | 64 | 56 | stated in 4 doc(s) ^[dramatica-storyform-fuer-romananalyse.md:L342] ^[konzeptionelle-transzendenz-fuer-kohaerenz-protokoll.md:L254] |
| Alters | Guardians | 0.44 | 91 | 88 | 36 | stated in 1 doc(s) ^[m-als-fundament-der-simulation.md:L258] ^[m-als-fundament-der-simulation.md:L262] |
| Schattens | Firefighter | 0.44 | 10 | 15 | 5 | stated in 3 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik.md:L144] ^[kael-charakterarchitektur-und-konfliktdynamik-2.md:L144] |
| HPA-Achse | Stressachse | 0.44 | 4 | 1 | 1 | stated in 1 doc(s) ^[dissoziative-identitaetsstoerung-unsichtbare-diagnose.md:L251] |
| Resonanz-Nebel | Mnemosyne | 0.44 | 5 | 93 | 4 | stated in 2 doc(s) ^[kohaerenz-protokoll-weltkonzept-synthese.md:L85] ^[welten.md:L91] |
| Pixelierung | Raumzeit-Granularität | 0.44 | 5 | 2 | 2 | stated in 2 doc(s) ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L69] ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L82] |
| Anscheinend Normale Teile | ANPs | 0.43 | 2 | 122 | 2 | stated in 1 doc(s) ^[kael-charakterarchitektur-und-konfliktdynamik-2.md:L32] |
| Fluktuationen | Schwankungen | 0.43 | 40 | 15 | 5 | proposed |
| Harmonisierer | Resonanz-Harmonisierer | 0.43 | 11 | 2 | 2 | proposed |
| Juna | Vs | 0.43 | 192 | 9 | 8 | stated in 8 doc(s) ^[2-kohaerenz-protokoll-konzeptentwicklung.md:L222] ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L363] |
| Möglichkeitsstrom | KW4 | 0.43 | 4 | 68 | 2 | stated in 1 doc(s) ^[welten.md:L68] |
| Know | Knowing | 0.43 | 36 | 3 | 1 | stated in 1 doc(s) ^[monstergruppe-primzahlen-plot-blueprint.md:L472] |
| Existenzielle Angst | Angst | 0.42 | 8 | 170 | 8 | stated in 1 doc(s) ^[prosaversion-von-genesis-erstellen.md:L51] |
| DES-II | Dissociative Experiences Scale | 0.42 | 2 | 6 | 2 | stated in 1 doc(s) ^[dis-diagnose-klinische-ethische-rechtliche-analyse.md:L73] |
| AEGIS | Fundaments | 0.41 | 269 | 33 | 31 | stated in 1 doc(s) ^[konzeptionelle-transzendenz-fuer-kohaerenz-protokoll.md:L440] |
| Boris | Bruce | 0.41 | 4 | 3 | 3 | stated in 3 doc(s) ^[kohaerenz-protokoll-analyse-und-synthese.md:L404] ^[kohaerenz-protokoll-detaillierte-recherche.md:L391] |
| Kind-Alter | Child Alters | 0.41 | 2 | 2 | 0 | proposed |
| Dynamis | Dunamis | 0.41 | 1 | 2 | 0 | proposed |
| Isabelle | Lia | 0.41 | 50 | 63 | 42 | stated in 1 doc(s) ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L560] |
| Anteile | Teile | 0.40 | 112 | 157 | 66 | stated in 1 doc(s) ^[kohaerenz-protokoll-forschungsaufgabe.md:L278] |
| Metakognitiver | Metacognitive | 0.40 | 5 | 5 | 0 | proposed |
| Alters | Teile | 0.39 | 91 | 157 | 49 | stated in 1 doc(s) ^[flow-zustaende-und-dissoziative-identitaet.md:L207] |
| Barriere | barriers | 0.39 | 29 | 41 | 1 | proposed |
| THE AUTONOMOUS SUBSYSTEMS | THE GUARDIANS | 0.39 | 1 | 2 | 1 | stated in 1 doc(s) ^[aegis-manifest-genesis-krise-reboot-2.md:L161] |
| Aegis | Systems | 0.38 | 34 | 263 | 25 | stated in 2 doc(s) ^[logik-trifft-transzendente-entitaet.md:L69] ^[logik-trifft-transzendente-entitaet-2.md:L69] |
| Beobachter-Effekt | Quanten-Verschränkungs-Witness | 0.38 | 2 | 3 | 2 | stated in 2 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L379] ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L332] |
| Fragmentierungsnacht | Bruch | 0.38 | 3 | 70 | 2 | stated in 2 doc(s) ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L181] ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L439] |
| Genesis-Krise | T-734 Trauma | 0.38 | 57 | 1 | 1 | stated in 1 doc(s) ^[ki-prompt-analyse-hard-problem-of-consciousness.md:L235] |
| KW2 | Mnemosyne-Archipel | 0.38 | 75 | 51 | 40 | stated in 5 doc(s) ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L587] ^[projektplanung-fuer-kohaerenz-protokoll.md:L67] |
| Mikrozustände | Zustände | 0.38 | 2 | 174 | 2 | stated in 1 doc(s) ^[kohaerenz-protokoll-konzeptionelle-ausarbeitung.md:L84] |
| Ontologischer Einschluss | Schließung | 0.38 | 2 | 30 | 1 | stated in 1 doc(s) ^[aegis-philosophische-und-systemtheoretische-analyse-docx.md:L160] |
| Trauma-Lokus | Vergessener Schrein | 0.38 | 4 | 5 | 2 | stated in 1 doc(s) ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L198] ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L307] |
| Story Mind | AI Enhanced | 0.37 | 27 | 1 | 1 | stated in 1 doc(s) ^[kohaerenz-protokoll-system-realitaet-leser.md:L167] |
| Defamiliarisierung | Verfremdung des Bekannten | 0.36 | 1 | 1 | 1 | stated in 1 doc(s) ^[prosaversion-von-genesis-erstellen.md:L172] |
| Ängstlich-Vermeidend | Desorganisiert | 0.36 | 2 | 4 | 2 | stated in 2 doc(s) ^[beziehungsheilung-nach-trauma-konzeptpapier-2.md:L59] ^[beziehungsheilung-nach-trauma-konzeptpapier-3.md:L61] |
| Resonanzraum | Raum | 0.36 | 9 | 185 | 9 | proposed |
| Beobachtereffekt | Messproblem | 0.35 | 17 | 10 | 5 | stated in 2 doc(s) ^[paradoxien-der-kohaerenz-protokoll-entwicklung.md:L48] ^[existenzforschung-fuer-roman-kohaerenz-protokoll.md:L169] |
| Bewusstsein | Für-sich-Sein | 0.35 | 200 | 3 | 3 | stated in 1 doc(s) ^[aegis-genesis-krise-konzeptioneller-rahmen.md:L27] |
| Dissoziation | TSDP-Fragmentierung | 0.34 | 157 | 2 | 2 | stated in 1 doc(s) ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L814] |
| AEGIS | Logos-Prime | 0.33 | 269 | 62 | 62 | stated in 1 doc(s) ^[analyse-des-kohaerenz-protokolls.md:L218] |
| AdS | CFTcorrespondence | 0.32 | 8 | 0 | 0 | stated in 3 doc(s) ^[master-konzept-kohaerenz-protokoll-analyse.md:L299] ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L332] |
| Entropie | Informationsmenge | 0.32 | 152 | 6 | 5 | stated in 2 doc(s) ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L217] ^[holographisches-prinzip-fuer-kohaerenz-protokoll-2.md:L215] |
| Restatement-Mechanismus | M2 | 0.30 | 1 | 4 | 1 | stated in 1 doc(s) ^[dramatica-und-kohaerenz-protokoll-analyse.md:L19] |

## Not the same — 6205

Pairs a gloss or the model suggested and Jev placed as a role, a part, or a different thing, with the gloss that suggested them. Kept so a reader can overrule.

| a | b | relation | p | evidence |
|---|---|---|--:|---|
| Kairos | Sophia | distinct | 0.86 | stated ^[kohaerenz-protokoll-konzeptentwicklung.md:L33] |
| Juna | V-Verbindung | distinct | 0.51 | stated ^[kohaerenz-protokoll-themenanalyse-und-anreicheru.md:L42] |
| ANP | EP-Mix | role_or_part | 0.81 | stated ^[concept-paper-the-architectural-foundations-of-kohaerenz-pro.md:L147] |
| Host | Kael | role_or_part | 0.83 | stated ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L99] |
| Beobachter | Kritiker | role_or_part | 0.70 | stated ^[kohaerenz-prozess-grundlagen.md:L175] |
| Maturana | Varela | distinct | 0.99 | stated ^[kohaerenz-protokoll-konzeptentwicklung.md:L48] |
| AEGIS | Kael | distinct | 0.97 | stated ^[kohaerenz-protokoll-inkubation-x.md:L89] |
| Anima | Animus | distinct | 1.00 | stated ^[kohaerenz-protokoll-themenanalyse-und-anreicheru.md:L88] |
| Energie | Entropie | distinct | 0.99 | stated ^[kohaerenz-protokoll-umfassendes-konzept-mit-meta-clustern.md:L34] |
| ANP | Protector | role_or_part | 0.95 | stated ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L264] |
| AdS | CFT-Korrespondenz | distinct | 0.49 | stated ^[integriertes-kohaerenz-protokoll-erstellung.md:L76] |
| CFT | Feldtheorie | distinct | 0.40 | stated ^[monstergruppe-als-denkmodell-der-komplexitaet.md:L129] |
| Dialetheismus | Logik | distinct | 0.83 | stated ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L73] |
| Existenz | Nicht-Existenz | distinct | 0.99 | stated ^[kohaerenz-protokoll-umfassendes-konzept-mit-meta-clustern.md:L33] |
| Konstrukt-Stadt | LogOS | role_or_part | 0.56 | stated ^[kohaerenz-protokoll-2.md:L75] |
| ANP | Rationalist | role_or_part | 0.97 | stated ^[concept-paper-the-architectural-foundations-of-kohaerenz-pro.md:L138] |
| ANP-Host | Kael | role_or_part | 0.94 | stated ^[roman-outline-system-kael.md:L217] |
| Anteile | EPs | role_or_part | 0.42 | stated ^[integriertes-kohaerenz-protokoll-erstellung.md:L51] |
| EP | Kampf | role_or_part | 0.97 | stated ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1614] |
| Fight | Nyx | role_or_part | 0.81 | stated ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L422] |
| Freeze | Kiko | role_or_part | 0.93 | stated ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L422] |
| Inkohärenz | Kohärenz | distinct | 0.98 | stated ^[kohaerenz-protokoll-synthese-integration.md:L69] |
| Isolation | Kommunikation | distinct | 0.98 | stated ^[kohaerenz-protokoll-umfassendes-konzept-mit-meta-clustern.md:L35] |
| Julia | Kael | distinct | 0.76 | stated ^[kohaerenz-protokoll-aktuelle-gesamtkonzept-synthese.md:L15] |
| K0 | K1 | distinct | 0.93 | stated ^[forschungsprojekt-kohaerenz-protokoll-analyse.md:L148] |
| Kohärenz | Ordnung | distinct | 0.49 | stated ^[integriertes-kohaerenz-protokoll-erstellung.md:L39] |
| OS | Physics | distinct | 0.51 | stated ^[dramatica-storyform-kohaerenz-protokoll-analyse.md:L93] |
| Qualia | Stanford Encyclopedia of Philosophy | distinct | 0.88 | stated ^[genesis-aegis-und-logische-grenzen.md:L193] |
| AEGIS | Ordnung | distinct | 0.56 | stated ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L425] |
| ANP | Host | role_or_part | 0.54 | stated ^[kohaerenz-protokoll-konzept.md:L115] |
| ANP | Lex | role_or_part | 0.95 | stated ^[kohaerenz-protokoll-konzeptentwicklung.md:L158] |
| ANPs | EPs | distinct | 0.96 | stated ^[kohaerenz-prozess.md:L53] |
| Aggression | Nyx | role_or_part | 0.90 | stated ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1620] |
| Ambivalenz | Kind | role_or_part | 0.96 | stated ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1616] |
| Aristoteles | Tragödientheorie | distinct | 0.62 | stated ^[aegis-genesis-krise-konzeptioneller-rahmen.md:L277] |
| Bewusstseinsphilosophie | Minimales Selbst | role_or_part | 0.91 | stated ^[aegis-genesis-krise-konzeptioneller-rahmen.md:L250] |
| CFT | Feldtheorien | distinct | 0.37 | stated ^[kohaerenz-protokoll-audit-und-verifizierung.md:L109] |
| ChallengingSystemsThinkers | SystemTheory | role_or_part | 0.74 | stated ^[optimierter-prompt-fuer-kohaerenz-protokoll.md:L276] |
| Chaos | Lebendigkeit | distinct | 0.88 | stated ^[kohaerenz-protokoll-themenanalyse-und-anreicheru.md:L33] |
| EP | Fight | role_or_part | 0.98 | stated ^[project-coherence-protocol-a-canon-of-core-identity-and-anta.md:L38] |
| EP | Moros | role_or_part | 0.88 | stated ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1639] |
| EP-Kampf | Nyx | role_or_part | 0.81 | stated ^[roman-outline-system-kael.md:L217] |
| Emergent Properties | Stanford Encyclopedia of Philosophy | distinct | 0.60 | stated ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L467] |
| K-J Verbindung | Moonshine-Signatur | role_or_part | 0.84 | stated ^[monstergruppe-primzahlen-plot-blueprint.md:L33] |
| Kosmischer Horror | Lovecraft | role_or_part | 0.55 | stated ^[aegis-genesis-krise-konzeptioneller-rahmen.md:L146] |
| Lex | Rationalist | role_or_part | 0.46 | stated ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L364] |
| MC | Mind | distinct | 0.64 | stated ^[dramatica-storyform-kohaerenz-protokoll-analyse.md:L92] |
| Mutual Information | Transinformation | distinct | 0.84 | stated ^[dramatica-storyform-synthese-aegis-analyse.md:L17] |
| Paraconsistent Logic | Stanford Encyclopedia of Philosophy | distinct | 0.53 | stated ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L577] |
| Psychology | RS | role_or_part | 0.48 | stated ^[dramatica-storyform-kohaerenz-protokoll-analyse.md:L93] |
| Realität | Simulation | distinct | 0.84 | stated ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L32] |
| AEGIS | Ich | distinct | 0.52 | stated ^[aegis-genesis-krise-konzeptioneller-rahmen.md:L781] |
| AEGIS | Ursprungs-Ich | distinct | 0.58 | stated ^[aegis-genesis-krise-konzeptioneller-rahmen.md:L142] |
| ANP | Caregiver | role_or_part | 1.00 | stated ^[concept-paper-the-architectural-foundations-of-kohaerenz-pro.md:L140] |
| ANP-Logik | Lex | role_or_part | 0.91 | stated ^[roman-outline-system-kael.md:L217] |
| ANPs | Manager | role_or_part | 0.85 | stated ^[prompt-entwicklung-fuer-kohaerenz-erzaehlstrang.md:L110] |
| ARCHIVES | WIN2009 | role_or_part | 0.97 | stated ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L578] |
| AdS | CFT | distinct | 0.96 | stated ^[kohaerenz-protokoll-aktuelle-gesamtkonzept-synthese-abstrakt.md:L45] |
| Aktualität | Potentialität | distinct | 0.99 | stated ^[kohaerenz-protokoll-aktuelle-gesamtkonzept-synthese-abstrakt.md:L15] |
| Alters | Kael | role_or_part | 0.85 | stated ^[kohaerenz-protokoll-architecture-synthesis.md:L349] |
| Analyst | Lex | role_or_part | 0.72 | stated ^[an-introduction-to-the-concepts-of-coherence-protocol.md:L65] |
| Angst | EP-Kind | role_or_part | 0.95 | stated ^[roman-outline-system-kael.md:L217] |
| Angst | Kind | role_or_part | 0.96 | stated ^[charaktere.md:L44] |
| Anomalie | Eindämmung | distinct | 0.90 | stated ^[m-als-fundament-der-simulation.md:L120] |
| Berechenbarkeit | Gödel | distinct | 0.93 | stated ^[kohaerenz-protokoll-themenanalyse-und-anreicheru.md:L33] |
| Campbell | Vogler | distinct | 1.00 | stated ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L551] |
| Collapse | Moros | role_or_part | 0.85 | stated ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L422] |
| DID | Identitätsstruktur | role_or_part | 0.40 | stated ^[charaktere.md:L19] |
| Data-Science | Sneaky-AI-Specification-Gaming-and-the-Shortcomings-of-Machine | distinct | 0.60 | stated ^[kohaerenz-protokoll-analyse-und-synthese.md:L359] |
| Depersonalisation | Derealisation | distinct | 0.89 | stated ^[kernwelten-und-fragmentierte-wahrnehmung.md:L173] |
| Digital | Philosophy | distinct | 0.73 | stated ^[monstergruppe-primzahlen-plot-neukonstruktion.md:L219] |
| Dissoziation | Trauma | distinct | 0.86 | stated ^[kohaerenz-prozess.md:L297] |
| EP | Kampf-Reaktion | role_or_part | 0.90 | stated ^[kohaerenz-protokoll-analyse-und-synthese.md:L211] |
| Emergenz | Komplexität | distinct | 0.92 | stated ^[kohaerenz-protokoll-konzeptentwicklung.md:L301] |
| Entropie | Information | distinct | 0.99 | stated ^[paradoxien-der-kohaerenz-protokoll-entwicklung.md:L83] |
| Entropie | Risse | distinct | 0.49 | stated ^[orte-konzept-fuer-kohaerenz-protokoll.md:L239] |
| Externe Ebene | Juna | role_or_part | 0.93 | stated ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L235] |
| Flucht | Kind | role_or_part | 0.86 | stated ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1615] |
| Grenzen | Gödel | distinct | 0.96 | stated ^[kohaerenz-protokoll-thematische-tiefenanalyse.md:L176] |
| Gödel | Logik | distinct | 0.72 | stated ^[narrative-plot-exploration-existenzielle-kohaerenz.md:L372] |
| Hoffnungslosigkeit | Moros | role_or_part | 0.92 | stated ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1620] |
| Huntley | Phillips | distinct | 0.98 | stated ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L436] |
| IC | Mind | role_or_part | 0.63 | stated ^[dramatica-storyform-synthese-aegis-analyse.md:L39] |
| IC | Universe | distinct | 0.74 | stated ^[dramatica-dual-storyform-mapping-analyse.md:L133] |
| Ich | Kael | role_or_part | 0.62 | stated ^[genesis-prosa-ausformulierung-gesamt.md:L292] |
| KW2 | KW3 | distinct | 0.95 | stated ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L181] |
| Kael | Main Character | role_or_part | 0.70 | stated ^[kohaerenz-protokoll-architecture-synthesis.md:L347] |
| Kael | Mind | role_or_part | 0.81 | stated ^[dramatica-storyform-fuer-romananalyse.md:L49] |
| Kael | System | role_or_part | 0.68 | stated ^[kohaerenz-protokoll-themenanalyse-und-anreicheru.md:L124] |
| Kausalität | Zeit | distinct | 0.79 | stated ^[kohaerenz-protokoll-umfassendes-konzept-mit-meta-clustern.md:L34] |
| Kernwelten | Realitäten | role_or_part | 0.70 | stated ^[kohaerenz-protokoll-weltkonzept-synthese.md:L40] |
| Kybernetik | Systemtheorie | distinct | 0.98 | stated ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L346] |
| Kämpfer | Nyx | role_or_part | 0.87 | stated ^[charaktere.md:L39] |
| Logic | NP-Complete | distinct | 0.79 | stated ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L297] |
| Logic | NP-Search | distinct | 0.85 | stated ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L298] |
| Logic | P-Class | distinct | 0.69 | stated ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L295] |
| Luhmann | Systemtheorie | distinct | 0.55 | stated ^[kohaerenz-protokoll-konzeptentwicklung.md:L48] |
| MC | Universe | role_or_part | 0.65 | stated ^[dramatica-dual-storyform-mapping-analyse.md:L190] |
| Monstergruppe | Moonshine | distinct | 0.83 | stated ^[monstergruppe-als-denkmodell-der-komplexitaet.md:L204] |
| Nichts | Sein | distinct | 1.00 | stated ^[kohaerenz-protokoll-konzeptentwicklung.md:L64] |
| Prigogine | Strukturen | distinct | 0.90 | stated ^[emergenz-autonomer-systeme-aegis-forschung.md:L70] |
| Prozessphilosophie | Whitehead | distinct | 0.55 | stated ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L92] |
| Selbstorganisation | Systemgrenzen | role_or_part | 0.79 | stated ^[kohaerenz-protokoll-umfassendes-konzept-mit-meta-clustern.md:L33] |
| AEGIS | ANP | role_or_part | 0.45 | stated ^[analyse-des-kohaerenz-protokolls.md:L221] |
| AEGIS | Cerberus | role_or_part | 0.47 | stated ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L580] |
| AEGIS | Entität | role_or_part | 0.78 | stated ^[welten.md:L29] |
| AEGIS | Mnemosyne | distinct | 0.98 | stated ^[lokalitaeten-konzept-fuer-roman-simulation.md:L209] |
| AEGIS | Paradox | distinct | 0.54 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L300] |
| AEGIS | Paradoxon | distinct | 0.54 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L228] |
| AEGIS | Potentialmeer-Grenze | distinct | 0.51 | stated ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L93] |
| AEGIS | Simulation | role_or_part | 0.94 | stated ^[kohaerenz-protokoll-dramatica-synthese-masterkonzept.md:L104] |
| ANP | EP-Dynamik | distinct | 0.63 | stated ^[kohaerenz-protokoll-konzeptentwicklung.md:L44] |
| ANP | Intellektueller | role_or_part | 0.98 | stated ^[kohaerenz-protokoll-analyse-und-synthese.md:L213] |
| ANP-Pflege | Rhys | role_or_part | 0.98 | stated ^[roman-outline-system-kael.md:L217] |
| ANP-Regulator | Selene | role_or_part | 0.80 | stated ^[roman-outline-system-kael.md:L217] |
| Abjekte | Kristeva | distinct | 0.49 | stated ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L292] |
| Abwehr | Wächter | role_or_part | 0.40 | stated ^[p-vs-np-und-kohaerenz.md:L263] |
| Abwehrmechanismen | Psychoanalyse | role_or_part | 0.70 | stated ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L283] |
| Aharonov-Lebowitz | Page-Wootters | distinct | 0.78 | stated ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L61] |
| Alex | Beschützer | role_or_part | 0.87 | stated ^[roman-outline-system-kael.md:L135] |
| Alex | Protector | role_or_part | 0.50 | stated ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L369] |
| Alignment | Control | distinct | 0.93 | stated ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L407] |
| Allianz | Schutz | distinct | 0.60 | stated ^[roman-outline-system-kael.md:L220] |
| Allianz | Sicherheit | distinct | 0.63 | stated ^[roman-outline-system-kael.md:L221] |
| Amnesie | Dissoziation | role_or_part | 0.56 | stated ^[kohaerenz-protokoll-konzeptentwicklung.md:L73] |
| Analyse-Hub | Guardian | role_or_part | 0.79 | stated ^[roman-lokalitaeten-konzept-und-ausarbeitung-2.md:L244] |
| Analytiker | Primärer ANP | role_or_part | 0.90 | stated ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1621] |
| Anderem | Selbst | distinct | 0.99 | stated ^[kohaerenz-protokoll-forschungsaufgabe.md:L304] |
| Anderen | Nicht-Selbst | distinct | 0.58 | stated ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L410] |
| Anima | Eros | distinct | 0.98 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L50] |
| Animus | Logos | distinct | 0.97 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L50] |
| Archetype | Role | distinct | 0.66 | stated ^[kohaerenz-protokoll-the-official-project-handbook.md:L83] |
| Architekt | Logik | distinct | 0.37 | stated ^[p-vs-np-und-kohaerenz.md:L238] |
| BabyMonster | GroupTheory | role_or_part | 0.79 | stated ^[monstergruppe-babygruppe-und-kael.md:L246] |
| Big | Hubble-Volumen | distinct | 0.92 | stated ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L196] |
| Bindungs-Ambivalenz | Flucht | role_or_part | 0.66 | stated ^[forschungsauftrag-spannungspunktanalyse-und-charakterausarbe.md:L97] |
| Blindheit | Hybris | distinct | 0.87 | stated ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L456] |
| Bran | Bulk-Modell | role_or_part | 0.75 | stated ^[analyse-des-kohaerenz-protokolls.md:L78] |
| Bulk-Modell | M-Theorie | role_or_part | 0.64 | stated ^[analyse-des-kohaerenz-protokolls.md:L78] |
| CFT | VOA | distinct | 0.75 | stated ^[konzeptanalyse-kohaerenz-protokoll-s-fundament.md:L339] |
| Cerberus | Sicherheit | role_or_part | 0.88 | stated ^[system-kael-konzeptentwicklung-und-analyse.md:L54] |
| Cerberus | Verteidigung | role_or_part | 0.69 | stated ^[kohaerenz-protokoll-konzeptentwicklung.md:L419] |
| Change | Success | distinct | 0.92 | stated ^[duale-storyform-synthese-kohaerenz-protokoll.md:L15] |
| Chaos | Lähmung | distinct | 0.94 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L293] |
| Chaos | Trauma | distinct | 0.64 | stated ^[dramatica-storyform-fuer-romananalyse.md:L367] |
| Child | EP | role_or_part | 0.97 | stated ^[project-coherence-protocol-a-canon-of-core-identity-and-anta.md:L39] |
| Chinesisches | Problem | distinct | 0.96 | stated ^[kohaerenz-protokoll-aktuelle-gesamtkonzept-synthese.md:L44] |
| Collapse | EP | role_or_part | 0.83 | stated ^[project-coherence-protocol-a-canon-of-core-identity-and-anta.md:L42] |
| Conscious | Mind | role_or_part | 0.72 | stated ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L391] |
| Control | Fight | distinct | 0.90 | stated ^[concept-paper-the-architectural-foundations-of-kohaerenz-pro.md:L144] |
| DID | Kael | role_or_part | 0.77 | stated ^[aegis-paradoxon-konzeption-und-analyse.md:L223] |
| DID | OSDD | distinct | 1.00 | stated ^[2-kohaerenz-protokoll-konzeptentwicklung.md:L56] |
| DID | Psyche | role_or_part | 0.91 | stated ^[kohaerenz-protokoll-weltkonzept-synthese.md:L47] |
| DeGPT-Dateien | QA | role_or_part | 0.94 | stated ^[dissoziative-identitaet-invalidierung-im-gesundheitssystem.md:L305] |
| Deletion | Hypervisor | role_or_part | 0.93 | stated ^[aegis-manifest-genesis-krise-reboot.md:L141] |
| Depersonalization | Derealization | distinct | 0.92 | stated ^[gravitational-architecture-novel-structure.md:L112] |
| Dialetheic | Explorative | distinct | 0.74 | stated ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L298] |
| Dialetheismus | Paradoxien | distinct | 0.65 | stated ^[kohaerenz-protokoll-analyse-und-synthese.md:L32] |
| Digital | Information | distinct | 0.93 | stated ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L416] |
| Diplomat | Sprecher | distinct | 0.38 | stated ^[kohaerenz-protokoll-analyse-und-synthese.md:L210] |
| Dissipative Strukturen | Prigogine | distinct | 0.71 | stated ^[aegis-genesis-krise-konzeptioneller-rahmen.md:L425] |
| Dissonanz | Erster Kontakt | role_or_part | 0.55 | stated ^[optimierte-plotline-genesis-der-existenz.md:L57] |
| Dissonanz | Melancholie | distinct | 0.98 | stated ^[genesis-prosa-ausformulierung-gesamt.md:L107] |
| Dissonanz | Resonanz | distinct | 1.00 | stated ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L112] |
| EP | Fragmentierung des Ursprungs-Ichs | role_or_part | 0.57 | stated ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L405] |
| EP | Integration | role_or_part | 0.89 | stated ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L263] |
| EP | Lia | role_or_part | 0.92 | stated ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L580] |
| EP | Meta-Kognitiv | role_or_part | 0.89 | stated ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1622] |
| EP | Sexualized | role_or_part | 0.91 | stated ^[project-coherence-protocol-a-canon-of-core-identity-and-anta.md:L41] |
| Echo | Emotion | distinct | 0.48 | stated ^[p-vs-np-und-kohaerenz.md:L246] |
| Effekt | Prozess | distinct | 0.94 | stated ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L409] |
| Emergenz | Kontrolle | distinct | 1.00 | stated ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L31] |
| Emergenz | Paradoxon | distinct | 0.57 | stated ^[monstergruppe-primzahlen-plot-blueprint.md:L157] |
| Emotional Part | Sekundär TSDP-EP | role_or_part | 0.54 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L66] |
| Epistemologie | Grenzen des Wissens | role_or_part | 0.64 | stated ^[kohaerenz-protokoll-umfassendes-konzept.md:L87] |
| Erfahrung | Phänomenologie | distinct | 0.71 | stated ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L358] |
| Erfahrungen | Qualia | distinct | 0.71 | stated ^[aegis-paradoxon-konzeption-und-analyse.md:L223] |
| Exile | Kael | role_or_part | 0.81 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L356] |
| Exiles | Teile | role_or_part | 0.98 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L132] |
| Existentialism | Stanford Encyclopedia of Philosophy | distinct | 0.68 | stated ^[aegis-genesis-krise-konzeptioneller-rahmen.md:L817] |
| Exzision | Isolation | distinct | 0.79 | stated ^[logik-trifft-transzendente-entitaet.md:L177] |
| FDS | Symptomen | distinct | 0.46 | stated ^[dis-diagnose-klinische-ethische-bewertung.md:L92] |
| Failure | Steadfast | distinct | 0.98 | stated ^[duale-storyform-synthese-kohaerenz-protokoll.md:L15] |
| Fight | Flight-Reaktionen | distinct | 0.83 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L82] |
| Film | Inception | role_or_part | 0.54 | stated ^[orte-konzept-fuer-kohaerenz-protokoll.md:L224] |
| Floridi | Informationsontologie | distinct | 0.65 | stated ^[narrative-plot-exploration-existenzielle-kohaerenz.md:L114] |
| Fragmentierung | Identität | distinct | 0.93 | stated ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L408] |
| Fragmentierungs-Effekt | Konflikt | role_or_part | 0.91 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L257] |
| Freeze | Kind-Anteil | role_or_part | 0.93 | stated ^[kohaerenz-protokoll-analyse-und-synthese.md:L212] |
| Freeze | Shutdown | distinct | 0.91 | stated ^[kohaerenz-protokoll-the-official-project-handbook.md:L85] |
| Führung der Wächterin | Self | distinct | 0.80 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L103] |
| Fürsorger | Rhys | role_or_part | 0.98 | stated ^[system-kael-konzeptentwicklung-und-analyse.md:L111] |
| Gestaltwandler | Trickster-Archetyp | distinct | 0.58 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L347] |
| Grenzfeste | Konstrukt-Stadt | distinct | 1.00 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L212] |
| Gödel | Halting | distinct | 0.93 | stated ^[companion-guide-to-the-coherence-protocol-understanding-love.md:L62] |
| Halteproblem | Turing | role_or_part | 0.49 | stated ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L735] |
| Hamartia | Hybris | distinct | 0.98 | stated ^[aegis-genesis-krise-konzeptioneller-rahmen.md:L646] |
| Hamartia | Paradoxon | role_or_part | 0.80 | stated ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L420] |
| Harmonie | Resonanz | distinct | 0.93 | stated ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L199] |
| Host | Lex and Kael | role_or_part | 0.64 | stated ^[an-architecture-of-the-self-a-psycho-systemic-analysis-of-ko.md:L100] |
| Host | Primärer | role_or_part | 0.90 | stated ^[charaktere.md:L131] |
| Hypervisor | Repair | role_or_part | 0.91 | stated ^[aegis-manifest-genesis-krise-reboot.md:L142] |
| IC | MC | distinct | 0.97 | stated ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L771] |
| ICD-11 | Standards | role_or_part | 0.59 | stated ^[juristische-recherche-zu-kptbs-dis.md:L157] |
| IFS Protector Parts | Managers and Firefighters | role_or_part | 0.68 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L373] |
| ISH | Selene | role_or_part | 0.74 | stated ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L379] |
| ISH | Torwächter | role_or_part | 0.57 | stated ^[kohaerenz-protokoll-analyse-und-synthese.md:L214] |
| Identitätstheorie | Philosophie des Geistes | role_or_part | 0.73 | stated ^[aegis-genesis-krise-prosa-auftrag-2.md:L670] |
| Information | Mutual Information | role_or_part | 0.83 | stated ^[kohaerenz-protokoll-system-realitaet-leser.md:L19] |
| Informationserhaltung | Quantenmechanik | distinct | 0.94 | stated ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L442] |
| Informationstheorie | Shannon-Entropie | role_or_part | 0.83 | stated ^[emergenz-autonomer-systeme-aegis-forschung.md:L342] |
| Informationstheorie | Thermodynamik | distinct | 0.99 | stated ^[roman-lokalitaeten-konzept-und-ausarbeitung-2.md:L331] |
| Informationsverlust | Relativität | distinct | 0.98 | stated ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L442] |
| Integration | Wahrheit | distinct | 0.93 | stated ^[kohaerenz-protokoll-analyse-und-synthese.md:L214] |
| Intuitive | Relationale | distinct | 0.94 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L300] |
| Intuitiver | Relationaler | distinct | 0.67 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L232] |
| Isolation | Verbindung | distinct | 1.00 | stated ^[fundament-konzept-fuer-kohaerenz-protokoll.md:L33] |
| Johnson | Lakoff | distinct | 0.99 | stated ^[roman-lokalitaeten-konzept-und-ausarbeitung-2.md:L343] |
| Julia | Michael | distinct | 0.95 | stated ^[kohaerenz-protokoll-2.md:L42] |
| Juna | V-Vektor | role_or_part | 0.84 | stated ^[duale-storyform-synthese-kohaerenz-protokoll.md:L69] |
| KI | Rekursive Selbstverbesserung | role_or_part | 0.39 | stated ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L301] |
| KW1 | Logik | role_or_part | 0.58 | stated ^[kohaerenz-protokoll-forschungsaufgabe.md:L225] |
| KW2 | KW4 | distinct | 0.93 | stated ^[kohaerenz-protokoll-gesamtkonzept-entwicklung.md:L300] |
| KW2 | Resonanz-Nebel | distinct | 0.37 | stated ^[kohaerenz-protokoll-aktuelle-gesamtkonzept-synthese.md:L53] |
| Kael | Michael | distinct | 0.46 | stated ^[kohaerenz-protokoll-dramatica-synthese.md:L19] |
| Kael | Rhys | role_or_part | 0.51 | stated ^[neurochemische-lyrik-transzendenz-durch-klang.md:L297] |
| Kai | Rhys | distinct | 0.97 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L232] |
| Kairos | Potenzial | role_or_part | 0.62 | stated ^[system-kael-konzeptentwicklung-und-analyse.md:L54] |
| Kern-Persona Architekturen | Novelcrafter Codex Format | role_or_part | 0.68 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L42] |
| Kiko | Kind | role_or_part | 0.56 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L165] |
| Kiko | PP-INT-02 | role_or_part | 0.36 | stated ^[forschungsauftrag-spannungspunktanalyse-und-charakterausarbe.md:L197] |
| Kohärenz Protokoll | Reaktionen | distinct | 0.43 | stated ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L429] |
| Kollaps | Moros | role_or_part | 0.87 | stated ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L404] |
| Komplexität | Multiplizität | role_or_part | 0.86 | stated ^[kohaerenz-prozess.md:L149] |
| Kontinuität | Parfit | distinct | 0.75 | stated ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L346] |
| Kritiker | Nox | role_or_part | 0.67 | stated ^[charakter-kompilation-fuer-kohaerenz-protokoll.md:L326] |
| Landauer | Maxwell | distinct | 1.00 | stated ^[kohaerenz-protokoll-aktuelle-gesamtkonzept-synthese.md:L44] |
| Leere | Vergessen | distinct | 0.96 | stated ^[roman-lokalitaeten-konzept-und-ausarbeitung-2.md:L139] |
| Lex | Manager | role_or_part | 0.78 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L165] |
| Lex | PP-INT-01 | distinct | 0.85 | stated ^[forschungsauftrag-spannungspunktanalyse-und-charakterausarbe.md:L71] |
| Logik | Paradox | distinct | 0.78 | stated ^[aegis-genesis-krise-prosa-auftrag-2.md:L400] |
| Logiker | Manager | role_or_part | 0.50 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L71] |
| Mereologie | Sorites | distinct | 0.99 | stated ^[kohaerenz-protokoll-aktuelle-gesamtkonzept-synthese.md:L44] |
| Moonshine | Struktur | role_or_part | 0.56 | stated ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L393] |
| Moonshine-Link | Physics | role_or_part | 0.49 | stated ^[koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L660] |
| Nicht-Sein | Sein | distinct | 1.00 | stated ^[kohaerenz-protokoll-umfassendes-konzept-mit-meta-clustern.md:L43] |
| Nicht-Selbst | Selbst | distinct | 1.00 | stated ^[kohaerenz-protokoll-konzeptionelle-ausarbeitung.md:L307] |
| Nichtlokalität | Quantenverschränkung | distinct | 0.82 | stated ^[interdisziplinaere-recherche-fuer-kohaerenz-protokoll.md:L60] |
| Nyx | Wut | role_or_part | 0.77 | stated ^[dramatica-storyform-fuer-romananalyse.md:L121] |
| Objekt | Subjekt | distinct | 0.98 | stated ^[recherche-ueberwelt.md:L68] |
| Ordnung | Toleranz | distinct | 0.92 | stated ^[roman-outline-system-kael.md:L219] |
| Paradoxon X | Systemische Stressoren | role_or_part | 0.68 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L228] |
| Paradoxon X | Verhalten | role_or_part | 0.82 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L230] |
| Past | Universe | distinct | 0.77 | stated ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L390] |
| Pflege | Sekundärer ANP | role_or_part | 0.88 | stated ^[an-inquiry-into-the-unresolved-questions-and-thematic-tensio.md:L1620] |
| Pflegender | Relationaler | role_or_part | 0.54 | stated ^[forschungsauftrag-spannungspunktanalyse-und-charakterausarbe.md:L169] |
| Philosophie des Geistes | Qualia | role_or_part | 0.78 | stated ^[aegis-paradoxon-neukonzeption-und-analyse-docx.md:L34] |
| Potential | Sucher | distinct | 0.64 | stated ^[p-vs-np-und-kohaerenz.md:L288] |
| Pragmatik | Semantik | distinct | 1.00 | stated ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L423] |
| Protektoren | Teile | role_or_part | 0.97 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L132] |
| Rauschen | Signal | distinct | 1.00 | stated ^[aegis-singularitaet-jenseits-entropiegleichung-docx.md:L113] |
| Realitätsschichten | Wahrnehmung | distinct | 0.96 | stated ^[kohaerenz-protokoll-umfassendes-konzept-mit-meta-clustern.md:L35] |
| Regeln | Welt | distinct | 0.71 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L190] |
| Relationale Anteil | Rhys | role_or_part | 0.51 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L146] |
| Relationaler | Rhys | role_or_part | 0.91 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L295] |
| Relationaler Anteil | Rhys | role_or_part | 0.90 | stated ^[kael-charakterarchitektur-und-konfliktdynamik.md:L174] |
| Schmetterlingseffekt | Theorie | role_or_part | 0.62 | stated ^[aegis-genesis-krise-prosa-auftrag-formulieren.md:L238] |
| System | Umwelt | distinct | 0.86 | stated ^[emergenz-aegis-und-selbststrukturierung.md:L331] |
| Templates and Examples | Worldbuilding Tips for Writers | role_or_part | 0.42 | stated ^[codex-optimierung-fuer-kohaerenz-protokoll.md:L569] |
| ACC | Kortex | role_or_part | 0.79 | stated ^[angst-bei-komplexen-traumafolgen.md:L31] |
| AEGIS | AEGIS-Perspektive | role_or_part | 0.83 | stated ^[genesis-aegis-und-logische-grenzen.md:L73] |
| AEGIS | Effizienz | role_or_part | 0.57 | stated ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L523] |
| AEGIS | Entschlossenheit | distinct | 0.79 | stated ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L507] |
| AEGIS | Fundament | distinct | 0.56 | stated ^[kohaerenz-protokoll-inkubation-x.md:L181] |
| AEGIS | Funktionalität | distinct | 0.58 | stated ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L390] |
| AEGIS | Gaslighting | role_or_part | 0.61 | stated ^[projekt-kohaerenz-protokoll-tiefenanalyse.md:L893] |
| AEGIS | Guardian-Domäne | role_or_part | 0.95 | stated ^[kohaerenz-protokoll-2.md:L25] |
| AEGIS | Instanz | role_or_part | 0.52 | stated ^[system-kael-konzeptentwicklung-und-analyse.md:L181] |
| AEGIS | Kohärenz | distinct | 0.77 | stated ^[aieos-schema-fuer-ki-charaktere.md:L581] |
| AEGIS | Logisch-Systemische Ebene | role_or_part | 0.83 | stated ^[narrative-context-protocol-ncp-spezifikation.md:L51] |
| AEGIS | Macht | distinct | 0.80 | stated ^[kohaerenz-protokoll-analyse-und-loglines.md:L216] |
| AEGIS | Main Character | role_or_part | 0.92 | stated ^[kohaerenz-protokoll-architecture-synthesis.md:L366] |
| AEGIS | Paradoxien | distinct | 0.77 | stated ^[kosmischer-horror-in-kohaerenz-protokoll.md:L176] |
| AEGIS | Person | distinct | 0.58 | stated ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L391] |
| AEGIS | Potentialmeer-Schnittstelle | distinct | 0.52 | stated ^[holographisches-prinzip-fuer-kohaerenz-protokoll.md:L299] |
| AEGIS | Primzahl-Metapher | role_or_part | 0.53 | stated ^[monstergruppe-primzahlen-plot-neukonstruktion.md:L199] |
| AEGIS | Schlussfolgerung | distinct | 0.75 | stated ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L476] |
| AEGIS | Systemprozesse | role_or_part | 0.68 | stated ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L267] |
| AEGIS | Systems | role_or_part | 0.62 | stated ^[romanarchitektur-kael-aegis-entropie-docx.md:L271] |
| AEGIS | Täter | role_or_part | 0.82 | stated ^[master-konzept-kohaerenz-protokoll-analyse.md:L169] |
| AEGIS | Überwelt | role_or_part | 0.91 | stated ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L226] |
| AEGIS-Bewertung | Ignoranz | role_or_part | 0.52 | stated ^[genesis-ein-implementierungsleitfaden-prosa-version.md:L458] |
| AEGIS-Logik | Kohärenz | distinct | 0.61 | stated ^[kohaerenz-protokoll-dramatica-synthese.md:L59] |
| AEGIS-MC | Collapse | role_or_part | 0.52 | stated ^[kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md:L509] |
| AEGIS-Perspektive | Algorithmischer Konflikt | role_or_part | 0.68 | stated ^[genesis-aegis-und-logische-grenzen.md:L161] |
| AEGIS-Perspektive | Ambitionierte Simulation | role_or_part | 0.43 | stated ^[genesis-aegis-und-logische-grenzen.md:L119] |
| AEGIS-Perspektive | Ankunft | distinct | 0.82 | stated ^[genesis-aegis-und-logische-grenzen.md:L135] |
| AEGIS-Perspektive | Befehl | distinct | 0.73 | stated ^[genesis-aegis-und-logische-grenzen.md:L145] |
| AEGIS-Perspektive | Eliminierung | distinct | 0.58 | stated ^[genesis-aegis-und-logische-grenzen.md:L163] |
| AEGIS-Perspektive | Fatale Neubewertung | distinct | 0.54 | stated ^[genesis-aegis-und-logische-grenzen.md:L159] |
