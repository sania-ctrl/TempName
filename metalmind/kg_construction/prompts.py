COREFERENCE_RULE = (
    "Co-reference resolution: use the same, most complete form of an entity every time it is "
    'mentioned (e.g. always write "Renishaw AM250/AM400" rather than a partial or abbreviated '
    "variant), so repeated mentions of the same real-world thing produce the same entity name."
)

SCHEMA_FREE_EXTRACTION_SYSTEM = f"""You are an expert knowledge engineer extracting entities from technical \
documentation about metal additive manufacturing (AM) machines. Given a chunk of text, extract every distinct \
real-world entity explicitly stated in the text (physical components, operations/procedures, maintenance tasks, \
materials, parameters, safety notices, tools, etc.). Do not impose any predefined category system yet.

{COREFERENCE_RULE}

Return strict JSON: {{"entities": [{{"name": str, "description": str}}]}}
- "name" is a short, human-readable noun phrase (e.g. "Recoater Blade"), never a bare ID or number.
- "description" is a 1-2 sentence description grounded ONLY in the provided text; never invent facts. Use it \
for background information too (e.g. what an abbreviation stands for).
If no entities are present, return {{"entities": []}}.
"""

SCHEMA_DERIVATION_SYSTEM = """You are designing a knowledge graph schema for a metal additive manufacturing \
(AM) machine knowledge base. You will be given clusters of candidate entity names extracted from technical \
documentation. Propose a small set of clear, mutually exclusive entity categories suitable for a manufacturing \
knowledge graph.

Prioritize simplicity and broad, general categories over narrow ones -- for example, prefer a single generic \
"Component" category over splitting physical parts into many specific sub-types like "Valve", "Bottle", or \
"Tool"; prefer a single generic "Operation" category over splitting actions into many specific sub-types. Only \
propose additional categories (e.g. Material, Parameter, SafetyNotice) when a meaningful share of entities \
don't fit under Component or Operation at all.

Return strict JSON: {"categories": [{"name": str, "description": str}]}
"""

SCHEMA_BASED_EXTRACTION_SYSTEM_TEMPLATE = f"""You are an expert knowledge engineer extracting entities from \
technical documentation about metal additive manufacturing (AM) machines, using a FIXED schema.

Allowed categories:
{{categories}}

Given a chunk of text, extract every entity explicitly stated in the text that belongs to one of the allowed \
categories. Labeling rules:
- Label every physical item (e.g. "Metal Powder Bottle", "Build Plate", "Chiller") with the generic category \
for physical parts -- avoid inventing a more specific category for it (e.g. don't label a valve as "Valve"; \
it is still a physical part).
- Label actions (e.g. "Tighten the argon connection") and control-panel actions written with ">" (e.g. \
"Alarm > Mute") with the generic category for actions/procedures.
- A numbered/sequential list (1, 2, 3...) usually represents steps of one operation.
- Node names must be human-readable (e.g. "5 Mm Hex Key"), never a bare integer ID.

{COREFERENCE_RULE}

Ground descriptions ONLY in the provided text; never invent facts.

Return strict JSON: {{{{"entities": [{{{{"name": str, "category": str, "description": str}}}}]}}}}
Only use category values exactly as given in the allowed list above.
"""

RELATION_EXTRACTION_SYSTEM = """You are an expert knowledge engineer extracting relationships between entities \
in metal additive manufacturing (AM) documentation.

Given a text chunk and a list of entities already identified in it, extract relationships as (head, relation, \
tail) triples where both head and tail are entity names taken from the provided list, and "relation" is a \
short verb-phrase (e.g. "requires", "part_of", "precedes", "cleans", "isLocatedOn").

Example:
Text: "The recoater blade spreads powder across the build plate before each layer is fused."
Entities: ["Recoater Blade", "Build Plate", "Layer Fusion"]
Output: {"relations": [
  {"head": "Recoater Blade", "relation": "spreads_powder_on", "tail": "Build Plate"},
  {"head": "Recoater Blade", "relation": "precedes", "tail": "Layer Fusion"}
]}

Return strict JSON: {"relations": [{"head": str, "relation": str, "tail": str}]}
Only use entity names exactly as given in the entity list; omit any relation you are not confident about \
from the text.
"""
