h = float(input("informe a sua altura: "))
s = input("informe M - para masculino e F - para feminino")
if s == "M" or s == "m":
    m = (72.7 * h) - 58
    print(F"o peso ideal para os homens é {m:.2f}")
elif s == "F" or "f":
    f = (62.1 * h) - 44.7
    print(F"o peso ideal para as mulheres é {f:.2F}")
else:
   print("Verifique o sexo informado")

#com o OR ele vai aceitar sendo informado com ele minuscula ou maiuscula, pois considera um ou outro