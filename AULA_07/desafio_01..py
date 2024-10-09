valor_hora=float(input("quanto voce recebe por hora?" ))
hora_trabalhada= float(input("Quantas horas voce trabalhou esse mês?" ))
IRRF= 0.11
INSS= 0.08
SINDICATO= 0.05
salario_bruto= valor_hora * hora_trabalhada
print(f"Valor do salario bruto é R$:",salario_bruto)
IRRF= salario_bruto*0.11
print(f"Valor do desconto do IRRF R$:",IRRF)
INSS= salario_bruto * 0.08
print(f"Valor do desconto do INSS R$:",INSS)
SINDICATO= salario_bruto * 0.05
print(f"Valor do desconto do SINDICATO R$:",SINDICATO)
SALARIO_LIQUIDO= salario_bruto - IRRF - INSS - SINDICATO
print(F"O valor do salário liquido é R$:", SALARIO_LIQUIDO)
