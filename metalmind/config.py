from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Settings:
    openai_api_key: str = os.environ.get("OPENAI_API_KEY", "")
    openai_model: str = os.environ.get("OPENAI_MODEL", "gpt-4o")

    neo4j_uri: str = os.environ.get("NEO4J_URI", "bolt://localhost:7687")
    neo4j_user: str = os.environ.get("NEO4J_USER", "neo4j")
    neo4j_password: str = os.environ.get("NEO4J_PASSWORD", "metalmind123")

    embedding_model: str = os.environ.get("EMBEDDING_MODEL", "all-MiniLM-L6-v2")

    chunk_size_tokens: int = int(os.environ.get("CHUNK_SIZE_TOKENS", "600"))
    chunk_overlap_tokens: int = int(os.environ.get("CHUNK_OVERLAP_TOKENS", "100"))

    duplicate_similarity_threshold: float = float(os.environ.get("DUP_SIM_THRESHOLD", "0.92"))
    image_similarity_threshold: float = float(os.environ.get("IMAGE_SIM_THRESHOLD", "0.85"))


settings = Settings()
