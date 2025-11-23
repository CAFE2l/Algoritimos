# Cria listas vazias para armazenar os dados dos alunos
nome = []
nota1 = []
nota2 = []
media = []

# Lê os dados de cada aluno e calcula a média individual
for i in range(1, 5):
    nome.append(input(f"Digite o nome do {i}º aluno: "))           # Adiciona o nome na lista
    nota1.append(float(input(f"Digite a primeira nota do {i}º aluno: ")))  # Adiciona a primeira nota
    nota2.append(float(input(f"Digite a segunda nota do {i}º aluno: ")))   # Adiciona a segunda nota
    media.append((nota1[i-1] + nota2[i-1]) / 2)                   # Calcula e adiciona a média individual

# Calcula a média da turma somando todas as médias e dividindo pelo número de alunos
media_turma = sum(media) / len(media)

# Lista alunos acima da média da turma
alunos_acima_media = []
for i in range(0, 4):
    print(f"Aluno {nome[i]:15} {media[i]:.1f}")                   # Mostra nome e média de cada aluno
    if media[i] > media_turma:
        alunos_acima_media.append(nome[i])                        # Adiciona nome se estiver acima da média

# Exibe alunos que ficaram acima da média
print(f"Os alunos acima da média ({media_turma:.1f}) foram: {alunos_acima_media}")

# Mostra a média geral da turma
print(f"Média da turma: {media_turma:.1f}")
