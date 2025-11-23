val = []
TotPar = 0
for i in range(1, 7):
    valor = int(input(f"Digite o {i}º valor: "))
    val.append(valor)

    if (val[i-1] % 2 == 0):
        TotPar += 1
    
print(f"O total de pares foi {TotPar}")
for i in range(1, 7):
    if (val[i-1] % 2 == 0):
        print(f"valores pares na posição {i}: com o número {val[i-1]}")