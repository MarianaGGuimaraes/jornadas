import requests

# a biblioteca requests vai fazer uma solicitação e vai voltar uma resposta da apu
url = ' https://www.google.com/'

resposta = requests.get(url)

print(resposta)

# dentro de uma api pode-se ter números de 100 a 500. 200 significa que a requisição do cliente foi bem sucedida.

url = 'https://jsonplaceholder.typicode.com/posts/1'

response = requests.get(url)
data = response.json()
print(data)
# a resposta é o que está no site do jsonplaceholder
