import requests
import json # para enviar solicitações

url = "https://api.openai.com/v1/chat/completions"

#no caso da openai o header é obrigatório pq ela tem TOKEN que é pg para utilizar. 
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer $OPENAI TOKEN"
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
# print(response.json()['choices'][0]['message']['content'])
