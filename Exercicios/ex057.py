
totHomens = []
totMulheres = []

while True: 
    salario = float(input("Qual o seu salário? "))
    sexo = str(input("Qual o seu sexo [M/F]? ")).upper()
    if (sexo == "M"):
        totHomens.append(salario)
    elif (sexo == "F"):
        totMulheres.append(salario)


    pergunta = str(input("Quer continuar? [S/N] ")).upper()
    if (pergunta == "N"):
        break

somaH = sum(totHomens)
somaM = sum(totMulheres)

print(f"O total pago a homens deve ser R${somaH:.2f}")
print(f"O total pago a mulheres deve ser R${somaM:.2f}")