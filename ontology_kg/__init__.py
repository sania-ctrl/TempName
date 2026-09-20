"""ontology_kg: a fixed-ontology, multi-process manufacturing knowledge graph.

Separate from `metalmind` (the Renishaw AM400 user-guide replication of the MetalMind paper):
where `metalmind` *derives* its schema dynamically per corpus via clustering (Algorithm 1),
this project applies one hand-designed, fixed ontology across four AM processes (FFF, SLA,
LPBF, Sintering), each backed by two academic papers, into a single combined graph:

    (:ManufacturingProcess)-[:HAS]->(:ProcessParameter)-[:AFFECTS]->(:PartProperty)

It reuses `metalmind`'s generic infrastructure (the OpenAI client wrapper, the
sentence-transformers embedding wrapper, and the token-based chunker) since those are
provider/utility code, not Renishaw- or Algorithm-1-specific -- but it has its own extraction
prompts, its own pipeline, and (deliberately) its own Neo4j database, configured via
`ontology_kg/config.py`.
"""
