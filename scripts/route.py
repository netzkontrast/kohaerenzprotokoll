#!/usr/bin/env python3
"""One door for every model call a tool makes — priced, consented and recorded before it is sent.

The cost rule, in the order work is tried:

  1. decidable            -> code. It never reaches this module.
  2. a typed judgement    -> Jev (`jev()`): yes/no, one of a set, a score. Per call.
  3. generation           -> an OpenRouter model whose listed price is 0, sent with
                             provider.data_collection = "deny". Nothing else, ever.
  4. synthesis            -> the Claude agent that called the tool. Not routed.

Three guards are code, not prose (P1), and each says what it could not check (P23):

- **Free only.** A model is used only if its listed prompt and completion prices are
  both 0 — read from OpenRouter's catalogue, never inferred from a `:free` name —
  and a response that reports `usage.cost > 0` stops the run.
- **Consent.** `Plan/runs/route/consent.json` (decision 007) names the documents
  that may be sent. A call declaring any other document is refused, and so is any
  request containing twelve consecutive words of a landed document outside the
  consent. Blind to: paraphrase, translation, and runs shorter than twelve words.
- **Recorded.** Every answered call is kept under `Plan/runs/route/calls/`, so a
  run replays offline, free and without a key (P5), and every call — answered,
  cached, refused or unreached — is a line in `Plan/runs/route/ledger.jsonl`.

A call that never returned is **unreached**, never a bad answer (P15), and an empty
or truncated answer is a defect that moves on to the next model (P19).

    python3 scripts/route.py models             # probe free models under the data policy
    python3 scripts/route.py serve [--port N]   # OpenAI-compatible proxy for third-party tools
    python3 scripts/route.py ledger             # what was called, by whom, at what cost
    python3 scripts/route.py guard <slug>       # would this document's text be refused?
    python3 scripts/route.py selftest           # offline: no key, no network
    echo PROMPT | python3 scripts/route.py complete --purpose P --doc SLUG

**The proxy.** A tool that takes an OpenAI base URL is pointed at
`http://127.0.0.1:<port>/v1` and names itself in the API key it sends —
`route:<purpose>:<doc>` — so it never holds a real key. Whatever model it asks for,
it gets a free one; `/v1/embeddings` is answered locally by a multilingual
sentence-transformers model when the proxy runs under an interpreter that has one
(`.venv-grawiki/bin/python`), because no free embedding model on OpenRouter
accepts the data policy. `serve --replay` answers only from the recording.

Jev needs `typesafe_sdk`: run the caller with `.venv-typesafe/bin/python`.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
import struct
import sys
import threading
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import subject  # noqa: E402

OUT = ROOT / "Plan" / "runs" / "route"
API = "https://openrouter.ai/api/v1"
EMBED_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
SHINGLE = 12          # words: a run this long of another document's text is that document
TIMEOUT = 180         # seconds per model attempt; free endpoints answer in 2-120 s (2026-09-23/24)
COOL = 60             # seconds a rate-limited model is skipped while others remain
PROBE = "Antworte nur mit dem Wort: Kohärenz"
REPLAY = False
LOCK = threading.Lock()


class Refused(Exception):
    """A call this module will not make: outside the consent, or not free."""


def paths() -> dict[str, Path]:
    return {"consent": OUT / "consent.json", "calls": OUT / "calls",
            "ledger": OUT / "ledger.jsonl", "catalogue": OUT / "models.json"}


def now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def rel(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def digest(obj) -> str:
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:20]


# ── consent ───────────────────────────────────────────────────────────────────

def consent() -> dict:
    path = paths()["consent"]
    if not path.exists():
        raise Refused(f"no {rel(path)}: nothing may be sent until the author decides")
    return json.loads(path.read_text(encoding="utf-8"))


def check_doc(doc: str | None) -> str | None:
    if doc in (None, "", "none", "-"):
        return None
    allowed = consent()["documents"]
    if doc not in allowed:
        raise Refused(f"{doc!r} is outside the consent ({rel(paths()['consent'])}); "
                      f"decision 007 allows {', '.join(allowed)}")
    return doc


WORD = re.compile(r"\w+")


def shingles(text: str) -> set[int]:
    w = WORD.findall(text.lower())
    return {hash(tuple(w[i:i + SHINGLE])) for i in range(len(w) - SHINGLE + 1)}


class Guard:
    """Every twelve-word run of a landed document the consent does not cover.

    A run the consented documents also contain is theirs to send, so boilerplate
    shared with them never refuses. Hashes are per process, never stored."""

    def __init__(self) -> None:
        allowed = set(consent()["documents"])
        mine: set[int] = set()
        self.foreign: set[int] = set()
        self.documents = self.blind = 0
        for d in subject.documents():
            s = shingles(d.body)
            if not s:
                self.blind += 1          # shorter than one run: nothing to recognise it by
            if d.slug in allowed:
                mine |= s
            else:
                self.foreign |= s
                self.documents += 1
        self.foreign -= mine

    def breach(self, text: str) -> list[str]:
        hits = shingles(text) & self.foreign
        if not hits:
            return []
        # Rare path: name the documents, so a refusal says whose text it was.
        return sorted({d.slug for d in subject.documents() if shingles(d.body) & hits})


_GUARD: Guard | None = None


def guard() -> Guard:
    global _GUARD
    with LOCK:
        if _GUARD is None:
            _GUARD = Guard()
    return _GUARD


def screen(text: str, purpose: str, doc: str | None) -> None:
    slugs = guard().breach(text)
    if slugs:
        ledger(kind="refused", purpose=purpose, doc=doc, outcome="refused",
               why=f"text of {len(slugs)} document(s) outside the consent: {', '.join(slugs[:5])}")
        raise Refused(f"the request contains text of {', '.join(slugs[:5])}, "
                      "which the consent does not cover")


# ── the record ────────────────────────────────────────────────────────────────

def ledger(**row) -> None:
    row = {"at": now(), **row}
    path = paths()["ledger"]
    with LOCK:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def recall(kind: str, key: str) -> dict | None:
    path = paths()["calls"] / kind / f"{key}.json"
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None


def store(kind: str, key: str, rec: dict) -> None:
    path = paths()["calls"] / kind / f"{key}.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")


# ── OpenRouter ────────────────────────────────────────────────────────────────

def is_free(model: dict) -> bool:
    """Listed price 0 for prompt and completion, and for every other listed price."""
    pricing = model.get("pricing") or {}
    if "prompt" not in pricing or "completion" not in pricing:
        return False
    try:
        return all(float(v) == 0 for v in pricing.values() if v not in (None, ""))
    except (TypeError, ValueError):
        return False


def _post(url: str, body: dict | None, timeout: int = TIMEOUT) -> tuple[int, dict]:
    """The one network call. Returns (status, json); selftest replaces it."""
    key = os.environ.get("OPENROUTER_API_KEY")
    if not key:
        return 0, {"error": {"message": "OPENROUTER_API_KEY is not set"}}
    req = urllib.request.Request(url, data=None if body is None else json.dumps(body).encode(),
                                 headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json",
                                          "X-Title": "kohaerenzprotokoll route.py"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, json.load(r)
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", "replace")
        try:
            return e.code, json.loads(raw)
        except ValueError:
            return e.code, {"error": {"message": raw[:300]}}
    except Exception as e:  # timeout, reset, DNS: not an answer (P15)
        return 0, {"error": {"message": f"{type(e).__name__}: {e}"[:300]}}


def _classify(status: int, body: dict) -> str:
    msg = json.dumps(body.get("error", body), ensure_ascii=False)
    if status == 404 and "data policy" in msg:
        return "data-policy"
    if status == 429:
        return "rate-limited"
    if status in (401, 403):
        return "forbidden"
    return "error"


def catalogue() -> dict:
    path = paths()["catalogue"]
    if not path.exists():
        raise Refused(f"no {rel(path)} — run: python3 scripts/route.py models")
    return json.loads(path.read_text(encoding="utf-8"))


_COOLING: dict[str, float] = {}


def rotation(prefer: str | None = None) -> list[str]:
    """Free chat models that accepted the data policy: answered first, rate-limited after."""
    chat = catalogue()["chat"]
    ok = sorted((m for m, v in chat.items() if v["status"] == "ok"), key=lambda m: chat[m].get("seconds", 99))
    later = sorted(m for m, v in chat.items() if v["status"] == "rate-limited")
    order = ok + later
    if prefer in order:
        order.remove(prefer)
        order.insert(0, prefer)
    t = time.time()
    warm = [m for m in order if _COOLING.get(m, 0) <= t]
    return warm + [m for m in order if m not in warm]


def lang(text: str) -> str | None:
    """'de', 'en' or None — enough to catch an English answer to a German task (P19)."""
    w = [x.lower() for x in WORD.findall(text)]
    de = sum(x in {"der", "die", "das", "und", "ist", "nicht", "ein", "eine", "mit", "von", "den", "im",
                   "auf", "für", "sich", "des", "auch", "als", "wird", "zu"} for x in w)
    en = sum(x in {"the", "and", "is", "not", "a", "of", "to", "in", "for", "with", "on", "as", "by",
                   "be", "this", "that", "are", "it"} for x in w)
    if de + en < 3:
        return None
    return "de" if de > en else "en"


def chat(request: dict, *, purpose: str, doc: str | None = None, prefer: str | None = None,
         expect: str | None = None, attempt: int = 0) -> dict:
    """One chat completion from a free model, or {"unreached": why}.

    `request` is an OpenAI chat body without `model`. Raises Refused only for a
    consent breach or a charged call; a model's failure is never raised."""
    doc = check_doc(doc)
    request = {k: v for k, v in request.items()
               if k not in ("model", "models", "stream", "stream_options", "provider", "route", "user")}
    screen(json.dumps(request.get("messages", []), ensure_ascii=False), purpose, doc)
    # attempt > 0 is a deliberate repeat (P18): a fresh call, never the first one replayed
    key = digest({**request, "attempt": attempt} if attempt else request)
    rec = recall("chat", key)
    if rec is not None:
        ledger(kind="chat", purpose=purpose, doc=doc, key=key, cached=True, outcome="ok",
               model=rec["model"], cost=0)
        return rec
    if REPLAY:
        ledger(kind="chat", purpose=purpose, doc=doc, key=key, cached=False, outcome="unreached",
               why="not in the recording")
        return {"unreached": "not in the recording"}
    models = rotation(prefer)
    tried: list[dict] = []
    for model in models + models:            # each model twice, in order, before giving up
        if len(tried) >= 2 * len(models):
            break
        if _COOLING.get(model, 0) > time.time() and any(_COOLING.get(m, 0) <= time.time() for m in models):
            continue
        body = {**request, "model": model, "provider": {"data_collection": "deny"}, "usage": {"include": True}}
        t = time.time()
        status, resp = _post(f"{API}/chat/completions", body)
        took = round(time.time() - t, 1)
        if status != 200 or "choices" not in resp:
            why = _classify(status, resp) if status else "unreached"
            if why == "rate-limited":
                _COOLING[model] = time.time() + COOL
            tried.append({"model": model, "status": status, "why": why, "seconds": took})
            time.sleep(1 if why == "rate-limited" else 0)
            continue
        usage = resp.get("usage") or {}
        cost = usage.get("cost")
        if cost:
            ledger(kind="chat", purpose=purpose, doc=doc, key=key, cached=False, outcome="charged",
                   model=model, cost=cost)
            raise Refused(f"{model} charged {cost} although listed free — stopping (decision 007)")
        choice = resp["choices"][0]
        msg = choice.get("message") or {}
        content = msg.get("content") or ""
        defect = None
        if not content.strip() and not msg.get("tool_calls"):
            defect = "empty"
        elif choice.get("finish_reason") == "length":
            defect = "truncated"
        elif expect and content.strip() and lang(content) not in (None, expect):
            defect = f"language {lang(content)}"
        if defect:
            tried.append({"model": model, "status": status, "why": defect, "seconds": took})
            continue
        rec = {"model": resp.get("model", model), "provider": resp.get("provider"), "seconds": took,
               "content": content, "response": resp, "tried": tried}
        store("chat", key, rec)
        ledger(kind="chat", purpose=purpose, doc=doc, key=key, cached=False, outcome="ok",
               model=rec["model"], provider=rec["provider"], seconds=took,
               prompt_tokens=usage.get("prompt_tokens"), completion_tokens=usage.get("completion_tokens"),
               cost=cost if cost is not None else None, attempts=len(tried) + 1)
        return rec
    why = "; ".join(f"{t['model']}: {t['why']}" for t in tried[-4:]) or "no model in the rotation"
    ledger(kind="chat", purpose=purpose, doc=doc, key=key, cached=False, outcome="unreached",
           why=why[:400], attempts=len(tried))
    return {"unreached": why, "tried": tried}


def complete(prompt: str, *, purpose: str, doc: str | None = None, max_tokens: int = 4000,
             json_mode: bool = False, expect: str | None = None, attempt: int = 0) -> dict:
    request = {"messages": [{"role": "user", "content": prompt}], "max_tokens": max_tokens, "temperature": 0}
    if json_mode:
        request["response_format"] = {"type": "json_object"}
    return chat(request, purpose=purpose, doc=doc, expect=expect, attempt=attempt)


# ── Jev ───────────────────────────────────────────────────────────────────────

def _questions(spec: dict):
    """JSON question specs -> typesafe_sdk questions. Validates before any call."""
    from typesafe_sdk import Choice, Noul, NoulCriteria, Score
    out = {}
    for k, q in spec.items():
        kind, instr, crit = q.get("type"), q.get("instructions"), q.get("criteria")
        if kind == "noul":
            out[k] = Noul(instructions=instr, criteria=NoulCriteria(true=crit["true"], false=crit["false"]))
        elif kind == "choice":
            out[k] = Choice(instructions=instr, criteria=dict(crit))
        elif kind == "score":
            if not 2 <= len(crit) <= 10:
                raise ValueError(f"{k}: a Score takes 2-10 levels; eleven is a server error (typesafe skill)")
            out[k] = Score(instructions=instr, criteria=list(crit))
        else:
            raise ValueError(f"{k}: type must be noul, choice or score, not {kind!r}")
    return out


def jev(state: dict, questions: dict, *, purpose: str, doc: str | None = None) -> dict:
    """Typed answers from Jev, or {"unreached": why}. Questions are JSON specs:
    {"type": "noul", "instructions": ..., "criteria": {"true": ..., "false": ...}},
    {"type": "choice", ..., "criteria": {label: description}},
    {"type": "score", ..., "criteria": [level, ...]} (2-10 levels, ordered)."""
    doc = check_doc(doc)
    screen(json.dumps([state, questions], ensure_ascii=False), purpose, doc)
    key = digest({"state": state, "questions": questions})
    rec = recall("jev", key)
    if rec is not None:
        ledger(kind="jev", purpose=purpose, doc=doc, key=key, cached=True, outcome="ok", model=rec["model"])
        return rec
    if REPLAY:
        return {"unreached": "not in the recording"}
    try:
        from typesafe_sdk import RetryPolicy, TypeSafeClient
        qs = _questions(questions)
    except ImportError:
        return {"unreached": "typesafe_sdk is not importable — run with .venv-typesafe/bin/python"}
    t = time.time()
    try:
        with TypeSafeClient(timeout=120, retry=RetryPolicy(max_retries=5, backoff_initial=1.0,
                                                           backoff_max=20.0)) as c:
            r = c.system_one(state=state, questions=qs)
    except Exception as e:
        why = f"{type(e).__name__}: {e}"[:300]
        ledger(kind="jev", purpose=purpose, doc=doc, key=key, cached=False, outcome="unreached", why=why)
        return {"unreached": why}
    answers = {}
    for k in questions:
        a = r.answers[k]
        answers[k] = {f: (dict(getattr(a, f)) if f == "probabilities" else getattr(a, f))
                      for f in ("noul", "choice", "score", "confidence", "probabilities")
                      if getattr(a, f, None) is not None}
    rec = {"model": r.model, "seconds": round(time.time() - t, 2),
           "input_tokens": r.usage.input_tokens, "answers": answers}
    store("jev", key, rec)
    ledger(kind="jev", purpose=purpose, doc=doc, key=key, cached=False, outcome="ok", model=r.model,
           seconds=rec["seconds"], prompt_tokens=rec["input_tokens"], cost=None)
    return rec


# ── local embeddings ──────────────────────────────────────────────────────────

_EMBEDDER = None
EMBED_LOCK = threading.Lock()


def embedder():
    global _EMBEDDER
    with EMBED_LOCK:        # ~60 s on first load: never under the ledger's lock
        if _EMBEDDER is None:
            from sentence_transformers import SentenceTransformer  # .venv-grawiki has it
            _EMBEDDER = SentenceTransformer(EMBED_MODEL, device="cpu")
    return _EMBEDDER


def embed(texts: list[str], *, purpose: str, doc: str | None = None) -> list[list[float]]:
    doc = check_doc(doc)
    screen("\n".join(texts), purpose, doc)
    vectors = embedder().encode(texts, normalize_embeddings=True).tolist()
    ledger(kind="embed", purpose=purpose, doc=doc, cached=False, outcome="ok",
           model=f"local/{EMBED_MODEL}", inputs=len(texts), cost=0)
    return vectors


# ── the proxy ─────────────────────────────────────────────────────────────────

class Proxy(BaseHTTPRequestHandler):
    server_version = "route/1"

    def log_message(self, fmt, *args):  # the ledger is the log
        pass

    def _send(self, code: int, obj: dict) -> None:
        data = json.dumps(obj, ensure_ascii=False).encode()
        self.send_response(code)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def _error(self, code: int, message: str, kind: str) -> None:
        self._send(code, {"error": {"message": message, "type": kind, "code": code}})

    def _who(self) -> tuple[str, str | None, int]:
        token = (self.headers.get("Authorization") or "").removeprefix("Bearer ").strip()
        if not token.startswith("route:"):
            raise PermissionError("name the caller in the API key: route:<purpose>:<document slug or ->[:<attempt>]")
        parts = token.split(":")
        purpose = parts[1] if len(parts) > 1 and parts[1] else "unnamed"
        attempt = int(parts[3]) if len(parts) > 3 and parts[3].isdigit() else 0
        return purpose, check_doc(parts[2] if len(parts) > 2 else None), attempt

    def do_GET(self):  # noqa: N802
        if self.path.rstrip("/").endswith("/health"):  # cgr's litellm_proxy provider asks this first
            return self._send(200, {"status": "ok"})
        if self.path.rstrip("/").endswith("/models"):
            data = [{"id": m, "object": "model", "owned_by": "openrouter-free"} for m in rotation()]
            data.append({"id": f"local/{EMBED_MODEL}", "object": "model", "owned_by": "local"})
            return self._send(200, {"object": "list", "data": data})
        return self._error(404, f"no route for GET {self.path}", "not_found")

    def do_POST(self):  # noqa: N802
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length") or 0)) or b"{}")
        except ValueError:
            return self._error(400, "the body is not JSON", "invalid_request")
        try:
            purpose, doc, attempt = self._who()
        except PermissionError as e:
            return self._error(401, str(e), "unnamed_caller")
        except Refused as e:
            return self._error(403, str(e), "outside_consent")
        path = self.path.split("?")[0].rstrip("/")
        try:
            if path.endswith("/chat/completions"):
                return self._chat(body, purpose, doc, attempt)
            if path.endswith("/embeddings"):
                return self._embed(body, purpose, doc)
        except Refused as e:
            return self._error(403, str(e), "refused")
        return self._error(404, f"no route for POST {self.path}", "not_found")

    def _chat(self, body: dict, purpose: str, doc: str | None, attempt: int = 0) -> None:
        stream = bool(body.get("stream"))
        usage_chunk = bool((body.get("stream_options") or {}).get("include_usage"))
        rec = chat(body, purpose=purpose, doc=doc, prefer=body.get("model"), attempt=attempt)
        if "unreached" in rec:
            return self._error(502, f"no free model answered: {rec['unreached']}", "route_unreached")
        resp = dict(rec["response"])
        resp["model"] = rec["model"]
        if not stream:
            return self._send(200, resp)
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()
        choice = resp["choices"][0]
        msg = choice.get("message") or {}
        delta = {"role": "assistant"}
        if msg.get("content") is not None:
            delta["content"] = msg["content"]
        if msg.get("tool_calls"):
            delta["tool_calls"] = [{"index": i, **tc} for i, tc in enumerate(msg["tool_calls"])]
        base = {"id": resp.get("id", "route"), "object": "chat.completion.chunk",
                "created": resp.get("created", int(time.time())), "model": resp["model"]}
        chunks = [{**base, "choices": [{"index": 0, "delta": delta, "finish_reason": None}]},
                  {**base, "choices": [{"index": 0, "delta": {}, "finish_reason": choice.get("finish_reason") or "stop"}]}]
        if usage_chunk:
            chunks.append({**base, "choices": [], "usage": resp.get("usage")})
        for c in chunks:
            self.wfile.write(f"data: {json.dumps(c, ensure_ascii=False)}\n\n".encode())
        self.wfile.write(b"data: [DONE]\n\n")
        self.wfile.flush()

    def _embed(self, body: dict, purpose: str, doc: str | None) -> None:
        texts = body.get("input")
        texts = [texts] if isinstance(texts, str) else list(texts or [])
        if texts and not isinstance(texts[0], str):
            return self._error(400, "token-id input is not supported; send strings", "invalid_request")
        try:
            vectors = embed(texts, purpose=purpose, doc=doc)
        except ImportError:
            return self._error(501, "no local embedder: run serve under .venv-grawiki/bin/python", "no_embedder")
        b64 = body.get("encoding_format") == "base64"
        data = [{"object": "embedding", "index": i,
                 "embedding": base64.b64encode(struct.pack(f"<{len(v)}f", *v)).decode() if b64 else v}
                for i, v in enumerate(vectors)]
        self._send(200, {"object": "list", "data": data, "model": f"local/{EMBED_MODEL}",
                         "usage": {"prompt_tokens": 0, "total_tokens": 0}})


def serve(port: int) -> ThreadingHTTPServer:
    return ThreadingHTTPServer(("127.0.0.1", port), Proxy)


# ── commands ──────────────────────────────────────────────────────────────────

def cmd_models() -> int:
    status, listing = _post(f"{API}/models", None, timeout=60)
    if status != 200:
        print(f"could not list models: {status} {listing}")
        return 1
    free = [m for m in listing["data"] if is_free(m)]
    status, elisting = _post(f"{API}/embeddings/models", None, timeout=60)
    efree = [m for m in elisting.get("data", []) if is_free(m)] if status == 200 else []

    def probe_chat(m: dict) -> tuple[str, dict]:
        t = time.time()
        s, r = _post(f"{API}/chat/completions", {
            "model": m["id"], "max_tokens": 400, "temperature": 0, "usage": {"include": True},
            "provider": {"data_collection": "deny"}, "messages": [{"role": "user", "content": PROBE}]}, timeout=120)
        row = {"context": m.get("context_length"), "seconds": round(time.time() - t, 1)}
        if s == 200 and "choices" in r:
            content = (r["choices"][0].get("message") or {}).get("content") or ""
            row["status"] = "ok" if content.strip() else "empty"
            row["provider"] = r.get("provider")
        else:
            row["status"] = _classify(s, r) if s else "unreached"
        return m["id"], row

    def probe_embed(m: dict) -> tuple[str, dict]:
        s, r = _post(f"{API}/embeddings", {"model": m["id"], "input": ["Kohärenz"],
                                          "provider": {"data_collection": "deny"}}, timeout=60)
        return m["id"], {"status": "ok" if s == 200 and r.get("data") else (_classify(s, r) if s else "unreached")}

    with ThreadPoolExecutor(12) as pool:
        chat_rows = dict(pool.map(probe_chat, free))
        embed_rows = dict(pool.map(probe_embed, efree))
    cat = {"probed": now(), "policy": {"data_collection": "deny"}, "listed": len(listing["data"]),
           "free": len(free), "chat": chat_rows, "embeddings": embed_rows,
           "local_embeddings": EMBED_MODEL}
    path = paths()["catalogue"]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(cat, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(listing['data'])} models listed, {len(free)} free by listed price; "
          f"probed under data_collection=deny -> {rel(path)}\n")
    for m, v in sorted(chat_rows.items(), key=lambda kv: (kv[1]["status"] != "ok", kv[0])):
        print(f"  chat  {v['status']:<13} {v['seconds']:>6}s  {m}")
    for m, v in sorted(embed_rows.items()):
        print(f"  embed {v['status']:<13}          {m}")
    usable = sum(v["status"] in ("ok", "rate-limited") for v in chat_rows.values())
    print(f"\n{usable} chat models in the rotation; embeddings: "
          f"{sum(v['status'] == 'ok' for v in embed_rows.values())} free remote, local {EMBED_MODEL}")
    return 0 if usable else 1


def cmd_ledger() -> int:
    path = paths()["ledger"]
    rows = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()] if path.exists() else []
    if not rows:
        print("the ledger is empty")
        return 0
    by = defaultdict(Counter)
    tokens = defaultdict(Counter)
    priced = unpriced = 0
    cost = 0.0
    for r in rows:
        k = (r.get("purpose", "?"), r.get("kind", "?"))
        by[k][("cached" if r.get("cached") else r.get("outcome", "?"))] += 1
        tokens[k]["in"] += r.get("prompt_tokens") or 0
        tokens[k]["out"] += r.get("completion_tokens") or 0
        if r.get("outcome") in ("ok", "charged") and not r.get("cached"):
            if r.get("cost") is None:
                unpriced += 1
            else:
                priced += 1
                cost += float(r["cost"])
    print(f"{len(rows)} ledger rows, {rows[0]['at']} .. {rows[-1]['at']}\n")
    print(f"  {'purpose':<28} {'kind':<7} {'ok':>5} {'cached':>6} {'unreach':>7} {'refused':>7} "
          f"{'charged':>7} {'in tok':>9} {'out tok':>8}")
    for (p, k), c in sorted(by.items()):
        t = tokens[(p, k)]
        print(f"  {p:<28} {k:<7} {c['ok']:>5} {c['cached']:>6} {c['unreached']:>7} {c['refused']:>7} "
              f"{c['charged']:>7} {t['in']:>9,} {t['out']:>8,}")
    models = Counter(r.get("model") for r in rows if r.get("outcome") == "ok" and not r.get("cached"))
    print("\nanswered by: " + ", ".join(f"{m} {n}" for m, n in models.most_common()))
    print(f"\ncost: ${cost:.6f} over {priced} priced calls; {unpriced} answered calls carry no price "
          f"(Jev reports input tokens, not cost) — never read 'unpriced' as free")
    return 1 if any(r.get("outcome") == "charged" for r in rows) else 0


def cmd_guard(slug: str) -> int:
    g = guard()
    print(f"guard: {len(g.foreign):,} twelve-word runs from {g.documents} documents outside the consent; "
          f"{g.blind} document(s) too short to recognise; blind to paraphrase and translation")
    hits = g.breach(subject.document(slug).body)
    print(f"{slug}: {'REFUSED, text of ' + ', '.join(hits[:5]) if hits else 'may be sent'}")
    return 0


def cmd_selftest() -> int:
    """Offline, no key, no network: every guard is shown to hold and to fail."""
    import tempfile
    global OUT, REPLAY, _post
    real_consent = json.loads((OUT / "consent.json").read_text(encoding="utf-8"))
    allowed = real_consent["documents"]
    outsider = next(d.slug for d in subject.documents() if d.slug not in allowed and len(d.body) > 2000)
    saved = (OUT, _post, REPLAY)
    bad = 0

    def check(name: str, ok: bool) -> None:
        nonlocal bad
        bad += not ok
        print(f"  {'ok ' if ok else 'BAD'} {name}")

    script: list = []
    calls: list[str] = []

    def fake(url, body, timeout=TIMEOUT):
        calls.append(body["model"] if body else url)
        return script.pop(0) if script else (0, {"error": {"message": "fixture exhausted"}})

    def answer(text, finish="stop", cost=0):
        return 200, {"model": "m", "provider": "fixture", "choices": [
            {"message": {"role": "assistant", "content": text}, "finish_reason": finish}],
            "usage": {"prompt_tokens": 5, "completion_tokens": 2, "cost": cost}}

    with tempfile.TemporaryDirectory() as tmp:
        OUT = Path(tmp)
        (OUT / "consent.json").write_text(json.dumps(real_consent), encoding="utf-8")
        (OUT / "models.json").write_text(json.dumps({"chat": {
            "a:free": {"status": "ok", "seconds": 1}, "b:free": {"status": "ok", "seconds": 2},
            "c:free": {"status": "rate-limited"}, "d:free": {"status": "data-policy"}}}), encoding="utf-8")
        _post = fake
        try:
            print("price")
            check("listed 0/0 is free", is_free({"pricing": {"prompt": "0", "completion": "0"}}))
            check("any non-zero price is not", not is_free({"pricing": {"prompt": "0", "completion": "0",
                                                                         "request": "0.001"}}))
            check("no pricing is not free", not is_free({"id": "x:free"}))
            print("consent")
            try:
                check_doc(outsider)
                check("a document outside the consent is refused", False)
            except Refused:
                check("a document outside the consent is refused", True)
            g = guard()
            foreign_text = subject.document(outsider).body[:3000]
            check(f"text of {outsider} is recognised", outsider in g.breach(foreign_text))
            check("text of a consented document is not", not g.breach(subject.document(allowed[0]).body[:3000]))
            check("short fragments pass (blind below twelve words, P23)", not g.breach("AEGIS und der Riss"))
            try:
                complete(foreign_text, purpose="selftest", doc=allowed[0])
                check("a request carrying foreign text is refused before sending", False)
            except Refused:
                check("a request carrying foreign text is refused before sending", not calls)
            print("rotation and defects")
            check("data-policy models are never in the rotation", "d:free" not in rotation())
            script[:] = [(429, {"error": {"message": "rate"}}), answer("Kohärenz")]
            r = complete("eins", purpose="selftest", doc=allowed[0])
            check("a rate-limited model falls through to the next", r.get("content") == "Kohärenz"
                  and calls[-2:] == ["a:free", "b:free"])
            n = len(calls)
            r2 = complete("eins", purpose="selftest", doc=allowed[0])
            check("the same request is answered from the recording", r2.get("content") == "Kohärenz" and len(calls) == n)
            script[:] = [answer("Kohärenz, zweiter Versuch")]
            r3 = complete("eins", purpose="selftest", doc=allowed[0], attempt=1)
            check("a repeat (attempt 1) is a fresh call, never the recording (P18)",
                  len(calls) == n + 1 and r3.get("content") == "Kohärenz, zweiter Versuch")
            script[:] = [answer("")] * 6
            r = complete("zwei", purpose="selftest")
            check("an empty answer is a defect, never returned (P19)", "unreached" in r)
            check("...and an unreached call is not recorded (P15)", recall("chat", digest(
                {"messages": [{"role": "user", "content": "zwei"}], "max_tokens": 4000, "temperature": 0})) is None)
            script[:] = [answer("halb", finish="length"), answer("ganz")]
            check("a truncated answer moves on", complete("drei", purpose="selftest").get("content") == "ganz")
            script[:] = [answer("The answer is that this is in English and not German."), answer("Die Antwort ist das.")]
            check("a wrong-language answer moves on", complete("vier", purpose="selftest", expect="de")
                  .get("content") == "Die Antwort ist das.")
            script[:] = [answer("teuer", cost=0.002)]
            try:
                complete("fünf", purpose="selftest")
                check("a charged call stops the run", False)
            except Refused:
                check("a charged call stops the run", True)
            REPLAY = True
            n = len(calls)
            check("replay answers from the recording", complete("eins", purpose="selftest", doc=allowed[0])
                  .get("content") == "Kohärenz")
            check("replay never reaches the network", "unreached" in complete("sechs", purpose="selftest")
                  and len(calls) == n)
            REPLAY = False
            print("proxy")
            srv = serve(0)
            threading.Thread(target=srv.serve_forever, daemon=True).start()
            base = f"http://127.0.0.1:{srv.server_address[1]}/v1"

            def post(path, body, key):
                req = urllib.request.Request(base + path, data=json.dumps(body).encode(),
                                             headers={"Authorization": f"Bearer {key}",
                                                      "Content-Type": "application/json"})
                try:
                    with urllib.request.urlopen(req, timeout=10) as r:
                        return r.status, r.read().decode()
                except urllib.error.HTTPError as e:
                    return e.code, e.read().decode()

            msgs = {"messages": [{"role": "user", "content": "sieben"}], "model": "openai/gpt-5.6-sol"}
            script[:] = [answer("sieben")]
            s, text = post("/chat/completions", msgs, f"route:selftest:{allowed[0]}")
            check("a paid model asked for is answered by a free one",
                  s == 200 and calls[-1] in ("a:free", "b:free") and "openai/gpt-5.6-sol" not in calls)
            s, text = post("/chat/completions", {**msgs, "stream": True}, f"route:selftest:{allowed[0]}")
            events = [l[6:] for l in text.splitlines() if l.startswith("data: ")]
            check("a stream request gets server-sent events ending in [DONE]",
                  s == 200 and events[-1] == "[DONE]" and json.loads(events[0])["choices"][0]["delta"]["content"] == "sieben")
            check("a caller that does not name itself is refused", post("/chat/completions", msgs, "sk-real")[0] == 401)
            with urllib.request.urlopen(f"http://127.0.0.1:{srv.server_address[1]}/health", timeout=10) as r:
                check("GET /health answers 200 (cgr's litellm_proxy checks it)", r.status == 200)
            check("a caller declaring a document outside the consent is refused",
                  post("/chat/completions", msgs, f"route:selftest:{outsider}")[0] == 403)
            srv.shutdown()
            print("jev questions")
            try:
                _questions({"q": {"type": "score", "instructions": "x", "criteria": [str(i) for i in range(11)]}})
                check("a Score with eleven levels is refused before sending", False)
            except ValueError:
                check("a Score with eleven levels is refused before sending", True)
            except ImportError:
                print("  -- typesafe_sdk not importable here; run under .venv-typesafe/bin/python to check it")
        finally:
            OUT, _post, REPLAY = saved
    print(f"\n{'all hold' if not bad else f'{bad} FAILED'}")
    return 1 if bad else 0


def main(argv: list[str]) -> int:
    global REPLAY
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--replay", action="store_true", help="answer only from the recording; never call out")
    sub = p.add_subparsers(dest="cmd", required=True)
    sub.add_parser("models")
    s = sub.add_parser("serve")
    s.add_argument("--port", type=int, default=8787)
    sub.add_parser("ledger")
    g = sub.add_parser("guard")
    g.add_argument("slug")
    sub.add_parser("selftest")
    c = sub.add_parser("complete")
    c.add_argument("--purpose", required=True)
    c.add_argument("--doc")
    c.add_argument("--max-tokens", type=int, default=4000)
    c.add_argument("--json", action="store_true")
    c.add_argument("--expect", choices=["de", "en"])
    j = sub.add_parser("jev", help="stdin: {\"state\": {...}, \"questions\": {...}}")
    j.add_argument("--purpose", required=True)
    j.add_argument("--doc")
    a = p.parse_args(argv)
    REPLAY = a.replay or os.environ.get("ROUTE_REPLAY") == "1"
    try:
        if a.cmd == "models":
            return cmd_models()
        if a.cmd == "ledger":
            return cmd_ledger()
        if a.cmd == "guard":
            return cmd_guard(a.slug)
        if a.cmd == "selftest":
            return cmd_selftest()
        if a.cmd == "serve":
            srv = serve(a.port)
            g = guard()
            print(f"route: http://127.0.0.1:{srv.server_address[1]}/v1  "
                  f"({'replay only' if REPLAY else 'free models, data_collection=deny'}); "
                  f"guard over {g.documents} documents outside the consent; "
                  f"rotation: {', '.join(rotation())}", flush=True)
            srv.serve_forever()
            return 0
        if a.cmd == "complete":
            rec = complete(sys.stdin.read(), purpose=a.purpose, doc=a.doc, max_tokens=a.max_tokens,
                           json_mode=a.json, expect=a.expect)
            print(json.dumps({k: v for k, v in rec.items() if k != "response"}, ensure_ascii=False, indent=1))
            return 1 if "unreached" in rec else 0
        if a.cmd == "jev":
            spec = json.load(sys.stdin)
            rec = jev(spec["state"], spec["questions"], purpose=a.purpose, doc=a.doc)
            print(json.dumps(rec, ensure_ascii=False, indent=1))
            return 1 if "unreached" in rec else 0
    except Refused as e:
        print(f"refused: {e}", file=sys.stderr)
        return 3
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
