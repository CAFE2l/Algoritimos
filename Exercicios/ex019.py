nome = str(input(f"Digite o nome do aluno: "))
nota1 = float(input(f"Digite a primeira nota: "))
nota2 = float(input(f"Digite a segunda nota: "))
media = (nota1 + nota2) / 2
if (media >= 6.5):
    print(f"O aluno {nome} teve um bom aproveitamento com a média de {media:.1f} e esta APROVADO")
else:
    print(f"O aluno {nome} teve um ruim aproveitamento com a média de {media:.1f} e esta REPROVADO")