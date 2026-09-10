from metalmind.kg_construction.pipeline import GraphEntity, GraphRelation, KnowledgeGraph
from metalmind.postprocessing.cleanup import prune_standalone_entities


def test_prune_standalone_entities_removes_only_disconnected_nodes():
    kg = KnowledgeGraph()
    kg.entities["a"] = GraphEntity(name="A", category="Component", description="")
    kg.entities["b"] = GraphEntity(name="B", category="Component", description="")
    kg.entities["c"] = GraphEntity(name="C", category="Component", description="")  # standalone
    kg.relations.append(GraphRelation(head="A", relation="connects_to", tail="B", source_chunk_id="c0"))

    removed = prune_standalone_entities(kg)

    assert removed == ["c"]
    assert set(kg.entities) == {"a", "b"}
