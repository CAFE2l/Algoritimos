def media():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2
    return print(f"a media da nota1 com a nota2 é de {media:.1f}")

media()