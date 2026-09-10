import base64

import pytest

from metalmind.preprocessing import video_ingestion


class FakeVisionLLM:
    def __init__(self, response_text="The operator removes the build plate and wipes it clean."):
        self._response_text = response_text
        self.calls = []
        self.total_tokens = 0

    def complete_vision(self, system, user_text, image_data_urls):
        self.calls.append({"system": system, "user_text": user_text, "image_data_urls": image_data_urls})
        return self._response_text, 42


def test_extract_frames_raises_without_ffmpeg(monkeypatch):
    monkeypatch.setattr(video_ingestion.shutil, "which", lambda name: None)
    with pytest.raises(RuntimeError, match="ffmpeg"):
        video_ingestion.extract_frames("nonexistent.mov")


def test_extract_frames_raises_for_missing_file(monkeypatch):
    monkeypatch.setattr(video_ingestion.shutil, "which", lambda name: "/usr/bin/ffmpeg")
    with pytest.raises(FileNotFoundError):
        video_ingestion.extract_frames("/definitely/not/a/real/video.mov")


def test_describe_video_builds_correct_data_urls_and_returns_llm_text(monkeypatch, tmp_path):
    fake_video = tmp_path / "s1_cleaning_build_plate.mov"
    fake_video.write_bytes(b"not a real video, just needs to exist")

    frames = [b"frame-one-bytes", b"frame-two-bytes"]
    monkeypatch.setattr(video_ingestion, "extract_frames", lambda path, max_frames=8: frames)

    llm = FakeVisionLLM()
    description = video_ingestion.describe_video(llm, fake_video, label="Cleaning the build plate")

    assert description == "The operator removes the build plate and wipes it clean."
    assert len(llm.calls) == 1
    call = llm.calls[0]
    assert "Cleaning the build plate" in call["user_text"]
    assert len(call["image_data_urls"]) == 2
    for raw_frame, data_url in zip(frames, call["image_data_urls"]):
        assert data_url == f"data:image/jpeg;base64,{base64.b64encode(raw_frame).decode()}"


def test_describe_video_raises_if_no_frames_extracted(monkeypatch, tmp_path):
    fake_video = tmp_path / "empty.mov"
    fake_video.write_bytes(b"x")
    monkeypatch.setattr(video_ingestion, "extract_frames", lambda path, max_frames=8: [])

    with pytest.raises(RuntimeError, match="No frames"):
        video_ingestion.describe_video(FakeVisionLLM(), fake_video)
