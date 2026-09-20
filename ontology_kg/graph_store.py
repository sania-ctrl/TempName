from .pipeline import OntologyGraph


def load_ontology_graph(client, graph: OntologyGraph) -> None:
    """Load an OntologyGraph into Neo4j using the fixed schema:
    (:ManufacturingProcess)-[:HAS]->(:ProcessParameter)-[:AFFECTS]->(:PartProperty), with
    :Document chunk provenance and :MENTIONED_IN edges mirroring metalmind's pattern.

    `client` is a `metalmind.graph_store.neo4j_client.Neo4jClient` -- reused as a thin,
    provider-agnostic Neo4j driver wrapper, but pointed at ontology_kg's own database
    (see ontology_kg/config.py) so this never touches metalmind's Renishaw graph.
    """
    with client._driver.session() as session:
        processes = {process for process, _ in graph.has_relations}
        for process in processes:
            session.run("MERGE (p:ManufacturingProcess {name: $name})", name=process)

        for chunk_id, chunk in graph.chunks.items():
            session.run(
                "MERGE (c:Document {chunk_id: $chunk_id}) "
                "SET c.doc_id = $doc_id, c.text = $text, c.order = $order",
                chunk_id=chunk_id,
                doc_id=chunk.doc_id,
                text=chunk.text,
                order=chunk.order,
            )

        for key, parameter in graph.parameters.items():
            session.run(
                "MERGE (n:ProcessParameter {key: $key}) "
                "SET n.name = $name, n.description = $description, n.embedding = $embedding",
                key=key,
                name=parameter.name,
                description=parameter.description,
                embedding=parameter.embedding,
            )
            for chunk_id in parameter.source_chunk_ids:
                if chunk_id not in graph.chunks:
                    continue
                session.run(
                    "MATCH (n:ProcessParameter {key: $key}), (c:Document {chunk_id: $chunk_id}) "
                    "MERGE (n)-[:MENTIONED_IN]->(c)",
                    key=key,
                    chunk_id=chunk_id,
                )

        for key, part_property in graph.properties.items():
            session.run(
                "MERGE (n:PartProperty {key: $key}) "
                "SET n.name = $name, n.description = $description, n.embedding = $embedding",
                key=key,
                name=part_property.name,
                description=part_property.description,
                embedding=part_property.embedding,
            )
            for chunk_id in part_property.source_chunk_ids:
                if chunk_id not in graph.chunks:
                    continue
                session.run(
                    "MATCH (n:PartProperty {key: $key}), (c:Document {chunk_id: $chunk_id}) "
                    "MERGE (n)-[:MENTIONED_IN]->(c)",
                    key=key,
                    chunk_id=chunk_id,
                )

        for process, parameter_name in graph.has_relations:
            session.run(
                "MATCH (p:ManufacturingProcess {name: $process}), (n:ProcessParameter {key: $key}) "
                "MERGE (p)-[:HAS]->(n)",
                process=process,
                key=OntologyGraph._key(parameter_name),
            )

        for relation in graph.affects_relations:
            session.run(
                "MATCH (a:ProcessParameter {key: $parameter_key}), (b:PartProperty {key: $property_key}) "
                "MERGE (a)-[r:AFFECTS]->(b) "
                "SET r.source_chunk_id = $chunk_id",
                parameter_key=OntologyGraph._key(relation.parameter),
                property_key=OntologyGraph._key(relation.part_property),
                chunk_id=relation.source_chunk_id,
            )
