from itertools import combinations

import numpy as np

from ..config import settings


def find_candidate_duplicates(kg, threshold: float = None) -> list:
    """Embedding-similarity duplicate detection (paper §KG post-processing / Fig. 4b).

    Compares entities within the same category and flags pairs whose description
    embeddings exceed `threshold` cosine similarity as candidates for the collaborative
    node-review step. Returns a JSON-serializable list, sorted most-similar first, meant
    to be reviewed by a human (accept/reject) before merging.
    """
    threshold = settings.duplicate_similarity_threshold if threshold is None else threshold

    by_category = {}
    for key, entity in kg.entities.items():
        if entity.embedding is None:
            continue
        by_category.setdefault(entity.category, []).append((key, entity))

    candidates = []
    for category, items in by_category.items():
        for (key_a, entity_a), (key_b, entity_b) in combinations(items, 2):
            similarity = float(np.dot(entity_a.embedding, entity_b.embedding))
            if similarity >= threshold:
                candidates.append(
                    {
                        "a": key_a,
                        "b": key_b,
                        "name_a": entity_a.name,
                        "name_b": entity_b.name,
                        "category": category,
                        "similarity": similarity,
                    }
                )
    candidates.sort(key=lambda c: -c["similarity"])
    return candidates


def merge_entities(kg, keep_key: str, remove_key: str) -> None:
    """Apply an accepted duplicate-merge decision to the in-memory KnowledgeGraph:
    fold `remove_key` into `keep_key` and repoint its relations."""
    keep = kg.entities[keep_key]
    removed = kg.entities.pop(remove_key)
    keep.source_chunk_ids |= removed.source_chunk_ids

    for relation in kg.relations:
        if relation.head.strip().lower() == remove_key:
            relation.head = keep.name
        if relation.tail.strip().lower() == remove_key:
            relation.tail = keep.name
