# HS256 / RS256
alg = 'HS256'

#SUB (subject) = ID do usuário do token pertencente
#EXP (expiration) = Timestamp de quando o token irá expirar
#IAT (issued at) = Timestamp de quando o token foi criado
#AUD (audience) = Destinatário do token

payload = {
    'iss': 'localhost',
    'name': 'teste',
    'email': 'teste@teste.com'
}

secret = 'Impacta'