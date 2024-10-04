import datetime # como é um módulo sempre tem que importar 
try:
    data_atual = datetime.date.today()
    idade = int(input("informe a sua idade:  "))
    tempo_trabalhado= int(input("Informe quantos anos voce está nesta empresa:  "))
except ValueError:
    print("Verifique os dados informados.")
else:
    if idade >=65:
        print("Apto a aposentadoria")
    elif tempo_trabalhado >=30:
        print("Apto a aposentadoria")
    elif idade >=60 and tempo_trabalhado >=25:
        print("Apto a aposentadoria")
    else:
        print("Inapto a aposentadoria")



