"""ontology_kg: a fixed-ontology, multi-process manufacturing knowledge graph.

Fully independent of `metalmind` (the Renishaw AM400 user-guide replication of the MetalMind
paper) -- no code in this package imports from `metalmind`, and it has its own Neo4j database.
Where `metalmind` *derives* its schema dynamically per corpus via clustering (Algorithm 1),
this project applies one hand-designed, fixed ontology across four AM processes (FFF, SLA,
LBM, Sintering), each backed by two academic papers, into a single combined graph:

    (:ManufacturingProcess)-[:HAS]->(:ProcessParameter)-[:AFFECTS]->(:PartProperty)

Its own OpenAI client wrapper (`llm_client.py`), embedding wrapper (`embeddings.py`), chunker
(`chunking.py`), and Neo4j driver wrapper (`neo4j_client.py`) are separate implementations from
metalmind's -- not shared, even though the logic is similar -- so this project stands on its
own. Configuration lives in `ontology_kg/config.py`.
"""
