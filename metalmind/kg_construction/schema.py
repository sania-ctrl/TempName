from .. import embeddings
from . import prompts

DEFAULT_CATEGORIES = ["Component", "Operation", "Maintenance", "Parameter", "Material", "SafetyNotice", "Document"]


def derive_schema(llm, entities: list, n_clusters: int = 8) -> list:
    """Algorithm 1, Phase 1 (line 7): cluster schema-free entities into schema categories.

    Entities are embedded and clustered with K-means (mirroring the PCA/K-means analysis in
    Fig. 4b); an LLM then names each cluster with a manufacturing-domain category label.
    """
    unique_names = list(dict.fromkeys(e.name for e in entities))
    if len(unique_names) < 2:
        return DEFAULT_CATEGORIES

    from sklearn.cluster import KMeans

    vectors = embeddings.embed_texts(unique_names)
    k = max(2, min(n_clusters, len(unique_names)))
    km = KMeans(n_clusters=k, n_init=10, random_state=42).fit(vectors)

    clusters = {}
    for label, name in zip(km.labels_, unique_names):
        clusters.setdefault(int(label), []).append(name)

    sample_lines = [f"Cluster {label}: {', '.join(members[:15])}" for label, members in clusters.items()]
    result = llm.complete_json(prompts.SCHEMA_DERIVATION_SYSTEM, "\n".join(sample_lines))
    categories = [c["name"] for c in result.get("categories", []) if c.get("name")]
    return categories or DEFAULT_CATEGORIES
