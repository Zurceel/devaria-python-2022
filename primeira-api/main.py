from typing import  Optional
from fastapi import FastAPI
from pydantic import BaseModel

class Usuario(BaseModel):
    nome: str
    usuario: Optional[str] = None
    senha: str


app = FastAPI()

@app.get("/ola-mundo")
def read_root():
    return {
        "mensagem": "Olá mundo, essa é minha primeira API!"
    }

@app.get("/api/soma")
def soma():
    return {
        "resultado": 2 + 3
    }

@app.post("/api/login")
def login(usuario: Usuario):
    if usuario.nome == "Gabriel" and usuario.senha == "1234":
        resposta = {
            "mensagem": "Login realizado com sucesso"
        }
    else:
        resposta = {
            "menagem": "Usuairo ou Senha incorretos"
        }

    return resposta