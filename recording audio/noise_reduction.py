import librosa 
import numpy as np
import matplotlib.pyplot as plt 
import scipy.fftpack as fft
from scipy.signal import medfilt
import soundfile as sf 

raw_audio , sample_rate = librosa.load('audio_files/micrecording_output.wav')

s_full , phase = librosa.magphase(librosa.stft(raw_audio))

noise_power = np.mean(s_full[:, :int(sample_rate*0.1) ], axis=1)

mask = s_full > noise_power[:, None]

mask = mask.astype(float)

mask = medfilt(mask, kernel_size=(1,5))

s_clean= s_full * mask

y_clean = librosa.istft(s_clean*phase)

mask = mask.astype(float)

mask = medfilt(mask, kernel_size=(1,5))

s_clean= s_full * mask

y_clean = librosa.istft(s_clean*phase)

trimmed_clean_audio ,_= librosa.effects.trim(y_clean ,top_db=20)

sf.write('audio_files/noise_reduction_output.wav', y_clean, sample_rate)

sf.write('audio_files/trimmed_noise_reduction_output.wav', trimmed_clean_audio, sample_rate)

plt.figure(figsize=(15,5))
plt.subplot(3,1,1)
plt.title('original audio')
plt.xlabel('time')
plt.ylabel('audio samples')
librosa.display.waveshow(raw_audio, sr=sample_rate)

plt.subplot(3,1,2)
plt.title('denoised audio')
plt.xlabel('time')
plt.ylabel('audio samples')
librosa.display.waveshow(y_clean, sr=sample_rate)

plt.subplot(3,1,3)
plt.title('trimmed denoised audio')
plt.xlabel('time')
plt.ylabel('audio samples')
librosa.display.waveshow(trimmed_clean_audio, sr=sample_rate)


plt.show()
trimmed_clean_audio ,_= librosa.effects.trim(y_clean ,top_db=20)

sf.write('audio_files/noise_reduction_output.wav', y_clean, sample_rate)

sf.write('audio_files/trimmed_noise_reduction_output.wav', trimmed_clean_audio, sample_rate)

plt.figure(figsize=(15,5))
plt.subplot(3,1,1)
plt.title('original audio')
plt.xlabel('time')
plt.ylabel('audio samples')
librosa.display.waveshow(raw_audio, sr=sample_rate)

plt.subplot(3,1,2)
plt.title('denoised audio')
plt.xlabel('time')
plt.ylabel('audio samples')
librosa.display.waveshow(y_clean, sr=sample_rate)

plt.subplot(3,1,3)
plt.title('trimmed denoised audio')
plt.xlabel('time')
plt.ylabel('audio samples')
librosa.display.waveshow(trimmed_clean_audio, sr=sample_rate)


plt.show()

