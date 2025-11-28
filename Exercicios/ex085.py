nome = []
sexo = []
salario = []
mulheresRicas = []

for i in range(0,5):
    nome.append(input("Digite seu nome: "))
    sexo.append(input("Digite seu sexo [M/F]: ").upper())
    salario.append(float(input("Digite seu salário: ")))

for i in range(5):
    if sexo[i] == "F" and salario[i] > 5000:
        mulheresRicas.append(nome[i])

print("Mulheres ricas:", mulheresRicas)
