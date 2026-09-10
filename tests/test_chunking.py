import pytest

from metalmind.preprocessing.chunking import chunk_markdown


def test_chunk_markdown_single_chunk_for_short_text():
    chunks = chunk_markdown("doc1", "hello world", chunk_size=600, overlap=100)
    assert len(chunks) == 1
    assert chunks[0].chunk_id == "doc1::chunk0"
    assert chunks[0].doc_id == "doc1"
    assert chunks[0].order == 0


def test_chunk_markdown_overlaps_and_covers_all_tokens():
    text = " ".join(f"token{i}" for i in range(1500))
    chunks = chunk_markdown("doc1", text, chunk_size=600, overlap=100)

    assert len(chunks) > 1
    for i, chunk in enumerate(chunks):
        assert chunk.order == i
        assert chunk.chunk_id == f"doc1::chunk{i}"

    # last chunk's tail should reach the end of the source text
    assert "token1499" in chunks[-1].text


def test_chunk_markdown_empty_text_returns_no_chunks():
    assert chunk_markdown("doc1", "", chunk_size=600, overlap=100) == []


def test_chunk_markdown_rejects_overlap_ge_chunk_size():
    with pytest.raises(ValueError):
        chunk_markdown("doc1", "some text", chunk_size=100, overlap=100)
