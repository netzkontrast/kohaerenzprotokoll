# Repository skills and the AEGIS instructions

Review scope: all project skill entrypoints under `.agents/skills/`, their routing
and repository-specific boundaries; targeted deeper reading of the workflows
changed below. Pinned `.claude/skills/` vendors were checked for metadata, not
validated as production tools. No live-model evaluation or literary-quality
benchmark was run. The catalog is intentionally qualitative; current counts come
from `check_skills.py`, not this page.

## Findings and edits in this PR

| Surface | Observed issue | Change |
|---|---|---|
| CLAUDE/NOW | Runtime inventory, history and stale counts crowded startup; no-board claim contradicted the implemented board | Startup/rules in CLAUDE, current steps in NOW, nuanced commit/correction procedures in session-method; history stays in git |
| `ingest` | Description selected a full ingest even for partial research reading | Route bounded research to reader-tools; require census/reconciliation only when those artifacts are requested |
| `graph-context` | Bounded research pack could be mistaken for a permitted character context | Explicit author/research-only scope; runtime permissions must filter before the model |
| `reader-tools` | Research role existed but no explicit AEGIS handoff boundary | Researcher provides attributed findings and gaps; no persona execution or automatic source promotion |
| `writing-skills` | Common no-prose-rewrite rule could be misread as banning isolated scenario output | Distinguish editorial findings, explicitly authorized drafting and fictional test artifacts; common guidance routes to the pilot briefing |
| `storyform` | Named a fixed A–I variant set; simulation constraints lacked a route | Enumerate actual drafts; derive pilot constraints from decided structure and canon without promoting implementation assumptions |
| `scene-architecture` | Good knowledge/cost guidance lacked a bridge to simulation | Planning handoff specifies perceptions, action prerequisites and before/after consequences; code owns state validity |
| `continuity-editor` | Generic inferred canon could become a runtime fact | State simulation review categories; no observed draft or run automatically updates canon |
| `character-card-builder` | Prose card could silently become an all-knowing agent prompt | Separate approved facts, proposed voice and scene-earned knowledge before translating into a profile |
| `tools` | Promotion described as unbuilt despite `promote.py` existing | Point to actual promotion and term-page tools, keeping their separate review meanings |

These are incremental edits to existing project skills. No AEGIS skill is created
before there is an executable workflow/fixture to describe. The pilot briefing
owns implementation acceptance; skills link to it rather than copying a second
tool API. `.claude/skills/` symlinks remain the single-copy discovery path.

## Keep, with bounded recommendations

| Skill group | Assessment / next useful improvement |
|---|---|
| `dialogue-gym`, `prose-rhythm`, `psychic-distance` | Keep craft drills distinct from model-generated character dialogue. Use dialogue-gym to assess the author's supplied attempt; it is not the AEGIS dialogue generator |
| `line-editor`, `copy-editor` | Keep findings-only behavior and exact locations; runtime event validation is outside their scope |
| `developmental-editor`, `workshop-critique` | Evaluate dramatic consequences on supplied text; do not call a valid JSON transcript a publishable scene |
| `beta-reader-panel`, `agent-first-pages` | Preserve blind/read-so-far inputs. Agent author-context must not leak into reader or player simulation |
| `reverse-character-cards` | Useful to compare an actual transcript's behavior against intended profile; extracted traits remain observations |
| `app-refresh` | Already acknowledges hook removal. Use for new NOW derivation and later replay UI; do not turn it into a prerequisite deployment approval for documentation work |
| `qmd` | Keep search versus census distinction. Cold-container qmd installation failed in this environment; report that and use exact-file reading, not fabricated semantic recall |
| `dspy` | Consider later prompt optimization only after repeatable labeled pilot cases exist; do not optimize canon or permissions |
| `hyperextract-learning` | Keep proposal layer and STOP decision; template extraction is not a world-state updater |
| `typesafe`, `jules` | Preserve provider/remote-session authorization and narrow task scope; no new need for either in the offline pilot |

Vendored HyperExtract skills report folder/name mismatches through the existing
validator. Do not fix them locally as part of this proposal; upstream changes and
pin updates are a separate task. Other vendors are not endorsed by passing
frontmatter checks.

## Review examples for Claude

| Request | Correct routing/result |
|---|---|
| “Find prompting ideas in these two Sources” | reader-tools/research, exact source lines and gaps; no mandatory census or Wiki write |
| “Ingest this source into the wiki” | ingest, independent extraction before wiki context, reconciliation and source-named commit |
| “Build the offline AEGIS pilot” | coding coordinator → CLAUDE + pilot briefing; fixtures/mocks, no narrative canon mutation |
| “Check the simulated dialogue's voice” | writing-skills + appropriate critic on supplied transcript, not dialogue-gym as an autonomous generator |
| “Make the AEGIS run canonical” | identify exact proposed content and author decision; a good run alone is insufficient |

After the first pilot, replace proposal language only for implemented behavior.
If a skill boundary repeatedly fails on these examples, add a focused fixture or
reference; do not grow every skill with the same startup/authority paragraph.
