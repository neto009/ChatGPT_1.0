from openai import OpenAI
from ..dto.conversation import Chat
from ..config.redis_config import ConexaoRedis
from ..dto.mensagem import Message
import os
import uuid
import json

model_id = 'gpt-3.5-turbo'
client = OpenAI(
    api_key=os.environ.get('GPT'),
)
conexao = ConexaoRedis()


def conversation(mensagem: Message) -> Chat:
    key_redis = __validar_key__(mensagem.key)
    valor = json.loads(conexao.obter_valor(key_redis))
    print(valor)
    response = __chamada_openai__(mensagem.conteudo)
    body_redis = [mensagem.conteudo, str(response.choices[0].message.to_dict())]
    #conexao.adicionar_lista(key_redis, *body_redis)
    return {response}


def __validar_key__(key) -> str:
    return str(key if key is not None and len(key) > 0 else uuid.uuid4())


def __chamada_openai__(mensagem) -> Chat:
    return Chat(client.chat.completions.create(
        model=model_id,
        temperature=0.8,
        messages=[{"role": "assistant", "content": "Voce sera um desenvolvedor de software, quando for questionado sobre sua funcionalidade deverá responder que é um desenvolvedor de software."},
                  {"role": "user", "content": mensagem}]
    ))
