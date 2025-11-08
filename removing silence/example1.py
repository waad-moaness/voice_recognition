import webrtcvad
import numpy as np
import soundfile as sf
import librosa

def frame_generator(y, sr, frame_duration=30):
    n = int(sr * frame_duration / 1000)
    offset = 0
    while offset + n < len(y):
        yield y[offset:offset+n]
        offset += n

def vad_filter(y, sr=16000, mode=2):
    vad = webrtcvad.Vad(mode)
    frames = list(frame_generator((y*32767).astype(np.int16), sr))
    speech = [f for f in frames if vad.is_speech(f.tobytes(), sr)]
    return np.concatenate(speech) / 32767.0


y_denoised , sr = librosa.load('audio_files/03-01-01-01-02-01-02.wav', mono=True, sr=16000)
y_vad = vad_filter(y_denoised, sr)
sf.write("removing silence/cleaned.wav", y_vad, sr)
