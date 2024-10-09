
usuarios = ["pedro", "maria" , "duda", "dirceu" , "elvis"]
senhas = ["123", "345", "567","@@@$$$","8910"]
usuario = input("Informe o seu acesso ao sistema: ")
for i in range(len(usuarios)):
    if usuarios [i] == usuario:
        senha = input("Informe a sua senha de acesso ao sistema: ")
        if senhas [i] == senha:
            resp = "Acesso liberado "
        else:
            resp = "Senha não confere"
        break
else:
    resp = "Usuário não encontrado"
print(resp)









