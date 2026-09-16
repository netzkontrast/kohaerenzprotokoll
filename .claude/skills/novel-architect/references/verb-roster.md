# Novel capability — full verb roster (Spec 101 master)

Moved out of `CLAUDE.md` 2026-09-16 (workflow-simplification pass): this is a
lookup table, not working agreement, and it duplicates what `search` /
`get_schema` already expose live from the engine — load it on demand instead
of every session. See `CLAUDE.md` §"Novel capability" for the parts that
stayed (how to invoke, the 5-verb spine, lifecycle enums, the gate ladder).

The `novel` capability is the engine for authoring this book. **91 verbs**
across 3 roles drive premise → manuscript with graph-recorded provenance.

## Storyform coherence (Spec 120)

`novel_coherence_check(ncp)` runs all 11 decidable storyform checks. The NCP
schema (v1.3.0, 463 appreciations + 144 narrative_functions) and the Dramatica
ontology ship with the capability; `validate_appreciations` / `validate_narrative_functions`
gate against the canonical vocabularies.

## Verb roster — params in **bold** are required (`intent_id`/`agent_id` always optional)

### Role: `act` (9 verbs)

| Verb | Params (required **bold**) | Purpose |
|---|---|---|
| `novel.chapter_report_full` | **`chapter_id`:str** | Full editorial dashboard for one chapter (act). |
| `novel.conceptualize` | **`title`:str**, **`author`:str**, `premise`:str="", `central_question`:str="" | Render a novel-concept document (act); the first verb of the MVN flow. |
| `novel.generate_scene_body` | `scene_id`:str="", `scene_brief`:str="", `alter_id`:str="", `system`:str="", `host_completion`:dict | None=None, `prefer_delegate`:bool=False, `max_tokens`:int=8000 | Spec 220 Slice 1 — wet scene-body generation via Spec 147 + Spec 279. |
| `novel.render_blurb` | **`novel_id`:str**, **`hook`:str**, **`stakes`:str** | Render a back-cover blurb (act, driver-free). |
| `novel.render_chapter_brief` | **`chapter_id`:str**, `research_intent_id`:str="" | Produce a research-dossier brief tied to a chapter (act, xcap to prompt). |
| `novel.render_manuscript` | **`novel_id`:str** | Concatenate chapters into a manuscript artefact (act). |
| `novel.render_query_letter` | **`novel_id`:str**, **`agent_name`:str**, `comp_titles`:str="" | Render an agent query letter (act, driver-free). |
| `novel.render_synopsis` | **`novel_id`:str** | Render a synopsis from chapter outline (act, driver-free). |
| `novel.storyform_critical_pass` | **`novel_id`:str** | Critical-thinking pass over the storyform (act, xcap to thinking). |

### Role: `effect` (39 verbs)

| Verb | Params (required **bold**) | Purpose |
|---|---|---|
| `novel.archive_codex_entry` | **`entry_id`:str**, `reason`:str="" | Flag a CodexEntry as archived (effect, soft-delete). |
| `novel.beta_ready_gate` | **`novel_id`:str** | Composite gate: all chapters drafted+ (effect). |
| `novel.capture_claim` | **`text`:str**, **`source_uri`:str**, **`domain`:str** | Record a NovelClaim node SERVING the intent (effect). |
| `novel.capture_idea` | **`text`:str** | Record an Idea node SERVING the intent (effect). |
| `novel.copy_gate` | **`novel_id`:str** | Composite gate: surface-level editorial readiness (effect). |
| `novel.create_chapter` | **`novel_id`:str**, **`number`:int**, **`title`:str**, `body`:str="" | Record a Chapter graph node + CHAPTER_OF the parent Novel (effect). |
| `novel.create_codex_entry` | **`novel_id`:str**, **`slug`:str**, **`name`:str**, **`kind`:str**, **`body`:str**, `triggers`:str="" | Mint a CodexEntry + CODEX_OF edge to the Novel (effect). |
| `novel.create_culture` | **`world_id`:str**, **`slug`:str**, **`name`:str** | Mint a Culture under a World + PART_OF_WORLD edge (effect). |
| `novel.create_language` | **`world_id`:str**, **`slug`:str**, **`name`:str** | Mint a Language under a World + PART_OF_WORLD edge (effect). |
| `novel.create_magic_system` | **`world_id`:str**, **`slug`:str**, **`name`:str** | Mint a MagicSystem under a World + PART_OF_WORLD edge (effect). |
| `novel.create_novel` | **`title`:str**, **`author`:str**, `genre`:str="novel" | Record a Novel node SERVING the intent; materialise disk on production. |
| `novel.create_religion` | **`world_id`:str**, **`slug`:str**, **`name`:str** | Mint a Religion under a World + PART_OF_WORLD edge (effect). |
| `novel.create_scene` | **`chapter_id`:str**, **`slug`:str**, **`pov`:str** | Record a Scene node + SCENE_OF the parent Chapter (effect). |
| `novel.create_world` | **`slug`:str**, **`name`:str** | Mint a World node + SERVES intent (effect). |
| `novel.create_world_axiom` | **`world_id`:str**, **`text`:str**, `severity`:str="hard" | Encode a WorldAxiom (rule) under a World (effect). |
| `novel.developmental_gate` | **`novel_id`:str** | Composite gate: structure-level editorial readiness (effect). |
| `novel.dispatch_novel_research` | **`question`:str**, **`domain`:str** | Mint a research lead + record NovelClaim (delegates to research cap). |
| `novel.export_docx` | **`novel_id`:str** | Render manuscript + write docx via FormatDriver (effect). |
| `novel.export_epub` | **`novel_id`:str** | Render manuscript + write epub via FormatDriver (effect). |
| `novel.export_pdf` | **`novel_id`:str** | Render manuscript + write PDF via FormatDriver (effect). |
| `novel.find_axiom_contradictions` | **`world_id`:str** | Decidable axiom-contradiction scan + emit CONTRADICTS edges (effect). |
| `novel.integrate_scene_body` | **`scene_id`:str**, **`body`:str** | Spec 130 phase 5 — write the generated body back to the Scene (effect). |
| `novel.line_gate` | **`novel_id`:str** | Composite gate: prose-level editorial readiness (effect). |
| `novel.link_character_to_world` | **`character_id`:str**, **`target_id`:str**, `edge_kind`:str="BELONGS_TO" | Add a typed edge from Character → World child (effect). |
| `novel.mark_narrative_beat` | **`scene_id`:str**, **`beat_label`:str**, `predecessor_id`:str="" | Mint a NarrativeBeat + optional PRECEDES edge from a predecessor (effect). |
| `novel.novel_coherence_check` | **`ncp`:dict** | Composite gate (Spec 120): runs all 11 storyform checks with chaining. |
| `novel.pre_draft_gate` | **`novel_id`:str** | Composite gate: storyform + research + chapters present (effect). |
| `novel.promote_idea` | **`idea_id`:str**, **`title`:str**, **`author`:str** | Idea → Novel transition; records PROMOTED_TO edge (effect). |
| `novel.publication_gate` | **`novel_id`:str** | Terminal composite: publish_ready + ≥1 export + front-matter declared (effect). |
| `novel.publish_ready_gate` | **`novel_id`:str** | Composite gate: contiguous chapters + status ≥ querying (effect). |
| `novel.query_ready_gate` | **`novel_id`:str** | Composite gate: status ≥ beta + content-clean (effect). |
| `novel.record_character_learns` | **`character_id`:str**, **`fact`:str**, **`scene_id`:str** | Mint a KnownFact + KNOWS + LEARNED_IN edges (effect). |
| `novel.record_story_event` | **`novel_id`:str**, **`label`:str**, **`when_story`:str**, `scene_id`:str="" | Mint a StoryTimeEvent + optional HAPPENS_AT edge from a scene (effect). |
| `novel.record_storyform_decision` | **`novel_id`:str**, **`decision`:str**, `rationale`:str="" | Record a contested storyform decision (effect, xcap to dogfood). |
| `novel.rename_novel` | **`novel_id`:str**, **`new_title`:str** | Update a Novel's title (effect, graph-only). |
| `novel.reveal_in_scene` | **`event_id`:str**, **`scene_id`:str** | Add the REVEALED_IN edge (event disclosed by this scene) (effect). |
| `novel.set_chapter_status` | **`chapter_id`:str**, **`status`:str** | Flip a Chapter's lifecycle status; enum-checked (effect). |
| `novel.set_novel_status` | **`novel_id`:str**, **`status`:str** | Flip a Novel's lifecycle status; enum-checked (effect). |
| `novel.update_codex_entry` | **`entry_id`:str**, `body`:str="", `triggers`:str="", `name`:str="" | Edit a CodexEntry's body / triggers / name (effect). |

### Role: `transform` (43 verbs)

| Verb | Params (required **bold**) | Purpose |
|---|---|---|
| `novel.analyze_readability` | **`body`:str** | Flesch Reading Ease for prose (transform, driver-free). |
| `novel.audit_novel_provenance` | **`novel_id`:str** | Aggregate the provenance graph census for the serving intent (transform, xcap to analyze). |
| `novel.chapter_report` | **`novel_id`:str** | Read-only aggregate over the novel's chapters (transform). |
| `novel.check_approach_concern` | **`ncp`:dict** | Mostly-decidable check (row 8): approach ↔ class compatibility (WARN-severity). |
| `novel.check_content_warnings` | **`body`:str** | Content-warning category scanner (transform, driver-free). |
| `novel.check_continuity` | **`novel_id`:str** | Cross-chapter proper-noun continuity check (transform). |
| `novel.check_crucial_element_placement` | **`ncp`:dict** | Decidable check (row 6): storyform.crucial_element_id == mc.problem_id. |
| `novel.check_dialogue_attribution` | **`body`:str** | Dialogue-tag check — plain ('said') vs flowery (transform). |
| `novel.check_dynamic_pair_reciprocity` | **`ncp`:dict** | Decidable check (row 1): mc.dynamic and os.dynamic must differ. |
| `novel.check_filter_words` | **`body`:str**, `threshold`:float=FILTER_WORD_DENSITY_THRESHOLD | Filter-word density check (transform, show-don't-tell). |
| `novel.check_ktad_coverage` | **`ncp`:dict** | Decidable check (row 2): concern_id == signposts[0] (K-position). |
| `novel.check_mental_sex_problem_solving` | **`ncp`:dict** | Decidable check (row 9): mental_sex ↔ class compatibility. |
| `novel.check_pov_consistency` | **`novel_id`:str** | Per-chapter POV uniformity check across scenes (transform). |
| `novel.check_quad_completeness` | **`ncp`:dict** | Decidable check (row 3): mc problem and solution are paired. |
| `novel.check_resolve_outcome_judgment` | **`ncp`:dict** | Decidable check (row 7): resolve/outcome/judgment triple is legal. |
| `novel.check_sensitivity` | **`body`:str** | Sensitivity-topic advisory scan (transform, WARN-severity). |
| `novel.check_show_dont_tell` | **`body`:str** | Telling-verb scan — interior-monologue tells (transform). |
| `novel.check_signpost_permutation` | **`ncp`:dict** | Decidable check (row 10): signposts in canonical order per class. |
| `novel.check_slot_fill` | **`ncp`:dict** | Decidable check (row 4): no null required slots (transform). |
| `novel.check_storybeat_moment_refs` | **`ncp`:dict** | Decidable check (row 11): every moment.storybeat_ref resolves (transform). |
| `novel.check_throughline_partition` | **`ncp`:dict** | Decidable check (row 5): 4 throughlines / 4 distinct Classes (transform). |
| `novel.check_voice_consistency` | **`bodies`:list[str]**, `z_threshold`:float=2.0 | Per-chapter voice-signature outlier check (transform). |
| `novel.count_words` | **`body`:str** | Word + char counter (transform, driver-free). |
| `novel.fetch_scene_body` | `body_handle`:str="", `max_chars`:int=0 | Spec 220 Slice 1.5 — public retrieval for a scene-body Artefact. |
| `novel.find_novel` | `query`:str="" | Substring-match novel titles (transform, driver-free). |
| `novel.flag_anachronistic_reference` | **`scene_id`:str**, **`character_id`:str**, **`fact_text`:str** | Check if the character knows the fact yet (transform). |
| `novel.list_chapters` | **`novel_id`:str** | List a novel's chapters ordered by number (transform). |
| `novel.list_claims` | `verified`:str="" | List captured claims; optional verified-status filter (transform). |
| `novel.list_codex_entries` | **`novel_id`:str**, `kind`:str="" | List CodexEntries for a novel, optionally filtered by kind (transform). |
| `novel.list_ideas` | `status`:str="" | List captured ideas; optional status filter (transform). |
| `novel.list_reveals_in` | **`scene_id`:str** | List events this scene discloses (transform). |
| `novel.list_story_events_up_to` | **`scene_id`:str** | Story-time slice: events with ``when_story`` ≤ this scene's anchor (transform). |
| `novel.list_world` | **`world_id`:str** | Render a tree of a World's contents (transform). |
| `novel.manuscript_coherence_check` | **`novel_id`:str** | Chapter-sequence contiguity check (transform, driver-free). |
| `novel.match_codex_entries` | **`novel_id`:str**, **`text`:str** | Scan ``text`` for any registered codex trigger; return matches (transform). |
| `novel.narrative_order` | **`novel_id`:str** | Topo-sort over PRECEDES; canonical narrative reading order (transform). |
| `novel.novel_progress` | **`novel_id`:str** | Aggregate progress (word-count + per-status counts) for a novel (transform). |
| `novel.pending_verifications` | — | Aggregate pending claims by domain (transform). |
| `novel.resume_session` | — | Return the most-recently-created Novel's id + title (transform). |
| `novel.scan_proper_nouns` | **`body`:str** | Extract proper nouns (Title-Case words, sentence-starter words filtered) (transform). |
| `novel.validate_appreciations` | **`ncp`:dict** | Row 12 hybrid: NCP appreciations ∈ canonical 463 (transform). |
| `novel.validate_narrative_functions` | **`ncp`:dict** | Row 13 hybrid: NCP narrative_functions ∈ canonical 144 (transform). |
| `novel.what_does_X_know_as_of` | **`character_id`:str**, **`scene_id`:str** | List facts the character has learned ≤ the scene's narrative position (transform). |
