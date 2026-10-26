# `netzkontrast/agency` read against this repository — 2026-10-26

The author asked to look into the agency repository (commit `1ab22a2`, read-only clone, nothing run). A first survey by
an Explore agent is folded into `Plan/concept/session-apps_2026-10-26.md` §10; this note records what a direct read of
its **`novel` capability** found, because that capability is written about this novel.

## What it is

`agency/capabilities/novel/` — about 170 verbs in 19 clusters (7,027 lines), node schemas, templates, the Dramatica
ontology, NCP **1.3.0** (this repository uses NCP 3.0.0-rc.1), five plot structures, and `kp-fragments.yaml` (KP-only
drafting prompt fragments, among them one per kind of part). Its design (`data/reference/kohaerenz-synthesis.md`):
**graph canonical, disk derived**, human prose the one disk-canonical exception — the reverse of this repository, where
files are the authority and the graph a view (CLAUDE.md, decision 021). Its worked example
(`examples/kohaerenz-protokoll/`) is six documents of the 2026-06-10 set, 81–96 % like the landed sources of that date
(`*-2026-06-10-md.md`), not byte-identical. The specs 136–141 that wrote the KP rules cite those six files.

## Where it overlaps what this repository built

| agency verb(s) | here | difference |
|---|---|---|
| `register_project_rule`, `run_project_rules`, `project_rule_gate` | `prose_rules.py` (decision 030) | ours carries status and the author's words per rule; theirs severity only |
| `propose_canon`, `approve_canon` (human-only, monotonic), `record_lock` (supersede, never delete), `lock_index`, `canon_gate` | `weiche.py answer`, `kanon.md`, `manuscript.py approve` | same doctrine: an agent proposes, a person approves; theirs refuses `managed_agent` as approver |
| `record_character_learns`, `what_does_X_know_as_of`, `flag_anachronistic_reference`, `story_time_query`, `events_pov_witnessed` | `continuity.py` (wissen, zeit) | theirs is a typed graph with a temporal-cycle check; ours four tables per chapter |
| `render_chapter_briefing`, `briefing_checklist`, `pre_draft_gate`, `preflight_report` | `brief.py` | similar contract; ours separates `[K]`/`[V]`/`[S]`/`[D]` |
| `create_storyform_set`, `route_scene_storyform` (hard / soft bridge), `record_storyform_transition` (Vortex), `bridge_frequency_report` | `weave.json`, `storyform.py` | the same idea of A/B routing and bridge chapters |
| `set_reveal_rule`, `check_reveal_timing`, `check_veil`, `record_leerstelle`, `reveal_gate` | not built | a reveal floor per fact and a „veil“ of terms forbidden before a chapter |
| `create_voice_profile`, `score_voice_match`, `voice_drift_gate`, `switching_log`, `check_alter_recognition` | not built | voice per part, recognised by syntax and body, never labelled |
| `plant_anchor`, `pay_off_anchor`, `anchor_status_report`, `record_motif_echo` | not built | open foreshadowing debt; motif stacking cap |
| `check_filter_words`, `check_show_dont_tell`, `check_pov_consistency`, gates developmental → line → copy | the writing skills (judgement, not code) | theirs are counters; ours readings |
| `generate_scene_body` | none, on purpose | decision 030: a session writes on beats the author approved; no verb writes prose unasked |

## A measurement: their Klein-c rule against the approved storyforms

`check_klein_c_inversion` (`clusters/dual_storyform.py`) requires the class pair swapped **and all eight dynamics
inverted** between primary and secondary storyform. Run by hand on `Plan/storyform/a.json` and `b.json`:

| | A | B | inverted |
|---|---|---|---|
| classes MC/OS | Mind / Psychology | Universe / Physics | yes |
| driver, outcome, judgment, limit, style, resolve, approach | Decision, Success, Good, Optionlock, Holistic, Change, Be-er | Action, Failure, Bad, Timelock, Linear, Steadfast, Do-er | yes, 7 of 7 |
| growth | **Stop** | **Stop** | **no** |

A's Growth is Stop **by the author's decision** (step 16 of decision 025: Start + Be-er broke rule D1, „the author changed
A's growth to Stop“). Their check would fail the approved storyforms on that slot. The source it rests on asks less: the
canon reset of 2026-04-30 tables only the **domain** inversion („Vier saubere Domain-Inversionen“,
`kohaerenz-protokoll-struktur-kanon-reset-2026-04-30-md.md` L219) and retires the Klein-four mapping as a world mechanic
(L584: „War Verifikationswerkzeug der Architektur, hat im Roman keine Funktion.“). So: their rule is stricter than its
source and contradicts a later author decision. Not a defect here; a finding for agency.

## Privacy and the corpus

- agency is a public repository. Its example folder carries the 2026-06-10 corpus documents; one line of
  `02_begriffe-und-konzepte.md` holds an early name barred here (decision 028). Counted, not printed.
- Other hits of the barred surfaces in agency are unrelated: NCP specification examples and the music capability's
  artist pages.
- This session sent nothing there: the clone is read-only, nothing was run, nothing pushed.

## What to take, if the author wants it

1. **Reveal floors and the veil** — a per-fact „not before chapter N“ and a list of terms barred before a chapter, as a
   check in `continuity.py` or `prose_rules.py`; the clinical terms and the reveal of the parts are this book's central
   timing.
2. **Voice profiles per part** with a match score — as queries, never as a gate on the author's prose.
3. **Anchors**: planted and unpaid foreshadowing as an open-debt list in the briefing.
4. **Supersede, never delete** for answers and locks — already proposed for the session records (§10 of the concept).

Not to take: the graph as the store of record, NCP 1.3.0, `generate_scene_body`, the Klein-c dynamics rule as written.
