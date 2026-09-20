from ontology_kg.pipeline import build_ontology_graph


class FakeOntologyLLM:
    """Dispatches on which ontology_kg prompt was used, keyed on a distinctive substring, so
    the pipeline can be exercised offline (mirrors metalmind's tests/test_pipeline.py pattern)."""

    def __init__(self):
        self.total_tokens = 0

    def complete_json(self, system: str, user: str) -> dict:
        if "extracting a fixed ontology" in system:
            return self._parameters_and_properties_for(user)
        if 'extracting "Affects" relationships' in system:
            return self._affects_for(user)
        raise AssertionError(f"Unexpected system prompt: {system[:50]}")

    @staticmethod
    def _parameters_and_properties_for(user: str) -> dict:
        if "Laser power" in user:
            return {
                "parameters": [{"name": "Laser Power", "description": "Power of the fusing laser."}],
                "properties": [{"name": "Porosity", "description": "Void content in the finished part."}],
            }
        if "Layer height" in user:
            return {
                "parameters": [{"name": "Layer Height", "description": "Thickness of each deposited layer."}],
                "properties": [],
            }
        return {"parameters": [], "properties": []}

    @staticmethod
    def _affects_for(user: str) -> dict:
        if "Laser Power" in user and "Porosity" in user:
            return {"affects": [{"parameter": "Laser Power", "property": "Porosity"}]}
        return {"affects": []}


def _papers():
    return {
        "LPBF": [
            (
                "lpbf_paper1",
                "Laser power was varied to study its effect on Porosity in the fused part.",
            )
        ],
        "FFF": [("fff_paper1", "Layer height was set according to the nozzle diameter.")],
    }


def test_build_ontology_graph_extracts_parameters_properties_and_relations():
    graph = build_ontology_graph(_papers(), FakeOntologyLLM())

    param_names = {p.name for p in graph.parameters.values()}
    property_names = {p.name for p in graph.properties.values()}
    assert param_names == {"Laser Power", "Layer Height"}
    assert property_names == {"Porosity"}

    assert ("LPBF", "Laser Power") in graph.has_relations
    assert ("FFF", "Layer Height") in graph.has_relations
    assert len(graph.has_relations) == 2

    assert len(graph.affects_relations) == 1
    affects = graph.affects_relations[0]
    assert affects.parameter == "Laser Power"
    assert affects.part_property == "Porosity"


def test_build_ontology_graph_embeds_all_entities():
    graph = build_ontology_graph(_papers(), FakeOntologyLLM())

    assert all(p.embedding is not None for p in graph.parameters.values())
    assert all(p.embedding is not None for p in graph.properties.values())


def test_build_ontology_graph_rejects_unknown_process():
    import pytest

    with pytest.raises(ValueError, match="Unknown process"):
        build_ontology_graph({"FDM": [("p1", "text")]}, FakeOntologyLLM())


def test_upsert_parameter_merges_repeated_mentions_across_chunks():
    from ontology_kg.pipeline import OntologyGraph

    graph = OntologyGraph()
    graph.upsert_parameter("Laser Power", "short", "chunk0")
    graph.upsert_parameter("Laser Power", "a much longer, more detailed description", "chunk1")

    assert len(graph.parameters) == 1
    entity = graph.parameters["laser power"]
    assert entity.description == "a much longer, more detailed description"
    assert entity.source_chunk_ids == {"chunk0", "chunk1"}
