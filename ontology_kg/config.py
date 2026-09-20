from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class OntologySettings:
    openai_api_key: str = os.environ.get("OPENAI_API_KEY", "")
    openai_model: str = os.environ.get("OPENAI_MODEL", "gpt-4o")
    embedding_model: str = os.environ.get("EMBEDDING_MODEL", "all-MiniLM-L6-v2")

    # Deliberately a separate Neo4j instance from metalmind's Renishaw graph (see
    # docker-compose.yml's neo4j-ontology service), so `--wipe` on one project never
    # touches the other's data.
    neo4j_uri: str = os.environ.get("ONTOLOGY_NEO4J_URI", "bolt://localhost:7688")
    neo4j_user: str = os.environ.get("ONTOLOGY_NEO4J_USER", "neo4j")
    neo4j_password: str = os.environ.get("ONTOLOGY_NEO4J_PASSWORD", "ontologykg123")

    chunk_size_tokens: int = int(os.environ.get("CHUNK_SIZE_TOKENS", "600"))
    chunk_overlap_tokens: int = int(os.environ.get("CHUNK_OVERLAP_TOKENS", "100"))


settings = OntologySettings()
