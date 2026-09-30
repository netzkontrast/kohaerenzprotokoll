"""Assemble Sources/notes/<slug>.md: frontmatter from the manifest-derived header (never typed),
the four note keys, and the hand-written body."""
import re
from pathlib import Path

ROOT = Path("/home/user/kohaerenzprotokoll")
SP = Path("/tmp/claude-0/-home-user-kohaerenzprotokoll/9312df84-970d-5f58-8110-95cdece16e80/scratchpad")
S = "technical-audit-research-mandate-the-kohaerenz-protokoll-fra"

header = (SP / "header.md").read_text(encoding="utf-8")
front = header.split("---\n")[1]
keep = [l for l in front.split("\n") if re.match(r"(source|drive_id|title|category):", l)]
assert len(keep) == 4, keep

markers = ["Research Mandate -", "Architectural Mandate", "Critical Consistency Takeaways",
           "Stress-Test Requirement", "Theoretical Mathematical Claim", "Narrative Requirement",
           "Alignment Status", "Prescribed", "Mandated", "Required", "Verified",
           "Strategic Executive Summary", "Final Synthese Verdict",
           "definitive structural requirements", "structurally verified", "ready for publication"]
marker_list = "[" + ", ".join('"' + m + '"' for m in markers) + "]"

read = ("L1-L40, the whole document. Read on 2026-09-29 by a document-reader subagent (Sonnet), who wrote the "
        "candidate list before any count and drafted this note until a usage limit stopped it; read again on "
        "2026-09-30 by a second document-reader subagent (Sonnet), who checked every quotation and every number "
        "of the draft against the document and finished the note.")
reads_as = ("an audit brief addressed to a writer and a writer LLM: instructions, claims about the world and "
            "borrowed theory in one voice, closing on its own verdict of verified and ready")

lines = ["---"] + keep + [
    f'read: "{read}"',
    f"stance_markers: {marker_list}",
    "stance_marker_count: 22   # occurrences of the 16 markers above, each counted in 05-verify.txt, section C",
    f'reads_as: "{reads_as}"',
    "---", ""]
body = (SP / "note-template.md").read_text(encoding="utf-8").replace("SLUG", S)
text = "\n".join(lines) + "\n" + body
(ROOT / "Sources" / "notes" / f"{S}.md").write_text(text, encoding="utf-8")
print("wrote note:", len(text), "chars,", text.count("\n"), "lines; markers:", len(markers))
