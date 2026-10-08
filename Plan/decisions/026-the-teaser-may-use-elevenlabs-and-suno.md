# 026 — The book teaser may send its text to ElevenLabs and Suno

**Date:** 2026-10-08 · **Decided by:** the author — asked „Darf Text an ElevenLabs oder Suno gehen?", answered „ja", with the teaser named as a book teaser, 9:16, about five minutes · **Status:** chosen for ElevenLabs; for Suno, chosen in principle, its route open (below); reversible by the author at any time

## What was chosen

The author asked for a video for the novel and for OpenMontage to be installed for it (`scripts/install.sh openmontage`,
`.agents/skills/openmontage/`). The rule that no corpus text leaves the container without the author's decision
(decisions 007, 008, 011) covers the teaser's text too, because a narration script for the novel quotes or retells it.

| provider | what may reach it | through |
|---|---|---|
| ElevenLabs (`api.elevenlabs.io`) | the teaser's narration script, sentence by sentence, for speech; the music prompts and lyrics written for the teaser, for music | OpenMontage's `elevenlabs_tts` and `music_gen`, key `ELEVENLABS_API_KEY` |
| Suno | the lyrics and style prompts written for the teaser | see *Suno's route* |

**The teaser's text** is text written for the teaser: its narration script, its lyrics, its prompts. It may quote or
retell what `Manuscript/kanon.md` holds and what the author has approved. It is not a document from `Sources/`, a wiki
page, a census or a note, and none of those is sent whole or in bulk.

## Suno's route

Suno publishes no API. OpenMontage's `suno_music` calls `api.sunoapi.org` (`.openmontage/tools/audio/suno_music.py`,
at the pinned commit), a reseller that is not Suno. The author's „ja" named Suno, so that reseller waits on its own yes
(`NOW.md`, *Questions for the author*). Until then the route is the author's own Suno account: a session writes the lyrics and
style prompts (the skill `suno-lyric-writer`), the author generates the track in Suno, and the file is added to the project.

## How it is held

- Keys come from the environment's settings, never from a file. The installer writes no `.env` into `.openmontage/`.
- Before each paid call the session names the tool, the provider, the model and whether the call is a sample or a
  batch, by OpenMontage's own *Decision Communication Contract* (`.openmontage/AGENT_GUIDE.md`). The project's
  `decision_log` keeps the record.
- The cost is the author's. A run is priced before it starts with OpenMontage's `estimate_cost`.
- Piper with `de_DE-thorsten-high` stays the local voice for drafts. It costs nothing and sends nothing.

## What it does not cover

- Every other provider OpenMontage can reach: Veo, Kling, FAL, OpenAI, Runway, HeyGen, Google TTS and the rest. Each
  waits on its own yes.
- Any text that is not the teaser's.
- Canon. What the teaser shows decides nothing about the novel: a scene the teaser tells is not canon because it was
  filmed.

## What would change our mind

- The author narrows or withdraws the yes.
- A provider's terms say that what is sent trains its models, and the author does not want that.
