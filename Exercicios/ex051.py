for i in range(0, 8):
    produto = float(input(f"Digite o preço do {i+1} produto: "))
    if (i == 0):
        maior = produto
        menor = produto
    else:
        if (produto > maior):
            maior = produto
        if (produto < menor):
            menor = produto
print("Acabou")
print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")