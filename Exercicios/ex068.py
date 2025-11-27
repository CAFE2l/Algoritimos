maior100 = 0
mulheres = 0 
media = []
maiorPesoHomens = 0
for i in range(0, 8):
    sexo = input("Qual o seu sexo [M/F]? ").upper()
    peso = float(input("Qual o seu peso? "))
    if (sexo == "F"):
        mulheres += 1
    if (sexo == "M" and peso > 100):
        maior100 += 1
    if (sexo == "F"):
        media.append(peso)
    if (sexo == "M"):
        if peso > maiorPesoHomens:
            maiorPesoHomens = peso
            
mediaPeso = sum(media) / len(media)
print(f"A média dee peso entre as mulheres é de {mediaPeso:.1f}")
print(f"Os homens que pesam mais de 100kg são: {maior100}")
print(f"O homem mais pesado teve: {maiorPesoHomens}")
print(f"foram cadastradas {mulheres} mulheres")