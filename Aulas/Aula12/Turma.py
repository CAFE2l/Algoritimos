nome = []
nota1 = []
nota2 = []
media = []

for i in range(1, 5):
    nome.append(input(f"Digite o nome do {i}º aluno: "))
    nota1.append(float(input(f"Digite a primeira nota do {i}º aluno: ")))
    nota2.append(float(input(f"Digite a segunda nota do {i}º aluno: ")))
    media.append((nota1[i-1] + nota2[i-1]) / 2)

for i in range(1, 5):
    print(f"Aluno {nome[i-1]:15} {media[i-1]:.1f}")