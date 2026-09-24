# Work around scripts/profile.py shadowing stdlib profile.py (needed transitively by
# torch/transformers, which sentence-transformers imports for the local embedder).
# python3 scripts/route.py puts scripts/ at sys.path[0], so `import profile` inside
# torch._dynamo resolves to scripts/profile.py instead of the stdlib module, and the
# proxy's /v1/embeddings answers 501 "no local embedder" even under .venv-grawiki.
# This executes the same, unmodified route.py source without scripts/ on sys.path.
import sys
sys.argv = ["route.py", "serve", "--port", "8787"]
path = "/home/user/kohaerenzprotokoll/scripts/route.py"
src = open(path, encoding="utf-8").read()
code = compile(src, path, "exec")
g = {"__name__": "__main__", "__file__": path}
exec(code, g)
