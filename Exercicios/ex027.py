nota1 = float(input(f"Digite a primeira nota: "))
nota2 = float(input(f"Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if (media <= 4.9):
    print(f"REPROVADO")
elif (media > 5 and media <= 6.9):
    print(f"RECUPERAÇÃO")
else: 
    print("APROVADO")