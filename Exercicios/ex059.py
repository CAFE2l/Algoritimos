maiorIdade = []
HomensCont = 0
mulher = []
mediaHomens = []

while True:
    idade = int(input("Qual a sua idade? "))
    sexo = str(input("Qual o seu sexo? [M/F] ")).upper()
    pergunta = str(input("Quer continuar? [S/N] ")).upper()
    if (pergunta == "N"):
        break
    maiorIdade.append(idade)
    if (sexo == "M"):
        HomensCont += 1
        mediaHomens.append(idade)
    elif (sexo == "F"):
        mulher.append(idade)


velho = max(maiorIdade)
nova = min(mulher)
media = sum(mediaHomens) / len(mediaHomens)


print(f"A maior idade cadastrada foi: {velho}")
print(f"Homens cadastrados foram: {HomensCont}")
print(f"A mulher mais nova tem: {nova}")
print(f"A média de idade dos homens é: {media:.1f}")
