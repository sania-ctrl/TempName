from itertools import combinations

import numpy as np

from ..config import settings


def name_token_overlap(name_a: str, name_b: str) -> float:
    """Jaccard similarity between two entity names' lowercased word sets -- a cheap, independent
    signal alongside embedding cosine similarity. Purely semantic similarity can conflate two
    genuinely distinct entities whose descriptions happen to be phrased alike (e.g. "Argon
    Cylinder" vs. "Nitrogen Cylinder"); this doesn't replace that judgment call, but it gives a
    reviewer a second number to weigh instead of trusting one embedding threshold alone. Real
    duplicates in the paper's own examples share tokens too (e.g. "Argon Supply Line" / "Argon
    Gas Supply" / "Argon Supply" all share "Argon" and/or "Supply")."""
    tokens_a = set(name_a.lower().split())
    tokens_b = set(name_b.lower().split())
    if not tokens_a or not tokens_b:
        return 0.0
    return len(tokens_a & tokens_b) / len(tokens_a | tokens_b)


def find_candidate_duplicates(kg, threshold: float = None) -> list:
    """Embedding-similarity duplicate detection (paper §KG post-processing / Fig. 4b).

    Compares entities within the same category and flags pairs whose description
    embeddings exceed `threshold` cosine similarity as candidates for the collaborative
    node-review step. Each candidate also carries `name_overlap` (see `name_token_overlap`)
    as a second, independent signal -- a low name overlap on an otherwise high-similarity pair
    is worth extra scrutiny before accepting the merge. Returns a JSON-serializable list,
    sorted most-similar first, meant to be reviewed by a human (accept/reject) before merging.

    `threshold` itself is still a judgment call -- run `scripts/calibrate_dedup_threshold.py`
    against your actual built graph to see the real similarity distribution (mirroring the
    paper's Fig. 4b histogram) rather than trusting the default.
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
                        "name_overlap": name_token_overlap(entity_a.name, entity_b.name),
                    }
                )
    candidates.sort(key=lambda c: (-c["similarity"], -c["name_overlap"]))
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
