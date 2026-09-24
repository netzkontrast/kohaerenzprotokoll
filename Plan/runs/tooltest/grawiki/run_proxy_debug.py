import sys, traceback
import sentence_transformers  # pre-import before scripts/ shadows stdlib profile
sys.path.insert(0, "/home/user/kohaerenzprotokoll/scripts")
import route

orig_embed_fn = route.embed
def embed_debug(texts, *, purpose, doc=None):
    try:
        return orig_embed_fn(texts, purpose=purpose, doc=doc)
    except Exception:
        traceback.print_exc()
        raise

route.embed = embed_debug

srv = route.serve(8787)
print("serving with debug wrapper", flush=True)
srv.serve_forever()
