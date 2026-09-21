"""Build the fixed-ontology, multi-process manufacturing knowledge graph -- fully independent of
the Renishaw AM400 replication in `metalmind` (its own code, its own database, no import of
metalmind anywhere in this package). One combined graph across up to four AM processes (FFF,
SLA, LBM, Sintering), using the schema:

    (:ManufacturingProcess)-[:HAS]->(:ProcessParameter)-[:AFFECTS]->(:PartProperty)

sourced from two papers per process. Loads into its own Neo4j instance (see docker-compose.yml's
neo4j-ontology service) so `--wipe` here never touches metalmind's Renishaw graph.

Persists to Neo4j after EVERY paper, not just at the end -- a real run is hundreds of LLM calls
long and can be interrupted (rate limits, a crash, a closed laptop); this way a mid-run
interruption only costs you the current paper's progress, not the whole run's.

Usage:
    python -m scripts.build_ontology_kg --manifest papers_manifest.json --wipe

Manifest format (paths point to plain text or Markdown files, one per paper):
    {
      "FFF": ["papers/fff_paper1.md", "papers/fff_paper2.md"],
      "SLA": ["papers/sla_paper1.md", "papers/sla_paper2.md"],
      "LBM": ["papers/lbm_paper1.md", "papers/lbm_paper2.md"],
      "Sintering": ["papers/sintering_paper1.md", "papers/sintering_paper2.md"]
    }
You don't need all four processes or exactly two papers each -- the manifest can be partial.
"""
import argparse
import json
from pathlib import Path

from ontology_kg.config import settings
from ontology_kg.graph_store import load_ontology_graph
from ontology_kg.llm_client import LLMClient
from ontology_kg.neo4j_client import Neo4jClient
from ontology_kg.pipeline import OntologyGraph, embed_new_entities, process_paper


def main():
    parser = argparse.ArgumentParser(description="Build the fixed-ontology manufacturing KG.")
    parser.add_argument("--manifest", required=True, help="JSON: {process: [paper_path, ...]}")
    parser.add_argument("--wipe", action="store_true", help="Wipe the ontology Neo4j database before loading")
    args = parser.parse_args()

    manifest = json.loads(Path(args.manifest).read_text())
    if not manifest:
        raise SystemExit(f"No processes found in {args.manifest}")

    papers_by_process = {}
    total_papers = 0
    for process, paper_paths in manifest.items():
        papers_by_process[process] = [
            (Path(p).stem, Path(p).read_text(encoding="utf-8")) for p in paper_paths
        ]
        total_papers += len(paper_paths)
        print(f"{process}: loaded {len(paper_paths)} paper(s)")

    llm = LLMClient(model=settings.openai_model, api_key=settings.openai_api_key)
    client = Neo4jClient(uri=settings.neo4j_uri, user=settings.neo4j_user, password=settings.neo4j_password)
    if args.wipe:
        client.wipe()

    graph = OntologyGraph()
    done = 0
    try:
        for process, papers in papers_by_process.items():
            for paper_id, text in papers:
                process_paper(
                    graph,
                    process,
                    paper_id,
                    text,
                    llm,
                    chunk_size=settings.chunk_size_tokens,
                    chunk_overlap=settings.chunk_overlap_tokens,
                )
                embed_new_entities(graph)
                load_ontology_graph(client, graph)
                done += 1
                print(
                    f"[{done}/{total_papers}] Saved to Neo4j after {process}/{paper_id} -- "
                    f"{len(graph.parameters)} parameters, {len(graph.properties)} properties, "
                    f"{len(graph.has_relations)} HAS, {len(graph.affects_relations)} AFFECTS so far"
                )
    finally:
        client.close()

    print(f"LLM tokens used: {llm.total_tokens}")
    print(f"Finished: {done}/{total_papers} papers loaded into Neo4j at {settings.neo4j_uri}")


if __name__ == "__main__":
    main()
