# MetalMind (implementation)

An implementation of the KG-construction pipeline and multi-faceted (vector / graph / hybrid)
retrieval-and-evaluation system described in *"MetalMind: A knowledge graph-driven human-centric
knowledge system for metal additive manufacturing"* (Fan et al., npj Advanced Manufacturing, 2025).

## Scope

This repo implements:

- **Automated KG construction** (`metalmind/kg_construction`, `metalmind/preprocessing`): Markdown
  ingestion, 600-token/100-overlap chunking, LLM-powered schema-free → schema-derivation →
  schema-based extraction (Algorithm 1 in the paper), entity/chunk embeddings, and image nodes.
- **Post-processing** (`metalmind/postprocessing`): standalone-node pruning and
  embedding-similarity duplicate detection, producing a review queue for the paper's
  collaborative accept/reject step (`scripts/apply_dedup.py` applies the decisions).
- **Multi-faceted RAG** (`metalmind/retrieval`, `metalmind/rag`): vector-based, graph-traversal, and
  hybrid retrieval modes over a Neo4j-backed KG, plus text→image and text→video retrieval.
- **Video ingestion** (`metalmind/preprocessing/video_ingestion.py`): a text-only stand-in for the
  paper's video-based action-recognition model. Frame-samples a source video, asks GPT-4o to
  describe the operation shown, then feeds that description through the normal chunking +
  entity/relation extraction pipeline like any other document — see "Adding the supplementary
  videos" below.
- **Evaluation harness** (`metalmind/evaluation`): faithfulness, answer relevancy, context
  precision/recall (RAGAS-style, LLM-judged), domain rubric scoring, and the paper's 70/30
  accuracy-vs-token-efficiency composite score.

**Not implemented** (out of scope for a code repo — needs dedicated hardware/licensed SDKs):
the MR headset interface, the Omniverse-trained action-recognition model itself (we substitute a
frame-sampling + vision-LLM description, not a trained recognizer), and the web UI for
collaborative node review (its underlying dedup logic is implemented and scriptable).

## Setup

```bash
cp .env.example .env        # fill in OPENAI_API_KEY at minimum
docker compose up -d        # starts Neo4j (bolt://localhost:7687, browser at :7474)

python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
```

## Usage

**1. Build the knowledge graph** from a directory of Markdown documents (see
`data/sample_docs/` for a tiny worked example standing in for the paper's Renishaw AM400 user
guide):

```bash
python -m scripts.build_kg --docs data/sample_docs --wipe
```

This runs Algorithm 1 end-to-end, prunes standalone nodes, writes candidate duplicate pairs to
`dedup_candidates.json` for review, and loads the resulting graph into Neo4j.

To also load images, pass `--images manifest.json` where the manifest maps
`{"image_id": {"url": ..., "caption": ..., "source_chunk_id": ...}}`.

**Adding the supplementary videos** (S1 "cleaning the build plate", S2 "replacing the filter"):
requires the `ffmpeg`/`ffprobe` binaries on PATH (`brew install ffmpeg` / `apt install ffmpeg` /
Windows: download from ffmpeg.org and add to PATH — not a pip package). Download the `.mov`
files from the paper's supplementary information page, then pass `--videos manifest.json` where
the manifest maps `{"video_id": {"path": "/local/path/to/s1.mov", "label": "Cleaning the build
plate"}}`. Each video is frame-sampled, described by GPT-4o vision, and that description is
chunked and extracted exactly like a Markdown document — so entities like "Cleaning Cloth" or
operations shown in the demo become real KG nodes, not just an attached caption. A `Video`
node is also added (mirroring `Figure`) so you can trace which entities/passages came from
which video. `scripts/ask.py --videos` surfaces linked videos alongside an answer, the same way
`--images` does.

**2. Review and apply duplicate merges** (the paper's collaborative verification step):

review `dedup_candidates.json`, write your accept/reject decisions as
`[{"a": "<key to keep>", "b": "<key to remove>", "merge": true}, ...]`, then:

```bash
python -m scripts.apply_dedup --decisions decisions.json
```

**3. Evaluate retrieval modes** against a query/ground-truth dataset. `data/eval_dataset.json` is
now the paper's actual 100-question evaluation set (pulled from the authors' repo,
[FHL1998/MetalMind](https://github.com/FHL1998/MetalMind), and verified against the exact example
questions quoted in the paper's supplementary information). The authors don't publish a
granular/global label per question, so only the 4 questions the supplement names by exact text are
tagged (`"granular"` / `"global"`); the rest are `"unlabeled"`. Re-run
`python -m scripts.fetch_eval_dataset` any time to refresh it from the source, or hand-label more
questions yourself if you want the full 70/30 breakdown from Fig. 2:

```bash
python -m scripts.evaluate --dataset data/eval_dataset.json
```

Prints the per-mode/per-metric table (mirroring Fig. 2) and the composite token-efficiency scores
(mirroring Table 1), grouped by whatever `type` values are present in the dataset.

## Tests

```bash
pytest
```

All tests run offline: `tests/conftest.py` mocks the sentence-transformers embedding model and
tiktoken's encoding so no network access or GPU is required to validate the pipeline logic
(chunking, extraction/relation wiring, dedup, pruning, retrieval, metrics, composite scoring).

## Architecture notes

- Entities are deduplicated across chunks by normalized name at construction time; the
  embedding-similarity dedup pass in `postprocessing/dedup.py` then catches near-duplicate
  *different* names (e.g. "5 Mm Hex Key" vs "5 Mm Hexagon Key", as in the paper's Fig. 4).
- The graph store adds `MENTIONED_IN` edges from entities to the chunks they were extracted
  from (in addition to the paper's `RELATION` edges between entities and `refers_to` edges from
  images to chunks), so graph retrieval can traverse from a query to relevant entities to their
  source passages, and so image retrieval can walk from either retrieved chunks or retrieved
  entities to linked figures. `Video` nodes follow the same `refers_to` pattern as `Figure`.
- The LLM and embedding clients are swappable via `.env` (`OPENAI_MODEL`, `EMBEDDING_MODEL`);
  swap `metalmind/llm/client.py` for a different provider's SDK if needed.
- `kg_construction/prompts.py` encodes the paper's actual published extraction rules (from its
  supplementary "Knowledge Graph Construction Guidelines for GPT-4o"): generic `Component`
  labels rather than specific ones (e.g. never "Valve"), `>` syntax for control-panel actions,
  numbered lists as operation steps, human-readable node names, and co-reference resolution to
  the most complete entity form. The category *set* itself is still derived dynamically per
  corpus via clustering (Algorithm 1), matching the paper's method rather than hardcoding its
  two dominant categories (Component, Operation).
