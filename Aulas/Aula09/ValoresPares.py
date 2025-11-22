valor = int(input("Digite um valor: "))
if valor % 2 != 0:
    valor -= 1
for cont in range(valor, 0, -2):
    print(cont)