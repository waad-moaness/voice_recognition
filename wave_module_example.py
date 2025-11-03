import wave 
import numpy as np
import matplotlib.pyplot as plt 

obj = wave.open('audio_files/03-01-01-01-02-01-02.wav', 'rb')
number_channels= obj.getnchannels()
sample_width = obj.getsampwidth()
number_samples= obj.getnframes()
sample_rate = obj.getframerate()
frames = obj.readframes(-1)
time_audio = number_samples / sample_rate

print('##### audio 1 #####')
print(f'number of channels: {number_channels}')
print(f'sample width:  {sample_width}')
print(f'sample rate: {sample_rate}')
print(f'number of actual raw frames  {len(frames)}')
print(f'number of frames in a byte {number_samples}')

obj.close()

new_obj = wave.open('audio_files/wave_module_saveing_files.wav', 'wb')

new_obj.setframerate(sample_rate)
new_obj.setnchannels(number_channels)
new_obj.setsampwidth(sample_width)
new_obj.writeframes(frames)

print('##### audio 2 #####')
print(f'number of channels: {new_obj.getnchannels()}')
print(f'sample width:  {new_obj.getsampwidth()}')
print(f'sample rate: {new_obj.getframerate()}')
print(f'number of frames in a byte {new_obj.getnframes()}')

new_obj.close()

# plotting 
# first open the new object file in read mode 
new_obj = wave.open('audio_files/wave_module_saveing_files.wav', 'rb')

#create a numpy array from a byte object as int values 
audio_samples = np.frombuffer(new_obj.readframes(-1), dtype=np.int16 )
audio_samples_time = new_obj.getnframes() / new_obj.getframerate()
time = np.linspace(0, audio_samples_time , num=new_obj.getnframes() )

plt.figure(figsize=(10,5))
plt.plot(time,audio_samples)
plt.title('audio visualization')
plt.xlabel('time')
plt.ylabel('audio_samples')
plt.xlim(0, audio_samples_time)
plt.show()