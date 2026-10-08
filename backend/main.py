from fastapi import FastAPI
from pydantic import BaseModel


#Criando a aplicação FastAPI
app = FastAPI()


# Definindo o modelo de dados para a requisição
class Solicitacao(BaseModel):
    solicitacao: str

# Definindo o modelo de dados para a requisição
@app.get("/health") 
def health():          
    return {"Status": "Entregue"} 

# Definindo o modelo de dados para a requisição
@app.post("/chat")
def fazer_pedido(pedido: Solicitacao):
    return {"response": f"solicitacao: {pedido.solicitacao}"}

