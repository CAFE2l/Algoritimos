homens = 0
mulheres = 0 
mulheres20 = 0 
for i in range(0, 5):
    idade = int(input("Qual a sua idade? "))
    sexo = str(input("Qual o seu sexo? [M/F] ")).upper()
    if (sexo == "M"):
        homens += 1
    elif (sexo == "F"):
        mulheres += 1
    elif (sexo == "F" and idade > 20):
        mulheres20 += 1
    elif (sexo == "M"):
        mediaIdadeHomens = idade / homens

media_idade = sum(i) / len(i)

print(f"foram cadastrados: {homens} homens")
print(f"foram cadastrados: {mulheres} mulheres")
print(f"foram cadastrados: {mulheres20} mulheres com mais de 20 anos")
print(f"A média de idade dos homens é: {mediaIdadeHomens}")
print(f"A média de idade das pessoas é: {media_idade}")
print("Acabou")