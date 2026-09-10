import ast
import re

from metalmind.kg_construction.pipeline import build_knowledge_graph
from metalmind.models import TextChunk, VideoAsset
from metalmind.postprocessing.cleanup import prune_standalone_entities
from metalmind.postprocessing.dedup import find_candidate_duplicates


class FakeLLM:
    """Deterministic stand-in for LLMClient: dispatches on which prompt template was used
    (matched by a distinctive substring of each prompts.py system message) instead of
    calling a real model, so the pipeline can be exercised offline."""

    def __init__(self):
        self.total_tokens = 0

    def complete_json(self, system: str, user: str) -> dict:
        if "Do not impose any predefined category system yet" in system:
            return {"entities": self._entities_for(user)}
        if "Propose a small set" in system:
            return {"categories": [{"name": "Component", "description": "physical parts"}]}
        if "Allowed categories:" in system:
            return {"entities": [dict(e, category="Component") for e in self._entities_for(user)]}
        if "extracting relationships between entities" in system:
            names = ast.literal_eval(re.search(r"Entities: (\[.*\])", user).group(1))
            if len(names) >= 2:
                return {"relations": [{"head": names[0], "relation": "part_of", "tail": names[1]}]}
            return {"relations": []}
        raise AssertionError(f"Unexpected system prompt: {system[:50]}")

    @staticmethod
    def _entities_for(user: str) -> list:
        if "Recoater Blade" in user:
            return [
                {"name": "Recoater Blade", "description": "Spreads powder across the build plate."},
                {"name": "Build Plate", "description": "Platform the part is built on."},
            ]
        if "Chiller" in user:
            return [{"name": "Chiller", "description": "Regulates laser optics temperature."}]
        if "Lonely Widget" in user:
            return [{"name": "Lonely Widget", "description": "Mentioned once, never related to anything."}]
        if "Cleaning Cloth" in user:
            return [{"name": "Cleaning Cloth", "description": "Used by the operator to wipe the build plate."}]
        return []


def _sample_chunks():
    return [
        TextChunk(chunk_id="doc::chunk0", doc_id="doc", text="Recoater Blade spreads powder on Build Plate.", order=0),
        TextChunk(chunk_id="doc::chunk1", doc_id="doc", text="Chiller cools the optics.", order=1),
        TextChunk(chunk_id="doc::chunk2", doc_id="doc", text="Lonely Widget sits unconnected.", order=2),
    ]


def test_build_knowledge_graph_extracts_entities_and_relations():
    kg = build_knowledge_graph(_sample_chunks(), FakeLLM())

    names = {e.name for e in kg.entities.values()}
    assert names == {"Recoater Blade", "Build Plate", "Chiller", "Lonely Widget"}
    assert len(kg.relations) == 1  # only the Recoater Blade / Build Plate chunk has 2+ entities
    assert all(e.embedding is not None for e in kg.entities.values())
    assert all(c.embedding is not None for c in kg.chunks.values())


def test_pipeline_output_survives_pruning_and_dedup():
    kg = build_knowledge_graph(_sample_chunks(), FakeLLM())

    removed = prune_standalone_entities(kg)
    assert set(removed) == {"chiller", "lonely widget"}

    candidates = find_candidate_duplicates(kg, threshold=1.1)  # impossible threshold
    assert candidates == []


def test_build_knowledge_graph_extracts_entities_from_video_description_chunks():
    # Mirrors how scripts/build_kg.py wires a video: describe_video() output is chunked and
    # appended to the normal chunk list, so it goes through the same extraction as any text.
    video_chunk = TextChunk(
        chunk_id="s1_cleaning_build_plate::chunk0",
        doc_id="s1_cleaning_build_plate",
        text="The operator wipes the build plate with a Cleaning Cloth before starting the next build.",
        order=0,
    )
    video = VideoAsset(
        video_id="s1_cleaning_build_plate",
        path="/videos/s1_cleaning_build_plate.mov",
        description=video_chunk.text,
        source_chunk_id=video_chunk.chunk_id,
    )

    kg = build_knowledge_graph([video_chunk], FakeLLM(), videos=[video])

    assert "Cleaning Cloth" in {e.name for e in kg.entities.values()}
    assert "s1_cleaning_build_plate" in kg.videos
    stored_video = kg.videos["s1_cleaning_build_plate"]
    assert stored_video.embedding is not None
    assert stored_video.source_chunk_id == video_chunk.chunk_id
