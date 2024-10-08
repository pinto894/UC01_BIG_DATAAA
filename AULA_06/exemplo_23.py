nomes= []
medias=[]
resp= "S"
while resp == "S" or resp == "s":
    nomes.append(input("Informe o nome do estudante: ")) #obj do append é acrescentar um elemento ao final de uma lista / comando para armazenar os dados dentro do vetor 
    medias.append(float(input("Informe a média do estudante: ")))
    resp = input("Deseja continuar (S/N)? ") #é um loop infinito 
print(nomes)
print(medias)