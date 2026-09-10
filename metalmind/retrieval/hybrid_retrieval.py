from .base import RetrievalResult
from .graph_retrieval import graph_search
from .vector_retrieval import vector_search


def hybrid_search(
    client, query: str, top_k_chunks: int = 3, seed_k: int = 3, hops: int = 1, max_context: int = 15
) -> RetrievalResult:
    """Mode 3 (paper §Multi-faceted RAG): vector-based retrieval to anchor on semantically
    relevant chunks, expanded with graph traversal for structured, relational context."""
    vector_result = vector_search(client, query, top_k=top_k_chunks)
    graph_result = graph_search(client, query, seed_k=seed_k, hops=hops, max_context=max_context)

    return RetrievalResult(
        context=(vector_result.context + graph_result.context)[:max_context],
        chunk_ids=vector_result.chunk_ids,
        entity_names=graph_result.entity_names,
    )
