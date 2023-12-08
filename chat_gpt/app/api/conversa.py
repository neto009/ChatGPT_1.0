from fastapi import FastAPI
from ..dto.mensagem import Message
from ..service.conversa_service import conversation

app = FastAPI()

@app.post("/conversa/")
async def receber_mensagem(mensagem: Message):
    return conversation(mensagem)
