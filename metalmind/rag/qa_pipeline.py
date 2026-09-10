ANSWER_SYSTEM = """You are a technical assistant for metal additive manufacturing (AM) machine operation and \
maintenance. Answer the user's question using ONLY the provided context. If the context is insufficient, say \
so explicitly rather than guessing. Cite specific details from the context where relevant.
"""


def answer_query(llm, query: str, retrieval_result) -> tuple:
    """Generate an answer grounded in the given retrieval context. Returns (answer_text, tokens_used)
    so callers can report the token-efficiency numbers in Table 1."""
    context_block = "\n\n".join(f"[{i + 1}] {c}" for i, c in enumerate(retrieval_result.context))
    user = f"Context:\n{context_block}\n\nQuestion: {query}"
    return llm.complete_text(ANSWER_SYSTEM, user)
