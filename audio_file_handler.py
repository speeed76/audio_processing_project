import os
import wave
import pyaudio  # Import pyaudio here
from datetime import datetime
from constants import FILENAME_FORMAT, WAV_OUTPUT_DIRECTORY, FORMAT, CHANNELS, RATE

def save_chunk(frames):
    # Ensure output directory exists
    if not os.path.exists(WAV_OUTPUT_DIRECTORY):
        os.makedirs(WAV_OUTPUT_DIRECTORY)

    filename = datetime.now().strftime(FILENAME_FORMAT)
    file_path = f"{WAV_OUTPUT_DIRECTORY}/{filename}"

    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))  # This should work now
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))

    print(f"Audio chunk saved: {file_path}")
