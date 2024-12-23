# código refatorado para BD SQL (PostgreSQL, pois o sqlite3 não permite múltiplos acessos a tabela).
# criar ETL para continuar rodando o código em tempo real. # utiliza RENDER (é uma cloud) para criar o BD.
# é necessário instalar via pip o psycopg2 para que esse drive permita que o código criado interaja com o postgresql


import time # para ficar rodando sem precisar que eu dê um comando. Criar robo que rode a x segundos puxando os dados para mim
import requests
from datetime import datetime #importar biblioteca de timestamp para fazer gestão do tempo
from dotenv import load_dotenv
from sqlalchemy import create_engine # para criar a tabela do bd
from sqlalchemy.orm import sessionmaker #sessionmaker para criar sessão com bd
import os
from database import Base, BitcoinPreco #importação do arquivo database, da classe e do objeto neles contido

# carrega variáveis de ambiente do arquivo .env
load_dotenv()

# Lê as variáveis separadas do arquivo .env (sem SSL)
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_PORT = os.getenv("POSTGRES_PORT")
POSTGRES_DB = os.getenv("POSTGRES_DB")

# Monta a URL de conexão ao banco PostgreSQL (sem ?sslmode=...)
DATABASE_URL = (
    f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}"
    f"@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"
)

# Cria o engine e a sessão para o bd
engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

# função para criar a tabela no postgresql
def criar_tabela():
    """Cria a tabela no banco de dados, se não existir."""
    Base.metadata.create_all(engine)
    print("Tabela criada/verificada com sucesso!")


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

# função criada para salvar os dados no postgresql
def salvar_dados_postgres(dados):
    """Salva os dados no banco PostgreSQL."""
    session = Session() #criar sessao
    novo_registro = BitcoinPreco(**dados) #inserir os dados que estavam no tipo dicionário dentro do objeto que coloquei na bd 
    session.add(novo_registro) #adicionar um novo registro
    session.commit() #commitar o novo registro
    session.close() # frechar a sessao dentro do postgresql
    print(f"[{dados['timestamp']}] Dados salvos no PostgreSQL!")

# indica que só roda as linhas de baixo se executar esse código de forma direta, não como módulo. 
if __name__ == "__main__":
    criar_tabela()
    print("Iniciando ETL com atualização a cada 15 segundos... (CTRL+C para interromper)")

    while True:
        try:
            dados_json = extract_dados_bitcoin()
            if dados_json:
                dados_tratados = transform_dados_bitcoin(dados_json)
                print("Dados Tratados:", dados_tratados)
                salvar_dados_postgres(dados_tratados)
            time.sleep(15)
        except KeyboardInterrupt:
            print("\nProcesso interrompido pelo usuário. Finalizando...")
            break
        except Exception as e:
            print(f"Erro durante a execução: {e}")
            time.sleep(15)

# poderia ser fieto de forma direta sem o try/except

# para checar a tabela abrir pgadmin e passar as variáveis de acesso. Registra um novo servidor no pgadmin, faz conexões com as variáveis e salva para se conectar.