import whisper
import os
from constants import WAV_OUTPUT_DIRECTORY

def transcribe_audio(file_path):
    model = whisper.load_model("base")  # You can choose different model sizes

    result = model.transcribe(file_path)
    print(f"Transcription for {file_path}: {result['text']}")

def transcribe_all_recordings():
    for filename in os.listdir(WAV_OUTPUT_DIRECTORY):
        if filename.endswith('.wav'):
            file_path = os.path.join(WAV_OUTPUT_DIRECTORY, filename)
            transcribe_audio(file_path)

if __name__ == "__main__":
    transcribe_all_recordings()
