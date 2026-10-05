"""The query words each lexical finder built for the 24 frozen questions, before and after SPEC.md step 5.

The three builders as they stood at `63f857d8` are copied here verbatim (`OLD`), so this file can show the
difference after the code changed; `NEW` is `askdb.query_words`, the one function that replaced them.

    python3 Plan/runs/query-words-2026-10-02/words.py      # prints, writes words.json
"""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import askdb  # noqa: E402
import benchset  # noqa: E402

ASKDB_STOP = set("der die das und oder ein eine einer eines ist sind wird werden wie was wer wann wo "
                 "warum welche welcher welches mit von zu im in am an auf aus für bei nicht nur auch "
                 "the a an of and or is are to in on for what when who how why which".split())
LEX_DE = set("der die das und ist nicht ein eine zu den von mit sich des auf für im dem als auch es an werden aus er hat "
             "dass sie nach wird bei einer um am sind noch wie einem über einen so zum war haben nur oder aber vor zur "
             "bis mehr durch man sein wurde sei kann ihre seine diese dieser dieses wenn was wo".split())
LEX_EN = set("the and of to a in is that it for as with was on be by are this not or from at which an but have has "
             "their its can will they we were been these more such into than how what when".split())
OLD = {
    "ask/bm25rel (askdb.fts_query)": lambda t: list(dict.fromkeys(
        w for w in re.findall(r"\w[\w-]*", t) if len(w) > 2 and w.lower() not in ASKDB_STOP)),
    "kg.search": lambda t: re.findall(r"\w+", t),
    "novelgraph Index.bm25": lambda t: [w.lower() for w in re.findall(r"[^\W_][\w]*", t)
                                        if w.lower() not in LEX_DE | LEX_EN and len(w) > 1],
}

if __name__ == "__main__":
    out = {}
    for c in benchset.cases():
        q = c["question"]
        new = askdb.query_words(q)
        row = {"question": q, "new": new}
        for name, fn in OLD.items():
            old = [w.lower() for w in fn(q)]
            row[name] = {"old": old, "added": [w for w in new if w not in old],
                         "dropped": [w for w in dict.fromkeys(old) if w not in new]}
        out[c["id"]] = row
    (HERE / "words.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for name in OLD:
        added = sum(len(r[name]["added"]) for r in out.values())
        dropped = sum(len(r[name]["dropped"]) for r in out.values())
        same = sum(1 for r in out.values() if not r[name]["added"] and not r[name]["dropped"])
        print(f"{name:32} questions unchanged {same:2}/24, words added {added:3}, dropped {dropped:3}")
        for cid, r in out.items():
            if r[name]["added"] or r[name]["dropped"]:
                print(f"   {cid:4} +{r[name]['added']} -{r[name]['dropped']}")
