import pyaudio
import numpy as np

# Set up the parameters for the audio stream
CHUNK = 1024  # The size of each audio chunk coming from the input device
WIDTH = 2  # The width in bytes of each sample
CHANNELS = 2  # The number of audio channels (1=mono, 2=stereo)
RATE = 44100  # The number of samples per second

# Create a PyAudio instance
p = pyaudio.PyAudio()

# Create a stream for the microphone
stream_in = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Create a stream for the speakers
stream_out = p.open(format=p.get_format_from_width(WIDTH),
                 channels=CHANNELS,
                 rate=RATE,
                 output=True)

print("Starting audio stream... Press Ctrl+C to stop.")

# Continuously record and play back audio in chunks
try:
    while True:
        data = stream_in.read(CHUNK)
        stream_out.write(data)
except KeyboardInterrupt:
    print("Stopping audio stream.")

# Close the streams
stream_in.stop_stream()
stream_in.close()
stream_out.stop_stream()
stream_out.close()

p.terminate()