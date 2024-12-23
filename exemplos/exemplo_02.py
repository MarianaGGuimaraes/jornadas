import requests

# posso utilizar o parametro dentro da chave valor. É como se fosse um select. 
url = 'https://jsonplaceholder.typicode.com/comments/'
params = {"postId":1} #obter apenas comentários do postId=1
response = requests.get(url, params=params)

# Chamar a função json() para obter os dados como um dicionário
comentarios = response.json() #O método response.json() converte a resposta do servidor, que está no formato JSON, para um dicionário Python.


print(f"Foram encontrados {len(comentarios)} comentários.") # o len conta aqui quantos comentários tem
print(f"Erro: {response.status_code} - {response.text}") # código de status da resposta (response.status_code) e o texto da resposta (response.text)