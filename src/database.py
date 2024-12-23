# declaro as colunas da tabela aqui. Aqui escrito em forma de objeto. O sqlalchemy vai pegar essa classe e transformar em sql
# importação dos elementos sql orm
from sqlalchemy.orm import declarative_base #faz conversão de objeto para código sql
from sqlalchemy import Column, Float, String, Integer, DateTime #atributos do bd, tipo de coluna que quero no bd
from datetime import datetime #para ter timestamp

#cria a classe Base do sqlalchemy (na versão 2.x)
Base = declarative_base()

# aqui declaro o nome da tabela e todas as colunas que terá
class BitcoinPreco(Base):
    """Define a tabela no banco de dados."""
    __tablename__ = "bitcoin_precos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    valor = Column(Float, nullable=False)
    criptomoeda = Column(String(50), nullable=False)  # até 50 caracteres
    moeda = Column(String(10), nullable=False)        # até 10 caracteres
    timestamp = Column(DateTime, default=datetime.now)

    # o alchemy é o mais utilizado, mas tem o sql model que utiliza o alchemy por trás.