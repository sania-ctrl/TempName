"""Build the MetalMind knowledge graph from a directory of Markdown documents and load it
into Neo4j.

Usage:
    python -m scripts.build_kg --docs data/sample_docs --wipe
"""
import argparse
import json
from pathlib import Path

from metalmind.config import settings
from metalmind.graph_store.neo4j_client import Neo4jClient
from metalmind.kg_construction.pipeline import build_knowledge_graph
from metalmind.llm.client import LLMClient
from metalmind.models import ImageAsset
from metalmind.postprocessing.cleanup import prune_standalone_entities
from metalmind.postprocessing.dedup import find_candidate_duplicates
from metalmind.preprocessing.chunking import chunk_markdown
from metalmind.preprocessing.document_loader import load_markdown_docs


def main():
    parser = argparse.ArgumentParser(description="Build the MetalMind knowledge graph from Markdown docs.")
    parser.add_argument("--docs", required=True, help="Directory of .md documents")
    parser.add_argument(
        "--images", help='JSON manifest: {"image_id": {"url": str, "caption": str, "source_chunk_id": str}}'
    )
    parser.add_argument("--wipe", action="store_true", help="Wipe Neo4j before loading")
    parser.add_argument("--dedup-report", default="dedup_candidates.json")
    args = parser.parse_args()

    docs = load_markdown_docs(Path(args.docs))
    if not docs:
        raise SystemExit(f"No .md files found in {args.docs}")

    chunks = []
    for doc_id, text in docs.items():
        chunks.extend(chunk_markdown(doc_id, text, settings.chunk_size_tokens, settings.chunk_overlap_tokens))
    print(f"Loaded {len(docs)} documents -> {len(chunks)} chunks")

    images = []
    if args.images:
        manifest = json.loads(Path(args.images).read_text())
        for image_id, meta in manifest.items():
            images.append(
                ImageAsset(
                    image_id=image_id,
                    url=meta["url"],
                    caption=meta.get("caption", ""),
                    source_chunk_id=meta["source_chunk_id"],
                )
            )

    llm = LLMClient()
    kg = build_knowledge_graph(chunks, llm, images=images)
    print(f"Extracted {len(kg.entities)} entities, {len(kg.relations)} relations, {len(kg.images)} image nodes")
    print(f"LLM tokens used: {llm.total_tokens}")

    removed = prune_standalone_entities(kg)
    print(f"Pruned {len(removed)} standalone entities")

    candidates = find_candidate_duplicates(kg)
    Path(args.dedup_report).write_text(json.dumps(candidates, indent=2))
    print(f"Wrote {len(candidates)} candidate duplicate pairs to {args.dedup_report} for manual review")
    print(
        "Review that file, then produce a decisions file of "
        '[{"a": key, "b": key, "merge": true/false}, ...] and run scripts/apply_dedup.py'
    )

    client = Neo4jClient()
    if args.wipe:
        client.wipe()
    client.load_knowledge_graph(kg)
    client.close()
    print("Loaded knowledge graph into Neo4j")


if __name__ == "__main__":
    main()
