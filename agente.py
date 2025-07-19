import requests

# 1. Obter o access_token
token_url = "Coloque seu token_url aqui"
client_id = "Coloque seu client_id aqui"
client_secret = "Coloque seu client_secret aqui"

token_resp = requests.post(
    token_url,
    headers={"Content-Type": "application/x-www-form-urlencoded"},
    data={
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret
    }
)

if token_resp.status_code != 200:
    print("Erro ao obter token:", token_resp.status_code, token_resp.text)
    exit(1)

access_token = token_resp.json()["access_token"]

# 2. Chamar o agente StackSpot para várias mensagens
AGENT_ID = "01JY1YZ82QJ28R7H0Y7D56PYCE"
agent_url = f"https://genai-inference-app.stackspot.com/v1/agent/{AGENT_ID}/chat"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Lista de mensagens para enviar ao agente
mensagens = [
    "Crie um README.md para um hello world em linguagem python.",
    "Crie um script em python que eu possar criar um agente no stackspot",
]

for pergunta in mensagens:
    payload = {
        "streaming": False,
        "user_prompt": pergunta,
        "stackspot_knowledge": False,
        "return_ks_in_response": True
    }
    resp = requests.post(agent_url, json=payload, headers=headers)
    if resp.status_code == 200:
        print(f"Pergunta: {pergunta}")
        print("Resposta do agente:", resp.json())
    else:
        print("Erro ao chamar agente:", resp.status_code, resp.text)