import subprocess
import os

def rnnoise_denoise(input_wav: str, output_wav: str):
    # Check if input exists
    if not os.path.exists(input_wav):
        raise FileNotFoundError(f"Input file not found: {input_wav}")

    # Ensure output directory exists, or ffmpeg will fail
    output_dir = os.path.dirname(output_wav)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # We use 'ffmpeg' with the 'arnndn' filter instead of 'rnnoise_demo'
    command = [
        "ffmpeg",
        "-y",               # Overwrite output without asking
        "-i", input_wav,    # Input file
        "-af", "arnndn",    # The RNNoise filter
        output_wav          # Output file
    ]

    # Run the command
    try:
        subprocess.run(
            command,
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        print(f"Successfully created: {output_wav}")
    except subprocess.CalledProcessError as e:
        print(f"Error processing audio: {e}")

# Run it
rnnoise_denoise(
    "final_test_audios/audio1.wav",
    "denoised_audio/audio1_denoised.wav"
)