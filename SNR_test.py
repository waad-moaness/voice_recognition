import numpy as np
import soundfile as sf

def estimate_snr(wav_path, silence_threshold_db=-40):
    audio, sr = sf.read(wav_path)

    if audio.ndim > 1:
        audio = audio.mean(axis=1)

    # Frame parameters
    frame_size = int(0.02 * sr)   # 20 ms
    hop_size = frame_size

    rms_values = []
    for i in range(0, len(audio) - frame_size, hop_size):
        frame = audio[i:i+frame_size]
        rms = np.sqrt(np.mean(frame**2) + 1e-10)
        rms_db = 20 * np.log10(rms + 1e-10)
        rms_values.append(rms_db)

    rms_values = np.array(rms_values)

    # Silence frames
    silence_frames = rms_values < silence_threshold_db
    speech_frames = rms_values >= silence_threshold_db

    if silence_frames.sum() < 5 or speech_frames.sum() < 5:
        return None  # Not enough data

    noise_level = np.mean(rms_values[silence_frames])
    speech_level = np.mean(rms_values[speech_frames])

    snr = speech_level - noise_level
    return snr


def denoise_decision(snr):
    if snr is None:
        denoise = False
    elif snr < 20:
        denoise = True
    else:
        denoise = False
    return denoise
# import glob
# test_audio = glob.glob("final_test_audios/*.wav")
# for i in test_audio :
#     snr = estimate_snr(i)
#     denoise = denoise_decision(snr)
#     print(f"SNR: {snr} dB, Denoise: {denoise}")

snr = estimate_snr("audio_files/Standard recording 4.wav")
denoise = denoise_decision(snr)
print(f"SNR: {snr} dB, Denoise: {denoise}")