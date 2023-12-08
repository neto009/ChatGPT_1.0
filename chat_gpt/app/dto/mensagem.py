from pydantic import BaseModel

class Message(BaseModel):
    conteudo: str
    key: str
