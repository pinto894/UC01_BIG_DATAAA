idades = [20,10,15,30,50,12,60,22,55,35]
print(f"A soma das idades é: {sum(idades)} anos") #sun=soma 
print(f"A maior idades é: {max(idades)} anos") #max = maior
print(f"A menor idades é: {min(idades)} anos") #min = menor
print(f"A media das idades é: {sum(idades) / len(idades)} anos") #não tem comando para media, então a gente soma com o sum e divide usando o len que é a quantidade/tamanho do vetor 
idades.sort() #coloca a lista em ordem crescente
print(idades)
