"""Apply reviewed duplicate-merge decisions to the graph already loaded in Neo4j.

This is the "collaborative verification" step from the paper: `build_kg.py` writes out
candidate duplicate pairs (dedup_candidates.json); a human (or several, whose votes you
average yourself before writing the decisions file) reviews them and accepts/rejects each
merge; this script applies the accepted merges via APOC's node-refactoring merge.

Usage:
    python -m scripts.apply_dedup --decisions decisions.json

Where decisions.json looks like:
    [{"a": "<key to keep>", "b": "<key to remove>", "merge": true}, ...]
"""
import argparse
import json

from metalmind.graph_store.neo4j_client import Neo4jClient


def main():
    parser = argparse.ArgumentParser(description="Apply reviewed duplicate-merge decisions to Neo4j.")
    parser.add_argument("--decisions", required=True, help="JSON list of {a, b, merge} decisions")
    args = parser.parse_args()

    decisions = json.loads(open(args.decisions).read())
    client = Neo4jClient()
    applied = 0
    with client._driver.session() as session:
        for decision in decisions:
            if not decision.get("merge"):
                continue
            session.run(
                "MATCH (keep:Entity {key: $a}), (remove:Entity {key: $b}) "
                "CALL apoc.refactor.mergeNodes([keep, remove], {properties: 'discard', mergeRels: true}) "
                "YIELD node RETURN node",
                a=decision["a"],
                b=decision["b"],
            )
            applied += 1
    client.close()
    print(f"Applied {applied} merge decisions.")


if __name__ == "__main__":
    main()
