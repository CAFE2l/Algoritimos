quantidade = []

while True:
    idade = int(input("Qual a idade do aluno? "))
    if (idade == 999):
        break
    quantidade.append(idade)


totAlunos = len(quantidade)
media = sum(quantidade) / len(quantidade)

print(f"A quantidade de pessoas na sala foi de {totAlunos}")
print(f"A média de idade da turma foi {media:.1f}")