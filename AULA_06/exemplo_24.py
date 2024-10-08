nomes= []
medias=[]
resp= "S"
while resp == "S" or resp == "s":
    nomes.append(input("Informe o nome do estudante: ")) 
    medias.append(float(input("Informe a média do estudante: ")))
    resp = input("Deseja continuar (S/N)? ") 
for i in range(len(medias)):
    print(i,"- ", nomes[i], " - " , medias [i])
maior_media = max(medias)
pos = medias.index(maior_media)
print(f"{nomes[pos]}, voce possui a maior média.")
print(f"A media das notas é: {sum(medias) / len(nomes):.1f} ")  
print(f"A maior média é: {max(medias)} ") 
print(f"A menor média é: {min(medias)} ") 
print(f"A amplitude da média da turma é  {max(medias)-min(medias)} ") #é a variação, discrepancia do conjunto de dados 
medias.sort()
print(medias)
