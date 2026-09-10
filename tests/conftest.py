import hashlib

import numpy as np
import pytest
import tiktoken

import metalmind.embeddings as embeddings_module


class _FakeEncoding:
    """Whitespace-based stand-in for tiktoken's cl100k_base encoding, so chunking tests
    don't need to fetch the real BPE file over the network. Token count and decode
    fidelity aren't exact, but chunk_markdown only relies on len()/slicing/decode, which
    this preserves."""

    def encode(self, text):
        return text.split(" ") if text else []

    def decode(self, tokens):
        return " ".join(tokens)


@pytest.fixture(autouse=True)
def fake_tiktoken(monkeypatch):
    monkeypatch.setattr(tiktoken, "get_encoding", lambda name: _FakeEncoding())


def _deterministic_vector(text: str, dim: int = 16) -> np.ndarray:
    digest = hashlib.sha256(text.encode("utf-8")).digest()
    seed = int.from_bytes(digest[:8], "little")
    rng = np.random.default_rng(seed)
    vec = rng.normal(size=dim)
    return vec / np.linalg.norm(vec)


@pytest.fixture(autouse=True)
def fake_embeddings(monkeypatch):
    """Replace the real sentence-transformers model with a fast, deterministic,
    offline stand-in so tests never need model downloads or network access.

    Call sites use `from .. import embeddings; embeddings.embed_texts(...)` (rather than
    `from ..embeddings import embed_texts`) specifically so this monkeypatch is observed
    everywhere.
    """

    def _fake_embed_texts(texts):
        texts = list(texts)
        if not texts:
            return np.zeros((0, 16))
        return np.stack([_deterministic_vector(t) for t in texts])

    monkeypatch.setattr(embeddings_module, "embed_texts", _fake_embed_texts)
    monkeypatch.setattr(embeddings_module, "embed_text", lambda t: _fake_embed_texts([t])[0])
