import tiktoken

from ..models import TextChunk

_ENCODING = "cl100k_base"


def chunk_markdown(doc_id: str, text: str, chunk_size: int, overlap: int) -> list:
    """Split `text` into token-based chunks of `chunk_size` tokens with `overlap` tokens
    of overlap between consecutive chunks (paper §Preprocessing: 600 tokens / 100 overlap
    by default). These become the subnodes linked to the file's central document node."""
    if chunk_size <= overlap:
        raise ValueError("chunk_size must be greater than overlap")

    enc = tiktoken.get_encoding(_ENCODING)
    tokens = enc.encode(text)
    if not tokens:
        return []

    step = chunk_size - overlap
    chunks = []
    start = 0
    order = 0
    while start < len(tokens):
        end = min(start + chunk_size, len(tokens))
        chunk_text = enc.decode(tokens[start:end])
        chunks.append(TextChunk(chunk_id=f"{doc_id}::chunk{order}", doc_id=doc_id, text=chunk_text, order=order))
        if end == len(tokens):
            break
        start += step
        order += 1
    return chunks
