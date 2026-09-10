import numpy as np

from .. import embeddings
from .base import RetrievalResult


def _seed_entities(client, query: str, seed_k: int):
    query_vec = embeddings.embed_text(query)
    rows = client.all_entities()
    scored = [(float(np.dot(query_vec, np.asarray(emb))), name, desc) for name, desc, emb in rows]
    scored.sort(key=lambda x: -x[0])
    return scored[:seed_k]


def graph_search(client, query: str, seed_k: int = 3, hops: int = 2, max_context: int = 15) -> RetrievalResult:
    """Mode 2 (paper §Multi-faceted RAG): seed with the entities most relevant to the query,
    then expand via graph traversal to surface indirect relationships and dependencies —
    e.g. multi-step processes — that a purely semantic search would miss."""
    seeds = _seed_entities(client, query, seed_k)

    context, entity_names, seen = [], [], set()
    for _, name, description in seeds:
        if name in seen:
            continue
        seen.add(name)
        entity_names.append(name)
        context.append(f"{name}: {description}")

    for _, name, _ in seeds:
        if len(context) >= max_context:
            break
        for neighbor_name, neighbor_desc in client.neighbors(name, hops=hops, limit=max_context):
            if neighbor_name in seen:
                continue
            seen.add(neighbor_name)
            entity_names.append(neighbor_name)
            context.append(f"{neighbor_name}: {neighbor_desc}")
            if len(context) >= max_context:
                break

    return RetrievalResult(context=context[:max_context], entity_names=entity_names[:max_context])
