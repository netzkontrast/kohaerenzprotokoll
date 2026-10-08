# 027 — The explainer's narration may go to ElevenLabs

**Date:** 2026-10-08 · **Decided by:** the session, on the author's delegation — asked five questions about a five-minute
explainer video, the author answered „Beantworte dir die Fragen selbst“ · **Status:** chosen; reversible by the author at any time

## What was chosen

Decision 026 lets the book teaser's own text go to ElevenLabs. The explainer (`Plan/runs/video/erklaervideo-2026-10-08/`) is a
second production, and 026 does not cover it. The session answered the voice question by the narrowest rule that still gives the
explainer a produced voice:

- **What may reach ElevenLabs:** the explainer's narration as written in `skript.md`. It describes the project's method, what
  sources say and what the author decided.
- **The guard:** the narration contains **no twelve consecutive words of a landed document**. That is the rule `scripts/route.py`
  already applies before a free model may see text (decision 011), so one threshold holds in both places. The short phrases the
  script quotes („bei Konflikt gewinnt das Neuere“, five words) stay under it.
- **What stays local:** every quotation plate on screen. It is set in HTML and rendered in the container, and nothing sends it
  anywhere.
- **How it is held:** the key comes from the environment (`ELEVENLABS_API_KEY`), and each paid call is announced and priced
  first, as in decision 026. Until the key is set, Piper speaks the animatic.

## What was rejected

- **Piper only, final as well.** It costs nothing and sends nothing, but a five-minute explainer in a synthetic voice that
  stumbles over coined terms („Kohärenz-Protokoll“, „Guardians“) works against the point of the video. Piper stays the voice of
  the animatic.
- **Reading quotations aloud.** Every quotation the script needs is shown on screen, not spoken. That keeps the guard simple, and
  it suits the design (Modus Lesen).

## What would change our mind

- The author narrows or withdraws it.
- The guard finds a twelve-word run in a revised script. That run is cut or moved to the screen before the call.
