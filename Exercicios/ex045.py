primeiroValor = int(input("Digite o primeiro valor: "))
segundoValor = int(input("Digite o ultimo valor: "))
incremento = int(input("Digite o incremento: "))

if primeiroValor > segundoValor:
    incremento *= -1


for valor in range(primeiroValor, segundoValor + (1 if incremento > 0 else -1), incremento):
    if (primeiroValor > segundoValor):
        print(valor, end=" ")
    else:
        print(valor, end=" ")
print("Acabou")