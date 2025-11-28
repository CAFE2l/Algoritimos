def maior():
    num1 = int(input("Digite o primeiro valor: "))
    num2 = int(input("Digite o segundo valor: "))

    if num1 > num2:
       return print(f"{num1} é maior que {num2}")
    elif num2 > num1:
       return print(f"{num2} é maior que {num1}")
    else:
       return print(f"{num1} é igual a {num2}")

maior()