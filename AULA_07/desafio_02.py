temperatura = []
resp= "S"
while resp == "S" or resp == "s":
    temperatura.append(float(input("Informe a temperatura: ")))
    resp= input("Deseja Continuar (S/N)? ")
print(f"A maior temperatura é: {max(temperatura)} ºC!") #max = maior
print(f"A menor temperatura é: {min(temperatura)} ºC!") #min = menor
print(f"A media das temperaturas é: {sum(temperatura) / len(temperatura)} ºC") #não tem comando para media, então a gente soma com o sum e divide usando o len que é a quantidade/tamanho do vetor 
