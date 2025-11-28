def maior():
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))
    num3 = int(input("Digite o terceiro valor: "))

    if num1 > num2 and num1 > num3:
        return print(f"{num1} é maior que {num2} e {num3}")
    elif num2 > num1 and num2 > num3:
        return print(f"{num2} é maior que {num1} e {num3}")
    elif num3 > num1 and num3 > num2:
        return print(f"{num3} é maior que {num1} e {num2}")
    else:
        return print(f"{num1} é igual a {num2} e {num3}")

maior()