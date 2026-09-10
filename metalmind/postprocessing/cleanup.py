def prune_standalone_entities(kg) -> list:
    """Remove entities with no relations to any other entity (paper §KG post-processing:
    "removing the standalone nodes"). Returns the list of removed entity keys."""
    connected = set()
    for r in kg.relations:
        connected.add(r.head.strip().lower())
        connected.add(r.tail.strip().lower())

    removed = [key for key in kg.entities if key not in connected]
    for key in removed:
        del kg.entities[key]
    return removed
