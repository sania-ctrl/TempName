"""Turn a source video (e.g. the paper's S1 "cleaning the build plate" / S2 "replacing the
filter" supplementary demos) into a text description that can flow through the same
entity/relation extraction pipeline as any Markdown document.

This is a text-only stand-in for the paper's actual video-based action-recognition model
(trained on synthetic Omniverse data -- out of scope here, see README). Instead of training a
model, we sample frames from the video and ask a vision-capable LLM to describe the operation
shown, then treat that description exactly like any other source text.

Requires the `ffmpeg`/`ffprobe` binaries on PATH (not a Python package -- install via your OS
package manager, e.g. `brew install ffmpeg` or `apt install ffmpeg`).
"""
import base64
import shutil
import subprocess
import tempfile
from pathlib import Path

DESCRIBE_VIDEO_SYSTEM = """You are a metal additive manufacturing (AM) process expert describing what an \
operator does in a short instructional video, based on a sequence of frames sampled evenly across it in \
chronological order. Write a clear, factual, step-by-step description of the operation shown: what components \
are touched, what actions are taken, and in what order. Ground your description ONLY in what is visibly shown \
in the frames; never invent steps you cannot see. If a step is ambiguous from the frames, say so rather than \
guessing.
"""


def _require_ffmpeg():
    if shutil.which("ffmpeg") is None or shutil.which("ffprobe") is None:
        raise RuntimeError(
            "ffmpeg and ffprobe are required to extract video frames but weren't found on PATH. "
            "Install ffmpeg (e.g. `brew install ffmpeg` or `apt install ffmpeg`) and try again."
        )


def _video_duration_seconds(video_path: Path) -> float:
    result = subprocess.run(
        [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(video_path),
        ],
        capture_output=True, text=True, check=True,
    )
    return float(result.stdout.strip())


def extract_frames(video_path, max_frames: int = 8) -> list:
    """Sample up to `max_frames` JPEG frames evenly across the video's duration. Returns a
    list of raw JPEG bytes, in chronological order."""
    _require_ffmpeg()
    video_path = Path(video_path)
    if not video_path.exists():
        raise FileNotFoundError(f"Video not found: {video_path}")

    duration = _video_duration_seconds(video_path)
    fps = max(max_frames / duration, 0.1) if duration > 0 else 1.0

    with tempfile.TemporaryDirectory() as tmp_dir:
        pattern = str(Path(tmp_dir) / "frame_%03d.jpg")
        subprocess.run(
            ["ffmpeg", "-y", "-i", str(video_path), "-vf", f"fps={fps}", "-vframes", str(max_frames), pattern],
            capture_output=True, check=True,
        )
        frame_paths = sorted(Path(tmp_dir).glob("frame_*.jpg"))
        return [p.read_bytes() for p in frame_paths]


def describe_video(llm, video_path, label: str = None, max_frames: int = 8) -> str:
    """Sample frames from `video_path` and ask the LLM to describe the operation shown.
    `label` is an optional human-readable title (e.g. "Cleaning the build plate") passed to
    the model as context."""
    frames = extract_frames(video_path, max_frames=max_frames)
    if not frames:
        raise RuntimeError(f"No frames could be extracted from {video_path}")

    data_urls = [f"data:image/jpeg;base64,{base64.b64encode(frame).decode()}" for frame in frames]
    label_line = f'Video title: "{label}"\n\n' if label else ""
    user_text = (
        f"{label_line}The following {len(frames)} frames are sampled evenly across the video's duration, "
        "in chronological order. Describe the metal AM operation shown."
    )
    description, _tokens = llm.complete_vision(DESCRIBE_VIDEO_SYSTEM, user_text, data_urls)
    return description
