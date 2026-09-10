import numpy as np

from .. import embeddings
from .base import RetrievalResult


def vector_search(client, query: str, top_k: int = 5) -> RetrievalResult:
    """Mode 1 (paper §Multi-faceted RAG): cosine-similarity search over `Document` chunk
    nodes. Best suited to granular, fine-grained queries."""
    query_vec = embeddings.embed_text(query)
    rows = client.all_document_chunks()

    scored = [(float(np.dot(query_vec, np.asarray(emb))), chunk_id, text) for chunk_id, text, emb in rows]
    scored.sort(key=lambda x: -x[0])
    top = scored[:top_k]

    return RetrievalResult(
        context=[text for _, _, text in top],
        chunk_ids=[chunk_id for _, chunk_id, _ in top],
    )
