"""Run the multi-faceted RAG evaluation harness (paper §Retrieval performance):
compares vector / graph / hybrid retrieval on faithfulness, answer relevancy, context
precision/recall, rubric score, token consumption, and a composite token-efficiency score.

Usage:
    python -m scripts.evaluate --dataset data/eval_dataset.json
"""
import argparse
import json

import numpy as np

from metalmind.evaluation import metrics, rubric, token_efficiency
from metalmind.graph_store.neo4j_client import Neo4jClient
from metalmind.llm.client import LLMClient
from metalmind.rag.qa_pipeline import answer_query
from metalmind.retrieval.graph_retrieval import graph_search
from metalmind.retrieval.hybrid_retrieval import hybrid_search
from metalmind.retrieval.vector_retrieval import vector_search

MODES = {"vector": vector_search, "graph": graph_search, "hybrid": hybrid_search}
METRIC_KEYS = ("faithfulness", "answer_relevancy", "context_precision", "context_recall", "rubric", "accuracy")


def evaluate_item(llm, client, mode_name, retrieve_fn, item):
    retrieval_result = retrieve_fn(client, item["query"])
    answer, tokens = answer_query(llm, item["query"], retrieval_result)

    faith = metrics.faithfulness(llm, answer, retrieval_result.context)
    relevancy = metrics.answer_relevancy(llm, item["query"], answer)
    precision = metrics.context_precision(llm, item["query"], retrieval_result.context)
    recall = metrics.context_recall(llm, item["ground_truth"], retrieval_result.context)
    rub = rubric.rubric_score(llm, item["query"], answer, retrieval_result.context)
    accuracy = float(np.mean([faith, relevancy, precision, recall, rub / 5]))

    row = {
        "faithfulness": faith,
        "answer_relevancy": relevancy,
        "context_precision": precision,
        "context_recall": recall,
        "rubric": rub,
        "accuracy": accuracy,
    }
    return row, tokens


def main():
    parser = argparse.ArgumentParser(description="Run the multi-faceted RAG evaluation harness.")
    parser.add_argument("--dataset", default="data/eval_dataset.json")
    args = parser.parse_args()

    dataset = json.loads(open(args.dataset).read())
    client = Neo4jClient()
    llm = LLMClient()

    results = {mode: {"granular": [], "global": []} for mode in MODES}
    tokens_used = {mode: {"granular": [], "global": []} for mode in MODES}

    for item in dataset:
        qtype = item["type"]
        for mode_name, retrieve_fn in MODES.items():
            row, tokens = evaluate_item(llm, client, mode_name, retrieve_fn, item)
            results[mode_name][qtype].append(row)
            tokens_used[mode_name][qtype].append(tokens)

    header = f"{'Mode':<8}{'Type':<10}{'Faith':>8}{'Relev':>8}{'Prec':>8}{'Recall':>8}{'Rubric':>8}{'Tokens':>10}"
    print(header)

    composite_inputs = {}
    for mode_name in MODES:
        for qtype in ("granular", "global"):
            rows = results[mode_name][qtype]
            if not rows:
                continue
            avg = {k: float(np.mean([r[k] for r in rows])) for k in METRIC_KEYS}
            avg_tokens = float(np.mean(tokens_used[mode_name][qtype]))
            composite_inputs.setdefault(qtype, {})[mode_name] = (avg["accuracy"], avg_tokens)
            print(
                f"{mode_name:<8}{qtype:<10}{avg['faithfulness']:>8.3f}{avg['answer_relevancy']:>8.3f}"
                f"{avg['context_precision']:>8.3f}{avg['context_recall']:>8.3f}{avg['rubric']:>8.2f}"
                f"{avg_tokens:>10.0f}"
            )

    print("\nComposite scores (70% accuracy / 30% token-efficiency, sigmoid-scaled 1-5):")
    for qtype, per_mode in composite_inputs.items():
        mode_names = list(per_mode.keys())
        accuracy_values = [per_mode[m][0] for m in mode_names]
        token_values = [per_mode[m][1] for m in mode_names]
        scores = token_efficiency.composite_score(accuracy_values, token_values)
        for mode_name, score in zip(mode_names, scores):
            print(f"  {qtype:<10}{mode_name:<8}{score:.2f}")

    client.close()


if __name__ == "__main__":
    main()
