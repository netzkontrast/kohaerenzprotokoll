import runpy, re, sys
sys.argv = ["x"]
g = runpy.run_path("/tmp/claude-0/-home-user-kohaerenzprotokoll/66b98e2f-1db4-55b3-b80a-cb16b5459113/scratchpad/build_chunk.py")
NODES, EDGES, LINES, CH, rng, KEY = g["NODES"], g["EDGES"], g["LINES"], g["CH"], g["rng"], g["KEY"]
plain = g["plain"]
inv = {v: k for k, v in KEY.items()}
# 1) chapter-sourced edges must sit inside that chapter, except the mode/OQ/transition ones sourced elsewhere
chap_of = {KEY[f"C{n}"]: n for n in range(41)}
bad = []
for e in EDGES:
    if e["source"] in chap_of:
        n = chap_of[e["source"]]
        lo, hi = rng(n)
        ln = int(e["source_location"][1:])
        if not (lo <= ln <= hi):
            bad.append((inv[e["source"]], inv[e["target"]], e["source_location"], LINES[ln-1][:90]))
print("chapter edges outside their chapter:", len(bad))
for b in bad: print("  ", b)
# 2) node label (core word) visible on its line
print("\nnode lines where the label's core is not on the line:")
for nid, n in NODES.items():
    ln = int(n["source_location"][1:])
    text = plain(LINES[ln-1]).lower()
    core = re.split(r" \(| — |/", n["label"])[0].strip("„\"").lower()
    if core and core not in text:
        print(f"  {inv[nid]:14} {n['source_location']:6} {n['label'][:50]!r:52} | {LINES[ln-1][:70]!r}")
