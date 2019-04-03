from jose import jwt
from flask import Flask
from flask import request
from flask import jsonify
import json

app = Flask(__name__)

@app.route("/criar", methods=['GET', 'POST'])
def criar_chave():
    dados = request.form.to_dict()

    alg = dados['alg']
    payload = dados['payload']
    secret = dados['secret']

    payload_final = json.loads(payload)

    chave = jwt.encode(payload_final, secret, algorithm=alg)
    arquivo = open('chave.py','w')
    arquivo.write("chave = '" + str(chave) + "'\n")
    arquivo.write("alg = '" + str(alg) + "'\n")
    arquivo.write("secret = '" + str(secret) + "'")
    
    mensagem = {"Chave": str(chave), "Algoritmo": str(alg), "Secret": str(secret)}
    return jsonify(mensagem)

@app.route("/decodificar", methods=['GET', 'POST'])
def decodificar_chave():
    dados = request.form.to_dict()

    alg = dados['alg']
    chave = dados['chave']
    secret = dados['secret']
    
    chave_decode = jwt.decode(chave, secret, alg)
    print(chave_decode)

    arquivo = open('chave_decodificada.py','w')
    arquivo.write("payload = " + str(chave_decode) + "")
    
    mensagem = {"Payload": str(chave_decode)}
    return jsonify(mensagem)

if __name__ == "__main__":
    app.run()