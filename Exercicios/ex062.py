totIdade = 0
mediaIdade = []
mais21=[]
while True:
    idade = int(input("Qual a sua idade? "))
    mediaIdade.append(idade)
    totIdade += 1
    if(idade > 21):
        mais21.append(idade)
    media = sum(mediaIdade) / len(mediaIdade)
    pergunta = str(input("Quer continuar? [S/N] ")).upper()
    if (pergunta == "N"):
        break
    
print(f"A média das idades foram: {media:.1f}")
print(f"o total de idades digitadas foram: {totIdade}")
print(f"As pessoas com mais de 21 anos foram: {mais21}")
