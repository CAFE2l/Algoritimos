v = []
for cont in range(1, 7):
    valor = int(input(f"Digite o {cont}º valor: "))
    v.append(valor)

for c in range(1, 7):
    print(v[c-1], end=" ")