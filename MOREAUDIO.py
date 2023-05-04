import pyaudio

# Set up the parameters for the audio stream
CHUNK = 1024  
WIDTH = 2  
CHANNELS = 2
RATE = 44100

# Create a PyAudio instance
p = pyaudio.PyAudio()

# Create a stream for the microphone
stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

# Record audio in chunks for 5 seconds
for i in range(0, int(RATE / CHUNK * 5)):
    data = stream.read(CHUNK)

# Close the stream
stream.stop_stream()
stream.close()

p.terminate()