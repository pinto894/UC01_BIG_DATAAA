idade=int(input("Digite a sua idade: "))  #para cada if voce pode ter varios elif mas somente um else 
if idade < 18:
    print("Voce é menor de idade!")
elif idade ==18:
    print("Voce tem 18 anos, falta pouco para alcançar o sucesso!")
elif idade >18 and idade <65:
    print("Show, Acesso liberado")
elif idade >60:
    print("O aplicativo não é para a sua idade!")
else:
    print("Acesso liberado")

#nesse caso usamos o and para acrescentar uma condição 
