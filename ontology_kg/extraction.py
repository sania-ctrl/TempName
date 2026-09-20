from dataclasses import dataclass

from . import prompts


@dataclass
class RawParameter:
    name: str
    description: str


@dataclass
class RawProperty:
    name: str
    description: str


@dataclass
class RawAffects:
    parameter: str
    part_property: str


def extract_parameters_and_properties(llm, chunk, process: str) -> tuple:
    """Single-pass extraction against the fixed ontology (no schema-derivation phase, unlike
    metalmind's Algorithm 1 -- the classes are hand-designed and constant across every paper)."""
    system = prompts.PARAMETER_PROPERTY_EXTRACTION_SYSTEM_TEMPLATE.format(process=process)
    result = llm.complete_json(system, chunk.text)

    parameters = [
        RawParameter(name=p["name"].strip(), description=p.get("description", ""))
        for p in result.get("parameters", [])
        if p.get("name")
    ]
    properties = [
        RawProperty(name=p["name"].strip(), description=p.get("description", ""))
        for p in result.get("properties", [])
        if p.get("name")
    ]
    return parameters, properties


def extract_affects(llm, chunk, parameters: list, properties: list) -> list:
    if not parameters or not properties:
        return []

    parameter_names = [p.name for p in parameters]
    property_names = [p.name for p in properties]
    user = (
        f"Text:\n{chunk.text}\n\n"
        f"Process parameters identified: {parameter_names}\n"
        f"Part properties identified: {property_names}"
    )
    result = llm.complete_json(prompts.AFFECTS_EXTRACTION_SYSTEM, user)

    valid_parameters, valid_properties = set(parameter_names), set(property_names)
    affects = []
    for a in result.get("affects", []):
        parameter, part_property = a.get("parameter"), a.get("property")
        if parameter in valid_parameters and part_property in valid_properties:
            affects.append(RawAffects(parameter=parameter, part_property=part_property))
    return affects
