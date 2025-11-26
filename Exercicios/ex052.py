menor5 = 0
maior18 = 0
idades = []  # Lista para guardar as idades

for i in range(10):
    idade = int(input(f"Digite a idade da {i+1}ª pessoa: "))
    idades.append(idade)  # Adiciona idade na lista
    if idade < 5:
        menor5 += 1
    if idade > 18:
        maior18 += 1

media = sum(idades) / len(idades)  # Calcula a média correta das idades
maior_idade = max(idades)          # Encontra a maior idade

print(f"A média de idade é {media:.2f}")
print(f"Pessoas com menos de 5 anos: {menor5}")
print(f"Pessoas com mais de 18 anos: {maior18}")
print(f"A maior idade foi {maior_idade}")
