# Procedimento de utilização da biblioteca JWT JOSE

Copie os arquivos:
  - modelo.py
  - client.py
  - jwtBiblioteca.py

Primeiramente é necessário informar dentro do arquivo modelo o tipo do algoritmo que irá ser utilizado, os dados que deverá ser informado dentro do payload e digitar a assinatura desejada dentro de secret.

Após inicializar o arquivo o client.py, ele irá solicitar a opção desejada sendo 1 para criar o token com base nos dados do arquivo modelo.py e irá retornar o arquivo chave.py e 2 para decodificar o token que utilizará como base o arquivo chave.py e irá retornar o arquivo chave_decodificada.py. Ambos irá retornar a mensagem em jsonify.
