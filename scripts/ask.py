"""Ask MetalMind a question and see the answer immediately — no evaluation metrics, just
retrieval + one generation call, so the answer comes back as fast as possible.

One-shot:
    python -m scripts.ask "What alcohol concentration is required for wiper cleaning?"

Interactive (keeps the Neo4j connection and LLM client warm between questions):
    python -m scripts.ask

Options:
    --mode {vector,graph,hybrid}   retrieval strategy (default: hybrid)
    --images                       also print any images linked to the retrieved context
"""
import argparse

from metalmind.graph_store.neo4j_client import Neo4jClient
from metalmind.llm.client import LLMClient
from metalmind.rag.qa_pipeline import answer_query
from metalmind.retrieval.graph_retrieval import graph_search
from metalmind.retrieval.hybrid_retrieval import hybrid_search
from metalmind.retrieval.image_retrieval import images_for_retrieval
from metalmind.retrieval.vector_retrieval import vector_search

MODES = {"vector": vector_search, "graph": graph_search, "hybrid": hybrid_search}


def ask(client, llm, query: str, mode: str, show_images: bool) -> None:
    retrieve_fn = MODES[mode]
    retrieval_result = retrieve_fn(client, query)

    if not retrieval_result.context:
        print("No relevant context found in the knowledge graph for that question.\n")
        return

    answer, tokens = answer_query(llm, query, retrieval_result)
    print(f"\n{answer}\n")
    print(f"[{mode} mode, {tokens} tokens, {len(retrieval_result.context)} passages used]")

    if show_images:
        images = images_for_retrieval(client, retrieval_result)
        if images:
            print("Related images:")
            for url, caption in images:
                print(f"  - {caption}: {url}")
    print()


def main():
    parser = argparse.ArgumentParser(description="Ask MetalMind a question and get an immediate answer.")
    parser.add_argument("query", nargs="?", help="Question to ask. Omit to start an interactive session.")
    parser.add_argument("--mode", choices=MODES.keys(), default="hybrid")
    parser.add_argument("--images", action="store_true", help="Also show images linked to the retrieved context")
    args = parser.parse_args()

    client = Neo4jClient()
    llm = LLMClient()

    try:
        if args.query:
            ask(client, llm, args.query, args.mode, args.images)
            return

        print(f"MetalMind interactive Q&A (mode={args.mode}). Type 'quit' to exit.\n")
        while True:
            try:
                query = input("> ").strip()
            except (EOFError, KeyboardInterrupt):
                print()
                break
            if not query:
                continue
            if query.lower() in {"quit", "exit"}:
                break
            ask(client, llm, query, args.mode, args.images)
    finally:
        client.close()


if __name__ == "__main__":
    main()
