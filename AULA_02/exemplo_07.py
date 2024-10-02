#calcular o valor de uma prestação em ataso, utilizando a formula: valorfinal = prestacao+(prestacao*(taxa/100)*tempo

prestacao = float(input("informe o valor da prestação: "))
taxa = float(input("informe a taxa de juros mensal: "))
tempo = int(input("informe a quantidade de meses em atraso: "))
valor_final = prestacao + (prestacao * taxa / 100* tempo)
print(F"sua prestação em atraso é de R$ {valor_final:.2F}") #FSTRINGER