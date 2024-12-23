import requests
import json # para enviar solicitações
import os 
from dotenv import load_dotenv # para utilizar a biblioteca python-dotenv e fazer com que o token não apareça

load_dotenv()

url = "https://api.openai.com/v1/chat/completions"

openai_api_key = os.getenv("OPEN_API_KEY") # Chamo a senha que está no .env

#no caso da openai o header é obrigatório pq ela tem TOKEN que é pg para utilizar. 
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {openai_api_key}" #passo a variável sem precisar colocar a senha no código
} #depois de bearer vem o token

# esse data é justamente a pergunta que quero enviar para o chat gpt
data = {
    "model" : "gpt-3.5-turbo",
    "messages": [{"role": "user", "content": "Qual é a capital da França?"}]
}

# o data converte para o dicionário
response = requests.post(url, headers = headers, data = json.dumps(data))

# aqui vai me trazer o dicionário das informações em data
print(response.json())

# posso também escolher o que quero puxar 
# print(response.json()["choices"][0]["message"]["content"])
