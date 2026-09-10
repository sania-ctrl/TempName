from dataclasses import dataclass
from typing import Optional


@dataclass
class TextChunk:
    """A subnode of a document: one ~600-token slice with 100-token overlap (paper §Preprocessing)."""

    chunk_id: str
    doc_id: str
    text: str
    order: int
    embedding: Optional[list] = None


@dataclass
class ImageAsset:
    """An image extracted from a source document, represented as its own KG node (Figure)."""

    image_id: str
    url: str
    caption: str
    source_chunk_id: str
    embedding: Optional[list] = None
