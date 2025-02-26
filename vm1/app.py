from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/mensagem/{texto}")
def processar_mensagem(texto: str):
    resposta = requests.get(f"http://sistema-distribuido_vm2_1:8001/processar/{texto}").json()
    return {"sistema": "VM1", "resposta": resposta}
