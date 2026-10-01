"""Pinned local static model. Queries never download weights or send text."""
import hashlib
import numpy as np
from huggingface_hub import snapshot_download
from tokenizers import Tokenizer


class Embedder:
    def __init__(self, config, offline=False):
        self.config = config
        options = dict(repo_id=config["model"], revision=config["revision"],
                       allow_patterns=["*.json", "*.safetensors"])
        try:
            self.path = snapshot_download(**options, local_files_only=True)
        except OSError:
            if offline:
                raise
            self.path = snapshot_download(**options)
        self.tokenizer = Tokenizer.from_file(self.path + "/tokenizer.json")
        self.model = None

    def count(self, text):
        return len(self.tokenizer.encode(text, add_special_tokens=False).ids)

    def encode(self, texts):
        if self.model is None:
            from model2vec import StaticModel
            self.model = StaticModel.from_pretrained(self.path, normalize=True)
        if not texts:
            return np.empty((0, self.model.dim), dtype=np.float16)
        values = self.model.encode(texts, max_length=None, use_multiprocessing=False)
        norms = np.linalg.norm(values, axis=1, keepdims=True)
        values = np.divide(values, norms, out=np.zeros_like(values), where=norms != 0)
        if not np.isfinite(values).all():
            raise ValueError("nonfinite embedding")
        return values.astype(np.float16)


def ids_hash(ids):
    return hashlib.sha256("\n".join(ids).encode()).hexdigest()
