mulheres = []  # Lista guarda (nome, idade) das mulheres
homens = []    # Lista guarda (nome, idade) dos homens
idades = []    # Lista só com as idades de todos

while True:
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    sexo = input("Digite seu sexo [M/F]: ").upper()
    continuar = input("Quer continuar? [S/N]: ").upper()

    idades.append(idade)

    if sexo == "F":
        mulheres.append((nome, idade))
    elif sexo == "M":
        homens.append((nome, idade))

    if continuar == "N":
        break

# Pessoa mais velha de todas
idade_mais_velha = max(idades)
# Procurar quem tem essa idade
for pessoa in mulheres + homens:
    if pessoa[1] == idade_mais_velha:
        nome_mais_velho = pessoa[0]
        break

# Mulher mais jovem
mulher_mais_jovem = min(mulheres, key=lambda x: x[1]) if mulheres else ("Nenhuma", 0)

# Média de idade do grupo
media_idade = sum(idades) / len(idades) if idades else 0

# Homens com mais de 30 anos
homens_mais_30 = sum(1 for _, idade in homens if idade > 30)

# Mulheres com menos de 18 anos
mulheres_menos_18 = sum(1 for _, idade in mulheres if idade < 18)

print(f"O nome da pessoa mais velha é {nome_mais_velho} com {idade_mais_velha} anos")
print(f"A mulher mais jovem é {mulher_mais_jovem[0]} com {mulher_mais_jovem[1]} anos")
print(f"A média de idade do grupo é {media_idade:.2f} anos")
print(f"Quantidade de homens com mais de 30 anos: {homens_mais_30}")
print(f"Quantidade de mulheres com menos de 18 anos: {mulheres_menos_18}")
