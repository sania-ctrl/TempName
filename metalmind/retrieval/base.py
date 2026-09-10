from dataclasses import dataclass, field


@dataclass
class RetrievalResult:
    """Uniform output of every retrieval mode: text passages to feed the LLM as context,
    plus the provenance (chunk ids / entity names) needed for image retrieval and eval."""

    context: list = field(default_factory=list)
    chunk_ids: list = field(default_factory=list)
    entity_names: list = field(default_factory=list)
