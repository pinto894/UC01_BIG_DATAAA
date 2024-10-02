#tendo como dado de entrada à altura (h) de uma pessoa, construa um programa que calcule seu peso ideal, utilizando as seguintes formulas:
# para homens (72.7*h)+58 e para mulheres (62.1*h)-44.7

h = float(input("informe a sua altura: "))
M = (72.7 * h) - 58
F = (62.1 * h) - 44.7
print(F"o peso ideal para os homens é {M:.2f} e o peso ideal para as mulheres é {F:.2F}") #fstringer