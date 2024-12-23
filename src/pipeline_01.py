import time # para ficar rodando sem precisar que eu dê um comando. Criar robo que rode a x segundos puxando os dados para mim
import requests
from tinydb import TinyDB
from datetime import datetime #importar biblioteca de timestamp para fazer gestão do tempo

# função para extrair
def extract_dados_bitcoin():

    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    dados = response.json() #quero pegar só os dados
    return dados

# função para transformar os dados. O nome amount, base, currency que tem na saída da api vai receber o nome valor, cripto e moeda. Ela vai receber os dados que tão na saída do extract. 
def transform_dados_bitcoin(dados):
    valor = dados["data"]["amount"] #valor receberá dados com esses params
    criptomoeda = dados["data"]["base"]
    moeda = dados["data"]["currency"]
    timestamp = datetime.now().timestamp()

    #salvar tudo numa chave. pq quero que tudo fique num pacote para salvar tudo junto dentro de um db ou outro tipo de arquivo
    dados_transformados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp" : timestamp
    }
    return dados_transformados

#vou passar os dados transformados e o nome do bd tinydb (nosql). Assim criará um arquivo local do tipo json. 
def salvar_dados_tinydb(dados, db_name="bitcoin.json"):
    db = TinyDB(db_name)  #digo que meu bd vai ser o tinydb. a biblitoeca pede isso
    db.insert(dados) # fazer insert no banco nosql
    print("Dados salvos com sucesso")

# indica que só roda as linhas de baixo se executar esse código de forma direta, não como módulo. 
if __name__ == "__main__":
    #Extração dos dados
    while True:    #criar condição que nunca vai acabar. loop dentro do processo a cada 15 seg. 
        dados_json = extract_dados_bitcoin()
        dados_tratados = transform_dados_bitcoin(dados_json)
        salvar_dados_tinydb(dados_tratados)
        time.sleep(15)