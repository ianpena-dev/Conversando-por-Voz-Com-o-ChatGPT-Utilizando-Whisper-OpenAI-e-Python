import os
from dotenv import load_dotenv

from services.speech_to_text import transcrever_audio
from services.chat import perguntar_chatgpt
from services.text_to_speech import gerar_audio
from services.capture_audio import gravar_audio 
load_dotenv()

def main():
    print("=" * 40)
    print("🎙️ Voice ChatGPT iniciado")
    print("=" * 40)

    while True:
        input("\nPressione ENTER para falar (ou Ctrl+C para sair)...")

        gravar_audio()

        texto = transcrever_audio("app/audio/input.wav")
        print(f"\n🧾 Você disse: {texto}")

        resposta = perguntar_chatgpt(texto)
        print(f"\n🤖 Resposta: {resposta}")

        gerar_audio(resposta)

if __name__ == "__main__":
    main()