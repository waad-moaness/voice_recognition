import numpy as np
import matplotlib.pyplot as plt 
import wave 
import librosa
import soundfile as sf 

raw_audio , sample_rate = librosa.load('audio_files/micrecording_output.wav')

audio_trimmed,_ = librosa.effects.trim(raw_audio, top_db=35)

sf.write('audio_files/micrecording_output_trimmed.wav', audio_trimmed, sample_rate)

plt.figure(figsize=(15,5))

plt.subplot(1,2,1)
plt.title('original audio')
plt.xlabel('time')
plt.ylabel('audio samples')
librosa.display.waveshow(raw_audio, sr=sample_rate)

plt.subplot(1,2,2)
plt.title('trimmed audio')
plt.xlabel('time')
plt.ylabel('audio samples')
librosa.display.waveshow(audio_trimmed, sr=sample_rate)

plt.tight_layout()
plt.show()







