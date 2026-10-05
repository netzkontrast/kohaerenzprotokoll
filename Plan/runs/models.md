# Which model, where

Every contract run by model and by the category of its source — written by `scripts/contracts.py`, the table `scripts/modelpick.py` chooses from (`Plan/hyperextract/models.json`: about a fifth of runs explore a model at random, the rest take the best **labelled** one). *admitted* rows are staging's, not a judgement; only *labelled ok* is precision, and a cell with fewer labelled rows than the policy's `min_labels` ranks nothing.

| contract | category | model | runs (explored) | found nothing | admitted | $ per admitted row | labelled | ok |
|---|---|---|---|---|---|---|---|---|
| `AliasPairs` | plot-outline | sonnet | 1 (0) | 0 | 8 | 0.0195 | 0 | — |
| `AliasPairs` | theorie-logik | sonnet | 1 (0) | 0 | 3 | 0.0204 | 0 | — |
| `AliasPairs` | worldbuilding | haiku | 1 (0) | 0 | 32 | 0.0091 | 15 | 6 (40%) |
| `Analogies` | kernkonzept | haiku | 1 (0) | 0 | 15 | 0.0052 | 14 | 7 (50%) |
| `Analogies` | plot-outline | sonnet | 1 (0) | 1 | 0 | — | 0 | — |
| `Analogies` | theorie-logik | haiku | 1 (0) | 0 | 1 | 0.0327 | 1 | 0 (0%) |
| `Analogies` | theorie-logik | sonnet | 1 (0) | 0 | 0 | — | 0 | — |
| `Anchors` | plot-outline | haiku | 1 (0) | 0 | 14 | 0.0069 | 19 | 0 (0%) |
| `Anchors` | plot-outline | sonnet | 1 (0) | 0 | 7 | 0.0225 | 0 | — |
| `Anchors` | theorie-logik | haiku | 1 (0) | 0 | 6 | 0.0064 | 11 | 6 (55%) |
| `Anchors` | theorie-logik | sonnet | 1 (0) | 1 | 0 | — | 0 | — |
| `Attributions` | plot-outline | sonnet | 1 (0) | 0 | 3 | 0.0440 | 0 | — |
| `Attributions` | theorie-logik | haiku | 1 (0) | 0 | 0 | — | 0 | — |
| `Attributions` | theorie-logik | sonnet | 1 (0) | 0 | 2 | 0.0249 | 0 | — |
| `CardFields` | charaktere | haiku | 1 (0) | 0 | 39 | 0.0042 | 14 | 12 (86%) |
| `CardFields` | plot-outline | sonnet | 1 (0) | 0 | 1 | 0.1411 | 0 | — |
| `CardFields` | theorie-logik | sonnet | 1 (0) | 0 | 5 | 0.0127 | 0 | — |
| `CastRoles` | plot-outline | haiku | 1 (0) | 0 | 15 | 0.0062 | 12 | 7 (58%) |
| `CastRoles` | plot-outline | sonnet | 1 (0) | 0 | 2 | 0.0678 | 0 | — |
| `CastRoles` | theorie-logik | sonnet | 1 (0) | 0 | 6 | 0.0083 | 0 | — |
| `CausalLinks` | charaktere | haiku | 1 (0) | 0 | 8 | 0.0085 | 0 | — |
| `CausalLinks` | kernkonzept | haiku | 6 (0) | 0 | 690 | 0.0064 | 7 | 2 (29%) |
| `CausalLinks` | plot-outline | haiku | 3 (0) | 0 | 54 | 0.0140 | 0 | — |
| `CausalLinks` | plot-outline | sonnet | 1 (0) | 0 | 2 | 0.0744 | 0 | — |
| `CausalLinks` | storyform | haiku | 3 (0) | 0 | 142 | 0.0073 | 3 | 3 (100%) |
| `CausalLinks` | theorie-logik | haiku | 1 (0) | 0 | 0 | — | 6 | 5 (83%) |
| `CausalLinks` | theorie-logik | sonnet | 1 (0) | 0 | 5 | 0.0146 | 0 | — |
| `CausalLinks` | theorie-physik | haiku | 1 (0) | 0 | 53 | 0.0063 | 1 | 0 (0%) |
| `CausalLinks` | worldbuilding | haiku | 2 (0) | 0 | 94 | 0.0080 | 1 | 1 (100%) |
| `ChapterBeats` | plot-outline | haiku | 1 (0) | 0 | 32 | 0.0032 | 15 | 14 (93%) |
| `ChapterBeats` | plot-outline | sonnet | 1 (0) | 0 | 21 | 0.0092 | 0 | — |
| `ChapterBeats` | theorie-logik | sonnet | 1 (0) | 0 | 1 | 0.0498 | 0 | — |
| `ChapterCards` | plot-outline | haiku | 1 (0) | 0 | 36 | 0.0033 | 15 | 13 (87%) |
| `ChapterCards` | plot-outline | sonnet | 4 (0) | 1 | 234 | 0.0073 | 0 | — |
| `ChapterCards` | theorie-logik | sonnet | 1 (0) | 0 | 1 | 0.0472 | 0 | — |
| `DiegeticTerms` | charaktere | haiku | 1 (0) | 0 | 5 | 0.0267 | 5 | 1 (20%) |
| `DiegeticTerms` | plot-outline | sonnet | 1 (0) | 0 | 0 | — | 0 | — |
| `DiegeticTerms` | theorie-logik | sonnet | 1 (0) | 0 | 1 | 0.0515 | 0 | — |
| `EntityFacts` | charaktere | haiku | 1 (0) | 0 | 60 | 0.0031 | 10 | 9 (90%) |
| `EntityFacts` | plot-outline | sonnet | 1 (0) | 0 | 14 | 0.0136 | 0 | — |
| `EntityFacts` | theorie-logik | sonnet | 1 (0) | 0 | 4 | 0.0145 | 0 | — |
| `Knowledge` | plot-outline | sonnet | 1 (0) | 0 | 1 | 0.1303 | 0 | — |
| `Knowledge` | theorie-logik | haiku | 1 (0) | 0 | 2 | 0.0183 | 12 | 3 (25%) |
| `Knowledge` | theorie-logik | sonnet | 1 (0) | 0 | 6 | 0.0121 | 0 | — |
| `LocationRegistry` | plot-outline | sonnet | 1 (0) | 0 | 0 | — | 0 | — |
| `LocationRegistry` | theorie-logik | sonnet | 1 (0) | 1 | 0 | — | 0 | — |
| `Locks` | kernkonzept | haiku | 1 (0) | 0 | 0 | — | 0 | — |
| `Locks` | plot-outline | sonnet | 1 (0) | 0 | 1 | 0.1135 | 0 | — |
| `Locks` | theorie-logik | sonnet | 1 (0) | 1 | 0 | — | 0 | — |
| `OpenPoints` | plot-outline | sonnet | 1 (0) | 0 | 7 | 0.0169 | 0 | — |
| `OpenPoints` | theorie-logik | haiku | 1 (0) | 0 | 3 | 0.0105 | 3 | 1 (33%) |
| `OpenPoints` | theorie-logik | sonnet | 1 (0) | 1 | 0 | — | 0 | — |
| `Pitch` | kernkonzept | haiku | 1 (0) | 0 | 0 | — | 0 | — |
| `Pitch` | plot-outline | sonnet | 1 (0) | 0 | 1 | 0.1093 | 0 | — |
| `Pitch` | theorie-logik | sonnet | 1 (0) | 1 | 0 | — | 0 | — |
| `Precedence` | plot-outline | haiku | 1 (0) | 0 | 33 | 0.0031 | 12 | 2 (17%) |
| `Precedence` | plot-outline | sonnet | 1 (0) | 0 | 2 | 0.0669 | 0 | — |
| `Precedence` | theorie-logik | sonnet | 1 (0) | 1 | 0 | — | 0 | — |
| `ProseRules` | charaktere | haiku | 1 (0) | 0 | 50 | 0.0031 | 11 | 10 (91%) |
| `ProseRules` | plot-outline | sonnet | 1 (0) | 0 | 11 | 0.0156 | 0 | — |
| `ProseRules` | theorie-logik | sonnet | 1 (0) | 0 | 4 | 0.0165 | 0 | — |
| `Quantities` | kernkonzept | haiku | 1 (0) | 0 | 0 | — | 0 | — |
| `Quantities` | plot-outline | sonnet | 1 (0) | 0 | 30 | 0.0067 | 0 | — |
| `Quantities` | theorie-logik | sonnet | 1 (0) | 0 | 5 | 0.0114 | 0 | — |
| `RelationReadings` | plot-outline | sonnet | 1 (0) | 0 | 85 | 0.0035 | 0 | — |
| `RelationReadings` | theorie-logik | sonnet | 1 (0) | 0 | 31 | 0.0022 | 0 | — |
| `Rules` | kernkonzept | haiku | 1 (0) | 0 | 16 | 0.0050 | 8 | 0 (0%) |
| `Rules` | plot-outline | sonnet | 1 (0) | 0 | 5 | 0.0301 | 0 | — |
| `Rules` | theorie-logik | haiku | 1 (0) | 0 | 5 | 0.0070 | 3 | 2 (67%) |
| `Rules` | theorie-logik | sonnet | 1 (0) | 0 | 5 | 0.0118 | 0 | — |
| `StandingClaims` | kernkonzept | haiku | 1 (0) | 0 | 0 | — | 0 | — |
| `StandingClaims` | plot-outline | sonnet | 1 (0) | 0 | 5 | 0.0297 | 0 | — |
| `StandingClaims` | theorie-logik | haiku | 1 (0) | 0 | 0 | — | 0 | — |
| `StandingClaims` | theorie-logik | sonnet | 1 (0) | 1 | 0 | — | 0 | — |
| `StatedRelations` | plot-outline | sonnet | 1 (0) | 0 | 19 | 0.0125 | 0 | — |
| `StatedRelations` | theorie-logik | sonnet | 1 (0) | 0 | 16 | 0.0053 | 0 | — |
| `Storypoints` | plot-outline | sonnet | 1 (0) | 0 | 3 | 0.0418 | 0 | — |
| `Storypoints` | storyform | haiku | 1 (0) | 0 | 11 | 0.0174 | 11 | 4 (36%) |
| `Storypoints` | theorie-logik | sonnet | 1 (0) | 1 | 0 | — | 0 | — |
| `StructureBeats` | plot-outline | haiku | 1 (0) | 0 | 11 | 0.0090 | 12 | 12 (100%) |
| `StructureBeats` | plot-outline | sonnet | 1 (0) | 0 | 7 | 0.0221 | 0 | — |
| `StructureBeats` | theorie-logik | sonnet | 1 (0) | 0 | 1 | 0.0527 | 0 | — |
| `TermCensus` | plot-outline | sonnet | 2 (0) | 0 | 0 | — | 0 | — |
| `TermCensus` | theorie-logik | sonnet | 1 (0) | 0 | 0 | — | 0 | — |
| `TermContrasts` | charaktere | haiku | 1 (0) | 0 | 14 | 0.0053 | 0 | — |
| `TermContrasts` | kernkonzept | haiku | 6 (0) | 0 | 1245 | 0.0038 | 9 | 5 (56%) |
| `TermContrasts` | plot-outline | haiku | 3 (0) | 0 | 170 | 0.0048 | 0 | — |
| `TermContrasts` | plot-outline | sonnet | 1 (0) | 0 | 7 | 0.0238 | 0 | — |
| `TermContrasts` | storyform | haiku | 3 (0) | 0 | 294 | 0.0038 | 0 | — |
| `TermContrasts` | theorie-logik | sonnet | 1 (0) | 0 | 4 | 0.0127 | 0 | — |
| `TermContrasts` | theorie-physik | haiku | 1 (0) | 0 | 75 | 0.0045 | 0 | — |
| `TermContrasts` | theorie-psychologie | haiku | 1 (0) | 0 | 119 | 0.0034 | 0 | — |
| `TermContrasts` | worldbuilding | haiku | 3 (0) | 0 | 280 | 0.0041 | 19 | 15 (79%) |
| `TermDefinitions` | charaktere | haiku | 1 (0) | 0 | 21 | 0.0035 | 0 | — |
| `TermDefinitions` | kernkonzept | haiku | 6 (0) | 0 | 818 | 0.0050 | 6 | 4 (67%) |
| `TermDefinitions` | plot-outline | haiku | 3 (0) | 0 | 241 | 0.0032 | 2 | 1 (50%) |
| `TermDefinitions` | plot-outline | sonnet | 1 (0) | 0 | 11 | 0.0147 | 0 | — |
| `TermDefinitions` | storyform | haiku | 3 (0) | 0 | 278 | 0.0036 | 1 | 1 (100%) |
| `TermDefinitions` | theorie-logik | sonnet | 1 (0) | 0 | 8 | 0.0081 | 0 | — |
| `TermDefinitions` | theorie-physik | haiku | 1 (0) | 0 | 97 | 0.0035 | 1 | 0 (0%) |
| `TermDefinitions` | theorie-psychologie | haiku | 1 (0) | 0 | 174 | 0.0022 | 0 | — |
| `TermDefinitions` | worldbuilding | haiku | 3 (0) | 0 | 375 | 0.0029 | 16 | 13 (81%) |
| `TermReadings` | plot-outline | sonnet | 1 (0) | 0 | 65 | 0.0035 | 0 | — |
| `TermReadings` | theorie-logik | haiku | 5 (0) | 0 | 66 | 0.0033 | 0 | — |
| `TermReadings` | theorie-logik | sonnet | 1 (0) | 0 | 22 | 0.0037 | 0 | — |
| `TermTaxonomy` | plot-outline | sonnet | 1 (0) | 0 | 7 | 0.0206 | 0 | — |
| `TermTaxonomy` | theorie-logik | haiku | 1 (0) | 0 | 7 | 0.0050 | 7 | 3 (43%) |
| `TermTaxonomy` | theorie-logik | sonnet | 1 (0) | 1 | 0 | — | 0 | — |
| `ThemeMotifs` | plot-outline | sonnet | 1 (0) | 0 | 2 | 0.0669 | 0 | — |
| `ThemeMotifs` | theorie-logik | haiku | 1 (0) | 0 | 4 | 0.0089 | 4 | 3 (75%) |
| `ThemeMotifs` | theorie-logik | sonnet | 1 (0) | 0 | 5 | 0.0132 | 0 | — |
| `Utterances` | charaktere | haiku | 1 (0) | 0 | 3 | 0.0433 | 3 | 3 (100%) |
| `Utterances` | plot-outline | haiku | 1 (0) | 0 | 0 | — | 9 | 4 (44%) |
| `Utterances` | plot-outline | sonnet | 1 (0) | 0 | 5 | 0.0296 | 0 | — |
| `Utterances` | theorie-logik | sonnet | 1 (0) | 0 | 3 | 0.0177 | 0 | — |
