"""Shared embedding utilities.

Callers should `from .. import embeddings` and call `embeddings.embed_texts(...)`
rather than `from ..embeddings import embed_texts`, so that tests can monkeypatch
`metalmind.embeddings.embed_texts` and have the patch observed everywhere.
"""
from functools import lru_cache

import numpy as np


@lru_cache(maxsize=1)
def _model():
    from sentence_transformers import SentenceTransformer
    from .config import settings

    return SentenceTransformer(settings.embedding_model)


def embed_texts(texts: list) -> np.ndarray:
    """Embed a list of strings. Matches the paper's `all-MiniLM-L6-v2`, 384-dim model."""
    if not texts:
        return np.zeros((0, 384))
    return np.asarray(_model().encode(list(texts), normalize_embeddings=True, show_progress_bar=False))


def embed_text(text: str) -> np.ndarray:
    return embed_texts([text])[0]


def cosine_sim(a, b) -> float:
    return float(np.dot(np.asarray(a), np.asarray(b)))
