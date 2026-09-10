import numpy as np

from .. import embeddings

FAITHFULNESS_SYSTEM = """You are evaluating whether an AI-generated answer is factually supported by the given \
context. Break the answer into atomic factual claims, then judge for each claim whether it is directly \
supported by the context.

Return strict JSON: {"claims": [{"claim": str, "supported": bool}]}
"""

RELEVANCY_SYSTEM_TEMPLATE = """Given the following answer, generate {n} distinct questions that this answer \
would be a good, complete response to.

Return strict JSON: {{"questions": [str, ...]}}
"""

CONTEXT_PRECISION_SYSTEM = """For each numbered context passage, judge whether it is relevant to answering the \
given question.

Return strict JSON: {"relevance": [true_or_false, ...]} in the same order as the passages.
"""

CONTEXT_RECALL_SYSTEM = """Break the ground-truth answer into atomic factual statements. For each, judge \
whether it can be attributed to (found in) the given context.

Return strict JSON: {"statements": [{"statement": str, "attributed": bool}]}
"""


def faithfulness(llm, answer: str, context: list) -> float:
    """(i) Faithfulness: factual consistency of the answer relative to the retrieved context."""
    result = llm.complete_json(FAITHFULNESS_SYSTEM, f"Context:\n{chr(10).join(context)}\n\nAnswer:\n{answer}")
    claims = result.get("claims", [])
    if not claims:
        return 1.0
    return sum(1 for c in claims if c.get("supported")) / len(claims)


def answer_relevancy(llm, question: str, answer: str, n_variants: int = 3) -> float:
    """(ii) Answer relevancy: penalizes incomplete/redundant answers by checking how well
    questions re-generated from the answer align with the original question."""
    system = RELEVANCY_SYSTEM_TEMPLATE.format(n=n_variants)
    result = llm.complete_json(system, answer)
    generated = result.get("questions", [])
    if not generated:
        return 0.0
    question_vec = embeddings.embed_text(question)
    sims = [embeddings.cosine_sim(question_vec, embeddings.embed_text(q)) for q in generated]
    return float(np.mean(sims))


def context_precision(llm, question: str, context: list) -> float:
    """(iii) Context precision: proportion of retrieved passages that are actually relevant."""
    if not context:
        return 0.0
    passages = "\n\n".join(f"[{i + 1}] {c}" for i, c in enumerate(context))
    result = llm.complete_json(CONTEXT_PRECISION_SYSTEM, f"Question: {question}\n\nPassages:\n{passages}")
    flags = result.get("relevance", [])
    if not flags:
        return 0.0
    return sum(1 for f in flags if f) / len(flags)


def context_recall(llm, ground_truth: str, context: list) -> float:
    """(iv) Context recall: how much of the ground-truth answer is attributable to retrieved context."""
    if not context:
        return 0.0
    user = f"Ground truth:\n{ground_truth}\n\nContext:\n{chr(10).join(context)}"
    result = llm.complete_json(CONTEXT_RECALL_SYSTEM, user)
    statements = result.get("statements", [])
    if not statements:
        return 1.0
    return sum(1 for s in statements if s.get("attributed")) / len(statements)
