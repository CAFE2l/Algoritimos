primeiroValor = int(input("Digite o primeiro valor: "))
segundoValor = int(input("Digite o ultimo valor: "))
incremento = int(input("Digite o incremento: "))

for valor in range(primeiroValor, segundoValor+1, incremento):
    print(valor, end=" ")
print("Acabou")