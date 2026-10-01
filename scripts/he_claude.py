"""HyperExtract's model: Claude through `claude -p`, first party (decision 011) — standard library only.

A contract run is `hx.extract` (HyperExtract, ported: `scripts/hx.py`) with this model answering each chunk, then
`reading_extract.stage`. The model is asked for one JSON object that validates against the template's schema and hands
back the validated object — the one call HyperExtract's extraction chain makes, with the same message it made through
LangChain until 2026-10-01: the prompt with the chunk in it, then `JSON_ONLY` and the schema, and no system message.

- Every call goes through `claude_cli.call` (P6): no tools, no MCP, no settings,
  no `CLAUDE.md`, an empty working directory, thinking off.
- Every call is recorded in `Claude.calls` — seconds, tokens, cost, and
  `ok` or the failure's kind — so a run can say what it cost, including paid replies that fail validation and
  their retries (P15: a chunk that failed is `failed`, never a chunk with nothing in it).
- A reply that is not JSON, or does not validate, is asked for once more with
  the error named; a second failure raises, and `hx.extract` drops that chunk as
  HyperExtract did, which `reading_extract.candidates` refuses when no chunk survived.

    python3 scripts/he_claude.py run <slug> <template.yaml> --run <name> [--model haiku] [--gate] [--approval "<text>"]
    python3 scripts/he_claude.py selftest

`run` is the pipeline's HyperExtract pass on one document: `reading_extract.extract` with this model, then
`reading_extract.stage` into `Plan/runs/<slug>/hyperextract/<name>/`, with `calls.jsonl` and `usage.json` beside
the candidates. A run whose every chunk failed is recorded there too, with why, and staged nothing. A list, set or
graph template runs (`hx.RUNS`); a set and a graph merge by their identifiers, never with a model. `selftest` runs the
whole path on the committed fixture with a fake `claude`, offline.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import claude_cli  # noqa: E402

JSON_ONLY = ("Reply with exactly one JSON object and nothing else — no prose, no code fence. Copy every "
             "quotation character exactly as the text writes it: German quotation marks open with „ and close "
             "with “, never with a straight quote. It must validate against this JSON schema:\n")
# Haiku, copying „getaktet“, closes it with a straight quote — `„getaktet"` — which ends
# the JSON string it stands in (measured 2026-09-30: 3 of 5 calls unreadable, and
# `claude -p --json-schema` failed the same way five times). A straight quote right
# after a „-opened span with no closing mark is put back to the “ the source writes.
GERMAN_CLOSE = re.compile(r'„([^„“"\n]{0,400})"')


def parse_json(text: str) -> tuple[Any, int]:
    """(the object, how many German closing marks were put back to parse it)."""
    text = re.sub(r"^```(?:json)?\s*|\s*```$", "", text.strip())
    start, end = text.find("{"), text.rfind("}")
    if start < 0 or end < start:
        raise ValueError("no JSON object in the reply")
    body = text[start:end + 1]
    try:
        return json.loads(body), 0
    except json.JSONDecodeError:
        repaired, n = GERMAN_CLOSE.subn(r"„\1“", body)
        if not n:
            raise
        return json.loads(repaired), n


class Claude:
    """`claude -p` as the model `hx.extract` asks; `model` is a CLI alias (`haiku`, `sonnet`)."""

    def __init__(self, model: str = "haiku", thinking: int | None = 0, timeout: float = 300.0,
                 binary: str | None = None):
        self.model, self.thinking, self.timeout, self.binary = model, thinking, timeout, binary
        self.calls: list[dict] = []

    def _call(self, system: str, text: str) -> str:
        try:
            reply = claude_cli.call(self.model, system, text, thinking=self.thinking,
                                    timeout=self.timeout, binary=self.binary)
        except claude_cli.CallError as exc:
            self.calls.append({"ok": False, "kind": exc.kind, "error": str(exc)[:300]})
            raise
        usage = reply.get("usage") or {}
        self.calls.append({"ok": True, "seconds": reply.get("_seconds"),
                           "input": sum(int(usage.get(k) or 0) for k in
                                        ("input_tokens", "cache_read_input_tokens", "cache_creation_input_tokens")),
                           "output": int(usage.get("output_tokens") or 0),
                           "cost_usd": float(reply.get("total_cost_usd") or 0.0)})
        return str(reply.get("result") or "")

    def __call__(self, text: str, spec: str, check: Callable[[Any], dict]) -> dict:
        """One chunk: the prompt with the schema after it, a reply checked, asked once more on a failure."""
        asked = f"{text}\n\n{JSON_ONLY}{spec}"
        error = None
        for _ in range(2):
            reply = self._call("", asked if not error else
                               f"{asked}\n\nYour previous reply failed: {error}. Reply again, JSON only.")
            try:
                obj, repaired = parse_json(reply)
                if repaired:
                    self.calls[-1]["repaired_quotes"] = repaired
                return check(obj)
            except (ValueError, json.JSONDecodeError) as exc:
                error = str(exc)[:300]
                self.calls[-1]["ok"] = False
                self.calls[-1]["kind"] = "invalid"
        raise ValueError(f"no reply validated against the schema: {error}")


# --- offline self-test: the whole path with a fake `claude` ----------------------------------------------------------

FAKE = r'''#!/usr/bin/env python3
import json, os, sys
text = sys.stdin.read()
with open(os.environ["FAKE_CLAUDE_LOG"], "a", encoding="utf-8") as log:
    log.write(json.dumps({"argv": sys.argv[1:], "stdin": text}) + "\n")
reply = os.environ.get("FAKE_CLAUDE_REPLY", "")
if "failed:" in text and os.environ.get("FAKE_CLAUDE_SECOND"):
    reply = os.environ["FAKE_CLAUDE_SECOND"]
print(json.dumps({"type": "result", "is_error": False, "result": reply,
                  "usage": {"input_tokens": 100, "output_tokens": 20}, "total_cost_usd": 0.001}))
'''


def selftest() -> int:
    import os
    import stat
    import tempfile
    import hx
    import reading_extract
    cases = []
    folder = ROOT / "Plan" / "hyperextract" / "fixtures"
    text = (folder / "reading.txt").read_text(encoding="utf-8")
    template = ROOT / "Plan" / "hyperextract" / "TermReadings.yaml"
    t = hx.load(template)
    good = (folder / "TermReadings.json").read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory() as tmp:
        fake = Path(tmp) / "claude"
        fake.write_text(FAKE, encoding="utf-8")
        fake.chmod(fake.stat().st_mode | stat.S_IEXEC)
        os.environ["FAKE_CLAUDE_LOG"] = str(Path(tmp) / "log.jsonl")
        os.environ["FAKE_CLAUDE_REPLY"] = good
        llm = Claude(model="haiku", binary=str(fake))
        data = reading_extract.native_extract(template, text, llm)
        cases.append(("a validated reply becomes the template's items",
                      data == json.loads(good) and llm.calls and all(c["ok"] for c in llm.calls)))
        cases.append(("every call recorded with its cost", all("cost_usd" in c for c in llm.calls)))
        sent = json.loads((Path(tmp) / "log.jsonl").read_text(encoding="utf-8").splitlines()[0])
        want = hx.render(hx.prompt(t), source_text=text) + "\n\n" + JSON_ONLY + hx.spec(t)
        cases.append(("the model is sent HyperExtract's prompt, then the schema", sent["stdin"] == want))
        cases.append(("no system message, as LangChain's one human message had none",
                      "--system-prompt" not in sent["argv"] or
                      sent["argv"][sent["argv"].index("--system-prompt") + 1] == ""))
        os.environ["FAKE_CLAUDE_REPLY"] = "Gern, hier ist die Antwort: keine."
        os.environ["FAKE_CLAUDE_SECOND"] = good
        llm = Claude(model="haiku", binary=str(fake))
        data = reading_extract.native_extract(template, text, llm)
        cases.append(("prose first, JSON when asked again: one retry, recorded",
                      data == json.loads(good) and [c["ok"] for c in llm.calls][:2] == [False, True]))
        retry_usage = claude_cli.totals(llm.calls)
        cases.append(("invalid reply and retry both count as paid calls",
                      retry_usage["cost_usd"] == round(sum(c["cost_usd"] for c in llm.calls), 4)
                      and retry_usage["input_tokens"] == 100 * len(llm.calls)
                      and retry_usage["failed_calls"] >= 1))
        obj, n = parse_json('{"quote": "sondern „getaktet" ist", "stance": "asserts"}')
        cases.append(("a German span closed with a straight quote is repaired, and counted",
                      obj["quote"] == "sondern „getaktet“ ist" and n == 1))
        obj, n = parse_json('{"quote": "plain \\"words\\" here"}')
        cases.append(("valid JSON is left alone", obj["quote"] == 'plain "words" here' and n == 0))
        os.environ["FAKE_CLAUDE_REPLY"] = json.dumps({"items": [{"term": "x", "quote": None, "stance": "asserts"}]})
        os.environ.pop("FAKE_CLAUDE_SECOND", None)
        llm = Claude(model="haiku", binary=str(fake))
        data = reading_extract.native_extract(template, text, llm)
        cases.append(("a reply that fails the schema twice empties its chunk",
                      data == {"items": []} and [c["kind"] for c in llm.calls] == ["invalid", "invalid"]))
        os.environ["FAKE_CLAUDE_REPLY"] = "Gern, hier ist die Antwort: keine."
        llm = Claude(model="haiku", binary=str(fake))
        data = reading_extract.native_extract(template, text, llm)
        try:
            reading_extract.candidates(data)
            cases.append(("prose twice: the chunk empties and staging refuses it", False))
        except ValueError:
            cases.append(("prose twice: the chunk empties and staging refuses it",
                          not any(c["ok"] for c in llm.calls)))
    failed = [n for n, ok in cases if not ok]
    print(f"he_claude: {len(cases) - len(failed)} of {len(cases)} cases hold"
          + (" — FAILED: " + ", ".join(failed) if failed else "") + "; offline, a fake claude")
    return 1 if failed else 0


APPROVAL = ("decision 011 (Claude, first party); the author's instruction of 2026-09-30 to put "
            "HyperExtract into the pipeline and read with Haiku")


def run(slug: str, template: Path, name: str, model: str = "haiku", binary: str | None = None, gate: bool = False,
        approval: str | None = None) -> int:
    """One document through one template with Claude, staged, every call recorded. `gate` sends the model
    only the paragraphs that hold a cue of the contract (`hegraph.gate`) and records the share in `usage.json`.
    `approval` is what the record says licensed the run: the default is the author's instruction of 2026-09-30 to
    put HyperExtract into the pipeline; a run under a later instruction names it (the backfill does)."""
    import tempfile
    import hx
    import reading_extract
    from subject import document
    if hx.load(template).type not in hx.RUNS:
        raise SystemExit(f"{template.name}: only {', '.join(hx.RUNS)} templates run here")
    doc = document(slug)
    text = None
    if gate:
        import hegraph
        text = hegraph.gate(doc.body, template.stem)
    llm = Claude(model=model, binary=binary)
    target = ROOT / "Plan" / "runs" / doc.slug / "hyperextract" / name
    failed = None
    try:
        envelope = reading_extract.extract(template, doc, llm, f"claude-cli/{model}", text)
    except ValueError as exc:
        failed, status = str(exc), 1
    if failed is None:
        with tempfile.TemporaryDirectory() as tmp:
            export = Path(tmp) / "export.json"
            export.write_text(json.dumps(envelope, ensure_ascii=False, indent=2), encoding="utf-8")
            status = reading_extract.stage(doc, template, export, name)
    else:
        target.mkdir(parents=True, exist_ok=False)
    usage = {"document": doc.slug, "template": template.name, "model": f"claude-cli/{model}",
             **claude_cli.totals(llm.calls),
             "approval": approval or APPROVAL}
    if gate:
        usage["gate"] = {"characters_sent": len(text), "characters_in_document": len(doc.body),
                         "share": round(len(text) / max(len(doc.body), 1), 3)}
    if failed:
        usage["failed"] = failed
    (target / "usage.json").write_text(json.dumps(usage, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (target / "calls.jsonl").write_text("".join(json.dumps(c, ensure_ascii=False) + "\n" for c in llm.calls),
                                        encoding="utf-8")
    print(json.dumps(usage, ensure_ascii=False))
    return status


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    if argv[:1] != ["run"]:
        print(__doc__)
        return 2
    import argparse
    ap = argparse.ArgumentParser(prog="he_claude.py run")
    ap.add_argument("slug")
    ap.add_argument("template", type=Path)
    ap.add_argument("--run", required=True)
    ap.add_argument("--model", default="haiku")
    ap.add_argument("--binary")
    ap.add_argument("--gate", action="store_true", help="send only the paragraphs that hold a cue of the contract")
    ap.add_argument("--approval", help="what licensed the run, if not the default of APPROVAL")
    a = ap.parse_args(argv[1:])
    return run(a.slug, a.template, a.run, a.model, a.binary, a.gate, a.approval)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
