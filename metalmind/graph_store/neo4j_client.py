import re

from ..config import settings


def _sanitize_label(label: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_]", "", label or "")
    return cleaned or "Entity"


class Neo4jClient:
    """Wrapper around the Neo4j driver: loads a `KnowledgeGraph` and exposes the read
    queries used by the retrieval modes (vector / graph / hybrid)."""

    def __init__(self, uri: str = None, user: str = None, password: str = None):
        from neo4j import GraphDatabase

        self._driver = GraphDatabase.driver(
            uri or settings.neo4j_uri, auth=(user or settings.neo4j_user, password or settings.neo4j_password)
        )

    def close(self):
        self._driver.close()

    def wipe(self):
        with self._driver.session() as session:
            session.run("MATCH (n) DETACH DELETE n")

    def load_knowledge_graph(self, kg):
        with self._driver.session() as session:
            for chunk_id, chunk in kg.chunks.items():
                session.run(
                    "MERGE (c:Document {chunk_id: $chunk_id}) "
                    "SET c.doc_id = $doc_id, c.text = $text, c.order = $order, c.embedding = $embedding",
                    chunk_id=chunk_id,
                    doc_id=chunk.doc_id,
                    text=chunk.text,
                    order=chunk.order,
                    embedding=chunk.embedding,
                )

            for key, entity in kg.entities.items():
                label = _sanitize_label(entity.category)
                session.run(
                    f"MERGE (n:Entity:`{label}` {{key: $key}}) "
                    "SET n.name = $name, n.category = $category, n.description = $description, "
                    "n.embedding = $embedding",
                    key=key,
                    name=entity.name,
                    category=entity.category,
                    description=entity.description,
                    embedding=entity.embedding,
                )
                for chunk_id in entity.source_chunk_ids:
                    if chunk_id not in kg.chunks:
                        continue
                    session.run(
                        "MATCH (n:Entity {key: $key}), (c:Document {chunk_id: $chunk_id}) "
                        "MERGE (n)-[:MENTIONED_IN]->(c)",
                        key=key,
                        chunk_id=chunk_id,
                    )

            for relation in kg.relations:
                session.run(
                    "MATCH (h:Entity {name: $head}), (t:Entity {name: $tail}) "
                    "MERGE (h)-[rel:RELATION {type: $rel_type}]->(t) "
                    "SET rel.source_chunk_id = $chunk_id",
                    head=relation.head,
                    tail=relation.tail,
                    rel_type=relation.relation,
                    chunk_id=relation.source_chunk_id,
                )

            for image_id, image in kg.images.items():
                session.run(
                    "MERGE (i:Figure {image_id: $image_id}) "
                    "SET i.url = $url, i.caption = $caption, i.embedding = $embedding "
                    "WITH i "
                    "MATCH (c:Document {chunk_id: $chunk_id}) "
                    "MERGE (i)-[:refers_to]->(c)",
                    image_id=image_id,
                    url=image.url,
                    caption=image.caption,
                    embedding=image.embedding,
                    chunk_id=image.source_chunk_id,
                )

    def all_document_chunks(self):
        with self._driver.session() as session:
            result = session.run(
                "MATCH (c:Document) WHERE c.embedding IS NOT NULL "
                "RETURN c.chunk_id AS chunk_id, c.text AS text, c.embedding AS embedding"
            )
            return [(r["chunk_id"], r["text"], r["embedding"]) for r in result]

    def all_entities(self):
        with self._driver.session() as session:
            result = session.run(
                "MATCH (n:Entity) WHERE n.embedding IS NOT NULL "
                "RETURN n.name AS name, n.description AS description, n.embedding AS embedding"
            )
            return [(r["name"], r["description"], r["embedding"]) for r in result]

    def neighbors(self, entity_name: str, hops: int = 1, limit: int = 15):
        with self._driver.session() as session:
            result = session.run(
                f"MATCH (n:Entity {{name: $name}})-[:RELATION*1..{hops}]-(m:Entity) "
                "RETURN DISTINCT m.name AS name, m.description AS description LIMIT $limit",
                name=entity_name,
                limit=limit,
            )
            return [(r["name"], r["description"]) for r in result]

    def images_for_entities(self, entity_names: list):
        if not entity_names:
            return []
        with self._driver.session() as session:
            result = session.run(
                "MATCH (n:Entity)-[:MENTIONED_IN]->(c:Document)<-[:refers_to]-(i:Figure) "
                "WHERE n.name IN $names "
                "RETURN DISTINCT i.url AS url, i.caption AS caption",
                names=entity_names,
            )
            return [(r["url"], r["caption"]) for r in result]

    def images_for_chunks(self, chunk_ids: list):
        if not chunk_ids:
            return []
        with self._driver.session() as session:
            result = session.run(
                "MATCH (i:Figure)-[:refers_to]->(c:Document) WHERE c.chunk_id IN $ids "
                "RETURN DISTINCT i.url AS url, i.caption AS caption",
                ids=chunk_ids,
            )
            return [(r["url"], r["caption"]) for r in result]

    def all_images(self):
        with self._driver.session() as session:
            result = session.run(
                "MATCH (i:Figure) WHERE i.embedding IS NOT NULL "
                "RETURN i.url AS url, i.caption AS caption, i.embedding AS embedding"
            )
            return [(r["url"], r["caption"], r["embedding"]) for r in result]
