"""Build the fixed-ontology, multi-process manufacturing knowledge graph -- a separate project
from the Renishaw AM400 replication in `metalmind`. One combined graph across up to four AM
processes (FFF, SLA, LPBF, Sintering), using the schema:

    (:ManufacturingProcess)-[:HAS]->(:ProcessParameter)-[:AFFECTS]->(:PartProperty)

sourced from two papers per process. Loads into its own Neo4j instance (see docker-compose.yml's
neo4j-ontology service) so `--wipe` here never touches metalmind's Renishaw graph.

Usage:
    python -m scripts.build_ontology_kg --manifest papers_manifest.json --wipe

Manifest format (paths point to plain text or Markdown files, one per paper):
    {
      "FFF": ["papers/fff_paper1.md", "papers/fff_paper2.md"],
      "SLA": ["papers/sla_paper1.md", "papers/sla_paper2.md"],
      "LPBF": ["papers/lpbf_paper1.md", "papers/lpbf_paper2.md"],
      "Sintering": ["papers/sintering_paper1.md", "papers/sintering_paper2.md"]
    }
You don't need all four processes or exactly two papers each -- the manifest can be partial.
"""
import argparse
import json
from pathlib import Path

from metalmind.graph_store.neo4j_client import Neo4jClient
from metalmind.llm.client import LLMClient

from ontology_kg.config import settings
from ontology_kg.graph_store import load_ontology_graph
from ontology_kg.pipeline import build_ontology_graph


def main():
    parser = argparse.ArgumentParser(description="Build the fixed-ontology manufacturing KG.")
    parser.add_argument("--manifest", required=True, help="JSON: {process: [paper_path, ...]}")
    parser.add_argument("--wipe", action="store_true", help="Wipe the ontology Neo4j database before loading")
    args = parser.parse_args()

    manifest = json.loads(Path(args.manifest).read_text())
    if not manifest:
        raise SystemExit(f"No processes found in {args.manifest}")

    papers_by_process = {}
    for process, paper_paths in manifest.items():
        papers_by_process[process] = [
            (Path(p).stem, Path(p).read_text(encoding="utf-8")) for p in paper_paths
        ]
        print(f"{process}: loaded {len(paper_paths)} paper(s)")

    llm = LLMClient(model=settings.openai_model, api_key=settings.openai_api_key)
    graph = build_ontology_graph(
        papers_by_process, llm, chunk_size=settings.chunk_size_tokens, chunk_overlap=settings.chunk_overlap_tokens
    )
    print(
        f"Extracted {len(graph.parameters)} process parameters, {len(graph.properties)} part properties, "
        f"{len(graph.has_relations)} HAS relations, {len(graph.affects_relations)} AFFECTS relations"
    )
    print(f"LLM tokens used: {llm.total_tokens}")

    client = Neo4jClient(uri=settings.neo4j_uri, user=settings.neo4j_user, password=settings.neo4j_password)
    if args.wipe:
        client.wipe()
    load_ontology_graph(client, graph)
    client.close()
    print(f"Loaded ontology knowledge graph into Neo4j at {settings.neo4j_uri}")


if __name__ == "__main__":
    main()
