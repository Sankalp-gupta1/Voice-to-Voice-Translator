import sounddevice as sd
from scipy.io.wavfile import write
import time

def record_audio(filename="input.wav", duration=15, fs=44100):
    print("🎙️ Speak Now...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()
    write(filename, fs, recording)
    print("✅ Audio Recorded")
    return filename
