h = float(input("informe a sua altura: "))
sexo = input("informe M - para masculino e F - para feminino")
if sexo == "M":
    m = (72.7 * h) - 58
    print(F"o peso ideal para os homens é {m:.2f}")
elif sexo == "F":
     f = (62.1 * h) - 44.7
     print(F"o peso ideal para as mulheres é {f:.2F}")
else:
   print("Verifique o sexo informado")

#somente será aceito se for digitido em letras maiusculas, igual está no código 