from dataclasses import dataclass, field
from typing import Optional

from tqdm import tqdm

from . import embeddings, extraction
from .chunking import chunk_text

PROCESS_TYPES = ("FFF", "SLA", "LPBF", "Sintering")


@dataclass
class OntologyEntity:
    name: str
    description: str
    source_chunk_ids: set = field(default_factory=set)
    embedding: Optional[list] = None


@dataclass
class AffectsRelation:
    parameter: str
    part_property: str
    source_chunk_id: str


@dataclass
class OntologyGraph:
    parameters: dict = field(default_factory=dict)  # normalized name -> OntologyEntity
    properties: dict = field(default_factory=dict)  # normalized name -> OntologyEntity
    has_relations: set = field(default_factory=set)  # {(process, parameter_name)}
    affects_relations: list = field(default_factory=list)
    chunks: dict = field(default_factory=dict)  # chunk_id -> TextChunk

    @staticmethod
    def _key(name: str) -> str:
        return name.strip().lower()

    def upsert_parameter(self, name: str, description: str, chunk_id: str) -> str:
        key = self._key(name)
        existing = self.parameters.get(key)
        if existing:
            existing.source_chunk_ids.add(chunk_id)
            if len(description) > len(existing.description):
                existing.description = description
            return key
        self.parameters[key] = OntologyEntity(name=name.strip(), description=description, source_chunk_ids={chunk_id})
        return key

    def upsert_property(self, name: str, description: str, chunk_id: str) -> str:
        key = self._key(name)
        existing = self.properties.get(key)
        if existing:
            existing.source_chunk_ids.add(chunk_id)
            if len(description) > len(existing.description):
                existing.description = description
            return key
        self.properties[key] = OntologyEntity(name=name.strip(), description=description, source_chunk_ids={chunk_id})
        return key


def build_ontology_graph(
    papers_by_process: dict, llm, chunk_size: int = 600, chunk_overlap: int = 100
) -> OntologyGraph:
    """Build one combined graph across every process in `papers_by_process`, using the fixed
    ontology: (:ManufacturingProcess)-[:HAS]->(:ProcessParameter)-[:AFFECTS]->(:PartProperty).

    `papers_by_process` maps a process name (one of PROCESS_TYPES) to a list of
    `(paper_id, text)` tuples -- one entry per source paper, already loaded as plain/Markdown
    text. Unlike metalmind's Algorithm 1, there is no schema-derivation phase: the three
    classes are fixed, so extraction is a single pass per chunk.
    """
    graph = OntologyGraph()

    for process, papers in papers_by_process.items():
        if process not in PROCESS_TYPES:
            raise ValueError(f"Unknown process '{process}'; expected one of {PROCESS_TYPES}")

        for paper_id, text in papers:
            chunks = chunk_text(paper_id, text, chunk_size, chunk_overlap)
            for chunk in chunks:
                graph.chunks[chunk.chunk_id] = chunk

            for chunk in tqdm(chunks, desc=f"{process} / {paper_id}"):
                raw_parameters, raw_properties = extraction.extract_parameters_and_properties(llm, chunk, process)

                for p in raw_parameters:
                    key = graph.upsert_parameter(p.name, p.description, chunk.chunk_id)
                    graph.has_relations.add((process, graph.parameters[key].name))
                for p in raw_properties:
                    graph.upsert_property(p.name, p.description, chunk.chunk_id)

                for a in extraction.extract_affects(llm, chunk, raw_parameters, raw_properties):
                    graph.affects_relations.append(
                        AffectsRelation(parameter=a.parameter, part_property=a.part_property, source_chunk_id=chunk.chunk_id)
                    )

    _embed_entities(graph.parameters)
    _embed_entities(graph.properties)

    return graph


def _embed_entities(entities: dict) -> None:
    keys = list(entities.keys())
    if not keys:
        return
    descriptions = [f"{entities[k].name}: {entities[k].description}" for k in keys]
    vectors = embeddings.embed_texts(descriptions)
    for key, vector in zip(keys, vectors):
        entities[key].embedding = vector.tolist()
