import os
import shutil
from glob import glob

# 1. Setup
source_folder = '/home/waad/Documents/voice_recognition/final_test_audios'
new_folder = '/home/waad/Documents/voice_recognition/modified_test_audio'
# Create the new folder if it doesn't exist
os.makedirs(new_folder, exist_ok=True)

# 2. Get files WITHOUT sorting
# This preserves the order exactly as your file system gives it to Python
files = glob(os.path.join(source_folder, 'audio*.wav'))

# 3. Copy and Rename
for i, old_path in enumerate(files, 1):
    # New name will be 1.wav, 2.wav, etc. inside the new folder
    new_path = os.path.join(new_folder, f"audio{i}.wav")
    
    shutil.copy(old_path, new_path)
    print(f"Copied: {old_path} -> {new_path}")