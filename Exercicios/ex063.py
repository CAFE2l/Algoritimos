valores = []
valoresPares = 0
while True: 
    num = int(input("Digite um número: "))
    valores.append(num)
    pergunta = input("Quer continuar? [S/N] ").upper()
    if (pergunta == "N"):
        break
    if (num % 2 == 0):
        valoresPares += 1
soma = sum(valores)
media = soma / len(valores)
menor = min(valores)


print(f"A soma dos valores é {soma}")
print(f"A média dos valores é: {media:.1f}")
print(f"O menor valor é: {menor}")
print(f"Os valores pares foram: {valoresPares}")