"""Inspect the ACTUAL pairwise entity-similarity distribution in your built graph, so you can
pick a duplicate-detection threshold from real data instead of trusting a guessed constant.
Mirrors the paper's Fig. 4b similarity-distance analysis.

Run this after `scripts/build_kg.py` has loaded a real graph into Neo4j.

Usage:
    python -m scripts.calibrate_dedup_threshold
"""
from collections import defaultdict
from itertools import combinations

import numpy as np

from metalmind.graph_store.neo4j_client import Neo4jClient
from metalmind.postprocessing.dedup import name_token_overlap


def main():
    client = Neo4jClient()
    rows = client.all_entities_with_category()
    client.close()

    by_category = defaultdict(list)
    for name, _description, embedding, category in rows:
        if embedding is not None:
            by_category[category].append((name, np.asarray(embedding)))

    pairs = []
    for category, items in by_category.items():
        for (name_a, emb_a), (name_b, emb_b) in combinations(items, 2):
            similarity = float(np.dot(emb_a, emb_b))
            pairs.append((similarity, name_token_overlap(name_a, name_b), category, name_a, name_b))

    if not pairs:
        print("No within-category entity pairs found -- build the graph first (scripts/build_kg.py).")
        return

    similarities = np.array([p[0] for p in pairs])
    print(f"{len(pairs)} within-category entity pairs compared\n")
    print(
        f"min={similarities.min():.3f}  mean={similarities.mean():.3f}  "
        f"median={np.median(similarities):.3f}  max={similarities.max():.3f}\n"
    )

    print("Histogram (cosine similarity, 0.05-wide buckets):")
    counts, edges = np.histogram(similarities, bins=20, range=(0.0, 1.0))
    max_count = max(counts.max(), 1)
    for count, lo in zip(counts, edges[:-1]):
        bar = "#" * max(1, round(60 * count / max_count)) if count else ""
        print(f"  {lo:0.2f}-{lo + 0.05:0.2f}: {count:>6}  {bar}")

    print("\nTop 25 most similar pairs -- inspect these to judge where real duplicates start")
    print("(high similarity + high name_overlap is the strongest duplicate signal):\n")
    pairs.sort(key=lambda p: -p[0])
    print(f"  {'similarity':>10}  {'name_overlap':>12}  category            name_a  <->  name_b")
    for similarity, overlap, category, name_a, name_b in pairs[:25]:
        print(f"  {similarity:>10.3f}  {overlap:>12.2f}  {category:<18}  {name_a!r}  <->  {name_b!r}")

    print(
        "\nSet DUP_SIM_THRESHOLD in .env to a value just below where this list stops looking "
        "like real duplicates to you."
    )


if __name__ == "__main__":
    main()
