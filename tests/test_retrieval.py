from metalmind import embeddings
from metalmind.retrieval.graph_retrieval import graph_search
from metalmind.retrieval.hybrid_retrieval import hybrid_search
from metalmind.retrieval.image_retrieval import (
    images_by_answer_similarity,
    images_for_retrieval,
    videos_for_retrieval,
)
from metalmind.retrieval.vector_retrieval import vector_search


class FakeClient:
    """Duck-typed stand-in for Neo4jClient exposing only the read methods retrieval uses."""

    def __init__(self, chunks=None, entities=None, edges=None, images=None, videos=None):
        self.chunks = chunks or []  # (chunk_id, text, embedding)
        self.entities = entities or []  # (name, description, embedding)
        self.edges = edges or {}  # name -> [(neighbor_name, neighbor_description)]
        self.images = images or []  # (url, caption, embedding, chunk_id)
        self.videos = videos or []  # (path, description, embedding, chunk_id)

    def all_document_chunks(self):
        return self.chunks

    def all_entities(self):
        return self.entities

    def neighbors(self, name, hops=1, limit=15):
        return self.edges.get(name, [])[:limit]

    def images_for_chunks(self, chunk_ids):
        return [(url, caption) for url, caption, _e, chunk_ids_ref in self.images if chunk_ids_ref in chunk_ids]

    def images_for_entities(self, entity_names):
        return []

    def all_images(self):
        return [(url, caption, emb) for url, caption, emb, _ref in self.images]

    def videos_for_chunks(self, chunk_ids):
        return [(path, desc) for path, desc, _e, chunk_ids_ref in self.videos if chunk_ids_ref in chunk_ids]

    def videos_for_entities(self, entity_names):
        return []


def _emb(text):
    return embeddings.embed_text(text).tolist()


def test_vector_search_returns_most_similar_chunk_first():
    client = FakeClient(
        chunks=[
            ("c0", "How to clean the wiper", _emb("How to clean the wiper")),
            ("c1", "Chiller coolant level check", _emb("Chiller coolant level check")),
        ]
    )
    result = vector_search(client, "How to clean the wiper", top_k=1)

    assert result.chunk_ids == ["c0"]
    assert result.context == ["How to clean the wiper"]


def test_graph_search_seeds_then_expands_neighbors():
    client = FakeClient(
        entities=[
            ("Recoater Blade", "Spreads powder.", _emb("Recoater Blade spreads powder.")),
            ("Chiller", "Cools optics.", _emb("Chiller cools optics.")),
        ],
        edges={"Recoater Blade": [("Build Plate", "Platform for the part.")]},
    )
    result = graph_search(client, "Recoater Blade spreads powder.", seed_k=1, hops=1)

    assert "Recoater Blade" in result.entity_names
    assert "Build Plate" in result.entity_names
    assert any("Build Plate" in c for c in result.context)


def test_hybrid_search_merges_vector_and_graph_context():
    client = FakeClient(
        chunks=[("c0", "Wiper cleaning needs 99% alcohol.", _emb("Wiper cleaning needs 99% alcohol."))],
        entities=[("Wiper", "Cleaning component.", _emb("Wiper cleaning component."))],
        edges={"Wiper": [("Alcohol", "Cleaning solvent.")]},
    )
    result = hybrid_search(client, "Wiper cleaning needs 99% alcohol.", top_k_chunks=1, seed_k=1, hops=1)

    assert result.chunk_ids == ["c0"]
    assert any("Wiper" in c for c in result.context)
    assert any("Alcohol" in c for c in result.context)


def test_images_for_retrieval_matches_by_chunk_id():
    from metalmind.retrieval.base import RetrievalResult

    client = FakeClient(images=[("http://img/1.png", "Wiper diagram", _emb("Wiper diagram"), "c0")])
    result = RetrievalResult(context=["..."], chunk_ids=["c0"], entity_names=[])

    hits = images_for_retrieval(client, result)
    assert hits == [("http://img/1.png", "Wiper diagram")]


def test_images_by_answer_similarity_respects_threshold():
    caption = "Diagram of the wiper cleaning procedure"
    client = FakeClient(images=[("http://img/1.png", caption, _emb(caption), "c0")])

    hits = images_by_answer_similarity(client, caption, threshold=0.99)
    assert hits == [("http://img/1.png", caption)]

    no_hits = images_by_answer_similarity(client, "totally unrelated text about the argon supply line", threshold=0.99)
    assert no_hits == []


def test_videos_for_retrieval_matches_by_chunk_id():
    from metalmind.retrieval.base import RetrievalResult

    client = FakeClient(
        videos=[("/videos/s1.mov", "Operator cleans the build plate.", _emb("cleans build plate"), "c0")]
    )
    result = RetrievalResult(context=["..."], chunk_ids=["c0"], entity_names=[])

    hits = videos_for_retrieval(client, result)
    assert hits == [("/videos/s1.mov", "Operator cleans the build plate.")]
