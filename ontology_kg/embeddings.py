"""Embedding utilities local to ontology_kg -- deliberately not shared with metalmind, so this
project has no code dependency on the Renishaw/metalmind work. Functionally the same
sentence-transformers wrapper, reimplemented here rather than imported.
"""
from functools import lru_cache

import numpy as np


@lru_cache(maxsize=1)
def _model():
    from sentence_transformers import SentenceTransformer

    from .config import settings

    return SentenceTransformer(settings.embedding_model)


def embed_texts(texts: list) -> np.ndarray:
    if not texts:
        return np.zeros((0, 384))
    return np.asarray(_model().encode(list(texts), normalize_embeddings=True, show_progress_bar=False))


def embed_text(text: str) -> np.ndarray:
    return embed_texts([text])[0]
