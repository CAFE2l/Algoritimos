vetor = []
mais25 = []
for i in range(1,8):
    idade = int(input(f"Digite a idade da {i}ª pessoa: "))
    vetor.append(idade)
    if (idade > 25):
        mais25.append(i-1)


media = sum(vetor) / len(vetor)
maior = max(vetor)
print(f"As pessoas que são maiores de 25 anos foram encontradas na posição: {mais25}")
print(f"A média das pessoas cadastradas foram: {media:.1f}")
print(f"A maior idade cadastrada foi: {maior} na posição {vetor.index(maior)}")