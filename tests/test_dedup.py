import pytest

from metalmind.kg_construction.pipeline import GraphEntity, GraphRelation, KnowledgeGraph
from metalmind.postprocessing.dedup import find_candidate_duplicates, merge_entities, name_token_overlap


def _kg_with_near_duplicates():
    kg = KnowledgeGraph()
    kg.entities["5 mm hex key"] = GraphEntity(
        name="5 Mm Hex Key", category="Component", description="A tool.", embedding=[1.0, 0.0]
    )
    kg.entities["5 mm hexagon key"] = GraphEntity(
        name="5 Mm Hexagon Key", category="Component", description="A tool.", embedding=[1.0, 0.0]
    )
    kg.entities["chiller"] = GraphEntity(
        name="Chiller", category="Component", description="Cooling unit.", embedding=[0.0, 1.0]
    )
    kg.relations.append(GraphRelation(head="5 Mm Hex Key", relation="used_on", tail="Chiller", source_chunk_id="c0"))
    return kg


def test_find_candidate_duplicates_flags_near_identical_embeddings():
    kg = _kg_with_near_duplicates()
    candidates = find_candidate_duplicates(kg, threshold=0.99)

    assert len(candidates) == 1
    assert {candidates[0]["a"], candidates[0]["b"]} == {"5 mm hex key", "5 mm hexagon key"}
    assert candidates[0]["similarity"] > 0.99
    # "5 Mm Hex Key" {5,mm,hex,key} vs "5 Mm Hexagon Key" {5,mm,hexagon,key} share 3 of 5
    # distinct tokens -- a real duplicate should carry a meaningful name_overlap alongside
    # its high embedding similarity.
    assert candidates[0]["name_overlap"] == pytest.approx(3 / 5)


def test_find_candidate_duplicates_respects_threshold():
    kg = _kg_with_near_duplicates()
    assert find_candidate_duplicates(kg, threshold=1.5) == []


def test_name_token_overlap_matches_paper_style_examples():
    # Real near-duplicate names from the paper's own Fig. 4b example share tokens even when
    # they don't match exactly -- this is the independent lexical signal surfaced alongside
    # embedding similarity for a human reviewer to weigh.
    assert name_token_overlap("Argon Supply Line", "Argon Gas Supply") == pytest.approx(2 / 4)
    assert name_token_overlap("Vacuum Cleaner", "Atex Vacuum Cleaner") == pytest.approx(2 / 3)
    assert name_token_overlap("Chiller", "Recoater Blade") == 0.0


def test_name_token_overlap_handles_empty_names():
    assert name_token_overlap("", "Chiller") == 0.0
    assert name_token_overlap("Chiller", "") == 0.0


def test_merge_entities_repoints_relations_and_drops_removed_key():
    kg = _kg_with_near_duplicates()
    merge_entities(kg, keep_key="5 mm hex key", remove_key="5 mm hexagon key")

    assert "5 mm hexagon key" not in kg.entities
    assert "5 mm hex key" in kg.entities
    assert all(r.head != "5 Mm Hexagon Key" and r.tail != "5 Mm Hexagon Key" for r in kg.relations)
