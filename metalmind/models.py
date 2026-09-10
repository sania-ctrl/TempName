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


@dataclass
class VideoAsset:
    """A source video (e.g. the paper's S1/S2 supplementary demo clips), represented as its
    own KG node (Video). `description` is a GPT-4o-generated, frame-sampled transcript of what
    the video shows; that description is also chunked and run through the normal entity/relation
    extraction pipeline, so the video contributes real KG content, not just a caption."""

    video_id: str
    path: str
    description: str
    source_chunk_id: str
    embedding: Optional[list] = None
