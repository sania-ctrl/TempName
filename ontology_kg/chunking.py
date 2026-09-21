import tiktoken

from .models import TextChunk

_ENCODING = "cl100k_base"


def chunk_text(doc_id: str, text: str, chunk_size: int, overlap: int) -> list:
    """Split `text` into token-based chunks of `chunk_size` tokens with `overlap` tokens of
    overlap between consecutive chunks. Local to ontology_kg -- functionally the same
    windowing logic as metalmind's chunker, but reimplemented here rather than imported, so
    this package has no dependency on metalmind's code."""
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
        chunk_str = enc.decode(tokens[start:end])
        chunks.append(TextChunk(chunk_id=f"{doc_id}::chunk{order}", doc_id=doc_id, text=chunk_str, order=order))
        if end == len(tokens):
            break
        start += step
        order += 1
    return chunks
