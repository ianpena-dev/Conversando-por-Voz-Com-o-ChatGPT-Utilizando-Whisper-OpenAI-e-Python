from openai import OpenAI
import os

def perguntar_chatgpt(mensagem):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    resposta = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Responda de forma clara e objetiva."},
            {"role": "user", "content": mensagem}
        ]
    )

    return resposta.choices[0].message.content