from gtts import gTTS
import pygame
import time
import os

def gerar_audio(texto, caminho="app/audio/output.mp3"):
    # Garante que a pasta existe
    os.makedirs(os.path.dirname(caminho), exist_ok=True)

    # Gera o áudio com gTTS
    tts = gTTS(text=texto, lang="pt")
    tts.save(caminho)

    # Inicializa o mixer do pygame apenas uma vez
    if not pygame.mixer.get_init():
        pygame.mixer.init()

    # Carrega e toca o áudio
    pygame.mixer.music.load(caminho)
    pygame.mixer.music.play()

    # Aguarda até terminar de tocar
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
