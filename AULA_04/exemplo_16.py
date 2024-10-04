#if #elif else
try:
    produto= input("Informe um produto: ")
    quantidade = int(input("Informe a quantidade adquirida:  "))
    valor = float(input("informe o valor unitário:  "))
except ValueError:
    print("verifique o valores informados")
else:
    total = quantidade * valor
    print(f"o valor total sem desconto é R${total:.2F}")
    if quantidade <=5:
        print("total a pagar" , total * 0.98)
    elif quantidade >5 and quantidade <=10:
        print("total a pagar", total *0.97)
    else:
        print("total a pagar", total * 0.95)


