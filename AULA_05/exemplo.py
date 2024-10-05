soma = 0                          #só podemos calcular a media depois que tiver a soma, por isso ela fica do lado de "fora"
#media= 0
for i in range (5):
    nome = input("Informe o seu nome:")
    idade = int(input("Informe a sua idade:  "))
    soma = soma + idade
media = soma / (i + 1)
print(f"A soma é {soma}")
print(f"A media  é {media:.0f}")
