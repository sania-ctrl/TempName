import numpy as np

from .. import embeddings
from ..config import settings


def images_for_retrieval(client, retrieval_result) -> list:
    """Step 1 (paper §Multi-faceted RAG, image retrieval): images directly linked to the
    entities/chunks that were retrieved as context."""
    hits = set()
    hits.update(client.images_for_chunks(retrieval_result.chunk_ids))
    hits.update(client.images_for_entities(retrieval_result.entity_names))
    return list(hits)


def images_by_answer_similarity(client, summary_text: str, threshold: float = None) -> list:
    """Step 2 (paper §Multi-faceted RAG, image retrieval): after generating the answer,
    compare the summarized response against every image caption's embedding; keep images
    whose similarity exceeds `threshold` (0.85 in the paper)."""
    threshold = settings.image_similarity_threshold if threshold is None else threshold
    summary_vec = embeddings.embed_text(summary_text)

    scored = []
    for url, caption, emb in client.all_images():
        similarity = float(np.dot(summary_vec, np.asarray(emb)))
        if similarity >= threshold:
            scored.append((similarity, url, caption))
    scored.sort(key=lambda x: -x[0])
    return [(url, caption) for _, url, caption in scored]
