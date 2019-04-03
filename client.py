from jwtBiblioteca import criar_chave
from jwtBiblioteca import decodificar_chave
import requests as req
import json

# Exemplo
# localhost:5000/api/foo?a=hello&b=world

def main():
    print("")
    print("Selecione se deseja criar ou decodificar o Token")
    print("1 - Criar / 2 - Decodificar / [Digite qualquer tecla] - Sair")
    print("")
    
    while True:
        print("")
        opc = input("Digite a opção: ")
        if opc == "1":
            criar()
            continue
        elif opc == "2":
            decodificar()
            continue
        else:
            break

def criar():
    from modelo import alg, payload, secret
    url = "http://127.0.0.1:5000/criar"
    payload_final = json.dumps(payload)
    dados = {"alg": alg, "payload": payload_final, "secret": secret}
    retorno = req.api.post(url,dados).json()
    print(retorno)

def decodificar():
    from chave import chave, secret, alg
    url = "http://127.0.0.1:5000/decodificar"
    dados = {"alg": alg, "chave": chave, "secret": secret}
    retorno = req.post(url,dados).json()
    print(retorno)

main()