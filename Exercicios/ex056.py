soma = 0

while True: 
    num = int(input("Digite um número para o somatório (ou 1111 para parar): "))
    if num == 1111: 
        break
    soma += num

print(f"A soma dos números foi {soma}")
