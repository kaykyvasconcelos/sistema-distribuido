import requests

def menu():
    while True:
        print("\n💻 Bem-vindo ao Sistema Integrado 💻")
        print("[1] Saber Sobre os Autores")
        print("[2] Saber Como Funciona")
        print("[3] Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            resposta = requests.get("http://localhost:8000/mensagem/autores").json()
            print("\n🔹", resposta["resposta"])
        elif escolha == "2":
            resposta = requests.get("http://localhost:8000/mensagem/funcionamento").json()
            print("\n🔹", resposta["resposta"])
        elif escolha == "3":
            print("\n✅ Saindo do sistema...")
            break
        else:
            print("\n❌ Opção inválida, tente novamente!")

if __name__ == "__main__":
    menu()

