nome = input("Estudante, informe o seu nome: ")
av1 = float(input("Nota da AV1: "))
av2 = float(input("Nota da AV2: "))
media = (av1 + av2) / 2
if media >= 70:
    print(F"{nome}, Parabéns, voce foi aprovado, pois sua média foi {media:.2F}")
elif media >= 30 and media <70:
    print(F"{nome}, Te vejo na recuperação, pois sua média foi {media:.2F}")
else:
    print(F"Voce está reprovado, pois sua média foi {media:.2F}")

#exemplo usando o and