from fastapi import FastAPI

app = FastAPI()

# Endpoint para retornar autores
@app.get("/dados/autores")
def autores():
    return {"resposta": "Autores: Kayky Vasconcelos, Samara Marques, Thais Helena, Leonardo Arouche e  Rafael Ferreira. Desenvolvido para a disciplina de Sistemas Distribuídos."}

# Endpoint para explicar o funcionamento
@app.get("/dados/funcionamento")
def funcionamento():
    return {"resposta": "O sistema funciona utilizando microservices Docker, FastAPI e comunicação entre VMs."}

