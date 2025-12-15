import shutil
import subprocess
from pathlib import Path
from typing import Tuple

def ensure_ffmpeg_available():
    if shutil.which("ffmpeg") is None:
        raise RuntimeError("ffmpeg not found on PATH. Install it in the container.")

def convert_to_wav(in_path: str, out_path: str, timeout: int = 60) -> Tuple[str, str]:
    ensure_ffmpeg_available()
    in_path = str(Path(in_path))
    out_path = str(Path(out_path))
    cmd = [
        "ffmpeg", "-y",
        "-nostdin",
        "-v", "warning",           # reduce ffmpeg verbosity in normal runs
        "-i", in_path,
        "-ar", "16000",            # sample rate
        "-ac", "1",                # mono
        "-sample_fmt", "s16",      # 16-bit PCM
        out_path
    ]
    proc = subprocess.run(cmd, capture_output=True, text=True, check=False, timeout=timeout)
    if proc.returncode != 0:
        # include stderr in your logs/metrics for diagnostics
        raise RuntimeError(f"ffmpeg failed (rc={proc.returncode}): {proc.stderr.strip()}")
    return proc.stdout, proc.stderr