RUBRIC_SYSTEM = """You are a domain expert in metal additive manufacturing (AM) machine operation, evaluating \
an AI assistant's answer against these criteria:
1. Technical accuracy relative to the provided context
2. Completeness (covers the key aspects of the question)
3. Clarity and actionability for a machine operator
4. Appropriate scope (neither missing critical context nor including irrelevant detail)

Score the answer from 1 (poor) to 5 (excellent) as a single overall rubric score.

Return strict JSON: {"score": int, "justification": str}
"""


def rubric_score(llm, question: str, answer: str, context: list) -> int:
    """(v) Domain-specific rubric: a 1-5 expert-style rating standing in for the paper's
    human-expert rubric scoring."""
    user = f"Question: {question}\n\nContext:\n{chr(10).join(context)}\n\nAnswer:\n{answer}"
    result = llm.complete_json(RUBRIC_SYSTEM, user)
    score = result.get("score", 3)
    try:
        return max(1, min(5, int(score)))
    except (TypeError, ValueError):
        return 3
