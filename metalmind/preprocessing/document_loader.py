from pathlib import Path


def load_markdown_docs(doc_dir) -> dict:
    """Load every `.md` file in `doc_dir`. Each file becomes one document (central node),
    keyed by its filename stem (paper §Preprocessing: "each Markdown file corresponds to
    a central node")."""
    docs = {}
    for path in sorted(Path(doc_dir).glob("*.md")):
        docs[path.stem] = path.read_text(encoding="utf-8")
    return docs
