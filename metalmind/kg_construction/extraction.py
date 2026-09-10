from dataclasses import dataclass
from typing import Optional

from ..models import TextChunk
from . import prompts


@dataclass
class RawEntity:
    name: str
    description: str
    category: Optional[str] = None


@dataclass
class RawRelation:
    head: str
    relation: str
    tail: str


def extract_entities_schema_free(llm, chunk: TextChunk) -> list:
    """Algorithm 1, Phase 1 (line 4): schema-free entity extraction for one chunk."""
    result = llm.complete_json(prompts.SCHEMA_FREE_EXTRACTION_SYSTEM, chunk.text)
    entities = []
    for e in result.get("entities", []):
        name = (e.get("name") or "").strip()
        if not name:
            continue
        entities.append(RawEntity(name=name, description=e.get("description", "")))
    return entities


def extract_entities_by_schema(llm, chunk: TextChunk, categories: list) -> list:
    """Algorithm 1, Phase 2 (line 10): schema-based entity extraction for one chunk."""
    system = prompts.SCHEMA_BASED_EXTRACTION_SYSTEM_TEMPLATE.format(
        categories="\n".join(f"- {c}" for c in categories)
    )
    result = llm.complete_json(system, chunk.text)
    entities = []
    for e in result.get("entities", []):
        name = (e.get("name") or "").strip()
        category = e.get("category")
        if not name or category not in categories:
            continue
        entities.append(RawEntity(name=name, description=e.get("description", ""), category=category))
    return entities


def extract_relations(llm, chunk: TextChunk, entities: list) -> list:
    """Algorithm 1, Phase 2 (line 11): relation extraction between entities found in one chunk."""
    if len(entities) < 2:
        return []
    entity_names = [e.name for e in entities]
    user = f"Text:\n{chunk.text}\n\nEntities: {entity_names}"
    result = llm.complete_json(prompts.RELATION_EXTRACTION_SYSTEM, user)
    valid_names = set(entity_names)
    relations = []
    for r in result.get("relations", []):
        head, tail = r.get("head"), r.get("tail")
        if head in valid_names and tail in valid_names and head != tail:
            relations.append(RawRelation(head=head, relation=r.get("relation") or "related_to", tail=tail))
    return relations
