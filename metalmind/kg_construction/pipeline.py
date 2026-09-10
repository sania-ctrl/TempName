from dataclasses import dataclass, field
from typing import Optional

from tqdm import tqdm

from .. import embeddings
from ..models import ImageAsset, TextChunk, VideoAsset
from . import extraction, schema


@dataclass
class GraphEntity:
    name: str
    category: str
    description: str
    source_chunk_ids: set = field(default_factory=set)
    embedding: Optional[list] = None


@dataclass
class GraphRelation:
    head: str
    relation: str
    tail: str
    source_chunk_id: str


@dataclass
class KnowledgeGraph:
    entities: dict = field(default_factory=dict)  # normalized name -> GraphEntity
    relations: list = field(default_factory=list)
    chunks: dict = field(default_factory=dict)  # chunk_id -> TextChunk
    images: dict = field(default_factory=dict)  # image_id -> ImageAsset
    videos: dict = field(default_factory=dict)  # video_id -> VideoAsset

    @staticmethod
    def _key(name: str) -> str:
        return name.strip().lower()

    def upsert_entity(self, name: str, category: str, description: str, chunk_id: str) -> str:
        key = self._key(name)
        existing = self.entities.get(key)
        if existing:
            existing.source_chunk_ids.add(chunk_id)
            if len(description) > len(existing.description):
                existing.description = description
            return key
        self.entities[key] = GraphEntity(
            name=name.strip(), category=category, description=description, source_chunk_ids={chunk_id}
        )
        return key


def build_knowledge_graph(
    chunks: list, llm, images: list = None, videos: list = None, n_schema_clusters: int = 8
) -> KnowledgeGraph:
    """Algorithm 1: LLM-powered KG construction pipeline (post-processing handled separately
    in `metalmind.postprocessing`).

    `videos` registers VideoAsset provenance nodes (Video -> refers_to -> Document, mirroring
    Figure). The text chunks generated from each video's description (see
    `metalmind.preprocessing.video_ingestion.describe_video`) must already be included in
    `chunks` by the caller, so they go through the same Phase 1/2 extraction as any other
    source text rather than being handled specially here.
    """
    kg = KnowledgeGraph()

    chunk_vectors = embeddings.embed_texts([c.text for c in chunks])
    for c, vec in zip(chunks, chunk_vectors):
        c.embedding = vec.tolist()
        kg.chunks[c.chunk_id] = c

    # --- Phase 1: schema-free entity extraction (lines 3-6) ---
    all_entities = []
    for chunk in tqdm(chunks, desc="Phase 1: schema-free extraction"):
        all_entities.extend(extraction.extract_entities_schema_free(llm, chunk))

    # --- Derive schema by clustering (line 7) ---
    categories = schema.derive_schema(llm, all_entities, n_clusters=n_schema_clusters)

    # --- Phase 2: populate KG using the derived schema (lines 9-14) ---
    for chunk in tqdm(chunks, desc="Phase 2: schema-based extraction"):
        chunk_entities = extraction.extract_entities_by_schema(llm, chunk, categories)
        for e in chunk_entities:
            kg.upsert_entity(e.name, e.category, e.description, chunk.chunk_id)
        for r in extraction.extract_relations(llm, chunk, chunk_entities):
            kg.relations.append(
                GraphRelation(head=r.head, relation=r.relation, tail=r.tail, source_chunk_id=chunk.chunk_id)
            )

    # --- Embed entities (lines 15-19) ---
    keys = list(kg.entities.keys())
    descs = [f"{kg.entities[k].name}: {kg.entities[k].description}" for k in keys]
    if descs:
        vectors = embeddings.embed_texts(descs)
        for k, vec in zip(keys, vectors):
            kg.entities[k].embedding = vec.tolist()

    # --- Image nodes (lines 20-26) ---
    for img in images or []:
        if img.caption:
            img.embedding = embeddings.embed_texts([img.caption])[0].tolist()
        kg.images[img.image_id] = img

    # --- Video nodes (provenance only; their description text was already extracted above) ---
    for video in videos or []:
        if video.description:
            video.embedding = embeddings.embed_texts([video.description])[0].tolist()
        kg.videos[video.video_id] = video

    return kg
