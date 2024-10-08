nomes_01 = "Alessando, Maria , Pedro, Duda , Eduardo" #string
nomes_02 = ["Alessando", "Maria" , "Pedro", "Duda" , "Eduardo", "Manoel"] #vetor #toda representação de vetor começa com conchetes 
print(nomes_01)
print(nomes_02)
print(nomes_02[2])
n = 1
print(len(nomes_02)) #len = serve para mostrar o comprimento do vetor, quantos registros tem no vetor, nesse caso foram 6
for i in range(len(nomes_02)): #a linha for é uma estrutura de repetição, e nessa situaçã ele repete na quantidade de vezes do vetor 
    print(F"{n} - {nomes_02[i]}")
    n+=1