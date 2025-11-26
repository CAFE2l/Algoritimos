media_altura = []
acima90 = 0
altao = 0
baixinho = 0

for i in range(7):
    peso = float(input(f"Digite o peso da {i+1}ª pessoa: "))
    altura = float(input(f"Digite a altura da {i+1}ª pessoa: "))
    media_altura.append(altura)

    if peso > 90:
        acima90 += 1
    if peso < 50 and altura < 1.60:
        baixinho += 1
    if altura > 1.90 and peso > 100:
        altao += 1

media = sum(media_altura) / len(media_altura)

print(f"A média de altura é: {media:.2f}")
print(f"As pessoas que pesam mais de 90kg são: {acima90}")
print(f"As pessoas que pesam menos de 50kg e têm menos de 1.60m são: {baixinho}")
print(f"As pessoas que medem mais de 1.90m e têm mais de 100kg são: {altao}")
