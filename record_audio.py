import pyaudio
import wave
from audio_file_handler import save_chunk
from constants import CHUNK_SIZE, FORMAT, CHANNELS, RATE, RECORD_SECONDS

def record_audio():
    audio = pyaudio.PyAudio()
    stream = None

    try:
        stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK_SIZE)

        print("Recording...")

        frames = []

        for i in range(0, int(RATE / CHUNK_SIZE * RECORD_SECONDS)):
            try:
                data = stream.read(CHUNK_SIZE)
                frames.append(data)
            except IOError as e:
                if e.errno == pyaudio.paInputOverflowed:
                    print("Input buffer overflow. Skipping this chunk.")
                    continue

        print("Finished recording.")

    finally:
        if stream and stream.is_active():
            stream.stop_stream()
            stream.close()
        audio.terminate()

    save_chunk(frames)

if __name__ == "__main__":
    record_audio()
