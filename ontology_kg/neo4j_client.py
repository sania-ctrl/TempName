"""Minimal Neo4j driver wrapper local to ontology_kg -- deliberately not shared with metalmind,
so this project has no code dependency on the Renishaw/metalmind work (it already had its own
database; now it has its own driver wrapper too).
"""
from .config import settings


class Neo4jClient:
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
