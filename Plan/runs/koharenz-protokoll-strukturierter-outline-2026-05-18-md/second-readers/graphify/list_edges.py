import runpy, sys
sys.argv = ["x"]
g = runpy.run_path("/tmp/claude-0/-home-user-kohaerenzprotokoll/66b98e2f-1db4-55b3-b80a-cb16b5459113/scratchpad/build_chunk.py")
KEY, EDGES, LINES = g["KEY"], g["EDGES"], g["LINES"]
inv = {v: k for k, v in KEY.items()}
seen_pairs = set()
for e in EDGES:
    s, t = inv[e["source"]], inv[e["target"]]
    if s.startswith("C") and s[1:].isdigit():
        continue
    if s in ("m1", "m2", "m3") and t.startswith("C"):
        continue
    ln = int(e["source_location"][1:])
    tag = {"EXTRACTED": "X", "INFERRED": "I", "AMBIGUOUS": "A"}[e["confidence"]]
    print(f"{s:>13} -> {t:<14} {tag}{e['confidence_score']:<4} L{ln:<5} {g['plain'](LINES[ln-1])[:75]}")
