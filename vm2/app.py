from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/processar/{texto}")
def processar(texto: str):
    if "autores" in texto:
        resposta = requests.get(f"http://sistema-distribuido_vm3_1:8002/dados/autores").json()
    elif "funcionamento" in texto:
        resposta = requests.get(f"http://sistema-distribuido_vm3_1:8002/dados/funcionamento").json()
    else:
        resposta = {"resposta": "Comando não reconhecido. Tente novamente!"}

    return resposta

