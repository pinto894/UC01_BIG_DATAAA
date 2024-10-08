
usuarios = ["pedro", "maria" , "duda", "dirceu" , "elvis"]
senhas = ["123", "345", "567","@@@$$$","8910"]
usuario = input("Informe o seu acesso ao sistema: ")
for i in range(len(usuarios)):
    if usuarios [i] == usuario:
        resp = input("Informe o seu acesso ao sistema: ")
        resp2 = int(input("Informe a sua senha de acesso ao sistema: "))
        break
else:
    resp = "Usuário não encontrado"
print(resp)









