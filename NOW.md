# Now

The current handover, in execution order. History is in git; author questions are in `Plan/questions-for-the-author.md`. Counts come from `python3 scripts/state.py`, never from this page. Read `CLAUDE.md` for startup and standing operating rules.

## The author's standing instructions

- 2026-10-13 **AEGIS agent and interactive-novel planning:** prepare a PR, simplify NOW.md/CLAUDE.md and align the skill review with the new Claude instructions. The offline pilot is the proposed next implementation; no simulation output becomes canon.
- 2026-10-05 **Ingest in batches of ten:** prioritize unread sources named by open conflicts, then the canon era, then date. Complete and reconcile each document before the next. Use a light pass for prompts/templates/near-duplicates. Stop and report after a batch, a new conflict record, or a check still red after one fix. At most one chapter-relevant question per document; keep the app current after each document.
- 2026-10-05 **Up to two parallel Sonnet ingest readers:** census/note reading may overlap; reconciliation, readings and commits stay sequential in queue order. Other model calls remain serial and recorded.
- 2026-10-06 **Remove hook for App Check:** keep app-refresh available; no mandatory pre-PR hook. New app content must have an address, agent export and useful interaction.
- 2026-10-05 **Manuscript is the novel workspace:** decisions in `Manuscript/kanon.md`; drafts and cards are working material. Approved storyform wins over drafts. Sources and Legacy prose are research, never an automatic voice reference or canon.
- 2026-09-30 **Stop the unhelpful HyperExtract backfill:** decision 019 and its STOP file remain in force.
- 2026-09-24 **Note questions and continue:** continue independent work; do not invent an answer to unblock a dependent decision. Third-party corpus transfer still needs the author's decision (007/008/011).

## Questions for the author — noted, not waited on

Read `Plan/questions-for-the-author.md` for the full record. Resolve only the choice required by the current operation.

- Writing ownership and source reading while drafting: `Plan/concept/novel-writing-plan_2026-09-29.md` §11. `Manuscript/` is already chosen; do not ask that again.
- Remaining plot Weichen and treatment approval: `Plan/runs/storyform-2026-10-06/entscheidungsvorlage.md`, `Plan/weichen/`, `Manuscript/kanon.md`. W0 and Q8 are answered; earlier cards may be stale.
- Retrieval defaults, independent gold and model experiments: `Plan/concept/graph-contracts_2026-09-30.md`, `Plan/concept/evaluation-audit_2026-09-30.md`, `SPEC.md` §9. The E4 allowance is specific, not general model permission.
- Third-party audio transcription, entity lists and translation pairs: the author-question record and decisions 007/008/011; no new permission is implied here.
- Promotion, German term pages and scheduling: `Plan/concept/promotion_2026-10-08.md`, `Plan/concept/wiki-terms_2026-10-08.md`, `Plan/concept/agent-sessions_2026-10-05.md`.
- AEGIS adaptation choices: playable viewpoint, fixed ending versus variant and AEGIS' knowledge/voice; `Plan/briefings/aegis-agent-pilot.md`. Mark pilot assumptions rather than reopening decided canon.

## Half-done — where the next session starts

- **AEGIS agent pilot** — proposed implementation from the author's 2026-10-13 planning request. Read `Plan/briefings/aegis-agent-pilot.md` and `Plan/concept/aegis-agent_2026-10-13.md`. **Next:** define two manual cases and implement their offline perception/action/event/replay loop before adding any live model or playable UI.
- **The storyforms, step by step with the author** — approved structure in `Plan/storyform/`; content decisions in `Manuscript/kanon.md`; treatment and chapter execution remain proposals where not approved. `Plan/runs/storyform-2026-10-06/entscheidungsvorlage.md` orders remaining choices. **Next:** hold the joint decision session, then approve the treatment act by act before deriving NCP events from those approved paragraphs.
- **The architecture is [`SPEC.md`](SPEC.md), adopted by the author** — decision 021; offline migration steps are built. Optional finders stay optional. **Next:** design and run step 8 E4, fixed pack versus bounded expansion versus RLM at equal total cost, Claude only, serial, within the specific $20 allowance and read evidence only.
- **The ingest continues past step 6** — the sample is reconciled and the 2026-10-05 pause is lifted. Choose the next unread source from current records, not an old batch number; run `account.py order` and inspect source/claim status. Follow `.agents/skills/ingest/SKILL.md`. **Next:** select and claim the next unread source by the standing priority, complete its reconciliation and checks, and stop after the authorized batch.
- **The HyperExtract work is measured and nothing is adopted** — proposal contracts in `Plan/hyperextract/`; stopped backfill in `Plan/runs/hyperextract-backfill-2026-09-30/STOP`. Resumption is only with the author's word; `backfill.py status` reports remaining work.
- **Gold for learnings** — `Plan/runs/gold-2026-09-30/README.md` and `Plan/concept/evaluation-audit_2026-09-30.md` §5 hold the cases and ceiling problem. **Open:** a second blind relation reader on the existing pilot documents, one recorded model run at a time, before extending the sample.
- **Entity lists** — `scripts/entities.py` exists; measure current lists with `state.py`, not prose. The corpus-wide run waits on the author's yes for its model path and transfer scope.
- **NCP plot development** — `Plan/storyform/development.json` and `Plan/runs/writing/book/plot-development_2026-10-06.md` hold proposal-only goals, actions, costs and knowledge. **Next:** compare the proposed deletion targets for Kap 1/12/13, carry the 06:10 consequence into Kap 2, and prepare the concrete recovery, lost return path and filter choices for Kap 19/20/24.

## Verification

Run the CI steps in `.github/workflows/checks.yml`; report failures and unavailable suites individually. NOW changes also require session derivation and app-refresh. No branch or previously green result is a current completion claim. Session claims and active work are derived by `python3 scripts/sessions.py board`.
