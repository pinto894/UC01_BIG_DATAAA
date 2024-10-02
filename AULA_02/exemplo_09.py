import datetime
data_atual = datetime.date.today()
n2 = input("informe o seu nome: ")
n1 = int(input("Informe o seu ano de nascimento: "))
resultado =   data_atual.year - n1
print(n2,"a sua idade é: ", resultado)
