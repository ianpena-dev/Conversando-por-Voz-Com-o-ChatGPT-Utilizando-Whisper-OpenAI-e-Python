import sounddevice as sd
from scipy.io.wavfile import write

def gravar_audio(arquivo="app/audio/input.wav", duracao=5, fs=44100):
    print("🎤 Gravando...")

    audio = sd.rec(int(duracao * fs), samplerate=fs, channels=1)
    sd.wait()

    write(arquivo, fs, audio)

    print("✅ Gravação finalizada.")