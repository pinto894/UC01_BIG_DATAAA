try:
    n1 = int(input("informe um numero inteiro: "))
    n2 = int(input("informe um numero inteiro: "))
except ValueError: #verifica o erro para o caso de alguem digitar uma letra em vez de numero inteiro
    print("verifique a entrada de dados.")
else:
    try:
        valor = n1 / n2 #o try executa essa ação 
    except ZeroDivisionError: #ver qual erro foi gerado no try senão vai para o else
        print("Não é possivel dividir por zero.")
    else:
        print(valor)



