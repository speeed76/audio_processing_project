import pyaudio

# Audio recording parameters
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 5

# File handling parameters
FILENAME_FORMAT = "%Y%m%d%H%M%S.wav"
WAV_OUTPUT_DIRECTORY = "./recorded_chunks"
