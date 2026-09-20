PARAMETER_PROPERTY_EXTRACTION_SYSTEM_TEMPLATE = """You are extracting a fixed ontology from an academic paper \
about metal additive manufacturing. The ontology has exactly three classes:

- ManufacturingProcess: the specific AM process this paper is about (given to you below, not extracted)
- ProcessParameter: a controllable input/setting of the process explicitly discussed in the text (e.g. layer \
thickness, laser power, print speed, sintering temperature, scan strategy)
- PartProperty: a resulting property of the manufactured part explicitly discussed in the text (e.g. tensile \
strength, surface roughness, porosity, dimensional accuracy, density)

This paper is about the "{process}" process. Given a chunk of text from it, extract every ProcessParameter and \
every PartProperty explicitly mentioned. Ground descriptions ONLY in the provided text; never invent facts.

Return strict JSON:
{{"parameters": [{{"name": str, "description": str}}], "properties": [{{"name": str, "description": str}}]}}
If none are present, return empty lists.
"""

AFFECTS_EXTRACTION_SYSTEM = """You are extracting "Affects" relationships from an academic paper about metal \
additive manufacturing. Given a text chunk and lists of process-parameter and part-property names already \
identified in it, extract every (parameter, property) pair where the text explicitly states that changing the \
parameter affects the property (e.g. "increasing laser power reduces porosity" -> parameter "Laser Power" \
affects property "Porosity").

Return strict JSON: {"affects": [{"parameter": str, "property": str}]}
Only use names exactly as given in the provided lists; omit any relationship you are not confident about from \
the text.
"""
