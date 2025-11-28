def potencia():
    base = int(input("Digite a base: "))
    expoente = int(input("Digite o expoente: "))

    potencia = base ** expoente
    return print(f"{base} elevado a {expoente} é igual a {potencia}")

potencia()