from audio_preprocessing.format_conversion import convert_to_wav
import subprocess

try:
    stdout, stderr = convert_to_wav("voice recordings /amira/WhatsApp Audio 2025-12-11 at 10.03.23 PM.ogg", "out.wav", timeout=30)
    print("Converted OK; ffmpeg stderr (warnings):", stderr)
except RuntimeError as e:
    print("Conversion failed:", e)
except subprocess.TimeoutExpired:
    print("ffmpeg timed out")