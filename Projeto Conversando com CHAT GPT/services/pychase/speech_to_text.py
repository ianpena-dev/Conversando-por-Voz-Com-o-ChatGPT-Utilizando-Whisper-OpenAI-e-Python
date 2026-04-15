from openai import OpenAI
import os

def transcrever_audio(caminho_audio):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    with open(caminho_audio, "rb") as audio:
        resposta = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio
        )

    return resposta.text