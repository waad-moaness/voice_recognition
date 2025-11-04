import numpy as np
import pyaudio 
import matplotlib.pyplot as plt 
import wave 

Frames_per_buffer = 3200
Format = pyaudio.paInt16
Channels = 1
sample_rate = 16000

p = pyaudio.PyAudio()
stream= p.open(
    frames_per_buffer = Frames_per_buffer,
    rate = sample_rate,
    channels = Channels,
    format= Format,
    input= True
)

print('start recording...')

seconds = 8
frames= []
for i in range(0,int(sample_rate/Frames_per_buffer*seconds)):
    data = stream.read(Frames_per_buffer)
    frames.append(data)


stream.stop_stream()
stream.close()


obj = wave.open('../audio_files/micrecording_output.wav', 'wb')
obj.setframerate(sample_rate)
obj.setnchannels(Channels)
obj.setsampwidth(p.get_sample_size(Format))
obj.writeframes(b''.join(frames))
obj.close()

p.terminate()

