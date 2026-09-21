from dataclasses import dataclass
from typing import Optional


@dataclass
class TextChunk:
    """A token-based text slice, local to ontology_kg (deliberately not the metalmind.models
    version -- this project has no code dependency on the Renishaw/metalmind work)."""

    chunk_id: str
    doc_id: str
    text: str
    order: int
    embedding: Optional[list] = None
