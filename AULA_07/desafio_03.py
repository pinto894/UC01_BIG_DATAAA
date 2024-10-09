sexo=[]
olhos = []
cabelos= []
idade=[]
resp= "S"
qtd_sexo_idade=0
qtd_olhos_cabelos=0
while resp == "S" or resp == "s":
    sexo.append(input("Informe o sexo M- Masculino ou F - Feminino")) 
    olhos.append(input("Informe a cor dos seus olhos A - azuis, V- verdes ou C- castanhos "))
    cabelos.append(input("Informe a cor dos seus cabelos L- louros, P - pretos ou C - castanhos"))
    idade.append(int(input("Informe a sua idade: ")))
    resp = input("Deseja continuar (S/N)? ") 
for i in range(len(sexo)):
    if (sexo[i]== "F" or sexo [i] == "f") and (idade >= 18 and idade <= 35):
        qtd_sexo_idade +=1
    if (olhos[i] == "V" or olhos[i] == "v") and (cabelos[i] == "L" or cabelos[i] == "l"):
        qtd_olhos_cabelos +=1
print(f"A maior idade é {max(idade)} anos.")
print(f"A menor idade é {min(idade)} anos.")
