import redis
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class ConexaoRedis:
    def __init__(self, host=os.getenv("CONEXAO_REDIS"), port=6379, db=0):
        self.host = host
        self.port = port
        self.db = db
        self.conexao = redis.StrictRedis(host=self.host, port=self.port, db=self.db)

    def definir_valor(self, chave, valor):
        self.conexao.set(chave, valor)

    def obter_valor(self, chave):
        conteudo = self.conexao.get(chave)
        if conteudo:
            return conteudo.decode('utf-8').replace("'", '"')
        return None

    def adicionar_lista(self, chave, *itens):
        self.conexao.lpush(chave, *itens)

    def obter_lista(self, chave):
        return self.conexao.lrange(chave, 0, -1)