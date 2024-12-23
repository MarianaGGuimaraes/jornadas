import requests

url = 'https://api.coinbase.com/v2/prices/spot'
headers = {
    "Accept": "application.json",
    "User-Agent": "MinhaAplicacao/1.0"
} #aqui tenho informaçoes sobre o que quero receber e o nome da aplicação
params = {"currency":"USD"} # obter apenas essa moeda na consulta

response = requests.get(url, headers=headers, params=params) # na minha requisição posso passar url, params e header que é como se fosse o cabeçalho das informações que estou passando

data = response.json()
print(f"Preço do Bitcoin (USD):", data["data"]["amount"]) 