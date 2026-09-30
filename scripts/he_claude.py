"""HyperExtract's chat model: Claude through `claude -p`, first party (decision 011).

`reading_extract.extract()` takes the caller's LangChain clients and leaves the
provider to the caller (PR #124). This is that provider for Claude: a
`BaseChatModel` whose `with_structured_output(schema)` — the one call
HyperExtract's extraction chain makes — asks `claude -p` for one JSON object
that validates against the template's schema, and hands back the validated object.

- Every call goes through `claude_cli.call` (P6): no tools, no MCP, no settings,
  no `CLAUDE.md`, an empty working directory, thinking off.
- Every call is recorded in `ClaudeChat.calls` — seconds, tokens, cost, and
  `ok` or the failure's kind — so a run can say what it cost, including paid replies that fail validation and
  their retries (P15: a chunk
  that failed is `failed`, never a chunk with nothing in it).
- A reply that is not JSON, or does not validate, is asked for once more with
  the error named; a second failure raises, and HyperExtract logs and empties that
  chunk, which `reading_extract.candidates` refuses when no chunk survived.

It runs in HyperExtract's interpreter (`templates.he_python()`), which has
LangChain; both commands below find that interpreter themselves.

    python3 scripts/he_claude.py run <slug> <template.yaml> --run <name> [--model haiku] [--gate] [--approval "<text>"]
    python3 scripts/he_claude.py selftest

`run` is the pipeline's HyperExtract pass on one document: `reading_extract.extract`
with this model and fake embeddings (a list template's merge is a plain append, and
no search index is built), then `reading_extract.stage` into
`Plan/runs/<slug>/hyperextract/<name>/`, with `calls.jsonl` and `usage.json` beside
the candidates. A run whose every chunk failed is recorded there too, with why,
and staged nothing. Only list templates: a graph template's node merge would lean
on the embeddings. `selftest` runs the native factory, feed and merge on the
committed fixture with a fake `claude`, offline.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import claude_cli  # noqa: E402

try:
    from langchain_core.language_models.chat_models import BaseChatModel
    from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage
    from langchain_core.outputs import ChatGeneration, ChatResult
    from langchain_core.prompt_values import PromptValue
    from langchain_core.runnables import RunnableLambda
except ImportError:  # the repository's own interpreter: only the CLI entry below works
    BaseChatModel = object

JSON_ONLY = ("Reply with exactly one JSON object and nothing else — no prose, no code fence. Copy every "
             "quotation character exactly as the text writes it: German quotation marks open with „ and close "
             "with “, never with a straight quote. It must validate against this JSON schema:\n")
# Haiku, copying „getaktet“, closes it with a straight quote — `„getaktet"` — which ends
# the JSON string it stands in (measured 2026-09-30: 3 of 5 calls unreadable, and
# `claude -p --json-schema` failed the same way five times). A straight quote right
# after a „-opened span with no closing mark is put back to the “ the source writes.
GERMAN_CLOSE = re.compile(r'„([^„“"\n]{0,400})"')


def flatten(messages: list) -> tuple[str, str]:
    """(system, text): the system messages joined, the rest as the stdin text."""
    system = "\n\n".join(m.content for m in messages if isinstance(m, SystemMessage))
    rest = [m for m in messages if not isinstance(m, SystemMessage)]
    if len(rest) == 1:
        return system, str(rest[0].content)
    return system, "\n\n".join(f"[{m.type}]\n{m.content}" for m in rest)


def as_messages(value: Any) -> list:
    if isinstance(value, PromptValue):
        return value.to_messages()
    if isinstance(value, str):
        return [HumanMessage(content=value)]
    if isinstance(value, list):
        return value
    raise TypeError(f"cannot read a prompt from {type(value).__name__}")


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


class ClaudeChat(BaseChatModel):
    """`claude -p` as a LangChain chat model; `model` is a CLI alias (`haiku`, `sonnet`)."""

    model: str = "haiku"
    thinking: int | None = 0
    timeout: float = 300.0
    binary: str | None = None
    calls: list = []

    @property
    def _llm_type(self) -> str:
        return "claude-cli"

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

    def _generate(self, messages, stop=None, run_manager=None, **kwargs) -> ChatResult:
        system, text = flatten(messages)
        return ChatResult(generations=[ChatGeneration(message=AIMessage(content=self._call(system, text)))])

    def with_structured_output(self, schema, *, include_raw: bool = False, **kwargs):
        """The one call HyperExtract makes: a prompt in, a validated `schema` object out."""
        if include_raw:
            raise NotImplementedError("include_raw is not supported")
        spec = json.dumps(schema.model_json_schema() if hasattr(schema, "model_json_schema") else schema,
                          ensure_ascii=False)

        def structured(value):
            system, text = flatten(as_messages(value))
            asked = f"{text}\n\n{JSON_ONLY}{spec}"
            error = None
            for attempt in range(2):
                reply = self._call(system, asked if not error else
                                   f"{asked}\n\nYour previous reply failed: {error}. Reply again, JSON only.")
                try:
                    obj, repaired = parse_json(reply)
                    if repaired:
                        self.calls[-1]["repaired_quotes"] = repaired
                    return schema.model_validate(obj) if hasattr(schema, "model_validate") else obj
                except (ValueError, json.JSONDecodeError, Exception) as exc:  # pydantic's ValidationError included
                    error = str(exc)[:300]
                    self.calls[-1]["ok"] = False
                    self.calls[-1]["kind"] = "invalid"
            raise ValueError(f"no reply validated against the schema: {error}")

        return RunnableLambda(structured)


# --- offline self-test: HyperExtract's own factory with a fake `claude` --------------------

FAKE = r'''#!/usr/bin/env python3
import json, os, sys
text = sys.stdin.read()
reply = os.environ.get("FAKE_CLAUDE_REPLY", "")
if "failed:" in text and os.environ.get("FAKE_CLAUDE_SECOND"):
    reply = os.environ["FAKE_CLAUDE_SECOND"]
print(json.dumps({"type": "result", "is_error": False, "result": reply,
                  "usage": {"input_tokens": 100, "output_tokens": 20}, "total_cost_usd": 0.001}))
'''


def native_selftest() -> int:
    """Inside HyperExtract's interpreter: the real factory, feed and schema, a fake `claude`."""
    import os
    import stat
    import tempfile
    from langchain_core.embeddings import FakeEmbeddings
    import reading_extract
    cases = []
    folder = ROOT / "Plan" / "hyperextract" / "fixtures"
    text = (folder / "reading.txt").read_text(encoding="utf-8")
    template = ROOT / "Plan" / "hyperextract" / "TermReadings.yaml"
    good = (folder / "TermReadings.json").read_text(encoding="utf-8")
    with tempfile.TemporaryDirectory() as tmp:
        fake = Path(tmp) / "claude"
        fake.write_text(FAKE, encoding="utf-8")
        fake.chmod(fake.stat().st_mode | stat.S_IEXEC)
        os.environ["FAKE_CLAUDE_REPLY"] = good
        llm = ClaudeChat(model="haiku", binary=str(fake), calls=[])
        data = reading_extract.native_extract(template, text, "synthetic", llm, FakeEmbeddings(size=8))
        cases.append(("a validated reply becomes the template's items",
                      data == json.loads(good) and llm.calls and all(c["ok"] for c in llm.calls)))
        cases.append(("every call recorded with its cost", all("cost_usd" in c for c in llm.calls)))
        os.environ["FAKE_CLAUDE_REPLY"] = "Gern, hier ist die Antwort: keine."
        os.environ["FAKE_CLAUDE_SECOND"] = good
        llm = ClaudeChat(model="haiku", binary=str(fake), calls=[])
        data = reading_extract.native_extract(template, text, "synthetic", llm, FakeEmbeddings(size=8))
        cases.append(("prose first, JSON when asked again: one retry, recorded",
                      data == json.loads(good) and [c["ok"] for c in llm.calls][:2] == [False, True]))
        retry_usage = claude_cli.totals(llm.calls)
        cases.append(("invalid reply and retry both count as paid calls",
                      retry_usage["cost_usd"] == round(sum(c["cost_usd"] for c in llm.calls), 4)
                      and retry_usage["input_tokens"] == 100 * len(llm.calls)
                      and retry_usage["failed_calls"] >= 1))
        # A German span closed with a straight quote is put back to the mark the source writes.
        obj, n = parse_json('{"quote": "sondern \u201egetaktet" ist", "stance": "asserts"}')
        cases.append(("a German span closed with a straight quote is repaired, and counted",
                      obj["quote"] == "sondern \u201egetaktet\u201c ist" and n == 1))
        obj, n = parse_json('{"quote": "plain \\"words\\" here"}')
        cases.append(("valid JSON is left alone", obj["quote"] == 'plain "words" here' and n == 0))
        os.environ.pop("FAKE_CLAUDE_SECOND", None)
        llm = ClaudeChat(model="haiku", binary=str(fake), calls=[])
        data = reading_extract.native_extract(template, text, "synthetic", llm, FakeEmbeddings(size=8))
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
    """One document through one list template with Claude, staged, every call recorded. `gate` sends the model
    only the paragraphs that hold a cue of the contract (`hegraph.gate`) and records the share in `usage.json`.
    `approval` is what the record says licensed the run: the default is the author's instruction of 2026-09-30 to
    put HyperExtract into the pipeline; a run under a later instruction names it (the backfill does)."""
    import tempfile
    from langchain_core.embeddings import FakeEmbeddings
    import reading_extract
    from subject import document
    if "type: list" not in template.read_text(encoding="utf-8"):
        raise SystemExit(f"{template.name}: only list templates run here (a graph merge uses the embeddings)")
    doc = document(slug)
    text = None
    if gate:
        import hegraph
        text = hegraph.gate(doc.body, template.stem)
    llm = ClaudeChat(model=model, binary=binary, calls=[])
    target = ROOT / "Plan" / "runs" / doc.slug / "hyperextract" / name
    failed = None
    try:
        envelope = reading_extract.extract(template, doc, llm, FakeEmbeddings(size=8), f"claude-cli/{model}", text)
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
    if argv[:1] not in (["selftest"], ["run"]):
        print(__doc__)
        return 2
    if BaseChatModel is object:  # not HyperExtract's interpreter: find it and run there
        import subprocess
        from templates import he_python
        py = he_python()
        if py is None:
            print("not reached: scripts/install.sh hyperextract", file=sys.stderr)
            return 2
        return subprocess.run([str(py), __file__, *argv]).returncode
    if argv[0] == "run":
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
    return native_selftest()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
