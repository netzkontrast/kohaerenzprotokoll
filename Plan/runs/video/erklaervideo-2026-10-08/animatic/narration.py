"""Narration for the explainer animatic: one Piper WAV per sentence, one track per scene, timings as JSON.

Reads the '> ' lines under each '### N ·' heading of skript.md. '[Pause]' adds 0.6 s, '[lange Pause]' 1.4 s,
any other bracket is a stage direction and is dropped. Writes assets/vo/scene-N.wav and assets/vo/timings.json.
"""
import json, re, subprocess, sys, wave, struct
from pathlib import Path

SKRIPT, OUT, MODEL = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3]
GAP, PAUSE, LONG, LEAD, TAIL = 0.35, 0.6, 1.4, 0.5, 0.9
scenes, cur = {}, None
for line in SKRIPT.read_text(encoding="utf-8").splitlines():
    m = re.match(r"### (\d+) · ", line)
    if m: cur = int(m.group(1)); scenes[cur] = []; continue
    if cur and line.startswith("> "): scenes[cur].append(line[2:])

def tokens(text):
    """Sentences and pauses, in order."""
    out = []
    for part in re.split(r"(\[[^\]]*\])", text):
        if part.startswith("["):
            if part == "[Pause]": out.append(("pause", PAUSE))
            elif part == "[lange Pause]": out.append(("pause", LONG))
            continue
        for s in re.split(r"(?<=[.?!:])\s+(?=[A-ZÄÖÜ„\"])", part.strip()):
            if s.strip(): out.append(("say", s.strip()))
    return out

RATE = 22050
def silence(sec): return b"\x00\x00" * int(sec * RATE)
timings = {}
OUT.mkdir(parents=True, exist_ok=True)
for n, lines in scenes.items():
    pcm, t, caps = bytearray(silence(LEAD)), LEAD, []
    for kind, val in tokens(" ".join(lines)):
        if kind == "pause":
            pcm += silence(val); t += val; continue
        tmp = OUT / "_s.wav"
        subprocess.run(["piper", "-m", MODEL, "--length-scale", "1.08", "--sentence-silence", "0", "-f", str(tmp)],
                       input=val, text=True, check=True, capture_output=True)
        with wave.open(str(tmp)) as w:
            assert w.getframerate() == RATE and w.getsampwidth() == 2 and w.getnchannels() == 1
            frames = w.readframes(w.getnframes()); dur = w.getnframes() / RATE
        caps.append({"text": val, "start": round(t, 3), "end": round(t + dur, 3)})
        pcm += frames; t += dur
        pcm += silence(GAP); t += GAP
    pcm += silence(TAIL); t += TAIL
    with wave.open(str(OUT / f"scene-{n}.wav"), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(RATE); w.writeframes(bytes(pcm))
    timings[n] = {"duration": round(t, 3), "captions": caps}
    print(f"scene {n}: {t:6.2f} s, {len(caps)} sentences")
(OUT / "_s.wav").unlink(missing_ok=True)
(OUT / "timings.json").write_text(json.dumps(timings, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"total {sum(v['duration'] for v in timings.values()):.1f} s")
