"""Pack text and meta of the 24 frozen cases, for a before/after comparison."""
import hashlib, json, sys
sys.path.insert(0, "scripts")
import ask, askdb, benchset, graph as kg, graphrag
s, g = askdb.Store(), kg.build()
out = {}
for c in benchset.cases():
    text, meta = ask.build_pack(c["question"], "position", ask.BUDGET, s, graphrag.without(g, c["key"]))
    out[c["id"]] = {"sha": hashlib.sha256(text.encode()).hexdigest(), "chars": len(text), "bytes": len(text.encode()),
                    "shown": meta["shown"], "sent": meta["sends_text_of"], "cut": meta["cut_by_budget"],
                    "meta_keys": sorted(meta)}
json.dump(out, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
print(len(out), "cases; mean bytes", sum(v["bytes"] for v in out.values()) // len(out), "max", max(v["bytes"] for v in out.values()))
