import requests, json, os
from dotenv import load_dotenv

load_dotenv()

key = str(os.getenv('API_KEY'))

cores = {
    'limpar': '\033[m',
    'verde': '\033[1;30;42m',
    'azul': '\033[1;30;44m'
}

headers = {"Authorization": f"Bearer {key}", "Content-Type": "application/json"}
link = "https://api.openai.com/v1/chat/completions"
id_modelo = "gpt-3.5-turbo"

while True:
    mensagem_usuario = input(f"{cores['azul']}Usuário:{cores['limpar']} ")
    if mensagem_usuario.lower() == "sair":
        break
    else:
        body_messagem = {
            "model": id_modelo,
            "messages": [{"role": "user", "content": f"{mensagem_usuario}"}],
        }
        body_messagem = json.dumps(body_messagem)
        requisicao = requests.post(link, headers=headers, data=body_messagem)

        #print(requisicao)
        resposta = requisicao.json()
        mensagem_chatgpt = resposta['choices'][0]['message']['content']
        print(f"\n{cores['verde']}Assistant:{cores['limpar']}")
        print(f"{mensagem_chatgpt}\n")

