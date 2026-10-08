---
name: openmontage
description: Produce a video for Kohärenz Protokoll — the book teaser first — with OpenMontage, the agentic video studio installed in .openmontage/ (netzkontrast/OpenMontage, pinned). Covers starting it in this container, which of its tools work here without a key, the German voice, rendering 9:16 with HyperFrames, which providers may receive the teaser's text (decision 026), and where a production's files go. Use when asked for a video, teaser, trailer, Reel, voice-over, soundtrack or storyboard for the novel.
---

# OpenMontage, in this repository

OpenMontage turns the session into a video studio. It is **instruction-driven**: its intelligence lives in its own
`AGENT_GUIDE.md`, the pipeline manifests in `pipeline_defs/`, and the stage-director skills in `skills/`. Its
Python only supplies tools and checkpoints. This skill adds what holds in *this* repository: how to start it here, what
was measured to work, and the rules that are ours, not OpenMontage's.

**Read `.openmontage/AGENT_GUIDE.md` before the first production step.** Its Rule Zero holds: every production goes
through a pipeline, stage by stage, each stage's director skill read first.

## Starting it

```bash
bash scripts/install.sh openmontage    # pinned clone, .venv, Remotion's node_modules, the German voice, HyperFrames' Chrome
cd .openmontage
export PATH="$PWD/.venv/bin:$PATH" DO_NOT_TRACK=1 HYPERFRAMES_SKIP_SKILLS=1
python -c "from tools.tool_registry import registry; import json; registry.discover(); print(json.dumps(registry.provider_menu(), indent=2))"
```

- **`PATH` carries `.venv/bin`.** Without it `piper_tts` reports itself unavailable, because it looks for the `piper`
  command on `PATH`.
- **`DO_NOT_TRACK=1`.** HyperFrames sends anonymous telemetry unless told not to.
- **The working directory is `.openmontage/`.** Its tools, its `projects/` workspaces and the Piper voice resolve from
  there.
- The whole of `.openmontage/` is git-ignored and disappears with the container (`CLAUDE.md`, *A fresh container*).

## What works here, measured 2026-10-08

The container has 4 CPUs, 15 GB RAM, no GPU, and no provider key set.

| capability | state |
|---|---|
| Composing and rendering with **HyperFrames** (HTML + GSAP) | works: 1080×1920 with audio, a 4.2 s clip rendered in 12.4 s, so about 3× real time on CPU |
| **German voice, local**: `piper_tts` with `model: de_DE-thorsten-high` | works, writes a WAV, sends nothing |
| Subtitles (`subtitle_gen`), audio mixing (`audio_mixer`, `audio_enhance`), analysis (`video_analyzer`, `scene_detect`, `frame_sampler`, `visual_qa`), `color_grade`, `video_stitch`, `video_trimmer`, `auto_reframe`, `threejs_world`, `diagram_gen`, `pixabay_music` | listed as available by the registry; not yet exercised |
| **Remotion** (`render_demo.py`, `video_compose` with `render_runtime: remotion`) | **fails here**: Remotion starts its browser with `--no-proxy-server`, the only way out of this container is the agent proxy, and every Google Font then fails with `ERR_CERT_AUTHORITY_INVALID`. A composition that loads no remote font may render; none was tried. On the author's machine Remotion is unaffected. |
| Image and video generation, cloud TTS, music | each needs a key (`.env.example` names them); none is set |

When AGENT_GUIDE.md's *Present Both Composition Runtimes* rule applies, say that Remotion cannot render here and why,
and record that as `rejected_because` in the `render_runtime_selection` decision.

## The rules that are this repository's

1. **What may leave the container (decision 026).** The teaser's own text may go to **ElevenLabs**: its narration
   script, and the music prompts and lyrics written for it. The same text may go to **Suno**, but only through the
   author's own Suno account (lyrics and prompts from the skill `suno-lyric-writer`). OpenMontage's `suno_music` calls
   `api.sunoapi.org`, a reseller that waits on its own yes. Every other provider (Veo, Kling, FAL, OpenAI, Runway and
   the rest) waits on its own yes. A document from `Sources/`, a wiki page, a census or a note is never sent.
2. **Keys come from the environment's settings, never a file.** No `.env` is written into `.openmontage/`. A key
   absent from the environment means the provider is off; say so and continue with the local tools.
3. **Canon decides what the teaser may tell.** Its content comes from `Manuscript/kanon.md` and what the author has
   approved. The storyforms in `Plan/storyform/` and the treatment are proposals. A wiki reading is never content.
   A scene the teaser shows does not become canon by being filmed.
4. **Announce before paying.** Before each paid call, OpenMontage's *Decision Communication Contract* applies: name the
   tool, the provider, the model, and whether it is a sample or a batch. Model and generation runs go one at a time,
   by the author's standing instruction of 2026-09-30.
5. **What a production keeps.** OpenMontage writes its workspace to `.openmontage/projects/<id>/`, which is not
   committed and dies with the container. The script, the storyboard, the decision log and the shot list are text: copy
   them to `Plan/runs/video/<id>/` and commit them there. Media go to the author, never into git: the render as an
   Artifact asset, or whatever the author names.

## Provisional

```yaml
skill: openmontage   # provisional — written from one install and two test renders, before any production
                     # may not: decide the teaser's content, send any text outside decision 026, commit media
                     # retire when: a production runs end to end and shows this page wrong or unnecessary
```
